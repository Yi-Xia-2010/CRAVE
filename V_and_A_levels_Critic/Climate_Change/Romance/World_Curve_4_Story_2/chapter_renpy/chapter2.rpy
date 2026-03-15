label chapter2:

    # [Scene: Saltway Community Hall | Morning]

    scene bg ch2_c4ca42_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain murmuring on a patched tin roof; a kettle hissing softly in the corner.]
    # play music "music_placeholder"  # [Music: Gentle, optimistic BGM — low strings and a patient piano]
    "You step in with your notebook still warm from the morning's pages, the cover settling against your hip the way a promise settles against a tidal line. The hall smells of wet banners and strong coffee"
    "— the kind that tastes like work and lasts through meetings. Light from the boardwalk pools across the table where the plywood sheet waits, blank but for the faint ghost of last week's tide stamps."
    "You set the notebook down and slide open the lid. Your handwriting feels cramped on the board's surface, tide-lines drawn with a blunt marker that squeaks against weathered wood. Salt has smudged one of the stamped"
    "charts; a brown smear undermines a neat row of numbers. You curse under your breath — a small, private annoyance — then remind yourself the data is a map, not a verdict."
    "Maya arrives the way she always does: half-breathless, wholly present, her patched coat brushing the table and then yours in a little electric contact that is all comradeship and no pretense."
    show maya_lin at left:
        zoom 0.7

    maya_lin "You started without me? Traitor."
    show ava_maren at right:
        zoom 0.7

    ava_maren "I left room for you to stage a dramatic entrance. You missed your cue."
    "Maya presses her palms to the plywood, eyes bright as molten glass, and folds your cramped lists into a plan as if sorting clothes. She gestures, quick and efficient, placing volunteer shifts next to material donors, then labors and then community-watch hours."

    maya_lin "Jun can round up the records. Old Mara can marshal the planting crew. We should fold Silas into the fabrication team — he learns fast. You mark the tides; I'll call the volunteers. We'll make a rota."

    ava_maren "Rota means schedule, right? Or is it a plot to keep me awake?"
    "Maya's laugh is brief and stubborn and the hall seems to inhale. She taps a finger where a tide-line and the footbridge meet, then looks up like she's found a missing stitch."

    maya_lin "We need Jun's angle. If VossCorp's permits have those loopholes Jun talked about, we use them to press for community tenure. Jun — you still coming?"
    "The door opens and Jun steps in, his rain-stained blazer more threadbare than you remember. He carries a recorder and a wet envelope of papers, eyes tired but focused."
    show jun_park at center:
        zoom 0.7

    jun_park "I'm coming. And yes — discreetly. I can pull the permit trail without making a splash. There's a clause about accelerated approvals; it might tie into their funding calendar."

    ava_maren "Discreet as in careful, not hiding. We need facts, Jun, but we need people to know what those facts mean."
    "(He offers a small, tired smile.)"

    jun_park "Always the public translator, Ava. I'll get the documents. Say a word and I leak them to the right journalist."

    maya_lin "Jun, who? We don't need dramatic headlines yet. We need leverage at the council table."

    jun_park "Right. Quiet leverage. An audit letter, a public query that doesn't burn the source. It'll make them respond."

    "The conversation loops — not short exchanges, but small negotiations; you trade phrases about schedules, material lists, and who can scaffold next week. The multi-turn rhythm of planning — propose, correct, pushback, agree — settles into a quiet competence. Your survivor's guilt sits in the room like a familiar chair: useful for leaning on, not for sleeping in. You sense it tug at the margin of every sentence" "Can we really keep everyone? Will a living wall hold? Am I promising what I can't deliver?"

    menu:
        "Offer Jun the last cup of coffee":
            "You slide the steaming mug across the table toward Jun. He accepts it with a grateful murmur; the warmth seems to brighten his shoulders and the conversation loosens into practical detail."
        "Keep the coffee for yourself, make notes":
            "You wrap your hands around the mug and feel the heat go straight to your palms. Your notes sharpen; you map the tide-line again, fingers leaving damp arcs on the plywood. Jun watches you and smiles, a soft recognition of the work you carry."

    # --- merge ---
    "Both outcomes rejoin and the planning conversation continues."
    "Maya taps a stack of wet napkins where you've been sketching grant language between meetings — short clauses, community-benefit statements, phrases that feel both legal and intimate: people-first; retrofit, not remove; living infrastructure as public commons."

    maya_lin "You can talk to Mara about the oral history for the grant narrative. Her memory is a public good, Ava. People respond to stories more than spreadsheets."

    ava_maren "Stories open doors. But the spreadsheet buys materials."
    "Jun folds his papers into his blazer pocket and nods."

    jun_park "I'll thread the audit query through channels tomorrow. Quietly, like I said. And I'll annotate any clauses that could be pressure points. We can use them in the council packet."
    "Maya gives you a look that is equal parts fierce and gentle."

    maya_lin "You pull the council packet together, and I'll organize the volunteers. You're the one who makes the math human."

    ava_maren "People first."
    # play sound "sfx_placeholder"  # [Sound: The rain slows to a soft patter; the kettle's hiss fades. The hall feels like a heart with steady beats.]
    # [Scene Transition: A narrow boardwalk, sunlight now breaking through low clouds.]
    # [Scene: Tide Garden | Noon]
    hide maya_lin
    hide ava_maren
    hide jun_park

    scene bg ch2_c4ca42_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Water lapping against algae-streaked stone; distant construction sounds softened by the garden's hush.]
    # play music "music_placeholder"  # [Music: Low, hopeful harp; the tempo easing into a warm pace]
    "You meet Ori in the Tide Garden, his overalls smeared in paint and salt, welding goggles pushed up on his head like a casual crown. He is a small flurry of motion, hands always finding something to mend or to make beautiful."
    "(He grins when he sees you.)"
    show ori_navarro at left:
        zoom 0.7

    ori_navarro "You're late by neighborhood standards and early by civil-engineer standards. Pick a crime."
    show ava_maren at right:
        zoom 0.7

    ava_maren "I prefer to commit both."
    "Ori's amber eyes have that mischievous light you know, the one that makes problems look like projects. He runs a gloved hand along a seam, proud and a little embarrassed."

    ori_navarro "I finished the joint last night. See? The root mesh is woven through the bio-concrete so the plants anchor and the module still flexes. We can bolt these to pontoons or splice them into the existing seawall."
    "You lean close enough to smell the faint sweetness of algae and the metallic tang of reclaimed wire. Tiny shoots of microgreens peek from the lattice, and a few damp leaves brush your knuckles."

    ava_maren "It looks… alive."
    "Ori watches your fingers touch the plants."

    ori_navarro "Beauty is resistance, remember? Also, structural integrity. Two birds with one anchor bolt."
    "He steadies a plank while you test the module's flex. Your fingers meet on the plank's edge for a brief second while both of you steady it; small contact that feels larger than the length of skin that meets."

    menu:
        "Let your hand linger for a moment":
            "You hold the plank steady with him a beat longer than necessary. The garden seems to lean in with you; Ori's smile softens into something almost like an answer, but he looks away first, blinking as if to clear an idea."
        "Pull your hand back politely":
            "You withdraw quickly and steady the plank from your side. Ori notices, and his grin takes on an affectionate, teasing tilt. He nudges the module into place and says something about your 'stubborn efficiency' that makes you laugh despite yourself."

    # --- merge ---
    "Both outcomes rejoin and the scene continues."
    "Ori tucks a sun-bleached topknot behind his ear with a practiced motion that makes the sun catch at the tips. For a second, you notice everything about him that has nothing to do with public projects:"
    "the freckle by his ear, the way his laugh reaches his eyes, the thin line of a scar on his thumb where an old project went a little too far."

    ori_navarro "You look like you're cataloguing instructions in your head. Are you learning to relax, Ava Maren, or are you planning the rota for breathing exercises?"

    ava_maren "If breathing had a rota, I'd schedule it before meetings."
    "Ori eyes the notebook on your hip — he knows it, knows you — and he steps closer to point at a margin note you'd scrawled earlier. He traces the phrase 'people-first' with a fingertip where the ink has bled."

    ori_navarro "People-first. I like that. It's soft and hard at once. That's how we build — marrow and shell."

    ava_maren "We have to make it persuasive. The council needs a narrative they can hold while the engineers do the math."

    ori_navarro "Tell them a story they can't ignore. Tell them the tide-line as a family map. Show how these roots anchor more than stone."

    ava_maren "And we'll show them it's affordable, maintainable, and—"

    ori_navarro "—and lovely.' (He finishes, like a soft bell. 'Lovely"
    "You both stand for a moment in the diffuse light, watching children inclined at a low terrace, a volunteer adjusting a bolt, Mara's shadow as she inspects a planting bed. The work is ordinary and miraculous."
    "You begin to sketch again — grant language on a wet napkin pulled from Ori's satchel. Your handwriting is small and neat where you draft the executive summary: community-managed modules; in-kind labor credits; training programs for"
    "local youth. You scribble budget estimates in a margin, then cross them and rework them. The slow arithmetic of hope."

    ori_navarro "You look exhausted. You should sit."

    ava_maren "I don't want to sit when there are bolts to mark and a rota to finish."
    "Ori hesitates the way he does before real confessions — he makes a joke, soft and protective."

    ori_navarro "All right, general. But don't try to carry the ocean. Let me hold the corner with you."

    ava_maren "We hold it together."
    # play sound "sfx_placeholder"  # [Sound: A gull calls far off; a few faint hammer taps punctuate the air. The city hums like a distant engine — possible storms on the horizon, but the noon light is generous.]
    "Your arousal — measured, low, intimate — has climbed from the steady meeting rhythm to this warm, coordinated action. The energy in the garden is hopeful and focused, like the close of a long rehearsal when the stage finally agrees to hold the actors."
    "You tuck the napkin into your notebook, the 'people-first' line folded between pages, and you breathe once, deliberately. The survivor's guilt hums under your breath, but the day's work, the small proof embodied by the living wall, eases it into a manageable weight."
    "You look up at Ori. He meets your gaze, and for a moment the plans and permits recede; there is only the simple fact of being together in work and in light."
    "(Softly)"

    ori_navarro "Tomorrow you present the packet to the council, right?"

    ava_maren "I'll draft the proposal tonight. I need Jun's annotations, Mara's voice, and—' (You list names as if casting a net.) '—a few more volunteers for the install team."

    ori_navarro "I'll make you a mock-up of the visuals. If people can see it, they start to imagine living there. And silhouettes sell more than spreadsheets."
    "Ava Maren: (You let the idea settle.) 'Show them silhouettes. Tell them the story. Make it feel like something their grandchildren might touch.'"
    "Ori nods, then, for a beat that tastes like the highest point of the morning, he slides a small seaglass charm from his neck and taps it on the notebook's cover — a quiet, private punctuation."

    ori_navarro "Bring them something they can touch. We'll make them feel it."
    "You close the notebook, the pages whispering shut. The plan needs allies, resources, and a public narrative that holds as much heart as it does math. The Tide Garden hums around you — the living modules"
    "flex, the solar sails fold shadows into wings, and the city beyond sings of cranes and possible futures."
    "You tuck your hands into your jacket pockets, feeling the paper and the warmth of Ori's charm thrum against your palm like a small, steady tide."
    "You look back at the plywood board in your mind, at Maya's quick orders, Jun's careful compromises, Mara's patient memory, Ori's lit mischief. For a moment the enormity of it — keeping a neighborhood whole against"
    "the machinery of displacement — presses at the edges of your chest, but it is not an avalanche. It's a steady climb you will share."
    "Your arousal settles close to the chest: low, focused, optimistic. You feel the momentum of the day as a rope you can step onto, not as a cliff you must leap."
    "You step off the garden's edge onto the boardwalk again, notebook at your hip. The sun has thinned; clouds gather like a promise that will keep until the next tide."
    "The next step is inevitable: the proposal. But before that — before arguments and numbers and council rooms — there is the warm, human work of translating fear into a narrative the city can hold."
    "You fold your fingers around the notebook and taste, briefly, the salt and the coffee and something like hope."
    hide ori_navarro
    hide ava_maren

    scene bg ch2_c4ca42_3 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
