label chapter8:

    # [Scene: Your apartment above the docks | Pre-dawn]
    # play music "music_placeholder"  # [Music: Taut strings, fast tempo]

    scene bg ch8_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low tide against pilings, a distant engine idling]

    "You wake because your phone is an insistence. The notification thread—Municipal Operations—blinks like an ultimatum. The subject line reads" "Final blueprints attached. Enactment begins Monday."
    "The renderings are beautiful in the way industry renders hope: clean cross-sections, crisp angles, annotated reduction percentages—'expected surge reduction: 78%.' The modeled waterlines retreat from homes in perfect gradients. Your wristband buzzes against your pulse: a tide alert, moderate but arriving sooner than the models' calm would admit."
    "You feel the memory of the last storm like a bruise moving under your ribs. You trace a margin note in your head—what Saira said the other night about marsh migration—and another note slides in, sisterly"
    "and immediate: Tessa's text from two hours ago, 'They're starting crews on the site. You seeing this? —T.'"
    "You close your eyes and the harbor sounds sharpen: the clack of a tarp being secured, the distant clink of tools, a gull breaking into raucous laughter. Beneath it all there's a human drum—camera shutters and"
    "the hush of reporters' whispers—the town's whole life being rearranged into a sequence of images that will be posted and argued over before lunch."
    "You lift your notebook from the bedside table. It is heavy in that way a thing goes when it's full of reasons. Your coral pendant rubs against your sternum. Hope tastes like coffee and the metallic"
    "tang of adrenaline; it's bitter and vital. You can feel the day reaching for you."
    # [Scene: Seawall project site | Morning — Press day]

    scene bg ch8_6b08b4_2 at full_bg
    # play music "music_placeholder"  # [Music: Percussive rhythm increasing]
    # play sound "sfx_placeholder"  # [Sound: Distant generator, microphone feedback, shouted questions]
    show cassian_cass_romano at left:
        zoom 0.7

    cassian_cass_romano "This design reduces the modelled surge across the western quay by seventy-eight percent over a fifty-year period.' (He gestures, tablet screen looping animation.) 'It's scalable. It's adaptive. We can phase construction to minimize disruption."

    cassian_cass_romano "We drafted community liaison positions, Mira. Maintenance endowments. I know that won't erase every fear, but—' (he pauses, searching) '—it creates a scaffold."
    "The models feel cooler to the touch than the damp air as you take the tablet. He watches you read like someone watching a tide line and learning patience."
    "His competence is a warm hand on a rough day. It is not everything, but it is something you can lean into when the water comes fast."
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "They'll sell us safety like they sell us sandwiches—quick, wrapped, and made somewhere else!"
    "A ripple of cheers answers him. He stands at the bow of a cluster of small boats tied together—old nets doubled as banners, faces the press can translate into story: community, loss, resistance. Jonah Reyes's grin—half-anger,"
    "half-plea—finds you across the water. He tosses his cap to the air like he's throwing a gauntlet."

    jonah_reyes "Mira. You helped draft that seal for oversight. Don't let them damn it with signatures and press conferences."
    "Cassian 'Cass' Romano turns toward Jonah Reyes, jaw tight."

    cassian_cass_romano "Jonah, we've built safeguards into the contract. There's room for community seats. You know that."

    jonah_reyes "Room in a contract isn't the same as a seat at the table when the table's measured from above."
    "You step between their lines without thinking, the old boardwalk wood warm beneath your boots."
    show mira_kestrel at center:
        zoom 0.7

    mira_kestrel "Both of you—stop making this a courtroom. This is the town. We need answers, not soundbites."

    cassian_cass_romano "Tell me what you need. Real terms—I'll put them in the clause set."

    jonah_reyes "We need guaranteed labor prioritization for local crews. We need the marsh left room to migrate. We need—"
    "Jonah's list is not finished. You know it by heart; it is the library of the town's scars and small triumphs. His words vibrate with memory and handcallused urgency."

    menu:
        "Ask Cass to show the maintenance endowment numbers now":
            "Cass narrows his eyes and thumbs a folder toward you; his calm becomes a new kind of pressure—transparent, immediate. || The cameras pounce, but for a breath the two of them are unguarded."
        "Step into the flotilla and talk to Jonah's crew":
            "The scent of wet rope and smoked fish hits you; Jonah's crew hushes and offers you hot coffee from a thermos, their trust immediate and tactile."

    # --- merge ---
    "Cass meets your choices with the kind of patience that can carry plans forward or push them over the edge. The cameras pounce, but for a breath the two of them are unguarded."
    "Tessa slips up beside you, cheeks windburned, hair frizzed from the sea spray."
    hide cassian_cass_romano
    show tessa_kestrel at left:
        zoom 0.7

    tessa_kestrel "You look like you'll split in two if you don't make a decision soon.' (She nudges your arm.) 'Don't worry—whatever you pick, we've got your back. Promise."
    "Her faith is a small geodesic truth: even if you make the wrong call, the town will not abandon you. That steadies the part of you that fears choosing in the dark."
    hide jonah_reyes
    show cassian_cass_romano at right:
        zoom 0.7

    cassian_cass_romano "There's a clause—renewal review every five years, community veto power on maintenance plans. I can have legal draft it in plain language. No corporate double-speak."
    hide mira_kestrel
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "Veto power that can be bought out is still a sold-out veto. We need timelines for job allocation, clear environmental buffers. We need community stewards."
    "Their eyes find yours like two compasses aligning for a storm. Both men lean on different truths; both want you to tip toward them."
    # [Scene: Municipal Hall — Conference Room | Afternoon — Public Forum]
    hide tessa_kestrel
    hide cassian_cass_romano
    hide jonah_reyes

    scene bg ch8_6b08b4_3 at full_bg
    # play music "music_placeholder"  # [Music: High strings overlaying quick percussion—heartbeat tempo]
    # play sound "sfx_placeholder"  # [Sound: Mics clicking, murmured impatience]
    show mayor_lynette_cole at left:
        zoom 0.7

    mayor_lynette_cole "Time is a currency we can't afford to waste. If we do not sign, the funding window closes and the firm reallocates to another municipality.' (She taps a tablet.) 'We have federal matching funds that expire in sixty days. There are risks in delay."
    show dr_saira_ngoma at right:
        zoom 0.7

    dr_saira_ngoma "And there are ecological costs that accrue over decades, not line items for next quarter. Hard structures displace marsh, change sediment flow, and gridlock fish migration corridors. That has socio-economic impacts—on fisheries, on the marsh harvests—long after the ribbon is cut."

    "A reporter" "Doctor, can you quantify that?"

    dr_saira_ngoma "Hard to fully quantify because the models have nonlinear responses. But we can mitigate—if we insist on design alteration and long-term funding guarantees for adaptation, not perpetual dependency."
    "The clock on the screen in the corner of the room ticks audibly in your head. Mayor Lynette's posture says 'deliverable.' Cassian 'Cass' Romano's presence says 'doable.' Jonah Reyes's flotilla outside says 'resist.' Dr. Saira's measured worry says 'careful.'"

    mayor_lynette_cole "Mira, as the community scientist and liaison—your authorization will move us from planning into construction. The cameras will follow. The town needs a face to the decision."
    "Her gaze lands on you like a weather event that demands response. There is an expectation baked into it: that you can translate messy humanity into policy. You feel every informal conversation, every late-night suggestion, every compromise laid like pebbles in your palm."
    "You are a ledger of small obligations—a long list of people whose lives will be altered by this wall. You imagine Tessa's hands learning a new trade, Old Man Rafi telling a different story about the"
    "harbor, Jonah's crew coming back to work with something that looks like dignity. You imagine also shapes of marshes that will have to find new homes. There's guilt, yes, but also a hungry, sharp hope that"
    "some combination of care and engineering can save more than each alone."
    show cassian_cass_romano at center:
        zoom 0.7

    cassian_cass_romano "Let me put it plainly. I can slow the project for community oversight clauses without losing major funding. Or we proceed, and it's fast. What do you need to authorize this?"
    hide mayor_lynette_cole
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "Don't let 'slowing' be a polite way of telling us 'do it and we'll fix it later.' Mira, you know the kind of fixes 'later' becomes."

    cassian_cass_romano "We all know what 'later' can mean. That's why I proposed escrowed maintenance funds and a public oversight board with real teeth."

    jonah_reyes "Teeth that get pulled by lawyers when cash dries up."
    "Tension climbs like a tide. The room is a pressure vessel filled with bright intentions and brittle promises."

    menu:
        "Request an immediate public maintenance escrow demonstration":
            "Saira nods and pulls up a provisional escrow plan on the holo; Lynette's jaw tightens when the numbers are real and messy."
        "Ask Jonah to outline specific local labor guarantees in front of the council":
            "Jonah's voice steadies; he names contractors and crews by name, and the council looks suddenly—uncomfortably—human."

    # --- merge ---
    "The council shifts, optics and human faces colliding as technical detail and named people alter the room's equilibrium."
    hide dr_saira_ngoma
    show mayor_lynette_cole at right:
        zoom 0.7

    mayor_lynette_cole "We have media waiting outside for a clear decision. The optics matter. Mira—if you don't sign today, headlines will read 'Town Divided.' If you do, they'll read 'Town Protected.'"
    "You laugh—a short exhale that sounds like a small concession to farce."
    hide cassian_cass_romano
    show mira_kestrel at center:
        zoom 0.7

    mira_kestrel "Optics won't save people the way good design and good stewardship will. I won't let this be performance."

    mayor_lynette_cole "Performance keeps the grants flowing. Real change requires real capital."
    hide jonah_reyes
    show dr_saira_ngoma at left:
        zoom 0.7

    dr_saira_ngoma "If you sign without strict ecological safeguards we risk creating a dependency that costs more people their livelihoods in twenty years than the wall saves in ten."
    "The room pulses. The pressure is not a threat—it is an engine. VeryHigh arousal is not panic but a focused inferno; every glance becomes a lever. You sense momentum forming the shape of the town's near"
    "future. Your survivor's guilt—normally a cold stone at the base of your throat—burns something sharper now. It argues, not from fear of collapse, but from a fierce desire to ensure that, if loss must be carried,"
    "it is borne with dignity and purpose, not as collateral."
    hide mayor_lynette_cole
    show tessa_kestrel at right:
        zoom 0.7

    tessa_kestrel "Mira, whatever you choose, remember why you came back. Don't let the urgency strip the town of its hands."
    hide mira_kestrel
    show cassian_cass_romano at center:
        zoom 0.7

    cassian_cass_romano "We can build something that lasts. Let me prove it."
    hide dr_saira_ngoma
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "We don't want you to prove anything to the firm, Mira. We want you to protect us."
    "Their proximity is a map of different intimacy: Cassian 'Cass' Romano's confident touch maps to policy and shared purpose; Jonah Reyes's rough hands map to memory and the tactile knowledge of loss. Both offer you roots; both ask you to bend in a way that will change the town's shape."
    hide tessa_kestrel
    hide cassian_cass_romano
    hide jonah_reyes

    scene bg ch8_6b08b4_4 at full_bg
    # play music "music_placeholder"  # [Music: Crescendo—full orchestra—then a single, bright sustained chord]
    # play sound "sfx_placeholder"  # [Sound: The whole town seems to be holding its breath, the ocean a low undercurrent]
    "You set your notebook on the table and open to a fresh page. The pen feels like a surge couched in a small object. You draw three columns in careful handwriting. You label them not with"
    "cold categories, but with consequences: who keeps work, who keeps marsh, who keeps memory. The ink is dry in seconds; your hand moves faster than your pulse can catch up."
    "This is a pivot you have been rehearsing in private for months. This is the moment where theory and memory collide in the public square. You are terrified, yes—but also alive with the knowledge that action"
    "will change things for the better if you choose wisely. The pressure is immense; the stakes look like lives. You are not paralyzed. You are pressed into clarity."
    show mayor_lynette_cole at left:
        zoom 0.7

    mayor_lynette_cole "Make it clear. The town needs a face on this."
    show dr_saira_ngoma at right:
        zoom 0.7

    dr_saira_ngoma "Whatever you do, embed ecological triggers in the contract—automatic reviews, funding release tied to habitat metrics."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "And guarantee that local crews get the jobs. Don't let 'efficiency' mean 'outsourced.'"
    hide mayor_lynette_cole
    show cassian_cass_romano at left:
        zoom 0.7

    cassian_cass_romano "I will write that into the contract. I'll have my team draft it this afternoon. But I need an authorization signal to mobilize crews next week."
    "You feel the swell peak. The choice is no longer abstract. It is an intake of breath before a plunge."
    # play music "music_placeholder"  # [Music: A single high note held—then silence that feels like the eye of a storm]
    hide dr_saira_ngoma
    hide jonah_reyes
    hide cassian_cass_romano

    scene bg ch8_6b08b4_5 at full_bg
    "You put the pen down. The room leans forward as if your ink could pull them all across some line."
    "You think of the town in frames—children who will learn to read tides as story, Old Man Rafi telling the next generation about a season when the ocean and people decided how to live together, Tessa"
    "learning to weld alongside the crews. You picture the marsh fighting for room, and the compromises that might let both human and habitat breathe. The pressure at your chest is not a threat; it's a call."
    "The world narrows to this clean, terrible, exquisite point where choice becomes action."

    menu:
        "Authorize full engineering deployment now for maximum protection.":
            jump chapter9
        "Negotiate a hybrid contract with strict community oversight clauses.":
            jump chapter17
        "Withdraw support; reveal environmental trade-offs publicly.":
            jump chapter13
    return
