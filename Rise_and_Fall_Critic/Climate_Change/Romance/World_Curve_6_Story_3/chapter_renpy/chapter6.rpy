label chapter6:

    # [Scene: Flooded Promenade | Late Afternoon — After Storm]

    scene bg ch6_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, slow cello underlined with distant brass — a mournful, steady pulse]
    # play sound "sfx_placeholder"  # [Sound: The slap of water against boots, an intermittent megaphone crackle, camera shutters like rain]
    "You stand waist‑deep in water that has the cold bite of remembered winters. The wet fabric of your trousers draws at your skin; each inhale pulls the salt and diesel of the bay into a throat"
    "that has learned to hold its words until they carry weight. Around you, people link arms like human scuppers — a line of bodies against something that wants to erase them. Tomas's voice rides the low"
    "hum of the crowd, rough with sea and decades of weather."
    show tomas_belmar at left:
        zoom 0.7

    tomas_belmar "We've lived with tides our whole lives. We don't need a wall that pushes us out."
    "He slams the microphone down and the chant picks up: names of lost shops, names of streets, the litany of small violences disguised as progress. Elena is there, paint flecks on her overalls, eyes bright with"
    "rain and something else — a fierce, uncontainable thing that looks like hope folded thin."
    show elena_torres at right:
        zoom 0.7

    elena_torres "This bay remembers us. It remembers our names. It won't be sold."
    "Your fingers find the pendant at your throat without thinking — a small, private anchorage. You taste the metallic residue of salt and adrenaline. Cameras arrive first as lenses, then as a tide: phone screens, a"
    "television crew with a tripod that sinks half an inch into the wet cobbles, a drone whirring above like a patient gull. Flashlight beams cross wet faces and turn the promenade into a mosaic of reflected"
    "indignation."

    menu:
        "Step forward and take the megaphone":
            "You lift the megaphone to your lips. Your voice comes out cracked and clear; you say the plan plainly—what a living seawall is, and why displacement is not a solution."
        "Stay linked and let Tomas and Elena speak":
            "You press your shoulder against the neighbor's and let their words carve the headlines. Your presence is the needle that holds the seam; your story sits quieter in the crowd, but no less firm."

    # --- merge ---
    "You choose, but the choice doesn't change the tide of cameras — the story finds its angle regardless. Cass's security detail moves at the edge of the crowd like an offered hand, then stops; the mayor"
    "herself appears under a blue umbrella, her face cast in soft lines of responsibility and calculation."
    show cassandra_cass_green at center:
        zoom 0.7

    cassandra_cass_green "Mara—"
    hide tomas_belmar
    show mara_evans at left:
        zoom 0.7

    mara_evans "You don't have to call me that here."
    "She steps close enough for the microphone to catch the rustle of her coat. Her voice is careful, practiced."

    cassandra_cass_green "I hear you. I—I'm asking for a pause on the review. We're opening mediation. No contractor inspections until we have it."
    "A ripple of cautious applause — relief like a pulled breath. But your internal ledger ticks with conditions: 'pause' is not 'no'; 'mediation' is not 'moratorium.' You scan her face for a crack; there is empathy"
    "at the corners of her mouth and the ghost of a ledger running behind her eyes."

    mara_evans "That's a start. What does 'mediation' mean—time, scope, who sits at the table?"
    "Cass's answer is diplomatic but precise; she gestures toward the row of aldermen in their dry coats by the dais of a temporarily-set-up press area."

    cassandra_cass_green "Emergency pilot approval. Time‑limited. Reporting requirements. We'll bring technical partners and community representatives to the table."
    "Your chest tightens as if the water around you had an opinion. The word 'pilot' rings with the softness of impermanence. You know pilots can be scaled into permanence — or folded away when it is inconvenient."

    menu:
        "Press for an explicit moratorium in public":
            "You step into the light and demand more from Cass on the spot. She nods, her jaw set; a camera leans forward. For a heartbeat it feels like you can force the ledger to change columns."
        "Accept the emergency pilot and insist on community co‑design for the scope":
            "You agree, but you make goodness a condition. The mayor writes down names. Priya's tablet appears in your mind: metrics, oversight, co‑design workshops. It's not everything, but it makes a map of accountability."

    # --- merge ---
    "Cass hesitates at your insistence and then, with a small concession that feels like a borrowed timepiece, agrees to include community representatives on the steering committee. The mayor's press release will say 'inclusive approach' and the cameras nod along, satisfied."
    "Noah Ríos appears beside you, water darkening the hem of his pants, curls plastered to his forehead. His smartglasses are smeared with salt; when he smiles it's slow and nervous, like someone who has been holding their breath and discovered that air still exists."
    hide elena_torres
    show noah_ros at right:
        zoom 0.7

    noah_ros "I got the mats loaded into the staging trucks. We can weave the sensors into the modular strips tonight. If we stream the attenuation data to the council, it's hard to ignore."

    mara_evans "Do you trust it? Really?"
    "Noah Ríos's hands are still trembling from the cold and the adrenaline, but his fingers find yours in the shallow water. The contact is small and human and immovable."

    noah_ros "I trust it enough that I'm willing to let the city watch it fail, if that's what happens. But I don't think it'll fail. We've tested the dampening curves. We have baseline models. We just need them to look."
    "You and he talk like people piecing together a machine from memory: sensor latencies, power storage, the way kelp beds change the frequency of waves. Each technical sentence folds into a sentence about people — what"
    "happens to a shop that floods, what happens to children who learn tides as calendar."

    noah_ros "If we can show real reduction in force at critical intervals, neutral aldermen will stop reading the op‑eds and start reading the graphs."

    mara_evans "And Arman?"

    noah_ros "He'll spin. He always does. But if public data says otherwise, that machine grinds a different way."
    # play sound "sfx_placeholder"  # [Sound: A rising murmur — distant engine noise, then Arman Kade's voice on a public address feed; his PR team frames him in a wet suit and a smile]
    hide cassandra_cass_green
    show arman_kade at center:
        zoom 0.7

    arman_kade "I welcome collaboration. Efficiency is what keeps our city functioning. Let's sit at the table."
    "There is a thud in your chest; the offer tastes like smoke. It's a foothold and a threat, both."
    "Tomas, ever direct, scans the crowd and then Cass, then Arman Kade on the screen."
    hide mara_evans
    show tomas_belmar at left:
        zoom 0.7

    tomas_belmar "He says 'collaboration' and expects our backs. We don't negotiate away homes."
    "Elena laughs then — a high, wet sound that turns into a sob and then into a wordless exhale. You step into her and loop an arm around her waist, pulling her close until the salt water and her breath and your heartbeat make a shared rhythm."
    "Elena: (between laughs) 'We made them listen. For now.'"
    "Her laugh is small and jagged, edged with exhaustion. You hold her because no one else will, because your arms can still make space for someone who needs to be held."

    menu:
        "Let Noah pull you into the celebration":
            "Noah's fingers squeeze briefly. He grins in that crooked way and you let the warmth spread—solid and human among the wet cold."
        "Stay focused on the logistics — the mats, the data feeds":
            "You nod toward the staging trucks and pull Noah with you; celebration can wait. The sensors need to come online cleanly. The victory means nothing if the numbers don't stand up."

    # --- merge ---
    "But even small celebrations are threaded with worry. Cass's conditional approval comes with strings: a strict pilot scope, reporting deadlines that will eat into volunteer hours, and municipal oversight that could, if mishandled, become a chokehold. You can feel the future arriving already wrapped in paperwork."
    "Priya arrives at your elbow, tablet in hand, her brow furrowed in the kind of concentration that has wiped nights from her face."
    hide noah_ros
    show priya_anand at right:
        zoom 0.7

    priya_anand "I'm pulling the dashboard now. Noah Ríos, route the sensor feed to the council channel and to an independent mirror. We need redundancy and public access. If the data's open, it's harder to bury."
    hide arman_kade
    show noah_ros at center:
        zoom 0.7

    noah_ros "Got it. We'll set the hash verification and timestamping. And—' (he hesitates, voice quiet) '—we'll make the analytics readable. Not just engineers. People need to see the wave disappear."
    hide tomas_belmar
    show mara_evans at left:
        zoom 0.7

    mara_evans "Make it human. Show them a child's play mat on the other side of the promenade that doesn't stretch into a moat when a surge comes."

    priya_anand "I'm already formatting the story overlays."
    "The mats go out that evening with the slow, steady grace of people who have practiced humility and urgency. Volunteers wade into the shallows, anchor points hammered into the cobble where they will hold the mats"
    "like scars against the water. Sensors blink and send their first electronic sighs into the network: tiny numbers that mean so much when translated into the language of policy."
    hide priya_anand
    hide noah_ros
    hide mara_evans

    scene bg ch6_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A soft tone as each sensor syncs; the crowd hushes as the first graphs are projected]
    "An alderman you didn't expect — one who often sits on the fence — watches the projection and presses a wet thumb to the glass as if to press the numbers into the world. The graph"
    "dips where the living wall absorbs the blow. Neutrality slides toward curiosity, then to a kind of acquiescent admiration."

    "Alderman" "That's... notable. If that holds across a storm, we should consider expansion trials."
    "You feel a strange mix of triumph and fatigue. It's not triumph perché—it's weathered, taxed. The crowd exhales and someone starts the chant again, only softer this time, as if afraid to break the fragile thread."
    "Arman Kade's initial PR steam slows into a more cautious cadence. He sends a representative down the promenade, then steps back and issues a public statement offering to 'sit at the table.' You watch the clip"
    "on a projected screen: the smile is the same as ever, practiced for donor luncheons and ribbon cuttings. The offer is a concession and a recalibration of the battlefield."
    "Elena pulls you into the middle of the street where the puddles hold your reflections like small, imperfect mirrors. She laughs again until it breaks, and tears smear the paint on her cheeks so it looks like sunrise on a storm-touched face."
    show elena_torres at left:
        zoom 0.7

    elena_torres "You did it. We kept our strip. They can't call it fate anymore."
    show mara_evans at right:
        zoom 0.7

    mara_evans "We bought a stretch of time, and a demonstration. We made them look."
    "Her laugh breaks into a sob that is almost a laugh, and you fold her close against the soggy hem of your coat. Around you people congratulate, argue, make lists, exchange a dozen small practicalities that"
    "will become the scaffolding of the pilot: schedules, sign-up sheets, legal aid clinics at Tomas's suggestion."
    show tomas_belmar at center:
        zoom 0.7

    tomas_belmar "Don't celebrate too loud,' he says, not unkindly. 'Pilots are paperwork and politics."

    mara_evans "I'll take paperwork over bulldozers."

    tomas_belmar "That's the kind of pragmatism that keeps boats afloat."
    "Noah Ríos leans into you then, voice low and threaded with relief and a residue of fear that will not leave him unmarked."
    hide elena_torres
    show noah_ros at left:
        zoom 0.7

    noah_ros "I saw your signature in the steering committee list. You pushed for community seats hard."

    mara_evans "Because if we don't sit there, someone else will write the minutes."
    "He smiles, and for a fraction of time the damp curl of his hair looks like a promise rather than a worry. You tuck a strand behind your ear, fingers still smelling of oil and kelp."
    "But you don't let yourself believe in a clean victory. Cass's approval is conditional: the pilot is time‑limited, the scope narrow, the reporting frequent. Every concession you accepted to get the mayor to the table is"
    "now a line on which future debates will hinge. You can see it all forming—the deadlines that will demand staff, the evaluations that will require numbers, the politics that will try to slid the pilot into"
    "a checkbox."
    "You step aside and open your notebook, fingers nimble despite the cold. You write down a list: independent auditors, community liaisons, a rotating schedule so no one burns out, Priya's dashboard link, Noah Ríos's hardware checklist. Each line is a promise to yourself and a ledger out in the open."
    hide mara_evans
    hide tomas_belmar
    hide noah_ros

    scene bg ch6_601bcb_3 at full_bg
    # play music "music_placeholder"  # [Music: Cello motif returns — a slow downshift into minor, threading the victory with a question]
    "Across the street, reporters push for quotes. An interviewer asks for a sound bite that will fit into a thirty-second slot. You frame a sentence that is true and unvarnished."
    show mara_evans at left:
        zoom 0.7

    mara_evans "We won this strip because we refused to be priced out of our lives. We will show, with work and care, that protection doesn't mean dispossession."
    "The interviewer nods, satisfied, and the clip will loop later with a lower third that says 'Local Resistance Triumphs'. But inside the clip, in the long, unsponsored gestures between sentences, the work is visible: the damp gloves, the foam anchors, the tired blush that no camera oil can fix."
    "Arman Kade approaches the edge of the crowd at dusk, the sodium lamps throwing hard light on his coat. He looks at the mats, at the volunteers, at the faces—calculating, measuring. For a moment you feel"
    "the old dread press at your sternum, but it is tempered by the sight of the sensors blinking steady in the dusk, like a small defiant constellation."
    show arman_kade at right:
        zoom 0.7

    arman_kade "You made a persuasive case. Keep me informed. There's room for cooperation."
    "You see the offer and the undermining both; you see the map he imagines—a city divided into protected parcels— and you hear, too, the splintered enthusiasm of your neighbors, who will now have to keep watch not just against the sea, but against the slow erosion of political will."

    mara_evans "We'll sit at the table. We won't be silent there."

    arman_kade "Good. We'll have your technical reports on the first weekly review."
    "His voice is smooth; the promise is paper-thin."
    "You look at Noah Ríos, at Elena, at Tomas, at Priya with the tablet tucked under her arm like a modern talisman. You feel, in your chest, the same sharp little sorrow that first drove you"
    "back here years ago after a storm took your family's storefront. This victory is a slice of relief; it is not the end of the arithmetic on whom the city chooses to save. You can see"
    "the long negotiation ahead like a map of low, dangerous shoals."
    "Noah Ríos squeezes your fingers and leans his head against yours. It's brief. It is enough."
    show noah_ros at center:
        zoom 0.7

    noah_ros "We'll write the reports honest. We'll make sure the data is messy and public. We'll give them a reason to keep looking."

    mara_evans "And if they don't?"
    "Noah Ríos's jaw tightens for a half-second — the part of him that fears not being enough flickers."

    noah_ros "Then we'll keep building. We'll take this model where we can. We'll show that it works and that people deserve it."
    "You nod. There is a comfort in the plan, even as the plan acknowledges further storms."
    hide mara_evans
    hide arman_kade
    hide noah_ros

    scene bg ch6_601bcb_4 at full_bg
    # play music "music_placeholder"  # [Music: A single violin note that holds, then resolves into a minor chord]
    "You walk the stretch of saved shoreline once more when the crowds thin, barefoot in the wet, boots squelching in the mud. Elena's laughter has turned to a quieter, steadier hum as she calls out names"
    "for tomorrow's volunteer roster. Tomas sits on a crate and smokes, looking out at the water with the expression of someone who has seen too much and still chooses to be present."
    show tomas_belmar at left:
        zoom 0.7

    tomas_belmar "You did the thing we couldn't when the storm took us. You made them listen."
    show mara_evans at right:
        zoom 0.7

    mara_evans "We made them look. That's the start."
    "He grunts, which is his version of agreement. The sky is a bruised indigo, low and close. Light from the city limns the clouds from below, making the horizon a thin, stubborn line."
    "You think of the people who will come next week and the week after, of the deadlines Cass has set, of Arman Kade's recalculated strategies and the way money reshapes conversations. You are tired in a"
    "way that goes deeper than muscle — tired in the particular bone-deep way of people who have watched their lives threatened and decided to make a plan anyway."
    "You close your notebook and press it to your chest like a map. For tonight, the street holds its own. For tonight, Elena laughs and the neighbors sing and Noah Ríos's hand in yours is warm"
    "and real. For tonight, the living seawall stands where the city said nothing noble could."
    # play music "music_placeholder"  # [Music: The cello and violin blend into a hush; the soundscape narrows to wind, water, and soft human voices]
    hide tomas_belmar
    hide mara_evans

    scene bg ch6_601bcb_5 at full_bg
    "You know the mayor's approval has strings. You know the pilot will require more than goodwill. You also know that for the first time since your storefront was taken, you can imagine a future where your"
    "neighborhood remains in place—not because it's cheaper, but because it is worth defending. The victory tastes of salt, tired hands, and the knowledge that a fight postponed is not a fight won."
    "You tuck the pendant back into your shirt and look at the stretch of shore you helped save. There is a small, private gratitude that settles like a stone: you've bought time. You've made something real"
    "enough to show. And in the quiet under the city's lamps, that is both fragile and fierce."
    # play sound "sfx_placeholder"  # [Sound: Distant applause dies down; a gull calls once and then is gone]
    # play music "music_placeholder"  # [Music: A final, low chord — not triumphant, but steady]

    scene bg ch6_601bcb_6 at full_bg

    scene bg ch6_601bcb_7 at full_bg
    "THE END"
    # [GAME END]
    return
