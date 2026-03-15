label chapter14:

    # [Scene: Municipal Meeting Room | Morning]

    scene bg ch14_bd95da_1 at full_bg
    # play music "music_placeholder"  # [Music: Gentle, rising piano with soft string underswell]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls and the muffled slap of tide against the harbor pilings]
    "You press your thumb against the dented key in your pocket without thinking, feeling its familiar roughness beneath the pad of your skin. The MOU you signed last night sits folded in your satchel like a"
    "promise that needs muscles to keep it alive. Across the table, faces you trust and faces you still have to win lean in. The air smells faintly of coffee and algae — Atera in a cup."
    "Amina clears her throat and lets the room settle. Her braid brushes the back of her collar like a cord keeping everything taut."
    show mayor_amina_bakar at left:
        zoom 0.7

    mayor_amina_bakar "We have a window, and we have funding for a pilot. The question is—what do we make it prove? Physical resilience, livelihoods, or governance? We only get to pilot one model first."
    "You already know the three vectors — they're mapped across the table in margins and sticky notes: engineered safe zones with living-shoreline credits; kelp cooperatives; alternating parcels with co-managed revenue. Each has pull. Each has a"
    "risk. The rising chord in the piano makes your chest feel like it will expand."
    "Jun drums his fingers on a stack of site surveys."
    show jun_park at right:
        zoom 0.7

    jun_park "If we pick something that doesn't produce jobs, people won't stick. Tools and paychecks matter more than theory. We can build breakwaters, sure, but if my cousin can't pay rent 'til harvest, I'm telling him a story, not a plan."
    "Riv leans forward, eyes bright and impatient, a bandana slipping as he gestures."
    show ravi_riv_delgado at center:
        zoom 0.7

    ravi_riv_delgado "And if we pick something that hands the money to developers without teeth, watch 'em sell the credits to the highest bidder and call it climate justice. We need accountability baked into the pilot."
    "Elias Maren folds his hands in front of him, an old tide map folded into the cuff of his notebook. He looks at you and then at the renderings, tracing an imaginary kelp line with his gaze."
    hide mayor_amina_bakar
    show elias_maren at left:
        zoom 0.7

    elias_maren "Whatever we choose, it has to be demonstrable. People need to see a living shoreline actually dampen a swell or a kelp coop actually bring income. The science can carry the story, if we let it."
    "Soren Voss stands by the window, hands folded, the sunlight making a thin halo on the reflective weave of his coat. He watches the harbor with that planner's distance that has soothed and irritated you in"
    "equal measure. Today there is a different line to his jaw — concentration rather than performance."
    hide jun_park
    show soren_voss at right:
        zoom 0.7

    soren_voss "Scale matters. We can pilot a modular approach that people can buy into. Credits — if structured right — can prime investment and give us measurable offsets to finance more protection.' (He taps a tablet; a projection of phased parcels blooms on the screen.) 'This is about teachable, sellable models. If we show a funder a replicable ledger, we unlock more towns."
    "You listen to the clashing logics and feel, beneath them, something starting to knit: not agreement, not yet, but a common aim. The room smells like hot paper and resolve."

    menu:
        "Trace the proposed breakwater line with your finger":
            "You reach for the rendering, your finger steady. Soren leans in, and the two of you fall into a rhythm of measurement and margin—work that feels like speech. Jun watches you with a nod of approval."
        "Tap the kelp map and point to the harvest plots":
            "Your finger pauses on the kelp plots. Elias smiles so softly that you almost don't notice; he begins explaining growth cycles and local market links, and your breath eases into the cadence of possibility. Riv scribbles a note, already thinking about outreach."

    # --- merge ---
    "The discussion continues with the group's responses integrating from either action."
    "Amina folds her hands and offers a neutral smile that is anything but neutral."
    hide ravi_riv_delgado
    show mayor_amina_bakar at center:
        zoom 0.7

    mayor_amina_bakar "You won't be surprised if I ask Mika to lead the steering committee drafting the pilot criteria. You carried the charter last night. You have the workshop and community trust. Will you take it?"
    "All eyes turn to you. Your chest tightens in that way that used to mean obligation alone; now it also tastes like opportunity. You straighten a sleeve, the fabric catching on the patch of your elbow like an old seam."
    hide elias_maren
    show mika_hoshino at left:
        zoom 0.7

    mika_hoshino "I'll do it. But I want binding metrics—auditable commitments on ecological outcomes and local hiring, and a rotating oversight seat for community reps. No backroom changes."
    "Soren's gaze finds yours. For a second, the planner's wall flattens into something softer; there's an acknowledgment there — not a promise, but the opening of one. He steps closer to the table, close enough that the corner of the projected map spills onto his cuff."

    soren_voss "Binding is fair. I want the model to survive scrutiny. If the governance has teeth and the metrics are clear, I'll fight for this in the funding circles."
    "Elias Maren watches him, expression careful."
    hide soren_voss
    show elias_maren at right:
        zoom 0.7

    elias_maren "You'll be in public briefs and hearings, Soren. If you promise teeth, you'll have to sign the audits. Transparency isn't optional."
    "Soren pauses, and for a moment his eyes are unreadable — a calculator and a conscience both balancing. When he speaks again, his voice has the soft call of someone who has learned to temper salesmanship with stake."
    hide mayor_amina_bakar
    show soren_voss at center:
        zoom 0.7

    soren_voss "Then we write the audits in. We fund independent verification. We train local monitors. We build in clawbacks if ecological targets fail."
    "Riv snorts softly, then grins."
    hide mika_hoshino
    show ravi_riv_delgado at left:
        zoom 0.7

    ravi_riv_delgado "Now that's language I can go protest to—with a clipboard. But also: public forums. Regular check-ins. If we do this, people should be able to yell at us every month."
    "Jun chuckles, the sound like a plank settling."
    hide elias_maren
    show jun_park at right:
        zoom 0.7

    jun_park "And boots on the ground. If you want the town to buy in, show them the traineeships and the tools."
    "The discussion unfurls into logistics: who trains, who audits, which parcels are pilot-ready, how to phase installations with harvest seasons, water windows for kelp planting, permitting timelines, and the ledger model for credits. Your mind nimbly"
    "toggles between details — buoy spacing, apprentice rosters, audit frequency — the muscle memory of repair applied to policy."
    # [Scene: Pilot Site Walk | Midday]
    hide soren_voss
    hide ravi_riv_delgado
    hide jun_park

    scene bg ch14_bd95da_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind in the reedbeds; the distant creak of a research platform; the gulls' cries softer now]
    # play music "music_placeholder"  # [Music: Light acoustic guitar with hopeful strings]
    "You stand at the edge of a proposed parcel where the boardwalk cuts through the reedbeds. Salt beads on the rail under your hand, cold and bright. The pilot sites look less like renderings and more"
    "like lies you can mend: a narrow strip with a ruined boathouse, a low chunk of marsh, an empty lot stamped by tire tracks and weeds."
    "Elias Maren kneels to the mud, pointing out a seam in the sediment where kelp lines could anchor."
    show elias_maren at left:
        zoom 0.7

    elias_maren "This current eddy here creates a calm pocket—ideal for a kelp anchor and for juvenile fish. If we place breakpoints along the scar line we reduce fetch, and the kelp can increase sedimentation over time."
    "You can hear the excitement in his voice, the soft pulse of someone who teaches by showing. His hand brushes yours as he reaches for a corroded bolt; it's an incidental contact, but it lands with a small, steady warmth."
    "Soren Voss stands a few paces back, speaking into a recorder with crisp notes on access routes and construction materials. When he looks at you, the planner and the person are both present — a rare overlap that steadies you."
    show soren_voss at right:
        zoom 0.7

    soren_voss "If we modularize the engineering features — small, repeatable segments — we can combine them with kelp beds in adjacent parcels. That alternation could be the political compromise we've been chasing."

    "Riv, ever the provocateur, posts a flier on a nearby corkboard" "TELL US WHAT YOU WANT. PUBLIC FORUM NEXT WEEK."
    show ravi_riv_delgado at center:
        zoom 0.7

    ravi_riv_delgado "You think they'll come?"
    hide elias_maren
    show mika_hoshino at left:
        zoom 0.7

    mika_hoshino "They come when they see something is changing for the better. They come when the changes put dinner on table and keep kids in school. They come when they trust the hands steering it."
    "Jun taps at his phone, checking logistics."
    hide soren_voss
    show jun_park at right:
        zoom 0.7

    jun_park "Training rigs can be set up at your workshop, Mika. We can have the first cohort in two months if the funding clears. People learn faster when their hands are busy."
    "The day moves through tasks and promises. You climb in and out of trenches of conversation — legal language with Amina, technical schematics with Elias, funding rhythm with Soren, blunt practicality with Jun. Every exchange pulls you closer to the center of things."

    menu:
        "Offer to host the first trainee group at your workshop":
            "You say yes before your brain finishes weighing the work. Soren smiles — brief, approving — and Elias beams with relief. Jun slaps your shoulder like a craftsman promising easier mornings."
        "Suggest a neutral, public space for trainees, to emphasize community ownership":
            "You propose the boardwalk pavilion. Riv's face lights up; he can already picture public classes and an open tool sign-out. Amina nods — governance momentum aligns with community visibility. Soren notes implications for logistics, his planner's mind spinning with scheduling."

    # --- merge ---
    "The group's planning adapts to either location choice and moves forward with training logistics."
    # [Scene: Development Parcel Overlook | Late Afternoon]
    hide ravi_riv_delgado
    hide mika_hoshino
    hide jun_park

    scene bg ch14_bd95da_3 at full_bg
    # play music "music_placeholder"  # [Music: Strings swell warmly; a low horn of the harbor cues a communal, resilient mood]
    # play sound "sfx_placeholder"  # [Sound: The harbor bell, far-off voices preparing for evening]
    "You stand on the bluff as the light leans golden. The parcels look like a chessboard — pieces that could be arranged to protect or profit. The conversation turns, inevitably, to revenue: how credits might finance"
    "conservation, how development can fund training and buyouts for the most vulnerable, how to avoid turning resilience into extraction."
    "Amina folds her hands, the mayoral weight in her voice a soft anchor."
    show mayor_amina_bakar at left:
        zoom 0.7

    mayor_amina_bakar "We need a governance model that isn't just about who gets a seat at the table. It needs real pathways for review and redress. What we build today must be reversible if it fails its tests."
    show elias_maren at right:
        zoom 0.7

    elias_maren "Independent verification, public dashboards—let people see the data. Transparency reduces rumor, and it gives community members the tools to hold us accountable."
    show soren_voss at center:
        zoom 0.7

    soren_voss "Agreed. Dashboards, audits, local monitors, and a staggered scaling plan. We make the ledger public and the bids auditable."
    "Riv whistles softly."
    hide mayor_amina_bakar
    show ravi_riv_delgado at left:
        zoom 0.7

    ravi_riv_delgado "And we build community education into the budget. If people's livelihoods hinge on kelp or on shoreline maintenance, they need training and shares."
    "The plan blooms into something tangible: a first phase with demonstrable ecological targets, local hiring quotas, a community oversight seat with rotating terms, a public dashboard, and clear clawback provisions. You write notes in the margins"
    "of your own mental ledger — dates, names, scopes — the scaffolding of a real pilot."
    "As the sun folds down, the warmth of possibility settles in your chest like a new kind of courage. You have been carrying guilt and the reflex to do it alone for so long; now there are hands. Not perfect hands. Not unblemished. Just hands that answer when you call."
    "Soren steps beside you on the bluff, a pace that is neither too close nor distant."

    soren_voss "You did good today. The language you pushed for—those oversight clauses—will make funders squirm, but they'll make the model stronger."
    "You look at him. His face is half lit by the harbor's low light; there is something honest there, a weariness white as a bone. His expression is complex — the thing the Schrödinger rule kept you from assuming, but which, in this moment, you can read as sincere."
    hide elias_maren
    show mika_hoshino at right:
        zoom 0.7

    mika_hoshino "We don't have all the answers. But we have people who are willing to keep working when the storms come. That's new."

    soren_voss "It is. And it's worth protecting."
    "His hand hovers, almost, near the small string bracelet on your wrist — an unspoken offering of contact. You don't step away. You don't step forward. The moment pivots on choices you won't make now: trust, intimacy, politics. For now, you let the quiet of shared exhaustion settle between you."
    "Elias Maren watches from a few steps back, his profile flattened against the harbor. He meets your gaze and gives a small, encouraging nod — practical, warm, as if to say: science and heart make a good team."
    hide soren_voss
    show elias_maren at center:
        zoom 0.7

    elias_maren "Mika? When you finalize the steering criteria, we should include a pilot metric for kelp biomass and recruitment. If we can show ecological improvement in two seasons, the model gains legitimacy fast."

    ravi_riv_delgado "And I'll get the forum scheduled. We'll make sure the town knows how to read the dashboard and when to yell at us."
    hide ravi_riv_delgado
    show jun_park at left:
        zoom 0.7

    jun_park "I'll line up tools and build rigs. If the trainees are ready before the winter swell, they'll have skills that last."
    "Amina folds the first draft of the steering terms and slides it across the table to you."
    hide mika_hoshino
    show mayor_amina_bakar at right:
        zoom 0.7

    mayor_amina_bakar "So — one last decision today. What is the pilot's emphasis? The governance scaffolding is set to accept any of the three, but whichever we choose first will shape public perception and the tenor of future funding."
    "You inhale, tasting salt and coffee and the sharp joy of a plan beginning to move as if it had its own breath. The rising music in your chest matches the pull of the town below, the steady insistence of progress."
    "You think of your mother's workshop — hammers, nets, the way hands can fix things when they are given a chance. You think of Elias bending over kelp charts at dawn, of Riv with his imperfect"
    "flyers, of Soren's quiet adjustment to being held to account. The choice isn't purely technical. It's a declaration about what you believe Atera is worth."
    "You lay a hand on the draft criteria Amina pushed to you, the paper warm from her lamp. The decision waits like low tide: inevitable, revealing, full of spots that will either teem with life or need careful tending."
    # play music "music_placeholder"  # [Music: Piano and strings swell into a hopeful motif]
    hide elias_maren
    hide jun_park
    hide mayor_amina_bakar

    scene bg ch14_bd95da_4 at full_bg
    "You are the one who will steer the pilot's first emphasis. The room leans with you."

    jump chapter15
    return
