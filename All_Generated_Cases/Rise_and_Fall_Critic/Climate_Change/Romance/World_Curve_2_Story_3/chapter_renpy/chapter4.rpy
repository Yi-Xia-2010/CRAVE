label chapter4:

    # [Scene: Havenport Boardwalk | Late Afternoon]

    scene bg ch4_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, insistent percussion with a distant cello line]
    # play sound "sfx_placeholder"  # [Sound: Gulls, the slap of waves, the murmur of a gathered crowd; a generator hums like a nervous insect]
    "You stand at the edge of the crowd, the compass at your throat a familiar weight against your collarbone. The decision you made in the mayor's office sits heavy and hot behind your ribs: refusal. Refusal"
    "to trade the coastline for a contract. Refusal to let old ways be smoothed over by new ones that will rent the town's future on corporate terms."
    "Ivy is a spear of neon green in the swell of bodies — her safety vest a bright promise. She hands you a length of twine; her grin is quick and fierce, the kind that has stitches in it from too many scraped knees and late-night plans."
    "Elder Tomas stands to your left, small against the sky but rooted, his walking stick tapping the boards in a rhythm you feel in your teeth. Lina is three steps up on a crate, camera level,"
    "voice low into her recorder. Ariana Voss is there somewhere at the edge of the press of people — you see the flash of her yellow boots and the way her shoulders slope as she listens,"
    "hope like a breath you can almost hear."
    "You press your thumb against the compass again as if your skin could steady the needle. You do not want this to be a performance. You want it to be honest — a naming of what is at stake."
    "You climb onto a rotting crate, the wood complaining beneath your weight. The crowd hushes into a tidal hush. Salt and tar and the faint, greasy sweetness of fried food hang in the air. Someone behind"
    "you starts a chant in the old fishercall cadence; other voices fold in until it becomes a single, human drum."
    show marin_sato at left:
        zoom 0.7

    marin_sato "We are not a line item."
    "A cheer rises, sudden and sharp. You let it ride out before forcing the next words slow and clear, because the mayor tuned a microphone to you and because every syllable might be recorded into the decisions that follow."

    marin_sato "They can build stone and steel. They can promise us tides tamed. But you — our mothers, our boatmakers, our children — know the coastline is more than protection. It's memory. It's access. We will not sell that off."
    show ivy_morales at right:
        zoom 0.7

    ivy_morales "Speak plainly, Marin. Tell them what they'll lose."

    marin_sato "They already know. We have to make them feel it. Tell them about Tomas's boats. Tell them about the nursery. Tell them what we will—"
    show elder_tomas_hale at center:
        zoom 0.7

    elder_tomas_hale "Tell them the ropes have names. Tell them the nets were mended by those names. It's why we stand."
    "The crowd leans in. Lina angles her camera toward Tomas, fingers gentle on the focus ring."

    menu:
        "Open with Tomas's story — make it personal":
            "You point to Tomas and call for the names. The crowd hums; the air shifts to a hush so intimate it feels like the sea holding its breath. People begin to call out the names of their boats and lost docks, and the protest becomes a ledger of memory."
        "Start with a policy attack — call Tideguard out by name":
            "You bring up Tideguard and their glossy brochures. Someone near you shoves a printed leaflet into the air like an accusation. The mood sharpens into anger; legal teams at the edges straighten like predators sensing a scent."

    menu:
        "Step forward and offer to meet Cassian's team — diffuse the standoff":
            "You raise your hand and call for a mediated meeting. Some around you sigh relief; others hiss softly, thinking compromise is capitulation. The lawyers swap notes, eyes narrowing in the briefest calculation."
        "Double down on the boardwalk — lead the chant louder":
            "You drop your shoulders and drive your voice into a chant. The crowd matches you and grows; the lawyers retreat a hair as the sound swells, but you sense the attention hardening from negotiable to adversarial."

    jump chapter5
    return
