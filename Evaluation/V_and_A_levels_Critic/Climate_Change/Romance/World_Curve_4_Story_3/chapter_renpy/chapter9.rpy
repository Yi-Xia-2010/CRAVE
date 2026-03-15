label chapter9:

    # [Scene: Sea Wall / Boardwalk | Night — Storm]

    scene bg ch9_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Sirens wail in the distance; boards creak; the sea bangs and then bangs again, relentless.]
    # play music "music_placeholder"  # [Music: Percussive, frantic strings—heartbeat tempo; brass stabs on the downbeat]
    "You taste salt and diesel on the wind. Your jacket is soaked; the fabric sticks to your forearms, the Moleskine heavy and useless in your pack. Somewhere beneath the thunder you can hear the scrape of"
    "plywood, the shouted names of people you know. The harbor is not patient tonight. It is hungry and loud and impossibly close."
    "Samir is at your shoulder, camera held aloft like a small, steady lighthouse. His face is streaked with rain and something raw—fear folded into a press-fed focus that keeps him from running. He shoots, breath coming out in visible, frightened clouds, and every frame he takes feels like a ledger."
    show samir_reyes at left:
        zoom 0.7

    samir_reyes "This is— This is worse than the models said last month."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "I know. I know. Keep filming. Record everything. If nothing else, people need to see what happened."
    "Samir stabs his thumb at the live feed icon. 'We're getting calls already. People need water. The shelter at the school—it's—'"

    maya_reyes "Tell them to stand by. I'll try to get a line through to Mayor Delgado. Iris—where is she?"
    "You cannot think in the slow, methodical ways you used to. Plans have evaporated into the rain. Your mind is a cascade of possible failures, each one louder than the sea."

    menu:
        "Push toward the low-lying blocks with Samir to help search and warn":
            "You grab Samir's sleeve and pull. He follows with the camera shaking, voices in the distance growing urgent as you run toward the warren of streets that will take the worst. The smell of wet insulation hits you first—then a child's toy floating face-up in black water."
        "Head to the construction command near the sea wall to coordinate emergency resources":
            "You push through the press and contractors, shouting orders you don't feel sure of. The foreman hands you a radio like an accusation. You try to marshal trucks and pumps; every call reveals another bottleneck."

    # --- merge ---
    "Both outcomes converge at the Construction Command by the sea wall."
    # [Scene: Construction Command, Sea Wall Access | Night — Storm]
    hide samir_reyes
    hide maya_reyes

    scene bg ch9_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Crackling radios; someone cursing; water sluicing through a channel cut for temporary pumps.]
    # play music "music_placeholder"  # [Music: Tense, there-and-back piano motifs; a single violin line that scratches at nerves]
    "You find Maren Voss before she finds you. She is all practiced poise unraveling at the edges—exactly contained enough for the cameras, but her voice tight with the satisfaction of vindication. She steps toward you as"
    "if to offer help; instead, it's a microphone shoved in place by a reporter who wants the narrative that will sell tonight's fear."
    show maren_voss at left:
        zoom 0.7

    maren_voss "This is precisely why decisive, consolidated action matters. We moved quickly. We protected commerce, we safeguarded essential infrastructure. This proves the project—"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "People are under three feet of water in the Lomas block. They've been waiting on relocation payments—"

    maren_voss "Relocation is complex. We cannot—' (she looks past you at the sea) '—fix everything overnight. What we have done is prevent economic collapse."
    "The reporter presses, hungry. Maren Voss's answers are smooth, terrifyingly certain. Her language turns the storm into data: proof, validation, metrics. Around her, the ring of contractors nod; the cameras magnify her steel-gray eyes until they look almost editorial."

    maya_reyes "You call this a success while families drown in houses that were supposed to have been eased out—"

    maren_voss "We cannot save every home without destroying the town's ability to function. Sometimes—' (she pauses, the cold logic snapping into place) '—hard choices enable survival for more people than not."
    "Her words are a scalpel. They are also the exact rhetoric you heard in budget meetings and in the council chamber, only now the syllables have been baptized in rain. You feel the old guilt like"
    "a phone ringing in your ribs—your yes, given in the council room, in defense of an emergency path you hoped would be temporary. You can see where that concession sits, a rusted seam in the hull"
    "you thought was steady."
    "Mayor Ana arrives, rain on her sash, mascara streaked like a roadmap of exhaustion. She is trying to hold herself steady for the cameras and for the people who are now filling the shelter's gym. Her voice cracks once and then hardens."
    show mayor_ana_delgado at center:
        zoom 0.7

    mayor_ana_delgado "We will deploy additional relief teams. We are coordinating with regional partners—"

    maya_reyes "You promised binding relocation aid."

    "Mayor Ana (looking between you and Maren Voss)" "We will—' (she looks at the ground, ashamed at the incompletion in her hands) '—we are doing everything we can."
    "Maren Voss's jaw tightens, an invisible contract being signed by the look in her eyes. You hear the rhetoric shift from 'we' to 'those who were protected', and the pronouns slice."

    menu:
        "Confront Maren publicly—name the neighborhoods she left behind":
            "You step forward, voice shaking but loud enough to pierce the crowd. Names fall out like stones: Lomas, East Wharf, the old fisher flats. People in the command ring go still; a woman cries out. Maren Voss's smile thins into something like contempt. The cameras pivot."
        "Pull Ana aside and demand a closed-door commitment, opting for damage-control rather than spectacle":
            "You take Ana's sleeve and drag her into the storm's shadow. Her breath is jagged. She promises to call for emergency funds and legal review. You feel the bargain forming—less visible, more bureaucratic."

    # --- merge ---
    "Both outcomes lead toward the Low-lying Neighborhoods / Lomas Block as relief and accountability begin to unfold."
    # [Scene: Low-lying Neighborhoods / Lomas Block | Night — High Tide]
    hide maren_voss
    hide maya_reyes
    hide mayor_ana_delgado

    scene bg ch9_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: People calling for each other's names, the muffled groan of a refrigerator as water invades, the distant keening of an ambulance.]
    # play music "music_placeholder"  # [Music: Dissonant chords swell; low drums simulate a pounding heart—urgent, ragged]
    "You made choices for Harborwell that were supposed to save it. Standing on the ruined stoop of a house you once advised on permits for, you watch the verdict come in physical form. The sea found the seams you left unattended."
    "Elias Hart is there, soaked to the waist, his denim jacket a sodden badge. He stands on a submerged stoop where a child's rain boots float, empty; his hand-carved whistle is clenched and mute in his"
    "fist. His eyes are green, rimmed red, and there is no theatrical rage—only a blunt, bone-deep betrayal."
    show elias_hart at left:
        zoom 0.7

    elias_hart "You told people you were choosing them. You told us you'd fight for binding protections. We stood in the wind with our petitions. We collected signatures. We rallied people into the streets."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "I believed— I believed the wall would buy time to get everyone out. I thought—"

    elias_hart "You thought? You thought in council rooms and meetings and models. People thought in their kitchens. Samir's filming a house right now where two kids are clinging to a doorframe."
    "Samir's footage flickers on a volunteer's handheld screen—two children, a soaked teddy, a neighbor's hand reaching through the water. The image is a strike to your sternum."

    maya_reyes "I tried to get the relocation money faster. There were approvals, the procurement cycle—"

    elias_hart "But you didn't make them sign binding. You didn't turn words into paperwork people could hold. You chose speed over guarantees, Maya."
    "Your name—Maya—lands in the air like a dropped stone. He doesn't call you by the public title you hold in the lab or the council. He calls you what you are to him: small, intimately known."

    maya_reyes "I thought saving the harbor would buy room to save the rest. I thought jobs would keep people here—"

    elias_hart "You thought what you'd always been taught—trade-offs. The people I grew up with can't afford your calculus."
    "Iris pushes through the crowd, rubber gloves pulled up, hands black with mud. She does not shout. Her look is steadier than Elias Hart's, more weather-forged."
    show iris_tanaka at center:
        zoom 0.7

    iris_tanaka "We told 'em the marsh can't just be paved around. We told 'em fish move, storms change. But policy wanted a line you can photograph. People listened to the promise of work and protection."
    "The tide takes a porch swing, the sound of its chain cutting through your thoughts. People are shouting—requests, names, accusations—unfiltered, immediate. Volunteers drag wet furniture toward the volunteer center; someone is trying to set up a portable diesel pump on a generator that coughs and dies."

    maya_reyes "I'm sorry."

    elias_hart "Sorry doesn't make a basement stop filling.' (he spits the words, then laughs hollowly) 'Sorry doesn't put roofs back on kids' heads, Maya."
    "You try to respond with the careful lists of mitigations you used to fall back on—redirection of funding, emergency relief, a pledge to expedite legal protections—but words are paper in a storm. Each sentence you form"
    "is eaten by the noise until it shows up on a volunteer's recorder as damp, maybe-well-meaning static."
    hide elias_hart
    show samir_reyes at left:
        zoom 0.7

    samir_reyes "People are blaming you on the feed, Mags."

    maya_reyes "Let them. Let them have it."
    "Elias Hart steps closer, guttering with rain, and his voice drops to a kind of pleading that is worse than the anger."
    hide maya_reyes
    show elias_hart at right:
        zoom 0.7

    elias_hart "We could've done differently. We should've insisted on legal anchors—on moving people first. You know how to get them. You used the council's language to justify—"
    hide iris_tanaka
    show maya_reyes at center:
        zoom 0.7

    maya_reyes "I used the council's language because I thought that would save more lives in the short run.' (you feel each syllable as if it were a grain of salt in an open wound) 'If I'd known the storm would come this early—"
    "He presses his forehead to the cold wood of the porch rail, as if trying to steady both himself and you. There is silence that thumps—heavy, accusatory."

    elias_hart "When you say 'save the town', what you mean is 'save the parts that make us look like a town'.' (he looks at the businesses, at the protected lights gleaming behind the sea wall) 'Who do you think works those shops? Who lives in these houses?"
    "You have no defense that will withstand the clarity of this moment. The calculus you once trusted rearranges itself in a single, cruel frame: the town is safer where value was already concentrated; the people without political capital paid the immediate price."
    # [Scene: Downtown / Makeshift Press Area | Night — After the Initial Surge]
    hide samir_reyes
    hide elias_hart
    hide maya_reyes

    scene bg ch9_3be532_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Shuffling feet, a low murmur of sadness and shock; a newscaster's calm voice in the background attempting structure where there is none.]
    # play music "music_placeholder"  # [Music: A slow, descending cello that smells of grief]
    "Maren Voss's televised address hits the feed with the momentum of inevitability. She stands under a covered awning, water dripping off the lapel of her trench. The cameras have found their narrative: consolidation worked where it was applied. Her tone is measured; the content is dangerous in its simplicity."
    show maren_voss at left:
        zoom 0.7

    maren_voss "This storm validates the plan. Where we took decisive action, infrastructure held. Where outdated patterns remained, harm occurred. We now must consider more consolidation to protect the municipality from future—"
    "A woman in the crowd screams a name—Lomas—over and over, like a litany. The scream is not rhetorical; it is a physical wound. The microphones pick it up, the feeds loop it."
    "Mayor Ana whispers something to Maren Voss, a private pleading you cannot hear. Maren Voss's face changes for a breath—an almost human micro-expression—and then the polished mask reasserts itself. Power is lubricated in the smallest mercies and then welded into policy."
    show mayor_ana_delgado at right:
        zoom 0.7

    mayor_ana_delgado "We will negotiate more equitable terms at the next council session."
    show maya_reyes at center:
        zoom 0.7

    maya_reyes "Where were those terms before the contracts were signed?"

    maren_voss "We acted in the town's best interest. That is what leadership requires."
    "People thrust microphones at you; volunteers tug at your sleeve; Elias Hart stands at the periphery, refusing to be corralled into the frame of civic acceptance. He looks like someone who used to believe in fireworks now watching embers die in rain."
    "Iris emerges from a cluster of volunteers, carrying a soaked crate of canned food on her shoulder. She is practical; there is no grand speech. She kneels to help an old woman from her porch as if that will be the argument that matters later. For tonight, it is enough."
    hide maren_voss
    show iris_tanaka at left:
        zoom 0.7

    iris_tanaka "You were in the room, Maya. We all watched you choose. For what it's worth, I'm still with you if you actually show up."
    "Elias Hart hears this and flinches, like someone who wasn't sure he wanted rescue and then was offered it anyway."
    hide mayor_ana_delgado
    show elias_hart at right:
        zoom 0.7

    elias_hart "Iris—"

    "Iris (cutting him off)" "Don't make it about you."
    "There is a press scrum and then a lull—a tired, terrible waiting as pumps are set up, as people are counted. The arousal leaks into a tiredness that is almost worse: the exhaustion of people who"
    "have burned off their immediate fury and slid into the slow, grinding grief of rebuilding."
    "You wander down to the edge of the old pier, where the jagged concrete of the abandoned wall balks the surf in a way that is beautiful and ruined. You press your hand to the cold,"
    "salt-pitted stone and feel the town in it—the history of decisions, the layered sediment of intention and neglect."
    "Samir comes up behind you, camera down. He is radioactive with what he has filmed. He tells you there are calls for an inquiry, for resignations, for criminal negligence. He mentions Maren Voss's surge in approval ratings—'proof' for some, he says, that rhetoric becomes policy by spectacle."
    hide maya_reyes
    show samir_reyes at center:
        zoom 0.7

    samir_reyes "They're calling it decisive leadership. People want answers, Mags. But they also want someone who can look like they saved them.' (he flinches) 'It's getting ugly on the comment threads."
    "You close your fist around the brass compass locket at your throat until the edges bite. The metal is warm from your skin. You had let it be an anchor once; tonight it is a cold accusation."
    hide iris_tanaka
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "I thought I was doing the most to prevent loss—"

    samir_reyes "You did what you thought you'd do. That won't fill these houses tonight."
    "The wind picks up, as if to answer. You watch furiously: a woman from the flooded Lomas block wrapping a child in a donated sleeping bag; a contractor rappelling to check a pump; a pair of fishermen pushing an inflatable through dark water like a desperate ark."
    "Maren Voss's statements continue to ripple through the feeds. She calls for 'strategic consolidation' in the weeks that follow; her voice grows in the polls as images of saved storefronts go viral. She stands, in footage,"
    "hands clasped, and looks like victory's proof. Because the wall held in places that mattered to cameras and commerce, the argument for further consolidation looks sharper to people outside the neighborhoods that sank."
    "You do not sleep that night. You sit on the old pier and scan the horizon while the lights of the downtown strip remain stubbornly intact behind the wall. The contrast is a cruelty, a photograph"
    "you cannot unsee. Your own choices have become part of a tableau that benefits some and punishes others."
    # [Scene: Dawn Aftermath | Old Pier / Abandoned Sea Wall]
    hide elias_hart
    hide samir_reyes
    hide maya_reyes

    scene bg ch9_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low, steady drip; distant sobbing; the creak of a rescue boat being hauled ashore.]
    # play music "music_placeholder"  # [Music: A single, sustained minor chord. No resolve.]
    "You watch Elias Hart leave the scene without looking back. He doesn't shout, doesn't slam a car door—he simply walks away with the rain darkening his shoulders, the whistle absent from his mouth, the look on"
    "his face that holds a memory of what you once were together and what you are now: strained to breaking."
    "Iris stays, working, eyes like flint. Mayor Ana holds a brittle press conference, and Samir posts one more clip—ten minutes that no one will want to watch twice."
    "The town is safer in certain corridors: the shops will open again. There will be insurance payouts where values are concentrated. There will be photos of freshly swept sidewalks and an economy that appears to march"
    "on. But at the edge of that image, in the places you chose not to anchor, there are houses that will not be the same. Families move in the slow, humiliating way of the displaced—salvaging jewelry,"
    "a box of photographs, a hope that fits into a single car."
    "You stand at the abandoned sea wall one last time, the concrete jagged beneath your palms, and the weight of what you enabled sits like a stone in your chest. You replay the council votes, the"
    "private concessions, the arguments you made in the sterile light of the Glasshouse. Each one was defensible. Each one, in the end, had a cost."
    "Maren Voss's face appears on the screen of your phone—an interview in which she says the storm validated the strategy and calls for further consolidation to prevent 'scattered vulnerability.' Her words are precise; they will become"
    "policy if she is not checked. She gains clout, and with it the capacity to make more of the same moves that produced tonight's map of loss."
    "You think of the children on the flooding stoop, of Samir's footage, of Iris's mud-stained hands, of the volunteers who slept in their cars to hand out soup. You think of Elias Hart and how his"
    "silence broke into a thousand small refusals to trust you again. Your role in enabling the plan is heavy and undeniable."
    "You press the brass compass between your palms until the edges press skin-white, and you let your breath make a visible line in the cold air. You don't know if you are at the end of"
    "a path or the beginning of a long, brutal reckoning. The Icarus arc—your ascent in the name of decisive action and the consequent fall—feels carved into the town now, a ledger of ascent and ruin."
    "You close your eyes. The harbor's smell—brine, diesel, wet wood—fills your lungs like an accusation and a benediction at once."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "We have to repair it. We have to…make it right."
    "The words are almost prayer and almost a strategy. They are small against the magnitude of what has happened and the very loud momentum that will shape Harborwell's next months: consolidations proposed, aid temporarily deployed, lawsuits filed, and, beneath it all, the slow, sleepless work of holding neighbor to neighbor."
    "You open your eyes to a town that has been spared in places and hollowed in others. That is the true weight now—recognizing that some of what you saved must be balanced by what you broke."
    hide maya_reyes

    scene bg ch9_3be532_6 at full_bg
    # play music "music_placeholder"  # [Music: A single, unresolved chord hangs; no uplift; just the thin continuation of sound]
    "You let the compass cool against your skin. The harbor breathes around you, indifferent to names, plans, promises. The social fabric is torn, and whether it can be mended will be the work of years."
    "You do not know if Elias Hart will ever speak to you without the taste of betrayal between words. You do not know if Maren Voss's consolidation will be rerouted into something less destructive. You do"
    "not know if the legal protections you once delayed can be pulled forward or if those waiting will ever forgive the delay that sent water into their homes."
    "You stand in the damp and let the weight settle. The town will carry this night with it like a scar, visible and private all at once."

    scene bg ch9_3be532_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade to a low, melancholy hum]

    scene bg ch9_3be532_8 at full_bg
    "THE END"
    # [GAME END]
    return
