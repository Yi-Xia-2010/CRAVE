label chapter8:

    # [Scene: Kaito's Field Lab / Main Door | Dawn]
    # play music "music_placeholder"  # [Music: Low, minor strings; rain tapping a steady rhythm]

    scene bg ch8_6b08b4_1 at full_bg
    "You leave the lab with the notebook closed like a held breath. The rain smells of iron and seaweed—sharp and metallic on the tongue—so familiar it knits a bruise of memory across your chest. The lamp"
    "light falls wet on Kaito's knuckles as he buttons his coat; his sensor pendant blinks a steady, embarrassed green."
    show kaito_sato at left:
        zoom 0.7

    kaito_sato "You look like you haven't slept."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "I didn't, exactly.' (Your voice is smaller than you expect.) 'Did you—did you copy the last readouts?"

    kaito_sato "All here.' (He taps a tablet screen; graphs bloom, jagged and honest.) 'Salinity spikes at Station Three, fifteen minutes before the last sluff. The pattern matches the models—only denser than we thought."
    "He shows you—a smear of numbers that means erosion, that means cliffs softening like old bread. His fingers hover over the screen, then curl into his pockets. There's a quick, self-deprecating smile that doesn't reach his eyes."

    kaito_sato "If we put sensors at the headlands and near the mangrove stubs, we can get a lead time. Not perfect. But it gives Tomas and the crews a window."
    "You taste iron again. Your brother's watch on your wrist ticks on, slow and accusing, as if it could sew time back together. The lab's fluorescent hum seems to thicken the air."
    "You inhale. Outside, the market square is a darker pool beneath the rain, but it's where people still meet—where gossip, anger, grief, and hope get traded in equal measure."
    # [Scene: Harborfall Market Square | Morning]
    # play sound "sfx_placeholder"  # [Sound: Market calls muffled by rain; gulls distant; the slap of wet fabric]
    hide kaito_sato
    hide maya_inoue

    scene bg ch8_6b08b4_2 at full_bg
    "Tomas is already there, leaning on his cane, the gold in his beard a dull flame in the gray. Around him, three fishers you recognize—callused hands and old scarves—argue about nets like priestly disputes."
    show tomas_bianchi at left:
        zoom 0.7

    tomas_bianchi "They'll promise the moon and hand us a contract in fine print. Trust was our currency; they want to monetize it."
    "You move through the smell of fried dough and wet rope, your boots leaving dark prints on the boards. The fishers look up, and the lines around their mouths tell you everything you need to know—loss, calculation, suspicion."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "We have something that can warn you earlier. Not a wall—an early warning network. It won't be pretty. It won't be instantaneous. But it will give you minutes that could matter."

    "Old Fisher 1" "Minutes don't mend a boat, girl. They mend a decision."

    "Old Fisher 2" "And who pays for the minutes when Lux brings a wall with her name on it?"
    "Tomas watches you with soft, slow intensity. He doesn't move to argue; he waits for you to earn it."

    tomas_bianchi "Show them the numbers, Maya. Show them the thing that says tomorrow might be different."
    "Kaito Sato steps forward, breath steaming in the rain. He sets a small portable sensor on the table—brass and plastic, a humble thing—and the pendant at his chest blinks like a heartbeat."
    show kaito_sato at center:
        zoom 0.7

    kaito_sato "Watch.' (He gestures, and the sensor projects a transient readout into the air—salinity curves that wobble as the tide flexes.) 'See that climb? That spike is saline surge. It eats at the root mass before you see the collapse. If we can catch that...we can buy time."
    "The fishers lean in. The projection paints their faces in cold blue. You feel, for a flicker, that the whole square could tilt with their consent."

    "Old Fisher 3" "You say it saves us. I say it makes us vulnerable if it fails."

    kaito_sato "Then we don't move faster than we test. We place, we read, we respond."

    "His voice is steady; your chest eases. But there are other sounds—a smooth, rehearsed applause that doesn't belong to the market. LuxCorp's PR team has a portable display beneath an umbrella two stalls over: a slick animation of a wall rising like a white promise. Two uniformed staff hand out pamphlets with bullet points" "Immediate Protection,' 'Donor-Backed Funding,' 'Guaranteed Jobs."
    "PR Woman: (smiling too brightly) 'Mayor Elena's briefing later will feature concrete models. You should come—see the future the city's counting on.'"
    "You smell the gloss of their flyers—ink and ambition. The PR woman's teeth are a precise, designed thing."
    "Internal monologue: The town is hungry for certainty. Lux's wall is a spoonful that looks like a meal. But it's not always the right taste. Kaito's sensors are the slow stew—less immediate, but nourishing if tended."
    "Your brother's watch ticks louder. The weight of a possible choice presses at your shoulders like a tide."

    menu:
        "Appeal to their memory—mention the last storm":
            "You recite the day your brother didn't come back, not to dramatize but to remind them why early warning matters. Faces soften, some nod; Tomas closes his eyes, the old grief settling between you."
        "Focus on the data—let the numbers speak":
            "You point at the spike graphs, at Kaito's steady charts. A pragmatic few lean forward, whispering about grants and logistics. Tomas's jaw tightens; he prefers stories, but he listens."
        "Call out LuxCorp's PR directly":
            "You step toward the kiosk, voice thick. The PR woman smiles sharper; a ripple of cold air cuts the circle. Kaito grips your arm, sensing the escalation."

    menu:
        "Encourage Kaito to publish the first reads":
            "You nudge him toward transparency—let the town see the errors as part of the process. Kaito glances at you, torn but relieved at your faith."
        "Suggest we keep the initial reads private until refined":
            "You turn the sensor away from the path of gossip. Kaito studies the data quietly and agrees, but his jaw clenches; secrecy tastes like safety and fear in one mouthful."

    jump chapter9
    return
