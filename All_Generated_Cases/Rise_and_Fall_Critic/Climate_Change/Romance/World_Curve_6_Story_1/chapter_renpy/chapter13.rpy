label chapter13:

    # [Scene: Old Shipyard | Early morning, after the surge]

    scene bg ch13_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the slow creak of settling beams, water lapping against warped decking]
    # play music "music_placeholder"  # [Music: Low, mournful cello with sparse piano taps]
    "You step off the boardwalk and onto the gritty shoulder of the Old Shipyard. The air is close with salt and a metallic tang that makes your throat raw. Mud clings to the soles of your"
    "boots like a memory that won't let go. The Polaroid you tucked into your notebook trembles when you slide a finger over its edge; the image inside is trivial—Jonah laughing with a thumbs-up—but the paper feels"
    "like proof you used to know how to steady things."
    "Porches that were once painted in pastel resilience sag now; warped planks gape like opened mouths. Ringed by salt-streaked stairs, a child's plastic bucket half-buried in sludge looks like a fossil of ordinary life. You can"
    "taste rust on your tongue—an imagined flavor, or the actual tang of oxidized nails. Either way, it is bitter."
    "You walk between the ruined thresholds, cataloguing with a planner's reflex: which pilings failed, which berm seams leaked, which parcels were left exposed because the pilot's parcels were isolated islands in an ocean of unreinforced coast."
    "The data you insisted upon sits in your head like a ledger of what you thought was enough—and the shore writes its contrary ledger in broken porches and who is not standing on them anymore."
    "Bento Morais stands near a collapsed railing, his hat pulled low, hands folded as if in prayer or counting. Elena crouches in the doorway of a half-submerged cottage, mud on her knees and a clutch of"
    "leafless stems in her fist. Jonah leans against a ruined mast, eyes rimmed red, silent as a horizon line. Dr. Lian Zhou walks the line with a tablet, her expression precise and exhausted."
    "You open your notebook and let your pen hover. Lists have been a language you trust: steps, measurements, thresholds. Today the lists feel like tallying losses."
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "We ran the monitoring correctly. The models were clean. We documented everything."
    show dr_lian_zhou at right:
        zoom 0.7

    dr_lian_zhou "You did the thing the science required,' she says, voice even. 'We have high-quality time-series—salinity, soil compaction, vegetation survival curves. From a research standpoint, it was a textbook implementation."
    "You want to relax into that sentence—let data be absolution—but your tongue presses against the inside of your cheek. The thing you wanted to prove begins to look like a ledger of omission: temporal scale versus human scale, sample plots versus whole shoreline."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "Textbook. Right. The house I grew up in doesn't care if it's textbook. It cares about wood and the man who swept its steps and the smell of coffee on Sundays."

    mira_kestrel "I know. I know. We tried to make the trial rigorous because—"

    jonah_reyes "Because you thought proof could buy time. Because we needed a story the funders would trust. Because you wanted to be right when you were accused of being late."
    "His voice is not loud, but it has edges. You want to say that you agreed to the slow path because the town deserved evidence it could understand, not because you liked waiting. Instead, you let"
    "your hands empty themselves of the notebook and close around the compass at your throat."

    dr_lian_zhou "The surge's timing was outside modeled percentiles, but still within long-tail projections. The failure sequence shows seams at parcel boundaries—heterogeneous reinforcement created differential pressure points. That is the mechanism."

    "Elena" "We counted seedlings yesterday. Today there are empty trays and a muddy corner where the greenhouse floor buckled. There were families depending on those plantings for the shoreline's next season."
    hide mira_kestrel
    show bento_old_bento_morais at left:
        zoom 0.7

    bento_old_bento_morais "Time and tide ask different questions than lab notebooks, Mira. They ask what you do while the water's coming."
    "Your chest tightens at Bento's words; they are not a rebuke exactly, but the cadence of something older than policy. You think of your father's boat—how it scraped and finally surrendered—and the old brass compass that"
    "belonged to your mother, warm against your skin when you slipped it on in the lab that morning. Guilt is not loud here; it is a slow, rusted thing that eats from the inside out."

    menu:
        "Go to Jonah and stand with him in silence":
            "You cross the mud-slick planks and rest your palm against Jonah's shoulder. He flinches, then lets the weight sit there like a temporary anchor. No words pass; your silence carries apology."
        "Check the ruined porches for salvageable materials":
            "You move through the thresholds, pulling loose boards and salvaging nails. Your hands are busy and practical; the work steadies you, and an old neighbor offers a ghost of a grateful nod."

    # --- merge ---
    "The scene continues after either action."
    # [Scene: The Shipyard | Late morning, central staging area]
    hide dr_lian_zhou
    hide jonah_reyes
    hide bento_old_bento_morais

    scene bg ch13_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Occasional hammer, distant motor of a cleanup pump, murmurs of people sorting salvage]
    # play music "music_placeholder"  # [Music: Sparse strings, a pulsing low note]
    "You arrive at the shipyard and the scale of what was isolated becomes painfully obvious. Where your pilot plots had carefully maintained boundaries—replicated treatments, control strips, monitored roots—lies a quilt of exposure. The neighboring parcels were"
    "not reinforced; they were waiting for a separate grant, for a volunteer day, for the slow accumulation of small acts that, together, would have made a whole. Instead, gaps acted as seams for the surge to"
    "exploit."
    "You see where the sediment bags stopped, a half-meter gap between the last bag and an unfortified stair. The water pushed through that seam like a needle through cloth. You think of statistical significance and then"
    "of the baby’s boot that now hangs from a bent railing, full of green muck."
    "Kai is not here; he had been organizing volunteers and missing seedlings feel like a personal blow to him as well. Elena approaches you, hands raw with where she had tried to peel mud off trays."

    "Elena" "If we'd taken the NGO money, we could've bought more bags, more people to put them in. I know you wanted clean data. But there were neighbors we could have protected immediately."
    show dr_lian_zhou at left:
        zoom 0.7

    dr_lian_zhou "Elena is correct about capacity. Our methodology favored control and repeatability. That is a trade-off. We were not wrong; we were insufficient."
    "You hate the word insufficient because it implies that better would have done it—like there was a version you failed to reach."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "We documented failure modes. We will have learnings for the region, Lian. That's why we made the choice."

    dr_lian_zhou "Yes. Those learnings may prevent future loss elsewhere. But here, they cannot un-sing what the water sang."
    "A neighbor passes with a bucket of salvaged photos. Bento watches the exchange and scratches his jaw."
    show bento_old_bento_morais at center:
        zoom 0.7

    bento_old_bento_morais "They'll tell your papers about sequence and threshold. They'll talk in conferences. Down here, we tell stories to remember who we were. Those two things—papers and stories—do not always hold hands."
    "You think of the meetings, the nights poring over code and curves, the stubborn refusal to let politics dictate methodology. You wanted to protect the town by making decisions that could be held up under scrutiny. You see now that the tide does not pause for scrutiny."

    menu:
        "Argue for immediate expansion into neighboring parcels":
            "You stand up straighter and gesture toward the open shore. Your words are quick and insistent, cataloguing what materials and volunteers would be needed. For a moment energy surges through the crowd; then faces fall as they reckon with exhaustion."
        "Conserve energy and focus on documenting the data—let the science speak":
            "You sink back into the paperwork, poring over logs and timestamps. Your calm professionalism offers structure for those who want to understand, but the others watch you with an expression that is part plea, part accusation."

    # --- merge ---
    "The scene continues after either action."
    # [Scene: Greenhouse Collective | Afternoon, after the cleanup]
    hide dr_lian_zhou
    hide mira_kestrel
    hide bento_old_bento_morais

    scene bg ch13_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The gentle drip of water from a leaky gutter, the creak of a warped door]
    # play music "music_placeholder"  # [Music: A single piano motif, held and unresolved]
    "The greenhouse is quieter than the shipyard. Elena stands amid the wreckage, counting missing trays with a methodical cruelty. Hands that used to coax life into little roots now move through emptiness. You feel each missing seed like a small domestic death."

    "Elena" "We had planned to plant twenty meters of cordgrass this month. That would have connected our pilot to the eastern lot—helped the sediment stabilize. We had the seedlings, barely. But priority was method over momentum."
    "You can hear accusation in her voice; it is not only directed at you, though your name sits between the words like a fulcrum."
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "We didn't refuse help because we don't care. We did it because I thought stronger data could save more people later."

    "Elena" "Save more people later. That's cold comfort when your front step is gone."
    "You reach for an explanation and find only the rhythm of apology forming. You think of Jonah's shuttered eyes and the way Bento's hands have started trembling in the mornings. You try to reconcile the part"
    "of you that trusts evidence with the part that trusted a community to act faster than grant cycles."
    show bento_old_bento_morais at right:
        zoom 0.7

    bento_old_bento_morais "There is a sort of pride in being right. It tastes like ash. We must be right for the wrong reasons sometimes—only to find the reasons aren't worth the scale of what we lose."
    "Dr. Lian Zhou kneels to collect a flopped seed tray, her fingers moving with the same precise care she used in data annotation."
    show dr_lian_zhou at center:
        zoom 0.7

    dr_lian_zhou "We will publish. We'll show how parcel heterogeneity led to failure propagation. Grants may follow, policy discussions may change. But that is a future that is built on the bodies of this town's now."
    "You, for the first time since the meeting that led to this pilot, let yourself imagine a point-of-view file on a conference table: your name, the pilot's clean graphs, a polite applause. The image curdles in your mind."
    "Jonah stands in the doorway, watching you work. He crosses the room slowly and lays a mud-caked hand over the compass at your throat. His fingers are callused; the touch is an accusation and a benediction."
    hide mira_kestrel
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "Did we ever stop being honest with each other about what would happen if we waited for proofs?"
    hide bento_old_bento_morais
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "No. We tried to make the proof another way of being honest."

    jonah_reyes "Honesty doesn't keep water out."

    mira_kestrel "No. It doesn't."
    "A long silence folds between you—full of things unsaid: blame, fear, exhaustion, the memory of happier mornings where you could imagine fixing things together instead of counting what else the sea would take."

    menu:
        "Tell Jonah you are sorry, explicitly":
            "You say the word out loud, clumsy and human. Jonah closes his eyes and the tightness in his face rearranges. He nods once, and it is both acceptance and the beginning of a distance."
        "Offer to rebuild what you can with him, practical and immediate":
            "You propose a plan—two people, a list of materials, a day of work. Jonah studies you like he's measuring tide height, then gives a small, reluctant agreement. The plan is tiny, but it is something real."

    # --- merge ---
    "The scene continues after either action."
    # [Scene: Old Shipyard Steps | Dusk]
    hide dr_lian_zhou
    hide jonah_reyes
    hide mira_kestrel

    scene bg ch13_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slow retreat of the sea, a hinge creaking, distant conversations turned to the hush of people working late]
    # play music "music_placeholder"  # [Music: A low sustained note that eases into a minor-key lull]
    "Night slides in. You sit on a ruined step with the compass in your palm and your notebook on your knees. The lists you make—what was protected, what failed, what parameters were misestimated—begin as professional instruments. Each line limb-tightens into sentences about trade-offs: rigor vs. reach, repeatability vs. rapid scale."

    "You write" "What we did right:' and the paragraph is clear—methodology, data integrity, clear failure documentation, replicable protocol. Then you write: 'What we failed to do:"
    "Elena's hands are raw from sorting seedlings. Bento sits a few steps below you, his profile a map of old storms. Jonah is nearby, the silhouette of work and refusal both. People move around you, reclaiming"
    "what they can, their sentences small and practical: someone needs plywood to cover a window, someone else needs a roster for who can haul bags tomorrow. There is work to be done, always work to be"
    "done—an exhaustion that is also an endurance."
    "You close your notebook and let the pen fall across the page. Somewhere between the factual and the mournful, a shape forms: a recognition that your choices delivered knowledge at the cost of immediate protection. That trade-off is a moral geometry you will carry as a permanent scar."
    show dr_lian_zhou at left:
        zoom 0.7

    dr_lian_zhou "Mira, the region will look at our dataset. It will inform decisions that could prevent loss at scale. That's not nothing."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Right now, that feels like nothing to the families who soaked through last night."

    dr_lian_zhou "I know. I'm sorry. Our ethics committee will not put that phrase on a slide, but I will live with it without any neat graphs to justify it."
    "Her apology is small and inadequate and honest. It is not the kind that mends porches. It is the kind that sits in the same room as regret."
    "Jonah finally speaks, the words slow and patient as the sea."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "I don't know if what you did is worth it, Mira. I don't know if being right will ever be the same as being kind."
    "You feel the question like a tideline washing your ankles. You could answer with justification—point to models, to downstream lives, to the way knowledge births policy. You could answer with anger or deflection. Instead you press"
    "the compass to your lips and let it be the small, private thing that belongs to your mother and to the town that raised you."

    mira_kestrel "I wanted both. I wanted data and people. I thought the two would meet."

    jonah_reyes "Sometimes they don't."
    "The night deepens. People begin to leave, folding into households to tell stories and count losses and repair and cook what is left. The shipyard's lights flicker like tired stars."
    "You sit for a long time, watching the water reflect a pale moon that does not care for human charts. The lists in your notebook fold into each other; rows of method and rows of grief become the same handwriting."
    "Finally you stand, the weight of the day in your shoulders. You tuck the notebook away and push the compass back beneath your shirt where it presses against your sternum like a small, familiar hurt."
    hide dr_lian_zhou
    show bento_old_bento_morais at left:
        zoom 0.7

    bento_old_bento_morais "We will rebuild parts. We always have. But remember—rebuilding without learning is just more rebuilding, and that's another kind of sorrow."
    "You nod because his sentence is larger than the moment and true. Outside, the tide hushes toward the horizon. Inside you, the tide rearranges the shoreline of what you are willing to carry."
    hide mira_kestrel
    hide jonah_reyes
    hide bento_old_bento_morais

    scene bg ch13_601bcb_5 at full_bg
    # play music "music_placeholder"  # [Music: Cello holds a single, somber bow; then fades slowly]
    "You walk away from the Old Shipyard with the sound of people working in the background and the quiet weight of decisions in your chest. The end of the pilot is not a single event but"
    "a long, small unraveling—soft, inexorable, and absolute in its quietness. You have your data. You have your lists. You have the town, altered."

    scene bg ch13_601bcb_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    scene bg ch13_601bcb_7 at full_bg
    "THE END"
    # [GAME END]
    return
