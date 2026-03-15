label chapter9:

    # [Scene: Glass Harbor Development Site | Dawn]

    scene bg ch9_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant diesel hum; the sharp click of camera shutters; voices braided into a rising static]
    "You wake to the sound of boots on plywood. Dawn tastes of rust and bleach and the copper of adrenaline. Overnight, the sky has gone thin and hard—the kind of light that makes whatever you are about to do look smaller, sharper, inevitable."
    "The barricade held the first shift. For a few hours the town's bodies were the only thing between fill and marsh. You remember hands—Tala's quick, knotting ropes; Captain Reyes' slow, stubborn fingers braided around a piling."
    "You remember the pilot habitat's warm glow, a fragile argument in wood and sailcloth against a horizon that wants to be bulldozed."
    "But the county came with papers that smell of printer ink and authority. Someone read the injunction aloud—flat legal tones that land like stones. Heavy equipment idled like predators. The developers' legal weight is a tide all its own."

    scene bg ch9_3be532_2 at full_bg
    # play music "music_placeholder"  # [Music: Percussion tightens—rapid snare taps underscoring breaths]
    "Mayor Lionel Park approaches, his shirt damp at the back, face a tired map of stress and small, private concessions. He speaks first, voice low and fraying."
    show mayor_lionel_park at left:
        zoom 0.7

    mayor_lionel_park "Maya. I—this isn't what I wanted. They're greenlit. The county has pressure. The jobs—people need work now."
    "You keep your voice measured, because measured is the only language that can be used in municipal rooms and court transcripts. But the tremor under your ribs is not for show."
    show maya_alvarez at right:
        zoom 0.7

    maya_alvarez "Mayor, jobs won't mean anything for people who have nowhere to sleep when the next surge comes. Tell me you can slow this—there has to be a hold, a mediation, anything."
    "Mayor Lionel Park: (runs a hand over his face) 'I've tried, you know that. They offered to phase protections, payouts to affected families. I pushed—God, I pushed for marsh buffers. They said 'no' unless the contract moved. The county said they needed a concrete plan today. I couldn't—'"
    "Maya Alvarez: (interrupting, soft and sharp) 'Couldn't what? Choose people over a spreadsheet? Lionel—'"
    "Mayor Lionel Park: (cuts in, ashamed) 'I chose the thing that would keep the town whole on paper. The farmworkers, the fishers—they'll have checks. Some houses can be raised. I thought—maybe—'"

    maya_alvarez "Maybe you thought you'd buy time.' (You hear how brittle that sounds. It goes where it needs to.) 'This doesn't buy what matters."
    # play sound "sfx_placeholder"  # [Sound: A shout from the gate—shouting, the metallic flare of police radios; the crowd's chant stutters then swells again.]
    "The first scuffle starts like a flint striking: a contractor tries to lift a barrier, someone in the crowd moves too fast, an official steps in with a clipboard like a shield. Bodies collapse into one another. You lurch forward because you cannot help the momentum of movement."
    # play music "music_placeholder"  # [Music: Brasses and drumline explode into very-high intensity; breaths accelerate]
    "You grab an arm to pull a youth back from the gate. The young man—face streaked with salt and dust—wrenches free, trying to wrench the fence open. Hands find one another and then pry; a glint"
    "of metal—an officer's baton—flashes. A woman falls hard; someone screams. The world contracts and everything is both too loud and impossibly close."

    menu:
        "Tackle the contractor trying to force the gate":
            "You spring forward, tackling the man from the side. Bodies fold into the wet scent of spilled coffee and salt. For a beat, your weight halts a machine's momentum. Someone grabs your arm—Tala—yelling that you'll be on a list by noon."
        "Pull back and hold the crowd together":
            "You step back and use the volume of your voice, a practiced cadence, to keep the chain from breaking. 'Hold the line!' you shout. People lean into each other; the pitch of the scuffle changes from individual sparks to a single, strained rope."

    # --- merge ---
    "The scene continues as the crowd's resistance meets the county's enforcement; arrests begin and Captain Reyes is shoved back."
    "The sound of impact is dull, then high with panic. A few are hauled into vans; handcuffs glint like small, obscene promises. You try to keep count—two, three, a handful more than you can name without"
    "your throat closing. Captain Reyes reels back from a shove, his pipe falling into the dust, scraped knuckles trembling like old rope."
    "Captain Reyes: (voice tight, old tide in it) 'They pull at the land like it's a blanket to fold away. We made stories here. We made children. You think they don't hear the sea? They hear coin.'"
    "You go to him, fingertips finding rough, varnished skin. He squints at you, that slow, remembering look, and then he laughs—an aching sound that holds both fury and sorrow."
    show captain_reyes at center:
        zoom 0.7

    captain_reyes "You did what you could, niña. You did."
    "Maya Alvarez: (low) 'It wasn't enough.'"
    "Captain Reyes: (waves a hand, as if shooing at fate) 'Enough is a thin coin. But you put your body where it counts. Don't let the number of cuffs be the measure of the right.'"
    # play sound "sfx_placeholder"  # [Sound: The metallic chew of heavy machinery starting; a rope of diesel smoke stings your eyes]
    hide mayor_lionel_park
    hide maya_alvarez
    hide captain_reyes

    scene bg ch9_3be532_3 at full_bg
    "By midday the developers win the small, hard ways that add up to a verdict. The mayor—pressed against the shadow of paperwork and phone calls—signs the final permits because the alternative, he says, is worse: lawsuits"
    "that will bury the town in legal limbo; the loss of other services; the collapse of whatever small economic relief he can deliver."
    "Mayor Lionel Park: (quietly, to you) 'I thought... there were ways to bend this. They didn't give them. I'm sorry, Maya.'"
    "Maya Alvarez: (meeting his eyes) 'Apologies won't hold the marsh.'"
    "He looks away, a man unmoored in his own town."
    "Evan Kaito is there, in the chaos, with a thermos of tea and the camera slung low. He moves through the crowd like a steady current—quiet, present. He hands you a paper cup; steam curls into"
    "your face, slightly sweet with mint. His camera records everything he can, the town in motion, testimony to this hour."
    "Evan Kaito: (softly) 'I tried to get the engineers to look at the saltmarsh feedback models. Sora and I—there's data I can push to the network. It's not nothing.'"
    "Maya Alvarez: (drinking, voice ragged) 'It feels like everything. It feels like nothing.'"
    "Evan Kaito: (lets out a breath) 'You saved attention. Records matter. People will remember who stood in the way when it counted.'"
    show maya_alvarez at left:
        zoom 0.7

    maya_alvarez "Some families already told me they'll take the payout. They can't wait for policy to catch up with their rent."
    "Evan Kaito: (his jaw tightens) 'I know. I'm sorry. I wish—'"
    "Maya Alvarez: (stopping him) 'Don't apologize for trying. Help me make something that counts.'"
    "Evan Kaito: (after a beat) 'I will. I can take what we have—compile it, push it. There are sympathetic engineers inland. I can build a public archive. It'll be raw, but it will be a record.'"
    "Maya Alvarez: (voice low but building) 'Make sure their names are on it. Make sure Captain Reyes' testimony is front and center. Make sure the children know what was here.'"
    "Evan Kaito: (nods) 'I'll keep recording. I'll travel. I'll—'"
    "He looks at you then, and there's a question in the quiet between words—one that trembles with personal risk. You both know the underside of 'I'll' can be 'I can't stay.' His eyes search yours for permission, for shared plan, for something you can't afford to promise."

    menu:
        "Tell Evan to stay and fight with you":
            "You reach for his hand and squeeze. 'Stay,' you say, though you know 'stay' will mean both of you living in a town hollowed at its edges. His fingers close around yours, slow and sure, and for a second both your hearts skip like stones."
        "Tell Evan to take the recordings and go wider":
            "You pull your hand back and place the camera strap in his palm. 'Take it,' you say. 'Go where it will be listened to.' He nods, voice clenched: 'For the marsh.' He hugs you, long and soft, then turns, packing the footage like a small, heavy hope."

    # --- merge ---
    "Regardless of the choice, the scuffle's aftermath and the town's losses shape the evening; plans are made to carry the record of this day onward."
    "The scuffle's crest leaves us bruised in public and raw in private. A few people accepted payouts at the barricade—checks in hands, faces torn between relief and shame. The moral high ground fractures into sharp, dangerous"
    "pieces as families weigh the safety of today against the promise of tomorrow. You watch neighbors you grew up with sign forms, the seed beads in Tala's hair catching the light like small indictments."
    # play sound "sfx_placeholder"  # [Sound: Quiet sobbing and the low grind of a bulldozer beginning its first measured cut]
    hide maya_alvarez

    scene bg ch9_3be532_4 at full_bg
    "Captain Reyes walks the edge of the marsh, fingers trailing the top of the grass as if reading a memory. He speaks to the land in stories—how they used to run gillnets in the channels, how"
    "an old hurricane once taught them to raise houses on stilts. The stories are ritual, small anchors against erasure."
    "Captain Reyes: (voice nasal with salt and age) 'They'll put in stone and concrete. They'll call it 'protection.' But they can't hold the taste of this salt. You keep the stories, niña. Tell them again.'"
    show maya_alvarez at left:
        zoom 0.7

    maya_alvarez "I will. I'll keep telling them. I promise."
    "Captain Reyes: (nods) 'You carry a strange tide.'"
    # play music "music_placeholder"  # [Music: A furious, driving motif—violins and percussive hits—pushing the scene to its emotional apex]
    "By evening the site is a map of what will be and what was. The heavy machines have made their first shallow pen marks. The marsh's contours are measured and translated into lines on a consequential"
    "drawing. The pilot habitat stands like a shrine just beyond the new perimeter, its light softer and more stubborn than the glare of survey lamps."
    "You stand on the boardwalk as the wind shifts; ash and dust hang in the air like a memory of storm. The town smells of hot metal and wet soil and the faint sweetness of crushed"
    "seedpods preserved in pockets. People who stayed crowd the railings, hands white on the wood, eyes hollow but unbowed."
    "You feel a hollow growth in your chest—an absence shaped like a future you had sketched and folded into your pocket. It hurts, sharp as a new salt blister. But under the ache is something else: a tight, fierce promise."
    "Maya Alvarez: (thinking) 'We saved memory. We made noise. Evidence exists now—names, recordings, testimonies. That has value.'"
    "Evan stands beside you, camera off for the first time all day. He offers his jacket without a word; the gesture is small, ordinary, counted among the rare acts that change things by being kind."
    "Evan Kaito: (quiet) 'I can leave tonight. I can get the footage to Sora and to a few contacts who will run models on it. They'll publish. It won't stop the machines here now—but it will make the work harder for them elsewhere.'"
    "Maya Alvarez: (softly) 'Then go. Take everything.' (There is no heroism in the instruction—only the clean math of futures.) 'Don't make promises you can't keep. Help the people we've lost today by making the story hurt in the right ears.'"
    "Evan Kaito: (searches you) 'And you? Will you—'"
    "Maya Alvarez: (eyes on the marsh) 'I have to carry this fight somewhere else. We need pressure centered on regulation, on structural changes. I won't be able to do it all from here. I have to make alliances, gather evidence, raise the tide of public will bigger than their contracts.'"
    "Evan Kaito: (a hard swallow) 'So we—'"
    "Maya Alvarez: (finish his thought) 'We do different work. We both hold pieces.'"
    "He takes your face in both hands for a breath—the gesture not to stop you but to steady both of you. His lips meet yours—a brief, brave punctuation in a long, ragged sentence. It says many things: gratitude, apology, love, and a permission to go."
    "Evan Kaito: (voice breaking, steady) 'Make them listen.'"

    maya_alvarez "And you make sure they remember why we tried."
    # play sound "sfx_placeholder"  # [Sound: The distant click of the excavator biting earth; a gull screams once, a single sharp note]
    hide maya_alvarez

    scene bg ch9_3be532_5 at full_bg
    "You walk the boardwalk one last time that night. People move to whatever next is available—some to raised foundations, some to the checks in hand that buy them a bus ticket away. There are embraces and"
    "quiet goodbyes, and the town rearranges itself around loss. Captain Reyes stands at the cliff, pipe in mouth, and when you turn to him he grins—worn but true."
    show captain_reyes at left:
        zoom 0.7

    captain_reyes "You did the right thing. You didn't let them pretend they didn't know."
    "Maya Alvarez: (voice small) 'Right isn't always enough.'"

    captain_reyes "Right is a seed. It grows where you plant it."
    "You feel the seed in your satchel, the small fold of paper with collected names and testimony Evan has already copied to his drives. It is both weight and tool."
    # play music "music_placeholder"  # [Music: Resolves into a hopeful, ascending motif—strings unfurling into a fragile but determined theme]
    hide captain_reyes

    scene bg ch9_3be532_6 at full_bg
    "You leave Maris Bay at first light, the town a map of ragged losses and small, stubborn continuities. You do not leave in defeat. You leave with guilt braided to resolve; you leave with a public"
    "record and a coalition of names; you leave with Captain Reyes' stories in your ears and Tala's laughter like an anchor at your back. You leave because the fight needs to travel—because scaling the argument beyond"
    "one site is how you make the next barricade stronger."
    # [Scene: Boardwalk | Dawn—Departure]
    # play sound "sfx_placeholder"  # [Sound: A single gull; the steady footfall of moving on]
    "Evan helps you carry the last pack to the car. There is a stillness between you that is not closure but not resignation. It is agreement on separate tasks: he will carry the footage and the"
    "memory into networks; you will carry the organizing, the law, the long, slow grind toward policy that can hold."
    "Evan Kaito: (softly) 'Promise me you'll write. Promise me you won't let this be a quiet memory.'"
    "Maya Alvarez: (a half-smile, resolute) 'I won't. We'll make it loud together, from different places.'"
    "You pause at the rail, looking back at the marsh as the first machine makes a shallow, obscene mark. The grasses bow as if in mourning; the pilot habitat's light blinks one more time before you turn away."

    scene bg ch9_3be532_7 at full_bg
    # play music "music_placeholder"  # [Music: A single hopeful chord held long, then gently releasing]
    "You carry guilt like ballast and hope like a torch. The story of Maris Bay continues elsewhere—testimony, data, legal challenges, grassroots coalitions. You have lost ground, but you have not lost the people who remember. You"
    "have not lost the proof that communities can rise up and that their resistance is recorded."
    "As the road unwinds, the horizon holds both the memory of what was and the stubborn belief that repair works like a stitching—slow, stubborn, and human."

    scene bg ch9_3be532_8 at full_bg
    # play music "music_placeholder"  # [Music: Quiet, warm outro—piano and low strings]

    scene bg ch9_3be532_9 at full_bg
    "THE END"
    # [GAME END]
    return
