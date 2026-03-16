label chapter5:

    # [Scene: The Beacon | Early Evening — After Soup]

    scene bg ch5_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low, comfortable murmur — cutlery on bowls, chairs scraping, the distant creak of the boardwalk outside. The sensor on the table emits a quiet rhythmic ping.]
    # play music "music_placeholder"  # [Music: Soft ascending piano, steady and hopeful]
    "You follow Elias 'Eli' Navarro down the Beacon's concrete steps and the doorway hugs you in — steam from Rosa's soup fogs the glass for a beat, then clears to reveal the room alive with people"
    "who have already started to care. The air smells like broth and salt-scrubbed wood; a faint tang of solder and old paper from Hal's worn briefcase underpins it. Your notebook rests in your jacket pocket; the"
    "sensor reader dangles from its lanyard, a familiar weight against your chest."
    "Rosa waves from behind the counter, flour on her cheek, a steaming ladle poised in a gesture of welcome. Miriam is already standing by the whiteboard, marker in hand, energy like static; Hal sits with his"
    "knees splayed, a thermos at his side, eyes that track the room like a tide gauge. Elias 'Eli' Navarro squeezes your hand once, privately, and then releases it so you can stand at the marker without"
    "awkwardness."
    "You feel the quiet buoyancy you felt earlier on the boardwalk — responsibility, yes, but carried now by more hands than yours. There are invoices, there are values, and tonight you are going to try to make them overlap."
    show amara_vale at left:
        zoom 0.7

    amara_vale "Thank you, everyone. For soup and for coming. We have three big budget lines to reconcile: mangrove restoration and the promenade scaffolding, grants and business retrofits, and the microgrid pilot. All of them are legitimate. None of them are cheap."
    show miriam_santos at right:
        zoom 0.7

    miriam_santos "Legitimate and urgent. People can't wait on slow returns while their shops flood. We have volunteers, but we don't have rent money."
    show harold_hal_finnegan at center:
        zoom 0.7

    harold_hal_finnegan "When we fixed the seawall after '29, it wasn't just labor that saved us — it was maintenance. Whoever plans for the upfront also needs to plan for the upkeep. That's where projects die or live."

    "Elias 'Eli' Navarro" "I've run some rough phasing options. If we prioritize the mangrove beds and a modest raised promenade now, the ecological benefits take longer to show economically, but they cut wave energy and maintenance costs over a decade. If we divert cash to immediate retrofits, shops survive another season, but we lose leverage for larger landscape work."
    "You set the marker tip to the whiteboard and the black scratches across the surface — line items, timelines, possible funding partners. The room narrows into your focus: saplings, scaffolding, sensors, stipends, maintenance schedules. You can almost hear each item's heartbeat as you name it."
    hide amara_vale
    show rosa_kwan at left:
        zoom 0.7

    rosa_kwan "My customers will be at the meeting. They want to know if their doors will stay open. They also want the promenade to look like Seabright, not a construction site for years."

    miriam_santos "That's why stipends and small grants matter. If you're asking people to close or adapt, you have to pay the cost. Otherwise 'community-led' is a euphemism for 'let the poor subsidize resilience.'"

    harold_hal_finnegan "And legal strings. Grants come with strings. Private money comes with its own. We need iron-clad maintenance clauses. Not romance clauses — worksheets."

    "Elias 'Eli' Navarro" "We can phase maintenance into the budget. A maintenance fund seeded by initial grants, supplemented by a small levy if the town approves it. My worry is that the levy will scare small-business owners unless we show a near-term benefit."
    "Your mind ticks through scenarios you know well: a line item that looks generous on paper but becomes a deadline people can't meet; saplings planted that fail when volunteers burn out; sensors that go unmaintained and"
    "become paperweights. You think of Hal's hands, the rough palm that mended so many designs; you think of Rosa's apron, flour still drying around the cuff."
    "You want to speak with clarity, to thread the moral argument through the invoices so both Miriam's indignation and Elias 'Eli' Navarro's caution feel heard. You begin to sketch a phased plan on the board: Phase"
    "1 — emergency retrofits and stipends; Phase 2 — mangrove bedding and promenade scaffolding; Phase 3 — sensors and maintenance endowment. As you write, the room's energy shifts — conversation as construction."

    menu:
        "Open with a story about the shoreline before '29":
            "You start with a memory: gulls, the low hum of fishermen, a wooden pier that used to hold more summer shoes than sand. The room quiets; Hal closes his eyes for a moment, and faces in the crowd soften. You've given the budget a human face."
        "Start with the numbers — strike while the pragmatic iron is hot":
            "You lift a printout and read the headline numbers aloud: costs, timelines, grant deadlines. Eyes narrow, pens start to move. The warmth is efficient; people who need specifics lean in."

    menu:
        "Emphasize ecological benefits first — sell the long-term story":
            "You imagine the mangroves' slow work: roots catching sediment, young fish returning. You feel the future in your chest. This tells a story of stewardship, of legacy, and many listeners will find it noble."
        "Lead with immediate community relief — sell the quick wins":
            "You picture Rosa's open door, Miriam's volunteers paid for their time, a shopkeeper wiping a grateful tear. This sells hope fast and puts money in pockets today. It courts immediate buy-in."
        "Frame the microgrid as systemic leverage — sell a structural change":
            "You pull the microgrid into focus: local power, reduced dependence, an asset that can multiply resilience. It's ambitious, legally dense, and could attract different funders — but it requires a patience sale."

    menu:
        "Prioritize mangrove + promenade scaffolding":
            jump chapter6
        "Prioritize grants and retrofits for small businesses now":
            jump chapter16
        "Push for microgrid pilot requiring legal work":
            jump chapter16
    return
