<!-- Vættir (CR 2) — S3 Germanic forest, nature spirit
     Nature spirits of land, sea, and sky. Normally neutral; hostile only when land is desecrated.
     AC 13, HP 40 (9d8), fly 40 ft (hover). Incorporeal when in spirit form.
-->
[h: tokenName = getName()]
[dialog("Vættir: Nature Spirit", "width=420; height=420; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#001a0d;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#2ecc71;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #2ecc71;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#001a0d;border:1px solid #2ecc71;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#2ecc71;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .cd{font-size:11px;color:#e74c3c;background:#2c0000;border:1px solid #e74c3c;border-radius:3px;padding:6px;margin-top:6px}
  .nt{font-size:11px;color:#f39c12;background:#2c1500;border:1px solid #f39c12;border-radius:3px;padding:6px;margin-bottom:8px}
</style></head><body>
<h2>&#9880; VÆTTIR — [r: tokenName]</h2>
<div class="sub">Land spirit — hostile only when its territory is desecrated or the grove is defiled.</div>
<div class="sr"><span>AC 13</span><span>HP 40</span><span>Fly 40 ft (hover)</span></div>
<div class="nt">
  <b>Propitiation:</b> A character who makes an offering and succeeds on DC 12 Religion check can calm one Vættir as an action, removing it from combat. Thusnelda's tribe knows the rites; if she is present, she can calm them all.
</div>
<div class="ab">
  <div class="lb">Spectral Strike (melee)</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+4]</div>
  <div class="dt">[h: dmg=2d8] Damage: <b>[r: dmg+2] force</b> (2d8+2) — bypasses non-magical weapon resistance</div>
</div>
<div class="ab">
  <div class="lb">Nature's Curse (60 ft, DC 13 Wis save)</div>
  <div class="dt">Target must succeed on DC 13 Wisdom save.</div>
  <div class="cd"><b>On fail:</b> Cursed for 1 hour. While cursed, all Survival, Nature, and Animal Handling checks are made at disadvantage — the land itself rejects the creature. Removing the curse requires Remove Curse or a successful propitiation rite.</div>
</div>
<div class="ab" style="border-color:#888">
  <div class="lb" style="color:#888">Incorporeal Movement</div>
  <div class="dt">Can move through other creatures and objects as difficult terrain. Takes 5 (1d10) force damage if it ends its turn inside an object. Resistant to bludgeoning, piercing, and slashing from non-magical weapons.</div>
</div>
</body></html>
[/dialog]
