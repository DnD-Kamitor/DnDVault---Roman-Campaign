<!-- Lemur (CR 1) — battlefields, unburied dead; S2 aftermath or S4
     Bestiary stat block (custom). AC 12, HP 22 (4d8+4), fly 30 ft (hover)
     Bury the dead to end the encounter. Combat just makes them return tomorrow.
     From: Shadow of Mars bestiary.qmd
-->
[h: tokenName = getName()]
[dialog("Lemur: Roman Restless Dead", "width=420; height=440; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0d0d1a;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#7f8c8d;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #7f8c8d;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#1a1a2a;border:1px solid #7f8c8d;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#95a5a6;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#3498db;background:#001a2c;border:1px solid #3498db;border-radius:3px;padding:6px;margin-bottom:8px}
  .cd{font-size:11px;color:#e74c3c;background:#2c0000;border:1px solid #e74c3c;border-radius:3px;padding:6px;margin-top:6px}
</style></head><body>
<h2>&#9760; LEMUR — [r: tokenName]</h2>
<div class="sub">Restless Roman dead. Combat does not end this. Burial ends this.</div>
<div class="sr"><span>AC 12</span><span>HP 22</span><span>Fly 30 ft (hover)</span></div>
<div class="nt">
  <b>Real solution:</b> Bury the mortal remains with proper funerary rites (10 min ceremony, DC 10 Religion check). <i>Bless</i> cast over remains allows the check automatically. If destroyed without burial, Lemur reforms at death location after 24 hours — twice. Third destruction is permanent only if remains were buried at any point.<br>
  <b>During Lemuria</b> (May 9, 11, 13): Cannot stay more than 30 ft from a living creature.
</div>
<div class="ab">
  <div class="lb">Draining Touch</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+4]</div>
  <div class="dt">[h: dmg=1d6] Damage: <b>[r: dmg+2] psychic</b> (1d6+2)<br>
  DC 12 Constitution save or gain 1 level of exhaustion (max 1 from this ability, recovered on long rest).</div>
</div>
<div class="ab">
  <div class="lb">Scatter (when one Lemur drops to 0 HP)</div>
  <div class="dt">All Lemures within 30 ft: DC 12 Wisdom save or Incapacitated until end of their next turn (hovering, confused). Cluster mechanic — destroying one creates chaos among the rest. This is the combat payoff; the burial is the narrative payoff.</div>
</div>
</body></html>
[/dialog]
