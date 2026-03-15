label chapter5:

    # [Scene: Blackbrand Development Site — Staging Yard | Night — Midnight]

    scene bg ch5_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant generator thump; the muffled scrape of machinery; a gull’s cry turned thin by wind; the sump of boots on sodden planks.]
    # play music "music_placeholder"  # [Music: Tense, pulsing low strings; percussive, building tempo]
    "You move like a shadow across the staging yard, a practiced slip between crates and cranes. Your palms ache from knots tied earlier; the rope still smells of algae and salt. Around you, volunteers fold into"
    "formations you sketched with your ink-stained hand—lines of bodies linked across the mud, tethered to one another and to stakes hammered into the flats. The human web is rough but sure: hands, shoulders, straps of reclaimed"
    "sail flipped into armbands, a kid’s bicycle chain looped to make a quick clasp."
    "Your father's compass sits heavy against your sternum. It is only metal and memory, but tonight it is a fulcrum beneath your ribs. You count faces—Nita’s broad back at the head of a line, Leila checking"
    "sensor housings by headlamp, Juno tucked near the low tide with a headlamp blinking like a frightened star. Reverend Sol moves slow among people, his cane tapping time, a soft hush cutting through a whispered exchange."
    "Kai is close enough that you can feel the heat from his shoulder when he leans in to speak."
    "Everything tastes of diesel and mud and the metallic edge of adrenaline."

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low, coordinated radio crackle from the security perimeter; a pair of boots hitting a wet board—clearer now, closer.]
    show kai_navarro at left:
        zoom 0.7

    kai_navarro "They moved the floodlights. Took them two hours to clear the bulldozer out of the main trench, but—' (he swallows, attempting a grin that doesn't land) '—they’re here. Expecting an escalation."
    show mara_linh_alvarez at right:
        zoom 0.7

    mara_linh_alvarez "How many?"

    kai_navarro "Three squads. Standard security rotation, maybe two dozen on the ground, more in the trucks.' (He watches your face; his amber eyes flare worry.) 'They've got riot shields in hard cases. Leila's reading the acoustics—she says the sound of vehicles crawling through the sand will let us know their approach before they hit the perimeter."
    show dr_leila_osei at center:
        zoom 0.7

    dr_leila_osei "Sensors are live. We’ll have thirty seconds to a minute warning when the trucks come off the causeway.' (She doesn't look up from her handheld; her breath fogs in the light.) 'If anyone slips in the mud, call it out. We'll have medics and warm blankets staged."

    "Nita (calling out)" "And if they try to push through—' (the bandana at her temple is soaked with sweat) '—we don't move. We hold the line."

    "Reverend Sol (softly)" "Holding is a vow. But vows and tactics must line up. We cannot be reckless and we must not be timid."
    "You feel the pull of both words. Holding has the moral clarity of defiance; pulling back has the cold strategy of law. You think of faces, of porches that will flood if the barrier sets the"
    "tide against them, of Juno's laugh on the promenade that still haunts you when waves get louder in the night."
    hide kai_navarro
    hide mara_linh_alvarez
    hide dr_leila_osei

    scene bg ch5_4001e7_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Radio static clicks into a voice—unfamiliar, official—muffled by distance.]

    "Juno (whispering, near your elbow)" "If they drag us off the flats they’ll put me in cuffs for sure.' (His voice cracks; bravado barely masking fear.) 'I—Mara, what if they hurt someone?"
    show mara_linh_alvarez at left:
        zoom 0.7

    mara_linh_alvarez "We planned medics. We planned warm routes. Leila’s right—callouts only. No sudden moves."

    menu:
        "Tighten the knots on the webbing":
            "Your fingers find the familiar muscle memory; ropes cinch smoother and the line breathes easier."
        "Hand Juno an extra thermal":
            "He accepts it with a muttered thanks; his shoulders drop a degree, small relief like slack rope."

    menu:
        "Step forward and start the chant louder":
            "Your voice catches other voices. For a moment the night is a single sound; hands squeeze with new will."
        "Stay quiet, listen":
            "You let Kai's breath anchor you; you hear the truck's tires sloughing sand—an audible threat, precise and immediate."

    menu:
        "Take Kai's hand":
            "You squeeze, a silent pact; for a second your world narrows to the warmth of his palm."
        "Stand apart and watch the perimeter":
            "You step back, giving yourself space to think; the distance makes the decisions look sharper and lonelier."

    jump chapter6
    return
