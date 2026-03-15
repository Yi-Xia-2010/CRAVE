label chapter2:

    # [Scene: Glasshouse Research Lab | Morning]

    scene bg ch2_c4ca42_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the soft hum of refrigeration units]
    # play music "music_placeholder"  # [Music: Quiet, hopeful ambient with light piano undercurrent]
    "You step in with your field jacket still damp at the cuffs, the Moleskine tucked under your arm like a promise. The lab smells of ozone and wet soil—clean, technical, and strangely domestic when the plant"
    "trays beside the window give off that faint green warmth. Your utility watch blurts a tide alert and you let it sit against your wrist, more a reminder than alarm."
    show professor_julian_kim at left:
        zoom 0.7

    professor_julian_kim "Maya. Right on time. Come see this."
    "You set the Moleskine down and lean over the table. He unrolls the projection like a ritual—contour lines that are not mountains but the moving shore. Blue screens glow behind him, casting soft halos on your"
    "face; hazel flecks catch the light and feel absurdly steady in the cold lab air."

    professor_julian_kim "These are the tidal projection ensembles, and here—' (he taps a shaded band) '—salt-marsh absorption models, layered with land-use scenarios. We ran a higher frequency storm sequence. The marsh buys us time, but it's not infinite."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "How soon would a marsh like this stop doing the work we need it to?"

    professor_julian_kim "Depends on stressors. On maintenance. On storms. In the worst ensemble—the one with intense storm clustering—you'll see the boardwalk shear in one season. It's not dramatic in the map; it just...drops. But for people, that's everything."
    "You reach out, fingertips waiting just above the paper as if you can press urgency into the ink. The models read like weathered futures: gentle gradients, then sudden cliffs where a single storm curve slices through a neighborhood."

    professor_julian_kim "Exactly. You always said we need a web of small actions. Models don't romanticize; they just give you the range of possible tomorrows. You can plan within that band."
    "Multi-turn exchange lengthens into technical details—sediment budgets, planting densities, maintenance schedules. You ask thin, focused questions; he answers, drawing arrows with a pen that smells faintly of coffee. Each explanation is another thread you can tie to the map you started last night."

    menu:
        "Ask to run a neighborhood-specific model":
            "You point at the part of the projection that overlaps the lower boardwalk. Julian's eyes light; he slides a tablet toward you and says he'll queue it after lunch. The possibility of a localized output settles like a small found tool in your hands."
        "Say you'd rather walk the shore first":
            "You close the chart gently. Julian nods and offers you a thermos; the idea of seeing the data reflected in actual pilings feels like aligning two halves of a compass. He warns you'll see things the model only hints at."

    menu:
        "Lower a sample bottle into the water":
            "You hand Iris a sterile bottle. The water inside is a thin, brackish brown. Iris frowns, and the micro-unease in her face confirms the model's whisper: this isn't just a shifted current; it's a shifting ecosystem."
        "Take photos and log GPS points":
            "You hand Samir's old camera to Iris—she takes a few slow, exact shots. The pixels feel like records, small proofs to show the council with names attached."

    menu:
        "Tell Elias you'll help plan the mapping workshop":
            "You fold the map carefully, the corners aligning like intentions, and tell Elias you'll draft the workshop mapping with him. He clasps your forearm, gratitude brightening his face; the moment feels quiet and right."
        "Ask for time to align models with community schedules first":
            "You ask for a few days to cross-reference schedules and models. Elias nods, not disappointed—practicality suits him too. There's a shared understanding that this is work, not a rush."

    jump chapter3
    return
