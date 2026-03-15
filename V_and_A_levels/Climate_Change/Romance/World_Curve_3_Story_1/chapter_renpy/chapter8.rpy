label chapter8:

    # [Scene: Rooftop Greenhouse | Pre-Dawn]

    scene bg ch8_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of the prototype, distant gulls, rain pattering on corrugated plastic]
    # play music "music_placeholder"  # [Music: Pulsing percussive beat—tight, rhythmic]
    "You wake to the aftertaste of rain on the air and the compass warm at your throat. The pendant presses there like a metronome: steady, private. Beyond the glass the city is a silhouette of low"
    "roofs and the dark line of the Flats; the Planning Hall is a pale rectangle on the horizon. The prototype's LEDs throw small, synthetic constellations across packed seed trays."
    "Ibrahim 'Ibe' Rafiq is already crouched over a crate of fasteners, his silhouette precise against the fog. Samira stands a little apart, clipboard clutched, eyes scanning the network of feeds on her tablet. Volunteers shuffle in"
    "layers of thrifted rain gear; chatter is practical and careful, the sort of talk people make when they are doing something that matters."
    "Your hands find the notebook in your jacket the way they always do. You don't open it—there isn't time for maps right now—but the weight of inked lists sits like ballast against your ribs. The greenhouse"
    "smells of wet earth, solder, and the faint copper tang of the prototype's hydraulic oil."

    "Ibrahim 'Ibe' Rafiq" "We run a single module this morning. Slow lift, full monitoring. If it moves like the sims, we get confidence. If it doesn't—' (He swallows.) 'We learn fast."
    show samira_chen at left:
        zoom 0.7

    samira_chen "Council approved this as a limited test. Eloise signed off on oversight. Press is on standby. You're aware of the optics, Mara."
    show mara_lin at right:
        zoom 0.7

    mara_lin "I'm aware."

    menu:
        "Check the hinge tolerances one more time":
            "You kneel beside the module and run your gloved fingers along the hinge, feeling for slack. The fasteners answer with a low, mechanical confidence; the sensor readouts flicker green. You exhale a little less sharply."
        "Go down to brief the volunteers at the quay":
            "You step toward the hatch, voice already finding the cadence of instructions: who holds, who watches lines, where to stand. The volunteers look up and fall into place like practiced birds."

    # --- merge ---
    "You reverse between both impulses—detail and people—long enough to feel the weight of the decision. In the end you split your time: three minutes with the hinge, five with the volunteers, and a single, tight conversation with Ibe about tolerances."

    "Ibrahim 'Ibe' Rafiq" "If the hinge loads unevenly, the whole ['module'] could torque. We can't let a single failure cascade.' (He taps the sensor array.) 'The telemetry's fine, but it's the mechanical joint I don't trust."

    mara_lin "We won't let it cascade.' The words are more prayer than promise. 'Slow lift. Red team on the lines. If anything squeaks past amber, we stop."

    "Ibrahim 'Ibe' Rafiq" "You and your stopwatches."

    samira_chen "I'll log everything. If we get one good lift, the advisory board can use it."
    "You look at the volunteers: faces lined by the weather, by years of living close to the water. Kai is there with a thermos, Rosa's protege hands are raw but steady. The press vans crouch at the edge of the quay like black gulls; photographers climb ladders for better lines."
    hide samira_chen
    hide mara_lin

    scene bg ch8_6b08b4_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Metallic creak of the crane arriving, diesel thrumming]
    # play music "music_placeholder"  # [Music: Snare hits increase pace—building tension]
    # [Scene: Pilot Block, The Flats | Dawn]

    scene bg ch8_6b08b4_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Slosh of boots in mud, hydraulic hiss, a distant megaphone]
    "The crane lifts with a ponderous dignity. You ride the edge of it with volunteer hands on ropes, the module dangling like a promise. Hands are salted, nails black with mud and oil. The air is"
    "heavier here; the tide starts its subtle pull, water fingering up channels beneath the boardwalk."
    "Eloise Varela arrives in a municipal vehicle, trench coat still beading with rain. She steps down into the mud with an immaculate gait as if a policy could be walked like a pathway. Her AR glass is up; she scans the scene with a planner's hunger."
    show eloise_varela at left:
        zoom 0.7

    eloise_varela "Good morning. Keep me updated. The city needs measurable results."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Results and records. Both."
    show samira_chen at center:
        zoom 0.7

    samira_chen "We have a full log. If anything happens, we follow the safety chain."

    eloise_varela "See that you do."
    # play sound "sfx_placeholder"  # [Sound: A close creak—metal on metal—and someone curses softly behind you]
    # play music "music_placeholder"  # [Music: Low rumble; the rhythm tightens]

    "Ibrahim 'Ibe' Rafiq" "Load is shifting—left hinge. Someone get a line on the aft bracket."
    "You move before you compute. Instinct and training kick in—callouts clipped, hands smarting with adrenaline but moving cleanly. Volunteers respond, a practiced choreography: brace, feed slack, hold tension."

    mara_lin "Red team, aft bracket. Fingers clear. Eyes on the telemetry. Samira, mark the time."

    samira_chen "Marked."

    menu:
        "Signal the crane to pause immediately":
            "You catch the rigger's eye and pulse the hand signal you drilled; the crane's arm judders and holds. The module hangs, breathless, and the ring of people exhales as one."
        "Shout instructions to the volunteers to manually counterweight":
            "Your command slices the air. Volunteers haul with synchronized heaves, boots sucking at the mud. For a moment, the world is a single shared effort, muscle and breath."
        "Trust the sensors and watch the telemetry":
            "You step back and squint at Samira's tablet. The readouts look nominal, but the left hinge's microstrain spikes like a heartbeat. You feel the gap between data and reality as a kind of vertigo."

    # --- merge ---
    "Momentum accelerates. The module tilts minutely—too small to be dramatic, big enough to be wrong. A cable rubs its neighbor and gives a high metallic whine. The press murmurs into recorders, volunteers curse under breath."

    "Ibrahim 'Ibe' Rafiq" "Now! Now! Lock off the left actuator!"
    "The left hinge answers with a groan—then with a sound that is nothing in the simulators: a small, twisting snap followed by the sick, slow slither of metal."
    # [Sound: A long, terrible groan; mud slurps; a crate topples
    hide eloise_varela
    hide mara_lin
    hide samira_chen

    scene bg ch8_6b08b4_4 at full_bg
    # play music "music_placeholder"  # [Music: Rapid strings, heartbeat percussion—Arousal peaks]
    "Time splits. The air tastes like iron and hot oil. You hear someone scream, and it's both immediate and strangely distant."
    show mara_lin at left:
        zoom 0.7

    mara_lin "Evacuate the immediate perimeter! Clear the boardwalk!"
    "But there are complications—children of volunteers watching from behind coils of rope; a TV crew a little too close for comfort; the module's center of mass is veering toward a row of newly planted reed fences."

    "Ibrahim 'Ibe' Rafiq" "If it falls, it'll take the terrace—those fences, the anchor points—we lose the test and a chunk of the Flats' defenses."
    "You look at Samira. Her face is a map of municipal constraint and a sudden, personal worry."
    show samira_chen at right:
        zoom 0.7

    samira_chen "If the installation collapses we log the failure and call for technical support. We shouldn't—' (She swallows) '—we shouldn't take unnecessary risks."
    "Eloise Varela steps closer, voice even, but the coolness is stretched thin."
    show eloise_varela at center:
        zoom 0.7

    eloise_varela "Stop the procedure. Safety first. We cannot have—"
    "Her sentence cuts off as a volunteer, mud-slick, wraps a length of paracord around a failing bracket with a cursing breath and strains with the rest of the makeshift crew."

    "Volunteer (breathing hard)" "We can hold it—if we can get a jack, some wedges—"

    "Ibrahim 'Ibe' Rafiq (to you, urgent, breathless)" "Mara—if we can get reinforcement in place, even a temporary brace, we can save the alignment. We need hands now."
    "Your chest thumps against your ribs. The compass is a hot coin at your collarbone. The horizon is a flattened blur; the sound of the tide is a deeper drum. You can hear the reporters' microphones rustling like birds in a distant thicket."
    "Everything condenses into three brutal options, the kind that leave consequences carved into people and plans."
    # play sound "sfx_placeholder"  # [Sound: Tension in the air like a wire about to snap]
    # play music "music_placeholder"  # [Music: Full, relentless percussion—climaxing]

    menu:
        "Evacuate the site and document the failure to troubleshoot safely.":
            jump chapter9
        "Organize a volunteer manual reinforcement—risky but could save the installation and public faith.":
            jump chapter15
        "Live-broadcast the failure, forcing Eloise to commit municipal resources.":
            jump chapter16
    return
