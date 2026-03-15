label chapter2:

    # [Scene: Maris Bay Research Greenhouse | Late Afternoon]

    scene bg ch2_c4ca42_1 at full_bg
    # play music "music_placeholder"  # [Music: Soft, hopeful piano with distant marine wind motifs]
    "You step back inside the greenhouse the way you step into an old room that still knows you—the glass remembers the prints of your hands, the bench where you once propped your notebook. The air is"
    "humid and close; it tastes of wet earth and salt, and when you breathe it in you can feel the remainder of the van's diesel on the back of your tongue like a faint promise of"
    "movement."
    "Your notebook lies open on the worktable, the last line from the night before—Bridge. Listen. Protect.—still soft with ink. You close your fingers around the spine for a moment, like testing whether a vow is a stitch or a rope. It feels both."
    # play sound "sfx_placeholder"  # [Sound: Tiny drip from a condensation gutter. A distant gull cries once.]
    "Dr. Lian bends over a bank of sensor modules, her short-cropped hair bobbing as she talks. Her voice has that quick, practical rhythm that maps ideas into tasks."
    show dr_lian_obasi at left:
        zoom 0.7

    dr_lian_obasi "If we array the salt sensors on three transects—boardwalk, mid-marsh, and outer breakwater—we can get hourly flux data. That'll tell us whether planted eelgrass is dampening wave energy or just getting drowned."
    show marin_sol at right:
        zoom 0.7

    marin_sol "And the algal tanks? Will they integrate with the sensors, or do we need a dedicated feed?"

    dr_lian_obasi "We can stream the algae bioluminescence as an early indicator—stress sensors first, then hydraulic models. Low energy draw. Mostly off-grid.' (She taps the slate with a fingertip.) 'You'd need volunteers for the weekly calibrations, though. It's fiddly, but people like fiddly when it gives them a role."
    "You watch her hands while she explains—quick gestures that make scaffolds of meaning. You sketch a rough timeline across the page: pilot plots near the Boardwalk Floodplain this autumn; winter nursery expansions in the greenhouse; dune planting next spring. Your handwriting is tidy where focus has room to be deliberate."

    menu:
        "Pass Dr. Lian the sketch":
            "You slide the page toward her. She leans in, tracing a line with a boot-scarred finger and eyes lighting. 'This could scale,' she says, already seeing volunteers slot into the calendar."
        "Keep it private for now":
            "You fold the page under your hand and smile tightly. Lian squints at you, then nods. 'We'll show the pilot to the co-op when it's ready,' she says as if reading the hesitation, and you feel the weight of stewardship again."

    # --- merge ---
    "You tidy a damp leaf from the edge of your page and look up as the greenhouse door sighs open. The door brings in salt spray and a shape in oilskin: Kaito, rope slung over one shoulder, the carved whale talisman catching the light against his sweater."
    show kaito_navarro at center:
        zoom 0.7

    kaito_navarro "Marin."

    kaito_navarro "You're here early. The pier sent a message—Aria's team is set up for a staged run. Cameras and comps, the whole postcard.' (He rubs at his palms.) 'Will this... marsh and breakwater stuff block launches? The coop's worried we won't get boats out when we need 'em."
    "You take a breath. You never want to minimize that worry—boats are lifelines here, and Kaito's voice carries both protective heat and a careful softness."

    marin_sol "No. The idea is cooperative—living breakwaters offset wave energy and channel current, not gate it off. We'll prioritize launch corridors, tie marsh planting to scheduled pier maintenance, and train brigades to clear paths in storm windows."

    kaito_navarro "And that little corridor will actually hold in a big surge? TideLine's seawall shows numbers—'X meters head reduction'—that's convincing to folks who read headlines."

    dr_lian_obasi "Models and headlines aren't the same thing. Living systems take time. They also live with the sea; they recover, they adapt. Our sensors will measure—real feedback. Not just a press release."
    "Kaito Navarro studies you, the rope slack in his hand. His hazel eyes fold into a question that is half private—the carved whale talisman resting against his hip a steady counterweight."

    kaito_navarro "You think the town can wait for a system that grows? People are tired."

    marin_sol "They're tired because they've had to carry so much already. If we give them something they own, they'll keep it. If we hand them a wall that closes access, we take something else away."
    "There is a softness in Kaito's shoulders that eases when you speak in that particular, careful way—science braided to neighborhood memory. You reach instinctively for the talisman and turn it between your fingers for a second,"
    "feeling the grain of the wood and the history inside it. A small contact—no decision—only a pause."

    menu:
        "Touch the talisman":
            "Your fingers close on the whale, and Kaito's mouth twitches like he's remembering a story he won't say aloud. 'My grandfather carved that,' he says after a beat. 'Said it keeps you pointing out.' You nod and feel steadier."
        "Keep your hands on the notebook":
            "You fold your hands over the ink, keeping the plan between you and the page. Kaito watches for a moment, then exhales, the sound like a tide pulling back. 'Alright,' he says. 'Just—don't let us lose the pier.'"

    # --- merge ---
    "The greenhouse door breathes again; Old Tomas moves in with a slow, careful gait, hands folded into the sleeves of his knitted cap. He smells like smoked fish and rain. He carries the kind of silence that is full of stories."
    hide dr_lian_obasi
    show old_tomas at left:
        zoom 0.7

    old_tomas "You youngsters think in maps and graphs. Back when my knees were straighter, the eelgrass ran from here all the way to the second spit. You could see it in the water like a green carpet. Boats slid easier; crabs had homes. Storms didn't eat like they do now."

    marin_sol "What changed first? The storms? The trawlers? Or the sea itself?"

    "Old Tomas (eyes turning inward, remembering)" "All of it. The sea learned new habits. We learned the hard way. But you listen—good thing.' (He pats the bench.) 'If you put the grass back in the right places, it remembers how to keep the mud. It needs people, though. You can't plant eelgrass and walk away."
    "Rosa, who has been sorting seedlings at the far bench, looks up and pushes a tuft of wet hair behind her ear."
    hide marin_sol
    show rosa_sol at right:
        zoom 0.7

    rosa_sol "Tomas is right. We can plant, but people need to learn the care. We need crews, schedules, someone who'll show up in the cold."
    "You look from Tomas to Rosa to Lian: each face is a node in the network you are trying to build. It's not one model; it's many hands and one long patience."
    hide kaito_navarro
    show dr_lian_obasi at center:
        zoom 0.7

    dr_lian_obasi "Funding is patchwork. Mayor Ana's on board until the budget hearing; she'll want numbers and short-term wins. We write the pilot grant to show a clear, accountable deliverable: thirty meters of planted breakwater paired with measured launch corridors."
    hide old_tomas
    show mayor_ana_beltran at left:
        zoom 0.7

    mayor_ana_beltran "Limited budgets. Limited time. Show me the numbers, Marin. Show me the people who will do the work. If TideLine brings a fund and a fast job, we need to know why we choose differently."
    "You feel the practical pressure in that voice, but also a threaded trust—she puts her weight behind what she believes will hold the town together. The mayor's urgency is not panic; it's a request for pragmatic hope."

    menu:
        "Read the mayor your grant outline now":
            "You clear your throat and call up the pilot timeline. Mayor Ana listens, asks two precise questions about volunteer retention. You answer. There's relief in her 'good'—a small, warm thing that feels like a vote."
        "Wait to formalize until you've run the sensor arrays":
            "You tell the mayor you'll have initial sensor feeds before the hearing. She agrees, but you hear the vibration of a calendar closing in your chest. It will mean more late nights."

    # --- merge ---
    "Outside, through the glass, the pier stitches the town to the sea. You can see the edge of TideLine's modular prototypes—gleaming, segmented platforms—neat rectangles against the churning gray. A staged photo-op has been set up: a"
    "polished banner, a small cluster of press, and—one woman who stands apart in a way that reads like a signature."
    "Aria Chen: (in the photo) Her bob cuts the light like a ruler; in the photo she is framed with hands on hip, a blueprint in one hand, the other extended as if offering certainty. Her"
    "suit's piping catches the wet glow of the pier lights; she is all sleek lines and efficient promise."
    "You: (internal) The prototypes are clean and fast. They hum with a promise of measurable protection. They also hum with the kind of power that wants tidy answers."
    "Rosa walks to the window and presses her palm to the glass, watching Aria position herself for the camera. There is an ugliness in the shine, but also a clarity—people like clarity when they're frightened."

    rosa_sol "She's everywhere. The brochure said 'scalable resilience.' What does that mean for us? Does it mean we sign something and the pier is theirs?"
    hide rosa_sol
    show marin_sol at right:
        zoom 0.7

    marin_sol "Not if we make it clear early. The grant application not only asks for funding for pilot planting; it ties a co-op clause to maintenance—training, shared access, a community board that signs off on any structural change."
    "Kaito Navarro folds the rope into a loose coil and sets it down carefully, like laying out a small promise. The room feels full but practiced—plans settling into their places."

    dr_lian_obasi "If we pilot this in the Boardwalk Floodplain, the data will speak for itself. TideLine's numbers are attractive, but they're models on someone else's shore. We can show what living systems do here."
    "Old Tomas chuckles softly, a sound like old rope on a winch."
    hide dr_lian_obasi
    show old_tomas at center:
        zoom 0.7

    old_tomas "You think science is clean. It's not. It's patient. It settles. Sometimes that's what we need."
    "You make one more sketch: marsh planting beds placed to deflect current into natural corridors, a diagram of volunteer brigades rotating maintenance, a note for the pilot grant's measurable outcomes. You promise Dr. Lian and Rosa—out"
    "loud and in a voice that steadies you—that you'll work to make space for everyone, that you'll find a way for access and habitat to breathe together."
    hide mayor_ana_beltran
    show rosa_sol at left:
        zoom 0.7

    rosa_sol "Then write it big. Make us see how it doesn't close the water off."
    "You grin, a small upturn that feels like sunlight through storm-clouds."

    marin_sol "The tug of responsibility sits warm and manageable under your ribs. It's not easy, but it is clearer now: this is how you build a different kind of protection—one that remembers people's lives as part of the coastline."
    "You turn the page and, with the slow certainty of someone learning to keep time differently, write the words again: Bridge. Listen. Protect."
    hide marin_sol
    hide old_tomas
    hide rosa_sol

    scene bg ch2_c4ca42_2 at full_bg
    # play music "music_placeholder"  # [Music: Piano softens to a single held note]
    "Page-Turn Moment: The glass between you and the pier is thin. On this side, plans and people and algae light; on the other, polished promises and a photograph ready to travel. You understand the cost of"
    "haste and the labor of repair in the same breath. You stand with mud on your knees and a map in your hand, and you can feel how slow projects fold into a town's long life."
    "The choice waits—still not resolved—and that waiting is a kind of pressure: not frantic, but necessary. You inhale, and the greenhouse holds you like a promise."

    scene bg ch2_c4ca42_3 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
