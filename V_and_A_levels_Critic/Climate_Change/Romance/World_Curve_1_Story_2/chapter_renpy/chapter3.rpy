label chapter3:

    # [Scene: Boardwalk | Late Afternoon]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, steady percussive rhythm—mid-tempo]
    # play sound "sfx_placeholder"  # [Sound: Distant megaphone cadence; gulls circling; the slosh of water against pilings; the shuffle of boots and the rustle of laminated flyers]
    "You walk back onto the boardwalk with the taste of rain and adrenaline in your mouth, the mechanical rhythm of the last chamber still in your limbs. The town has a way of arranging urgency into"
    "visible lanes: polished speech at the lectern, paint-stained voices on the rails, and a neat fence with a developer's logo staring like an affront. Salt flakes at the edge of your boots. Your Moleskine is folded"
    "in your hand, corners damp; the seagull pin over your heart is a small, private weight."
    "From the council chamber to this stretch of sea-scarred wood, the same split keeps opening: the planner inside you catalogues load paths and collapse modes; the neighbor inside you counts the faces in the crowd and"
    "remembers the houses that once stood where now only pilings rise. You feel both equally, and neither feels tidy."

    scene bg ch3_98c6f2_2 at full_bg
    show dr_noor_patel at left:
        zoom 0.7

    dr_noor_patel "Ari—thank you for coming out. I need to pull you aside."
    "They tilt their head toward a quieter corner where a tide-monitor kiosk juts from the railing. The volunteers keep shouting statistics and chant refrains; the megaphone's rhythm keeps time. Dr. Noor's voice is lower here, meant for ears not the cameras."

    dr_noor_patel "When you spoke at the meeting, you steered us into a place we can stand on. There's something else—an erratum in the modeling you should see."
    "You steady yourself against the kiosk, breath fogging. Models, charts, numbers; they are the scaffolding you trust more than speeches. You want to both brace and lean forward."
    show ari_navarro at right:
        zoom 0.7

    ari_navarro "An erratum?"

    dr_noor_patel "A correction. We reran the levee stress models with coupled sediment transport. In isolation, some levee geometries look stable. Coupled to the current shoreline dynamics, they can increase lateral erosion—especially along the Old Harbor District. That means a hard levee without living shorelines could speed the loss of cultural edges, not just protect them."
    "They pause, choosing language with the care of someone who knows how a single sentence can rearrange votes and hopes."

    dr_noor_patel "It's not absolute. It's conditional on placement, on maintenance, on complementary restorations. But it's material. It changes the political frame."
    "Your fingers curl on the notebook until the paper crinkles. The technical caveat—dry and ugly in a lab report—lands here like a pebble thrown into a crowded pond. You taste salt and the faint metallic dryness of nerves."

    ari_navarro "So—some engineered options could make the very neighborhoods we're trying to save slide away faster?"

    dr_noor_patel "Yes. If we do only armor and ignore marsh regeneration, the erosive feedbacks intensify. The mitigation has to be coupled: engineered defences plus living shorelines, sedge planting, managed retreat paths. Otherwise... we trade one failure for another."
    "Dr. Noor taps a tablet and spins a quick visualization—sediment plumes and shifting shoreline lines. Camera crews passing by angle for a shot, but Dr. Noor closes the tablet and pockets it."

    dr_noor_patel "I didn't bring this up earlier because I worried about panic. But you asked for the full briefing. You should have it before you make any public alignment."
    "You feel the small climb of responsibility—the thought that every word you speak now will be folded into other people's futures. The arousal in your chest is deliberate: not panic, but crisp focus."

    menu:
        "Ask for the full dataset, now":
            "You press for numbers, for error bars, for ranges. Dr. Noor exhales and hands you the tablet: rows of scenarios, shaded uncertainty bands. The air sharpens around the facts."
        "Hold it for a quieter time":
            "You tell Noor you need to hold the details until after you've felt the political terrain. Noor's mouth tightens—reluctant, but understanding. They nod and tuck the tablet away."

    menu:
        "Fold the flyer into your pocket":
            "You fold the flyer and slide it into your jacket, the crease softening with the warmth of your hand. Sora's shoulders relax—minor triumph—and they loop an arm around a volunteer, returning to the megaphone."
        "Ask Sora a pointed question about logistics":
            "You ask about supply chains and command structure. Sora brightens; they pull up a map from their satchel and starts enumerating staging zones, volunteer rosters, and contingency routes—practicality wrapped in idealism."

    menu:
        "Join Sora's People's Emergency Plan openly.":
            jump chapter4
        "Accept Lina's conditional pilot; lead the municipal study.":
            jump chapter7
        "Expose Ephraim's funding ties; campaign to block private development.":
            jump chapter10
        "Refuse binary choices — propose a hybrid council process on the spot.":
            jump chapter13
    return
