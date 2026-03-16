label chapter4:

    # [Scene: Harrow Bay — City Archive & Council Hall | Early Morning]

    scene bg ch4_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: High-tempo strings under a driving percussion]
    # play sound "sfx_placeholder"  # [Sound: A distant gull; the low murmur of a city waking]
    "You walk out of the chamber with the weight of signatures cupped in your hands. The expedited contract is inked; the city’s coffers have been opened. The word 'now' hums behind your ribs — a heavy,"
    "electric thing. You can still feel the chair's oak under your palms, remember the Council Chair's measured cadence as if it were someone handing you a detonator wrapped in good intentions."
    show maya_soren at left:
        zoom 0.7

    maya_soren "I'll take responsibility for the oversight team and the monitoring plan."
    "A chorus of relief washes the room — polite applause, a few relieved exhalations, the quick exchange of congratulatory murmurs. Relief hits you like tidewater: sudden, buoyant, and cold. But beneath that buoyancy is a jagged current you taught yourself to read."
    "You tell yourself the checks are in place. You tell yourself Jonas and Lena and the escrow line will be enough. You check the tablet, watch the contract confirmation blink green. The promise of action is"
    "intoxicating and immediate. Your chest tightens with the knowledge that 'immediate' will cost people things you can't yet name."
    # [Scene: Coastal Research Vessel "Aster" | Midday — Out at Sea]
    hide maya_soren

    scene bg ch4_453e40_2 at full_bg
    # play music "music_placeholder"  # [Music: Percussive, metallic rhythms; a low brass pulse]
    # play sound "sfx_placeholder"  # [Sound: Wind thrumming, the slap of waves, commands shouted over headsets]
    "You board the Aster with the contract in your satchel and a list of monitoring protocols in your head. Elias Voss meets you on the foredeck, grin already half-assembled against the sea wind. He holds a"
    "line, then drops it when he sees you; the sound is a small, private call."
    show elias_voss at left:
        zoom 0.7

    elias_voss "We didn't waste any time.' (He laughs, but there’s an edge you can't miss.) 'Crews are staged. Pylons are prepped. Living-reef modules pre-seeded and ready for placement."
    show maya_soren at right:
        zoom 0.7

    maya_soren "You went ahead with the deployment schedule?"

    elias_voss "You signed us in, Maya. I signed on the logistics. We're on the clock; the harbor's window isn't forever.' (He reaches for your shoulder; a quick, grounding touch.) 'We can do this without cutting corners."
    "The Aster's lab smells of algae, antiseptic, and hot metal. Technicians move between crates, their boots clanking against the deck — a percussion line marking the beginning of an irreversible rhythm. You walk the line with"
    "Elias, checking tags, scanning QR chips. Every module has your initials on the monitoring log. Every pylon will be hammered through seabed that remembers older storms as if they were scars."

    menu:
        "Check the module integrity one more time":
            "You kneel, fingers numb from the wind, and run your diagnostic pad across the module seams. The readout flickers, then stabilizes — enough for now."
        "Trust Elias and brief the crews":
            "You stand, hand Elias the tablet. His approval is fast and efficient. The crews tighten their lines and the Aster starts to spit distance between bow and harbor."

    # --- merge ---
    "You choose."
    "The first pylons go in with a sound like the world taking a breath — heavy, purposeful, final. The living-reef modules unfurl like sleeping things waking, anchored in place by bolts and collective will. Cameras roll;"
    "municipal cameras, private feeds, live streams. Your face is in a hundred small squares, a leader turned into motion."
    show dr_lena_huang at center:
        zoom 0.7

    dr_lena_huang "We monitor chemical gradients and benthic response at 24, 48, and 72-hour intervals. If you see significant anoxic shifts we pause."

    elias_voss "We will. We know what to look for."
    "As the Aster turns back toward harbor, your stomach is a knot of adrenaline and premonition. The net result is palpable: the pylons gleam in renders and in the water like promises. You feel the city breathing behind you—expectant, eager. The initial wave of praise arrives before the sun sets."
    # [Scene: Boardwalk & Promenade | Late Afternoon]
    hide elias_voss
    hide maya_soren
    hide dr_lena_huang

    scene bg ch4_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: A triumphant brass swell that quickly frays into uneasy minor strings]
    # play sound "sfx_placeholder"  # [Sound: Cheers, camera shutters, the low simmer of debate; children laugh nearby]
    "You step onto the boardwalk and the applause hits like surf. Flags flail. Reporters push microphones toward you. Asha Reed stands at the edge of the press cordon, arms folded, not clapping. Her presence is a temperature shift: a single body that reads 'no' against a chorus that says 'yes.'"
    show rosa_calder at left:
        zoom 0.7

    rosa_calder "You did good, niña.' (Her voice is a thread of earth and memory; she squeezes your hand with arthritic certainty.) 'My garden will sleep a little safer."
    show jonah_mek at right:
        zoom 0.7

    jonah_mek "You kept your word — you moved fast when it mattered.' (He grins, but his eyes flick to rooftops and stilts, calculating what comes next.) 'We can shore up enough houses if we get this right."
    "Cameras angle to catch your profile, to freeze the moment of triumph. You answer questions with practiced brevity. You cite monitoring protocols and emergency contingencies, the escrow and the independent auditors. The crowd eats the scaffolding of your accountability with hunger."
    show elias_voss at center:
        zoom 0.7

    elias_voss "This is step one.' (He turns the mic toward you, deferring to the plans you wrote.) 'We still need to scale kelp beds and watch the marine life. But the pylons — they'll buy us time."
    hide rosa_calder
    show dr_lena_huang at left:
        zoom 0.7

    dr_lena_huang "I want to reiterate: we cannot assume no impact. Kelp transplantation changes nutrient flows.' (She looks at you squarely; the scientific caution in her eyes is an unlit fuse.) 'If we see eutrophication we stop and reassess."

    "The praise is real and so is the undercurrent of warning. Words now swing back and forth like flags in a storm" "win' and 'cave-in'; 'progress' and 'ecological trade-off"

    menu:
        "Step between Elias and the press to deflect tough questions":
            "You raise a hand, redirecting a loaded question into procedural language. The crowd nods, mollified."
        "Let Elias take the heat and answer with technical detail":
            "Elias leans in, his voice steady. He draws eyes away from you with confident, measured explanations."

    # --- merge ---
    "The choices you make now don't change the pylons, but they shape how the city remembers this day."
    # [Scene: Lower Quay — Narrow Alleyways & Stilted Homes | Dusk]
    hide jonah_mek
    hide elias_voss
    hide dr_lena_huang

    scene bg ch4_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Taut strings with a sharp violin motif; percussion accelerates]
    # play sound "sfx_placeholder"  # [Sound: A nearby radio plays a distant news report; a raised voice cuts through the alleys]
    "You arrive to find a crowd — fewer than the boardwalk, but louder in the way a hurt neighbor is louder than an applauding stranger. Asha Reed steps forward with the force of someone who has"
    "been waiting. Her notebook is open; her voice is a blade honed on every wrong she has seen."
    show asha_reed at left:
        zoom 0.7

    asha_reed "You sold out.' (She doesn't whisper. The accusation lands like a thrown stone.) 'You signed their contract and handed them the docks behind the people's backs."
    show maya_soren at right:
        zoom 0.7

    maya_soren "You know that's not true.' (You take a breath, searching for the soft place between what you did and what she feels.) 'We put monitoring in place. The contract has clauses for review and suspension."

    asha_reed "Clauses won't mend lost fisheries or paid-off compromises.' (Her eyes are bright; fury has that strange clarity.) 'You put built solutions before people who live here. You let them decide the terms instead of letting us keep them."
    "The crowd tightens. Jonah steps up to you with a measured, brotherly look, trying to be the buffer between two friends turned antagonists."
    show jonah_mek at center:
        zoom 0.7

    jonah_mek "Asha — we all want the same thing. Maya moved the line because we needed a fence between us and the sea."

    asha_reed "That fence costs more than wood and metal. It costs the liberties of those who always paid the price so others could sleep easier.' (She shakes her head.) 'You promised transparency, Maya. But you signed with them."
    hide asha_reed
    show elias_voss at left:
        zoom 0.7

    elias_voss "We were transparent about the funds and the oversight.' (His voice rises; when Elias sharpens, it cuts quick.) 'We can't wait for the perfect study while streets flood."
    hide maya_soren
    show asha_reed at right:
        zoom 0.7

    asha_reed "You can't just call it 'buying time' and expect that erases who benefits.' (She looks directly at you, and for a moment her face is nothing but hurt and accusation.) 'What will you do when the fishermen lose their nets to shifting currents because we rushed?"
    "The moment fractures. Words spill like broken glass. The air sits heavy with all the things neither side said earlier: the displaced garden beds you once authorized; the elderly who moved because of prior projects; the"
    "friend who whispered they felt sold out the first time a developer put profit ahead of people."
    hide jonah_mek
    show dr_lena_huang at center:
        zoom 0.7

    dr_lena_huang "If I may—' (She steps in, scientific calm trying to mediate.) 'We need to collect baseline data immediately. We monitor salinity, dissolved oxygen, nutrient loading. We must be ready to dismantle modules if thresholds are exceeded."

    asha_reed "And who decides the thresholds? You? The company that wrote the contract?' (Her voice shakes with a single exacting fury.) 'Power decides. Power is the problem."
    "The crowd splits into murmured factions. People you thought neutral shift like weather vanes. The alliances you've held together with meeting minutes and good intentions begin to fray, thread by delicate thread."

    menu:
        "Appeal to the crowd, promising immediate independent audits":
            "You raise your hands and promise audits led by community representatives. A few heads nod; doubt lingers like fog."
        "Call for a pause and insist on on-site testing before further installations":
            "You call for immediate sampling. Technicians scramble; the crowd waits with an edged silence."

    # --- merge ---
    "You try both words and procedure. Neither calms the tidal pull of mistrust."
    "Elias steps closer to Asha, voice low and edged."

    elias_voss "You know I'm trying to fix things, Asha. I—"

    asha_reed "Trying isn't the same as choosing the right things, Elias.' (Her look at him is Exasperation made human.) 'You saw the grants and you wanted the hero moment."

    elias_voss "I wanted a chance to make a difference without our hands tied."
    "Your throat closes. The air tastes of salt and iron and accusation. The crowd leans in as if expecting a physical blow; instead they get something worse: the slow, visible unraveling of trust."
    "Rosa Calder squeezes your arm, her voice small but fierce."
    hide elias_voss
    show rosa_calder at left:
        zoom 0.7

    rosa_calder "We have always known that trade-offs are part of survival.' (She looks at you with a thousand years of garden seasons in her eyes.) 'But make sure you are trading for us and not just for a promise that sounds good on a podium."
    "You feel the hinge of the day — the moment the city's face changes from hopeful to suspicious. Voices overlap; someone shoves a microphone closer to Asha and she accepts it like a gauntlet."

    asha_reed "This isn't only about technology.' (She points, then looks at you.) 'It's about who holds the keys when the levees are down. And you... you chose their bank."
    hide asha_reed
    hide dr_lena_huang
    hide rosa_calder

    scene bg ch4_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: The percussion snaps to silence, then returns as a furious, racing drumbeat]
    # play sound "sfx_placeholder"  # [Sound: A collective intake of breath; a child begins to cry somewhere in the crowd]
    "You realize, with the bone-deep clarity of someone who has made a decision that will not be undone, that the city's trust is now conditional, fragile as sea glass. The praise that came earlier feels like a distant shore — visible but unreachable from this swell."
    "This is the fall: alliances that once held firm begin to shift, to argue in corners, to redraw lines in the sand. You hear the first phrases of fracture — 'sold out,' 'compromise,' 'who benefits?' — and they echo long after the boardwalk's applause has faded."
    # [Scene: The Boardwalk Overlook | Night — Harbor Lights Flicker]

    scene bg ch4_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Low, unresolved cello; a distant, single trumpet]
    # play sound "sfx_placeholder"  # [Sound: Waves, the murmur of debate continuing in pockets]
    "You stand alone for a breath, the satchel heavy at your side. Elias squeezes your hand — an anchor. Jonah stands nearby with a careful, frayed grin. Rosa's shawl smells of earth and salt. Asha's silhouette walks away into the alleys like a star gone out."
    "You think of the contract — of clauses that will be parsed by lawyers, of audits that will become battlegrounds. You think of the living-reef modules breathing in a sea that does not owe you mercy."
    "You think of all the faces turning from applause to accusation, of how quickly 'help' becomes 'harm' in the ledger of a strained city."
    "Your chest feels raw; the city's heartbeat is a drum you once tried to steady with plans and spreadsheets. Now it sounds like a warning. The emotional pressure inside you builds — tight, urgent, a storm swelling on the horizon."

    scene bg ch4_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Strings rise to a fevered pitch, then cut to silence]
    "You know the work will continue tomorrow. Contracts will be parsed, sensors deployed, community meetings scheduled. But tonight the horizon is different. Something has shifted in the public's trust and in your relationships. The pylons will"
    "stand, the reef will be in the water, and with them a new, sharper debate has been set loose."
    "You fold the satchel over your shoulder and look out at the pylons — dark teeth against a flat, uncertain sea. In the glow of the harbor lights, you finally understand that signing the contract did"
    "more than buy time: it forced a truth into the open. Whoever holds the next meeting will need to answer not just about engineering but about belonging, about who gets to decide who stays and who"
    "moves. The stakes are higher than you allowed yourself to imagine in the council chamber that morning."

    scene bg ch4_453e40_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
