label chapter16:

    # [Scene: The Glasshouse | Evening]

    scene bg ch14_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft drip of water, a distant hum—generators or a town that never quite sleeps]
    # play music "music_placeholder"  # [Music: Low, mournful cello with the wind threading through it]
    "You are bent over a table littered with jars and folded maps. Your fingers smell of mud and cedar—work that keeps asking for more of you. Nia moves between a stack of seed trays and a"
    "coil of rope, humming under her breath, bright as if she can still will hope into stubborn soil."

    "You trace a pencil arc on a page labeled with the headers you promised you'd keep" "Pilot Zones — Community-Run."
    "Nia leans on the table. She watches you with that frankness little sisters have, as if she measures you not by what you save but by what you refuse to lose."
    show nia_voss at left:
        zoom 0.7

    nia_voss "You know, stubborn would be a compliment if you learned to bribe the tide sometimes."
    show mara_voss at right:
        zoom 0.7

    mara_voss "I'd rather bribe it with plants than promises, yeah."

    nia_voss "Promise me one thing: when the town sings your praises, don't let it go to your head. Save it for the seedlings."

    mara_voss "I'll save it in the field notebook. Somewhere between tide tables and regret."
    "The two of you fall into the rhythm of work. The Glasshouse smells like wet earth and old glass; the light is soft but short. Outside, the headland's machines whisper—an undercurrent you try to ignore."

    menu:
        "Hand Nia the next tray":
            "You pass the tray to her. Her fingers are quick and efficient, and she hums as if planting is an incantation. For a moment, the room feels like a tiny, defiant world."
        "Keep the tray and sort the labels":
            "You keep the tray. Labeling is an act of ownership; each sticker is a small boundary against the developer's bulldozers. Nia rolls her eyes, amused, and sorts a seed packet in the blink between heartbeats."

    # --- merge ---
    "The scene continues."
    hide nia_voss
    hide mara_voss

    scene bg ch14_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The faint, mechanical scrape of metal—surveyors measuring, the developer's geometry cutting into place]
    "You sleep less these nights, not from panic but from the piling logistics—permits, volunteer rosters, seed schedules. You are building not only habitat but the scaffolding of a movement: phone lists, lunch rosters, a map of"
    "who can operate a pump and who can stand at a microphone. It is less glamorous than blockades and more stubborn than press releases. It is, you tell yourself, the work a town can hold."
    # [Scene: The Headland | Morning]

    scene bg ch14_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Heavy machinery breathes; a metallic clang punctuates the air]
    # play music "music_placeholder"  # [Music: Sparse piano chords; a cold, flat undertone]
    "You stand at the edge of the site and feel the cold press of a different economy against your skin: diesel and possibility. The developer's representatives move with the sleek synchronicity of a plan that has"
    "rehearsed being inevitable. They present renderings like small, gleaming futures, and people in hard hats nod as if the pictures were contracts signed in advance."

    "Developer" "We can protect most of the town. Jobs will follow. We have engineering studies—"
    show mara_voss at left:
        zoom 0.7

    mara_voss "Engineering does not equal ecology. A sea wall aims against a symptom. It doesn't breathe. It doesn't feed people with the same hands that used to fish these flats."

    "Developer" "Ms. Voss, we understand your concern. What we propose is mitigation—adaptive elements—"

    mara_voss "You call it adaptation. Do you know the name of the cordgrass that binds this marsh? Do you know the inlets older than your budget lines?"

    "Developer" "We can include—"

    mara_voss "You can include a planter, a promenade, a plaque. But inclusion in a rendering is not a habitat. The little channels will be cut off. The juvenile fish will lose nursery grounds. Jobs made by this will be short-lived if the fish leave."

    "Developer" "We have to consider the town's immediate needs. Ebb and flow is simply—"

    mara_voss "Not simply."
    "You can feel the weight of the crowd that watches from beyond the headland—families, old fishers, people who have never had the luxury of ideological purity. The developer smiles with the practiced patience of someone who believes compromise belongs to the present."
    "Tomas Calder arrives, his cap older than the company vehicles, his hands smelling of tar and early tide. He does not turn toward the developer's glossy promises with either contempt or blind hope; he turns toward you."
    show old_tomas_calder at right:
        zoom 0.7

    old_tomas_calder "You were right to call this out. But right doesn't always put bread on the table."

    mara_voss "No. But the wrong doesn't always keep houses either. We are not choosing between jobs and no jobs—we're choosing what kind of jobs, and what they'll last."

    old_tomas_calder "Young people need more than ideals. They need roofs. I'm not blind to that, Mara—not anymore."

    mara_voss "I'm not asking for blind loyalty. I'm asking for time, for pilots that can show both."

    old_tomas_calder "Time is faith in people. Faith is thin these days."
    "The developer's voice hums back, a smooth overlay. You leave them talking and walk the perimeter, feeling each marker like a small landmine of future grief."
    # [Scene: The Dock | Low Tide, Late Afternoon]
    hide mara_voss
    hide old_tomas_calder

    scene bg ch14_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A gull's distant cry; the slap of a hull nudging the pier]
    # play music "music_placeholder"  # [Music: A single clarinet line; a memory of warmer days]
    "Elias 'Eli' Calder is at the dock, hands deep in ledger pages, mouth set against a worry you already know. He doesn't announce his decision with drama—he sets a hat on the ledger like a bookmark"
    "and looks at you with an amber patience that has weathered storms and small cruelties."
    show elias_eli_calder at left:
        zoom 0.7

    elias_eli_calder "They're offering a relocation package. Work in the city for a year, maybe two. It'd be steady. Tomas says my uncle could get a contract down there with men he trusts."
    show mara_voss at right:
        zoom 0.7

    mara_voss "You're thinking of leaving."

    elias_eli_calder "I am thinking of keeping the family afloat. My brother's mortgage doesn't wait for seagrass to prove itself. You asked me to choose between immediate survival and an abstract future. I can't—"

    mara_voss "I didn't ask you to leave."

    elias_eli_calder "You asked me to trust that what you're doing will pay out. That the town will turn—so I can keep building boats. Trust is a useful thing when rent is not due."

    mara_voss "So it comes to rent."

    elias_eli_calder "Do you think this is easy for me?' (He gestures at the ledger, at the small fleet tied and idle.) 'Do you think I want to walk away from here? From my hands' work? From you?"
    "Mara Voss: (everything wants to curdle into blame) 'Then don't.'"

    elias_eli_calder "If it were that simple I'd still be young enough to believe simplicity.' (His fingers drum the ledger. He looks at you, eyes asking for permission he will not ask aloud.) 'I love this place, you know that. I love what you do. But love doesn't buy bait, Mara."
    "Mara Voss: (the name in his mouth is heavier than any anchor) 'If you go—'"

    elias_eli_calder "If I go, it won't be because I don't believe. It'll be because I'm tired of watching us survive on promises—of seeing Tomás patch roofs with borrowed lumber.' (He reaches for your hand; his thumb traces the scar on your palm, a small, private geography.) 'I want to be someone who can fix things now. Not when hypotheticals pay out."
    "You stay silent, because the argument you want to make—about long-term resilience, about the town as living economy—is also an article of faith that requires time people don't have. He squeezes your hand once, a farewell disguised as comfort."

    elias_eli_calder "You taught me to see the shore in layers. I need to feed my people between tides."

    mara_voss "So you'll go?"

    elias_eli_calder "By next week."

    mara_voss "Will you—write sometimes?"

    elias_eli_calder "I'll send pictures of the city nets if you send pictures of the first planted cordgrass bed."

    mara_voss "That's not the same."

    elias_eli_calder "No. It never is. But it's something. Please—keep doing the work. For the town. For me. For what remains."
    "He leaves his brass compass—one of the things he always wore—on the ledger. You watch him walk, small against the scaffolding, and you know that this is not only a physical leaving. It is a recalibration: of loyalty, of what you can carry alone."

    menu:
        "Pick up the compass":
            "You lift the compass. It is heavier than it looks, a cold, circular weight. You tuck it into your jacket like a promise you don't yet trust."
        "Leave the compass on the ledger":
            "You leave it. Let it be his to carry back into your life if paths cross. The ledger closes with a soft thump and a handful of salt on the page."

    # --- merge ---
    "The scene continues."
    # [Scene: The Marsh | Dawn — Months Later]
    hide elias_eli_calder
    hide mara_voss

    scene bg ch14_f99e88_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The marsh is quieter now; fewer gulls, fewer boats]
    # play music "music_placeholder"  # [Music: A minor violin swell, then a slow, resigned fade]
    "You come to the marsh early, before the town wakes. The developer's raised boardwalk cuts across one side of the cove like a scar; it gleams utilitarian and certain. On the other side, in the places"
    "you and the community smudged seeds into soil and stitched small, living defenses, green lifts like stubborn breath."
    "People pass you sometimes—the ones who still fish, the ones who make delicate new livelihoods from guided ecology walks and small-scale nursery work. They nod. Some days, gratitude is enough. Some days, gratitude is a thin coat against a chill that goes all the way to the bone."
    "Nia runs up with a tin of coffee, cheeks bright from wind. She sits beside you on the old driftwood you turned into a bench."
    show nia_voss at left:
        zoom 0.7

    nia_voss "We have a school group coming in next week. Rina found a grant for a lesson plan. Kids will learn about nursery beds."
    show mara_voss at right:
        zoom 0.7

    mara_voss "Good. Teach them the cords and the channels. Teach them to name what matters."

    nia_voss "Do you ever regret not taking the other path? The negotiations?"
    "Mara Voss: (you think about renderings that promised protection and instead produced a boardwalk and offices; you think about Elias 'Eli' Calder's compass left like a punctuation) 'Regret is a tide. It comes in and pulls"
    "at whatever's left. Sometimes I think if I'd argued differently we'd have a different shoreline. Sometimes I know this is the only shoreline I'd let stand on principle.'"

    nia_voss "Principle doesn't feed everyone."

    mara_voss "No. But something does feed the place still. We salvaged pockets. We saved nursery grounds where they trusted us to manage them."

    nia_voss "And Eli?"
    "You feel the question like a cold wind. You look at the water, at the small channel where juvenile fish still dart. You think of the ledger on the dock, the compass, the thinness of promises."

    mara_voss "He went. He needed to keep his family from being at the mercy of a calendar made by other people's plans."

    nia_voss "Are you angry?"

    mara_voss "Angry and grateful and broken in ways that don't make neat narratives. I wanted—' (you stop because language falls clumsy around the shape of what you lost) 'I wanted us to be able to find both a future and keeping what made this home."

    nia_voss "Do you think he will come back?"

    mara_voss "I don't know."
    "Tomas appears in the reeds, his gait slower now. He carries a thermos and a small pack of tools. His eyes go over the marsh and rest on you with a kind of hard affection."
    show old_tomas_calder at center:
        zoom 0.7

    old_tomas_calder "You did something here. Not everything. But you did something."

    mara_voss "It wasn't enough."

    old_tomas_calder "Enough is the wrong measure for those who live here. You changed the odds. That's all anyone can do some days."

    mara_voss "We lost shore. We lost people."

    old_tomas_calder "And you kept a bit of it alive. You didn't sell the farm to a rendering. There's dignity in that, even if it hurts."
    "You stand and walk the small channel you fought for. Your boots sink in the kind of mud that remembers footsteps, and each one feels like a ledger of choices. You think of the kids who"
    "will learn the cordgrass' name, of Nia's stubborn bright hands, of Tomas' slow, dependable consent. You think of Elias 'Eli' Calder on a city dock, two time zones away; you think of a compass that might"
    "sit untouched on a shelf."
    hide nia_voss
    hide mara_voss
    hide old_tomas_calder

    scene bg ch14_f99e88_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant truck; a child's laugh as a school group practices naming plants]
    # play music "music_placeholder"  # [Music: The cello returns with a resigned, elegiac tone]
    "You preserve moral clarity. You hold lines you believe in. But the town bears new wounds—boardwalks where marsh once fed boats, offices where nets once dried. Some people left. Others stayed and retooled. The living-shore pilot"
    "you led survives in pockets, but the greater shore is different than it might have been. You carry that in your chest like a weight that has neither apology nor vindication."
    "You sit on the driftwood and let the tide come in around your boots. Salt burns at the corners of your eyes, or perhaps it's only wind. You fold open your weathered field notebook, and on"
    "the first page you write a single, quiet line—not a victory, not a resignation, but a record to hand forward."
    show mara_voss at left:
        zoom 0.7

    mara_voss "We kept what we could. We will teach them to keep more."
    "A gull wheel shadows the water. The town goes on—some flourishing, some thinning. Love, which in softer stories binds and heals, here becomes another kind of economy: accounting for who can stay and who must leave."
    "You balance the books the only way you know how—by tending what remains, by teaching names to the next generation, by refusing convenient erasure."
    hide mara_voss

    scene bg ch14_f99e88_7 at full_bg
    # play music "music_placeholder"  # [Music: A single slow chord resolves and then eases into silence]
    # play sound "sfx_placeholder"  # [Sound: The steady, muted rhythm of waves meeting land]
    "You are not whole. The horizon is not the one you dreamed of. But the marsh breathes in small places, and you are an honest witness to that persistence."

    scene bg ch14_f99e88_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    scene bg ch14_f99e88_9 at full_bg
    "THE END"
    # [GAME END]
    return
