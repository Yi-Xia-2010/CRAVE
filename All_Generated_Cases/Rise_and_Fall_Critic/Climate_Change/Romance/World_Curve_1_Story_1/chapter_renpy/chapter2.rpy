label chapter2:

    # [Scene: The Beacon | Morning]

    scene bg ch2_c4ca42_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of sensors, kettle whistle, distant gulls over the bay]
    # play music "music_placeholder"  # [Music: Warm, hopeful piano undercurrent]
    "You push open the Beacon's door and the smell that meets you is all familiar things: brewed coffee, damp canvas, and the sharp metallic tang of seawater that never quite leaves this building. The whiteboards inside"
    "are already a landscape of lines and scrawled notes — tide graphs, volunteer rosters, an optimistic but messy timeline. Light from the low morning slides across the wet concrete outside and catches on a smear of"
    "salt that someone hasn't scrubbed from the rail."
    "Hal is at the longest table, leaning over a printout, fingers stained with graphite and old weld-smoke. A corner of his sweater has a patch sewn on with clumsy thrift-store hands; he looks up with that old, careful smile when you come in."
    show harold_hal_finnegan at left:
        zoom 0.7

    harold_hal_finnegan "Morning, Amara. Sensors bounced a spike at three-thirty. Nothing catastrophic, but enough to wake the retired boys up."

    harold_hal_finnegan "You brought the coffee this time?"
    "You close your coat against the draft and set your bag down. In your hands the sensor reader weighs like a promise — a small, stubborn thing that translates salt and stress into numbers you can"
    "explain to other people. You run your thumb over the faded lighthouse sticker on your notebook and feel the echo of last night's resolve — not doing this alone."
    show amara_vale at right:
        zoom 0.7

    amara_vale "I did. And I ran the overnight logs; there are a few nodes that climb in sync with the west swell. I want us to map the trend before the meeting."
    hide harold_hal_finnegan
    hide amara_vale

    scene bg ch2_c4ca42_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A soft digital chirp as a new data packet arrives]
    "Miriam arrives in a flash of teal hair and clipped energy, dropping a stack of flyers and a clipboard on the table. Her presence fills the room like someone handing out a megaphone in a quiet place."
    show miriam_santos at left:
        zoom 0.7

    miriam_santos "You're late, Hal."

    miriam_santos "And you, Amara — don't you dare make this only about graphs. If we want the crowd, we need faces and a story."
    show harold_hal_finnegan at right:
        zoom 0.7

    harold_hal_finnegan "She has a point. The council likes numbers, the people like stories. Lucky for you, you have both."
    "Your chest warms when they say it — both: the thing you've tried to carry yourself is now the thing you can share. The mood is light but focused; volunteers' names are being pinned next to tasks, the whiteboard dividing into logistics, outreach, and data."
    "You walk the board, finger tracing a path from sensor nodes to outreach — the path your plans must follow. You're thinking of raised promenades and mangrove saplings, of logistical details that will make them possible"
    "without turning the town into someone else's cookie-cutter coastal development. Hal watches you, reading the map on your face like a blueprint."

    harold_hal_finnegan "If we phase the work, we can run volunteers and hire small crews for technical jobs. Old Harbor's basements need priority. I'll get the reinforcement specs out today if Eli can run the stress projection with you."

    miriam_santos "I'll have Rosa host a table tonight. We'll get oral histories—short, sharp. People remember a porch more than a graphline."
    "You walk the board, finger tracing a path from sensor nodes to outreach — the path your plans must follow. You're thinking of raised promenades and mangrove saplings, of logistical details that will make them possible"
    "without turning the town into someone else's cookie-cutter coastal development. Hal watches you, reading the map on your face like a blueprint."

    harold_hal_finnegan "If we phase the work, we can run volunteers and hire small crews for technical jobs. Old Harbor's basements need priority. I'll get the reinforcement specs out today if Eli can run the stress projection with you."

    miriam_santos "I'll have Rosa host a table tonight. We'll get oral histories—short, sharp. People remember a porch more than a graphline."

    menu:
        "Open the meeting with data — show the tide trends first":
            "You square your shoulders. 'Numbers first, then stories,' you say, knowing the urgency will land harder if people see the curve. Miriam nods, already jotting 'Graphs' under first fifteen minutes."
        "Start with a story — bring a neighbor to speak":
            "You choose the human line. 'We start with Mrs. Gallo's porch. Let people feel what we mean,' you say, and Miriam smiles like the idea is a warm shore. Hal hesitates, then concedes that emotion will make the numbers bite deeper."

    # --- merge ---
    "Either way, the meeting will be full."
    hide miriam_santos
    hide harold_hal_finnegan

    scene bg ch2_c4ca42_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft thud of paper landing]
    "Before you can pin your choice to the board, someone taps the glass. A courier's leaflet; a glossy brochure. Marco Voss's name is visible even from across the room — the sleek type, the promise of"
    "large numbers and faster fixes. The brochure is a different weather: cool, polished, and designed to reflect trustworthiness."
    "Miriam picks it up, thumb flipping through photographs of concrete barriers and renderings of a transformed waterfront that looks unmistakably modern — and unmistakably not Seabright."
    show miriam_santos at left:
        zoom 0.7

    miriam_santos "He's already sent materials. 'Comprehensive redevelopment,' promises everything he thinks corporations are allowed to promise."

    miriam_santos "He'll want to talk funding."
    show harold_hal_finnegan at right:
        zoom 0.7

    harold_hal_finnegan "Marco's money moves quick. It can shore up a lot of things overnight. But his plans tend to eat local places and cough up profit."
    "He looks at you; there's concern there."

    harold_hal_finnegan "We don't want to trade small losses for a big wall that forgets people."
    "You hold the brochure with both hands even though it's barely needed; the paper is warm from the courier's bag. There's a familiar friction in the back of your throat — hope that money could mean"
    "more mangrove plantings, dread that 'redevelopment' will mean bulldozers and buyouts. You remember the way Marco's grin once smoothed a town hall room into submission; memory says be cautious. Your instincts — the quiet ones —"
    "say you can make him answer to the town."

    menu:
        "Invite Marco to present at the town meeting":
            "You fold the brochure carefully. 'Invite him to come. Let the town hear the plan and ask questions,' you propose. Miriam clicks her pen: it's risky, but transparency could keep him honest."
        "Acknowledge receipt and say you'll decide after the community sets priorities":
            "You tuck the brochure aside. 'We need to set our priorities first,' you tell them. 'We can't let him set the terms.' Hal nods with relief; Miriam makes a note to draft a reply that keeps the door open without giving the frame away."

    # --- merge ---
    "Both options feel like stepping stones onto a larger tide. Whichever you choose, the Beacon will be where the community turns those glossy promises into things with human names attached."
    # play music "music_placeholder"  # [Music: Slight swell — a hopeful violin line]

    "Elias 'Eli' Navarro" "Looks like the room found its teeth while I was gone."

    "Elias 'Eli' Navarro" "Hal said you wanted me to run the foundation stress curves with you."
    "You meet his eyes. There is something steady in the set of his shoulders that untangles the way your chest knots when you think of finances and livelihoods and the weight of choosing wrong. You tell"
    "him what you need — the priority homes, the sequence for reinforcements, a practical window for volunteer work — the things that will keep people in their places without burying them in debt."
    show amara_vale at center:
        zoom 0.7

    amara_vale "I want projections that show risk over five-to-ten years, not just the next fundraising quarter. If we phase the work, we can protect more houses sooner. But I need someone to confirm the curves with me. Will you do it?"

    "Elias 'Eli' Navarro" "I will. And I'll be honest — some of the quick fixes do buy time, but not always the dignity we want for families. If we can phase it to keep businesses afloat while protecting homes, that's where I sit. I'll run the curves tonight and show you where incremental reinforcement is actually stronger than a single wall."

    harold_hal_finnegan "Good. Between Eli and my specs, we can give the town a plan that's shovels-ready and not a PR stunt."

    miriam_santos "And I'll keep people in the loop. We start outreach tonight. Rosa's table, Hal brings the old plans, Eli brings the numbers, Amara opens with whatever you chose earlier."
    "You feel the room contract into a small, functioning machine — people placed where their skills turn into something that can lift a town. A warmth unfurls from your chest: relief, yes, but also the bright,"
    "clear edge of possibility. The Beacon smells like coffee and wet paper and a confidence you haven't let yourself taste in a long time."

    "Elias 'Eli' Navarro" "Also — remind me to visit Mrs. Gallo. She showed me the porch last time I was here. I'll make sure the stress curves account for those old posts, too."
    "You laugh, the sound light. For a moment your old worry — that you'd have to shoulder the entire thing, the guilt and the logistics and the sleepless nights — seems silly. It sits, a smaller thing, parceled now among people who will carry it with you."
    hide miriam_santos
    hide harold_hal_finnegan
    hide amara_vale

    scene bg ch2_c4ca42_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Marker cap clicks; the hum of the sensors steadies like a held breath]
    # play music "music_placeholder"  # [Music: Piano rises into a warm chord]
    "You look at the board: the town meeting's heading, time, place. Your hand hovers over the marker as if it were the first stake in the ground."
    "You think about the porch in '29, the ledger of sensor spikes, Marco's glossy promises, Hal's hands, Miriam's megaphone, Eli's steady eyes. This is the point where all those things get named and set on a table together."
    "You want the meeting to be honest and fierce; to keep Seabright recognizable and safe. You want to ask for help without making concessions that unmoor people's lives. The board is a clean horizon. You feel your resolve sharpen into something bright and useful."
    "You press the marker to the board and begin to write the meeting notice."
    # [Page-Turn Moment]
    "You pause mid-stroke. The marker's ink pools for a second like a dark harbor in miniature. Outside, the rain has thinned to a drizzle that polishes the town, and for a beat the world feels arranged:"
    "a problem, a people, and a plan forming under your hand. The Beacon's whiteboards have always been where possibility begins; today they feel like the town's spine being rewired into something stronger."

    scene bg ch2_c4ca42_5 at full_bg
    # play music "music_placeholder"  # [Music: Sustained hopeful chord, then a soft fade]

    scene bg ch2_c4ca42_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
