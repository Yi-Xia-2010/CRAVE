label chapter12:

    # [Scene: Courtroom | Morning]

    scene bg ch12_f99e88_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense strings with a steady percussion pulse]
    # play sound "sfx_placeholder"  # [Sound: Coughing, the shuffle of papers, a gavel's dull thud]
    "Narration:"
    "You stand with your palms flat against the wooden rail, the grain rough under your fingers. The courtroom smells of old paper, coffee gone cold, and a faint, stubborn trace of salt that seems to have"
    "followed you in from the harbor. Every face in the room feels like a measurement: some are worn with hope, others folded tight with fear. The judge's bench sits like a small island of impartiality under"
    "a bright, indifferent light."
    show old_tomas at left:
        zoom 0.7

    old_tomas "We didn't call the sea friend, not exactly. But we knew how to keep time with it. It taught us when to go and when to hold. Those gates—those big machines—they change the rhythm. They don't ask if a person depends on the tide to feed a child."
    "Narration:"
    "His sentences land inside you like stones. They are simple; they are dangerous. Each detail becomes evidence of the life you're trying to protect. The lawyers ask the 'big questions,' but the town's weight is in these small, domestic facts. You had hoped that would be enough."
    "Jun Park rises for TideLine's counsel, smooth and anxious in equal measure. He reads company language like a script written for a courtroom rather than a harbor — 'efficiency,' 'risk mitigation,' 'scalability.' When he looks up"
    "toward you, his composure cracks a fraction; you see someone who believes in what they were taught but not always in what it costs."
    show jun_park at right:
        zoom 0.7

    jun_park "Our prototype is a public service. It protects lives and property. We do not seek to limit access—"
    show marin_sol at center:
        zoom 0.7

    marin_sol "Access is not only legal language. It's bones and breath. It's the small hour when the crab boats leave and when children learn to mend nets. You can measure dollars and gates. You cannot measure dinner-bell customs."

    jun_park "I understand that. I really do. But—"
    "Narration:"
    "The judge asks for decorum. The room hums with the momentum of formalities, but outside it feels like pressure. Your conscience is blunt and awake; the legal path feels righteous, necessary. You remember the night you"
    "agreed to pursue this—Mayor Ana's exhausted eyes, Lian's cautious optimism—and you hold to the belief that public airing will prevent a worse fate."

    menu:
        "Lock eyes with Old Tomas, let him know he is not alone":
            "You meet his steady gaze; his hands relax a fraction—he gives you the smallest nod and the room seems to recede."
        "Bow your head and read your notes, keep the focus on facts":
            "You look down, ink blurring slightly as the flood of words steadies. Your voice when you speak will sound more legal, less personal."

    # --- merge ---
    "Continue narrative."
    # play sound "sfx_placeholder"  # [Sound: Outside, a protest chant swells and breaks against the courthouse walls like surf. The press cameras click in a jagged rhythm. The court reporter's fingers fly.]
    "Mayor Ana approaches you after Tomas' testimony. Her face carries the weight you helped saddle on her shoulders, lines deeper than the week before. She is practical to the bone; you have watched her balance budgets under storms. Now she stands between your ideals and the municipal ledger."
    hide old_tomas
    show mayor_ana_beltran at left:
        zoom 0.7

    mayor_ana_beltran "Marin, we won hearts in that room today. But TideLine's teams have pockets deeper than our optimism. This goes on—this costs us. There will be consequences in services, in summer programs, in grants already allocated."

    marin_sol "And we'll watch what we saved wither while we wait for legal fees to breathe. Is this the trade you meant when you said 'public good'?"

    mayor_ana_beltran "I didn't mean for anyone to lose their roof. I didn't mean for the greenhouse expansion to stall or for the after-school fishing lessons to be cut. But I'm not going to sell our future for a quick cover, Marin."
    "Narration:"
    "Her conviction glances off you like weather. It is not a door closing; it's a boundary. You promised the town you'd push for accountability. Now you see the shape of the cost."
    # [Scene: Montage — Months of Litigations | Various Times]
    hide jun_park
    hide marin_sol
    hide mayor_ana_beltran

    scene bg ch12_f99e88_2 at full_bg
    # play music "music_placeholder"  # [Music: Fast, insistent percussion underscoring the montage]
    "Narration:"
    "The courtroom becomes a second home. You learn the smell of courthouse coffee at dawn and the pattern of legal counsel pacing at midnight. Old Tomas' statements circulate in the official record; you watch his testimony"
    "reappear in articles, in op-eds, and then in the slow, bureaucratic replies of TideLine's counsel. Each hearing brings a small moral victory and a new drain on municipal funds."
    "Rosa runs neighborhood drives and stitches together grant applications with the tenacity of someone mending a torn sail. You help where you can: fielding interviews, presenting ecological models, sitting through depositions while your hands go numb"
    "with cold and adrenaline. Kaito Navarro shows up with stacks of soup and strong shoulders; he holds town meetings on the pier and coordinates emergency watch rosters. His presence is a steady engine, but even steady"
    "engines take fuel."

    "Old Tomas (during a break, leaning on his cane)" "You did the right thing, girl. The law remembers what a man like me remembers."
    "Narration:"
    "His praise is a small, heavy thing. It rests on your chest like a pebble. But rightness does not put food on a table, not always. You begin counting differently: how many hearings until the grants"
    "dry, how many months until the community garden's irrigation is cut, how many families until the seasonal boats leave for good."

    menu:
        "Stay and water the greenhouse beds before heading to the afternoon hearing":
            "You wrap chilled fingers around the hose, feeling the first, fragile leaf give under your touch. It steadies you, small and stubborn, like the life you're trying to keep."
        "Head straight to the pier meeting to organize the next protest":
            "You move into motion—maps, megaphone, routes—action focuses the ache into something you can manage."

    # --- merge ---
    "Continue narrative."
    # [Scene: Maris Bay Research Greenhouse | Late Afternoon]

    scene bg ch12_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The drip of an uncapped irrigation line, distant gull calls]
    "Narration:"
    "The greenhouse becomes a ledger of postponed promises. The scaffolding to expand a research wing leans like a hopeful skeleton; the sensors Lian wanted sit in crates. You stand in the humid corridor and feel the"
    "weight of every canceled workshop, every student who will not learn here because the town had to choose between legal defense and community classes."
    show dr_lian_obasi at left:
        zoom 0.7

    dr_lian_obasi "We can salvage seedlings. Community science isn't a luxury. But if the funding dries you won't be able to keep the staff on. You know that. I know that."
    show marin_sol at right:
        zoom 0.7

    marin_sol "I know. I also know TideLine's clauses would change access in ways we can't quantify. I'm not willing to hand over the shore for a promise that optimizes for 'people at risk' on a spreadsheet."
    show dr_lian_obasi at center:
        zoom 0.7

    dr_lian_obasi "Then we pay in other ways."
    "Narration:"
    "Paying in other ways bleeds slow and bright. Faces you once counted on for seasonal work drift from the boards of the co-op to posters asking for help. The mayor announces cuts on a rainy Tuesday,"
    "her voice steady through a public feed, her eyes rimmed and human. After-school programs are first; the volunteer docents for the storm-shelter garden follow. You watch the list like a death roll."
    # [Scene: The Old Pier & Fishing Co-op | Early Morning]
    hide dr_lian_obasi
    hide marin_sol
    hide dr_lian_obasi

    scene bg ch12_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The muffled clank of winches; a child counting shells]
    "Narration:"
    "Contracts signed to preserve 'open access' require 'maintenance' crews that patrol and log entries. Regulation becomes friction; friction becomes attrition. Small fishermen are fined for minor infractions—untied ropes, missing permits—because the new bureaucracy can enforce tiny"
    "rules with big penalties. You watch as seasonal families pack rusted boats and names vanish from the co-op roster."
    show kaito_navarro at left:
        zoom 0.7

    kaito_navarro "They said they'd protect us. They said 'community-friendly.' Do they know what our boats look like? Or did they send someone who thinks a coastline is an algorithm?"
    show marin_sol at right:
        zoom 0.7

    marin_sol "They know numbers. They don't know tides. We made people listen today — but legal pressure is a long, grinding machine. It chews at funding and at patience."

    kaito_navarro "We can keep fighting. I can keep fighting. I don't know if it's enough."
    "Narration:"
    "His jaw is a map of stubbornness and loyalty. You want to tell him to leave with you, to carry this fight elsewhere where it might be less costly. But the town is stitched into him as it is into you; leaving would be another kind of defeat."

    menu:
        "Suggest Kaito come with you and help displaced communities elsewhere":
            "You imagine him beside you in a different harbor, hands still strong, tired but hopeful. He pauses, grip loosening as if considering a new horizon."
        "Ask him to stay and promise to visit as often as you can":
            "He presses a thumb into your palm, a silent contract. The promise sounds small and fragile, like a bottle tossed into the sea."

    # --- merge ---
    "Continue narrative."
    # [Scene: Train Station | Rain-bleached Afternoon, Months Later]
    hide kaito_navarro
    hide marin_sol

    scene bg ch12_f99e88_5 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano notes; a low, sustained cello note underpins the scene]
    # play sound "sfx_placeholder"  # [Sound: The hiss of the train's brakes; the murmur of distant voices]
    "Narration:"
    "The town is thinner. You feel it in the absence of faces, in the fewer boats tied at the pier, in the greenhouse's quiet. You have packed a small bag: a battered notebook, a multi-tool, some"
    "seed packets, Lian's last sample jar, a sweater Kaito swore would keep you warm. There is no theater to this leaving — only the concrete and the hiss and the steady beat of your heart hitting"
    "a tempo that will not slow."
    "Kaito Navarro arrives with wet hair and a coat that still smells of the sea. His hands, callused and honest, hold a thermos—soup, no doubt—and a rolled piece of fishing net he's been repairing. He says"
    "nothing at first. You've argued and consoled and planned together in messy, beautiful ways. Now the space between you is defined by all the small things that fit into a town."
    show kaito_navarro at left:
        zoom 0.7

    kaito_navarro "You packed light."
    show marin_sol at right:
        zoom 0.7

    marin_sol "I've always been bad at carrying goodbyes."

    kaito_navarro "You didn't have to come to every hearing. You didn't have to make the town a public theater for our pain. You could have walked a quieter line."

    marin_sol "I don't do quiet lines when it comes to home."

    kaito_navarro "Home stayed. People left. You leaving feels like... an ending I didn't know how to tell myself."

    marin_sol "I didn't either. I thought the right thing would be enough to keep it whole."

    kaito_navarro "Right things come with billable hours and ink-stamped clauses. I watched the kids at the co-op counting down weeks until their parents left for other work. I watched Old Tomas fold his stories into the court record and then sit alone on his porch because half the porch is empty. We fought with everything we had, Marin."
    "Narration:"
    "Every memory of the last months rushes forward — the courtroom's sterility, Dr. Lian's tired smile, Rosa's frantic calls, the mayor's steadying hand that still had to make cuts. The righteous heat of legal victory cools"
    "into a different metal: grief and the knowledge that your conscience kept you awake, but you also kept the ledger open for others' losses."

    kaito_navarro "Where will you go?"

    marin_sol "To where they're calling me. To places with smaller harbors and big displacement. To work with people who lost more than a garden. It's a long train ride."

    kaito_navarro "Is this what you want? Or is it what you need to punish yourself less for what happened here?"

    marin_sol "I don't know if it's punishment or penance. I know I have to move. I promised myself I would follow where work could do the most good."

    kaito_navarro "And I promise I'll keep the pier open as long as I can. I will keep the meals going, Marin. I will hold this town in the ways I can."

    marin_sol "You're always a stubborn keeper."

    kaito_navarro "Someone has to be."

    kaito_navarro "Do you regret it? Any of it?"

    marin_sol "I regret the small things. The garden lost workshops. Kids who won't learn to take apart an engine. The dinners we couldn't fund. But I don't regret standing up. I don't regret the voice we made heard."

    kaito_navarro "And us?"

    marin_sol "Us is a different ledger. I thought we'd build a bridge and walk it together. The bridge cost more than we thought."

    kaito_navarro "Maybe some bridges are built on two shores. Maybe one of us has to cross first."

    marin_sol "Maybe."
    "Narration:"
    "Your chest fills with urgency. The train's whistle is a kind of summoning. You keep telling yourself that leaving is action—moving toward new communities, new fights, new chances to do better. Yet the immediacy is a"
    "wound: names being crossed off co-op boards, a shrunk summer lunch program, empty chairs at the shelter. The town did not privatize fully; the legal fights bought time and dignity in places. But the cost has"
    "been real and hungry."
    "Kaito Navarro pulls you into a hug that seems to stretch time thin. It is long and quiet — the kind that says more than words can carry. You feel his heartbeat against your chest, his"
    "coat's dampness mixing with your own salt. It is not cinematic. It is human and raw and final in the way single, decisive motions are."

    kaito_navarro "Come back if you can."

    marin_sol "I will try."
    "Narration:"
    "There is grief threaded through the warmth of the hold. Leaving is not failure; it is a ledger entry of priorities and outcomes. You have clarity of conscience, and clarity of consequence. You are leaving because"
    "someone must go where the displacements multiply and the paperwork is endless and the people need someone who knows how to translate loss into aid."
    # play sound "sfx_placeholder"  # [Sound: The train announcement calls your platform. The hiss grows sharper. You step back, feeling each inch as a small break.]

    kaito_navarro "Promise me you'll write. Not about court transcripts—about small things. The kids, the pier, Old Tomas' stories when you can. Don't let us become only a case study."

    marin_sol "I promise."

    kaito_navarro "Keep this. For the sound of a boat leaving, for when you need to remember what you fought for."

    marin_sol "Thank you."
    "Narration:"
    "The whistle becomes a drumbeat. You hoist your bag, heavier with the talisman than with clothes, and step onto the train. As it pulls away, the platform blurs: faces, the greenhouse's fogged glass, the old pier"
    "leaning into the gray. The town is smaller from this angle, but no less real."
    "Marin Solé [internal]:"
    "Your chest is knotted and raw. It will take time to know whether leaving was a rescue for anyone or merely a reallocation of burden. You choose to trust that the clarity of conscience will not"
    "erase the ache of loss. You leave with the knowledge that you did what you could, and with the knowledge that 'what you could' asks others to pay."
    hide kaito_navarro
    hide marin_sol

    scene bg ch12_f99e88_6 at full_bg
    # play music "music_placeholder"  # [Music: Cello holds; piano gives a single, resigned chord]
    "Narration:"
    "Months will pass. You'll write letters full of small triumphs and slow rebuilds. You will stand on other shores and find new stories that demand translation, and you will carry Maris Bay in your pocket like"
    "a map of what justice sometimes costs. The town will not be the same — neither will you. There is a grief that keeps company with conviction. It is cold sometimes, but it is honest."

    scene bg ch12_f99e88_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade to a low, steady drone]

    scene bg ch12_f99e88_8 at full_bg
    "THE END"
    # [GAME END]
    return
