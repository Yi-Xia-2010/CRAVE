label chapter14:

    # [Scene: Reclaimed Wetlands Festival | Twilight → Night]

    scene bg ch12_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Upbeat community tune undercut by a taut, rising string motif]
    # play sound "sfx_placeholder"  # [Sound: Low murmur of the crowd, laughter, the slap of wet boots on planks; distant gulls calling]
    "You stand at the edge of the boardwalk, satchel heavy at your hip, breath gone thin with a kind of fever. The festival presses around you — the smell of smoked fish, lantern oil, and a"
    "wet wool scarf pressed against your neck. Kaori 'Kai' Matsuda is beside you, grin fixed and electric, fingers working the knots of the rigging as if they're the easiest problem in the world."
    show kaori_kai_matsuda at left:
        zoom 0.7

    kaori_kai_matsuda "Tonight is for the people. Story first — numbers later. Make them feel it, Marina. Make them want to save this place with their hands."
    "You want to remind her about the sensors, the tolerances, the signal delays. You also want to feel her certainty instead of the cold stone of doubt in your chest. You nod because she needs the yes; because the crowd needs a spectacle that can make bureaucracy feel human-sized."

    menu:
        "Double-check the tether one more time":
            "You step closer, fingers numb, and run them along the braided line — salt grit bites into your skin. Kaori 'Kai' Matsuda watches, annoyed but not unkind."
        "Let Kaori 'Kai' Matsuda finish; signal the launch":
            "You stand back. Kaori 'Kai' Matsuda's hands move like lightning. The raft shudders as volunteers push it free — applause rolls over you like surf."

    # --- merge ---
    "Continue"
    hide kaori_kai_matsuda

    scene bg ch12_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A swell of applause, someone starts a chant; the projector flickers to life and shows a looping animation of kelp long-lines cradling the shoreline]
    "You step forward when Kaori 'Kai' Matsuda does. Together you gestured toward the flats — not with engineering diagrams, but with the long, slow story of the sea breathing in and out, of children's futures, of"
    "Old Tom's maps folded into careful hands. The crowd leans in. The pilot is lowered; cameras tilt; Mika's drone hums its approval overhead like some blessed insect."
    "Elias Kato is at the edge of the light, hands shoved into a trench coat, jaw tight. He meets your eyes for a fraction of a second — something like hope, something like fear — and you answer with a small, stubborn smile that feels like a thin shield."

    menu:
        "Catch Elias' eye and give a small thumbs-up":
            "He doesn't return the thumb right away; his fingers close, then open. He looks like someone trying to steady a bridge."
        "Ignore him and face the crowd — this is your moment":
            "You turn to the people. All those faces, lit by lanterns, press into your throat like a demand: do it."

    # --- merge ---
    "Continue"
    # play music "music_placeholder"  # [Music: The strings swell; the crowd's cheer builds; the pilot raft glides away on the shallows, trailing hopeful banners]
    # play sound "sfx_placeholder"  # [Sound: A distant, sharp wind-note, like something warning]
    "Then the weather steps forward."
    "At first it's a movement at the edges of sound — a high, clean wind that pulls at the banners and knifes at the corners of lantern-glass. The kind of wind that makes the air taste"
    "metallic. Someone shouts about a storm on the weather app, someone else laughs and says the forecast was clear. The pilot bobs, steady. The projection keeps humming. You tell yourself small, practical things—check the sensors, tighten"
    "a cleat, recall the volunteers — and they sound thin against the roar that's building."
    # [Scene: Tidal Flats | Immediate]

    scene bg ch12_e67f19_3 at full_bg
    # play music "music_placeholder"  # [Music: Staccato percussion, rising to a sharp, chaotic tempo]
    # play sound "sfx_placeholder"  # [Sound: Wind ripping canvas; a howl that seems to come from the entire bay; a sudden, heavy rain]
    "The storm arrives without ceremony. Rain lashes the bulbs, turning the festival into a strobing, wet world. People shout over the wind; someone yells to secure the rigs. The pilot's tether arcs wrong. A buoy, slapped"
    "by a rogue gust and then a rogue current, tips and slams against a piling with a wet, splintering sound that pitches the raft. Lines that had seemed so carefully arranged twist like nettles; the long-line"
    "wraps once, then twice, around rusted metal and a slipping anchor."
    "Panic fractures the applause. Phones flash; someone screams a child's name. The drone’s feed stutters, then cuts to static. You run, boots sinking in the flattened mud, hands reaching for a rope that slides slick as"
    "a fish. The pilot drifts, half-submerged, its painted kelp face turned to the sky like a plea."
    show kaori_kai_matsuda at left:
        zoom 0.7

    kaori_kai_matsuda "Hold it! Hold it! Pull the—"
    "Her voice is swallowed. For a beat there is only the storm and the wet sound of a snapped line."
    # play sound "sfx_placeholder"  # [Sound: a sharp snapping, like a snapped ancient bone]
    "You feel the snap in your core. It's not just rope giving out; it's the breath of the room. The buoy spins, the long-line goes slack, and the pilot slides away, pulled by a current that"
    "wasn't on any of your maps. The projected animation blurs, then blacks out. The crowd's murmuring becomes a howl of accusation."
    hide kaori_kai_matsuda

    scene bg ch12_e67f19_4 at full_bg
    # play music "music_placeholder"  # [Music: All strings cut; a ringing silence falls for a heartbeat, then a low, accusing bass]
    show amalia_reyes at left:
        zoom 0.7

    amalia_reyes "People are freezing out here—Marina, what happened? We told you to wait for clear weather—"
    "You taste blood and salt. Your fingers are raw from the rope; the pendant at your collar bites cold into your sternum. You should have known the line-loading at high tide; you should have insisted on"
    "the redundant buoys; you should have stopped Kaori 'Kai' Matsuda when she pushed for spectacle. You hear your father's voice in memory, patient and small: careful, always careful."
    "Kaori 'Kai' Matsuda finds you first, grabbing both your shoulders so hard you see white at the edges of your vision."
    show kaori_kai_matsuda at right:
        zoom 0.7

    kaori_kai_matsuda "You wanted them to feel it. You wanted this to be about story. Look at what it did. Look."
    "Kaori 'Kai' Matsuda's accusation is a freight-train. Her face is wet with rain and she looks smaller, rawer, somehow un-hinged. She is not asking; she is naming a wound."
    show marina_reyes at center:
        zoom 0.7

    marina_reyes "It— I thought we could show them. I thought—"

    kaori_kai_matsuda "You thought you could win them with a moment. You didn't build for this, Marina. You built theatrics."
    "You try to answer; words tangle. Kaori 'Kai' Matsuda doesn't pause. She threads her anger into a sharp needlepoint aimed straight at you. The crowd hears it. Voices pick up the accusation like an echo."
    "Elias Kato moves between you and the crowd without meaning to. He is soaked through, hair plastered to his forehead. There is a new hardness in him — not quite anger, not quite defeat — that makes his amber eyes look almost brittle."
    hide amalia_reyes
    show elias_kato at left:
        zoom 0.7

    elias_kato "This was an experiment. They knew the risks. There are things to be learned—"

    "Townsperson" "Learned? My roof is still leaking from last month's high tide! We needed to protect our houses, not a show!"
    "Rina Corbett's voice comes through a megaphone — a municipal official who smells of institutional calm. Even under the rain, she keeps her sleeves rolled and her jaw set. You can hear the way she's already framing the scene, assembling the clean nouns that will justify machines."
    hide kaori_kai_matsuda
    show rina_corbett at right:
        zoom 0.7

    rina_corbett "We appreciate the initiative, but this demonstrates the need for professionally managed infrastructure. The council will accelerate the seawall project and request emergency approval for heavy machinery to reinforce vulnerable roads."
    "The words land like a verdict. Machinery. Seawalls. Emergency approval. The crowd, already raw, metabolizes that into fear about displacement; the small and fragile thing you and Kaori 'Kai' Matsuda were trying to grow is suddenly dwarfed by the promise of steel."
    # play music "music_placeholder"  # [Music: A single, dissonant chord reverberates; the festival's warmth scoured away]
    # play sound "sfx_placeholder"  # [Sound: Murmurs harden into demands; someone bargains loudly about compensation; a reporter's microphone thrusts forward]
    "Mika runs up to you, eyes wide, cheeks streaked with mud and mascara."
    hide marina_reyes
    show mika_tran at center:
        zoom 0.7

    mika_tran "We— we had the sensors...I put them on the line— I thought they would stream—"
    "You look at the drone-operator's tablet, a mess of frozen frames and error codes. The data you were so proud of is corrupted: timestamps split, telemetry missing. It is suddenly very easy for others to call you reckless, for municipal authorities to call you naive."
    "Old Tom stands under the edge of an awning, face like a worn map. He folds his hands as if gearing himself to say a truth."
    hide elias_kato
    show thomas_old_tom_bellamy at left:
        zoom 0.7

    thomas_old_tom_bellamy "The storm don't give notice to a pretty picture. I've been telling them that for years."
    "His words give a kind of permission to the crowd's anger. Fingers point. Names are said — responsibilities assigned with the brutal efficiency of grief."
    "Kaori 'Kai' Matsuda turns back to you, voice breaking now in a way that used to be reserved for children or for funerals."
    hide rina_corbett
    show kaori_kai_matsuda at right:
        zoom 0.7

    kaori_kai_matsuda "You had my backs, Marina. You promised they'd be seen. I believed you. This was never supposed to humiliate the team."
    hide mika_tran
    show marina_reyes at center:
        zoom 0.7

    marina_reyes "I thought— we could move them. People needed to feel this. I thought—"

    kaori_kai_matsuda "You thought. You thought."
    "There are no more quiet replies left between you. Accusations bloom like oil on water. The cooperative — your cooperative — is no longer a promise; it's the photograph of a failed promise that's already being printed with editorial headlines."
    hide thomas_old_tom_bellamy
    hide kaori_kai_matsuda
    hide marina_reyes

    scene bg ch12_e67f19_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The crowd's noise folds into the omnipresent small sound of a press pack deciding a narrative]
    "You can feel it: the fragile scaffolding of credibility cracking. Funding partners who showed tentative interest last week will call their advisors tomorrow. The council will parse this failure into reasons to favor heavy engineering and"
    "legal retreat zones. The story that began with hope is being rewritten as proof that community experiments can't scale — or worse, that they're dangerous."
    "Elias Kato is speaking to a reporter in clipped sentences that try to balance empathy and distance, but you hear the resignation under each one."
    show elias_kato at left:
        zoom 0.7

    elias_kato "We need to be pragmatic. The town needs infrastructure that can respond to sudden storm events. We have to consider managed retreat for the most at-risk parcels."
    "Every time he uses the phrase 'managed retreat,' you can feel neighbors flinch. The words sound like eviction notices."
    # [Scene: Reclaimed Wetlands Festival | Edge of Boardwalk | Moments Later]
    hide elias_kato

    scene bg ch12_e67f19_6 at full_bg
    # play music "music_placeholder"  # [Music: Nothing but the storm and a distant, keening note]
    # play sound "sfx_placeholder"  # [Sound: Footsteps moving away; someone softly sobbing under a tarpaulin]
    "You move from person to person like a shadow, trying to stitch things with talk — apologies, explanations, offers to convene meetings — but the stitches won't hold. People want concrete guarantees, not your raw apology."
    "They want roofs fixed, roads raised, permits signed. They do not want long-terms and experiments."
    "Amalia finds you then, dragging her clipboard like armor. Her face is streaked with rain and lipstick; her hands are shivering."
    show amalia_reyes at left:
        zoom 0.7

    amalia_reyes "They want numbers or they want machines, Mare. People are scared. They're calling the council now. They want something that won't fail. That was worse than showing nothing at all."
    "You open your mouth and the word that comes is a small, hot confession."
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "I thought story could move people. I thought—"

    amalia_reyes "People need to survive, not be moved into tears."
    "Her tone is not blame exactly; it's exhaustion. Her look will carve into you for a long time."

    menu:
        "Stand your ground and try to rally volunteers for damage control":
            "You shout over the wind, calling names, organizing a human chain. A few come running. Others turn away. Your voice feels like it's coming from under water."
        "Step back and let the council speak—avoid making it worse":
            "You let Rina's spokeswoman step up. Your silence is a wound. Volunteers you wanted to trust now look at you with the thinness of people who need a leader, not a spectacle."

    # --- merge ---
    "Continue"

    "The night fractures into small, savage decisions. Phones hiss with messages that will become a ledger of blame: sponsors withdrawing, a foundation putting its grant review on indefinite hold, a sympathetic journalist tweeting that community experiments risk the very things they try to save. You read one message from a funder" "This event undermines our risk assessment. We need guarantees before moving forward."
    "Kaori 'Kai' Matsuda pulls you aside one last time, voice wet and low."
    show kaori_kai_matsuda at center:
        zoom 0.7

    kaori_kai_matsuda "Don't try to fix this with more words. This wasn't about them. It was about you wanting applause. You can't make people trust a dream you stage. Trust is slow. You burned it."

    marina_reyes "I— I didn't mean to—"

    kaori_kai_matsuda "Meaning doesn't count. Outcomes do."
    "She walks away before you can reach for her, and the space she leaves is an emptiness that smells of ozone and wet wool. Elias Kato watches her leave with his hands in his pockets. For"
    "a moment his face is a map of regret, then he turns to help someone: a family whose dock pulled loose, a child clinging to a mother's hand. He does the tangible things. You see him"
    "make lists in his head, the kind that end in policy and permit numbers. He will do what he knows: repair, plan, file."
    hide amalia_reyes
    hide marina_reyes
    hide kaori_kai_matsuda

    scene bg ch12_e67f19_7 at full_bg
    # play music "music_placeholder"  # [Music: A single, minor piano note that takes too long to fade]
    # play sound "sfx_placeholder"  # [Sound: The storm moving offshore, leaving a wet, aching silence]
    "You stand on the boardwalk as the crowd disperses into the rain-wet streets. The pilot drifts away beyond the last pilings, a small, bright insult against the flat horizon. The cooperative's name is already being reshaped into a cautionary tale."
    "You are not hit by a single dramatic blow; the damage is smaller, multiplied: a grant deferred, a community meeting turned sour, an ally's quiet withdrawal. Funding dries like riverbed mud. The municipal voice grows louder in the spaces you had hoped to fill with kelp and people."
    "Your internal breath collapses into a small, heavy thought that settles cold under your ribs: you built a moment and it collapsed into proof of your failure. The community's trust — that thing you have carried"
    "like a buoy pendant close to your skin — has gone, at least for now, drifted like your pilot into a dark stretch of water."

    scene bg ch12_e67f19_8 at full_bg
    # play music "music_placeholder"  # [Music: A low, sustained bass; then cut]
    # play sound "sfx_placeholder"  # [Sound: Distant engines — the first heavy-machinery trucks, perhaps — a new rumble on the horizon]
    "You press your thumb against the frayed cord of the pendant. It is only leather and brass, but it is the last thing you have tonight that is not a headline."
    "Page-turn moment: You walk away from the flats under a sky gone flat and merciless. Each step pulls you farther from the bright story you tried to tell. Behind you, the council begins to prepare press"
    "releases, Kaori 'Kai' Matsuda's voice is a wound that won't close, and civil engineers will already be drawing lines that will redraw people's lives. You realize with a quiet, concrete grief that the cooperative is not"
    "only damaged — it is delegitimized in the eyes that matter. You can salvage technical data, you can beg, you can convene meetings until your voice is hoarse. But the narrative that now exists — that"
    "community experiments fail when the weather turns — will be hard, cold, and politically useful to the very machinery that pushes people away."

    scene bg ch12_e67f19_9 at full_bg
    # play music "music_placeholder"  # [Music: Long, single, unresolved low note]

    scene bg ch12_e67f19_10 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter26
    return
