label chapter1:

    # [Scene: Saltline Harbor | Early Morning]

    scene bg ch1_Start_1 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano with low, warm synth pads — slow tempo]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, soft creak of timber, water lapping]
    "You step off the ferry with the satchel heavy at your shoulder and the salt-shell pendant cool against your collarbone. The town meets you in the language it has always used — wind, rope, and the"
    "metallic smell of sun-bleached tar. Everything is the same and not: dock planks newer in places, patched with mismatched timber; a row of vertical gardens stitched into a leaning warehouse wall; a buoy with a hand-painted"
    "warning about low tides dangling like an old tooth."
    "Your boots sound hollower than you expect on the wet wood. The harbor breathes slowly, a long exhale. People move with a practiced economy, carrying boxes of plants, hauling nets, a child trailing a kite that"
    "wavers like a tired gull. Faces glance up when you pass; there is curiosity folded into recognition, but also the thin reserve of a town that measures weight before it trusts."
    "You let the current of the quay pull you toward the bulletin board — Rin's domain. The paper notes are layered like geological strata: peeling posters for storm-prep workshops, hand-drawn maps of evacuation routes, and a"
    "fresh, neat leaflet stamped with a corporate emblem you don't recognize. Under all of it: a bright, crooked sketch of a community potluck pinned with a bottle cap."
    # play sound "sfx_placeholder"  # [Sound: The soft slap of a hand-painted sign against a post]

    scene bg ch1_Start_2 at full_bg
    "Rin spots you before you find your voice. She comes up the board with an armful of stapled pamphlets, hair peeking from under a knit hat like a comet tail. She grins — unapologetically wide, a little shocked, a little delighted."
    show rin_okubo at left:
        zoom 0.7

    rin_okubo "Marin Alvarez? Is that really you? God, look at you — you brought back all your field gear and fashion sense too. Where've you been, the North Pole of practical sorrow?"
    show marin_alvarez at right:
        zoom 0.7

    marin_alvarez "I brought the tide band, not the North Pole. It's… good to see you, Rin."
    "Rin plops a pamphlet into your hand as if momentum alone can convey a thousand words. Her freckles seem to map out the same routes you remember from childhood summers."

    rin_okubo "We put your name on all these — well, not 'we' in the formal sense. People keep asking. Luka told half the town he saw you 'walking the shoreline' last night like some coastal ghost."
    "You laugh — it's small, the sound caught in the damp air. Laughter feels like a borrowed thing at the moment."

    marin_alvarez "Don't let Luka go telling tall tales. He's got a canon of them now."
    "Rin's smile softens, and there is a cautious tilt to her head that you remember from when you both were thirteen and trying to decide whether to sneak into the tide pools."

    rin_okubo "Look, everyone knows you left to—what did you call it—'go build the future.' People are worried, Marin Alvarez. They want to know if you'll be staying, if you'll help. And… some of them blame the old reinvestment plan. You know that."
    "You feel the sentence settle on you like wet clothing. You can hear the whisper of old rain in your bones: the marsh that was, the plan that promised safety and delivered scarred mudflats. You practiced"
    "your explanations on the ferry, on the walk in, but explanations are thin against memory."

    marin_alvarez "I know. I—' (you let the admission hang) 'I came back because I couldn't think where else to start fixing. Not because I have answers."
    "Rin studies you, a complex look that is part sympathy, part assessment."

    rin_okubo "That's what Luka says too. 'Bring hands' — he says everyone's tired of words. But people also want to know if the hands belong to someone who remembers what was lost."

    rin_okubo "Also — Kaito Sakamura was asking about you. He left a sketch at the workshop. It's terrible; you should go see it. He calls everything 'work-in-progress' like it's the name of a philosophy degree."

    marin_alvarez "Kaito Sakamura's sketches are never terrible. They're... stubbornly honest."
    "Rin cocks her head, mischief returning."

    rin_okubo "Stubborn. Honest. Archaic. Those are his brand pillars."

    menu:
        "Step toward the workshop with Rin":
            "You let yourself follow Rin's quick step, feeling the weight of the town's gaze ease with movement. The familiar thump of wooden ladders and the smell of sawdust and brine draw you in; your hands itch to touch the grain."
        "Pause at the bulletin board and read more notices":
            "You linger among the paper strata, tracing names and schedules with your eyes. The town's calendar acquaints you with its present: storm drills, coral nursery volunteer hours, a meeting about the proposed coastal barrier. You feel held in a ledger of small obligations."

    # --- merge ---
    "'Rin waits only a beat, then laughs when you choose — as if you always will. If you went with her, the rest of the conversation slides into the warmth of the workshop; if you stayed, you gather a clearer map of what faces and factions are awake here."
    "Either route folds you into the harbor's rhythm. The workshop is noisy in the way a home becomes noisy — measured clanks, the whisper of sanded wood, spice-jar tins organized like tools. If you stayed at"
    "the board, you catch Luka's silhouette across the docks first, leaned on the same bench he always used.'"
    hide rin_okubo
    hide marin_alvarez

    scene bg ch1_Start_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low rumble of his voice as he speaks to a gull he pretends to be in conversation with]
    show luka_sorensen at left:
        zoom 0.7

    luka_sorensen "Marin Alvarez. We needed someone with both hands and a head that wouldn't forget the sea's manners."
    "You approach with the slow, careful gait you use when measuring something you love. Luka's beard rustles when he smiles; the skin at his temple is a map of sun and storm."
    show marin_alvarez at right:
        zoom 0.7

    marin_alvarez "I needed to be reminded of manners."
    "Luka: 'Manners are not enough, but they're a good place to start. Sit. Tell me what you remember most.”"
    "You sit, the bench creaking under your weight like an old joint remembering its function. For a long moment you only listen: the sea, Luka's even breathing, someone hammering in the distance. The soundscape stitches a safety you forgot you could fit into."

    marin_alvarez "I remember the marsh cordgrass bending like a chorus, then—' (your voice dips) '—how quickly we mistook firmness for permanence."

    luka_sorensen "We all mistake permanence for fidelity. The lesson keeps being expensive.' (he taps the bench) 'But lessons are not always punishments. They can be maps. What matters is what you draw from them, not how clean your hands end up."
    "You consider that. Your palms, ink-smudged from field notes, feel callused in a way that doesn't match the unease in your chest."
    hide luka_sorensen
    hide marin_alvarez

    scene bg ch1_Start_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft scraping of a plane on wood]
    "You notice him before he notices you. The sun catches the line of his jaw; he moves with the comfortable economy of someone who learned rhythm from ropes and tide charts. He lifts his head as"
    "if sensing new weight in the air — perhaps it's you, perhaps it's the same intuition that led him to patch roofs before storms. He pauses, tools in hand."
    show kaito_sakamura at left:
        zoom 0.7

    kaito_sakamura "Marin Alvarez! You're back. Thought you were a rumor stitched up by the tide."
    "You stand a moment longer, as if letting the scene write itself in your chest. There's a small, familiar ache where old affection and present responsibility overlap."
    "Kaito Sakamura walks over, the harbor opening between you two like a stage set, intimate and public at once. He doesn't run; he approaches with the slow kindness that once let you share long silences while rebuilding a dinghy."

    kaito_sakamura "You look like you could use a cup of something strong and too hot for drinking."
    show marin_alvarez at right:
        zoom 0.7

    marin_alvarez "I could use both that and—' (you hesitate) '—a reckoning that doesn't make people leave."
    "Kaito Sakamura halts at the word as if it has weight purely because you named it. He pulls a cloth from his pocket, wipes sawdust from his hands, and gives you a look that is all questions folded into a single, steady presence."

    kaito_sakamura "We all want different things for Saltline. I want it to stand and sing. I haven't always known how to say the engineering part without making people feel like they're a number. Maybe you do."

    marin_alvarez "Maybe I do, and maybe I don't. I'm here to listen, not to lecture. That's all I can promise at first."

    kaito_sakamura "That's a start. Better than a promise of blueprints and silence. Come see the workshop. I have bad sketches and good coffee."
    "You both smile that tired, mutual understanding smile — the kind that says, 'we will try small things for now.' Behind Kaito Sakamura, a poster flaps. You catch the edge of a targeted leaflet: a rendering"
    "of a high concrete barrier curving down the coastline, stamped with Elena Moro's agency logo."
    hide kaito_sakamura
    hide marin_alvarez

    scene bg ch1_Start_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A faint, bureaucratic hum in your mind; a breeze lifts the paper]
    "Your stomach pinches, but the feeling is low and steady, not an alarm. Elena Moro's name has been in town conversations like a tide chart: a line people watch with both hope and wary teeth. You"
    "cannot tell from the leaflet how many homes might be moved, or how many marshes might be reshaped into engineered permanence. The details blur by design."
    show kaito_sakamura at left:
        zoom 0.7

    kaito_sakamura "Elena Moro's people have been meeting with Ishaan. They're funding surveys. It's… complicated.' (he shrugs, small) 'He stopped by last week with a tablet and a suit. He smiled a lot."
    show marin_alvarez at right:
        zoom 0.7

    marin_alvarez "That's Ishaan. They always bring smiles and models. The question is whether smiles count as consultation."
    "Kaito Sakamura frowns — not at you, but at the abstractness of policy talk that sits like an uninvited tide between you and the community. He sets his jaw, then lets it soften."

    kaito_sakamura "Whatever comes, we'll need both hands — and people who've learned from what we lost. I want to be part of that. I hope you do, too."
    "You feel something like a lighthouse turning on inside you: steady, small, practical. Not a blaze, but a necessary point of reference."

    menu:
        "Step closer and ask Kaito about the sketches he mentioned":
            "You move in as if to read his shoulders. He brightens and reaches for the sketchbook in his back pocket, flipping the pages to show you plans half-drawn in charcoal and watercolor notes of tidal gardens. His excitement is quiet and contagious."
        "Look back out over the water and speak about Elena Moro's plan instead":
            "You let your gaze travel over the harbor while you speak. Words come slower: 'We need to know what we will lose, not only what we'll gain.' Kaito Sakamura listens, brow furrowed, his desire to help steadying your words rather than challenging them."

    # --- merge ---
    "'The morning continues in the harbor’s soft metric — measured greetings, the exchange of tools, a tradesman trading a joke for a favor. Conversation here rarely moves fast; it simmers. You trade news, possibilities, and omissions like fishermen trading nets: essential, deliberate, and weathered.'"
    "At one point Luka catches your eye and tilts his head, a small gesture that holds more than a lifetime of stories. He says nothing, but his silence speaks the oldest language you know: continuity. Saltline"
    "has a way of asking you to remember your part in the story before you try to write new pages."
    "You wander the docks a little longer, letting the town collect itself around you. People nod, some with warmth, some with the careful neutrality of those who still measure trust. You feel watched in a friendly"
    "way — not the invasive kind, but the kind that keeps a town steady. Embedded in that attention is expectation, which settles in your chest like a low, persistent tide: the town expects something. Perhaps it"
    "expects your hands, perhaps your expertise, perhaps the courage to admit you do not hold the answer."
    "You touch the seashell at your throat. The pendant is colder this morning, like a question mark against your skin. You breathe in brine and a hint of wood smoke, and for a moment the harbor seems to hold its breath with you."
    "There is no high drama here, no thunderclap. The tension is tidal: slow, steady, and inevitable. You are home, and home asks for reckoning in small things — a potluck, a repaired hull, a meeting at"
    "the community hall — not just in grand infrastructure plans. The scope of what might be required is vast, but the next step will be local and concrete."
    "You feel, quietly, that the proper place to begin is not at a boardroom table with blueprints, nor at a protest line with placards, but back here where hands meet wood and neighbors trade time. Saltline's"
    "future will be written in many small acts. You do not yet know which of those acts you will lead, but you know you are not immune from the town's memory."
    "The harbor exhales as a boat slips away, ropes singing softly. A gull wheels and lands on a distant piling."
    "You look down at your callused palms one last time and let the feeling of being observed and needed fold into something like purpose. It is not triumph. It is not ruin. It is the neutral weight of a beginning."
    hide kaito_sakamura
    hide marin_alvarez

    scene bg ch1_Start_6 at full_bg
    # play music "music_placeholder"  # [Music: Piano resolves to a single, sustaining note — quiet, steady]
    "You turn toward the path that leads to the Community Hall — to schedules, to names, to the slow work of listening and planning. You know the next conversation will be different, threaded with old grievances"
    "and new proposals. You do not force an answer yet. For now, the tide is returning, and you are walking with it."
    # [Scene Transition: Walk toward the Community Hall, footprints in damp sand]
    # play music "music_placeholder"  # [Music: Fades into a low, expectant ambient tone]
    "You breathe in the harbor air once more and step forward."

    scene bg ch1_Start_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter2
    return
