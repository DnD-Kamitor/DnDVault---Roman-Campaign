<!-- Dire Wolf (CR 1) — S3 Germanic forest
     AC 14 (natural armor), HP 37 (5d10+10), Speed 50 ft
-->
[h: tokenName = getName()]
[dialog("Dire Wolf Attacks", "width=380; height=320; temporary=true;")]
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
<h2>&#128058; DIRE WOLF — [r: tokenName]</h2>
<div class="sr"><span>AC 14</span><span>HP 37</span><span>Speed 50 ft</span></div>
<div class="ab">
  <div class="lb">Bite</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+5] <span style="font-size:14px;color:#aaa">(1d20+5)</span></div>
  <div class="dt">[h: dmg=2d6] Damage: <b>[r: dmg+3] piercing</b> (2d6+3)</div>
  <div class="nt">
    <b>Knockdown:</b> DC 13 Strength save or target is knocked Prone.<br>
    <b>Pack Tactics:</b> Advantage if an ally is within 5 ft of target and not incapacitated.
  </div>
</div>
</body></html>
[/dialog]
