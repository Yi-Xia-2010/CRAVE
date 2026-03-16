label chapter15:

    # [Scene: Courtroom | Morning — Hearing Day]

    scene bg ch12_e67f19_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmured crowd, the soft click of camera shutters, the judge's gavel thudding into the silence]
    # play music "music_placeholder"  # [Music: Tense, pulsing low strings — tempo quickening]
    "You arrive with a paper folder heavier than it looks. The injunction petition is folded into it like a held breath. You can feel the damp weight of the Commons on your palms — a hundred"
    "signatures, Rae's stencil marks, Tommy's crooked scrawl — and something like responsibility presses against your ribs."
    show mara_lin at left:
        zoom 0.7

    mara_lin "I'm ready,"

    "Lead Counsel" "We've practiced the chronology. Amina's exhibits are up front. Elias will be called to testify. Stay close to the facts."
    "(She taps her own folder, watching your face like a compass.)"
    "The judge takes the bench. The courtroom narrows to the physics of testimony: a microphone, a lectern, the steady tick of the clock above the door. You smell coffee and dust and the faint chemical tang"
    "of the legal pads. Your heartbeat pins itself to the rhythm of a distant surf."
    "Dr. Amina Bhatt is first to speak with the force of evidence: sediment cores, modeled sea-level projections, peer-reviewed indices. Her voice is calm, exact, and it lands in the room like mapped tide-lines — precise, indisputable."
    show dr_amina_bhatt at right:
        zoom 0.7

    dr_amina_bhatt "This site, when measured against our modeled storm surge intensities and soil porosity, shows a high probability of levee undermining within five to seven storm seasons without adaptive restoration."
    "(She slides a binder of charts forward. Her hands are steady; her eyes meet the clerk's like an anchor.)"
    "You watch faces in the gallery shift: some frown, some soften. The defense lawyer smiles, thin. The corporate rep across the table folds his hands like a closed tide pool."

    "Defense Counsel" "These are models, Doctor. Models are useful, but they are not deterministic. There are economic stakes and wellbeing tied to continued activity."

    dr_amina_bhatt "No model is prophecy, but the empirical cores match the modeled risk. These are not projections divorced from site observations — they corroborate one another."
    "Her testimony is threaded with the kind of scientific rigor that sounds like law. It gives the judge a structure to say yes to a temporary halt and a stronger mandate for assessment."

    menu:
        "Clarify a technical point aloud":
            "You rise, voice clear: you press the detail about marsh infill and how that alters nearby erosion. The attorneys nod; Amina adds a clarifying figure."
        "Let Amina carry the technicalities":
            "You keep your hands folded. Amina answers with the specifics, and the room turns to her. You feel both protective and sidelined."

    menu:
        "Push to make the monitoring public and transparent":
            "You argue for public dashboards and community stewards. Amina nods, seeing the political leverage. Counsel warns about pre-judging certain sites."
        "Limit disclosures to preserve legal posture":
            "You agree to keep some data confidential for legal protection. It tightens the case, but you sense the community will bristle at the secrecy."

    menu:
        "Funnel more resources into the legal fight":
            jump chapter17
        "Seek a negotiated scientific pause with Amina mediating":
            jump chapter8
    return
