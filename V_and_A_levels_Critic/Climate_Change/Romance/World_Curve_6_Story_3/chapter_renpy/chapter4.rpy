label chapter4:

    # [Scene: Saltmarsh Fen | Dawn]

    scene bg ch4_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Brisk, hopeful strings with a rising percussive heartbeat]
    # play sound "sfx_placeholder"  # [Sound: The slap of boots on wet boardwalk, the light rustle of reed bundles, a murmur of voices turning into a steady hum]
    "You step off the last board and into the fen — clay that smells of peat and salt, the cold giving the ground the scent of something alive and stubborn. Dawn strips the sky into different"
    "grades of blue; the world seems to be waking with intention. Your jacket is damp at the collar, your palms raw from cord and wood, but your chest is — for the first time in a"
    "long time — a place where something else can grow."
    "Old Man Rafi stands at the shallow edge where the water kisses new soil. He has the sea in him: voice sand-rough, hands that remember nets generations ago. He passes a length of eelgrass from person to person the way priests pass wine."
    show old_man_rafi at left:
        zoom 0.7

    old_man_rafi "We give back what the storm took. We teach the tide where to bend, and it will teach our children where to stand."
    "You hold the eelgrass between calloused fingers, watching the way it trembles like a small promise. Around you, people — fisherfolk, teenagers with paint-streaked sleeves, volunteers from the Repair Garden — work with a rhythm you've"
    "only ever seen in groups that mean to survive together. Tessa is nearby, barked orders under her breath, clipboard inked with names and times, impatience bright in every motion."
    show tessa_kestrel at right:
        zoom 0.7

    tessa_kestrel "Mira, you and Jonah take the next row. Don't over-pack the sedge—remember the roots need air. And don't let Cass try to out-technic us again."
    "You glance toward the boardwalk where Jonah waits, trucker cap back on like a flag. He gives you a half-smile that says he knows your knee-jerk worry and refuses to let it have the whole day."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "Morning. Coffee later, if you promise not to make me promise anything too big right away."
    hide old_man_rafi
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "Only if you stop calling every plan 'outsider engineering' before you hear it."

    jonah_reyes "Fair. But I'm watching you. Keep those tide lines right."
    "The work itself is sweet and immediate: bundles of sedge are planted in pockets of loam, fingers slide through cold water to wedge roots into place, tarps are pegged so the marsh won't lose the seedlings"
    "to an errant gust. Children run between adults, carrying potted grasses as if they are important cargo — because they are."

    menu:
        "Help the youngest volunteer plant a sedge bundle":
            "You crouch, small hands in yours. He giggles as you show him how to angle the roots; his palm fits into yours, salt-sticky and sure."
        "Double-check the spacing of the eelgrass rows with Jonah":
            "You and Jonah kneel together, your shoulders bumping as you measure off the tide bands. He murmurs a correction and you nod; there is a private satisfaction in the shared work."

    # --- merge ---
    "Old Man Rafi hums a low chant, the kind that asks the tide to remember mercy. It feels old and right and also very new when a whole neighbourhood is humming with the same breath."
    hide tessa_kestrel
    show old_man_rafi at right:
        zoom 0.7

    old_man_rafi "We do not fight the sea. We teach it honor."
    "The statement is neither romantic nor placid; it's a plan. It is exactly the message Brinehaven needs today."
    # [Scene: Research Lighthouse | Mid-Morning]
    hide jonah_reyes
    hide mira_kestrel
    hide old_man_rafi

    scene bg ch4_453e40_2 at full_bg
    # play music "music_placeholder"  # [Music: High-tempo piano interlocked with the steady tick of instruments]
    # play sound "sfx_placeholder"  # [Sound: The low mechanical whir of data loggers, rain tapping the roof in a rhythm that keeps time with your pulse]
    "By midday you are upstairs at the lighthouse with Dr. Saira. The space smells of antiseptic and old metal, the bright kind of clean that comes from careful hands. Saira stands over a cluster of small"
    "devices — GPS modules, tide gauges, a stack of humming weatherproofed sensors — and her fingers move like someone threading the future together."
    show dr_saira_ngoma at left:
        zoom 0.7

    dr_saira_ngoma "Good work at the fen. But tell me: how will you scale this monitoring? Planting is nothing without the feedback to prove it holds."
    "You feel the coral pendant under your shirt, warm against the sternum like an answering heartbeat. Her question lands not as critique but as a point on a map you haven't yet drawn in full."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "We start with transect points along the fen, then step up to more nodes as we see stability. Community volunteers will log sunrise and tide shifts—people are already doing the heavy lifting."

    dr_saira_ngoma "People are brilliant partners. But volunteers can burn out. Who will maintain these devices when winter hits and hands go to other work? Who funds replacements after the next surge?"
    "The room tightens, not with accusation but with urgency. You know Saira is not trying to break you — she is trying to make the plan survive real winters."

    mira_kestrel "We set redundancy. Train a roster through the Repair Garden. Maybe Mayor Cole chips in maintenance funds if we show early gains."

    dr_saira_ngoma "Show her the gains. Then hold her to it."
    "You and Saira troubleshoot thresholds and alert protocols. She pushes you to formalize community-led maintenance schedules, to tie volunteer labor to modest stipends so people keep coming back. The conversation is brisk and electric — a negotiation between ideal and executable. It leaves you sharper, more certain."

    menu:
        "Sketch a simple maintenance schedule on the back of your notebook":
            "Your handwriting goes angular and purposeful. The page fills with names and times; the schedule looks like something that will actually be kept."
        "Ask Saira to help draft a quick volunteer training sheet":
            "Saira nods and pulls a blank template from her pocket. Together you outline a training drill that can be taught in an hour. It feels solid."

    # --- merge ---
    "The space smells of antiseptic and old metal, the bright kind of clean that comes from careful hands. The conversation is brisk and electric — a negotiation between ideal and executable. It leaves you sharper, more certain."
    # [Scene: Community Seed & Repair Garden | Afternoon]
    hide dr_saira_ngoma
    hide mira_kestrel

    scene bg ch4_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: Lively acoustic guitar with hand percussion]
    # play sound "sfx_placeholder"  # [Sound: Children chattering, scissors snipping, the pop of seed packets]
    "By afternoon the Repair Garden is a deliberate riot of hands and color. Kids learn to knot nets and sow salt-tolerant grasses; an elderly volunteer shows a teenager which soil amendments keep the pots from going"
    "sour. Tessa runs a roster like a maestro conducting a small orchestra of volunteers, her impatience tempered by a contagious hope."
    show tessa_kestrel at left:
        zoom 0.7

    tessa_kestrel "Okay, class — two knots, feed the roots not the leaves, and one smile per accident."
    "A kid drops a pot and both of you laugh as you scoop damp earth back into a cracked barrel. The laughter rings clear, and you realize you can feel your shoulders unclench in ways you didn't expect."
    "Cassian 'Cass' Romano arrives as the afternoon sun throws long shadows. For once his trench coat is rolled at the sleeves; his hands are dirt-smudged, his tablet tucked against his side like a talisman. He looks"
    "awkward and earnest all at once — a fish out of urban water and trying."
    show cassian_cass_romano at right:
        zoom 0.7

    cassian_cass_romano "I didn't want to miss the planting. You're doing well, Mira."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "Good. You rolling up your sleeves or just staging a photo op?"

    cassian_cass_romano "No photos. Just... learning. I want to see your methods."
    "Jonah Reyes's eyes narrow, but there is no venom — only a watchfulness that protects a community's hard-won trust. Cassian accepts the quiet challenge and, under Tessa's thinly veiled coaching, fumbles through a knot until it holds."

    cassian_cass_romano "Okay. Live knots. Teach me."
    hide tessa_kestrel
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "Start with the loop, then the tuck. Don't pull too hard."

    cassian_cass_romano "Like this? Huh. That feels... constructive."

    jonah_reyes "Not bad. Keep your hands where we can see them."
    "The banter is a rope between them: tight, tested, but not yet frayed."
    # [Scene: Boardwalk / Repair Garden — Dusk]
    hide cassian_cass_romano
    hide jonah_reyes
    hide mira_kestrel

    scene bg ch4_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Warm cello with a crescendoing rhythm — steady, building toward a swell]
    # play sound "sfx_placeholder"  # [Sound: Low conversation, the hiss of a portable stove, the occasional clink of enamel mugs]
    "Night settles without fanfare. Lantern light turns the faces of your neighbours into soft reliefs of hope. Conversations stretch long and generous. Plans are talked through again and again — not as lectures but as rehearsals, each rehearsal strengthening the muscle until action becomes reflex."
    "Jonah Reyes and you share coffee under the lanterns. His rope-and-shell bracelet brushes your wrist as he hands you a mug; the metal touch sends a tiny electric current through a place where guilt and hope meet. The contact is casual and seismic all at once."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "You did good today. The kids' knots were... actually pretty tidy. Your plans are getting legs."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "We all did. And Saira turned a corner on the monitoring plan; she wants those training sheets formalized."

    jonah_reyes "You're doing something right if even the city-slick engineers roll up their sleeves."

    mira_kestrel "Keep that up and I'll have you designing sensors by next week."

    jonah_reyes "Don't make me jealous of a laptop."
    "Cassian 'Cass' Romano lingers nearby, leaning against a post, the lantern light catching the silver streak at his temple. He watches the group with something like approval, then crosses the small distance between him and you both."
    show cassian_cass_romano at center:
        zoom 0.7

    cassian_cass_romano "Mira. Tonight — it's honest. The work, the kids. Thank you for letting me help."
    "You feel the gentle pull of gratitude. There's a complicated sweep of things — admiration, professional respect, and the memory of earlier meetings — but tonight the company is generous, and that changes what those feelings do to you."

    mira_kestrel "You showed up. That matters."

    cassian_cass_romano "I want to belong to whatever keeps this place alive. However you need me."

    jonah_reyes "Belonging means listening, not leading from back rooms."

    cassian_cass_romano "I know. I'm learning."
    "The moment stretches: a three-way compass of intent. No one moves to claim territory. Instead, everyone leans forward a little in the direction of shared work."
    "Night deepens, voices slow a beat. The talk around you turns to logistics and care: who will check the sensors at dawn, who will ferry compost, who will teach the knot class next week. The intensity"
    "doesn't fade — it consolidates into warmth that makes the lantern glow brighter in your memory than in reality."
    "Jonah Reyes's hand finds yours for an instant at the mug's rim; the world narrows to the press of skin and the smell of coffee and the low, steady tide somewhere beyond the boards. You feel"
    "something like permission settle in your ribs — permission to let hope be more than an argument on paper."

    mira_kestrel "Stay a little. Coffee's good company for solving the world's problems."

    jonah_reyes "That's my best offer. And it's non-negotiable."
    "You laugh. It comes out quick and a little wet with relief. He laughs too, and his rope-and-shell bracelet makes a gentle chiming sound against your wrist."

    menu:
        "Rest your hand on Jonah's for a long moment":
            "You let your palm stay. He doesn't pull away. Lantern light makes his skin look like brushed amber. A private, easy heat spreads through you."
        "Pull your hand back and focus on the plans spread on the table":
            "You withdraw, fingers curling around the edge of a plan. The plans feel heavier and suddenly more important — you fold them open and point out priorities. Jonah watches, not unkindly."

    # --- merge ---
    "Cassian watches you both with a small, almost-invisible smile. He looks… pleased in a way that isn’t possessive but reflective. For the first time, you think he might believe that a hybrid of engineering and community knowledge isn't just theoretically possible — it's happening in front of him."

    cassian_cass_romano "This—' (gestures to the cluster of people and light) '—this is what I hoped for."

    jonah_reyes "Then keep showing up. Actions speak louder than renderings."

    cassian_cass_romano "I will."
    "The night's conversations coil and uncoil like ropes: taut moments of argument, then slack of shared humor, then a new pull toward the same direction. You count names mentally — Tessa for the kid roster, Old"
    "Man Rafi for ceremonial memory, Saira for scientific backbone, Jonah for labour and trust. The list feels less like an inventory and more like a map of hands you can reach."
    "Everything is not solved. Funding remains a question; storms will still come; political pressure may try to twist the work into spectacles. But tonight — tonight — the town breathes differently. People move as if they have found a rhythm that can take them beyond reaction."
    "You sit back, lantern light warming the pendant against your sternum. There's a warmth at the center of your chest that is not guilt but momentum. You think of the fen, of roots taking hold, of Saira's checklist and Tessa's hubris-turned-practicality and Jonah's steady presence."
    "The arousal that has been building all day — the energy of hands joined and plans made — tightens into a single, focused ache: you want to keep this going. You want to test this new"
    "model against the next storm. You want to see what becomes of a town that chooses to braid its future together."
    "You inhale deeply, and the salt and coffee and lantern smoke mingle into a small, fierce perfume of home."
    hide jonah_reyes
    hide mira_kestrel
    hide cassian_cass_romano

    scene bg ch4_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: A single sustained string that rises and holds — hopeful, unresolved, propulsive]
    # play sound "sfx_placeholder"  # [Sound: The tide far off, steady as a metronome]
    "You let the moment sit: a living question that tastes like possibility."

    scene bg ch4_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
