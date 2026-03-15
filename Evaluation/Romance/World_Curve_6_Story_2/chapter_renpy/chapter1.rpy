label chapter1:

    # [Scene: Highwater Cove | Dawn]
    # play sound "sfx_placeholder"  # [Sound: Distant sirens; gulls crying; a low generator hum]
    # play music "music_placeholder"  # [Music: Sparse piano with low strings — tense, brittle]
    "You wake to the vibration of a town that will not sleep. Sirens thread through the fog like needles: warning, warning. Salt and diesel sit thick in the air, a tang that settles on your tongue and drags your lungs into work before your eyes are fully open."
    "You fumble for the brass compass at your throat out of habit—fingers that know its dents better than the maps in your head. It is warm where it presses into your chest beneath your jacket, heavy"
    "with the memory of Nan, of promises. Rain has left pavement mirror-slick; the reflectivity turns the streetlights into a dozen small moons that wobble beneath your boots as you step outside."

    scene bg ch1_Start_1 at full_bg
    "You did not mean to fall asleep. There are notes taped to the inside of the door—Rafi's scrawl, a grocery list, a half-finished diagram for a pump—but the sirens made the choice for you. You draw"
    "the scarf over your mouth against the spray and step into the mirrored street. Every footstep sends up a soft squelch; the wet presses into the fabric of your boots like memory into bone."
    # [Scene: Highwater Cove Harbor | Dawn]
    # play sound "sfx_placeholder"  # [Sound: Boards creak underfoot; distant shouts; the slap of water against pilings]

    scene bg ch1_Start_2 at full_bg
    "As you wade toward the harbor—water lapping around the soles of your boots—you see the town's patchwork response already in motion. Neighbors form human chains to haul sandbags; someone bangs a drumbeat of shouted instructions. A"
    "generator coughs; its exhaust threads through the air and mixes with rotting kelp and frying salt."
    "Gracie 'Nan' Armitage sits on a low crate near the fishmarket, needle moving through bright quilts the color of stubborn flowers. Her hands are slow and sure, stitching warmth into squares that will line the school"
    "gym turned shelter. She looks up as you approach, and for a moment her lined face is a map of all the storms you've both weathered."

    "Gracie "Nan" Armitage" "Maya. You're up. Sit before the wind takes you whole."
    "You move closer, the compass tapping once against your sternum. Nan smells of lavender soap and the sea. Her eyes—small, sharp—take you in and hold you as if weighing whether your shoulders will buckle today."
    show maya_armitage at left:
        zoom 0.7

    maya_armitage "I can't. Tanks at the Institute—"

    "Gracie "Nan" Armitage" "The tanks will leak if you don't get there, and the quilts won't sew themselves while you debate. You promised the town anything you could do, child, not everything in the world."

    maya_armitage "I know. I just—"
    "you swallow the rest"

    maya_armitage "I woke to sirens and—"

    "Gracie "Nan" Armitage" "—and the town stares at you because it wants you to fix a tide. That isn't on your back alone, love. Not today.' (She taps her needle against her knee.) 'Bring me one of those sensors and I'll stitch the patrol schedules into the corner. Make the shelter know who's coming and leaving."
    "Her pragmatism is an anchor and a chisel. You feel gratitude and a bitter, familiar guilt at the same time; old promises ache like a tendon."

    menu:
        "Help Nan finish the quilts for the shelter.":
            "You sit, folding fabric into neat stacks. The rise and fall of the needle is hypnotic; for a few minutes you are not the town's savior, just a granddaughter keeping hands busy."
        "Head straight to the Tidal Institute to assess infrastructure damage.":
            "You stand, fingers curled around the compass, and pull away. Nan's eyes follow you. She doesn't stop you—she's always trusted you to choose the work that burns the brightest."

    menu:
        "Prioritize sealing the tank; delay preparing testimony.":
            "You strip off a glove and take the clamps. The cold metal bites. For now, saving the specimen feels like saving a fragment of the town's future."
        "Prepare the emergency testimony now; have Rafi secure the tank.":
            "You move to the tablet, fingers translating charts into sentences. Your words are careful, too clean for the panic in your chest."

    menu:
        "Close the distance; let Jonah see how worn you are.":
            "You close the short gap and let him track the exhaustion on your face. He doesn't say much—he wraps an arm briefly around your shoulders, the motion measuring out a kind solidarity."
        "Keep a professional distance; focus on the logistics for the council.":
            "You step back and pull your tablet from your pocket, words already forming. The space between you becomes a map: emotional line items on one side, triage on the other."

    jump chapter2
    return
