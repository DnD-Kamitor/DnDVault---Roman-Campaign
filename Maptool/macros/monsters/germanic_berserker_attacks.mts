<!-- Germanic Berserker (CR 2) — S2 wall assault, Phase 1-2
     AC 13 (hide), HP 67. Vercingetorix's champions.
     NOT the cult-maddened soldier from Session 1.
     Francisca throw FIRST, then greataxe at the parapet.
-->
[h: tokenName = getName()]
[dialog("Germanic Berserker Attacks", "width=420; height=440; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#1a0800;color:#e0e0d0;padding:12px;margin:0}
  h2{color:#e05020;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #e05020;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .rk{font-size:11px;color:#f39c12;background:#2c1a00;border:1px solid #f39c12;border-radius:3px;padding:8px;margin-bottom:8px}
  .ab{background:#2a0800;border:1px solid #e05020;border-radius:4px;padding:10px;margin-bottom:8px}
  .abr{background:#2a0800;border:1px solid #f39c12;border-radius:4px;padding:10px;margin-bottom:8px}
  .ab2{background:#1a1000;border:1px solid #8a6030;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#e05020;text-transform:uppercase;letter-spacing:1px}
  .lbr{font-size:11px;color:#f39c12;text-transform:uppercase;letter-spacing:1px}
  .lb2{font-size:11px;color:#8a6030;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .rp{font-size:11px;color:#9b59b6;background:#1a001a;border:1px solid #9b59b6;border-radius:3px;padding:6px;margin-top:8px}
</style></head><body>
<h2>&#9876; GERMANIC BERSERKER — [r: tokenName]</h2>
<div class="sub">Vercingetorix's champion — leads the ladder charge</div>
<div class="sr"><span>AC 13 (hide)</span><span>HP 67</span><span>Speed 30 ft</span></div>
<div class="rk">
  <b>&#9888; RECKLESS ATTACK (each turn, player's choice):</b> Gain advantage on ALL melee attacks this turn. ALL attacks against him have advantage until his next turn. A berserker almost always uses this — he trusts his HP to absorb it.
</div>
<div class="ab">
  <div class="lb">Francisca — Thrown (20/60 ft) · BEFORE mounting ladder</div>
  [h: atk=1d20]
  <div class="rv">Attack: [r: atk+5] <span style="font-size:14px;color:#aaa">(1d20+5)</span></div>
  <div class="dt">[h: dmg=1d6] Damage: <b>[r: dmg+3] slashing</b> (1d6+3)<br>
  Thrown axe bounces unpredictably — DC 12 Acrobatics or knock shield aside (GM: target loses shield bonus until they use bonus action to reseat it).</div>
</div>
<div class="ab">
  <div class="lb">Greataxe — Normal</div>
  [h: atk2=1d20]
  <div class="rv">Attack: [r: atk2+5] <span style="font-size:14px;color:#aaa">(1d20+5)</span></div>
  <div class="dt">[h: dmg2=1d12] Damage: <b>[r: dmg2+3] slashing</b> (1d12+3)</div>
</div>
<div class="abr">
  <div class="lbr">Greataxe — Reckless (roll 2d20, take higher)</div>
  [h: r1=1d20] [h: r2=1d20] [h: best=if(r1>=r2,r1+5,r2+5)]
  <div class="rv">Attack: [r: best] <span style="font-size:14px;color:#aaa">(rolled [r: r1] / [r: r2])</span></div>
  <div class="dt">[h: rdmg=1d12] Damage: <b>[r: rdmg+3] slashing</b> (1d12+3)<br>
  Remember: attackers have advantage against him this round.</div>
</div>
<div class="rp">
  <b>Danger Sense:</b> Advantage on Dex saves against effects he can see (ballista, oil flasks, spells with visible components).<br>
  <b>Behaviour:</b> Leads the western ladder. First over the parapet. Immediately attacks the nearest armed defender. Calls out in Germanic: he is here for the chieftain's honour, not for Roman gold.
</div>
</body></html>
[/dialog]
