label chapter7:

    # [Scene: Voss Coastal Spire Lobby | Late Afternoon]

    scene bg ch7_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hush of an advanced HVAC; the soft click of a security loop; a far-off gull muffled by glass]
    # play music "music_placeholder"  # [Music: Low, understated piano with a cold undertone]
    "You step off the wet pavement and into a kind of clinical warmth that belongs to promises already budgeted. The air tastes faintly of ozone and lemon cleaner; your boots make a muted sound against stone."
    "The lobby smells of new leather and a synthetic citrus that tries—and fails—to cover the tang of salt on your jacket. Light slices off Elena Voss's cuff as she moves, a line you can follow like"
    "a metronome."
    "Avi is awkward in this place of hard edges. His linen suit has the faint crease of someone who slept three hours but polished his rhetoric. He counts swing votes the way other people smooth their"
    "hands—automatic, necessary. He rubs at his temple, then offers you a private nod the way you once shared conspiratorial glances in the market between stalls."
    "A cluster of Senatorial attorneys nestle near a high table, tablets open like juries. Claire stands to your left, hands flat on a dossier—her presence is steadier than the building's aesthetic. Jonah Reyes is farther back,"
    "in the gallery of observers, a patchwork jacket against the spire's clinical skyline; he looks out of place here and entirely present. His jaw is a closed hinge—so much is said in that single line."
    "You breathe in. The lobby hums like a machine that hasn't learned how to be gentle."

    scene bg ch7_453e40_2 at full_bg
    show elena_voss at left:
        zoom 0.7

    elena_voss "Thank you for coming, Councilor Malhotra. Dr. Hsu. Ms. Solano. I understand we all want the same thing: a town that survives the next century. Our model predicts—"

    elena_voss "—that a central coastal barrier with hydraulic docks will reduce inundation events by seventy-two percent under current scenario trajectories. It buys time for the entire region."
    "You feel the word 'buy' like currency sliding under the table—protection priced in increments. Elena's footage shows gleaming concrete, automated gates closing with clinical precision; the present softened to a glossy render of futures."
    show councilor_avi_malhotra at right:
        zoom 0.7

    councilor_avi_malhotra "The plan could be phased. We can secure funding and pilot zones—"

    councilor_avi_malhotra "—and that gives neighborhoods time to adapt. We can write relocation packs, easements—"

    "A senator's attorney" "We will ensure legal protections for affected homeowners where applicable. There will be compensation schedules tied to assessed lost use."
    show dr_claire_hsu at center:
        zoom 0.7

    dr_claire_hsu "Elena, those models ignore nonlinear feedbacks with salt-marsh systems. Blockage at the wrong tidal node can increase backwater flooding in low-lying neighborhoods—"

    dr_claire_hsu "—and once we harden the coastline, we lose the buffering functions that sustain fisheries and livelihoods. Permanence is not the same as safety."

    elena_voss "No model is perfect, Dr. Hsu, but our architecture is adaptive. Gates operate selectively; the promenade areas generate revenue to fund buyouts. This is progressive infrastructure."
    "You swallow. The word 'buyouts' lands like a stone. The lobby's acoustic keeps the syllable hanging between the glass and the rain outside."
    hide elena_voss
    show mara_solano at left:
        zoom 0.7

    mara_solano "A permeable revetment is not a concession. It's a living buffer. If you cut off tidal exchange and rely on gates, you're assuming repairability after storm hits—"

    mara_solano "—we need redundancy that doesn't require a technician in a tower every time the sky breaks."
    hide councilor_avi_malhotra
    show elena_voss at right:
        zoom 0.7

    elena_voss "Ms. Solano, your wetland proposals are elegant, but they scale slowly. When insurance collapses, people need immediate shelter. This is about deliverables."
    "Avi interposes, hands smoothing a folder as if order will make the argument kinder."
    hide dr_claire_hsu
    show councilor_avi_malhotra at center:
        zoom 0.7

    councilor_avi_malhotra "There is a path that threads both models. Some zones could be reinforced with engineered barriers while buffers are restored where feasible—"

    councilor_avi_malhotra "—we can map sacrificial zones, propose legal easements, and set up a community trust for displaced families."
    "You sense a loop forming: Elena reframes urgency into centralization; Avi translates risk into compromise; Claire and you counter with ecological limits. The attorneys nod; their posture is not rebellion—it's readiness."

    menu:
        "Ask Avi to delineate which neighborhoods he'd designate as 'sacrificial' right now":
            "You press Avi for specifics. He exhales and names streets you know by the tilt of their steps, using the euphemism of 'low asset zones.' The attorneys shift forward; Elena's expression tightens—this is the currency of policy, and you have bared a ledger."
        "Push Claire to explain the worst-case backwater scenario in plain words":
            "You ask Claire to strip the model's hedges and show what's likely in human terms. She draws you a cross-section in the margin of her paper, tracing water lines to a single neighborhood you grew up passing each morning. The lawyers glance at the sketch—the problem becomes less abstract and more a map of people."
        "Stand quiet and listen — catalog the faces in the gallery":
            "You hold your tongue and read the room: Jonah Reyes's jaw, Rosa's folded hands, the tilt of Mateo's head. Silence lets you gather the small betrayals and loyalties that won't appear in any chart."

    # --- merge ---
    "The meeting moves upstairs. Security doors part; the council chamber is a different animal—less theatrical than the lobby, narrower, with a ring of fluorescent strips above a long table. The public gallery is bolted on like a second story of a ship; you can feel the weight of eyes."
    hide mara_solano
    hide elena_voss
    hide councilor_avi_malhotra

    scene bg ch7_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant rain intensifies; the building's hum lowers like a held breath]
    # [Scene: Town Hall Plaza — Council Chamber | Early Evening]

    scene bg ch7_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmurs ripple like tide; a microphone feedback squeals and is shushed]
    # play music "music_placeholder"  # [Music: Sparse strings that lean into a minor key]
    "Elena Voss sets her tablet down with the same deliberate calm. She plays a short reel: time-lapse of engineered gates deploying, families walking a leveled promenade, children playing on elevated platforms. The images lean on futures that feel sanitized of mud and salt."
    show elena_voss at left:
        zoom 0.7

    elena_voss "We offer a phased plan that reduces emergency response costs and stabilizes property values. This preserves fiscal health and keeps investment coming to the entire town."
    "You hear the murmurs—some approving, many uncertain. Jonah Reyes's face in the gallery is a question mark you want to solve. You can feel him watching you the way tides watch shorelines."

    "A councilor (dry)" "What are the legal easements? How long before buyouts are executed?"

    "A senator's attorney" "We propose five-year packages with relocation assistance. Those who refuse can be eligible for enhanced local protections, subject to eligibility."
    "You think of Aunt Pilar's house—patched shutters, a rooster on the roofline of memory. Elena's 'enhanced protections' sounds like a promise with conditions you can't trust."
    show mara_solano at right:
        zoom 0.7

    mara_solano "Enhancement isn't a substitute for continuity. Dollars don't keep the stories. If we move people out of the ecological flows that have sustained them—"

    mara_solano "—you're sacrificing cultural continuity for an economic model that assumes those people will accept relocation."

    elena_voss "Ms. Solano, there are trade-offs in all emergency responses. My obligation is to propose a design that minimizes loss of life."
    show dr_claire_hsu at center:
        zoom 0.7

    dr_claire_hsu "Minimal loss of life on paper is different from erasing communal infrastructure. Fisheries depend on marsh connectivity. If we centralize defenses and the marsh dies, you've shifted risk inland. You will lose the very livelihoods you claim to save."
    hide elena_voss
    show councilor_avi_malhotra at left:
        zoom 0.7

    councilor_avi_malhotra "We're threading a needle. It will require legal language—easements, limited eminent domain in some parcels, a trust to fund buyouts. We can attach community oversight committees."

    "A senator's attorney" "Community oversight is advisory at most unless codified with binding clauses. We can draft oversight provisions."
    "The room smells of stale coffee and institutional fatigue. You translate 'codified' into the language you are trained to use: thresholds, trigger events, monitoring stations, mutable covenants. You hear your own voice shaping policy with the slow, heavy accuracy of tides."
    "You present a map—wetland buffers shaded in aquamarine, permeable revetments marked, monitored nodes flagged. The council leans in. You draw the limits: where marshes must remain, where human corridors could be reinforced without cutting tidal exchange."

    mara_solano "If we set monitoring thresholds—salinity, sediment flux, tidal prism—then we can trigger measured interventions before structural hardening becomes necessary. That's how we keep place and protection together."
    hide mara_solano
    show elena_voss at right:
        zoom 0.7

    elena_voss "We can integrate monitoring. But the primary line of defense should not be a monitoring-triggered mercy. It should be reliable, engineered protection. When the storm surge comes, your marshes may not respond fast enough."

    councilor_avi_malhotra "Then we can commit to a two-layer approach. Pilot hardening in high-traffic areas—"
    hide dr_claire_hsu
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "You keep talking about 'high-traffic areas' like they're assets and not people's streets. You can buy statistics, Elena. You can't buy a grandmother's porch."

    elena_voss "We can develop heritage funds—preserving facades and memories in curated spaces. It's pragmatic."

    jonah_reyes "Curated spaces are museums. People are still wet when the storm comes."
    "There is a quiet argument in his eyes—protective, raw. You regard him and feel a tug: the one between the public and the private, between hearts and charts."

    menu:
        "Answer Jonah directly — name the neighborhoods you think should be treated differently":
            "You call out the blocks by name, and the room seems to inhale. The attorneys exchange looks; you're offering the kind of evidence they can subpoena, but you also put faces on the data."
        "Ask Avi for an interim wording that keeps options open for wetland buffers":
            "You corner Avi quietly and propose tentative wording—'adaptive easement'—language that might keep room for ecology inside legalese. He nods, relieved to have a hinge to present."

    # --- merge ---
    "The evening wears on into a tangle of clauses. Phrases like 'sacrificial zones,' 'relocation packages,' and 'binding easements' float between you like flotsam. You keep translating between two dialects—scientific humility and procedural decisiveness—until your throat goes dry."
    "At one point, a senator's attorney asks for a motion to table certain contentious items until legal review. Avi's shoulders unknot. Elena's cuff blinks approval. You watch, aware of the small victories and the concessions that sit like stones in your pockets."
    "Dr. Claire Hsu pulls you aside when the formal Q&A ends. The hallway is cooler, and the rain outside has returned, soft and steady."
    hide councilor_avi_malhotra
    show dr_claire_hsu at left:
        zoom 0.7

    dr_claire_hsu "You didn't lose the floor, Mara. You made them consider thresholds. That's not nothing."

    "You" "Thresholds can be moved. 'Consider' is a political plea, not protection."

    dr_claire_hsu "I know. But you put ecological criteria into the record. They can be enforced. It gives community advocates something concrete. It's how policy teeth are grown."
    "You look toward the chamber door. Jonah Reyes exits not to come down to you but to stand by the plaza's railing, hands gripping salt-slick metal. His face is unreadable—something between accusation and insistence. You cannot"
    "be certain how he interprets the negotiation. The relationship between what you negotiated and what he's sacrificed is complex; it's a tide that both binds and pushes apart."
    "Avi returns with a calendar and a cautious smile."
    hide elena_voss
    show councilor_avi_malhotra at right:
        zoom 0.7

    councilor_avi_malhotra "We have a vote scheduled in two weeks. Tentative commitments from Elena on pilot zones and from the attorneys on relocation language. It won't be everything any of us wanted. But it's a step."
    "You feel the landing of that word—'step'—like something both promising and inadequate. Negotiation feels adult, practical, like mending a net with both hands and a dull needle. Inside, however, there is a slow sinking, a sense"
    "that the stitches you are making might cover over places that should remain raw—places whose names are memory and livelihood."
    hide jonah_reyes
    hide dr_claire_hsu
    hide councilor_avi_malhotra

    scene bg ch7_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain on pavement, a distant bell; the building's lights dim to a neutral glow]
    # play music "music_placeholder"  # [Music: A single, sustained cello note that fades into silence]
    "You leave with documents folded, promises mapped, and an appointment on the calendar. The vote hangs like a tide mark on the near horizon. The town's future has been parceled into meetings and clauses; the edges"
    "of what will be preserved and what will be repurposed are beginning to be inked."
    "You step back into the rain and feel the salt on your skin, sharp and immediate. The spire's lights recede behind you, and the market's neon begins to blink awake as if nothing momentous has happened at all."
    "You hold both the relief that something is moving and the grief for what compromise might shave away—a front porch swallowed into a line item, a family history folded into a relocation check."
    # [PAGE-TURN MOMENT: The calendar on Avi's tablet blinks 'VOTE: Two Weeks.' You fold your hands against your jacket and feel the weight of every possible loss and every possible salvation arranged like a tide chart. Jonah Reyes watches from the plaza, a complex look you cannot fully read. Claire's warning nags at your ribs. The town waits. You breathe; the vote will not be gentle.]

    scene bg ch7_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Low, unresolved chord]

    scene bg ch7_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter8
    return
