label chapter3:

    # [Scene: Saltwren Commons | Late Afternoon]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, hopeful motif — acoustic guitar with brushed strings]

    "You feel the rooftop conversation fold into your bones like a map you've traced a dozen times. Elias Navarro's promise — light, steady, not theatrical — still hangs between you" "I will. If you let me."
    "The Commons is the place trust wears its sleeves out. Mud on your boots, the copper bracelet gone warm against your wrist, the compost-soaked scent of turned earth; these are the proofs you carry when you"
    "go into rooms that prefer plans to people. You collect a handful of what feels like evidence: a small packet of salt-tolerant sedge roots Rae Carter insisted you bring, a crumpled page from your field notes"
    "with a sketch of the proposed living berm, and the faint smear of paint on your fingers from last-minute banners."
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the murmur of people preparing to move toward Town Hall]
    "You close your eyes for one slow breath, tasting brine and tea, and feel the pull of the evening: the council hearing is the hinge everyone said it would be. Tonight, everything either edges toward cooperation or fractures into loud pieces."

    menu:
        "Double-check the seed packet in your satchel":
            "You thumb the packet between callused fingers until the label blurs into meaning: resilience, not romance. The label steadies you."
        "Walk to Town Hall with Elias—signal him with a nod":
            "When your eyes find him across the Commons, Elias Navarro meets your gaze and lifts his hand once, a small, steady signal. You walk together; the crowd parts like shallow water."

    menu:
        "Catch Elias' eye and mouth 'now'":
            "Elias Navarro nods almost imperceptibly and slides a schematic across his lap toward you. His attention is steady; his patience, a ballast."
        "Stand and prepare to speak about Saltwren's value":
            "You rise with Rae Carter's momentum. The donated chair creaks as you stand; the room tilts its attention toward you and your roots."

    menu:
        "Agree to speak in favor of Elias' hybrid pilot publicly":
            "You press your palm to the paper in your bag and nod. The decision blooms in your mouth like a first bright word. 'We'll propose the pilot,' you tell Elias Navarro, and the word feels right."
        "Decide to request a private meeting with Celeste after the hearing":
            "You fold your hands, thinking of leverage and purse-strings. 'I want to hear what she'll offer off the record,' you say, the thought practical and cold in a way that matters. Elias Navarro listens, unreadable for a beat."

    menu:
        "Support Elias' hybrid pilot publicly":
            jump chapter4
        "Meet privately with Celeste to negotiate funding terms":
            jump chapter9
        "Organize an immediate direct-action protest to block fast-tracking":
            jump chapter13
    return
