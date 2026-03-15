label chapter12:

    # [Scene: Rooftop Greenhouse & Community Rooftop | Dusk]

    scene bg ch10_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, anticipatory cello with a distant, pulsing synth]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, a faint municipal siren far off, paper rustling]
    "You are perched on the edge of the rooftop, your elbows on your knees, the notebook heavy and quiet inside your bag. The hybrid council has formed: small modules plus accelerated restoration, decided by votes and"
    "handshakes. The agreement felt like a thin bridge built between cliffs—necessary, imperfect, holding for now."
    "But 'holding' is different from 'finished.' Tonight the bridge groans."
    "Mayor Isla Cortez paces near the string lights, tablet in hand. Her jaw is tight; the municipal patch on her sleeve creases with each step. Dr. Kavir Singh stands by the herb beds, palms folded, eyes"
    "on a sequence of tide charts pinned to the railing. Jun leans against a post, hands stained with soil, muttering to themselves as they scroll through deployment maps."
    "Mateo Hale is quiet at the far end, shoulders braced, looking out at the harbor line as if he can read plans there. Sora Lin is closer to you—paint-spattered sleeve tucked into their palm—and their expression is a pile of friction and hope, impossible to read all at once."
    "You inhale. The rooftop smells of damp earth, citrus from Elena's parcel still warm in your bag, and the metallic bite of incoming rain. Every smell tethers you to the town you want to save and to the mess of politics that will make or break it."
    show mayor_isla_cortez at left:
        zoom 0.7

    mayor_isla_cortez "The council's consensus was tentative, Aria. We said 'pilot'—we need proof. We need receipts and a timeline before I can sign reimbursements."
    "You hear the careful blue of her voice—practical, public-facing—but underneath is the electric hum of pressure."
    show aria_navarro at right:
        zoom 0.7

    aria_navarro "We can produce the timeline. Jun's sensors are almost calibrated, Kavir has the baseline data... we only need the first deployments in the water to show progress."
    show dr_kavir_singh at center:
        zoom 0.7

    dr_kavir_singh "Progress is not just deployment, Aria. It's measured outcomes. We have two weeks of tide windows left before the seasonal storms change. We should be explicit about endpoints."
    "Mayor Isla Cortez sighs. 'Two weeks is a short clock. The auditors want clarity on spending. They asked for contingency plans twenty-four hours ago.'"
    hide mayor_isla_cortez
    show jun_park at left:
        zoom 0.7

    jun_park "Contingency plans are in my head and on a USB back at the lab. The upload stalled because the backup server's router fried last week."
    "The rooftop air tightens around that last line. You feel the page of your notebook shift under your palm."

    menu:
        "Step closer and insist on a live upload now":
            "You stand, knees stiff, and call across the rooftop—your voice firm. Jun looks up, startled, fingers already moving. The team arranges a hurried relay to the lab's backup terminal."
        "Stay where you are and listen for the subtext":
            "You keep your seat, letting the argument unfold like a soft knot. You watch faces instead of data: Sora Lin's jaw, Mateo Hale's hands. The silence teaches you the shape of what everyone is afraid to say."

    # --- merge ---
    "..."
    "The practicalities begin to spit sparks: receipts, auditors, servers. It is granular and bureaucratic—and it eats time the way the tide eats the quay."
    "Mayor Isla Cortez folds her arms. 'If we don't meet the auditors' benchmarks, they freeze funds. If funds freeze, the modules don't move, the seedlings don't get the sediment trays—people will start to talk about relocation.'"
    "Sora Lin steps forward, voice a little rough. 'Then we don't wait for them to 'talk.' We show up. We plant. We make them look at what they're trying to lock down.'"
    "Mateo Hale breathes out, a controlled sound. 'You can't just—planting is fine, but if a surge hits and we haven't installed the first levee modules where the currents strip the new sediment, we waste effort. We waste lives.'"
    "The debate spirals into tension you know too well: urgency versus process, spectacle versus measured intervention. You can hear the town in every syllable, every hold on a word."

    aria_navarro "We need both to happen, or neither will. The council was supposed to enable both."
    hide aria_navarro
    show mayor_isla_cortez at right:
        zoom 0.7

    mayor_isla_cortez "The council is splintering. Meetings across three committees, midnight calls, someone leaked budget drafts to a paper in the city. The auditors smelled it and moved in. They call for a formal review, effective immediately."
    "A hollow wind stabs the rooftop; a stray bulb flickers."

    dr_kavir_singh "Auditors can be reasonable—if we give them clarity. If we give them a clear chain of custody for funds and an initial deployment schedule, we can get an exception for a six-week pilot."
    hide dr_kavir_singh
    show sora_lin at center:
        zoom 0.7

    sora_lin "A six-week pilot that leaves us waiting for paperwork while the water rises? I won't stand by and make the town pawns for a delay."
    hide jun_park
    show mateo_hale at left:
        zoom 0.7

    mateo_hale "We need someone to cut through the choke points. Someone with the authority to move money now."
    "You study Mayor Isla Cortez's face. She is reading the same ledger of risk that all of you are, but the ledger includes political lines you do not hold."

    mayor_isla_cortez "If you—if someone—present a motion tonight to give me temporary allocation power, I can authorize limited disbursements for emergency deployment."
    "The words land like stones. Somewhere down by the harbor, an engine coughs and the sound is oddly loud."
    hide mayor_isla_cortez
    show aria_navarro at right:
        zoom 0.7

    aria_navarro "Temporary? For how long?"
    hide sora_lin
    show mayor_isla_cortez at center:
        zoom 0.7

    mayor_isla_cortez "Long enough to launch the first modules and fund the initial restoration supplies. Short enough to satisfy council oversight bodies on paper."
    "Sora Lin's fingers curl. 'Short enough for what? For you to sign and then them to come in and bulldoze everything three years later?'"
    "Mateo Hale's jaw tightens. 'We don't have three years.'"
    "Your chest feels like low tide—exposed, full of residue. The rooftop lights throw everyone into silhouette. The conversation loops and nothing is decided."
    # [Scene: The Tidal Research Lab (The Tidal Lab) | Night]
    hide mateo_hale
    hide aria_navarro
    hide mayor_isla_cortez

    scene bg ch10_453e40_2 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano chords with a low rumble]
    # play sound "sfx_placeholder"  # [Sound: The steady ping of incoming emails, a far-off thunderroll, the slosh of water against the lab apron]
    "You move from rooftop to lab because this is where the pieces sit—the sensors, the data, the raw things that count in a grant audit and on the ground. The lab smells like warm plastic, wet"
    "cloth, and coffee gone cold. Fluorescent lights hum. Jun's fingers are smeared with solder; they're talking to an automated logger with the kind of casual profanity reserved for beloved, malfunctioning things."
    show jun_park at left:
        zoom 0.7

    jun_park "If the backup doesn't come online, the auditors will want to see who had access to the keys. Who authorized purchases, who signed off on the volunteer payrolls—"
    show dr_kavir_singh at right:
        zoom 0.7

    dr_kavir_singh "Which is why we need chain-of-custody statements and a notarized ledger. Mateo Hale, did the procurement forms go to municipal procurement?"
    show mateo_hale at center:
        zoom 0.7

    mateo_hale "They went to procurement. The problem is procurement won't act fast enough without a policy exception. I'm not asking for a blank check; I'm asking for an exception to the normal timeline."
    hide jun_park
    show aria_navarro at left:
        zoom 0.7

    aria_navarro "Isla suggested temporary allocation authority, remember? It's a wrench, but it can unstick things."

    dr_kavir_singh "A wrench that might strip threads. Centralization solves speed but concentrates blame."

    mateo_hale "Someone will be on the hook if it fails. I know that. I also know what a storm can do in a night."
    "You close your eyes and imagine the sound of a storm flattening the quay—a living thing with teeth. The lab's monitors blink like a heartbeat. The rain outside moves from a whisper to a thin drum."

    menu:
        "Call Mateo Hale and pull him off-site to coordinate the deploy schedule":
            "You hit call. Mateo Hale's voice is solid but tight; he agrees to head straight to the construction site with a skeleton crew. You feel the small, sharp relief of action."
        "Text Sora Lin and ask them to mobilize planting crews at the reclamation site":
            "You type to Sora Lin. A flurry of green-heart emojis and three quick messages arrives: they already have a list and a van. Their optimism is electric, and for a second you taste hope that steadies your hands."

    # --- merge ---
    "..."
    "The lab phones light up with the auditors again. An official voice says the review will be comprehensive. You feel a cold paralyze the room—the old administrative dread that can undo months of sweat with a single stamp."

    dr_kavir_singh "We can provide documentation. We can show outcomes. But if the first storm of the season finds us fragmented, it won't matter how clean our spreadsheets are."
    hide dr_kavir_singh
    show jun_park at right:
        zoom 0.7

    jun_park "The community will remember that we floundered."
    "You look at everyone. Mateo Hale's eyes are a blueprint of worry. Sora Lin's expression is a drumbeat: go. Dr. Kavir Singh's calm is an anchor. Jun looks like they need a nap and a win."

    aria_navarro "We won't let it flounder."
    "The words are a promise you make in a place of flickering monitors and wet floors. Promises are small things until they're not."
    # [Scene: The Mangrove Reclamation Site | Pre-dawn, before the storm]
    hide mateo_hale
    hide aria_navarro
    hide jun_park

    scene bg ch10_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: A single violin line, slow and mournful]
    # play sound "sfx_placeholder"  # [Sound: Mud sucking at boots, the slap of tarpaulin, a generator's distant growl]
    "Volunteers are here because they believed in the council's hybrid promise. The saplings tremble in plastic trays. The sediment trays are stacked but some are missing anchors; the modular blocks that should have been placed near"
    "the living shoreline are still boxed on the quay because procurement paused after the audit notice."
    show elena_navarro at left:
        zoom 0.7

    elena_navarro "We can plant the little ones, niña. We can keep the roots fed. But if the next surge takes the foundation, it will be harder."
    "You smell wet fish and lemon oil from her hair. The smell roots you. Around you, a dozen faces are open and tired."
    "Mateo Hale arrives with two municipal workers, his jacket damp. He moves with a deliberate efficiency, checking placements, measuring lines."
    show mateo_hale at right:
        zoom 0.7

    mateo_hale "We can set temporary anchors—sacrificial—but they'll need sandbags and a fast tide window. If we delay another day, the window closes."
    "Sora Lin appears with a van of volunteers, paint on their forearms, a grin that cuts like a blade. They slam the van door and start distributing shovels. 'We can cover the anchors with woven mats and plant at the same time,' they call. 'We can be fast.'"
    "The sky has grown heavy enough that the horizon looks like a held breath. Someone on a radio says 'tropical depression' and everyone's stomach drops."
    show dr_kavir_singh at center:
        zoom 0.7

    dr_kavir_singh "If we do this ad hoc, we expose the seedlings to early scour. If we centralize, we risk alienating volunteers."
    "The voices layer: fear, strategy, exhaustion."
    "You plant a sapling because action momentarily quiets the worry. Your hands are cold with mud; the roots feel like small, demanding organisms of hope. Planting is a ritual and a protest and a necessary labor."
    hide elena_navarro
    show aria_navarro at left:
        zoom 0.7

    aria_navarro "If we push for a centralized surge, we could get modules seeded fast and place sediment barriers before the surge. But what do we lose if power is centralized? What do we risk to the communal momentum Sora Lin has built?"
    hide mateo_hale
    show sora_lin at right:
        zoom 0.7

    sora_lin "We don't give them our story to hold. We do this together."
    hide dr_kavir_singh
    show mateo_hale at center:
        zoom 0.7

    mateo_hale "We don't have an extra season to test community processes. The town needs measurable protections now."
    "The radio crackles. 'Watch—tide forecast updated. Storm intensifies sooner than expected.'"
    "The words punch the air."
    hide aria_navarro
    show jun_park at left:
        zoom 0.7

    jun_park "If the tide rises tonight, the unanchored sediment trays will wash. The seedlings will move with the water. We will lose biomass and trust in the same night."
    "Mayor Isla Cortez's call comes through on a satellite line. Her voice is thin with decision-making. 'I can motion for temporary allocation authority. It will concentrate power, but it will get things moving. I need Aria to stand with me.'"
    "You feel the weight of that ask like a stone in your chest. Temporary authority sounds like a good tool in a toolbox that is also a trap. You remember the rooftop lights, the auditors' voices, Jun's solder-stained hands."
    "Sora Lin squares their shoulders, mud on their knuckles. Mateo Hale's eyes are a flat, hard horizon."
    "The rain begins in earnest: it stripes the air, salt and fresh water braided together. The ground smells of iron and the quiet pressure of coming disaster."
    "You are the hinge. The council falters into argument. Volunteers look to you. The mayor calls for your support. Dr. Kavir asks for evidence of oversight. Mateo asks for speed. Sora asks for solidarity."
    "You can hear the town in the sound of rain on tarpaulin, in the ache in Elena's face, in Jun's whispered 'please,' where all the data meets all the need."
    "Your chest tightens. You think of the notebook warm in its bag, the list of tasks, the projections sketched in half-sleep. You think of the seedlings in your hands—small, living proof."
    "The choices before you are not clean. They cut and bend and demand payment."
    "You inhale the wet air and prepare to speak."
    # play music "music_placeholder"  # [Music: Tense low hum]
    # play sound "sfx_placeholder"  # [Sound: Thunder close; the storm drum increases]

    menu:
        "Push for emergency centralization—give the mayor temporary direct control to allocate resources quickly.":
            jump chapter13
        "Insist the council continue but enforce strict operational protocols and rapid volunteer mobilization.":
            jump chapter14
        "Stage a dramatic public reinstallation—combine a visible engineering patch with a mass planting day to restore confidence.":
            jump chapter13
    return
