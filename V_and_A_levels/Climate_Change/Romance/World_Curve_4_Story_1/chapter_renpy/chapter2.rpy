label chapter2:

    # [Scene: The Flats | Morning]

    scene bg ch2_c4ca42_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft thunk of a corer entering silt, distant gulls, a volunteer laughing as a boot slips.]
    # play music "music_placeholder"  # [Music: Warm, steady acoustic rhythm — hopeful but measured]
    "You wedge the corer into the mud and feel the give — slow, layered, like history revealing itself in compacted lines. Your fingers are cold in the glove, but your palms remember the motion: steady pressure, a soft twist, then the satisfying suction as the tube comes free."
    "You read the strata aloud because it helps you make sense of it out loud. The volunteers write numbers in their clipboards; the town's rhythm folds itself around this small, ordered labor."
    show maya_soler at left:
        zoom 0.7

    maya_soler "Okay — three centimeters of fresh silt over a denser layer. That matches last week's transect near stake F2. Hold this while I mark the depth."

    "Elena" "Got it. Do you want me to flag the location with red tape or blue?"
    "You glance at the sky — a clean band of light at the horizon, the clouds a muted slate that won't break the mood. Your Moleskine is clipped to your belt. The patched elbow on your jacket rubs against the corer handle like a reminder of yesterday's unfinished lists."

    maya_soler "Red for newly accreted silt, blue for erosion scars. If we keep the colors consistent, our mapping will read like a story."
    hide maya_soler

    scene bg ch2_c4ca42_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Engine brake, a chorus of helpful voices, the slightly amplified hum of Lina's megaphone warming up]
    # play music "music_placeholder"  # [Music: A hopeful strum that lifts the room]
    show lina_park at left:
        zoom 0.7

    lina_park "Morning, Maya! I brought reinforcements, snacks, and a volunteer who bakes absurdly good banana bread. Also—' (she brandishes the megaphone) '—I brought my voice in case we need to corral enthusiasm."
    show maya_soler at right:
        zoom 0.7

    maya_soler "Perfect timing. We could map the oyster reef lines and mark the proposed pilot channel before lunch. The more hands, the faster we can get a continuous transect."

    lina_park "Also, got a few high-schoolers who want to learn how to do a cross-section properly. They're keen. You're sure about the protocol?"
    "You feel the surge: the marsh will hold under the concentration of people who care. Hope isn't a huge tidal wave here; it's a coordinated current — practical, shared, cumulative."

    maya_soler "Start at stake A, run your tape perpendicular to the creek. Record depth every half-meter. If you find cordgrass roots, note them — we want presence and density."
    show noah_reyes at center:
        zoom 0.7

    noah_reyes "You have the most soothing way of telling us to get dirty."
    hide lina_park
    show arin_kai at left:
        zoom 0.7

    arin_kai "You two plotting world domination without me?"

    maya_soler "Just saving a bay. How's your morning?"

    arin_kai "Boat's available. My dad's crew can help haul the gear out to the reef markers. If you want manpower on the water, we've got it. Also —' (he lifts a coil of rope in a small offering gesture) '—I can navigate the shoals; I know where the old oyster beds show under low tide."
    "You watch the way his eyes crinkle when he smiles. There's a quiet steadiness there, the kind that rearranges problems into manageable pieces. It makes you want to hand him a map and a plan and trust them both."

    maya_soler "That's huge, Arin. If you can take the volunteer boat team, we can run simultaneous transects — reef mapping from the water and cordgrass density from the boardwalk."

    arin_kai "I'll take it. But only if you promise not to make me wear your lab coat."
    "Laughter ripples through the group. The sound is small but firm — a communal knot tightening into resolve."

    menu:
        "Give Arin the northern reef sector":
            "You hand him a laminated map with the northern markers circled. He nods and takes the map with the casual ease of someone used to reading water. He slings the rope over his shoulder and moves toward the boat with the volunteers in tow."
        "Keep the northern sector and take the boat yourself":
            "You hesitate, then fold the map back into your Moleskine. The idea of measuring from the boat holds a particular intimacy — the tide under your hull, data flowing in your hands — but you smile at Arin and hand him the map anyway, trusting his knowledge."

    menu:
        "Stay and help the high-schoolers with data entry":
            "You kneel beside the kids with a tablet, showing them how to log coordinates and explain why consistency matters. Their faces tighten with concentration, and one of them looks at you like they've been handed a secret."
        "Take the afternoon to compile the draft presentation with Lina":
            "You step back from the transect line and side-step toward Lina's van, the human tide carrying the last markers to the boardwalk. Compiling is different work — arranging the day's small triumphs into a story that decision-makers can read — and it pulses in you with a quiet urgency."

    jump chapter3
    return
