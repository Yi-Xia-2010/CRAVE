label chapter5:

    # [Scene: Saltgarden Research Lab | Late Afternoon]

    scene bg ch5_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The gentle, mechanical heartbeat of aerators; distant gulls; the shuffle of boots on damp concrete]
    # play music "music_placeholder"  # [Music: A rising, hopeful motif — woodwinds and soft strings building]
    "You press the palm of your hand to a tray and feel the cool, living slick of water and green threads. The trays hum with a promise: tiny blades anchored to mesh, each one a stitch"
    "against the sea. Your notebook is tucked into your jacket like an old compass; your thumb finds the coral pendant beneath your collar as if to steady a quickening pulse."
    "Ilias Navarro is beside you, sleeves rolled, sleeves streaked with mud and salt. His ocean-blue eyes crinkle when he smiles — the kind of smile that loosens the tightness in your chest. He moves with the"
    "kind of careful speed that comes from years on small boats; his hands know how to coax a fragile thing into holdfast."
    show ilias_navarro at left:
        zoom 0.7

    ilias_navarro "Look at the density on this frame. If we stagger transplant dates, we can minimize trauma from early storms and—"
    show maya_kestrel at right:
        zoom 0.7

    maya_kestrel "—and teach the volunteers the rhythm, not just the steps. Not everyone will keep to a calendar, but they'll keep to habits if it feels like tending a garden, not running a lab."

    ilias_navarro "You always think in systems and metaphors at once. I like it."

    maya_kestrel "Someone has to translate lab-speak into what Etta will actually do at dawn."
    "You show him a rough map on a scrap of waterproof paper — eelgrass frames, sheltered coves, rain-catch barrel placements. He traces the routes with a mud-sticky finger, adding a loop where juveniles congregate."
    hide ilias_navarro
    hide maya_kestrel

    scene bg ch5_4001e7_2 at full_bg
    show ilias_navarro at left:
        zoom 0.7

    ilias_navarro "If we standardize a simple field protocol — map, collect, transplant, monitor — other towns could replicate it. Low-tech, low-cost, and community-trained."
    show maya_kestrel at right:
        zoom 0.7

    maya_kestrel "Scalable without selling our soul."
    "Your chest loosens. The syllables of that thought taste like salt and insurance."
    # play sound "sfx_placeholder"  # [Sound: A pair of quick footfalls; the lab door opens. A figure in a damp lab coat steps inside.]
    hide ilias_navarro
    hide maya_kestrel

    scene bg ch5_4001e7_3 at full_bg
    # play music "music_placeholder"  # [Music: A quiet chord of validation underpins her entrance]
    show dr_hana_sato at left:
        zoom 0.7

    dr_hana_sato "You've got good survival rates so far. Holdfast counts are comparable to controlled trials I've seen.' (She studies your face, then the frames.) 'This isn't anecdotal. There's something repeatable here."
    "You let out a breath you didn't know you were holding. Validation from Hana feels like a solid stone placed beneath a shaky plank. It could hold the weight of Mayor Ansel's hesitations."
    show maya_kestrel at right:
        zoom 0.7

    maya_kestrel "We still need more replicates and longer monitoring, but the protocols are straightforward. Field training takes the biggest leap — it's about trust as much as technique."

    dr_hana_sato "Document everything. Variance, microhabitats, tidal windows. If you can show reproducible outcomes, Ansel will listen. And funders—' (she hesitates, and when she hesitates it means she knows names and powers you can't command) '—will pay attention for the right reasons."
    show ilias_navarro at center:
        zoom 0.7

    ilias_navarro "We were thinking of training modules — hands-on sheets, short videos, and a simple mapping app to collect coordinates and results."

    dr_hana_sato "Make it open-source. The science is stronger when it's shared."
    "You feel a small flare of triumph — shared, technical, righteous. It spreads outward through the lab like light through water."

    menu:
        "Thank Hana and keep the documentation tight; prioritize data quality":
            "You lean forward, voice steady. 'We’ll make the records rigorous. If the numbers stand, we won’t need persuasive speeches; the results will do the talking.' Hana's nod is sharp, almost maternal, and you file the decision away as method."
        "Push for immediate public training sessions to harness momentum":
            "You glance toward the open door where volunteers gather. 'Let's run a public session this weekend. Momentum is fragile; we should build it while hearts are in it.' Ilias brightens at the word 'weekend' and you can already smell the coffee and compost."

    # --- merge ---
    "..."
    hide dr_hana_sato
    hide maya_kestrel
    hide ilias_navarro

    scene bg ch5_4001e7_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low, steady murmur of instruction; the rhythmic slap of rope being coiled; a child's delighted shriek at a crab in shallow water]
    # play music "music_placeholder"  # [Music: The hopeful motif grows, adding a bright violin line]
    "Etta Muir ties a knot with practiced fingers, her face a map of wind and stories."
    show etta_muir at left:
        zoom 0.7

    etta_muir "When I was a girl, we used to reinforce the banks with reed and root. You young folk are remembering old ways with new hands.' (She looks at you, the weight of community memory in her eyes.) 'Don't forget—we do this to keep our nets and our songs. Not to make pretty maps for panels."
    show maya_kestrel at right:
        zoom 0.7

    maya_kestrel "We won't forget. This is for the nets and for the songs."
    "Ansel lingers near the boardwalk, hands in coat pockets, watching volunteers with an expression that softens when someone points out a sample. He moves toward you, the town's problems and hopes folded into his posture."
    show mayor_ansel_reed at center:
        zoom 0.7

    mayor_ansel_reed "Hana said it could sway me. If this is reproducible, we can argue for municipal support. But—' (he lifts a palm) '—we need to be sure it's durable enough to spare people real losses. The council will need numbers and a plan for storms while projects scale."

    maya_kestrel "We can pair immediate protective measures with your structural plans — temporary sandbags managed by volunteers tied to the living berms. It's not instant, but it's durable if people keep it tended."
    hide etta_muir
    show mayor_ansel_reed at left:
        zoom 0.7

    mayor_ansel_reed "Good. Come to council with lessons learned and a budget that doesn't read like wishful thinking."
    "His words land like a plank placed across a gap: solid, practical, needing labor on both sides."
    hide maya_kestrel
    hide mayor_ansel_reed
    hide mayor_ansel_reed

    scene bg ch5_4001e7_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The whisper of synthetic fabric; a polite, rehearsed tone]
    # play music "music_placeholder"  # [Music: A thin tension enters the motif — not dissonant, but a reminder of friction]

    "Emissary" "Seren Blake sends regards. She’s reviewed Hana's preliminary notes. Her office is prepared to match local funding if Hearthbend agrees to a zoning framework for priority channels — engineered conduits to protect the harbor's commercial routes."
    "Conversations sag mid-breath. The elder to your left pauses in her braiding. Some volunteers glance at the schematic as if it were a new tide."
    show etta_muir at left:
        zoom 0.7

    etta_muir "Priority channels? So you want to decide whose shore counts and whose doesn't."

    "Emissary" "It's targeted — to protect fishing lanes and key infrastructure. Faster implementation. Less debate."
    "Ilias Navarro's jaw tightens. He steps closer as if to lean on you, shoulder brushing your arm."
    show ilias_navarro at right:
        zoom 0.7

    ilias_navarro "Faster is not always better if it cuts the living parts out. Eelgrass relies on gentle slopes and shared stewardship, not locked channels."

    "Emissary" "We understand the value of living systems. This is a hybrid approach. Seren believes in decisive action that protects livelihoods swiftly."
    "You can feel the harmony you've been shaping vibrate with a new frequency. Voices ripple through the crowd — some nod at the idea of speed; others bristle at conditional strings."

    menu:
        "Call for a community forum now; let everyone speak before any deal.":
            "You step onto a crate and raise your voice to carry over the harbor. 'We decide our coast, together. If there's a proposal on the table, we discuss it here, with everyone on the dock.' Faces turn, and momentum shifts toward public deliberation."
        "Ask the emissary for specifics and a written proposal before public discussion.":
            "You fold your arms and ask, 'Put the conditions on paper. We can't debate hypotheticals.' The emissary's smile stays, but his fingers hover over the tablet as he synthesizes an outline."

    # --- merge ---
    "..."
    "Dr. Hana Sato moves to stand beside you, quiet and deliberate."
    show dr_hana_sato at center:
        zoom 0.7

    dr_hana_sato "Conditional funds can speed things, but they set the terms of what gets protected. If you take money tied to prioritized channels, you'll shape the coastline to those priorities.' (She looks directly at you.) 'You need to be clear what Hearthbend is willing to cede and what it will not."
    hide etta_muir
    show mayor_ansel_reed at left:
        zoom 0.7

    mayor_ansel_reed "We can't refuse resources that could prevent immediate damage. But we also can't be boxed into decisions that erase neighborhoods."
    hide ilias_navarro
    show etta_muir at right:
        zoom 0.7

    etta_muir "What good is survival if the songs drown?"
    "The question lodges in your throat. Your promise to protect everyone feels suddenly heavy — the ledger you carry shifts under new coin."
    "You walk between the tables, feeling the texture of reclaimed wood under your fingertips and the dampness of kelp on your boots. Volunteers watch you; their hands are callused and hopeful. The plan you sketched beneath the lab's hum suddenly seems both more necessary and more fragile."
    "Ilias Navarro places a hand on your shoulder — mud under his fingernails, warm and grounding."
    hide dr_hana_sato
    show ilias_navarro at center:
        zoom 0.7

    ilias_navarro "We could make the protocol shareable. Open-source it, host the documents, the mapping, the training videos. If people everywhere can deploy it without strings, the model scales without giving up control."
    hide mayor_ansel_reed
    show maya_kestrel at left:
        zoom 0.7

    maya_kestrel "Open-source… That means transparency, community ownership. It could undercut the leverage of conditional funders."

    ilias_navarro "It also invites collaboration. Other towns might refine it; academics could help validate it faster. We keep the knowledge public, and we ask for support — not for strings but for partnership."
    "You imagine the protocol online: clear, downloadable, a roadmap from seedling to berm. You see Hearthbend's name attached to an idea that ripples outward, not a stamp that seals choices closed."
    # play music "music_placeholder"  # [Music: The hopeful motif swells — brighter strings, a hint of choir — as the possibility blooms]
    hide etta_muir
    show dr_hana_sato at right:
        zoom 0.7

    dr_hana_sato "If you can show reproducible outcomes and open access, funders who care about impact might match you without conditions. You'd be shifting the power dynamic."
    hide ilias_navarro
    show mayor_ansel_reed at center:
        zoom 0.7

    mayor_ansel_reed "That could be a persuasive half-measure to stall any binding agreements while we test. It gives us leverage."
    "Etta gives you a look that is at once skeptical and curious — a fisherwoman's appraisal of a new net."
    hide maya_kestrel
    show etta_muir at left:
        zoom 0.7

    etta_muir "If you bind our hands to a plan that only saves some, it'll be our bones that break. But if you make the skill common, it's harder to take away."
    "Your guilt flares — a familiar, hot thing. You promised to protect everyone. Voices here are not yours to curate; the town will decide, and your role is to steward that process honestly."
    "You close your eyes for a breath. The scent of salt, kelp, and warm rope fills your lungs. There is noise all around — debate, laughter, the push of tide on pilings — and beneath it, the steady sound of many hands working."
    "The plan Ilias offers feels elegant and principled: community-mapping, open protocols, shared governance. For a moment a future unfurls where Hearthbend's small hands shape a regional movement, where knowledge is a tide that lifts more than a wall raises some."
    "You can feel the tide turning — not quiet, not without conflict, but moving in the direction you have argued for: from reactive fixes to shared, living resilience."
    hide dr_hana_sato
    hide mayor_ansel_reed
    hide etta_muir

    scene bg ch5_4001e7_6 at full_bg
    # play music "music_placeholder"  # [Music: A warm, sustaining chord—hope held steady]
    "You know a decision is imminent. Choices will be framed as urgency or prudence, survival or surrender. You can feel the town's breath caught between the offer of speed and the promise of autonomy."
    "You set your hand on the map again, fingers tracing the inked curves that mark possible futures."
    # [Scene: Community Rooftop Garden | Early Evening]

    scene bg ch5_4001e7_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The chatter of volunteers turned council; distant roar of surf]
    # play music "music_placeholder"  # [Music: Gentle strings and a single sustained piano note — anticipatory but warm]
    show mayor_ansel_reed at left:
        zoom 0.7

    mayor_ansel_reed "We have options. We can refuse conditional funding and go public with the protocol; accept partial, governed funds with clauses; or try to formalize a regional cooperative. Each choice changes who decides what stays."
    "You inhale, feeling hope and responsibility braided together. The community leans on your steadiness; Ilias Navarro looks to you with an earnestness that steadies your resolve."

    menu:
        "Refuse to accept any conditional corporate funds — publish the open-source protocol and rally volunteer labor.":
            jump chapter6
        "Accept partial funding tied to ‘priority zones’ but demand community governance clauses.":
            jump chapter13
        "Propose a regional cooperative with Seren and other towns — share governance in exchange for infrastructure support.":
            jump chapter16
    return
