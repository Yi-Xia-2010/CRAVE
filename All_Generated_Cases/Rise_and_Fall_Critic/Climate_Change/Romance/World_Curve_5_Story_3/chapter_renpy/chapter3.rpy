label chapter3:

    # [Scene: Old Quay | Early Evening]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm strings with a steady, hopeful rhythm]
    # play sound "sfx_placeholder"  # [Sound: Low murmur of voices; water lapping against pilings; the distant call of a gull]
    "You breathe in. Salt and citrus—Elena Navarro's bundle—mix with the faint diesel tang of a generator powering the projector. The air is warm, pressed to the skin, and the sea breathes at the edges of the"
    "gathering: the tide is close enough to smell the mud, far enough to keep feet dry. Faces you know fold into the crowd—old fishermen in rubber boots, teenagers with spraypainted posters, neighbors with toddlers asleep on"
    "their shoulders. The quay feels like a heart beating itself awake."
    show aria_navarro at left:
        zoom 0.7

    aria_navarro "This is the frame. Numbers and story need to hold together long enough for someone to choose what comes next."
    show dr_kavir_singh at right:
        zoom 0.7

    dr_kavir_singh "Whenever you're ready, Aria."
    "You set the laptop on the crate, flick the projector on; a pale slide blooms against a tarp—maps, sensor graphs, a photograph of a child holding a newly planted mangrove shoot. The projector hums. Someone murmurs appreciation at the image."
    "You open your mouth and speak, your voice steady but threaded with the small tremor of meaning."

    aria_navarro "Thank you all for coming. Tonight isn't just about plans on paper. It's about which futures we choose for our homes and children. We have options that can protect us now, and options that will heal what the sea has begun to take. I want us to look at both."
    hide aria_navarro
    hide dr_kavir_singh

    scene bg ch3_98c6f2_2 at full_bg
    "You run through the data gently: sensor-backed projections of storm surges, modeled flood lines, the carbon and sediment benefits of healthy mangroves. You pair each statistic with a fingerprint of story—a fisher's memory, a child's first"
    "mud-squelch planting. The crowd listens; the light from the lanterns pools into attentive pockets on faces."
    "A hand shoots up from the front rows—one of the elder fishers whose name you know but don't need to call. He smells of smoke and salt and has a voice like gravel."

    "Elder Fisher" "Numbers sound nice, niña, but what's nearer? My house? My nets? My wife sleeps with the door unlocked because she thinks the tide might not come back right."
    "You meet him with the calm you prepare for in late nights of drafting and listening. You consider the technical answer—deployable modules, quick construction timelines—but you also hold the human one."

    menu:
        "Show the immediate flood model—project where seawalls would save homes":
            "You switch to the deployment model slides. The tide lines recede visually from homes on the map, and a hush falls; people nod, thinking of roofs and warm beds."
        "Tell the fisher a short story about Mrs. Delgado, who planted a mangrove with her grandchildren":
            "You tell the small story instead. The crowd leans in; someone smiles, and that fisher's jaw relaxes as the image of a mangrove row and a child's small hands settles in the air."

    # --- merge ---
    "The meeting continues as the exchange is addressed by others in the crowd."
    "Mateo Hale steps forward before you can let the moment go on too long. His boots thud softly on the wet boards; he wears his municipal jacket, the reflective strip catching the lantern light like a promise of order."
    show mateo_hale at left:
        zoom 0.7

    mateo_hale "We can get modular seawalls in within weeks. They're designed to flex with the tide. We buy time, ensure people's houses aren't lost in the next surge. Delay equals danger."
    "Sora Lin doesn't let him finish without answering. They move as if they were part of the crowd's breath: quick, alive, a smear of cobalt streaks in the evening."
    show sora_lin at right:
        zoom 0.7

    sora_lin "Buying time is different from buying safety. Those walls push the problem outward and make people think the sea is conquered. Mangroves and seagrass rebuild the coast. They hold sediment, they slow water, and they belong to the community—we plant, we care for them; that care keeps people here."
    "The exchange is not sharp so much as layered—two kinds of urgency pressing against each other. Mateo Hale's words are measured, short sentences like beams. Sora Lin's are full of images and heat and the noise of the crowd swells with their cadence."

    mateo_hale "I don't discount care. But we have families on the line now. We have an evacuation history that shows walls change outcomes. Metrics we can measure mean lives we can save."

    sora_lin "Metrics you measure might miss what we lose—the culture, the trust in the shoreline. You can't measure the lullaby a child learns from the mangrove's sound. You can't let 'we'll do it later' be an excuse when the sea is already at our back."
    "The crowd shifts; Elena Navarro watches you from one side, her face a map of the town's years. Her hands are folded over something—maybe the same smell of citrus from earlier—and she eyes both Sora Lin and Mateo Hale like she is weighing tides."
    show elena_navarro at center:
        zoom 0.7

    elena_navarro "We need hope that keeps both the house and the history. I trust my daughter. Tell them the thing that makes you want them to stand with you."
    hide mateo_hale
    show aria_navarro at left:
        zoom 0.7

    aria_navarro "This is the tight line—to speak for both shelter and memory. To be clear enough for the mayor to vote, but generous enough to hold people together."
    "A younger woman at the back raises a concern about funding timelines. The mayor checks her tablet; the municipal ledger is a real, tight band."
    hide sora_lin
    show mayor_isla_cortez at right:
        zoom 0.7

    mayor_isla_cortez "We need an approach that the council can approve tonight—something decisive. Grants and donor timelines are not infinite. Aria, you've put these together. Which do you recommend we choose immediately?"
    "The question lands like a bell. The projector light softens; dozens of faces turn to you. Mateo Hale's jaw tightens. Sora Lin's mouth is set, but their eyes are hopeful, fierce. Dr. Kavir Singh watches you for the science; Elena Navarro for the heart. The moment lengthens."
    "Before you answer, Jun Park nudges your shoulder—small, practical, a spark."
    hide elena_navarro
    show jun_park at center:
        zoom 0.7

    jun_park "If it helps, you can frame it as a first-deploy with a plan to scale into restoration. Folks like steps they can see."
    "You swallow. There are ways to stitch hope into policy, to frame the medium-term as both urgent and caring. Your chest loosens at the thought of that middle ground, but you know the town will hear your words as a direction to act, to back."

    menu:
        "Lead with the measurable—prioritize immediate deployment, promise staged restoration":
            "You outline a rapid-deploy first step with scheduled restoration phases. People's eyes flick from relief at the immediate protection to concern about the promised future work—satisfaction tempered by questions about follow-through."
        "Lead with the communal—call for accelerated restoration now with municipal support spread over time":
            "You place the restoration at the center, appealing to volunteers and cultural memory. The crowd erupts with chants of 'Plant!'—excitement and fear braided together as people imagine mud on their hands instead of concrete under their feet."
        "Explain a pilot hybrid council to decide priorities democratically over the next month":
            "You suggest a hybrid pilot governed by a community council, balancing quick modules and accelerated planting. The idea draws mutters—it's messier and slower, but people nod at the promise of shared control."

    # --- merge ---
    "The debate continues as leaders respond and the room prepares to vote."
    "Mateo Hale crosses his arms, the municipal patch creasing."
    hide aria_navarro
    show mateo_hale at left:
        zoom 0.7

    mateo_hale "Messy doesn't save a house tonight, Aria. If you suggest a slow council, I'll have to get permits and cranes and the mayor's approval dragged through more meetings. The risk of delay is real."
    "Sora Lin steps closer to you, near enough that the lantern light catches the cobalt streak in their hair like a small flare."
    hide mayor_isla_cortez
    show sora_lin at right:
        zoom 0.7

    sora_lin "Messy is how we make sure the people who live here decide how we live here. If the plan is only decided in a council room, it's not ours."
    "Your heart is a tight drum in your throat. In the data, the hybrid models show promising interaction effects—but they also require trust and a visible plan for execution. The crowd is not a single mind;"
    "it's a networked, living thing—each face an argument, each clap a vote that could tilt a policy."
    hide jun_park
    show aria_navarro at center:
        zoom 0.7

    aria_navarro "We don't have to choose between urgency and agency. We can plan for immediate protection where lives are at imminent risk, while launching community-led staging for restoration that scales quickly with local oversight. But I want us to decide it together, with a clear timeline and accountability."
    "Mayor Isla Cortez folds her hands and taps a stylus against her tablet. She sorts the room with a leader's eye—who will be satisfied, who will be convinced."
    hide mateo_hale
    show mayor_isla_cortez at left:
        zoom 0.7

    mayor_isla_cortez "You're asking us for clarity, Aria. The council wants to know what to put their vote behind tonight. This is the moment. We need an answer."
    "You feel a warmth under the ribs—the rising chord of the evening—people on edges leaning in, the town's tide of hope pulling toward action. Your role is not just to choose, but to frame the choice so whoever votes understands what's at stake: lives, livelihoods, future stewardship."

    aria_navarro "This is the hinge. Whatever I say will bend futures. I can promise measured safety, call for communal restoration, or offer a shared pilot that asks for patience but offers ownership. All of those are honest. All of them ask something of the town."
    "You glance at Mateo Hale—his hands are steady but his fingers flex near a pocketed multi-tool. Then to Sora Lin—their lips are parted like they're about to sing. Elena Navarro's eyes shine with an unspent private pride, and Dr. Kavir Singh's expression is quietly unreadable—complex."
    hide sora_lin
    hide aria_navarro
    hide mayor_isla_cortez

    scene bg ch3_98c6f2_3 at full_bg
    show mayor_isla_cortez at left:
        zoom 0.7

    mayor_isla_cortez "Aria—speak plainly. Tell us which of these we should vote on right now. We will follow a clear recommendation."
    "Your voice finds a calm center. You choose words that carry data and memory, policy and trust. You know that the town is ready to rise with you."
    "You take one more breath, look out across the faces you grew up with and the younger ones you're helping to inherit the coast, and prepare to name the way forward."

    menu:
        "We prioritize deployable adaptive infrastructure—seawalls and modular levees—so we buy time and protect homes.":
            jump chapter4
        "We commit to community-led ecological restoration—massive mangrove and seagrass planting—so we build long-term resilience.":
            jump chapter8
        "We launch a hybrid pilot: small adaptive modules plus accelerated restoration, decided by a community council.":
            jump chapter12
    return
