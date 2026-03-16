label chapter14:

    # [Scene: Boardwalk | Night — rain steady, wind sharp]

    scene bg ch14_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain on wood, distant generator hum, muffled conversations through radio static]
    # play music "music_placeholder"  # [Music: Sparse piano over low strings — steady, low pulse]
    "You press the resignation letter flat against your palm like a coin you can't spend. The paper is damp where the rain found the edge of your pocket; the ink has not blurred, but the words"
    "feel softer now that someone else will read them. You left them at City Hall this afternoon—neat, formal, impossible to be read as anything but a decision—and the act reverberates in your chest with a slow,"
    "stubborn echo."
    "Your breath fogs a small oval in the cold air. Behind the wall of noise from the construction site, the harbor keeps its own counsel: a gull's thin cry, a boat's chain rasping against a piling,"
    "the relentless hush of tide. You let those sounds fill the space where the council chambers hummed earlier—where Maren Voss's slides had clicked, where the mayor's cadence had tried to give everything a civilian calm."
    "You thought you would feel relief. What comes instead is a grinding clarity: you can no longer keep both hands on the levers and expect to hold every life steady. You gave up the lever tonight."
    "The harbor answers with a wind that smells exactly like the choice you made—salt, cold metal, a little smoke from the work lights."

    "Your phone buzzes once. Samir's photo of City Hall, captioned with a single, blunt filter" "Closed doors, open docks."

    scene bg ch14_3be532_2 at full_bg
    # play music "music_placeholder"  # [Music: A low, patient chord — activity without hurry]
    "You turn away from the construction lights and walk the boards that creak with old promises. Each step is the same rhythm you used to listen for in council meetings—timed breaths, measured statements—but now it is"
    "literal: the board underfoot, the tide at the pilings, the small talk of fishermen folding into routine."
    "You keep your jacket zipped against the rain. You keep your scarf—the blue one your mother gave you—tight enough that you can feel its worn thread against your throat. It is silly how much that thread steadies you."
    # [Scene: Tidewatch Harbor | Early Morning — weeks later]

    scene bg ch14_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Hammers, low voices, a child laughing somewhere near a repaired doorway]
    # play music "music_placeholder"  # [Music: Mid-tempo acoustic guitar with discreet percussion — steady work-song cadence]
    "You wake to the smell of damp cedar and coffee. Elias Hart is already up on the roof opposite yours, kneeling with a coil of rope and a grin that looks like work—practical, inevitable. He waves,"
    "and for a second the harbor is a smaller place: two sets of shoulders bent toward the same problem."
    show elias_hart at left:
        zoom 0.7

    elias_hart "I brought extra nails. And Iris says her boat's mainline's ready if you need muscle."
    "You climb up. The roof is heavier now—layers of tarpaulin, new shingles clumsy beside old ones, a scattering of salt. Your palms get callused again in a way that speaks of small victories: the shingles fit;"
    "the leaks slow. It's not grand policy. It is a stubborn refusal to let houses rot while committees argue."

    elias_hart "You okay? People are saying a lot about the council—some of it's ugly."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "I did what I had to. I couldn't keep promising things I couldn't guarantee."

    elias_hart "You stepped away."

    maya_reyes "I stepped away."

    elias_hart "Then help me not let the town fall apart by hand. Teach the workshops. Run the mapping. Be stubborn here, with me."
    "You blink. The offer is plain and dangerous in the way that good things are: it binds you to a different kind of responsibility."

    menu:
        "Take the tide-mapping workshop next week":
            "You nod and run a thumb along your journal's spine—sudden, practical, relieved. 'I'll do it,' you say, and the plan moves from thought into schedule."
        "Ask for more time—coordinate with Professor Kim first":
            "You hesitate; research still tracks in your mind. 'Give me three days. I want the models tight before I teach the town how to map the hazards.' Elias's smile softens—he trusts your caution."

    # --- merge ---
    "Continue narrative"
    hide elias_hart
    hide maya_reyes

    scene bg ch14_3be532_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hammer's steady thud, gulls wheeling]
    # play music "music_placeholder"  # [Music: The guitar picks up, patience and motion woven]
    "Iris shows up midday with a thermos of soup and a face like old rope—weathered, taut against everything it's seen. She gives you both a look that's part blessing and part scold."
    show iris_tanaka at left:
        zoom 0.7

    iris_tanaka "You left the tables."
    "She nods toward the pier where volunteers are stacking sandbags and distributing donated tarps. 'Good. People need someone who'll get their hands dirty 'til they stop bleeding.'"
    "You pass out nails, hand around a mug. Samir wanders through with his camera, quiet, cataloguing faces like he is building an archive of what staying looks like. He pauses beside you and lowers the lens."
    show samir_reyes at right:
        zoom 0.7

    samir_reyes "You look… different."
    "You let him photograph anyway. You do not ask what he'll caption it."
    # [Scene: Rooftop Garden & Salt Marsh Restoration Site | Afternoon — months pass]
    hide iris_tanaka
    hide samir_reyes

    scene bg ch14_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Bees, distant drills, Elias Hart's laughter as children chase gulls]
    # play music "music_placeholder"  # [Music: Warm strings under a steady folk rhythm — hopeful, tethered]
    "Work becomes the language you speak. You teach a workshop about elevation mapping—how to read a slope, how to place storm ladders, how a salt marsh can hold water like a living sponge. Your voice steadies"
    "in front of a crowd—neighbors, fishermen, an accountant whose hands are soft with paper but who now jams a tarp square with a care he didn't know he had."

    "Maren Voss's sea wall is a recurring shadow in the talk. It exists beyond the ridge where the harbor opens, an engineered certainty that keeps some houses dry and leaves others exposed in new ways. People ask you about it in the same breath as they ask where to get sandbags. You answer honestly, which means you cannot simplify" "It helps some. It leaves others vulnerable. We need both immediate measures and communal safety nets."

    "A woman in the crowd, voice raw from worry, asks" "Will my street be next? Do we move or make do?"
    "You don't have the power you used to. You have something else: time, proximity, the ability to teach neighbors to measure, to seed, to shelter. Your answers are practical, filled with compromise and hands-on steps. It"
    "is not the sweeping policy of the council; it is mud and rope and the small geometry of survival."
    "Elias Hart works the kids into planting crews; Samir uses the camera to print flyers that become a small, ragged exhibit down on the pier. People come for food and leave with seedlings and a little more knowledge."

    menu:
        "Lead the marsh replanting tomorrow at dawn":
            "You accept without hesitation—your boots are already muddy at the thought. 'Dawn,' you say. The crowd cheers softly, relief like a wet blanket."
        "Coordinate a legal clinic to help those in relocation zones":
            "You pause, thinking of paperwork and deadlines. 'We'll pull Julian in—he owes us his notes. I'll set it up.' The practical solution ripples outward, slower but steadier."

    # --- merge ---
    "Continue narrative"
    # play music "music_placeholder"  # [Music: The tempo steadies; tasks multiply into days and then months]
    "In the evenings, you and Elias Hart sit under the torn festival banners—the same ones that used to flutter above weekend parades, now mended with different hands and patched fabric. Your laughter there is quiet and"
    "small, the kind that comes after long work and little victories. Sometimes you quarrel in the way of people who share space: over whether to spend dwindling community funds on a new pump or a legal"
    "fee, over how much to push Samir into documenting versus letting him breathe."
    "You notice how the easy, impulsive warmth between you has earned a new patience. There's a bruise under the way you share tasks—an honest, slow stitching where once quick stitches hid poor seams."
    "You do not remake the council minutes. You do not erase the nights when you compromised. Those choices are ledgers under your ribs. Instead you keep bringing hammer and song."
    # [Scene: The Pier | Late Afternoon — the sea wall's new face gleams in the slant sun]

    scene bg ch14_3be532_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The sea against concrete, children playing, a man arguing with a contractor]
    # play music "music_placeholder"  # [Music: Low strings and a piano motif — tension returning, steady but restrained]
    "One afternoon, Samir hands you a print of a photograph: a narrow alley where a family who chose to stay has piled mattresses and sandbags against their doorway. Across town, another photo shows a newly rebuilt"
    "storefront—its owner praised the jobs from the redevelopment. The two prints are pinned to your kitchen wall, a small map of the trade-offs that define your town."
    "You walk the pier and feel each step as a ledger entry. The wall is impressive up close—cleaned concrete, a scar of engineered purpose. You watch contractors finishing a section: a little plaza of funded benches,"
    "LED lights, a plaque about 'resilience.' A cluster of apartments up the ridge answers with new paint."
    "An older woman stands near the fence, eyes like lanterns. She folds her hands around a grocery bag, salt flakes in the crease of her wrist."

    "Older Woman" "They tell us the wall keeps us safe. But the water finds its way. My niece lived on the north side. She packed her life into a trailer two months ago."
    "Her voice is small but not resigned. It is the precise mix of grief and calculation that has become familiar. The wall's benefits are visible; so are its costs."
    "You want to march back to City Hall. You want to tear out every clause that allowed the project to steamroll other measures. Instead you stand, hands in your pockets, watching the contractors smear fresh concrete like an artist finishing a painting that will outlast the day."
    "Maren Voss appears then—unsmiling, efficient, a neat silhouette in a dark trench coat. She is not hostile; she is the politician who made the call you refused to champion. Her presence is a reminder that institutions can move faster when unburdened by the moral scrubbing that once slowed you."
    show maren_voss at left:
        zoom 0.7

    maren_voss "You left a seat at the table. I won't pretend the path is clean. But there are people with jobs now."
    "You could answer with the long list—of neighborhoods left exposed, of legal protections unbargained. You could recount the unpaid work you and others do to mend consequences. You choose steadiness."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Jobs that last are better than jobs that are temporary. And protections that last are better than promises."

    maren_voss "I tried to make something sustainable. Sometimes I had to cut corners to get it done."
    "You think of the older woman's niece and of the mattresses and the Aleppo of compromises you once thought would be strategic. The harbor tastes metallic in your mouth."
    "You do not fight her then. You accept the world she built and then walk away, because the sustainable things you'll grow now are different: marsh grass, social ties, the legal literacy that keeps people from being steamrolled."
    # play music "music_placeholder"  # [Music: The strings lift into a gently aching phrase]
    "You and Elias Hart sit on the edge of the pier as the sun bruises the horizon. Children shout in the distance. The sea is a flat black sheet and, beyond the wall, the water finds its own levels."
    show elias_hart at center:
        zoom 0.7

    elias_hart "Do you regret it?"

    maya_reyes "I regret the harm that still happens. I don't regret stepping away from the place where I could not fix it without breaking my own hands."

    elias_hart "Then stay. Patch roofs. Teach. Be stubborn here, with me."
    "You look out at the sea and then back at him. The festival banners flapping above the boardwalk catch a stray light and the torn fabric makes a flag of your life: patched, frayed, still waving."
    # play music "music_placeholder"  # [Music: A soft, conclusive chord]

    "You reach into your pocket and take out your Moleskine. On the page you write three words with a careful, certain hand" "Mud. Hands. Time."
    "You fold the page and slide the book back into your jacket. Around you the harbor breathes—loss and repair braided in every tide. You have left the halls of power. You have no illusions about neat"
    "endings. The choices you made before are an architecture that will take years to test."
    "But here, on the pier, with tarps flapping and children laughing and a woman who may yet find community help for her niece, the future looks like a set of small actions strung together. It is not triumphant. It is not clean. It is honest."
    "You rise, ready to leave for tomorrow's workshop, boots heavy with salt. Elias Hart shoulders a sack of seedlings and falls into step beside you. Iris calls from across the pier about a pump that needs"
    "fixing. Samir lifts his camera for one last shot of the sunset, and his expression is quiet—documentary made intimate."
    "As you walk back through the boardwalk's heart, the town's shape settles into you: an architecture of people, stubborn and imperfect, choosing to repair what they can. You will live with the consequences of places you walked away from—and of places you stayed to mend."
    hide maren_voss
    hide maya_reyes
    hide elias_hart

    scene bg ch14_3be532_7 at full_bg
    # play music "music_placeholder"  # [Music: The guitar and strings close on a restrained, bittersweet cadence]
    "You do not promise resolution. You promise presence."

    scene bg ch14_3be532_8 at full_bg
    "THE END"
    # [GAME END]
    return
