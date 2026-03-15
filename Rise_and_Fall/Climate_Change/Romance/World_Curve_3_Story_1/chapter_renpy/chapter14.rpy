label chapter14:

    # [Scene: Town Hall Plaza | Night]

    scene bg ch14_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant chants, the low thrum of pumps, a cluster of raised voices fading into the rain]
    # play music "music_placeholder"  # [Music: Quiet, insistent piano—soft major chords that refuse to resolve]
    "You remember the exact taste of that night: metallic on your tongue, like a coin dropped into brackish water. The folded printout Claire handed you burns in your memory the way a decision does when it"
    "finally settles into your hands. You stood, and you said the words in the council like a stone thrown into the harbor—ripples you couldn't pull back."
    "The chamber fractured. Elena's team rose on a tide of legalese; microphones buzzed; a council clerk's throat cleared so many times it echoed. Outside, someone chanted a rhythm that sounded like a distant gull."
    "Claire's hand is on the packet again now—hers trembles just enough for you to notice. She keeps her voice low, practical."
    show dr_claire_hsu at left:
        zoom 0.7

    dr_claire_hsu "We did what we had to. The models—(they're unstable; they understate failure modes when you blind them to localized sediment flux). You forced the variables into light."
    "You say nothing at first. Words rankle differently when they're public and permanent."
    show mara_solano at right:
        zoom 0.7

    mara_solano "We bought time, or we bought chaos.' (You let the sentence hang, tasting both possibilities.) 'Which is it, Claire?"

    dr_claire_hsu "Both. The review will be surgical. It will take months. Elena's firm will scream. They'll file for injunctions. They will make this about you, about ethics, about process. We'll need every bit of scientific rigor and every legal contact we can scrape together."
    "Claire's eyes find yours—a weary, steady alignment that tells you what she already knows: this is not purely science anymore. It's survival and stories and reputations."
    hide dr_claire_hsu
    hide mara_solano

    scene bg ch14_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A reporter's camera shutter; a canned PR statement being dictated over a phone]
    "You look toward the doorway. Jonah stands there, drenched, his red bandana darkened by rain, his amber eyes—tired, yes, but steady. For a moment his face is a map of the months ahead: worry lines sketched"
    "into the corners of his smile. He steps into the chamber like someone stepping onto a small boat in rough water."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "You did what you had to, Mara—(you know that). But this isn't just on you. We do this together."
    "Mara Solano: (You inhale rain-quick air.) 'I don't get to say whether it was right or not yet. Only whether I could live with myself if I didn't try.'"

    jonah_reyes "Then we live with the trying. We'll take the heat. We'll stand at market tables and tell the truth. We'll patch roofs and feed people and get lawyers and—' (his voice tightens) '—and we'll make sure the town can still be lived in after all this."
    "His confidence is not a cure; it is a commitment. You feel it in the way his fingers find yours at the hem of your jacket—brief, grounding."

    menu:
        "Call Jonah now and tell him to get the coop moving":
            "You pull out your cracked smartwatch and thumb Jonah's name. He answers on the second ring, breathless with rain and ready with a plan: 'Market tonight. Bring the maps.' His voice steadies something in you."
        "Walk the boardwalk alone to see what people are saying":
            "You move into the rain, toward the old market boardwalk. The neon reflections bite at the puddles; vendors shout rumors and reassurances. A woman folds up her awning and hands you a thermos: 'For thinking, hija.' The town smells of wet wood and fried plantain—alive, messy, speaking."

    # --- merge ---
    "The narrative continues and rejoins the main scene."
    hide jonah_reyes

    scene bg ch14_3be532_3 at full_bg
    # play music "music_placeholder"  # [Music: Layered strings rise into a hopeful motif]

    "The immediate aftermath is worse than any press release makes it sound. The firm files suit. The firm spins narratives. Their billboards go up in clean fonts" "SECURE THE FUTURE."
    "Some of your allies panic; others gird. Rosa and Mateo hold a cooperative meeting under a tarp in the market—flour and fish scales on their hands, the smell of citrus from a crate that hasn't been"
    "sold and will feed a neighborhood tonight. Aunt Pilar calls you three times in two days; the third time she speaks, her voice is steady as an oar."
    show aunt_pilar at left:
        zoom 0.7

    aunt_pilar "You made a storm, niña. Now we learn which roofs hold. We will repair. We will plant. We will see who stays."
    "There are losses you cannot soften. A shuttered bakery, the last bright umbrella of a vendor who decides a different city will be safer for her child. Some families leave with boxes and old photographs. You"
    "are present at each goodbye in different ways: with a packed crate, with an offer of work, with a hand that squeezes and releases."
    "And yet—steadiness assembles itself out of smaller mercies. The independent review Claire demanded begins. Reporters come and write longer pieces than the firm's PR—pieces that show the overlooked offsets in Elena's models, the proprietary assumptions that"
    "ignore local sediment patterns and community land use. As the facts gather, pressure becomes leverage."
    # [Scene: Rooftop Gardens of La Plaza | Afternoon — Weeks Later]
    hide aunt_pilar

    scene bg ch14_3be532_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A child laughing, the soft clink of a watering can; occasional distant pump noise]
    # play music "music_placeholder"  # [Music: Warm acoustic guitar, light percussion—steady, building]
    "Months fold into one another. Funding is uncertain; contractors idle; scaffolding creaks in wet wind. But the pause allows a new paperwork to be written—laws with teeth for wetlands, community land trusts codified with legal counsel"
    "pulled together with sweat and bake sales and fundraisers. You sit in a council room that feels less like a theater and more like a workshop, the smell of coffee and chalk dust binding everyone together."
    "Jonah Reyes and the market cooperative pilot a mutual-aid schedule. The rooftop gardens expand—more pots, more donated soil, an extra bed for kale. Mateo teaches a planting circle to teenagers who one day will remember the year the town learned to hold its breath and then breathe again."

    menu:
        "Mark a planter with a ribbon for those who left":
            "You tie a thin blue ribbon around a planter post. It flutters like a small flag. Jonah nods when he sees it—the gesture answers a grief without words."
        "Plant a citrus sapling instead, for future harvests":
            "You press the sapling into loam, fingers dark with earth. Jonah helps tamp the soil. The seedling looks absurdly small, but it smells like hope when you water it."

    # --- merge ---
    "The narrative continues and rejoins the main scene."

    scene bg ch14_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Voices negotiating, hammers, laughter underneath it all]
    # play music "music_placeholder"  # [Music: The piano returns, now layered with strings and soft brass—resolute, brightening]
    "Not everyone is satisfied. The Voss Spire fights every inch; Elena's legal team tries to narrow the review to procedural delays. There are nights you lie awake with Claire’s equations and the memory of your father's"
    "hands on a rope ladder, trying to make the math match a moral calculus. There are council votes that end in narrow margins. There are petitions that move through public comment like tides."
    "And yet the delay—the chaos you invited—opens room enough to thread protections through the approvals. Community land trusts are established to prevent forced displacement in certain neighborhoods. The wetlands that Claire modeled for preservation move from"
    "lines on paper into actual terraces planted with coir logs and marsh grasses, hand-tied by volunteers with salt on their sleeves. The designs include legal easements and maintenance funds derived from redevelopment taxes—a compromise, but one"
    "with binding teeth."
    "You watch a child climb a reclaimed pier that now bends upward gently instead of forming a wall; the child shrieks with delight when a small wave rushes under. It is a small thing, but in its smallness it is a proof."
    # [Scene: Market | Morning — A Year Later]

    scene bg ch14_3be532_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The familiar clatter of trade; a radio dj playing a hopeful track; the sizzle of empanadas]
    # play music "music_placeholder"  # [Music: Upbeat, warm—community chorus sampled in the background]
    "The market is not the same as it was. Some stalls are new, some faces changed. But the cooperative is stronger—insurance pools, rotating leadership committees, emergency gardens. You and Jonah take shifts together, passing a stack of flyers and pointing to a mapped route for flood-safe deliveries."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "We did a good job, you know. Not perfect. But good."
    "Mara Solano: (the truth comes out as a half-laugh, half-sob) 'We paid with too much. I still see the empty porch at Rosa's old stand. I still hear the list of names who left.'"

    jonah_reyes "We carry that. We didn't make it not hurt. We made it possible."
    "He reaches across the stall and squeezes your hand—callused, warm, steady. You think of the months of legal meetings and seed mixes and nights on the rooftop watching the town breathe. You think of Claire's exhausted,"
    "fierce dedication; of Aunt Pilar's recipes and steady hands; of the people who refused to wait and left, and those who stayed and rebuilt."
    "You feel the bruise of the year, but beneath it a muscle has formed—the town's collective will to remain here, together."
    # [Scene: Rooftop Gardens of La Plaza | Golden Hour]
    hide jonah_reyes

    scene bg ch14_3be532_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft hum of insects, someone plucking a ukulele, distant gulls]
    # play music "music_placeholder"  # [Music: Warm strings and piano in a gentle swell]
    "Mara Solano: (you taste the question) 'Maybe. But I'd rather they remember that people kept each other fed. That we wrote rules into law that can't be waved away by a slick slogan. That we made a place where the rooftop gardens could exist.'"
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "And us?"
    "Mara Solano: (you turn toward him; the light catches the silver streak at his temple) 'You and me—we're a patched thing. We weren't spared the fight, but we learned how to lean. That's not a small victory.'"
    "He smiles, small and honest."

    jonah_reyes "Lean on me, then. We'll keep leaning."
    "You press your forehead to his temple for a moment—salt on skin, the scent of citrus and soil and soap. The sound of the town below is a comforting tangle: market calls, distant pumps, the cadence of people who have learned to be both tender and stubborn."
    "You think of the possible endings that used to haunt the edges of your planning—total erasure, gentrified façades, a slit for a harbor where porches used to be. Those futures still lurk as possibilities, but not"
    "as inevitabilities. The legal protections you helped force into being do not erase all risk, but they redistribute it, knitting community safeguards into the fabric of policy."
    hide jonah_reyes

    scene bg ch14_3be532_8 at full_bg
    # play music "music_placeholder"  # [Music: The music rises, a full chord of hopeful major harmonies]
    "You allow yourself to mark the small, steady list of wins: enforceable wetlands, a legal framework for community ownership, the cooperative's new micro-insurance fund, the market's weekly donations to emergency kitchens, the rooftop gardens feeding a"
    "dozen more households in lean months. You also allow the grief to remain—names of those who left and small, empty places that still ache."
    "Aunt Pilar joins you on the bench, shawl flaring like a bright tide marker."
    show aunt_pilar at left:
        zoom 0.7

    aunt_pilar "You broke the easiest way and chose the hard way. It worked. It hurt. But you held the town."
    "Mara Solano: (words finally whole, quiet) 'We held it together. Not alone.'"
    "She squeezes your hand and looks out over the water, where the light fractures into a thousand small possibilities."
    hide aunt_pilar

    scene bg ch14_3be532_9 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft rustle of pages; a child's distant laugh]
    # play music "music_placeholder"  # [Music: A single piano motif that has become a kind of promise]
    "You close the notebook and tuck the compass pendant beneath your shirt. It is heavy and familiar. Jonah lifts your hand, fingers threaded with yours, salt and dirt mapped into the lines of both your palms."
    "You look at him and then past him—to a town that still smells of sea and citrus and possibility. You feel the long arc of the last year settle into something like a promise: not a"
    "guarantee that the sea will be kind, but that your place in the world has been contested and won in small, durable ways."
    "Your breath catches—not from dread, but from gratitude that you could fight, that you were not alone, that the town's survival was not traded away for a glittering, vacant security."

    scene bg ch14_3be532_10 at full_bg
    # play music "music_placeholder"  # [Music: Gentle strings, then a soft breath of silence]
    "You sit with Jonah, with Aunt Pilar, with the co-op's newest volunteers. The town will still have storms. Paperwork can be appealed; roads will need fixing. But there is a rhythm now: repair, plant, teach, protect,"
    "argue, rebuild. It will not be easy. It will not be clean. It will be real."

    scene bg ch14_3be532_11 at full_bg
    # play music "music_placeholder"  # [Music: Piano and strings hold a sustained, uplifting chord]
    # play sound "sfx_placeholder"  # [Sound: Distant gull call; the faint, ongoing thrum of pumps as a lullaby]
    "You let the night come. You let the city breathe around you. You let your hand find his again. For all the bruises and the losses, the arc has risen. Love, damaged and patient, holds."

    scene bg ch14_3be532_12 at full_bg

    scene bg ch14_3be532_13 at full_bg
    "THE END"
    # [GAME END]
    return
