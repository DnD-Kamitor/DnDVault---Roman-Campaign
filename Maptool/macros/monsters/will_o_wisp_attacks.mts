<!-- Will-o'-Wisp (CR 2) — S4 sacred grove, optional encounter
     Standard D&D 5e. AC 19, HP 22 (9d4), fly 50 ft (hover)
     Effectively immune to most weapons when invisible. Feeds on dying creatures.
-->
[h: tokenName = getName()]
[dialog("Will-o'-Wisp", "width=420; height=420; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#00001a;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#3498db;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #3498db;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#00001a;border:1px solid #3498db;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#3498db;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#e67e22;background:#2c1500;border:1px solid #e67e22;border-radius:3px;padding:6px;margin-bottom:8px}
  .cd{font-size:11px;color:#e74c3c;background:#2c0000;border:1px solid #e74c3c;border-radius:3px;padding:6px;margin-top:6px}
</style></head><body>
<h2>&#9728; WILL-O'-WISP — [r: tokenName]</h2>
<div class="sub">Grove spirit manifestation. Feeds on dying creatures. Almost impossible to hit when invisible.</div>
<div class="sr"><span>AC 19</span><span>HP 22</span><span>Fly 50 ft (hover)</span></div>
<div class="nt">
  <b>Tactics:</b> It goes Invisible as a bonus action, shocks from safety, then turns visible briefly to draw a dying character closer. Force damage, radiant damage, or spell effects that can target invisible creatures are the answer. If the party has a downed character, the Will-o-Wisp will try to use Consume Life on them — address this immediately.
</div>
<div class="ab">
  <div class="lb">Shock (lightning damage)</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+4]</div>
  <div class="dt">[h: dmg=2d8] Damage: <b>[r: dmg] lightning</b> (2d8)</div>
</div>
<div class="ab">
  <div class="lb">Consume Life (vs creature at 0 HP within 5 ft)</div>
  <div class="dt">Target must succeed on DC 10 Constitution saving throw or die. The Will-o-Wisp regains 10 (3d6) HP. A character stabilized with Medicine is still vulnerable to this.</div>
</div>
<div class="cd">
  <b>Invisibility (bonus action):</b> Becomes invisible until it attacks or uses Consume Life, or until concentration ends. Attackers have disadvantage on attacks against it while invisible.<br><br>
  <b>Resistances:</b> Acid, cold, fire, necrotic, thunder. <b>Immunities:</b> lightning, poison. Non-magical weapons barely dent it. Focus spells and force damage.
</div>
</body></html>
[/dialog]
