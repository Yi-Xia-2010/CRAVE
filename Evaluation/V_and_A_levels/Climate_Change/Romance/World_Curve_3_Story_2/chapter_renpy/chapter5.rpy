label chapter5:

    # [Scene: Saltmarsh Wetlands | Night]

    scene bg ch5_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind climbing from a whisper to a hard rasp; waves thumping somewhere beyond the reed line; the hollow clack of stakes being driven into wet sand.]
    # play music "music_placeholder"  # [Music: Tense, driving strings with a high, hopeful violin motif beneath — a heartbeat that won't quit.]
    "You kneel at the water's edge, a stub of pencil between gloved fingers, and drag a shaky line into the damp sand. The graphite catches on grit and seaweed; your breath fogs, hangs, and is gone."
    "Your braid is plastered to your neck, salt on the skin where your collar has rubbed it raw. Every mark you make feels like an argument with the tide itself."
    "Around you, the camp is a constellation: lamps like small suns, the blinking LEDs of Noor’s instruments like constellations reborn at sea level. Volunteers haul reed bundles, lash mats with cord that squeaks through wet hands."
    "Prof. Noor moves among them, toggling sensors, squinting at readouts, her fingers stained the brown of soil."
    "Rosa's yellow jacket is a flare in the low light; she barks a command and the word threads out, snapped into action. Ben stands a little apart, hands jammed in his coat pockets, face a map"
    "of storms you have both lived through. His eyes keep drifting to the line where the marsh gives way to surf."

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The buzz of the drone is clinical, almost indifferent; the wind answers with a rising keening.]

    "You open the terse note because knowing is its own kind of armor. Legal counsel" "We advise that all unauthorized modifications cease pending review."
    "You fold the message back into your palm. Your fingers smell of peat and solder; there is a faint metallic tang at the back of your tongue. You think of your brother: a shape that comes"
    "with every decision, a measure you return to when consequences stretch wide. The old, familiar pull — if I had been faster, if I'd done more — tugs at your ribs like a tide."
    "Prof. Noor leans close, the lamp light carving ridges across her face."
    show prof_noor_azizi at left:
        zoom 0.7

    prof_noor_azizi "Data tonight will be messy. If we can get one full tidal cycle, even noisy, it proves resilience in practice. But the instruments are vulnerable and the volunteers—"
    "Prof. Noor's voice trims itself at the end, the caution grown from long experience. Her eyes find yours and there is no judgment there, only the clarity of someone who has spent decades watching experiments fail and succeed by the thinnest margin."
    "You look up and see Aiden Kuro materialize from the shadow of the boardwalk — bundled nets over one shoulder, a thermos wrapped in a cloth in the other hand. His cap is soaked, a dark"
    "halo around his face. When his eyes meet yours, they are soft in a way that steadies the rush like a buoy."
    show aiden_kuro at right:
        zoom 0.7

    aiden_kuro "You look like hell,"
    show maya_soler at center:
        zoom 0.7

    maya_soler "I feel like it, too.' (You rub the pencil-stub between thumb and forefinger.) 'We're close, Aiden. If this holds through the squall, we have evidence. We prove living structures can flex where concrete just breaks."
    "Aiden Kuro shifts, tightening the strap on his nets. He breathes in from the thermos and the smell of strong tea and salt finds you — familiar, grounding."

    aiden_kuro "Proof won't mean anything if someone gets hurt. Ben saw what the last engineered 'solution' did to people's boats. I don't want to be through this and find we fixed one problem by making another."
    hide prof_noor_azizi
    show ben_harper at left:
        zoom 0.7

    ben_harper "I've been around when the sea took more than it gave. We've got to be practical. If the wind turns and a volunteer slips —"
    "Rosa Tan snaps back, fingers clamped on a rope like a second hand around the night."
    hide aiden_kuro
    show rosa_tan at right:
        zoom 0.7

    rosa_tan "We either show the town we can do this by doing it, or we give Elias another week to paint his promenade and buy votes. Momentum matters. People will read retreat as failure."
    "The argument is a living thing circling you, and you are part of it. You feel the pull to overcommit — the old, familiar shape of your brother in the space your shoulders are trying to"
    "hold steady. Every fiber of you wants to be the one who keeps everyone safe and the plan alive."

    menu:
        "Reach for Aiden Kuro's thermos":
            "Your hand closes on the cloth-wrapped thermos. The heat sears through the fabric; for a second you think of the small, quiet breakfasts you once shared with him on calm fishing mornings. He watches you, and there’s a softness that makes your chest unclench."
        "Take the nearest line and shout orders":
            "You snatch the wet rope and call out commands. Your voice cuts through the wind — sharp, necessary. Volunteers obey like clockwork; an order becomes a lifeline in the dark. Aiden's eyes meet yours, and he nods, biting his lip like he’s trying to keep something unsaid."

    # --- merge ---
    "Return to main narrative."
    "Noor kneels at the edge of a sensor array and squints at a flickering readout. A small LED blinks amber, then green. The wind jerks the reed mats; a lash pops. A volunteer swears, and the word is swallowed by surf."
    hide maya_soler
    show prof_noor_azizi at center:
        zoom 0.7

    prof_noor_azizi "If anything fails tonight, we lose more than credibility. We lose people’s trust. But if it succeeds — even a small success — that will spread like salt in the best way. It will taste of the place."
    "The drone banks closer, its camera angling to catch the line of faces, the blades spinning like indifferent metronomes. Elias's presence hangs in that mechanical eye: polished proposals, renderings of promenades, promises wrapped in stainless steel."
    "He is not here, but his reach already is. The text message's edges have begun to feel like a countdown."
    "Aiden Kuro crosses to stand at your shoulder. He brushes a clump of wet hair from your forehead with a thumb that is rough and warm. His touch is ordinary and intimate and it steadies something in you that fear cannot name."
    hide ben_harper
    show aiden_kuro at left:
        zoom 0.7

    aiden_kuro "Maya, look at me. If you push everyone through this and the tide takes them—what will you be left with? If you stop and we lose tonight — you still have tomorrow and the day after and these people who will remember that you kept them safe. Promise me you won't drown yourself to prove a point."
    hide rosa_tan
    show maya_soler at right:
        zoom 0.7

    maya_soler "And if we pull back now, Elias floods the council with renderings and lawyers. He makes his wall look inevitable. He buys time with money and the town's voice gets drowned. I've seen what happens when we let that happen."
    "Your voice is threadbare but clear. The sky has turned a low, bruised purple; rain comes in a hard, salt-sliced sheet that prickles every exposed cheek. Lamps make halos in the spray. The instruments around Noor blink faster, feeding you noise and meaning in the same breath."

    prof_noor_azizi "Data and lives are not a binary, Maya. We have to choose a way that doesn't make either a casualty. But the night will not wait for indecision."
    "Ben Harper steps closer, his presence like a rock turned to show the current."
    hide prof_noor_azizi
    show ben_harper at center:
        zoom 0.7

    ben_harper "You're younger than me. You don't owe the sea anything. You owe yourself breath and tomorrow. Don't make martyr because the night is loud."
    "This time Rosa Tan replies first, voice raw and urgent."
    hide aiden_kuro
    show rosa_tan at left:
        zoom 0.7

    rosa_tan "And you don't owe Elias the benefit of miracles. People need hope that isn't sold to the highest bidder."
    "You hear the town in them: worry, clarity, accusation, love. Your heart hammers — not the slow, procedural urgency of a meeting, but a rapid drum of immediate peril. The storm is chewing at the edges"
    "of the marsh. Salt stings the back of your throat. The volunteers wait on your breath like sailors waiting for a command."

    menu:
        "Kneel and inspect the southern anchor yourself":
            "You drop to your knees in the mud, hands cold and sure as you check the lashings. The reef of your palms know the trade; the work steadies your pulse. Aiden crouches and mirrors you without asking. For a moment the world narrows to rope and mud and the steady person beside you."
        "Stand and call for evacuation procedures":
            "You stand, voice clear and loud, and start the evacuation cadence. People move, ropes release, lamps are snatched down. You feel the sting of letting go, but the motion feels right — a steward who protects rather than proves. Aiden holds the net tight, eyes like flint."

    # --- merge ---
    "Return to main narrative."
    "The wind climbs again, a scream threaded with water. A wave—bigger than the ones before—folds over the break and sends a spray that shoves at your ribs. Someone yells; a lamp tips but a volunteer catches"
    "it, spatters of oil and flame kissing wet wood and then nothing. The instruments ping alerts; Prof. Noor's tablet registers a dip in power, then a recovery. The drone records with a cold, fascinated lens."
    "Your chest feels like a cage of tide-worn planks. You can almost see your brother standing behind you, not accusing but asking whether you would be the one who lets the town go piece by piece."
    "His absence is a weight you wear like a coat. Everything inside you wants to shoulder that coat until your bones ache."
    "Aiden Kuro's hand finds yours again, brief and possessive. His thumb rubs a circle on the back of your glove, as if trying to smooth the tension from you. The touch is small; it is everything."
    hide maya_soler
    show aiden_kuro at right:
        zoom 0.7

    aiden_kuro "Whatever you choose, you're not alone in it."
    "His voice is steady, and even in the roar you can hear the promise. For a dizzy second, amid rain and mud and the smell of iron in the air, the possibility of something tender and"
    "tenacious takes root: the plan could succeed, and you would have someone at your side who understood the cost. That thought, like a planted reed, sways but does not break."
    "Prof. Noor checks a sensor and hisses under her breath; a cable has been jarred loose. Rosa is shouting orders and swearing over the interference. Ben moves with measured steps, an old cadence of storms and"
    "survival. The drone, the legal note, Elias’s distant bluff — they loom, but they do not decide for you."
    "You feel the arousal of the moment peak — the storm is a living metronome, faster and louder, your heart syncing with it. Each choice is a wave cresting. The volunteers look to you. Aiden’s amber"
    "gaze waits for the shape your answer will take. Noor’s eyes ask for the practical, Ben for the humane, Rosa for the bold. Your brother's shadow asks for you to be the kind of person who"
    "doesn't leave things half-done."
    "You inhale, cool and full of salt. Time narrows until the only thing that exists is this: the choice you make now will shape whether the pilot stands when the sea tests it next, and whether the town sees you as the steward of both people and place."
    # play music "music_placeholder"  # [Music: Single, sustained high violin note; then cut to a hush that is louder than noise itself.]
    hide ben_harper
    hide rosa_tan
    hide aiden_kuro

    scene bg ch5_4001e7_3 at full_bg

    jump chapter7
    return
