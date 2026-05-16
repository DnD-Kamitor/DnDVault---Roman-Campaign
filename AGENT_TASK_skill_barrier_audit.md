# Agent Task: Skill Barrier Format Audit

## What this project is

A D&D 5e campaign book written in Quarto Markdown, published at:
https://dnd-kamitor.github.io/DnDVault---Roman-Campaign/

The book uses a three-tier knowledge gate system. The format of these gates is currently wrong in several files and needs to be fixed.

---

## The format rule — READ THIS CAREFULLY

There are three types of knowledge gates:

### Tier 1 — Open text (no gate)
Everyone knows this. Lives in the main section body. No special formatting needed.

### Tier 2 — Passive stat/proficiency gate
The player either has the stat/proficiency or they don't. No roll required.

**Correct format:**
```
**History proficiency** — Description of what you know
**Wisdom 14+** — Description of what you know
**Strength 14+** — Description of what you know
```

**Wrong format (fix these):**
```
*History proficiency:* Description    ← old style, fix to bold dash
*Wisdom 14 or higher:* Description   ← fix to "14+" and bold dash
```

### Tier 3 — Active DC check (collapsible)
A real dice roll, only triggered by specific player actions. Must include: the ability score, the skill in parentheses, and a trigger phrase.

**Correct format:**
```html
<details>
<summary><strong>DC 13 Intelligence (History) — Recalling [specific topic]</strong></summary>
Content here.
</details>
```

**Wrong format (fix these):**
```html
<summary><strong>DC 13 — What any soldier knows</strong></summary>    ← no skill, no trigger
<summary><strong>DC 15 — What a veteran knows</strong></summary>      ← no skill, no trigger
```

A bare `DC 13` with no skill name is **meaningless at the table**. Always include `Ability (Skill) — trigger phrase`.

---

## Files already fixed — DO NOT TOUCH

- `knowledge.qmd` — fully fixed, all 45 DC headers updated, all "without a check" bullets reformatted

---

## Files that need fixing

Work through these one at a time:

1. `chapter1.qmd`
2. `chapter2.qmd`
3. `chapter3.qmd`
4. `chapter4.qmd`
5. `chapter5.qmd`
6. `roles.qmd`
7. `roman_tactics.qmd`

---

## What to look for in chapter files

The chapter files have DC checks in two places:

**A) Skill audit tables** — tables with columns like `DC | Skill | Trigger | What they learn`. These are usually already in correct format. Check that the skill column is filled in and the trigger is specific.

**B) Scene descriptions** — inline text like:
- `"DC 15 History check"` — needs to be `"DC 15 Intelligence (History) check — triggered when [X]"`
- `"DC 13"` alone — needs skill and trigger
- `"DC 17 Insight"` — needs the ability score: `"DC 17 Wisdom (Insight)"`

**C) Collapsible blocks** — same `<details><summary>` format as knowledge.qmd. Apply the same fix.

---

## What to look for in roles.qmd and roman_tactics.qmd

These files also use collapsible knowledge sections. Apply the same DC header fix:
- `DC 13 — What [X] knows` → `DC 13 Ability (Skill) — Recalling [specific topic]`

Use context from the content inside the collapsible to determine the correct ability and skill. Examples:
- Military knowledge → `Intelligence (History)`
- Tactical knowledge → `Intelligence (History)` or `Wisdom (Survival)`
- Religious knowledge → `Intelligence (Religion)` or `Wisdom (Insight)`
- Nature/flora → `Intelligence (Nature)`
- Political knowledge → `Intelligence (History)`
- Reading people → `Wisdom (Insight)`
- Medical → `Wisdom (Medicine)`
- Social/persuasion → `Charisma (Persuasion)`

---

## Workflow

For each file:
1. Read the full file
2. Find all `DC [number]` occurrences
3. Check each one: does it have `Ability (Skill) — trigger`? If not, fix it.
4. Find all "without a check" bullet points using `*italic:*` format — reformat to `**bold** —`
5. Write the fixed file back using Edit (not Write — use targeted edits to avoid clobbering other content)
6. Move to the next file

---

## Style rules (do not violate)

- No em dashes (--) in prose. Use colon, semicolon, or comma. Exception: the ` — ` separator in the gate format IS correct (it's a formatting separator, not prose)
- No AI attribution anywhere in content files
- Latin words stay italicised in prose
- Do not change any content — only fix the gate format labels
- Do not add or remove whole sections

---

## When done

Report which files were changed and approximately how many DC headers and bullet points were fixed per file.
