<!-- Orc Raider (CR 1/2) — S3 optional
     AC 13 (hide armor), HP 15 (2d8+6), Speed 30 ft -->
[h: tokenName = getName()]
[dialog("Orc Raider Attacks", "width=380; height=280; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0a0a1a;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#4a1a00;margin:0 0 6px 0;font-size:15px;border-bottom:1px solid #8B4500;padding-bottom:4px}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#1a0800;border:1px solid #8B4500;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#8B4500;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
</style></head><body>
<h2>&#9876; ORC RAIDER — [r: tokenName]</h2>
<div class="sr"><span>AC 13 (hide)</span><span>HP 15</span><span>Speed 30 ft</span></div>
<div class="ab">
  <div class="lb">Greataxe</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+5] <span style="font-size:14px;color:#aaa">(1d20+5)</span></div>
  <div class="dt">[h: dmg=1d12] Damage: <b>[r: dmg+3] slashing</b> (1d12+3)</div>
</div>
<div class="ab">
  <div class="lb">Javelin (30/120 ft)</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+5] <span style="font-size:14px;color:#aaa">(1d20+5)</span></div>
  <div class="dt">[h: dmg=1d6] Damage: <b>[r: dmg+3] piercing</b> (1d6+3)</div>
</div>
<div class="ab" style="border-color:#555">
  <div class="lb" style="color:#555">Aggressive</div>
  <div class="dt">Bonus action: move up to speed toward a hostile. Always charges. Orcs die angry.</div>
</div>
</body></html>
[/dialog]
