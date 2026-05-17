<!-- Myling (CR 2) — S3 Germanic forest, child-spirit undead
     Tome of Beasts (Kobold Press). AC 11, HP 78 (12d8+24), Speed 30 ft
     Seeks to be buried. Will not stop pursuing until buried or destroyed.
-->
[h: tokenName = getName()]
[dialog("Myling Attacks", "width=420; height=440; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0d0d1a;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#e74c3c;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #e74c3c;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#1a0000;border:1px solid #e74c3c;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#e74c3c;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .cd{font-size:11px;color:#e74c3c;background:#2c0000;border:1px solid #e74c3c;border-radius:3px;padding:6px;margin-top:6px}
  .nt{font-size:11px;color:#3498db;background:#001a2c;border:1px solid #3498db;border-radius:3px;padding:6px;margin-bottom:8px}
</style></head><body>
<h2>&#9760; MYLING — [r: tokenName]</h2>
<div class="sub">Unburied child's spirit. It wants burial. It will beg before it attacks.</div>
<div class="sr"><span>AC 11</span><span>HP 78</span><span>Speed 30 ft</span></div>
<div class="nt">
  <b>Resolution without combat:</b> A character who performs a burial rite over the Myling's physical remains (if found) or speaks words of passage (Religion DC 12, 1 action) causes the Myling to stop attacking and dissolve peacefully. Finding the remains first requires Investigation DC 13 in the area.
</div>
<div class="ab">
  <div class="lb">Grab</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+5]</div>
  <div class="dt">[h: dmg=2d6] Damage: <b>[r: dmg+3] bludgeoning</b> — target is Grappled (escape DC 13 Strength)</div>
  <div class="cd"><b>Deathly Weight:</b> While grappled, the target must succeed on DC 13 Strength check to move, or is pulled Prone. At end of target's turn while grappled: DC 13 Constitution save or gain 1 exhaustion level (max 3 from this ability).</div>
</div>
<div class="ab">
  <div class="lb">Bite (Grappled targets only)</div>
  [h: batk=1d20] <div class="rv">Attack: [r: batk+5] (advantage — target can't act)</div>
  <div class="dt">[h: bdmg=2d4] Damage: <b>[r: bdmg+3] piercing</b> (2d4+3)</div>
</div>
<div class="ab">
  <div class="lb">Horrifying Screech (30 ft, recharge 5-6)</div>
  <div class="dt">All creatures within 30 ft: DC 13 Constitution save.</div>
  <div class="cd"><b>On fail:</b> Frightened and Deafened for 1 minute. Repeat save at end of each turn.</div>
</div>
</body></html>
[/dialog]
