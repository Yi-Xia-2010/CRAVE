label chapter8:

    # [Scene: Municipal Hall | Late Afternoon]

    scene bg ch8_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmur of conversation, a kettle tapping in the back, rain pattering against tall windows]
    # play music "music_placeholder"  # [Music: Tense piano with a quickening string undercurrent]
    "You stand just behind the dais, the signed memorandum folded in your hands like something both heavy and featherlight. The hall smells of coffee, wet wool, and the faint ozone of a day that could go"
    "either way. Your compass pendant presses warm against your sternum; you feel Elias's presence as much as you see him—his shoulder close to yours, his hand brushing the small of your back when he steadies the"
    "stack of papers."
    "Tamsin Hale sits at the table with a posture that could have been carved from stone. Mira Chen's smile is a thin strip of chrome; the tablet on her lap blinks with the grant confirmation. In"
    "the audience, faces blur into a tide of hope and fatigue—fishermen with callused fingers, retirees who remember when the boardwalk was whole, young parents holding damp coats around their children."
    "You breathe, letting the small, controlled things hold you: the crease of the paper, Elias's steady rhythm beside you, the click of the microphones waking."
    show councilwoman_tamsin_hale at left:
        zoom 0.7

    councilwoman_tamsin_hale "This memorandum marks a change in how we protect and steward this town. It pairs scaled funding with on-the-ground stewardship. It is—' (she taps the paper with a gloved fingertip) '—practical."
    show mira_chen at right:
        zoom 0.7

    mira_chen "Fast-tracked, yes, but designed to respect local knowledge. The fund is ready to disburse on signature."
    show elias_voss at center:
        zoom 0.7

    elias_voss "We do this together. We show them we can—' (he lets the sentence hang) '—that we will."
    hide councilwoman_tamsin_hale
    show maya_ortega at left:
        zoom 0.7

    maya_ortega "We will. We'll make proof that dignity and jobs can coexist with ecological care."
    "A ripple of applause. Somewhere in the back someone whooped. It hits you like a small, warm wave—relief so sharp it scrapes."

    menu:
        "Offer a small, grateful smile to the crowd":
            "You turn your face toward the room and return a smile. A woman in the second row wipes her eyes; a child waves a soggy paper flag. The warmth settles in your chest for a breath."
        "Keep your gaze fixed on the signed memorandum":
            "You keep your eyes on the paper, reading the signatures like braille. The ink is real; the ink is binding. The warmth is delayed, replaced by a new weight."

    # --- merge ---
    "Tamsin signs with a clean, efficient stroke. Mira follows—her stylus hisses on glass before she lifts her head and forces that corporate smile into place. Elias slides the folder into your hands and, for a heartbeat,"
    "your fingers touch. The contact is nothing and everything: a promise, a tether, a private oath."

    "Council Chair (quietly)" "We should publicize this. The town needs to feel the momentum."
    "You look up to the rows of cameras, the community volunteers clustered in the back, Luca's familiar jacket by the doorway—so many small human things you are determined to protect. The projection behind you flashes plans"
    "of living seawalls, tidal gardens, and a phased timetable meant to pace hope into reality."
    hide mira_chen
    show councilwoman_tamsin_hale at right:
        zoom 0.7

    councilwoman_tamsin_hale "Speed makes the difference this winter. We'll need an accelerated build schedule to get the most vulnerable zones secured ahead of the predicted high tides."
    hide elias_voss
    show mira_chen at center:
        zoom 0.7

    mira_chen "We can shift contractors onto an accelerated timeline. The fund allows it."
    hide maya_ortega
    show elias_voss at left:
        zoom 0.7

    elias_voss "Acceleration is one thing. Cutting corners another. We have to keep oversight on-site—community liaisons, third-party checks."

    councilwoman_tamsin_hale "Oversight is part of the plan. We don't have time for endless pilots."
    "Conversation tightens—subtext like tightened straps. You can feel the room's temperature rise as urgency and relief commingle."

    "Maya Ortega (quietly to Elias)" "If we rush, will the marshes hold?"

    "Elias Voss (his jaw sets)" "They should. If the planting protocols are followed and the substrate is right—if the contractor doesn't cheap out."
    "Mira's smile thins at the name. Tamsin’s eyes flick to the entrance where the city's rapid-build contractors stand in dark jackets, tablets blinking."

    mira_chen "We have contractors with experience in emergent builds. We've priced the timeline for efficiency. This is what gets roofs over heads and payroll moving."

    "Rosa Delgado (from audience)" "Don't let 'efficiency' mean 'we take the easy cut and leave the rest to rot.' The town's work can't be a PR job."

    "Councilwoman Tamsin Hale (the practiced politician meets the community organizer)" "Agreed. The memorandum includes community oversight."
    "The applause that follows is uneven—some hands clap hard, some not at all. The hybrid memorandum is signed; papers are stacked and photographed; flashbulbs bloom like white flowers."
    hide councilwoman_tamsin_hale
    hide mira_chen
    hide elias_voss

    scene bg ch8_6b08b4_2 at full_bg
    # play music "music_placeholder"  # [Music: Strings rise rapidly, a heartbeat pattern beginning to push forward]
    # [Scene: Municipal Hall | Evening — News Montage]

    scene bg ch8_6b08b4_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: TV chatter, urgent tone; distant thunder rolling]
    "That night, headlines puncture the fragile calm. The stormfront arrives a day earlier than the model predicted. A cold green light bleeds over the horizon. High tides climb in thin sheets, and the newly signed zones—where your team planted marshbeds that afternoon—feel the first real test."
    # play music "music_placeholder"  # [Music: Percussive, urgent—drums and high strings in a droning pulse]
    # play sound "sfx_placeholder"  # [Sound: Wind howling; waves slapping; the creak of newly fastened scaffolding]
    "You and Elias are at the harbor by dusk; the living seawall glows under portable work lights as crews hustle. Rapid-build teams churn in, engines snatching at wind. The grant's accelerated schedule has a teeth-gnashing pace; there is energy and a smell of gasoline mixed with sea salt."
    show elias_voss at left:
        zoom 0.7

    elias_voss "We need the substrate bags here now! Move the volunteers off the low stretch—now!"
    "A contractor in a reflective vest answers with clipped efficiency, then a younger foreman runs a hand through his hair."

    "Contractor Foreman" "If we move concrete anchors—"
    show maya_ortega at right:
        zoom 0.7

    maya_ortega "No concrete anchors across the marshbeds. Planting beds need saline-tolerant substrate; anchors can break rootlines."

    "Foreman" "We don't have time to import the engineered substrate at volume. This is what the schedule allows."
    "Tension frays into argument. A government inspector's handheld device bleeps: a series of compliance checkboxes being forced through at the edge of the site."

    menu:
        "Push the foreman to stop work and wait for proper substrate":
            "You step between the foreman and the crew, voice steady and loud enough for the radios to pick up. Some hands freeze—some volunteers look relieved. The foreman scowls but hesitates; the timeline hiccups."
        "Order volunteers to shore-up the temporary berm while the foreman continues":
            "You split your energy—send volunteers to shore up the berm. It buys time, but you're worried the berm will fail if the marshbeds are improperly set. Sweat trickles down your neck as the pumps whine."

    # --- merge ---
    "Machines shove sand; men and women with shovels race to hand. In the dark, under emergency floodlights, a miscommunication becomes a disaster. A truck dumps substrate too forcefully into a planted plot; rootlines are smashed and"
    "compacted. The planted marshbed slumps as sea water finds the path of least resistance. The tide takes the loosened plants and pulls them into a muddy swirl."
    "You run—boots slapping the dock, heart hammered in your throat. You grab at a spool of rope as it snaps. The sound is clean and terrible, like wood breaking."

    "Maya Ortega (to a volunteer whose hands are slick with mud)" "Get the tarp! Stop water from scouring the bed!"

    "Volunteer" "They're using the wrong mesh—it's tearing!"
    "A generator hiccups and dies. The community-run workshop upriver—the one storing seedlings and salt-tolerant plugs—loses power in the surge. Inside, racks of fragile started seedlings topple; trays of laminated guides and volunteer-made tool kits are soaked. A volunteer curses; another wails."
    "Elias Voss grips your arm, knuckles white."

    elias_voss "We need to call the coordinator—get a reclamation crew on those plots. And the workshop—get people to salvage what they can."

    maya_ortega "Who do I call? The grant team? The inspector? Tamsin?"

    elias_voss "Call anyone. Call everyone."
    "You fumble for your satellite phone; the line is choked with a thousand other urgent signals. Radios overlap each other in a painful chorus. Reporters are already craning necks to film the first signs of failure; the footage will be on screens and feeds by morning."
    hide elias_voss
    hide maya_ortega

    scene bg ch8_6b08b4_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A collective intake of breath from the crews; a child's sob somewhere beyond the lights]
    # play music "music_placeholder"  # [Music: Strings shred into high, staccato notes; percussion crashes—chaos is musical now]
    "Mira appears, face paler than her smile earlier, an umbrella useless in the gale. She touches your sleeve—an accidental human gesture in the storm."
    show mira_chen at left:
        zoom 0.7

    mira_chen "We will document the failures and cover remediation costs. This is what funding is for."
    "Councilwoman Tamsin Hale strides across wet planks with policy certainty in her step, but the policy is suddenly messy with mud."
    "Councilwoman Tamsin Hale: (to you, voice tight) 'We included emergency allocations for contingencies. We planned for this—'"
    show maya_ortega at right:
        zoom 0.7

    maya_ortega "We planned for models. Models aren't people with soaked hands and seedlings drowning."

    "Councilwoman Tamsin Hale (a blink of something like shame)" "You're right. We have to be better. We'll reassign crews. Twice the oversight. I'll—"
    "Before she can finish, a loud crack—engineers' scaffolding gives under water-saturated soil. A temporary bridge slumps; a contractor curses. The camera lights flash in and out with power surges. Someone records a volunteer sprinting up the boardwalk with a sodden tarp; their breath fogs in the cold air."
    hide mira_chen
    hide maya_ortega

    scene bg ch8_6b08b4_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant sirens; the wind eating words]
    "You and Elias work through the night. Hands blister from quick knotting and frantic labor; salt and blood make a single metallic tang on your lips. You are exhausted in a way that goes past fatigue: the sort of bone-deep wear that tastes like betrayal."
    "A contractor error has undermined a newly planted marshbed; a week of careful community labor is overturned in hours. A small workshop that was a hub for volunteers—the place where you had planned to teach nursery"
    "techniques and tidal gardening—has lost stock and power. The images will be tweeted, streamed, looped."
    "At dawn the media has a new headline: HYBRID PLAN TESTED: EARLY FAILURES RAISE QUESTIONS. Voices you had hoped would be allies now cut through airwaves—some sympathetic, some merciless. Tamsin's initial statement is quoted and re-quoted;"
    "Mira's 'we will cover remediation costs' is listed, then dissected. On the docks, a man you know from your childhood checks his boat and swears softly, not at the sea but at the larger machinery of"
    "promises."
    "Elias Voss stands close beside you as the tide pulls at what is left. You feel the residual heat of your hand on his; the bandage of a volunteer's finger peels blood into the mud."
    show elias_voss at left:
        zoom 0.7

    elias_voss "We thought the compromise would buy time. It bought exposure."
    show maya_ortega at right:
        zoom 0.7

    maya_ortega "Exposure and responsibility. We invited faster money into fragile work. I thought we could steer it."

    "Elias Voss (his voice cracks)" "You did steer it. You still are steering."

    "Maya Ortega (the admission is a small, ragged thing)" "But steering isn't the same as controlling the sea."
    # play music "music_placeholder"  # [Music: A low, grieving cello; a single high violin line that refuses to resolve]
    hide elias_voss
    hide maya_ortega

    scene bg ch8_6b08b4_6 at full_bg
    "You both stand there, hands blistered, as the sea takes a little more than you expected. The shoreline is changed—small, meaningful losses: a bench pulled under, a set of nursery crates torn apart, a newly planted"
    "stretch washed into clumps. The signage of the hybrid plan flaps in the wind, its edges frayed; one corner holds the smear of wet ink where a signature blurred."
    "Across the harbor, Tamsin organizes a reassignment of crews with crisp commands. Mira is on the phone—fast words, corporate triage. The rapid-build teams continue to move with effective brutality: efficient, decisive, sometimes careless."
    "You look at Elias. He looks at you. The promise between you feels both solid and serrated."
    show elias_voss at left:
        zoom 0.7

    elias_voss "We opened a door."
    show maya_ortega at right:
        zoom 0.7

    maya_ortega "And the jamb's already splintering."
    "Silence falls—not the calm of peace but the heavy pause after a bell toll. The town did, for a while, buy itself time and dignity on paper. The paper is now wet, edges curling. The dignity stands, but its scaffolding is compromised."
    "You can name anger and grief and a dozen other aching things. You can feel the truth: that compromise has a cost and that a victory on paper can become a vulnerability in practice. You can also feel, under the cold and salt, a stubborn ember—work unended."
    hide elias_voss
    hide maya_ortega

    scene bg ch8_6b08b4_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The persistent, distant sound of waves; the low hum of generators; a volunteer sobbing once, swallowed by wind]
    # play music "music_placeholder"  # [Music: A slow, minor chord progression—resignation braided with resolve]
    "You lift your face to the wind and let the brine wash your cheeks. Elias takes your hand—no flourish, only the press of skin. It is not a solution. It is not an answer. It is a shared wound and a shared pledge."
    show maya_ortega at left:
        zoom 0.7

    maya_ortega "We clean up. We document. We learn. We ask for true oversight. We keep showing up."
    show elias_voss at right:
        zoom 0.7

    elias_voss "And we'll tell the town what happened, honestly."
    "You look toward the Municipal Hall where the signatures now hang in photographs. The hybrid plan lives both there and here in the mud, in the broken marshbed and in the soaked seedlings."
    "For tonight, there is loss. There is the knowledge that time bought on signatures can be brittle when applied in haste; that intention and funding do not always equal durability. And yet, as you take inventory"
    "of the damage and list the repairs that must be made, there is a stubborn, small human resolution that refuses to be erased."
    "You close your hand on the compass pendant out of habit and steadiness. The wound in your chest eases into a hollow that is still useful: it stores the memory of what failed and the names of who must be called at dawn."
    hide maya_ortega
    hide elias_voss

    scene bg ch8_6b08b4_8 at full_bg
    # play music "music_placeholder"  # [Music: A single, sustained cello note that thins and fades, leaving an empty resonance]
    "You stand with Elias in the aftermath, hands blistered, watching as the sea takes a little more than you expected. The public signing sits between two truths now: a procedural victory on paper, and a vulnerability"
    "in substance. The town has bought time—and the cost of that time is visible in the splintered jambs and in every soaked tray."
    "You feel the fatigue settle like silt. You feel devastated. You feel strangely clear. The work will go on; it has to. The romance between you and Elias is not a refuge from the responsibility; it"
    "is another stake in what must be rebuilt or mourned. You will argue with Tamsin again; you will call Mira; you will stand at more harbors. But for this night, the compromise you helped forge is"
    "both shelter and wound."

    scene bg ch8_6b08b4_9 at full_bg
    # play music "music_placeholder"  # [Music: A soft, unresolved chord—weighty but not entirely without light]

    scene bg ch8_6b08b4_10 at full_bg
    "THE END"
    # [GAME END]
    return
