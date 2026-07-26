<!-- Germanic Spearman (CR 1/2) — S2 wall assault, ladder climbers
     AC 13 (hide + wooden shield), HP 16
     Eight spearmen in two groups. Framea throw BEFORE mounting ladder.
     Half speed on ladder, no Dash, no reaction while climbing.
-->
[h: tokenName = getName()]
[dialog("Germanic Spearman Attacks", "width=420; height=400; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#100a00;color:#e0e0d0;padding:12px;margin:0}
  h2{color:#c8a040;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #c8a040;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#1a0e00;border:1px solid #c8a040;border-radius:4px;padding:10px;margin-bottom:8px}
  .ab2{background:#1a0e00;border:1px solid #8a7040;border-radius:4px;padding:10px;margin-bottom:8px}
  .ab3{background:#1a0e00;border:1px solid #607050;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#c8a040;text-transform:uppercase;letter-spacing:1px}
  .lb2{font-size:11px;color:#8a7040;text-transform:uppercase;letter-spacing:1px}
  .lb3{font-size:11px;color:#607050;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#f39c12;background:#2c1a00;border:1px solid #f39c12;border-radius:3px;padding:6px;margin-top:8px}
</style></head><body>
<h2>&#9876; GERMANIC SPEARMAN — [r: tokenName]</h2>
<div class="sub">Ladder climber — framea throw first, then melee at the parapet</div>
<div class="sr"><span>AC 13 (hide + shield)</span><span>HP 16</span><span>Speed 30 ft</span></div>
<div class="ab">
  <div class="lb">Framea — Thrown (30/120 ft) · Before ladder</div>
  [h: atk=1d20]
  <div class="rv">Attack: [r: atk+4] <span style="font-size:14px;color:#aaa">(1d20+4)</span></div>
  <div class="dt">[h: dmg=1d6] Damage: <b>[r: dmg+2] piercing</b> (1d6+2)<br>
  Thrown at wall defenders BEFORE reaching the ladder. Range 30/120.</div>
</div>
<div class="ab2">
  <div class="lb2">Framea — Melee (reach 5 ft, at the parapet)</div>
  [h: atk2=1d20]
  <div class="rv">Attack: [r: atk2+4] <span style="font-size:14px;color:#aaa">(1d20+4)</span></div>
  <div class="dt">[h: dmg2=1d6] Damage: <b>[r: dmg2+2] piercing</b> (1d6+2)<br>
  Once on the wall. Two-hand: [h: dmg3=1d8]<b>[r: dmg3+2]</b> (1d8+2).</div>
</div>
<div class="ab3">
  <div class="lb3">Seax — Backup melee</div>
  [h: atk3=1d20]
  <div class="rv">Attack: [r: atk3+4] <span style="font-size:14px;color:#aaa">(1d20+4)</span></div>
  <div class="dt">[h: dmg4=1d4] Damage: <b>[r: dmg4+2] piercing</b> (1d4+2) · Light weapon.</div>
</div>
<div class="nt">
  <b>Pack Tactics:</b> Advantage on attacks when an ally is within 5 ft of target. Devastating once 2+ reach the parapet.<br>
  <b>Ladder rules:</b> Half speed (15 ft/round), no Dash, no reaction. Berserker leads — first up, takes the initial hits.<br>
  <b>Shield:</b> Slung during climb (GM: -1 AC while on ladder).
</div>
</body></html>
[/dialog]
