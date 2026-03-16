label chapter8:

    # [Scene: Verdant Terrace | Night — Storm Surge]

    scene bg ch8_6b08b4_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense percussion with rising strings — frantic tempo]
    # play sound "sfx_placeholder"  # [Sound: A sudden, deep roar of water; the slap of waves against makeshift levees; radio static under voices]
    "You taste metal and salt on your tongue before you can place why—an old, animal reflex. The terrace feels smaller, then impossibly exposed, as if the city itself has folded inward and squeezed the air out"
    "of the night. Lights from the Beacon are dim behind a veil of rain; the neon of the distant urban district is smeared into liquid streaks."
    "The first breach is not cinematic. It's a wet, ugly sound: the give of sandbags, the slurp of pooled water finding a seam in our defenses. Someone throws a shovel and it sticks in the tide like a plea."
    "You run before you've decided to. Your boots slap across reclaimed wood; mud sprays your calves. The decentral pumps you helped map and calibrate hiccup — a sputter, then a cough — and a volunteer in"
    "a yellow hood screams, and the radio channels you rely on bloom into chaos: overlapping reports, clipped callsigns, an automated alert that bleats and then dies."
    show mina_kuroda at left:
        zoom 0.7

    mina_kuroda "Aiko! Here! The western berm—it's going!"
    "You grab the rope. It is wet and alive, the fibers full of salt and storm. Your fingers know the knots. You feel every volunteer around you as a pair of hands and a name: Mina,"
    "Sora, Elias Chen, someone with paint on their sleeves from earlier that afternoon. You feel the ledger of the Beacon open into a page of immediate, brutal inventory: people, pumps, food caches, evacuation lanes."
    # play sound "sfx_placeholder"  # [Sound: Radio chatter — overlapping voices, one voice cutting through]
    show rafi_alvarez at right:
        zoom 0.7

    rafi_alvarez "—hold up. I have something. Static, hang—"
    # play sound "sfx_placeholder"  # [Sound: A beat of heavy rain]
    "You pivot, heart hammering. Rafi's voice is a thread; you pull on it because you know how he follows threads. He ducks under a tarpaulin, breath fogging in the lamplight, screen held up. A smear of"
    "leaked text scrolls across it in green letters. You don't need the words to feel them: contingency. Curtail. Infrastructure access. Public safety."

    rafi_alvarez "This came through an unsecured channel—Dr. Rowan Hale's name is on the header. 'Contingency: restrict access to local pumps and routing nodes if public safety dictates.' They planned for closure. They planned to lock us out."
    "The revelation hits the air like a cold weight. For a second the storm goes away and you can just hear the thud of your own pulse. Betrayal is a clean, corrosive noise."
    show sora_watanabe at center:
        zoom 0.7

    sora_watanabe "They always keep a map with an X where people live."
    "Elias Chen's laugh breaks like a snapped rope—no humor in it. He moves forward, command changing his tone: immediate, incandescent."
    hide mina_kuroda
    show elias_chen at left:
        zoom 0.7

    elias_chen "Then we don't let them. We push back. Everyone to Parcel Seven—hold the breach. If we do not stop it here, the Terrace goes, and with it the kitchens, the seed bank, the pumps. We hold."
    "You can see why Elias Chen's plan is magnetic: it is simple, moral in its rawness, and it feeds on momentum. People begin to gather, voices sharpening into that single thing he is good at: confidence that spreads."
    "But your brain is already counting. You taste calculus in the rain. The staged fallback you sketched in your notebook—routes, staggered teams, reserve power cores—rises in your head like a formula that won't stop. If you"
    "commit everyone to the western berm, the eastern evacuation lanes will be orphaned; the seed caches in the lower terraces will drown. If you stagger manpower—fortify the most vulnerable egress, keep medical and food lines open—we"
    "save more lives but concede territory. There is no neutral middle."
    hide rafi_alvarez
    show aiko_mori at right:
        zoom 0.7

    aiko_mori "Elias Chen, wait! If we concentrate at Parcel Seven, the eastern corridor—Evac Line Gamma—loses three pumps. We can keep seventy people moving out with a staggered redeploy. We can—"
    "Elias Chen cuts you off with the old, impatient smile that's usually comforting and tonight feels like a gauntlet."

    elias_chen "Seventy means nothing if the Terrace dies. If the Terrace falls, we lose distribution and morale. Everyone dies slower. We hold the line now. We need bodies here."
    "Dialogue turns sharp. You're both familiar with each other's voices in crisis; they are tools you've used together and against one another."

    aiko_mori "This is not an argument about courage. It's math and flows. If the pumps at Alpha and Beta fail while everyone's stuck at Seven, there will be bottlenecks. People will drown in alleyways because no one was rerouted."

    elias_chen "And if we don't stop the water at Seven—if we lose the Terrace entirely—there will be no pumps left to speak of. No community. No kitchens. No Beacon."
    "Mina steps between you, gloved hands lifting like a mediator's placard."
    hide sora_watanabe
    show mina_kuroda at center:
        zoom 0.7

    mina_kuroda "Both of you—stop. We need a plan we can move on now, not a calculus duel in the rain."
    "Sora finds you both with her eyes, as if scanning a map only she can read. She does not pick a side. She considers the history in the stones under your feet."
    hide elias_chen
    show sora_watanabe at left:
        zoom 0.7

    sora_watanabe "When the sea took the old pier, we mended it with whatever we could. We learned where to let water pass and where to stop it. The sea always chooses. We've only ever chosen how to be ready.' (she nods at you both) 'Do not let fury choose for you."
    "The pumps cough again—a mechanical wheeze—and a volunteer by the northwest planter box is screaming something about current changes in the channel. The rain bites along your jawline; your wet hair clings to your scalp. You"
    "register, with that detached clarity that crisis brings, the immediate constraints: limited generator time, a thinning supply of sandbags, volunteers already exhausted from previous shifts."

    menu:
        "Run to the western berm and grab the last dry sandbags":
            "You tear away from the thought of analysis and move with the crowd—your hands close on cold, gritty sand and you pass it along, muscles burning but present in the ancient human gesture of passing lifelines."
        "Pull the radio and coordinate evac lanes for Gamma and Delta":
            "You stay put, knees pressed into wet wood, fingers fumbling with knobs. You route volunteers on channels and mark the lines with a trembling but steady voice, drawing a digital path through static."

    menu:
        "Shout for everyone to move to Parcel Seven—full defense":
            "You raise your voice until it hurts and let your belief in standing and fighting carry over the storm. People respond because they trust you; bodies move like one, a brief and terrible beautiful thing."
        "Order a staggered retreat—open Evac Gamma, reroute food lines, secure elders first":
            "You speak soft and precise, your voice a machine of care in the chaos. People split reluctantly but with the clarity of mission, and you watch the first cluster move toward the lit path, your hands shaking as you mark the route."
        "Try to split teams—send anchors to Seven while others shepherd evac lanes":
            "You make a plan that threads both impulses together, barking roles and deadlines. For a breath it feels like balance, until the wind takes the plan and scatters the paper it was written on."

    jump chapter9
    return
