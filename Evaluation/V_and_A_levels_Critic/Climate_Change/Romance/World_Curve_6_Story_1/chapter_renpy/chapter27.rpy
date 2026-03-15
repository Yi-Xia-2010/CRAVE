label chapter27:

    # [Scene: New Promenade | Morning — After the Surge]

    scene bg ch13_762cd5_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant sirens cut, gulls, the hush of water retreating; soft clink of metal against metal.]
    # play music "music_placeholder"  # [Music: Low, steady cello with a minor key — a slow, persistent pulse]
    "You stand with the cool of the new promenade under your palm, the stone still smelling faintly of salt and diesel. The wall is immense and honest in its indifference. It did its job; the tide"
    "broke against it and did not cross. You can feel the city’s gratitude like a light pressure in the air — municipal banners, news drones skimming the horizon, anthemic headlines on the digital billboards farther inland."
    "Safety, measured and announced."
    "But the safety is a braided thing with other threads you cannot unweave. The promenade's surface tucks warmth into your scuffed boots, and beneath that a cavernous ache opens in your chest where the Low Row used to be whole."
    "You remember the surge: the way the water heaved, the way the sensors blinked before the noise. You remember the neighbors lined up, faces lit by phone screens and floodlights, the way Rafi's voice cut through"
    "the chaos. The wall held. People lived. That is an iron fact. And still—there are shuttered doorways, storefronts sagging on one side, a playground only half intact. The cost is visible in the angles of things"
    "that used to be right."
    "You press the trefoil at your wrist through the sleeve of your jacket. The metal is cool. You let your fingers curl around nothing and everything."

    scene bg ch13_762cd5_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmurs, camera shutters; a politician's distant congratulatory speech plays through a loudspeaker]
    # play music "music_placeholder"  # [Music: Cello sustains, held tone; the low pulse continues]
    "You watch a municipal representative pose with engineers in slate vests. The photograph will circulate: smiling faces framed by the seawall's curve. Your name will be a footnote at best; your work will be translated into"
    "a line in a press release. You taste copper and salt and a hardness settles behind your eyes."
    # [Scene: Temporary Fences and Relief Center | Midday]

    scene bg ch13_762cd5_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low conversation, a child's muffled crying, the rustle of tarpaulins; boots on gravel.]
    # play music "music_placeholder"  # [Music: A thin violin thread under the cello, quiet but persistent]
    show rafi_odeh at left:
        zoom 0.7

    rafi_odeh "You made it to the promenade. Good. We had to reroute the supply trucks—flooded half the access strip. I've got twenty families in the community center and three small businesses marked as 'uninhabitable' for now."
    show maya_corvin at right:
        zoom 0.7

    maya_corvin "Who needs immediate shelter? Who's been separated from family?"

    rafi_odeh "The Delgado fish stall—gone. Mrs. Ortega's storefront—two floors washed out on the back. Lio's mural crew found two neighbors clinging to their roofs overnight; pulled them to the bakery roof. We're tracing the rest."

    maya_corvin "Bakery roof—who's coordinating medical checks? Heat exhaustion sets in fast after a shock like that."

    rafi_odeh "Ana's got medical volunteers, but we need a water shuttle and translators. And—' He lowers his voice, exhausted with both hope and a practical cruelty. 'The municipal buses are filling with offers to take families north. Some don't want them to leave the neighborhood; others are terrified. We need to respect both."

    maya_corvin "I'll tag-team the registry and help Lio with the mural schedule. The mural needs faces and names—something fixed, something that remembers."

    rafi_odeh "And you'll keep chasing the clauses in those contracts. We need your voice at the meetings. But first—' He hands you a clipboard, the paper damp at the edges. 'Go. Paint. Sort. Listen."
    "You take the clipboard. The paper smells of dust and tea and something metallic, the smell of people who have slept under tarps and are still arranging their grief into action."

    menu:
        "Help Lio paint the memorial panel":
            "You kneel in the dust beside Lio. Your hand is clumsy with color at first; he guides your strokes, and for a little while grief becomes shape."
        "Head to the registry to organize shelter":
            "You fold the clipboard around names and numbers and step into a corridor of voices. You hand out assignments, your voice steady like a lever."

    # --- merge ---
    "Continue"
    # [Scene: Low Row — Walking the Damaged Streets | Late Afternoon]
    hide rafi_odeh
    hide maya_corvin

    scene bg ch13_762cd5_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant tapping of a spray-can, a generator idling, a radio reading out names; the smell of wet wood, algae, old paint.]
    # play music "music_placeholder"  # [Music: Cello with a low piano—melancholy, careful]
    "Lio wipes his hands on an old rag and doesn't look up when you approach. His face is lean, eyes shadowed; there is an age in his posture you didn't expect."
    show lio_corvin at left:
        zoom 0.7

    lio_corvin "You coming to help or to sit and style the facts for the cameras?"
    show maya_corvin at right:
        zoom 0.7

    maya_corvin "I'm here to help line the names. Not for cameras."

    lio_corvin "Good. Then pick up a brush. And talk to Elias when you can—he'll be at the municipal oversight point. He came by earlier but left. Scared he'll be swallowed by schedules, I think."

    maya_corvin "He said he'd stay. He said he'd help."

    lio_corvin "He said a lot. We all say a lot. He also said he'd accept the new oversight role. Means he'll be in the meetings he used to fight for us from the back of."
    "You taste the word accept like a bitter herb. You know what 'accept' can mean: the slow trade of immediacy for paper, of protest for protocol. Elias's amber eyes have always been a place you could"
    "anchor a discussion; now they are a mirror for a city-scale compromise you do not fully trust."

    maya_corvin "Did he say why?"

    lio_corvin "Said he can push changes from the inside. Or that he's tired. You decide."
    "You crouch by the mural’s edge and steady your hand. The paint is gritty in the heat. You place a small, deliberate leaf beside a painted name—tiny green like the gardens on the rooftops that survived."
    # [Scene: Back Alley near the Construction Access | Early Evening]
    hide lio_corvin
    hide maya_corvin

    scene bg ch13_762cd5_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Hints of machinery, a low argument in the distance; the quiet click of Kai's shoes on stone.]
    # play music "music_placeholder"  # [Music: The cello thins; a higher, metallic string weaves tension]
    "Camila 'Kai' Navarro catches your eye before you reach her. There is something unreadable in her face — a practiced neutrality with a fissure of something like regret."

    "Camila 'Kai' Navarro" "You look like you could use terrible news or company. I can't tell which you'd prefer."
    show maya_corvin at left:
        zoom 0.7

    maya_corvin "Surprise me."

    "Camila 'Kai' Navarro" "They did what they had to. The surge was worse than projections in pockets. The wall held where it needed to. That saved a lot. I didn't build it for glory. I built it to stop people from drowning in the street."

    maya_corvin "And yet the Low Row lost homes. And stores. People are sleeping under tarps. How do you justify that?"

    "Camila 'Kai' Navarro" "I don't justify losses. I calculate acceptable loss given uncertain models and limited time. If I'd waited, more would have died. That's the calculus."

    maya_corvin "Acceptable loss."

    "Camila 'Kai' Navarro" "You're making that phrase mean less human than it is. I spoke with on-site leads this morning. There's dissent. Some engineers refused to sign off on the accelerated seals—we had overtime crews brought in. There are personnel calls for a safe pause that weren't heeded."

    maya_corvin "You mean a strike?"

    "Camila 'Kai' Navarro" "Not a headline strike. A few key engineers stepping away, putting in formal complaints. I kept production running with contingency teams. The work was rushed. People were tired. I'm not defending every choice."

    maya_corvin "How many people were put at risk because of that rush?"

    "Camila 'Kai' Navarro" "We lost two scaffolding leads in an early storm breach. We lost hours of controlled testing. Had the wall been delayed, the hospital at the inlet might have flooded. You ask the wrong question if you ask me to tally blame today."

    maya_corvin "No. You ask the right question if you answer it honestly. Who covered the nasty gaps—who paid?"

    "Camila 'Kai' Navarro" "People did. Workers did. So did neighborhoods. And yes—the project saved the hospital, and yes—some of the worst tidal breaches didn't reach main infrastructure because of the wall. But that doesn't mean it was clean. People were beyond tired. They were pushed."
    "Her candor lands like a pebble in a still pond. Ripples spread: the knowledge of engineers pushed, the human cost that sits in the background of any 'success'."

    "Camila 'Kai' Navarro" "If you want to hold me to account, I will not smooth this. I will tell you what I know: there are reports, emails, and a handful of field logs that confirm exhaustion and shutdowns. I'm not trying to exonerate the company; I'm offering the truth I have."
    "Maya Corvin [internal] Her offering of truth is a narrow, gloved hand extended. It is not apology. It is the kind of admission that leaves you less satisfied and more hollow."

    maya_corvin "Why tell me? Why trust me with this?"

    "Camila 'Kai' Navarro" "Because the public narrative will frame this as a win. Someone needs to know what margins looked like. And because—' She hesitates, and when she finishes the sentence it is oddly small. 'Because I don't sleep well knowing people broke to keep the machine moving."

    maya_corvin "You say you don't sleep well. Then stop the machine from breaking people."

    "Camila 'Kai' Navarro" "I tried. I didn't succeed of all my tries."
    "Her admission is a thin, serrated thing. It does not comfort. It sharpens the edges of your grief."

    menu:
        "Demand those field logs":
            "You push the packet back to her and ask for the logs. Kai's fingers tighten around the folder; she promises to send them through secure channels."
        "Tell Kai to take the logs to Rafi and community counsel":
            "You suggest she hand everything to the community legal team. Kai's face hardens for a second, then she nods, as if deciding you'll be more merciless than the law."

    # --- merge ---
    "Continue"
    # [Scene: New Promenade — Dusk]
    hide maya_corvin

    scene bg ch13_762cd5_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Tides moving away, a child laughing somewhere behind tarps, the soft crackle of a loudspeaker playing a civic address in the distance; breath cold in the air.]
    # play music "music_placeholder"  # [Music: Cello returns alone, slow, as if counting a measured loss]
    show elias_kahn at left:
        zoom 0.7

    elias_kahn "They put the oversight brief in my inbox this morning. It's full of conditions and checkpoints and—' He swallows. 'They want me in charge of compliance. They want someone who knows both worlds."
    show maya_corvin at right:
        zoom 0.7

    maya_corvin "They want someone who will keep them honest."

    elias_kahn "They want someone who will make sure the sensors are on and the reports are filed. Honest is a heavy word. I'm not sure that's what they mean."

    maya_corvin "So you accepted."

    elias_kahn "I accepted a role that gives me a seat where I can push for the monitoring you wanted, for the wetlands clauses to be implemented. I figured—if I'm there, I can keep the worst from being erased."

    maya_corvin "And what if being there means your voice is used to placate us? What if your presence greases the machinery that decides who gets saved and who gets left behind?"

    elias_kahn "I don't want to be a placard in their photo ops. I want to be a lever. You think I'm not exhausted? You think I didn't weigh what it would cost to step away from the meetings?"

    maya_corvin "I think you made a choice that will be easier for the city to put on a poster than to actually hold accountable."

    elias_kahn "Do you think I don't know that? Do you think I'm immune to the compromises?' He takes a breath that trembles. 'I am tired, Maya. I am tired of shouting into open rooms and watching plans vanish into false starts. If I can push changes from within—if I can shepherd pilot clauses and get the wetland corridors recognized—then I have to try."

    maya_corvin "At what cost, Elias? At the cost of being here? At the cost of the very people you promised you'd fight beside?"

    elias_kahn "I didn't take the job to leave you. I took it because I thought it could help us all. I thought—"

    maya_corvin "You thought. You thought for the city and not for us. That's the problem."

    elias_kahn "That's not fair."

    maya_corvin "It is the truth."
    "He looks at you like someone trying to remember how to map soft things onto a hard schedule. There is pleading in his expression now, not from politics but from fear of losing you in the slow attrition of municipal time."

    elias_kahn "Tell me what to do. Tell me where to stand."
    "Maya Corvin [internal] You want to give him directions like a map: stand here, do this, do not make them forget the people. But you also know he will be pulled by policy meetings, by counsel memos, by the inertia that eats vows. Your anger tastes like salt and ash."

    maya_corvin "Stand with the people when it matters, Elias. Not with the press release. We need more than memos."

    elias_kahn "I'll try."
    "You watch him, and the word 'try' feels both fragile and final. He steps back as if to leave, and the space between you hardens. He turns to go, then pauses."

    elias_kahn "If you need me, call. I will answer when I can."

    maya_corvin "I will hold you to that."
    "He leaves. The sound of his footsteps fades into the promenade hum. The distance he steps is small, but the map of your days redraws in that smallness."
    # play music "music_placeholder"  # [Music: The cello holds a single, low note, then eases out to silence.]
    "You stand alone, the city's lights puncturing the dusk. Around you, the neighborhood breathes in uneven rhythms — some inhaling relief, others exhaling loss. The murals dry under lamps; Rafi's tents hum; Lio packs paint away"
    "with a slow, precise care. Camila 'Kai' Navarro's confession knots in your mind: the knowledge of workers pushed too hard, of lives rearranged in the name of saving more lives. Elias Kahn's choice sits like a"
    "bruise."
    "You press your palm to the promenade's rail. The trefoil at your wrist depresses into your skin and the pain is a small precise reminder: there will be work tomorrow. And the day after. Vigilance will"
    "not be a single victory. It will be a labor that frays and must be tended, again and again."
    "You let the weight of what was saved and what was lost settle into you like silt. There is no triumph here. There is no easy consolation. There is only the stubborn fact that people are"
    "alive and the stubborn fact that the shape of your neighborhood is altered. The paradox doesn't resolve; it sits waiting for someone to stay awake with it."
    hide elias_kahn
    hide maya_corvin

    scene bg ch13_762cd5_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A far-off radio reading names of aid drop locations; the tide's last whisper]
    # play music "music_placeholder"  # [Music: A single bowed cello note, long and minor]
    "You pull your jacket tighter against the chill and start to walk back toward the relief center. The day has ended; the work will go on into night. You will shelter, register, argue clauses, attend meetings,"
    "stand in front of cameras, and place names on walls. You will wake and do it again."
    "You think of the clauses still loose in contracts, of the whispered complaints Kai showed you, of the families sleeping under tarps, of Elias signing forms that may keep him away more than they keep him"
    "useful, of Lio's murals catching light in the morning. You feel, in your bones, that survival won today is not the same as justice. You tighten your jaw, press your thumb against the trefoil, and let"
    "the meager, fierce resolve settle: vigilance becomes a daily labor, and you will be there to do it."

    scene bg ch13_762cd5_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter32
    return
