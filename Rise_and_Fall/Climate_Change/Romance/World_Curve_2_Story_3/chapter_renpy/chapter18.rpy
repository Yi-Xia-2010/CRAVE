label chapter18:

    # [Scene: Tidewatch Lab | Morning]

    scene bg ch15_f99e88_1 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano, slow and uneven; a distant, steady hum of refrigeration]
    # play sound "sfx_placeholder"  # [Sound: Distant truck engines; the slap of paper against glass in the breeze]
    "You wake to a silence that tastes like waiting — the kind that has a rhythm of its own and a meter you can count on. Your notes are stacked where you left them; the models"
    "blink quietly on the tablet like patient witnesses. The inbox has two new threads: one from the external peer you sent the data to, confirming review, and another from council staff noting that funding will be"
    "withheld until the review completes. The word withheld sits in your head like something small and hard."
    "You know what 'withheld' will do in practice. It slows the grant money, delays contracts, turns plans into promises. It also buys time for the truth to be tested. For a moment you let both realities"
    "meet: the relief that scientific rigor might prevent a worse outcome, and the immediate scar of a town that needs visible defense now."
    "You can feel Luca's presence already, even before he opens the door — the way the lab breathes faster when he comes in. He steps inside with salt on his jacket, eyes wide, a courier's breath of diesel and optimism."
    show luca_moreno at left:
        zoom 0.7

    luca_moreno "They redirected the crews before dawn. The developer's crews — armored rigs, contractors with badges — they're building that emergency wall on the promenade. It's flashy, Isla. People are lining up to watch. They think it's security."
    show isla_morgan at right:
        zoom 0.7

    isla_morgan "You think I wanted to stall, Luca?' (Your voice is steady but small; you catch the edge of your own guilt in it.) 'Peer review isn't stalling — it's protection against a decision that could make erosion worse."

    luca_moreno "Protection doesn't bail out a flooded house.' (He runs a hand through his hair, impatient.) 'We told people a community plan would keep them safe. They waited. And now anyone who can drive a rig is putting concrete where it looks dramatic."

    isla_morgan "And if the concrete makes the next high tide smash that promenade like a knife through paper? We hand them an illusion, not resilience.' (You lay a finger on a map, tracing the channels where the breakwaters should spread energy gradually.) 'I'm trying to keep the evidence and the community from being pitted against each other."

    luca_moreno "You're keeping them from action.' (He leans closer, words quick.) 'I can't convince people to hold until a paper is finished. They want to see something — anything — that says they'll still have a home."

    isla_morgan "We are doing actions. The living breakwaters aren't glamorous; they take coordination and time. But rushing the wrong fix will make everything worse."
    "Luca's jaw tightens; for a second he looks younger than he is, fed up with the world’s slowness."

    luca_moreno "So what do you want me to do? Write them postcards? Organize candle vigils?"
    "You and Luca circle each other on the floor of the lab like two birds on a single wire. You both know there are no perfect answers, only tradeoffs whose costs will be paid by someone."

    menu:
        "Call the foremen and try to re-route crews":
            "You find the number, your thumb hovering over the screen. You force the call, your voice practiced and persuasive, but the foreman tells you the contracts were reassigned. Money overrides pleas. You hang up with your mouth tasting like rust."
        "Go to the Salt Flats with Luca to show people the consequences":
            "You grab your waterproof and Luca's handfalls into place beside you. At the flats you stand in the wind and show the models to anyone who will look — your words carve shapes into the air but they are small against the machinery's clatter. You leave a few more doubters than you expected; you also leave a growing line of people who will not forget what you said."

    # --- merge ---
    "You choose neither conclusively; both choices feel like small stitches. The rain thickens outside."
    # [Scene: Salt Flats | Afternoon]
    hide luca_moreno
    hide isla_morgan

    scene bg ch15_f99e88_2 at full_bg
    # play music "music_placeholder"  # [Music: Low brass with an insistent metallic rhythm]
    # play sound "sfx_placeholder"  # [Sound: Diesel engines, the distant clang of pile-driving, gulls crying above]
    "The developer's emergency fortifications rise in regimented rows along the promenade — tall, smooth sections of concrete that gleam in the wet. They are efficient at a glance: shiny, photograph-ready, and positioned where a camera will"
    "capture their defiance against the sea. Where you had planned staggered, permeable reefs to slow waves and feed habitats, the developer placed a straight, impermeable line that will likely redirect erosive force elsewhere."
    "You stand on the flats and watch as a foreman points at your maps with a glove that smells of oil. Luca has gathered a ring of young volunteers and a handful of elders who remember"
    "the old channels. The crew works where the money tells them to, and you can feel the living breakwater project losing time with each lifted girder."
    "You walk up to the foreman; he looks at you like a problem solved."
    show isla_morgan at left:
        zoom 0.7

    isla_morgan "You're redirecting the crews from the reed-bed arrays. Those arrays diffuse the energy — the straight wall will concentrate wave force at the headlands."
    "Foreman: (shrugging) 'I don't pick the spots, miss. I build what I'm paid to. If the council wants a different plan, they can pay us for it.'"
    "Luca Moreno: (to the gathered crowd) 'This isn't about aesthetics. If we let them bank on spectacles, they'll promise jobs today and sell our shoreline tomorrow.'"
    "A woman near you — a homeowner — folds her wet coat tighter, eyes shiny."

    "Homeowner" "You two have been arguing for months. We need our roofs to stay put."
    "You feel the guilt spike like cold. You want to tell her that the living systems can keep roofs intact in the long run — but you also know 'long run' doesn't help a single shattered mattress."

    menu:
        "Offer to help shore a neighbor's foundation tonight":
            "You move through the crowd with sacks of sand and a borrowed pump. You and Luca and half a dozen volunteers patch what you can with your hands and sweat. For a brief, luminous hour you are enough."
        "Return to the Tidewatch Lab to protect the data and coordinate remotely":
            "You let Luca carry the field work. Back at the lab you shore up files, encrypt transmissions, and write an emergency brief for the external reviewer. The work feels necessary and cold; it does not soothe the homeowner with the wet coat."
    "THE END"
    # [GAME END]
    return
