<!-- Tribal Warrior (CR 1/8) — S3 Germanic ambush (×12) + 2 Scouts
     AC 12 (hide armor), HP 11 (2d8+2), Speed 30 ft
     Pack Tactics — fight in the tree line; difficult terrain negates Roman formation
-->
[h: tokenName = getName()]
[dialog("Tribal Warrior Attacks", "width=380; height=300; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0d1a0d;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#27ae60;margin:0 0 6px 0;font-size:15px;border-bottom:1px solid #27ae60;padding-bottom:4px}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#0a1f0a;border:1px solid #27ae60;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#27ae60;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#f39c12;background:#2c1a00;border:1px solid #f39c12;border-radius:3px;padding:6px;margin-top:8px}
</style></head><body>
<h2>&#9876; TRIBAL WARRIOR — [r: tokenName]</h2>
<div class="sr"><span>AC 12 (hide)</span><span>HP 11</span><span>Speed 30 ft</span></div>
<div class="ab">
  <div class="lb">Spear (melee or thrown — 20/60 ft)</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+4] <span style="font-size:14px;color:#aaa">(1d20+4)</span></div>
  <div class="dt">[h: dmg=1d6] One-hand: <b>[r: dmg+2] piercing</b> (1d6+2) | Two-hand: [h: dmg2=1d8]<b>[r: dmg2+2]</b></div>
</div>
<div class="nt">
  <b>Pack Tactics:</b> Advantage on attacks if an ally is within 5 ft of target.<br>
  <b>Forest ambush (×12+2 Scouts):</b> S3 ambush. Tree line = difficult terrain for Romans. No formations. 12 warriors is Medium-Hard encounter. Thusnelda can halt this with a word if the party hasn't attacked. It's a test, not a fight.
</div>
</body></html>
[/dialog]
