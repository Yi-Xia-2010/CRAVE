label chapter1:

    # [Scene: Harrow Bay Boardwalk | Early Morning]

    scene bg ch1_Start_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the gentle slap of shallow water on pilings, a toolbox clink somewhere down the boardwalk]
    # play music "music_placeholder"  # [Music: Quiet, minimal piano with gentle synth pads]
    "You step onto the boardwalk with the tide pulled back like a held breath. The wooden planks give a familiar, uneven response under your boots — a slow, measured creak that marks every step. Salt crystals"
    "cling to the edges of railings; algae leaves faint green fingerprints on your jacket as you brush past. Even at low tide, the harbor smells like iron and kelp, the air thick with humidity that leaves"
    "a trace of ocean on your tongue."
    "Your satchel swings against your hip. Inside: a slim tablet with notes on last season’s repairs, a stack of field cards clipped in a neat row, and a folded photo of the garden you once had"
    "to move. You feel the weight of that picture as a tactile thing, tucked under paper and policies: an ache that organizes itself into careful priorities."
    "You pause at the first gap — a short stretch of board washed loose by last month's swell. Jonah is there already, sleeves rolled, measuring tape looped over one shoulder. He looks up as you approach, and his smile is the kind that softens the morning's dampness."
    show jonah_mek at left:
        zoom 0.7

    jonah_mek "Mornin', Maya. You timed it well. Low tide gives us access to the lower joists without the kit-rafts."
    show maya_soren at right:
        zoom 0.7

    maya_soren "Good. I want to get this section done before the market opens. How's the cedar stock? Any surprises?"

    jonah_mek "Mostly the usual—some board rot deeper than we guessed. I can splice in reclaimed beams, but it'll show. The neighbors like visible repairs; makes them trust the work's local.' (He taps his utility belt.) 'Also — Rosa sent over jars of sea-salt caramel for morale.' He grins. 'And for bribery."
    "You let out a low laugh that tastes like salt and resolution. You run a hand over the loose plank, feeling the gummy residue where old tar meets wood."

    maya_soren "You could push for replacement with treated composites — longer life, less maintenance — but treated composites mean budget negotiations with the council, and the council means Asha's scrutiny and the neighborhood's memory of being displaced. So you hold the line on reclaimed wood when possible, prioritize visibility and repairability. It's a small, stubborn ethics you live by, and Jonah knows it."

    jonah_mek "You want me to start the splice? Or you handling stakeholder calls while I sweat?"

    maya_soren "I'll call Rosa and cut the materials list. Can you handle the splice with the apprentice? And Jonah— thank you for covering the promenade side. We need it done by midday inspection."

    jonah_mek "You drive a hard bargain.' (He winks.) 'Coffee after? I found a vendor selling proper drip."

    menu:
        "Take Jonah up on the coffee":
            "You accept. The promise of a hot cup steadies the morning; Jonah's grin widens and he sets his tape down, already talking about roast profiles."
        "Decline — stay on the clock":
            "You shake your head, fingers already typing into your tablet. Jonah nods, understanding. He tucks the coffee plan away but mutters about making you pay in later favors."

    # --- merge ---
    "..."
    "You duck into the market corridor adjacent to the boardwalk to call Rosa. Stalls are waking up: nets hung to dry, jars catching light, an older woman arranging succulents without gloves. The air here is warmer, perfumed with frying plantain and the metallic dust of new tools."
    "Rosa Calder greets you with the same steady, stubborn energy she used to give seedlings. She is small, hands knuckled with age and soil, braid threaded with sea-grass. Her garden is a rumor turned settlement; even at dawn she is arranging packets of seeds like prayers."
    show rosa_calder at center:
        zoom 0.7

    rosa_calder "Maya, child. The lower quay misses you. How are you?"

    maya_soren "I'm good, Rosa. Boardwalk repairs first thing. I wanted to ask about the community beds — any seeds you want prioritized for the rooftop? I'm drafting a supply run list after this."

    rosa_calder "Always the practical one. Tomatoes and chickpeas. And corn if you have the space.' (She pauses, eyes on you.) 'And Maya—take care. When you rally people, make sure you remember the stories that root them. Policies don't plant themselves."

    maya_soren "I know. I'll be careful."

    rosa_calder "Good.' (She presses a small packet into your hand — pepper seeds, dry and warm.) 'For luck."
    "Her fingers are warm and smelling of soil when they brush yours. For a second you feel the old weight of belonging — the particular tether of someone who remembers what grew where."
    # [Scene: Tide-steps by the lower quay | Mid-Morning]
    hide jonah_mek
    hide maya_soren
    hide rosa_calder

    scene bg ch1_Start_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft scrape of boots on algae, a distant laugh from children testing the exposed sandbar]
    # play music "music_placeholder"  # [Music: Low, rhythmic marimba tapping, unobtrusive]
    "You climb down to the tide-steps to inspect the pilings Elias mentioned on a message last night. He'd left a note about testing a prototype — a hybrid system: sea-wall framing combined with kelp-rooted revetments. It sounded both daring and sane, like him."
    "Elias Voss is bent over a stack of laminated schematics, the edges softened by salt. He looks up when you approach; his hair is still damp from an early sensor drop, and he has that out-at-sea brightness in his eyes."
    show elias_voss at left:
        zoom 0.7

    elias_voss "Hey. You found my note. I wasn't sure you'd have time before the market."
    show maya_soren at right:
        zoom 0.7

    maya_soren "I have time. Show me."

    elias_voss "So — imagine the conventional sea-wall, but modular. Sections anchored to pilings and interlaced with living kelp traps. The kelp's root mats help diffuse wave energy, and the modules are designed to be repaired by local crews.' (He taps a diagram.) 'You know the usual concerns: local ecology, displacement. I designed the modules to be small, so they don't require heavy machinery."
    "You study the schematic. The diagram is neat, annotated in Elias's quick hand: buoyancy chambers, biodegradable mesh, attachment collars sized for the quay's pilings."

    maya_soren "Elias's optimism always presents itself like a lever — here's an idea, pull it and whole things shift. You're used to weighing the lever's fulcrum: who it helps, who gets pushed. Your instinct is to map consequences before you let the hope take root."

    maya_soren "This looks thoughtful. Small-scale is better politically. But kelp restoration can change currents or siltation; Dr. Huang is going to want modelled impacts. Also — who owns the modules once they're deployed? The council? A community trust?"

    elias_voss "Exactly — ownership was my sticking point. I wanted it to be community-governed, but the initial funding lines push to private stakeholders.' (He runs his hand through his hair.) 'That's why I need your voice, Maya. You can make the governance proposal listen to the people who'll live with it."
    "He watches you as if measuring the probability that you'll say yes. There's a light nudge of intimacy in the way he defers to you on governance: he trusts your steadiness."

    elias_voss "I ran a small test bed last winter — kelp took, pilings reduced impact by measurable amounts. If we can combine the modules with community-led maintenance, it could be scalable without corporate strings."

    maya_soren "The data would need to be transparent. And any funding has to include guarantees for displaced livelihoods if we change fish paths.' (You tap the tablet; your fingers leave wet prints.) 'I'll file this and call a convening at the Resilience Hub. We need stakeholders in one room: residents, scientists, activists, craftworkers."

    elias_voss "You'd do that?' (His smile is a slow sunrise.) 'I know you have history with convenings—"
    "He stops, searching your face. There's something tentative in his tone that isn't there when he's talking to instruments. You can feel the small shift — this is more than a technical ask for him. His hope has threaded through to something that wants your presence."

    elias_voss "And Maya… if this could really help Harrow Bay, I'd like you to be part of the steering group. With you in it, we get the community perspective honestly."

    maya_soren "I'll need details for the agenda. And transparency on the modeling. Dr. Huang will expect simulations before she signs off. Also—' (You hesitate, because habit takes your pen to the old, sensitive spot) '—invite Asha. She'll either break it or make it stronger."
    "Elias's expression tightens a fraction."

    elias_voss "Asha — yes. I know things have been… complicated.' (He looks beyond you, at the stretch of the quay where Asha was last seen organizing the seed exchanges.) 'But she keeps us honest. I'd rather have her in the room than out in the street shouting."

    maya_soren "We'll invite everyone. No decisions that shut people out."

    menu:
        "Ask Elias about ecological trade-offs first":
            "You lean over the schematic and press for clarity on possible silt shifts. Elias appreciates the technical interrogation and launches into a calm, detailed run-through, pulling up numbers on his tablet; his confidence shifts into researcher mode, which you respect."
        "Focus on governance and community control":
            "You steer the conversation toward ownership language and repair logistics. Elias relaxes; his eyes soften when you speak of community maintenance teams, clearly relieved to have you anchor the social side."

    # --- merge ---
    "..."

    elias_voss "I'll get the modeling notes to you by afternoon. And—' He hesitates, searching for a bridge between professional and personal. 'Would you… want to ride out the prototype trial? Come with me on the Aster for a day? It’s low-key, mostly sensors and checks. I figure you could see it in action."

    maya_soren "The sea-vessel is a different rhythm — days of wet metal and calculated motion. Your first relief deployments were on ships like that. Your impulses drink the ocean and pay attention to its moods."

    maya_soren "I'll consider it. I need to get the boardwalk splices done and a convening scheduled. But I want to see the data myself.' (You fold the schematic and tuck it into your satchel.) 'Elias — thanks. This could be something."

    elias_voss "It could be."
    # [Scene: Market Exit toward Resilience Hub | Late Morning]
    hide elias_voss
    hide maya_soren

    scene bg ch1_Start_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low chatter, the distant clang of municipal maintenance, a soft radio broadcasting council minutes]
    # play music "music_placeholder"  # [Music: Soft guitar arpeggio, steady and warm]
    "As you leave the market, Asha appears at the edge of the walkway like a flare of color against the boardwalk's muted tones. She's mid-argument with two volunteers, gesturing with a hand-painted poster and a stack"
    "of seed packets. When she sees you her posture shifts — not openly hostile, but unreadable in the precise way that makes you hold your breath."
    show asha_reed at left:
        zoom 0.7

    asha_reed "Maya."
    show maya_soren at right:
        zoom 0.7

    maya_soren "Asha."

    asha_reed "Elias has been busy.' (She scans the diagram with a practiced skepticism.) 'Hybrid walls. Modular kelp traps. It reads like optimism on stilts — I'm not against tech. I'm against fixes that ship governance away from the people who plant their lives here."
    "Her eyes, always sharp as a compass, find yours. There's a history in them — accusation, affection, and a steadying loyalty to the neighborhoods."

    maya_soren "He's proposing community governance. He asked that you be in the room. I want a convening at the Resilience Hub — everyone at the same table. No decisions that shut people out."

    asha_reed "A convening is good. But we need real guarantees, Maya. Not promises tucked into funding memos. Who audits the data? Who controls maintenance contracts? Who gets the labor? These are not rhetorical.' (She leans closer, voice low.) 'We've seen 'community' used as a label so funds can be fenced off to others."

    maya_soren "You sense the friction more than hear it: Asha after heartbreaks of past displacements, Elias after prototypes that hurt people, and you in the middle, trying to make policy into living things. The air between you carries the same damp as the sea, but layered with more complicated currents."

    maya_soren "We'll set the agenda around those exact points. Auditing, contracts, labor commitments, dispute resolution. No one signs anything until the community trust clause is in the charter."

    asha_reed "I'll hold you to that, Maya.' (Her hands find the bandolier of seed packets at her shoulder; she offers you one without smiling.) 'And if you cut corners to make the numbers look pretty —' (Her voice is quieter now, near to a warning.) '—I'll organize people who won't let you get away with it."

    maya_soren "I don't plan to cut corners. I plan to make space for grief and for repair.' (You look at her, and for a beat the sharp edges of distrust soften.) 'We both want Harrow Bay to survive. We just disagree about how to trust the people who survive it."
    "Asha's expression is complex — neither softened nor hardened completely. She nods, a small, guarded concession."

    asha_reed "Then bring the proof. Bring the audits. Bring Dr. Huang's models. And don't let Elias's charisma be the only metric."
    "Elias, who has been listening from a few feet away, straightens. His face is open but there is a line of tension in his jaw."
    show elias_voss at center:
        zoom 0.7

    elias_voss "I wouldn't want it any other way.' (He looks from Asha to you.) 'We can lay everything on the table."

    maya_soren "Good. We meet at the Resilience Hub this afternoon. I'll send invites, schedules, and the items to be tabled. Come prepared to propose real oversight measures."
    # [Scene: Walk to Resilience Hub | Noon]
    hide asha_reed
    hide maya_soren
    hide elias_voss

    scene bg ch1_Start_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Your footsteps against the raised walkways, a muffled drum of distant repair work]
    # play music "music_placeholder"  # [Music: A calm piano motif carrying a subtle upward motion]
    "You walk toward the Resilience Hub with the schematic folded in your satchel, Jonah’s measured footsteps beside you as he carries the splice tools. The walk is short but not trivial: it's the distance between fieldwork and governance, between the salt and the city hall."
    "Your internal rhythm steadies: the convening will require agendas, minutes, neutral facilitators, and contingency plans. Organizing has always been a way you arrange grief into structures that can be shared."
    show maya_soren at left:
        zoom 0.7

    maya_soren "You file Elias's prototype under 'urgent follow-up' and promise yourself to prepare questions for Dr. Huang about model sensitivity. You promise Asha that oversight will be non-negotiable. You promise Jonah coffee and to check Rosa’s community beds this evening. The promises feel like bricks for a modest bridge."
    "You step up the ramp into the warm amber light of the Resilience Hub rooftop garden — the place that is by design both refuge and instrument. Green smells, condensation on glass, the low hum of"
    "community fermenters. You can already picture the room: folding chairs arrayed in half-moons, a cleared whiteboard, the soft buzz of neighbors crossing into civic work."
    "You pause at the threshold, feeling the gentle increase of pressure that comes with convening people around hard things. It's not panic; it's the steady pull of responsibility. The schematic in your satchel is a small,"
    "tangible hope. Asha’s guarded nod and Elias's bright insistence are two hands on different ends of the same rope."
    "You take a breath, cool and briny, and step into the hub, a facilitator of intentions."
    # play music "music_placeholder"  # [Music: The piano motif resolves into a single held chord — an invitation to attention]
    "You set the packet on the central table, fingers pressing down to hold paper and possibility in place. Around you, the rooftop leaks the quiet murmurs of people beginning to arrive: a neighbor setting a bowl"
    "of seaweed salad near the seating, Dr. Huang's white coat materializing at the edge with an analytical expression, volunteers arranging chairs. The air is full of ordinary, earnest momentum."

    maya_soren "There will be disagreements. There will be technical footnotes and moral footnotes and moments where the word 'compromise' tastes like ash. But there will also be the work itself — the steady, communal labor of tending a city that can't be left to slogans."
    "You lift your head. Outside the glass, the water is horizon-smooth, and a gull traces a slow arc. Inside, people set their desks, their chairs, their expectations."
    "You file the prototype into the hub's shared registry on your tablet and create a docket: kelp/sea-wall hybrid, modeling needs, governance terms, labor guarantees, community audits. You tap 'Save.'"

    maya_soren "I'll convene the stakeholders here this afternoon. We'll start with diagnostic modeling, then governance frameworks, then community commitments. We hold each other to transparency."
    "You notice Elias watching you, a look that is easy to read now: hope folded into cautious faith. Asha stands near the herb beds, arms crossed but present."
    "The city hums. The tide will return. People will arrive."
    "You inhale the wet air, ready to gather voices into a plan that, you hope, will keep Harrow Bay whole."
    hide maya_soren

    scene bg ch1_Start_5 at full_bg
    # play music "music_placeholder"  # [Music: The piano motif softens, leaving a single sustained note]
    "You step back, letting other preparations continue. It's time to let the room fill, and to let arguments begin — the careful, slow labor of making policy from people's lives."
    # [Page-Turn Moment]
    "You stand at the center of the rooftop garden, a quiet hub of intent. Outside, the bay's skin shifts; inside, chairs scrape and voices warm up. The schematic in your satchel is more than paper now"
    "— it's a question you will ask aloud, a compromise you must hold, a small promise to the neighborhoods who will live with whatever you decide. For a moment you let the city's damp, briny breath"
    "wash over you and feel both the weight and the possibility of what comes next."

    scene bg ch1_Start_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter2
    return
