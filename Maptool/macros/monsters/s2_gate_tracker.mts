<!-- S2 Gate Tracker — prop tracking gate status during S2 siege -->
[h: tokenName = getName()]
[dialog("Gate Status Tracker", "width=340; height=240; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0a0a1a;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#c0392b;margin:0 0 6px 0;font-size:15px;border-bottom:1px solid #c0392b;padding-bottom:4px}
  .row{display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #333;font-size:13px}
  .val{color:#fff;font-weight:bold}
</style></head><body>
<h2>&#9974; GATE STATUS — [r: tokenName]</h2>
<div class="row"><span>Gate HP</span><span class="val">AC 17 — HP 54 (Heavy Wood+Iron)</span></div>
<div class="row"><span>Battering Ram</span><span class="val">2d10+4 per 3 attackers, action</span></div>
<div class="row"><span>Breach at 0 HP</span><span class="val">Enemies flood in — Scene 4 triggers</span></div>
<div class="row"><span>Barricade (action)</span><span class="val">+20 HP, costs one PC action per round</span></div>
</body></html>
[/dialog]
