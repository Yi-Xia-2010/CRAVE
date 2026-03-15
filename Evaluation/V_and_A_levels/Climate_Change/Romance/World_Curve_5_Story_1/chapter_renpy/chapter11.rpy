label chapter11:

    # [Scene: Marisol Bay Boardwalk | Morning]

    scene bg ch6_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls; the soft thrum of generator-backed cameras; murmurs rising like tidewater]
    # play music "music_placeholder"  # [Music: Low steady cello, a hopeful undercurrent]
    "You arrive with the weight of the last choice still warm in your palms — the decision from Chapter 5, Option A, that pushed TideLab into the light and into the ring. The viral footage changed"
    "everything overnight: a three-minute splice of the stand, a shaky shot of Corinne's convoy, Jules' footage intercut with interviews—enough to make Marisol Bay the picture the country woke to."
    "Your boots splash in the shallow puddles. The air tastes like salt and paper cups of coffee. People look at you with the particular way people look at someone who has been both center and scaffolding:"
    "gratitude braided tightly with fatigue. You have learned this look. You have learned to carry those threads without unraveling."
    "Jules finds you near the rail, camera strap damp on her shoulder, her blue hair flattened by the wind. She smiles, the kind of grin that is mostly adrenaline and a little euphoria."
    show jules_park at left:
        zoom 0.7

    jules_park "It blew up. The clip hit a national feed around dawn. The reporter we trusted—Marin—ran the document dump this morning. Old Voss memos, internal risk estimates—things that don't age well in public."
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "You and Marin—how did you get those past their legal vetting? You risked a lot."

    jules_park "You ask the wrong person; you ask me, I say stubbornness. But we scrubbed everything. Nothing that compromises our counsel. Just...context."
    "You press your thumb against the leather of your notebook until the grain almost disappears. Your mind catalogs: evidence chain, counsel's approval, the town's safety. Every victory has edges."

    menu:
        "Check the documents one more time with Jules":
            "You step back into the TideLab tent and run your fingers over printouts again. Jules watches you with a quiet, conspiratorial patience; the documents feel heavier after you touch them, but whole."
        "Trust Jules and step out to the crowd":
            "You leave the tent and breathe the public air. People part for you like soft ocean. A few faces you recognize — Mateo, Abuela Rosa — and it steadies you."

    # --- merge ---
    "Narrative continues into the next scene."
    # [Scene: TideLab | Midday]
    hide jules_park
    hide amaya_reyes

    scene bg ch6_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hiss of a portable heater; the murmur of volunteers exchanging details]
    # play music "music_placeholder"  # [Music: A measured, rising piano line]
    "Luka Maren is crouched over a drone controller, hands moving with practiced gentleness. He looks up, eyes like warm amber embers, and for a moment you just look at each other and count the small things"
    "that made this possible: nights soldering sensors, wet boots shared on storm watches, the stubborn laugh you both made once when a buoy floated off in the wrong tide."
    show luka_maren at left:
        zoom 0.7

    luka_maren "They want to interview me for a tech piece. Marin's asking for a demo of the restoration rigs. They want pictures of a 'community solution.'"
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "Be careful. Language matters. We don't hand them diluted hope. We give them the mechanics and the people."

    luka_maren "You're the rhetorician today. I'll be the one who makes the thing work."
    "You meet eyes for a beat too long. There are things you haven't said in public—how guilty you feel about the chaos, the neighbors who lost income while the stand held, the nights you lay awake"
    "imagining what another storm could do. But there is also the steadiness of what you built together."
    "Mateo arrives, raincap in hand, and squeezes your shoulder with the weathered reassurance of kin."
    show mateo_reyes at center:
        zoom 0.7

    mateo_reyes "Council's going to be packed. Tamsin says she'll call the special session at noon. If they actually listen—"

    amaya_reyes "They will listen. We have evidence and the town. They will listen."
    "Tamsin's message comes in as you step out: an invite to speak at the community session. Her text is careful, the kind of politeness that has been tempered into diplomacy by pressure."

    menu:
        "Rehearse a data-heavy address":
            "You sketch a few talking points in the margins of your notebook: sediment rates, modeled flood plain changes, success rates from pilot oyster beds. It's precise; your voice steadies."
        "Prepare an appeal to the town's stories instead":
            "You write down three names — Abuela Rosa, Mateo, Jules — and a single sentence: 'We are not lines on a plan.' That short sentence feels like handing the day a pulse."

    # --- merge ---
    "Narrative continues into the community hearing."
    # [Scene: Community Hall | Early Afternoon]
    hide luka_maren
    hide amaya_reyes
    hide mateo_reyes

    scene bg ch6_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Muffled voices and the occasional clap; a camera's autofocus whirring]
    # play music "music_placeholder"  # [Music: Tension lifts into a bright, open chord progression]
    "The hearing begins with presentations from Tamsin, who carries the weight of municipal procedure like a ledger. She is composed, but the lines at her temples betray how hard the last days have been. Across the"
    "table, Corinne Voss sits impeccable and precise, platinum hair a punctuation mark, AR glasses off and folded like a sentinel's shield."
    show tamsin_cho at left:
        zoom 0.7

    tamsin_cho "Council, we've convened this emergency session to address the concerns raised by recent disclosures and by our community. I have listened to residents. I have reviewed the staff advice. The proposal as submitted by Voss Marine is significant — it promises protection for critical infrastructure — but it also raises issues around displacement and long-term ecological impact."
    show corinne_voss at right:
        zoom 0.7

    corinne_voss "Our modelling demonstrates that, absent decisive infrastructure, more people will be displaced in the long term. Our design does minimize habitat loss across a broad horizon. We are open to adjustments that do not compromise efficacy."
    "You stand when your name is called. The hall tilts toward you; the cameras tilt with it. You don't reach for data or for platitudes. You speak with the blunt compassion you've honed."
    show amaya_reyes at center:
        zoom 0.7

    amaya_reyes "We worked all night to get the records into hands who could read them. We did not want spectacle. We wanted scrutiny. Those documents show a plan built without enough accounting for lived histories here — not just rooms on a map, but people tied to the tide.' (beat) 'We are not against protection. We are against protection that erases us."
    "Corinne Voss watches you like someone observing a tide line, measuring what will wash away. Her voice, when she answers, is practiced and narrow, but in the thread of it there is a microphone slip—something a reporter will pick up."

    corinne_voss "We make hard choices based on large-scale risk. Emotion is part of the debate, but it's not a substitute for engineering."

    amaya_reyes "No one asked emotion for permission. We asked for inclusion."
    "Questions from the council edge toward the leaked memos. A council member holds up a printout showing a Voss internal risk matrix at odds with Corinne's public assurances. The room exhales."
    "Tamsin stands, hands clasped as if to contain the shake in them."

    tamsin_cho "Given the new evidence and the community concerns, I cannot in good conscience recommend a vote on full relocation at this time. I propose a conditional path: reduce the seawall footprint, finance distributed marsh restoration overseen by community cooperatives, and commit to a pilot of community-owned aquaculture financed through Voss bonds."

    corinne_voss "Voss Marine will scale back the seawall's footprint by thirty percent in critical neighborhoods and fund a distributed marsh restoration program. We'll seed a community aquaculture fund to be managed locally, with technical oversight from Voss. We will also establish a joint oversight board including municipal, community, and Voss representatives."
    "The hall shifts. A dry, incredulous, then mounting sound washes through — first disbelief, then stunned relief. You feel it in your limbs: a looseness, like a muscle after it unclenches."
    # play music "music_placeholder"  # [Music: A warm swell of strings and muted brass]
    # play sound "sfx_placeholder"  # [Sound: A single, held inhalation from the crowd — then applause, slow and deliberate at first, then building]
    "Corinne Voss's voice holds, but there is something softer beneath the steel."

    corinne_voss "This is not everything I wanted. But I recognize the need for legitimacy, and I will not proceed without it."

    amaya_reyes "We will hold them to account. TideLab will be at the table. Our marshes will be restored. Our neighbors will stay."
    "Luka Maren appears at your side, salt in his hair and that locket heavy on his chest as if marking the moment. He squeezes your hand — the gesture isn't public theater, but solidarity. He leans in, voice low."
    hide tamsin_cho
    show luka_maren at left:
        zoom 0.7

    luka_maren "We did it."
    "You swallow, the word huge in your mouth. The victory is not unblemished: the scale still carries compromise, and you carry a private tally of the chaos the fight cost. But the town is still here."
    "Most homes remain. Funding for TideLab — for expansion of your humble operation into something that can train, employ, and protect — arrives in the form of corporate checks tied to community governance. It is complicated,"
    "but viable."
    "Abuela Rosa stands nearby, hands shaped by decades of work, shawl wrapped tight against the wind. She hums — not an exultant song but a low coastal tune you have heard since childhood — and it sounds like blessing."
    hide corinne_voss
    show abuela_rosa at right:
        zoom 0.7

    abuela_rosa "The tide moves, niña. Sometimes it takes. Sometimes it gives. Today it gives a little."
    "Mateo laughs, a sound that is almost disbelief and almost joy."
    hide amaya_reyes
    show mateo_reyes at center:
        zoom 0.7

    mateo_reyes "They actually listened. God help them if they don't mean it."
    "You laugh too, and in that laugh there is release — a spasm of sorrow and triumph braided together."
    # [Scene: TideLab Exterior / Marshland Reserve | Late Afternoon]
    hide luka_maren
    hide abuela_rosa
    hide mateo_reyes

    scene bg ch6_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The wet slap of boots in mud; the chatter of volunteers. Abuela Rosa's humming threads through it.]
    # play music "music_placeholder"  # [Music: Gentle acoustic guitar, hopeful and unhurried]
    "You stand in the mud with Luka beside you, the world tasting of brine and new dirt. The sun presses a soft warmth through a thinning cloud. The air is full of the ordinary miracle of hands at work."
    show luka_maren at left:
        zoom 0.7

    luka_maren "I turned down the other offers."
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "You did?"

    luka_maren "Marin called from [redacted] this morning with a 'strategic role.' It would have meant moving and a lot of bureaucracy. But—' (he fingers the locket) '—I want this to be where the tech meets the people. I want to do it with you."

    amaya_reyes "Are you sure? This will be everything and also crumbs. It will be slow."

    luka_maren "I know. I prefer slow and honest to fast and...absent."
    "You let the words settle like sunlight on wet wood. They make a little map of possible futures in your chest — a life with tangled schedules and seedlings and grant writing, with nights measuring sediment cores and mornings checking tide gauges. It is not tidy, but it is shared."
    "Later, you and Luka stand before the crowd on the boardwalk as volunteers plant the last of the seedlings. Salt clings to your hair. Your jacket smells faintly of algae and saved coffee. Someone passes you a paper cup. You drink; it tastes like victory and sea."

    amaya_reyes "This work will not protect us overnight. It will not be without sacrifice. But it will be ours. Our marshes, our fisheries, our rights to stay and shape the shore. TideLab will expand. We'll train, we'll employ, we'll steward."
    "The crowd responds with cheers, with the low chorus of people who have been afraid and then found a rope. Your chest loosens. Guilt lingers — a corner of your mind catalogues every displaced schedule, every"
    "volunteer who burned out, every family's lost catch — but it is tempered by the way neighbors help one another lift a sodden seedling into place."
    "Abuela Rosa breathes in close, planting beside you. Her hands are sure; she hums quietly, as if reciting a line of containment and blessing."
    show abuela_rosa at center:
        zoom 0.7

    abuela_rosa "Plant the roots deep, niña. Roots know the way."
    "You press the soil around a seedling and feel something like belonging swell — neither triumphant nor triumphant enough, but steady."
    hide luka_maren
    hide amaya_reyes
    hide abuela_rosa

    scene bg ch6_f99e88_5 at full_bg
    # play music "music_placeholder"  # [Music: Strings resolve into a soft, sustaining chord; the clatter of distant waves becomes rhythmic and reassuring]
    "You and Luka walk back toward the shed with mud on your boots and warmth in the chest. He reaches for your hand again, this time not as a reliance but as a pact."
    show luka_maren at left:
        zoom 0.7

    luka_maren "We'll build it differently. We'll make a model other towns can pick up. Cooperative aquaculture, resilient marshes, sensors that tell a story rather than sell one."
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "We'll keep each other honest."
    "He smiles, tired and honest, and you return it. There is no guarantee that every storm will be weathered. There is no guarantee that Voss will always keep its word. But there is a new scaffolding — legal, social, ecological — and a community that learned to speak together."
    "You look at the bay, at the horizon where sky and water argue and make room for each other. You think of the ledger you carried — the town ledger and TideLab's notebook — and how they have begun to be read together."
    # play music "music_placeholder"  # [Music: The melody thins into a single held note, warm and steady]
    hide luka_maren
    hide amaya_reyes

    scene bg ch6_f99e88_6 at full_bg
    "You still carry guilt for the chaos, for the nights people lost sleep and work. It sits beside the relief like a stone in your pocket. But the town holds. Most homes remain. Seeds go into"
    "the earth. Funding flows into cooperative accounts. Corinne Voss and Voss have been forced to step back and pay forward; Tamsin has found a way to thread municipal responsibility through communal stewardship. Luka stays. TideLab expands."
    "Abuela Rosa hums."
    "You breathe in the salt, and the breath tastes faintly of hope."

    scene bg ch6_f99e88_7 at full_bg
    "THE END"
    # [GAME END]
    return
