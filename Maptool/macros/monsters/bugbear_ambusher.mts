<!-- Bugbear Ambusher (CR 1) — S3 optional encounter
     AC 16 (hide armor + shield), HP 27 (5d8+5), Speed 30 ft -->
[h: tokenName = getName()]
[dialog("Bugbear Ambusher Attacks", "width=380; height=300; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0a0a1a;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#8B4513;margin:0 0 6px 0;font-size:15px;border-bottom:1px solid #8B4513;padding-bottom:4px}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#1a0a0a;border:1px solid #8B4513;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#8B4513;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
</style></head><body>
<h2>&#128122; BUGBEAR AMBUSHER — [r: tokenName]</h2>
<div class="sr"><span>AC 16 (hide+shield)</span><span>HP 27</span><span>Speed 30 ft</span></div>
<div class="ab">
  <div class="lb">Morningstar</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+4] <span style="font-size:14px;color:#aaa">(1d20+4)</span></div>
  <div class="dt">[h: dmg=2d8] Damage: <b>[r: dmg+2] piercing</b> (2d8+2)</div>
</div>
<div class="ab">
  <div class="lb">Javelin (thrown 30/120 ft)</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+4] <span style="font-size:14px;color:#aaa">(1d20+4)</span></div>
  <div class="dt">[h: dmg=1d6] Damage: <b>[r: dmg+2] piercing</b> (1d6+2)</div>
</div>
<div class="ab" style="border-color:#555">
  <div class="lb" style="color:#555">Surprise Attack</div>
  <div class="dt">If hits a surprised creature, add 2d6 extra damage. Brute: two-handed weapons deal +1 die (already included in morningstar).</div>
</div>
</body></html>
[/dialog]
