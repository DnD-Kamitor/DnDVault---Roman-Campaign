<!-- Syrian Archer (CR 1/2) — Fort Vindolanda auxilia
     AC 13 (leather), HP 11 (2d8+2), Speed 30 ft -->
[h: tokenName = getName()]
[dialog("Syrian Archer Attacks", "width=380; height=280; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0a0a1a;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#B8860B;margin:0 0 6px 0;font-size:15px;border-bottom:1px solid #B8860B;padding-bottom:4px}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#1a1400;border:1px solid #B8860B;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#B8860B;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
</style></head><body>
<h2>&#127993; SYRIAN ARCHER — [r: tokenName]</h2>
<div class="sr"><span>AC 13 (leather)</span><span>HP 11</span><span>Speed 30 ft</span></div>
<div class="ab">
  <div class="lb">Composite Longbow (150/600 ft)</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+4] <span style="font-size:14px;color:#aaa">(1d20+4)</span></div>
  <div class="dt">[h: dmg=1d8] Damage: <b>[r: dmg+2] piercing</b> (1d8+2)</div>
</div>
<div class="ab">
  <div class="lb">Shortsword (melee fallback)</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+4] <span style="font-size:14px;color:#aaa">(1d20+4)</span></div>
  <div class="dt">[h: dmg=1d6] Damage: <b>[r: dmg+2] piercing</b> (1d6+2)</div>
</div>
<div class="ab" style="border-color:#555">
  <div class="lb" style="color:#555">Archer tactics</div>
  <div class="dt">Stays at range, uses Dodge if engaged melee. Cohors I Hamiorum auxilia — trained horse archers fighting on foot at Vindolanda.</div>
</div>
</body></html>
[/dialog]
