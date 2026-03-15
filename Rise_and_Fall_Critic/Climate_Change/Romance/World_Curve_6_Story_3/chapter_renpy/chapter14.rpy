label chapter14:

    # [Scene: Resilience Lab & Greenhouse | Morning]

    scene bg ch14_9d8ae5_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of the wave tanks; the soft clank of metal on metal from a toolbox; distant muffled thump of heavy machinery across the water.]
    # play music "music_placeholder"  # [Music: Low, somber strings — steady, a sense of laboring forward under weight]
    "You let the morning press into your lungs: damp soil on the air, the salt-sour tang of the bay threaded with coffee and the coppery scent of pipes. For a long beat you stand with your hand on the glass, feeling the lab's breath — filtered, engineered, alive."
    "You remember the scaffold you sketched in ink last night. It was thin and careful; it held a promise. That promise is here now only as paperwork, pallets, and people because you and others translated it"
    "into motion. That fact steadies you and also makes the world feel heavier: promises in motion require tending, and tending is suddenly full of hazard."

    scene bg ch14_9d8ae5_2 at full_bg
    show noah_ros at left:
        zoom 0.7

    noah_ros "Morning.' (He appears from behind a rack of seedlings, sleeves rolled, a tablet haloed by sunlight in his palm.) 'Sensors are mapped to the trust dashboard. We're streaming live for the supply-chain feeds too — well, what we've got."
    "You can hear the cautious optimism in his voice. You also register something else: a crease at the corner of his mouth that doesn't quite belong to patience. It's the thinness of someone carrying a new burden."
    show mara_evans at right:
        zoom 0.7

    mara_evans "Show me.' (Your voice is steadier than you feel; steadiness is useful right now.) 'Walk me through the endpoints."

    noah_ros "Okay — here.' (He taps the tablet; a diagram blooms.) 'Each sensor has a public feed and an authenticated layer for the trust. Priya insisted on node-level audits. The prototypes sit on kelp terraces we're planting this week. Arman's crews are paired along the core; the plan was—' (he hesitates) '—the plan was parallel deployments. Redundancy. Equity."

    "Priya (off-screen, calling over)" "We built redundancy where we could. But the grant ledger is showing delayed disbursements. The vendor shipments are flagged at the port."

    mara_evans "Delayed by how long?"
    show priya_anand at center:
        zoom 0.7

    priya_anand "They're estimating two to four weeks on critical components. Some bioplastic panels are backordered. It's not catastrophic for planting — but it slows workforce hiring, stipends, and certain anchoring gear."
    "Your chest tightens. Delays were always possible; the way they gnaw at people who rely on paychecks is what makes them personal. You feel the air go a little thinner around your lungs."
    hide noah_ros
    hide mara_evans
    hide priya_anand

    scene bg ch14_9d8ae5_3 at full_bg
    "Noah Ríos: (softly) 'There's another thing. Cass called. She... she wants to keep public messaging positive. She thinks a bump in confidence now keeps the hybrid viable.'"
    "You consider the cascade that optimism can cause: more volunteers showing up, donors reassured, media narrative contained. You also know the other side — how silence can be an erasure when public trust demands transparency."

    menu:
        "Point out the delays at the next briefing":
            "You say nothing at first, then quietly: 'We need to flag the delays in the briefing. People deserve to know what to expect.' Noah nods, relief flickering across his face as if someone finally vocalized what he'd been bracing for."
        "Keep it quiet to avoid panic":
            "You press your lips together and run a thumb over the pendant. 'Not yet,' you murmur. 'Not on the dais. We'll manage the fallout internally.' Noah's eyes hollow a beat — grateful and uneasy — and he tabs something on his tablet."

    # --- merge ---
    "The choice floats away almost before you decide; for now the lab needs hands. You move through it anyway, issuing instructions, correcting a planting angle, smoothing a tension on a mooring rope. Physical labor is a refuge when politics pinches the stomach."
    # [Scene: Harbor Core Construction Site | Midday]

    scene bg ch14_9d8ae5_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The steady beat of pile drivers; a distant public-address announcement; gull cries; boots in wet sand.]
    # play music "music_placeholder"  # [Music: Percussive low notes — the sound of industry continuing while tension increases]
    "You walk the cordoned perimeter, map and tablet in hand. Engineers hand you blueprints with measured confidence; community volunteers point out access points that must remain open. You sketch on the back of an envelope, annotating the plans with elbows and knees and feet — the shapes of the everyday."
    "An Arman foreman meets you at one of the demarcation lines, palms open like an apology wrapped in policy."
    show arman_kade at left:
        zoom 0.7

    arman_kade "Ms. Evans. Progress, yes? This will safeguard the port's economic spine."
    show mara_evans at right:
        zoom 0.7

    mara_evans "It will safeguard the economic spine. People need safe access too. We agreed on public corridors at forty-meter intervals."
    "Arman Kade: (smiling) 'And we will honor corridors where practical. There's always room for operational adjustments.'"
    "You study his eyes and feel the coral of distrust bloom. His smile is professional; it hides the kind of calculation that measures access rights in profit margins."
    "Later — in the shade of an equipment pallet — Priya shows you a printout, thumbnails of contractual language scrawled in lawyers' shorthand. Her finger stops at a clause that wasn't there yesterday."
    show priya_anand at center:
        zoom 0.7

    priya_anand "This amendment slipped through in the investor rework. It's a management clause. It allows privatized control of 'access strips' under emergency operation conditions."

    mara_evans "They can't do that."

    priya_anand "Legally it's amber — not automatic seizure, but a broad delegation of control. Cass is aware in the abstract; she didn't want a press scene. I—' (she exhales) '—I didn't see it until legal redlines landed."
    "The machinery thumps, uncaring. You think of the alley behind Elena's bakery, the graffiti on the door you traced as a child, the way the air holds bread at dawn. A clause on paper feels suddenly like a length of rope around a future you were promised."
    # [Scene: City Council Backroom | Early Afternoon]
    hide arman_kade
    hide mara_evans
    hide priya_anand

    scene bg ch14_9d8ae5_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The muffled applause from the public dais beyond; a coffee machine sputtering.]
    # play music "music_placeholder"  # [Music: A single, descending piano motif — the mood slackens]
    show cassandra_cass_green at left:
        zoom 0.7

    cassandra_cass_green "Mara. I know this looks bad. The amendment's language came from the investors' counsel. They argued the city's liability needs a mechanism to act quickly in emergencies."
    show mara_evans at right:
        zoom 0.7

    mara_evans "That's argument language. The effect is privatization of access. It lets management lock down strips that people rely on for livelihoods."
    "Cass: (softly) 'I pushed back as far as I could. We hammered out transparency requirements and review windows. But politically, I couldn't force a veto without risking the entire hybrid package and funding. This was the trade.'"
    "Mara Evans: (your voice tight) 'You traded space where people live and work for a promise of speed.'"
    "Cass stares at you, then at the table. Her hands are steady in ways you wish for yourself."

    cassandra_cass_green "Trade-offs are cruel. I know. I chose the path that keeps the most people in place. I chose to bind investors into public audits they can't easily wiggle out of. We can still litigate parts of that clause. We can still legislate oversight."

    mara_evans "Can we? Or will 'oversight' mean hearings while demolition crews finish what contracts started?"

    cassandra_cass_green "We have until next week to adjust the operational parameters. The press release was scheduled for tomorrow. I don't want a spectacle that gives Arman leverage or unravels investor confidence."
    "You want to throw the press release into the harbor. Instead you feel your fingers tighten on the folder until the paper groans."

    menu:
        "Demand Cass delay the press release until the clause is publicly explained":
            "You lean forward, voice low and fierce. 'Delay it. Put the clause on the table. Let people see what we're negotiating.' Cass's jaw works; she considers the political cost and nods, a fissure of respect passing between you."
        "Ask Cass to let you and Priya work the clause quietly first":
            "You say, 'Give us till Friday. Priya and I can craft an amendment that doesn't inflate panic.' Cass exhales, relief and calculation crossing her face in quick succession, and she taps the calendar on her tablet."

    # --- merge ---
    "Cass's eyes linger on you. For a moment the city hangs between a broadcast and a backroom whisper."
    # [Scene: Abandoned Pier & Kelp Nursery | Evening]
    hide cassandra_cass_green
    hide mara_evans

    scene bg ch14_9d8ae5_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slap of water against concrete, murmured chants gathering down at the edge, the creak of old pilings underfoot.]
    # play music "music_placeholder"  # [Music: Sparse strings, a single mournful cello line]
    show tomas_belmar at left:
        zoom 0.7

    tomas_belmar "We are not a line on a ledger. We are the hands that pulled nets. We are the kitchens and the stories."

    "People hold homemade signs" "Our Streets, Our Lives."
    show elena_torres at right:
        zoom 0.7

    elena_torres "They rezoned my street—'managed retreat,' they called it.' (Her voice is small and then volcanic.) 'They gave us thirty days to 'assess relocation options.'"
    "You take the paper she presses into your hand. The words are bureaucratic and final-seeming in a way that feels like a slap."
    show mara_evans at center:
        zoom 0.7

    mara_evans "Who signed this?"
    "Elena: (bitter laugh) 'The zoning office. They said it was a 'preemptive classification.' No one told the people before it was filed.'"
    "A woman near you cries out, sharp and immediate. Someone passes around hot tea; the steam smells like betrayal and old bread."

    tomas_belmar "We march. We make noise. We take the pier back. We will show them this is not a negotiable ledger entry."
    "You feel something like cold come loose beneath your breastbone. Hope had been a slow-building thing; this feels like a pocket of air collapsing. The updraft that lifted you a week ago folds inward."
    # [Scene: Resilience Lab — Night]
    hide tomas_belmar
    hide elena_torres
    hide mara_evans

    scene bg ch14_9d8ae5_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant sirens ebbing; the soft click of a keyboard.]
    # play music "music_placeholder"  # [Music: Low, restrained piano — grief that hasn't yet found an outlet]
    "Noah Ríos meets you near the labs' back door. His face is thin and apologetic, as if he's been parsing blame in the dark."
    show mara_evans at left:
        zoom 0.7

    mara_evans "Priya told me about the amendment. She showed me the clause. Why didn't you —"
    "Noah Ríos: (rubs the back of his neck) 'I didn't... I saw redlines on the schedule, I saw the supply delays, and I thought if we didn't keep the narrative together investors might pull. I thought"
    "we could renegotiate the language in time. I—' (He stops, because words are blunt tools for this kind of wound.) 'I didn't foresee the legalese being used that way. I didn't think they'd write 'management' to"
    "mean 'privatized access.''"

    mara_evans "You work with them. You sat across tables with these people."
    show noah_ros at right:
        zoom 0.7

    noah_ros "Yes. I sat there because we needed capital to make the sensors open-source and durable. I thought tying them into the trust would bind investors to transparency. I thought we could make the tech a lever for public accountability."
    "You search his face for malice and find none — only the small, porous fear of someone who wanted to be useful and found their usefulness translated into concession."
    "Mara Evans: (whisper) 'Noah—'"

    noah_ros "I am sorry. I am so sorry. I didn't read every phrase. I trusted the lawyers, the drafts. I thought Priya's audits would be enough."
    "The conversation thickens: apology, defense, shame. You say things you have been holding back for nights: that trust is more than code, that people's livelihoods do not translate easily into mitigation plans, that a clause on paper is a door when built with the wrong hinges."

    noah_ros "What do you want me to do?"
    "Mara Evans: (the question is a physical weight) 'Tell me you will fix it. Tell me you'll help me fix it. Help me choose how to stop this from becoming a cage.'"

    noah_ros "I'll do whatever you ask. Public spectacle, legal wrangling, quiet patchwork — I'll stand with you."
    "A long silence follows. You can hear the cold grind of the city's mechanics, indifferent and relentless."
    hide mara_evans
    hide noah_ros

    scene bg ch14_9d8ae5_8 at full_bg
    "You feel the sense of responsibility tighten into something painful and operable: a choice to be made now, with reputations and people's homes on the line."
    "You think of Elena's letter, of Tomas at the pier, of volunteers laying kelp in the rain. You think of Cass' calculated politics and Priya's legal drafts. You think of Noah's apology and his hands, steady once when wiring sensors."
    "You know, with a certainty that makes your mouth dry, that whatever you choose will alter the texture of this campaign: it will change trust and trajectory both. You are at the hinge again, and this"
    "time the hinge is made of law, press releases, and the small faces among the crowd."

    scene bg ch14_9d8ae5_9 at full_bg
    # play music "music_placeholder"  # [Music: A single dissonant chord held, then faded]
    "You gather your notes, the clause printout, Priya's annotations, and Noah's tablet. You stand in the doorway, feeling the weight of the city like weather on your shoulders."

    jump chapter15
    return
