label chapter6:

    # [Scene: Marsh of Tides | Night — Storm]

    scene bg ch6_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, urgent percussion mingled with an undertow of strings]
    # play sound "sfx_placeholder"  # [Sound: A distant tone — a warning alarm — then the ragged roar of wind and sea]
    "You thought you had bought the town a breathing room. The Arc's first segments had gone in with a gleam and a promise: a visible line between 'safe' and 'at risk.' You thought the compromise —"
    "a hybrid, a hand across the old divides — meant time. Enough time to plant cordgrass and train neighbors and teach Jonah the calibrations for sensors."
    "Now the night eats that thought."
    "The alarm blares across the marsh like a second tide. It cuts through the steady slurry of rain and mud like a fingernail. You feel it under the soles of your boots before you hear it,"
    "a vibration that matches the panicked drum of your pulse. The planting crew scatters; someone screams that the waves have come higher than the forecast. You taste copper and salt and the electricity of a plan"
    "ripped open."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "Jonah — get the crates! Secure the gear—"
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "I'm on it!"
    "He doesn't wait for your permission, only the way he always moves when it's down to muscle. His hands are already slick with mud; he slings a recovery crate over his shoulder. A child at the edge of the channel clutches at his sleeve, eyes wide."
    "You can smell diesel and wet rope and the faint sweet rot of overturned seaweed. The Arc is a ring of cold metal beyond the near line of pilings, its sodium work lamps throwing hard pools"
    "of light onto the water. You look toward the mouth of the channel you and the volunteers fought to keep open — the lifeline for migrating fish and the town's subtle hydraulics — and the lamps"
    "show something that stops your breath: a seam, a joint, flexing like a mouth."
    # play sound "sfx_placeholder"  # [Sound: The scream of pumps — then a stutter, like a breath caught half-expelled]
    hide maya_reyes
    hide jonah_reyes

    scene bg ch6_601bcb_2 at full_bg
    show dahlia_kestrel at left:
        zoom 0.7

    dahlia_kestrel "We've got a pressure anomaly. Field teams, stand by --"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "The seam — keep the channel clear! You can't seal both sides!"

    dahlia_kestrel "We designed redundancy. We prioritized—"

    maya_reyes "Prioritized what? My father's town? The fishery? We argued for that seam, Dahlia. We argued for it because it keeps life moving."

    dahlia_kestrel "No one designed a storm like this. We didn't forecast this magnitude; the models—"

    maya_reyes "You built with models. People live here."

    dahlia_kestrel "And I built to save as many as possible. We will mobilize the pumps. Containment teams, now."
    "Her reaction is complex — the public part of her is broadcast, calibrated; the private part hides in the small hiccup after she speaks. You can't tell if it's guilt or a cold logistical recalculation. Either reading fits, and neither comforts you."

    menu:
        "Wade into the surge to help anchor a crate":
            "You step into the pull of brown water, mud sucking at your calves. Jonah's grip is steady; together you heft the crate toward the boardwalk as the sea hisses past. The salt bites your throat and something hot like anger floods your chest — at the seam, at the sterile neatness of plans undone."
        "Stay on the elevated plank and coordinate evacuation":
            "You climb up, palms slick on the rail, and call names: who is missing, who needs the warmth of the community room. Your voice must be calm; you repeat instructions until they land. There is a hollow at your sternum, but the people on the planks move faster for your steadiness."

    # --- merge ---
    "Continue to the following narration."
    "The choice you make scuffs the texture of the night but does not stop it. Waves find the places engineers forgot to love. The pumps scream and then stutter; a joint at the seam where the"
    "Arc meets the channel buckles. Water sluices sideways with the eager cruelty of a thing that wants to fill every pocket of human comfort."
    # [Scene: The Arc / Construction Platform | Night]
    hide dahlia_kestrel
    hide maya_reyes

    scene bg ch6_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Intercoms crackle; a generator thrums under everything]
    show rosa_mendes at left:
        zoom 0.7

    rosa_mendes "Maya. We set up a route to the boardwalk. People are coming in with mattresses and flashlights. There are sirens on the promenade; Mayor Durant is organizing shelter."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "How many houses—?"

    rosa_mendes "We're moving everyone we can. The council is trying to triangulate emergency funding."

    maya_reyes "Dahlia — why did it fail there? We insisted on that channel."
    show dahlia_kestrel at center:
        zoom 0.7

    dahlia_kestrel "It wasn't a failure of intent, Councilor Mendes. It was an exceedance event. The retention calculations—"

    maya_reyes "Those retention calcs are meant for models. This is a town. The models don't look into the eyes of people who are losing their kitchen tables."

    dahlia_kestrel "We will take responsibility for operational failures. We will deploy repair teams and open the emergency fund. Our PR is on the way."

    maya_reyes "Responsibility is not a press release."

    dahlia_kestrel "You're right. It isn't."
    "The exchange spirals beyond the words. Reporters arrive: microphones like cold flowers thrust toward you. Their questions are rapid-fire, accusatory, hungry for a villain."

    "Reporter 1" "Who is at fault for the breach? Was this negligence?"

    "Reporter 2" "Ms. Kestrel, did your company cut corners to meet deadlines?"

    "Reporter 3" "Maya Reyes — you were part of the advisory team. What did you sign off on?"

    maya_reyes "I fought for the channel. We fought for a hybrid. We asked for community oversight. This is not just a technical failure — it's a human one, too. We will hold those accountable. We will also... we will also make sure our neighbors are safe."
    "The cameras flash and then turn. Faces. You see Jonah helping an old man climb to the boardwalk; his hoodie is shredded by marsh grass, hands clumsy but sure. You see Elias Kwan out on the"
    "water, a silhouette against sodium lamps, the rope cutting into his palm as he fights with lines to steady a boat. His jacket is open at the collar, salt drying into white seams. For a moment"
    "you don't know if relief or a new, hollow dread fills you when he looks back; the light reveals nothing definitive in the way his eyes hold you. His expression is a map of tired choices."

    menu:
        "Run out to the pier and help Elias secure the boats":
            "You pull on an extra jacket and sprint. The wind strips at your face. When you reach Elias Kwan, his jaw tight, you take the end of the rope. Your hands against his, you are both a tether and a witness — you hear the bone-deep fatigue under his words. 'We kept some out,' he says. It is both news and a wound."
        "Stay with neighbors and triage the injured":
            "You stay, kneeling in damp blankets, pressing a towel to a child's shivering arms. You patch a neighbor's ear with makeshift dressings, your palms smelling of iodine and coffee. Elias Kwan looks back once, then disappears into the light; the feeling that he is both near and unreachable sits heavy in your chest."

    # --- merge ---
    "Continue to the following narration."
    "Whatever small movement you make, the outcome is the same: the Arc's segment tears away like a page from a book someone else finished. The noise of it — a metallic groan, the sucked-out sound of"
    "air — settles like dust in your ears. In the afterlight, the town will have photographs of that tearing: a cold, clinical arc turned ragged by the sea."
    # [Scene: Boardwalk / Afterlight — Hours Later]
    hide rosa_mendes
    hide maya_reyes
    hide dahlia_kestrel

    scene bg ch6_601bcb_4 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano, descending, small strings]
    "You stand in mud up to your knees, field journal sodden, the pressed marsh grass inside the pages limp and brown. Your pen is ruined; ink has bled into a map of the night. The triumphant momentum you felt days ago has fractured into a thousand small reckonings."
    show rosa_mendes at left:
        zoom 0.7

    rosa_mendes "How many will lose their homes, Maya?"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "I don't know."
    "You say the words and they taste like iron. You think of your father's boat listing in a storm years ago and the way the town leaned into him afterward. You think of Jonah's hands, Elias"
    "Kwan's rope, the seedlings in the marsh that now drift like little corpses. 'I don't know. But we will count. We will build lists. We will find shelter. We'll—'"

    rosa_mendes "There's pressure to let them finish the build; insurance math isn't patient with slaughtered timelines."

    maya_reyes "Pressure from where? From people who don't feel the mud under their boots?"
    "You bite the question off. It is sharper than the taste of salt. 'We will push for community control of the recovery funds. We will document everything. We will hold them accountable — for the seam, for the sensor blind spots, for the way decisions were framed as inevitability.'"
    "Rosa nods slowly, the lines around her mouth drawn taut. 'The town is exhausted, Maya. They look to you because you made them believe something possible. They'll expect answers.'"

    maya_reyes "They should expect honesty and work."
    show elias_kwan at center:
        zoom 0.7

    elias_kwan "We lost three nets tonight. The east shoal's shifted. The boat at the second bend took on water. I thought we'd get more warning. Thought the barriers would hold."

    maya_reyes "I thought so too."
    "You want to tell him you are sorry; you want to tell him you trusted a promise; you want to tell him it wasn't all your fault. The network of blame is both more and less tidy than that."

    elias_kwan "We keep fishing or we get new work. People need paid now. What do we do, Maya?"
    "You are the person who has always turned questions into plans, who moved from grief into action when your father did not come back. But tonight the map of action is a torn thing. The marsh"
    "you love is sullied; seedlings you planted lie flattened and brackish. The town is bleeding jobs, houses, and trust."
    "You close your soaked journal. The pressed grass falls free like a small, dead thing. For a moment you cradle it as if it were a bird with a broken wing."

    maya_reyes "We start with the people. We patch what we can. We document. We call in repairs. We open the community rooms and stretch the food supplies. We mount a public accounting of the failure. And then — we rebuild differently. We don't hand everything over to a promise that looks tidy on a balance sheet."

    elias_kwan "Different how?"

    maya_reyes "More of us, in the plans. No sealed seams without local ops. Jobs tied to restoration. Training teams. And legal guards on any deployment."
    "Rosa listens, her expression unreadable in the way people become when they carry both duty and fear. Dahlia Kestrel stands near the wreckage, hands in her pockets, the company tablet dark in her grip. The reporters are still there, but their questions have thinned into a hum."
    hide rosa_mendes
    show dahlia_kestrel at left:
        zoom 0.7

    dahlia_kestrel "We'll fund the emergency repairs. We will offer transitional employment to those impacted. And an independent audit will be commissioned."

    maya_reyes "An audit doesn't bring homes back."
    "You are aware of the rawness of your voice. You are aware of how many angles of this story will be told by photographs and press releases. You are aware, too, of your own smallness in the face of structural failure."

    dahlia_kestrel "No. But it's a start."
    "There is grief threaded through the concession — and something else, too, a fractious, human hush where plans are remade in public. The town will remember this night in the faces of those who lost more"
    "than property. It will remember it in the way neighbors showed up for one another, in the way hands found each other in roiling water."
    "You sit down on the soaked boardwalk, the wood cold under your palms. Rain pats your hair. Jonah folds a blanket over your knees and then, without a word, moves on to the next person who"
    "needs covering. Elias Kwan doesn't quite sit; he perches, the rope a halo over his shoulder, and watches the horizon like a man mapping the future one shoreline at a time."
    "There is a particular, private failure you feel more acutely than blame or press conferences. It is the small betrayal of hope — the realization that your insistence on hybridism did not inoculate the town from"
    "harm. You had believed in a fit between people and engineered solution; tonight you learn how thin that seam can be when the sea pushes where you never dreamed it might."
    "You open your sodden journal and trace the smeared arrow you drew days ago: 'training + local ops = resilience.' The ink runs. The idea remains; the paper will not keep it whole. It will be"
    "your work to make that equation liveable even when the ledger is full of loss."

    maya_reyes "Tides remember."
    "You whisper the phrase; it is both prayer and logistics. 'We remember them back.'"
    "There will be inquiries and anger and, if you're lucky, change that grows slow and imperfect. There will also be neighbors who leave because the cost of staying becomes a calculus they cannot bear. There will"
    "be new faces in town working on scaffolded repairs, and old faces who count what remains. Your heart is a ledger now, balanced with grief and responsibility."
    # play music "music_placeholder"  # [Music: Quiet, minor chord — acceptance without peace]
    # play sound "sfx_placeholder"  # [Sound: A gull crying, distant, like a note unresolved]
    "You rise, mud on your knees, journal under your arm. Elias Kwan moves beside you. Jonah takes the end of a rope and, with muscular human steadiness, begins to haul a tarp across a ruined doorway."
    "Rosa walks ahead, already making lists in her head. Dahlia Kestrel stands where the light throws her like a statue; she will speak at council meetings and in press rooms and make offers that read well"
    "on paper. You will sit at those tables and you will argue, and sometimes you will win small things. Sometimes you will lose. That knowledge is its own gravity."
    "You tighten your jacket against the cold and smell, for a long, quiet instant, the bay's strange, bitter-sweet perfume — wet wood, seaweed, diesel, and the faint sweetness of spilled coffee cooling on a tabletop where"
    "someone will soon be counted as safe. Your father's voice returns, not as instruction now but as memory: Tides remember, Maya. Build for the remembering."
    "You set the journal down on a plank and let it sit, a sodden talisman. You cannot undo the night. You can only name what was broken, who it broke for, and begin the long, necessary work of mending in public. The town will be different. You will be different."
    hide maya_reyes
    hide elias_kwan
    hide dahlia_kestrel

    scene bg ch6_601bcb_5 at full_bg
    # play music "music_placeholder"  # [Music: A single, low violin note that holds and then slowly releases]
    # [Scene: Fade Out]
    # play music "music_placeholder"  # [Music: Fade to quiet]

    scene bg ch6_601bcb_6 at full_bg
    "THE END"
    # [GAME END]
    return
