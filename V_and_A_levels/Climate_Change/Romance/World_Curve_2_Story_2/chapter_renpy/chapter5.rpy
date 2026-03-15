label chapter5:

    # [Scene: The Arbor | Late Afternoon — Storm Gathering]

    scene bg ch5_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Rapid percussion undercut with a low, humming synth — taut and urgent]
    # play sound "sfx_placeholder"  # [Sound: The distant roar of surf; a police siren far-off; paper rustling]
    "You stand beneath the greenhouse glass and feel the sky press down like a fist. The decision you made in the council—people-first, now—still tastes of copper on your tongue. That choice pulsed through the town like an exposed wire; now the wire sparks."
    "The Arbor smells like damp soil and heated metal. It smells like toes on wet planks and the faint, stubborn sweetness of tomatoes someone refuses to let go of. Your fingers are cold where they grip"
    "the damp leather of your notebook; water beads on the page as if the weather itself is annotating your thoughts."
    "Elias 'Eli' Rowan is at the central bench, sleeves rolled, hands already starting to sketch angles on a scrap of corrugated plastic. His breaths come in quick pulls; he has the look you know well when the solution lives in his palms—half exhilaration, half accusation."

    "Elias 'Eli' Rowan" "We can bolt them tonight. Modular sections, weight down with sandbags, stagger the line to slow the swell. I know—I've been tinkering on the model—"
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "Tess said Livia's lawyers filed notices this morning. The council hall is full of cameras, Eli. They're watching for anything they can call illegal."
    "Elias 'Eli' Rowan rubs his temple, then laughs too quickly, a sound that wants to be brave and ends up brittle."

    "Elias 'Eli' Rowan" "Legal notices don't stop water. They stop people who are afraid of paperwork. We can't sit and wait for them to decide who gets wet."
    "You study his hands—the knuckles white where he presses the pen to mark a seam. There's a bruise blooming on the side of his thumb from a wrench he didn't realise he'd been tightening. You think"
    "of the past project he keeps away from the light and the way that history tightens around him like a string of knots."
    "Dr. Naomi Park stands with a tablet balanced on her hip, numbers scrolling in small, furious columns. Her face is pinched with the kind of worry that used to live in lecture halls, not greenhouses."
    show dr_naomi_park at right:
        zoom 0.7

    dr_naomi_park "A phased pilot reduces ecological risk and gives us data to defend ourselves in court. You can't make a legal case out of good intentions; you make it out of measured outcomes."
    "Rafi is propped against a potting table, salt in his beard, a map unfurled between his knees. He taps a finger on a line that traces the ruined boardwalk like a scar."
    show rafi_gmez at center:
        zoom 0.7

    rafi_gmez "Visibility matters. People need to see action. If we put something small out there and the town sees it hold—hell, they might rally. They might stand. We can't be forever translating charts."
    "Grandma Hira sits on an overturned crate, shawl pulled close, eyes like smoothed pebbles that have seen a dozen tides. She speaks with the slow certainty of someone reading a tide you've never measured."
    hide mara_kestrel
    show grandma_hira at left:
        zoom 0.7

    grandma_hira "When my street went under, we watched planks float like driftwood. I remember calling names until my voice cracked. We had no plan. If you lead people into the water without telling them where the ropes are, they drown trying to save something they can't hold."
    "Tess comes in on a breathless run, rain beading her short hair. Her fluorescent lanyard is limp, her hands shaking. Tess's face is an open worry; she has the look of someone carrying too much truth."

    "Tess O'Malley" "I got the dump. Covenants. Side letters. Livia's investors tie development to clauses that strip protections—land swaps, tax forgiveness—it's ugly. I can leak it. But if they tie the leak back to me—"
    hide dr_naomi_park
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "They'll come for you, Tess. They'll label you a traitor. They could lock you out of council roles, ruin your career."

    "Tess O'Malley" "Maybe. Maybe they'll also make people look at Livia in a way they haven't yet. Maybe the cameras will turn from the seawall to the contracts."
    "The air tightens. Somewhere beyond the greenhouse the town hums like a living thing being poked with a stick; cameras blink on and off like insect eyes. You can feel Livia's presence as surely as the salt on the air—her legal notices a thin paper net cast over the harbor."
    hide rafi_gmez
    hide grandma_hira
    hide mara_kestrel

    scene bg ch5_4001e7_2 at full_bg
    "You replay the models in your head—the way a half-meter change raises a child's bedroom into a current—and your mouth goes dry. The scientist in you enumerates uncertainties the way a weathered sailor names shoals: unknown"
    "substrate, shifting silt, estuary backflows. The activist in you hears Rafi and hears Grandma Hira and hears the children who sleep on cots in the community hall."
    "Your heart knots in a cold, taut loop. This is not a theoretical exercise anymore. The choice is a live wire. Whoever acts first owns the narrative: hero, villain, or cautionary tale."

    menu:
        "Place your palm on the modular prototype and steady Eli's design":
            "Your hand finds the cool metal; Elias 'Eli' Rowan's shoulders loosen an inch. He looks at you the way someone looking for permission looks—relieved and raw. The bench smells of oil and new cut timber."
        "Step back and re-run the simulations with Naomi":
            "You pull your notebook back under the lamp. The screen's glow makes small ghosts on your fingers. Naomi's eyes sharpen—she appreciates the pause, but her jaw is tight with impatience."
        "Ask Tess for the files now—push the leak forward":
            "Tess's fingers hover over her phone. You see fear and a fierce spark. She nods, quick and certain, but you can almost see the consequences forming around her like a net."

    menu:
        "Promise Eli you'll help him build—start tonight":
            "Elias 'Eli' Rowan's face opens; for a breath the world narrows to the two of you and the hum of tools. He reaches for you as if to anchor his plan in your certainty. The greenhouse lights flare; the smell of wet timber sharpens."
        "Ask Naomi to draft a minimal monitoring protocol you can deploy quickly":
            "Naomi nods, relieved. She moves to her tablet with a briskness that looks like hope rearranged into action. Numbers begin to march across the screen like soldiers mustered."

    menu:
        "Tell Eli you'll stand with him on the planks if it comes to it":
            "Elias 'Eli' Rowan closes his eyes as if to memorize the promise. For an unsteady second you hear only the wind; then his hand finds yours, warm and callused. The tide hisses like an audience."
        "Tell Tess to upload but demand she anonymize the source":
            "Tess stammers a 'Yes'—fear and steadiness battling in her features. She tells you she can mask the transfer, but her fingers betray the truth: trust will cost her something."
        "Demand a short, risky build with Naomi's quick-monitor template—compromise":
            "Naomi nods, teeth bared against the stress. She immediately starts listing parameters—anchor depths, sensor placements, emergency pullback triggers. The language of compromise sounds like hope dressed in caution."

    menu:
        "We build unauthorized modular breakwaters now.":
            jump chapter6
        "We stage an occupation of the flooded promenade and demand concessions.":
            jump chapter14
        "We use Tess’s back-channel to expose council covenants and seek negotiated protections.":
            jump chapter15
    return
