# Session 5: The Wrath of Mars — MapTool Token Guide

This folder contains all tokens needed for **Session 5 (*The Wrath of Mars*)**, organized into:
1. `Ready_to_Place/`: Tokens that are 100% configured, audited, and ready to drop onto your map.
2. `Tokens_to_Update/`: Monster tokens that can have S5 sensory text and audio macros added.

---

## Scene-by-Scene Token Placement

### Scene 0: Cold Open — The Crystal Is Failing
* **Map:** `s5_mars_vault_overview.jpg` (Grid: 70px = 5 ft)
* **Party Start:** Upper spiral descent (`X: 15, Y: 5`)
  * All 6 PC tokens (`Brian`, `Iris`, `Julia_Jana`, `Rivia_Calida_Mendera`, `Tanit_bint_Abdmelqart`, `Ursula_Günther`)
* **Hazard:** Central fissure shuddering; necrotic pulse timer (DC 14 Con save after 15 rounds of lingering).

---

### Scene 1: The Sunken Armory & The Choking Hall
* **Map:** `s5_mars_vault_overview.jpg` (Zones 2 & 3; Grid: 70px = 5 ft)
* **Party Entry:** North stair (`X: 15, Y: 22`)
* **Sunken Armory (`X: 15, Y: 28`):** Untouched blade marked with Mars's ram's-eye stamp (counts as Belatucadrus-grade weapon if party missed the shrine).
* **Choking Hall (`X: 12, Y: 35` & `X: 18, Y: 35`):**
  * 2× `Wraith.rptok` (ancient legionary shades; *Incorporeal Movement* through stone walls; *Life Drain* DC 14 Con save reduces maximum HP).

---

### Scene 2: The Convergence Hall — Three Passages
* **Map:** `s5_mars_vault.jpg` (Zone 3; Grid: 70px = 5 ft)
* **Party Vestibule:** North entrance (`X: 20, Y: 8`)
* **Three Passage Options:**
  1. **West (Left) Route (`X: 10, Y: 24`):** Necrotic floor rune trap + dead cultist with journal confirming chieftains' corruption.
  2. **Center Route (`X: 19–21, Y: 25–28`):** 6× `Zombie.rptok` (marching legionary corpses; *Undead Fortitude* bypassed completely by radiant damage).
  3. **East (Right) Route (`X: 28–32, Y: 26`):** 1× `Wight.rptok` + 2× `Specter.rptok` (flanking ambush from dark alcoves; ceiling flyby).

---

### Scene 3: Vercingetorix's Last Stand (★ Climax Combat)
* **Map:** `s5_mars_vault.jpg` (Approach to Zone 4; Grid: 70px = 5 ft)
* **Party Entry:** Reconvergence arch (`X: 20, Y: 40`)
* **Portal Chokepoint (`X: 20, Y: 46`):**
  * `Vercingetorix_Bound.rptok` (CR 11 Undead Boss, AC 18, HP 150)
  * **Tactics:** Dread Spatha (10-ft reach), *Parry* (+4 AC reaction), *Fear Aura* (DC 15 Wis save).
  * **Relentless Trait:** When reduced to 0 HP, drops to 1 HP instead unless the killing blow is radiant or from a **Belatucadrus-consecrated weapon**!
  * **Final Death Revelation:** Vercingetorix reveals the 4 Caesar iron winches around the anvil before dissolving.

---

### Scene 4: The Antechamber of Mars & Threshold of Janus
* **Map:** `s5_mars_confrontation.jpg` (The Sanctum; Grid: 70px = 5 ft)
* **Sanctum Archway (`X: 25, Y: 45`):**
  * `Janus_(Threshold_Vision).rptok` (Dual-faced threshold divinity). Macro: `Voice: Threshold of Janus` (*audio/clips/s5_janus_threshold.mp3*).
* **Cameo Plinth (`X: 10, Y: 25`):**
  * `Wight_General_(Centurion_Cameo).rptok` (If spared in Session 1, spirit speaks once: *"I held this three hundred years..."* then dissolves).
* **Central Altar (`X: 25, Y: 25`):**
  * `Mars.rptok` (Diminished Avatar, CR 20, AC 22/16, HP 300).
  * 4× `Caesar_Chain_Winch.rptok`:
    * North Winch: `X: 25, Y: 15`
    * South Winch: `X: 25, Y: 35`
    * East Winch: `X: 35, Y: 25`
    * West Winch: `X: 15, Y: 25`
  * **Dynamic Unmaking Ritual (Option 1):** DC 14 Athletics locks each winch.
    * Round 1: AC drops from 22 &rarr; 19.
    * Round 2: AC drops &rarr; 16, loses legendary resistances.
    * Round 3: Mars is pinned to the anvil; Spear can be shattered with an action!
