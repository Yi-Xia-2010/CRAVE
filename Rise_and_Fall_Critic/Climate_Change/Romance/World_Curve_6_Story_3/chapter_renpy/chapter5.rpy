label chapter5:

    # [Scene: Decaying Pier Platform | Dawn]

    scene bg ch5_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Water lapping softly, a distant gull; the low thrum of the hydrophone in your sling]
    # play music "music_placeholder"  # [Music: Sparse, low cello — a steady, uneasy heartbeat]
    "You bend to the line and your fingers remember how to work the salt-stiff knots. The cord is slick; the kelp brushes your knuckles like cold hands. Your notebook lies open on a weathered crate, the"
    "page beneath your palm darker with sea spray. Noah is crouched beside you, sleeves rolled, his patched sensor blinking like a small promise. You can feel the damp in the air pressing at the back of"
    "your throat—tactile, unavoidable—and under it all is the sound the hydrophone makes when the water moves: a clean, close note that you have learned to treat like truth."
    show noah_ros at left:
        zoom 0.7

    noah_ros "Okay — harmonics at 0.8 to 1.2 hertz. Look."
    "(he points, breath fogging in the cold air) 'Readout's stable. Wave amplitude down by thirty to forty percent in the shallow band. Marsh mat traction shows measurable deceleration on the current models.'"
    "You take the tablet from him, thumb hovering over the chart. The graph hums in a small blue glow: there, a trough where you had expected only noise. For a second something unclenches inside you—not triumph, not yet, but the lightness that comes from not being wrong."
    show mara_evans at right:
        zoom 0.7

    mara_evans "Show me the baseline again."
    "(your voice is steady because if you let it quiver, everyone will hear it) 'And the sediment displacement numbers for the southeast anchor.'"
    "Priya leans in with her tablet, face lit by the screen. Her voice is clipped, efficient—relief folded into professional habit."
    show priya_anand at center:
        zoom 0.7

    priya_anand "Baseline holds. Relative erosion reduced along the test strip. The mats retain—about twenty-five percent more particulate matter after moderate surge runs. That's not nothing."
    "Tomas, standing a little back with arms folded against the wind, squints at the graphs the way someone reads the tides by the shape of a cloud."
    hide noah_ros
    show tomas_belmar at left:
        zoom 0.7

    tomas_belmar "It's good. It's proper work. But good doesn't mean ready for a feeding frenzy of contracts."
    "There is a murmur from the small crew gathered on the pier: nervous laughs, a child clapping. The buoy bells tinkle. For the first time since you started this patchwork of designs and favors and late"
    "nights, you feel the shape of a path: not a finished bridge, but a plank laid toward something that might hold."

    menu:
        "Let the team celebrate, even briefly":
            "You set the notebook down and allow a half-smile to slip free; someone pops a thermos lid and the group loosens, stories crowding the cold. The thaw is small but real."
        "Keep the focus — run another calibration":
            "You square your shoulders and call for another run; the jubilation is postponed. People look disappointed, but the data gains another line."
        "Call Cass now and signal cautious optimism":
            "You lift the phone to your ear and send a short packet: encouraging but reserved. Noah gives you a look — hopeful, worried, grateful — and when you hang up you can already hear the gears of policy starting to turn."

    # --- merge ---
    "Scene continues"
    "Noah Ríos watches you as you decide, his mouth shifting into a grin that doesn't reach his eyes."
    hide mara_evans
    show noah_ros at right:
        zoom 0.7

    noah_ros "We've got something, Mara. Not perfect, but—"
    "(he lets the sentence hang) 'We can iterate. We can make it better.'"
    "You want to tell him that 'better' is the only verb you've slept with for years. Instead you let the tide of practical plans rise: anchoring points, reinforcement schedules, supply lists. Your head catalogs them in"
    "quick pulses — wood, rope, recycled concrete, labor hours — because counting is a way of keeping fear at bay."
    # [Scene: Kelp Test Beds | Mid-morning]
    hide priya_anand
    hide tomas_belmar
    hide noah_ros

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The creak of moorings; careful footsteps over wet decking]
    # play music "music_placeholder"  # [Music: A thin piano line with dissonant undertones]
    "You move from station to station, untangling a line here, pressing a probe into a mat there. The kelp smells of old ocean and green rot; the boards beneath your feet steam faintly where the sun"
    "finds them. Priya kneels and taps a point on her tablet, translating numbers into sentences for the group."
    show priya_anand at left:
        zoom 0.7

    priya_anand "We can map this across a broader stretch. Scale's the question — and money, obviously."
    "Elena is at the edge of the pier holding a torn awning cloth in both hands, eyes on the pile of notices folded outside her shop down the lane. The paper is thin, an official red stamp smudged where it touched rain."
    show elena_torres at right:
        zoom 0.7

    elena_torres "They sent the notices. Two more storefronts. Tomas said the landlord won't say he'll wait."
    "You want to step toward her, to take the paper, to tear it up and hold the pieces like a votive. Instead you compress the urge into something colder."
    show mara_evans at center:
        zoom 0.7

    mara_evans "We'll include displacement risk in the next report. We'll make the case it costs less to retrofit than to relocate."
    "(you mean it; you mean it almost desperately)"
    hide priya_anand
    show noah_ros at left:
        zoom 0.7

    noah_ros "And show every dollar saved by local labor. Investors respond to numbers and narratives. If we put in the pilot and we make the numbers undeniable—"
    hide elena_torres
    show priya_anand at right:
        zoom 0.7

    priya_anand "They will still demand a timeline. And Cass will be asked to demonstrate an immediate mitigation."
    "At the word 'Cass' a radius of silence falls. The mayor's influence is the air between the councils; that someone has to show results soon is not conjecture, it's calendar."

    menu:
        "Go to Elena and try to comfort her":
            "You fold Elena into a quick, awkward hug, fingers searching her shoulders. She presses her face against your coat and for a minute the work feels human again; then the papers rustle and reality returns."
        "Pull Priya aside to draft an emergency brief":
            "You sit with Priya on a damp crate and start writing a tight memo: figures first, people second. Priya's typing is fluent; the memo becomes a machine."

    # --- merge ---
    "Scene continues"
    "Tomas clears his throat, voice low."
    hide mara_evans
    show tomas_belmar at center:
        zoom 0.7

    tomas_belmar "You can make numbers sing, Mara. But numbers don't stop men from serving notices. They don't stop a wave. Remember that."
    "The words settle in you like a stone you have already been carrying. Your sense of responsibility does something familiar: it swells, then narrows into a laser. You could spend the rest of the week making"
    "the model perfect, or you could spend the rest of the week fighting in council chambers while someone else erects a wall that cuts your neighborhood off. Either path asks for blood."
    # [Scene: Decaying Pier Platform | Late Morning — Clouds Gathering]
    hide noah_ros
    hide priya_anand
    hide tomas_belmar

    scene bg ch5_4001e7_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Phone buzzes; distant sirens start and stop; an incoming live news chime]
    # play music "music_placeholder"  # [Music: Low strings with a rising, anxious motif]
    "Your phone vibrates. Cass's contact fills the screen — the label reads MAYOR. You answer with the same practiced steadiness you use when you call people back about permits or broken pumps, though your stomach tightens."
    show cassandra_cass_green at left:
        zoom 0.7

    cassandra_cass_green "Mara."
    "(her voice is measured, there is an edge of public rehearsed calm) 'I just came off a press line. Investors are calling my office. Arman's piece ran in the city paper — he's framing delay as"
    "jeopardizing commerce. The council is talking about emergency measures. We need a demonstration that neutralizes panic. Can you find something we can show within forty-eight hours?'"
    "You feel the weight of 'forty-eight hours' as a physical thing: heavy, sharp-edged."
    show mara_evans at right:
        zoom 0.7

    mara_evans "A demonstration with the current setup? We can show sea damping and erosion reduction for a controlled run. It won't be a finished seawall, Cass. But it will be evidence that living systems lower forces over time."
    "Cass: (a small, unreadable pause) 'The problem is optics. People see barriers; they understand concrete. If we can't put up a demonstrable 'thing' that looks like protection, the council will default to Arman's plan.'"
    "You hear papers rustle on her end, the sound of a city in motion. Her next sentence arrives sharper."

    cassandra_cass_green "And the investors are making noise in public forums. They want assurance—something quick to say to their stakeholders."
    "The mayor's speech is complex; there are loyalties in it that you cannot map from where you stand. Her voice reads as strained alliance: supportive, yes, but threaded with the calculus of votes and donors."
    "Noah Ríos steps closer, glancing at you with eyes that say plainly: do they want us to sell the coat or to keep the coat and get some thread?"
    show noah_ros at center:
        zoom 0.7

    noah_ros "We can build a phased pilot."
    "(he offers) 'Use faster materials for the visible face—recycled composites as a facade—and keep the living mat integrated behind it. It gives Cass something to show and buys us time.'"
    hide cassandra_cass_green
    show priya_anand at left:
        zoom 0.7

    priya_anand "That buys time but costs control. And if we hand the visible narrative to Arman's supporters—"

    mara_evans "It also risks legitimizing shortcuts. If the visible face is hard armor, the city will become used to that as the solution."
    "(you feel the sentence tighten in your chest) 'We can't let short-term optics become the long-term paradigm.'"
    # play sound "sfx_placeholder"  # [Sound: A tablet chimes; someone reads aloud from a news article. The voice is thin with contempt.]
    hide mara_evans
    show elena_torres at right:
        zoom 0.7

    elena_torres "Arman says it's 'romanticism that costs jobs.'"
    "The op-ed's cadence is a drumbeat: fear-scare, economy-threat, swift-solution. You hear Arman's voice as if he's standing across the pier: calm, polished, absolutely sure of the moral rectitude of his urgency. The sentence lands in the group like a slap."
    "A local shop owner down on the lane, a woman who used to hand out bread during storms, collapses against the doorframe of her shop. Rent notices in her hand. Tears stream through the salt on her face. Elena drops the awning; it flaps uselessly in the wind."
    "You move toward them and for the first time the options stop being abstract. The calculus of models and pilots and optics suddenly is the count of how many red-stamped envelopes are in a single mailbox."
    "Your responsibility narrows until everything that isn't direct aid is background noise."

    noah_ros "We have three paths. Public action, compromise for pilot funding, or prioritize evacuation planning while we keep the pilot going quietly."

    priya_anand "Each has downstream costs. Legal trouble, loss of community control, or displacement."
    hide noah_ros
    show tomas_belmar at center:
        zoom 0.7

    tomas_belmar "And your heart, Mara. Which one can you live with?"
    "You close your eyes for an instant and picture the pier from earlier: hands that hammered; the child's kelp frond pressed into your palm. A storm in the future feels like a knife pointed at that memory."

    menu:
        "Call for a quick community meeting here on the pier":
            "You shout for attention: a small circle forms, voices rise, plans are sketched on a piece of cardboard. There's a raw sense of democracy — messy and loud — and you feel the weight of leading it."
        "Tell Noah and Priya to draft the phased-pilot proposal now":
            "Noah nods, shoulders set; Priya already opens a blank document. The work becomes efficient, methodical — but there is a quiet in Elena's eyes that did not soften."
        "Ask Tomas to organize evacuation lists while you secure data":
            "Tomas moves with the surety of someone who's done this before; he starts calling names and checking boats. You move back to the sensors and the numbers, hands shaking just enough to show how much you care."

    # --- merge ---
    "Scene continues"
    "The rain becomes more than mist; it's fine grit that bites at exposed skin. The pier smells of wet canvas and iron. The people around you lean into whatever role you give them. You are the hinge. You can feel the city's calendar trying to twist you open."
    "Inside your head, the obligations chant: keep people here; keep people safe; do not hand the story to those who would displace them. The words form like tide lines — overlapping, contradictory."
    "You think of Elena's face when she read the notice. You think of the child's kelp frond. You think of Noah's wary optimism. You think of Cass's measured tone and Arman's op-ed that makes her office shudder under investor calls."
    "Your chest feels too small for the list of choices the day hands you."
    hide priya_anand
    hide elena_torres
    hide tomas_belmar

    scene bg ch5_4001e7_4 at full_bg
    # play music "music_placeholder"  # [Music: Strings pull tight, then fall away into a single sustained minor chord]
    "You take a breath and prepare to commit — to choose a path that will define what 'protection' looks like in Esperanza Bay, and what the word 'we' really means."

    menu:
        "Organize a public blockade and demand a moratorium on Arman":
            jump chapter6
        "Accept phased materials and speed constraints to win pilot funding":
            jump chapter7
        "Coordinate targeted evacuations while continuing the pilot quietly":
            jump chapter8
    return
