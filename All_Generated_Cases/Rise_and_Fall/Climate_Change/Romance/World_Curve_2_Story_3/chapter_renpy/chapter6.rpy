label chapter6:

    # [Scene: Tidewatch Lab | Late Afternoon — Storm Approaching]

    scene bg ch6_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, tight strings — a slow, descending motif]
    # play sound "sfx_placeholder"  # [Sound: Rain hammering, distant gulls cut off by wind; a steady, small electrical hum from the refrigeration unit]
    "You feel the click under your thumb and, for a second, nothing else registers — only the cold tiny fidelity of the action: a file sent, a press that is irrevocable. The publish button is a"
    "small lever and it lands the same way every small lever does: with a clean, terrible certainty."
    "The lab smells like wet paper and coffee gone stale, with salt chewing at the corners of everything. Your fingertips prick from the cold glass of the tablet. Your hand that holds the compass tightens on"
    "the leather thong without meaning to; the brass is warm from your skin. Outside, wind tugs at the eaves like an impatient thing."
    show isla_morgan at left:
        zoom 0.7

    isla_morgan "Okay. Done."
    "A soft vibration in the tablet tells you that the first emails went out, that a local journalist has already opened the folder. You watch the little confirmation bubble disappear and your stomach turns, not with nausea so much as the sudden absence of a safe harbor."
    "Jonah Merrick steps closer, his boots whispering on the wooden floor. His face is carved by seasons — the map of him is a thing you know by touch: the ridges of cheekbones, the small white"
    "scar at his brow. He doesn't speak right away. He watches the horizon of your jaw and then slowly nods."
    show jonah_merrick at right:
        zoom 0.7

    jonah_merrick "You should've hid it a bit longer, lass."

    isla_morgan "I thought— transparency would keep us honest. If they see the model now, they can choose with eyes open."

    jonah_merrick "Sometimes, eyes open is worse. Sometimes it makes 'em panic."
    "You can hear the other voices arriving — Luca's voice a scatter of energy in the doorway, Ravi's lighter laugh behind him. They fill the room like gusts. You want to tell them everything and nothing all at once; instead you breathe and let the rain give you a rhythm."

    menu:
        "Tuck the compass into your pocket and leave it":
            "You slide the compass away, feeling its weight gone from your palm but not from your chest. The motion steadies you, but you notice the small empty space at your waist like a missing anchor."
        "Keep the compass visible on the bench":
            "You lay the compass on the table, brass catching the lamp's dull light. It feels like a deliberate offering, a reminder that decisions are measured and not only emotional. Jonah's eyes flick to it and his expression softens."

    # --- merge ---
    "The scene continues"
    "Luca crosses the room in two strides, rain trailing from the hem of his jacket. He flicks his bandana, trying to make a joke."
    show luca_moreno at center:
        zoom 0.7

    luca_moreno "So? Do we get to mobilize or do we start a bake sale?"

    isla_morgan "No bake sale. We talk. We meet. We ask people what they'd take and what they'd lose."

    luca_moreno "And if they panic instead?"

    isla_morgan "Then we try to hold them. We give them plans that aren't just words."
    "His hand on your shoulder is familiar and solid; the touch should comfort, but the undercurrent is worry. His eyes are bright like a flare — you can see both anger and fear there."

    luca_moreno "You know what journalists do. They make simple headlines out of terrible things. They'll pick the worst picture."

    isla_morgan "Then we put the context next to the headlines. We show the models, the tradeoffs, the alternatives. We don't let opinion write the North Star."

    jonah_merrick "Words are wind to some folk. They'll look at charts and think of their boats, their children."
    "You look at the lab's window and the town outside seems smaller than it did this morning, compressed by the sky into something fragile and sharp. You have done what you believed was right. The thought is both an anchor and a weight."
    # [Scene: Promenade / Town Noticeboard | Early Evening — Meeting Announcement]
    hide isla_morgan
    hide jonah_merrick
    hide luca_moreno

    scene bg ch6_601bcb_2 at full_bg
    # play music "music_placeholder"  # [Music: Tension; percussion building into anxious pulses]
    # play sound "sfx_placeholder"  # [Sound: Shouts, a camera's mechanical click, the murmur of an assembled crowd]
    "The meeting forms fast — faster than your maps anticipated. People cluster in the floodlit shadow of the town hall. The air tastes of diesel and seaweed and the metallic tang of fear. Someone's child wails"
    "nearby; a dog is pulled close. Headlines already scroll on a handheld screen: DIVERTED CURRENTS? DAMAGED MOORINGS? SOME SCREAMS FOR HELP ARE ONLY ONE CLICK AWAY."
    "Aria Chen emerges from the cluster of council members, immaculate despite the drizzle. Her coat repels the rain like regulation. She steps onto the promenade steps with practiced calm, and the crowd opens a little around her because she has always moved through public space like a ruler of traffic."
    show aria_chen at left:
        zoom 0.7

    aria_chen "We will review the data. We will ensure safety."
    show isla_morgan at right:
        zoom 0.7

    isla_morgan "We didn't publish to scare people. We published because the numbers don't lie — the reef shifts currents in ways we need to plan for, not to hide from."

    aria_chen "And yet these shifts look dangerous in the press. We cannot have the town frozen by rumor while the tide rises."
    "A dozen hands raise like a nervous verdict. Voices overlap: fishermen worrying about moorings; a young mother asking if her pier will be taken away; an older man cursing the whole lot of you for changing their harbor."

    menu:
        "Step forward and explain the models, point to the charts":
            "You walk to the makeshift lectern, your voice steadier than you feel. As you trace lines on the chart, a few faces soften; others close their jaws. Your words are precise, but you can see the two kinds of listening: the one that wants to understand, the one that hears loss."
        "Let Luca take the lead and speak in plain terms":
            "Luca grabs the microphone and speaks in the warm, blunt way that gets people to lean in. He offers practical steps and volunteering shifts. The crowd cheers in places and hisses in others; his energy buys you a few minutes of common purpose, but the urgency doesn't leave the headlines."

    # --- merge ---
    "The scene continues"
    "A reporter elbowed forward, waving her phone like a talisman. The clip is shorter than you would like, a strip of your intention compressed into provocative frames. Within the hour a regional outlet spins an angle: REEF EXPERIMENTS ENDANGER BOATS. Panic scents the air like an oil spill."
    "Luca's jaw tightens when he catches the headline on someone's phone. He meets your eyes across the sea of people, and in that look there is accusation and a brittle, sudden grief."
    show luca_moreno at center:
        zoom 0.7

    luca_moreno "Did you have to release it now? Could you not—"

    isla_morgan "No. If we waited, someone else would have made smaller choices that forced us into larger losses. People deserve to know what could happen."

    luca_moreno "People also deserve time to prepare without hysteria. You gave them a week and a panic."
    "His anger is not theatrical; it is the raw sound of someone who feels betrayed by a promise you both had: to protect the town by skill and care. You open your mouth and close it. Words feel like tools that might either mend or cut deeper."
    # [Scene: Salt Flats / Living Breakwater Demonstration Site | Night — Sudden Storm]
    hide aria_chen
    hide isla_morgan
    hide luca_moreno

    scene bg ch6_601bcb_3 at full_bg
    # play music "music_placeholder"  # [Music: Rapid, claustrophobic strings; thunder like a drumroll]
    # play sound "sfx_placeholder"  # [Sound: Wind howling, ocean bottles clashing, a nearby engine coughing and dying]
    "They decide to try the retrofit immediately — volunteers, rope, engines. Panic accelerates logistics into improvisation: boats launched without inspection, bolts driven without torque checks, volunteers pressed into roles they'd never done. You'll tell yourself later"
    "that you should have stopped it; in the moment, your hands move because action still feels preferable to paralysis."
    "The storm arrives as a bruise: wind that cuts like an edge, rain like thrown nails. Work lights glare off salt-slick wood into a strobe of confusion. You taste copper and fear."
    "Jonah Merrick is there, because he'd always be there. He ties a line off a cleat with the practiced speed of a fisherman who has tied more than his life to a rope. A scarp —"
    "a sudden, violent notch in the sea floor — opens nearby like a snapping jaw. A small fishing skiff, halfloaded with volunteers, groans and heels. You see the boat slip and then tilt under a wave"
    "that looks like black glass."
    show isla_morgan at left:
        zoom 0.7

    isla_morgan "Hold the line! Keep the stern clear!"
    show luca_moreno at right:
        zoom 0.7

    luca_moreno "We're losing her!' (He lunges, voice raw. 'Hold the bow!"
    show jonah_merrick at center:
        zoom 0.7

    jonah_merrick "Get that rope!"
    "Hands everywhere, wet, fumbling. The world is reduced to the sound of the rope sliding and the pop of fibrous stress. For a moment things hang — the boat lurching, the light flashing — and then"
    "a muffled, impossible sound: timber breaking, a small, personal catastrophe edited into the larger noise of the storm."
    "Silence slices the immediate aftershock: a single, small human absence where before there had been a life. Someone screams — not loud as a radio but a cut-through sob that has no contour except grief. You taste salt and the metallic ring of loss."
    "Jonah Merrick comes down hard on the ladder as he throws his weight to stop the boat and takes an angle of the wet deck that shouldn't have been possible for him at his age. He"
    "goes down with a thump that sounds like an old door finally given up. The line slips from his fingers."
    "You run. You pull at Jonah's shoulder and find that his face is more mapping of pain than bone: a white film of shock around one eye, blood braided into his stubble. His breath is a bad, wet sound."

    isla_morgan "Jonah! Hold on. Tell me where it hurts!"

    jonah_merrick "My leg...can't...feel it."

    luca_moreno "We've got to get him to the promenade. Someone call an ambulance. Now."
    "You move like a machine; the motions you practiced in simulations become practical liturgy: stop the bleeding, keep him warm, call for help. But your hands know the small impossibility of stanching everything that is broken."
    "Aria Chen appears at the edge of the fray as if summoned by the crisis. Her voice is steady, sharp."
    hide isla_morgan
    show aria_chen at left:
        zoom 0.7

    aria_chen "This is exactly why we can't trust experimental projects to substitute for comprehensive infrastructure! We need the fast-track development now — proper defenses, professionally built, with funding we can count on."
    hide luca_moreno
    show isla_morgan at right:
        zoom 0.7

    isla_morgan "This wasn't what I wanted. We were trying to—"

    aria_chen "Intentions don't patch decks, Isla. They don't hold moorings against a scarp. The town is hurting — we need certainty."
    "Luca, exhausted and furious, turns on you with a blow that was never meant to be physical."
    hide jonah_merrick
    show luca_moreno at center:
        zoom 0.7

    luca_moreno "You told us you'd be careful. You promised we'd get people ready. You published and then let things happen too quick for caution."

    isla_morgan "I published to make them choose with facts. I didn't expect this — I didn't expect to lose—"

    luca_moreno "Intentions again. And a boat sank and Jonah is hurt and Aria will hold this like a cudgel."
    "His words land with a weight you feel all the way through your ribs. The fracture between you is sudden and crystalline, and in it is a grief beyond blame: a human equation where your variables"
    "collided and the outcome is pain. He storms away, voice swallowed by rain. You want to call him back and you don't know if you can."

    menu:
        "Stay with Jonah and help the medics":
            "You kneel by Jonah, hold his hand while the medics do what they can. His eyelids flutter; he squeezes your fingers in a small, pained recognition. Your chest is a raw, open place, full of the helplessness of care."
        "Run after Luca to stop him from leaving":
            "You catch Luca as he disappears between cranes. He collapses against a piling and turns to face you with eyes rimmed red. You can say nothing that will undo the boat or the injury, but you can put your hands on him and let both of you tremble."

    # --- merge ---
    "The emergency response continues"
    "The siren finally arrives, howling like a mourning animal. Stretchers are carried up the wet slope. Cameras still glide, capturing the choreography of emergency. Someone chants for accountability, someone else for answers. The harbor smells of oil and burnt rope and the thin metallic tang of someone else's blood."
    "Aria moves through the press with the ease of someone who knows how to spin a narrative. She stands beneath the promenade lights and speaks with the gravity of a policymaker holding the line."

    aria_chen "We must act now to secure Greyhaven. This incident proves we cannot leave our fate to experiments with unknown downstream effects. I will propose an immediate fast-track. We will secure investment and begin professional construction."

    isla_morgan "You'll bulldoze what remains of our flats and our fisheries!"

    aria_chen "I will secure safety and jobs. That is leadership."
    "Her words are precise, the politics polished into a blade. The crowd fractures into those who want immediate action and those who want to resist losing what remains."
    "Luca returns later, his face windburned and hollow. He avoids your eyes until, finally, there is no more avoidance left."

    luca_moreno "You said you'd hold us — me — to a certain standard. You said you'd be cautious. You made this public and then the town moved faster than any of us could manage."

    isla_morgan "I believed I was making space for agency. I believed knowledge would allow better choices."

    luca_moreno "But panic took the space you opened. And now Jonah—"
    "He stops because no words can take back the boat, the injury, the blood on the planks. Your hands are salt-slick with it. You don't know which you are more ashamed of: the misread of consequences or the illusion that science alone would be a salve."
    "You look out across the harbor and see a skyline made of low houses and broken boats that weep in the light. The town is rearranging itself into a new vocabulary: loss, accusation, a demand for protection that may come at the price of what the town has always been."
    # [Scene: Promenade Overlook | Night — Evacuation]
    hide aria_chen
    hide isla_morgan
    hide luca_moreno

    scene bg ch6_601bcb_4 at full_bg
    # play music "music_placeholder"  # [Music: A slow, mournful cello; wind-swept harmonics]
    # play sound "sfx_placeholder"  # [Sound: Evacuation sirens keening, a child's muffled sob, the low murmur of many conversations]
    "Evacuation notices go up — an official, brittle paper slapped to a lamppost; a council announcer repeats instructions into a megaphone. The word 'evacuate' has an administrative finality that feels like a verdict. People shuffle with"
    "duffel bags, hands on others' shoulders, the town made into a procession of fragile things."
    "You stand on the promenade edge and press your palm to the cold iron railing. The salt on your skin dries into a strange, chalky map. You think of the small boat slipping under a wave,"
    "the look in Jonah's face as he crumpled, the sudden break between you and Luca that feels less like an argument than a fissure carved by pain."
    "Jonah Merrick watches from a stretcher as they wheel him past. His eyes find you, and for a heartbeat there is no blame in them — only the tired steadiness you have always loved: a kind"
    "of weathered absolution. He squeezes your hand once, so faint you might have imagined it."
    show jonah_merrick at left:
        zoom 0.7

    jonah_merrick "Do the work, lass. Even when it costs."
    show isla_morgan at right:
        zoom 0.7

    isla_morgan "I will. I don't know how to do it right yet."
    "Above the town, lights from emergency vehicles throw long, shuddering beams across the water. A gull rides the wind and disappears into the dark. The skyline weeps: lights blink on and off as homes are closed,"
    "shutters banged. Somewhere a radio repeats instructions about safe routes and shelter allocations. The human soundscape here is made of small, resolute acts: doors barred against the night, a neighbour offering a blanket, someone singing a"
    "hymn under their breath."
    "You feel the town's unravelling as a physical thing — frayed ropes, the slow, unstoppable drawing out of stitches. Your data, once a tool you expected to shape choice, has become a catalyst that hardened fear"
    "into policy and politics into a tool for power. Aria's fast-track line has already started to gather votes; crisis has a way of making certainty sound like salvation."
    "You think of your father's compass — the brass heart you keep — and of the many small levers you pulled in this day. Each move made sense in isolation. Together, they feel like a tangle you did not see until it was too tight to undo."
    "Luca stands a few meters away, his profile cut against the wet light. He does not come to you. Instead he watches the harbor like a man who has lost his map."
    "You lower your head and let the rain claim your face. The sirens build into a chorus — urgent, final. The town moves as a single, wounded organism toward the nearest shelter."
    "You realize with a cold clarity that your choice to publish accelerated the town's unravelling. It opened a path where panic met improvisation, and in that volatile seam people were hurt. The science you wielded to"
    "protect has become, in the public eye, one reason to push for an expensive development that will reshape Greyhaven in ways you did not intend."
    "For a long moment you do nothing but watch the harbor take one more small life from the night, and the image nests itself in your chest like a stone."
    "You think of what 'protect' will mean now: more concrete, different hands, likely with strings attached. You think of Jonah's pained face, of Luca's hurt, of Aria's hands already drafting a resolution."
    "The evacuation sirens clang through the rain like a hand striking a bell. The skyline — always singing with the fragile lights of home — weeps in reflected amber. People move beneath the lamps, small and definitive."
    "You close your eyes and listen to the town you love being remade into a different kind of safety, and you understand how thin the margin between care and harm can be."
    hide jonah_merrick
    hide isla_morgan

    scene bg ch6_601bcb_5 at full_bg
    "THE END"
    # [GAME END]
    return
