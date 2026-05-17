<!-- Scout (CR 1/2) — S3 Germanic scouts (×2 with ambush)
     AC 13 (leather), HP 16 (3d8+3), Speed 30 ft
     Multiattack: 2 attacks
-->
[h: tokenName = getName()]
[dialog("Scout Attacks", "width=380; height=320; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0d1a0d;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#2ecc71;margin:0 0 6px 0;font-size:15px;border-bottom:1px solid #2ecc71;padding-bottom:4px}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#0a1f0a;border:1px solid #2ecc71;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#2ecc71;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
</style></head><body>
<h2>&#9876; SCOUT — [r: tokenName]</h2>
<div class="sr"><span>AC 13 (leather)</span><span>HP 16</span><span>Speed 30 ft</span></div>
<div class="ab">
  <div class="lb">Multiattack: 2 attacks (any combo)</div>
  [h: a1=1d20][h: a2=1d20]
  <div class="rv">[r: a1+4] / [r: a2+4]</div>
  <div class="dt">
    [h: d1=1d6][h: d2=1d8]
    Shortsword: <b>[r: d1+2] piercing</b> | Longbow (150/600 ft): <b>[r: d2+2] piercing</b>
  </div>
</div>
<div class="ab" style="border-color:#888">
  <div class="lb" style="color:#888">Keen Hearing and Sight</div>
  <div class="dt">Advantage on Perception checks. Scouts act as early warning for ambush — if Scouts are present, the warriors get a surprise round unless the party makes a group Stealth check against DC 15 before entering the area.</div>
</div>
</body></html>
[/dialog]
