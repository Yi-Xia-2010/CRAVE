label chapter7:

    # [Scene: Mariner's Row | Dawn]

    scene bg ch6_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant jackhammers, the low thrum of generators; gulls argue over open water]
    # play music "music_placeholder"  # [Music: Percussive strings build, a rapid, anxious motif]
    "You wake to the sound of construction like a second tide. It moves with the same inevitability—a roar building at the edges of your hearing until it occupies everything."
    "You remember Dr. Arun's hand on your shoulder like a benediction or a warning. 'Be careful about what you promise people tonight.' His voice is a fossil in your memory; you replay it and the feeling"
    "it left—the weight of responsibility, the taste of iron on the tongue—until you can see the shape of the day before it arrives."
    "The street smells of diesel and wet wood. Sandbags are gone. In their place, a gleam of new concrete, a half-built promenade with temporary fencing and Vale flags snapping in the wind. Cameras perch on cranes"
    "like indifferent birds. Men in consortium jackets ferry tablets and clipboards down the row; they move precisely, as if precise motion erases history."
    "You move through the crowd. Faces tilt toward you—some with resignation, some with accusation, some with a hunger for explanation you cannot feed. Lina meets your eyes first; her braid is matted with salt, her palms"
    "stained with paint. Her storefront—where her mother sold pickled fish and small curios—has a Vale placard on the door and a contractor's notice tacked over the window."
    show lina_cortez at left:
        zoom 0.7

    lina_cortez "They offered us a relocation package."
    "Her laugh is too quick, brittle. 'They said we'd be safer. Same shop, new block. Who wants a 'same shop' when the shore is your wall?'"
    "You step closer, the railing biting your palm through the fabric of your gloves. Words thrash in your throat. They want a single name to blame; you are painfully aware of the ledger of decisions and the way every line favors some lives over others."
    hide lina_cortez

    scene bg ch6_601bcb_2 at full_bg
    # play music "music_placeholder"  # [Music: The strings shift to a harsher minor interval]

    "Tamiko stands on a crate across the alley, live feed dangling from her phone like a flayed flag. Her face is drained but set. She shows you the feed: Tamiko's exposés—once incendiary—now run as background footage for human-interest pieces. The headlines have already been folded into the consortium's PR" "Rapid Response Saves Thousands."
    show tamiko_sato at left:
        zoom 0.7

    tamiko_sato "They spin it faster than we can breathe."
    "You feel the air tighten. It is hotter now—pressure building—and you realize the intensity that has been coiling since the hearing is not easing; it's swelling into something nearer to violence."

    menu:
        "Call out to the foreman":
            "You shout across the temporary fence, your voice raw. The foreman looks up, blinks, and then gestures with that disarming corporate smile—'Today is about safety.' You get a badge scanned and a polite escort off site."
        "Record Tamiko's feed and stay silent":
            "You lift your phone and point it at Tamiko's feed, hands steady. The recording is clinical; it preserves faces and numbers more faithfully than your memory. Lina catches your eye and nods once, as if the act of keeping evidence is a small, private defiance."

    menu:
        "Hand Tamiko your notebook — let her film your notes":
            "You press the water-stained notebook into Tamiko's hands. She holds it as if it's a living thing, then turns the camera to you. For a breath, your voice is steady, and you speak of place and people and the cost of quick fixes. The clip is raw; it lands with a small, horrible weight."
        "Fold the notebook into your jacket and watch silently":
            "You fold the notebook away, fingers scuffing the brittle edge. Silence becomes a shield. Tamiko's eyes search you for a signal; you give her none. The camera keeps rolling. Your silence is loud."
    "THE END"
    # [GAME END]
    return
