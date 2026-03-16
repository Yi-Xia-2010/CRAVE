label chapter9:

    # [Scene: Raised Main Street | Morning]

    scene bg ch9_3be532_1 at full_bg
    # play music "music_placeholder"  # [Music: Bright strings with a steady, uplifting pulse]
    # play sound "sfx_placeholder"  # [Sound: Distant drills, the soft clack of boots on boardwalk planks, laughter mixing with the caw of gulls]
    "You wake into the day with grit under your nails and the smell of tar and sea in your throat. The raised street outside your workshop is half-finished but already feels like an idea turned solid:"
    "a promise that kept its shape when it met wind and tide. People are moving like a current along it — Jun and a crew tightening a storefront awning, Riv chalking a children’s hopscotch on the"
    "new concrete lip, a nurse from the temporary clinic carrying boxes labeled 'Pediatrics' with a ridiculous, triumphant grin."
    "Your jacket is still speckled with concrete dust. When you step outside, the wind presses a salt-sweet lift against the back of your neck, and the town greets you in small, ordinary ways: a wave from"
    "Amina as she talks with a contractor, the clink of Elias Maren's drone control as he checks a living-shoreline sensor down by the inlet. The raised streets hum with the low, efficient industry of people who"
    "have decided to keep going."
    "You tighten the braid on your wrist without thinking — the way your mother taught you to loop a knot when decisions needed holding in place. This is what the last weeks have become: clauses, meetings,"
    "late-night revisions, mornings that begin at the sightline between sea and street. It was messy. It was human. It is working."

    scene bg ch9_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Water lapping, the gentle slap of kelp, Elias Maren's voice counting off samples]
    show elias_maren at left:
        zoom 0.7

    elias_maren "We seeded another row last night. The hold looks promising in the shallow patch by Dock Twelve."
    show mika_hoshino at right:
        zoom 0.7

    mika_hoshino "Any signs of recruitment yet? Young urchins? Fish?"

    elias_maren "A few—more than I expected. The microhabitat took faster where the substrate was coarser. It’s small, but it's making a difference already."
    "He speaks slowly, like he’s mapping currents with words. You can see the optimism in him; it’s not blithe, it’s measured. He folds his hands around a small vial of kelp spores, and the light through it looks like a tiny green dawn."
    "Soren Voss approaches from the opposite end of the pocket, his coat still carrying that neat, engineered cut. There is a softness to his shoulders today that betrays how exhausted he must be; the construction bids,"
    "the finance meetings, the press briefings — they lean into him, but the first raised curb seems to ease something in his stance."
    show soren_voss at center:
        zoom 0.7

    soren_voss "They lined the curbs with cedar like you suggested. It keeps the salt from eating the seams as quickly."

    mika_hoshino "You listened."

    soren_voss "You asked clearly. I learned to listen where it mattered. Credit where due."
    "He says it smooth as glass, and inside that glass there’s more than the surface. You remember the long nights of negotiating clauses and the lines you pushed for: stewardship seats, transparent audits, a community veto."
    "Whether your insistence recreated binding language or whether the plan moved so quickly that the watchful eyes of the town became the safeguard, either way, the exchange — of concern, of demands, of careful phrasing —"
    "made the streets you walk on possible."
    hide elias_maren
    show jun_park at left:
        zoom 0.7

    jun_park "Come on, boss — ribbon-cutting rehearsal, or you gonna make us wing it?"

    mika_hoshino "I'm only here for the free food."
    "Jun’s laugh is solid and familiar. He carries a bucket of pebbles that will go into a planter — little weights that the kids will later rearrange into patterns they swear are maps."

    menu:
        "Help Jun plant the pebbles":
            "You crouch and fit small stones between roots, the motion steadying. Jun's grunt beside you is a background drum; the planter feels like a miniature harbor in your hands."
        "Walk the living shoreline with Elias":
            "You follow Elias along the water's edge, talking low about recruitment rates and the way light hits at dawn. The damp reeds brush your palms; hope smells like wet earth and salt."

    # --- merge ---
    "Continue"
    "The festival preparations are all at once meticulous and raucous — banners painted with slogans both practical and whimsical, a stage borrowed from the warehouse, a long table where Riv and his crew assemble jars of"
    "pickled clams and spiced seaweed. Children run beneath scaffoldings as if they were made for secret passage. The town moves like something newly healed trying out its limbs."
    # [Scene: Raised Street Market | Afternoon]
    hide mika_hoshino
    hide soren_voss
    hide jun_park

    scene bg ch9_3be532_3 at full_bg
    # play music "music_placeholder"  # [Music: Warm acoustic guitar layered with low brass]
    # play sound "sfx_placeholder"  # [Sound: Chop of knives, chatter, the distant whir of a concrete saw still being used in the background]
    "Amina threads her fingers through a stack of proposals but keeps looking up at the crowd. The mayor wears the expression of someone who has carried a thousand small losses and still found a currency of"
    "hope to spend. She spots you and comes over, the scent of citrus from the market wafting between you."
    show mayor_amina_bakar at left:
        zoom 0.7

    mayor_amina_bakar "You held people together. You carried the talks through when tempers flared. The oversight board — they asked for you to sit as their liaison."
    show mika_hoshino at right:
        zoom 0.7

    mika_hoshino "Me?"

    mayor_amina_bakar "You always keep the practical end in mind. We need that. And the town wants someone who knows the docks beyond the plans on a screen."
    "You think about saying no. You think about the hours, about the guilt that pools behind your ribs when you imagine failing. But when you look out and see Jun sealing a shop's new raised threshold"
    "with a practiced tuck of mortar, when Elias Maren kneels to show a kid how to plant a kelp plug, the thought of stepping back looks less like relief and more like slackening the rope that"
    "holds everyone."

    mika_hoshino "Then I’ll do it. I’ll be there, and I’ll drag whatever receipts we need."
    "Soren Voss, who has been watching the exchange with an unreadable expression, moves closer as if to stand in the light you're both sharing."
    show soren_voss at center:
        zoom 0.7

    soren_voss "You did something most planners couldn't: you gave a project a face that people trust. That makes all the difference."

    mika_hoshino "You made it move, Soren. I helped make sure it didn't forget why it moved."
    "He looks at you then in a way that asks for the full truth without saying so. For a moment his strategic polish slips and you glimpse someone who carried a private map of the future and learned to redraw it with other hands."

    menu:
        "Accept Soren's offer to walk the boardwalk with him later":
            "You nod. Later, the two of you step along the new railing, talking low. He asks about your mother and you tell him a small, true memory — and he listens, not as a planner logging facts but as someone who is beginning to hold them."
        "Tell Soren you'll catch up with him after checking the clinic":
            "You promise to find him later. He tilts his head, a little disappointed, but he understands. You tuck the moment into the day's long ledger and move on to the clinic's queue."

    # --- merge ---
    "Continue"
    "Elias Maren arrives with a small tray of kelp seedlings, and when he hands you one you feel the damp, green weight in your palm like a compact continuation of everything you care for."
    hide mayor_amina_bakar
    show elias_maren at left:
        zoom 0.7

    elias_maren "You okay with how the kelp plots are being integrated into the walls?"

    mika_hoshino "They're tighter than I expected. Jun's crew did a good job setting placement into the foundation."

    elias_maren "It'll help the nearshore food web. And —' [he hesitates, the current of his words pulling toward something personal] '— it helps me, too. Seeing people wrap around this like they've wrapped around a lifeline."
    "You both stand with the seedlings between you, the midday light knifing through condensate on a nearby tarp. For a second the noise of the festival drops into a private channel: the press of optimism that is patient and stubborn and, for you, quietly urgent."

    elias_maren "You made room for science and for people. That balance isn't easy."

    mika_hoshino "You made a lot of room yourself, Elias. You convinced folks that the kelp could be more than algae — that it could be work and food and a bit of insurance."

    elias_maren "We did it together."
    "The afternoon slides toward evening. The raised curb is now a place for people to lean, for children to trace tide marks with chalk, for elders to tell the newer faces the old stories as if"
    "they were regardable things to be loved into being. The clinic doors are open now, the first raised thresholds proven stable, the temporary signs 'Emergency Response Center' replaced with 'Community Health — Open.' Small clinics bring"
    "small laughter: bandaged fingers being teased, a baby offered a ribbon, a volunteer insisting on a second cup of tea."
    # [Scene: Festival Nightfall | Dusk]
    hide mika_hoshino
    hide soren_voss
    hide elias_maren

    scene bg ch9_3be532_4 at full_bg
    # play music "music_placeholder"  # [Music: A hopeful choir pad under gentle piano]
    # play sound "sfx_placeholder"  # [Sound: A distant drumline begins, mingled with sea breeze and the pop of bottles being opened]
    "A central table bears a carved ribbon. Soren Voss steps forward to speak, and the crowd hushes with that particular silence that rests only when there is something to be held in common. He does not"
    "put on the salesman’s patter. He looks at the town first, and then at you — and you feel the room tether to whatever passes between you."
    show soren_voss at left:
        zoom 0.7

    soren_voss "This isn't a monument to one plan or one person. It's an arrival point and a promise: that we'll keep watching, that we'll build with the people who live here, and that we'll be willing to change course if the tide demands it."
    show mayor_amina_bakar at right:
        zoom 0.7

    mayor_amina_bakar "And the oversight board is seated. Mika Hoshino — you lead the board's liaison role. Your voice will be the town's voice in the governance meetings."
    show mika_hoshino at center:
        zoom 0.7

    mika_hoshino "I'll do my best. That's all I can promise."
    "Elias Maren joins you at the edge of the crowd, his hand finding the small vial of kelp at his neck. Jun and Riv are flanking the table, grinning like boys who have stolen someone's thunder"
    "and kept the pie. You look at the raised street stretched beneath lantern light and you feel an odd, precise happiness — not the sharp peak of victory, but the steady warmth of work that found"
    "its shape."
    "The ribbon is cut. Children scream and run beneath the fluttering banners. The drumline kicks in and people begin to dance in pairs and small knots. Food moves like a tide along the tables. You taste"
    "salt and fried fish and the unexpected sweetness of a honeyed seaweed tart. Laughter is the main instrument of the night."
    "Later, when the crowd thins and lanterns throw long, patient shadows, you stand on the new curb and look out to sea. The living shoreline pockets glitter under the moon's lowered light — small islands of"
    "structured nature stitched to engineered seams. In the water, kelp blades drift like hands waving. The town looks good from here: ragged, human, repaired enough to be brave."
    "Soren Voss is beside you, but he doesn’t crowd. He watches the town with that pale, blueprint gaze softened by something like awe."

    soren_voss "You made this less abstract. You kept it honest."

    mika_hoshino "You made it move. I kept the people from being erased in the motion."

    soren_voss "That's the beginning of some kind of partnership, isn't it? Practical and a little… complicated."

    mika_hoshino "Everything worth doing is both."
    "He looks at you with an expression that is not quite confession and not quite calculation — something in between that might be the outline of trust. You think of the many small meetings, the clauses"
    "you fought for, the nights you worried you were asking for too much. You think of Elias Maren tending kelp under damp lights and Jun's hands patching a broken step. You think of your mother’s key"
    "and how often you've used it since she left you the workshop. All of those hands braided into the rope that holds Atera steady tonight."
    "Elias Maren appears with a thermos and two paper cups, handing you one like an offering."
    hide soren_voss
    show elias_maren at left:
        zoom 0.7

    elias_maren "To the first raised street. To people who keep showing up."

    mika_hoshino "To showing up."
    "There is a quiet, enough like a vow that you tuck it into your chest. Around you the lanterns sway. Somewhere nearby, Riv starts a small, off-key song and Jun teaches a kid to hammer a"
    "safe rhythm on a tin can. The town that kept breathing through the floods has set itself to a new cadence: ongoing work with moments of celebration threaded through."
    hide mayor_amina_bakar
    show soren_voss at right:
        zoom 0.7

    soren_voss "Mika Hoshino— if we keep doing this, the model could be something other towns look to. That—' [he gestures at the street, at the people] '—that would be your mark as much as mine."

    mika_hoshino "I don't want a mark so much as a thing that keeps people here, keeps livelihoods running, and keeps our kids from learning the flood lines on pictures."

    soren_voss "Then we'll keep building it, together. Not flawless. Not finished. Us."
    "You want to debate him on the word 'together' because cooperation has had so many different faces in your life. Instead you press your thumb to the small scar on your wrist — a memory of rope and deck and grit — and let the moment stand."
    hide mika_hoshino
    hide elias_maren
    hide soren_voss

    scene bg ch9_3be532_5 at full_bg
    # play music "music_placeholder"  # [Music: The strings swell into a steady, rising motif that holds warmth rather than finality]
    # play sound "sfx_placeholder"  # [Sound: The mingled ambient — tide, distant chatter, the rustle of kelp]
    "You do not believe this is an end. You never did. The work ahead is long; audits will be demanded, politics will twinge, kelp may fail in a season and the town will have to plant"
    "anew. But tonight you stand on a raised curb with a hand-warm cup, and the future looks like a tool you could learn to use."
    "Elias Maren bumps your shoulder, an intimate, unhurried punctuation."
    show elias_maren at left:
        zoom 0.7

    elias_maren "No matter what, you helped make this town a place worth staying in."
    show mika_hoshino at right:
        zoom 0.7

    mika_hoshino "We all did. It's not mine, Soren, or Elias's. It’s ours."
    "Soren Voss inclines his head. Elias Maren's gaze is soft and steady. Jun calls from the other end of the street for one last song. You laugh, and the sound feels like belonging."
    "You think of the braided string on your wrist and loop it once more. You think of the dented key in your pocket. You think of the people who will come after you, who will inherit"
    "both the raised streets and the responsibility to watch them. You are not done. You are part of something that is going to take more hands, more stubborn nights, more small repairs — and that steadies"
    "you in the best way."
    hide elias_maren
    hide mika_hoshino

    scene bg ch9_3be532_6 at full_bg
    # play music "music_placeholder"  # [Music: Single piano note, held, then a gentle chord resolving upward]
    # play sound "sfx_placeholder"  # [Sound: The tide, slow and constant]
    "This is a beginning that keeps happening. The festival will end; the work will continue. People will argue and reconcile and file reports and plant kelp and argue again. And you — you will keep showing up."
    # [Scene: Raised Street | Night — Final Frame]

    scene bg ch9_3be532_7 at full_bg
    # play music "music_placeholder"  # [Music: Warm strings fade into a hopeful whisper]
    # play sound "sfx_placeholder"  # [Sound: Night gulls, distant soft laughter]
    "You breathe in the sea and the city-scent of hot food. You let the night fold around the promise of work that will never be complete but will always be shared. Your hands are steady. Your"
    "heart is quieter than it was — not at rest, but steady with resolve. The town is not saved, not finally; it is, for the moment, protected, patched, and more equal to its future than it"
    "was yesterday."
    "You walk back to your workshop, the raised curb steady beneath your boots. Behind you, lanterns bob and people begin tidying up, sharing tasks as naturally as they share stories. Ahead, there are contracts to read"
    "and meetings to keep and kelp seedlings to mark on tide maps. There will be nights where your willingness will be tested, where you will wonder whether you have given too much or not enough. But"
    "tonight, by the lamplight and the water, you decide — quietly and with the sort of stubbornness that builds anything worthwhile — to stay."

    scene bg ch9_3be532_8 at full_bg
    "THE END"
    # [GAME END]
    return
