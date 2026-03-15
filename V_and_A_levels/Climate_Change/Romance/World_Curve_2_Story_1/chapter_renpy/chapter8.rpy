label chapter8:

    # [Scene: Municipal Plaza | Late Afternoon]

    scene bg ch7_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Urgent strings undercut by a low, insistent percussion]
    # play sound "sfx_placeholder"  # [Sound: The murmur of voices, camera shutters, distant gulls; an ambulance siren a block away, swallowed by wind]
    "You step up to the temporary podium because someone pushed the mic toward you and because if you don't speak, everything will feel like a surrender you can't forgive yourself for. Your throat tastes of salt"
    "and paper—petition pages, last-minute notes. The crowd looks to you with the brittle hope of people who've been holding their breath for too long."
    show mira_santos at left:
        zoom 0.7

    mira_santos "We were not born to be moved like furniture,' you say, and your voice comes out steadier than you feel. 'We were born here. We remember. We will not let a promise dressed in concrete take that away."
    "There is a thin cheer. Someone clangs a pot in the back. A woman near the front wipes her eyes with the back of her hand. Cameras zoom closer; a reporter's voice asks a question you don't hear fully."
    show noah_rivera at right:
        zoom 0.7

    noah_rivera "You said you'd go public, Mira Santos. Good. We need names for the injunction—who's willing? Jun's already calling allies."
    "You glance to where Jun stands, phone clutched, raincoat hood down though the sky is only the threat of rain. The municipal plaza feels smaller now—walls of people, bodies pressed against the cold wooden boards of"
    "the boardwalk that leads into the square. The wind slices through, carrying the distant, professional warmth of Cassandra 'Cass' Whitlock's PR voice—soft assurances layered over footage of smiling families and architect's renderings."
    show jun_park at center:
        zoom 0.7

    jun_park "I've got a list from the youth group. We've got people willing to be plaintiffs, but—and this is big—some volunteers are asking if we'll be able to protect them if a judge rules against us. They want guarantees."
    "You can hear how the word 'guarantees' fractures the air. The legal system doesn't hand out guarantees the way you hand out flyers. It hands out statutes, injunctions, delays. You can feel the town leaning toward"
    "whatever feels like shelter, even if that shelter is Cassandra 'Cass' Whitlock's polished, unblinking promise."

    menu:
        "Give the crowd a rallying, emotional promise":
            "You curl your fingers around the mic and speak in a cadence meant for memory: 'I cannot promise you zero change. I can promise we will fight so every story, every name, every home is counted.' The plaza breathes in; a string of applause ripples out."
        "Lay out the legal steps plainly":
            "You drop the rhetoric and read from your notes—injunction timelines, counsel names, how evidence will be filed. The reaction is quieter but steadier; faces shift from pleading to planning. Jun nods, approval plain on their face."

    # --- merge ---
    "Noah pulls you aside as the applause fades. He smells like oil and sea salt; his hoodie is speckled with paint, dried into crusted colors."
    "Noah pulls you aside as the applause fades. He smells like oil and sea salt; his hoodie is speckled with paint, dried into crusted colors."

    noah_rivera "We can file tonight. I've got the marshal's contact. People will camp at the council if we do—pressure's half the battle. But Mira Santos—this will drain us. It will take everything."
    "You want to tell him you know. You want to say you have a list—attorneys, timelines, witness statements—but the Schrödinger rule in the back of your head hums: you can't assume everyone who stood with you earlier still will. You pivot to the safer truth."

    mira_santos "Then we take everything. We file. We ask for interim relief. We make them show us in court why they think they can decide our futures without us."

    jun_park "Good. I'll call the attorneys. Elias Park—' (they sweep their arm to where Elias Park stands near the Saltworks display set up for demos) '—Elias can help with the technical affidavits. He knows the microgrid data."
    "Elias Park meets your eye across the crowd. His expression is a tight, unreadable knot—he steps forward, jacket zipped against the wind, camera strap across his chest. For a second the world narrows to the space"
    "between you: a charged, private current of accountability and something warmer and more dangerous. He says nothing at first; his silence counts like a small, solemn agreement."
    hide mira_santos
    show elias_park at left:
        zoom 0.7

    elias_park "I'll do it. But if this goes sideways—Mira Santos, I don't want you to carry all of it alone."
    "You want to argue that you've carried it already, and that you're tired of saying 'we' when you mean 'I'. Instead you let your fingers brush against the coral scarf at your throat and answer the thing you can actually promise."
    hide noah_rivera
    show mira_santos at right:
        zoom 0.7

    mira_santos "I won't carry it alone."
    hide jun_park
    hide elias_park
    hide mira_santos

    scene bg ch7_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A smartphone buzzes—an alert: 'Cass Infrastructure: Press Release — Community Consultation Announced.']

    "The PR volley is precise. Cassandra "Cass" Whitlock's team tweets a carefully edited clip of her pressing a child's hand into her palm beside a model of a seawall. The clip's caption" "Pragmatic. Humane. Ready."
    "A sharp thread of panic snakes through the crowd. Volunteers cluster, whispering about rent checks and babysitters and whether they can afford the time. You sense energy bleeding away, siphoned by promises that sound like stability but smell faintly of profit margins."
    # [Scene: Saltworks (Reclaimed Marsh Labs) | Early Evening]

    scene bg ch7_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: Percussive heartbeat, electronic undercurrent]
    # play sound "sfx_placeholder"  # [Sound: Soldering hiss; distant municipal bells; the occasional squawk of a gull]
    "You and Elias Park slip into the Saltworks like two bodies returning to a shared ritual—screens light your faces, algae-scented hoses clink. The lab smells of wet reeds and solder. The world outside feels louder: telephones, headlines, the thud of someone hammering a temporary sign."
    "Elias Park sets down a stack of hard drives, breath clouding in the cool air of the late-evening marsh. His fingers move with mechanical diplomacy—gentle, precise, trying to make sense of chaos with tools."
    show elias_park at left:
        zoom 0.7

    elias_park "We need affidavits. Sensor logs, timestamps, eyewitness statements—everything that ties Cassandra 'Cass' Whitlock's projections to the present risk. Jun's assembling testimony, but we'll need the engineering reports framed in plain language the judge can actually digest."
    "You sit at the bench and pull up the Moleskine's rough lists—things to subpoena, names of witnesses, the timeline of storms. The Saltworks' lights throw watercolor reflections into the shallow pools. The work is methodical: evidence as slow, painstaking weathering."
    show mira_santos at right:
        zoom 0.7

    mira_santos "Draft the affidavits. I'll get the names confirmed. Noah will coordinate plaintiffs. Jun will handle press releases that scream less and point to more—documentation. We file before midnight."
    "Elias Park watches you write the schedule like he's reading a map of someone who has decided to run headfirst into a gale."

    elias_park "And us? How do we—' He stops, searches for words that won't put a target on you or on him. 'How do we keep from burning out before we get to court?"
    "You look at him. His question isn't only practical; it is a tenderness wrapped in calculus. There's a history in the way he hesitates—an old lesson learned from a failed project, from promises made and then overturned. You could say 'rest', but rest is a contraband luxury right now."

    mira_santos "We don't. Not in the sense you're asking. We ration. We rotate. We make sure people come back to their families with their names still theirs."
    "He laughs—a short, staccato sound that's made of anxiety and defiance."

    elias_park "That sounds terrible. And effective."
    "You both work against the clock. The injunction filing requires signatures, scanned exhibits, legal forms that feel designed to trip exhausted hands. Noah arrives with coffee and three volunteers who look like they've already lost a"
    "day and their appetite. Aunt Lila appears too, wrapped in an old cardigan that smells of lavender and sea spray."
    show aunt_lila_santos at center:
        zoom 0.7

    aunt_lila_santos "You think the law will listen to stories? You think judges will hear salt in our voices?"
    "You rest your palm flat on the table, as if to feel the pulse of the room."

    mira_santos "The law listens to evidence and pressure. We give it both. We make their promises look like what they are—numbers with no faces."
    "Aunt Lila's face folds into something both proud and pained."

    aunt_lila_santos "Make sure you speak for the memories, not just the maps. If you lose what makes us, you'll still win a kind of victory that leaves the rest empty."
    "Her words land like stones. Fear spikes again—fear of winning the wrong thing. The psychology of legal wins creeps in: injunctions can delay, but the financial and psychological pressure Cassandra 'Cass' Whitlock can apply is immense."
    "Volunteers may be bankrupted by time or intimidated by legal counters. Cassandra 'Cass' Whitlock's firm has resources. You don't."

    menu:
        "Stay at the Saltworks to oversee filings all night":
            "You set up on the bench, the glow of the laptop a small island. Your hands move through affidavits; the night bleeds into typographical margins and court deadlines. Elias brings you a thermos without asking. For a moment, you are only precise motion."
        "Send Elias home to rest and keep the technical work going":
            "You tell Elias to go and sleep. He blinks, wounded and relieved all at once. He argues, but then folds, promising to be back at first light with fresh eyes. He leaves you with a lingering look that means more than 'be careful'."

    # --- merge ---
    "By midnight, the filings are queued—emails sent to clerks, exhibits uploaded, sworn statements timestamped."
    "By midnight, the filings are queued—emails sent to clerks, exhibits uploaded, sworn statements timestamped. The adrenaline carried you this far, a raw, metallic wire in your chest. You feel triumphant and immediately empty. The victory is procedural, small, and it tastes of rust."
    "Then the counterattack begins."
    # [Scene: Municipal Plaza / Boardwalk Edge | Midnight -> Early Morning]
    hide elias_park
    hide mira_santos
    hide aunt_lila_santos

    scene bg ch7_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Low brass, building dissonance]
    # play sound "sfx_placeholder"  # [Sound: A legal firm's voicemail, repeated; footsteps leaving; the distant roar of the ocean]
    "You awake on a borrowed cot in the Saltworks to Jun shaking your shoulder. The morning has the color of exhaustion—washed-out blues and the raw white of screens."
    show jun_park at left:
        zoom 0.7

    jun_park "A lot of volunteers took down their tents overnight. Some got letters—'comply or risk eviction' with municipal letterhead. The council's been flooded with 'concerned citizen' emails. Cassandra 'Cass' Whitlock's lawyers file a motion to quash the injunction on procedural grounds. They're saying our plaintiffs lack standing."
    "Your stomach drops in a way that feels physiological, like someone pushed a weight into your lower ribs. The legal motions are technical knives—small, precise, slowly cutting the crowd's resolve."
    show mira_santos at right:
        zoom 0.7

    mira_santos "That's okay. We expected pushback. We'll respond."
    "You sound small when you say it. It is a brittle kind of hope that the law will behave as you'd rehearsed. You read the motion anyway: threaded with legalese and a clinical undermining of community"
    "testimony. They cast citizens as nebulous, plaintiffs as misaligned. Their language tries to make people into abstractions."
    show noah_rivera at center:
        zoom 0.7

    noah_rivera "They're not just fighting us in court. They're fighting the people who help us show up. Letters like that—people with rent to pay, repossessions in the background—they snap. Volunteers are scared. They're leaving."
    "You feel the ground tilt. Fear becomes not a theoretical thing but a series of small, cutting losses: a woman who used to run the community kitchen calls to say she can't afford to spend nights"
    "in the plaza; a teenage organizer reports that her parents forbade her from participating; the town's baker said she'll withdraw her support if the bakery is threatened with fines."
    "Elias Park stands beside you, shoulders drawn in. He pulls a small prototype from his jacket—the micro-turbine pendant heavier than it looks. He twists the copper cuff on his wrist like a talisman."
    hide jun_park
    show elias_park at left:
        zoom 0.7

    elias_park "They'll play long. They have to. It's their advantage. They'll hope we run out of money, of energy, of people willing to fight. If they can starve the movement, they win the moral calculus."
    "You think of Aunt Lila's warning about the hollow victory. You think of the families on the edge of town, of the map of flood lines you'd studied for years. The tide is more than a physical force now—it's political and legal and lit with glossy advertisements."
    "Your name circulates in local feeds; op-eds call you 'emotional' or 'intransigent'. Cassandra 'Cass' Whitlock's spokespeople frame her plan as 'inevitable responsibility'—a message crafted to make their opponents look like obstructionists in the face of progress."
    "The narrative war is crueler than any single courtroom; it's about convincing people that despair has a practical alternative."
    hide mira_santos
    hide noah_rivera
    hide elias_park

    scene bg ch7_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Crescendo—strings and timpani; the beat speeds]
    "You can see the list of strategies in your head—negotiate compromise, go scorched-earth with public pressure, or slow-draw municipal allies into quiet buys of time. Each is a moral fork with teeth. Each will cost something you don't yet quantify."
    "Aunt Lila finds you by the edge of the boardwalk, where the sound of the sea is loud enough to drown the press. The lighthouse silhouette is just a brooding shape against a bruised sky. She places a small hand on your forearm—warm, familiar, a map of generations."
    show aunt_lila_santos at left:
        zoom 0.7

    aunt_lila_santos "You have a fire in you, child. But fire without a direction burns houses as easily as it clears brush."
    "You want to tell her that direction is exactly what you're trying to find. Instead you let the decisions make themselves into pressure in your chest. The town needs a strategy, not only raw will. But daily attrition is already gnawing at the bones of your people."
    show elias_park at right:
        zoom 0.7

    elias_park "We need to decide how to press this. The legal team needs direction. Are we negotiating for protections that hand them legitimacy, or are we burning for principle and risking everything? Or do we keep a quiet line to the council to buy time?"
    "He does not say the words for you. He doesn't have to. The choice hangs like a tidal line across the night sky."
    "Your pulse is a drum in your ears. Fear has sharpened into a high, cold clarity. You can feel volunteers thinning, the legal strategy devouring hours, Cassandra 'Cass' Whitlock's PR machine turning public sympathy into a ledger entry. The wave is not one event—it's a steady, remorseless pressure."
    "You imagine what surrender looks like: sanitized renderings replacing wooden porches, the smell of tar and cement, the dead quiet where late-night laughter used to be. You imagine what victory looks like: long court battles, settlements that leave scars, neighborhoods saved at the cost of compromise."
    "You breathe in, tasting salt and the metallic tang of litigation."
    # play music "music_placeholder"  # [Music: The score tightens to a single, high-pitched string; the tempo rises—breath, heartbeat, footsteps—building toward a moment of irrevocable choice]

    menu:
        "Negotiate a formal compromise to secure legal protections for key neighborhoods while conceding some infrastructure.":
            jump chapter9
        "Double down on an all-out legal blockade and public pressure.":
            jump chapter11
        "Pursue a quiet settlement with municipal allies to slow the process and buy time.":
            jump chapter17
    return
