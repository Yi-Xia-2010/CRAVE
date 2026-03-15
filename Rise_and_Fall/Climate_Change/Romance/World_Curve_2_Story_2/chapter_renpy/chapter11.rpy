label chapter11:

    # [Scene: Glasshouse | Dawn]

    scene bg ch11_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, mournful cello with a distant wind motif]
    # play sound "sfx_placeholder"  # [Sound: Soft slap of boots on wet stone; the kettle hissing faintly in the background]
    "You push the glass door and the smell of damp soil and old glass folds over you like a confession. Seed trays line a long workbench—green smudges against worn wood, each cell a tiny argument against"
    "erasure. Your fingers still smell of mud from last night; the cold has left freckles along the backs of your hands."
    "Nia is already here, sleeves rolled, hair pinned up in a knot that looks like it was tied by somebody who needed both speed and stubbornness. She moves with the small, efficient rituals that keep everyone"
    "fed: marking labels, counting plugs, checking lights. Her face lifts when she sees you, then softens into something almost like relief."
    show nia_voss at left:
        zoom 0.7

    nia_voss "You look like you haven't slept. Thermos is still warm—you didn't finish your last cup."
    show mara_voss at right:
        zoom 0.7

    mara_voss "Didn't feel like finishing it. Machines were closer to the headland than I thought."
    "You set your notebook on the bench, the page folded where you pressed your thumb like a pledge. The little things are louder now: the creak of the greenhouse door, the dripping from a gutter, the"
    "beep of a field sensor you left charging. Outside, the headland's machinery keeps time—an industrial metronome that ties itself to every conversation in town."
    "Rina Park arrives without fanfare, pushing the double doors with her shoulder and carrying a tablet. She smells of coffee and a different kind of weather—agency air, pressed sleeves, the efficiency of someone used to clicking through proposals."
    show rina_park at center:
        zoom 0.7

    rina_park "Morning. Sorry to barge in—got something you need to see."

    mara_voss "What now?"

    rina_park "Emergency annex. There’s a fund—fast money, short timeline. They'd pay for hiring and scaling the pilot projects. We can promise jobs fast, show metrics quicker than the developer's PR can spin their timeline."
    "You hear Nia’s breath hitch. The idea is tempting like bright bait; it would buy time, payroll, breathing space. But the memory of a checklist you once saw—strings pulled by funders with their own calendars—sits heavy: deadlines that shape priorities, not communities."
    "Rina Park's eyes are honest but determined. She leans on the bench as if anchoring herself to the room."

    rina_park "We can keep this local, Mara. We can stipulate how the funding is used. They want outcomes. We give them outcomes that save marsh and jobs. It's pragmatic."
    "You want to answer with the math, with the caveats, with the long list of ways outside money bends the arc of local plans. Instead you taste the word 'pragmatic' and it tastes like compromise."

    menu:
        "Tell the crew now—be transparent about the NGO offer":
            "You call everyone over; voices bloom into quick, messy questions. Nia bites her lip, Tomas folds his arms; there's energy, yes, but also the ripple of worry about strings."
        "Keep it quiet—consult with Elias \'Eli\' Calder first":
            "You tuck the tablet away and ask Rina to wait. Relief and disappointment flicker across Nia's face. Rina's jaw tightens; she steps back, reminding you, gently, that speed favors the bold."

    # --- merge ---
    "The crew goes back to work with a brighter urgency or a quieted tension depending on your choice; either way, the clock tightens."
    hide nia_voss
    hide mara_voss
    hide rina_park

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant, muted alarm—someone's phone, a timeline blinking awake]
    "You leave the Glasshouse with a list half-drawn in your head. There is talk of money in one hand and the smell of diesel on the other; both claim they can save people."
    # [Scene: Headland | Mid-Morning]

    scene bg ch11_e67f19_3 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano; intervals that hang like unspoken doubts]
    # play sound "sfx_placeholder"  # [Sound: The low thump of heavy equipment in sleep mode; gulls screaming over grit]
    "The headland feels colder than the Glasshouse—open, brutal, and public. You walk the gravel path toward the dock where Elias 'Eli' Calder stands, hands shoved into the pockets of his canvas vest, gaze fixed on the machines like a man inspecting a wound."
    "Elias 'Eli' Calder looks at you the way someone looks at an old map with parts rubbed away: searching for landmarks that still mean home."
    show elias_eli_calder at left:
        zoom 0.7

    elias_eli_calder "They've moved the markers overnight. Surveyors were here at dawn. Tomas says the contractor wants to start grading next week."
    show mara_voss at right:
        zoom 0.7

    mara_voss "That fast?"

    elias_eli_calder "Fast's what the contracts demand. Fast's what keeps people from worrying about rent for another month."
    "His voice narrows around 'rent' and you hear the ledger beneath it—boats serviced, nets mended, school bills. The practical measurements of survival."
    "You step closer, the salt wind tugging at the collar of your jacket. Up close, Elias 'Eli' Calder's face is more open than the town square; he looks tired in a way that isn't just about"
    "working long hours—it's the exhaustion of someone balancing on a ledger that could tip at any time."

    elias_eli_calder "So what do we do? Sit in the Glasshouse and plant daffodils while the bulldozers sketch their shadows over the channels?"

    mara_voss "We shouldn't be pitting jobs against marsh. There's a middle—pilot zones, raised docks, jobs for local boatbuilders. But it needs backing."

    elias_eli_calder "Backing means paperwork. Backing means talking to people who put up fences as gestures. Talking can be appeasing, Mara. Talking can be how important things get smoothed into someone else's plan."
    "He is not unsympathetic to negotiation; he is wary of its teeth. His loyalty pulls him toward solutions that keep hands working. You can feel the distance between your methods—data and design—and his instinct—build and maintain—like two tools pressing on the same wound."
    "Tomas arrives, slow and deliberate, map case in hand. He smells of smoke and old rope. He doesn't waste words."
    show old_tomas_calder at center:
        zoom 0.7

    old_tomas_calder "Mayor wants to see you this afternoon,' he says. 'Said it's urgent. Said 'we need a plan.'"
    "The word 'urgent' is a pleat in time. Urgent usually means a decision that will leave someone out in the rain."
    "Elias 'Eli' Calder flinches at 'Mayor'—not because of the person, but because of the way politics folds into livelihoods."

    elias_eli_calder "If you go into that office, they'll make you the face of compromise, Mara. They'll dress the concessions in ribbon and call it protection."

    mara_voss "And if I don't—"

    elias_eli_calder "Then they push through the plans and leave us picking through the marsh, wondering how we didn't see the cuts."
    "His eyes study your face. There is an edge to his worry that isn't simple opposition—it's a fear that the thing you protect may be sacrificed for a promise that isn't binding."

    menu:
        "Tell Elias you'll go and press for pilot zones—risk the label of compromiser":
            "Elias doesn't relax. He nods slowly, respect and an ache behind it. 'Just—hold the line on the channels,' he says. His voice is small with hope."
        "Tell Elias you won't negotiate—promise to double down on local projects":
            "Elias's jaw tightens; anger, then a raw fear. 'If you do that, Mara, you leave us exposed,' he says. He turns away, and for a breath you think you feel the distance grow between you."

    # --- merge ---
    "You notice how the choices split trajectories even before the words leave your mouth. There is no clean path. Only margins and the people who live inside them."
    hide elias_eli_calder
    hide mara_voss
    hide old_tomas_calder

    scene bg ch11_e67f19_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant machine coughs like a throat clearing]
    "Tomas unfolds a weathered map across the dock. He traces the channels with a finger that remembers storms you barely recall."
    show old_tomas_calder at left:
        zoom 0.7

    old_tomas_calder "Pilot zones only last if the law lines up. You need the mayor to sign protections, or else they mean almost nothing. And signatures take votes—votes take promises—and promises cost something."
    "His voice is small, but it says all the procedural things that feel like deliberate erosion: timelines, votes, contracts. You feel the weight of those bureaucratic gears grinding in the background."
    "You look at Elias 'Eli' Calder again. His expression is complicated—tight, protective, but not unmoving. The merge-rule hums at the back of your mind: you can't assume exactly where his loyalties have landed in the last"
    "weeks, only that his reaction is significant and layered. You store it as 'complex' and let it shape your next steps."
    # [Scene: Mayor Rosa’s Office | Midday]
    hide old_tomas_calder

    scene bg ch11_e67f19_5 at full_bg
    # play music "music_placeholder"  # [Music: Low strings with dissonant undercurrent]
    # play sound "sfx_placeholder"  # [Sound: The muffled bustle of the town outside; a phone on the desk humming intermittently]
    "Mayor Rosa receives you with the practiced calm of someone who balances applause and reproach daily. Her sleeves are rolled; the lapel pin of the town crest glints. There is a fatigue in her eyes that"
    "looks like late meetings and early calls, and a firmness that says decisions have consequences she must own."
    show mayor_rosa_alvarez at left:
        zoom 0.7

    mayor_rosa_alvarez "Mara. Thank you for coming. Sit, please."
    show mara_voss at right:
        zoom 0.7

    mara_voss "Thank you for seeing me on short notice. The town's on a clock."

    mayor_rosa_alvarez "I know. Council passed a motion to open negotiations with Azure Crescent. They want to propose modifications. They want community buy-in."
    "She speaks with the cadence of someone translating duty into action."

    mayor_rosa_alvarez "We can try to secure limited legal protections for pilot zones—buffer strips, restricted grading in key channels, local hiring clauses. But I won't lie: the developer's leverage is strong. Jobs are on the line and so is my seat. Compromise may be the only thing that prevents more immediate harm."
    "Her hands fold over each other; the words 'I won't lie' arrive like a weather forecast that is half threat, half policy. You can see where she stands: pushed by a need to preserve immediate livelihoods and political stability."
    "You feel a familiar tension coil—between what you know scientifically is necessary and what the town can stomach politically. The marsh does not vote. People do."
    "Rina Park, who has been shadowing you throughout the morning, leans in as if she can be the bridge between grant timelines and municipal protocols."
    show rina_park at center:
        zoom 0.7

    rina_park "If you agree to enter negotiations with the mayor, we can frame a proposal that ties pilot protections to guaranteed, measurable job placement. We get the mayor to announce it publicly—momentum builds."

    mayor_rosa_alvarez "Public announcements without enforceable language are hollow. I need something that sticks. Legal wording. Timetables. Penalties."

    rina_park "We can draft that. The funders want quick wins. We can use that urgency as leverage to secure the wording."
    "You watch the exchange and hear, again, the same danger: language that sounds binding but leaves room for interpretation. Mayor Rosa's gaze crosses to you, waiting—expecting you to translate scientific detail into political terms."

    mayor_rosa_alvarez "Mara, are you prepared to be the face of this? To stand before a crowd and tell them that what we can get is imperfect but necessary?"
    "The word 'Face of compromise' is heavy. To stand where people who trusted you might see erosion and call it trade-off—would it change the way they see you? Would it change what you did?"
    "You open your mouth, ready to thread terms between science and politics, then your phone buzzes—Rina Park's message flashing: 'They'll want terms. They'll want speed.' The kettle whistles in the distance of your memory, a reminder of the crew at the Glasshouse needing payroll."
    "Tomas's voice interrupts in your mind: 'Signatures take votes—votes take promises—and promises cost something.' The room seems to contract to the size of that sentence."

    mayor_rosa_alvarez "I need a posture from you, Mara. If we go into this, what’s the primary objective? Legal protections first, or jobs first? Because they won't be the same in practice."
    "You inhale. The marsh in your head feels exposed—channels like veins on a paper map."
    "Before you can answer, Rina Park leans in and lowers her voice."

    rina_park "There is another way. Emergency annex funding—if we accept, we can scale our pilot and show economic data in weeks. It ties us to funders' timelines, yes, but it gives us proof to bring to the mayor. It may shift the bargaining power."
    "The words hover: power, proof, timelines. Each bearing the truth that time costs in a different currency—some paid in legal language, some in a payroll ledger, some in the slow death of eelgrass."
    "Mayor Rosa folds her hands again."

    mayor_rosa_alvarez "Or you refuse to meet with them at all. Make your stand purely local. That will preserve moral clarity. It will also leave the town exposed politically. You'd be saying no to an offer of structural protections in exchange for a chance at keeping everything intact."
    "You feel the room tilt. The three pathways stretch before you like cold tide marks."

    mayor_rosa_alvarez "Mara, you must choose a posture. I cannot negotiate for you and expect the community to follow a leader who hasn't decided."
    "There is silence. The kind that holds the sound of the town leaning in, waiting. The greenhouse lights, the gulls, the thump of machines—all become background to this choice. Your chest is tight; your mouth dry."
    "You think of Nia's determined hands, of Elias 'Eli' Calder's cautious loyalty, of Tomas's maps and Rina Park's tablet."
    "You realize now that any direction will cost something: compromise, dependency, or isolation. The marsh will feel it, the town will feel it, your relationships will be bent by it."
    hide mayor_rosa_alvarez
    hide mara_voss
    hide rina_park

    scene bg ch11_e67f19_6 at full_bg
    # play music "music_placeholder"  # [Music: Single sustained violin note that fades to silence]

    menu:
        "Ask the mayor for time to consult the community and draft a hybrid proposal":
            "Mayor Rosa nods, but you see worry line her forehead. 'Time is a luxury,' she says. You step out into the hall with the uneasy certainty that consulting buys political risk but may save integrity."
        "Tell Rina to start the emergency annex paperwork now and present it as leverage":
            "Rina's face lights with fierce energy; she already has contacts and timelines. You feel the pull of money and momentum, and a small, anxious hope that speed will be your ally."
        "Refuse to enter any negotiations—commit to expanding local projects with or without outside help":
            "Mayor Rosa's face tightens. 'You'll be isolated,' she says. You feel the moral clarity you crave, but also the coldness of exposure. Tomas's maps and Elias \'Eli\' Calder's ledger spin in your head like weather charts."

    # --- merge ---
    "You stand at the mouth of a decision that will shape not only the marsh but how the town remembers its own resilience. The choice hangs like a storm front—inevitable and unforgiving."

    menu:
        "Appeal to Mayor Rosa and enter local negotiations to secure limited legal protections for pilot zones.":
            jump chapter12
        "Apply for emergency NGO annex funding to scale jobs and prove economic arguments quickly.":
            jump chapter18
        "Refuse to negotiate with the developer; double down on community projects regardless of wider outcomes.":
            jump chapter16
    return
