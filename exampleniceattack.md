[h: r1 = 1d20]
[h: r2 = 1d20]

[h: radiantDice = if(CharLevel >= 17, 3, if(CharLevel >= 11, 2, if(CharLevel >= 5, 1, 0)))]

[h: atkNorm = r1 + Proficiency + IntMod]
[h: atkAdv  = max(r1, r2) + Proficiency + IntMod]
[h: atkDis  = min(r1, r2) + Proficiency + IntMod]

[h: isCritNorm = if(r1 == 20, 1, 0)]
[h: isCritAdv  = if(max(r1, r2) == 20, 1, 0)]
[h: isCritDis  = if(min(r1, r2) == 20, 1, 0)]

[h: weaponDie = 1d8]
[h: radiantDmg = if(radiantDice > 0, roll(radiantDice, 6), 0)]

[h: baseDmg = weaponDie + IntMod + radiantDmg]
[h: critDmg = baseDmg + 8 + radiantDice * 6]

[h: radText = if(radiantDice > 0, " + " + radiantDice + "d6 radiant", "")]
[h: radBreak = if(radiantDice > 0, " + " + radiantDmg, "")]
[h: radCritBreak = if(radiantDice > 0, " + " + radiantDmg + " + " + (radiantDice * 6), "")]

[h: dmgNormal = "1d8+" + IntMod + radText + " → " + weaponDie + " + " + IntMod + radBreak + " = " + baseDmg]
[h: dmgCrit = "<span style='color:#ffff44; font-weight:bold;'>⚡ CRIT</span><br>1d8+" + IntMod + "+8" + radText + " → " + weaponDie + " + " + IntMod + " + 8" + radCritBreak + " = " + critDmg]

[h: dmgTextNorm = if(isCritNorm, dmgCrit, "<b style='font-size:120%;'>" + dmgNormal + "</b>")]
[h: dmgTextAdv  = if(isCritAdv,  dmgCrit, "<b style='font-size:120%;'>" + dmgNormal + "</b>")]
[h: dmgTextDis  = if(isCritDis,  dmgCrit, "<b style='font-size:120%;'>" + dmgNormal + "</b>")]

[h: flavorRoll = 1d20]
[h: flavorList = "Radiant energy empowers your crushing blow!,The warhammer glows with divine light!,Your intellect guides the devastating strike!,Magical radiance trails your swing!,True Strike ensures your aim is perfect!,The weapon shimmers with holy power!,Arcane force enhances your impact!,Light and steel crush your enemy!,The enchanted hammer finds its mark!,Your mind focuses the radiant energy!,Radiance bursts from the point of impact!,You deliver a magically-guided smash!,Intelligence and force combine in power!,The glowing hammer strikes true!,Sacred energy courses through the weapon!,A warrior's weapon guided by knowledge!,Your tactical strike finds weakness!,The warhammer blazes with holy wrath!,You strike with brilliant fury!,Magic and muscle unite in impact!"]
[h: flavorText = listGet(flavorList, flavorRoll - 1)]

[h: output =
"<div style='background-color:#6b6b6b; color:white; padding:8px; border-radius:5px; border:2px solid #4a4a4a; font-family:Arial, sans-serif; min-width:700px; font-size:90%;'>" +

  "<div style='font-weight:bold; margin-bottom:5px; border-bottom:1px solid #7b7b7b; padding-bottom:3px;'>" +
    "✨ TRUE STRIKE WARHAMMER — ONE-HANDED <span style='font-style:italic; font-weight:normal; color:#e0e0e0; margin-left:12px; font-size:95%;'>" + flavorText + "</span>" +
  "</div>" +

  "<div style='font-size:92%; margin-bottom:6px; color:#e0e0e0;'>" +
    "2024 True Strike: weapon attack using Int | No Wand of the War Mage bonus<br>" +
    "Warhammer Mastery — Push: on hit, if the target is Large or smaller, push it up to 10 ft straight away from you<br>" + +
    "CharLevel " + CharLevel + " → +" + radiantDice + "d6 radiant" +
  "</div>" +

  "<table style='width:100%; border-collapse:collapse;'><tr>" +

  "<td style='background-color:rgba(0,0,0,0.2); padding:6px; border-radius:4px;'>" +
    "<div style='font-weight:bold; margin-bottom:2px;'>Normal</div>" +
    "<div style='white-space:nowrap;'>" +
      "To Hit: <b style='font-size:120%;'>" + atkNorm + "</b> <span style='font-size:85%;'>(" + r1 + "+" + Proficiency + "+" + IntMod + ")</span><br>" +
      "Damage: " + dmgTextNorm +
    "</div>" +
  "</td>" +

  "<td style='width:8px;'></td>" +

  "<td style='background-color:rgba(0,0,0,0.2); padding:6px; border-radius:4px;'>" +
    "<div style='font-weight:bold; margin-bottom:2px;'>Advantage</div>" +
    "<div style='white-space:nowrap;'>" +
      "To Hit: <b style='font-size:120%;'>" + atkAdv + "</b> <span style='font-size:85%;'>(max(" + r1 + "," + r2 + ")+" + Proficiency + "+" + IntMod + ")</span><br>" +
      "Damage: " + dmgTextAdv +
    "</div>" +
  "</td>" +

  "<td style='width:8px;'></td>" +

  "<td style='background-color:rgba(0,0,0,0.2); padding:6px; border-radius:4px;'>" +
    "<div style='font-weight:bold; margin-bottom:2px;'>Disadvantage</div>" +
    "<div style='white-space:nowrap;'>" +
      "To Hit: <b style='font-size:120%;'>" + atkDis + "</b> <span style='font-size:85%;'>(min(" + r1 + "," + r2 + ")+" + Proficiency + "+" + IntMod + ")</span><br>" +
      "Damage: " + dmgTextDis +
    "</div>" +
  "</td>" +

  "</tr></table>" +

"</div>"
]

[r, self: output]
