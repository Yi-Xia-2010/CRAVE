label chapter1:

    # [Scene: Boardwalk | Dawn]

    scene bg ch1_Start_1 at full_bg
    # play music "music_placeholder"  # [Music: Sparse, minor piano with distant, mournful cello — slow tempo]
    # play sound "sfx_placeholder"  # [Sound: Slow, rhythmic slap of water; gulls calling far off; the scuff of your boots]
    "You breathe the town in the way you always do at dawn — like taking inventory. Salt on your tongue from yesterday's breeze, the oily whiff of fried coffee from Rosa's kitchen, the sharp metallic tang"
    "of old nails and sea air. Your Moleskine is tucked under your arm, its corners softened with tide-drips and pencil smudges. The compass at your sternum is cool against the fabric of your jacket, the dent"
    "in its rim a familiar weight; you press your thumb over it as if you could steady what the sea keeps shifting."
    "The boardwalk tilts under your boots. Where the planks have bowed and split, thin rivers collect rain and tidal spray; they mirror neon from closed shop windows and your own reflection, hollowed and narrow. You catalogue"
    "everything automatically: salt stains like faded constellations, the way some railings sag toward the surf, a child's sand-splattered raincoat snagged on a lamppost. It is a ritual that steadies you — observation as prayer. You make"
    "a small list in your head, then sketch a rough cross-section in the margin of your notebook: plank, gap, rust, algae bloom — note: propose recycled plastic replacement? — but the motions feel more brittle than"
    "they have in months."
    "Ahead, Rosa's café glows like a fragile lamp in a storm. Its front window fogs with breath and steam; inside, string lights toss a honeyed pool across mismatched tables. The sound of the espresso machine is steady and human, a heartbeat you can trust."
    "Finn is at the railing, sleeves rolled, hands in the knotwork of a new line. He looks up as you approach, his jacket a patchwork of scavenged fabric and proud repairs — a personal map of"
    "every job he's ever taken for the town. He is humming under his breath, fingers looping and tightening; he always hums when he's thinking of knots, as if the rhythm helps him compute forces and futures"
    "at once."
    show finn_serrano at left:
        zoom 0.7

    finn_serrano "Morning, Maya. Tide's higher than the chart said. Could be wind, could be the—"
    hide finn_serrano

    scene bg ch1_Start_2 at full_bg
    show finn_serrano at left:
        zoom 0.7

    finn_serrano "—the ocean deciding to be ornery."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "Or the ocean doing what it always does. You're up early."

    finn_serrano "You know me. Kisses the dock, calls it by name. You look like you carried the tide in your teeth."
    hide finn_serrano
    hide maya_serrano

    scene bg ch1_Start_3 at full_bg
    show finn_serrano at left:
        zoom 0.7

    finn_serrano "Find anything good?"
    "You force a smile but your chest tightens. 'Salt patterns, warped boards. A new leak in the boardwalk past the old bait shop. I sketched the seam.'"
    hide finn_serrano

    scene bg ch1_Start_4 at full_bg
    show finn_serrano at left:
        zoom 0.7

    finn_serrano "The mayor's team coming by the hall today, right? For the funding thing?"
    "Maya Serrano: (your stomach drops) 'They were supposed to present the matching grants decision today. I—'"
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "I was counting on that."
    hide finn_serrano
    hide maya_serrano

    scene bg ch1_Start_5 at full_bg
    show finn_serrano at left:
        zoom 0.7

    finn_serrano "Hey. If it gets delayed, we can do the emergency shore reinforcement with the volunteers. We have pallets and sandbags, and Rosa's got hot coffee. We can stretch it."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "Stretching works until someone needs a new roof.' Your voice is steadier than you feel. 'The matching grant isn't just plywood and sandbags. It's the engineers we need, permits, paid labor for people who can't volunteer away their rent."

    finn_serrano "I know.' He finishes the knot with a flourish and hands you the loop. 'You always say don't fight the tide alone."
    "You curl your fingers around the rope, feeling the salt grit under your nails. The compass pendant is heavier now, a small, private gravity."

    menu:
        "Stop and trace the salt stains with your fingertip":
            "You run a finger along a white crescent and the salt flakes off like old promises."
        "Keep walking toward Rosa's without stopping":
            "You pull your coat tighter and walk faster, as if speed can outrun worry."

    menu:
        "Call Elias first — mobilize people now":
            "You dig your phone out, thumb hovering. The idea of being loud tomorrow seems like armor."
        "Start drafting the counterproposal — be the steady hand":
            "You flip open your notebook and bite the end of your pencil. Plans feel safer than shouting, at least for now."

    jump chapter2
    return
