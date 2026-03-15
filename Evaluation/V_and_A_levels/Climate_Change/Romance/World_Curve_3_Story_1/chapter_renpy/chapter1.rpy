label chapter1:

    # [Scene: Harbor Market | Morning]

    scene bg ch1_Start_1 at full_bg
    # play music "music_placeholder"  # [Music: Soft, ambient morning BGM — distant gulls and low mariner song]
    # play sound "sfx_placeholder"  # [Sound: Wooden walkways creak, muffled conversation, kettle hissing]

    "You step onto the raised quay as the market wakes. The air is a salt-and-sweet braid: brine from the harbor, the sharp sugar of brown paper bags, a damp earthiness from last night's moss repairs. The sun hangs low and orange; it cuts across the water in a slow, patient strip. Everything feels slightly reclaimed — ropes mended with leftover twine, a sign hand-painted on salvaged plywood" "MARKET — PAY WHAT YOU CAN PERIODICALLY."
    "Your jacket smells faintly of the greenhouse: wet canvas, rosemary tucked into a pocket. Your brass compass swings against your sternum and catches the light with each step. People nod as you pass — not the"
    "rehearsed politeness of an office morning, but the small, necessary courtesies of a place that has learned to keep each other."
    "Kai is already behind his stall, arranging fish and jars of pickled samphire with the theatrical care of someone curing more than product: he's keeping ritual. He looks up and grins when he sees you, and the harbour's soundscape seems to loosen at the edges."
    show kai_moreno at left:
        zoom 0.7

    kai_moreno "Look at you, barefoot in spirit even with those boots on. Coffee? I've got a thermos that survived three seasons."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Always. That thermos is practically municipal infrastructure at this point."

    kai_moreno "Rosa sent over second-wave marsh plugs last night. Says the soil's 'sleep-ready.' She wants ten hands at the Flats tomorrow—no excuses."
    "You let the cup rest between your gloves and your thumb traces the tide-ring scar on the rim. Rosa's messages tend to be both instruction and benediction; you keep them near to you the way you"
    "keep the compass. The Flats — the saltmarsh restoration site — is the work you keep returning to in your head all day, every day. Planting cordgrass, stitching channels back into the mud, teaching volunteers to"
    "read the tide like a page in a book."

    kai_moreno "Ibrahim 'Ibe' Rafiq's bringing his new modular frames to the rooftop greenhouse next week. He said you might want to help test anchor points."
    "The name finds a soft place inside you. Your chest eases and tightens at once — the particular, quiet anxiety that arrives with every shared plan."
    hide kai_moreno
    hide mara_lin

    scene bg ch1_Start_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft clink of metal, distant motor of a supply boat]
    "Ibrahim 'Ibe' Rafiq looks up as you approach. He wipes his hands on a rag and gives you that half-smile that tries to be casual. His presence is a warm instrument in the morning — steady, tuned."

    "Ibrahim 'Ibe' Rafiq" "Morning, Mara. Seems like the market is compensating for last night's sky.' 'You look like you haven't slept, but in the best possible 'resilience' way."
    show mara_lin at left:
        zoom 0.7

    mara_lin "Late plans and earlier tide checks. The Flats takes more bribing than volunteers admit."

    "Ibrahim 'Ibe' Rafiq" "Bribery's an honest tactic. Keeps folks motivated. Besides, I like watching you defend it."
    "He says it gently, and there is a quiet exchange in the cadence. You know the meaning behind the good humor: that he'd rather build something that keeps people in their homes than move them out."
    "You lean against the railing and watch a child skip across a raised plank, her sneakers skimming puddles."

    menu:
        "Take the pastry and make a plan right away":
            "You bite into the pastry and feel the warm sugar settle in your chest like a small, necessary promise. You start listing volunteers and tools, the way a map unfurls in your hands."
        "Decline politely; focus on the tide charts first":
            "You fold the pastry back to Kai with a smile and pull your notebook instead, flipping to the tide notes. The world sharpens into measurements and schedules, the comforting language of work."

    # --- merge ---
    "You laugh, letting the pastry promise sit between you. The morning proceeds in modest ritual: exchange of tools, the barter of gossip and weather, a string of small favors that keep the market — and the town — taut and breathing."
    hide mara_lin

    scene bg ch1_Start_3 at full_bg
    "You thumb through your notebook. There are hand-drawn maps: mudflats marked with little Xs where Rosa wants new plugs, a tiny sun indicating 'best planting,' notes in the margins about volunteers with names and strengths. This"
    "is your ledger and your prayer — how to steward a place that keeps asking to be held."
    "Samira threads through the stalls with her municipal vest catching the low light. When she sees you, she hesitates just a hair longer than necessary. Government people move in straight lines; their pauses are deliberate."
    show samira_chen at left:
        zoom 0.7

    samira_chen "Mara. Eloise Varela is announcing the Asterport Shield this afternoon at the Planning Hall. Public address at three. She wanted to make sure community groups received notice—there's a briefing packet in the clerk's office if you need it."
    "The words are even and efficient. The breath after them hangs like distant fog."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Three. We'll be there. Do you… is there—anything in it now that we should be expecting?"

    samira_chen "Only what the press release says now: 'comprehensive barrier and reconfiguration plan.' I don't have special access, Mara. I wish I did. If anything changes, I'll find you."
    "Her gratitude is thinly veiled hope. You nod because nodding is a way of keeping the world moving on its axis."
    "Ibrahim 'Ibe' Rafiq's eyes find yours. For a moment he is looking at the municipal vest, then at the far-off Planning Hall line of glass and code, then back at you. The tide between what you"
    "build in the Flats and what Eloise Varela will propose presses and recedes in a rhythm you've both felt."

    "Ibrahim 'Ibe' Rafiq" "Shield,' he repeats, tasting the word. 'Sounds heavy. Like someone trying to hold the whole ocean back with one hand."

    mara_lin "Or it could mean they finally do something long overdue. The question is who pays, who moves, and how fast."
    "Ibrahim 'Ibe' Rafiq shifts his weight; his fingers find the small talisman at his neck and rub it once. You understand the gesture — a sort of private throttle he keeps on his reactions. It makes him human-sized again."

    "Ibrahim 'Ibe' Rafiq" "We can push for community oversight. Modular designs. Phased builds so nobody gets boxed out."

    mara_lin "Phased builds need people at the table from day one. I want conditional approvals, community liaisons with veto power — not just placation through a facade of consultation."
    "The market continues its slow choreography around you: a child trading a drawing for a jar of clams, an old woman bartering knitting for a bag of compost, the rhythm of daily life carrying on like"
    "a promise that weather will change but mornings will come. The announcement at three sits like a low cloud on the horizon — not yet a storm, merely the shape of one."
    "Rosa approaches with her habitual calm. Her apron smells of sea mud and lavender. She lays a hand on your forearm like a benediction and nods to the two of you."
    show rosa_alvarez at center:
        zoom 0.7

    rosa_alvarez "We plant with tide and song, Mara. The Flats remembers who plants and who flees. Don't speak for the Flats without the Flats in the room."

    mara_lin "We won't."

    rosa_alvarez "There are new marsh plugs. There is clay to be lifted. There is also tea in my shed.' (Her smile is wry.) 'Small comforts anchor people as surely as sandbags."

    menu:
        "Agree to meet Rosa at the shed after the market":
            "You tell Rosa you'll be there; the promise settles into your limbs like a plan that has been spoken aloud. It feels good: belonging worn like a coat."
        "Say you'll check in after the Planning Hall announcement":
            "You ask Rosa for a brief window to attend the announcement. Your voice is steady, but there's a pull under your ribs — a calculation between duty and watching the city decide for itself."

    # --- merge ---
    "Kai fusses with another string of bulbs as if the market's light must be intentionally kept up against the day. He leans over as you make your small decisions and says, sotto voce, 'If the city's"
    "voice gets loud, we should make ours louder. Even if louder in our case is more people planting and less noise on the feed.'"
    "You consider the shape of 'louder'. For you, louder isn't always banners and megaphones; sometimes it's ten volunteers knee-deep in mud, hands memorizing the same motions until they become muscle memory against a future tide. Sometimes louder is a stitched-together plan with people's names on it."
    "The morning slows into a gentle forward motion. Volunteers trickle in and set tools down, nodding to you as if you are midwife and coordinator both. Conversations curl and unspool like fishing line."
    "Ibrahim 'Ibe' Rafiq watches the harbor, then the Planning Hall across the water. There is no tremor in his face; only the focused, careful look of someone rehearsing the next move in a game where every piece is a life."

    "Ibrahim 'Ibe' Rafiq" "Whatever happens this afternoon, we begin the Flats tomorrow. Agreement or not. People get tired of waiting while plans get made for them."

    mara_lin "Tomorrow then."
    "You feel the tide under the quay in the way the wood gives with each footfall. The sun edges up, making the water a strip of laborious gold. The market hums with its usual, improbable optimism;"
    "conversations about seed density share space with gossip about the mayor's new tie. The announcement at three is on the horizon, a low note that hasn't resolved yet."
    "You pick at the compass pendant until the brass is warm under your thumb. It feels like an instrument for navigation and for holding onto direction when the city speaks in new, unfamiliar languages. You think"
    "of the Flats' mud, of Rosa's hands, of the list of volunteers folded into your notebook. You think of Ibrahim 'Ibe' Rafiq, and the way his smile carries both plan and refuge."
    "There is a small tightening in your chest — not panic, merely focus. The market continues to breathe around you, patient and ordinary in its resilience."
    "You fold the notebook closed and slide it into your jacket. You give Ibrahim 'Ibe' Rafiq a look that is both promise and question."

    "Ibrahim 'Ibe' Rafiq" "Ready when you are. We can make anchors that won't uproot people."

    mara_lin "Then let's make them."
    "You watch the Planning Hall across the water, where glass will show the announcement and screens will cast new hues over faces. The afternoon waits. The Flats waits. The city waits to see what the word 'shield' will mean in practice."
    "Everything is quiet, deliberate, and full of small commitments."
    hide samira_chen
    hide mara_lin
    hide rosa_alvarez

    scene bg ch1_Start_4 at full_bg
    "You feel the moment stretch — an ordinary, loaded pause. There are things to be done and an announcement to be heard. Your day divides simply into two acts: tending the Flats and listening to the city decide."
    "You let the pause hang like a page waiting to be turned."

    scene bg ch1_Start_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter2
    return
