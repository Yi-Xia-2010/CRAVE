label chapter18:

    # [Scene: Neutral Warehouse (adjacent to Rooftop Nursery) | Late Afternoon]

    scene bg ch11_e67f19_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant drill hammers a syncopated rhythm; a gull cries; the hum of a nearby generator underpins conversation like an anxious metronome.]
    # play music "music_placeholder"  # [Music: Driving strings with urgent percussion — hope threaded through tension]
    "You step through the threshold and the humid air of the Low Row follows you in — warm, salt-sweet, full of soil and engine oil. Your chest is a drum; adrenaline and determination hum in your"
    "veins from the meeting with Kai. This is the logical hub where promises turn into appendices and signatures. The air tastes like possibility and diesel."

    scene bg ch11_e67f19_2 at full_bg
    "People are already clustered: Rafi with soil-streaked palms folded, Lio balancing a projector and grinning, elders with hands folded like prayer. Elias stands near the projector, trench coat sleeves pushed up, eyes rimmed with fatigue but"
    "focused. Kai waits with her engineers, jawset beneath the platinum bob, that porcelain pendant barely visible under her collar."
    "You draw a slow breath and let the soundscape settle into focus: the rustle of paper, a neighbor clearing a throat, the low murmur of agreement and dissent braided together. You feel the momentum you carried out of the last meeting tightening into something fiendishly real."
    show elias_kahn at left:
        zoom 0.7

    elias_kahn "Thank you for coming. We—' (he glances at you, then at the room) '—we're running against time. We need a path that protects people now and leaves options for the future."
    "You want to say the word you say to yourself when choices are hard: 'both.' But the room will not accept platitudes; it wants scaffolding and teeth."

    "Camila 'Kai' Navarro" "Our timeline can be executed in twelve months with provisional barriers and integrated corridors. We can deploy now, and the data shows a dramatic reduction in acute flood risk.' (she spreads a glossy drone print) 'In exchange, we require a performance clause tied to maintenance and integration rights for our monitoring systems. It's not control—it's accountability."
    hide elias_kahn

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A faint mechanical whir — one of Kai's tablets warming up]
    show dr_sima_raza at left:
        zoom 0.7

    dr_sima_raza "These projections align with emergency response thresholds. But they also show long-term accretion patterns that demand flexible management — wetlands require space to migrate. Concrete, if continuous, will cut off ecological feedback."
    "Rafi: (voice thick) 'We can't hand our shore over to a clause that lets paperwork decide when our roofs get emptied. People here fish, they sell clams, they grow tomatoes on roofs. This isn't an abstract risk.'"
    "You watch the faces as arguments line up like waves. Lio steps forward with a roll of painted canvas; he plants it against a pillar — a mural in progress: children on stilts, a festival of lights walking the tide. The image is defiant and fragile."

    menu:
        "Stand at the front and insist on community seats now":
            "You move to the pallet that serves as a podium, palms flat, and your voice slices through the noise: 'We will not accept temporary measures without permanent say.' The room stills, eyes on you."
        "Pull Elias aside and ask for a procedural lifeline":
            "You take Elias by the sleeve and tug him to the side. He recognizes the look—fatigue meeting resolve—and nods. 'If we do this through municipal channels,' he whispers, 'I can push for binding language.' He returns, steadier."
        "Call on Rafi to tell a story first":
            "You gesture to Rafi and he clears his throat, hands folding around the podium. The room leans in. An elder reaches for his arm as if to anchor the memory he will unfurl."

    menu:
        "Propose a performance metric that includes ecological indicators":
            "You propose a composite score: flood mitigation plus wetland migration allowance plus community livelihood indices. The engineers frown, then sketch. It turns the abstract into something they can test."
        "Insist on immediate provisional barriers before any legal language":
            "You press for speed. Kai's engineers smile like predators sensing permission; Elias's jaw tightens. The room divides between those craving instant safety and those fearing long-term loss."
        "Suggest an independent legal trust to hold the clause":
            "You outline a legally independent trust with community trustees and third-party auditors. The lawyers in the room lean in; it's a pivot toward enforceability, and the air tastes, for a moment, like a real compromise."

    menu:
        "Accept Kai’s fast-track with enforced oversight clauses.":
            jump chapter23
        "Push for an expanded municipal-coordinated compromise.":
            jump chapter40
        "Withdraw and devote all resources to a community-only pilot.":
            jump chapter43
    return
