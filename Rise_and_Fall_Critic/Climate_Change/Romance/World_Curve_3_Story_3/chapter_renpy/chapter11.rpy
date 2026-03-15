label chapter11:

    # [Scene: Saltbridge Boardwalk | Early Morning]

    scene bg ch9_6b08b4_1 at full_bg
    # play music "music_placeholder"  # [Music: Gentle piano with soft strings — an ascending motif that feels like careful breathing]
    # play sound "sfx_placeholder"  # [Sound: The dull slap of boots on wet wood; distant laughter; the tinny hum of a generator]
    "You keep your jacket collar up against the spray and let the damp smell of seagrass and diesel stitch you back into the morning. The boardwalk is not the oldscape of summer fairs and late-night songs,"
    "but it is yours — the ledgered lines of your notebook tucked under your arm prove that, and the compass at your throat is warm from the walk. People pass with tool belts and thermoses, faces"
    "set but kinder than they were last winter."
    "Finn steps out from between two pallets, grinning as he tests a freshly refitted bilge pump. His hands are salted with grease; the small crew he leads — a patchwork of teenagers and older fishers — looks up to you as if you've already been part of the plan."
    show finn_serrano at left:
        zoom 0.7

    finn_serrano "Morning, boss. Soup shift tonight? Rosa says your meetings are eating her stock."
    "(he says, half a tease, half pride)"
    "You let a laugh loose that surprises you with how easy it feels. The laugh folds itself into a breath you hadn't realized you needed."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "Soup helps. Paperwork eats the supply. Both are important.' (You glance toward the dunes where the new green berms hum with early planting crews.) 'How's the boat?"

    finn_serrano "She leaks emotionally, but the pumps like her now.' (He taps the hull with a mock-serious nod.) 'We've got her mostly sealed. Elias Novak is bringing the last of the volunteer riggers out to check the lashings."
    "Elias Novak appears from the other end of the boardwalk, a canvas tool bag slung off one shoulder, his scarf damp with salt and paint. He moves with the easy, urgent gait you know — the"
    "kind that collects people as it goes. When he sees you, the hint of a grin softens to something steadier."
    show elias_novak at center:
        zoom 0.7

    elias_novak "You look like you slept clutching a blueprint. Are we signing anything today, or just moving piles of sand?"
    "You hold his gaze. There is history there — the late-night protests, the shouted chants, the fevered meetings — and a quieter thread: shared coffees, elbows knocking over folding tables, the way he listened when you"
    "could not sleep. You feel the warmth of that memory like a physical thing, then tuck it back behind the practical hum of the day."

    maya_serrano "A bit of both. We finalize the oversight panel later; Dr. Hana wants to run the shoreline models this afternoon. Noah Kestrel's team is bringing the funding schedule. Rosa's running the logistics."
    "Elias Novak: (tilting his head) 'Noah Kestrel's here already?'"

    maya_serrano "He dropped off a list of contractors last night and stayed to talk. Brought soup, actually. I didn't expect soup."
    "Elias Novak's laugh is quick and relieved."

    elias_novak "That man understands negotiation vocabulary and soup. Saltbridge is already softer for it."

    menu:
        "Smile and wave to Finn":
            "You give Finn a brief, steady smile — the sort that says you're proud and tired and not yet broken. He grins back and returns to the pump, humming an old boat song."
        "Keep walking, focus on the plans":
            "You tuck your chin and keep walking, letting the practical list spool through your head. The plan has corners that need ironing; there's grace enough for later."

    # --- merge ---
    "Continue to rooftop sanctuary scene."
    # [Scene: Rooftop Sanctuary (Reclaimed Mall Garden) | Late Morning]
    hide finn_serrano
    hide maya_serrano
    hide elias_novak

    scene bg ch9_6b08b4_2 at full_bg
    # play music "music_placeholder"  # [Music: Light harp and airy pads — the motif lifts like sunlight through greenhouse glass]
    # play sound "sfx_placeholder"  # [Sound: A soft murmur of conversation; the scraping of metal stakes; the occasional chirp of a recording device]
    "Dr. Hana stands at the projection, sleeves rolled, eyes bright behind her glasses. Her voice is steady and quick; she gestures to living shoreline diagrams that show how oyster reefs and marsh grasses bend wave energy and give the sea places to be soft instead of deadly."
    show dr_hana_park at left:
        zoom 0.7

    dr_hana_park "We prioritize blocks with the highest density of elderly residents and the lowest evacuation access. Roof gardens buy time and food security. If we stagger work with the job training program, we can have local crews maintain everything and keep money circulating here."
    "You move through the small crowd, letting the technical language land and translate into the faces you know. This is where your stubborn practicality meets the models Hana loves: numbers become neighbors, graphs become thresholds between homes saved and homes lost."
    "Noah Kestrel stands near the projection, tablet in hand, sleeves rolled as much from habit as necessity. His eyes catch yours for a fraction longer than polite conversation requires; there's something careful in that look now — less distance than before, more a steady presence."
    show noah_kestrel at right:
        zoom 0.7

    noah_kestrel "The firm will release the first tranche once the oversight charter is signed. We agreed to community representation and an audit clause. There are stipulations — buyouts in the highest-risk rows — but we also committed to the jobs fund and to subsidized rooftop retrofits."
    show maya_serrano at center:
        zoom 0.7

    maya_serrano "Some families won't return.' (the sentence leaves a small ache behind your ribs) 'Some houses are more than wood and nail. They're memory and maps."
    "Noah Kestrel: (nods, jaw tightening) 'I know.' (He searches for the right words, the engineer's way of measuring feeling against facts.) 'We pushed on the buyout terms. We made space for relocation counseling and for grants"
    "to preserve artifacts — photographs, plaques, community murals. It's not enough to bring a foundation; we need to carry stories.'"
    "You feel a swell of relief at the last line — the idea that material mitigation can attend to memory. Relief and guilt trade a small, human bartering between your ribs."

    maya_serrano "Dr. Hana's models show that the living shoreline option reduces wave energy by the time we hit those rows. If we plant aggressively and the jobs program works, we can build local capacity instead of outsourcing maintenance."
    "Dr. Hana: (smiling, tired) 'And the rooftop network expands your food security footprint. People can stay — not all, but many. It's incremental healing.'"

    noah_kestrel "Incremental is durable. It's slower, but it includes people."
    "Elias Novak moves closer, folding his arms. He looks at Noah Kestrel, then at you, then back to the projection."
    "Elias Novak: (softly) 'You did this. You held the line and let people argue long enough to get here.'"
    "You: (inwardly) You think of the neighbor's dark porch, of the red thread on your wrist. You think of the nights you stood at the hall's doorway and felt the town's pulse like a second heartbeat. The gratitude in Elias Novak's voice is a warm, complicated cloak."

    maya_serrano "We did it together. Nobody did it alone."
    "Noah Kestrel: (quiet) 'I meant what I said about the audit. If anything looks like it's edging toward displacement for profit, pull the committee. I'll back you.'"
    "You look at him — at the careful set of his mouth, the way his eyes soften when he thinks no one is watching. You remember warm soup in a paper bowl, handed over during a"
    "night with no power. You listen to the hum of the rooftop bees and the low, patient sound of people planning repair."

    menu:
        "Accept the offered mug of soup from Noah":
            "You accept. The warmth goes into your hands before it fills your stomach. For a moment you let the practical kindness wash the edges off the guilt."
        "Decline politely, focus on the map":
            "You decline with a small smile. There's still money to track and meetings to hold; practicality asks for space, and you give it to her."

    # --- merge ---
    "Continue to Rosa's Café scene."
    # [Scene: Rosa's Café | Early Evening]
    hide dr_hana_park
    hide noah_kestrel
    hide maya_serrano

    scene bg ch9_6b08b4_3 at full_bg
    # play music "music_placeholder"  # [Music: Warm cello under soft acoustic guitar — steady, rising]
    # play sound "sfx_placeholder"  # [Sound: Clink of ceramic, low-conversations, the comforting hiss of espresso]
    "Rosa moves with the practiced efficiency of someone who has spent decades making other people's days better. Her hands are flour-dusted and steady; she sets a steaming tray down and meets your eyes."
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "We set up a triage schedule. Counselors from the health clinic are coming on Thursdays. Finn's team is handling emergency routes. Noah Kestrel's fund gets its first payroll next week.' (She pauses, then adds, in a softer voice) 'You look like you need a pastry."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "I need a sleep training program and an accountant."
    "Rosa: (laughs) 'One bite of a danish, then the accountant.'"
    "Elias Novak sits opposite you, hands wrapped around a mug. He watches the room with an organizer's attention: who comes in, who waits, who needs a chair. The café is slowly filling with people who are frightened and braced for the slow work of repair."
    show elias_novak at center:
        zoom 0.7

    elias_novak "We had three families agree to the retrofit program today. They were scared, but when they saw the models, they decided to stay. I told them about the job openings for maintenance. I told them who to call."

    maya_serrano "You gave them names?"

    elias_novak "I gave them your name.' (He watches you for how you take it.) 'Because you pushed for the oversight charter."
    "You feel the weight shift — a lessening that does not remove the ache of loss, but eases the hand at your back."
    "Noah Kestrel arrives with a crate of soup and a stack of forms. He moves with the quiet competence of someone who has learned to be present in practical ways. He sets a pot down and offers you a ladle. The gesture is small, but it lands like an anchor."
    hide rosa_alvarez
    show noah_kestrel at left:
        zoom 0.7

    noah_kestrel "I tightened the contractor agreements. We have clauses for local hiring and penalties for noncompliance. I also put in an allocation for cultural preservation — plexi boxes, climate-controlled storage for murals and documents.' (He meets your eyes.) 'We can make room for stories."
    "Maya Serrano: (your voice is steady, softer than the morning) 'Thank you. For pushing and for... being here.'"
    "Noah Kestrel: (shrugs, then smiles faintly) 'Someone has to read the fine print. Someone has to hold the ladle.'"
    "Elias Novak reaches across the table and takes your hand for a second — a quick, fierce contact that says more than words. Finn, from across the room, calls a joke in a loud voice that breaks the tension and gets everyone laughing in a small, bright herd."
    "You: (narration) The guilt you have carried for months softens into a sober steadiness. It does not vanish; it becomes work: training crews, making meetings accessible, ensuring oversight is real and enforceable. You are tired, but"
    "not without resources. You have community. You have promised structures that will outlast one person."
    "Dr. Hana joins your table, eyes kind and clear."
    hide maya_serrano
    show dr_hana_park at right:
        zoom 0.7

    dr_hana_park "There's still hard work. People will grieve the rows we can't save. But we created pathways—economic, emotional, procedural—that weren't there before. That's real change."
    hide elias_novak
    show maya_serrano at center:
        zoom 0.7

    maya_serrano "Does it feel like victory?"
    "Dr. Hana: (after a beat) 'It feels like beginning to heal.'"

    menu:
        "Offer to run the relocation counseling sessions":
            "You volunteer. Your voice is practical and calming; the room accepts your steadiness with relief. It is another night of work, but it ties you to people in a way paperwork never could."
        "Organize the job training schedule instead":
            "You volunteer for logistics. Your hands find the ledger, and the chaos begins to organize into time slots and mentors. It is a different kind of intimacy — steady, essential."

    # --- merge ---
    "Continue to Saltbridge Community Hall scene."
    # [Scene: Saltbridge Community Hall | Late Night]
    hide noah_kestrel
    hide dr_hana_park
    hide maya_serrano

    scene bg ch9_6b08b4_4 at full_bg
    # play music "music_placeholder"  # [Music: Swelling strings and a warm, bright synth—an ascending cadence that promises continuity]
    # play sound "sfx_placeholder"  # [Sound: Quiet applause; a single child laughing at the back; the rustle of paper]
    "Mayor Lillian Cho takes the podium with a practiced nod. Her posture is official, but there is a softness in the way she looks at the committee — the civic machinery finally aligning with community will."
    show mayor_lillian_cho at left:
        zoom 0.7

    mayor_lillian_cho "This agreement is not a perfect instrument. It will require oversight, accountability, and the continued involvement of every resident here. But it is a start — a legally binding start that keeps money local and work local."
    "Applause threads through the room. You feel hands on your shoulder, a quick squeeze from Finn, a private thumbs-up from Elias Novak. Noah Kestrel stands back, letting you step forward to say something to the assembled town. The words come as if pulled from that same compass at your throat."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "We didn't save every building. We didn't keep every old line of paint or every porch light. What we did do is build a system that listens. We made room for you — for repair crews from here, for preservation funds, for oversight that a committee with teeth can enforce. We fought to make safety mean everyone, not just those with access to investment."
    "The room is quiet enough that you can hear the old heater sigh. Somewhere outside, waves kiss the shore with an indifferent rhythm that is no longer only threat — it is part of the world you are learning to work with."

    maya_serrano "If this is the first sunrise of a long mending, then we are the people holding the seams."
    "The committee formalizes the oversight charter. Names are read. Signatures dry into the margins of the document like small promises. Finn's name is there as lead for the emergency vessels; Rosa's as logistic anchor for triage;"
    "Dr. Hana as scientific liaison; several community elders hold seats that were hard-won. Noah Kestrel signs, then Elias Novak, then Maya Serrano."
    "Noah Kestrel steps closer after the signing, his hand finding yours with a familiarity that has grown into something steady — not the fevered claim of raw intensity, nor the cool distance of an engineer; it's"
    "the kind of presence that says: I will be here when the tide is long and the night is cold."
    show noah_kestrel at center:
        zoom 0.7

    noah_kestrel "We did the thing we said we'd do. I'll keep my word."
    "You: (your internal voice) The red thread at your wrist slackens but does not fall away. It is tied, now, not only to a private promise but knotted into the communal work you have shaped. The"
    "guilt that once felt like a stone has become a stone you can set into the foundation."
    "Elias Novak: (softly, proud) 'And we'll keep yelling, if anyone tries to slip anything by the committee.'"
    "You all laugh — a small, real sound that feels like a roof finally shored. The tape lights on the hall flicker, the projector hums down, and people begin to file out into an evening that"
    "still smells of salt and wood smoke but also of frying onions and newly printed job flyers."
    "You walk outside with Noah Kestrel at your side and Elias Novak a few paces ahead, hands tucked into pockets, the sea folding itself along the shore. The town looks like it has been injured and"
    "is learning to stitch itself. It's not a picture you framed as victory, but it is, unmistakably, growth."
    "You: (narration) You rest for the first time in weeks on a bench looking at the slow work of lanterns being strung across the boardwalk. The oversight committee, the jobs program, the living shorelines — these"
    "are not the end of struggle. They are scaffolds. They are the beginning of a thicker, tougher hope."
    "Noah Kestrel: (quietly) 'Will you come by tomorrow to meet the first crew? Rosa's making extra soup.'"

    maya_serrano "Yes."
    "Noah Kestrel gives you a small, infrequent smile — the kind that holds its warmth for a long time. Elias Novak bumps your shoulder and turns toward the dunes, already talking about plants. Finn tests the"
    "bilge pump with a satisfied hum. Dr. Hana lingers to draw a new line on the rooftop map."
    "The town breathes. You breathe with it."
    # play music "music_placeholder"  # [Music: The motif resolves into a gentle, rising chord that promises continuity rather than finality]
    hide mayor_lillian_cho
    hide maya_serrano
    hide noah_kestrel

    scene bg ch9_6b08b4_5 at full_bg

    scene bg ch9_6b08b4_6 at full_bg
    "THE END"
    # [GAME END]
    return
