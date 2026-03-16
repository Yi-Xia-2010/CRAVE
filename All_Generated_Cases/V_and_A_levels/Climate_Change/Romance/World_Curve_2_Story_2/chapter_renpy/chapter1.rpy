label chapter1:

    # [Scene: New Aster Harbor | Dawn]

    scene bg ch1_Start_1 at full_bg
    # play music "music_placeholder"  # [Music: Soft, briny piano; slow tempo]
    # play sound "sfx_placeholder"  # [Sound: Gulls calling, distant thud of a capstan, the steady hiss of surf]
    "You step down off the bus with your field notebook tucked under one arm and the sea-glass pendant warm against your throat. Salt tangs the air—bright and a little sharp—and the harbor smells of diesel and"
    "wet kelp, a familiar perfume that steadies you more than it should. The pier planks creak underfoot, patched and oiled in places, raw in others; the town's handiwork stitched into the bones of the place."
    "A paint-splattered skiff rocks against a repaired piling. Gulls wheel in lazy circles above it, and the surf's hiss seems to keep time with your breathing. Somewhere across the water, a metal panel clanks—a neighbor tightening something that will not be made by architects but by hands that remember."

    scene bg ch1_Start_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low chuckle from Rafi; soft metallic click from Elias 'Eli' Rowan’s toolkit]
    show rafi_gmez at left:
        zoom 0.7

    rafi_gmez "Look at you, you packed half the estuary in that notebook, huh?"
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "Only the useful half."
    "Your fingers tighten on the leather cover."

    mara_kestrel "And the other half is probably tide-rusted."

    rafi_gmez "Good. We need somebody to tell us what rust will do next.' (He looks at the harbor) 'How was the lab up there? Still full of Dr. Park’s Post-its?"
    "You let a laugh out—soft, relieved. There's warmth in being noticed for your particular kind of compulsive cataloguing."

    menu:
        "Step forward and hug Rafi":
            "You fold into him; the oilskin is rough but steady. He pats your back like he's checking that you're the same person who left and came back."
        "Keep a respectful distance and clap his shoulder":
            "You clap his shoulder instead, the contact brisk. He snorts as if you were being ceremonial—then nods, satisfied either way."

    # --- merge ---
    "..."

    rafi_gmez "Good to have you back. Elias 'Eli' Rowan's been fiddling with a salvaged inverter since last week—says it'll keep the seedlings warm when the cloud cover goes long."
    "Elias 'Eli' Rowan looks up at the name, goggles pushed onto his head, hair thrown into wind-stiffed spikes. His grin is a bright, easy thing—an architecture of optimism."

    "Elias 'Eli' Rowan" "And, well, you can tell me if my scavenged inverter is heresy.' (He waves the braided cord of his remote as if it were a flag.) 'Or if it's a miracle."

    mara_kestrel "I'll tell you the truth."
    "You: (fingers tightening on the leather cover) 'If it's a miracle, we'll measure it. If it's heresy, we'll fix it together.'"

    "Elias 'Eli' Rowan (mock solemn)" "Unicorns and manuals. Sounds like a plan."
    "He leans forward, eyes searching yours for a fraction longer than necessary. There's an undercurrent of something unspoken—past projects, past mistakes—but in his expression it's buffered by the present: someone who wants to get it right this time, with other people, here."
    # [Scene: Boardwalk | Morning]
    hide rafi_gmez
    hide mara_kestrel

    scene bg ch1_Start_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft footfalls on wood, a distant hammer]
    "You walk with them along the boardwalk; the town's patchwork becomes a conversation. New concrete plates sit next to splintered boards, and the air holds that wet wood smell, mossy and honest."
    show rafi_gmez at left:
        zoom 0.7

    rafi_gmez "You remember the old arcade? Used to be right there.' (He points at a waterline stain) 'We used to eat dulse chips in summer."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "I do.' Your voice is small against the sound of the sea. 'You could still find a place to hang a hammock between two memories."

    "Elias 'Eli' Rowan" "And maybe put a rain-catcher on the roof of the arcade,' he says. 'Not to replace anything, just—support it."
    "You stop at a planter where seedlings reach in bright, stubborn green. Recycled solar panels catch what light there is and throw it down in thin rectangles on the boards. The Arbor breathes—wood, glass, and the faint mineral scent of fertilizer."
    # [Scene: The Arbor | Mid-Morning]
    hide rafi_gmez
    hide mara_kestrel

    scene bg ch1_Start_4 at full_bg
    # play music "music_placeholder"  # [Music: Low, hopeful synth pad]
    # play sound "sfx_placeholder"  # [Sound: Drip of irrigation; the faint whir of a modest fan]
    "The Arbor is hands-on optimism: solar tubing, braided gutters, and seed trays in various states of hope. You set the notebook down on a workbench crowded with spanners and seed trays, the leather making a soft sound against rough wood."
    show rafi_gmez at left:
        zoom 0.7

    rafi_gmez "We saved space for you.' (He reaches over and nudges a tray at the edge.) 'Figured you'd like to count leaves for breakfast."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "Like clockwork.' Your fingers trace the spine of the notebook. The ritual calms you—calibration as a prayer. 'How did the winter hold up?"

    "Elias 'Eli' Rowan" "Less dramatic than last year.' He shrugs, but there's an edge in it. 'Still, tides were...funny. Missed the usual rhythm in January. A few houses had more puddles than their basements deserve."

    mara_kestrel "That's not nothing."

    "Elias 'Eli' Rowan" "No.' He watches you study a tray of seedlings. 'You look...settled, Mara. How long's this 'back to stay' thing going to last?"

    mara_kestrel "As long as I'm useful."

    "Elias 'Eli' Rowan" "That's a selfish answer.' He grins. 'Good selfish."
    "You give a little laugh. It warms you, small and necessary."

    menu:
        "Offer Elias 'Eli' Rowan a hot thermos from your pack":
            "You pull the thermos out—tea still steaming. He takes it with both hands, grateful, and the warmth moves through him in soft, visible relief."
        "Keep the thermos to yourself and focus on the seedlings":
            "You tuck the thermos away. Elias 'Eli' Rowan watches you for a beat, then nudges a packet of seed tape across the bench like a truce. 'For later,' he says."

    # --- merge ---
    "..."

    rafi_gmez "Enough romance,' he teases. 'Get the wristband calibrated; Dr. Park'll want the first tide-run before noon."

    mara_kestrel "On it."
    # [Scene: Estuary Research Lab | Late Morning]
    hide rafi_gmez
    hide mara_kestrel

    scene bg ch1_Start_5 at full_bg
    # play music "music_placeholder"  # [Music: Quiet, steady arpeggio]
    # play sound "sfx_placeholder"  # [Sound: Soft hum of the solar array; the high-frequency buzz of the wristband calibrating]
    "The lab smells like antiseptic cleaner turned a little briny at the edges. Your fingers—callused from fieldwork, ink-streaked—unfurl the wristband and click it against your wrist. It hums, small and obedient, solar cells blinking like patient"
    "eyes. The display warms into life; numbers and graphs settle into their grids, familiar as tide marks."
    "You set sensors along the window sill—temperature probes, salinity testers, a strand of reed tied to a marker to watch the micro-fluctuations. The laptop fan breathes; you open the tidal model you've adapted for this estuary and feed it the seasonal parameters. Your breath finds the rhythm of the computation."
    "Your mind does two things at once. The scientist in you catalogs variables—return periods, storm surge anomalies, the slow creep of mean sea level. The child who remembers the old boardwalk counts images: a splintered bench,"
    "the arcade's neon bent under salt, Grandma Hira's shawl drying after a high tide that stole her stoop. Both perspectives weigh in; both give you tools. One is exacting. The other is an ache you can't"
    "quantify."
    "You toggle a control and run the model."
    # [Direction Cue: Tight on screen as graphs bloom—gentle curves, then slight inflections]
    # play sound "sfx_placeholder"  # [Sound: Soft digital blip as the simulation completes]
    "The results appear, neat and clinical. They are worrying in small increments—return periods for what used to be fifty-year floods shortening, flood lines inching closer to familiar streets. Not catastrophic. Not yet. But the change that"
    "used to be a rumor carved into local memory is now numbers, and numbers make new arrangements inevitable."
    "You feel your chest tighten—an old, familiar pressure—then relax into it. It's not panic. It's the sober thrill of an engineer seeing a problem clearly enough to begin fixing it."
    "You breathe out. 'Small shifts,' you murmur. 'Manageable.'"
    "Elias 'Eli' Rowan looks over your shoulder, brows knitting at the projection. 'Manageable?' His voice hunts for certainty. 'Manageable how?'"
    "Mara Kestrel: (you turn the screen toward him) 'We can design buffers—green berms, distributed rain capture, modular breakwater tests. Nothing glamorous, but maintainable by people here. We start small, prove it works.'"

    "Elias 'Eli' Rowan" "Proof is what I like to build. We can make a prototype—here, by the Arbor, using the old dock timbers and that salvaged mesh."
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "Exactly. Keep people in place, keep livelihoods intact. We keep the town's bones."
    show rafi_gmez at right:
        zoom 0.7

    rafi_gmez "And recipes for fixing them. You can't have a miracle that nobody knows how to cook."
    "The three of you stand, shoulder-to-shoulder, the screen reflecting in all your eyes. Hope is threaded through the worry—steady and practical. The arousal of the morning has been low, but it has been building: from the"
    "hush of arrival, through the quiet exchanges, to the soft click of the model giving you a map."
    "You reach into your pocket and touch the sea-glass pendant at your throat. It is cool, worn to a pale edge by years of being held. It anchors you in a way no dataset could; it"
    "remembers the child who played on ruined planks and the adult who will now fight for them."

    "Elias 'Eli' Rowan" "So…you're really back, huh? For good?"
    "You pause. It is a question shaped like an invitation and a promise both. Saying yes feels like deciding a tide-line—not an arrogant claim that you'll control everything, but an agreement to stay with what your home needs."

    mara_kestrel "I'm home to help."

    "Elias 'Eli' Rowan" "Good. We'll make something that works. Together."
    "Rafi whistles softly—a sound like approval—and returns to his coffee, eyes twinkling."
    "Inside you, the scientist catalogues next steps; the community-minded person composes a plan; the private memory files away small comforts for storms to come."
    "There is urgency here, but it is a steady urgency—clear-eyed and collaborative rather than frantic. Dawn has given way to a pale morning, and with it a fragile promise: something to build, someone to build with."
    "You pull up the model one more time to run a sensitivity analysis—tweaking parameters, imagining small interventions. Each iteration shifts the flood line in inches and feet, sometimes better, sometimes worse. You note them down, your handwriting neat despite the quickening pulse in your fingertips."
    "The highest point of tension for the morning, the quiet peak the day has been edging toward, lands not as a shout but as a soft, insistent challenge: the numbers demand action, and the people beside you are already reaching for the tools."
    "You close the laptop and inhale the greenhouse air—wet, green, alive."
    "There is work to do."
    # [Scene Transition: Sunlight pools through glass as the trio gathers tools. The town hums a low, steady life beyond the panes.]
    # play music "music_placeholder"  # [Music: A single hopeful piano chord lingers]
    "You feel the page of the morning turn beneath your thumb."
    hide mara_kestrel
    hide rafi_gmez

    scene bg ch1_Start_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter2
    return
