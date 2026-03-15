label chapter8:

    # [Scene: Seawall | Morning — after the storm]

    scene bg ch8_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind still hunting the edges of the concrete. Far-off gulls call like accusations. Somewhere behind the wall, water licks and swallows the shoreline in soft, relentless rhythms.]
    # play music "music_placeholder"  # [Music: A minor piano motif underscored by a slow cello — somber, unresolved]
    "You stand with your palms pressed against cold concrete, feeling the faint vibrations of waves that did not spare anything they reached. The morning air smells of iron and rot—salt mixed with something warmer and wrong."
    "It takes a second to name it: decomposing marsh grass, the low, sour fruit of drowned root systems."
    "In the few days since the ribbon-cutting, weather that a week ago would have been a headline has broken like a promise across the bay. The seawall holds, technically. The town has something to point to,"
    "something vertical and costly and visible. But beyond the concrete fringe the marsh—your marsh—has gone quiet in a way that makes your chest ache. The reed beds, which last season hummed with wrens and the odd"
    "lanternfish that came in with the tides, now sprawl like clotted hair. Mud is scoured into channels; the usual sponge of sediment that fed young cordgrass is missing."
    show elena_lena_maris at left:
        zoom 0.7

    elena_lena_maris "You wanted certainty and you bargained for protection. You forgot to ask whether the ocean would forgive the interruption."
    hide elena_lena_maris

    scene bg ch8_6b08b4_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Her breath in the wind, the soft slap of a sample jar closing]
    # play music "music_placeholder"  # [Music: A single dissonant violin note]
    show dr_asha_khatri at left:
        zoom 0.7

    dr_asha_khatri "This isn't just storm mortality. Look at the sediment profiles—there's been an abrupt drop in accretion. The wall trapped the flow differently. The tides that used to deposit silt on the marsh plane are turning elsewhere."
    "You move closer. Her face is set in the way scientists get when data becomes indictment."
    show elena_lena_maris at right:
        zoom 0.7

    elena_lena_maris "Didn't the modeling account for this? We had environmental clauses. There were—"
    "Dr. Asha Khatri: (cutting in) 'Models are simplifications, Lena. We accounted for currents at baseline. We did not—and could not—predict this magnitude of storm-surge redistribution combined with the wall's hard reflection effects. That reflective energy is"
    "scouring the channel edges. The marsh is being starved, not drowned, and when you starve an ecosystem it can collapse faster than you can plant a willow.'"
    "You taste a flash of hot shame. The wall was supposed to buy the town time. Time is now a ledger being balanced against the lives that lean on that marsh: crabs, nurseries, the shoals that"
    "fed families. The math that convinced councilmen and investors looks cruel in mud and broken reed."

    dr_asha_khatri "We can attempt sediment augmentation and engineered breaches—small, targeted interventions—but they'd need funding and permission immediately. Otherwise, what you see will spread."

    elena_lena_maris "Immediate. Permission. Funding. The three words that feel like someone else's world when people on my street withdraw their savings."

    menu:
        "Wade into the marsh to inspect the roots up close":
            "You shove your boots into the soft mud and let the cold suck at your calves. Up close, the roots are papery. You scoop a clump free and hold it like an accusation. The salt crystallizes on your jacket and the sample trembles in your hands."
        "Stay on the seawall and record samples from above":
            "You stay on the concrete, cameraing and tabling notes. From here you can bracket the damage and preserve your composure; you make lists and a careful voice. It steadies you, but someone later will tell you that distance looked like aloofness."

    # --- merge ---
    "The scene continues as the party moves into town."
    # [Scene: Town Streets | Midday]
    hide dr_asha_khatri
    hide elena_lena_maris

    scene bg ch8_6b08b4_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Chants—some rhythmic, some raw. A megaphone snaps with a voice: "WHOSE SHORE? OUR SHORE!" Cars inch past, and a radio in a truck plays a news anchor's clipped voice in the background.]
    # play music "music_placeholder"  # [Music: Low percussion, the heartbeat of protest; distant, mournful harmonics]
    "Rosa 'Rosie' Alvarez appears as if from the crowd—paint-stained bandana tied freshly, hands smeared with something that smells like coffee and old varnish. The co-op has become a nexus for anger and logistics: sandwiches, flyers, a list of displaced workers. Her smile is tight when it finds you."
    show rosa_rosie_alvarez at left:
        zoom 0.7

    rosa_rosie_alvarez "Lena. You okay? People want answers. They're asking why you stood there at the ribbon with Iris. Marco's at the front—he's not pulling punches."
    "Before you can answer, Marco rounds a corner, face sun-creased and taut. He carries a sign but it isn't the paper sentiment—it's the look he's been wearing since dawn: raw, wounded."
    "Marco Maris: (shouting before he reaches you) 'You sold us out! You hugged Valence and handed them our tide!'"
    show elena_lena_maris at right:
        zoom 0.7

    elena_lena_maris "Marco—"
    show marco_maris at center:
        zoom 0.7

    marco_maris "No. Don't 'Marco—' me. You were at the ceremony. You cut the ribbon. People are losing work because boats can't dock where the sediment shifted. The bait shacks are flooded in a new pattern. People have had to close shifts because the fish aren't coming in the same spots. This is your doing!"
    "You feel the words like weight thrown into the middle of you. He is right in the rawest way—your public presence at the ribbon is a ledger entry in people's personal losses."

    elena_lena_maris "You wanted to be in the room where decisions were made. Now the room spills into the street and the cost reads like a bill they want you to pay."
    "Rosa 'Rosie' Alvarez: (softly, grabbing Marco's arm) 'He was trying to help. He thought—'"

    marco_maris "Thought what? That a wall made at a tower would suddenly care about the Maris family frontage?"

    elena_lena_maris "I didn't sign it off alone. I negotiated language—"
    "Marco Maris: (interrupting, bitter) 'Negotiated. You signed a picture with the woman whose firm wrote the check. How's that different for us?'"
    "You open your mouth and the sound that comes is smaller than the demand. There's no single conversation that can undo the visible consequences, no clause that folds grief back into neat paper. Yet you must speak, and your voice quavers."

    elena_lena_maris "I hear you. I hear the hurt. I'm not here to justify what happened—I'm here to fix it."

    marco_maris "Then fix it, Lena. Or step aside."

    menu:
        "Step toward Marco and put a hand on his shoulder":
            "You close the distance. His jaw tightens, but he doesn't pull away. The crowd's noise reduces for a sliver; you feel the simple, human geography of being there. It buys you a moment of trust you might need."
        "Stand your ground and outline the remediation steps aloud":
            "You take out your phone, voice steady, and begin listing measures: sampling, emergency grants, marsh breaching. The crowd listens for a while, measuring whether your words are policy or platitude. Some nod; others scoff. The distance feels like a ledger again."

    # --- merge ---
    "The scene continues toward the meeting at the tower."
    # [Scene: Valence Urbanworks Tower | Afternoon]
    hide rosa_rosie_alvarez
    hide elena_lena_maris
    hide marco_maris

    scene bg ch8_6b08b4_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Elevator hum, polite footsteps on marble, a distant chime. Outside the tower, a protester's chant filters through the glass like a foreign language.]
    # play music "music_placeholder"  # [Music: High, thin synth notes—calm but insistent]
    "Iris Valence meets you in a conference room glassed toward the bay. Her hair is neat, her cuff flicks through air with precise gestures. The look she gives you is complicated—apology pressed under a strategy, intimacy"
    "under a ledger. You have seen it before: years ago, in classrooms and late-night plans; this is the same efficiency shaped into policy."
    show iris_valence at left:
        zoom 0.7

    iris_valence "Lena. The press is circling. We can control the narrative if we act now. We put protections in place—"
    show elena_lena_maris at right:
        zoom 0.7

    elena_lena_maris "We put a wall in place. But Asha says the marsh is starved. The fishermen are losing ground. We didn't forestall these feedbacks."
    "Iris Valence: (leaning forward, voice even) 'No human system is perfect. We can add mitigations—sediment injections, managed breaches, targeted living shorelines in places the wall misses. We must show the town we're responsive. Show them the money behind the fixes.'"
    "Iris Valence: (a beat) 'But the alternative is chaos. You know how quickly political momentum turns. If you step away publicly now—'"

    elena_lena_maris "If I stand with you, I'm asking people to trust me in a way they already feel I've broken."

    iris_valence "You stood with me at the ribbon because you believed the plan could be made better from inside. Stay inside—help me shape the amendments. If you do, we can rewrite parts of the contract: binding environmental performance metrics, independent audits, community oversight seats."
    "There's a pleading layer under the corporate clarity; your history threads through it, making her terms feel like both an offer and an appeal to a past you once shared. You remember nights when both of"
    "you sketched coastlines on the same napkin and vowed not to let pragmatism swallow people whole. Now the napkin is a filing cabinet."

    elena_lena_maris "Keep the power and try to bend it, or walk away and keep your hands clean? Power is useful. Power is also what hurt the marsh."

    iris_valence "Say yes, Lena. Be at the press conference. We'll announce an emergency fund, and I'll personally authorize the environmental panel. Let the town see you fight for them—within the apparatus."
    "You feel the weight of cameras that will interpret every facial micro-expression as complicity or courage. You imagine Marco's face when he watches you on-screen."
    "Iris Valence: (softening) 'I know I owe you an explanation beyond corporate memos. I'll give you space to shape the language. But I need you there.'"

    elena_lena_maris "And if the audits don't change policy fast enough? If the sediment doesn't come back? People need action that isn't just fiscal theater."

    iris_valence "Then we move faster. We make the fixes immediate. We publish audits weekly. We open our data."
    "She watches you like someone counting the beats between your words."
    # [Scene: The Pier | Dusk]
    hide iris_valence
    hide elena_lena_maris

    scene bg ch8_6b08b4_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Close, intimate wind; the low squeak of mooring ropes; Jonah's footsteps on wet wood.]
    # play music "music_placeholder"  # [Music: Sparse guitar — warm but shaded]
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "You got Asha's samples?"
    show elena_lena_maris at right:
        zoom 0.7

    elena_lena_maris "She thinks the wall changed sediment patterns. She thinks it's starving the marsh."
    "Jonah Reyes: (exhale) 'We suspected displacement effects, but not like this. This fast.'"
    "Jonah studies the marshline, then turns to you. There's pleading and hard pragmatism in his amber-green eyes."

    jonah_reyes "People are losing income. The bait houses that front on those channels—Rosie's cousin—he closed two nights ago. Marco's right to be furious. I am too. I backed you when you went to the tower, because I thought we could keep the town in the room. I thought—"
    "He stops. Words gather like driftwood."

    jonah_reyes "We could do what Asha said—sediment augmentation and targeted restoration—but it needs boots, coordination, and money. We could pull volunteers, but that's not the same as grants. We could push for an emergency hybrid retrofit—force Valence to fund quick fixes while we put living-shoreline teams on the water. Or you could stand with Iris and try to steer the firm from inside. Or you could walk. All three are ugly in different ways."

    elena_lena_maris "And the risk?"

    jonah_reyes "Standing with Iris: you keep resources and fast approvals but you might lose the trust that lets people work with you on the ground. Resigning: you have street cred but you lose access to large funds and the legal bite to bind Valence. Forcing a hybrid retrofit: it's a technical bandaid that might placate enough people, but it might also be the middle ground that satisfies no one long-term."
    "You look at Jonah. In his hand he fiddles with the dented wrench on his belt—an object that has fixed more things with sweat than any meeting has with memos."

    jonah_reyes "I trust you either way, but I think the town trusts you more if they see you choose the people—that you don't pick tower optics over them."

    elena_lena_maris "Trust is currency. Institution is leverage. The marsh is time. I'm balancing a ledger I didn't entirely create, and every weight shifts someone else's life."
    # play sound "sfx_placeholder"  # [Sound: A distant chant—growing, angrier—threads up from the town, a reminder.]

    "Dr. Asha Khatri (arriving at the pier, breathless)" "There's a window before the next high tide and the storm surge cycle. Sediment injection points would need to be scheduled now. If we can coordinate barges and volunteers, we could shore up the worst of it. But funding has to move immediately, Lena."

    "Iris Valence (via call, voice calm through line)" "We can allocate emergency funds, but public assurance matters. We need a spokesperson—your face in the room. Lena, we need you to stand publicly with me, accept responsibility, and negotiate stronger environmental safeguards. It will make the legal path smoother."
    "Jonah's jaw tightens. Marco's voice from the street calls your name like a summons."

    elena_lena_maris "The choices are laid out not as clean beacons, but as worn pathways into different kinds of loss. Each will cut something out of the town's fabric."
    hide jonah_reyes
    hide elena_lena_maris

    scene bg ch8_6b08b4_6 at full_bg
    # play music "music_placeholder"  # [Music: The cello returns, lower, darker; a single held note that refuses resolution]
    "You stand at the seam of public responsibility and private allegiance, the town's breath waiting like a held chord. Voices pull at you from every direction—Marco’s fury, Rosie’s organizing, Asha’s maps, Jonah’s tethered hope, Iris’s measured pragmatism. Each claim is true; each claim pulls toward different futures."
    "Build tension, then stop at the choice—do not resolve yet."

    menu:
        "Stand publicly with Iris, accept responsibility, and negotiate stronger environmental safeguards.":
            jump chapter9
        "Resign from the partnership and return to grassroots organizing with Jonah.":
            jump chapter14
        "Force an emergency hybrid retrofit—partial marsh restoration and targeted seawall modifications.":
            jump chapter15
    return
