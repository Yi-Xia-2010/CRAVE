label chapter11:

    # [Scene: Saltgarden Research Lab | Morning]

    scene bg ch11_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm, hopeful strings with a clean arpeggio]
    # play sound "sfx_placeholder"  # [Sound: Soft pump hum, distant gulls, a kettle boiling somewhere across the husk of the warehouse]
    "Narration:"
    "You wake into the lab with the taste of last night's rooftop air still in your mouth — herb-scented and honest — and a small, steady pulse in your throat where the coral pendant rests. The"
    "methods note you and Ilias stayed up late drafting has a rhythm now: diagrams smudged with ink and kindness, an open-source license line that reads like an invitation rather than a sale. It sits on the"
    "lab server, and in a few hours the world will be able to read the exact way you coax eelgrass to take in harbors that have almost forgotten how to hold life."
    show maya_kestrel at left:
        zoom 0.7

    maya_kestrel "We did the leak check on the seed trays last night, right? No sneaky capillary drains?"
    show ilias_navarro at right:
        zoom 0.7

    ilias_navarro "Yeah."
    "Narration:"
    "(He lifts a tray with a pair of gloved hands, the dim light catching flecks in his hair.) 'Hana ran the flow model again at three a.m., and she said the variance is within expected bounds"
    "for a community kit. It doesn't need perfect conditions — it needs people who won't let it be alone.'"
    "Narration:"
    "You watch him set the tray down and feel the familiar pull of gratitude — small, generous, dangerous because it loosens something you keep knotted. When your fingers brush the mesh, the fabric of possibility feels tactile: salt-and-silt, human hands, a future that can be touched."
    show rafi_soto at center:
        zoom 0.7

    rafi_soto "You two look like you built a thing worth writing about."
    "Narration:"
    "Rafi's energy is light but steady; his camera bobs like a bird. He pours through the lab with a practiced eye, framing the kelp fronds against the window like a native who knows how to make ordinary things look like miracles."

    rafi_soto "Headlines or humanity? Which way do you want the lede?"

    maya_kestrel "Both,' you answer, even as your chest tightens. 'Make it about the people who gave it time."

    rafi_soto "Good. I already have quotes. Neighbors who took the kits called me at dawn — three towns, Maya. People want to try this. They want to learn."
    "Narration:"
    "Warm light pools on the concrete as you let that land. Three neighboring towns — a lattice forming. For the first time in a long while, scale doesn't sound like a sell-out. It sounds like other hands coming to the table."

    menu:
        "Offer Rafi a wet-net photo — make it about craft":
            "You hand him the wet net; he takes a close shot of your hands. He says, 'This is the frame I wanted.' The article will keep the work centered."
        "Ask him to focus on the pilot families — make it about people":
            "You point him to the bench where an apprentice sorts seedlings, and he follows. His notes become humane, names and all. The piece will carry faces into policy rooms."

    # --- merge ---
    "The scene continues."
    "Narration:"
    "You and Ilias move through small domestic rituals: he shows you a stitch for repairing a buoy line, you show him how to cradle a seedlet without crushing the tender holdfast. These are not glamorous things; they are stitches in a town's future. They are the language you speak together."

    ilias_navarro "We could run a short workshop on the boardwalk next week. Hands-on, we bring the kits."

    maya_kestrel "If three towns volunteer, we make materials for easily reproducible sessions. Open-source, yes, but taught in community rooms — people teaching each other."

    ilias_navarro "Exactly. Proof-of-concept through people, not press releases."
    # [Scene: Regional Symposium — Conference Hall | Midday]
    hide maya_kestrel
    hide ilias_navarro
    hide rafi_soto

    scene bg ch11_e67f19_2 at full_bg
    # play music "music_placeholder"  # [Music: Light piano with intermittent motivational brass]
    # play sound "sfx_placeholder"  # [Sound: Quiet murmur of applause, the rustle of programs, the click of a projector]
    "Narration:"
    "Hana's voice is precise and soft, the kind that makes technical detail feel humane. She walks through your shared data like someone reading a poem no one thought could be measured — survival rates, propagation curves, and the simple metric that mattered most: how often a kit got tended."
    show dr_hana_sato at left:
        zoom 0.7

    dr_hana_sato "What surprised us was adherence. When communities owned the care, success multiplied. It's not just biology; it's social infrastructure supporting biology."

    dr_hana_sato "This is replicable in small ports with similar hydrology. We modeled three pilot rollouts and found interruption risk is low when implemented with buffer coordination."
    "Narration:"
    "Applause ripples. The room smells faintly of coffee and polished badges. You sit with Ilias's hand lightly on your knee — a steady pressure — and notice how presence feels like a method in itself."

    "Audience Member" "What about industrial projects nearby? Heavy machinery can alter turbidity and flows quickly."

    dr_hana_sato "Then we coordinate. Time buffers matter. Simple rules: no heavy trenching in agreed zones during propagation windows; turbidity monitors; communication channels. It's not that complicated — it's that political."
    "Narration:"
    "The question hangs like a bell. You imagine machines, a line of bulldozers regrading a shoreline. You imagine the seeded trays in the shallows, tiny and patient. The applause after Hana's answer sounds like hope, but there is an edge: momentum invites other actors to move faster."

    menu:
        "Stay after the panel to answer a delegate's detailed question":
            "You stay. You answer with the practical steps the delegate needs. He leaves with a list and a commitment to test the kit."
        "Slip out quickly to call Mayor Ansel about emergent pressure":
            "You leave the room with the briefing in your pocket. Your call gets his voicemail, but your message lands: 'We need time.' It's sent into the bureaucracy now."

    # --- merge ---
    "The scene continues."
    "Narration:"
    "The regional press pickups are gentle at first — headline about 'neighbors teaching neighbors' — but the human story Rafi writes carries weight. His piece doesn't fetishize novelty; it shows a mother explaining seedlings to her"
    "grandson, an apprentice with calloused hands counting success rates. By late afternoon three municipal councils have reached out asking for kits and training."
    show rafi_soto at right:
        zoom 0.7

    rafi_soto "This is the cleanest echo I've seen in months. People want to try before they bet everything on steel."

    "Maya Kestrel (quiet, to Ilias)" "For once, scaling doesn't feel like selling out."
    show ilias_navarro at center:
        zoom 0.7

    ilias_navarro "It feels like tying slack lines together into a net."
    "Narration:"
    "You let that image settle: a net not to capture but to hold. Hope feels engineered and living, braided."
    # [Scene: Harborfront — Early Evening]
    hide dr_hana_sato
    hide rafi_soto
    hide ilias_navarro

    scene bg ch11_e67f19_3 at full_bg
    # play music "music_placeholder"  # [Music: Low, tender cello; a slow ascending motif]
    # play sound "sfx_placeholder"  # [Sound: Distant engine noise, gulls calling, the slap of water on pilings]
    "Narration:"
    "You are halfway to promising yourself dinner when the courier's steps quicken. The Mayor's expression tightens — his usual practiced reserve folding into a real, public strain. He looks toward the Skyhub platform where, earlier, sleek"
    "vehicles had moved in for an inspection. There is a message in his fingers, weightier than the paper."
    show mayor_ansel_reed at left:
        zoom 0.7

    mayor_ansel_reed "Maya. There are regional directives: Seren Blake's firm is preparing mobilization — heavy equipment. They say it's urgent. Pressure came down this afternoon."
    "Narration:"
    "The coral at your throat seems to pulse like a metronome. You try to keep your face steady, because your face will be judged here as much as your words."
    show maya_kestrel at right:
        zoom 0.7

    maya_kestrel "Urgent how? A storm window? A permit timeline?"

    mayor_ansel_reed "They framed it as protecting regional freight lines. There's funding attached; they say delay risks cascading impacts. The regional coordinators want a decision this week."
    "Narration:"
    "You feel the scale of this pressure like a physical current under your boots. If machines move, the pilots in the shallow morphologies you're trying to nurture could be buried or dislodged. If you force a pause, the Mayor risks being painted obstructionist when the region needs 'swift action.'"
    show ilias_navarro at center:
        zoom 0.7

    ilias_navarro "We could map the pilot zones and ask for temporary buffer zones. It would be technical; it would be defensible."

    mayor_ansel_reed "Seren Blake will want timeframes. She's efficient. She'll expect a seat at the table."
    "Narration:"
    "You picture Seren Blake with her pristine cuff and sharp contours: efficient, decisive, the kind of person who makes fast choices look inevitable. You have not negotiated with her directly since the earlier town meetings; your"
    "last impressions are of press-ready poise and a willingness to close the calculus on uncomfortable human margins. The council will listen to a plan that looks administratively tight."
    hide mayor_ansel_reed
    hide maya_kestrel
    hide ilias_navarro

    scene bg ch11_e67f19_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant tractor, a gull shriek]
    # play music "music_placeholder"  # [Music: The cello motif lifts into a hopeful, urgent rise]

    "Dr. Hana Sato (arriving, breathless)" "I just got off a call. Seren Blake's team says they'll begin preliminary grading in ten days."
    "Narration:"
    "Ten days. Your throat closes around the number like a knot. Ten days is both short and monumental: long enough for you to seed and monitor a first-cycle, if you race; short enough for heavy equipment to come through and erase the microtopography you rely on."
    show rafi_soto at left:
        zoom 0.7

    rafi_soto "If we publicize the overlap — show staged maps and timelines — we could make it politically costly to bulldoze through pilot zones."
    show mayor_ansel_reed at right:
        zoom 0.7

    mayor_ansel_reed "Political cost is measured in headlines and votes, Rafi. The region counts budgets."
    show ilias_navarro at center:
        zoom 0.7

    ilias_navarro "We don't have to be adversarial to be protective. A formal coordination agreement could ensure buffer zones while they proceed elsewhere."
    "Narration:"
    "Your head splits into calculations — a thousand small, consequential trades. Each option feels like a different kind of fidelity: fidelity to the community's way of caring, fidelity to pragmatic compromise, fidelity to scaling quickly before the machines arrive. You can already hear the counter-narratives forming: 'obstruction', 'naïveté', 'pragmatism.'"
    "Maya Kestrel (internal) You measure what you can give and what you cannot. You are a planner; you are trained to render messy trade-offs into contours that can be negotiated. But planning is also promise. If"
    "you allow heavy machinery to run through these zones, what promises break? If you lean into broad publicity, can the town withstand a public fight? If you accept outside funds now, do you lose the open-source"
    "heartbeat that made neighbors volunteer in the first place?"

    ilias_navarro "Whatever we choose, we do it together. With data, with people. Not behind closed doors that forget names."
    hide rafi_soto
    show dr_hana_sato at left:
        zoom 0.7

    dr_hana_sato "I can present an urgent addendum to the region — turbidity monitors, a recommended sequencing map. It will carry weight. It won't stop everything, but it could buy days."

    mayor_ansel_reed "They want us to choose."
    "Narration:"
    "You feel the lab lights hum in your memory like a small engine of will. Your coral pendant pulses against your throat like a question — not accusatory, but attentive. The town's volunteers have already committed"
    "labor and trust. The pilots are fragile but alive. The region wants speed; your work asks for time."

    menu:
        "Ask Hana to draft the addendum tonight — technical buffer plan":
            "Hana nods, already thinking in schemas. 'Give me parameters,' she says. You hand her the seed maps. She's gone inside her head, and you can see a defensible plan forming."
        "Tell Rafi to publish an urgent piece about the timeline to galvanize public scrutiny":
            "Rafi's face lights up with the work. He types furiously; the narrative will reach morning readers and pressure the region politically. You feel the tremor of public attention aligning with your work."

    # --- merge ---
    "The scene continues."
    "Narration:"
    "Your chest loosens a little at the sight of people moving — not simply reacting, but organizing. That is the town's best muscle: to turn panic into careful action. You can feel a hopeful cadence threading through the anxiety."
    hide mayor_ansel_reed
    show seren_blake at right:
        zoom 0.7

    seren_blake "We are prepared to coordinate on minimal buffers if the town provides clear, GIS-defined zones within 72 hours. Otherwise, our timetable is fixed."
    "Narration:"
    "Her message is efficient and oddly open — but precise. You recognize the calculus: she offers a path that puts the onus of definition on you. You could define protective zones and get a formal agreement;"
    "you could refuse and push the square of public scrutiny; you could take an offer that accelerates your own work, with strings. Each route has its own blend of gains and losses."
    hide ilias_navarro
    show mayor_ansel_reed at center:
        zoom 0.7

    mayor_ansel_reed "Decisions in three days, Maya. You have political actors calling. I can hold a short session if you want to present options."
    hide dr_hana_sato
    show ilias_navarro at left:
        zoom 0.7

    ilias_navarro "Whatever you choose, I'll be there to present the data, the people, and the method. We'll show them how this scales without erasing."
    "Narration:"
    "The harbor wind rubs salt across the back of your neck. Your notebook — your armor — sits heavy in your bag. For a moment, you imagine the pilot plots laid like seeds on a grid,"
    "each one a small story. The room of the region is not a laboratory bench; it's a web of interests and timetables. The choice is not only technical."
    "Maya Kestrel (internal) You breathe. The rise in the music in your mind matches the hope you can nearly touch: people are mobilizing; pilots have volunteers; Dr. Hana Sato and Rafi and Ilias have momentum. Even"
    "Seren Blake's message, at its sharpest, is an opening for negotiation rather than an ultimatum. The ascent is not guaranteed, but the vector is up."
    "Narration:"
    "You square your shoulders and look across the boardwalk at the crowd — the apprentices packing seed trays into a battered van, neighbors talking in low urgent voices, a child pointing at the puddles where seedlings"
    "might someday fledge. The thing you protect is not only biology but a way of living that teaches people to keep watch."
    # play music "music_placeholder"  # [Music: Swells into a hopeful chord; strings and piano intertwine]
    hide seren_blake
    hide mayor_ansel_reed
    hide ilias_navarro

    scene bg ch11_e67f19_5 at full_bg
    "Narration:"
    "There is a decision to make, and it will define the next steps. You feel the town's breath behind you, and the science at your elbow, and something like affection warming your hands."

    menu:
        "Seek a formal coordination agreement with Seren to protect pilot hydrology zones.":
            jump chapter12
        "Double down on grassroots deployment and publicize potential conflicts, forcing political scrutiny.":
            jump chapter14
        "Accept a private research grant to scale quickly and prove effectiveness before Seren’s machines start.":
            jump chapter18
    return
