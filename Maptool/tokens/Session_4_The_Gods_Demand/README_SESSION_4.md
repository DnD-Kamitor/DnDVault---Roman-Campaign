# Session 4: The God's Demand — MapTool Token Guide

This folder contains all tokens needed for **Session 4 (*The God's Demand*)**, organized into:
1. `Ready_to_Place/`: Tokens that are 100% configured, audited, and ready to drop onto your map.
2. `Tokens_to_Update/`: Monster tokens that can have S4 sensory text and audio macros added.

---

## Scene-by-Scene Token Placement

### Scene 0: The Farbog Crossing
* **Map:** `s3_farbog_crossing.html` or `SkeletonFortressEntrancePublic.jpg` (Grid: 50px = 5 ft)
* **Party Start:** South bank (`X: 12, Y: 45`)
  * `Rivia_Calida_Mendera.rptok` (Macro: `Box Cataclysm Aura` — causes disadvantage on calm diplomacy within 30 ft and alerts undead at double range)
  * `Ursula_Günther.rptok` (Macro: `Secondary Weapons` — spatha / spear / javelins; greataxe sealed)
  * `Brian.rptok`, `Iris.rptok`, `Julia_Jana.rptok`, `Tanit_bint_Abdmelqart.rptok`
* **Props & Hazards:**
  * `Bone_Token_OTHALAN.rptok` at the Standing Stone (`X: 15, Y: 40`).
* **Encounter (Mid-Causeway `X: 18–22, Y: 24–28`):**
  * 3× `Wight.rptok` (lurk in acidic mire to pull PCs down)
  * 3× `Banshee.rptok` (wailing spirits rising from the bog; audio: `s4_banshee_dread_mother.mp3`)

---

### Scene 1: The Germanic Village
* **Map:** `s3_germanic_village.html` (Grid: 50px = 5 ft)
* **Party Entry:** South trail (`X: 10, Y: 30`)
* **NPCs at Central Hearth (`X: 20, Y: 18`):**
  * `Sigrun_the_Trader.rptok`
  * `Arnulf_the_Firekeeper.rptok`
  * Villagers reveal Thusnelda has gone north to the Sacred Grove to "settle the debt."

---

### Scene 2: The Sacred Grove
* **Map:** `s4_sacred_grove.html` (Grid: 50px = 5 ft)
* **Party Approach:** South treeline (`X: 14, Y: 35`)
* **Prop Token at Grove Center (`X: 14, Y: 22`):**
  * `Belatucadrus_Shrine.rptok` (`OBJECT` Layer)
  * **Consecration Rule:** Blood sacrifice (1d4 piercing) consecrates one weapon. The weapon deals radiant damage and **BYPASSES Vercingetorix's Relentless recovery trait** in Session 5!

---

### Scene 3: The Ritual Sacrifice Circle
* **Map:** Same `s4_sacred_grove.html` map (Standing stone circle at north clearing)
* **Center of 7 Stones (`X: 28, Y: 15`):**
  * `Thusnelda.rptok` (Male völva seer, Druid 5, AC 13, HP 38)
  * **Ritual Clock:** 3 rounds before self-sacrifice. Macro button: `Ritual Clock (Round 1-3)`.
  * **Aura Interaction:** Persuasion checks have disadvantage if Rivia's box is carried within 30 ft.

---

### Scene 4: The Skull Entrance (★ Combat)
* **Map:** `SkeletonFortressEntrancePublic.jpg` (Grid: 70px = 5 ft)
* **Party Start:** Offering path base (`X: 15, Y: 38`)
* **Guardians:**
  * 2× `Bone_Naga.rptok` at stair foot (`X: 14, Y: 14` & `X: 16, Y: 14`) — spellcasting, bite poison, bludgeoning vulnerability.
  * 4× `Skeleton.rptok` on bone piles (`X: 12, Y: 16` & `X: 18, Y: 16`) — animate on initiative count 20.

---

### Scene 5: The Ossuary & Deep Vault Threshold
* **Map:** `Blood-Cult-Dungeon-Gridded-29x43-MapPublic.jpg` (West skull chamber; Grid: 70px = 5 ft)
* **Party Entry:** West entry stairs (`X: 4, Y: 21`)
* **West Chamber:** Curated bone piles and tally sticks. Advance party to **Level 6** here!
* **Deeper Encounters (Session 4 Climax / S5 Transition):**
  * **Blood-Growth Rooms:** 1× `Yochlol.rptok` (`X: 18, Y: 14`) + 2× `Dretch.rptok` (`X: 16, Y: 12` & `X: 20, Y: 16`)
  * **Minor Altar:** 3× `Shadow_Demon.rptok` (`X: 15, Y: 28` & `X: 19, Y: 28`)
  * **Gathering Hall:** 3× `Wraith.rptok` (`X: 15, Y: 38`) — audio: `s4_wraith_chieftain_confession.mp3`
  * **Core Room:** 1× `Glabrezu.rptok` (`X: 15, Y: 15` on dais) — audio: `s4_glabrezu_core_entrance.mp3`
