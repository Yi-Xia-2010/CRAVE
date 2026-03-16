label chapter11:

    # [Scene: Salted Rooftop Garden | Early Morning]

    scene bg ch11_e67f19_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low gull calls, the distant clank of a mooring line, a phone buzz from your jacket pocket.]
    # play music "music_placeholder"  # [Music: Sparse, descending strings—slow and taut]
    "You pull the phone from your jacket. The secure message glows: a cropped photo of a wooden crate spilled open on a cold dock, brackets of metal and small piles of bolts scattered across wet planks."
    "No sender name—just a municipal header you don’t recognize and a short line of text that reads like a warning and a dare. Your stomach drops into the same space your father's boat used when the"
    "keel first bit a wave."
    "You taste the salt in the air and the sharpness of betrayal. The rooftop smells of damp earth and cut leaves; the greenhouse is a pocket of green light above a city that feels increasingly brittle."
    "Elias Navin is already there, leaning on a reclaimed bench, sensor band flickering a faint green. His face is paper-pale with sleep or something close to it, but his hands move with the quiet certainty of"
    "someone who measures time in data points."
    show elias_navin at left:
        zoom 0.7

    elias_navin "You got the message."
    "He doesn't ask who sent it; he knows you did."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "Someone opened our crates. Bolts scattered, sensors missing, manifests altered."
    "Your voice is small next to the greenhouse glass, but it carries the weight it must."

    elias_navin "We lost telemetry from two of the northern pylons last night. Logs were scrubbed. Whoever did this knew where to cut power to the back-ups."
    "He closes his eyes for a beat."
    "You let the words sit between you—salt, glass, and the ghost of someone’s gloved hand. There is a rhythm to your thinking: identify, protect, salvage. You are the ledger; you are supposed to keep the account straight. But the ledger is damp and the ink runs."
    "Theo arrives on the run, hair damp, a solar pack clinking with tools. He drops a small weatherproof case on the table and opens it—inside, a tangle of ground-up plastic and a single rusted bolt with a peculiar notch."
    show theo_mendes at center:
        zoom 0.7

    theo_mendes "Found this at Site Three. Patterning on the edge like a handheld pry. Whoever did it didn't have time to bring a toolbox—just wanted chaos."
    "He grins, half-joke, but his eyes are tight."
    "You trace the bolt with a thumb, feeling the irregular cut like a bruise. Objects become evidence and symbols at once; you do not want to let symbol alone rule you, but every broken bolt is also a risk to someone who will trust the structure to hold."

    menu:
        "Examine the photo closely on your phone":
            "You zoom in, fingers trembling, and notice a faded stencil on the crate slat—three narrow stripes, half-worn away; the detail is small but feels deliberate."
        "Call the dock volunteer immediately":
            "Your voice is steady when you call; on the other end, someone swears and says they saw a van slip away into fog. It isn't much. It is something."

    # --- merge ---
    "You breathe in greenhouse air, taste compost and salt. The choices narrow like a tide drawing out: show your hand now, or keep it close and gather the facts."
    # [Scene: Hybrid Project Site — Northern Pylon | Midday]
    hide elias_navin
    hide mara_kestrel
    hide theo_mendes

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The thud of boots in mud, the hiss of a small pump, a distant council chopper hum.]
    # play music "music_placeholder"  # [Music: Low, insistent percussion—an anxious heartbeat]
    "You climb down the muddy path beside the pylon. The living reef modules sit askew; bolts missing where they should have cinched the engineered frames to the base. Where sensors should pulse green, there is dead"
    "glass and wiped LED readouts. The smell of algae and torn rope fills your nose. At the edge of a puddle, a smear of oil traces the outline of a gloved hand."
    "Elias Navin crouches, palms hovering over a seam like a surgeon. He sets down his field notebook, pencils trembling just enough to betray him."
    show elias_navin at left:
        zoom 0.7

    elias_navin "They pulled the strain gauges. Look—there's a splice where the feed should have been. Someone cut the record before the backup could capture the event."
    "He taps the casing with a fingertip, the sound a tiny, accusing knock."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "Do you think this is coordinated?"
    "You hate the way your voice floats—thin, hopeful for denial."

    elias_navin "Patterns match the crate photo. Time stamps align with a city-wide communications blackout. Whoever did this has either municipal access or knows municipal timing."
    show theo_mendes at center:
        zoom 0.7

    theo_mendes "Or someone planted a clever mimic. We need raw hardware—take the casing, the bolt, EVERYTHING. Chain of evidence."
    "He looks at you with an intensity that is almost pleading. 'If we start cataloguing now, we can at least say we tried.'"
    "You feel the old, familiar pull: protect the people who plant mangroves at daybreak, the ones who stand on mud at dusk, the kids whose feet learn the tides before they learn timers. You also feel"
    "the ledger's other demand: make the numbers add up so the council can't ignore theft as random bad luck."

    menu:
        "Bag the bolt and seal the site":
            "You carefully place the bolt in a zip bag and tape it to your journal, a small, reluctant relic—proof preserved."
        "Rush back to the lab with Elias and Theo":
            "You sprint back across the slick planks, the wind cutting at your jacket; the urgency knits you tight and gives your steps a single purpose."

    # --- merge ---
    "You take the bolt and tuck it into your pocket. The small weight steadies you."

    elias_navin "We can run a forensic trace, but we need lab time. Theo can spin up a sandbox to analyze the notch pattern. If it's municipal hardware, the serials will show up. If it's a mimic, we have to think who benefits from failure."
    "He taps the sensor band; it pulses green, then flickers. 'We should also secure the manifests. Chain-of-custody—if they doctored those, the audit won't mean anything unless it's pristine.'"
    "Your jaw tightens. The word 'doctor' tastes like a banned medicine. You picture Jun Park's press-slick posters—rendered cafés, tidy fonts. You picture the Basin, Rosa's shawls, Ivy's paint-splattered overalls. Every image pulls a different corner of your heart."
    # [Scene: The Basin (Community Floodplain Garden) | Late Afternoon]
    hide elias_navin
    hide mara_kestrel
    hide theo_mendes

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Voices overlapping—anger, fear, hushed counsel; a distant gull landing in old rope.]
    # play music "music_placeholder"  # [Music: Minor key piano, slow and patient]
    "You arrive to the Basin and the air is hotter, edged with frustration. Volunteers huddle around coffeepots; hands that once bound mangrove root balls now shake when they speak. Ivy meets you first—soil under her nails,"
    "paint on her knuckles, her mouth set in an expression that could be brave or brittle."
    show ivy_kestrel at left:
        zoom 0.7

    ivy_kestrel "They found this by the compost heap."
    "She holds up a page from a council minute—someone has scribbled over the section about supply chains, an obscene cartoon scrawled across the signatures. 'Who does that, Mara? Who thinks this is a joke?'"
    "Rosa stands by, hands folded, eyes like river pebbles—dark and ancient. She doesn't move quickly, but what she says lands like tide-stones."
    show rosa_alvarez at right:
        zoom 0.7

    rosa_alvarez "People will fear what they do not understand. Fear wants a shape. If we do not give it one, it will find one for us."
    show mara_kestrel at center:
        zoom 0.7

    mara_kestrel "We will secure every deployment. We will catalog everything that’s been tampered with. We will not be made into a spectacle."
    "But even as you say it, you know spectacle is already at the mouth of the harbor—waiting."

    "Volunteer" "We need to call the press. Let them see this. Let them see the sabotage."

    "Volunteer 2" "No. If that happens the funding dries up. They'll pull out and leave us with a scaffold and no teeth."
    "The room fragments into voices that pull like different currents. Your chest tightens; choices form like storm clouds: expose and risk panic, confront and risk a political clampdown, or dig in silently and hope the saboteurs are stopped before more harm is done."
    # [Scene: Tideworks Lab (Makeshift Field Lab) | Early Evening]
    hide ivy_kestrel
    hide rosa_alvarez
    hide mara_kestrel

    scene bg ch11_e67f19_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hum of a generator, the click of a relay, the soft clack of a keyboard.]
    # play music "music_placeholder"  # [Music: A low, descending cello—resigned and stark]
    "You stand too long atop a chair of tension, watching Elias Navin and Theo parse corrupted logs. Theo's fingers fly—command lines and packet captures bloom and then die under his gaze."
    show theo_mendes at left:
        zoom 0.7

    theo_mendes "There's a hollow where the backup snapshots should be. Like someone wiped the mirror and left the original intact. Whoever did this knows our redundancy sequence."
    "He frowns. 'Also—look at this: an unregistered municipal signature injected into the manifest chain.'"
    show elias_navin at right:
        zoom 0.7

    elias_navin "It could be an inside job. It could be a contractor with badge access. It could be a planted frame. We need to be precise about our accusations."
    "He looks at you; for once his calm is cracked by worry."
    "You feel that old guilt—if you'd pushed harder for audited manifests, if you'd insisted on more eyes on the crates, would this have been caught sooner? The spiral of hypotheticals spins and you keep catching yourself on the teeth of what-ifs."
    show mara_kestrel at center:
        zoom 0.7

    mara_kestrel "We can trace the signature. But if it points toward someone in the municipal chain, we blow it wide open. Jun will either close ranks or…something worse."
    "You stop because your mouth runs out of futures to name."

    elias_navin "We can run a discreet trace to see whether the signature is genuine. Theo can spin a honeypot to lure communications. Quiet, contained. If it's municipal, we bring the proof to a neutral auditor."
    "His voice is precise, the edge of something wanting to be said and withheld."

    theo_mendes "Quiet buys us time. It also lets whoever did this think they're winning for longer. If they wanted panic, they'd leak something now."
    "He pinches the bridge of his nose."
    "You close your eyes and see the Beacon—Old Lighthouse—where memory sits like a lamp. You see hands that worked to save a harbor, and you see hands that now move through municipal corridors with different measures"
    "of power. The ledger demands answerability. Your heart demands protection for people who are not numbers."

    menu:
        "Push for a discreet forensic trace with Elias and Theo":
            "Your voice is low and determined; Elias nods with cautious relief, and Theo's shoulders relax. The plan feels measured and alive."
        "Call Jun and demand an immediate audit":
            "You dial Jun and your finger hesitates. The line rings; when he answers, you hear civility with a tautness beneath it. He promises oversight 'if you want it'—the words feel fragile."

    # --- merge ---
    "The lab's amber light feels smaller, as if it could be blown out by a single breath. Outside, the city leans toward something that will change the shape of relationships and livelihoods."
    # [Scene: City Hall Glass Atrium (Council Chamber Lobby) | Night]
    hide theo_mendes
    hide elias_navin
    hide mara_kestrel

    scene bg ch11_e67f19_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Footsteps echo, a distant murmur behind closed doors, the soft click of a keycard.]
    # play music "music_placeholder"  # [Music: Thin, high violin—tense and descending]
    "You walk into the atrium under a banner that promises safety in clean fonts. Jun Park is already there, immaculate coat buttoned against the sea air. He slides from behind a column like someone stepping into a prepared stage-lamp circle."
    show jun_park at left:
        zoom 0.7

    jun_park "Mara."
    "He offers a measured smile."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "Crates opened. Bolts missing. Sensors wiped. Manifests fudged."

    jun_park "I am deeply concerned. We'll open the audit schedule. Increased security for municipal shipments. An independent investigator."
    "He folds his hands a fraction, as if weighing the words."

    mara_kestrel "Who will pay for the increased security? Who will guarantee volunteers aren't criminalized when they ask questions?"

    jun_park "We will cover costs. We cannot allow fear to become a contagion. We must act to shore up trust in the whole system."

    "He pauses, then, softer" "I don't want this to break what we've built."
    "Your chest tightens. The way he says 'we' is both inclusive and authoritative. You feel the monstrous tug of two pulls: the urgent need to protect your neighbors from the immediate physical danger of loose bolts"
    "and torn frames, and the equal need to protect them from being steamrolled by a municipal machine that might trade neighborhoods for downtown survival."

    jun_park "Mara, I know you. I know this town. If you go public—if you confront without proof—you give ammunition to those who want to see chaos. Open them up at the wrong time and funding will dry up; people will leave. I can't let that happen."

    mara_kestrel "And if you cover things up?"
    "The words are a stone thrown into still water; ripples spread. 'If you frame this as local mismanagement, volunteers will be blamed. People will be hurt.'"

    jun_park "I can't promise you all answers today. But I'm offering transparency—oversight, auditor access. Let us work together to trace this. Public spectacle won't help."
    "His eyes are steady. You know enough not to read them as confession. You know enough to know you can't afford to be naïve. Every choice is a hazard."
    "Rosa's counsel repeats in your head: fear will find a shape. If you do not name it, others will. Ivy's paint-smudged hands remind you of the smallest residents who cannot be traded like chips in a municipal ledger."
    "You press your palm into your journal in your pocket. Damp paper, compass warm against skin. The city seems to hold its breath."
    "You have a decision to make that will set the next tide: press for immediate public confrontation, bury the fight in quiet investigation, or fling the doors to the press and force the city's hand."
    "The room feels colder. The weight of possible harm presses down like a low cloud. Your throat is tight; your choices are all risk."
    # play music "music_placeholder"  # [Music: A single dissonant chord held; then silence]

    menu:
        "Confront Jun publicly and demand accountability.":
            jump chapter12
        "Investigate quietly with Elias and Theo.":
            jump chapter15
        "Open meetings to press to expose sabotage.":
            jump chapter12
    return
