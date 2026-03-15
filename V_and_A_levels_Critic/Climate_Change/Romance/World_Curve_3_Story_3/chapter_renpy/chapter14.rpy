label chapter14:

    # [Scene: Community Center | Morning — Rain-scrubbed light]

    scene bg ch12_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Driving strings, bright brass swells; percussion like marching boots]
    # play sound "sfx_placeholder"  # [Sound: A moderator's gavel, a murmur that snaps into focused silence]
    "Narration:"
    "You arrive with mud on your boots and the Moleskine folded inside your jacket. The notice from the state regulator is pinned to the meeting agenda like a flare: formal review initiated. The room exhales around"
    "you—relief, a new kind of pressure, and a dozen things that must happen in sequence and simultaneously."
    "Mayor Rosa stands at the podium, palms steady on the lectern. Lupe moves through the crowd with a stack of forms and a grin that looks like action. Ava touches your sleeve and for a heartbeat"
    "you simply feel the warmth of someone who stayed up nights turning numbers into answers."
    show mayor_rosa_santiago at left:
        zoom 0.7

    mayor_rosa_santiago "The review is public. Elias' firm will present their revised assessment in two weeks. The regulator has added environmental compliance benchmarks and our community representatives will sit on the oversight panel."
    "Narration:"
    "Applause cracks the room—small, fierce. You feel the arousal like a tide: not a panic but a surge. This is high, this is now. The stakes have shifted into daylight."
    show ava_kim at right:
        zoom 0.7

    ava_kim "We can put together the audit addendum. Cross-reference sediment transport, fish-trawl timing, the mitigation plan—I'll run the models overnight."
    show maia_rivera at center:
        zoom 0.7

    maia_rivera "And we'll ask for community seats on the review board. No rubber-stamp approvals."
    hide mayor_rosa_santiago
    show lupe_kade at left:
        zoom 0.7

    lupe_kade "I'll design the compensation plan. Short-term payouts for lost catch and a priority hiring list for the pilot projects. People need bread now, not promises."
    hide ava_kim
    show dana_park at right:
        zoom 0.7

    dana_park "We channel the energy—vigils were good, but now we file, we watch, we make the contractor's schedule public. Pressure with a plan."
    "Narration:"
    "Your chest tightens, then settles into a focused burn. The emotion is clean: you led a pause that rewrote the late-night deals into a shared process. That doesn't make it easy. It makes it real."
    hide maia_rivera
    hide lupe_kade
    hide dana_park

    scene bg ch12_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rustle of paper; Elias clears his throat]
    show elias_wren at left:
        zoom 0.7

    elias_wren "Maia. The firm will comply with the review. We'll publish the revised impact assessment, and we'll incorporate community feedback into the mitigation schedule."
    show maia_rivera at right:
        zoom 0.7

    maia_rivera "Public revisions. Transparent methodology. Community seats. Those are the terms."

    elias_wren "Agreed. And—' (his voice softens in a way that surprises you) '—I want to make sure the fishermen have a role in the design, Maia. I don't know this town like you do. I want to learn."
    "Narration:"
    "His steel-gray eyes loosen just enough to admit hesitation. The arousal spikes—hope braided with wariness. This is not a surrender; it's the first visible bend in a hardened line."
    show jonah_kade at center:
        zoom 0.7

    jonah_kade "If we're going to work with them, there has to be oversight. No sneaky clauses. Lupe, you handle the books; Maia and Ava, you handle the science. I'll bring the cooperative to the table."

    maia_rivera "We keep an independent auditor on retainer and a community liaison with veto power on deployment timelines."

    jonah_kade "Then I'll back it. But Maia—don't let them pass what we can't reverse."
    "Narration:"
    "The room cracks into plans: volunteer rotas, audit timelines, a provisional schedule for pilot engineering that must meet the new environmental constraints. Voices overlap, fast and purposeful—this is a chorus of the town pushing forward."

    menu:
        "Sign up for the wetlands shift":
            "You put your name on Lupe's clipboard, feeling the immediate, urgent satisfaction of action."
        "Stay and draft the oversight criteria with Ava":
            "You pull Ava aside and start writing the terms for community seats and data transparency on a stray napkin."

    # --- merge ---
    "Continue to the next scene."
    # [Scene: Marisol Wetland Reserve | Noon — High tide rolling in, cloud-teased light]
    hide elias_wren
    hide maia_rivera
    hide jonah_kade

    scene bg ch12_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Shovels hitting peat, calls across the water, gulls keening]
    # play music "music_placeholder"  # [Music: Fast-tempo strings layered with rhythmic hand drums; the pace is relentless and bright]
    "Narration:"
    "The wetland is a cathedral of grunts and laughter. Hands are scrubbed raw, faces flecked with silt. Mayor Rosa kneels between two volunteers, Lupe hands out vouchers and a promise of priority hiring, Ava runs a"
    "handheld sensor and shouts data up over the work. Dana organizes a human chain for transporting native reeds, turning fire into choreography."
    show ava_kim at left:
        zoom 0.7

    ava_kim "Sediment consolidation at sector C is better than the model predicted. If we integrate these living breakwaters with the pilot engineering arrays, we can reduce erosion by another fifteen percent."
    show maia_rivera at right:
        zoom 0.7

    maia_rivera "We keep the living systems primary. Structures supplement, not replace."
    show elias_wren at center:
        zoom 0.7

    elias_wren "I never thought I'd be knee-deep in this kind of mud."

    maia_rivera "Most engineers don't. They design from above. This town builds from below."
    "Narration:"
    "He looks at you—an inquisitive angle. The thaw is happening not with speeches but with blisters and shared stain. You find yourself arguing less, listening more. When Elias admits a misread in his initial assessment—an underestimate"
    "of tidal scouring—you don't savor it as victory. You mark it as a correction and file it under 'work to do.'"
    hide ava_kim
    show jonah_kade at left:
        zoom 0.7

    jonah_kade "Pass that over. We'll use them to anchor the mats. If we get this right, the net migration will have places to rest."
    hide maia_rivera
    show lupe_kade at right:
        zoom 0.7

    lupe_kade "Grant paperwork is progressing—Mayor Rosa is finalizing a cooperative fund. It'll stretch, but it prioritizes hires from the cooperative and funds the apprenticeship program."
    hide elias_wren
    show mayor_rosa_santiago at center:
        zoom 0.7

    mayor_rosa_santiago "Compensation payouts begin next week. Community oversight training starts Monday. We hold everyone accountable."
    "Narration:"
    "The pace is breathless—intense and communal. You taste salt and iron, hear the laughter that follows exhaustion. This is very high arousal—more like a successful sprint than a slow campaign."

    menu:
        "Pull Elias aside to ask about the revisions":
            "You take him by the sleeve. He listens as you point at the map, and the conversation stays practical—data, timelines, the human costs. He answers with fewer defenses and more questions."
        "Help Lupe teach a volunteer how to catalog damage claims":
            "You crouch and show a trembling fisherman how to mark affected traps. He tells you about his grandmother's boathouse. You take notes, your hand steady."

    # --- merge ---
    "Continue to the next scene."
    # [Scene: Community Center | Evening — The projection screen shows revised schematics; the regulator's badge glows on the corner of the slide]
    hide jonah_kade
    hide lupe_kade
    hide mayor_rosa_santiago

    scene bg ch12_e67f19_4 at full_bg
    # play music "music_placeholder"  # [Music: Crescendo into hopeful horns and layered strings; the rhythm is triumphant but earnest]
    # play sound "sfx_placeholder"  # [Sound: Applause, a few scattered tears, a cork pop in the back, a single sustained drum roll as the regulator's spokesperson finishes]
    "Narration:"
    "The public revision is not theatrical. It's procedural, messy, and beautiful. Elias presents the updated impact assessment—methodology transparent, uncertainty bands wider, mitigation commitments spelled out. Mayor Rosa frames the cooperatively negotiated grant: jobs prioritized, funds disbursed in tranches contingent on environmental checkpoints."

    "Regulator Spokesperson" "The firm has agreed to a public revision. The oversight panel will include town representatives. Benchmarks are enforceable. We will monitor and report monthly."
    "Narration:"
    "When Elias says, 'We underestimated the community knowledge and overestimated our control,' a hush passes—then applause that feels like forgiveness deferred but possible. He steps down, and the way his shoulders lower is something you haven't seen: a man unarmored by certainty."
    show elias_wren at left:
        zoom 0.7

    elias_wren "I was wrong on assumptions. I see that now, and I owe that to the work you all did. If the firm made the first mistake, we will fix it publicly."
    show maia_rivera at right:
        zoom 0.7

    maia_rivera "Make it right. Let the oversight be real. Let data be public. Let people keep their voice."

    elias_wren "Agreed. And Maia—' (he hesitates) '—thank you for not turning this into a show of blame. That would have cost more than any grant."
    "Narration:"
    "Something clicks—a recognition that truth doesn't have to be a blade. You feel your old reflexes—guilt, the urge to push the town into righteousness at any cost—soften into something steadier: stewardship balanced with care."
    show jonah_kade at center:
        zoom 0.7

    jonah_kade "You did good, Maia. We did it together."

    maia_rivera "We kept the channel open. That's what matters."
    hide elias_wren
    show lupe_kade at left:
        zoom 0.7

    lupe_kade "And the compensation spreadsheet survived. That's practically a miracle."
    hide maia_rivera
    show dana_park at right:
        zoom 0.7

    dana_park "Now we make sure the firm sticks to it. No rest until the checks clear and the hiring lines form."
    hide jonah_kade
    show ava_kim at center:
        zoom 0.7

    ava_kim "I've set up the audit pipeline and the public dashboard. Transparency is a verb now."
    "Narration:"
    "Night falls. The center empties slowly, hands and bodies exhausted and humming with relief. The model you've built—hybrid, accountable, rooted in living systems and responsible engineering—feels like an imperfect victory: funds delayed; some losses accepted; jobs retooled; dignity intact."
    # [Scene: Marisol Wetland Reserve | Night — Lanterns strung along the boardwalk; the tide murmurs against new breakwaters]
    hide lupe_kade
    hide dana_park
    hide ava_kim

    scene bg ch12_e67f19_5 at full_bg
    # play music "music_placeholder"  # [Music: Solo violin with soft percussion; undercurrent of shared laughter and quiet conversations]
    # play sound "sfx_placeholder"  # [Sound: The wave-sigh, the crackle of the fire, distant town bells]
    "Narration:"
    "You sit, fingers ink-smudged and finally clean, the Moleskine on your lap. The day has eroded something inside you—the rigid certainty that everything had to be saved at all costs—and in its place sits something quieter and sturdier."
    show elias_wren at left:
        zoom 0.7

    elias_wren "We have so much to do, Maia. I wanted to be a savior and instead I learned to listen. That won't be easy to keep."
    show maia_rivera at right:
        zoom 0.7

    maia_rivera "Listening isn't passive. It's work. But I can teach you the difference between a pilot and a promise."

    elias_wren "And maybe you can teach me when to let engineering follow the marsh, not lead it."
    "Narration:"
    "Jonah watches the exchange without comment, his expression unreadable and complex—respect, relief, an old tension eased. He pats your knee as he stands to fetch another log for the fire. The gesture is small and steady, like how he loves: practical, present, and cautious in its tenderness."
    show jonah_kade at center:
        zoom 0.7

    jonah_kade "Tomorrow we start the oversight training. I'll bring the crew. Maia—if you need me there, I'll be there."

    maia_rivera "I'll need you."
    "Narration:"
    "The conversation rolls like the tide—honest, slow, warm. The romance threads aren't tied into a neat bow. They are rewoven into something more durable: trust negotiated in the open, respect earned through labor, and the possibility of something that survives storms."
    hide elias_wren
    show ava_kim at left:
        zoom 0.7

    ava_kim "People will grieve what they lost. We can't fix that. But we can slow the next storm's hunger."

    maia_rivera "That's all any of us can promise."
    "Narration:"
    "You close the Moleskine—pages filled with tide maps, meeting notes, sketches of living breakwaters, and lists of names. Your hands smell faintly of rosemary and mud; your chest is quieter, the knot of guilt loosened into a muscle you can live with."
    hide maia_rivera
    hide jonah_kade
    hide ava_kim

    scene bg ch12_e67f19_6 at full_bg
    # play music "music_placeholder"  # [Music: A hopeful chord that resolves slowly; a choir-like hum underneath]
    "Narration:"
    "It is not a triumph without cost. Funds were delayed, some families tightened their belts, and not every shoreline will be reclaimed. But the model is real now: transparent, accountable, and replicable. You have turned truth"
    "into infrastructure rather than ammunition. The town has seats at the table, jobs that will train a new generation, and a shoreline that will be more resilient because people built it themselves."
    show elias_wren at left:
        zoom 0.7

    elias_wren "Maia—thank you. For pushing when it mattered, and for tempering the push with kindness."
    show maia_rivera at right:
        zoom 0.7

    maia_rivera "Thank you for listening."
    "Narration:"
    "You tuck the Moleskine back into your jacket. The night is soft. Tomas' stories will be retold, fishermen will check their nets tomorrow, Lupe will sleep and start again in the morning, Dana will channel tomorrow's march into the oversight committee. The town moves forward as one organism—scarred, awake, mobilized."
    # play music "music_placeholder"  # [Music: Single sustained note fades into gentle ambient ocean sounds]
    hide elias_wren
    hide maia_rivera

    scene bg ch12_e67f19_7 at full_bg
    "Narration:"
    "You stand, shoulders loosening for the first time in months. The braided blue cord on your wrist catches the lantern light. You breathe in salt and rosemary and the honest ache of work well-begun."

    scene bg ch12_e67f19_8 at full_bg
    # play music "music_placeholder"  # [Music: Gentle, hopeful piano; strings like a sunrise]

    scene bg ch12_e67f19_9 at full_bg
    "THE END"
    # [GAME END]
    return
