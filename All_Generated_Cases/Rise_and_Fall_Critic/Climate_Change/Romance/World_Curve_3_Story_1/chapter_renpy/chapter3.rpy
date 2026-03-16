label chapter3:

    # [Scene: Broken Pier | Morning]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, mournful strings; distant gull calls]
    # play sound "sfx_placeholder"  # [Sound: Waves battering wood, loose boards creaking]
    "You walk the length of what remains of the pier because you have to see it with your own eyes. The morning light is thin, the kind that doesn't warm so much as reveal. Salt skins"
    "your lips; a spray rises off the sea and settles like dust on your jacket. The broken planks make a jagged rhythm under your boots; when you lean on the railing, the metal is cold enough"
    "to tug the warmth from your palm."
    "Your thumb finds the braided bracelet at your wrist and holds on out of habit and as a talisman. You flip open your tablet once, then close it again—the message count is a tide you don't"
    "want to measure here, not yet. The pier feels like proof of a ledger you cannot balance: one storm, one season, one council vote away from rewriting everything you thought was steady."
    "You listen for the town in the sounds around you: a dog barking far inland, the soft thud of a dockworker stacking crates, and underneath it the mechanical heartbeat of the harbor—generators, winches, someone starting an engine. The sea keeps writing its margin."
    # [Scene: Tom's Shop | Mid-Morning]

    scene bg ch3_98c6f2_2 at full_bg
    # play music "music_placeholder"  # [Music: Off-key harmonica underbed; a clock with a stubborn tick]
    # play sound "sfx_placeholder"  # [Sound: Bench lathe whirring, the clink of a wrench]
    "The bell above the door clangs and Tom looks up with the kind of face weathered into expectations. Heat and oil hang in the air like an old jacket. You breathe in the metallic tang and it feels like home and like accusation at once."
    show tomas_tom_alvarez at left:
        zoom 0.7

    tomas_tom_alvarez "You look like you haven't slept, sis."
    "(You let out a sound that answers without numbers.)"
    show iris_alvarez at right:
        zoom 0.7

    iris_alvarez "We lost more of the promenade."
    "(He sets down a rag, then gestures vaguely toward the window where the pier's remains slice the horizon.)"

    tomas_tom_alvarez "I was at the marina before daylight. Lina's already tallying half a dozen boats that won't be out for a week. How bad?"
    "(He doesn't rush to fill in the blanks. He figures you'll see the map when you need to.)"

    tomas_tom_alvarez "It's bad enough that Ravi wants the council in a day. Marin Voss's talking regional money."
    "You watch him. His hands are thick with practice and with the small habitual gentleness he saved for dogs and roped knots. There is an unspoken ledger between you two: everything the town asks of you, he absorbs in muscle and shop-time."

    tomas_tom_alvarez "You gonna stand there and do the paperwork, or are you gonna get out there and tell folks how to stack sandbags?"
    "(The question pins you because the two options are not exclusive in your chest.)"

    iris_alvarez "I have ideas. I have numbers. But I can't—"
    "(You swallow a protest that tastes like guilt.)"

    iris_alvarez "—I can't do it alone."

    tomas_tom_alvarez "Good. Don't then. Most things around here don't get done by lone wolves."
    "His voice is steady, but there's a tremor in his eyes — the practical fear of someone who measures loss in equipment and bills. You remember last year's repair jobs, the nights he didn't go home. That memory makes your chest ache in a specific, private way."

    tomas_tom_alvarez "You gonna stand there and do the paperwork, or are you gonna get out there and tell folks how to stack sandbags?"

    menu:
        "Ask Tom to make a quick prototype brace":
            "Tom squints, then grins despite himself. 'Give me an hour and some scrap. We'll see if the old hands can keep your data honest.' He moves to the bench already planning cuts."
        "Refuse hands-on work and push to the meeting":
            "Tom's smile thins. 'Okay, then make them listen. If you let someone else run this, watch the fine print.' He taps the map on the table with a grease-dark finger."

    # --- merge ---
    "Continue in town planning and mobilization scenes."
    # [Scene: Lina Harrow's Marina | Late Morning]
    hide tomas_tom_alvarez
    hide iris_alvarez

    scene bg ch3_98c6f2_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slap of a loose tarp, a distant radio static]
    # play music "music_placeholder"  # [Music: Sparse piano notes, melancholy]
    "Lina's marina smells of diesel and salt and something else — the copper of money and the grit of salvage. She counts losses like you count stitches: precise and a little weary."
    show lina_harrow at left:
        zoom 0.7

    lina_harrow "I keep thinking of the festival lot. That government's money could mean relocation for a dozen stalls and a tax hit for me. If they take the shoreline, who pays for my slips?"
    "(You want to tell her your hybrid could protect the lot, or that community-built modules could be installed at a fraction of the projected municipal cost. But you also know that words don't plug leaks.)"
    show iris_alvarez at right:
        zoom 0.7

    iris_alvarez "We're at a crossroads. Marin Voss has a plan with regional funding, but it will require redevelopment of some low-lying blocks."
    "Lina: (Her laugh is brief and brittle.) 'Redevelop. They love that word. It translates to 'we take what we want and call it progress.''"
    "She looks at you like she expects you to pick a side—like everyone else. You feel the gravity of it: a market stall returned to full bustle, or a row of empty foundations dotted with plaques. The smell of tar and scraped paint sits in your nose."

    lina_harrow "If you side with them, Iris, don't expect me to help stack a single modular barrier for free."

    iris_alvarez "I don't want to close anyone's shop."

    lina_harrow "Then don't be surprised when the town chooses what's easiest for the budget."
    "Her stance is a kind of grief. You cannot console it with data; only with consequence."
    # [Scene: Greenhouse Commons — Before the Forum | Early Afternoon]
    hide lina_harrow
    hide iris_alvarez

    scene bg ch3_98c6f2_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmured conversations, the rustle of seed packets]
    # play music "music_placeholder"  # [Music: Understated, thin strings with a slow pulse]
    "The Commons smells of damp soil and tea and, underneath, the staleness of too many meetings. People gather in knots, speaking under their breath, hands unsure of where to land. Etta moves between them with the quiet of someone who has learned how to carry other people's weight."
    "You look at the map pinned to the central board—your own annotated lines riding over Ravi's scrawl and Marin Voss's clean overlays. The torn edge from yesterday's map still clings to the corner like a stubborn memory."
    "Kai Nakamura is here early, leaning on a pallet bench, camera hanging and fingers stained with ink. He grins when he sees you, but there's an undercurrent: urgent, impatient."
    show kai_nakamura at left:
        zoom 0.7

    kai_nakamura "They started without us, of course. Someone thought a town meeting was a good idea and didn't wait for the DIY brigade."
    "(You laugh, and it cracks)"
    show iris_alvarez at right:
        zoom 0.7

    iris_alvarez "It feels like half the town is either furious or terrified."

    kai_nakamura "Makes for attendance. Look—I've brought prototypes."
    "(He unfolds a small, elegant sketch of a modular barrier that can be assembled from reclaimed timber and plastic drums. It looks hopeful; it looks possible.)"

    kai_nakamura "We can train people. We can move faster than Marin Voss's procurement schedule."
    "You study his drawings. They are optimistic: simple joints, quick assembly, an emphasis on materials the town already has. You want to believe it because part of you loves the idea of neighbors building together, hands learning the same moves, shared sweat as social glue."

    kai_nakamura "If we start now, municipal approval can follow or catch up later. But you know the risk—no guaranteed funding, and if a storm hits before we finish..."
    "(He doesn't finish. The sentence hangs, an image of half-constructed defenses washing away.)"
    "Kai Nakamura's eyes search yours for a different kind of permission, one that isn't just professional endorsement but personal trust. He tilts his head, all easy charm and the raw edge beneath it."
    "Marin Voss arrives polished, the kind of presence the council expects: slate trench coat, tablet case like a brief fortress. They step into the Commons with a practiced smile that doesn't reach the eyes the way"
    "it used to. You try to read them; 'complex' is the label that keeps its neutrality, and it's the only honest one. Their fingers linger on the municipal map before they meet your gaze."
    show marin_voss at center:
        zoom 0.7

    marin_voss "We can secure regional funds. There are strings, yes. The funding requires redevelopment of certain low-lying blocks to justify long-term investment. It's not ideal, but it scales and it protects the harbor's backbone."

    iris_alvarez "Redevelopment of the festival lot?"

    marin_voss "Some areas, yes. We can negotiate retention clauses for cultural sites, but there will be trade-offs."
    "Their voice is even, rehearsed for meetings and headlines. You watch them because what they don't say is as loud as anything they do. The silence between you contains policy, possibility, and a history you cannot fully trace."
    "Etta sidles up, dirt under her nails and a look that says she has memory and no time for rhetoric."
    hide kai_nakamura
    show etta_bloom at left:
        zoom 0.7

    etta_bloom "Money's a tool. It cuts both ways. You can't hand it over whole and expect the town to remain the same. But you also can't rebuild without it."
    "Her rasp is honest. She looks at you as if she is weighing whether you are a safe place to land the town's next generation of hope."

    menu:
        "Take Kai aside to ask about training timelines":
            "Kai Nakamura's face lights up. 'Two weekends for the first cohort, if we pull in Tom and the marina crew. We'll need a lot of hands, but that's the point.' He starts sketching out a rough calendar on a napkin."
        "Approach Marin to ask about what 'redevelopment' really entails":
            "Marin Voss's composure tightens. 'It's a phased plan. We prioritize the structural nodes and work out cultural preservation clauses. It won't be painless, but it will be fundable.' They fold their tablet shut neatly, the motion a clear boundary."

    # --- merge ---
    "Participants reconvene for the community forum."
    # [Scene: Greenhouse Commons — Community Forum | Mid-Afternoon]
    hide iris_alvarez
    hide marin_voss
    hide etta_bloom

    scene bg ch3_98c6f2_5 at full_bg
    # play music "music_placeholder"  # [Music: Low cello, intermittent gust sounds]
    # play sound "sfx_placeholder"  # [Sound: Murmurs rise and fall, a chair scraped hard against concrete]
    "You stand at the front because people look at you like an anchor—because you are one of the few who tries to speak both data and affection in the same breath. The room tightens when Marin"
    "Voss speaks, polite and municipal, then loosens again when Kai Nakamura answers, warm and insurgent. Lina's jaw is tight in the back. Tom sits center-right, arms folded, watching the town like it's a boat he might"
    "have to shove off a lee shore."
    show marin_voss at left:
        zoom 0.7

    marin_voss "Regional funding requires a comprehensive risk mitigation plan. It includes structural reinforcement of critical points and redevelopment of vulnerable parcels to ensure long-term viability."
    show kai_nakamura at right:
        zoom 0.7

    kai_nakamura "And if the town builds parallel capacity—modular barriers, community-run gardens, rooftop absorbers—then we can distribute the risk and keep ownership local. Funding is important, but autonomy matters too."
    "Marin Voss: (They incline their head toward you, an invitation and a test.) 'Ms. Alvarez, your assessment?'"
    "(You feel the weight of every glance. Your data runs through your mind: erosion rates, cost-per-meter for different defenses, the social toll of displacement. You imagine Etta's hands in soil, Lina's ledger, Tom bent over a"
    "hull. The numbers say hybrid gives the best chance of preserving both shoreline and culture, but hybrid is hard—politically and practically.)"
    show iris_alvarez at center:
        zoom 0.7

    iris_alvarez "My models suggest a hybrid approach—targeted municipal reinforcement where the structural backbone is critical, combined with community-built buffer systems and rooftop resiliency to reduce load on those nodes."

    kai_nakamura "That could work. It means we get funding where we need it fast, and we protect the neighborhood's agency where we can. But it needs coordination—timelines, shared procurement."
    "Marin Voss: (Their reply is quick, measured.) 'Coordination means oversight. Oversight means the municipality will require compliance protocols. That may feel like top-down control.'"

    iris_alvarez "I don't want control. I want durable protection and community stewardship."

    "A man in the audience stands up, voice cracking with fear" "If we wait for some hybrid to be sweet-talked into existence, will the next storm take someone's home? We need action now."

    "Another voice—older, gravelled—cuts in" "And if we hand our land to developers 'for the long term,' will there be any place left for the festival? For us?"
    "The room becomes a sea of small storms: fear, fury, bargaining. You feel each one as if it's your own skin being pinched."

    marin_voss "We can negotiate cultural retention clauses. We can prioritize spaces like the festival lot in early phases."

    kai_nakamura "Or we can start building now, show a working model, and make procurement chase us because it's already proven."
    "Your internal monologue tightens: every concession will have teeth. Every grassroots victory will require blood and nights you won't get back. Leading a hybrid means you'll be the hinge—where two different pressures meet—and hinges sometimes snap under repeated stress."
    "Marin Voss studies you with a look that is complicated and unreadable; it contains calculation and a memory of a conversation you never had. Kai Nakamura's posture is expectant and a little wounded—he's asking you for"
    "a vote of faith that you haven't given yet. Lina's face in the crowd is hard as flint; Tom's hands are planted between his knees like he's bracing a hull for impact."
    "You can feel the town's options narrowing like a lens. The air tastes like the metallic promise of rain."
    "Your throat is dry. The map on the projector blurs at the edges as you imagine the lists of people who will applaud and the ones who will curse you. The grade of this decision isn't"
    "measured in personal success; it's measured in whether the festival tent survives, whether a single shopfront remains, whether a child's memory of the pier is of splintered wood or of a repaired boardwalk and neighbor-led murals."
    "You take a breath. The room holds it with you."
    hide marin_voss
    hide kai_nakamura
    hide iris_alvarez

    scene bg ch3_98c6f2_6 at full_bg
    # play music "music_placeholder"  # [Music: Strings swell then recede into a hush]
    "You realize what you must do next is choose how to speak your plan into being. You could cast your lot with Kai Nakamura and the town's labor, endorse Marin Voss's quick-but-compromising funding, or attempt to marshal both into a single, fragile course."
    "You feel the drop—the town's options slimming and your shoulders getting heavier."

    jump chapter4
    return
