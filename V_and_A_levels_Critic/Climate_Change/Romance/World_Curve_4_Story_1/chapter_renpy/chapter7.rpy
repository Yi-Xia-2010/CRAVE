label chapter7:

    # [Scene: Saltwren Commons | Late Afternoon — Storm Warning]

    scene bg ch6_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Dissonant strings, rising tempo]
    # play sound "sfx_placeholder"  # [Sound: Distant thunder; the boardwalk creaks like a tired animal]
    "You taste salt and wet earth in the air, and the Commons is a mouthful of nervous energy. People move with purpose: Rae straps up painted placards and mutters a chant under her breath; Tommy hauls"
    "a coil of rope with knotted, familiar grunts. Your hands are already raw from tying stakes into saturated soil, and your jacket smells faintly of compost and rain."
    "You remember the meetings, the mediated promises that felt like slow sutures. You remember arguing for slow, living solutions—beds and berms and plants that learn to bend—with Elias outlining calibrated pumps and sensor arrays. None of"
    "that feels slow now. The tide is on a timetable that doesn't care for compromise."
    "A low, wrong sound runs under everything—the sea pushing against concrete. The first sheets of rain arrive hard, each one a small, pinched staccato on the old driftwood roofs. Water beads on your lashes."
    show tomas_tommy_reyes at left:
        zoom 0.7

    tomas_tommy_reyes "Mara—boardwalk's starting to lift at the southeast span. If that goes, the channels reroute right through the nursery beds."
    show mara_lin at right:
        zoom 0.7

    mara_lin "On it."
    "You can feel your voice compress; there is no room for anything else."
    "You and Rae move like a practiced machine. You wedge sandbags into sagging gaps, stomp mud into the seams, fingers blistering where rope bites. The wind presses against your back as if pushing you out to sea."

    menu:
        "Tie the seed trays down":
            "You crouch into the mud, clutching trays as the wind tries to peel them away. The seedlings shudder, but you hold them like a promise."
        "Help Tommy anchor the boardwalk":
            "You shoulder a wet, stubborn length of timber with Tommy. Together you hammer stakes that scream under the hammer's blow, and for a moment you feel the muscle of the town."

    # --- merge ---
    "..."
    # [Scene: Promenade | Night — The Eye Doesn’t Come]
    hide tomas_tommy_reyes
    hide mara_lin

    scene bg ch6_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Sirens in the distance; a high, urgent radio voice; water hitting concrete like an army]
    # play music "music_placeholder"  # [Music: Percussive, frantic rhythm]
    "The Promenade's survey flags are little ragged teeth. You can see, as if lit from inside, where Celeste's engineers left clean lines of gravel and steel—rigid promises that crack differently from living roots. Where the reclaimed"
    "beds should have absorbed the surge, a throat of water finds an old service cut and pours through it like a fist."
    "You are running now. The Commons and the Promenade are a single language of collapse: one moment a boardwalk, the next a sluice of brown water swallowing boxes and signs. A section of the promenade shears"
    "away with a sound like the last page of a book being torn free—the concrete gives, and a column of spray eats the sky."
    show elias_navarro at left:
        zoom 0.7

    elias_navarro "Mara, we need to get pumps at 3B and 4—"
    show mara_lin at right:
        zoom 0.7

    mara_lin "We need to stop the water from carving through the Commons. If that sluice holds, the low row is gone."

    elias_navarro "Pumps will buy us ten, twenty minutes. If we don't—"

    mara_lin "If we don't the beds are gone and—"
    "The thought doesn't finish. You don't want to finish it."
    "Rain finds the seams in your collar. The radio squeals. Someone screams your name from around a bend; someone else collapses from cold, and you are there to catch them before they slip into the mud."
    "A tree—old, salt-scarred—splits under wind stress and spills its branches like a toppled ship across a path. A child's toy floats past on the current. You taste iron; it's not only the sea anymore."

    menu:
        "Stay and pull the trapped volunteer from under the trellis":
            "You throw yourself into the space between fallen wood and slick roots, arms burning as you pry a hand out of mud. The volunteer coughs and collapses against you; you hold them until they stop trembling."
        "Run for the Tidewatch Lab radio and call Amina":
            "You sprint, soaked, your boots slipping, and the lab's light is a beacon. You seize the handset, voice ragged, and call for coordinated pump deployment."

    # --- merge ---
    "..."
    # [Scene: Tidewatch Lab | Night — The Lab Becomes a Lifeboat]
    hide elias_navarro
    hide mara_lin

    scene bg ch6_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Monitors beep; the hum of a generator trying to outrun the outage]
    # play music "music_placeholder"  # [Music: Taut strings with a single, hot drum]
    "Inside the lab, the scientific calm is grammar failing at punctuation. Dr. Amina Bhatt is a tether: voice steady, fingers dancing over a screen that shows cross-sections becoming wrong in real time. Her face is drawn, but she speaks like a person reading the last maps of a made-up country."
    show dr_amina_bhatt at left:
        zoom 0.7

    dr_amina_bhatt "Sensors are sending back a pressure spike at 21:12. The promenade breach is propagating to the estuary faster than predicted. We have structural failure at Node C."
    show mara_lin at right:
        zoom 0.7

    mara_lin "How long until the low-lying lanes are under the cut?"

    dr_amina_bhatt "Ten minutes. Maybe less."
    "Elias Navarro has his wristband up, rain dripping off the strap. He looks smaller here, instrument in hand, surrounded by the things that solaced him all year—maps, models, the clean math of things that should have worked."
    show elias_navarro at center:
        zoom 0.7

    elias_navarro "We can route pumps to the estuary channel and use the mill sluices to redistribute pressure."

    mara_lin "You can—"
    "Your voice slashes him. The accusation is a physical thing. 'Did you ever consider the marsh would need more room? Did you—did we—'"
    "He meets your eyes. There's fatigue, then a sudden, pained apology that isn't finished by the words."

    elias_navarro "We thought we had a compromise. The modeling assumed—"

    mara_lin "Assumed. You always assume the numbers will hold. Real people aren't numbers. My neighbors are not 'assumptions.'"
    "It turns into shouting because the sound outside gives you something to echo against. The argument is not clean; it stops and starts like tidewater. Amina moves between you like a referee, but there's no winning here."

    dr_amina_bhatt "Please. Now is not the time—"

    mara_lin "When, Amina? When will it be the time to stop pretending a pump can plant roots?"

    elias_navarro "Stop—Mara. This isn't about winning. This is about saving—"
    "His sentence drowns as a new alarm gobbles the room's air. The lab's screen blinks an SOS: a low-lying neighborhood—Rowan Street—has been overtopped. The feed is a window where shapes struggle in dark water. You see a roof, then a hand. Your throat locks."
    hide dr_amina_bhatt
    show tomas_tommy_reyes at left:
        zoom 0.7

    tomas_tommy_reyes "There are people trying to climb to attics on Rowan. Boats could get them if we clear the channel."
    "He looks at Elias, then at you—his face reads like a ledger of old debts and newer fears."
    "You and Elias look at each other and then away. In the time it takes to say 'Let's go,' an entire household is reconfigured into survival."
    # [Scene: Low-Lying Neighborhoods — Night to Dawn]
    hide mara_lin
    hide elias_navarro
    hide tomas_tommy_reyes

    scene bg ch6_e67f19_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rescue ropes creak; distant wails; the heavy slap of water against siding]
    # play music "music_placeholder"  # [Music: A single mournful cello, then silence punctuated by sobs]
    "You go out, elbow-deep in cold that feels like it belongs to someone else. Your hands—so used to tending seedlings—are now hauling people into boats. You pull an old woman by the shoulders and hear a"
    "name you know — the name of someone whose laugh you remember from a neighborhood garden party two summers ago. A child grips your sleeve and won't look away."
    "Elias Navarro is there, commanding, calm fingers finding knots, voice a lighthouse. He hauls a family up into a skiff and stays until the last person is moved. He works like he's trying to measure his guilt in saved bodies."
    show tomas_tommy_reyes at left:
        zoom 0.7

    tomas_tommy_reyes "We lost the north row—greenhouse gone. The compost bins are floating like islands. A bunch of families—"
    "(He swallows.)"

    tomas_tommy_reyes "They're going to need shelter."
    show mara_lin at right:
        zoom 0.7

    mara_lin "We held some. We didn't hold all of it."
    show elias_navarro at center:
        zoom 0.7

    elias_navarro "We—"
    "He can't finish the sentence cleanly. 'We saved who we could.'"
    "You laugh, the sound raw and too loud in the narrow alley. 'Saved who we could,' you repeat, as if the words are both a shield and an indictment. 'That's not the same as not having failed.' Your voice breaks across the last word."
    "He reaches as if to take your hand and the weather takes that small human grace and shakes it loose."

    elias_navarro "Mara, look—"
    "(He tries to reason you down from the cliff.) 'If I'd pushed harder at the council—if I'd—'"

    mara_lin "If you'd pushed harder, there might have been faster construction of floodwalls that would have meant—"

    elias_navarro "And if we'd let that happen, their salt marsh would have been paved over. We would have traded one failure for another."
    "The argument spins, sharp and hard-edged. Both of you are listing through consequences like wounded sailors naming broken ribs."
    "Celeste Park moves through the emergency tents with efficient steps, an offer of bussed shelter and corporate blankets in her gloved hands. Her smile is thin and exact. She looks at the ruined promenade and the"
    "broken seedlings, measuring what can be built anew. You want to hate her effort—how it comes wrapped in PR—but right now hate is a commodity you cannot afford. Her expression is complex, unreadable where it matters,"
    "and you cannot tell if she's pained or pleased at the scale of need."
    hide tomas_tommy_reyes
    show celeste_park at left:
        zoom 0.7

    celeste_park "We can set up a temporary promenade—modular, fast. We have partners willing to fund emergency housing."

    mara_lin "And what of the marshlands? What of the people whose income depends on what you call 'temporary'?"

    celeste_park "We provide structure. People can rebuild with safety."
    "The words are precise and sound like a promise, but your stomach flips when you imagine the price."
    # [Scene: Old Mill Rooftop | Dawn — After the Crash]
    hide mara_lin
    hide elias_navarro
    hide celeste_park

    scene bg ch6_e67f19_5 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano, a single low note that holds and sags]
    # play sound "sfx_placeholder"  # [Sound: The distant rumble of recovery trucks; gulls calling like questions]
    "By the time you climb the rope ladder to the Old Mill rooftop, the worst of the storm has spent itself. The rooftop is raw with salt spray and strewn with broken lanterns. The garden there—a"
    "refuge that felt indestructible on calmer days—has holes where trellises collapsed. A single mason jar hangs, half-full of rain."
    "Elias Navarro follows you up the ladder slower than you expected. He stands at a distance that used to be easy to close. The town underfoot looks different: houses with tarps, people with blankets, a strip of promenade now a hatched black tear. The Commons looks wounded—alive, maybe, but injured."
    show mara_lin at left:
        zoom 0.7

    mara_lin "This is what it looks like when the compromises we make are measured in people's scattered things."
    show elias_navarro at right:
        zoom 0.7

    elias_navarro "I thought—"
    "(His voice is small. For the first time since you met, he looks like someone shivering without the shelter of data.) 'I thought mediation would give us time to do right. I believed—'"
    "You can't find a way to say the sentence he wants you to hear—there's too much salt in your mouth. Instead you say what you know to be true and terrible."

    mara_lin "Belief doesn't keep the water out."
    "He closes his eyes. For a heartbeat you see his face as unadorned: exhausted, raw, someone who has to live inside a choice he made. Then his jaw sets."

    elias_navarro "I did what I thought would help most people. I called in pumps. We saved homes."

    mara_lin "You negotiated a pause that let them finish the first phase of the promenade. You framed risks as tolerable. People died because a gap opened where the marsh needed room."
    "The words drop between you like stones. He opens his mouth, then shuts it."

    elias_navarro "I'm sorry. I—"

    mara_lin "Sorry doesn't—"
    "(You stop; nothing can finish that sentence. The vocabulary of apologies has been exhausted.)"
    "The two of you stand on the rooftop like two small, persistent things on a battered shore. The world is loud with repairing machines and quieter with mourning. Around the mill, neighbors distribute hot drinks. Someone"
    "is singing—terrible and brave. You both look at the Commons and at the Promenade, and in that look the years of shared labor and misbound trust fold into an ache that is not only yours."
    "Tommy comes up the ladder without asking. He drops his wet cap to the boards and sits, shoulders heavy."
    show tomas_tommy_reyes at center:
        zoom 0.7

    tomas_tommy_reyes "We got most of the folks out of Rowan. We lost some sheds, a greenhouse, a few beds. Rae's family—"
    "(He doesn't finish.)"

    mara_lin "Who?"

    tomas_tommy_reyes "Rae's brother—he couldn't get his boat free. I thought—"
    "(His voice breaks.) 'We tried.'"
    "Rae is walking below, holding her camera like proof that something happened, and when she looks up her eyes find yours. There's a new weight there, an old youthfulness folded into the lines that will take years to iron out."

    mara_lin "Do you understand why I can't stand the idea of 'compromise' as a bandage any longer? Why I thought slower, living solutions would resist this—why I thought they'd be different?"

    elias_navarro "I do. I do. I just—"
    "(He reaches again, and this time his hand brushes yours briefly. Wet skin. No promise.)"
    "The touch is a small betrayal—a memory of better weather. It doesn't hold."

    elias_navarro "Maybe we just saw different timelines, Mara. Maybe I kept thinking of what could be engineered in a season. You kept thinking of what would take generations."

    mara_lin "And in the space between our timelines, the town...broke."
    "He looks away, then back, and the decision is a physical thing you can feel forming in the hollow of your chest: not a single, clean choice but a slow unmaking. He steps back, and with that distance he sets the terms."

    elias_navarro "I have to go coordinate relief up and down the coast. There are other towns—"
    "(He swallows.)"

    elias_navarro "They're calling me. I can't stay here and watch you—"
    "(He stops; the rest is unvoiced.)"

    mara_lin "So you leave because you can't watch me do what I have to? Because it's simpler to run to other fires than to stand in this mess with me?"
    "He looks stricken. It is not a noble departure. It is a man who has labored in the calculus of harm, who chooses an axis that will let him keep moving. You know, with a cold bluntness, that neither of you can pretend this is only about geography anymore."

    elias_navarro "I—"
    "(He exhales like someone who has been holding a stone.)"

    elias_navarro "I care about this place. I care about you. But I also have to do the work where I can make a difference, Mara."

    mara_lin "And leaving here makes a difference?"
    "He meets your gaze, and for a moment there is an earnestness that hurts."

    elias_navarro "It should."
    "You let the word hang and it becomes its own small accusation and prayer. The rooftop wind pushes salt into your eyes. Behind him, the town is a palimpsest of what was and what will be."
    "You are left with choices that will not be dramatized; you are left with the fact that the person you trusted to measure risk in service of the town and the person you loved has chosen"
    "a different measure."
    "Elias Navarro turns toward the ladder. He moves with the slow, weary motion of someone whose shoulders have been given too much to carry. He doesn't look back. The sound of his boots on the gangway is a percussion that marks a season's end."
    "You stay on the rooftop until the light softens and the work begins again below. People need you to be steady. People need you to organize shelters, to catalog who lost what, to plant the first"
    "shovel of new berm so that the Commons will remember how to hold water differently next time. You are all of those things and you are also someone who has had something ripped away."
    "The dawn is gray and unkind. The town is broken, and so are you—beautiful in the way things are beautiful when they are honest about their fractures."
    "You wrap your frayed satchel around your wrist and descend. There is no promise. There is only the work and the long rawness of grief."
    hide mara_lin
    hide elias_navarro
    hide tomas_tommy_reyes

    scene bg ch6_e67f19_6 at full_bg
    # play music "music_placeholder"  # [Music: A single low chord resolves into a weary, steady pulse]

    scene bg ch6_e67f19_7 at full_bg
    "THE END"
    # [GAME END]
    return
