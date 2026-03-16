label chapter9:

    # [Scene: Glass Pier | Late Afternoon — Storm Shelf Approaching]

    scene bg ch9_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low, mechanical hum of security drones; distant gulls beaten silent by wind]
    # play music "music_placeholder"  # [Music: A taut string motif, tempo quickening]
    "You lead them along the pier like a current—people shoulder-to-shoulder, banners clinging to soaked poles, feet finding board where metal and glass meet wood. Your hand closes around the megaphone; the skin at your knuckles tightens."
    "The memo Jun flagged—what it reveals about thresholds and contingency clauses—burns under your tongue, and the way the cameras edge to frame conflict feels like a cold finger on the back of your neck."
    "Calder Voss's security lines are a moving wall of gray: hired men with neat caps and rainproof vests, a strip of corporate badges that read more like armor than identification. Police units form a perimeter farther"
    "down, their boots sluicing water off the pier in regular, efficient arcs. Somewhere above, an investor's feed blinks: a flippant graph, then a string of anxious emojis. The public eye is a lens that chooses a"
    "story before it sees the facts."
    "You lift the megaphone. Your voice is a rope thrown into wind."
    show ava_maren at left:
        zoom 0.7

    ava_maren "We are not—' (your words fracture as a gust cuts across the pier) '—going to be erased because someone prefers a tidy ledger to our lives."
    "Jun steps up beside you, recorder visible and small like a pulse-spot of stubborn light."
    show jun_park at right:
        zoom 0.7

    jun_park "Time-stamped. On the record. We have internal memos showing—"

    "Security" "Ma'am, step back. For everyone's safety."
    "The man from the security line speaks with a practiced, lulling cadence. He is not rude—he is efficient, and efficiency feels like a blade now."

    ava_maren "This is not about safety. This is about the right to stay. We have tenure. We have evidence."

    "Security" "We are instructed to maintain order. Please relocate to the designated area."
    "Ori Navarro is behind you, hands full of prototypes—small floating planters, braided with cords and algae, the little things you and he built to show beauty and function combined. His topknot is already damping at the"
    "edges from the salt in the air. He catches your gaze and gives you a grin that does not reach the eyes. In that instant, your chest is full of a dozen small loves and a"
    "dozen small accusations."
    show ori_navarro at center:
        zoom 0.7

    ori_navarro "Don't let them shrink this into a scuffle. Let Jun—let the recorder do the work. Let the cameras see what they need to see."

    ava_maren "And let them displace people while the cameras warm up?"

    ori_navarro "I—' (he swallows) 'I don't have a plan for the legal machinery. I have a plan for what's right at our feet."
    "Your mouth finds the megaphone again. Rain begins as a scatter of cold needles."

    menu:
        "Press forward into the cordon.":
            "You push your shoulders into the current of people, feeling the pressure of bodies and the immediate human will to not be moved. A security woman's jaw sets; an officer lifts a hand. The camera crews pivot to catch the confrontation."
        "Hold position and turn to Jun.":
            "You drop your hand to Jun's shoulder, a deliberate signal to delay spectacle for proof. Jun nods tautly; for a breath, the crowd breathes in with you."

    # --- merge ---
    "Continue with the scene as written below."
    # [Scene: Glass Pier | Moments Later — The First Slash of Storm]
    # play sound "sfx_placeholder"  # [Sound: A thunderclap that doesn't roll so much as drop; rain becomes a sheet]
    hide ava_maren
    hide jun_park
    hide ori_navarro

    scene bg ch9_3be532_2 at full_bg
    # play music "music_placeholder"  # [Music: Percussion shatters into dissonant drums]
    "The storm arrives like a verdict. It has no patience for rhetoric. The gusts buffet banners until wood cracks; the seaglass lights Ori wired flare and then cut out as a surge lashes the pier. Saltwater"
    "slams against the glass fascia and leaps onto the walkway in sheets that slick the boards and soak the hems of coats in seconds."
    "Someone shouts—words swallowed by wind. A drone dips, then rights, its rotors whining a high, frantic note. Cameras bob like gulls in a gale; angles that only moments ago favored confrontation now widen to show people clinging to railings, to each other, to any dry patch."
    "You can feel the megaphone vibrate in your hand, a thin, brave thing that suddenly sounds tiny."
    "Old Mara is at the front, her shawl a sopping, heavy mass of wool and salt. It hangs from her shoulders like a sodden net. She does not shout; she holds her place, head bowed against the rain, beads of her necklace clinking with the water's rhythm."
    show mara_old_mara_tetu at left:
        zoom 0.7

    mara_old_mara_tetu "Ava, child—"
    show ava_maren at right:
        zoom 0.7

    ava_maren "Mara—"

    mara_old_mara_tetu "Hold to the people. Do not let them make saints of our leaving."
    "Her words are simple and hammer-true. They hang between you as the first of the enforcement teams moves."
    "They are not subtle. Enforcement officers—formal now, with taped badges and thick gloves—walk door to door on the floating approach, their steps precise as if following a script. They tape notices to doors and shutters with"
    "methodical calm: IMMINENT HAZARD — RELOCATION ORDER. The language is clinical. The thresholds they use echo the memos Jun held up days ago—the same legal scaffolding you intended to dismantle publicly."
    "You see a family by a stoop—young children with plastic bins, a woman balancing a box on her hip, a man staring at the notice as if it were a living thing. Boxes stack on porches"
    "like small altars. A child drops a toy; it spins in the rain and rests still."
    "Ori Navarro lunges for the planters, trying to shove them into a covered nook beneath an overhang. He fights the wind, the cords slipping through his wet fingers. His amber eyes flick to you—helpless, pleading, asking a question you do not know how to answer."
    "You run to him and grab his sleeve."

    ava_maren "Help me—"
    show ori_navarro at center:
        zoom 0.7

    ori_navarro "We're trying. That's what we do."
    "But the enforcement team is already at the next house. A notice is slapped onto a door with a practiced slap that sounds obscene in the downpour."
    # play sound "sfx_placeholder"  # [Sound: Jun's recorder is a thin, insistent whirl in your ear; his voice is close enough to be a punctuation]
    hide mara_old_mara_tetu
    show jun_park at left:
        zoom 0.7

    jun_park "—public path now obstructed by enforcement; community members are being issued relocation orders—"
    "You reach for the notice, for any piece of paper that could be torn and used as evidence, but a uniformed hand pins you back with polite force."

    "Officer" "Step back, ma'am. This is an emergency protocol."

    ava_maren "No."
    "They read you with the patience of a machine that knows it is following saved steps. Your refusal fractures into something like a sob and like a command at once."

    menu:
        "Shove the notice down, make it an exhibit.":
            "You yank the paper free, water darkening the ink. Cameras tilt in to record the action; a reporter shoves a lens close. A security man steps toward you like a predator closing a gap."
        "Pull Ori and retreat to the community cluster.":
            "You grab Ori's arm and pull him back. For a moment you are two bodies pressed against the storm, a human barricade where people can breathe. A child tucks behind your knees, eyes wide."

    # --- merge ---
    "Continue with the scene as written below."
    # [Scene: Saltway Quarter | Night — After the First Sweep]
    hide ava_maren
    hide ori_navarro
    hide jun_park

    scene bg ch9_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The storm has not ended; it scratches at the roofs like teeth]
    # play music "music_placeholder"  # [Music: A single low cello, bowed, insistent—minor]
    "You make your way back through Saltway the way you always have—by smell and by memory—only the smells are now of diesel and wet cardboard and the hot copper of panic. The tide has rearranged itself;"
    "boats bob where there was once a pantry, and pontoons that linked homes now float with slack moorings. The Tide Garden is a wet sculpture, plants flattened, their soil washed in soft rivulets that carry the"
    "garden's small life into the channel."
    "There are gaps where people are gone; shutters closed without a last light. When you find them, the moving crews are efficient and grave. They load family trunks onto vessels with a solemn choreography—their faces softened"
    "by professionalism but their eyes flat as ledger lines. Promises are offered in measured tones: temporary housing, expedited assistance, trauma resources—phrased to be administratively correct and humanly small."
    "A woman you know—Mrs. Vale, who ran the corner shop and baked a brittle biscuit that tasted of cinnamon and local salt—stands on her stoop with two boxes. Her hands shake. Her husband is arguing quietly with an officer; he looks like someone bargaining with fate."

    "Mrs. Vale" "They said 'for your safety.' They said they'd make it right."
    show ava_maren at left:
        zoom 0.7

    ava_maren "We will—' (the lie stalls) 'We'll make sure Jun runs it. We'll file an injunction. We'll—"
    "Your voice breaks on plans that already seem like fragile kites undone by the wind."
    "Ori Navarro is at your side, his hair soaked, his palms raw from hauling. He keeps glancing at the planters—some of them broken, soil spilled into the boards. He kneels, fingers in the mud like a priest tending a wound."
    show ori_navarro at right:
        zoom 0.7

    ori_navarro "I'm sorry. I thought—"

    ava_maren "For what? Making art? Making light? Not seeing this coming?"

    ori_navarro "For crossing a line between theater and strategy. For thinking beauty would bring people into our frame and not into theirs."
    "The exchange ricochets between you: accusation, apology, avoidance. It is not a tidy fight. It is a series of small, cumulative blasts—each one exposing the raw shape of your different failures."

    ava_maren "We told people to meet us. We said 'public hearings.' We exposed their memos—and they used our exposure as cause."

    ori_navarro "They always do what they have to. They have lawyers, Ava. They have fleets. We had only our faces and a megaphone."

    ava_maren "Our faces were supposed to be enough."

    ori_navarro "I know. I'm sorry. I tried to make them see."
    "You look away because looking at him is like holding a broken compass in your hand. You can measure your direction only in the absence of certainty."
    # play sound "sfx_placeholder"  # [Sound: A distant siren cuts through, then another, then silence like a punch-drunk breath]
    hide ava_maren
    hide ori_navarro

    scene bg ch9_3be532_4 at full_bg
    show mara_old_mara_tetu at left:
        zoom 0.7

    mara_old_mara_tetu "They moved my neighbor's Evens—said 'imminent.' He packed his ledger like a book of apologies and left. He had no time to collect the jars—he kept the jars on the shelf."
    "You kneel beside her. Your sleeve soaks in the salt and the story."
    show ava_maren at right:
        zoom 0.7

    ava_maren "We tried, Mara. We tried to stop—"

    mara_old_mara_tetu "Tried is a bruised word now. You did what you could with what you had. That is not the same as enough."
    "Her eyes are not accusing; they are cataloging truth—the kind that never softens into excuse."
    # [Scene: Saltway Community Hall | Small Hours — Dripping and Quiet]
    hide mara_old_mara_tetu
    hide ava_maren

    scene bg ch9_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain reduced to a persistent patter; voices low and raw]
    # play music "music_placeholder"  # [Music: Sparse piano notes fall like raindrops]
    "You sit with the remains of the night—mugs half-filled, a notebook whose pages smear when you turn them. People drift in and out of the hall: some to call family, some to sleep on leaned-together chairs, some to try to gather the legal files that might form a future defense."
    "Jun returns to the huddle, recorder steady but his face ashen."
    show jun_park at left:
        zoom 0.7

    jun_park "The footage—' (he breathes) '—it shows enforcement moving after we rallied. The angles are brutal. Some feeds show people pushing toward the cordon; other feeds show the notices taped afterward. Corporates are spinning it—'disorder justified intervention.' Investors are retweeting 'public safety.'"
    show ava_maren at right:
        zoom 0.7

    ava_maren "So our truth can be rearranged like a set of tide markers."

    jun_park "It can be. It will be."
    "Maya bursts in, rain-spangled and furious, ledger clutched to her chest."
    show maya_lin at center:
        zoom 0.7

    maya_lin "They moved Mrs. Vale's family tonight—told them to board a shuttle to the temporary housing hub. They say 'policy.' The council rep keeps repeating 'safety protocols' on live feeds. We look like the ones who started the chaos."
    "You stand, the floorboards creaking under your boots, and feel a new, raw thing open in your chest: a grief that tastes like anger, and beside it, the slow, heavy weight of responsibility that you have always carried."

    ava_maren "Where do we go when the place that made us now writes us out of the map?"
    hide jun_park
    show ori_navarro at left:
        zoom 0.7

    ori_navarro "We go where the people who stayed need us. We go where the plans we made can help the ones left behind."

    ava_maren "Some of them aren't left behind. Some were moved. They used our moment to clear them."
    "There, in the hush, heat flares—an incandescent, miserable clarity. The exposure that was meant to protect became the lever by which displacement was justified. The city's machinery is a machine with gears that bite hard and pull apart the seams you stitched together with care."
    # [Scene: Saltway Pier | Dawn — Aftermath]
    hide ava_maren
    hide maya_lin
    hide ori_navarro

    scene bg ch9_3be532_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Water slaps the pier in long, slow movements; gulls return in cautious flocks]
    # play music "music_placeholder"  # [Music: Low, sustained chord resolving into a single, minor note]
    "You walk the edge of the pier alone for a long time—because walking alone is how you measure what is left. Boxes are stacked in silent rows, waiting to be moved. A banner—once bright with slogans—lies"
    "half-submerged, some letters washed away. The Tide Garden stands like a wounded thing; volunteers are already dredging soil, attempting to salvage roots."
    "Old Mara appears at your shoulder without sound."
    show mara_old_mara_tetu at left:
        zoom 0.7

    mara_old_mara_tetu "People will talk. People will say we started a riot. People will say we were reckless."
    show ava_maren at right:
        zoom 0.7

    ava_maren "They will say worse. They will say our hearts were in the right place. But that won't put someone back."

    mara_old_mara_tetu "No. It won't. But there are those who stayed. And there is still salt in the soil. There is still hull to patch."
    "You fold your hands into yours. Your bracelet, the braided sea-glass and twine, is cold and wet. You rub it until the beads sing against each other."

    ava_maren "I thought if we made the story human—if we made it beautiful—people would see the lives behind the memos."
    show ori_navarro at center:
        zoom 0.7

    ori_navarro "You were right to try. You were right to bring them into the light."
    "You turn. He is closer now, rain in his hair drying into salt-stiffed curls, eyes tired and wide. There is a hollowness to the way his smile attempts repair."

    ava_maren "Right to try—yes. But the result—"

    ori_navarro "I know. I know."
    "He exhales as if letting go of a weight that he has been holding too long."

    ori_navarro "I can leave, Ava. I can go patch other gardens where no one will try to move them while we make a scene."

    ava_maren "Leave? Or be useful? Are those the only choices you have for redemption?"

    ori_navarro "They're the options I can see right now. I don't want us to be held together by this failure, by what we couldn't stop."

    ava_maren "Or we stay and rebuild what they wanted to take."

    ori_navarro "And maybe get ground down here until there's nothing left of us but the outline of what we tried."
    "The conversation spirals in ways neither of you can steady. You both know what the other means but neither says it—about long-distance promises, about the need to spread work to seed hope elsewhere, about whether personal love can be forged anew from civic loss."
    "You feel the tide in your chest—something rising and inevitable. The cost of public life sits between you: the need to hold community on one hand, and the irresistible pull of building more places, more prototypes,"
    "more defenses elsewhere with the other. The city has taken more than your plan; it has demanded you pay in personal currency too."
    "You walk toward the edge of the pier and look down at the water. The storm has left a new mouth in the shoreline; the channel is wider by a handful of meters. A small boat drifts, lugging boxes and a toolbox, people who are both neighbors and strangers now."
    "You close your eyes and let the wind speak. The salt stings like a truth across your face. You feel the shape of failure settle—not as a single collapsed moment but as a steady, dull ache that will follow each step."
    "You pick up your notebook. Its cover is damp; your pen slides out and leaves a smear. You flip it open and there, half-smeared, are the sketches of the living seawall—the plans that once felt like salvation. They are still there, water-dark but legible."
    "You press your thumb to the ink and feel its smudge on your skin."

    ava_maren "We did what we could with what we had."

    mara_old_mara_tetu "Then you must do the next thing."
    "You look at Ori Navarro—at Jun, at Maya, at the people who remained—and for a second, there is a hollow hush where words used to be. You do not know what form the next thing will"
    "take. You do not know if Saltway will ever be whole. You know only the small, hard fact that some were moved tonight and their boxes are on other piers, and the promises that paper-made will"
    "not heal the wet places in people's faces."
    "You fold the notebook into your jacket and let the rain finish its washing. The city behind you is already knitting new headlines, finding the easiest moral through-lines. You remember Jun's recorder clicking through the night; you remember the camera angles that turned desperate faces into evidence that justified removal."
    "You place your hand on the railing. The wood is cold. The tide pulls and releases like a slow, indifferent breath."

    ava_maren "I will keep building. I'll keep making plans. If we were reckless, let the reckoning be with me. I will not let this be the end of everything here."
    "Ori Navarro reaches for your hand and this time you do not pull away. His fingers are warm despite the cold, clumsy, and certain."

    ori_navarro "Then we'll build again. Maybe not where they expect. Maybe not the same way. But we'll keep making room."
    "You let the words settle. They are small. They are not enough. They are all you have in the face of a night that took more than it gave."
    hide mara_old_mara_tetu
    hide ava_maren
    hide ori_navarro

    scene bg ch9_3be532_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A single gull calls; it is answered by distant, uncertain voices]
    "You stand there as the sun edges up, not because the day heals what happened but because it makes time, and in time there is work to be done. There is grief to carry and a"
    "plan to rewrite. There is, stubbornly, a small, damaged seed of resolve that will not be washed away."

    scene bg ch9_3be532_8 at full_bg
    "THE END"
    # [GAME END]
    return
