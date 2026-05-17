<!-- Strix (CR 4) — night encounters, light source targeting
     Bestiary stat block (custom). AC 15, HP 78 (12d8+24), fly 60 ft
     Strike-and-withdraw. Targets light sources before targeting people.
     From: Shadow of Mars bestiary.qmd
-->
[h: tokenName = getName()]
[dialog("Strix: Night Predator", "width=420; height=440; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0d0d0d;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#95a5a6;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #95a5a6;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#1a1a1a;border:1px solid #95a5a6;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#95a5a6;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#e67e22;background:#2c1500;border:1px solid #e67e22;border-radius:3px;padding:6px;margin-bottom:8px}
</style></head><body>
<h2>&#9768; STRIX — [r: tokenName]</h2>
<div class="sub">Targets light sources first. Strike and withdraw. Sustained firelight repels it.</div>
<div class="sr"><span>AC 15</span><span>HP 78</span><span>Fly 60 ft</span></div>
<div class="nt">
  <b>Tactics:</b> Strix dives on the nearest light source (torch, lantern, spell), extinguishes it with Talons, withdraws 30 ft, then attacks the newly darkened target. Iron bells on the perimeter alert to its approach. A sustained bonfire it cannot extinguish keeps it at range indefinitely.
</div>
<div class="ab">
  <div class="lb">Talons (dive attack — moves before attack)</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+6]</div>
  <div class="dt">[h: dmg=2d6] Damage: <b>[r: dmg+4] slashing</b> (2d6+4). If targeting a held light source: DC 13 Strength save or light source is dropped/extinguished.</div>
</div>
<div class="ab">
  <div class="lb">Bite</div>
  [h: batk=1d20] <div class="rv">Attack: [r: batk+6]</div>
  <div class="dt">[h: bdmg=1d8] Damage: <b>[r: bdmg+4] piercing</b> (1d8+4)</div>
</div>
<div class="ab">
  <div class="lb">Blood Drain (recharge 5-6, attached)</div>
  [h: dratk=1d20] <div class="rv">Attach: [r: dratk+6]</div>
  <div class="dt">[h: drdmg=1d6] Initial: <b>[r: drdmg+4] piercing</b>. While attached: <b>[h: tick=1d6][r: tick+4] necrotic</b> at start of each Strix turn. DC 13 Strength (action) to pull free.</div>
</div>
</body></html>
[/dialog]
