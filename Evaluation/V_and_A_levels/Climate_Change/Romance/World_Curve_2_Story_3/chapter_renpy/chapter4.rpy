label chapter4:

    # [Scene: Glasshouse Lab & Seedbank | Dusk]

    scene bg ch4_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Quickening strings under a percussive, urgent rhythm]
    # play sound "sfx_placeholder"  # [Sound: Low hum of pumps, distant gulls, the slap of a canvas tarpaulin outside]
    "You step into the glasshouse with your coat still flecked by rain — the world outside streaked and raw — and the air here wraps around you like a wet blanket, warm and thick with the"
    "scent of salt and growing things. Your palms smell of kelp and solder; your fingers still remember the knot you tied to mark the first long-line. Tonight, there is no slow, steady planning. Tonight the town"
    "moves."
    "Kaori 'Kai' Matsuda is already there, sleeves rolled, braid catching the light like a neon tracer. She is speaking with Mika over a spread of schematics pinned to a rusted lab table, her hands cutting the"
    "air to underline points. The solar strips — thin, flexible panels Kai has been stitching into canvas — are stacked in neat coils. They look almost defiant against the old wood of the workbench."
    show kaori_kai_matsuda at left:
        zoom 0.7

    kaori_kai_matsuda "If we anchor the panels to pilings and string the lines in a staggered pattern, the shadowing will reduce wave stress and still let the kelp breathe. We can have the first array online by dawn if we push."
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "We can, but we need anchors and boats and someone to manage volunteers at the flats. Amalia's got the volunteers, right? Mika?"
    show mika_tran at center:
        zoom 0.7

    mika_tran "Amalia texted an estimate. Fifty if you count families who can hand a rope. More if you count the kids. I made a checklist — pumps, clips, two spare spare drills."

    kaori_kai_matsuda "Then we stop talking about lists and start mailing them bolts. I hate bureaucrats who say 'we'll see' and mean 'we'll do nothing.'"
    "You watch Kaori 'Kai' Matsuda move — precise, fierce. The urgency in her voice tacks the moment higher. Your chest tightens: the plan is finally breathing, but it is fragile, threaded through people who are already stretched thin."
    "Your father taught you how tides speak through wet sand. You were supposed to be the quiet scientist, the patient one. Instead you feel like a match-head: lit."
    hide kaori_kai_matsuda
    hide marina_reyes
    hide mika_tran

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Zip of canvas, clink of metal]
    "Kaori 'Kai' Matsuda looks at you, the smile softening for a heartbeat."
    show kaori_kai_matsuda at left:
        zoom 0.7

    kaori_kai_matsuda "You doing okay? You look like you swallowed a storm."
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "I'm fine.' (it comes out small) 'I'm thinking. We're moving fast, Kai. I keep seeing — my father, the house before the flood. If anything goes wrong—"

    kaori_kai_matsuda "So don't let it. Delegate. You're not a single rope, Marina; you're the whole pulley system. Let people pull. They'll surprise you."
    "You want to argue — you want to say you don't get to be tired; not with the town on a map that could disappear. Kaori 'Kai' Matsuda's eyes go softer, and for a second she"
    "looks less like a marching rally and more like someone who has chosen this life because she couldn't stand by. The lab smells of algae and solder and old coffee, and beneath that, the salt-sheened grief"
    "you carry."

    menu:
        "Take a breath and make a list":
            "You let your shoulders drop a fraction, breathe into your belly, and call out tasks. Your voice steadies. Mika nods and snaps a photo of the checklist for distribution."
        "Jump straight to the docks":
            "You push past the bench, heart hammering, and grab an armful of solar strips. Kaori \'Kai\' Matsuda smirks and falls in beside you — the practical flurry begins."

    # --- merge ---
    "The team moves toward the tidal flats; the night accelerates."
    # [Scene: Laurel Bay Tidal Flats | Dusk → Night]
    hide kaori_kai_matsuda
    hide marina_reyes

    scene bg ch4_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: A tight, staccato motif — percussion rises; wind strings layer in]
    # play sound "sfx_placeholder"  # [Sound: Boat timbers creaking, gulls calling less and less as the sky bruises]
    "You move from the lab into the flats where the town's edges blur into the sea. The air is colder here; salt spray stings your face. Volunteers are gathering: fisherfolk with foam-scarred hands, teenagers with headlamps,"
    "Amalia holding a damp clipboard like doctrine. Lanterns swing, casting warm islands against the wet. The first long-line is a promise unspooled between boats, and everyone who touches it adds weight."
    show amalia_reyes at left:
        zoom 0.7

    amalia_reyes "We have families signed up to anchor rotations. Old Tom brought two of his crew. I shifted the festival volunteers to logistics — they'll hand out hot broth, keep the kids away from splices."
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "Good. Tell the team to watch for one another. If the company sends anyone to harass the boats, we fall back to the staging point. No one goes solo."

    amalia_reyes "You and Kaori \'Kai\' Matsuda wrote that rule.' (a beat) 'You don't have to say it now, but—"
    "You feel the old, familiar ache in your chest: being the one who keeps the map of safety in your head. You remember your father's voice, the way he hummed while patching nets, the ledger of"
    "tidal markers he'd kept. You did not swear to fight the sea alone — you swore to hold the town steady. But how many people should you ask to stand with you against hired machines and"
    "legal threats?"
    "Old Tom arrives, heavy breath fogging the air. He smells of tar and rope. You watch him steady a post with the deliberateness of someone who has learned to pace his hands against storms."
    show thomas_old_tom_bellamy at center:
        zoom 0.7

    thomas_old_tom_bellamy "You know why I'm here, Marina Reyes. Your ma would've sent me if she could. We don't get many chances to pull the line ourselves anymore."

    marina_reyes "We need you. We need everyone's hands. The solar strips will slow the current nearshore and give the kelp a chance. If the company drives piles where those lines go—"

    thomas_old_tom_bellamy "Then they'll have a bay with a wall and no beds. Folks can't eat walls."
    "A boat horn blares far off — a sharp punctuation. The volunteers stiffen. The weight in your ribs tightens; adrenalin moves through you like a current."
    hide amalia_reyes
    show kaori_kai_matsuda at left:
        zoom 0.7

    kaori_kai_matsuda "Mika, clip those buoys. Amalia, rotate the people on the east anchor. Marina Reyes, check the lines on the south boat. We go on three."

    marina_reyes "Three."

    menu:
        "Speak plainly to the fishers — ask them to risk it for heritage":
            "You walk along the line, hands on rough rope, and speak of tides and nets and what the bay used to look like. A few nod with the memory of their mothers' names, and they tighten their grips."
        "Offer stipends and equipment — call in favors":
            "You promise small stipends, offer a battery of shared drills, and the town's mechanic pledges fuel. A skeptical few blink, then nod; practical help loosens some hands."

    # --- merge ---
    "The long-line is secured and volunteers take their positions as night deepens."
    hide marina_reyes
    hide thomas_old_tom_bellamy
    hide kaori_kai_matsuda

    scene bg ch4_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The metallic thrum of a portable winch; voices layered in determined chatter]
    "The night moves faster than you can catalog. Kaori 'Kai' Matsuda clamps a solar strip to a pilings' weathered face, the neon braid flashing like a warning. Mika hauls a spool; Amalia marshals people with the"
    "steady, soft urgency of someone who knows how to make a village work. Every small victory — a tightened knot, a functioning clip — tastes of salt and fear."
    "Beneath all the clatter is a thudding counterpoint: the knowledge that a lawsuit, a trespass notice, or a line of heavy equipment could undo this work in an hour. You feel each possibility like a tide pulling at the ankles."
    # [Scene: Municipal Hall Construction Site | Late Night]

    scene bg ch4_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Percussive drums and rising dissonant strings; a single brass note rings intermittently]
    # play sound "sfx_placeholder"  # [Sound: Distant idling engines, the occasional shout, rain tapping a metallic rhythm]
    "You and the volunteers approach the construction boundary. The municipal hall's pale concrete looms, but tonight it's the construction zone that holds the town's breath. Bulldozers crouch like sleeping beasts. Floodlights cut the darkness into slices."
    "The company's temporary trailers glow with interior lamplight; men in hard hats move like phantoms."
    "Rina's voice is a thin thread over the phone — Rina, with her municipal office posture, professional and dry. She has always been good at softening edges into files and deadlines."
    show rina_corbett at left:
        zoom 0.7

    rina_corbett "Marina Reyes. This is not a private demonstration. We can talk in the morning, but you and your people are at risk. There will be legal consequences if you impede construction."
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "Rina, we told you about the ecological surveys. You know the beds are there. The long-lines are a mitigation, not a stunt."

    rina_corbett "I know the biology. I also know the company has permits. My hands are tied by municipal obligations. I don't want arrests on my desk, Marina Reyes."
    "Your mouth tightens. Rina's words are formal, but there is an edge of genuine worry — not necessarily for the same things you worry about. Legal consequences are not abstract. They will reach into people's homes and bank accounts and histories."
    show kaori_kai_matsuda at center:
        zoom 0.7

    kaori_kai_matsuda "Let them file papers. We'll file history. We'll put our bodies where the wall goes and name what they want to erase. You think they came here to save us?"
    "Elias Kato appears then, not in a hard hat, but in his trench coat, mud spattered on the hem. He watches the rows of people with that steady, measured gaze. When he steps forward, hands folded, the air between you and him tightens with unspoken pasts."
    hide rina_corbett
    show elias_kato at left:
        zoom 0.7

    elias_kato "Marina Reyes. I'm—' (he stops; the word catches) 'You're asking people to put themselves in front of machinery. There are safer avenues. Let me negotiate a pause with council and legal counsel."

    marina_reyes "How many pauses have we taken, Elias Kato? How many 'safe avenues' have given us a line item under 'study' and a banquette for the company's PR machine? People are hungry. Houses are at stake."

    elias_kato "And people getting hurt will give them all the leverage they need to push us into a corner. You know how these things go. A single headline — and the town will fracture."

    kaori_kai_matsuda "So we accept being slowly drowned? We accept slow attrition as if it's mercy?"

    elias_kato "I'm asking you to be strategic. To minimize harm."

    kaori_kai_matsuda "Strategic can mean cowardice when you're used to being safe. We've had enough safety."
    "Elias Kato looks at her, then at you, and for the first time tonight his amber eyes are not only observant but raw, as if he can feel the tug of the place in his chest."

    elias_kato "I won't sabotage you. I wouldn't. But I won't stand idly while people put themselves in danger either."

    marina_reyes "I don't ask you to sabotage anything. I ask you to see what this is before it's paper on a wall."

    elias_kato "I see it. I do. But I see other things too."
    "The exchange loops; partners and past lovers ping-pong under the floodlights. The talk is not gentle. It is loaded with the memory of a better argument and the residue of what you both once were. Voices"
    "rise as the company manager — a broad-shouldered man wearing white gloves that don't match the mud beneath his boots — approaches."

    "Company Manager" "Ladies, folk. This is private property. You need to disperse before we call for enforcement."

    kaori_kai_matsuda "We are not moving."

    "Company Manager" "Then we will escalate."
    # play sound "sfx_placeholder"  # [Sound: A heavy engine idles closer; a distant metallic clank — the first bulldozer is sliding into position]
    # play music "music_placeholder"  # [Music: Tension peaks — high strings, staccato drums, a low brass rumble]
    hide marina_reyes
    show rina_corbett at right:
        zoom 0.7

    rina_corbett "Marina Reyes — I'm telling you as a friend: there will be enforcement. They'll get permits expedited if you force it. I'm filing a notice to have a legal team stand by. Please, think about the people you're asking to stand here."
    "Your internal monologue is a cyclone. You calculate: volunteers' names, who has health problems, who drove in from the farther side of town. You remember your father's calloused hands, the ledger of markers he left —"
    "proof that someone had to mark the boundaries. You feel the weight of being the one who makes choices for others. The moral question coils in your stomach and grows sharp: who do you put at"
    "risk to keep a place from being paved?"

    elias_kato "Marina Reyes. If they call enforcement and someone lashes out, if machinery hits a rope, I won't be able to—"
    hide kaori_kai_matsuda
    show marina_reyes at center:
        zoom 0.7

    marina_reyes "You don't have to promise anything. Just don't pretend there are no stakes."
    hide elias_kato
    show kaori_kai_matsuda at left:
        zoom 0.7

    kaori_kai_matsuda "And if we back down now, they'll come back tomorrow with more permits. We lose ground twice."
    "The night air tastes like iron. Lanterns bob; faces are lit from below with resolve and fear. The company's floodlights sweep the line; cameras mounted on a trailer pivot like watchful birds. The bulldozer's blade rests like a jaw, ready to bite."
    "Everyone looks to you. Your buoy pendant — hidden under your sweater — weighs like a secret verdict against your sternum."
    hide rina_corbett
    hide marina_reyes
    hide kaori_kai_matsuda

    scene bg ch4_453e40_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The whine of diesel, murmurs across the crowd]
    "You can feel the town's breath at your back. This is the most electric it's ever been since you returned: anger, grief, love, fear braided into a single rope. The moral calculus is not arithmetic. It is a living tangle."
    "Page-Turn Moment: You inhale the cold air and feel it go into the place that organizes your decisions. All the small wins tonight sit like lanterns along the line, and beyond them the heavy machines sit"
    "like a question. You realize the next hours could define what this town keeps and what it loses. Saying nothing is a choice that will be heard by history. You take in the sound of engines,"
    "the glow of floodlights, the quiet resolve of people who have come because they believe you. For a breath, you let the weight of all those hands and names press into you, not as blame but"
    "as trust. The thought is a kind of liturgy: if we stand, we stand together. If we fall, we fall together."

    scene bg ch4_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Single sustained chord, then a held silence where every footfall seems amplified]
    # play sound "sfx_placeholder"  # [Sound: Engine rumble, then the distant click of cameras]

    scene bg ch4_453e40_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
