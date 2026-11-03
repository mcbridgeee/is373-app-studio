"""APP-002 accounts: the JSON API and browser forms share prepared security helpers."""

import re
from typing import Annotated

from fastapi import APIRouter, Depends, Form, Header, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from pydantic import ValidationError

from app import security
from app.schemas import LoginInput, PublicUser, SignupInput

router = APIRouter()
PUBLIC_FIELDS = ("id", "username", "role")
USERNAME_PATTERN = re.compile(r"[a-z0-9_]{3,32}")
CsrfHeader = Annotated[str | None, Header()]
FormText = Annotated[str, Form()]


def _public(user):
    """Return identity only, never a password hash or session identifier."""
    return {key: user[key] for key in PUBLIC_FIELDS}


def _valid_username(value):
    """Echo a username back into a form only when it is already a valid identity."""
    normalized = value.strip().lower()
    return normalized if USERNAME_PATTERN.fullmatch(normalized) else ""


def _signup_problem(error):
    """Turn a validation failure into one plain sentence without echoing input."""
    fields = {str(item["loc"][0]) for item in error.errors() if item["loc"]}
    if "username" in fields:
        return "Use 3–32 letters, numbers or underscores for your username."
    return "Use a password between 15 and 128 characters."


def _page(request, name, status_code=200, **context):
    """Render a form page with a CSRF token and the session cookie it belongs to."""
    cookies = Response()
    context["csrf_token"] = security.csrf_token(request, cookies)
    page = request.app.state.templates.TemplateResponse(
        request=request, name=name, context=context, status_code=status_code
    )
    for value in cookies.headers.getlist("set-cookie"):
        page.headers.append("set-cookie", value)
    return page


@router.get("/api/csrf")
def api_csrf(request: Request, response: Response):
    """Start a pre-login session so signup and login are CSRF-protected too."""
    return {"csrf_token": security.csrf_token(request, response)}


@router.post("/api/signup", status_code=201, response_model=PublicUser)
def api_signup(
    request: Request, credentials: SignupInput, x_csrf_token: CsrfHeader = None
):
    """Create a member; the input model rejects any role or extra field."""
    security.require_csrf(request, x_csrf_token)
    security.limit_signup(request)
    return security.signup(
        request.app.state.settings, credentials.username, credentials.password
    )


@router.post("/api/login", response_model=PublicUser)
def api_login(
    request: Request,
    response: Response,
    credentials: LoginInput,
    x_csrf_token: CsrfHeader = None,
):
    """Set the HttpOnly session cookie; the JSON body never carries the token."""
    security.require_csrf(request, x_csrf_token)
    return security.login(request, response, credentials.username, credentials.password)


@router.get("/api/me", response_model=PublicUser)
def api_me(user: Annotated[dict, Depends(security.require_user)]):
    """401 before login; the current account after login."""
    return _public(user)


@router.post("/api/logout")
def api_logout(request: Request, response: Response, x_csrf_token: CsrfHeader = None):
    """Revoke the session on the server, not only the cookie in this browser."""
    security.require_csrf(request, x_csrf_token)
    security.logout(request, response)
    return {"detail": "You are logged out."}


@router.get("/signup", include_in_schema=False)
def signup_form(request: Request):
    """Show the signup form."""
    return _page(request, "signup.html")


@router.post("/signup", include_in_schema=False)
def signup_submit(
    request: Request,
    username: FormText = "",
    password: FormText = "",
    csrf_token: FormText = "",
):
    """Create a member, then send them to log in."""
    try:
        security.require_csrf(request, csrf_token)
        security.limit_signup(request)
    except HTTPException as error:
        return _page(request, "signup.html", error.status_code, error=error.detail)
    try:
        credentials = SignupInput(username=username, password=password)
    except ValidationError as error:
        return _page(
            request,
            "signup.html",
            422,
            error=_signup_problem(error),
            username=_valid_username(username),
        )
    try:
        security.signup(
            request.app.state.settings, credentials.username, credentials.password
        )
    except HTTPException as error:
        return _page(
            request,
            "signup.html",
            error.status_code,
            error=error.detail,
            username=credentials.username,
        )
    return RedirectResponse("/login", status_code=303)


@router.get("/login", include_in_schema=False)
def login_form(request: Request):
    """Show the login form."""
    return _page(request, "login.html")


@router.post("/login", include_in_schema=False)
def login_submit(
    request: Request,
    username: FormText = "",
    password: FormText = "",
    csrf_token: FormText = "",
):
    """Log in and go to the dashboard, or show one generic error."""
    try:
        security.require_csrf(request, csrf_token)
    except HTTPException as error:
        return _page(request, "login.html", error.status_code, error=error.detail)
    try:
        credentials = LoginInput(username=username, password=password)
    except ValidationError:
        return _page(
            request,
            "login.html",
            422,
            error="Enter your username and password.",
            username=_valid_username(username),
        )
    redirect = RedirectResponse("/dashboard", status_code=303)
    try:
        security.login(request, redirect, credentials.username, credentials.password)
    except HTTPException as error:
        return _page(
            request,
            "login.html",
            error.status_code,
            error=error.detail,
            username=_valid_username(credentials.username),
        )
    return redirect


@router.get("/dashboard", include_in_schema=False)
def dashboard(request: Request):
    """The private member space; anonymous visitors are sent to log in."""
    user = security.authenticate(request)
    if user is None:
        return RedirectResponse("/login", status_code=303)
    return _page(request, "dashboard.html", user=_public(user))


@router.post("/logout", include_in_schema=False)
def logout_submit(request: Request, csrf_token: FormText = ""):
    """Revoke the session, then return to the homepage."""
    try:
        security.require_csrf(request, csrf_token)
    except HTTPException as error:
        user = security.authenticate(request)
        if user is None:
            return RedirectResponse("/login", status_code=303)
        return _page(
            request,
            "dashboard.html",
            error.status_code,
            user=_public(user),
            error=error.detail,
        )
    redirect = RedirectResponse("/", status_code=303)
    security.logout(request, redirect)
    return redirect
