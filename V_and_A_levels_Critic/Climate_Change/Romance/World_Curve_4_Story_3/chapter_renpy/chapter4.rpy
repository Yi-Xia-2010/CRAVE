label chapter4:

    # [Scene: Tidewatch Harbor | Late Afternoon]

    scene bg ch4_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Bright, driving strings with a buoyant percussion undercurrent]
    # play sound "sfx_placeholder"  # [Sound: Gull calls, the slap of waves against pilings, a low murmur of conversation]
    "You stand shoulder-to-shoulder with Elias Hart, your maps spread across a battered folding table. His canvas satchel lies open beside him—stacks of hand-printed flyers, a coil of twine, the wooden whistle catching the light. Your tide-mapped"
    "charts are weighted by a coffee mug; salt has crusted the rim of the mug and crustles under the cardboard sleeve when you move it."
    show elias_hart at left:
        zoom 0.7

    elias_hart "Look at this turnout. Iris just promised three boats to help haul in the first platforms if we get the go-ahead. Samir's already filming the lines—he says the framing looks like a movement."
    "You feel the pulse of the crowd through the soles of your boots—the warm, impatient energy of people ready to act. The smell of fried fish and seaweed from a nearby stall weaves with the sharper"
    "tang of wet paper and your own damp scarf. Your chest lifts in a way that feels almost like exhaling for the first time in months."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Tell me what you heard—what Mayor Ana told you before she left the meeting?"

    elias_hart "She said the council approved a pilot. Modular platforms, seed funding for marsh restoration—conditional, but it's green-lit. The vote was close, but it's a start. People are... they were clapping in the chamber. You should've seen Julian—he had that ridiculous, relieved smile."
    "You close your fingers around the map's edge. The inked contours of neighborhoods you traced late into the night seem suddenly like a network of small promises. For a beat, the guilty ledger in your chest quiets; it is replaced by a clean, raw hope that hums beneath your ribs."
    hide elias_hart
    hide maya_reyes

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Laughter rising like a tide]
    show elias_hart at left:
        zoom 0.7

    elias_hart "We did this, Maya—no, you did. I just stole your charts and added pretty glue."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "You mended the flyer better than I could have kept the margins straight."
    "Elias Hart's laugh throws sunlight into the space between you. The wind tangles his hair; a stray curl brushes the side of your face. Your fingers twitch toward it—habit, memory—then stay, fingers folded into the map."
    "There is a steadiness in the small restraint; you keep it because this moment is not only about you."

    menu:
        "Offer Elias your scarf to keep him from shivering":
            "You drape your blue scarf over his shoulders; he laughs and ties the ends together in a clumsy knot around his neck, and for a second he looks like a child who stole his mother's warmth."
        "Keep the scarf—let it be a quiet talisman between you":
            "You fold the scarf back into your jacket, feeling its familiar weight. He notices and meets your eyes, a question in the way his smile softens."

    menu:
        "Suggest a celebratory tide-cleanup after the workshop":
            "You pitch the idea; volunteers clap and two fishermen exchange nods. It becomes a small ritual—repair and prepare in the same breath."
        "Push for a tighter volunteer sign-up list focused on technical roles":
            "You shift the conversation toward logistics; fewer hands at first but more trained, and people accept the trade-off, signing their names with solemn determination."

    menu:
        "Step onto the pier and call for an immediate occupation":
            "You imagine the cry you'll sound: a dozen voices turned into dozens of bodies, the pier a living argument. Your mouth opens; the air tastes of copper and ambition."
        "Pull Elias aside to sketch a legal plan with Professor Kim":
            "You see Julian's lined fingers moving across clauses and timestamps; the legal machine begins its soft hum. It's slower, but it can anchor the council's commitment."
        "Walk up to Mayor Ana and ask for a private, binding negotiation":
            "You picture Ana's tired eyes and the quick exchange of names for lists; the compromise could secure scaffolding for the plan now, while asking patience of the crowd."

    menu:
        "Organize a waterfront occupation to pressure funding now.":
            jump chapter5
        "File a scientific injunction with Professor Kim—play by the rulebook.":
            jump chapter5
        "Negotiate quietly with Mayor Ana to lock in limited gains.":
            jump chapter13
    return
