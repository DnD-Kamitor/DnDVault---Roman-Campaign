<!-- Wolf (CR 1/2) — S2 road, S3 forest
     AC 13, HP 11 (2d8+2), Speed 40 ft
-->
[h: tokenName = getName()]
[dialog("Wolf Attacks", "width=380; height=320; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#1a1200;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#d4a017;margin:0 0 6px 0;font-size:15px;border-bottom:1px solid #d4a017;padding-bottom:4px}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#2a1f00;border:1px solid #d4a017;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#d4a017;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#e67e22;background:#2c1500;border:1px solid #e67e22;border-radius:3px;padding:6px;margin-top:8px}
</style></head><body>
<h2>&#128058; WOLF — [r: tokenName]</h2>
<div class="sr"><span>AC 13</span><span>HP 11</span><span>Speed 40 ft</span></div>
<div class="ab">
  <div class="lb">Bite</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+4] <span style="font-size:14px;color:#aaa">(1d20+4)</span></div>
  <div class="dt">[h: dmg=2d4] Damage: <b>[r: dmg+2] piercing</b> (2d4+2)</div>
  <div class="nt"><b>Knockdown:</b> DC 11 Strength save or target is knocked Prone.</div>
</div>
<div class="ab" style="border-color:#888">
  <div class="lb" style="color:#888">Pack Tactics</div>
  <div class="dt">Wolf has <b>advantage</b> on attack rolls against a creature if at least one of the wolf's allies is within 5 ft of the target and the ally isn't incapacitated. Roll twice above and take the higher result.</div>
</div>
</body></html>
[/dialog]
