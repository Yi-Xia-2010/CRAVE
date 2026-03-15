label chapter15:

    # [Scene: Docks | Morning]

    scene bg ch13_e67f19_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Cranes groaning; boots slapping on metal; a public-address voice muffled by fog]
    # play music "music_placeholder"  # [Music: Driving percussive strings, tempo quickening]
    "You arrived before the sun had finished drying the fog from the harbor. Where the community had once stacked nets and crates, crates with a different logo roll out now—slick polymer rolls, bundled mats that smell"
    "faintly of preservatives and machine oil. Men and women in neutral uniforms move like a choreography you've seen in training videos: efficient, rehearsed, polite. They knot straps and calibrate sensors with the kind of calm that"
    "makes your stomach twist."
    "Mateo is there—his blazer sleeves rolled up, shoulders tight. He meets your eyes and gives a small, quick nod. It's the nod of someone who knows what a compromise costs, and is still trying to believe in it."
    show mateo_ros at left:
        zoom 0.7

    mateo_ros "They're modular. Quick to lay down after the storm. Jobs yesterday, stabilization this week. Council signed fast—contracts were cleared."
    "You touch the edge of your notebook through your raincoat. The leather is damp. The locket at your throat feels heavier than metal. Your decision hangs in your mouth, sour and real: you chose relief for now."
    "Dr. Selene Park steps down from a raised platform, platinum hair immaculate despite the salt air. Her coat repels spray in perfect beads; every movement is measured to look both competent and benevolent. She looks like a solution made visible."
    show dr_selene_park at right:
        zoom 0.7

    dr_selene_park "Aiko Navarro. Thank you for bringing us in. We'll get the first line in before high tide—mitigate displacement and reopen the market. We can show measurable metrics in days."
    "You want to remember why you said yes. You reach for it like a rope. The reasons spool out in practical phrases inside your head—wages, displaced businesses, a hospital generator that needed fuel, a child's school"
    "that opened again this week. Relief arrived as currency and you exchanged trust for it."

    mateo_ros "They did agree to priority hires for locals, at least on paper."
    show aiko_navarro at center:
        zoom 0.7

    aiko_navarro "Paper doesn't hold a boat in a storm,"
    "you say, sharper than intended."

    dr_selene_park "We built this for extremes. It's repeatable, scalable. With the right maintenance contracts—"
    "Your eyes cut to the teams pulling a large biotech mat across the mud. Sensors hum. A mat unrolls, dark-green and slick, the kind of engineered algae woven into polymer. It settles like a skin over the marsh grass."
    "The sound of the marsh changing—squelch, the whisper of living things being covered—registers at the base of your skull, a small alarm you don't have time to answer."

    menu:
        "Step forward and ask the crew how local hire quotas are enforced":
            "You step onto the loading ramp, heart loud in your ears. The crew chief reads his tablet with professional patience and recites a clause about quotas and subcontractors—words that make your insides hollow because you already know how cursory enforcement can be."
        "Hold back and watch from the shadow of the stacks":
            "You hang back. From here you can see the geometry of the rollout but not the faces who will wear its consequences. It feels cowardly and wise at once. Mateo sees you and his look is two halves—relief and reproach."

    # --- merge ---
    "..."
    # [Scene: Markets | Midday]
    hide mateo_ros
    hide dr_selene_park
    hide aiko_navarro

    scene bg ch13_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Merchant calls, coins clinking, a distant power tool; smell of grilled fish and oil]
    # play music "music_placeholder"  # [Music: A tonic synth undercurrent—hope threaded with an uneasy major chord]
    "Money moves faster than rumor. A clerk you know hands you a small envelope—first week's payroll for hired dockworkers. Ivy's face is alight when she finds you, flour on her cheek, apron stained from bread sold this morning. She hugs you like there's a fire and you are the flame."
    show ivy_navarro at left:
        zoom 0.7

    ivy_navarro "They brought rigs! They hired Marco from the east wharf. They paid him for the week already. Aiko—your plan—"
    show aiko_navarro at right:
        zoom 0.7

    aiko_navarro "This isn't—"
    "You stop. The sentence fragments. Relief tastes mixed: sweet with underlying metal."
    "Tala appears like a flare—purple hair tied back, voice threaded with exasperation. She corners you between a vegetable crate and a corporate canopy, and there is no softness in the way she steps in."
    show tala_kumari at center:
        zoom 0.7

    tala_kumari "You handed them the keys. You didn't negotiate the clauses that stop them from subcontracting the maintenance out of town. The community can't be a checkbox."

    "Aiko Navarro (defensive)" "Tala, we couldn't wait. People needed work. A week without income and we lose more than pride."

    tala_kumari "We lose autonomy. We lose everything that made this place ours. Did you think they'd change because we asked nicely?"
    "Your mouth tastes of old arguments. The market around you hums—people buying fish, children running between legs. You feel split down the middle: the practical part of you that counted jobs in spreadsheets, and the other part that feels the marrow of place being sanded away."
    hide ivy_navarro
    show mateo_ros at left:
        zoom 0.7

    mateo_ros "We pushed for local hiring and oversight language. It could have been worse. But Tala's right—enforcement is the risk."

    aiko_navarro "We got breathing room. We can build from that."
    "Tala Kumari's jaw tightens."

    tala_kumari "Breathing room isn't the same as breathing. When the maintenance goes to outside contractors, any fixes that depend on local knowledge—Rohan's channels, the way the tide hits the eastern promontory—will be ignored."
    "Your hands curl into the fabric of your coat. For a second you taste the salt and fear of becoming someone who solves problems with stamps instead of people."

    menu:
        "Promise Tala you'll push a community oversight committee and mean it":
            "You say it quickly, loudly—too loudly to be a casual remark. Tala studies your face as if turning a stone. She nods, brittle. It's a bandage that will have to hold."
        "Insist the immediate relief proves the decision was right and focus on the markets":
            "You point to the queues, to the money changing hands. It calms some vendors; it angers Tala. Her eyes drill into you with the kind of disappointment that rearranges your ribs."

    # --- merge ---
    "..."
    # [Scene: Tidepark Research Greenhouse | Late Afternoon]
    hide aiko_navarro
    hide tala_kumari
    hide mateo_ros

    scene bg ch13_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Camera shutters; reporters' murmurs; the faint drip of condensation]
    # play music "music_placeholder"  # [Music: A high, thin sustained note—tension like a held breath]
    "Dr. Selene hosts a demonstration under the storm of flashbulbs. The crowd is a cross-section: municipal staff, a smattering of neighbors, and the press whose lenses reduce everything to headline shapes. She speaks with the polish of someone who has never had to choose between rent and science."
    show dr_selene_park at left:
        zoom 0.7

    dr_selene_park "These engineered mats replicate native filtration while attenuating wave energy. In trials, we see a 40-percent reduction in immediate inundation. This is scalable adaptation."
    "Her words are exact, flawless. They land like promises stamped and signed. You can see the models: neat, sanitized cross-sections of marshland becoming infrastructure. Mateo stands near you, jaw clenched, palms pressed flat against a rolled blueprint as if to keep it steady."
    show mateo_ros at right:
        zoom 0.7

    mateo_ros "They phoned in additional funding for the municipal restoration budget. We can expand the hybrid plan if—"
    "Before he finishes, the crowd hushes. Someone's phone is buzzing—more than a buzz, an urgent chorus. Mateo's face drains. He swipes and his tablet fills with a live feed from another coast: a trial site in a climate-neighboring province."
    "On-screen, images jump: mats laid over seagrass, lab technicians pointing, then a slow, suffocating decline. A video from a local fisherman—grainy—shows thick mats smothering eelgrass, fish flitting away from pale beds. Another clip: engineers pulling up patches of dead biota, the water cloudy with sediment."

    mateo_ros "This is from a week after deployment. They found rapid die-off—seagrass beds collapsing, anoxia pockets forming..."
    "A woman in the second row gasps; a reporter starts to whisper into a recorder. Dr. Selene's composed face shifts—the tiniest micro-expression. For a moment she looks like someone who has just seen a number that wasn't supposed to be there."

    dr_selene_park "Preliminary reports indicate localized effects. We will analyze—"
    show old_man_rohan at center:
        zoom 0.7

    old_man_rohan "That grass is where the baby mullet hide, where the scallops set. You can't roll a blanket over what grows there."

    dr_selene_park "Our models account for biomass turnover—"

    old_man_rohan "Your models didn't grow the tide. You didn't teach us how the water remembers the last spring."
    "The greenhouse air is suddenly too thin. Reporters pounce with questions; Dr. Selene parries with data. But the clips loop and loop, a small death played on repeat. Each replay clawed at the crowd's hope."
    "Mateo's hands shake now, a tremor of someone balancing on a toothpick. He looks at you, eyes raw."

    mateo_ros "Aiko—this could mean unanticipated feedback loops. If seagrass dies, we lose carbon sequestration and shoreline stability. The mats could buy time while creating a worse baseline."
    "You feel a current beneath your feet: your earlier choice dragging like a chain. The arousal you've been carrying—quick breaths, ringing in ears—tightens into something louder, angrier. You think of the dockworkers who smiled with their"
    "pay envelopes, of Ivy's flour, of the children playing near the new mats as if they were toys."
    "Tala Kumari's voice cuts through the murmurs, higher now, rawer."
    hide dr_selene_park
    show tala_kumari at left:
        zoom 0.7

    tala_kumari "We knew what their solutions smelled like. We begged for pilots with local protocols. We begged for staged rollouts. We begged—"
    hide mateo_ros
    show dr_selene_park at right:
        zoom 0.7

    dr_selene_park "We acted at council request to meet immediate hazards. We will review these datasets and adapt."
    "A man in a corporate shirt taps the screen to stop a video. The sound dies like an amputated thing. That silence fills the greenhouse until it presses against your ears."
    "Your phone buzzes with messages—someone from a distant lab, a journalist, a name you don't recognize sending a screenshot. The decision you made, the one that unlatched funds and logistics in one efficient motion, now sits bleeding contradictions across screens."
    hide old_man_rohan
    show mateo_ros at center:
        zoom 0.7

    mateo_ros "We can call for an immediate independent assessment. Pause further deployment until we understand—"

    dr_selene_park "A pause would jeopardize the protections being installed across vulnerable stretches. Delay equals exposure."

    mateo_ros "But risk could equal harm too if those mats cause cascading failure."

    dr_selene_park "Every action has trade-offs, Mr. Ríos. We weigh the immediate human cost against modeled outcomes. We chose to move."
    "You feel it then: the room tilting, ethics and spreadsheets colliding. The high arousal that carried you through the council hearing—urgent, pressured—breaks open into a raw, frantic volume. You cannot put the sound of the dying seagrass out of your head. It is the sound of decision turned into consequence."
    "Ivy touches your sleeve, the contact a small anchor."
    hide tala_kumari
    show ivy_navarro at left:
        zoom 0.7

    ivy_navarro "Aiko,"
    "she says, voice thin."

    ivy_navarro "What do we do now?"
    "Your hands fumble for the notebook, pages damp and inked with plans and names. The notes are suddenly small against the scale of the image on the screen. Your chest tightens until you taste iron."
    "You remember the promise you made—to protect people now. That promise is still true. But in the dark seam between now and later, something is already breaking."
    hide dr_selene_park
    hide mateo_ros
    hide ivy_navarro

    scene bg ch13_e67f19_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant surf; a reporter's question rises and folds into a sea of noise]
    # play music "music_placeholder"  # [Music: Crescendo—strings and low brass, urgent and unresolved]
    "You inhale. The decision you made is not a single act but a path that bends and fractures in ways you could not have measured. You feel the weight of faces in the room: Dr. Selene"
    "poised to defend, Mateo reaching to reconcile, Tala burning with accusation, Rohan muttering names of places that no model could hold. The future yawns with both help and harm."
    "Everything seems to happen at once—the market's laugh, the dockworkers' boots, the thin video of dead seagrass—converging into a single hot point."
    "You close the notebook and let the sound of it click shut be an attempt at finality that it cannot be. Your chest is a fist of cold tide."
    "You have done what you thought would save people. The sea is giving you back a question you don't know how to answer."
    "A long pause passes—a tide pulling away before it returns—leaving the greenhouse in a stretch of raw, electric expectation that insists on continuing."

    scene bg ch13_e67f19_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter18
    return
