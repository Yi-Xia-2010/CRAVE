label chapter10:

    # [Scene: Mika's Workshop | Dawn]

    scene bg ch10_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A kettle begins to hiss on a small stove; distant gulls call. Footsteps on board planks.]
    # play music "music_placeholder"  # [Music: Gentle, rising strings with a hint of percussion — like tools finding rhythm.]
    "You fit the dented metal key into the old lock and let the click sound like an agreement. The workshop smells of oil, wet rope, and the faint sweetness of seaweed someone left to dry on"
    "the bench. Your palms bear salt and the heat of the kettle; for once, they tremble from excitement more than from worry."
    "The tables are already ringed with chairs. Jun's cap is on the far workbench, rim dusted with sawdust that catches the light. Riv is pacing with his bandana tied bright and conspicuous, a stack of flyers"
    "fanned in one hand like a magician's cards. You set your jaw, breathe out, and step into the role you promised to try: convenor, not lone-fixer."
    show jun_park at left:
        zoom 0.7

    jun_park "Mornin', Mika. Coffee's weak but it does the job. You okay?"
    show mika_hoshino at right:
        zoom 0.7

    mika_hoshino "I am. The town's what I'm carrying today.' (You roll a tool between your fingers.) 'We need structure. Rules that actually work on the ground."

    jun_park "Rules, not platitudes. I can prep a rotation schedule for repair crews. A roster that doesn't burn people out."
    show ravi_riv_delgado at center:
        zoom 0.7

    ravi_riv_delgado "I hit Mrs. Delgado's stoop. She'll host a potluck tonight if we promise no speeches—just food and hands-on demos. People love food, Mika. They love tangible stuff even more."
    "You look around at the mural of tide lines in your head and at the brass plaque your mother riveted into the workbench. There's a kind of domestic holiness here: nicked benches, labeled jars of screws,"
    "the dented kettle. Turning this into a real cooperative will require endless small acts like these, not grand gestures."
    hide jun_park
    hide mika_hoshino
    hide ravi_riv_delgado

    scene bg ch10_453e40_2 at full_bg
    # play music "music_placeholder"  # [Music: The strings swell slightly, hopeful and steady.]
    show mika_hoshino at left:
        zoom 0.7

    mika_hoshino "Okay. We'll do bylaws, shared ownership for equipment, and a schedule. Jun, draft a maintenance protocol. Riv, organize outreach routes and the potluck. I'll turn the ledger over — and Elias Maren is running a training on kelp co-op protocols this weekend."
    show ravi_riv_delgado at right:
        zoom 0.7

    ravi_riv_delgado "Kelp co-op protocols. Say that five times fast and then shout it from the boardwalk."
    show jun_park at center:
        zoom 0.7

    jun_park "And be blunt with Amina. We need that municipal plot to put up demonstration beds before the next tide season."
    "You feel the weight of saying Amina's name — politics exists like an undercurrent — but the room doesn't flinch. You have allies, and naming the risks aloud makes them manageable."
    # [Scene Transition]
    # [Scene: Greenhouse Rooftop Lab | Late Morning]
    hide mika_hoshino
    hide ravi_riv_delgado
    hide jun_park

    scene bg ch10_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The muted chatter of neighbors below; the greenhouse fan whirs.]
    # play music "music_placeholder"  # [Music: Soft piano with plucked strings, warm and intimate.]
    "You climb the narrow ladder and step into a world that always feels reassuringly enclosed: the greenhouse is a raft of green in a town of salt and wood. Elias Maren is there, sleeves rolled up,"
    "hands still carrying the faint smell of algae. He looks up, and for an instant he is all attention — a lighthouse switching focus to you."
    show elias_maren at left:
        zoom 0.7

    elias_maren "I've got sample protocols for community-run kelp beds. Short training modules, hands-on. People can learn to monitor nitrate levels, map growth patterns. We won't need a lab per se—just steady volunteers and simple tools."
    show mika_hoshino at right:
        zoom 0.7

    mika_hoshino "Can you make that clear for someone who's never touched a refractometer?"

    elias_maren "I'll make it clear for someone who thinks sea-science sounds like sorcery. We'll do demos, and I'll bring the drone. Show the beds from above so folks can see what's actually happening."
    "He runs a thumb along a drawing: rows of floating lines, buoys, and hand-lashed anchors. The plan is humble — modular floats, community-owned rope, a registry of participant hours. It feels like a blueprint for belonging."

    menu:
        "Ask Elias to simplify the training to one page":
            "He quickens, making shorthand diagrams, his eyelashes crinkling in concentration—relief and gratitude leaking into his smile."
        "Request Elias bring a live demo piece of kelp to the potluck":
            "He laughs softly and tucks the notebook under his arm like a promise—already imagining a jar of living green as a conversation starter."

    # --- merge ---

    elias_maren "Also—if we couple the kelp beds with community harvest shares, revenue can flow back into tools and wages. It's not charity; it's ownership."

    elias_maren "Also—if we couple the kelp beds with community harvest shares, revenue can flow back into tools and wages. It's not charity; it's ownership."
    "You think about the ledger you promised to open. Ownership changes how people show up. It makes late-night repairs less about thankless obligation and more about someone you can call a partner."
    # [Scene Transition]
    # [Scene: Municipal Land — Salt Flats Edge | Afternoon]
    hide elias_maren
    hide mika_hoshino

    scene bg ch10_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Conversation, the clink of stakes being hammered, a far-off diesel truck.]
    # play music "music_placeholder"  # [Music: A slow, bright motif with a steady heartbeat of a drum — progress with caution.]
    "Mayor Amina stands with arms folded, scarf braided into the silver braid at the crown of her head. Her face is tired but composed—an expression you have learned to read as 'careful openness.' Around her, two municipal planners fuss with papers and maps."
    show mayor_amina_bakar at left:
        zoom 0.7

    mayor_amina_bakar "We can earmark this strip as demonstration beds. It's municipal, yes. But you need to show me governance that won't let equipment disappear or promises evaporate after the grant runs dry."
    "You take a breath. You present the preliminary bylaws — a straightforward document with clauses for shared ownership, scheduled maintenance, transparent ledgers, and community arbitration. You have Jun's line-item budgets and Riv's outreach plan stapled in."
    show mika_hoshino at right:
        zoom 0.7

    mika_hoshino "We propose rotating stewardship, a public ledger, and a small oversight committee made up of residents. If the cooperative holds people accountable, the town keeps the benefit."
    "Amina studies the pages like a judge weighing an important precedent, then looks at you."

    mayor_amina_bakar "If you can prove operation for six months with volunteer labor and a clear distribution plan for harvests, I'll sign off on long-term access. But understand—if representatives complain about misuse, I will pull it back."

    mika_hoshino "That's reasonable. We'll accept reporting and periodic audits. This isn't just about a grant—it's about changing how we steward what we have."
    "Her eyes soften a fraction. There is relief in that softness, not because she loves the plan, but because she sees the town organizing itself instead of waiting for an external savior."
    # play sound "sfx_placeholder"  # [Sound: A distant cheer from the workshop — Riv must be canvassing the market already.]
    # play music "music_placeholder"  # [Music: The strings tilt upward; hope thickens like sunlight on water.]
    # [Scene Transition]
    # [Scene: Boardwalk & Reedbeds — Evening Potluck | Dusk]
    hide mayor_amina_bakar
    hide mika_hoshino

    scene bg ch10_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Forks clinking, low laughter, and the soft creak of wet wood beneath feet.]
    # play music "music_placeholder"  # [Music: Warm acoustic guitar with backing hums — communal, intimate.]
    "The potluck feels like a small miracle: neighbors sharing food, stories, and labor. Mrs. Delgado sits at the head with a bowl of something steaming and indestructibly comforting. Riv runs a hands-on demo table where people"
    "can touch a small living section of kelp tethered to a float. Jun mans the repair-station with clamps and goodwill."
    "You move through the crowd, shaking a few hands, accepting a plate, and feeling the cooperative tumble into real, messy life. People argue about distribution ratios over bread and then laugh and pass it anyway. It's noisy and practical and alive."
    "Riv: (to a young couple) 'You take two shares. You can help with nights, and we'll show you how to dry it. It's tasty, and it's a wage.'"

    "Young resident" "Will it actually pay? I can't do three unpaid shifts a week."
    show mika_hoshino at left:
        zoom 0.7

    mika_hoshino "We tracked hours and assigned a basic compensation model. If you work harvest nights, you get a share plus small pay. We won’t make anyone do unpaid labor."
    show jun_park at right:
        zoom 0.7

    jun_park "And we set a cap so it never spirals into exploitation. You’ll know your hours in advance."
    "The conversation is clumsy but earnest. The cooperative isn't tidy yet — bylaws are being argued over bowls of stew — but it's yours in the most authentic way."

    menu:
        "Offer to lead the first accounting session":
            "You say it quietly and people glance at you with grateful surprise, relief like rain in parched soil; Jun pats your shoulder like a benediction."
        "Suggest a rotating potluck schedule so everyone shares hosting":
            "Riv snaps his fingers delightedly and the chatter swells into practical maps of who can host and when; neighbors scribble names on a shared list."

    # --- merge ---
    "Elias Maren sets up a small projector and shows photographs of healthy kelp beds, scaled-up models of shared floats, and a damp-eyed diagram of how nutrient cycles will stabilize local fisheries."
    "Elias Maren sets up a small projector and shows photographs of healthy kelp beds, scaled-up models of shared floats, and a damp-eyed diagram of how nutrient cycles will stabilize local fisheries."
    show elias_maren at center:
        zoom 0.7

    elias_maren "This isn't a fix-all, but kelp improves water quality, sequesters carbon, and returns a measurable yield. We can train everyone to monitor and maintain. Then the community decides how to distribute."
    "An older fisherman rests his chin in his hand and watches the images, and for the first time tonight you see him nod. That tiny head-bob holds more weight than any grant application."
    # [Scene Transition]
    # [Scene: Workshop — Late Night, After the Potluck]
    hide mika_hoshino
    hide jun_park
    hide elias_maren

    scene bg ch10_453e40_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low hum of late conversation fading, a clock tick audible in the hush.]
    # play music "music_placeholder"  # [Music: Piano and strings hold a soft, steady cadence — like breath after exertion.]
    "The hours after the potluck are where the cooperative's nervous system is soldered into something practical: signatures, decentralized keys for storage lockers, a simple code of conduct. You run your finger beneath the column that will list hours, and beneath it, the promise of payment."
    "Riv bursts back in, cheeks flushed, hands waving a sheaf of papers that look official because they are."
    show ravi_riv_delgado at left:
        zoom 0.7

    ravi_riv_delgado "We did it. Small grant approved — community micro-grant. It's not a mountain, but it's seed money. We can buy floats, nets, and a weatherproof lockbox for the ledger."
    "You feel your breath catch, a quick, light surge of disbelief that blooms into fierce gratitude. The town leaned in and the world leaned with it, just a little."
    show jun_park at right:
        zoom 0.7

    jun_park "We've got suppliers who'll give us a discount if we pay upfront. I can stretch the materials. We'll schedule the first build night next weekend."
    "A few people clap softly, not theater but sincere. Elias Maren leans against a bench, his smile small and private, as if he is trying not to look triumphant because triumph here is shared."
    show elias_maren at center:
        zoom 0.7

    elias_maren "We schedule the training, the harvest windows, and the public reporting. I'll draft a monitoring protocol for the first three months."
    hide ravi_riv_delgado
    show mika_hoshino at left:
        zoom 0.7

    mika_hoshino "I'll make the ledger public and set up a watch rotation. No one person carries all of it."
    "You look at the names now penned across the founding minutes — a mix of familiar faces and newer ones who had been skeptical an hour before. There is something luminous in seeing it recorded: proof the town can act."
    "Outside, near the docks, a faint low fog begins to roll in like tidewater seeking to reclaim the shore. You do not feel afraid. You feel a steady, rising current under your feet — the town pulling itself up."
    "Soren Voss's presence remains minimal: a brief text that arrived earlier, formal and distant, congratulating 'community initiative' but offering no involvement. You tuck the message away like a page of a closed book; his choice to"
    "stay removed is its own statement. For tonight, that absence doesn't hollow the victory. It frames it."
    # play music "music_placeholder"  # [Music: The strings rise, warmer and brighter.]
    "You fold the newly stamped ledger and place it into the dented metal box that once held your mother's spare screws. Your hands no longer tremble from the earlier mixture of duty and fear; they are"
    "steady with a new muscle: the capacity to convene and the willingness to be convened."
    "You allow yourself a small, private smile."

    mika_hoshino "We did the first thing — we built a thing together."
    # [Page-Turn Thought: The grant is modest, the floats are hand-stitched, and the harvest is months away. But already there is a schedule, a shared ledger, and the first community-owned harvest lined on the calendar. The cooperative will be messy, human, and imperfect — and precisely for that reason, it may last. You stand at the threshold of a new kind of life: less solitary, more multiplied by hands you trust. Dawn will bring building; tonight brings a kind of fragile, expanding hope. You close the metal box and feel its weight—the weight of commitment—and step outside to listen to the harbor breathe.]
    hide jun_park
    hide elias_maren
    hide mika_hoshino

    scene bg ch10_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter11
    return
