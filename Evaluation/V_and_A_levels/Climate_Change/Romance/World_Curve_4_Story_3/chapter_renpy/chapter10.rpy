label chapter10:

    # [Scene: The Beacon | Early Evening]

    scene bg ch8_b0bdfc_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense BGM — percussion edging in, strings tremulous]
    # play sound "sfx_placeholder"  # [Sound: Low murmur of conversations; distant gulls; an almost-electronic ping from the live sensors]
    "You step into the Beacon's plaza carrying the aftertaste of the lab's feed — salt and circuitry, the small electric thrill that meant the trial worked. That success is already a lever in someone else's hand."
    show lila_park at left:
        zoom 0.7

    lila_park "Our deployment has proven the network's responsiveness. Scale this, integrate engineered seawalls, floating platforms, and designated resilience districts, and Marabel becomes a model — safe, fundable, repeatable."
    "Her voice is flat, efficient—that same voice that convinced councils as easily as it convinced investors. Around her, slides click through: flood-lines, cost-benefit curves, rendering after rendering of a smooth, defended coastline. People lean forward like gulls leaning into a wind."
    "Narration:"
    "You watch faces: some bright with relief, others folding like paper. Mayor Rosa's jaw is loose at the edge; you read weariness there like a map. The lawyers speak in commas and clauses; their words are designed to breathe safety into ambiguity."

    "Lawyer" "Managed trust governance ensures continuity of care. The trust holds title in perpetuity with covenants guaranteeing preferential occupancy."
    "You frown at the phrase—'preferential occupancy' feels like a promise wrapped in a legal glove. Your chest tightens because you can imagine how promises can be translated, contorted, auctioned."
    hide lila_park

    scene bg ch8_b0bdfc_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A sharp click as a new slide advances]
    show lila_park at left:
        zoom 0.7

    lila_park "We will maintain allocations for residents. You'll have seats on the board; we'll administer maintenance and insurance, and the infrastructure will be maintained to a standard that municipal budgets cannot match."
    show noah_reyes at right:
        zoom 0.7

    noah_reyes "We can negotiate terms — more community seats, veto powers, audit rights. It won't be perfect, but it's leverage."
    "You feel the warmth of his breath like a small tide at your collarbone. He places the rolled map he carried on the table between you and Lila, an old gesture of solidarity that suddenly feels charged."

    noah_reyes "We need clear legal guarantees. Resident veto on land disposition. Binding timelines. Transparency clauses."

    lila_park "We can draft operational charters. The consortium is amenable to community representation, provided implementation is not compromised."
    "Narration:"
    "Her words are precise and practiced; her eyes hold the steel-gray calm of someone who believes speed is salvation. The plaza hums with pressure. You feel urgency like a physical current, tugging fingers and loyalties."

    menu:
        "Ask for clause clarity, point to the 'preferential occupancy' line":
            "You clear your throat and specify how 'preferential occupancy' is written: duration, transferability, enforcement. The lawyer's smile tightens a fraction; papers are smoothed. Lila's gaze narrows, appreciative of a fighter who knows the text."
        "Stay silent and watch reactions":
            "You keep your mouth shut and catalog faces—Rosa's tired nod, Marta's folded arms across her chest, Eli's hands fidgeting with a rope. Silence lets you hear the subtext."

    menu:
        "Promise Marta you'll call the neighborhood assembly tonight":
            "You nod, throat tight, and tell Marta you'll set a meeting in the lot behind the old boatyard—she exhales like a storm easing. Hope shifts; wheels set in motion."
        "Tell Eli you'll draft compromise language with Noah and Rosa":
            "You tell Eli you'll try to craft terms that keep docks safe and community seats strong. He grunts, not entirely satisfied, but willing to wait for words that hold weight."

    jump chapter12
    return
