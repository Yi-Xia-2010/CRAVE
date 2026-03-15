label chapter3:

    # [Scene: Old Estuary Boardwalk | Morning]

    scene bg ch3_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant mechanical sigh of pumps, vendors tuning stalls, a gull calling once and dropping away]
    # play music "music_placeholder"  # [Music: Warm strings with a bright, steady rhythm — hopeful, gathering momentum]
    "You walk with purpose. The cutting in your pack presses reassuringly against your ribs — a tiny green proof that living things still matter in bureaucratic rooms. Elias Hart matches your pace, voice low but steady"
    "as he runs through the opening lines one last time. His words are loose, passionate, and they vibrate against the careful logic you've been rehearsing in the lab all week."
    show elias_hart at left:
        zoom 0.7

    elias_hart "Start with the people, then hit them with the plan. Faces first, pipes second. Make them feel why this matters."
    "You listen and weigh his cadence against the rows of charts and algae samples waiting at Tideworks. Hana Kim will want lean data and measurable outcomes; Leon Voss will want numbers and deliverables. But Elias Hart"
    "— and the market folk and Teo’s teams — will bring the hands that build what you design."
    show asha_rivera at right:
        zoom 0.7

    asha_rivera "We open with the market. Sofia's story. Then the living seawall schematic. Short, human, then technical."

    elias_hart "Perfect. They'll remember Sofia before they remember flood maps."
    "The air between you and Elias Hart is complex — the past threaded through present purpose. You tuck that into the corners of your mouth and turn the conversation outward. The boardwalk smells like roasted corn and seawater; your palms are warm from the grip of your notebook."

    menu:
        "Quiet your voice and recite the opening lines like a practiced script":
            "You close your eyes for a breath, feeling each syllable settle. Rehearsed cadence gives you armor, and the words sit sharp and ready on your tongue."
        "Tell the personal anecdote about Sofia first, letting your voice catch on the emotion":
            "You let the memory of Sofia rise — the way she held a wilted seed packet like a promise. Your voice roughens; emotion makes the room you imagine fuller."

    # --- merge ---
    "..."

    elias_hart "Either way, don't let them drown out the names. They've got to hear the people."
    "You cross from the salt-scented fringe of the estuary toward the municipal building. The city seems to hold its breath with you — a quiet confidence that small, stubborn things can still matter. You climb the steps into the Council Room, the sunlight folding into glass and polished wood."
    # [Scene: Council Room | Morning]
    hide elias_hart
    hide asha_rivera

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low murmur, the rustle of program sheets; someone resettles a child on a lap]
    # play music "music_placeholder"  # [Music: A gentle uplift — piano arpeggios twining with the strings]
    "Mayor Lila sits at the center of the dais, laminated schedule visible as always. Her expression is taut with the weight of schedules and promises, but when she looks at you there's something like openness there — not trust yet, but the possibility of it."
    show mayor_lila_ortega at left:
        zoom 0.7

    mayor_lila_ortega "Ms. Rivera. The council has read your briefing. For the record, we expect succinct proposals. You have the floor."
    "You set your notebook on the lectern and feel the eyes of your neighborhood land on you like a tide. Sofia sits two rows back, apron folded neatly, her hands worrying a seed packet in a"
    "slow, steady rhythm. Hana Kim is at the table to your right, an AR monocle catching the light, a calm stack of slides glowing faintly. Leon Voss is on the opposite side, suit impeccable, smile contained."
    show hana_kim at right:
        zoom 0.7

    hana_kim "Mayor. We'll show modelled outcomes for engineered barriers and a cost-benefit analysis for phased microgrids. They're scalable and minimize displacement."
    "Elias Hart leans forward in the audience and calls out, his voice threaded with fervor rather than presentation polish."
    show elias_hart at center:
        zoom 0.7

    elias_hart "We don't need to wait for another study. People here have already built defenses that work with the tide. Give them the permits, give them supplies, and they'll do it."

    mayor_lila_ortega "Both sides have valid points. This council needs a clear recommendation. Ms. Rivera, how do you reconcile community action with engineered resilience?"
    "You inhale. The room narrows to the lectern and to all the faces that brought you here. You think of Jun's data that nudges your plans toward measurable outcomes, of Teo's hands rebuilding pilings at dawn,"
    "of the living seawall prototypes with their salt-tolerant plantings. You also think of Hana Kim's quiet competence and Leon Voss's dangerous generosity."
    hide mayor_lila_ortega
    show asha_rivera at left:
        zoom 0.7

    asha_rivera "We reconcile them by remembering that durability isn't just engineering — it's people. A living seawall seeded by neighbors, informed by sensor feedback, and backed by targeted funding can be both rooted and scalable."

    hana_kim "Asha, what I can offer is precise: sensor arrays that measure erosion in real time, modular pumps that engage during extreme tides, and a pilot budget to test performance within six months. We'll put community oversight in writing."

    elias_hart "And who writes the oversight? A clause in a contract? We need people building, not bureaucrats approving. Trust is forged by work, not legalese."
    hide hana_kim
    show leon_voss at right:
        zoom 0.7

    leon_voss "Our firm is committed to transparent reporting. We can fast-track materials and logistical support. Public-private partnership is how cities scale protection without bankrupting them."
    hide elias_hart
    show sofia_navarro at center:
        zoom 0.7

    sofia_navarro "My cousin's house flooded twice last year. If a trained engineer can stop that, I'll listen. But if it means our walkways move and we can't find each other's doors anymore, that's not protection — that's erasure."
    "Mayor Lila watches the exchange with small, calculating nods. Her hands fold around a pen; her schedule is a map she must not ignore."
    hide asha_rivera
    show mayor_lila_ortega at left:
        zoom 0.7

    mayor_lila_ortega "Ms. Rivera, Ms. Kim, Mr. Hart — the city needs something actionable this quarter. Politics moves on timelines. Convince me of a path that protects people and keeps our neighborhoods whole."
    "Hana Kim's gaze toward you is precise and, for a flicker, unreadable — the old friendship between you and her is compressed into professional edges. Elias Hart's eyes are direct, searching for the tether of shared conviction. Neither look resolves your history; both press you toward your responsibility."
    "You feel the room's energy tilt toward possibility. People here have shown up. Sofia's seeds are folded into another layer of hope. The data can be convincing; the people's work can be powerful. You find your voice again, steadier and warmer."
    hide leon_voss
    show asha_rivera at right:
        zoom 0.7

    asha_rivera "Mayor, we can pilot living seawalls in the next two neighborhoods most at risk. We'll train and employ local crews — Teo and the community can do the hands-on work — while Hana Kim’s team installs a limited sensor array and provides maintenance training. We can commit to community oversight, shared metrics, and a public dashboard updated weekly. If the pilot meets agreed benchmarks, the program scales."
    hide sofia_navarro
    show hana_kim at center:
        zoom 0.7

    hana_kim "Those benchmarks can be scientific and social. I won't let success be measured only by numbers."
    hide mayor_lila_ortega
    show elias_hart at left:
        zoom 0.7

    elias_hart "If the community builds it, the community should lead the work. But we need materials faster than donations can gather."
    hide asha_rivera
    show leon_voss at right:
        zoom 0.7

    leon_voss "We can front materials for a single pilot site and provide logistics. In exchange, the city acknowledges our role in the initial phase."
    hide hana_kim
    show mayor_lila_ortega at center:
        zoom 0.7

    mayor_lila_ortega "Public acknowledgement is not the same as ceding control. I want guarantees — contracts, timelines, and a clarity on who holds the authority during emergencies."
    "An uneasy murmur ripples. Contracts, timelines — the language that organizes a city's response — feel at once necessary and chilling."
    "You remember Jun's advice about measurable outcomes: choose metrics that honor the community's lived experience as much as the engineering models. You think of the cutting against your ribs, and how small things can be proof."

    menu:
        "Emphasize the human-story benchmark — displacement and daily access — over raw erosion averages":
            "You choose to make the pilot's success tangible: families staying in their homes, walkways intact, markets open. Faces matter as much as millimeters of shoreline saved."
        "Lean into combined metrics: erosion rate reduction paired with employment numbers and weekly dashboard transparency":
            "You propose a hybrid rubric. Engineers will like the numbers; the community gets verifiable assurances. It sounds like compromise, but it feels like protection."

    # --- merge ---
    "..."
    "Mayor Lila's fingers drum a soft cadence on the table. She looks out, briefly, at the gallery full of neighbors. There is a warmth in the room now — people who could have stayed angered and instead leaned in to be present. That warmth hums with possibility."

    mayor_lila_ortega "I can take a recommendation to the council if it's specific and if the community endorses it publicly. Ms. Rivera — you stand at the center of these approaches. I need to know where you'll put your voice."
    "The question lands like a marker on a map. This is not an accusation — it's a practical pressing. Your heart thuds, but it is a steady sound: the same pulse that carried you out of the lab and across the boardwalk."
    "You look at Hana Kim. Her face is composed, a matrix of professional care and something quietly hopeful. You look at Elias Hart; his hands are clenching and unclenching, the sign of someone holding excitement and"
    "restraint at the same time. You see Sofia flattening the seed packet, eyes bright with trust."
    "The room waits. The possibility of a path that protects both people and place hangs in the air like morning mist about to be traversed by sunlight."
    hide elias_hart
    show asha_rivera at left:
        zoom 0.7

    asha_rivera "Mayor — before I answer, I want this to be a moment where the city sees that options can be braided together. We don't have to choose loss as the price of safety. But I also won't offer a half‑measure that leaves anyone exposed."

    mayor_lila_ortega "Then give me the recommendation that you're prepared to champion publicly. The council will expect clarity."
    "Your pulse quickens with something like hope — uncomfortable, bright. The council room feels suddenly smaller, focused; outside, the harbor continues to breathe. This is the kind of pressure that can forge new things: laws, alliances, and hard-won compromise."
    "You know there are three distinct paths you could champion — each with its own risks and promises. The mayor's pen hovers, the people around you hold their breath, and the hope in the room tightens into something actionable."
    # [Page-Turn Moment: You hear, for an instant, the chorus of the barrio — Teo's tools, Sofia's laugh, the rustle of market awnings — and realize that whatever you choose will ripple outward. This is not the end of debate but the moment where debate becomes policy. Your next words will set the direction; the city leans closer.]

    menu:
        "Stand with Elias and prioritize grassroots mobilization and community-built living seawalls.":
            jump chapter4
        "Negotiate with Hana to pilot engineered adaptive infrastructure under strict community oversight.":
            jump chapter8
        "Propose a hybrid pact: seek mayoral backing to pilot a small cooperative pairing community seawalls with selective Aegis tech.":
            jump chapter12
    return
