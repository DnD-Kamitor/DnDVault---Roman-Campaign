<!-- Animated Armor (CR 1) — S4 Sunken Armory, divine construct NOT undead
     Standard D&D 5e stat block. AC 18, HP 33 (6d8+6), Speed 25 ft
     CAMPAIGN NOTE: These are divine constructs — Mars' blessing on consecrated armor.
     NOT undead. Undead-specific abilities (Turn Undead, etc.) do NOT work.
     They react to hesitation — decisive movement does not draw them.
-->
[h: tokenName = getName()]
[dialog("Animated Armor: Divine Construct", "width=420; height=380; temporary=true;")]
<html><head><style>
  body{font-family:Georgia,serif;background:#1a0a00;color:#e0e0e0;padding:12px;margin:0}
  h2{color:#e8c547;margin:0 0 4px 0;font-size:15px;border-bottom:1px solid #e8c547;padding-bottom:4px}
  .sub{font-size:11px;color:#888;margin-bottom:8px;font-style:italic}
  .sr{display:flex;justify-content:space-between;font-size:12px;color:#aaa;margin-bottom:8px}
  .ab{background:#2a1a00;border:1px solid #e8c547;border-radius:4px;padding:10px;margin-bottom:8px}
  .lb{font-size:11px;color:#e8c547;text-transform:uppercase;letter-spacing:1px}
  .rv{font-size:26px;font-weight:bold;color:#fff}
  .dt{font-size:12px;color:#bbb;margin-top:4px}
  .nt{font-size:11px;color:#e74c3c;background:#2c0000;border:1px solid #e74c3c;border-radius:3px;padding:6px;margin-bottom:8px}
</style></head><body>
<h2>&#9876; ANIMATED ARMOR — [r: tokenName]</h2>
<div class="sub">S4 Sunken Armory — divine resonance, not undead. Turn Undead does nothing.</div>
<div class="sr"><span>AC 18</span><span>HP 33</span><span>Speed 25 ft</span></div>
<div class="nt">
  <b>Key DM note:</b> These target anyone who hesitates. A character who moves decisively through the armory without touching armor pieces or lingering near them does not trigger activation. Characters who stop, examine, or touch pieces trigger the armor nearest them. The clue under a corroded shield says: "The god hears the loudest heart."
</div>
<div class="ab">
  <div class="lb">Multiattack: 2× Slam</div>
  [h: a1=1d20][h: a2=1d20]
  <div class="rv">[r: a1+4] / [r: a2+4]</div>
  <div class="dt">
    [h: d1=1d6][h: d2=1d6]
    Slam 1: <b>[r: d1+2] bludgeoning</b> (1d6+2) | Slam 2: <b>[r: d2+2]</b>
  </div>
</div>
<div class="ab" style="border-color:#888">
  <div class="lb" style="color:#888">Construct traits</div>
  <div class="dt">
    Immune to: poison, psychic damage; Blinded, Charmed, Deafened, Exhaustion, Frightened, Paralyzed, Petrified, Poisoned.<br>
    Darkvision 60 ft. Does not breathe, eat, or sleep.
  </div>
</div>
</body></html>
[/dialog]
