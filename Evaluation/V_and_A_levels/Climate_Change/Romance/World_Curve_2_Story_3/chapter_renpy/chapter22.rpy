label chapter22:

    # [Scene: Glasshouse Lab & Seedbank | Dawn]

    scene bg ch15_6b9e63_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low, constant hum of backup pumps; rain still stabs the roof in a staccato. Somewhere outside, a generator coughs and restarts.]
    # play music "music_placeholder"  # [Music: Dissonant strings — a rapid, tense motif building under a distant percussion]
    "You run a finger along the seam of the sealed crate and feel grit under your nail. The cold of the metal is a knife against the inside of your palm; for a second you imagine"
    "cold pulling through everyone you know. The seeds sit inside like small, patient accusations and promises both. You remember the crate's label — your handwriting, careful and hopeful and now smeared by salt spray — and"
    "you swallow until your throat unclenches."
    show amalia_reyes at left:
        zoom 0.7

    amalia_reyes "We counted names. We patched the checklist. People are at the hall, and some are on the flats trying to salvage what they can."
    "(She sets down a clipboard, voice steady but thin.) 'There are a few who want the council to reopen the floodwall contract now. Others—' (She looks at you.) '—they want arrests.'"
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "Arrests won't bring back the road. Arrests won't mend the pilings."
    hide amalia_reyes
    hide marina_reyes

    scene bg ch15_6b9e63_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The scrape of mud from his boots; he picks a cracked mug from a shelf and sets it down like a small truce]
    show elias_kato at left:
        zoom 0.7

    elias_kato "We can get temporary shelter for the families near the spit,' he says. 'Federal relief is delayed, but we can prioritize emergency funds. I can—' (He stops; decides to drop the procedural script.) 'I can help with routing pumps to the low ground. We don't have to do this alone."
    "You study him. There is relief in the offer and a long, bad ache braided around it: promises that have already felt like compromises. The town will measure you both by what you saved and what you couldn't."
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "Your pumps will keep the water out of basements for a week,' you say. 'They won't replace the pilings, Elias. They won't make people who lost their roofs feel like home again."

    elias_kato "No, they won't. But they'll stop the cameras from showing wet furniture in living rooms next week. They'll keep the clinics open. We can keep services running while we plan for longer-term protections.' (He chooses words like scaffolding.) 'That's the space I've been trying to carve."

    marina_reyes "That space feels like a ledger.' Your fingers curl into the edge of the crate until you taste metal. 'It sounds like lawyering our grief away."
    "Elias Kato's jaw tightens. His amber eyes narrow, not angry so much as riffling through alternatives. He takes another breath, slower, as if measuring how vulnerable he can be."

    elias_kato "You didn't owe anyone permission. But now—' (He taps the reports.) '—now it's about getting people through the next storm season. We can negotiate longer-term protections if we stitch the community back together."
    "Amalia watches you two like she's counting breaths. Mika bursts in from the doorway, soaked to the waist, carrying a drone that smells of salt and burnt circuitry."
    show mika_tran at center:
        zoom 0.7

    mika_tran "Sensors are down on the west line. We lost a buoy. Old Tom said he'd meet us on the flats. People are angry — yelling at the crew trucks, at the council tent, at anyone with a clipboard."
    "Old Tom: (arriving, rain crusting his beard) 'Angry's not the half of it. They want reasons. They want someone to point a finger.' (He folds his hands like a net.) 'And when you point, you need to be able to tie a knot that holds. Not promises in the air.'"

    marina_reyes "We're getting the community out, and then we plant what we can.' Your voice hardens in the center — not because you have a plan yet, but because the heat of the moment demands a shape. 'We plant the first long-line today."
    "Elias Kato flinches. He has that distance in his face when he counts costs: it's a map he reads to stay useful."

    elias_kato "Today? The flats are unstable. The tide charts are—"

    marina_reyes "Then we'll use the low tide window. We'll be careful. We don't have 'wait' anymore."

    menu:
        "Tell Elias to sign the municipal relief forms now":
            "You slide the forms across the bench toward him. 'Sign them. Make them real now.' He takes the pen with fingers that tremble almost not at all."
        "Tell Elias to come with you to the flats":
            "You step forward and lay a palm on his forearm. 'Then come. Tie the line with us. Don't stand behind paper.' He looks at your hand as if for the first time; the line between offer and presence sharpens."

    # --- merge ---
    "Narrative continues to the Laurel Bay Tidal Flats scene."
    # [Scene: Laurel Bay Tidal Flats | Mid-Morning]
    hide elias_kato
    hide marina_reyes
    hide mika_tran

    scene bg ch15_6b9e63_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Waves cling to pilings; a few shouts rise and break; the drone of a survey copter clicks overhead; wooden boards creak underfoot.]
    # play music "music_placeholder"  # [Music: Percussive, urgent — timpani rolls under a rising brass motif]
    "You step onto the flats with boots sinking into cold mud. Each step leaves a print that the sea could swallow by afternoon, and in that small erasure you feel the town's fragility. People watch as"
    "you approach; some faces are raw with loss, others glare like they carry court papers under their arms."

    scene bg ch15_6b9e63_4 at full_bg
    show kaori_kai_matsuda at left:
        zoom 0.7

    kaori_kai_matsuda "So you plant kelp while the town signs off on seawalls?' She doesn't ask; she states it into the wind. 'That's one way to play optimism."
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "Kelp gives living armor. It buys time for people and for the mud to settle around new pilings.' You keep your voice even. There is a ring of pleading under it — not to Kai, but to the people watching. 'It meshes with—"

    kaori_kai_matsuda "With soft buffers?' She laughs, but it is thin. 'When the insurance companies are deciding who gets a payout, they don't ask if your algae farm looked nice. They count concrete."

    "A neighbor calls out from the half-rebuilt porch of a raised house" "We need roads first! Not ribbons of seaweed!"
    "Old Tom moves between voices, a living memory that makes people pause."
    show thomas_old_tom_bellamy at center:
        zoom 0.7

    thomas_old_tom_bellamy "We don't have the luxury of a single answer. We need nets and screws and songs. We need action in every lane. Blaming helps nothing; tying helps everything."
    "You feel the crowd tilt on a hinge: fury toward institutional actors; fury toward those who advocated for practical walls; fury at the weather that keeps coming with no conscience."
    "Elias Kato steps up beside you quietly. He does not enter the shouting; instead he speaks to the ledger of logistics."
    hide kaori_kai_matsuda
    show elias_kato at left:
        zoom 0.7

    elias_kato "There is funding for emergency bolstering if we document needs now,' he says. 'If we can map the damage and show the utility-saving potential of hybrid plans, there's a better chance we'll keep the clinic and school running."
    "The words land like a rope thrown toward a pair of hands. Some reach for it. Some snarl and refuse."
    "Kaori 'Kai' Matsuda: (to Elias) 'You're a calm voice when the sky is falling. How do you make that work?'"
    "Elias Kato: (to Kai) 'I count. I sometimes forget that counting can feel like coldness. But I count people too.'"
    "Kaori 'Kai' Matsuda gives you a look that you can neither claim nor refute — the Schrödinger look: whether it's respect, accusation, or something like grief folded in is indecipherable."

    menu:
        "Shout over the crowd: 'We start the long-line now!'":
            "You lift your voice until it cracks. The words cut through the hubbub; there are people who move toward you and people who face away. The knotters step forward."
        "Walk quietly to the high tide marker and set anchor alone":
            "You walk to the high tide marker alone, heart slamming — a solitary liturgy. Someone follows, then another. Action, not speech, becomes the call."

    # --- merge ---
    "The community begins the long-line installation; narrative continues."
    "Mika and a small crew have pulled a spool of line from the back of a pickup. Hands reach: old, young, weathered and new. You remember your father's hands — the way he folded rope, the"
    "way he taught you the steady loop that became more than fishing gear. Your buoy pendant swings against your palm like a tiny compass that points to both grief and stubbornness."
    "The first knot you tie is clumsy. Salt stings your thumb. Someone jokes that your hands are shaking; you don't correct them. The second knot holds."
    "Elias Kato reaches for the other end of the coil. His fingers are sure, and for a moment all the small politics fall away and only work remains: counting eyelets, tightening tension, holding a rope against a rising sea."

    marina_reyes "Hold it steady.' Your breath is a fast metronome. 'When I say, heave."

    elias_kato "On you."
    # [Scene: Cliffside Lighthouse & Storm Watch | Afternoon]
    hide marina_reyes
    hide thomas_old_tom_bellamy
    hide elias_kato

    scene bg ch15_6b9e63_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind screams; a rope whistles; the long-line strains like a living thing. Distantly: the groan of a truck hauling salvage. People shout and answer like flares.]
    # play music "music_placeholder"  # [Music: Cacophonous crescendo — strings and low brass driving an unstoppable, urgent pulse]
    "You stand at the edge of the cliff with the buoy in your palm like a small, stubborn heart. Below, the long-line arcs into the water because of the work everyone's done — knotted, tensioned, a"
    "stitched seam between land and sea. The first kelp trial will anchor there; it will not stop the whole of the storm's harm, but it is a living promise. Your chest is a drum. Everything else"
    "is noise: the snapped board somewhere down the slope, a child's scream muffled and then swallowed, the scraping of community members fastening the line."
    "Kaori 'Kai' Matsuda appears at the cliff's lip like a comet, hair whipping, breath cut short by the climb. Her eyes meet yours — quick, unreadable, then raw."
    show kaori_kai_matsuda at left:
        zoom 0.7

    kaori_kai_matsuda "You still keep at it.' It's not a question. There's no applause in it. 'You still try."
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "I can't stop,' you say. 'Not if there's a thread to pick up."

    "Kaori "Kai" Matsuda (quiet, too close)" "Threads fray. They can strangle, too."

    marina_reyes "Then tie a better knot,"
    "Elias Kato is two steps from you, his hand grazing the rope you hold. He doesn't touch your shoulder. He lays a palm on the tension of the line instead, feeling its give. The gesture is practical and also, impossibly, intimate in a way words have never been for you."
    show elias_kato at center:
        zoom 0.7

    elias_kato "I'll set the municipal tents below,' he says. 'I'll get pumps and heaters. I can keep the clinic on temp power."

    marina_reyes "Do it,' you say. 'But don't make it the only thing you do.' There is pleading in it that doesn't want to be pleaded. 'Come back if you can."

    "Elias Kato (a small, brittle laugh)" "I'll be near, Marina. Not always visible, but near."
    "You watch him move down the path, his coat a dark marker against the spray. You listen to the ropes sing as they take the sea's weight. The kelp lines dip and rise, a slow breathing."
    "The storm picks up—then becomes a concentrated, cacophonous roar. Waves throw themselves like fists at the line. One surge dents the rope; the whole world shudders. Someone screams. The line groans."
    "You plant the buoy into the water with a violence that surprises even you, a decision made in the muscles more than the mind. The buoy rocks, dips, is taken by a wave, and the long-line"
    "follows, trailing like an umbilical into the dark. You steady the line with both hands until your knuckles ache; the rope vibrates up into your bones."

    "Amalia (shouting, almost incoherent over wind)" "Hold! Hold! Marina!"
    "Your vision narrows to the thickness of the rope and the sound of your own breath. This is the place where all the prior calculations, compromises, betrayals, love, and fear condense into one pulling knot."

    "Kaori "Kai" Matsuda (from the cliff's edge)" "If it can't hold—' (Her voice breaks, then hardens.) '—then at least we'll have tried to grow something instead of just building walls."
    "You think of the houses that will not be saved. You think of the family down on Brine Lane who lost a mother's wedding chest to the tide. You think of the council votes and the"
    "memos and the nights you spent arguing that a living coast might be worth the risk. You think of Elias Kato's hands, steady with numbers, and your father's hands, calloused and kind."
    "Everything in you is raw — the old grief, the fresh burns of accusation, the tenderness that refuses to leave. You drive the knot as tightly as you ever have, and for a brittle, shining second the line holds as the sea tests it."
    "A roar louder than the others climbs the cliff: someone begins to sing — an old tune Old Tom used to hum about nets and stars. The sound is ragged, out of tune, but it stitches something in your chest into a taut, painful hope."
    "Marina Reyes: (to the sea, to the town, to the rope) 'We will come back. We will come back for this.' Your voice is a rasp against wind. It is not a promise of perfection; it is an oath to persistence."
    "Elias Kato appears back at the cliff edge, mud on his cuffs, a chart clenched in his hand. He does not say whether the council will sign a new contract or whether the funds will be"
    "enough. Instead, he steps into the wind and takes one of the spare coils. He ties with a surgeon's precision, a quiet demonstration of utility and care."

    elias_kato "Whatever we lost,' he says, barely audible, 'we can at least make sure more people don't lose next year."
    "You look at him, at Kaori 'Kai' Matsuda, at Amalia shouting orders and Mika jerry-rigging a sensor, at Old Tom steadying a younger man's hands while he learns a fisher's knot. Around you, people move with the purpose of those tending a wound."
    "The rope vibrates under your weight like an animal's throat. The sky opens a little and the rain comes down harder, slicing at surfaces and erasing things with a cold, indifferent precision. A wave slams farther than you expected; water sprays up and hits your face cold and salt-sharp."
    "You taste salt and metal and the memory of your father's laugh. The buoy bobs once, twice. The kelp line holds."
    "There is no catharsis here. The town is not whole. Homes are lost; laughter will be different on porches that remain. Trust is a thread pulled thinly across the map — some places cling to it,"
    "others snap. You know some people will never forgive what you chose, that others will never forgive Elias Kato. Kaori 'Kai' Matsuda's face is unreadable in the spray. Old Tom's hands tremble with age but not"
    "with fear."
    "You tuck your buoy pendant back into your palm and press it there until it hurts, an old coin warming with your skin."

    "Mika (calling out)" "Sensors back online. Data's streaming. We're not blind."

    "Amalia (near tears, smiling a little)" "We kept the seeds. That's not nothing."
    "You breathe in, the salt-torn air filling you like an accusation and a benediction. The line hums. The town is ragged around the edges but not erased."
    "Elias Kato comes up behind you and, without claiming anything, slides an arm around your shoulders for a breath. It is neither a rescue nor a surrender; it is the simplest articulation he has: presence."

    elias_kato "We'll rebuild what we can. We'll bury what we can't save and keep the memory alive in plans and in living things."
    "You tilt your head into the wind and let his words wash over you, not a balm but a shield. You want to say that you'll forgive him for staying pragmatic; you want to say he"
    "should have chosen the cooperative earlier. None of those things change the tide. Instead, you hold the cliff and the rope and the moment as if fixing them were possible — because it is, in small"
    "measures."
    "The storm drives on. The kelp line stretches into the gray. Children shriek as they chase each other on raised walkways; an old woman laughs, a sound like breaking glass and stubborn light."

    "Marina Reyes (whispering, to no one and to everyone)" "I will plant again. I will keep planting."
    hide kaori_kai_matsuda
    hide marina_reyes
    hide elias_kato

    scene bg ch15_6b9e63_6 at full_bg
    # play music "music_placeholder"  # [Music: A single, sustained bowed note holds while percussion thrums like a heartbeat, then fades into a low, unresolved chord]
    "You do not know whether this will be enough. You only know how you are made: to pick up rope, to count tide, to tie until the knot holds. You let the truth of that become your work."

    scene bg ch15_6b9e63_7 at full_bg
    # play music "music_placeholder"  # [Music: Rain and a single mourning bell; then slow, fading wind]

    scene bg ch15_6b9e63_8 at full_bg
    "THE END"
    # [GAME END]
    return
