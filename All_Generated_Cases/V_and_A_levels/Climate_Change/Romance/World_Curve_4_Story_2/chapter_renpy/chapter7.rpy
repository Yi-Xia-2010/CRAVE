label chapter7:

    # [Scene: City Archive & Council Hall | Early Evening]

    scene bg ch7_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense BGM — low strings, a pulsing undercurrent]
    # play sound "sfx_placeholder"  # [Sound: A distant siren; the soft scrape of chairs; the rustle of printed amendments]
    "You leave the podium with your satchel a weight at your hip and the memory of the gavel's soft tap still vibrating in your teeth. The room that filled with expectation has condensed into a dozen"
    "small verdicts: guarded looks, tight nods, a cell phone screen already recording the fissure you opened."

    "Council Chair" "Ms. Soren, the motion will stand as recorded. The Council recognizes your insistence on a full review. We will schedule hearings and an environmental assessment per your request."
    "You feel the words land like a tide pulling back—no roaring applause, only the attentive silence of a bureaucracy making space for delay. The Chair's tone is polite; his eyes say what the press will say in the morning. 'We hear you, but time is not our ally.'"

    "Councilor Alvarez" "You realize what this signals to donors, Ms. Soren. That delay could cost us the funding window. The sea won't wait for committees."
    "You do. You feel the cost threaded along your nerves: contracted timelines, the escrowed funds blinking on a ledger somewhere, donors with red lines in their margins. You do. But you also feel the memory of"
    "a garden uprooted for concrete—Rosa's hands muddy, the way the community's laughter cut short when bulldozers arrived. That image is why you refused."
    show maya_soren at left:
        zoom 0.7

    maya_soren "I will not trade certainty for a lie of speed. Not this time. Not when the people who were always last to be asked will be the first to lose everything if we rush."

    "Council Chair" "Ms. Soren, understand the political reality. There will be fallout. Some councilors will quietly seek alternatives — private tenders, emergency clauses. You understand the ramifications for your leadership seat?"
    "The chamber hums with careful distance. A reporter leans forward, pencil poised like a blade. A councilor murmurs about 'public panic.' Each phrase is a ledger entry against your public favor."
    "You open your mouth to answer, but the words you want—context, justice, long memory—are heavy and won't fit in the allotted time."
    hide maya_soren

    scene bg ch7_453e40_2 at full_bg
    # play music "music_placeholder"  # [Music: Strings shorten into staccato pulses]
    "You step out into the board corridor. The air smells of old paper and rain-sick salt. Outside the high glass, Harrow Bay's silhouette is a smear: cranes, raised walkways, and the darkening plain of the sea."
    # [Scene: Resilience Hub | Evening]

    scene bg ch7_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: Rhythm increases — a quickened, anxious percussion]
    # play sound "sfx_placeholder"  # [Sound: The thrumming of the hydroponics pumps, someone hammering in the distance]
    "You arrive to a smaller, more honest audience—people who won't parse your words into political capital because they live with the consequences. Elias Voss meets you at the door, hands buried in his jacket pockets, face flushed with something that could be anger or fear."
    show elias_voss at left:
        zoom 0.7

    elias_voss "You turned them down,' he says, the statement a pry. 'You really turned them down, Maya. With the forecast trending on the models we ran."
    show maya_soren at right:
        zoom 0.7

    maya_soren "I did. The contract bypassed safeguards: limited transparency, proprietary monitoring, little community control. I can't sign something that puts our neighborhoods at the mercy of a black box."

    elias_voss "So you gamble on hearings and committees? While the weather windows close? While assets are being readied? You—' He stops, searches your face. 'You know what happens when windows close."
    "You feel his hands tremble slightly; the urgency behind him is raw and immediate, as if his blood were already at sea. Your chest tightens with protective instinct—for him, for the boat that taught him to read swells, for the optimism that makes him try again and again."

    maya_soren "This isn't about theoretical safety. It's about who gets to choose what safety looks like. I've seen 'quick fixes' become permanent displacements. I won't be the person who signs that away."

    elias_voss "And if something hits before the review wraps? If that garden, that street, that kitchen is gone because we waited for process—what then? What about the people who can't afford to wait?"
    "Your exchange is not new, but the stakes have sharpened. Eyes gather in the room—Asha Reed at the table with her hand still ink-smudged from flyers, Dr. Lena with a tablet clutched like a talisman, Jonah by the tool wall, Rosa folding her hands on her lap."
    show asha_reed at center:
        zoom 0.7

    asha_reed "You made a choice I can respect, Maya. It's rare to see someone put process and people above quick bandages. That said—' (she pauses, measuring) '—process without movement is its own harm. We must do both."
    "Asha Reed's tone is warmer than it was in the chamber—approval small and precise. Her shoulders relax a fraction; a wedge of solidarity slips through her usual blaze. It is not trust yet, but a door unlatched."
    hide elias_voss
    show dr_lena_huang at left:
        zoom 0.7

    dr_lena_huang "The ecological assessment is necessary. There are feedbacks that a rapid deployment could trigger—sediment shifts, kelp displacement—but I am also neurologically aware of the lag between pure data and lived risk. We need a plan that acknowledges both."
    hide maya_soren
    show elias_voss at right:
        zoom 0.7

    elias_voss "So we build something temporary—reversible barriers, rapid-deploy soft structures—while the review runs. We buy ourselves days, maybe weeks. Is that so impossible?"
    "You feel the room pivot on that word: temporary. It smells of compromise and sacrifice and something like survival."
    hide asha_reed
    show jonah_mek at center:
        zoom 0.7

    jonah_mek "I can build revetments and tie-offs. Nothing permanent. Quick timber mats, sandbag frames. It buys time."
    hide dr_lena_huang
    show rosa_calder at left:
        zoom 0.7

    rosa_calder "Whatever we do, we keep it local. We plant roots back into the soil. We remember."
    "The conversation bounces—technical details, procedural constraints, moral calculus. It is fast, layered, voices overlapping. The urgent cadence of the moment pushes you to choose not just strategy but tone: conciliatory, defiant, maternal, pragmatic. Each posture will change who walks with you."

    menu:
        "Reach for Elias's hand":
            "You let your fingers close around his wrist, an anchor and a promise. Elias exhales—part relief, part reprimand—and says, 'Then we do it together.' Asha watches, inscrutable."
        "Step back and point to the whiteboard":
            "You pull away and trace the outline of processes, meetings, and timelines. Your voice narrows to the technician's clarity; Elias's expression tightens but he nods toward the schematics. Asha leans in, eyes scanning the dates."

    # --- merge ---
    "The micro-choice ripples outward in the room's energy. Whether you anchor Elias or speak to the plan, the result is the same: the Hub becomes a war room. In the haze of condensation and incandescent light, you parse options like debris flung up at high tide."
    # play music "music_placeholder"  # [Music: Percussive strings spike; the storm's edge hisses like a held breath]
    # play sound "sfx_placeholder"  # [Sound: Thunder, distant but insistent]
    # [Scene: Rooftop Garden | Night — Storm Clouds Gather]
    hide elias_voss
    hide jonah_mek
    hide rosa_calder

    scene bg ch7_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Full orchestra, tension rising toward a peak — brass under a low vocal tone]
    # play sound "sfx_placeholder"  # [Sound: The clack of rain beginning to lace the air; distant creak of raised walkways]
    "You convene the core group on the rooftop where, months ago, you'd held optimistic planning sessions. Now the greenhouse domes fog thickly; the tomato vines sway as if whispering urgency. The air tastes of salt and wet earth—intensified, as if the world itself is leaning in."
    show dr_lena_huang at left:
        zoom 0.7

    dr_lena_huang "The forecast has sharpened. Model clusters converge: increased storm intensity with high surge potential. If we do a phased approach, I need clear constraints on what 'temporary' means, and metrics we can monitor in real time."
    show maya_soren at right:
        zoom 0.7

    maya_soren "Agreed. Clear constraints. Transparent metrics. Community oversight."
    show asha_reed at center:
        zoom 0.7

    asha_reed "And who sits on that oversight? We don't want a token seat. We want veto power on anything that risks displacement."
    hide dr_lena_huang
    show jonah_mek at left:
        zoom 0.7

    jonah_mek "And materials—locally salvaged, reversible, maintainable. No corporate proprietary systems we can't service."
    hide maya_soren
    show elias_voss at right:
        zoom 0.7

    elias_voss "I can fast-track prototypes for soft barriers and kelp-anchoring arrays. But I need authorization to mobilize the Aster for immediate deployment tests. Even a small run could show efficacy before a storm hits."
    "You inhale the wet cold like a punishment. Everything compresses into the next decision: move now with limited footprints, halt for absolute scientific certainty, or fold resilience into community micro-projects that empower residents but lack scale."
    "Each choice bears a cost measured in sea levels, lost gardens, livelihoods, and the fragile thread of trust that holds this coalition together."
    hide asha_reed
    show maya_soren at center:
        zoom 0.7

    maya_soren "I chose review because my memory will not let me choose otherwise. But memory is not a substitute for safety. If I fail to find a way that holds both—people's voices and their roofs—then I have failed in the same way as when I ordered that compromise years ago."

    "Rosa steps forward, voice small but steady" "You once told me you would not let my seeds be number in a ledger. Keep that promise."
    "The sky answers with closer thunder. The string lights flicker, and for a moment the rooftop is only bodies leaning into one another under a primed sky."

    menu:
        "Work through the night with the team":
            "You set the schedule, assigning watch shifts, monitoring protocols, and a makeshift command cadence. Elias rolls up his sleeves without being told. Everyone snaps into motion, the anxiety converting into furious, focused labor."
        "Send everyone home to fortify their own blocks and rest":
            "You order people to return to their neighborhoods, to batten down and strengthen local networks. Jonah's jaw tightens—pride and worry—and Asha lingers a heartbeat before nodding, the activist in her already planning supply dispatches."

    # --- merge ---
    "The wind bites colder. The urgency is no longer abstract policy; it is sandbags, boats, and the hum of engines. You can feel your pulse in your throat, the taste of metal on your tongue. Standing"
    "there, beneath the pitched clouds and humming lamps, the decision that must be made crystallizes into a hard-edged question."

    maya_soren "We will not sign away oversight for speed. But we cannot stand idle while the sea closes in. We need a path that honors both the science and the people."
    hide jonah_mek
    show dr_lena_huang at left:
        zoom 0.7

    dr_lena_huang "There are three operationally distinct paths we can take. Each choice has measurable outcomes—and risks. We must pick one now and allocate resources accordingly."
    hide elias_voss
    show asha_reed at right:
        zoom 0.7

    asha_reed "And whoever is at the helm will be judged by what happens next. Be clear about what you can live with."
    "Elias Voss looks at you as if asking both for permission and absolution. His blue eyes are narrowed, urgent. The feeling between you is raw: not accusations anymore but the brittle, exposed intimacy of people who trust each other enough to be hurt."

    maya_soren "This is the hinge. The city will read our choice as a moral argument writ in sand and stone. I can feel the future tilting."
    # play sound "sfx_placeholder"  # [Sound: A cold gust snaps a banner; rain begins in earnest. Voices rise and sharpen.]
    # play music "music_placeholder"  # [Music: Crescendo — the highest, most urgent swell yet]

    menu:
        "Implement temporary, reversible protective measures while review continues.":
            jump chapter8
        "Hold all action until review concludes, prioritizing scientific certainty.":
            jump chapter11
        "Authorize small community-led micro-projects with local control and monitoring.":
            jump chapter12
    return
