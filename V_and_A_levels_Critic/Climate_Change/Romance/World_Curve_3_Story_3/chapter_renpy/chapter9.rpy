label chapter9:

    # [Scene: Rooftop Garden of Maia's Childhood House | Night]

    scene bg ch8_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain tapping, a distant roll of thunder, the faint rumor of voices far below]
    # play music "music_placeholder"  # [Music: Rapid, taut strings — a steady, urgent motif building]
    "You have not slept properly in days. The palimpsest of clauses in your Moleskine looks like a tide map drawn wrong: lines written, crossed out, traced again until the ink bleeds into the paper's grain. Each"
    "revision is an attempt to pin the future down with legal language, to make survivable what storms and spreadsheets blur."
    "Your hands smell of coffee and salt. The braided blue cord around your wrist barks against your pulse each time you flip the page."
    show maia_rivera at left:
        zoom 0.7

    maia_rivera "Read the last paragraph again,"
    show ava_kim at right:
        zoom 0.7

    ava_kim "They gave us a line about 'operational flexibility' in the event of 'unforeseen marine conditions,'' (she scrolls through an annotated tablet, eyes narrowed) 'and then they bracketed 'unforeseen' in a way that pushes interpretation toward the contractor."
    "Maia Rivera: (You tap your pen on the paper until the rhythm matches the strings. Interpretation is where power shifts. It's where access becomes control.) 'So tighten 'unforeseen.' Define parameters. Tie change orders to an independent review.'"
    "Ava: (She exhales, sounding both tired and fierce.) 'Independent reviewers, yes. But set the reviewer selection in the contract, Maia. If you leave the selection vague they'll outsource the decision to their firm.'"

    maia_rivera "Two independent reviewers, appointed by a panel that includes cooperative representatives."

    menu:
        "Underline the reviewers' appointment process to make it legally explicit":
            "You draw a thick underline, the ink sinking into the paper with a permanence that feels almost ceremonial."
        "Make a marginal note to revisit the language with legal counsel in the morning":
            "You write 'LAW' in the margin and sleep for the first time in two days, knotting the clause to someone else's steadiness."

    # --- merge ---
    "..."
    "Ava: (She taps the tablet, then looks up at you.) 'If we demand their timeline be extended for these clauses, they'll say we're delaying an emergency deployment. They'll paint us as obstructionists.'"

    maia_rivera "Let them say it."
    hide maia_rivera
    hide ava_kim

    scene bg ch8_6b08b4_2 at full_bg
    "Jonah Kade: (He rubs his chin, thumb tracing the clause where you guaranteed co-op seats.) 'You sure you want the seats to be binding? That's… heavy.'"
    "Maia Rivera: (You feel the map of Marisol in your chest—lines of kin and loss, work and history. Seats at a table are not symbolic here; they're the difference between being consulted and being overridden.) 'Yes. Binding seats. No advisory-only language.'"
    show jonah_kade at left:
        zoom 0.7

    jonah_kade "Binding means fights at the table. Binding means signatures that will be used against us later."
    "Maia Rivera: (You look at him, and under the streetlamp-silver rain his expression is worn but loyal.) 'Binding also means we don't get walked past. It keeps them honest.'"
    "Jonah Kade: (He looks away for a breath, then back.) 'I trust you.' (He doesn't say 'I trust the plan'—he says it to you, and that steadies a new part of you.) 'I trust that you'll keep our nets in the water.'"
    "Maia Rivera: (Your chest tightens in a way that is almost a physical intake of the night air. Trust is not a guarantee; it is a vote.)"

    menu:
        "Ask Jonah to speak for the cooperative at the next council meeting":
            "He hesitates, then nods; 'I'll speak if you want,' he says, and the offer lands like a small oath."
        "Tell Jonah you need him present but not speaking":
            "He gives a half-smile, understanding the nuance; 'I'll be there, on the docks or at the table,' he says, and you let him hold that quiet space."

    # --- merge ---
    "..."
    # [Scene Transition: Rooftop garden light shifts; camera passes through the fog and descends to the Community Center negotiation rooms — fluorescent glare, folding chairs, a long table strewn with printouts]
    # [Scene: Community Center — Negotiation Room | Dawn]
    hide jonah_kade

    scene bg ch8_6b08b4_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The building hums — the heater, murmured voices, the occasional slap of a wet coat on plastic]
    # play music "music_placeholder"  # [Music: Staccato percussion adds to the strings — urgency tightens]
    "Mayor Rosa Santiago: (Hands folded, face composed but lined with the work of this town) 'We have to decide how to proceed today. Contractors expect a start date. The state liaison wants numbers.'"
    show maia_rivera at left:
        zoom 0.7

    maia_rivera "We have drafted clauses that demand—' (you slide the Moleskine and a printed amendment across the table) '—an independent fisheries impact study with pre-agreed reviewers; binding seats for co-ops on the governance board; phased deployment with audit gates."
    "Lupe: (Her voice is brisk; she keeps her hands tight on a stack of payroll projections) 'Look: the cooperative is two weeks from burning through contingency. If infrastructure means steady contracts for fish processing, that's livelihoods. But if it displaces us… no one eats.'"
    "Ava: (She points to a highlighted line on the amendment.) 'Phase one cannot reconfigure fishing grounds without explicit co-op consent. Phase two must be contingent on the fishery audit meeting predetermined biological benchmarks.'"
    "Elias Wren: (He leans forward, neat and composed, his fingers steepled. His team glows on a tablet; LED light washes across his face.) 'Modular phases are reasonable. Audit clauses are fine in principle. But audit gates"
    "introduce delay. The coastal models predict a storm window where deployment must proceed or we risk the very infrastructure we're funding being compromised.'"
    "Maia Rivera: (You can feel every breath in the room as if it were the wind before a wave. The word 'delay' in his sentence is a wedge. You know the time-weather math; you also know what unconditional speed would cost the town.)"
    show elias_wren at right:
        zoom 0.7

    elias_wren "If we agree to your wording with strict selection protocols for reviewers, we can accelerate parallel installation. We are willing to include co-op seats—initially as observer seats—transitioning to voting seats after a 12-month monitoring period."
    "Maia Rivera: (The phrase 'observer seats' slides across the table like an olive branch carved of glass. It glints, but it cuts.)"
    "Mayor Rosa Santiago: (She folds petition papers with the practiced hands of someone who has held many grievances.) 'A phased approach could mean money and protection now. But binding seats… that's a political promise with teeth.'"
    "Dana Park: (She stands at the back, soaked through, a damp protest banner rolled into her arm. Her voice is sharp with a rising public pulse.) 'Binding or bust. If you bargain that away they'll brand us pacifists while they bulldoze the wetlands.'"
    "Lupe: (Her hands are shaking slightly now, not from the cold. She slides a paper toward you — a ledger, rows of numbers dotted with red.) 'We need payroll to be steady. We are not ideologues;"
    "we're a co-op trying to make rent. If observer seats keep our boats afloat while we prove we can hold them in, that matters.'"
    "Maia Rivera: (Your throat thickens. Numbers and ethics braid together here. The town's survival is in spreadsheets and in the slow accretion of trust. You imagine Tomas' hands—callused and blunt—folding the ledger in the same way he folds maps, trying to feel where the faults line up.)"
    # play sound "sfx_placeholder"  # [Sound: A ripple of distant shouts — protesters outside. Someone bangs a metal placard. The building vibrates with it; the sound enters your chest.]
    "Ava: (She meets your eyes.) 'We can push for binding seats right now. We can insist on the selection process for reviewers being explicit. But be honest—if we push too hard we risk Elias walking away.'"

    maia_rivera "If he walks away, the state could step in with a different contractor. Or no action happens, and the storm eats what we tried to protect."

    elias_wren "Maia—' (he uses your name in a way that is meant to be steadying) 'What I'm proposing is a compromise. Modular, phase-gated, with audits. It preserves a timeline while giving your community a governance pathway."
    "Maia Rivera: (Your chest tightens into a knot that translates into a single, sharp clarity: whatever you choose now will be read in years like a map. The sentences you put to paper will be the"
    "contour lines the town follows. You feel the weight of signatures like stones in your palms.)"
    hide maia_rivera
    hide elias_wren

    scene bg ch8_6b08b4_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain turns harder; a metallic rattle as contractors outside shift gear]
    "Mayor Rosa Santiago: (Quiet, decisive) 'Elias, can you guarantee that phase one will not change existing fishing zones unless the co-op expressly agrees? Can you make the co-op seats binding and immediate, not delayed?'"
    "Elias Wren: (He pauses, an almost imperceptible tightening at the edges of his composure.) 'We can make the co-op seats immediate, but they would be limited in scope at the outset to advisory capacities until the"
    "first audit is complete. Full voting rights can be transitioned as the monitoring data supports it.'"
    "Dana Park: (She scoffs softly, but it is a sound that carries.) 'So immediate advisory seats and eventual voting rights when your models deign our work valid. 'Eventual' is a delay wrapped in polite language.'"
    show lupe_kade at left:
        zoom 0.7

    lupe_kade "If eventual means six months and paychecks keep coming, people can weather six months."
    "Maia Rivera: (There is a clock inside you that ticks in different units—ethical seasons, fishing cycles, payroll weeks. Your mouth tastes of metal. You try to measure the human cost of 'eventual' against the cost of 'now'.)"
    "Ava: (Her fingers find a pen. She draws a clause in the margin.) 'We can accept phased deployment if we get three things: explicit reviewer selection language; a no-reconfiguring clause for phase one; and an escrow-funded payroll guarantee should phase one contracts replace co-op income.'"
    "Elias Wren: (He looks at the paper, then at the people around the table.) 'An escrow arrangement is possible, but escrow requires third-party arbitration. That introduces complexity.'"
    "Maia Rivera: (You see the map of consequences unfold, each clause a tributary that feeds riverbeds of future decisions. The room grows smaller as the weather outside grows louder. Your heartbeat is a drum under the legalese.)"
    hide lupe_kade

    scene bg ch8_6b08b4_5 at full_bg
    "Jonah Kade: (Soft, but firm) 'You don't have to agree to something that strips the town's agency.'"
    "Maia Rivera: (Your fingers clench the pen. The ink caught on the nib seems to freeze time.) 'I know.' (You swallow.) 'We have to decide whether the oversight in this compromise is enough to keep our"
    "people safe and our seas livable, or whether it's a shiny half-measure that will be used later to justify exclusion.'"
    "Elias Wren: (He leans in, voice controlled, practical.) 'If you accept the phased compromise with the audit clause, we begin work in weeks and mitigate imminent storm risk. If you reject it, the contract may collapse—and there is no guarantee another firm will step in with comparable resources.'"
    "Maia Rivera: (You can feel the room's breath hitch; the storm outside is a metronome for your decision. Contractors are already mobilizing equipment in the lot; traffic lights blink through sheets of rain. Dana's protest is no longer a background noise; it is a force at the door.)"
    # play music "music_placeholder"  # [Music: All instruments stop for a heartbeat; then a single, insistent drumbeat resumes — the crash building toward a decision]
    "Maia Rivera: (Everything narrows to the margin you've been circling for nights. Every clause you write becomes a promise, or a loophole. You think of Tomas’ stories of tides that took whole years; of Lupe counting"
    "paychecks by candlelight; of Jonah's hands steady at the helm; of Ava's tired, steady stubbornness. Your chest tightens until the next breath is urgent.)"
    # [Page-Turn Thought: The pen over the page becomes a small lever. One phrase will let construction begin in time for a predicted window; another will force pause and the possibility that nothing starts. The storm does not ask for perfect outcomes—only for action. Your next line will decide what kind of action.]
    # [Linear Handoff — Page-Turn Moment]
    "You let the pen hover. The rain is louder now, a hard drumming that presses against the windows like percussion. Outside, metal and tar move under the hands of contractors who could either be your allies"
    "or the town's undoing. Inside, eyes track you—Ava's counsel, Jonah's quiet faith, Lupe's ledger, Dana's protest hunger, Mayor Rosa's weighing hands, Elias' precise patience. The folio waits for ink. The world narrows to the clause."

    scene bg ch8_6b08b4_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter10
    return
