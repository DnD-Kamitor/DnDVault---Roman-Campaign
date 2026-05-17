<!-- Draugar (CR 6) — S3 burial mound boss encounter
     Bestiary stat block (custom). AC 15 (chain shirt), HP 136 (16d8+64), Speed 30 ft
     Undead Fortitude, Swelling Rage at 60 HP (grows to Large), Grave Goods Throw
     From: Shadow of Mars bestiary.qmd
-->
[h: tokenName = getName()]
[dialog("Draugar: Burial Mound Terror", "width=440; height=500; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#1a0000;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#e74c3c;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #e74c3c;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#2a0000;border:1px solid #e74c3c;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#e74c3c;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#f39c12;background:#2c1500;border:1px solid #f39c12;border-radius:3px;padding:6px;margin-bottom:8px}
  .cd{font-size:11px;color:#e74c3c;background:#2c0000;border:1px solid #e74c3c;border-radius:3px;padding:6px;margin-top:6px}
</style></head><body>
<h2>&#9760; DRAUGAR — [r: tokenName]</h2>
<div class="sub">Barrow lord — fights at its mound boundary. Growing rage, not retreating.</div>
<div class="sr"><span>AC 15 (chain shirt)</span><span>HP 136</span><span>Speed 30 ft</span></div>
<div class="nt">
  <b>Tactics:</b> Grave Goods Throw on round 1 (ranged), then closes for Greatclub. At 60 HP it swells Large — gets bonus slam. Lure it to the 100 ft boundary; fight on open ground. Return its grave goods + decapitation rite (DC 14 Religion) to prevent reformation.
</div>
<div class="ab">
  <div class="lb">Grave Goods Throw (ranged, 30 ft — round 1 preferred)</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+8]</div>
  <div class="dt">[h: dmg=2d8] Damage: <b>[r: dmg+5] bludgeoning</b> (2d8+5)</div>
</div>
<div class="ab">
  <div class="lb">Multiattack: 2× Greatclub (3× when Large after Swelling Rage)</div>
  [h: a1=1d20][h: a2=1d20]
  <div class="rv">[r: a1+8] / [r: a2+8]</div>
  <div class="dt">
    [h: d1=3d8][h: d2=3d8]
    Greatclub 1: <b>[r: d1+5] bludgeoning</b> | Greatclub 2: <b>[r: d2+5]</b>
    [h: d3=3d8]
    (If Large/Swelling Rage): Bonus Slam: <b>[r: d3+5]</b>
  </div>
</div>
<div class="cd">
  <b>Undead Fortitude:</b> If damage reduces to 0 HP, DC (5 + damage taken) Constitution save. On success: drops to 1 HP instead. Fails against radiant damage or critical hits.<br><br>
  <b>Swelling Rage (at 60 HP):</b> Immediately grows Large. Extra slam attack added to Multiattack. Triggers earlier than expected — plan for it.
</div>
</body></html>
[/dialog]
