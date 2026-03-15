label chapter4:

    # [Scene: Saltwren Commons | Morning — Two Days After the Council Vote]

    scene bg ch4_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Brisk, hopeful strings with a rising tempo]
    # play sound "sfx_placeholder"  # [Sound: Hammers, chatter, the steady slap of tide against pilings; camera shutters in the distance]
    "You arrive to the Commons on the wings of momentum. Word traveled faster than you expected: the hybrid pilot you and Elias pushed through the chamber is no longer a meeting-room abstraction. It's a line of"
    "flagged stakes along the promenade, a stack of coir mats, and the low, purposeful hum of people who finally feel like they're doing something that might matter."
    "The air is sharp with brine and turned soil; compost heat fogs in small wafts when a volunteer lifts a crate. Rae is already mid-chant — not angry, this time, but breathless with possibility — while"
    "Tommy passes out thermoses and jokes about you stealing his best spade. Your hands still smell faintly of tea; your chest hums with a quick, bright nervousness. This is work, and it matters."
    "Elias Navarro threads through the clusters of volunteers like someone who has practiced being unflappable. He lifts a clipboard with one hand and steadies a wayward survey flag with the other. He sees you and his"
    "face opens — a relief like sunlight breaking a cloud. When he reaches you, his voice leans into you, quick and steady."
    show elias_navarro at left:
        zoom 0.7

    elias_navarro "They set the markers exactly where Dr. Bhatt recommended for sediment capture. The tide schedule lines up for tomorrow's planting window if we move volunteers an hour earlier."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Good. Volunteers are already signing in. Rae organized extra gloves. How's the sensor array coming along?"

    elias_navarro "Amina's team finished calibration last night. We'll stream the first data back to Tidewatch as soon as the first mats settle. If the salinity readouts match the model, we get a very tidy justification for the living inserts."
    "You swallow the technical language and let it rest against the thing you feel: the small heat of being part of something that both stitches the coastline and stitches people together. Your words come softer."

    mara_lin "And the messaging? We need to be careful — make it clear this is community-first."

    elias_navarro "We frame it as co-design. I can handle the press line. You do the heart-side story — the lived stuff. Between us, we keep the language anchored."
    "You both look toward the edge of the Commons where a line of press vans glints in the sun. A cluster of residents lingers there — some curious, some wary. Celeste Park stands a little apart,"
    "as immaculate as ever against the muddied boards: trench coat, portfolio, a watchful expression that is, for lack of a better word, complex. She claps when a volunteer drives a stake in true to ceremony, and"
    "the clap doesn't tell you everything about what she might do next."

    menu:
        "Walk over and invite Celeste to observe the planting":
            "You step forward, palms open, and call to her. She approaches with a measured smile; something unreadable passes across her features — respect or calculation — and she accepts a pair of work gloves with a nod. The cameras tilt; the story looks more like compromise."
        "Ignore Celeste and focus on the volunteers":
            "You keep your attention on the volunteers. Celeste watches from the edge, folding her arms, the posture writing on the air 'I'll deal with this later.' The cameras still catch her silhouette — the photograph gains tension."

    # --- merge ---
    "Scene continues regardless of choice."
    "Rae bounds up, cheeks flushed, a stencil bag slung over her shoulder. She gives you a grin that is toothy and honest."
    show rae_carter at center:
        zoom 0.7

    rae_carter "We painted a sign. 'Living Edge — Planting Day.' It's loud because people have short attention spans and loud signs cut through."

    mara_lin "Perfect. Put it by the boardwalk entrance. Make sure it's readable in drone shots."

    rae_carter "Drone shots. We're official."
    "Tommy sidles up with a bundle of jute mats under his arm, the smell of seaweed and diesel clinging to his coat."
    hide elias_navarro
    show tomas_tommy_reyes at left:
        zoom 0.7

    tomas_tommy_reyes "If the promenade holds half what you say it'll hold, my nets won't be the only thing saved come storm season.' (he pats your shoulder) 'But don't go soft on ’em — money makes people talk differently."

    mara_lin "We won't. This pilot is proof. We need payoffs that are real for fishers, for homeowners, for kids who play here."

    tomas_tommy_reyes "Good. Because if this all becomes a glossy walkway for visitors, you're not the one hauling fish out of flooded nets."
    "The exchange leaves a raw edge in the air — practical stakes, livelihoods at the heart of the rhetoric. You feel the thrill of urgency: this pilot must prove itself quickly, and everyone knows it."
    # [Scene: Promenade Pilot Site | Midday]
    hide mara_lin
    hide rae_carter
    hide tomas_tommy_reyes

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The louder buzz of a small excavator, shouted coordination, a distant gull; the sea sounds bigger here]
    "You and Elias stand on a temporary boardwalk, the pilot's layout a ribbon of possibility: a hybrid of engineered terraces and planted marsh pockets — living marsh inserts grafted into a narrow promenade segment. Engineers measure"
    "angles while hands sink into mud. Dr. Amina Bhatt barks numbers into a tablet and then softens when she sees Elias."
    show dr_amina_bhatt at left:
        zoom 0.7

    dr_amina_bhatt "The first sediment baselines are within expected variance. If we maintain planting density at the edge and stagger the mats, we can double retention for the next swell season."
    show elias_navarro at right:
        zoom 0.7

    elias_navarro "We can also phase the inserts so they don't disrupt local traffic on the promenade. Minimal compromise, maximal ecological function."
    show mara_lin at center:
        zoom 0.7

    mara_lin "And community participation?"

    dr_amina_bhatt "Already scheduled. Your workshops were in the report."

    elias_navarro "You were right to run those. The data are more persuasive when they come paired with lived narratives."

    mara_lin "Someone needs to keep human stories on the table."
    "A camera crew edges closer; an on-air reporter rehearses questions. Celeste Park stands a little further off — she watches the machinery, watches the volunteers, sometimes checking her watch. When she moves, it's toward a group of local business owners clustered near a temporary fence."
    hide dr_amina_bhatt
    show celeste_park at left:
        zoom 0.7

    celeste_park "Pilot looks promising. Thoughtful staging."

    mara_lin "We're trying something that doesn't erase the shoreline's functions. We're testing a shared model."

    celeste_park "I'm glad to see collaboration. I believe the town will need investment at scale.' Her smile is efficient. 'If the pilot works, Solhaven will be more marketable. Investors like certainty."
    "There is a weight behind her words you cannot ignore — funding is the oxygen of bigger projects. You keep your voice even."

    mara_lin "We don't want money at the cost of local control."

    celeste_park "Control and vision can coexist. They need someone to steward resources and someone to steward place. The town deserves both."
    "Her answer is polished; you cannot tell whether it's a bridge or a trap. The ambiguity sits like salt on your tongue."

    menu:
        "Press Celeste on what 'steward resources' means":
            "You press, and Celeste's smile narrows just slightly. She opens her portfolio and slides a schematic across a folding table — careful, tidy, full of clauses. The cameras zoom in. Her language turns legal and attractive."
        "Deflect and turn back to volunteers":
            "You deflect with a laugh and hand a shovel to a tired volunteer. Celeste watches, inscrutable. The moment keeps the pilot's momentum but leaves the financial question hanging."

    # --- merge ---
    "Scene continues regardless of choice."
    "Dr. Amina Bhatt moves between you and Celeste with the brisk authority of someone who spends equal time translating data and soothing egos."
    hide elias_navarro
    show dr_amina_bhatt at right:
        zoom 0.7

    dr_amina_bhatt "Let's not let funding chatter overshadow today's metrics. We have a tidal window. The living inserts need planting now if we want them to root before the next full cycle."
    hide mara_lin
    show elias_navarro at center:
        zoom 0.7

    elias_navarro "I'll handle the press debrief. Would you lead the planting orientation for the volunteers?"
    hide celeste_park
    show mara_lin at left:
        zoom 0.7

    mara_lin "Give me twenty. I'll run through the planting order, check cuttings, and make sure the kids from the afterschool group know where to stand."

    elias_navarro "Perfect. Meet me at the Tidewatch upload station in three hours? We can review the first-hour stream together."

    mara_lin "See you there."
    "Your stride back toward the volunteers is quick; your pulse matches the tempo of the day. The pilot is kinetic, and you are at the center of the motion. You tell people where to press their"
    "hands into the coir, how to angle the plugs so the salt-tolerant sedge will catch the next high. A child asks why the mud smells like rotten seaweed; you bend and show them the tiny crustaceans"
    "and the hope that they're part of a living system."
    # [Scene: Tidewatch Lab | Late Afternoon]
    hide dr_amina_bhatt
    hide elias_navarro
    hide mara_lin

    scene bg ch4_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low electronic beeps, the soft clink of tea cups, the quick breath of a lab fan]
    "The lab is warm from people and machines. Amina leans over the central monitor, the first data feed flicking in: salinity, turbidity, sediment deposition rates. The graphs are not dramatic — they are patient, incremental lines that mean the pilot is doing its job."
    show dr_amina_bhatt at left:
        zoom 0.7

    dr_amina_bhatt "Look at the deposition spike right after the second ebb. The mats captured more fines than the control stretch. That's our win."
    show elias_navarro at right:
        zoom 0.7

    elias_navarro "If that trend holds, we can argue for a phased roll-out, backed by hard data."
    show mara_lin at center:
        zoom 0.7

    mara_lin "How fast can that evidence translate into broader funding and permits?"

    dr_amina_bhatt "Fast enough if we package it with the social metrics — volunteer hours, local testimonials. Funders respond to stories that are scalably framed."

    elias_navarro "And scalable doesn't have to mean centralizing control. We can build governance into the design."

    mara_lin "Governance often gets lost in legalese."

    elias_navarro "Then we write governance into the pilot's governance: community stewards, shared maintenance schedules, transparent reporting. We make it inconvenient for anyone to turn it into corporate-only property."
    "You let yourself imagine the lattice of people who might actually care for living marsh inserts. Your chest loosens at the thought of that coalition. There's a quick, private warmth at Elias' attention — not just to the project but to how you shape the project's soul."

    dr_amina_bhatt "I'll start drafting a community data dashboard. If we can show monthly metrics, it reduces the angle of 'uncertainty' that investors use to demand heavy oversight."

    elias_navarro "I'll coordinate with the town to ensure the council sees the next upload first."

    mara_lin "Good. And keep the language plain. People need to read the reports without a glossary."

    elias_navarro "Plain and steady. That's our brand."
    "The lab's window frames the horizon like a painting; the sun is a low coin glinting on the darkening water. There is a sudden, electric influx of messages on Elias' wristband — a coordinated burst of"
    "local coverage and, below that, an official-looking email with a corporate header. Elias reads it, his brow momentarily tightening."

    elias_navarro "Celeste's team is asking for a meeting. They want to talk about scaling."

    mara_lin "Now?"

    elias_navarro "Now."
    "You watch the way his hands curl around the tablet: the weight of being a bridge between measurable science and political maneuvering. You feel a thrill — this is the moment that could expand the pilot"
    "into something that actually protects the town, or unravels under outside influence. The arousal pitches higher; everything happens faster than the lab fan can hum."
    # [Scene: Old Mill Rooftop | Sunset]
    hide dr_amina_bhatt
    hide elias_navarro
    hide mara_lin

    scene bg ch4_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Slow swell of strings tightening into an anticipatory chord]
    # play sound "sfx_placeholder"  # [Sound: Wind pulling at a loose banner; distant murmur of the town below]
    "You and Elias climb the rope ladder to the rooftop as the last light turns the seawater into molten pewter. The rooftop feels private compared to the day's public energy — a small island where talk"
    "can unfurl without a camera tilt. Salt rides your coat; the air smells of rain on hot tile."
    show elias_navarro at left:
        zoom 0.7

    elias_navarro "We did so much today. People arrived. They stayed. Amina's numbers look good."
    show mara_lin at right:
        zoom 0.7

    mara_lin "We did more than I'd hoped. But it's not just about metrics anymore, is it?"

    elias_navarro "No. It's about who gets to decide what 'resilience' means for Solhaven. And it's about whether we do it together."

    mara_lin "You're getting very philosophical for an engineer."

    elias_navarro "Only because you make me. And —' (he hesitates, then continues with careful warmth) '— because I care how you describe it."
    "You look at him. In the lab he is methodical; here, under the wide sky, he is earnest and immediate. The day's adrenaline softens into something warmer and more dangerous: the possibility of you and him not just aligning on projects, but on commitments."

    mara_lin "I don't trust institutions easily. I protect the Commons because it's where grief and memory live. Funding can snip those threads if it isn't careful."

    elias_navarro "I know. And I don't want to be the person who hands you a contract and says 'trust me.' I want us to write the terms together."

    mara_lin "I need to know that when money is on the table, you remember the people who will be watering the plants at midnight."

    elias_navarro "I promise to remember. And if I ever forget, tell me. Make me come back down to the mud."
    "You both laugh — a soft, quick thing that feels like an agreement. He reaches for your hand, fingers warm and certain. It's a small, concrete thing that makes the day's abstract commitments feel human-sized."

    elias_navarro "So — what's next? We have momentum. We can scale, but there are choices. We can bring Celeste in and secure funding quickly; we can keep expanding community-led; or we can push for faster construction to outpace political friction. Each path has trade-offs."
    "You feel the rush of options like tidewater tugging at a channel: each current tempting, each capable of carrying you somewhere new. The rooftop hums with the ache of decision: there are lives on both sides of any choice, and that's what makes it sacred."
    "The arousal crescendos — reporters will spin outcomes, Celeste will sharpen her offers, the town will watch. Your chest is hot with the sense that this decision will map not only the promenade's future but the shape of your partnership with Elias."
    "You inhale the salt-tinged air and let the horizon steady you. The pilot's early success has opened the doorway; the corridor beyond is lit but forked."
    # play music "music_placeholder"  # [Music: String section reaches a high, sustained note — bright, urgent]
    hide elias_navarro
    hide mara_lin

    scene bg ch4_453e40_5 at full_bg
    "You realize this is the hinge. The field you fought to protect needs more than experiments; it needs a strategy that matches your values or a willingness to accept compromises that will change the shape of"
    "the Commons. You feel hopeful and accelerated — a positive surge of energy and possibility — but you also feel the gravity of the choice. This is the highest point of the day: the moment everything"
    "pivots."

    menu:
        "Negotiate a scaled agreement with Celeste to secure funding":
            jump chapter5
        "Keep expansion community-led and refuse corporate strings":
            jump chapter6
        "Push for immediate construction to outpace political moves":
            jump chapter6
    return
