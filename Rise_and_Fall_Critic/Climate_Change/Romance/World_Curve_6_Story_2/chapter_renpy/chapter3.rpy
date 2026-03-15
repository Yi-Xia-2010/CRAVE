label chapter3:

    # [Scene: Saltgarden Research Lab | Morning]

    scene bg ch3_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft drip of water, a rack creaking as kelp shifts; a distant gull’s wail like an unanswered question]
    # play music "music_placeholder"  # [Music: Low, melancholy strings — a slow descending motif]
    "You come into the Saltgarden the way you come into other guilty rooms — with your shoulders already braced for what must be decided here. The lab smells like wet slate and fresh kelp, that green-sour"
    "tang that tastes of possible things: food, medicine, shelter. Your notebook is folded against your ribs; the coral pendant rests warm at your throat as if it understands the weight of the morning."
    show ilias_navarro at left:
        zoom 0.7

    ilias_navarro "You came early."
    "He sets a clear sleeve of eelgrass on the bench between you, the little cutting trembling with damp. 'Thought you might like to see how the cuttings take in controlled flow.'"
    "You can let your fingers hover over the sleeve without touching. The green is small and foolishly brave. You remember the town hall's wooden doors, the calibrated smiles, the mayor's 'interim protection' — a phrase that"
    "sits sour in your mouth. Here, among wet glass and grow lights, those words feel like a foreign currency."
    show maya_kestrel at right:
        zoom 0.7

    maya_kestrel "They look... alive."
    "You force a small laugh that doesn't reach your eyes. 'Ilias, you said there was something else. You sounded... off at the meeting.'"
    "Ilias Navarro's mouth presses together for a beat; he rubs a thumb along the edge of a tray as if to steady a thought."

    ilias_navarro "Seren Blake's team reached out. They offered me access to the regional lab — more equipment, more controlled trials, better data resolution. On paper, it accelerates restoration timelines. They want validation from local fieldwork to claim the engineered wetlands are effective."
    "You taste bitterness — not just at Seren Blake's name but at the idea that your town's experiments might be folded into someone else's press release. The lab hums around you; a fan stirs the damp"
    "air. You think of kelp beds holding the sea, of hands in mud, of the slow work of learning when to bend and when to hold."

    maya_kestrel "Validation — or co-option? Their wetlands are engineered, right? Concrete cells, staged flows. The kind of thing that gets finished fast and looks like safety until you look at what it replaces."
    "Ilias Navarro leans back on his heels, fingers finding the braid of his tide-watch bracelet."

    ilias_navarro "They're engineered, yes. But the models show boosted recruitment for eelgrass if combined with living beds. They offered me a position to run trials at scale, to see if our methods can be integrated. I didn't— I mean, I haven't said yes. Part of me thinks, if we can prove restoration at scale, we get time. If we get time, we save more than we lose."
    "You feel the old bruise in your chest shift — a memory of a flashing storm and the brother you couldn't save. 'Time' is a ledger you can barely afford to open. Ilias's optimism sits next to your exhaustion like two fragile lamps under a gale."

    maya_kestrel "And the cost?"

    ilias_navarro "Cultural concessions. Access rules. They want branding and a fast rollout. They also have political clout. Seren Blake can get permits signed before the next high-tide vote."
    "He watches you measure the sentence by its impact. The fan clicks; the kelp rustles like low applause."

    ilias_navarro "I'm torn. I want the science to work. I want people to be safe. I want your plan to be the way forward. But I'm starting to feel the town's needs with a stopwatch."
    "Silence rises between you and takes the lab with it. You find the coral pendant and rub its carved grooves until they blur."

    menu:
        "Ask him to explain Seren's lab offer in technical detail":
            "Ilias picks up a tablet and scrolls through schematics, his voice clinical at first, then layered with unease as he points out where community stewardship would have to cede control. You follow the lines of flow and feel the political currents bend."
        "Press him on what he'd want if nobody was watching":
            "He blinks, and for a beat you see a private thing: the scientist who once stayed up all night for a filament of data and the man who wants his own hands to be useful. He says softly that he'd want the beds to be for the people who fish them, not for a press release."
        "Warm your hands around a tray and let the smell steady you":
            "The warmth and the tang of sea-moss ground you; your voice softens. You tell him you need proof that the effort will protect homes, not just shorelines on a map."

    menu:
        "Promise Etta you'll stand with the town publicly":
            "Etta's face softens and a wet laugh escapes her. She draws you close, pressing your shoulder like a seal of trust. The roots underfoot seem to take a little more root as well."
        "Ask Etta for time to think, privately":
            "She frowns, but it's not the sharpness of betrayal — it's worry. 'Time,' she says slowly, 'is a luxury. But I give you till dusk.' Her hand lingers in yours longer, as if passing a torch that's warm and fragile."

    menu:
        "Campaign publicly for community-led restoration and refuse Seren’s offer.":
            jump chapter4
        "Negotiate with Seren to combine engineering funds with local stewardship.":
            jump chapter7
        "Work quietly with Ilias to build a replicable low-tech proof-of-concept before declaring policy.":
            jump chapter10
    return
