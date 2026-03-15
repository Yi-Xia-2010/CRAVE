label chapter9:

    # [Scene: Marisol Bay Boardwalk | Morning — after the viral footage]

    scene bg ch6_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm, steady strings; a light rhythmic pattern underlies the scene]
    # play sound "sfx_placeholder"  # [Sound: Murmurs of a crowd, distant studio microphones clicking, the soft slap of waves against pilings]
    "You stand where the drone once had the best view of your face—salt and rain still clinging to your jacket, notebook tucked against your ribs like a small, faithful creature. The clip that went viral loops"
    "in your head: your voice, the line in the sand, the wind that made everything honest. The town has the taste of vindication. It is bittersweet, and you feel both."
    show amaya_reyes at left:
        zoom 0.7

    amaya_reyes "This morning we woke up with strangers' words in our mouths, but the choice is the same—what do we build next?"
    show jules_park at right:
        zoom 0.7

    jules_park "The reporter—Marta—she ran the records last night. Old procurement memos, revised impact assessments. Corinne's team had notes buried in footers that contradict public filings. It's clean. It's—"
    hide amaya_reyes
    hide jules_park

    scene bg ch6_601bcb_2 at full_bg
    show jules_park at left:
        zoom 0.7

    jules_park "—it's a garden we can point to."
    "You take that in. Jules's grin is bright enough to crack the clouds. You want to laugh and start planting stakes right where you stand."
    show mateo_reyes at right:
        zoom 0.7

    mateo_reyes "People are calling from the docks. Boats won't leave the harbor today if they know help's coming. Dockhands are bringing coffee to the volunteers. Abuela woke before dawn to stitch more seed packets."
    "You find Abuela Rosa by the railing, shawl clutched to her chest, watching the water like it's a living ledger. Her eyes are thin, and she hums something old and steady. The sound grounds you; it is a small ritual that says, we go on."
    # play sound "sfx_placeholder"  # [Sound: A cluster of polite, professional footsteps shifts the crowd's attention; camera shutters]
    hide jules_park
    hide mateo_reyes

    scene bg ch6_601bcb_3 at full_bg
    show tamsin_cho at left:
        zoom 0.7

    tamsin_cho "Amaya. We had pressure. From the council, from the county. With those records—my office can't in good conscience back full relocation. They want hearings; they want transparency. I'm recommending we pause and open formal mediation."
    "Your chest loosens a notch. Pause is an instrument you know how to play: longer than a breath, shorter than surrender. It gives you leverage."
    show corinne_voss at right:
        zoom 0.7

    corinne_voss "Marisol Bay is a priority to us. We maintain a commitment to safety and long-term viability. That said—"
    hide tamsin_cho
    hide corinne_voss

    scene bg ch6_601bcb_4 at full_bg
    show corinne_voss at left:
        zoom 0.7

    corinne_voss "—we will submit a revised footprint and fund restorative measures in consultation with the town."
    "There is a hush that isn't quite applause. It is the sound of a community holding its breath and deciding whether to exhale."

    menu:
        "Step forward and accept the microphones":
            "You walk into the soft cone of TV light. Your voice is rough but steady; you thank the volunteers and call for the council hearings to be open and public."
        "Let Luka speak first":
            "You step back and watch Luka climb the platform. He pulls his locket out for luck, clears his throat, and speaks about small-tech stewardship; his words are earnest, and the crowd listens."

    # --- merge ---
    "The narrative continues with Luka moving close to you and speaking quietly."
    show luka_maren at right:
        zoom 0.7

    luka_maren "You could have taken it all alone today."
    show amaya_reyes at center:
        zoom 0.7

    amaya_reyes "You know that isn't me."
    "Luka looks at you as if cataloguing small mercies—the chipped watch, the braid of seeds around your wrist. He presses his palm to your shoulder briefly; there is a quiet that says I am here."

    luka_maren "I could have taken the corporate route. I almost—"
    hide corinne_voss
    hide luka_maren
    hide amaya_reyes

    scene bg ch6_601bcb_5 at full_bg
    show luka_maren at left:
        zoom 0.7

    luka_maren "—but I don't want to be the reason we start losing people to promises."
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "I don't either. That's why we did this."
    "There is an unspooling between you—words you don't say and can't yet. He smiles, tired and honest, the kind of smile that has the shape of a decision already made."
    # [Scene: TideLab | Noon — the hub is busier than it's been in months]
    hide luka_maren
    hide amaya_reyes

    scene bg ch6_601bcb_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Spoons clinking in a thermos, low laughter, the steady beep of a pressure sensor being tested]
    # play music "music_placeholder"  # [Music: A small uptempo motif—lighter strings and plucked guitar]
    "Inside TideLab, the air smells of wet soil and solder. Jules is streaming a loop of the leaked documents on an old monitor—people crowd around, reading, nodding, and then, surprisingly, laughing and clapping in the modest way of those who have been owed truth for too long."
    show abuela_rosa at left:
        zoom 0.7

    abuela_rosa "We plant, and the earth answers. It doesn't ask for permission from big glass houses."
    show mateo_reyes at right:
        zoom 0.7

    mateo_reyes "You did good."
    "You cradle the packet between thumb and forefinger, thinking of the roofs and boats and the neighbor who keeps the cemetery ledger. Guilt softens, not gone—always present as a weather line on the horizon—but focused into something usable: repair."
    show jules_park at center:
        zoom 0.7

    jules_park "Also—national outlets want spokespeople for the hearings. Marta asked me if TideLab can present independent models."
    hide abuela_rosa
    show luka_maren at left:
        zoom 0.7

    luka_maren "We could scale community sensors. Co-manage them. We could make the aquaculture plans cooperative—community-owned floats. If we get funding from Voss, it's earmarked: TideLab oversight, local jobs, training."
    "You consider it. It's a trade, but the terms are different now. The company had to step back because people looked, and then the people found their footing."

    menu:
        "Accept Luka's plan with conditions":
            "You outline a list: community oversight, transparent auditing, profit-sharing with local fishers. Luka nods and pulls his multi-tool, already sketching modular designs in the air."
        "Ask for a pause to consult Abuela Rosa and Mateo":
            "You call a quick circle. Abuela's hands hover over the maps, and her single syllable—'Listen'—slows the room into thoughtful silence."

    # --- merge ---
    "Luka produces the silver locket containing the pressed kelp and touches it as the decision settles between you."
    "Luka reaches into his pocket and produces the silver locket containing the pressed kelp. He touches it as if grounding himself."

    luka_maren "I was going to say yes to a consultancy this fall. There was money that could've made those modules on a bigger scale. But—"
    hide mateo_reyes
    hide jules_park
    hide luka_maren

    scene bg ch6_601bcb_7 at full_bg
    show luka_maren at left:
        zoom 0.7

    luka_maren "—this feels like where the work should be."
    "You feel the decision settle in both of you. It is not dramatic; it fits like a repaired seam. He will not leave. You feel relief as a tangible thing, like a dry place in your chest you can rest on."
    # [Scene: Community Hall | Afternoon — public council hearing]
    hide luka_maren

    scene bg ch6_601bcb_8 at full_bg
    # play music "music_placeholder"  # [Music: A soft choir of strings underlines the speech rhythm; mid-tempo, patient]
    # play sound "sfx_placeholder"  # [Sound: The murmur of people, an official gavel tapping, microphones popping]
    "The hearing is procedural and intimate. Tamsin sits near the council, her face worn but resolute. Corinne stands to present Voss's revised plan. Cameras line the aisles. You are called to speak with a roster of citizens—farmers, fishers, students, elders. Each voice is a stitch."
    show corinne_voss at left:
        zoom 0.7

    corinne_voss "We did not anticipate the breadth of community concern that has arisen. In light of new information and the clear wish of Marisol Bay's residents, Voss Marine will propose a reduced structural footprint, targeted where infrastructure is most at risk. Additionally, we will commit funds to a distributed marsh restoration program and to establish a cooperative aquaculture fund managed by the community—audited and overseen with TideLab participation."
    "A ripple goes through the room. You look at Tamsin; she exhales, a small, relieved sound."
    show tamsin_cho at right:
        zoom 0.7

    tamsin_cho "Council will vote to accept the hearing schedule. We will form a joint oversight committee, including TideLab and community representatives."
    show abuela_rosa at center:
        zoom 0.7

    abuela_rosa "You held the line. But remember—repair is long work. Roots take time."
    "You answer with a smile that is mostly gratefulness and partly exhaustion."
    hide corinne_voss
    show amaya_reyes at left:
        zoom 0.7

    amaya_reyes "We asked for more time and for a seat at the table. That's what justice looks like in small places: the right to stay and shape the place you call home."
    "Corinne's posture is different now—less the sharp angle of an executive on a pier and more the weary set of someone who met resistance and found it costly. She meets your gaze for a beat."
    hide tamsin_cho
    show corinne_voss at right:
        zoom 0.7

    corinne_voss "This compromise is not perfect for Voss, but it is realistic. We will fund TideLab expansion in the form of a grant for equipment, training, and community aquaculture shares."
    "You hear people exhale and then, more quietly, begin to cry. Not all of them; not loudly. The sounds are a patchwork of relief and the residual coil of months of fear."
    hide abuela_rosa
    hide amaya_reyes
    hide corinne_voss

    scene bg ch6_601bcb_9 at full_bg
    # play music "music_placeholder"  # [Music: Swells a little—hopeful without triumphalism]
    show luka_maren at left:
        zoom 0.7

    luka_maren "Co-lead, Amaya? TideLab and all that it could be."
    "You weigh the word—co-lead—heavy and bright. It means partnership outward and inward: splitting burdens, sharing choices, being accountable not only to the town but to each other."
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "Yes. We'll do it together."
    "He squeezes your hand, not theatrically, but as if confirming a mutual pact. Around you the hall buzzes with plans: marsh beds to restore, modular floats to prototype, training sessions for fisheries co-ops. Abuela Rosa hums and begins folding seed packets with practiced fingers, passing them like benedictions."
    show mateo_reyes at center:
        zoom 0.7

    mateo_reyes "We'll need more hands and more boots. And coffee."
    hide luka_maren
    show jules_park at left:
        zoom 0.7

    jules_park "And I have Marta drafting an op-ed on the audits. Transparency will be our backbone."
    "You feel the weight of guilt—small, stubborn—like a pebble in your shoe. You know the chaos that stretched short-term resources and bruised people. You do not erase those nights. But the guilt sharpens into care; it becomes the map you use to avoid future harm."

    amaya_reyes "We won a space to fight for our town on our terms. And we will use it."
    hide amaya_reyes
    show corinne_voss at right:
        zoom 0.7

    corinne_voss "We will also commit to long-term monitoring; Voss will fund independent reviewers for five years. If the community's measures exceed our expectations, we will collaborate further. If not—"
    hide mateo_reyes
    hide jules_park
    hide corinne_voss

    scene bg ch6_601bcb_10 at full_bg
    show corinne_voss at left:
        zoom 0.7

    corinne_voss "—we adjust."
    "The word 'collaborate' hangs between you like a plank you both need to walk. It is imperfect, but cooperative. It contains hands instead of bulldozers."
    # play sound "sfx_placeholder"  # [Sound: Gentle applause, the rustle of paper, the distant gulls]
    hide corinne_voss

    scene bg ch6_601bcb_11 at full_bg
    # play music "music_placeholder"  # [Music: Resolves into a warm, contemplative chord—mid arousal, steady triumph]
    "You step outside onto the boardwalk as people filter out. The bay looks like a promise in muted color. Luka loosens his grip on your hand and turns to the crowd with you beside him."
    show luka_maren at left:
        zoom 0.7

    luka_maren "This is our work. We will plant. We will build small things that make room for big lives. TideLab will train, employ, and be accountable. We will own a share of what we make."
    "A cheer rises—not thunderous, but whole. It is the sound of people choosing to stay and to keep building."
    show abuela_rosa at right:
        zoom 0.7

    abuela_rosa "Remember, even when the storms come, roots keep their memory."
    "You clasp the child's small, soil-marked hand and feel, for a moment, the future as something you can reach into and mend."
    # [Scene: TideLab — Sunset]
    hide luka_maren
    hide abuela_rosa

    scene bg ch6_601bcb_12 at full_bg
    # play music "music_placeholder"  # [Music: Soft piano and string duet; calm, optimistic]

    "You stand with Luka and Mateo as the last of the sun slides down. The boardwalk behind you is patched with signs that read" "Marisol Bay: Restored, Resilient."
    "You think of every person who showed up—the ones who stitched banners and the ones who spoke with trembling voices. You think of the nights you held maps and the mornings you planted seeds. The victory is not clean and it is not total, but it is real."
    show luka_maren at left:
        zoom 0.7

    luka_maren "Thank you—for trusting me, for standing. Let's make TideLab something that can't be bought."
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "We will make it a place people can run to, not away from."
    "He leans forward and kisses you—quick, plain, and steadier than the weather. It is not a seal on a fairy tale; it is a pact: to stay and to share the labor of keeping a place alive."
    # play music "music_placeholder"  # [Music: Gentle diminuendo; the strings linger and then hush]
    # play sound "sfx_placeholder"  # [Sound: Waves breathing; the low chatter of people folding in on themselves like a community]
    "You look at the seedlings, at the new benches, at the cooperative registration forms stacked on a salvaged crate. You feel relief as a current under your ribs—cautious, practical, and buoyant."
    show abuela_rosa at center:
        zoom 0.7

    abuela_rosa "We will be all right. Now, we learn the long work."
    "You nod. The long work is no longer only a weight; it is also a promise to the people who refused to be erased."
    hide luka_maren
    hide amaya_reyes
    hide abuela_rosa

    scene bg ch6_601bcb_13 at full_bg
    # play music "music_placeholder"  # [Music: A single held, warm chord; then fade]

    scene bg ch6_601bcb_14 at full_bg
    "THE END"
    # [GAME END]
    return
