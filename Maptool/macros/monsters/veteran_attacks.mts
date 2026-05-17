<!-- Veteran (CR 3) — Centurion Varro (ally), enemy NCOs, S2-4
     AC 17 (splint), HP 58 (9d8+18), Speed 30 ft
     Multiattack: 2× longsword + 1× shortsword
-->
[h: tokenName = getName()]
[dialog("Veteran Attacks", "width=420; height=400; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0a1a0a;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#27ae60;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #27ae60;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#0a1f0a;border:1px solid #27ae60;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#27ae60;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#3498db;background:#001a2c;border:1px solid #3498db;border-radius:3px;padding:6px;margin-bottom:8px}
</style></head><body>
<h2>&#9876; VETERAN — [r: tokenName]</h2>
<div class="sub">Centurion Varro (ally) or enemy Roman NCO. Worth three normal soldiers.</div>
<div class="sr"><span>AC 17 (splint)</span><span>HP 58</span><span>Speed 30 ft</span></div>
<div class="nt">
  <b>Varro as ally:</b> He fights alongside the party. Use this macro when running his attacks to keep combat moving. He targets the highest-threat enemy and protects downed allies.
</div>
<div class="ab">
  <div class="lb">Multiattack: 2× Longsword + 1× Shortsword</div>
  [h: a1=1d20][h: a2=1d20][h: a3=1d20]
  <div class="rv">[r: a1+5] / [r: a2+5] / [r: a3+5]</div>
  <div class="dt">
    [h: d1=1d8][h: d2=1d8][h: d3=1d6]
    Longsword 1: <b>[r: d1+3] slashing</b> | Longsword 2: <b>[r: d2+3]</b> | Shortsword: <b>[r: d3+3] piercing</b>
  </div>
</div>
<div class="ab">
  <div class="lb">Heavy Crossbow (ranged — 100/400 ft)</div>
  [h: ra=1d20] <div class="rv">Attack: [r: ra+3]</div>
  <div class="dt">[h: rd=1d10] Damage: <b>[r: rd+1] piercing</b> (1d10+1)</div>
</div>
</body></html>
[/dialog]
