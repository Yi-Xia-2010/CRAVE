label chapter10:

    # [Scene: Commerce Strip Field Office | Morning]

    scene bg ch10_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Up-tempo strings with a driving percussion undercurrent]
    # play sound "sfx_placeholder"  # [Sound: Distant jackhammers, the murmur of a crowd, paper rustling]
    "You arrive before most people do, rain still dampening the cobbles. Your hands smell faintly of coffee and tide—an old, familiar mix that steadies you. The proposal sits as if waiting: a sleek slide deck on"
    "Mira Chen's tablet, budget lines highlighted, timelines mapped in clean type. The numbers look like a promise. The promise settles in your chest like a stone made lighter by someone else's hand."
    show mira_chen at left:
        zoom 0.7

    mira_chen "Maya—"

    mira_chen "We can start next week. Full crews, guaranteed payroll, compliance checked. This isn't just concrete; it's payroll and insurance and immediate safety."
    show maya_ortega at right:
        zoom 0.7

    maya_ortega "Immediate safety—' (you swallow) '—and immediate disruption. How fast are we talking?"

    mira_chen "Forty-eight-hour mobilization. Piles in place within three days. The temporary boardwalk goes up the same week to keep Commerce traffic moving. You'll see results before the next storm cycle."
    "Councilwoman Tamsin Hale stands slightly behind her, hands folded, eyes like a pair of lenses. She doesn't need to say the math out loud; the wash of relief on the faces in the crowd already does some of her work."
    show councilwoman_tamsin_hale at center:
        zoom 0.7

    councilwoman_tamsin_hale "We secured a contingency fund for small-business transition. We can adjust fascia and vendor placement—within limits. The project is accountable and fast."
    "The word 'fast' hums in you. Fast means fewer nights cutting sandbags, fewer emails to overwhelmed insurers. Fast means people can sleep without nightmares about flooded basements. You think of Luca's call last week—Luca with a"
    "new scar across his knuckle from hammering a failing threshold back into place. The ledger of what you owe your town is long, and tonight numbers feel like a ledger you can finally balance."
    "Elias Voss appears at your shoulder, soil still under his nails from an early morning at the bakery-turned-popup stall. He wears optimism like a jacket, patched and practical."
    hide mira_chen
    show elias_voss at left:
        zoom 0.7

    elias_voss "If this goes in, I can carve vendor spaces into the plan—priority leases for locals, discounted rates for six months. It won't be perfect, but it's something."

    maya_ortega "Something is a place to start.' (you press your fingers against the compass at your throat) 'Mira, the ecological impact—are there mitigations for the marsh edge?"
    hide maya_ortega
    show mira_chen at right:
        zoom 0.7

    mira_chen "We can add engineered wetland buffers in phases. But the priority is structure. The faster we seal the line, the fewer catastrophic breaches. The buffers can be integrated—after the initial stabilization."
    "You can hear the urgency in her cadence. It asks you to choose a rhythm: immediate safety now, ecological nuance later. Your chest is claustrophobic and, oddly, light with the arithmetic of relief."

    menu:
        "Ask Mira Chen to show the phased mitigation timeline now":
            "Mira Chen pulls the slate closer and scrolls, laying out stepwise wetland work—timelines, contractors, contingencies; you feel the shape of possibility widen."
        "Let Elias Voss and Councilwoman Tamsin Hale handle the vendor negotiations, and take care of community outreach":
            "Elias Voss meets your eyes, nods, then steps forward to speak to a clustered group of merchants; you sense the arc of shared labor, and an ache in your ribs softens into a workable plan."

    menu:
        "Walk the line and speak to the marsh restoration team":
            "You step carefully between stakes and mud, feeling the give of peat under your boots. The restoration team points out vulnerable root systems and lists small design shifts that could save plant beds—your mind begins counting tradeoffs."
        "Attend the engineer's meeting to press for amendments directly":
            "You sit at the metal folding table, meet the engineers eye-to-eye, and feel the cadence of negotiation quicken; technical terms throw sparks, but you notice a crack where a compromise might fit."

    menu:
        "Insist on design amendments that include tidal gardens":
            jump chapter13
        "Accept the standard build for immediate safety and funding":
            jump chapter14
        "Negotiate community oversight panels to monitor implementation":
            jump chapter15
    return
