label chapter11:

    # [Scene: Pilot Site (Instrumentation on Beach) | Morning — overcast, wind sharpening]

    scene bg ch10_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Waves talking soft and close; the bleat of a gull; the beep of a logger syncing]
    # play music "music_placeholder"  # [Music: Quickening strings with a bright undertow — urgency braided with possibility]
    "Alea Maren breath the morning in like a promise. The salt bites at the back of your throat; wind threads through the hem of your jacket. The pilot is real under your hands — a small"
    "army of instruments, a few borrowed grad students, and the steady signature of Dr. Lian Cho arranging clipboards with surgical care. You can feel the acceptance of the time-limited engineering pilot like a hinge closing: it"
    "gives you access, accountability, and a clock."
    show dr_lian_cho at left:
        zoom 0.7

    dr_lian_cho "Sensors check. Power is stable. GPS lock acquired. Alea, the loggers are set to sample at five-second intervals for the first tidal cycle, then we'll bin to minute-averages for analysis."
    show alea_maren at right:
        zoom 0.7

    alea_maren "Good. Make sure we flag the battery cycles in the metadata — last thing we need is a false drift."

    dr_lian_cho "And I'm co-signing the monitoring protocol. Public notes approved. We can push the first packet to the funder's dashboard after QA this afternoon."
    show tomas_reyes at center:
        zoom 0.7

    tomas_reyes "When do the volunteers start the shoreline watches? Rin said they'd be here late, but they were itching to set schedules."

    alea_maren "Two-hour blocks, twice a day — dawn and dusk. We pair each volunteer with a sensor id so observations can be compared directly. And we'll train them to note the same covariates: wind, fetch, any litter, and human activity."

    dr_lian_cho "Also — Alea. When you describe the instrumentation, don't hide the uncertainties. The board will want clean answers, but the community deserves the full picture."
    "Alea Maren feel a quick, private laugh in your throat — both at the tiny arrogance of wanting perfect models and at yourself for buying into the armor of numbers. The pilot is discipline, but it"
    "is also permission: permission to be rigorous, permission to make the argument in provable sentences."

    menu:
        "Explain the sensors with a metaphor — 'think of them as seafloor stethoscopes'":
            "You lean forward, hands shaping the air into a chest; the volunteers chuckle and tilt their heads like dogs hearing an old song, and their faces relax into curiosity."
        "Stick to the numbers — stress sampling rates and QA steps":
            "You outline the sampling schema, and several volunteers nod with professional gravity; a few eyes glaze for a beat, then sharpen when you mention how their notes will be compared to instrument data."

    # --- merge ---
    "The scene continues."
    # [Scene: Lab (Wave-Tank Room) | Midday — fluorescent light humming]
    hide dr_lian_cho
    hide alea_maren
    hide tomas_reyes

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The pump's low thrum; the click of a recorder; the muffled scrape of shoes on concrete]
    # play music "music_placeholder"  # [Music: Percussive rhythm; the strings move into a hopeful, brisk motif]
    "Alea Maren direct the wave-tank run like a conductor. Scaled geometry on a palette of sand and glue — a concrete segment in the center, marsh-sediment mats arranged along an adjacent shore profile — and the"
    "machine coughs and begins. You watch the model's water bow against the engineered block, and something honest and electric opens in you: here, in miniature, are the arguments you have been rehearsing in abstracts and meetings."
    show dr_lian_cho at left:
        zoom 0.7

    dr_lian_cho "Run the higher-energy scenario. We need to see edge amplification."
    show alea_maren at right:
        zoom 0.7

    alea_maren "Increase the fetch. Add a short-runup of wind shear. Record the pressure transients at the seam."
    "The model answers. Water crests, slams, and the seam — where engineered meets soft — bows in quick, ugly arcs. Sensors pick up spikes. The engineered segment reduces overt surge behind it, but reads like a"
    "choke point: pressure concentrated at the ends, pulses that would, in real life, gouge into unarmored shorelines. The living mats absorb subtle energy, their blades bending and siphoning small increments of momentum, but their reduction is"
    "patient and incremental — meaningful over many cycles, not in a single event."
    "Rin Sato leans against the doorway, arms folded around a thermos like a casual banner. Their smile is half amusement, half genuine hunger for the show."
    show rin_sato at center:
        zoom 0.7

    rin_sato "Professor Harbor, you know how to make tiny oceans dramatic."

    alea_maren "Only on borrowed physics."

    rin_sato "So, what is your verdict? Concrete is a bully that keeps the town's toes dry but kicks the pavement down the road? Marsh is the slow-cooking stew?"
    "Alea Maren and Dr. Lian trade a look — she precise, you careful — and then you both start talking, layered and overlapping: the numbers, the implications, the timescales. Rin interrupts occasionally with a practical question"
    "— can volunteers help grow enough marsh to test scale? — and your replies are rapid, tidal: yes, if we seed nursery beds; yes, if we couple with managed retreat in vulnerable strips; yes, if we"
    "get committed labor and funding that values time."

    dr_lian_cho "We need to be upfront with the funders about trade-offs. The pilot isn't a verdict; it's an arbiter."

    alea_maren "And an arbiter we can demonstrate with real data."
    hide dr_lian_cho
    show tomas_reyes at left:
        zoom 0.7

    tomas_reyes "It feels good to see it not just on paper. Makes me want to get my hands in the mud, honestly."

    menu:
        "Stay for an extra run to check edge effects again":
            "You nod, fingers already on the controls. The pump hums to life and the extra run confirms the spikes — smaller or larger; the pattern stands. Your pulse quickens in a clean, productive way."
        "Log the run and go brief the volunteers at the pier":
            "You cap the tank, notes flying into your notebook. You carry the results like a lit fuse to the gates of public work, exhilarated by the translation task."

    # --- merge ---
    "The scene continues."
    # [Scene: Tide & Thread Community Kitchen | Evening — warm amber light, soup steam]
    hide alea_maren
    hide rin_sato
    hide tomas_reyes

    scene bg ch10_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Clatter of ladles; low laughter; a radio murmuring local news]
    # play music "music_placeholder"  # [Music: A warm cello line under bright piano — community warmth with a pulse]
    "The meeting with volunteers is kinetic. Rin Sato moves through the room like a comet, setting people in pairs, making jokes, and somehow stitching the scientific discipline you're bringing into something human-scale. Alea Maren read out"
    "the observation timetable and the volunteers — older fishermen, schoolteachers, teenagers with art-splattered sleeves — take the tasks with a seriousness that melts something inside you."
    show rin_sato at left:
        zoom 0.7

    rin_sato "Professor Harbor will be assigning you scientific robes if you're not careful."
    show alea_maren at right:
        zoom 0.7

    alea_maren "Only if you promise to teach the robes to make stew."

    "Volunteer (Mrs. Calder)" "We can do dawn watches. I can get my niece to help with the app if she needs a project."

    alea_maren "Perfect. Pair her with Tomas for the first week — he'll walk her through the app logging and the checklist."

    "The pilot has given you an apparatus, but it is the people who make meaning of its output. You translate model outputs into tasks and rituals: diaries for shoreline watchers, a Sunday morning bake-and-brief at Tide & Thread, a ledger where volunteers note anomalies. Your sentences slow when explaining to someone whose hands are more used to nets than notebooks — you lower the jargon, find images that anchor the data" "When the sensor spikes like this, it's like a breath you can see on the water."
    "Rin Sato watches you the whole time — amused, affectionate, but also careful. They see how you armor with certainty. They see you unpeeling it, slowly, in front of the town."

    rin_sato "You know, you don't always have to wear the confidence like chainmail. People lean on you because you make them feel seen. Let that sit between the figures."

    alea_maren "Chainmail is comfortable."

    rin_sato "Then at least add a scarf."
    "There is a buoyant, forward motion tonight: volunteers signing up, Tomas promising to lead a weekend nursery build, Dr. Lian making notes about QA schedules. The pilot has become a machine that does more than measure — it organizes, trains, channels civic energy into reproducible action."
    # [Scene: Lab — Late Night | Lights low, a single desk lamp; notebook open]
    hide rin_sato
    hide alea_maren

    scene bg ch10_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant thump of late traffic; the lab's HVAC sighing; the soft tictac of a clock]
    # play music "music_placeholder"  # [Music: A high-string motif building; heartbeat-like percussive marks]
    "Alea Maren double-check assumptions. The data packet from the day sits on your laptop like a small, incandescent thing. You re-run code, tweak the binning, test how different tide windows alter the interpretation. The model outputs"
    "are generous and cruel at once: engineered segments reduce overt surge where they stand, undeniably; but the edges show pressure pulses that scale nonlinearly with fetch. The living elements lower energy but only when deployed across"
    "broad swaths and with time for soil accretion. It is messy — but it is legible."
    show dr_lian_cho at left:
        zoom 0.7

    dr_lian_cho "Funders are already asking for an interim positive headline. They want 'Stormwall Prevents Flooding' if the numbers look tidy."
    show alea_maren at right:
        zoom 0.7

    alea_maren "We won't give them tidy if the data isn't tidy."

    dr_lian_cho "We can show them early wins without glossing over trade-offs. Edge amplification is crucial. If we can couple engineered segments with living shorelines and a managed retreat of a narrow strip, we give them a story and the town a path."
    "Alea Maren think of the town — of Maya's steady hands at the cafe, of Tomas's eager grin, of Rin's half-joke but steady presence. You think of your sibling, the one you lost; the memory is"
    "sharp but not paralyzing tonight. The pilot is both a means and a promise: to turn grief into evidence, to make decisions that can be argued in meetings and tested in reality."
    "Your phone buzzes — a terse message from a funder contact asking for a quote by morning. The ticker of time seems louder now. Your chest is a drumbeat that matches the strings, quickening toward something."
    "Rin Sato appears in the doorway without announcement, hair wind-tossed, carrying the handpainted umbrella like a banner."
    show rin_sato at center:
        zoom 0.7

    rin_sato "You're working yourself into a storm, Alea."

    alea_maren "Data calms storms."

    rin_sato "Data helps you name them. It doesn't hold your hand afterward."

    alea_maren "Then let's make it a hand worth taking."
    # [Scene: Small Conference Room — Next Morning | Bright, whiteboard-scattered]
    hide dr_lian_cho
    hide alea_maren
    hide rin_sato

    scene bg ch10_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low murmur of conversation; paper shuffling; clicks as slides change]
    # play music "music_placeholder"  # [Music: Building strings reaching a peak — momentum, a thrill of contest]
    "Alea Maren stand before a small, attentive room. The latest packet is on the screen: mapped surge attenuations, pressure transients at seam nodes, simulated scenarios with combined living elements and partial engineered segments. Eyes follow the"
    "graphs in a neat choreography — funders hungry for optimism, council staff checking for liabilities, volunteers watching like family."

    "Funder Liaison" "If you can provide a clear headline, investors will cascade further support. We need a compelling narrative of success."
    show alea_maren at left:
        zoom 0.7

    alea_maren "The interim data is instructive and imperfect. Engineered segments reduce immediate surges, but we observe concentrated pressure at adjacent unarmored shores — a transfer, not a hiding. Living elements absorb energy incrementally; they need scale and time, and they reduce erosive feedbacks when paired with managed retreat in critical zones."
    show councilor_bea_ortega at right:
        zoom 0.7

    councilor_bea_ortega "You're asking for patience and money in equal measure."

    alea_maren "Yes. I am asking for a phased investment strategy: targeted engineering where necessary, rapid deployment of living shores in contiguous swaths, and agreed triggers for retreat where modeling indicates irrecoverable risk. The pilot gives us the metrics to write those triggers objectively."

    "Funder Liaison" "We can headline a 'measured approach' if you give us a timeline with wins in six months."
    show dr_lian_cho at center:
        zoom 0.7

    dr_lian_cho "Buildable wins: increased nursery output; two kilometers of marsh plugs installed by season's end; a modeled reduction in peak stress at monitored seams."
    "Rin Sato catches your eye from the back of the room and mouths, You can do this. You feel adrenaline bloom — not panic, but clarity sharpened to a blade. The room waits. The choice is"
    "not 'should we do this' — you've already accepted the pilot — but how you will frame the results: optimistic and provisional, or cheer the engineered wins while softening the trade-offs. Funders want a clean story;"
    "the town wants truth. Your role has become translation and translation always shades the meaning."
    "Your notebook is open on the podium, damp where you pressed your thumb into the page. The cursor blinks on the slide you will present. The clock ticks. You can hear the gulls outside in the same rhythm as your pulse."
    "Alea Maren inhale. The moment tightens into a single, luminous point: speak the nuanced truth and risk losing short-term cash, or hand the funders a bold headline that may smooth the path but could obscure the cracks you're already seeing at the edges."
    # play music "music_placeholder"  # [Music: String motif peaks; high, hopeful; heartbeat percussive]
    "Alea Maren set your pen down ready to speak."
    # [Page-Turn thought: You imagine the headline that will appear in the dashboard and in the papers. You imagine the town's faces reading it. You imagine Rin beside you and Dr. Lian's steady hand. The pilot has given you data — now it asks you to choose how to tell it.]
    hide alea_maren
    hide councilor_bea_ortega
    hide dr_lian_cho

    scene bg ch10_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter12
    return
