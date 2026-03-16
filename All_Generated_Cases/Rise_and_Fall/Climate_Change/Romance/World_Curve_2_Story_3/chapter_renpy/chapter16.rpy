label chapter16:

    # [Scene: Town Hall | Morning — Council Chambers after the Vote]

    scene bg ch14_f99e88_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, slow piano; a single minor note repeats]
    # play sound "sfx_placeholder"  # [Sound: Quiet murmur of a crowd settling; a distant gull call cut by rain]
    "You sit near the back, hands folded over the compass in your palm until the brass grows warm. The cautious report you filed — the one you wrote with careful caveats and recommended pauses — is"
    "on the table in every hand here. You can feel the shape of it in the room, how it has been smoothed and folded to fit the council's margin notes."
    show aria_chen at left:
        zoom 0.7

    aria_chen "We've all seen the data. Dr. Morgan's monitoring has been invaluable. The pilot shows promise. With the council's approval, we'll scale the measures and layer in engineered defenses where necessary. Jobs will follow. Security for our families."
    "You hear the applause start like a tide: small, then rolling. They call your name politely when she mentions you — 'Dr. Morgan' — and faces tilt in your direction like a question."
    "You open your mouth before thinking and close it again. Your instinct is to name every conditional, every margin note; to say 'No, this is not an all-clear.' But the room is already moving toward a different grammar. Aria's smile is a hinge; decisions swing on it."

    "Aria Chen (softening)" "Isla—your leadership here has guided our science. We owe you gratitude."
    "You swallow. Her gratitude is a seal pressed over choices you didn't intend to authorize. There is a round of polite clapping, a few standing nods. Someone next to you whispers that funding transfers will be"
    "signed next week. A council member speaks of 'the economy' and 'renewal,' and the word 'hope' is placed gently like a wreath."

    menu:
        "Rise and correct her — point out the caveats":
            "You stand, the compass now a small, astonished weight. You clear your throat; the room slants toward you. 'The pilot's results are site-specific,' you begin, and the words come out precise but hollow. You can hear Aria's smile tighten before you finish."
        "Stay seated and let Aria carry the moment":
            "You stay in your chair, palms pressed to the brass. You let the applause finish. People come up to shake your hand; 'You did good,' they tell you, and each handshake presses you flatter against your own quiet objections."

    # --- merge ---
    "If you stand, Aria's eyes cool but remain courteous; she replies in measured sentences about adaptation, piloting, and mitigation — each phrase a reframe. If you sit, a young council aide hugs you like a bandage."
    "Either way, the story outside the chamber will be easier to sell than the compromises you've threaded into your report."
    # [Scene: Salt Flats | Noon — Construction and Reconfiguration]
    hide aria_chen

    scene bg ch14_f99e88_2 at full_bg
    # play music "music_placeholder"  # [Music: Low industrial hum; a muted percussive beat of metal on metal]
    # play sound "sfx_placeholder"  # [Sound: Diesel engines, the slap of waves against new concrete, the metallic rattle of chains]
    "You walk the flats with Luca at your side, watching the project as if you could read its intentions in the way machinery touches mud. The living reefs you dreamed of — low, porous structures that"
    "bend waves and nurture eelgrass — were always a compromise. Now those reefs are a line item on a ledger, validated by the monitoring you provided, and scaffolding already closes the gap where moorings used to"
    "sit."
    "A small knot of fishermen stand by a dock that used to be full of boats. Jonah is not there; you look for him the way you look for landmarks on foggy mornings. Instead, a younger"
    "man with callused hands and a face like flaking paint pushes his cap back and spits into the mud."

    "Fisherman" "They promised the jobs, aye? Said we'd get work, kept afloat. But they put concrete where the flats used to breathe. My mooring's gone. What do we do with nets when the water runs different?"

    "Luca Moreno (jaw tight)" "They told us the pilot would mean jobs and a living shoreline. They told you it would protect you."
    "Fisherman: (bitter) 'They didn't tell us our lines would snag on steel. They didn't tell us that the fish would find new routes. They told us to trust the models.'"
    "You know the models' limits. You also know what happens when limits are translated into permits and contracts. Aria's team has framed the monitored data as validation — not as a cautionary signal but as a"
    "stepping stone toward hardened structures. The concrete is being justified as 'necessary backups' and nobody in the council chamber is shouting about reed beds."

    menu:
        "Document the new coastline changes — photograph and record":
            "You lift your tablet and start taking images, tagging GPS coordinates. The blue light of screens seems absurd against raw mud, but you record every inch anyway, the way a witness keeps a ledger."
        "Confront the foreman about placement choices":
            "You approach the foreman, voice flat. He moves like machinery; his helmet bobs. 'It's council direction,' he says, and you realize the people with shovels cannot unchoose what the vote has ordered."
    "THE END"
    # [GAME END]
    return
