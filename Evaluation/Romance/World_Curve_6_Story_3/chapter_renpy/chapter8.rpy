label chapter8:

    # [Scene: Port Veridian Harbor | Morning]

    scene bg ch7_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low mechanical thrum of dredgers, gulls calling, ropes creaking]
    # play music "music_placeholder"  # [Music: Warm, rising strings — a steady, hopeful motif]
    "You are standing on the slick edge of the dock with your satchel heavy against your hip, the sea-glass pendant cold at your throat. The decision you made in the council still sits like an afterimage"
    "behind your eyes — a brace and a promise both. Machinery thumps in time with your pulse: hulks of steel churning the estuary, pilings being driven like new ribs into the shoreline."
    "Salt and diesel braid in the air. The smell is sharp and honest; it means work, wages, roofs held down tonight. Neighbors cluster along the quay, faces salted with relief. A line of nets is hauled"
    "aboard an old trawler and, for the first time in months, glints of fish tumble into a wooden crate. People laugh a little too loudly; someone cries, then laughs again."

    scene bg ch7_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Noah Rhee’s voice, rough but steady over the machinery]
    show noah_rhee at left:
        zoom 0.7

    noah_rhee "Tie off that boom. Hold it steady—Marisol, you on the pumps. This is our shot today."
    "You move forward and he looks up at you — the expression is that complicated kind of gratitude someone born of the sea shows: spare, brittle, and real."

    noah_rhee "You did this, Maya. You stood with us. I know what that meant."
    "You want to say it's not just you. But you also know the scaffolding of this morning was built by contracts and concrete and a lot of hands that wanted immediate shelter. You close your fingers around the strap of your satchel and let the present hold you."
    show maya_ibarra at right:
        zoom 0.7

    maya_ibarra "We needed steady nets and hungry mouths fed, Noah. You and the crews gave people that back. We'll keep watching the cost."

    noah_rhee "Cost. Yeah. We'll watch, eh? But don't talk to me about marshes when a kid's dinner is on the line."
    "The exchange is rough but not hostile. There is a recognition between you: survival for now. He turns back to the crew, barked orders resuming. The machines bite into silt."

    menu:
        "Join the crew hauling nets":
            "You drop down beside the fishermen, hands slick with fish and rope; the effort is physical and immediate, and a dockhand thanks you with a crooked grin."
        "Head to the Tidewatch Lab to check sensor readouts":
            "You race back to the lab, mud streaking your boots, and the sensor dashboards glow with new churned data — a pulse of altered salinity and turbidity that needs interpretation."

    # --- merge ---
    "'You decide—briefly—what kind of presence you'll be this morning. Either way, the town's rhythm has shifted: engines, work, mouths fed.'"
    # [Scene: Construction Site — Near the breakwater | Midday]
    hide noah_rhee
    hide maya_ibarra

    scene bg ch7_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Pounding impacts, the metallic clang of the pile driver, distant conversation]
    # play music "music_placeholder"  # [Music: Light percussion with hopeful woodwinds]
    "Elliot Chen arrives with his sketch cloth rolled under one arm, damp at the edges. He walks between rows of equipment like someone walking through a gallery with mixed feelings about the exhibition. His eyes are"
    "bright but there is an edge — a small fracture that you can see when light hits his face."
    show elliot_chen at left:
        zoom 0.7

    elliot_chen "You knew they'd move fast."
    show maya_ibarra at right:
        zoom 0.7

    maya_ibarra "They needed to. People are tired of waiting."
    "He studies the pilings, the way the shadows fall between them, then looks at you."

    elliot_chen "—I helped map where they were driving. We can do this smarter than just brute force."
    "Dialogue between you stretches, a careful rope between two wills."

    maya_ibarra "That's the thing. You can help. Your plans could make this less destructive."

    elliot_chen "And you'll keep pushing for monitoring? For mitigation? For… options?"

    maya_ibarra "Yes. If you're willing to stay."
    "He hesitates. The hurt in him isn't only professional; it is personal — a small thing you didn't plan to fracture when you chose the immediate work. He looks away toward the estuary where the shoreline has been altered by the machine's teeth."

    elliot_chen "I never wanted to be the person who watched a town choose comfort over its future."

    maya_ibarra "You're not that person. Help me make sure this comfort doesn't become permanent harm. Help me set the rules."
    "He runs a hand through damp hair, then nods once, a little stubborn, a little brave."

    elliot_chen "Alright. I stay. But I'm not just consulting — I'm on the decks, Maya. If this slips into mistake, we call it out. No soft-peddling."
    "You both turn toward the work as if agreement itself can be an anchor."
    hide elliot_chen
    hide maya_ibarra

    scene bg ch7_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Her voice, crisp, carrying above the machinery]
    show dr_kira_ansel at left:
        zoom 0.7

    dr_kira_ansel "The initial reductions in turbidity are promising where dredging hasn't gone—' (she stops, gauging the scene) '—but we must be clear-eyed. Habitat loss isn't a distant event; it's immediate when you shift currents and displace sediments."
    "Noah Rhee, overhearing, rounds on her with the bluntness of someone who measures time in tides not models."
    show noah_rhee at right:
        zoom 0.7

    noah_rhee "We know what happens to folks when the nets stop coming in, Doctor. That isn't 'distant' for me. My sister's got three mouths to feed."

    dr_kira_ansel "And I'm not unsympathetic. But if you're asking me to choose a side, I will instead offer to design monitoring that can be acted upon. Let me show you what the trade-offs actually look like in the data."
    "Aria Sol arrives from the edge of the fenced development site — polished, efficient, a smile like a business card."
    show aria_sol_representative_of_veridian_holdings at center:
        zoom 0.7

    aria_sol_representative_of_veridian_holdings "This is progress. Contracts signed, jobs standing. Veridian Holdings will ensure the town never has to beg for permits again. Think long-term security."
    "The group pivots into a tense, multi-layered conversation: money and ethics, urgency and stewardship. Voices overlap, sometimes interrupting."

    noah_rhee "We don't need lectures about 'habitat' when the water takes the house."

    aria_sol_representative_of_veridian_holdings "We are offering guarantees—insurance, infrastructure, predictable employment."

    dr_kira_ansel "Guarantees that erase functions of the estuary are not guarantees at all; they're transferences of risk to future generations."
    hide dr_kira_ansel
    show elliot_chen at left:
        zoom 0.7

    elliot_chen "Then help us make guarantees that are conditional. Let monitoring dictate further steps. Let us build feeders—small, adaptive interventions that can be removed or amended."
    "You watch each face because each carries the town's future in their hands at this moment. The machines keep working. There is a hum of potential: people earning paychecks, kids being watched less anxiously by their parents, kitchens lit that would have been dark."

    menu:
        "Counter Aria's pitch with a public appeal to keep local oversight":
            "You step onto a crate and speak to the crowd, your voice ringing across the docks; people listen, some nodding, some furrowing brows—your words reframe the contract as a conditional partnership."
        "Ask Dr. Kira to set up immediate environmental monitoring and announce it publicly":
            "You invite Dr. Kira to the makeshift stage and she outlines a real-time monitoring plan that calms some fears and angers others, but gives a clear mechanism to hold armoring to account."

    # --- merge ---
    "'You take a breath and choose where to direct the day's moral energy: into public pressure or into technical guardrails. Either path pulls together different parts of the town.'"
    # [Scene: Estuary Edge / Reclaimed Shoreline | Late Afternoon]
    hide noah_rhee
    hide aria_sol_representative_of_veridian_holdings
    hide elliot_chen

    scene bg ch7_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A calmer tide; distant laughter; the soft clink of rigging]
    # play music "music_placeholder"  # [Music: Swelling strings with a hopeful undertow]
    "By afternoon the harbor has steadied in a way it hasn't in a season. The pilings have created lee where the sea slaps less fiercely. Boats sit more even in their slips. Nets are mended; hatches"
    "close heavy with haul. An older woman presses a wrapped bundle into your hands — warm bread, eyes bright with gratitude. A teenage boy gives you a thumbs-up. The immediate math is simple and human: bellies"
    "full, rent paid, a school uniform replaced."
    "The town's bar—temporary tables set under a tarpaulin—turns into an impromptu village square. People swap stories, trade tools, and talk about the first paychecks. The atmosphere is buoyant and raw; relief lubricates the edges of exhaustion."
    "You feel it inside you — an upwelling of careful joy. You had feared this choice would bury you under guilt; instead it has opened a corridor of possibility. Not absolution, but a breathing space in"
    "which negotiation can happen. The work people are doing is not a betrayal of the future; it is a lifeline that must be knotted to stewardship, not cut loose to wash away."
    "Elliot Chen sidles up to you with staining on his palms and a smudge of grease on his cheek. He offers a small, sardonic grin."
    show elliot_chen at left:
        zoom 0.7

    elliot_chen "Not the plan I drew, but it's keeping people fed."
    show maya_ibarra at right:
        zoom 0.7

    maya_ibarra "It's ugly and necessary."

    elliot_chen "Ugly can be fixed if we keep the right eyes on it."
    "He pats the strap of your satchel — a private encouragement. Dr. Kira Ansel stands nearby with a tablet full of site maps; her posture is tired but determined."
    show dr_kira_ansel at center:
        zoom 0.7

    dr_kira_ansel "If we set baselines now, if we get the monitoring in place and the community trained to read it, we can catch the worst of it. We can ask for incremental adjustments."
    hide elliot_chen
    show aria_sol_representative_of_veridian_holdings at left:
        zoom 0.7

    aria_sol_representative_of_veridian_holdings "And Veridian Holdings will fund the first year of monitoring. We want this to demonstrate stability. There's a benefit to that."
    hide maya_ibarra
    show noah_rhee at right:
        zoom 0.7

    noah_rhee "Fine. But any monkey business, and I'm taking my crews and going. People need certainty."
    "You look between them — the city's funding, the scientist's caution, the fisher's demand for certainty, your friend Elliot's guarded hope. Each holds a part of the solution. Your chest tightens at the moral calculus, but your voice is steadier than it was that morning."
    hide dr_kira_ansel
    show maya_ibarra at center:
        zoom 0.7

    maya_ibarra "We have a window now. People are less hungry. We can use this momentum to set rules, not just build walls."
    "The murmurs around you lean toward agreement. There is energy: people who had been arguing for months now stand shoulder to shoulder building something together. Tension remains, but the air tastes of salt and possibility. You"
    "do not forget the marshes — you can still smell them in your mind, see the reeds bending — but you also see a child with warm bread, a neighbor sleeping without fear."
    "Inside you, two truths sit: some protections must be immediate, and protections must also be accountable. The rising chord in the town today is not resolution; it is the beginning of a contract you will have"
    "to translate into practice. The harbor is functioning again, and with it comes political capital you can spend — to save what you can and to shore up what you must."
    hide aria_sol_representative_of_veridian_holdings
    hide noah_rhee
    hide maya_ibarra

    scene bg ch7_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Strings swell into a major chord, light percussion marking forward motion]
    "This is the moment to decide how momentum becomes policy. You can lock in hard armor; you can split gains to begin a restoration trial; or you can force negotiation now, using this success as leverage for a hybrid that binds immediate work to strict monitoring."
    "You inhale the salt and diesel and hope together."

    menu:
        "Make the armoring permanent and expand dredging for more immediate security.":
            jump chapter9
        "Allocate some profits to funding a parallel marsh-restoration trial while continuing the armoring.":
            jump chapter11
        "Use the momentum to force a negotiated hybrid plan with Elliot's team and strict environmental monitoring.":
            jump chapter17
    return
