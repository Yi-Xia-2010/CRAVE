label chapter3:

    # [Scene: The Dunes and Emergency Barricade | Dusk]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, hollow strings; distant, rhythmic percussion that mimics the sea]
    # play sound "sfx_placeholder"  # [Sound: Gulls crying; the soft, abrasive whisper of wind across sand; sand shifting underfoot]
    "You leave the warm halo of the community hall the way you leave a wound — careful, because anything careless might tear the scab. The streetlamps throw halos over puddles; your boots make small, wet impressions"
    "that the tide will likely erase. Rosa's café light recedes behind you, a rectangle of domestic safety whose smell of coffee and cinnamon you can still taste at the back of your throat."
    "Your notebook is heavy with half-formed sentences. The line you wrote in the margin is a hinge that swings two ways and always toward loss. You thumb the dented compass at your collar; the metal is"
    "cool, familiar, a measure of directions you used to know by heart. The red thread on your wrist pulls a little tighter, as if it too anticipates the snap you can feel in your stomach."
    "Ahead, the barricade looks smaller close up and monstrously large from the boardwalk: a stitched border of sandbags, pallets, and old doors, protest banners stitched between them like flags for a town that doesn't know whether"
    "it's under siege or simply awake. Salt has crusted on the painted letters. Someone's handwriting — looping and urgent — reads: NOT ON OUR SHORES."
    "You slow your step. The horizon is a trembling grey line where the sea keeps a long, patient distance. The air tastes metallic, as if the sky is bleeding iron. Gulls wheel, their cries sharp as punctuation."

    scene bg ch3_98c6f2_2 at full_bg
    "Your palms remember the weight of hauling sacks through the night. Muscle memory flares and then quiets; memory is its own kind of ache."
    "You expected to be alone. You wanted the clarity that solitude can provide. Instead, a familiar voice — Elias — folds into the wind like a thrown scarf."
    show elias_novak at left:
        zoom 0.7

    elias_novak "You came down here."
    "(He has that way of making statements mean an invitation.)"
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "I meant to. After the hall..."
    "You keep your voice small because the night is already loud with other people's stakes. 'I promised a community proposal.'"

    elias_novak "You promised a lot of things tonight."
    "'Good promises. Dangerous ones.' He pushes off the railing and walks closer, boots spitting up sand. 'Listen — people are ready, Maya. I met with the kids from the marina; the dockworkers are talking to Rosa's"
    "regulars. We can fill the council chamber. We can shout until the Mayor's ears ring.'"

    maya_serrano "And then what? We shout. They ignore us. They send security. They fast-track Kestrel's funding and we end up negotiating scraps."
    "The words are sharper than you intend. You taste the salt of old arguments. 'You know how the council works. You know how Lillian maneuvers.'"

    elias_novak "Yeah, I know how she maneuvers. I also know how people move when something is theirs. When they can’t be bought or blanded into relocation schemes. If we make it public — really public — corporate boards flinch. Media lights draw attention. People in offices upstate see faces they can't erase."
    "You watch him. He believes in the swell, in bodies and voices as anchors. You can see the image he paints and feel the pull in your chest: the lure of collective wrath made constructive, the hope that a community can be ferocious and gentle at once."

    menu:
        "Step closer to Elias and match his urgency":
            "You step forward, letting the sound of his conviction fill the space between you. For a few heartbeats the idea of mass mobilization feels like an actual plan, whole and warm."
        "Hold back and list logistical risks aloud":
            "You keep your distance and let the ledger in your head breathe: arrests, broken limbs, the hungry machinery of legal retribution. The neat lines of numbers make the emotion fray at the edges."

    # --- merge ---
    "The scene resumes with Elias asking Maya to turn the proposal into a movement."

    elias_novak "Look — none of this is easy. But the worst thing would be sleeping and letting them redraw the map. You said you'd put together a proposal. Help me turn it into a movement."
    "You want — more than anything — for the town to be whole. You also want for Finn not to be forced into a place where he has no work. Your brother's face, walked-into the wind,"
    "rose unbidden. You remember his hands, the calluses from nets and rope, the way he smiles when something he fixes holds."
    "Footsteps crunch behind you. Noah walks up the dune like someone who measures every step because each one maps consequences. He is clean and oddly out of place among the frayed banners: navy coat, a tablet tucked under his arm, a small corporate pin catching the dimming light."
    show noah_kestrel at center:
        zoom 0.7

    noah_kestrel "You're arguing in the open air."
    "The tone is flat, not unkind. 'I could have sent a message. But I thought… better to be honest.'"

    maya_serrano "Honest about what, Noah? That your firm can deliver a sea-wall that actually keeps water out? That it's costly and—"
    "You stop, because the word 'costly' is a polite lid for eviction and bought-out neighborhoods."

    noah_kestrel "Costly, yes. Difficult, yes. But if we tie it to a fast-track contract, the work begins months sooner. Lives are protected sooner. Rezoning can be implemented fairly if we design buyout programs with equity in mind."
    "He speaks like an engineer describing load-bearing stresses — facts first, rhetoric second. 'We don't have to hand the entire town to developers. There are ways to prioritize vulnerable households.'"

    elias_novak "Equity in a corporate contract is a pretty sentence, Noah. You know that. You know how those clauses get buried under legalese."

    noah_kestrel "And you know blowback. You know what happens when regulatory frameworks aren't met. You know what happens when volunteers get hurt and there's no indemnity. Your crowd can make noise, Elias, but noise doesn't fix foundations."

    maya_serrano "So what's the—"
    "You want to ask which of them is right, but the question is stupid; both of them are right and the truth is a set of slices. '—what do I do? How do I square not losing people with not selling the town out?'"
    hide elias_novak
    hide maya_serrano
    hide noah_kestrel

    scene bg ch3_98c6f2_3 at full_bg
    "The three paths fold into the page like knives pressed into wet clay. Each promises to cut something valuable away."
    show noah_kestrel at left:
        zoom 0.7

    noah_kestrel "Negotiate now. Fast-track the engineering phase. We set up a community oversight board to monitor buyouts and maintenance. Keep people in their homes where possible. Where not possible, equitable relocation assistance. I know it's not perfect, but it's practical."
    show elias_novak at right:
        zoom 0.7

    elias_novak "Practical gets you maps with fewer names on them. 'Equitable relocation' is a phrase you can print on a brochure and still lose a block to flood insurance tables. People are not spreadsheets, Noah. They are living, breathing assemblages of stories. You bulldoze their stories, you bulldoze the reason they'll fight for any future."

    noah_kestrel "And you think leaving things to a movement won't tear the town apart? You think we can just 'fight' and not have fallout? Tactics have costs."

    elias_novak "At least the costs are ours. At least we decide the stakes."
    "You look between them and hear Dr. Hana's voice in your head, precise and tired."
    show dr_hana_park at center:
        zoom 0.7

    dr_hana_park "Strategically traumatic, Maya. Sometimes a brutal, surgical choice protects the majority long-term. But you have to be ready to live with the trauma you ask of others."
    "You taste the word 'trauma' like copper. It is not a deterrent; it is a complication that wraps itself around every argument like kelp."
    "A weight settles in your chest and you realize Finn is there too, though you hadn't noticed him approach. He stands a few yards away, hands shoved in a patched jacket, eyes on the barricade. Seeing"
    "him narrows the world to a single luminous axis: keep Finn and people like him safe."
    hide noah_kestrel
    show finn_serrano at left:
        zoom 0.7

    finn_serrano "You can't make everyone happy,' he says quietly. 'You know that, Maya."
    "He looks at you with a kid's stubbornness and a man's tiredness. 'But you are maybe the one person everyone listens to long enough to try something different.'"
    hide elias_novak
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "That doesn't make it any easier."
    "You look down at your thread-tied wrist. 'I promised I wouldn't go it alone, and I keep trying to shoulder it anyway.'"
    hide dr_hana_park
    show elias_novak at center:
        zoom 0.7

    elias_novak "Nobody's asking you to be Atlas."
    "He comes closer; the wind tugs a loose strand of his hair into his face. 'We want you to stand with us.'"
    hide finn_serrano
    show noah_kestrel at left:
        zoom 0.7

    noah_kestrel "And we want you to help steer the negotiations so they don't steamroller the vulnerable."
    "You close your eyes for a clean, brief second and count the breaths that give you back to yourself. The wind is a metronome. Each option is a scale with human lives as weights."
    "You bring your pen down to the paper and, with hands that tremble, you prepare to choose."
    hide maya_serrano
    hide elias_novak
    hide noah_kestrel

    scene bg ch3_98c6f2_4 at full_bg
    # play music "music_placeholder"  # [Music: Strings swell then pull taut, unresolved]
    "Narration: It comes down to you. It has to."

    menu:
        "Stand with Elias — prioritize grassroots mobilization and direct action.":
            jump chapter4
        "Work with Noah — negotiate pragmatic infrastructure and concessions.":
            jump chapter8
        "Lead an independent evacuation/relocation plan — accept painful sacrifices.":
            jump chapter12
    return
