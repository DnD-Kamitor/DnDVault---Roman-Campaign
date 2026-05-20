# Simulation Report: Sessions 1–5

Full read-through simulation, 2026-05-20. Each bug has a label, location, description, and fix spec. Work through them in order — the cross-session bugs at the bottom depend on context built by the earlier ones.

---

## Session 1 Bugs

### BUG-S1-01 — Scene 0 / Scene 1 Overlap
**File:** `chapter1.qmd`  
**Location:** Scene 0 → Scene 1 transition  
**Problem:** Scene 0 ends with a full principia briefing read-aloud (Corvinus speaking, Cassia's omen line). Scene 1 then re-opens the same room with a second, more detailed principia read-aloud. A DM reading straight through will run two versions of the same scene, or skip Scene 1 thinking Scene 0 already covered it.  
**Fix:** Add a DM direction line between Scene 0 and Scene 1:  
> *"Scene 0's principia moment is a visceral 30-second hook only — the flash of the briefing, not the full scene. Scene 1 is the actual running of the meeting. Do not run both as separate scenes: Scene 0 sets the tone, Scene 1 provides the mechanics and NPC detail."*

---

### BUG-S1-02 — DarkTemple Maps Not in S1 Session Folder
**File:** `chapter1.qmd`, `Maptool/maps/build_campaign_maps.sh`  
**Location:** Pre-Session Maps table  
**Problem:** The build script copies `DarkTempleEntrancePublic.jpg` and `DarkTempleInteriorPublic.jpg` only into `Fort_Vindolanda/` and `S5_The_Wrath_of_Mars/` — not into `S1_Blood_and_Omens/`. The Session 1 map table only lists `DungeonVol2` for "all vault rooms." But `DarkTempleEntrance` is the perfect map for the descent/sealed stair and `DarkTempleInterior` for the Altar Chamber.  
**Fix:**  
1. Add to `build_campaign_maps.sh` in the S1 block: `copy_map DarkTempleEntrance "$S"` and `copy_map DarkTempleInterior "$S"`  
2. Update Session 1 map table:

| Scene | Map file | Use |
|---|---|---|
| Descent / shaft head | `DarkTempleEntrance` | Sealed stair, the moment before the party descends |
| Shield Hall, Flooded Gallery, Bone Chamber, Binding Chamber, Runic Corridor | `DungeonVol2` | Stone dungeon with altar circle; reuse across branching rooms |
| Altar Chamber | `DarkTempleInterior` | Vault interior, altar, spear reveal |
| Scene 4 exterior | Fort_Vindolanda folder | Marius Coda and cultists above ground |

---

### BUG-S1-03 — No Guidance on Representing the Vault's Branching Structure
**File:** `chapter1.qmd`  
**Location:** Pre-Session Maps section  
**Problem:** The vault has 7 distinct areas (Entrance Passage, T-Junction, Shield Hall, Hidden Alcove, Flooded Gallery, Bone Chamber, Binding Chamber, Runic Corridor, Altar Chamber). The map note says "reuse for every vault room, reposition tokens between scenes" with no guidance on how to represent left/right branches.  
**Fix:** Add a DM note after the map table:  
> *"The branching vault (Shield Hall vs. Flooded Gallery) plays best as theater of the mind for the branch rooms — the DM describes, players track direction. Use DungeonVol2 for any scene that benefits from a grid: the Bone Chamber fight and the Binding Chamber chain puzzle are the two most useful. Use DarkTempleInterior for the Altar Chamber climax. Sketch the T-junction on a scrap of paper for the table at the start of Scene 2 and ask players to point which branch they take."*

---

### BUG-S1-04 — Spear Attunement Has No Explicit Trigger Point
**File:** `chapter1.qmd`  
**Location:** Scene 3 "The First Touch" and DM Notes "Spear of Mars: Attunement Properties"  
**Problem:** The "First Touch" scene describes a DC 14 Wisdom save with corruption consequences. The DM Notes separately list attunement properties (+2 attack/damage, +1d8 necrotic, Wisdom save disadvantage). But there is no explicit statement of when attunement occurs or how to connect the two sections. A DM might assume touching the spear counts as attunement, or might not realize there is an attunement system at all.  
**Fix:** Add to the end of "The First Touch" section:  
> *"Touching the spear is not attunement. Attunement requires a short rest while holding it (standard rules). The spear will not resist. The First Touch corruption save (DC 14 Wisdom) is a separate mechanic. A character who attunes adds the properties in the DM Notes Attunement Properties section to their sheet; the Wisdom save disadvantage from attunement stacks with the corruption track penalties."*

---

### BUG-S1-05 — Handout 3 (Omens) Has No In-Scene Trigger
**File:** `chapter1.qmd`  
**Location:** Pre-Session Props section and scene structure  
**Problem:** Handout 1 has an explicit trigger ("When Corvinus formally assigns the mission, give Handout 1 now."). Handout 2 has an explicit trigger ("Give Handout 2 as the party steps inside the threshold."). Handout 3 (Omens Observed) is listed in the Props section as "Give to players as prop" with no trigger scene specified.  
**Fix:** Add a trigger in Scene 0:  
> *"After the dream sequence but before the principia scene, when Corvinus mentions 'we lost four men and the dogs are dead': give Handout 3 (Omens Observed). It is a physical list that functions as a player prop for the rest of the session — they can add their own observations to it."*

---

### BUG-S1-06 — Cassia's OGAS "Agenda" Contradicts Her Actual Scene Behavior
**File:** `chapter1.qmd`  
**Location:** DM Notes OGAS table  
**Problem:** Cassia's listed Agenda is "Seem cooperative while feeding the party doubts and secret guidance." But in Scene 5 she approaches the party at a near-run and says directly to the nearest character "Do not give it to him. He will use it." This is not seeming cooperative — it is direct opposition to Corvinus in front of witnesses.  
**Fix:** Update Cassia's Agenda:  
> *"Cooperate publicly with Corvinus in the principia; create private doubt in the party whenever Corvinus cannot see or hear her. In Scene 5, when she has run out of options, drop the cooperative performance entirely and act openly. She has accepted the risk."*

---

## Session 2 Bugs

### BUG-S2-01 — Tribune's Name Inconsistency
**File:** `chapter1.qmd`, `chapter2.qmd`  
**Location:** Chapter 1, Scene 1 ("Tribune Lucius Aurelius") vs Chapter 2 everywhere ("Tribune Lucius Valerius Maximus")  
**Problem:** Chapter 1 introduces the Tribune as "Tribune Lucius Aurelius, attached to the Legate's office by order of Rome." Chapter 2 uses the full name "Lucius Valerius Maximus" throughout including Handout 4. These are inconsistent.  
**Fix:** Update Chapter 1, Scene 1 to use the canonical full name: "Tribune Lucius Valerius Maximus, attached to the Legate's office by order of Rome." The "Aurelius" was a ghost from an earlier draft.

---

### BUG-S2-02 — Assassin's Escape Timeline Unclear
**File:** `chapter2.qmd`  
**Location:** "The Sextus Murder" section  
**Problem:** Sextus is killed "the morning before the Tribune arrives." The assassin (Decanus Quintus Flavius) "left the fort with the Tribune's entourage, hiding in plain sight." But if the murder happened before the Tribune arrived, how was Quintus already integrated into the Tribune's entourage? The mechanism for his escape needs grounding.  
**Fix:** Add to the Sextus Murder DM section:  
> *"Quintus Flavius was pre-arranged by Brutus to join the Tribune's escort as a 'local liaison' — the paperwork was prepared weeks in advance by Brutus' network in Rome and delivered with the Tribune's sealed orders. The Tribune may not know who Quintus actually is. Quintus killed Sextus that specific morning because he knew it was his last night inside the fort before the Tribune's departure began the next day. The timing was his. The cover was Brutus'."*

---

### BUG-S2-03 — No Contingency for Vercingetorix Dying in Session 2
**File:** `chapter2.qmd`  
**Location:** DM Notes — Vercingetorix section  
**Problem:** The text calls the Session 2 fight "very hard at level 4, winnable but costly." If the party kills Vercingetorix in combat, Sessions 3-5 lose their most important NPC. There is no contingency for this outcome in the DM Notes.  
**Fix:** Add to the end of the Vercingetorix DM Notes section:  
> *"If the party kills Vercingetorix in Session 2: his lieutenant (use the same trust track, same knowledge — he carries everything Vercingetorix knew, but the personal history is absent). The Complete Trust entry costs one additional exchange to unlock because the party killed their chief. That is the consequence. It is not a brick wall. Name the lieutenant: use 'Arnulf' from the NPC token set, same stat block."*

---

### BUG-S2-04 — G.C.B. Name Needs DM Note
**File:** `chapter2.qmd`  
**Location:** Handout 5 / History DC 13 clue  
**Problem:** "G.C.B." is decoded as "Gaius Cassius Brutus" — a name that combines two different historical Roman Republican assassins (Gaius Cassius Longinus and Marcus Junius Brutus). This may puzzle players with classical history knowledge who will ask "that's two different people."  
**Fix:** Add a DM note alongside the Handout 5 description:  
> *"Brutus chose this cognomen deliberately. He is not descended from either Republican figure — he adopted the compound name as a political statement, aligning himself with the tradition of senatorial checks on military power. If players notice it, they are right to notice it: Brutus sees himself as heir to a specific Republican tradition, and this name is his manifesto."*

---

## Session 3 Bugs

### BUG-S3-01 — Missing S3→S4 Transition for Both Ritual Outcomes
**File:** `chapter3.qmd`, `chapter4.qmd`  
**Location:** End of Session 3 / Start of Session 4  
**Problem:** Session 3 has two endings — ritual success (spear shatters) and ritual failure (spear intact, Mars' presence intensifies). Session 4 is entirely premised on the spear still existing and needing to be carried below the fort. There is no DM note explaining what happens if Session 3 succeeded.  
**Fix 1:** Add to end of Session 3 Conclusion section:  
> *"If the ritual succeeded: Session 4 is not about the spear (it is destroyed). It is about Brutus' siege, which he launched in response to intelligence that the party was attempting to destroy his leverage. Mars was satisfied by the grove ritual but is not yet appeased — he still expects acknowledgment. Session 4's underground sequence becomes: escort the spear's FRAGMENTS (in Thusnelda's sealed clay jar) to the vault's altar as a formal return. Mars accepts this. The antechamber ritual in Session 4 Scene 4 uses 'the remains of the spear' rather than the whole weapon. All other mechanics hold."*

**Fix 2:** Add to Session 4 Tracking table:  
| Question | Session 4 implication |
|---|---|
| Was the Session 3 ritual successful? | If yes: the party carries spear fragments in Thusnelda's clay jar. If no: the party carries the whole spear. All antechamber scenes work the same way — Mars cares that they came, not the form of the offering. |

---

### BUG-S3-02 — Stone Golems (CR 10) Intent Unclear at Level 5
**File:** `chapter3.qmd`  
**Location:** Scene 5 — Option A  
**Problem:** Option A calls 3 Stone Golems at CR 10 against a Level 5 party. A Level 5 five-player party has a Deadly threshold of approximately 2,000 adjusted XP. Three CR 10 creatures at 120 HP each is multiple Deadly encounters. The intent seems to be "survive as a clock mechanic, not defeat them," but this is not stated. A DM reading this will either expect an impossible fight or assume the party should somehow win.  
**Fix:** Reframe the Option A header and add a DM note:  
> *"Option A — Defensive Hold (not a winnable fight at Level 5)"*  
> *"The standing stones are avatars of Mars' anger, not killable enemies. The party's goal is to hold them off long enough for the ritual to complete (4 successes on the Option B Skill Challenge, see below). Options A and B run simultaneously: while some party members fight the golems, one holds the ritual. Track golem engagement: each party member actively fighting a golem keeps it occupied for 2 rounds before it pivots to the ritual holder. The golems fade automatically when the ritual completes. Do not run Option A as a combat that needs to be won."*

---

## Session 4 Bugs

### BUG-S4-01 — No Callback Linking Session 4's Vault to Session 1's Vault
**File:** `chapter4.qmd`  
**Location:** Scene 3 — The Procession Below  
**Problem:** Session 4's underground sequence ends at "the same granite altar where the spear once rested" — the Altar Chamber from Session 1. But there is no explicit note connecting this to the Session 1 vault. A DM who has not run Session 1 recently will not know these are the same location. The Sunken Armory, Choking Hall, and Elder Stair are a NEW ROUTE to the same chamber (via the old Roman water tunnel, not the Session 1 excavation shaft).  
**Fix:** Add a DM note at the start of Scene 3:  
> *"This route (Sunken Armory → Choking Hall → Elder Stair) is a separate access path to the same Altar Chamber from Session 1 — the old Roman water tunnel mapped by Vercingetorix's envoy, not the excavation shaft the party used in Session 1. The Wight's remains are still in the Altar Chamber. The chains are still there. If the party explored the vault in Session 1, they recognize the chamber when they arrive; they enter from a different direction but the room is unmistakable. This is the intended callback: the campaign begins and ends in the same circle of stone."*

---

### BUG-S4-02 — Handout 8 "(Revised)" and Handout 9 "(New Purpose)" Have No Current Content Defined
**File:** `chapter4.qmd`  
**Location:** Props and Handouts section  
**Problem:** "Handout 8 (Revised): Replace the Triumph note with explicit orders..." tells the DM what to change from, not what the handout currently contains. "Handout 9 (New Purpose): The fort-wide order of battle" similarly describes purpose without content. The DM cannot make these without writing them from scratch.  
**Fix:** Write out both handouts in full:

**Handout 8 — Brutus' Intercepted Raven Message:**
```
[Torn papyrus, re-assembled from pieces found in the watchtower hearth ash]

...granary before dawn. Leave nothing they can use.
Cassia must not reach the vault. She knows the form.
Complete this before the god wakes and our window closes.
If the fort falls, burn what you cannot carry.
Rome will not mourn a frontier garrison. It will thank you.

    — G.C.B.
```

**Handout 9 — Fort Vindolanda Order of Battle (Siege Day):**
```
FORT VINDOLANDA — DAY 6 OF SIEGE
Order of Battle and Duty Roster

North Wall: Optio Gaius Felix + 8 men
South Gate: Centurion Varro + 4 veterans
West Wall (breached section): Auxiliary detail, 6 men
Principia: Legate's bodyguard, 4 Praetorians
Shrine and adjacent: Augur Cassia (do not reassign)

Rations: 3 days at full distribution / 5 days at half
Water: Cistern at 60% — do not use south well (contaminated)
Signal code: 1 long = fire, 2 short = breach, 3 long = all to walls

Supply tunnel exit (DO NOT DISTRIBUTE): south ditch, 
third post east of the water gate. Varro only.
```

---

### BUG-S4-03 — NatureGoddessTemple Map Is Used for Two Different Locations
**File:** `chapter4.qmd`  
**Location:** Maps for This Session table  
**Problem:** `NatureGoddessTemple` is listed twice in the campaign: once in Fort_Vindolanda as "Principia (HQ building)" and once in the Session 4 map table as "The choice point — where Mars speaks." Both uses are legitimate (the map is a cross-shaped stone building with a courtyard, which works for both), but the DM needs to know this is the same file serving two narrative contexts.  
**Fix:** Add a note to Session 4 map table entry:  
> *"NatureGoddessTemple — same map as the Principia in Fort_Vindolanda. Appropriate for both because the ritual antechamber shares the same architectural character: stone, vaulted, still. The DM is not looking for two different maps here."*

---

## Session 5 Bugs

### BUG-S5-01 — Mars Stat Block Referenced but Never Defined
**File:** `chapter5.qmd`  
**Location:** Scene 2 — Option B  
**Problem:** "Use the stat block from the previous version with these contextual tweaks" — the "previous version" is a prior draft that does not exist in any current file. The DM has the following summary: "HP 300, AC 20, four attacks, Divine Smite, War Cry, Legendary Actions (Strike, Summon Fallen, God's Eye)." But that is not a runnable stat block.  
**Fix:** Write Mars's full stat block into the Session 5 DM Notes. Minimum viable version:

**Mars, God of War (Divine Presence)**  
*Gargantuan celestial, lawful neutral*  
AC 20 (divine armor) | HP 300 | Speed 40 ft, fly 60 ft  
STR 26 (+8) | DEX 16 (+3) | CON 24 (+7) | INT 18 (+4) | WIS 22 (+6) | CHA 22 (+6)  
Saves: Str +14, Dex +9, Con +13, Wis +12  
Skills: Athletics +14, Perception +12  
Damage Immunities: poison, psychic; bludgeoning/piercing/slashing from non-magical weapons  
Condition Immunities: charmed, exhaustion, frightened, paralyzed  
**Divine Awareness:** Mars cannot be surprised and is aware of all creatures within 120 ft.  

**Actions (Multiattack: 4 attacks)**  
*God's Pilum:* Ranged spell attack, +12 to hit, range 120 ft, 4d8+8 piercing + 3d6 fire.  
*War Blade:* Melee weapon attack, +14 to hit, reach 10 ft, 3d10+8 slashing + 2d6 radiant.  
*Divine Smite (1/round):* On a hit, add 6d8 radiant damage. Target must succeed on DC 18 Con save or be Stunned until end of next turn.  
*War Cry (Recharge 5–6):* Each creature of Mars' choice within 60 ft makes a DC 18 Wisdom save or is Frightened for 1 minute (save again at end of each turn).  

**Legendary Actions (3/round, at end of another creature's turn)**  
*Strike:* One War Blade attack.  
*Summon Fallen (costs 2):* A Wight or Shadow appears at a point Mars designates within 60 ft. Max 3 summoned at once.  
*God's Eye (costs 3):* Mars reads one creature's deepest intention (no save). He states it aloud. If true, the creature is Frightened for 1 round.  

**Victory Condition:** Reduce to 150 HP or demonstrate *virtus* that satisfies him (DM judgment). He calls "Enough" and lowers his weapon.

---

### BUG-S5-02 — Arena Weapon Cards (Handout 11) Not Defined
**File:** `chapter5.qmd`  
**Location:** Scene 2 — Option A; Props section  
**Problem:** Handout 11 is referenced as "Arena Weapon Cards — place face down on the table when Scene 2 begins" and "Each weapon has a visible cost." But no weapons are defined anywhere.  
**Fix:** Define 5 arena weapons for Handout 11. Each card has: weapon name, attack/damage, special property, and visible cost.

**Card 1 — Gladius of Distinction:** +2 attack/damage rolls. *Sacred edge:* add 2d6 radiant on hit. *Cost:* each attack also deals 1d6 radiant to the wielder (the god's attention burns the unworthy carrier).

**Card 2 — Pilum of the Unbroken Line:** Range 60/120 ft, 2d8+4 piercing. *Formation throw:* on a hit, target must succeed DC 15 Str save or be restrained until end of next turn. *Cost:* the thrower cannot move the round they use it (they held the line).

**Card 3 — Scutum of Endurance:** Grants +3 AC. *Last stand:* when the wielder drops to 0 HP, they can drop to 1 HP instead (once only). *Cost:* the wielder has disadvantage on attack rolls while carrying it (it is a shield, not a weapon).

**Card 4 — Spear of the Veteran:** Versatile (1d6/1d8), reach 10 ft. *Disciplined strike:* if the wielder did not move this turn, the attack deals +2d6 damage. *Cost:* the wielder must end their turn where they started it if they use the bonus.

**Card 5 — War-God's Seax:** Finesse, 1d6+3 piercing. *Precision:* ignore target's AC bonus from armor (not shields). *Cost:* on a miss, the seax deals 1d4 damage to the wielder's hand — Mars accepts no wasted cuts.

---

### BUG-S5-03 — Session 5 Map Table Misidentifies Arena Location and Maps
**File:** `chapter5.qmd`  
**Location:** Maps for This Session table  
**Problem:** Session 5's divine confrontation happens on the transformed PARADE GROUND above ground (cold open: "In the center of the parade ground the sand funnels upward..."). But the map table lists `DarkTempleInterior` as "Mars' judgment arena (Scene 2)" — that is the underground vault. The parade ground is outside. DarkTempleInterior is an underground chamber.  
Additionally: `DarkTempleEntrance` is listed as "The transformed parade ground; the moment time stops" — but DarkTempleEntrance is an interior staircase, not an exterior plaza.  
**Fix:** Update Session 5 map table:

| Scene | Map file(s) | Use |
|---|---|---|
| Parade ground transformation (cold open) | `CityStreets` or `BridgeCheckpoint` | Open fort exterior; reposition as the central parade ground |
| Mars' throne and judgment arena | Use narration only (no grid needed) or `AncientAltar` | The black sand circle does not need a grid — it is described, not battlemapped |
| Option A / Option B combat | `AncientAltar` | If players need a grid for fighting Fausta or Mars |
| Retreat below fort | `CathedralCatacombs`, `AncientTombs` | If party retreats underground |
| Option B/C altar resolution | `DarkTempleInterior` | If the party descends to the vault altar as part of resolution |
| Sacred grove (epilogue) | `NatureGoddessTemple`, `IslandRuins` | Epilogue scenes, not trial scenes |

---

## Cross-Session Bugs

### BUG-CROSS-01 — "Corrupted Worker" in Session 5 Conflates Two Different Characters
**File:** `chapter5.qmd`  
**Location:** Pre-Session Continuity Tracker  
**Problem:** Session 5 continuity tracker lists "Influenced NPC survival" and "(corrupted worker lived, he appears among witnesses)." The "corrupted worker" is Marius Coda from Session 1. The "influenced NPC" is the party member possessed by the spear in Session 3. These are two entirely different people but the tracker conflates them.  
**Fix:** Separate the two entries in the continuity tracker:  
| Session | Choice | Session 5 effect |
|---|---|---|
| S1 | Marius Coda: subdued (not killed) | He appears at the arena edge among witnesses. He does not fight. He watches. If the party makes the honor argument in Option C, he speaks one sentence unprompted: "It was the spear talking. Not me. I remember now." Mars hears this. |
| S3 | Session 3 influenced NPC: survived | They stand with the party on the sand, corruption cleared. Mars looks at them and says nothing, which is the most unnerving thing he does all session. |

---

### BUG-CROSS-02 — Aelius Rufus Never Appears After Session 1
**File:** `chapter2.qmd`  
**Location:** Pre-Session Reactive World Setup  
**Problem:** Chapter 1 states: "If stabilized, Aelius Rufus survives and appears in Session 2 as someone who owes the party his life and remembers what Marius said just before the killing started." He never appears in Sessions 2–5 despite this explicit promise.  
**Fix:** Add Aelius Rufus to Session 2 Reactive World Setup table:

| NPC | Their State at Session 2 Start | Active Agenda |
|---|---|---|
| Aelius Rufus *(if stabilized in Session 1)* | Recovering in the medicus quarters, bandaged but mobile. | Find whoever saved his life and tell them what he heard: Marius said "Give it to me and I will keep you safe" while looking at whoever held the spear. That selectivity — the spear reaching toward one carrier, not randomly — is information Cassia does not have yet. |

And add a scene hook: "If the party visits the medicus quarters during Scene 2's investigation window, Aelius Rufus is there. No check required; he recognizes them and will talk."

---

### BUG-CROSS-03 — Session 3 Citizenship Window Assumes Success Path Only
**File:** `chapter3.qmd`  
**Location:** Conclusion — Citizenship Elevation section  
**Problem:** "After the spear is destroyed and the party returns to Corvinus' reach, Corvinus files papers." The failure path (ritual failed, party fleeing, siege beginning) is not addressed for citizenship purposes.  
**Fix:** Add to the citizenship section:  
> *"If the ritual failed and the party is still in the field during Session 4: Corvinus files citizenship papers after the siege ends, not before. The Session 3 window defers to the end of Session 4. The papers arrive during Session 4's conclusion scene rather than as a separate inter-session moment. The eligibility criteria are the same; only the timing shifts."*

---

### BUG-CROSS-04 — Vercingetorix's Dying Condition Has No Specified Cause
**File:** `chapter2.qmd`, `chapter3.qmd`, `chapter4.qmd`  
**Location:** Vercingetorix's Secret across all three sessions  
**Problem:** Sessions 2, 3, and 4 all list "He is dying" as Vercingetorix's secret, with Session 4 noting he is "dying faster." There is no stated cause. "Dying faster" implies acceleration but from what? Without a cause, the DM cannot describe his symptoms or answer player questions that dig into this.  
**Fix:** Add to Session 2 Vercingetorix DM Notes (and forward-reference in Sessions 3-4):  
> *"Vercingetorix is dying from a slow wasting illness — almost certainly a Roman-introduced fever disease he first contracted during trading contact with frontier settlements. His people's healers have no treatment for it. He knows what it is; he has watched it take others. He does not tell the party because it changes how they treat him, and he does not want that. In Session 4, 'dying faster' means the siege stress is accelerating the wasting. By Session 5's epilogue, he has perhaps three months."*

---

### BUG-CROSS-05 — Senator Brutus Has No OGAS Until Session 4
**File:** `chapter2.qmd`, `chapter3.qmd`  
**Location:** DM Notes — OGAS sections  
**Problem:** The Sclanders methodology designates Brutus as the "Never Present Villain" from Sessions 1-4. But he has no OGAS entry in Sessions 1, 2, or 3 — only Session 4. The DM has no reference for what Brutus is actively doing while he is off-screen, making his presence feel passive rather than active.  
**Fix:** Add "Off-Screen Villain" sidebar to Session 2 and Session 3 DM Notes:

**Session 2 — Senator Brutus (off-screen):**  
> *Objective: Prevent the spear from reaching Rome where it would pass beyond his control.*  
> *Goal this session: Get Tribune Lucius to secure or destroy the spear. Control the narrative.*  
> *Agenda: Direct orders via the Tribune. Maintain deniability. Pre-positioned Quintus Flavius as an insurance agent.*  
> *Secret: Has a secondary ritual prepared — a private ceremony conducted under different auspices — in case the Tribune fails. The fort's destruction would be acceptable to him if it prevents a public resolution.*

**Session 3 — Senator Brutus (off-screen):**  
> *Objective: Same.*  
> *Goal this session: Launch Vindolanda's siege through allied chieftains while the party is in the forest. Let the fort fall before the party returns.*  
> *Agenda: Two specific chieftains in the warband confederation owe Brutus money and old favors. They are the siege's actual organizers. Vercingetorix does not know this. Sigrun knows one name if the party can reach her.*  
> *Secret: Does not know about the grove ritual. His intelligence ends at the treeline.*

---

## Summary Table

| Bug ID | Session | Severity | Type |
|---|---|---|---|
| BUG-S1-01 | S1 | Medium | DM clarity |
| BUG-S1-02 | S1 | Low | Map organization |
| BUG-S1-03 | S1 | Low | DM guidance |
| BUG-S1-04 | S1 | Medium | Mechanical gap |
| BUG-S1-05 | S1 | Low | Handout trigger |
| BUG-S1-06 | S1 | Medium | NPC inconsistency |
| BUG-S2-01 | S2 | High | NPC name error |
| BUG-S2-02 | S2 | Medium | Plot timeline gap |
| BUG-S2-03 | S2 | Medium | Missing contingency |
| BUG-S2-04 | S2 | Low | DM note missing |
| BUG-S3-01 | S3→S4 | High | Structural continuity |
| BUG-S3-02 | S3 | High | Encounter balance |
| BUG-S4-01 | S4 | Medium | Missing callback |
| BUG-S4-02 | S4 | Medium | Spatial clarity |
| BUG-S4-03 | S4 | High | Handout content missing |
| BUG-S4-04 | S4 | Low | Map note missing |
| BUG-S5-01 | S5 | Critical | Stat block missing |
| BUG-S5-02 | S5 | High | Handout content missing |
| BUG-S5-03 | S5 | Medium | Map mismatch |
| BUG-CROSS-01 | S1/S3/S5 | Medium | NPC conflation |
| BUG-CROSS-02 | S1→S2 | Medium | Missing thread |
| BUG-CROSS-03 | S3→S4 | Medium | Missing failure path |
| BUG-CROSS-04 | S2–S4 | Low | NPC detail gap |
| BUG-CROSS-05 | S2–S3 | Medium | Villain tracking gap |

**Critical (1):** Mars stat block must be written before running Session 5.  
**High (5):** Tribune name, S3→S4 transition, Stone Golem balance, Handout 8/9 content, Arena Weapon Cards.  
**Medium (12):** Address before running each respective session.  
**Low (6):** Address during editing pass.
