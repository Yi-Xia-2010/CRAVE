label chapter13:

    # [Scene: Council Chamber Annex | Morning]

    scene bg ch13_f99e88_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm, steady strings; a light optimistic tempo]
    # play sound "sfx_placeholder"  # [Sound: Low murmur of city staff, the occasional rustle of paper and the soft beep of a printer upstairs]

    "You stand at the edge of the oval table, elbows braced on reclaimed-wood. Your seed-bead bracelet hums faintly against your wrist when you move — an old rhythm that keeps you tethered. Elias sits across from you, tablet open, fingers resting over a draft ordinance titled" "Pilot Zone Protections and Co-Management Act."

    "You remember telling him, days ago, that you wanted a document that could be carried back to the neighborhood and read without legalese — something a raft-builder and a council aide could both bring to a meeting and understand. He had smiled, then bit at the corner of a pen and said" "We'll write it like a map."
    "Rani leans in from the doorway, shoulders dusted with sawdust and optimism. Lucia arrives after her, trench cape clasped at the throat, eyes quick and appraising — as unreadable as stormwater on glass. She carries, improbably,"
    "a stack of annotated structural details: elegant sketches that could have been cold, but her voice, when she crosses the room to set them down, is softer than you expect."
    show lucia_montrose at left:
        zoom 0.7

    lucia_montrose "I've marked the reinforcement points that won't cut into the marsh's hydrology. If we stage the work, we can avoid most of the heavy piling."
    "You feel a small, surprised joy at that concession — an engineering voice bending instead of bulldozing. The room leans into the possibility with you."
    show elias_harrow at right:
        zoom 0.7

    elias_harrow "We'll require co-management clauses. Community boards with binding veto on maintenance decisions, local hiring quotas for repair crews, and an open data stream for monitoring performance. Transparency is baked in."
    show mara_solenne at center:
        zoom 0.7

    mara_solenne "And funding? The only reason a pilot survives is payroll and materials. Communities can't be the unpaid labor for infrastructure."
    "Elias taps the tablet."

    elias_harrow "Allocated municipal bonds for pilot zones, reallocated storm-response funds, and a small innovation grant from Beaconworks. It is narrow, but it's immediate."
    hide lucia_montrose
    show rani_cho at left:
        zoom 0.7

    rani_cho "Immediate is a good word. 'Immediate' means people don't have to choose between a paycheck and a training session."
    "Lucia Montrose folds her hands, the pearl brooch catching light. There is a pause — politics and pride balanced on a breath."
    hide elias_harrow
    show lucia_montrose at right:
        zoom 0.7

    lucia_montrose "I'll speak at the public forums and explain the staged engineering approach. If I can frame it as risk management rather than sentimental conservation, we get buy-in from commerce and the council."
    "You watch Lucia choose her words as if she were adjusting a lever; the city responds to tone sometimes before it does to truth. The realization that she will use her influence for this narrow protection feels like coal turning to ember under your palms."

    "The legal language is crisp. The clause on co-management reads plain and fierce" "Pilot zones shall be co-managed by an appointed Community Stewardship Board and the City for a minimum of eight years, with legally enforceable maintenance plans and funding commitments."
    hide mara_solenne
    hide rani_cho
    hide lucia_montrose

    scene bg ch13_f99e88_2 at full_bg
    # play music "music_placeholder"  # [Music: Warm strings swell slightly]
    "You breathe, thinking of the old reed beds in the Drowned Garden, of Eda's hands sifting mud. This ordinance will not save every blade of grass — but it buys time, jobs, a footprint of dignity for neighborhoods that have been treated like margins for too long."
    "Elias folds the template into the city clerk's binder. His expression drifts toward you, an unspoken promise in the set of his jaw."
    show elias_harrow at left:
        zoom 0.7

    elias_harrow "We did the math. We built the contingencies. We made it readable."
    show mara_solenne at right:
        zoom 0.7

    mara_solenne "You made it human."
    "He shakes his head, but there is something like pride there."

    elias_harrow "We made it human together."
    # [Scene: Pilot Zone | Early Afternoon, Weeks Later]
    hide elias_harrow
    hide mara_solenne

    scene bg ch13_f99e88_3 at full_bg
    # play music "music_placeholder"  # [Music: Light percussion with hopeful synth pad]
    # play sound "sfx_placeholder"  # [Sound: Hammers, the slap of boots on decking, distant gulls, laughter]
    "You stand on a freshly lashed pontoon, palms damp from peat. Rani is teaching a pair of trainees how to splice a nylon rope; their hands are clumsy and earnest. Each knot is a promise of paychecks and practice."
    "You feel the first tangible thrum of the ordinance — funded positions, on-the-job training, a payroll sheet that lists local names. The municipal bonds trickle into the contractor that hires neighbors first; Beaconworks sends toolkits and sensors for community monitors."
    show rani_cho at left:
        zoom 0.7

    rani_cho "You remember when the city said they'd only do big concrete? Now look — folks are getting paid to keep the marsh breathing."
    show mara_solenne at right:
        zoom 0.7

    mara_solenne "Feels like we're finally getting paid for the labor nature always did for us."
    "A young woman — a trainee named Sima — looks up, the salt in her hair bright."

    "Sima" "My son won't have to miss school because of rain anymore. I'm actually… I can breathe."
    "You close your eyes at that. The sentence anchors you — smaller than legislation, truer than rhetoric."

    "Elias moves by your side with the open-source playbook printed on recycled paper in his hand. The cover reads" "Community Coastal Maintenance: A Playbook — Co-authored by Elias Harrow & Mara Solenne.' Underneath, a line in your handwriting: 'For keeping wet places wet and people working."
    show elias_harrow at center:
        zoom 0.7

    elias_harrow "We didn't expect the diagrams to take on this much of a life. Your notes about the ebb-lines made the sensor layout better."

    mara_solenne "Your diagrams made my pitch credible at Mateo's hearing. It's a good friendship of skillsets."
    "He watches you as if cataloguing the small ways you both have changed."

    elias_harrow "Partnership."

    menu:
        "Help Rani teach a rope-splice":
            "You kneel beside Rani and guide a trainee's hands; under your fingers the knot becomes a small proud thing. Rani claps them on the back and hands you a mug of tea in thanks."
        "Walk the monitoring transect with Elias":
            "You move along the marsh with Elias, the sensors beeping at the edges of eelgrass. He shows you a data readout; your thumb traces the line where water and soil meet. You both laugh at a quirk in the code and then fall into a silence that isn't awkward — just comfortable and full."
        "Talk to Sima about trainings":
            "You sit on a low piling and hear Sima's plans out loud: a certificate she wants to earn, a schedule that will keep her son in school. You make a note to push for childcare stipends in the next funding memorandum. She leaves with a roster to sign and a wider smile."

    # --- merge ---

    "The playbook is modest but exact: maintenance schedules, community-monitoring templates, legal language for co-management, and a glossary that translates engineering jargon into practical neighborhood tasks. You wrote notes in the margins — memories and small instructions" "When the tide is low, check the southern culvert,' 'Beware the spring storm—revisit anchors."
    "Lucia turns up at one of the afternoon community workshops to demonstrate non-invasive piling techniques. She stands before a clustered group of neighbors and tradespeople, sleeves rolled, speaking with a clarity that scrubs away suspicion."
    hide rani_cho
    show lucia_montrose at left:
        zoom 0.7

    lucia_montrose "This is not a trade-off between commerce and nature. This is staging: protect critical lines without severing the wetland's life. The pilot proves we can limit risk without erasing ecosystems."
    "There is applause that is not factional — it is practical and tired and ready to be done with argument. Lucia answers hard questions directly. When someone asks about long-term liability, she outlines a phased oversight"
    "plan, hands steady. Her presence in this space does more than soften opposition; it lends credibility across the aisle."
    "You notice Elias watching Lucia sometimes — not with suspicion now, but with a scientist's appreciation. He asks a pointed technical question; Lucia replies with a diagram; Elias leans in, and you read the exchange as a form of new respect forming."
    # [Scene: Rooftop Market & Greenhouse | Golden Hour, Months Later]
    hide mara_solenne
    hide elias_harrow
    hide lucia_montrose

    scene bg ch13_f99e88_4 at full_bg
    # play music "music_placeholder"  # [Music: Warm acoustic guitar with a gentle chorus]
    # play sound "sfx_placeholder"  # [Sound: Market chatter, the clink of cups, a distant thunderhead promising more rain]

    "A long table is set up under a canvas awning. On it are copies of the playbook, laminated quick guides, and a poster that shows metrics: acres of marsh stabilized, number of local hires trained, percent reduction in shoreline erosion in the pilot zone. The poster reads" "Pilot Zone Results — Year 1: 34 Percentage reduction in acute erosion events; 62 local hires; 6 community monitors."
    "Councilor Mateo is there, sleeves rolled, handing out small commemorative seed packets. Lucia is at the makeshift podium, her earlier formalness replaced by a warmth that suits the market. She is honest about compromise — about what was saved and what had to be staged."
    show lucia_montrose at left:
        zoom 0.7

    lucia_montrose "We didn't save every square meter. We saved the people who live here and the essence of what kept them strong."
    "She gestures to you and Elias. 'This didn't happen from the top-down. It happened because neighbors and engineers sat at the same bench and refused to reduce either the city or its citizens to a single solution.'"
    "Elias calls you over. He leans close, his voice low over the hum of the crowd."
    show elias_harrow at right:
        zoom 0.7

    elias_harrow "We put the first iteration of the sensor network online this morning. The data stream is public. I wrote an open API so any neighborhood can plug into it."
    "You rest your hand on his forearm, feeling the calluses and the warmth."
    show mara_solenne at center:
        zoom 0.7

    mara_solenne "You know, you could have chosen a different metric to make the case faster. You chose the ones that mattered to us."

    elias_harrow "You made me choose better metrics."
    "The market feels like a small republic — everyone in it a participant, not an audience. A child runs by with a salt-damp kite; an elder claps at the announcement of a training stipend. Rani passes"
    "you a plate of fried taro and grins as if the victories are hers as much as anyone's."
    hide lucia_montrose
    show rani_cho at left:
        zoom 0.7

    rani_cho "We built this like a raft — each plank mattered."
    "You laugh, and the sound feels open and clean."

    menu:
        "Read the metrics poster aloud to the crowd":
            "You stand up on a crate and read the poster: numbers, names, timelines. People cheer at the names they recognize. Your voice wobbles once and then steadies. You feel the city listening differently."
        "Hand a playbook to a visiting counselor from another ward":
            "You slide a playbook into a counselor's hand. She flips the pages, surprised by the legal clarity and the community tasks. She asks how much it cost; you say 'less than the last wall.' She nods slowly, eyes widening."

    # --- merge ---
    "At the edge of the market, Lucia finds you again. For a moment you stand with your backs to the crowd, listening to the rain begin to thread the sky."
    hide elias_harrow
    show lucia_montrose at right:
        zoom 0.7

    lucia_montrose "You organized people into a structural argument. That's rare."

    mara_solenne "You wrote structural arguments into the plan. That's also rare."
    "She inclines her head."

    lucia_montrose "I am not wrong to build for the city. But I underestimated what co-management could do."
    "There is a small apology tucked into the last sentence, and you accept it as you accept the rain: inevitable and good."
    # [Scene: Pilot Zone | Dusk, Six Months Later]
    hide mara_solenne
    hide rani_cho
    hide lucia_montrose

    scene bg ch13_f99e88_5 at full_bg
    # play music "music_placeholder"  # [Music: Gentle swell of strings and choir-like harmonics]
    # play sound "sfx_placeholder"  # [Sound: Quiet water, a single distant laugh, the soft beep of a data packet being sent]
    "You walk the tide-line with Elias, the playbook tucked into your jacket. The co-management board meets tonight; you are both on the agenda. People you know — not names on petitions, but neighbors who fixed pumps"
    "and taught classes — are on the roster. Their faces are lit by headlamps and resolve."
    show elias_harrow at left:
        zoom 0.7

    elias_harrow "We can expand the pilot next quarter if the data keeps trending."
    show mara_solenne at right:
        zoom 0.7

    mara_solenne "We will expand it when the next ward wants to try it. We won't force it; we'll share the map and the playbook and the trust."
    "He adjusts the compass on his cord, the family keepsake clicking softly under his palm."

    elias_harrow "I never thought my work would feel like a public love letter."
    "You laugh, and the laughter curls into something that feels like a promise."

    mara_solenne "Then write it well."
    "He squeezes your hand; the gesture is practical and intimate. It says, without fanfare, 'we are in this together.'"
    "Months have passed since the ordinance signed; the pilot zones stand as small, stubborn proofs. Neighborhood crews have been trained in maintenance; Beaconworks runs a mentorship program; Lucia chairs a quarterly forum where engineers and stewards"
    "share results and revise methods. The metrics are not miraculous: erosion slowed, biodiversity indices rose slightly, and residents report fewer emergency disruptions during storms. But numbers are not the only thing that changed. There is a"
    "cadence to the community now that did not exist before: regular paydays for marsh work, shared tool libraries, and a public data stream that keeps decisions honest."

    "You publish a final section in the playbook" "How to Teach."
    show eda_nal at center:
        zoom 0.7

    eda_nal "You kept the hands in the mud. Good."
    "The room breaks into a scattered applause, pragmatic and gentle."
    # [Scene: Rooftop | Night]
    hide elias_harrow
    hide mara_solenne
    hide eda_nal

    scene bg ch13_f99e88_6 at full_bg
    # play music "music_placeholder"  # [Music: A single violin line, warm and intimate]
    # play sound "sfx_placeholder"  # [Sound: Distant sleet beginning, a soft city breath]
    "You feel the solidity of the months behind you: plans passed, hands taught, the slow accretion of trust. This narrow ordinance did not remake the city all at once — it made a place where work"
    "could continue and where people's labor had value recognized by law. That, you realize, is the foundation of any larger movement."
    show elias_harrow at left:
        zoom 0.7

    elias_harrow "We co-wrote something that people can actually use. Not an ideal, but a tool."
    show mara_solenne at right:
        zoom 0.7

    mara_solenne "Tools build things. And things build lives."
    "He turns to you, amber eyes luminous in the rooftop light."

    elias_harrow "Are you tired?"

    mara_solenne "Yes. And it's a good tired. It means we did the work."
    "He reaches out, fingertips brushing the copper wire threaded in your hair — a small, private map of you he knows by touch."

    elias_harrow "We will refine the playbook. We'll help other wards. We'll keep the workshops rolling."
    "You let the future sit between you, a careful plan that includes both. You think of the possible endings the city could have had and feel gratitude for this one — a practical, hopeful compromise that"
    "preserves work and marsh and something larger: the dignity of ordinary life in the face of rising seas."
    "Lucia's last public contribution had been exactly that: a technical lecture followed by a town-hall apology for the way systems treated margins. It didn't make up for history, but it shifted her into an ally with"
    "a power that could be used differently. She sent you an email later that week:"
    show lucia_montrose at center:
        zoom 0.7

    lucia_montrose "Keep the pressure where it matters; I will keep the policy where it works."
    "Her ellipsis at the end felt almost tender."
    "Rani appears at your side, breathless from some late fix. She plops down and offers you a handful of toasted seeds."
    hide elias_harrow
    show rani_cho at left:
        zoom 0.7

    rani_cho "We'll need a new batch of nets next week. Trade you some knot lessons for a recipe for that soup you make."
    "You smile; the deal is instantly sealed."
    "You think, finally, of love — not merely as private exchange, but as a public craft. Yours with Elias is practical: data and deadlines, long meeting nights and quiet mornings in the mud. It is a"
    "partnership that trusts the other's skills and honors the other's fears. It is an architecture."
    "Elias leans his head against yours, and for a long moment the city is nothing but rain-scented air and the small steady beat of community."
    "You have a sense of completion that is not an endpoint but a sturdy landing. The ordinance is narrow, but it is anchored and replicable. The pilot zones are proof that small, protected spaces can ripple"
    "outward. The romance has deepened into a craft of shared labor and mutual respect, and you are both tired in a way that is full."

    "You open the playbook one last time and find, on the inside back cover, a note handwritten by people who have made the pilot their own" "If you can keep the mud from being evacuated from our hands, you keep us. Keep the mud. Keep us."
    "You close it and tuck it into your jacket, where the hydroponic locket rests against your heart. Outside, the city breathes rain. Inside, there are jobs, legal teeth that protect places, a tested set of practices, and people who know how to do the work."
    "You stand, feeling a small and steady glow that is equal parts relief and resolve. The work will continue; the fight did not end with this ordinance. But for the first time in a long while, you can feel the tide shifting under something you and your neighbors helped build."
    hide mara_solenne
    hide lucia_montrose
    hide rani_cho

    scene bg ch13_f99e88_7 at full_bg
    # play music "music_placeholder"  # [Music: Strings resolve into a warm, hopeful cadence]
    # play sound "sfx_placeholder"  # [Sound: Rain softens into a steady hush]

    scene bg ch13_f99e88_8 at full_bg
    "THE END"
    # [GAME END]
    return
