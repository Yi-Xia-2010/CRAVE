label chapter12:

    # [Scene: Floating Market of Canal Twelve | Night]

    scene bg ch12_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Water lapping against hulls, a distant municipal bell, the low mechanical hum of TideGrid nodes far off.]
    # play music "music_placeholder"  # [Music: Sparse piano, low and resigned]
    "You move through the market like someone reading the margins of a book you once loved. Names and faces come back to you in half-lines — the woman who sold pickled kelp from stall six, the"
    "boy who taught himself to play a tin harmonica, the shoals of children who used to run between your knees. Tonight the air tastes of metal and salt, and under it a new, colder tang: algorithmic"
    "order."
    "You remember the ledger first as a word on Rin Voss's televised brow, then as a stack of procedural waivers on Elias's tablet, the signatures like small, decisive stamps of consent. You can still feel the"
    "way his thumb used to rub the back of your hand when you believed in shared scaffolding; now the motion is shorter, rehearsed. That memory presses against your ribs and leaves a bruise."

    "Vendor" "Mae! Two for a taste, like always?"
    show maia_soler at left:
        zoom 0.7

    maia_soler "Not tonight."
    "A child splashes barefoot at the pier's edge; his laugh fractures the gloom for a second and you almost let it tell you everything will be fine. The ledger saved hospitals. You know that in the"
    "marrow of yourself — you watched the morning the hospital wards stayed dry while the east quarter sank two meters. You counted the beds that wouldn't be swallowed and the people who would now sleep without"
    "the fear of waking to water."
    "But the market's map has shifted. Paper signs are gone from moorings; notices from municipal scheduling systems flutter on posts like new flags. The TideGrid's rescheduling algorithm has nudged boats into different slots, shifted vendors' tides"
    "to optimize flow. Someone's cart — a painted wooden barrow you used to lean against — has been rerouted to a farther berth. Its owner stares after it with a thin, defeated patience that looks like"
    "mourning."

    menu:
        "Offer to help the vendor re-secure the barrow":
            "You wade into the shallows, hands cold and sure. The vendor's fingers tremble when she shows you the new mooring clamps; you work in silence, the two of you stitching a small, private fix against a system that has already decided your place."
        "Stand back and watch, feeling the weight of larger consequences":
            "You stand under a dripping awning and let the market fold around you. Watching feels like a different kind of labor — one that catalogs loss instead of repairing it. The vendor catches your eye and offers a crooked smile that does not reach her hands."

    # --- merge ---
    "You decide to do both in fits: a knot here, a word of comfort there. People expect Maia Soler to fix things small and immediate; they do not always ask whether fixing is enough. Ibe leans"
    "from his stall, saw tucked behind his ear, watching you with a look that is equal parts solidarity and answerable anger."

    "Ibrahim "Ibe" N'Diaye" "You look like someone who swallowed the sea and keeps walking. How's the ledger treating you, Maia?"

    maia_soler "It keeps hospitals from drowning. It keeps a lot of things from happening."

    "Ibrahim "Ibe" N'Diaye" "At the cost of who's calling the tide. The Ledger rearranged my deliveries. My suppliers now have TideGrid certification — which Ibe does not. Who knew a saw would need a serial number?"
    "You laugh, but it is a short, brittle thing. His voice is warm as ever, but his hands are quieter than usual, the rhythm of carpentry interrupted by fewer orders. You remember building the community terrace"
    "with him, the way his hands shaped planks until they fit like memory. Now contracts favor certified vendors, and your friend's ledger of work thins."

    "Ibrahim "Ibe" N'Diaye" "If you have a lead on local contracts, you give it to me."

    maia_soler "I will. I'll push for exemptions where it's possible."
    "He clamps a board with practiced movements, the smell of resin and warm wood a small defiance in the rain. Old jokes pass between you as scaffolding, but each laugh carries the distance of a tide."
    # [Scene: Canal Twelve — Narrow Boardwalk Outside Ibe's Workshop | Later]
    hide maia_soler

    scene bg ch12_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant broadcast cut in, carrier signal and an announcer's voice; the TideGrid hub hums like an animal breathing.]
    # play music "music_placeholder"  # [Music: Low cello, resigned]
    "You leave the market and walk toward where the city screens cluster — a public wall at the canal bend that the municipal broadcast uses for updates. Tonight it shows Rin's face in a loop: poised,"
    "immaculate, the wave lapel pin glinting like an accusation. Behind her, graphs and floating nodes sweep like the geometry of salvation."

    "Rin Voss (City Broadcast)" "In declared emergencies, the stabilization ledger will allow prioritized command of nodes. We do not have the luxury of indecision. This is about saving lives now."

    "The screen shifts to footage of trucks offloading supplies at the hospital docks. Statistics roll" "Active Lives Preserved: 14,302.' Below that, a sidebar notes 'Autonomy Adjustments: Temporary prioritization enacted citywide."
    "You feel the numbers as a cold tally against your sternum. Numbers are precise. They are also indifferent."
    "Elias Kade stands near the screen, shoulders hunched beneath his slate-blue jacket, his tablet dim at his side. He looks smaller than the marquee, like someone who has stepped out of a machine and is trying to remember how to be human."
    show maia_soler at left:
        zoom 0.7

    maia_soler "You told me you'd only sign if there were community guarantees."
    show elias_kade at right:
        zoom 0.7

    elias_kade "I did.' (he breathes out a laugh that is more a spasm) 'We put them in the protocol — oversight committees, audit logs. They exist."
    "You watch his jaw work. The light from the screen catches gold in his eyes, and you feel an old tenderness twist with a new ache."

    maia_soler "They do, on paper. But who's enforcing them when the ledger overrides? Who keeps the ledger honest when decisions need speed?"

    elias_kade "Rin promised independent auditors. I pushed hard for two community seats in the oversight charter.' (his voice tightens) 'We— I— thought that would be enough."

    maia_soler "You thought."
    "He reaches for your hand, an old motion reaching across a chasm. His fingers are familiar; they hold tools, not truths. There is a pause where something in you wants to accept the contact because it"
    "is human — because you are tired and the world is tired and comfort is currency — and another shard that remembers signatures and minutes and the ledger's quiet authority."

    menu:
        "Ask Elias to show you the oversight logs now, right here":
            "Elias hesitates, the mechanical instinct to fetch data kicking in. He scrolls and shows you entries: audit timestamps, redactions, the oversight committee's email thread. You read the words and feel their legal steadiness, but between the lines the governance seems thin, stretched by emergency clauses."
        "Tell Elias you need space and walk away toward the old dock":
            "You step back from the screen and the broadcast. The water smells stronger near the ruins, cleaner in a way. Elias doesn't follow at once; he watches you go with an expression that says he understands and does not."

    # --- merge ---
    "Elias's silence following either choice is a language of its own — complex, unreadable. He has done what he thought would save people; you recognize the moral architecture of his intention. You also feel the slow erosion of trust, a tide moving not with waves but with algorithmic increments."
    # [Scene: City Screens — Central Plaza | Night]
    hide maia_soler
    hide elias_kade

    scene bg ch12_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A recorded voice pronounces "Priority Allocation Active" with bureaucratic calm.]
    # play music "music_placeholder"  # [Music: Single violin string, thin and singular]
    "Old Man Toma sits on the plaza steps, his patchwork cloak damp. He folds a hand-drawn map — once a city's memory, now an artifact. You sit beside him. He does not look at the screens."
    show old_man_toma at left:
        zoom 0.7

    old_man_toma "Maps used to be about knowing where you could go. Now they're about where you are allowed to be."
    show maia_soler at right:
        zoom 0.7

    maia_soler "They saved the hospital, Toma."
    "Toma: (a small, almost invisible nod) 'They saved a hospital and made the rest of us into margins. When the sea asks questions, it prefers one voice. That voice can be kind. It can be cold. Either way, it is a single voice.'"
    "You look at him and see the memory of the promenade — the carved stones, the watchful faces who would vote on which planks to raise and whom to help. The ledger replaced that vote with a decision-tree built by engineers and executives."

    maia_soler "Do you think there was another way?"
    show old_man_toma at center:
        zoom 0.7

    old_man_toma "Always another way.' (his eyes are not unkind) 'But not always the time for it. Time runs like a tide and we live with its marks."

    menu:
        "Sit with Toma and talk about old strategies for resistance":
            "Toma brightens minutely and tells you of long-ago tactics, of how neighbors pooled rope and knowledge and held elections under lanterns. The conversation is a balm; it refills a bit of what the ledger drained."
        "Walk the plaza alone, collecting impressions for the ledger you once promised to write":
            "You walk, hands in pockets, and jot notes against your palm. The city feels heavier, and your notes feel like a ledger of losses — people rearranged by algorithm, businesses downtrodden, rituals interrupted. You realize the ledger you promised yourself will have to be different than the one Rin wrote."

    # --- merge ---
    "You choose both in small acts: a conversation with Toma that warms and a walk that sharpens. The duality sits in your chest — the push to preserve what remains, and the need to document what was traded away."
    "Later, from a distance, you watch a broadcast of municipal pressers: Rin's silhouette at the dais, the city statistics blinking in ordered columns. On live-feed panels across neighborhoods, residents call in — some with gratitude, some with the quiet fury of those whose moorings were moved without consent."
    "A vendor near the dock gets into an argument with a municipal scheduler who speaks in policy codes. The vendor's hands are wet with rope; he yells something about his mother, about her shop being a"
    "living thing that predates any algorithm. The scheduler replies with the clinical cadence of someone who sees problems as problems to be solved, not lives to be tended. You feel the argument like a chisel: it"
    "chips away at both sides until the pieces are too small to mend."
    "Elias Kade finds you again beneath the municipal screen. There are no scripts left between you now — only the gravity of the ledger and the residue of choices."
    hide old_man_toma
    show elias_kade at left:
        zoom 0.7

    elias_kade "They called me a collaborator today."

    maia_soler "And you are."

    elias_kade "I thought we were choosing lives over principle."

    maia_soler "We chose a version of both and lost the rest."
    "There is space here for recrimination — and for mercy. Both hover like gulls in the sky, circling."

    elias_kade "We can push for more oversight. I will keep fighting inside the system."

    maia_soler "Fighting inside the system is what you do best.' (you take his hand, briefly) 'But fighting inside it is not the same as standing beside the people who have been put on the margins."
    "His face shifts: frustration, grief, a tired kind of pleading."

    elias_kade "I didn't mean to make you feel abandoned."

    maia_soler "I didn't mean to be abandoned either."
    "There is a long silence after that, the kind that holds more than anything you could say. You know now, with a clarity that is both painful and inevitable, that the ledger has redrawn not only shorelines but loyalties."
    # [Scene: Old Dock District — Dawn (a few days later)]
    hide maia_soler
    hide old_man_toma
    hide elias_kade

    scene bg ch12_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant TideGrid maintenance drones; a lone gull]
    # play music "music_placeholder"  # [Music: Slow, aching violin]
    "You stand where the promenade used to be, the stones half-buried and moss-furred. Toma's map — the one he folded so carefully — lies in your bag. Ibe's saw is quieter now, but he is arranging"
    "planks for a community table, a small, deliberate act that refuses the ledger's totalizing reach."
    "You think of the hospital stats that argued for centralized control. You think of the vendor who lost his favorite spot. You think of the child at the market whose laugh still haunts you, resilient and unbothered by adult calculations."
    show maia_soler at left:
        zoom 0.7

    maia_soler "We saved bodies but felt the city thin out."

    "A soft wind carries a scrap of municipal notice across the stones; you catch it. The paper reads like a prayer written by engineers" "Efficiency will save us."
    "Elias Kade appears at the edge of the ruins, framed in the early light. He has spent nights drafting oversight proposals, speaking to committees, bargaining with Rin's aides. You no longer expect his answers to soothe every wound. What you expect now is honesty."
    show elias_kade at right:
        zoom 0.7

    elias_kade "I don't want to triangulate us into silence."

    maia_soler "Silence has been the ledger's quietest ally."

    elias_kade "What do you want from me, Maia?"
    "Maia Soler: (there are many answers, each contingent and heavy) 'I don't want easy phrases. I want shared labor — and shared accountability. I want you to keep fighting, but not only through blueprints and boards. Promise me you won't forget the people the ledger displaces.'"
    "He closes his eyes briefly and opens them with a steadier look."

    elias_kade "I promise to push for binding oversight. I promise to fight for community seats that have teeth.' (he swallows) 'I will—' (he searches for a word that won't sound like calculus) '—I will try to be present, not just procedural."

    maia_soler "Being present is not a checkbox."

    elias_kade "I know.' (he steps closer) 'If that were enough, we'd have already been whole."
    "There is tenderness between you — a worn thing, real but rearranged by events. You hold onto it like a splinter of light. Then you let it go in a way that feels like a final, honest offering."

    maia_soler "We are not the same as we were when this began. We both carried different parts of this city into the ledger. Maybe the only honest thing is to admit what that did to us."

    elias_kade "If that's what you need — space, time, a different kind of fight — I will give it."
    "You both stand then, the ruins between you like a map of choices. There is no dramatic parting; nothing cinematic. There is only the quiet recognition that some bridges will be mended, and others will be rerouted forever."
    "Old Man Toma approaches, leaning on his cane. He places a hand on each of your shoulders in turn — first yours, then Elias's — a benediction that is less about blessing and more about witnessing."
    show old_man_toma at center:
        zoom 0.7

    old_man_toma "People will build new things. They will find ways even when the ledger tries to plan them away.' (his eyes rest on you) 'But remember: survival is not the only metric. Keep an account of what was loved. Keep that ledger, too."
    "You nod. You will keep that ledger — not the city's algorithmic one, but a human ledger of stories, names, promises. You will record who was moved, who resisted, who stitched community life back together with"
    "callused hands and shared soup. It will be slow. It will be imperfect. It will matter."
    hide maia_soler
    hide elias_kade
    hide old_man_toma

    scene bg ch12_f99e88_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A gull cries; a distant machinery hum continues, steady and indifferent]
    # play music "music_placeholder"  # [Music: Cello and piano in a low, concluding motif]
    "You walk away from the ruins with a small, steady step. You do not know whether the ledger can be reformed from within; you do not know whether Elias's promises will hold against the pressures of"
    "power. What you do know is this: the city kept breathing, and a great number of lives were preserved. You also know that preservation made new absences — of rituals, of authority shared at the neighborhood"
    "scale, of the easy intimacy you once took for granted with a partner."
    "You let the city be both a victory and a wound. You let the ledger exist with its cold efficiencies and hold on to the human accounts you will build in response. That will be your work now: to tally what numbers do not capture."

    scene bg ch12_f99e88_6 at full_bg
    # play music "music_placeholder"  # [Music: The motif resolves into a single, minor chord that does not promise repair but does promise endurance]

    scene bg ch12_f99e88_7 at full_bg
    "THE END"
    # [GAME END]
    return
