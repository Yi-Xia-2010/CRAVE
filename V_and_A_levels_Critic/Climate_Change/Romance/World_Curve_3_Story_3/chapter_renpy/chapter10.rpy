label chapter10:

    # [Scene: Offshore Project Site | Night]

    scene bg ch9_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Metal groans, diesel throbs, distant gulls cut by wind]
    # play music "music_placeholder"  # [Music: Tense, propulsive percussion building into a driving, hopeful surge]
    "You stand at the edge of the temporary staging area, the salt on your jacket crystallizing under the lights. The modular platforms glitter—iridescent seams stitched into the dark water—each one a promise signed in ink and"
    "compromise. They sit in neat ranks like a new kind of reef: clinical, precise, and impossibly loud against the bay's old rhythms."
    "Your chest is a drum. Every breath tastes of sea and tool-iron. This is what it looked like when things finally moved—fast, bright, unstoppable. Contractors shout in clipped tones; a crane operator's radio crackles with countdowns."
    "The whole machinery of mitigation hums with the kind of efficiency you used to only read about in proposals. It terrifies you and, strangely, steadies you."
    "Elias approaches with a folded map in his hands, edges softened by your fingerprints. He walks differently tonight—no theatrical pause, no salesmanship. Even under the LEDs his face reads smaller, like a person who has traded spectacle for something harder and quieter."
    show elias_wren at left:
        zoom 0.7

    elias_wren "They're lining up the final pylons for tomorrow's low tide. We've got teams scheduled around the clock for the next four days. It will change the flow—but it will also buy time."
    "(You feel the words land like a net—practical, unavoidable.)"
    show maia_rivera at right:
        zoom 0.7

    maia_rivera "Buy time,"

    maia_rivera "We need those windows,' you say. 'But you know—"
    "(He meets your eye. There is an unspoken ledger between you two.)"

    elias_wren "I know what you asked for. The hiring quotas, the community oversight clause, the reparations line we added for lost fishing spots. We built them in."
    "(Relief rushes like an electric line through your ribs. Then something colder settles in—an aftertaste.)"

    maia_rivera "Built in,' you echo. 'And enforced?"
    "(His jaw flexes—a small human fissure in corporate calm.)"

    elias_wren "We did. Contracts are tied to on-site monitors and a joint oversight board. It won't be perfect. But it's in writing."
    "You let that be true for a breath. Paper can be a promise; paper can also be a map of compromise. Your hands curl into the Moleskine in your pack—old vertebrae of your work—and you press your thumb against the worn cover until the skin blanches."

    menu:
        "Thank him with a careful smile":
            "You offer a small, careful smile and he returns it with a flicker that looks almost like permission. The map between you folds quieter."
        "Keep the conversation strictly about logistics":
            "You tilt the map toward the pylons and start ticking off schedules. Elias nods; his hand rests on the paper for a beat longer than necessary, then moves away. The warmth cools into task."

    # --- merge ---
    "The scene continues."
    hide elias_wren
    hide maia_rivera

    scene bg ch9_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The ringing of metal, water lapping at newly driven piles]
    # play music "music_placeholder"  # [Music: Percussion peaks, then underlays with urgent strings]
    "You walk the line where industry meets old harbor—where the wet, barnacled wood of the boardwalk clamps against new steel. The harbor smells of oil and rosemary, of fish and hot metal. Lupe waits at a"
    "temporary tent, a stack of tablets and thermal receipts in her hands. Her face is a taut, triumphant thing: payroll reconciled, accounts rerouted, people paid according to the first revised pay cycles."
    show lupe_kade at left:
        zoom 0.7

    lupe_kade "Maia—payroll's live. First round of transition pay went through at noon. A lot of folks are breathing."
    "(You hear the relief like a bell. You want to let it ring unmolested.)"
    show maia_rivera at right:
        zoom 0.7

    maia_rivera "Thank you. You did the impossible wrangling numbers into hope."
    "(She shrugs, proud and weary.)"

    lupe_kade "You did the talking. I did the spreadsheets. Jonah's been in and out—helping retrofit a couple of skiffs. He looks… stubbornly realistic."
    "(You look toward the docks. Jonah is there, sleeves rolled, hands thick with grease. He helps a younger fisher adjust a new routing transponder. The man moves with the slow certainty of someone who reads the sea like scripture.)"

    maia_rivera "How is he?"
    "(Her eyes flick to Jonah, then away.)"

    lupe_kade "He's taking shifts. Keeps his jaw set. Says the routes will work if folks respect them. He did say—' (she pauses, considering whether to soften) '—he did say that the maps still hold memory, Maia. Folks still talk about the old spots."
    "Jonah's voice carries now—a low bark to a crewman, then softer as he steps toward you, grease on his knuckles like a lineage."
    show jonah_kade at center:
        zoom 0.7

    jonah_kade "Good to see you. We got a hull that needs a brace. If you can spare some of Ava's crew, we'd get it done by dawn."
    "(You feel the pull: a hundred small fixes that stitch lives back together.)"

    maia_rivera "I'll find them. I have a list.' Your fingers curl around the pen in your pocket. 'You all right?"
    "(He gives a half-shrug, that fisherman stoicism you know well. His eyes—sea-glass and storm—are open and raw. He looks like someone who gave up certainty for motion.)"

    jonah_kade "We got jobs. We got training programs. That's a lifeline. But the spots shift. The old run—it's not where it was."
    "(The ache sharpens—ancestral lines wobbling under a new map.)"

    maia_rivera "We accounted for some of that in the reparations plan. Community oversight can redirect research funding to track migratory changes—hire local fishers as monitors. If we do this right—"
    "(He pins you with the kind of honest, bristling honesty you both know. Not accusation; not praise. Just a fact.)"

    jonah_kade "Man, 'if' is a lot of work."
    "(His words land like a hook. There's friction in the air: gratitude braided with grief. You both know sacrifices were made to get here.)"

    menu:
        "Promise to prioritize local monitoring hires":
            "You promise—out loud, binding your mouth to the board. Jonah's shoulders ease a fraction. He nods tightly, then turns back to the skiff with a quiet promise of his own."
        "Ask Jonah to lead the monitoring team":
            "You look at Jonah, offering a responsibility that feels like trust. He blinks as if surprised, then swallows. 'I'll think about it,' he says, and it reads like a yes that hasn't fully formed."

    # --- merge ---
    "The scene continues."
    hide lupe_kade
    hide maia_rivera
    hide jonah_kade

    scene bg ch9_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low, communal hum; a mix of congratulations and muttered grief]
    # play music "music_placeholder"  # [Music: Full orchestra surges—trumpets and strings—then threads through with a lone cello]
    "Word spreads fast. Mayor Rosa convenes an informal gathering on the boardwalk—a short speech, hands on the lectern like someone holding a fragile ledger of community hope."
    show mayor_rosa_santiago at left:
        zoom 0.7

    mayor_rosa_santiago "This wasn't easy,' she says, voice firm with the weight of votes and petitions. 'We chose—imperfectly, with eyes open—to take a step that preserves lives and livelihoods. We will hold them to their promises."
    "(You stand in the audience, the chorus of faces around you minefields of gratitude and reservation. Tomas shuffles up beside you, cane tapping in a rhythm that steadies you more than you deserve.)"
    show tomas_rivera at right:
        zoom 0.7

    tomas_rivera "You did what you could, niña,' he says quietly. He smells of wood smoke and the salt of a hundred afternoons teaching you how tides tell stories. 'This town will remember who kept watch."
    "(For a moment the past folds foldedly into the present. It is enough to make your vision blur.)"
    # [Scene: Harbor Boardwalk | Afternoon]
    hide mayor_rosa_santiago
    hide tomas_rivera

    scene bg ch9_3be532_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Children shouting, tools clinking, a faint radio playing an old sea shanty]
    # play music "music_placeholder"  # [Music: Energetic strings with bright piano—fast, hopeful]
    "The next weeks move like a whitewater. Training programs fill the retrofitted facility; Lupe teaches payroll classes in the mornings and oversees apprenticeship sign-ups in the afternoons. The repair shop hums; new hands learn old knots."
    "Money flows in modestly but reliably, the kind that changes bills into food, nights into small comforts."
    "Yet beneath the motor and the cheer, the town murmurs. Older fishers sit on crates, eyes on the horizon, mouths closed around history."
    "Older Fisher: (muttering) 'We used to read the moon and the smell of mackerel to know where to drop lines. Now the lights tell us where to stand.'"
    "(The mutter is a litany. You catalog the names of losses as reflex: lost spots, altered runs, the cultural maps that don't translate into ledgers. Each is a fissure. Each is true.)"
    "Jonah pulls you aside—brief, private—his callused fingers find yours, a touch more than needed to steady you against a question."
    show jonah_kade at left:
        zoom 0.7

    jonah_kade "You did good work with the oversight stuff,' he says, voice thick with unsaid things. 'You pushed hard. People are eating."
    "(His praise feels like both balm and blade.)"
    show maia_rivera at right:
        zoom 0.7

    maia_rivera "I did what I could,' you answer. 'We did what we could."
    "(He searches your face; the look he gives contains a hundred possible endings—some of them tender, some of them severed.)"

    jonah_kade "Sometimes I think—maybe we could've held more back. Maybe we could have kept more of what was ours."
    "(You want to tell him you understand; that you carry his memory of lost seasons like a stone in your pocket. But the truth thins under the rush of events.)"

    maia_rivera "We traded something to get something. We made a choice together."
    "(A brittle laugh.)"

    jonah_kade "Together. Right."
    hide jonah_kade
    hide maia_rivera

    scene bg ch9_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low tide, distant laughter, a soft thump as someone closes a hatch]
    # play music "music_placeholder"  # [Music: Cello solo—warm, aching, and audacious]
    "Later, Elias finds you on the boardwalk, hands stained with map ink and dust. The chaos of the day has been eroded into a softer conversation, slower and careful."
    show elias_wren at left:
        zoom 0.7

    elias_wren "You negotiated clauses that will bind us,' he says, less an announcement than a confession. 'It made the rollout harder. People will be watching us."
    "(His words land like a promise and a threat rolled into one.)"
    show maia_rivera at right:
        zoom 0.7

    maia_rivera "I didn't give you easy lines,' you say. 'But I knew speed mattered."
    "(He steps closer, folding a map with deliberate care. When his fingers brush yours, it's not theatrical—it's domestic. There is a gravity to that small contact that makes the world tilt.)"

    elias_wren "I didn't expect to learn patience.' (He smiles, small and shy.) 'You taught me how to do that."
    "(Your breath stumbles—hope like quicksilver. There's a current here you almost let yourself follow. The field between you two is complicated and honest: it is policies and late-night edits, but there is also a gentleness that feels like the beginning of trust.)"

    elias_wren "Would you—' He hesitates, uncharacteristically human. '—help me show the board how the oversight works in practice? Your voice carries in ways mine doesn't."
    "(You measure the offer. It's work, and it's intimacy in the only form you trust: shared labor.)"

    maia_rivera "Yes,' you say. 'I'll help."

    menu:
        "Accept his offer with a plan to include local monitors":
            "You nod, already outlining steps in your head—training modules, community liaisons. Elias listens, taking notes as if learning a language for the first time."
        "Insist on a public session led by Tomas and Jonah in addition to your technical briefing":
            "You insist that the story of the bay be told by those who lived it. Elias agrees, a little surprised, but you see relief wash through him at the idea of the town's voice being loud and raw."

    # --- merge ---
    "The scene continues."
    # [Scene: Boardwalk at Dusk | Sunset]
    hide elias_wren
    hide maia_rivera

    scene bg ch9_3be532_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind through grasses, the far-off clang of the project's final adjustments]
    # play music "music_placeholder"  # [Music: Full orchestra—triumphant horns braided with a tender violin line; the tempo quickens to a fever pitch]
    "You stand alone where the lights meet the old wood, chestnut hair loose in a breeze that smells of rosemary and diesel and salt. The town is a series of small, sharp successes stitched together by"
    "long nights and longer arguments. There are jobs, a cleaner harbor, and an infrastructure that has already dampened the bite of seasonal storms. People sleep a little easier; children's laughter returns to corners of the quay."
    "But the loss hums, a low, honest undertow. You can hear it in the way older fishers walk with slightly different steps, in the muted pride of a dock that once sang with knowledge now charted"
    "in corporate schematics. You negotiated reparations and local hiring quotas. You insisted on oversight. You fought for community control even as some authority slipped away—to speed, to funding, to safety."
    show tomas_rivera at left:
        zoom 0.7

    tomas_rivera "You stitched a blanket from scraps, niña,' he says. 'It won't be as warm as the old quilts—some threads are missing. But it will keep us alive."
    "(You close your eyes and pour everything into that sentence—relief, grief, the fevered rush of nights where you chose words like tools.)"
    show maia_rivera at right:
        zoom 0.7

    maia_rivera "It will keep us alive,"
    "(Elias walks up slowly, giving space—an understanding earned through clauses and late negotiations. He presents you with one final folded map, edges softened by use. There’s a gentleness in his movement that feels like an offering.)"
    show elias_wren at center:
        zoom 0.7

    elias_wren "For when you want to remember what the compromise looked like,' he says. 'To keep track of promises."
    "(You accept it. His fingers brush yours—a small, honest contact that speaks of possibility, of a careful, cautious affection built over arguments and shared labor.)"
    "(Jonah watches from across the harbor, a silhouette that does not move toward you. His figure is complex—support and distance braided together. You read the unreadable in his posture, the way his shoulders carry memory and"
    "new burdens. You want to go to him and also know that the town will call him back to other duties. The relational knot can't be untied with one gesture.)"
    # play music "music_placeholder"  # [Music: Swells—triumph and ache merged into one wave; percussion thrums like a heart at max tempo]
    # play sound "sfx_placeholder"  # [Sound: Distant applause as the oversight board announces its first hire—local monitors sworn in; horns sound quietly from a few boats]
    "You look out at the bay. The newly installed platforms gleam. Gulls wheel. The repaired boats bob in a rhythm that—though altered—still belongs to this place."
    "You have protection now. You have jobs and training and a cleaner harbor. You have oversight clauses and reparations and a town that will argue itself through the next seasons. But parts of the bay's soul—old"
    "maps, certain runs, some private rituals of knowledge—have shifted in ways that are already teaching new generations different languages of survival."
    "Your pulse is a drumbeat that matches the cadence of the night. The very act of deciding, of writing clauses into contracts, of insisting on co-management—even imperfect—was a kind of love. It was for people who"
    "needed roofs, for hands that need to feed mouths, for the neighborhood that had voted by its attendance and petition signatures. It was also an admission that you could not hold everything."
    "You breathe in, the salt-air filling your lungs. Your hands—callused from fieldwork and softer from late-night negotiations—rest over the Moleskine inside your bag. The blue braided cord at your wrist rubs against your skin, an anchor."
    "You think of the boathouse that once was, of Tomas' stories, of Lupe's sharp laugh, of Jonah's steady hands, of Elias' quiet patience. You feel, in the center of it all, a warmth that has the"
    "jagged edges of compromise."
    hide tomas_rivera
    hide maia_rivera
    hide elias_wren

    scene bg ch9_3be532_7 at full_bg
    # play music "music_placeholder"  # [Music: Final swell—a complex chord that resolves into something like peace: bright, bittersweet, and firm]
    "You let the ache settle into your bones and intone a small, private credo: we did not save everything, but we saved enough to keep trying. Enough to hand some hope to tomorrow."

    scene bg ch9_3be532_8 at full_bg
    # play music "music_placeholder"  # [Music: Gentle decrescendo into single piano note]

    scene bg ch9_3be532_9 at full_bg
    "THE END"
    # [GAME END]
    return
