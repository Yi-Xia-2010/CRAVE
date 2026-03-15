label chapter12:

    # [Scene: Hana's Diner | Morning]

    scene bg ch12_e67f19_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low radio chatter, clatter of cutlery, a distant gull]
    # play music "music_placeholder"  # [Music: Quiet, minor-key piano; low strings sustain]
    "The bell above the door tinkles when you push it. Heat and the smell of strong coffee and bacon press against your face like a damp cloth. The diner is louder than it usually is at"
    "this hour—voices knit with relief and the brittle edge of triumph. A cluster of people by the counter are peering at a cracked phone screen; the headline blares in quick, bright font: LUXCORP TERMS LEAKED —"
    "LOCAL ACTIVISTS EXPOSE CLAUSES. For a moment the world narrows to that glow."
    "You feel the cheer inside you rise and then fold into something colder. The victory tastes like pennies. People grin at you, slap your shoulder. Hana is behind the counter, wiping her hands on her apron, eyes bright but tired."
    show hana_kim at left:
        zoom 0.7

    hana_kim "Did you see? You did it. They look—' (she shakes her head, laughing sharp) '—they look like they swallowed a gull."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "We did it together."

    "Neighbor" "About time someone pulled the curtain back."
    "You meet their eyes—faces you grew up beside—and for a few seconds you let the relief settle. It feels like vindication: the town's suspicion, the late-night meetings with paper copies and whispered readings, the quiet anger that kept you awake. The headlines confirm the shape of what you already feared."

    menu:
        "Smile and accept the praise":
            "You give a tight smile and nod. The warmth hits your ribs like a hand; for now, it's enough."
        "Keep your head down and listen":
            "You sink into the booth, listening instead of answering. Voices fill in the room—some hopeful, some fearful—and you calibrate each tone like a sensor."
        "Check your phone for follow-ups":
            "You pull your phone; notifications bloom. The cheers are joined by an undercurrent—emails flagged urgent, a terse message from the Mayor. Your chest tightens again."

    # --- merge ---
    "The diner quiets into a hum of conversation as Hana leans in and lowers her voice, the island of carefulness holding."
    "Hana leans in, lowering her voice. The diner, for all its good cheer, is an island of carefulness."

    hana_kim "You know they'll spin this. They'll call it sabotage, or worse—necessary tough decisions. People are scared, Maya. They want roofs and sandbags, not editorials."

    maya_inoue "I know.' The words wear grooves from being repeated in your head. 'But if those terms mean they'll take the shoreline or control who can fish where, then a 'solution' isn't a solution."

    hana_kim "I know.' She pushes a plate toward you. 'Eat. You'll need something solid when the town turns to you with questions."
    "You pick at the food, tasting salt and smoke. Outside, rain lashes the promenade; the radio downstairs announces a LuxCorp statement on loop—calm, polished, words arranged to soothe. It doesn't soothe. Underneath the official voice, you"
    "hear the sudden, brittle clack of retreat—investors called a meeting. There's a word that hums in the back of your mind: withdrawal."
    # [Scene: Harborfall Promenade / Town Square | Midday]
    hide hana_kim
    hide maya_inoue

    scene bg ch12_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The clack of rain on metal, the murmur of passing crowds, a distant ambulance wail]
    # play music "music_placeholder"  # [Music: Low cellos, a steady, bone-deep rhythm]
    "By noon the town has clustered into pockets of conversation. Phones are out, pages flipped, posts shared. You move through faces—some flush with triumph, others creased with worry. The municipal kiosk cycles LuxCorp's polished statement beside"
    "clips of your town hall uploads. The juxtaposition feels obscene; the infinite calm of corporate speak against the raggedness of living rooms and boats."
    "You see Mayor Elena first, framed in the middle of a ring of council aides and a reporter you've seen at every vote. She holds a printed memo at her chest like a fragile shell. Her"
    "jaw works; the municipal pin on her lapel glints. She looks older than the morning."
    show mayor_elena_rossi at left:
        zoom 0.7

    mayor_elena_rossi "They—investors have called off some of the regional funding. They're 'reassessing exposure',' (she says the phrase as if tasting something sour). 'They think we're now a political risk."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "They'll come back if we negotiate,' you say before you think, the planner reflex surfacing. 'We can—there are conditional offers, staged disbursements. We can readjust the timeline."
    "Mayor Elena: (a sound like a small laugh, not happy) 'And sign away oversight? The clauses are still on the table, Maya. The headlines don't reopen options; they harden positions. The funders are afraid, and when investors are afraid, money moves faster than the sea.'"
    "You step closer, rain soaking the hem of your jacket. Salt wind tastes like iron on your lips. The town listens—ears tuned to the conversation that might decide policy, livelihoods. This is no longer abstract; it's budget lines, payrolls, and the municipality's ability to pay contractors for the berm work."

    maya_inoue "So what—do we roll back the leak? Try to placate them? We can't un-know what we know."
    "Mayor Elena's fingers curl around the memo. Her eyes flick to the kiosk screen where LuxCorp's spokesperson smiles with an unreadable tilt."

    mayor_elena_rossi "You don't get to decide what investors feel, Maya. You only get to decide whether this town can weather what comes next. If funding collapses, we don't just lose convenience; we lose the capacity to act when the next storm comes."
    "The word 'capacity' lands like a stone. For a heartbeat, you see the arithmetic of it: payrolls, emergency pumps, the slow buying of sand—all of it attached to lines on a ledger that can be cut."

    menu:
        "Argue that transparency must come first":
            "You say that transparency is the only sustainable base to build on; without trust, engineered solutions will always be brittle."
        "Push for immediate contingency funding":
            "You press the mayor to open an emergency contingency—crowdfund, alliances, anything to buy time. Elena's mouth tightens; time is the one thing neither of you have in abundance."

    # --- merge ---
    "The reporter presses forward with a question that crystallizes the public moment, and Mayor Elena looks to you for a shared reflection."
    "A reporter presses forward, mic extended."

    "Reporter" "Mayor, will the town now reject LuxCorp outright?"
    "Mayor Elena: (softly) 'We have to give people a choice that isn't shaped only by fear of loss or fear of losing funding. We have to make the referendum about what we want our shore to be—not a referendum about who's right in an abstract fight.'"
    "You nod because you know she isn't wrong. But you also know that winning a referendum means winning a war of narratives—against glossy ads, against people who will show up with contracts and promises and jobs."
    # [Scene: Kaito's Field Lab (Workshop) | Afternoon]
    hide mayor_elena_rossi
    hide maya_inoue

    scene bg ch12_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft hum of equipment, Kaito's camera's faint whir as it processes footage]
    # play music "music_placeholder"  # [Music: Sparse piano, low synth—an anxious, hollow sound]
    "Kaito Sato stands at his desk with an image frozen on the screen: an empty lot where volunteers used to plant native reeds, a soggy field of footprints that stop in the mud. His fingers hover above the keys as if waiting for something to break the stillness."
    show kaito_sato at left:
        zoom 0.7

    kaito_sato "I set the camera to time-lapse. For two weeks it's been full of hands and forks and laughter.' He exhales sharply. 'Yesterday it's... this."
    "You lean closer. The frame shows a small sea of disturbed soil and a forlorn few scattered across it. A banner from the education drive is sagging against a fence. Where once there was motion and commitment, there is vacancy."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "Why did they leave?"
    "Kaito Sato: (rubs his temple) 'Someone confronted a volunteer group about the leak. They said—' (he stops, looking for the right words) '—they said we were the reason the funding pulled out. Some asked if we'd knowingly destabilized contracts to ‘score points.’'"
    "You feel a fuse of something hot and sharp. You want to tell him you did what you believed was necessary. You want to tell him that not exposing the truth would make future repairs impossible"
    "to trust. Instead you find your hands closing around your brother's watch in your pocket. The metal is cold again. It is a compass that points toward both past storms and present consequence."

    maya_inoue "Did they blame you too?"
    "Kaito Sato's sea-green eyes go flat with worry. He looks at you as if the light in the lab has been turned down."

    kaito_sato "Some did. Some thanked us. Some—' (he rubs a hand over his face) '—some said they don't want to be on the side that scared the money away. They worry about their kids' roofs more than they want moral clarity."

    maya_inoue "And the camera…?"

    kaito_sato "Recorded the lot at dawn. I wanted to capture the work, not the aftermath. Now it's on record. It'll be useful for grant applications—proof that we started something—but a single photo won't fix the immediate gap."
    "You stare at the image until the pixels blur. The idea of a small lot, once full of hands, empty because of a headline—it's like seeing a leak in a boat that used to keep you afloat."
    "Kaito Sato reaches across the bench and puts a hesitant hand on yours."

    kaito_sato "We did what we thought was right. But I—' (he falters, then steadies) '—I don't want this to make things worse for people who can't afford it."

    maya_inoue "I don't either."

    menu:
        "Apologize to Kaito for the fallout":
            "You say the words aloud—'I'm sorry'—soft and precise. Kaito's shoulders drop an inch; there's relief in the small opening but no solution."
        "Stand firm—defend the leak as necessary":
            "You say that some truths have to be pulled into light, even if the light hurts. Kaito listens, jaw working; he doesn't disagree, but you both know the cost."

    # --- merge ---
    "You and Kaito sit in the hum of the lab, the town's slow leak mapped in your hands and in the watch you carry."
    "Kaito looks at your hand on the watch. A corner of his mouth lifts, near-sad."

    kaito_sato "He would've wanted the truth to be clear, wouldn't he?' (he nods toward the watch) 'Your brother."

    maya_inoue "He would've wanted people to be safe.' The sentence arrives like a small ledger balancing—safety and truth weighed against each other. 'He also wouldn't have wanted us fighting each other in the meantime."
    "You both sit in the hum of the lab. Outside, Harborfall moves—people huddled under umbrellas, council cars arriving at the municipal building, the distant scrape of a truck that might be hauling away equipment when budgets are recalculated. The town breathes and waits; the wait feels like a slow leak."
    "Your internal voice maps the consequences like tide-lines: headlines will spread, funders will pull, contractors will idle. Friends will grate against one another at grocery counters. The moral clarity that once shone like a beacon is"
    "now a rationed commodity—passed around in small pieces that don't fully warm the hands they touch."
    "You close your eyes for a second and the watch rests heavy against your palm, a small, constant recall of the price you willingly, painfully paid for truth."
    "You stand and move toward the door, the lab light cutting your shadow long across the workbench. The town is pivoting; the referendum is now a referendum on trust itself—trust in you, trust in each other,"
    "trust against the convenience of quick fixes. Your chest tightens with a knowledge you can't put away: headlines don't plug breaches. Papers and proof do not build berms. They change the terrain of who will be"
    "willing to invest time, money, and risk."
    "You step back out into Harborfall's salted air. The rain has picked up, slicing the promenade into silver threads. Somewhere, a LuxCorp spokesperson's voice continues to rehearse calm. Investors are on calls you will not hear."
    "The town murmurs, divides, and tries to steady itself on the little things that still hold: a diner stove, a volunteer's shovel leaning against a fence, a lighthouse's weak beam. Your brother's watch ticks on your"
    "wrist, each second a tiny, impartial count."
    "You think of the referendum, the market square, the people you might have pushed away and the ones who now applaud you from the diner booths. You cannot undo the leak. You can only measure what"
    "you will do next with the truth you've opened—measure against time, against storms, against the prickle of headlines that now determine budgets."
    hide kaito_sato
    hide maya_inoue

    scene bg ch12_e67f19_4 at full_bg
    # play music "music_placeholder"  # [Music: A single cello note held and then released into silence]
    "You inhale and feel the cold gather in your lungs—the town's fear, its brittle triumphs, the possibility that exposing a lie might become the reason a pump isn't bought. The next hours will be loud. The"
    "next days will be louder. You understand, with the clarity of someone who has been close to loss, that righteousness does not automatically equal readiness."
    "For a moment you let yourself imagine the worst and the kindest outcomes at once: the town rallied and resourced, or the town watched budgets tighten and felt the saltwater rising without enough hands to hold it back. Both futures sit in your bones like two tides."
    "You pick a path forward because there must be one, and because leaving the town to the tides is not an option you can live with. But you also feel the gravity of what you've set"
    "in motion—the quiet un-making that follows an act of revelation. The town will applaud you in some corners; in others you will be the cause of the silence."
    "The rain turns harder, drowning the distant gulls. You close your eyes and listen to Harborfall as if it's a body with a fever. Somewhere close, a child asks a parent what the headlines mean."
    "You hold your brother's watch one last time before you tuck it into your pocket. The metal is familiar; the storms it has counted are not over."

    scene bg ch12_e67f19_5 at full_bg
    # play music "music_placeholder"  # [Music: Low, resigned strings]
    "A press van pulls into town. The municipal kiosk scrolls names you recognize and accusations you don't. The town gathers itself for the moment that will determine whether we are the small-town heroes who uncovered corruption—or"
    "the group that scared away money that could have bought life-saving infrastructure. You stand at the edge of that possibility, listening to the sound of an argument that hasn't resolved yet."
    "The rain keeps falling."
    # [Page-Turn Thought: You think of the referendum board, of the town square, of the crowd that will want simple answers. You think of LuxCorp's unreadable posture and of investors calculating risk. You think of Kaito's empty lot and of Hana's diner warmth. You think of your brother's watch ticking, counting storms you cannot turn away from. This is not the end of who you are—it is the moment when the world names you and waits to see whether naming will make you whole or hollow.]

    scene bg ch12_e67f19_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter16
    return
