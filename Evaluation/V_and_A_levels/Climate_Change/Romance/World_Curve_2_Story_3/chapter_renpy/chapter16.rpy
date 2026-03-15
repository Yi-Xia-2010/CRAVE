label chapter16:

    # [Scene: Glasshouse Lab & Seedbank | Night — Immediately after the withdrawal order]

    scene bg ch14_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Pumps humming, the whisper of plastic tarps being folded, the metallic clink of sample vials]
    # play music "music_placeholder"  # [Music: High, urgent strings — staccato, relentless]
    "You arrive like you always do when the town tilts toward crisis: hands full, breath short, mind cataloguing what must not be lost. The seedbank door is already ajar — Mika at the threshold, cheeks wet"
    "with rain or fatigue, or both. You taste salt and solder in the air; the glasshouse smells of wet soil, iodine, and the expensive sterility of preserved possibility."
    "You don't need to tell anyone what to do. They know. Your voice catches on the right words and then drops away, replaced by the work that keeps panic from becoming catastrophe."
    show mika_tran at left:
        zoom 0.7

    mika_tran "We got the long-terms in the insulated racks. Backup drives are encrypted and offsite. I can... I can take the rest — I'll swap the drone batteries and—"
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "Prioritize spores and raw culture lines. The living samples first. If we lose the protocols, we can rebuild — if we lose the living stock, we lose the lineages."
    "Mika looks up at you, eyes wide and young in the green light. Her fingers are steady but fast, the motion of someone who learned urgency from sleepless nights and too-small tools."

    mika_tran "We should seal the east shelf, too. Kai said to pull the test long-line immediately, but—"
    "You don't answer. Your thumb rubs the buoy pendant through the flap of your jacket — an absent gesture that steadies the rhythm in your chest. The pendant is a small, personal talisman that has outlived"
    "speeches and promises; tonight it is a compass you don't trust but can't stop consulting."
    hide mika_tran
    hide marina_reyes

    scene bg ch14_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The crack of thunder far off, then closer — like a thrown voice]
    "Kaori 'Kai' Matsuda's arrival is a collision. She storms in, neon braid swinging, solar wristband blinking like an annoyed beacon."
    show kaori_kai_matsuda at left:
        zoom 0.7

    kaori_kai_matsuda "You pulled them back. You pulled us back. Marina Reyes—' (she stops when she sees the trays) 'You can't just prioritize 'future work' while the machines push people's houses into the mud."
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "If we keep bodies in the water and the seedbank dies, there is no future to fight for. We preserve the archive — we preserve the argument."

    kaori_kai_matsuda "Or you preserve the trophies that let them write us out of the story. Old money and engineers will take the data, and the people who showed up with dirt on their boots will be gone."
    "The exchange sharpens everyone in the room like a dropped knife. Amalia hovers by the rack with a damp clipboard; the festival plans she folded and refolded are now a paper map of promises. Her voice breaks when it comes."
    show amalia_reyes at center:
        zoom 0.7

    amalia_reyes "People trusted you tonight. They came because you asked them to stand. You said you'd stand with them."
    "Your chest tightens — you hear the accusation as if hammered on wet wood. You also hear the pile-driver from the flats, a dull, infuriating punctuation to every thing said inside the glass."

    marina_reyes "I know what I asked them. I asked them to protect what will let us come back."
    hide kaori_kai_matsuda
    show mika_tran at left:
        zoom 0.7

    mika_tran "We don't have time to debate the ethics of triage.' (She snaps a lid closed with a practiced motion.) 'We have to move the incubators into the internal vault. Kaori — can you and Amalia coordinate volunteers to carry trays? I'll lift the cold packs."
    "Kaori 'Kai' Matsuda stares at you for a long, flat moment before brute pragmatism overrides outrage. You watch her jaw work, see the internal calculation flipping between fury and focus."
    hide marina_reyes
    show kaori_kai_matsuda at right:
        zoom 0.7

    kaori_kai_matsuda "Fine. But I'm not fixing this later with 'we got lucky.'"

    menu:
        "Help Mika lift the heaviest incubator":
            "You crouch and feel the unit's weight, the metal biting into your palms. The two of you move as if by muscle memory and the incubator slides into the cart. Mika exhales, small and fierce. 'There,' she says. You nod and your heart is a drum that won't slow."
        "Step outside to check the flats for escalation":
            "You push the door open and the cold breath of the night hits you. At the flats, floodlights rake the dark; you see the grey shape of a bulldozer and a line of townspeople like a ragged incision on the shore. The sound of shouting lances the rain. For a second you are an outsider in both places."

    # --- merge ---
    "The choice you make — whether in muscle or in gait — is a performance that says something to the people in the glasshouse. It matters less than the work, but it matters."
    # [Scene: Tidal Flats | Night — Outside, where the long-lines still drape the water]
    hide amalia_reyes
    hide mika_tran
    hide kaori_kai_matsuda

    scene bg ch14_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Engines idling, voices colliding, the slap of wet rope]
    # play music "music_placeholder"  # [Music: Percussive, breathless — drumbeats pushing forward without relief]
    "You step out of the glasshouse with a cart humming and the taste of urgent loss on your tongue. Someone — a neighbor with a market-voice — hurls the word 'coward' into the dark and it finds its mark. You feel it as a tangible bruise across your sternum."
    "Old Tom stands a little apart, hands deep in his coat, rain spitting white through the brim of his cap. He doesn't look at you but he tells you the tide patterns as if reading a line of scripture."
    show thomas_old_tom_bellamy at left:
        zoom 0.7

    thomas_old_tom_bellamy "You did what you had to, girl. Saving seeds ain't the same as saving houses, but it's seed you save tonight, you save tomorrow."
    "His voice is small, and the tide has taken the edges off whatever comfort it could have given."
    "Kaori 'Kai' Matsuda moves like a force of nature: she climbs onto a pile, hollering coordinates, coaxing volunteers who are shaking with rain and adrenaline. She is doing no less than trying to reforge the momentum you pulled away from."
    show kaori_kai_matsuda at right:
        zoom 0.7

    kaori_kai_matsuda "We can still make a spectacle! We can still show them the long-line works!' (She points at the line taut in the water.) 'If we pull the machines in front of it, cameras will bite. We get one good shot and maybe—"
    show marina_reyes at center:
        zoom 0.7

    marina_reyes "You can't stall the machinery forever. If anyone gets hurt, everything we need to argue for later disappears under litigation and force.' (You feel the words like a stone that doesn't sink so much as settle inside you.) 'I won't gamble people's safety for a shot."
    "Her face splits into something that is less anger now than heartbreak and contempt. The crowd's reaction is immediate — many of them nod, resigned; several shake their heads like a public scolding."
    hide thomas_old_tom_bellamy
    show amalia_reyes at left:
        zoom 0.7

    amalia_reyes "They wanted me to tell you not to leave. They said when word got out they'd come. Don't you feel that? The weight of everyone who expected you to choose them?"
    "Mika, nearby, is dripping saltwater off her jacket into the mud. She looks younger than her tasks, and her hands tremble as she checks straps and seals. You notice this detail and it pains you: the"
    "apprentice whose whole life you are trying to safeguard looks like she will bend, not break."

    menu:
        "Call for a medic and a hotline for legal observers":
            "You lift your voice, steady enough to be heard. A town volunteer grabs a radio and nods. 'Medic's on the way,' someone answers. A small procedural chain starts — legal observers, camera logs — the kind of slow bureaucracy that can become armor. It feels insufficient, but it is something."
        "Confront Kai publicly and try to persuade the crowd":
            "You climb onto the same pile Kaori \'Kai\' Matsuda stands on and call out, voice raw. You speak about lineage and life and the cold arithmetic of triage. Half the crowd listens; half of them close like shutters. Kaori \'Kai\' Matsuda's jaw sets and she steps forward like a collision you're trying to avoid."

    # --- merge ---
    "You try both, because there is no single answer that can hold the world together tonight. Each action feels like it widens a split — between urgency and prudence, between flash and foundation."
    hide kaori_kai_matsuda
    hide marina_reyes
    hide amalia_reyes

    scene bg ch14_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A sudden shout — "They're hauling the line out!" — and in a heartbeat the crowd moves toward the water like a single organism.]
    "The contractors are methodical, the pile-driver a metronome of inevitability. Men in reflective vests move with the certainty that law and contract give them. They will clear the way. They will say they are protecting infrastructure."
    "You watch as a rope — one of the long-lines you fought for — is winched, not with reverence but with procedure. It doesn't make a sound that comforts; it makes a grinding sort of sound like fabric being rubbed raw."
    "Kaori 'Kai' Matsuda lunges for a stake, for a camera, for a headline. Hands grab her and pull; someone hits a radio. For a second you're afraid she'll be hauled off. She isn't. She stands, shaking, altar of neon braid and stubbornness."
    show kaori_kai_matsuda at left:
        zoom 0.7

    kaori_kai_matsuda "You chose a vault over a body. Do you know how that reads?"
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "I chose a future where our offspring can call this place home. I chose the biology of the bay over the immediate theater of resistance."

    kaori_kai_matsuda "Theatre wins votes. Roots win arguments later — if anyone's left to hear them."
    "Amalia intervenes in a way that is both fierce and small: she folds herself around volunteers with a flurry of instructions, protective as a mother, trying to take anything she can from the night and turn it to shelter."
    show amalia_reyes at center:
        zoom 0.7

    amalia_reyes "We preserved the archive. We didn't lose everything. We'll come back—"
    "A disbelieving laugh cuts her off. Someone in the crowd throws a wet rag that slaps the muddy ground between you and the machines like an accusation."
    # [Scene: Glasshouse Lab — The Vault Door]
    hide kaori_kai_matsuda
    hide marina_reyes
    hide amalia_reyes

    scene bg ch14_601bcb_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The thud of the door closing; the echo like a gavel]
    # play music "music_placeholder"  # [Music: A single high note sustained, then cut — silence that is not relief]
    "You stand with the last tray in your hands. The interior vault is a small room that once felt like a future's heart; now it is a sealed compromise. You slide the tray into the insulated"
    "rack, fingers numb. Mika begins to type the final log entry into the offline ledger; her face by the light of the tablet is pale and set."
    show mika_tran at left:
        zoom 0.7

    mika_tran "Copies are sealed. We routed an encrypted manifest to three trusted contacts offsite. Physical keys are split between Amalia, me, and—' (she looks at you) '—you."
    "Your name in her mouth is a coin that clinks on a hard floor. You are both named and made ornamental by it. The vault door descends, a metallic sigh that feels like both protection and a tomb lid."
    "You put the last seal — an old piece of wax run over twine — and the smell of it catches in your throat: warm beeswax, fossil and funeral. You lock the inner latch and then"
    "the outer one. The seals carry the weight of futures that might yet be claimed."
    show amalia_reyes at right:
        zoom 0.7

    amalia_reyes "We bought time,"
    "Kaori 'Kai' Matsuda, who has finally come back inside, stands with mud on her boots and fury on her shoulders. She stares at the sealed door like it is the thing that should have stayed open and fought."
    show kaori_kai_matsuda at center:
        zoom 0.7

    kaori_kai_matsuda "You can seal the seeds away, but you can't seal the resentment. People will remember tonight."
    hide mika_tran
    show marina_reyes at left:
        zoom 0.7

    marina_reyes "I know."
    "No one in the room believes you entirely. You don't either. You feel the coldness of the steel under your palm as you step back. This was a preservation and also a surrender. Saying it aloud doesn't make it cleaner."

    menu:
        "Tell Mika to prepare a public statement that frames this as triage":
            "You begin to dictate, voice trembling but precise: 'To our community — we prioritized living stock to ensure the continuity of restoration efforts. We will not abandon the people of Laurel Bay.' Mika nods and begins typing. The words take shape like a scaffold, but none of them erase the wet footprints outside."
        "Go out and stand where the long-line was, alone":
            "You step into the rain and stand at the edge of where the kelp buoyed a promise. Night presses in, and you feel smaller than the sound of the machines. You taste betrayal on the air; sometimes it is your own. Your buoy pendant bangs cold against a rib and you hold it like a small accusation."

    # --- merge ---
    "The choice of what to say — whether to craft a narrative that stitches this night's fractures — is a small theater. The damage has been done in gestures and absences, not in phrasing alone. Still,"
    "words matter. You know that the public line will be picked apart and repurposed by journalists, organizers, and the opponents who will reframe your prudence as timidity."
    hide amalia_reyes
    hide kaori_kai_matsuda
    hide marina_reyes

    scene bg ch14_601bcb_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A child's voice in the crowd, asking a question into the rain; no answer comes]
    # play music "music_placeholder"  # [Music: Crescendo of strings, then a harsh, very high violin that scratches at the edges of your hearing]
    "Everything accelerates — calls from volunteers, the sudden need to account for people, the small hands that must be kept safe. Your chest is tight in a way that feels like a bruise spreading under the skin."
    "You think of your father's hands, how callused they were, how they taught you that preservation is sometimes a slow and stubborn thing. You hear your own voice echo in the vault: did you make the right call? Is there a right call?"
    "Kaori 'Kai' Matsuda steps close, close enough that you can feel the heat from her jacket despite the rain."
    show kaori_kai_matsuda at left:
        zoom 0.7

    kaori_kai_matsuda "You did what you thought would keep the work alive. I can respect that. I can also hate you for it."
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "I don't want you to hate me. But I don't have the luxury of a single righteous stand if it costs the biology we're trying to scale."

    kaori_kai_matsuda "Then don't be surprised if the town chooses theater. They wanted you to be the banner tonight, not the archivist."
    "Her accusation lands like rain: consistent, indifferent, wetting everything. Around you, the people who stayed begin to filter back into the lab, faces washed clean by exhaustion and salt. Some offer condolences. Others offer silence that screams."
    hide kaori_kai_matsuda
    hide marina_reyes

    scene bg ch14_601bcb_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The vault's latch clicks; outside, the machines continue their slow, inevitable work]
    # play music "music_placeholder"  # [Music: A single, relentless percussion — heartbeat tempo]
    "You have preserved possibility. You have also fractured trust. The future you protected is a small, dark seed in a cold room, wrapped and labeled. It will not sprout while it is sealed; it only waits."
    "You cannot erase the night. You can only account for your choices, and later, if there is time and luck, try to stitch them back together with truth and labor."
    # [Page-Turn Moment: You stand with the echo of the vault door in your ears — the sealed hum of saved life — and realize that protecting possibility tonight has made you an agent of slow rescue and immediate exile. The town's pulse has shifted; there are embers where there was fire. You slide your hand into your pocket and feel the small hard shape of your buoy; it is warm from your skin, a solitary heartbeat against the cold. The rain keeps coming, insistent, as if it will wash all decisions clean. It won't. You whisper the ledger's last line to yourself — a vow, a note, a preparedness — and step away from the vault into the long night, carrying the weight of what you saved and what you left behind.]

    scene bg ch14_601bcb_8 at full_bg
    # play music "music_placeholder"  # [Music: Strings cut to a thin, sustained note that trembles without resolving]
    # play sound "sfx_placeholder"  # [Sound: Distant machinery, low and unstoppable; the soft, continual patter of rain]

    scene bg ch14_601bcb_9 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter25
    return
