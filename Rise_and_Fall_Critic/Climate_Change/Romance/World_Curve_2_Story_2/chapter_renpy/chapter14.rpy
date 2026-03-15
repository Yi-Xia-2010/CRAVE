label chapter14:

    # [Scene: Harborfall Promenade | Dusk]

    scene bg ch14_77cd71_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, a low machine hum from temporary pumps, the intermittent drip of tarps]
    # play music "music_placeholder"  # [Music: Sparse cello and low piano, a descending motif]
    "You stand where the promenade bends toward the mouth of the cove, toes balanced on tide-lines scoured into the wood. The horizon is a flat smear; the water has eaten a notch where the eelgrass used"
    "to hold its shape. Salt crusts your jacket cuffs. Your brother’s dive watch—cold against your wrist, its hands frozen on a time that will never come back—catches the last light, a small, precise relic of a"
    "life that should have been longer."
    "The referendum passed. The town has money and a map of clauses, and yet the map already feels like paper caught at the edge of a storm: it folds, it tears, it blows away. You can"
    "see the consequences braided into the shore itself—raised foundations like islands, a house here sinking on one side, a strip of new water where the cove once curved. Somewhere out of sight, seedlings that never took"
    "have been yanked free; near the eelgrass bed, heavy rock placements have scoured mud like an angry hand."
    "You breathe in. The brine smells of iron and old diesel. You taste apology and sand."
    # [Scene: Town Hall Annex / Mayor's Interim Office | Early Evening]

    scene bg ch14_77cd71_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmured councilors, a printer's last tired cough]
    # play music "music_placeholder"  # [Music: Minor strings, steadying heartbeat rhythm]
    show mayor_elena_rossi at left:
        zoom 0.7

    mayor_elena_rossi "We've secured the emergency relocation fund. It's… not everything. It won't cover full buyouts or every elevation. But it will—' (she searches for the word) '—shore up what we can and give people options."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "Options,' you say. Your voice is even because you've practiced this. 'Priority should be elderly households, critical infrastructure, and then—then we need transparency about subcontractors. No more unilateral placements."

    mayor_elena_rossi "Transparency. We've asked for audits. I've called the regional office. But funds will be rationed. There will be people we can't cover."
    "A silence settles that has weight. Not all losses fit into budget lines."

    maya_inoue "Then we make sure the people we can't cover can leave with dignity. Relocation centers, help with paperwork, storage for belongings. We can't let 'can't cover everyone' become an erasing."

    mayor_elena_rossi "We'll do what we can, Maya. We will. I promise the town won't be left to rot."
    "You want to press for more—investigations, legal holds, a public list of who decided what and when—but the room is full of weary faces, and promises sometimes have to be the concrete we pour into a crack to keep it from widening."

    menu:
        "Read the audit list aloud now":
            "You flip through the binder and start to read names—contractors, dates, placement orders. The room listens like a chorus holding its breath. Mayor Elena takes notes. Tomas shifts in his chair. The list anchors issue to person, but it also sharpens fear in several faces."
        "Hold the list back and speak to the people first":
            "You close the binder gently and stand. Outside, the town waits. You choose to let people tell you what they need in the raw before you hand them pages and clauses. The room swells with murmured approvals and a few worried frowns—the choice is about where resistance begins: evidence or empathy."

    # --- merge ---
    "Continue to next scene"
    # [Scene: Hana's Diner | Night]
    hide mayor_elena_rossi
    hide maya_inoue

    scene bg ch14_77cd71_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Silverware, a tea kettle's last whistle, quieter conversations than before]
    # [Smell: Chicken soup, coffee, a faint bleach-sweet of sanitizer]
    # play music "music_placeholder"  # [Music: A low, intimate guitar line]
    show hana_kim at left:
        zoom 0.7

    hana_kim "You look like the lighthouse—blown inside.' (She sets a bowl down in front of you; steam fogs your glasses.) 'Eat. You never do."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "I keep rehearsing apologies in my sleep,' you admit. 'To people who lost houses. To Tomas. To—' (you swallow) '—to Kaito. I'm sorry and it feels like saying it doesn't do anything but make me smaller."

    hana_kim "Apologies are for the heart. Plans are for the hands. You do both—don't let either one tell you they cover the other.' (She reaches out, blunt and human.) 'People need you to be here, even when you're tired of the sound of your own promises."
    "You look at the bowl and at Hana, at the quiet of the diner. Her smile is worn but steady. It's both comfort and a rebuke."

    hana_kim "And if you're going to keep apologizing, at least do it after people have eaten."
    "You smile because it's absurd to faintly laugh when everything is breaking. It helps, a little."
    # [Scene: Mangrove Estuary / Eelgrass Beds | Low Tide]
    hide hana_kim
    hide maya_inoue

    scene bg ch14_77cd71_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The husk of water moving, small fish flicking in shallow pools, boots on wet wood]
    # [Smell: Hydrogen sulfide under the brine, the green iron of algae]
    # play music "music_placeholder"  # [Music: A solitary violin, slow and hollow]
    show tomas_bianchi at left:
        zoom 0.7

    tomas_bianchi "We planted. We raised. We argued and sang. And still the water took. Not because people didn't try, but because the way it moves changed.' (He plucks a bit of sod and lets it fall between his fingers.) 'Sometimes saving a place means leaving it, Maya."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "Sometimes saving it means staying and doing the small impossible things. I keep thinking—if we'd had more time, if I'd pushed the council harder—"
    "Tomas [gentle gruffness]: (cuts you off) 'You led. You moved people who were frozen. We all did our part. The sea doesn't owe us outcomes. But it listens to hard work and stubbornness. So do people.'"
    "You watch him in the late light. The truth sits between you like a boat moored in a storm: the work you did mattered, and still things were taken. Both are true."

    menu:
        "Help Tomas untangle a net":
            "You kneel in the mud and your knees find the cold. The net is a tangle of old and new—history and hazard. Hand by hand, you and Tomas sort it. It feels like a small ritual of repair."
        "Walk the edge and count the losses quietly":
            "You walk the estuary's edge, counting hollow docks and ragged seawalls. The list becomes a litany you whisper into your coat. It steadies you differently—like naming helps measure what you must try to mend next."

    # --- merge ---
    "Continue to next scene"
    # [Scene: Kaito's Field Lab (Workshop) | Night, Later]
    hide tomas_bianchi
    hide maya_inoue

    scene bg ch14_77cd71_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The click of a camera, a slower rhythm of someone recording; the distant thump of generators]
    # play music "music_placeholder"  # [Music: Low electronic hums under a pained cello]
    show kaito_sato at left:
        zoom 0.7

    kaito_sato "You had people behind you at the referendum. You did what you thought would keep the town in local hands. I argued the opposite, I—' (he stops, searching for the right shape to put regret into) '—I thought leverage could be used differently."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "Did you think I was naive?"

    kaito_sato "Sometimes. Not in the way you hope. I thought we could stitch the community to the technical fix and make something that would hold. Instead, in places, the stitches frayed. I have my share of blame."

    maya_inoue "You left."

    kaito_sato "I left to try to help others. There's a conference — regional towns are calling. I can help them avoid what happened here.' (He folds his hands.) 'I don't think I can save Harborfall from where I am if I'm always at your shoulder. Maybe I should have stayed. Maybe I should have fought harder, not for my sensors but for how they were used. I don't have a tidy answer."
    "The two of you argue then—slowly, then more sharply. Not the shouting of enemies, but the sharpness of two people who loved one another enough to be honest even when honesty hurts."

    maya_inoue "Did you ever think my reluctance was cowardice? Or that I didn't see the utility of contact with donors?"

    kaito_sato "I thought your loyalty would be a bridge we could walk together. I didn't expect the referendum to tie our hands the way it did. I didn't expect that the compromises would be the ones that sank other things.' (He looks at you like a man showing you a wound he cannot fix.) 'I needed to be honest with you, Maya. I can't keep trying to hold everything for every town and for us at the same time."

    maya_inoue "So you're leaving."

    kaito_sato "For now. To help others. To make sure they have tools that don't become blunt instruments. I'm sorry—' (he reaches for you and then withdraws) '—for what I couldn't do here."
    "You: The lab light pools between you. You think of the sensor networks, the nights of solder and laughter, of the way he taught you to read data like weather—like language. Then you think of the holes—people who needed more than sensors, people who needed more than promises."

    kaito_sato "I want you to keep leading here. In the ways only you can. I'll be working from a distance. It doesn't mean I love this place less."

    maya_inoue "It doesn't mean I love you less either.' (The admission slips out; you both wince as if at a truth that might undo you.) 'But love doesn't fix everything."
    "He does not stay to reconcile. He packs a small satchel, straps the camera, leaves you standing in the white light with the door trailing rain. The lab door clicks shut like a punctuation."
    # [Scene: Storm-broken Lighthouse | Midnight]
    hide kaito_sato
    hide maya_inoue

    scene bg ch14_77cd71_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind that sounds like a voice, the persistent slap of water on stone]
    # [Smell: Wet rope, seaweed, the stale tang of old lightning]
    # play music "music_placeholder"  # [Music: Low chorus, long, minor]
    "You climb the lighthouse path because it has always been where decisions gather their weight. The wind tugs at your braid; the teal streak stands up like a small flag of endurance. Below, Harborfall sleeps fitfully—lights"
    "blinked out, tarps flapping in the wind, the diner shuttered for the night. Tomas's house is a dark silhouette. Hana's window shows a single light, the diner broom standing like a sentry."
    "You stand at the lamp and let the wind take your breath. Your brother's watch is cold against your skin, stopped on a time you'll never reach. You press it and listen to your own pulse."
    "The ledger of losses scrolls through your mind: seedlings, eelgrass, a cove that won't be the same, families who left with boxes and bowed backs, a quay raised and another house left to sag."
    show maya_inoue at left:
        zoom 0.7

    maya_inoue "We measured everything. We measured shoreline, storm frequency, loaned funds, volunteer hours. We put numbers to loss and still the thing we wanted to save is not whole."
    "A gust throws salt across the scaffold. The lamp sputters. You don't feel triumphant. You don't feel defeated in the simplistic sense—it's a complicated tiredness, a grieving that is not singular but communal."
    "You think of the referendum—about keeping decisions local—and how that pride sits next to the sight of places that were not protected. You think of the hybrid placements that disturbed what little eelgrass remained and of"
    "the mangrove seedlings that never rooted. Both strategies were attempts to do right; both cost something essential. Both were chosen with love for the town. Both failed in parts."
    "Tomas's voice from earlier comes back to you, grainy and true: sometimes saving a place means leaving it. You do not agree entirely, but you let it rest in you."
    # [Scene: Lighthouse Top | Same Night]
    hide maya_inoue

    scene bg ch14_77cd71_7 at full_bg
    # play music "music_placeholder"  # [Music: A single cello note, then silence]
    "Maya Inoue: You fold your hands around the stopped watch and make a decision that is not a neat victory. You will keep measuring, because data saves people and because it prevents the lies we tell"
    "ourselves about what we can change. You will press for audits and for dignity in relocation, for funds to repair what can be repaired and for ceremonies for what cannot. You will teach others what you've"
    "learned and you will allow grief its long, ragged apprenticeship."
    "You will do this without the arrogant certainty that one method or one person will save everything. That humility is a wound and a way forward."
    "You close your eyes and, for a moment, allow the grief to come fully—not as a thing to be fixed but as a proof that the town mattered enough to hurt for. In that acceptance there"
    "is a strange kind of steadiness: a clarity about what you will fight for and what you must mourn."
    "You think of Kaito's retreat to help other towns, of Hana's steady hands, of Tomas sorting nets, of Mayor Elena trying to keep everyone afloat. You imagine them in the morning—some returning, some gone—and you imagine"
    "the town remade in ways you would not have chosen but will learn to live in. There will be new songs and new absences. There will be small victories and new losses."
    show maya_inoue at left:
        zoom 0.7

    maya_inoue "We did what we could. We'll do more tomorrow."
    hide maya_inoue

    scene bg ch14_77cd71_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rain on the metal scaffold, like a muted applause]
    # play music "music_placeholder"  # [Music: Cello holds a low, sustaining note that bruises then settles]
    "The lighthouse beam swings once and finds the dark water. It does not promise safety. It promises to keep a light burning for those who choose to come back and for those who cannot. You let the promise be enough for now."
    "You turn and begin the walk back down the path, boots taking one measured step after another. Each footfall is a compromise—between grief and duty, between what you lost and what remains to protect."

    scene bg ch14_77cd71_9 at full_bg
    # play music "music_placeholder"  # [Music: A single resolving chord, somber but not hopeless]

    scene bg ch14_77cd71_10 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    scene bg ch14_77cd71_11 at full_bg
    "THE END"
    # [GAME END]
    return
