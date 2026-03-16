label chapter4:

    # [Scene: Stormwall Construction Site | Late Afternoon — Overcast, wind picking up]

    scene bg ch4_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, rhythmic thud of machinery, a low wind beginning to rasp through rigging]
    # play music "music_placeholder"  # [Music: Low, tense strings undercut by the pulse of construction]
    "You arrive with the weight of the council vote still settling in your sternum—Route A written across the town ledger now, the town's breath held in the scaffolding you've helped authorize. The modules are beautiful in"
    "their harshness: geometric, efficient, a promise measured in cubic meters. They smell of wet concrete and diesel, and their surfaces are slick with sea spray."
    "You should feel relief. Instead you feel the small, pricking alarm that comes before real weather."
    "Mateo Hale meets your eyes without looking like he’s looking. His jaw is set, mud streaking his forearms. There is relief in his shoulders—this is what he was built to do—but there is also something fragile you don't have words for yet."
    show mateo_hale at left:
        zoom 0.7

    mateo_hale "We got good placement on the north seam. If the next swell comes at an oblique angle, it'll shear the second joint, but—' (he stops himself, fingers tracing a seam in the air) '—we've got redundancy on deployment. We move fast, we limit exposure."
    "You can hear the measure in his voice: metrics, contingencies, a map of probabilities. It's steady. It is also not the same thing as comfort."
    show aria_navarro at right:
        zoom 0.7

    aria_navarro "What are our margins if the storm spikes more than predicted?"

    mateo_hale "She won't, based on the buoy reads an hour ago. But if—' (he glances toward Jun) '—if Jun's sensors missed a local uptick, we can tack more anchors. It will cost time."
    "Jun looks up, wiping hands on a rag; their face is flushed with the effort of making something small and perfect in a world that's becoming frayed. They offer a tight smile."
    show jun_park at center:
        zoom 0.7

    jun_park "I cross-checked the feeds. There was a microburst signature—small, localized. I flagged it. The municipal forecast smooths that out. It's the edge cases that bite."
    "Sora Lin's laugh is short, like a rope snapping."
    hide mateo_hale
    show sora_lin at left:
        zoom 0.7

    sora_lin "Edge cases are where the town lives. People live in edges, Aria. You promised them a future—not a bet."
    "You don't answer immediately. You are thinking of Elena's hands—callused, quick to knot a rope, quicker to stitch a net. You remember the way the crowd at the council meeting leaned forward when you said 'deployable'"
    "and 'measureable'—you remember the way their faces also held fear. You promised measure. You promised protection."
    "Elena crosses the wet ground to you, her voice steady as the tide."
    hide aria_navarro
    show elena_navarro at right:
        zoom 0.7

    elena_navarro "You did what you thought would keep our houses whole, niña. We'll see if it keeps us."
    "Her eyes are a ledger of histories: previous storms, names, repairs. There is pride there, and a thin tremor you could call worry."

    menu:
        "Step closer to Mateo and point at the north seam to suggest immediate extra anchoring":
            "You edge toward Mateo, close the distance, and your voice takes on the low calm you reserve for when facts must cut through fear. He hears you—actionable, exact. He nods once and instructs a crew to add a second cable at the seam."
        "Walk to Jun and ask them to recheck the sensor array":
            "You crouch beside Jun, fingers finding their grease-streaked ones. They warm under your palm. Your request is quieter—an appeal to verification rather than instruction—and Jun returns to the console with a concentrated set of eyebrows, relaunching diagnostic pings."

    menu:
        "Shout for an immediate evacuation of the low quay, prioritizing people with children and the elderly":
            "Your voice cuts over the rain. People respond—shouts change into a rough chorus of direction. Hands find hands, ropes are thrown, a procession forms toward the central stair. You feel the old practical magic of communal movement sweep through the quay."
        "Stay to coordinate the technical response, directing Jun and Mateo about drone lifts and seam stabilization":
            "You crouch by Jun's console, fingerprint wet smudges on the screen. You call out coordinates, align drones for lift runs, and patch telemetry through to Mateo. Your hands are busy saving people in a different register—mechanical rescue rather than physical hauling."

    menu:
        "Double down—redesign and fortify the modular wall immediately; call in extra municipal crews.":
            jump chapter5
        "Stop construction and pivot to emergency mangrove planting and community rescue—lean into local knowledge.":
            jump chapter6
        "Create an emergency mixed response: Mateo leads repairs while you organize volunteers to reinforce natural barriers.":
            jump chapter16
    return
