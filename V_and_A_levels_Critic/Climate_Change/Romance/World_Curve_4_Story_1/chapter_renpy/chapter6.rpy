label chapter6:

    # [Scene: Saltwren Commons | Night — Storm Approaching]
    # play music "music_placeholder"  # [Music: Low, thrumming percussion building into urgent, dissonant strings]
    # play sound "sfx_placeholder"  # [Sound: Distant thunder; gulls silenced by wind; rope creaking]

    scene bg ch6_4001e7_1 at full_bg
    "You taste metal and rain on your tongue before the first wall of water arrives — an animal, sudden and enormous. The Commons, everything you have coaxed back from dereliction, smells of wet earth and rotting"
    "leaves. Your fingers are cold through the gloves shoved into your back pocket; the copper bracelet at your wrist feels slick with condensation."
    "Tommy is already down on the lower boardwalk, shouting over the wind as he knots a line to a driftwood post. His voice is ragged and practical: no drama, just the work that comes when things"
    "break. Rae is hauling crates of seedlings into the highest shed she can reach, moving like a frantic, small hurricane."
    "You look for Elias Navarro. He is there — jacket soaked at the shoulders, tablet clasped under one arm, jaw tight. He keeps his eyes on the sea and then on you, the way he does"
    "when the world is a problem to be solved. Tonight the problem smells of salt and sour fear."
    show elias_navarro at left:
        zoom 0.7

    elias_navarro "We have to pull the pumps forward. If the tide surges past the northern berm it will cut the boardwalk in two. Dr. Bhatt's sensors just spiked—"
    show mara_lin at right:
        zoom 0.7

    mara_lin "The berm's hold or the pump's range—what saves the houses further inland?"

    elias_navarro "Both, ideally. But the berm's compromised. We can divert power to the emergency pumps and—"

    mara_lin "Divert power from the Tidewatch feed?' (Your voice is small, brittle with calculation.) 'That leaves half the monitoring blind."
    "Elias Navarro's mouth tightens in that measured way; he wants the answer to be a plan you can nod at. He wants to believe the map will do the comforting."

    elias_navarro "Just for the night. We have to triage. Save where human life is at immediate risk."
    "Your chest throbs with the memory of your sibling's last night — the sense of a lull then a sudden, smooth taking. You breathe, the decision a hot stone in your palms."

    menu:
        "Stay here to shore the Commons":
            "You plant your feet and start tightening the makeshift sluices, ordering volunteers, stacking the last sandbags. The boardwalk groans but holds a little longer."
        "Go with Elias toward the Promenade":
            "You follow Elias into the gale. He doesn't take your hand; his pace is all urgent motions and clipped directions, but his shoulder brushes yours once, and then he's gone into the swell."

    # --- merge ---
    "Continue to the Promenade / next scene"
    # [Scene: Promenade / Construction Site | Night — Gale]
    # play music "music_placeholder"  # [Music: Staccato brass with crashing cymbals; heartbeat-like drum]
    # play sound "sfx_placeholder"  # [Sound: Steel clanking; distant alarms; the ocean striking concrete with a relentless percussion]
    hide elias_navarro
    hide mara_lin

    scene bg ch6_4001e7_2 at full_bg
    "The Promenade smells of machinery and diesel. The corporate banners you once hated now whip into tatters. There are survey stakes with their neat geometry, now meaningless against the shove of living sea. You run, ankle-deep"
    "in cold water, alongside Elias Navarro and a wedge of volunteers. You watch engineers tie rebar into a desperate lattice with hands that tremble; you listen to Celeste Park's voice on the phone somewhere, even as"
    "you can’t make out the words — the unmistakable, calm cadence of someone who believes things can be ordered into safety."

    "Tommy appears at your elbow, eyes wide where the street dips and the water has already claimed curb and mailbox. He spits salt and says a single cruel thing you know to be true" "It's faster than we thought."
    "Elias Navarro is barking orders into a radio. He toggles the tablet, then compresses his jaw and turns to you."
    show elias_navarro at left:
        zoom 0.7

    elias_navarro "We can seal the breach here temporarily with the inflatable barriers. It's not elegant, but—"
    show mara_lin at right:
        zoom 0.7

    mara_lin "Temporarily for whom? For the tourists who will come next summer? For the boardwalk vendors?"
    "He flinches, because you are aiming at something larger than an engineering choice. You are aiming at a fracture you didn't want to make explicit."

    elias_navarro "For people sleeping in the alphabet of time zones inland, Mara. For families."
    "You answer with the kind of quiet that is not resignation but a blown fuse."

    mara_lin "We built the Commons to be a buffer. We fought to keep living shoreline, not to trade it for a wall you can paper over."
    "The tide answers you both by spitting a new wave onto the scaffolding. A length of wooden railing snaps, sending a spray like silver glass into faces and coats. Someone screams — a high, animal sound — and the world narrows to movement and rescue."
    # [Scene: Promenade / Breach Point | Night — Crisis]
    # play sound "sfx_placeholder"  # [Sound: A sustained, horrific cracking as concrete gives way; floodwater roaring like an animal]
    hide elias_navarro
    hide mara_lin

    scene bg ch6_4001e7_3 at full_bg
    "The sea finds the seam. Where the promenade used to be a line of hopeful lights and plans, there is now a jagged mouth of black water slurping at the earth. The breach is fast, efficient,"
    "implacable. You watch a vendor's van roll, half-floating, the driver's silhouette slumped. A child's tricycle flashes in the murk."
    "Dr. Amina Bhatt arrives with a weathered instrument case and the expression of someone who has catalogued many failures. She moves through the chaos with a surgeon's economy but her hands tremble when she helps lift a soaked person onto a makeshift stretcher."
    show dr_amina_bhatt at left:
        zoom 0.7

    dr_amina_bhatt "Get the evac teams north. Close the low-lying stairwells. We need to prioritize human life and then—"
    "Rae yells that the Commons warning siren hasn't been heard in the lower terraces; the wiring must have been chewed when the promenade went. You run, the push of water at your calves, the cold clawing"
    "up your legs. The Commons, your gardens, the boxes of seedlings you nurtured — they are slipping away in green-and-brown clumps."

    menu:
        "Shout orders to the evac teams":
            "You scream until your throat rasps, directing people along paths you know by memory. Someone follows. A neighbor with a lantern takes an old woman by the elbow. You feel the work steady you for a moment."
        "Go straight to the breached boardwalk to find the van's driver":
            "You run to the gaping maw and peer into black water. You are struck by how small and human the things in the water are: a blue sneaker, a child's stuffed fish. You find the driver's hand and grip it; for a second it meets yours and is warm and then a wave pulls it away."

    # --- merge ---
    "Continue to Tidewatch Lab / next scene"
    # [Scene: Tidewatch Lab | Night — Emergency Response]
    # play music "music_placeholder"  # [Music: High, relentless synthetic pulses intercut with sirens]
    # play sound "sfx_placeholder"  # [Sound: Monitors beeping; rain pelting glass; the faint, threatening creak of the building bending]
    hide dr_amina_bhatt

    scene bg ch6_4001e7_4 at full_bg
    "You and Elias Navarro get to the Tidewatch Lab because that is where the grid can be controlled and where Dr. Amina can triangulate floods and set priorities. The lab smells of tea and wet paper;"
    "there is a thin blue light from instruments that map the town as if it were anatomy."
    show elias_navarro at left:
        zoom 0.7

    elias_navarro "If I reroute the pumps to the east network, the terraces by Old Mill will get a fighting chance. But it will lower pressure on the Commons systems."
    show mara_lin at right:
        zoom 0.7

    mara_lin "You can measure outcomes, Elias. I know what the numbers say. It's not the numbers I trusted you with — it was the people you promised to count."
    "He looks at you then, like someone trying to balance a number of tiny, impossible weights."

    elias_navarro "I counted them. I counted you. I—"
    "Dr. Amina Bhatt kneels to reattach a cable. She is the slow center in a spinning disaster."
    show dr_amina_bhatt at center:
        zoom 0.7

    dr_amina_bhatt "We move where we can save lives first. The rest we document and plan for recovery. That is the only framework that won't get people killed."

    mara_lin "And when we lose whole neighborhoods to your framework, who rebuilds the soul of the place? Who stitches the grief?"
    "Her gaze is heavy, unreadable. She wipes a hand on her sleeve and says nothing. Her silence is a ledger."
    # [Scene: Old Mill Rooftop | Night — Rescue & Confrontation]
    # play music "music_placeholder"  # [Music: A single violin line shuddering under thunder; then silence and wind]
    # play sound "sfx_placeholder"  # [Sound: Sirens distant; someone screaming a name; the raw sound of people clinging to ledges]
    hide elias_navarro
    hide mara_lin
    hide dr_amina_bhatt

    scene bg ch6_4001e7_5 at full_bg
    "The rooftop is cold and raw. The town looks like a map someone has scribbled over in panic: lights out, streets gone, dark puddles where habit used to be. You find a group by the mill's"
    "chimney — a family huddled under a tarpaulin, Tommy holding a child whose eyelids are crusted with salt."
    show mara_lin at left:
        zoom 0.7

    mara_lin "We have the emergency shelter at the school. Move now."
    show tomas_tommy_reyes at right:
        zoom 0.7

    tomas_tommy_reyes "They're on the other side. The bridge's gone. You know it, Mara."
    "You swallow the sound you want to make into a more useful thing: orders, an idea, a plan. But the plan is blown away. There is only the immediate, human need."
    "Elias Navarro appears at the ladder like a figure breaking through rain. He looks exhausted, the lines at his mouth deep. You are furious in a way that makes your fingers ache."

    mara_lin "You diverted the pumps."
    "He replies before his sentence is finished, as if to forestall your accusation with the bluntness of truth."
    show elias_navarro at center:
        zoom 0.7

    elias_navarro "I diverted them to protect the Old Mill ridge. If we hadn't, the school would have flooded. Children would—"

    mara_lin "But the Commons—"
    "He reaches for you and you jerk back. This is not the moment for hands; it's the moment for naming what must be named: betrayal, necessity, the collision of two loves — for place and for people — crumpling in the press of water."

    elias_navarro "I made a call. I thought — I thought I was doing the right thing."

    mara_lin "Thought is not the same as listening."
    "He closes his eyes. The rain traces tracks through the dirt on his cheek like tributaries."

    elias_navarro "I didn't think it would take the Commons."

    mara_lin "You didn't think about the Commons at all."
    "There is a silence so heavy it is almost physical: the wind seems to respect it. Then the sky breaks over the town like a final verdict. For a dizzy, furious second, you could imagine turning"
    "away forever — taking the Commons and the gardens and all the small, stubborn things that matter and walking until no one could drag you back."
    "But people are still calling for help. Someone is trapped under a collapsed porch in a low-lying lane. You can hear them speaking names, breathing. The rawness of human voice slices through your private ruin."

    elias_navarro "Help me find them—please. Mara, please."
    "You look at him; the man you kissed on the rooftop months ago and the man who will have to answer for decisions that broke your town. Everything inside you is a razor: the urge to"
    "lash, the urge to save, the urge to refuse to be the one who patches what his choices undid."

    menu:
        "Work with Elias to dig people out":
            "You shoulder down the anger and hand him a pry-bar. Together you pry up sodden floorboards and lift screaming timber. For a few brutal minutes the world narrows to muscle and air and the faint, miraculous croak of life."
        "Refuse and lead a separate rescue to other parts":
            "You step away and call a line of volunteers. You organize a flank, pulling people to shore, hauling blankets and small children into lit, dry arms. The work is clean; it is furious. It keeps your hands busy while your mouth stays a locked fist."

    # --- merge ---
    "Continue to Dawn / aftermath scene"
    # [Scene: Low-Lying Neighborhoods | Dawn — Aftermath]
    # play music "music_placeholder"  # [Music: Sparse piano notes; a low horn moaning under it; a slow, desolate harmony]
    # play sound "sfx_placeholder"  # [Sound: The distant, methodical murmur of generators; people talking in small, stunned clusters; gulls beginning to assert themselves again]
    hide mara_lin
    hide tomas_tommy_reyes
    hide elias_navarro

    scene bg ch6_4001e7_6 at full_bg
    "Dawn finds the town hollowed and exhausted. The town hall is a hub of paper and temper. People sit with wet clothes and broken things and talk in the soft, fraying tones of those who survived. There are too many wet chairs and too few beds."
    "You walk the Commons and count ruin like a litany: raised beds sheared, plants floating like small grieving things, the boardwalk collapsed into a dark cut. The compost piles run like small brown rivers. The copper bracelet at your wrist feels too small."

    "Tommy stands with a thermos, looking older than you remember. He says nothing for a long time, then manages" "We've lost homes. We've lost a stretch of what made this place ours."
    "You want to tell him about the nights of planting by hand, the stolen hours, the stubbornness that built green things out of ruin. Instead you find your voice a raw thing."
    show mara_lin at left:
        zoom 0.7

    mara_lin "We knew this could happen. We warned them. We tried to build with the tide, not against it."
    "Elias Navarro comes up behind you; there is a new hollow to him, a man reshaped by decisions that cut through more than wood. He holds a small stack of photographs that have been showing up at the shelter — images of the town from before, bright and ordinary."
    show elias_navarro at right:
        zoom 0.7

    elias_navarro "I routed the pumps so the school didn't flood. I thought—' (The sentence will be the same as last night, but repetition has weight.) 'We saved a lot of people because of that choice."

    mara_lin "And at what cost?"
    "He meets your eyes, and for the first time since the storm, his face is not composed of plans but of a person who has been wtorn by making hard calls."

    elias_navarro "I thought I'd be able to do both. For a while I believed it."

    mara_lin "Belief doesn't rebuild the houses, Elias. It doesn't replace the trees, or the soil we've turned for years. It doesn't undo what we've already lost."
    "His hands curl into fists around the photographs. For a moment he looks at them like a talisman, then folds them into himself."

    elias_navarro "I'm sorry,"
    "You want more than an apology. You want accountability, a recognition of the way choices shape people and places in ways that last. A small part of you — the stubborn, organizing part — wants to"
    "get back to work. Another part sits very coldly with the possibility that your partnership can't survive the arithmetic of triage."
    "Celeste Park arrives with a cluster of aides and a polished, flat expression. She moves through the shelter like an emissary from a world that makes sense because it's been ordered. She lays a plan on the council table about reconstruction and funding. Her words are calm, steel-gray light."
    show celeste_park at center:
        zoom 0.7

    celeste_park "We can rebuild in phases. A seawall, commercial space to bring revenue, and a managed boardwalk. It is a rational, fundable plan."
    "You watch people listen, count noses, measure need. There is a sound in the room like teeth grinding: the town evaluating tradeoffs like a budgetary calculus for grief."
    "Dr. Amina Bhatt stands near a window, staring at the debris field that used to be a marsh. She says nothing, and when she does speak it is not in defense of models or promises."
    hide mara_lin
    show dr_amina_bhatt at left:
        zoom 0.7

    dr_amina_bhatt "We will document and adapt. We will press for relocation where it's necessary. But we must also be honest about the limits of what we can save."
    "You realize, in a cold and terrible clarity, that the fight you thought you were in — for soil, for seedlings, for the shape of a promenade — is also a ledger. The ledger will be filled in by hands you cannot fully guess."
    # [Scene: Commons Edge | Mid-Morning — Quiet Before the Next Storm]
    # play music "music_placeholder"  # [Music: A single, sustained cello note; the fabric of the day thin and fragile]
    # play sound "sfx_placeholder"  # [Sound: A distant foghorn; drip of water from tarps; low voices forming threads of rumor and plans]
    hide elias_navarro
    hide celeste_park
    hide dr_amina_bhatt

    scene bg ch6_4001e7_7 at full_bg
    "Elias Navarro kneels beside you. He does not reach for your hand. The space between you is a geography you both have to cross."
    show elias_navarro at left:
        zoom 0.7

    elias_navarro "I thought I could save both the school and the Commons. I thought I could be clever enough."
    show mara_lin at right:
        zoom 0.7

    mara_lin "We both thought a lot of things.' (You turn your mud-streaked palm toward him.) 'We thought we could make something that wouldn't be tested."
    "He swallows. When he speaks, it is the same patient cadence he uses when explaining a failing model, but there is a tremor beneath it."

    elias_navarro "I didn't want to put you in a position where you'd have to forgive me."
    "You look at him then with all the things you have been carrying — the loss, the fury, the small, quiet reflex of love that is stubborn and dangerous."

    mara_lin "Forgiveness is not a thing you hand out like a permit, Elias. It's work. And right now I have to do more than forgive. I have to decide whether I can trust you with people's lives and the things they love."
    "He closes his eyes like someone bracing himself against an incoming wave."

    elias_navarro "If there's a way to rebuild that includes the Commons — not as ornament but as backbone — I will fight for it. I don't want to lose what we built."
    "You let the words sit. They are not enough, but they are not nothing."
    "Tommy approaches, and for a moment the three of you are the town's thinned skeleton — people who have been up all night and want a map to the next actions. He looks at Elias Navarro, then at you."
    show tomas_tommy_reyes at center:
        zoom 0.7

    tomas_tommy_reyes "We need people who make hard calls. We need people who can get things done. But we also need folks who remember why we're doing it."
    "The plainness of it slams into the space between you. You think of your sibling again, of seasons you planted for that person you buried in mud and salt. You feel grief like a patient claw."
    "Celeste Park clears her throat, and everyone turns. She is about to speak about rebuilding, about investments and timelines. Her plan is crisp, and when she speaks, the room leans forward like a body hoping for a cure."
    "You look around the shelter at faces: some are burning with righteous anger, others hollowed by exhaustion. Children play with damp paper. There is a woman mending a child's sweater, a man who lost his boat sitting very still."
    "You find that your certainty is gone in the cleanest way. There is no single enemy; there is a thousand small tragedies folded into policy and weather and human error."
    "Elias Navarro touches the sleeve of your jacket. The contact is tentative, like someone testing whether a broken bone will spark again. You do not pull away, but you do not lean in."

    mara_lin "I don't know if this is something I can bend around. Or if it's something that breaks me when bent."
    "He searches your face like a problem he can't solve on a screen. For a long, impossible second the two of you are a ledger of choices and faces and rain."

    elias_navarro "Then tell me what to do. I will try."

    mara_lin "You tried.' (The sentence is small and sharp.) 'But baby steps and triage are not promises. Not to a town that has already been battered."
    "He lets out a breath that sounds like guilt and sleep deprivation mixed. The sky beyond the broken boardwalk is a pale, frightened gray. There are clouds gathering again on the horizon, and the town moves"
    "like a tired animal ready to sleep but unable to forget how close the teeth still are."
    # [Scene: Commons — End of Morning]
    # play music "music_placeholder"  # [Music: A low, unresolved chord; wind under the sound of human voices]
    # play sound "sfx_placeholder"  # [Sound: Folding chairs scraping; the soft murmur of people forming new committees; distant hammering as boards are salvaged]
    hide elias_navarro
    hide mara_lin
    hide tomas_tommy_reyes

    scene bg ch6_4001e7_8 at full_bg
    "You stand up. Your legs ache but you can still walk. The Commons is a ruin you can name, and naming is a small kind of power."
    "You look at Elias Navarro. He looks back, and in his face you can read apology, fatigue, and a fragile hope that might not survive the next high tide."
    "You do not take his hand. You do not step away. You keep both feet in the mud."
    "The town will have to make decisions you cannot alone. Committees will grind. Celeste Park will have her plans. Dr. Amina Bhatt will advise, and Tommy will keep his watch. You will do the thing you always do: gather people, write lists, make shelter, plant where you can."
    "But something in your chest is very quiet, and you know the silence will not be filled by apologies alone."

    scene bg ch6_4001e7_9 at full_bg
    # play music "music_placeholder"  # [Music: A final, low sustained string — unresolved]

    scene bg ch6_4001e7_10 at full_bg
    "THE END"
    # [GAME END]
    return
