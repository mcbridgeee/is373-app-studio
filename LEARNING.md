# Conversation evidence

AI-drafted task summary, not a transcript or grade. It may be public. Use actual
short words or labeled paraphrases; disclose help and leave missing responses
pending. The learner reviews, corrects or removes new excerpts before commit/push.
Accuracy approval is not proof of understanding. Label simulated trials explicitly.

**Available conversation context:** One local coaching chat, from the SSH clone onward (November 2, 2026).

## APP-001

- Prediction: "i am intentionally choosing the archetype sage, and the warm, bookish feel to be calming to users." Expects the design to feel "aesthetic", "matcha", "reading in bed", "cup of tea", "plant on my desk", while staying "an aesthetic, low pressure choice for learning vocabulary, feeling personal and smart/wise to use"; "not flashy, not in your face, and doesn't feel like it's bombarding you."
- Check interpretation: On `test_chosen_brand_reaches_the_homepage`: "this test would not test the fonts, and this test would catch if the html formatting was off (no <h1>), if there was no svg, and it would catch if the words "your project" is on the page"
- Browser observation: "the nav bar looks really great, the svg logo alongside the wordmark looks great. the color palette is good, and it looks good on mobile." Also noticed that the "see how it works" button "may not contrast strongly enough."
- Keep decision: Keep the sage button: "it suits the overall look well and vibe of the app ... it is a clear button, and the only button, on the page for the user to click, so for now it does its job." Learner was unsure how much the text contrast matters.
- Review: Learner read the full APP-001 record and confirmed it accurate before the first push (November 3, 2026).
- Help/gaps: AI ran setup and the foundation check, checked the scope against the APP-001 tests, and created issue #1 from the learner's approved wording. Learner added mobile-first to the scope. Learner supplied the app idea, visitor, Sage archetype, promise and six original logo SVGs; AI saved the SVGs into the project. Learner's reason for the look: "the soft sage and cream colors and bookish serif font make it feel like reading at home, not like a study app pushing you." Learner chose all-lowercase text, skipped dark mode and approved the AI's build plan; the headline, voice words and section copy were AI suggestions the learner accepted with the plan. AI built the page and fonts, and found and fixed the logo still animating under reduced motion. Learner noticed the fonts were not showing (cached stylesheet, fixed by a hard refresh) and asked for the logo to be centered and improved; AI fixed a 33px off-center offset, enlarged the logo and added a soft glow.
- Evidence links / next step: Onboarding, on the neutral page: "its a full website page, and that none of the buttons work yet. and for a shell it has good typographic hierarchy." Issue [#1](https://github.com/mcbridgeee/is373-app-studio/issues/1), branch `app-001-homepage`, PR [#2](https://github.com/mcbridgeee/is373-app-studio/pull/2), merged after both CI jobs passed; issue #1 closed. Learner decided to merge after reviewing the CI results.

## APP-002

- Prediction: Learner predicted that a logged-out request to `/api/me` should get a signup page, or an error saying they aren't logged in with a clear call to create an account or log in.
- Check interpretation: On `test_logout_revokes_a_copied_token_and_get_does_not_log_out`, after one hint, asked what a 200 in place of 401 would mean: "i dont know, i think it would just return a different error". Not yet evidenced: what the replay check protects against.
- Browser observation: Signed up, logged in and out: "it catches if you have enough characters in your password", logging in "takes you to the screen with all your information, and logging out logs you out", and "if you try to go to / dashboard while logged out it gives no error just takes you to the sign in page." Learner's concern: "i don't think it's secure, and i dont think it can sense if someone is trying to break in or hack your account."
- Keep decision: Keep: "it does the flow we wanted it to and is aligned to specs and the agreed upon plan and scope".
- Review: Learner confirmed the prediction excerpt, then the check answer, browser observation, keep reason and help notes, as accurate before the APP-002 push.
- Help/gaps: AI explained that `/api/me` answers with data (401 error vs. account info), while the logged-out call to action belongs on the browser page `/dashboard`. Learner chose to keep only the lesson's required scope, dropping the signup date and word-list area. AI built the API routes, forms and dashboard with the prepared security helpers, and fixed buttons that were not displaying lowercase. After the learner's check answer, AI explained that a 200 would mean a copied cookie still works after logout, so someone holding it would stay logged in as the learner; AI also explained the existing login throttling and what the app does not detect. Learner then asked to revise the cookies so a copied cookie cannot keep someone logged in; AI showed this is already what the replay check proves (logout revokes the session on the server; sessions also expire after 15 minutes), so no code changed.
- Evidence links / next step: Issue [#3](https://github.com/mcbridgeee/is373-app-studio/issues/3), branch `app-002-accounts`, PR [#4](https://github.com/mcbridgeee/is373-app-studio/pull/4), merged after both CI jobs passed; issue #3 closed. Learner decided to merge after reviewing the CI results.

## APP-003

- Prediction: If a logged-in member without admin permission types `/api/admin` directly: "they should be shown that they have no access".
- Check interpretation: For `test_a_role_claim_cannot_override_the_current_database_role`: "if the code trusted the role in the cookie instead of checking the database, anyone can make themselves admin by editing their cookie." The learner expects the test would then fail because `/api/admin` would return 200 instead of 403.
- Browser observation: Learner made two throwaway accounts and promoted one with the terminal role command. Logged in as the admin: "i can see everyones accounts." After removing admin and reloading: "it just gives the same warning from before, that admin access is required."
- Keep decision: Keep, because "it does what was agreed upon in scope, and everything is working as it should".
- Review: Learner confirmed the prediction, check answer, browser observation, keep reason and help notes as accurate before the APP-003 push.
- Help/gaps: Learner confirmed the scope sticks to the lesson's requirements and chose the read-only account list as the admin result. AI built the admin API and page with the prepared `require_admin` check and reviewed member and admin access on a throwaway database. After the browser try, the learner asked whether an admin can delete accounts or recover passwords; AI explained these are outside the agreed read-only scope and that roles change only through the terminal command.
- Evidence links / next step: Issue [#5](https://github.com/mcbridgeee/is373-app-studio/issues/5), branch `app-003-roles`, PR [#6](https://github.com/mcbridgeee/is373-app-studio/pull/6), merged after both CI jobs passed; issue #5 closed. Learner decided to merge after reviewing the CI results.
