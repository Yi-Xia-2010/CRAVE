label chapter5:

    # [Scene: Living Seawall Site | Morning]

    scene bg ch5_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The steady slap of water against pilings, distant laughter, hammers tapping a counter‑rhythm]
    # play music "music_placeholder"  # [Music: Warm strings with a hopeful, ascending motif]
    "You stand at the lip of the work platform, boots planted on damp wood, and take in what the barrio has made of the estuary overnight. Floating modules bob in a disciplined cluster like a small,"
    "stubborn fleet. The living seawall's initial lattices are threaded with saplings and woven mats; where yesterday had been a single tentative row, there are now spans of green threading the mudflats. Each new knot is a"
    "promise."
    "The air is thick with brine and compost: citrus peels drying in the sun, the sharp whiff of seaweed, and the sweet, earthy perfume of fresh soil in plastic trays. A kid runs past carrying a"
    "coil of rope thrice his height; Teo's laugh follows, bright as a bell. For a moment the work sounds like music, all syncopated motion and shared purpose."
    "But under the steady rhythm something misses a beat. You notice the pumps — the old, jury‑rigged suction units — sputtering near the outer modules where the tides are meaner. Supply manifests as a second, quieter"
    "problem: the composite mesh you trusted would arrive by now is still not listed on the depot manifest. Your thumb drags along the inked edge of your map in your pocket until the paper softens; the"
    "motion calms you."
    "You breathe in and let the rising certainty from yesterday do its quiet work: this is worth protecting. The question is how, and how quickly."
    show mateo_teo_rivera at left:
        zoom 0.7

    mateo_teo_rivera "You see that outer anchor? It keeps sliding every high tide. We can lash it tighter, but—' (he lifts a wrench; grease dark at his knuckles) '—we need more creeper‑stakes and that mesh for reinforcement. The mesh shortfall's slowing crews on the south stretch."
    show asha_rivera at right:
        zoom 0.7

    asha_rivera "We can improvise temporary anchors. But the pumps failing is a bigger fire now. If the outer section floods and the plants drown, we lose months of work."
    "Elias Hart appears, hair damp at the nape, hands already stained with mud. He smells like the work itself: salt, sweat, the faint smoke of a cooking pit."
    show elias_hart at center:
        zoom 0.7

    elias_hart "We can requisition from the depot. People are done waiting for permits while the tide keeps moving the line. Tell them to bring the forklifts, and we'll move twice as fast. We can shore that stretch before the next swell."
    "His voice holds the warm centrifugal force it always has. Elias wants motion; he wants action now. You admire that in him — it's how things get built — but your gut pulls to the ledger, to the consequences that roll quietly behind a good idea."

    asha_rivera "Requisitioning will net supplies fast, but it risks legal repercussions. The mayor's office will have a fit if we skip protocol. And Leon's people are watching for anything that looks like chaos."

    elias_hart "Leon watches whether we move or don’t. If we stall because we're polite, people lose homes. We can't keep arguing with systems that move slower than the sea."

    asha_rivera "We won't be polite, but I don't want us to be reckless. There's a middle way if we can pull more hands, reallocate labor, and patch pumps enough to hold the line while we look for longer‑term help."
    "Elias Hart: (sharp, then softer) 'Middle ways are great for poems, Asha. But floods aren't patient.'"
    "Your doubt sits in your chest like a stone and, as always, work dissolves it — or at least shapes it into something usable."

    menu:
        "Grab the outer anchor and lead the lash team":
            "You roll up your sleeves, knot the rope beside Elias and Teo, and the labor crowd's energy swells. For a while your hands do the talking: measuring, pulling, cursing in unison. The seawall breathes steadier under the new strain."
        "Head to the pumps to trouble‑shoot the diagnostics":
            "You crouch beside a sputtering unit, fingers cold and methodical. The pump's intake is clogged with a slurry of algae and tiny plastics; you clear it, rig a crude filter, and whisper encouragement the way you whisper to failing things. It hums back to life and you feel the room loosen with the small relief of machines that behave."
        "Call Jun and inventory supplies with Teo":
            "You slide into the supply tent and, with Teo, run the manifest in the dim light. The list tightens around your chest as you realize deliveries are delayed. Jun promises to look into municipal channels and the two of you make a plan to push the data request through if needed. The plan smooths something inside you: purpose is a kind of shelter, too."

    menu:
        "Record a short testimony from Sofia at the market":
            "You walk to Skyward Market and coax Sofia into telling a concise story about a winter when her stall flooded. Her voice trembles at the edges but she finishes with a laugh about seedlings that refused to die. The clip, raw and human, fits Jun's charts like sunlight through glass."
        "Organize a midweek showcase at the boardwalk":
            "You pin a flier, text the neighborhood channels, and choose a spot where the seawall is most presentable. The idea sparks — people offer salsa, a hand with a speaker; momentum hums anew. The plan gives everyone a visible goal for the next three days."

    menu:
        "Support Elias’s direct requisition and labor mobilization.":
            jump chapter6
        "Focus resources on building airtight data and petitions with Dr. Jun to secure public funding.":
            jump chapter16
        "Open a discreet dialogue with Hana to seek conditional technical aid for pumps and composite mesh.":
            jump chapter17
    return
