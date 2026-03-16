label chapter11:

    # [Scene: City Hall - Planning Office | Morning — overcast, wind thinning after storm]

    scene bg ch9_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, a city siren cutting, murmurs swelling into determined conversation]
    # play music "music_placeholder"  # [Music: Fast, rising strings with sharp percussion — urgency balanced with a hopeful major key]
    "You step into the room and the air is already electric, charged by a thousand small decisions finally converging. The projector bathes everyone in a pool of shifting map colors: priority zones, risk contours, shaded patches"
    "labeled 'community buffer.' Your pulse echoes the projection's blink — a metronome counting down to signatures."
    show aiko_navarro at left:
        zoom 0.7

    aiko_navarro "Morning."
    "(You lower your voice though you know it will be heard; saying hello grounds you.)"
    "Mateo Ríos stands near the hologram, palms flat on the table as if holding the town's shape steady. His face is a map of restraint — eyes bright, jaw set — and when he looks at you a fraction of that steadiness visits your ribs like a hand of reassurance."
    show mateo_ros at right:
        zoom 0.7

    mateo_ros "They've posted the amendment clause. Council asked for it after the meeting last night."
    "You inhale. The clause looks like a small thing on paper and like a tethered lifeline in practice. It is, simultaneously, compromise and hard-won protection."
    hide aiko_navarro
    hide mateo_ros

    scene bg ch9_6b08b4_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Cameras clicking faintly in the corridor outside; whispered logistics]
    show councilor_nguyen at left:
        zoom 0.7

    councilor_nguyen "We need signatures to finalize the pilot funding. The election window shrank our margin.' (His voice is dry with urgency.) 'If we don't act today, everything reverts to the emergency procurement process."
    "Dr. Selene Park enters last, her coat slick with mist. The AR frames on her spectacles blink with data points you don't need to read to understand: efficiency, throughput, projected retention. Her smile is precise."
    show dr_selene_park at right:
        zoom 0.7

    dr_selene_park "I'm pleased we've reached a workable governance model. Institutional oversight will ensure scale, and local inputs will —' (she inclines her head toward you) '— refine implementation."
    "Tala is at the doorway, arms folded, eyes thin with unslept resolve. Old Man Rohan leans on a cane, the salt-dark lines on his face deeper than usual. Ivy is beside him, shoulders squared; she holds a small canvas satchel that smells faintly of lemon oil and tar."
    show tala_kumari at center:
        zoom 0.7

    tala_kumari "We'll be watching this closely. No token meetings. Full participation or we walk the streets and make sure the cameras remember who refuses to listen."
    hide councilor_nguyen
    show ivy_navarro at left:
        zoom 0.7

    ivy_navarro "We need relocation schedules that don't force folks out overnight. Jobs, not just handouts."
    "You feel the whole room tighten, then, inexplicably, loosen. This isn't a single victory. It is a compromise braided with conditions: measurable protections for the marsh in priority zones, mandated job training and placement, and a"
    "phased relocation plan with rent subsidies — but also an admission that some traditional craft sites and waterfront stalls will be submerged or repurposed to build engineered berms and scaffolded eelgrass beds."
    hide dr_selene_park
    hide tala_kumari
    hide ivy_navarro

    scene bg ch9_6b08b4_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The animation's soft whoosh mixes with a single, distant thunderclap]
    "Old Man Rohan's mouth presses into a thin line. He looks at the flickering image of a fishing cove reclassified as 'Habitats / Access Restricted.' His hands, when they tighten on the cane, look like nets folding into themselves."
    show old_man_rohan at left:
        zoom 0.7

    old_man_rohan "My nets won't fit in these new piers.' (He speaks as if naming a wound.) 'Don't tell me this will save my memories."
    "You step closer before you think. The room expects rhetoric; the room needs memory. Your voice is steadier than you feel."
    show aiko_navarro at right:
        zoom 0.7

    aiko_navarro "No one will forget how to use a net. We build training pods in the preserved coves. We'll fund co-ops so your techniques are paid work and teaching work. We will schedule community access windows into protected zones."
    "Rohan's eyes are unreadable for a beat, then a tiny, almost imperceptible nod — a fragile acceptance, not relief."

    menu:
        "Give Rohan your arm to steady him":
            "You slide your arm under his, feeling the familiar grain of his jacket. He huffs a laugh that smells of tar and pepper; it steadies something in you."
        "Place your palm over his knuckles, wordless":
            "Your palm warms his knuckles. He stares at your hand as if memorizing it, and the room's tension unhooks for a breath."

    # --- merge ---
    "Proceed to next scene"
    # [Scene: The Aquarium | Late Morning — the community meeting]
    hide old_man_rohan
    hide aiko_navarro

    scene bg ch9_6b08b4_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A rising chorus — applause, murmurs, a single child asking why the water got higher]
    # play music "music_placeholder"  # [Music: Layered percussion converging into a triumphant, driving motif]
    "You stand at the front as Councilor Nguyen calls the meeting to order. Mateo follows, pulling up the presentation you rehearsed when nights were long and the map in your head didn't look like this. Your"
    "speaking notes rest where you can reach — a few lines crumpled into the corner — but when you touch them you feel the locket at your throat, heavy and steady."
    show aiko_navarro at left:
        zoom 0.7

    aiko_navarro "We won't fix everything. We can't promise every fisherman the same shoreline they remember. But we can protect the marsh in ways that keep it breathing — for the fish, for the people, for the stories. This plan gives us a seat at every table: in monitoring, in hiring, in phasing relocations."
    "Tala stands, interrupting you not because she disagrees entirely but because she cannot let a soft edge stay where action must be harder."
    show tala_kumari at right:
        zoom 0.7

    tala_kumari "Words are good. Paper is better. But we need audits. Third-party observers. Consequences if Dr. Park's firm cuts corners for speed.' (Her gaze locks on Dr. Selene.) 'Will your company submit to citizen oversight, Dr. Park?"
    "Dr. Selene Park's smile doesn't change, but something in her eyes shifts: a measured recognition that performance now includes public scrutiny."
    show dr_selene_park at center:
        zoom 0.7

    dr_selene_park "Transparency is now part of the contract. We will accept an Elders Council seat on the oversight board, and an independent compliance auditor. Operational speed will be balanced with mandatory community review cycles."
    "A murmur circulates through the room — disbelief, relief, and a mounting cheer. The arousal spikes: phones are raised, hands clap, a chorus swelling into applause that shudders like a wave against the aquarium tiles."
    "Mateo catches your eye; the look between you is complicated — pride braided with the exhaustion of nights spent redrafting clauses. He steps forward, laying a hand on the holo-table to steady the model and the moment."
    hide aiko_navarro
    show mateo_ros at left:
        zoom 0.7

    mateo_ros "This isn't a win that anyone takes alone. It's a stitched solution. It saves habitat and creates jobs — but it asks for sacrifice. We're asking you to believe that the tradeoffs are worth it."
    "Your chest thumps. The room's energy is volcanic — very high, very focused. You feel the gravity of the moment bend toward decision, and for a second everything compresses: the past salt, the future possibility, the faces you love and owe."

    menu:
        "Speak briefly about your mother and why this matters":
            "You tell them a single, true sentence about the house you lost. The room listens as if inhale were permission; a few eyes wet."
        "Deflect to Mateo to keep the tone technical":
            "You gesture to Mateo. He takes the moment, his voice calm and precise, and the room leans into the pragmatic details."

    # --- merge ---
    "Proceed to next scene"
    # [Scene: Marsh — Midday | Tidal flats and new scaffold pilot zones]
    hide tala_kumari
    hide dr_selene_park
    hide mateo_ros

    scene bg ch9_6b08b4_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slap of a damp shovel, calls across the mud, a gull crying; distant construction noises]
    # play music "music_placeholder"  # [Music: A swelling brass line, triumphant and bittersweet]

    "You walk the pilot zone with Mateo, Tala, and a hired team. The air tastes briny and sharp. There are new things to love here: scaffolded mangrove starts held by woven fiber anchors; raised boardwalks with ramps; a small training shed where a notice reads" "Marisma Co-op: Apprentice Sign-ups Here."
    "Ivy kneels by a cradle of replanted marsh grass, fingers deft with the care you've seen her give to market produce. She looks up when you approach, and the set of her jaw is softer, proud in a practical way."
    show ivy_navarro at left:
        zoom 0.7

    ivy_navarro "They're hiring through the co-op. We'll get a rotation for the fishers, and the training pays. It won't be the same, but it means rent checks that don't depend on yesterday's tide."
    "Old Man Rohan stands at the edge of an old cove now fenced for restoration. He watches a small team raise a modest pier that allows controlled access. His mouth tugs."
    show old_man_rohan at right:
        zoom 0.7

    old_man_rohan "They take my stall. My place by the pier. But maybe — maybe they'll pay the men who learn in that training."
    "You reach for him and find your hand in his, palm against callus. There is grief in that palm — the kind that is not rhetoric but fact — and there is also a spark of something else: hope folded into new labor."
    hide ivy_navarro
    hide old_man_rohan

    scene bg ch9_6b08b4_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A sudden shout — cheers from a small crowd who watch as a test berm keeps a modest wave at bay; applause breaks like surf]
    # [Scene: City Hall - Planning Office | Afternoon — contract signing]

    scene bg ch9_6b08b4_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The room holds breath; a storm rumble dissipates outside; microphones take in the hush]
    # play music "music_placeholder"  # [Music: Rapid strings, then a single, resonant chord as the first pen is lifted]
    "Councilor Nguyen raps a knuckle to call silence. He nods to Dr. Selene, to you, to Mateo — a chain of acknowledgment that feels like a relay passing a torch."
    show councilor_nguyen at left:
        zoom 0.7

    councilor_nguyen "Today we sign a different kind of contract. Not only one that protects infrastructure, but one that protects people, memory, and watchfulness."
    "Dr. Selene Park moves with surgical certainty to the corner clause — the one that binds corporate action to community oversight and mandates reparative hiring. The cameras pounce on her still face. For a breath, she looks almost human: a person boxed by expectation."
    show dr_selene_park at right:
        zoom 0.7

    dr_selene_park "We will deploy at scale, and we will open our models to the oversight board. We will fund the apprenticeship program."
    "Mateo takes a breath, then signs with a sure stroke. His pen leaves a small smear; he looks up at you, an unreadable, tender thing in his gaze. You respond with a small, private smile that says more than any public statement — gratitude, fatigue, an unnamed closeness."
    show aiko_navarro at center:
        zoom 0.7

    aiko_navarro "On behalf of the community steering committee, I sign."
    "You—and with you, the marsh, the people who taught you nets and tide charts and how to coax sedge from muck—place your pen to the paper. The ink sinks like a tide into grain; the room exhales as one."
    # play sound "sfx_placeholder"  # [Sound: A flood of camera shutters, a spontaneous cheer, some sobs; the applause is volcanic]
    # play music "music_placeholder"  # [Music: The strings snap into a major surge — victorious and aching]
    "The signatures complete, Councilor Nguyen stamps the final clause. The sound is like a seal falling into place. People crowd forward: hands outstretched to touch the paper, to feel the promise as if it were a talisman."
    "Old Man Rohan approaches slowly, then stops. He looks at the document, then at the sea beyond the hall's window, then at you. You can see the math in his face: what stays, what leaves."
    hide councilor_nguyen
    show old_man_rohan at left:
        zoom 0.7

    old_man_rohan "Will they remember to let us fish on the good days?' (Tremor.) 'Will my grandson learn the same knots?"
    "You squeeze his hand. You don't have the certainty he asks for, only the stitched guarantees now on paper — enforceable, audited, imperfect."
    "You look around at the faces: Tala's fierce, open-eyed satisfaction; Ivy's pragmatic smile; Mateo, who lets you read the fatigue in him and counters it with an anchored, soft expression. Dr. Selene's lips are a thin"
    "line; she inclines her head toward the room in a private acknowledgment that her company will be held to account."

    menu:
        "Take a breath and make a short public remark: 'This is not the end'":
            "You step forward to the mic. The words come blunt and true: 'This is not the end. It's the beginning of being watchful.' People clap. It steadies the room into purposeful motion."
        "Let Mateo make the closing statement to emphasize technical oversight":
            "You let Mateo go. He summarizes the enforcement mechanisms crisply; the room nods in practical accord, and the cameras narrow on the clause specifics."

    # --- merge ---
    "Proceed to next scene"
    "Outside, the first tentative sunlight breaks through ragged clouds and hits the bay in a silver streak. Across town, the market stalls will be rearranged; some roofs will be lifted higher; some families will begin the"
    "slow work of moving. These are hard things, and they are also necessary ones. You feel them both — the sting and the relief — at full volume."
    # [Scene: Cliffside Promenade and Old Sea Wall | Dusk — the ceremonial closure]
    hide dr_selene_park
    hide aiko_navarro
    hide old_man_rohan

    scene bg ch9_6b08b4_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Waves hissing against the repaired sections; laughter, a few whispered laments; a distant radio playing an old sea shanty]
    # play music "music_placeholder"  # [Music: A swelling chorus that threads triumph with a gentle minor undertone]

    "You and Mateo walk a pace apart and together. There is lightness in his step; there is a tired, good smile that finally arrives. At the top of the promenade the old sea wall stands less battered — concrete patched, living plantings tucked into cracks. A small plaque reads" "In memory of those who taught us to read the tide."
    "Old Man Rohan stands by the wall, watching the waves. He raises a hand in an old fisher's salute, slow and deliberate. You return it, clumsy with feeling."
    "Ivy slips her hand into yours and holds on with a practical grip that says: we'll work, we'll grieve, we'll rebuild."
    "Tala leans close and whispers — a half-smile, fierce and warm — 'We made them listen. We keep them honest.'"
    "Dr. Selene Park approaches at a measured pace. When she speaks, her voice is quieter, less public-performance and more human."
    show dr_selene_park at left:
        zoom 0.7

    dr_selene_park "Your oversight will improve outcomes. It will also slow deployment. That is... acceptable."
    "You nod. The company that once promised only speed has accepted a new variable: memory. That concession tastes of victory."
    "Mateo pauses, fingers finding yours. There is a small, steady pressure — intimate but not theatrical — a pact that whatever this victory cost, it also knit you into something ongoing: partnership, stewardship, the daily practice of keeping promises."
    show mateo_ros at right:
        zoom 0.7

    mateo_ros "This changes everything and nothing at once.' (He exhales.) 'We have more to do."
    "You let the sentence sit between you — catastrophic and hopeful at the same time. The arousal reaches its last, hottest peak: the signing, the cheering, the vows to watch, the knowledge of those who will"
    "leave, and the certainty that work begins anew tomorrow with boots in mud and lists in hand."
    hide dr_selene_park
    hide mateo_ros

    scene bg ch9_6b08b4_9 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The ocean, steady and enduring; the murmur of plans forming like a tide pooling in the harbor]
    # play music "music_placeholder"  # [Music: Final chord — major, sustained, a warmth that holds grief within it rather than erasing it]
    "You close your eyes for a moment and map the day onto your skin: the bracing cold of the morning, the warmth of the signatures, the salt in Rohan's laugh. Pride and loss sit together, sibling emotions sharing the same bench."
    show aiko_navarro at left:
        zoom 0.7

    aiko_navarro "We did it."
    "Mateo's hand tightens around yours. He doesn't promise anything grand; he simply looks at you with an expression that holds all the complicated things — admiration, care, weariness, possibility."
    show mateo_ros at right:
        zoom 0.7

    mateo_ros "We did. And we'll keep doing it."
    "You watch the bay, breathing in the tang of sea and the less obvious scent of fresh paint, of new wood, of seeds planted. The marsh will not be wholly saved nor wholly lost. It will"
    "be altered and tended; some livelihoods will shift; some memories will ache in vacancies where stalls once stood. But there are apprenticeships signed, co-ops funded, oversight clauses inked. Dr. Selene's firm will not be the single"
    "voice in the room anymore."
    hide aiko_navarro
    hide mateo_ros

    scene bg ch9_6b08b4_10 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft singing drifting from a nearby gathering, an old shanty adapted with new words about holding the tide]
    # play music "music_placeholder"  # [Music: A gentle, lingering motif — hopeful, melancholic, resolved]
    "You think of the people who stayed and those who left, of houses whose thresholds are now empty, of the hands that will teach new nets and new ways to read the water. You think of"
    "the locket at your throat and the map inside it — a childhood shoreline changed but remembered. You think of the work ahead: audits, community meetings, nights in mud and days in negotiation."
    "You do not romanticize the future into painless certainty. Instead, you accept a different gift: procedural hope — a design that requires stewardship, attention, and the grit of belonging. That acceptance is its own kind of"
    "triumph. It tastes like salt and like something sweeter: the small certainty that the next morning you will stand in the mud with a shovel and not be alone."

    scene bg ch9_6b08b4_11 at full_bg
    # play music "music_placeholder"  # [Music: Soft denouement — a single piano note, then silence]

    scene bg ch9_6b08b4_12 at full_bg
    "THE END"
    # [GAME END]
    return
