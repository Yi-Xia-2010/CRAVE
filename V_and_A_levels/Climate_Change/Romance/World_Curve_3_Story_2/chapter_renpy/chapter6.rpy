label chapter6:

    # [Scene: Saltmarsh Wetlands | Morning]

    scene bg ch6_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A chorus of work — hammers tapping, voices calling, a gull that sounds like laughter. Water murmurs through channels.]
    # play music "music_placeholder"  # [Music: Bright, urgent strings driving forward; a triumphant brass motif underneath.]
    "You step into the saltmarsh and the air hits you — cold and sharp with salt, warmed at the edges by the thin sun. The storm's teeth are still visible in the broken stakes and the"
    "line of seaweed, but there is also movement that did not exist yesterday: hands at work, faces lit with purpose, a dozen small repairs sewing the place back together."
    "Your boots sink into spongy ground; the smell of peat and wet wood lifts with each breath. A volunteer lifts a sod bundle, laughing as she curses at the mud; the sound is immediate and human and stitches itself into the place."
    "You look at the living breakwaters — the woven oyster cages and planted reed ribs — and in some places they have taken the worst of the surf, bending but holding. In others, the sea found"
    "weak spots and tore gaps you hadn't foreseen. The results are not perfect. They are not complete. They are unmistakably real."
    "Prof. Noor is there, hair damp from fog, cheeks flushed. She hands you a moist printout: a before-and-after thermal map, a scatter of turbidity measurements, photos taken by volunteers that trace the wave run-up. The data sits in your palm like a small, brilliant thing."
    show prof_noor_azizi at left:
        zoom 0.7

    prof_noor_azizi "Look at the differential here. Where we anchored the beds and the reef ribs to the substrate, wave energy drops by thirty to forty percent. That's not anecdote — it's measurable change."
    show maya_soler at right:
        zoom 0.7

    maya_soler "And the places that failed?"

    prof_noor_azizi "We misjudged orientation. Anchors shifted where the seabed had been scoured. That's fixable. It means smarter siting, not abandonment."
    "You feel your chest rise fast, adrenaline and relief braided together. The urgency of the last days — the council, the meetings, Elias's presentations — presses behind your ribs like a heartbeat. The marsh feels both fragile and ferocious, like the town itself."

    menu:
        "Kneel to inspect a partially upheld reef rib":
            "You crouch, fingers cold, and find one of the oysters clinging stubbornly. The barnacles are alive; a small crab makes a dash. For a second the science is tactile and immediate."
        "Call the volunteer photographer over and ask for more shots":
            "You wave over Lila with the drone photos. Her fingers move fast across the screen; she grins. 'This will turn faces in the council chamber,' she says, and you nod, feeling the weight of proof shifting toward action."

    # --- merge ---
    "You rise and walk the line where the marsh meets repair work. Volunteers pass you bundles; a woman tucks a wool cap under your braid without ceremony. The sound of a small radio plays a tinny"
    "update from the boardwalk: council meeting in session, Elias is speaking. The marsh thrums with expectancy, and your throat tightens with very nearly moving into speech — into an argument, into a plea, into a promise."
    # [Scene Transition: The boardwalk is a streak of human warmth against the glittering water. Light slants, glances off chrome and wet planks.]
    # [Scene: Elara Boardwalk / Council Annex (Outside) | Late Morning]
    hide prof_noor_azizi
    hide maya_soler

    scene bg ch6_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmurs swell into a roar, then collapse into attention as the council reconvenes.]
    # play music "music_placeholder"  # [Music: Crescendo — high strings and snare, a moment of theatrical hush, then a forward surge.]
    "The annex doors open and you step into a corridor that smells of coffee and wet wool. You carry prints, notes, the worn edge of your notebook folded under your arm. The chamber is full —"
    "Ben Harper at the front with a hand on his cap, Rosa with a stack of petitions, fishermen with salt on their sleeves. The weight of the room is a thing you can name now: evidence,"
    "anger, hope, work."
    show elias_voss at left:
        zoom 0.7

    elias_voss "—we all want what is best for Elara. We will build defenses that give us certainty. I hear the community, and I am prepared to adjust the timeline."
    "There is a beat — a sharp, electric silence. He meets your eyes, and for a moment the sheen on his voice cracks into something almost human."
    show maya_soler at right:
        zoom 0.7

    maya_soler "You mean a hybrid approach? Targeted hard defenses where modeling shows clear risk, and living breakwaters where the community relies on access and culture?"

    elias_voss "Yes. With a phased redevelopment that includes support for local businesses during transition. We will seed funds for wetland restoration, and include community committees for siting."
    "Prof. Noor, stepping forward, doesn't let the concession sit as mere words. She speaks fast, precise, brimmed with a joy that is scientific and political all at once."
    show prof_noor_azizi at center:
        zoom 0.7

    prof_noor_azizi "If we map the geodata with community knowledge — fishermen routes, historical scours — we can site engineered spines where engineering is necessary, and living structures along access corridors. The pilot shows it's effective when sited. We can scale from there."

    "Councilmember Diaz" "Ms. Soler, seeing the evidence and the community's work, the council moves to approve a hybrid plan — a combined strategy of targeted seawall reinforcement and living breakwaters, with mandated local oversight and interim economic support for affected businesses."
    "A cheer rises — not a frenzy, but a thunder of released breath. The council vote is recorded; the motion carries. People are clapping, some weeping, others hugging. Ben Harper slaps Elias on the back with"
    "a force that is affectionate and final. Rosa squeezes your hand so hard you feel the familiar spark of shared history."

    elias_voss "I'll hold the development to a phased plan. We fund local storefront resiliency as I promised. We will build with Elara, not over it."
    "You watch the exchange, and the city of your chest unknots. The triumph isn't gilded; it is full of small stipulations and compromises, and that is exactly what you wanted. The pilot's evidence has become more"
    "than charts — it is the town, standing and working and refusing to be erased."
    # play sound "sfx_placeholder"  # [Sound: The gulls above seem to shout approval. The brass motif swells, then folds into a warm, low chord.]

    menu:
        "Step into the crowd to thank Noor and the volunteers":
            "You push through and clasp hands with the people who stayed up all night tying shims and hauling bagged sand. Their gratitude is immediate and wet; you feel the town's heartbeat under your palms."
        "Stay by the annex steps and watch Elias from a distance":
            "You wait a moment longer, letting the concession register. Elias notices you looking and inclines his head; you give him no more than a nod. It is an acknowledgment that neither of you will forget what brought you here."

    # --- merge ---
    "You feel the world tilt forward. The plan is approved. Elias has conceded in public. It is not a surrender so much as a choreography of necessities, and within that choreography, the tools to keep Elara alive have been preserved."
    # [Scene Transition: The reclaimed edge — where boardwalk meets marsh, where new steps and access points have been carved between the reeds — glows in late morning.]
    # [Scene: Reclaimed Edge | Midday]
    hide elias_voss
    hide maya_soler
    hide prof_noor_azizi

    scene bg ch6_4001e7_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The sea is a steady bass, a heartbeat. Laughter and soft talk roll in a human tide.]
    # play music "music_placeholder"  # [Music: Intimate strings with a rising, celebratory pulse; a single flute threads the melody of the sea.]
    "Aiden Kuro is there before you realize you want him to be. He stands with an arm slung over a bundle of new rope, amber eyes bright with salt and sunlight. His rope bracelet glints. He"
    "looks like he always has — steady and practical — and yet something about his shoulders is looser, as if relief has unpacked from him and settled into place."
    "You approach, and the air between you is electric and warm, full of unsaid apologies and small victories. The town is alive behind you; people pass with plates of baked bread, and the smell rising is domestic and holy."
    show aiden_kuro at left:
        zoom 0.7

    aiden_kuro "I was afraid, Maya. I kept thinking—what if we fixed the shoreline and lost the pier? What if promises came like paper and blew away?"
    show maya_soler at right:
        zoom 0.7

    maya_soler "I thought about that, too. And about your boats. About Ben's cap and the bakery on Dock One. We didn't have to be right on everything. We had to make sure the things that keep people breathing—work, access, memory—weren't collateral."

    aiden_kuro "I saw the crews out in the wet at dawn. I saw you directing people, barefoot in the mud. I was so stubborn I couldn't see how proud I was going to be. I—' He trails off, then smiles in a way that makes light bend. '—I was afraid of losing what I knew. Now I'm proud to help keep it."
    "You swallow, the guilt that has been a small stone in your chest all these years loosening its hold but not falling away. It is still there as a reminder, but light has started to move through it."

    maya_soler "We both gave and held. You helped reroute the fishing schedules so small boats can use the new inlets at low tide. I fought for local bidding on restoration work so contractors from Elara get the work. We'll keep monitoring. We'll keep changing things when the data says to."
    "Aiden Kuro's hand finds yours — rough, sun-browned, callused — and the contact is electric in a clean, honest way. The rope bracelet catches the light; a thin strand of salt crusts the woven fibers."

    aiden_kuro "Promise me we'll keep listening. Not only to the sea's charts, but to each other."
    "You feel the ocean as if it were a living thing between you two, alive with possibility. You nod, the motion small, total."

    maya_soler "I promise. And I'll bring you more than charts — I'll bring the whole town's voice. We'll make space for the fishermen and the bakers and the kids who climb on the breakwater. We'll make it ours."
    "He laughs, a sound like wind through the rigging. 'Good. Because I'm not going anywhere.'"
    "You laugh back, and the sound elasticates, pulling in the people around you. The sun warms the damp wood, the smell of baked bread drifts from the café, the marsh reeds whisper, and for a breath — for a long, golden breath — everything in Elara seems arranged with intention."
    "Prof. Noor approaches, carrying a thermos; her eyes are bright. Elias stands a little way off, talking to Ben in a voice that is finally ordinary. The town moves like a choir, not without cracks, but singing together."
    show prof_noor_azizi at center:
        zoom 0.7

    prof_noor_azizi "We did the science, you did the people work, and the town did the rest. This is how adaptation looks: messy, human, directional."

    maya_soler "It still costs. There are repairs and losses to tally."

    prof_noor_azizi "Yes. But the ledger is shared now. It's not your burden alone."
    "You feel gratitude, a fierce, almost dizzying thing, sweep across you. The heavy guilt that once made you build walls around yourself begins to soften into something else: responsibility shared, love redistributed. You are not the only hand on the wheel."
    "Aiden Kuro leans his forehead briefly against yours, salt and sun on his skin. The contact is small but sacred."

    aiden_kuro "Maya—when I saw those kids today, running along the new access points, I thought maybe there's a different kind of inheritance we can leave them."

    maya_soler "A sea that changes but a town that learns with it."
    "He smiles, and you both look out across the marsh — the repaired ribs in their places, volunteers now turning to build community tables, bakers setting loaves on the boardwalk rail to cool."
    "You breathe in; wet wood, salt, baked bread, the faint chemical tang of repair glue. The future is not a clean victory; it is a long, stitched thing. But it is a future you will meet"
    "not in the solitude of guilt, but in the company of people you love and who love this place as fiercely as you do."
    "You feel the arousal of the morning settle into something like jubilant endurance — a steady, energizing pulse that says this is only the beginning of the work, but the beginning is lit."
    hide aiden_kuro
    hide maya_soler
    hide prof_noor_azizi

    scene bg ch6_4001e7_4 at full_bg
    # play music "music_placeholder"  # [Music: Release — full strings and choir-like harmonics carrying the feeling of triumph and communal resolve.]
    "You close your eyes for a second and let the moment hold. This is not the end of storms, but it is the end of being alone against them. You and Aiden, the town, Noor, Ben, Rosa — you are a net now, stitched of many hands."
    "You open your eyes and smile. The guilt doesn't vanish. It won't in a single day. But the weight eases into a manageable thing — a compass rather than an anchor."

    scene bg ch6_4001e7_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A bell from the café; a child's shout as they chase a gull.]
    # play music "music_placeholder"  # [Music: Final chord — bright, sustained, and resolving.]

    scene bg ch6_4001e7_6 at full_bg
    "THE END"
    # [GAME END]
    return
