label chapter9:

    # [Scene: Council Chambers / Redevelopment Pavilion | Late Morning]

    scene bg ch9_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low conversations, the whisper of camera shutters, the distant gulls cutting over the harbor. A single microphone waits at the podium like an instruction.]
    "You can still feel the shape of yesterday in the curve of your shoulder — the notebook's damp leather, the thumb that turned the silver ring when you needed a compass. Whatever path led you here,"
    "the chamber receives it the same way: as a fact with consequences. The air tastes faintly of printer ink and brewed coffee; under that is peat and sea-salt, the memory of the corridor pulled taut in"
    "your chest."
    "You move forward because movement is the only way to keep masonry from crumbling under grief. You pass Marta in the aisle. Her hair is threaded with grit but her eyes are unexpectedly bright; she squeezes"
    "your hand, hard enough to remind you that people are the work, not the paperwork."
    "Lina steps aside and meets you at the podium. Her expression is careful, pitched between relief and residual alarm. She leans in, voice low."
    show lina_voss at left:
        zoom 0.7

    lina_voss "Whatever happens in there — whatever you chose to do — we'll frame it so people hear the stakes. They need to know what can be fixed and what won't come back."
    show aria_solen at right:
        zoom 0.7

    aria_solen "They deserve both. They deserve to make that call with their eyes open."
    "Jun arrives with a printout; he sets it on the lectern and taps a confidence curve where the data levels off. His thumb leaves a damp ring."
    show jun_park at center:
        zoom 0.7

    jun_park "The model shows the living shoreline—if managed—reduces surge impact in the long run. It won't be perfect without supplementary defenses, but community stewardship lowers the ecological cost. We can buy time."
    "Caden Holt's voice comes, smooth and measured."
    hide lina_voss
    show caden_holt at left:
        zoom 0.7

    caden_holt "And the capital infusion provides immediate shelter and jobs. There's a balance to strike, Aria. You know that."
    "You sense the room tilt slightly at your name — expectation and exhaustion braided together. You breathe as if inhaling the tide."

    aria_solen "Balance isn't a ceiling. It's the floor. We keep what keeps us safe and what holds our stories. If the plan erases place, it's no victory."

    caden_holt "It's a pragmatic win. We can protect lives at scale."

    aria_solen "At what cultural cost? We aren't just a line on a map."
    "There's a pause long enough for the chamber to absorb the tide of people present — vendors, elders, council aides, a few journalists. The decision you made earlier—however it was reached—unspools here in consequences and new"
    "contracts. But the shape it takes is not only a political ledger; it's hands in mud, seedlings in palm, the slow building of trust."
    # play music "music_placeholder"  # [Music: A single ascending piano arpeggio underlines the exchange; it's hopeful without being sentimental.]
    "Lina steps in between you and Caden Holt, palms open like a mediator's offering."
    hide aria_solen
    show lina_voss at right:
        zoom 0.7

    lina_voss "There's a compromise on the table. Hybrid governance. The consortium funds a partial seawall, but co-op oversight manages the living shore. A trust will hold the reed corridor's stewardship. It'll be auditable, and the council will appoint a community liaison."

    jun_park "Scientifically defensible. We'll need long-term monitoring funds, but the metrics are viable."

    caden_holt "It's not everything either side wanted, but it's workable."
    "You let the word 'workable' settle, like a plank placed on a mudflat. It is not pristine. It is not the whole corridor, but it means reed beds will breathe again in places they might have been lost."
    hide jun_park
    show aria_solen at center:
        zoom 0.7

    aria_solen "If the trust has teeth — community-led governance, funding tied to measurable ecological outcomes, and a seat for vendors and elders — then we can call that progress."
    "Caden Holt studies your face, then nods. Lina's expression loosens a degree."

    caden_holt "We'll draw the language. Allow for community vetoes on relocations and put the monitoring panels in the charter."
    hide caden_holt
    show jun_park at left:
        zoom 0.7

    jun_park "And emergency repair funds will be codified. No political footnote."
    "You inhale, feeling something uncoil in your chest — not victory, but relief. The corridor will live in pieces. The people won't all be displaced. It is not the whole you wanted when you began; it is a scaffold you can build from."
    # play sound "sfx_placeholder"  # [Sound: A scattered round of low applause. It is tentative, human, like scaffolding being tested.]
    "You step away from the podium into the press of bodies. Reporters ask for a sentence; a camera light glares cold. You think of the child at the market yesterday, of Jun's thin patience with numbers,"
    "of Rafi's weathered hands that map tidal memory. You pick words that won't flinch but will give breathing room."

    aria_solen "This isn't the end of hard choices. It is a start. We will steward the shoreline together."

    menu:
        "Reach for Jun’s shoulder in the crowd":
            "Your hand finds his sleeve; he looks surprised, then smiles the small, weary smile of a colleague who has seen late-night data turn into real shorelines. It costs you nothing to be human here."
        "Step toward the exit and breathe alone":
            "You walk to the doorway, the rain-slick glass pulling the world into softened shapes. For a few seconds you let the salt wind take the edge off your teeth. Solitude cushions the next step."

    menu:
        "Take his hand, briefly":
            "Your fingers curl around his; it's a small, steadying weight. The market hums around you and for a second the work and the world and the two of you are aligned."
        "Let the moment be wordless and walk away with a nod":
            "You nod and tuck the seed packet into your pocket instead of taking his hand. It's a promise wrapped in motion — practical, intentional, and not polished. He watches you go with an unreadable look."
    "THE END"
    # [GAME END]
    return
