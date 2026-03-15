label chapter11:

    # [Scene: Test Platform on the Promenade | Late Afternoon — After Storm]

    scene bg ch11_fa9d90_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, trembling strings; a single downbeat of timpani underlines the crowd murmur]
    # play sound "sfx_placeholder"  # [Sound: Water slapping concrete, distant gull cries, the creak of wet rope; someone counts down softly into a handheld microphone]
    "You stand in your trench coat at the edge of the platform, breath fogging in the humid air. The smell of sea—brine, diesel from a distant workboat, wet fabric—wraps itself around your lungs. Your notebook is"
    "zipped inside your sling; your fingers find the pendant at your throat the way old habits find shorelines. Around you, the crowd presses—shop owners with tape on their palms, reporters with water-speckled notebooks, aldermen in damp"
    "suits behaving as if fabric could still keep politics dry."
    "Noah Ríos's voice is near you, an organized calm that steadies your pulse by simple measure. He is crouched at the diagnostics board, thumbs brushing a tablet. His sensors spit a steady stream of numbers into"
    "a public feed: amplitudes, phase shifts, attenuation indices. A projector throws an overlay on the screen—a clean curve that will either hold like a rope or shred like kelp against a storm."
    "Your chest tightens in that familiar way: urgency braided with fatigue. This is not only a test of technology. It is a demonstration of trust—trust in the community that will be asked to live with whatever"
    "the city signs, trust that data will be listened to, trust that promises made in the glare of cameras will matter once the gavel is silent."

    scene bg ch11_fa9d90_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A soft, electronic ping; someone in the crowd whispers, "Is it working?"]

    menu:
        "Press your hand into the pendant":
            "You let your palm press the cold metal of the pendant; it steadies you. Noah glances over and smiles once, private and small."
        "Fold your arms and watch the screens":
            "You cross your arms, the fabric of your coat creaking. Your face sets into the measured calm you've practiced with Priya; Noah catches your eye with a question that says, 'Did we do enough?'."

    # --- merge ---
    "Continue main narrative"
    show noah_ros at left:
        zoom 0.7

    noah_ros "Baseline is steady. Wave input at 0.8 meters—attenuation nodes coming live."
    show mara_evans at right:
        zoom 0.7

    mara_evans "Keep me up. If the first array holds, we push the feed. Be ready for noise."
    "Noah Ríos's hand is an accidental presence across equipment and then, at the moment the first joined feed flickers alive, his fingers brush yours on the rail. The touch is brief, a punctuation in damp air,"
    "but the data makes a sound like a held breath released: an uptick on the feed, the attenuation curve dipping in a way that translates into numbers and, more importantly, into places kept dry."
    # play sound "sfx_placeholder"  # [Sound: A collective intake of breath; the projector hums as the curve smooths]
    hide noah_ros
    hide mara_evans

    scene bg ch11_fa9d90_3 at full_bg
    "A woman in the front row—Elena—laughs with a sound that is half sob. Behind her, Tomas grips a wooden pole, knuckles white as driftwood. Cameras pivot toward the screen like hawks toward fish. For a moment the Promenade is a held note: anticipation, the kind that is sticky with salt."

    "Reporter" "Can you translate that for us—what does 22 Percentage mean for a bakery on the Strand? For a child's school?"
    show priya_anand at left:
        zoom 0.7

    priya_anand "It means energy from waves is being dissipated earlier. Over a storm surge of this scale, it could be the difference between ankle-deep and knee-deep. Models still need scaling but—"

    menu:
        "Step forward and speak plainly to the crowd":
            "You step up to the mic and speak without the softly honed policy language—stories about Tomas's dock, Elena's paint shop—your voice cracks, and the crowd leans in. People nod. Numbers become windows into daily life."
        "Let the data speak; hand the mic to Priya":
            "You step back and let Priya explain the models. Her graphs are precise and the aldermen scribble. Your name is not on every headline this afternoon; the argument grows technical and harder to dismiss."

    # --- merge ---
    "Continue main narrative"

    priya_anand "(measured) This prototype doesn't solve systemic exposure. It mitigates wave energy in targeted bands. It buys us time and lowers economic risk in neighborhood zones—when maintained and governed locally."
    "Cass (in a voice amplified by civic authority, stepping forward in a cream suit streaked with salt) clears her throat. The murmuring thins. You recognize the tightness around her mouth—the mayor balancing a dozen fraying ropes at once."
    show cassandra_cass_green at right:
        zoom 0.7

    cassandra_cass_green "What you have shown is promising. The council must act on public safety, economic stability, and equity. We will propose a mediated framework: targeted hard defenses where critical infrastructure and lifelines demand impermeable protection, combined with funded living systems—community-led projects like this one—in residential neighborhoods."
    "Arman Kade watches from the dais, a figure cut in navy and steel, his smile reserved and practiced. When he speaks, his voice is the sort the harbor knows: smooth, with a contractor's certainty."
    show arman_kade at center:
        zoom 0.7

    arman_kade "The city needs decisive, scalable solutions. I will collaborate where necessary, but the timeline matters. Investors need a clear path. We cannot tinker indefinitely while storms learn our terrain."

    cassandra_cass_green "We will allocate funds to both pathways. Contracts will include community stewardship clauses; Arman will lead critical infrastructure zones, and the city will fund community stewards to implement living systems."
    hide priya_anand
    show tomas_belmar at left:
        zoom 0.7

    tomas_belmar "Stewardship clauses? Who holds them? Who sits on the boards? Who keeps these things from becoming another paperwork shelter for profit?"

    cassandra_cass_green "We will form an oversight council. Community representatives will have seats. Contracts will require transparent audit trails."

    arman_kade "Those are perfunctory niceties, Mayor. You know the difference between governance and gridlock. We can build—rapidly—if you let us."
    hide cassandra_cass_green
    show mara_evans at right:
        zoom 0.7

    mara_evans "Rapid deployment that displaces people isn't protection. It's relocation. You can't promise a community a seawall and then sell them a life somewhere else with better zip codes. Where I grew up, a promise meant more than a map. It meant you could still walk to the bakery your mother liked. Who is accountable if maintenance lapses? If funding dries up?"

    arman_kade "Accountability is built into procurement. We deliver. We manage. The city doesn't have the capacity to babysit every kelp bed."
    hide arman_kade
    show noah_ros at center:
        zoom 0.7

    noah_ros "Capacity can be built. It can be taught. We designed sensors to hand data back to communities, not to centralize it."
    hide tomas_belmar
    show arman_kade at left:
        zoom 0.7

    arman_kade "And who pays to build that capacity? Who absorbs the initial risk?"
    hide mara_evans
    show elena_torres at right:
        zoom 0.7

    elena_torres "We already absorb risk when our roofs fly off. We already pay with our lives."
    "There is a brittle, public silence. The projector hums like a distant tide."
    hide noah_ros
    show cassandra_cass_green at center:
        zoom 0.7

    cassandra_cass_green "This will be a hybrid strategy. Arman will be awarded contracts for critical zones—ports, power, transit hubs. Community-led living systems will be funded in neighborhoods, with oversight councils and legal protections written into contracts."
    hide arman_kade
    show mara_evans at left:
        zoom 0.7

    mara_evans "And the legal protections—will they be retroactive if a private contractor's plan forces relocation? Will there be recourse?"

    cassandra_cass_green "The contracts will include anti-displacement clauses. They will require mitigation funds and relocation assistance where unavoidable."
    hide elena_torres
    show tomas_belmar at right:
        zoom 0.7

    tomas_belmar "Words are cheap. We need enforceable timelines, independent audits, and penalties that bite."
    "Cass looks at Tomas, then at you. The light through the clouds is thin, pieces of sun like scissors cutting into the wet world. For the first time today, you see the mayor's face lose the"
    "carefully practiced public gloss and become a map of compromises made and still to be made."

    cassandra_cass_green "I know you. I know what you fought for. This is not everything you wanted. But it's not nothing. It is a structure that, if we remain vigilant—if we build the oversight, if we keep each other honest—we can make it protect lives."
    hide cassandra_cass_green
    show arman_kade at center:
        zoom 0.7

    arman_kade "Then let's sign and move. The window for funding is finite."
    "The crowd breaks into a low, complicated noise: some relieved, some wary, some angry. Cameras pivot. A reporter asks about timelines. Questions slug the air like gulls trying to hold a fish in a wind."
    hide mara_evans
    hide tomas_belmar
    hide arman_kade

    scene bg ch11_fa9d90_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft lapping of water at the platform, like hands tapping a slow rhythm]
    "Noah Ríos steps to your side after the press swirl, fingers finding yours without asking. You let your palm open; on the pier the sun fracturing through clouds paints his cheekbone gold. Relief settles across your"
    "shoulders like damp cloth: the demonstration worked. The city has adopted a mixed strategy—neither clean victory nor total defeat. It is an honest, brittle compromise."
    show noah_ros at left:
        zoom 0.7

    noah_ros "You did it. They saw the curves."
    show mara_evans at right:
        zoom 0.7

    mara_evans "They saw the curves. They still signed for hard walls in key zones. He keeps roles. We get funding, oversight clauses, and a promise."

    noah_ros "Promises, oversight. All the words that mean 'watch them when the money dries'."
    "You both look out where the kelp line tugs against its moorings. In the near distance, cranes silhouette against a pale patch of sky—machines ready to raise concrete where the living shoreline might have been given more room. The air tastes of rain and possibility and the residue of compromise."
    "Tomas shuffles up the pier, cap in hand. His face is older than the map you carry in your head; he has seen many 'solutions' come ashore and leave the people holding the bills."
    show tomas_belmar at center:
        zoom 0.7

    tomas_belmar "You all did good work today. The numbers mattered. But don't let them write us out. Stay on the councils. Watch the contracts. Teach the kids what to tend. The sea is patient but not kind."
    "Elena presses your shoulder—paint-splattered and stubborn—and you return the pressure. It is small solidarity. It anchors something."

    mara_evans "We will push for audits. We will train stewards. We'll keep the community seats. We'll make sure living systems are not a sideshow."
    hide noah_ros
    show cassandra_cass_green at left:
        zoom 0.7

    cassandra_cass_green "I will hold them to it. I can't promise perfection. I can promise attention."
    hide mara_evans
    show arman_kade at right:
        zoom 0.7

    arman_kade "Then we can move forward."
    "There is a quiet between those words where you measure all the things that will have to be done: governance structures to be written before contractors bulldoze a budget line; community training that will take years"
    "and sweat; an oversight council that will need teeth and public records and the willingness to sue when necessary. There are always spaces in compromises where people fall through."
    hide tomas_belmar
    hide cassandra_cass_green
    hide arman_kade

    scene bg ch11_fa9d90_5 at full_bg
    # play music "music_placeholder"  # [Music: A low minor chord with distant woodwind, not resolved]
    "You let the relief sit with you like salt—rough on the tongue. You feel Noah Ríos's hand find yours again, a quiet rhythm of proximity and promise. The data curves are real. The contracts promise protection,"
    "and in places, they will keep roofs whole and businesses open. But you are not naïve: hybrid solutions require governance, oversight, and trust that must be earned and renewed every season."
    show mara_evans at left:
        zoom 0.7

    mara_evans "We won a ring of safety, not the shore."
    show noah_ros at right:
        zoom 0.7

    noah_ros "We'll keep working. We'll watch the audits. We'll teach people to read the feeds."
    "You watch a child fling a pebble into the puddle and betray a laugh that is matched by a neighbor nearby. The scene is ordinary and fragile. You find some strange consolation in the ordinary—it's a stubborn proof of why you fight."
    "In the back of your head, the tightness remains: clauses that read like paper can be breeched by an opportunistic market; oversight can be starved by budget lines; community seats can be filled with friendly faces"
    "who forget whose names are written on the bakery's awning. You think of the family storefront you lost when you were sixteen, the way a promise had sounded then, and how different it felt to hold"
    "a city to account now."
    hide mara_evans
    hide noah_ros

    scene bg ch11_fa9d90_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A gull's long cry, then nothing but the low hum of the bay]
    "You and Noah stand until the light fades into a softer strip across the water. You will go back to drafting oversight language, to hosting community workshops, to fighting in council rooms and in the press."
    "This is not an ending you would have written—too many compromises, too many corners cut—but it is an outcome that protects people and preserves place in ways that would have been lost to unmitigated hard defense."
    "You tuck the pendant under your collar, and let yourself, for a moment, feel the relief that is honest and partial. Then you set your jaw. There are meetings tomorrow, and after that, persistent work: audits"
    "to file, contracts to parse, and a community that will look to you not for perfection, but for relentless, organized care."
    # play music "music_placeholder"  # [Music: Strings diminish into a single sustained, unresolved minor note]

    scene bg ch11_fa9d90_7 at full_bg

    scene bg ch11_fa9d90_8 at full_bg
    "THE END"
    # [GAME END]
    return
