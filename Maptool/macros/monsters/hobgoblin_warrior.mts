<!-- Hobgoblin Warrior (CR 1/2) — S3 optional
     AC 18 (chain mail + shield), HP 11 (2d8+2), Speed 30 ft -->
[h: tokenName = getName()]
[dialog("Hobgoblin Warrior Attacks", "width=380; height=280; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0a0a1a;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#8B0000;margin:0 0 6px 0;font-size:15px;border-bottom:1px solid #8B0000;padding-bottom:4px}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#1a0a0a;border:1px solid #8B0000;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#8B0000;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
</style></head><body>
<h2>&#9876; HOBGOBLIN WARRIOR — [r: tokenName]</h2>
<div class="sr"><span>AC 18 (chain+shield)</span><span>HP 11</span><span>Speed 30 ft</span></div>
<div class="ab">
  <div class="lb">Longsword</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+3] <span style="font-size:14px;color:#aaa">(1d20+3)</span></div>
  <div class="dt">[h: dmg=1d8] One-hand: <b>[r: dmg+1] slashing</b> (1d8+1) | Two-hand: [h: dmg2=1d10]<b>[r: dmg2+1]</b> (1d10+1)</div>
</div>
<div class="ab">
  <div class="lb">Longbow (150/600 ft)</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+3] <span style="font-size:14px;color:#aaa">(1d20+3)</span></div>
  <div class="dt">[h: dmg=1d8] Damage: <b>[r: dmg+1] piercing</b> (1d8+1)</div>
</div>
<div class="ab" style="border-color:#555">
  <div class="lb" style="color:#555">Martial Advantage</div>
  <div class="dt">Once per turn, +2d6 damage if an ally is adjacent to the target. Position hobgoblins in pairs.</div>
</div>
</body></html>
[/dialog]
