label chapter2:

    # [Scene: Saltwood Community Hall | Evening]

    scene bg ch2_c4ca42_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, steady hum — minor-key strings, patient but taut]
    # play sound "sfx_placeholder"  # [Sound: Murmur of voices, the scrape of chairs, a soft drizzle tapping the hall’s windows]
    "You step fully into the room and the air hits you: coffee, salt-stung sweat, and the faint metallic tang of too many handheld radios. Your field notebook lies open on the nearest table like a set"
    "of prayers — living-dune cross sections, marsh restoration timelines, volunteer rosters, sketches of planted berms. The pages smell faintly of damp paper and your thumb-smudged graphite."
    "Mayor Jerome Hale moves through the room, a damp scarf thrown around his neck, folders tucked under one arm. He smiles with the kind of curved politeness you learned to read as 'I have to be all things to all people.' His voice reaches you when he passes."
    show mayor_jerome_hale at left:
        zoom 0.7

    mayor_jerome_hale "Maya — good to see you. We need you clear and sharp tonight. There will be reporters on the line if Elena's backers press."
    "You swallow and feel the brass of the tide-watch in your pocket. The warmth is small and private; it steadies a pulse that is already trying to sprint."
    "Aiden Koa arrives like a tide returning: salt-stiff navy canvas jacket, hands stuffed in patched oilskins, eyes moving across the room until they find you. He gives you a look—protective, impatient, two syllables of warning without"
    "sound. You catch the lift of his mouth as he nods once, and that little motion steadies you more than the watch does."
    show aiden_koa at right:
        zoom 0.7

    aiden_koa "You look like you rehearsed the whole walk over, Serrin. Don't let them steamroll the people."
    "You offer him a half smile. He doesn't ask the question you avoid: what will it mean if the seawall goes up; who will lose access to the quay; which nets will come up empty."
    hide mayor_jerome_hale
    hide aiden_koa

    scene bg ch2_c4ca42_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Slide click; a thin electronic ping when Elena gestures]
    show dr_elena_park at left:
        zoom 0.7

    dr_elena_park "Immediate, engineered barriers are the fastest way to prevent loss of life and property. Our model is proven in other regions. With private investment, we can have physical protection in two construction seasons."
    "Her cadence is crisp and hollow in the hall's warm light. It sounds dangerously like comfort. You feel your chest tighten; 'fast' and 'proven' rub against the lived memory of last winter's roaring flood and the mud where the Miller house used to be."
    "You stand and make your way to the table. Nyla is already feeding you last-minute figures from her tablet — projected erosion rates, economic models showing the co-op's expected income over five years if the wall is built, and worst-case ecologic impacts."
    show nyla_torres at right:
        zoom 0.7

    nyla_torres "If the wall cuts access at low tide, the fishers lose seasonal grounds — that's a 32 Percentage projected income drop for us in year one. The marsh retreat accelerates erosion inland by a meter a year in some models."
    "You look down at a cross-section: the living dune you sketch, rooted with marram grass and seeded for resilience, contrasted with Elena's concrete segments. Numbers on the tablet glow like small alarms. Your mouth feels dry."
    "There is a part of you that wants to throw the tablet across the room and another that wants to show every figure until the room understands what is being traded."

    menu:
        "Place the cross-section at the center of the table":
            "You set the page down, fingers splayed, and your voice finds the low register you use with the town. 'This is what will grow back if we protect it ourselves,' you say, tracing the dune line. A murmur runs through the hall — some nod, some purse their lips."
        "Lean on Nyla's tablet and challenge Elena's timeline":
            "You lean in, tapping a projected stat. 'Two seasons is a fiction in our weather; construction on that scale will be delayed by storms, permits, and—' Elena cuts in, cool and precise, and the room tilts toward technicalities instead of losses."

    # --- merge ---
    "You choose a tone somewhere between, because neither showy gesture nor clinical argument will settle this room tonight. You speak, but the first few sentences come out smaller than you practiced; the room fills them so you push harder."
    show maya_serrin at center:
        zoom 0.7

    maya_serrin "I am not arguing against protection. I'm arguing for who decides what 'protection' means. Living shorelines work with tides and species that keep our sands and reeds in place. We can design modest, hybrid structures now and scale them — with the community maintaining access, with jobs for local fishers and volunteers. We don't have to be forced into a single suit of armor that changes the coastline forever."

    dr_elena_park "Ms. Serrin, with all due respect, what you describe takes decades to establish at scale and depends on variable ecological responses. People need dry houses next storm season. My firm can secure federal matching funds if the town commits to an engineered approach today."
    hide dr_elena_park
    show mayor_jerome_hale at left:
        zoom 0.7

    mayor_jerome_hale "Elena has donors ready; matching funds make this politically palatable for the council. I have to consider the budget and the optics. If the grant doesn't push, we may lose both options."
    "The room tenses. A woman whose porch was undercut last winter grips a thermos so hard the cardboard creaks."

    "Elderly Homeowner" "My daughter's children sleep in the spare room in the back because the front of our house leans. What do you propose we do tonight while you figure growth plans?"
    "Your throat closes. You hear Old Man Cala's voice in your head — the slow cadence of someone who remembers when the estuary fed half our town, and of dunes that used to be broad and soft."
    hide nyla_torres
    show old_man_cala at right:
        zoom 0.7

    old_man_cala "We've always learned the water. We don't bar it and call it safe. I am not a scientist, but I know the sea forgets concrete and remembers life."
    "You meet Aiden Koa's eyes and he stands up before you finish. He moves not to the podium but to where some of the fishers sit, rolling his shoulders like someone bracing for a shove."
    hide maya_serrin
    show aiden_koa at center:
        zoom 0.7

    aiden_koa "If you seal off access, Elena, you might keep water out of their basements — but you'll keep boats out of their hands. You make the sea private. How is that protecting us?"
    hide mayor_jerome_hale
    show dr_elena_park at left:
        zoom 0.7

    dr_elena_park "Mr. Koa, this isn't about making the sea private. It's about preventing catastrophe. The design includes community ramps at scheduled intervals."

    aiden_koa "Scheduled intervals don't catch a sudden spring run. They don't account for the old cycles we still fish. You can't schedule a livelihood."
    "The back-and-forth opens like a seam. Voices rise, not shrill but raw. Mayor Hale tries to mediate, hands pressed together, an old habit of diplomacy."
    hide old_man_cala
    show mayor_jerome_hale at right:
        zoom 0.7

    mayor_jerome_hale "Please — we've all heard both sides. We can table this and revisit in the morning. We have to finish the stakeholder conference call; there's a lot at stake."
    "You feel the room fragment: someone starts to clap in agreement, someone else hisses in outrage. Prayerful glances shoot toward Old Man Cala and then fall back to you, to Elena, to Jerome. The hum of"
    "the projector sounds suddenly intrusive, a small machinery heartbeat in a room that wants an answer like a wound wants bandaging."

    "Nyla leans in, urgent and clinical" "Maya, if we delay, erosion models show an extra—"
    "Nyla is cut off by the Mayor raising his hand, voice thin with the strain of trying to hold multiple futures in one face."

    mayor_jerome_hale "We can't make an irreversible commitment tonight. We will bring this to a vote at ten tomorrow. Please, everyone — let’s reconvene then."
    "The declaration lands with a dull thud in your chest: tomorrow. The word becomes a taut wire stretched across the room. It's both relief and a new kind of torture. Delay buys time but also gives"
    "power to the loudest, the richest, the most certain. It births a night for second-guessing."

    menu:
        "Stay after to talk quietly with the fishers":
            "You linger as people filter out; a few fishers come close, lowering their voices. You listen more than you speak, making notes at the margins of your notebook as Nyla and Aiden trade plans. The weight of promises presses in, but the smallness of these shared plans feels slightly like a hearth."
        "Follow Elena to her projector and ask for specifics":
            "You trail Elena to the front, forcing a technical exchange that cuts into her polished pitch. She answers with risk numbers and contingency clauses; the language is precise and unmoved. It feels like bargaining with steel."

    # --- merge ---
    "You stay and collect what you can — names of people who will speak tomorrow, a list of concerns about access and livelihoods, the small, human wounds that won't read on a grant application. Aiden and"
    "Nyla sketch a plan to be at the quay at dawn with nets and cameras to document access points. You scribble enrollment rosters for volunteers who will help seed dune plantings if you can buy time."
    hide aiden_koa
    hide dr_elena_park
    hide mayor_jerome_hale

    scene bg ch2_c4ca42_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rain outside swells; the hall's acoustics make each departing footstep too loud]
    "You step out into the narrow lane and inhale the night. The boardwalk calls like a memory of wood and salt. Old planks groan under your boots as you choose the path away from the brittle"
    "warmth of the hall. The dusk settles heavy around the marsh: a green-tinged mist, marsh reeds bowing like folks in prayer."
    # [Scene: Abandoned Boardwalk | Dusk]

    scene bg ch2_c4ca42_4 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano — single notes echo with each step, creating a fragile cadence]
    # play sound "sfx_placeholder"  # [Sound: Boards creak; distant gull calls; the ocean hisses rhythmically]
    "You walk slowly, the meeting replaying behind your eyes like a sequence of failed stitches. Each exchange—Elena's polished promises, Aiden's blunt loyalty, Nyla's urgent numbers—resonates against the boards. The tide breathes up and down; it does"
    "not care for committees, for grants, or for reconciliations. The future feels like a drawer pulled open to reveal not one option but a scattering of delicate, breakable pieces."
    "Your internal voice tightens into a question that has been underneath every sentence you prepared: what are you willing to trade to buy someone else’s calm tonight? Which lives are invisible if the corridor of access is sealed? The doubt is a hard pebble lodged under your tongue."
    "You stop near a warped plank that used to be a favorite spot for children to fling stones. You press your palm to the railing; it is slick with salt, the grain of the wood standing like fossilized lines of weather."
    "A howl of a dog far down the shore reminds you that the town is itself a living thing made of people and habits, not only of grant matrices and engineering reports. The meeting's postponement feels"
    "less like mercy and more like a countdown. Tomorrow is not a reset; it is a weighting."
    "You think of the Miller house, of Old Man Cala's stories, of the smell of damp wool in Aiden Koa's jacket. You think of the volunteers who will come at dawn because they still believe in"
    "being neighbors. You think of the models Nyla fed you, numbers that look like quiet avalanches when you arrange them against human schedules."
    "The sound of the tide is steady, indifferent; there is a cruelty to that steadiness. Your chest tightens further until each breath is a manual task, deliberate and small."
    "You know, with the same certainty that tide charts give you, that a choice tomorrow will define whose lives count."
    # play music "music_placeholder"  # [Music: The piano holds a single, unresolved chord — patient, heavy]

    scene bg ch2_c4ca42_5 at full_bg
    "The night presses in. The decision waits."

    scene bg ch2_c4ca42_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
