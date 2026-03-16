label chapter2:

    # [Scene: The Arbor | Late Morning]

    scene bg ch2_c4ca42_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm, steady acoustic loop with light percussive taps]
    # play sound "sfx_placeholder"  # [Sound: Drip of condensation, distant gulls, a radio tuned low to a community station]
    "You are at the long, scarred workbench in the Arbor. Seedlings crowd every possible surface—small green fists of life in mismatched pots and upcycled gutters. Your notebook lies open, seaweed pressed between pages like a slow"
    "tide. The air is humid and green: soil and wet burlap, a faint sweetness of compost under the sharper tang of salt."
    "Your wristband vibrates against your skin. You flip up the tablet cradle and Dr. Naomi Park’s face fills the screen—sharp glasses, grey-streaked bun wound tight; even on video she looks like someone who keeps time with tides and spreadsheets."
    show dr_naomi_park at left:
        zoom 0.7

    dr_naomi_park "Mara. Sorry to interrupt your morning. Are you at the lab or the Arbor?"
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "Arbor."

    dr_naomi_park "Good. I need an urgent run on the estuary salinity models. The latest sensor cluster reported a pulse overnight—sharp spike across the south channel. If we don't map it against the tidal prism now, we lose a window to predict the intrusion."
    "You feel the familiar slide of equations forming behind your eyes: nodes, boundary conditions, parameter uncertainties. The scientist in you sorts the problem into manageable pieces, impatient to begin. The community-minder in you feels the clock differently—people need pumps, nets, patchwork levees, and someone to show up with tools."

    mara_kestrel "How sharp are we talking?"

    dr_naomi_park "Enough that the eelgrass beds on the south flats could be stressed if the intrusion persists. Naomi's voice softens—'I hate asking this, Mara, but can you prioritize a sensitivity iteration? I can push processing from here if you initialize the run."
    "She waits—no flourish, just the professional quiet that means the data is already moving through her head."

    mara_kestrel "I can start it. Give me forty-five minutes for the initial grid, then I’ll hand it to you."

    dr_naomi_park "Forty-five. Thank you. And Mara—watch the southern transect when you do your field checks. Your wristband logs might show micro-anomalies I can't see from the fixed stations."
    "You close the tablet and set to work, but the bench is alive with voices and tools. Tess O'Malley appears in the doorway like a sudden gust—short red hair plastered to her collar from a misty"
    "walk, a council lanyard bright against her anorak. She carries a slim packet the size of a pamphlet and wears that look you know all too well: eager worry."

    "Tess O'Malley" "Mara—sorry to drop in. Busy?"

    mara_kestrel "Always. What's up, Tess?"

    "Tess O'Malley" "A council brief—leaked, if you want to be dramatic. Livia's proposal is on a fast track. There are private stakeholder meetings this week, some before the public notice goes up. I—' (she hesitates, hands folding like she's trying to keep something inside) '—I thought you should know."
    "You feel the space between air and metal tighten. Fast tracks mean fixed decisions, and this town's history is full of fast tracks that left people out in the wet."

    mara_kestrel "How fast?"

    "Tess O'Malley" "They've scheduled a sponsor pitch for Thursday, and there's talk of bringing in outside contractors to fast-deploy sections of the barrier. It's…moving quicker than anyone expected. I don't know if the council will rubber-stamp it, but Livia's got momentum."
    "Tess's eyes search yours for a reaction. On the bench, Elias 'Eli' Rowan is soldering something that smells faintly of ozone; Rafi's coffee steams nearby. Your hands hover over your notebook, between pressed seaweed and a tide-chart page gone soft at the edges."

    "Elias 'Eli' Rowan" "Speaking of moving fast—want to see something? I finished a compact harvester prototype. Light enough for one person to position, heavy enough to hold under a spring tide."
    hide dr_naomi_park
    hide mara_kestrel

    scene bg ch2_c4ca42_2 at full_bg

    "Elias 'Eli' Rowan" "It could feed small fish farms and power rooftop pumps. If we spool a few of these along the channel, they might keep the micro-lifts running even during high water."
    "You run gloved fingers along welded seams, feeling the heat of recent work. The engineer in Eli speaks in gestures and solutions; your immediate brain catalogues potential failure modes: biofouling, drag coefficients, maintenance load."
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "It's promising. What's the torque on that rotor at three-knot flow?"

    "Elias 'Eli' Rowan" "About—' (he says a number, then checks a scribble on his notepad) '—enough to turn a micro-generator. I've got a mounting idea that won't need cranes. We could prototype a line in a weekend."
    "He looks at you as if the plan is already a shared map. His gray-blue eyes are open and steady."

    "Elias 'Eli' Rowan" "We can test it today if you want."
    "A small warmth rises in your palm where his glance lands; his elbow brushes yours. His hand finds yours briefly—not a gesture saturated with history, but steadying. The contact is soft and quick, a human cable across a table of tools."

    mara_kestrel "Later. I need Naomi's run started and a field reading before we deploy anything upstream. The models will tell us where to place tests so we don't stress the beds."

    "Elias 'Eli' Rowan" "Okay. Models first. Then we build. That's a good order."

    menu:
        "Start Naomi's model now, alone":
            "You close your notebook, set up the initial grid, and let the early iterations unwrap. The familiar rhythm of numbers calms you; you like seeing patterns take shape."
        "Ask Eli to help set up the model, then head to the tide line together":
            "You gesture for Eli to bring his spare laptop. He props the harvester beside the tablet and, with a hack of humour, inputs boundary conditions. The two of you fit into a quick, efficient rhythm—hands and minds working together."

    # --- merge ---
    "You decide in a breath to split the difference: you pull the laptop into the sun and start the grid while Eli boots a secondary device to carry to the field. Rafi offers a wry whistle."
    show rafi_gmez at right:
        zoom 0.7

    rafi_gmez "That's the only way this place runs—people doing two things at once."
    "The bench chatter dissolves into the practical noise of an Arbor: metal clinks, muted laughter, and the intermittent beep of your wristband as it samples the air. Thirty minutes feels like both an instant and a lifetime of small decisions."
    # [Scene: Tide Line | Early Afternoon]
    hide mara_kestrel
    hide rafi_gmez

    scene bg ch2_c4ca42_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Water lapping, distant hammering as a pier is repaired]
    "You walk the tide line with Elias 'Eli' Rowan and Rafi. The sky is a pale, low bowl that keeps the sound close. The tide is out enough to reveal mud and the pale, trembling of"
    "roots. Your wristband chirps when you dip it into the shallows; a small readout blooms on your wrist—pH, conductivity, micro-sediment turbidity. You scribble numbers with a pen that smells of salt, the page shaking in your"
    "hand."
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "The south channel is the town's pulse. If salt pushes in, the pulse changes. We won't notice immediately, but ecosystems will."
    "The wristband ticks again. A small anomaly blinks in the conductivity stream—slightly elevated in narrow pockets near a collapsed jetty. You circle it on the map and mark a transect."
    show rafi_gmez at right:
        zoom 0.7

    rafi_gmez "You kids remember the night the old boardwalk came apart? I was here then. Looked like a curtain call—boards popped up and the whole thing folded like theater scenery."
    "He squints toward a ragged half-plank still clinging to rusted bolts."

    rafi_gmez "Felt wrong that night. Sounded wrong. People talk about losing things twice—first the wood, then the memory. We don't want that here again."
    "You listen to him, and the memory he hands you isn't just his: it's a town memory that warms and stings. It makes your hands tighten on the clipboard."

    "Elias 'Eli' Rowan" "If we place a string of harvesters along that stretch, we could reduce flow energy in those pockets and give the beds time to recover. They could act like living breakwaters—modular, replaceable, community-maintained."
    "You and Elias 'Eli' Rowan discuss placement—lengths, moorings, how to avoid scouring eelgrass. Your voice is low; you both know the models will refine his instincts if you run them properly. But there's momentum in his"
    "plan that could be used now, in a weekend, to show people a tangible option."
    "Tess's warning replays in your head. Naomi's urgent tone hangs there like a map with a missing key. The town is all at once buoyant—hands ready and ingenuity bubbling—and fragile: a policy decision could rearrange everything."

    menu:
        "Encourage Eli to set up a quick pilot at the pocket now":
            "You nod to Eli. He grins, quick and relieved, and together you haul the module into the shallows. It squeaks and bobbles, then settles, bearing its first pull. The community around you notices; a small crowd forms."
        "Insist on finishing the model run before any deployment":
            "You shake your head and point to your wristband readouts and the transect map. Eli studies the data, smiling ruefully, and agrees to wait—he trusts you. The weight of delay presses against the excitement, but an order settles: model, then build."

    jump chapter3
    return
