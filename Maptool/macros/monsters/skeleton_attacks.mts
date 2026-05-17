<!-- Skeleton (CR 1/4) Attack Macro
     Campaign macro — select the Skeleton token before running.
     Standard D&D 5e stat block: AC 13 (armor scraps), HP 13 (2d8+4)
-->
[h: tokenName = getName()]

[dialog("Skeleton Attacks", "width=380; height=320; temporary=true;")]
<html>
<head>
<style>
  body { font-family: Georgia, serif; background:#1a1a1a; color:#e0e0e0; padding:12px; margin:0; }
  h2 { color:#95a5a6; margin:0 0 6px 0; font-size:15px; border-bottom:1px solid #95a5a6; padding-bottom:4px; }
  .stat-row { display:flex; justify-content:space-between; font-size:12px; color:#aaa; margin-bottom:8px; }
  .attack-box { background:#1a1a1a; border:1px solid #7f8c8d; border-radius:4px; padding:10px; margin-bottom:8px; }
  .label { font-size:11px; color:#95a5a6; text-transform:uppercase; letter-spacing:1px; }
  .roll { font-size:26px; font-weight:bold; color:#fff; }
  .detail { font-size:12px; color:#bbb; margin-top:4px; }
  .resist { font-size:11px; color:#27ae60; background:#001a0d; border:1px solid #27ae60; border-radius:3px; padding:6px; margin-top:8px; }
</style>
</head>
<body>
<h2>&#9760; SKELETON — [r: tokenName]</h2>
<div class="stat-row"><span>AC 13 (armor scraps)</span><span>HP 13</span><span>Speed 30 ft</span></div>

<div class="attack-box">
  <div class="label">Shortsword</div>
  [h: atk_sword = 1d20]
  <div class="roll">Attack: [r: atk_sword + 4] <span style="font-size:14px;color:#aaa;">(1d20+4)</span></div>
  <div class="detail">
    [h: dmg_sword = 1d6]
    Damage: <b>[r: dmg_sword + 2] piercing</b> (1d6+2)
  </div>
</div>

<div class="attack-box">
  <div class="label">Shortbow (ranged)</div>
  [h: atk_bow = 1d20]
  <div class="roll">Attack: [r: atk_bow + 4] <span style="font-size:14px;color:#aaa;">(1d20+4)</span></div>
  <div class="detail">
    [h: dmg_bow = 1d6]
    Damage: <b>[r: dmg_bow + 2] piercing</b> (1d6+2) — Range 80/320 ft
  </div>
</div>

<div class="resist">
  <b>Vulnerabilities:</b> bludgeoning damage.
  <b>Immunities:</b> poison, exhaustion, Frightened, Poisoned, Exhaustion.
  Skeletons obey the last creature to animate or command them; mindless otherwise.
</div>
</body>
</html>
[/dialog]
