label chapter14:

    # [Scene: Solhaven Promenade | Dawn]

    scene bg ch11_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense BGM — a low, driving pulse with discordant strings]
    # play sound "sfx_placeholder"  # [Sound: Distant horns, the thud of boots, a shouted count]
    "You moved here from the Commons with a rope looped over your shoulder and the taste of metal on your tongue — the memory of the tide pulling at foundation posts, the way it had taken"
    "a life once and left a hollow behind your ribs. You chose to escalate. The choice throws a current that pulls everyone into motion."
    "The promenade is a narrow strip of shore crisscrossed with construction markers and temporary floodlights. Concrete ribs jut from the sand like the exposed bones of a plan someone thought would outlast the sea. People cluster"
    "in ragged groups: volunteers with wet hair and handmade signs, local fishers in stained coats, college interns in bright vests, a few legal observers with badge lanyards. A line of uniformed security and municipal officers forms"
    "along the fencing, faces set like flint. Between the two, you stand with Rae, Tommy, and a handful of others who look at you as if you are a map for what comes next."
    "Rae bounces on the balls of her feet, stencil boards under one arm, breath hot in the cold air. 'We can block the trailer access. If we lock down here, they can't stage heavy equipment,' she says, voice sharp with adrenaline."
    "Tommy rubs his hands together, the motions more about habit than warmth. 'We don't want people to get hurt, Mara. You know that. If they push, the tide's near high. That ramp's slick.'"
    "You feel the damp of the morning in your boots, the salt-sour smell of exposed seaweed and diesel. Your hands remember the boardwalk planks of the Commons, the places you planted seedlings that survived a hundred"
    "tides. Each image is a small, stubborn proof that place matters. You breathe and the air feels like paper — fragile and easily torn."
    show elias_navarro at left:
        zoom 0.7

    elias_navarro "Mara, we can still—(he searches for the right term) —apply pressure through the injunction. Media coverage helps. A staged blockade risks escalation and arrests."
    "Rae snorts, not unkind. 'Staged? This is real life, Elias. They're moving dirt tomorrow unless we physically stop them. Laws don't stop a bulldozer that's already in.'"

    elias_navarro "I know. I'm not saying don't act. I'm saying plan the action to protect people. Get a legal team on standby, map exit routes, keep medics close."
    "You feel the word plan like a glove — useful, but not always a fit. Plans in the courtroom mean delay; plans at the water's edge mean paperwork while the tide rises. You remember the promise"
    "you made, the one that sits under your copper bracelet: to make space that saves lives, not just scores. That promise is heavier than any banner you could hold."
    hide elias_navarro

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Handcuffs clicking; someone crying out; the crowd chanting]
    # play music "music_placeholder"  # [Music: Percussion rises — heartbeat tempo]
    "When the first line of officers steps in, the crowd swells. You lock eyes with a woman two rows back — Mrs. Halvorsen from the Commons collective, who planted marsh grass with you last spring. Her"
    "jaw is clenched, and a small child clings to her skirt. The officers start taking names. They begin with those nearest the fence."
    "Celeste Park appears as if she's stepped out of a brochure: trench coat buttoned, portfolio under one arm, eyes like silver coins catching light. She walks the line with an executive's measured pace, the crowd's noise"
    "folding around her. Her presence is immaculate and jarring against the grit. She doesn't need to shout to be heard."
    show celeste_park at left:
        zoom 0.7

    celeste_park "This is regrettable,' she says, voice smooth. 'Construction delays cost jobs and funding. You must understand—businesses are watching Solhaven. The promenade secures the town's future."
    "You want to tell her about the things she'd call 'regrettable.' About the tidal breach that ate a porch and a brother. About the marsh you planted where kids learned to hide fiddler crabs in cupped"
    "hands. But Celeste Park's voice is made to convince and to close space for doubt."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Your 'future' is built on foundations you don't trust to stand in a storm. You call us regrettable while you pile steel on the shore."
    "Celeste Park's mouth thins. She inclines her head the smallest amount, polite, unreadable."

    celeste_park "Then we disagree about what trust looks like, Mara. I would prefer it not turn into chaos."
    "Her hands are empty; her words are not."
    "An officer steps forward and grips a young volunteer by the arm, hauling them toward a police van. Shouts rise. Rae plants herself and starts chanting, a rhythm that feels like a heartbeat. A line of"
    "bodies links arms. The first arrests are messy, public and humiliating. A man you recognize — a volunteer who'd taught kids to build bird boxes at the Commons — is pushed to the wet sand, cuffs"
    "biting into his wrists. The scene compresses into a single painful image: sunlight on salt and the dull red of a scraped palm."
    "Your chest tightens until the world narrows to the sound of your own breathing and the sharp edges of anger."

    menu:
        "Lock arms with the chain":
            "You step forward and loop your elbow through the rope, palms sticky with salt and sweat. The officer's hand lands on your shoulder; you can feel the press of their uniform through fabric. The crowd's chant swells and something in you steadies. || Choice B ('Call for a tactical retreat to the Commons') -> Reaction: 'You shout to Rae and Tommy, voice hoarse: 'Commons—now!' People turn, unsure. Some start moving; others freeze, watching those being led away. For a breath you are the harbor for indecision, and it lands like an accusation.'"
        "Call for a tactical retreat to the Commons":

    menu:
        "Confront the corporate attorney directly in the hallway":
            "You step out and call him by name, voice low and close. He smiles thinly, and the legal team stiffens. Your words are sharp; for a second the polished veneer cracks. || Outcome B: You grab Elias's sleeve and speak fast, practical. He listens, jaw working, and pulls out his tablet. For a brief, bright second you see the engineer — the person who sketches anchors and tolerances — and hope organizes the chaos."
        "Pull Elias aside to demand a focused legal timeline":

    jump chapter18
    return
