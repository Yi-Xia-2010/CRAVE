label chapter3:

    # [Scene: Municipal Hall | Overcast Afternoon]

    scene bg ch3_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low murmur of the community, the distant slap of tires on wet pavement, an undercurrent of restless coughing. The faint clack of rain against the glass.]
    # play music "music_placeholder"  # [Music: Sparse, low strings — steady, minor-key pulse]
    "You remember the promise — 'I'll listen' — like a small stone in your palm. It is warm where your buoy pendant meets your chest. The municipal hall smells of damp paper and coffee gone cold;"
    "the room somehow feels smaller than the greenhouse where you last spoke with Elias, closer to the scale of consequences. Faces tilt up at the projector screen: neighbors, fishermen, municipal employees, volunteers from the cooperative. Kaori"
    "'Kai' Matsuda is there—her braid a neon slash in the crowd—eyes bright and sharp. Mika sits near the back, fingers worrying a strap. Old Tom folds his hands over a knee, his beard a knot of"
    "rope and history."
    "Rina steps forward. Her posture is practiced, precise; she opens the briefing with a voice that is businesslike and tired."
    show rina_corbett at left:
        zoom 0.7

    rina_corbett "Thank you all for being here. We know what's at stake. We've called this session to discuss a coordinated municipal plan for adaptation. We will hear a presentation from Elias, a community response, and then public testimony."
    "A scattering of applause, thin and polite, dies out. You feel a coil of alertness tighten behind your ribs — not excitement, not dread so much as a sober readiness."
    show elias_kato at right:
        zoom 0.7

    elias_kato "The model we built uses ten years of tide and storm data plus recent survey drones. The proposal: strategic seawalls at critical nodes, elevating the school and medical center, and targeted managed retreat in the lowest-lying parcels. We can protect essential services and buy time while other restorative measures scale up."
    "He clicks; the map animates. The visual logic is clinical, the language curated to reassure: 'buy time,' 'critical nodes.' You hear the careful optimism in his voice, the exact, measured cadence that has always steadied a"
    "room. But under it there is a current — an arithmetic that counts houses and dollars, that maps some people to safety and others to zones labeled 'relocation.'"

    "Councilmember Rina" "We'd like to open the floor for questions after the full briefing."
    "Before anyone can speak, a voice slashes through the polite order."
    show kaori_kai_matsuda at center:
        zoom 0.7

    kaori_kai_matsuda "This plan hands our tide-lines to contractors and lawyers and calls it care. Walls mean displacement. Walls mean the same folks who couldn't get a meeting before will lose everything while the town congratulates itself on a 'modern solution.'"
    "Murmurs ripple. Kaori 'Kai' Matsuda's hands are full of tactile protest: a printed schematic of her modular floating farms, a photo of a community-built microgrid. She slams the papers on a table; the thud echoes."

    kaori_kai_matsuda "We are already doing the work. Pilot farms anchored at the flats could reduce erosion, provide food, and keep people where they've been for generations. People who can't afford to move won't be 'managed' — they'll be moved."
    "Elias Kato doesn't answer at first. He watches Kaori 'Kai' Matsuda the way someone reads a forecast—taking in markers and adjusting. The room bristles; some faces lean toward Kaori 'Kai' Matsuda, furious and hungry for hope; others look at Elias Kato as if waiting for instructions."
    "You step up when Rina gestures, because your cooperative's name is in people's mouths and your throat has an ache from holding back. The podium is cool against your palms; the hall seems to lean in."

    menu:
        "Close your eyes, breathe, and begin with the story of your father":
            "You take a breath that tastes of sea-salt and old rope. You begin with your father's hands, the first knot you learned; the room quiets at the human shape of risk."
        "Open with technical data — emphasize modeled reductions in erosion from kelp long-lines":
            "You lead with numbers and diagrams. Some eyes flick away; engineers nod. Kaori 'Kai' Matsuda watches you with a small, unreadable look."
        "Look at Elias before you speak, and then turn to the crowd":
            "You hold Elias Kato in your peripheral vision — steady, guarded — and then let your words move outward to the room, as if tying both halves together."

    menu:
        "Tell Kaori 'Kai' you'll organize direct action — announce plans to block the site":
            "Kaori 'Kai' Matsuda's face drops, then lights; she grabs your elbow as if to pull you toward something inevitable. The crowd around you tightens in solidarity."
        "Tell Elias you'll join the working group — ask for concrete commitments first":
            "Elias Kato releases a tensioned breath, an almost-smile that is all relief and warning. He pulls out his tablet to list deliverables, the planner in him resurfacing."
        "Propose the festival demo — a public hybrid demonstration":
            "You watch both of them consider the idea. It hangs between you — risky, visible, and oddly hopeful. Mika's eyes sparkle; Kaori 'Kai' Matsuda's mouth twitches with the beginnings of a plan."

    menu:
        "Lead the community — we’ll block construction and build the cooperative now.":
            jump chapter4
        "Work with Elias — I’ll join the municipal process to shape the plan.":
            jump chapter7
        "Stage a high-profile demo at the festival — show what regenerative buffers can do.":
            jump chapter10
    return
