<!-- Germanic Berserker (CR 2) — S2, Vercingetorix's champion. Francisca FIRST, then greataxe. -->
[h: r1=1d20] [h: r2=1d20]
[h: dmg_francisca=1d6]
[h: dmg_axe=1d12]
[h: best=if(r1>=r2, r1, r2)]
/me attacks!<br>
<b>Francisca (thrown 20ft, ROUND 1):</b> ATK: [e: r1+5] | DMG: [e: dmg_francisca+3] slashing. DC 12 Acrobatics or lose shield bonus.<br>
<b>Greataxe (normal):</b> ATK: [e: r1+5] | DMG: [e: dmg_axe+3] slashing<br>
<b>Greataxe (RECKLESS — 2d20 take higher):</b> ATK: [e: best+5] (rolled [r: r1]/[r: r2]) | DMG: [e: dmg_axe+3] slashing<br>
<i style='color:#e05020'>(Reckless: all attacks vs berserker have advantage until his next turn. Danger Sense: adv on Dex saves vs visible effects.)</i>
