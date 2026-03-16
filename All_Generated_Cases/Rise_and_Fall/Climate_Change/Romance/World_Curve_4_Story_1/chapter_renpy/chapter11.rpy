label chapter11:

    # [Scene: Rosa's Greenhouse Conservatory | Late Afternoon — After the Plan to Expose Elys]

    scene bg ch10_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, steady strings with a hint of rising violin — warm and expectant]
    # play sound "sfx_placeholder"  # [Sound: Drip irrigation, a bike bell in the distance, the soft rustle of leaves]
    "You arrive with Lena at your shoulder, the greenhouse immediately wrapping you in humidity and the scent of damp soil, citrus, and salt — a small, living theater for what you’re about to do. Your Moleskine"
    "presses against your ribs like a talisman. Around the central table, people you’ve fought with and for cluster close: Rosa with a towel thrown over her shoulder, Tomas leaning against a reclaimed crate, a slim line"
    "of neighbors with phones held high like lanterns. Mayor Anton stands slightly apart, spectacles fogged at the edges of his lenses. Elys is here too, hands folded; she smiles, measured and, in your chest, unreadable."
    "This is the choice you made in Chapter Three — public exposure, in a place that holds history as much as seedlings. The greenhouse feels exactly right: warm, porous, soil between your fingers and witnesses lined up like witnesses to a tide change."
    "Rosa sets a tin of citrus tea on the table. Steam threads up into the light. Her eyes find you and for a second all the noise simplifies into a single steady thing — her trust."
    show rosa_marin at left:
        zoom 0.7

    rosa_marin "We have sun for another hour. Speak, child. Tell them in a way folk can carry home."
    "You run your fingers across the edge of the table. The paper-stapled packets and a tablet sit waiting; Lena’s recorder blinks a small red light. Your mouth is dry, but your voice comes from somewhere deeper than nerves — the place that learned to name loss and keep going."
    show mara_voss at right:
        zoom 0.7

    mara_voss "We promised each other honesty. Today, we show you what that honesty looks like."
    show lena_park at center:
        zoom 0.7

    lena_park "We pulled municipal memos, developer communications, and promotional materials. We traced the timeline of promises and the discrepancies between what's been told in campaign gloss and what the contracts show. We have on-record messages and sign-offs that connect the redevelopment narrative to private investment clauses — clauses that weaken community protections. We are releasing them now."
    hide rosa_marin
    hide mara_voss
    hide lena_park

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A collective intake of breath; the rustle of pages, a phone camera clicking]
    "You watch faces shift. A neighbor whose stoop you repaired last summer looks stricken; a young volunteer squeezes her hands into a fist. Tomas’s jaw tightens for a beat, then relaxes when he catches your eye — a silent calibration of strategy, concern threaded with resolve."
    show tomas_herrera at left:
        zoom 0.7

    tomas_herrera "How verified is this? Lena, is everything cleared for public release?"
    "Lena Park meets his gaze without flinching."
    show lena_park at right:
        zoom 0.7

    lena_park "Cross-checked, timestamped, multiple sources. I have backups. But we need to decide the frame: do we drop everything publicly or seed it for a controlled release? The risk is legal fire from Elys’ counsel."
    "You feel the old urge to shield — to pace the reveal, to calculate. But the greenhouse smells of peat and decision; the sun narrows in a way that makes courage feel less abstract."
    "You think of the families who lost windows to the last surge, of Rosa teaching kids to plant salt-tolerant grasses on a shoestring budget. You think of Elys’ glossy flyers promising 'revitalized waterfront' while the fine"
    "print blurs community control. This exposure is not about personal victory; it's about making a true choice visible to everyone."

    menu:
        "Release everything to live stream now":
            "Lena’s thumb hovers over the upload. Cameras flare as the feed begins; a ripple of voices grows outside the greenhouse, immediate and incandescent."
        "Start with the summary — keep the full files locked":
            "Lena nods; she flips to a prepared one-page summary. People listen, the mood controlled but curious, like a tide pulled back to show the reef."

    # --- merge ---
    "Either way, the evidence is heavy and true enough to change the shape of the room."
    "Lena waits for your cue. You choose."
    # [Outcome A: A live notification ping sounds; voices swell. On a neighbor's livestream the greenhouse fills screens across the bay. People outside begin to gather, holding signs and sharing the clip.]
    # [Outcome B: Paper turning; Lena reads the summary. The crowd leans in, murmurs rising into conversation. Phones stay in pockets for now, the moment feeling intimate and deliberate.]
    "Lena produces an audio clip next — a short, clipped exchange between a developer liaison and a municipal advisor, the kind of ordinary language that carries extraordinary implications. You feel it like a current through the floorboards."

    lena_park "—yes, we prioritise leases here; public easements are negotiable depending on parcel —"
    "The word 'negotiable' lands like a pebble dropped into still water. Someone laughs, sharp and disbelieving. Elys’s composure flickers but does not fall."
    show elys_reed at center:
        zoom 0.7

    elys_reed "Context matters. You can stitch sounds together until they make the story you want. We are talking about jobs, homes—"
    hide tomas_herrera
    show mara_voss at left:
        zoom 0.7

    mara_voss "Context is exactly what you had, Elys. Context included your proposal to reclassify certain easements. Context is the contracts, not just the speech."
    "Elys’s smile cools into a practiced calm. You notice the slight way she tugs at the cuff of her sleeve — a human gesture grafted onto a polished posture."
    hide lena_park
    hide elys_reed
    hide mara_voss

    scene bg ch10_453e40_3 at full_bg

    scene bg ch10_453e40_4 at full_bg
    "Mayor Anton clears his throat, the sound wooden but earnest."
    show mayor_anton_chi at left:
        zoom 0.7

    mayor_anton_chi "These are serious allegations. If accurate, they undermine public trust. We need to act carefully — public inquiry, due process. Hasty moves can be reversed."
    "Tomas moves closer to you, low enough that only you can hear."
    show tomas_herrera at right:
        zoom 0.7

    tomas_herrera "This will force their hand. Legal gets messy, but it also buys time if we do it right. Are you ready for a courtroom fight, Mara?"
    "You taste salt and citrus and decide, at least for the moment, to lean into hope: that transparency will combine with pressure and create safety for the shore."
    "You imagine injunctions and audits and, beyond them, kids planting marsh grass in a protected strip that survives the next surge. You imagine a town that can hold two truths: that redevelopment can bring funding, and that it must not be a cover for extraction."
    "Rosa steps between the two of you and lays a weathered hand on the table."
    show rosa_marin at center:
        zoom 0.7

    rosa_marin "We have to pick a path that holds the land, not just wins headlines. Law can protect roots. Talks can slow chainsaws. Action can keep men from laying down beds of concrete. Your choice will be the seed we plant next."
    "Her words thread the room with a kind of patience that does not dilute urgency."
    "Elys folds her hands again, a blade of calm under a glass of heat."
    hide mayor_anton_chi
    show elys_reed at left:
        zoom 0.7

    elys_reed "If you believe these allegations, then use the instruments of democracy. File your claims. Let the law speak. I will cooperate with a transparent review — if it is truly independent."
    "Her offer lands like an anchor. It could be lever or trap."
    "Anton’s mouth twitches, the politician balancing on a fulcrum."
    hide tomas_herrera
    show mayor_anton_chi at right:
        zoom 0.7

    mayor_anton_chi "We can convene third-party auditors. Or the council can request public records. Or civil society can mobilize."
    "Lena, always hungry for the public frame, leans in."
    hide rosa_marin
    show lena_park at center:
        zoom 0.7

    lena_park "We can drag this into daylight in three ways: legal exposure, a negotiated oversight pact bolstered by third-party auditors, or direct action to make visible what's already happening in the field."
    "Tomas looks at you again, this time not as planner to activist but as partner."
    hide elys_reed
    show tomas_herrera at left:
        zoom 0.7

    tomas_herrera "Each choice shapes more than strategy. It shapes who we are as a community."
    "You can feel the rise — the hopeful tilt of possibility. The greenhouse hums with it: neighborly outrage folding into deliberate planning. Phones record but hands are also ready to carry buckets and bind hands with"
    "rope if need be. People are not waiting to be saved; they’re ready to act with thoughtfulness."

    menu:
        "Push Lena to release the audio and documents to the press immediately":
            "Lena’s fingers hover, then press send. The press inbox floods. Outside, neighbors begin to chant; the evidence hits the papers before dusk."
        "Ask Mayor Anton to agree to bring in independent auditors before public release":
            "Anton nods slowly, the weight of the office visible. He agrees to call a special session, and the greenhouse breathes with cautious, organized hope."
        "Call for a peaceful direct action on the construction lot next week":
            "A murmur of fierce agreement spreads; the plan begins to sketch itself on napkins and phones — blockades, shifts, human chains around heavy equipment. The mood is electric, risky, and communal."

    # --- merge ---
    "Neighbors talk, divide, stitch plans; Rosa pours another cup of tea and sets it by your hand."
    "Neighbors talk, divide, stitch plans; Rosa pours another cup of tea and sets it by your hand. The sun strips gold across the plants, and even Elys’s shadow looks softer at the edges in that light."
    "Hope does not feel naïve here — it feels like a practical thing, like compost: rooted, smelly, fertile."
    "Dialogue extends, braided and deliberate: questions, counters, reassurances. Tomas argues for structure; Rosa for roots; Lena for daylight. Elys speaks of jobs and stability, and Mayor Anton keeps returning to process. You speak when you must"
    "and listen the rest of the time, because this is the town you know — messy, stubborn, alive."
    hide mayor_anton_chi
    show mara_voss at right:
        zoom 0.7

    mara_voss "Whatever path we pick, it has to protect the people and the living systems that make this place home. Not just the headlines. Not just the balance sheet."
    hide lena_park
    show elys_reed at center:
        zoom 0.7

    elys_reed "Then let's agree on oversight that stands up to scrutiny. If you can prove wrongdoing, we’ll correct course."
    "The offer hangs. It could be a bridge or a bargaining chip. You can feel the choices branching like roots under the table."
    "You are tired, yes, but the fatigue has a different shape now — serious and purposeful. There is a rising tide of civic power here, and you are one of the people steering it. You imagine"
    "the next steps: lawyers, auditors, placards, or human chains. Each will demand something from you and from everyone here. But each also promises a way to guard the shore."
    hide tomas_herrera
    hide mara_voss
    hide elys_reed

    scene bg ch10_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Strings swell gently — ascending, hopeful]
    "You look at the faces around you: Tomas’s steady hand, Lena’s fierce eyes, Rosa’s patient certainty, the mayor’s wary hope, even Elys’s complex composure. The choice you make now will send ripples across public squares and council chambers alike."
    "The room grows quiet, waiting like soil before rain."

    menu:
        "Option A: 'Push full legal exposure—file public records requests and pursue judicial injunctions.'":
            jump chapter12
        "Option B: 'Seek a negotiated oversight pact with Mayor Anton and third-party auditors.'":
            jump chapter13
        "Option C: 'Organize direct action—sit-ins at construction sites, blockade heavy equipment.'":
            jump chapter14
    return
