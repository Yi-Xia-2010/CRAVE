label chapter8:

    # [Scene: Offshore Project Site | Late Afternoon — Storm-Banded Sky]

    scene bg ch7_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense BGM — low synth thrum with a snare-like pulse building]
    "You step from the harbor walk onto the platform and the air changes—metallic, ozone-sweet, charged before the storm. Your fingertips are still smudged with mud; the smell of wet peat and salt hangs under the clinical"
    "odor of warm electronics. The leather of your jacket squeaks where it brushes a crate. Every sound feels amplified: the click of a tablet closing, the distant slam of a rope, the soft hum from the"
    "floating turbines beyond the scaffolding."
    "Elias meets you at the threshold with that measured, corporate smile that never quite reaches his eyes. He extends a leather folio like an offering. You can see the corners of timelines, the precise edges of impact assessments, signatures that promise money, manpower, speed."
    show elias_wren at left:
        zoom 0.7

    elias_wren "Maia. Thank you for coming. We wanted you to see the plans in person—transparent as possible.' (His fingers press the folio to your palm; his voice is smooth, practiced.) 'We can protect the bay and bring jobs. The models show a fifty to seventy percent reduction in surge energy for the main inlet once the breakwater and offshore platforms are operational."
    "You take the folio, feel the weight of contracts and the cold of Tony-clipped signatures. The schematic on his lapel pin flickers—a rotating 3D of engineered reefs and sleek turbines, tidal arrows marked in bold lines. It looks like salvation from a render: clean, inevitable."
    "Maia Rivera: (You flip through the folio with a controlled hand; your chest tightens as each page resolves into charts and assurances. Numbers are persuasive; money is persuasive. Your mouth tastes of copper and obligation.) 'The"
    "renderings are... impressive. But 'models' are not the bay. What about migratory corridors for the anchovy shoals? What about the nursery marshes? Those are not lines on a rendering.'"
    "Elias slides a page forward, calm as a tide that always returns."

    elias_wren "We included migration mitigation in the latest assessment. There are simulated corridors—"
    show maia_rivera at right:
        zoom 0.7

    maia_rivera "Simulated corridors rely on assumptions. Real fish move in messy ways and change with each storm. I need empirical assurances: baseline surveys, adaptive management clauses, real monitoring officers from the cooperative."
    "Elias pauses, the smoothness briefly thinning."

    elias_wren "We can include monitoring. We can—' (He searches for the right level of concession.) '—define an independent oversight panel. It will slow permitting, but it can be done."

    menu:
        "Scan the AR schematic first, let the renderings wash over you":
            "You lean in toward Elias' lapel display, watching simulated waves fold across the breakwater. The animation's motion soothes and angers you at once—this kind of certainty could save lives, but it erases small things that are harder to model."
        "Finger through the folio's signed agreements, checking clauses":
            "You flip to the contract pages, eyes skimming indemnities and milestone deadlines. Your chest tightens at the phrase 'expedited deployment'; someone has already valued speed over nuance on paper. The signatures are real."

    menu:
        "Go down to Jonah and argue from the dock":
            "You step off the platform toward the dock, water spraying your boots. Jonah looks up, wary. The air tastes like salt and possibility and you can feel the familiar rhythm of his breathing. You speak to him raw and blunt; he responds guardedly, the two of you closing like two halves of a net."
        "Stand your ground and continue negotiating with Elias":
            "You stay. Elias takes your continued presence as leverage. The negotiation sharpens—an exchange of clauses and deadlines, each sentence like a pull on a rope. You force specifics; he offers substitutes. The meeting's tension climbs."

    menu:
        "Push Elias for strict environmental clauses, even if it slows deployment.":
            jump chapter9
        "Accept Elias's timeline to get infrastructure in rapidly.":
            jump chapter11
        "Demand a public co-management agreement and tie contracts to cooperative oversight.":
            jump chapter11
    return
