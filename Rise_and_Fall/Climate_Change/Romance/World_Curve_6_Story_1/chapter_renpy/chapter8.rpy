label chapter8:

    # [Scene: Community Center | Afternoon]

    scene bg ch8_6b08b4_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, slow cello with distant gulls stitched underneath]
    # play sound "sfx_placeholder"  # [Sound: Paper rustling, murmur of a growing crowd, the faint hiss of a kettle in the back]
    "You stand beside Mira at the front table, hands deep in the packet of seed envelopes she is handing out. The scarf around your neck is still damp from the morning’s rain; it smells of earth"
    "and boiled tea. Your leather journal lies open where you left it—pages of names, street songs, recipes folded into the margin like specimens."
    show mira_soto at left:
        zoom 0.7

    mira_soto "Here—one for you, one for the reporters. Tell them which tomato sings in July. Make it sound like home."
    show ava_marin at right:
        zoom 0.7

    ava_marin "They already know the tomatoes. They don't always understand why we teach who planted them."
    "Mira presses her palm to your shoulder with a quick, fierce comfort."

    mira_soto "Then tell them it's not about fruit. Tell them it's about curving the map with the things people leave behind."
    "You take a seed envelope and feel the dry weight of it between your fingers. The room has settled into a hush; the audio loop of an elder's voice folds around the crowd like a tide."

    "Journalist" "Ava—if I can—why make this public exhibit now? What's the point when construction's been halted?"
    "You study the faces in the front row: students with notebooks, a woman with a camera still wet with fog, a man whose work jacket smells of diesel. Their attention presses on you like weather."

    ava_marin "Because if we do not name the streets, someone else will. If we do not make our lives legible, they'll translate them into consumable pieces—'heritage' you can visit but not live in. This is how our names survive."
    hide mira_soto
    hide ava_marin

    scene bg ch8_6b08b4_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low murmur of agreement, a single hand clapping softly]
    "You open the journal and read. You say the names aloud—each one a small bell—tell the little song your neighbor hummed while mending nets, recite a recipe in which oregano cancels the taste of brine. The"
    "room listens. The judge's preliminary opinion had been faxed earlier and now sits on the lectern; someone nudges it toward you with a reverent, almost guilty hand."

    "Volunteer" "They cited cultural harm. It's—it's in the opinion."
    "You look down at the judge's typed lines: the legal language is clinical, but the phrase 'cultural harm' sits heavy as a stone. For a moment, victory feels like a light you can hold."
    show ava_marin at left:
        zoom 0.7

    ava_marin "We won a name."
    show mira_soto at right:
        zoom 0.7

    mira_soto "We won a name,' she echoes, quieter—then adds, 'and names can be frame and cage both."
    "You keep reading because the room wants proof, wants narrative. Your voice cracks once on a line: a child's playground song you can almost hear under the rain. The reporters scribble."

    "Reporter 2" "Do you think recognition will change policy? Some developers are already calling this—"
    "Before they can finish, a commotion at the door. A man in a suit slips in, his face practiced, his brochure glossy. Behind him: a photographer with a smile that reads like hunger."

    "Developer" "Beautiful work. Imagine a 'Tideward Heritage' walkway—curated tours, protected parcels, low-impact visitor lodging. We can safeguard the visuals and fund maintenance."
    "You feel the room contract. The word 'heritage' falls like a banner you did not hang."

    ava_marin "And who will live in those parcels?"

    "Developer" "We can include subsidized units, of course. But tourism will sustain it—maintenance, preservation. It's pragmatic."

    mira_soto "Pragmatic for whom?"
    "The exchange becomes a small skirmish of tones—polite, cold, suddenly sharp."

    ava_marin "Our lives are not props. Protection must be for people, not postcards."

    "Developer" "You're speaking in absolutes. There are investors who can make this viable."
    "You feel the familiar tug: a moral clarity that becomes a ledger. The judge's language—intended to protect—has made you legible; that legibility is a magnet."

    menu:
        "Read the elder's last song in full":
            "You let the room hear the full length of the song: the cadence of feet on the boardwalk, the exact line about rain that saves the boats. People close their eyes. A few in the back wipe their faces. For a split second, no one is negotiating."
        "Pivot to facts—present a list of households at risk":
            "You flip pages, your finger finding the spreadsheet of addresses and needs. The room leans in with a different hunger—logistics and lists. Mira’s hand tightens on yours; someone at the back starts speaking about relocation stipends. The energy shifts from elegy to exigency."

    # --- merge ---
    "The two reactions bloom differently across the room—one softens, the other mobilizes"
    hide ava_marin
    hide mira_soto

    scene bg ch8_6b08b4_3 at full_bg
    # play music "music_placeholder"  # [Music: The cello grows more insistent; a dissonant high note threads under the murmur]
    "The day passes like some slow, tidal thing. Journalists cluster around the exhibit, cameras framing hands and weathered signs. The judge's opinion is quoted in the local feed by evening—a line of protective language. For a while, you can taste vindication like salt."
    # [Scene: City Hall Promenade | Early Evening]

    scene bg ch8_6b08b4_4 at full_bg
    # play music "music_placeholder"  # [Music: Thin piano, a cold wind note]
    # play sound "sfx_placeholder"  # [Sound: Distant construction horns, the click of a reporter's recorder]
    show evelyn_harrow at left:
        zoom 0.7

    evelyn_harrow "Congratulations on the exhibit,' she says, the words even, measured. 'The judge's language gives us room to formalize preservation."
    show ava_marin at right:
        zoom 0.7

    ava_marin "Preserve what? A bench with a plaque? A diorama of poverty?"

    evelyn_harrow "Protected parcels can secure certain blocks—preserve facades and allocate funding for upkeep. We can create a trust, a governance board. This is how cities codify memory."
    "You fold your arms against the wind. The promenade smells sharply of diesel and municipal disinfectant."

    ava_marin "And who sits on that 'governance board'?"

    evelyn_harrow "Representatives—nonprofits, local leaders, private partners. It will be a partnership."
    "You can see, with terrible clarity, how the language will bend. 'Preservation' becomes a product, and products require customers."

    ava_marin "So—those most in need get priced out while facsimiles of our porches become a revenue stream."

    evelyn_harrow "Not necessarily. There will be assistance programs."

    ava_marin "Assistance is a migration plan by another name. The cost of living rises when a place becomes 'heritage'. The people who made it live there can't always pay that premium."
    "Evelyn Harrow pauses. For a breath, her steel gray eyes flicker—complex, as if some private ledger balances across a colder calculation."

    evelyn_harrow "I do not want to displace anyone. But I do want Tideward remembered—functionally and legally. We must make decisions for the city's long-term viability."
    "The exchange stops without resolution. You hear, above the promenade's curated calm, the distant sound of a moving truck starting up on a street you know."
    # [Scene: Moonlit Boardwalk | Night]
    hide evelyn_harrow
    hide ava_marin

    scene bg ch8_6b08b4_5 at full_bg
    # play music "music_placeholder"  # [Music: Sparse strings and a low, hollow wind instrument]
    # play sound "sfx_placeholder"  # [Sound: Oars in water, the muffled voice of neighbors speaking in small clusters]
    "You walk the boardwalk later, your journal tucked against your ribs. The exhibit's prints still hang in your head—faces, names, the judge's typed line—and the developer's brochure like a flavorless aftertaste. Families gather in doorways beneath"
    "the soft light; someone is loading boxes into an old pickup. You can see the price tags in the eyes of neighbors when you ask about relocation help; numbers cut across their faces like cold light."
    show tomas_marin at left:
        zoom 0.7

    tomas_marin "This is the price of being legible. They'll take the story and sell you a ticket to it."
    "You sit beside him. The wood is damp and smells of salt and old varnish. He rubs his hands together, as if warming them from a memory."

    tomas_marin "We fixed boats for a living. Now the boats are props in someone else's brochure."
    show ava_marin at right:
        zoom 0.7

    ava_marin "We asked to be heard. We wanted rights, not displays."

    tomas_marin "I never trusted anything with a committee."
    "The boardwalk hums with small, practical conversations: who needs an engine part, who can take over a rooftop garden. Each talk is a small repair against displacement."
    "Your smartwatch buzzes—short, insistent. Ilan Cortez's name lights the screen: a short message, a photograph of a small, 3D-printed module with a filter cartridge and a price tag that reads like a challenge."

    "Ava Marin (reading, aloud to no one)" "Made it under cost. Mobile filters. Can be deployed door-to-door."
    "You stare at the picture until the image fuzzes. The module is small enough to fit in a palm, enough promise to feel like a weight. This is Ilan Cortez's world: tools, prototypes, immediate relief. It tugs at the part of you that wants to keep people dry tonight."
    "A memory presses against that tug—the judge's sentence about cultural harm, the developer's brochure, the faces of those priced out while facades were preserved. The prize of 'recognition' sits like a ledger on your shoulders: names saved on a page, people left on damp floors."
    "You think of the exhibit: the way the community's voice reshaped legal language, the way that language reshaped the market's interest in your neighborhood. You think of the filters—small, cheap, practical—and the immediate difference they could make."
    "Mira finds you on the boardwalk, her eyes rimmed with liquid that the fog hides."
    show mira_soto at center:
        zoom 0.7

    mira_soto "He sent you a picture, didn't he?"

    ava_marin "He did."

    mira_soto "You could go with him. Distribute the filters. Teach people to use them. Or you could—"
    "Her sentence trails because it is impossible to finish without slicing the world into two neat pieces that do not exist."

    mira_soto "Or you could keep building the archive clinic, make the city acknowledge us as people first. You're torn, Ava. We all are."
    "You rest your hand over your journal and feel the texture of twine under your palm. The sound of the marsh is a slow, patient thing. The fog folds around the lamp posts like a shawl."

    ava_marin "I don't know how to pick without feeling like I betray one side or the other."

    mira_soto "Maybe there's no choosing today. Maybe there's a way to make both less harmful."
    "You look down at Ilan Cortez's message again. The photograph of the filter is sharply lit—practicality eating the edges of ideology. Your chest tightens; your jaw sets. The ledger inside you—names on one side, urgent needs on the other—suddenly feels impossibly heavy."
    hide tomas_marin
    hide ava_marin
    hide mira_soto

    scene bg ch8_6b08b4_6 at full_bg
    # play music "music_placeholder"  # [Music: A single, unresolved minor chord held, then cut]
    # play sound "sfx_placeholder"  # [Sound: The distant beginning of rain]
    "You turn the phone over in your hand, the screen a small bright thing against the dark. You can hear every possible future—compromises, betrayals, small victories—like gulls arguing on the wind. Your next move will mark more than you know."

    scene bg ch8_6b08b4_7 at full_bg
    "THE END"
    # [GAME END]
    return
