label chapter10:

    # [Scene: Municipal Green Atrium | Late Afternoon]

    scene bg ch8_6b08b4_1 at full_bg
    # play music "music_placeholder"  # [Music: High-tempo percussion under a cold synth pad; rhythms quicken with each spoken clause]
    # play sound "sfx_placeholder"  # [Sound: Rain turning to hail against the atrium glass — a static percussion that makes voices jump]
    "The room feels too bright for the kind of conversation you're in. It throws away shadows and leaves only decisions, hard-edged and visible. You can hear your own breathing like a metronome under the council's formal"
    "tones. The schematics on the screen show a seawall segment slicing the waterfront, annotated with sensors, storm gates, and a strip of retrofitted urban canopy. Numbers tick along the margins like a countdown."
    show ari_nakamura at left:
        zoom 0.7

    ari_nakamura "The pilot covers three blocks. It reduces overtopping probability by sixty percent in model runs. We can start within ninety days if the council signs the memorandum and the grant clears."
    "You watch the way Ari says numbers — shaped, precise. There's no flourish. It is a delivery method for certainty. Your practical mind catalogues what matters: timeline, funding, maintenance responsibilities, clauses that trigger eminent relocation."
    "Nora [low] leans closer to you, whispering, her voice barely above the hum of the room."
    show nora_daz at right:
        zoom 0.7

    nora_daz "They've already budgeted the mobilization fees. If we push too hard on oversight they'll say we obstruct deployment."
    "You feel the pressure tighten — not an emotional collapse, but a procedural squeeze. It's a machine that runs on signatures and deadlines. Every delay routes funds elsewhere. Every clause you carve in affects delivery windows and the language that shelters people."
    "Luca Chen [sharp] stands across from Ari, boots planted as if on deck. He's been organizing the rallies for days; you can feel the tension in his hands like taut rope."
    show luca_chen at center:
        zoom 0.7

    luca_chen "We can't just hand over the waterfront to a sealed contract, Maya."

    ari_nakamura "And they live safer if the infrastructure is in place. This is an implementable, scalable solution. We can co-govern maintenance."
    "Luca Chen's jaw tightens, the set of his shoulders telling a different story from his words. You read the implicit: he doubts co-governance when power and resources are unequal. You read Ari's implicit: scaling saves lives at a macro level."
    "You tuck a thought behind your ribs: the community values that can't be translated into metrics. You also hold a ledger — a list of people whose roofs sag, whose boats are their pensions. You are neither sentimental nor cold; you are focused."

    menu:
        "Ask Nora to flag every clause that grants subcontractor autonomy":
            "Nora's knuckles whiten as she flips pages. 'If it's in there they can reassign maintenance, evict by proxy, or dilute our oversight,' she says. Her pen taps a rapid Morse on the table."
        "Tell Luca to delay the first rally until you read the redlines":
            "Luca exhales, shoulders folding a beat. 'Delay if you must. But don't stall so long the grant shifts away,' he answers. There's a soft plea under the command."

    # --- merge ---
    "Both outcomes converge to the following narrative."
    # [Scene: Glass Council Chambers | Evening]
    hide ari_nakamura
    hide nora_daz
    hide luca_chen

    scene bg ch8_6b08b4_2 at full_bg
    # play music "music_placeholder"  # [Music: Tighter strings; a constant ticking overlays the percussion, tempo increasing]
    # play sound "sfx_placeholder"  # [Sound: A distant amplified cough, papers shuffling like small waves]
    "The legal advisor steps through clauses aloud, each phrase a small tidal force. You listen, parsing the language like tide charts. 'Maintenance-assignment clauses,' 'anticipated displacement allowances,' 'force majeure with expedited relocation triggers' — the terms sound"
    "inevitable when spoken in the chamber's echo. The data is clinical, and that's what you're thankful for: the room's tone lets you dissect risk without being drowned in rhetoric."
    show ari_nakamura at left:
        zoom 0.7

    ari_nakamura "We include a mobilization clause to ensure contractors can stage quickly. It's standard. We can add a community liaison role."
    "You think of liaisons who hold ceremonial titles and little power. You think of grant timelines that fetishize speed over stewardship. This isn't about villainy; it's about institutional incentives."
    show nora_daz at right:
        zoom 0.7

    nora_daz "And the subcontractor clause? If it's broad, it lets them assign maintenance to an entity outside the city's oversight. We need a constraint on that, or a trigger that brings it back to municipal review."

    ari_nakamura "You make a practical point. But overly prescriptive procurement language can void grants. There's a balance."
    "You feel the room begin to accordion — expanded by options, constricted by deadlines. Your pulse picks up pace, not from panic but from the mechanical need to choose a tension that holds."
    "A junior staffer passes a tablet into your hands — a redline version. Your eyes skim headings: indemnities, salvage rights, occupancy language. Under 'Project Succession,' there's a footnote, tiny and boxed: the sponsor reserves the right"
    "to assign operational control to 'approved subcontractors' that meet defined operational benchmarks. The benchmarks are purposefully technical."
    "You tap the margin, thinking in procedural moves: add an amendment. Tie assignment to community consent. Make occupancy non-transferable without unanimous local council approval. But you also know the counterargument Ari will make: too many strings and the insurer pulls out."

    ari_nakamura "We can work with you on clause language. I want this to be a model."
    "His voice lands without rhetorical heat. Readable? Unreadable? You bracket the question; the Schrödinger rule hums in the back of your skull — don't assume his sincerity based on past gestures you might or might not have shared. Treat the facts."
    "You and Nora stay after most leave. The chamber empties like a tide out — chairs scraping, screens dimming."

    nora_daz "If we sneak a binding amendment in, it's a legal headache. But it could be enforceable. If we push publicly for endorsement, we get the optics and speed. If we refuse, we keep our leverage but we risk losing the slot and the city moves on."
    "You map those three options mentally with the precision of tidelines and legal clauses. Each has a cost. Each has a vector through people's lives."

    menu:
        "Underline 'approved subcontractors' and attach a clause requiring community board approval":
            "Nora nods slowly, already drafting language. 'It'll be messy political theater, but it might stick,' she says, eyes bright with the twin flames of legal cunning and fatigue."
        "Call your tech contact for clarity on how subcontracting has been used historically":
            "Your phone buzzes. A terse message arrives with a PDF: past contracts show assignment used to transfer obligations to shell entities. The header reads: 'red-flag. escalates displacement risk.' The word sits like a splinter."

    # --- merge ---
    "Both outcomes converge to the following narrative."
    # [Scene: Tideside Promenade | Night — Luca's Rally Preparation]
    hide ari_nakamura
    hide nora_daz

    scene bg ch8_6b08b4_3 at full_bg
    # play music "music_placeholder"  # [Music: Pulse quickens to near-climax tempo; claps and chants prep overlay the percussion]
    # play sound "sfx_placeholder"  # [Sound: Waves lapping against pilings; distant generator hum]
    "You step onto the promenade and hear the communal engine: folks who have been repairing nets, cooking soup, and nailing plywood together. Luca moves through them like someone made of that same material — pragmatic, warm, hands that know rope."
    show luca_chen at left:
        zoom 0.7

    luca_chen "If you endorse publicly without hard legal protections, people will remember us for handing everything over. They'll forgive delayed safety for integrity, but not the feeling of betrayal."
    "You look at faces shaped by tides and time. The community's patience has a shelf life measured in storms. Your sense of duty funnels into a single problem statement: how to leverage Ari's infrastructure without becoming the conduit of displacement."

    luca_chen "Don't do anything alone. If you sign, sign with us. If you insert clauses, tell us first. If you're going to refuse — say it here, not behind doors."
    "Your internal voice clarifies, methodic: transparency breeds trust. But it can also blow funding. There is a calculus: speed versus sovereignty. The arousal in the scene is high — the rally builds, drums beginning to sync"
    "with the hatch of hail on the atrium glass as if one weather informs the other."
    "Ari Nakamura arrives on the promenade, sleeves rolled, the engineered suit replaced with a practical jacket that still looks tailored to function. He watches the group without expression that tells you little."
    show ari_nakamura at right:
        zoom 0.7

    ari_nakamura "I don't want to be the person who divides you. I want a pilot that is technically sound and politically replicable. Tell me — what can we write that will protect the people and keep the project fundable?"
    "You feel every pair of eyes briefly settle on you. It's the stillness before a wave breaks. The decision is not only legal or political; it is personal governance — the model of your stewardship."
    "Nora slides up beside you, folder in hand. Luca's fingers press once into your shoulder — an anchor, neither plea nor ultimatum but physical solidarity."
    "You taste salt and paint and gasoline; the world narrows to language and leverage. The soundscape tightens: drums, rain, low murmurs. Your heart matches the rhythm set earlier — steady, accelerating, calibrated for action."
    "Ari Nakamura's expression is unreadable; it folds into 'complex' by necessity. Luca Chen's posture is pleading with authority. Nora's eyes are unambiguous in their fatigue and resourcefulness."
    "You reach for your notebook, pen poised. The choices line up in procedural clarity."
    "You could:"
    "- Endorse Ari's pilot publicly, fast-tracking protection with visible infrastructure."
    "- Sneak a strong community amendment into the contract, binding legally but risky in negotiation."
    "- Refuse the pilot and mobilize the community in direct action, preserving control but incurring delay and confrontation."
    "The air tastes like metal and rain. All three paths will change who holds the waterfront and how quickly."
    # play music "music_placeholder"  # [Music: Percussion peaks; a single sustained note holds, then tightens]
    hide luca_chen
    hide ari_nakamura

    scene bg ch8_6b08b4_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Hail loud on the atrium panes — a punctuation]

    menu:
        "Option: 'Endorse Ari's pilot publicly for immediate protection.'":
            jump chapter11
        "Option: 'Sneak a strong community amendment into the contract.'":
            jump chapter13
        "Option: 'Refuse the pilot and mobilize the community in direct action.'":
            jump chapter21
    return
