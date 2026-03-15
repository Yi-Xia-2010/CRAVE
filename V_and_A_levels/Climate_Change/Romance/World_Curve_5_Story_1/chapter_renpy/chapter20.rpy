label chapter20:

    # [Scene: TideLab | Late Morning — Rain Still Falling]

    scene bg ch11_d3396b_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain on corrugated metal, a distant gull calling once, like a punctuation.]
    # play music "music_placeholder"  # [Music: Tense, driving percussion under a steady synthetic swell]

    "You taste metal on your tongue again — the residue of too many meetings, too many deadlines. The ledger you signed is folded under your elbow; the words you wrote are still warm with ink" "Concurrent strategy — legal route continues. Community education & measured public actions to be scheduled. No unilateral protests. Secure evidence."
    "The room reacts to that sentence the way tidewater reacts to a storm: small, insistent movements building into an inevitable swell. Jules is sorting footage into labeled folders, fingers moving faster than her speech. Mateo is"
    "on the phone behind you, voice hushed but taut; you can feel the vibration of his knuckles against the counter when he hangs up. Luka Maren stands by the bench with his drone controller clasped like"
    "a compass — eyes flicking between the court filing printout and the live stream of a Corinne Voss PR drop on his tablet."
    show jules_park at left:
        zoom 0.7

    jules_park "We got raw footage from the west pier—storm surge models, and… footage of their excavation prep. Good angles. If we cut it with the tide-maps, it's visceral."
    "You look at the footage. The screen shows a crane silhouette against a bruised sky, bulldozers chewing at a shoreline. The image is curiously clinical; Corinne Voss's PR caption is the varnish."
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "We need context, not outrage. The filing needs evidence chain, timestamps, metadata. Jules, seal those originals and hand me a copy."
    "Jules: (nods, sharp) 'On it. I can scrub the watermarks if we need it for broadcast—'"
    "Luka Maren: (interrupting) 'No. Don't scrub. The chain of custody matters more than cinematic shots. If the video looks edited, Marina's affidavit will be shredded.'"
    "A small silence forms. It's not empty; it's loaded."

    amaya_reyes "We are threading a needle. Visibility helps — regulators notice loud things — but visibility also gives Corinne Voss an opening to discredit us."
    "Luka Maren: (quiet, measured) 'And there's another opening. Corinne Voss has been floating an invite to a shared research network. If I join, we could access their environmental monitoring feeds. Influence from the inside.'"
    "The air tightens. You can smell the wet fabric of Luka Maren's smock, salt and solder; a human counterpoint to the technical proposal."

    amaya_reyes "Influence is not neutral. It's optics. If your presence gets spun as 'insider support,' our credibility in court and with the town is compromised."
    show luka_maren at center:
        zoom 0.7

    luka_maren "I know. I also don't like feeling locked out of data that matters for the injunction. I could act as a data conduit—no public-facing deals, just access, and strict logs."
    "Mateo, who has been leaning against the sample shelf, finally folds his arms and steps forward."
    hide jules_park
    show mateo_reyes at left:
        zoom 0.7

    mateo_reyes "And what about the small stuff? Lines of credit, Amaya. We can't feed the boats if everything freezes. A moratorium that drags could sink families."
    "Abuela Rosa, steady as tide-rock, shifts her shawl and speaks in a voice that carries more history than any filing."
    hide amaya_reyes
    show abuela_rosa at right:
        zoom 0.7

    abuela_rosa "Courage must be measured. The law is a net; it catches those with the right weight. But nets tear. We need to know where to mend."
    "You feel the conversation pull you in all directions at once. There are legal levers, PR levers, human levers. Each one snaps against the others like rigging."

    menu:
        "Read the municipal notice aloud":
            "You pull the email open and let the room hear Tamsin's latest update—deadline language, procedural jargon, the hush of bureaucracy. Heads bend over the words, and the urgency sharpens."
        "Call Luka off-site to walk the data option":
            "You call Luka Maren's number and step outside into the rain; his voice is closer over the line, practical, and it gives you two minutes of focused reality: what feeds you can feed the motion — but not if integrity is burned."

    menu:
        "Let Mateo address the council first":
            "You step aside, and Mateo's voice carries across the chamber—raw, honest. It reframes the debate as real people vs. glossy models. The room shifts; some councilors frown, other faces soften."
        "Present the filing summary yourself":
            "You take the podium. Your voice is steady but quick. You lay out the evidence chain, the deadline, and the human cost. The council listens, a clock counting between words."

    menu:
        "Launch a coordinated public campaign tied to our legal filings (press, regulators, viral footage).":
            jump chapter22
        "Proceed quietly through precedent, aiming to win on technical legal grounds.":
            jump chapter8
        "Negotiate a conditional moratorium with Tamsin, using legal pressure as leverage.":
            jump chapter26
    return
