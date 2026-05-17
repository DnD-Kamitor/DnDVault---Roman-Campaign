<!-- Larvae (CR 5) — S4 Principia basement area
     Bestiary stat block (custom). AC 14, HP 97 (13d8+39), Speed 30 ft / fly 30 ft
     Wears the face of someone the target has wronged. Resets rather than retreating.
     From: Shadow of Mars bestiary.qmd
-->
[h: tokenName = getName()]
[dialog("Larvae: Guilt Mask", "width=440; height=500; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#1a001a;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#8e44ad;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #8e44ad;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#1a001a;border:1px solid #8e44ad;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#8e44ad;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#e67e22;background:#2c1500;border:1px solid #e67e22;border-radius:3px;padding:6px;margin-bottom:8px}
  .cd{font-size:11px;color:#e74c3c;background:#2c0000;border:1px solid #e74c3c;border-radius:3px;padding:6px;margin-top:6px}
</style></head><body>
<h2>&#9760; LARVAE — [r: tokenName]</h2>
<div class="sub">Wears the face of someone the primary target wronged. Resets below 20 HP — does not flee.</div>
<div class="sr"><span>AC 14</span><span>HP 97</span><span>Speed 30 ft / Fly 30 ft</span></div>
<div class="nt">
  <b>DM prep:</b> Before the session, note which character has the most unresolved guilt. The Larvae opens wearing THAT person's face (choose from their backstory). While unrecognized, target has disadvantage on ALL saves vs Larvae. DC 15 Insight (active) to see through it. Burst it below 20 HP before the Threshold Reset — then chase it through the wall.
</div>
<div class="ab">
  <div class="lb">Corrupting Claw</div>
  [h: atk=1d20] <div class="rv">Attack: [r: atk+7]</div>
  <div class="dt">
    [h: dmg=2d8] Damage: <b>[r: dmg+4] psychic</b> (2d8+4)<br>
    DC 14 Wisdom save or Frightened until end of next turn.
  </div>
</div>
<div class="ab">
  <div class="lb">Memory Drain (60 ft, no attack roll)</div>
  <div class="dt">DC 14 Wisdom save. On fail: target loses one prepared spell slot (lowest available) or one use of a class feature until long rest. The target briefly relives the memory attached to the face the Larvae wears.</div>
</div>
<div class="cd">
  <b>Threshold Reset (below 20 HP):</b> The Larvae passes through the nearest solid surface and does not return until the start of its next turn. It does not flee — it resets. Face restores on re-entry. Current HP: track separately.<br><br>
  <b>Mask of the Familiar:</b> While wearing the unrecognized face, target has disadvantage on saves vs Larvae's abilities. When Larvae drops below half HP (48 HP), the face cycles each round searching for a stronger reaction.
</div>
</body></html>
[/dialog]
