<!-- Zombie (CR 1/4) — S5 final vault
     Standard D&D 5e. AC 8, HP 22 (3d8+9), Speed 20 ft
     Undead Fortitude — hard to kill outright.
-->
[h: tokenName = getName()]
[dialog("Zombie Attacks", "width=380; height=300; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#1a1a1a;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#7f8c8d;margin:0 0 6px 0;font-size:15px;border-bottom:1px solid #7f8c8d;padding-bottom:4px}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#1a1a1a;border:1px solid #7f8c8d;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#95a5a6;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .cd{font-size:11px;color:#e67e22;background:#2c1500;border:1px solid #e67e22;border-radius:3px;padding:6px;margin-top:8px}
</style></head><body>
<h2>&#9760; ZOMBIE — [r: tokenName]</h2>
<div class="sr"><span>AC 8</span><span>HP 22</span><span>Speed 20 ft</span></div>
<div class="ab">
  <div class="lb">Slam</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+3]</div>
  <div class="dt">[h: dmg=1d6] Damage: <b>[r: dmg+1] bludgeoning</b> (1d6+1)</div>
</div>
<div class="cd">
  <b>Undead Fortitude:</b> If reduced to 0 HP by damage other than radiant or a critical hit: DC (5 + damage taken) Con save. On success: drops to 1 HP instead. Radiant damage and critical hits bypass this entirely — tell radiant-damage casters they are doubly useful in S5.
</div>
</body></html>
[/dialog]
