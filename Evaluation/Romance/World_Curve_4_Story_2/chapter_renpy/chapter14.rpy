label chapter14:

    # [Scene: Skyline Rooftop Garden | Evening]

    scene bg ch14_9d8ae5_1 at full_bg
    # play music "music_placeholder"  # [Music: Gentle, ascending guitar motif; soft percussion like measured footsteps]
    # play sound "sfx_placeholder"  # [Sound: Low hum of distant pumps at the prototype site, occasional gull cry, people murmuring below]
    "You close your journal the way you always do—slow, deliberate, a hinge at the spine. The pressed marsh grass between the pages breathes the faint smell of peat and salt. Around you, the rooftop smells of"
    "compost, warm tomato leaves, and a last sip of cooling coffee. It feels impossibly ordinary and wildly important at once."
    "Across the bay, the prototype lights burn like careful stars. In the hour between work and sleep, everything looks like possibility—wet metal and marsh plots, strings of bulbs and hand-lettered signs. The pilot performed well. You"
    "have the data; you have the stories. Hope is not a promise, but it is palpable, a thing that hums under your skin."

    scene bg ch14_9d8ae5_2 at full_bg
    # play music "music_placeholder"  # [Music: Slight swell—light, steady]
    show dahlia_kestrel at left:
        zoom 0.7

    dahlia_kestrel "You did good work, Ms. Reyes. The metrics are clean. The oscillations are minimal. This model scales."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Scales how, exactly? Scalability isn't just numbers. It's people—jobs, coastal knowledge, seasons. We can't treat the town like a lab."

    dahlia_kestrel "I agree on the people, which is why modular, reversible components make sense. Fast deployment when the tide comes. Then removal or reconfiguration as communities adapt."
    show elias_kwan at center:
        zoom 0.7

    elias_kwan "Fast is fine. But who builds them? Who keeps them? If we hire outside crews and they vanish in summer, we've traded one problem for another.' (He catches your eye, half-joke, half-plea.) 'Apprenticeships. Folks who know the bay and the machines."

    dahlia_kestrel "Apprenticeships can be part of the rollout. We can fund training and local hiring quotas."

    maya_reyes "But how do we keep the controls local? How do we stop a corporate buyout rebranding 'community work' into a service contract that leaves us with fewer rights, not more?"

    dahlia_kestrel "We draft enforceable community safeguards. Governance language. Audits."

    elias_kwan "Audits are fine on paper. On the docks, governance needs hands. Mentorship, pay that pays bills, tools that don't get repossessed. You've seen what's happened when jobs vanish in my family."
    "There is a small pocket of silence. The bulbs hum. The bay breathes. Your chest aches with the weight of everything that could be saved—and everything that could be lost if you make the wrong call."
    "The prototype's success makes the decision urgent; success invites scale, and scale invites choices you will be measured by for years."

    menu:
        "Ask Elias for concrete apprenticeship numbers":
            "You turn to Elias. His shoulders relax with the invitation; he rattles off figures—seasonal hires, a two-year training ladder, mentors who'd be paid for the first six months—and you feel the plan get roots."
        "Ask Dahlia what 'enforceable safeguards' mean concretely":
            "You peg your question on a phrase she uses. Dahlia reaches into a slim tablet and shows clauses—sunset provisions, community vetoes, a legal escrow for funds—her voice steady, the options suddenly legible but cold."

    # --- merge ---
    "Continue"
    hide dahlia_kestrel
    hide maya_reyes
    hide elias_kwan

    scene bg ch14_9d8ae5_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Footsteps on the catwalk, distant clank of machinery, a gull settling into the dark]
    # play music "music_placeholder"  # [Music: Transition to a brighter, hopeful piano phrase]
    "You walk with them—Dahlia moving like a plan in motion, Elias like weather-worn rope. You keep your journal closed at your side, but your mind is already a ledger: contingencies, guardrails, apprenticeship wages, legal language that"
    "must not be porous. The rooftop shrinks behind you; in front, the prototype site is half-lit, half-quiet, like a living diagram."
    # [Scene: Prototype Site | Night]

    scene bg ch14_9d8ae5_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low mechanical whirr, water lapping against pilings, the measured beep of sensors]
    # play music "music_placeholder"  # [Music: Warm strings; a subtle ascending motif to underline cautious optimism]
    show dahlia_kestrel at left:
        zoom 0.7

    dahlia_kestrel "The modules lock into each other, temporary anchors that can be adjusted. They don't require a full concrete foundation; they sit with the tides and can be withdrawn when better solutions are available."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Reversible is good. It gives the community time to adjust rather than be overwritten overnight. But reversible for whom? For us, or for the company who owns the patent?"

    dahlia_kestrel "We can license differently. Open-source elements, community licenses, tiered access. You dictate the governance."
    show elias_kwan at center:
        zoom 0.7

    elias_kwan "And the work? We need local crews with steady income. Not just pilots that pay for a season.' (He looks at you directly.) 'If we're scaling, build jobs into the model. Make the apprenticeships non-negotiable."

    maya_reyes "Then whatever the route—slow, modular, or licensed—we put people at the core. Oversight, local hiring, and a commitment to keep control within the community."

    dahlia_kestrel "That's reasonable. Measurable, too. We can bind hiring targets to release schedules. We can let audited community boards have a veto on certain adjustments."
    "You breathe that in. Each proposal is a promise wrapped in paper clauses. You imagine the apprenticeships Elias mentioned: a young fisher learning to calibrate a sensor, an older net mender learning to retrofit panels. You"
    "imagine the town with more steady work, hands learning new tools that still echo the old ones."

    menu:
        "Trace the seam of a module with your thumb":
            "You run a thumb along the joint. The metal is colder than you expect, but the fit is clean. That tiny tactile assurance steadies your determination."
        "Step back and look at the marsh plots instead":
            "You turn to the marsh plots: cordgrass glistening under the lights, small birds sheltering in the reeds. Seeing the living thing you fight for brings your priorities back into sharp focus."

    # --- merge ---
    "Continue"
    "You make notes. Pros. Cons. Worst-case scenarios. Escape hatches, veto thresholds, funding cliffs. The arc of policy unfolds in your head like a map: each road forks into politics, livelihoods, and memory."

    elias_kwan "Whatever you decide, we'll stand with it. But you'll have to hold my brother's pay in one hand and our bay in the other. Don't let one break the other."

    maya_reyes "I won't. We'll build a plan that pays people and patches the world. That's the point."

    dahlia_kestrel "Then we draft. We consult. We set metrics and enforcement. Speed need not be brutal; it can be precise."
    "The night feels like a held breath that has started to let out. The prototype performed—now the question is how to make performance into protection without erasing the texture of home. Your journal is full of"
    "contingencies, but you know the town will measure you by more than footnotes: by paychecks kept, by seasons saved, by the way a hand can still know a line in a net."
    "You sit on a bench near the trial marsh, the wind carrying the smell of wet earth and machine oil, and let the decision compress into something simple: three routes, each with its own promise and"
    "its own risk. You feel hope—clean, rising—because options mean possibility, and possibility means work to do."
    # play music "music_placeholder"  # [Music: The guitar motif returns, ascending; the atmosphere is quietly triumphant]
    "Your pen hovers over the last page. This is not just policy. It is a moral architecture for your town. It will shape who works beside you and what stories the bay tells in fifty years. You inhale the salt air and feel ready."

    jump chapter15
    return
