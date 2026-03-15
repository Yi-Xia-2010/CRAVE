label chapter3:

    # [Scene: Town Hall Plaza | Late Afternoon — Overcast, humidity thick after a squall]

    scene bg ch3_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low generator hum under the crowd's murmur; distant pumps thrum like a heartbeat. A gull cries once, cut short by the wind.]
    # play music "music_placeholder"  # [Music: Sparse piano chords with a slow, descending motif]
    "You come in on the tail of the market's momentum — the momentum Jonah Reyes and the co-op built, and the momentum that could just as easily bulldoze what it means to be this town. The"
    "plaza smells of wet concrete and stale coffee, with a counter-note of seawater and frying oil from a vendor who refused to close. The air sits heavy; even the banners sag, ink softened at the edges."
    "Your hands are damp at the seams of your jacket. Claire's message is a phantom at the back of your skull: I can verify model anomalies. You want to let that pull you toward a public"
    "accounting; you also feel the weight of being the person who drew the marsh terraces that could save or doom a neighborhood, the daughter who couldn't save her father. Duty, memory, strategy — they crowd your"
    "chest in equal measures."
    "A small chant rises from the crowd, then breaks like surf. Voices tilt toward both you and Jonah Reyes, hungry for a plan that isn't only rhetoric."
    "Jonah Reyes is a step beside you. He holds his camera like a talisman — not for photos now, but like a thing that might catch light or truth if the world decided to shift. His"
    "face goes pale as Elena Voss begins to speak across the plaza. He keeps his mouth shut, jaw tight, and the bandana at his wrist clenches where his fingers press."
    show elena_voss at left:
        zoom 0.7

    elena_voss "Members of the council, residents — thank you for gathering despite the weather. We know what storms have done. We know what delay costs. Our proposal delivers evacuation-ready infrastructure, reliable flood gates, and a restored business corridor. It stabilizes the economy so your children don't have to leave when the next category hits."
    "Arias of agreement ripple from some places in the crowd; sharp, practical words land like nails. Her voice is engineered for calm. The cuff on her wrist pulses faintly with telemetry; she gestures once and a"
    "holographic cross-section of her coastal barrier whirs into the halo of mist — clean lines, steel, hydraulics."
    "You want to catalog every failure implicit in that model, every neighborhood whose foundations are invisible in that cross-section. You want to say: those lines are a map of what you will lose. But Elena Voss's"
    "smile is practiced, and the crowd is not a single thing — it houses fear, need, tiredness."
    "Councilor Avi Malhotra steps up with his sleeves rolled and ink on his cuffs. He speaks slowly, as if he could make time stretch."
    show councilor_avi_malhotra at right:
        zoom 0.7

    councilor_avi_malhotra "Ms. Voss, any defense plan needs to be accountable to those who live here. We need staged protections, community oversight, and guarantees for relocation assistance if needed."

    elena_voss "Councilor Malhotra, we welcome collaboration. The model accounts for staged deployment and community liaison offices. Speed and scale are essential — delays cost lives and livelihoods."
    "Avi's eyes flick to Mara Solano and Jonah Reyes, and for half a breath you think he searches you for a sign of whether negotiation can be credible. The smell of wet rope and old paint"
    "is sharp in your nose; somewhere in the crowd a child laughs, which makes the sound ache in the wrong way."
    "Jonah Reyes presses his camera against his ribs, then speaks up with a voice that trembles but is full of something like demand."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "Speed doesn't mean taking our homes as collateral. Who's paying for temporary shelters? Who's auditing the displacement numbers? You can't just call it 'staged' and expect people to trust that they'll be the last ones moved."

    elena_voss "We will publish relocation protocols. There will be a compensation schedule aligned with market conditions."

    jonah_reyes "Market conditions don't hold our grannies' recipes or the murals on Paloma's wall. They're not marketable."
    "You can see Elena Voss's smile thin. There is a steel edge there that doesn't need to be named; she has made a career of smoothing edges into lines on a ledger. The crowd hums; some faces harden, other faces betray exhaustion and the calculus of not having options."
    hide elena_voss
    show mara_solano at left:
        zoom 0.7

    mara_solano "A barrier without wetlands is a bandage. It will keep water out of downtown but push it elsewhere. We've studied where marshes have to stay to relieve pressure — it's not just sentiment; it's physics."
    hide councilor_avi_malhotra
    show elena_voss at right:
        zoom 0.7

    elena_voss "Dr. Solano, your work is respected. But physics and policy operate on different timescales. We build what works at scale now."
    "You feel the old guilt like a salt scrape under your ribs: your father on a night when the sea remembered its teeth. That memory is not merely motivation; it's a ledger of debts you fear repaying with people's roofs and lives."

    menu:
        "Reach for Jonah's wrist":
            "You close your fingers around his skin. He's warm, trembling. He squeezes back, a brief acknowledgment that you're still here."
        "Step forward and demand data":
            "You push past the polite curl of conversation into the center of the plaza, voice loud enough that conversation fractures. Some heads turn; others close in interest."

    # --- merge ---
    "The choice is trivial, small, but it cracks something open: protective reflex, or the reactor of argument. Jonah Reyes gives you a look that is equal parts fear and something like plead."

    jonah_reyes "Mobilize the market. If we show up in numbers, we can stop them. We can push the council."
    hide jonah_reyes
    show councilor_avi_malhotra at center:
        zoom 0.7

    councilor_avi_malhotra "Numbers are persuasive, yes. But so are signed agreements. Marches without legal teeth can be pushed aside, and then we have less than we do now."
    "You can feel Claire's presence in the small vibration of your phone before you see the name flash. You fish it out with hands that smell of wet leather and salt."
    # play sound "sfx_placeholder"  # [Sound: Phone ping — a crisp, private tone]
    hide mara_solano
    hide elena_voss
    hide councilor_avi_malhotra

    scene bg ch3_98c6f2_2 at full_bg
    "It arrives like a hand at the edge of a cliff. It is both promise and danger. Publicly exposing a model's cracks could fracture trust in Elena Voss's proposal — but it could also put you"
    "in legal crosshairs, and you have no guarantee that the town or the council will believe you without Dr. Hsu's imprimatur, which might not be enough against a corporation with lawyers and LED-lit displays."
    "You think of Aunt Pilar's face; you think of the murals that have survived three rounds of salt and a generation of neglect. You think of Jonah Reyes's camera as if it were a heart that could be photographed whole."
    "Claire in the crowd? You don't know where she is. She may be watching from a distance, already in the lab, already running partial verifications. The Schrödinger static in your mind hums: you can't assume she's already published, only that she offered help."
    "Avi leans toward Mara Solano, voice an urgent whisper that nonetheless carries."
    show councilor_avi_malhotra at left:
        zoom 0.7

    councilor_avi_malhotra "If you can help me get commitments — signed, legal commitments — then we can protect neighborhoods in the short term. But I can't promise full rejection of private partners. There's pressure from the chamber to stabilize investments."
    show elena_voss at right:
        zoom 0.7

    elena_voss "Avi, with cooperation from local scientists and oversight in place, we can move quickly. We don't need a public spectacle to rush protections into play."
    "Jonah Reyes glares at her for a long beat, then to Mara Solano, as if measuring whether your resolve is an argument he'll believe in."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "If we wait for lawyers and committee meetings, they will build the barrier and call it progress while they clear us out. People will lose homes before we get signatures."
    "Your mind lists consequences faster than you'd like: immediate mobilization could spark confrontations with police, risk arrests, and push Voss to clamp down hard; negotiation could leave you complicit in carving up the town; exposure of"
    "model anomalies could delegitimize Elena Voss but invite legal and corporate retaliation, and maybe endanger Claire and you personally."
    "You want to be brave. You want to be cunning. You want to be loved without the cost of other people's homes. That triangular ache sits there plainly: love, duty, consequence."

    menu:
        "Whisper to Avi: 'What exactly can you commit?'":
            "You bend close, voice low. Avi's eyes flick, he lists potential guarantees — temporary housing funds, a community oversight board — and you hear the strain in his syllables."
        "Show Claire's message to Jonah":
            "You turn the screen toward Jonah Reyes. His jaw sets; for a second he looks hollowed out by possibility. He asks, quietly, 'Can she be trusted to go public?'"

    # --- merge ---
    "The plaza surges; someone starts a chant again and this time it sounds like a wave that might break the plaza into shards. Elena Voss offers a final, practiced concession — a staged oversight panel, a"
    "'community liaison' — and then steps back into the halo of her security detail. Her team begins to distribute slick pamphlets with renderings of promenades and cafés on terraces, all shiny and dry as if they"
    "will never touch real water."
    "The crowd swells with noise. Jonah Reyes moves as if to start the march. Avi rubs his temples and looks at the council table. Claire's message is a live wire in your pocket."
    "You realize you are standing on the knife's edge of strategy and identity. Each path is not only tactical; it will alter your relationship with Jonah Reyes, with Avi, with Claire, and with the town itself."
    "You can feel the old science in your blood telling you where water will go, and the old grief telling you what it takes to stop it."
    "Your pulse thuds in your ears. The plaza waits for the choice to fall. You can feel the tide in a different sense — not just the sea itself but the social tide that follows your decision."
    hide councilor_avi_malhotra
    hide elena_voss
    hide jonah_reyes

    scene bg ch3_98c6f2_3 at full_bg
    # play music "music_placeholder"  # [Music: Tensioned strings, descending]
    "You breathe. The options line up before you like tide marks on a pilaster."

    menu:
        "Stand with Jonah. Mobilize the market and streets now.":
            jump chapter4
        "Work with Avi to broker a compromise with Voss.":
            jump chapter7
        "Work with Claire to expose Elena's model vulnerabilities to the public.":
            jump chapter10
    return
