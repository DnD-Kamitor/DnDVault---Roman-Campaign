<!-- Alp (CR 4) — S3 extended rest encounter; sleeping-area threat
     Bestiary stat block (custom). AC 13, HP 78 (12d8+24), Speed 30 ft / fly 40 ft
     Attacks only sleeping or paralyzed targets. Iron at thresholds repels it.
     From: Shadow of Mars bestiary.qmd
-->
[h: tokenName = getName()]
[dialog("Alp: Nightmare Spirit", "width=440; height=480; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0d0020;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#9b59b6;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #9b59b6;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#1a0020;border:1px solid #9b59b6;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#9b59b6;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .cd{font-size:11px;color:#e74c3c;background:#2c0000;border:1px solid #e74c3c;border-radius:3px;padding:6px;margin-top:6px}
  .nt{font-size:11px;color:#f39c12;background:#2c1500;border:1px solid #f39c12;border-radius:3px;padding:6px;margin-bottom:8px}
</style></head><body>
<h2>&#9760; ALP — [r: tokenName]</h2>
<div class="sub">Nightmare spirit. Enters as mist. Sits on sleepers' chests. Iron at every threshold repels it.</div>
<div class="sr"><span>AC 13</span><span>HP 78</span><span>Fly 40 ft</span></div>
<div class="nt">
  <b>Counter:</b> Cold iron placed at every door, window, and vent repels the Alp entirely. One unguarded threshold lets it in. A rotating guard with torches prevents it from landing. It flees at any damage — use Mist Form immediately on taking any hit.
</div>
<div class="ab">
  <div class="lb">Nightmare Grip (sleeping/paralyzed targets only)</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+6]</div>
  <div class="dt">
    [h: dmg=3d8] Damage: <b>[r: dmg+3] psychic</b> (3d8+3)<br>
    Target DC 13 Wisdom save or gain one level of exhaustion and can't benefit from rest tonight.
  </div>
</div>
<div class="ab">
  <div class="lb">Claw (waking targets)</div>
  [h: catk=1d20] <div class="rv">Attack: [r: catk+5]</div>
  <div class="dt">[h: cdmg=2d4] Damage: <b>[r: cdmg+3] slashing</b> (2d4+3)</div>
</div>
<div class="ab">
  <div class="lb">Mist Form (reaction to any damage taken)</div>
  <div class="dt">The Alp instantly shifts to mist. It can't attack in this form but is immune to all damage until the start of its next turn. It repositions through gaps (under doors, through shutters). On its next turn it reforms — it does not flee the area, it resets.</div>
</div>
<div class="cd">
  <b>Paralytic Presence:</b> A creature that wakes mid-attack by the Alp must succeed on DC 14 Constitution save or be Paralyzed until the start of its next turn (sleep paralysis).
</div>
</body></html>
[/dialog]
