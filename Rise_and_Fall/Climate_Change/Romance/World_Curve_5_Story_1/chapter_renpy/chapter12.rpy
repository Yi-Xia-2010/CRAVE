label chapter12:

    # [Scene: Civic Rooftop Garden | Dusk]

    scene bg ch10_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: A low cello line underpins the air, minor keys; a distant gull cuts through the sound]
    # play sound "sfx_placeholder"  # [Sound: Salt-roughened paper, the soft murmur of the crowd, shoes on damp wood]
    "You step forward to the podium with the pilot proposal folded in your hands like something both fragile and necessary. The words have been argued and reworded, annotated in the margins with Linh’s saltwater tolerance values"
    "and Maya’s sketchy flourishes. You remember the rooftop breathing in and out behind you — the collective hold, the small sound of a town deciding."
    show aria_marin at left:
        zoom 0.7

    aria_marin "We propose a controlled pilot — living shorelines in Pilot Bay, a lowered berm on the southern curve, and a community land trust to protect households at highest risk. Small scale. Transparent metrics. Community-managed."
    "The crowd answers with a mixture of nods and held breaths. Someone coughs. A child tugs at a sleeve. Your voice feels like the last plank on a creaking walkway: supporting, but under pressure."
    show kai_solano at right:
        zoom 0.7

    kai_solano "You said 'compromise' earlier. Is that what this is? Half measures while they buy time to build a wall where it matters to them?"

    aria_marin "It's a test. We can learn—fast—what works here without giving away control of people's land. This pilot buys us data and time."

    kai_solano "And if the data says 'not enough'? What then, Aria? Will you fold and call it evidence for the wall?"
    "You sense the room tighten; his accusation is not only of policy but of you — of perceived alliances, of old mistakes you haven't been forgiven for. The old habit of tightening your jaw rises, but you lower it. Your hands trace the compass at your throat."
    show noah_vega at center:
        zoom 0.7

    noah_vega "If the pilot demonstrates scalability and protects the most vulnerable, my firm will consider conditional investment in the next phase.' (a pause) 'We need metrics; we need outcomes. We can scale what we know works."

    "Kai Solano (barks a laugh that isn't funny)" "You hear that? 'Conditional.' As if people's lives are a line item."
    hide aria_marin
    show maya_marin at left:
        zoom 0.7

    maya_marin "It isn't about lines. It's about the smell of the marsh in summer and the place by the pier where I learned to wade. Compromise doesn't mean surrender — it can mean saving both."
    hide kai_solano
    show dr_linh_pham at right:
        zoom 0.7

    dr_linh_pham "We must be explicit about sampling windows and error bars. Tidal variance in the bay this season is off the models by up to fifteen percent. If you're expecting seedlings to tolerate X salinity and we get X plus fifteen, we need contingencies."
    hide noah_vega
    show aria_marin at center:
        zoom 0.7

    aria_marin "Then we build the contingencies into the memorandum. Clear thresholds for success and failure. If we fail, we pivot together — not unilaterally."
    "There is a long, wet pause. The fog presses the town's faces close. After a moment, people step forward, names are offered, hands clasp the corners of the draft. You watch as signatures ribbon across the"
    "page — ink beading small and dark on damp paper. When Noah Vega signs, his nod is thin and technical, not trust. When Kai Solano signs, his jaw works like someone swallowing something bitter. Maya's fingers"
    "are smudged with paint; when she signs, she grins, helpless and fierce."
    hide maya_marin
    hide dr_linh_pham
    hide aria_marin

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The scratch of pens, a small cheer from the fringe of the crowd]
    show aria_marin at left:
        zoom 0.7

    aria_marin "This is a start."
    show elder_tomas_quay at right:
        zoom 0.7

    elder_tomas_quay "Starts are what we have. Remember the old docks? They began with planks and the patience of those who knew how to mend."
    "The rooftop disperses in a rain of earnest nods and whispered disputes. Hope feels like honest, unglamorous work — the right kind, but not an easy kind."

    menu:
        "Stay to field volunteers' questions":
            "You remain on the rooftop, walking the corkboard of plans, answering where the volunteers need direction. Hands reach for you; you point to the timeline and the first field day. The town leans in and the plan grows heavier on your shoulders."
        "Walk down to Pilot Bay with Kai and Maya":
            "You step off the roof toward the east stair with Kai and Maya at your heels. The fog opens into the sound of surf and the taste of iron on your tongue; being on the ground makes decisions feel urgent and real."

    # --- merge ---
    "The scene continues."
    # [Scene: Tidal Conservatory | Morning — Three Days Later]
    hide aria_marin
    hide elder_tomas_quay

    scene bg ch10_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: High, anxious strings; a low synth underscore]
    # play sound "sfx_placeholder"  # [Sound: Water dripping, a distant generator hum, the clink of lab tools]
    "You watch volunteers unload crates of seedlings — marsh grass, saltwort, eelgrass — and the first little motes of panic begin at the edges. Someone pulled a label wrong at the nursery; a batch marked for"
    "low salinity is better suited for brackish pools. Hands that wanted to help now handle the wrong plants."
    show dr_linh_pham at left:
        zoom 0.7

    dr_linh_pham "Tell me you labeled provenance and salinity tests."

    "Volunteer" "We... we used the last crate we had. We thought—"

    dr_linh_pham "We thought wrong. We can sort, but the tide window is shrinking."
    "You kneel to a tray, fingers numb in the cool humidity. The leaves are fine, pale green, but you know plants don't forgive improvisation the way people sometimes do."
    show aria_marin at right:
        zoom 0.7

    aria_marin "Okay. We triage. Move the most sensitive trays into elevated flats. Keep the hardier ones low. Kai, can you marshal people for the sorting line?"
    show kai_solano at center:
        zoom 0.7

    kai_solano "Yeah. We'll do it. But we need to secure the southern curve too — the berm materials are late."

    aria_marin "Noah Vega's contractors promised a delivery by tomorrow morning."

    "Kai Solano (looks at Noah's number on your phone; hard)" "He promised a lot of things."
    hide dr_linh_pham
    show noah_vega at left:
        zoom 0.7

    noah_vega "We have pumps and geotextile rolls. We can reinforce the footing tonight, but I need election of who will coordinate with my crews. We can't be ad hoc forever."
    hide aria_marin
    show dr_linh_pham at right:
        zoom 0.7

    dr_linh_pham "And the models?"
    hide kai_solano
    show aria_marin at center:
        zoom 0.7

    aria_marin "Can be retuned. We'll run new scenarios against these species' tolerances. Dr. Linh?"

    dr_linh_pham "I'll calibrate overnight. If the tide runs higher than expected again, the survival function changes non-linearly."

    aria_marin "Non-linear. The word lands like a stone. You are good with maps and schedules, with systems that bend the way you tell them. Nature, when it misbehaves, does not wait for your plans."

    menu:
        "Authorize Noah's crew to take charge of the berm this evening":
            "You sign off. Noah's team moves with engineered efficiency; the berm looks professional, but Kai's jaw tightens — a message to the activists that the firm is running the show."
        "Keep community crews in control and ask Noah to lend equipment only":
            "You set the community crews as lead and accept the firm's tools. The work is messier, slower, but it keeps agency local. Noah watches, expression unreadable."

    # --- merge ---
    "The scene continues."
    # [Scene: Pilot Bay | Night — One Week Into Implementation]
    hide noah_vega
    hide dr_linh_pham
    hide aria_marin

    scene bg ch10_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano notes with a underside of distant thunder; the mood is taut and sinking]
    # play sound "sfx_placeholder"  # [Sound: The roar of waves, a steady rain on tarps, strained voices, the slap of water against hurried boots]
    "You wake before dawn to the thud of incoming tides and a new alarm on your tablet. Linh's overnight calibration flagged a new variable: an unpredicted storm surge combined with an offshore current shift. Predicted high tide — the one you planned around — is now a foot higher."
    "You run across the mud with a dozen others, the taste of salt in your teeth, neon on your cheeks. The berm's lower curve shudders as the water eats at its base. Your planted rows sit"
    "in shallow, brackish pools where they cannot yet establish roots. Then, as the night deepens, the low beds go under."
    show dr_linh_pham at left:
        zoom 0.7

    dr_linh_pham "These seedlings are drowning in saline beyond their tolerance. We can still save some—if we get them into higher flats within the hour."
    show kai_solano at right:
        zoom 0.7

    kai_solano "We need pumps. Noah Vega, where are the pumps you promised?"
    show noah_vega at center:
        zoom 0.7

    noah_vega "They're here. We deployed two. We can run dewatering and get temporary baffles up. But if the site design is failing at this magnitude, we need to scale the berm now."

    kai_solano "Scale it now and you erase the marsh. You make it a concrete cap. It isn't a compromise; it's a takeover."

    noah_vega "If we don't stabilize the site, we lose everything. You want preservation? We preserve what is left."
    "You watch them trade words like blows. Your perfectionism organizes scenarios in your head: contingency A, B, C, each one a thin corridor toward capitulation or survival. You think of the volunteers who showed up in"
    "rain boots and borrowed gloves, of Maya's mural sketches, of the signatures on your damp memorandum."
    hide dr_linh_pham
    show aria_marin at left:
        zoom 0.7

    aria_marin "We stabilize the beds without erasing the marsh. We use pumps to buy time, temporary raised flats for transplants, and we re-evaluate the berm's slope to hold against the new tidal info. We do the least-damaging fix that buys us a second season."

    kai_solano "Will that be enough?"

    aria_marin "Will it be enough? Every clause you craft, every exception you grant, feels like a rope bridge over a deepening tide. Fail, and the activists will see you as naïve. Fail, and Noah’s firm will call the whole thing untenable and withdraw support. Fail, and you will watch neighborhoods become negotiation chips."
    hide kai_solano
    show dr_linh_pham at right:
        zoom 0.7

    dr_linh_pham "If we act now, we have maybe a thirty to forty percent recovery for this planting. Not ideal. But volunteers can raise at least half into higher flats tonight."
    "A volunteer — a woman with paint-splattered sleeves — meets your eyes and says, simply, 'We came because you asked us. We'll do whatever.'"
    "You [time stretches]: You feel the town's expectation like a weight in your ribs. You are good at maps; you are less good at the ragged improvisation that grief and weather force. Your hands ache from hauling sandbags. Your jaw hurts from clenching."
    hide noah_vega
    show kai_solano at center:
        zoom 0.7

    kai_solano "If this goes under, people will say we sold out. They'll say you sold out."
    hide aria_marin
    show noah_vega at left:
        zoom 0.7

    noah_vega "If this goes under, no one wins. We should do the pumps and the flats. Then measure. Then decide."

    dr_linh_pham "We need a single call now. Who coordinates the on-site operations? Who signs off on the pump deployment, on the transplants? The town needs a chain of command."
    "You stand in the rain, the salt on your face an accusation and a benediction. Rainwater gathers in the hollow of your palm; it is cool and real."
    "Your perfectionism scrapes against a harder fact: this compromise is not a polished ceremony. It is hideous, hands-on labor in the dark. Its success will be messy, partial, and dependent on people who do not always agree."
    "You look at the muddied seedlings, at the volunteers with tea-stained hands, at Kai Solano's clenched fists, at Noah Vega's pragmatic stance, and feel the full, small city settle onto your shoulders."
    hide dr_linh_pham
    hide kai_solano
    hide noah_vega

    scene bg ch10_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: A single low violin note holds and then thins to near silence]
    # play sound "sfx_placeholder"  # [Sound: Waves drowning the world for a moment; a distant siren that becomes the town's pulse]
    "You have one moment before the tide speaks again."
    "You can hear the future in the surge: a choice that is not moral theater but material — pumps, flats, more compromise, or abandonment. You know what every path will cost. Your ring is cold and"
    "heavy against your palm. The memorandum at the bottom of your satchel feels like a promise written on tidewater. The fog bites your cheeks. You inhale salt and decision and the smell of wet earth. Whatever"
    "you choose will echo across seasons."

    scene bg ch10_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter13
    return
