label chapter8:

    # [Scene: The Drowned Orchard | Night — Storm]

    scene bg ch8_6b08b4_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, rolling cello; a distant percussion like thundered footsteps.]
    # play sound "sfx_placeholder"  # [Sound: The orchard's wooden stilts groan; the sea hurries like someone running late; ropes snap with a wet, thin scream.]
    "You wake to the sound — not a voice, not quite a human noise — a snapping, a rope easing out of its knot, the kind of small catastrophe that becomes large before thinking catches up."
    "The room of sleep folds away and you are already upright, the brass tidewatcher cold against your sternum where it slides under your shirt."
    "Outside the Drowned Orchard is a ruined constellation. Rain comes sideways, sharp and stinging; each drop tastes of salt and the sharpness of ruined plans. Lanterns you and volunteers stitched together bob like small surrendered stars,"
    "dim halos dragged along by the tide. The raised walkway you helped anchor only weeks ago has broken somewhere along its span; a plank the width of your palm spins in the current."
    "You do not let yourself count how long it takes to cross the distance from the boardwalk to the orchard. Your boots are full of water by the time you reach the edge. The air is"
    "thick — not only with rain, but with the metallic tang of worry, the smell of wet wool and soaked yarn, the oil of a hundred hand-mended things being washed out."

    scene bg ch8_6b08b4_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: An instrument chirps fast as a heartbeat.]
    "'Ruben!' Cassian Rhys's voice cuts across the storm, ragged from running. He is paint-smeared — a smear of yellow across one cheek, the sleeve of his jacket plastered to his arm. His knuckles are crusted with"
    "salt and pigment; the harmonica in his satchel rattles when he grabs at it in a way that makes you want to laugh and then forget why laughter exists."
    "You see him before he sees you: old hands, smaller somehow when they're wet; a cane that catches the moonlight and flakes away like bark. The surge finds the orchard's weakest seam and takes it like"
    "a thoughtless mouth. Ruben's feet find nothing. He is swept out of the walkway and into a pocket of foam where the lanterns bob and the water is suddenly full of threads and leaves and the"
    "smell of overturned earth."
    "You move because moving is the only prayer you know."
    "Your hands find his coat, pull. Someone else — Nadia — has a good grip on his collar; Asha is already checking his pupils, murmuring numbers into a tablet as if reading tides out loud. Cassian"
    "Rhys is at the edge, and he doesn't move until you pull Ruben up and into the boardwalk; then his face is the hollow of a place the sea has chiselled out of him."
    "Ruben coughs and tastes of rain. He is smaller than you remember; the cane lies in pieces at his feet, splintered like an old promise. He laughs once, a wry, wind-bent sound that could be a blessing or a lament."
    show ruben_ortega at left:
        zoom 0.7

    ruben_ortega "Used to think the bay's teeth were gentle. Not tonight, eh?"
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "You're alive. That's what matters. Breathe. Hold my hand."

    ruben_ortega "You're young, Mira Kestrel. You never did let the sea break you gently."
    show cassian_rhys at center:
        zoom 0.7

    cassian_rhys "We should have seen the seam. We—"

    mira_kestrel "No. We didn't. We read what we could. We reinforced where we could. Pointing fingers now won't make the walkway whole."
    "Cassian Rhys looks at you, paint dark in the creases of his palm. He wants something — blame to push outward, or to pull inward; you can't tell which he needs most. His jaw works; he swallows and then speaks again, softer."

    cassian_rhys "Ruben falling — it makes the whole plan look like a child's raft, Mira. People will see that. Jonah will make them see that."
    "You taste guilt like iron. Your fingers are still slick with water and you slide the sensor unit into your palm. The LED blinks green once, then flares orange as the module's small antenna picks up"
    "a chorus of data. You don't trust impressions tonight; you trust numbers because numbers do not spare the tender."

    menu:
        "Help tend to Ruben — warm him, patch his cane, stay by his side":
            "You kneel in the rain, wrapping an arm around Ruben's shoulders, pressing blankets into his chest and letting your hands tell him he is not alone."
        "Run to the sensors and field kits — data now will keep more people safe":
            "You grab the crate of sensors and sprint back toward the greenhouse light, mud sucking at your soles; the readouts will wait for hands, but they will not wait for the sea."

    # --- merge ---
    "Continue"
    "You go both places at once and not at all; the town requires a distributed self. Nadia brings a blanket and Cassian Rhys — no, Cassian Rhys — watches you move and doesn't try to stop you. Asha is already talking into her collar, voice clipped with professional calm."
    hide ruben_ortega
    show asha_mehta at left:
        zoom 0.7

    asha_mehta "Sediment spike at 0.3 kilometers south of the orchard. Current redirected toward the western mangrove fingers. Berm integrity at sector three is compromised by erosion undercutting.' (She looks up: eyes bright behind rain-smudged glasses.) 'Mira, the sensors didn't predict this redirection. The model didn't include the combined overflow from last week's sap run."

    mira_kestrel "Run the high-resolution log. Cross-correlate with the tidewatcher—now."
    # play sound "sfx_placeholder"  # [Sound: Your tablet burbles, spitting out graphs. Rain hisses on the screen like static.]
    "You run the data with your fingers that no longer feel steady. The readouts scream: sediment pulses, scouring undercut zones, currents that loop back into the town's narrow channels. Where the community planted marsh grass is a ragged line; where your berms were piled, water finds teeth and gnaws."
    "Somebody begins to shout. Voices fold into one another like torn maps. You can hear grief begin to shape into blame."

    "Neighbor 1" "You told us grass would hold—"

    "Neighbor 2" "We trusted those diagrams—how could you let this happen?"
    hide mira_kestrel
    show nadia_kestrel at right:
        zoom 0.7

    nadia_kestrel "Stop. You're all breathing and afraid. That's where we start, not accusation."

    cassian_rhys "They need someone steady at the front. Jonah will be here with cameras in five. He'll make this proof he promised. He'll stand in a suit and lay a finger on a plan like it's the only way."
    "You picture Jonah Hale's neat coat against this rain, the silver pen that signs agreements that shift landscapes. You picture his cool eyes scanning for efficiency where there is heartbreak."
    hide cassian_rhys
    hide asha_mehta
    hide nadia_kestrel

    scene bg ch8_6b08b4_3 at full_bg
    show jonah_hale at left:
        zoom 0.7

    jonah_hale "I'm sorry for everyone's scare tonight, but this is exactly why we need a reliable engineered barrier. Nature-based approaches are vulnerable to... anomalies. We need measurable, robust infrastructure."
    show cassian_rhys at right:
        zoom 0.7

    cassian_rhys "You need this to be true so your investors can sign. You promised a solution, Jonah. You promised certainty."

    jonah_hale "I promised safety. I'm offering protection that won't float away with the lightest storm. We can secure the waterfront and bring jobs. Right now, this incident is the best argument for that."
    "Mayor Lin Park is already here, coat clasped, mayoral composure thin as vellum. She looks exhausted in the way people do when they have to be the calm in a tidal room."
    show mayor_lin_park at center:
        zoom 0.7

    mayor_lin_park "Mira Kestrel. The grant for our hybrid pilot — it's contingent on demonstrable progress. If the consortium uses this at the hearing, the town could lose access to funds earmarked for reinforcement. We could be frozen out."
    hide jonah_hale
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "If we lose the funds, what else falls apart?"

    mayor_lin_park "Services. School programs. Either we take big investment that buys stability or we double down on uncertain measures that ask people to risk their homes."
    "Your chest tightens like a band. The orchard's knitted lights float, each bob a small lit memory of dinners, of children's laughter, of Ruben's long stories about tides. You think of Nadia's bright hoodie, of children"
    "who learned to plant marsh grass with sticky fingers. You think of Cassian Rhys's stubborn optimism, now raw at the edges."
    "A chorus of accusations rises when Jonah Hale speaks to a camera — a line of people with their faces washed out in lamplight. Some want to sue; others want the mayor to declare an emergency;"
    "a small group forms at the edge, fists clenched, mouths forming plans that involve barricades."

    menu:
        "Step between Jonah and the crowd, ask for a calm hearing":
            "You move forward, voice steady through the rain: 'We will not let tonight be a spectacle. Sit with us. Look at the data first.' The crowd's noise dims, if only by a degree."
        "Let Cassian speak—he's good at stirring people, and this might be the spark we need":
            "You step back and let Cassian Rhys climb onto a crate, paint-dark on his hands. He calls for a halt to construction, and the crowd leans in like it's an answer."

    # --- merge ---
    "Continue"
    "Things pivot on breath and choice. You're not naïve — you know the cost of every option laid before you like a set of maps: a relocation, a blockade, a last-ditch bureaucratic appeal. Each carries a"
    "different kind of loss. Each demands a form of courage you may not be sure you hold."

    "Ruben, wrapped in a tarpaulin, coughs and says, voice gravel-soft" "We always make our choices by the light in our hands. Tonight the light's guttering. Don't let it go out without asking why it struggled."
    hide cassian_rhys
    show asha_mehta at right:
        zoom 0.7

    asha_mehta "If we can show the Mayor the emergency data — the sediment scour and unexpected current nodules — she can pause construction. It buys time for redesign."
    hide mayor_lin_park
    show cassian_rhys at center:
        zoom 0.7

    cassian_rhys "Time is what they sell, Mira. Time is what their contracts eat. If we blockade, national attention will force accountability. People will see what's happening. If we stay polite, if we wait, we will be drowned in paperwork while our houses are salted."
    hide mira_kestrel
    show mayor_lin_park at left:
        zoom 0.7

    mayor_lin_park "Escalation risks criminal charges. It risks the town's reputation and the trust of regional partners. I need a path that secures shelter tonight for those at immediate risk."
    hide asha_mehta
    show jonah_hale at right:
        zoom 0.7

    jonah_hale "We can draft a relocation support package — voluntary, supported — to move vulnerable households into safer units while we build a protective project. It preserves lives and shows decisive action."
    "Silence collapses into the sound of rain. The orchard's lanterns circle in the surf, tiny moons on a bruised sea."
    "Your hands find the tidewatcher; its brass feels like an old truth. The sensor tablet at your belt thrums with raw numbers. The town looks at you, partly in accusation, partly in hope. No matter the"
    "past that brought you here, the choice now will set the town's shape for years. You feel the moral geometry as a weight across your shoulders."
    # play music "music_placeholder"  # [Music: The cello holds a single drawn note; the rain is suddenly very loud.]
    "You breathe, counting, as if counting might make the next step less likely to fracture."

    menu:
        "Organize a voluntary, supported relocation for the most vulnerable neighborhoods and negotiate protections for those who stay.":
            jump chapter9
        "Amplify direct action: blockade construction sites, escalate national attention to force a different political calculus.":
            jump chapter12
        "Bring emergency data to Mayor Lin and demand an immediate pause and redesign.":
            jump chapter9
    return
