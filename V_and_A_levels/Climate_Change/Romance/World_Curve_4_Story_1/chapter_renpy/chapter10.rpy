label chapter10:

    # [Scene: Maya's Office | Night]

    scene bg ch10_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant harbor horns, the slow drip from a leaky window, a neighbor's radio muffled through the wall]
    # play music "music_placeholder"  # [Music: Low, urgent synth undercurrent]
    "You come back to the room that has become your net — a web of names and numbers stapled to each other, connected by red string. Your fingers smell faintly of toner and salt. The Moleskine lies open, an impatient page marked with a single, underlined question: who benefits?"

    "You push a stack of contracts aside and trace your fingertip along a highlighted clause. The boardroom language is clinical" "expedited approval,' 'revenue-sharing mechanism,' 'contingent municipal guarantees."

    "A new PDF on your tablet chimes — an email from Lina with a subject line" "Legal ready. We can call hearings in 48 hrs."
    "You breathe. The room smells of paper and old coffee. Your brain supplies the rest: developer memos you've only glanced at before, and one—buried—note with Evelyn Hart's initials beside an approval schedule. The minutes make it look tidy. Your hands betray you, trembling while you click."
    "Noah knocks: the sound is polite against your door, then a chair scraping as he sits opposite the lamp's circle. He smells of diesel and salt. He's brought a thermos and a folder."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "Couldn't sleep either. Thought you might want company."
    show maya_soler at right:
        zoom 0.7

    maya_soler "I was going to go over the appendix again. Lina says legal can move fast."
    "Noah leans in, eyes flicking over the red-string map on your board. He taps a node. 'You found the appendix.' He doesn't ask. He knows your habit: you dig until something gives."

    maya_soler "It looks like expedited approvals, plus a revenue clause that… that could shift cost to the town if projected returns fall short.' (Your mouth tastes like metal.) 'And Evelyn Hart's name keeps appearing in attachments labeled 'sponsor alignment.'"

    noah_reyes "You sure it's not just bureaucratic language?' (He folds his hands, the old familiar attempt to weigh you down with reason.) 'Those things always sound worse than they are."

    maya_soler "That's what I thought at first. Then—' You pull a printout free and slide it across. 'This memo references 'confidential appendices' with conditions for 'preferred contractor selection.' It mentions bond guarantees tied to municipal revenue forecasts. If that clause triggers, the town will need to cover shortfalls."
    "Noah scans it, jaw tightening. The harbor light from the window sketches hard lines on his face."

    noah_reyes "If the town gets stuck on the hook, that’s not just spreadsheets. That's services, schools, the pier upkeep—people we know.' (He looks at you, steadier than he feels.) 'You think Evelyn Hart knew?"

    maya_soler "Her initials are on the cover sheet. There's a stamped route of approvals. It's not circumstantial.' (You close your eyes for a second, trying to keep the world from tilting.) 'But if I publicize this without legal backing, the developers' lawyers could sue and freeze funds. Or investors walk. Or worse—Mayor Tomas claws into panic and signs anything to avoid immediate collapse."
    "Noah drops his voice to a near whisper, conspiratorial with worry."

    noah_reyes "You ever think about how one truth can become two disasters? You expose them and the town shudders financially. You don't, and—' He swallows. 'Things get built anyway. The marsh dies in pieces."
    "You feel the room tighten as if the red string were pulling in. Your insomniac mind runs through outcomes like tide lines: short-term safety, long-term ruin, legal paralysis. Each scenario drags with it names—Rita's crooked porch, Arin's boat, the kids from the school whose field floods every spring."

    menu:
        "Call Lina now and push for immediate legal motion":
            "You fumble for your phone and type a terse, breathy message. Lina replies within a minute: 'We're drafting an injunction strategy. Stay put. We move fast.' The tiny confirmation lifts and then sinks—momentum, but exposed."
        "Wait and show Arin first to get his read":
            "You silence the phone and pick up the printouts. Arin's profile floods your memory—steady, practical. You don't want to shoulder this alone. You tuck the pages into a folder and promise yourself you'll knock on his door at dawn. Waiting feels like betrayal, and courage at once."

    # --- merge ---
    "Noah watches you choose and doesn't comment; he knows this is not a decision to be knocked over by bravado."
    # [Scene: Harbor | Pre-dawn]
    hide noah_reyes
    hide maya_soler

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slap of wake against plywood, distant gulls calling like loose chains]
    # play music "music_placeholder"  # [Music: Tight percussive strings building]
    "Noah pilots the boat, engine a soft, steady thrum beneath your feet. Your folder is there between your knees, the printouts pressed into a plastic sleeve. The cold bites through your jacket and you pull the"
    "collar up. The air here tastes sharper—ocean, algae, old rope—and it clears your head in small increments."
    "Noah points to a low bank where reeds thin."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "Rita wanted me to bring you here. She said the old marsh maps might line up with what you're seeing in the appendices.' (He glances at you.) 'She thinks the historical rights could stop some clauses dead."
    "You nod, fingernails worrying the edge of the sleeve. The boat bumps a tuft of spartina. You imagine Rita folding maps at her kitchen table, tracing lines with a finger the way you trace data points."
    "When you climb out, the mud sucks at your boots with a hungry quiet. Rita hands you a brittle sheet, edges yellowed and annotated in her cramped, careful handwriting. The ink has faded but the coastal contours are stubbornly clear."
    show rita_soler at right:
        zoom 0.7

    rita_soler "These are from your grandfather's ledger.' (Her voice is papery but fierce.) 'We never lost the knowledge. We misplaced trust."
    "You fold the map in your palms like a lifeline."
    show maya_soler at center:
        zoom 0.7

    maya_soler "If these lines show historical tidal flows, they could be a basis to argue the seawall placement is reckless."

    rita_soler "Don't put too much hope in maps. People move quicker than ink.' (She gives you a look that says she knows both endings too well.) 'But they give you something real to hold."

    maya_soler "Thank you."

    noah_reyes "If you want, I can pull records from the harbor office next. There are receipts and permits—paper that sometimes doesn't make it into digital batches.' (He gestures toward the pier.) 'Small things add up."

    maya_soler "Yes. Pull everything. Every invoice, every email printout, any signature blocks.' (Your voice tightens.) 'We need a chain, not a suspicion."
    "Noah nods, then pauses, looking at you like someone measuring whether to speak a hard truth."

    noah_reyes "Watch yourself, Maya. This... this will snag people. Not just Evelyn Hart or the developers. Folks who don't sleep at night because of mortgages and boats that won't haul. You want to expose it, you need people ready for the fall."

    maya_soler "I know."

    menu:
        "Tell Noah to prioritize discreet records pulls — avoid alerting town hall":
            "Noah sets his jaw. 'Quiet hands, then,' he says. He tightens a strap and the boat hums like a promise. The work feels clandestine and necessary."
        "Ask Noah to take the documents openly to Mayor Tomas to force transparency":
            "Noah's eyes narrow. 'That will tip the town into public panic,' he says. 'Or it will force them to act. Your call.' The possibility of an immediate confrontation hangs between you like fog."

    # --- merge ---
    "You choose again, the choices multiplying like tide pools. The decisions fragment into moral debris. You think of Lina's legal team, lined up and ready in emails; you think of Arin's hands knotting rope on the"
    "deck of his boat in the old way. You think, too, of Evelyn Hart's clipped memos and the cold efficiency of the signatures that sit like teeth in paper."
    # [Scene: Municipal Hall — Conference Room | Midday]
    hide noah_reyes
    hide rita_soler
    hide maya_soler

    scene bg ch10_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmurs, the distant clack of typing, an overzealous clock ticking]
    # play music "music_placeholder"  # [Music: Fast, staccato strings — urgency ratcheting up]
    "Lina Park is a whirlwind—tablet in hand, voice full of controlled fire. Mayor Tomas Greer sits heavier than you'd like, elbows on the table, the strain visible in his jaw. Arin arrives late, coat still smelling faintly of harbor salt."
    show lina_park at left:
        zoom 0.7

    lina_park "We have counsel on tentative injunction language. We can subpoena the appendices for redacted review. We can't win in court if we don't have process documented.' (She stabs a finger at the screen.) 'Public hearings will need notice, and we must be meticulous in our claims. No theatrics."
    show maya_soler at right:
        zoom 0.7

    maya_soler "If we request a review, the developers' counsel will stonewall on grounds of confidentiality. If we go public now, finances could freeze. If we wait, construction could start."
    show arin_kai at center:
        zoom 0.7

    arin_kai "Is there a middle path? A temporary moratorium on work until documents are reviewed?' (He leans forward, pragmatism folding into worry.) 'If we can get the Mayor to issue even a short pause, it keeps the town afloat while legal does its job."
    hide lina_park
    show mayor_tomas_greer at left:
        zoom 0.7

    mayor_tomas_greer "We can't just halt contracts without probable cause. The town could be sued for breach. I don't want to be the one who pulls the plug and leaves people out of work.' (He rubs his temple.) 'We need certainty."
    "Lina Park shoots a look at you—sharp, assessing."
    hide maya_soler
    show lina_park at right:
        zoom 0.7

    lina_park "Certainty comes from facts. We've got facts. The appendices show preferential terms tied to municipal revenue instruments. That's enough to seek review."
    "Your stomach drops. The room shrinks; the clock ticks too loud. Arin's fingers drum a slow, restless rhythm on the table. Mayor Tomas looks between you and Lina, as if trying to put a needle on a scale."

    arin_kai "If this leaks before we're ready—' (He stops, looking at you.) 'We lose leverage, yes. But if we don't do something, the marsh is gone in pieces.' His tone is low, almost pleading. 'Maya, your call."
    "You hold all those voices and the weight of your research. In your mind the memos align like a tide chart heading toward a storm. The appendix you keep in your pocket feels like a hot coal."
    "Lina leans in; her voice is less sharp and more human, urgent with a strategist's compassion."

    lina_park "We can file for emergency review within forty-eight hours. We can prepare a press statement that frames this as a call for transparency—not an accusation. It might blunt the shock and force process instead of collapse."
    hide arin_kai
    show maya_soler at center:
        zoom 0.7

    maya_soler "But if the developers pull funding in response… the town doesn't have the cash flow to cover sudden liabilities.' (You can't keep the fear out of your words.) 'People will lose jobs. They'll blame us—rightly or wrongly."

    mayor_tomas_greer "And they'll blame me either way. I don't want to be the Mayor who lost the town. I want to be the Mayor who kept it alive."
    hide mayor_tomas_greer
    show arin_kai at left:
        zoom 0.7

    arin_kai "We can't keep living like that, Tomas. Always choosing the least bad of two terrible options.' (His voice cracks.) 'We need a path that doesn't just trade tomorrow for today."
    "The room's tension curls tighter. Files rustle. The projector hums. You feel the heartbeat of the town pressing at your temples. Your insides somersault into a clarity so cold it numbs: there is a smoking clause"
    "in the appendix that proves preferential selection tied to a private investor who stands to gain enormously if the seawall goes up on a particular line. There is also a clause—buried—that shifts contingent financial liability to"
    "the town under a set of realistic scenarios."

    "You can see the headline already" "Town Investigates Seawall Deal; Funding Uncertain."
    "You stand, palms flat on the table, and the room inclines toward you like tidewater. You are the point that will cut the current."
    "You flip the appendix open on the table so everyone can see. The words are small but deadly precise."

    maya_soler "This clause could cost the town—"
    "Lina reaches across, putting a steady hand near your arm—not touching, but offering contact."

    lina_park "We can proceed with process—subpoena, review, temporary moratorium wording. Or we can go public and force accountability.' (Her eyes are sharp.) 'There's no risk-free option here."
    "Arin Kai: (He looks at you, then away.) 'You're the one who found it. People will look to you for how this starts. I want to stand with you. But whatever we do, we need to protect the people we say we're protecting.'"
    "You swallow and hear your pulse in your ears. The red thread in your office, the maps on the mudflat, the memos stamped confidential—they all lead to this moment: speak and possibly fracture the town's immediate lifeline, or withhold and let a possibly corrupt plan proceed."
    "Your mouth is dry. You feel insomnia's residue like grit in your throat. High adrenaline surges through you, sharpening every sense—the hum of the projector, the particular smell of burnt coffee from an overused pot, the feel of the paper corner against your palm."
    "You think of Evelyn Hart's clipped signature again, the way the memos made everything efficient and tidy—too tidy. You imagine the headlines that could follow and the slow, grinding collapse that might come after a rushed"
    "financial exodus. You also imagine the marsh, the particular stand of glasswort next to the northern spit, the place you measured as a teenager and swore not to let disappear."
    "Silence stretches, taut and humming."
    "You are the fulcrum. The choice sits like a stone in your hand—heavy, cold, impossible to ignore."
    hide lina_park
    hide maya_soler
    hide arin_kai

    scene bg ch10_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Single high string note that holds and fractures]
    "You breathe in, feeling the whole town press in. This is the moment when a single click could send a file into the public vein and the heart of Lira Bay would have to react. Or"
    "when you could close the folder, take counsel, and attempt a quieter surgical strike with legal muscle."
    "You imagine walking away: the appendix back in your drawer, the work continuing in secret—but your conscience will keep tally. You imagine the other path: open hearings, anger, hope, rawness, a public reckoning that might save the marsh or break the town."
    "Every scenario is ruin and rescue braided together."
    "You place your hand on the appendix and, for a moment, let the paper warm against your skin."

    scene bg ch10_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Crescendo — strings, a low brass note, and then silence]

    scene bg ch10_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter11
    return
