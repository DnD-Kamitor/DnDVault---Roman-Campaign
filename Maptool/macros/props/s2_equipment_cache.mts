<!-- S2 Equipment Cache — Wall Defence Supply Depot
     Place this token in the fort courtyard (centre).
     GM right-clicks → runs this macro to show all available equipment.
     Defenders drag individual item tokens OR use this as a checklist.
     Track usage: cross out each item as used (MapTool notes field).
-->
[h: tokenName = getName()]
[dialog("S2 Wall Defence — Equipment Cache", "width=480; height=600; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#1a1000;color:#e0e0d0;padding:12px;margin:0}
  h2{color:#c8a040;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #c8a040;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sec{font-size:12px;color:#c8a040;text-transform:uppercase;letter-spacing:1px;margin:10px 0 4px 0;border-bottom:1px solid #3a2a00;padding-bottom:2px}
  .ab{background:#1e1400;border:1px solid #a08030;border-radius:4px;padding:8px;margin-bottom:6px}
  .ab2{background:#1e1400;border:1px solid #c04040;border-radius:4px;padding:8px;margin-bottom:6px}
  .ab3{background:#1e1400;border:1px solid #405080;border-radius:4px;padding:8px;margin-bottom:6px}
  .ab4{background:#1e1400;border:1px solid #406030;border-radius:4px;padding:8px;margin-bottom:6px}
  .it{font-size:13px;font-weight:bold;color:#fff}
  .qty{font-size:11px;color:#f39c12;float:right;font-weight:bold}
  .ef{font-size:12px;color:#bbb;margin-top:3px}
  .roll{font-size:13px;color:#60d060;font-weight:bold}
</style></head><body>
<h2>&#128672; S2 WALL DEFENCE — Equipment Cache</h2>
<div class="sub">Fort courtyard centre — Quartermaster Quartus's emergency depot</div>

<div class="sec">Ranged / Thrown — Priority</div>

<div class="ab2">
  <div class="it">Oil Flask (improvised fire bomb) <span class="qty">×8</span></div>
  <div class="ef">Thrown 20 ft. Dex DC 12 to hit square. <b>On hit:</b> target takes 2d6 fire dmg; area burns 5 ft radius, 1d6 fire/round for 2 rounds (DEX save DC 12 end of each turn to extinguish).
  <br><b>vs. Ogre:</b> Direct hit = 2d6 + ongoing. 3 hits likely stops him or forces reroute. Devastating on ladder bases (burning ladder = no climb for 2 rounds).
  [h: f1=1d6][h: f2=1d6] Hit damage: <span class="roll">[r: f1+f2] fire</span></div>
</div>

<div class="ab">
  <div class="it">Ballista Bolt Rack (south tower ballista) <span class="qty">×12 bolts</span></div>
  <div class="ef">Range 120/480 ft. Two operators: one aims (Dex DC 12 under pressure), one loads. Attack +6. Dmg 3d10 piercing.
  [h: b1=1d10][h: b2=1d10][h: b3=1d10] Damage: <span class="roll">[r: b1+b2+b3] piercing</span>
  <br>vs. Ogre: +6 to hit, 3/4 cover (AC 15). One bolt = average 17 dmg. Two hits likely staggers him. vs. Archers at zone 9: range 80ft — well within range.</div>
</div>

<div class="ab">
  <div class="it">Javelin Rack <span class="qty">×20</span></div>
  <div class="ef">Range 30/120 ft. STR atk +3. Dmg 1d6+STR piercing. One action = throw one.
  [h: jd=1d6] Damage: <span class="roll">[r: jd+3] piercing</span>
  <br>Good from wall vs. ladder climbers. No disadvantage on cramped parapet.</div>
</div>

<div class="ab">
  <div class="it">Arrow Bundle (for any bowman) <span class="qty">×60 arrows (6 bundles)</span></div>
  <div class="ef">Standard arrows, no special properties. Each bundle = 10 arrows. Distribute to party archers at start of combat.</div>
</div>

<div class="sec">Area Denial — Gate + Ladder</div>

<div class="ab2">
  <div class="it">Boiling Water Cauldrons <span class="qty">×3 cauldrons</span></div>
  <div class="ef">Action to tip over parapet onto a 5-ft square below. DEX save DC 13 or 3d6 fire damage. Half on save.
  [h: w1=1d6][h: w2=1d6][h: w3=1d6] Damage: <span class="roll">[r: w1+w2+w3] fire</span>
  <br>Takes 1 action to drag into position (already preheated). Devastating on ladder climbers (no cover).</div>
</div>

<div class="ab3">
  <div class="it">Caltrops (bag) <span class="qty">×4 bags</span></div>
  <div class="ef">Cover 5-ft square. Any creature entering: DEX save DC 15 or speed = 2 ft (until magically healed or DC 15 Medicine). No damage but stops rushers cold. Spread at gate breach or on courtyard approach.</div>
</div>

<div class="ab3">
  <div class="it">Portable Barricade (pre-built) <span class="qty">×2</span></div>
  <div class="ef">Drag into gate breach: costs one action + Athletics DC 12. HP 30, AC 13. Gives half cover to defenders behind it. Ogre must beat it down (greatclub +6 = ~13/swing) before entering. Buys 2–3 extra rounds.</div>
</div>

<div class="sec">Melee / Close Defence</div>

<div class="ab4">
  <div class="it">Spare Shields (legionary scutum) <span class="qty">×6</span></div>
  <div class="ef">+2 AC. Any character proficient with shields can equip as bonus action. Pre-equipped = ready. Useful if a defender's shield is destroyed or if someone comes without one.</div>
</div>

<div class="ab4">
  <div class="it">Spare Spears <span class="qty">×8</span></div>
  <div class="ef">Dmg 1d6 piercing (1d8 two-handed). Reach 5 ft. STR or DEX +3 attack. Good parapet weapon — longer reach than sword on narrow wall.</div>
</div>

<div class="ab4">
  <div class="it">Rope + Grapple Hook <span class="qty">×2</span></div>
  <div class="ef">Push a ladder away from wall: Athletics DC 14 as action (disadvantage if under fire). Dislodge = climber falls (1d6 per 10 ft fallen, DEX save DC 13 for half).</div>
</div>

<div class="sec">Medical / Support</div>

<div class="ab3">
  <div class="it">Healers Kit <span class="qty">×3 kits (30 uses)</span></div>
  <div class="ef">Stabilise dying creature: Medicine DC 10. No spell slot needed. One use per kit per creature per combat. Distribute to Julia Jana, Tanit, or any non-combatant character.</div>
</div>

<div class="ab3">
  <div class="it">Torch Bundle <span class="qty">×12 torches</span></div>
  <div class="ef">Improvised melee: 1d4 fire. Light source 20-ft radius. Primary use: set ladder bases on fire (bonus action throw, DEX DC 10 to attach to ladder; ladder burns for 1d4 rounds, half speed to climb).</div>
</div>

</body></html>
[/dialog]
