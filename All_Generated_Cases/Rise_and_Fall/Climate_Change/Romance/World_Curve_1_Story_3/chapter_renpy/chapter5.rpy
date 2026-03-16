label chapter5:

    # [Scene: Beaconworks Lab | Late Afternoon]

    scene bg ch5_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm, ascending strings with light percussive taps]
    # play sound "sfx_placeholder"  # [Sound: Low drone of pumps, distant traffic muffled by rain, a radio chatter fading between technicians]
    "You arrive with the smell of the neighborhood still clinging to you — brine, damp hemp, the oil-sour tang of freshly sanded wood. Your hands smell of salt and machine grease; when you rub them together"
    "the scent wakes a memory of Rani’s bench back in the Drowned Garden. Your pack is lighter than it felt yesterday, as if the crowd’s breath has taken some of the weight."
    "Tables have been pushed into a loose ring. Rani is there, sleeves rolled, a coil of nylon line at her feet and several sketched raft frames spread open like blueprints for rebellion. Eda sits with a"
    "small notebook of stitched paper, her fingers tracing a line of shell in the margin the way she maps tides. Beaconworks technicians hover near the holo-table, hands stained with sensor calibrant. Elias Harrow is at the"
    "simulation console, shoulders hunched in that familiar concentration he enters when the world reduces to models and variables."
    "You feel, in the space between your ribs, the same impatient guilt as always — the edges of loss that have pushed you toward action — softened now by a pulse of possibility. Today, here, the"
    "conversation might bend policy. Today you can show them how root mats and pylons might be friends, not enemies."
    show elias_harrow at left:
        zoom 0.7

    elias_harrow "We paused the machines long enough for this to be more than talk. The simulation is running a new constraint set — softer buffers, variable porosity. It’s accepting a root-mat parameter."
    show mara_solenne at right:
        zoom 0.7

    mara_solenne "Talk me through it."

    elias_harrow "If we let the buffer absorb more energy — non-linear damping — the wall can be set back twenty meters. But that requires flexible attachment points on the pylons. The tricky part is maintenance cycles: living mats need tending. They’re not a one-off install."
    "Rani leans forward and slaps a hand on one of her raft sketches. Sawdust puffs in the air and smells like warm bread."
    show rani_cho at center:
        zoom 0.7

    rani_cho "Tending’s the point. If it’s our garden, we know how to hold it. We can bolt modular frames to the pylons and weave the mats to them. If Beaconworks helps with the brackets, we give it a shot without losing the soul of the thing."

    "Technician" "Structurally we can design bolting plates that distribute load. But we need liability parameters, and the city will want inspection windows. That’s where Council has always tripped us up."
    "Eda Nal lifts her eyes — slow and knowing. When she speaks, the room quiets; her voice carries generations of mapping the tide."
    hide elias_harrow
    show eda_nal at left:
        zoom 0.7

    eda_nal "A place that breathes will heal faster than one that holds its breath. But breath needs rhythms — people who know when to let water come and when to keep it out. We must teach them the rhythm first."
    "You feel the plan arranging itself into three clear shapes in your head: rapid and local; shared leadership; or a larger, city-backed project with strings attached. Each shape carries a different kind of chance. Your fingers,"
    "still smelling faintly of oil, trace an invisible line on the holo-map where eelgrass might curl into a pylon’s shadow. It is soothing; drawing helps you think."
    hide mara_solenne
    hide rani_cho
    hide eda_nal

    scene bg ch5_4001e7_2 at full_bg
    "You open your mouth, then close it, choosing the next words carefully. Policy will be won by good engineering and a political narrative. The community’s voice will be stronger if the pilot’s governance makes sense."
    show mara_solenne at left:
        zoom 0.7

    mara_solenne "We need to decide governance first. Resources follow structure. If we can agree on who holds authority and who bears responsibility, the rest lines up."
    "Elias Harrow watches your face, as though measuring the unspoken edges of what you will accept."
    show elias_harrow at right:
        zoom 0.7

    elias_harrow "I can model outcomes for each governance scenario — probability ranges for survival, upkeep costs, social risk. But numbers don’t build trust."
    "Rani snorts softly."
    show rani_cho at center:
        zoom 0.7

    rani_cho "You do the numbers; we do the tending. But if you and Beaconworks come in full-steam with inspectors and forms, people scatter. Folks need to feel it's theirs."

    "Technician" "Co-management could give us the middle ground. We provide the brackets and technical oversight; you provide stewardship and local knowledge. The city would sign off faster if we’re at the table."
    "Eda Nal folds her hands over her notebook. She looks at you, and the gaze is both blessing and test."
    hide mara_solenne
    show eda_nal at left:
        zoom 0.7

    eda_nal "Remember, child, what you carry is not just a list of demands. It is the faces of those who will cross these walkways in thirty years. Choose a shape that holds them."
    "Your heart accelerates — not from fear but from the kind of responsibility that hums electric. Around the table people begin to voice micro-proposals: a volunteer maintenance rota from Rani’s team; a Beaconworks-sponsored technician-in-residence program; a"
    "city escrow fund for equipment replacement. The conversation ricochets like pebbles on water — full of impact."

    menu:
        "Ask Elias to run a rapid-prototype sim now — show a best-case scenario":
            "You press your palm flat on the holo-table. Elias blinks, then his fingers fly. For a moment the lab is only the glow of possibility: if the numbers line up, press releases become harder to weaponize."
        "Push for an on-the-ground demo with Rani's raft-builders this week":
            "You say the words and feel them land. Rani’s grin is feral and immediate; she already sees plank and nail and the faces who will come out to help. Action, she reminds you, is a language people understand."

    # --- merge ---
    "Scene continues as written below."
    "Elias takes your lead on the sim when you ask; the room watches as numbers bloom and a three-minute rendering ripples across the holo-surface. Wave height drops along the simulated shore; the living mats show survival"
    "probabilities. When you suggest a hands-on demo, Rani’s eyes light up and the lab’s energy tilts toward movement — a tangible pilot that smells of peat and rope."
    "Dialogue spills into deeper tracks. The Beaconworks technician voices legal caution; Rani pushes back with human stories; Eda grounds the room with traditional knowledge. You speak and listen in equal measure. The discussion is not neat;"
    "it lurches with friction and then settles into a new shape. Multi-turn exchanges weave through technical details and moral stakes."

    "Technician" "If the city signs the funding, we have to commit to maintenance schedules. If you want autonomy, we can't force that compliance."

    rani_cho "We don't want a babysitter. We want enough bolting power so the mats don't wash out on the first surge."

    elias_harrow "We can design inspection windows—structured check-ins that respect local leadership but ensure safety thresholds are met."
    hide elias_harrow
    show mara_solenne at right:
        zoom 0.7

    mara_solenne "That sounds like co-management with clearly defined roles. But what about a purely community-run model? If we keep control, we keep trust, but we limit scale."

    eda_nal "There is room for each. What matters is the stitch. A sewn net can hold more than a single rope."
    "The room is alive with possibility. You feel your impatience — the part of you that wants immediate rescue — loosen, replaced by the steadier build of strategy. The rising tone of the day lifts you; for the first time in a while you sense not just reaction but construction."
    "Elias Harrow steps closer to you privately, lowering his voice, the warmth of paper-white LED catching the line of his jaw."
    hide rani_cho
    show elias_harrow at center:
        zoom 0.7

    elias_harrow "Whatever you pick, I’m with you in the engineering. I’ll model the outcomes. I want to make sure the city's commitment doesn't strip your neighbor's agency."

    mara_solenne "I don't want to be traded for a budget line. And I don't want to slow us so much that the area gets bulldozed while we debate."

    elias_harrow "Then let’s design for both speed and stewardship. Build brackets that can be retrofitted by volunteers."
    "The two of you talk long enough that the technician clears her throat and calls the room back. Decisions need names. The pilot needs governance. Funding and control hinge on the label you choose at the table."
    "You look around: Rani’s hands, still dusted with sawdust; Eda’s lined face; the technicians' pragmatic faces; the holo-map that now shows not just models but people's names pinned to maintenance nodes. The moral geometry of the"
    "moment crystallizes — autonomy, partnership, or scale. Each will change who holds the maps and how your relationship with Elias will read to the city: quiet partnership, shared authorship, or a negotiated compromise."
    "Your throat is dry, but your voice feels clear."

    mara_solenne "Alright. We decide governance now. We choose the pilot model and stand behind it together."
    # play sound "sfx_placeholder"  # [Sound: A single, hopeful chord on the synth — an upward lift]
    # [Scene: Beaconworks Lab | Late Afternoon — Continuation]
    # play music "music_placeholder"  # [Music: Strings swell softly, optimistic and determined]
    "You sense the chapter closing like a tide line: the work you started with a crowd has narrowed into a shape you can carry forward. Hands reach across the table. Papers are signed; not contracts, but"
    "lists and commitments — a volunteer roster, a technician secondment request, a memo to Council. The team affirms that this moment can be made into something viable."
    "The room leans in, waiting for your choice — the one that will bind funding, control, and the public face of your partnership with Elias."

    jump chapter6
    return
