label chapter5:

    # [Scene: Tide Lab (Converted Research Ferry) | Morning — Post-Pilot]

    scene bg ch5_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Camera shutter echoes softly; distant gulls; the low hum of pumps and monitors]
    # play music "music_placeholder"  # [Music: Bright strings, steady and hopeful]
    "You stand at the lab bench with your notebook folded into the inner pocket of your jacket, the berm sketch a small, private compass against your ribs. The prints—Jonah's—catch the lab light and throw back a"
    "city you've been trying to name: the shore held, the salt-marsh ribs flexing, people on reclaimed walkways, seedlings catching sunlight."
    "You breathe in. The air smells of metal, coffee grounds, and the faint green of algae—an oddly comforting bouquet that says this place is alive and working."
    "Jonah Reyes leans across the bench; his shoulder brushes yours and it feels like a quiet confirmation. He points at a print where the berm curves gracefully around a flooded inlet, dotted by small clusters of planted sedge."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "That's the spread the feed picked up. They ran your quote with it—'Dignity in adaptation.' You gave them a line they couldn't ignore."
    show mara_ellis at right:
        zoom 0.7

    mara_ellis "Dignity? That sounds like something Maya would pin to a poster."

    jonah_reyes "Maya would pin it and add glitter. But it's true. People respond to that word."
    "You study the prints again. Momentum is visible in pixels and headlines, but you feel it in subtler places: the steadier cadence of the pumps, the volunteers who show up earlier, the way the seedlings have teeth now."
    "You breathe in. The air smells of metal, coffee grounds, and the faint green of algae—an oddly comforting bouquet that says this place is alive and working."
    "Professor Asha Rao enters, carrying a stack of printouts, her braid swinging with the motion. Her face is bright with a smile that doesn't erase the scientist's caution behind it."
    show professor_asha_rao at center:
        zoom 0.7

    professor_asha_rao "Congratulations are in order. The council's vote this morning—unanimous to pilot expansion citywide. They cited your data and the community testimony. New Maris wants to replicate the model."
    "You feel your chest rise, a soft, physical lift that the strings in your head mirror. The word 'unanimous' tastes like rare and fragile fruit."

    mara_ellis "Citywide?"

    professor_asha_rao "Citywide. But listen—there are strings attached. Investors and contractors are circling. That growth will bring changes we didn't model for yet."

    mara_ellis "We planned for scale in the code and the sediment maps—"

    professor_asha_rao "—but not for corporate procurement cycles, not for integrated proprietary systems that gate data. The physics scale linearly; the social systems do not. We need to talk through thresholds, maintenance loops, and governance clauses before anyone signs anything."
    "You feel the warmth of the moment and the cold of the warning braided together. Hope rising; caution tethered to the keel."

    menu:
        "Make a short, impromptu thank-you":
            "You step forward, voice steady. 'Thank you—to everyone who planted, measured, and believed.' The crew claps. Jonah squeezes your shoulder, and a camera clicks."
        "Turn the moment toward logistics":
            "You hold up a hand and say, 'We should prioritize a governance clause for the pilot expansion.' The room shifts—applause fades into quick questions about timelines and liability."

    menu:
        "Ask for a community-subcontract clause now":
            "You speak quickly. 'Any maintenance scope must prioritize local crews and open procurement windows.' The rep nods, but the smile is guarded. You feel a small victory—procedural, but meaningful."
        "Table contract talks and focus on monitoring clauses":
            "You say, 'We need to finalize monitoring and governance before procurement.' The room reluctantly agrees. The rep's expression cools; you note the flicker of impatience."

    menu:
        "Accept integrated contracts with careful clauses; we scale now.":
            jump chapter6
        "Refuse NovaSeis involvement and insist on transparent, local-only contracts.":
            jump chapter13
        "Secretly gather and publish independent post-installation data to build legal leverage.":
            jump chapter6
    return
