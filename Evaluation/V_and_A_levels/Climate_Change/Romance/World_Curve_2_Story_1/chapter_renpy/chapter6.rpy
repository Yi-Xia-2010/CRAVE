label chapter6:

    # [Scene: Municipal Hall | Midday]

    scene bg ch6_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Percussive, urgent strings; a distant low brass]
    # play sound "sfx_placeholder"  # [Sound: Rain on the plaza, the murmur of a crowd, a gavel thud settling like sediment]
    "You walk up the broad steps and feel the town like a living bruise. Salt and wet wool cling to your coat. Voices—some nailed-down, some ragged—spill from the open doors. Inside, the chamber smells of old"
    "wood, wet paper, and too-strong coffee. Light from the bay throws a cold reflection across the council dais where glossy renderings of a “secured future” glare like polished teeth."
    "Cassandra 'Cass' Whitlock stands near the microphone, composed as a machine that will not rust. Her suit is immaculate; her smile is practice. Behind her, a slick slideshow rolls — engineered sea walls, vitrines of investors'"
    "returns, a timeline framed in clean, inevitable lines. Around the room, neighbors clutch handmade signs: “Remember Marrow Bay,” “Protect Our Homes,” “Community First.”"
    "Your notebook is in your coat pocket, pages now damp. The Saltworks prototype hums in your memory like an argument that didn't get to finish. The choice you made—refuse the middle ground, try to keep this"
    "work local—has left you here, both accused of naivety and credited for courage. The chamber is a wound you have to stand in."

    "Council Chair Moreno" "We will hear opening statements. Ms. Whitlock first."
    show cassandra_cass_whitlock at left:
        zoom 0.7

    cassandra_cass_whitlock "Thank you. What we propose is scale, safety, and a fast track that gives Marrow Bay the infrastructure it needs before the next season. My firm will oversee construction, operations, and relocation with compensation packages ready. This is not charity—it's investment in survival."
    "You feel the room tilt at the word 'relocation.' Somewhere near the back someone exhales like a small animal."
    show noah_rivera at right:
        zoom 0.7

    noah_rivera "Relocation isn't survival if it erases where we learned to be ourselves."

    cassandra_cass_whitlock "Mr. Rivera, we are not here to erase. We are here to ensure that children can go to school come next winter."
    "A council member—thin and tired—taps a tablet. The exchange is polished, rehearsed. Your throat tightens."

    menu:
        "Step up to the microphone and call Cass out":
            "You stand, the room noticing the movement like a collective inhalation. Your voice scrapes out: 'You talk about kids; you talk about safety. But where is the line that says profit can't buy their graves?' A murmur ripples; Cass's smile thins."
        "Sit and let the community witnesses speak first":
            "You sit. Aunt Lila rises, supported by Jun; she begins in a voice that carries because it has carried storms for decades. The chamber listens as oral histories spill forward—sand, a lighthouse lamp, a daughter's laughter—human details that don't fit on renderings."

    # --- merge ---
    "Both outcomes converge back to the public testimony and the council's deliberation that follows."
    show aunt_lila_santos at center:
        zoom 0.7

    aunt_lila_santos "We don't want a future where our names are footnotes. We want shorelines that still hold memories."
    "Council Member Alvarez: (softly) 'We hear you. But the modeling—'"
    "You want to reach into the screen and tear the models open. The council's “modelling” is a map of likelihoods, not of loss. You raise your hand because the room is shifting and the moment demands it."
    hide cassandra_cass_whitlock
    show mira_santos at left:
        zoom 0.7

    mira_santos "My team and I built a working prototype at the Saltworks. It's not fancy. It bends with the tides, not fights them. It is made by people who will live with it. Give us the pilot; let the town keep oversight."
    hide noah_rivera
    show cassandra_cass_whitlock at right:
        zoom 0.7

    cassandra_cass_whitlock "Ms. Santos, your passion is clear. But fast-track funding prevents needless delay that will cost lives. Our oversight is robust; our engineers will take the burden."

    mira_santos "Whose burden? Will your engineers listen when an elder says, 'Don't take the fishing bench'?"
    "Cassandra 'Cass' Whitlock's jaw tightens almost imperceptibly. For a breath the room is compressed, the two kinds of logic clashing like weather fronts."

    "Council Chair Moreno" "We now move to a vote."
    "The chamber hums. Your chest is a drum in a band of thunder."
    # play sound "sfx_placeholder"  # [Sound: A glassy silence, the rustle of ballots]

    "Council Member Alvarez" "All in favor of issuing an emergency fast-track permit to Whitlock Coastal, with mandated timelines and oversight—aye."
    "You hear 'aye' like a clock hand moving. One by one, the ayes tally. The expanse of the room contracts and then explodes—people's voices folding into one another, some cries of outrage, some of resigned acceptance."

    "Council Chair Moreno" "The motion carries."
    # play sound "sfx_placeholder"  # [Sound: Gavel strike — a sound like a ship running aground]

    cassandra_cass_whitlock "This is the first step toward protection."
    hide aunt_lila_santos
    show noah_rivera at center:
        zoom 0.7

    noah_rivera "Protection for whom?"
    "You watch as a woman in the row behind you begins to cry, the sound immediate and raw. A kid bangs a sign against a seat until it snaps. Somewhere, someone throws up their hands and leaves."
    "Outside, a small convoy of vehicles idles like scavengers. Inside, Cass is already dictating the first wording for press releases. Legal teams move with the kind of calm surgeons use on healthy tissue."
    # [Scene: Saltworks Turnover | Afternoon]
    hide mira_santos
    hide cassandra_cass_whitlock
    hide noah_rivera

    scene bg ch6_4001e7_2 at full_bg
    # play music "music_placeholder"  # [Music: Industrial rumble; metallic percussion]
    # play sound "sfx_placeholder"  # [Sound: Chains, engines, a high-pitched electronic lock engaging]
    "You run toward the Saltworks because letting it go on paper is one thing; seeing it handed over is another. The boardwalk is a line of witnesses—some trying to block, some filming, some sobbing quietly. A"
    "Whitlock van parks beside the raised platforms. Men and women in crisp jackets begin to inventory the prototypes, snapping cases closed, photographing serial numbers."
    "Elias Park is already there, sleeves rolled, hands dirt-streaked. He is working, quietly efficient, but the lines around his eyes register shock and a tight, restrained energy. He meets your gaze; relief and anger pass between you like tide foam."
    show elias_park at left:
        zoom 0.7

    elias_park "They have lawyers. They have permits. We have—"
    show mira_santos at right:
        zoom 0.7

    mira_santos "We have each other, and a handful of batteries."
    "A Whitlock operations manager approaches, clipboard like a shield."

    "Operations Manager" "Ms. Santos, you'll need to step back. This site is under corporate control now."
    "You place a hand on the micro-turbine you've been debugging for months. It is warm, humming with small potential. Two technicians lift a wooden crate stamped with your handwriting—NOAH'S HANDS BUILDING—and begin to carry it toward the van."
    "You reach for the crate."

    menu:
        "Try to physically stop them from loading the crate":
            "You step forward, palms open, blocking their path. The lead tech looks at you, then at his tablet. Security arrives and grips your arms. Your chest fills with a white-hot mix of fear and fury."
        "Document everything, speak to press, appeal to the crowd":
            "You turn, voice raised, telling the crowd what's being taken and why. A dozen phones point; a reporter takes notes. The technicians grow more cautious, but the crate still moves. Your words plant seeds that will not be erased."

    # --- merge ---
    "Both outcomes lead to a confrontation diffused by security and legal posturing; Elias restrains escalation and the technicians continue inventorying."

    elias_park "Mira, they will bristle if we escalate. They'll use any clamp-down to paint us as unreasonable."
    "You feel the weight of his caution—the same hesitation that once kept him from walking away from a failing project. You don't want caution now; you want a stack of small, quiet explosions."

    "Whitlock Legal Representative" "We intend to integrate the prototype into a broader system with scheduled community input sessions."
    "You can hear the conditionality in her voice—'community input' is a word with hinges."
    "A team begins to unclip your signage that reads SALTWORKS: A COMMUNITY PILOT. White-painted bolts come out; a gleam of metal undercuts the color of your hopes."
    # [Scene: Boardwalk | Late Afternoon]
    hide elias_park
    hide mira_santos

    scene bg ch6_4001e7_3 at full_bg
    # play music "music_placeholder"  # [Music: High strings, urgent and cutting]
    # play sound "sfx_placeholder"  # [Sound: The thump of wood on doorframes, neighbors' voices rising into a chorus]

    "Relocation notices are handwritten in bureaucratic script: legalese that translates into two words you can feel like cold" "temporary relocation."
    "Mrs. Ortega from the bait shop holds a notice and reads it again, as if the words might reassemble into mercy. Jun kneels in the gutter and crumples a corner of the paper between his fingers. The ocean behind them is the same ocean as always, indifferent and beautiful."
    "You move from house to house, delivering what information you can—who to speak to, where legal aid congregates, where to find blankets. People cluster on porches like huddled birds. A notice is affixed to Aunt Lila’s"
    "door. You watch as she opens it with slow hands, the motion of someone too old to run but still required to witness."
    show aunt_lila_santos at left:
        zoom 0.7

    aunt_lila_santos "They can move our furniture. They can't move the stories."
    "You want to say that words like hers will not be enough, but then you recall the way people hold onto stories. You also recall the legal forms that will be used to untangle property claims. The paperwork seems to outpace grief."
    "Elias Park takes a small toolkit out of his jacket and starts to unscrew a bracket from a shared solar column—a tiny, symbolic act of reclaiming. A corporate drone buzzes and records."
    show elias_park at right:
        zoom 0.7

    elias_park "If they take everything, we'll still have hands."
    show mira_santos at center:
        zoom 0.7

    mira_santos "Hands are not a town plan."
    "The drone backs away, then returns with a security van and two officers who do the work of neutralizing small resistances with procedural calm. They stick notices on posts like tide markers."
    # [Scene: Old Lighthouse | Dusk]
    hide aunt_lila_santos
    hide elias_park
    hide mira_santos

    scene bg ch6_4001e7_4 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano, low and mournful]
    # play sound "sfx_placeholder"  # [Sound: Wind through the stones, distant sirens that feel secondary to the pounding in your chest]
    "You and Elias climb the narrow spiral where you once practiced what you'd say to the sea. The wind smells of iron and something like endings. Up in the lantern room, the lamplight is an intimate,"
    "private burn; it doesn't erode the harshness of the day but it makes a small island of warmth."
    "You sit on the bench where Aunt Lila used to mend nets. Elias leans his head against the cool window, watching the boardwalk shrink into a scatter of lights and motion. You can see the corporate"
    "convoy still at the Saltworks, a rectangle of movement like a smudge on the map."
    show elias_park at left:
        zoom 0.7

    elias_park "They took the paperwork, the permit, the platforms—everything with a serial number. But they left the stories."
    show mira_santos at right:
        zoom 0.7

    mira_santos "They're not the same stories if there is a sign and a logo over them."

    elias_park "We can keep building in corners. We can find ways to help people resist displacement, keep legal pressure on them, work with Jun and Noah. It won't be the same. But—"
    "You cut him off, not angry but raw. 'But?' you push."

    elias_park "But I won't leave. Not you, not the town."
    "The firmness in his voice is a small rescue. You close your eyes and let the salt in your lashes taste of what you've lost and what remains."
    "You clasp his hand. The contact is grounding, real—fingertips pressed into the weathered copper of his cuff. For a moment, tenderness blooms like a stubborn plant through cracked concrete."

    mira_santos "We stay together."

    elias_park "Then we'll make that shelter useful."
    "Silence sits between you like a legal document you can't yet read. The lighthouse lamp turns, a slow, indifferent sweep across the water. The town below is smaller now in the way a bone is smaller"
    "when a body is broken; the coastline lines have been redrawn by people with ledgers."
    "You think of Aunt Lila's hands, of Noah's stubborn laughter, of Jun's flyers fluttering like prayer flags. You think of the seeded prototypes, of micro-turbines that hum with possibility even when boxed. The fast-track has cut"
    "a path; it will reshape property, lives, and decisions. Small-scale efforts are being folded into a centralized plan and rebranded; the Saltworks, once communal stubbornness made physical, wears someone else's logo."
    "Your chest aches with a grief that is nearly physical. The collapse is not cinematic; it is paper, signatures, machine clamps and the quiet erasure of daily rituals. The town is not gone. But it is diminished. Your ideals are bruised tissue."
    "Elias Park squeezes your hand. The warmth is immediate and fierce."

    elias_park "We will do the work that can't be covered by contracts. We'll show what corporate models miss. We'll be unglamorous and persistent."

    mira_santos "And what if they make it illegal to help? What if the next step is to criminalize small resistance?"

    elias_park "Then we'll find another way—teach, rebuild, shelter. We still have neighbors. That's a start."
    "You look at him—a person who keeps gears and hope in the same pockets—and for a jarring second you imagine the life the two of you could build that isn't a public statement but a private,"
    "stubborn practice of care. That image is both consolation and a wound. The ending you can see is not triumphant. It is a narrow survival, a bending that tastes of ash."
    hide elias_park
    hide mira_santos

    scene bg ch6_4001e7_5 at full_bg
    # play music "music_placeholder"  # [Music: A single sustained chord resolves into a low, humming silence]
    "You and Elias stay on the lighthouse while night falls, letting the town breathe around the new reality. The notices will stand on doors. The Saltworks sign will be replaced. The law will have its pageantry."
    "Your hands are smudged with salt and oil, and you have learned that holding on and letting go are not opposites but twin tasks."
    "You rest your head against Elias’s shoulder. He is here. The town is here, altered but still wrung with possibility. The future is smaller and harder; your optimism has been made lean. You close your eyes,"
    "and in the dark you make the quiet, stubborn promise to continue—if for no other reason than because some stories refuse to be entirely taken."

    scene bg ch6_4001e7_6 at full_bg
    "THE END"
    # [GAME END]
    return
