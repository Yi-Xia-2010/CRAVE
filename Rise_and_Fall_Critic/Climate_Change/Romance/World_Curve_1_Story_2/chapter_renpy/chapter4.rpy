label chapter4:

    # [Scene: Mika's Workshop | Dawn]

    scene bg ch4_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft thud of tide against the pilings; a distant gull.]
    # play music "music_placeholder"  # [Music: Low, hopeful hum — a steady pulse under the sounds of morning.]
    "You wake with sand in your teeth and the key warm against your palm — the residue of last night's decision still settling into bone. You promised the town your workshop, and your mouth tastes like"
    "the salt air that taught you to fix things. The promise is a weight and a promise at once: an obligation you chose because everyone else chose to stand beside you."
    "Tools clink as you move. The workbench smells of machine oil and seaweed tincture — your mother's smudge of lavender and stove smoke mingled with the ocean's metallic tang. You run your thumb across the braided"
    "string on your wrist, feeling the small comfort of rope that once tied a net. Today you tie other things together."

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: —]
    # play music "music_placeholder"  # [Music: —]
    show elias_maren at left:
        zoom 0.7

    elias_maren "Morning. I brought the new sensor kits and—' (he sets a box down gently, as if the parts inside could bruise) '—and another pot of coffee. Thought we might need it."
    show mika_hoshino at right:
        zoom 0.7

    mika_hoshino "You always know when there's going to be too little sleep.' (You strip the tape from a crate, letting the smell of salted rope spill out.) 'Good — we need that. Jun's coming with the volunteers, and Riv's already posted the pickup times. Mayor Amina said she'd stop by after council."

    elias_maren "She did?' (He flips the tide map open on the bench; soft sea-blue ink arcs like promise.) 'That's better than I expected. The modelers in the city were—well, let's say surprised by our numbers. If we can show a real reduction in surge over a test span, Amina's willing to put up seed funding."
    "You watch the way his fingers trace contour lines. When he talks about the currents, his voice loosens, and you notice the faint crease by his eye where the light catches. The map is not just paper; it's the shape of a possible future."

    elias_maren "These living lines — kelp ropes attached to anchored lines — change how energy moves at the surface. They dampen waves at their source. We can demo it in a controlled run this week if we get anchors, buoys, and a good deployment window."

    mika_hoshino "Anchors we can do. Buoys we can repair. Deployment window—' (you tap the worn metal of the key against the table) '—we'll buy it with timing and sweat."
    "Elias Maren smiles, small and grateful, and the boat of your chest rocks with it: relief, like a tide pulling something loose."

    menu:
        "Double-check every buoy seal myself":
            "You pick up a sealing kit and crawl under the workbench with a tiny flashlight. The rubber smells of salt and oil; it feels right to know the work at that level."
        "Let Elias test the electronic sensors first":
            "You hand Elias the sealed pack. He hums approval as he runs diagnostics; the screen blinks green, and you feel the practical burden shift a notch toward trust."

    # --- merge ---
    "Continue"
    # [Scene: Rooftop Greenhouse | Mid-Morning]
    hide elias_maren
    hide mika_hoshino

    scene bg ch4_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant harbor noise, soft footfalls on decking, the drip of condensation into metal trays.]
    # play music "music_placeholder"  # [Music: Warm, rising strings — intimate and small but building.]
    "You climb the rusted ladder to the greenhouse, crate under one arm. The air up here is heavy with breath — humid and alive. Salt-tolerant seedlings curl in nutrient film; copper pipes snake along the benches"
    "like veins. A small fan turns lazily, carrying the smell of wet soil and something green-sweet, like the inside of a tidepool."
    "Elias Maren kneels by a tray, eyes narrowed in that way that says he's both scientist and worshipper. He holds up a kelp seedling to the light; fibers glint like filament."
    show elias_maren at left:
        zoom 0.7

    elias_maren "Look how they cling. Less than a week and their holdfasts are forming. This strain's faster by days. If we seed ropes like this and anchor them in a staggered line, they should create a dense canopy within a season."
    show mika_hoshino at right:
        zoom 0.7

    mika_hoshino "Faster is better, but not if it unbalances harvest. Jun wants sustainable cycles — you know he'll push for quotas."

    elias_maren "I know. That's why your workshop is crucial. Local maintenance, local harvest windows, and sharing the data. If the community can tend and benefit, it's not a project imposed from outside."
    "You feel the warmth of the grow-lamps on your forearms and the soft grit of algae under your nails. Your practical instincts are counting out the tasks: floatation, anchor redundancy, community training. Elias counters by mapping"
    "growth curves and nutrient uptakes. Where you see bolts and rope, he sees systems and seasons. The friction between you is productive; it sharpens rather than dulls."

    menu:
        "Help Elias tie the prototype rope lines":
            "Your fingers find the knot pattern you taught yourself as a child. Elias watches your hands with an expression that is pure, unguarded admiration."
        "Adjust the camera angles for the dive footage":
            "You crouch by the monitor, fiddling with the cameras. The footage snaps into cleaner focus; Elias leans over your shoulder, and the proximity makes your heart stutter like a skipped wave."

    # --- merge ---
    "Continue"
    "Elias Maren: (soft laugh) 'You always choose the practical side. I love that about you. Even when I'm waxing scientific, I rely on your muscle.'"
    "You find the compliment both simple and enormous. It's quieter than promises and steadier than declarations — the kind of thing built by nights bent over benches and mornings hauling wet rope."
    # [Scene: Harbor — Loading for Subtidal Deployment | Afternoon]
    hide elias_maren
    hide mika_hoshino

    scene bg ch4_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Creaking boards, shouts of coordination, the slap of a crate into the barge.]
    # play music "music_placeholder"  # [Music: Energetic percussion — hopeful, forward-driving.]
    show jun_park at left:
        zoom 0.7

    jun_park "Right—everyone, listen up. We deploy in one tide window. Teams A and B on anchors. Team C with the buoys. Team D — rope and seeding. No one rushes ties; life depends on this."
    show ravi_riv_delgado at right:
        zoom 0.7

    ravi_riv_delgado "And snacks! I brought sandwiches. Moral fiber, people."
    show mika_hoshino at center:
        zoom 0.7

    mika_hoshino "Jun, show them the harvest rotation schedule. Don't let anyone get overambitious."
    "Jun: (gruff but grin-soft) 'I taught them to sand planks, not crush ecosystems. We'll rotate every plot, leave regrowth buffers, harvest low and steady.'"
    "Elias Maren: (checking a handheld) 'Drones are online. Live feed to the greenhouse. We'll be able to watch seedling attachment in real time. If the holdfast counts look strong, we can tweak anchor tension next run.'"
    "You feel the salt wind like a hand at the back of your neck, urging you forward. The barge lurches, and for a moment the town—so long a collection of separate lives—moves as one machine forward into the sea."
    # [Scene: Subtidal Restoration Site — Dive Footage Room | Early Evening]
    hide jun_park
    hide ravi_riv_delgado
    hide mika_hoshino

    scene bg ch4_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft shushing of water in speakers, murmured commentary from the volunteer team.]
    # play music "music_placeholder"  # [Music: A single piano line — fragile, then steady as growth.]
    "You stand shoulder to shoulder with Elias Maren, Jun, and a knot of volunteers around the monitor. The footage stutters, then smooths. Light filters through the kelp canopy, scattering gold-green shafts that make the water look like stained glass."
    show elias_maren at left:
        zoom 0.7

    elias_maren "There—see that? Three seedlings just latched in the last thirty seconds. Their holdfasts are small but vigorous. If we maintain this density, the canopy should reduce nearshore surge by measurable percentages."
    show jun_park at right:
        zoom 0.7

    jun_park "Measured percentages, eh? Show me numbers that let me sleep easy."
    "Elias Maren: (grins, turning the screen to a graph) 'Here. The model predicts a twenty-five percent reduction in wave energy within the test corridor after the canopy establishes. The live sensors on the buoys are already showing a drop during the last low-surge window.'"
    "You press your palm to the cool glass of the monitor. The image feels like a small miracle: green life where there was gray. In the crowd, hands clap quietly, like people accustomed to not expecting miracles but grateful when they arrive."
    "Mayor Amina: (voice steady; she stands framed in the doorway, scarf clamped against the wind) 'That's persuasive. Conditional approval — I need demonstrable metrics over two cycles and a community maintenance plan with shared governance. If you meet those conditions, the municipal grant is yours.'"
    show mika_hoshino at center:
        zoom 0.7

    mika_hoshino "We can provide that. We'll run the test cycles, publish the data, and put maintenance schedules to a vote at the next assembly."
    hide elias_maren
    show mayor_amina_bakar at left:
        zoom 0.7

    mayor_amina_bakar "Good. I want explicit volunteer training, agreed harvest quotas, and transparency audits. If this works, Atera's model can be a model for other towns. I want us to be careful, and I want us to be proud."
    "Her requirements are not roadblocks; they are scaffolding. You feel the town's future being measured not by single heroic gestures but by small accountable steps."
    # [Scene: Greenhouse — Night]
    hide jun_park
    hide mika_hoshino
    hide mayor_amina_bakar

    scene bg ch4_453e40_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low conversation, the clink of chopsticks, the faint tick of a sensor updating.]
    # play music "music_placeholder"  # [Music: Warm strings, rising with contentment.]
    "Mika Hoshino and Elias Maren sit with Jun and Riv under the greenhouse glass, bowls between your knees. The night outside is dark and slightly damp, but the greenhouse is a cocoon of warmth and living things. Your hands smell faintly of rope and diesel and kelp."
    show jun_park at left:
        zoom 0.7

    jun_park "Not bad for a day's work. You two are fast together. It's like watching someone read a blueprint and someone else hold the ruler steady."
    show ravi_riv_delgado at right:
        zoom 0.7

    ravi_riv_delgado "Also, those noodles are life-savers. Science says carbs improve morale."
    show elias_maren at center:
        zoom 0.7

    elias_maren "We couldn't have done it without the steady hands of this workshop.' (He looks at you; his gaze is soft and certain.) 'You kept the schedule and the crews and the temper."
    hide jun_park
    show mika_hoshino at left:
        zoom 0.7

    mika_hoshino "You made something that looks like magic to me. I make sure the magic doesn't fall through a hole in the deck."
    "Elias Maren: (half-teasing) 'So that's your role then — keep the magic from sinking. I'll be the one to get it breathing.'"
    "You trade a look — small, unembellished, but full of something that feels like trust taking shape. There's a pleasure in cooperation that is quiet and fuelled by shared, honest labor."
    # [Music swells gently; the greenhouse light eases like a promise.]

    menu:
        "Ask Elias about where he sees this five years from now":
            "You lean in, curiosity raw. Elias's hands pause in mid-air, and he draws a map with his words — kelp corridors, kids learning in the hatchery, a town less frightened of storms. Listening to him, you can imagine stitching your life into that map."
        "Remind Jun to file the maintenance manual tonight":
            "You nudge Jun, who grumbles but reaches for his notebook. Practical steps. The list grows, and with every tick you feel the future becoming an organized thing you can actually build."

    # --- merge ---
    "Continue"
    # [Scene: Harbor — Test Run Day | Midday]
    hide ravi_riv_delgado
    hide elias_maren
    hide mika_hoshino

    scene bg ch4_453e40_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The measured count of the team leader; a rising whoosh as a controlled swell passes through the corridor.]
    # play music "music_placeholder"  # [Music: Triumphant but understated brass; hope tempered by craft.]
    "You stand by the edge as the test begins. The choreography of deployment has an almost religious focus: everyone knows their cue. The wave arrives—deliberate, measured—and the monitors record. For a breath, you hold your own."
    "Elias Maren: (two-way radio clipped to his jacket) 'Readings on buoy three… now.'"
    "A green series of numbers scrolls across the screen. The graph dips; the amplitude is lower where the kelp canopy has taken hold. A cheer bubbles up, careful at first, then more confident as the data repeats across subsequent passes."
    "Jun: (quiet laugh) 'I'll eat my hat if that isn't the proudest planking I've ever laid.'"
    "Riv: (clapping you on the back) 'You did that, Mika. You did that.'"
    "Mayor Amina: (checking her tablet) 'If these averages hold over the next cycle, I will release the first tranche of funding. Consider this a municipal handshake.'"
    "Elias Maren turns to you, eyes bright. The sea-air has left salt on his cheek, and the shape of his smile seems to fit better in this place than it did a week ago."
    show elias_maren at left:
        zoom 0.7

    elias_maren "We did it. Together."
    "Mika Hoshino: (your voice steadier than you feel) 'We did. This—this is what I wanted. Not just to patch holes, but to build something that can be kept by the people who live here.'"
    "The data has its own music — numbers resolving into possibility. Around you, the town exhales as if relief were a physical thing."
    hide elias_maren

    scene bg ch4_453e40_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A soft notification chime; the harbor seems to brighten.]
    "You press your palm to the notification like a benediction. The grant is a tool and not a solution, but it is real. Your chest is full, not just from victory but from the recognition that"
    "the work you chose — joining hands with Elias Maren, with Jun, with Riv, with Amina — is changing the town's trajectory."
    "Elias Maren: (quiet, close) 'You trusted me with your workshop. You trusted the project. Thank you.'"
    show mika_hoshino at left:
        zoom 0.7

    mika_hoshino "I trusted you because you made it sensible. Because you made it something people could do, not just hope for."
    "He looks at you then, and there is a softness there that is not naive; it is steady and earned. It makes the future look like a small, constructible thing rather than a distant storm."
    # [Page-Turn Thought: The kelp forest on the monitor sways as if breathing. For the first time in a long while, you imagine Atera pulling itself less by panic and more by practice. You can already see the next work list — more anchors, community workshops, audits — but that orderliness feels less like constraint and more like the scaffolding of care. You wrap your fingers around a rope and feel, with clarity, that you are not alone in holding it.]
    hide mika_hoshino

    scene bg ch4_453e40_9 at full_bg
    # play music "music_placeholder"  # [Music: Gentle swell of strings, hopeful and steady.]

    scene bg ch4_453e40_10 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
