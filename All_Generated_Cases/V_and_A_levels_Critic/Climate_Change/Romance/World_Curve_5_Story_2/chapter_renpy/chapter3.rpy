label chapter3:

    # [Scene: City Hall - Planning Office | Late Afternoon]

    scene bg ch3_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Quiet HVAC hum, soft murmur of pre-meeting voices, distant tide like a remembered rhythm]
    # play music "music_placeholder"  # [Music: Warm, steady BGM — hopeful, measured]
    "You remember the Aquarium's kettle and the small click of your notebook cover like a talisman. The list of talking points is still folded in your palm, the edges softened by thumbprints. From Chapter 2: you"
    "left with a plan and a readiness that felt like a tide finally turning. That readiness is the weight you carry through the City Hall doors."

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The scrape of a chair as Mateo stands to let you pass]
    # play music "music_placeholder"  # [Music: A single chord swells and settles]
    show mateo_ros at left:
        zoom 0.7

    mateo_ros "You look like you could use the world's calmest breath. Want me to cue a slide if you lose your place?"
    show aiko_navarro at right:
        zoom 0.7

    aiko_navarro "Only if you flash a 'get back in there' sign. No theatrics."

    mateo_ros "No theatrics. Just a finger pistol if you go rogue."
    "You both laugh — a small, human punctuation. The chamber settles as Councilor Nguyen taps the gavel and the room goes live."
    hide mateo_ros
    hide aiko_navarro

    scene bg ch3_98c6f2_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A digital chime as Selene's feed connects]
    # play music "music_placeholder"  # [Music: Underlying rhythm tightens, staying optimistic]

    "Dr. Selene Park (Hologram)" "Good afternoon. I look forward to assessing all proposals."
    show councilor_nguyen at left:
        zoom 0.7

    councilor_nguyen "Thank you, Dr. Park. We'll hear from our community presenters first."
    "You step to the podium. The floor feels solid. Your notebook, pressed against your ribs, is as much a talisman as the locket. You tell yourself the town's stories are as rigorous as data; that the people at risk are not variables but collaborators. You breathe, and you begin."
    show aiko_navarro at right:
        zoom 0.7

    aiko_navarro "Councilors, neighbors, friends — I'm Aiko Navarro. I grew up on Low Street; when the sea took my mother's porch, I learned that knowledge isn't only years of charts — it's the way Rohan reads the tides, it's Ivy's market route that must keep going, and it's Tala's organizing that turns noise into a plan people can follow."
    "(You let the name-drop land. It warms the room. Eyes soften. Tala's jaw relaxes; Rohan's hand tightens on his cane in a small, proud clench.)"

    aiko_navarro "Our marsh restoration prototype is built to be deployable now, to be maintained by the people who live with the tides, and to prioritize species and livelihoods together. It uses low-cost scaffolding, native planting sequences, and locally sourced materials. The model we tested at Tidepark greenhouse reduced erosion in trial plots and increased juvenile fish shelter by measurable margins."
    hide councilor_nguyen
    hide aiko_navarro

    scene bg ch3_98c6f2_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A quiet murmur of approval; someone nods]
    "You move through the speaking points — human picture first, model second, ask last. You wave a hand to the slide where community volunteers bend into the mud, faces streaked with salt and laughter. You explain"
    "the maintenance schedule, the training program, and the materials budget. You mention adaptability: staged rollouts, checkpoints, and shared governance."
    "Your measured voice carries data and people in the same sentence. That is intentional. You see Councilor Nguyen's hand unconsciously rub the edge of a tablet; his interest is present, practical."

    menu:
        "Open with the personal story of your mother's porch":
            "You let the memory come out whole: the creak of boards, the smell of sea-sap on her scarf. Councilors lean forward; the room narrows to faces and that small, shared ache. Tala wipes her eyes discreetly."
        "Begin with the sediment-retention chart to establish credibility":
            "You start with the numbers: percent retention, sampling intervals, confidence bands. Heads tilt toward the data; Dr. Park's hologram registers a micro-adjustment. Mateo's finger taps along the timeline in approval."

    # --- merge ---
    "The Q&A begins like the spray before a storm: salt-tinged and alive."

    "Dr. Selene Park (Hologram)" "Aiko, your work is compelling. However, local-only systems scale slowly. My firm can seed engineered mangrove scaffolds and deploy algae barrier arrays within weeks, with contract-backed performance guarantees. Wouldn't the town be better served by a solution that assures measurable protection on municipal timescales?"
    "Her tone is brisk but not unkind; the kind of voice that assumes inevitability. You can see the projection's background infographics shift to timelines and ROI curves."
    show aiko_navarro at left:
        zoom 0.7

    aiko_navarro "Dr. Park, speed and measurable outcomes matter — we agree on that. But measurable doesn't always mean equitable. Past deployments have produced measurable metrics at the expense of displacement. Our approach is staged to be measurable too; we track biodiversity indices and household safety, and we include training so maintenance doesn't become an outside contract."

    "Dr. Selene Park (Hologram)" "Staged programs are riskier."

    aiko_navarro "Risk is part of any honest plan. Our risk is social: loss of livelihood, erosion of trust. We mitigate by embedding local stewardship. When maintenance is local, response time improves, and long-term costs fall."
    "Mateo Ríos leans forward, adding calm ballast."
    show mateo_ros at right:
        zoom 0.7

    mateo_ros "If I may—there's a place for both approaches. The municipal hybrid I sketched is designed to combine institutional procurement with local labor and oversight. It buys some speed, but retains local governance mechanisms."
    show councilor_nguyen at center:
        zoom 0.7

    councilor_nguyen "Cost? Timeline? Accountability?"

    mateo_ros "Phased funding, deliverables tied to community checkpoints, municipal procurement engine for scale. It's a middle path."
    "Tala stands, voice like a bell."
    hide aiko_navarro
    show tala_kumari at left:
        zoom 0.7

    tala_kumari "Middle paths can be sweet words for compromise that leaves the most vulnerable out. We want control. People who live here should decide how their marsh is managed."
    hide mateo_ros
    show old_man_rohan at right:
        zoom 0.7

    old_man_rohan "We've lost shores before. You want quick concrete? You'll lose the eelgrass and the crab nurseries. You'll push some people to the road. If they won't listen to us, who will tend the marsh when the contracts end?"
    "Ivy, cheeks flushed from the cold, speaks up in her frank market voice."
    hide councilor_nguyen
    show ivy_navarro at center:
        zoom 0.7

    ivy_navarro "My neighbors aren't asking for a tech miracle. They want work that keeps rent down and nets to mend. Which option gives us that?"
    # play sound "sfx_placeholder"  # [Sound: A low, expectant hum — the chamber's air seems to hold its breath]
    "A corporate representative — a crisply dressed local liaison for Dr. Park's firm — stands now, hands folded."

    "Corporate Rep" "Our deliverables include workforce training modules and community liaison officers. We have philanthropic offsets for relocation as needed. We can front funding and guarantee system performance."
    "Tala narrows her eyes at the last phrase."

    tala_kumari "Guarantee doesn't mean community."
    "The room briefly fragments into a dozen small arguments — practicalities and principles, fear and hope. But beneath the noise the BGM keeps a hopeful line. Your arousal level rises with your pulse — not panic,"
    "but the warm, focused attention of a person who knows the stakes and feels the possibility."
    "You scan the room. Mateo watches you like someone silently offering a steady hand. Rohan's gaze is slow and honest. Ivy's worry is sharp, immediate. Dr. Park's hologram flicks, composed and expectant. Councilor Nguyen clears his throat, hands folded."
    hide tala_kumari
    show councilor_nguyen at left:
        zoom 0.7

    councilor_nguyen "Ms. Navarro, your plan is persuasive. We need a recommendation from you: given all voices, who should we invite into a pilot program? A local consortium, a municipal hybrid, or Dr. Park’s firm? Your recommendation will shape alliances and resources."
    "The room quiets. The air feels charged in that hopeful way things feel right before a decision that matters. This is the cliff-edge you rehearsed for in your notebook. Your internal monologue runs through the checklist — principles, people, timelines, leverage."
    "You feel the community in the back of the room like a tide: Tala's determination, Rohan's memory, Ivy's immediate need. You feel Mateo's cautious optimism like a rope tied around your waist, steadying you toward scale."
    "You feel Dr. Park's certainty like wind at your back, promising speed and measured metrics."
    "You thought of every compromise you might make on the walk here. You imagined grant cycles and training schedules, the smell of wet peat and the taste of salt on your tongue when you're kneeling in"
    "mud. You imagine the marsh alive with juvenile fish again, hands callused from planting stakes, and a ledger that matches the tides."

    menu:
        "Answer with a principled, community-first recommendation":
            "Your voice is quiet but firm. The room leans in. Tala's eyes shine. Rohan nods slowly, the lines on his face easing. Some council members exchange thin smiles; others glance at Dr. Park's hologram with polite concern."
        "Recommend Mateo's municipal hybrid, emphasizing scale and oversight":
            "You outline the municipal hybrid's ability to scale and the accountability checkpoints. Mateo's expression relaxes into relief. Councilors sit straighter, seeing a plausible path toward funding. Tala's jaw tightens; she folds her arms."
        "Propose opening to Dr. Selene Park's firm for speed and resources":
            "You emphasize the urgency of protection and the firm's capacity to act quickly. The corporate rep straightens; Dr. Park's hologram manages a small, satisfied incline of the head. Tala's lips purse; Rohan's brow creases with worry."

    # --- merge ---
    "The room holds as Councilor Nguyen's gaze rests on you, expectant and patient."

    councilor_nguyen "Ms. Navarro?"
    "You inhale. The whole room is listening. The town's next steps tilt on the word you are about to say."

    menu:
        "Invite a community-led consortium—us, local fishers, and Tala's groups.":
            jump chapter4
        "Recommend Mateo’s municipal hybrid plan—public funding plus municipal oversight.":
            jump chapter8
        "Open the pilot to Dr. Selene Park's firm—the fastest funder and tech.":
            jump chapter12
    return
