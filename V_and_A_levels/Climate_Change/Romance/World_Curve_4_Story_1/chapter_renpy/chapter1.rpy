label chapter1:

    # [Scene: Lira Bay Harbor | Late Afternoon]

    scene bg ch1_Start_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, coastal ambient—distant gulls, soft synth pads]
    # play sound "sfx_placeholder"  # [Sound: Wooden planks creak, a buoy knocking rhythmically, distant engine hum]
    "You step down from the bus with your bag slung across one shoulder and your Moleskine damp and warm under your hand. The boardwalk smells like old rope and seaweed—salt and a faint diesel tang that"
    "folds into the memory of countless summers. Your jacket is still stiff with mud where you kneel in sample plots; the elbows bear the stitches you made on the ferry two days ago. The air holds"
    "that peculiar heaviness that comes before rain, but the light is golden, forgiving."
    "You look out across the flats. The marsh channels are different than in the photos you kept on your phone—narrowed in places, opened in others, silt drawn into odd barbs like a script you almost understand."
    "At low tide the channels map the bones of the bay; they tell stories of where water ran and where it didn't. You press your thumb to the leather cover of your Moleskine and feel the"
    "pulse of a familiar urgency—that same quiet tug that made you leave grad lectures for tidal mud and late-night lab runs."
    "You inventory the obvious: tide is low enough for wrack sampling at first light, the south spur has silted toward the western reeds, and the old marker buoy by Dock 4 lists at a shallower angle."
    "Less obvious: the lane of boats is tighter than you remember; some pylons are newly reinforced. People adjust before thinking they have to — you see that even here."
    # [Scene: Pier | Late Afternoon]

    scene bg ch1_Start_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rita humming under her breath, a gull calling near the lantern house]
    # play music "music_placeholder"  # [Music: Soft acoustic strum]
    show rita_soler at left:
        zoom 0.7

    rita_soler "You finally came back, niña."
    "You let your shoulders drop in a way you didn't realize you were holding them. Rita's voice is a small knot of warmth and reproach. She hasn't changed—small frame, hands like dried sea fans—but the way"
    "she stands against the wind makes it clear she has been holding ground for everyone."
    show maya_soler at right:
        zoom 0.7

    maya_soler "I had to. The grant paperwork took forever, but it wasn't the papers I worried about.' (You rub the mud from your sleeve.) 'I wanted to see the flats before the next tide."

    rita_soler "Good. They need your eyes. And so do I.' (She studies your jacket, then your face.) 'How's the city treating you? Too many suits talking about numbers and forgetting what the bay sounds like?"
    "You consider the rightness of that answer. Evelyn Hart had been mentioned in emails—polished proposals, feasibility studies—but Rita's question threads to something older than policy talk: practical memory. You remember the house on the hill that"
    "used to fold around family dinners when storms came in; you remember how it felt to be small and helpless on the porch."

    maya_soler "The city has good maps. They don't have the tides that hit midnight kids. They don't have Rita's memory.' (You try to make it light; it lands as a soft confession.) 'I missed the sound of these pilings."

    rita_soler "You missed it, eh? Then you'll know what to do.' (Her smile is brief, knowing.) 'But don't be soft with them. They like to dress urgency as inevitability."

    maya_soler "And you? How's home—your garden, the roof—"

    rita_soler "I've got the gutter patched. And I've been keeping an ear on Arin. He was down near the lantern house this morning. He couldn't stop fussing over his nets."
    "Rita's look toward the pier carries a weight you both understand. People here move in patterns neither of you invented but both must respect."

    menu:
        "Approach Rita for a hug":
            "You let yourself fold forward into her arms. The scarf smells like sun-washed cotton and rosemary; the world simplifies for a heartbeat."
        "Keep a careful distance and clasp her forearms":
            "You grasp her forearms, checking her face for worry. The contact is practical; it steadies both of you."

    menu:
        "Ask Arin about his family's concerns directly":
            "You push gently. He lists names and times, and the specifics come out in a long, practical breath—schedules, nets, money—proof that this is about survival, not stubbornness."
        "Offer to show Arin some initial data instead":
            "You flip open your Moleskine and trace the tide lines. He watches the pen, curiosity softening his features; for a moment, the scientist in you and the fisher in him speak the same language."

    menu:
        "Check the logger's raw data now":
            "You pull up the raw feed; the numbers make a soft, ordered shape across the screen. There's a subtle shift in sediment transport two months ago—you flag it in the Moleskine."
        "Note the discrepancy in your Moleskine for later and keep mending":
            "You jot a short line: 'check sediment anomaly—Feb.' You fold the paper in and finish the elbow. It's practical, paced."

    jump chapter2
    return
