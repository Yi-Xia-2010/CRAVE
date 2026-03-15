label chapter7:

    # [Scene: Voss Development Office (Glass Tower) | Morning]

    scene bg ch7_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm, cautious piano with a rising string undercurrent]
    # play sound "sfx_placeholder"  # [Sound: The distant murmur of protest through the tower's filters — muffled chants and the occasional drum; inside, the quiet hum of HVAC and soft typing]
    "You step into a space that was designed to make things feel inevitable. The light here is clean enough to show every flaw; when you pass the chrome wall your patched jacket answers back at you"
    "like an accusation and a truth both. Your reflection is small and stubborn between the steel lines: a weathered pair of shoulders and the thin braid on your wrist that keeps you tied to Atera's hands-on"
    "work."
    "Soren Voss is already standing by the table, his silhouette precise against the holo-model he conjures with a tap on his transparent data-bracelet. Pale-gray eyes lock on you as if reading an elevation plan instead of"
    "a person. He doesn't smile — not yet — but his voice is designed to make solutions sound close and reasonable."
    show soren_voss at left:
        zoom 0.7

    soren_voss "Thank you for coming, Mika. Mayor. Elias. Jun.' (He inclines slightly.) 'We have a narrow window to secure funding. My plan raises the streets along the primary corridors, installs a resilience corridor along the bay, and packages incentives for investors. It's fast, measurable, and fundable."
    show mayor_amina_bakar at right:
        zoom 0.7

    mayor_amina_bakar "We need fundable and accountable.' (Her voice wears the tired steadiness of someone who balances petitions and footnotes.) 'But we also need the town in these plans."
    "Elias Maren shifts in his chair, fingers worrying the corner of his field notebook. He looks at the model through the holo as if counting currents between the digital buoys."
    show elias_maren at center:
        zoom 0.7

    elias_maren "The corridor idea could work if the shorelines are living systems rather than just stone and concrete. Kelp beds, engineered marshes — they absorb wave energy and create jobs for people who know the water."
    "Soren Voss taps the bracelet. A slice of the model rotates: grey raised streets, linear storm walls. He nods like a careful composer."

    soren_voss "Those features can be integrated. It increases initial costs, but it provides community benefits and—' (he searches for the right phrase) '—marketable resilience."
    "You feel the meeting like a tide pulling at different shoals. On one side: Soren's clarity and momentum. On the other: the messy, living work Elias sketches and that your hands know. Saying nothing is its"
    "own kind of decision. You clear your throat and find Soren's language easier than you expected — timelines, deliverables, milestones — but you use it to push."
    hide soren_voss
    show mika_hoshino at left:
        zoom 0.7

    mika_hoshino "If we do this, the plan needs clauses. Living-shoreline buffers with maintenance scheduled and funded. A community employment quota — not just contractors flown in for the build. And local governance oversight, with a veto on any zoning changes that displace long-standing fishing plots."
    "Soren Voss's jaw tightens for a heartbeat, then smooths."
    hide mayor_amina_bakar
    show soren_voss at right:
        zoom 0.7

    soren_voss "Fair. We can structure a community stewardship board embedded in the development trust. Employment quotas can be tiered and audited. The living shorelines — we'll set adaptive performance targets. If the systems don't meet them, there are penalties and remediation."
    "Jun Park leans forward, voice low and rough with sawdust and skepticism."
    hide elias_maren
    show jun_park at center:
        zoom 0.7

    jun_park "Penalties don't stop losing control. We need lines on the map that only locals can redraw. A quota is words on a page unless the people enforcing it live here and answer to the people who do the work."
    "Soren Voss regards Jun like one inspects a structural member for load-bearing capacity."

    soren_voss "We can write community appointment processes into the governance charter. Appointments, recall provisions, transparency portals — yes. The funders will want an external auditor for confidence, but the charter can mandate majority-local decision thresholds for cultural and occupational displacements."
    "Amina Bakar exhales, the movement a small, private relief."
    hide mika_hoshino
    show mayor_amina_bakar at left:
        zoom 0.7

    mayor_amina_bakar "If it's verifiable, if the charter is legally binding with local seats, then the council can consider the proposal. But I need exact language, timelines, and fallback funding in case ecological measures don't reach targets quickly enough."
    "Elias Maren presses a hand to the table, eyes bright with more than theory."
    hide soren_voss
    show elias_maren at right:
        zoom 0.7

    elias_maren "We'll design the ecological offsets to show demonstrable ecosystem services within two seasons. Pilot kelp farms seeded next month, living-breakwater platforms installed within six months. They won't only be mitigation; they'll be part of the town's economy — training, harvest partnerships, micro-enterprise grants."
    # play sound "sfx_placeholder"  # [Sound: A low chant rises outside the glass. Riv's voice floats in — sharp, earnest. A placard bobbles on a sea of neon bandanas.]
    "Riv's presence is a pulse: immediate, impatient, necessary. You feel the town pressing through the glass in shouts and songs."
    "Soren Voss's face doesn't close. If anything, his cadence shifts toward the rhetorical, the kind of persuasive rhythm that soothes funders and mayors."
    hide jun_park
    show soren_voss at center:
        zoom 0.7

    soren_voss "These are the deliverables I'd present to investors. Clearly mapped outcomes, public oversight, and a projected ROI timeline that keeps funding flows steady. Atera's story becomes one others want to fund."
    "You notice yourself borrowing his icons — 'deliverables,' 'ROI' — and it feels less like mimicry and more like learning the dialect of change so you can hold Soren to it. Language is leverage."
    hide mayor_amina_bakar
    show mika_hoshino at left:
        zoom 0.7

    mika_hoshino "Then let's write them into the RFP. Living shoreline performance targets, staffing and apprenticeship quotas for locals, an independent community stewardship board with recall powers, and a binding review clause if ecological targets aren't met."
    "Soren Voss smiles just enough — a plan coming into focus."

    soren_voss "Agreed, in principle. We'll draft the RFP with those clauses. I'll stipulate funding for apprenticeship programs during the construction phase. We'll also commit to a phased build so we can measure and adapt. That should appease anxious funders and allow for ecological adjustments."

    menu:
        "Push for legally ironclad wording now — don't leave room for later wiggle.":
            "You lean in, voice steady. Soren's calm meets your firmness. He nods, and the air tightens as the team prepares to draft precise clauses. Elias exhales, relief soft and immediate. Jun's knuckles whiten on the table, hopeful."
        "Accept his 'in principle' and demand a transparent timeline for final legal wording — for now, secure commitments and move to public oversight.":
            "You choose the steady pragmatic route. Soren's eyes show the faintest respect — someone willing to shepherd the process rather than stage a win. Amina makes a note. Elias murmurs agreement: a phased path is survivable if strict checkpoints are signed by funders."

    # --- merge ---
    "Soren looks at the holo again and taps a node; the model unfurls to show a raised bluff plan with new terraces and stairways, pedestrian corridors that rise with the street grid. You all stand and"
    "move to a glass balcony that cantilevers over the town. The air hits you as you step outside — sea-salt, diesel from a distant boat, the clean bite of morning."
    # [Scene: Raised Bluff / Tower Balcony | Morning]
    hide elias_maren
    hide soren_voss
    hide mika_hoshino

    scene bg ch7_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Protestors below chant in rhythmic bursts; gulls wheel; the breath of wind moves through your jacket like a metronome.]
    "You learn Soren's cadence by translating his timelines into things you understand: seasons, harvests, tide cycles. He listens when you say it that way — not merely polite, but attentive."
    show mika_hoshino at left:
        zoom 0.7

    mika_hoshino "If the raised corridor is built in phases tied to ecological metrics, then we can seed the kelp beds before heavy construction starts. The kelp will reduce wave energy and buy time for terraces to settle. We need those buffer periods written into milestone triggers."
    show soren_voss at right:
        zoom 0.7

    soren_voss "We can program construction-halting triggers into contracts. If wave attenuation metrics fall below thresholds, we pause and remediate. It costs money, but it's insurable. And importantly, it demonstrates adaptive governance."
    "Elias Maren steps close to the railing, pointing toward the kelp-dark water at the harbor mouth."
    show elias_maren at center:
        zoom 0.7

    elias_maren "Those platforms there — if we anchor experimental breakwaters and kelp attachments — they become demonstrable offsets. I'll design them with measurable carbon drawdown and wave attenuation metrics, and we can publish monthly community reports."
    hide mika_hoshino
    show jun_park at left:
        zoom 0.7

    jun_park "And the jobs? Don't make them 'training' unless there's steady work after the build. Otherwise we hand people a ladder and then take it away."
    "Soren Voss's hand moves — not to the bracelet now, but to the small, human gesture of showing a folded photograph from his wallet. He hesitates before exposing the image: a woman standing on a similar shore, small and resolute in older clothing. The moment is brief; his eyes soften."

    soren_voss "My sister worked in coastal redevelopment. She taught me the human cost of bad planning. I don't want that to be our story. I want this to work for the people who live here."
    "The admission is private and not theatrical. You feel it as a tilt — a small easing of the rigid plan into something that might hold a person."

    "Riv's chants rise into a cadence — a list of demands that, while blunt, are not unreasonable" "Local seats now! Living shorelines! No displacement!"
    "Amina Bakar folds her hands and closes her eyes for a second, collecting the political arithmetic."
    hide soren_voss
    show mayor_amina_bakar at right:
        zoom 0.7

    mayor_amina_bakar "If we go forward, we go with monitoring and enforcement written into every contract, with easily accessible complaint channels and a schedule for community reviews. And if this plan is to pass, we have to present it to the public with clear points of accountability."
    "Soren Voss nods. 'Agreed. Public presentation with a transparent timeline. I'll commit to including third-party environmental auditors and a contingency fund for community relocation assistance should any displacement be unavoidable.'"
    "Elias Maren looks at you, then at Soren, then back to the harbor. You see the wariness in him soften into a kind of practical hope."

    elias_maren "If we can model the offsets and show draft data within two months, the town will have something tangible to point to. People respond to measurable change."
    hide elias_maren
    show mika_hoshino at center:
        zoom 0.7

    mika_hoshino "Then we set measurable change as the standard. Not just promises. Not just aesthetics. Deliverables that the town can verify."
    "The conversation moves like tide: a pull, a pause, a readjustment. Jun's warning is still there, but so is a growing scaffold of compromise. Soren is giving language where there had been diagrams; Elias is giving"
    "science where there had been worry; Amina is pairing both with the practical checks the council needs."
    # [Scene: Mika's Workshop / Rooftop Lab | Noon]
    hide jun_park
    hide mayor_amina_bakar
    hide mika_hoshino

    scene bg ch7_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft drip of condensation in the greenhouse; a radio saying, "City channels report negotiation progress" in the background]
    "Elias Maren moves like someone who has carried ideas back from the sea each season: hands sure, eyes imagining blue. He outlines the first pilot: living-breakwater modules built from reclaimed material, kelp spores seeded from community boats, a rotating apprenticeship roster so locals learn monitoring and maintenance."
    show elias_maren at left:
        zoom 0.7

    elias_maren "We'll set up monitoring stations that feed into a public dashboard. Real-time data on biomass growth, water clarity, and wave attenuation. Your workshop becomes a hub — repair, training, and a staging ground for crews."
    "You let the words land. The idea of your workshop — the dented key to your mother's bench, the patchwork benches — becoming a formal hub makes a small, fierce pride glow inside you."
    "Jun Park drops a bundle of lumber by the door, voice blunt as ever."
    show jun_park at right:
        zoom 0.7

    jun_park "Don't let them privatize the hub. Make it co-op-owned. We'll put the charter in the RFP so it's guaranteed."
    show mika_hoshino at center:
        zoom 0.7

    mika_hoshino "We'll draft that clause. Co-op ownership with a majority-local board. Apprenticeships guaranteed through the development trust."
    "Jun Park grunts, satisfied in the way a craftsman is when a cut finally fits."
    "Across town, Riv organizes outside the tower. You can picture the bright bandanas and the way his grin fractures into speeches and strategy."
    "You feel tired, but the fatigue is the kind that follows honest work. The negotiation hasn't been a surrender; it's been sanding a rough plank into something that can bridge a gap."
    "Soren Voss calls you later in the afternoon. His voice through the line is the same composed cadence, but there's less of the polished edge now."
    hide elias_maren
    show soren_voss at left:
        zoom 0.7

    soren_voss "The funders asked for a preliminary RFP by week's end. We've framed the deliverables to include living shoreline performance, apprenticeship funding, and a stewardship board with recall provisions. Amina has tentatively supported a public presentation next Thursday."

    mika_hoshino "Then we make the RFP unassailable. We make the deliverables measurable and public. We demand funding lines for remediation and local governance."

    soren_voss "Agreed. I'll have legal draft the clauses. Bring any wording you want to the table; I'll incorporate it. We move fast, but not so fast the town can't breathe."
    "You close your eyes for a second, picturing the harbor again — not as it is, but as it might be: raised streets threading through restored marsh, kelp beds bobbing like dark medals, your workshop doors open with boards of names on them."
    "A fragile trust has begun along that thin seam between pragmatism and principle. It is not complete. It may never be complete. But for the first time since the flood, the town has a plan that"
    "stitches engineering to ecology, that promises jobs and oversight, and has people — real people — appointed to hold the seams together."

    "Your phone vibrates with a message from Riv" "Keep pressure. We trust you. We watch you."
    "You step out onto the raised bluff again as the sun tilts lower. The town's lights begin to wink on. The plan is fragile and full of edges, but it moves. That movement feels, today, like hope."
    # [Page-Turn Thought: The contract language will be written tomorrow, but tonight you carry the shape of it in your head — clauses like compass points. If the RFP holds measurable clauses, if apprenticeships are funded, if the stewardship board has teeth, then Atera might not only survive the next storm; it might teach others to do the same. You fold that possibility into your pocket like a map and step back toward the tower — toward the public presentation when every clause will be read aloud and weighed.]
    # play music "music_placeholder"  # [Music: Brightening strings swell into a hopeful motif]
    hide jun_park
    hide mika_hoshino
    hide soren_voss

    scene bg ch7_453e40_4 at full_bg

    scene bg ch7_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter8
    return
