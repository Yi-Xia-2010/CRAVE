label chapter20:

    # [Scene: Town Streets | Night — Storm Approaching]

    scene bg ch14_dff609_1 at full_bg
    # play music "music_placeholder"  # [Music: Rapid, staccato percussion building into a pounding tempo]
    # play sound "sfx_placeholder"  # [Sound: Distant sirens, the thump of sandbags being stacked, the wet slap of rain beginning to fall]
    "You step out of the municipal building and the air hits you like a slap: cold, salt-laden, metallic. It tastes of old promises and new panic. Your phone buzzes in your pocket — another legal notice,"
    "another plea — and you leave it there. There are more urgent vibrations: the town itself, reacting."
    "Tommy is already two steps ahead of you, shoulders hunched under a soaked beanie, shouting over the wind. His voice is a rope trying to hold something in place."
    show tomas_tommy_reyes at left:
        zoom 0.7

    tomas_tommy_reyes "Mara! The corner by the fish market's flooded past the knee. We can't get the truck through. A few folks are cut off on the lower boardwalk."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Where exactly? Names."

    tomas_tommy_reyes "Gonzales family, three—Mrs. Keene from the bakery—two volunteers stuck at the promenade anchor. Tide's coming faster than the models said."
    "You taste your own mouth — salt, fear, iron. Your gut clenches around a familiar memory: the sibling you couldn't save, the sound of a siren that didn't come in time. That old ache sits under your ribs and pushes you to move faster."
    hide tomas_tommy_reyes
    hide mara_lin

    scene bg ch14_dff609_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Radio chatter, clipped and urgent]
    "Dr. Amina appears at the edge of the makeshift command post, hair damp, face drawn but controlled. She hands you a tablet with a map pulsing red."
    show dr_amina_bhatt at left:
        zoom 0.7

    dr_amina_bhatt "Surge model updated. Wind shift—adds three to five feet at the promenade's exposed section. The half-finished seawall will not hold. We need to triage response zones now."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Timeframe?"

    dr_amina_bhatt "Fifteen minutes to the first crest. Thirty to peak. If we don't move people off the promenade, they're at highest risk."
    "Elias Navarro comes up behind you, jacket plastered to his shoulders. His jaw is tight. He folds and unfolds a laminated evacuation protocol with fingers that are trying to be steady."
    show elias_navarro at center:
        zoom 0.7

    elias_navarro "Command sent a priority list: hospitals and critical infrastructure first. It's—"

    mara_lin "Our gardens, our homes, the people on the boardwalk—those are infrastructure, too. You know that."

    elias_navarro "I know. But I have to follow the directive. If I divert resources and the hospital loses power, the casualty count could be different in a way the system hates."
    "There's a weight in his voice — not just professional care, but human hesitation. He wants to be helpful in a way that doesn't break whatever authority he's tethered to. You see the gears running behind"
    "his eyes: models, liability, the promise he feels to something bigger than the town. It makes him careful. You want him to be less careful."
    "Celeste Park arrives in a compact SUV that makes a clean, impossible line through the chaos. She steps out with a coat buttoned against spray; her motions are precise. She looks at you, then at the"
    "map, then at the crowd, and you can't tell whether she is calculating risk or theater. Her expression is complex — unreadable in full."
    hide dr_amina_bhatt
    show celeste_park at left:
        zoom 0.7

    celeste_park "I have two contractor boats staged at the north pier. They'll be ready to ferry if you authorize access. They'll work faster than your volunteers."

    mara_lin "What's the catch?"

    celeste_park "No catch. We need to keep the site from collapsing. We can't have a public relations disaster on top of a meteorological one."
    "You don't trust that 'no catch.' You also don't have time to unspool everything you suspect. The storm's first teeth are already scoring the town."

    menu:
        "Send a volunteer crew to the promenade now":
            "You point to the boardwalk and bark orders; hands grab ropes and breathes hitch but resolve hardens — volunteers sprint toward the promenade."
        "Authorise Celeste's contractor boats for the promenade":
            "You give a nod to Elias; Celeste's team moves with studied efficiency, loading harnesses and lines as the lights on their vehicles glow clinical and alive."

    # --- merge ---
    "Continue"
    # [Scene: Saltwren Commons | Night — Rising Water]
    hide mara_lin
    hide elias_navarro
    hide celeste_park

    scene bg ch14_dff609_3 at full_bg
    # play music "music_placeholder"  # [Music: A low, insistent drone beneath a frantic violin line]
    # play sound "sfx_placeholder"  # [Sound: Shouts muffled by rain, the creak of wet wood, water lapping against planters]
    "You push through a spray of wet willow and a chorus of voices. Rae is there, soaked to the skin, her camera useless but her voice loud enough to cut through panic."
    show rae_carter at left:
        zoom 0.7

    rae_carter "We have two kids trapped near the greenhouses! They've got a teacher with them, but the path's gone. The boardwalk snapped toward the west—no safe approach from land."
    "Your hands move before your thoughts finish. You hand out life vests, loop a rope around your waist, and test the pull of the tide. The Commons is your domain; you know every plank that groans,"
    "every rickety railing that has kept a seedbed from going under. This is a map you can read blind. So you do."
    "Tommy is at the helm of a borrowed skiff, teeth clenched, revving a sputtering engine. He looks at you like he's asking permission to be reckless."
    show tomas_tommy_reyes at right:
        zoom 0.7

    tomas_tommy_reyes "I can go. Shortest run. But if that line snaps—"
    show mara_lin at center:
        zoom 0.7

    mara_lin "We rig a secondary tether. Two lines. You'll have Rae on the bow with a pole. Amina, you're on comms with command. Elias—get me the contractor boat's ETA."
    "Elias Navarro fumbles the radio, then slams down a call to his superiors. The voice on the other end is flat, procedural, the kind of voice that unhooks the human detail from urgency."
    hide rae_carter
    show elias_navarro at left:
        zoom 0.7

    elias_navarro "We're diverting one small-craft allocation to the Commons. Yes—yes, it's temporary."

    "External Voice (over radio)" "You can't reassign without authorization. The hospital—"

    elias_navarro "We will keep a comms line open. If the hospital needs it back, we'll return it. But there are children trapped. I can show you live feed."
    "He presses the tablet to the camera feed and shows the trembling thumbnail of Rae's recording: small figures huddled under algae-streaked glass. There is no time for labored approvals; there is only the hollow thump of a heart and the water taking more room."
    "Dr. Amina shoves a hand into the back of your jacket and steadies you with the force of a person who measures storms in data and weighs human life like numbers in a ledger. Her voice is not apologetic."
    hide tomas_tommy_reyes
    show dr_amina_bhatt at right:
        zoom 0.7

    dr_amina_bhatt "If you send Tommy, we can't get him back before the second crest without risking the pier team. We need to decide: who we absolutely can't lose and who we manage for acceptable risk."
    "You taste bile. You think of your sibling again, not as sorrow you can wear like a cloak, but as an instruction burned into you: don't let the tide decide. Act. Save who you can."
    "Elias Navarro meets your eye, and for a second he looks like he might relent completely — like he might slide his professional chain and stand beside you in the mud. Then his shoulders hitch."

    elias_navarro "I can fight them for authorization, but it could delay everything by five minutes. Five minutes in a surge's timeline is an eternity."
    "Your voice comes out small and sharp."

    mara_lin "Then say their names. Tell them the kids' names. Tell them the teacher's name."
    "He starts to — begins to form words that will make the abstract become personal — and then a dispatch chimes into his ear. He winces. There is a new message: the hospital's backup generator is compromised at the north wing."

    elias_navarro "If they lose power, we have critical care patients on portable respirators. We can't—"

    mara_lin "If we lose the kids to the sea, what then? Do we write a report that says 'we had priorities'?"
    "The rain intensifies, each drop a tiny accusation. The walls of the Commons thrum. You are out of safe rhetorical ground. Decisions must be made and you will be the one whose voice becomes a dam or a doorway."

    menu:
        "Authorize Tommy’s skiff despite the risk":
            "You set your jaw and nod. Tommy slams the throttle and the skiff spits water as it launches, Rae hanging off the bow with a rope, voices slicing the dark."
        "Pull Celeste's boats to the Commons to run a faster, safer shuttle":
            "You point toward the contractor line; Celeste's team forms a practiced chain, hydraulic winches humming as they lower a stable ferry into the churning water. Volunteers breathe a little easier, but you feel the string that ties help to politics tug at you."

    # --- merge ---
    "Continue"
    # [Scene: Promenade (Half-Finished) | Night — The Surge Nears]
    hide mara_lin
    hide elias_navarro
    hide dr_amina_bhatt

    scene bg ch14_dff609_4 at full_bg
    # play music "music_placeholder"  # [Music: Brass and percussion clash; tempo accelerates to frantic]
    # play sound "sfx_placeholder"  # [Sound: Metal groaning, a distant siren collapsing into a coughing static]
    "You arrive at the promenade and the sky feels lower here, closer to you as if the world has leaned in to listen. Construction lights cast everything in harsh, clinical hues. The half-built wall — a man-made promise — is already tasting the sea and finding itself wanting."
    "Workers, contractors, and a few residents cling to ropes and piles of salvaged timber. Someone screams; you can't tell who at first. Then you see a hand, white-knuckled, grasping a steel beam half-submerged. A support cable snaps with a sound like a bone breaking."
    "Celeste Park is there, moving with crisp purpose, issuing orders that cut like a saw but produce results. She looks at you when she notices you, and her expression is exactly on the line between sympathy and calculation — unreadable, as ever."
    show celeste_park at left:
        zoom 0.7

    celeste_park "We need to clear the lower deck. My teams can set anchor lines and pull people up to the temporary gantry. But we need authorization for the electrical cut-off and to divert personnel."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Do it. Now."

    celeste_park "Good. I'll coordinate with command.' (she meets your eyes) 'Mara, you understand this could mean demolishing what remains of the promenade's west side to save lives."
    "There's a room in your chest that freezes at that phrasing: demolish. Destroy to save. It is clean and terrible, and the math is cold. You nod, because you have always believed that you can weigh harm against harm and make the lighter choice. But it doesn't feel lighter tonight."
    "Elias Navarro arrives at your shoulder, soaked through, drawing breath like someone who has been underwater and is trying not to inhale the rest of it."
    show elias_navarro at center:
        zoom 0.7

    elias_navarro "Command is calling. They say reassigning their crews will breach our insurance bounds and they'll recall all outside contractors."

    mara_lin "Then we'll use volunteers and whatever boats we have. We do it ourselves."

    elias_navarro "I—' (his voice breaks) 'I can muddy the paperwork. I can take the hit on the report, but I can't make that call alone."
    "You look at him. The rain throws his hair into his eyes; there's a thinness to him, a human fray. This is not the safe, neat engineer you first met in the lab; this is someone being pulled apart by institutional cords and human throes."
    "Dr. Amina cuts in, voice hard as flint."
    hide celeste_park
    show dr_amina_bhatt at left:
        zoom 0.7

    dr_amina_bhatt "Surge is three to five minutes away. If you commit crews here and something else fails, we will have a triage failure elsewhere. Decide now. Do we hold the promenade at risk to save those on-site, or do we secure the hospital and the Commons?"
    "Your throat tightens. You remember a sound — your sibling's voice, lost to a night like this. Everything narrows to that memory and the shape of a hand you couldn't hold."
    "Tommy plants his feet in the mud and says, plain and terrible:"
    hide mara_lin
    show tomas_tommy_reyes at right:
        zoom 0.7

    tomas_tommy_reyes "If we don't get those folks up now, there's no later."
    "The sirens grow louder. A wave of rain slams the promenade like a physical thing. Someone cries out. You can see the water's edge licking the lower scaffolding. The town is a living thing caught between two jaws."
    "Elias Navarro presses his palm to your shoulder; it is a soft, almost private plea."

    elias_navarro "Tell me which to save."
    "You inhale. The world is a sheet of sound and the air tastes like metal and fear. Choices condense into a single, searing point. You know what the options will be. You feel them in the bones of the boardwalk and the crying of the radios."
    "Everything is on a knife-edge now. The crest is minutes away. Your chest feels impossibly small and impossibly huge at once."
    "You reach for your radio. Your hand shakes."
    hide elias_navarro
    hide dr_amina_bhatt
    hide tomas_tommy_reyes

    scene bg ch14_dff609_5 at full_bg
    # play music "music_placeholder"  # [Music: Single, relentless drumbeat — heartbeat synchronised with the surge countdown]
    # play sound "sfx_placeholder"  # [Sound: The wind lifts a scrap of paper, which spins and is swallowed by the dark]
    "You are the hinge."
    "You are the one who will decide."
    "You think of the town's future, of the gardens, of the hospital vents humming with borrowed air, of the kids in the greenhouse, of every compromise you have ever made and every promise you have kept."
    "You don't have the luxury of a clean answer."
    "You only have the decision."
    # [Scene: Emergency Coordination Center | Night — Pressure Peaking]

    scene bg ch14_dff609_6 at full_bg
    # play music "music_placeholder"  # [Music: Noisier now — strings tearing into dissonance, brass blaring]
    # play sound "sfx_placeholder"  # [Sound: A distant roar as the first crest hits the outer breakwater]
    show dr_amina_bhatt at left:
        zoom 0.7

    dr_amina_bhatt "We need to commit now. Call it. We can't keep spreading what little we have and expect miracles. Pick the highest probability of survival."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Names and locations — give me the list again, precise."

    dr_amina_bhatt "Promenade lower deck: twelve, mixed adults and contractors, some with injuries. Hospital north wing: eight critical care patients on temporary support. Commons greenhouse: five — two children, a teacher, two volunteers."
    show elias_navarro at center:
        zoom 0.7

    elias_navarro "If we prioritize hospital, we secure life-sustaining equipment. If we prioritize promenade, we save more immediately exposed people. If we prioritize Commons, we save the children and local organizers who will hold the recovery."
    "Celeste Park stands to the side, arms folded, watching, her face the calm of someone tracking a complex equation."
    hide dr_amina_bhatt
    show celeste_park at left:
        zoom 0.7

    celeste_park "Whatever you choose will be criticized. It is inevitable. Choose what keeps the greatest number alive. The optics—"
    "Her mouth says 'optics' like a scalpel. You feel the town's eye on you already — the murmurs, the future headlines, the small and large griefs that will gather around every outcome."
    "You close your eyes for a breath. You can feel the wind climbing through the rafters, find the salt in the air, and you can hear the tide taking its claim. Your hands are steady for only a second before they go to the radio."
    "You could take the path the models favor. You could favor the path the heart demands. Each line is a cut through the same body of town."
    "Your finger hovers."
    # play music "music_placeholder"  # [Music: Crescendo; everything strung taut]
    # play sound "sfx_placeholder"  # [Sound: A loud, singular crack as a support gives somewhere down the coast; someone screams; a child laughs somewhere else, horribly out of place]
    "You think of the sibling again. You imagine the hand you couldn't hold reaching for you now and shaking and saying, 'Do what you can.'"
    "The radio's green light blinks. The world narrows to the red marker on the map and the names attached to it."
    "You press the transmit."
    "You say the first words."
    "You do not yet hear the answer."
    "You have begun."
    # [Page-Turn Moment]
    "You stand between two kinds of duty — the measured, procedural duty that keeps systems whole, and the raw, immediate duty to the bodies in front of you. Rain strips away polite arguments until you're left"
    "only with breath, bone, and pulse. The next voice you hear will either steady a hand or break it. You feel, in that long half-second before the reply, the full weight of everything that will follow."
    hide mara_lin
    hide elias_navarro
    hide celeste_park

    scene bg ch14_dff609_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter24
    return
