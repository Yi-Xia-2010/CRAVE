label chapter2:

    # [Scene: Main Street | Morning]

    scene bg ch2_c4ca42_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, steady hum — gentle piano with distant marine wind]
    # play sound "sfx_placeholder"  # [Sound: Distant gull call, muffled footfalls on damp wood]
    "You walk the length of Main Street with the brass compass against your thigh, its small weight a metronome against the rhythm in your chest. The harbor smells of kelp and diesel and the cinnamon warmth"
    "spilling from Rosa’s café; steam threads the air into small, honest clouds. Your braid clings damp against your neck. The morning is neither bright nor dark — washed in the gray that has become this town’s"
    "normal — and it presses you into a careful, folding quiet."
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "There you are, niña. You look like you slept with charts in your brain."
    "You try to smile. 'I wished I had,' you say, and the words land smaller than you expect."

    rosa_alvarez "How is Tomas?"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "He’s... considering options. He’s stubborn in the way that makes me proud and terrified."
    "Rosa squeezes your hand. The café’s air is thick with roasted beans and cardamom; the string of fairy lights in the window casts halos on her wrinkled smile."

    rosa_alvarez "Tell him for me — whatever he decides, there'll always be coffee here.' (beat) 'And tell him to stop using my tables for welding, eh?"

    menu:
        "Say, 'I'll tell him, but he might need convincing.'":
            "You promise in a softer voice, picturing Tomas's stubborn jaw, and Rosa nods like she already knows."
        "Say, 'I'll bring him by myself.'":
            "The offer trembles out of you; Rosa's eyes go bright and old and grateful, and you feel the first small lift of not carrying everything alone."

    # --- merge ---
    "You leave with the warmth still pressed into your palm. The compass swings once more, then settles. Main Street narrows toward Town Hall: a low brick building whose steps have been smoothed by a hundred meetings,"
    "a hundred weeks where people came together to decide how to keep their homes intact."

    rosa_alvarez "Good. Now go. Eyes open, Maya."
    # [Scene: Town Hall — Exterior Steps | Late Morning]
    hide rosa_alvarez
    hide maya_reyes

    scene bg ch2_c4ca42_2 at full_bg
    # play music "music_placeholder"  # [Music: Soft, contemplative strings — a slow build]
    # play sound "sfx_placeholder"  # [Sound: Murmur of conversation, umbrellas clicking shut]
    "Under Marco's umbrella, he arrives precisely on schedule, the blazer more immaculate than the weather allows. He moves through the crowd with the night-side confidence of someone practiced at small shows of control."
    show councilor_marco_lin at left:
        zoom 0.7

    councilor_marco_lin "Good morning, everyone. Thank you for coming."
    "His greeting is a thin shield. You can see the way some faces relax and others tighten. Marco's vote is the hinge; he knows it, they all know it. You feel Asha's presence like an anchor at your back — quiet in a way that cuts through the room's noise."
    show asha_malik at right:
        zoom 0.7

    asha_malik "We should listen to every proposal fully,' she says to you as she joins, voice like worn sea glass. 'The science needs to be heard, but the people must be seen."
    "You nod. Her certainty is small and steady; it keeps you tethered beneath the tilt of your worry."
    # [Scene: Town Hall — Back Room | Midday]
    hide councilor_marco_lin
    hide asha_malik

    scene bg ch2_c4ca42_3 at full_bg
    # play music "music_placeholder"  # [Music: Low, steady ostinato — the tempo inches up]
    # play sound "sfx_placeholder"  # [Sound: Soft rustle of paper, chairs creaking, a cup set down carefully]
    "June Park steps in like a clean line drawn across the room: trench coat clasped, briefcase clicked closed. The silver streak at her temple catches the light like a punctuation. Her presence cuts a different sort of certainty—engineered, polished, no room for fog."
    show june_park at left:
        zoom 0.7

    june_park "Thank you, Councilor Lin, and thank you, San Brisa,' she begins, voice even and practiced. 'Aurelia's seawall is a proven solution. We have modeled storm resistance, insurance reductions, and timelines that protect your property values immediately."
    "She clicks and the projector hums. Steel pylons rise on the screen. Diagrams march in tidy rows: expected wave heights, cost-benefit analyses, insurance-savings charts. The language is clinical. 'Protection,' 'mitigation,' 'efficiency.'"
    "You feel your notebook grow heavier in your hands, though it's unchanged; the weight is a thought that sits in your chest. Words slide into you — 'immediate,' 'certainty' — and though you know the numbers,"
    "you also know what those pylons look like: a blunt edge between people and ocean, a boundary that keeps some things safe by divorcing others."
    # play sound "sfx_placeholder"  # [Sound: A low, focused murmur as people take in the slides]
    hide june_park

    scene bg ch2_c4ca42_4 at full_bg
    "Eli Navarro is there, sleeves rolled as if he'd been pulled from a workbench and set in the front row. His paint-speckled fingers are as you remembered, tucking a folding timber ruler into a back pocket"
    "on instinct. When June concludes, he stands with the easy gravity you have come to rely on."
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "Clinically tidy, yes,' he says, voice warm but not without edge. 'But we need to think about the living systems those pylons replace. Living shorelines—marsh restoration, engineered reefs—absorb energy and preserve access. They’re not just ecological ornament; they’re long-term resilience."
    show june_park at right:
        zoom 0.7

    june_park "Mr. Navarro, with respect, living systems don't provide the same immediate, quantifiable protection for high-value commercial zones. Time matters when banks demand certainty and insurers calculate premiums."

    eli_navarro "And time also matters when you push people out of neighborhoods to save profit centers. We aren't asking to ignore immediate needs. We're proposing phased pilot projects that demonstrate function — we can model for insurers and show staged results."

    june_park "Pilot projects are costly and uncertain. Aurelia's approach secures the town now."

    eli_navarro "Secures, or shifts risk elsewhere?' 'We can design prototypes that are quicker and cheaper than you assume. We have skilled people here. We can prove it."
    "June's mouth thins. The exchange is measured but the subtext is sharp. Around you, murmurs ripple like a distant tide—approval and skepticism braided together."

    menu:
        "Interject, citing Asha's field data.":
            "You open your mouth and then close it; Asha gives you a small look that says 'later.' You swallow and let Eli take the front line for now."
        "Hold your ground, let Eli speak while you watch Tomas.":
            "You watch Eli frame the arguments, and your eyes find Tomas in the doorway. His jaw is tight, the corner of his mouth set. Letting others speak feels like an exercise in trust and dread."

    # --- merge ---
    "Tomas stands at the room's threshold like a hinge. He doesn't enter fully; he lets the door frame hold him. His hands are the hands that fixed your mother's porch, the hands that steady the town's"
    "small machinery. The decision today is not just policy — it's a ledger of the life he keeps."
    "You think of Rosa's coffee-stained smile, of Asha's patient insistence, of Eli's easy gestures. The room divides between those who want solidity now and those who wager on a different future. Every proposal reads like a promise and a threat at once."
    show councilor_marco_lin at center:
        zoom 0.7

    councilor_marco_lin "Both proposals raise valid points. The question facing us is which path protects our town and its people in the short and mid term.' 'I want to hear from the community. Let us proceed with questions."
    "June Park nods, composed; Eli Navarro leans forward, elbows splayed, ready. Voices that had been murmurs step into the room like the slow climbing of a tide — careful, edged with worry."
    "You feel your pulse shift from a steady thrum to a quiet, urgent tapping. It is not loud enough to startle anyone; it is only a reminder under the skin. The options in the room are"
    "not theoretical anymore. You picture Tomas's shop window, the salt-etched tools, the list of customers pinned beneath a magnet."
    "Asha touches your sleeve in a wordless gesture that says: remember the data, remember the people."
    "You prepare to speak — to thread the numbers with the memories, to make the scientific plausible and the human present — and the room leans in."
    hide eli_navarro
    hide june_park
    hide councilor_marco_lin

    scene bg ch2_c4ca42_5 at full_bg
    # play music "music_placeholder"  # [Music: Soft, unresolved chord — the tempo holds, building subtly]
    # play sound "sfx_placeholder"  # [Sound: A collective inhale, like the slow collecting of breath before a long exhale]
    "The decision is about to be framed; the first public opinion will land like a stone. You stand on the edge of that moment, feeling all the small things that have led here — guilt, hope,"
    "a tether of loyalty to a town that has given you everything and asked for too much in return."
    "You are ready to speak. The room waits."

    scene bg ch2_c4ca42_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
