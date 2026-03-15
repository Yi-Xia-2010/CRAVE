label chapter14:

    # [Scene: Reclamation Works | Morning — first light behind low clouds]

    scene bg ch12_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Mechanical roar, metal biting into earth; gulls shriek, drowned out by diesel engines.]
    # play music "music_placeholder"  # [Music: Rapid, driving strings — urgent, relentless]
    "Narration:"
    "You arrive before the machines have finished naming the shore. The decision made at the hearing is already being translated into motion: teeth of iron, lines of concrete. The air is thick with churned salt, diesel,"
    "and the sharp tang of disturbed mud. Every bite the machines take at the inlet feels like punctuation — a clause in the city’s new sentence."
    "Narration:"
    "Your notebook is in your hand like a talisman, pages damp from last night’s hurried notes. You think of the hearing, of the way your voice held steady when the cameras were on. You think, too,"
    "of the promises you and others made there — that lives would be shielded, that the emergency shoring would buy time. That logic sits heavy and exact beside the sight of the cove being filled in."
    "Narration:"
    "Lito stands a few yards away, hands jammed deep in his jacket pockets, face a tight map of disbelief. He watches the machine swallow his cove — the one he taught you to knot a mooring"
    "at, the one with the silver rock you cracked open for bait. He looks like he’s trying not to move; not to give the waves an excuse to keep coming."
    show lito_reyes at left:
        zoom 0.7

    lito_reyes "They didn't even leave the old moorings. Not enough room. They just... folded it over."
    "Narration:"
    "You hold a breath that tastes like iron. For a moment your chest is a closed room and grief and satisfaction press at opposite doors. The city's metrics will record fewer flooded homes, fewer emergency rescues,"
    "insurance lines calming. That is not nothing. People sleep inside their houses now who would not have. That truth hits you with the sharpness of a bell: lives spared in narrow but concrete ways."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "They did what they said they'd do — protected the main lines. But they took the edge. They took what we used to call 'ours.'"

    lito_reyes "Enough for the books, maybe. Not enough for us."
    "Narration:"
    "Lito's voice has the brittle steadiness of someone counting losses. He turns away when a hydraulic jaw snaps the last reed free, and you can see the place in his face where the daily rhythm used to live."

    menu:
        "Put your arm around Lito":
            "You step in close, shoulder to shoulder, letting warmth and weight speak. He leans into the contact for a beat and then inhales, the sound raw. It does not fix the cove, but it slows the collapse between your chests."
        "Stand rooted and watch the machines":
            "You keep your hands around the notebook, back straight, jaw set. Keeping your face still feels like an offering: if you don't flinch, maybe the loss will take a different shape. Lito's silence answers yours like a held drumbeat."

    # --- merge ---
    "The main narrative resumes with the machines continuing their work."
    "Narration:"
    "The machines keep their rhythm. They are efficient, obscene in their effectiveness. You measure their progress the way you used to measure tides: by the line they leave on the gulls, by the way the reeds stop answering the wind."
    "Narration:"
    "You think of the people who will sleep inside walls that hold. You think of the people who will no longer have a cove to pull a small boat against. You let both truths be true"
    "at once — an honest bifurcation — and feel a strange, searing clarity settle through you. Relief does not cancel grief; grief refracts relief into something hard and glass-like."
    # [Scene: Boardwalk | Noon — sun fighting through the cloud deck]
    hide lito_reyes
    hide maya_reyes

    scene bg ch12_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmurs and clinking glasses from a catered tent; under that, distant machinery.]
    # play music "music_placeholder"  # [Music: Brass interjections over a brisk percussive heartbeat — the public pulse of momentum]
    "Narration:"
    "Officials and investors network under rented canopies. The mayor moves through them with a practiced smile, a weathered campaign pin catching the light. Camille Duval is there — precise, spotless, already wearing the victory that was"
    "always part program, part inevitability. Her heels make small, certain sounds on the patched planks."
    "Narration:"
    "Mayor Sofía approaches you first, her smile folded with something like exhaustion and calculation."
    show mayor_sofa_lvarez at left:
        zoom 0.7

    mayor_sofa_lvarez "Maya. You did us a service by staying in the public eye. The emergency shoring wouldn't have had public trust otherwise."
    "Narration:"
    "You look at her and feel the scale of what was traded. You also know the ledger is not simple; she balanced votes, budgets, human risk. She is not a villain in this arithmetic. She is"
    "a mayor who chose a route when choices were measured against evacuation timelines and insurance models."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "It bought us time. It also cost a stretch of living water. People lost their moorings, their daily practice."

    mayor_sofa_lvarez "We kept more people in their homes than we would have otherwise. That has to count."
    "Narration:"
    "The two of you circle the truth. Neither side claims victory like a trophy. It feels more like a mutual acknowledgment that public governance is a series of impossible equations, and sometimes the numbers that save lives are the same numbers that hollow places out."
    show camille_duval at center:
        zoom 0.7

    camille_duval "We made the hard choice that no one else would. The region needed stability. We prevented what we could not allow: cascading failures, damaged infrastructure, a city that would become an ongoing emergency zone."

    maya_reyes "At what cost, Camille? Reeds, moorings, livelihoods — those are not just sentimental details. They are functioning parts of an ecosystem that supports your 'stability.'"

    camille_duval "Ecosystems adapt. Engineering preserves the parts of the city that must remain intact if people are to have futures here. There will be remediation plans. There will be funding. We can replant, reintroduce marsh edges in controlled zones."

    maya_reyes "You can't plant fifteen years of tidal patterns with a contractor's timeline."

    camille_duval "No. But I can buy the year in which you tell me I'm wrong with fewer people drowned."
    "Narration:"
    "The line between you tightens into a single taut thread. Her certainty confronts your insistence on place-based values. The conversation could fray into recrimination; instead it becomes a proving ground — each of you offering a different moral calculus. Around you, press flashes like small, merciless stars."

    menu:
        "Ask Camille about remediation timelines":
            "You keep your voice steady and force details: how many hectares, when will be the first planting, who holds long-term maintenance? Camille answers with numbers and milestones. Her roadmap is clean and funded; it comforts and repels you in the same breath."
        "Tell the mayor you won't sign community acquiescence":
            "You refuse the polite politics, saying you won't put your name to a process that paved over parts of your neighborhood. The mayor's jaw tightens; she understands the cost. Her eyes hold sadness, not surprise."

    # --- merge ---
    "The narrative continues with reflections on Camille's professionalism and the mixed feelings it inspires."
    "Narration:"
    "You do not find solace in Camille's charts. You do, however, find contours of respect: she did not come as a conqueror gloating. She is a professional who believes in a certain kind of protection. That"
    "fact irritates and steadies you all at once. The world is occasionally full of people who mean well and are wrong; sometimes it is full of people who mean differently and are right for the short"
    "term."
    # [Scene: Marsh | Late afternoon — low sun turning the water to linseed]
    hide mayor_sofa_lvarez
    hide maya_reyes
    hide camille_duval

    scene bg ch12_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A softer hush here, a mournful reed-song where earlier there was a chorus.]
    # play music "music_placeholder"  # [Music: Strings swell into a cathartic, luminous line — intense, clarifying]
    "Narration:"
    "At the edge of the new seawall you find the things that anchor memory: a bead of green glass lodged in a crack of old piling; a rusted cleat with a family’s name half-erased. You kneel and cup the bead as if it were a heartbeat you could carry."
    "Narration:"
    "Your phone buzzes — a message from Elias. His words are practical, stained with the same compromise you see in the city’s choices: testing sensor placements, retrofitting pylons, scheduling legal consultations with the firms managing the"
    "shoring's liabilities. He stayed; the job needed someone to translate the engineers' actions into mitigations that minimized long-term harm. He thought he could steer the ship from inside."
    show elias_stone at left:
        zoom 0.7

    elias_stone "Did what I could today. Met with the team. We can try modular living shorelines in the secondary channels. Not perfect, but better than nothing. Coffee tonight?"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Better than nothing. Better for some channels. Not for Lito’s cove."
    "Narration:"
    "Elias arrives as the sun tilts, his sleeves rolled, a smudge of grease under a thumbnail. There's a distance in him that wasn't there before — not cruel, but occupied by logistics, by legal briefs, by the mental weight of operationalizing a policy he never fully endorsed."

    elias_stone "I thought staying would let me shepherd this. I thought if I could be in the room, I could make the engineering make sense for people."

    maya_reyes "Did you make it make sense?"

    elias_stone "We slowed some things. We got commitments for habitat offsets and funding for long-term monitoring. I argued for living shore pilots. They agreed to limited pilots."
    "Narration:"
    "You both watch a gull fold itself into the sheen of the new revetment and feel how small that single victory is compared to the cove refilled behind you."

    elias_stone "Maya — I wish we had stopped more of it."

    maya_reyes "So do I."
    "Narration:"
    "The conversation could pulse into recrimination. Instead it becomes a fragile tracing of where your paths split. There is love in the exchange, a worn familiarity that still knows how to rest on a shared joke"
    "about bad coffee at field sites. There is also a cleaner, angrier truth: good intentions could not tip the scales that day."

    elias_stone "I can't be everywhere. I thought staying here was the best way to help, but the work keeps pulling me into courtrooms and coordination meetings. I don't know if that will look like anything you recognize as help."

    maya_reyes "You did what you thought would do the most good. So did I. Different rooms. Different fights."

    elias_stone "Yeah."

    menu:
        "Reach for Elias' hand":
            "You close the distance and take his hand. For a moment you are two people tethered in a place that no longer holds what it once did. He squeezes back, and the contact is small relief — human, real, finite."
        "Step back and give him space":
            "You retract, making room for the truth to find its own shape. Elias expects you to lean in; instead you choose to let the silence be its own kind of answer. He nods, understanding, and walks away slower than usual."

    # --- merge ---
    "The narration continues with Maya's decision and the reflections that follow."
    "Narration:"
    "You make a choice in the hush — whether to anchor to the man who stayed or to stand separate and let each of you carry what you must. Both choices feel like a kind of survival. Neither choice is a betrayal; both are a negotiation with reality."
    "Narration:"
    "You go home that night with salt dust at the seams of your jacket and a map filled with annotations of loss and with pins for the tiny wins. You sit at your kitchen table and"
    "trace the lines with your finger: the inlet that is gone, a proposed living-shore pilot in a side channel, the locations where families have agreed to accept relocations. The ledger is both comfort and indictment."
    # [Scene: Your Front Steps | Night — light rain begins again]
    hide elias_stone
    hide maya_reyes

    scene bg ch12_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain on tarps, distant generator hums, doors shutting behind departing neighbors.]
    # play music "music_placeholder"  # [Music: A lullaby of percussion and rising strings — intense but settling toward a luminous resolve]
    "Narration:"
    "You pack your bag with the things you need: the field notebook, the dented thermos, the pendant with the green bead you found. There is a list of contacts, a pile of petitions, a stack of"
    "photographs of reeds in bloom that you tape to the inside of your folder so you can see what this place used to sound like in light."
    "Narration:"
    "You have fought in public hearings, in neighborhood halls, in the muddy marsh. You have lost some fights and won others. Tonight the scale tips toward an official stability you did not want, but you are"
    "not erased by it. The city can measure what it calls security; you keep a map of what it cannot count."
    "Narration:"
    "Lito finds you on the steps, face wet with rain or tears — you cannot be sure. He presses a small, limp fishing line into your palm: a knot he says he couldn't salvage from the old mooring."
    show lito_reyes at left:
        zoom 0.7

    lito_reyes "Keep it. Wherever you go, don't let them have all the stories."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "I won't."
    "Narration:"
    "Elias appears at the end of the block, giving you a nod that contains both farewell and thanks. It is not dramatic — both of you are too tempered for theatrics — but it is real."
    "You feel the tug: part of you wants to follow him into the rooms where engineers archive mitigations; part of you knows your presence matters in different places, where seeds are planted and neighborhoods organize their"
    "grief into plans."
    "Narration:"
    "You make a decision that feels both like grief and liberation. You will leave the neighborhood to continue activism elsewhere — to carry the maps, the stories, the bead. You do not abandon the people here;"
    "you carry their long slow ache into whatever next fight will listen. This is not defeat in your bones. It is an acceptance of the cost and a redirection of energy toward where your hands can"
    "still change things."
    "Narration:"
    "You walk the boardwalk one last time under the rain, feeling the sting of loss and the sharpness of commitment braided together. The city, for all its new walls and fills, sleeps more evenly tonight. Buildings"
    "that would have flapped like sheets in storms have acquired armor. That armor buys a kind of breathing room for thousands. That fact settles in your chest like a bright, painful stone."
    "Narration:"
    "You are not sure if the marsh will ever be what it was. You are sure that it taught you how to keep fighting in new ways. You carried that lesson through the hearing, through the"
    "machines, through the quiet parting. You carry it now — fierce, clarified, and strangely hopeful."
    hide lito_reyes
    hide maya_reyes

    scene bg ch12_f99e88_5 at full_bg
    # play music "music_placeholder"  # [Music: Full, luminous swell — triumphant and aching, strings and brass lifting toward a clear, high note]
    # play sound "sfx_placeholder"  # [Sound: The machinery fades to a distant thrum; the rain becomes a steady, enveloping sound]
    "Narration:"
    "You step off the boardwalk, the city spreading behind you like a ledger of choices. You leave the neighborhood with a map full of grief and with a heart that still chooses work. There is an"
    "unshakeable pride in the small, stubborn acts you led — the neighbors you convened, the pilots you pushed, the people you sheltered. Those things are true. They are not the whole story, but they are worth"
    "carrying."
    "Narration:"
    "You fold the torn map into your notebook, close it, and place it near your heart. The beads of rain feel like a benediction."

    scene bg ch12_f99e88_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade into a sustained single, clarifying chord — bright, long, and resolved]

    scene bg ch12_f99e88_7 at full_bg
    "THE END"
    # [GAME END]
    return
