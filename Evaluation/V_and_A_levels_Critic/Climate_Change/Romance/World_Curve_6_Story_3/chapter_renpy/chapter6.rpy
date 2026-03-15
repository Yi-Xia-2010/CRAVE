label chapter6:

    # [Scene: Research Lighthouse | Dawn — A Quiet Morning After the Covenant Signing]

    scene bg ch6_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Soft, hopeful strings with a low drone beneath]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls; the faint clack of boots on wet stairs]
    "You wake with the taste of lantern smoke and sugar in your mouth — the residue of late-night plans and someone's too-sweet celebration bread. Your coral pendant presses cold against the hollow of your throat until Jonah's thumb finds it and warms the cord."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "You looked like you were carrying the whole harbor on your shoulders last night."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Maybe I was."

    jonah_reyes "Then let me carry some. We signed the covenant. The co-op is official. We got Old Man Rafi to bless the work and Saira to back the plans with the data we need.' (he pauses, searching) 'And we... we agreed, Mira. You and me. You heard that before anyone else."
    "You feel Jonah's callused hand brush the pendant sideways, then cup it. His thumb rubs the worn braid and, almost without thinking, his lips press against the coral. The kiss is short and not showy —"
    "intimate as the keeping of a lantern in a storm. It leaves a path of warmth down your collarbone that rushes into the hollow of something you have kept locked since the first time the sea"
    "took a summer."

    mira_kestrel "I heard it.' The word is a promise and a fragility wrapped together. 'I meant it."

    jonah_reyes "Good. Because I'm not leaving. Not now. Not when—' He swallows. 'Not when you're finally asking the town to trust something other than fear."
    "The tower smells of rain and cold metal and the faint ink of your notebook's pages. You reach for that small, tide-scented weight at your hip — your notebook — and find that the pages tremble"
    "less than your pulse. You make a note, a quick line: 'co-op ratified. Rafi blessing. Tessa's hands on the berms.' The handwriting looks steadier than you feel."

    menu:
        "Trace Jonah's thumb with your finger":
            "You let your finger follow the old scar on his knuckle where rope once burned. The motion steadies you both, a private pact in a public morning."
        "Turn back to the maps and review the berm schematics":
            "You lean over the table, forehead resting against a map corner. For a wild second, diagrams replace faces — anchors and lines and levies that could hold water at bay."

    # --- merge ---
    "Scene continues"
    # [Scene: Boardwalk & Docks | Midmorning — Community Work Day]
    hide jonah_reyes
    hide mira_kestrel

    scene bg ch6_601bcb_2 at full_bg
    # play music "music_placeholder"  # [Music: A quick strum of hopeful chords; voices layered in laughter and instruction]
    # play sound "sfx_placeholder"  # [Sound: Hammers, shouted encouragement, a child's squeal splitting the air]
    "The town moves like a tide you can see — pull, mend, push. A repaired shed stands with a new plank glinting in the gray. A child runs by with gulls chasing shadow. Old Man Rafi"
    "stands under a bruise of cloud, his sea-worn coat stitched from a hundred small rescues, and he speaks a blessing: not in grand words but in the cadence of an old fisher's respect — names given"
    "to currents, old nets left to dry, a short prayer to keep hands steady."
    show old_man_rafi at left:
        zoom 0.7

    old_man_rafi "We stitch what we can. We give the earth its roots back and the sea its edges. Bless be the hands that do the work."
    "A murmur of assent. You watch a young volunteer — Tessa, sunlight slicing her hair — laugh as she struggles with a sod of marsh grass. She makes a face at you, eyebrows up: 'See? Practical."
    "Get your hands dirty.' The sight of her—alive, stubborn, impatient as a wave—settles something in your chest that rumpled into momentum last night."
    "Cassian 'Cass' Romano appears by the docks, trench coat mottled with salt, tablet in hand. He doesn't intrude; instead he watches, the lines at his eyes softening. When he approaches, it's with the careful, measured cadence of someone used to translating between technical languages and human ones."
    show cassian_cass_romano at right:
        zoom 0.7

    cassian_cass_romano "You're making good progress. The co-op model — it's... resilient in practice.' (he scans the work) 'If funding holds, we can help reinforce key choke points where the marsh weakens."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "Help, or buy?"

    cassian_cass_romano "Help. But on your terms. I—' He looks at you, and the tone shifts, softer. 'I meant what I said about letting you lead. About community seats. I can push the firm to prioritize that, Mira."
    hide old_man_rafi
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "We need both manpower and steady funding, Cass. But not at the cost of people deciding for themselves. That's the point."

    cassian_cass_romano "Agreed. Then we'll keep the oversight local, and I will fight to keep financing tied to community milestones. No blank checks."

    jonah_reyes "You'll be watched."

    cassian_cass_romano "Good. Keep me honest."
    "The back-and-forth breathes a fragile confidence into the morning. For a passing hour, jokes and work and shared bread make fear seem like a tide that can be pushed back. You laugh when Tessa flings a"
    "sod onto someone's lap and declares it 'artisanal reclamation.' The sound goes somewhere deep and honest."

    menu:
        "Offer Cass a cup of coffee to talk terms again":
            "You hold out the thermos. He accepts, fingers brushing yours. The exchange is small and ordinary; it brightens his expression, and you make a promise to hold him to his words."
        "Call Jonah over and plan the next row of berms with him":
            "You point along the marsh. Jonah leans in, mapping tide lines with his finger. Plans form out of rough hands and mutual shorthand. You both know the labor ahead."

    # --- merge ---
    "Scene continues"
    # [Scene: Research Lighthouse | Afternoon — Weather Models Shift]
    hide cassian_cass_romano
    hide jonah_reyes
    hide mira_kestrel

    scene bg ch6_601bcb_3 at full_bg
    # play music "music_placeholder"  # [Music: Tense low strings, the tempo quickening]
    # play sound "sfx_placeholder"  # [Sound: The hum of equipment; a sudden, distant, rolling thunder]
    "Saira's message is an elastic thing that snaps taut in your chest: the sea’s surface has warmed two degrees above seasonal average; an unnamed cyclone is organizing faster than models predicted. The tone on her voice is tight; she doesn't have room for soft."

    "Dr. Saira N'Goma" "Mira — the feed just updated. It's intensified overnight. The sea surface temps are fueling it. We have maybe twenty-four hours."
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "How strong?"

    "Dr. Saira N'Goma" "Projections show rapid intensification. If it takes that trajectory, some of the berms won't hold. The engineered barriers farther downbay—if their funding holds—might blunt surge, but not if maintenance lapses. You know the model constraints."
    "You do. You know them like the ink on your palms. The calculations map onto memories of nights spent watching water take a roof or a dock. The arousal that has been a low, steady pressure"
    "— all the planning, the signings, the warmth of Jonah's hand — snaps into a white-hot alarm. Everything becomes beats and breath and the raw mechanics of survival."
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "We double the shifts. Pull in every hand that can row or stack or dig. Tessa, pull the youth crew. Rafi, get the elders inside. Mira — what else?"

    mira_kestrel "We prioritize the schoolboats and the nursery sheds. Flare canisters on the east dock. Reinforce the berm at the western inlet — that's the weakest link right now. Cass — keep your teams on the engineered barriers, but coordinate with us."
    show cassian_cass_romano at center:
        zoom 0.7

    cassian_cass_romano "Already on it. I've got a crew on standby and remote pumps we can run. But the pump power is limited; we need to triage."
    "The lighthouse window stares back at you, a flat, wet mirror of the sea that is not yet angry and is already dangerous. You feel every decision like a physical strain. You divide your plans into lists and hand them out like lifejackets."
    # play sound "sfx_placeholder"  # [Sound: A siren begins low and then rises. A bell strikes thrice, then again, like a heartbeat sped up into alarm.]
    # play music "music_placeholder"  # [Music: Strings shred into dissonance; percussion like falling boards]
    "You run."
    # [Scene: Boardwalk & Docks | The Storm — VeryHigh Intensity]
    hide mira_kestrel
    hide jonah_reyes
    hide cassian_cass_romano

    scene bg ch6_601bcb_4 at full_bg
    # play music "music_placeholder"  # [Music: A crashing, relentless percussion; high, keening brass; no melody, only impact]
    # play sound "sfx_placeholder"  # [Sound: Wind screaming, wood splintering, people shouting over the elements]
    "The storm arrives like a blame you can throw nothing against. A wall of warm water lifts and rushes. The berms you and the town built — braided, rooted, honest — take the first hits. In"
    "some stretches, the sand holds like a clenched jaw. In others, where the soil was thin and the funds scarce, the tide finds a seam and rips it open."
    "You stand on the lighthouse balcony with a headlamp tied crooked to your brow, and the sea is a thing alive and older than vows. From this height you can see the geometry of failure as"
    "much as the geometry of bravery: a stretch of town where boats bob harmlessly behind Cass's engineered barriers; another where water has already licked the repaired docks and is climbing like an animal up broken planks."
    "Jonah Reyes slides down the boards to the east dock. You see him plant his feet and fight the surf like a man who learned his faith in rope and oar. He dives toward a flare"
    "kit that had come loose, wrestles it free, and then turns toward a bobbing shape — a child's small boat, overturned and half-full of water. He doesn't hesitate."
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "Jonah! The east berm—"
    "He looks at you, and there is a clause of terror in his face you have never seen: not the stubbornness of protest but the nakedness of a person who is about to lose something he"
    "did not know he could not afford to. 'Go!' he hails back. 'Get people to the nursery and the high ground. I'll get them.'"
    show cassian_cass_romano at right:
        zoom 0.7

    cassian_cass_romano "Mira! We need to prioritize the pump at the north channel — if we lose it, the whole street floods!"

    mira_kestrel "We have to keep the flares going. People are still at sea."

    cassian_cass_romano "We can't save every place at once. Triage!"
    "The words 'triage' and 'impossible' and 'not enough' hammer into you from all sides. The sound of splintering timber is a drumbeat for failure. You are everywhere and nowhere: pulling a rope with a teenager whose"
    "hands are already numb, shouting to anchor a post, half-consciously checking maps, relaying coordinates to Cassian's crew."
    "Then there's a sharp, sickening pop — a berm gives where you had been sure it would hold. A wedge of water surges through, and you feel the air leave the town like breath exhaled in"
    "grief. People scream; others sob with the noise of it. In that instant you recall, with a hot, sudden clarity, the first time you watched your childhood home betray you. The knot you thought you'd unspooled"
    "remains, and now a new strand tightens and snaps."
    "Jonah Reyes fights in the surf — you watch hands and back and shoulder muscles strain — and he looks smaller than belief. He returns, soaked, clutching a soaked flare activation case. His eyes flick to"
    "you for a fragment of a second — there is triumph there, but it's laced with a horror so near it makes his mouth set like someone biting a cord. He passes the flare, but when"
    "he tries to pull another child toward the ladder, a surge takes him off balance. For a hit-and-miss breath you watch him disappear under a crest and then surface again. He coughs, and the cough is"
    "a hard punctuation mark."

    mira_kestrel "Keep pulling. Don't stop."
    # play music "music_placeholder"  # [Music: Brass and strings shred into a single descending wail]
    # play sound "sfx_placeholder"  # [Sound: A long, animal moan of wind; the bell from the lighthouse cracked and strangled]

    "You fight with hands that are not enough. You throw your shoulder into a splinter, dig your heels into the wet, and you hear the wet planks cry. People on the boardwalk — who laughed with you hours ago — are now a chorus of immediate, raw commands" "Anchor the generator! Take the kids to the school! Secure the boats!"
    "And still, water finds the places love couldn't buy. A family's storage shed that was rebuilt by a hundred hands floats away like a paper thing. Cassian 'Cass' Romano's pumps grind and cough and then falter"
    "where his contractor's rotation has left gaps; a seam opens and the barrier he built becomes a dam that is breached. He reaches for you, eyes blazing not with blame but a pleading you cannot answer."

    cassian_cass_romano "We can patch it, Mira, but we need power and—"

    mira_kestrel "Then tell me which neighborhood and I'll send people. Tell me and I'll move heaven."
    "He looks at you as though searching for a faith he is not sure he has the words for. 'You choose,' he says. 'Prioritize.'"
    "You cannot choose. All you can do is throw your body and will into the places where hands are the only currency that counts."
    # [Scene: Boardwalk & Docks | The Eye Breaks — The Highest Point of the Storm]
    hide mira_kestrel
    hide cassian_cass_romano

    scene bg ch6_601bcb_5 at full_bg
    # play music "music_placeholder"  # [Music: Near silence for a second, then an explosive percussion that threatens to break the scene itself]
    # play sound "sfx_placeholder"  # [Sound: A child's cry that seems to undulate with the thunder]
    "Jonah Reyes returns to you, soaked and shaking and bearing the shape of someone who has been very near losing everything they thought they were. He grabs your sleeve, his nails biting into fabric."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "There was a little one— Lila. Katrina's girl. We almost—"
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Is she—?"

    jonah_reyes "She's okay. She's with Rafi. We saved her. Mira—"
    "He drops his voice and the storm seems to lean in."

    jonah_reyes "We lost Mateo's boat. The fishery lost crates. Old Man Harper's net store—he's gone. Some places held. Some places—"

    mira_kestrel "How bad?"

    jonah_reyes "Bad."
    "You listen to the word fill the space between thunderclaps. It is an honest and terrible description. Your hands tremble. Your coral pendant bangs against the charts in your jacket."

    mira_kestrel "We did everything we could."

    jonah_reyes "We did everything we could with what we had. Was that enough?"
    "The question is not a rhetorical one. It lands on your chest like a dropped plank. You feel the old ledger in your head — the memory ledger of everything you failed to save before —"
    "and you sense, with a sharp, succeeding pain, that the tally will be heavy again."
    # [Scene: Boardwalk — Nightfall After the Storm]
    hide jonah_reyes
    hide mira_kestrel

    scene bg ch6_601bcb_6 at full_bg
    # play music "music_placeholder"  # [Music: A single, low cello note held until it breaks]
    # play sound "sfx_placeholder"  # [Sound: Muffled weeping; the soft scrape of boots on water-stained wood]
    "The town's breath is ragged. Fires are lit in safe patches to boil water. People huddle in doorway arcs, wrapped in donated blankets and the smell of wet wool. You walk the ruined length of the"
    "boardwalk, hands raw from hauling, nails full of salt. A child offers you a small, water-stiff drawing of a boat with a crooked sun; you take it like a relic."
    show old_man_rafi at left:
        zoom 0.7

    old_man_rafi "We did what the town could. The sea is a hard teacher."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "We thought we could outwork it."

    old_man_rafi "We never outwork the sea. We learn to live with it, to bargain, to make good gifts and call that stewardship. And sometimes the sea takes what you think is yours."
    "You stand on wet planks and watch people salvage what they can. The smell of ash — from a fire pushed too close to the wood — mixes with the salt and the sweet rot of"
    "seaweed. A family's fish boxes float past like small, dark driftwood coffins. You imagine each one containing the livelihoods of families that will have different winters after this."
    "Voices gather behind you, less storm now and more human. They are sharp and small and terrible."

    "Neighbor" "You promised we'd be safe. You said—"

    "Another Voice" "She signed that covenant! Who keeps the oversight? Where was the council last night?"
    "People look at you as if you are the hinge on which fate turned. You, who organized, who negotiated, who held the co-op's pen in your hand. You who slept with the weight of responsibility like a cold stone under your ribs."

    mira_kestrel "We did what we could. We prioritized lives—"

    "Neighbor" "Prioritized what? The docks? The berms? Or the photo ops Mayor Lynette loves? Tell us what was supposed to happen."
    "A silence like a net drops between you and the crowd. Jonah places a hand on your shoulder — strong and warm, a tether. He squeezes once; it's meant to be a lifeline. You feel the"
    "pressure and it offers something like comfort. But it's not apology and it's not absolution. It's simply there."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "We fought. We saved people. Don't stand here and be your own judge in front of them. They need answers, sure — but they'll get them clearer if we stand together."
    "A man in the back — Mateo, whose boat you remember going out earlier — shakes his head so hard his cap flies off."

    "Mateo" "You told us to trust the berms. My traps are gone. My season's gone. What do we eat? What do my boys do?"
    "Each question hits like the sea's slap. The people who look to you are not asking for kindness; they are demanding the accounting of survival."

    mira_kestrel "I know. I know. I'm—"
    "A hundred small accusations spring like splinters and you feel each one. You think of the ledger of losses, of the first house that was taken years ago when you were away, the memory of your"
    "failure that you have been carrying like a secret wound. That wound reopens and floods."
    "Your hands go to your coral pendant. It is wet, and the coral's surface is warmed by your palm. The pendant feels heavier than it did in the lighthouse, carrying not just salt but the weight of what you couldn't prevent."
    hide old_man_rafi
    hide mira_kestrel
    hide jonah_reyes

    scene bg ch6_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: Single cello note finally snaps; silence envelopes the scene for a beat too long]
    # play sound "sfx_placeholder"  # [Sound: The ocean, a distant, steady, indifferent breathing]
    "You walk to the end of the boardwalk where the planks thin and the water is a level black. You sit on the wet wood, boots soaked, knees cold. The pendant rests against your sternum like a small, stubborn heart."
    "You think of the night you left to study and the house you couldn't save. You think of the nights rebuilding, of Tessa's bright impatience, of Rafi's ritual blessings, of Jonah's steady hands and the brief"
    "sharpness on Cass's face when funding faltered. You think of all the hands that have shaped the berms and the barriers — people who believed they could carve safety from storm and sand."
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "I gave everything."
    "The phrase is not a defense; it is a confession. It feels both true and hollow. In the hush that follows the storm's roaring exit, guilt blooms anew — not the pitying kind but a harder,"
    "colder thing that settles like frost. You had promised stewardship. You had made plans that were as much moral as technical. You had led. Still, the sea took."
    "A child appears at your side, mud on her knees and hair plastered to her face. She holds out a small, sodden toy boat and offers it to you like an offering, like a question."

    "Child" "Is the sea mad at us?"

    mira_kestrel "No. The sea isn't mad. It doesn't choose. But sometimes... sometimes it takes what we love. And sometimes our best isn't enough."
    "The child looks at you with a small, adult seriousness that alone can cut clean through pretense. She drops her gaze to your pendant and then to your hands."

    "Child" "Then what do we do now?"
    "You have no ready answer that will stitch things back. You reach out and take the toy, feeling the frayed paint and cold plastic. You stand with it a moment, the board below you slick and"
    "a little treacherous, and you feel the knot inside you — the one that has always made you careful — unravel into something harder: grief sharpened into a bitter, steady shape."
    "Jonah Reyes comes to stand beside you. He doesn't try to fix the sense of accusation aimed at your shoulders. He simply plants himself there, a living wall against the wind and the town's eyes."
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "We'll sort it. We'll rebuild. It won't be the same, Mira. It won't be what it was. But we'll keep—"

    mira_kestrel "Keep what? Our lives? Our hands? Sometimes I don't know what I'm bargaining for anymore."

    jonah_reyes "You bargained for people. You put the town first. That means something."

    mira_kestrel "It means I have to live with what I couldn't stop. And that's a heavier thing than I expected."
    "Silence settles. The town is not ablaze; it's raw and messy, bodies working through shock, the practical things of salvage and making lists and rationing fuel. But the political calculus — the way blame hardens into"
    "factions and sentences — has begun its slow turn. Eyes that once shared laughter find new edges. You are at the fulcrum, feeling the torque of responsibility and the impossibility of fully holding the town's collapse"
    "in your arms."
    # play music "music_placeholder"  # [Music: A single, low, sustained chord; then a long, resigned exhale of wind]
    hide mira_kestrel
    hide jonah_reyes

    scene bg ch6_601bcb_8 at full_bg
    "You sit on the wet plank and let the weight of the pendant and the day's events press against your sternum. The knot within you — the old failure, the new losses — does not unwind"
    "into catharsis. It tightens, then stretches into a new, harder grief that is both personal and communal. Love — Jonah's hand still warm on your shoulder, Tessa's practical determination, Rafi's ritual — remains a warmth that"
    "cannot hold back a tide."
    "You realize, with a clarity that is part shame and part acceptance, that you gave everything you could. It wasn't enough."
    # play music "music_placeholder"  # [Music: Faint, mournful wind instruments; then a soft decrescendo into silence]

    scene bg ch6_601bcb_9 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gull; the steady breathing of a town that will learn to measure loss]

    scene bg ch6_601bcb_10 at full_bg
    "THE END"
    # [GAME END]
    return
