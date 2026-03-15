label chapter13:

    # [Scene: Mangrove Patch / Abandoned Shipyard | Dusk]

    scene bg ch13_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft rasp of water against wreckage; distant gulls complaining; a single loose clank from a forgotten winch]
    # play music "music_placeholder"  # [Music: Sparse piano, low, a ribbon of cello beneath — elegiac but steady]
    "You stand ankle-deep in mud that smells of iron and old seaweed, the chill pulling at the cuffs of your jacket. Your fingers are stained with kelp-sap and concrete dust; when you rub them on your"
    "pants the print of the work day smudges like a map someone else tried to redraw. You count in your head the list that will not stop running—plots saved, nets mended, people moved—and a weight settles"
    "behind your sternum that is not quite regret and not quite relief."
    "Everything that followed the vote has a rhythm you can still hear: meetings with clauses scribbled in legal blue, volunteers bending over trays of seedlings at dawn, Seren Blake’s sleek presentations on tablets that glowed like"
    "small suns. Acceptance of the conditional funds felt like gripping a rope thrown into a rising tide. It kept some things afloat; it pulled others away."

    scene bg ch13_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Your breath, small and precise.]
    "You trace the engineered frames where eelgrass has taken a hesitant hold. The plants here breathe differently now—some clumps thick and healthy, silvered with light; others threadbare, parted as if to make room for something larger"
    "that never arrived. The pilot worked in patches. Some fisheries stirred back to life. A few heritage sites sit safe under the sanctuaries you argued for; a plaque on a raised platform lists names and donors,"
    "a gilded compromise that tastes like salt and money."
    "Ilias Navarro steps out from behind a half-sunken hull, a streak of seaweed caught in the hair at his nape. His field notebook is wet but clasped tight, camera at his side. He breathes the same cold air as you and his face finds you before his words do."
    show ilias_navarro at left:
        zoom 0.7

    ilias_navarro "You found them already."
    show maya_kestrel at right:
        zoom 0.7

    maya_kestrel "They found us, more like."

    ilias_navarro "The eelgrass beds are thicker where we planted the frames last month. Hana says the recruitment is better than the models predicted.' (He smiles, small, brittle with relief.) 'We were lucky—timing, tides. You led the permit push like you always do."

    maya_kestrel "We won the permit.' (You don't say how many meetings bled into each other, or how many nights you slept with lights burning over maps.) 'We kept the sanctuaries. We got hardware in the water. We—"
    "Ilias Navarro: (interrupting, gently) 'We saved some things.'"
    "The phrase should feel like triumph. Instead it tastes partial, like a meal eaten while someone else takes the chairs. He reaches for your hand, fingers cold from the water, and his palm fits around yours with the practiced ease of someone who has learned how to steady you."

    menu:
        "Kneel to check the new eelgrass plugs":
            "You bend forward, fingers sliding into damp soil to feel the hold of living roots. The pull is strong enough to anchor hope, if only in this place."
        "Stand and listen to Ilias":
            "You let him talk, letting the warmth of his voice stitch the hour together. His optimism feels like a small terrace against the sea's erasure."

    menu:
        "Push Hana for aggressive public transparency":
            "You press for the numbers to be public. If people see the buyouts, maybe scrutiny will slow them. That feels like throwing light into a dark corner and hoping it scares something off."
        "Ask Ilias to catalog beneficiaries first":
            "You suggest building a human narrative—who is hurt by these buyouts—so that when Rafi runs a story it's not just data, it's faces and names. Ilias nods; his voice steadies at the work."

    menu:
        "Offer to help the family with logistics":
            "You walk over, voice steady as you offer an extra pair of hands. The couple's nod is quick, wary; it is a relief you cannot give them back."
        "Let them go and watch, keeping distance":
            "You stay by Etta's doorway and watch the van pull away. Watching feels like a ledger you keep; intervening feels like choosing who can stay and who must go."
    "THE END"
    # [GAME END]
    return
