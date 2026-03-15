label chapter16:

    # [Scene: Brinehaven Pier | Morning]

    scene bg ch15_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Engines idle, gulls’ distant caw, the slap of tide against pilings]
    # play music "music_placeholder"  # [Music: A warm, steady chord, building lightly]
    "You arrive with your sketchbook folded flat against your chest, the leather strap of your compass pendant cool under your throat. The pier smells sharp—salt and diesel, hot bread from Rosie’s food cart, and the faint"
    "mildew of damp boxes. Hands move everywhere: volunteers tying down tarps, elders counting inventory, kids trading stickers. The town is a machine of small mercies."
    show elena_lena_maris at left:
        zoom 0.7

    elena_lena_maris "Okay—trucks A through D leaving in fifteen. Marco, you and Jonah take manifests for the north run. Rosie, can you start the warm kits? Blankets, a thermos, the sewing kits you promised Mrs. Estevez."

    "Rosie" "Already on it. I’ve got the aprons full of bandanas—someone’s already labelled the return-rights packets. We’ve got tea, too. Keep people breathing, Lena."
    "You watch Marco refuse a handkerchief offered by an older man and instead tie his own bandana around a child’s hair. He’s trying to be steady and failing at it in a way that’s painfully honest."
    show marco_maris at right:
        zoom 0.7

    marco_maris "They keep asking if they can come home. How do I tell them it’s not that simple?"
    "You feel the ache of the question like a bruise under your ribs. You answer aloud because people need the shape of your thinking."

    elena_lena_maris "You tell them that we’re building a path back. Not promises that dissolve, but legal guarantees and funding—temporary housing, retraining, and infrastructure that won’t let them fall through the cracks."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "We drafted the mobility grants—cover moving, job placement, apprenticeship in wetland restoration. We can train folks to staff the monitoring, pay them to rebuild the boardwalk. This isn't abandonment; it's transfer of power into people’s hands."
    "Iris Valence watches from the shadow of a stack of pallets, her trench cinched, the tablet still clutched like an anchor. She approaches before you can walk to her—her boots make the planks click to a different tempo."
    hide elena_lena_maris
    show iris_valence at left:
        zoom 0.7

    iris_valence "Lena. The firm is redirecting emergency grant money. We can fund more durable protections in the most trafficked zones—bolster the marina, secures docks—if you greenlight the relocation aid as a paired measure. People can stay near jobs and come back."
    "Her tone is businesslike, polished, but her eyes hold the same old calculus. You look at her, and you remember lectures on campus and arguments in corridors. There is history here—worn and complicated—and it tastes like the sea."
    hide marco_maris
    show elena_lena_maris at right:
        zoom 0.7

    elena_lena_maris "If funding comes with strings that prioritise profit over rights, I won't sign. Rights-to-return must be binding. No developer carve-outs."

    iris_valence "Then write them with me. Put the clause in plain English. Let the lawyers fight over the semantics—people need the paperwork now."
    "Dr. Asha Khatri arrives, breathless from the marsh, salt flecks in her braid. She opens a case and pulls out a small, wet soil sampler, the smell of peat quick and alive."
    hide jonah_reyes
    show dr_asha_khatri at center:
        zoom 0.7

    dr_asha_khatri "We’ll set up community monitoring stations—paid positions. The habitat restoration has to be measurable. If we can show progress in six months, it becomes much harder to bulldoze the program for profit."
    "You nod, already picturing the little rigs Jonah described—the DIY sondes powered by salvaged panels, kids learning to read tide graphs. You trace the lines in your head as if sketching a shoreline: a path that lets people go and return without losing a claim on home."

    menu:
        "Help load the last of Mrs. Estevez's boxes":
            "You lift the single, stubborn box—inside, a crock with chips and a photograph wrapped in oilcloth. Mrs. Estevez grips your wrist and squeezes hard; her eyes ask a question you answer with a nod."
        "Go to the paperwork tent to review the rights-to-return clause":
            "You push through the crowd and find Jonah and Iris bent over a tablet. The language needs a consumer-rights clause; your pen hovers until you write words that will bind a bureaucracy to a person."

    # --- merge ---
    "'You choose both, of course. There is no luxury in single choices today—only layered commitments. At the paperwork tent, you read aloud the clause until your tongue knows its edges.'"

    elena_lena_maris "‘Return rights shall include prioritized housing allocation, covered moving fees, protected place on municipal registries, and retraining stipends for up to two years.’ We need witness signatures from community reps."

    iris_valence "And an escrow mechanism. My firm can administer the escrow as long as there's community oversight."
    hide iris_valence
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "Community oversight how? Will that just be advisory?"

    "Rosie" "It’s got to be seats with votes. No lip service."

    dr_asha_khatri "We’ll add a scientific oversight seat too. The restoration program needs teeth. Funds go through the escrow and are released by milestones—planting density, survival rates, employment numbers."
    "The dialog ricochets: taut, practical, threaded with unspoken resentments and long-shared care. Each pushback forces you to name compromises you didn't want but understand. You feel the old guilt—your family house gone, the nights you spent"
    "learning policy to avoid being forced into someone else’s solution—but it is steadied by a clear plan that keeps dignity on both shores."
    # [Scene: Relocation Center (Old School Gym) | Late Morning]
    hide elena_lena_maris
    hide dr_asha_khatri
    hide jonah_reyes

    scene bg ch15_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The murmur of registration, a child laughing, scuffed sneakers]
    # play music "music_placeholder"  # [Music: A gentle, rising piano motif]
    "You move through the center like someone who has to keep her feet grounded in both worlds. The intake line is a slow river of stories—old fishermen clutching weathered binders, a single mother with two toddlers and a canvas bag of toys, a teenager who refuses to look up."
    show elena_lena_maris at left:
        zoom 0.7

    elena_lena_maris "We have temporary work for anyone willing to enroll in restoration training. Wages start above minimum; there are guarantees for childcare. No one pays for access to this."
    "A woman named Fátima reaches out, pressing a folded letter into your hand—household receipts, a wedding photo water-stained. Her voice shakes but holds."

    "Fátima" "My husband's nets are—if he can't fish, he can't earn. Will the apprenticeship mean he can fish again? Or will he end up—"
    "You take a breath. You decide to be blunt because vagueness is cruelty."

    elena_lena_maris "It means an income now and training that pays. It means you keep your claim on your house. It means, when it's safe, you can come back and work on the shoreline you helped restore. It won't be the same at first, but it will be yours."
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "And there are micro-grants for small businesses—Rosie is already mapping co-op spaces."

    "Rosie" "We’ll seed a co-op storefront in the temporary center—crafts, fish smokehouses, training in marketing. The town brand will belong to the town."
    "You slow to speak with Marco at the door. He is checking manifests but his face has the rawness of someone carrying more than physical labor."
    show marco_maris at center:
        zoom 0.7

    marco_maris "They called it state-sanctioned abandonment at first. I get why they thought that. But people are starting to see the packets you wrote—legal protections, monitored funding. It's not perfect, Lena, but it's better than silence."
    "You let yourself accept the half-true comforts—notes of progress amid messy compromise—and you fold them into your ribs like small flints."

    menu:
        "Sit and listen to Fátima's plan for a return business":
            "You crouch to the toddler’s height and talk through recipes and smokehouses; an old trade gets a new map, and you feel the warmth of practical hope."
        "Walk the intake line to personally sign each return-rights packet":
            "Your hand grows cramped from signing, but names collect under your pen like promises. Each signature anchors policy to a person."

    # --- merge ---
    "'The choices are small movements—flavor notes in a much larger chord—but they matter because they shape who you are while the town changes. You do both in shifts, letting the work be the sermon of this day.'"
    # [Scene: Marshlands / Living Shoreline Site | Afternoon]
    hide elena_lena_maris
    hide jonah_reyes
    hide marco_maris

    scene bg ch15_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Spoons tapping on thermoses, sodden earth sucked from roots, a distant motorboat idling]
    # play music "music_placeholder"  # [Music: Quiet strings, hopeful and intimate]
    "You stand ankle-deep in warm mud and feel the heartbeat of the place. Dr. Asha hands you a tiny sensor—no larger than a matchbox."
    show dr_asha_khatri at left:
        zoom 0.7

    dr_asha_khatri "These will log salinity, sediment, and water level. They’re community-run; whoever has training can read the data. Pay for data collection; pay for care. That money keeps the habitat and the jobs."
    show elena_lena_maris at right:
        zoom 0.7

    elena_lena_maris "If we can prove the marsh sequesters carbon and buffers storms, we get more leverage to resist destructive proposals. It’s policy with a sensor on a stick."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "You’ve always made maps powerful, Lena. Now you’re making mud persuasive."
    "Jonah Reyes’s hand finds yours, mud dark under both nails. It’s small and immediate—an anchor against the abstract largesse Iris sometimes carries. His laugh makes you breathe easier."
    "Iris Valence walks the line with a clipboard. She kneels, surprising you, and touches a sapling like she’s testing whether it’s real."
    hide dr_asha_khatri
    show iris_valence at left:
        zoom 0.7

    iris_valence "We’ll match seed funding to employment milestones. If monitoring shows sustained recovery, my firm will divert more funds into community-owned infrastructure, no strings attached."
    "You look at her, searching for the edge you used to see—something that would make you distrust every glint. Instead, you find a willingness to bind corporate muscle to community governance; it's not repentance, but it's leverage."

    elena_lena_maris "We hold you to that. Binding funds, community oversight, public reporting. And any future development must include community seats with decisive votes."

    iris_valence "Agreed. Put the clause in the charter."
    "You watch volunteers plant, backhoe-soil crumbling into new life, and for a long moment you let the tide of small actions swell into a sense of repair."
    # [Scene: Reconstruction Boardwalk | Evening]
    hide elena_lena_maris
    hide jonah_reyes
    hide iris_valence

    scene bg ch15_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Hammers, laughter, soft conversation; the tide breathing steady and slow]
    # play music "music_placeholder"  # [Music: Full orchestral warmth, a rising motif resolving into a steady, hopeful cadence]
    "The evening meeting is not celebratory—there’s a sober edge—but the room is full. People who were quiet for weeks speak up. Parents trade contact information. Rosie passes around bowls of stew. Councilors sign the first page"
    "of the charter; you stand too because your hands are full of everything that happened that day."

    "Mayor" "Brinehaven agrees to this plan: targeted, voluntary relocations with guaranteed rights to return, escrowed funding governed by a community board, job retraining programs, and monitored habitat restoration to tie protections to measurable ecological recovery."
    "There is a ripple of something like relief. Not triumph, but the lightening that follows a shared load."
    "You look at each face: Dr. Asha, who taught your hands to trust data; Jonah Reyes, who laughs despite everything; Iris Valence, her jaw softening, the corporate cuff left open like an offering; Marco, eyes red"
    "but steady; Rosie, hands dusted with paint and fish oil. Their presence is the proof—this was not a unilateral shove into safety but a negotiated passage."
    show elena_lena_maris at left:
        zoom 0.7

    elena_lena_maris "We lose things; we will. We also keep things. We keep rights. We keep jobs tied to care of the place. We do not let this become a land grab in a new coat. That’s the promise."
    "A woman in the back stands, her voice woven from salt and patience."

    "Resident" "And if someone abuses the escrow? If a contractor tries to weasel funds?"
    show iris_valence at right:
        zoom 0.7

    iris_valence "We have penalties, public audits, and a clause that returns funds if milestones fail. The charter is public. The monitoring data is open-sourced."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "And the town holds the seats. If anyone tries to steal back control, you can vote them out. This isn't a one-time bandage. It’s the beginnings of governance."
    "You feel the rising arc of the room—the tiny, shared faith that institutions can be shaped by the people they serve. It’s not naive to hope when you’ve built the scaffolding for accountability."
    hide elena_lena_maris
    show marco_maris at left:
        zoom 0.7

    marco_maris "My dad used to say the sea’s a thief and a giver. Today we made a ledger. We marked who owes what—to the sea, to each other. I still hate that we have to leave for a while. But I can see a return that's worth it."
    "There is applause—not wild, but whole. It sounds like a tide coming in that will not drown. It sounds like work that will hold."
    "You take Jonah Reyes’s hand—he squeezes—and you look out the window at the boardwalk you first learned to repair with your father. Lantern light pools on the planks like small promises."
    hide iris_valence
    show elena_lena_maris at right:
        zoom 0.7

    elena_lena_maris "This is not the victory we dreamt of when the town was whole. It is better: an organized, humane plan that preserves rights and dignity. We built a path—messy, legal, human—that lets people leave without losing the right to return."
    hide jonah_reyes
    hide marco_maris
    hide elena_lena_maris

    scene bg ch15_f99e88_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A single gull calls and then is quiet]
    # play music "music_placeholder"  # [Music: The warm motif resolves and lingers—a quiet, honest chord of hope]
    "You stand in a place where loss has been acknowledged and translated into protection. The plan is imperfect; someone will grieve, and someone will be angry. But there is a scaffolding now—community seats with votes, escrowed"
    "funds, paid roles in habitat monitoring, and retraining that redraws livelihoods rather than erasing them."
    "You tuck your sketchbook back into your jacket. Your hands are a little scraped; your heart is a little raw. Yet when you breathe in, the salt air seems less like an accusation and more like a ledger you helped balance."

    scene bg ch15_f99e88_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    scene bg ch15_f99e88_7 at full_bg
    "THE END"
    # [GAME END]
    return
