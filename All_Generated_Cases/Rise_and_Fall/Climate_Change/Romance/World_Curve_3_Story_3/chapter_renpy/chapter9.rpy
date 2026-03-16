label chapter9:

    # [Scene: Municipal Hall | Evening]

    scene bg ch9_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low murmur of people cooling down after a long meeting; distant gulls and the steady pulse of generators]
    # play music "music_placeholder"  # [Music: Warm, rising strings with a steady drum undercurrent]
    "You step back through the doors and the world seems to reframe itself in the small, bright geometry of the annex: clipboards, sandbagged thresholds, and faces that are still lit by the afterglow of argument. Your"
    "tide-watch is warm against your palm; it pins you to the moment you chose. Tomas is speaking into a mic and calling what happened a victory—his voice ricocheting against glass and wet pavement—while other voices thread"
    "through the room like different currents. Some hands clap; some hands hang limp."
    "You feel relief like a slow tide lifting under calluses—the grant is conditional but real; the machines will hum, and crews will move. Alongside that relief, a thin ache: the trade each solution asks for, the bits of yourself you signed away to get it."
    "Tomas finds you at the edge of the crowd. He presses a hand to your shoulder, not quite a grip, more a steadying presumption."
    show mayor_tomas_nkem at left:
        zoom 0.7

    mayor_tomas_nkem "You did it, Maya. The council signed on because you made the technicals readable and the trade-offs honest. Without you, that grant dies in paperwork."
    "You keep your voice low because everything in the hall is still fragile."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "We made the grant readable, Tomas. We also set conditions. The buyouts are equitable on paper—seed-bank transfers, relocation aid, guarantees for community-managed greenhouses. None of it means anything without oversight."

    mayor_tomas_nkem "Then put the oversight where I can see it. We'll need your hand in the committee."
    "Rita approaches with a stack of forms and a coffee that’s gone cold. Her apron is speckled with soil, and she moves like someone who has learned negotiation by doing it at the market stall for years."
    show rita_ortega at center:
        zoom 0.7

    rita_ortega "People will sign, they will grieve, and they will also want to keep what can be kept. The seed bank's safe for now, thanks to you. But I want community seats on that committee. Concrete and hearts both have to be watched."
    "Your throat tightens with gratitude. Her faith is practical—rooted, like the roots she plants in the greenhouse."

    menu:
        "Talk strategy with Tomas now":
            "You slide into a quiet corner with Tomas, sketching the committee's charter on the back of a grant summary. You choose language that protects tenants and stipulates cultural transfers. Tomas nods, and the plan gains the legal backbone it needs."
        "Find Rita and listen to people's concerns":
            "You follow Rita into a knot of residents. Their words tumble out—loss, fear, pragmatic gratitude. You listen, taking notes with a small breath between every personal story, and you promise community seats with a clarity that feels like a stitch."

    menu:
        "Inspect the seed-bank transfer yourself":
            "You kneel by crate after crate as Rita and volunteers enumerate heirloom packets. The scent of dried basil and thyme reaches you through the tape and newspaper. You promise each donor that the packets will be planted in the new community greenhouses."
        "Walk the boundary line with Elias":
            "You go to the waterline where the new barriers meet old mangrove roots. Elias is there, hands in his pockets, watching tides you both have seen change. You stand shoulder to shoulder, and for a long moment, the two of you share the same silent catalog of what must be saved."
    "THE END"
    # [GAME END]
    return
