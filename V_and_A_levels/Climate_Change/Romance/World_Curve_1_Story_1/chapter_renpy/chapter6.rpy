label chapter6:

    # [Scene: Boardwalk & Rally Site | Dawn]

    scene bg ch6_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Brass and strings swell into a bright, urgent fanfare]
    # play sound "sfx_placeholder"  # [Sound: Camera shutters, voices rising into a single rising hum; gulls circling, distant engine hum]
    "You remember the tide that morning like a breath held and released — the world between two beats. Salt on the air, the mud cold through your boots, and the steady pressure of a hundred hands"
    "linked beside you. The blockade holds. It is more than wood and bodies; it is all the small, stubborn things that have kept the neighborhood alive."
    "Lito stands two people down, grin smeared with mud, eyes bright. He waves a knuckled fist at you and then ducks into the chain, shoulder set like an anchor."
    show lito_reyes at left:
        zoom 0.7

    lito_reyes "You always pick the dramatic mornings, huh?"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Only the ones that make history,"
    "He laughs, quick and fierce. When he speaks again it's quieter, almost a confession."

    lito_reyes "Ma, she'd be proud. You know that, right?"

    maya_reyes "She would be. And she'd tell us to stop shivering and get to work."
    "Amaya appears at the line's edge with a stack of hand-scrawled signs and wet hair clinging to her scarf. Her eyes are bright with something like rain and something like thunder."
    show amaya_chen at center:
        zoom 0.7

    amaya_chen "National's here. Cameras at the north gate. Mayor's convoy's stalled outside town. Rowan's on a livestream with the university feeds."

    maya_reyes "Good. Make them listen to the mud, not the charts on corporate slides."
    "Amaya's fingers find yours for a beat — a steadying touch — and then she's off, directing neighbors into tighter formation. The crowd breathes as one. You feel the rush of it: very high and very alive."
    hide lito_reyes
    hide maya_reyes
    hide amaya_chen

    scene bg ch6_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Microphone hiss; the reporter's voice thin over the roar of the crowd]

    "Reporter" "Maya Reyes, can you tell us why you're standing here today?"
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "Because our shore is not a blank ledger for someone else's profit. Because marshes are living infrastructure, and because we know how to build resilience that keeps people and nature together."

    "Reporter" "You expect the mayor to take your side?"

    maya_reyes "We expect her to take the facts seriously.' (You glance at the row of phones livestreaming everything.) 'And we hope she'll remember who her voters are."
    # play music "music_placeholder"  # [Music: Percussion tightens; a collective inhale moves through the crowd — arousal rising]
    # play sound "sfx_placeholder"  # [Sound: A ripple of strained applause; the distant thrum of many feet, like surf]
    "The morning presses forward with crystalline intensity. Cameras document. Phones archive. Voices ripple into the world. Then, through the commotion, a hush falls when a message spreads along the line: Rowan is at the town hall with the mayor and a copy of the community's data."
    "Rowan emerges on a low step, sodden field coat haloed with plastered marsh grass. His hand holds a battered tablet — graphs, tide projections, annotated sediment maps. He looks worn but intact, and when he speaks his voice cuts the noise with plainness."
    show professor_rowan_hale at right:
        zoom 0.7

    professor_rowan_hale "Mayor Álvarez has the model now. It's not just ours; the university corroborated the sediment accretion rates. The Duval permit can't proceed without an environmental hearing."

    maya_reyes "Can she pause it? Right now?"

    professor_rowan_hale "She can. The data's the hinge. We need you here until she makes that call."

    maya_reyes "Then we stand."

    menu:
        "Step forward and speak to the national reporter":
            "You step into the camera's frame and give a focused, fierce minute on living shores and local knowledge — your words thread the science to the faces around you."
        "Stay in the chain and keep watch":
            "You squeeze the hand of the neighbor beside you, feeling each pulse like a signal. You let others take the camera; your role is the line that won't break."

    # --- merge ---
    "The live feed cuts to Town Hall interior; the scene continues via the projected screens."
    hide maya_reyes
    hide professor_rowan_hale

    scene bg ch6_601bcb_3 at full_bg
    # play music "music_placeholder"  # [Music: A tense, rising chord resolves as the mayor stands to address the press; the crowd outside watches on projected screens]
    # play sound "sfx_placeholder"  # [Sound: The mayor's shoes on linoleum; murmurs; a chair scraped back]
    "Inside, Mayor Sofía Álvarez wears compromise like a coat — heavy, necessary. She studies the room: a row of delegation faces, Camille Duval in a cool suit at the end of a polished table, and Rowan with his field coat. The feed aligns a thousand tiny watchful faces to hers."
    show mayor_sofa_lvarez at left:
        zoom 0.7

    mayor_sofa_lvarez "This city is tired of being bullied by promises that come without land, without livelihoods. I will not make that choice lightly."
    "Camille Duval's expression falters for a fraction — a ledger's tick in a human face — then composes into a mask of corporate certainty."
    show camille_duval at right:
        zoom 0.7

    camille_duval "Our project ensures long-term protection. A pause undermines investor confidence and delays safety upgrades."

    mayor_sofa_lvarez "We will not trade one form of risk for another without clarity. I am placing Duval's permit on hold pending a phased review. We will fund a pilot for living-shore solutions — community-led, scientifically monitored."
    # play sound "sfx_placeholder"  # [Sound: A collective sound — like the catching of a thousand breaths — rises from the feed watching the hall]
    # play music "music_placeholder"  # [Music: Crescendo into triumphant brass]
    "You feel the announcement in your bones. The blockade's solidity becomes official weight. The crowd outside whoops; someone whistles; Amaya's sobs catch in a delighted, incredulous laugh. Lito kisses his dirt-caked hand and presses it to his chest."
    show amaya_chen at center:
        zoom 0.7

    amaya_chen "You did this. We did this."
    hide mayor_sofa_lvarez
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "We — together. Rowan's work, your organizing, Lito's stubborn grin. All of it."
    hide camille_duval
    show professor_rowan_hale at right:
        zoom 0.7

    professor_rowan_hale "The mayor's endorsement opens a pathway for funding eligibility. We can run the pilot with local crews, build the modular buffers Elias Stone sketched out, and monitor accretion. This is the start."
    hide amaya_chen
    hide maya_reyes
    hide professor_rowan_hale

    scene bg ch6_601bcb_4 at full_bg
    # play music "music_placeholder"  # [Music: A softer, high-strings motif threads under the brass — intimacy threaded through victory]
    show elias_stone at left:
        zoom 0.7

    elias_stone "They took the sketches seriously. They liked the modular approach — small, replicable units that don't flatten the marsh. They want a pilot team — local crews, training programs. It's funded, for now."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "You told them we could do it without bulldozers?"

    elias_stone "I told them people who live here deserve a shot at building what they'll inherit. I messed up my ink run, by the way.' (He taps his satchel; a smear of blue runs into the edge of a plan.) 'Looks like stormwater and improvisation have better aesthetics than corporate renderings."
    "You laugh, the sound high and cracking. He reaches out on instinct, thumb brushing the patch of silver at your temple — familiar, tender, loaded with shared nights and plans. The contact is a bridge."

    elias_stone "Maya, we did it. You did it."

    maya_reyes "We did it."
    "Camille Duval's retreat is quieter than the earlier noise. In the hall her voice is clipped and formal."
    show camille_duval at center:
        zoom 0.7

    camille_duval "This is a political decision. Duval will pursue legal avenues and we will continue to propose our model."
    hide elias_stone
    show mayor_sofa_lvarez at left:
        zoom 0.7

    mayor_sofa_lvarez "And we will ensure ecological reviews and public oversight. This city will not be reshaped behind closed doors."
    "Camille Duval's posture remains composed; her eyes toward you are complex — not quite regret, not quite indifference — a ledger of cost and conviction. She gathers her papers and steps out, her PR entourage a smaller, more brittle breeze than her entrance had suggested."

    menu:
        "Call out to Camille as she leaves":
            "You call her by name. For a half-derisive second she turns; your question isn't an accusation so much as a listing of lives that matter. She doesn't answer, but her jaw loosens as if the question lodged."
        "Let her go and return to the people":
            "You turn back to the chain and fold yourself into the crowd. Her retreat becomes background noise; the present work needs attention, not spectacle."

    # --- merge ---
    "The day moves into hands-on work at the marsh; scene transitions to the pilot implementation."
    # [Scene: Marsh | Late Afternoon — The Pilot Plan Moves into Practice]
    hide maya_reyes
    hide camille_duval
    hide mayor_sofa_lvarez

    scene bg ch6_601bcb_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slap of boots in mud, measured saws, the clink of metal; gulls call like punctuation]
    # play music "music_placeholder"  # [Music: Percussive momentum with uplifting cello lines]
    "Training begins in earnest. Hands that once hauled nets now learn the rhythm of living-shore placement. Rowan shows field students how to take sediment cores. Amaya coordinates volunteer rosters, her voice a steady metronome among the clatter."
    "You kneel in the mud to plant the first ceremonial reed. The crowd gathers in a wide, ragged circle. Someone passes you a small bag of sea glass, collected over years — a handful of green and cobalt beads smoothed by tides and time."
    show lito_reyes at left:
        zoom 0.7

    lito_reyes "Here."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "This goes in first. For everyone who stayed."
    "You press the reed into the soft soil and pour the glass around its roots, the small sound like rain against tin. The gesture is both private and public: an offering, a promise, a stitch."

    menu:
        "Speak words for those who can't be here":
            "You say the names aloud — neighbors displaced, storms lost — and the crowd answers with a chorus of fragments: a child's name, a buried boat, a birthday missed. The reed stands as a ledger of memory and intent."
        "Keep your vow quietly":
            "You press the glass and reed into the soil without words, letting the motion say what you cannot. A neighbor squeezes your shoulder; the silence between you is full."

    # --- merge ---
    "The pilot takes root; training, placement, and community coordination continue into evening."
    # play music "music_placeholder"  # [Music: Swells into a warm, triumphant chord; laughter and singing braid with the sound of tools]
    "The pilot takes root in effectiveness and in education: modular units placed, seedlings fastened, local crews trained, and a stipend program announced to hire community members. National coverage pivots from spectacle to models — from the"
    "company's glossy renderings to videos of neighbors with drenched sleeves and dirt under their nails explaining accretion curves and planting schedules."
    "You move through the site, shaking hands, trading quick, breathless strategizing. Every conversation is a thread in a greater weave — funding mechanics, monitoring protocols, apprenticeship schedules. The arousal remains high — adrenaline braided with resolute joy."
    # [Scene: Boardwalk | Evening — The Quiet After the Storm of the Day]
    hide lito_reyes
    hide maya_reyes

    scene bg ch6_601bcb_6 at full_bg
    # play music "music_placeholder"  # [Music: A low, satisfied piano; soft strings carrying embers of earlier brass]
    # play sound "sfx_placeholder"  # [Sound: Murmured toasts, the far-off slap of waves, the creak of the boardwalk settling]
    "When the last public statements settle and the cameras leave for other flashes, you find a spare moment of stillness on the wet boardwalk. Elias Stone is already there, hands wrapped around two dented thermoses; steam fogs between you."
    show elias_stone at left:
        zoom 0.7

    elias_stone "Hot. Bit bitter. Yours if you want it."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Yours if you want the silence that follows all this noise."

    elias_stone "I'll take both."
    "You sit side by side, no need for grand words. His fingers find yours — callused, reliable, rough against the soft skin at your palm. The contact is small and enormous at once."

    elias_stone "You carried so much of this. You still do."

    maya_reyes "I don't anymore. Not the same way. It doesn't all live on my shoulders tonight."
    "He turns his hand, palm up, and you slide yours into it. The warmth spreads into the ache you've kept close for months. Guilt that used to sit like a stone in your chest loosens into something usable — a responsibility shared rather than a burden hoarded."

    elias_stone "Promise me we'll keep teaching. We'll scale the pilot. We'll make this work a thousand small things that add up."

    maya_reyes "I promise. And—' (you tighten your grip) '—we'll keep being honest about loss. We don't get to pretend the marsh is invincible. We just learn to protect it with people who belong here."
    hide elias_stone
    hide maya_reyes

    scene bg ch6_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: Fades into a single held note that dissolves into contented breath]
    "Around you, neighbors sing a ragged sea shanty. Lito is dancing with a kid on his shoulders. Amaya gives a small speech about the next training cohort with more fire than restraint. Rowan is already sketching"
    "the monitoring schedule on a napkin, precise and delighted. Mayor Sofía passes by, her eyes creased with fatigue and something like relief; she nods at you, and that nod is an acknowledgment of shared labor and"
    "consequence."
    "You look across the marsh where the reed you planted stands thin and stubborn against the ebb. For all the vulnerability that remains — for all the storms that will come — today belongs to a"
    "different ledger. The victory is not a wall; it is a scaffold: people learning, funding tied to oversight, training that roots local knowledge into practice. It is honest and imperfect and likely to be the beginning"
    "of long, hard work."
    show elias_stone at left:
        zoom 0.7

    elias_stone "Whatever comes, we'll keep the work human."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "And we'll keep each other accountable. That's the part that matters."
    "You let the night settle around you, a living thing that holds warmth instead of cold. You feel less alone. Love and work braid into a promise you can carry forward."
    hide elias_stone
    hide maya_reyes

    scene bg ch6_601bcb_8 at full_bg
    # play music "music_placeholder"  # [Music: Resolute finale — bright, warm, a final chord that lingers]
    "You stand, pushing off the boardwalk. Around you are faces worn and jubilant, exhausted and emboldened. The marsh is still vulnerable; storms will come. But the victory today is rooted in the faces around you and in the long list of small, steady acts that built it."
    "You breathe in the salt air and let the future feel less like an accusation and more like a task shared."

    scene bg ch6_601bcb_9 at full_bg
    "THE END"
    # [GAME END]
    return
