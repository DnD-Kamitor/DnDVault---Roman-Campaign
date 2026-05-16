# Agent Task: Role Progression Trees and Class Substitution Blocks

## What this project is

A D&D 5e campaign book written in Quarto Markdown, published at:
https://dnd-kamitor.github.io/DnDVault---Roman-Campaign/

The book has a role system (`roles.qmd`) — 15 military roles for the vexillatio extraordinaria. Currently each role has a brief "Senior Advancement" block with one trigger and one bonus. This task expands that into a full branching progression tree with campaign-specific perks, and adds class substitution toggles to every role.

---

## Files to modify

- `roles.qmd` — the only file you touch

## Files NOT to touch

- `knowledge.qmd` — already fully audited, do not change
- `roman_tactics.qmd` — reference only for weapon stat blocks; do not edit
- `supplies.qmd` — separate agent task; do not edit
- `chapter1-5.qmd` — separate agent task; do not edit

---

## The tier system

Each role has three tiers:

| Tier | Requirement | What changes |
|---|---|---|
| **Standard** | 0 commendationes | Existing mechanics (already in the book) |
| **Veteranus** | 3 commendationes | Player chooses Branch A or B; gains Perk 1 |
| **Specialis** | 7 commendationes | Perk 2 unlocked on chosen branch |

Commendationes are the existing campaign advancement currency (already described in `peoples.qmd` and `gm_intro.qmd`). Do not change those files — just reference this threshold in the progression block.

Branch choice is permanent. Once a player chooses Branch A or B at Veteranus, they follow that branch to Specialis.

---

## Citizenship gate rules

Some advancement perks require minimum citizenship status. These are hard gates — the player cannot take the perk until the citizenship condition is met, even if they have enough commendationes.

| Gate label | What it means |
|---|---|
| *(Latinus+)* | Requires Latini status (3+ commendationes citizenship track, already active) |
| *(Civis)* | Requires full Roman citizenship (7+ commendationes citizenship track) |

---

## Race / background restriction rules

Some perks are locked to specific backgrounds or classes. These appear in parentheses alongside the perk name. The restriction is flavor-mechanically motivated — do not remove restrictions or replace them with generic gates.

Lock format: *(locked: [reason])* or *(requires: [condition])*.

When a perk is locked, add a one-line explanation of why in italics below the perk description. This makes the restriction feel diegetic rather than arbitrary.

---

## Class substitution rules

Every role has a standard equipment kit. When a player brings a spellcasting class to the role, the kit changes. All class substitutions are hidden inside a collapsible toggle per class.

**Format:**

```html
<details>
<summary><strong>Class equipment substitutions</strong></summary>

**Wizard / Sorcerer / Warlock:** Replace all martial weapons and medium/heavy armor with: arcane focus (rod or wand), component pouch, spellbook (Wizard only), padded armor or mage armor (Sorcerer/Warlock). Retain all non-weapon role items (tools, kits, insignia).

**Cleric / Druid:** Replace martial weapons with: holy symbol (shield-mounted counts), wooden staff or mace. Retain medium armor if class allows; replace heavy armor with scale mail if class does not allow it.

**Bard:** Replace heavy armor with leather armor. Retain all weapons the Bard has proficiency in; replace others with a hand crossbow and shortsword. Add musical instrument (mandolin or horn).

**Paladin / Ranger:** No substitution required. Retain full kit.

**Rogue:** Replace heavy armor with studded leather. Retain all one-handed weapons; replace two-handed weapons with a shortsword and hand crossbow.

**Monk:** Replace all armor with clothing (Monk's Unarmored Defense applies). Replace all weapons with: handaxe × 2 or shortsword × 1 (Monk weapons). Add 10 darts.

**Fighter / Barbarian:** No substitution required. Retain full kit.

</summary>
</details>
```

Write this block once per role, after the equipment list and before the knowledge gates. Do not repeat the full text for every class — write the actual substitution relevant to this role's kit. If a role's standard kit is already light (no heavy armor, no two-handed weapons), note "No substitution required" for the heavy-class entries rather than repeating boilerplate.

---

## Progression tree format

Place the progression block after the existing `### Senior Advancement` section in each role. Replace the existing brief Senior Advancement with the full tree — do not keep both.

**Format:**

```markdown
### Advancement

**Standard** (0 commendationes): [one-line summary of base role mechanics]

---

**Veteranus** (3 commendationes): Choose one branch.

#### Branch A: *[Branch Latin name]* — [English gloss]

**Perk 1: *[Perk Latin name]*** — [Full mechanical description. Campaign-specific: bonus to skill checks in specific circumstances, special action options, camp unlocks, or social status effects. NOT generic feats or ASIs.]

#### Branch B: *[Branch Latin name]* — [English gloss]

**Perk 1: *[Perk Latin name]*** — [Full mechanical description.]
*(requires: [condition])* ← only if gated

---

**Specialis** (7 commendationes): Perk 2 on your chosen branch.

#### Branch A (continued): *[Perk Latin name]*

**Perk 2: *[Perk Latin name]*** — [Full mechanical description.]
*(requires: [condition])* ← only if gated

#### Branch B (continued): *[Perk Latin name]*

**Perk 2: *[Perk Latin name]*** — [Full mechanical description.]
*(requires: [condition])* ← only if gated
```

---

## All 15 roles — complete specifications

Write these blocks into `roles.qmd`, one per role, replacing the existing Senior Advancement sections.

---

### 1. OPTIO (Adjutant/Second-in-Command)

**Branch A: *Ductor*** — Leader of men

**Veteranus Perk 1: *Impetus Ductoris*** — Once per short rest, when you give a verbal command to an ally who can hear you, they may immediately move up to half their speed as a reaction. This movement does not provoke opportunity attacks.

**Specialis Perk 2: *Auctoritas*** — Your command presence is recognized by all ranks. Allied NPCs under your direct command have advantage on Wisdom saving throws against fear effects. Officers who outrank you must make a DC 14 Charisma saving throw to publicly countermand your orders in front of common soldiers; on a failure, they appear indecisive and lose one step of attitude among the soldiers present.

---

**Branch B: *Scrutator*** — Investigator and disciplinarian

**Veteranus Perk 1: *Nota Suspectorum*** — You have advantage on Wisdom (Insight) checks to detect deception or gauge loyalty. When you spend at least 10 minutes interrogating a subject, the DM must tell you if the subject is actively lying, though not what the truth is.

**Specialis Perk 2: *Retes Disciplinae*** — *(Latinus+)*
You maintain a quiet network of informants within the unit. Once per session, you may learn the current location and general activity of any named soldier or camp NPC without making a check — the information is accurate to within the last 2 hours.
*Requires Latini status: disciplinary authority over Roman-born soldiers is restricted to those with legal standing.*

---

### 2. TESSERARIUS (Watch Officer / Password Keeper)

**Branch A: *Vigilator*** — Watchmaster

**Veteranus Perk 1: *Custodia Perfecta*** — You have advantage on Wisdom (Perception) checks while on guard duty or watching a fixed point. Allied characters you are directly supervising cannot be surprised while you are conscious and not incapacitated.

**Specialis Perk 2: *Patres Stationis*** — You have trained a reliable watch rotation. Once per long rest, you may designate up to two allied NPCs as your watch. While they are on duty under your direction, you and the rest of the contubernium gain the benefits of a short rest during what would otherwise be a guard shift.

---

**Branch B: *Infiltrator*** — Counterintelligence operative

**Veteranus Perk 1: *Lapsus Clandestinus*** — You have advantage on Dexterity (Stealth) checks to move through occupied civilian spaces (markets, taverns, crowds). When you follow a target for more than 1 hour without being detected, you automatically learn their next planned meeting or destination.

**Specialis Perk 2: *Persona Falsa*** — You have built a civilian cover identity registered with the Frumentarius network. Once per session, you may invoke this identity to pass as a non-military person. Any NPC not already suspicious of you must succeed on a DC 15 Wisdom (Insight) check to see through the cover.

---

### 3. AQUILIFER (Eagle Bearer)

**Branch A: *Bellator*** — Warrior-bearer

**Veteranus Perk 1: *Aquila Vincit*** — While you carry the aquila (eagle standard), allied soldiers within 30 feet have advantage on saving throws against being frightened. As a bonus action, you may issue a battle cry, granting allies within 30 feet advantage on their next attack roll before the end of their next turn.

**Specialis Perk 2: *Fortitudo Legionis*** — *(Civis)*
When you are reduced to 0 hit points while carrying the aquila, you may choose to remain conscious with 1 hit point. This feature recharges after a long rest. If the aquila falls to the ground, all allies within 60 feet must make a DC 13 Wisdom saving throw or become frightened until the start of their next turn.
*Requires full citizenship: the right to die for the aquila is a legal and religious privilege of Roman citizens.*

---

**Branch B: *Custos Aquilae*** — Sacred guardian of the eagle

**Veteranus Perk 1: *Memoria Sacra*** — You have learned the rites of the aquila's sacred maintenance. When you perform a 10-minute ritual prayer at the start of a day, roll a d6. On a 4 or higher, Mars grants a boon: all allies within 60 feet gain +1 to attack rolls until your next long rest. This ritual cannot be performed if the unit has an unresolved corruption penalty.

**Specialis Perk 2: *Nexus Aquilae*** — *(Civis + Religion proficiency)*
You are a living conduit between the unit and Mars. Once per long rest, when an ally within 60 feet would be reduced to 0 hit points, you may use your reaction to redirect that damage to the aquila instead. The aquila is treated as an object with AC 18 and 20 hit points for this purpose. If the aquila reaches 0 hit points, it is desecrated — a major narrative consequence.
*Requires citizenship and religious training: this rite is reserved for those bound to Rome by law and to Mars by vocation.*

---

### 4. SIGNIFER (Standard Bearer / Pay Officer)

**Branch A: *Auctor*** — Financial guardian

**Veteranus Perk 1: *Peculium Augetur*** — You have direct access to the unit's savings account. Once per session, you may draw up to 15 gold pieces from the unit's collective fund (tracked as a shared resource). You gain advantage on Charisma (Persuasion) checks with merchants and bankers when citing official legion accounts.

**Specialis Perk 2: *Creditum Imperiale*** — Your reputation as an honest signifer opens doors in Roman financial networks. You can secure credit of up to 50 gold pieces from any Roman merchant or banker without collateral, repayable within 30 days. Military NPCs treat you as one rank higher for social interaction purposes when financial matters are in play.

---

**Branch B: *Cerberus*** — Debt enforcer

**Veteranus Perk 1: *Nexus Debitorum*** — You know precisely who owes what to whom across the camp and vicus. Once per session, you may reveal that a named NPC owes the unit a formal debt (the DM must make this debt real and plot-relevant going forward). NPCs who owe you money have disadvantage on Charisma checks made against you.

**Specialis Perk 2: *Retes Pecuniae*** — You have become the informal banker of the region. You learn automatically when any named NPC in or near the camp receives or spends a significant sum (20 gp or more). Once per session, you may intercept, freeze, or redirect one such payment, with narrative consequences determined by the DM.

---

### 5. CORNICEN (Horn-Blower / Signal Corps)

**Branch A: *Tubicen*** — Signal master

**Veteranus Perk 1: *Signale Perturbans*** — As an action, you may sound a false or contradictory tactical signal. All enemies within 60 feet who can hear it must succeed on a DC 13 Wisdom saving throw or spend their next action following the false signal rather than their intended action.

**Specialis Perk 2: *Maeander Hostium*** — After observing a coordinated group of enemies for 1 minute, you can predict their next tactical movement. The DM must describe their intended formation shift, retreat trigger, or next coordinated action before it occurs. This works once per encounter.

---

**Branch B: *Praeceptor*** — Teacher and cultural bridge

**Veteranus Perk 1: *Vox Concordiae*** — *(requires Performance proficiency)*
Your music creates genuine morale improvement. During a short rest, you may perform to allow allies who can hear you to spend one fewer Hit Die while gaining the same healing. Alternatively, your performance can reduce one unit member's exhaustion level by 1 (once per long rest).
*Requires Performance proficiency: the diplomatic power of music demands formal training.*

**Specialis Perk 2: *Lingua Barbarorum*** — You have used music as a bridge across the cultural divide. You learn one barbarian language of your choice (Germanic, Celtic, or Dacian). Allied Germanic NPCs have their initial attitude improved by one step toward you. You can attempt to communicate through music with creatures that share no language with you, using a Performance check contested by the creature's Insight.

---

### 6. MEDICUS (Camp Doctor)

**Branch A: *Archiater*** — Field surgeon

**Veteranus Perk 1: *Periculum Superatur*** — When you stabilize a dying creature using Medicine, they regain 1 hit point rather than remaining at 0. When you spend a healer's kit charge to restore hit points, the target regains the maximum result for that die (no roll; treat as average plus Constitution modifier).

**Specialis Perk 2: *Chirurgia Magistra*** — Once per long rest, you may perform emergency surgery on a willing creature during a short rest. The target regains hit points as if they had spent all their Hit Dice (roll them all, add Constitution modifier per die), but they must complete a long rest before benefiting from this feature again.

---

**Branch B: *Toxicologus*** — Poison and disease specialist

**Veteranus Perk 1: *Venena Nota*** — You have advantage on Intelligence (Medicine) checks to identify poisons, diseases, and drugs. When you examine a poisoned creature, you automatically learn the poison's name and its effects — though not necessarily its source.

**Specialis Perk 2: *Antidotum Perfectum*** — During a short rest, you may prepare an antidote to any poison you have previously identified. This antidote cures the poison without requiring a saving throw and grants the target advantage on Constitution saving throws against that specific poison for 24 hours. You may have one antidote prepared at a time.

---

### 7. HARUSPEX (Diviner / Entrail Reader)

**Branch A: *Augur Publicus*** — Official Roman diviner

**Veteranus Perk 1: *Prodigium Declaratum*** — Once per session, you may formally declare that an omen is favorable or unfavorable for a specific planned action. If favorable: allies gain advantage on their first attack roll or ability check in the relevant encounter. If unfavorable: the DM must introduce at least one additional warning or complication before any consequence arrives.

**Specialis Perk 2: *Auspicia Maxima*** — *(Civis)*
Your auguries carry legal force. Military commanders must delay major operations by at least one day if you formally declare the omens adverse, following Roman religious law. This grants the party one additional planning scene before any time-pressured encounter.
*Requires full citizenship: the legal authority to halt military action on religious grounds belongs only to Roman citizens under the lex auguralis.*

---

**Branch B: *Mystes*** — Mystery tradition initiate

**Veteranus Perk 1: *Ritus Antiquus*** — *(locked: Soldier background only)*
You have been initiated into pre-Roman ritual practices that survived in the military's folk religion. You may perform a 1-hour ceremony to commune with local spirits. The DM reveals one hidden fact about the current location: an environmental truth, a historical event, or a spiritual significance — not a secret about a specific NPC.
*Locked to Soldier background: knowledge of the old rites survives among long-service soldiers, not civilians.*

**Specialis Perk 2: *Theologia Vetusta*** — You have reconciled Roman official religion with older local traditions, creating a personal theology recognized by neither but respected by both. You may speak with local spirits as if using the *speak with dead* spell (once per long rest), but the spirits are genii loci tied to the land, not the dead. Answers concern the land and its history, not specific individuals.

---

### 8. FABER (Engineer / Craftsman)

**Branch A: *Architectus*** — Field engineer

**Veteranus Perk 1: *Machina Belli*** — You can build or repair a siege engine (ballista, scorpio, onager) in half the listed construction time and at 75% of the listed cost. When you operate a siege engine you personally helped build or maintain, you add your proficiency bonus to damage rolls.

**Specialis Perk 2: *Castrametatio Perfecta*** — During a long rest in the field, you may direct the unit to construct basic field fortifications: palisade stakes, a ditch, and a firing platform. These grant allies inside +2 to AC against ranged attacks and advantage on Wisdom (Perception) checks until the fortifications are dismantled.

---

**Branch B: *Demolitor*** — Demolitions and siege-breaking

**Veteranus Perk 1: *Calx Viva*** — You have learned to weaponize quicklime, pitch, and fire. During a short rest, you may prepare one incendiary device. When thrown (range 20/60), it covers a 10-foot-radius area: creatures in the area must succeed on a DC 14 Dexterity saving throw or take 2d6 fire damage; the area becomes difficult terrain for 1 minute.

**Specialis Perk 2: *Destructor Murorum*** — After studying a wall, fortification, or structure for 1 minute, you can identify its exact structural weakness. Siege checks targeting structures you have assessed are made with advantage, and the DM must tell you the minimum force (or exact placement) needed to bring down a specific section.

---

### 9. LIBRARIUS (Clerk / Administrative Officer)

**Branch A: *Cornicularius*** — Senior administrator

**Veteranus Perk 1: *Archivum Legionis*** — You have memorized legion administrative procedure. You can produce authentic-looking military documentation (orders, travel passes, census entries, duty rosters) in 10 minutes. The DC to detect your forgeries is equal to your Intelligence (Forgery Kit or Calligrapher's Tools) check result. You have advantage on Intelligence (History) checks related to Roman law and administration.

**Specialis Perk 2: *Auctoritas Scriba*** — *(Latinus+)*
Your administrative authority is recognized formally. Once per session, you may invoke administrative procedure to delay any official action (arrest, requisition, formal investigation) by 24 hours, citing pending paperwork, missing authorizations, or required review. The delay is procedurally legitimate and cannot be overridden without a scene.
*Requires Latini status: administrative authority to obstruct official action requires recognized legal standing.*

---

**Branch B: *Agens in Rebus*** — Imperial intelligence operative

**Veteranus Perk 1: *Persona Non Grata*** — *(locked: Outlander background only)*
You know how to erase administrative traces. Once per session, you may remove a named NPC (or yourself) from one official record — travel papers, census rolls, duty roster, or tribunal record. The erasure is detectable on a DC 16 Intelligence (Investigation) check.
*Locked to Outlander background: only those who have lived outside Roman record-keeping understand how to unmake it.*

**Specialis Perk 2: *Rete Secretorum*** — *(locked: Paladin class only)*
You have assembled a network of verified, trustworthy informants across the Limes, and the Paladin's divine sense makes you a reliable node in the network. Once per session, you may send an encrypted message and receive a reply within 24 hours from any named fort within 100 miles of your location.
*Locked to Paladin class: divine sense provides the verification system that makes the network's communications secure.*

---

### 10. EXPLORATOR (Scout / Forward Observer)

**Branch A: *Speculare*** — Scout-specialist

**Veteranus Perk 1: *Vestigia Legere*** — You can track creatures across any terrain type without penalty. When you spend at least 10 minutes examining a location, you can reconstruct a precise account of events that occurred there within the last 24 hours: who was present, what they did, and in what order.

**Specialis Perk 2: *Silva Nota*** — You have mapped the surrounding wilderness in systematic detail. The party cannot be surprised when traveling through terrain you have previously scouted (within the current campaign region). Once per long rest, you may declare that you know a hidden route: the party avoids one random encounter and arrives 2 hours earlier than expected.

---

**Branch B: *Reticularius*** — Contact network handler

**Veteranus Perk 1: *Amici in Tenebris*** — *(requires Charisma 12 or higher)*
You have cultivated a web of civilian informants: farmers, traders, and shepherds who report to you. Once per session, you may contact a local informant who can provide current information about enemy movements, strangers, or unusual events within a 30-mile radius.
*Requires Charisma 12: this network is built on personal trust, not rank or pay.*

**Specialis Perk 2: *Larva*** — You have built a cover identity in the local civilian population, known under a false name and trade. NPCs do not connect you to the legion unless they have seen you in uniform or been told otherwise. You can move through civilian areas without triggering military-related wariness in NPCs, and hostile forces tracking the unit do not count you as a military target in civilian disguise.

---

### 11. FRUMENTARIUS (Imperial Supply Officer / Intelligence Agent)

**Branch A: *Annonarius*** — Supply officer

**Veteranus Perk 1: *Cursus Annonae*** — You have mastered legion supply chain procedure. Once per session, you may requisition one item from the legion's stores (worth up to 25 gp) without payment, citing operational necessity. A commanding officer must make a DC 14 Charisma (Persuasion) check to formally deny the requisition; on a failure, the denial creates a paper record that reflects poorly on the officer.

**Specialis Perk 2: *Praefectus Annonae*** — *(Civis)*
Your supply authority is formally recognized. You may redirect supplies between units without approval. Once per session, you may transfer one supply category (food, arrows, healing kits, repair materials) from another unit's allocation to yours, with no check required. The transfer creates an official record that the DM tracks as a narrative consequence.
*Requires full citizenship: formal authority over inter-unit supply distribution is restricted to citizens under the annona regulations.*

---

**Branch B: *Senior Frumentarius*** — Intelligence officer

**Veteranus Perk 1: *Suspecti Inversi*** — *(Civis)*
You have turned an enemy informant. Once per session, you may reveal that a named NPC is secretly working for you. The DM makes this real retroactively, but the informant's information may be outdated, incomplete, or colored by their original loyalties.
*Requires full citizenship: Frumentarii intelligence operations above supply cover require citizen authorization under the emperor's direct mandate.*

**Specialis Perk 2: *Speculator Principis*** — *(Civis + Deception proficiency)*
You have direct access to Frumentarius command structure. Once per session, you may submit an official report triggering an investigation into any named NPC. The investigation begins within 3 days. NPCs who know or suspect your Frumentarius affiliation have disadvantage on Charisma checks made against you.
*Requires citizenship and Deception training: operating at this level demands both legal standing and the ability to lie convincingly to superiors.*

---

### 12. SACERDOS (Camp Priest)

**Branch A: *Pontifex*** — Official military priest

**Veteranus Perk 1: *Benedictio Militum*** — During a short rest, you may lead a formal prayer to the tutelary deity of your choice. Allies who participate gain temporary hit points equal to your Wisdom modifier plus your proficiency bonus. Each ally may only benefit from this once per long rest.

**Specialis Perk 2: *Prodigium Imperativum*** — *(Civis)*
Your priestly authority can compel action on religious grounds. Once per session, you may declare a religious emergency (*prodigium*) requiring immediate attention. This declaration overrides non-military orders for up to 24 hours and grants the party access to restricted areas or personnel on religious grounds, with no check required.
*Requires full citizenship: the authority to invoke prodigium with legal force belongs only to citizens eligible for the collegium of Roman priests.*

---

**Branch B: *Confessor*** — Spiritual counselor

**Veteranus Perk 1: *Confessio Tacita*** — Soldiers and camp residents trust you with things they would not tell anyone else. Once per session, a named NPC who interacts with you for 10 minutes or more will share one piece of information they would not normally reveal — not necessarily their deepest secret, but something genuine and useful. This works only on willing NPCs not currently under duress.

**Specialis Perk 2: *Sanctuarium*** — *(locked: City Watch or Soldier background only)*
You may formally declare a space sacred. Any combat within a declared sanctuary requires all participants to make a DC 14 Wisdom saving throw or have disadvantage on attack rolls until the start of their next turn. The space does not prevent violence, but violation carries immediate social and legal consequences the DM must honor.
*Locked to law-enforcement backgrounds: only those who know what sanctuary means under Roman law know how to invoke it with force.*

---

### 13. FLAMEN MARTIALIS (Priest of Mars / War-Priest)

**Branch A: *Bellator Dei*** — Divine warrior

**Veteranus Perk 1: *Devotio Maior*** — *(Civis + freeborn status only)*
You have sworn the greater devotio, consecrating your kills to Mars. Once per long rest, when you reduce an enemy to 0 hit points, you may consecrate the kill. Until the end of your next turn, you add your proficiency bonus to all damage rolls. Using this feature increases your Corruption by 1.
*Requires full citizenship and freeborn status: the devotio is a Roman legal-religious act that requires free Roman ancestry to be valid in the eyes of Mars.*

**Specialis Perk 2: *Hasta Sacra*** — *(locked: Charlatan background excluded)*
You carry a weapon consecrated in the original ceremony of the Flamen Dialis rite. This weapon counts as magical for overcoming damage resistances. Once per long rest, when you hit with this weapon, the target must make a DC 14 Constitution saving throw or become frightened of Mars himself (not you) for 1 minute.
*Excluded from Charlatan background: the consecration ceremony requires genuine devotion; the rite fails for those whose faith is performance.*

---

**Branch B: *Mysteriarch*** — Mystery rite leader

**Veteranus Perk 1: *Tria Arma*** — *(locked: requires genuine Mars worship — not available to those whose primary allegiance is to another deity)*
You have received the three sacred weapons of Mars in ritual vision. Once per short rest, when you make a weapon attack with a spear, javelin, or sword, you may call on Mars to guide the strike. The attack is made with advantage. If it hits, it deals maximum damage dice (do not roll; treat each die as its maximum value).
*Locked to Mars worshippers: the Tria Arma is a martial vision given only to those who have sworn primary allegiance to Mars.*

**Specialis Perk 2: *Fax Martis*** — *(locked: requires freeborn Roman ancestry — not available to freed slaves or those of non-Roman parentage)*
Once per long rest, as an action, you invoke the Torch of Mars. For 1 minute, a 10-foot-radius area around you sheds bright light. Undead within this light have disadvantage on all attack rolls. Allied soldiers within the light who are below half their hit point maximum regain 1d6 hit points at the start of each of their turns.
*Locked to freeborn Romans: Mars grants his torch only to those whose blood belongs to Rome by birth and law.*

---

### 14. CAPSARIUS (Combat Medic / Stretcher Bearer)

**Branch A: *Ambulans*** — Combat medic

**Veteranus Perk 1: *Celeritas Medici*** — When you use your action to administer healing (including a healing spell, healer's kit, or Medicus feature), you may move up to half your speed before or after the action without provoking opportunity attacks. You can drag an unconscious creature up to your full speed as part of this movement.

**Specialis Perk 2: *Triage Perfecta*** — Once per encounter, when you treat a downed ally as a bonus action, you choose the outcome: you may either stabilize them normally, or restore them to 1 hit point and allow them to act on their next turn (rather than waiting a full round to regain consciousness after stabilization).

---

**Branch B: *Herbalista*** — Field herbalist

**Veteranus Perk 1: *Pharmacopoeia Militaris*** — *(locked: Urban backgrounds only — Criminal, Charlatan, Guild Artisan, Noble, Urchin)*
During a long rest in any settled area (camp, vicus, town), you may restock your healer's kit to full charges without paying, sourcing from local herbalists and markets. In the field, you can identify medicinal plants with a DC 10 Intelligence (Nature) check and create 1d4 healer's kit charges worth of healing supplies per long rest.
*Locked to Urban backgrounds: knowledge of where to find and barter for medicinal components requires familiarity with markets and apothecary networks.*

**Specialis Perk 2: *Andromeda Secretum*** — You have developed a compound with no Roman name, its recipe taught by a Germanic captive healer. Once per long rest, you may administer it to a willing creature. For the next 24 hours, the target does not need to eat or sleep, gains advantage on Constitution saving throws, and cannot be affected by natural disease. The compound is mildly addictive. The DM tracks the narrative consequences of extended use.

---

### 15. CUSTOS ARMORUM (Armory Master)

**Branch A: *Praefectus Armorum*** — Armory master

**Veteranus Perk 1: *Visio Armorum*** — You can identify any weapon or piece of armor by sight alone. You know its exact condition, estimated remaining durability, and whether it has been modified, damaged, or sabotaged. Any weapon or armor that you personally maintain grants +1 to its associated roll (attack roll or AC) while in good condition.

**Specialis Perk 2: *Inventarium Perfectum*** — Your armory records are exact. Any weapon theft, unauthorized modification, or equipment sabotage affecting items under your oversight is automatically detected by you within 24 hours. Once per session, you may loan a named item from armory stores (worth up to 50 gp) to the party — an item that "fell off the manifest" and carries no official record of transfer.

---

**Branch B: *Mercator*** — Black market dealer

**Veteranus Perk 1: *Furtivus Commercium*** — *(locked: Soldier or City Watch background — military family only)*
You have established contacts in the military black market. You can acquire any mundane item (including controlled or otherwise restricted goods) in any settlement, at 150% of standard cost, within 1d4 days. You are never asked where you obtained the goods.
*Locked to military backgrounds: knowledge of which supply officers to bribe, and how, is insider knowledge from service.*

**Specialis Perk 2: *Res Obscurae*** — *(locked: Paladin class only)*
You have handled enough military contraband, cursed weapons, and spiritually charged items that you have developed an instinct for what is wrong about an object. When you handle an item for 1 minute, you learn whether it is magical, cursed, or spiritually significant — though not what it does or how to use it.
*Locked to Paladin class: the Paladin's divine sense underlies this ability; it is not experience alone but sensitivity to the divine.*

---

## Where to insert content in roles.qmd

For each role, locate the heading structure:
- `### Senior Advancement` (or similar)

Replace the existing Senior Advancement block entirely with the new `### Advancement` block using the full tier format above.

Locate the equipment list section for each role (usually preceded by `### Starting Equipment` or a similar heading). Insert the `<details><summary>Class equipment substitutions</summary>...</details>` block immediately after the equipment list and before the first knowledge gate collapsible.

Do not reorder any other sections. Do not change NPC holders, pay rates, or mechanical prerequisites. Do not edit the knowledge gate collapsibles (DC checks) — those are handled by a separate audit.

---

## Style rules (do not violate)

- **No em dashes (--) in prose.** Use a colon, semicolon, or comma. The ` — ` separator in headings (`**Perk Name: *Latin*** — Description`) is a formatting separator, not prose punctuation, and is permitted.
- **No AI attribution** anywhere in content files.
- **Latin words in italics** when they appear in prose.
- **Do not change content** — fix only the advancement structure. Do not alter OGAS tables, scene descriptions, NPC names, or campaign lore.
- **Do not add or remove whole sections** beyond replacing Senior Advancement with the new Advancement block.
- Campaign-specific perks only. Do not award feats or Ability Score Improvements — those come from standard 5e leveling.

---

## When done

Report:
- Which roles were updated
- How many class substitution blocks were added
- Any roles where the existing Senior Advancement section could not be located (so the human can check manually)
