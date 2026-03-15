label chapter8:

    # [Scene: Town Hall Rooftop | Evening — storm-smeared sky]

    scene bg ch8_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind tearing at a loose banner; distant horns from the harbor; the low murmur of the town below]
    # play music "music_placeholder"  # [Music: Tense, urgent strings — a rising ostinato]
    "You arrive with the taste of brine still at the back of your throat; the harbor’s salt clings to the cuff of your jacket like a judgment. The rooftop is crowded with familiar, tired faces and"
    "a few strangers in crisp coats who carry the smell of antiseptic rather than seawater. Mayor Amara Sol stands near the pergola, hands folded, the light catching on the town pin at her lapel like a"
    "small, defiant flare."
    show mayor_amara_sol at left:
        zoom 0.7

    mayor_amara_sol "We have ten council members who will swing either way. Two are wavering. Nine hundred households are in the floodplain. The vote is tomorrow at noon."
    "You let those numbers pool in your chest and become a cold stone. Numbers have always been things you could handle—clear inputs, rational outputs—but tonight they feel porous, like sand. Lina is moving through the group"
    "with a clipboard and a breathless urgency that reads like love turned militant. She is already organizing a dawn protest: signs, shifts, someone to bring hot soup, another to make sure the speakers' amplifier is battery-backed."
    show lina_park at right:
        zoom 0.7

    lina_park "If we let them call this an emergency and move first, they build around what makes money. The old alleys, the fishermen's sheds—gone. We can't let 'em write us out of our own maps."
    "You watch her hand flatten on the weathered town plan; the gesture looks like it could bruise paper. Tomas stands near the railing, jaw working as if chewing a problem into pieces you can see. Elias"
    "Rowe is close enough that when he leans in—sketchbook folded like a shield—you feel the faint heat that always comes with him but find your thoughts elsewhere."
    show elias_rowe at center:
        zoom 0.7

    elias_rowe "We can get oversight. Conditions, monitoring, an independent audit clause. We make them sign protections for the historic districts."
    "You open the Moleskine and your pen already knows the shapes of clauses—oversight committees, phased approvals, escrowed funds. You feel ridiculous, like a shoal-swept mariner trying to stitch a storm-sail with a thread of reassurance."
    hide mayor_amara_sol
    hide lina_park
    hide elias_rowe

    scene bg ch8_6b08b4_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A gull cries somewhere below, a sharp punctuation to the rooftop’s hum]
    # play music "music_placeholder"  # [Music: The strings climb — sharper, impatient]
    show mayor_amara_sol at left:
        zoom 0.7

    mayor_amara_sol "If we don't accept a timeline, Serena's investors pull. If they pull, the town doesn't just lose a project—insurance rates spike, contractors walk, and we face rolling blackouts and clogged evacuation corridors next storm season."
    "You picture those corridors choked with water and tired feet. The memory of your father, of a shed that smelled like diesel and coffee, rides up your ribs like a blade you keep trying not to open."

    "Tomas Reyes" "We've seen what waiting for the 'perfect' plan costs. I've watched neighbors pack up while committees argued. I don't want another storm to take someone because we were pontificating."
    "His voice is a rope thrown across a chasm. Lina's face crumples in one small, human fissure between fury and fear."
    show lina_park at right:
        zoom 0.7

    lina_park "We also can't sign our future away for a glossy photo op. They won't fix what they don't value. This town isn't a pilot project for someone else's résumé."
    "The rooftop conversation fractures and reassembles like glass in a surge—sharp edges, then a new, uneasy whole. You find yourself drafting conditional oversight language out loud, an odd, public exhalation of clauses and contingencies that feels like bargaining with the sea."
    "You try to be precise. The pen is a small, useless thing against the larger tides."

    menu:
        "Read your draft aloud to the group":
            "You stand and read the clauses slowly; words like 'escrow' and 'independent audit' land in the cold air. Some nod. Others look at you like you offered them a map with half the coastline erased."
        "Keep your notes private and listen":
            "You tuck the notebook away and listen. Lina tells a story about a roof that washed into the channel; you feel shame like salt in an open cut."

    # --- merge ---
    "Continue"
    # [Scene: Community Meadow (Rooftop garden beds) | Night slides into pre-dawn]
    hide mayor_amara_sol
    hide lina_park

    scene bg ch8_6b08b4_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rustle of tarps being folded; the distant throb of a generator; a dog barking far off]
    # play music "music_placeholder"  # [Music: A low percussion that mimics heartbeats — steady and quickening]
    "Lina moves like someone who has rehearsed courage out of exhaustion. She's plastering slogans onto cardboard with furious speed, smearing paint with fingers that still smell faintly of soil. She looks up when you approach, and"
    "for a sliver of a second her expression cracks into something softer—something unreadable, layered with gratitude and a dangerous hope."
    show lina_park at left:
        zoom 0.7

    lina_park "We hit the harbor at dawn. We get a line of people between the crews and the seawall blueprints. We won't be violent—just a living presence. We make them see us."
    "You want to say it isn't enough, that presence might be an invitation to cameras that will cut the town into soundbites, but speaking that thought would be to pitch a stone at someone's tethered life-raft."
    "Elias Rowe joins you, sketchbook under his arm, eyes bright and tired."
    show elias_rowe at right:
        zoom 0.7

    elias_rowe "If you let them build without stipulations, the seawall will be designed to protect the harbor and main roads, not the creeks and alleys. Living shorelines break waves differently—they buy time and retain the things that make this place ours."
    "You catch the tremor in his hands when he presses a small schematic to you—living berms, marsh pockets knit to engineered pilings. He speaks as if each line can be coaxed into being by faith, which is both reckless and endearing."
    "You try to meet his optimism with measured caution and fail."
    show maya_calder at center:
        zoom 0.7

    maya_calder "I can draft oversight. I can get monitoring clauses and preservation buffers for the oldest blocks. We can—"

    elias_rowe "Or we can ask them to bundle living-shoreline pilots into the contract. Make it non-optional. Tie their payout to ecological benchmarks, not just concrete milestones."
    "His words land like a hand on your shoulder. You feel the old armor peel, a slow, icy slide of grief and the neat rationality that used to hold everything together. It is humiliating—you're supposed to"
    "be the scientist who keeps feelings at bay by converting them into models. Instead you are bargaining with people, with futures."

    menu:
        "Take Elias's hand, briefly":
            "You close your fingers around his—warm, callused, steady. The contact is a little rebellion; it loosens something like breath."
        "Keep your hands on the notebook and gesture toward the clauses":
            "You point to your notes instead. Your fingers tremble. Elias watches, patient and a little wounded."

    # --- merge ---
    "Continue"
    # [Scene: Harbor | Dawn — the negotiation]
    hide lina_park
    hide elias_rowe
    hide maya_calder

    scene bg ch8_6b08b4_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The roar of surf meeting the old breakwater; shouted directions; shutters clacking as cameras calibrate]
    # play music "music_placeholder"  # [Music: Full orchestral surge — horns and strings in a violent, escalating rhythm]
    "Serena Voss stands where wind and water meet—immaculate as a ship's prow, cufflinks glinting as if with the cold light of calculation. Her holo-tablet casts blue across her face; the investors' feeds already pulse like hungry"
    "lanterns over the crowd. She gives you the offer again, as if repetition can turn concession into mercy."
    show serena_voss at left:
        zoom 0.7

    serena_voss "Approve the emergency allocation within seventy-two hours. We break ground immediately after signatures. Main roads, harbor, essential services—secure within months. Think of how many roofs we'd save."
    "Her voice is precise, and for a moment you almost believe the geometry of safety she lays out. Then Lina's signs flash in the peripheral vision of the press—'HOMES NOT PROFIT'—and the gloss slides off the"
    "plan. You can see the seam where her seawall will favor high-value corridors and leave marginal streets to rot."
    show mayor_amara_sol at right:
        zoom 0.7

    mayor_amara_sol "We cannot gamble on waiting for pilots to scale. People need certainty. But—"
    "Her pen hovers. You feel the weight of her hesitation as if it were your own chest closing in. The councilors' faces are pixilated concern—some watching polls, some counting dollars. The town is a map of levers and hesitations and someone is sitting on the fulcrum."
    "You hold your notebook like a lifebuoy and humiliate yourself by thinking you can be both scientist and diplomat, that your clauses can paper over grief and make it acceptable."
    show maya_calder at center:
        zoom 0.7

    maya_calder "We can include strict oversight language. Escrowed funds for community relocation if necessary, independent auditors, and a phased approval that ties subsequent funds to ecological and social benchmarks."

    serena_voss "That's exactly the kind of responsible governance we encourage. Constraints add market assurance. Our legal team will consider those clauses."
    "You want to breathe. Instead your pen scratches out the phrase 'market assurance' as if erasing a small, personal betrayal."
    hide serena_voss
    show elias_rowe at left:
        zoom 0.7

    elias_rowe "Not 'consider.' Make pilots mandatory. Tie disbursement to living-shoreline benchmarks. If you do the seawall only, you hand them the map of who stays and who goes."
    "There is a shift, tiny and seismic. Serena Voss's expression doesn't change; it's practiced, but something like a cold shadow crosses her eyes."
    hide mayor_amara_sol
    show serena_voss at right:
        zoom 0.7

    serena_voss "Pilots delay. Investors want certainty. Delays threaten the contract and, by extension, the security you claim to want."
    "The cameras tighten. Someone on the edge of the crowd whispers of lawsuits; another voice murmurs about insurance. The wind picks up; spray beads at the top of the breakwater like thrown salt."

    "Tomas Reyes" "Don't let them make us a museum of what used to be. But don't throw us to the tide either."
    "His words are fragments, each one too heavy to hold. The pressure coils tighter, a physical thing that makes your fingers ache and your jaw clench. Something inside you that kept grief fenced into tidy compartments—graphs, charts, field notes—splinters."
    "You think of your father's boat, of the way he would tie the dock lines with hands that knew every knot by memory. You think of the smell that used to mean safety: diesel, coffee, weathered"
    "wood. That smell is gone from many places now, replaced by the sterile tang of corporate solutioning."

    maya_calder "If we accept the contract as-is, we risk carving the town around a new center—wealth and infrastructure here, others left beyond the wall's protection. If we push for pilots, we may delay what keeps people dry this season."
    "Silence drops like a curtain. Your notebook's red underline of '72 hours' from last week's meeting feels now like a pulsing, accusing eye."

    serena_voss "Make your oversight conditions reasonable. Allow us to act quickly. We'll fund preservations where necessary, open bidding to local contractors. You don't have to choose purity over saving lives."
    "Her words are a blade dressed as balm."
    "You realize, with sudden clarity that tastes like iron, that every path cuts something vital. You can feel the town splitting—not just politically, but in the lived geometry of who will sleep under roofs that hold."
    "The gust slams the map on the table; the holo-graphics flicker. Your chest feels jammed with a thousand small decisions pressing like tide-lines."
    "Inside your ribcage, something breaks—the neat rationality you wore like armor against grief snaps like thin wire. The sound is small but its echo is enormous. You are suddenly raggedly human, and the crowd can see it, reflected in wet lamplight and the cameras' lenses."
    "Lina's jaw is a hard line. Elias's hand hovers near yours and doesn't close. Mayor Sol's pen trembles. Tomas folds his arms against the wind as if he could hold back the sea itself."
    "You are a fulcrum. Every word you write into the notebook will be quoted, spun, weaponized. Every clause will bend a life. The choice narrows to three sharp edges, each committing the town to a different carved future."
    # play music "music_placeholder"  # [Music: Climactic, knives-sharp; strings and percussion converge on a single, held chord]
    # play sound "sfx_placeholder"  # [Sound: A distant siren, the slap of a heavy wave against concrete]

    menu:
        "Sign the constrained seawall with oversight":
            "You hear the syllables 'sign' and they taste of rust and relief. Some faces soften; others look betrayed. The cameras flare."
        "Insist on bundling living-shoreline pilots":
            "You say 'bundle' and the word hangs between hope and stubbornness. Serena's jaw tightens; Lina's eyes light like flint. The crowd murmurs—fear and pride braided together."

    # --- merge ---
    "Continue"
    hide maya_calder
    hide elias_rowe
    hide serena_voss

    scene bg ch8_6b08b4_5 at full_bg
    # play music "music_placeholder"  # [Music: The held chord fractures into an urgent, discordant cadence — every second a drumbeat toward choice]
    "You know what each option means in your bones. You also know there is a third path that would rip open everything: expose Haruto’s suppressed dataset and let the truth go loose."
    "Your fingers hover over the page, then over your tablet where the dataset lives in a buried folder—if it is there, if the access is still yours. The Schrödinger-like doubt is a small, cruel thing; you pivot away from specifics and toward consequence."
    show maya_calder at left:
        zoom 0.7

    maya_calder "We can accept focused funds with strict oversight. We can insist on bundled pilots that force ecological accountability. Or we can make the suppressed data public and force an independent review—risking investor flight and legal storms, but maybe, finally, true transparency."
    "The wind bites. A gull folds in on itself against the gust. The town waits like a held breath at the edge of drowning or redemption."
    # play music "music_placeholder"  # [Music: Peak — a single, very high sustained string; then a sudden, deliberate cut]

    menu:
        "Accept a narrowly constrained seawall contract with strict oversight language.":
            jump chapter9
        "Insist on a bundled agreement—seawall plus living-shoreline pilots.":
            jump chapter9
        "Release the suppressed dataset publicly to force independent review.":
            jump chapter13
    return
