label chapter4:

    # [Scene: The Low Row | Midday]

    scene bg ch4_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Footsteps on wooden planks, the distant thrum of machinery, a megaphone warming up]
    # play music "music_placeholder"  # [Music: Percussive, driving rhythm — urgent and hopeful]
    "You chose this. The decision that felt like a row of dominoes now sits warm under your palms: signatures, testimonies, a binder you can point to when someone asks what a neighborhood looked like when it"
    "still had a voice. The air tastes of salt and sweat and tomato-stem sharpness from the rooftop nursery sacks someone shoved down for shade. Your braid catches the light — a strip of auburn fire against"
    "the crowd — and your boots thud on the crate as you step up."
    "Rafi is already in motion, a human metronome. He hands you a stack of leaflets with a grin that doesn't quite reach his eyes — too many things to fix in too little time."
    show rafi_odeh at left:
        zoom 0.7

    rafi_odeh "Okay. Two teams on the promenade. One on the radio pitch. Lio's doing content — make it cinematic, make them feel it. Maya, you're our translator. You keep the models simple and the muscle in the message."
    "You take a breath and fold a leaflet in half, the ink smelling faintly of solvent and sun. The models sit in a waterproof tube at your feet — Dr. Sima's layered graphs, tide line projections,"
    "the wetlands map you memorized in sleepless chunks. They are technical and precise. You will make them human."
    "You climb down and move along the row, leaflets folded like small white flags, interrupting afternoon conversations with a practiced smile. Children run between legible shoelaces and patched knees; Mrs. Ortega pauses drying sea-glass necklaces to take two copies, fingers trembling when she recognizes the outline of the oyster beds."
    "Mrs. Ortega: (silent recognition)"

    "Neighbor (soft)" "My abuelo planted those beds. If they go, so do his stories."
    "You stay with her until she breathes the story into the leaflet, until the sea-mist evaporates and turns into resolve on her face. This is not a lecture. It is communion: the technical data you carry must become the language of loss and legacy."

    menu:
        "Read the model numbers, be precise":
            "You clear your throat, give them the hard numbers — projected inundation lines, economic estimates. A few listeners lean forward; others' faces flatten from numbers into distance."
        "Tell Mrs. Ortega's story instead":
            "You tell the story of the oyster beds and how the tides taught children to measure time. The crowd murmurs; someone wipes their eye. The technical diagrams will still be there later, but for now, people remember why they are fighting."

    # --- merge ---
    "The crowd's focus deepens; whether by numbers or story, attention coalesces into a plan of action."
    "You can feel the pulse rising — not panic; a high, focused sprint. Lio's camera whirs as he ducks between stalls, capturing a mural being painted across a shutter: a long-limbed woman holding a strip of marsh that becomes a child’s hand. He yells directions in half-verse."
    show lio_corvin at right:
        zoom 0.7

    lio_corvin "Make it loud! Make the color pop! Get the breeze — yeah, like that!"
    "You laugh, breathless, and cue him into the next shot: a close-up of the compass cord around your neck, tarnished and useless, and then a pan out to hands collecting signatures. Those shots will go hot on the feeds."
    # [Scene: Rooftop Nursery & Green Lab | Afternoon]
    hide rafi_odeh
    hide lio_corvin

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Bees, the soft clink of watering cans, the low murmur of neighbors debating]
    # play music "music_placeholder"  # [Music: Strings and hand percussion — urgency tempered by warmth]
    "Rafi has turned the nursery into a campaign operations center. A whiteboard lists routes, a laptop blinks a streaming chat from volunteers, and a kettle on a portable stove hisses. You stand on a low crate again, this time under a translucent dome, voice ricocheting off plastic and plant life."
    show maya_corvin at left:
        zoom 0.7

    maya_corvin "We need testimony at the hearing. We need someone who knows oysters, someone who remembers the promenade before the breakers. We need the map to speak to the faces that live on it."

    "Neighbor" "I'll talk. I can show the photos of the gardens. They'll have to look us in the eye."
    "The conversation keeps catching and unspooling. People interrupt one another, trade names, fill gaps with laughter or with the brittle whisper of fear. This is messy and beautiful; it's the sound of people claiming the right to be complicated."
    show elias_kahn at right:
        zoom 0.7

    elias_kahn "I can't be public. Mayor's guidelines. But you need this — contacts, deadlines, a cursory list of procedural pitfalls. If you file the referendum notices exactly like this, you'll keep a lot of bureaucrats from saying 'not in compliance.'"

    maya_corvin "You did this on your own time."

    elias_kahn "They don't hire people who work for free unless they want loyalty. Consider it municipal inertia in your favor.' (He forces a small smile, then becomes careful.) 'Be careful with what you promise at the hearing. They'll try to reduce our options to either/or."
    "The exchange lingers, more than the paper. He is here and not here — the 3-Check would call it complex; to you, it feels like a tether. You accept the list and fold it into your pocket, the paper warm from his touch."

    menu:
        "Use Elias's procedural list verbatim":
            "You distribute the list to the volunteers. The campaign tightens; the legal forms are filled with less error. It's efficient, less romantic — but efficient gets signatures counted."
        "Simplify the legal steps and focus on canvassing":
            "You keep the list to yourself and send people out to speak from the heart. The urgency of stories brings more faces to the tents; a few forms get messy and need fixing later."

    # --- merge ---
    "Both paths push the campaign forward — one through tightened procedure, the other through broadened outreach; each creates different immediate trade-offs."
    "Up on the dome, you pin a diagram to the wall: wetlands corridors, living levees, a scaled hybrid pilot. You translate phrases while your hands move — 'retention basin' becomes 'neighborhood sponge'; 'bypass channel' becomes 'pathway for fish and kids.' People copy the phrasing into their phones like spells."
    show rafi_odeh at center:
        zoom 0.7

    rafi_odeh "Get someone to the radio. I have Anna from 'WaveLine' on standby. They'll run a ten-minute piece if we can put a face to the data."
    "You call the little local station, trading seconds of explanation like currency. Minutes later, Lio's mural clip cuts in on the air, the camera jumping from paint to signature to a grandmother's hand tracing an oyster shell on the leaflet."
    # play sound "sfx_placeholder"  # [Sound: The tinny voice of local radio, then the swell of the viral clip]
    # play music "music_placeholder"  # [Music: Electronic beat overlays the mural footage; momentum builds]
    "Word accelerates. A neighbor posts the clip to a local stream; the clip blooms — comments, shares, local activists tagging each other. Your chest beats fast in your ribs, a bright animal pulsing in the dark of exhaustion. This is what momentum feels like."
    # [Scene: The Low Row — Street-side TV & Screens | Late Afternoon]
    hide maya_corvin
    hide elias_kahn
    hide rafi_odeh

    scene bg ch4_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A polished voiceover, the mechanical whisper of edited effects]
    # play music "music_placeholder"  # [Music: Cold, steady corporate chord]
    "Then Kai's campaign drops: glossy shots of a monolithic seawall, a voiceover about 'inevitability,' footage of engineers in pristine suits standing at neat blueprints. The ad's aesthetics are deliberate — impossible to match on a shoestring budget."

    "Camila 'Kai' Navarro" "Safety at scale is not optional."
    "Neighbors gather, hands balled into fists, mouths opening and closing like fish. The ad's radius of inevitability collides with your neighborhood's messy humanity in a few seconds of color."

    "Neighbor (angry)" "They paint protection like it's a gift. They forget it takes lives and stories to make a coastline."
    show rafi_odeh at left:
        zoom 0.7

    rafi_odeh "Their video is pretty. Our truth is louder."

    "You feel the arousal spike — not fear, not yet — but the ferocity of a clarifying storm. People shout, then laugh; someone starts a chant that turns into a call for signatures. Lio threads footage of the corporate ad into the mural clip with a snip, adding a line" "We deserve both safety and the things that make us home."
    # play music "music_placeholder"  # [Music: Percussion and brass, driving forward — hope pushing like tidewater]
    # [Scene: Rooftop Nursery & Green Lab — Community Testimonies | Early Evening]
    hide rafi_odeh

    scene bg ch4_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Stories told in breathy, urgent tones; paper rustling]
    # play music "music_placeholder"  # [Music: Crescendo, hopeful and urgent]
    "You take the mic again. One by one, neighbors step forward: an oyster fisher who names tide markers like old friends; a teacher who shows photos of field trips among the nursery's beds; Lio plays a"
    "montage — a child planting, an elder laughing. Each testimony stitches public policy to people."
    show mayor_ana_velez at left:
        zoom 0.7

    mayor_ana_velez "Maya. I've been briefed. I can see the traction. The city will convene a mediated workshop to discuss a pilot hybrid solution. I want community representation on the panel."
    "There is a catch — always a catch. But the offer is a door."
    show maya_corvin at right:
        zoom 0.7

    maya_corvin "We will come. But the panel can't be a show. We need time on the agenda, scientific consideration for the wetlands corridors, and binding language about monitoring."

    mayor_ana_velez "I expect civility and evidence. Bring both, and we will have a chance to move from protest to policy."

    "You press for specifics. The Mayor gives dates, and a tone of institutional pragmatism that rings like a bell and loosens something in your chest — a small, fierce gratitude. Elias sends a single text then" "Prep list attached. I can get you time on the dais if you keep it tight."
    "The community roars in the background. People clap, some cry, others laugh. Polls — a neighbor's tablet — flash green as a local tracker ticks up: support for a hybrid pilot climbing across precincts. Numbers don't"
    "make you cry, but they make your jaw set. The needle is moving in your favor."
    show rafi_odeh at center:
        zoom 0.7

    rafi_odeh "This is it. If we keep pushing, they have to listen. We have momentum. We make them count votes, not cash."
    "You feel the climb of arousal reach a peak you can almost see: signatures, viral clips, a municipal ear turned toward you. All of it is raw, frayed, alive."
    # play sound "sfx_placeholder"  # [Sound: A sudden gust, the first anger of storm clouds offshore; a metallic creak as solar panels shiver]
    # play music "music_placeholder"  # [Music: Rhythmic motifs accelerate — highest intensity yet]
    "You and a small team pack the binder: signatures folded and flagged, testimony schedules, a neat stack of your translated pamphlets, Elias's procedural cheat-sheet tucked between pages. The binder is heavy with other people's names and decisions. It becomes an anchor you cannot — will not — let slip."
    # [Scene: The Old Promenade | Dusk]
    hide mayor_ana_velez
    hide maya_corvin
    hide rafi_odeh

    scene bg ch4_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Waves scudding under the promenade; the whisper of raindrops starting to scatter]
    # play music "music_placeholder"  # [Music: A sustained, reverent chord that matches pounding hearts]
    "You walk the old promenade with the binder in your lap, the straps of your boots slick with seawater. The air has turned metallic and hungry; storm clouds race east. Each step echoes: wood, wet, hollow."
    "The decision clock on the municipal feed — a ribbon of public time — ticks down somewhere beyond the curve of buildings. The binder thumps against your thigh with each step, names interleaving like a chorus."
    "You feel everything at once: exhaustion, adrenaline, an incandescent hope that glows hot and stubborn beneath the skin. Tonight might not settle anything forever — it's not that kind of triumph — but it is a"
    "pivot. The city has been forced to listen. The narrative has shifted, even slightly. You let yourself receive the small, sharp pleasure of that movement."
    "A wave pushes ashore and kisses the promenade's edge; you lift your feet, laugh with a sound that is more release than joy. Lio's latest clip vibrates in your pocket; someone tagged the Mayor's office. The pages in the binder are dog-eared and beautiful."
    "You sit on the damp steps, the binder open, the signatures forming a paper tide that mirrors the ocean at your feet. The rain moves faster now, a fine curtain. You press your palm to a"
    "page, feeling the faint indent of a neighbor's signature, and you let your head tip back to watch the clouds. The campaign has been a sprint and a communion; each person you asked promised one thing:"
    "not to watch the world happen to them."
    # play music "music_placeholder"  # [Music: The percussion resolves into a breathing, steady pulse — high, alive, hanging on the edge of what comes next]
    # play sound "sfx_placeholder"  # [Sound: The city decision clock somewhere distant, a soft, inexorable tick]
    "You are wet, exhausted, and incandescent with a hope that behaves like a live wire. The mediated workshop will come, the polls will be parsed, the corporate ads will continue — but for this moment, the"
    "binder is full, the petition is real, and the Low Row's chorus has found its beat."

    scene bg ch4_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade to a single sustained note that invites forward motion]

    scene bg ch4_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
