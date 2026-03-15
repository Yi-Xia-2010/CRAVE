label chapter19:

    # [Scene: Town Streets | Night — Squall]

    scene bg ch14_01c203_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind keening through eaves; distant sirens pulsing]
    # play music "music_placeholder"  # [Music: High, urgent strings; a percussion heartbeat undercutting the storm]
    "You open your eyes to the world rearranged by water. The gavel's echo still vibrates in your bones — a legal punctuation that ripples into everything: announcements, crews, permits, and now, the storm's immediate appetite. Rain hits your jacket like thrown pebbles; each drop is a small drum of inevitability."
    "Your satchel feels heavier because it is full of the town's edges: a printed list of vulnerable addresses, a damp volunteer roster, a pocket radio with one good channel, and the copper bracelet at your wrist"
    "cold as a coin. Your hands shake, not from the cold but from the volume of decisions pressing through you — who to warn first, which levees to shore up, which boats to send."
    "You are at the center because you always are when the town needs someone to move between technical plans and human panic. You taste metal on your tongue: old fear braided with resolve."

    scene bg ch14_01c203_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Static from a radio; a voice: "—repeat, we've lost comms with Dockside four—"]
    show tomas_tommy_reyes at left:
        zoom 0.7

    tomas_tommy_reyes "Mara,' he huffs, voice cut by the wind, 'Folks on the lower boardwalk say the water's breaking over the old pilings. We can't wait on permits."
    "You look across the street where the emergency coordination center has thrown open its doors and spilled warm light into the rain. Inside, the converted auditorium is a map of urgency: folding tables stacked with radios, volunteers peeling on high-visibility vests, and a whiteboard where priorities become arguments."
    # [Scene: Emergency Coordination Center | Night — Interior chaos]
    hide tomas_tommy_reyes

    scene bg ch14_01c203_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Volunteers shouting, paper rustling, radios bursting with fragmented reports]
    # play music "music_placeholder"  # [Music: Dissonant, escalating strings — a taut wire ready to snap]
    show elias_navarro at left:
        zoom 0.7

    elias_navarro "We have two operational launch points left. The harbor tugs are offline. The institute recommends triage per the emergency matrix — critical infrastructure, then medically vulnerable. If we deviate, we risk displacing resources."
    "You can hear the engineering logic, tight and precise. But down the hall, a woman cries that her mother is stranded at Saltwren Commons; the Commons will flood if the tide and surge combine. Numbers and faces slide past each other and entangle."
    show mara_lin at right:
        zoom 0.7

    mara_lin "The Commons is full of seniors and kids tonight — Rae coordinated a sleepover for volunteers who couldn't get home. The tidal window matches the surge. If we follow the matrix to the letter, they may not make it."
    "Elias Navarro exhales, a short, sharp sound like the intake before a calculus. He taps the tablet, fingers moving with training. 'I— I can request reallocation, but it will need sign-off from the county ops. That's thirty minutes minimum if the network holds.'"
    "You feel time folding. Thirty minutes is a canyon in this weather."
    "Dr. Amina Bhatt moves between clusters of volunteers like a lighthouse keeper; her voice is calm but unnerving in its clarity. A tablet is clipped to her hip. She has data for everything — wave set"
    "models, breach probabilities, tireless scenarios. When she looks at you, the room briefly quiets as if her eyes pull the air taut."
    show dr_amina_bhatt at center:
        zoom 0.7

    dr_amina_bhatt "Mara, the forecast updated. Surge exceeds the promenade's design threshold by nearly a meter. If the wave overtops, the undercut will travel fast. We need to prioritize evacuation routes that stay above the projected flowline."
    "You digest the numbers and the meaning: places that matter to memory — Saltwren's garden plots, the boardwalk where Tommy taught kids to bait a line — are now choices on a spreadsheet. The bitter part sits heavy: triage is not just logistics; it's moral arithmetic."

    menu:
        "Order volunteers to prep boats for Saltwren":
            "Your voice cracks but firm; a cluster of hands raise, eyes bright with willingness."
        "Push for formal reallocation through county channels":
            "Elias nods with bureaucratic calm; a volunteer's hopeful furrows smooth into impatience."

    # --- merge ---
    "Narrative continues below."
    "The volunteers move. Some are steady because they've been steady for years; some are trembling, young faces lit by phone screens. You watch Rae sprint past in a soaked hoodie, her hair plastered to her temple,"
    "camera slung but forgotten. She throws you a glance that says 'Do something' without a need for words."
    hide elias_navarro
    show tomas_tommy_reyes at left:
        zoom 0.7

    tomas_tommy_reyes "We can get skiffs off the old boatyard if we cut the towing lines,' he says. 'But the tide'll drag us out if the surge hits early. We need a marshal at the mouth, someone on watch with the depth markers."
    "You can already feel the list widening: who to send, which path to take, what to sacrifice. There is no neutral move here."
    # [Scene: Promenade (Half-Finished) | Night — Wind-hammered construction site]
    hide mara_lin
    hide dr_amina_bhatt
    hide tomas_tommy_reyes

    scene bg ch14_01c203_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Cables groan; a generator wails; the sea's roar punctuates sentence fragments]
    # play music "music_placeholder"  # [Music: Percussion accelerates; a low brass warns]
    "On the promenade, the company foremen and a small security detail hunch beneath the scant shelter of a trailer. Celeste Park stands with the portfolio you remember only as a shape: tidy, sealed, and oddly luminous"
    "under the stormlight. Her hair is neat despite the weather; her coat makes her a cutout against the chaos. She watches you with those steel eyes that catalogue risk and possibility at the same time."
    show celeste_park at left:
        zoom 0.7

    celeste_park "The contractors are locked in to critical reinforcement. If we pull them now, we risk the entire schedule and the safety protocols they follow. There are workers under tarps; some are injured. We have heavy equipment that could clear debris for faster passage."
    "She speaks like someone for whom leverage is oxygen."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Their heavy equipment could also become a hazard. If the surge hits, it could wash out and shred the boardwalk — taking people with it. We need to think about removal routes and where to stage the injured."
    "Celeste Park tilts her head, narrowing her eyes in a way that says she's already factoring your objection into her calculus. Her expression is unreadable in its complexity — part annoyance, part calculation, part something like respect that she will not acknowledge."

    "Celeste Park (softly)" "Or you can let them stay and hope the matrix saves them."
    "The sentence lands like a gauntlet."
    "Elias Navarro moves between you and her with the worn diplomacy that has kept him at tables before. He places a hand lightly on your elbow — not necessarily tender, but an attempt to side-step confrontation into conversation."
    show elias_navarro at center:
        zoom 0.7

    elias_navarro "We have limited stretchers, limited fuel for launches, and a half dozen calls from the county asking for prioritized assets. If we consolidate resources here at the promenade, we can move injured faster to the medical hub. But that means fewer boats for Saltwren."
    "His jaw is tight. You can see the gears of decision turning: his training says triage by vulnerability and by strategic asset protection; his heart is something else, visible in the quick look he sends toward"
    "the Commons on the horizon where a pale smear of light betrays ankle-deep standing water."

    mara_lin "So it's that choice: injured workers and infrastructure here, or seniors and kids at Saltwren. Both are people. Neither option is clean."

    "Elias Navarro's reply is a whisper, a fragment" "There are protocol consequences if we deviate."
    "You don't say the word 'consequences'; there's no need — the storm speaks in consequences."

    menu:
        "Demand the mobile cranes be used to lift people at the promenade":
            "Celeste flares — an imperious nod; she directs the foremen with razor efficiency."
        "Redirect volunteers and skiffs to Saltwren, using Celeste's machines later":
            "Elias' fingers curl; he looks like someone separating his plans into what he must follow and what he wants to do."

    # --- merge ---
    "Narrative continues below."
    "You watch as decisions begin to concretize into actions: Celeste barking orders into a radio, Tommy hustling a line of volunteers toward the boatyard, Rae sprinting toward a flooded lane with a battery pack and determination like a blade."
    "Dr. Amina Bhatt returns from a console, face flushed from exertion. She drops a tablet on the table, revealing a new model run with the updated surge. Her voice is flat with the force of evidence."
    hide celeste_park
    show dr_amina_bhatt at left:
        zoom 0.7

    dr_amina_bhatt "If we commit all launches to Saltwren now and the promenade fails catastrophically, the debris field will close the harbor and strand recovery vessels. Conversely, if we focus on infrastructure and delay direct rescues, there's a window — small — where the Commons will be unsurvivable."
    "Your chest tightens into a steady drum of panic. The room feels too small for the problem. There is a palpable split: one radial of the town clinging to projections and the other to the immediate human noise at your feet."
    "Elias Navarro steps closer, the rain stitched through his jacket already. 'Mara,' he says, and there is a softness in his voice that briefly slips the harness of protocol. 'What do you want on the list right now?'"
    "The question is both practical and unsayable. You have trained for this: your life has been a negotiation between ecological models and the pull of memory and responsibility. Your answer will order who lives tonight and who becomes a missing name in a morning story."
    "You can feel the room leaning on you. Volunteers fall quiet as if waiting for a baton."
    "Your mind refuses easy arithmetic. You recall a sibling's laugh, pockets full of clam shells, and the last time the sea took and did not give back. You taste salt and loss and the metallic clarity of decision."
    hide mara_lin
    hide elias_navarro
    hide dr_amina_bhatt

    scene bg ch14_01c203_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind swallows a streetlamp; the radio bleats an urgent, undecipherable call]
    "The arousal ramps to a sharp peak. The center of the town narrows to a single hinge: you, the leader by default, must choose a distribution of teams and resources. Each allocation is a moral vector."
    "Then, because the world insists on being complicated, a new call crackles through — civilian reports that the old nursery at Saltwren has a generator failure and several immobile residents. Simultaneously, the promenade's foreman radios that a makeshift scaffold has collapsed and two workers are pinned."
    "Your breath stops. Both calls are alive, urgent. Both require the same limited assets: stretchers, skiffs, fuel, volunteers who cannot be in two places at once."
    "Elias Navarro looks at you, and for a second his face is an open map of conflict. 'We can petition to pull county reserves,' he says, voice thin. 'But I— I can't promise they'll arrive before either location is overwhelmed.'"
    "You feel the weight of his uncertainty like a physical thing leaning on your shoulder. You are aware, in a raw way, of the strain threading into whatever this is between you and him — not"
    "a single emotion, but a braided complexity: shared purpose, mutual accusation, urgent proximity. His expression is hard to parse; unreadable and full of intent."
    "Tommy catches your eye and nods once, a motion that says he will follow whatever you decide."
    "Everything tightens. The storm seems to hold its breath with you."

    menu:
        "Send the first wave to Saltwren, tie the cranes to recovery later":
            "Volunteers cheer and rush, but Celeste's jaw hardens into a vow of paperwork and reprisals."
        "Focus initial rescue on pinned workers at the promenade, then attempt a secondary Saltwren run":
            "Celeste gives a brittle, almost relieved smile; Rae slams a fist into her palm—impatient but mobilized."

    # --- merge ---
    "Narrative continues below."
    "You feel the tide not only at the shoreline but in people's faces — hope, accusation, fear. The room is a constellation of motions: radios, clipping rain, shouted names, a tableau of human agency bent into shapes by urgency."
    "You lift the marker. Your voice — when you speak — is a thread pulled taught."
    show mara_lin at left:
        zoom 0.7

    mara_lin "We allocate the launches and stretchers now. We split teams: rapid-response for the pinned at the promenade and two skiffs to the Commons. Dr. Amina, increase the monitoring sweep. Elias, I need your call-sign on the reallocation. Tommy, marshal the volunteers at the dock. Rae, document everything."
    "Your words are a map. But even as you speak, you feel the fissure under the sentence: resource limits will make those allocations less than intended. You can already guess which side will get the barest scrim of help and which will be met by a wave of arrival."
    "Elias Navarro hesitates — a breath that lengthens into something like an apology. He meets your gaze. 'If the county denies reallocation,' he says, 'we hold to the plan and re-route as possible. I'm— I'm with"
    "you in this, Mara.' The last three words are quick, nearly swallowed by the wind."
    "He looks toward Celeste Park, toward the foremen, toward the lights that mark the Commons. There is something raw and urgent beneath his procedural language; a tension between his professional identity and the neighbor he is"
    "being asked to be. His face is complex — not simply allied, not simply opposed."
    "The marker ink blots slightly as your hand presses harder. You can feel your pulse in your throat. This is the hinge. The allocation call will be sent. Lives will orbit the result."
    "You raise your hand to confirm, to speak the final allocation into motion, and for a single, jagged heartbeat the world narrows to the sound of rain and the thud of your own blood."
    hide mara_lin

    scene bg ch14_01c203_6 at full_bg
    # play music "music_placeholder"  # [Music: Strings snap into a single, sustained high note; the sound seems to hold breath]
    "This is where decisions harden into consequences. The storm does not care about your intentions."

    scene bg ch14_01c203_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter22
    return
