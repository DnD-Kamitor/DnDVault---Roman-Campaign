# Session Progress

Last updated after each completed task. Check here to see current status.

---

## Done this session

- [x] **Milestone 79** — Source book integration (Glory of Rome + Lex Arcana Britannia): Coronae, Lemures, Belatucadrus in knowledge.qmd; Peoples Near the Vallum + Alaisiagae + Agrona in germanic_tribes.qmd; Vindolanda decline narrative + Belatucadrus shrine in vindolanda_guide.qmd
- [x] **fort_vindolanda_prompt.md** — Generation prompt for Fort Vindolanda (4591 chars)
- [x] **Style cleanup** — Removed all `---` dividers and prose em-dashes from all .qmd files
- [x] **Books/ gitignore** — PDFs removed from tracking
- [x] **Milestone 80** — GitHub CI `if: success()` guard; professions.qmd campaign hooks rewritten (removed 8 plot spoilers: Brutus named, Marius Coda named, chapter callouts, replica spear, Brutus agents, Brutus cult in Collegium section)

---

## Done this session (continued)

- [x] **Milestone 81** — knowledge.qmd: 60 passive gates converted to `<details>` collapsibles; intro text updated. vindolanda_guide.qmd: 41 passive gates converted. All .qmd files: zero remaining open passive gate bullets.
- [x] **Milestone 82** — MapTool monster attack macros (all sessions): 31 MTScript files covering every creature in S1-5. Each opens an HTML dialog with live dice rolls, campaign-specific DM notes, and tactical callouts. Custom bestiary creatures (Alp, Draugar, Genius Loci, Larvae, Strix, Lemur, Nix) included. S5 includes Fausta Luperci (Option A) and Mars himself (Option B, victory at 150 HP). README updated with full session tables.
- [x] **Encounter scaling (5 players)** — chapter1.qmd updated: Flooded Gallery 3→4 Shadows (Easy→Medium), XP text updated from four-player to five-player throughout. Bone Chamber (Hard 1,700 XP) and Altar Chamber (near-Deadly 1,800 XP) already appropriate for 5 players. Difficulty table in macros/monsters/README.md.
- [x] **Milestone 83** — Session 1 simulation audit: all 10 bugs fixed. BUG-1: stale Scene 3 deleted, attunement properties moved to DM Notes. BUG-2: Animated Armor ghost reference replaced with Wight + Shadows. BUG-3: Runic Corridor explicit DM answer (OTHALAN ends every row; tribal shield order confirmed). BUG-4: chain sequence added (west first, north second, east last, then master). BUG-5: Scene 5 (The Reckoning) written: Corvinus/Lucius confrontation read-aloud, four resolution branches, Cassia private word, Varro closing beat. BUG-6: Tribune Lucius introduced in Scene 1. BUG-7: Marius Coda named in read-aloud; Cultists named Titus Flavinus and Gnaeus Peregrinus. BUG-8: Fallen legionaries specified (Gaius Pullus dead, Marcus Dexter dead, Aelius Rufus dying with DC 12 Medicine and Session 2 payoff). BUG-9: Bone Chamber DM note on Titus Sempronius Caecilius as ritual feeder. BUG-10: Wight language named (pre-Roman Belgic Germanic); lamp origin attributed to Titus.

---

## Queued (in order)

### Session 0 simulation audit — bugs found (gm_session0.qmd + session0.qmd)

Full mental simulation run. Ordered by severity.

- [ ] **S0-BUG-1: Dream mismatch** — gm_session0.qmd states the Prologue Scene 4 dream is "the same dream that opens Session 1's cold open." It is not. Prologue dream: dark corridor, torch that illuminates only you, something breathing in the dark. Chapter 1 cold open: ankle-deep blood, spear glowing like a dying star, the voice "MEUM." These are intentionally different escalations (Day 0: formless presence; Day 3: god speaks), but the file claims they are the same. Fix: replace "the same dream" with a DM note explaining the two dreams are linked but distinct — the Prologue is the first contact, the cold open is the god finding its word.
- [ ] **S0-BUG-2: Fatum card vs. Three Questions card confusion** — session0.qmd says to write "a one-sentence version of your answer to each question on an index card" (implying three cards per player). gm_session0.qmd Part 4 says each player writes ONE sentence ("I will --") on ONE card. A DM collecting cards at session end would be confused about what they're gathering. Fix: clarify in both files. The Three Questions produce conversation; the Fatum Card is a separate synthesis step afterward, distilling all three into one "I will --" sentence. One card per player, collected at the end.
- [ ] **S0-BUG-3: Cover story cards have no distribution trigger** — gm_session0.qmd describes cover story cards in detail but never says WHEN to hand them out. Players need them before the Prologue Scene 1 (they're arriving at the fort with a stated reason). Fix: add one instruction line after the role assignment section: "After roles are confirmed and before the Prologue begins, hand each player their cover story card. They hold this information as their character's reason for being at Vindolanda."
- [ ] **S0-BUG-4: Gallic laborer in Prologue Scene 3 is unnamed and is Marius Coda** — The "Gallic laborer from the road crew" who worked at the excavation and describes "a room that was waiting" is not identified. He is Marius Coda — the same man who becomes the Berserker in Session 1 Scene 4. A DM who doesn't connect these will miss the payoff when players recognize him. Fix: name him in the Prologue ("A Gallic stone-hauler named Marius Coda sits at the back table") and add a DM note: he was part of the well-digging crew, touched nothing, was near the vault for three hours. That was enough. Let players recognize him in Session 1 when they crest the shaft.
- [ ] **S0-BUG-5: Prologue Scene 2 has four locations, not five** — The Session 76 milestone entry notes "fort walk with Varro + 5 locations" but only four are written: Principia, Valetudinarium, Fabrica, Stables. One location is missing. Fix: add the fifth location — the Armory (custos armorum relevance, plus it has something wrong: two gladii re-edged in the last two days for "bending in their sleep"). The Armory also connects the Fabrica scene without duplication.
- [ ] **S0-BUG-6: Quartus's red-marked board entries have no answer** — Prologue Scene 1 surfaces three red-crossed entries on the assignment board with a DC 13 Investigation check. If players succeed, Quartus closes the board. The check resolves with no information on success. Fix: the passive DC should let players SEE the marks. The active DC should let them READ what the marks cover before Quartus closes the board. Answer: the three entries are workers from the northeast construction crew — the initial four-man team sent into the vault. One entry is two men assigned together. Quartus crossed them out when they did not report back. He knows. He will not discuss it.
- [ ] **S0-BUG-7: No transition from Prologue Scene 1 to Scene 2** — Quartus assigns bunks and the scene ends. Varro then "meets the party at the barracks" with no connecting tissue. Players would ask "do we go to our bunks?" or "what now?" Fix: add one line at the end of Scene 1: "When they reach the east barracks and claim their bunks, Centurion Varro is already there, arms crossed, watching them arrive. He has been told to expect exactly this group."
- [ ] **S0-BUG-8: Cassia's absence in Scene 2 has no skill check** — Her aide says she is "occupied with preparations" and will not say what preparations. If a player asks "can I learn more?" there's nothing to roll. Fix: add DC 13 Persuasion (active, pushing the aide past the official answer): success reveals Cassia is in the principia's basement archive reviewing old construction records. This is true, informative, and doesn't spoil her actual discovery.
- [ ] **S0-BUG-9: No Prologue close-out text** — After Scene 4 (The First Night), "morning comes without further incident" and the text ends. A DM has no instruction for how to formally close the Prologue. Fix: add two closing sentences for the DM: "End here. Tell the players: Session 0 is complete. The dream they just shared is the hook for Session 1 — either run it immediately or at the next meeting. Do not explain the dream."
- [ ] **S0-BUG-10: No Session 0 timing overview for the DM** — A DM running this cold doesn't know how long it takes. Part 2 (aloud questions with 5 players) could run 90-120 minutes; Part 3 (private questions with 5 players) could take 30-40 minutes. The Prologue is 1.5-2 hours. Total is potentially a 4-5 hour meeting. Fix: add a 5-line timing overview at the top of gm_session0.qmd before Part 1: Part 1 (10-15 min), Part 2 (60-90 min), Part 3 (20-30 min), Part 4 (15 min), Prologue (90-120 min, same meeting or next session depending on table energy).

### Session 1 simulation audit — new bugs found (chapter1.qmd)

Additional bugs found after applying Milestone 83 fixes. Ordered by severity.

- [ ] **S1-NEW-BUG-1: Scene 1 has no principia read-aloud** — The cold open ends with the Legate's voice ("You're going down there"), then Scene 1 restarts the scene with a bullet-point briefing list and no read-aloud to establish the physical space. A DM transitions from gorgeous atmospheric prose to a dry list. Fix: add a 3-4 line principia read-aloud to open Scene 1 that gives the physical space (the three NPCs at the table, the smell of incense, the maps unrolled) before the briefing list begins.
- [ ] **S1-NEW-BUG-2: Cassia's Scene 1 behavior contradicts her OGAS** — She "interrupts, warning that the omens forbid disturbing the spear." Her OGAS secret agenda is to seem cooperative while feeding doubts. Bluntly opposing Corvinus causes him to remove her from the room (which he does in the Refusal Contingency), which ends her usefulness in the scene. Fix: replace the description of her interruption with a DM note on HOW to run her in Scene 1 — she doesn't oppose Corvinus directly; she says one quiet phrase to the party, not to Corvinus, that plants a doubt without giving him a target to shut down.
- [ ] **S1-NEW-BUG-3: Varro's Scene 1 contribution contradicts his OGAS** — He "suggests destroying it immediately." His OGAS goal is to learn what it is before the Legate deploys it. Suggesting immediate destruction is the opposite of his actual agenda, which requires keeping the spear available long enough to understand it. Fix: change his Scene 1 contribution to expressing skepticism about the retrieval timeline: "We don't know what sealed it or who is on the other side of that seal. Sending men down without understanding what they're walking into is how we lose the men." This is consistent with his OGAS and creates more interesting friction with Corvinus.
- [ ] **S1-NEW-BUG-4: No light source provision for the descent** — Scene 2 assumes the party has torches but nothing in Scene 1 or Scene 2 provides them. The vault scenes depend on torchlight for the Shadows, the Flooded Gallery, and several read-alouds. Fix: add one sentence to Scene 2 before the shaft description: "Corvinus's aide meets them at the excavation shaft with four torches and a tinderbox, which he hands over without comment."
- [ ] **S1-NEW-BUG-5: Shield Hall rune mapping is not in the Shield Hall section** — The DM answer in the Runic Corridor section tells a DM which tribe maps to which rune (Marcomanni/TIWAZ, Cherusci/HAGALAZ, Suebi/ISA, others/NAUDHIZ, Mars/OTHALAN). But the Shield Hall section gives the tribe names and symbols without the rune mapping. A DM describing the Shield Hall has no information to give a player who notes the arrangement. Fix: add a DM note to the Shield Hall after the passives: "The shield arrangement encodes the Runic Corridor's safe path. Order: Marcomanni/boar (TIWAZ rune), Cherusci/three-fingered hand (HAGALAZ), Suebi/serpent (ISA), mixed small offerings (NAUDHIZ), Mars/wolf at the highest point (OTHALAN). A player who notes and rolls DC 13 Intelligence carries this mapping to the Runic Corridor."
- [ ] **S1-NEW-BUG-6: Binding Chamber chain directions have no room orientation** — The chain sequence DM note uses compass directions (east, north, west walls) but the room has no established orientation relative to the path of travel. A DM cannot tell players "the east chain" without knowing which wall is east. Fix: replace compass directions with spatial ones: "left wall as you entered from either branch (west), right wall (east), far wall toward the Runic Corridor (north)." Then the mnemonic stays: oldest chain first, newest chain last, then centre.
- [ ] **S1-NEW-BUG-7: Runic Corridor has no spatial description** — The corridor is described as 30 feet long with rune rows on the floor, but never describes what a player is physically choosing between in each row. How many runes per row? How wide is each row? Without this, a DM asked "how do I navigate this?" has nothing concrete to describe. Fix: add to the puzzle description: "Each row is approximately 3 feet wide spanning the full corridor, containing five runes side by side. There are eight rows to cross from the Binding Chamber archway to the Altar Chamber archway. A character stepping through states which rune they step on in each row."
- [ ] **S1-NEW-BUG-8: Two different skill checks for communicating with the Wight** — The Altar Chamber collapsible header says "DC 14 Wisdom (Insight)" for communicating with the Wight. The Persuasion attempt text says "DC 14 Persuasion." A DM asked "what do I roll?" would be confused. Fix: consolidate to one check. The Persuasion attempt text and the collapsible header should match. Use DC 14 Persuasion (the active attempt to explain) or DC 14 Wisdom (Insight) (reading whether the Wight can be reached) as two options for the same action, player's choice.
- [ ] **S1-NEW-BUG-9: Handout 2 (vault inscription) has no distribution trigger in the scene flow** — Handout 2 is listed in Pre-Session prep but no scene references when to give it to players. Fix: add a line in the Altar Chamber section after the spear reveal read-aloud: "Give Handout 2 (Vault Inscription) now — it is carved into the altar stone and visible once the party is inside the chamber threshold."
- [ ] **S1-NEW-BUG-10: Handout 1 (Legate's Orders) has no distribution trigger in Scene 1** — Listed in Pre-Session prep but Scene 1 doesn't say when or whether Corvinus physically hands it over. Fix: add one sentence to Scene 1 after the briefing: "When Corvinus formally assigns the mission, he sets a wax tablet on the edge of the table without picking it up again. This is the written order. Give Handout 1."
- [ ] **S1-NEW-BUG-11: Scene 5 Cassia's entrance has no physical context** — She appears "at the edge of the courtyard" from a direction that is not the principia. But if the shaft is beneath the principia, the scene plays out inside or immediately adjacent to the principia building. Where does Cassia come from? Fix: add one sentence: "Cassia approaches from the principia's east side entrance — the one that faces the bathhouse, not the main door — as if she had been waiting at a distance where she could see the shaft but Corvinus could not see her."
- [ ] **S1-NEW-BUG-12: Level-up has no in-fiction framing** — "Advance to Level 4" closes the session as a raw mechanic with no in-world wrapper. After the weight of Scene 5, this is an abrupt landing. Fix: add 2-3 sentences. The characters have survived contact with a god's anchor point, run a Hard combat and a near-Deadly combat while depleted, and made a consequential choice under pressure from a senior officer. The level-up is what they carry out of the vault: not a reward but a change. Cassia or Varro can mark the moment in-fiction with one line.

### Other queued tasks

- [ ] **Em-dash sweep** — Pre-existing prose em-dashes in content written before this session (not the structural `**Bold** —` gate format, which is kept)
- [ ] **Task D** (roman_tactics.qmd) — Pilum bending mechanics sidebar, coronae section, auxiliaries entry
- [ ] **Task E** (bestiary.qmd) — Lemures entry with Roman context, May festival mechanics, bean ritual
- [ ] **Task F** (chapter flavor) — Selgovi NPC in chapter2.qmd; Agrona cult traces in chapter3.qmd; Alaisiagae raven omen in chapter5.qmd
- [ ] **Task G** (vindolanda_guide.qmd) — Vallum five-layer defense diagram description; road names (Via Imperialis, Via Liminalis, Via Puellarum)
- [ ] **Track A** (Handouts) — 10 remaining HTML handouts (handout_02 through handout_11); prioritise handout_02 (vault inscription) and handout_03 (omens) as S1 essentials
- [ ] **Track B** (GM reference cards) — Sessions 2–5
- [ ] **Track C** (MapTool macros) — corruption_increase/decrease/reset.mts, commendationes_tracker.mts, role_display.mts, roman_calendar.mts
- [ ] **Encyclopaedia Arcana** (Spanish ed.) — De Re Militari translation still pending

---

## Format rules (quick ref)

- No em-dashes in prose. Use colon, semicolon, or comma instead.
- No `---` dividers in .qmd files.
- `**Bold** — description` in bullet gate format is structural — preserve it.
- Passive gate collapsible format:
  ```html
  <details>
  <summary><strong>History proficiency</strong></summary>
  
  Gate content here.
  
  </details>
  ```
- DC gate format: `<details><summary><strong>DC 13 Intelligence (History) — trigger phrase</strong></summary>`
