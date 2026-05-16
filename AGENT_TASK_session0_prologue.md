# Agent Task: Session 0 — In-World Prologue + Character Creation Improvements

## What this project is

A D&D 5e campaign book written in Quarto Markdown, published at:
https://dnd-kamitor.github.io/DnDVault---Roman-Campaign/

Session 0 currently has two files:
- `session0.qmd` — player-facing character creation document (out-of-game questions)
- `gm_session0.qmd` — GM guide for running Session 0

**Problem:** There is no in-world content. Players read character creation questions, make their characters, and then jump straight into the Chapter 1 cold open (which starts mid-crisis, three days after something terrible has begun). Adults playing this campaign for the first time have no feel for the world, the fort, the NPCs, or daily Roman military life before the crisis hits. The disconnect weakens the cold open's impact.

**Goal:** This task adds two things:
1. A **playable in-world prologue** to `gm_session0.qmd` — a structured GM-run scene covering the party's arrival at Fort Vindolanda the day before Session 1. This is a table scene, not a character creation document.
2. Minor improvements to `session0.qmd` — small additions that ground the questions in world texture.

---

## Files to modify

- `gm_session0.qmd` — add the prologue section (major addition)
- `session0.qmd` — small improvements only (add a "daily life" sensory orientation section and one new set of setting questions)

## Files NOT to touch

- `chapter1.qmd` — the cold open stays in chapter1.qmd, not here
- `knowledge.qmd` — do not touch
- Any other file

---

## The prologue design

### Context

The party has just been transferred to Fort Vindolanda on the Germanic frontier. Their official paperwork says "construction oversight assignment." They do not yet know they are a special unit. They arrive on the same day — probably the same wagon from the nearest supply road — but some may not know each other.

This prologue covers **the day before Session 1**. It should take 1.5 to 2 hours of real play time. Session 1 begins the next morning when Corvinus summons them.

The prologue is **not** a tutorial. It is immersion. It gives players a feel for what normal life at this fort looks like so that when Session 1 breaks that normal, the contrast has weight.

### Cast of NPCs available in this scene

| NPC | Role | Personality hook |
|---|---|---|
| **Quartus** (Quartermaster) | Processes them in, issues their quarters assignment | Bureaucratic, sour, suspicious of transfers; softens slightly if bribed or flattered |
| **Varro** (Centurion) | Gives them an orientation walk of the fort | Hard, professional, watches them carefully; hints that the fort has been "off" lately but says nothing specific |
| **Brennus** (Taberna owner, vicus) | Runs the only good tavern outside the gates | Warm, gossipy, knows everything about everyone; will trade information for coin or conversation |
| **Valeria** (Medicus) | Camp doctor at the valetudinarium | Precise, slightly cold, very competent; will mention in passing that she has had three unusual cases in the last week |
| **Rufus** (Smith) | Runs the fabrica (smithy) | Big, quiet, opinionated about weapons; reacts well to characters with smith or craft backgrounds |
| **Lucilla** (Mail handler, mensarii office) | Handles the camp's correspondence | Overly cheerful, moves fast, knows where everyone's mail is and where everyone has been |
| **Cassia Liviana** (Augur) | Fort's official diviner | Absent from the main fort area tonight; players may see her in the distance at the principia steps, but she does not engage tonight. This is notable because she is normally visible and social. |

**Corvinus (Legate)** does not appear tonight. His office lights burn until the third watch. His aide says he is in private correspondence.

### The structure: four scenes

---

#### PROLOGUE SCENE 0: The Road In (read-aloud + travel description)

This is a brief 5-minute atmospheric opening before they dismount at the gate.

**Read aloud:**
> The road has been Roman for fifty miles. Stone-laid, ditched on both sides, the surface wearing down to pale chalk where the centre is most-travelled. The milestones are accurate. The legionary patrols you have passed have been on schedule. The empire functions here.
>
> Then the land changes. The road crests a low ridge and Fort Vindolanda comes into view: a rectangle of earth and stone on a rise above the valley, its turf ramparts crested with a timber palisade, its four gates facing the cardinal points. The south gate is open. Smoke from the bakery. Laundry on the wall between the towers.
>
> At this distance it looks like what it is: a garrison fort on a routine posting, squared off against a horizon of grey hills. Nothing alarming.
>
> The road descends toward the gate. A sentry on the rampart watches you arrive. He does not move to wave you through. He watches for a moment longer than he needs to, then turns and says something to the man beside him.
>
> You do not hear what he says.

**DM direction:** Do not explain the sentry's behavior. It is the first note of wrong. Move on.

---

#### PROLOGUE SCENE 1: Processing In (at the gate and quartermaster's office)

Characters present their transfer papers to the gate guard, then are directed to Quartus at the *horrea* (granary/quartermaster's office).

**Quartus's processing check:**
- He reviews their paperwork, frowns, reviews it again. "Construction oversight. In the principia basement. Fine."
- He assigns them quarters in the east barracks, together (unusual — normally transfers go to existing units). He does not remark on this.
- He issues each character a bunk assignment, a duty schedule for the next three days, and a wooden pass token for after-hours vicus access.
- If asked why they are all quartered together: "Legate's orders. Don't ask me."

**Skill checks in this scene:**

- *Insight DC 12 (active: watching Quartus process their papers):* He stamps the paperwork without reading it. This is unusual. Supply officers always read what they stamp. He already knew they were coming and in what configuration.
- *Perception DC 10 (passive):* The board behind Quartus normally lists current unit assignments. Three entries have been crossed out with a single red mark in the last week. No names. Just red marks.
- *Investigation DC 13 (active: asking about the red-marked entries on the board):* Quartus closes the board before you finish your sentence. "Administrative. Nothing to do with you."
- *Persuasion DC 11 (active: asking Quartus anything beyond procedure):* He answers one question honestly before shutting down. Pick the question wisely. He will not discuss the Legate. He will discuss the fort's supply situation (short on salt pork, waiting on a wagon), the last work crew (the well-diggers), or the medical bay's unusual traffic.

---

#### PROLOGUE SCENE 2: The Fort Walk (Varro's orientation tour, or self-directed)

Varro, the Centurion, meets the party at the barracks and walks them through the fort. He does this for all new transfers. The tour is functional: here is the principia, here is the *via principalis*, here is the bathhouse schedule, here is where you eat, here is what you do when the horn blows. He is professional and efficient.

**What is available in the fort:**

Give players agency here. They can follow Varro, split up and explore, or stop at any location that interests them. Each location has one NPC and one discovery.

**The Principia (HQ building):**
- Augur Cassia is not at her usual place at the east entrance. Her aide says she is "occupied with preparations." He will not say what preparations.
- Investigation DC 11 (active: looking at the principia steps): There are fresh marks in the stone near the eastern door — pale scrape marks from something heavy being moved recently, within the last day.

**The Valetudinarium (Medical bay):**
- Valeria is bandaging a legionary's wrist. The wound is not from combat. It is a self-inflicted laceration, shallow, in a pattern.
- She greets the party professionally. If asked about the wound: "Legionary sleepwalking. Third this week." She does not offer more.
- Medicine DC 12 (active: looking at the wound pattern): The laceration was deliberate but not self-harming — more like writing. The pattern has three strokes that resemble a rune shape (Tiwaz, though the characters won't know the name yet).

**The Fabrica (Smithy):**
- Rufus is at the forge, re-edging a gladius. He looks up, nods, keeps working.
- He will talk if a character shows genuine interest in craft or weapons. He mentions: "Had to re-forge four weapons in the last two days. The men keep bending their blades. Not fighting. Just... bending them in their hands while they sleep, apparently."
- He does not find this funny. He does not find it frightening either. He finds it annoying.

**The Stables:**
- The horses are nervous. All of them. They have been nervous for four days, according to the stablehand. The stablehand is sixteen years old and visibly unsettled.
- Nature DC 10 (passive): Horses react to predators with this kind of sustained edge. Whatever they sense is not a one-time event. It is a constant presence.

**Varro's tells (throughout the tour):**
- He takes a slightly longer route past the *principia* basement access door. There is a wooden plank across it, wedged shut, with a wax seal. He does not mention it.
- Perception DC 12 (passive): The wax seal on the door has been broken and re-pressed at least twice. The repairs are visible in good light.
- Insight DC 13 (active: watching Varro during the tour): He is not tense about any specific location. He is managing general unease. The fort has been bothering him for days and he has not identified why, which bothers him more than the original feeling did.

---

#### PROLOGUE SCENE 3: The Vicus (Optional, evening)

The vicus — the civilian settlement outside the south gate — is available in the evening if players choose to go. The wooden pass token from Quartus allows it.

Brennus's taberna is the social hub. It is warm, it smells of stewed lamb and cheap wine, and it has eight other soldiers in it who will not speak to new arrivals until the second cup.

**Brennus:**
- He greets them warmly, pours without asking.
- He talks if they listen. He gossips: the supply wagon is three days late; a Germanic trader named Sigrun usually comes by this time of month and hasn't; the Legate has not left the principia for two days.
- Investigation DC 10 (active: asking Brennus about anything unusual): He says, lowering his voice: "The dogs. Six nights ago. All of them. I found my own dog at dawn, stiff at the gate. No wound. Just dead, like a fire gone out." He pauses. "I've been on this road for eleven years. Dogs don't just die."
- Insight DC 11 (active: watching Brennus tell this): He is not exaggerating for effect. He is telling them because he is relieved to tell someone who might care.

**The other soldiers in the taberna (optional roleplay):**
- A legionary named Sextus, posted to the north tower, has not spoken since the dogs died. He sits in the corner and drinks methodically. He will not discuss the dogs if approached.
- A Gallic worker from the road crew — the excavation team — is at the back table, very drunk. If approached carefully (Persuasion DC 12): he was one of the men who dug up the vault access. He describes what they found not as a ruin but as "a room that was waiting." He becomes frightened when describing it and will not say more.

---

#### PROLOGUE SCENE 4: The First Night

End the prologue with this:

**Read aloud (late evening, in the barracks):**
> The barracks quiet around the third watch. The night is clear, cold, usual.
>
> Then, in the space between two heartbeats, you all dream the same dream.
>
> You are standing in a corridor of stone. The torch you carry does not cast light outward. It illuminates only you — a small circle of warmth — and beyond the circle, everything is absolute dark. In the dark, something breathes.
>
> You wake. The barracks is dark and silent. For a moment you cannot remember where you are.
>
> Then one of you — whoever woke first — hears it from outside: a long, hollow sound from the direction of the principia. Not a horn call. Not a voice. Something that uses the same air as a voice but is not one.
>
> It stops. Nothing answers it. Nobody else in the barracks moves.
>
> Morning comes without further incident.

**DM direction:** This shared dream is the same dream that opens Chapter 1's cold open — *"Three nights ago. You dream."* Do not connect them explicitly tonight. The players will make the connection when Session 1 begins. This is the seed. Let it sit.

---

### Format rules for this prologue

- Write it in DM voice — direct, practical, first-person where natural. Not encyclopedia entries.
- Read-aloud text in blockquote format (`>`), slow and atmospheric.
- No em dashes in prose. Use colon, semicolon, or comma.
- Latin words italicised (*principia*, *via principalis*, *vicus*, *valetudinarium*).
- No AI attribution.
- Skill checks in this format: *Skill DC XX (passive or active: trigger condition):* outcome.

---

### Where to insert in gm_session0.qmd

Add a new top-level section titled `## The Prologue: Day of Arrival` near the END of `gm_session0.qmd`, before any existing appendix or wrap-up content. Do not restructure the existing file — append this section.

If the file already has a final section, insert the prologue section before it.

---

## session0.qmd improvements

Add one new subsection to `session0.qmd` called `## A Day at the Fort` immediately before the `## Character Hooks` section.

This subsection is 300-400 words of sensory orientation written in second-person present tense, describing what a normal day at Vindolanda looks and smells and sounds like — the *tuba* calls that mark the hours, the smell of the bakery before dawn, the sound of the smithy, the mud in the vicus after rain, the quality of the cheap wine, the specific weight of the duty schedule pinned to every legionary's bunk. Its purpose is to give players a sensory anchor for their characters before they get to Session 0's character questions.

This is flavour text, not mechanics. It does not need skill checks or interactive elements. It should make the fort feel real.

---

## When done

Report:
- How many scenes were added to gm_session0.qmd
- Line count change
- Whether the session0.qmd sensory section was added
- Any location where you could not find a clean insertion point
