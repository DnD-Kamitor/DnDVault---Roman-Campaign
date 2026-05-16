# Agent Task: Session 1 — Vault Redesign and Depth Pass

## What this project is

A D&D 5e campaign book written in Quarto Markdown, published at:
https://dnd-kamitor.github.io/DnDVault---Roman-Campaign/

The file `chapter1.qmd` contains Session 1: Blood and Omens. The session has a good cold open and strong atmosphere, but the vault is fully linear, combat is trivially easy for adult players (2 CR 1 creatures + 1 CR 2), there are no real puzzles or hidden content, and the party has no meaningful choices about how to navigate the space.

**Goal:** Rework the vault section to be deeper, more dangerous, and more rewarding to explore. Target audience: mixed group of adult D&D players, experienced and newer. They want real difficulty, real story, and moments they will remember.

---

## Files to modify

- `chapter1.qmd` — the only file you touch

## Files NOT to touch

- `knowledge.qmd`, `roman_tactics.qmd`, `supplies.qmd`, `roles.qmd` — do not touch

---

## What to preserve unchanged

**Keep exactly as written:**
- The Session Overview, Guy Sclanders' Principles section
- Pre-Session Preparation (props, handouts, maps tables)
- Scene 0: Cold Open (the shared dream + principia briefing) — do not change a word
- Scene 1: Meeting the Legate — keep as written
- The Conclusion section
- The DM Notes section (OGAS, refusal contingency, corruption mechanic, Aquilifer vacancy, commendationes, optional encounters)
- The Skill Audit section at the end

**Modify:**
- Scene 2: Descent into the Ruins — expand and add the branching vault layout
- Scene 3: The Spear — expand with upgraded combat and spear reveal
- Scene 4: Return to the Surface — expand combat encounter

---

## The redesigned vault

### Overview

The current vault is a single linear corridor:
`Shaft → Chamber 1 (Shields) → Chamber 2 (Chains) → Chamber 3 (Altar)`

Replace this with a branching structure. Both branches are available from the beginning. They teach the players different things and feed different kinds of player — the combat-forward player and the lore/exploration player. Both paths merge before the altar.

**New vault map (text representation):**

```
SHAFT (40 ft descent)
   |
ENTRANCE PASSAGE (short tunnel, smell of metal + old water)
   |
T-JUNCTION
  /          \
LEFT BRANCH   RIGHT BRANCH
(Shield Hall  (Flooded Gallery
 + hidden      + Bone Chamber)
 alcove)
   |               |
   +----- BINDING CHAMBER -----+
                |
         RUNIC CORRIDOR (puzzle)
                |
         ALTAR CHAMBER (boss combat)
```

The T-junction is clearly visible. Neither passage is blocked. Players choose.

---

### Scene 2: Descent and the Vault

#### The Shaft

Keep the existing shaft description. Add one detail:

At the bottom of the ladder, before the passage begins, scratched into the clay wall at knee height where a man crouching would see it:

> *Seven scratches in a vertical line. Then one diagonal line through all seven. A Roman numeral countdown to zero. Beside it, a single word in Latin: NOLITE.*
> *(Do not.)*

This was left by a previous work crew member. It is not a puzzle — it is a warning that the players are free to interpret however they like.

---

#### The Entrance Passage

> *The passage runs straight for forty feet. Narrow, low, cut through earth reinforced with stone slabs that look Roman at the top and Germanic at the bottom — two construction eras meeting unevenly in the walls. The air has no direction; it simply sits, heavy and cold, with a mineral smell underneath something organic that you cannot place.*
>
> *Fifteen feet in, a Roman pick lies abandoned on the floor. It is not rusted. The handle is broken, not decayed. Someone dropped this recently and left without it. The head is pointed in the direction you came from.*

Perception DC 10 (passive): The pick is pointed back toward the shaft — the direction of retreat, not work. Whoever dropped it was running.

At the far end, the passage opens into a T-junction. Left passage: warmer air, dry stone. Right passage: colder air, the sound of slow water somewhere below the floor.

---

### LEFT BRANCH: The Shield Hall and Hidden Alcove

#### The Shield Hall (existing Chamber 1 — keep all content)

Preserve the existing read-aloud text and all skill checks for the Shield Hall exactly as written.

**Add one discovery at the end of the Shield Hall** — a hidden alcove:

After the existing Shield Hall content, add:

> *At the far end of the hall, where the archway leads onward, there is a slight wrongness in the wall to the left. Not a gap — the stones are continuous. But one shield has been hung with its face to the wall rather than facing the room.*

Investigation DC 15 (active: examining the backwards shield):
On success: the shield conceals a narrow gap, not a door — a deliberate crack in the stone, widened by hand tools. Inside, wrapped in badly degraded cloth, three objects: a Roman wax tablet, a Germanic carved bone token, and a bronze stylus.

The wax tablet is partially legible (DC 12 Intelligence to read the damaged Latin):
*"Third watch. If you are reading this, the garrison has not come back. The chains held for three hundred years. They held because we honored the bargain. Corvinus knows nothing of the bargain. That is why the dogs are dead. Warn the—"*
The rest is obliterated. The last word before obliteration may have been *augur* or *augurem* (players must decide).

The bone token is carved with a Germanic rune: OTHALAN (ancestral land). This is the same rune from the altar inscription. A character with Religion DC 13 (passive) or History DC 13 (passive) recognizes it as a marker of formal agreement — a contract token. Two parties held tokens like this to seal a bargain. This is one half. The other half is presumably still at the altar.

**This discovery is the three-clue rule in action.** It implies: there was a bargain between whoever sealed the vault and whoever guards it. The bargain has been broken (Corvinus's excavation). The violation caused the deaths. Cassia knows something about this (she is one of the three routes to the full truth). The party now has evidence before they reach the altar.

No combat in this branch until the Binding Chamber.

---

### RIGHT BRANCH: The Flooded Gallery and Bone Chamber

#### The Flooded Gallery

> *The right passage descends on a shallow grade. Within twenty feet the floor becomes wet, then ankle-deep water, then — at the low point — chest-deep water that stretches for thirty feet before rising again on the far side. The water is black and cold and does not move. The ceiling is three feet above the waterline at the deepest point. You can wade upright, but you will be chest-deep in ancient standing water that smells of peat and something faintly sweet that you do not want to identify.*

**Navigating the flooded section:**
- Athletics DC 11 (active: wading through carefully without making noise): success means silent passage; failure means splashing that echoes.
- Three **Shadows** lurk in the water. They are not aggressive by default — they are drawn to light and sound. Characters carrying torches draw them. Characters who extinguish light sources and move quietly (Stealth DC 14 group check) can pass without triggering combat.
- If combat is triggered: Shadows (CR 1/2, 3 of them). They have advantage on attack rolls in dim light. The flooded gallery is dim light at best with torches. This fight is genuinely dangerous at Level 3 — wading through knee-to-chest-deep water costs half movement, and Shadows drain Strength on a hit.
- DM note: If the party triggers combat here without preparation, they will feel it. If they think their way through (extinguish torches, move quietly), they pass for free. This is the skill check combat of the vault — rewarding players who think rather than just swing.

**What is in the flooded gallery:**
At the far wall, propped against the stone half-submerged, is a Germanic warrior's body — preserved in the peat water for centuries. He is armored. He is not undead. He is simply preserved.

Investigation DC 12 (active: examining the body): He was not killed by violence. He sat down, crossed his arms, and died here deliberately. His equipment is intact. A framea (Germanic spear, full 5e stats in roman_tactics.qmd) lies across his lap. A bone token hangs at his throat — carved with OTHALAN, the same rune as the one in the hidden alcove.

If a character takes the framea: it functions as a normal spear, but it is clearly Germanic craftsmanship and will be recognized by anyone with History DC 13 as pre-Roman Germanic work. Cassia will want to see it in Session 2.

If a character disturbs the body disrespectfully (taking the bone token, moving the body without ceremony): one Shadow reactivates in the water behind them. No warning. It simply appears.

Religion DC 14 (active: observing the body in context): This man is in the position of a *seiðr* death — voluntary, directed, purposeful. He did not die defending this place. He died completing a duty to it. This is the second half of the contract. The bone token confirms it: he is the Germanic party to the same bargain referenced in the wax tablet.

---

#### The Bone Chamber

Beyond the flooded gallery, the passage opens into a wider chamber with a collapsed section of ceiling on the east wall.

> *The chamber is wide and low — a natural cave that the builders worked into the structure without fully finishing. Loose stone fills one wall where the ceiling has given way. The rubble is old but not ancient: something heavy fell here, or something heavy was moved.*
>
> *Three stone benches line the far wall, each bearing the remains of what was once equipment — corroded, age-rotted, unidentifiable as anything specific. The chamber smells more strongly of organic decay than anywhere else in the vault.*

**Encounter: 2 Ghouls (CR 1 each) + 1 Ghast (CR 2)**

The ghouls are beneath the rubble, dormant, waiting. They activate when the party is fully in the chamber (not when they first enter the archway — give them one round of looking around before the rubble shifts).

The Ghast emerges last, from behind the stone benches where it has been pressed against the wall for centuries.

**XP calculation:** 200 + 200 + 450 = 850 × 2 (multiplier for 3 creatures) = 1,020 XP for a 4-player party. This exceeds the Hard threshold (900 XP) for Level 3 characters. It is Hard. Players who entered this branch by choosing the flooded gallery have already spent resources; this fight hits at the wrong time if they weren't careful.

**Tactical notes:**
- Ghouls use Claws to try to Paralyze before the Ghast closes — coordinated, though mindless.
- The Ghast's Stench aura (DC 10 Con save or poisoned until start of next turn) applies as soon as it emerges, affecting characters before they have had a turn.
- The low ceiling and stone benches create three-quarters cover options. Characters can use the benches. The ghouls can too.
- If a character is Paralyzed by a Ghoul and the Ghast attacks them: the Ghast gets advantage plus automatic critical. This is not accidental. It is designed to be frightening.
- **Escape route:** The passage back through the flooded gallery is always available. Retreating is a legitimate choice. The Shadows in the gallery do not re-activate for retreating characters who are moving loudly — they are drawn to noise but they already assessed the party as not-prey when they passed.

**After the combat:**
Investigation DC 12 (active: searching the chamber): beneath the stone benches, a clay vessel intact, containing carbonized grain and a small iron coin struck with a face that is clearly Mars but pre-Roman in style — older than the empire. This is a ritual offering. The offering was being maintained actively until very recently. Someone has been feeding this place.

---

### THE BINDING CHAMBER (replaces old Chamber 2)

Both branches converge here. The chamber is as currently written — the chains, the TIWAZ rune, the Latin inscription "We turned back here." Keep all existing read-aloud text and skill checks.

**Add a puzzle element to this chamber:**

The chains are not random decoration. They form a functional lock. One chain is visually different: it runs from the ceiling through a ring sunk into the floor, and it has a shaped iron grip at waist height instead of a bare link.

After the party enters and begins examining the chains:

Investigation DC 14 (active: studying the chain arrangement as a system rather than as individual chains):
On success: the chains are arranged in a deliberate pattern radiating from the central floor ring. They read as a mechanism. The central chain is the key. The order in which the outer chains were last touched (visible in the oxidation patterns on the links) tells you the sequence — three outer chains, handled in a specific order, then the central chain pulled.

If a character pulls the central chain without the sequence:
DC 13 Strength saving throw or be restrained for 1 minute (chains snap to wrist or ankle automatically). The restrained character can break free with DC 16 Athletics or be cut free with a bladed weapon (cutting through iron requires dealing 10 damage to the chain with a slashing weapon). No damage — just restraint and wasted time and noise.

If a character follows the sequence and pulls the central chain:
> *The chain does not fight back. It comes free of the floor ring with the clean sound of a mechanism that has been waiting to be operated correctly. In the wall to your right, a section of stone swings inward on a hidden iron pivot. Cold air and the smell of old cedar wood.*

The hidden alcove contains: a clay oil lamp (still full, Roman manufacture), a scroll wrapped in oilskin (barely legible, but fragments of Latin text describe "the terms of the binding" — this is the contract document. DC 15 Intelligence to read the damaged text: the Germanic tribes agreed to seal the vault for three Roman generations; the Romans agreed never to dig within fifty feet of the principia's eastern wall. The agreement was broken by the current excavation. The binding was void the moment the first shovel hit that ground.)

This document is evidence. It answers the wax tablet's incomplete warning. A character who found both the tablet and this scroll can now reconstruct exactly what happened and why the vault is waking up.

---

### THE RUNIC CORRIDOR (new, before the altar)

A 30-foot corridor connecting the Binding Chamber to the Altar Chamber.

> *The passage narrows. The floor changes from earth to cut stone, and the stone is covered in carvings — not random marks, but a mosaic of interlocking rune shapes that covers every inch of the floor from wall to wall, in rows, from the chamber behind you to the archway ahead.*
>
> *The runes glow faintly. Not with fire — with something cold, a blue-white edge on each carved line, steady as a held breath. There is no safe path around them. There is only through.*

**The puzzle:**

The floor is a runic sequence lock. The "safe" path through exists and is consistent: only specific runes in a specific order do not trigger. Wrong runes deal 1d8 lightning damage and make a sound that carries to the altar chamber, giving the altar guardians one round of preparation.

**Finding the safe path:**

The clues to the sequence exist in earlier chambers:
- The shield arrangement in the Shield Hall (left branch): the shields are hung in a specific order by tribe symbol. This order maps to the rune sequence. A character who noted the shield arrangement and succeeds on DC 13 Intelligence can trace the safe path.
- The bone token (either from the hidden alcove or the preserved warrior's throat): OTHALAN rune is the last rune in every row. If the party ends each row on an OTHALAN rune, they take no damage. This works even without the shield-order clue.
- Religion DC 14 (passive, while looking at the floor): The pattern has a liturgical logic — it reads like a prayer sequence. The safe path is the path of the ritual, not the path of least resistance. Characters with high Religion modifier can identify the prayer structure and navigate it correctly.

**For players who ignore the puzzle or fail all checks:**
They can simply walk through, taking 1d8 lightning damage per wrong rune. A determined party can brute-force the corridor if they have healing. There are approximately 8 rows, and a failed attempt on each deals 1d8 → average 4.5 damage per row → 36 damage total if every row is failed. Survivable but costly. This is intentional — the puzzle is not a wall, it is a cost.

---

### THE ALTAR CHAMBER (upgraded combat)

Keep the existing read-aloud text for the altar chamber exactly as written, including the Spear Presence section and the Spear Reveal read-aloud.

**Replace the combat encounter:**

Old encounter: 2 Animated Armor (CR 1 each) — trivially easy

New encounter: 1 Wight (CR 3) + 2 Shadows (CR 1/2 each)

**XP:** 700 + 100 + 100 = 900 × 2 (multiplier for 3 creatures) = 1,350 XP for a 4-player party. This exceeds the Hard threshold (900 XP) and approaches Deadly (1,600 XP). At Level 3, with depleted resources from the vault, this is the designed climax.

**Re-frame the guardians:**

The Wight was the High Priest of the binding ceremony. He chose to remain as the vault's permanent guardian — the same willing sacrifice concept established by the preserved warrior in the flooded gallery. He does not attack immediately.

**Replace the old "animated armor speaks" read-aloud with:**

> *The guardian has been here for three hundred years. You can see it in the way he stands — not the restless hunger of the walking dead, but the settled weight of something that made a choice and is still keeping it.*
>
> *He is armored in Germanic plate that has not rusted. His eyes are the color of old ice. He looks at the spear, then at you, then at the spear again.*
>
> *When he speaks, it is in a language three of you do not understand, and one of you* — *the one with the highest Wisdom — does, though you have never learned it:*
>
> *"The bargain was broken. Not by you. But by your kind. I am still bound. You are not."*

**Combat notes:**

The Wight uses his Life Drain action preferentially on the character holding or reaching for the spear. He is not trying to kill the party — he is trying to prevent the spear from leaving the chamber. If the party backs away from the spear and stays out of the altar's immediate area (beyond 15 feet), the Wight holds position and the Shadows stop attacking.

The Shadows (CR 1/2) flank and harass, using Pass Through to avoid opportunity attacks and cycling their Strength Drain. They are not self-directed — they follow the Wight's tactical positioning.

**Exit condition:** If the party is willing to leave the spear and back out, the Wight allows it. This is a legitimate choice. The combat is not obligatory — it is the result of insisting on taking the spear. If the party explains (in any language — gestures work, or someone has Germanic language) that they are not breaking the bargain voluntarily, that their Legate ordered this, the Wight pauses on a DC 14 Persuasion check. He does not let them take the spear — but he gives them one more piece of information before the combat resumes:

> *"The one who ordered this. His debt is greater than yours. But you carry it now."*

**On defeating the Wight:**
He does not rage or beg. He folds. Not to the ground — he lowers himself deliberately, sits cross-legged at the base of the altar, and becomes still. The Shadows dissipate.

> *He looks at the spear one more time. Then he looks at you.*
> *"Carry it carefully. What is inside it is older than Rome."*
> *Then he is still, and whatever animated him is gone.*

**The First Touch:** Keep existing text exactly as written (DC 14 Wisdom save, 1 level of corruption on failure).

---

### Scene 4: Return to the Surface (upgraded)

Keep the existing read-aloud text for the frenzied worker exactly as written.

**Upgrade the encounter:**

Old: 1 Berserker (CR 2) alone

New: 1 Berserker (CR 2) + 2 Cultists of Mars (CR 1/8, use Cultist stat block)

The two Cultists are legionaries who were stationed near the excavation. They were exposed to the spear's aura through the open shaft. They are not as far gone as the Berserker — they are not attacking yet — but they are standing near him, watching, not moving to stop him, and muttering the same phrase over and over under their breath.

The phrase: *"Mars aversus est. Mars aversus est."*

**What this adds:**
- The Cultists are not immediate combatants but they complicate the scene. If the Berserker is killed, the Cultists gain advantage on saving throws to resist the spear's aura for the next 24 hours — his death breaks whatever hold the spear had on them temporarily. If the party subdues rather than kills him, the Cultists snap out of it when he is restrained and become terrified witnesses.
- The Cultists are important for later sessions: they are the first evidence that the spear's corruption spreads through proximity, not just touch.
- DM note: Do not make the Cultists attack unless the party directly threatens them. They are enthralled, not combative. This scene is primarily about the Berserker; the Cultists are detail.

**After the scene:** Keep the existing resolution options table exactly as written.

---

## Skill Audit update

At the bottom of the Skill Audit section, add the following new entries for the new content:

### New skill checks — flooded gallery, bone chamber, binding chamber, runic corridor

These follow the same format as existing entries in the Skill Audit.

**Stealth DC 14 (active group check: extinguishing torches and moving through the flooded gallery silently):**
The players must state they are doing this. If they do, run a group Stealth check against the Shadows' Perception (passive 10). On success, they pass without triggering combat. On failure, the Shadows notice light or sound and investigate. The combat does not start immediately — there is one round where the party can see the Shadows approaching through the water before initiative. That round matters: a party who reacted to the warning might dive back, while one who thought they were undetected might be in the middle of the flooded section. Give them that beat.

**Investigation DC 12 (active: examining the preserved warrior's body in the flooded gallery):**
He died voluntarily. Everything about the body's posture confirms this. Give the player this fact plainly. Then: the bone token at his throat matches the one in the Shield Hall hidden alcove, if the party found it. If they did not, they have the rune but not the context. If they did, they have both halves of the contract — the evidence is complete.

**Investigation DC 14 (active: studying the chain arrangement in the Binding Chamber as a system):**
The chains form a mechanism. The sequence is readable from oxidation patterns. On 5 above DC: the character can see the sequence without any additional check — they simply know which order to use. On exact DC: they know it is a mechanism and have a strong guess at the sequence; one attempt before the restraint snap occurs. On failure: they see chains. They do not see the system. If they want to brute-force it, they know the risk.

**Religion DC 14 (passive: reading the runic corridor as a liturgical sequence):**
Any character with Religion +4 or higher automatically perceives the prayer structure in the rune layout. They know the safe path. Give this to the player directly — no preamble, no hedging. "The layout is a prayer. You know which runes complete each row correctly." They walk the corridor without damage.

**Persuasion DC 14 (active: explaining to the Wight that the party did not break the bargain voluntarily):**
One attempt, before or during combat. On success: the Wight pauses. He does not release them, but he gives them information they would not otherwise get. On failure: combat proceeds. The attempt was not wrong — it simply did not work. The Wight is not persuaded by regret; he would need evidence (the contract scroll from the Binding Chamber helps: showing it to him grants advantage on the Persuasion check if the party found it).

---

## Style rules

- No em dashes in prose. Use colon, semicolon, or comma.
- No AI attribution in any content file.
- Latin words italicised in prose.
- Read-aloud text in blockquote format (`>`), slow and atmospheric.
- DM-facing content in direct DM voice.
- Do not change any content outside the vault section and Scene 4 combat upgrade.
- Use Edit (targeted edits), not Write — do not overwrite the whole file.

---

## When done

Report:
- Which scenes were modified vs added
- Whether the left branch, right branch, binding chamber, runic corridor, and upgraded altar encounter were all inserted
- Line count before and after
- Any section where the insertion point was ambiguous
