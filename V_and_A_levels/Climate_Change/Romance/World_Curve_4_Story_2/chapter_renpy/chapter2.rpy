label chapter2:

    # [Scene: Rooftop Garden Resilience Hub | Afternoon]

    scene bg ch2_c4ca42_1 at full_bg
    # play music "music_placeholder"  # [Music: Gentle, optimistic strings; steady tempo]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, low murmur of arriving voices, a drip from a greenhouse pane]
    "You are halfway through setting the last chair when the room fills: neighborhood representatives, scientists, engineers, and activists settling into the amber light. The air smells of wet soil and salt, a comfort that steadies your"
    "pulse. You press the satchel strap against your chest, feeling the folded schematic like a heartbeat."
    show maya_soren at left:
        zoom 0.7

    maya_soren "Thank you all for coming. We'll keep this focused — models, trade-offs, labor and governance. We'll log everything on the hub registry and commit to transparency."
    "You fold your hands on the table and let the first sentences hang, a clear brace against the inevitable tension beneath the polite greetings. Eyes sweep to you: Dr. Lena Huang's measured gaze, Elias Voss's half-smile"
    "that wants to be brave, Asha Reed's folded arms, Jonah Mek's steady presence, Rosa Calder's small, watchful nod. Their faces read like the bay at low tide — familiar contours and hidden undercurrents."
    show dr_lena_huang at right:
        zoom 0.7

    dr_lena_huang "I'll begin with the science. The kelp-sea wall hybrid has promise for sediment capture and wave attenuation, but there are trade-offs. Introduced structures change current patterns; kelp monocultures can stress local trophic dynamics. We can't treat this as a silver bullet."
    "You hear the soft clack of a tablet as Lena pulls up a projected model. Her voice is crisp, clinical, but not cold — the tone of someone who has weighed consequence and wants the room to do the same."
    show elias_voss at center:
        zoom 0.7

    elias_voss "Favouring caution doesn't mean doing nothing, Lena. The pilot can be staged, monitored. We design for modularity — panels that can be adjusted, kelp beds in staggered plots. We gather data, iterate. I can work with Dr. Huang on the monitoring protocol."
    "Elias Voss's hands move while he talks, sketching the hybrid on the table in quick, patient strokes. There's earnestness in the motion — the kind that used to get him scolded as a kid for taking"
    "apart clocks to see how the hands would move. His voice softens when he looks at you, only for a beat, and you can't tell if the look is concern or faith. It sits between the"
    "two — complex and warm."
    hide maya_soren
    show asha_reed at left:
        zoom 0.7

    asha_reed "We don't need another airborne 'pilot' that ends up as a PR case. We've seen projects come in, displace gardens and elders, and leave a scaffold of broken promises. Who benefits when the data looks good but the people on stilts get boxed out?"
    "Asha Reed's words land like a flare; the room tightens. Her eyes are direct, insisting that the cost be measured in human care, not just metrics. She leans forward, voice pitched low so the words are for the room alone."
    hide dr_lena_huang
    show jonah_mek at right:
        zoom 0.7

    jonah_mek "Asha's right. My cousin runs a hardware coop in Lower Quay — he can't afford to be knocked back twice by a demo that demands leverage we don't have. If a pilot requires land seizures or exclusive contracts, it won't be the 'community' protecting us. It'll be people with money."
    hide elias_voss
    show rosa_calder at center:
        zoom 0.7

    rosa_calder "You all talk of 'adaptive strategies' like sewing new buttons on a coat. Those buttons are my neighbors' kitchens. If you bring metal and machines without promises to keep hands on the work — and pockets left intact — I will plant on your installations."
    "The voices overlap, building a knot of worry and righteous caution. You feel the room's energy rise: not panic, but a clear, mid-level pressure that demands action and clarity."
    hide asha_reed
    show maya_soren at left:
        zoom 0.7

    maya_soren "We hear that. I know the history — the garden that had to move, the shops that closed. Any pilot must be co-designed, with labor guarantees and retainers for local vendors. No exclusive contracts that lock out community ownership. Transparency and enforceable terms."
    "You lay out the first anchor — governance terms you committed to last session. The hub's registry syncs with your words; a live list appears on the table's projection: community labor quotas, open-access data streams, staged monitoring, dispute resolution steps. The projection glows like a promise you can point to."

    menu:
        "Ask Elias to explain the staging in layman's terms":
            "Elias Voss relaxes into the explanation, using a string of simple analogies — tide as a slow breath, kelp as webbing that slows the outflow. People nod; the schematic doesn't feel like jargon anymore."
        "Invite Rosa to name non-negotiables for the community":
            "Rosa Calder straightens, voice steady. She lists childcare protections for community workers, a clause ensuring local hiring for maintenance, and a seed-fund for displaced gardeners. Each item shutters down corners of the room into quiet agreement."

    # --- merge ---
    "You let both threads breathe into the conversation. The projection rolls a new field: social safeguards. Elias Voss's plan is more tangible now that it answers everyday needs; Rosa Calder's list roots the pilot in repair,"
    "not replacement. The room shifts from debating whether to pilot toward how — and your chest loosens with the small, sharp relief of forward motion."
    hide jonah_mek
    show dr_lena_huang at right:
        zoom 0.7

    dr_lena_huang "If we proceed, we must commit to adaptive monitoring: baseline surveys, monthly current profiling, biodiversity indices. If early signs show adverse effects, we must have protocols that can pause or reconfigure the structure. That's non-negotiable scientifically."
    hide rosa_calder
    show elias_voss at center:
        zoom 0.7

    elias_voss "Agreed. And operationally, the Aster can run seasonal demos — deploy sensors, map sediment changes, sample kelp genetics. We'll keep modules small and reversible."
    hide maya_soren
    show asha_reed at left:
        zoom 0.7

    asha_reed "Reversible means someone has to pay for that reversal. How do you fund the rollback? Who is accountable? History shows 'reversible' becomes 'too expensive'."
    hide dr_lena_huang
    show maya_soren at right:
        zoom 0.7

    maya_soren "We write rollback funding into the pilot budget. We create escrow tied to community oversight. We don't let 'too expensive' become an excuse for inaction or displacement."
    "Jonah Mek: (quietly) 'And what about labor? You lock in community folks for a 'trial' and then the contractors swoop in to maintain it. We need training and wages, not unpaid labor in the name of 'participation'.'"

    elias_voss "We'd never — I mean, the maintenance plan includes paid positions for locals, apprenticeship slots, and a rotating ops committee that includes Lower Quay representatives."

    asha_reed "I'll hold you to that. If you want my coalition's buy-in, community sovereignty has to be central, not an afterthought."
    "Your role tightens: mediator, guarantor, the voice that stitches technical detail to communal needs. You feel a familiar weight — responsibility that could chafe into isolation if left unchecked — but today it feels shared. The"
    "hub's translucent domes collect the light and soften the edges of disagreement into workable compromises."

    menu:
        "Propose the Aster demonstration within two months":
            "A ripple of approval spreads. Elias Voss pulses with visible relief, Jonah cracks a grin. Even Asha Reed inclines her head, registering the timeline as serious."
        "Suggest a phased desk-review before the sea trial":
            "Dr. Lena Huang nods, valuing caution, and a few people feel steadied. Elias Voss frowns slightly; it's not what he wanted, but he accepts that the room needs confidence-building steps."

    # --- merge ---
    "You weigh both options in a breath. The mid-afternoon light slants through the greenhouse, dust motes suspended like possible futures. Building trust means momentum; it also means safeguards. You choose the frame that threads both commitments — speed with guardrails."

    maya_soren "We'll pilot a hybrid, modular kelp-and-panel system, co-designed with community reps. We'll fund rollback escrow, enforce local hiring, and set a monitoring protocol with stop-criteria. The Aster will demonstrate a small-scale deployment — controlled, reversible — in roughly six to eight weeks. We'll publish the monitoring plan and budgets to the hub now."

    elias_voss "Six to eight weeks. I'll get the crew ready and line up the sensors. Thank you."
    hide elias_voss
    show dr_lena_huang at center:
        zoom 0.7

    dr_lena_huang "I'll draft the monitoring indices and stop-criteria. We'll make them legally binding attachments to the pilot agreement."

    asha_reed "I'll bring the coalition conditions — community oversight board seats and an independent auditor. We watch the books and the shore together."
    hide asha_reed
    show jonah_mek at left:
        zoom 0.7

    jonah_mek "I'll organize the work co-op for training and short-term hires. We'll build the first panels in the Lower Quay workshop — keep craft local."
    hide maya_soren
    show rosa_calder at right:
        zoom 0.7

    rosa_calder "And I want a garden buffer — temporary beds we can move if need be, but guaranteed replacement soil and funds if anything is disturbed."
    "You nod, tapping commands into the hub tablet. The registry fills: timelines, names, escrow account placeholders, monitoring criteria. Words solidify into the scaffolding of governance."
    hide dr_lena_huang
    hide jonah_mek
    hide rosa_calder

    scene bg ch2_c4ca42_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A single sustained chord in the strings; hopeful but measured]
    show maya_soren at left:
        zoom 0.7

    maya_soren "I'll schedule the Aster's demonstration and open the pilot documents for review. We'll meet weekly until deployment, with rotating community co-chairs. If anyone hears concerns, bring them early."
    show elias_voss at right:
        zoom 0.7

    elias_voss "I'll coordinate with Captain and crew. We'll keep the demo small and reversible."
    show asha_reed at center:
        zoom 0.7

    asha_reed "Fine. We'll be there — watching."
    "You feel the room exhale — a collective easing into something that is not a settled victory, but a shared work plan. The arousal that tightened the room earlier resolves into forward momentum: not triumphant, but constructive. Hope here is pragmatic and earned."
    "You step back, letting the group file edits into the hub. Outside, the bay's surface smolders in late light. Inside, voices continue — quieter now, but alive with tasks and commitments. The greenhouse domes hum; a condensation bead rolls down and falls into a potted herb with a soft plink."
    "You close your satchel for a moment and let the small, sustained satisfaction of gathered voices fill you. The pilot is not guaranteed success; the politics are still volatile. But for the first time since the garden meeting began, the possible future feels like something you can reach toward together."
    hide maya_soren
    hide elias_voss
    hide asha_reed

    scene bg ch2_c4ca42_3 at full_bg
    # play music "music_placeholder"  # [Music: Strings swell gently, then settle into a steady undercurrent]

    "You schedule the demonstration on the hub calendar, slot the Aster for a reconnaissance run, and send invitations to the co-chair list. The projection confirms" "Aster Demonstration — Week 6.' You add a note: 'Publish monitoring plan and budget; escrow funding to be finalized."
    "You linger a heartbeat, watching Elias Voss and Asha Reed exchange a look that is careful and not simple. You cannot tell exactly what passes between them — some things remain unreadable — but the room has moved closer to a shared, if fragile, axis."
    # [Page-Turn Moment]
    "You step to the greenhouse glass and press your palm to the cool pane. The bay beyond is a flat sheet of possibility. Inside, the hub's light outlines the decisions you've just brokered: promises written into"
    "code, committees formed, a ship booked to prove a point at sea. It is not an answer; it's a living plan. You let the thought hang: momentum built by many hands is harder to undo. You"
    "turn back to the room with the small, steady conviction that the work will continue tomorrow, and that you will not do it alone."

    scene bg ch2_c4ca42_4 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
