<!-- Goblin Skirmisher (CR 1/4) — S3 optional
     AC 15 (leather + shield), HP 7 (2d6), Speed 30 ft -->
[h: tokenName = getName()]
[dialog("Goblin Skirmisher Attacks", "width=380; height=280; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0a0a1a;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#556B2F;margin:0 0 6px 0;font-size:15px;border-bottom:1px solid #556B2F;padding-bottom:4px}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#0a1a0a;border:1px solid #556B2F;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#556B2F;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
</style></head><body>
<h2>&#9760; GOBLIN SKIRMISHER — [r: tokenName]</h2>
<div class="sr"><span>AC 15 (leather+shield)</span><span>HP 7</span><span>Speed 30 ft</span></div>
<div class="ab">
  <div class="lb">Scimitar</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+4] <span style="font-size:14px;color:#aaa">(1d20+4)</span></div>
  <div class="dt">[h: dmg=1d6] Damage: <b>[r: dmg+2] slashing</b> (1d6+2)</div>
</div>
<div class="ab">
  <div class="lb">Shortbow (80/320 ft)</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+4] <span style="font-size:14px;color:#aaa">(1d20+4)</span></div>
  <div class="dt">[h: dmg=1d6] Damage: <b>[r: dmg+2] piercing</b> (1d6+2)</div>
</div>
<div class="ab" style="border-color:#555">
  <div class="lb" style="color:#555">Nimble Escape</div>
  <div class="dt">Bonus action: Disengage or Hide each turn. Use this — goblins kite and harass, never stand and fight.</div>
</div>
</body></html>
[/dialog]
