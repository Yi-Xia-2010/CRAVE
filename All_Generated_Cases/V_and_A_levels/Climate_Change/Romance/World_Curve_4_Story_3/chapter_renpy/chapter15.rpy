label chapter15:

    # [Scene: Municipal Office | Late Evening]

    scene bg ch10_ef8be5_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense mid-tempo BGM — low synth under piano, steady enough to keep breath measured]
    # play sound "sfx_placeholder"  # [Sound: Distant harbor horn, rain tapping the promenade boards, the soft scrape of office chairs]
    "Narration:"
    "You step inside as the door exhales. The room smells of wet paper, brewed coffee gone cool, and the faint municipal tang of printer toner. Mayor Rosa's desk is a small island under one warm lamp;"
    "Lila Park stands by the table with a tablet in hand, its screen reflecting in the glass like an extra, clean ocean."
    "Narration:"
    "Noah is already there—leaning just enough on the credenza to look casual, a rolled map caught under his arm. He meets your eyes and gives you a narrow, honest look: steady, contained. It steadies you back."
    show mayor_rosa_alvarez at left:
        zoom 0.7

    mayor_rosa_alvarez "Thank you for coming in on short notice. We won't be long if we can keep this focused. Budget windows close fast. The council is watching."
    show lila_park at right:
        zoom 0.7

    lila_park "I appreciate everyone's time. We want to minimize disruptions. Our staged funding covers immediate sensor deployment, startup maintenance, and a pilot upkeep fund for the first six months. We can accelerate shoreline stabilization phases if we begin now."
    "Narration:"
    "Her voice is crisp, practiced—efficient as a tide gate. You notice the calibrated cadence of reassurance she offers the room, the same sentences she gives to press cameras and investors. The table between you holds a"
    "printed packet: neat clauses, page numbers, highlighted lines. The header reads 'Beacon Resilience Pilot — Terms.'"
    show asha_moreno at center:
        zoom 0.7

    asha_moreno "Community governance remains non-negotiable."
    "Narration:"
    "you say, and your voice shapes the room like a brace. 'Sensor data access, resident oversight on placements, and a clear plan for who owns the hardware after the pilot. We need local control over the interpretation and the deployment.'"

    lila_park "We want the community at the center of this. What I propose is a monitored pilot: the Beacon installs the arrays on agreed sites; we guarantee resident access to the dashboard; we fund a local liaison role. We'll agree to revisit governance structures after six months, with data-driven evaluation."

    mayor_rosa_alvarez "Six months is tight for public accountability, but it's something tangible. Re-election cycles… you know how the voters respond to immediate improvements."
    "Narration:"
    "Rosa's words sit on the table like coins — practical and precise. You feel the tug: budgets, schedules, the political calendar snapping like a net. You press the edge of a page with your thumb and taste the salt on the air as if it were a warning."
    hide mayor_rosa_alvarez
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "We need ironclad language about resident vetoes on siting and a clause that prevents unilateral asset reclassification. If the Beacon's hardware becomes 'managed assets' later, people lose their porches and their rights."

    lila_park "Third-party adjudication is standard for disputes involving multi-stakeholder assets. It prevents local disputes from freezing repair. Without it, liability becomes a standalone risk the funders won't accept."

    asha_moreno "Third-party adjudication can be a euphemism for removing local voice. Who sits on that third party? Who appoints them? Saying 'standard' doesn't address lived consequences."

    lila_park "Independent panels are composed of neutral experts. We can include community nominators.' (she taps the tablet) 'But we can't slow deployment indefinitely. The sea isn't waiting for our consent calendar."
    "Narration:"
    "The exchange tightens like rope. You feel the beat of your own pulse in your throat: the fight between speed and sovereignty, between the immediate safety of thresholds and the slow work of democratic guardrails. Lila"
    "frames urgency; Rosa frames budgets; Noah frames people in a way that insists the conversation hold its humanity."
    hide lila_park
    show mayor_rosa_alvarez at right:
        zoom 0.7

    mayor_rosa_alvarez "What about liability? If equipment fails during a storm, who pays for the damage? The town can't be on the hook."

    asha_moreno "That's why we need guarantees. Liability coverage is fine—if it doesn't become a mechanism to confiscate maintenance or to re-label infrastructure as corporate property when money shifts."
    hide asha_moreno
    show lila_park at center:
        zoom 0.7

    lila_park "We will include corporate liability coverage. It protects residents and the town from vendor collapse. But in return, we ask for managed asset language to ensure coordinated maintenance and upgrades."

    noah_reyes "Managed or not, if the agreement is written tightly, it can protect people and keep control local. We just need the definitions in black-and-white."

    lila_park "Agreed. The definitions are negotiable. We can draft them with town counsel and a community liaison. Start the pilot now; we revise governance in six months. If the Beacon meets benchmarks, we scale. If not, the terminus is the town and the contract halts."
    "Narration:"
    "It's an offer with the feel of an enclosed harbor: safe enough inside, but the gate bends toward the consortium's schedule. The phrase 'revisit governance after six months' sounds like a promise of return—a temporal leash that gives you the illusion of control in exchange for immediate action."

    menu:
        "Ask for an explicitly defined community nominator panel now":
            "You press for names and qualifications—something that can be circled in ink tonight. Lila pauses, then offers to include a clause for community-nominated seats, subject to majority approval in the six-month review."
        "Accept the six-month revisit but demand a provisional veto on siting":
            "You ask for an operational veto on sensor placement until the governance review. Lila narrows her eyes but nods; she agrees to provisional siting vetoes limited to 'critical community zones' with immediate review processes."

    # --- merge ---
    "The negotiation continues with these concessions folded into the draft terms."
    "Narration:"
    "The air tastes like paper and something metallic—anticipation and the faint ozone that follows conversations edged with law. You watch Noah work the room the way someone sets a buoy: careful adjustments, not flashy, but deliberate."
    "He references community stories—Marta's rooftop garden, Eli's repaired dinghy—and Lila visibly recalibrates, listening for the human contour behind the clauses."

    mayor_rosa_alvarez "If we take the pilot, I need contingencies for displacement. If emergency evacuations become necessary, what are our shelter guarantees? I can't promise votes on paper alone."

    lila_park "We can allocate funds for emergency housing reserves. We can also set up an emergency response partnership that prioritizes resident-owned properties."
    hide noah_reyes
    show asha_moreno at left:
        zoom 0.7

    asha_moreno "And transparency. Full audit access to deployment logs, sensor outputs, and contractual amendments."

    lila_park "Audit access will be provided to authorized municipal representatives and the community liaison. We can't open raw feeds to public servers for security reasons, but we can provide frequent vetted reports."
    hide mayor_rosa_alvarez
    show noah_reyes at right:
        zoom 0.7

    noah_reyes "Vetted reports only work if the vetting panel includes people who know how to read the data and care about outcomes—not just PR. We need training funds so residents can interpret the data themselves."

    lila_park "Training is reasonable. It builds local capacity. We'll include it in the pilot funding."
    "Narration:"
    "Each concession slides like a stone added to a levee. The structure looks sturdier for the moment. It is the kind of slow engineering you understand—layered arguments, compromises, and the occasional hard-sawn truth. And yet, when Lila's lawyer steps in to run through the contract language, the room's warmth thins."
    hide lila_park
    hide asha_moreno
    hide noah_reyes

    scene bg ch10_ef8be5_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The printer hums, the air conditioning cycles — small mechanical reminders of institutional processes]
    # play music "music_placeholder"  # [Music: Low sustain underlines the tightening tension]

    "Lila Park's Counsel" "We need to protect proprietary systems. Proprietary firmware provisions are standard. They guard IP and maintenance integrity. The 'managed assets' clause ensures coordinated upkeep—it's not a transfer of ownership; it's an operational classification."
    show asha_moreno at left:
        zoom 0.7

    asha_moreno "Operational classification that spells out removal of resident control the day investors change terms. You can call it anything. The community knows the difference between maintenance and repossession."
    show lila_park at right:
        zoom 0.7

    lila_park "Language can be clarified. We are committed to the six-month governance review and to including community representatives in that process. If the town wants different classifications then, the contract can be amended."
    "Narration:"
    "You feel each sentence like a small tide tug. Speed and efficiency lap at the argument's edges; transparency and tenure erode with each clause that defaults to corporate standard. You press for a schedule of reviews,"
    "for an explicit sunset on 'managed' language if community governance passes a majority vote in six months."

    menu:
        "Insist on a clause that requires unanimous town counsel approval for any classification change":
            "You demand unanimous counsel approval. Rosa's jaw tightens; the room goes still. Lila concedes to 'supermajority' instead—a compromise that leaves room for corporate maneuvering but signals teeth in oversight."
        "Request immediate public posting of contract drafts before signatures":
            "You ask that the full drafts be posted publicly for a week prior to signing. Lila hesitates—security and vendor privacy—but agrees to redacted posts and a summary briefing, promising fuller disclosure at the six-month mark."

    # --- merge ---
    "The contract draft is modified to reflect the compromise language and disclosure commitments."
    "Narration:"
    "The meeting becomes negotiation by increments. By the time two hours slide into the ledger, the contours of an agreement sit between you: a monitored pilot begins within weeks; funding disbursed in stages; training and audit"
    "access promised; a six-month governance review enshrined; and language that still contains 'managed assets' and 'third-party adjudication'—phrases that hum like warning buoys."
    show mayor_rosa_alvarez at center:
        zoom 0.7

    mayor_rosa_alvarez "This gives us time to act and breathing room for residents. It isn't perfect, but the council can see immediate mitigations."
    hide asha_moreno
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "It buys us time to build capacity—if we use it. If we don't, the six months will be lipstick on a corporate contract."
    hide lila_park
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "We leave the door open for renegotiation. But we make the mechanisms irreversible in favor of residents if they demand it after the review."
    hide mayor_rosa_alvarez
    show lila_park at center:
        zoom 0.7

    lila_park "That's the spirit I like. We'll draw terms that allow for community-upgrade points at the review. The Beacon invests, the town steers. It’s partnership."
    "Narration:"
    "For a moment, you let the word partnership sit in the air like a small, shaky raft. It might hold. It might not. The pilot moves from hypothetical to scheduled; signatures line the pages in blue"
    "ink. You feel the gravity of each initial, the way legal marks can rechannel whole neighborhoods."
    "Narration:"
    "You sign. They sign. The papers slide across like small, inevitable tides."
    # play sound "sfx_placeholder"  # [Sound: The scratch of pens; the soft exhale of chairs being pushed back]
    # play music "music_placeholder"  # [Music: The mid-tempo BGM holds—unresolved, not catastrophic]
    "Narration:"
    "You stand, the packet warm under your hands. Lila offers her hand—a practiced, polite grip. Rosa and Noah exchange a look that is not unhopeful. You feel like you have negotiated a shelter against the immediate"
    "storm. You also feel, coldly, that you have traded a measure of transparency for that shelter."
    "Narration:"
    "Noah stays by your side as you leave the office, his arm brushing yours in a gesture that is both private and cautious. There's so much unsaid between you—assessments and fears and a shared hunger to protect what can be protected."
    # [Scene: Promenade | Night — Immediately after]
    hide noah_reyes
    hide asha_moreno
    hide lila_park

    scene bg ch10_ef8be5_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Boards creak underfoot, gulls call distantly, a wind chime rattles like a loose tally]
    # play music "music_placeholder"  # [Music: A single minor piano line, slow; breathy synth undercurrent]
    "Narration:"
    "The night tastes of wet wood and sodium from the streetlamps. You tuck the brass compass closer to your chest; its coolness is a small, private truth against the burn of the decision. You remember your"
    "father, teaching you to read the lines of tide with a thumb and a knot—how he used to say that you could measure patience in boat rope."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "You did what you could. We have obligations now—training, audits, community liaisons. It's work. We can do the work."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "We did what we had—no, what we chose. There's a difference."
    "Narration:"
    "You let the sentence hang; it's not an accusation but a recognition of the trade."

    noah_reyes "Then let's make the work count. We'll be at every review. We'll teach as many people as we can to read the data. We won't let it become a black box."
    "Narration:"
    "His voice is low and honest. You want to believe it with your whole body. You want to believe in the training, in the panels, in the six-month review. But the legal phrases trail like cold"
    "fog: managed assets, third-party adjudication. You have seen how quickly good intentions can be rerouted into policy that protects balance sheets before porches."

    menu:
        "Walk the Promenade toward the Old Boatyard to clear your head":
            "You turn left, boots splashing shallowly, heading for the boatyard's sawdust and memory. The smell of wood and oil steadies you as you think of practical next steps."
        "Head straight home to call Eli and Marta and start organizing training sessions":
            "You turn right toward the raised gardens, already drafting a mental list of names to call. The thought of rallying people gives you a small, fierce comfort."

    # --- merge ---
    "The scene continues with your decision setting your next immediate steps in motion."
    "Narration:"
    "You don't know yet whether the pilot will preserve the town or hollow it out in slow increments. The night folds its questions around your shoulders like a damp shawl. Noah's hand finds yours for a"
    "moment, an unspoken pact: we'll be in this together. His expression is complex—encouraging and cautious, steady but not untroubled. It is all the clarity you can claim at the moment."
    "Narration:"
    "You press the compass into the inside of your jacket and let the metal cool against your sternum. Your father's lessons whisper back: measure the swell, not the rumor of it. Keep the hand steady."
    "Narration:"
    "Page-turning thought: The agreement buys time. It also writes a path someone else might follow if the pilot becomes the default. What happens when sensors begin to speak? Who will control that story? The answer will"
    "arrive not in this warm office but in the cold hum of live feeds—and in the choices people make when data becomes currency."
    hide noah_reyes
    hide asha_moreno

    scene bg ch10_ef8be5_4 at full_bg
    # play music "music_placeholder"  # [Music: Piano descends into a single held minor chord — unresolved, inviting continuation]
    # play sound "sfx_placeholder"  # [Sound: A far, faint electronic ping—unclaimed, indistinct—fades into the night]

    scene bg ch10_ef8be5_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter17
    return
