label chapter6:

    # [Scene: Flooded Promenade | Dawn]

    scene bg ch6_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rope against timber; gulls shrieking distantly; the pad-thud of wet boots.]
    # play music "music_placeholder"  # [Music: Urgent percussion—staccato, rising]
    "You wake to the taste of salt and sawdust in your mouth. Your jacket is still damp from the rooftop garden's mist; your notebook is tucked against your ribs like a promise. Around you, a dozen"
    "neighbors move with a single, ragged choreography—hands on wood, shoulders under concrete fragments, faces set against the wind. You fit a salvaged beam under your arm and duck your head into the surf."
    "Elias 'Eli' Rowan is beside you before you know you needed him. He is early-morning rough and all hands: sand in his hair, sleeves rolled, the woven scarf damp. There is grease under his fingernails and a thin, hopeful smile tugging at one corner of his mouth even now."

    "Elias 'Eli' Rowan" "You okay?"
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "As okay as I can be."

    "Elias 'Eli' Rowan" "Good. Tie off that first splice like we practiced—remember? Under the eye, not around."
    "He kneels to your shoelaces and, with the practiced clumsiness that has always made you smile, ties a frayed knot into your improvised laces—an old rope he found last week. His fingers press a little too"
    "long against your ankle. Gray-blue eyes flick up, searching yours, and you see a flash of something—excitement tempered with fear."

    mara_kestrel "Don't mess with my boots."

    "Elias 'Eli' Rowan" "Never. Not if I can help it."
    "You breathe salt and diesel and the green smell of upturned seaweed. This is what you chose: hands-and-shoulders work, greed-free engineering, neighbor-built defenses. This is what you believed could buy nights of sleep for Grandma Hira's block and a child's school on dry ground."

    menu:
        "Rest for a minute":
            "You let your shoulders drop and press your forehead to cold timber, tasting iron. A neighbor—Rafi—calls a jocular, tired challenge and jerks you back into motion."
        "Keep pushing":
            "You lift the beam again, feeling the cramped burn in your forearms. Elias 'Eli' Rowan's hand finds your elbow and steadies you; his grip says 'we'll do this together'."

    # --- merge ---
    "The work continues; the dawn and the tide do not wait."
    # [Scene: Harbor | Midday]
    hide mara_kestrel

    scene bg ch6_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Cheers turn into shouted instructions; hammers clack; a distant engine idles.]
    # play music "music_placeholder"  # [Music: A swelling motif—hopeful strings layered over pulsing rhythm]
    "You work until the ache in your shoulders becomes a language you no longer need to translate. People chant, slap backs, pass sandwiches and thermoses. When the first heavy swell slides toward the pier, hits the"
    "new modular line, and sees its force bled into wood and geometry—there is a collective breath that turns into a cheer. For the first time since you returned to New Aster, the water seems to obey"
    "a human plan."

    "Neighbor" "Look at that! It actually—"
    show rafi_gmez at left:
        zoom 0.7

    rafi_gmez "—it held. For now."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "We did it."

    "Elias 'Eli' Rowan" "We did it together."

    "Elias 'Eli' Rowan" "Naomi said models would help. We proved small-scale works in the real world."

    mara_kestrel "Models and muscle."
    "You take out your notebook and make the first measurements: wave height reduced by inches, shore overtopping delayed by minutes. For a day, that archive of numbers is a talisman. People gather on the pier and"
    "drink hot tea from chipped tins; someone brings a radio and the station plays an old tune that smells like summer."

    menu:
        "Note the data now":
            "You bend to your notebook, careful hands making neat columns even as the sun warms your back. Recording the moment feels like making it real."
        "Stay and celebrate":
            "You stay with the cluster of neighbors, letting the warmth and the noise sink into your chest. Elias 'Eli' Rowan catches your gaze, and for a beat neither of you speak—there is no need."

    # --- merge ---
    "Whether you record the numbers or the laughter, the moment holds its meaning for a little while."
    # [Scene: Arbor / Community Phone Tree | Afternoon]
    hide rafi_gmez
    hide mara_kestrel

    scene bg ch6_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A frantic knock of incoming calls; the static of a council broadcast bleeding through a small speaker.]
    # play music "music_placeholder"  # [Music: Low rumble—underneath, an anxious motif]
    "The radio cutting the afternoon is a thin knife: Livia Chen's legal order is announced on the municipal stream. Emergency declaration. Immediate removal authority. You feel the sound like a cold hand at your spine."
    show tess_omalley at left:
        zoom 0.7

    tess_omalley "They served it online—Livia's pushing the emergency line. Says 'unauthorized coastal modifications'—they cite safety and liability."

    "Neighbor (woman)" "They're going to tear it down—now?"
    show rafi_gmez at right:
        zoom 0.7

    rafi_gmez "They'll say it's illegal and dangerous."

    "Elias 'Eli' Rowan" "They can't—after what we did, after—"
    show mara_kestrel at center:
        zoom 0.7

    mara_kestrel "They can, if the law says so."

    "Elias 'Eli' Rowan" "We started something that was honest. They choose their tools. We choose ours."

    mara_kestrel "We need to be smarter than the laws, Eli. Not just faster."

    tess_omalley "They're sending a crew tomorrow morning with a tow and a citation. Livia says it's a liability risk—' (Her voice collapses into a dry laugh.) '—and she’ll push for criminal enforcement if it’s resisted."

    "Elias 'Eli' Rowan" "We'll explain. We'll show the data. We'll—"

    mara_kestrel "Or they'll bulldoze it and call us vandals."
    "The room fractures into arguments—shouts, pleas, bargaining. People who cheered with you an hour ago now look at each other with a new, brittle uncertainty. You feel the first thread of dread: the town's support can be as fickle as the tide."

    menu:
        "Call Naomi to buffer the legal argument":
            "You grab your phone, fingers numb. Naomi's voice—practical and cold—lets you borrow the language of numbers; she agrees to preface notes for emergency filings."
        "Rally now—defend the structures tomorrow":
            "You find yourself standing, voice raised. Neighbors match your breath; a map of who will be where forms like storm clouds. The decision pulls tight around your ribs."

    # --- merge ---
    "Either path tightens the community around the immediate crisis; the morning will test whatever you prepare."
    # [Scene: Harbor / Pier | One Week Later — Night / Storm]
    hide tess_omalley
    hide rafi_gmez
    hide mara_kestrel

    scene bg ch6_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The roar is absolute—wind like a freight train; ropes snapping; a sudden, wrenching crack as something gives.]
    # play music "music_placeholder"  # [Music: All instruments reversed into discordant, high-frequency chaos—heartbeat-percussion over crashing brass]
    "You run with the rest because there is no other response you've trained for—no plan for being watched by catastrophic physical force. The storm is a mouth and it wants to swallow the pier whole. Your"
    "hands are raw, your breath ragged in the gale, and every instinct is a desperate, useless litany against physics."
    "A module lifts, turns, and slams against a neighbor's boat with a sound that is more bone than wood. The boat folds like a paper animal. A man you know by his laugh—Leo, who always repairs toys for kids down on Harbor Road—goes down, head snapping. Someone screams his name."

    "Neighbor (shouting)" "Leo!"
    # play sound "sfx_placeholder"  # [Sound: A crushing, wet rupture; then a smaller, pained cry—metal on wood, rope sliding through hands.]
    "A young volunteer—maybe sixteen—named Ana hauls a beam, her gloves polished with blisters. A rope under tension breaks; the beam recoils, and you see her leg twist in a way that is not meant to bend. She cries out, a sound that stops the world."
    "You move toward her like an automaton, fingers fumbling for first-aid in a pocket that seems suddenly too empty. Elias 'Eli' Rowan is beside you—his face is a ruin. He drops to his knees and tries"
    "to stem the bleeding with gloved hands while swearing under his breath, the words sharp and useless against the thunder."

    "Elias 'Eli' Rowan" "I miscalculated—"
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "We miscalculated together."

    "Elias 'Eli' Rowan" "No. I—"

    mara_kestrel "Ana—hold on."
    show rafi_gmez at right:
        zoom 0.7

    rafi_gmez "Get her to shelter!"
    "But the modules shift again. A line snaps; a stack of rope writhe and sink. The water takes the wreck of the boat, the garbage, and a part of the pier. You watch the neighbor who"
    "pulled the rope yesterday stumble backwards and hit his head on a jagged plank. Someone screams for an ambulance that will not come in these conditions quickly enough."
    # play sound "sfx_placeholder"  # [Sound: Sirens muffled by wind; the hollow ring of an empty tin can blown along broken boards.]
    # play music "music_placeholder"  # [Music: Climactic dissonance—every string is cut short]
    "Elias 'Eli' Rowan's hand finds yours through the chaos, his grip small and useless. He stares into your face with eyes that have nothing left to hide behind."

    "Elias 'Eli' Rowan" "I thought—if we just bought time, they'd have room to move."

    mara_kestrel "We thought we'd buy time—"

    "Elias 'Eli' Rowan" "I thought our modules would flex. I misread the load curves."
    "You look at Ana, pale and furious in pain, at Leo being carried on a tarp, at the neighbor's boat like a crushed animal. Love and intention crack open under the weight of underestimated forces and of legal power that comes down like a judge's hammer."
    # [Scene: Harbor / Pier | Dawn After the Storm]
    hide mara_kestrel
    hide rafi_gmez

    scene bg ch6_601bcb_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Conversations that are not talking—mutters, low accusations, the clink of a clipboard.]
    # play music "music_placeholder"  # [Music: A slow, devastating cello line—grief with no cadence]
    "The town convenes like an open wound. Livia Chen's emergency declaration is not abstract anymore—it is an instrument for clearing, for arresting what remains. Council staff wear the language of legality like armor; press cameras gather the images the town will have to live with."

    "Neighbor (old woman)" "They called this the right thing."
    show rafi_gmez at left:
        zoom 0.7

    rafi_gmez "There are no right things in a storm."
    "People split along a new seam. Some praise your courage—the sort of brave reckoning that will go into someone's headline: 'Locals Fight Back.' Others call you reckless, irresponsible, naive. They point to the crushed boats and"
    "the broken arm and the hospital band on Ana's wrist as proof that the improvisation was a crime against prudence."

    "Elias 'Eli' Rowan" "They'll say I promised too much."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "They'll say you promised everything."
    "He turns on you—half-anger, half-plea. The accusation is not loud, but its weight slams into you like a breaker."

    "Elias 'Eli' Rowan" "Why did you push to build now? Why didn't we wait to get Naomi to certify the plan? Why—"

    mara_kestrel "Because people were sleeping in wet houses! Because Grandma Hira's threshold was submerged last week—because waiting costs people their lives."
    "His face is hollow with guilt. He mutters, almost to himself, 'I miscalculated.' You hear not only his remorse but the fracture line forming between what you saved and what you cost."

    rafi_gmez "This town always has to choose between someone getting wet and someone making a plan for years. We chose action."
    "You feel your culpability as cold water down your spine—slow, inexorable, cleansing in a way you do not want. The love you feel for Elias 'Eli' Rowan—and the thing you had hoped to build together—suddenly feels"
    "like part of the ledger of mistakes. Intention doesn't hold when the world is this furious."
    # [Scene: Pier | Late Morning — Town Meeting Aftermath]
    hide rafi_gmez
    hide mara_kestrel

    scene bg ch6_601bcb_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Voices overlap into a wash—accusations, condolences, policy talk.]
    # play music "music_placeholder"  # [Music: Sparse piano hitting a single, merciless note]
    "You stand in the center because you always do—because people look to you for explanations and because you are still the scientist who knows, in numbers, what might yet be done. You open your mouth, and"
    "the voice that comes is not the steady, mobilizing tone you rehearsed months ago. It is raw."
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "We tried to buy time."

    mara_kestrel "We failed in ways I never wanted to even imagine."

    "Elias 'Eli' Rowan" "I'm sorry."
    "You stare at him. The town around you is worse off. There are fewer boats. There is a young life in a cast, and there are reputations fractured, and there are families who now have to sort through what courage and recklessness mean when both have real costs."
    "Grandma Hira approaches you slowly, shawl damp, eyes steady and old as tide-stones."
    show grandma_hira at right:
        zoom 0.7

    grandma_hira "You did what your heart told you."

    mara_kestrel "And what if my heart is not enough?"

    grandma_hira "Then you live with the ledger and pay it back with what you have left."
    "You look at Elias 'Eli' Rowan, and the look is long—full of accusation, and care, and the raw ache of two people who thought love could be an answer to a physics problem. He meets your"
    "gaze, and there is nothing theatrical anymore—only the mundane, brutal fact of two people holding the shards of what they built."

    "Elias 'Eli' Rowan" "I thought I could keep you safe."

    mara_kestrel "We were trying to keep people safe."
    "The town will go on—there is no cinematic resolution that mends all things. Buildings will be repaired, lawsuits filed, policy arguments had and re-had. People will either admire or condemn what happened today. The community's fabric"
    "has a new tear, and there is no neat stitch that can hide the rawness."
    "You fold your notebook closed. The ink of names and measurements seems suddenly like a poor currency against the cost of bone and wood and ruined boats."
    "You feel grief, sharp and hot; you feel responsibility, cold and heavy; you feel love, soft and vulnerable between the two. They do not balance. They sit in you like three stones on a scale that will never settle."
    hide mara_kestrel
    hide grandma_hira

    scene bg ch6_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: A single, sustained cello note hangs until it fades into silence]
    "You close your eyes and let the rain—cold, indifferent—wash the salt and the grit from your hair."

    scene bg ch6_601bcb_8 at full_bg
    "THE END"
    # [GAME END]
    return
