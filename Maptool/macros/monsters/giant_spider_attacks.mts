<!-- Giant Spider (CR 1) — S3 Germanic forest
     AC 14, HP 26 (4d10+4), Speed 30 ft / climb 30 ft
-->
[h: tokenName = getName()]
[dialog("Giant Spider Attacks", "width=400; height=380; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0d0d0d;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#8e44ad;margin:0 0 6px 0;font-size:15px;border-bottom:1px solid #8e44ad;padding-bottom:4px}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#1a0d1a;border:1px solid #8e44ad;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#8e44ad;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#e67e22;background:#2c1500;border:1px solid #e67e22;border-radius:3px;padding:6px;margin-top:6px}
  .cd{font-size:11px;color:#e74c3c;background:#2c0000;border:1px solid #e74c3c;border-radius:3px;padding:6px;margin-top:6px}
</style></head><body>
<h2>&#9880; GIANT SPIDER — [r: tokenName]</h2>
<div class="sr"><span>AC 14</span><span>HP 26</span><span>Speed 30 ft / Climb 30 ft</span></div>
<div class="ab">
  <div class="lb">Bite</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+5] <span style="font-size:14px;color:#aaa">(1d20+5)</span></div>
  <div class="dt">[h: dmg=1d8] Damage: <b>[r: dmg+3] piercing</b> (1d8+3)</div>
  <div class="cd"><b>Poison:</b> DC 11 Constitution save or take 2d8 extra poison damage and be Poisoned for 1 hour. On save: half damage, not Poisoned.</div>
</div>
<div class="ab">
  <div class="lb">Web (ranged — 30/60 ft, recharge 5-6)</div>
  [h: watk=1d20] <div class="rv">Attack: [r: watk+5]</div>
  <div class="dt">Hit: target is Restrained. DC 12 Strength (action) to break free. Web has AC 10, HP 5, vulnerable to fire.</div>
</div>
<div class="nt">
  <b>Spider Climb:</b> Can move across ceilings and difficult surfaces. Web Sense: blind tremorsense 60 ft along a web. A party tangled in webs can't retreat cleanly — Spiders use Web first, then Bite restrained targets.
</div>
</body></html>
[/dialog]
