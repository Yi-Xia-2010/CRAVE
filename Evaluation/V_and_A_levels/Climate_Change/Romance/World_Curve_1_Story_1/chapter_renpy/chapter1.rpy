label chapter1:

    # [Scene: Boardwalk | Morning]

    scene bg ch1_Start_1 at full_bg
    # play music "music_placeholder"  # [Music: Sparse, low cello; a slow, measured tempo]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, water lapping softly against pilings]
    "You step off the bus with your thermos clutched like a talisman. The metal is cool through the canvas of your jacket. Your field notebook — corners dog-eared, spine softened by tide maps and hurried sketches"
    "— presses into your ribcage when you inhale. The air tastes of brine and wet wood, and the salt fog makes everything feel like it's been painted in halves."
    "Your chestnut bob is damp from the mist; the narrow silver streak at your temple catches what little light there is and looks too loud against the muted morning. The boardwalk groans underfoot, planks settling like"
    "an old memory waking. Each creak pulls a thread of something you thought you'd buried — the cousin you lost in a storm, the promise you made into a night that smelled of diesel and fear."

    scene bg ch1_Start_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Market chatter muffled by fog; frying oil hisses intermittently]
    "Lito is already there, sleeves rolled, hands moving as if he can fix the weather with them. He calls out your name with that familiar bluntness you both learned as kids — equal parts warmth and business."
    show lito_reyes at left:
        zoom 0.7

    lito_reyes "Look at you. Came back like a tide — late and full of secrets. How long you been holding on to that thermos?"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Long enough to know it keeps more than coffee hot. How are the nets holding up?"

    lito_reyes "We patched three this week. The harbor's been throwing up newer problems. Folks keep asking when 'they' will finish the barrier. When does finished mean safe?"
    "You stare at the half-finished flood barrier in the distance — clean concrete edges in a landscape that was never meant to be rectilinear. The sterile gray of poured concrete cuts the marsh like a surgical scar. Reeds press against it like prayer; the contrast aches."

    maya_reyes "When finished stops being about fences and starts being about living with water. When it includes the marsh.' (You fold your hands around the thermos.) 'That's what Professor Hale says."

    lito_reyes "Hale? The old man with the mud-laced coat? You trust that enough to make trouble?"
    "You both fall into a rhythm of the familiar — teasing that leans into the practical. Lito's smile gives way to the practical facts he can't tuck away with a joke."

    lito_reyes "Listen, sis. People are jittery. Camille's flyers are hitting the plaza today. Silver glass towers and 'secure tomorrow' — you know how that sounds to the landowners."

    maya_reyes "Cold and convincing.' (You hate how accurate the description is.) 'That's why I need to bring people together. Not just to fight a render. To show what keeps this place alive."

    menu:
        "Reach for Lito's forearm as you speak":
            "You close the distance, the familiar warmth of his callused skin grounding you. He nods, a small, unshakable agreement."
        "Keep your hands on the thermos, steady":
            "You hold the thermos like an anchor. Lito reads the posture and lets out a breath as if relieved you're here but not collapsing."

    # --- merge ---
    "..."
    # [Scene: Market | Morning]
    hide lito_reyes
    hide maya_reyes

    scene bg ch1_Start_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Conversation tumbling around you; the occasional bell of a boat engine]
    # [Smell: Frying oil, smoke, brine, and the sharper scent of heated metal from repairs]
    "Amaya threads a bright scarf through the crowd like a marker everyone can see. Her hair is shock-short and fiercely purple; she binds attention the way a lighthouse draws ships. When she spots you, she ducks through a cluster of neighbors, scarf flying."
    show amaya_chen at left:
        zoom 0.7

    amaya_chen "You're finally here. The calendar's full of holes if you don't show up.' (She stops close, voice low.) 'We had a dozen people ask for a plan yesterday. We can do leaflets, do a timeline, get the kids doing plantings — but we need someone who can read tides and make it mean something."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "I've got Hale's maps in my pack. I can pull the historical lines, show how the marsh used to breathe with the city.' (You feel the notebook like a small, heavy promise.) 'But I can't do names and faces and momentum without you."

    "Amaya (her eyes soften)" "Then don't. Bring the maps. Bring your scars and your stubbornness. I'll do the rest."
    "The three of you — you, Lito, Amaya — move as a small procession along the boardwalk. The half-built barrier looms, a promise of certainty. Reed ribbons and salt grasses press against its base as if"
    "trying to stitch it to the earth. You listen to the murmur of the market and the distant whine of a reclamation drone; the city's choices hum like a current underfoot."

    menu:
        "Reach out and run a fingertip along a reed":
            "Your finger feels the reed's papery resistance, damp and springy. A small, living thing that insists on being noticed. It steadies your breath."
        "Flatten your hand against the cold concrete barrier":
            "The concrete is colder than you'd expected, unforgiving. Your fingers splay and return with a trace of salt. The barrier feels final in a way that unsettles you."

    # --- merge ---
    "..."
    # [Scene: Tidal Fringe Marsh (passing view) | Late Morning]
    hide amaya_chen
    hide maya_reyes

    scene bg ch1_Start_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Insect chirr, distant birds; the marsh seems to exhale with each step]
    # [Touch: Salt in the air settles on your lips; your boots carry a faint squelch]
    "You drink in the marsh like someone trying to memorize a face. Everything about it is fragile and rooted at once: the way water collects at the base of the reeds, the spatter of sea glass"
    "under the surface, the smell of old wood. When you close your eyes for a second, that scent opens something tight inside you — a memory of the night you promised to keep this place. Guilt"
    "arrives soft and familiar, not new: the cousin you lost, the weight of a vow made in grief."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "I keep thinking 'if I had been there' — as if presence could alter weather or fate. But presence is what people can give each other. That's the work."
    show amaya_chen at right:
        zoom 0.7

    amaya_chen "We can't promise to stop every future storm,' she says, 'but we can make a place that withstands the ones that come. That matters to people who can't just pick up and go."

    maya_reyes "Then let's make it matter in a way no corporate render can replace."
    # [Scene: Community Shelter & Town Hall | Afternoon]
    hide maya_reyes
    hide amaya_chen

    scene bg ch1_Start_5 at full_bg
    # play music "music_placeholder"  # [Music: Low piano chords; a persistent, melancholic thread]
    # play sound "sfx_placeholder"  # [Sound: Chairs scrape, papers rustle; a hushed intensity fills the room]
    # [Smell: Coffee turns bitter in the air; the metallic tang of a city under strain]
    "You lay the tide maps across a long folding table. Professor Rowan Hale moves slowly around the edges of the room, spectacles fogged at the corners, white hair flecked with mud. His hands tremble slightly when"
    "he reaches for a map — not from age alone, but from the same thing that keeps you awake: care."
    show professor_rowan_hale at left:
        zoom 0.7

    professor_rowan_hale "These lines are not guesses. We have records. The marsh has been pushed back forty meters in three storm seasons. If we act with living systems in mind, we have a chance to slow the losses."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "We can rebuild the tidal corridor. Plant eelgrass, reconstruct sloughs, put in living shorelines that absorb energy rather than deflect it."

    professor_rowan_hale "Yes. But it will take long-term maintenance, legal access, and people who live here being front and center. It also takes funding that doesn't demand a 'quick' fix."
    "Mayor Sofía Álvarez stands at the head of the room, blazer neat but the lines around her eyes fresh from compromise. The fluorescent light makes everything more honest. She listens with a politician's patience — which is to say, she is already calculating."
    show mayor_sofa_lvarez at center:
        zoom 0.7

    mayor_sofa_lvarez "We are a city with limited coffers and real people sleeping on rooftops during flood probability weeks. A seawall, as Dr. Duval's firm proposes—' (her voice tightens at the name) '—buys time; it protects property values and, frankly, answers voter anxieties."

    maya_reyes "Buys time at the cost of the marsh. At the cost of livelihoods tied to that place."

    "Mayor Sofía Álvarez (sighs)" "Maya, we need solutions that are implementable within fiscal cycles. People want certainty."

    professor_rowan_hale "Certainty is an illusion when the system being relied upon is brittle. Living systems give us resilience precisely because they are flexible."

    mayor_sofa_lvarez "Flexibility sounds ideal in a lecture hall, Dr. Hale. In a city budget, it's instability. I can't promise what you want without guarantees."
    "Maya Reyes [internal]: The exchange leaves a residue like spent salt on your tongue. The mayor's worry is genuine, not cruel: choices made in urgent light narrow into lines that cut. Camille Duval's name hangs in"
    "the air like a ledger. Somewhere, the glossy flyer with the Duval Reclamation Tower — mirrored, immaculate — gleams with promises tailored to fear."
    # play sound "sfx_placeholder"  # [Sound: A murmured aside; someone mentions "Duval" under their breath.]

    "An older neighbor, hands folded like prayers, looks at you and says" "If they build that tower, they won't be thinking about our crabbing seasons."

    maya_reyes "They'll be thinking about rows of numbers,' (you say) 'and those numbers rarely match the tide."

    "Professor Rowan Hale (to the room)" "We need people to see the maps. To understand the long-term scenarios. And we need a plan that puts stewardship into the hands of the people who know this place — maintenance, monitoring, living defenses."

    mayor_sofa_lvarez "That's a heavy lift. But tonight you can present a community plan — and I'll listen. No promises beyond that."
    "The shelter hums with the kind of pressure that is low and constant, the kind that erodes patience. Camille Duval's corporate imagery exists both physically — flyers, renderings — and as a phantom that reframes every"
    "conversation. When you close your eyes, the Duval Tower is a shard of cold glass slicing through the marshlight you love."

    menu:
        "Place the tide maps flat in the center and invite questions":
            "You spread the maps wide, palms flattening paper. Neighbors edge closer, faces folding into concentration. The room leans toward data and memory."
        "Keep the maps folded, speak from memory and feeling":
            "You fold the maps into your jacket and speak from a place that isn't numbers but knowing. Some people nod slower; others look for the proof kept just out of reach."

    # --- merge ---
    "..."
    # [Scene: Community Shelter & Town Hall | Late Afternoon — Closing the Meeting]
    # play music "music_placeholder"  # [Music: The cello returns; the tempo shifts subtly, a slow rise]
    hide professor_rowan_hale
    hide maya_reyes
    hide mayor_sofa_lvarez

    scene bg ch1_Start_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hum of anxious conversation; the distant thrum of city machinery]
    "You lay out Professor Hale's tide lines, tracing the old channels with a finger. The room is quiet in that anticipatory way — not empty of sound, but full of held breath. People begin to speak"
    "in small, honest ways: the woman who runs the fish stall worried about spawning grounds; a young man who salvages dock planking asking about access rights; Lito ticking off repairs like a ledger of survival."
    "Mayor Sofía Álvarez thanks you for putting together the meeting, her voice thinner now, threaded with the weight of decisions she will have to carry home. Professor Rowan Hale gives a short, careful nod that feels like benediction."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "This is both resistance and homecoming."
    "The thought lands heavier than you expected. Guilt still hums under it, but there's a steadier place beneath that — determination. You feel the notebook in your pocket like a pulse. You imagine tonight: neighbors will"
    "leave with a contact list, a few volunteers, a plan for initial plantings, and a promise to show up for each other. It is small against the immensity of what Camille Duval offers on a polished"
    "flyer; small things often are. But it is real."
    "You look at the renderings again — the Duval Reclamation Tower, immaculate and reflective, a promise of engineered safety. In your mind it is both a threat and a challenge: a test of whether people can choose living systems over sterile certainty."
    show lito_reyes at right:
        zoom 0.7

    lito_reyes "You sure you want to do this?"

    maya_reyes "I have to.' (Your voice is quiet, steady.) 'If I don't try, who will remember why the marsh mattered?"

    "Amaya (places a hand briefly on your shoulder)" "Then we'll make tonight count. We'll get the names. We'll make the maps speak like they're alive."
    show professor_rowan_hale at center:
        zoom 0.7

    professor_rowan_hale "And I'll bring more historic charts. Science without people is just numbers. People without science are blind. We will stitch them together."

    "Mayor Sofía Álvarez (meeting your gaze)" "I can't promise you the funding you want overnight, but I'll bring the council an initial report. Bring me specifics. If it's compelling, I will act."
    "The room pulses with a tired, careful hope — the kind that sits alongside anxiety. The arousal in your chest increases just a notch: not frantic, but sharpened."
    "You fold the maps back into your notebook, the paper whispering like a small secret. For a moment, the weight of the past — the storm, the loss — presses against your ribs and you breathe"
    "through it. Then the decision arrives with the clarity of someone who has rehearsed saying yes to hard work for years."

    maya_reyes "Tonight I'll convene the neighbors for a restoration plan. Not to stop everything overnight, but to start the work that keeps us here."
    "It feels like both resistance and homecoming."
    hide maya_reyes
    hide lito_reyes
    hide professor_rowan_hale

    scene bg ch1_Start_7 at full_bg
    # play music "music_placeholder"  # [Music: The cello lingers a single, resonant chord — unresolved, patient]
    "You fold your jacket tighter against the damp and step toward the door taking the notebook with you. The city smells like rain and frying oil and possibility, and your bones feel both weary and braced."
    "You have called the meeting in your head a dozen times; now it exists as a plan on a page and a pull in your chest."
    "This is the moment you promised. It is small, and it is everything you can do for now."
    "You think of Camille Duval's flyers one last time — a mirrored tower you can see even when the lights are off — and you let the image sharpen your resolve instead of pinning you in place."
    # [Page-Turn: Your breath fogs the doorway as you step out into the marshlight; the night must be met with more than maps — with people. You feel the pull to act, to convene, to begin.]

    scene bg ch1_Start_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter2
    return
