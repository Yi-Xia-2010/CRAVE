label chapter5:

    # [Scene: Tidal Flats | Night — Storm Watch]

    scene bg ch5_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low diesel rumble, distant gulls, a pulsing pile-driver beat far off]
    # play music "music_placeholder"  # [Music: Tense percussion, rising in measured staccato]
    "You inhale. The air tastes like iron and salt and the faint oil-sour of machinery. The rope you grip is slick with sea-spray; it vibrates faintly through your palms as if answering the distant hammering. Around"
    "you, faces are maps of strain: Kai's jaw clenched, Amalia's knuckles white around a clipboard, Old Tom's mouth a thin line against the wind. Mika stands on a crate, throat tight, fingers working a handheld drone"
    "controller as if the controls might be another kind of prayer."
    "You think of the forecast on your phone: squall in forty-eight hours, maybe less. You think of the seedlings under glass, of the seedbank that smells of brine and green rot, of the cooperative's first long-line"
    "already tied into the mud like a promise. Your buoy pendant rests against your sternum beneath your sweater, a small, cold presence. Your chest feels full of small, hard things."
    show kaori_kai_matsuda at left:
        zoom 0.7

    kaori_kai_matsuda "They've brought in another crew. Pile-driving's gone from scheduled to frantic. They're trying to set the girders before the storm — no permits, no community input; just speed. We can't let them make rubble of the flats."
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "We can't let them trash the trial lines either. Those long-lines are the proof—if we lose them, we lose the leverage that gets people to listen next season."

    kaori_kai_matsuda "Then we hold. All of us. We swell the line, we make it impossible to work. We make the cameras show not empty mud but bodies."

    marina_reyes "Bodies that could be injured. Machines don't stop for photographs. If the company calls enforcement and someone gets hurt—"

    kaori_kai_matsuda "And if we stand down, what then? They'll set the wall and call it progress. They'll bulldoze families out the next time the tide comes higher. This is immediate. This is now."
    "The wind tries to push words out of your mouth. You find yourself answering with a different voice—one that already sounds like compromise, like the municipal meetings that taught you how to phrase hope into technical terms."

    marina_reyes "We can organize a staggered blockade, people with clear lines, marshals, medics. We can make it safer—"

    kaori_kai_matsuda "Safer how? Safer until they bring in armored vans? Safer until the council folds? Marina, we've been pivoting to 'safe' for months and the sea keeps coming."
    show thomas_old_tom_bellamy at center:
        zoom 0.7

    thomas_old_tom_bellamy "I remember the winter of '38. The water came in like a living thing that knew who owed it. We bound nets and sang and we lost boats anyway. You think the council's numbers will hold against the sea. I won't watch my neighbors get priced out so a wall grows a little higher."

    marina_reyes "We need a plan that keeps people here. We need the cooperative to give folks income while the town makes hard choices about infrastructure."

    thomas_old_tom_bellamy "Hard choices. Not just promises."
    "Murmurs roll through the crowd. A camera light pans, catching faces: grief, resolve, hunger for something to bite into. Your heartbeat is loud in your ears."
    hide kaori_kai_matsuda
    hide marina_reyes
    hide thomas_old_tom_bellamy

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Hum of pumps, drip of condensation, the soft clink of label tags]
    # play music "music_placeholder"  # [Music: Lowered string undercurrent, tight and hollow]
    "You move through wet grass with Mika and Amalia to the Glasshouse. Inside, the humid air wraps like a blanket; trays gleam with condensation, and every surface is lined with labeled vials and the soft green"
    "of nascent blades. The smell is warm, mineral, alive — the exact opposite of the cold, metallic roar outside."
    show mika_tran at left:
        zoom 0.7

    mika_tran "We got the backup generator hooked. Filters are new. If the power blinks during the storm, nothing dies immediately—I've got a temp protocol."
    "You crouch beside a tray and watch a tiny frond unfurl as if deciding whether the world is safe enough to grow. Your hands remember your father's hands, the motion of tying a knot around a"
    "net buoy. You imagine losing this — months of careful grafting, data, the small community of microbes and spores you've coaxed into being."
    show amalia_reyes at right:
        zoom 0.7

    amalia_reyes "If we pull the lines, we lose momentum. People will say we ran. They'll say the experiment failed."
    show marina_reyes at center:
        zoom 0.7

    marina_reyes "If we protect the seedbank, we have a future trial. If we lose people now, we may not have a town to return to, Amalia."

    mika_tran "There's a middle—could we pull only the most exposed lines? Drone them to a safer depth? It'd buy us time."

    amalia_reyes "You're talking logistics. People will read logistics as betrayal if they don't understand the reasons."

    marina_reyes "People read the shape of our choices more honestly than we think. If they see seedlings pulled and think we abandoned them to make deals, they'll be right to be angry."

    menu:
        "Tell the crew to pull non-essential lines":
            "You point at the map tacked to the wall and mark the vulnerable pens with a shaking finger; Mika nods and already taps commands into the controller."
        "Stay with the seedbank until morning":
            "You press your palm to the tray rack, as if you could warm the fronds with insistence; Amalia folds her arms, admiration and fear wrapped together."

    # --- merge ---
    "Narrative continues."
    "You watch the condensation bead and slide down the plastic. You think of the livelihoods hung on the long-line, and of Kaori 'Kai' Matsuda's fury when solutions look like retreats. You think of Elias Kato —"
    "the way he keeps his hands on plans like they are the thing that keeps people from drifting away — and you imagine what he will ask in the soft-lipped way of municipal pragmatism."
    hide mika_tran
    hide amalia_reyes
    hide marina_reyes

    scene bg ch5_4001e7_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Conversation filtered through plastic windows, the distant percussion of pile-driving growing closer]
    # play music "music_placeholder"  # [Music: Mechanical, insistent rhythm; heartbeat-brass overlay]
    "Your phone buzzes — Elias. You hold it like an ember."
    show elias_kato at left:
        zoom 0.7

    elias_kato "Marina. Listen. Rina says we can get a forty-eight hour pause if we hand over a sampling subset of your data. Not everything — just enough to show the council and the company's engineers that the living buffers are working."
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "You want our data to stop them for two days?"

    elias_kato "Two days is something. Two days means we can get a council hearing, a real temporary injunction while the town sees the models next week."

    marina_reyes "And in exchange?"

    elias_kato "Publicly? A good-faith moratorium while we vet permits. Privately? Access to select readings: canopy density, load tests, salinity spreads. It's targeted. It's tactical."
    show kaori_kai_matsuda at center:
        zoom 0.7

    kaori_kai_matsuda "You're bargaining with our work. Data is our leverage, Elias. Handing it over hands them a roadmap to shut us down later."

    elias_kato "If we can't get a pause, they'll run the piles in the rain and call it emergency works. Then what? No time for injunctions. No time for caution. We lose everything."
    "You feel the words as if physically pressed against your ribs: lose everything. The seedbank, the long-lines, the town. You imagine Old Tom's porch floating, Amalia's festival canceled forever, families packed into vans with boxes labeled 'memories.'"
    "Rina's voice comes through the line, clipped and efficient."
    hide elias_kato
    show rina_corbett at left:
        zoom 0.7

    rina_corbett "We can secure a temporary hold. But council needs to see that there's a credible, technical alternative. Your data is credible. Give us the subset, we pledge to put the moratorium on the table in the emergency session. We need a named contact to verify chain-of-custody. This is the only way without inviting litigation."

    kaori_kai_matsuda "And when they take the data and tweak it until it says tomorrow's wall is safer, then what? You think they'll protect our community because of a spreadsheet?"
    hide marina_reyes
    show elias_kato at right:
        zoom 0.7

    elias_kato "I don't want to steamroll. I want to save as many homes as possible. This isn't betrayal if it keeps people here."
    hide kaori_kai_matsuda
    show marina_reyes at center:
        zoom 0.7

    marina_reyes "The word 'betrayal' hangs like a dropped knot. It's all you can see: the split between saving experiments and saving people, between future leverage and present bodies. The storm clock tick-tocks through your bones."
    hide rina_corbett
    show mika_tran at left:
        zoom 0.7

    mika_tran "We could anonymize locations, scrub identifiers."

    marina_reyes "They'll demand verification. They want reproducible results, not promises. If we anonymize and they call it suspicious, Rina cannot defend us."

    elias_kato "Give me the subset. Let me do the pushing. We'll get the pause. I'll stand in front of the council and take the heat."
    hide elias_kato
    show kaori_kai_matsuda at right:
        zoom 0.7

    kaori_kai_matsuda "We've seen that 'I' before. We've seen good intentions turned into deals that kick scrape people off the flats."

    marina_reyes "Elias — if I hand over anything, what's in it for the people who can't pack up and move? What guarantee do we have that a moratorium will hold through the storm?"
    hide marina_reyes
    show elias_kato at center:
        zoom 0.7

    elias_kato "No guarantees, Marina. Nothing is guaranteed right now. But a pause is the only thing that keeps the long-lines from being torn out tonight."
    "The line goes quiet except for the ever-nearer hammering. Your throat tightens. You can feel everyone at once: their need, their fear, their trust pressed into your palms like a rope. The sea is a dark"
    "mass beyond the lights, and the wind has picked up enough to throw salt into eyes."

    menu:
        "Promise Elias you'll consider the data swap but ask for written guarantees":
            "You ask Elias to have Rina draft the moratorium language tonight; he hesitates, then agrees to try, voice a flat blade of resolve."
        "Tell Kai you'll fight to keep every line in the water":
            "You turn to Kaori 'Kai' Matsuda, fingers still numb from the cold rope; she grabs your forearm like an anchor, eyes bright with something like fierce gratitude and peril."

    # --- merge ---
    "Narrative continues."
    "Your pulse is a drum. The pile-driver that was a distant metronome becomes a steel heartbeat you can almost place on a map; the crew across the tape starts a new sequence — a higher, angrier"
    "tempo. Someone shouts; you can't make out the words. Floodlights sweep. The crowd tightens. The rain that hadn't yet arrived begins as a fine mist, then a keel-heavy sheet that starts to strike the lanterns."
    "You think of the cooperative's seedlings under glass, of Old Tom's weathered hands, of Amalia's festival plans, of Mika's tired, intentional competence. You think of Kaori 'Kai' Matsuda's fury and of Elias Kato's restrained pleadings. Each"
    "option curls into itself like a breaking wave — it contains both shelter and smash."
    "Your muscles know the old motions: tie a rope, wedge a knot, call a line. Your mind divides the world into lists and probabilities as Elias trained it to, and into roots and hands as your father taught you. Neither language is sufficient alone. The storm isn't waiting for language."
    hide mika_tran
    hide kaori_kai_matsuda
    hide elias_kato

    scene bg ch5_4001e7_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Pile-driver pounding, rain, a hundred breathing people]
    # play music "music_placeholder"  # [Music: Crescendo — brass and percussion clash, then a single piercing violin note]
    "You close your eyes for a moment. The weight in your chest is a stone of all the unpaid debts of the town. Your hands remember your father's knot. Your jaw aches from holding back the sound that might undo you."
    "If you escalate, you risk immediate confrontation, injury, arrests, and the long-lines staying in the water to show the world what they can do. If you pull back, you protect the seedbank and the future at"
    "the cost of losing the public force of bodies now. If you negotiate, you risk handing leverage to institutional actors who might use it to cut the grassroots out of the story."
    "Your breath fogs. Thunder rolls like an answer from the sea."
    "You feel the choice press up against the bones of your hands, the buoy pendant warm and heavy against your sternum, a compass you can't read."
    # play music "music_placeholder"  # [Music: Staccato strings — rising to a held chord]
    # play sound "sfx_placeholder"  # [Sound: Shout from the crowd — "Decide, Marina!"]
    # [Scene: Tidal Flats | Night — Decision Point]

    scene bg ch5_4001e7_5 at full_bg
    # play music "music_placeholder"  # [Music: One sustained, dissonant chord, hanging, waiting]

    menu:
        "We escalate — mass action now; hold the line.":
            jump chapter6
        "Protect our experiments — pull back and preserve the seedbank.":
            jump chapter16
        "Negotiate a short pause — I’ll share select data with Elias if they delay.":
            jump chapter21
    return
