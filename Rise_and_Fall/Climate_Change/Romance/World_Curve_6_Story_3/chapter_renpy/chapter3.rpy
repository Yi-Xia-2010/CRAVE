label chapter3:

    # [Scene: Beacon Lighthouse | Late Afternoon]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm, ascending strings with a steady rhythmic pulse — hopeful, building]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, wind tearing at banners; the lighthouse lamp pulses a slow amber]
    "You stand with the satchel heavy against your hip and the sea‑glass pendant cool at your throat. The prints and notes inside feel like a small covenant: data as promise, models as a map you cannot"
    "unwrite. The air tastes of salt and old rope; the lighthouse stone is damp under your palm when you lean against it, the texture rough and real."
    "Below, the town is a low blur of roofs and patched docks. Above, a shaft of sunlight cuts through the clouds and lays an honest, pale light over the sea. For a moment the world is"
    "only this: wind, light, the pull of water and the stubborn human noise gathered here on the ledge."
    "You can name the stakes — municipal contract hinges on one endorsement; permits and funding will follow — but naming them doesn't make them lighter. It only makes them clearer. Your responsibility feels like a hinge"
    "itself: what you choose will tilt more than policy. It will tilt livelihoods, marshes, memory."

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Muffled murmurs from the crowd; a gull cries sharply]

    "Mayor Cortez" "Thank you for coming. We don't have a lot of time before the council votes on the temporary municipal contract. Veridian Holdings has put a firm offer on the table, and we have counterproposals from within our own community. We'll need one clear endorsement to move forward. Maya—' (she looks at you with a practiced softness) '—the council has asked you to speak for the town's initiative. We're trusting your judgment."
    "You feel the gaze like the tide: steady, patient, expectant. Your tongue is dry, but not from fear; it's the dryness of someone who has rehearsed more than once in the quiet of a lab and"
    "on the edge of tidal marshes. You could speak from charts. You could speak from urgency. You could simply hand the papers over and let others carry the load."
    show elliot_chen at left:
        zoom 0.7

    elliot_chen "The hybrid living‑dike is a stepwise plan. We can pilot sections that protect the most vulnerable shorelines in months, not years. We pair engineered cores with woven coir and planting — it buys us resilience and keeps marshes functioning.' (he glances at you) 'We can stage it so people are trained and employed locally. It's not a tradeoff between safety and life; it's a design that aligns them."
    "He folds a page out toward you — diagrams of staggered cross‑sections, annotated with plant lists and sediment flow projections. The colors are gentle, the lines confident. You want to hold the cloth and trace the routes with your finger, to feel the logic born in hand."
    show noah_rhee at right:
        zoom 0.7

    noah_rhee "We don't have the luxury of dance and delay. Storm season comes and takes without asking if our 'designs' are ready. People need work now; they need nets that won't tear on rocks bisected by the last high tide. Armoring certain stretches, dredging channels where they're blocked — those are things my crew can start on next week. We don't need promises from a sketch.' (he meets your eyes; there's heat in it, not only anger) 'This town needs a roof that holds."
    "His hands are callused, one curled around the brass compass at his throat. There's a gravity to his urgency that lands in your chest. You remember the faces of the fishers, the shopkeepers stacking crates higher."
    "You remember your father's gap at the table and the blunt truth that some tools must be wielded now."
    "Across from Noah, Aria Sol's presence is all polished edges and measured color. Her tablet reflects the sky."
    show aria_sol_representative_of_veridian_holdings at center:
        zoom 0.7

    aria_sol_representative_of_veridian_holdings "Veridian Holdings can mobilize heavy equipment within days and cover the upfront costs. We propose a phased hard‑protection plan with oversight conditions negotiated by Mayor Cortez. We understand local concerns — we'll include monitoring and community labor clauses. This isn't about erasing the marsh; it's about giving the town breathing room to plan."

    "Mayor Cortez" "The company offers immediate security and a political cushion I can't ignore. But their contracts mean we cede permit control in certain zones, at least temporarily. That's the tightrope."
    "You can see the calculation in each face. Elliot's hope is scaffolding. Noah's certainty is an anchor. Aria's offer is a fast channel to safety with strings attached. There is no villainy here, only competing urgencies."
    "Your inner voice compiles the variables: immediate jobs, ecological function, long‑term community governance, the town's dignity. Guilt — as it often does — threads through your thinking: can you forgive yourself later if you choose wrong"
    "today? You steel yourself. Rising tone. You remind yourself of what has brought you to this ledge: not only grief, but a stubborn, practical love for place."

    menu:
        "Approach Elliot's sketch and ask a question":
            "You step forward and run a fingertip across the rough pencil lines. Elliot's shoulders soften; he explains the staging for the pilot in a quiet, steady voice."
        "Turn to Noah and ask about crew timelines":
            "You face Noah. He names the dates, the crew lists, the dock hands he can mobilize. The specificity calms a knot of anxiety in your chest."

    menu:
        "Ask Mayor Cortez about permit safeguards":
            "The Mayor's face eases; she outlines a provisional clause that could keep local oversight in place during the pilot phase, though it asks for political maneuvering."
        "Look directly at the assembled community and ask who needs what most":
            "A hand goes up; a fisherman speaks about immediate repairs, a shopkeeper asks about market access. Their voices slice through the abstractions and make the stakes human and immediate."

    menu:
        "I will lead Elliot’s hybrid living-dike program, combining nature-based solutions with targeted engineering.":
            jump chapter4
        "I will back Noah’s immediate protection contracts to secure livelihoods now.":
            jump chapter8
        "I accept Veridian Holdings’ phased hard-protection funding and oversight, with strict conditions.":
            jump chapter12
    return
