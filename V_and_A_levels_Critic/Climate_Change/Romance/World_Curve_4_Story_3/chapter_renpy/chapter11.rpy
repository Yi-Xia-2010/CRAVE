label chapter11:

    # [Scene: Glasshouse Research Lab | Late Afternoon]

    scene bg ch11_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Taut strings under a quickening percussion]
    # play sound "sfx_placeholder"  # [Sound: The distant caw of a gull, the low vibration of a phone buzzing on a metal bench]
    "You are still wearing the smell of the harbor — salt and diesel and the faint, sweet rot of seaweed — but here the air tastes different: a metallic tang from printers, the sterile chill of"
    "air-con, coffee gone cold in a thermos. The contracts look official in a way your field notes never will: embossed logos, thin lines of small-print clauses, numbered appendices. They hum with authority and consequence."
    "You lay a single palm on the top packet and feel the vibration from Samir's tablet where he sits across the bench, fingers jittering. He doesn't look up when he slides the device toward you; his face is pale under the lab's blue glow."
    show samir_reyes at left:
        zoom 0.7

    samir_reyes "You have to see this. They were meeting at the Harborview Club last night. Look."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Play it."
    hide samir_reyes
    hide maya_reyes

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Muffled laughter, the clink of glass; a voice you recognize as a developer's murmurs: "Zoning corridor...priority parcels...we'll tuck it under the infrastructure clause."]
    "Your stomach flips hot. Proof is slippery — a timestamp, a photo, a cigarette burned down in a glass ashtray — but the shape of it is clear enough. You imagine the seal on a permit,"
    "the quiet of a signature being slid across an invisible line, and the rooms that will be lost if those parcels turn commercial."
    "You feel the old compass locket against your throat, small and blunt. It used to anchor you. Now it feels like an accusation."

    menu:
        "Ask Samir to pull everything into a secure folder":
            "You direct Samir to catalogue every clip, every image — chain of custody, metadata, a slow armor. He nods, fingers moving faster; security feels possible in paperwork."
        "Call Elias and tell him what you saw":
            "Your thumb hovers over his contact; imagining his face — furious, pleading — is a current you can't ignore. You press call and brace for the tide."

    # --- merge ---
    "Continue to next scene."
    # [Scene: Boardwalk | Early Evening]

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slap of waves, voices from a distance — the town's life continuing — and your phone ringing in your pocket like a small alarm]
    # play music "music_placeholder"  # [Music: A high, urgent violin]
    "The call connects while you're two steps from him; you can see the way his shoulders have a new tightness, as if the sea shaved weight off everything it touched. He doesn't waste breath."
    "Elias Hart: (breathless) 'Maya — you saw it?'"
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "Samir sent footage. It looks like—"
    "Elias Hart: (cutting in) 'They met with Maren Voss's aides. They're carving up the parcels overnight. They offered local co-ops subcontractor slots — token things — and promised immediate work if we sign.'"

    maya_reyes "Immediate work isn't nothing."
    show elias_hart at right:
        zoom 0.7

    elias_hart "It's not nothing — that's the rub. It's everything, Maya. Jobs matter. But those parcels? They aren't for the community. They're for out-of-town interests. They'll hollow this place out."
    "His voice lifts into a raw edge. For a beat the boardwalk seems to amplify every syllable, wind carrying it away."

    maya_reyes "There are also clauses — development rights, exclusive vendor lists, zoning vetoes. They're not just funding projects; they're buying leverage."
    "Elias Hart: (bitter laugh) 'Of course they are. Of course. I thought you felt it too — the way the platform went up like a miracle. But if you hand them the ledger, they'll write the rest of the town out.'"
    "He moves closer, lowering his voice when he sees you watching him, as if there's a camera in the gulls."

    elias_hart "Maya — do not let them buy Harborwell."

    maya_reyes "What do you want me to do, Elias? Say no and let the crews go home? Tell the families who lined up for day work that I chose principle over their rent?"
    "He is quiet long enough for the tide to answer him."

    elias_hart "I want you to remember who this is for. Not donors. Not glossy reports. People."
    "The call ends with a static click. You are left with his words ringing like a bell you can't un-hang."
    # [Scene: Developer Meeting Room (Overheard) | Same Evening]
    hide maya_reyes
    hide elias_hart

    scene bg ch11_e67f19_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Voices, one clipped and corporate; the low, steady hum of an air filtration system]
    # play music "music_placeholder"  # [Music: Percussive hits, breathless tempo]
    "You aren't on the guest list, but you have ears everywhere. A city aide steps out of the meeting briefly; you catch a hush of conferral with a developer who slides a thin manila folder along the table."
    "Developer: (smooth) 'The philanthropic board understands the need for scale. Our plan integrates commercial zones—revenue anchors. We'll subcontract the co-ops for local labor; it's PR-neutral, actually.'"

    "Municipal Aide" "Politics is complicated. Mayor Delgado wants jobs. This bridges needs."
    "You press your forehead to the cold glass, breath fogging. Bridges can be tolls."
    # [Scene: Rooftop Garden & Salt Marsh Restoration Site | Night — Wind Picking Up]

    scene bg ch11_e67f19_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The high, restless whisper of wind through grasses; the distant roll of a refrigerated truck; a phone buzzing again on the bench]
    # play music "music_placeholder"  # [Music: A relentless, rising ostinato—drums and low strings]
    "You have brought the contract packets here because the rooftop feels like a truth-teller: soil, roots, the black, honest mud. You spread the papers across a bench and read until the ink tastes like a dare. Each clause is a hinge. Each amendment a door that closes on someone else."
    "Iris arrives, boots soft with mud. Her face is a map of weather and stubborn kindness."
    show iris_tanaka at left:
        zoom 0.7

    iris_tanaka "Permits signed in the night,' she says, not a question. 'A broker pulled strings. They used a procedural bypass — emergency designation."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Emergency for whom?"
    "Iris: (landing on the bench) 'Not for the fishermen. Not for the elders on Marsh Lane. For developers making sure their strip stays dry.'"
    "She taps a page with a gloved finger and the lamplight flickers. Her gloves still smell faintly of fish oil and rope; it's a smell that keeps you tethered to what is fed by the sea."

    iris_tanaka "They'll give low-paid construction contracts to local crews so it looks like local benefit. But the larger parcels? Gone. Market-rate housing, restaurants for tourists, a corporate hub. Then they pull the strings on zoning and—boom. We're priced out or boxed out."

    maya_reyes "And the co-ops?"

    iris_tanaka "Offered crumbs, Maya. You're not wrong to think about jobs. But crumbs don't feed forever."
    "Samir: (from the edge of the garden) 'There's more. I tracked an email chain — 'preferred vendors,' 'exclusivity windows.' If we sign, we can't bring in other partners. They lock procurement. They could blackball any community initiative that doesn't fit their plan.'"
    "You feel the clock tighten around your neck like a noose. The philanthropic representative called earlier, sweet and insistent; they want a signature by dawn to 'solidify implementation schedules.' The timeline that once felt like momentum now beats like a drumline driving you toward a precipice."

    menu:
        "Call the philanthropic representative and demand renegotiation":
            "You pick up the phone, your voice steady but hard. The rep answers with practiced warmth; you push for clause changes and payment schedule transparency. They stall — 'not tonight' — their cadence a polite refusal. You hang up with a throat full of sand."
        "Set up an emergency meeting with co-op leaders and Iris":
            "You send rapid messages: meet now, rooftop. Within ten minutes people gather in mud-stained boots. There's a flurry of plans and arguments — urgency makes ideas jagged but alive."

    # --- merge ---
    "Continue to next scene."
    "Your chest is a drum; your thoughts trip over each other — the people who will get a day's wage if the machines keep moving, the families who will lose yards to slick terraces that face"
    "the water like blind eyes, the promise of a prototype that could be replicated — but in whose image?"

    "You read the liability clause again" "By accepting funds, the Recipient consents to consultation with Funding Partners on any future zoning adjacencies that materially affect the funded parcels..."
    "You imagine a map with your name in the margin. You imagine the ledger stacked and stamped. You imagine Maren Voss’s polished face reading the lines and making hard choices you will not be able to explain away."
    # [Scene: Rooftop Garden | Night — Stormclouds Edging In]
    hide iris_tanaka
    hide maya_reyes

    scene bg ch11_e67f19_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind, a far thunder; the phone alarm of an incoming message; murmurs around you]
    # play music "music_placeholder"  # [Music: Intensifying strings, a sharp, urgent motif that won't let go]
    "Elias Hart returns, his jacket smelling of brine and smoke. He finds you holding the top contract like a sacrament and does not flinch."
    show elias_hart at left:
        zoom 0.7

    elias_hart "They gave my crew a small bid — two weeks of work and a promise of more if we go along. They called it 'inclusive procurement.'"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Inclusive for them, maybe."
    "Elias Hart: (voice tight) 'If you sign, they'll keep the token work but control who gets the rest. Your models — the mapping, the marsh restoration — could be turned into a boutique eco-tourism package. They'll sell our resilience as a lifestyle product.'"
    "He steps closer, anger and pleading wrestling in his features."

    elias_hart "You're one of few who can read these things and still see the people. Don't hand them the rulebook."

    maya_reyes "Or I say no, and the crews, the people who already lined up for work, lose out. I'm supposed to balance lives and futures, Elias. How am I supposed to do that without breaking both?"
    "He grabs your forearm, hard enough to hurt."

    elias_hart "You can do what you always do: find a way through that doesn't sell out the town. Or—"
    "His throat closes. He doesn't finish. He doesn't need to."
    "You are a spit of wood in a storm between a promissory note and an anchor. Your moral calculus rattles like loose screws."
    # [Internal Monologue — Rapid, Knife-Edged]
    "You tally faces. Samir's steady camera eye. Iris's lined hands. The children who chased kites on the boardwalk last summer. The people who will never be able to afford a reprieve if the coastline becomes a"
    "showcase for outsiders. You also measure immediate needs: rent due, scaffolding paid for, winter approaching."
    "You picture the donors' glossy brochures — Harborwell, 'a replicable prototype' — with bullet points and smiling stock photos. You picture a handful of people in a conference room deciding which neighborhoods matter."
    "Your pulse climbs until it feels like a second heartbeat."
    # play music "music_placeholder"  # [Music: Swells to a near-climax—strings and brass; the sound design tightens into a compelling insistence]
    "You fold the contract once. Twice. The creases are sharp as final decisions."
    "You could sign. You could refuse. You could force the truth out."
    "You look up at Elias Hart. He watches you like someone waiting for a lighthouse to move."
    "You look at Iris. Her expression is a rope of patience and warning."
    "You look at Samir. His jaw is set; he is already cataloguing consequences in his head."
    "The rooftop's lamps hum. The marsh waits."
    # [Scene: Rooftop Garden | Night — Decision Point]
    hide elias_hart
    hide maya_reyes

    scene bg ch11_e67f19_7 at full_bg
    # play music "music_placeholder"  # [Music: A held chord that breaks into silence]

    menu:
        "Sign the contract—secure immediate projects and jobs.":
            jump chapter12
        "Refuse the contract—fight to re-negotiate terms even if we lose funding.":
            jump chapter12
        "Leak the documents to the press to force transparency.":
            jump chapter15
    return
