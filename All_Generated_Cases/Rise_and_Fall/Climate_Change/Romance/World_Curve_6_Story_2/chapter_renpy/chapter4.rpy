label chapter4:

    # [Scene: Highwater Cove Harbor | Morning]

    scene bg ch4_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The scrape of metal on wood; distant gulls; a drill's rhythmic whine]
    # play music "music_placeholder"  # [Music: Warm, buoyant strings; a steady undercurrent of hope]
    "You step into the harbor and the town answers you back in the language it's always used: hands, tools, the smell of salt and diesel braided together. You didn't take Evelyn Hart's check. You didn't sign"
    "the glossy promise that came with a polite smile and a slide deck. Today the harbor is doing what it's always done when pressed—rearranging itself to survive."
    "You feel the compass in your pocket like an old promise. Its brass is cool, a small counterweight to the heat of your cheeks. Nan's quilts hang from a makeshift line, drying and turning the market"
    "into a patchwork of color. Someone's kid is hammering percussively on a broken cleat, and the sound threads into the bigger rhythm of work."
    "Rafi ducks out from under a sensor array, oil-smudged and triumphant. He waves a roll of duct tape like a banner."
    show rafi_chen at left:
        zoom 0.7

    rafi_chen "We MacGyvered the humidity sensor back to life. The casing's cracked, but the guts still sing. If we can't buy lab-grade parts, we make lab-grade improvisation."
    "(He grins; you can see the paint under his nails.)"
    show maya_armitage at right:
        zoom 0.7

    maya_armitage "Show me."
    "Rafi gestures, then launches into a rapid, excited explanation—how a salvaged pressure transducer maps the micro-tides, how a patched antenna can still pick up sentinel buoys if you angle it right. He talks fast; you counter with the questions that turn his tinkering into a data plan."

    rafi_chen "We'll need power. Solar's flaky in storms. Maybe a communal battery bank—old EV packs? If we coordinate schedules, we can keep the arrays live through gusts."

    maya_armitage "Okay. Get me a prototype tonight. I'll talk to Lena about permission to wire one to the community shed."
    "(You can feel the list in your head—permits, volunteers, routes—but you say the part that builds bridges.)"
    "Jonah Reyes appears at your elbow, a length of braided netting looped over his shoulder. Salt has left a white map on his collar; his knit cap is askew, curls escaping."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "You look like you need this more than the kids."
    "(He holds out the netting. It's rough and warm from being carried; his fingers brush yours when you take it.)"

    maya_armitage "You bring nets and jokes. Dangerous combination."
    "(You can't keep the smile from bleeding through—it's a small, honest theft of a breath.)"

    jonah_reyes "And you bring that deadly planner face. It'll keep us from accidentally building a floating shoebox."
    "(He nudges your shoulder with his hip as if to ground you.)"
    "There is heat in his steadiness that isn't words. It hums beneath the exchange—the remnant of storms and the heft of hands that have mended more than nets. You want to be precise with him: about"
    "your fears, about how refusing the check means more nights like this. Instead you pull the net taut between both of you and feel how cooperative problem-solving becomes a quiet kind of intimacy."
    hide rafi_chen
    hide maya_armitage
    hide jonah_reyes

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Someone laughs across the dock; the metal smell of salt and oil is sharp in the air]
    "Volunteers move in small choreography—sanding hulls, welding patches, stitching oyster shells into wire cages for reef planting. Nan organizes a corner with a deep calm; she pins up a laminated map and begins taking down names for shelter rotations and oral-history shifts."

    "Gracie 'Nan' Armitage" "We tell the children where the old boardwalk stood. We teach them what the tide line was called before the developers renamed it. Memory is ballast."
    "(Her voice is small but carries; people lean in.)"
    show maya_armitage at left:
        zoom 0.7

    maya_armitage "We'll catalog the stories and the stakes."
    "(Your throat tightens; it's work and it's prayer.) 'Rafi, make sure we put the oral histories on a portable drive. Copies to the institute and to the market booth.'"
    "Rafi: (nodding) 'I'll tape it inside the sensor crate. If the servers go down, the stories won't.'"

    menu:
        "Teach the youth how to splice nets now":
            "You crouch by the crate where the kids have gathered, letting Jonah take the heavier talk. Your hands move slow, patient; a boy mirrors each loop and tie. He looks up at you with wide, earnest eyes, and you feel the tension in your chest loosen for a breath."
        "Head to the Tidal Institute to file the application":
            "You fold the net and tuck it under your arm. You kiss Jonah's knuckle briefly—an anchor—and rush toward the institute. The paperwork won't file itself, and you can feel the grant clock like a second tide pulling at your sleeves."

    # --- merge ---
    "Rafi watches your choice with the amusement of someone who loves both your impulses."
    show rafi_chen at right:
        zoom 0.7

    rafi_chen "Either way, the work gets done. You always did like being where things happen."
    "(He reaches for his tool belt as if to affirm it.)"
    "You laugh, and the laugh is lubricated by exhaustion and relief. People are here. You have chosen to trust them instead of a single institutional hand. That trust is already translating into scaffolding—practical, hopeful scaffolding."
    # [Scene: The Tidal Institute | Afternoon]
    hide maya_armitage
    hide rafi_chen

    scene bg ch4_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft buzz of refrigeration; a murmured conversation about load-bearing calculations]
    # play music "music_placeholder"  # [Music: Light piano; optimistic, forward-moving]
    "The institute is a hive. Laptops are arranged like small islands; jars of kelp and tide core samples call for attention. You step in with the netting over your shoulder and the compass warm in your"
    "pocket. The room smells of seaweed and coffee; sunlight slices through the tall windows and catches the motes like tiny weather systems."
    "You set down your things, boot up a laptop, and Rafi appears with a tray of over-brewed coffee and an armful of salvaged electronics. He sets a sensor on the table as if offering it for inspection."
    show rafi_chen at left:
        zoom 0.7

    rafi_chen "Grant time?"
    "(He says it like a question that is also a dare.)"
    show maya_armitage at right:
        zoom 0.7

    maya_armitage "We apply. Crowdsource the rest. We make a coalition proposal: community oversight, transparent procurement, and a pilot for community-built floating moorings."
    "(You lay out the headline points, numbering them silently like beads.) 'We emphasize local labor, co-ownership, and an education clause.'"

    rafi_chen "And include a clause for maintenance training. You know developers will try to make it a broken-shelf project if we don't show them it's a living system."
    "(He taps a line of text on the screen.)"
    "You and Rafi trade edits, sentences sharpening into policy language. The tone of your words is different from the flowery slides you'd refused; these lines are blunt with purpose. You send an application to the regional"
    "fund—no glossy gala, just an honest, line-itemed plea. You post a crowdfunding page that is more sweat than story and watch as neighbors drop coins and canned goods into the metaphorical bucket."
    # play sound "sfx_placeholder"  # [Sound: Notification pings; the small bell of community support]
    hide rafi_chen
    hide maya_armitage

    scene bg ch4_453e40_4 at full_bg
    show rafi_chen at left:
        zoom 0.7

    rafi_chen "We can run the mooring prototype offshore this weekend if the tide is right. Tie it to that old buoy?"
    "(He points to a rusted marker in the bay visible through the window.)"
    show maya_armitage at right:
        zoom 0.7

    maya_armitage "Yes. Anchor to what we already have. Keep it simple."
    "(Your voice is steady with a strategist's ease.) 'Rafi, get me the blueprints for the mooring float. I'll get the volunteers and materials.'"

    rafi_chen "And the sensors—I'll waterproof the array. Duct tape and grit, but we'll get reading."

    maya_armitage "Duct tape and grit have a good record in our hands."
    "(You mean it. You also mean the community that has been building resilience for years without fanfare.)"

    menu:
        "Stay and help Rafi waterproof sensors":
            "You sit cross-legged on the floor, soldering iron warm in your lap. Rafi shows you the delicate seam; your fingers fumble at first, then find the rhythm. The sensor casing closes like a satisfied shell, and you feel a tiny victory hum in your bones."
        "Go to the market to drum up volunteers and supplies":
            "You sling the compass and run—market stalls already buzzing, people ready to barter. You return with a crate of salvaged batteries and three new volunteers who know welding. The sight of community hands showing up settles something in your chest."

    # --- merge ---
    "Rafi (laughing) 'You can't resist being in the thick of it. I knew that.'"
    "Rafi: (laughing) 'You can't resist being in the thick of it. I knew that.'"

    maya_armitage "Neither can you, apparently."
    "(He gives you a crooked grin; it is exactly the softening you wanted.)"
    # [Scene: Community Garden & Rooftop Farm | Golden Hour]
    hide rafi_chen
    hide maya_armitage

    scene bg ch4_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low conversation, the rustle of leaves, water trickling from a cistern]
    # play music "music_placeholder"  # [Music: Acoustic guitar; warm, communal]
    "You climb the stairs to the rooftop farm, where raised beds have been grafted into the bones of the market. The air is different here—less diesel, more earth. A neighbor hands you a jar of preserved"
    "lemons; someone else offers you a strip of seaweed jerky. Laughter wraps around the plants; children chase one another between planters, their boots stomping puddles."
    "Nan has a small crowd listening as she traces the old maps with a stick of chalk. People crowd the edges, learning the oral histories, the old homesteads' names. The garden is a cathedral of small rituals—watering, pruning, trading seeds—and it smells like hope."
    "You feel the lift of spirits in the terrace's warmth—the rooftop glows with practical beauty. It's the proof of small victories: a successful pollinator planting, a repaired rain cistern, the city's grant notification you've been too busy to read yet but that Rafi has pinned to the board."
    "Rafi: (tapping the pinned email) 'We got a thing. Small regional grant. Enough for materials for two floating moorings and reinforcement supplies.'"
    "(He looks a little stunned, like someone suddenly gifted a material he can hold.)"
    "A cheer rises, modest and immediate. Neighbors clap and hug, and someone starts playing a hand drum. A woman you don't know hands you a jar of pickled beans with no pretense—just gratitude."
    "Maya Armitage: (inward) The victory tastes like brine and sugar: small, real, and fragile. It buys plywood and float barrels but not the quiet safety of a full plan. That knowledge is a shadow at the edge of the celebration, but the shadow is thin today."
    "Jonah Reyes finds you by the herb beds, his palms dirt-smudged, his smile quieter than earlier."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "You did good. We did good."
    "(He tilts his head, as if measuring the world on a slope.)"
    show maya_armitage at right:
        zoom 0.7

    maya_armitage "We did."
    "(The word feels fuller when spoken aloud.) 'But it's only the beginning.'"

    jonah_reyes "Then let's start with the beginning."
    "(He pulls a loose strand of your scarf between two fingers and traces a salt line along it—an absurdly domestic action after so much work.)"
    "You: (a thought) You could, right now, rest into this human closeness and let the day's ache dissolve. You could also sketch the next steps on your notebook and keep the engines running. Both feel necessary."

    menu:
        "Sit and share the jar of pickled beans with Jonah":
            "You sit on the edge of the planter, open the jar, and pass it to Jonah. The two of you eat in companionable silence, trading small stories about a summer storm and a forgiven failure. The world narrows to jars, hands, and breath."
        "Pull out your notebook and list next-week priorities":
            "You pull your notebook onto your lap and begin to write: volunteer rosters, materials list, training schedule. Jonah watches you for a moment, then leans in to add a note about youth apprenticeships. The planning itself becomes another kind of intimacy—shared purpose inked into a margin."

    # --- merge ---

    jonah_reyes "Whichever you choose, I'm with you."

    jonah_reyes "Whichever you choose, I'm with you."
    "(He says it simply; the sentence is a harbor.)"

    maya_armitage "And I'm with you."
    "(You mean the town, the work, and the person who traces salt lines on your jacket.) It feels like an oath, small and durable."
    # [Scene: Pier | Night]
    hide jonah_reyes
    hide maya_armitage

    scene bg ch4_453e40_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft lapping of waves; the distant creak of a moored hull]
    # play music "music_placeholder"  # [Music: A tender cello; warm, intimate]
    "The pier is quiet. You and Jonah Reyes stand above the water, shoulders rinsed in the day's residue—sweat and salt and the faint oil of marine grease. The string lights bob softly. Around you, muffled laughter drifts upward from the market below, then dissolves into the sound of the sea."
    "Jonah Reyes: (softly) 'We held the line today.'"
    "(He traces the salt-streak on your jacket with a fingertip, following the path as though reading a map.)"
    show maya_armitage at left:
        zoom 0.7

    maya_armitage "We did."
    "(Your voice is smaller than you expected.) 'But there are bigger waves. Evelyn Hart's people will still press. Investors won't like that we did it without their logo.'"
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "Let them bring waves. We'll plant more oysters."
    "(He smiles, a resolute thing.) 'We'll teach kids how to weld, and we'll mend each other's roofs.'"

    maya_armitage "It feels good to believe."
    "(You rest your forehead for a moment against your hand, feeling the cool metal of the compass there. The town's work is not done, but the day has proof: a grant notice, hands ready, and a community that chose itself.)"

    jonah_reyes "You don't have to carry every board alone."
    "(He looks at you like someone offering both hands to lift and to hold.)"
    "Maya Armitage: (a small, guarded confession) 'I know I do it anyway.'"
    "(You let the truth fall into the space between you—your sacrificial streak, the self-expectation you wear like armor.)"

    jonah_reyes "And I'll help pick up the nails."
    "(His humor is blunt and affectionate. He reaches for your hand; you take it.)"
    "The touch is ordinary and radical—palpable proof that working together can repair more than structures. For a sustained moment the air holds nothing but small, domestic details: the texture of Jonah's palm callused from rope, the"
    "smell of your scarf damp with salt, and the distant click of a volunteer securing an oyster cage."
    "Maya Armitage: (inward) Tonight is a ledger entry that will matter. We refused a big check and spent the day translating refusal into action. The grant we clawed—small, yes—buys materials and, more importantly, confidence."

    jonah_reyes "Tomorrow we'll anchor the prototype. Rafi says the sensors will sing."
    "(He gives you a conspiratorial half-grin.) 'You coming?'"

    maya_armitage "Of course."
    "(You mean the community. You mean Jonah. You mean the work that keeps both alive.)"
    "You both look out toward the mouth of the harbor. The moon rests thin and honest over the water. The night is cool and the pier creaks with the tired satisfaction of something that has been mended."
    # play music "music_placeholder"  # [Music: The cello swells into a hopeful cadence; the sound of the harbor at rest]
    hide maya_armitage
    hide jonah_reyes

    scene bg ch4_453e40_7 at full_bg
    "You think of Nan's map, the kids learning knots, Rafi's patched sensors, and the seed jars on the rooftop. Each small thing is a stitch in a larger tapestry. The future is not secure—resource scarcity and political pressure loom—but tonight is testimony: the community can act, and it does."
    "You hold Jonah's hand and let the harbor's quiet settle into your bones. The climb is messy, hopeful, and fragile. It is proof."
    "A thought edges up—Evelyn Hart's emissaries will come, the city's machinery will grind, and the next round will be bargains and boundaries. Your chest tightens, not with despair but with readiness."
    # [Page-Turn]
    "You breathe in the night, tasting salt and wood smoke, and let the image of the patched pier stay in your mind like a breathing thing. The town has chosen its own way for now; the"
    "next meeting, the next negotiation, the next moral corner waits on the horizon. You are not finished—but for the first time in a long while, you know the team you'll climb with."

    scene bg ch4_453e40_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
