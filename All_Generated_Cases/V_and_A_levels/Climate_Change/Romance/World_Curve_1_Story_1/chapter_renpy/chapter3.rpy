label chapter3:

    # [Scene: Harbor Boardwalk | Night]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, urgent strings; tempo accelerating]
    "You step back out into the night and the boardwalk immediately feels narrower, as if the wind itself is tucking the world in at the edges. Your jacket flaps; the thermos in your hand is a"
    "warm, steady weight. The city smells of frying oil, salt, and a fresh, electric rain. Above the stalls, Camille's billboard — mirrored steel, a ribbon of chrome and bold type — throws a clinical light across"
    "wet planks. It claims certainty. It promises stability. It reframes the shoreline as a problem with a single engineered solution."
    "You let the image of the tower sit in your chest as you walk. It sits there like a question you have to answer before you sleep."
    # play sound "sfx_placeholder"  # [Sound: Reeds whispering; gulls cry; damp footsteps on wood]
    "Rowan meets you halfway along the fringe, boots leaving shallow prints in the softened boardwalk. He smells of wet earth and lab coffee. His hands — pale, trimmed, with the tidy tremor of someone who teaches"
    "patience — are stained with marsh silt. He opens the notebook to the page where you've been tracing erosion lines and leans in, pointing with a finger that still holds a dark crescent of soil."
    show professor_rowan_hale at left:
        zoom 0.7

    professor_rowan_hale "See this? The scarp's moved a bit farther in since the last survey. Not catastrophic yet, but it's faster after the last two storms."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Faster how? Inches, or—"

    professor_rowan_hale "Sometimes inches are all you get before a whole bank takes the rest. Look at the root mats; they’re loosening. If we don't stabilize, we lose buffer more quickly than anticipated."
    "His voice is measured, not alarmist. The maps in your notebook look smaller under his hand — precise lines, cross-checks, a late-night discipline. You trace the pencil marks the way you trace a decision you haven't made yet: carefully, as if pressure might chip the lead."

    maya_reyes "If we show these lines to the mayor — if we can pair them with a real-world pilot — it might change the conversation. But that needs funding, and you know how that looks."

    professor_rowan_hale "Technical credibility helps. It gives people something concrete to oppose a single-solution pitch with. But it won't itself move votes. For that you need people who are willing to show up."
    "You run your thumb along the margin of the page and feel the faint grit of salt. The marsh breathes around you: a low chorus of insects, the distant thump of a boat engine, the soft"
    "drag of tidal water against pilings. You can feel the urgency — a quickening under your ribs — but your face stays clear. Decisions are work; work is what keeps you steady."
    # [Scene: Marsh Fringe | Under a Leaking Tarp, Later]
    hide professor_rowan_hale
    hide maya_reyes

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain pattering; the muffled murmur of a market crowd not far off]
    # play music "music_placeholder"  # [Music: Light, staccato piano overlaying steady percussion — tempo climbs]
    "Elias Stone is there, sleeves rolled, the braided fishing-line bracelet at his wrist catching the light each time he moves his hand. Rolled plans stick from his satchel; a small digital pen blinks like a heartbeat."
    "He speaks in practical beats, weaving numbers and conditional clauses the way you weave knot and line."
    show elias_stone at left:
        zoom 0.7

    elias_stone "Conditional financing is what separates a pilot from a takeover. We draft performance thresholds — measurable outcomes, community oversight panels. If the firm's funding only unlocks after X percentage of success, then the community controls the release of capital."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "And you think they will agree to that? Camille's people aren't in the habit of ceding control."

    elias_stone "They might if the mayor wants it. If we present a design that limits cost overruns and shows short-term metrics — reduced erosion, plant survival rates — the political risk is lower for them. It can be framed as shared governance."
    "You look at him. There's a softness in his slate eyes, an engineer's hunger to fix the problem with a plan. There is also the shadow of his past in big firms, the one he doesn't"
    "advertise and you don't pry at tonight. Your history with him is braided now with practical things: budgets, timetables, compromises. You feel both the pull of possibility and the friction of giving up parts of the"
    "fight."

    elias_stone "I can help write it. I can stand in front of people and translate technical language into things that make sense at a kitchen table. But Maya —' (he hesitates, fingers adjusting the strap of his satchel) '— I won't do anything that strips the community of oversight."

    maya_reyes "Then keep me honest. If we do this, it must be written into the contract. No vague terms, no slow erosions of authority. We sign off on every milestone."

    elias_stone "Agreed. If we go this route, we'll need legal counsel on community-stewardship clauses, and we should line up Professor Rowan for the technical review."
    "There's a pause where neither of you speaks. In the tarp's shadow the rain drums faster, a small escalation that makes your decisions feel like they're moving parallel to a weather front."

    menu:
        "Push for immediate pilot paperwork with Elias — begin drafting tonight":
            "You reach for Elias' satchel, fingers already easing toward the rolled plans. The idea of clauses and thresholds feels like a rope you can use to tie the community's hand to the work. Elias exhales, surprised, then matches your pace, pulling a sheet of tracing paper to start a schematic in the dark."
        "Tell Elias to hold — organize more neighbor support first":
            "You fold the notebook closed and press your palm to its cover. 'Not yet,' you say. 'We need people at the docks before we hand them plans.' Elias's jaw tightens; he traces the edge of his bracelet with his thumb, considering. He does not disagree, but his eyes carry the wish to move faster."

    menu:
        "Step forward and open the demo with a short speech":
            "You take the megaphone with hands that do not shake. Your voice is tighter than you'd like, but it carries. You speak of marsh grasses and ribs of shoreline, of people who cannot be compensated for a lifetime on the water. The crowd answers with a clap that smells of salt and determination."
        "Let Amaya open and work the crowd behind the scenes":
            "You hand the megaphone back without ceremony. Amaya launches into a practiced, fierce speech. You move through the edges of the crowd, greeting faces, recording notes, watching how the energy organizes itself without you at the core."

    menu:
        "Start a public restoration action and mobilize the neighborhood.":
            jump chapter4
        "Work with Elias to propose a community-centered adaptive plan and pitch it to the mayor.":
            jump chapter8
        "Confront Camille publicly—leak evidence and demand a hearing.":
            jump chapter11
    return
