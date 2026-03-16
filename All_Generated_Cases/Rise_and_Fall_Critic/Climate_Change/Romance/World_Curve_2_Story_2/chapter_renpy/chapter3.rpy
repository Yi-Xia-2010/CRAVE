label chapter3:

    # [Scene: Rooftop Greenhouse & Community Garden | Dusk]

    scene bg ch3_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low wind over the berm, a gull's long cry, the distant hum of generators on the promenade]
    # play music "music_placeholder"  # [Music: Sparse strings, low and contained]
    "You press your palm to the cool glass and watch your breath fog a small halo before it melts away. The greenhouse smells of damp earth, compost, and the faint mineral tang of seawater blown in"
    "from the promenade. Your notebook is open on your knees; ink pools in a corner from where you jabbed the pen too hard. Names. Needs. The forum tomorrow. The weight of every household in Harborfall folds"
    "into the list like a brittle paper map."
    show kaito_sato at left:
        zoom 0.7

    kaito_sato "We can start small. Three sensors, placed at the low coves and by Mayor Rossi's pump house. If they read the tidal surges right, we can scale actuator support — pumps, valves — only where they're needed. It buys us time without selling the town."
    "You feel the teal braid at your temple, an absurdly small compass. Your mouth tastes of metal and salt. You remember the promise you made to Tomas, to the kids who learn to fish off the promenade, to your brother. Time is a ledger that never balances."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "And if the storm comes before the pilot grows teeth? If we stall, and something breaks…"

    kaito_sato "Then we fail at being cautious. But we don't fail by taking the town out from under itself. We keep control."
    "He reaches up and lays his hand — warm, steady — on your forearm. The gesture is light, but it anchors the anxiety that makes your fingers twitch."

    menu:
        "Let him steady you—a soft exhale and a long nod":
            "You let your shoulders drop a fraction. 'Okay,' you say. The word is smaller than you want but cleaner."
        "Draw away—explain the data you still need":
            "You pull your arm back and tap at a line in your notebook. 'We need three more sampling cycles. Noor says we can't—' Your voice snaps; the room leans into the break."

    # --- merge ---
    "Kaito's expression shifts — he reads you like a map of the tides. He doesn't push. Instead he tilts his head and lets the silence do its work."
    "Dr. Noor stands near the jars labeled with salt gradients, spectacles catching the light. Her tablet blinks with charts that could be pedigree or prophecy."
    show dr_noor_alvi at center:
        zoom 0.7

    dr_noor_alvi "The sensor pilot is the least risky scientifically, but least decisive politically. We can quantify risk. We cannot quantify the time it takes to change a vote."
    "Mayor Elena, in a municipal blazer threaded with salt stains, folds and unfolds a folder as if it were a ritual. She looks at everyone from under tired lids."
    hide kaito_sato
    show mayor_elena_rossi at left:
        zoom 0.7

    mayor_elena_rossi "Votes aren't just numbers in a spreadsheet. They're meals not served, roofs not replaced, someone's life. If LuxCorp opens their purse tomorrow, there's help in people's hands next week. I don't know that the town can wait on slow data when the models…"
    "Her voice trails. Behind her, Hana wipes her hands on an apron, a sheen of oil and broth clinging to the fabric. The diner has hosted more town arguments than the council hall; it will likely"
    "host tomorrow's after-talks too. Tomas leans against a stack of reclaimed crates, the lines in his face deep as weather."
    hide maya_inoue
    show tomas_bianchi at right:
        zoom 0.7

    tomas_bianchi "Mangroves, Maya. They make storms softer. The work's heavy, but it's ours. And it brings the fish back."
    "You can see Tomas picturing the roots in his mind — a stubborn, living barricade. His hands flex; you know his offer comes with calls to his old crew and nights of backbreaking planting."
    hide dr_noor_alvi
    show hana_kim at center:
        zoom 0.7

    hana_kim "I'll host the meetings. The diner stays open. We'll feed whoever shows up debating or crying. Meals calm people—give them something to hold when everything else is loose."
    "There is, somewhere in the room, a polished folder from LuxCorp. An emissary — neat, his jacket still dry from the interior climate of corporate glass — sits a little apart, tablet angled so everyone can"
    "see the glossy renderings of a raised sea wall, segmented gates, and LED-lit access points. The renderings shine like promises."

    "LuxCorp Emissary" "A turnkey wall reduces immediate risk. It frees municipal funds for reinvestment elsewhere. LuxCorp can finance the construction and maintenance for an initial period; we'll discuss revenue models thereafter. It's fast."
    "You feel a cold pressure in the greenhouse that has nothing to do with temperature. The emissary's calm is a kind of weight; the renderings feel like a curtain being dropped, neat and final."
    hide mayor_elena_rossi
    show maya_inoue at left:
        zoom 0.7

    maya_inoue "Revenue models?"

    "LuxCorp Emissary" "Long-term maintenance is typically shared. Naming rights, public-private partnerships. We align incentives."
    "There is an undercurrent in the room you know all too well—the texture of choices that ask you to trade one set of risks for another. LuxCorp's offer smells of solvent and polished varnish; Tomas' plan"
    "smells of mud and sweat. Kaito's smells faintly of electronics and winter labs. Your notebook blurs the three plans into competing columns, each with a tally of what would—might—be lost."
    "Mayor Elena looks at you. Hope and exhaustion sit on her face like salt crust."
    hide tomas_bianchi
    show mayor_elena_rossi at right:
        zoom 0.7

    mayor_elena_rossi "Maya, people want to know what you'll recommend tomorrow. Right now, you're the clearest voice we have in that room."
    "You want to be sure. You want to avoid the damage of a rushed decision that looks like salvation until the first storm rips it open. You also know that 'do nothing until perfect' is a decision in itself—a slow slide you can't afford."
    "A gust rattles a planter. Outside the glass, LuxCorp's plaza sits placid and aloof, its edges cutting the horizon into pieces. You imagine Lucia 'Lux' Moreno — she is not here — but memory of her"
    "presence is as precise as the renderings: a sharp laugh, a hand that signed contracts, a patience that could be mistaken for certainty. Her face would be ordered, unreadable. The place she represents promises safety at"
    "scale, and that promise is dressed for cameras."

    menu:
        "Imagine talking to Lux—rehearse the negotiation out loud":
            "You mouth phrases under your breath: 'We need community oversight. No naming rights without consent.' Saying it makes it real and smaller, like a seed you can plant."
        "Turn to Tomas—ask about manpower and timing":
            "You look at Tomas and picture the crews and the tide calendar. 'How many can you get? When can we start planting?' His answer lands like a schedule for the next month."

    # --- merge ---
    "Dr. Noor: (soft but firm) 'Whatever you choose, we should quantify conditionalities. If Lux builds, what are the clauses on relocation, public access, ecosystem compensation? If we pilot, what's the fail-safe if the sensors flag an imminent breach? If we referendum, how do we frame emergency exceptions?'"
    "Your pen is blunt. You doodle a small tide-line on the margin—three marks, one above the other. You can feel the old ache beside your thumb, that dull hum that surfaced after the storm that took"
    "your brother. It returns now as a pressure behind your throat, a small animal of a thing that will not be silenced."

    maya_inoue "We need to give people a choice before they feel like they had none,' you say, and the words are raw. 'But I also need to make sure that choice isn't a cliff."
    "Mayor Elena narrows her eyes and presses her lips together. The municipal ledger in her head is a sieve; promises must fit through it."

    mayor_elena_rossi "If you take Lux's meeting, you'll be accused of selling out. If you back Kaito, you'll be accused of being naive. If you push a referendum, you'll be accused of delaying. There's no safe harbor in any of those accusations."
    "You feel the room tilt—the friendly faces, the data, the renderings—all weighing on different parts of you. Your resolve is a thin thing that frays if you tug too hard at any thread."
    # [Scene: Promenade | Twilight]
    hide hana_kim
    hide maya_inoue
    hide mayor_elena_rossi

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A bell from a small trawler, the slap of water, distant city traffic muffled by fog]
    # play music "music_placeholder"  # [Music: Low piano, notes like footsteps]
    "You step out onto the promenade to let wind carry off the greenhouse's close heat. The air is sharper here, salt and diesel and the ghost of fish. Gulls wheel and complain. Lamps cast halos on the wet timber."
    "Tomas joins you, coat buttoned tight. His breath is a steady fog. He stares out at the line where sky meets water, where once there were more rocks than there are now."
    show tomas_bianchi at left:
        zoom 0.7

    tomas_bianchi "People will follow where their bellies tell them to go. This isn't just about what's right, Maya. It's about what keeps folk sleeping at night."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "And what's right? How do I make sure they're not choosing the easy fix because they're scared?"

    tomas_bianchi "You don't. You make sure they have enough truth to decide. You lay out what it'll cost them. Let them feel the cold before they vote for the warmth."
    "You think of Hana's hands, of Dr. Noor's charts, of Kaito Sato's quiet face. Each of them believes the path they offer is the one that will keep more people alive. Each path asks someone to give up something they value."
    # [Scene: Hana's Diner | Night]
    hide tomas_bianchi
    hide maya_inoue

    scene bg ch3_98c6f2_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Clink of plates, low conversation, the hiss of the kitchen stove]
    # play music "music_placeholder"  # [Music: Guitar hum under the conversations, minor key]
    "Inside, the diner is an arm around the town. Hana moves between tables with a practiced smile, setting plates down as if distributing small, human promises. The walls smell of boiled broth and jasmine from a small pot of tea."
    "Mayor Elena sits with Dr. Noor and you, and Kaito Sato lingers by the counter. The LuxCorp emissary has left a stack of glossy pamphlets on the counter; sunlight from under the door makes them look like shards."
    show mayor_elena_rossi at left:
        zoom 0.7

    mayor_elena_rossi "If we go to LuxCorp, we buy time. Time to rebuild, to rehome, to retrofit. But we sign something—there's always something. 'Maintenance' becomes 'control' if it's not checked."
    show dr_noor_alvi at right:
        zoom 0.7

    dr_noor_alvi "We can write conditionalities. We can demand audits. But contracts are tricky—jargon hides leverage."
    show kaito_sato at center:
        zoom 0.7

    kaito_sato "We include community oversight committees. Staged rollouts. Pilot-linked funding releases. There's room in the middle."
    hide mayor_elena_rossi
    show hana_kim at left:
        zoom 0.7

    hana_kim "Middle is where most folks get stuck. They like it until it's time to choose which side of the middle to stand on."
    "You feel the room close in around you, friendly and sharp-edged. You flip to a clean page and write three headings in a column: LuxCorp — Kaito Pilot — Referendum. Next to each you list a"
    "single word: Scale. Control. Legitimacy. Beside those, you write more honest things: Lost coves. Unprepared storms. Political fatigue."
    hide dr_noor_alvi
    show mayor_elena_rossi at right:
        zoom 0.7

    mayor_elena_rossi "Maya, we need you to say how you'll present it tomorrow. The town will listen to you."
    "Your hand hovers over the page as if the pen itself could choose for you. The greenhouse, the promenade, the diner — each place has its own scent, its own weight. Each person in the room looks to you for a hinge."
    "You know, with the knowledge that has always lived in your bones, that whatever you say will bind people. You think of Lucia 'Lux' Moreno — not as a person but as a force: fast, clean,"
    "relentless in making futures into products. You think of Kaito Sato — methodical, earnest, the sort of man who wants to prove things by making them small and measuring them. You think of the referendum —"
    "the messy, excruciating democracy that keeps decisions local but slow."
    "You imagine the forum: the crowd pressed into Hana's diner and spilling onto the promenade, flashlights and children and banners made by tired hands. You imagine the mayor's face when the vote comes, the emissary's calm"
    "hand offering a pen, Tomas counting bodies to form planting crews, Dr. Noor presenting a graph that might soothe or offend."
    "The choice lands like cold rain. You know the town will hear more than the arguments; they will hear the tremor under your voice, the steadiness or the fracture."
    "Your notebook waits under your fingers. The three options you must weigh sit like three doors in front of you, each leading to different kinds of shelter—and different forms of loss."

    menu:
        "Trace the sea wall on the pamphlet—picture the shoreline after":
            "You draw a line where the wall would be. It looks tidy and decisive. It also cuts off a cove you remember putting crab pots in as a child."
        "Sketch the sensor network—map possible nodes with Kaito":
            "You and Kaito mark potential sensor points across the tide-line. The map feels hopeful and fragile, like a paper boat."
        "Draft the referendum announcement—write the opening line aloud":
            "You write: 'Harborfall will decide its future.' Saying it aloud makes the words sharper; they taste both righteous and terrifying."

    # --- merge ---
    "You inhale. The chef's bell rings as someone orders coffee. You rest your palm on the page that puts three futures beside one another."
    "Your voice is low when you finally speak, but it carries the brittle authority of a person who has loved and lost and tried to turn that into something useful."
    hide kaito_sato
    show maya_inoue at center:
        zoom 0.7

    maya_inoue "Tomorrow, at the forum, we will present choices. Not just plans. Consequences. Costs. And we will ask the town what kind of Harborfall they want to be."
    "The room listens, and in their faces you see flickers of relief, fear, calculation. The decision is not yours alone, but you are the one who will frame it. You are the hinge."
    "The night presses in. Outside, LuxCorp's plaza is a dark rectangle now, lights beginning to lace through its windows like a skeleton of promise. The tide slides in and out, indifferent. Somewhere in your chest, the old ache thrums like a distant alarm."
    "You close the notebook, the pen leaving a smudged smear across the margin. Dawn is hours away; the forum, even closer. You will carry all of these small, dangerous things with you into tomorrow."
    "You stand. You feel the weight of the room's expectation settle on your shoulders like a leaden coat."
    "You must choose what to advise the town to consider when you step to the microphone. Your decision will pull the town's rope in one direction or another—toward speed, toward patience, or toward the long, precarious work of democracy."
    "Take a breath. Feel the cold behind your throat. Count the cost."
    "Which strategy will you present at the forum tomorrow—sell space to LuxCorp, back Kaito's pilot, or mobilize a referendum to reject outside control?"
    "Meet Lux at LuxCorp—negotiate the sea wall deal"
    "Partner with Kaito—prioritize the sensor pilot and nature-based methods"
    "Organize a citizen referendum—keep decisions locally controlled"

    menu:
        "Meet Lux at LuxCorp—negotiate the sea wall deal":
            jump chapter4
        "Partner with Kaito—prioritize the sensor pilot and nature-based methods":
            jump chapter7
        "Organize a citizen referendum—keep decisions locally controlled":
            jump chapter10
    return
