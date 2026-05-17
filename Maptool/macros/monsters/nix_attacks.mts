<!-- Nix (CR 3) — S2 Rhine river crossing
     Bestiary stat block (custom). AC 14, HP 65 (10d8+20), Speed 30 ft / swim 50 ft
     Shapechanger. Always starts disguised. River-bound advantage and HP regen in water.
     From: Shadow of Mars bestiary.qmd
-->
[h: tokenName = getName()]
[dialog("Nix: River Shapechanger", "width=440; height=480; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#001a1a;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#1abc9c;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #1abc9c;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#001a1a;border:1px solid #1abc9c;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#1abc9c;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#e67e22;background:#2c1500;border:1px solid #e67e22;border-radius:3px;padding:6px;margin-bottom:8px}
  .cd{font-size:11px;color:#e74c3c;background:#2c0000;border:1px solid #e74c3c;border-radius:3px;padding:6px;margin-top:6px}
</style></head><body>
<h2>&#9875; NIX — [r: tokenName]</h2>
<div class="sub">River shapechanger. Always starts disguised. Vercingetorix's tribe knows its name.</div>
<div class="sr"><span>AC 14</span><span>HP 65</span><span>Speed 30 ft / Swim 50 ft</span></div>
<div class="nt">
  <b>River Bound:</b> Within 1 mile of its river, Nix has advantage on ALL checks/saves and regains 10 HP at start of each turn while partially submerged. Fight it on land if possible. Vercingetorix knows its name — knowing a Nix's name allows a DC 12 Charisma check to demand one answer honestly.
</div>
<div class="ab">
  <div class="lb">Unearthly Beauty (passive aura, 30 ft, humanoid form only)</div>
  <div class="dt">Humanoid that starts its turn within 30 ft and can see Nix: DC 15 Wisdom save or Charmed 1 minute. Charmed creature uses movement to approach by most direct route. Charm ends if target takes damage. Target that interacted with Nix's disguise for 10+ min: save at disadvantage.</div>
</div>
<div class="ab">
  <div class="lb">Claw</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+5]</div>
  <div class="dt">[h: dmg=2d6] Damage: <b>[r: dmg+2] slashing</b> (2d6+2)</div>
</div>
<div class="ab">
  <div class="lb">Drowning Song (1/day, 60 ft, chosen target)</div>
  <div class="dt">DM selects the character with the most unresolved emotional stake. DC 15 Wisdom save. On fail: Incapacitated and must move toward the water by most direct route until they succeed on a save at the start of each of their turns, or until they take damage.</div>
  <div class="cd">The Nix targets correctly, not randomly. A Nix that uses this on the wrong person is just a monster. A Nix that uses it on the right person is a mirror.</div>
</div>
</body></html>
[/dialog]
