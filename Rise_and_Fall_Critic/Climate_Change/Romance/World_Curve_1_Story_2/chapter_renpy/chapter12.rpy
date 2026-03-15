label chapter12:

    # [Scene: Greenhouse Rooftop Lab | Midday]

    scene bg ch12_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft clatter of tools, low conversation, the hiss of a hydroponic misting system]
    # play music "music_placeholder"  # [Music: Steady, ascending strings]
    "You sit on the edge of a workbench, the ledger heavy in your jacket pocket. The leather presses against your ribs like a quiet, patient pulse — a list of names, commitments, and the town's small"
    "mathematics of survival. Around you, hands plant, stitch, and tally. The greenhouse smells of salt-tinted earth and warm metal, of algae jars and coffee gone cold on the windowsill."
    "You breathe in. The inhale tastes of a hundred small agreements: Jun's steady nods, Riv's frantic flyers, Elias's experimental seawater blends. You feel the cooperative as a thing you can touch now — rope-braided and human-warmed."

    scene bg ch12_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A soft laugh from the corner; someone hums an old sea shanty off-key]
    show mayor_amina_bakar at left:
        zoom 0.7

    mayor_amina_bakar "Mika. Or —' (she smiles, then corrects) '— you. The town called you the convenor long before the council did."
    show mika_hoshino at right:
        zoom 0.7

    mika_hoshino "We called ourselves a lot of things, Mayor. Convener. Cook. Band-aid. Today, we're trying 'coop'."

    mayor_amina_bakar "The council met this morning. They saw the photos. They saw the turnout. The matches are fast-tracked. I did what I could.' (Her voice is warm but tight.) 'It wasn't just me. It was your ledger — the numbers made it harder to ignore the human part."
    "You feel your throat thin. Data does strange things in town halls; tonight, it returned with hands attached."
    hide mayor_amina_bakar
    hide mika_hoshino

    scene bg ch12_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft scrape of notebook against pocket]
    # play music "music_placeholder"  # [Music: A gentle swell underlines the exchange]
    show elias_maren at left:
        zoom 0.7

    elias_maren "You shouldn't have carried that all by yourself. We—' (he pauses, searching for the right word) '—we carried it with you. Jun made sure the floats were seaworthy; Riv's been talking to the apprentices; I ran the pilot's yield estimates again. The kelp's doing better than I dared expect."
    show mika_hoshino at right:
        zoom 0.7

    mika_hoshino "You did what you do, Elias. You showed people the kelp beds and they stopped seeing a problem and started seeing a living solution."

    elias_maren "It helps having a workshop that smells like home and someone who can turn a plan into a plank. Your mother would've liked this."
    "You feel the memory arrive like a wave: your mother's voice over sanded planks, the clink of metal in the old toolbox. For a moment you are a child again, measuring tide marks with sticky fingers. Then the present reasserts itself — busy, bright, and full of others."
    show jun_park at center:
        zoom 0.7

    jun_park "All right, boss of patched jackets—' (he winks at you) '—we need to choose where the shipment lands tonight. Boardwalk or lower dock."
    hide elias_maren
    show ravi_riv_delgado at left:
        zoom 0.7

    ravi_riv_delgado "And the apprentices are ready for stage practice. If we run the harvest demonstration tonight, the funders on the call will see people actually lifting the yield. It's visceral."
    hide mika_hoshino
    show mayor_amina_bakar at right:
        zoom 0.7

    mayor_amina_bakar "Whether it was direct action, policy, or that staged harvest you did last month—doesn't matter. The thing is visible. I can match funds, fast. We can draft cooperative land leases this week. The way forward is institutionalized now."
    "You listen to Amina and feel an odd, buoyant disbelief: talk turned to action; action turned to policy. The greenhouse hums like a heart, steady and rising."

    menu:
        "Volunteer to coordinate the evening landing":
            "You push off the workbench, palms dusted with peat, and point to the map tacked on the wall. You mark the boardwalk with a quick, certain hand—this is where the town will see our harvest swing low against lanterns. Jun nods approval, slipping a rope into your palm, and the plan becomes a thing you can shoulder."
        "Stay and finish the seed trays":
            "You gather the seedlings into your arms, cradling them like small truths. 'Go on without me,' you tell them. 'I'll bring the next batch.' Elias presses a grateful hand to your shoulder; the greenhouse stays your domain tonight, a private work that will ripple outward tomorrow."

    # --- merge ---
    "The momentary choice — to be the hand that lands the shipment or the hand that tends the next generation — feels less like a fork and more like selecting which chord to strike in the same song."
    "You watch the cooperative's mechanics weave themselves; decisions are made by people whose names you trust."
    # [Scene: Boardwalk & Harbor | Dusk]
    hide jun_park
    hide ravi_riv_delgado
    hide mayor_amina_bakar

    scene bg ch12_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wooden planks sighing, laughter, the distant thunk of crate ropes]
    # play music "music_placeholder"  # [Music: Warm strings, rising to a hopeful cadence]
    "You walk the boardwalk as twilight folds the harbor into soft ink. Lantern light collects in puddles and in the faces of neighbors who have come with hot bread, with hands ready to lift, with skepticism"
    "folded down to waiting curiosity. The staged harvest — or what some call a demonstration of what community labor can do — is a citizen-made spectacle: neat rows of kelp-laden crates, apprentices with callused palms, and"
    "a small ribbon of people who know how to tell stories without gloss."

    scene bg ch12_f99e88_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A murmur of commentary; the faint digital ping of incoming messages]
    "You speak briefly to a camera — but more to the people behind it. Your voice is the voice of someone who has mended nets at dawn and stayed up late to tally hours. You say"
    "what you always wanted said: that resilience is made with labor that is shared, with knowledge passed down, and with land that is held by those who will steward it."
    show mika_hoshino at left:
        zoom 0.7

    mika_hoshino "This isn't a charity model. It's our sea and our work. We keep the kelp, we train the apprentices, and we set a price that pays people a living. We keep the leases communal so the benefits don't drift away."

    "A Mayor's aide" "You have the paperwork to make those leases legally binding?"

    mika_hoshino "We do. We have signatures. We have a plan. We have neighbors who will hold each other to it."
    show elias_maren at right:
        zoom 0.7

    elias_maren "You were a force today. You held them with a sentence."

    mika_hoshino "You held them with kelp."

    menu:
        "Sit beside Elias at the long communal table":
            "You accept his quiet. You sit, your patched sleeve nearly brushing his, and you talk about the days to come — training modules, yield estimates, a greenhouse schedule that fits both tending and tenderness. He listens, asks small, intimate questions about your mother's tools, and each answer feels like a knot tightened in a net that holds the two of you together."
        "Stand and address the gathered volunteers":
            "You rise, raise your hands a little, and the room quiets. 'Tonight is the first of many,' you tell them. You lay out the volunteer rotations and the training program. People nod, eyes bright. Jun claps the loudest. When you sit again, Elias catches your sleeve and squeezes, and the warmth travels up your arm like a promise."

    # --- merge ---
    "The meal is a long, luminous thing. Lanterns turn the harbor into a shallow pool of light, and faces are softened at the edges."
    "The meal is a long, luminous thing. Lanterns turn the harbor into a shallow pool of light, and faces are softened at the edges. Someone brings out paper plates lined with kelp crisps and stew, a"
    "collision of old recipes and new harvest. Children chase a stray dog along the boardwalk; an elder tells a joke about a storm that once took half the pier and left the other half stubborn."
    show mayor_amina_bakar at center:
        zoom 0.7

    mayor_amina_bakar "To the cooperative. To the people who made the town stop treating its future like an expense and start treating it like an inheritance."
    "Crowd [murmurs into louder cheer]"
    "You watch the clinking cups and feel something settle into your bones. It's not a finality — nothing in this era is final — but it is the sense of a plan that will persist beyond one of you. It is policy made by hands, not just speeches."

    elias_maren "Do you ever think... about leaving? About taking this somewhere bigger?"

    mika_hoshino "Sometimes. But then I remember the way the kelp moves in the water and how Jun laughs when a crate won't fit the truck. I remember my mother's key, and the workshops we've kept alive with elbow grease and stubbornness. This is where I chose to stay."

    elias_maren "Then I'm glad you did."
    "You feel the cooperative's success as a physical warmth: more apprentices in training, a schedule so tight it is like music, the town's economy tangibly shifting. Training programs are in the works — apprentices earning stipends,"
    "shared harvesting incomes circulating through local shops. Amina's signature is already on documents that will anchor cooperative land leases. The mayor's support is not the end but a scaffolding."
    hide mika_hoshino
    show jun_park at left:
        zoom 0.7

    jun_park "You still wear that jacket like a medal."
    "You laugh. You touch the patched elbow where your mother's initials are faint. Someone takes your picture — not for a headline, but for the cooperative's bulletin board — and you think of the ledger's iron weight in your pocket, lighter now because it is shared."
    hide elias_maren
    hide mayor_amina_bakar
    hide jun_park

    scene bg ch12_f99e88_6 at full_bg
    # play music "music_placeholder"  # [Music: Strings swell into a bright, expectant motif]
    "Night presses in, but the lanterns hold a soft, steady orbit. You step away from the table for a moment and stand by the railing, looking at the harbor. The water mirrors the lights and the promise of further work: a pattern of small, connected reflections."
    "Your internal voice catalogues not only what has been won but what remains: rules to finalize, apprentices to guide, maintenance schedules that will test patience, and the slow, patient work of keeping power local. The cooperative"
    "has muscles now — governance structures, matched funds, a legal scaffolding — but like any muscle it will require tending."
    show elias_maren at left:
        zoom 0.7

    elias_maren "Whatever comes next, we'll keep making it. Together?"
    show mika_hoshino at right:
        zoom 0.7

    mika_hoshino "Together."
    hide elias_maren
    hide mika_hoshino

    scene bg ch12_f99e88_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Laughter, soft conversation, the distant lapping of water]
    # play music "music_placeholder"  # [Music: Strings resolve into a warm, ascending chord]
    "You are recognized now — not as a celebrity, but as someone the town trusts to convene, to hold ledger and ledger-keepers alike. You still wear your patched jacket; you still tend the greenhouse at odd"
    "hours. The dented metal key is still in your pocket. You are, in equal measure, a leader and a neighbor."
    "There is a sweetness in knowing that love and duty are braided: the tug of tending another's hand and the tug of tending the commons have become one. What you build will not fix every scar"
    "left by the seas, but it will give the town tools to weather them, and a way to pass those tools on."

    scene bg ch12_f99e88_8 at full_bg
    # play music "music_placeholder"  # [Music: Gentle coda, rising gently]
    "You let the night carry the warmth into the harbor. The cooperative hums behind you like a living thing. Your mother’s key, the ledger, the greenhouse, the boardwalk laughter — they feel like threads in a net you now help hold taut."
    "You look up at the stars and pretend they are lanterns pulled low so the town can reach them. When the work begins at dawn, there will be more to do. But for now, there is"
    "a long table, a shared meal, and the quiet, rising certainty that the town's future is something you can keep shaping — together."
    # [Scene: Boardwalk | Night — Final]

    scene bg ch12_f99e88_9 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The last chair being pushed under a table; a distant gull; soft footsteps on wet wood]
    # play music "music_placeholder"  # [Music: Soft, sustained strings with a hopeful shimmer]
    "You fold your hands around the rim of your cup and feel the life of the town settle into a rhythm that includes you: leadership that still laughs, governance that still needs elbow grease, love that"
    "blooms between tide checks and training sessions. This is not a tidy victory; it is a living thing. It will need tending. You nod to that promise and to the people beside you."
    "You step back into the lane toward your greenhouse, Elias gently at your side, a future that is both intimate and civic pressing forward. Lantern light pools at your feet. The harbor breathes, the kelp beds wait, and the cooperative — braided, rooted, and stubbornly hopeful — begins another day."

    scene bg ch12_f99e88_10 at full_bg
    "THE END"
    # [GAME END]
    return
