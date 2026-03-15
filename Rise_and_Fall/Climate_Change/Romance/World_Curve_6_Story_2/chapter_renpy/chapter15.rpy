label chapter15:

    # [Scene: Courtroom-style Hearing | Midday — Overcast]

    scene bg ch14_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmur of the crowd, the clicking of a camera, a distant gull cut off by a cough; a moderator’s gavel taps once like a pulse.]
    # play music "music_placeholder"  # [Music: Low, restrained strings; a single cello line underpins the room's tension.]
    "You stand at the lectern. The microphone feels small and thin against your palm—an unreliable throat in a room that wants simple answers. Your bracelet thrums once with a microclimate blip; the skin beneath it is"
    "damp from the sweat you didn't notice forming. The documents you released sit in a neat stack in front of you, each sheet a blade that cuts into the polite architecture of 'partnership.'"
    "Your notes are organized—data blocks, timestamps, correspondence threads. You taught yourself to speak in evidence when everything else around you wants stories. Yet the words you intend to keep simple tremble in the space between your teeth and your tongue."
    "You take a breath. The air tastes of coffee and salt and the metallic reek of paper handled too many times."

    "Moderator" "Ms. Armitage, when did you release these documents to the press and to the federal oversight committee?"
    show maya_armitage at left:
        zoom 0.7

    maya_armitage "Three days ago. I—' (you steady your voice) '—I released them because the override clause tied to external investors would have allowed unilateral changes to public oversight within emergency timelines. The town deserves transparency."
    show evelyn_hart at right:
        zoom 0.7

    evelyn_hart "Those clauses are standard. They protect the project's schedule—which, if delayed, risks federal withdrawal of broader support."
    "You feel the room lean toward Evelyn's words like a tide. She speaks as if she is presenting a schematic, not a moral ledger. Her expression is composed; a cool measurement behind an ice-blue gaze. There is nothing performative in her civility. It is an argument wrapped in certainty."

    maya_armitage "Protected from what—themselves? Investors are not caretakers. When profit timetables override oversight, protections become a checkbox."

    evelyn_hart "Your concern is noted, Ms. Armitage. But the town also needs infrastructure now. Time is a resource climate change will not return."

    "Moderator" "Ms. Armitage, are you alleging criminal misconduct or a policy failure?"
    "You hesitate only a fraction. The memory of late nights mapping tidal ingress, Rafi's jittering hands and patched code, Jonah's blunt laughter when it was easier to hope than panic—these flash through the blinders of your resolve."

    maya_armitage "Both. The documents show preferential routing of contracts, funneling through shell firms tied to a third-party investor with vested interests in rapid, concrete construction. The emergency override clauses would have effectively silenced local oversight during 'urgent' incidents—meaning investors could change scope and deliverables without the community's consent."
    # play sound "sfx_placeholder"  # [Sound: A camera shutter; a whisper that becomes a ripple.]

    evelyn_hart "Ms. Armitage, the implication is severe. Do you possess evidence linking any city official to personal gain?"

    maya_armitage "I have correspondence that suggests expedited approvals were prioritized where timelines aligned with investor disbursements. It's not just theory—it's timing and benefit. That's why I gave it to oversight."

    evelyn_hart "And you gave private correspondence between public servants and private actors to the press. You knew the consequences of that."

    maya_armitage "I knew the consequences of letting a clause strip the community of oversight. We were one storm away from a legal override of democratic process. I chose the town."

    "Moderator" "We'll enter these documents into the record. There will be a federal inquiry."
    "The phrase lands with a dull, enormous weight. A federal inquiry—both shield and spotlight. You can taste its double edge: the chance to halt predatory timelines, the certainty of knives aimed at you in the press and in the boardrooms where reputations are currency."

    menu:
        "Emphasize the human cost":
            "You lean forward and, without the diagrams, tell the room about Nan's porch, about Jonah's brother's boat, about the child who lost a toy to a surge. The room is quieter; faces soften but the press scent sharpens."
        "Stick to the data":
            "You go back to the spreadsheets—projected inundation levels, timestamps, transaction graphs. The lawyers nod. The human faces in the crowd look like a distant audience."

    # --- merge ---
    "The hearing concludes and the narrative continues to the next scene."
    # [Scene: Council Chamber | Late Afternoon — Faint drizzle]
    hide maya_armitage
    hide evelyn_hart

    scene bg ch14_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low rumble of conversation, punctuated by someone banging a fist on a table in the back; rain tick-tacks against the high windows.]
    # play music "music_placeholder"  # [Music: A single harmonium note, melancholy and persistent.]
    "You leave the federal hearing with a press packet tucked against your ribs and Rafi shadowing your steps, eyes rimmed with red-rimmed worry. Jonah waits by the harbor door, rain darkening the cuff of his coat."
    "He looks older than you remember him—his jaw set in a way that suggests he has been measuring risk and loss for longer than these last frantic weeks."
    show rafi_chen at left:
        zoom 0.7

    rafi_chen "They put you on the front page. Tweets are… creative. Someone called you 'the harbor's saboteur' and 'a saint' in the same thread."
    show maya_armitage at right:
        zoom 0.7

    maya_armitage "Balance, Rafi. The internet has perfect equilibrium for extremes. Anything else?"

    rafi_chen "Nan's knitting group is making signs that say 'Thank you.' The market association—less enthused.' (he rubs the back of his neck) 'We might lose a small grant. But—' (he runs fingers over a schematic he keeps like a talisman) '—we aren't out of options. The oversight pause buys us time to structure community control. Which, you know, you made happen."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "You did what you thought was right, Maya."
    "You see him up close—salt in the edges of his lashes, the leather of his palm callused where he holds nets. His eyes are soft with respect but wounded in a way he won't name."

    maya_armitage "They'll make it personal. They always do."

    jonah_reyes "They'll make it legal. They'll make it loud. But they won't make it lonely—for you—not today."
    "You want to reach for him. The impulse is old as breath—push and rescue, clutch at a present that might be a future. But politics and love are not the same tide. They have different rules; one asks for sacrifice and the other, for reciprocity."

    jonah_reyes "My coop… the kids need the boats; wages are already thin. I can't sign up for a multi-year legal fight that would leave them afloat on promises. I can stand at your side while things go public. I can pull my boat from the council float if the coop needs me to. But I can't… uproot them for a battle that might cost us the nets we sleep under."
    "You feel the room rotate; a physical knowing settles: he will be steady at your shoulder, but his hands are tied to the cove in a way that yours, as an organizer, sometimes are not—or at least, not in the same way."

    maya_armitage "I never expected you to leave the work that feeds the town. I asked for you to be with me, not to carry my whole fight."

    jonah_reyes "There's a difference between standing with someone and walking into the courtroom as their hired solace. I owe the coop nights and futures. I owe my grandmother her grave kept right. I'm not walking away from that for headlines."
    "You are not surprised. You are still, somehow, broken by the particular geometry of 'not surprised.'"

    maya_armitage "Do you regret coming to the harbor tonight?"

    jonah_reyes "Regret is a luxury I can't afford. Respect isn't. I respect you."
    "There is a long silence where neither of you names the emptiness that opens between respect and shared beds, between political conviction and domestic stability. Outside, the rain thickens the harbor into a charcoal wash."

    menu:
        "Ask Jonah to come to the next hearing":
            "You risk the vulnerability—invite him again, map the timeline with him. Jonah nods but the nod is anchored to a ledger—the coop's rota—his face says he'll try, not that he'll be there."
        "Let silence sit":
            "You let the unsaid hang. Jonah squeezes your shoulder, a contained warmth. The lack of promises is a kind of truth both of you can accept for now."

    # --- merge ---
    "The evening's backlash unfolds and the narrative proceeds to the montage."
    # [Scene: Media Backlash Montage | Evening — Various Locations]
    hide rafi_chen
    hide maya_armitage
    hide jonah_reyes

    scene bg ch14_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Static, a crescendo of voices—some supportive, many accusing; a lone tambourine roll of outrage.]
    # play music "music_placeholder"  # [Music: Dissonant piano clusters; a heartbeat snare underneath.]
    "You weather a storm that is not rain. Anonymous op-eds accuse you of 'hampering progress' and 'personal vanity.' A familiar columnist calls you a 'self-appointed guardian with a personal agenda.' Your inbox is full of legal"
    "notices and donation links; donors who once promised seed money now ask for distance and deniability. Rafi's prototype funding is flagged for audit. The community trust fund idea you envisioned gains private donors who want naming"
    "rights. The world becomes a machine that insists upon naming and monetizing pain."
    "You read the comments between projects, because you cannot not know. The small kindnesses—Nan's hand through your hair, the group of schoolchildren making tide-line banners—exist side by side with emails that threaten slander suits. You count"
    "the cost in real currency and in more subjective units: sleep, the ease of a Saturday, the ability to hold Jonah without thinking of headlines."

    scene bg ch14_3be532_4 at full_bg
    show rafi_chen at left:
        zoom 0.7

    rafi_chen "They flagged our procurement logs. It’s bureaucratic harassment at worst, and a PR hit at best. But there’s traction. The feds put a hold on the pipeline funding. That means the concrete ships are idle. That means the city can't fast-track overrides."
    show maya_armitage at right:
        zoom 0.7

    maya_armitage "So we bought time."

    rafi_chen "We bought time by making you pay a price. People will try to make you small for it. You need to prepare for legal pressure."

    maya_armitage "I expected it. I didn't expect how personal they'd make it."

    rafi_chen "They'll try to peel you apart—personal history, past mistakes, anything to erode your credibility. Keep records. Keep friends close. Keep Nan fed. And maybe—' (he clears his throat) '—let Jonah decide how close he's willing to be."
    "You close your eyes. Rafi's practical counsel is a rope you take, knot by knot. You are tired and vigilant and oddly proud that the town now has breathing room to negotiate protections that wouldn't have existed otherwise."
    # [Scene: Council Chamber — Negotiation Table | Next Morning — Dull Sun]
    hide rafi_chen
    hide maya_armitage

    scene bg ch14_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low exchanges; a clock ticking louder than it should.]
    # play music "music_placeholder"  # [Music: Sparse piano, minor keys; tension like a tightened wire.]
    "Evelyn Hart enters, and for the first time since this began, she looks unsettled in a way that is not performative. The public inquiry has pried open doors she assumed would stay closed. Her hands are"
    "on the table; she still speaks in project timelines, but her sentences have a new edge—defensive, occasionally apologetic."
    show evelyn_hart at left:
        zoom 0.7

    evelyn_hart "The federal hold complicates funding schedules. I want to be clear: my team's goal has always been to protect Highwater Cove."
    show maya_armitage at right:
        zoom 0.7

    maya_armitage "Protection for whom, Evelyn? The language in your contracts privileged investor timelines over community review. That's not protection. That's a takeover."

    evelyn_hart "I miscalculated the city's communication. I underestimated communal sensitivity to oversight clauses. For that, I take responsibility."
    "You scan her face for the crack that would prove genuine contrition. The expression is complex—part calculation, part irritation at being forced to recenter the narrative."

    maya_armitage "We need enforceable community oversight—the trust fund must be community-run with legal teeth. No naming rights over essential infrastructure. And any emergency override needs a triple sign-off: the oversight board, an independent auditor, and the mayor."

    evelyn_hart "Triple sign-off will delay construction. It will increase costs."

    maya_armitage "Good. Delay and increase cost are sometimes the medicine communities need to avoid rushed harms."
    show mayor_lena_ortiz at center:
        zoom 0.7

    mayor_lena_ortiz "We need workable terms. The federal pause gives us leverage. We can demand restructuring of the investment pipeline. We can demand community seats on any board."

    evelyn_hart "If we do this, we rework every timeline. I can't promise donors won't pull out."

    maya_armitage "Then we face that. We do it openly and we build a public trust to cover shortfalls. We build local capacity. We don't hand the keys to external investors who can flip contracts from air."

    evelyn_hart "You're asking me to choose long-term accountability over short-term delivery."

    maya_armitage "Yes."
    "Her face flattens with the relief of being given an argument she can translate into policy. Yet the room knows the cost: funders that demand quick returns will threaten to leave, and political careers hinge on deliverables."

    evelyn_hart "If we rework the contracts, if we put binding community oversight—then the proposals will change. I can support that, but understand: this ends the version of the plan I advocated for."
    "You feel the subtle shift of victory: not complete, but foundational. The room's energy is a brittle, cautious optimism; you know better than to call it triumph."
    # [Scene: Reclaimed Marsh — Dawn — Quiet]
    hide evelyn_hart
    hide maya_armitage
    hide mayor_lena_ortiz

    scene bg ch14_3be532_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft plop of water, a distant gull, the faint scrape of a spade as volunteers work in measured silence.]
    # play music "music_placeholder"  # [Music: A single, melancholy violin matching the dawn—simultaneously elegiac and resolute.]
    "You walk the marsh when the world is quiet enough to hear the small returns—baby crabs scuttling, a shimmering strip of algae, a new reed pushing from mud. Courage isn't only loud; it's the slow, repetitive act of planting where you once feared to place anything."
    "Nan meets you by a check-dam with a thermos and a hand that still knows how to arrange a scarf into comfort. She doesn't need to say much; she wraps her kerchief around your neck like a benediction."
    show gracie_nan_armitage at left:
        zoom 0.7

    gracie_nan_armitage "You made a hard choice, child. Sometimes the world asks us to break ourselves to make a place that doesn't break others. It doesn't mean you are done with heartbreak. It means you did what you could."
    show maya_armitage at right:
        zoom 0.7

    maya_armitage "They've... dragged my name through it. The press said things about me—about my motives. Jonah—' (you stop; the word tastes like a wound) '—he's stayed. He's not gone. But he's not with me in court every day."

    gracie_nan_armitage "Love isn't only in the grand gestures. It can be in staying and it can be in stepping back to keep nets mended. That doesn't make your choice wrong."
    "You look across the marsh. Volunteers—some people you organized, some who simply woke up and came—move with a kind of quiet communion. The community trust fund is being formed; seed money will be raised via local"
    "benefit events, old boats turned into community savings vessels. The legal reforms the federal inquiry demands are beginning to take shape on paper. The town is safer than it was yesterday. But safety has a price."
    show rafi_chen at center:
        zoom 0.7

    rafi_chen "They've subpoenaed one of the shell companies. A handful of donors are backing the new trust quietly. We might have a path to retool the breakwaters to living systems instead of concrete—if we keep the oversight language locked."

    maya_armitage "And me?"

    rafi_chen "You're a person who exploded a status quo to force accountability. That doesn't erase the personal toll. You should rest. You should—"
    "You cut him off with a small laugh that turns into something like a sob. Rest is a word that used to mean sleep. Now it means negotiating law, answering televised panels, and possibly defending yourself in a courtroom."
    "Jonah Reyes appears on the raised boardwalk, boots quiet. He has been busy with the coop—mending a hull, teaching a young crew to splice rope. He watches you work the marsh with that same attentive steadiness he brings to boats."
    hide gracie_nan_armitage
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "I don't know if this—any of this—will leave room for figured love the way we once imagined. I won't lie: I am tired and scared and practical. But I respect you. I respect what you did."

    maya_armitage "Do you—do you regret not joining the legal fight?"

    jonah_reyes "I regret nothing I did for my family. I regret being afraid to risk them for an abstract right—maybe. But I also know that being here feeds the town in a thousand quiet ways. My staying is a sacrifice of a different shape."
    "You think of the gulf between the kinds of sacrifice—his, material and immediate; yours, reputational and existential. Neither is greater. They are unequal and still heavy."

    maya_armitage "So where does that leave us?"

    jonah_reyes "It leaves us with a future that's complicated. It leaves me with the choice to stand near you, not in your war. It leaves the space for something tender we may share without grand promises."
    "You close your eyes. The marsh breathes around you, small life and slow protest against the sea. You wanted a partner you could lean on, someone who would carry as much as you. You have instead"
    "an ally who understands boundaries and a town that will survive because you made it choose accountability over convenience."
    "You feel the cost like a cold stone in your chest and the relief of not being alone like a summer breeze that doesn't quite warm you."
    # play music "music_placeholder"  # [Music: The cello in the clouds deepens; the melody is minor and not apologetic.]
    "You made a calculation and you lost a kind of private ease. The federal inquiry moves forward. Evelyn's project pauses and is renegotiated with community teeth. Grant streams are rerouted into a community trust with legal"
    "fiduciaries. Shell companies are being audited. The living breakwaters plans gain traction where concrete plans stall. Highwater Cove's fate is changing—to something harder and, you hope, more just."
    "But you also watch Jonah walk his own path in the coop, and you accept that the kind of closeness you once pictured—quiet mornings with shared coffee and unforced conversation—will have to wait. It may arrive"
    "again in a different season, or it may rearrange into a form you cannot yet imagine. You have chosen the town over immediate personal comfort."
    "You take a breath that feels like an exhale across a winter sea."
    hide maya_armitage
    hide rafi_chen
    hide jonah_reyes

    scene bg ch14_3be532_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gull, marsh water, a volunteer's laugh—small and resistant.]
    # play music "music_placeholder"  # [Music: A low, steady drone; the final note lingers like a vow and a wound.]

    scene bg ch14_3be532_8 at full_bg
    "THE END"
    # [GAME END]
    return
