<!-- Germanic Druid / Seiðr-Völva (CR 2) — S2 wall assault, Phases 1-2
     AC 11 (16 with Barkskin), HP 27. WIS DC 12, atk +4.
     TWO druids: one Fog Cloud, one Entangle. Staggered concentration.
     Kill priority: silencing either druid ends its spell AND the chanting buff.
-->
[h: tokenName = getName()]
[dialog("Germanic Druid — Seiðr Chant", "width=460; height=580; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0a1200;color:#e0e0d0;padding:12px;margin:0}
  h2{color:#60aa40;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #60aa40;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ch{font-size:11px;color:#f39c12;background:#1a1400;border:1px solid #f39c12;border-radius:3px;padding:8px;margin-bottom:8px}
  .ab{background:#0e1e0e;border:1px solid #60aa40;border-radius:4px;padding:10px;margin-bottom:8px}
  .ab2{background:#0e1e0e;border:1px solid #c04040;border-radius:4px;padding:10px;margin-bottom:8px}
  .ab3{background:#0e1e0e;border:1px solid #8a6030;border-radius:4px;padding:10px;margin-bottom:8px}
  .ab4{background:#0e1e0e;border:1px solid #6060c0;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#60aa40;text-transform:uppercase;letter-spacing:1px}
  .lb2{font-size:11px;color:#c04040;text-transform:uppercase;letter-spacing:1px}
  .lb3{font-size:11px;color:#8a6030;text-transform:uppercase;letter-spacing:1px}
  .lb4{font-size:11px;color:#6060c0;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .dc{font-size:13px;font-weight:bold;color:#f39c12}
  .nt{font-size:11px;color:#9b59b6;background:#1a001a;border:1px solid #9b59b6;border-radius:3px;padding:6px;margin-top:8px}
</style></head><body>
<h2>&#9762; GERMANIC DRUID — [r: tokenName]</h2>
<div class="sub">Seiðr völva — chanting from zone 9, directing the assault through the Old Way</div>
<div class="sr"><span>AC 11 (16 w/ Barkskin)</span><span>HP 27 (5d8+5)</span><span>WIS DC 12 · Atk +4</span></div>
<div class="ch">
  <b>CHANTING BUFF (while alive and conscious):</b> All Germanic fighters in the assault gain +1 to attack rolls and advantage on saves vs. fear effects. Audible from the wall (Perception DC 14). Identifying as magical buff: Arcana DC 13.<br>
  <b>Kill either druid = end their spell concentration AND end the chanting buff.</b>
</div>
<div class="ab2">
  <div class="lb2">Fog Cloud — 1st level · Druid A · Round 1 (Concentration)</div>
  <div class="dc">No save. 20-ft radius sphere, range 120 ft. Heavily obscured = BLIND.</div>
  <div class="dt">All inside: attacks have disadvantage, attackers have advantage vs. them. Cast on wall-top or ladder approach — wall defenders cannot aim ranged weapons down into fog. Concentration: CON save DC 10+ damage taken to maintain.</div>
</div>
<div class="ab2">
  <div class="lb2">Entangle — 1st level · Druid B · Round 1 (Concentration)</div>
  <div class="dc">STR save DC 12 or RESTRAINED (speed 0). On each turn in area: repeat save.</div>
  <div class="dt">20-ft square, range 90 ft. Difficult terrain even on save. Cast on courtyard or at ladder base — a restrained soldier on a ladder falls: 1d6 per 10 ft. Devastating on bunched wall defenders.</div>
</div>
<div class="ab3">
  <div class="lb3">Produce Flame — Cantrip · Ranged 30 ft</div>
  [h: atk=1d20]
  <div class="rv">Attack: [r: atk+4] <span style="font-size:14px;color:#aaa">(1d20+4)</span></div>
  <div class="dt">[h: dmg=1d8] Damage: <b>[r: dmg+4] fire</b> (1d8+4)<br>
  A floating flame visible from the wall — unmistakable aiming marker for party countermeasures.</div>
</div>
<div class="ab4">
  <div class="lb4">Spike Growth — 2nd level · Phase 2 (Concentration · Once)</div>
  <div class="dc">No save to enter. 2d4 piercing per 5 ft moved through. Looks like natural terrain (Perception DC 15 to spot).</div>
  [h: sg1=1d4][h: sg2=1d4]
  <div class="rv">Per 5 ft: [r: sg1+sg2] <span style="font-size:14px;color:#aaa">piercing (2d4)</span></div>
  <div class="dt">20-ft radius, range 150 ft. Cast on the courtyard or gate approach. A soldier sprinting 30 ft through it: takes 6× 2d4 damage. Brutal on defenders forced to run to a breach.</div>
</div>
<div class="ab4">
  <div class="lb4">Hold Person — 2nd level (Concentration · Once)</div>
  <div class="dc">WIS save DC 12 or PARALYZED. Repeat save each turn. All attacks vs. paralyzed: auto-crit.</div>
  <div class="dt">Range 60 ft. Best used on the party's most dangerous melee fighter. While paralyzed: berserkers can walk up and auto-crit with greataxes. Concentration — killing the druid ends it immediately.</div>
</div>
<div class="ab">
  <div class="lb">Thunderwave — 1st level · If melee closes</div>
  <div class="dc">CON save DC 12 or 2d8 thunder + pushed 10 ft. Half on save.</div>
  [h: tw1=1d8][h: tw2=1d8]
  <div class="rv">Damage: [r: tw1+tw2] <span style="font-size:14px;color:#aaa">thunder (2d8)</span></div>
  <div class="dt">15-ft cube from self. Audible 300 ft away. Used only as last resort when melee closes on the druid — then immediately flees into treeline.</div>
</div>
<div class="ab">
  <div class="lb">Shillelagh — Cantrip melee (emergency only)</div>
  [h: atk2=1d20]
  <div class="rv">Attack: [r: atk2+4] <span style="font-size:14px;color:#aaa">(1d20+4)</span></div>
  <div class="dt">[h: dmg2=1d8] Damage: <b>[r: dmg2+2] bludgeoning</b> (1d8+2, WIS-based)<br>
  Does not stand in melee. Flee threshold: below 10 HP or melee contact.</div>
</div>
<div class="nt">
  <b>Slots:</b> 4× 1st (Fog Cloud, Entangle ×2, Thunderwave) · 2× 2nd (Spike Growth, Hold Person)<br>
  <b>Slot order priority:</b> Fog Cloud (Druid A R1) → Entangle (Druid B R1) → Hold Person (R2-3 on key fighter) → Spike Growth (gate breach) → Thunderwave (melee emergency)<br>
  <b>AI:</b> Never advance past boulders. Zone 9 only. Lose concentration → immediately recast Entangle. Below 10 HP → flee treeline (unit morale visibly drops when the chanting stops).
</div>
</body></html>
[/dialog]
