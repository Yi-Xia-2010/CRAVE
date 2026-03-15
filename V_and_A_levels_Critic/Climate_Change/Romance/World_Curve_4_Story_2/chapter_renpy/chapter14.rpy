label chapter14:

    # [Scene: Glass Pier | Late Afternoon → Dusk]

    scene bg ch13_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low, insistent hum of generators; reporters' murmurs; the speakers woven into the mural catch and replay a child's voice, then another, then a chorus like tide-rippled memory.]
    # play music "music_placeholder"  # [Music: Tense, urgent strings building beneath the noise]
    "You tell yourself this was the point of going quiet with Ori: to make something undeniable where the numbers and memos could not. You remember the long nights on the Ferryworks, solder smoke and salt on"
    "your sleeves, Ori's hands stained with algae and solder. You remember the way he insisted the story had to be human—small speakers, clipped tape of neighbors telling where they had learned to swim, where they had"
    "learned to fish, where their aunt kept a tin of spices through three floods. You remember the weight of that decision: to show, to place vulnerability where it could be filmed."
    "Now the show is live."
    "Ori Navarro is there—close, a shadowed figure against the mural, welding goggles pushed up like a crown. He catches your eye and grins, and for a instant the world narrows to the familiar cadence of his smile. Then the camera shifts and the city widens again."
    show ori_navarro at left:
        zoom 0.7

    ori_navarro "They can take our permits, take our plans—can't patent a grandmother's laugh."
    show ava_maren at right:
        zoom 0.7

    ava_maren "He says it like a joke, but your throat tightens. Laughter and grief live in the same place on you lately."

    ori_navarro "Hey. It's not nothing. Look—"

    ava_maren "I know it's not nothing."
    "You step closer to the mural. The speakers crackle; a little boy's voice says, 'My boat is named Lila.' The sound slices clean through the press's chatter."

    menu:
        "Step forward and speak":
            "You walk a few paces into the light, paper script folded in your hand. The camera finds you; the crowd hushes. Your voice shakes, but your words land—short, true. Faces soften. For three heartbeats you think we've done it."
        "Let Ori take the first words":
            "You stay behind him and let Ori step into the glare. He jokes, he slips into charm, and the room leans in—he makes them feel it. You feel proud and strangely hollow, as if the feeling belongs to him and to the moment, not to the tenure you were trying to secure."

    menu:
        "Interrupt Calder with a public call":
            "You step forward and raise your hand. The reporter nearest you flashes a light. 'Mr. Voss,' you shout, voice cracking, 'will you sign a legally binding community tenure clause—today—rather than speaking in abstractions?' The rig goes still; Calder smiles, answers a PR-polished rebuke. The exchange is viral for a day, then edited, then softened."
        "Record Calder quietly and let the footage speak later":
            "You hold your recorder low and stay out of the shot. You watch his smile and file it away, a slow, cold thing in your pocket—evidence to be used like a scalpel, not a blowtorch."
    "THE END"
    # [GAME END]
    return
