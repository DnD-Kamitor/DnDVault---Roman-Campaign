<!-- Fausta Luperci — S5 Option A: Trial of Champions
     Custom stat block: Champion-tier warrior, honored dead called by Mars.
     AC 18 (plate), HP 130 (17d8+51), Speed 30 ft.
     Legendary Defiance at 50 HP. Mars calls "Enough" after 10 rounds or at 0 HP.
     She fought alone at the Frozen Rhine. She respects endurance, not tricks.
-->
[h: tokenName = getName()]
[dialog("Fausta Luperci — Option A Champion", "width=440; height=500; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#0d1a1a;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#1abc9c;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #1abc9c;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#0d1a1a;border:1px solid #1abc9c;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#1abc9c;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#3498db;background:#001a2c;border:1px solid #3498db;border-radius:3px;padding:6px;margin-bottom:8px}
  .cd{font-size:11px;color:#e8c547;background:#1a1a00;border:1px solid #e8c547;border-radius:3px;padding:6px;margin-top:6px}
</style></head><body>
<h2>&#9876; FAUSTA LUPERCI — [r: tokenName]</h2>
<div class="sub">"She held the line at the Frozen Rhine when your Empire would not. She died alone."</div>
<div class="sr"><span>AC 18 (plate)</span><span>HP 130</span><span>Speed 30 ft</span></div>
<div class="nt">
  <b>She is real.</b> History DC 14 passive: this engagement and this soldier were real. Mars called a specific honored dead. She held a line, alone, and died. The party is fighting a person, not a construct. She respects endurance and discipline. She does not respect tricks. Roleplay her as someone who is doing a job.
</div>
<div class="ab">
  <div class="lb">Multiattack: 3× Longsword</div>
  [h: a1=1d20][h: a2=1d20][h: a3=1d20]
  <div class="rv">[r: a1+8] / [r: a2+8] / [r: a3+8]</div>
  <div class="dt">
    [h: d1=1d8][h: d2=1d8][h: d3=1d8]
    Attack 1: <b>[r: d1+5] slashing</b> | Attack 2: <b>[r: d2+5]</b> | Attack 3: <b>[r: d3+5]</b>
  </div>
</div>
<div class="ab">
  <div class="lb">Shield Bash (bonus action)</div>
  [h: sb=1d20] <div class="rv">Attack: [r: sb+8]</div>
  <div class="dt">[h: sd=2d4] Damage: <b>[r: sd+5] bludgeoning</b> — DC 15 Strength save or knocked Prone</div>
</div>
<div class="cd">
  <b>Legendary Defiance (when she drops below 50 HP):</b> She gains 20 temporary HP and automatically succeeds on one saving throw of her choice. Mars calls "Enough" when she is reduced to 0 HP or after 10 rounds. She kneels deliberately. She does not rage or beg. She folds. Victory: endure 10 rounds OR bring her to 0 HP.
</div>
</body></html>
[/dialog]
