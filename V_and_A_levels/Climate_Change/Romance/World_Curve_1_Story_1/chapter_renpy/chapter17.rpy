label chapter17:

    # [Scene: Boardwalk | Dawn]

    scene bg ch15_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low thrum of a distant engine, water lapping against pilings, a dozen quiet conversations threading through the morning air.]
    # play music "music_placeholder"  # [Music: Quick, ascending strings with bright brass punctuations — urgent, hopeful]
    "You wake before the sun and the town is still half-remembered in fog. The decision you made months ago—a hinge in a narrow room with fluorescence and too much at stake—has continued to unfold like waves finding new creases. Elias Stone took the offer. You stayed."
    "You press your thumb to the dented thermos and feel the warmth settle. Your chest is taut in a way you didn't expect: not the hollow ache of loss, but an active charge, like the moment"
    "before a tide breaks. You have learned how to hold two truths at once: personal absence and collective gain. Both are heavy; both push you forward."
    "You count the days since the call—since Elias Stone, voice steady and almost businesslike, outlined a national rollout that could scale the living-shore model you two sketched on the back of a napkin. He said the"
    "name of a grant, a city on the other coast, an institute that would finally listen. You remember the way his hand squeezed yours through the static: hopeful, fiercely practical, unwilling to pretend staying was the"
    "only way to matter."
    "You imagine him now—ash-blond hair thin against sea wind on a different shore—drafting a plan that will ripple back here. The thought makes your fingers ache in a good, purposeful way."

    scene bg ch15_3be532_2 at full_bg
    # play music "music_placeholder"  # [Music: Strings settle into a bright ostinato — steady, insistent]

    menu:
        "Walk the marsh to check the new planting beds":
            "You head out along the ribbon of boardwalk, boots slick, eyes scanning the green fringe where volunteers will arrive in two hours."
        "Call Elias to ask about the funding timeline":
            "You thumb his name and hold the phone as it rings, imagining the distant skyline he now wakes to. His voicemail is brief; you leave the plan condensed and warm."

    # --- merge ---
    "Continue"
    # [Scene: City Offices / Community Shelter | Late Morning]

    scene bg ch15_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmurs rise and fall; a microphone squeaks when adjusted. Outside, a city work crew lifts a new sign into place.]
    # play music "music_placeholder"  # [Music: Percussion building under a triumphant string line — high arousal, bright]
    "Mayor Sofía stands like someone who has spent too many nights negotiating between hope and obligation. Her blazer is neat; her hands are the honest kind that have held campaign pins and emergency forms. She watches"
    "you over the podium and, for a moment, you think of every thin compromise that led to this: late meetings, a leak exposed at a cost, a thousand small local victories strung into policy."
    show mayor_sofa_lvarez at left:
        zoom 0.7

    mayor_sofa_lvarez "Maya—this city has been through storms and harder choices than any of us wanted. But your coalition, and the work Elias Stone helped amplify, convinced the council there's another way to protect our shore—one that keeps people and marsh in the equation."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "This isn't about stopping the sea. It's about giving it something to hold on to—plants, sediments, neighbors who know how to tend them. We've built it to be learnable, transferable. We want this city to promise stewardship, not surrender."
    "The crowd answers with small sounds that build into a steady supportive chorus. Lito—wherever he is—sends a thumbs-up emoji through the projector; someone laughs. The room hums with expectancy."
    "Elias Stone appears on the screen behind the podium, grainy light and a long horizon behind him. He's in another city's harbor office, wind trimming his hair into a sculpted chaos. He smiles like someone who is trying not to cry and mostly succeeding."
    "Elias Stone: (into speaker) 'I wish I were there in person. You all know I'd rather be—' (a laugh, then sharper) '—but the grant is green. We have pilot funding matched to local stewardship contracts and"
    "a training network ready to go. Mayor, when you sign, you're not just approving a local pilot. You're creating a template I've been asking other cities to adopt.'"
    "You watch his fingers move as he gestures; there is a draft in his leather satchel splayed like a promise. His eyes find yours through the screen, and for one thin second the distance collapses into"
    "something crystalline: two people who traded presence for reach, trading the small domesticities of a shared life for a different kind of daily intimacy."
    show elias_stone at center:
        zoom 0.7

    elias_stone "Maya, your team will lead the training cohort. I'll be coordinating between sites—Seattle, Cape Verdant, the southern estuary pilot. We'll have a shared curriculum and a legal framework the mayor's office can sign onto to guarantee stewardship."

    maya_reyes "And you'll—"
    "Elias Stone: (interrupting, tenderly) 'I have to go build out the program. We'll write; we'll call. It's messy and long-distance, but it's not less real. It's not less demanding. I'm asking you to keep doing what you do best.'"

    maya_reyes "I'm already here."

    elias_stone "I know. And that matters—more than I can say."
    "The room breathes like a held exhale. The recorder ticks; cameras tilt. Mayor Sofía steps up to the signed documents—official, heavy paper with municipal seals. Her pen glows under the room's light."

    menu:
        "Ask to speak about local crew training before the mayor signs":
            "You clear your throat and offer a quick outline about mentorship and community wages. People applaud—this is the part you care about most."
        "Let the mayor sign without adding to the ceremony":
            "You stand in the crowd and let the moment be for the community. The mayor's pen lands with a small, ringing signature and the room is suddenly louder."

    # --- merge ---
    "Continue"
    # [Scene: City Offices / Mayor's Podium | Moment of Climax]
    hide mayor_sofa_lvarez
    hide maya_reyes
    hide elias_stone

    scene bg ch15_3be532_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Applause crescendos into cheers; distant foghorns seem to answer in the harbor; cameras click and someone whistles.]
    # play music "music_placeholder"  # [Music: Full orchestra—triumphant brass and racing strings; rhythmic drums push everything forward — the highest point of the chapter]
    show mayor_sofa_lvarez at left:
        zoom 0.7

    mayor_sofa_lvarez "By the power vested in me, and with the support of our council and partnering agencies, I sign this stewardship agreement. We commit municipal resources, training funds, and a legal covenant binding the land to community stewardship. Let this be the beginning, not the end."
    "The pen lifts. The paper folds into municipal history. Cameras flash. Around you, faces flood with relief and something like giddy disbelief. People clap you on the back. Amaya squeezes your shoulder until your ribs want to laugh."
    "You look at the projector: Elias Stone's face splits into a grin that is almost a laugh. He mouths something—thank you—and then, for all its public spectacle, there is a private, fierce exchange of gratitude that passes between you two like transmitted light."
    "Elias Stone: (voice lower, heard plainly despite the crowd) 'You did it. You kept them at the table.'"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "We did it."
    "A volunteer hands you muddy gloves and a young trainee in a borrowed beanie presses a paper seed packet into your palm. The smell of wet earth and the tang of salt mix into a scent you have lived inside for years."
    # [Scene: Tidal Fringe Marsh | Afternoon — Montage]
    hide mayor_sofa_lvarez
    hide maya_reyes

    scene bg ch15_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Overlapping audio—voices from different cities, laughter, a drill in the distance, the rustle of reeds. Phone calls, then letters being folded. The cadence is fast, urgent, elated.]
    # play music "music_placeholder"  # [Music: Layered rhythmic motifs; percussion keeps momentum high]
    "A week becomes a month. You move at a speed you didn't know you could hold—meeting contractors with calloused hands, briefing trainees under a battered tarp, signing off on lesson plans for other cities. Elias Stone"
    "calls at odd hours—early where he is, late where you are—and the static sometimes eats the end of a sentence. You learn to read meaning in pauses and in the unfinished lists at the bottom of"
    "his emails."
    "Elias Stone: (phone, through static) 'We just finished the first train-the-trainer session in Cape Verdant. They want the coastal buffer modeled on your cross-plugging technique. Your notes are on every desk.'"

    "You" "Are they really using the tidal-surge sensor layout we tested?"
    show elias_stone at left:
        zoom 0.7

    elias_stone "They are. They scaled it. Your spreadsheet did more than I thought it would."
    "You laugh—brief and startling. It sounds like a small explosion in your chest."

    "You" "You did more than I thought you would."
    "Elias Stone: (soft) 'We did.'"
    "You keep the field notebook in a zip pocket at your waist. You write down dates and names and the way the sun catches a particular stand of spartina. You note trainees who will become trainers,"
    "and trainers who will teach trainers in other towns. The marsh begins to feel less fragile in a practical sense; the plants take root faster than your old nightmares of erosion ever did."
    # [Scene: Boardwalk | Dusk]
    hide elias_stone

    scene bg ch15_3be532_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low conversations, a distant bike bell, the whisper of reeds. Elias Stone's voice calls from the phone, close enough to feel personal.]
    # play music "music_placeholder"  # [Music: Strings soften but keep a quick tempo—tender and insistent]
    show elias_stone at left:
        zoom 0.7

    elias_stone "I saw the footage from today. People planting in the mud the way you taught them—slow, methodical, laughing when they mess up. It's exactly what we said we'd make. You—"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Tell me the honest part."
    "Elias Stone: (after a long breath) 'Honestly? I miss your crooked coffee cups and the way you say 'watch the plume' like it's a spell. I miss how you roll your sleeves and don't ask permission to get in the mud.'"
    "Maya Reyes: (smile) 'I miss your coffee-making war stories.'"

    elias_stone "We'll write long letters. We'll send maps that look like love notes. But I can't promise mornings together. Not now."
    "You feel a stab of loss that is quick, clean, and already carrying a small, resolute heat. This is not a tragedy. This is a negotiated, adult departure—one that hurts because it mattered."

    maya_reyes "I don't want a promise I can't keep. I want you to do this, Elias. I want…more people to have what we taught them."

    elias_stone "Then go fix a damn marsh so I can stop talking about it in meetings."
    "You both laugh, and the sound is full of everything that built you."
    # [Scene: Tidal Fringe Marsh | Night — After the Ceremony]
    hide elias_stone
    hide maya_reyes

    scene bg ch15_3be532_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The crowd disperses into smaller clusters. A volunteer strums a guitar softly; a child tries to whistle and fails beautifully. Somewhere, a radio plays an old folk song about harbors.]
    # play music "music_placeholder"  # [Music: A single cello sustains a warm note as everything slows into a gentle afterglow]
    "You walk the plank toward the water alone for a moment, the mud soft under the boots. The mayor's signature is in the municipal ledger and the training modules are live; Elias Stone's role is sprawling"
    "and far-reaching. The marsh below the boardwalk glows with a dozen little bioluminescent indicators someone hung as a joke—they look like fireflies for the saline dawn."
    "You take out your field notebook. On the inside cover, in careful script, are the coordinates of the original planting. You trace them with a finger."
    "Your internal voice steadies — not empty, not numb. There is pride thumping in your chest like a fist against the ribs. Your work is not finished, but it hums with success. You are learning a"
    "new grammar for love: one that includes distance and shared purpose, that measures devotion in grant reports and in seedlings transplanted by hands that once only knew how to pull fishing nets."
    "You fold the notebook closed and tuck it back into your jacket. In the distance, a phone buzzes—another message from Elias Stone, a photograph of a new pilot site with a caption: 'They planted your method. It clings like hope.'"
    "Maya Reyes: (whisper to the marsh) 'Keep holding on.'"

    scene bg ch15_3be532_8 at full_bg
    # play music "music_placeholder"  # [Music: Swelling strings resolve into a warm major chord; the percussion thins to a heartbeat steadying into calm triumph]
    "You stand there for a long moment, warmed by the knowledge that the work you started will spread, imperfect and stubborn. People from far-off coasts will learn to read the tide in the same way you"
    "do; new stewards will sign their own agreements; some small cove will be saved because you and Elias Stone and a dozen stubborn neighbors refused to let it go without a fight."
    show elias_stone at left:
        zoom 0.7

    elias_stone "There are mornings we won't share. But I'm here in the way that counts for this work. Tell the trainees to be stubborn, and to always soak their boots before planting. You taught me that."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "I will."
    "The phone clicks. You tuck it away, colder now as the night takes it. You do not pretend the ache is gone. Instead, you let it exist next to the pride, side by side like two tools."
    "You look back at the community—faces lit with the soft glow of the after-ceremony lights. Hands that once only knew how to brace against storms now know how to graft life into the edge of the sea. The marsh breathes; so do you."
    hide elias_stone
    hide maya_reyes

    scene bg ch15_3be532_9 at full_bg
    # play music "music_placeholder"  # [Music: Final chord—warm, expansive, and lingering]

    scene bg ch15_3be532_10 at full_bg
    "THE END"
    # [GAME END]
    return
