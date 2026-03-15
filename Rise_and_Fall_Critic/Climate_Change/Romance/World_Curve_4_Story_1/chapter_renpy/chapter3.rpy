label chapter3:

    # [Scene: Skyfarm Terraces | Dusk]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Gentle, rising strings with light percussion — hopeful, measured]
    # play sound "sfx_placeholder"  # [Sound: Distant gull calls, a low machinery hum from the canal below, water lapping against pilings]
    # [Narration]
    "You come up the terrace steps with the echo of the lab still in your bones — Elias's palm warm against yours, the hum of simulations like a tide in your chest. The ribbon at the"
    "back of your knot brushes your neck; the locket at your throat is a cool coin of remembered shoreline. Dusk flecks the leaves of the tomato trellises gold; the air carries compost and salt and the"
    "faint metallic tang of the city's repairs. Everything feels immediate and alive."
    "You step onto a sun-warm plank and look out at the assembled faces: neighbors with callused knuckles, young engineers with tablet sleeves, the mayor's deputy with a clipboard that looks too new for this place. Old"
    "Man Toma leans on his cane like a ship's prow; Ibe's shirt has the stubborn stains of work. Serena stands a little apart from Elias, arms folded, eyes narrow but not unkind. Rin Voss arrives last,"
    "her coat a cut of storm-gray that seems to split the light — a signature that makes the murmurs in the terrace hush."

    scene bg ch3_98c6f2_2 at full_bg
    show rin_voss at left:
        zoom 0.7

    rin_voss "Good evening. Thank you for gathering with such short notice. The TideGrid is ready for phased deployment. What we propose tonight is rapid installation under a public-private compact — resources, manpower, and oversight from my firm in collaboration with municipal teams. Lives will be saved."
    # [Narration]
    "Elias shifts beside you, tablet tucked under his arm, the seedbank tin at his hip catching glints of light. He looks at you for the brief, private measure — the sort that asks, and expects, courage."
    show elias_kade at right:
        zoom 0.7

    elias_kade "Open-source architecture. Community access points. We can write the modules so neighborhoods run their own nodes. Rin — you know that's what I designed for. Transparency and local custodianship are built into the code."

    rin_voss "Ideals are admirable, Elias.' (a pause that is almost kind) 'But ideals die if the system isn't deployed at scale fast enough. We need governance that ensures reliability. That's what the compact offers: legal certainty, funding, and unified command in storms."
    # play sound "sfx_placeholder"  # [Sound: A nearby wind chime tinkles as a gull answers from below]
    # [Narration]
    "You can taste copper in the air — not just the literal metallic tang but the flavor of decision. Your chest tightens; hope glows like a flare inside that tightness. If TideGrid works, whole neighborhoods stop"
    "slipping away. If it falters, promises become ghost-marvels on a ruined shoreline. Between those outcomes, a thousand people you know live and breathe their days."

    "Mayor's Deputy" "Council needs a formal stance by midnight. We can't delay. The storm season window is closing and funding rounds are contingent on a deployment schedule."
    show serena_qiu at center:
        zoom 0.7

    serena_qiu "The codebase is robust in simulation, but we still need field diagnostics. There are edge cases. Sensor drift in brackish channels — that hasn't been stress-tested citywide. If we're going to scale, we need time for iterative debugging."

    "Ibrahim 'Ibe' N'Diaye" "Time to debug is time we don't have when water's at someone's door. But we can't let a machine tell us to stop harvesting our terraces because its algorithm thinks it's 'inefficient.' We built these terraces with our own hands."
    hide rin_voss
    show old_man_toma at left:
        zoom 0.7

    old_man_toma "When the tide was a stranger we knew the names of each dock. You hand that knowledge to a ledger and it forgets the names. Machines measure, but they don't remember why a bench has been tied to a post for eighty years."
    # [Narration]
    "The terrace tilts between urgency and caution. You listen to the cadence of voices — technical certainty, communal memory, bureaucratic pressure. Each argument wraps around you like the terraces' ropes. Hope threads through them: the possibility that technology and community practice need not be enemies."
    "You step forward because silence is a decision, too. Your voice feels like a plank underfoot — solid but narrow."
    hide elias_kade
    show maia_soler at right:
        zoom 0.7

    maia_soler "We have to be honest about what each approach asks of us. Scale buys time for many. Autonomy protects the way we live. Both have cost and both have promise. We can't pretend the choice is only one or the other."
    hide serena_qiu
    show rin_voss at center:
        zoom 0.7

    rin_voss "Ms. Soler, your work in the terraces is why the city breathes. But breaths are not enough when the lungs are wet. Partnering accelerates reach. With a trusted compact, your neighborhoods could be insured against the coming tides."
    # [Narration]
    "Her words come threaded with a rare warmth; you sense the strategic hand behind the smile. It's persuasive. Half the council leans in."
    hide old_man_toma
    show elias_kade at left:
        zoom 0.7

    elias_kade "We can design the compact to require open-source release and community oversight councils. The TideGrid's backbone doesn't have to be a leash. We can create gates — but the keys should be distributed."
    hide maia_soler
    show serena_qiu at right:
        zoom 0.7

    serena_qiu "Distributed keys are not a cure-all. Governance frameworks are messy. We can try, but we also have to model for failure modes where the centralized authority overrides local decisions for the 'greater good'."
    hide rin_voss
    show ibrahim_ibe_ndiaye at center:
        zoom 0.7

    ibrahim_ibe_ndiaye "And who sits on those councils? Lawyers in polished boots? Or the folks who know which pilings to tie in a storm? If it's the former, we lose more than land."
    hide elias_kade
    show old_man_toma at left:
        zoom 0.7

    old_man_toma "Listen to her. We remember how it was when outsiders told us what to keep. They took our stories with the earth."
    # [Narration]
    "Your mind flicks through faces: neighbors who taught you to graft cuttings onto rooftop soil; kids who chase light across the boardwalk; Elias, who can make equations sing like lullabies for cities. The question isn't merely"
    "technical. It's about trust — between you and your neighbors, between you and Elias, between your community and the people who hold power."
    "You can feel Elias beside you, patient insistence written on his profile. He reaches out, an absent-minded brush of fingers against your sleeve, as if to anchor both the moment and you."

    menu:
        "Squeeze his hand back":
            "You return the gesture quickly, a small pulse of warmth that steadies you. Elias's smile is brief, full of that impatient kindness that asks you to leap, and for a moment you imagine how aligning might look — tangible crews, lit nodes along the canals, people waking to steadier mornings."
        "Step between the council and Rin":
            "You plant both feet on the plank and step forward, the sun-warm wood grounding you. Your voice rises with practical authority; you begin mapping out how oversight councils might be formed, naming neighbors for seats and sketching accountability measures in the air."
        "Fold your hands and listen more":
            "You fold your hands at your waist and let the terrace speak. Faces soften when their stories are heard; you note phrasing, snatches of concern and hope. In the quiet, you start assembling a compromise in fragments — what oversight could look like, what guarantees matter most to the people at this table."

    # --- merge ---
    "The reactions ripple. Elias's eyes find yours and hold; Rin's polite smile narrows fractionally; the mayor's deputy inches a pen ready to jot. Each small motion is a vote. Hope hums — not naive, but calibrated, like the TideGrid's sensors when tuned to a steady threshold."
    # play sound "sfx_placeholder"  # [Sound: Subtle crescendo of strings; the terrace breathes with conversation]
    # [Narration]
    "You speak again, and this time you lean on specifics, because plans without particulars are paper boats."
    hide serena_qiu
    show maia_soler at right:
        zoom 0.7

    maia_soler "If we consider a pilot — modular nodes installed in partnership, with every node's firmware auditable in public repositories, and a rotating community oversight board that holds veto power for localized decisions — we might bridge the gap. We can demand timelines for debugging and legally binding clauses that prevent unilateral overrides."
    hide ibrahim_ibe_ndiaye
    show rin_voss at center:
        zoom 0.7

    rin_voss "A rotating board with vetoes? That complicates command during emergencies, Ms. Soler. Veto power can be a risk when minutes count."
    hide old_man_toma
    show elias_kade at left:
        zoom 0.7

    elias_kade "It can be engineered. Emergency override protocols can be limited to pre-agreed thresholds — transparent logs, judicial review windows. We don't have to choose centralization or chaos."
    hide maia_soler
    show serena_qiu at right:
        zoom 0.7

    serena_qiu "If we layer simulation and real-world diagnostics into each module's rollout and commit to a public bug-bounty-style program, we could mobilize civic scrutiny as a resource rather than an obstacle."
    hide rin_voss
    show ibrahim_ibe_ndiaye at center:
        zoom 0.7

    ibrahim_ibe_ndiaye "And we keep the terraces' access lines — hard stops that the grid can't lock out. If someone wants to raise water for a communal garden, they shouldn't need a permit."
    hide elias_kade
    show old_man_toma at left:
        zoom 0.7

    old_man_toma "Teach the children both the ledger and the stories. Make them keep both."
    # [Narration]
    "Around you, the terrace balances on that possibility: a hybrid, messy and hopeful, that asks everyone to do better. The strings swell with something like cautious cheerfulness. You feel the old, heavy weight of responsibility fold"
    "into a bright, practical hope: the idea that design can be democratic and that democracy can be designed."

    "Mayor's Deputy" "You will need to give a formal stance tonight. The council expects clarity."
    # [Narration]
    "Your throat tightens — but not with defeat. With the small, fierce relief of a person who knows an honest path is possible. You look at Elias. You look at Rin. You look at the faces"
    "that have given you your life in this city. Each look is a question. Each question is also an invitation."
    "Your decision will matter. The city will watch. And whatever you choose, you will carry that choice into the terraces and into people's mornings."
    hide serena_qiu
    hide ibrahim_ibe_ndiaye
    hide old_man_toma

    scene bg ch3_98c6f2_3 at full_bg
    # play music "music_placeholder"  # [Music: Strings resolve into a hopeful pause]

    menu:
        "Join Elias and accelerate TideGrid deployment":
            jump chapter4
        "Expand grassroots resilience—refuse TideGrid":
            jump chapter7
        "Broker a hybrid—demand community oversight":
            jump chapter10
    return
