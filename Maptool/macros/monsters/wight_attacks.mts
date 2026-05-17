<!-- Wight (CR 3) Attack Macro
     Campaign macro — select the Wight token before running.
     Standard D&D 5e stat block: AC 14, HP 45 (6d8+18)
     CAMPAIGN NOTE: This Wight is the vault guardian (High Priest). He does not attack
     unless the party insists on taking the spear. He speaks before combat.
-->
[h: tokenName = getName()]

[dialog("Wight: Guardian of the Vault", "width=420; height=480; temporary=true;")]
<html>
<head>
<style>
  body { font-family: Georgia, serif; background:#0d1117; color:#e0e0e0; padding:12px; margin:0; }
  h2 { color:#e8c547; margin:0 0 4px 0; font-size:15px; border-bottom:1px solid #e8c547; padding-bottom:4px; }
  .subtitle { font-size:11px; color:#888; margin-bottom:8px; font-style:italic; }
  .stat-row { display:flex; justify-content:space-between; font-size:12px; color:#aaa; margin-bottom:8px; }
  .attack-box { background:#1a1f0d; border:1px solid #e8c547; border-radius:4px; padding:10px; margin-bottom:8px; }
  .label { font-size:11px; color:#e8c547; text-transform:uppercase; letter-spacing:1px; }
  .roll { font-size:26px; font-weight:bold; color:#fff; }
  .detail { font-size:12px; color:#bbb; margin-top:4px; }
  .condition { font-size:11px; color:#e74c3c; background:#2c0000; border:1px solid #e74c3c; border-radius:3px; padding:6px; margin-top:6px; }
  .roleplay { font-size:11px; color:#3498db; background:#001a2c; border:1px solid #3498db; border-radius:3px; padding:8px; margin-bottom:8px; }
  .resist { font-size:11px; color:#27ae60; background:#001a0d; border:1px solid #27ae60; border-radius:3px; padding:6px; margin-top:6px; }
</style>
</head>
<body>
<h2>&#9876; WIGHT — [r: tokenName]</h2>
<div class="subtitle">Vault Guardian — High Priest of the Binding</div>
<div class="stat-row"><span>AC 14 (studded leather)</span><span>HP 45</span><span>Speed 30 ft</span></div>

<div class="roleplay">
  <b>Before combat:</b> The Wight does not attack immediately. He is waiting, not hunting. He speaks only if the party attempts to take the spear. DC 14 Persuasion (advantage with contract scroll) may pause combat — see chapter1.qmd for his speech.
</div>

<div class="attack-box">
  <div class="label">Life Drain (priority target: whoever reaches for the spear)</div>
  [h: atk_drain = 1d20]
  <div class="roll">Attack: [r: atk_drain + 4] <span style="font-size:14px;color:#aaa;">(1d20+4)</span></div>
  <div class="detail">
    [h: dmg_drain = 1d6]
    Damage on hit: <b>[r: dmg_drain + 2] necrotic</b> (1d6+2)
  </div>
  <div class="condition">
    <b>Max HP Reduction:</b> DC 13 Constitution save or target's HP maximum reduced by the necrotic damage dealt. Reduction lasts until the target finishes a long rest. Target dies if reduced to 0 max HP and rises as a Wight under Wight's control.
  </div>
</div>

<div class="attack-box">
  <div class="label">Longsword</div>
  [h: atk_sword = 1d20]
  <div class="roll">Attack: [r: atk_sword + 4] <span style="font-size:14px;color:#aaa;">(1d20+4)</span></div>
  <div class="detail">
    [h: dmg_sword = 1d8]
    One-handed: <b>[r: dmg_sword + 2] slashing</b> (1d8+2)
    [h: dmg_two = 1d10]
    Two-handed: <b>[r: dmg_two + 2] slashing</b> (1d10+2)
  </div>
</div>

<div class="attack-box">
  <div class="label">Longbow (ranged)</div>
  [h: atk_bow = 1d20]
  <div class="roll">Attack: [r: atk_bow + 4] <span style="font-size:14px;color:#aaa;">(1d20+4)</span></div>
  <div class="detail">
    [h: dmg_bow = 1d8]
    Damage: <b>[r: dmg_bow + 2] piercing</b> (1d8+2) — Range 150/600 ft
  </div>
</div>

<div class="resist">
  <b>Resistances:</b> necrotic; bludgeoning/piercing/slashing from non-silvered, non-magical weapons.
  <b>Immunities:</b> poison, exhaustion, Frightened, Poisoned.
  <b>Darkvision</b> 60 ft. <b>Sunlight sensitivity:</b> disadvantage on attack rolls and Perception in sunlight.
</div>
</body>
</html>
[/dialog]
