label chapter7:

    # [Scene: Rally Site — Access Road | Morning]

    scene bg ch6_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A rising roar of voices, shouted slogans, the thump of a news van generator, gulls wheeling. The tide murmurs against pilings like distant applause.]
    # play music "music_placeholder"  # [Music: High-energy strings and brass — urgent, triumphant]
    "Narration:"
    "You remember the tide that morning like someone holding a breath and letting it go. Everything hums — the cold at your cheeks, the damp rope in your gloved hands, the way the crowd leans together"
    "as if to become a single, unbreakable thing. National media lenses angle at faces you know by name and by the small histories they carry: Mrs. Ortega with her fishing hat, Jamal with a child's watercolor"
    "tied to his chest, the teenagers who learned about erosion in high school and came with shovels."
    "Lito stands two people down, chest smeared with marsh mud, grin wide enough to crack the worry out of him. Amaya's scarf is damp; she wipes her eyes with the back of her hand and smiles"
    "so hard it hurts — a good hurt. Your notebook is tucked inside your jacket, tide maps folded into a neat square; it feels less like paper and more like a talisman."
    "You can feel the press of history in the crowd — a pressure that doesn't crush but clarifies. People don't chant for the sake of noise; they chant because they've measured loss and counted absence, and refuse to let another map redraw their names."
    show lito_reyes at left:
        zoom 0.7

    lito_reyes "You did this, Maya. You dragged half the neighborhood out of bed and into this ridiculous sunrise."
    "He tries to sound light. His hands shake a little."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "You came because you wanted to. Because we needed you."
    "You keep your voice low; it steadies him, steadies you."
    show amaya_chen at center:
        zoom 0.7

    amaya_chen "They're rolling live in two minutes. Rowan's in the mayor's office with the packet. If Sofía goes through with the pause, it's because the data and the crowd both say yes."
    "Her words fall between you like flint and kindling."
    hide lito_reyes
    show professor_rowan_hale at left:
        zoom 0.7

    professor_rowan_hale "The model shows the incremental benefit of living shore elements at a neighborhood scale. It's not just ecology — it's reduced wave force, maintained fisheries, and longer-term savings over seawall-only approaches."
    "He taps a tablet; his voice is the slow, deliberate cadence of someone who has spent a life making small facts big enough to matter."
    "Narration:"
    "The cameras find you. The microphone approaches like a small, hot comet. Your pulse spikes — not with fear but with the bright, terrible joy of seeing community resolve become visible. Every shout, every flag, every"
    "mud-streaked face sharpens into a single motion: this is the hour you planned for. This is the hour you and everyone here spent nights mapping and mornings planting and afternoons arguing until your throat went raw."

    menu:
        "Step forward and address the cameras":
            "You plant both feet, lift your chin, and the microphone takes your voice. You speak for the marsh, for mouths that work the water, for those who fear eviction more than storms. The words come urgent, precise; people nod and the noise becomes a tide that carries your sentence forward."
        "Let Amaya take the lead":
            "You stay back and watch as Amaya moves into the light; she speaks with a fervor that makes the camera chew up her sentences. Your throat loosens with pride and the crowd bends toward her cadence, a choir warming to a conductor."

    # --- merge ---
    "Narrative continues."
    # [Scene: Town Hall — Mayor's Office & Press Corridor | Late Morning]
    hide maya_reyes
    hide amaya_chen
    hide professor_rowan_hale

    scene bg ch6_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Clustered questions from reporters, a microphone squeal, the distant chant from the access road.]
    # play music "music_placeholder"  # [Music: Percussive brass and strings; an exultant, urgent motif]
    "Narration:"
    "Inside the Town Hall the air is warmer but charged. Mayor Sofía's eyes sweep the assembled — the legal team, Camille's clean-suited liaison in the back, Rowan standing with mud flecked on his coat, Lito's jaw"
    "still set in defiance through a smile. The room smells of coffee, wet wool, and the dry antiseptic of municipal process. This is where petitions become policy, where pressure meets procedure."
    show mayor_sofa_lvarez at left:
        zoom 0.7

    mayor_sofa_lvarez "I've heard the testimony. I've seen the footage. I've read Professor Hale's recommendations and the legal assessments. Today, I'm pausing the Duval permit process pending a phased pilot for living-shore restoration developed with community input."
    "Her voice steadies the room like a hand on a wheel. Flashbulbs pop."
    "Narration:"
    "The words land like thunder that brings rain — immediate, reshaping. Around you, people exhale as if they'd been holding water in their lungs. Amaya laughs; Lito punches his palm into his other hand, mud flying."
    "Rowan's eyes are bright with something like relief and mischief combined — an old man who remembers a long fight finally turning a corner."
    "Camille Duval stands at the edge of the press pool, immaculate despite the drizzle. Her expression is a study in controlled outrage; she steps forward — not to gloat or retreat — but to remind the city that legal engines are longer-lived than the flash of a morning announcement."
    show camille_duval at right:
        zoom 0.7

    camille_duval "This pause is an administrative tool, Mayor. Let us be clear: Duval Enterprises will pursue every legal avenue afforded."
    "Her voice is crisp, unyielding; there's no personal venom, only the precise inevitability of a corporation set in motion."
    show maya_reyes at center:
        zoom 0.7

    maya_reyes "We know the law can be long, but the people's permission is essential, and the ecology will not wait until lawsuit calendars clear."
    "Your sentence lands with the stubbornness of everyone who has waded in cold water to hold the line."

    mayor_sofa_lvarez "We will convene a working group. Rowan, you'll co-chair with community representatives. We'll commission Elias' modular pilot designs to a public bid prioritizing local crews. This is about protecting homes and livelihoods, not profits alone."
    "She sighs, steadying the plan."
    hide mayor_sofa_lvarez
    show elias_stone at left:
        zoom 0.7

    elias_stone "I'll make sure the designs are buildable by the folks who live here. Modular, repairable, with ecology at the center — not accessory to it."
    "He looks at you; the look is steady, part apology, part promise."
    "Narration:"
    "The crowd outside swells when the windows rattle with the Mayor's words. News feeds light up. Camille's PR shimmer begins to fade under the weight of live testimony, mud-streaked faces, and the tangible sight of citizens occupying the very threshold of the marsh. It matters more than slick brochures."

    menu:
        "Step up to thank the mayor publicly":
            "You step to the microphone, voice catching on the last syllable then smoothing out. 'This pause is for the future of our children, of fishermen and fish, of a living shoreline.' Your sentence lands with warmth; the press scribbles and the crowd outside roars approval."
        "Find Lito and hold him close before the crowd gets louder":
            "You slip through the press and grip Lito's shoulder. He squeezes back, mud on both hands, and for a heartbeat the future is not policy but flesh — your brother, steady and real."

    # --- merge ---
    "Narrative continues."
    # [Scene: Tidal Fringe Marsh — Midday Planting Ceremony | Noon]
    hide camille_duval
    hide maya_reyes
    hide elias_stone

    scene bg ch6_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rhythmic dig of shovels, low chants turning to songs, children laughing. Distant traffic hum filtered through gull cries.]
    # play music "music_placeholder"  # [Music: A fuller chorus; swelling strings underscore joy and exertion]
    "Narration:"
    "You plant the first ceremonial reed with hands that know how to place a seed and how to place a promise. Around you, neighbors drop sea glass into the rootball like offerings — shards smoothed by"
    "a hundred tides, now embedded in soil as testimony. Elias kneels next to you, sleeves mud-speckled, ink smudges in his satchel wet from travel and rain — his sketches now a thing being called 'pilot funded'"
    "instead of 'sketches in a bag.'"
    show elias_stone at left:
        zoom 0.7

    elias_stone "Your sea glass makes everything look like an art installation."
    "He brushes a shard into the earth with his thumb; his fingers are rough and precise."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Your modular joints are what'll let people fix what the storms try to break. Not to mention you drew them like a man trying to keep his hands clean."
    "You tease, but your voice is thick."

    elias_stone "I learned from you. If we're building something that lasts, it has to be something people can touch and understand. And fix."
    "He meets your eyes, and the world shrinks to the span between the two of you — tidal and immediate."
    show professor_rowan_hale at center:
        zoom 0.7

    professor_rowan_hale "Make sure we record the method. Each planting is data and ceremony. We'll need both."
    "He winks at a volunteer with a camera; even the old scientist cannot resist the pageantry of communal labor."
    "Narration:"
    "The planting becomes music: shovels striking, laughter, the slap of wet soil. Camille watches from a distance, a lawyerly shadow. She speaks into a phone, voice low, professional. Her retreat into legal channels is not a"
    "defeat so much as a shift in the field of play — expected, harrowing, but smaller now against this chorus."
    hide elias_stone
    show amaya_chen at left:
        zoom 0.7

    amaya_chen "This is what they couldn't buy: people who love this place enough to make it again and again."
    "Her eyes shine; she is both organizer and worshiper of this fragile ecosystem."
    "Narration:"
    "You feel something in you uncoil. The guilt you've carried — for storms, for losses, for not doing enough sooner — loosens into something that can be handed over. Elias' fingers find yours as you both"
    "press the reed into the earth. There's no dramatic pause, only the simple fact of connection: two hands meeting to steady a shared action."

    menu:
        "Say a few words for the ceremony":
            "You clear your throat and speak, voice scattering at first then steadying as faces turn. 'For the marsh that fed us, for the children who will learn it — we plant to remember and to protect.' The crowd quiets, then bursts into applause."
        "Stay silent and let the reed speak for you":
            "You kneel, press the reed into the soil, and let silence do the naming. Around you, others create sound: a drum, a child's shout. Silence becomes its own kind of loudness."

    # --- merge ---
    "Narrative continues."
    # [Scene: Boardwalk — Dusk]
    hide maya_reyes
    hide professor_rowan_hale
    hide amaya_chen

    scene bg ch6_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft conversation, the hiss of kettle steam, distant city murmurs settling into night. A single gull cries as if to punctuate the day.]
    # play music "music_placeholder"  # [Music: Gentle, warm strings with a steady heartbeat percussion — intimacy after triumph]
    "Narration:"
    "Later, when the crowd thins and the placards are folded like paper boats, you and Elias sit on the wet boardwalk. The thermos between you is warm; the metal is rough against his palm. His fingers"
    "find yours not with the fever of the morning but with the quiet insistence of something chosen."
    show elias_stone at left:
        zoom 0.7

    elias_stone "You held the line today. You were... unstoppable."
    "He studies you, trying to measure the right proportion of praise and truth."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "I couldn't have done it without everyone. Without you."
    "The sentence is straightforward, but it carries the weight of nights you spent cross-referencing tide maps and elbowing through committee meetings."

    elias_stone "We adapted the designs on the go. The funding is there, the mayor signed the pilot — but the real work begins now. Teaching locals to build and repair, sourcing materials ethically, keeping control in hands that live here."
    "He pauses, a small, rueful smile. 'And building something that can be mended when it breaks. Like people.'"
    "Narration:"
    "You laugh — a sharp little sound that melts into a quiet. Guilt, once a heavy, private stone in your chest, has changed shape; it is now shared ballast. It doesn't disappear, but it sits between"
    "you as purpose: a promise to instruct and to shoulder, to accept help and to give it. The warmth of Elias' hand around yours is not an erasure of the past; it is a tether to"
    "the future you will make together."
    "Lito wanders by, nods in a way that says everything without saying anything, then heads to help pack tools. Amaya approaches with a thermos refill and a band of small, improvised sea-glass bracelets for the project's youth crew; she insists you both take one."
    show amaya_chen at center:
        zoom 0.7

    amaya_chen "So you two are actually going to keep doing this? Show people how to build? Train crews?"
    "She grins. Her energy refuses to let the moment become merely sentimental."

    elias_stone "Yes. We teach. We scale carefully. We fight the lawsuits with permits and public records and better, cheaper options that communities prefer."
    "He squeezes your fingers. 'And we make sure the work is done by the people who live here.'"

    maya_reyes "We'll keep building. We'll teach. We'll get the kids to design some of the modules."
    "The plan feels enormous and immediate at once — the very thing you rehearsed for in crowded rooms and muddy trenches."
    "Narration:"
    "The marsh will still be vulnerable. Storms will come; some things will be lost. But the victory today is honest: not a clean, perfect cure, but a reordering that prioritizes life, repair, and the people who"
    "will wake at dawn to fix what the night took. You feel the braided promise of love and labor tighten into a rope you can carry forward."

    elias_stone "I don't want to promise forever. I can't. But I promise this: I'm here. We build together. When it's meaty and messy and beautiful, I'll be at your side."
    "He leans his forehead against yours for a breath."

    maya_reyes "Then let's stop pretending we have to carry it alone."
    "You press your thumb to his, as if sealing plans on a blueprint."
    "Narration:"
    "The boardwalk creaks like an old, contented thing. The thermos is almost empty; the sky moves toward indigo. Somewhere, a reporter files a piece titled 'Living Shore Wins Small Victory,' and the headline is both modest and vast."
    "You look out over the marsh: reeds tremble, water catches a sliver of last light, and the planted reed you and Elias wedged into the ground stands small but adamant. Around it, people move — fixing, planning, laughing, bickering, promising. The future will need hands. There are hands enough."
    "You let the feeling come: not the end of struggle, but a contained, fierce joy. The blockade held. The city listened. A pilot will begin. Camille will fight in the courts; you expect as much. But"
    "today the people held a place together and turned a corporation's ledger into a different kind of accounting — one that counts time in tides and in children's futures."
    "Narration:"
    "You are no longer carrying the fight alone. Guilt has unwound into shared resolve. Love and work braid into something you can lift. You tuck your notebook back in its pocket, thumb over the worn maps,"
    "and for the first time in a long while, you let yourself imagine a small, stubborn future that can be built — plank by plank, reed by reed, hand in hand."
    hide elias_stone
    hide maya_reyes
    hide amaya_chen

    scene bg ch6_f99e88_5 at full_bg
    # play music "music_placeholder"  # [Music: Strings swell into a gentle final chord, then settle into a soft, sustained note.]

    scene bg ch6_f99e88_6 at full_bg
    "THE END"
    # [GAME END]
    return
