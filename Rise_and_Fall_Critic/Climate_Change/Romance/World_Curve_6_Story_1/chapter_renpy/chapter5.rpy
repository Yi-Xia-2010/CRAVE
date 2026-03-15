label chapter5:

    # [Scene: Old Shipyard | Morning]

    scene bg ch5_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls; the soft clack of measured footsteps on worn planks; a radio hum under conversation.]
    # play music "music_placeholder"  # [Music: Light, hopeful strings with a steady, rising motif]
    "You arrive with your notebook tucked under your arm, the Polaroid pressed between pages beside the seed packet—two small promises you can feel against the cardboard. The compass pendant rests warm at your throat; the metal"
    "is familiar enough to steady your breath. Morning fog unthreads itself from the harbor and hands you a quiet, salt-bright air. It smells like wet rope and coffee steam and the particular sweet of damp soil"
    "that holds new roots."
    "People are already working. Bento stands near the arch of the old warehouse, sleeves rolled, guiding an older team as if his hands remember every joint of the coastline. He moves slowly, but everyone leans in"
    "like he sets the rhythm. Kai darts between groups, shouting snippets of instruction over laughter—seed packets are being distributed like small contraband, bright against the mud."
    "Jonah Reyes is there, hands darkened with peat, hauling a coir log into place with two other volunteers. When he sees you he gives a quick, crooked grin that changes the way the morning sits on your shoulders: less like obligation, more like purpose."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "You look like someone who forgot their coffee but remembered everything important. You coming to wrestle stakes or to boss people around?"
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Both, probably. Someone needs to keep the map straight while everyone's losing their minds with burlap and optimism."

    jonah_reyes "Optimism's contagious. So is stubbornness—you're a carrier."
    "Your hands find the grain of the stake; the roughness blunts the small tremor in your fingers. Shoulder-to-shoulder—literally, as you and Jonah Reyes brace one another lifting the coir logs into the mud—you fall into the"
    "easy choreography of people who have built things before. The physical rhythm steadies thought. Your laptop hums in your pack, a thin, patient beat syncing with the town's small machinery of hope: community-sourced elevation points, crowdsourced"
    "observations, a mesh of real lives mapped into teal and ochre dots."
    "Dr. Lian Zhou arrives with a thin transect pole and a tablet that glares like a small moon. She moves with the economy of someone who's measured tides more often than small talk."
    show dr_lian_zhou at center:
        zoom 0.7

    dr_lian_zhou "Mira. We've got a half-meter variation across this quadrant—if we plant this mat at the lower elevation, average inundation will be higher the first season. Jonah, you want willow, but we should spike elevation here by twenty centimeters and increase sediment retention with additional coir."

    "You" "What's the work trade-off? If we raise elevation with more coir do we risk disrupting the planting pattern Jonah's been planning?"
    "Dr. Lian Zhou: (tapping her tablet) 'It changes the planting density, but it increases survival probability significantly. If volunteers are comfortable with an extra few hours per mat, the establishment rate climbs. We get better early-season data that advocates can use.'"

    jonah_reyes "Extra hours are fine. But what Lian's saying—if we over-engineer it we could lose the feel of it. This is supposed to be Tidehaven's work, not a science project dropped on us."
    "The exchange is familiar—science and craft circling each other like complementary tides. You listen, sorting obligations and impulses. The pendulum of your responsibility swings between the pragmatist who brought data and the daughter who promised her town she would return for its small, stubborn life."
    "Bento Morais calls, his voice a calm anchor."
    hide jonah_reyes
    show bento_old_bento_morais at left:
        zoom 0.7

    bento_old_bento_morais "Focus on the shoreline like you would a boat, yes? Lay the lines true, then stitch. Don't hurry the stitch."
    "His metaphor is the lightest pressure. People nod. Hands find ropes and shovels and each other."

    menu:
        "Grab a shovel and join Jonah at the low-tide trench":
            "You shoulder down into the mud beside Jonah, the cold seizing at your knees, and the work's rhythm quiets the louder parts of your mind—each scoop feels like an argument made with the ground."
        "Stay near the tablet and coordinate placements with Lian":
            "You crouch by Lian, fingers tracing contour lines on her tablet; your voice becomes an instrument of orders and reassurance, and you feel the town's confidence pulsing through your throat."

    # --- merge ---
    "..."
    # [Scene: Old Shipyard | Midday]
    hide mira_kestrel
    hide dr_lian_zhou
    hide bento_old_bento_morais

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Laughter, the scrape of shovels, a low drone of a delivery truck]
    # play music "music_placeholder"  # [Music: A warm acoustic progression; tambourine brushes add a communal beat]
    "By noon, the shipyard hums with a kind of clean chaos. Seedlings are lined like a small army on tarpaulins. The coir logs look like robust, earthy barricades waiting for their tide-test. Sweat beads on brows"
    "and wood smoke threads through the air from a volunteer's small stove. You taste salt and smoke and the faint metal of your compass against your skin."
    "A small, tidy van pulls up—white with a regional NGO logo. A woman steps out with a laminated packet and a practiced smile. She moves with a different cadence: soft but efficient, the kind of presence that promises resources and binds hands in bureaucratic knots."

    "NGO Representative" "Good morning—this is beautiful work. We were tracking your campaign. Our funders are excited about scaling this model regionally. We can offer a substantial grant, materials, and publicity."
    "Something in the way 'publicity' hangs in the air makes Jonah Reyes's jaw tighten. He steps forward protective like a man with generations of fish-marked hands."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "Scale is good. Funding's good. But Tidehaven's not a display. We make things with the town, not for it."
    "NGO Representative: (cheerful, smoothing) 'Absolutely. We like community-rooted narratives. Of course, grants come with branding and timelines—we'd want to coordinate a press window and a logo on materials. It helps with accountability to our donors.'"
    "Dr. Lian Zhou watches the exchange, not judging but cataloguing implications."
    show dr_lian_zhou at right:
        zoom 0.7

    dr_lian_zhou "Timelines are problematic if they force shortcuts in the pilot. The data integrity—"

    "NGO Representative" "We can incorporate monitoring milestones. We love citizen science. But yes—donor expectations will push for visible results in the first year."
    "You feel the familiar knot tighten at the base of your neck. The offer is a rope with glitter: real resources that could make the pilot resilient and expand its scope beyond the shipyard. But the"
    "language—branding, timelines—suggests an aesthetic and governance shift that could change who owns the narrative of Tidehaven's shoreline."
    "Asha Verma arrives then—her coat buttoned, brass-framed glasses slightly slipped. She watches the coir logs like an engineer admiring a blueprint. When the rep finishes she steps forward with the efficiency of someone who decides and moves."
    show asha_verma at center:
        zoom 0.7

    asha_verma "Funding's useful—but not at the expense of structural integrity. If you choose these plantings as a demonstration you must be prepared to show how they'll integrate with robust protections. A grant that accelerates a visible rollout without structural assessment is dangerous."
    hide jonah_reyes
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "We're pairing this with monitoring—Lian's team is collecting elevation and survival datasets. We want to show a living alternative."
    "Asha Verma: (narrowing her gaze) 'Living adaptations are valuable. But in the event of a major surge, an under-engineered visible project can give the community false assurance. Whoever funds this is buying more than seedlings—they're buying confidence. You need contractual language that controls scope.'"
    "Her words land like cool stones—practical, sharp. Jonah Reyes looks between you and Asha Verma, the long history of his reluctance to trust outside authorities played out in the measured set of his shoulders."
    hide dr_lian_zhou
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "So—what now? We either say no and stay small, or we say yes and try to keep the final say."
    "Your throat tastes of iron for a second; there are threads of every possible future braided into this exchange. You want to preserve the town's way: the aesthetics of burlap, the ownership in the hands callused"
    "from fishnets. You also want to protect people and outcomes with evidence. It's a moral knot, and your fingers are on the knot."
    "Bento Morais, overhearing, crosses his arms and says softly:"
    hide asha_verma
    show bento_old_bento_morais at center:
        zoom 0.7

    bento_old_bento_morais "Money's a tool. So's pride. We pick which one to sharpen. But remember—tools don't fix the wrong hand."
    "Kai Tan, bursting with a half-formed plan, grins."
    hide mira_kestrel
    show kai_tan at left:
        zoom 0.7

    kai_tan "If we take the funds we can insist on a governance clause that creates a community board. We could brand the grant as Tidehaven-led. They'd probably bite—donors like 'community stories.'"
    "The volunteer chatter ebbs into a hum. The NGO rep looks between faces, recalculating their pitch."

    menu:
        "Ask the rep for a draft of the grant language now—call their bluff":
            "You step toward their table, voice steady. The rep fetches a packet; the language reads like polite colonization—'partnership,' 'visibility,' 'deliverables.' You underline 'deliverables' with a hand that trembles, and Jonah nods as if you've landed a tiny blow."
        "Call a quick community huddle to let Tidehaven set the frame":
            "You blow a whistle and gather people into a ragged circle. Voices rise—Bento's quiet, Lian's technical, Kai's fierce. It's messy and human and exactly the kind of messy you trust."

    # --- merge ---
    "..."
    # [Scene: Old Shipyard | Night / After Dusk]
    hide jonah_reyes
    hide bento_old_bento_morais
    hide kai_tan

    scene bg ch5_4001e7_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft susurration of planting, low laughter, the distant slap of waves against pilings]
    # play music "music_placeholder"  # [Music: Sparse piano over soft pads; the motif lifts into a hopeful cadence]
    "Night molds the build into something intimate. The harbor, now a dark glass, reflects the work site as if it were its own small shore. Kai organizes a youth group to do night planting—his logic: seedlings"
    "face less midday stress and cooler water helps establish roots. The kids move with a seriousness that surprises you; they treat each seedling like a fragile future."
    "You find Jonah Reyes near a line of newly placed stakes. He wipes mud from his palms and presses his fingers to the base of a willow, adjusting its angle as if coaxing it to listen to the same wind you both grew up with."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "You did good today. Lian's numbers will help. Bento's hands anchored the older crew. Kai's kids planted like saints."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "We moved a lot of ground. But the rep's packet sits like a shadow in my bag. It promises reach and resources—and strings. I can't decide if it's an opportunity or a leash."
    "Jonah Reyes: (looking at you, voice softer) 'What do you want, Mira? Not what do we need—what do you want when you look at these willows in five years?'"
    "The question strips away protocol. You feel every choice as something that will shape your mornings for years: will you wake to banners and logos, or to the smell of burlap and your neighbors' oven smoke?"
    "The town is not an abstract to you—it's a ledger of breakfasts, a thousand quiet ways people show up for one another."
    "You touch your compass; it is cool now, a metronome at the base of your throat. The pendant's smallness is absurd and grounding."
    "Dr. Lian Zhou, kneeling beside a mat, speaks without taking her eyes off the seedlings."
    show dr_lian_zhou at center:
        zoom 0.7

    dr_lian_zhou "If we prioritize rigorous monitoring, we protect the integrity of the science and give Tidehaven arguments that matter in regional conversation. But it requires patience. Funders usually want quick metrics."
    "Asha Verma's silhouette appears in the glow; she scans the line of plugs and stakes, then meets your eyes."
    hide jonah_reyes
    show asha_verma at left:
        zoom 0.7

    asha_verma "A phased plan with strict monitoring provides defensibility. But don't mistake defensibility for delay. There are trade-offs. If you're prioritizing community control, that's a political decision. If you're prioritizing measured risk mitigation, that's different. Both are necessary. It's about balance."
    "Your internal monologue spins the options like coins. The 'community-run, small' coin carries warmth and trust but limited reach. The 'accept the grant with local governance clauses' coin hums with compromise—resources but strings. The 'rigorous, smaller pilot with monitoring' coin weighs method and integrity alone."
    "You think about the people who will stand behind the lines when the first test tide comes; you think of Bento Morais's slow certainty; of Jonah Reyes's hands still cupped around a stake. Hope is not naive here—it is a deliberate architecture you are helping to build."
    "The night wears on with a quiet productivity that feels like prayer. You walk the length of the build, feeling the damp give underfoot, watching lantern light catch on mud-slick ropes. The town's voice is present in each movement, in every shared tool and joke about sore backs."
    "You stop at the edge of the site and exhale. For a breath you allow yourself the simple fact that they came—the volunteers, the kids, the elders. The pilot exists now, more than a plan: it is a thing your neighbors can point to and say, 'We did that.'"
    "But the grant packet is heavy in your coat, and Asha Verma's point about defensibility rings like a bell."

    menu:
        "Sit with Jonah for a while and imagine the five-year morning":
            "You and Jonah sit on a damp crate, shoulder to shoulder. You imagine mornings full of small trades: one neighbor's surplus seedlings becoming another's ritual. The image steadies you; the choice feels less like a single verdict and more like a commitment to a town's temperament."
        "Walk to Lian and sketch out the strictest monitoring plan you can—numbers, timelines, personnel":
            "You and Lian bend over the tablet, sketching rigid data points and check-ins. It feels cold and precise, but it gives you a scaffolding—an argument you can hold up to donors and say: this is how we prove it works."

    # --- merge ---
    "..."
    "You stand between these currents—between art and instrument, between the cadence of local life and the leverage of outside resources. Rise swells in your chest; the build around you is a living promise that change can be shaped by hands that remember how to care."
    "The night makes the choices feel intimate and urgent at once. You tighten the clasp of your compass and look up at the long, dark sweep of the harbor. Dawn will demand an answer—or at least a direction."
    # [Scene: Greenhouse Collective | Later that Night]
    hide mira_kestrel
    hide dr_lian_zhou
    hide asha_verma

    scene bg ch5_4001e7_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft rustle of paper, a kettle boiling, the muffled harbor beyond glass]
    # play music "music_placeholder"  # [Music: A gentle uplift; a single cello line rises]
    "Inside the greenhouse you lay the NGO packet, Lian's annotated plan, and a scrap of handwriting from Bento—three different logics, one shared aim. Hands hover over the documents like people over an old map. The group's conversation is low and deliberate, not yet a decision but a negotiation toward one."
    show bento_old_bento_morais at left:
        zoom 0.7

    bento_old_bento_morais "We have enough town to make small things matter. But if we want a louder voice at the council table, we need evidence—and maybe the funds to do it."
    show kai_tan at right:
        zoom 0.7

    kai_tan "And youth will follow the story they can be proud of. If we brand it right—Tidehaven first—it could give us reach without losing us."
    "Jonah Reyes: (quietly) 'Sometimes reach means we lose the small, everyday edges that make Tidehaven belong to us.'"
    show dr_lian_zhou at center:
        zoom 0.7

    dr_lian_zhou "A hybrid is possible—secure funds with clear governance clauses, insist on monitoring, and stage public communications that center the town. But it takes someone to hold the terms in place."
    "When their eyes drift to you, the mantle of 'someone' weighs both light and heavy. You have done hard things before, but this is different: it will shape the town's story and your role in it."
    "Hope is the air you breathe—rising, insistently green—but responsibility is the ground beneath your feet."
    "You lay a hand on the Polaroid in your notebook for a breath, feeling the small bump of paper. Images can be arguments; objects can be anchors. The choices before you are a kind of architecture of trust."
    # play music "music_placeholder"  # [Music: The strings resolve into a warm, expectant chord]
    "You speak."
    hide bento_old_bento_morais
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "We can refuse the branding and keep it community-run and small. We keep ownership wholly local—we move slower, but it's our shoreline. Or we can accept the NGO grant but require local governance clauses—use their resources while insisting Tidehaven leads the narrative. Or we can push for a rigorous, smaller pilot with Lian's monitoring—even if funding is tight, we build defensible data and take the long view."
    "The sentence hangs like a buoy. Everyone listens. The air tastes faintly of peat and possibility."
    "You let the horizon of your options form in the heads of the people you love—Bento Morais's ancient calm, Jonah Reyes's protective steadiness, Dr. Lian Zhou's methodical ardor, Kai Tan's fierce hope, and even Asha Verma's uncompromising clarity. Each path speaks to a different way of loving this town."
    # play music "music_placeholder"  # [Music: A single, hopeful swell—then a quiet hold]

    menu:
        "Refuse external branding; keep it community-run and small.":
            jump chapter6
        "Accept the NGO grant but require local governance clauses.":
            jump chapter6
        "Push for a rigorous, smaller pilot with Dr. Lian’s monitoring—even if funding is tight.":
            jump chapter13
    return
