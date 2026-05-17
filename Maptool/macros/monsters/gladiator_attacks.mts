<!-- Gladiator (CR 5) — Vercingetorix, S2+
     AC 16 (studded leather + shield), HP 112 (15d8+45), Speed 30 ft
     CAMPAIGN NOTE: Vercingetorix does NOT attack the party unless attacked first.
     He wants to reach the spear. His grandfather died by it three generations ago.
-->
[h: tokenName = getName()]
[dialog("Gladiator: Vercingetorix", "width=440; height=500; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#1a0d00;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#e8c547;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #e8c547;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#2a1f00;border:1px solid #e8c547;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#e8c547;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#3498db;background:#001a2c;border:1px solid #3498db;border-radius:3px;padding:6px;margin-bottom:8px}
  .re{font-size:11px;color:#e67e22;background:#2c1500;border:1px solid #e67e22;border-radius:3px;padding:6px;margin-top:6px}
</style></head><body>
<h2>&#9876; GLADIATOR — [r: tokenName]</h2>
<div class="sub">Vercingetorix — ally unless attacked. Rune weapon (+1 shortsword, Tiwaz rune: +1d6 radiant vs oath-breakers)</div>
<div class="sr"><span>AC 16 (+shield)</span><span>HP 112</span><span>Speed 30 ft</span></div>
<div class="nt">
  <b>Roleplay first:</b> Vercingetorix is direct and formally furious. He communicates in Latin (partly adopted from Roman contact). He does not want the party dead — he wants the spear. If the party fights him unprovoked, they have made an enemy of the one Germanic leader who could help them.
</div>
<div class="ab">
  <div class="lb">Multiattack: 3× Spear (or 2× Spear + 1× Shield Bash)</div>
  [h: a1=1d20][h: a2=1d20][h: a3=1d20]
  <div class="rv">[r: a1+7] / [r: a2+7] / [r: a3+7]</div>
  <div class="dt">
    [h: d1=1d8][h: d2=1d8][h: d3=1d8]
    Spear 1: <b>[r: d1+4] piercing</b> | Spear 2: <b>[r: d2+4]</b> | Spear 3: <b>[r: d3+4]</b> (one-hand 1d6+4, two-hand 1d8+4)
  </div>
</div>
<div class="ab">
  <div class="lb">Shield Bash (replaces one spear attack)</div>
  [h: sb=1d20] <div class="rv">Attack: [r: sb+7]</div>
  <div class="dt">[h: sd=2d6] Damage: <b>[r: sd+4] bludgeoning</b> — DC 15 Strength save or knocked Prone</div>
</div>
<div class="re">
  <b>Reaction — Parry:</b> +3 AC against one melee attack that would hit. Must see attacker and be holding a melee weapon.<br><br>
  <b>Tiwaz Rune (shortsword):</b> Against a creature that has broken an oath or acted dishonorably, deal extra 1d6 radiant damage on a hit. DM decides when this applies.
</div>
</body></html>
[/dialog]
