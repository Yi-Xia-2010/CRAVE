label chapter15:

    # [Scene: Glass Harbor Edge | Late Afternoon]

    scene bg ch15_3be532_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense BGM shifting into a driving, hopeful motif]
    # play sound "sfx_placeholder"  # [Sound: Wind biting across plastic sheeting, distant machinery muffled; the low, constant murmur of a crowd]
    "You stand where the tide used to come close enough to kiss the boardwalk—only now it stops at leveled dirt and the thin wire of temporary fencing. The air tastes of wet concrete and kelp; dust"
    "lifts with each breath and carries the faint, sweet memory of crushed seedpods. Your palms are raw from rope and wood; your barometer necklace is warm against skin, a tiny, stubborn heartbeat against the wide, unpredictable"
    "ocean."
    "Mayor Lionel Park is between you and Irene: an arch of compromise caught mid-stance. Tala's hand is warm and fierce on your forearm; Captain Reyes, silent and solid as driftwood, watches from the crowd. Dr. Sora"
    "Kim holds a battered tablet, lines of live data pulsing like a different kind of tide."
    "Irene's platinum bob catches the light—less a blade today, more glass: sharp, reflective, fragile. She speaks first, voice tight but public-smooth."
    show irene_vale at left:
        zoom 0.7

    irene_vale "The truce stands for now. Designated zones will be off-limits to heavy work. We will fund temporary housing for the most at-risk households. In exchange, construction resumes where we've agreed—beyond the critical marsh corridors."
    "You feel everything in the room pool into that sentence, the history of nets and porches and names attached to them. You want to answer with a list of why marsh corridors matter—to flood attenuation, to"
    "fish nurseries, to the memory stitched into Captain Reyes' hands—but the crowd will not let this be a technical recital. It's grief and bargaining in the same breath."
    show maya_alvarez at right:
        zoom 0.7

    maya_alvarez "We also get apprenticeship funding. Community oversight. Real milestones, not promises on a glossy board."

    irene_vale "You'll get transparency. Metrics. A monitoring board. Money tied to milestones—"
    show tala_ruiz at center:
        zoom 0.7

    tala_ruiz "Money that actually goes to people, not PR.' (She steps forward, voice bright as a thrown rope.) 'We want training for restoration—jobs that don't require people to leave the marsh behind."
    hide irene_vale
    show mayor_lionel_park at left:
        zoom 0.7

    mayor_lionel_park "We've got to make this durable. Irene—Mayor Park—this truce won't survive another broken promise. People will move if this is just window dressing."
    "Dr. Sora Kim: (softly) 'The pilot data will tell us what the marsh does when it's allowed to work. It will also tell us where engineered protections are necessary. We can use both.' (Her fingers tap a graph; the numbers are liquid and clear.)"
    "The crowd grows louder—relief braided with fear. Somewhere, a child cries and the noise slices you for a second of private worry. This is not tidy. It will never be tidy. But the truce is a"
    "hinge; the town has asked you, and you have answered—now the work must prove the trust."

    menu:
        "Step forward and lay out the pilot schedule now":
            "You pull a list from your satchel, voice quick and fervent as you read the timetable—public demos within two weeks, community apprenticeships beginning in a month. People nod, some shout agreements; the air tastes like possibility."
        "Let Dr. Sora announce the science plan":
            "You step back and watch Sora unspool the evidence: controlled tests, monitoring stations, independent audits. Her calm lends authority; murmurs turn into determined murmurs. Either way, the crowd tightens itself into motion."

    # --- merge ---
    "Either way, the crowd tightens itself into motion."
    hide maya_alvarez
    hide tala_ruiz
    hide mayor_lionel_park

    scene bg ch15_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The murmur rising into a roar of coordinated work; hammers begin to tap like a new kind of tide]
    "You and Evan move like a practiced pair on stage and off. He doesn't speak much; his hands do—aligning a prototype's stanchion, checking seals, smoothing out the biodegradable membrane. His wristband blips; the band has tracked"
    "every microclimate nuance these last months. When he looks up, the fatigue around his eyes is matched by a steadiness that steadies you."
    show evan_kaito at left:
        zoom 0.7

    evan_kaito "We can run three full flood cycles tonight—scale it so the cameras can't miss the data. I'll remotely trigger the pumps and the fail-safes. Sora will have live output."
    show maya_alvarez at right:
        zoom 0.7

    maya_alvarez "You always make things look like they were never an accident, Evan. Start when you're ready."

    evan_kaito "I don't like making accidents. I like making proof."
    "His hand finds yours—brief, necessary—and in the press you feel the shorted wires of everything you've avoided saying. There will be time for confession later. For now, the world needs a demonstration that will not let politics swallow ecology."
    # [Scene: Pilot Habitats | Dusk]
    hide evan_kaito
    hide maya_alvarez

    scene bg ch15_3be532_3 at full_bg
    # play music "music_placeholder"  # [Music: Tempo accelerating into a high, urgent rhythm]
    # play sound "sfx_placeholder"  # [Sound: Mechanical pumps priming, the chirp of sensors, distant thunder on the horizon]
    "Dr. Sora Kim stands at the control panel, her glasses catching graphs that climb. The first simulated surge is scheduled: a staged, controlled high-water event meant to stress the systems and show the performance of living"
    "shorelines paired with your pilot habitats. The press pads at the perimeter; cameras focus like hungry birds."
    show maya_alvarez at left:
        zoom 0.7

    maya_alvarez "This is the one. If it holds, it's not just us with sun in our hair anymore—it's evidence."
    show dr_sora_kim at right:
        zoom 0.7

    dr_sora_kim "The sensors are calibrated. We're recording sediment transport, wave energy dissipation, species responses. This dataset will be difficult to spin."
    show tala_ruiz at center:
        zoom 0.7

    tala_ruiz "And we'll livestream community testimonies while the numbers roll. People will see what they built."
    "You feel the world tilt into that narrow, combustible slice of time: meters of data, rivers of people, a single test that could reframe the whole argument. Outside, the sky is a bruise; storm-cloud architecture arranges itself like a jury."
    "The pumps start. Water rises into the channel. The first panels flex, the reeds bend but do not break. The sensors sing—frequencies you have come to know as victory and also as truth."
    "Then the wind picks up faster than forecasted. The unofficial storm—the one people had muttered about at dusk—thunders through early, a raw, impatient force. Your trained simulation becomes real pressure. For a breath the world narrows to the sound of your own pulse and the panicked counterpoint of alarms."
    # play music "music_placeholder"  # [Music: Climactic swell—very high arousal]
    # play sound "sfx_placeholder"  # [Sound: Alarms, wind tearing at membranes, cheers and shouts mingled with the clack of machinery]
    hide maya_alvarez
    show evan_kaito at left:
        zoom 0.7

    evan_kaito "We're rolling real-time! Sora, readouts!"

    dr_sora_kim "Energy dissipation within predicted thresholds—sediment retention is positive—biological indicators stabilizing!"
    "The pilot habitats cling to their pilings like determined little towns. Water surges, then rebuffs itself—broken against living berms and flexible foundations, routed into pools that feed marsh grasses instead of scouring them out. You feel a lightness in your chest so sharp it borders on disbelief."
    "Someone in the press offers an exultant whoop that turns the crowd into release. People cry—more than one kind of tears. Captain Reyes laughs, incredulous and open, and the sound knits everyone together more firmly than any resolution ever could."
    hide dr_sora_kim
    show irene_vale at right:
        zoom 0.7

    irene_vale "Those numbers... where did you—"
    hide tala_ruiz
    show dr_sora_kim at center:
        zoom 0.7

    dr_sora_kim "Independent monitors. Community-maintained chains. Open-source streams. This is verifiable, Irene. This is the kind of evidence that can be audited and replicated."

    irene_vale "If we—if I—agree to fund restoration at scale and shift the harbor perimeter inland around critical corridors... will you commit to a phased plan that includes economic offsets?"
    "You feel the moment split like a wave. It's the decision you and the town have been steering toward for months—messy, necessary, human."

    menu:
        "Press for binding legal milestones now, no soft words":
            "Your voice cuts in like a tide—practical, uncompromising: binding milestones, third-party audits, guaranteed apprenticeship slots. The crowd reacts; some cheer, others gape at the sudden legal sternness. Irene's jaw tightens; the tone becomes businesslike and concrete."
        "Ask for community oversight and a grace period for implementation":
            "You ask for oversight—time to get people trained, to move homes with dignity, to make sure the money feeds families. The crowd exhales. Irene's eyes narrow, then soften; she nods slowly, as if deciding whether to be the person the town's shouting needs."

    # --- merge ---
    "The highest point crashes and settles. The storm continues to peel the sky open, but the pilot habitats stand, proof etched in water and grass and streaming numbers."
    "The highest point crashes and settles. The storm continues to peel the sky open, but the pilot habitats stand, proof etched in water and grass and streaming numbers. Someone starts a chant again, softer this time:"

    "Crowd" "For the marsh. For the marsh."
    # [Scene: Council House Atrium (Negotiation Wrap-Up) | Night]
    hide evan_kaito
    hide irene_vale
    hide dr_sora_kim

    scene bg ch15_3be532_4 at full_bg
    # play music "music_placeholder"  # [Music: A resolute, swelling chord—victory tempered by work to come]
    # play sound "sfx_placeholder"  # [Sound: Chairs scraping, the rustle of paperwork, low, earnest conversation]
    "The negotiation moves inside where the air is warm and the light is clinical. Irene sits at the head of a table flanked by her team; Marauding renderings of glass structures glow on a screen beside"
    "live feeds of the pilot sites. Mayor Lionel pounds out terms, Tala runs the sign-up sheet for apprentices like a conductor, Captain Reyes brings the memory of the marsh as testimony, and Dr. Sora Kim demands"
    "audit clauses."
    "You speak for the town and for the marsh; you also speak for the families who will move with dignity, and for the ones who will stay. Your words now are less the fire they were on the boardwalk and more like the scaffolding that will hold the next years."
    show maya_alvarez at left:
        zoom 0.7

    maya_alvarez "We will accept a hybrid. Engineered protections where absolutely necessary—outside the critical marsh corridors. Inside those corridors: restoration, living shoreline projects, apprenticeships, jobs paid at living wages, and public oversight. Fund the transition. Fund relocation with respect. Bind it to external audits. No PR-only metrics."
    show irene_vale at right:
        zoom 0.7

    irene_vale "I will fund the apprenticeship programs. We will co-fund restoration. We'll adjust the perimeter—some development will happen, but not at the expense of the marsh's core. The funding will be in escrow, released on milestones the monitoring board agrees on."
    show tala_ruiz at center:
        zoom 0.7

    tala_ruiz "We build these things, we get paid to keep our neighbors safe and employed. We keep memories alive."
    hide maya_alvarez
    show captain_reyes at left:
        zoom 0.7

    captain_reyes "My grandfather fished these grasses. If they are to be part of the future, teach the young ones to tend them like family."
    "The agreement is not a tidy victory. The terms are a quilt sewn quickly: some house lots will be moved, some skyline glass will rise where nets once hung. There are losses—real, named, grieved—but the core"
    "of what makes Maris Bay resilient remains. Jobs in restoration replace speculative positions. Apprentices learn to read tides and data. Dr. Sora's independent audits sit in the contract, a lever you can use if anything veers"
    "toward spectacle over substance."
    "You sit back when the signatures begin to appear, a small, exhausted smile at the edges of your mouth. The room is full of people who once shouted at one another and now accord one another the economy of mutual need."
    hide irene_vale
    show evan_kaito at right:
        zoom 0.7

    evan_kaito "You did it."
    hide tala_ruiz
    show maya_alvarez at center:
        zoom 0.7

    maya_alvarez "We did it. We all did."
    "He doesn't say he'll never be tempted by the wider world again—he's never promised that—but he folds that possibility into the sentence that comes after."

    evan_kaito "I'll be expanding the collective regionally. But I'm not going anywhere from Maris Bay for good. Not if you keep making trouble."
    "You laugh, tired and bright. The laugh is a small truce of its own—between duty and affection, between the work left and the life you can let yourself hold."
    # [Scene: Verdant Rooftop Nursery | Morning (Weeks Later)]
    hide captain_reyes
    hide evan_kaito
    hide maya_alvarez

    scene bg ch15_3be532_5 at full_bg
    # play music "music_placeholder"  # [Music: Gentle, triumphant strings; birds in the seams of the city]
    # play sound "sfx_placeholder"  # [Sound: The hum of restoration—hose trickles, shared laughter, a distant call of a gull]
    "The rooftop is a catechism of small, steady things: hands in compost, children learning where cordgrass sleeps, Evan showing a group how to fasten a solar ventilator. Tala corrals volunteers with her trademark grin. Dr. Sora is there, cheeks smudged with mud, counting out transplants like blessings."
    "Mayor Lionel stops by with a lunch he intends to offer diplomatically; Captain Reyes brings an old carved pipe he says will be put in the new interpretation center as a reminder of what memory feels like."
    "You walk the rows and feel the town in your palms—seedlings that will become sediment traps, jobs that will become careers, people who will become stewards. The truce has grown roots; it will not hold the town safe by itself, but it buys time and labor and dignity."
    show tala_ruiz at left:
        zoom 0.7

    tala_ruiz "Look—apprentice slot filled by Rosa. She used to fish; now she knows the marsh like a blueprint."
    show maya_alvarez at right:
        zoom 0.7

    maya_alvarez "That's what we needed. People who keep the knowledge."
    show evan_kaito at center:
        zoom 0.7

    evan_kaito "And a partner who won't let me get away with half-measures."

    maya_alvarez "Promise me you won't disappear when the collective grows."

    evan_kaito "I promise to be here. To come back between builds. To make this one of the centers. To keep learning how to stay."
    "There is no cinematic kiss. There is instead the comfortable, resolute contact of two people who have seen storms and chosen to build, together, anyway. Your relationship is not a fairy tale; it is a contract of care—the kind that demands effort and reward in equal measure."
    hide tala_ruiz
    hide maya_alvarez
    hide evan_kaito

    scene bg ch15_3be532_6 at full_bg
    # play music "music_placeholder"  # [Music: Sweeping, cathartic crescendo—very positive, very high, then settling into peaceful resolution]
    # play sound "sfx_placeholder"  # [Sound: The ongoing music of lives remade—hammers, waves, laughter, the beep of monitors]
    "You stand at the edge of the Verdant Rooftop Nursery and look out over a town remade not by miracle but by negotiation, by stubborn people, by engineers who can be gentle and politicians who can"
    "be chastened. Glass rises, yes, where nets once hung—but marsh remains where the sea needs it most. Apprentices who once feared a future of displacement now hold the tools to build resilience and careers."
    "There are losses: a handful of families moved inland; a favorite fishery dock is gone. You carry names of homes that will not be as they were. The skyline is different. But the future—tempered by compromise and proof—is alive and elected by people who will now steward it."
    show captain_reyes at left:
        zoom 0.7

    captain_reyes "You kept our tide-line in the conversation. That's what saved us."
    show maya_alvarez at right:
        zoom 0.7

    maya_alvarez "You kept us remembering why the marsh matters. We just translated that memory into action."
    hide captain_reyes
    hide maya_alvarez

    scene bg ch15_3be532_7 at full_bg
    # play music "music_placeholder"  # [Music: A final, soaring chord that resolves into quiet contentment]
    # play sound "sfx_placeholder"  # [Sound: Waves, softer now; a distant hammer; the quiet murmur of a town that will keep working]
    "You tuck your barometer back under your shirt, its coolness a private relic. The town will always ask things of you—more work, more patience, more compromise. Tonight, you let yourself stand in the small, fierce joy of a thing done right enough."
    show evan_kaito at left:
        zoom 0.7

    evan_kaito "Coffee on the boardwalk?"
    show maya_alvarez at right:
        zoom 0.7

    maya_alvarez "Coffee, and then work. Same as always."
    "He presses his forehead to yours for a brief, anchoring moment. No promises ring like absolutes—only the steady sound of people choosing each other and the place they share."
    # play sound "sfx_placeholder"  # [Sound: The wind, the sea, the steady hum of monitors that will keep watch long after celebrations are over]
    "You close your eyes for a heartbeat and then open them to the town's light. It's not an ending of all trouble. It is, instead, the necessary, human kind of ending: one chapter closed with care, another beginning with tools in hand."
    hide evan_kaito
    hide maya_alvarez

    scene bg ch15_3be532_8 at full_bg
    "THE END"
    # [GAME END]
    return
