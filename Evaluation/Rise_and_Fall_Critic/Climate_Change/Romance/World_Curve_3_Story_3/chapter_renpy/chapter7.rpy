label chapter7:

    # [Scene: Rooftop Sanctuary | Dawn]

    scene bg ch6_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Gentle, hopeful strings with soft percussion]
    # play sound "sfx_placeholder"  # [Sound: Morning gulls, the distant clack of a pulley, neighbors' quiet chatter]
    "Narration:"
    "You wake to the smell of damp soil and coffee, the world already soft around the edges from yesterday's rain. The solar fabric above the beds glows like a skin pulled taut over possibility, and your"
    "fingers still smell faintly of salt even after an hour in the dirt. This morning is not empty of the past — the memory of sirens and shouted slogans is a salt line under everything —"
    "but the work here scrubs at that scar until it looks more like map than wound."
    "Narration:"
    "You tie your braid back the way you always do and feel the dented compass at your throat, the red thread warm where it rubs. Finn — sleeves rolled, a smear of mud on one cheek"
    "— has already set the pulley near the rain barrel. He catches your eye and grins, the kind of grin that says everything will be okay for a small, precious while."
    show finn_serrano at left:
        zoom 0.7

    finn_serrano "You left me the best rope again. Said you wanted the one with the knot you made last summer."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "Good knots, Finn. They keep people fed."

    finn_serrano "And someone to remind them to eat when they're stubborn like you."
    "Narration:"
    "His hands pass the rope to you with the casual intimacy of family. The rope is rough and warm from his grip; the scent of diesel and coffee clings to him in equal parts. Around you,"
    "neighbors tend seedlings under the solar fabric — Rosa's niece measuring pH with a borrowed strip, an old carpenter showing a teenager how to set a level on the pallet beds. The rooftop is a small"
    "world learning to be self-sufficient, scaffolded against tides you won't be able to stop on your own."
    hide finn_serrano
    hide maya_serrano

    scene bg ch6_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Hum of a small portable heater, the click of a camera shutter from Elias]
    show elias_novak at left:
        zoom 0.7

    elias_novak "You plant like you plan—quietly, with ten backups in your head."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "And you photograph like you rally—loud enough that people turn around."

    elias_novak "I turn them to look at the work, too. That's the point."
    "Narration:"
    "He brushes soil on his fingers like a badge. His warmth is steady — not the thunder of speeches, but the slow heat of someone who stays when the sky turns. The camera around his neck"
    "is scarred with stickers; he keeps catching you watching him and then looks away, a blush behind his easy grin. When you check the tide-log in your notebook, your handwriting still trembles sometimes. Here, beneath the"
    "solar fabric, your hands shake less."

    menu:
        "Show the neighbor how to splice rope":
            "You set your jaw, guiding their hands through the knot step by step. The neighbor's fingers are clumsy at first; you tighten the loop and watch confidence replace hesitation. Elias snaps a quiet photo and hums approval."
        "Let them figure it out, step in only if they ask":
            "You let them fumble for a moment, counting breaths. They patch the loop themselves, face bright with surprise. You clap softly; Elias raises his camera like a toast, proud and discreet."

    # --- merge ---
    "Dr. Hana appears mid-morning like an answer you'd scheduled for later — tablet under her arm, sleeves rolled, hair caught in a practical clip. The rooftop seems to welcome her with a little ripple; she smells faintly of antiseptic and lemon oil, a scientist who has learned to appreciate basil."
    show dr_hana_park at center:
        zoom 0.7

    dr_hana_park "The raw data from the buoy array lines up with the model. Community modular barriers decrease localized inundation in projections by a significant margin if we deploy them like this.' [taps the screen] 'Low cost. High local control. And most importantly — incremental."

    maya_serrano "Incremental makes it practical. It lets us show progress without asking for everyone to give up everything at once."

    dr_hana_park "Exactly. And your network gives me the field variance I need. The living rooftops, the water-capture systems — they all increase resilience when you combine them with properly sited modular barriers."
    "Narration:"

    "Her words have the satisfying weight of instruments clicking into place. Translation — from protest into policy language — has always felt like sleight of hand. Now she hands you charts and a short, sharp sentence" "You made your case actionable."
    # [Scene: Rosa's Café | Midday]
    hide elias_novak
    hide maya_serrano
    hide dr_hana_park

    scene bg ch6_601bcb_3 at full_bg
    # play music "music_placeholder"  # [Music: Low guitar, comforting and steady]
    # play sound "sfx_placeholder"  # [Sound: The hiss of an espresso machine, muffled conversations]
    "Narration:"
    "You call the meeting at Rosa's because this café has always been both a heart and a mouth for Saltbridge. Rosa slides a tray of scones across the table and hums the same tune she hummed"
    "when you were small. The posters from the protests hang patched on the wall like flags that have seen hard weather."
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "You kids did good. The grant—well, the council said our presentation mattered. You had them listening."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "We had evidence. Hana's numbers made our urgency legible. And people here could stand up and say what they would use the money for."

    rosa_alvarez "And didn't you make them tea after? That helps, too."
    show elias_novak at center:
        zoom 0.7

    elias_novak "Tea and stubbornness. Two local exports."
    "Narration:"
    "The municipal grant is conditional — not everything you wanted, but enough to seed pilot installations and pay community stipends for labor. When the news arrived, you felt your stomach do something you only now recognize"
    "as relief; it was loud and strange and clean. Mayor Cho's statement is cautious and kind, a public softness you did not think you'd see: recognition, praise for community leadership, an agreement to match funds if"
    "the pilot succeeds."
    hide rosa_alvarez
    hide maya_serrano
    hide elias_novak

    scene bg ch6_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Mayor Cho's voice on the café TV — calm, rehearsed, softer than it used to be]
    show mayor_lillian_cho at left:
        zoom 0.7

    mayor_lillian_cho "Saltbridge has demonstrated ingenuity and care. We will support a pilot that empowers neighborhoods and prioritizes those most at risk."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "Her tone—does that make you feel relieved or suspicious?"
    show rosa_alvarez at center:
        zoom 0.7

    rosa_alvarez "Both. Politics is a stew. But right now, the town gets tools. We work with them, not for them. That's something."
    "Narration:"
    "Noah watches from across the harbor that afternoon, the Kestrel office glass reflecting the water like a mirror. Later, he sends a concise message: meet me by the pier. You're wary — his company represents scale"
    "and compromise — but you have learned the hard way that invitations can become bridges."
    # [Scene: Harbor Pier | Late Afternoon]
    hide mayor_lillian_cho
    hide maya_serrano
    hide rosa_alvarez

    scene bg ch6_601bcb_5 at full_bg
    # play music "music_placeholder"  # [Music: A steady piano line, hopeful]
    # play sound "sfx_placeholder"  # [Sound: Boat horns faint in the distance, the slap of small waves]
    show noah_kestrel at left:
        zoom 0.7

    noah_kestrel "I've seen your plans, Maya. Dr. Hana shared the projections. You have community buy-in and a realistic pilot. My firm can provide material logistics and engineering oversight — without taking ownership. We can help you scale, not subsume."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "Why the change? You used to push full redevelopment."

    noah_kestrel "I used to think bigger fixes were the fastest way to protect people. But I lived through a place where 'bigger' meant doors closed on some folks and open for others. You reminded me what protection has to look like: practical, distributive, accountable."

    noah_kestrel "I want to help do this right."
    "Narration:"
    "He offers a palm open, not to take, but to anchor. Your chest loosens; you feel the latch in your sternum unhook a little. The harbor smells of diesel and salt and the peculiar sweetness of"
    "possibility. Noah's offer is not a white flag or truce — it is a hand extended over a plank of shared work."

    menu:
        "Accept Noah's technical oversight gratefully":
            "You nod, feeling the relief of an extra set of hands. Noah's smile is quiet approval; Elias squeezes your shoulder from behind, wordless support. The plan narrows from wish to schedule."
        "Ask for a written memorandum ensuring community control first":
            "You hold the edge of the conversation steady, asking for guarantees. Noah listens, not offended, and promises clauses and oversight. The negotiation feels grown-up and honest; Elias thumbs a note into your palm, proud."

    # --- merge ---
    "Late at night, after the formal meetings and the public statements, the two of you go over the layout one more time. Your breath fogs in the lamplight; Elias's hair keeps falling in front of his face. You tuck it back, an old, domestic motion that feels small and essential."
    # [Scene: Rooftop Sanctuary | Night — Plan-Checking]
    hide noah_kestrel
    hide maya_serrano

    scene bg ch6_601bcb_6 at full_bg
    # play music "music_placeholder"  # [Music: Warm cello and hush of night]
    # play sound "sfx_placeholder"  # [Sound: Soft laughter, the distant slap of waves]
    "Narration:"
    "Late at night, after the formal meetings and the public statements, the two of you go over the layout one more time. Your breath fogs in the lamplight; Elias's hair keeps falling in front of his face. You tuck it back, an old, domestic motion that feels small and essential."
    show elias_novak at left:
        zoom 0.7

    elias_novak "If we add these staggered berms, runoff channels will redirect into the storage beds instead of the alley."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "And if we test the material mix Hana suggested, we can cut costs by—' (you trace numbers on the margin) '—almost a third."

    elias_novak "You always do the math quietly."

    maya_serrano "Someone has to count the costs. Someone has to make sure people don't get left on the wrong side of an equation."

    elias_novak "I can be that someone with you. I'll watch. I'll run errands at two a.m. if you need me to."

    maya_serrano "Watch, not fix me."

    elias_novak "Watch, and stand with you. Not fixing. Not leading. Side-by-side."
    "Narration:"
    "There is tenderness in the smallness of that exchange — no grand promises, just the committed act of presence. Your braid swings against your neck as you set a paperweight on the plan; Elias hums, a"
    "tired but genuine sound. The rooftop is quiet enough that you can hear the town breathing: a distant generator, someone singing off-key on a street, the gulls settling down."
    hide elias_novak
    hide maya_serrano

    scene bg ch6_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: Swell into hopeful strings]
    "Narration:"
    "Days fold into a rhythm. The pilot sites begin — community labor, paid stipends, Dr. Hana's instruments blinking in the early fog. You teach a neighbor to solder a rain sensor; Finn runs up and down"
    "with buckets; Rosa organizes lunch shifts and a rota of teachers for basic plumbing. The municipal grant is unlocked in stages as milestones are met, each one celebrated at the café with coffee and slightly embarrassed"
    "applause."
    show mayor_lillian_cho at left:
        zoom 0.7

    mayor_lillian_cho "What Saltbridge has shown is not only resilience of infrastructure but resilience of spirit. We will continue to listen."
    "Narration:"
    "The town still bears its scars — warped boardwalks, a few empty storefronts — but the lines of repair show like stitches on old fabric. Where there was despair, there's now an architecture of effort. Where"
    "there was spectacle, there is now scaffolding. Hope feels like work, a muscle being exercised."
    # [Scene: Rooftop Sanctuary | Golden Morning — Weeks Later]
    hide mayor_lillian_cho

    scene bg ch6_601bcb_8 at full_bg
    # play music "music_placeholder"  # [Music: Choir-like warmth under steady piano]
    # play sound "sfx_placeholder"  # [Sound: Laughter, the clack of tools, soft applause]
    "Narration:"
    "You stand on the edge of the rooftop and look out over the harbor. Across the water the Kestrel office glints, not as a threat but as a partner in an uneasy, earned truce. Rosa passes"
    "you a mug that steams; Elias folds his arms around himself, but his face is open. Finn comes up behind you and drapes a sodden jacket over your shoulders like the simplest courtesy."
    show elias_novak at left:
        zoom 0.7

    elias_novak "We did this."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "We did this together."
    "Narration:"
    "The municipal pilot is not the end of everything. The sea is still there, patient and indifferent, and there will be more challenges; you do not pretend otherwise. But today the town has a new vocabulary"
    "for its future — modular protection, community labor funds, rooftop networks — and your name, threaded into the ledger of Saltbridge, is not only a list of plans but a list of people kept safe."
    hide elias_novak
    hide maya_serrano

    scene bg ch6_601bcb_9 at full_bg
    # play music "music_placeholder"  # [Music: Crescendo into a bright, sustained chord]
    "Narration:"
    "Your love for Elias deepens not as escape from duty but as a connective force. Nighttime plan-checking becomes a habit of shared burritos, of whispered strategies and of hands that rest together over blueprints. He is"
    "not the answer to every question — neither are you — but together you are a stubborn, practical thing: a team."
    show elias_novak at left:
        zoom 0.7

    elias_novak "Promise me one thing."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "What?"

    elias_novak "If things get hard again, we try first to listen to the town and then to each other."

    maya_serrano "Deal. And you promise to stop taking photos when I'm mid-sentence."

    elias_novak "No. Those are historical records."
    "Narration:"
    "You laugh properly, the kind that loosens your chest. Around you, people tend seedlings as if tending futures. The solar fabric flutters; the harbor light fractures into a thousand bright pieces. In the face of a"
    "relentless sea, the town has built something both fragile and formidable — a network of hands, laws tweaked by lived experience, a language of mutual aid."
    hide elias_novak
    hide maya_serrano

    scene bg ch6_601bcb_10 at full_bg
    # play music "music_placeholder"  # [Music: Fade to single piano motif, steady and warm]
    # play sound "sfx_placeholder"  # [Sound: A gull calls once, clear and unhurried]
    "Narration:"
    "When Mayor Cho announces the conditional expansion — matched funding if the pilot meets its benchmarks — there's a small thrill across the town, not just because of money but because a civic structure has bent"
    "toward equity. Noah's office sends technicians to work directly with the community teams, schedules coordinated and responsibilities clearly written. Dr. Hana publishes a brief paper with co-authorship from community members; it reads like a manifesto and"
    "an instruction manual."
    "Narration:"
    "You stand on the rooftop a long time after the crowd thins, the compass at your throat heavy and familiar. You think of the neighbor whose porch light went dark, the red thread that tied a"
    "promise to your pulse, and how the meaning of 'everything' has changed. It now includes asking for help, bargaining hard for fairness, and — sometimes — accepting the small imperfect alliances that actually protect people."

    scene bg ch6_601bcb_11 at full_bg
    # play music "music_placeholder"  # [Music: Final warm chord]
    "Narration:"
    "This is not a victory lap. It's an ongoing, stubborn beginning. You have scars and ledgers, and a list of things still to do. But the ledger is alive now with other hands writing in it. You are not alone."
    # play sound "sfx_placeholder"  # [Sound: A soft, satisfying exhale — the town's breath aligning with your own]
    # play music "music_placeholder"  # [Music: Fade Out]

    scene bg ch6_601bcb_12 at full_bg
    "THE END"
    # [GAME END]
    return
