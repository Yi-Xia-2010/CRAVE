label chapter1:

    # [Scene: Marisora Harbor | Dusk]

    scene bg ch1_Start_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low gull calls; distant hull creaks; a soft wind pushing small waves against wooden pilings]
    # play music "music_placeholder"  # [Music: Sparse, melancholic strings]
    "You step off the shuttle with the tide-watch heavy in your palm. The brass is warm from your skin, the engraving half-softened by salt; it ticks in a way that feels like a small, private insistence."
    "The air tastes the same as the last time you left — sharp with salt and a faint tang of iron — and because it smells familiar, it hurts more. The harbor looks smaller and older"
    "than you remember, as if someone has been shaving years off its edges: broken planks mended with scavenged metal, buoy ropes repurposed into handles, paint layers like geological strata. There is a hardness to it now,"
    "like the town has learned to keep everything it loves at arm's length."
    "You run a thumb along the cracked edge of your tablet in your satchel. The crack fans like a river delta across the screen; the device boots with a stutter. Your faded green scarf is looped"
    "in the bag, a small, stubborn memory. You roll your sleeves without thinking — habit, armor, ritual. There is a checklist in your head, tidy and impatient: meet Rita, inspect nets, speak to Mayor, present preliminary"
    "models. The list steadies you and also makes you smaller."
    "A weathered skiff bumps the pier as a man hollers directions. Salt flakes off the ropes in mica-like showers. The harbor smells of wet wood and old diesel, of drying fish and someone frying something in"
    "an alley. Low clouds gather offshore, a bruised band that eats the sunset. The light here is flatter, the shadows longer; even the gulls seem to wheel with a kind of studied caution."
    "You scan faces for familiar lines. Hands that once moved like breathing maps of this place are now patched and callused in different ways—sewn leather, improvised ferrules, a waiting-for-help tenseness in the way people look at"
    "equipment. You have returned with answers, or so you told yourself on the flight down. The town has kept its charms — solar canopies blink like small promises, string lights dangle over community tables, someone has"
    "freshly painted a festival patch onto a captain's cap — but those details feel less like hope and more like a thin varnish over a deep, exhausted need."

    scene bg ch1_Start_2 at full_bg
    "You inhale. You can feel responsibility sitting at the base of your skull like an ache. You left after the storm years ago because there was nowhere left to stand; you came back because you believed"
    "staying might finally do the work that leaving couldn't. The thought is both a vow and a confession."
    # [Scene: Community Greenhouse & Seed Bank | Dusk]

    scene bg ch1_Start_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Hum of heaters, soft drip of condensation, distant muffled conversations]
    # play music "music_placeholder"  # [Music: Low cello notes underscoring tension]
    show rita_ortega at left:
        zoom 0.7

    rita_ortega "Maya! You actually made it."
    "She stands too fast and brushes a wet hand on her apron, smiling that quick, fierce smile she always gives when she wants to hide worry."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "I did."
    "Your voice sounds strange in the humid air, as if part of it belongs to the town now. 'How — how have things been?'"

    rita_ortega "Same as the headlines say, but worse between the lines."
    "She gestures at a bulletin board covered in seed packets and handwritten notes. 'Nets failing in pockets, fish moving offshore, and the grant? Delayed again. The regional office sent a letter — red tape, they said. 'Awaiting review.''"

    maya_reyes "Awaiting review."
    "You taste the phrase; it tastes like foam. There's so much that will fit into a review that doesn't meet the people who will drown. 'Do we know what they're reviewing? Timelines?'"
    "Rita: (Her laugh is sharp.) 'Timelines are a polite way of saying 'we hope to, maybe, if funds permit.' Tomas is trying to keep calm, but—'"
    "She presses her palm to her forehead. 'We can't do much without cash, Maya. Hands and courage don't buy concrete.'"
    "You feel the old reflex: solve, calculate, deliver. The models you can run on your tablet bloom in your head — projected outcomes, error bars, mitigation timelines — all instruments for a battle you are not sure you can win alone."

    rita_ortega "Listen, you look... tired."
    "She studies your rolled sleeves, the soil under your nails implied. 'We need you sharp. The neighborhood meeting's tonight — it's on the board out front. People will be there.'"

    maya_reyes "I know."
    "You close your fingers around the tide-watch inside your jacket. The brass hums against the bone of your palm. 'I wanted to start with a survey of the nets and some gauging data. If the currents have shifted, we can recommend new trap geometries.'"

    rita_ortega "That's science, Maya. It's what you do. But we've also got fishermen who will tell you the water doesn't listen to a model. People need to be part of the plan."

    maya_reyes "They will be."
    "You don't mean to snap, but the sentence is edged with the fatigue of trying to be both scientist and daughter of Marisora. You remind yourself to breathe. 'We—I'll work with Rita here. We'll bring data and proposals.'"
    "Rita puts a hand on yours, grounding, impatient. 'And your scarf?'"
    "She grins, the light in her eyes an accusation and a plea. 'If the storm comes, don't do it for the town alone. Do it for yourself.'"
    "You imagine folding the town inside your chest like the scarf, smaller but warm. The thought is an aching luxury."

    menu:
        "Show Rita the cracked tablet now":
            "You flip the tablet open, booting the models. Lines of predicted currents and a half-written email to the regional office appear. Rita peeks over your shoulder, brow furrowed as numbers give her a different kind of anchor."
        "Help hang a stray string light":
            "You climb a small ladder and steady a stray string light while Rita steadies you with a hand at the back. For a moment you both laugh at how something so small can feel like fixing the world."

    menu:
        "Ask Elias about Arlo's mistake":
            "You lean in, genuinely curious. Elias rolls his shoulders and recounts the way a mismeasure can ripple into a day's wasted labor. You listen, and the story becomes a design problem you now want to solve."
        "Tease Elias about going barefoot":
            "You grin and point at his bare feet. Elias shrugs and digs his toes into the wet wood, as casual as the sea itself. The tease breaks some of the gravity between you, and he laughs, a bright splash in the dusk."

    jump chapter2
    return
