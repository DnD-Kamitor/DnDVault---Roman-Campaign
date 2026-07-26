<!-- Germanic Archer (CR 1/4) — S2 wall assault, Phases 1-2
     AC 13 effective (AC 11 hide + half cover from boulders), HP 11
     Four archers in zone 9 behind boulders. Suppression fire.
     They do NOT advance. Retreat if engaged in melee.
-->
[h: tokenName = getName()]
[dialog("Germanic Archer Attacks", "width=400; height=360; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0a100a;color:#e0e0d0;padding:12px;margin:0}
  h2{color:#6aaa50;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #6aaa50;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#0a1a0a;border:1px solid #6aaa50;border-radius:4px;padding:10px;margin-bottom:8px}
  .ab2{background:#0a1a0a;border:1px solid #8a7040;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#6aaa50;text-transform:uppercase;letter-spacing:1px}
  .lb2{font-size:11px;color:#8a7040;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#f39c12;background:#2c1a00;border:1px solid #f39c12;border-radius:3px;padding:6px;margin-top:8px}
</style></head><body>
<h2>&#9016; GERMANIC ARCHER — [r: tokenName]</h2>
<div class="sub">Zone 9, behind boulders — half cover active</div>
<div class="sr"><span>AC 11 (13 w/ cover)</span><span>HP 11</span><span>Range 80/320 ft</span></div>
<div class="ab">
  <div class="lb">Shortbow (80/320 ft)</div>
  [h: atk=1d20]
  <div class="rv">Attack: [r: atk+4] <span style="font-size:14px;color:#aaa">(1d20+4)</span></div>
  <div class="dt">[h: dmg=1d6] Damage: <b>[r: dmg+2] piercing</b> (1d6+2)<br>
  Half cover: attacker needs to overcome AC 13 (not 11).</div>
</div>
<div class="ab2">
  <div class="lb2">Seax — melee (emergency only)</div>
  [h: atk2=1d20]
  <div class="rv">Attack: [r: atk2+2] <span style="font-size:14px;color:#aaa">(1d20+2)</span></div>
  <div class="dt">[h: dmg2=1d4] Damage: <b>[r: dmg2+1] piercing</b> (1d4+1)<br>
  Archer retreats if engaged — he is a harasser, not a fighter.</div>
</div>
<div class="nt">
  <b>Half Cover (boulders):</b> +2 AC, +2 Dex saves while behind boulder.<br>
  <b>Pack Tactics:</b> Advantage if ally within 5 ft of target.<br>
  <b>Suppression role:</b> Forces defenders behind crenellations. If defender takes cover, archer delays ladder climbers reaching clear kills.
</div>
</body></html>
[/dialog]
