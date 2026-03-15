label chapter17:

    # [Scene: Saltwren Commons | Morning — hours after the leak]

    scene bg ch13_f05820_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense, urgent strings with tight percussion; tempo quickens]
    # play sound "sfx_placeholder"  # [Sound: Camera shutters, distant shouted questions, a phone buzzing with rapid notifications]
    "You wake to the smell of brine and diesel. Salt and compost; the Commons’ thin sweetness—then the edge of something metallic from the press trucks idling at the lane. Your phone is a small, insistent drum in your hand: messages, emails, a lawyer’s terse line, a screenshot forwarded by Rae."
    "Rae Carter is already pacing the boardwalk, teal undercut bright against a gray sky. Her hands move like someone trying to pin an avalanche down with tape. Tommy is at the water’s edge, sleeves rolled, jaw set; the fishing community chatter is tight, wary."
    show rae_carter at left:
        zoom 0.7

    rae_carter "They put the papers online before dawn. All of it—transcripts, internal memos. People are saying the developer ghostwrote the feasibility studies. National feed picked it up. Mara—"
    "You keep your voice measured because your pulse is not."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Show me."
    "Rae Carter shoves her phone toward you. The headline crawls across the screen, loud and clinical. The leak paints everything in blame: emails between project planners, redlines, a memo that reads like a promise—promises to expedite"
    "approvals, language about 'acceptable externalities.' Your name drifts through the feed in comments—accusations, support, pity."
    "Tommy: (quiet) 'They'll run with anything that makes someone look like a villain. We need to say something. We need to be first with the facts.'"
    "You feel the Commons’ wooden slats underfoot—damp, giving—but your knees don't. Hundreds of small hands built this place: yours included. The thought of it becoming a headline—reduced to a byline and a hashtag—feels like someone setting a match near the compost piles."

    menu:
        "Step forward and give a short statement to the first crew":
            "You catch Rae’s eye and walk to the camera. Your words are concise, edged: you name the town’s facts and frame the leak as evidence to support the injunction. The crew’s questions multiply like gulls."
        "Stay back and organize the team quietly":
            "You pull Rae aside and make a list: who manages social posts, who rings the legal team, who reads the leak line-by-line. It’s methodical, small, and it steadies the people around you."

    # --- merge ---
    "The scene resumes with the arrival of Elias and the unfolding media attention."

    rae_carter "Good. Keep it tight."

    rae_carter "Okay — that’s the plan. We can breathe through this."
    "Footsteps on the boardwalk announce Elias. He looks like he has been awake for a long time; the light in his eyes is small and raw. He keeps his hands in front of him, holding a tablet and a stack of printouts. His expression is complex—earnest, but boxed-in by constraint."
    show elias_navarro at center:
        zoom 0.7

    elias_navarro "I just spoke to Amina. She's… coordinating statements with the institute. She says the technical team is willing to be subpoenaed if it comes to that.' (He takes a beat.) 'Mara, I—"
    "You don't let him finish with platitudes."

    mara_lin "We have a judge’s tentative pause, brief as it is. The leak will make the counter-narrative louder. Celeste’s PR will frame us as obstructionists. We have to own the frame or it becomes someone else's truth."

    "Elias Navarro (patient, trying)" "Then let's shape it together. I can publish the raw models, the monitoring data. Amina can validate it publicly. We can make it about the science—"

    mara_lin "It’s never only about the science."
    "You cut in."

    mara_lin "Place has memory. You know that."
    "Elias searches your face and finally nods, slow and almost apologetic. 'I know. I'm trying not to forget that.'"
    hide rae_carter
    hide mara_lin
    hide elias_navarro

    scene bg ch13_f05820_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low roar of a distant engine—somewhere farther, a crowd starts forming near the promenade]
    show rae_carter at left:
        zoom 0.7

    rae_carter "There are vans outside Town Hall already. Celeste’s camp is mobilizing—her representatives are on air. They’re calling for the pause to be overturned. They call it 'stagnation blocking progress.'"
    "You feel the tempo tighten in your chest. The leaks shifted the chessboard into a bonfire. People with real needs—neighbors worried about rent, fishermen wondering about permits—call you and listen for an answer. The phone is hot against your ear."
    # [Scene: Media Coverage Montage | Various — rolling clips]
    hide rae_carter

    scene bg ch13_f05820_3 at full_bg
    # play music "music_placeholder"  # [Music: Pulsing electronic beat; anxious staccato]
    # play sound "sfx_placeholder"  # [Sound: Overlayed broadcast snippets and text overlays]
    "Anchor Voice 1: (clip) '—documents suggest a coordinated push to soften environmental review—'"
    "Anchor Voice 2: (clip) '—developers say the promenade will bring jobs, significant economic uplift—'"
    "Social Clip: (overlayed text) 'Whistleblower documents leak. #SaveSolhaven trends.'"
    "You watch a loop of Celeste speaking on a live feed—her tone practiced, hands steady as she frames the project as a deliverable: jobs, infrastructure, certainty. The camera eats her polish; it loves the arc of a savior narrative."
    "Celeste Park: (clip) 'This is not about profit at the expense of place. We are building resilience for the whole region—'"

    "Voice in the comments" "If this gets held up, more businesses leave. We can't wait for marshes to save us."
    "The comments below the feed are splintered, harmonic at one end and sharpened to hate at the other. Your inbox fills with legal notifications: filings against the developer, counter-filings. A media outlet posts a document with"
    "redacted names; a local columnist tweets that your movement is 'emotional.' The national echo chamber converts nuance into binaries."
    # [Scene: Saltwren Commons | Midday — small cluster near the old bench]

    scene bg ch13_f05820_4 at full_bg
    # play music "music_placeholder"  # [Music: Low, insistent percussion; heartbeat-like]
    "Dr. Amina Bhatt arrives with a satchel full of printouts and an exhausted, pragmatic face. She hugs Elias briefly, then turns to you; there’s an unspoken apology in the way she looks at the Commons."
    show dr_amina_bhatt at left:
        zoom 0.7

    dr_amina_bhatt "I’ve been on the phone with the institute's legal team. They recommend we prepare for aggressive discovery requests. They also recommend we publish certain baselines—transparency reduces suspicion, it can blunt the sensationalism. But transparency can also be weaponized."
    show mara_lin at right:
        zoom 0.7

    mara_lin "How long before the hearing?"

    dr_amina_bhatt "This afternoon. The injunction hearing is—what, three? Two? —the council called an emergency session after yesterday's filings splashed online. The national outlets are already calling for statements. Celeste's camp is pushing for a quick vote to override the pause; her lawyers filed motions this morning."
    "Elias Navarro: (quiet) 'They're framing oversight as delay. They're saying the injunction threatens jobs.'"
    "You taste copper."

    mara_lin "They'll say anything to get the wall poured. We have to make sure oversight looks like safety, not obstruction."

    dr_amina_bhatt "We’ll testify. I'll give technical context. But you—' (she softens) '—you’ll have to carry why local ecology matters in people's daily lives. Scientific data doesn't tell the whole human story."
    "You close your eyes for a second, feeling the Commons’ grasses whisper under wind. The memory of your sibling—mud in the hem of their coat, wind roaring—slides across your vision like a filmstrip. That grief is a coal you carry, hot and dangerous. It makes your jaw set."
    "Rae Carter comes up beside you, voice low but fierce. 'People want to show up at Town Hall. They want to be seen. I can move some folks down there. But it could get ugly. The feeds will frame any protest as chaos.'"
    "You consider options for half a second—flash decisions, the reflexes of organizer training—and then make a small, careful plan. The rising tide of attention is not something you can push back; you have to steer it."

    menu:
        "Ask Rae to coordinate a peaceful human chain outside Town Hall":
            "Rae nods, already picturing recycled signs and a ring of neighbors with tea flasks to show calm solidarity. She smiles a quick, tight smile and begins messaging."
        "Tell Rae to focus on social media narratives and keep people safe at the Commons":
            "Rae's face tightens with frustration for a beat, then she bends her head to her phone and begins drafting a thread—careful facts, comforting language, resources for legal aid."

    # --- merge ---
    "The plan is set and the group prepares to move toward Town Hall."
    "Elias Navarro: (low) 'Whatever we do, don’t let this become about personalities. We need to force the optics back to process—facts, oversight, safety.'"

    mara_lin "We also can't pretend we're untouchable. People lost home here. People died. We are not abstraction."
    "Elias meets your gaze as if trying to reconcile two maps of the same place."
    # [Scene: Town Hall & Council Chamber | Afternoon — packed hearing]
    hide dr_amina_bhatt
    hide mara_lin

    scene bg ch13_f05820_5 at full_bg
    # play music "music_placeholder"  # [Music: Full orchestra swells to a sharp, urgent crescendo; timpani rolls]
    # play sound "sfx_placeholder"  # [Sound: Microphone feedback, murmurs rising into shouts, an occasional gavel rap]
    "You cross the floor of Town Hall and feel the cool institutional air—too clean, fluorescent. The building smells faintly of coffee and printer toner and the residue of many small bureaucratic battles. Cameras draw lines of"
    "light over faces. A bank of microphones stands to the side; lawyers have clipped their pads together with the efficient ferocity of predators."
    "Celeste Park’s team arrives like a wave—polished counsel, clipboards, a small stack of polished talking points. She enters with the calm of someone who has rehearsed storms and enjoys bending them into windless plans. When she sees you, the tilt of her smile is measured."

    "Celeste Park (public, smooth)" "Solhaven deserves certainty. We respect the Commons—this project will incorporate public spaces. But we can't allow a small group to halt regional renewal."
    "You feel the room lean with her. Cameras drink it in. Her voice is practiced in the way of people who learned persuasion as craft."
    "Developer's Lawyer: (stands and summarizes motions) 'The injunction is overbroad, they claim; the relief sought is prejudicial to economic stability.' The council listens. The judge, gray-haired and patient in an institutional way, calls order. But the order flaps in the wind of a thousand cellphones."
    "A civil lawyer for your side stands and unfolds the leak into the room: sworn affidavits, emails, suggestions of editorializing in the internal review. The counsel’s voice is clipped, urgent. She paints a picture of expedited approvals, of risk downplayed."

    "Lawyer" "We are not anti-development. We are anti—procedural manipulation that discounts local knowledge and human safety."
    "Celeste's counsel: (countering) 'There is a cost to delay. We have obligations to investors, to employees. The development includes adaptive engineering. These are not mutually exclusive goals.'"
    "The press picks up the sparring. Microphones thrust like probing fingers. A national network cuts to a live panel: two commentators, the clip of Celeste, an on-screen graphic demonizing 'obstructionist locals' versus 'visionary investors.'"

    scene bg ch13_f05820_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Heartbeat overlaid with the muffled echo of legal terminology]
    "Dr. Amina Bhatt is sworn. Her testimony is technical, but her voice carries a human steadiness. She lays out baseline models, sediment stability metrics, possible failure modes. She uses the words 'uncertainty' and 'probability' and shoulders"
    "them with fairness. She also names what the numbers cannot carry—the centuries of living memory in tidal patterns, the way families orient to specific coves."
    show dr_amina_bhatt at left:
        zoom 0.7

    dr_amina_bhatt "Models are tools. They depend on assumptions. When assumptions are financial or political rather than empirical, their outputs are compromised."
    "Celeste Park stands to rebut and the room tightens like a fist. She speaks of mitigation plans, of engineered assurance, of contingency funds. Her words fall into applause in pockets of the room—local small-business representatives nod; an older man in the front row claps once and looks relieved."
    "Elias Navarro testifies in the middle of all this. He reads, measured, from the joint assessment he and Amina assembled—technical language, but sprinkled with concrete examples: who is displaced by a failed shoreline, what flood shelters look like, how adaptive designs can be phased."
    show elias_navarro at right:
        zoom 0.7

    elias_navarro "There are engineering pathways that incorporate living shorelines. But phasing requires time and oversight. Abrupt fast-track implementation increases risk."
    "Celeste Park: (after Elias) 'My team has modeled staged implementation. We can bond against structural failures. There is a fiscal plan.'"
    "Your counsel leans into the leak documents and threads a narrative: the documents suggest pressure to minimize review. There is a murmur—a wave that rises and cracks. Celeste’s face tightens. She looks at you then, and for the first time there is a flash—something like calculation and then resolve."
    "Outside, Rae Carter organizes a human chain. The cameras that entered with us now broadcast the human ring of neighbors. The images are raw: people holding hands, a grandmother with a placard, a child asleep against"
    "a shoulder. The editorial lines begin to split—some commentators call it staged, others call it real."
    # play music "music_placeholder"  # [Music: Sudden drop to a single, taut violin note; then drums kick in, relentless]
    # play sound "sfx_placeholder"  # [Sound: Phones exploding with notifications; a reporter whispers into a live mic; a moderator's gavel tries to restore order]
    "A new filing arrives mid-hearing—served electronically, pushed to the clerk’s inbox. The judge pauses, the clerk reads its title out loud. It’s a countersuit from the developer alleging defamation tied to the leaked documents and signaling"
    "an intent to seek damages for delay. The atmosphere tilts; it's now not only a zoning struggle but a legal war with money and reputation on either flank."
    "You feel your throat close. The energy in the room spikes, braided with fear and ferocity. People shout; cameras jerk. The judge announces a recess to consider the new filings. In the hallway, anchors mill like vultures."
    "Elias Navarro catches your sleeve as the throng moves. 'Mara—' he says, voice thick. 'They'll try to make you the face of this. They'll make you personal so they can avoid the structural questions. Be careful.'"
    show mara_lin at center:
        zoom 0.7

    mara_lin "They already did. Look at the feeds."
    "Elias Navarro: (frustrated, softer) 'I know. I just—' He stops, then forces a breath. 'I want to be with you on record. But if they subpoena institute personnel, it will change the scope. The legal team may ask for labs, for raw data. We have to be ready.'"
    "Mara Lin: (a rasp) 'And if they open discovery on the Commons' private correspondences and community messages? People will be exposed. We will be exposed.'"

    elias_navarro "We can push back. We can limit the scope. We can—"
    "You want to tell him not to rationalize another escalation into policy language; you want him to hold you; you want him to pick a side that isn’t only a method. Instead you press your fingers"
    "into your palm and remember the feel of the rooftop after a storm—the salt spray, the way the town smelled when it had a memory of being rebuilt. That memory is brittle and fierce."
    # [Scene: Town Hall Corridor | Recess — clump of allies around you]
    hide dr_amina_bhatt
    hide elias_navarro
    hide mara_lin

    scene bg ch13_f05820_7 at full_bg
    # play music "music_placeholder"  # [Music: A relentless undercurrent; dissonant chords]
    # play sound "sfx_placeholder"  # [Sound: Low, urgent conversation; a camera crew setting up outside the doors]
    "Rae Carter: (urgent) 'How do we keep the narrative from splintering? If Celeste's lawyers frame this as defamation, the town could be ordered to pay damages or be gagged. We could lose a lawsuit and lose voice.'"
    "Lawyer [Your Counsel]: (practical) 'We prepare for protective motions. We redact sensitive private messages. We prepare witnesses to delineate collective actions from individual rhetoric. But litigation is slow and cold. It eats momentum.'"
    "Tommy: (angry) 'So, we fight bank to bank while the sea comes closer? That’s what you want?'"
    "You feel the ground under the town shift. The hearing will decide legal standing for the pause. It will also fold into the media narrative: either the town secures oversight and scrutiny, or the developer wins an expedited green light. The stakes coil through your chest."
    "Elias Navarro: (quiet) 'There is another thing. The institute—some of their donors are national. If this goes national, it will bring not only attention but pressure. That pressure can be helpful—funding, oversight—but it can also become leverage against local autonomy.'"
    show mara_lin at left:
        zoom 0.7

    mara_lin "Leverage is a weapon that cuts both ways."
    "Dr. Amina Bhatt: (measured) 'We must prepare clear evidence, a chain of custody for the leak, and community testimony that cannot be dismissed as 'emotional.' But when the cameras ask a human question, we must have human answers.'"
    "Your phone buzzes again; a new clip cycles: a pundit calls the injunction 'eco-nannyism' and features a rapid montage of local businesses voicing fear. The clip is designed to put the town in a no-win frame: economy OR environment, urgency OR caution."
    # play music "music_placeholder"  # [Music: The percussion ramps; violins seethe; a cymbal crashes like surf breaking]
    hide mara_lin

    scene bg ch13_f05820_8 at full_bg
    "You steadied your breath. The room refocuses; the judge calls the hearing back to order. Everyone returns to their places. You take a seat near the front because the world seems to need an anchor close"
    "to the judge. You look at Elias—his jaw is clenched, his hands flat on a stack of papers like a promise. Across the room, Celeste sits with a composed mask; her fingers tap a rhythm that"
    "matches the underlying drums in your chest."
    "The judge adjusts his glasses, looks down at the new filings, and then looks up at the packed chamber. The list of possible outcomes—further injunctions, tightened oversight, an order to lift the pause for 'economic harm'—hangs"
    "in the air like a storm cloud. The public and legal narratives have braided into a single noose of pressure."
    # play music "music_placeholder"  # [Music: Full, relentless crescendo; the tempo now mirrors the quickness of a raced pulse]
    # play sound "sfx_placeholder"  # [Sound: The room hushes; even the cameras' shutters slow as if listening]
    "You feel everything pressing forward—proof, testimony, grief, rhetoric—on a single hinge. The judge's next words will not only influence a construction timeline; they will change the tenor of national discourse for Solhaven. They will decide whether"
    "oversight becomes an incorporated part of the project or whether the pause becomes a footnote."
    "You taste salt and metal on your tongue. Your hands are not steady. Your mind loops between legal strategies, community safety, the possible human costs of a failed fast-track. The hearing breathes in. The judge looks"
    "at you, then at the lawyers, then at Celeste and you. He clears his throat."
    "You know the decision will come down to what the court believes is possible to prove right now—and what it fears will unravel if it waits."

    scene bg ch13_f05820_9 at full_bg
    # play music "music_placeholder"  # [Music: A single unresolved chord held, electricity in the silence]
    "You inhale, preparing for whatever comes next—the gavel, the call to order, the moment that will push everything into the open."

    scene bg ch13_f05820_10 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter21
    return
