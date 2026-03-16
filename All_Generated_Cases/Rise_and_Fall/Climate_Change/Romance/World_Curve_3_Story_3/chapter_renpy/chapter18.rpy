label chapter18:

    # [Scene: Municipal Hall | Morning]

    scene bg ch15_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low murmur of voices; a kettle clicking off; rain ticking against the annex windows]
    # play music "music_placeholder"  # [Music: Warm strings; steady, rising undercurrent]
    "You breathe in the damp of the morning and the salt that always seems to follow you into rooms that should be dry. The choice you made weeks ago — to step back and hand agency"
    "to the people who would live with the consequences — has led you here: not to abdication but to negotiation. The municipal hall smells of printer toner, old coffee, and the faint, impossible sweetness of Rita's"
    "lemon cookies at the corner of the table."
    "Rita folds a legal clause like it is a seed packet, tilting it toward you. Her expression is all motion: hands, bright eyes, a pace of someone who builds consensus the way others spin rope. Mayor"
    "Tomas watches from the head of the table, fingers steepled, the gold signet ring catching the light like a small lighthouse. Dr. Ayla Voss stands near the projection, tablet humming with regional models — precise, cool"
    "lines on a warm morning."
    "You slide the green scarf from your bag and keep it folded in your palm like a ritual. It is the small thing that grounds you when the language gets abstract and the stakes feel like raw tides."
    show mayor_tomas_nkem at left:
        zoom 0.7

    mayor_tomas_nkem "This charter has teeth now, Maya—binding oversight clauses, reporting metrics. It keeps the grant intact."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "It also has to keep neighbors in the room. The oversight Dr. Ayla Voss proposes can feel like a leash if it's not paired with clear community governance."
    show dr_ayla_voss at center:
        zoom 0.7

    dr_ayla_voss "Oversight isn't a leash. It's accountability. The regional engineers need guarantees that the modular systems will meet load tolerances. Otherwise funding will be withdrawn."
    hide mayor_tomas_nkem
    show rita_ortega at left:
        zoom 0.7

    rita_ortega "And guarantees aren't only about numbers. They're about who waters the nursery at dawn, who knows where the old nets can be repurposed without stripping livelihoods. We need language that recognizes practice as evidence."
    "Dr. Ayla Voss's jaw tightens. For a beat she seems to measure layers of history on Rita — something distant, almost like an external variable. Then she unfolds her hands, small concession."

    dr_ayla_voss "We can codify stewardship practices as part of maintenance schedules. We can make community inspections a formal part of the compliance cycle."
    "You let the sentence sit like a plank across a gap. The tension is not between good and bad actors; it's between different currencies of trust. You can feel the hum of politics — Tomas's survival,"
    "Dr. Ayla Voss's reputation, Rita's insistence on dignity — and beneath it, the town's old rhythms waiting to be honored."
    hide maya_reyes
    hide dr_ayla_voss
    hide rita_ortega

    scene bg ch15_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The scrape of a pen; the kettle sighing]
    show rita_ortega at left:
        zoom 0.7

    rita_ortega "Make the maintenance logs public and simple. Use platforms that work here — paper rosters pinned at the gazebo will do as much as an app, sometimes more."
    show mayor_tomas_nkem at right:
        zoom 0.7

    mayor_tomas_nkem "We can attach a clause for public rosters. But we keep the engineering sign-offs as non-negotiable."
    show maya_reyes at center:
        zoom 0.7

    maya_reyes "That's fair. We need both: the rigor Dr. Ayla Voss demands and the co-ownership Rita builds. Can we phrase it so inspections are co-led? Regional engineers and community stewards sign together."
    "Dr. Ayla Voss's lips narrow, then give. She taps the tablet, pulling a line of text into view."
    hide rita_ortega
    show dr_ayla_voss at left:
        zoom 0.7

    dr_ayla_voss "Co-led inspections. Conditional release of funds based on agreed milestones. We'll schedule a quarterly review with the council, but minutes are public."
    "Rita beams like someone who's had salt potato stew on a cold night and found an extra spoon."
    hide mayor_tomas_nkem
    show rita_ortega at right:
        zoom 0.7

    rita_ortega "And let's include a clause for heritage measures: capturing fishing knowledge, seed exchange protocols, and a fund for families who choose to relocate."
    hide maya_reyes
    show mayor_tomas_nkem at center:
        zoom 0.7

    mayor_tomas_nkem "Relocation support will be tough politically."
    hide dr_ayla_voss
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "But necessary. If we don't make moving dignified and supported, we'll force people into shame and risk later failure."
    "The conversation loops and doubles back, respectful friction turning into constructive heat. You add phrasing, soften a sentence here, tighten a liability clause there. Every change feels like a small dyke, an adjustment to a shore that will keep water out and life in."

    menu:
        "Draft the 'co-led inspection' clause with explicit community signatures required":
            "You pen the clause and slide the page toward Rita. She taps the spot with her finger as if blessing it; Tomas nods and Ayla raises an eyebrow before quietly approving. The room exhales."
        "Propose a phased approach: start with voluntary co-inspections, then formalize after three cycles":
            "You suggest a phased timeline. Ayla frowns at the softer start but admits it might help with uptake. Rita marks the idea as 'bridge strategy' and the draft grows wider, more inclusive."

    # --- merge ---
    "You choose the wording that feels like a bridge rather than a wall. It matters less which exact phrase you choose than the momentum you cultivate: shared responsibility under a binding framework. That is the compromise — not a loss, but a deliberate reweaving."
    # [Scene: Construction Sites & Mangrove Nursery | Afternoon]
    hide rita_ortega
    hide mayor_tomas_nkem
    hide maya_reyes

    scene bg ch15_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Hammers, laughter, the distant slap of waves; the scent of wet wood and diesel]
    # play music "music_placeholder"  # [Music: Upbeat folk strings; the rhythm of hands at work]
    "The town is a choreography of repair. You walk the construction line where Elias Jun now teaches a cooperative — hands-on sessions turning old boats into floating barriers, nets woven into mats that break wave energy."
    "Arlo works at your side, earnest and clumsy, eyes on Elias Jun the way apprentices watch craftsmen in myths. Children dart between pallets like minnows."
    show elias_jun at left:
        zoom 0.7

    elias_jun "You want to put a keel here, or are we mounting the buoyancy modules instead? Your call, partner."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Let's do buoyancy. It's lighter to deploy and the community teams can lift the sections together."

    elias_jun "I could say I told you so when the tide surprises us, but I'll let your science take the honor."
    "You both laugh, and it's warm and a little shy, the kind of laughter that stitches small seams back into a relationship. You rebuild trust with shared work: early breakfasts of stale bread and soft-boiled eggs, evenings sanding splinters, the silence of your hands speaking what your mouths can't."

    menu:
        "Spend the afternoon teaching rivet work with Elias":
            "You take a rivet gun, shoulder close to Elias as he shows you the angle. Your hands find their rhythm; the proximity is salt-warm and familiar."
        "Walk the mangrove nursery and catalog sapling species with Rita":
            "You trail Rita between trays, smelling peat and mud. She talks about species lines like names in a family album; you write notes, and it feels like planting roots in paper."

    # --- merge ---
    "You split your afternoon between both: a rivet here, a note there. The work is honest and immediate; each screw tightened is a promise. The cooperative hums with purpose. Mothers watch from a distance; old fishers who once scoffed at 'young projects' stand by to learn."

    elias_jun "We make something lasting, not just for headlines. For dinners — for the kids who will know how to fix a hull."

    maya_reyes "And for the kids who might not be able to fish the way you and I grew up doing. That's the hard part."

    elias_jun "Then we teach them both. Fix a barrier, mend a net. Give them tools, not ultimatums."
    "You feel the caution melt into a plan: skills, craft, livelihoods preserved within new structures. Hope is not a single triumphant song; it's the layered chorus of small, repeated actions."
    # [Scene: Municipal Hall — Charter Signing | Late Afternoon]
    hide elias_jun
    hide maya_reyes

    scene bg ch15_3be532_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft applause; shutters of cameras; gulls arguing overhead]
    # play music "music_placeholder"  # [Music: Tender choir; swelling to a steady hopeful cadence]
    "The signing is simple and solemn. Rita stands at the mic and says a name for every transferred right. Tomas reads the municipal assurances. Dr. Ayla Voss signs with a calm hand that betrays an ease"
    "you hadn't expected: she has learned to let local knowledge shape a model, not simply be an input."
    show rita_ortega at left:
        zoom 0.7

    rita_ortega "This charter is not our last word — it's our first common language. We will steward mangroves, tend the nursery, maintain the modular barriers, and support families who choose to move."
    show mayor_tomas_nkem at right:
        zoom 0.7

    mayor_tomas_nkem "And by my signature, the town will secure regional funding and ensure relocation support for families who need it."
    show dr_ayla_voss at center:
        zoom 0.7

    dr_ayla_voss "And I commit to technical oversight that respects community practice. Engineers will be present at co-inspections; models will be explained in public meetings."
    "Elias Jun stands at your side and signs last. His handwriting is blocky and honest. When he hands the pen back, his fingers brush yours — brief, a quiet repair."
    "You look out at the faces around the canopy: old men with palms like oyster shells, teenagers in hoodies with paint on their knuckles, a woman holding a toddler who watches the signatures like a game."
    "The town is not healed of its losses, but it has reorganized itself with intention."
    hide rita_ortega
    hide mayor_tomas_nkem
    hide dr_ayla_voss

    scene bg ch15_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of conversation that smells like lemon cookies and spilled tea]
    # [Scene: Rooftop Watch at Dusk | Evening]

    scene bg ch15_3be532_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind through potted herbs; a distant laugh; the steady tick of your tide-watch]
    # play music "music_placeholder"  # [Music: Solo guitar; soft, hopeful]
    "You and Elias Jun ascend to your rooftop garden later, a private harbor above the public work. The rooftop holds the small domestic proofs of the life you've reclaimed: a battered telescope, a line of drying"
    "nets repurposed as laundry, a tin of screws you both always forget to return. The green scarf — by then a small, deliberate emblem woven into the community's banner — is looped around the railing, fluttering"
    "like a promise."
    show elias_jun at left:
        zoom 0.7

    elias_jun "We did it. Not alone, not perfectly. But together."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "We did. And we'll keep doing it. There will be storms we didn't anticipate. There will be new rules to write. But today feels like a foothold."

    elias_jun "Mornings with you and a thermos of bad coffee. Nights sanding until the moon looks like a coin. I'll take that."
    "You laugh, and the sound slides across the horizon. The rooftop is small and steady, a safe geography where words mean what they say. You think about Dr. Ayla Voss standing with Rita at the signing,"
    "Tomas's hesitant relief, the way neighbors traded seeds afterward like currency of care. You think of families who moved with dignity, their new houses painted with the same colors as the old porches. You think of"
    "those who stayed and how their adjustments were honored."
    "A man across the harbor flashes lights — the signal your group used for shifts — and you check the tide-watch automatically, then relax. Routine returns as a comfort rather than an obligation."

    maya_reyes "You taught Arlo how to splice a line like my grandmother taught me to braid rope."

    elias_jun "He taught me to slow down, and to listen before I fix. Not a bad trade."
    "There is silence that isn't empty but full of accumulated work. You look at Elias Jun: the salt in his hair, the sawdust still clinging in a way that makes you want to brush it off. He looks at you like someone measuring distance and deciding it's worth the step."
    "You take the scarf from the railing and knot it into the banner again with careful fingers. The fabric has gathered small stains — oil, mud, a smear of rust — each a memory of labor."
    "You tie the knot and feel the weight of it as a language: I am here. We are here."
    # [Music swells gently; the strings lift]
    "You let the moment settle into you, cautious but rising — a hope that has been earned through meetings, nights of revision, and the slow architecture of trust. Neighbors below call out the time of the evening watch. Laughter pools like light."
    "You know this is not an ending in the sense of completion; this is an ending that feels like arrival. The charter is signed. The cooperative hums. Funding is steady enough to plan and imperfect enough to demand vigilance. Love has been rebuilt as a pattern of small, reciprocal acts."
    "You close your hand around Elias Jun's, and the tide-watch ticks against your wrist like a steady, human pulse."
    hide elias_jun
    hide maya_reyes

    scene bg ch15_3be532_7 at full_bg
    # play music "music_placeholder"  # [Music: Full orchestra — warm, resolved]
    "You think of the possible futures you once feared, and how this one leans toward care. The banner with your green scarf flutters; somewhere a child hides seeds in a pocket and later swaps them at"
    "the nursery. Rita plans a festival to celebrate the new apprenticeship program. Arlo signs up the first cohort of trainees."
    "You draw a slow breath that tastes like salt and lemon cookies and the hard, steady joy of a task that matters. You let yourself feel it fully: cautious, communal, real."

    scene bg ch15_3be532_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    scene bg ch15_3be532_9 at full_bg
    "THE END"
    # [GAME END]
    return
