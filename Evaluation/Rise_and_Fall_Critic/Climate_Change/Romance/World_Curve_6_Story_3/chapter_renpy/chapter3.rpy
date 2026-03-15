label chapter3:

    # [Scene: City Council Chamber | Midday]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm, ascending strings with a steady rhythmic undercurrent — hopeful, measured]
    # play sound "sfx_placeholder"  # [Sound: Murmured conversations settling, the soft click of a projector, a distant gull through a vent]
    "You walk in with the taste of the greenhouse still on your tongue: iron from pumps, damp soil, the faint sweet of kelp. The chamber's air is different — conditioned and dry, like a throat cleared"
    "for testimony. Your boots sound too loud on the polished floor. You close your hand around the pendant beneath your sweater and feel the familiar weight: a small, private anchor."
    "Cassandra Cass Green sits behind the dais, sea‑glass brooch catching the light as if it were a small promise. Her smile is practiced, but when she looks at you there is a momentary softening, a fissure"
    "that feels like possibility. Arman Kade occupies the other end of the chamber like a punctuation mark in navy; his waveform cufflinks glint with every slight motion. He watches you with an expression you cannot quite"
    "read — complex, like weather that might break or clear."
    "Noah Ríos is in the third row, sleeves rolled up despite the formality. His prototype sensor — the one he swore would blink its way into hearts and budgets — sits beside him, a tiny LED"
    "pulsing on and off like a measured breath. Elena leans forward in the gallery, paint under her nails still visible; Tomas Belmar stands beside her, shoulders stooped but steady, eyes like tide charts: patient, knowing."

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Projector hum; a soft intake of breath from the gallery]
    "You step to the podium. The mic feels slightly warmer than you expect, and for a second the room contracts — just you, your voice, the slide behind you. You exhale and let the work steady you."
    show mara_evans at left:
        zoom 0.7

    mara_evans "Honorable Council members — Mayor Green — thank you for hearing me today. I'm Mara Evans. I grew up on the East Strand. I watched the storefront my family had for generations fall to one storm. I am here because that loss taught me what we must protect: not just infrastructure, but the people who live between the tides."
    "(You pause. The slide behind you shifts to an aerial sketch: living mats threaded with kelp lines, benches that double as berms, community access points marked in bright yellow.)"

    mara_evans "This is a living seawall — co‑designed with residents, integrating kelp nurseries, permeable terraces, and modular, green‑steel reinforcements. It grows stronger with the community: jobs in kelp farming, public access maintained, and an adaptive structure that bends with our changing tides."

    "Councilmember 1" "Ms. Evans, can you speak to measurable protection? Sea level projections are not abstract in our budgets. Investors and constituents want to know: how many centimeters of storm surge mitigation, and on what timeline?"
    "Your throat tightens. The question is a hook meant to pull you into spreadsheets, into the language of immediacy that favors a single, fast answer."

    mara_evans "We have models prepared.' (You gesture; a graph blooms behind you — measured curves, confidence bands.) 'Pilot sections demonstrated a reduction in wave energy by twenty to forty percent depending on configuration. More importantly, the system's adaptive growth means cost per protected household declines over time, and community maintenance creates local stewardship that external contractors cannot replicate."
    "Arman Kade leans forward, palms resting lightly on the dais rail as if he wants to be close enough to touch the slide."
    show arman_kade at right:
        zoom 0.7

    arman_kade "It's an elegant picture, Ms. Evans. But 'adaptive' is not the same as 'timely.' The city cannot gamble on an unproven, multi‑year pilot when we can erect a consolidated seawall within months that will protect critical infrastructure and reassure markets. We need something that will hold the line now."
    "His voice is smooth, rehearsed. Council murmurs ripple like surf hitting distant rocks. You can feel the shape of the argument — security, speed, the promise of certainty — filling the room like a high tide. It is persuasive precisely because it speaks to fear."

    mara_evans "Noah Ríos's sensor network can give real‑time metrics for the living sections. We can begin pilots at scale before any broader build, producing the same demonstrable data investors ask for while keeping people here. This isn't 'either/or' — it's a staged, accountable pathway."
    "(You click. A close‑up of Noah Ríos's prototype fills the screen; the LED on his device blinks in time with the tiny icon. You notice a few council members tilt their heads toward the light. Noah"
    "Ríos meets your eyes across the aisle — a flicker of worry, of determination. He nods once, small and sure.)"

    menu:
        "Tuck the pendant and bend to sound calmer":
            "You press your pendant into your palm and let your shoulders drop. Air moves in a little easier. Your voice regains its evenness."
        "Slide a small schematic to Noah Ríos under the podium":
            "You slide the folded schematic and his hands catch it mid‑breath. His fingers tighten; he reads, then gives you the tiniest, steady smile."

    # --- merge ---
    "Continue the narrative after the interaction."

    "Councilmember 2" "Mayor, we need guarantees. If a pilot fails, who covers the cost? If we pivot resources to community projects, what ensures they don't stall halfway?"
    "Cass's question is careful, the cadence of someone balancing re‑election and hunger for practical results. She is the hinge in this room. Her sea‑glass brooch glitters; you feel the warmth of something like hope when she narrows her eyes, not in suspicion, but in focus."

    mara_evans "We build binding maintenance agreements with community cooperatives, insurance‑backed contingency clauses, and staged deliverables mapped into the city budget. Priya's team has prepared a phased funding schedule that ties payments to measurable ecological and social metrics."
    "Arman Kade's rebuttal comes polished and fast — he frames delays as risk, frames community projects as 'soft' solutions unsuited to the city's urgent fiscal calculus. He speaks about investor confidence, the cost of inaction, and"
    "the moral imperative of protecting the majority now. His arguments land like well‑thrown pebbles on a pond; the rings spread."

    arman_kade "You can either secure the city's economic spine, or you can entangle us in experiments that please a few neighborhoods but leave us exposed. We build a seawall, we move forward."
    "You can feel heat rise in your neck. The image he paints is stark: a city that prioritizes the core, with margins sacrificed. But his language — decisive, protective — also resonates with people who remember the last flood into the municipal treasury."
    "Tomas Belmar leans forward in the gallery and speaks before you can think to silence him."
    show tomas_belmar at center:
        zoom 0.7

    tomas_belmar "Protection shouldn't mean removal. We know the water. We know how to live with it. You can't buy what this place is made from."
    "His voice is a cracked bell — not performative, but true. A few heads in the council gallery turn. Elena catches your eyes; her jaw is set. The room has shifted — the testimony is no longer just about plans; it's about faces you know."
    "Noah Ríos steps out from his seat, approaching the side of the dais with a cautious certainty. He speaks quietly, clearly, the tone of someone who prefers equations to rhetoric but has learned the language of persuasion."
    hide mara_evans
    show noah_ros at left:
        zoom 0.7

    noah_ros "Council — my team has run redundancy tests on the sensors. We can deliver a small‑scale deployment within three weeks that generates the data Ms. Evans referenced. We need a commitment to pilot funding, not a closed door."

    "Councilmember 3" "Three weeks? That's optimistic."

    noah_ros "Optimistic, yes. But it's also realistic with the right support. And the data is what makes a living system accountable. It wouldn't be guesswork — it's measurable, replicable, and community‑managed."
    "You and Noah Ríos trade a look that says what words cannot: we have the tools; we need the chance. Hope, in the chamber, feels almost loud enough to be heard."

    menu:
        "Step down and clasp Elena's hand in the gallery":
            "You step off the podium and reach for Elena. Her hand is warm and callused. For a heartbeat the fight shrinks to a small, human moment."
        "Remain at the podium and wait for Council's questions":
            "You stay. The room's focus returns to you; you breathe and let the detail‑work pull you forward — numbers, timelines, accountability."

    # --- merge ---
    "Continue the narrative after the interaction."
    "Cass leans forward, eyes like a calculating tide map."
    hide arman_kade
    show cassandra_cass_green at right:
        zoom 0.7

    cassandra_cass_green "If we grant a pilot, what prevents the city from being held accountable if it fails? Is the administration prepared for the political fallout if a portion of the waterfront is compromised during a storm?"
    hide tomas_belmar
    show mara_evans at center:
        zoom 0.7

    mara_evans "We prepare for that possibility by designing redundancy and emergency response frameworks with community leadership baked into the process. We don't expect perfection. We expect partnership, transparency, and an insurance structure that mitigates downside. The alternative — a sealed, privatized seawall — protects buildings but displaces people who have nowhere else to go."
    hide noah_ros
    show arman_kade at left:
        zoom 0.7

    arman_kade "Displacement is a policy problem, not a technical one. We can build safeguards that minimize relocation. But time is the variable here."
    "The exchange continues. It builds in texture: interruptions, clarifying questions, councilmembers pressing about budgets, timelines, and measurable metrics. You answer where you can, lean on Noah Ríos for technical specifics, and let Tomas Belmar and Elena's"
    "presence do the part numbers cannot: remind the room that this is a human place."
    "After a sustained back‑and‑forth, the Mayor stands and addresses the chamber with the authority of someone who knows the political weight of a calendar."

    cassandra_cass_green "Council has until the mid‑month vote. We will consider an expedited seawall plan and a pilot grant for community projects. I ask everyone to present their final clarifications by next week. We will not make decisions in the dark."
    "Her voice carries a small mercy: a schedule that keeps the issue alive. It's not victory, but it is space — and space is what you need to move from argument to action."
    "Arman Kade's expression as the room begins to clear is difficult — complex, unreadable. He offers a polite nod that does not read as agreement but as calculation. You do not assume more than that; you catalog the look and file it under possibility."
    "Noah Ríos sidles up beside you once the formalities thin out. He smells faintly of solder and coffee. The sensor's LED blinks again in his hand, a tiny lighthouse."
    hide cassandra_cass_green
    show noah_ros at right:
        zoom 0.7

    noah_ros "You held the room. You were… better than I expected."

    mara_evans "You kept the bluff from turning into a show of cards."

    noah_ros "We could prove this. Fast prototypes, staged metric releases. The council wants numbers — give them numbers. It'll mean cutting corners in some design aspects, accepting compromises on access in the short term, but it could buy us leverage."
    "You turn that over in your head: trading some design purity for demonstrable metrics, trusting that once data exists, hearts and spreadsheets can be moved. It could mean a tighter partnership with Noah Ríos, long nights,"
    "and perhaps decisions that gnaw at your ideals. Or it could mean the concrete of the seawall winning while your living systems remain a footnote."
    "Elena squeezes your hand when she passes — no speech, only a pressure that translates as faith."
    hide mara_evans
    show tomas_belmar at center:
        zoom 0.7

    tomas_belmar "Make the mayor see the people who put work into this. Not numbers. The work. Numbers follow."
    "His words are simple and true. You feel your conviction and your fatigue braided together; still, there is a momentum here — more than fear, more than loss. The room's exit hums like a tide going out: receding, but leaving possibilities exposed."
    "The clock on the dais ticks toward decisions. You stand in the doorway of what comes next, heart steadying into resolve."
    "You are at a fork. The choices are not just tactical; they are a portrait of who you are and what you will ask the people you love to carry. There's a possible triumph in any"
    "of them — if you choose carefully, if you can hold others to your standards and let compromise be a step, not a surrender."
    # play music "music_placeholder"  # [Music: Strings swell slightly, sustaining an upward, hopeful motif]
    hide arman_kade
    hide noah_ros
    hide tomas_belmar

    scene bg ch3_98c6f2_3 at full_bg
    "You take a breath. The city gives you room to act."

    menu:
        "Rally the neighborhood and refuse Arman":
            jump chapter4
        "Work with Noah to make immediate demonstrable prototypes":
            jump chapter9
        "Negotiate with Cass to broker a public-private compromise":
            jump chapter13
    return
