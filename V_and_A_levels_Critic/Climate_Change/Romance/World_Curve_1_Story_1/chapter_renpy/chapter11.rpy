label chapter11:

    # [Scene: Harborfront bench | Night]

    scene bg ch11_e67f19_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Harbor wind, a steady, rattling whisper; distant rally chants like a tide under the city’s breath]
    # play music "music_placeholder"  # [Music: Tense, driving strings; tempo quickening]
    "You fold the memorandum open and close it with the same clumsy politeness you give fragile things. Paper creases under your fingers. The signature line from the meeting still hangs at the edge of your memory"
    "— a held pen, Irene's unreadable face, Luca’s too-smooth grin. You remembered saying the words you had practiced: oversight, pilot, housing protections. Then the document was placed in front of you like a lit match."
    "Now, alone beneath the sodium lamp, you read the draft with the harbor wind flattening your bun into a damp, stubborn knot against your neck. The clauses run like a tide chart — numbers, permits, timelines"
    "— and under them the city’s intention: rapid barriers for rapid safety, parcels ceded in exchange for anchor loans. The living-infrastructure pilot is there — a small, ringed promise — but it's nested inside legal language"
    "that could be rewritten by a single lawyer’s quirk."
    "Salt smells sharp on the paper. The lamp hums a thin, electrical note you can feel in your teeth. Your chest tightens. This is not only about pilings and permits; it is about who gets to sleep tonight without fear, and who wakes to the sound of backhoes at dawn."

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A faint megaphone from the rally, cadence of voices building]
    "You test a sentence on your tongue — the one you’ll say if you sign, the one that will sit in minutes and histories. It tastes like copper and tidewater. Signing could mean immediate funds for"
    "pilings and pumps that could save homes that cannot wait. Refusing could mean a longer fight that might preserve more agency and soil in the long run. Elliot’s third way sits between them: phased private barriers"
    "while scaling community pilots — a brittle bridge that needs legal bolts."
    show elliot_chen at left:
        zoom 0.7

    elliot_chen "You look like someone who's been trying to read clause twenty-seven by moonlight."
    "You look up. He has his drafting glasses on his head, smudged; his jacket smells faintly of moss and machine oil. There’s a jar of seawater on the bench between you — a habit he keeps, an offering of immediate tangibility."
    show maya_rios at right:
        zoom 0.7

    maya_rios "It reads like someone wrote safety in one hand and a yacht registry in the other."

    elliot_chen "Luca's prose is expensive. It's the kind that glitters and keeps you from seeing the seam."
    "You watch him as he scans the lines. There's a bright impatience in his green eyes tonight, the kind you have seen when he believes the prototype will work if only someone would stop postponing the start date."

    elliot_chen "Irene said yes to oversight, right? She said addenda. That means—"

    maya_rios "Addenda are promises that can be tabled. The language matters. 'Oversight' can be advisory or binding. 'Pilot' can be piloty."
    "Elliot's brow furrows. He taps the paper with a trembling finger like it’s a flat sea he can sketch a solution on."

    elliot_chen "We could force the timeline. Fast approvals for pilot permits, audited milestones, public enforcement clauses. I can draft a phased approach tonight—anchor the private works to the pilot's completion."
    "His urgency feeds the air. You feel the lift — a way forward, precarious and full of possibility."
    # play sound "sfx_placeholder"  # [Sound: Footsteps; a hush parts the wind as more bodies gather nearby — Sami and a cluster of neighbors, Dr. Noor under an umbrella, Irene and Luca a short distance away near City Hall’s lit façade]
    hide elliot_chen
    hide maya_rios

    scene bg ch11_e67f19_3 at full_bg
    "Sami Alvarez arrives like a current — bright vest, voice rough at the edges with recent shouting."
    show sami_alvarez at left:
        zoom 0.7

    sami_alvarez "Maya! People are freezing out there. Kids are scared. If this barrier gets built, some roofs stop leaking now. Some roofs.' (He gestures helplessly to the cluster of neighbors.) 'We have to save them."

    "Neighbor 1" "My twins wake up crying from the last storm. I can't tell them we'll fight in court while the tide gets higher."

    "Neighbor 2" "And what about our histories? My family's been on that pier for thirty years. I won't sign away my land for a glossy wall."
    "The crowd becomes a chorus of immediate, competing claims — urgency for survival and the ache of ancestral loss. Your throat tightens around both."
    "Dr. Noor steps forward, palms open like a calm measurement."
    show dr_noor_patel at right:
        zoom 0.7

    dr_noor_patel "The data supports immediate stabilizing measures in critical zones. But the long-term model shows risks if we over-rely on hard armor. Where you can phase, do so. Where you must protect short-term life, prioritize it with strict, enforceable conditions."
    "You listen. Her voice is steady; she is the person who taught you to read a floodplain and a risk matrix the way some people learn to read their own pulse. Her presence is both comfort and responsibility amplified."
    "Irene Voss approaches with Luca at her shoulder, the two of them a practiced blade of municipal and private interests."
    show irene_voss at center:
        zoom 0.7

    irene_voss "We can move permits within weeks. Luca's team will front anchors and quick mobilization. The pilot will be included — a demonstrable living segment. We are proposing explicit language for oversight and housing protections."
    hide sami_alvarez
    show maya_rios at left:
        zoom 0.7

    maya_rios "Explicit how? Legal guarantees? Third-party enforceability? Or oversight that can be turned off with the next council majority?"
    "Irene Voss's face does not soften; it becomes something more complex than a smile or a frown — a ledger of past failures and pragmatic calculation. You cannot read her like a ledger, not fully. Her eyes flick to Luca, to Dr. Noor, then back to you."

    irene_voss "Enforceable. Binding timelines. Penalties for non-compliance. We will include clauses for independent audits, community representation on the oversight board."
    hide dr_noor_patel
    show luca_marin at right:
        zoom 0.7

    luca_marin "And generous buyouts for households that choose relocation. Compensation and relocation assistance, expedited paperwork. This is the fastest path to large-scale protection."
    "Sami’s jaw tightens at 'buyouts'. You hear the raw edge of indignation and fear. The neighbors stir."
    hide irene_voss
    show sami_alvarez at center:
        zoom 0.7

    sami_alvarez "You give money and call it progress. You uproot people who don't have options. That's not the same as safety."
    "You look at the buyout clause. It reads like a polite erasure: targeted funds, relocation routes, a deadline. For some the funds will be lifelines; for others they are a coffin nail."
    "Your chest is a drum. The arousal in you rises: breath coming faster, the sodium lamp's hum a high string in your skull. The papers rustle like surf."

    menu:
        "Mark the buyout clause with a red pen":
            "You drag a jagged line across the paragraph, the red ink bleeding like a wound. Heads turn; the act is small but visible."
        "Fold the clause under and leave it unmarked":
            "You tuck the page down as if hiding a hurt. Elliot's shoulders slump in relief and then in worry, reading your silence."

    menu:
        "Call for a real-time edit session — demand language be rewritten now":
            "You lift your voice and call for lawyers and Klaus’s copy editor; a council lawyer steps forward, and the night swells with fast typing — possibility becomes process."
        "Say nothing, and ask for a written amendment to be vetted later":
            "You bite your lip and push the paper back toward Irene, buying time but not certainty. The delay tastes like a cautious truce."

    menu:
        "Accept the funded barrier deal with guaranteed pilot and housing protections.":
            jump chapter12
        "Refuse the deal; demand enforceable legal guarantees and community veto.":
            jump chapter15
        "Broker Elliot’s phased hybrid plan as a third way, asking for rapid pilot approvals.":
            jump chapter12
    return
