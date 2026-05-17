<!-- Stone Golem (CR 10, modified) — S5 Animated Standing Stones
     Standard stat block but HP capped at 120 (avatars of Mars, not full golems).
     AC 17, HP 120, Speed 30 ft. Magic resistance. Immune to most damage types.
     CAMPAIGN NOTE: These are avatars of Mars' anger, not independent creatures.
     Slow ability is the most dangerous: halves speed and restricts bonus actions/reactions.
-->
[h: tokenName = getName()]
[dialog("Stone Golem / Animated Standing Stone", "width=440; height=480; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#1a0a00;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#e8c547;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #e8c547;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#2a1a00;border:1px solid #e8c547;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#e8c547;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#e74c3c;background:#2c0000;border:1px solid #e74c3c;border-radius:3px;padding:6px;margin-bottom:8px}
  .re{font-size:11px;color:#27ae60;background:#001a0d;border:1px solid #27ae60;border-radius:3px;padding:6px;margin-top:6px}
</style></head><body>
<h2>&#9876; ANIMATED STANDING STONE — [r: tokenName]</h2>
<div class="sub">Avatar of Mars' anger. HP capped at 120 (not full Golem). Magic Resistance. ×3 of these.</div>
<div class="sr"><span>AC 17</span><span>HP 120 (modified)</span><span>Speed 30 ft</span></div>
<div class="nt">
  <b>Three at once is Deadly.</b> 3 Stone Golems vs 5 Level 6 characters: ~6,000 adjusted XP. That is well beyond Deadly (2,500). Use Slow early and often. They are meant to be fled or cleverly bypassed if Mars is displeased, not defeated in straight combat.
</div>
<div class="ab">
  <div class="lb">Multiattack: 2× Slam</div>
  [h: a1=1d20][h: a2=1d20]
  <div class="rv">[r: a1+10] / [r: a2+10]</div>
  <div class="dt">
    [h: d1=3d8][h: d2=3d8]
    Slam 1: <b>[r: d1+6] bludgeoning</b> (3d8+6) | Slam 2: <b>[r: d2+6]</b>
  </div>
</div>
<div class="ab">
  <div class="lb">Slow (recharge 5-6, 10 ft radius, DC 17 Con save)</div>
  <div class="dt">All targets in 10 ft radius: DC 17 Constitution save or Slowed for 1 minute. While Slowed: speed halved, -2 to AC and Dex saves, can't use reactions, on its turn can use either an action or a bonus action (not both), can make only one attack regardless of features. Repeat save at end of each turn.</div>
</div>
<div class="re">
  <b>Immunities:</b> poison, psychic. Non-magical, non-adamantine weapons are immune (attacks have no effect). <b>Magic Resistance:</b> advantage on saves vs spells and magical effects.
</div>
</body></html>
[/dialog]
