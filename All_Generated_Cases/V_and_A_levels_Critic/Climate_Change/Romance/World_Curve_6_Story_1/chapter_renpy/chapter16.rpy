label chapter16:

    # [Scene: Neutral Warehouse (adjacent to Rooftop Nursery) | Midday]

    scene bg ch11_ac0435_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low drone of corporate mapping drones parked at the back; a distant gull; the rustle of paper and taped fabric banners]
    # play music "music_placeholder"  # [Music: Percussive strings, building tempo — urgent, forward-moving]
    "The air inside tastes of salt and machine oil. Heat presses against the corrugated walls and the humidity wraps around your jacket like a hand. Dr. Sima's charts — neat columns of color, probabilistic swaths and"
    "confidence bands — lie shoulder-to-shoulder with Camila 'Kai' Navarro's drone-capture panoramas: laser-scanned elevation meshes, thermal slices, and glossy schematics. Coffee steam curls up from a communal thermos and carries the faint, bitter comfort of something steady"
    "in the middle of movement."
    "You feel the momentum like a physical thing in the room: a wind at your back and a pressure in your throat. Today is the hub where every small argument and all the long meetings coalesce."
    "The Rooftop Nursery's banners outside cast moving shadows through the warehouse's windows; Lio's projected murals bleed color against the far wall, a tide of painted faces and salt-slicked boats that make the stakes unmistakable."

    scene bg ch11_ac0435_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft click of a tablet waking as Elias Kahn taps it; the almost-silent whirr of a drone warming its rotors]
    "You take a breath, then another. Elias Kahn stands near the charts, his shirt slightly unbuttoned from the morning's heat, fatigue etched at the corners of his amber eyes but a steadiness in his stance that"
    "steadies others. Camila 'Kai' Navarro leans against a support beam — precise, controlled, the neoprene sheen of her sleeves catching light — her engineers clustered behind her, hands steady on tablets and tethered models. Rafi is"
    "already speaking with a neighbor in the corner, palms stained with soil; the elder — Señora Ortega — sits wrapped in a thin shawl, the room leaning in."
    "This is where the city's coastline might be decided. The room is full of voices and the smell of possibility. The arousal in you spikes — a quick, bright electrical charge. You know: this has to move, and it has to hold."

    menu:
        "Open with data; let Dr. Sima set the frame":
            "You gesture to Dr. Sima, letting her graphs do the first shaping. The room settles into methodical attention, eyes tracking colored bands and probabilities."
        "Begin with memory; make it personal":
            "You clear your throat and begin with a story — the Old Promenade at dusk, Lio's hands on a mural. The room leans in, faces softening as the technical lines tilt toward people."

    menu:
        "Press for binding community veto on any contract changes":
            "You demand a clause that gives the community veto power over post-signature amendments. Heads turn; Elias Kahn looks pained but intrigued; Camila 'Kai' Navarro's posture stiffens, the neon of the timeline stuttering."
        "Focus on establishing an independent monitoring authority":
            "You propose an independent monitoring authority with enforceable triggers. Dr. Sima nods vigorously; Rafi claps once, hard. Camila 'Kai' Navarro pauses — not rejection, calculation."

    menu:
        "Accept Kai’s fast-track with enforced oversight clauses.":
            jump chapter19
        "Push for an expanded municipal-coordinated compromise.":
            jump chapter31
        "Withdraw and devote all resources to a community-only pilot.":
            jump chapter41
    return
