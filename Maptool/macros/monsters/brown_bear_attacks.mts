<!-- Brown Bear (CR 1) — S3 Germanic forest
     AC 11, HP 34 (4d10+12), Speed 40 ft / climb 30 ft
     Multiattack: Claws + Bite
-->
[h: tokenName = getName()]
[dialog("Brown Bear Attacks", "width=380; height=320; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#1a0d00;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#c0854a;margin:0 0 6px 0;font-size:15px;border-bottom:1px solid #c0854a;padding-bottom:4px}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#2a1500;border:1px solid #c0854a;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#c0854a;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
</style></head><body>
<h2>&#9876; BROWN BEAR — [r: tokenName]</h2>
<div class="sr"><span>AC 11</span><span>HP 34</span><span>Speed 40 ft / Climb 30 ft</span></div>
<div class="ab">
  <div class="lb">Multiattack: Claws + Bite</div>
  [h: a1=1d20][h: a2=1d20]
  <div class="rv">[r: a1+5] / [r: a2+5]</div>
  <div class="dt">
    [h: d1=2d6][h: d2=1d8]
    Claws: <b>[r: d1+4] slashing</b> (2d6+4) | Bite: <b>[r: d2+4] piercing</b> (1d8+4)
  </div>
</div>
<div class="ab" style="border-color:#888">
  <div class="lb" style="color:#888">Keen Smell</div>
  <div class="dt">Advantage on Perception checks that rely on smell. Cannot be surprised by a creature it has smelled. S3 forest: bears will smell the party before they see them — animal handling DC 12 (active) to read its mood before it charges.</div>
</div>
</body></html>
[/dialog]
