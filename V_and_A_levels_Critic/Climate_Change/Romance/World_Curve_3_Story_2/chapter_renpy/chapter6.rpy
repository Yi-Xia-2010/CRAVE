label chapter6:

    # [Scene: Saltline Harbor | Morning]

    scene bg ch6_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Fast, buoyant strings underlay a drumbeat — the sound of many hearts aligning]
    # play sound "sfx_placeholder"  # [Sound: The clack of mallets, the creak of wet wood, gulls calling, a distant motor as a final barge approaches]
    "You arrive with the residual weight of the last meeting lodged in your chest — whether you came here after a cautious agreement sealed in a boardroom or after mud-streaked afternoons in a pilot marsh, the"
    "harbor greets you the same: bright, noisy, and on the edge of something that might hold."
    "The air tastes of salt and solder; kelp-smell and damp paint fold into one. Your satchel bumps against your hip. The sensor on your wrist blinks a steady green. You inhale, and the breath feels like a promise."

    scene bg ch6_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The crowd quiets as Luka steps down from the lighthouse crate, his voice carrying over the water]
    show luka_sorensen at left:
        zoom 0.7

    luka_sorensen "Saltline built a thousand small answers before big ones were invented. Today we make another."
    "You feel the crowd lean into the sentence, the weight of history pressing inward and opening outward at once. Maya races past, cheeks flushed with wind and excitement, a camera bobbing at her chest. Kaito Sakamura"
    "is there already, sleeves rolled and palms inked with rope—he looks up at you, eyes steady as the horizon."
    show kaito_sakamura at right:
        zoom 0.7

    kaito_sakamura "You ready for a miracle or a mess?"
    show marin_alvarez at center:
        zoom 0.7

    marin_alvarez "Ready for whatever the harbor needs."

    kaito_sakamura "Good. I don't want to be the only one covered in kelp when the mayor arrives."
    "The spoken banter hides something deeper — a tether between you that has stretched and been knotted, frayed and repaired. You notice how his thumb grazes the wooden compass at his neck, how he's kept a"
    "careful distance until now, waiting for you to take the lead. He doesn't step forward; he matches your pace."
    hide luka_sorensen
    hide kaito_sakamura
    hide marin_alvarez

    scene bg ch6_4001e7_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of the agency's portable generator mixed with the harbor's analog noise]
    show elena_moro at left:
        zoom 0.7

    elena_moro "The slabs' tolerances held in yesterday's stress test. The hybrid anchors will take the worst of the surge and the kelp will dampen the current. It's a compromise that performs."
    "You hear the technical precision in her words and the echo of something approachable — a careful admission that structure and organism can cooperatively do what one alone cannot. Her face is unreadable for a moment; then, almost imperceptibly, her jaw loosens."
    "Ishaan: (offering a thin folder) 'Funding is in the account. The charter language is on the table. We have signatures pending community co-signing.'"
    show marin_alvarez at right:
        zoom 0.7

    marin_alvarez "Then let's not waste time."
    # play sound "sfx_placeholder"  # [Sound: A cheer rises as the final barge nudges into place carrying coral frames cradled like newborn boats. Children press against the temporary railings, glittering with sea-spray.]

    menu:
        "Check the sensor readings one last time":
            "You crouch by the scale platform, fingers cold on the display. Numbers slide into the green band and your chest unclenches—practical reassurance. You stand, calling for volunteers with a voice steady from certainty."
        "Search the crowd for Kaito's eyes":
            "You scan faces until you find him near the south frame, grin wide and hands raised. Relief floods you in a warm, ridiculous rush; you shout his name and he answers with a laugh that is everything and nothing you expected."

    # --- merge ---
    "Continue the scene at the next direction cue."
    # play music "music_placeholder"  # [Music: Strings swell; percussion quickens]
    hide elena_moro
    hide marin_alvarez

    scene bg ch6_4001e7_4 at full_bg
    show maya_chen at left:
        zoom 0.7

    maya_chen "Marin! The nursery kids said their coral nodes are already showing polyps—look!' (She thrusts a trembling tablet into your hands; the close-up shows tiny white dots winking on a glimmering frame.) 'They're alive."
    show marin_alvarez at right:
        zoom 0.7

    marin_alvarez "Good. That's good—keep them shaded for the next two tides."

    maya_chen "Two tides? You sound like Luka now."
    show luka_sorensen at center:
        zoom 0.7

    luka_sorensen "You listen to the sea long enough and you pick up the old grammar."
    "The crowd surges forward as the final frame is slotted onto the slab. Hands of all ages and calluses align — fishermen, tide-lab technicians, teenage activists with cropped hair, elders with arthritis ironically generous with rope."
    "Elena Moro steps forward and, with a practicality that is almost a caress, ties a final securing line."
    hide maya_chen
    show elena_moro at left:
        zoom 0.7

    elena_moro "This is better than any model in my feed. It has you in it."
    "Her gaze meets yours, and you hold it, letting ambiguity live there — complex, honest. It isn't capitulation; it's recognition."
    # play sound "sfx_placeholder"  # [Sound: Thunder murmurs far off, like a drum-roll. The sky keeps a reserved blue, but the moment is urgent.]
    # play music "music_placeholder"  # [Music: Brass blares briefly, like a call to arms turned celebration]
    hide marin_alvarez
    show kaito_sakamura at right:
        zoom 0.7

    kaito_sakamura "No backing out if this goes sideways. You keep steering and I'll keep fixing whatever you point at."
    hide luka_sorensen
    show marin_alvarez at center:
        zoom 0.7

    marin_alvarez "Deal."
    "The ceremonial moment arrives — a long plank lowered between two slabs, a portable table set with a stack of paper, pens, and a damp cloth. Luka clears his throat and the harbor hushes, a human breath held."
    hide elena_moro
    show luka_sorensen at left:
        zoom 0.7

    luka_sorensen "Saltline won't be saved by a single day's heroics. It will be saved by people who promise to keep doing the hard small things, and by those who will lend their muscle when the tide comes. Today we sign to share power, money, and obligation. We sign to be both stewards and auditors, to be accountable and kind."
    "You step to the table. Elena Moro is at the other end; Ishaan holds the pen like it's both sword and bridge. Kaito Sakamura stands at your side, thumb rubbing the compass pendant."
    hide kaito_sakamura
    show ishaan_rao at right:
        zoom 0.7

    ishaan_rao "The clause guaranteeing community co-signatory rights is enforceable and non-negotiable. It took some arguing, but it's there."

    marin_alvarez "Good. That was non-negotiable for us. It keeps the marsh protected, and it keeps people at the table."
    hide marin_alvarez
    show elena_moro at center:
        zoom 0.7

    elena_moro "We architected the slabs to protect the core and left gaps for living systems to integrate. You fought for the kelp corridors; we did the load-bearing. We both had to lose our purity to get here.' (She looks at you, then at Kaito.) 'Turns out practical compromise can smell like the sea."

    menu:
        "Reach for the pen and sign immediately":
            "Your name glides across the paper; the pen leaves a smear of ink that looks, in the sunlight, like a river. The crowd claps and you feel the sound reach into the places in your chest that had been hollow. Elena nods, something like relief in her posture. Kaito squeezes your shoulder and you think, for a heartbeat, that this is enough."
        "Take Kaito's hand first, then sign together":
            "You take his callused hand and hold it like an anchor. He squeezes back, steadier than any engineering plan. Together you sign, hands brushing over the ink. The crowd dissolves into applause; Luka laughs and tells a corny joke about tides and temperaments. Your chest burns with a kind of joy that's been earned."

    # --- merge ---
    "Continue the scene at the next direction cue."
    # play sound "sfx_placeholder"  # [Sound: Applause crescendos — a real, ragged, unapologetic sound. Someone starts a work-song that morphs into a chant; others join, harmonies rough and wholehearted.]
    "You step back as the signatures finish. Elena Moro signs with a quick, precise stroke. Ishaan's hand trembles a little as he signs; you see his professional armor soften. He looks at the charter, then at the people laboring in the harbor, then at you."

    ishaan_rao "This is the right call. We built the scaffolding. You built the will."

    "Maya climbs onto a crate and shouts, voice thin with adrenaline" "Saltline for Saltline!"
    "The chant picks up. Children weave kelp into streamers and drape them over the slabs; an elder pours a small libation of seawater over the corner of the largest slab — part blessing, part measurement. The"
    "frames settle; the kelp flutters and the coral nodes, suspended, catch sunlight like small promises fulfilled."
    hide luka_sorensen
    hide ishaan_rao
    hide elena_moro

    scene bg ch6_4001e7_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A collective intake of breath, then a roar of true, astonished approval]
    show kaito_sakamura at left:
        zoom 0.7

    kaito_sakamura "You did it. We did it."
    show marin_alvarez at right:
        zoom 0.7

    marin_alvarez "We did it.' (You feel the words like an anchor and an unfurling at once.) 'This isn't the end. It's the first long step."

    kaito_sakamura "Then let's take a thousand more."
    "Your lips brush for a moment — nothing cinematic, just a contained, fierce press of warmth against cold salt on your skin. It is small, decisive, real. When you pull apart, his smile is immediate and"
    "open, and you see, without needing to be told, that this is a partnership that will measure itself in tides and conversations, in repairs and rituals."
    show luka_sorensen at center:
        zoom 0.7

    luka_sorensen "Tonight, we light the lanterns on the promenade. We'll sing the old harbor hymn for those we lost and for the ones who stayed. Bring your tools. Bring your stories."
    hide kaito_sakamura
    show maya_chen at left:
        zoom 0.7

    maya_chen "And photos! We need a chronicle!"
    hide marin_alvarez
    show elena_moro at right:
        zoom 0.7

    elena_moro "I underestimated the stubbornness of your people. I should have known they'd win me over."
    hide luka_sorensen
    show marin_alvarez at center:
        zoom 0.7

    marin_alvarez "We win each other, sometimes."
    # play music "music_placeholder"  # [Music: A swelling chorus of strings and woodwinds; the tempo slow now, triumphant but intimate]
    hide maya_chen
    hide elena_moro
    hide marin_alvarez

    scene bg ch6_4001e7_6 at full_bg
    "You stand at the harbor edge with Kaito Sakamura, Luka beside you, Maya buzzing like an electric current. Elena Moro and Ishaan linger at the signing table, talking low. The charter is tucked into a waterproof"
    "tube and handed to the cooperative's clerk — a ceremonial act that feels like giving the town a pulse."
    show luka_sorensen at left:
        zoom 0.7

    luka_sorensen "The sea will give and the sea will take. But we will be there to help when it does. We will show up."
    "You feel the truth of that in your bones. The guilt that once made you curl inward loosens, rewired by a community that can hold failure and triumph at the same time. The work will be"
    "long; storms will come. But there is now a scaffold — engineered and living — and a governance that binds finances to people. It's imperfect and fierce, and you love it."
    show kaito_sakamura at right:
        zoom 0.7

    kaito_sakamura "Dinner at the workshop? I made something that might be edible."
    show marin_alvarez at center:
        zoom 0.7

    marin_alvarez "I'll be there. Bring the compass; I'll bring the tide charts."
    "You walk the plank back toward the town as the lanterns bloom and people begin to sing. The work songs fold into an old hymn, and the harbor listens. The kelp frames sway in the settling light like slow applause."
    hide luka_sorensen
    hide kaito_sakamura
    hide marin_alvarez

    scene bg ch6_4001e7_7 at full_bg
    # play music "music_placeholder"  # [Music: Full, warm strings carry the final chord; a single piano line threads through — steady, hopeful]
    # play sound "sfx_placeholder"  # [Sound: Laughter, low conversation, distant gulls settling for the night]
    "You let the moment land. It is a victory measured in many small hands and in the signatures that bind money to accountability, in the living beds that will keep salt at bay while nourishing life."
    "It is a healing of a different sort: the practical mending of marsh and relationship."
    "Kaito Sakamura slips his arm around your waist as you both watch the tide consider the new edge. You feel the familiar sea-salt on your face and a steadiness in your chest you haven't known for a long time."
    show luka_sorensen at left:
        zoom 0.7

    luka_sorensen "Tonight we remember who's here. Tomorrow we begin the next phase."
    "You nod, because you already know. There will be endless lists and measurements and arguments and small miracles. There will be nights when the work seems to unravel and mornings when the kelp frames hold a"
    "new polyp of life. But for now, the harbor is full of music and the sound of a people choosing each other."
    hide luka_sorensen

    scene bg ch6_4001e7_8 at full_bg
    # play music "music_placeholder"  # [Music: Resolves into a single, sustaining note — peaceful, open, certain]
    # play sound "sfx_placeholder"  # [Sound: The tide sighs forward; a gull cries once like punctuation]

    scene bg ch6_4001e7_9 at full_bg
    "THE END"
    # [GAME END]
    return
