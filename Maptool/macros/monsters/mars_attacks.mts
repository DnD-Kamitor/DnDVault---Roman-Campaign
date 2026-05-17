<!-- Mars — S5 Option B: Trial of Blades (Full Party vs. the God)
     Custom stat block. HP 300, AC 20.
     Victory at 150 HP or demonstrating a tactic that forces concession.
     4 attacks per round + Legendary Actions.
     Environmental effect: buildings phase in as terrain each round.
     CAMPAIGN NOTE: Mars says "Enough" when satisfied. This is not a kill fight.
-->
[h: tokenName = getName()]
[dialog("MARS — God of War (Option B Trial)", "width=460; height=560; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#1a0000;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#e74c3c;margin:0 0 4px 0;font-size:16px;border-bottom:2px solid #e74c3c;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#2a0000;border:1px solid #e74c3c;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#e74c3c;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:28px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#e8c547;background:#1a1a00;border:1px solid #e8c547;border-radius:3px;padding:8px;margin-bottom:8px}
  .la{font-size:11px;color:#3498db;background:#001a2c;border:1px solid #3498db;border-radius:3px;padding:6px;margin-top:6px}
</style></head><body>
<h2>&#9876; MARS — Trial of Blades</h2>
<div class="sub">Victory at 150 HP or by forcing a concession. He says "Enough." This is not a death fight.</div>
<div class="sr"><span>AC 20</span><span>HP 300 (victory at 150)</span><span>Speed 60 ft</span></div>
<div class="nt">
  <b>Each round:</b> A random barracks building phases into the arena. Clever use grants advantage for one round. Mars notices the tactic and approves. A god is hard to hide from — but harder is not impossible (Stealth DC 15).<br>
  <b>Victory condition:</b> Reduce to 150 HP OR pin his weapon, blind him with furnace ash, or demonstrate a tactic that forces him to pause. He stops, looks at his weapon, and says "Enough."
</div>
<div class="ab">
  <div class="lb">Multiattack: 4× Divine Pilum</div>
  [h: a1=1d20][h: a2=1d20][h: a3=1d20][h: a4=1d20]
  <div class="rv">[r: a1+12] / [r: a2+12] / [r: a3+12] / [r: a4+12]</div>
  <div class="dt">
    [h: d1=2d8][h: d2=2d8][h: d3=2d8][h: d4=2d8]
    Hits: <b>[r: d1+7]</b> / <b>[r: d2+7]</b> / <b>[r: d3+7]</b> / <b>[r: d4+7]</b> (piercing + divine)
  </div>
</div>
<div class="ab">
  <div class="lb">War Cry (recharge 5-6, 30 ft)</div>
  <div class="dt">All creatures in 30 ft: DC 18 Wisdom save or Frightened for 1 minute. Repeat save at end of each turn.</div>
</div>
<div class="ab">
  <div class="lb">Divine Smite (bonus damage on hit, 1/round)</div>
  <div class="dt">[h: sm=4d8] One hit per round deals an extra <b>[r: sm] radiant</b> damage (4d8). Choose which attack this applies to after seeing if it hits.</div>
</div>
<div class="la">
  <b>Legendary Actions (3/round, at end of another creature's turn):</b><br>
  1. <b>Strike:</b> One Divine Pilum attack [h: la1=1d20][h: lad=2d8] → [r: la1+12] to hit, [r: lad+7] damage<br>
  2. <b>God's Eye (2 actions):</b> Mars marks one creature — until end of its next turn, all attacks against that creature have advantage.<br>
  3. <b>Summon Fallen (3 actions):</b> A spectral legionary appears in an unoccupied space. Use Skeleton stat block. It acts on Mars' initiative.
</div>
</body></html>
[/dialog]
