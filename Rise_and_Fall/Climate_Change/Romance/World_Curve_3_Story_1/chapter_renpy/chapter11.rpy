label chapter11:

    # [Scene: Tidewatch Coastal Lab | Dawn]

    scene bg ch11_e67f19_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The lab's pumps thrum a steady heartbeat; a lone gull calls, distant and bright.]
    # play music "music_placeholder"  # [Music: Quiet, hopeful strings undergird conversation]
    "You come in with the rain still beading on your jacket, the envelope from last night pressed flat in your chest like a held breath. The lab smells of coffee and ozone and damp plastic—the familiar, practical scent of a place that translates weather into numbers and hope into plans."
    "Claire Hsu looks up as you set the packet on the stainless bench. Her face is lit by the tablet; the sharp silver at her temples catches the light like a punctuation mark. She doesn’t reach"
    "for the papers immediately. She watches you instead, and you feel the question in that look: Are you ready for the world to know?"
    show dr_claire_hsu at left:
        zoom 0.7

    dr_claire_hsu "We ran the sensitivity analyses you asked for overnight. I scrubbed the inputs, blind-tested with three independent datasets. The anomalies you flagged—those redirected surge vectors—hold. They're not artifacts."
    "You let out a breath you hadn't known you'd been holding. The rush is part relief, part the vertigo of stepping off a dock into deep water with a rope tied to your waist."
    show mara_solano at right:
        zoom 0.7

    mara_solano "So it's real. Not just a fluke."

    dr_claire_hsu "Real. And reproducible. Which means the model Elena's team used can't account for certain coupled feedbacks in the redeveloped waterways. In plain language: under certain storm trajectories, the barrier could funnel water where neighborhoods already on the edge are sitting."
    "Her voice is calm, precise—an anchor. But the way she taps the tablet, like folding a corner of a map, betrays a mix of scientific vindication and dread."
    "Jonah Reyes arrives as if on cue: wet hair flattened to his skull, camera strap crossing his chest, eyes bright and quick. He sets down a thermos and a roll of film—habit, not necessity—and grins at you with that unstoppable, human optimism he carries in the crease of his smile."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "You look like someone who just found the secret page in a book. Did we?"

    mara_solano "We did. Claire validated it. The packet's ready for an independent review. We can—"
    "Claire Hsu interrupts with the practicality that steadies you."

    dr_claire_hsu "We prepare a controlled release. Timestamped dataset, methods, third-party reviewers. We notify counsel and the community archive simultaneously. We avoid speculation, avoid theatrics. The science must be untouchable."
    "The plan is meticulous; it is the instrument you trust more than the rhetorical flourish. Still, the world outside the lab will choose what kind of story it wants to tell."

    menu:
        "Lean scientific: release raw data and methodology":
            "You force your fingers to type the sentence that will accompany the datasets: 'We present raw findings for independent verification.' It feels austere — like ledger entries in a ledger that might need to stand in court."
        "Frame it human: lead with the community impact statement":
            "You draft the opening in a different voice: 'These findings point to immediate risks for people's homes and lives.' Your chest tightens; you can already hear how the cameras will cushion or sharpen that line."

    # --- merge ---
    "..."
    "Claire reads both drafts with a something like approval and worry mashed together."

    dr_claire_hsu "Both. The raw data and the statement. The community must hear what it means, and scientists must be able to reproduce it. We keep control of the narrative by being transparent, not by clenching our teeth."

    jonah_reyes "I'll photograph the town as we release. People in frames, not graphs. Pictures stick."
    "You nod. The compass at your throat feels warm against your skin; the pendant's bronze face mirrors a sliver of the lab's light. There's an odd, steadying comfort in that small ring of metal."
    # play sound "sfx_placeholder"  # [Sound: Notification ping — a press inquiry; another — Elena Voss's legal liaison seeking 'clarification.']
    # play music "music_placeholder"  # [Music: Strings swell, hopeful but taut]
    "Claire frowns at the pinging tablet."

    dr_claire_hsu "They're moving fast. Legal's already sniffing at the edges. Expect a counter-narrative. Expect demands for retraction."

    mara_solano "Then we move faster. Timestamped packets, chain-of-custody logs, community witnesses. We invite independent reviewers today."
    "Jonah Reyes palms your shoulder — a quick, reassuring touch that feels like a small tide against your shore."

    jonah_reyes "We don't get to be perfect. We get to be honest. That's the point."
    hide dr_claire_hsu
    hide mara_solano
    hide jonah_reyes

    scene bg ch11_e67f19_2 at full_bg
    # [Scene: Town Hall Plaza | Midday]

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Microphones hum, murmurs swell into shouts; camera shutters—Jonah's steady, others frantic—click like rain on metal.]
    # play music "music_placeholder"  # [Music: Brassy, rising ensemble — forward momentum]
    "You stand behind the podium with Claire at your side, Jonah a few rows back with his camera. Elena Voss is there in her immaculate coat, flanked by composed spokespersons and a legal team wired with"
    "quiet confidence. The press is a hungry tide: lenses, notepads, flash. The world is watching, which is the point you insisted upon."
    show mara_solano at left:
        zoom 0.7

    mara_solano "My name is Mara Solano. I grew up here. I studied these marshes. We are not just data points."
    "Your voice finds a cadence. The plaza narrows; every face becomes a map of weathered choices. You speak in the small, precise way that carries the conviction of someone who has spent nights with tide maps and mornings on soggy piers."

    mara_solano "Claire Hsu and I are presenting independent analyses that show the proposed engineered barrier underestimates redirected surge for certain storm tracks. That scenario places neighborhoods at increased risk. We are releasing our methods and data for third-party review and asking the council to issue a temporary injunction until an independent panel reviews this evidence."
    "A ripple moves through the crowd — not outrage, exactly, but a collective inhalation. Jonah's camera clicks: a shot of Rosa and Mateo in the front row, aprons folded across their laps; Aunt Pilar's hands, knuckles white with resolve; Councilor Avi's face, a study in contained calculation."
    "Elena Voss steps forward with a practiced smile, steel-gray eyes cool and certain."
    show elena_voss at right:
        zoom 0.7

    elena_voss "The company stands by its models. We welcome scrutiny, of course, but let's be clear: delay means delaying critical infrastructure that will protect thousands. We cannot let fear stall progress."
    "There's a friction in the air — two logics colliding. Her words are smooth and confident; yours are textured with local knowledge and human cost. Neither is wholly wrong; both carry power."
    "Councilor Avi Malhotra moves between: measured, linen suit creased with the day's work."
    show councilor_avi_malhotra at center:
        zoom 0.7

    councilor_avi_malhotra "We must weigh both the immediate need for defenses and the risk Claire and Mara present. This body will hear from independent reviewers. There will be testimony. Calm, please."
    "The hearing becomes electric. Friends swell in the crowd, strangers lean forward. The press hones on images: Jonah's photograph of market stalls under a bruised sky, Elena's spokesperson posing with a rendering of a gleaming barrier. Narratives form in the gaps between sentences; the cameras choose what to frame."

    menu:
        "Speak only to the science from the podium":
            "You finish your prepared statement, let Claire take the technical lead, and step away from the mic. The clarity of method cuts through emotion; some listeners shift uneasily, craving a human face."
        "Tell a story of a family at risk":
            "You pivot, voice roughening as you tell of a childhood storm and a neighbor's house that never recovered. The crowd presses closer; some faces soften, others bristle at the emotional appeal."

    # --- merge ---
    "..."
    "Claire takes the mic after you and walks the room through the reproducibility steps. Her testimony is surgical and human all at once: she names the data, the tests, the reviewers lined up to validate. Each sentence is a brick placed in a fragile bridge from science to policy."
    hide mara_solano
    show dr_claire_hsu at left:
        zoom 0.7

    dr_claire_hsu "We do not ask for a halt because we prefer one narrative over another. We ask because the methods and results demand an impartial assessment. If the models fail in the ways we've shown, the consequences are not theoretical."
    "Her authority makes a dent in the room. Reporters scribble; a cameraman sweats under hot lights."
    "Then the inevitable roar: Elena's lawyers file a motion even as the hearing proceeds. The plaza hears of it like a distant storm front: legal filings, threats of suit, demands for retraction. Someone in the crowd"
    "shouts that the company is being smeared; someone else accuses your team of stalling progress."
    "The town fractures in slow grooves: cheers from neighbors who remember losses; anxious murmurs from those who work for companies tied to Voss's contracts and fear livelihoods evaporating. The mood balances precariously on whether community control can translate into financial security."
    # play sound "sfx_placeholder"  # [Sound: The legal team's recorded statement; a lawyer's clipped voice mentioning 'reckless interference.']
    hide elena_voss
    hide councilor_avi_malhotra
    hide dr_claire_hsu

    scene bg ch11_e67f19_4 at full_bg
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "They'll try to make it look personal. They'll spin it into a story where we are villains or petty. We need to keep the facts in front of people."
    "You feel the smear like a burn on the back of your neck. It is simultaneously absurd and dangerous — the way a rumor can be a small match in a coastal wind. You want to"
    "answer every lie, to set the record clean, but Claire's earlier counsel echoes: transparency, restraint, reproducibility."
    # [Scene: Town Hall steps | Late afternoon]
    # play music "music_placeholder"  # [Music: Resilient, rising chords]
    hide jonah_reyes

    scene bg ch11_e67f19_5 at full_bg
    "News of the model's flaws travels. National outlets pick up the thread. The Department of Coastal Safety requests files; a public interest group offers legal aid. Grant officers call; funders ask for proposals. Community groups mobilize on the boardwalk; volunteers begin mapping parcels for interim wetland projects."
    "A temporary injunction is announced: the council, under pressure, accepts a pause pending the independent review. For a moment, the world seems to tilt toward the possibility you always fought for — the community breathing room to craft its own adaptation."

    scene bg ch11_e67f19_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Cheers and sobs threaded together; someone rings a small bell in the crowd.]
    "Aunt Pilar hugs you so tight you can feel the salt of many years on her face."
    show aunt_pilar at left:
        zoom 0.7

    aunt_pilar "You did good, mi'ja. We can breathe."
    "You want to believe it will be straightforward from here: science validated, injunction in place, the town protected. But the opposing tide does not relent. Legal threats keep whispering at the edges of every phone call."
    "Anonymous posts become a smear campaign—soft insinuations about sabotage, about motives. Funders waver under pressure from shareholders and acquisition rumors. Your name and Jonah's are threaded into ugly articles that suggest impropriety without evidence."
    "Jonah Reyes sits beside you on a damp bench near the boardwalk, camera idling in his lap. He looks at you—his amber eyes steady, tired but fierce."
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "They'll try to make us small to make the problem smaller. We don't let them."
    "You take his hand; it's a small human anchor in a sea of headlines."
    show mara_solano at center:
        zoom 0.7

    mara_solano "We keep the record open. We keep the community in front. We don't play into their attempts to isolate this as a personality fight."

    jonah_reyes "And when they push harder?"

    mara_solano "We push harder. But we have to pick where to push. We can go national, force the system to reckon; we can bargain for a local compromise that keeps community power; or we can step back, keep working quietly and rebuild what we can if the reputation hit is too high."
    "The rise you’ve been feeling all day collects into a single, pointed crest: revelation has opened a path. Doors you thought bolted have eased. People rally, funds move close enough to be practical, Claire's credibility buys"
    "time—and yet the cost is clear: personal attacks, legal teeth, and a town that now must choose."

    menu:
        "Answer every smear publicly":
            "You draft a line-by-line rebuttal, press releases and social media posts queued. It's cathartic and dangerous — a counterassault that could keep the truth visible or drown your message in controversy."
        "Hold public silence, amplify community voices":
            "You decide to let the community's many voices take the lead — market vendors, Aunt Pilar, volunteer organizers. It diffuses the personal target but requires patience and trust in others to carry the story."

    # --- merge ---
    "..."
    "The phone in your pocket vibrates with offers and threats, grant solicitations and menacing legal counsel. In the hush between tides you feel your own moral compass tug: the promise to protect this place, the obligation to the truth, the ache for partnership that has sustained you through storms."
    # play sound "sfx_placeholder"  # [Sound: A distant siren, not panic but continuing necessity; the pumps keep their rhythm.]
    "You stand at the intersection of consequence and invitation. The town has begun to rally; the hole in the plan has been exposed and the first stones of a different future are being laid. The climb will be steep. The air tastes of salt and possibility."
    # play music "music_placeholder"  # [Music: Crescendo—warm, ascending]
    hide aunt_pilar
    hide jonah_reyes
    hide mara_solano

    scene bg ch11_e67f19_7 at full_bg
    "You breathe in rain and possibility and the resonance of people's faces. This is the moment where tactics and values must find a shape."
    # [Decision Handover — Major Decision Point]
    "You must choose how to follow the exposure."

    menu:
        "Push the full expose nationally—force systemic reckoning.":
            jump chapter12
        "Use the leverage to negotiate a local compromise that enshrines community control.":
            jump chapter12
        "Pull back the public release to control fallout—focus on quiet restoration.":
            jump chapter15
    return
