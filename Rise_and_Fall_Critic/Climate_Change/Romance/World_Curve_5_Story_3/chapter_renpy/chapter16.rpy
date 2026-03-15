label chapter16:

    # [Scene: Flooded Construction Fringes | Pre-dawn — Storm Lurking]

    scene bg ch13_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Loud, rhythmic slap of waves against temporary barriers; distant metal groan as a barge shifts]
    # play music "music_placeholder"  # [Music: Dissonant cello, slow heartbeat tempo]
    "You move through the wet fringe like someone walking through fogged glass—every shape is familiar and altered, edges softened by water and fatigue. You remember the choice you made on the quay: a mixed emergency—Mateo's crews"
    "repairing where they could, you organizing hands to shore up living barriers, Sora spooling volunteers into the mud. It felt like a compromise then; now the seams show."
    "The air tastes of iron and diesel; your boots leave dark prints that the tide tries to swallow. The rain hasn't let up; it sharpens voices into staccato orders and anxious laughter. Jun's headlamp bobs ahead,"
    "a small, human pulse. Elena hands out plastic-wrapped empanadas like blessings; you accept one with sticky fingers and warm gratitude, but you don't taste it—there is no appetite for warmth tonight."
    show mateo_hale at left:
        zoom 0.7

    mateo_hale "Aria—give me the next splice. Clamp the winch now, Jun, before it slips."
    show aria_navarro at right:
        zoom 0.7

    aria_navarro "I'm on it—tell me the angle you want. Slow and steady."

    mateo_hale "We don't have slow. We have the tide timer and the people's houses on the other side."
    "His jaw is a rock in the downpour. There's no cruelty in his tone, only a pressure you recognize as someone trying to hold a collapsing thing together with measured brute force."
    "Sora Lin, muddy and incandescent, appears on the quay's lip with a line of volunteers. They meet your eyes and, for a moment, there's that raw look—sorrow braided to resolve—that you hate and need all at once."
    show sora_lin at center:
        zoom 0.7

    sora_lin "We're losing ground at sector three. The volunteers are exhausted and we still lack sandbags—where did they send the supply truck?"

    aria_navarro "It got rerouted to clear a collapsed boardwalk. The crew there called for—"

    sora_lin "Then we make the truck the priority. People are standing in water in their kitchens."
    "You want to answer with data—tidal forecasts, load tolerances—but the spreadsheets are useless when someone's child is shivering in a wet shirt. You feel the old reflex: solve, fix, move the numbers until they sit like armor. It doesn't hold tonight."
    "Jun sidles up, grease on their knuckles, breath visible in the air. They hand you a small, sodden sensor with a blinking LED that looks sullen."
    hide mateo_hale
    show jun_park at left:
        zoom 0.7

    jun_park "The sea-level reader's intermittent. The buoy drifted an inch—might be biofouling or a line snag. I can jury-rig it, but I need two hands and a dry spot."

    aria_navarro "Do it. I'll get you the tools and—"

    jun_park "We're all out of dry spots, chief."
    "There is a humor in them that acts as an anesthetic. You let it sit for a second like something that smells faintly of home and salt."

    menu:
        "Go with Mateo to secure the heavy modules":
            "You shoulder the wet rope and let Mateo's pace set you—his quiet focus gives you something solid to follow, and you both absorb the physicality of fixing rather than arguing. It eases the raw edges in your chest for a time."
        "Stay with Sora and the volunteers to shore the living barrier":
            "You kneel in the mud beside Sora, hands learning the rhythm of sapling placement and knotted rope. The work is slower, more fragile, but it gives people a ritual to anchor to; their soft thanks is its own kind of repair."

    # --- merge ---
    "Continue to the next sequence"
    "Mateo catches your decision with a flash of relief or disappointment—it's unreadable in the wet light—and sets to work like a man trying to fold the sea into a plan. Sora looks at you with something"
    "like accusation and gratitude at the same time. Either way, the tide is indifferent to what you choose."
    # [Scene: Stormwall Construction Site | Dawn — The Second Surge]
    hide aria_navarro
    hide sora_lin
    hide jun_park

    scene bg ch13_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A rising roar as the sea swells; machinery coughing; a chorus of shouted, clipped commands]
    # play music "music_placeholder"  # [Music: Low brass, rising in a slow, menacing swell]
    "You have barely caught your breath when the second surge arrives—taller, angrier, a lip of water that crashes against your expectations and the sections you'd held together overnight. A modular block, half-aligned and braced by volunteers,"
    "jerks loose. The crane operator curses; a winch screams. A wooden form snaps with a sound like a throat closing."
    show mateo_hale at left:
        zoom 0.7

    mateo_hale "Hold the line! Cut the cable—cut it now!"
    show aria_navarro at right:
        zoom 0.7

    aria_navarro "No—Jun, the splice—"
    show jun_park at center:
        zoom 0.7

    jun_park "I've got it! One—two—"
    "(then a splintering noise)"
    "You feel the world tilt. The block slams into the shallow, and the water finds a new route through the seams. Mud and municipal pride sluice away together. Someone on the quay swears in a language"
    "older than the town, and then the crowd turns from anxious to accusatory with the speed of flame finding dry brush."

    "An older man you know from the bazaar shoves past, voice raw" "You promised protection—what kind of protection is this?"
    "Sora Lin fights to be practical, hands moving as if to sew the sky shut with rope. Mateo Hale's face hardens, a map of responsibility and failure. You can hear the shift in the air: tiredness mutating into doubt."
    hide mateo_hale
    show sora_lin at left:
        zoom 0.7

    sora_lin "You planned for this. We told you to sequence the living barriers first so root systems would hold when the blocks shifted."
    hide aria_navarro
    show mateo_hale at right:
        zoom 0.7

    mateo_hale "And we told you that without structural anchors the plants will wash out. We used both—"

    sora_lin "We used both as words!"
    "The exchange has sharp edges. Each counterpoint is not merely tactic but identity—what you believe counts as care for the town. You feel the old ache of being the middle—responsible and blamed."
    "You find yourself answering the crowd now. Your voice is small against the machinery."
    hide jun_park
    show aria_navarro at center:
        zoom 0.7

    aria_navarro "We tried to build a way that held both. I—"
    "(your throat clamps)"

    aria_navarro "I didn't foresee that the splice would fail like that."

    mateo_hale "You couldn't foresee everything, Aria. None of us could. But we can fix it."
    "His fix sounds like a vow. To you, it sounds like denial."
    hide sora_lin
    show jun_park at left:
        zoom 0.7

    jun_park "Patch is in place! We can divert flow, but we need more hands behind the berm—people to haul the gabions."

    "Elena (arrives with a soaked coat)" "I'll get folks. I'll get them to sing if I have to. But Aria—' (her voice is gentle) 'Are you holding up?"
    "You want to tell her you are fine because saying otherwise would cascade into pity or panic. Instead you tell her the practical truth:"

    aria_navarro "I'm trying."

    menu:
        "Admit publicly that the hybrid approach failed and promise a full review":
            "You step onto a crate and force your voice past the salt in your throat. The admission draws a raw sound from the crowd—some anger, some relief—and a few faces close in, searching for direction. It's dangerous honesty, but it moves the air."
        "Double down—outline the technical fixes and order more aggressive repairs":
            "You speak fast about load redistribution and emergency anchors, your words a web of numbers and timelines. It rallies the engineers; it alienates the volunteers. People nod—or they do not—and the gulf subtly widens."

    # --- merge ---
    "Continue to the next sequence"
    # [Scene: Old Quay | Late Evening — After the Surge]
    hide mateo_hale
    hide aria_navarro
    hide jun_park

    scene bg ch13_4001e7_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Muffled conversations, the distant clatter of repairs, a gull complaining as if to remind everyone of the sea]
    # play music "music_placeholder"  # [Music: Sparse piano, slow intervals between notes]
    "By the time the immediate crisis stabilizes—by which you mean certain leaks are staunched and someone has counted on fingers where people slept in cars—fatigue smells like mildew on everyone. You and Sora sit on a"
    "low crate beneath a string of green lanterns that buzz like captive insects. Mateo stands a short distance away, talking quietly into a handheld radio, jaw set."
    "Elena joins you, hands still smelling of fish and salt, and drops a thermos into your lap. The heat fogs up the metal rim and you inhale the sharp sweet of tea as if it were a small rescue."
    show elena_navarro at left:
        zoom 0.7

    elena_navarro "You should have asked for rest sooner,' she says without accusation. 'Controls need an honest hand."
    show aria_navarro at right:
        zoom 0.7

    aria_navarro "And if the honest hand is clumsy? If the honest hand breaks a thing we could have fixed?"

    elena_navarro "Then you fix it again. You can't keep catching everything, niña. People need to know how to catch for themselves."
    "Her words are both balm and reprimand. They land with a firmness that makes you straighten."
    "Jun flops down across from you, boots still muddy. They pull a battered pack from between their knees and hand you an improvised map of the town with marks in messy pen."
    show jun_park at center:
        zoom 0.7

    jun_park "We lost sensors at sector five, but not all. I can make a patch network, cheap and dirty. It'll give us eyes while we rebuild."

    aria_navarro "How long?"

    jun_park "Two days with help. Four without. But it's doable."
    "They look to you with that unspoken question: will you ask for help, or will you try to shoulder it alone?"
    "Across the quay, Mateo Hale and Sora Lin meet briefly. Their conversation is quiet, then tenses, then softens—but you can't hear the words. Their faces are open to the rain and to each other in ways"
    "that make something raw and aching in your chest: the knowledge that repair will ask more than scaffolds; it will ask humility, trade-offs, and maybe, in the quiet places, personal reparations."
    "You stare at the map in Jun's hands and see not only infrastructure but a tangle of loyalties and resentments—who trusts whom, who will follow which leader, who will walk away. The effort that began as a hybrid plan is fraying into multiple small futures."
    hide elena_navarro
    show sora_lin at left:
        zoom 0.7

    sora_lin "Aria, we need to fix this in a way that doesn't make people feel like they were sidelined. If we don't, they'll never trust the plan again—even if the walls hold."

    "Mateo Hale (from across the quay)" "And we need efficiency. We need expertise and decisive action so homes don't get flooded while we debate democracy in the mud."
    "Their words are not opposites but two sides of the same coin. You feel the coin's sharp edge against your palm."

    aria_navarro "If I call in outside help, we might fix things faster—but I risk the community's agency. If I try to rebuild a council now, it could restore trust but cost precious time. If I step back, I might heal relationships but lose authoritative control over operations. I am small in the shadow of the sea, and every choice feels like a theft from someone else."
    "Your chest tightens. The rain has softened to a steady sheet that blurs the edges of the quay; lanterns reflect like wounded stars. Fatigue hums under your skin; guilt settles like a weight in your pockets."
    "Elena squeezes your hand once. It is the only anchor you have tonight."
    "You know a decision needs to be made—and soon. People are hungry for direction, for admission, for a plan that tastes like fairness. You can feel the town holding its breath, waiting to see whether you'll bend toward external expertise, local reform, or personal sacrifice."
    # play music "music_placeholder"  # [Music: Drop to a single, unresolved piano chord]
    hide aria_navarro
    hide jun_park
    hide sora_lin

    scene bg ch13_4001e7_4 at full_bg

    menu:
        "Call for external regional specialists to advise and temporarily co-manage recovery.":
            jump chapter17
        "Reform the council on the spot—clear roles, rotational leadership, and binding emergency protocols.":
            jump chapter19
        "Step back from leadership to rebuild relationships—let Sora or Mateo lead operational recovery while you rebuild trust.":
            jump chapter19
    return
