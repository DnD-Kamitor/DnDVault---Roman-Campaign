<!-- Cultist of Mars (CR 1/8) Attack Macro
     Campaign macro — select the Cultist token before running.
     Standard D&D 5e stat block: AC 12 (leather), HP 9 (2d8)
     CAMPAIGN NOTE: S1 cultists are not actively attacking yet. They stand watching.
     They only fight if the party attacks them or the Berserker is killed.
     After Berserker's death, they may snap out of trance (DM call).
-->
[h: tokenName = getName()]

[dialog("Cultist of Mars", "width=380; height=320; temporary=true;")]
<html>
<head>
<style>
  body { font-family: Georgia, serif; background:#0d0a1a; color:#e0e0e0; padding:12px; margin:0; }
  h2 { color:#c0392b; margin:0 0 4px 0; font-size:15px; border-bottom:1px solid #c0392b; padding-bottom:4px; }
  .subtitle { font-size:11px; color:#888; margin-bottom:8px; font-style:italic; }
  .stat-row { display:flex; justify-content:space-between; font-size:12px; color:#aaa; margin-bottom:8px; }
  .attack-box { background:#1a0a0a; border:1px solid #c0392b; border-radius:4px; padding:10px; margin-bottom:8px; }
  .label { font-size:11px; color:#c0392b; text-transform:uppercase; letter-spacing:1px; }
  .roll { font-size:26px; font-weight:bold; color:#fff; }
  .detail { font-size:12px; color:#bbb; margin-top:4px; }
  .note { font-size:11px; color:#3498db; background:#001a2c; border:1px solid #3498db; border-radius:3px; padding:6px; margin-top:8px; }
  .fanaticism { font-size:11px; color:#e67e22; background:#2c1500; border:1px solid #e67e22; border-radius:3px; padding:6px; margin-top:6px; }
</style>
</head>
<body>
<h2>&#9876; CULTIST OF MARS — [r: tokenName]</h2>
<div class="subtitle">Corrupted Legionary — Stage 1-2 corruption exposure</div>
<div class="stat-row"><span>AC 12 (leather)</span><span>HP 9</span><span>Speed 30 ft</span></div>

<div class="attack-box">
  <div class="label">Scimitar</div>
  [h: atk = 1d20]
  <div class="roll">Attack: [r: atk + 3] <span style="font-size:14px;color:#aaa;">(1d20+3)</span></div>
  <div class="detail">
    [h: dmg = 1d6]
    Damage: <b>[r: dmg + 1] slashing</b> (1d6+1)
  </div>
</div>

<div class="fanaticism">
  <b>Dark Devotion:</b> The cultist has advantage on saving throws against being Charmed or Frightened. Mars's corruption grants immunity to the normal fear that would make a fragile fighter retreat.
</div>

<div class="note">
  <b>S1 Behaviour:</b> These two cultists do not initiate combat. They watch and mutter. If the Berserker dies, DC 12 Wisdom save: on success they snap out of the trance and become frightened witnesses. On fail they attack in the Berserker's name. If subdued: they are legitimate witnesses to the corruption aura from the excavation shaft — useful to the party later.
</div>
</body>
</html>
[/dialog]
