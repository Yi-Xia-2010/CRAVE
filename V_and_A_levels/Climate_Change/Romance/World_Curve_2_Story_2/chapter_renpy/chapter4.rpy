label chapter4:

    # [Scene: Council Hall | Night]

    scene bg ch4_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain on stone, distant gull calls cut by traffic—an undercurrent of low, anxious murmuring]
    # play music "music_placeholder"  # [Music: Tense, quickening strings; a steady percussion like a heartbeat]
    "You step out of the chamber with the taste of council air still in your mouth—too-polished coffee, the metallic echo of the gavel. Rain pins your hair to your neck; the coat takes the cold and"
    "wears it where your shoulders are tired. The room's weight sits in your chest like an extra rib: the empty white of the projector, the eyes stacked in rows, the chair's demand for a clear answer"
    "you gave."
    "You didn't give it the way some in the hall wanted. You gave the town back to itself—small, messy, stubbornly human—and the press, and the powerful, and the numbers have already begun to clamber."
    "Eli is waiting on the other side of the steps, hood pushed back, hair frizzed with salt. His grin is quick—too quick—and the palms of his hands are dark with tar, the smell of hot resin"
    "lifting and sticking to you as he takes your arm. The contact steadies the storm inside you for a fraction of a breath and then sets it racing again."

    "Elias 'Eli' Rowan" "How bad was it in there? Did anyone try to—?"
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "They tried to sell certainty. Livia sold the future in crisp steps. I sold weight. She called it 'delay.'"

    "Elias 'Eli' Rowan" "You did what you had to. We can start tonight. Bring tools, bring people."

    mara_kestrel "Tonight? The injunction—Tess warned me it was coming."
    "A flurry of movement pulls at the sidewalks: neighbors unfurling posters from plastic tubes, chalk scrawl taking over rain-darkened planters, the kind of urgent organizing that makes your skin prickle. The town has broken clean into action, a visible fracture and a pulse."
    # [Scene Transition: Walk to The Arbor — rain slashing against glass; overhead lights warm against the gray]
    # [Scene: The Arbor | Night]
    hide mara_kestrel

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The buzz of a generator, the rhythmic clack of rivets, distant hammering; conversations layered like fabric]
    # play music "music_placeholder"  # [Music: Low, insistent rhythm—urgent but not frantic]
    "Inside the Arbor, it smells of wet wood, heated metal, and a green undernote of soil. Sunlight is a memory—streaks of reflected sodium lamps paint the glass. You set your soaked notebook on the workbench and"
    "watch Eli peel off his tar-smeared gloves, the protection they provide a map of his worry."
    "Rafi arrives with a bundle of paper, and when he unfurls it, the smell of old salt and the tear of brittle edges fills the bench between you."
    show rafi_gmez at left:
        zoom 0.7

    rafi_gmez "These are your kind of maps, Mara. Not the tidy prints—real lines. Look here—my grandfather marked it when the tide took the old quay. See where the marsh used to hold?"
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "These are beautiful.' (your voice tight) 'And dangerous. They show what we've already lost."
    "Dr. Naomi Park appears, damp hair tucked into a loose knot, a sheaf of annotated printouts tucked under one arm. Her face is a practiced map of concern—lines at the eyes that only deepen when she looks at the models."
    show dr_naomi_park at center:
        zoom 0.7

    dr_naomi_park "The covariances on the southern transect are worse than we thought. If we harden the break near the estuary without restoring the reedbeds, we shift wave energy—"

    "Mara Kestrel (cutting in)" "—and drown the flats we need for juvenile fisheries. I know."

    "Dr. Naomi (careful)" "Which is why the models ask us to be slow. Trade-offs aren't moral blips—they're tectonic."
    "Her words land like stones. You feel each syllable find purchase in the soil of your conviction and spin the ache wider: slow decisions can mean fewer mistakes, but slow decisions can also mean waiting for a storm that won't wait for models."

    "Elias 'Eli' Rowan" "Models are one thing. People are another. We can put up modular breakwaters—low, removable—stitch them in with planted beds. We can retrofit rooftops to catch the next storm's water. Do something real now."

    "Dr. Naomi (exhaling)" "Pilots are good. But pilots have to be designed with the metrics in mind or the council rips them apart."
    "The bench becomes a map: sketches splayed, salvaged metal fittings, a salvaged wave-attenuator prototype in the center like a small island. Your hands move—measuring, sketching, translating the life's worth of neighbors into bolts and seams. The"
    "sea-glass pendant at your throat is cold, then a slow, steady warming as if the stone knows the town's immediate heat."

    menu:
        "Sketch the first modular breakwater profile now":
            "You draw urgent, angular lines, the tip of your pen cutting the paper. Your hand shakes but the proposal forms—anchors that can be reset, timber ribs wrapped in recycled mesh. Eli murmurs improvements, and the pair of you fall into the easy sync of past projects."
        "Call a quick neighborhood meeting outside the Arbor first":
            "You step outside into the rain and shout for instant attention. Voices collect—neighbors breathing in the cold. You explain the sketch in rough terms; consensus forms like a tide. It takes longer, but you leave with names, chores, and the weight of shared responsibility."

    # --- merge ---
    "The narrative continues."
    # [Scene: Late Workshop Hours | Sodium Lamps — Night deepens]
    hide rafi_gmez
    hide mara_kestrel
    hide dr_naomi_park

    scene bg ch4_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Welding hiss, the clink of metal, low conversation threaded with occasional laughter that tastes brittle]
    # play music "music_placeholder"  # [Music: Agitated tempo—staccato strings rising]
    "Tess O'Malley slips into the workroom with the guarded gait of someone carrying a secret in a town where secrets leak like tide. Her anorak is pulled up against the ongoing rain."
    show tess_omalley at left:
        zoom 0.7

    tess_omalley "You need to know—Livia filed an injunction. The council lawyer confirmed it an hour ago. They served it on a community plot owner near the promenade. They're moving fast."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "On what grounds?"

    tess_omalley "Unauthorized modifications of public seawalls. Liability. Safety."

    mara_kestrel "Or power.' (your voice hardens) 'They'll call it safety and call it final."
    "Elias 'Eli' Rowan's jaw tightens. He steps closer, lowering his voice so the table's hum swallows it."

    "Elias 'Eli' Rowan" "If she freezes us legally, the pilot never gets off the ground."

    mara_kestrel "Then we risk working anyway. We—' (you stop because the legal frost presses in) '—or we slow, make the papers, fight through channels. People need work, Eli. They need protection faster than permits."

    "Rafi (cutting in)" "I don't want to see my brother's shop flood again. We should build where we can build. The old markers show places the tides forget for a while. Use those."
    "Grandma Hira arrives, breathless from running between houses, her shawl dotted with rain. Her eyes slide over the plans and rest on you with a weathered intensity."
    show grandma_hira at center:
        zoom 0.7

    grandma_hira "Listen. If the law stops us, the law will not stop the water. We patch what we can. We watch. We hold hands when the nights get worse. You make places where children can sleep, Mara. We don't ask permission from the sea."
    "Her words are small and fierce; they bend something in you that has been braced since the council. The town's memory, Rafi's hand-maps, Grandma Hira's insistence: these are not data points. They are bones."

    menu:
        "Tell the group we push tonight despite injunction":
            "You look at each face in turn. When you say 'we go tonight,' the room exhales like a single lung. Tools are claimed. People cross-check ropes and measure lines with hands that have known storms. There's a tremor of fear in the laugh, but the work begins immediately."
        "Insist on a strategic pause to gather legal counsel and media":
            "You call for pause. Some grimace. Others nod, relieved. Dr. Naomi agrees to redraft risk assessments for publication. Tess promises to leak the injunction details to friendly press. It's slower, but it adds armor."

    # --- merge ---
    "The narrative continues."
    # [Scene: Estuary Research Lab — Late Night]
    hide tess_omalley
    hide mara_kestrel
    hide grandma_hira

    scene bg ch4_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft beeps of equipment, the whisper of people moving on alert]
    # play music "music_placeholder"  # [Music: A taut, rising drone—tense and focused]
    "You and Eli hunch over a table of outputs. Dr. Naomi spreads an overlay—model run A against Rafi's map."
    show dr_naomi_park at left:
        zoom 0.7

    dr_naomi_park "If you harden the wrong segment, wave refraction increases here—' (she taps a line) '—and you take the marsh in ten years instead of twenty. The models can't tell you the cultural cost. They can tell you the biophysical trajectory."

    "Elias 'Eli' Rowan" "So, what? We wait while houses get weaker? Tell me how not to resent a court order when there's a child with water at her doorstep."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "You don't need to tell me. We both—"
    "The pendant at your collar burns warmer; you press a thumb to it without thinking. The motion grounds you, knits the anxious threads into something with shape."

    mara_kestrel "Naomi, the models matter. But they can't be a reason to delay every time the sea pounds. People can't be held hostage by 'maybe it'll be worse in ten years.' We have tools. We have neighbors. We have Rafi's maps and Grandma Hira's stories. We can design pilots that are reversible, that monitor impacts as we go."
    "Dr. Naomi: (after a long breath) 'I will help. But I will demand monitoring protocols. I will demand staged reviews. If you go unsanctioned, I cannot—' (her voice catches) '—I cannot put my name on something that will destroy habitat without accountability.'"

    "Elias 'Eli' Rowan" "There are worse things than losing faith in institutions. There's losing the people who believe in you because you promised something you couldn't deliver."

    mara_kestrel "And there are worse things than risking everything for a chance to keep them."
    "They both stand in that sentence, two sides of the same coin: ethics and urgency, calculation and faith. The night narrows to the possible harm of inaction and the palpable danger of being shut down."
    # play sound "sfx_placeholder"  # [Sound: A soft ding from Tess' comm — an incoming notice]
    hide dr_naomi_park
    hide mara_kestrel

    scene bg ch4_453e40_5 at full_bg
    show tess_omalley at left:
        zoom 0.7

    tess_omalley "Livia just tweeted—'Unauthorized works endanger public safety. Council backed by independent review.' The mayor's office is echoing it. Public opinion is swinging."

    "Rafi (spitting a laugh that's more a curse)" "She'll throw lawyers at us. She'll put up signs and cameras. She'll call in contractors. If they arrest someone tonight, they'll make martyrs of us one by one."
    "The room tilts; everything feels faster. Your pulse thuds—sharp, insistent. High arousal, low margins."
    "You move your hand over the sketch again, dark tracing under fluorescent light. Each line is a promise; every promise asks for a price. You think of the child tying knots on the promenade earlier, the"
    "shop owner who patched shutters with duct tape, Grandma Hira's hands—fingers that have kept a community from washing away."
    "Elias 'Eli' Rowan steps closer until your shoulders almost touch. He lowers his voice, the intimacy of the whisper raw with urgency."

    "Elias 'Eli' Rowan" "If we push—if we push hard—I'll be with you. But we'll lose sleep, maybe friends. We'll get dragged into court. People will be scared. We might be right, and we might end up in front of a judge explaining why we fixed a seawall with ropes."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "I know. I know the cost. I've kept a ledger in my head for months of what any of our decisions would take. But I also—' (you let the sentence hang) '—I can't watch them wait to be moved. I can't be the scientist who waits for perfect when someone needs a roof."
    "There is a brittle sound in the room—metal on wood, a muffled curse—then a silence as everyone looks at you. Your decision is a gravity well pulling all attention in."
    "The sodium lamps outside hum like a distant storm siren. Rain ticks on glass like fingers drumming an ultimatum."
    "You swallow. The pendant at your throat is hot, the metal chain stinging the skin where it rests against your collarbone. Your hand tightens around your notebook. Each name written inside is a small planet you are responsible for."
    "Everything funnels into a sharp, jagged clarity: activism will cost time, energy, maybe trust. It will also buy time for a child to sleep dry tonight."
    "You look at Eli. He looks back. The room waits. Outside, Livia’s message spreads like oil on a wave."
    "You close your eyes long enough to feel the town—the Harbor's salt breath, Grandma Hira’s stubborn warmth, Rafi's lined maps, Naomi’s cautious science—sitting heavy on your shoulders."
    "You exhale, a sound that spits rain and nerves and an outline of a plan into the damp air."
    # play music "music_placeholder"  # [Music: Crescendo—strings and percussion reach a tense peak]
    hide tess_omalley
    hide mara_kestrel

    scene bg ch4_453e40_6 at full_bg
    "You are resolute. People-first measures won't wait for perfect models."
    # [Page-Turn Moment]
    "You lift your head, the room sharpening into faces and names. The decision is not yours alone, but the room has already begun to accept that you'll be the one to set the pace. The pendant at your throat is finally still."

    scene bg ch4_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Abrupt cut to a single sustained tension note]

    scene bg ch4_453e40_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
