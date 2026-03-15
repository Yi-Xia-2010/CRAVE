label chapter10:

    # [Scene: Harborfall Promenade | Morning]
    # play music "music_placeholder"  # [Music: Low, distant strings; a single trumpet thread undercurrent]

    scene bg ch10_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Gull calls, a distant diesel cough, the soft slap of pamphlets against a railing]
    "You stand on the promenade and watch the town wake like a slow tide. Fog lifts in ragged strips. The sea smells of iron and old kelp, and your dive watch—heavy in the pocket of your"
    "jacket—taps against your ribs with a familiar, useless rhythm. It is a small thing that anchors you to what is lost and what remains; you imagine your brother fastening it on a wrist that used to"
    "know how to laugh storms down."
    "Your waterproof notebook is in your hand, pages slightly damp from yesterday's rain. On its inside cover: names, addresses, shorthand arguments—one-sentence truths you hope will hold the town together. The referendum is a fragile vessel, and you are bailing with a spoon."
    "You walk toward Hana's, the smell of frying onions folding into the brine. Banners flutter on the lampposts—some handmade, some printed in corporate steel-blue—and already the street is absorbing the new geometry of the vote: groups"
    "clustered like flotsam, pamphlet towers sprouting on tables, a kid with a spray-painted sign chasing a dog."
    # [Scene: Hana's Diner | Midday]

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Coffee machine hiss, the soft clatter of silverware, low conversation]
    # play music "music_placeholder"  # [Music: Piano, minor key with slow tempo]
    "Hana is at the hatch wearing her apron like a battle flag. Her smile is ferocious in the way of people who have learned to feed a town through any weather."
    show hana_kim at left:
        zoom 0.7

    hana_kim "You look like you haven't slept, Maya. Sit. I'll force coffee on you like it's an emergency ration."
    "You let her shepherd you to the corner table. The diner has been refitted into a nerve center: maps taped to the windows, pens in jam jars, a whiteboard listing canvassing shifts. The air is warm"
    "with grease and determination. Voices circle—Tomas' low mutterings, Dr. Noor's shorthand in a corner, the familiar low laugh of people who still think community can fix anything if given time."
    "Hana leans in, wiping her hands on a towel. Her eyes are quick and soft."

    hana_kim "We collected twenty signatures before breakfast. Tomas took the early round at the pier, Mayor's office said they'd post the referendum notice today. But Lux put up another billboard last night—giant wave, a steel wall. God, those colors."
    "You thumb through the notebook. The list of volunteers is long enough to be hopeful. The list of costs—advertising buys, municipal fees, printing—hangs like unread mail."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "We need door-to-door. People don't debate schedules in the square; they talk over dinner. Tomas knows the coves. Noor has data nights if we can borrow the community center. And—' you pause, tasting the word—'we need to keep this honest. No scare-scripting."

    hana_kim "Honesty's our best weapon. But the world has money made into a megaphone. They bought a megaphone. We have two things: the truth and stubborn lungs."
    "There is a knock at the diner's window. You turn. Tomas is there, rain-beaten hat in hand, eyes that have watched a hundred seasons and come back with fewer illusions."
    show tomas_bianchi at center:
        zoom 0.7

    tomas_bianchi "Maya. I signed the petition. Many will. But listen—people are afraid. They ask for rocks and walls. Tell me again why you want roots in mud instead of concrete."
    "The question is older than you. It is the shape of your struggle compressed into one slow drawl."

    maya_inoue "Because roots breathe. Because the mangroves will slow the water and feed the estuary, not just push the problem sideways. Because the town survived by reading the sea, not by pretending we can dominate it."
    "Tomas folds his hands, the Caribbean knot of an old seafarer. He does not argue so much as lay out consequences of memory."

    tomas_bianchi "I know what the sea does. I lost nets to tides the same as anyone. But storms take jobs, houses—don't make people choose philosophy when their barns float. People will vote to keep their roofs."
    "The exchange ripples through you. There is no tidy rebuttal; there is only a stubborn, inevitable collision between principle and shelter."

    menu:
        "Offer Tomas the community plan, earnest":
            "You unfurl the maps and point to the estuary, voice low and granular: you show him the pockets where seedlings could be planted, the raised walkways—his fingers trace the route like an old chart. He nods, eyes softening but wary."
        "Acknowledge the fear, offer pragmatic compromise":
            "You lower your voice and speak plainly: 'We can make phased protections—temporary barriers while mangroves take. We don't have to lose everything overnight.' Tomas listens; the line around his mouth relaxes a degree. He doesn't smile, but he doesn't walk away either."

    # --- merge ---
    "Hana watches the quiet negotiation and brings more coffee. She has a way of standing at the rim of arguments and knitting them together when you both need a stitch."

    hana_kim "Whatever you pick, I will feed the people who do the work. But promise me—don't let this become us vs them. We burn faster than any billboard."
    "You promise. It is one of the few promises you can keep."
    # [Scene: Market Square | Afternoon]
    hide hana_kim
    hide maya_inoue
    hide tomas_bianchi

    scene bg ch10_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmurs of debate, the rustle of paper, a municipal PA in the distance repeating referendum logistics]
    # play music "music_placeholder"  # [Music: Strings, thinner now; unresolved chords]
    "Canvassing is a choreography of small truths. You move from door to door with volunteers, the notebook heavy in your hand. The town answers with a thousand textures: an old woman who remembers the lighthouse's keeper,"
    "a teenager with Futurist stickers on his sleeve, a family with a house on stilts that the children chase each other around. You talk about stewardship, about who decides what to save, about what kind of"
    "Harborfall you want to leave to the next tide."

    "You encounter the LuxCorp van twice—once rolling through with a public relations rep smiling too brightly, once parked with a screen looping a simulation: a glimmering wall holding back an apocalyptic swell. The colors are immaculate blue. The tagline repeats" "Protect More Lives. Act Now."
    "They have polished certainty. You have ragged honesty."
    "At one door a young father slams the pamphlet down."

    "Young Father" "You want us to vote against a company that'll pay for our protections? How am I supposed to sleep when your 'roots' will take ten years?"
    show maya_inoue at left:
        zoom 0.7

    maya_inoue "You don't have to wait ten years while doing nothing. The referendum is about control, not delay. If the town decides, the money goes into a community plan—conditional, accountable, transparent. We can set timelines and benchmarks."
    "Young Father: (a beat) 'And if investors walk? We lose everything.'"

    maya_inoue "Then we plan for contingencies. We build alliances with neighboring towns, claw for grants—it's messy, but it's ours."
    "His jaw tightens. He doesn't sign today. You file his name under 'Follow-up' and move on."

    menu:
        "Call Kaito and ask him to bring simplified sensor demos to market square":
            "You pull out your phone and call Kaito. He answers within three rings, tentative and awake. He agrees to bring the prototypes—small wins helping people feel the science beneath the talk. Volunteers cheer when he arrives an hour later with a crate of blinking sensors."
        "Conserve energy; focus on older voters and door-to-door instead":
            "You tuck your phone away and prioritize the map: elders and fishermen first. It's slower but deeper. By evening, Tomas and a few volunteers have knocked on more doors than the sensors could reach."

    # --- merge ---
    "You see Mayor Elena across the square, clipboard in hand, wearing that tired dignity that only municipal leaders carry. She gestures you over; her eyes read like someone who has counted votes into the early hours and woken to the same arithmetic."
    show mayor_elena_rossi at right:
        zoom 0.7

    mayor_elena_rossi "Maya, the council's worried. Lux has filed to run paid ads; their legal says we can't stop commercial speech. I'm trying to secure a neutral space on the town feed, but our budget—' she exhales, '—our budget is a paper boat."

    maya_inoue "Ask for a public forum for data transparency. Call Noor to present the risks and timelines. Push for fact sheets on both options. People need to see the trade-offs."

    mayor_elena_rossi "Fact sheets are fine until the day the sea comes. I promised to keep people safe. I don't think the referendum will save us tomorrow."
    "Her hands find yours for a brief moment, an anchor between leaders who understand how brittle promises feel."

    mayor_elena_rossi "But if this goes through, your fingerprints will be on it. If it fails, I will have to live with that too. I want fairness, Maya. I want you to know I am trying."

    maya_inoue "I know. I believe you are."
    "Her gratitude is small and human. It glows like an ember but it will not stave off cold alone."
    # [Scene: Promenade — Dusk]
    hide maya_inoue
    hide mayor_elena_rossi

    scene bg ch10_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant thunder roll, the hiss of a projector, voices thinning]
    # play music "music_placeholder"  # [Music: Cello, slow, with low piano—resigned cadence]
    "Evenings feel like the old Harborfall for a heartbeat: volunteers eating Hana's soup under strings of bulbs, older hands comparing tide notes with young ones, laughter that starts because someone dropped a joke about corporate PR."
    "For a moment you carry a lightness that surprises you. You are proud—this is what town looks like when it stands up to being priced out of its own future."
    "But politics is a slow tide. LuxCorp's counter-campaigns arrive like slick swells: paid billboards, a short film with drone shots of serene beaches behind their proposed wall, a glossy brochure that folds like a promise. Towns"
    "two miles down the coast have already started accepting conditional funding; their mayors' faces appear in local feeds endorsing the steel-blue future. Investors murmur. The municipal coffers do not scale to match glossy production."
    "Kaito Sato finds you by the railing. He looks like he has been everywhere and nowhere; sensors hang from his satchel, one blinking patiently."
    show kaito_sato at left:
        zoom 0.7

    kaito_sato "You're moving a mountain with a teaspoon."
    "It isn't an accusation—it's a plea. He knows the math better than most. He knows the lag between planting and protection."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "We need that teaspoon. We need people who will tend the roots."

    kaito_sato "I'm worried about timing. If Lux frames this as 'wait and lose,' they'll convert fear into a mandate. Investors are opportunistic. If we can't show at least partial, replicable results quickly, the referendum could backfire."

    maya_inoue "We can't trade our stake in the town for a veneer of safety."
    "Kaito Sato: (after a long beat) 'I know. I'm not saying sell out. I'm saying we need a narrative and scaffolding that looks immediate—sensors, temporary berms, a clear step one. People need to see movement.'"

    maya_inoue "People also need to feel that the movement is theirs. If this is another external fix... it's not the same."
    "He looks at you, an unreadable mixture of hope and calculation folding under his gaze."

    kaito_sato "Whatever you choose, I will help."
    "Kaito Sato's promise feels both like balm and a reminder: engineering can help, but it cannot substitute consent."

    menu:
        "Tell Kaito how you really feel—frustration and tenderness":
            "The words come out clipped and honest: you admit the exhaustion, the fear, the way his calm terrifies and comforts you. Kaito's face softens; he reaches across and squeezes your hand briefly. The moment is warm and complicated, then they both step back."
        "Stay professional; focus on logistics for the vote":
            "You keep your voice measured and tactical, listing timelines and resource needs. Kaito nods, searching your face for the spark behind the planner. He accepts your composure but his concern doesn't ease."

    # --- merge ---
    "Night thickens and LuxCorp's screens continue their patient broadcast: safety rendered as a product. The promotional images crash against the gel of reality in your head—steel walls that might protect some coves but seal off others, jobs traded for contracts, fishermen without nets."
    "You fold your hands around the dive watch in your pocket. The weight of it is a private metronome counting out risks: legal, social, physical. You think of your brother and the tide that took him."
    "Activism is supposed to be a way to keep that from happening again. But sometimes keeping means making hard concessions—and you don't know which ones you will have to make."
    "At the edge of the square, a small group begins to fray. Arguments harden into shouts. Someone tears down a pamphlet and storm-walks away. You feel it in your chest: the strain of being the hinge between stubborn hope and the relentless logic of money."
    "You walk home in the rain that follows the light, the town behind you like a living thing that breathes uneasily. You prepare the next day—schedules, volunteers, the whiteboard of who will speak where. The referendum"
    "will mean something either way: validation if you win, emboldenment if you lose. It will not keep the sea at bay tomorrow."
    "You make one last call—Mayor Elena, Tomas, Hana—voices you shore up your resolve with. The town's energy is raw and beautiful, then fraying. You sleep in fits, dreams made of seawalls and seedlings braided together."
    # [Scene: Rooftop outside Hana's Diner | Dawn]
    hide kaito_sato
    hide maya_inoue

    scene bg ch10_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Sparse gull call, distant generator hum]
    # play music "music_placeholder"  # [Music: Minimal piano, single descending motif—somber]
    "Dawn finds you holding your notebook again, the page edges curled. The referendum will be framed tomorrow in the square. You will step up and speak for a vision that asks the town to be patient, proud, and sovereign. It is a moral choice steeped in risk."
    "You take a breath and feel the weight of what you have asked of your neighbors—of yourself. You have rallied a village to vote for control over convenience, to trust communal labor where money buys speed."
    "You did it because principle matters to you, because giving the town its voice felt like honoring your brother's memory."
    "But then the practical thoughts press in, quick and insistent: paid ads will drown our voices. Voters scared of losing their homes will vote for immediate shelter. If we fail, investors will take the town's consent"
    "as permission to roll out solutions without accountability. If we win, will we have enough time? Enough money? Enough cohesion?"
    "You feel the fall settle into you—the hard, honest gravity of difficult choices and the cost of refusing shortcuts. This is not a triumphant march. It is a slow descent into a longer fight."
    "You finish the page in the notebook and close it. The lines between right and feasible blur. You lift your head and look toward Market Square, where by noon the town will be gathered."
    "Your next step matters. So does the shape of the strategy you carry to the microphone."
    "You hold the choices in your hands: whether to anchor the referendum on the patient work of ecological restoration; to swing the town's machinery by exposing corporate terms and playing hard; or to try to braid both together into a precarious compromise."

    menu:
        "Anchor on ecological restoration—mangroves and local stewardship":
            jump chapter11
        "Run a media expose on LuxCorp's terms":
            jump chapter12
        "Propose a hybrid: citizen-led plan with conditional external funding":
            jump chapter13
    return
