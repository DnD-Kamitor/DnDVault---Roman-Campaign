<!-- Genius Loci (CR 4) — S3 sacred grove spirit
     Bestiary stat block (custom). AC 16, HP 104 (16d8+32), fly 30 ft
     CANNOT initiate combat. First action is always Compel Respect. Desecration triggers it.
     From: Shadow of Mars bestiary.qmd
-->
[h: tokenName = getName()]
[dialog("Genius Loci: Grove Spirit", "width=440; height=480; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#001a0d;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#27ae60;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #27ae60;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#001a0d;border:1px solid #27ae60;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#27ae60;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#e67e22;background:#2c1500;border:1px solid #e67e22;border-radius:3px;padding:6px;margin-bottom:8px}
  .cd{font-size:11px;color:#9b59b6;background:#1a0020;border:1px solid #9b59b6;border-radius:3px;padding:6px;margin-top:6px}
</style></head><body>
<h2>&#9880; GENIUS LOCI — [r: tokenName]</h2>
<div class="sub">Spirit of the sacred grove. Cannot initiate combat. First action is always Compel Respect.</div>
<div class="sr"><span>AC 16</span><span>HP 104</span><span>Fly 30 ft (Home Ground advantage)</span></div>
<div class="nt">
  <b>If combat starts, you made a mistake.</b> Go back: replay the environmental warnings (temperature dropped, birds went silent, water reversed). Ask the party what they do now. The grove spirit wants help, not a fight. It became hostile because someone cut a marked tree, fouled the spring, or broke a ritual object.
</div>
<div class="ab">
  <div class="lb">Compel Respect (FIRST action only, cannot waive)</div>
  <div class="dt">Each creature within 30 ft that has taken a hostile action here: DC 14 Wisdom save or must make a small genuine offering (drop a weapon, pour water, speak a name of the dead) before taking any hostile action against the spirit. The creature can refuse — but refusing marks it as a desecrator.</div>
</div>
<div class="ab">
  <div class="lb">Multiattack: 2× Slam (only after Compel Respect has been used)</div>
  [h: a1=1d20][h: a2=1d20]
  <div class="rv">[r: a1+7] / [r: a2+7]</div>
  <div class="dt">
    [h: d1=2d8][h: d2=2d8]
    Slam 1: <b>[r: d1+5] bludgeoning</b> | Slam 2: <b>[r: d2+5]</b>
  </div>
</div>
<div class="ab">
  <div class="lb">Guardian's Shield (reaction)</div>
  <div class="dt">When a creature the genius loci has blessed would take damage, reduce that damage by 2d8 ([h: gs=2d8]this roll: <b>[r: gs]</b>).</div>
</div>
<div class="cd">
  <b>Propitiation (action, no roll):</b> A creature that presents a 10 gp+ offering and succeeds DC 12 Religion earns the genius loci's blessing: advantage on all checks and saves within the territory for 24 hours. The Grove's spirit is weakened by the corrupted spear — it WANTS the party to succeed.
</div>
</body></html>
[/dialog]
