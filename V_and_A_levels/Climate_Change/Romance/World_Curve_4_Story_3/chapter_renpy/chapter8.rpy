label chapter8:

    # [Scene: The Beacon Plaza | Morning — Low overcast, light rain]

    scene bg ch7_5caaae_1 at full_bg
    # play music "music_placeholder"  # [Music: Soft, metered percussion — steady, watchful]
    # play sound "sfx_placeholder"  # [Sound: The hiss of drizzle, distant gulls, the intermittent click of tools]
    "You arrive with your ledger unrolled under your arm and the brass compass heavy against your palm. The decision you made—trial the Beacon's array under legal oversight—has already shifted the town's rhythm. Today that shift is"
    "visible: lines on maps are being translated into metal and code, and the people who will live with the change are watching as much as the engineers."
    "You smell wet concrete and hot solder; the air tastes faintly of iron and sea. Your boots leave dark prints on the plaza stones. A line of Beacon engineers moves with practiced efficiency; someone clips a"
    "sensor to a stanchion and a trace of light walks up a network cable like a small, obedient creature. Lila Park stands nearby in slate coat, arms folded, watching the deployment as if it were a"
    "performance she both directs and critiques."
    show lila_park at left:
        zoom 0.7

    lila_park "Calibration's on track. We're getting clean reads in under three minutes. That variance used to be fifteen. That's—' (she inclines her head toward you, precise) '—a big difference for evacuation windows."
    "You swallow the small, exact answer you could give about model margins. Instead, your voice is measured, intentionally human."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Faster windows save lives. We're grateful for the improvement."
    "Lila Park's mouth tilts with a smile that is not quite warmth, not quite calculation."

    lila_park "Gratitude is mutual. Marabel makes a strong demonstration site."
    "She gestures toward a legal observer—Mayor Rosa's counsel—who stands with a tablet and a printed contract folder like an extra sensor in human form. Across the plaza, a group of volunteers organized by Marta sets up"
    "a tea station under a patched awning; their laughter is a thin, bright thread in the steady rain."
    "Your chest regulates to the cadence of the work. Gratitude, yes. Also a ledger you thumb through in your head: improved forecasts, fewer midnight evacuations, fewer ruined generators at the shelters. On the other side of"
    "that ledger, another column ticks: maintenance fees, firmware updates, 'platform-managed assets' written in donor-smooth language that resists your touch."
    "Noah Reyes is beside you before you know you wanted him there—rolled-up maps under his arm, curls damp from the drizzle. He doesn't ask to see the ledger; he reads your face instead."
    show noah_reyes at center:
        zoom 0.7

    noah_reyes "How's it look from this side?"

    asha_moreno "Cleaner reads. The tide maps compress the window by a few hours. That's good."
    "Noah Reyes studies the sensors, then looks to Lila Park, then back to you."

    noah_reyes "I pushed for that clause—community access rights to the raw feed. They said yes in principle.' (his brow tightens) 'But it's gated. Access points, they called it. We get keys, yes, but the keys live in their platform."
    "His hands press the rolled map gently, like a promise he is trying to keep flat."

    asha_moreno "Keys that live on someone else's server aren't the same as control."
    "Noah Reyes's gaze finds yours. There is an argument inside him—pragmatic and human—that he is choosing how loudly to voice."

    noah_reyes "I negotiated oversight windows. We can audit. They agreed to quarterly joint reviews.' (he exhales) 'It's not everything, but it's something we can build from."

    asha_moreno "Something you and I agreed would be temporary until the town could stand its own systems."

    noah_reyes "Exactly. Temporary."
    "Across the plaza, a young engineer—Caleb, you think—walks with a tablet and keeps glancing at the legal observer. His shoulders are narrow, his face shut against the rain. When he passes you, his eyes flick to your compass and linger with a complication that reads like apology and hope."
    hide lila_park
    show caleb_osei at left:
        zoom 0.7

    caleb_osei "If you want a look at the feed parameters later, I can pull a raw dump. Not the pretty plots—real numbers."

    asha_moreno "Thank you. That could help with the community audits."
    "Caleb nods, unreadable, then moves on. Lila Park watches him for a beat, then turns back to the array, the calculus of advantage folded tight around her expression."
    # [Scene: Tidewatch Lab | Midday — Humid with steady drizzle]
    hide asha_moreno
    hide noah_reyes
    hide caleb_osei

    scene bg ch7_5caaae_2 at full_bg
    # play music "music_placeholder"  # [Music: A light piano motif — practical, intimate]
    # play sound "sfx_placeholder"  # [Sound: Keyboard taps, soft murmur of people collaborating]
    "Inside Tidewatch, the mood is closer—less public performance, more revision of plans. Marta sets a tray of steaming cups down; the smell of ginger tea is a balm. Eli Duarte has arrived with a crate of"
    "reclaimed hardware—old GPS units he's been refurbishing—and he wipes his hands on a rag as he jokes with the volunteers."
    show eli_duarte at left:
        zoom 0.7

    eli_duarte "These hulls aren't just for fishing anymore. If we bolt nets to the bows, they'll carry people, food—whatever we need—above the worst of the surge."

    "Marta Park" "We can teach teams to drive them. We can run drills."
    "You listen to the practical conversation—the steady work of making resilience tangible—and you circulate between tasks: recalibrating a forecast, answering a volunteer's question about sensors, annotating a map with new evacuation corridors. Each annotation is a tiny vote toward what you believe Marabel should be."
    "Noah Reyes hovers near the instrument rack, occasionally reaching to steady you when you're bent over a screen. His hand rests on the small of your back—a small, deliberate contact that says he is there to"
    "share the weight. You notice, and the notice is a quiet warmth in the middle of semantics and contracts."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Did the Beacon's API team finally send the endpoints?"
    show noah_reyes at center:
        zoom 0.7

    noah_reyes "They did. Wrapped in a terms doc that reads like a polite takeover.' (he gives you a crooked look) 'I read it twice. We can scope our access—temporarily—without exposing private data. But the maintenance schedule... the default is their technicians."

    asha_moreno "Default technicians cost money. Whose budget line is that on?"

    noah_reyes "Initial funding covers the first quarter. After that, unless we raise independent funds, maintenance lands on the town.' (his mouth tightens) 'We can start a fund drive—Marta's crew is good at that—but it's a strain."

    asha_moreno "We must be honest with people about that."

    noah_reyes "We will.' (he says it like a vow, then softer) 'You don't have to carry it alone."

    asha_moreno "I know."
    "Their back-and-forth is ordinary—policy and intimacy braided together. The tone is Mid: measured pressure, building, not yet a storm but a weather front moving in."

    menu:
        "Help Marta inventory volunteer supplies":
            "You step over to the awning, hands briefly warm in the ceramic of a tea cup. Marta hands you a checklist; the volunteers laugh as you count tarps. The act of organizing steadies you."
        "Stay with Noah to review terms":
            "You slide back to the lab table and the legal doc. Noah's shoulder knocks yours lightly as he points at a clause; together you outline a response. The work brings a finite focus that steadies the ache in your chest."

    # --- merge ---
    "Continue with the day's tasks and the town's planning."
    # [Scene: Raised Gardens | Late Afternoon — Wind picks up, sky bruised]
    hide eli_duarte
    hide asha_moreno
    hide noah_reyes

    scene bg ch7_5caaae_3 at full_bg
    # play music "music_placeholder"  # [Music: Quiet strings — hopeful, steady]
    # play sound "sfx_placeholder"  # [Sound: The creak of planks, muted conversation, a distant car horn]
    "Marta's volunteer network feels more alive than ever. The gardens are a place where the town's hands show."
    show marta_chen at left:
        zoom 0.7

    marta_chen "These plots are resiliency. They feed the town and they feed morale.' (she tucks a seed packet into your palm) 'We need more hands to shore the plant beds; the sensors keep a safer schedule for watering, but it's the people who make it stick."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "I'll put out a call. And we'll map garden access for emergency routes—connect the raised beds with the shelters."
    "Marta Chen studies your face with the clean, impatient affection of someone who speaks in tasks."

    marta_chen "Promise me you'll be clear about the costs. People trust you to tell them both the good and the trade-offs."

    asha_moreno "I will."
    "Eli Duarte arrives at the edge of the garden, carrying a plank of wood and a grin that carries sawdust and memory."
    show eli_duarte at center:
        zoom 0.7

    eli_duarte "Boatyard's busy. The barges are coming along.' (he glances at the Beacon in the distance) 'If those sensors keep their promise, people will sleep better. That's a real thing."

    asha_moreno "Better sleep is something to value."
    "Eli Duarte's optimism is practical: build, test, fix. It keeps you tethered."
    # [Scene: The Old Boatyard | Early Evening — Damp, the light softens]
    hide marta_chen
    hide asha_moreno
    hide eli_duarte

    scene bg ch7_5caaae_4 at full_bg
    # play music "music_placeholder"  # [Music: Acoustic guitar riff — cozy, work-worn]
    # play sound "sfx_placeholder"  # [Sound: The rasp of plane on wood, occasional laughter]
    "The boatyard hums with the slow, satisfying rhythm of making. You help carry a hull brace into place. The touch of wood, the scrape of rope—a different kind of ledger, one that balances accounts with calluses and sweat."
    show eli_duarte at left:
        zoom 0.7

    eli_duarte "We'll have drills next week. If the Beacon's alerts cut our reaction time, those barges will mean fewer stranded roofs.' (he taps the hull rhythmically) 'Think of it as redundancy."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Redundancy is what keeps us alive."

    eli_duarte "You're doing the right thing, pushing the trial. Lila's tech gives us that redundancy.' (he raps the hull, then softens) 'But keep one eye on the fine print. Those who build the nets don't always want them cut."
    "His words land with the precise caution of someone who knows wood and weather. You nod, the compass in your pocket warm."
    "Noah Reyes finds you among the hulls as the light shifts. His coat is flecked with rain; his hair has a salt-flattened look. He leans on a workbench and watches you with a patience that makes the air between you easier to breathe."
    show noah_reyes at center:
        zoom 0.7

    noah_reyes "We had the oversight meeting. They accepted the audit windows but asked for 'managed access' language.' (he exhales) 'I pushed. I pushed for more local admin rights. They gave conditional admin—keys with time limits."

    asha_moreno "Time-limited keys feel like a leash that bobs on the tide."

    noah_reyes "I know.' (he reaches out, thumb finding the small of your back again) 'But the grant saved two shelters this week. People slept in them without wet floors."

    asha_moreno "That matters."
    "He leans closer, his voice a private thing under a sky that looks like it will cry again."

    noah_reyes "I don't want us to lose the town to convenience. I want us to keep it whole.' (he searches your face) 'You and me—we can keep fighting from inside the process."

    asha_moreno "Fighting and being inside are different muscles. I can do both, but not forever."
    "Noah Reyes's hand lingers, asking for a permission you haven't named. You find yourself resting your palm against his when no one is watching, the contact a small alliance."

    menu:
        "Trace the map with Noah's finger and plan a funding drive":
            "You slide a finger along the paper, plotting community events and donor pitches together. Noah nods, his face lit by the plan rather than the rain. The act of planning makes the future feel a little more manageable."
        "Step back to check the maintenance clauses on your tablet":
            "You pull your tablet out, the screen bright against the dusk. Your eyes scan 'platform-managed assets' and the fee schedule. Your stomach tightens; the technical language reads like a slow tide. Noah watches you, patient but worried."

    # --- merge ---
    "Both paths lead back to the lab with plans and concerns in hand."
    # [Scene: Tidewatch Lab | Night — Rain steady, streetlamps haloed]
    hide eli_duarte
    hide asha_moreno
    hide noah_reyes

    scene bg ch7_5caaae_5 at full_bg
    # play music "music_placeholder"  # [Music: Tensioned synth — steady, expectant]
    # play sound "sfx_placeholder"  # [Sound: The soft ping of alerts, the rain a constant undercurrent]
    "Back in the lab, the town's new breathing pattern is audible: fewer panicked calls in the night, a steadier supply chain for emergency meals, volunteers who can rest between shifts. Your maps show that—the lines of"
    "evacuation corridors tightened, shelter occupancy more predictable. For a while, the trial is working as advertised."
    "Then a notification pings on your tablet—an automated threshold alert from the Beacon network. The tone is not urgent; rather, it's the voice of the machine doing what it was built to do: call attention."
    # play sound "sfx_placeholder"  # [Sound: High, polite ping]

    scene bg ch7_5caaae_6 at full_bg
    "You read the message slowly. The update will improve algorithmic accuracy; the default scheduling routes maintenance through Beacon's technicians unless you select an alternate path. The alternate path exists—community-managed maintenance—but requires formal certification, training hours, and funds."
    "Your ledger slides into focus: the maintenance column, the minute print, the phrase 'platform-managed assets' again and the clear sentence below it that reads like a contract's heartbeat: maintenance defaults to Beacon unless amended in writing."
    "Noah Reyes leans over your shoulder, his breath a warm pulse at your neck."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "If we accept the default now, it buys us immediate bandwidth. Less hassle, fewer midnight wake-ups.' (he meets your eyes) 'We can use the time to train volunteers."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "And if we accept the default, we start sending town money outward on a schedule that is hard to reverse."

    noah_reyes "I know. I don't want to spend what saves people now on services that make us dependent."
    "Caleb Osei appears in the doorway, rain beading on his hair. He has a printout in his hand and a look like someone who has been carrying a small worry for too long."
    show caleb_osei at center:
        zoom 0.7

    caleb_osei "There's a clause in the maintenance addendum about remote access tokens. It allows patching, but it also allows telemetry throttling during high-traffic windows.' (he doesn't look at Lila Park so much as toward the idea of her company) 'They say it's to protect the network. I say it could be used to gate our access."
    "Lila Park's voice comes over a softspeaker outside, practiced and close."

    "Lila Park (via small speaker near the array)" "The firmware update is standard. We recommend immediate installation. It will close a vulnerability and improve forecast precision. We propose maintenance windows twice monthly during low tide cycles."
    "Her cadence is efficient; the words are tidy. You can imagine them in a brochure. They are also persuasive in the face of fear."
    "You feel the arousal climb, clean and steady—mid-range energy: not panic, but the attentive edge of pressure. The lab feels smaller; the rain sounds larger against the glass. The choice is not dramatic in fireworks, but it is material."

    noah_reyes "We could delay it until we staff the certification. We could set conditional acceptance—install on non-critical nodes first."

    asha_moreno "Staggered deployment. Audit logs kept locally. A clause that allows emergency rollbacks only by mutual consent."

    caleb_osei "I can scope the rollback window. I can carve out a last-resort token that requires two signatories."

    "Lila Park (via small speaker near the array)" "I appreciate the caution. But each delay increases exposure. The updated models show higher near-term risk in certain inlets. The sooner the network is homogeneous, the better our collective response."
    "You hold the tablet, the place where policy and survival intersect. On the screen, a bright button blinks: ACCEPT DEFAULT SCHEDULING. Below it, a less visible line reads: REQUEST COMMUNITY-CONTROLLED SCHEDULE (requires certification and approval)."
    "Noah Reyes's hand squeezes yours once—gentle, an anchor. Your compass lies heavy in your pocket, reminding you of tides and trajectories."
    "You feel the decision tightening at the center of your chest. It is not a single dramatic split, but a slow, inevitable narrowing: trust the Beacon's immediate gains or insist on a slower, more costly path to autonomy."
    "Your pulse aligns with the steady ping of the network. The room holds its breath in small motions—the soft scrape of a chair, the rustle of a legal pad. The town's future is encoded in a choice whose weight is measured in hours, dollars, and the quiet erosion of control."
    "You lift your finger toward the screen. Time slows—not a thunderclap, but the mid-tempo stretch before a tide turns."
    hide noah_reyes
    hide asha_moreno
    hide caleb_osei

    scene bg ch7_5caaae_7 at full_bg
    # play music "music_placeholder"  # [Music: Single, sustained note; then a subtle rise that suggests momentum without frantic urgency]
    "Page-turning thought: Accepting now secures more nights of rest for neighbors and fewer splintered roofs tomorrow. Delaying carves out a firmer claim to independence but risks a near-term gap vulnerable to the sea. Both choices are moral and practical; both carry losses."

    scene bg ch7_5caaae_8 at full_bg
    # play music "music_placeholder"  # [Music: Held chord that invites continuation]

    scene bg ch7_5caaae_9 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter10
    return
