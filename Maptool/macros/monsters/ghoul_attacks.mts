<!-- Ghoul (CR 1) Attack Macro
     Campaign macro — select the Ghoul token before running.
     Standard D&D 5e stat block: AC 12, HP 22 (5d8)
-->
[h: tokenName = getName()]

[dialog("Ghoul Attacks", "width=400; height=400; temporary=true;")]
<html>
<head>
<style>
  body { font-family: Georgia, serif; background:#1a1a1a; color:#e0e0e0; padding:12px; margin:0; }
  h2 { color:#c0392b; margin:0 0 6px 0; font-size:15px; border-bottom:1px solid #c0392b; padding-bottom:4px; }
  .stat-row { display:flex; justify-content:space-between; font-size:12px; color:#aaa; margin-bottom:8px; }
  .attack-box { background:#2a1a1a; border:1px solid #c0392b; border-radius:4px; padding:10px; margin-bottom:8px; }
  .label { font-size:11px; color:#c0392b; text-transform:uppercase; letter-spacing:1px; }
  .roll { font-size:26px; font-weight:bold; color:#fff; }
  .detail { font-size:12px; color:#bbb; margin-top:4px; }
  .note { font-size:11px; color:#e67e22; background:#2c1a00; border:1px solid #e67e22; border-radius:3px; padding:6px; margin-top:8px; }
  .condition { font-size:11px; color:#e74c3c; background:#2c0000; border:1px solid #e74c3c; border-radius:3px; padding:6px; margin-top:6px; }
</style>
</head>
<body>
<h2>&#9762; GHOUL — [r: tokenName]</h2>
<div class="stat-row"><span>AC 12</span><span>HP 22</span><span>Speed 30 ft</span></div>

<div class="attack-box">
  <div class="label">Claws (Paralyzing)</div>
  [h: atk_claw = 1d20]
  <div class="roll">Attack: [r: atk_claw + 2] <span style="font-size:14px;color:#aaa;">(1d20+2)</span></div>
  <div class="detail">
    [h: dmg_claw = 2d4]
    Damage on hit: <b>[r: dmg_claw + 2] slashing</b> (2d4+2)
  </div>
  <div class="condition">
    <b>Paralysis:</b> DC 10 Constitution save or target is Paralyzed until end of its next turn.
    On save failure, any subsequent hit by any attacker is a critical hit.
  </div>
</div>

<div class="attack-box">
  <div class="label">Bite (vs Incapacitated only)</div>
  [h: atk_bite = 1d20]
  <div class="roll">Attack: [r: atk_bite + 2] <span style="font-size:14px;color:#aaa;">(1d20+2)</span></div>
  <div class="detail">
    [h: dmg_bite = 2d6]
    Damage on hit: <b>[r: dmg_bite + 2] piercing</b> (2d6+2)
  </div>
  <div class="note">
    Only usable against a Paralyzed or Incapacitated target. Attack roll has advantage (target can't act). This attack already benefits from advantage; roll manually twice if you need to show both dice.
  </div>
</div>

<div class="attack-box" style="border-color:#888;">
  <div class="label" style="color:#888;">Undead Fortitude reminder</div>
  <div class="detail" style="color:#aaa;">Ghouls are immune to poison and the Poisoned condition. They do not need to breathe, eat, or sleep. Charmed and frightened conditions do not apply.</div>
</div>
</body>
</html>
[/dialog]
