label chapter10:

    # [Scene: Skyfarm Terraces | Morning]

    scene bg ch10_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Gentle, rising strings; a light percussive pattern like footsteps on wood]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the soft drip of irrigation, low mechanical whir of a nearby pilot node]
    "You start the morning where the city feels most human: soil between your fingers and the smell of sea-salt on the breeze. The sigils — Ibe's idea, carved by a ring of artisans over three long"
    "nights — swing lightly at each node's access point. Each one is different: a wave rendered in gouged lines, a child's handprint burned into the grain, a tiny compass cut into the rim. They are less"
    "a logo than a promise."
    "You run your thumb along the edge of one sigil and feel the rasp of fresh wood. It anchors you in the particular: a neighborhood can still mark its territory of care, even when machines hum underfoot."
    show ibrahim_ibe_ndiaye at left:
        zoom 0.7

    ibrahim_ibe_ndiaye "They turned out like the old festival charms. Solid. People took to them quicker than I expected."
    "He smells of sawdust and salt — a salt that has become part of the city's perfume. He points out a cluster of seedlings thriving under a drip-line the hybrid's pilot module helps regulate. The terraces are fuller than they were last season."
    show elias_kade at right:
        zoom 0.7

    elias_kade "We pushed the last patch at dawn. The public repo mirrors are syncing. Serena double-checked the diagnostics. It looks... good."
    "He carries optimism like a toolbelt, and right now it glints with real data. You want to tell him that the sight calmed something in you, but words arrange themselves carefully — you are both builders and negotiators now."
    show maia_soler at center:
        zoom 0.7

    maia_soler "Good how?"

    elias_kade "Stable under tidal variance for the past twelve cycles. Fail-safes tripped properly when we simulated an overcurrent. The community hooks — your sigils' mapped controls — responded. People could alter flow without needing a central override."
    "You want to believe every 'good' because you paid for each of those small victories with sweat and sleepless nights, because every family that kept its roof is a ledger entry of labor and love. But you also know the systems will be tested in ways simulations can't always predict."

    menu:
        "Offer Elias a thermos of coffee":
            "You step to the supply crate, handing him the thermos. His grin is small and private, and for a moment there is only the shared steam of two people who have been awake too long."
        "Ask Elias about the open-source mirror locations":
            "You lean in toward his tablet, and his face brightens with the kind of pride he seldom wears in public. He scrolls, explaining branches and forks. You listen, notepad at the ready."

    # --- merge ---
    "The day continues with the terraces fuller and the community more involved."
    hide ibrahim_ibe_ndiaye
    show rin_voss at left:
        zoom 0.7

    rin_voss "You demanded oversight panels. We wrote them into the Accord. Public charter. Binding review schedules. No backdoors."
    "There is a pause long enough for sea-salt to settle on the conversation. You read the motion behind the words: power shared means different power brokers in the mix. For now, the panels are real, and"
    "your name appears as a stipulated community representative. The ink on the charter still smells of finishing oils."

    maia_soler "Binding means binding. Whoever drafts the language — it must include clear audit windows and community veto triggers."

    rin_voss "Agreed. And transparency on deployment sequences. We lose legitimacy if people feel decisions are secret."

    elias_kade "Serena helped design a public bug-bounty process. Citizens can flag anomalies and be compensated for local reporting. Code-wise, it's auditable. Symbolically, those sigils are more than wood; they're a visible reminder that the machine answers to the people."
    "You imagine children circling the sigils years from now, teaching each other which notch releases which valve. You imagine Old Man Toma telling those children the story of when the city learned to tie its machines to its stories. The image steadies you."
    # [Scene: Pilot Hybrid Deployment Site | Late Afternoon]
    hide elias_kade
    hide maia_soler
    hide rin_voss

    scene bg ch10_453e40_2 at full_bg
    # play music "music_placeholder"  # [Music: Low, optimistic synth under the strings; a heartbeat rhythm suggesting industry and harmony]
    # play sound "sfx_placeholder"  # [Sound: Tools clinking, a warm laugh from a nearby crew, the soft hiss of a vent]
    "The pilots go up like careful stitches. Volunteers ferry panels, artisans hoist sigils into place, and you stand beside Serena as she runs another live diagnostic. The lab's fluorescent coolness has been replaced by the honest grit of hands and wood and salt-spattered clothing."
    show serena_qiu at left:
        zoom 0.7

    serena_qiu "We pushed the redundant handshake logic into the public mirrors. If a node deviates beyond threshold, the system isolates it and notifies three independent community custodians before any automatic correction. That's the real difference — human oversight in the loop."
    show maia_soler at right:
        zoom 0.7

    maia_soler "And the time window? Ten minutes?"

    serena_qiu "We tightened it to five. Too long invites damage; too short and you remove human judgment. It's a compromise."
    "Her voice holds the pragmatic cadence of someone who doubted at first but built conviction out of constraint. You think of the people waiting in their homes, gardeners on rooftops, children splashing near the promenade. You are making trade-offs on behalf of a thousand small mornings."
    show ibrahim_ibe_ndiaye at center:
        zoom 0.7

    ibrahim_ibe_ndiaye "The sigils are more than ceremony. We carved emergency overrides — physical keys. If the network goes quiet, the community can still tip a valve manually. Old tech for when new tech sleeps."
    "You press your palm flat to one of the carved keys — the grain is warm from sun and the carved notch sits neatly beneath your fingers. It is practical and ceremonial all at once."
    hide serena_qiu
    show elias_kade at left:
        zoom 0.7

    elias_kade "Do you want to… check the main log with me? I could use another pair of eyes before the evening sync."
    "There is a private gravity when he asks. After months of argued code-lists and late-night installs, the two of you have developed a rhythm: he teases patterns out of data; you read people into the curves. It is an intimacy of comprehension."

    menu:
        "Stay with the log, help debug":
            "You crouch beside him, tablet between you, and together you trace a line of code. He explains his assumptions and you point out where social edge-cases could break the logic. The work becomes a conversation that also tastes like soup and moonlit rooftops."
        "Go check the manual override seals with Ibe":
            "You follow Ibe down a gangway to the manual housing. The smell of oil and cedar wraps around you. You run your hands over each seal, verifying the artisan's work. Ibe jokes about you being obsessed with texture, and you laugh, the sound loose and real."

    # --- merge ---
    "Evening comes, the pilots hold, and the community begins to watch their city change from within."
    # [Scene: Flooded Promenade | Dusk]
    hide maia_soler
    hide ibrahim_ibe_ndiaye
    hide elias_kade

    scene bg ch10_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: Warm guitar picking under the strings; a single, hopeful motif recurs]
    # play sound "sfx_placeholder"  # [Sound: Children calling, distant call of a vendor, the soft clatter of a repair team finishing their shift]
    "The promenade looks less like a scar and more like a seam. Where the water once licked at doorsteps with ravenous intent, there are now planned channels, raised thresholds, and community gardens that sip regulated tides. The hybrid's modulary presence is becoming part of everyday choreography."
    show old_man_toma at left:
        zoom 0.7

    old_man_toma "They'll tell the story differently now. Some will call you clever machines, some will call you wise neighbors. Tell them both."
    show maia_soler at right:
        zoom 0.7

    maia_soler "Tell them that we were stubborn and lucky and tired. That will be accurate."
    "You walk the promenade with Elias Kade and Ibe flanking you on either side — two very different kinds of grounding. Elias Kade's hand finds yours for a heartbeat, then withdraws when a vendor calls out"
    "a question. The intimacy is awkward and warm, the kind that comes from shared fixes and shared fear."
    show elias_kade at center:
        zoom 0.7

    elias_kade "We should celebrate tonight. Not because it's perfect — not yet — but because it matters. Because we built something people can touch."

    maia_soler "I want the children to know both the ledger and the stories."

    elias_kade "And the code."

    maia_soler "And the code, yes. But not instead of the stories."
    hide old_man_toma
    show serena_qiu at left:
        zoom 0.7

    serena_qiu "You all are writing history right now. Make sure to leave good comments in the repo."
    "The day winds down into a quiet you haven't allowed yourself in months. For weeks the pilots behaved like honest animals and people showed the incredible generosity of learning new rituals. The Skyfarm terraces are feeding"
    "more bellies; a communal soup exchange is scheduled for twice a week; artisans have been commissioned to carve sigils for neighborhoods beyond yours. The hybrid feels like a craft — equal parts machine and human knot."
    "You savor that sensation like a rare sweetness."
    # play sound "sfx_placeholder"  # [Sound: A soft digital ping from Elias Kade's wrist tablet, barely louder than a cricketsong]
    # play music "music_placeholder"  # [Music: Strings swell slightly, a hopeful chord that holds]
    "Elias Kade glances down, the light playing across his face in a way that makes the hollows softer. The notification is small, technical: a flagged telemetry variance in one of the more remote modules. Serena glances"
    "at the readout. Ibe frowns and prods a pebble with the toe of his boot."

    elias_kade "Probably a false positive from tidal noise."

    serena_qiu "Probably, but it's flagged as a redundancy handshake miss. The node isolated itself and queued a manual verification."
    "Your heart speeds for a moment that is not panic. It is the particular quickening of someone who knows the difference between a false alarm and the first whisper of a new problem. You feel the"
    "community beside you — faces and hands and the sigils — the whole city as a delicate lattice."
    "You: These are the moments that will write the next chapter. Every system has edges where it will fray. The question isn't whether they will fray but how and who will hold the loose strands."

    elias_kade "We can check it now. Or we can let the custodians do their verification cycle first and watch the logs."
    "You know both choices are valid responses. You also know that the way you choose will set a tone — for trust in process, for speed over caution, for the balance between centralized rescue and local agency. The decision hangs in the salt-tinged air like a small, inevitable tide."
    "You lift your hand, feeling the old copper locket at your throat; the promenade's lamps turn a softer amber as night falls. Somewhere beyond the market, a child's laugh cuts clean through the technical ping. Your"
    "choice — to act immediately with Elias Kade at your side, or to trust the newly-formed oversight channels to follow protocol — will say as much about who you are to this city as any charter"
    "ever could. You do not resolve it here. The tide of consequence is already moving, and whatever you do next will pull others with it."
    hide maia_soler
    hide elias_kade
    hide serena_qiu

    scene bg ch10_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter11
    return
