<!-- S2 West Gate Integrity Tracker — HP 60. Ogre rams automatic each round (3d6+4). GM prop token. -->
[h: gateHP = getProperty("GateHP")]
[h: gateHP = if(string(gateHP) == "" || string(gateHP) == "0", 60, gateHP+0)]
[h: d1=1d6] [h: d2=1d6] [h: d3=1d6]
[h: dmg = d1+d2+d3+4]
[h: newHP = max(0, gateHP - dmg)]
[h: setProperty("GateHP", newHP)]
[h: pct = newHP * 100 / 60]
[h: col = if(newHP <= 0, "#ff2020", if(newHP <= 20, "#ff8020", if(newHP <= 40, "#e8c020", "#60c840")))]
[h: statusLine = if(newHP <= 0, "<b style='color:#ff2020;font-size:14px'>⚠ GATE BREACHED — OGRE CHARGES IN!</b>", if(newHP <= 20, "<b style='color:#ff8020'>BREACH IMMINENT — 1-2 rounds left!</b>", if(newHP <= 40, "<i style='color:#e8c020'>Gate buckling — reinforce or flee.</i>", "<i style='color:#6aaa50'>Gate holding.</i>")))]
/me OGRE RAMS THE WEST GATE!<br>
<b>Damage:</b> [e: dmg] bludgeoning ([r: d1] + [r: d2] + [r: d3] + 4)<br>
<b>Gate HP:</b> <span style='color:[r: col]'>[r: newHP] / 60</span><br>
[r: statusLine]
