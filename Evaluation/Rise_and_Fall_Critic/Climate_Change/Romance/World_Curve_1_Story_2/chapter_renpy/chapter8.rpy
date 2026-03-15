label chapter8:

    # [Scene: Voss Development Office | Late Afternoon]

    scene bg ch8_6b08b4_1 at full_bg
    # play music "music_placeholder"  # [Music: Steady, warm strings — a rising motif]
    # play sound "sfx_placeholder"  # [Sound: A distant gull, the low hum of the building's ventilation, paper shuffling]
    "You step into Soren Voss's office with the harbor in your head: the taste of salt still behind your teeth, the memory of the bluff where the town's lights blinked awake. The meeting room smells faintly"
    "of cold coffee and new paper. Outside, the sea is a flat, patient slate; inside, there is the bright, contained energy of people trying to turn anxiety into a plan."
    show soren_voss at left:
        zoom 0.7

    soren_voss "We have the memorandum draft. Legal's clean, the funding mechanism is in place, and the timeline gets us shovels in the ground within months, not years."
    "You keep your voice even. You've learned that even measured sentences can steer momentum."
    show mika_hoshino at right:
        zoom 0.7

    mika_hoshino "Fast is good — we need traction. But funding without teeth lets promises erode. We need measurables: remediation lines, apprenticeships, enforceable ecological targets."
    hide soren_voss
    hide mika_hoshino

    scene bg ch8_6b08b4_2 at full_bg
    show elias_maren at left:
        zoom 0.7

    elias_maren "If we don't anchor restoration in the contract, the kelp beds and living shorelines risk being add-ons. They become optional in a crunch. We can pilot a living-breakwater now, but it needs funding guarantees."
    "Soren leans back and lets his hands fold into one. He doesn't interrupt; instead, he lets the room feel the freight of what he knows the town needs and what he must deliver to his investors."
    show soren_voss at right:
        zoom 0.7

    soren_voss "I know trust is frayed. My job is to deliver scale. People want certainty — roads that stay dry, businesses that don't evaporate overnight. I can get the capital. But I can't do every technical detail. That's where your expertise, Elias…and your community, Mika, must come in."
    "You notice the way his eyes flick to you — not seeking approval, but testing whether you'll help him carry the shape of this plan. For a second his steel-gray gaze softens. There's fear there; a"
    "practical, raw fear of failing and of having a blueprint look like a promise that broke."

    soren_voss "Once, where I come from, they raised the boardwalk, and then another storm wiped the paperwork clean. I don't want that to be my legacy. I don't want Atera to be another line on a CV."
    "The admission sits in the room like sunlight through fog. You feel the small, surprising lift inside yourself — not relief exactly, but the easing of a taut string. Vulnerability changes the negotiation. It makes a"
    "plan less like an extractive device and more like a bridge someone else might actually walk across."

    menu:
        "Point at the clause about enforceable monitoring and say we add specific metrics now":
            "You slide the draft toward Soren, tapping the paragraph on monitoring. Your hand is steady. 'We need baseline metrics, named labs, penalties for missed remediation milestones,' you say. Elias Maren breathes a small, grateful thread of air."
        "Ask for a short, binding pilot period with milestones to test the living-breakwater before full rollout":
            "You suggest a staged approach—pilot first, scale after milestone checks. Soren nods slowly; it's a promise softened into steps. Elias Maren smiles — a small, private thing — and the room relaxes a degree."

    # --- merge ---
    "The negotiation continues."
    "Jun clears his throat — you feel the timber of someone who sees construction sites in everything — and adds a practical note."
    show jun_park at center:
        zoom 0.7

    jun_park "If you're funding apprenticeships, we need to tie them to actual jobs. Trucks, materials — not just 'training.' The town remembers promises that didn't pay the bills."
    "Riv, who has been fidgeting with a bandana knot, speaks up before the conversation can drift into jargon."
    hide elias_maren
    show ravi_riv_delgado at left:
        zoom 0.7

    ravi_riv_delgado "And oversight. Full stop. If seats on the stewardship board are just token, it's worse than nothing. We want binding seats and vetoes on ecological decisions. No backdoor changes."
    "Mayor Amina Bakar folds her hands and speaks with the weight that comes from balancing a hundred small collapses."
    hide soren_voss
    show mayor_amina_bakar at right:
        zoom 0.7

    mayor_amina_bakar "We need a public registry for deliverables. Transparent audits. If Soren's plan accelerates funding, it's a public good — but the public needs to hold it. That means legal standing and clear enforcement pathways."
    "Soren exhales. The air seems to hold for a beat; each person has put a stake in the ground. The memorandum is no longer only his timetable. It is becoming the town's."
    hide jun_park
    show soren_voss at center:
        zoom 0.7

    soren_voss "I've been prepared to accept some oversight. What I won't accept is micromanagement that slows funding to the point we lose momentum. There has to be a balance — or we don't get anything at all."
    "You consider that. Momentum means lives protected sooner. But momentum without guardrails can hollow out what the protection was supposed to save."
    "Your palm grazes the dented key at your waist — a physical thing from your workshop, a reminder of a mother's hands and the work you inherited. It steadies a thought: safeguards are not just technical"
    "clauses. They're guarantees to the people who will keep showing up after the cameras leave."
    hide ravi_riv_delgado
    show mika_hoshino at left:
        zoom 0.7

    mika_hoshino "We make the RFP unassailable. We make deliverables measurable and public. We take the funding — but we bind it with enforcement. Apprenticeships are tied to payrolls, restoration milestones must be verified by independent labs, and the stewardship board must have seats with legal teeth."
    "Soren studies the revised paragraph you gesture toward, then looks at Elias Maren."

    soren_voss "Elias, can your team handle the independent verification? And Mika — can Amina and the cooperative write enforcement language that satisfies both legal counsel and the funding board?"
    hide mayor_amina_bakar
    show elias_maren at right:
        zoom 0.7

    elias_maren "We can do verification. But it has to be clear who signs off at each milestone. Independent labs, yes, and community representatives on audit panels."
    hide soren_voss
    show mayor_amina_bakar at center:
        zoom 0.7

    mayor_amina_bakar "I will work with legal. If we get language like that on paper, I can promise a vote of confidence from the council."
    hide mika_hoshino
    show jun_park at left:
        zoom 0.7

    jun_park "And payroll lines in the contract for apprenticeships — or we walk."
    hide elias_maren
    show ravi_riv_delgado at right:
        zoom 0.7

    ravi_riv_delgado "We don't want to stop progress. We just want to make sure this town survives it."
    "Soren closes his eyes for a second and exhales. He is, unmistakably, weighing his options: speed versus durability, headlines versus history."
    hide mayor_amina_bakar
    show soren_voss at center:
        zoom 0.7

    soren_voss "You all are going to make me the most micromanaged developer in the country. Fine. If that's what it takes to get a project that lasts, then that's what I sign up for. But—"
    "He falters a fraction, and it's a gift of honesty. He looks at you, and the edge in his voice is softer; it's not defeat, it's a kind of offering."

    soren_voss "—I need your help making sure it doesn't stall. Help me write the language. Help me sell it to the funders as a model that scales without bureaucracy. If we do that, Atera becomes the story we show other towns. If we can't, then we're a cautionary tale."
    "You feel the room lean toward the possibility — not just of money or levees, but of a replicable model stitched with local agency. The feeling is electric and quietly terrifying; it calls for more work, not less."

    menu:
        "Volunteer the workshop as a drafting hub to speed the legal language and keep community voices present":
            "You offer the greenhouse-rooftop lab and your workshop as a late-night drafting hub. Soren's eyebrows lift — surprised, but he accepts. Elias Maren grins; Jun nods like someone who will bring coffee and saws."
        "Ask Soren to bring in funders to a town forum before the final sign-off":
            "You insist funders see the town face-to-face. Soren hesitates — it's unconventional — but he agrees. Riv claps softly; the idea of the funders hearing the boardwalk creak underfoot excites him."

    # --- merge ---
    "The group settles on immediate next steps and drafting responsibilities."
    "The negotiation becomes a series of small compacts. You push for apprenticeships tied to payroll, independent verification, a public registry, and a stewardship board with binding seats. Soren offers a faster release of funds in exchange"
    "for a slightly shorter approval window. Elias Maren insists on pilot milestones and ecological vetoes. Mayor Amina promises to shepherd the legal language through council. Jun and Riv promise to hold the town's pressure so the"
    "plan doesn't flatten into a press release."
    "Every ask you make is a piece of a larger machine. Every concession Soren offers is a hinge."

    soren_voss "Write me the wording you want. I'll tell legal to draft it that way, and we'll include the pilot milestones you want. If you want joint governance with binding seats, we'll frame it; we may need a few more clauses to satisfy the funding board, but I'm willing to build them."
    "You realize the night has bent toward something real. The memorandum isn't finished, but it has teeth. Momentum has been married to safeguards, at least on paper. That feels like a victory you can live with."
    "Outside, the light has thinned to a coastal violet. The sea breathes low and regular, the town's edges softening into dusk. You step onto the bluff after the meeting to let the air re-sink into you,"
    "carrying the scent of ozone and warmed tar. The harbor is a network of lit rectangles below — not stars, but working lights — and you think of all the hands that will have to keep"
    "them lit."
    "Elias Maren catches up to you on the bluff, carrying his sea-salt-laden field notebook. He walks beside you for a minute without speaking, the silence threaded with the kind of companionable exhaustion you only get from long work."
    hide jun_park
    show elias_maren at left:
        zoom 0.7

    elias_maren "You pushed hard in there. I saw it. You kept them honest."
    "You feel something like a hand on your shoulder, only gentler — recognition."
    hide ravi_riv_delgado
    show mika_hoshino at right:
        zoom 0.7

    mika_hoshino "We kept the direction. We didn't give up speed. Now it's a matter of wording and people. If the clauses are tight and the audits are real, funds can flow without us losing the thing we're trying to save."

    elias_maren "That's the kind of compromise that builds resilience. It's messy, but it actually makes something stronger."
    "The words land like tide-stones: not a finishing blow, but a laying of the first solid stones in a foundation."

    "Your phone buzzes — Riv" "We trust you. Keep pressure.' Jun's text: 'Bring sample payroll templates."
    "And then Soren's offer hangs in your chest like a quiet promise: help him sell this as a model to other towns. The idea of Atera as an example of pragmatic hope sits heavy and good in your bones."
    "You know the next step forms a fork. There are ways to seal these gains and pathways to risk that could blow them open again. Your bluntness has opened room; now you must decide how far"
    "to lean into Soren's infrastructure plan, how fiercely to insist on ecological guards, or whether to press for a new hybrid governance that binds funding to local power."
    "The tide's rhythm underlines your thoughts — rise, recede, rise. Momentum is moving forward. You can feel the air changing in the town, the work shifting from talk to measurable steps."
    # [Scene: Bluff Overlooking Harbor | Twilight]
    hide soren_voss
    hide elias_maren
    hide mika_hoshino

    scene bg ch8_6b08b4_3 at full_bg
    # play music "music_placeholder"  # [Music: Strings rise brighter, hopeful]
    "You fold your hands against the chill, letting the salt air fill your lungs. This choice is not about who is right or wrong; it's about what shape of future you commit to building with everyone watching."

    menu:
        "Insist on strict ecological clauses and community oversight.":
            jump chapter9
        "Back Soren fully for rapid implementation, trusting we can correct course after.":
            jump chapter9
        "Negotiate a conditional joint governance model using Soren's funding but with binding local seats and ecological veto; this complex model requires further structuring.":
            jump chapter13
    return
