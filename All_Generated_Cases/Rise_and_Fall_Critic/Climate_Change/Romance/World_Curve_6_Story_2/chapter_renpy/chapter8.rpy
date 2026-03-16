label chapter8:

    # [Scene: Saltgarden Research Lab | Morning]

    scene bg ch8_6b08b4_1 at full_bg
    # play music "music_placeholder"  # [Music: A soft, ascending motif — light strings and a lone clarinet]
    "Narration:"
    "You close the notebook and feel the map you've begun to draw sit like something alive in your hands. It is no longer only an argument; it's a set of places with names and borders and"
    "people meant to stand in them. The coral pendant warms against your sternum as if it, too, answers to this new shape of work."
    "Sound of distant boots and the low murmur of voices drifts from the lab's door. The lab smells of brine and the tang of algae, and the humidity leaves the fabric of your jacket damp at"
    "the collar. You let yourself—briefly—be proud. Not triumphant, not smug; just honest, which is almost the same thing when the planet keeps testing you."
    "Ilias Navarro comes up behind you, hands damp from rinsing fragments, his waterproof notebook tucked under one arm. He watches the map, then looks at you."
    show ilias_navarro at left:
        zoom 0.7

    ilias_navarro "This looks...anchored. Do you feel that? Like a line we can pass along."
    show maya_kestrel at right:
        zoom 0.7

    maya_kestrel "Anchored is the word I'm trying to be. Not permanent—adaptive. Areas that breathe."

    ilias_navarro "Adaptive is the right word. The living fragments will take faster if we stagger planting with the ebb cycles. We can show measurable improvement within months."
    "Maya Kestrel: (searching the map with your finger) 'If the marsh blocks storm surge in the pilot sectors the way Dr. Hana modeled, then we have data to bring to Ansel and to the people. Evidence makes promises easier to keep.'"

    ilias_navarro "And the promises you're making—are you certain they're the ones you want to be writing?"
    "His ocean-blue eyes flick to you, then away, looking at the greenhouse glass where rain streaks like fingers down the pane. You taste salt and the memory of the sibling you lost; for a second the room feels very large and very small at once."

    maya_kestrel "I'm certain I want people safe. I'm less certain about who loses what to get there."

    ilias_navarro "We'll make fewer 'less certain' if we keep iterating with the community. That's the thing that matters to me."
    "Narration:"
    "He reaches for your hand—an offer of closeness that is neither clumsy nor theatrical. You let the contact be a small truce against the rest of the world."

    menu:
        "Trace the new sanctuary boundaries on the map":
            "You lift the pen and add a soft dashed line where elders requested ceremonial fishing remain. The ink smudges slightly in the greenhouse humidity, but the meaning is clear."
        "Ask Ilias about sequencing the plantings":
            "He brightens, sketching tidal windows with a stub of charcoal and counting volunteers needed per shift. His optimism is logistic and quiet."
        "Step outside for a sharp coffee and air":
            "You step into the rain and let the cold slap the humidity from your face. Coffee later, you promise yourself; for now, the weather reasserts the stakes."

    # --- merge ---
    "Continue"
    # [Scene: Old Shipyard | Late Morning]
    hide ilias_navarro
    hide maya_kestrel

    scene bg ch8_6b08b4_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Clank of prefab pilings being lowered; a gull's plaintive call]
    # play music "music_placeholder"  # [Music: A steady, hopeful harp pattern underlaid with low percussion]
    "Narration:"
    "The shipyard smells of oil and mud and the heavy, metallic tang you recognize as the town's skeleton. Seren Blake's team is already there — efficient, sleeves rolled, blueprints unrolled on a weathered crate. Prefab pilings lie like a neat forest along the slip."
    "Mayor Ansel arrives with his tweed collar up against the rain, carrying the weight of the town in his posture but with relief threaded through his steps. Dr. Hana stands nearby, tablet in hand, watching the tides with professional calm."
    show seren_blake at left:
        zoom 0.7

    seren_blake "These pilings get the boardwalk up above the new high-water line. We can stage the work in sectors so business doesn't stop."
    show maya_kestrel at right:
        zoom 0.7

    maya_kestrel "Sector work is good if the timing doesn't push people out before they have alternatives. I want the sanctuaries delineated on these plans—places designated for ceremonial fishing, market stalls, and boat access."

    seren_blake "We can allocate zones. Co-governance clauses make that binding. But the board will want clear deliverables and timelines."

    maya_kestrel "Co-governance isn't a slogan. It needs teeth. Legal language. Community oversight."
    show mayor_ansel_reed at center:
        zoom 0.7

    mayor_ansel_reed "If we can show the reductions in flood frequency from the pilot marshes, the regional funders—"
    hide seren_blake
    show dr_hana_sato at left:
        zoom 0.7

    dr_hana_sato "—will back an oversight mechanism. The science supports structured monitoring. We can embed community stewards as data partners, trained to collect tidal response metrics."
    "Seren Blake studies you. Her face is composed; the glass of the nearby office pavilion reflects the harbor like a second sky."
    hide maya_kestrel
    show seren_blake at right:
        zoom 0.7

    seren_blake "I don't do loopholes. I do rapid implementation. But we can codify oversight in procurement and in the phased releases of funds."
    "You feel the weight of her words: muscle, speed, and the implied softness of concession. There is room for your map here—if you can make the language unambiguously protective."
    hide mayor_ansel_reed
    show maya_kestrel at center:
        zoom 0.7

    maya_kestrel "Then we need the sanctuaries legally protected, not just sketched on paper."

    dr_hana_sato "I can draft monitoring protocols that include cultural use metrics. Mayor, if we can thread those through procurement, we can make contractual enforcement."
    hide dr_hana_sato
    show mayor_ansel_reed at left:
        zoom 0.7

    mayor_ansel_reed "I'll bring it to the council. It will be hard. But the pilot results will help."
    "Narration:"
    "Workers move with a purposeful rhythm; prefab pilings shimmy into place with mechanical certainty. The hybrid of prefab and living restoration feels almost elegant—callused hands and precise screws paired with bundled kelp and replanted eelgrass."
    "Ilias Navarro sidles up beside you, mud on his boots, excitement threaded with nerves."
    hide seren_blake
    show ilias_navarro at right:
        zoom 0.7

    ilias_navarro "Look—Dr. Hana's numbers are good. The model says pilot sectors should see flood frequency drop by thirty percent in two seasons."

    maya_kestrel "Thirty percent. That's…that's a measurable saving. People can see that. They can feel that."

    ilias_navarro "Yeah. And the living beds will keep giving. They support juveniles, they dampen wave energy—it's not only about the wall."

    maya_kestrel "So it's science and structure. The Compromise Map."

    ilias_navarro "Your name for it is nicer than 'compromise'—sounds more hopeful."
    "You both laugh, and for a beat the shipyard's cold metal and salt smell fade into the background like a minor chord resolving upward."

    menu:
        "Ask a foreman about how leases will be handled":
            "The foreman shrugs with practiced caution but promises the contract team is drafting buy-back offers for leaseholders. It isn't a guarantee, but it's movement—paper turning into policy."
        "Push for a clause binding the pilings schedule to community review points":
            "Seren makes a note. Her expression softens in the smallest way: she respects someone who makes practicality a kind of moral pressure."

    # --- merge ---
    "Continue"
    # [Scene: Harborfront Market | Afternoon]
    hide maya_kestrel
    hide mayor_ansel_reed
    hide ilias_navarro

    scene bg ch8_6b08b4_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rustle of clipboards, the rattle of change, children's laughter in the distance]
    # play music "music_placeholder"  # [Music: Light, bright strings; flutes dance in the mix]
    "Narration:"

    "Rafi's article runs with a headline that makes your stomach do a complicated loop of relief and worry" "Compromise Map Brings Early Gains; Volunteers Flood Planting Days."
    show rafi_soto at left:
        zoom 0.7

    rafi_soto "You're getting good traction. My piece framed it as 'expedient but inclusive'—I tried to get at the nuance."
    show maya_kestrel at right:
        zoom 0.7

    maya_kestrel "Expedient but inclusive is a phrase that sounds like a press release and a promise at once."

    rafi_soto "That's the thing. People want to believe something will work. When they can plant a sucker or hold a trowel, they invest in it differently."
    "You watch volunteers sign up for planting days, noting names and phone numbers as if they were stitches you'd come back to later. The smell of frying fish from a nearby stall and the bright cashbox jingles feel ordinary and sacred at once."
    "Etta Muir passes by, shawl dripping in a polite way, and stops at your table. She runs a thumb over the map where you’ve marked a small crescent of water reserved for ceremonial net casting."
    show etta_muir at center:
        zoom 0.7

    etta_muir "You kept that little bay, didn't you? You promised me you'd keep it."

    maya_kestrel "It's written in the draft with your name on it."

    etta_muir "Don't rely on ink. Rely on people."

    maya_kestrel "I'm relying on people and making people part of the ink."
    "Etta's eyes crinkle; it's a complicated, weathered look—blessing and challenge wrapped together."
    "Narration:"
    "Volunteer sign-up rates climb. Rafi's photos—hands in mud, smiles wet with rain—travel on social threads and through the town's group chats. You feel the momentum building like a wooden wave: slow, incremental, and solidifying at the edges."

    menu:
        "Give a short, honest quote for Rafi":
            "You tell him, 'This isn't a perfect fix. It's a start that chooses people.' He grins, types the words, and the quote reads like a promise."
        "Deflect the camera and ask volunteers to introduce themselves":
            "You listen as a young teacher explains why she'll bring her class. Their reasons stitch into the story in a way a headline never could."

    # --- merge ---
    "Continue"
    # [Scene: High Tide Boardwalk | Early Evening]
    hide rafi_soto
    hide maya_kestrel
    hide etta_muir

    scene bg ch8_6b08b4_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant surf, a child's shout, a hammer's rhythmic echo as finishing touches go on]
    # play music "music_placeholder"  # [Music: Warm cello undertones lift into a major key — hopeful, measured]
    "Narration:"
    "In the pilot sectors, you start to see the shape of change. The engineered pilings lift the promenade above the worst of the last month's surge. Alongside them, the newly planted eelgrass fronds wriggle in the"
    "backwash like green fingers learning to hold. On the boardwalk you can, for the first time in months, hear the town talk in more than two registers—there is cautious optimism beneath the worry."
    show dr_hana_sato at left:
        zoom 0.7

    dr_hana_sato "Readings show reduced overtopping where the living beds were installed first. The coupling of engineered elevation and biological damping is performing as modeled."
    show maya_kestrel at right:
        zoom 0.7

    maya_kestrel "People will notice this. They'll walk further, open stalls, let children near the water again."

    dr_hana_sato "They will. And the monitoring network we've set up gives us the evidence to defend the sanctuaries."
    "Narration:"
    "A group of fishers pause to look at the planted beds. Not all faces are welcoming—some are tight with uncertainty about leases and future income—but others nod as if remembering a sense of stewardship returning."
    "Ilias Navarro stands beside you, watching the surf and the green blades waving under the water. His hand finds yours, and you feel the evening air cool on your damp skin."
    show ilias_navarro at center:
        zoom 0.7

    ilias_navarro "We did a good thing today."

    maya_kestrel "We did a thing. It's not finished."

    ilias_navarro "Nothing's finished. But—' (he searches for the word) '—it's less frightening when there's work stitched into it."
    "You both watch a child run along the raised boardwalk, splashing in a puddle safe behind the new pilings. The sight feels like a small prophecy."
    "Narration:"
    "Yet even with pilot successes, the map's edges cut into lives. You get a call in the night from a family scheduled to relocate. Their voice is raw, and you lie awake afterwards with the carved"
    "pendant warm against your palm. The map is a gift and a blade, and you carry both knowing that's how compromise often tastes."
    "You walk the shipyard's damp metal late into the night—palms pressed flat to cold steel as if to test whether futures can be rooted into something that will stay. The town hums under a safer sky"
    "in some places and frays in others. The ledger is still heavy, but there are new lines you can explain aloud now."
    hide dr_hana_sato
    show mayor_ansel_reed at left:
        zoom 0.7

    mayor_ansel_reed "The council will listen if we bring them the data. But they will also ask for guarantees. They want to see sanctuaries in the contracts."

    maya_kestrel "We need those guarantees. Not gestures—but enforceable language."
    hide maya_kestrel
    show dr_hana_sato at right:
        zoom 0.7

    dr_hana_sato "We can write monitoring metrics and trigger points into procurement. If certain cultural-use thresholds are compromised, funds can be withheld."
    hide ilias_navarro
    show seren_blake at center:
        zoom 0.7

    seren_blake "We can agree to hold releases of the next tranche to demonstrated compliance with those thresholds."
    hide mayor_ansel_reed
    show maya_kestrel at left:
        zoom 0.7

    maya_kestrel "So—co-governance with teeth?"

    seren_blake "Yes. Co-governance with teeth—if it means the project doesn't stall."
    hide dr_hana_sato
    show mayor_ansel_reed at right:
        zoom 0.7

    mayor_ansel_reed "It will be a hard vote. The board will push back against delays, but the pilot successes buy political capital."
    "Narration:"
    "The possible paths unfurl before you like the map on the lab table: legal guarantees, fast-tracked protections with buyouts, or insisting on a binding fund with retraining. Each promises a different shape of safety and loss."
    "The rising music in your chest isn't only about success; it is about the kind of success you want to steward."
    "Ilias Navarro squeezes your hand, sensing the weight you carry."
    hide seren_blake
    show ilias_navarro at center:
        zoom 0.7

    ilias_navarro "Whatever you choose, you'll have people at your back. We'll pitch in where we can."

    maya_kestrel "I know. That helps."
    "Narration:"
    "You fold your jacket about you and look at the town you've always loved—the boathouses, the market, the new pilings, the little stretch of ceremonial water you fought to keep. Hope feels practical now: it comes"
    "as contracts and volunteers, as protocols and plantings, as measurable decreases in flood frequency. It also comes as hard negotiations you must be willing to enter."
    # play music "music_placeholder"  # [Music: The motif swells, bright and patient — a rise that promises work and the possibility of keeping more than you feared you'd have to lose]
    "Narration:"
    "You take a breath and prepare to translate the hope into enforceable terms. The map will become policy; the policy will be tested in council and in courts and in the long, slow weather. You will have to choose how to enforce the community safeguards you carved into the plan."

    menu:
        "Hold Seren to the co-governance clauses — push for legal guarantees for cultural sanctuaries.":
            jump chapter9
        "Fast-track construction for immediate protection, accepting that some leases and boats will be bought out.":
            jump chapter15
        "Insist on a binding relocation fund and job retraining for displaced fishers.":
            jump chapter17
    return
