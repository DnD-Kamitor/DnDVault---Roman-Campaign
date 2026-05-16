<!-- ============================================================
     Shadow of Mars — Corruption Tracker
     MapTool 1.13+ MTScript

     SETUP (one-time):
       1. Open MapTool > Edit > Campaign Properties > Token Properties
       2. Add a Number property named: CorruptionLevel   (default 0)
       3. Create a new macro on the Campaign panel, paste this code.
       4. Mark the macro "Apply to Tokens" = false.
          Run it by selecting a player token and clicking the macro.

     TOKEN PROPERTY USED:
       CorruptionLevel  (integer 0-5)
   ============================================================ -->

[h: tName  = getTokenName()]
[h: cLevel = getProperty("CorruptionLevel")]
[h: cLevel = if(cLevel == "" || !isNumber(cLevel), 0, cLevel + 0)]

<!-- Stage names -->
[h: sName  = json.get(json.fromList("Unmarked,Noticed,Pulled,Claimed,Consumed,Mars-Sworn"), cLevel)]

<!-- Mechanical effects per level -->
[h: effects = json.fromList(
  "No effect. You are the baseline.",
  "DC 10 Wisdom save each dawn. Fail = visions of conquest linger through the morning.",
  "Disadvantage on all Wisdom saving throws.",
  "DC 12 Wisdom save to willingly disengage from combat.",
  "DC 14 Wisdom save to avoid attacking allies when below half HP.",
  "Character passes to GM control. Mars-Sworn. No further saves."
)]
[h: fx = json.get(effects, cLevel)]

<!-- Pip row: filled circles for current level -->
[h: pipHtml = ""]
[h: i = 0]
[while(i <= 5, 1):
  {
    [h: filled = if(i <= cLevel, "filled", "")]
    [h: pipHtml = pipHtml + "<div class='pip " + filled + "'></div>"]
    [h: i = i + 1]
  }
]

<!-- Build increase / decrease buttons -->
[h: btnIncrease = if(cLevel < 5,
  "<a class='btn red' href='" + macroLink("corruption_increase@campaign", "TOKEN", "", currentToken()) + "'>▲ Increase</a>",
  "<span class='btn disabled'>▲ Increase</span>"
)]
[h: btnDecrease = if(cLevel > 0,
  "<a class='btn dim' href='" + macroLink("corruption_decrease@campaign", "TOKEN", "", currentToken()) + "'>▼ Decrease</a>",
  "<span class='btn disabled'>▼ Decrease</span>"
)]
[h: btnReset = "<a class='btn dim' href='" + macroLink("corruption_reset@campaign", "TOKEN", "", currentToken()) + "'>Reset to 0</a>"]

[frame("Corruption: " + tName, "width=380; height=300"): {
<html>
<head>
<style>
  body  { font-family: Georgia, serif; background: #1a0800; color: #c8a060; padding: 14px; margin: 0; }
  h2    { font-size: 14px; color: #e87020; margin: 0 0 6px; letter-spacing: .06em; }
  .lvl  { font-size: 28px; font-weight: bold; color: #ff6010; }
  .sn   { font-size: 13px; font-style: italic; color: #d09050; margin-left: 6px; }
  .pips { display: flex; gap: 5px; margin: 8px 0; }
  .pip  { width: 18px; height: 18px; border-radius: 50%; background: #3a1800; border: 2px solid #6a3010; }
  .pip.filled { background: #e05000; border-color: #ff7020; }
  .fx   { background: #2a1000; border-left: 3px solid #8b2500; padding: 7px 9px; font-size: 11px; margin: 8px 0; line-height: 1.5; }
  .btns { display: flex; gap: 6px; margin-top: 10px; flex-wrap: wrap; }
  .btn  { padding: 5px 12px; border-radius: 3px; font-size: 11px; text-decoration: none; cursor: pointer; }
  .btn.red     { background: #8b1500; color: #f0a060; }
  .btn.dim     { background: #3a1800; color: #c08040; }
  .btn.disabled { background: #1a0800; color: #4a2010; cursor: default; }
</style>
</head>
<body>
  <h2>[r: tName]</h2>
  <div>
    <span class="lvl">[r: cLevel]</span>
    <span class="sn">— [r: sName]</span>
  </div>
  <div class="pips">[r: pipHtml]</div>
  <div class="fx">[r: fx]</div>
  <div class="btns">
    [r: btnIncrease]
    [r: btnDecrease]
    [r: btnReset]
  </div>
</body>
</html>
}]
