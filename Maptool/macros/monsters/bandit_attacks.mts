<!-- Bandit (CR 1/8) — S2 road encounter
     AC 12 (leather), HP 11 (2d8+2), Speed 30 ft
-->
[h: tokenName = getName()]
[dialog("Bandit Attacks", "width=380; height=300; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0d0d1a;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#7f8c8d;margin:0 0 6px 0;font-size:15px;border-bottom:1px solid #7f8c8d;padding-bottom:4px}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#1a1a2a;border:1px solid #7f8c8d;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#95a5a6;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
</style></head><body>
<h2>&#9876; BANDIT — [r: tokenName]</h2>
<div class="sr"><span>AC 12 (leather)</span><span>HP 11</span><span>Speed 30 ft</span></div>
<div class="ab">
  <div class="lb">Scimitar (melee)</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+3] <span style="font-size:14px;color:#aaa">(1d20+3)</span></div>
  <div class="dt">[h: dmg=1d6] Damage: <b>[r: dmg+1] slashing</b> (1d6+1)</div>
</div>
<div class="ab">
  <div class="lb">Light Crossbow (ranged — 80/320 ft)</div>
  [h: atk2=1d20] <div class="rv">Attack: [r: atk2+3] <span style="font-size:14px;color:#aaa">(1d20+3)</span></div>
  <div class="dt">[h: dmg2=1d8] Damage: <b>[r: dmg2+1] piercing</b> (1d8+1)</div>
</div>
</body></html>
[/dialog]
