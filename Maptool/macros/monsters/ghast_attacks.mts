<!-- Ghast (CR 2) Attack Macro
     Campaign macro — select the Ghast token before running.
     Standard D&D 5e stat block: AC 13, HP 36 (8d8)
     NOTE: Run Stench check at start of Ghast's first turn (DC 10 Con or Poisoned).
-->
[h: tokenName = getName()]

[dialog("Ghast Attacks", "width=420; height=460; temporary=true;")]
<html>
<head>
<style>
  body { font-family: Georgia, serif; background:#1a1a1a; color:#e0e0e0; padding:12px; margin:0; }
  h2 { color:#8e44ad; margin:0 0 6px 0; font-size:15px; border-bottom:1px solid #8e44ad; padding-bottom:4px; }
  .stat-row { display:flex; justify-content:space-between; font-size:12px; color:#aaa; margin-bottom:8px; }
  .attack-box { background:#1e1a2a; border:1px solid #8e44ad; border-radius:4px; padding:10px; margin-bottom:8px; }
  .label { font-size:11px; color:#8e44ad; text-transform:uppercase; letter-spacing:1px; }
  .roll { font-size:26px; font-weight:bold; color:#fff; }
  .detail { font-size:12px; color:#bbb; margin-top:4px; }
  .aura { font-size:11px; color:#f39c12; background:#2c1f00; border:1px solid #f39c12; border-radius:3px; padding:8px; margin-bottom:8px; }
  .condition { font-size:11px; color:#e74c3c; background:#2c0000; border:1px solid #e74c3c; border-radius:3px; padding:6px; margin-top:6px; }
</style>
</head>
<body>
<h2>&#9762; GHAST — [r: tokenName]</h2>
<div class="stat-row"><span>AC 13</span><span>HP 36</span><span>Speed 30 ft</span></div>

<div class="aura">
  <b>&#9888; STENCH AURA (passive):</b> Any creature that starts its turn within 5 ft must succeed on a DC 10 Constitution save or be Poisoned until the start of its next turn. On a successful save, the creature is immune to the Ghast's Stench for 24 hours. Undead and creatures that don't breathe are immune.
</div>

<div class="attack-box">
  <div class="label">Bite</div>
  [h: atk_bite = 1d20]
  <div class="roll">Attack: [r: atk_bite + 3] <span style="font-size:14px;color:#aaa;">(1d20+3)</span></div>
  <div class="detail">
    [h: dmg_bite = 2d8]
    Damage on hit: <b>[r: dmg_bite + 1] piercing</b> (2d8+1)
  </div>
  <div class="condition">
    <b>Paralysis:</b> DC 10 Constitution save or Paralyzed until end of its next turn.
  </div>
</div>

<div class="attack-box">
  <div class="label">Claws (stronger than Ghoul)</div>
  [h: atk_claw = 1d20]
  <div class="roll">Attack: [r: atk_claw + 5] <span style="font-size:14px;color:#aaa;">(1d20+5)</span></div>
  <div class="detail">
    [h: dmg_claw = 2d6]
    Damage on hit: <b>[r: dmg_claw + 3] slashing</b> (2d6+3)
  </div>
  <div class="condition">
    <b>Paralysis:</b> DC 10 Constitution save or Paralyzed until end of its next turn.
  </div>
</div>

<div class="attack-box" style="border-color:#e74c3c; background:#2c0808;">
  <div class="label" style="color:#e74c3c;">Critical vs Paralyzed target</div>
  <div class="detail">
    If the Ghast hits a Paralyzed target: automatic critical hit.
    [h: crit_bite = 4d8] Crit Bite damage: <b>[r: crit_bite + 1]</b> (4d8+1)
    [h: crit_claw = 4d6] Crit Claw damage: <b>[r: crit_claw + 3]</b> (4d6+3)
  </div>
</div>
</body>
</html>
[/dialog]
