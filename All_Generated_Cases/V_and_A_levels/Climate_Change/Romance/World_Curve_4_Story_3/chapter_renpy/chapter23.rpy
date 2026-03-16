label chapter23:

    # [Scene: The Old Boatyard | Morning]

    scene bg ch13_66a4ee_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Mallet tapping, a rasp of plane against wood, gulls high and thin]
    # play music "music_placeholder"  # [Music: Low, urgent strings — a thread of tension woven through steady percussion]
    "Narration:"
    "You arrive before most of the town. The air is sharp with salt and sawdust, a scent that scrapes like memory. Eli is already there, hands scarred and steady, chipping away at the hull's inner curve."
    "Each stroke sends a small constellation of shavings into the light; each shaving is a clock that remembers other tides."
    show eli_duarte at left:
        zoom 0.7

    eli_duarte "You came early,' he says without looking up, voice sanded by work. 'Figured I'd have to do the hard part before the town hears the speeches."
    "Narration:"
    "His smile is crooked; the work says what words cannot. You step closer, and the wood smells of resin and old weather. The hull's nameplate—once proud and painted—has been sanded away. He keeps the grains of that wood like a litany."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "How are you doing with it?"

    eli_duarte "Depends on the hour."
    "Narration:"
    "He laughs, then quiets."

    eli_duarte "Depends on whether the echo stops in the splintered boards or in me.' He lays the plane down and wipes his hands on his jeans. 'We wanted something to touch. Something to say it's us who kept making here, even when the sea tried to take the sentence away."
    "Narration:"
    "You lay your fingers on the raw curve; the timber is cool, the texture a thousand tiny ridges. Memory presses against the palm of your hand—the small boat on your father's trailer, the last storm that"
    "taught you what to measure. Your compass sits warm under your sweater, an old weight against your sternum."

    eli_duarte "What should we carve? Names? Dates? A sentence?"
    "Narration:"
    "Your chest tightens. Naming feels like claiming loss. Leaving it blank feels like refusing to remember. The choice isn't big—it's ceremonial, almost petty—but right now every small motion carries the town's grief."

    menu:
        "Carve the names and dates":
            "You say the names softly, letting them hang in the air. Eli nods and begins to mark the template, his chisel finding the first rhythm."
        "Leave it as a blank curve—an open wound":
            "You trace the hull's curve with your fingertips and tell Eli to leave it uninscribed, a place for anyone to lay a letter or a shell. He frowns, then hums, smoothing the wood by hand."
        "Carve a short line: 'We tried'":
            "You propose a small, honest line. Eli inhales as if the text will steady him. He taps the chisel twice, then sets the first letters with exact, deliberate strikes."

    # --- merge ---
    "Whatever you decide, Eli accepts it as a kind of law. He sets to work with a rhythm that steadies the morning. People drift by—neighbors bringing coffee, children with splintered rulers. Each arrival alters the hull's"
    "story by presence alone: Aunt Rosa brings a stitch of scarf to tie around the prow; a teenager leaves a faded photograph under a plank."
    "Narration:"
    "Noah stands at the fence, coffee steam ghosting upward. He catches your eye and lifts his mug in a small salute. The gesture is private, an unspoken ledger entry between the two of you: still here, still counted."
    show noah_reyes at center:
        zoom 0.7

    noah_reyes "You thinking of the Promenade plaque?' he asks, voice low. 'Or the lab's list?"

    asha_moreno "Both. And also something that won't let us forget what we refused to sell."

    noah_reyes "Good. We need anchors that are not only legal."
    "Narration:"
    "The boatyard hums on. The hull's new identity takes shape under Eli's hands—a compromise of memory and craft. The town's grieving is tactile here: splinters become offerings; sanding becomes penance. Your guilt is raw and close,"
    "but under the rasp there is purpose. The morning won't forgive you, but it will let you work."
    # [Scene: Floating Market & Raised Gardens | Late Morning]
    hide eli_duarte
    hide asha_moreno
    hide noah_reyes

    scene bg ch13_66a4ee_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Lively chatter, the rattle of seed screens, distant gulls]
    # play music "music_placeholder"  # [Music: Quick, energetic percussion — the tempo of communal labor]
    "Narration:"
    "The gardens are louder than the boatyard. Marta's voice carries across the platforms: a call to attention that feels like a command and a comfort at once. Soil dusts your boots; the heat of bodies pressed together radiates sweeter than the sea wind."
    show marta_chen at left:
        zoom 0.7

    marta_chen "Okay! Seeds out! We sift, we label, we trade. This is not just growth—it's evidence.' Her hand gestures expand as if planting the town itself. 'We teach, we plant, and we make sure nobody goes hungry while we lawyer the world."
    "Narration:"
    "You move through lines of neighbors—hands that know seed by feel, not by name. Marta's energy is sharp and necessary; the workshop feels like a rapidly beating heart. She presses a sieve into your hands and points to an older woman with trembling fingers."

    marta_chen "She wants to learn the timing for spartina. You show her what you know."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "I show her,"

    marta_chen "We lost beds, we lost boats, but we didn't lose how to make soil matter.' She steps closer, voice quieter. 'You teaching that lab class today—did you say yes to the Beacon's scaled help?"
    "Narration:"
    "The question lands like a stone. Your palm tightens around the sieve. Marta's glance flicks to where the Beacon's halo is visible over the town like an indifferent eye. Lila's offer—scaled help with tighter strings—has become a rumor that smells of contracts and new property lines."

    asha_moreno "They offered scaled assistance,' you admit, voice lean. 'With conditions. Rosa is pushing governance language. We... are sorting the terms."

    marta_chen "Don't let them put fences on the soil.' She huffs, then softens. 'We need tools, yes. But not keys they can turn without us in the room."

    menu:
        "Take the mic and teach a quick seed-sifting technique":
            "You step up and demonstrate, your voice steadying as you speak. People gather, questions roll in, the town learns one more thing to hold itself."
        "Stay back and take notes for the Tidewatch lesson":
            "You stay in the crowd, scribbling details into your ledger. Noah watches you—relief and worry mingling in his eyes."
        "Pull Marta aside to demand her help in the governance meetings":
            "You drag Marta near and outline a plan: workshops to mobilize neighbors for public comment. She grins, fierce and immediate, and agrees to marshal volunteers."

    # --- merge ---
    "Each small decision ripples outward. The gardens become a map of who the town will be if it survives: communal plots, shared tools, a barter shelf with a handwritten sign—'Leave a cutting, take a cutting.' The community rearranges itself around labor and commons."
    "Narration:"
    "The garden work accelerates; hands move faster, hearts too. Children run between plots, carrying bundles like small flags. The town's resilience is being stitched in public—simultaneously brave and brittle. Your guilt, that old ache of responsibility,"
    "sharpens into a different pressure: the need to negotiate now, to translate grief into policy and furrows."
    # [Scene: Tidewatch Lab | Afternoon]
    hide marta_chen
    hide asha_moreno

    scene bg ch13_66a4ee_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant sensor pings, the low murmur of conversation]
    # play music "music_placeholder"  # [Music: Pulsing electronic rhythm — urgent, insistent]
    "Narration:"
    "By afternoon, the lab smells of ozone and coffee. You set your compass on the lectern like an altar. Students—neighbors, volunteers, a few municipal staff—settle into folding chairs. The tide charts on the screen are honest and cruel; they do not flatter."
    show asha_moreno at left:
        zoom 0.7

    asha_moreno "Today we talk about gradients,' you begin, voice carrying over the click of a pointer. 'How a shoreline can be a living system instead of a wall. How marsh wrack traps sediment, how plantings work with the tide instead of fighting it."
    "Narration:"
    "You pace the lecture in thirds: science, tactics, community labor. Hands raise—questions are precise and raw. Someone asks about cost; someone else asks about safety. You answer each with the slow arithmetic of necessity and ideal."
    "Narration:"
    "Noah watches from the back, notebook open. He meets your eye when you pause and offers a small, private smile that steadies you in a way policy never can."
    show noah_reyes at right:
        zoom 0.7

    noah_reyes "Good framing,' he murmurs when a break opens. 'You're translating lab language into something people can hold."

    asha_moreno "They're tired of jargon,' you reply. 'They need to know what to do at dawn when the tide comes in and the sensors are down."
    "Narration:"
    "The door opens. Lila slips in—impeccable even in this damp light, the beacon of her own certainty. She carries a company tablet like a shield. The room's temperature drops a degree; her presence draws the lines of argument closer."
    show lila_park at center:
        zoom 0.7

    lila_park "Asha,' she says, voice even. 'I'm glad to see the community engaged. We can scale support—engineered plant mats, seeded platforms, sensor kits. We can expedite the accretion process if we collaborate."
    "Narration:"
    "You feel the old reflex—defense—rise. Lila's help would accelerate many of the things you're teaching by hand. It would also tie resources to terms, to data access, to maintenance schedules decided in boardrooms. The room listens; the students' faces shift from curiosity to calculation."
    hide asha_moreno
    show mayor_rosa_alvarez at left:
        zoom 0.7

    mayor_rosa_alvarez "We're drafting a phased governance model,' she says. 'Resident seats, transitional support for displaced households, and an oversight clause. Lila, your firm could provide technical assistance—if we can secure the right legal language."

    lila_park "Of course,' Lila replies. 'We can tailor the contract. Transparency dashboards, resident liaisons, shared data streams."
    "Narration:"
    "The sentences glide past one another with dangerous ease. Shared data streams. Resident liaisons. Tailored contracts. Each phrase is a lever; each lever shifts power."
    hide noah_reyes
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Shared data streams must be auditable by the town,' you say. 'Resident liaisons must answer to the elected board. And any maintenance protocol cannot be a de facto privatization of access to the shoreline."

    lila_park "Auditable—yes, within reasonable bounds. Liaison—yes, appointed with consultation. But understand: timelines matter. If we don't act now, repair windows close. The funders won't wait."
    "Narration:"
    "Her urgency cracks like a whip. High arousal—pressure—sits in the room as an electric charge. The lab's screens show projections that make your throat hollow: without intervention, more homes may go. With intervention, terms change. There is no clean path."
    hide lila_park
    show noah_reyes at center:
        zoom 0.7

    noah_reyes "We all want to avoid another night like the last. But we can't trade long-term control for short-term peace."
    hide mayor_rosa_alvarez
    show lila_park at left:
        zoom 0.7

    lila_park "Noah, I'm not asking you to sign away your town. I'm offering a partnership that can be scaled elsewhere—Marabel as a model. That will bring more funding, more resilience."
    hide asha_moreno
    show mayor_rosa_alvarez at right:
        zoom 0.7

    mayor_rosa_alvarez "We need to weigh immediate safety against governance safeguards. I propose a phased approval—pilot now, oversight council forming simultaneously."
    "Narration:"
    "Your heart beats too fast. The compass at your throat feels like a tiny fist. You think of Eli's hull, of Marta's seed screens, of the marsh wrack beginning to trap sediment in shallow coves. You"
    "think of the child who counted survivors with solemn fingers. The ledger in your bag looks heavier than it did in the morning."

    lila_park "You'll teach the community how to scale what you're doing,' she adds, softer. 'We'll provide the platforms and the logistics."
    hide noah_reyes
    show asha_moreno at center:
        zoom 0.7

    asha_moreno "Logistics aren't neutral. They decide who eats and who loses an address. They decide which people get to speak when contracts are drawn."
    "Lila Park: (A beat.) 'Then let's write the contract so the town governs the governance. Resident veto points, escrowed funds, legal penalties for overreach.'"
    "Narration:"
    "She says the phrases you want to hear. But as quickly as comfort rises, a hundred small alarms light along your ribs. Lila talks like an engineer who has learned the cadence of compromise; you hear, beneath it, the soft click of locking mechanisms."
    hide lila_park
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "We can make the clauses,' he says. 'We can demand audits, resident control. But we can't pretend that money and time don't matter."

    mayor_rosa_alvarez "We don't have the luxury of pretending,' she says. 'We had a night where that cost us. Let's make the guardrails now."
    "Narration:"
    "Words become plans; plans become potential fences. The volume of the room rises—not in anger but in pressure. Voices cross like waves; tension crescendos. Your guilt—old, loyal—stings anew. You are the town's interpreter now: translating grief into structure, loss into governance."

    asha_moreno "If we do this, it will be under terms we can enforce. It will include public audits, on-site resident oversight, and real contingency funds controlled locally. But if any clause undermines the commons, we walk."
    hide mayor_rosa_alvarez
    show lila_park at right:
        zoom 0.7

    lila_park "Understood."
    "Narration:"
    "The word 'understood' hangs like a promise and a threat at once. The lab's monitors ping; outside, a sensor blinks with a rhythm like a heartbeat. The day advances and urgency does not lessen—it sharpens toward the next moment when contracts will be drafted and signatures pressed."
    hide asha_moreno
    hide noah_reyes
    hide lila_park

    scene bg ch13_66a4ee_4 at full_bg
    # play music "music_placeholder"  # [Music: Full, urgent orchestral swell — then a hard cut to a single sustained note]
    "Narration:"
    "You feel every choice as pressure—an increased tempo under your ribs. Choices made now will echo in a decade: who governs the shoreline, who keeps homes, who gets to plant or be priced out. The town"
    "is bruised and organizing, and that organizing is a furious, difficult thing. Your chest tightens with guilt that is softening only into purpose—the kind that demands action."
    "Narration:"
    "There will be clauses to hammer out, nights at the table, neighbors who will come with stories that haunt the legal text. There will be victories that taste like ashes, and losses that will be reassembled"
    "through sheer, stubborn labor. You inhale. The compass at your throat is a small, steady proof that you can orient by something besides fear."

    scene bg ch13_66a4ee_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant, insistent sensor ping — precise, remorseless]
    # play music "music_placeholder"  # [Music: Held single note that invites continuation]

    scene bg ch13_66a4ee_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter25
    return
