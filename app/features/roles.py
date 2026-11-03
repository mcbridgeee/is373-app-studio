"""APP-003 roles: the server checks the current database role on every request."""

from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse

from app import security
from app.database import connect

router = APIRouter()


def _accounts(settings):
    """Read-only list of usernames and roles; never ids, hashes or sessions."""
    with connect(settings) as connection:
        rows = connection.execute(
            "SELECT username, role FROM users ORDER BY username"
        ).fetchall()
    return [{"username": row["username"], "role": row["role"]} for row in rows]


@router.get("/api/admin")
def api_admin(
    request: Request, _admin: Annotated[dict, Depends(security.require_admin)]
):
    """Anonymous → 401, member → 403, admin → 200 with the account list."""
    return {"accounts": _accounts(request.app.state.settings)}


@router.get("/admin", include_in_schema=False)
def admin_page(request: Request):
    """The same boundary for a typed URL: hiding the nav link is not the check."""
    user = security.authenticate(request)
    if user is None:
        return RedirectResponse("/login", status_code=303)
    templates = request.app.state.templates
    if user["role"] != "admin":
        return templates.TemplateResponse(
            request=request,
            name="admin.html",
            context={"denied": True},
            status_code=403,
        )
    return templates.TemplateResponse(
        request=request,
        name="admin.html",
        context={"denied": False, "accounts": _accounts(request.app.state.settings)},
    )
