label chapter1:

    # [Scene: Harborfront Research Lab (The Tidehouse) | Morning]

    scene bg ch1_Start_1 at full_bg
    # play music "music_placeholder"  # [Music: Soft, hopeful synth with distant ocean swell]
    # play sound "sfx_placeholder"  # [Sound: Low gull calls, quiet drip of water against hull]
    "You wake to the soft creak of the Tidehouse settling into another tide. Light comes through the glass like diluted tea—cool and patient. Your wristband vibrates: a morning sync with the boathouse sensors, a small green"
    "LED that says nothing so loudly as 'things are still measuring.' You run a thumb over the worn leather notebook at your hip; tide charts, a doodled plan for a reed barrier, a child's watercolor of"
    "the Old Pier you keep because the memory still fits in your palm."
    "The air smells of brine and warm paper. Your jacket is still damp where you tucked it over a chair last night. You move through the cluttered lab—hanging jars with labelled samples, salt crystallized along jar"
    "rims, a whiteboard crowded with tentative sketches—and feel the small, steady rhythm of the place. This is where data becomes argument becomes hope."
    "You cross to the bench and pull up yesterday's logs: sediment trap readings, turbidity curves, the little blip from the experimental reed bed you seeded three weeks ago. The numbers are not miraculous, but they are coherent; they point the same way."
    "Samir appears from the back room with his tablet held like an offering, hair still tossed from sleep. He smells faintly of coffee and solvent—he always smells of 'work in progress.'"
    show samir_hale at left:
        zoom 0.7

    samir_hale "Morning. You have to see this—turbidity down twenty percent at Site C during the last storm window. The traps show net accretion instead of loss."
    show mira_solace at right:
        zoom 0.7

    mira_solace "Twenty percent?' (You lean in over his shoulder, scanning the graph.) 'That's better than the models projected for a first flush. Are the sensors calibrated? Did you run the cross-check?"

    samir_hale "Triple redundancy. We swapped the passive loggers with the new housings last week. No drift. The reed shoots are—' He gestures, searching for the word. '—establishing. Root mass picking up. It's small, but it's not noise."

    mira_solace "Small is what we need. Small that keeps happening."

    samir_hale "If this keeps, the projections for shoreline microloss change for the next five years. It's not a wall, but it's a footprint—socially cheap, ecologically sensible."
    "You: (internal) Something in you eases—an anatomical unknotting that has nothing to do with charts. You remember the last time a number like this appeared: a grant that fell through, a promise washed away. But this"
    "is different. The data is patient; it doesn't flash. It waits for you to notice."
    hide samir_hale
    hide mira_solace

    scene bg ch1_Start_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft beep of a data upload]
    "Samir hands you the tablet. The graph gleams in the Tidehouse light: a definite slope. Your fingers remember the measurements you took by hand, the mud between your nails, Noah's stubborn grin when he said the"
    "patches looked greener. This moment is small and bright—like the first green that pushes through winter soil."

    menu:
        "Make the kettle and bring everyone a cup":
            "You set the kettle on the tiny stove. The hiss of boiling water rounds the room into something more domestic; when Samir returns with two chipped mugs, conversation softens and ideas trade like shared warmth."
        "Step outside to check the reed beds yourself":
            "You pull on boots and step into the salt-bright morning. The reeds scrape your palms; mud gives under your soles. The sensors flash against the wet stems—real, anchored, stubborn as anyone who's stayed. When you return, your coat smells of green water and the conversation has a new edge."

    # --- merge ---
    "The scene continues with the Tidehouse mood sharpening into momentum."
    "You choose, but whichever small impulse you follow, the mood at the Tidehouse sharpens into momentum. Samir rallies a sequence of verbal plans—data briefs, neighborhood meetings, a short note to the municipal archives—and you answer, threading"
    "method through his enthusiasm. The language isn't romance or rhetoric; it is the slow, steady talk of people who know how to build things that outlast storms."
    # [Scene: Tidehouse Boathouse Exterior | Morning]

    scene bg ch1_Start_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Steps on wet wood, a distant motorboat cough, muffled voices from the causeway]
    "Etta arrives with the weight of years in her shoulders and a basket of jars wrapped in sea-blue cloth. Her braid is crownlike, salt-silver, and she moves with a sure, easy authority—someone who has watched the harbor change and learned to read its moods."
    show etta_maren at left:
        zoom 0.7

    etta_maren "Mira. The folks by Pier 7 dropped samples. They say the algae bloom eased after you moved the oyster trays. 'Better water,' one of them said. Simple words, but she's smiling."
    show mira_solace at right:
        zoom 0.7

    mira_solace "We need the lab reads for confirmation, but if local observations match the sensors—"

    etta_maren "People notice when the water remembers its own life. They feel it in the way nets don't tear so often, how kids climb the jetties again.' (She inclines her head.) 'You did that. You all did."
    "Arin Voss arrives while you're still sorting through the jars, wind in his hair and a camera slung across his chest. He smells of salt, paint, and the diesel of a borrowed van. His grin widens when he sees you."
    show arin_voss at center:
        zoom 0.7

    arin_voss "I took photos at the rooftop pilot last evening—look at the root spreads. We had five neighbors plant—old Mrs. Kade from third floor even brought seeds. People were laughing. The footage is good. We can show it."

    mira_solace "Neighbors at the rooftop—good. The question is scale. Photographs are persuasive, but Samir's numbers will persuade differently."
    hide etta_maren
    show samir_hale at left:
        zoom 0.7

    samir_hale "Both. Visuals get attention; the numbers make the mayor's office listen. If Arin's footage pairs with the accretion curves, we can ask for a modest pilot expansion. Low cost, low disruption."

    arin_voss "Then let's do a public planting. Rally people. Make it festive. Make it visible."

    mira_solace "Public is fine, but we need controls. If we scale without monitoring, we lose causality. We'll need sensor deployment, volunteer training, clear maintenance schedules."

    arin_voss "Okay. Sensors. Training. You plan the monitoring; I'll organize the street-level push."
    "You: (internal) There it is—the compromise that tastes like a first true step. Your hands, for a moment, hover over your notebook. It feels right: method and madness braided together."
    "Etta watches you both with a watery smile. The harbor has room for both your kinds. She offers a small, conspiratorial cluck."
    hide mira_solace
    show etta_maren at right:
        zoom 0.7

    etta_maren "Make it a thing of care. People will come if it's for their children, their boats, their memories."
    hide arin_voss
    show mira_solace at center:
        zoom 0.7

    mira_solace "We start small, show results, then scale. We keep the records transparent. We teach maintenance as part of the ritual."
    hide samir_hale
    show arin_voss at left:
        zoom 0.7

    arin_voss "Teach and party afterwards. I can make a film of the teach-and-party."

    menu:
        "Agree to Arin's public planting with the monitoring plan":
            "You nod. The plan lands like a pebble in water; ripples of plans and responsibilities circle outward. Arin clamps a hand on your shoulder, grin wide, and Etta hums approval. The schedule forms between you: sensors, volunteers, a banner design."
        "Insist on doing a quiet controlled expansion first":
            "You fold your arms around the lab's instruments. 'Controlled' you say, and Samir nods, relieved at the caution. Arin looks disappointed—then practical—already adjusting his enthusiasm to fit your careful frame. The mood shifts to deliberate preparation."

    # --- merge ---
    "The group coalesces around a shared plan; preparations begin."
    "You take in their faces—Samir precise, Etta patient, Arin incandescent—and you realize the room contains more than data. It holds people who have been waiting for permission to act. Momentum is not a sudden tide but"
    "a collection of gestures: a camera shutter, a jar handed to a neighbor, a sensor clipped into mud."
    # [Scene: Rooftop Common Garden | Late Morning]
    hide etta_maren
    hide mira_solace
    hide arin_voss

    scene bg ch1_Start_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Bees, the soft rustle of leaves, distant city hum softened by growth]
    # [Smell: Earth warmed by sun, citrus from a potted shrub]
    "You climb the narrow stair to the rooftop garden with Samir and Arin trailing—Samir with a small case of instruments, Arin with the camera clicking quietly. The garden's air is thicker, warmer, full of green perfume."
    "It is astonishing how quickly plant life paints over the city's edges when given a few square meters."
    "You kneel at the planting edge, fingers in the soil. The sensor pad under your palm hums and then resolves into numbers on your wristband. Moisture stable, root conductivity up, microclimate slightly cooler than the adjacent concrete. A little ecosystem on a rooftop doing the work you need."
    show mira_solace at left:
        zoom 0.7

    mira_solace "It's holding."
    show arin_voss at right:
        zoom 0.7

    arin_voss "It feels held."
    show samir_hale at center:
        zoom 0.7

    samir_hale "The records look clean. If we can standardize deployment—modular planters, a toolkit for neighbors—we can replicate this across mid-rise roofs."

    mira_solace "If we standardize and teach maintenance, we don't just retrofit buildings; we build civic skills."
    "Etta's voice arrives through the stairwell—she has accompanied a neighbor up, offering tea in a thermos, an old habit of making people sit and tell their stories."
    hide mira_solace
    show etta_maren at left:
        zoom 0.7

    etta_maren "There was a boy here last night who said he could hear the soil breathe. Young ones notice things we teach ourselves not to."
    hide arin_voss
    show mira_solace at right:
        zoom 0.7

    mira_solace "Then we teach them to care for the breathing. We make knowledge contagious in a good way."
    "You look at your team: Samir's cautious optimism, Arin's fervent warmth, Etta's steady patience. There is a thread—data, community, and ritual—that ties them. You feel the first real tug of momentum: not a policy victory or a headline, but the sensation that something replicable has begun. It could spread."

    samir_hale "We should present this at the neighborhood assembly. The numbers plus a few photos and a practical rollout plan—"
    hide samir_hale
    show arin_voss at center:
        zoom 0.7

    arin_voss "And make it a happening. We'll bring drums, and seed packets, and show the footage from last night. Etta can open with a blessing."

    mira_solace "Or we take it directly to the Old Pier community—people whose livelihoods are at stake. Start where the shore still remembers its old geometry."

    etta_maren "The pier listens. Bring the story there first."
    "You feel the decision forming like a tide: convene, present, expand. The idea is humane and straightforward. It is also dangerous in its optimism—public attention could draw Liora Kade's kind of solution, which would scuttle grassroots work for big contracts. But caution tastes sweeter when it's paired with preparation."
    "You breathe in the warm, plant-sweet air and taste possibility. The Tidehouse hums behind you, a small engine of commitment. The rooftop garden rustles like a chorus."
    hide etta_maren
    show samir_hale at left:
        zoom 0.7

    samir_hale "If we want to convene, we should make a concise brief—what we did, why it matters, what we need volunteers to do. I'll draft it."

    arin_voss "I'll film, I'll make flyers, I'll talk to the market people on the causeway. Make it celebratory—people come for warmth."
    hide mira_solace
    show etta_maren at right:
        zoom 0.7

    etta_maren "You lead the facts, Mira. You make the machines be kind. We'll bring the people."
    "You look at the harbor horizon where the sky and water meet in a seam of slate and light. This morning feels like the beginning of something that won't solve the city overnight, but might change enough edges to matter."
    "You stand, palms brushed with soil, and feel, plainly, that you are not alone in wanting to save the place you remember. The data sits in your band, the community sits in Etta's wrinkled hands, hope sits in Arin's camera flash. Momentum—gentle, cumulative—has tilted toward action."
    "You know the next step: gather the neighbors where their memories still cling to the boards and ropes of the Old Pier and show them what small care can do. The idea settles into you like a plan should—clear, urgent, possible."
    hide arin_voss
    hide samir_hale
    hide etta_maren

    scene bg ch1_Start_5 at full_bg
    # play music "music_placeholder"  # [Music: Swells slightly, then softens into expectant silence]
    "You breathe. You gather your things. Outside, the harbor light sharpens."
    # [Page-Turn Moment]
    "You step toward the stairwell as voices shuffle and plans begin to form. On the landing you pause, listening to the garden's small noises—the promise of replication—and you feel the harbor tilt with you. The Old Pier waits like a memory that could be taught to keep living."

    scene bg ch1_Start_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter2
    return
