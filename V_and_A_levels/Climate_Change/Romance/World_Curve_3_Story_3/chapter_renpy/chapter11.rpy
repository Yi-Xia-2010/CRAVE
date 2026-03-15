label chapter11:

    # [Scene: Asteria Coastal Research Lab | Post-Midnight]

    scene bg ch11_e67f19_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The server rack hums; a distant foghorn moans through the window. Soft, urgent notification pings from a muted tablet.]
    "You press your thumb to the brass tide-line pendant and feel the small ridge beneath your skin, a steady anchor under the tremor in your fingers. The encrypted folder sits in your outbox. You have read"
    "the side agreement a dozen times: shell entities, routed profits, names that map like shallow scars to Consortium board members. The logic of it is ugly and simple."
    "You forward the files to the reporter you trust. Your thumb hesitates on the final confirm. The cursor blinks. You think of the neighborhoods—the patched stalls on the Tideward Promenade, the rooftop seedlings—and of the failure"
    "that has weighted your back like a wet coat. This one could cut a path through the rot or it could tear the seams of the city wide open."

    menu:
        "Send it now, no edits":
            "You hit send; the encryption handshake starts. Your stomach drops in a way sharpened by resolve. The reporter's auto-reply arrives: 'Received. We'll hold off until we verify sources.' A small victory."
        "Delay—add oral histories as context":
            "You drag the oral histories into the packet, binding memory to ledger. The transfer time stretches; you can feel the seconds like tightening ropes. Emil's hand finds yours and squeezes, as if to say patience is also a tool."
        "BCC Asha and Emil for redundancy":
            "You add two blind carbon copies and feel ridiculous and reassured at once. The files duplicate into trusted hands; redundancy feels like a lifejacket."

    # --- merge ---

    "A soft chime replies" "Transfer complete. Encrypted receipt logged."

    "A soft chime replies" "Transfer complete. Encrypted receipt logged."
    show emil_kwon at left:
        zoom 0.7

    emil_kwon "You did the right thing."
    "(His voice is low; steady as tide-worn rope.)"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Right for who?"
    "(Your voice slides out thinner than you intend.)"

    emil_kwon "Right for the city, right for the truth. And—"
    "(He shifts, thumb tracing the seam of your paracord bracelet.) '—right for the people who don't have anyone else reading their accounting sheets.'"
    "He doesn't speak about the fallout. You don't need him to. His fingers braid around yours like a promise made of small, practical knots."
    hide emil_kwon
    hide maya_reyes

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Another ping—this one a calmed, clinical note; Asha's name flashes.]
    show asha_karim at left:
        zoom 0.7

    asha_karim "Prepare for the fallout. Make copies. Make them public if you must, but make sure the oral histories are surgically bound to the ledger. Memory reframes evidence."
    "(Her tone is brisk, not unkind. The lab's refrigerator hums as punctuation.)"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "I've already attached the histories. The reporter has the packet."

    asha_karim "Good. Now—contacts, safe transfer nodes, a backup on physical drives. Don't let a single server be the only place this lives. If they're smart, they'll try to scrub fast."
    "You feel the lab shift. Tasks proliferate like swimmers surfacing: who to call to copy, where to stash drives, which archives to encrypt. The arousal within you spikes—tight, electric—because each step is urgent and necessary."

    menu:
        "Call Diego—mobilize community archivists":
            "You call Diego. His laugh is quick and then serious: 'We'll get every oral history you have in triplicate. No one erases a neighborhood if we can help it.' It lands like a chant."
        "Send physical drives to Asha's lab":
            "You box the drives and mark them for courier pickup. Asha's response via text: 'I'll hide them in the herbarium. Plants remember.' You grin despite everything."

    # --- merge ---
    "Emil leans forward, eyes like green glass catching the lab light. He reads the transcript of the side agreement too quickly for comfort and sets the tablet down with the flattened breath of a man who measures his anger like a tool."
    "Emil leans forward, eyes like green glass catching the lab light. He reads the transcript of the side agreement too quickly for comfort and sets the tablet down with the flattened breath of a man who measures his anger like a tool."
    show emil_kwon at center:
        zoom 0.7

    emil_kwon "This is bigger than anyone thought. If it goes public without safeguards—"
    "(He stops; he searches your face.) '—people will lose roofs, not just reputations.'"

    maya_reyes "I know. I remember what we couldn't save before."
    "The memory is sharp as salt: a flooded alley, a child's toy ticking under murky water. It is why you carried the pendant home from a market stall years ago. It is why you cannot let this be a tidy corporate scandal while people get pushed into the tide."
    # play sound "sfx_placeholder"  # [Sound: Footsteps in the corridor; a low murmur rises like a second wave. Your communicator vibrates—Mayor Chen's name on the screen.]
    hide asha_karim
    show mayor_lila_chen at left:
        zoom 0.7

    mayor_lila_chen "Maya—I've been briefed. This country—this city—depends on measured responses. Panic will sink more than a scandal will. What do you propose?"
    "(voice, secure line)"

    maya_reyes "Transparency, but not terror. An inquiry that forces accountability and at the same time immediate protections for vulnerable neighborhoods. Emergency funds, temporary moratoriums on evictions—"

    mayor_lila_chen "You understand the markets will move if I call a public inquiry. Investors flee. Jobs could be at risk. These are trade-offs I cannot ignore on principle alone."

    maya_reyes "Then don't do nothing."
    "Lila's breath hits the receiver like a ledger closing. The conversation is not a negotiation; it's a scale measuring human lives, investments, and the speed of the tide."
    # [Scene: Old Beacon Lighthouse | Pre-Dawn]
    hide maya_reyes
    hide emil_kwon
    hide mayor_lila_chen

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The sea murmurs; gulls call and the lamp's mechanism ticks. Far-off, a municipal vehicle's muffled engine passes.]
    "You climb the spiral, Emil at your shoulder. The salt is in the air and on your coat; the wind smells of algae and wet stone. The lighthouse's warmth is small and honest. Here, decisions feel like they have to be named aloud to exist."
    "Asha arrives, boots leaving damp prints on the stair. She brings a canvas satchel of rolled maps and a face smoothed with lines of worry that you know mean action."
    show asha_karim at left:
        zoom 0.7

    asha_karim "The reporter will want exclusivity and quick verification. They have clout but they'll also need corroboration. If the city stalls, people in the shadows will bear the worst of it. Prepare public channels and private safeties."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "If we go public—"
    "(Your jaw tightens against the ache of possibility.) '—we pull the city's scab off in front of everyone.'"
    show emil_kwon at center:
        zoom 0.7

    emil_kwon "And if we don't, those who benefit keep building. The long game dies in silence."
    "You watch Asha's eyes—sharp and kind—and you feel something like a rope being pulled taut inside you. The arousal climbs. Each argument is a tide pulling a different shore."
    # play sound "sfx_placeholder"  # [Sound: A sudden flurry of pings; your tablet lights up: the reporter requests a face-to-face at dawn. A cascade of DMs from community members flood in, pleading, offering help, fearing what they have heard in rumors.]

    "You read the messages. A young father's voice" "If this is true, they already have plans for how to move us.' An elder: 'Don't do anything that makes the city close its doors on us."
    hide asha_karim
    show noah_ortega at left:
        zoom 0.7

    noah_ortega "We must ensure any action we take protects the city's stability. Reckless exposure could harm the most vulnerable. I urge deliberation."
    "(in the clip)"
    "You watch him and see what you have always seen: a man who believes decisiveness is a moral good. The expression on his face is unreadable—steel-gray smallness around his eyes. You cannot know where his loyalties finally land; you can only know the effect of his words."
    hide maya_reyes
    hide emil_kwon
    hide noah_ortega

    scene bg ch11_e67f19_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The reporter's confirmation—"Meet at the quay in thirty minutes. Exclusive. Bring everything."]
    "Emil's hand finds yours again, squeeze precise and urgent."
    show emil_kwon at left:
        zoom 0.7

    emil_kwon "We can push for a public dump. We can hand this to a closed inquiry. We can bargain with them—use the leak to secure protections now and keep the worst of the initial shock away."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "All three feel like compromises against something. My past failure whispers that a compromise is how we let people be lost."
    show asha_karim at center:
        zoom 0.7

    asha_karim "Then decide the compromise you can live with. And prepare for every outcome."
    "You think of the seedlings in the rooftop farm, of Diego's mapped neighborhoods, of Asha's herbarium. The city's life is threaded through your fingers—delicate, stubborn, alive. You have evidence that can tilt the balance. You have allies who will hold the rope with you. The moment compresses."
    # play music "music_placeholder"  # [Music: Tense, rising strings; the soundscape tightens into percussion—heartbeat, rain beginning to prickle on the lens]
    # play sound "sfx_placeholder"  # [Sound: The foghorn cuts once, a long, clarion note. The city's pulse ratchets up.]
    "Your pulse matches the lamp's tick and the server's hum. The decision is both personal and political, intimate and arena-sized. Each option will shape who gets to stay, who gets moved, who gets protected. The arousal hits a peak: everything is now and necessary."
    "You breathe. The pendant cools under your fingers."
    "You must choose."

    menu:
        "Publish the leak publicly—force immediate accountability and a swift political crisis.":
            jump chapter12
        "Deliver evidence to a confidential inquiry—push for systemic change quietly, protecting vulnerable residents from shock.":
            jump chapter14
        "Use the evidence as leverage in private negotiations—secure explicit safeguards for communities in exchange for delaying exposure.":
            jump chapter16
    return
