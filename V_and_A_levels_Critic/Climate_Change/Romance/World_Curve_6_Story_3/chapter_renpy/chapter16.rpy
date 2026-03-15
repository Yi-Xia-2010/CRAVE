label chapter16:

    # [Scene: Municipal Hall | Night]

    scene bg ch14_f99e88_1 at full_bg
    # play music "music_placeholder"  # [Music: A taut, urgent string ostinato; percussion like a heartbeat]
    # play sound "sfx_placeholder"  # [Sound: Camera shutters, murmurs rising into shouts]
    "You press your thumb to the corner of the last PDF and hit send. The cursor blinks and the files fly: contracts with buried clauses, emails with offhand references to “acceptable losses,” spreadsheets that bend cost-benefit"
    "calculations until the margins read like a different language. Your laptop hums; the room till now full of low conversation sharpens into a single, keening frequency."
    "It is not silence. It is the sound of every expectation you have ever carried cracking at once."
    "You feel the coral pendant at your throat warm against skin gone cold. The warmth is private and ridiculous and real. It steadies you for the act — for the refusal to let the ledger be someone else’s secret."

    scene bg ch14_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A phone buzzes, then another; a ringtone like a small alarm]
    show mayor_lynette_cole at left:
        zoom 0.7

    mayor_lynette_cole "Mira — you say you published — is this—?"

    "You do not answer immediately. Speech feels insufficient; the files themselves are the answer, raw and glaring. You watch screens feed lines from the emails" "acceptable collateral,' 'expedite, regardless of cultural impact,' 'reserve right to reassign funds."
    show old_man_rafi at right:
        zoom 0.7

    old_man_rafi "They put a price on our names. They priced the graves, Mira."
    show mira_kestrel at center:
        zoom 0.7

    mira_kestrel "They hid the price in numbers. They made it look tidy. So I put the numbers back where everyone can see them."
    "The first exclamation is like a struck bell. People stand, some shout. Someone in the back hurls a phrase you know has weight — 'resign' — and it lands like a physical thing in the air. The media angle narrows: corruption, cover-up, a town sold the appearance of safety."

    menu:
        "Step forward to the microphone":
            "You step up, breathe with the room, and read excerpts aloud. Each clause sounds worse when said. The crowd listens like people caught in a storm."
        "Let the documents do the talking":
            "You fold your hands on the table and let the files circulate. Reporters pick them up like flotsam; one by one, they lift the story to broadcast. The mayor's composure unravels faster than your speech would have."

    # --- merge ---
    "The main narrative continues."
    "A dozen voices press against you — questions, accusations, demands. Cassian 'Cass' Romano stands to your left like someone in a suit at the edge of a shoreline, wet with his own humiliation. His jaw works."
    "He has the corporate calm of someone trained to absorb impact, but the thin tightness in his throat betrays him."

    "Journalist" "Cassian Romano — your firm is named in these documents. What do you say to the allegation that contractors suppressed viable marsh restoration options because they were 'cost-inefficient'?"
    hide mayor_lynette_cole
    show cassian_cass_romano at left:
        zoom 0.7

    cassian_cass_romano "We advised a range of options. Funding constraints were real. If—if processes were manipulated, I'm—I'm investigating that on my end."
    "You hear the qualifier. You hear the legal scaffolding. You hear shame. He looks at you, and for a beat his steel-gray eyes go something like open, embarrassed apology, searching for a place to begin."
    hide old_man_rafi
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "Investigating? While boats sink and kids lose summer work? While Old Man Rafi has to decide whether to sell his nets? How long will 'investigate' keep us afloat?"
    "He wants blood. He wants a rope to pull someone accountable. His voice is not only for public catharsis; it is grief strung taut. You feel it like a line through you — the personal and the political braided."

    mira_kestrel "Investigations don't fix roofs, Jonah. But they stop more roofs from being sold under us as if their collapse is policy."
    "The mayor's face drains; reporters smell victory. The word 'resign' becomes a chorus, and Mayor Lynette's composure folds like an old map. Her resignation is both a relief and a fresh wound — an easy public answer to a deeper rot."
    hide mira_kestrel
    show mayor_lynette_cole at center:
        zoom 0.7

    mayor_lynette_cole "If stepping down helps the town breathe, I—' (a pause) 'I will submit my resignation."
    "A howl of triumph and accusation spills forward; you flinch as if struck. The arousal in the room becomes a cyclone. Cameras click; the broadcast van is already rolling footage that will be clotted across channels"
    "within the hour. Outside, rain begins in earnest, as if the weather itself is calling witness."
    # [Scene: Boardwalk | Dawn]
    hide cassian_cass_romano
    hide jonah_reyes
    hide mayor_lynette_cole

    scene bg ch14_f99e88_3 at full_bg
    # play music "music_placeholder"  # [Music: Low, pulsing chords; wind through rigging]
    # play sound "sfx_placeholder"  # [Sound: A siren receding, a gull shrieking, the slap of a cable against wood]
    "You walk the boardwalk before the press briefings end. The town wears exhaustion on its shoulders. In public, people are roaring; here, private conversations are like sutures — rough, urgent, necessary."
    show tessa_kestrel at left:
        zoom 0.7

    tessa_kestrel "You did the right thing, Mira. People are crying in the general store. Old Mrs. Pace brought down her quilts to the hall like offerings."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "It isn't enough, Tess. The audit will take months. Money is frozen. Projects stall. People need materials now."
    "Tessa's face darkens — impatience flaring into fear beyond her years."

    tessa_kestrel "They need the money, Miri. They need nets and tarps. They don't all have patience."

    "A man leans from the steps of a boathouse, salt-crusted cap slouched over one eye. He blames you in the softest way" "You broke the pipeline, girl. Now we're on rationed supply."

    menu:
        "Promise to prioritize immediate relief channels":
            "You move to organize a midday inventory and open a community ledger for emergency distribution. You lie awake later, counting tarps and receipts."
        "Insist the audit must complete before funds move":
            "You hold the line — transparency first. Families grumble, some call you idealistic. You spend nights making lists of who goes hungry if the ledger stalls."

    # --- merge ---
    "The narrative continues."
    "Jonah Reyes: (soft, then cutting) 'You could have come to us, Mira. You could've given us a heads-up so we could brace. Instead it's on the news and the town is in panic.'"

    mira_kestrel "And if I hadn't put the files out? If the same people had waved a prettier ribbon next winter and called it progress?"
    "He goes very still. His anger is a constellation of fear for the future and the raw immediate loss of livelihood. For a moment you are sure your chest will split with everything you both feel."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "I trusted you with the town, with us."

    mira_kestrel "You can trust me to tell the truth."
    "The argument spirals—not cataclysmic yet, but sharp, close. It is not only political; it is private, a test of whether a person can hold both loyalty and accountability."

    jonah_reyes "Then don't expect me to make it easy. I'm proud of you and I'm furious with you. Both at once."
    "You both laugh in a way that leaves the salt taste of tears. He steps forward, and for a second you both reach for something like reconciliation. The touch that follows is not a sealing of"
    "vows but a recognition made in hospital wards and emergency rooms — two people who have learned how to calm another's breath."
    # [Scene: Research Lighthouse | Months Later — Over the course of the next year]
    hide tessa_kestrel
    hide mira_kestrel
    hide jonah_reyes

    scene bg ch14_f99e88_4 at full_bg
    # play music "music_placeholder"  # [Music: A grinding, persistent rhythm; mechanical and human]
    # play sound "sfx_placeholder"  # [Sound: The low thrumming of pumps; footsteps on metal stairs]
    "You trade the high adrenaline of scandal for the grinding, bureaucratic work of building structures. Meetings stack like tide marks; minutes are taken, posted, debated. 'Community seats' becomes a phrase as sacred and dull as prayer. Cooperative procurement is a manual of small, precious resistances."
    show dr_saira_ngoma at left:
        zoom 0.7

    dr_saira_ngoma "We will take longer. We'll need to build audits into the process, not bolt them on. Expect snags. Expect legal pushback."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Then we build raggedly, and insist that raggedness be honest. We will keep records open and make the town's voice the first readout."
    "Cassian 'Cass' Romano — bruised professional, quiet ally — shows up more often with technical sketches and spreadsheets that don't hide the messy trade-offs. He brings counsel and models, but he also brings an increasing humility."
    "When he leaves, he lingers by the doorway and rests a hand briefly on your shoulder in a gesture that is not romantic so much as an acknowledgment of shared blame and labor."
    show cassian_cass_romano at center:
        zoom 0.7

    cassian_cass_romano "I was complicit. I didn't lie to you about that. But I can help unmake what I helped build."

    mira_kestrel "Help rebuild — and teach us how to make sure it can't be hidden again."
    "At public meetings, Old Man Rafi teaches younger members to say their names into the record. He insists that oral history accompany ledgers. People take turns at the microphone; someone new to civic engagement stammers through first testimony and leaves with their back straightened."
    hide dr_saira_ngoma
    hide mira_kestrel
    hide cassian_cass_romano

    scene bg ch14_f99e88_5 at full_bg
    # play music "music_placeholder"  # [Music: A strained, hopeful motif that never quite settles]
    "The work is commendable and punishing. Funds are held for review, grants stall in bureaucracy. The structures we create are clean on paper; their implementation is messy. You feel each delay like a bruise on the town's ribs."
    "Then winter comes twice — the second one, heavier and faster than forecasts had promised, tests the coalition in a way paper never could."
    # [Scene: Second Winter Storm Night | Very High Intensity]

    scene bg ch14_f99e88_6 at full_bg
    # play music "music_placeholder"  # [Music: Staccato brass, crashing percussion; no melody — only survival rhythm]
    # play sound "sfx_placeholder"  # [Sound: Sirens, the roar of surf, timber cracking, people shouting]
    "The storm is a beast with teeth. Even with co-ops and community pumps, gaps appear: a procurement delay left a crucial sealing compound unloaded; a volunteer team is short when a truck gets stuck. The open ledger did not make every delivery arrive on time."
    "You stand at the lighthouse, rain cutting at your face, shouting into a radio. Your hands are raw from stringing sandbags. The lighthouse lamps slice the dark like a metronome. There are decisions to make that"
    "will cost: which docks get reinforced with limited crews; whether to send volunteers into flooded alleyways to rescue generators; prioritization becomes triage."
    "Jonah Reyes's voice is in your ear through the static, precise as a metronome. He is leading a wave team, screaming orders. Cass is coordinating a remote salvage crew, his voice small and steady: the engineer's calm in the middle of collapse."
    show cassian_cass_romano at left:
        zoom 0.7

    cassian_cass_romano "We can shore Pier Three with spare pilings stored at the east yard! I know a crew — two hours to mobilize!"
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Do it. Take what you need. Mark it in the ledger as emergency requisition — we'll reconcile after."
    "The laddered roar of the storm takes breath away. In the chaos, a board giving under seawater kills a generator and sends a spray of sparks. A small shack collapses near Old Man Rafi's path; he"
    "stumbles, curses, pulled out of the fall by Jonah and two other hands that are already soaked and shaking."
    show old_man_rafi at center:
        zoom 0.7

    old_man_rafi "I'm not done yet! Not with my stories!"
    "But the storm keeps taking. The town loses boats, the dock fractures, and in one bad, violent instant smoke rises from a shed where stored nets and toolkits ignite from a stray spark. The smell of"
    "burning rope and salt is a physical burn under the nose. People cry and shout and dig with bare hands. You do not stop moving."
    "Some losses are impossible to prevent. A younger fisher you have watched since he was a boy loses a boat in a way that looks like the end of a life you all knew. You hold his hand and feel how sharp grief can be, how immediate, how hot."

    mira_kestrel "We made structures to be moral fortresses. But moral fortresses take time to be strong against a storm's real teeth."
    "Jonah is soaked through; his eyes are hollowed with a grief that has not yet learned words. When at last the wind dies to a wet whisper, the town gathers like creatures counting wounds."
    # [Scene: Aftermath — The Boardwalk | Dawn]
    hide cassian_cass_romano
    hide mira_kestrel
    hide old_man_rafi

    scene bg ch14_f99e88_7 at full_bg
    # play music "music_placeholder"  # [Music: Sparse strings; a low, aching cello]
    # play sound "sfx_placeholder"  # [Sound: People talking in low tones; the distant cry of a gull; the creak of a repaired door]
    "There is a terrible clarity in the morning. The cooperative procurement sprang leaks where the bureaucracy failed to move quickly enough. Families mourn boats and sheds; others breathe because someone prioritized their street's generator and saved"
    "refrigeration for medicines. The ledger is open, each loss and rescue item logged in ink and in the memory of neighbors."
    "Old Man Rafi sits on the dock with a thermos and hands you a small, sodden package — a strip of old rope he saved from the night before. He looks at you, eyes bright as glass."
    show old_man_rafi at left:
        zoom 0.7

    old_man_rafi "You took the scales from the table, Mira. It cost us."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "It did. And we are still here. We can name what we lose."
    "He nods, the little blue bead in his beard catching weak light. Tessa tends to families, jaw set; Jonah organizes salvage crews with a methodical, brittle focus that looks like grief turned to work."
    "Cass stands at a respectful distance, his coat salt-streaked. He doesn't look for absolution. He looks like someone who knows he owes the town an account beyond repair; he gives it anyway: practical help, routing materials, showing up when asked without preface."
    show cassian_cass_romano at center:
        zoom 0.7

    cassian_cass_romano "I will help you build what you wanted — transparently. I don't expect forgiveness. I expect to do the work."

    mira_kestrel "Do it with us, or stand aside. No more hiding."
    "He nods. There is no romance in that exchange: only partnership in the most literal sense — of shoulder to shoulder, ledger to ledger."
    hide old_man_rafi
    hide mira_kestrel
    hide cassian_cass_romano

    scene bg ch14_f99e88_8 at full_bg
    # play music "music_placeholder"  # [Music: A low, repeated motif that is neither triumph nor defeat — only the continued pulse of labor]
    "The federal audit proceeds. Mayor Lynette is gone. The town's governance reshapes into a cooperative organism, slow and legally exacting. It changes things that mattered: procurement is public, community seats have voice and veto power over"
    "aesthetics and allocation, oral histories must accompany impact statements. We win transparency and lose speed. The moral victory is real, and it is bitter."
    "You stand on a cold morning, the coral pendant warm only in the memory of its heat, and feel the weight of everything that cost these changes. The moral clarity that you insisted on is a"
    "sharp-edged thing — it keeps a promise but it also keeps a ledger of names and lost boats."
    "Jonah comes to stand near you without asking. He leans his shoulder against yours in a brief, human punctuation. There is love there, big and messy and unlabeled. There is also the ache of choices that have rearranged futures."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "We did it like we always do — with our hands."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "We did it in a way that makes space for other hands to be heard."
    "He does not press you for answers. He steadies you. The town buffs itself with work and ritual: a bell rung for the lost, a meal shared for the rescued, the ledger crossed and re-crossed with"
    "receipts and apologies and promises. The structures hold enough to keep the community's character, but not enough to keep every storm at bay."
    hide jonah_reyes
    hide mira_kestrel

    scene bg ch14_f99e88_9 at full_bg
    # play music "music_placeholder"  # [Music: A single sustained note that trembles and then settles into low resonance]
    # play sound "sfx_placeholder"  # [Sound: The distant, steady pounding of waves]
    "You close your notebook and slide it into your jacket. You feel, unmistakably, that the truth cost everything — relationships, time, belongings, nights without sleep — but it also seeded something else: a governance that could bear witness and be answered."
    "You do not have a neat romantic resolution. You have a deep bond with one partner who has walked through everything with you, and a new, complicated alliance with another who has taken responsibility in public"
    "and private. The story of love here is less tidy than a ribbon and more like the ledger: multiple entries, some reconciliations, some permanent losses, and an ongoing accounting."
    "You press the pendant to your chest. The cold bites. You breathe in the smell of wet rope and iron and the distant smoke of a repaired hearth. The victory is small on the map but"
    "monstrous in its cost. The town will rebuild under a different logic now — slower, clumsier, more honest."

    scene bg ch14_f99e88_10 at full_bg
    # play music "music_placeholder"  # [Music: A low, mourning choir that fades into a single, resilient note]
    # play sound "sfx_placeholder"  # [Sound: A gull calls; someone in the distance laughs; a child’s feet patter on wet wood]
    "You stand with your coral pendant against the cold and let the weight of that clarity settle. The ledger is open. Names are written in it. Some things were saved. Some things were lost. The town"
    "has found a different future, and you have found, amid the ruins, a moral truth you can live by — even when it is, painfully, not enough to stop the sea."

    scene bg ch14_f99e88_11 at full_bg
    # play music "music_placeholder"  # [Music: A gentle, final toll of a bell]

    scene bg ch14_f99e88_12 at full_bg
    "THE END"
    # [GAME END]
    return
