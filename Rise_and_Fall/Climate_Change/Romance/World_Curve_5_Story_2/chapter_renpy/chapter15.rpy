label chapter15:

    # [Scene: Pier (packing trucks) | Morning]

    scene bg ch15_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slap of canvas, the roll of a hand truck, distant gulls calling. A radio murmurs a logistics channel.]
    # play music "music_placeholder"  # [Music: Warm strings, steady but buoyant]
    "You stand at the mouth of the pier with a clipboard that feels heavier than paper. Your jacket is damp where the spray has settled; your compass pendant is cool against your throat. Boxes labeled 'Relief"
    "— Return Rights Enclosed' sit beside crates of donated tools and seedlings. People you love move like tide lines around you—Rosie barking gentle orders, Marco lugging a generator like it's the heaviest thing and the most"
    "important, Jonah threading rope through a tarp with fingers that know where to pull."
    "You inhale. The smell is a complex tide: salt, wet cardboard, the faint smoke from a breakfast grill. You can taste the plan—the grind of policy and the grit of human labor combined—and it tastes like work that might save people."

    "Rosie" "Lena—you're pale. Sit for two minutes. Eat. We need your head sharp."
    show elena_lena_maris at left:
        zoom 0.7

    elena_lena_maris "Can't. Someone's got to sign the manifests when the van rolls out, and Asha's flagged three families with priority needs."
    "Rosie: (softening) 'And you'll stand up straight when you do it. Promise?'"

    elena_lena_maris "I promise."
    "Jonah Reyes looks up and meets your eyes. There's that familiar easy steadiness, but underneath it: an edge—worry sharpened into focus. He hands you a thick manifest."
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "We have two family units heading to the temporary center. Transport's covered. Training stipends are in the package. I double-checked the clause on guaranteed return—it's in there, legally binding."

    elena_lena_maris "Good. Make sure the clause references community governance on timing and habitat impact. People need to know this isn't a one-way street."

    jonah_reyes "It isn't.' (He pauses.) 'But they need assurances: fair compensation while away, retraining, storage for boats and tools. We'll make them whole enough to come back."

    elena_lena_maris "Not 'whole'—different. We can't put their childhoods back together. But we can insure their rights, their skills, and their dignity."
    "Jonah Reyes: (a small, rueful smile) 'Never ask you for poetry when there's a contract to sign.'"
    "You both laugh, small and brittle, then steadier."

    menu:
        "Help Jonah secure the tarps":
            "You kneel beside him, the rope biting slightly into your palm. His fingers brush yours for a fraction of a second and he mutters a curse about cheap canvas. It grounds you both—hands in the same tangle of action."
        "Call the relocation center to confirm intake":
            "You step aside and call. A warm voice answers; you run through names, allergies, and a promise over data lines. Each confirmation is a small, deliberate mercy."

    # --- merge ---
    "Continue to Scene: Relocation Center (converted school gym) | Midday"
    # [Scene: Relocation Center (converted school gym) | Midday]
    hide elena_lena_maris
    hide jonah_reyes

    scene bg ch15_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmured conversations, a volunteer passing soup, a child chasing a foam ball.]
    # play music "music_placeholder"  # [Music: Quiet piano motif, hopeful, patient]
    "Inside the gym, faces are close and immediate. You move from cluster to cluster, answering questions with a practiced tenderness. A mother presses a worn photograph into your hand; a fisherman asks in halting voice if he'll be allowed to mend his nets when he comes back."
    "You kneel so your eyes are level with the child's drawing—a sun half-cut by a wave; the waves are colored green at the bottom, the house bright orange. You look at the mother."
    show elena_lena_maris at left:
        zoom 0.7

    elena_lena_maris "We negotiated a clause. Temporary relocation includes storage for tools and a right to return when the monitoring thresholds are met and community governance approves restoration efforts. There will be retraining payments and a priority list for rebuild materials."
    "Mother: (tears, then a laugh that is almost disbelief) 'You promise?'"

    elena_lena_maris "We promise in paper and in people. I'm asking everyone here to hold me accountable."
    "Dr. Asha Khatri arrives with a tablet of model visualizations—graphs of marsh health, eelgrass recovery projections, and timelines for staged protections."
    show dr_asha_khatri at right:
        zoom 0.7

    dr_asha_khatri "The targeted relocations reduce exposure for eighty percent of the risk-weighted population. If we create the living-shoreline buffers and commit to habitat monitoring for five years, the model shows higher probability of safe returns than a blanket relocation."

    elena_lena_maris "Five years is a long time."

    dr_asha_khatri "It is. But it's bounded and written into the agreement. And it buys magnesium time—time to let the marsh heal enough to support livelihoods again."
    "Marco stands to the side, hands jammed in his hoodie, jaw working. He meets your eyes with a raw, immediate question."
    show marco_maris at center:
        zoom 0.7

    marco_maris "You're really doing this? Letting people go now so they can maybe come back when the water behaves? They're gonna lose years. My mates can't wait. They need work."

    elena_lena_maris "I know. That's why we tied retraining and guaranteed redeployment into the plan. Some will stay—where it's safe—and new jobs in restoration and retrofit work will be prioritized locally."
    "Marco: (bitter) 'That's not the same as fishing.'"

    elena_lena_maris "It isn't. It's part of keeping the town—your town—alive. You can choose to be here when the marsh is seeding again, even if the shape is different. We didn't choose this; but we can shape how it happens."
    "Marco: (a long exhale) 'If you say it's a fight worth having, then I'll help. I'll roster people for the planting teams.'"
    "Elena 'Lena' Maris: (relief like a small tidepull) 'Bring the rest of them. Bring everyone you can.'"

    menu:
        "Stay to help a family fill the storage forms":
            "You sit with the old man at the table and fill forms by hand, writing boat serials and tool lists. His fingers tremble when he signs; you press the pen into his hand so he knows his mark is held, honored."
        "Head back to the pier to check the shipment of seedlings":
            "You rush out into the light, inhaling the tang of algae and earth. Jonah's loading sedges into crates; volunteers laugh as mud spats their boots. The seedlings look fragile and miraculous."

    # --- merge ---
    "Continue to Scene: Marsh / Living Shoreline Site | Late Afternoon"
    # [Scene: Marsh / Living Shoreline Site | Late Afternoon]
    hide elena_lena_maris
    hide dr_asha_khatri
    hide marco_maris

    scene bg ch15_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft suction of boots in mud, a chorus of insect wings, a distant motor as a drone circles and hums.]
    # play music "music_placeholder"  # [Music: A rising string motif; warm, building]
    "You stand at the edge of the marsh, watching hands press roots into place. The mud pulls at your boots; the salt stings the skin along your knuckles. Jonah is beside you, his hair tied back, sleeves rolled to the elbow. He hands you a sapling."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "Here. Plant it like you mean it."
    "Elena 'Lena' Maris: (burying roots, feeling the give and the hold) 'We planted more than willows today. We planted trust. Contracts help—funding, rights, lawyers—but this is where the town signs its own name on the recovery.'"

    jonah_reyes "There are still families who feel betrayed. Some of them are your neighbors, Lena. I don't want this to break us."
    show elena_lena_maris at right:
        zoom 0.7

    elena_lena_maris "It may. Some things will be broken and some will be rebuilt. But the point is that people keep the choice and the promise to come back. That's not nothing."

    jonah_reyes "Not nothing. And not everything.' (He leans closer.) 'Are you okay with that trade?"
    "Elena 'Lena' Maris: (you've held this question inside for nights) 'I am. It's the smallest humane path. We are choosing the least erasure.'"
    "He rests his palm against the small of your back for a second—practical, steady—and then returns to arranging coir logs. There is tenderness in the motion; care as a tool."
    "Dr. Asha Khatri stops by, wiping mud on her sleeve like a ritual."
    show dr_asha_khatri at center:
        zoom 0.7

    dr_asha_khatri "The drone feed shows eelgrass beds further out holding. If we can keep nutrient loads down, and if the shoreline doesn't get hammered by another surge this season, the early indicators are good. We can trigger step-one of the return plan in eighteen months, given monitoring compliance."

    elena_lena_maris "Eighteen months is a start. We'll make the monitoring community-run—training locals to take samples, host readings on the boardwalk we rebuild."
    "Dr. Asha Khatri: (a smile that is all stubborn tenderness) 'Exactly. Science is data—yes—but it's also people with nets and notebooks and stubbornness. We have both.'"
    # play sound "sfx_placeholder"  # [Sound: Distant applause. A truck horn. The tide sighs against the woven coir as if in agreement.]
    # [Scene: Reconstruction Boardwalk (early evening) | Golden Hour]
    hide jonah_reyes
    hide elena_lena_maris
    hide dr_asha_khatri

    scene bg ch15_3be532_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft conversation, the creak of boards settling, kids playing with a cardboard boat.]
    # play music "music_placeholder"  # [Music: The strings resolve into a warm, major key. A single trumpet joins—bright, hopeful.]
    "You walk the boardwalk slowly, feeling the give and the new bolts underfoot. The view of the marsh has changed: lines of green hold into the water, and the first planted willows cast neat shadows. There"
    "is loss—houses marked with tags, familiar roofs absent—but there is also an architecture emerging: a mixed landscape of human care and natural barrier."
    "Iris Valence stands near the far rail, coat off, sleeves rolled. Her hair is still impeccable; her gaze is sharper than the breeze. She watches the town with an unreadable expression."
    show iris_valence at left:
        zoom 0.7

    iris_valence "You did good work lining up the legal language. The fund closures happen quicker when someone local stands as guarantor."
    show elena_lena_maris at right:
        zoom 0.7

    elena_lena_maris "I couldn't have done it without you on the funding end. Nor without Jonah on the field. This plan—' (you sweep your hand toward the marsh and the boardwalk) '—is stitched together with too many hands to claim ownership."
    "Iris Valence: (a small, almost-exact smile) 'We make a better argument together than apart.'"
    "Elena 'Lena' Maris: (the memory of past university debates and a softer, earlier closeness flickers) 'You make a better argument, yes. I hope the town makes a better life for it.'"

    iris_valence "They will, if we keep transparency. If Valence is accountable to the community board for expenditures and if re-entry is a community decision, not a corporate timeline."
    "Elena 'Lena' Maris: (nodding) 'That accountability has to be ironclad. No loopholes. No shiny incentives to forget the people.'"

    iris_valence "Agreed."
    "Jonah Reyes walks up behind you and slides his hand into yours, fingers curling in a familiar fit. It's not theatrical; it is an unspoken pact."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "You said you'd hold me to the truth of it."

    elena_lena_maris "And you said you'd hold me to the town."

    jonah_reyes "We'll keep each other honest."
    "Marco, leaning on a repaired plank near the children, calls out with a grin that is almost sheepish."
    hide iris_valence
    show marco_maris at left:
        zoom 0.7

    marco_maris "Okay, everyone! After we plant the last batch tomorrow, there's a big pot of coffee and someone claimed to have Rosie’s famous fried fish."
    "Rosie: (from the crowd) 'Whoever said that better be ready to wash dishes! But yes—fish for all.'"
    "Laughter threads through the group like rope."
    "You look at the people gathered—their hands, their cheeks weathered, their smiles small and fierce. They are tired and alive. They are not what they were, but neither are they only a memory."
    "You feel the pulse of something like triumph—not unqualified, but steady. You made a choice that cost and saved in unequal measures. You brokered a plan that pulled people out of immediate danger while building a"
    "bridge for return. Some families moved; some stayed; most of you are committed to monitoring, retraining, and a shared governance structure that will decide when, and whether, homes are reoccupied."
    "You breathe in the salt and the woodsmoke. The compass pendant at your throat warms with your heartbeat. Jonah squeezes your fingers."

    jonah_reyes "Whatever comes next, we do it with them."

    elena_lena_maris "Yes. With them."
    # play music "music_placeholder"  # [Music: The warm motif swells, then settles into a single, hopeful note that hangs in the air like a held promise.]
    "You stand on the boardwalk at dusk, watching trucks roll away one by one—some carrying families, others carrying seedlings and tools destined to return with those who will come back. The town hums with quiet, coordinated"
    "motion. Children call to each other. Volunteers swap tools and stories. You feel the weight of the decision you helped shape—its cruelty in some parts, its mercy in others—and you accept its necessary imbalance because it"
    "was made with care, with teeth, with legal muscle and local will."
    "Iris watches you for a beat longer, then nods, a motion that says: this will be scrutinized—and you will be ready."
    "Marco lifts a hand and gives a small, formal salute, then a grin. Rosie bounces over and presses a thermos into your hands."

    "Rosie" "You've earned this. Drink."
    "You raise the thermos and drink the hot, bitter coffee like a benediction. Your mouth tastes like salt and future work."
    "You look west as the sun slides down, painting the marsh in gold. The shoreline you've chosen—part human scaffolding, part living system—stands where once there was only threat. It is not perfect. It does not erase grief. But it is a plan that keeps people in the story."

    "You tuck your sketchbook into your jacket. Inside, one of your shoreline cross-sections has a new annotation" "Return Rights + Community Monitoring = Stewardship."
    "Jonah leans close, voice low, almost a confession:"

    jonah_reyes "You ever imagine we'd be here like this? Mending a place instead of moving on?"
    "Elena 'Lena' Maris: (softly) 'I always imagined we'd be somewhere messy. I didn't expect to feel this…possible.'"

    jonah_reyes "Possible is good."
    "You look at the faces around you—Rosie, Marco, Asha kneeling to check a sample, Iris speaking quietly into her earpiece—and feel the rising tone of the day settle into something you can live with: a compromise that hums with care."
    hide elena_lena_maris
    hide jonah_reyes
    hide marco_maris

    scene bg ch15_3be532_5 at full_bg
    # play music "music_placeholder"  # [Music: Warm chord resolves and lingers]
    "You have brokered a plan that is brutal in some of its asks but designed to honor rights, to keep return possible, to rout money and training into the people who will steward the place back"
    "to life. Tonight: beds set, meals ready, saplings bunched and labeled. The next morning: a roster of volunteers, a schedule of tests, a community board convening to oversee expenditures."
    "You close your eyes for a second and let the noise of the pier—the creak, the laughter, the lullaby of tide—wash over you. You do not have all the answers. You have, instead, a living project"
    "and people who have agreed to hold it together. That will have to be enough."

    scene bg ch15_3be532_6 at full_bg
    # play music "music_placeholder"  # [Music: A single, hopeful note hangs a moment, then fades]

    scene bg ch15_3be532_7 at full_bg
    "THE END"
    # [GAME END]
    return
