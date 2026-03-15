label chapter3:

    # [Scene: Harborwell City Hall — Council Chamber | Evening]

    scene bg ch3_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low murmur of the crowd, the periodic creak of the old chamber benches, a distant gull cut off by the windowpanes]
    # play music "music_placeholder"  # [Music: A steady, hopeful string motif—mid-tempo, rising gently beneath the room’s conversation]
    "You are in the aisle, the Moleskine tucked into the inner pocket of your jacket. The map you folded the other day sits heavy there in your mind even if it isn’t in your hands—routes and"
    "marsh edges and neighborhoods you know by the cadence of their front steps. The memory of past compromise, the one you carry like a pebble in your chest, presses against your ribs. It is not sharp"
    "enough to stop you tonight. It is simply there, a reminder of what’s at stake."
    "Samir stands a few rows ahead, his phone perched steady on a tripod; the glow of its screen throws a bluish strip across his face. He doesn’t smile. He doesn’t have to. He films everything with the careful distance of someone who knows that images will outlast words."
    "Across the dais, Maren Voss stands with a tablet angled toward the council. Her coat is immaculate. Her voice is precise and warm in turn, practiced in the cadence of persuasion."
    show maren_voss at left:
        zoom 0.7

    maren_voss "We have engineers standing by. A reinforced sea wall along the boardwalk, a consolidated commercial strip—deliverable within two years. Jobs, stable tax revenue, a tangible defense. We can protect Harborwell now."
    "A few hands clap—measured, hopeful. The idea of protection, of immediate work, hangs like a promise people crave after too many sleepless tides."
    "Elias Hart is by the rail, whistle around his neck like a talisman. When he speaks, his voice is rough with the sea and with earnestness."
    show elias_hart at right:
        zoom 0.7

    elias_hart "A wall treats symptoms and forgets the shore. Marshes, living platforms, local co-op investments—these create livelihoods that last. They root us to place, not push us behind corporate glass. We can pilot modular homes and marsh restoration simultaneously. People here know how to live with water—let’s listen."
    "His words ripple through the audience. Some faces brighten; others narrow. Elias leans on the rail, gaze sweeping the room until it rests, briefly, on you. The look is complicated—hope threaded with something like plea. You"
    "do not know whether your private conversation weeks ago would change the meaning of that look. The past is a split screen; you choose to listen to the urgency instead."
    hide maren_voss
    hide elias_hart

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant breath of air-conditioning, a chair scraping as someone shifts]
    "Professor Julian Kim rises to his feet and clears his throat. He folds his hands like someone with a thermos full of steadiness."
    show professor_julian_kim at left:
        zoom 0.7

    professor_julian_kim "The models show multiple viable trajectories. With targeted restoration and phased living platforms, we can maintain occupancy and reduce long-term losses. A mixed approach reduces risk concentration—statistically significant across scenarios."
    show mayor_ana_delgado at right:
        zoom 0.7

    mayor_ana_delgado "Can you make it plain, Julian? People need to hear what the math actually means."

    professor_julian_kim "It means: we can reduce expected displacement by dispersing risk. It means community-led action, adequately funded, is not just idealism. It is resilience."
    "The crowd murmurs in a different key now—data is an undercurrent to desire. You feel your throat tighten. The pebble in your chest is warmer; it is no longer only guilt. It is responsibility, primed to be action."
    "Iris slides into the aisle beside you like she’s always been there: scent of brine and diesel, fingers still carrying the memory of rope. Her voice is a low rumble meant for you as much as for herself."
    show iris_tanaka at center:
        zoom 0.7

    iris_tanaka "We keep the people in the picture, Maya. Not a line-item on a ledger."
    "You nod, fingers finding the brass compass locket at your collar out of habit. It is cold against your skin. You press it with the pad of your thumb and let the rhythm steadify you."

    menu:
        "Flip open your Moleskine and double-check the maps one last time":
            "You open to sketch pages—tide lines, marsh thresholds, a note in the margin: 'community hubs, redundancy'—and the shapes steady your argument in your mind."
        "Close the book and walk to the rail to stand beside Elias":
            "You fold the Moleskine back into your pocket and step forward until you are shoulder-to-shoulder with Elias; his elbow brushes yours and it feels like an alliance even before a word is spoken."

    # --- merge ---
    "Scene continues"
    "The mayor taps her gavel once, not for order but to invite focus. Lights hum. You can feel the room holding its breath."

    mayor_ana_delgado "We need a path forward tonight. Maren has offered a direct route to security. Elias and community organizers propose a distributed, labor-and-knowledge model. Professor Kim has articulated technical viability. Maya—"
    "Her eyes land on you. The gaze is not accusatory; it is expectant in the quiet way of someone asking a friend to tell the truth."
    "You rise because your legs answer before your mind decides. The aisle seems longer than it is, lined with faces that are neither wholly for you nor against you—complex, watchful. You catch Samir’s eye. He gives"
    "you a small tilt of his chin: steady. Your brother’s presence is an anchor that keeps you honest."
    hide professor_julian_kim
    hide mayor_ana_delgado
    hide iris_tanaka

    scene bg ch3_98c6f2_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low thrum of applause that begins like a ripple and stops at the start of your sentence]
    "You speak, and your voice is a measured tide."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "Mayor, Council—this isn’t just an engineering problem. It’s a question about whom we protect and how we define safety. The models Professor Kim shared show options, not mandates. We can layer protection: structural defenses where absolutely necessary, and living, adaptive systems where they sustain livelihoods. We can fund pilots that give work to locals while restoring ecosystem services—"
    "Maren Voss interrupts politely, a smile that fits like a well-pressed collar."
    show maren_voss at right:
        zoom 0.7

    maren_voss "With respect, Maya, 'maybe' and 'pilot' are comforts for those with time. We need payrolls—now. Businesses are collapsing. People need steady wages and a clear shore."
    "You meet her eyes. There is steel there too, the kind of steel born from hard decisions. The room tightens; two logics pulling at the same map."

    maya_reyes "I don’t deny urgency. I lived urgency—and made a choice that cost people. I’m not here to repeat that. I’m here to make sure urgency doesn’t become an excuse for unjust displacement. If we rush into a one-size wall project, we consolidate risk and benefits in ways that will leave the most vulnerable exposed."
    show elias_hart at center:
        zoom 0.7

    elias_hart "And if we let fear sell us a single solution, we lose community ownership of resilience. Jobs made from rebuilding our shore should be jobs that train locals, pay living wages, and are rooted in knowledge that belongs here."

    maren_voss "No one is asking to sell the town’s soul. We are asking to keep it breathing. Economies collapse faster than marshes restore. We have already seen that."
    hide maya_reyes
    show professor_julian_kim at left:
        zoom 0.7

    professor_julian_kim "Both sides raise valid points. The statistical optimum on its own—"
    hide maren_voss
    show mayor_ana_delgado at right:
        zoom 0.7

    mayor_ana_delgado "Ana Delgado doesn’t get to script everyone's life. But she does need a plan that holds votes and keeps people fed. Maya—what do you advise?"
    "You feel the pebble shift. You could reach for the philanthropic offer again—that shadowy funding that would buy time but demands strings you cannot yet untie. You could declare for the co-op, risk political ire but"
    "ignite a people-powered campaign. You could step with Maren and secure immediate protection and jobs, steering municipal trust back toward you but at the cost of your private conscience."
    "Your chest tenses, and your hands find the lapels of your jacket, steadying yourself through touch. The chamber sounds recede a fraction; all that remains is breath, the small squeak of someone shifting, your own pulse measuring out the next moments."
    # play music "music_placeholder"  # [Music: The hopeful string motif raises a single, sustained note—no panic, only focused ascent]
    "You remember the map on your bench, the way you traced corridors of care between lab and docks. You remember the faces of people who will rely on whatever decision comes from you. The weight in"
    "your chest isn’t only guilt tonight; it is also a readiness—an opening you haven’t allowed yourself in years."
    "Iris’s hand rests for a moment on your forearm—weathered and warm."
    hide elias_hart
    show iris_tanaka at center:
        zoom 0.7

    iris_tanaka "Whatever you name tonight, make sure it leaves room for people to speak into it."
    "You swallow. You are aware of every breath—of the salt of Harborwell settling on your tongue like a careful promise."

    menu:
        "Cite Professor Kim's models first, framing the decision in data and distributed strategy":
            "You lift your chin and reference the model projections, steering the room toward a mixed, phased approach that promises both protection and local work—eyes in the crowd shift, some nod, some frown."
        "Appeal directly to the town—tell one short, human story to cut through the politics":
            "You tell the room about a neighbor’s porch that took three tides to rebuild and the way children learned to read storm warnings; the chamber hushes, the math softens against the human detail."

    # --- merge ---
    "Scene continues"
    "The room expects a line—one definitive stance. The mayor’s fingertips drum once against the gavel like a heartbeat."

    mayor_ana_delgado "Council members need a recommendation. This body needs something to move on tonight. Maya—if you speak for the models, we’ll listen. If you stand with the co-op, Municipal Finance will have to adjust their projections. If you endorse the redevelopment, we can mobilize immediately. The floor is yours."
    "Your palms are dry and warm. The pebble in your chest has stopped being just an accusation; it has become a compass that points toward a difficult but principled horizon. You can feel the room leaning in, collective breath coiled—expectant but not frantic."
    "This is the fork. This is where your professional credibility, your history, your heart collide."
    hide professor_julian_kim
    hide mayor_ana_delgado
    hide iris_tanaka

    scene bg ch3_98c6f2_4 at full_bg
    # play music "music_placeholder"  # [Music: The strings settle into a clear, mid-tempo pulse—steady, hopeful]
    "You inhale, the sound small, the motion decisive. The next words will not resolve everything. They will choose a direction."

    menu:
        "Stand with Elias and the co-op — push a community-led adaptation plan.":
            jump chapter4
        "Endorse Maren's redevelopment project for immediate protection and jobs.":
            jump chapter7
        "Pursue the private philanthropic funding—quiet emergency money that buys time but requires concessions.":
            jump chapter10
    return
