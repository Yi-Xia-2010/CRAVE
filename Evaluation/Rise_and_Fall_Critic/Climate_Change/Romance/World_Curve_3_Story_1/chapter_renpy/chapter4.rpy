label chapter4:

    # [Scene: Tom's Shop | Morning]

    scene bg ch4_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls and the thud of a dropped toolbox]
    # play music "music_placeholder"  # [Music: Low, insistent cello]
    "You chose this. The choice sits in your chest like a stone warmed by hands — heavy, familiar, necessary. You watch Kai Nakamura unfold a small, folded prototype from beneath his windbreaker and for a moment,"
    "under the oil-scented light, it looks like a promise. His grin cuts through the tightness you've been carrying; the kind of grin you remember from summers on the pier, when a scraped knee was fixed with"
    "spit and a shrug and everything still felt repairable."
    "Tom wipes his hands on a rag and laughs before he can stop himself. The sound is wet with grease and good humor."
    show kai_nakamura at left:
        zoom 0.7

    kai_nakamura "Okay, picture this — stackable modules, interlocking lips. If one seam pops, the next one picks up the slack. Cheap, quick, and we can build them from salvaged boards and recycled plastic."
    "You step closer and the prototype's edges are rough but clever: a tongue-and-groove cut that would clip with a satisfying snap if it were larger. You trace the line with a fingertip, feeling the grain."
    show iris_alvarez at right:
        zoom 0.7

    iris_alvarez "The math fits in my head. The models, the cost curves, the people-hours. It all folds into the same ledger I keep in my head at night. But a ledger doesn't hold hands or haul tar in a rainstorm. It doesn't make someone show up when their boat is a wreck and their rent is due."
    show tomas_tom_alvarez at center:
        zoom 0.7

    tomas_tom_alvarez "If we build them right, we can pitch them as temporary defenses — buy us time. I've got planks, tar, some bolts. Not much money, but muscle is free."

    iris_alvarez "We'll need a roster. Shift-based work so people can keep their jobs. And Etta — she'll want seeds, not just wood."

    kai_nakamura "Etta's seeds help us anchor the community. When people plant, they stay. That's the point."
    "There's a pause where the three of you line up the practical and the sentimental and try to make them fit."

    menu:
        "Sketch the volunteer roster now, while momentum's hot":
            "You spread a scrap of kraft paper across the bench and write times and names in a rush. Tom nods, Kai grins, and the energy in the room spikes; for a beat, the plan is a living thing."
        "Finish the prototype measurements first, to avoid rework later":
            "You tap a pen against the blueprint, smoothing the edges of the design. Kai frowns at the delay but doesn't argue; there's trust there, brittle and useful."

    # --- merge ---
    "Proceed to the Greenhouse Commons scene"
    # [Scene: Greenhouse Commons | Midday]
    hide kai_nakamura
    hide iris_alvarez
    hide tomas_tom_alvarez

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft drip of condensation, laughter muffled through wet glass]
    # play music "music_placeholder"  # [Music: Quiet piano with a melancholic turn]
    "Etta arrives with pockets full of seed packets and a smile like a folded map of the town's past. She palms you a packet of rye and looks at your hands, stained with oil and ink."
    show etta_bloom at left:
        zoom 0.7

    etta_bloom "You think you can save a town with timber and tar, child? You save the people first with food and shelter. We plant, they stay. That's how I know."
    show iris_alvarez at right:
        zoom 0.7

    iris_alvarez "We build the barrier, we protect the ground where people plant."
    "Etta examines a modular sketch and taps the edge. 'Make sure the base is broad. The sea eats a thin wall like teeth on driftwood.'"
    show lina_harrow at center:
        zoom 0.7

    lina_harrow "I'm not giving this whole harbor up for a school project, Iris.' (Her eyes flick to you and then to Kai Nakamura's solar patches.) 'But I won't watch the old pier vanish either. I'll give you dock space for staging. Don't make me regret it."
    "Iris Alvarez: (relief and impatience mixing) 'Dock space is huge, Lina. We'll be careful with the traffic.'"
    "Lina's mouth tenses; she mutters about liability and customers and the bank. You know what's unspoken: every foot of concrete she turns over for us is a foot she doesn't put toward a new development that"
    "could make more money faster. You accept the offer because things here are traded in quiet bargains."

    menu:
        "Accept Lina's dock staging and promise strict cleanup rules":
            "You clasp Lina's hand, making it a pact. She eyes you shrewdly but nods, and the ledger of favors shifts in your favor."
        "Ask Lina for a small rental fee to keep commitment mutual":
            "You propose rent and her jaw tightens; she warns you about long-term costs but concedes on the condition you keep the area shipshape. The agreement feels transactional but steadier."

    # --- merge ---
    "Proceed to the Tom's Shop late afternoon scene"
    # [Scene: Tom's Shop | Late Afternoon]
    hide etta_bloom
    hide iris_alvarez
    hide lina_harrow

    scene bg ch4_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A dozen small conversations, the scrape of a marker on whiteboard]
    # play music "music_placeholder"  # [Music: Low strings, a minor chord repeating]
    "You draft waivers like a midwife delivers a baby — careful, legal, necessary, and a little cruel. Your fingers move over the tablet, typing in language that keeps volunteers safe and the town out of a"
    "courtroom. The words feel like fabric stretched over a skeleton: they protect, but they don't warm."
    show iris_alvarez at left:
        zoom 0.7

    iris_alvarez "I can feel the old habit—taking on what others should hold—sliding into place. If a form exists, I fill it. If a load is heavy, I lift it. If a night is cold, I sleep under the greenhouse lights. It keeps things moving. It also keeps me from asking for help in the ways that matter."
    show kai_nakamura at right:
        zoom 0.7

    kai_nakamura "Iris, you're writing us into more paperwork. People joined because they want to build, not sign contracts."

    iris_alvarez "We need people to show up next month, Kai. We need to know who is trained to handle the winch. Liability is what shuts us down before we get started."

    kai_nakamura "If we get stuck in permits, momentum dies. I can't —' (He presses his palms to his temples.) 'I can't stand watching enthusiasm evaporate into red tape."
    show tomas_tom_alvarez at center:
        zoom 0.7

    tomas_tom_alvarez "Both of you make sense. But the sea doesn't care about your patience or mine. It hits whether we're ready."
    "The conversation ricochets: Kai's impatience, your caution, Tom's dry pragmatism. The tension is not new — it's new only in its immediacy."
    hide iris_alvarez
    hide kai_nakamura
    hide tomas_tom_alvarez

    scene bg ch4_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind picking up outside the open door]
    "You find yourself sleeping on the greenhouse bench that night, the grow lights warm against your cheeks, the rain like a metronome. You wake to the sound of boots and the clinking of tools: volunteers arriving,"
    "faces lit with purpose. The first build day hums; salt-streaked hands pass bolts, laughter threads between commands, and for a few hours, the world narrows to the exactness of joining two boards."
    # [Scene: Pier — Partial Barrier Build | First Storm Surge — Dawn]

    scene bg ch4_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Surge hitting with a wet, rolling force; shouts and the thump of waves]
    # play music "music_placeholder"  # [Music: Percussive drums increasing in tempo]
    "Your hands are numb from the cold, from hoisting, from not sleeping. The smell of tar and wet wood is a second skin. You watch volunteers brace, rope lines taught like violin strings."
    "And then — seam. A seam gives with a sound like paper tearing. One module's tongue slips free under pressure and, with the momentum, the neighboring joins wrench apart like a zipper undone."
    "A chorus of curses rises. Someone tries to wedge a spare plank. A volunteer slips in mud and their shout fractures into terrified silence. You run, heart stabbing, to the line and find the module buckled, water curling into the shallow gap."
    "Kai Nakamura reaches you two breaths after, his hair sodden, eyes wide in that way hope becomes open fear."
    show kai_nakamura at left:
        zoom 0.7

    kai_nakamura "We can clamp it. We can—"
    show iris_alvarez at right:
        zoom 0.7

    iris_alvarez "Clamp what? We have clamps, but not enough people, not enough time. The tide's already higher than the forecast."

    kai_nakamura "We test, we iterate. We learn."

    iris_alvarez "We needed a seam that wouldn't fail on the first real surge."
    "He looks at you, searching, then down at the broken join. There's something vulnerable there, not the insolent grin from the shop but an honest, unexpected admission of being human-sized against an ocean."

    kai_nakamura "We didn't expect yesterday would be the test. We shouldn't have been arrogant about the timing."

    iris_alvarez "No — we shouldn't have been unprepared for the obvious. I pushed us into volume over redundancy. I thought momentum would shelter us. I thought people showing up made us invincible."
    "Silence swells and then cracks with the tide. Around you, the town watches. The applause that comes from the promenade is immediate: hands clapping for the attempt, for bravery, for neighbors who tried. But it lands"
    "like a bandage over a deeper bruise — it warms and it fails to fix."

    iris_alvarez "The applause stings. It recognizes effort but not consequence. Guilt is not a rational number I can balance on my tablet. It is a hollow that opens in my chest, a place where blame collects."
    "The municipal inspector arrives, coat buttoned against the spray, expression practiced and tight. You look up to find Marin Voss's face in the inspector's crowd — measured, unreadable. They cross the line between officialdom and neighbor"
    "and their eyes skim you. You cannot tell if there is reproach, relief, or simply resignation."
    show marin_voss at center:
        zoom 0.7

    marin_voss "We need a report. Liability concerns, emergency repairs, risk assessments. This is why permits exist."

    iris_alvarez "We were trying to buy time. People showed up because they care."

    marin_voss "Care does not substitute for certified engineering. If someone is hurt, the town answers."

    kai_nakamura "And if the town delays, nothing gets built and everything gets lost."

    marin_voss "Both are true. Neither is a solution by itself."
    "The inspector's words land like scales being set out. Your throat tightens. You know the legal labyrinth empties out into real losses: businesses shuttered, properties sold to developers who will replace porches with breakwaters that look"
    "like fences. The roster you built this morning is a map of hands you counted on; now those hands shake or argue or step away."
    "Tom puts a warm, heavy hand on your shoulder. 'We did what we could, kid.' His voice is kind, but even kindness has edges. You want to believe him but the tang in your mouth is not salt alone."

    iris_alvarez "This is the cost of habit — of stepping into gaps when others hesitate. It keeps things moving, yes, but at what toll? At what accumulation of seams that will eventually give under real pressure?"
    "The town's applause finishes like a tide pulling back. Someone drags a tarp to cover the broken join; others mutter about shifts, improvements, reinforcement. Volunteers return to work with wet sleeves and determined faces. But when you close your hands, the ache of responsibility blooms."
    "Kai Nakamura catches your eye. For a long beat, neither of you says the words that anchor or unravel relationships: I was wrong; forgive me; you were right. The storm continues to roar. The barrier is half-finished and half-broken and fully vulnerable."
    # play music "music_placeholder"  # [Music: Low, descending piano; the mood narrows into a single, held chord]
    "You feel the town watching you — not accusing yet, but expecting leadership that now feels brittle. The options begin to line up in your mind like fjords one must commit to crossing."

    menu:
        "Double down on community builds and fast iteration, learning from the seam failure.":
            jump chapter5
        "Pause and petition the municipality for provisional support to certify our designs.":
            jump chapter7
        "Bring Kim-like open-source blueprints to nearby towns to recruit volunteers and materials.":
            jump chapter9
    return
