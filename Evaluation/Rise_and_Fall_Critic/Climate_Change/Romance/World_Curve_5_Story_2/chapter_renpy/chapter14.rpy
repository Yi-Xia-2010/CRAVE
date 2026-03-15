label chapter14:

    # [Scene: Old Pier Market | Twilight]

    scene bg ch14_9d8ae5_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low murmur of vendors folding goods, a single gull calling, distant mechanical thrum from a survey ship's engines.]
    # play music "music_placeholder"  # [Music: Sparse piano, minor key; low strings undercut the air with a persistent, worried pulse]
    "You stand with the coil of rope over your shoulder and the leather notebook warm against your ribs. The beam has turned the market into a tableau—faces caught in that pale strip of light—and you feel"
    "the room of the town compress into something urgent. People are moving in micro-decisions: a board pulled taut, a child coaxed home, a lamp secured against a wind that hasn't come yet."
    "You let the rope curl into a knot the way your hands know how, but your mind keeps knotting tighter: the neighboring district's emergency seawall approval, a promise of money and quick action, the investor shorthand"
    "of 'scale' and 'relocation.' Those words have a taste you know too well—metallic and too-sweet, as if they were meant to cover rust."
    "Marta approaches with a crate of last-minute flyers. Her knuckles are raw; the paint on her overalls is a map of other people's patchwork repairs. She lowers her voice so only you can hear."
    show marta_quin at left:
        zoom 0.7

    marta_quin "They're already on the radio. Lina just called me—said it's a 'precedent' and 'urgent.' People are saying it'll spare lives, Aria. But they're saying it like a bandage."
    "You notice Eli Navarro at the edge of the crowd, his silhouette against the pale glow of The Helix reflected on the water. He meets your eyes and there is a hardness there you haven't seen today—sharp, immediate, protective."
    show eli_navarro at right:
        zoom 0.7

    eli_navarro "They can't do this to the shore without us. Not without asking. Not like that."
    show aria_solen at center:
        zoom 0.7

    aria_solen "We don't know what they'll propose yet. But the council will hear them before we get word in full."

    eli_navarro "They don't have to wait. They can fund the machinery, pay contractors up front, move families. Quick is bloody persuasive."
    "Jun appears, tablet tucked under one arm, eyes already flicking through the incoming feeds. He sounds like someone reading a wound aloud."
    hide marta_quin
    show jun_park at left:
        zoom 0.7

    jun_park "Preliminary plans are circulating. Reinforced bulkheads—steel pilings. The engineering window they're citing matches a storm window two weeks from now."
    "You feel the familiar tightness coil beneath your breastbone—old grief, new urgency. The thought that comes unbidden: if you don't act, more rooms will be closed off to the tide and to memory."
    "Old Man Rafi: (from the far stall, voice cracked and low) 'When they name the shoreline with someone else's scales, we forget how to listen to the water.'"
    "His words hang between your shoulders, heavier than the rope. You look at the vendors—hands that have mended nets and patched roofs and salted fish now folded into pockets of silence. Someone in the back whispers 'relocation' like it is a verdict."

    menu:
        "Step up to the maker with the radio and listen in":
            "You push through the tarps and press your ear against the speaker; the announcer's voice is flat with official certainty, and for a terrifying second the plan sounds inevitable. You write a single line across your palm: 'Ask first.'"
        "Pull Marta aside to organize an emergency flyer run":
            "Marta's eyes shine wetly and she nods. You both crease the flyers into stacks and tuck them under arms like contraband—action you can do now."

    # --- merge ---
    "Continue with the following narration."
    hide eli_navarro
    hide aria_solen
    hide jun_park

    scene bg ch14_9d8ae5_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The creak of boards as the tide pushes; a vendor stomps a tarp; the distant, tidy bark of a municipal announcement van]
    "You can't shake the taste of Rafi's words. The market hums, everybody with something to lose, and the beam beyond the pier pulses like an accusation. Eli Navarro's jaw ticks."
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "We need people in the room. Faces. If they see the co-ops, if they see Rafi, if they see Jun's data—' (he gestures at the tablet in Jun's hands) '—they can't just sign on."
    show aria_solen at right:
        zoom 0.7

    aria_solen "They might. There's a strange kind of authority in 'emergency.' It compresses debate."
    show jun_park at center:
        zoom 0.7

    jun_park "It also compresses the data window. If you compress the data, you risk missing a tipping point in sediment flux. The seawall might protect one neighborhood and scuttle the next's marshes."
    "Eli Navarro's hand finds yours briefly—an anchor or a fuse, you can't tell. There is history in that contact: arguments, late-night repairs, the way he learned to let his fingers say what his mouth won't."

    aria_solen "Then we bring the data. We make this about the shore's functioning, not just the money."

    eli_navarro "And if the room's full of suits with lawyers?"
    "You feel the absence of an answer like a draft. The market's crowd is shifting—some preparing to return home, others waiting for news. The beam keeps cutting the horizon."
    # [Scene Transition Cue: A municipal van's headlights sweep across the boardwalk; a thud of municipal decision-making seems to come closer]
    # play music "music_placeholder"  # [Music: Low percussion; unresolved strings]
    # [Scene: Redevelopment Pavilion / Council Antechamber | Night — Immediately]
    hide eli_navarro
    hide aria_solen
    hide jun_park

    scene bg ch14_9d8ae5_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The click of a press conference being set up; muffled bursts of conversation; a projector hum]
    # play music "music_placeholder"  # [Music: Tense, low-register piano; the harmony narrows and cools]
    "Lina meets you at the doors, her raincoat buttoned tight, a phone cupped to her ear for the whole world to hear. Her expression is tight—earnest, exhausted."
    show lina_voss at left:
        zoom 0.7

    lina_voss "They're calling it an 'emergency expedited approval.' The developer's put up quick guarantees: temporary housing, contractor lines, a promise to move 'vulnerable populations' first."
    show aria_solen at right:
        zoom 0.7

    aria_solen "And who decides who's vulnerable? The people who've lived here their whole lives, or the people with the right paperwork and the right lobbyist?"

    lina_voss "They say they'll involve local partners. They say—' (she searches your face) '—Aria, if we resist and the seawall collapses a district, people will die. The risk is real."
    "You feel the word 'die' land like a stone. You remember your sibling's laugh swallowed by water and mud. Memory is a measurement you cannot unlearn: every plan must be weighed against the possibility of loss."
    "Caden Holt arrives then, an even line of authority: suit jacket damp but composed, his cuffwatch glinting. He has the kind of voice trained for rooms just like this—measured, persuasive, quick to close distance."
    show caden_holt at center:
        zoom 0.7

    caden_holt "Emergency action is not optional when models show cascading loss. We can fast-track approvals and mobilize resources. The plan they've proposed brings labor, materials, and immediate shoreline protection."

    aria_solen "Their engineering window is narrow because it's politically convenient. It cuts corners we can't afford ecologically."

    caden_holt "We can't afford indecision either. 'Ecology' becomes an argument for paralysis if it costs lives. I'm offering an alternative: accept scaled action now, avoid catastrophe, maintain as much cultural fabric as possible on higher ground."
    "Your pulse is an uneven metronome. The logic is an old riddle: protect lives now and accept later loss of place, or risk the shore to preserve something more fragile—identity, memory, daily practice."
    hide lina_voss
    show jun_park at left:
        zoom 0.7

    jun_park "The models correlate fast bulkhead deployment to displaced sediment plumes that will smother the marsh's nursery zones. We can mitigate, but mitigation is not prevention."
    "Old Man Rafi moves through the antechamber like a slow tide. He stops in front of the renderings and doesn't look at the steel lines and cross-sections so much as at the shadow they cast."
    hide aria_solen
    show old_man_rafi at right:
        zoom 0.7

    old_man_rafi "They call the land 'efficient' and forget it's alive with songs. You can't move a song and call it the same."
    "A murmur ripples through the council staff. Vendors you recognize appear in the doorway—faces drawn tight. One of them, a woman who sells smoked fish, presses her palms together like she might be holding on to something that wants to fall."

    "Fish Vendor" "Not everyone can go to higher ground. Not everyone has a second home. Where do we put memory?"

    caden_holt "We propose immediate relocation support for those who need it. We can't let attachment be an excuse to die on the shore."
    hide caden_holt
    show eli_navarro at center:
        zoom 0.7

    eli_navarro "Relocation is always a first step to erasure. You move families, then you sell the piers, then you replace our nets with private marinas."
    hide jun_park
    show caden_holt at left:
        zoom 0.7

    caden_holt "We can structure governance to keep co-op rights. But we must be realistic: the scale of funding here means compromises."
    hide old_man_rafi
    show aria_solen at right:
        zoom 0.7

    aria_solen "Realism has been used as a hammer before. It floors the very voices it's supposed to protect."
    hide eli_navarro
    show lina_voss at center:
        zoom 0.7

    lina_voss "There are no answers that don't hurt someone. That is the cruel part. The question is what hurts less."

    menu:
        "Ask Jun to run a rapid sediment-impact briefing for the incoming press":
            "Jun's face goes tight, then determined; he nods and leans over his tablet, fingers moving faster. You feel the small, correct power of data as a weapon of persuasion."
        "Step outside and gather the vendors to occupy the antechamber stairs":
            "You step out and pull people together like a magnet; their mutters become a chorus. You know the sight of a crowd can slow procedural wheels. The sound of many feet becomes a language the suits hear."

    # --- merge ---
    "Continue with the following narration."
    hide caden_holt
    hide aria_solen
    hide lina_voss

    scene bg ch14_9d8ae5_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The murmur of a newsroom beginning to align. Distant, the mechanical throb of the survey ship grows like an undercurrent.]
    "Caden Holt's tone shifts; he senses the council hanging, the public gaze sharpening."
    show caden_holt at left:
        zoom 0.7

    caden_holt "If we delay, we lose the funding window and the engineering teams. If we accept, we claim a seat at the table and ensure community representation in implementation. It's the only realistic path to get material protections in time."
    show eli_navarro at right:
        zoom 0.7

    eli_navarro "A seat at the table isn't enough when the table's being moved to a different continent of values."
    show aria_solen at center:
        zoom 0.7

    aria_solen "What are they offering exactly? How many homes? Who funds 'relocation support'?"
    hide caden_holt
    show lina_voss at left:
        zoom 0.7

    lina_voss "Temporary shelters, subsidized housing vouchers in the short term, grants for 'resilience upgrades' if you relocate to designated zones."
    hide eli_navarro
    show jun_park at right:
        zoom 0.7

    jun_park "Their environmental assessment is a cursory review. The sediment models are aggregated; they gloss over local feedback—"
    hide aria_solen
    show caden_holt at center:
        zoom 0.7

    caden_holt "Aggregating is how you make fast decisions. We can't litigate every calculation while water eats a child's bedroom."
    "Your internal monologue runs through the weight of your past: the room where your sibling was lost was full of decisions made without you. You have promised yourself that you will never, ever choose convenience over"
    "people. But this feels different; the choice could be the difference between immediate survival and long-term survival with its cultural costs."
    "Eli Navarro stands a breath away, the way he looks at you a pressure test. His hand hovers, then closes around the strap of his bag. He sounds like someone trying to catch himself, not knowing which instinct to trust."
    hide lina_voss
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "We can fight—and drag the story across the country, rally lawyers, make it a precedent. We can delay and hope to win. But the longer we shout, the more damage might be done now."
    hide jun_park
    show aria_solen at right:
        zoom 0.7

    aria_solen "Litigation could buy time for the living shoreline plan to scale. Negotiation could buy protections and force co-op governance. Acceptance might keep people from flooding tonight."
    hide caden_holt
    show marta_quin at center:
        zoom 0.7

    marta_quin "All those options are heavy with cost. I keep thinking of Rafi's song—you can move the people, but the pier's smell won't follow."
    "The survey ship's lights blink like an underwater constellation. The beam cuts through the antechamber window and leaves a white bruise across the carpet. Outside, the harbor water is a black mirror."
    "You can feel the room narrowing to a single hinge. Each argument lands like a pebble tossed into shallow water; the ripples converge and raise the same urgent question. The town's identity—its scents, its languages, the sound of a net being mended at dawn—hangs in the balance."
    "Caden Holt folds his hands."
    hide eli_navarro
    show caden_holt at left:
        zoom 0.7

    caden_holt "This is not about ideology. This is about triage."
    hide aria_solen
    show eli_navarro at right:
        zoom 0.7

    eli_navarro "This is exactly about ideology. Whose lives get triaged, Caden?"
    hide marta_quin
    show lina_voss at center:
        zoom 0.7

    lina_voss "We're out of time to pretend this is anything but a decision that will define us."
    "You taste salt and iron; your mouth is dry. Your fingers feel the texture of the notebook beneath the strap, the press of your thumb against the spiral where you've noted every small promise. You think"
    "of the child from the market, of Rafi's slow hands, of the way the Helix's lamps looked like stars you could hold."
    "You know any path will break something. Knowing doesn't make choosing easier."
    # play music "music_placeholder"  # [Music: A single, austere chord; the room seems to hold its breath]
    "You step toward the dais, where council staff are already arranging a procedural vote. Around you, voices lower into resigned, clustered murmurs—people assessing what they are willing to lose and what they will fight to keep."
    "The beam beyond the window cuts a bright, clinical line across the scene; in that light, a choice feels like being measured."
    # [Scene: Council Chambers | Immediate — Decision Moment]
    hide caden_holt
    hide eli_navarro
    hide lina_voss

    scene bg ch14_9d8ae5_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant press feed clicking on; the survey ship's engines as a low, relentless presence]
    "You open your mouth to speak and find your voice small inside the amphitheater. But you have been here before—standing where compromises were born and broken. You remember the person you swore not to be: someone"
    "who chose comfort over memory. You remember the lives that shorthand decisions have already taken."
    "This is the hour the town asks of you: do you hold the line, negotiate a partial salvation, or accept damage now to shield people from immediate harm? Each choice carries weight, each will shape what the archipelago becomes."

    jump chapter15
    return
