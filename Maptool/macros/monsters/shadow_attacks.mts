<!-- Shadow (CR 1/2) Attack Macro
     Campaign macro — select the Shadow token before running.
     Standard D&D 5e stat block: AC 12, HP 16 (3d8+3)
     Import: Campaign > Edit Campaign > Macros tab > New Macro, paste this content.
-->
[h: tokenName = getName()]
[h: roll_attack = 1d20]
[h: roll_damage = 2d6]
[h: str_dc = 13]

[dialog("Shadow: Strength Drain", "width=380; height=340; temporary=true;")]
<html>
<head>
<style>
  body { font-family: Georgia, serif; background:#1a1a2e; color:#e0e0e0; padding:12px; margin:0; }
  h2 { color:#9b59b6; margin:0 0 6px 0; font-size:15px; border-bottom:1px solid #9b59b6; padding-bottom:4px; }
  .stat-row { display:flex; justify-content:space-between; font-size:12px; color:#aaa; margin-bottom:8px; }
  .attack-box { background:#2d2d4e; border:1px solid #9b59b6; border-radius:4px; padding:10px; margin-bottom:8px; }
  .label { font-size:11px; color:#9b59b6; text-transform:uppercase; letter-spacing:1px; }
  .roll { font-size:28px; font-weight:bold; color:#fff; }
  .detail { font-size:12px; color:#bbb; margin-top:4px; }
  .note { font-size:11px; color:#e67e22; background:#2c1a00; border:1px solid #e67e22; border-radius:3px; padding:6px; margin-top:8px; }
  .condition { font-size:11px; color:#3498db; background:#001a2c; border:1px solid #3498db; border-radius:3px; padding:6px; margin-top:6px; }
</style>
</head>
<body>
<h2>&#9760; SHADOW — [r: tokenName]</h2>
<div class="stat-row"><span>AC 12</span><span>HP 16</span><span>Speed 40 ft (hover)</span></div>

<div class="attack-box">
  <div class="label">Strength Drain (Melee)</div>
  <div class="roll">Attack: [r: roll_attack + 4] <span style="font-size:14px;color:#aaa;">(1d20+4)</span></div>
  <div class="detail">
    [h: dmg = 2d6]
    Damage on hit: <b>[r: dmg + 2] necrotic</b> (2d6+2)
  </div>
  <div class="condition">
    <b>Strength Drain:</b> DC [r: str_dc] Constitution save or target's Strength score reduced by 1d4.
    Humanoid reduced to 0 Strength dies and rises as a Shadow in 1d4 hours.
  </div>
</div>

<div class="attack-box">
  <div class="label">Re-roll Attack (new roll)</div>
  <div class="roll">
    [h: roll2 = 1d20]
    Attack: [r: roll2 + 4] <span style="font-size:14px;color:#aaa;">(1d20+4)</span>
  </div>
  <div class="detail">
    [h: dmg2 = 2d6]
    Damage: <b>[r: dmg2 + 2] necrotic</b>
  </div>
</div>

<div class="note">
  <b>Dim Light:</b> Shadow has ADVANTAGE on attack rolls when target is in dim light or darkness.
  Roll twice above and take higher result. Strength Drain damage also bypasses resistance to non-magical attacks.
</div>
</body>
</html>
[/dialog]
