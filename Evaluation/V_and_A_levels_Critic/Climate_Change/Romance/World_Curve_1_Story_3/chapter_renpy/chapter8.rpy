label chapter8:

    # [Scene: Glass Harbor Development Site | Late Afternoon]

    scene bg ch8_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Sirens taper into harsh, metallic whistles; a chorus of voices—chants, orders, and a distant gull—threads through the air]
    # play music "music_placeholder"  # [Music: Urgent strings build; percussion drives forward]
    "You are standing with your palms full of salt and soil. The pilot habitat behind you gleams like a fragile promise—its solar textile sails half-furled, its reed baskets full of the marsh plants you've coaxed into"
    "life. The crowd around you is a living, breathing map of Maris Bay: neighbors in sun-creased hats, teenagers with seed beads tangled in their hair, older hands callused and steady."
    "An officer's warning still hangs over the site like a thin rain. You can taste it—metallic, sharp—and beneath it the constant, low exhale of the ocean. Your barometer swings in your palm, a tiny copper pendulum measuring something older than municipal laws: pressure."
    # play sound "sfx_placeholder"  # [Sound: A shout—"They're taking the beds!"—cuts across the site]

    scene bg ch8_6b08b4_2 at full_bg
    "They move like a machine that has been taught to ignore memory. One security worker reaches for a seed bed—a neat rectangle of planted marshgrass that you've organized by neighborhood. Hands close around the crate; a grown man in a high-visibility vest lifts it like taking a child's keepsake."
    "Tala is first to him, a daylight flare of motion. She lunges, voice bright and sharp."
    show tala_ruiz at left:
        zoom 0.7

    tala_ruiz "Put those down. Those belong to the community."
    "Security: (cold, clipped) 'Private property. Clear the area.'"
    "The man tries to step past her. The crowd surges as if a current runs beneath everyone's feet. Someone grabs the edge of the crate. Another voice—older, steady—begins to sing under the shout, a low, familiar fishing tune that seems to gather courage."
    "Captain Reyes moves through the press like a ship through fog, his presence part memory, part authority. He plants himself between the workers and the seedlings, a low wooden stick in his hand more like a staff than a weapon."
    show captain_reyes at right:
        zoom 0.7

    captain_reyes "Those beds are not just plants. They're our buffer. They're what keeps our nets from dragging in mud when the tide takes a mind to rise."
    "You feel the scrape of the crowd—breath, fabric, the metallic click of camera shutters. Evan stands a few paces away, his brass camera lifted but steady, eyes narrowed into a slow, guarded focus. When his gaze"
    "finds you, there's something unreadable in the way he holds himself: apology and resolve braided together. He doesn't run. He doesn't shout. He records."
    hide tala_ruiz
    hide captain_reyes

    scene bg ch8_6b08b4_3 at full_bg
    # play music "music_placeholder"  # [Music: Strings intensify; a drumbeat underlines a ballooning chorus of voices]
    "The security worker grips harder. A scuffle—two steps, one shove; a wet thud of someone being pulled off-balance. A handful of volunteers are separated and cuffed before your eyes. Someone cries out. It is not violent"
    "in the cinematic sense, but it is intimate and precise: hands, breath, the sudden absence of a friend in your line of sight."
    "Your think-piece listing of priorities—protect the marsh, keep people in their homes, scale Evan's kit—collapses into the simple arithmetic of the moment: who will stand and who will be taken."

    menu:
        "Step forward and place your body between the security and the seedlings":
            "You shove past Tala, breath hot with salt, and plant your feet in front of a crate. A security guard hesitates, then grips your shoulder. You taste grit and determination."
        "Stay where you are and begin the chant, louder":
            "You lift your voice and the chant finds a hundred cords. The sound is a physical thing, pressing around the men in vests and making them blink as if into light. People tighten their arms around one another."
        "Reach for Evan's camera and steady his recording":
            "Your fingers brush the brass; Evan looks at you and exhales like he's been holding his breath. He nods, small and grateful, and his lens keeps turning."

    # --- merge ---
    "Return to main scene"
    "Hands—yours, Tala's, Captain Reyes'—move in the blurred middle distance. An officer takes names, a clipboard like a ledger of loss. The first pair of cuffs closes with a small, sharp sound. Legal consequences begin to fall into place before the dust settles."
    "You taste fear, and beneath it an electric bright hope. The arrests will be a headline; they will put pressure on the developer's PR. They will also be a wound people will carry. That duality thrums through you like an exposed wire."

    scene bg ch8_6b08b4_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low, urgent hum grows—reports being called, phones clicking through live feeds, the murmur of legal advice being whispered]
    "Captain Reyes draws closer, voice like a tide that remembers both calm and storm. He speaks deliberately, not to the security but to the people—so that everyone can anchor to what he says."
    show captain_reyes at left:
        zoom 0.7

    captain_reyes "Years back, we fought like this. Not for pride, but because if the line breaks, the sea takes more than nets. It takes the memory of why we kept them. We stood, we bled, and we taught our children to stand with us. This is the next line."
    show maya_alvarez at right:
        zoom 0.7

    maya_alvarez "Captain—"
    "Captain Reyes: (cutting gently) 'You don't need me to tell you that, niña. You know what happens when grass goes away. You know the taste of mud on the tongue. But remember—standing is not the same"
    "as winning. We made wins by making people see the water 'fore it climbed the stair.'"
    "He lets the sentence hang. It is counsel and a charge. Around you, faces harden with decision. Some tremble; others look as if choice has been pried from their hands and placed on a table to be divided."
    "Dr. Sora Kim appears at your shoulder as if materializing from the fog of incense and smoke that is now community anger. Her lab coat is patched, and her cheeks are flushed from the adrenaline of fieldwork and moral exasperation."
    show dr_sora_kim at center:
        zoom 0.7

    dr_sora_kim "We can make a paper that will sting. Rapid-impact data on the marsh's buffering capacity, economic models tied to long-term flood reduction, high-frequency drone footage showing erosion rates—synthesized fast. I can put a team on it tonight."

    maya_alvarez "An injunction? How fast could that move?"
    "Dr. Sora Kim: (brows narrowing) 'Fast, for science. Slow to effect legal stops unless we pair it with an emergency motion. Courts move differently than tides. Evidence alone rarely halts a shovel; it delays, it complicates. But it builds the case in a way the media can't drown.'"
    "You press your thumb into the cool copper of the barometer. Its swing feels like measuring the crowd's heart."
    "Mayor Lionel Park steps onto the plywood stage, hands raised not in victory but in an appeal for calm. His face is the face of someone balancing payrolls and petitions. He tries for empathy; his voice trembles in places."
    hide captain_reyes
    show mayor_lionel_park at left:
        zoom 0.7

    mayor_lionel_park "Everyone—I'm listening. I know you. I grew up here. But we also have to think of jobs and funding—"
    "Tala: (cutting in, hot) 'You think of payrolls and not of who'll have a porch next season.'"

    mayor_lionel_park "No—I'm trying to—there's a legal path, a negotiated path. Arrests will fracture this town."
    "Tala's glare could cut glass. The crowd's murmur turns into a low growl of impatience. You can feel the town's history press in on every syllable."
    "Evan remains on the fringe, hands folded around his camera like a talisman. Maya Alvarez moves toward him for a breath."

    maya_alvarez "Evan. Stay. We need your footage. We need you."
    "Evan Kaito: (soft, the words pulled slowly) 'I thought about stepping in. I thought about making a stand the same way I helped build those concrete models in the city once. I can't undo that. But"
    "I can make sure the world sees this. I can run data streams, build a time-lapse. I won't walk away.'"

    maya_alvarez "You don't have to carry—"
    "Evan Kaito: (interrupting, barely smiling) 'I'm carrying it already. I won't let it rot in silence. I won't let you do it alone.'"
    "His voice is steady, a small anchor. There is guilt in it, but also a hard-won decision. When he speaks, his fingers lightly tighten on the camera strap. It's a quiet, intimate promise."

    menu:
        "Take Evan's wrist and whisper a plan":
            "You hook your fingers with his. For a moment the world narrows to two rhythmically beating hearts and a schematic sketched in sand—the pilot, the filming angles, a timeline. Evan gives you a small, raw nod."
        "Turn back to the crowd and shout for legal volunteers":
            "Your voice cuts through the clamor. People peel off, hands raised and ready; lawyers and neighbors step forward, the crowd rearranges into a plan. Tala grins; the energy shifts."

    # --- merge ---
    "Return to main scene"
    "Dr. Sora Kim's offer hangs like a possible bridge. Captain Reyes has set memory and moral force against the workers. Arrests have already been made. Evan will not abandon you. Tala's grin is fierce as an engine."
    "The air is thick—dust, seawater, the copper scent of adrenaline and the faint sweet of crushed seedpods. Everything feels dangerously close: the machines, the law, the town's past and future. The moment has the quality of"
    "a tide turning—too soon and lives are flung; too late and the marsh is gone."
    "Your barometer swings wildly, then steadies as if answering your breath. Your chest is tight, but not with defeat. It is tightly wound with a different feeling: resolve. Hope threaded through risk. The town is looking"
    "at you because you are the one people have trusted to translate memory into policy, grief into action."
    "You think of the pilot habitat behind you, glowing in the late light—an argument in wood and sailcloth. You think of the people cuffed and the faces that will remember. You think of the legal machinery"
    "that could pause a shovel and the science that could force the public's eye to linger."
    "The crowd presses in, and your barometer swings one last time against your palm, like the metronome of a choice about to be played."
    hide maya_alvarez
    hide dr_sora_kim
    hide mayor_lionel_park

    scene bg ch8_6b08b4_5 at full_bg
    # play music "music_placeholder"  # [Music: A final, high, sustained chord that begs release]
    "How far do you escalate on the frontline?"

    menu:
        "Hold the blockade, risk arrests to stop construction.":
            jump chapter9
        "File an injunction backed by Dr. Sora Kim’s rapid science; pause construction through legal channels.":
            jump chapter11
        "Accept a short truce protecting the most vulnerable and double down on public pilot demonstrations.":
            jump chapter15
    return
