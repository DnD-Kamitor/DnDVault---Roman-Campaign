<!-- Bandit Captain (CR 2) — S2 road encounter leader
     AC 15 (studded leather), HP 65 (10d8+20), Speed 30 ft
     Multiattack: 2 scimitar + 1 dagger (or 2 scimitar in melee)
-->
[h: tokenName = getName()]
[dialog("Bandit Captain Attacks", "width=420; height=400; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0d0d1a;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#e74c3c;margin:0 0 6px 0;font-size:15px;border-bottom:1px solid #e74c3c;padding-bottom:4px}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#1a0a0a;border:1px solid #e74c3c;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#e74c3c;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#f39c12;background:#2c1500;border:1px solid #f39c12;border-radius:3px;padding:6px;margin-top:8px}
</style></head><body>
<h2>&#9876; BANDIT CAPTAIN — [r: tokenName]</h2>
<div class="sr"><span>AC 15 (studded leather)</span><span>HP 65</span><span>Speed 30 ft</span></div>
<div class="ab">
  <div class="lb">Multiattack: 2× Scimitar + 1× Dagger</div>
  [h: a1=1d20][h: a2=1d20][h: a3=1d20]
  <div class="rv">[r: a1+5] / [r: a2+5] / [r: a3+5]</div>
  <div class="dt">
    [h: d1=1d6][h: d2=1d6][h: d3=1d4]
    Scimitar 1: <b>[r: d1+3] slashing</b> | Scimitar 2: <b>[r: d2+3] slashing</b> | Dagger: <b>[r: d3+3] piercing</b>
  </div>
</div>
<div class="ab">
  <div class="lb">Dagger (ranged — 20/60 ft)</div>
  [h: ra=1d20] <div class="rv">Attack: [r: ra+5]</div>
  <div class="dt">[h: rd=1d4] Damage: <b>[r: rd+3] piercing</b></div>
</div>
<div class="nt">
  <b>Reaction — Parry:</b> +2 AC against one melee attack that would hit him. Must see attacker and be holding a melee weapon.
</div>
</body></html>
[/dialog]
