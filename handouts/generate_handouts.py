#!/usr/bin/env python3
"""
Generate all Shadow of Mars campaign handouts as PDFs.

Usage:  python3 handouts/generate_handouts.py
Output: handouts/handout_NN_slug.pdf  (10 files)
"""

import os
import subprocess
import sys

try:
    from weasyprint import HTML
except ImportError:
    sys.exit("weasyprint not found. Run: pip3 install --user weasyprint")

OUT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# CSS — page setup
# ---------------------------------------------------------------------------

PAGE = """
@page { size: A5; margin: 14mm; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: P052, 'URW Bookman', 'Garamond Libre', 'Liberation Serif', serif; }
"""

# ---------------------------------------------------------------------------
# CSS — four visual themes
# ---------------------------------------------------------------------------

WAX = """
body { background: #1a0e06; }
.card {
  background: #3d1a0a;
  border: 2px solid #5c2810;
  outline: 5px solid #2a0c04;
  outline-offset: 2px;
  border-radius: 5px;
  padding: 30px 34px;
  color: #e8c090;
}
.heading {
  font-size: 10.5pt;
  font-weight: bold;
  letter-spacing: 0.18em;
  color: #c87832;
  text-align: center;
  text-transform: uppercase;
  margin-bottom: 18px;
}
.rule { height: 1px; background: #8b4010; margin: 14px 0; }
.body-text { font-family: P052, 'Liberation Serif', serif; font-size: 11pt; line-height: 1.95; }
.translation {
  font-style: italic;
  color: #a06030;
  font-size: 10.5pt;
  line-height: 1.8;
  margin-top: 14px;
  padding-top: 14px;
  border-top: 1px dashed #5c2810;
}
.seal {
  font-size: 9.5pt;
  letter-spacing: 0.22em;
  color: #8b4010;
  text-align: center;
  margin-top: 18px;
  text-transform: uppercase;
}
.bullet-list { margin-left: 1.1em; margin-top: 6px; }
.bullet-list li { margin-bottom: 7px; font-size: 10.5pt; line-height: 1.7; }
.sub-heading { font-size: 10pt; font-weight: bold; letter-spacing: 0.1em; color: #c87832; margin-top: 14px; margin-bottom: 6px; text-transform: uppercase; }
"""

STONE = """
body { background: #3a3028; }
.card {
  background: #cec9be;
  border: 3px solid #8a7a6a;
  border-radius: 2px;
  padding: 30px 34px;
  color: #1a1208;
}
.heading {
  font-size: 11pt;
  font-weight: bold;
  letter-spacing: 0.2em;
  text-align: center;
  text-transform: uppercase;
  color: #2a1a08;
  margin-bottom: 14px;
}
.rule { height: 2px; background: #8a7a6a; margin: 12px 0; }
.rune-row {
  font-size: 13pt;
  font-weight: bold;
  letter-spacing: 0.25em;
  text-align: center;
  color: #1a1208;
  margin-bottom: 6px;
}
.rune-gloss {
  font-size: 9pt;
  letter-spacing: 0.18em;
  text-align: center;
  color: #5a4a38;
  text-transform: uppercase;
  margin-bottom: 16px;
}
.body-text { font-family: 'NimbusRoman', P052, 'Liberation Serif', serif; font-size: 10.5pt; line-height: 1.85; font-style: italic; }
.warning {
  font-size: 12pt;
  font-weight: bold;
  color: #3a1010;
  text-align: center;
  margin-top: 16px;
  letter-spacing: 0.08em;
}
"""

PAPYRUS = """
body { background: #4a3a1a; }
.card {
  background: #f2e2a8;
  border: 2px solid #8a6a3a;
  border-radius: 3px;
  padding: 30px 34px;
  color: #1a0e06;
}
.heading {
  font-size: 11pt;
  font-weight: bold;
  letter-spacing: 0.14em;
  color: #2a1208;
  text-align: center;
  text-transform: uppercase;
  margin-bottom: 14px;
}
.rule { height: 1px; background: #8a6a3a; margin: 12px 0; }
.body-text { font-family: 'Garamond Libre', Crimson, 'Liberation Serif', serif; font-size: 10.5pt; line-height: 1.9; }
.translation { font-style: italic; color: #5a3a18; font-size: 10pt; }
.note { font-size: 9.5pt; color: #6a4a28; font-style: italic; margin-top: 14px; }
.bullet-list { margin-left: 1.1em; margin-top: 6px; }
.bullet-list li { margin-bottom: 7px; font-size: 10.5pt; line-height: 1.7; }
.encoded {
  font-family: 'Liberation Mono', 'DejaVu Sans Mono', monospace;
  font-size: 9pt;
  background: #e6d490;
  padding: 10px 12px;
  border-left: 3px solid #8a6a3a;
  word-break: break-all;
  line-height: 1.6;
  margin: 10px 0;
}
.plaintext { font-style: italic; color: #3a2008; font-size: 10pt; line-height: 1.8; margin: 10px 0; }
.sig { text-align: right; font-style: italic; margin-top: 14px; font-size: 10pt; }
.sub-heading { font-size: 10pt; font-weight: bold; color: #3a1a08; margin-top: 14px; margin-bottom: 4px; text-transform: uppercase; letter-spacing: 0.1em; }
.sub-heading-rule { height: 1px; background: #c0a060; margin: 10px 0 6px; }
.map-box {
  font-family: 'Liberation Mono', 'DejaVu Sans Mono', monospace;
  font-size: 9pt;
  line-height: 1.5;
  background: #e8d898;
  padding: 10px;
  border: 1px solid #8a6a3a;
  margin: 10px 0;
  color: #2a1a08;
}
.germanic {
  font-style: italic;
  font-size: 10pt;
  color: #3a2008;
  margin-top: 12px;
  text-align: center;
}
"""

BLOOD = """
body { background: #080606; }
.card {
  background: #181010;
  border: 2px solid #6b0000;
  outline: 4px solid #0a0606;
  outline-offset: 2px;
  border-radius: 4px;
  padding: 30px 34px;
  color: #e0c8b0;
}
.heading {
  font-size: 15pt;
  font-weight: bold;
  letter-spacing: 0.22em;
  color: #c00000;
  text-align: center;
  text-transform: uppercase;
  margin-bottom: 10px;
}
.subtitle {
  font-size: 10pt;
  font-style: italic;
  color: #907050;
  text-align: center;
  margin-bottom: 18px;
}
.rule { height: 1px; background: #6b0000; margin: 14px 0; }
.body-text { font-size: 10.5pt; line-height: 1.95; }
.bullet-list { margin-left: 1.1em; margin-top: 8px; }
.bullet-list li { margin-bottom: 9px; font-size: 10.5pt; line-height: 1.7; }
.exchange {
  font-size: 10pt;
  font-style: italic;
  color: #c00000;
  margin-top: 18px;
  padding-top: 14px;
  border-top: 1px solid #6b0000;
}
"""

# ---------------------------------------------------------------------------
# HTML wrapper
# ---------------------------------------------------------------------------

def page(theme_css, card_body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8">
<style>{PAGE}{theme_css}</style>
</head>
<body>
<div class="card">
{card_body}
</div>
</body>
</html>"""

# ---------------------------------------------------------------------------
# Handout content
# ---------------------------------------------------------------------------

HANDOUTS = [

    ("01_S1_scene1_legates_orders.pdf", WAX, """
<div class="heading">Mandatum Legati Marci Aurelii Corvini</div>
<div class="rule"></div>
<div class="body-text">
  Ad milites electos:<br><br>
  Descendite in ruinas.<br>
  Recuperate telum divinum.<br>
  Nemo tangat telum nisi ego permitto.
</div>
<div class="translation">
  To the chosen soldiers:<br>
  Descend into the ruins.<br>
  Recover the divine weapon.<br>
  No one shall touch the weapon unless I permit it.
</div>
<div class="rule"></div>
<div class="seal">In Nomine Senatus Populique Romani</div>
"""),

    ("02_S1_vault_inscription.pdf", STONE, """
<div class="heading">Ruinae Vindolandae — Altare Infimum</div>
<div class="rule"></div>
<div class="rune-row">TIWAZ &mdash; HAGALAZ &mdash; NAUDHIZ &mdash; ISA &mdash; OTHALAN</div>
<div class="rune-gloss">War &mdash; Disruption &mdash; Need &mdash; Stillness &mdash; Ancestral Land</div>
<div class="rule"></div>
<div class="body-text">
  Here lies the God-Killer, the Spear of Broken Oaths,
  sealed by the blood of heroes. May it never taste sunlight again.<br><br>
  Forged in vengeance. Quenched in divine blood.
  The son of Mars fell here. His father's wrath lingers still.
</div>
<div class="rule"></div>
<div class="warning">DO NOT WAKE WHAT SLEEPS HERE.</div>
"""),

    ("03_S1_opening_omens.pdf", PAPYRUS, """
<div class="heading">Auspicia Adversa &mdash; Cohortis XIV Legio</div>
<div class="rule"></div>
<div class="body-text">
  The following signs have been observed in the seven days preceding this report:
</div>
<ul class="bullet-list">
  <li>All camp dogs died at midnight on the third day. No visible cause.</li>
  <li>Sacrificial sheep presented black livers at both morning observations.</li>
  <li>Ravens observed flying reversed pattern over the <em>principia</em> on two occasions.</li>
  <li>Springs in the northeast sector run red (iron contamination suspected; source unknown).</li>
  <li>Night sentries report shadows without bodies moving along the east palisade.</li>
  <li>Legionaries on patrol report distant war-horns; no enemy force has been located.</li>
</ul>
<div class="rule"></div>
<div class="body-text">
  The augury is not favorable. I advise against major operations until expiation is performed.
</div>
<div class="sig"><em>Haruspex Gaius Paterculus,<br>in the consulship of Rufus and Quintillus</em></div>
"""),

    ("04_S2_tribunes_orders.pdf", WAX, """
<div class="heading">Senatus Populusque Romanus</div>
<div class="rule"></div>
<div class="body-text">
  By authority of the Senate and the consulship of Lucius Fulvius Rufus
  and Marcus Plautius Quintillus:<br><br>
  Tribune Lucius Valerius Maximus is hereby empowered to act in the
  Senate's name in all matters pertaining to the artifact recovered at
  Fort Vindolanda.<br><br>
  All military personnel are ordered to render full assistance.
  The Legate's command is suspended pending senatorial review.
</div>
<div class="rule"></div>
<div class="seal">In nomine Senatus Populique Romani</div>
"""),

    ("05_S2_encoded_letter.pdf", PAPYRUS, """
<div class="heading">Epistula Privata — Obsignata</div>
<div class="rule"></div>
<div class="body-text"><strong>Encoded text:</strong></div>
<div class="encoded">Cqn arcrxvpe expde: Aqr xqrjxbqe jcbq. Dkb jcbq xrrno Kbc. Dkb jcbq eba Kbe kbbi ecba kbi. Ebo jcbq. Ebo rea ebo. M.J.E.</div>
<div class="body-text"><strong>Plaintext (Caesar cipher, shift 3):</strong></div>
<div class="plaintext">
  The artifact must not reach Rome. By any means necessary.
  Our mutual friend's ambitions depend on its permanent removal.
  You know what to do.
</div>
<div class="rule"></div>
<div class="sig">Signed: G.C.B.</div>
<div class="note">Found folded twice. The back reads, faintly: <em>shift 3</em>.</div>
"""),

    ("06_S3_thusneldas_map.pdf", PAPYRUS, """
<div class="heading">Mappa Thusneldae — Via ad Lucum Sacrum</div>
<div class="rule"></div>
<div class="body-text">
  The map is drawn on torn leather. The lines are uneven. Nothing is straight.
</div>
<div class="map-box">
     N
     |
  ~river~     ~river~
     |      /
     *ford* (== two parallel dashes)
      \\
   ~river~     [?]
                (smudge; a fourth river? erased?)

  [O O O O O O O] &lt;-- seven standing stones, ring
   (each bears a rune from the vault inscription)

      X
     /X\\          &lt;-- crossed spears
    / X \\
  [ GROVE ]
</div>
<div class="germanic">
  <em>Mannaz raidho wunjo</em><br>
  Man. Journey. Joy.<br>
  <em>"The man who makes this journey finds what he seeks."</em>
</div>
<div class="note">
  The fourth river is missing or hidden. Thusnelda did not mark it.
  The warning over the grove is not decorative.
</div>
"""),

    ("07_S3_bloody_message.pdf", PAPYRUS, """
<div class="heading" style="font-size:16pt; letter-spacing:0.25em; color:#3a1010;">MARS VIDET OMNIA</div>
<div class="body-text translation" style="text-align:center; margin-bottom:18px;"><em>Mars sees all.</em></div>
<div class="rule" style="background:#5a3a18;"></div>
<div class="body-text" style="font-size:9.5pt; color:#5a3a28; font-style:italic; letter-spacing:0.05em;">
  The first line is cut clean, deliberate. Each letter the same depth.
  Someone knew exactly what they were writing.<br><br>
  Below it, scratched in a shaking hand, as if the arm fought itself:
</div>
<div class="rule" style="background:#5a3a18;"></div>
<div class="body-text" style="font-size:11pt; font-style:italic; color:#2a1208;">
  I did not want to do this.
</div>
"""),

    ("08_S4_raven_order.pdf", WAX, """
<div class="heading">Mandata G. Cassii Bruti</div>
<div class="rule"></div>
<div class="body-text"><em>To our friends within Vindolanda:</em></div>
<ul class="bullet-list">
  <li>Burn the granary before dusk.</li>
  <li>Kill the augur if opportunity presents.</li>
  <li>If the spear moves, collapse the stair.</li>
  <li>Leave no witnesses; the frontier must fall quiet.</li>
</ul>
<div class="rule"></div>
<div class="seal">G.C.B.</div>
<div class="translation" style="font-size:9pt; margin-top:10px;">
  Delivered by raven. Narrow strip of parchment. Black thread.
  Ink hurried; soot smear on the lower edge.
</div>
"""),

    ("09_S4_siege_orders.pdf", WAX, """
<div class="heading">Fort Vindolanda &mdash; Siege Day Orders</div>
<div class="body-text"><em>Issued by Centurion Varro, verified by Cassia.</em></div>
<div class="rule"></div>

<div class="sub-heading">Trumpet Codes</div>
<ul class="bullet-list">
  <li>Two short: fire in the <em>vicus</em></li>
  <li>Long + short: gate breach</li>
  <li>Six rapid: shrine summons (Mars' demand)</li>
</ul>

<div class="sub-heading">Watch Rotations</div>
<ul class="bullet-list">
  <li>North wall: Contubernia I&ndash;III (veterans)</li>
  <li>South gate: Auxiliaries under Optio Felicitus</li>
  <li>Workshop cordon: Faber squad, on alert for saboteurs</li>
</ul>

<div class="sub-heading">Escort Route</div>
<div class="body-text" style="margin-top:6px; font-style:italic;">
  Principia &rarr; Hidden stair &rarr; Sunken armory &rarr; Choking hall &rarr; Elder stair
</div>

<div class="sub-heading">Resource Status</div>
<ul class="bullet-list">
  <li>Grain: 9 days if rations hold, 6 if granary burns</li>
  <li>Water: contaminated at north gate well (boil)</li>
  <li>Civilians sheltered in <em>vicus</em> shrine (Mercury)</li>
</ul>

<div class="sub-heading">Notes</div>
<ul class="bullet-list">
  <li>Three volunteers must kneel when the stair opens. Cassia requires witnesses.</li>
  <li>Vercingetorix's runners offer diversion at south ditch at dusk.</li>
  <li>Tribune Lucius requests to accompany escort (motive unclear).</li>
</ul>
"""),

    ("10_S5_mark_of_mars.pdf", BLOOD, """
<div class="heading">The Mark of Mars</div>
<div class="subtitle">This character has stood before a god of war and lived.</div>
<div class="rule"></div>
<div class="body-text">For the remainder of their days:</div>
<ul class="bullet-list">
  <li>Advantage on Intimidation checks.<br>
    <em style="font-size:9.5pt; color:#907050;">Other soldiers see something in them they cannot name.</em>
  </li>
  <li>Once per long rest: ask the DM "What does Mars want from this situation?"
    and receive an honest answer.</li>
</ul>
<div class="exchange">
  In exchange: Mars may call on them. Once. At his choosing.
</div>
"""),

    ("12_S1_entry_passage_othalan_token.pdf", STONE, """
<div class="heading">Object Found — Entry Passage</div>
<div class="rule"></div>
<div class="body-text">
  A thumb-sized tile carved from pale bone. One face is smooth.
  The other bears a single rune, cut deep and deliberate:
</div>
<div class="rune-row" style="font-size:28pt; margin: 18px 0; letter-spacing:0.4em;">&#x16DF;</div>
<div class="rune-gloss">The carving is old. The edges are worn from handling.</div>
<div class="rule"></div>
<div class="body-text">
  An iron pin runs through a hole bored at the top, as if it was meant
  to be worn or carried close. The pin is cold despite the ambient heat
  of the torches.
</div>
"""),

    ("13_S1_shield_hall_rune_sketch.pdf", PAPYRUS, """
<div class="heading">Field Sketch — Shield Hall</div>
<div class="rule"></div>
<div class="body-text">
  The shields on the racks are old. Legion issue, or close to it.
  Most carry damage marks and old repairs. But on the iron boss
  of each shield, someone has cut a symbol.
</div>
<div class="rule"></div>
<div class="body-text">Five symbols repeat across all fifteen shields:</div>
<div class="map-box" style="text-align:center; font-size:18pt; letter-spacing:0.5em; padding:16px;">
  &#x16CF; &nbsp; &#x16BA; &nbsp; &#x16BE; &nbsp; &#x16C1; &nbsp; &#x16DF;
</div>
<div class="body-text">
  Three shields show the first symbol.<br>
  Three show the second. Three the third.<br>
  Three the fourth. Three the last.<br><br>
  The symbols are not Latin.
</div>
<div class="note">
  [Field note, charcoal on scrap leather. Not a formal document.]
</div>
"""),

    ("14_S1_shield_hall_reversed_shield.pdf", PAPYRUS, """
<div class="heading">Discovery — Shield Hall, Far Archway</div>
<div class="rule"></div>
<div class="body-text">
  There is a slight wrongness in the wall to the left of the archway.
</div>
<div class="rule"></div>
<div class="body-text">
  Not a gap. The stones are continuous. But one shield has been hung
  with its face to the wall rather than facing the room.<br><br>
  Every other shield in the Shield Hall faces outward. This one faces
  in, its boss pressed against the stone. It has been placed that way
  deliberately. The leather grip is still intact. Someone put it here
  and left it.<br><br>
  <em>Reaching behind the shield: the stone gives slightly.
  It is not load-bearing. It is a panel.</em>
</div>
<div class="rule"></div>
<div class="note">
  What is inside the alcove is described when the panel is opened.
</div>
"""),

]

# ---------------------------------------------------------------------------
# Generate
# ---------------------------------------------------------------------------

def main():
    ok = 0
    for filename, theme, body in HANDOUTS:
        out_path = os.path.join(OUT, filename)
        html_str = page(theme, body)
        try:
            HTML(string=html_str, base_url=OUT).write_pdf(out_path)
            # Convert PDF → PNG (150 DPI, single page)
            png_base = out_path.replace(".pdf", "")
            subprocess.run(
                ["pdftoppm", "-r", "150", "-png", "-singlefile", out_path, png_base],
                check=True, capture_output=True,
            )
            print(f"  OK  {filename}  →  {os.path.basename(png_base)}.png")
            ok += 1
        except Exception as exc:
            print(f"  ERR {filename}: {exc}", file=sys.stderr)
    print(f"\n{ok}/{len(HANDOUTS)} handouts generated in {OUT}/")

if __name__ == "__main__":
    main()
