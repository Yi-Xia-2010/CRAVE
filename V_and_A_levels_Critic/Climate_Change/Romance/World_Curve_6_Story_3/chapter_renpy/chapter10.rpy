label chapter10:

    # [Scene: Research Lighthouse | Midnight]

    scene bg ch10_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Driving, urgent strings with a single hopeful violin line]
    # play sound "sfx_placeholder"  # [Sound: The steady hum of instruments; the soft clack of keys; a faint, distant foghorn]
    "You are awake in a way that removes the possibility of sleep: all of you — mind, memory, obligation — tuned to the same frequency. The lighthouse room smells of wet wool, solder, and over-brewed coffee."
    "Your navy-blue hair is pulled into a tight knot that will leave a crescent of soreness along your scalp by dawn. The field notebook is beside the keyboard, pages weighted open by a paperclip and a"
    "list of sections: contracts, marginal notes, cost models, red flags."
    "Your wristband vibrates against your skin — a thin, private drumbeat — and you check it automatically: a short encrypted message from Tessa, three words and an emoji that is almost a grin. The buzz is a small, human thing in the machine-night. It steadies you."
    "You set your fingers to the keys and begin to parse clauses the way you have learned to parse storms: look for patterns, hidden currents, pressure gradients. Lines of legalese flatten into shapes you can feel:"
    "where incentives leak, where contingencies are buried, where 'guarantees' are and are not actually guaranteed."
    "You think of the day you left Brinehaven to study; you think of the day you came back and found the shoreline different around the places you could not save. Guilt collects like sediment in your"
    "chest — heavy, patient — but tonight it becomes ballast. You are not the same person who watched and waited."

    scene bg ch10_453e40_2 at full_bg
    show dr_saira_ngoma at left:
        zoom 0.7

    dr_saira_ngoma "There. If we run the sensitivity on the construction contingency again with the adjusted labor index — it collapses the projected 'break-even' by nearly half."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Which means the firm's risk buffer is thinner than they claim. And the clause that allows 'adjusted procurement'—"

    dr_saira_ngoma "—lets subcontractors re-price after milestones. It can trigger cost overruns and remove oversight. Whoever wrote that built a back-door."
    "You say nothing at first because words feel like tools that can either carve truth or fracture it. Your fingers hover."

    mira_kestrel "Show me where they hedge on environmental mitigations."

    dr_saira_ngoma "Here and here. Notice the conditional phrasing. 'Contingent upon approved budgets'—meaning the town signs off, then funding shortfalls can delay mitigation, pushing risk back onto residents."

    mira_kestrel "So publicly they're promising sandbags and seawalls, privately they're building exit clauses."

    dr_saira_ngoma "Precisely."
    # play sound "sfx_placeholder"  # [Sound: Your wristband vibrates again; a different tone — not Tessa, not Dr. Saira]
    hide dr_saira_ngoma
    hide mira_kestrel

    scene bg ch10_453e40_3 at full_bg
    "You pick up."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "How bad?"
    "You can hear the harbor behind him — gulls, the clank of netting. His voice is a hearth."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Worse than they'd told Lynette in the packet. Not necessarily fatal — but structured so the town takes most of the risk."

    jonah_reyes "Then let's make them see it. You publish, you take the heat — we'll be right behind you."

    mira_kestrel "Jonah, I don't want to drag you into—"

    jonah_reyes "You already did. I chose. You choose. We do the hard thing together. Not everyone will like it, Mira, but I'm with you."
    "There is a brief silence at the other end, the kind that carries the weight of a promise. Your chest unclenches a fraction. The thought of his amber warmth beside you — not always agreeing but steady — steadies your fingers again."
    show dr_saira_ngoma at center:
        zoom 0.7

    dr_saira_ngoma "Tessa's pulled together the FOIA requests and the ledger crosswalk. She can get the procurement history into a readable thread. We just need the narrative and the redlines."
    hide jonah_reyes
    show tessa_kestrel at left:
        zoom 0.7

    tessa_kestrel "I already labeled the sensitive sections and wrote the lay summary. People will understand this."
    "You glance at Tessa; she's younger and furious with hope. There is urgency in the tilt of her shoulders. She smells faintly of sea-spray and the lemon soap you keep in the lab sink. You feel protective and afraid in the same breath."

    menu:
        "Proofread the lay summary one more time":
            "You take the document back, scanning every sentence for a place a lawyer might hide a loophole, feeling the tautness of the night. Tessa watches you, both anxious and relieved that you care enough to check."
        "Trust Tessa's summary and prep the release":
            "You hand the summary back and pivot to the upload. Tessa grins, mischief and pride, and Dr. Saira starts packaging the charts. The night sharpens into momentum."

    # --- merge ---
    "You choose — briefly — to let the team choose the rhythm of work. The lighthouse becomes an engine room: charts converted to infographics, legalese translated into clear human stakes, a threaded narrative that shows how costs, timelines, and clauses interlock to shift risk."
    "Midnight becomes 2 a.m., then 3 a.m. The wet glass outside reflects a single lighthouse lamp and the occasional wash of brakes from a passing car; inside, the world contracts to screens and the quiet chorus of urgency."
    "Your wristband vibrates again. The message preview is short and formal: a Caller ID flagged you a 'Request for Clarification' from 'Cassian Romano — Firm.' Your pulse quickens — Cass's steel-gray eyes have looked at you"
    "before with something that meant more than professional friction. Now his voice over the phone will be a thermometer for his trust."
    "You answer."
    hide mira_kestrel
    show cassian_cass_romano at right:
        zoom 0.7

    cassian_cass_romano "Mira. I heard about the thread. I… I saw some of the numbers. Is there a mistake?"
    hide dr_saira_ngoma
    show mira_kestrel at center:
        zoom 0.7

    mira_kestrel "No. There's no arithmetic mistake. There's a pattern. Your contract contains a clause that undermines mitigation timelines and lets procurement change hands without municipal oversight. It shifts risk."

    cassian_cass_romano "That can't be the intent. Those clauses are standard. They protect the firm in volatile supply chains."

    mira_kestrel "And they protect up-front profits under the guise of flexibility. They expose the town to delayed mitigations and erode community control."

    cassian_cass_romano "If that's how it reads, we can change it. We can amend the language."

    mira_kestrel "Then do it now. Show us redlined edits. Put public assurances in writing with penalties that bind the contractor, not just the town."

    cassian_cass_romano "This is fast. If you go public before we have a formal amendment, you put the project at risk. I don't want to see any of the protections —"

    mira_kestrel "I don't want to see smoke-and-mirrors, Cass. Transparency isn't a threat; it's a requirement. The town deserves to know what they're signing."

    cassian_cass_romano "I believed in process, Mira. I believed process could protect us. If you think going public is the only way to hold people to account—"

    mira_kestrel "I'm doing it because we need the town to decide with eyes open. If we wait for your firm's good faith, we risk the delay that costs people their homes."

    cassian_cass_romano "And you'll accept the fallout if the funding collapses?"

    mira_kestrel "I would rather tear a system open than let it be repaired in secret."
    "Silence. The call clicks off. You are left with the echo of his hurt — precise, compact — and the clang of inevitability."
    hide tessa_kestrel
    show dr_saira_ngoma at left:
        zoom 0.7

    dr_saira_ngoma "He's offering a chance to fix it. That doesn't negate the need to publish."

    mira_kestrel "No. It doesn't."
    # play sound "sfx_placeholder"  # [Sound: A distant door creaks; Old Man Rafi's voice, deeper than the rain, carrying up the spiral stairs]
    hide cassian_cass_romano
    show old_man_rafi at right:
        zoom 0.7

    old_man_rafi "Truth moves like the tide, girl. Slow in its grinding, but relentless. Let it have its course."

    mira_kestrel "Is it cruel to pull the rope and let the tide change sooner than some expect?"

    old_man_rafi "Sometimes the sea is kinder when you warn it. Sometimes folks need to feel the wind before they fix the sail."
    "You nod. The metaphor lands like a small buoy of certainty. You are not naïve about consequences; you are choosing the harm of revelation over the harm of deceit."
    # [Scene: Research Lighthouse | Pre-Dawn]
    # play music "music_placeholder"  # [Music: Crescendo with an urgent trumpet and quickening strings]
    hide mira_kestrel
    hide dr_saira_ngoma
    hide old_man_rafi

    scene bg ch10_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Your laptop sending the final packet; an electronic 'send' like a bell]
    "Tessa runs the final check. Dr. Saira stabilizes the server upload. Jonah Reyes sits in the corner, boots propped, fists unclenched for the first time in hours."
    show tessa_kestrel at left:
        zoom 0.7

    tessa_kestrel "Everything's packaged. Dossier, redlines, FOIA documents, an annotated timeline. We have an accessible summary and a downloadable dataset."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "We include the clause highlights, the cost discrepancy charts, the timeline of procurement. We press it to the municipal server and to the regional press list."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "And we stage release at Municipal Hall at first light. People will be there."
    "You feel the readiness in the team as a physical thing — a tension that wants to be put into motion. Your heart drags upward into your throat with the knowledge that the next keystroke will turn private unease into public conversation."

    mira_kestrel "When I hit publish, we are accountable for the aftermath. For the anger and for the relief. Are we still doing this?"
    hide tessa_kestrel
    show dr_saira_ngoma at left:
        zoom 0.7

    dr_saira_ngoma "Yes."
    hide mira_kestrel
    show tessa_kestrel at right:
        zoom 0.7

    tessa_kestrel "Yes."

    jonah_reyes "Yes."
    "You rest your fingers on the trackpad. The cursor blinks like a held breath."

    menu:
        "Pause and call Mayor Lynette before publishing":
            "You lift your phone, debating protocol vs morality. The idea of giving the mayor a heads-up feels like an act of respect, but it also risks preemptive dampening. Your hand shakes a fraction, then settles."
        "Publish immediately and let public scrutiny compel the hall to act":
            "You press send. The dossier leaves your machine and rides the network into the town's inboxes. There's no time to second-guess; only motion now."

    # --- merge ---
    "The room narrows to the blue-white light of the screen. Your coral pendant presses into your sternum. You breathe, inhale the salt-edge of late-night air, and tap the key."
    # play sound "sfx_placeholder"  # [Sound: A clear, absurdly loud click as the file sends — then an almost immediate chorus: message alerts, the ping of emails, a ringing line from an unknown number]
    # play music "music_placeholder"  # [Music: Surge to maximal intensity with a hopeful major chord]
    # [Scene: Municipal Hall | Dawn]
    hide jonah_reyes
    hide dr_saira_ngoma
    hide tessa_kestrel

    scene bg ch10_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A swell of conversation like surf; the press a bass undertow; the rumble of a municipal PA system booting]
    "You arrive with the team, your hair loosening into a halo of damp waves, your field notebook in hand. Mayor Lynette is at the entrance, a tablet in her hand, eyes bright with that particular look politicians get when they feel the wind shift."
    show mayor_lynette_cole at left:
        zoom 0.7

    mayor_lynette_cole "Mira—this is explosive. You could have—"
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "I could have waited. I chose not to."

    mayor_lynette_cole "Do you understand the funding ramifications? The state bond will delay if there's litigation. We lose leverage."

    mira_kestrel "We lose leverage if the town doesn't know what it's signing. That's the point, Lynette. Transparency gives the people the ability to consent."

    mayor_lynette_cole "The optics—"

    mira_kestrel "—are the point. The town decides with eyes open, or the town is decided for."
    "There are murmurs from the crowd: relief, anger, the low, keening sound of people unlatched from the unknown."
    "Old Man Rafi steps forward, cane tapping, voice like a bell."
    show old_man_rafi at center:
        zoom 0.7

    old_man_rafi "We have weathered storms with our hands. If the sea's changed the rules, we have to change our talk. Let there be no more back rooms."
    "A woman in the front row begins to cry; a man shouts about lost winters and better outsized promises. Dr. Saira moves through the crowd, handing out printed summaries, answering technical questions with steady warmth. Tessa stands beside you, face bright and unreadable for a moment, then mourning and fierce."
    "And then the town roars."
    "Not unanimous. Not clean. A polyphony: cheers from those long suspicious of outside deals; curses from those who fear funding loss; an old woman who calls out the name of her disappeared pier and then asks"
    "practical questions about relocation; teenagers who chant for accountability. The sound is a tidal force that lifts and rakes and leaves everything rearranged."
    "Jonah Reyes squeezes your hand, thumb pressing a line of reassurance into your palm. You feel both exultation and an ache as the energy of the crowd wraps you like a new, raw skin."
    # play sound "sfx_placeholder"  # [Sound: The press microphones amplify questions; a dozen phones record; a camera flash stabs like lightning]
    # play music "music_placeholder"  # [Music: High-energy, hopeful fanfare underscored by anxious strings]
    "Cassian 'Cass' Romano watches from the edge of the crowd, the corporate lapel pin nearly invisible in the glare. His face is complex — something between anger, hurt, and a dawning, reluctant respect. You lock eyes"
    "briefly, and in that small space something passes: a recognition that your method challenges his but also that the need to do right is a shared axis."
    "You stand in the center of it and feel — sharply, like wind through bones — the moral clarity you have chosen. You did not choose the easy road. You chose to unmask. Lightness and exhaustion"
    "arrive together: the relief of having aligned your actions with your ethics, the gravity of knowing the next days will be tumult."
    "You sleep poorly that night in a small folding chair at the lighthouse, the dossier open beside you like a map of consequences. When you close your eyes, you see clauses as tides and penalties as"
    "undertows. Yet a new feeling has settled in your chest: something clean and steady that is not guilt. It is the shape of living according to a decision you can explain in the daylight."
    hide mayor_lynette_cole
    hide mira_kestrel
    hide old_man_rafi

    scene bg ch10_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: A quiet, hopeful motif — the violin from earlier, but gentler now]

    "You recheck your wristband. No new messages for a long moment. Then a simple note from Dr. Saira" "Good. Brace for the next wave."
    "You set your notebook against your ribs. You fold your hands. The town is awake now; the conversation has begun. The cost will be high. The risk is real. But the compass point is true."
    "You look toward the horizon, the sea-line scumbled under the waking light, and for the first time in a long time you feel that you are not only naming storms — you are choosing what to do about them."
    # [Scene Transition: The lamp of the Research Lighthouse blinks once; the crowd at Municipal Hall continues to churn; decisions germinate like salt-tolerant shoots]
    # play music "music_placeholder"  # [Music: Fade to an expectant, patient hum]
    "You turn the page of your notebook and listen, waiting for the next necessary move."

    scene bg ch10_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter11
    return
