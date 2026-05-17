<!-- Haugbui (CR 3) — S3 Germanic forest, burial mound undead
     Tome of Beasts (Kobold Press). AC 15, HP 82 (11d8+33), fly 40 ft (hover)
     Barrow-guardian that haunts the grave mound. Does not pursue beyond its territory.
-->
[h: tokenName = getName()]
[dialog("Haugbui: Barrow Guardian", "width=420; height=460; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0d0d1a;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#9b59b6;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #9b59b6;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#1a0d1a;border:1px solid #9b59b6;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#9b59b6;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .cd{font-size:11px;color:#e74c3c;background:#2c0000;border:1px solid #e74c3c;border-radius:3px;padding:6px;margin-top:6px}
  .nt{font-size:11px;color:#3498db;background:#001a2c;border:1px solid #3498db;border-radius:3px;padding:6px;margin-bottom:8px}
</style></head><body>
<h2>&#9760; HAUGBUI — [r: tokenName]</h2>
<div class="sub">Barrow guardian — does not pursue beyond its mound. Destroy its grave goods to end it permanently.</div>
<div class="sr"><span>AC 15</span><span>HP 82</span><span>Fly 40 ft (hover)</span></div>
<div class="nt">
  <b>Territory:</b> The Haugbui cannot willingly move more than 100 ft from its mound. Lure it to the boundary to fight on open ground. If its grave goods are returned and the mound purified (DC 14 Religion, 10 min ceremony), it does not reform.
</div>
<div class="ab">
  <div class="lb">Multiattack: 2× Slam</div>
  [h: a1=1d20][h: a2=1d20]
  <div class="rv">[r: a1+6] / [r: a2+6]</div>
  <div class="dt">[h: d1=2d6][h: d2=2d6] Slam 1: <b>[r: d1+4] bludgeoning</b> | Slam 2: <b>[r: d2+4] bludgeoning</b></div>
</div>
<div class="ab">
  <div class="lb">Draining Gaze (60 ft, no attack roll)</div>
  <div class="dt">Target in line of sight must succeed on DC 14 Constitution save.</div>
  <div class="cd"><b>On fail:</b> Target gains 1 level of exhaustion (maximum 1 from this ability, recovered on long rest). Undead and creatures immune to exhaustion are unaffected.</div>
</div>
<div class="ab">
  <div class="lb">Haunt (1/day, 30 ft)</div>
  <div class="dt">Each creature within 30 ft must succeed on DC 14 Wisdom save.</div>
  <div class="cd"><b>On fail:</b> Frightened for 1 minute. Target can repeat the save at the end of each of its turns, ending on a success.</div>
</div>
</body></html>
[/dialog]
