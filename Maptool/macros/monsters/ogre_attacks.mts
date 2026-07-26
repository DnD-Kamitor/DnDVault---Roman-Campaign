<!-- Ogre (CR 2) — S2 wall assault, Phase 2
     AC 11 (hide armor), HP 59 (7d10+21), Speed 40 ft. Large creature.
     Living battering ram vs. west gate. Greatclub + Javelin.
     Gate HP 60 — breaches in ~3 rounds if not stopped.
-->
[h: tokenName = getName()]
[dialog("Ogre Attacks", "width=430; height=460; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0a0a00;color:#e0e0d0;padding:12px;margin:0}
  h2{color:#a08030;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #a08030;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#1a1400;border:1px solid #a08030;border-radius:4px;padding:10px;margin-bottom:8px}
  .ab2{background:#1a1400;border:1px solid #607050;border-radius:4px;padding:10px;margin-bottom:8px}
  .ab3{background:#200a0a;border:1px solid #c04040;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#a08030;text-transform:uppercase;letter-spacing:1px}
  .lb2{font-size:11px;color:#607050;text-transform:uppercase;letter-spacing:1px}
  .lb3{font-size:11px;color:#c04040;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#f39c12;background:#2c1a00;border:1px solid #f39c12;border-radius:3px;padding:6px;margin-top:8px}
</style></head><body>
<h2>&#128296; OGRE — [r: tokenName]</h2>
<div class="sub">Living battering ram — pointed at the west gate, that is his entire mission</div>
<div class="sr"><span>AC 11 (hide)</span><span>HP 59 (7d10+21)</span><span>Speed 40 ft · Large</span></div>
<div class="ab3">
  <div class="lb3">Battering Ram — vs. Gate (each round, automatic action)</div>
  [h: rd1=1d6][h: rd2=1d6][h: rd3=1d6]
  <div class="rv">Gate damage: [r: rd1+rd2+rd3+4] <span style="font-size:14px;color:#aaa">(3d6+4 bludgeoning)</span></div>
  <div class="dt">Gate HP: 60. Portcullis HP: 60 (AC 20). Bars: AC 20, HP 60.<br>
  At this rate gate falls in ~3 rounds if no one stops him.<br>
  He can be targeted through arrow slits: 3/4 cover (AC 15, +5 Dex saves).</div>
</div>
<div class="ab">
  <div class="lb">Greatclub — Melee (if party engages him)</div>
  [h: atk=1d20]
  <div class="rv">Attack: [r: atk+6] <span style="font-size:14px;color:#aaa">(1d20+6)</span></div>
  <div class="dt">[h: d1=1d8][h: d2=1d8] Damage: <b>[r: d1+d2+4] bludgeoning</b> (2d8+4)</div>
</div>
<div class="ab2">
  <div class="lb2">Javelin — Ranged (30/120 ft) · If someone blocks his path</div>
  [h: atk2=1d20]
  <div class="rv">Attack: [r: atk2+6] <span style="font-size:14px;color:#aaa">(1d20+6)</span></div>
  <div class="dt">[h: jd1=1d6][h: jd2=1d6] Damage: <b>[r: jd1+jd2+4] piercing</b> (2d6+4)<br>
  Carries 3 javelins. Throws if he cannot reach the gate.</div>
</div>
<div class="nt">
  <b>Large creature:</b> Occupies 2×2 squares. Threatens adjacent squares with reach 5 ft. Can shove as bonus action vs. Medium creatures (STR contest, ogre +4).<br>
  <b>Flanking (east postern):</b> Smart play is to lure him away from the gate with ranged fire, then use the postern to slip behind him. Atk from two sides = disadvantage on his attacks this round.<br>
  <b>INT 5:</b> Cannot be tricked or deceived. Does not pursue fleeing enemies. Gate. Gate. Gate.
</div>
</body></html>
[/dialog]
