label chapter19:

    # [Scene: TideLab | Late Afternoon]

    scene bg ch10_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain hardening on corrugated metal; a distant, rhythmic thump of a construction barge]
    # play music "music_placeholder"  # [Music: Low, urgent pulse — a cello with a clipped tempo]
    "You brush salt grit from the notebook's cover with the back of your hand and set it on the workbench as if laying down an accusation. Outside, the rain has gone from prelude to insistence; each"
    "drop is small percussion against the roof, counting down in a language you do not want to translate. The TideLab smells of wet rope, solder, and the herbal smoke Abuela Rosa leaves tucked in a corner"
    "to keep the damp at bay."
    "On the bench, a row of sensor logs waits like witnesses: black-encased recorders, a mesh of timestamped SD cards in ziplocks, and a stack of glass sample vials in a foam tray. You feel the weight"
    "of each thing like a ledger entry — small, precise obligations that will have to bear the next argument in court."

    scene bg ch10_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain hardening on corrugated metal; a distant, rhythmic thump of a construction barge]
    show jules_park at left:
        zoom 0.7

    jules_park "We photographed every marker this morning. GPS stamps, timestamped photos from two angles, and the timestamp on the controller matches the log on the sensor array."
    "You nod, but your mouth catches on the truth beneath the neatness: documentation does not mean justice. Documentation is dry paper held up to wet storms and hungry lawyers. Still, the work is precise and necessary."
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "Double locks on the ziplocks. Ledger entry for every transfer. No one carries a sample outside the lab without two signatures."

    jules_park "Two signatures, photo, and an audio note. I’ve been recording runs—background noise, voices, everything. You never know what will be questioned."
    "You lean over the bench, feeling the urgency like heat in your palms. Luka is kneeling by the server rack, small blue LEDs blinking like a nervous heartbeat. He runs his hand along a cable and"
    "looks up with that steady, softer expression that makes pressure less like a blow and more like a lesson in focus."
    show luka_maren at center:
        zoom 0.7

    luka_maren "I’ve layered the transmissions with a rolling hash and signed them. If anyone tries to claim tampering, the chain will show where packets diverged. Jules’ photographs and your physical logs will cross-verify timestamps. We can prove integrity."

    amaya_reyes "How long to finalize the encryption signatures?"

    luka_maren "Few hours. I want to run redundancy across offsite nodes — cloud mirrors, an air-gapped backup, and a notarized time-stamp from the municipal server. Tamsin's lawyer can notarize the chain when we hand it over."
    "There’s a tension under his words you can feel: hope folded into meticulousness, the kind that knows how fragile optimism is when it meets paperwork."

    menu:
        "Ask Luka to prioritize notarization now":
            "You push the stack of printouts toward him. 'Start the notarization sequence now. If we get hit with a notice, we need a public timestamp.' Luka's fingers hesitate on the keyboard, then move with calm precision."
        "Tell Luka to finish redundancy first":
            "You bite your lip and say, 'Finish redundancy. If the chain breaks because we rushed this, it’s useless.' Luka exhales and nods; he returns to the server with a softer urgency."

    # --- merge ---
    "The lab hums like a field hospital: triage of evidence instead of wounds. Jules moves between benches, labeling, photographing, narrating with the kind of thoroughness that is almost ritual. Each annotation in your ledger feels like a prayer for procedure: who handled what, when, where, why."
    "Tamsin arrives with a paper sleeve of municipal-stamped documents and an expression that is all bland professionalism and small panic."
    hide jules_park
    show tamsin_cho at left:
        zoom 0.7

    tamsin_cho "I found a municipal lawyer—Marina Keo. She’s worked environmental permits before, not a crusader, but she sees an exploitable procedural gap. If we can get a temporary restraining order while the injunction is filed, we might stall their approvals."
    "You clamp your hands together to hold steady. A restraining order is a blunt instrument and will invite spectacle — and countermeasures."

    amaya_reyes "How fast can Marina move? Corinne’s team is already pushing expedited permits."

    tamsin_cho "She'll move tonight if we hand over the notarized timestamps and chain of custody documents. But… she'll need a clear public record that the data is unassailable. Corinne’s counsel is already drafting a quick-approval package for the port expansion. Expect motion to dismiss and a counterpetition."
    "Mateo comes in from the doorway, rain dripping off his cap, and the familiar lines of his face look sharper in the lab light."
    hide amaya_reyes
    show mateo_reyes at right:
        zoom 0.7

    mateo_reyes "How long before we get something on the record? We’re losing two fishing spots to the dredge approvals this week. You know what that does to a week-to-week family. People don’t have patience for court paperwork."
    "Your chest tightens in a way that is old and private; guilt is a domestic animal you have habitually fed."
    hide luka_maren
    show amaya_reyes at center:
        zoom 0.7

    amaya_reyes "We’re building the system so it's defensible. If we rush and lose on a technicality, they’ll bury us."

    "Mateo (voice low, bitterly practical)" "If we stall, we lose the fishers’ moorings. If we move slow and win, what good is winning in twenty years when houses are underwater now?"
    "Abuela Rosa steps in as if the building itself opened for her. Her shawl is damp, the bright coastal motifs dulled by rain, but her eyes are clear and unyielding."
    hide tamsin_cho
    show abuela_rosa at left:
        zoom 0.7

    abuela_rosa "Long fights can outlast the hot flames of those who burn. You put water against iron; it takes time. The company has money and shiny words. We have history and patience that is older than their charts."
    "The carapace of your resolve flexes; Abuela Rosa’s voice is a balm and a challenge. Her faith in time is an argument against your present guilt, but it is not an answer to the fishing nets fraying at the docks."
    hide mateo_reyes
    hide amaya_reyes
    hide abuela_rosa

    scene bg ch10_98c6f2_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A new, sharper knock at the door — someone carrying envelopes]
    "The day accelerates. Somewhere between notarizations and envelopes, the town starts to fray at the edges. Volunteers who’ve been a backbone for months show up late, faces hollowed by extra shifts and unpaid bills. Jules’ camera"
    "reveals more than imagery; their footage documents anonymous letters slipped under doors and a truck idling by the shoreline during night surveys."
    show jules_park at left:
        zoom 0.7

    jules_park "We found tire tread marks at the north markers, and someone tried to chew through the sensor cable last week. I logged the audio clip. There's a muffled voice in the background. I can enhance, but—"
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "Enhance. And put that clip in the secure evidence archive. Mask identities where needed and keep the originals air-gapped."
    show luka_maren at center:
        zoom 0.7

    luka_maren "We should consider a limited public disclosure—release the raw data sets and the timestamp verification to the community portal. If people can see the logs themselves, it may push public opinion and relieve some pressure on volunteers."
    hide jules_park
    show tamsin_cho at left:
        zoom 0.7

    tamsin_cho "Public disclosure can help, but it also exposes the chain to public manipulation and wants a media narrative you may not control. Corinne's PR machine will spin anything we publish."
    "Your mind juggles variables: integrity versus momentum; patience versus immediate relief. Each option carries weight you have buried by becoming the person who takes responsibility."

    menu:
        "Push for limited public disclosure now":
            "You consider the scale: transparency could rally the town and make intimidation visible. 'Let's release a curated set—raw data with explanations,' you say. Tamsin's jaw tightens but she nods; Luka already fingers a drive."
        "Keep the archive sealed until the notarization is complete":
            "You shake your head and press your thumb to a printout. 'Not until we have notarization. Corinne will weaponize half-truths.' Luka's shoulders slump but he respects the decision."

    # --- merge ---
    "The morning that once smelled like routine documentation becomes a gauntlet. Corinne’s response is clinical and fast: public notices of expedited approvals, a glossy release showing smiling engineers and a schematic beach profile that removes neighborhoods"
    "with elegant clean lines. The municipal server posts an administrative notice that a revised permit is under consideration with an unusual 48-hour comment window."
    "Tamsin swears, slaps the tablet down, and begins rifling through precedent cases. Her mouth moves too fast; she’s used to bureaucratic time, not this compressed rush."

    tamsin_cho "They're framing it as emergency public works to prevent imminent hazard—legal language that can justify expedited procedures. If they get emergency authorization, our timeline collapses."

    amaya_reyes "Then we need emergency court motion to halt administrative processing until discovery is complete. Marina wants everything stamped tonight."
    hide amaya_reyes
    show mateo_reyes at right:
        zoom 0.7

    mateo_reyes "People are showing up at the docks already. They're honking. They want banners, signs, a march. The councilman called and said the town is cracking. If we don't let people act, they act without us and we lose the narrative."
    "The lab becomes an echo chamber of competing urgencies. You feel your pulse in the bones of your hand when you touch the ledger; every line is a potential argument and every blank an accusation."
    "Abuela Rosa finds your hand on the ledger and squeezes it with fingers that have weathered more storms than the town’s newest engineers."
    hide luka_maren
    show abuela_rosa at center:
        zoom 0.7

    abuela_rosa "You are not their conscience and not their jailer either. Keep the work tight, child. Keep your people fed with both information and small victories. Bring them in to see what you do. Let them hold the timestamps themselves."
    "Her practical wisdom is a small, defiant weapon against the corporate momentum. It gives you a new plan: education as tactic and a way to keep the town tethered to the slow engine of the law."
    hide tamsin_cho
    show amaya_reyes at left:
        zoom 0.7

    amaya_reyes "We’ll host a workshop at the Hall tonight. Show the chain of custody. Teach people to read their own data. If we bring them into the archive, they can act informed and reduce reckless moves."
    hide mateo_reyes
    show jules_park at right:
        zoom 0.7

    jules_park "I can run a live demo. Show how a timestamp breaks if someone tampers. Make it visceral."
    hide abuela_rosa
    show luka_maren at center:
        zoom 0.7

    luka_maren "I'll prep a simplified packet — how to verify the rolling hash, how to log a transfer. If we teach volunteers the method, it’ll reduce errors and make testimony stronger."

    "Tamsin (bitter)" "And it also makes us vulnerable to PR. If this goes sideways, it becomes a story about 'town paranoia' instead of 'engineering overreach.'"
    hide amaya_reyes
    show mateo_reyes at left:
        zoom 0.7

    mateo_reyes "Either we get them to see the ledger or the ledger means nothing to the people who feel the water in their feet. We can't build a case in a bubble."
    "The decisions pile like coral growth: the legal track requires patience and impeccable records. The community needs movement and tangible defense. Corinne's machinery is fast and will use legal technicalities and PR to bulldoze momentum. Your"
    "chest aches with the old guilt: you chose the legal path, and neighbors are paying the interest."
    "You close your notebook and listen to the rain for a moment, counting the beats. The lab’s lighting seems harsher now; the workbenches look smaller under the weight of upcoming hearings and threats. The arousal that"
    "began as methodical energy sharpens into a high, painful focus — urgency braided with anxiety."
    hide jules_park
    hide luka_maren
    hide mateo_reyes

    scene bg ch10_98c6f2_4 at full_bg
    # play music "music_placeholder"  # [Music: The pulse quickens — a high, insistent violin underscores the next moments]
    "You stand, the decision knot tightening like a noose you’re tugging to measure your own resolve. Around you, people shuffle paperwork, tape evidence bags, rehearse explanations for non-technical neighbors. The town's patience is a taut string."
    "You think of the tide-maps in your field notebook, of the names of streets that will vanish if the wrong permit passes; you think of Luka staying up all night to perfect a signature algorithm; you"
    "think of Mateo’s nets, the sound of their engine, the smell of diesel and salt. You feel Abuela Rosa’s practical faith in slow fights like an ember you can coax into heat."
    "There is no longer a single clear path. The legal engine is assembling; it will be slow and defensible. But the water at the docks is rising and Corrine’s approvals are moving with a speed that"
    "smells like inevitability. The town is fraying into impatience and small acts of defiance that could either strengthen the case or give the company grounds to paint the community as irrational."
    "You close your eyes for a second and let the room's noise hammer through you — the printers, the murmur of voices, the rain. The decision you must make is not about law or protest alone;"
    "it is about pacing the town’s anger so it becomes sustained power instead of a scattering flame."
    "You draw a breath that tastes like metal and rain and resolve."

    "You reach for the ledger and write—slow, neat script" "Concurrent strategy — legal route continues. Community education & measured public actions to be scheduled. No unilateral protests. Secure evidence. Marina to file emergency motion tonight."
    "The pen feels heavier than it should. Around you, people look up, waiting to see which version of you will hold — the organizer, the lawyer, the sister, the stubborn idealist."
    "In the hallway, a municipal email pings: a new notice. Corinne’s PR feed posts a staged photograph — a smiling engineer pointing to models, the caption promising rapid protection. Comments flood in. The town's patience and your legal timeline both hang in the balance."
    "You feel the moment pull taut, like the last piece before a seam splits."

    scene bg ch10_98c6f2_5 at full_bg
    # play music "music_placeholder"  # [Music: Cut to a single sustained, strained note]
    "You know the next steps: notarization, filings, a hearing that will be public, a media cycle that will chew at your defenses. You know the stakes: livelihoods, homes, and the slow arithmetic of sea-level inches. You know the cost of hesitation and the cost of the wrong kind of action."
    "You open your eyes. The lab waits. The town waits. The rain does not slacken."
    "Page-turn: You step toward the phone to call Marina and Tamsin, ready to set the emergency motion in motion, but your thumb pauses over the contact labeled 'Community Channel'—because the choice ahead is not procedural but"
    "moral, a line between method and momentum that will cry out in the weeks to come."

    scene bg ch10_98c6f2_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter20
    return
