label chapter4:

    # [Scene: Tideward Promenade | Morning]

    scene bg ch4_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Urgent strings with a forward-driving rhythm]
    # play sound "sfx_placeholder"  # [Sound: The low thrum of generators; seagulls arguing above; a steady, distant surf]
    "You arrive with your notebook pressed to your ribs like an anchor. The pages have a warm impression from where your hand rested last night; salt grit collects in the cuff of your jacket. Around the"
    "pavilion, HelioCorp technicians move with practised efficiency—clipboards, laminated schematics, a bright, clinical calm that smells faintly of ozone and coffee. The community cluster—Mina, a few terrace volunteers, and Elias—stands as a contrast: muddy boots, sun-dark hands,"
    "laughter threaded with nervousness."
    show aiko_mori at left:
        zoom 0.7

    aiko_mori "Thank you for coming,"
    show dr_rowan_hale at right:
        zoom 0.7

    dr_rowan_hale "We appreciate the invitation, Ms. Mori."
    "He inclines his head with the precise politeness of someone used to being heard. 'HelioCorp's goal is rapid, reliable protection. Our pilot is modular—deploy sensors, a temporary barrier, real-time modeling. We want to move quickly.'"
    "He speaks like a clean algorithm. The air tightens—speed is an attractive word when tides are impatient. You feel the heartbeat under your ribs quicken; hope and caution cross in a two-step you know well."

    aiko_mori "Speed is necessary,' you admit, flipping the notebook open. 'But not at the cost of governance. We will agree to a pilot if we have an oversight charter—jointly governed. Community seats. Open-data access. Independent audits. No clauses that allow unilateral takeovers. And protections for local lands and livelihoods during construction."
    "Dr. Rowan Hale watches your hands as you list each clause, as if cataloguing. The pavilion glass reflects your face, slightly fragmented. He nods, but the world in his eyes is a set of calculations."

    dr_rowan_hale "Those are rigorous terms,' he says. 'They complicate timelines, add administrative weight—"

    aiko_mori "They also protect what you're supposed to be protecting,' you cut in. 'If the data is closed, if the contracts let decision-makers rezone and displace people, then any short-term reduction in exposure will come at a permanent social cost."
    "Dr. Rowan Hale: a slight lift at the corner of his mouth. 'You use 'we' carefully—you're representing a complex network of stakeholders.'"

    aiko_mori "I'm representing people who have lived here. I'm also representing common sense: transparency reduces sabotage, and community seats reduce resistance. You want sensors to work; let the community know what the sensors see."
    "Dr. Rowan Hale's eyes sharpen; there's a pause long enough for the tide to make the silence thicker. Around you, members of the terrace mutter agreements. Elias Chen's hand finds yours and squeezes—brief, stubborn. You feel the pressure like a promise and a plea."

    menu:
        "Push harder on the independent audits clause":
            "You lean forward, redoubling your gaze on Rowan. 'Independent audits, with auditors chosen jointly.' The room takes the suggestion into its hands like a shared tool—someone whispers, 'Yes.'"
        "Smile and accept the charter outline, saving negotiation capital":
            "You let out a breath, folding the clause list back into the notebook for the moment. 'Let's make the oversight practical—clear timelines and an appeal process.' Elias relaxes a fraction, nodding."
        "Defuse with a small joke to ease tension":
            "You half-smile. 'And coffee at every board meeting—roasted locally.' A short, honest laugh breaks the edge; Rowan's expression loses the thinnest filament of steel."

    # --- merge ---
    "The negotiation resumes; the room moves toward concrete terms and concessions."
    "Dr. Rowan Hale exhales, a tiny concession in the shape of a sound."

    dr_rowan_hale "Independent audits can be arranged,' he says after a beat. 'And community seats—two, initially, with observers at the modelling table. Open-data access via an API. We'll need to define scope—sensor types, placement, data latency. We will not sign anything that allows displacement without community consultation. HelioCorp will fund the pilot's initial costs."
    "The words arrive fast—an efficiency you recognize from the other world you used to inhabit. Each item is a checkbox being marked. Your cheeks warm with an adrenaline that tastes like triumph and fear."

    aiko_mori "We need iron-clad language about data ownership,' you reply. 'And I want a clause that allows the pilot to be paused for independent review."
    "Dr. Rowan Hale: (considering) 'Reasonable. Pause authority will require a joint quorum. We'll draft language for the charter today. Our legal team can have a working draft by evening.'"
    "Mina Kuroda steps forward, her hands still smelling of lemon and soil."
    show mina_kuroda at center:
        zoom 0.7

    mina_kuroda "And the crew—if they're going to work on our pads, they eat from our kitchen. They learn where things have always been planted. They don't bulldoze memories."
    "A soft, genuine smile unfastens Dr. Rowan Hale's composure; for a swallow of seconds, his suit reads less like armor and more like clothes on a man thinking of his own losses."

    dr_rowan_hale "Then HelioCorp crews will eat in your kitchen. We'll have community liaisons embedded in the morning shift. Protocols for site sensitivity will be observed."
    "You write it down. The pen scratches fast; the notebook swallows terms and conditions like a ledger of trust. Elias Chen watches every word get inked, thumb tapping a staccato rhythm against his thigh."
    hide aiko_mori
    show elias_chen at left:
        zoom 0.7

    elias_chen "Aiko—"
    "He looks at you, the warmth in his face a low, steady flame. 'Are you—are you sure we can keep the power where it belongs? I don't want to wake up to giant machines deciding where our nets go.'"
    hide dr_rowan_hale
    show aiko_mori at right:
        zoom 0.7

    aiko_mori "We keep it in the charter,' you say. 'We keep veto power on rapid deployment that affects displacement. We make the model open so community experts can interrogate it."
    "Elias Chen looks unconvinced but nods, and then he says, softer, 'Okay. We'll hold them to it.'"
    "Dr. Rowan Hale watches that exchange, his pale-blue gaze lingering on Elias Chen for a beat longer than a courtesy requires. He inclines his head toward you in a way that carries something like respect—sharp, focused, and oddly warm."
    hide mina_kuroda
    show dr_rowan_hale at center:
        zoom 0.7

    dr_rowan_hale "Ms. Mori, your rigor is commendable. It's rare to see a community leader with both technical fluency and the patience to litigate ethics. HelioCorp will cooperate under those constraints."
    "The compliment lands like a hand on your shoulder. You're seen. It's disorienting in the best way."
    # [Scene: Tideward Promenade | Midday — Installation Begins]
    hide elias_chen
    hide aiko_mori
    hide dr_rowan_hale

    scene bg ch4_453e40_2 at full_bg
    # play music "music_placeholder"  # [Music: Percussive rhythms layered with hopeful brass]
    # play sound "sfx_placeholder"  # [Sound: Metal on metal; the cheerful din of organized labor; a gull's cry turned triumphant]
    "Work starts at a sprint. Sensors get anchored into rebar pilings; data cables disappear beneath sandbags. You move through the scene like a conductor—checking placements, annotating coordinates, looping community liaisons into the command line. HelioCorp engineers"
    "explain the telemetry; you ask pointed questions about redundancy and data encryption. They answer, sometimes too fast, sometimes with patient diagrams."
    "Your notebook gains a new weight. Pages fill with timestamps, clause references, and a margin scribble—'community seat names'—then a quick sketch of the promenade's cross-section where marsh grasses will soft-baffle wave energy."
    "Elias Chen is everywhere: hauling a crate, knotting twine, planting the first line of cordgrass where the engineers say the sensors won't be disrupted. He moves with a kind of focused stubbornness that suits him—action as an argument."
    "Mina Kuroda appears with steaming bowls from the Beacon kitchen. She hands you a bowl; the broth is salty and home. You lift it to your lips and taste the neighborhood: kelp, miso, and the iron tang of fast work."
    show mina_kuroda at left:
        zoom 0.7

    mina_kuroda "This is politics served hot,' she teases. 'Eat it now; you'll have no time later."
    "You laugh, the sound raw but bright."
    show aiko_mori at right:
        zoom 0.7

    aiko_mori "We keep the kitchen open for crews,' you tell her. 'And we schedule harvest times around installation."
    "Mina Kuroda nods approvingly. 'Good. They need to learn hoe and heart.'"

    menu:
        "Plant beside Elias, matching his rhythm":
            "You kneel in the same trench, trowel in hand. Elias grins and hands you a seedling; your fingers find the same dirt line. Our movements sync for a few minutes—silent, effective."
        "Plant at the fringe, focusing on marsh resilience":
            "You plant farther along the curve, aiming for the buffer zone. It gives you a vantage to watch both sensors and people. Elias looks up and gives you a brief nod—concern folded into trust."
        "Step back and observe, updating the log instead of planting":
            "You hover by a sensor, inputting notes and verifying coordinates. Elias catches your eye and raises his trowel in a small salute. You feel useful in a different, quieter way."

    # --- merge ---
    "Planting proceeds in its communal rhythm; sensors come online and the team's work coalesces."
    "Hands dirty, you feel alive. The tempo is fast; conversations cascade into technical clarifications and jokes about leaking boots. HelioCorp crews and terrace volunteers match tools and ideas. The modelers set up a temporary substation on"
    "a raised platform—laptops humming, a server with amber LEDs blinking like a new constellation. People cross the new border lines—corporate badges and hand-stitched aprons overlapping."
    "Dr. Rowan Hale appears at the edge of the terrace, sleeves rolled back against the day. He watches the planting for a long moment, quiet as if taking inventory of an orchestra before its swell."
    show dr_rowan_hale at center:
        zoom 0.7

    dr_rowan_hale "This is good,' he says finally, stepping into the light. He speaks with a voice that has lost none of its clarity, but the steel has a warmth now. 'Seeing the sensors integrated with living buffers—that balance was the point, wasn't it? Technology that compliments ecologies, not replaces them."

    aiko_mori "Yes,' you reply. 'We can't build walls without roots."
    "Dr. Rowan Hale's gaze shifts to you, and that look—attention sharpened into appreciation—carries a pressure you haven't felt in some time. Somewhere in it is gratitude; somewhere in it is a tacit recognition of competence that almost set a strange, private thing alight inside your chest."
    "Elias Chen, passing by, catches the exchange. The set of his jaw is small, almost invisible, but you catch the thin line of worry etched there. He gives you a quick, private smile that tries to fold the concern away."
    hide mina_kuroda
    show elias_chen at left:
        zoom 0.7

    elias_chen "Don't let him make you soft,"

    aiko_mori "I never rely on anyone to be soft for me,' you answer, planting the grass with a practiced motion. 'I rely on people being careful."
    "Elias Chen snorts. 'That sounds very Aiko.'"
    "He grins in a way that makes the line between laughter and care precarious and warm. The two of you work in companionable silence for a stretch—brief touches, shared tools, and a rhythm settled into partnership."
    "Back at the command platform, the first sensor pings green. A small cheer rises like bubbles surfacing. Someone records it; someone else sends the raw telemetry to the open-data endpoint you insisted on. The line of"
    "numbers scrolls across a screen; the terrace's volunteer scientist—an enthusiastic teenager with paint on his forearms—points to a graph, then to the marsh, then to the seedlings, as if tying threads visible to some people but"
    "invisible to others."
    "Mina Kuroda claps you on the back. 'Look at you—Aiko Mori, running corporate pilots and community kitchens.'"
    "You laugh again, this time with a fullness that loosens your shoulders."
    "Dr. Rowan Hale steps closer, lowering his voice so the nearby radios won't catch it."

    dr_rowan_hale "You negotiated well. There are risks in openness, but you made the safeguards legible. You made the pilot something I can be proud of."

    aiko_mori "I'm not asking you to be proud,' you say, throat tightening. 'I'm asking you to be accountable."
    "Dr. Rowan Hale: a pause. 'They're not mutually exclusive.'"
    "He meets your eyes and his hand lifts, a small, unexpected gesture—an echo of the compass he keeps. 'If this pilot succeeds it will be, in part, because of people like you.'"
    "You feel seen again, but this time the sight is more complicated: admiration folded with the strain of consequences yet to be measured. Elias Chen watches you two, his expression unreadable for a breath, then softens with an exhale that says he's staying in this, whatever it will require."
    "Your notebook collects the last set of timestamps. You jot down the quorum rules, the pause authority language, and the early schedule for audits. Your handwriting becomes a map of promise and contingency."
    hide aiko_mori
    hide dr_rowan_hale
    hide elias_chen

    scene bg ch4_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: The strings swell—hopeful, urgent]
    # play sound "sfx_placeholder"  # [Sound: The surf hushes to a steady pulse; distant laughter; a single sensor pinging again, steady and sure]
    show aiko_mori at left:
        zoom 0.7

    aiko_mori "You can feel the ledger turning—this page thick with compromise and action. There is an electric thread that ties the sensor's green light, Elias's dirt-streaked smile, Mina's steady hands, and Rowan's cautious praise. It hums through you like current."
    "You stand at the terrace edge, the breeze pulling at your hair and bringing the taste of brine and soil to your mouth. Everyone around you moves like a promise being kept—fast, loud, and fragile. The pilot breathes. So do you."
    hide aiko_mori

    scene bg ch4_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Crescendo—bright brass and driving percussion]
    # play sound "sfx_placeholder"  # [Sound: A chorus of activity; a distant bell from the Beacon]
    "You close the notebook for a moment and let your fingers rest on the cover. The trust is taut, like rigging on a ship. It holds. For now, it holds."
    "Page-turn thought: This is what momentum feels like—hard-won knots tied quickly, hands raw and hopeful. Something begins now that cannot be unbegun."

    scene bg ch4_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
