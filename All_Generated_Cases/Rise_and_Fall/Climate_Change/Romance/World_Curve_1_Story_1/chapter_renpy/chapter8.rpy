label chapter8:

    # [Scene: Harborside Promenade | Morning, overcast with salt mist]

    scene bg ch8_6b08b4_1 at full_bg
    # play music "music_placeholder"  # [Music: Light, hopeful guitar with soft hand-drums]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the murmur of early volunteers, kettle on a small gas stove hissing]
    "You arrive with your notebook under your arm and the taste of last night's coffee still in the back of your throat. The promenade is a stitched map of people and purpose—Asha's bright scarf like a"
    "flare, Theo bent over a laptop under a tarpaulin, Elias 'Eli' Maren hauling crates of potted greens with a grin that won't quit. Rosa is already at the table, folding pamphlets with hands that remember rope"
    "and nets more than staplers."
    "You press your thumb into the frayed seam where the blue thread holds the notebook—an old comfort—and breathe in the brine and baking bread coming from the volunteer stall. Momentum smells like damp paper and warm hands."
    show asha_patel at left:
        zoom 0.7

    asha_patel "Morning. We have the forum set for eleven. I roped in two neighborhood captains and a local reporter.' (She hands you a steaming paper cup.) 'Coffee's on you, speech is on me, and the moral panic is on—well, let's try to keep that off the table."
    show maya_calder at right:
        zoom 0.7

    maya_calder "Thanks.' (You take the cup and feel the warmth slide into your palms.) 'I want this to be pressure that invites, not frightens. We have to convert curiosity into actual commitments—sign-ups, small donations, rooftop hosts."
    "Asha leans in, lowering her voice despite the open air. She smells of citrus soap and paint."

    asha_patel "We can do a two-track approach: empathy-first messaging and hard numbers on the handouts. But we need a hook. Theo, can we make the data digestible in fifteen seconds?"
    "Theo looks up from his laptop, rubbing the bridge of his nose where a faint scratch lines his glasses."
    show theo_baines at center:
        zoom 0.7

    theo_baines "We can. I rewrote the model to show neighborhood-level risk as a simple slider—household impacts, income disruption, and adaptability score. But if we show too much uncertainty, donors will freeze. If we show too little, we get accused of hand waving."
    "You: (You feel the familiar tightening at the base of your throat—the choice between honesty and persuasion.) 'We need trust,' you say. 'So show them risk, but pair every risk stat with a tangible action—how a"
    "rooftop bed or a sand-socketed berm reduces personal risk. People need to know what they can do now.'"

    theo_baines "Pair data with agency. Got it."

    menu:
        "Hand Asha one of Theo's simplified graphs and ask her to weave it into the opening":
            "Asha nods, taking the sheet. She hums, already crafting language that will make numbers sound like next steps."
        "Let Elias 'Eli' Maren open the forum with music and stories, then bring in data after people are present":
            "Elias 'Eli' Maren's face brightens. He promises a short set—songs that end with a call to the tables. The crowd will be warmer when numbers arrive."

    # --- merge ---
    "The forum opening proceeds with either a numbers-led or story-led approach, shaping crowd temperature."
    "You watch Elias 'Eli' Maren arrange the crates into a makeshift stage, stringing fairy lights between trellises. He moves like he always does—brisk, improvisational—pulling laughter out of volunteers like a harmonica pulls a tune."

    "Elias 'Eli' Maren" "If people are dancing, they're listening. If they're listening, they'll sign. Simple chain reaction."
    "Rosa folds another flyer slowly, each crease deliberate."
    hide asha_patel
    show rosa_calder at left:
        zoom 0.7

    rosa_calder "Be careful what bridges you burn,' she says, not unkindly. 'We've pulled our nets through storms before. We need friends in the council, too. Not everyone with a badge is the enemy."
    "You: (You imagine the council chamber's sterile cool, the way Dr. Sienna Kade's name calms a room or turns it taut.) The memory of her precise, unreadable face is a shadow here—something complex, not a caricature."
    "You can see her influence in budgets and in the polite ways the city defers to 'experts.'"

    maya_calder "We're not here to burn bridges,' you say. 'We're here to make the bridge wider—hold more people."
    # [Scene: Rooftop Gardens & Micro-farms | Midday, gold bleeding through cloud]
    hide maya_calder
    hide theo_baines
    hide rosa_calder

    scene bg ch8_6b08b4_2 at full_bg
    # play music "music_placeholder"  # [Music: Harmonica and guitar weave into an acoustic festival rhythm]
    # play sound "sfx_placeholder"  # [Sound: Laughter, the slap of boots on decking, the chink of tin cups being collected]

    "Elias 'Eli' Maren" "Two hours, then demo tours! We're turning soil into proof.' (He hands you a small, sun-warmed lettuce.) 'Taste one."
    "You: (You bite into the lettuce, and it's crisp and faintly peppery. The flavor is small revolutions—salt-kissed, grown over the city's concrete ribs.) 'It's better than the slide deck promises,' you say, and you mean it."
    "Theo appears with a tablet in hand, cheeks flushed from climbing the ladder."
    show theo_baines at left:
        zoom 0.7

    theo_baines "I compiled microcase studies—three household profiles, projected benefits over five years using local inputs. If we put those in people's hands, donors see real people, not abstract percentages."
    show asha_patel at right:
        zoom 0.7

    asha_patel "And we have volunteers ready to deliver those packets to council members' neighborhoods. Let them read the names of their constituents before the vote."
    "Rosa watches the crowd, her eyes noting who laughs and who carries the burden of a tired jaw."
    show rosa_calder at center:
        zoom 0.7

    rosa_calder "Start small and show growth. People remember what fed them."
    "You feel a surge of something that isn't just adrenaline—it's craft turning into a plan. You can orchestrate this: a festival to humanize data; door-to-door packets to make councilors feel the neighborhood's pulse; a staged interruption if we must. Each is a lever with different pressure and consequence."

    menu:
        "Volunteer to hand-deliver packets to a councilor's neighborhood with Theo":
            "Theo claps your shoulder. The walk is brisk, the exchange quiet but effective—neighbors accept the packet with nods, a few add their own notes."
        "Help Elias 'Eli' Maren fine-tune the festival's program so the message lands between songs":
            "Elias 'Eli' Maren and you sit under the trellis, writing short scripts between setlists. Laughter and applause become the connective tissue for policy language."

    # --- merge ---
    "Both routes deepen neighborhood engagement and refine outreach tactics."
    "Elias 'Eli' Maren sits beside you on a low bench, his sea-glass eyes bright. He keeps tucking a loose strand of hair behind his ear, an absent gesture that steadies him."

    "Elias 'Eli' Maren" "People will come because it's beautiful,' he says. 'They'll stay because it helps. You can hit the council with facts, but you win affection with a bowl of soup and a song."
    hide theo_baines
    show maya_calder at left:
        zoom 0.7

    maya_calder "Sometimes I worry that charm alone won't push funding lines. But charm opens the door."

    "Elias 'Eli' Maren" "And your plans keep it from slamming shut."
    "The two of you talk longer than is strictly necessary about logistics—sound levels, which volunteers will lead tours, who will introduce the microcase studies. The conversation widens and contracts like tides, practical and personal folded together."
    # [Scene: Harborside Forum Setup | Late Afternoon]
    hide asha_patel
    hide rosa_calder
    hide maya_calder

    scene bg ch8_6b08b4_3 at full_bg
    # play music "music_placeholder"  # [Music: Strings swell faintly, hopeful]
    # play sound "sfx_placeholder"  # [Sound: A murmur of an assembling crowd, the clack of a folding chair]
    "A small cluster of neighborhood council members arrives early. You feel the familiar executive etiquette wash over them—pursed lips, the soft leather of their folders. They look, in turns, curious and guarded."
    "Maya Calder steps to the mic first, then let Asha lead with a warm welcome. Theo hands over a stack of simplified data sheets to the reporters. Elias 'Eli' Maren plays a short set that turns conversation into rhythm. The crowd begins to lean in."
    show asha_patel at left:
        zoom 0.7

    asha_patel "We're asking for three things today,' she says, voice steady. 'A pilot budget for community-run green infrastructure, guaranteed relocation assistance where necessary, and a transparent timeline for the seawall so it's not our community making sacrifices alone."

    "Council Member" "And what do you propose as an alternative in areas where the wall is the only viable option?"
    "You: (You feel the knot of responsibility tighten and then ease—you have prepared for this.) 'Not alternatives—complements. We propose a hybrid strategy: targeted barriers in conjunction with community-managed regenerative systems that reduce load and create livelihoods. We can model these outcomes in weeks, not years.'"
    "The exchange opens a door. Cameras angle; someone tweets a clip. Momentum hums. You see faces in the crowd—young parents, older fishers, a small group of city planners scribbling notes. Hope is a crowd that leans forward."
    "Theo: (to you, quietly) 'We can amplify the neighborhoods' cost-savings if we get funders to see the long-term ROI.'"
    "Rosa: (placing a hand on your arm) 'Don't let the urgency make you violent. We can be formidable without burning people.'"
    "Your internal monologue runs through outcomes like tide charts—each tactic plotted for risk and reward. You imagine the council disrupted in a way that forces dialogue but risks hardening opinions. You imagine releasing comparative data that"
    "shifts donor calculus but fractures trust. You imagine the rooftop festival scaled into undeniable proof, slow but persuasive."
    "Your agency hums: you can be theatrical or methodical, expose or persuade, rage or woo. The future hinges on which song you choose to sing."

    menu:
        "Suggest we stage a symbolic interruption at the council vote to force immediate concessions":
            "Asha frowns, weighing the moral cost. Theo shifts uneasily. Elias 'Eli' Maren's fingers drum—excited but aware. Some in the crowd clap; others exchange worried looks."
        "Advocate for carefully releasing comparative data to funders, with legal checks":
            "Theo's eyes light up at the thought of hard evidence doing the persuading. Rosa stiffens—her worry about burned bridges sharpens. The reporter in the back scribbles faster."

    # --- merge ---
    "The choice will shape tactics and relationships with funders and council members."
    "You stand under the bunting, the city's breath mingling with the festival's music and the low, steady click of volunteer radios. The decision is a tide you can't avoid; it will pick up everything you've sewn so far and carry it somewhere new."
    "You feel your fingers close around your notebook. Words line up—strategy, ethics, risk, love. You can taste the bright copper of possibility."
    hide asha_patel

    scene bg ch8_6b08b4_4 at full_bg
    # play music "music_placeholder"  # [Music: Hopeful motif swells, then softens]
    # play sound "sfx_placeholder"  # [Sound: The crowd's chatter becomes a single, expectant hum]
    "You inhale. You can feel the city waiting for the note you will strike."

    menu:
        "Interrupt the council vote with a mass demonstration.":
            jump chapter9
        "Publicly release comparative data to pressure funders.":
            jump chapter9
        "Build a scalable, live green-infrastructure demonstration to win hearts and evidence.":
            jump chapter14
    return
