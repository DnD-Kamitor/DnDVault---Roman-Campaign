<!-- Wraith (CR 5) — S5 final vault
     Standard D&D 5e. AC 13, HP 67 (9d8+27), fly 60 ft (hover)
     Life Drain reduces max HP. Sunlight sensitivity. Can create Specters.
-->
[h: tokenName = getName()]
[dialog("Wraith Attacks", "width=420; height=440; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0d0020;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#9b59b6;margin:0 0 6px 0;font-size:15px;border-bottom:1px solid #9b59b6;padding-bottom:4px}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#1a0020;border:1px solid #9b59b6;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#9b59b6;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .cd{font-size:11px;color:#e74c3c;background:#2c0000;border:1px solid #e74c3c;border-radius:3px;padding:6px;margin-top:6px}
  .re{font-size:11px;color:#27ae60;background:#001a0d;border:1px solid #27ae60;border-radius:3px;padding:6px;margin-top:8px}
</style></head><body>
<h2>&#9760; WRAITH — [r: tokenName]</h2>
<div class="sr"><span>AC 13</span><span>HP 67</span><span>Fly 60 ft (hover)</span></div>
<div class="ab">
  <div class="lb">Life Drain (primary attack)</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+6]</div>
  <div class="dt">
    [h: dmg=4d8] Damage: <b>[r: dmg+3] necrotic</b> (4d8+3)
  </div>
  <div class="cd"><b>Max HP Reduction:</b> DC 14 Constitution save or target's HP maximum reduced by the necrotic damage dealt. Lasts until long rest. Target dies and becomes a Specter if max HP reaches 0.</div>
</div>
<div class="ab">
  <div class="lb">Create Specter (1 humanoid corpse within 10 ft, action)</div>
  <div class="dt">A humanoid killed by Life Drain or lying dead nearby rises as a Specter. The Specter is under the Wraith's control. A Wraith can have up to 7 Specters in service at once. <b>Do not let fallen PCs lie near it.</b></div>
</div>
<div class="re">
  <b>Resistances:</b> acid, cold, fire, lightning, thunder; bludgeoning/piercing/slashing from non-silvered, non-magical weapons.<br>
  <b>Immunities:</b> necrotic, poison. Incorporeal Movement.<br>
  <b>Sunlight sensitivity:</b> disadvantage on attacks and Perception in sunlight.
</div>
</body></html>
[/dialog]
