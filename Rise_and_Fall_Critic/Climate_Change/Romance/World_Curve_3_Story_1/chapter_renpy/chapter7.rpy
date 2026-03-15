label chapter7:

    # [Scene: Municipal Hall | Late Afternoon]

    scene bg ch6_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm strings with a steady, optimistic pulse]
    # play sound "sfx_placeholder"  # [Sound: Low murmur of conversations, the click of a pen, distant traffic running through puddled streets]
    "You stand at the edge of the long conference table, the memorandum between hands that smell faintly of printer toner and sea salt. The room has the peculiar aftertaste of decisions — coffee gone cold in"
    "paper cups, paperwork shuffled into neat piles, and the soft exhale of people who have just shouldered something heavy and survived it."
    "Marin Voss slides the slim tablet back across the table and looks up. Their eyes are steady, pale as the sea on an overcast morning. There is a slight looseness at one corner of their mouth"
    "that, in any other time, you might have misread as indifference. Today it reads like understanding."
    show marin_voss at left:
        zoom 0.7

    marin_voss "We couldn't guarantee everything, Iris. But this staged enforcement — the modular certification, the maintenance schedules, the emergency funds — it gives the promenade a fighting chance. It keeps Lina's businesses from being bulldozed, and it buys the community the breathing room you asked for."
    show iris_alvarez at right:
        zoom 0.7

    iris_alvarez "It's not perfect.' Your voice is low, to keep the tremor out of it. 'But it lets people keep their livelihoods and gives Tom room to scale the fittings. It keeps the heart of the promenade intact."
    "Ravi leans forward from the end of the table, fingers steepled, relief and the hint of exhaustion scoring his features. He set the funding line into motion; you can see the small victory in the loosened shoulders he hides so carefully."
    show ravi_singh at center:
        zoom 0.7

    ravi_singh "The regional bond came through for the emergency tranche. It's conditional and measured, but it's real. We'll audit and report — keep everyone honest and accountable."
    "The pen moves. Marin Voss signs with a practiced, efficient motion. For a second the only sound is the scratch of ink and a distant gull muffled by the rain. When they look up you meet"
    "their gaze, and something unspoken passes: a small nod that isn't performative — it's private and precise."
    "You feel the weight in your throat unspool a little."

    menu:
        "Reach out and clasp Marin's hand":
            "You close the distance on instinct and take Marin's hand. It's warm, slightly callused at the thumb from work you don't ask about. Marin gives a small, almost-astonished smile when your fingers tighten. The room seems to exhale with you."
        "Step back and offer a calm smile":
            "You keep your hands folded, letting the professional space remain. Your smile is steady and open; Marin inclines their head in return. The agreement rests between you like a contract signed by both courage and compromise."

    # --- merge ---
    "The meeting continues with the agreement settled."

    marin_voss "We negotiated for what mattered, Iris. For the promenade, for the shops, for the maintenance corps. Thank you — for pushing us to find the middle ground."
    "You watch as Lina steps forward, boots scuffing damp tile, harbor-scented and direct. Her waterproof vest still has a smear of rope grease from the docks. She crosses the room like someone who has measured storms and docklines her whole life."
    hide marin_voss
    show lina_harrow at left:
        zoom 0.7

    lina_harrow "I told my crew we'd take the maintenance shift. They'll keep the modular joints inspected after storm cycles. If the town supports materials and Tom keeps making those fittings to spec, we'll be the first line."
    "Tom is there too, broad-shouldered and looking both smaller and larger at once in the municipal light. He smells of oil and wet wood, and when he speaks, his voice carries the sort of plain weight that calms people."
    hide iris_alvarez
    show tomas_tom_alvarez at right:
        zoom 0.7

    tomas_tom_alvarez "I'll expand the shop hours. We'll run an extra shift and standardize the fittings. Kai—if you need volunteers to patch at odd hours, tell me and I'll show up the next morning with a coffee pot."
    "Kai Nakamura, leaning against a far wall with the soft residue of sawdust and blueprint ink on his sleeves, looks at you with that grin that somehow always arrives after a day of impossible work. He pushes his beanie back with one hand, revealing hair damp from the rain."
    hide ravi_singh
    show kai_nakamura at center:
        zoom 0.7

    kai_nakamura "Nobody's leaving anyone to do all the work alone. We iterate, we learn, we tighten the seams."
    hide lina_harrow
    show iris_alvarez at left:
        zoom 0.7

    iris_alvarez "We keep the town's character and bring the resilience up to code — together. That was always the point."
    "The conversation rounds and flows: technical clarifications, a promise from Ravi to publish a timeline, Lina outlining her roster rotation, Marin Voss asking for specific inspection frequencies, Tom sketching adjustments on a napkin. Each exchange is"
    "human and messy — bargaining for materials, for hours, for trust — but each closes with agreement rather than argument. The municipal hall, which the day before had seemed a place of gridlines and budgets, feels,"
    "for the first time in months, like a place where compromise and care can meet."
    hide tomas_tom_alvarez
    hide kai_nakamura
    hide iris_alvarez

    scene bg ch6_4001e7_2 at full_bg
    # play music "music_placeholder"  # [Music: Gentle piano and plucked guitars, an upward sweep]
    # play sound "sfx_placeholder"  # [Sound: Squeak of repaired planks, low laughter, the distant slap of small waves]
    "Outside, the rain has eased. The promenade glints with damp boards and repair work stretching into the twilight. Volunteers trade tools and jokes; someone plays a battered radio, and a local song carries small warmth across"
    "the harbor. Etta's old terracotta pots line a newly stabilized planter, soil dark and rich, promising green for summer."
    "You walk the repaired length, fingers brushing the boards, noting new bolts that shine like deliberate stitches. The pier doesn't look the same it did before the storm — some sections are newer, some shored with patched pieces — but there's a coherent path now, a patchwork that works."
    "Tom catches up to you, hands still smelling of tar and brass. He leans on the railing and looks out over the water as if measuring depth with his eyes."
    show tomas_tom_alvarez at left:
        zoom 0.7

    tomas_tom_alvarez "We did what we could, kid."
    show iris_alvarez at right:
        zoom 0.7

    iris_alvarez "We did. You did."

    tomas_tom_alvarez "Make sure you eat tomorrow, alright? You're running on fumes and guilt."
    "You laugh, a short, grateful sound. 'I'll let Kai make me a terrible breakfast. It's tradition.'"

    tomas_tom_alvarez "Good. Someone ought to suffer for you to keep working."

    menu:
        "Tell Tom you'll slow down tonight":
            "You promise, and the lie tastes sweet. Tom's shoulder press is a benediction — practical, rough, and exactly what you need. The harbor light softens, and you feel less alone with your responsibility."
        "Say nothing and keep walking":
            "You shake your head and keep moving, hands in pockets. Tom watches you go with that half-worry half-understanding look; you feel the tug of duty pull you onward but also the warmth of the moment you left behind."

    # --- merge ---
    "The scene moves to the repaired pier at dusk."
    # [Scene: Repaired Pier | Dusk]
    hide tomas_tom_alvarez
    hide iris_alvarez

    scene bg ch6_4001e7_3 at full_bg
    # play music "music_placeholder"  # [Music: Lush strings rising into a hopeful chord]
    # play sound "sfx_placeholder"  # [Sound: Soft creak of wood, distant gulls, a thread of conversation below]
    "You and Kai Nakamura sit on the edge of the repaired length of pier, feet dangling over boards that still smell faintly of resin and salt. His hands are stained with ink and tar; he pulls"
    "one thumb absentmindedly along the frayed edge of his beanie. The repairs behind you hum with the low contentment of work well-begun — the town's voices carried back across the water in easy waves."
    show kai_nakamura at left:
        zoom 0.7

    kai_nakamura "You did good in there. You made them see it wasn't either-or."
    show iris_alvarez at right:
        zoom 0.7

    iris_alvarez "I had help.' The admission is small, and true. 'You helped marshal people. Tom and Lina did the real lifting. Marin held the lines. Ravi found the funds."

    kai_nakamura "And Iris held the map."

    iris_alvarez "Held the map, and kept tripping over the rocks."
    "Kai Nakamura reaches out, presses his forehead to yours. His hands are steady, callused, alive with the day's labor. The gesture says what words haven't: we took a risk, we almost broke, and we held."

    kai_nakamura "We figure it out, together. That's what I always thought. Teams, neighbors, friends."
    "You close your eyes for a second, tasting the salt air and a sudden, fierce gratitude. The town will not snap back to how it was before the tides rose; no single policy or plan could"
    "do that. But the accord — clumsy, bureaucratic, and tender — stitches a new shape that includes the people and places you love."

    iris_alvarez "I don't know if it's enough in the long run.' The worry is honest and immediate. 'But... it's a start."

    kai_nakamura "Start is where we begin rebuilding.' He pulls his beanie off, pushes his damp hair back, and grins like a conspirator. 'We get better, we iterate. It's what we do."
    "Your chest unclenches in a way you hadn't allowed yourself to imagine possible: not totally, not forever, but enough that your shoulders slide down an inch and the constant ache loosens."
    "The light softens to indigo. Lanterns on the promenade bloom like collected stars, and the repaired boards beneath you glow with reflected warmth. People move in the background — Lina organizing the dock crew with a"
    "precise authority, Tom exchanging a thumbs-up with someone carrying a crate of fittings, Ravi typing a quick update on his tablet with a look of tired satisfaction. Marin Voss stands slightly apart, watching the scene with"
    "the careful composure that has become their armor — and if you look closely, the corner of their mouth lifts, private and small."
    "You rest your forehead against Kai Nakamura's and let the moment hold: the crisis that pushed you into the breach became the very crucible that clarified who you are and who the town can be. You"
    "are tired — miles of planning, sleepless nights, heated council sessions, hands raw from work. But beneath the exhaustion is a steadier thing: rise."
    hide kai_nakamura
    hide iris_alvarez

    scene bg ch6_4001e7_4 at full_bg
    # play music "music_placeholder"  # [Music: Full-bodied, gentle swell]
    # play sound "sfx_placeholder"  # [Sound: The sea breathing, a town breathing with it]
    "Iris Alvarez [Thinking]: Here is the proof that people can stitch their lives into new forms without losing everything that made them themselves. It isn't a cure for the climate — nothing is — but it"
    "is a model of hope and stubborn love. We took pieces that could have torn us apart and sewed them into something more durable."
    show kai_nakamura at left:
        zoom 0.7

    kai_nakamura "Dinner's on me tomorrow. You better accept."
    show iris_alvarez at right:
        zoom 0.7

    iris_alvarez "I'll accept the burnt toast if you insist."
    "You both laugh, and the sound folds into the soft night."
    hide kai_nakamura
    hide iris_alvarez

    scene bg ch6_4001e7_5 at full_bg
    # play music "music_placeholder"  # [Music: The strings resolve into a warm, hopeful cadence]
    # play sound "sfx_placeholder"  # [Sound: Night settles; waves lap with a steady comfort]
    "You stand, feet on the repaired planks that now feel like home made anew. The town will never be the same — it shouldn't be. But the Patchwork Accord preserves the core: the people, the livelihoods,"
    "the hands that will keep working. You are tired, yes; you are scarred, yes; but together, you have become durable."

    scene bg ch6_4001e7_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade out on a single sustained note]

    scene bg ch6_4001e7_7 at full_bg
    "THE END"
    # [GAME END]
    return
