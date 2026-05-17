<!-- Specter (CR 1) — S5 final vault; also created by Wraith
     Standard D&D 5e. AC 12, HP 22 (5d8), fly 50 ft (hover)
-->
[h: tokenName = getName()]
[dialog("Specter Attacks", "width=380; height=340; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0d0020;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#8e44ad;margin:0 0 6px 0;font-size:15px;border-bottom:1px solid #8e44ad;padding-bottom:4px}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#1a0020;border:1px solid #8e44ad;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#8e44ad;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .cd{font-size:11px;color:#e74c3c;background:#2c0000;border:1px solid #e74c3c;border-radius:3px;padding:6px;margin-top:6px}
</style></head><body>
<h2>&#9760; SPECTER — [r: tokenName]</h2>
<div class="sr"><span>AC 12</span><span>HP 22</span><span>Fly 50 ft (hover)</span></div>
<div class="ab">
  <div class="lb">Life Drain</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+4]</div>
  <div class="dt">[h: dmg=3d6] Damage: <b>[r: dmg] necrotic</b> (3d6)</div>
  <div class="cd"><b>Max HP Reduction:</b> DC 10 Constitution save or target's HP maximum reduced by the necrotic damage. Lasts until long rest.</div>
</div>
<div class="ab" style="border-color:#888">
  <div class="lb" style="color:#888">Sunlight Weakness / Incorporeal</div>
  <div class="dt">Sunlight sensitivity. Incorporeal Movement. Immune to poison, necrotic. Resistant to bludgeoning/piercing/slashing from non-magical weapons. A crowd of Specters all applying max HP reduction can drop a character's ceiling faster than their actual HP — watch this carefully.</div>
</div>
</body></html>
[/dialog]
