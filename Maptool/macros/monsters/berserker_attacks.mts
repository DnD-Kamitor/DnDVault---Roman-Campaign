<!-- Berserker (CR 2) Attack Macro
     Campaign macro — select the Berserker token before running.
     Standard D&D 5e stat block: AC 13 (hide armor), HP 67 (9d8+27)
     CAMPAIGN NOTE: This is a corruption-maddened Roman soldier. He targets
     whoever holds the spear exclusively. If no one holds it, closest party member.
-->
[h: tokenName = getName()]

[dialog("Berserker: Corruption-Maddened", "width=400; height=380; temporary=true;")]
<html>
<head>
<style>
  body { font-family: Georgia, serif; background:#1a0a00; color:#e0e0e0; padding:12px; margin:0; }
  h2 { color:#e74c3c; margin:0 0 4px 0; font-size:15px; border-bottom:1px solid #e74c3c; padding-bottom:4px; }
  .subtitle { font-size:11px; color:#888; margin-bottom:8px; font-style:italic; }
  .stat-row { display:flex; justify-content:space-between; font-size:12px; color:#aaa; margin-bottom:8px; }
  .attack-box { background:#2a0a00; border:1px solid #e74c3c; border-radius:4px; padding:10px; margin-bottom:8px; }
  .label { font-size:11px; color:#e74c3c; text-transform:uppercase; letter-spacing:1px; }
  .roll { font-size:28px; font-weight:bold; color:#fff; }
  .detail { font-size:12px; color:#bbb; margin-top:4px; }
  .reckless { font-size:11px; color:#f39c12; background:#2c1a00; border:1px solid #f39c12; border-radius:3px; padding:8px; margin-bottom:8px; }
  .roleplay { font-size:11px; color:#9b59b6; background:#1a001a; border:1px solid #9b59b6; border-radius:3px; padding:6px; margin-top:6px; }
</style>
</head>
<body>
<h2>&#9876; BERSERKER — [r: tokenName]</h2>
<div class="subtitle">Corruption Stage 3 — no longer responds to orders</div>
<div class="stat-row"><span>AC 13 (hide)</span><span>HP 67</span><span>Speed 30 ft</span></div>

<div class="reckless">
  <b>&#9888; RECKLESS (each turn, Berserker's choice):</b> At the start of his turn, the Berserker can gain advantage on ALL melee attack rolls this turn. If he does, ALL attack rolls against him have advantage until the start of his next turn. A maddened Berserker almost always uses this.
</div>

<div class="attack-box">
  <div class="label">Greataxe — Normal</div>
  [h: atk1 = 1d20]
  <div class="roll">Attack: [r: atk1 + 5] <span style="font-size:14px;color:#aaa;">(1d20+5)</span></div>
  <div class="detail">
    [h: dmg1 = 1d12]
    Damage: <b>[r: dmg1 + 3] slashing</b> (1d12+3)
  </div>
</div>

<div class="attack-box" style="border-color:#f39c12;">
  <div class="label" style="color:#f39c12;">Greataxe — Reckless (roll twice, take higher)</div>
  [h: r_atk1 = 1d20]
  [h: r_atk2 = 1d20]
  [h: r_best = if(r_atk1 >= r_atk2, r_atk1 + 5, r_atk2 + 5)]
  <div class="roll">Attack: [r: r_best] <span style="font-size:14px;color:#aaa;">(rolled [r: r_atk1] / [r: r_atk2])</span></div>
  <div class="detail">
    [h: r_dmg = 1d12]
    Damage: <b>[r: r_dmg + 3] slashing</b> — remember attackers also have advantage vs him
  </div>
</div>

<div class="roleplay">
  <b>Behaviour:</b> He screams "WHERE IS IT — GIVE IT TO ME — IT'S MINE" and attacks whoever holds the spear. If the spear is put down, he still charges the last person who held it. Two Cultists nearby are not attacking but muttering and watching — they break the trance if the Berserker is subdued.
</div>
</body>
</html>
[/dialog]
