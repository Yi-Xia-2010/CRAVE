label chapter2:

    # [Scene: Verdante City Hall Plaza | Early Evening]

    scene bg ch2_c4ca42_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, steady synth underscoring—measured, civic]
    # play sound "sfx_placeholder"  # [Sound: Murmured conversation, the soft clatter of a rainstick umbrella, distant gull calls]
    "You step off the damp curb and into the plaza where the city has gathered: folding chairs arranged in civic rows, a scattering of placards, and a ring of cameras. The air smells of rain and"
    "hot concrete—ozone along with the faint, greasy sweetness of street food from a vendor at the edge of the square. Your coral scarf is still damp at the fringe where you tucked it last night; it"
    "sits like a familiar punctuation against the newness of municipal lighting."
    "A large screen hangs over the dais. Cyan lines and smooth polygons hover beyond the speakers' heads: Verdante's coastline, reimagined in phased blocks and labeled timelines. The HUD feels like a promise stitched in light."
    show elias_moreno at left:
        zoom 0.7

    elias_moreno "Thank you for coming. What you'll see tonight is a municipal overlay—phased defenses, prioritized zones, adaptive modular sections that can be deployed as funding arrives. It's designed to scale, to be replicable across other coastal cities."
    "You listen. The renderings glide: turbines tucked into piers, raised promenades, data layers that count economic risk in tidy blocks. The language is technical, and the tone is optimistic—efficiency, resilience, deployable within a municipality's fiscal year. It hums with the faith of someone who trusts plans."

    elias_moreno "Phase one secures critical infrastructure—power, hospital access, the ferry lines. Phase two extends living shorelines where possible and builds modular cantilevers for market access. Phase three is a citywide retrofit fund. We can protect thousands if we sequence correctly."
    "You can see why people take comfort in the geometry on the screen—the lines make hazard into something manageable. Your chest tightens in an even, practical way: not outrage, not surrender, but the steady friction of"
    "two truths pressed together. The renderings allocate blocks where Mariner's Row sits in reality; the diagrams reduce porches and family plots to numbered zones."
    "Lina approaches and falls into step at your shoulder, boots spattered with yesterday's tide. Her voice is small but edged."
    show lina_cortez at right:
        zoom 0.7

    lina_cortez "They make it look so clean. Like you can just 'zone' a life away."
    "You glance at her; she taps the edge of the projection with a gloved finger—no imprint, only a faint-blue wash. Her braid is damp. Behind her, Tamiko adjusts a camera strap with a practiced hand, already framing the feed to catch nuance that the municipal cameras won't."
    show tamiko_sato at center:
        zoom 0.7

    tamiko_sato "They'll spin it as compassion—save the city, and tough choices follow. We need to make sure 'tough choices' don't become eviction orders."
    "Dr. Arun steps forward with a tablet heavy with annotated data. He folds his hands as if to steady the numbers."
    hide elias_moreno
    show dr_arun_patel at left:
        zoom 0.7

    dr_arun_patel "Engineering solves hazards, yes. But adaptation without tenure protections and participatory governance creates new vulnerabilities. Structural solutions must be negotiated socially, or they fail long-term."
    "Elias listens to all of them, fingers resting on the podium as he toggles between overlays. His voice softens when he looks your way—there's a bridge there, an unspoken attempt to translate. He is earnest; you"
    "feel that. But earnestness doesn't answer the lived detail: someone's shed, the smell of an oiled fishing net, a child's chalk drawing that will vanish under a constructed promenade."
    hide lina_cortez
    show elias_moreno at right:
        zoom 0.7

    elias_moreno "Mira—these proposals include community consultation periods. We can embed social housing in the planning. I—"
    "You find yourself interrupting, not maliciously but with a clarity that rises from memory."

    "You" "Consultation periods are not the same as power-sharing. You can schedule a meeting, but the timelines and funding commitments leave little room for the messy, slow work that keeps a neighborhood intact."
    "Elias shifts, not defensive but surprised—his eyes narrow as he reorients to the human variable rather than the diagram."

    elias_moreno "I know you're right about the mess. I also know what's at stake if we wait. If we don't act at municipal scale, the next storm will take what we won't have secured. I want both—efficiency and justice. Help me find the design that does both."
    "He says 'help' with an openness that pins you somewhere between ally and adversary. Your instincts want to list conditions: tenure guarantees, phased community-controlled work, transparent contracting. But the room is not yours to fix alone."

    menu:
        "Ask Elias for a specific guarantee—tenure protections now":
            "Your voice is precise, the terms you want already formulated in your head. Elias pauses, brows pulling together; you see the data streams in his eyes flick as he calculates political and budgetary constraints."
        "Reserve the terms; press for broader public process":
            "You take a quieter tack. You talk about process—more public hours, neighborhood design workshops, binding oversight committees. Elias nods slowly; he looks relieved by the procedural route but also wary of timelines."

    menu:
        "Offer to co-chair the community oversight committee":
            "You volunteer. The plaza quiets for a heartbeat; Elias's relief is a small thing but visible—an unclenching at his jaw. Lina squeezes your hand in solidarity."
        "Ask for more time to consult neighbors before committing":
            "You ask for time. The request is procedural, stabilizing—Elias accepts deferment with a nod, though you can see the deadline clock ticking on his face."

    jump chapter3
    return
