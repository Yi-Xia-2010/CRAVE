label chapter3:

    # [Scene: City Hall | Late Afternoon — Council Hearing]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense, rhythmic underscore — percussion like a quickened pulse]
    # play sound "sfx_placeholder"  # [Sound: Rain pattering on glass, the soft scrape of chairs, murmured council voices fading as the room settles]
    "You step into the chamber and the air tastes of cold coffee and old varnish — the city’s breath held in a throat of polished mahogany. The gallery is fuller than you expected: neighbors in waxed"
    "jackets, a handful of Spire regulars, and names on badges that mean late-night tool runs and shared tarps. Your chest gives a small, deliberate squeeze; the notebook at your hip feels like an anchor and a"
    "fuse at once."

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A pen cap clicks in your pocket like a tiny metronome]
    "Ten minutes. The number arrives in the same way tide data has always arrived to you — not as a distant prediction but as a wave with teeth. Ten minutes to hold a coastline in public"
    "language, to make people who prefer graphs feel the weight of a home that smells of kelp and frying oil."
    "Irene Voss stands at the dais. Her steel bob is a blade that frames her face; her gray eyes sift through the room like a referee counting fouls. Behind her, Luca’s renderings gleam: broad machines, concrete"
    "ribbons along the water, glittering promenades that promise regained land and corporate logos. They cast slick shadows across the council floor."

    "Irene Voss's voice when she speaks is clear, practiced" "We need decisive infrastructure, scalable, financed. My proposal secures the shoreline and the jobs we need."
    "You can feel Sami at the back of your vision — a bright stitch in the gallery — humming like a charged wire. Elliot Chen catches your eye and gives you a small, almost shy lift"
    "of the chin, like a craftsman handing over a model and asking, without words, Will you take it? Dr. Noor sits with worn folders; her palms rest on tide charts as though to steady them."

    menu:
        "Glance at Elliot's tablet one more time":
            "You let your thumb flick the edge of the tablet screen; sensor graphs glow, a steady chorus of blue and green. Elliot leans in, whispering a last calibration: 'If the storm window stays within this, the living cells will root.' His voice is quick, earnest."
        "Scan the crowd for familiar faces":
            "You sweep the gallery: Mrs. Alvarez with her quilted tackle bag, council aides in damp suits, your neighbor from Dock 4 whose kid still thinks the harbor is a swimming pool. Sami catches your eye and nods—small, fierce encouragement."

    # --- merge ---
    "The moment tightens; you return attention to the chamber."
    "You breathe. The building's acoustics make your inhale loud. This is more than diagrams; it is a ledger of who you are willing to trust with the future."

    scene bg ch3_98c6f2_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low electrical hum from the demo box in the corner — a pulse like a heartbeat]
    "You rise when your name is called. Your voice wants to keep some words in a safe pocket, but the room expects you to unfold everything you know. You open your mouth and the first sentence lands in the chamber with the clean, inevitable sound of a dropped tool."
    show maya_rios at left:
        zoom 0.7

    maya_rios "Councilmembers, neighbors — the Harborfront is not a problem to be moved. It's a system: homes, boats, small businesses, people who have responded to the sea for generations. Our proposal starts where the water meets life — a living seawall prototype, community labor credits, and a retrofit pilot for the most vulnerable terraces."
    "A murmur; a soft shuffle like wind through reed. You feel, behind the professional cadence, the memory you do not want to carry into the room—the laugh of your brother, the way he sprinted when water"
    "rose too fast and you couldn't reach him in time. The memory is a stone you must place precisely or it will break the surface tension of what you say next."
    "You keep your hands steady. Your training shapes the second paragraph: data points that anchor hope in numbers. Elliot Chen had uploaded the prototype's sensor run; Dr. Noor's scenarios bracket the worst cases and the likely outcomes. You let them breathe into your language."

    maya_rios "Our sensors—' (you reach to the tablet) '—show early root adherence within seventy-two hours in simulated surge conditions. With community labor credits, we can deploy local teams, keep costs low, and bind maintenance to the people who will live with it. The retrofit pilot reduces interior flood risk for sixty-eight percent of units in the at-risk terraces on initial modeling."
    show dr_noor_patel at right:
        zoom 0.7

    dr_noor_patel "The tidal projections are convergent with our model. Given phased monitoring, the prototype provides both mitigation and data for scaled deployment. It's low-cost, adaptive, and offers less ecological disruption than concrete barriers."

    "Councilperson" "Ms. Rios, how do you mitigate for rapid-onset events?"
    show sami_alvarez at center:
        zoom 0.7

    sami_alvarez "Make them see people, not pixels."
    "You modulate. You fold in a line about volunteers and neighborhood maintenance, about training that doubles as employment. You mention the labor credits again because it is the hinge between civic infrastructure and livelihood — between technical efficacy and dignity."
    "Elliot Chen, when you gesture toward the tablet, offers another quick exchange at your elbow."
    hide maya_rios
    show elliot_chen at left:
        zoom 0.7

    elliot_chen "If we add live telemetry during the pilot, we can prove adaptive response. It writes the maintenance schedule for us and shows the council the savings."
    hide dr_noor_patel
    show maya_rios at right:
        zoom 0.7

    maya_rios "It buys the city learning in months, not years. It keeps displacement off the table by using salvaged materials and local labor."
    "The chamber shifts. A section of the council leans toward the promise of innovation; another bristles at the implication that grassroots teams can be trusted with public safety. Luca rises then, silky and precise."
    hide sami_alvarez
    show luca_marin at center:
        zoom 0.7

    luca_marin "With all due respect, prototypes are romantic until a storm hits. Our design guarantees shoreline recovery—fast. Funding that comes through private partnerships can be mobilized in months, not seasons. It returns property to productive use."
    "Irene Voss smiles then, measured: a flat, professional certainty that leans on precedent as if precedent were a law of nature."
    hide elliot_chen
    show irene_voss at left:
        zoom 0.7

    irene_voss "We cannot risk experimenting on people's homes when the next season could mean catastrophic losses. The project I propose is financed and fast. It secures jobs. It secures the waterfront."
    "There's a pitch to her voice—smooth, political—that draws nods from the cautionary. You notice the room splitting along predictable lines: financial security on one side, community agency on the other. But the split is not purely ideological; it's a ledger of fear and hope."

    menu:
        "Call out the displacement risk directly":
            "You let the word 'displacement' land like a bell. A councilmember frowns; a developer in the room shifts. Sami's jaw tightens and you see someone in the gallery start to whisper. The word gives faces to your data."
        "Emphasize the job-training angle":
            "You pivot to the labor credits and the training program. The word 'jobs' softens some stiff faces; a few council aides jot numbers. Elliot's eyes shine a fraction — practical language opening practical doors."

    # --- merge ---
    "The choice reframes the room's reaction; you continue your testimony."
    "Irene Voss's rebuttal is surgical: she frames urgency and scale as moral imperatives. Luca places an offer on the table—private funding, expedited construction, a rosy economic forecast. The clauses about eminent sale are thinly stated, paper-thin, and you feel the breath of compromise across the room."

    "A councilmember asks you a direct question about governance" "How will you ensure accountability and maintenance?"

    maya_rios "Community stewardship, public monitoring, and transparent reporting. We couple volunteer labor with paid oversight positions funded through reduced insurance costs and maintenance credits. The system is designed to be resilient and to grow with data."
    "Another hand shoots up. 'And if a prototype fails?'"
    "Your pulse answers before your mouth does. The chamber's acoustics make each inhalation a public act. You think of the worst-case simulations and Dr. Noor's cautious optimism. You think of the practical, honest sweat of Elliot"
    "Chen’s team at the Spire — nights spent wiring sensors and seeding moss. You think of Sami's hands, always ready to paddle into something dangerous for a neighbor."
    "Dr. Noor stands briefly to reinforce the point, her tone softening with the weight of long experience."
    hide maya_rios
    show dr_noor_patel at right:
        zoom 0.7

    dr_noor_patel "Every engineered system can fail. The point of a pilot is to learn and to adapt. If you build only what past precedent dictates—concrete and absolute—you lose the chance to reduce harm without wholesale displacement. Adaptive systems give you the chance to iterate toward safety."
    "Elliot Chen leans forward from the gallery, his voice carrying an earnestness that slices through formality."
    hide luca_marin
    show elliot_chen at center:
        zoom 0.7

    elliot_chen "We can get demonstrable, city-credible results within a season. Give us oversight, give us a probe area, and we'll deliver monitoring reports that matter."
    "You feel the room compress. The clock on the dais ticks in a sound that now matches the music under your ribs. Hearts in the gallery beat like carp under skin. The tension is dense and electric; every sentence becomes a lever."
    "You find yourself at the ethical map you promised earlier. Each route on the map has a coastline: conservation with community strength; public escalation; or pragmatic compromise. Each requires a different trust, a different kind of letting go."
    "Your internal voice lines up the options with painful clarity:"
    "- Stand with Elliot and push for a community-led pilot — trust neighbors, prototype first, hope to prove and protect without displacement."
    "- Join Sami and Dr. Noor; escalate public pressure and demand hearings — raise the stakes in public, risk polarizing moderates but possibly force more transparency."
    "- Negotiate with Irene Voss and Luca for funded infrastructure in exchange for concessions — secure immediate resources, accept political and ethical cost, and hope to protect homes through compromise."
    "The chamber is louder than before; rain against the windows has become a drumroll. Your hands want to do what they always do — build something with your own fingers until it will hold. But this"
    "is a different kind of construction: it asks you to choose whom you will bind into the work."
    "Irene Voss watches you with a look that is both appraisal and invitation. Sami's jaw is set like a hinge. Elliot Chen's eyes are open, warm, asking not for rescue but for partnership. Dr. Noor is"
    "quiet, the way people are before a lab door opens. Luca smiles with the ease of someone who knows how to translate urgency into contracts."
    "Your ten minutes have narrowed into one breath. The room waits — not hostile so much as expectant — as if the city itself leans in to hear which promise you will put weight behind."
    # play sound "sfx_placeholder"  # [Sound: A distant thunderclap rolls, the room exhaling as one]
    "Your pulse thrums in your ears. Hope sits at the center of the pressure like a buoy. You feel its buoyancy — positive, fierce — and the rapidness of your heartbeat forces clarity out of fear."
    "This is the moment: the choice will map the next season of work, the next wave of neighbors saved or uprooted, the trust you are willing to open yourself to."
    "You let the ethical map hang in the air and you prepare to set your direction."
    # play music "music_placeholder"  # [Music: Crescendo to a sharp, urgent chord — highest arousal point]
    hide irene_voss
    hide dr_noor_patel
    hide elliot_chen

    scene bg ch3_98c6f2_4 at full_bg

    menu:
        "Stand with Elliot and push for a community-led pilot.":
            jump chapter4
        "Join Sami and Dr. Noor; escalate public pressure and demand hearings.":
            jump chapter7
        "Negotiate with Irene and Luca for funded infrastructure in exchange for concessions.":
            jump chapter10
    return
