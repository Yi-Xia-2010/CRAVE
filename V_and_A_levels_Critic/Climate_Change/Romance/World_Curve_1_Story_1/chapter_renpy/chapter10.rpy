label chapter10:

    # [Scene: City Hall Meeting Room | Dusk]

    scene bg ch10_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Urgent, lilting strings under a steady percussive heartbeat]
    # play sound "sfx_placeholder"  # [Sound: Rain against glass as a tight, metallic drumroll; distant traffic hush]
    "You take the chair opposite Irene Voss and feel the tilt of the room settle onto your shoulders — not hostile, not warm, but expectant in a way that carries consequence. The city's fatigue hangs in"
    "the air like humidity: everyone's done with endless plans that never outlast the next storm. That fatigue makes money look like water-breathing — real, essential, a thing some people can finally take in."

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A soft, practiced click as Irene Voss sets her tablet down; the click a punctuation mark]
    "Luca's glossy model sits between you: a miniature horizon of concrete ridges, gleaming membranes, and neat little parks suspended like afterthoughts. It smells faintly of new plastic and lacquer — the city translated into a promise you can hold."
    show irene_voss at left:
        zoom 0.7

    irene_voss "Maya, we're at the edge of what delay can buy us. The proposal protects critical infrastructure and—"

    irene_voss "—it keeps households from being uprooted in the immediate term. We need scale, and we need it fast."
    "You swallow. Her words are measured; they are built to carry weight. You can see why the council listens. The ledger beside her is already populated with figures and timelines that read like inevitability."
    show maya_rios at right:
        zoom 0.7

    maya_rios "Fast has to mean thoughtful,' you say. 'There have to be guardrails. Community oversight. Housing protections. A clause for living infrastructure pilots. If we're doing this together, those lines aren't negotiable."
    hide irene_voss
    hide maya_rios

    scene bg ch10_453e40_3 at full_bg
    show luca_marin at left:
        zoom 0.7

    luca_marin "Of course. We're not here to bulldoze community spirit. We can build in pilots. Timelines, however, are non-negotiable. Contractors need clarity to mobilize. Delays cost lives and budgets."
    show dr_noor_patel at right:
        zoom 0.7

    dr_noor_patel "And yet history shows top-down barriers often fail on ecological timelines. Materials corrode, maintenance budgets evaporate. Without living systems integrated from the start, you buy time at a future's expense."
    "The name of the future you fear — displacement, ecological brittleness — sits like a stone in your throat. But there are faces in the room with you: neighbors in rain-slick jackets, Sami's thin jawline at"
    "the far end, Elliot Chen leaning back with an unreadable stillness. They each anchor the ledger to human stakes."
    # play sound "sfx_placeholder"  # [Sound: A murmur — a neighbor, low]

    "Neighbor" "We need the street fixed before the next king tide. My little girl sleeps in a bag of sandbags every spring."
    "The room's pressure sharpens. You can feel the city's appetite for something that moves. Hope rises in you with the same quickness as dread: money and mobilization would mean some people sleep in dry beds this season. That is a thing that matters."
    show maya_rios at center:
        zoom 0.7

    maya_rios "If this moves forward, those clauses are how we keep you from staging repairs that displace families. Housing protections — enforceable. Community oversight — real seats gained, not token meetings. Living infrastructure — a binding pilot scope with benchmarks."
    "Irene Voss studies you a long fraction of a breath. The mother-of-pearl brooch is a comet in her lap as she nods."
    hide luca_marin
    show irene_voss at left:
        zoom 0.7

    irene_voss "We can include oversight. We can ring-fence funds for pilot work. But deadlines compress. Contractor oversight becomes strict because there isn't room for iterative delays. I can agree to benchmarks, but we set penalties for missed milestones. The city's ledger doesn't allow indefinite piloting."
    "You can hear the math in her phrasing — an arithmetic of crisis that treats concessions as additions on a tight budget, not as part of the project itself. The fight is about whether living systems are marginal or central to what the city will accept as 'safe.'"
    hide dr_noor_patel
    hide maya_rios
    hide irene_voss

    scene bg ch10_453e40_4 at full_bg
    "Your fingers brush the notebook unconsciously. It holds community lists, the names of households who cannot relocate, a map of pilings and children you promised to protect. Each clause you allow could be the difference between a family's roof and a corporate relocation offer."

    menu:
        "Tap the notebook with your knuckle":
            "You tap the notebook once, a private signal that counts—discipline, memory, a small pledge. It steadies your voice."
        "Fold your hands flat on the table":
            "You flatten your palms to the wood, feeling its cool grain. It grounds you; you can taste the iron tang of determination."

    # --- merge ---
    show irene_voss at left:
        zoom 0.7

    irene_voss "You're asking for community power. Good. I'm not opposed to it. But understand: every seat you win at oversight, we will constrain in scope. The council needs auditability, predictability. We will bring on contractors with track records. Delays will be costly."

    irene_voss "You're asking for community power. Good. I'm not opposed to it. But understand: every seat you win at oversight, we will constrain in scope. The council needs auditability, predictability. We will bring on contractors with track records. Delays will be costly."
    "Elliot Chen speaks up for the first time, and when he does, there is warmth in his voice that cuts through the tension."
    show elliot_chen at right:
        zoom 0.7

    elliot_chen "We can set milestone benchmarks that include ecological performance, not just build-time. Living pilots can be integrated into the first phase if there's a shared maintenance fund—trained community teams funded through initial contracts."
    show luca_marin at center:
        zoom 0.7

    luca_marin "Designing consensus is lovely. Funding maintenance is less so. Voters want walls and dry streets, not theory. The simplest way to reassure the market and the bank is to show a robust, fast barrier. Then we layer in pilot programs as separate budgets."
    hide irene_voss
    show dr_noor_patel at left:
        zoom 0.7

    dr_noor_patel "Separate budgets often become afterthoughts. They get cut when the first maintenance cycle hits. Integrating living infrastructure into the primary contract is the only way to ensure ecological uptake."
    "You feel the pitch of the exchange rise: words like 'integrate' and 'fund' become tools against one another. The room is fastened to a single hinge — either the city takes a posture of rapid, centralized defense or it folds complexity in from the beginning."
    hide elliot_chen
    show maya_rios at right:
        zoom 0.7

    maya_rios "Integration, not afterthought. Binding, enforceable contracts for housing protections. Community seats not advisory—real veto power on demolition within the first three miles of the coast. And pilot projects in three neighborhoods, including Harborfront."
    hide luca_marin
    show irene_voss at center:
        zoom 0.7

    irene_voss "Three neighborhoods is ambitious. Two is fiscally safer. We can set parameters for Harborfront as conditional—if community teams meet training benchmarks within forty-five days."
    "The clock in your chest accelerates. Forty-five days to train teams across neighborhoods with different capacities—it's possible with the Spire's networks, but it will be brutal. Hope sparks: if this passes, the living pilots get real"
    "funding. Skepticism claws at the edge of the hope: if you accept too many constraints, oversight becomes oversight in name only."

    "Neighbor" "Please. People are out there now. If this is about politics, we don't have time. Do it right, but do it now."
    "Sami's hand finds yours on the table — a brief contact. You feel the current of trust that is older than this negotiation: a childhood promise. It steadies you."

    menu:
        "Squeeze Sami's hand briefly":
            "You give a short, tight squeeze. It says what words won't—remember what's at stake. Sami's jaw loosens with relief."
        "Withdraw your hand and keep the pressure in your voice":
            "You pull your hand back and let the argument carry the weight. Sami nods, taut but trusting your lead."

    # --- merge ---
    hide dr_noor_patel
    show elliot_chen at left:
        zoom 0.7

    elliot_chen "If we get funds, we have to hire locally and train locally. I can run the training curriculum from the Spire, and we'll publish benchmarks publicly. Transparency isn't optional."

    elliot_chen "If we get funds, we have to hire locally and train locally. I can run the training curriculum from the Spire, and we'll publish benchmarks publicly. Transparency isn't optional."
    hide maya_rios
    show luca_marin at right:
        zoom 0.7

    luca_marin "Public dashboards are great theater. They don't fix money gaps."

    irene_voss "This is the compromise I can carry into the council. Two pilots guaranteed, Harborfront conditional, forty-five day training window for community teams, strict contractor oversight with penalties for missed milestones. We accept living infrastructure as part of the initial program, but it cannot delay core barrier production."
    "You feel hope — small and specific — rise like brackish green in a gray tide. It's a concession, but it contains scaffolding for what you've been fighting for: community power in the center of implementation."
    "The price is abbreviated timelines and the rigor of contractor oversight — controls that could clamp down on creativity or freeze budgets for maintenance."
    "Your throat is a dry coil. You think of the ledger again: numbers that promise immediate shelter, sap that might bleed away the community's agency over time. You think of your brother — the small violences"
    "storms can visit in an instant — and of the neighbor's sleeping bag of sandbags. There is no single, clean answer. There is only navigation."
    "Irene Voss slides a printed memorandum across the table; the paper is glossy, the clauses tight and legal in their breath."
    hide irene_voss
    hide elliot_chen
    hide luca_marin

    scene bg ch10_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Strings rise to a tense, hopeful peak; percussion quickens]
    # play sound "sfx_placeholder"  # [Sound: The soft rustle of paper, the room holding its breath]
    show irene_voss at left:
        zoom 0.7

    irene_voss "Sign here to authorize the project entry to council. The motion includes the two guaranteed pilots and the Harborfront conditional clause. It bonds the city's funds with contractor commitments and oversight penalties. It is the window we have."
    "You can see the pen beside the line, waiting like a tide mark. Your fingers hover above it, an almost physical negotiation between hope and caution."

    "Dr. Noor's voice comes back to you, remembered and present both" "Top-down works when it's adaptive. But adaptation needs permission to learn from failure. Make the contract learnable."
    "Elliot Chen watches you, his expression unreadable until it isn't: his pupils catch the lamp like green bay lights."
    show elliot_chen at right:
        zoom 0.7

    elliot_chen "If you sign this, make the benchmarks public and legally binding. If you don't, we risk losing the window. Either way, we hold the city accountable."
    "Your breath comes fast. The room's noises compress — rain, a distant siren, the tiny click of a projector warming. Hope and pressure braid together: signing could mean roofs stay on heads; it could also mean ceding long-term guardianship. Your hands tremble slightly above the paper."
    hide irene_voss
    hide elliot_chen

    scene bg ch10_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Crescendo, then a held single note]
    "You remember the bench at the Spire, the practice of opening your mouth to ask for help. This moment is that same hinge: asking for help — from the city, from contractors — or insisting on purity and risking paralysis."
    show maya_rios at left:
        zoom 0.7

    maya_rios "I won't sign blind. I will sign if the pilots are integrated, if oversight is real, and if housing protections are legally enforceable. And we make the benchmarks public."
    "Irene Voss studies the memorandum, then meets your gaze with the kind of appraisal that has moved policy. Her face is unreadable in the half-light — complex, professional, offering both admission and a dare."
    show irene_voss at right:
        zoom 0.7

    irene_voss "We'll take it to the council with those addenda."
    "The ledger is handed to you now in a way that makes the room breathe differently. This is not a capitulation or a triumph yet; it's a pressure point, a vessel that will be filled by the signatures and the ink that follows."
    hide maya_rios
    hide irene_voss

    scene bg ch10_453e40_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain intensifies to a steady, urgent drum; footsteps in the corridor faintly echo]
    "Your heart ratchets. This is the city's hinge — a decision that will be preached in council chambers, in living rooms, on the Spire's bulletin. You feel the weight of names, the gravity of pilings and promises."
    "You look up. Elliot Chen's mouth is a thin line; Sami's eyes are raw and bright; Dr. Noor's hand rests on a folio of weather logs like a benediction. Irene Voss watches with that appraisal-turning-invitation stare. Luca leans back, professionally pleased, the model gleaming."
    "Everything narrows to the pen at the edge of the world."

    scene bg ch10_453e40_8 at full_bg
    # play music "music_placeholder"  # [Music: Single held chord; then silence — the moment pregnant]

    scene bg ch10_453e40_9 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter11
    return
