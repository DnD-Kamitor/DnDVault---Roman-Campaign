<!-- Boar (CR 1/4) — S2 road encounter
     AC 11, HP 11 (2d8+2), Speed 40 ft
-->
[h: tokenName = getName()]
[dialog("Boar Attacks", "width=380; height=320; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#1a0d00;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#c0854a;margin:0 0 6px 0;font-size:15px;border-bottom:1px solid #c0854a;padding-bottom:4px}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#2a1500;border:1px solid #c0854a;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#c0854a;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#e67e22;background:#2c1500;border:1px solid #e67e22;border-radius:3px;padding:6px;margin-top:8px}
</style></head><body>
<h2>&#9876; BOAR — [r: tokenName]</h2>
<div class="sr"><span>AC 11</span><span>HP 11</span><span>Speed 40 ft</span></div>
<div class="ab">
  <div class="lb">Tusk</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+3] <span style="font-size:14px;color:#aaa">(1d20+3)</span></div>
  <div class="dt">[h: dmg=1d6] Damage: <b>[r: dmg+1] slashing</b> (1d6+1)</div>
</div>
<div class="nt">
  <b>Charge:</b> If the boar moves 20+ ft straight and hits with tusk, target takes extra 3 (1d6) slashing damage and must succeed on DC 11 Strength save or be knocked Prone.<br><br>
  <b>Relentless (1/day):</b> If the boar takes 7+ damage in one hit and would fail a save, it can succeed instead. Once per short or long rest.
</div>
</body></html>
[/dialog]
