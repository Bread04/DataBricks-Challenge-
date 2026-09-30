# Design Thinking Session: DataBricks-Challenge- (DengueRadar)

**Date:** 2026-09-30
**Facilitator:** Bread
**Design Challenge:** Help a community group-chat admin share a trustworthy two-week dengue warning that neighbours read and act on.

**Honesty note:** we have not yet spoken to any user. Everything below marked **[Sourced]** comes from the Deep Recon reports in `_bmad-output/planning-artifacts/research/` or the judge-panel session. Everything marked **[Hypothesis]** is an assumption to test in the real conversation. No quote or observation here comes from a real user.

---

## 🎯 Design Challenge

**What we are exploring:** the last mile of DengueRadar. A forecast only helps if someone in a neighbourhood shares it in a way people trust, understand and act on. Our working idea is that a group-chat admin (an RC volunteer, an MCST council member or an engaged resident) copies a ready-made post into a chat their neighbours already read.

**Primary users**
1. **The admin** who would post it. Their job is to keep the chat useful without causing panic, spreading something wrong or looking like they speak for an authority.
2. **The resident** who receives it, including older residents and people who read another language.

**Constraints**
- Round 1 is slides only, due 6 Oct 11:59pm (team target 4 Oct). No build is required.
- One 15-minute conversation is realistic; a five-to-seven-person test is not.
- We cannot send anything to real people. Data is public and aggregate only.
- Planning areas do not match RC, constituency or MCST boundaries, so the admin must self-select their area.
- No unsourced claims: group-chat use is our observed practice, not yet a sourced fact.

**What success looks like**
- One real conversation whose findings change the mock post or slide 2.
- A mock post the admin says they would post, and that a recipient reads correctly in about ten seconds.
- We learn what would stop an admin from posting, which is our biggest unknown.

**Existing research to build on**
- Deep Recon (30 Sep): the channel is plausible, but no source shows RC or condo chats circulating official notices; NEA already sends current-state alerts via myENV; community messaging has weak, mostly indirect evidence; forwarded-message misinformation is a real risk.
- Judge-panel feedback: an admin will not post something that looks official without a clear source; the post must be short, dated and not alarming; four languages matter.

### Challenge statement

**How might we help a community group-chat admin share a short, sourced, calm two-week dengue warning that neighbours understand and act on, without the admin having to sound like an authority or risk spreading something wrong?**

---

## 👥 EMPATHIZE: Understanding Users

### Methods selected

| Method | Why it fits | Status |
|---|---|---|
| **User Interviews** | The only way to learn what stops an admin from posting | Planned: 15-minute conversation (script in `pitch/round1-outline.md`) |
| **Empathy Mapping** | Organises what we believe so we can spot what we are guessing | Done below, from sources and hypotheses |
| **Journey Mapping** | Shows where in "notice → post → replies" an admin could drop out | Done below, as a hypothesis |

### User Insights

**What the sources say [Sourced]**
- Resident-run neighbourhood Telegram groups exist, from a few hundred to about 10,000 members, with residents volunteering as moderators and members answering each other's questions; residents describe a "kampung spirit" (HardwareZone / Straits Times, Jul 2025).
- Volunteers already carry dengue prevention messages door to door: 5,000 PA grassroots and CERT volunteers joined NEA's SG Clean Ambassadors in 2022 to share B-L-O-C-K and S-A-W tips (NEA, Jul 2022). No source says they use chats for it.
- Forwarded messages spread fast and are often partly wrong: in a 2020 Singapore study, 52.3% of 151 adults forwarded at least one COVID message, and about 14% were heavy forwarders (peer-reviewed, small young sample).
- NEA already alerts people through the myENV app about high mosquito population and clusters near saved locations, but only for people who installed it and set locations; alerts describe the present.
- No source was found on languages used in these chats, on older residents' reliance on them, or on official notices being posted in RC or condo chats.

**What the judge-panel persona said [Sourced, but a simulated persona, not a real user]:** an admin will not post something official-looking without a clear source; wants it short and calm; four languages appear in their chat.

### Key Observations

1. The **admin carries the reputational risk** of what they post, not just the effort. [Hypothesis, supported by the misinformation evidence]
2. Neighbours will **reply with questions** ("is this real?", "what do I do?"), and the admin ends up answering. [Hypothesis]
3. **Our own honest label works against us**: a "student project" source may feel less trustworthy than an official one, but pretending to be official is not an option. [Tension to test]
4. Many people **never see myENV alerts**; chats reach people who did not install anything. [Hypothesis]

### Empathy Map Summary (all [Hypothesis] until the conversation)

**The admin**

| | |
|---|---|
| **Says** | "Where is this from?" · "Is it official?" · "Can it be shorter?" · "I don't want to cause panic." |
| **Thinks** | "If it's wrong, people will blame me." · "Will the aunties and uncles understand it?" · "Is someone else already posting this?" |
| **Does** | Copies and forwards from sources they trust, adds a greeting, sometimes translates, answers replies. |
| **Feels** | Responsible, cautious, wants to help, wary of spamming the chat. |
| **Pains** | Authority and blame, boundary mismatch, replies they can't answer, weekly repetition. |
| **Gains** | Looking helpful, keeping neighbours safe, having something easy to post. |

**The resident**

| | |
|---|---|
| **Says** | "Is this real?" · "What do I do?" · "Why is it in English?" |
| **Thinks** | "Do I need to worry?" · "Who sent this?" |
| **Does** | Skims, forwards to family, ignores long posts. |
| **Feels** | Anxious at a bare "HIGH", numb if posts repeat every week. |
| **Pains** | Jargon, long text, no clear action, stale forwarded messages. |
| **Gains** | One clear thing to do this week. |

### Journey map: the admin (Hypothesis)

`Trigger` (a warning exists for my area) → `Trust check` (where is it from?) → `Fit check` (is this my area? my language?) → `Edit` (add a greeting, adjust tone) → `Post` → `Replies` (questions arrive) → `Follow-up` (next week, again?).

Where they are most likely to drop out: **trust check** (no clear source), **fit check** (estate spans two areas), **replies** (no ready answers) and **follow-up** (weekly fatigue).

---

## 🎨 DEFINE: Frame the Problem

### Point of View Statement

**A community group-chat admin needs a post they can put their name behind, because being wrong or sounding official costs them their neighbours' trust; the difficulty is not typing the message but standing behind it.**

### How Might We Questions

1. How might we make the source and the valid-until date impossible to miss without making the post long?
2. How might we let an admin share a warning without appearing to speak for NEA?
3. How might we keep the tone calm while still worth acting on?
4. How might we give the admin ready answers to the questions neighbours will reply with?
5. How might we work when the admin's estate spans two planning areas?
6. How might we stop weekly posts from becoming noise?
7. How might we serve residents who read Chinese, Malay or Tamil?
8. How might we let an admin check the message in seconds before posting?
9. How might we reach residents who are not in any chat?

### Key Insights

- **The post is a trust product.** Its source line, date and wording matter more than its forecast.
- **The admin's second job is answering replies.** A post without reply-ready answers pushes work onto the admin.
- **Honest labelling is a design choice, not a weakness.** "Student project using NEA data" is truthful; whether it is enough is a testable question.
- **Boundary mismatch and fatigue are both real design problems**, so the admin picks the area and we post only on a change.

### Jobs to be done (admin)

- **Functional:** keep neighbours informed about something that affects them.
- **Emotional:** feel responsible without feeling exposed.
- **Social:** be seen as helpful, not alarmist.

---

## 💡 IDEATE: Generate Solutions

### Selected Methods

Brainstorming (quantity, no judgment), SCAMPER (adapt what we already have), Analogous Inspiration (other notice systems).

### Generated Ideas

1. One-tap copy, WhatsApp and Telegram versions (already planned).
2. **Answer card:** reply-ready one-liners for "Is this official?", "What do I do?", "Should I worry?".
3. A short link to NEA's own page as the trust anchor (only once the link is verified).
4. "Higher than usual" wording with the level second (adopted).
5. A five-line cap on the post.
6. A valid-until date on every post (adopted).
7. A second-language version of each post, speaker-reviewed.
8. **Preview screen** showing the post as neighbours will see it, before copying.
9. A 30-second **pre-post check** (right area? right date?).
10. Pin one "this week's 3 things" message instead of reposting weekly.
11. Post only on a band change (adopted).
12. An optional "did you do your weekly check?" poll in the chat, to close the loop.
13. A phrase bank of calm wording.
14. A printable poster for lift lobbies and noticeboards, for residents not in chats.
15. A short voice-note script for older residents.
16. A small shareable image card in addition to text.
17. A QR code to NEA's page.
18. A "pass it on to your parents" version for families.
19. A hint for admins whose estate straddles two planning areas ("also check [neighbouring area]").
20. Two tiers: Medium = "watch", High = "act this week".
21. An adjustable greeting line ("Hi neighbours").
22. A transparent source line: "DengueRadar, a student project using NEA data".
23. Analogy: **haze and weather advisories** use plain bands, each with a simple action.
24. Analogy: **transport disruption notices** are short, dated and say what to do now.
25. SCAMPER: **Substitute** probabilities with plain words; **Eliminate** numbers; **Adapt** advisory bands; **Combine** post plus poster; **Reverse** the flow by asking neighbours to report a checked spot.

### Top Concepts

1. **The trust-first post:** five lines at most, plain words, a calm "higher than usual", three actions, a date and valid-until, and an honest source line. *Goes on slide 2 as the mock.*
2. **The answer card:** ready replies for the admin. *Test in the conversation; a slide mention only if it lands.*
3. **Preview and pre-post check:** the admin sees what neighbours see and confirms area and date. *Sprint concept, not for the Round 1 slides.*

Stretch: the printable poster for noticeboards.

---

## 🛠️ PROTOTYPE: Make Ideas Tangible

### Prototype approach

Methods: **Paper Prototyping** (two printed mock posts), **Role Playing** (the admin reads a post aloud as they would send it), **Storyboarding** (four frames), and **A/B comparison** of the two variants. Nothing is built or sent. We fake everything except the wording.

### Prototype description

**Variant A (full)** *(illustrative; not a real forecast)*

```
DENGUE FORECAST · [Area] · week of 6 Oct
Next 2 weeks: higher than usual (level HIGH, up from Medium)
Why: heavy rain 2 to 4 weeks ago, now warm; cases rising nearby.
This week:
1. Lift and empty flowerpot plates, overturn pails and wipe rims, change vase water
2. Keep roof gutters clear
3. Use repellent, wear long sleeves and pants
Valid until 19 Oct. Forecast by DengueRadar, a student project using NEA data. Not a diagnosis. Your estate may span another area.
```

**Variant B (short)** *(illustrative)*

```
[Area]: dengue risk higher than usual for the next 2 weeks.
This week: empty flowerpot plates and pails, keep gutters clear, use repellent.
Valid until 19 Oct. Source: NEA data, DengueRadar (student project).
```

**Answer card** *(draft wording; NEA link to be added only once verified)*
- *"Is this official?"* → "No. It's a student forecast built on NEA's public data. NEA's own cluster map has the official picture."
- *"What do I do?"* → "The three steps in the post: empty containers, keep gutters clear, use repellent."
- *"Should I worry?"* → "It's a forecast of higher activity nearby, not a report that anyone is ill."

**Storyboard (four frames):** (1) the admin sees the forecast for their area; (2) previews and picks Variant A or B; (3) posts it in the chat; (4) a neighbour replies, the admin answers from the card, the neighbour does the first step.

### Features to test

- Source wording: "student project using NEA data" against no label.
- "Higher than usual" against a bare "HIGH".
- Length (A against B).
- Whether the valid-until date is noticed.
- Whether the answer card would be used.
- Whether the admin's estate maps to one area.

---

## ✅ TEST: Validate with Users

### Testing plan

**Who:** one group-chat admin (15 minutes), plus, if possible, two or three recipients who read each variant for ten seconds and explain it back (family or friends, including one older person). Small numbers give direction, not proof.

**Tasks and questions**
1. Admin: "Read Variant A, then B. Which would you post, and what would you change?"
2. Admin: "What would stop you posting either?"
3. Admin: "A neighbour replies 'is this official?'. What do you say?" (then show the answer card)
4. Recipient: "In your own words, what is this telling you, and what would you do?"
5. Everyone: "Is the wording calm? Which language would you want?"

**Capture:** a **Feedback Capture Grid** (Likes, Questions, Ideas, Changes). No names, numbers or contact details; ask permission to quote anonymously.

### Assumptions to test (Assumption Testing)

| # | Assumption | What would disprove it |
|---|---|---|
| A1 | An admin will post an unofficial forecast if the source is clear | The admin says they would only forward official notices |
| A2 | "Student project using NEA data" is acceptable | The admin says it makes the post unusable |
| A3 | Recipients understand "higher than usual" | They read it as "someone is ill" or "nothing to do" |
| A4 | Recipients know what to do after reading | They cannot name one action |
| A5 | Admins would post weekly | They say monthly, or only when it's serious |
| A6 | One area fits the admin's estate | Their estate spans two or more areas |

### User Feedback

**Not yet collected.** The conversation has not happened. Do not fill this section with anything other than what a real person said.

| Likes | Questions | Ideas | Changes |
|---|---|---|---|
| _(pending)_ | _(pending)_ | _(pending)_ | _(pending)_ |

### Key Learnings

None yet. Decision rules for when the results arrive:

- If the admin refuses an unofficial source → the design needs an endorsement path (roadmap, and say so on the slide), or a different post framing.
- If recipients misread "higher than usual" → change the wording before it goes on a slide.
- If the estate spans several areas → keep the multi-area picker in the design and mention it.
- If the admin says weekly is too often → post only on a change, and drop the weekly claim.
- If the admin would post it as is → use their one-sentence quote on slide 2.

---

## 🚀 NEXT ITERATION

### Refinements

- Update the mock post and slide 2 with whatever the real conversation changes.
- Choose Variant A or B for the slide mock, based on the admin's and recipients' reactions.
- Decide whether the source line stays as "student project using NEA data".

### Action Items

1. **Have the conversation** with one admin, by 2 Oct. Anyone on the team who knows one.
2. Print or screenshot Variant A, Variant B and the answer card to use in the conversation.
3. If possible, show both variants to two or three recipients and ask them to explain each in their own words.
4. Apply the findings to `pitch/round1-outline.md` (mock post, slide 2, field-check line) by 3 Oct.
5. If no conversation happens, remove the field-check slot and keep "proposed channel" wording.

### Success Metrics

- **Round 1:** one real admin conversation informs the mock post; the slide 2 mock is the version an admin said they'd post; nothing on the slide claims more than we learned.
- **If shortlisted:** an admin can copy a post in one tap; a first-time reader explains it correctly in ten seconds; the answer card covers the replies an admin actually got.
