#!/usr/bin/env python3
"""
Canonical stat blocks for the final two sessions (Session 6 = Chapter 4 pack,
Session 7 = Chapter 5 pack). Single source of truth: the print modules and the
stand-alone stat-block sheet are generated from the data below.

Outputs:
  gm_tools/final_statblocks.html            stand-alone A4 sheet, every creature
  gm_tools/chapter04_print.html             <!-- statblock:Key --> ... <!-- /statblock --> regions refreshed
  gm_tools/chapter05_print.html             same

Usage:
  python3 scripts/build_final_statblocks.py
"""
import html
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
GM = BASE / "gm_tools"


def mod(score):
    m = (score - 10) // 2
    return f"+{m}" if m >= 0 else str(m)


# name, type line, AC, HP, speed, abilities, extras(list of (label, text)), traits, actions,
# bonus, reactions, legendary, gm note, session tag
SB = {}


def add(key, **kw):
    SB[key] = kw


# ─────────────────────────── SESSION 6 ───────────────────────────
add("Thusnelda", name="Thusnelda, Völva of the Village", session=6,
    type="Medium humanoid (Germanic), neutral good", ac="12 (hide)", hp="27 (6d8)", speed="30 ft.",
    ab=(10, 14, 11, 13, 16, 14),
    extra=[("Skills", "Insight +5, Medicine +5, Perception +5, Religion +3"),
           ("Senses", "passive Perception 15"), ("Languages", "Germanic, broken Latin"),
           ("Challenge", "1 (200 XP)")],
    traits=[("Völva", "Thusnelda can cast <em>guidance</em> at will, <em>speak with animals</em> and <em>augury</em> 1/day each (Wis, DC 13)."),
            ("Cunning Action", "Dash, Disengage or Hide as a bonus action.")],
    actions=[("Ritual Knife", "<em>Melee Weapon Attack:</em> +4 to hit, reach 5 ft., one target. <em>Hit:</em> 5 (1d6+2) piercing."),
             ("Shortbow", "<em>Ranged Weapon Attack:</em> +4 to hit, range 80/320 ft. <em>Hit:</em> 5 (1d6+2) piercing.")],
    note="He will not fight the party unless they threaten the village. If restrained, he does not struggle after round 1.")

add("Myling", name="The Myling (\"Wulf\")", session=6,
    type="Small undead, neutral", ac="11", hp="13 (3d6+3)", speed="0 ft., fly 40 ft. (hover)",
    ab=(7, 13, 10, 7, 10, 14),
    extra=[("Skills", "Stealth +3"), ("Damage Resistances", "bludgeoning, piercing, slashing from nonmagical attacks"),
           ("Damage Immunities", "cold, poison"), ("Condition Immunities", "exhaustion, grappled, poisoned"),
           ("Senses", "darkvision 60 ft., passive Perception 10"), ("Languages", "Germanic (a child's)"),
           ("Challenge", "1/2 (100 XP)")],
    traits=[("Incorporeal Movement", "Moves through creatures and objects; 1d10 force if it ends its turn inside an object."),
            ("Tragic Compulsion", "Must be carried. While carried he weighs more each hour (Str DC 10 per hour or 1 exhaustion; carrier changes reset it). Laid beside his own bones at the old altar in the Sacred Grove (north of the village), he rests.")],
    actions=[("Bone-Chill Touch", "<em>Melee Spell Attack:</em> +3 to hit, reach 5 ft. <em>Hit:</em> 4 (1d8) cold; DC 11 Con or speed -10 ft. until end of its next turn."),
             ("Wail of the Lost (Recharge 5-6)", "Each creature within 30 ft.: DC 12 Wis save, 10 (3d6) psychic and frightened until end of its next turn; half and not frightened on a success. Wakes dormant undead within 300 ft.")],
    note="Only hostile if abandoned or refused. Reward for laying him to rest: <strong>Myling's Rest</strong> for the carrier (advantage on death saves, immune to frightened) until the end of Session 7.")

add("BoneNaga", name="Bone Naga", session=6,
    type="Large undead, lawful evil", ac="15 (natural armor)", hp="58 (9d10+9)", speed="30 ft.",
    ab=(15, 16, 12, 15, 15, 16),
    extra=[("Damage Immunities", "poison"), ("Condition Immunities", "charmed, exhaustion, paralyzed, poisoned"),
           ("Senses", "darkvision 60 ft., passive Perception 12"), ("Languages", "Germanic"), ("Challenge", "4 (1,100 XP)")],
    traits=[("Spellcasting", "Int-based, spell save DC 12, +4 to hit. Cantrips: <em>mage hand, minor illusion, ray of frost</em>. 1st (4 slots): <em>charm person, sleep</em>. 2nd (2 slots): <em>detect thoughts, hold person</em>. 3rd (1 slot): <em>lightning bolt</em> (8d6, DC 12 Dex half).")],
    actions=[("Bite", "<em>Melee Weapon Attack:</em> +5 to hit, reach 10 ft., one creature. <em>Hit:</em> 6 (1d6+3) piercing plus 10 (3d6) poison.")],
    note="Monster Manual block. Not vulnerable to bludgeoning (only the skeletons are). No rejuvenation: the chieftains bound them, not a lich. Round 1: <em>hold person</em> on whoever leads down the stair; <em>lightning bolt</em> once when 3+ PCs bunch on it, and let them see it coming.")

add("Skeleton", name="Skeleton", session=6,
    type="Medium undead, lawful evil", ac="13 (armor scraps)", hp="13 (2d8+4)", speed="30 ft.",
    ab=(10, 14, 15, 6, 8, 5),
    extra=[("Damage Vulnerabilities", "bludgeoning"), ("Damage Immunities", "poison"),
           ("Condition Immunities", "exhaustion, poisoned"), ("Senses", "darkvision 60 ft., passive Perception 9"),
           ("Languages", "understands the languages it knew in life but can't speak"), ("Challenge", "1/4 (50 XP)")],
    traits=[],
    actions=[("Shortsword", "<em>Melee Weapon Attack:</em> +4 to hit, reach 5 ft. <em>Hit:</em> 5 (1d6+2) piercing."),
             ("Shortbow", "<em>Ranged Weapon Attack:</em> +4 to hit, range 80/320 ft. <em>Hit:</em> 5 (1d6+2) piercing.")])

add("Yochlol", name="Yochlol, Gestating (campaign variant)", session=6,
    type="Medium fiend (demon, shapechanger), chaotic evil", ac="15 (natural armor)",
    hp="68 while gestating (full 136, 16d8+64)", speed="0 ft. while rooted; 30 ft., climb 30 ft. once hatched",
    ab=(15, 14, 18, 13, 15, 15),
    extra=[("Saving Throws", "Dex +6, Int +5, Wis +6, Cha +6"), ("Skills", "Deception +10, Insight +6"),
           ("Damage Resistances", "cold, fire, lightning; bludgeoning, piercing, slashing from nonmagical attacks"),
           ("Damage Immunities", "poison"), ("Condition Immunities", "poisoned"),
           ("Senses", "darkvision 120 ft., passive Perception 12"), ("Languages", "Abyssal, telepathy 60 ft."),
           ("Challenge", "10 (5,900 XP) full; treat as CR 6 while rooted")],
    traits=[("Gestating", "Rooted in the blood-growth pillar: speed 0, reach 10 ft., no Mist Form, no Change Shape. At the start of round 4, if the pillar still stands, it tears free: gains 40 HP, speed 30 ft., Mist Form."),
            ("The Pillar", "AC 10, 30 HP, vulnerable to fire and radiant. Destroying it before round 4 halves the yochlol's current HP and it can never hatch."),
            ("Magic Resistance", "Advantage on saves against spells and other magical effects."),
            ("Spider Climb / Web Walker", "Once hatched, climbs anything and ignores webs.")],
    actions=[("Multiattack", "Two Slam attacks."),
             ("Slam", "<em>Melee Weapon Attack:</em> +6 to hit, reach 10 ft. while rooted, one target. <em>Hit:</em> 5 (1d6+2) bludgeoning plus 21 (6d6) poison."),
             ("Web (at will, innate, DC 14)", "As the spell. Fills the room's doorway on round 1."),
             ("Mist Form (hatched only)", "Becomes toxic mist; creatures that enter its space: DC 14 Con or poisoned until end of next turn.")],
    note="The room is a pressure cooker, not a slugfest: three rounds to burn the pillar. Point at the fire in the brazier stands outside the door.")

add("Dretch", name="Dretch", session=6,
    type="Small fiend (demon), chaotic evil", ac="11 (natural armor)", hp="18 (4d6+4)", speed="20 ft.",
    ab=(11, 11, 12, 5, 8, 3),
    extra=[("Damage Resistances", "cold, fire, lightning"), ("Damage Immunities", "poison"), ("Condition Immunities", "poisoned"),
           ("Senses", "darkvision 60 ft., passive Perception 9"), ("Languages", "Abyssal, telepathy 60 ft. (works only with Abyssal speakers)"),
           ("Challenge", "1/4 (50 XP)")],
    traits=[],
    actions=[("Multiattack", "One Bite and one Claws."),
             ("Bite", "<em>Melee Weapon Attack:</em> +2 to hit, reach 5 ft. <em>Hit:</em> 3 (1d6) piercing."),
             ("Claws", "<em>Melee Weapon Attack:</em> +2 to hit, reach 5 ft. <em>Hit:</em> 5 (2d4) slashing."),
             ("Fetid Cloud (1/day)", "10-ft. radius of disgusting green gas for 1 minute. Each creature starting its turn there: DC 11 Con or poisoned until start of its next turn; while poisoned, action or bonus action (not both), no reactions.")])

add("ShadowDemon", name="Shadow Demon", session=6,
    type="Medium fiend (demon), chaotic evil", ac="13", hp="66 (12d8+12)", speed="30 ft., fly 30 ft.",
    ab=(1, 17, 12, 14, 13, 14),
    extra=[("Saving Throws", "Dex +5, Cha +4"), ("Skills", "Stealth +7"), ("Damage Vulnerabilities", "radiant"),
           ("Damage Resistances", "acid, fire, necrotic, thunder; bludgeoning, piercing, slashing from nonmagical attacks"),
           ("Damage Immunities", "cold, lightning, poison"),
           ("Condition Immunities", "exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained"),
           ("Senses", "darkvision 120 ft., passive Perception 11"), ("Languages", "Abyssal, telepathy 120 ft."), ("Challenge", "4 (1,100 XP)")],
    traits=[("Incorporeal Movement", "Moves through creatures and objects; 5 (1d10) force if it ends its turn inside an object."),
            ("Light Sensitivity", "In bright light: disadvantage on attack rolls and on sight-based Perception."),
            ("Shadow Stealth", "In dim light or darkness, Hide as a bonus action.")],
    actions=[("Claws", "<em>Melee Weapon Attack:</em> +5 to hit, reach 5 ft. <em>Hit:</em> 10 (2d6+3) psychic, or 17 (4d6+3) psychic if it had advantage.")],
    note="The Sun-Path brazier puzzle (Scene 8) turns the whole room to bright light: Light Sensitivity on, Shadow Stealth off.")

add("Wraith", name="Wraith (Chieftain Spirit)", session=6,
    type="Medium undead, neutral evil", ac="13", hp="67 (9d8+27)", speed="0 ft., fly 60 ft. (hover)",
    ab=(6, 16, 16, 12, 14, 15),
    extra=[("Damage Resistances", "acid, cold, fire, lightning, thunder; bludgeoning, piercing, slashing from nonmagical attacks that aren't silvered"),
           ("Damage Immunities", "necrotic, poison"),
           ("Condition Immunities", "charmed, exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained"),
           ("Senses", "darkvision 60 ft., passive Perception 12"), ("Languages", "Germanic"), ("Challenge", "5 (1,800 XP)")],
    traits=[("Incorporeal Movement", "Moves through creatures and objects; 5 (1d10) force if it ends its turn inside an object."),
            ("Sunlight Sensitivity", "In sunlight: disadvantage on attack rolls and sight-based Perception.")],
    actions=[("Life Drain", "<em>Melee Weapon Attack:</em> +6 to hit, reach 5 ft. <em>Hit:</em> 21 (4d8+3) necrotic; DC 14 Con or max HP reduced by the damage taken until a long rest. Dies if max HP hits 0."),
             ("Create Specter", "Targets a humanoid within 10 ft. that died violently in the last minute; it rises as a specter under the wraith's control.")])

add("Glabrezu", name="Glabrezu (Core Guardian)", session=6,
    type="Large fiend (demon), chaotic evil", ac="17 (natural armor)", hp="157 (15d10+75)", speed="40 ft.",
    ab=(20, 15, 21, 19, 17, 16),
    extra=[("Saving Throws", "Str +9, Con +9, Wis +7, Cha +7"),
           ("Damage Resistances", "cold, fire, lightning; bludgeoning, piercing, slashing from nonmagical attacks"),
           ("Damage Immunities", "poison"), ("Condition Immunities", "poisoned"),
           ("Senses", "truesight 120 ft., passive Perception 13"), ("Languages", "Abyssal, Latin (learned for the bargain), telepathy 120 ft."),
           ("Challenge", "9 (5,000 XP)")],
    traits=[("Innate Spellcasting", "Int, DC 16. At will: <em>darkness, detect magic, dispel magic</em>. 1/day each: <em>confusion, fly, power word stun</em>."),
            ("Magic Resistance", "Advantage on saves against spells and other magical effects.")],
    actions=[("Multiattack", "Two Pincers and two Fists, or two Pincers and one spell."),
             ("Pincer", "<em>Melee Weapon Attack:</em> +9 to hit, reach 10 ft. <em>Hit:</em> 16 (2d10+5) bludgeoning; Medium or smaller target grappled (escape DC 15). Two pincers, each can hold one target."),
             ("Fist", "<em>Melee Weapon Attack:</em> +9 to hit, reach 5 ft. <em>Hit:</em> 7 (2d4+2) bludgeoning.")],
    note="Do not open with <em>power word stun</em>. Save it for the PC who refuses the bargain loudest. It offers the bargain first (see Scene 9).")

# ─────────────────────────── SESSION 7 ───────────────────────────
add("Zombie", name="Zombie", session=7,
    type="Medium undead, neutral evil", ac="8", hp="22 (3d8+9)", speed="20 ft.",
    ab=(13, 6, 16, 3, 6, 5),
    extra=[("Saving Throws", "Wis +0"), ("Damage Immunities", "poison"), ("Condition Immunities", "poisoned"),
           ("Senses", "darkvision 60 ft., passive Perception 8"), ("Languages", "understands what it knew in life, can't speak"),
           ("Challenge", "1/4 (50 XP)")],
    traits=[("Undead Fortitude", "If damage reduces it to 0 HP, Con save DC 5 + damage taken; on a success it drops to 1 HP instead. Not vs radiant damage or critical hits.")],
    actions=[("Slam", "<em>Melee Weapon Attack:</em> +3 to hit, reach 5 ft. <em>Hit:</em> 4 (1d6+1) bludgeoning.")])

add("Wight", name="Wight", session=7,
    type="Medium undead, neutral evil", ac="14 (studded leather)", hp="45 (6d8+18)", speed="30 ft.",
    ab=(15, 14, 16, 10, 13, 15),
    extra=[("Skills", "Perception +3, Stealth +4"),
           ("Damage Resistances", "necrotic; bludgeoning, piercing, slashing from nonmagical attacks that aren't silvered"),
           ("Damage Immunities", "poison"), ("Condition Immunities", "exhaustion, poisoned"),
           ("Senses", "darkvision 60 ft., passive Perception 13"), ("Languages", "Latin, Germanic"), ("Challenge", "3 (700 XP)")],
    traits=[("Sunlight Sensitivity", "In sunlight: disadvantage on attack rolls and sight-based Perception.")],
    actions=[("Multiattack", "Two Longsword or two Longbow attacks; Life Drain can replace one Longsword."),
             ("Life Drain", "<em>Melee Weapon Attack:</em> +4 to hit, reach 5 ft. <em>Hit:</em> 5 (1d6+2) necrotic; DC 13 Con or max HP reduced by that amount until a long rest."),
             ("Longsword", "<em>Melee Weapon Attack:</em> +4 to hit, reach 5 ft. <em>Hit:</em> 6 (1d8+2) slashing, or 7 (1d10+2) two-handed."),
             ("Longbow", "<em>Ranged Weapon Attack:</em> +4 to hit, range 150/600 ft. <em>Hit:</em> 6 (1d8+2) piercing.")])

add("Specter", name="Specter", session=7,
    type="Medium undead, chaotic evil", ac="12", hp="22 (5d8)", speed="0 ft., fly 50 ft. (hover)",
    ab=(1, 14, 11, 10, 10, 11),
    extra=[("Damage Resistances", "acid, cold, fire, lightning, thunder; bludgeoning, piercing, slashing from nonmagical attacks"),
           ("Damage Immunities", "necrotic, poison"),
           ("Condition Immunities", "charmed, exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained, unconscious"),
           ("Senses", "darkvision 60 ft., passive Perception 10"), ("Languages", "understands what it knew in life, can't speak"),
           ("Challenge", "1 (200 XP)")],
    traits=[("Incorporeal Movement", "Moves through creatures and objects; 5 (1d10) force if it ends its turn inside an object."),
            ("Sunlight Sensitivity", "In sunlight: disadvantage on attack rolls and sight-based Perception.")],
    actions=[("Life Drain", "<em>Melee Spell Attack:</em> +4 to hit, reach 5 ft. <em>Hit:</em> 10 (3d6) necrotic; DC 10 Con or max HP reduced by that amount until a long rest.")])

add("Vercingetorix", name="Vercingetorix, Bound", session=7,
    type="Medium undead, neutral", ac="18 (Gallic mail, shield)", hp="150 (20d8+60)", speed="30 ft.",
    ab=(20, 12, 16, 14, 14, 18),
    extra=[("Saving Throws", "Str +9, Con +7, Wis +6"), ("Skills", "Athletics +9, Intimidation +8, Perception +6"),
           ("Damage Resistances", "necrotic; bludgeoning, piercing, slashing from nonmagical attacks"),
           ("Damage Immunities", "poison"), ("Condition Immunities", "exhaustion, frightened, poisoned"),
           ("Senses", "darkvision 60 ft., passive Perception 16"), ("Languages", "Gaulish, Latin"), ("Challenge", "11 (7,200 XP)")],
    traits=[("Relentless (1/day)", "When reduced to 0 HP, he drops to 1 HP instead, unless the damage was radiant or dealt by a weapon consecrated at the Belatucadrus shrine (or the ram's-eye blade from the Sunken Armory). Say it: <em>\"He should be dead. He isn't.\"</em>"),
            ("Aura of the Unfinished War", "Undead allies within 30 ft. deal +2 damage with melee attacks."),
            ("Bound", "He cannot leave the Convergence Hall. Two hundred years of trying.")],
    actions=[("Multiattack", "Three Dread Spatha attacks."),
             ("Dread Spatha", "<em>Melee Weapon Attack:</em> +9 to hit, reach 5 ft. <em>Hit:</em> 9 (1d8+5) slashing plus 9 (2d8) necrotic."),
             ("Fear Aura (Recharge 5-6)", "Each creature within 30 ft. that can see him: DC 15 Wis or frightened for 1 minute (repeat save each turn end)."),
             ("Command the Fallen (1/day)", "1d4 skeletons claw up from the floor and act on his initiative.")],
    reactions=[("Parry", "+4 AC against one melee attack that would hit him.")],
    note="<strong>Champion's Duel:</strong> if a PC (Ursula is the natural one) formally challenges him, he holds his skeletons back and fights one-on-one with honour. <strong>Final Death:</strong> 1 lucid minute, three true answers, then the unmaking secret (see Scene 3).")

add("Mars", name="Mars, Diminished Avatar", session=7,
    type="Large celestial (god of war), lawful neutral", ac="22 (divine panoply); 16 once the altar chains are locked",
    hp="300 (24d10+168)", speed="40 ft. (cannot leave the Antechamber)",
    ab=(28, 16, 24, 18, 20, 22),
    extra=[("Saving Throws", "Str +16, Con +14, Wis +12, Cha +13"), ("Skills", "Intimidation +13, Perception +12"),
           ("Damage Resistances", "bludgeoning, piercing, slashing from nonmagical attacks"),
           ("Damage Immunities", "fire, poison"), ("Condition Immunities", "charmed, exhaustion, frightened, paralyzed, poisoned"),
           ("Senses", "truesight 120 ft., passive Perception 22"), ("Languages", "all"), ("Challenge", "20 (25,000 XP)")],
    traits=[("Legendary Resistance (3/day)", "Auto-succeeds on a failed save. <strong>Lost entirely once the altar chains are locked</strong> (Ritual Round 1)."),
            ("Anchored", "While the spear is in the Antechamber, Mars cannot be banished, teleported or moved against his will."),
            ("Not to Be Killed", "At 0 HP the avatar breaks apart and Mars cannot act for the rest of the encounter, but he is not destroyed and the spear is untouched. The choice still has to be made.")],
    actions=[("Multiattack", "Four Divine Pilum attacks. <strong>Two</strong> once the bloodline is severed (Ritual Round 2)."),
             ("Divine Pilum", "<em>Melee or Ranged Weapon Attack:</em> +10 to hit, reach 10 ft. or range 60 ft., one target. <em>Hit:</em> 12 (2d6+5) piercing plus 3 (1d6) radiant. The pilum returns to his hand."),
             ("War Cry (Recharge 5-6)", "Each creature within 30 ft. that can hear him: DC 18 Wis or frightened for 1 minute (repeat save each turn end).")],
    legendary=("Mars can take 3 legendary actions, one at a time, at the end of another creature's turn.",
               [("Pilum Strike", "One Divine Pilum attack."),
                ("Divine Presence", "One creature within 60 ft.: DC 18 Wis or frightened until the end of its next turn."),
                ("Divine Smite (costs 2)", "His next Pilum hit this round deals +13 (3d8) radiant. <strong>Unavailable once the bloodline is severed.</strong>"),
                ("Summon the Fallen (costs 2)", "One Shadow Demon steps out of the red light (max 2 at once).")]),
    note="He targets whoever is working the ritual, never a downed PC: he wants witnesses. He is cold and methodical, waiting to be impressed. Mars is genuinely Mars; never resolve him into an impostor.")


# ─────────────────────────── rendering ───────────────────────────
def render(key):
    s = SB[key]
    names = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
    scores = "".join(
        f'<div class="score"><span class="label">{n}</span>{v} ({mod(v)})</div>' for n, v in zip(names, s["ab"]))
    out = [f'<div class="stat-block" id="sb-{key}">',
           f'<div class="name">{html.escape(s["name"])}</div>',
           f'<div class="type">{s["type"]}</div>',
           f'<p><strong>Armor Class</strong> {s["ac"]}<br><strong>Hit Points</strong> {s["hp"]}<br><strong>Speed</strong> {s["speed"]}</p>',
           '<hr class="rule">', f'<div class="scores">{scores}</div>', '<hr class="rule">']
    out.append("<p>" + "<br>".join(f"<strong>{l}</strong> {t}" for l, t in s.get("extra", [])) + "</p>")
    out.append('<hr class="rule">')
    for l, t in s.get("traits", []):
        out.append(f"<p><strong><em>{l}.</em></strong> {t}</p>")
    if s.get("actions"):
        out.append('<h4>Actions</h4>')
        for l, t in s["actions"]:
            out.append(f"<p><strong><em>{l}.</em></strong> {t}</p>")
    if s.get("reactions"):
        out.append('<h4>Reactions</h4>')
        for l, t in s["reactions"]:
            out.append(f"<p><strong><em>{l}.</em></strong> {t}</p>")
    if s.get("legendary"):
        intro, items = s["legendary"]
        out.append('<h4>Legendary Actions</h4>')
        out.append(f"<p>{intro}</p>")
        for l, t in items:
            out.append(f"<p><strong>{l}.</strong> {t}</p>")
    if s.get("note"):
        out.append(f'<p class="gm-note"><strong>GM:</strong> {s["note"]}</p>')
    out.append("</div>")
    return "\n".join(out)


CSS = """
@import url('https://fonts.googleapis.com/css2?family=IM+Fell+English:ital@0;1&family=IM+Fell+English+SC&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
@page{size:A4;margin:14mm}
body{font-family:'IM Fell English',Georgia,serif;font-size:9pt;line-height:1.4;color:#1a1000;background:#fff;padding:10px}
h1{font-family:'IM Fell English SC',Georgia,serif;font-size:18pt;color:#5a1a00;border-bottom:2pt solid #8B4513;margin:0 0 6px;text-align:center}
h2{font-family:'IM Fell English SC',Georgia,serif;font-size:13pt;color:#5a1a00;border-bottom:1pt solid #c8b090;margin:10px 0 6px;column-span:all}
h4{font-size:9pt;font-variant:small-caps;color:#5a1a00;border-bottom:.5pt solid #c8b090;margin:4px 0 2px}
.columns{column-count:2;column-gap:6mm}
.stat-block{background:#fdf5e0;border:1pt solid #8B7355;border-top:2pt solid #8B4513;border-bottom:2pt solid #8B4513;padding:6px 8px;margin:0 0 6px;font-size:8.5pt;break-inside:avoid}
.stat-block .name{font-family:'IM Fell English SC',Georgia,serif;font-size:11pt;color:#5a1a00}
.stat-block .type{font-style:italic;font-size:8pt;color:#5a3a10;border-bottom:.5pt solid #c8b090;padding-bottom:3px;margin-bottom:4px}
.stat-block .scores{display:flex;gap:6px;margin:3px 0;font-size:8pt;flex-wrap:wrap}
.stat-block .score{text-align:center;min-width:34px}
.stat-block .score .label{font-weight:bold;font-size:7pt;color:#8B4513;display:block}
.stat-block .rule{border:none;border-top:.5pt solid #c8b090;margin:3px 0}
.stat-block p{margin-bottom:2px}
.gm-note{background:#fff0d0;border-left:2pt solid #c87800;padding:3px 5px;margin-top:3px}
.intro{column-span:all;font-style:italic;margin-bottom:6px;text-align:center}
@media screen and (max-width:700px){.columns{column-count:1}}
"""


def build_sheet():
    parts = ["<!DOCTYPE html>", '<html lang="en"><head><meta charset="UTF-8">',
             '<meta name="viewport" content="width=device-width, initial-scale=1">',
             "<title>Final Sessions Stat Blocks</title>", f"<style>{CSS}</style></head><body>",
             "<h1>The Shadow of Mars: Stat Blocks for the Final Two Sessions</h1>",
             '<p class="intro">Generated by scripts/build_final_statblocks.py. Matches the print modules and MapTool tokens. '
             'Session 6 = Chapter 4 pack (party Level 6). Session 7 = Chapter 5 pack (party Level 7).</p>',
             '<div class="columns">', "<h2>Session 6: The Village, the Grove and the Temple Below</h2>"]
    parts += [render(k) for k, v in SB.items() if v["session"] == 6]
    parts.append("<h2>Session 7: The Wrath of Mars</h2>")
    parts += [render(k) for k, v in SB.items() if v["session"] == 7]
    parts.append("</div></body></html>")
    (GM / "final_statblocks.html").write_text("\n".join(parts), encoding="utf-8")


MARK = re.compile(r"<!-- statblock:(\w+) -->.*?<!-- /statblock -->", re.S)


def inject(path):
    text = path.read_text(encoding="utf-8")
    missing = [k for k in MARK.findall(text) if k not in SB]
    if missing:
        raise SystemExit(f"{path.name}: unknown stat block keys {missing}")
    new = MARK.sub(lambda m: f"<!-- statblock:{m.group(1)} -->\n{render(m.group(1))}\n<!-- /statblock -->", text)
    path.write_text(new, encoding="utf-8")
    return len(MARK.findall(new))


if __name__ == "__main__":
    build_sheet()
    for f in ("chapter04_print.html", "chapter05_print.html"):
        p = GM / f
        if p.exists():
            print(f"{f}: {inject(p)} stat blocks refreshed")
    print(f"final_statblocks.html: {len(SB)} stat blocks")
