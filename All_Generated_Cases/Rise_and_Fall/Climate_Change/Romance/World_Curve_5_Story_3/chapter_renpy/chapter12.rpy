label chapter12:

    # [Scene: Marshland Corridors | Dawn — Two Weeks After the Hearing]

    scene bg ch12_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low tide breathes against marsh mud, distant machinery hums from the seawall work; a child's laughter cuts through the air.]
    # play music "music_placeholder"  # [Music: Soft, ascending strings with steady percussion — hopeful but tempered]
    "You wake before the town. When you step out, the air tastes of ion and wet earth, salt and something new: the sharp, metallic edge of contracts inked and promises made. The regulation notice had arrived"
    "like a tide line on the town's legal shore — conditional halts, mandates for monitoring, and a grudging concession from Atlantech to fund marsh corridors. It is not everything you wanted. It is more than you"
    "feared."
    "Your hands still remember how to work: the calluses near your thumb, the habit of folding fragile seedlings in like small breaths. You tuck a sodden clump of spartina into the mud and press until the"
    "roots meet forgiveness. Around you, people press, too — families erecting temporary berms, volunteers lowering biodegradable mats, Dr. Kaito pacing with the grave deliberation of someone who has seen decades of shorelines and storms."
    show dr_kaito_mori at left:
        zoom 0.7

    dr_kaito_mori "They listened to the data and to the town. That's a rare hinge, Amaya."
    show amaya_saito at right:
        zoom 0.7

    amaya_saito "Rare and fragile. We'll need to keep the hinge from rusting."
    "You say it to him, but your voice is steadier than the thought feels."

    dr_kaito_mori "You always were good at making hinges. You taught us to look at stress points and reinforce them with life, not just with concrete."
    "He offers a small, dried-smile; the kind that comes from long experience rather than surprise. You remember telling yourself that this would be a marathon, not a victory lap. The regulators' conditional halt gives you time"
    "and teeth — monitoring requirements, scheduled reviews, funding tied to restoration benchmarks. Atlantech's concession binds corporate resources to ecological outcomes. It is compromise dressed in paperwork, but it is leverage."
    hide dr_kaito_mori
    hide amaya_saito

    scene bg ch12_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The scrape of a shovel. Elena's footsteps are firm.]
    show elena_cruz at left:
        zoom 0.7

    elena_cruz "The council pushed hard. The mayoral letter made the difference with the regulators. The town held together when it mattered."
    show amaya_saito at right:
        zoom 0.7

    amaya_saito "You made them look at us as a whole community, not a line item."

    elena_cruz "We were a stubborn line item, yes."
    "Elena's words are a small warmth that sits behind your ribs. The town's insistence — rallies, public comment, people writing their house histories into petitions — changed the arc of a meeting that had felt tilt-heavy"
    "against you. Still, as you lift another seed clump from the tray, you can see the line where industry met shore: a sterilized patch of concrete anchors, a fortified segment protecting the fish market and the"
    "hospital. The marsh between those anchors has been granted corridors, wide and green. The fortified segments will remain."

    menu:
        "Walk the new corridor's edge and map micro-habitats":
            "You set your waterproof tablet to record, kneel at a salt pan, and note a crab burrow that survived the grading. The act of cataloguing gives you a small, practical calm."
        "Help the Hoshi family relocate a sapling bed inland":
            "You lift the crate with surprising leverage; Mrs. Hoshi squeezes your wrist and says, 'You kept your promise.' You blink, and something steadier arranges itself in your chest."

    menu:
        "Open Lucas' message now.":
            "The message is a short video feed: scaffolding at a distant site, his voice clipped by static. He says he leaves next week to manage mitigation in another region. You feel your throat push a sound you don't finish."
        "Finish logging the sensor calibration before replying.":
            "You finish the calibration with the steady attention that has always soothed you. When you reply, your message is measured and practical; it keeps the connection from fraying in the heat of emotion."

    menu:
        "Walk out to the new boardwalk with Mika and point out return patterns for the birds":
            "You name the species you see; Mika scribbles in the volunteer notebook. You feel small and powerful at once — the knowledge of patterns as a kind of protection."
        "Open the public dashboard and post the month's turbidity trends with a short explanation":
            "You write a clear summary. People comment and ask questions. The town talks back, and the feedback keeps the policy alive and accountable."
    "THE END"
    # [GAME END]
    return
