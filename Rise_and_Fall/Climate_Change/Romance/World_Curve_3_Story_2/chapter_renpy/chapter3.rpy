label chapter3:

    # [Scene: Town Hall / Planning Office | Twilight — Storm Approaching]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, insistent cello; distant, growing wind]
    # play sound "sfx_placeholder"  # [Sound: Door thud; papers skitter; a gull's cry swallowed by rain]
    "You are still leaning on the edge of the long table when the door bangs open and a gust of cold, wet air sweeps through. The sound makes everyone flinch—the boardroom, for a heartbeat, becomes the marsh: exposed, raw, listening."

    "The word lands after the breath settles" "compliance."
    "You taste metal and anger at the back of your tongue. It is a flavor you know too well—part righteous heat, part old fear. You press your fingertips into the worn spine of your notebook until"
    "the leather protests. The friendship bracelet tucked within scrapes your palm like a compass you can't follow."
    "Mayor Lucia's voice cuts through the room in the way she always does—measured, practiced, the cadence that built and kept this town. But tonight her steadiness is threaded with strain. Outside, the storm is already finding"
    "routes the maps didn't predict: gutters carrying a child's toy boat in a slow, stubborn spin; a vendor sopping at a stall on the boardwalk; a ferry of umbrellas moving like a hesitant shoal."
    show mayor_lucia_varela at left:
        zoom 0.7

    mayor_lucia_varela "We have the conditional funding on the table. It will be fast-tracked if we vote tonight."
    "You hold your breath as if inhaling might flood the room. The maps pinned to the wall, the tide charts Dr. Sato ran yesterday, and the 3D model under Elias's trailer dome all feel like different languages for the same emergency."
    hide mayor_lucia_varela

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain hitting the glass; distant shouts]
    "Dr. Kenji Sato stands with his hands folded, the blue of his laptop screen painting his face in waves. The models behind him boil with numbers you know by heart and dread: surge heights, return intervals,"
    "the physics of damage. They are rigorous and monstrous and their glow is almost accusatory."
    show dr_kenji_sato at left:
        zoom 0.7

    dr_kenji_sato "The projections don't lie. The sooner we reduce exposure, the fewer lives will be at risk."
    "You can feel the room shifting under that fact. It is a truth that does not decide itself."

    menu:
        "Step to the window and watch the water":
            "You move to the window. The boardwalk seems smaller close-up, human in its clutter—chairs, string lights, a tarp flapping like a tired bird. A child with a red raincoat chases the spinning toy boat and laughs; the sound twists in you. You think of timbers, of the lantern that bobbed like a small moon."
        "Stay at the table and fold your hands over the notebook":
            "You keep your hands on the spine of the notebook as if it were a small dam. The paper smells faintly of salt and ink. You can feel the bruise behind your ribs: a brother's name you have not let the room simplify into a statistic. Your throat tightens; words gather like storm clouds."

    # --- merge ---
    "The vote starts before you can fully decide how to hold yourself."
    "The vote starts before you can fully decide how to hold yourself. Lucia calls names. Councilors read from prepared statements. The mood is brittle; alliances clack together like wet wood."
    show mayor_lucia_varela at right:
        zoom 0.7

    mayor_lucia_varela "All those in favor—"
    "There are nods too quick. A councilor who owes a favor. A voice from decades of risk-aversion. Someone thinking about insurance premiums and the glossy headlines their vote might buy."
    show amina_reyes at center:
        zoom 0.7

    amina_reyes "If we proceed without safeguards—if we let 'compliance' mean checkbox mitigation—we will lose the marsh in ways spreadsheets never show. The artisanal fishing lanes, the spawning runs, the living shoreline—they're not quantifiable in models that treat them as 'losses' to be bought out."
    "Elias Hart's eyes find yours across the table. He leans forward in that calm way, almost like a harbor taking in a new vessel—evaluating, not dismissing. The hand he reaches across the paper-strewn table is steady;"
    "when it clasps yours there is a warmth that is also an offer of partnership."
    hide dr_kenji_sato
    show elias_hart at left:
        zoom 0.7

    elias_hart "We can shape it from inside. I want that too—ecological buffers, adaptive design. We can insist on phased implementation, mandatory monitoring. Work with me."
    "You can feel the weight of the offer. Partnership with Elias would mean institutional resources, access, leverage—tools that could physically alter outcomes. It would also mean stepping into a machine that has its own momentum and language. You taste the ledger and the salt."
    "Niko Kaur's presence at the table is a taut wire. When the vote edges toward 'in favor' on a narrow margin, Niko Kaur's jaw tightens until it looks like it might fracture."
    hide mayor_lucia_varela
    show niko_kaur at right:
        zoom 0.7

    niko_kaur "You can't hand our choices to people who see us as a test case. They'll measure us, then ship us an answer."
    "Niko Kaur's hands are streaked with salt and tar—work hands, history hands—and when the vote finally passes, something inside them snaps. They push back from the table, the bench scraping like a warning."
    # play sound "sfx_placeholder"  # [Sound: Chair scrape; the door opens behind Niko Kaur with a rush of wet air]

    niko_kaur "This town decides its fate. Not your models. Not your money. We rebuild our way."
    "They storm out, and the door slams in a way that echoes down your spine. The salt on Niko Kaur's face catches the office light; angry rain seems to follow them."
    "Marina keeps her hands folded in her lap. She was the one who organized the children's art display on the boardwalk—little paintings of boats and marsh grass—and now her eyes find the floor. When they flick"
    "to you, they are small and raw, like someone expecting blame but afraid of giving it."
    hide amina_reyes
    show marina_lopez at center:
        zoom 0.7

    marina_lopez "I don't know what to tell the kids."
    hide elias_hart
    show amina_reyes at left:
        zoom 0.7

    amina_reyes "Tell them the truth we can hold: that we will try, and that there are people who will still stand with them."
    "The conversation turns. Dr. Sato tries to translate model uncertainty into policy levers; he has more than once been the bridge between numbers and flesh."
    hide niko_kaur
    show dr_kenji_sato at right:
        zoom 0.7

    dr_kenji_sato "We can run conditional scenarios—phased construction, living-edge trials alongside engineered barriers. But we need authority to pause and adapt as we monitor impacts."
    hide marina_lopez
    show elias_hart at center:
        zoom 0.7

    elias_hart "That's exactly what I'm arguing for. If we get the funding now, we can earmark a portion for ecological oversight—Kenji's monitoring, community liaisons, adaptive clauses."
    "You feel the room narrowing and widening at the same time. The vote has passed on a margin so thin it seems almost surgical. The fracture sets: those who see inevitability in large structures and those who see them as erasers of culture."

    menu:
        "Let Elias clasp of your hand steady you":
            "You don't pull away. Elias's fingers are callused but warm. His reassurance is pragmatic and real; you feel the path opening—access to resources, influence inside a bureaucracy. It feels like compromise that might save lives."
        "Pull your hand back and speak like Niko":
            "You yank your hand away. Your voice cuts sharper than you'd intended. It tastes of old betrayals: 'Compromise' is often a phrase people use to dissolve communities into acceptable losses. You can already hear Niko's footsteps outside."

    # --- merge ---
    "Dr. Sato's graphs continue to glow, lines dancing like small, cold phantoms."
    "Dr. Sato's graphs continue to glow, lines dancing like small, cold phantoms. The 3D sea-wall model sits metaphorically outside in Elias's trailer, white and predatory in your mind like a shark drawn into a bay. You"
    "picture it under the aluminum dome—sleek, promising, a thing that would change shorelines, currents, and people's daily work."
    "You flip the notebook open and it slaps against your palm. The pages are a small map of grief: sketches of marsh contours, tide notes, and the name you have been keeping folded into margins. Your"
    "brother's name is inked there, not as a statistic but as a person who lived between the reeds and the water and whose absence maps the choices you cannot unmake."

    amina_reyes "I tried to measure what couldn't be replaced."

    elias_hart "We're not trying to erase him. We want to keep people safe. Let me help make sure his memory shapes this, not gets buried by it."
    "You want to believe him. You want to believe the resources and his competence can be bent toward honoring what was lost instead of repeating the same erasures."
    "But you also remember Niko Kaur's hands rebuilding a keel by candlelight, the way the boatyard smells of tar and persistence. You remember the night of the storm in a different register—the sound of planks freeing"
    "themselves, the lantern bobbing, the way neighbors turned out with ropes and soup. That memory is not a critique of safety; it's a refusal to let the cost be counted only in dollars."
    "The room feels colder. The hum of the fluorescent lights is abrasive. Outside, the water finds new routes again—floodwater making small, determined maps through the market stalls. You think of the people who will use the"
    "new wall as a back to cling to, and of the marshes that will no longer have a chance to breathe and migrate."
    "Your chest tightens until you can hardly draw a full breath. Betrayal blooms, not like an accusation but as a physical hollowing under your ribs. The town's future and your heart seem to be swept away by the same tide."
    "You stand in the pause after the vote, surrounded by people who are both allies and strangers now—Elias offering professional reassurance, Niko Kaur furious and gone, Marina quiet, the models glowing like presiding judges. The decision is raw and immediate."
    hide amina_reyes
    hide dr_kenji_sato
    hide elias_hart

    scene bg ch3_98c6f2_3 at full_bg
    # play music "music_placeholder"  # [Music: A single, low violin note held and then released into silence]
    "You feel pulled in three distinct directions, each a promise and a wound. The paths ahead are loud with consequence."

    menu:
        "Work with Elias to shape the engineering plan from within, insisting on ecological safeguards.":
            jump chapter4
        "Refuse institutional compromise; rally the boatwrights and the boardwalk to organize a grassroots living-shoreline plan with Niko.":
            jump chapter7
        "Launch a coalition campaign that tries to bind both sides—work with Marina to build public pressure for a hybrid, community-led grant.":
            jump chapter10
    return
