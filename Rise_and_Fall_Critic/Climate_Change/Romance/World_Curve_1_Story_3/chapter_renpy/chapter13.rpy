label chapter13:

    # [Scene: Meeting Room | Morning]

    scene bg ch11_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm strings, a hopeful ascent undercut with light percussion]
    # play sound "sfx_placeholder"  # [Sound: The distant churn of municipal pumps; a kettle hisses somewhere down the hall]

    scene bg ch11_e67f19_2 at full_bg
    "You stand where the light falls like a benediction across the holo-map. In one pocket, the compact multi-tool hums faintly; in the other, the cutting in its cloth sling brushes. Around the table are Hana Kim,"
    "Dr. Jun, and Mayor Lila — the room smells of warm coffee and the faint metallic tang of server equipment. The momentum you felt leaving the conference yesterday is still in your joints; the hybrid pilot"
    "exists now not as an abstraction but as a stack of clauses that needs careful language."
    "Your chest loosens with the small, steady certainty of work that matters. The rising tone of the day — sunlight, agreement, people moving — lifts something in you. This is not a casual negotiation; it's the"
    "scaffolding for how your neighbors will live. You place your palm on the table and let the glow of the map warm your skin."
    show dr_jun_park at left:
        zoom 0.7

    dr_jun_park "The data Jun sent last night lines up with what we charted — failure modes, maintenance windows, sensor drift. We can quantify outcomes, but we need the clause structure to enforce them."
    show hana_kim at right:
        zoom 0.7

    hana_kim "(nods, voice even) We can build a governance API — ledgered logs for pump cycles, sensor readings, maintenance tickets. If the community has read-write keys, the tech is transparent."
    show mayor_lila_ortega at center:
        zoom 0.7

    mayor_lila_ortega "Transparency is good. Legal enforceability is better. We need to write this so it survives a legal challenge and public scrutiny."
    hide dr_jun_park
    show asha_rivera at left:
        zoom 0.7

    asha_rivera "Agreed. My priority is twofold: ensure the community can't be sidelined, and make the tech usable for people who don't live in command terminals. We need plain language with teeth."
    "Hana Kim leans forward, the AR monocle flicking a pale glyph across the map. Her tone carries the measured calm you've always trusted — and a steel you sometimes bristle against."

    hana_kim "Plain language is easy. The problem is intellectual property. Aegis won't hand over core code without protections. We can open-source the deployment layer, the maintenance scripts, and APIs that allow local telemetry to be read and patched. But core control loops — the parts tied to patented hardware — are a tougher sell."

    asha_rivera "We can't accept black boxes. If the pump calibrations or barrier responses are opaque, the community is locked out of meaningful oversight. I need access that lets local technicians act in real time when the company is slow or absent."
    "Dr. Jun rubs the bridge of his nose and watches you both."
    hide hana_kim
    show dr_jun_park at right:
        zoom 0.7

    dr_jun_park "What if we tier access? Full read access to logs and modular control at the community-maintained layer, plus a contractual stipulation that core control adjustments require documented community sign-off during the pilot period?"

    mayor_lila_ortega "And binding penalties if Aegis denies access or withholds critical updates. Escrowed funds for emergency maintenance, released under specific conditions."
    "Hana Kim: (a small, almost imperceptible smile) 'Escrow models are workable. So is a covenant that requires open data streams. I'll have to push with Leon, but I can frame it as risk reduction for them; community auditing reduces reputational and operational risk.'"

    asha_rivera "We also need a maintenance cooperative — paid positions trained locally, responsible for day-to-day upkeep. It can't be that the company installs and walks away."
    hide mayor_lila_ortega
    show hana_kim at center:
        zoom 0.7

    hana_kim "Agreed. Training modules, local handover schedules, and a maintenance ledger tied to released funds."

    dr_jun_park "We should define 'community veto' carefully. Veto can be a blunt instrument; we need triggers and thresholds so it protects without being paralyzing."
    "You taste salt and coffee, adrenaline folded into the warmth. You imagine Teo learning sensor diagnostics in the plaza, Sofia teaching a rota, Jun calibrating sensors with neighborhood kids peering over his shoulder. The idea of formal structures that still feel like home hums bright and possible."

    menu:
        "Draft the clause as 'community veto'—strong, clear, non-negotiable":
            "You push the marker toward that phrase. The room goes still; Mayor Lila tightens, Jun tilts his head considering legal ambiguity. Hana Kim's hand pauses over the keyboard, measuring the political friction this could raise. The word feels like a shield."
        "Frame it as 'community consent with defined triggers'—more technical, less absolute":
            "You guide the language to be surgical: consent that activates under enumerated conditions. Jun grips the edge of the table; Hana Kim nods, relieved that this is a frame the engineers can operationalize. It feels like marriage between principle and practice."

    # --- merge ---
    "The scene continues."
    "Hana Kim glances at you after your decision — her expression complex, unreadable in small ways that mean everything and nothing at once. She pushes a string of clauses into the document: open-data streams, escrowed maintenance,"
    "training commitments. You feel the architecture of partnership taking shape, a lattice of legal and technical bones that could hold something human."
    hide asha_rivera
    show mayor_lila_ortega at left:
        zoom 0.7

    mayor_lila_ortega "I'll take this to the council with a draft covenant. But commitment from Aegis will want a public face. They like optics. They like press."
    hide dr_jun_park
    show asha_rivera at right:
        zoom 0.7

    asha_rivera "We control the frame. If it's a public rollout, it must be tied to enforceable milestones — not a photo-op. Otherwise their PR could outpace protections."

    hana_kim "We can bake milestones into the release schedule. Public rollout for political leverage, but with withdrawn triggers if milestones aren't met."
    hide hana_kim
    show dr_jun_park at center:
        zoom 0.7

    dr_jun_park "And community auditors — third-party but selected by the neighborhood — to certify milestone completion."
    "Mayor Lila taps the holo-map; a pin flares."

    mayor_lila_ortega "This is promising. With these clauses, I can present a conditional endorsement. But you'll need to show the barrio that this is their power, not corporate charity."

    asha_rivera "I'll bring the draft to Skyward Market. We'll test it with people who will live under it."
    # [Scene: Skyward Market | Midday]
    hide mayor_lila_ortega
    hide asha_rivera
    hide dr_jun_park

    scene bg ch11_e67f19_3 at full_bg
    # play music "music_placeholder"  # [Music: Light percussive rhythm, a community heartbeat]
    # play sound "sfx_placeholder"  # [Sound: Children laughing, a vendor calling out prices, the rustle of canvas awnings]
    "You thread through stalls, the cutting tucked against your chest like a small promise. Teo waits at the edge of a hydroponic bed, sleeves pushed up, mechanics' grease on his hands. Elias Hart watches from where"
    "a muralist is retouching a banner; his stance is casual, but his eyes are quick and bright."
    show mateo_teo_rivera at left:
        zoom 0.7

    mateo_teo_rivera "You got it in a form the people can read?"
    "You hand him a printed excerpt. The paper shivers in the breeze; someone tosses a handful of seed packets into a child’s hands and the market bursts into a laugh."
    show asha_rivera at right:
        zoom 0.7

    asha_rivera "Mostly plain language. Jun and Hana Kim mapped the triggers and maintenance schedule. There's escrow for emergency repairs, training modules for local crews, and a slate for community auditors."
    "Elias Hart folds his arms, eyes flicking to Hana Kim who stands a few paces away, talking quietly with a cluster of neighbors. His face is open, then closes into that unreadable thing you know as nuance."
    show elias_hart at center:
        zoom 0.7

    elias_hart "Sounds like compromise. My fear is optics—if Aegis shows up with fans and banners, folks will forget the clauses. Or they'll be dazzled by tech and forget who's supposed to hold the keys."

    asha_rivera "That's why we're doing this here first. If the market signs onto the covenant, it's harder for the optics to drown out the reality."

    elias_hart "Let me talk. Let me tell them about the living seawalls the kids painted last season. People respond to stories, not legalese."
    "You feel Elias Hart's voice pull at something older than policy — the mural days, the nights of hauling sandbags, the first time you held his hand as a small, defiant comfort against a storm. Whatever"
    "history lies between you and him is layered and complex; for now, you let the work be anchor."

    menu:
        "Hand Elias the mic; let him lead with story":
            "You nod and step back. Elias Hart's voice rides the market soundscape like a tide — warm, urgent, personal. People lean in. Teo grins and starts handing out translated bullet points. Hana Kim watches, expression complex, then allows a small smile."
        "Start the briefing yourself, emphasize the clauses and enforcement":
            "You take the makeshift stage and speak in measured, plain terms. Your words carve a map of guarantees — the escrow, the maintenance coop, the audit triggers. People ask sharp, practical questions; Jun answers with data, and the room appreciates the clarity. Elias Hart circles, adding color between your lines."

    # --- merge ---
    "The conversation continues with neighbors asking hard questions."
    "Elias Hart steps up either way, or he folds into the conversation as you lead; the result is the same: neighbors ask the hard questions. Sofia points to the clause about relocation protections. A shopkeeper wants"
    "to know about job guarantees for the maintenance cooperative. A schoolteacher asks if the data will be accessible to her students. You answer, and when you don't know, Jun or Hana Kim fills the gap with"
    "patient specificity. The exchange is messy and human and, crucially, engaged."
    "Hana Kim takes a step into the ring, the AR monocle catching sun like a silver wink."
    hide mateo_teo_rivera
    show hana_kim at left:
        zoom 0.7

    hana_kim "Open-source deployment layers will allow community techs to adapt to local contexts. We'll provide toolkits and training. As for the IP, we're proposing a license specifically for civil-safety deployments — a legal instrument that keeps corporate protections but allows community-level control."
    "A ripple of thoughtful murmurs runs through the crowd. You feel the tide turning; technical barriers are being translated into usable language, and the community is making them theirs."
    hide asha_rivera
    show mateo_teo_rivera at right:
        zoom 0.7

    mateo_teo_rivera "If this goes through, I want my team trained first. No second fiddle."
    hide elias_hart
    show asha_rivera at center:
        zoom 0.7

    asha_rivera "They're top of the list."
    "Elias Hart watches you — something like trust glinting in his sea-glass eyes, but not unambiguous. You file that look as another small movement toward mending what was strained."
    "Dr. Jun: (quiet, to you) 'This is the right balance: legal teeth, political theater restrained by clear breakpoints, and technical pathways that make participation possible.'"

    asha_rivera "It feels right. It feels like something we can show the council and the city that isn't just an idea."
    # play music "music_placeholder"  # [Music: The strings swell into a bright chord; the community chatter rises like a living chorus]
    "You spend the afternoon tightening language, listening, and letting the market's questions sharpen the covenant. Each suggested tweak — a clearer maintenance timeline, a defined audit interval, a binding penalty clause — makes the document leaner"
    "and stronger. The work is granular and slow, but you can see the arc: milling noise turned into ordered commitments."
    "Hana Kim pulls you aside as the sun slips toward a soft gold."

    hana_kim "Leon will want staged releases. He'll ask for metrics and PR moments. We can use that to our advantage, but we have to decide how much leverage we trade for speed."
    "You feel the decision like a hinge in the chest. Speed can save people in the short term; slow guarantees protect them forever. The hybrid pilot was supposed to be a bridge between those impulses — now you have to decide how to bolt that bridge in place."

    menu:
        "Push Hana to demand legal guarantees first — slow but strong":
            "You say it plainly. Hana Kim's jaw sets, and she breathes out a technical assent. The room around you seems to inhale with the same relief; some neighbors clap softly, approving the hard line."
        "Use staged public rollouts to build momentum while locking in milestones":
            "You suggest a middle way: use public momentum to secure faster commitments. Hana Kim nods, a plan already forming in her head; Jun raises a note of caution but agrees it could move the city faster. Elias Hart looks wary but intrigued."

    # --- merge ---
    "The drafting continues toward a finalized covenant."
    "You look at the document one last time — clauses marked, triggers highlighted, the maintenance cooperative spelled out in painstaking detail. The day has given you a thing of rough and honest beauty: legal language braided"
    "with community practice, tech pathways pried open and made usable, scaffolding for a partnership that feels like it could hold people."
    "Mayor Lila calls as the market hums toward evening; she's read the draft and wants to meet. Her voice over the line is brisk, hopeful."
    hide hana_kim
    show mayor_lila_ortega at left:
        zoom 0.7

    mayor_lila_ortega "Bring me the covenant and a clear ask. If the community signs publicly, I can shepherd the council. But I need a locking mechanism — something that ensures Aegis can't walk away."
    "You close your eyes for a breath. The market lanterns swing, and behind them the dark edge of the harbor glows faint. You think of the children chasing waves, the mural repainting a promise, Jun's careful"
    "hands. The pact you've been shaping is at once legal scaffolding and a moral promise. It deserves teeth."
    "You set the document on the table in front of you, fingertips tracing the margins where clauses live like small seeds waiting to sprout into policy. The path forward narrows into a single question with weight: how do you lock Aegis into a true partnership?"
    # play music "music_placeholder"  # [Music: A single rising chord, then a patient, expectant silence]
    hide mateo_teo_rivera
    hide asha_rivera
    hide mayor_lila_ortega

    scene bg ch11_e67f19_4 at full_bg

    menu:
        "Push for legally binding contracts with community veto and maintenance cooperatives.":
            jump chapter15
        "Stage a public joint rollout to create political momentum and pressure for guarantees.":
            jump chapter7
        "Propose a staged pilot with escrowed funds released only after community-audited outcomes.":
            jump chapter11
    return
