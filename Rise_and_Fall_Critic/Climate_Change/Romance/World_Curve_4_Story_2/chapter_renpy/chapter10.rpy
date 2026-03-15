label chapter10:

    # [Scene: Glass Marsh | Morning]

    scene bg ch10_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft squelch of boots in mud, distant gulls, a steady, reassuring hum of a small outboard in the distance]
    # play music "music_placeholder"  # [Music: Quiet, rising piano motif — tentative hope]

    "You chose this. You remember the weight of the lectern under your hands and the thin, steady line you drew in the council chamber" "Double down on the scientific restoration plan with Dr. Leyna."
    "The marsh breathes around you — each breath a low exhale of brine, silt, and the mineral tang of old storms. Your boots sink an inch and come away with a silver mirror of marsh water."
    "You press the notebook into your palm as if it were a compass for more than direction; the page inside is smudged with damp, a map of plots and dates, and one single word underlined twice:"
    "patience."
    "Dr. Leyna Ortiz crouches beside you, sleeves rolled, tablet balanced on her knee. She speaks in the clipped, excited rhythm of someone who lives in data the way other people live on weather: a string of"
    "percentages, chlorophyll readings, projected growth curves. But when she looks at the mats being lowered and the first strands of seagrass stir, her voice loosens."
    show dr_leyna_ortiz at left:
        zoom 0.7

    dr_leyna_ortiz "If we get stable anchoring and the silt stays below that threshold, these mats can increase below‑surface shoot density by twenty to thirty percent in a season. That’s not just numbers — that’s habitat for larvae, reduced turbidity, a feedback loop."
    show alys_maren at right:
        zoom 0.7

    alys_maren "And the breakwaters? The living ones we seeded last month — are they holding the current the way we hoped?"

    dr_leyna_ortiz "Better. Wave energy dissipation is up fifteen percent in the pilot strip. It’s small, but for this coastline, small is a beginning."
    "Ronan wades through the shallows, hauling a weighted anchor line. He laughs when a brave little fish darts between his feet. His joy is brash and immediate — the kind that makes you feel the work is already worth it."
    show ronan_pike at center:
        zoom 0.7

    ronan_pike "I found a baby crab in one of the weave pockets. Leyna, you saw that, right? That's — that's a whole crustacean census in one find."

    dr_leyna_ortiz "Data point: one crab. Heart rate of scientists: elevated."
    "You smile without meaning to. There is science here and there is life; the two are colliding in a good way."
    "Oba Kofi stands a little apart, cane planted, eyes on the horizon where the marsh meets the sea. He smells of old tar and rope and something sweet — perhaps the scent of smoked fish or the tang of the sea-heated sun on wood."
    hide dr_leyna_ortiz
    show oba_kofi at left:
        zoom 0.7

    oba_kofi "When I was a boy these flats were full of eelgrass taller than a man's knee. The fish would hide, the crabs would dance. You and Leyna — you bring that memory back into living things."

    alys_maren "We bring it back with care. We don't fake it. We let the place do the rest."

    oba_kofi "That is how you win with the sea. Not by outrunning it, but by joining it."
    "Ivo Calder is there too, sleeves rolled over his workshirt, hands already ringed with the shine of salt. He hands you a coil of anchor rope without speaking, but when your fingers touch the rope the"
    "brief exchange contains a thousand things: solidarity, the shared rhythm of labor, and something unreadable that tightens your chest with a warmth you’re careful not to label."
    hide alys_maren
    show ivo_calder at right:
        zoom 0.7

    ivo_calder "Keep an eye on the north line. The tide's got a little push today."
    hide ronan_pike
    show alys_maren at center:
        zoom 0.7

    alys_maren "I'll mark it. Ronan — hold the starboard anchor steady."
    hide oba_kofi
    show ronan_pike at left:
        zoom 0.7

    ronan_pike "On it. Hey, Alys — you think we'll see nursery beds expand to the old channel this season?"

    alys_maren "If the anchors hold and the juveniles find shelter, yes. It's not guaranteed, but the probability is better than it was."
    "The conversation loops — technical then human, the sort of back-and-forth that settles into the rhythm of people who must balance hope and realism. You tighten a knot, feel the rough rope bite into your palms, and you are satisfied by the small pain of useful work."

    menu:
        "Run your thumb along the notebook's margin notes":
            "Your thumb smudges a note, but the act steadies you — the lines blur into a map you can follow."
        "Stand still and watch the mats settle":
            "You let the marsh do the telling for a moment; a snipe lifts and crashes through the reeds, and you breathe in time with it."

    menu:
        "Mention the council notes about scaling the project":
            "You pull the notebook out and show him the sketched timeline; Ivo traces the dates with the tip of his finger and says, 'We can make those dates real, together.'"
        "Stay silent and just watch the seedlings with him":
            "You let the silence say what words might clutter; he meets your gaze and the quiet feels like a mutual agreement."

    menu:
        "Draft a short public summary for the mayor — simple language, pictures":
            "You open your notebook and start a three-line lead: 'Seed. Shelter. Return.' The words land like pebbles of truth; you can already hear them read aloud in the hall."
        "Call Ronan and ask him to edit the volunteer video first":
            "You pull up Ronan's contact and text him. His reply arrives with three exclamation marks and a promise: 'On it — will make it sing.'"

    jump chapter11
    return
