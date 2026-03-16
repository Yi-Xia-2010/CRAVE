label chapter5:

    # [Scene: Rooftop Garden Lab | Night into Dawn]

    scene bg ch5_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Soft, ascending strings; a steady percussion like a heartbeat]
    # play sound "sfx_placeholder"  # [Sound: Rain pattering, the distant slap of waves, the occasional creak of rigging]
    "You start where the failure left off — elbow-deep in tar and salt, headlamp haloing the edges of the workbench. The seam that split in the storm is a lesson that hums in your teeth; every"
    "frayed rope and popped rivet is a note in a running sermon about humility, speed, and stubborn skill. You promised the town action, not platitudes. Tonight, you keep that promise."
    "Your palms smell of creosote and damp canvas. You run a thumb along the bend of the bent ring on your finger until the cold steadies your pulse. The rooftop is cramped but alive: crates of"
    "recycled polymer, coils of tensile strap, a spool of galvanised cable, and a chalkboard full of half-sketched load diagrams. Moist soil clings to your boots. Under the greenhouse glow the plants look almost defiantly green, like"
    "small flags that refuse to be erased."

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Camera shutter — a soft, contented series of clicks]
    "Kai Nakamura's camera clicks again and again, collecting angles of damp tarps and the way the morning slips gold across rivets. He smiles without looking at you — a private, delighted smile that says he finds"
    "this frantic, messy life beautiful. You feel it, too: the work's ugly grace, the geometry of things that hold."
    show kai_nakamura at left:
        zoom 0.7

    kai_nakamura "You always make the worst deadlines look poetic."
    show iris_alvarez at right:
        zoom 0.7

    iris_alvarez "You always take pictures of me like I'm going to be a museum exhibit someday."

    kai_nakamura "Maybe you are. The town's museum of stubborn things.' (He winks, then knots a loop.) 'Hand me the crimper?"
    "You reach, and your fingers find his. For a split second the world narrows to the warmth of his palm and the shared pressure of a tool against a stubborn bolt. It's a small thing — a handover — but it feels like the way a promise gets made real."

    menu:
        "Double-check the tensile chart one more time":
            "You run your finger down the chalkboard, reading numbers aloud. Kai Nakamura hums, then adjusts the anchor point. The strap holds; the knot sits like a satisfied animal. You're calmer for knowing the math."
        "Trust your gut and finish the knot":
            "You stop second-guessing and finish the crimper pull. Kai Nakamura lets out a breath as the strap cinches tight. There's a reckless ease to action; the joint feels right, not perfect, but honest."

    # --- merge ---
    "Continue"
    hide kai_nakamura
    hide iris_alvarez

    scene bg ch5_4001e7_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Laughter, shouted measurements, the rhythm of hammers]
    "Neighbors arrive in trickles and then in a tide. Lina's marina crew shows up with reclaimed beams, wet and heavy and grinning — the marina's neon stripes blurred by rain. Tom appears as if from the"
    "shadow of Old Shipwright's Lane, sleeves rolled, a tower of rivets in his hands and a grin that breaks the worry-line on your face. Etta arrives last, small and exacting, carrying a tin of seeds and"
    "a thermos of something bitter and hot."
    show tomas_tom_alvarez at left:
        zoom 0.7

    tomas_tom_alvarez "Thought you'd want more steel. You did good, kid. We can shore this up proper."
    show iris_alvarez at right:
        zoom 0.7

    iris_alvarez "We learned what failed. Now we make it better."

    tomas_tom_alvarez "Right. Then let me be the one who complains about your stubbornness when you won't let us sleep, huh?"
    show etta_bloom at center:
        zoom 0.7

    etta_bloom "Sleep is overrated if the sprouts survive.' (She produces a packet of microgreens.) 'These will feed the volunteers between shifts."
    "Their hands are quick and steady. You hand out bracing plates, you mark angles, you test the seams again — and again. The rooftop becomes a small laboratory of improvisation: dynamic loads estimated with borrowed formulas,"
    "straps looped through reforged eyes, a prototype joint bolstered with triangulated braces. Every iteration is faster than the last. Mistakes happen; you fix them together."
    hide tomas_tom_alvarez
    hide iris_alvarez
    hide etta_bloom

    scene bg ch5_4001e7_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Keyboard clicks, the ping of upload success]
    "Kai Nakamura rests his elbow against a crate and watches you file the change. 'Open-source and open-hearted,' he murmurs. 'You're really doing this.'"
    show iris_alvarez at left:
        zoom 0.7

    iris_alvarez "If one town gets to adapt, others should get the same chance without buying into a corporation's glossy brochure."
    show kai_nakamura at right:
        zoom 0.7

    kai_nakamura "Then we make the brochure ourselves.' (He grins, but his eyes go soft.) 'And we'll have better photos."
    "He reaches across and presses his palm to your braided bracelet, as if steadying something more fragile than metal. The gesture stops your breath — not because it's dramatic, but because it's deliberate: a small anchoring that says I am here, I will hold."

    menu:
        "Accept the break for coffee and rest":
            "You let go of the strap and rub the ache from your knuckles. Tom insists on making coffee; Kai Nakamura teases you for being responsible. You close your eyes for ten minutes and wake to a warmer shoulder and renewed focus."
        "Keep testing until the sun is high":
            "You refuse the break. Your fingers go numb around the tools; your thoughts tunnel into the problem and solutions bloom under pressure. When you finally look up, the team has adjusted their rhythm to yours — energized rather than exhausted."

    # --- merge ---
    "Continue"
    # [Scene: Rooftop Garden Lab | Midday]
    hide iris_alvarez
    hide kai_nakamura

    scene bg ch5_4001e7_5 at full_bg
    # play music "music_placeholder"  # [Music: Brighter strings, a steady ascending motif]
    # play sound "sfx_placeholder"  # [Sound: The municipal phone buzzing; a notification tone]
    "Your tablet buzzes with a terse message from Municipal Hall. You don't like messages that arrive like business cards — short, clipped, full of implication. Marin Voss's name is on the screen. You open it because not opening it would be an accident of cowardice."

    "Message (Marin Voss)" "Send specifications for the reinforced joint. I will review before tomorrow's inspection."
    "You: The message reads like a drill. No warmth. No flourish. But the content is a bridge. You type back, concise and technical, attaching diagrams and load calculations. You press send before you can second-guess the tone."
    show kai_nakamura at left:
        zoom 0.7

    kai_nakamura "That's something, right?' (He nudges your shoulder.) 'It's not enthusiasm, but it's not a door either."
    show iris_alvarez at right:
        zoom 0.7

    iris_alvarez "It's a door with a cautious hinge."
    hide kai_nakamura
    hide iris_alvarez

    scene bg ch5_4001e7_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Footsteps, a paper rustle, the inspector's shoes on gravel]
    "The inspector walks the prototype with a professional eye, tapping measurements into a tablet. He finds improvement — smaller gaps, better anchor redundancy — and he notes them with a tone that balances relief and legal duty."

    "Inspector" "This is a marked improvement. You're meeting several performance thresholds we didn't expect after the last failure."
    show iris_alvarez at left:
        zoom 0.7

    iris_alvarez "We patched the weak points and rerouted the load paths. We tested under strain cycles."

    "Inspector" "I'm impressed at the ingenuity.' (He hesitates.) 'However, there are permit issues. Some of these retrofits fall under municipal codes for structural alteration. I have to flag that in my report."
    "The word 'permit' is a weight. It stains the air a little. You feel your shoulders tighten — that familiar tug of bureaucracy — but the room is full of faces that have come out in"
    "the rain because they believe the roof and the town matter. Their belief is a counterbalance to the inspector's paperwork."
    show tomas_tom_alvarez at right:
        zoom 0.7

    tomas_tom_alvarez "We'll do whatever it takes.' (He squares his jaw.) 'We just need the okay not the finger-wagging."

    "Inspector" "I can accelerate a provisional review if Marin Voss or Ravi signs off. I can recommend flexibility, but it isn't mine to grant."

    iris_alvarez "Then we'll ask Marin Voss and Ravi to see it themselves."
    # [Scene: Greenhouse Commons | Evening]
    hide iris_alvarez
    hide tomas_tom_alvarez

    scene bg ch5_4001e7_7 at full_bg
    # play music "music_placeholder"  # [Music: Quiet hopeful piano with gentle swells]
    # play sound "sfx_placeholder"  # [Sound: Clink of mugs, low mutters, the distant tide]
    "You organize a bridging meeting under the Greenhouse Commons lamps, exactly where community and craft can sit in the same warm light. The table is long and rough, strewn with diagrams, cups of steamy tea, and"
    "a sample joint bolted to a pallet for close inspection. Ravi arrives first, sleeves rolled and an expression that mixes worry and strategy. Marin Voss comes last, pale-gray eyes narrow with assessment."
    show ravi_singh at left:
        zoom 0.7

    ravi_singh "People have been talking. If this works, it changes our options. If it fails, we need contingency plans."
    show iris_alvarez at right:
        zoom 0.7

    iris_alvarez "We won't deny risk. We won't hide testing data. We want a provisional agreement — certification to allow small-scale implementation while we continue real-time testing and iterations."
    "Marin Voss: (Quiet) 'Certification in phases. Clear metrics for rollback. Liability clauses.' (They study the physical model.) 'You've reduced single-point failures. That triangulation is better than I expected from a community build.'"
    "Iris Alvarez: (Startled by the praise) 'We iterated fast. We made the seams redundant. We filed everything online — version control, test logs, stress maps.'"
    show marin_voss at center:
        zoom 0.7

    marin_voss "I read some commits.' (A small admission.) 'The version notes were… thorough."
    "Kai Nakamura: (Leaning forward) 'It's not pretty. It's honest. We want municipal buy-in for provisional certification — enough to mobilize materials and allow adjacent neighborhoods to replicate without legal risk.'"
    "Marin Voss studies the room. For a long moment their gaze flicks from the sweat-matted hair of volunteers to the compactness of your diagrams, to the microgreens Etta offers like a conciliatory olive branch. The greenhouse"
    "light softens the edges of their features; something in the lines of their face relaxes."

    marin_voss "You've got ingenuity and community capacity.' (They fold their hands.) 'We can draft a tiered provisional approval. Conditions — monitoring, rollback triggers, and a capped liability framework. I'll present it at Hall."
    "Ravi exhales like a man who has been given a tool he didn't expect. 'If Marin Voss brings that forward and the inspector files a supportive note, we can unlock a small emergency fund. It's not a full grant, but it's movement.'"
    "You feel a lightness you haven't felt since before the storm pulled the pier out from under the festival. It's not victory; it's mobility — the town can move again. The shoulders around the table loose their tense set; laughter sparks, small and relieved."
    hide ravi_singh
    show etta_bloom at left:
        zoom 0.7

    etta_bloom "You're all children of the shore. You argue like it.' (She smacks your hand lightly.) 'Now finish that cup."
    "Kai Nakamura meets your eyes across the table and lifts his mug in a private toast. You lift yours back. The sound of ceramic is tiny and authoritative."

    menu:
        "Thank Marin personally, vulnerably":
            "You step forward and say what you've been holding: that you needed them to believe this was possible. Marin Voss flinches at the directness but nods, the movement almost imperceptible. The room shifts closer."
        "Let the group celebration stand, stay focused on logistics":
            "You keep your gratitude practical — who to contact, which tests to run next. The energy remains efficient; people leave with tasks and momentum. You tuck the warmth into your chest to use later."

    # --- merge ---
    "Continue"
    hide iris_alvarez
    hide marin_voss
    hide etta_bloom

    scene bg ch5_4001e7_8 at full_bg
    # play music "music_placeholder"  # [Music: Strings swell gently to a hopeful peak]
    # play sound "sfx_placeholder"  # [Sound: The distant shore, a gull calling; footsteps receding as people disperse, contented chatter]
    "You walk the path off the Greenhouse Commons with Kai Nakamura at your side. The town isn't fixed. The funding line is still thin. There are holes in the plan you haven't solved. But around you,"
    "people move with purpose, and the municipal machinery — cautious and bureaucratic and essential — creaks forward instead of closing like a trap."
    show kai_nakamura at left:
        zoom 0.7

    kai_nakamura "You did this."
    show iris_alvarez at right:
        zoom 0.7

    iris_alvarez "We did this."
    "He presses his palm to your bracelet again, this time not to anchor you but to bind a shared cadence. It's small. It's human. It feels like the first steady step up after standing on slippery rock."
    "You think of the pier, the festival lights, Tom's grin, Lina's rough hands, Etta's seeds. You think of Marin Voss bending rules like light to find daylight, and Ravi finding funds like a narrow seam of"
    "ore. You think of the uploads to the repository, the way strangers across a wire could pull down your files and learn to save their own streets. The thought makes you dizzy in the best possible"
    "way."
    "Page-Turn Moment"
    "The wet promenade catches neon and lamp light and throws it back in bright strips. You can almost see, somehow, the town's future — not polished, but stitched, a patchwork held together by deliberate hands. You"
    "feel the ascent as a gradual physical incline rather than a sudden lift: a string of agreements, a handful of signatures, a thousand small repairs. You put a hand to the bent ring on your finger"
    "and let the cold remind you that promises are kept in action."
    hide kai_nakamura
    hide iris_alvarez

    scene bg ch5_4001e7_9 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter8
    return
