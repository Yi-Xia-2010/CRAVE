label chapter1:

    # [Scene: Havenport Boardwalk | Dawn]

    scene bg ch1_Start_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Gull calls, a far creak of rigging, the slow slap of water against pilings. A low diesel hum—generators from recent repairs—flickers beneath the gullsong.]
    # play music "music_placeholder"  # [Music: Sparse piano with a slow, minor progression; low strings swell softly beneath.]
    "You press the brass compass pendant to your sternum. The metal is warm from your skin and oddly steady under your ribs, as if it answers a question you haven't entirely formed yet."
    "The tide is doing what it always does and no longer promises the same things. It erases footprints in a minute and leaves new ones in the places you never meant to walk. You watch it"
    "draw and smudge the town's edges — the rope lines, the bolts on old pilings, the breakwater stanchions — as if trying to rewrite where Havenport begins and ends."
    "Your hands still smell of salt and old rope. The knuckles are browned and puckered from sun and storms; they remember the weight of nets, the rhythm of hammering, the slow certainty of repeated repairs. You"
    "run your fingers through dark, seaweed-brown hair, twist the messy ponytail, and feel the sun-burnished patch on your palm as if it were a map to the parts you can't fix with diagrams."
    "You inventory everything that could be the starting place for something different: Greenwave's volunteer crew waking up in a dozen houses; the field notebook you keep pressed with leaves and errant sketches of living seawalls; the"
    "small satellite of colleagues at the Coastal Research Hub who can run models but not mend hearts; Elder Tomas's warnings like a half-remembered tide song in the back of your head; the envelope from Tideguard still"
    "unopened on your table; and Cassian Rhee's voice—slick, measured—already threaded through the town like a current you didn't ask for."
    "Ivy Morales appears before your senses have even tagged her presence properly: the quick clip of her boots on the planks, a neon vest bobbing like a buoy. She hands you a thermos without ceremony, her grin narrower than usual."
    show ivy_morales at left:
        zoom 0.7

    ivy_morales "You look like you pulled the tide into your chest and forgot to breathe. Coffee?"
    show marin_sato at right:
        zoom 0.7

    marin_sato "Please. Strong enough to stand up to Cassian's lullaby."

    ivy_morales "Always the right order of business. Did you sleep at all?"
    "Marin Sato: (You flip the cap, sip. It's sharp against the cold.) 'Not really. I was up sketching the nursery layout again. Kelp needs a different anchoring pattern if we want it to survive the storm surge models.'"

    ivy_morales "That's the thing — you think about the plants like they're people you owe something to. I like that. But the town's talking. Tideguard's feelers are circling the marina, Lina already sniffed out a promotional op, and—"
    "(she hesitates, voice softens)"

    ivy_morales "—Cassian's been in the papers. People want a plan that looks finished."
    "You let the thermos heat your fingers and the words sit. Finished plans are tidy. Grassroots ones are messy and honest. You can almost taste the difference in the air: soldered optimism versus the salt of long labor."

    menu:
        "Smile, deflect the worry":
            "You tip your chin. 'Let them sniff. We'll give them something to cover in their headlines that actually helps.' Ivy's eyebrows lift. She presses the thermos back into your hands like it's an anchor."
        "Admit fatigue":
            "You drop your shoulders. 'I'm tired of patchwork, Ivy. I keep sewing and something else rips.' She nods, fast and sympathetic, and for a moment the sun seems to nearly rise in the space between your words."

    # --- merge ---
    "The conversation continues as morning moves on."
    "Ivy tugs off her vest and slings it around her waist with a practiced motion, scanning the harbor toward the Tideguard Pavilion, which sits too clean against the skyline."

    ivy_morales "You thinking of calling people? A meeting, like old times?"

    marin_sato "I am. The council needs to hear the models; Greenwave needs volunteers; the Hub needs to be in the room. And Cassian—"
    "(the name sticks like a splinter)"

    marin_sato "—Tideguard's envelope can wait. I want the town's voice first."

    ivy_morales "Good. You'll need Elder Tomas in the room. If he gets up and speaks, folks will listen."
    "She nods toward the far end of the boardwalk where an old figure stands with the gait of someone who has threaded the coastline his whole life."
    hide ivy_morales
    hide marin_sato

    scene bg ch1_Start_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The scrape of a wooden stick, the whisper of a net being adjusted somewhere behind him.]
    show elder_tomas_hale at left:
        zoom 0.7

    elder_tomas_hale "Morning, Marin."
    "(He says the name as if testing its edges; his voice is sandpaper and salt.)"
    show marin_sato at right:
        zoom 0.7

    marin_sato "Morning, Tomas."
    "(Your hands tighten around the thermos. His presence brings memories you didn't know you needed: the smell of pitch, the scrape of a plane against cedar when you were twelve and eager to learn.)"

    elder_tomas_hale "You look older."
    "(A dry smile. Then his gaze goes to the water, to the horizon, as if measuring something the tide cannot show.) 'You know the old boatmakers used to read the shoreline like scripture. They'd tell you"
    "when a place was tired. Havenport's tired in some ways. But it's stubborn. Stubborn's not bad. Stubborn gets things done.'"

    marin_sato "Stubborn gets things fixed, or stuck."
    "(You admit, and he flinches because he knows the trade.)"

    elder_tomas_hale "Both."
    "(He taps his walking stick once against the boards.) 'Don't bend your stubborn into being the only way. And don't let them coat the harbor with steel if it means forgetting how to live here. There's a balance.'"
    "The warning is the same shape as it always was, but the edges are sharper now. Tomas doesn't wave Cassian away—he doesn't have to. His words hang in the space between boards and tide and your ribs."
    "Lina Park's camera clicks from a distance as she records the morning light across the water. You see her not as an outsider but as someone who can quicken the town's pulse."
    show lina_park at center:
        zoom 0.7

    lina_park "Marin! Ivy! I'm doing a piece today—quick impressions; how are people feeling this morning?"

    marin_sato "Tell them there's work to do. Tell them we've got more questions than answers but the people who know the place must talk first."

    lina_park "Angles matter."
    "(She thumbs through notes.) 'I'll give them the people-first angle. But Marin—'"
    "(she lowers her voice)"

    lina_park "—you should be careful. Tideguard funds can come with strings."

    marin_sato "We know."
    "(You force a smile that doesn't reach your eyes.)"
    "The morning seems to collect itself around these small conversations: a knot of practicalities and old memories, laughter too thin to disguise the tiredness beneath. You fold your field notebook closed in your coat — the pressed leaves crackle faintly — and you think of Ariana."
    "She is not here yet, but you see her clearly anyway: platinum-ash bob, a blue streak, yellow boots bright against the softened palette of the town. You imagine her stepping off a bus or out of"
    "a rental car, a slim tablet clutched to her chest, ideas and tendency toward optimism radiating like heat. The thought should set something lighter in you—hope is supposed to behave that way—but instead the hope arrives"
    "as a fragile shell, thin as a crab's carapace."
    "You think of the envelope on your table. You haven't opened it, because some things should be paid attention to in a room with witnesses, and because opening it alone feels like consenting to a narrative that may not include the people who built this place."
    "You breathe in the scent of damp cedar and diesel and the faint tang of new kelp that Greenwave volunteers hauled last night for a pre-trial run. The smell anchors you. You remap your obligations like"
    "knots on a rope in your head: the meeting, the volunteer roster, the materials list, the need to speak plainly at the council, Tomas's admonition not to let the harbor be turned into a fortress."
    "Ivy leans against a piling and watches you, eyes patient and small."
    hide elder_tomas_hale
    show ivy_morales at left:
        zoom 0.7

    ivy_morales "If you call this meeting, we'll do it the way you want. Grassroots at the front, scientists and reporters as witnesses, council in the middle. We can ask Lina to run the piece with community voices. Tomas'll speak. Folks will come if you put the word out."

    marin_sato "That's the plan."
    "(Your voice is steadier than you feel. The compass at your throat is oddly heavy as if the brass contains some weight that isn't just metal.)"

    ivy_morales "You okay, though? Really?"
    "(You close your eyes for a second and let the gulls' calls lace through the space where your certainty falters.)"

    marin_sato "I don't know if the town wants what I want, Ivy. I don't know if living seawalls and kelp rows will satisfy a market that prefers a seawall of concrete with Tideguard's name on it. I'm tired of sticking bandages on holes that keep getting bigger."
    "Ivy's jaw tightens. She reaches, unexpectedly, and squeezes your forearm — not patronizing, not flirtatious, simply human. The touch is quick and firm, like a line thrown to steady something in surf."

    menu:
        "Recite Tomas's warning aloud":
            "You repeat Tomas's words: 'Don't let them coat the harbor with steel if it means forgetting how to live here.' Saying it aloud makes it less a private fear and more a question to be answered. Ivy's nod is slow and solemn."
        "Push the thought down, focus on logistics":
            "You count off the meeting tasks: volunteers, list of stakeholders, a timeline. The rhythm steadies you. Ivy helps by pulling her tablet out and tapping open the volunteer schedule."
        "Think about Ariana and let hope fray into resolve":
            "You picture Ariana's bright boots stepping onto wet planks, and the image hardens into something actionable rather than comforting. You say, 'We'll bring the models; we'll bring the stories.' Ivy breathes out like someone letting a sail catch wind."

    # --- merge ---
    "The group's resolve consolidates and the plan to call the meeting takes shape."
    "The wind picks up. A gull drops close to the pilings and then wheels away. The sky bruise-light is thick with the promise of weather—nothing dramatic yet, but the kind of atmospheric pressure that makes flags limp and people consider whether to tie down things that might fly."
    "Your decision settles like a stone into the bottom of your chest: call the meeting. The shape of the morning narrows until the to-do list is the only path forward. But you can feel the low"
    "undercurrent — the knowledge that meetings can change things or lubricate the way for decisions you do not control. You taste the ache of all those small sacrifices you've made, the missed dinners, the nights spent"
    "drafting proposals until your eyes blazed, and the quiet places where you told yourself it was fine because someone else would pick up the rest."
    "Elder Tomas taps his stick, the sound a single punctuation on the boardwalk."
    hide marin_sato
    show elder_tomas_hale at right:
        zoom 0.7

    elder_tomas_hale "Make sure it's not just the people with loud voices. Make sure the ones who would be pushed out are the first you call. That's how you keep a town, Marin. You don't patch over it and call it stable."
    hide lina_park
    show marin_sato at center:
        zoom 0.7

    marin_sato "I won't forget."
    "You feel the meeting like a door you will open. You can already see the room in your head: the Greenwave banners folded against the wall, a scatter of datasheets from the Hub, Lina's notebook open"
    "to a middle page where she will write the town's sentence. You imagine the council members' faces, the skepticism, the old men who've fished these waters their whole lives. You picture Cassian Rhee's suit entering the"
    "room later, some polished solution in his hands, and the way his smooth words will try to simplify your stubbornness into an obstacle to be removed."
    "The compass at your throat is a small, private oracle. You turn it over in your fingers, read the scuffs like a language. It doesn't tell you the right answer—only that you have a direction and have to walk."
    "You reach into your pocket for your phone. Your thumb hovers over the contacts list, the names that will fill the room. The day waits, the tide waits, and the boardwalk creaks like an old lung filling."
    "You close your eyes for a moment and imagine the meeting beginning: voices, arguments, cries, laughter, the thin light of resolve. You're not pretending this will be easy. You are bracing for erosion and for repair, both."
    hide ivy_morales
    hide elder_tomas_hale
    hide marin_sato

    scene bg ch1_Start_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The wind lifts; a distant foghorn answers.]
    "You draw in a long, measured breath. Then you press your thumb to the screen."
    # play music "music_placeholder"  # [Music: The piano chord lingers, unresolved; strings hold a low, melancholic note.]
    "You are about to call the people who will decide the shape of Havenport's next storm."

    scene bg ch1_Start_4 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter2
    return
