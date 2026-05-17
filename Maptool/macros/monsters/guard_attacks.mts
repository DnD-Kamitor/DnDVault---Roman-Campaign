<!-- Guard (CR 1/8) — Praetorians, Roman Legionaries (S2-4)
     AC 16 (chain shirt + shield), HP 11 (2d8+2), Speed 30 ft
-->
[h: tokenName = getName()]
[dialog("Guard / Praetorian Attacks", "width=380; height=280; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0a0a1a;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#c0392b;margin:0 0 6px 0;font-size:15px;border-bottom:1px solid #c0392b;padding-bottom:4px}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#1a0a0a;border:1px solid #c0392b;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#c0392b;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
</style></head><body>
<h2>&#9876; GUARD / PRAETORIAN — [r: tokenName]</h2>
<div class="sr"><span>AC 16 (chain+shield)</span><span>HP 11</span><span>Speed 30 ft</span></div>
<div class="ab">
  <div class="lb">Spear (melee or thrown — 20/60 ft)</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+3] <span style="font-size:14px;color:#aaa">(1d20+3)</span></div>
  <div class="dt">[h: dmg=1d6] One-hand: <b>[r: dmg+1] piercing</b> (1d6+1) | Two-hand: [h: dmg2=1d8]<b>[r: dmg2+1]</b> (1d8+1)</div>
</div>
<div class="ab" style="border-color:#888">
  <div class="lb" style="color:#888">Formation note</div>
  <div class="dt">S2: Tribune + 6 Praetorians. All 6 acting as a unit is an Extremely Dangerous encounter. Varro can delay them (S2 chapter notes). Fighting 6 Guards at once = near-Deadly for 5 Level 4 characters.</div>
</div>
</body></html>
[/dialog]
