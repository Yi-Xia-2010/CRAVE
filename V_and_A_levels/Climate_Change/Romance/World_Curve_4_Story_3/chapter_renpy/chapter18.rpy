label chapter18:

    # [Scene: Promenade | Night]

    scene bg ch11_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Urgent strings, quick tempo]
    # play sound "sfx_placeholder"  # [Sound: Phone buzz; distant gull calls; the soft slap of waves against pilings]

    "You taste salt and old regret and the brief tinny authority of your phone screen as it lights up in your palm. The notification is a raw cut — a link that feeds into a thread, then another, then a rising chorus of outrage. Someone has posted the contract. Someone highlighted the phrase that everyone has been afraid of" "investor claims under unforeseen exigency."
    "Your breath is quick, the frayed cord of the compass rubbing against your thumb as if reminding you there are anchors older than clauses. Around you, lights from the Beacon halo the promenade, clinical and alien"
    "against Marabel's worn wood. The town's hum sharpens into jagged edges: forum posts, messages, the low panic of the market vendors packing up early."
    "You swipe. Replies cascade—angry, scared, incredulous. Insurance companies respond with automated notices; a property group you've seen in glossy pamphlets starts asking thinly veiled questions about waterfront titles. It's not just words on a screen. The leak becomes leverage in seconds."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "I saw it. We need to anchor people—facts, steps. Panic fills silence faster than information."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "They'll use fear to move titles and payments. That clause—it's a lever. (You swallow.) We have to stop them from turning this into a shopping list."
    "Noah Reyes studies the thread, fingers tapping a rhythm. He isn't afraid of the arguments; he's afraid of the fracture those arguments make in people. His gaze slides from your face to the boardwalk where a small knot of elders is gathering, uncertain."

    noah_reyes "I'll get Mayor Rosa on a press update. You handle logistics—Eli, Marta, volunteers. Keep the narrative local: who's helping, where to go, what to expect."
    "You nod, but your mouth tastes metallic. Logistics now means triage: marsh reinforcement, sandbags at low points, ride plans for those who can't climb stairs. It also means public trust—it means writing the first sentence people will repeat when their hearts are thrumming."
    # [Scene: Boardwalk | Continuous]
    hide noah_reyes
    hide asha_moreno

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slap of boots, shouted directions, the creak of pulley ropes]
    # play music "music_placeholder"  # [Music: Percussive beats increase]
    "Eli arrives with a boat slung on his shoulder and a quiet you can fold into. He moves through the crowd, calling names, guiding elders toward the launch. Marta is at the raised gardens, barking orders"
    "into a megaphone, then softening into hands-on comfort as she helps someone climb onto a platform planted with tomato cages and pots."
    show eli_duarte at left:
        zoom 0.7

    eli_duarte "Asha—you're taking the marsh line, right? That saddle where the test wall links to the old reed beds? If that goes, the road's a river."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Yes. We'll reinforce the berm and link the coir rolls. Noah's coordinating the lifts."
    "Eli's jaw tightens—his face speaks of hands that have always fixed things with wood and salt. You share a look that doesn't need words: the old boatyard taught you both how fast repair becomes prayer."
    "Marta, wiping soil on her hands, cuts in."
    show marta_chen at center:
        zoom 0.7

    marta_chen "We can fold the gardens into refuge points. Folks know where they are. Use the solar lamps, string lines. But we need manpower by the estuary, and we need it now."

    asha_moreno "I'll split teams—two to the berm, two for sandbags, a couple with Eli for the ferry runs. Mayor Rosa—"
    "A volunteer interrupts, breathless and trembling, waving her phone. 'There's video—Beacon sensors picked up a pressure drop at the test wall. It's trending. It's—'"
    "The word trails into the surf and then becomes a command: The Beacon. The lab. You and Noah exchange a look that tastes like glass."

    menu:
        "Send more hands to the Bora berm":
            "You call out across the boardwalk, reallocating volunteers. Hands move faster; the berm line tightens, but two ferry runs are delayed."
        "Keep the ferry schedule prioritized":
            "You signal Eli to keep the launches rolling. Elders are safe quicker, but the berm line loses crucial muscle. You feel the trade in your ribs."

    # --- merge ---
    "The operations continue with altered manpower distribution and growing urgency."
    # [/INTERACTION]
    # [Scene: Tidewatch Lab | Moments Later]
    hide eli_duarte
    hide asha_moreno
    hide marta_chen

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Static from radio, low hum of servers]
    # play music "music_placeholder"  # [Music: High-pitched synth under current strings]
    "You slide into the lab, the air smelling of ozone and damp charts. A screen glows with a thin line of telemetry, then it stutters — and the waveform becomes a scream. The test wall's live"
    "feed shows a seam opening at the seam joint, water pressing through like a hand forcing a seam."
    "Technicians bark over the comms. Caleb, Lila's junior engineer, appears at the door, blurred and wet, eyes wide with the kind of fear you only see when someone's whole certainty collapses."
    show caleb_osei at left:
        zoom 0.7

    caleb_osei "We—it's a stress failure. Sensors... they're recording differential loads. We didn't predict this timing."
    "Lila Park's message arrives like a small, formal storm: an apologetic text, her words crisp in the clinical light. 'We are mobilizing resources. Our teams are en route. We will make this right.'"
    "You read the message and feel both relief and a new tightening. Her engineers are human, but the contract's teeth are already gnashing the town's heels. The leak sits open in your phone, the clause framed in dishonor."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "She says they're on their way. That doesn't fix the clause that's now a legal wedge. It doesn't stop investors from smelling opportunity."
    "Noah Reyes places both hands on your shoulders—not to steady a falter but to give you a place to brace the pain."
    show noah_reyes at center:
        zoom 0.7

    noah_reyes "We can't unring this bell. But we can show people we're acting. We need a clear timeline: what's being deployed, where shelters are, what residents should do."
    "The lab's screens hiccup again. The Beacon's sensor feed overlays a live map—water encroachment in red, the test wall's seam flashing. The model predicts a rate of ingress you haven't seen in simulations. The air tastes like the inside of a held breath."
    "Mayor Rosa's voice threads through the comms, firm and too small."
    hide caleb_osei
    show mayor_rosa_alvarez at left:
        zoom 0.7

    mayor_rosa_alvarez "Asha, Noah—what's our message for the town? Lila says she can bring crews and materials. People are scared. There are questions now about titles and insurance rates. We need options, not platitudes."
    "You feel the old civic weight settle into your bones: the duty to offer choices that don't just comfort, but defend. Your mind races through legal, ecological, social levers—through the leak that might be weaponized, through the flood that can't be calmed by argument alone."
    # [Scene: Beacon Plaza | Simultaneous]
    hide asha_moreno
    hide noah_reyes
    hide mayor_rosa_alvarez

    scene bg ch11_e67f19_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Loudspeaker feedback; distant clatter as sandbags are moved]
    # play music "music_placeholder"  # [Music: Intensifying percussion; quick violins]
    "Outside, the town is a choreography of urgency. Volunteers haul sand behind creaking barricades; Marta organizes garden platforms as provisional shelter, calling names, layering tarps. Eli ferries elders across a wash of churning water, his boat a small, stubborn island of hands and rope."
    "You find yourself directing the marsh reinforcement, sleeves rolled, fingers sticky with wet coir. Each knot you tie feels like a promise that may fray. The sea is loud now, a presence that doesn't negotiate."
    "Noah Reyes returns from a brief press update, voice hoarse from telling people what to do. He catches your eye; you can see the strain stitched under his skin, the old fear past the planner's calm."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "People need to feel we see them. Lila's crews could give us materials and heavy lifts—if we accept them, the Beacon's footprint grows. If we refuse, we might be courting catastrophe for principles."
    "You breathe out, lungs tight. The leak has turned the private clause into a public threat and the failing wall into immediate harm. Each option is a crucible: safety with strings, legal exposure with uncertain payoff, or a community gamble with real risk to houses and memories."
    "Lila Park appears on a live feed projected onto a portable screen—her face framed by rain, professional, a hand steadying a tablet."
    show lila_park at right:
        zoom 0.7

    lila_park "We are deploy—' (The feed flashes with a static cut.) '—ing full support. We regret the leak. We're coordinating with your mayor. Please let us help."
    "You study her expression at the edges; there is apology in the wording, but the face on the screen is trained to speak for systems. You can imagine the hours and teams behind her; you cannot see the clauses her lawyers have written into the margins."

    menu:
        "Post Lila's apology to the town feed to calm panic":
            "You press 'share.' The message settles into feeds and buys voices a little time, but murmurs about the clause keep spreading. Some volunteers look at you with hopeful, wary eyes."
        "Hold back and verify Lila's teams before sharing her message":
            "You ask for immediate proof of credentials and manifests. It slows the calming but prevents a false sense of security—people bristle at the delay."

    # --- merge ---
    "The town's response shifts depending on trust and timing, altering immediate morale and operational tempo."
    # [/INTERACTION]
    # [Scene: Promenade Edge | Climax]
    hide noah_reyes
    hide lila_park

    scene bg ch11_e67f19_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A collective shout; the metallic groan of a failing structure]
    # play music "music_placeholder"  # [Music: Crescendo—drums pounding, violins shrieking then cutting to a single low note]
    "The wall fails in excruciating real time. The Beacon's sensors map the breach: pressure differentials spike, water velocities surge. In the lab the data looks like a wound; on the promenade it looks like a line of force that wants to claim everything in its path."
    "A child cries; an elder grips a rail until knuckles blanch. Volunteers double down, shovels arc, sandbags pile like small fortresses. Eli shouts over the water, voice gone raw, while Marta ties a tarp into a"
    "sling for someone who cannot climb stairs. You are everywhere and nowhere—your hands are in the coir, your ears on the radio, your mind running legal phrases and tide lines together until they burn."
    "Noah Reyes finds you between the berm and the lab, rain in your hair, compass cold and slick under your palm. He takes your face in both hands for a second—short, fierce—their warmth a surprising cut through the storm."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "Asha. Look at me. We have three real choices in front of us. We pick based on what we can live with."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "(Your voice is a raw edge.) We can lean on Lila—accept their crews and materials now to hold the line. We can go public with the leaked clauses and try to legally pull them back—might lose funding and face litigation. Or we can throw everything into a fast, risky natural restoration—replant marshes, reroute flows, bet on biology to bind what engineering couldn't."
    "Noah Reyes's thumb traces the salt at the corner of your eye, steadying you."

    noah_reyes "Each one costs something. Each one protects something else. I don't know which one keeps us whole. But I know you—we both know what matters to you and to this town."
    "You stand in the rain and taste the choices: urgency pulling to the pragmatic fix, anger pushing toward public accountability, stubbornness bleeding into a gamble on living systems. Panic whips around you; the arousal of the night reaches a fever pitch. Your chest is tight enough to bruise."
    "Mayor Rosa approaches, wet but composed, eyes like a ledger that has always balanced competing debts."
    show mayor_rosa_alvarez at center:
        zoom 0.7

    mayor_rosa_alvarez "Asha, Noah—we need a clear call. The town needs direction, and they need it now."
    "The decision sits between you like a lighthouse beam—cold, bright, impossible to step into without consequence."
    # play music "music_placeholder"  # [Music: Climactic pause, a held low note]
    hide noah_reyes
    hide asha_moreno
    hide mayor_rosa_alvarez

    scene bg ch11_e67f19_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant thunder; the town's murmur lowers to a single, expectant hum]
    "You look down at the compass, then up at the faces around you: Eli, salt-streaked and furious; Marta, trembling but unbowed; Mayor Rosa, steady and pressed; Noah, offering his steadiness like a raft. The leak has"
    "become a weapon; the wall's failure is immediate harm. Your heart is heavy. The choices you make now will shape not just infrastructure but trust, property, and the weave of daily life."

    menu:
        "Work with Lila to mobilize corporate resources to shore the town immediately.":
            jump chapter21
        "Expose the leaked clauses and pursue legal action with Mayor Rosa to renegotiate terms publicly.":
            jump chapter30
        "Mobilize the community for an accelerated natural restoration—risky, resource-heavy, but autonomous.":
            jump chapter21
    return
