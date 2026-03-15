label chapter8:

    # [Scene: Mangrove Reclamation Site | Dawn — Two Weeks After the Vote]

    scene bg ch7_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low conversation, the soft rasp of boots in mud, a gull calling, distant engines idling on the quay.]
    # play music "music_placeholder"  # [Music: Sparse, low piano with filtered synth—melancholic but steady]
    "Narration:"
    "You remember the first morning like an afterimage—hands raw from peat, laughter slipping over the water, Sora painting protest banners with sapling leaves as stencils. There was a ceremonial clapping when the hundredth mangrove went in,"
    "as if the earth itself had been invited back to the table. People who'd never dug a hole in their lives came with gloves on and eyes that shone. The tide felt like an ally then;"
    "even the gulls seemed to watch, curious."
    "You smell wet soil and citrus from Elena's packed sandwiches. The taste of salt and coffee is constant at the edges of everything. Your notebook, water-streaked at the corners, sits heavy with measurements and small sketches"
    "of root systems. You run a thumb over your diver's watch—its barometer reads calm—and allow yourself the small, private permission to feel hopeful."
    show sora_lin at left:
        zoom 0.7

    sora_lin "Numbers are good, but songs are louder. We'll paint the stakes with names. People remember names longer than graphs."
    "Narration:"
    "Sora stands knee-deep in mud a few meters down, hands smeared with green and brown. They hum while pushing each sapling in, humming a cadence you think they made up on the spot. Their expression is"
    "complex—hope braided with the tightness of someone who knows loss by habit but refuses to be shaped by it. You don't press them for what that complexity means; it's enough that they are here."
    "Elena catches your eye and gives the half-wink she always does—one that says keep going, niña—without the weight of explanation."

    "Jun tinkers at the edge of the line, checking a string of low-cost moisture sensors clamped to bamboo stakes. He looks up as you approach and grins, small, guilty" "They actually stayed upright overnight. Technology and ceremony, huh?"
    "You laugh—an honest sound—and the day stretches open."
    show aria_navarro at right:
        zoom 0.7

    aria_navarro "Let's make sure the root collars are below tide reach this time. We did this last bed shallower than the paper says—less compaction. If we do a staggered planting depth along the contour, they'll anchor better."
    show jun_park at center:
        zoom 0.7

    jun_park "I'll rebias the water sensors to record the surge peaks. If we get a clear tide log, Kavir can show the council. Numbers make people less nervous."
    "Narration:"
    "You say nothing for a beat, because it's true in a way that still hurts: names, hands, songs—this is how memory becomes obligation."

    menu:
        "Help Sora paint stakes":
            "You take a stake and let paint smear under your nails. Sora hums louder and you both laugh, the laugh of people refusing to be small."
        "Walk the line with Jun and check sensors":
            "You crouch with Jun, fingers cold, reading tiny LED blips. He nudges the red wire back into place and says it will hold—practical reassurance that smells faintly of solder and optimism."

    # --- merge ---

    "The day folds into a steady rhythm. You coordinate, joke, record, and plant. Mayor Cortez stops by with a thermos and a curt, thin smile—the kind she uses when she wants to be close but must remain a certain distance. She lays a hand briefly on Elena's shoulder and says quietly to you, Aria" "Good work."
    "Narration:"
    "At dusk, the site feels like a promise kept. Rows of young mangroves bend into the dying light like an audience bowing after a show."
    # [Scene: Old Quay | Night]
    hide sora_lin
    hide aria_navarro
    hide jun_park

    scene bg ch7_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind picking up, the low rumble of a distant motor, conversation quieter now.]
    # play music "music_placeholder"  # [Music: Minor string swell—the mood deepening toward something unsettled]
    "Narration:"
    "Three nights later, you are at the quay rechecking sensor data when the tide turns on you. The weather apps say a routine king tide; the lab's models say two meters above mean. You have seen"
    "king tides before. You have not, until this night, seen one with the ocean's teeth bared like this."
    "The first sign is sound: a sudden, wrong wind that pushes along the harbor like a hand. The water edge that had been a thoughtful distance from the young roots slips forward in a bright, angry"
    "line. A frothed surge—higher than forecasted—rips into the planting beds. You can feel it in your teeth."
    # play sound "sfx_placeholder"  # [Sound: A sharp crack of something giving, a collective gasp, the slap of water on wooden piles]
    show jun_park at left:
        zoom 0.7

    jun_park "Aria—look!"
    "Narration:"
    "You run. Mud sucks at your boots. Your hands go for the stakes, for the saplings, for anything that might keep a root in the ground. You find Sora Lin at the front line, hands thrown"
    "forward like a ritual net. They shout something—part instruction, part mantra—but the water is faster. The first row of saplings tips, clutches of them uprooted and carried off like bread crusts."
    "You see bodies—neighbors and volunteers—racing along the line, torches waving, calling to each other. You see Elena's hand flatten against her face, fingers gone white. The smell, immediate and cutting, is not just salt: it's the sharp metallic tang that always follows something broken."
    show sora_lin at right:
        zoom 0.7

    sora_lin "Hold the line! Tie 'em down! Names—call the names!"
    "Narration:"
    "You act on muscle memory. You tie, wedge, push. One sapling you had planted yourself snaps free and, for a reckless second, you imagine following it into the water—following a small, grieving thing all the way out to sea."

    menu:
        "Run to haul the uprooted saplings back":
            "You charge into the shallows, cold pushing through your socks. You manage to salvage a few but they are water-logged and limp, roots fouled with tape and sand. Each returned plant is a bruise."
        "Help coordinate the line—organize people to secure remaining beds":
            "You yell, point, pull elbows. People respond; ropes go up between posts and volunteers brace. It's ugly, improvisational engineering. Not perfect, but it buys time."

    menu:
        "Tell Jun and Sora to draft a revised planting protocol tonight—double down on restoration":
            "You stand, voice steady despite your chest. Jun nods and gets to work on tidal models; Sora claps you on the shoulder and already begins to sketch a faster training plan for volunteers. There's exhaustion on every face, but also the brittle gleam of renewed purpose."
        "Ask Mayor Cortez to authorize temporary, municipal levees while restoration regrows":
            "You breathe out and call for the mayor. Her face goes taut, then pragmatic. She agrees to explore temporary levees—her voice is careful, apologetic to some, relieved to others. The word 'compromise' hangs heavy, like a bridge that might or might not hold."

    menu:
        "Advocate doubling down on restoration—redouble volunteer mobilization, improve planting techniques, and ask for time.":
            jump chapter9
        "Compromise with municipal engineers to build temporary levees while restoration regrows—accept outside help.":
            jump chapter11
        "Organize a large, visible cultural action to reclaim public trust and force Mayor Cortez to guarantee funds for a slow, local plan.":
            jump chapter11
    return
