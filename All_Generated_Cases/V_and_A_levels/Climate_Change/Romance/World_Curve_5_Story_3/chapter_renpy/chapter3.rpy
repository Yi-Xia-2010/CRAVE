label chapter3:

    # [Scene: Community Meadow (Rooftop) | Midday]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm acoustic guitar; steady, hopeful rhythm]
    # play sound "sfx_placeholder"  # [Sound: Low murmur of voices; a kettle somewhere down the hall; wind threading through tall grasses]
    "You stand at the edge of the pergola, tide notebook heavy under your palm. The compass at its corner is the same weight it has been for years — a physical reminder that direction is a"
    "choice, not a promise. Sun warms the ink on your thumb. Around you, the town gathers like a tide: sun-faded hands, wrinkled maps, children's crayon waves on posterboard."
    "Lina Park moves through the crowd with the efficiency of someone who has learned to organize hope. She pins an extra talking-point to the board and gives you a short, fierce nod before returning to line up speakers."
    show lina_park at left:
        zoom 0.7

    lina_park "Five minutes until we call to order. Keep it to three minutes, folks—facts, feelings, and a clear ask. Maya, you'll be third."
    "You inhale. The air tastes like salt and old wood and the faint sweetness of lemon-scented hand soap from the refreshment table. Tomas sits near the back, cap pulled low, hands clasped like they are keeping"
    "something from floating away. He doesn't say anything; he never needs to. His face reads like a map of every storm this town has endured."
    hide lina_park

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A gull cries distant and thin]
    show elias_rowe at left:
        zoom 0.7

    elias_rowe "You good?"
    show maya_calder at right:
        zoom 0.7

    maya_calder "As I'll be. For three minutes, we are good."
    "Elias exhales a sound that is almost a laugh. He reaches as if to tuck a stray curl behind your ear, stops at the edge of the motion, and instead presses his palm to the back"
    "of your hand — a practical, steadying touch. It sends a small, electric warmth through the base of your wrist. It is enough."

    menu:
        "Open with dry data — set the frame with the sediment graphs first":
            "You step to the mic and let the numbers speak: sediment lines, projected retreat, error bars. The room leans in because you have made a map of the threat—clear, unavoidable."
        "Start with a human story — a memory of your father on the docks":
            "You take a breath and tell them about your father, the compass he gave you, how the tide once took more than it left. Eyes soften; the data that follows lands inside people's chests, not just their heads."

    # --- merge ---
    "The meeting bell rings; Mayor Amara Sol stands, voice polished but small tremor at the edges"
    hide elias_rowe
    hide maya_calder

    scene bg ch3_98c6f2_3 at full_bg
    show mayor_amara_sol at left:
        zoom 0.7

    mayor_amara_sol "Order. We're here to hear proposals and questions. Time limits observed. Ms. Voss, you'll present first."
    # play sound "sfx_placeholder"  # [Sound: Holo-tablet slide click; a faint electronic bloom as Serena's presentation appears on the rooftop screen]
    hide mayor_amara_sol

    scene bg ch3_98c6f2_4 at full_bg
    show serena_voss at left:
        zoom 0.7

    serena_voss "Good afternoon. We appreciate Aster's Reach's willingness to partner on urgent protections. The plan I'm proposing secures high-value infrastructure within twelve months, funded by private investment and municipal backing. It buys us time."
    "Her slides move like polished machinery: timelines, cost-benefit matrices, neat diagrams of a reinforced seawall. The investors' logos sit in a corner like sponsors at a lecture. There is a hum of admiration from some, relief from others. You can see where panic relaxes into something that looks like order."
    show maya_calder at right:
        zoom 0.7

    maya_calder "Time is a currency we don't have evenly."
    "Serena's steel-gray eyes find you across the crowd, and for a second they flick from tablet to face and there's an unreadable shadow there — a professional courtesy, maybe, or something closer to calculation. She tucks her tablet into her palm the way someone folds an umbrella shut after rain."

    serena_voss "We also have a sealed contract outlining funding conditions and prioritized zones. I'm happy to walk anyone through the specifics after questions."
    "Lina stands, her voice a crisp metronome."
    show lina_park at center:
        zoom 0.7

    lina_park "We need triage now and a plan that keeps neighborhoods connected. We need certainty that 'prioritized' won't mean 'divested.'"
    "The mic comes to you in the third slot. Your fingertips find the familiar grain of the tide notebook; the sample vials at its edges catch the sun and glint like caught fish. Professor Haruto's archival"
    "records click up on a side screen at your gesture — scanned photographs of past shorelines, notes in a fading hand, graphs that show more than erosion: patterns of displacement, clusters of cultural loss."

    maya_calder "Thank you. I'm Maya Calder."
    "(you pause because the room needs the frame)"

    maya_calder "I've spent years tracking the sediment fluxes and overlaying them with how this town actually uses this coast. Data without context is a forecast; context without data is a memory. We need both."
    hide serena_voss
    hide maya_calder
    hide lina_park

    scene bg ch3_98c6f2_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Quiet intake of breath across the crowd]
    show maya_calder at left:
        zoom 0.7

    maya_calder "If we build only for high-value assets, we risk saving roofs while losing the threads that stitch this town together. Here—"
    "(you tap a chart and Professor Haruto's archival overlay blooms)"
    "'—is what continuing the current course looks like in fifty years. It isn't a line on a graph; it's homes relocated, festivals canceled, whole livelihoods remapped.'"
    "A ripple moves through the crowd — not panic, but that careful shaking of people considering the cost of what they have always taken for granted. A child's hand tightens on a protest sign."
    show serena_voss at right:
        zoom 0.7

    serena_voss "All projections carry uncertainty, Ms. Calder. Immediate reinforcement keeps people safe tonight. We are not opposed to future adaptation; we are proposing a bridge."

    maya_calder "A bridge built only to wealthy berths becomes a wall to the rest of us. The 'bridge' you speak of could become an exclusionary baseline if we don't design safeguards now."
    "Serena studies the crowd, the mayor, the sealed contract she keeps folded like a promise in her briefcase."

    serena_voss "We can negotiate those safeguards. My offer today is funding—immediate deployment of reinforcements around critical infrastructure. In exchange, we ask for prioritized redevelopment zones to ensure investor confidence."
    show mayor_amara_sol at center:
        zoom 0.7

    mayor_amara_sol "Investor confidence means money is easier to raise, Serena. But it also means political consequences. We have to be able to justify any carve-outs to a town that will vote on this."
    "Tomas finally speaks, voice gravel-rough."

    "Tomas Reyes" "My sister's house sits where your line says 'non-essential.' She raised three kids there. 'Prioritized' don't mean nothing to her when the water comes in."
    "Silence settles like sea-glass on the garden. Eyes find one another — yours, Serena's, Elias's. Elias's gaze carries both measurement and momentum; he opens his mouth to suggest a technical compromise, then closes it, leaving the theater to you."
    hide maya_calder
    show elias_rowe at left:
        zoom 0.7

    elias_rowe "Whatever you choose to say, hold them to the human scale."
    "You nod. You feel the room tilt toward you like a listening shore."
    hide serena_voss
    show maya_calder at right:
        zoom 0.7

    maya_calder "We have an opportunity before us. We can accept funds that move at the pace of corporate calendars and hope that safeguards keep pace. Or we can bootstrap a pilot, prove community-led living shorelines can work at scale, and attract blended finance on terms we set. Or—"
    "(your voice tightens, not with fear but with the weight of possibility)"
    "'—we can force a transparency that makes any plan accountable to the people who live here.'"

    menu:
        "Underline the pilot option — call for volunteers and a demonstration site":
            "You outline a tight pilot: a week-by-week timeline, volunteer rosters, and metrics that any investor could audit. Lina's eyes light with galvanizing fire; people begin to lean forward, already imagining their hands in the earth."
        "Challenge Serena to guarantee legal safeguards in writing, then open negotiation":
            "You ask Serena to commit to legally binding safeguards before funding is accepted. She pauses, the tablet's light reflecting across her jaw. It's a direct gamble — she can sign, or walk."
        "Threaten to publish Haruto's data if the town is denied full access":
            "You hold up Professor Haruto's archive and explain its omissions; the implication of disclosure hums in the air. The room tightens, recognizing the moral and legal friction you could ignite."

    # --- merge ---
    "A hand shoots up from the edge of the crowd — a teacher, voice shaking. The discussion continues with questions about timing and scope."
    "A hand shoots up from the edge of the crowd — a teacher, voice shaking."

    "Teacher" "How long for a pilot? How many roofs would it protect during the next storm?"

    maya_calder "A carefully placed pilot, tested through a seasonal cycle, could demonstrate functional protection along a critical bay without requiring full-scale relocation. It won't be instantaneous like a seawall, but it designs resilience into neighborhoods, not around them."
    "Lina steps in, practical as ever."
    hide mayor_amara_sol
    show lina_park at center:
        zoom 0.7

    lina_park "We'd need volunteers, permits, and publicity. We can mobilize the meadow team and the Greenline Hub folks. We don't need to wait for permission to start outreach."
    "Serena crosses her arms, watching the exchange as if cataloguing the human variables."
    hide elias_rowe
    show serena_voss at left:
        zoom 0.7

    serena_voss "Pilots are useful metrics—but they can also be used by opponents to delay large-scale protections. Investors don't like pilots when they think 'delay.'"

    maya_calder "Investors also don't like lawsuits or community revolt. A pilot that works can unlock blended finance with better terms than a one-off corporate buy-in."
    hide maya_calder
    show mayor_amara_sol at right:
        zoom 0.7

    mayor_amara_sol "We're near the edge of the time allotment. We need a resolution about next steps: will the council pursue private emergency reinforcement, a community pilot, or full disclosure and legal action?"

    "Your chest is a steady drumbeat. The arousal of the room builds but remains purposeful — no hysteria, only determination. The romantic thread between you and Elias is quiet now, woven into a mutual steadiness: small gestures that mean, I am here. He slides a tiny sketch toward you during a lull — a modular planting terrace that could be adapted for a pilot site. His handwriting in the margin says simply" "If you want me."
    "You fold the corner of your tide notebook so the compass rests against the page like a silent anchor. You think of Professor Haruto's line about moral models: the way a community's knowledge can be its most durable instrument."
    "Serena steps forward and, for the first time, her tone softens enough that you can hear the old engineer beneath the executive."

    serena_voss "I'm prepared to offer immediate funds for reinforcements around critical infrastructure. In exchange, the town agrees to prioritized zones for redevelopment. However—"
    "(she lifts a hand, as if to steady the word)"
    "'—I'm willing to open a concurrent pathway: an auditable pilot co-funded and monitored by independent scientists. We can create a joint oversight board.'"
    "A murmur runs through the crowd like a hopeful undertow. Eyes dart toward you, to the mayor, to Serena."
    hide lina_park
    show maya_calder at center:
        zoom 0.7

    maya_calder "That's the offer."
    hide serena_voss
    hide mayor_amara_sol
    hide maya_calder

    scene bg ch3_98c6f2_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The garden exhales — low, near-symphonic — as if the town is collectively holding and releasing its breath]
    "Elias meets your gaze. His amber eyes are patient, expectant, and for a breath you consider the personal lens through which every choice now filters: a shared pilot would keep you both grounded here, a negotiation"
    "could open resources but complicate trust, a public release of Haruto's work could force accountability but fracture alliances."
    "You feel the full warmth of the VeryPositive arc settle like sunlight: this is not a collapse but a cusp. The room is tense with potential, not despair. The choices are hard, but they are alive with agency."
    "Serena folds her hands, unreadable again but not unkind."
    show serena_voss at left:
        zoom 0.7

    serena_voss "Maya—will you stand with that oversight board if we form it? Or will you call instead for full public release of Haruto's dataset?"
    "Maya Calder: (the decision hangs like a buoy bobbing in a restless sea) 'We have to choose who we are as a town.'"
    # play music "music_placeholder"  # [Music: Guitar resolves into a single, sustained hopeful chord — the moment of choice]
    "You look out over the crowd — faces weathered, bright, anxious, steady. Lina's jaw is set. Tomas's hands twitch as if he wants to help. The mayor's pen clicks once. Elias's palm is an anchor at your elbow."
    "Every option feels like planting: careful, deliberate, and alive with a potential to grow."
    "You breathe in the salt, the sunlight, the collective breath of Aster's Reach. Then you decide which tide to ride."
    "Rally a community pilot with Elias and Lina—prove living shorelines can scale."
    "Enter a controlled negotiation with Serena—seek funding while protecting safeguards."
    "Release Professor Haruto’s suppressed dataset publicly—force transparency."

    menu:
        "Rally a community pilot with Elias and Lina—prove living shorelines can scale.":
            jump chapter4
        "Enter a controlled negotiation with Serena—seek funding while protecting safeguards.":
            jump chapter7
        "Release Professor Haruto’s suppressed dataset publicly—force transparency.":
            jump chapter10
    return
