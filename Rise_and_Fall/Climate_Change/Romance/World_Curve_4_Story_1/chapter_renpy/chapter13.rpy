label chapter13:

    # [Scene: Municipal Planning Office | Morning]

    scene bg ch12_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, taut piano; a slow, descending motif]
    "You sit at the head of the table with the Moleskine closed beside your elbow, its spine still carrying the impression of a seal. The room smells of strong coffee and printer toner, undercut by the"
    "wet, metallic tang of the harbor wind pushed in through the door each time it opens. Your jacket is damp at the shoulders from the walk—salt in the fabric that will hold its memory."
    "Mayor Anton folds his hands, the paper between them soft from reading. Tomas is to your left, fingers tapping the edge of his tablet; he doesn't look at the screen, only at you. Rosa stands near"
    "the doorway with a thermos, palms still seeded with soil—her presence is as steady as the peat she tends. Across the table a third-party auditor—two grey suits and an older woman with a cropped salt-and-pepper haircut—sets"
    "down a thick, stamped folder."
    show mayor_anton_chi at left:
        zoom 0.7

    mayor_anton_chi "Thank you for coming. We've had staff draw up what we'd discussed. It's an oversight pact—binding language, independent auditors, a public steering committee. It halts suspect permits while we audit the models."
    "You listen to the words and feel them in the same place you felt the tide take your childhood front stoop: a force re-routing itself around your life. The legal phrases are smooth, familiar in their attempt to make messy living systems into checkboxes."
    show mara_voss at right:
        zoom 0.7

    mara_voss "Halting permits is the first step. Who signs off on what counts as 'suspect'? What are the enforcement mechanisms when a developer violates a conditional hold?"
    "Mayor Anton: (hesitates) 'We have criteria. The auditors will have trigger points tied to hydrology and buffer integrity. The enforcement clause—' (he taps the folder) '—allows council to issue immediate stop-work orders.'"
    "Tomas Herrera leans forward, voice soft but precise."
    show tomas_herrera at center:
        zoom 0.7

    tomas_herrera "We fund an expedited audit team for high-risk parcels. The steering committee will include two community seats with veto power over emergency approvals."
    "Rosa's voice is quiet but cuts through like a spade."
    hide mayor_anton_chi
    show rosa_marin at left:
        zoom 0.7

    rosa_marin "Community seats are good, Anton. But power on paper doesn't stop a backhoe at night. How will neighbors know quickly? How do you make the enforcement visible, immediate?"
    "The gray-suited auditor clears her throat."

    "Auditor" "We can deploy a public registry with real-time permit status and an ombudsperson line. Legally, emergency stop orders are binding—"
    "You feel the clause 'binding' like a thin seam in a levee. You know how fast water finds seams."

    mara_voss "Language matters,' you say. 'Time matters. 'Binding' must mean immediate physical stops, not just paperwork. We need on-the-ground inspection teams and a rapid-response legal fund. Otherwise, we'll have the illusion of oversight and none of the teeth."
    "A council aide shuffles in a sheet of revised text. Mayor Anton rubs his temples. His tone tightens in the way elected officials do when balancing votes and optics."
    hide mara_voss
    show mayor_anton_chi at right:
        zoom 0.7

    mayor_anton_chi "Mara, the budget constraints are real. If we insist on rapid-response teams for every action, we risk the whole package getting killed tomorrow. We need compromise."
    "You taste the word compromise like salt—necessary, corrosive."
    "Tomas Herrera finds your hand under the table and gives it a brief, grounding squeeze. He meets your eyes and says, quietly:"

    tomas_herrera "There's a drafting path. We can write trigger thresholds: any permit within X meters of defined wetlands moves into emergency status. We can specify funding sources for a rapid legal fund—phased, but guaranteed."
    "You want a firewall, not a phased promise. Your mouth tightens. This is the place where ideals are measured against ballots and line items; you have been here before, pushing soil into a sinking shovel."
    "Rosa folds her hands over the thermos, her knuckles white with conviction."

    rosa_marin "If the choice is perfect language or preserving lives, we take lives. But we mark every concession, and we mark every parcel that is given up. We make it public."
    "The auditor nods."

    "Auditor" "We will include a public register of every concession, every conditional approval, and an executive summary of the risk analysis for each parcel."
    "Mayor Anton exhales like a person letting air out of a held breath."

    mayor_anton_chi "If we sign this today—motion passes, temporary stop on suspect permits, creation of the steering committee with two community seats and third-party auditors—this is a win that prevents near-term harm and gives us time to build the program."
    "You can see the math in his eyes: political capital, upcoming elections, donors tapping at the edges. You weigh the teeth of the pact against the slow speed of municipal machinery."
    hide tomas_herrera
    show mara_voss at center:
        zoom 0.7

    mara_voss "We put conditions in writing. No night work on coastal parcels. Automatic site inspections after any storm above threshold. Veto for emergency approvals has to be executable within twenty-four hours."
    "There is a pause long enough for the rain to drum the window. The auditors confer in a whisper of paper. Tomas's fingers tense beneath the table then relax."
    hide rosa_marin
    show tomas_herrera at left:
        zoom 0.7

    tomas_herrera "We can get that verbatim. The auditors will take an addendum."
    hide mayor_anton_chi
    show rosa_marin at right:
        zoom 0.7

    rosa_marin "And community notice? Digital is good, but not everyone can check an app. Flyers, a siren system, lighthouse beacons—something everyone knows to look for."
    "Mayor Anton's mouth twitches, a small, tired smile."
    hide mara_voss
    show mayor_anton_chi at center:
        zoom 0.7

    mayor_anton_chi "We budget for a community alert line. And the steering committee gets a public communications officer."
    "The pact is compiled line by line, clause by clause; it reads dense and lawful, and also like a promise stitched together in a seamstress's dim light—functional, under pressure."

    menu:
        "Straighten the Moleskine and breathe, letting them take the lead":
            "You smooth the worn cover between your fingers, measuring relief and distrust in the same motion. You let your shoulders drop slightly, the way you allow a plan to exist before you test it."
        "Push for one more redline—immediate stop-work enforceable by community patrol":
            "You raise your voice just enough to cut through protocol. The room tilts: faces sharpen, Anton's jaw tightens, but Tomas meets your gaze with a look that says he will fight the clause."

    menu:
        "Volunteer to lead the documentation team, cataloging all concessions in real time":
            "You sign up to be the archival nerve of the movement. You stay up late compiling lists and geotags; you learn the town's parcels like the lines on a palm."
        "Focus on organizing rapid-response volunteers for physical defenses":
            "You start building chains of people, sandbag drills at dawn. Your hands remember how to move earth and breath as the town trains to be its own first line of defense."
    "THE END"
    # [GAME END]
    return
