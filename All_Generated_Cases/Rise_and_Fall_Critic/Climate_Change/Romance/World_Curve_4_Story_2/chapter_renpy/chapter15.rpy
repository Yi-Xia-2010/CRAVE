label chapter15:

    # [Scene: Old Lighthouse Rooftop Greenhouse | Dawn]

    scene bg ch15_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Gull calls distant, the low mechanical hum of pumps, an undercurrent of wind through rigging]
    # play music "music_placeholder"  # [Music: Sparse strings, minor-key — weighty, patient]
    "You stand with your palm on the warm rim of a seed tray, feeling the faint pulse of heat lamps through the plastic wrap. The greenhouse smells of wet soil and citrus—Maya's improvised compost tea—laced with"
    "salt and the sharp chemical tang of stabilizers from the engineered mats waiting outside. Your compass is a cold press against the soft fabric of your jacket. Celine's signature is on the municipal covenant; the funds"
    "are flowing. The acceptance of the hybrid plan sits in your chest like a stone that keeps the tide at bay and, simultaneously, remembers what it pressed under."
    "You watch Leyna scroll through the morning's feed on her tablet, her fingers moving with that scientist's economy—small, precise motions that try to make chaos legible. Ivo is out by the glass, leaning on the sill,"
    "chin propped on his fist. He looks at the harbor and back at you, and for a moment the weight between you balances not on plans but on a shared history of hands and seawater."
    show dr_leyna_ortiz at left:
        zoom 0.7

    dr_leyna_ortiz "The covenants bought us monitoring and enforceable setbacks. They bought the terraces and the living mats in the shallow bays. Early data from the pilot is positive — turbidity down, juvenile beds recolonizing. But enforcement windows are narrow. We have legal teeth, yes, but only if the council keeps biting."
    show alys_maren at right:
        zoom 0.7

    alys_maren "And if they don't?"

    dr_leyna_ortiz "Then the teeth rust. The clauses are good on paper, but they're not bulletproof in a crisis. Emergency clauses, discretionary waivers—those can be invoked. We built a mechanism that depends on political will."
    show ivo_calder at center:
        zoom 0.7

    ivo_calder "Political will's a currency Celine knows how to mint. She'll be arguing for flexibility the second the mayor's budget creaks."
    "You breathe in through your nose and the smell of compost steadies you. You can taste the bargain you struck: local control tied to outside capital; ecological guardrails written in legal language; an uneasy partnership with"
    "the woman who dresses every decision like a deal. It feels, perversely, like rescue and surrender in the same motion."

    menu:
        "Check the terrace installation schedule with Leyna":
            "Leyna flips the tablet and shows you the sequencing. 'If we shift crew three hours earlier we can seed the south quadrant before the next high wind,' she says, eyes bright with the fixable."
        "Walk out to the terrace site with Ivo":
            "Ivo slaps a hand against the greenhouse doorframe. 'Good. Come see what raw hands can do,' he says. Outside, the taste of salt and sawdust is immediate, and the work smells like sweat and diesel."

    # --- merge ---
    "The narrative continues."
    "Whatever you choose, the day will be full of screws, signatures, and small reconciliations. You tuck your notebook into your jacket and feel the braided cord against your wrist; it is a loop that reads like a promise more than a plan."
    # [Scene: Engineered Terraces | Midday]
    hide dr_leyna_ortiz
    hide alys_maren
    hide ivo_calder

    scene bg ch15_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rasp of shovels, a distant engine, the clatter of a crate dropped. A dog barks faintly near the warehouses.]
    # [Smell: Fresh-cut timber, damp earth, hot metal.]
    "The terraces look hopeful from the cliff: geometry made of effort, a man-made mimicry of natural protection. Leyna walks the line with you, her boots sinking into the mud in a rhythm that is almost prayer."
    "Oba Kofi stands at the lowest tier, cane planted, watching the water skim the new surfaces with the slow recognition of someone reading tide marks like scripture."
    show oba_kofi at left:
        zoom 0.7

    oba_kofi "This was how my father told it: small edges hold the sea back. But the sea is patient; it finds ways. Keep the hands, girl. Keep the hands."
    show alys_maren at right:
        zoom 0.7

    alys_maren "We keep them. The covenants force maintenance checks, compensation funds for temporary relocations—"

    oba_kofi "Paper is wind sometimes, Alys. The real work is remembering why we build."
    "Maya is here, sleeves rolled, hair braided tight. She laughs too loud when Ronan trips with a spool of rope. The scene is almost ordinary: kids making jokes, crews hauling mat sections, the conspiratorial intimacy of"
    "people who have rebuilt things before. But under that ordinary is the new arithmetic — who gets priority crews, which shorelines receive masonry versus living mats, how to allocate scarce trucks."
    show celine_harrow at center:
        zoom 0.7

    celine_harrow "We agreed to strict ecological covenants. We have reach-back funds for oversight, and the contracts were written to include community liaisons. This is the model municipalities will look to."

    alys_maren "And if a private contractor tries to waive maintenance to meet quarterly targets?"

    celine_harrow "Then we enforce. We have penalties. We have oversight. We also need to be pragmatic when a storm threatens homes; flexibility prevents panic."
    "Her pragmatism tastes of ledger lines. You see, in fine print, clauses that allow 'temporary emergency deviations' with post-event review. It is a hinge. You can feel the tension in how each stakeholder pronounces the word 'temporary' — a promise for some, a loophole for others."
    hide oba_kofi
    show dr_leyna_ortiz at left:
        zoom 0.7

    dr_leyna_ortiz "The science says staggered, adaptive measures are best. But the legal framework needs custodians. We need the community to be that custodian. If enforcement lapses — if the council's eyes slide — we will see the erosion where the hardening was applied without habitat buffers."
    hide alys_maren
    show ivo_calder at right:
        zoom 0.7

    ivo_calder "And when that erosion eats your neighbor's dock, who's standing on principle? People need roofs tonight. They need the work today."
    "You want to answer both: Ivo's urgency and Leyna's caution. Your throat tightens because the truth is that both are right and both will be wrong somewhere down the line. You can feel how the compromise you accepted is already an argument in small parts."

    menu:
        "Tell the crew to prioritize the north stretch — it's where the village keeps most homes":
            "The crew looks toward the north. 'We'll get them there before dark,' Maya says. It's a visible act; a comfort to many."
        "Insist on the scientific sequence; seed the pilot bay first":
            "Leyna nods, gratitude plain. 'If that pilot fails because we rearranged the sequence, everyone loses the long game,' she says. Your insistence tastes like long-term stakes."

    # --- merge ---
    "The narrative continues."
    "Your decisions ripple. People catch on to which way you lean like flags on a breeze."
    # [Scene: Harbor | Late Afternoon — Storm Rolling In]
    hide celine_harrow
    hide dr_leyna_ortiz
    hide ivo_calder

    scene bg ch15_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The wind speaks now as a thing with teeth. The harbor bell tolls, urgent. An undercurrent of shouting, then engines starting — volunteer pickups, Ivo's crew preparing for launch.]
    # [Smell: Ozone and diesel and the musky tang of low tide.]
    "No plan survives the first real test. The storm arrives like a ledger that remembers who invested and who didn't. The terraces grip in places where mats were planted and workers stood cold for hours; elsewhere,"
    "where developers shoveled faster and skimped on root structure to meet a deadline, the sea bites back. The engineered seawalls hold along main streets—where the covenants stipulated reinforced setbacks—but down in the poorer stretches, where 'temporary"
    "deviations' were approved in the name of immediate shelter, water finds a lower seam and pushes through."
    show ronan_pike at left:
        zoom 0.7

    ronan_pike "We lost the boatyard storefront! The water took the dock posts clean!"
    show ivo_calder at right:
        zoom 0.7

    ivo_calder "They signed off on the emergency waiver. Celine said it was better than nothing."
    show celine_harrow at center:
        zoom 0.7

    celine_harrow "We moved to protect lives. Ivo, you know the council had no good choices."
    hide ronan_pike
    show alys_maren at left:
        zoom 0.7

    alys_maren "The covenant allowed deviations only with post-event review. Who signed the waiver?"

    celine_harrow "The emergency committee with the mayor's imprimatur. We acted—swiftly—so people wouldn't be out in the open."
    "Ivo's jaw tightens. Leyna stands a few feet away, hands balled into her pockets, watching the water rim a small house where a child once painted fish on the step. The enforcement you counted on is"
    "fraying into crisis triage. The legal protections you thought would bind people to ecological sense loosen under immediate human panic."
    hide ivo_calder
    show oba_kofi at right:
        zoom 0.7

    oba_kofi "Law can be wise, girl, but it is the people who have to want the law kept."
    "You watch a volunteer pass a soaked blanket to an elderly woman whose stoop now sits in a foot of new ocean. That woman looks at the blanket, then at the seawall two blocks away holding"
    "stubbornly, and the way her eyes move makes the trade-offs a threshing sound inside you."

    menu:
        "Rush to coordinate rescue with Ivo — hands first, policy later":
            "Ivo nods, already moving. 'We don't argue with the tide,' he says. You drop your clipboard and lift crates, sleeves rolled; your hands know the language of salvage."
        "Contact Leyna and the council to lock down post-event reviews — push for immediate legal accountability":
            "Leyna takes out her tablet and starts drafting a request for a review hearing. 'We have to make sure 'temporary' doesn't become permanent,' she insists. Your fingers ache from the weight of paperwork you must now use as a tool."

    # --- merge ---
    "The narrative continues."
    "There is no neat victory here. There is only triage and paperwork and the soft arithmetic of loss."
    # [Scene: Cliff-top Overlook | Dawn — After the Storm]
    hide celine_harrow
    hide alys_maren
    hide oba_kofi

    scene bg ch15_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant engines, an occasional cracked laugh, the soft, steady call of an unseen bird]
    # [Smell: Wet wood, salt, a faint, acrid trace of burned wiring]
    "You climb the cliff steps, boots heavy with mud and bits of the day's work. Dawn is an embarrassed light, painting the water with reluctant color. In the hush, you can count the wins and the"
    "losses like wounds: saved docks, drowned stoops, a barn up the ridge that held because the seawall was prioritized, a row of low-income homes taken because materials were diverted during the emergency."
    "Maya meets you at the top, her face thin with fatigue. She doesn't need to ask; the tally is written in the slump of your shoulders."
    show maya_maren at left:
        zoom 0.7

    maya_maren "We helped people. We pulled families from their roofs. But Tony's shop—"
    show alys_maren at right:
        zoom 0.7

    alys_maren "Tony said he'd rather lose the shop than see his neighbors homeless. He wrote it on his calendar last spring. He said he trusted the plan."
    "You remember Tony's hands—calloused, sticky with varnish, the way he used to knot line with a sailor's ease. You remember telling him where to stand when the water came, and you remember his nod. Memory is a ledger you cannot balance."
    "Ivo appears beside you, wind-rough, hair sticking to his forehead. His eyes are a kind of molten apology. He reaches for you, then doesn't. The distance between your practical side and your human side has never been so visible as in this exhausted morning."
    show ivo_calder at center:
        zoom 0.7

    ivo_calder "We did what we could. We were right to protect the houses when we did. But we lost some things we could've saved if we'd moved differently."

    alys_maren "We followed the hybrid — the money, the covenants. We built what law allowed. We couldn't make everyone choose."

    ivo_calder "You thought the covenants would be a shield. I thought we'd make sure no one had to choose. Both of us were trying to keep Saltwick whole."
    "You want to take his hand. You want to argue about the ethics of deviation and post-event review or lie together and watch the sunrise. Instead you feel the compass's dent against your sternum, a steady"
    "cold that says you were not only a scientist but a person who will be asked to live with the consequences of compromise."
    hide maya_maren
    show celine_harrow at left:
        zoom 0.7

    celine_harrow "We avoided the worst. We preserved municipal solvency and protected the main arteries. In time, more will be rebuilt."

    alys_maren "Some will be rebuilt for whom, Celine? Who decides whose roofs matter first?"

    celine_harrow "We did what the council could under pressure. We saved the town's spine. Without the funds, none of this would be possible."
    "Her words feel like scales dropping: both true and sharp. You look out at the terraces, at the patches of seagrass that glint with recent planting—small green victories—and at the washed-out footpaths where children once ran barefoot."
    hide alys_maren
    show dr_leyna_ortiz at right:
        zoom 0.7

    dr_leyna_ortiz "Ecologically, we can recover what we planted. Legally, the covenants will help in the long run if the council enforces them. But we must hold the line on 'temporary.' We must document, litigate if necessary. Science without custody is just experiment."
    hide ivo_calder
    show oba_kofi at center:
        zoom 0.7

    oba_kofi "There is healing. There is also learning. The ocean gives mercy sometimes, and takes it other times. You have done well where you could. Now you must be the ones who will watch—watch the law, the walls, and the memories. That is the hardest work."
    "You let the sunrise press its thin light into the ash of the storm. It is a light that tells the truth without flattery: partial, patient, honest about the miles yet to walk."
    "You think of the covenant clause about post-event review, about the people who will need help navigating the paperwork, the advocates who will need training to hold officials to their promises. You think of Ivo's hands digging into mud, of Leyna's tired face, of Maya's small, fierce hope."
    "You cannot undo the night. You cannot undo the compromises. But you can stand on the cliff and see the scars and the seedlings both. You bear the knowledge that compromise bought time and bought pain."
    "It bought debate; it bought survivors and survivors' debts. It bought the legal scaffolding for something better, but some scaffolding bent under pressure today."
    "You feel the weight of it settle into the bones the way salt settles into ship timbers. You promised protection; you also promised care. The hybrid plan was meant to thread both promises together. It did not always succeed. It never could succeed for everyone."
    "You close your hand around your compass and let the ocean noise fill the spaces where words fail. This is the kind of ending that is not an ending at all but a handoff to the"
    "long work — policy fights in Harrow Hall, community training sessions in the greenhouse, legal petitions, and, stubbornly, the planting of seagrass year after year."
    "You do not know if Ivo will stay at your side in the way you hoped. You know he will stay in Saltwick, whether at your side or in the harbor, mending, protecting, stubborn. You know"
    "Celine will keep her seat in council and wield her craft. You know Leyna will keep pushing numbers until the data tells stories that the public can trust. You know Oba Kofi will keep telling the"
    "tides' old tales."
    "You exhale and the breath tastes like mud and salt and resolve."
    hide celine_harrow
    show alys_maren at left:
        zoom 0.7

    alys_maren "We did not save everything. But we saved something we can grow from."
    "The morning is a pale, deliberate thing. People are already at work clearing debris, checking on neighbors, reading legal texts under tarps of plastic. The hybrid plan — with its covenants, its enforcement mechanisms, its political compromises — will require vigilance and grief in equal measure."
    "There is no triumphant swell, no clean resolution; the music is a low, steady chord that accepts the brokenness and insists on movement. The story of Saltwick continues, stitched with scar tissue and seedlings, governed now"
    "by law that demands caretakers and by people who will have to decide, day after day, whether to hold those caretakers to account."
    hide dr_leyna_ortiz
    hide oba_kofi
    hide alys_maren

    scene bg ch15_f99e88_5 at full_bg
    # play music "music_placeholder"  # [Music: Single, fading note — somber, unresolving]

    scene bg ch15_f99e88_6 at full_bg
    "THE END"
    # [GAME END]
    return
