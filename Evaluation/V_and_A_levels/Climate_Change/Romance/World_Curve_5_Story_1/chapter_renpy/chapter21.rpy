label chapter21:

    # [Scene: TideLab | Early Morning]
    # play music "music_placeholder"  # [Music: Sharp, urgent strings — a repeating figure that quickens the heartbeat]

    scene bg ch11_e67f19_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain slashing against corrugated metal; distant horns from the quay]
    "You feel the lab before you see it: the low thrumming of battery banks, the sharp click of a tablet keyboard, the tang of recycled salt and wet soil. The night—short and restless—has left fingerprints on"
    "every surface. Papers are stacked in careful, anxious piles; a projector's glow ghosts across Corinne Voss's glossy renderings and your own tide-model printouts. The two images rub against each other like polarities."
    "Your pulse is fast. It is not fear exactly; it is pressure concentrated into a single, urgent point. Deadlines are teeth. The permit clock is a metronome in your skull, and every tick snaps another volunteer to attention."
    "You move through the room with the economy of someone who knows where the tripping points are. Jules is hunched over a laptop, fingers skittering through footage. Luka Maren is calibrating a sensor array with methodical"
    "hands—his movements a small island of focus in the storm of tasks. Abuela Rosa sits at the bench edge, hands folded around a steaming cup; her eyes track you like tide lines."
    show jules_park at left:
        zoom 0.7

    jules_park "We pulled overnight clips—Voss's barges and the staging boats. Good close-ups of the dredging rigs. Could go live with a feed, but we'd need a press primer."
    "Jules's voice skips. They keep glancing to the doorway, to the way the rain slices the window. You can tell they're calculating how much exposure you can stomach."
    "Luka Maren looks up, amber eyes sharp in the lamplight. 'If we go viral with raw footage, we get attention. We also invite counters—PR teams, legal threats, coordinated takedown. It becomes a chessboard with extra players.'"
    "You want to say yes and no at once. The thing about you is that you are allergic to binary answers when the ground is that slippery."
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "We file the suit. But we give people something to stand behind—sensors, footage, an explainer. Transparency so people understand the legal steps."
    "(You keep the sentence short because long ones leave room for doubt.)"
    "'I won't ask the town to wait without seeing the gears.'"
    "Abuela Rosa's gaze is gentle, unreadable in the way elders often are—neither approval nor disapproval, only gravity."
    show abuela_rosa at center:
        zoom 0.7

    abuela_rosa "Show them the gears. Teach them how to turn them. Do not let fear be the teacher."
    "Mateo arrives in a rain-speckled sweater, shoulders high from the wind. He drops a folder on the bench; the clap of paper is loud in the space."
    hide jules_park
    show mateo_reyes at left:
        zoom 0.7

    mateo_reyes "Banks are calling. Credit lines are on reminders. If the permit goes and the project starts, fisherfolk lose access to the beds we've relied on. I can stand with you, hermana—but I need a plan that pays the bills in weeks, not months."
    "His worry is immediate and human—lines of credit and market weeks. It snaps the strategy into concrete terms: wins on paper are fragile things when people's rent is due."
    "Luka Maren meets your eyes for a long beat, then shifts to the sensor array in his hands as if its wires are easier to read than human faces."
    hide amaya_reyes
    show luka_maren at right:
        zoom 0.7

    luka_maren "There's a research consortium—Voss-linked—offering shared data access. They promise influence in permitting committees. We could get a seat at the table, but their platform is... entangling. If we use them to amplify our sensors, people might see us as compromised. Integrity for leverage; that's a hard trade."
    "You taste salt and metal. The sensor array hums against Luka Maren's palm like a small engine, impatient."
    hide abuela_rosa
    show jules_park at center:
        zoom 0.7

    jules_park "We can stage a demo tonight—teach folks to read the dashboard, stream a guided tour. Or we can hold the playback for regulators to avoid muddying the legal record."
    "Amaya Reyes: (you let the words fall like stones) 'Both move energy. Both burn people out. We need a hub strategy—legal muscle and social oxygen.'"

    menu:
        "Let Luka take the drone tonight to capture shoreline buildup":
            "You hand Luka the extra battery. He nods, eyes quick with relief and guilt. He promises to be careful with footage metadata. Jules packs an annotated checklist."
        "Keep footage sealed for legal counsel; use tonight for community training only":
            "You tap the tablet screen to lock the raw files. Jules exhales and flips slides for the training. The room settles into teach-and-learn rhythm, practical and contained."

    # --- merge ---
    "Both outcomes converge; resume the main narrative."
    "You watch the volunteers move—small, efficient bursts of action: charging batteries, folding canopies, printing contact sheets. The lab is a mouthful of purpose. The threat of Corinne Voss's team—shiny suits, quick permits—cuts across everything like a cold wind. It presses from the concrete quay to your bones."
    hide mateo_reyes
    hide luka_maren
    hide jules_park

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant thunderclap, like a gavel]
    "You convene a quick briefing. Tamsin is scheduled at noon in the council chambers, but you need clarity—what leverage do you hold, and how brittle is it?"
    "Luka Maren leans against the bench. He speaks lower, voice catching like a wire."
    show luka_maren at left:
        zoom 0.7

    luka_maren "If we present a public campaign tied to the filing, regulators might act faster. But they can also be swayed by Voss's narrative: jobs, infrastructure, inevitability. We hand them a spectacle and they hand us a counter-narrative."
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "Then we control the narrative contours: facts, context, human stories. Not just footage—tide models, oral histories, economic impact. If the regulators see the town's face alongside the data, decisions slide from abstractions to obligations."

    luka_maren "And if Voss floods the feed with sponsored content? If they spin the story into loss and salvage and inevitability?"

    amaya_reyes "Then we outwork the spin. We prepare legal briefs alongside press packages. We keep channels open to sympathetic regulators. We get counsel to vet everything."
    show jules_park at center:
        zoom 0.7

    jules_park "Counsel costs. So do outreach ops. Someone's budget has to climb, and fast."
    hide luka_maren
    show mateo_reyes at left:
        zoom 0.7

    mateo_reyes "My family isn't a research budget."
    hide amaya_reyes
    show abuela_rosa at right:
        zoom 0.7

    abuela_rosa "No. But your family has names. Names are currency too. They can translate to pressure if you spend them wisely."
    "You swallow. The syllables of advantage and loss clatter in your mouth. The lab, for a moment, is a clock tower rung hollow—time, time. Somewhere along the quay, engines rev."
    # [Scene: Council Chambers | Late Morning]
    # play music "music_placeholder"  # [Music: Percussive, clipped — staccato percussion under a low synth pad]
    hide jules_park
    hide mateo_reyes
    hide abuela_rosa

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmur of hallway footsteps; the rain intensifies outside]
    "You enter with the stack of filings, printouts splayed like armor. Tamsin stands by a table, tablet in hand, an island of municipal propriety amid the humidity. Her face is practiced; the planner's calm is a mask fitted to meetings."
    show tamsin_cho at left:
        zoom 0.7

    tamsin_cho "The moratorium clause is negotiable up to a point. Council can issue a conditional hold if the permit triggers immediate environmental risk markers. But it has to be enforceable and precise—dates, metrics, penalties. Otherwise it's theater."
    "Tamsin taps the tablet, projecting a sample moratorium outline into the room. The holograph shimmers: legal language is a pale, clinical thing compared to the smell of wet wool and coffee. You feel the scale of translation: people's stories to statute."
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "We need breathing room that is tight enough to be enforceable and flexible enough to respond to emergency markers. If it's sloppy, Voss will exploit ambiguity."

    tamsin_cho "Agreed. But Voss's counsel is fast. They'll push for language that allows phased work with mitigations. We can push back with the filings—the precedents—but that requires time and specialist input."
    show luka_maren at center:
        zoom 0.7

    luka_maren "Specialist input costs time and money. And the permit clock doesn't pause for invoices."
    "Your throat tightens. The urgency is unbearable—an electric wire thrumming under skin. You think of Mateo's ledger, Abuela Rosa's woven shawl, the kids who learn tide heights by heart. You think of the technicalities that decide whether homes are razed or reinforced."
    "Tamsin studies you, something unreadable playing across her features."

    tamsin_cho "There is also the option of a coordinated public campaign. Bring regulators national attention, force greater scrutiny. But it invites PR counters and possible legal motions from Voss. Or you proceed quietly through precedent—slower, technical. Or you use legal pressure to broker a moratorium with us."
    "You can feel the room tilt towards the three poles: public spectacle, quiet precedent, or conditional moratorium. Each is a lever; each snaps at different people."
    hide tamsin_cho
    show mateo_reyes at left:
        zoom 0.7

    mateo_reyes "If you go loud, the banks will hear the noise. If you go quiet and lose, we lose everything quietly. If you negotiate... you might get a stopgap, but is stopgap enough?"
    "Abuela Rosa reaches out and covers your hand. Her skin is papery, warm."
    hide amaya_reyes
    show abuela_rosa at right:
        zoom 0.7

    abuela_rosa "You are not alone in carrying this, niña. The town is a net; pull one strand too hard and it tears."
    "Luka Maren: (between you and Tamsin) 'There's also the messier option—join a Voss-linked research network for influence. It gives us data access that could sway regulators from within, but the optics will be brutal.'"
    "Tamsin's mouth tightens. She is municipal machinery—diplomacy is her tool, but she is not blind to optics."
    hide luka_maren
    show tamsin_cho at center:
        zoom 0.7

    tamsin_cho "I can propose a conditional moratorium, but you'll need to define the enforcement metrics. If you want me to bring it to council, you'll have to present compact, measurable markers: turbidity thresholds, real-time sensor criteria, fines for violations, a timeline for review."
    "You hear the permit clock click. The thunder outside grows teeth."
    "Your internal voice is a razor: choose the scale of the response that fits the town's capacity and the moral calculus of risk. You run through trade-offs like a checklist in your head—visibility vs. vulnerability, speed vs. solidity, community trust vs. perceived co-option."

    menu:
        "Push Tamsin to draft the moratorium language now—tight metrics, enforceable penalties":
            "Tamsin hesitates, then nods. She pulls up a template and begins to annotate it with precise markers. Luka Maren rubs his forehead, already calculating sensor specs to match the language."
        "Argue for preparing the public campaign package first—materials, spokespeople, verified footage":
            "Jules's shoulders lift as if a weight were added. They start organizing press lists and a timeline, fingers flying over their keyboard. Mateo's jaw clenches: he isn't sure but he understands urgency."

    # --- merge ---
    "Both outcomes converge; resume the main narrative."
    "You look at each face in turn—Luka Maren's tentative determination, Jules's bright exhaustion, Mateo's worry-lined honesty, Abuela Rosa's slow steady presence—and the scale of the town settles across your shoulders."
    "The room condenses to the decision point. The rain is a steady drum now, the thunder a steady gavel. You have the filings. You have the footage. You have the town."
    "You inhale, and it is all air and salt and the electric smell of something about to begin."
    "Amaya Reyes: (quietly, steadily) 'We need to pick a legal-tactical strategy. We can't split ourselves into a dozen unfinished things. One course now, aligned with the filing, with contingencies. We can pivot later, but the first step must be decisive.'"
    "Tamsin: (nods, voice measured) 'The council will want specifics. If you go public, we'll need a communications plan that matches the legal record. If you go precedent, we buy time for counsel and technical evidence. If"
    "you negotiate a moratorium, I'll draft conditions—but the town must agree on what metrics protect both homes and livelihoods.'"
    "Luka Maren watches you, something like fear and faith warred in his expression. He reaches for your hand before you can think—an impulsive, human thing—and squeezes."
    hide mateo_reyes
    show luka_maren at left:
        zoom 0.7

    luka_maren "Whatever you choose, I stand with you. I will build the tech to match the plan, not the other way around."
    "You let his hand go with a gentleness that feels like permission. The lab and the council and a weathering coast all wait on your voice."
    # play music "music_placeholder"  # [Music: Strings and percussion swell to a peak, then hold on a single sustained chord — the room breathes with it]
    hide abuela_rosa
    hide tamsin_cho
    hide luka_maren

    scene bg ch11_e67f19_4 at full_bg
    "You inhale again. The choice is not the end; it is the sharp hinge on which the next set of possibilities swings outward."

    menu:
        "Launch a coordinated public campaign tied to our legal filings (press, regulators, viral footage).":
            jump chapter25
        "Proceed quietly through precedent, aiming to win on technical legal grounds.":
            jump chapter11
        "Negotiate a conditional moratorium with Tamsin, using legal pressure as leverage.":
            jump chapter29
    return
