label chapter8:

    # [Scene: City Hall - Planning Office | Late Morning]

    scene bg ch7_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The muffled hum of HVAC, the occasional ring of a notification; distant gulls are swallowed by city noise.]
    # play music "music_placeholder"  # [Music: Tense, insistent strings building beneath dialogue]
    "You enter with Mateo’s blueprints tucked in their waterproof tube, the tube warm from his hand. The memory of the Council vote — your recommendation for the municipal hybrid — still hangs on your tongue like salt."
    "Councilor Nguyen sits at the head of the table, palms steepled. He is the picture of procedural calm, but his eyes flick to his tablet every few seconds. Pressure has a face here: a bald timeline, an election calendar with days circled in red."
    show councilor_nguyen at left:
        zoom 0.7

    councilor_nguyen "Ms. Navarro, thank you. We need to agree on metrics today. Recovery percentage, planting survival rates, displacement figures. We measure, we report, we show results."
    "You feel the room tighten around those metrics. Data as a lever; the lever has weight. You notice how the word 'community' is already condensed into a footnote in one of the projected slides."
    show aiko_navarro at right:
        zoom 0.7

    aiko_navarro "We should include qualitative indicators — fishing access, seasonal knowledge transfer, elder-led patrols. Those can't be reduced to a single survival percentage."
    show mateo_ros at center:
        zoom 0.7

    mateo_ros "We can translate those into proxy metrics. Participation counts, scheduled transect checks, recorded oral histories digitized and timestamped. It's clumsy, but—"
    "Tala's name arises in your mind like a flare. You can see her, arms folded, at the Aquarium, bristling at anything that sounds like formalization of their lived memory. You picture Old Man Rohan's slow, careful way of explaining tides with a story, not a chart."

    councilor_nguyen "Proxy metrics are viable, Ms. Navarro. The council needs comparables across districts. If we can't show progress in ninety days, funding becomes politically untenable."
    "The sentence lands. Ninety days. The timeline compresses the tide into a deadline."

    "You answer, because silence would be assent" "We can pilot the proxy approach, but we must build in review points that let us adjust methods if they fail to capture what matters."
    "A murmur. A councilor taps their pen. Across the table, Mateo's jaw loosens into an almost-smile. Relief smells like coffee and urgency."

    councilor_nguyen "Make them explicit. Submit a monitoring plan by Friday. Include costs, responsibilities, and community liaison roles."
    "You nod. You write it down in your waterproof notebook, thumb pressing into the page until the paper creases. The notes already look insufficient."
    hide councilor_nguyen
    hide aiko_navarro
    hide mateo_ros

    scene bg ch7_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Your pen on paper is loud as thunder in the room's thin air.]
    "You leave the meeting with the tube under your arm and a hollow tightening in your chest. Outside, the city presses at the glass; a municipal pickup idles, its hazard lights blinking like a heartbeat."
    # [Scene: Tidepark Municipal Lab | Afternoon]

    scene bg ch7_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low whirr of centrifuges, soft beeps of monitoring rigs, and the slap of wet boots on concrete.]
    # play music "music_placeholder"  # [Music: Percussive, rapid — a heartbeat accelerating]
    "Mateo Ríos walks beside you between beds where seedlings are arranged in neat grids, labels clipped like little flags. There's comfort in the order here. Machines take variables and make them legible."
    show mateo_ros at left:
        zoom 0.7

    mateo_ros "They're running the first set of survival simulations. The models predict a seventy-two percent take rate under current tidal forecasts."
    "You study the seedlings. They look small and misplaced in their tidy rows."
    show aiko_navarro at right:
        zoom 0.7

    aiko_navarro "Our elders talk about micro-topography — subtle hollows where seedlings survive storm surges. The grids flatten that variability."

    mateo_ros "We're trying to balance reproducibility with nuance. For the pilot, officials want clearly attributable results."
    "You can hear the pull in his voice: the knowledge that measurable success will unlock the next tranche of funding, the resources that could give the community time. He looks at you like someone asking permission for a compromise."
    "Old Man Rohan stands nearby, fingers stained dark from peat. He points to a marsh bed without looking at the instruments."
    show old_man_rohan at center:
        zoom 0.7

    old_man_rohan "You put them in straight lines, they drown same as they dry. Tides don't like tidy. They eat your plans."

    "A lab technician straightens, uncomfortably. A spreadsheet flashes on a screen" "SURVIVAL RATE: 72 Percentage — FORECAST ACCURATE."

    aiko_navarro "The models are useful — but they have blind spots. If we don't let place talk, data will tell a different story."
    "Rohan's words hang heavier than any output."

    mateo_ros "We can do both. We can map the hollows, then run the grid where it fits. I promise I'll push for the mixed protocol in my report."
    "You want to believe him fully. You do, with the part of you that counts tides and probabilities. But another part — the part that keeps a pressed bit of marsh grass inside her notebook — is already bracing for erosion."

    menu:
        "Examine the peat bed with Rohan":
            "You crouch, palms dampening the peat, and Rohan hums an old tide rhyme that makes the hair rise on your forearms."
        "Review the survival prediction data instead":
            "You pull the tablet close and the numbers fill you like a tide — tidy, bright, and not quite honest."

    menu:
        "Step onto the podium and speak directly to the crowd":
            "You stand, voice caught, then steadied. You speak about small hollows, about Rohan, about why metrics must listen to memory. Some faces soften; others sharpen."
        "Pull Mateo aside and draft a rapid amendment for the monitoring plan":
            "You drag Mateo to the corner, words spilling in urgent shorthand. He nods, fingers already drafting. It feels like patching a boat while the tide climbs."

    menu:
        "Fully cooperate with municipal rollout, prioritizing scale and metrics.":
            jump chapter9
        "Coordinate a public demonstration with Tala to pressure City Hall for guaranteed community governance.":
            jump chapter11
        "Secretly negotiate with Dr. Selene to include community elders in official documents in exchange for her firm's resources.":
            jump chapter11
    return
