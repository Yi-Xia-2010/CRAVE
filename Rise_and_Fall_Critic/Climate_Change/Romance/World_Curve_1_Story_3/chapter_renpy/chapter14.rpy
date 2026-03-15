label chapter14:

    # [Scene: Skyward Market Rooftop Greenhouse | Morning]

    scene bg ch12_3be532_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm, rising strings; gentle percussion like a heartbeat]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the clink of tools, a low hum from the pilot's pumps]
    "You step out into the greenhouse and the city exhales with you — steam from the food stalls warms your cheeks, and the smell of wet earth and citrus fills your throat. The pilot's sensors blink"
    "in a rhythm you have learned to read: heartbeat, breath, readiness. This morning carries the weight of everything that came before it and the lightness of what might follow."
    "You remember the decision that led you here — the hybrid pact the mayor endorsed, the clause that finally wrote community veto into law, the contract language Jun helped phrase so it couldn't be footnoted away."
    "The memory is not a trophy; it's a tally: hours of meetings, nights of argument, elbows grease and legalese. It sits in you like a pocket of warm water, familiar and sustaining."
    "Teo is already at the edge of the dome, grease on his knuckles, a roll of cable and a grin that says he believes this will work. He waves you over, then falters for a beat when he sees your face and the way you steady yourself against the rail."
    show mateo_teo_rivera at left:
        zoom 0.7

    mateo_teo_rivera "You look like someone who slept two hours and carried the sun on their back. Good. That means you're ready."
    show asha_rivera at right:
        zoom 0.7

    asha_rivera "I'm tired, Teo. But right now, tired feels like fuel."
    "He laughs, a bright exhale, and turns back to tighten a sensor mount. In the rows of planting beds, neighbors file in — Sofia arranging seed packets, an old teacher testing her tablet, someone you don't recognize holding a child whose hair smells like salt and mango."
    "Dr. Jun arrives with a tablet under his arm, the same calm constancy he has always had. He taps the screen; the feed shows baseline readings, the anomaly thresholds set where you insisted they be."
    show dr_jun_park at center:
        zoom 0.7

    dr_jun_park "The initial calibration looks clean. Redundancies are online — open-source logs syncing at three-second intervals. Legal access is recorded. You built the stops, Asha."

    asha_rivera "We built them together. The hard part is keeping them open and honest when pressure comes."
    "Hana Kim stands beside the pilot, hands folded but relaxed. The AR monocle glints as she scrolls through deployment protocols. She watches the crowd with an expression that is both careful and, now, faintly relieved. You"
    "think of the months of negotiation: her insistence on measurable outcomes, your insistence on community control, the mayor’s compromise that turned both sets of demands into enforceable items."
    hide mateo_teo_rivera
    show hana_kim at left:
        zoom 0.7

    hana_kim "Leon signed off on the funding release this morning. The cooperative account is live. And —' (she taps, showing you a line of code) '— the feed is already public. Anyone can audit the sensor logs. No opaque channels."

    asha_rivera "Good. No secret systems. No back channels."
    "Elias Hart arrives last, breathless from running up the market steps, his jacket hung with new patches. He carries a stack of printed flyers — a crowd-control plan, a schedule of volunteer shifts, an outline for"
    "the public training sessions. He gives you a look that flickers between admonishment and affection."
    hide asha_rivera
    show elias_hart at right:
        zoom 0.7

    elias_hart "So did you register me as 'moral support' or 'designated loudmouth'?"
    hide dr_jun_park
    show asha_rivera at center:
        zoom 0.7

    asha_rivera "Both. You'll be loud when we need the crowd and quiet when we need the calibration."

    elias_hart "I'll try to calibrate my volume settings. No promises about my temperament."
    "His smile is easy and bright; it's the same light that once made you believe slogans could be scaffolding. But beneath his impatience is the same concern — for visibility, for ensuring this pilot isn't rolled"
    "out quietly while neighborhoods get displaced elsewhere. His worry is not abstract: it's the memory of people turned out of low ground in other districts, promises made and then quietly reversed."
    "You close your eyes for a second, tasting soil and salt and the metallic tang of new technology. The pilot hums. The roof is a patchwork of voices and footsteps, and for the first time in"
    "a long while, you feel like the conversations you've begged for are actually happening — publicly, transparently, in the daylight."

    menu:
        "Check the sensor mesh one last time":
            "You kneel and run your fingers along a strand of cabling, feeling the tiny vibrations of power. Your hands remember the circuitry as if they were planting rows; the mesh reports green. You nod, relieved, then stand to face the crowd."
        "Walk the rows and greet the volunteers":
            "You walk between the beds, hand on a damp leaf, one by one greeting faces you know and faces you don't. Each handshake anchors a promise; neighbors lean in with questions and small offers of help. You leave with a pocket full of small commitments."

    # --- merge ---
    "Continue to the montage and launch sequence."
    hide hana_kim
    hide elias_hart
    hide asha_rivera

    scene bg ch12_3be532_2 at full_bg
    # play music "music_placeholder"  # [Music: A brisk, hopeful motif — strings and light percussion]
    "You speak at the launch: a short, steady address that says what you mean without ceremony. You name the pilot for what it is — a test, a home, a precedent. You thank people by name;"
    "you credit both the engineers and the market vendors; you say the hard parts — the trade-offs, the vigilance required — because leaving them unsaid would be a betrayal."
    show asha_rivera at left:
        zoom 0.7

    asha_rivera "This pilot is not ours to own. It's ours to steward. The sensors are open-source. The cooperative holds operations. The community holds veto power. If any element fails, we change it in public. If any party seeks to override that transparency, they will be stopped by the law and by our own will."
    "A hush falls — not the heavy hush of fear, but the attentive hush of people listening to their own words mirrored back. Jun's eyes shine; Teo's jaw sets. Hana exhales, and when she speaks, it's low and precise."
    show hana_kim at right:
        zoom 0.7

    hana_kim "We've built in kill-switches controlled by the cooperative. The code will be mirrored to multiple repositories. Leon insisted on performance clauses; we insisted on audits. It's messy, but mess is how things actually get made."
    "Elias Hart steps forward, takes the microphone from you, and tilts his head to the crowd."
    show elias_hart at center:
        zoom 0.7

    elias_hart "We'll also teach anyone who wants to learn. We won't outsource our memory. We'll make sure this tech isn't a tool that forgets what it's for.' (he locks eyes with you) 'You're right about that."
    "His voice is rough with feeling. There's a multitone conversation between the two of you — the tempered, bureaucratic practicalities you've honed and the urgencies he carries. Neither of you wins an argument; you make one together. That, more than any clause, feels like victory."
    # [Scene: Skyward Market | Midday]
    hide asha_rivera
    hide hana_kim
    hide elias_hart

    scene bg ch12_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Laughter, the clank of a wrench, children running through hanging greens]
    # play music "music_placeholder"  # [Music: Gentle, rhythmic — community drums underscoring conversation]
    "Training starts. You stand with Jun and Hana as volunteers crowd around, learning to read dashboards, to refill nutrient solutions, to perform manual overrides if the pumps falter. The cooperative board is elected on the spot"
    "— hands raised, names called, responsibilities claimed. The mayor's office sends a representative to witness the signing; the legal documents are folded and stamped and archived in multiple places."

    "You listen to neighbors ask blunt, necessary questions: What happens in the storm? Can we decouple the pumps? Who decides when a sensor is replaced? Jun answers with diagrams, Hana answers with timelines, and Teo answers with barter" "Bring me a coffee and an extra hand and we'll fix it before lunch."
    "An older woman from the barrio — Rosa, who remembers the first levee as a boy — presses something into your hand. It's a small, embroidered patch: a mangrove root stitched in thread."

    "Rosa" "If this works, make sure the seedlings go back into the streets. If it doesn't, make sure we still get to tell the story right. Promise me that."
    "Asha Rivera: (your voice folds around the word like a brace) 'I promise. We will steward both the water and the story.'"

    menu:
        "Demonstrate the override to the crowd":
            "You step up, finger poised over the switch, and explain the safety protocols with a steady, careful cadence. The crowd leans in; someone asks a technical question and you answer. Seeing the mechanism in action takes away fear more effectively than any line on a contract."
        "Let Jun lead the demo":
            "You step back and watch Jun take the console. His quiet competence steadies the room. Letting him speak lets you listen — to the people's concerns, to the small grateful nods and the sparks of curiosity in children's eyes."

    # --- merge ---
    "Continue to the montage and the spread of the model."

    scene bg ch12_3be532_4 at full_bg
    # play music "music_placeholder"  # [Music: A hopeful, swelling chord]

    "Word spreads. You watch a live feed as another neighborhood on the other side of the river opens the repository and begins a conversation. Someone tags you with a short message" "How did you secure the veto clause?' You draft a reply that is as much a lecture as a love letter: 'Show up, insist on enforceability, build redundancy, and make everything visible."
    "Later, as the sun slants low, you walk through La Marisma. The neighborhood glows with new light strings, and the seawall prototypes cast narrow, protective shadows. People move with a different kind of ease; they speak"
    "about pumps and planting and policy at once, as if those nouns had always belonged together."
    "Elias Hart finds you near a narrow stairwell that leads to a garden terrace. He leans against the railing, watching the tide-line where mangrove roots snag litter and promise. His expression is open and complicated —"
    "the same way every person you love has ever been when change asks more than they expected."
    show elias_hart at left:
        zoom 0.7

    elias_hart "You did something dangerous."
    show asha_rivera at right:
        zoom 0.7

    asha_rivera "We're all dangerous, Elias. We love things enough to fight for them."
    "He pushes his hair back, a little sheepish. 'I was scared the project would become about placating the mayor. I'm still suspicious of Leon. But today — watching people learn to read their own sensors — I felt... anchored.'"
    "You hold the word for a moment. Anchored. It fits better than you expected."

    asha_rivera "We anchored it with law and with people. That's what will make it last."
    "He nods. Then, as if testing the space between you, he says, quiet, 'Do you think we can keep this? Not just the pilot—us, the way we work together.'"
    "You meet his gaze. There is history in both of your faces, things unspoken about argued lines and the nights neither of you slept. You don't reach for an old answer; instead, you offer what you can be certain of."

    asha_rivera "We can keep learning. We can keep showing up. That's how stewardship grows."
    "He exhales, a sound like relief and surrender braided together."
    # [Scene: La Marisma — Market Square | Dusk]
    hide elias_hart
    hide asha_rivera

    scene bg ch12_3be532_5 at full_bg
    # play music "music_placeholder"  # [Music: Soft piano, then a rising orchestral swell]
    "Hana Kim's speech is concise: metrics, timelines, accountability. She speaks of audits and open data, of teach-ins and shared governance. When she finishes, she steps down and crosses the small square to where you stand. Her"
    "hand brushes yours — a brief, steady touch that says more than any press release."
    show hana_kim at left:
        zoom 0.7

    hana_kim "We won't be perfect. There will be missteps. But we've set a structure that forces a reckoning when they happen. I want to keep working with you, Asha. If you'll have me."
    show asha_rivera at right:
        zoom 0.7

    asha_rivera "I will. We make a better net together."
    "She smiles, careful and soft. Elias Hart, watching, does not look possessive or threatened — only pleased, as if two good things can exist in the same light."
    "Dr. Jun appears with a printed booklet: the first edition of the 'La Marisma Blueprint' — clean type, diagrams, narratives from residents, legal appendices, and the open-source sensor instructions. He hands the booklet to you, eyes bright."
    show dr_jun_park at center:
        zoom 0.7

    dr_jun_park "We made it readable. We made it replicable. People will use this. They will change it. It'll never stay the same. That's the point."

    asha_rivera "Then let's make sure the next city doesn't have to relearn what we've learned here."

    "You turn the booklet's pages. The first line reads" "Community Stewardship: A Protocol."
    hide hana_kim
    hide asha_rivera
    hide dr_jun_park

    scene bg ch12_3be532_6 at full_bg
    # play music "music_placeholder"  # [Music: A warm major chord, sustained]
    "Night falls. The pilot continues to breathe; its sensors report normal parameters. The cooperative board locks in its first grant disbursement; the legal team files the ordinance attachments in public records; volunteers leave with toolbags and"
    "plans to plant the first stretch of living seawall. On a small stage, a child recites a poem about roots and water and how the city learned to hold both."
    "You walk alone for a moment to the edge of a low seawall, where the city meets the estuary. The tide laps slowly; it has not been conquered. You do not imagine a world without storms."
    "You imagine, instead, a community that can weather them with systems that are transparent, accountable, and responsive."
    "You close your eyes and hear, under everything else, the low, steady hum of the pilot — a promise you helped write into code, into law, into people's hands. It is not the only answer, you know, but it is an answer that can be taught and replicated."
    "Elias Hart appears beside you, and after a long silence he says, simply, 'Thank you.'"
    show asha_rivera at left:
        zoom 0.7

    asha_rivera "For what?"
    show elias_hart at right:
        zoom 0.7

    elias_hart "For not giving up on the ugly middle. For holding the line between tech and people. For being stubbornly reasonable."
    "You both laugh softly. Hana Kim joins you a moment later; all three of you stand as the city lights blink on like a network of small commitments."
    show hana_kim at center:
        zoom 0.7

    hana_kim "We should get some sleep. There's a lesson to teach in the morning and sensors to re-check at dawn."
    hide asha_rivera
    show mateo_teo_rivera at left:
        zoom 0.7

    mateo_teo_rivera "Also, free empanadas!"
    "The sound draws you back toward the market. People are still there — talking, mending, planning. The cooperative sign swings in the breeze. The prototype pumps whisper. Somewhere, far downriver, a new group reads the blueprint online and begins to plan."
    hide elias_hart
    hide hana_kim
    hide mateo_teo_rivera

    scene bg ch12_3be532_7 at full_bg
    # play music "music_placeholder"  # [Music: Uplifted strings and a choir-like, human hum]
    "You let yourself feel the slow rise of something that has been rare: cautious triumph. It is made from agreements that hurt at the edges and from people who stayed when leaving would have been easier."
    "It is not a tidy victory. It is work. But it is work that will be taught and repeated."
    "You tuck the printed blueprint into your jacket, take a deep breath that tastes like salt and orange peel, and walk back into the market, where the music and conversation fold you into the crowd. Tonight,"
    "no one sleeps easy; they sleep with pages of a plan beside them, and that is close enough."

    scene bg ch12_3be532_8 at full_bg
    # play music "music_placeholder"  # [Music: Resolve — a final, warm chord lingered]

    scene bg ch12_3be532_9 at full_bg
    "THE END"
    # [GAME END]
    return
