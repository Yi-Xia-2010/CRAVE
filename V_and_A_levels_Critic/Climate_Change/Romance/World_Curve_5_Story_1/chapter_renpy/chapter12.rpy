label chapter12:

    # [Scene: Council Annex | Late Morning]

    scene bg ch12_f99e88_1 at full_bg
    # play music "music_placeholder"  # [Music: Bright, urgent strings; a steady percussion undercurrent]
    # play sound "sfx_placeholder"  # [Sound: Muffled chatter and the distant scrape of chairs from adjacent rooms]
    "You still remember the weight of the pen—the small, decisive pressure that turned worry into policy. The cough of the air-conditioning is a domestic, almost conspiratorial sound; the room smells faintly of lemon cleaner and hot"
    "paper. Your gloves are somewhere in the bag at your feet, but your hands are steady enough to fold the corner of the signed page and tuck it into your notebook."
    show mayor_serena_okoye at left:
        zoom 0.7

    mayor_serena_okoye "This gives us the framework we needed. Enforcement language is clear enough to move forward."
    show elias_rook at right:
        zoom 0.7

    elias_rook "We couldn't have done it without the legal team and the community council. And—without you, Ayla."
    "You hear the clause in his voice that wants to turn into something else. For now it lodges like a warm pebble in your chest. You meet his steel-blue gaze and notice how his hair is"
    "wind-mussed, how his hands still carry a faint smudge of soil from the test plots outside the lab."
    "You let the gratitude settle; it is not unalloyed. Somewhere between the gloss of Jonah's signatures and the fine print, there are losses: terraces that cannot be rebuilt, a narrow promenade cutting through a familiar patch"
    "of mint, the memory of a childhood fence post that will not return. But the covenant holds land trusts and greenhouse funding in law—words that will mean roofs and raised beds for many."
    show jonah_hale at center:
        zoom 0.7

    jonah_hale "A rational compromise, Ms. Moreno. We're all better for it."
    "You take his hand. It is cool and deliberate, like the handshake itself could anchor an entire future. You feel the tremor of everything that followed the inked line—months that will not be easy but will be full of tangible labor."
    hide mayor_serena_okoye
    hide elias_rook
    hide jonah_hale

    scene bg ch12_f99e88_2 at full_bg
    # play music "music_placeholder"  # [Music: The strings swell into a hopeful motif]
    # [Scene: Restored Rooftop Terraces | Dawn, Three Months Later]

    scene bg ch12_f99e88_3 at full_bg
    # play music "music_placeholder"  # [Music: Rhythmic, driving—hand drums and violin harmonies]
    # play sound "sfx_placeholder"  # [Sound: The thump of a delivery truck backing up; the slap of soil into wheelbarrows; laughter and shouted instructions]
    "You wear the jacket you patched together a hundred times over. Your gloves are the same pair—the seams smoothed by use—and you smell damp earth and diesel. The terraces hum with purpose: city crews set rebar"
    "for planters, volunteers ferry compost in a human chain, lab technicians pin up sensor arrays beside heirloom tomatoes."
    show elias_rook at left:
        zoom 0.7

    elias_rook "I'll run a seasonal simulation to make sure our water budgets hold up. If we reroute overflow to the eastern channel, those boxes will survive a ten-year storm."

    elias_rook "And I'll run a seasonal simulation to make sure our water budgets hold up. If we reroute overflow to the eastern channel, those boxes will survive a ten-year storm."
    "You wear the jacket you patched together a hundred times over. Your gloves are the same pair—the seams smoothed by use—and you smell damp earth and diesel. The terraces hum with purpose: city crews set rebar"
    "for planters, volunteers ferry compost in a human chain, lab technicians pin up sensor arrays beside heirloom tomatoes."

    "Volunteer" "Ayla, how deep for the sedges?"
    show ayla_moreno at right:
        zoom 0.7

    ayla_moreno "Wide base, shallow crown. Let the roots spread out—think of them splaying like anchors."

    elias_rook "And I'll run a seasonal simulation to make sure our water budgets hold up. If we reroute overflow to the eastern channel, those boxes will survive a ten-year storm."
    "Your exchanges are practical and warm; the two of you are a practiced team. The work is fast, intense—hands in mud, sleeves rolled, briefings squeezed between wheelbarrow runs. The arousal of the scene is high: plans become bricks and soil, spreadsheets become green."
    show kira_tseng at center:
        zoom 0.7

    kira_tseng "You did what you had to, Ayla. But some of us wanted less bargaining and more blocking."

    ayla_moreno "I know. I argued in the room. I pushed for enforcement clauses that would lock these spaces into law."

    kira_tseng "Legal paper is thin when machines have money behind them."

    ayla_moreno "Then keep watching the machines. Hold them accountable. This isn't the end of the fight—it's a new front."

    kira_tseng "You always make it sound inevitable. I just— I needed to say it out loud."
    "You and Kira exchange a look that holds both grievance and the brittle thread of trust. Her rebuke has teeth, but it is not final. It is the kind of public pain that helps keep compromise honest."

    menu:
        "Let Elias handle the town hearing response":
            "You step back slightly and watch Elias speak with quiet authority, noticing the steadiness he brings when you need it most."
        "Take the mic and speak for the terraces yourself":
            "You step forward, soil under your nails catching the lights, and your voice rises clear—part instruction, part invocation—reminding everyone why the gardens matter."

    # --- merge ---
    "The meeting proceeds with the oversight plan presented and debated."
    # [/INTERACTION]
    # [Scene: City Hearing / Public Meeting | Afternoon]
    hide elias_rook
    hide ayla_moreno
    hide kira_tseng

    scene bg ch12_f99e88_4 at full_bg
    # play music "music_placeholder"  # [Music: Tense brass, then resolving into hopeful harmonics]
    # play sound "sfx_placeholder"  # [Sound: Applause, the rustle of papers, an undercurrent of murmured debate]
    "You and Elias present co-authored oversight plans to Mayor Serena and the council. Your slides are practical—maintenance schedules, community oversight boards—and Elias moves through risk scenarios with the same measured kindness that makes his models persuasive."
    show elias_rook at left:
        zoom 0.7

    elias_rook "These covenants include community co-management, explicit funding streams, and a review panel that includes local stakeholders."
    show mayor_serena_okoye at right:
        zoom 0.7

    mayor_serena_okoye "Enforcement mechanisms are solid. We can allocate immediate funds to implement."
    show kira_tseng at center:
        zoom 0.7

    kira_tseng "You call it co-management, but how do we stop the subtle erosion—the permits, the exclusions, the slowly changing rules that push people out?"
    "You feel every gaze on you. For the second time that morning you stand between a policy that saved spaces and the people who fear what was lost."
    hide elias_rook
    show ayla_moreno at left:
        zoom 0.7

    ayla_moreno "We write the covenant so it can't be undone by small changes. There are trigger clauses for judicial oversight, penalties for non-compliance, and community-appointed auditors. We won't be policed out of our own roofs."

    kira_tseng "And when Jonah's partners start seeing returns they didn't count on? When the promenade becomes desirable real estate?"
    hide mayor_serena_okoye
    show elias_rook at right:
        zoom 0.7

    elias_rook "That's why the land trusts are perpetual—no speculative sale. The covenant locks in community stewardship."
    "The exchange spirals—voices rise, then settle into a rhythm of argument and counterargument. You feel each point like a wind against a fragile canopy. But with every rebuttal, the legal scaffolding you fought for proves functional; it holds."
    hide kira_tseng
    show mayor_serena_okoye at center:
        zoom 0.7

    mayor_serena_okoye "Passed. The council accepts the oversight plan for immediate implementation. We'll convene the first audit panel within thirty days."
    "Applause erupts, not triumphant but relieved, the kind that follows a long, dangerous negotiation. You let the sound wash over you. It's not all victory—there are still losses, people who lost plots—but for now the net is survival and expansion in the places that matter."
    # [Scene: Community Greenhouse | Twilight, Late Summer]
    hide ayla_moreno
    hide elias_rook
    hide mayor_serena_okoye

    scene bg ch12_f99e88_5 at full_bg
    # play music "music_placeholder"  # [Music: Soft cello and piano; undercurrents of uplift]
    # play sound "sfx_placeholder"  # [Sound: The gentle drip of condensation; distant laughter from the plaza]
    "You sort seed jars into boxes on the communal table. The greenhouse smells like damp leaves, compost tea, and rosemary. Outside, the city hums; inside, there is a sanctuary hum—the slow, intimate life of plants."
    show elias_rook at left:
        zoom 0.7

    elias_rook "You saved these?"
    show ayla_moreno at right:
        zoom 0.7

    ayla_moreno "I couldn't bring back the fence, but I kept the seeds that grew along it."
    "He smiles, small and earnest, and without the performative neatness that Jonah brings. He folds the torn packet into the pages of your notebook, his fingers pausing over the soil-streaked margin."

    elias_rook "We'll plant those together, next season."

    ayla_moreno "You'll get mud on your sleeves."

    elias_rook "And I'll wear it like a badge.' (he wipes his hands on his pants and looks up) 'You did the thing no one thought we'd have the patience for."
    "The two of you trade small, low jokes—familiar language now. It's easy to forget how enormous the months were until you feel the damp of your hands and the ache in your shoulders. The intimacy is"
    "not only a stealing of private moments; it's stitched from shared labor, from the hours of argument and the midnight calls when a storm threatened a tender transplant."
    show kira_tseng at center:
        zoom 0.7

    kira_tseng "Alright—enough horticulture. Someone stole the playlist at the plaza and everyone's complaining."

    ayla_moreno "Then we better give them something to complain about—harvest pies, maybe."

    kira_tseng "You'd make a terrible politician and a perfect baker."

    ayla_moreno "I'll take that as a compliment."

    menu:
        "Stay and catalogue the seed inventory":
            "You cross items off the list, precise and careful, feeling the authority of small, exact things—counts that keep the patches alive."
        "Go with Kira to the plaza and help set up the harvest table":
            "You grab a crate and head out into the evening; the world is wet and bright and full of people waiting to see what you built."

    # --- merge ---
    "The evening unfolds with communal work and celebration either way."
    # [/INTERACTION]
    # [Scene: Harbor Pier / Restored Coir Mattresses | Low Tide]
    hide elias_rook
    hide ayla_moreno
    hide kira_tseng

    scene bg ch12_f99e88_6 at full_bg
    # play music "music_placeholder"  # [Music: Rhythm of flutes and hand percussion—ancestral, grounding]
    # play sound "sfx_placeholder"  # [Sound: The rope creak, Mateo's quiet humming, water lapping]
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "Feels good to be back. The sea isn't kinder, but we learned how to lean into it."
    show ayla_moreno at right:
        zoom 0.7

    ayla_moreno "We learned how to build with it, not against it."

    mateo_alvarez "Your grandmother would've liked that.' (he taps a spot on the pier) 'She'd say, 'Remember the kind of plant that can take a slap of brine and keep on singing.'"
    "You: (you run your hand through the coir—it's rough and warm) 'That's why we stitched the salt-tolerant grasses into the first line. They hold the soil and make room for the smaller things.'"
    "He looks at you with the patient, private respect elders give to those who carried a memory forward into action."

    mateo_alvarez "This will keep the pier for kids to fish from. Not everything's for sale."
    "You feel the small, bright ache of that sentence—validation that the work you did mattered in a way that outlasts contracts and renderings."
    # [Scene: Twilight Festival Plaza | Evening]
    hide mateo_alvarez
    hide ayla_moreno

    scene bg ch12_f99e88_7 at full_bg
    # play music "music_placeholder"  # [Music: Jubilant, communal—hand drums, violins, a chorus of voices clapping in time]
    # play sound "sfx_placeholder"  # [Sound: Cheers, the pop of a cork, a child's delighted squeal as they find a pocket of puddle water]
    "You walk the plaza and know faces: volunteers with soil-streaked cheeks, councilmembers who voted for the covenant, elders who came back to fish, teens who plastered posters. There is a hum of relief that is almost audible—conversations overlapping in a glad, noisy braid."
    "Elias Rook finds you by the edge of the crowd, hands stained and smile wide, and he squeezes your shoulder in a private kind of celebration."
    show elias_rook at left:
        zoom 0.7

    elias_rook "Look at this. You did it."
    show ayla_moreno at right:
        zoom 0.7

    ayla_moreno "We did it. Not all, but enough."
    "Kira Tseng climbs the stage and looks out at the crowd. For a beat you worry she'll tear into the compromise again; instead, she raises a jar of preserves."
    show kira_tseng at center:
        zoom 0.7

    kira_tseng "For the fights ahead and the ones we've won. To stubborn roots and stubborn people."
    "The plaza echoes the toast. You raise your own cup and let something like a laugh spill out—ridiculously loud and entirely free. The arousal peaks here: months of toil culminating in this communal noise, this Gaelic,"
    "messy chorus of people who chose to keep a piece of their city for actual living things."
    "Elias Rook takes your hand—callused, warm—and tucks the torn seed packet—now safely inside your notebook—into your palm. His fingers linger on yours, a soft precinct against the world."

    elias_rook "We'll plant more. We'll make room for new things and remember the ones we lost."

    ayla_moreno "I'd plant the whole city if we could."
    "He laughs, breathless, and leans in—narrow, faithful. The kiss is not the sweeping, cinematic closure of fairy tales; it is brief and damp with the evening air, salted with work, and entirely honest."
    "You pull back and look at the crowd—faces lit by bulbs, wet streets reflecting the glow, a seawall standing off beyond the harbor in silhouette, limited and bounded by agreements you helped shape. It is an imperfect horizon, but it is a horizon nonetheless."
    hide elias_rook
    show mayor_serena_okoye at left:
        zoom 0.7

    mayor_serena_okoye "You held them together when it mattered. Thank you."

    ayla_moreno "We held each other. That mattered more."
    hide ayla_moreno
    hide kira_tseng
    hide mayor_serena_okoye

    scene bg ch12_f99e88_8 at full_bg
    # play music "music_placeholder"  # [Music: Sweeping, triumphant strings; a low choir that suggests ongoing work and deep roots]
    # play sound "sfx_placeholder"  # [Sound: The plaza's murmur softening into contented conversations; far-off sea]
    "You let the harvest sit in your chest like a warm stone. The victory is messy—some plots are gone, some promenades stand where gardens once were—but the covenant keeps the roofs and greenhouses that feed neighborhoods"
    "and teach children tides and seeds. The work ahead will be long and complicated, but tonight you taste something very close to closure: a tender, compromised joy that refuses to be diminished."
    "You press your thumb against the glass vial at your throat, feeling the smooth curve of saved seeds. Elias Rook squeezes your fingers once, a small, private promise."
    show elias_rook at left:
        zoom 0.7

    elias_rook "Stay. Help me with the next phase of models. Or don't—stay here and keep the roots deep. Either way, I'm with you."
    "You consider the handful of futures at your feet—policy and pottery, algorithms and compost. You choose not to make a speech about love or duty. Instead you turn yourself back to the crowd, to the plates"
    "of pie, to the board where children have scrawled what they want their harbor to be."
    "You laugh again, and the sound is part of the festival now—part cheer, part exhausted relief. The city has been altered by compromise, yes, but not destroyed. You made pockets of living resistance sturdy enough to hold the tide."
    hide elias_rook

    scene bg ch12_f99e88_9 at full_bg
    # play music "music_placeholder"  # [Music: A single, sustained violin note resolving into a warm silence]
    "You breathe in the smell of rosemary and sea salt and know, in a way you didn't before, that contracts can be soil if you bury the right things in them: community, care, and the stubborn intention to make life grow."
    # play music "music_placeholder"  # [Music: Fade to quiet, leaving a single soft chord]

    scene bg ch12_f99e88_10 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant gull; soft applause]

    scene bg ch12_f99e88_11 at full_bg
    "THE END"
    # [GAME END]
    return
