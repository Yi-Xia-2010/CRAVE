label chapter25:

    # [Scene: New Promenade | Dawn after the Surge]

    scene bg ch13_5ceb3d_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant applause from municipal officials; the low, relentless hiss of retreating water; gulls whining]
    # play music "music_placeholder"  # [Music: Low strings, steady, a minor chord undercutting the city’s applause]
    "You stand on the edge of what the city calls safety. The promenade’s concrete is still new under your boots, its joints clean, the metal railings polished by hand — or by machines. The wind takes"
    "the salt from your hair and bites at the braid’s loose beads; your compass hangs cold against your sternum beneath your jacket, a quiet weight of memory."
    "From here you can see the arc of the Low Row: rooftops stitched with tarps, the nursery’s greenhouse domes like small moons, Lio’s murals exposed in long runs of color and grief. The seawall took the"
    "surge and held. That is the fact the city will print on glossy pamphlets and paste to billboards. That is the statistic the mayor will recite to cameras. It is also not the whole truth."
    "You listen to the applause carry across the water and taste iron at the back of your tongue. Survival arrived with a price stamped in the shadows the wall casts. You can name the losses: a"
    "bakehouse where Mrs. Ortega sold brittle empanadas, now a flattened frame; a corner clinic, its door jammed and supplies moved to a temporary tent; a mural that marked the neighborhood’s founding, peeled away by surge and"
    "heavy equipment. Each one feels like a small theft conducted in daylight."
    "You press your palm to the trefoil on your wrist without realizing you’re doing it. The skin there is cold. The gesture steadies you more than it comforts you."

    scene bg ch13_5ceb3d_2 at full_bg
    # play music "music_placeholder"  # [Music: Strings thin to a single, persistent viola line — unresolved but not frantic]
    "You know how the record will be written: an engineered victory, lives saved, infrastructure secured. You also know how this reads on the ground: a neighborhood remade into a different map. Between those two truths you live."
    # [Scene: Low Row — Temporary Relief Center | Midmorning]

    scene bg ch13_5ceb3d_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmured conversations, the whirr of a portable generator, children’s feet slapping puddled concrete]
    # play music "music_placeholder"  # [Music: Soft piano, slow, minor intervals]
    "Rafi moves like a rope through the room, efficient hands, dirt under his nails, the same patch-covered vest but his smile frayed at the edges. He hands you a thermos and then takes it back to"
    "distribute. Volunteers stream in; neighbors call out names. You step between a table of food and a board of temporary housing assignments and find Lio crouched in front of a half-finished wall of paint, working with"
    "a brush as if breath itself were paint."
    "Lio looks up and meets your eyes, and for a second the confession in his look reads simple: this is how we hold what we have. He does not stop painting."
    show lio_corvin at left:
        zoom 0.7

    lio_corvin "They said the wall was going to make things simple. Simpler isn’t the word I’d use."
    "You watch his hand tremble a little as he steadies a sweep of color."

    lio_corvin "Do you want me to make it bigger? More faces?"
    "You inhale and the room smells of wet pigment and boiling sugar. You have a dozen places you should be at and a thousand things you want to do. This, too, is part of the aftermath: triage of bodies and memory, logistics and mourning braided together."

    menu:
        "Stand with Lio and paint alongside him":
            "You grab a spare brush. The paint stains your fingers; the motion is simple, tactile, and it anchors you to the work of remembering. Lio smiles without sarcasm. He talks about names; you add one you hate losing and then another."
        "Help Rafi sort relief supplies instead":
            "You shoulder a box of blankets and move toward the distribution table. The labor is plain and urgent; someone’s nephew needs shoes, someone else needs a baby formula. The work keeps your hands busy and your head from looping on the wall's shadow."

    # --- merge ---
    "You make a choice and the room shifts around that decision; either route keeps you in the relief center, bound to the same network of grief and care."
    "Rafi notices the exchange, catches your eye, and comes over. He leans in and speaks under his breath."
    show rafi_odeh at right:
        zoom 0.7

    rafi_odeh "We’ve got families in a gym up on the third terrace. Names on the list. Mrs. Ortega asked for someone to check the bakehouse frame for salvageable ovens."
    show maya_corvin at center:
        zoom 0.7

    maya_corvin "I’ll split. Lio— —I’ll take the morning. Rafi, the ovens first. If there’s a list I can sign—"

    rafi_odeh "You never were good at standing still. Fine. Take Lio a thermos. He’ll keep the mural honest."
    "The conversation is practical and then not; grief and organization are the same cloth here, patched so tightly they bleed together."
    # [Scene: Temporary Fences and Construction Edge | Noon]
    hide lio_corvin
    hide rafi_odeh
    hide maya_corvin

    scene bg ch13_5ceb3d_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant hum of pumps; clipped radio chatter; an undercurrent of discontent, low but present]
    # play music "music_placeholder"  # [Music: A low, steady cello making the air feel thicker]
    "You follow a path wrung through the new fencing to the construction edge. The seawall’s concrete is stucco-smooth and warm from the sun. Near a truck, two workers argue in low voices — clipped, then sharp"
    "— and a woman in a pristine field suit moves against the crowd with the calm of someone used to being the pivot. Camila 'Kai' Navarro is speaking with an engineer whose shoulders are set like"
    "a man who has swallowed a bad conscience."
    "Camila 'Kai' Navarro’s mouth is the practiced smile of someone who knows what this scene will look like in print. When she sees you, she inclines her head, but there is a distance to it now:"
    "professional, efficient, the warmth that once flickered between you reduced to an economy of purpose."

    "Camila 'Kai' Navarro" "You came. Good. The monitoring arrays will be online by evening."
    show maya_corvin at left:
        zoom 0.7

    maya_corvin "They were rushed. The engineers—"

    "Camila 'Kai' Navarro" "We accelerated schedules. There were trade-offs. You know how these things are."
    "You watch her eyes for a moment. At public briefings they are steel; in a back corridor they are anything but. You want to ask if she feels the hollow where the old promenade used to be, or if the numbers have taught her how to sleep at night."

    "Camila 'Kai' Navarro" "Some of the crew voiced concerns. A small work stoppage this morning. They wanted more testing cycles."
    "She reaches into her jacket and slides an encrypted printout across an aluminum flap of the barrier. The print is small and dense — names, timestamps, terse notes. Inside it reads like protest: missed checks, compressed timetables, a foreman’s message saying 'pressure is political, not technical.'"

    "Camila 'Kai' Navarro" "I pushed because lives were on the line, but I didn’t ignore their notes. I filed them. We will make time to address them. Publicly, the narrative is that the wall held. Privately, there are people who feel we asked too much."
    "For a breath neither of you speak. The machines breathe around you both."

    maya_corvin "You asked them to rush."

    "Camila 'Kai' Navarro" "I asked for speed and oversight. I asked for both. They’re not mutually exclusive."
    "You study her. The porcelain pendant at her throat — a small talisman you once asked about and were answered with silence — catches the light and flashes like a small, delicate admission."

    "Camila 'Kai' Navarro" "There are engineers tonight who doubt the process. There are others who are relieved. Both things can be true at once."
    "You should say something decisive; instead you feel the thinness of a single human word in the face of institutional force."

    menu:
        "Confront Kai about the human cost":
            "Your voice tightens. You say what you have been holding — the ovens, the clinic, Lio’s murals. Kai listens; her jaw sets. She does not apologize, but she does not look away."
        "Keep your voice measured, ask about oversight details":
            "You ask how oversight will be enforced. Kai answers with timetables and watch committees and municipal slots. The answers are competent, and not comforting."

    # --- merge ---
    "Both lines of engagement leave you with more information and more responsibility; whether you spoke bluntly or technically, the consequence is the same — you become more entangled in the oversight that will follow."

    "Camila 'Kai' Navarro" "We will have independent monitors on-site. Mayor Velez has agreed to periodic audits. Elias is overseeing the municipal oversight board."
    "You feel the name land like a small stone. Elias Kahn — steady, diplomatic Elias Kahn — now the city's official face of the oversight you had asked for in a different life. The news does not make your chest lighter."
    # [Scene: Makeshift Municipal Office — Near the Promenade | Midafternoon]
    hide maya_corvin

    scene bg ch13_5ceb3d_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Tinny voicemail beeps, a distant PA announcement, the occasional clink of ceramic from a donated mug]
    # play music "music_placeholder"  # [Music: Minor strings, slow and steady; a heartbeat beneath conversation]
    "You find Elias Kahn at a folding table, sleeves rolled, a neat stack of field notes beside him. He looks tired in a way that isn’t physical alone — his face carries the soft erosion of"
    "compromise. When he sees you, his expression opens, then tightens; he wants to reach, but the reach is more the offer of company than touch."
    show elias_kahn at left:
        zoom 0.7

    elias_kahn "They called me in to formalize the oversight. It’s… a big post."
    "You nod. You have watched him threading compromise into policy for years; now he is the policy. It should be a cause for relief."
    show maya_corvin at right:
        zoom 0.7

    maya_corvin "You could have done this from the start."

    elias_kahn "From the start, I was in technical committees. But this — this is a position that gives me teeth. I can allocate auditors, I can order safety holds, I can force transparency."
    "He speaks like someone trying to persuade both you and himself. You want to want that to be enough."

    maya_corvin "Or it pulls you away."

    elias_kahn "Maybe. There will be more meetings. More travel for hearings. They want someone the corporate delegates and the community trust. They asked me."
    "You feel the space between the two of you stretch, not with anger but with different latitudes. There is a practical honesty in his words that grazes a hard place in your chest."

    maya_corvin "Will you still come to the nursery next week? Lio says the seedlings need the first pruning."

    elias_kahn "I will do my best. But I can’t promise the same Saturdays. The role will demand time."
    "The pronoun lands like a small death. You remember how you both used to walk the boardwalk at dusk and talk about designs that honored people. Those evenings now feel like a book you once read."

    elias_kahn "This isn’t me abandoning the grassroots. If anything, it’s the opposite — I can protect it from within."
    "You want to believe him. The words are plausible, warm, and policy-shaped. They do not dispel the tiny certainty that policy becomes a different kind of life, one that requires a different kind of absence."
    "Elias Kahn reaches across and lays a hand near yours on the table, not pressing but present."

    elias_kahn "Stay with me in the room when you can. Keep calling me out where I forget. That’s how we keep each other honest."
    "You look at the hand, the worn callus where he always taps his pen. You want to promise everything and know you cannot. The conversation dissolves into list-making and times — careful, municipal things."
    # [Scene: New Promenade — Edge of Evening]
    hide elias_kahn
    hide maya_corvin

    scene bg ch13_5ceb3d_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Exhausted cheers from distant municipal crews; the low tide pulling like a long breath; the murmur of a small memorial gathering]
    # play music "music_placeholder"  # [Music: Sparse piano, descending, then an unresolved sustain]
    "Night comes so quickly that it feels dishonest. There is a small vigil on the promenade: candles in jars, a folding chair with a stack of photographs, neighbors murmuring names into the dark. Lio stands before"
    "his mural, paint-splattered hoodie heavy, the colors swollen in the low light. Rafi moves through the crowd distributing hot soup."
    "You stand and watch, trefoil pressed to your skin. Each name they read is a small hammer: a business that shuttered, a room that will not be rented again, a tradition that will reframe itself into"
    "memory. The wall kept the water out, measured and auditable; the water’s absence is not a triumph so much as a reconfiguration."
    "Camila 'Kai' Navarro approaches from the high ground, hands clasped in front of her — the posture of someone arriving to bear a balance sheet. When she sees you at the edge of the vigil she hesitates, then offers a single, complex look."

    "Camila 'Kai' Navarro" "They’ll say we saved the city."
    show maya_corvin at left:
        zoom 0.7

    maya_corvin "Saved some things. Rewrote others."

    "Camila 'Kai' Navarro" "Words are always partial."
    "She does not try to take your hand. There is no attempt at reconciliation more tender than a shared catalog of what was done and what was lost. It is a transactional closeness, the kind built on mutual necessity and careful distance."
    "Elias Kahn arrives later, slow, and stands a few feet away. He watches the mural, the candles, the faces, and in his amber eyes you read a fatigue that is not only from long hours. There"
    "is a wall inside him, too, built of calendars and meeting minutes and the slow grind of policy. He looks over at you and offers a small, private smile that does not bridge the space between"
    "your lives anymore."
    show elias_kahn at right:
        zoom 0.7

    elias_kahn "We can keep corridors alive. We can write audits into contracts. We can make the funding last if we’re careful."

    maya_corvin "You can write them. People will still lose things."
    "He nods because he knows the calculus as well as you do. His answer is a promise and an acknowledgment; both are hollow in different ways. You do not argue. The argument has been had and folded into statutes. What remains is living with those statutes."
    show rafi_odeh at center:
        zoom 0.7

    rafi_odeh "We have to make sure the displaced get homes that aren’t temporary forever. Social bonds aren’t supposed to be portable."
    hide maya_corvin
    show lio_corvin at left:
        zoom 0.7

    lio_corvin "They paint what’s left. They make the place again."
    "You look at the mural — faces of neighbors, hands joined, the old promenade rendered in hues that won’t be in any municipal brochure. It is a map of what matters in a language the wall cannot translate."
    "You breathe out and the sound seems small, private. The night smells of tar and the sea; the trefoil is a cold weight at your wrist. Your resolve tightens, not the bright flame that once spurred"
    "you to mass meetings but a steady, stubborn ember: vigilance. You will check permits, audit reports, read the small print and the big print. You will keep naming what was lost. You will stand with Lio"
    "painting murals and with Rafi distributing soup. Survival, you understand now, is daily labor more than a single engineering victory."
    "Everything is quieter than victory. The city will tell its story; you will keep telling the other one."
    hide elias_kahn
    hide rafi_odeh
    hide lio_corvin

    scene bg ch13_5ceb3d_7 at full_bg
    # play music "music_placeholder"  # [Music: A low, lingering cello note, unresolved]
    # [Page-Turn Moment]
    "You walk the promenade one last time before the lights go down and picture the months ahead: audits, listening sessions, the slow, dogged work of stitching policy to practice. You think of Elias Kahn in municipal"
    "halls you may rarely visit; you think of Camila 'Kai' Navarro at her consoles, commanding efficiency that wore a different kind of cost; you think of Lio and Rafi and the mural that will age under"
    "salt and sun. The moment is not one of defeat alone — there is survival here — but it is threaded through with sorrow and a knowledge that the ground has shifted beneath your feet. You"
    "will not stop. You may not win in the way you once imagined. But vigilance will be the work you choose."

    scene bg ch13_5ceb3d_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    scene bg ch13_5ceb3d_9 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter35
    return
