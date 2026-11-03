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
- Check interpretation: Pending.
- Browser observation: Pending.
- Keep decision: Pending.
- Review: Learner confirmed the prediction excerpt is accurate.
- Help/gaps: AI explained that `/api/me` answers with data (401 error vs. account info), while the logged-out call to action belongs on the browser page `/dashboard`.
- Evidence links / next step: Issue [#3](https://github.com/mcbridgeee/is373-app-studio/issues/3), branch `app-002-accounts`; plan and build next.

## APP-003

- Prediction: Pending.
- Check interpretation: Pending.
- Browser observation: Pending.
- Keep decision: Pending.
- Review: Pending.
- Help/gaps: Pending.
- Evidence links / next step: Keep APP-002 before agreeing this lesson.
