label chapter3:

    # [Scene: Floodplain Market | Late Afternoon — High Tide Approaching]

    scene bg ch3_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A constant undertow of voices—overlapping, frayed—underscored by gull cries and the distant thrum of a generator. Somewhere, a child laughs and then is shushed.]
    # play music "music_placeholder"  # [Music: Tense BGM — low strings and a driving percussion loop; tempo steadily increasing]
    "You step off the promenade and onto the market planks with your sketchbook heavy at your hip and the compass warm against your sternum. The smell hits you first—frying oil, damp kelp, hot metal from nearby gear, and the unmistakable brine that tastes like history and threat at once."
    "The square is packed more than usual. Stalls are shuttered; crates form a ragged ring around a makeshift stage of stacked pallets. Reverend Sol stands at the center like an old buoy: steady, carved cane in"
    "hand, his voice trying to hold a wavering sea of anger and fear. Nita is two stalls over, apron gone—her hands on her hips, eyes hard as ballast. Juno stands by her, arms folded, chin set;"
    "the kid keeps glancing at you as if trying to measure whether safety still exists within your shoulders."
    "You feel each face tilt toward you as you move through them. Not because you asked them to: because the town wants something from you now—direction, a plan, a name for the fear."

    "Reverend Sol" "Mara—' (his voice is softer than the crowd; you feel it as if he’s speaking into a fog) '—we can't let this drift. You understand the soil and the sea. Speak plainly."
    "Your mouth is dry. You imagine the compass pressed into your palm like the lid of a sealed promise. A hundred different outcomes crowd the hollows of your chest: compromises that saved pockets and lost neighborhoods; quick fixes that smoothed paperwork but hollowed out trust. Each possibility hums with consequence."
    "Nita intercepts you before you reach the pallets. Her face is a map of certainty and exhaustion."
    show anita_nita_ramirez at left:
        zoom 0.7

    anita_nita_ramirez "You heard Evelyn's plan. Concrete segments, cranes, lights. They call it progress. It will bury half of the eelgrass beds and put a toll on the fishers. Are you going to stand for that, or are we going to stand for ourselves?"
    "You open your mouth. You want to list the living-shoreline pilot—kelp lines, oyster clusters, porous berms. You want to cite Dr. Leila's tentative models and the idea of scaling slowly. But the crowd is a clock"
    "counting down to a public hearing, and Evelyn's company is filing permits while you two argue semantics."

    menu:
        "Answer Nita with calm facts":
            "You take a breath and lay out the data—how oyster reefs dissipate wave energy, how kelp lines slow surge. Nita’s shoulders drop fractionally; she nods but the hard set of her jaw remains."
        "Respond with a sharp, emotional plea":
            "You let the ache of your father’s loss thread through your voice. Your words land like stones—solid, raw. Nita's eyes flash; she reaches for your arm and squeezes it, anger turned into urgent solidarity."

    menu:
        "Take Evelyn’s offer to speak privately":
            "You nod, step down from the pallets, and inclination pulls you toward a quieter conversation. Evelyn's aides close ranks politely; the air smells like ozone and polished metal. The crowd scowls, feeling betrayed by the idea of backroom deals."
        "Refuse and stay in public, force transparency":
            "You plant your feet on the pallets and meet Evelyn's gaze across the sea of faces. People lean in; some cheer, some hiss. Your refusal tightens the room like a drum."

    menu:
        "Organize a public resistance and demonstration":
            jump chapter4
        "Negotiate a hybrid plan with binding community governance":
            jump chapter7
        "Stage a bold solo demonstration of a living reef offshore":
            jump chapter10
    return
