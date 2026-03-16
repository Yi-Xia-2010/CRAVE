label chapter4:

    # [Scene: Rooftop Greenhouse Lab | Dawn]

    scene bg ch4_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Soft percussion with light strings — steady, purposeful]
    "You wake before your alarm, the decision still warm behind your sternum like an ember. From the meeting last night you carried a single instruction into the quiet: get people into the mud. You pull on"
    "your olive jacket, feel the familiar scuff at the elbow, and tuck the thermos into your palm as if it anchors you to the plan."
    "The greenhouse is humid and smelling of peat and wet soil, each breath tasting of possibility. Amaya is already moving among the trays, her grin a quick sun through the glass."
    show amaya_chen at left:
        zoom 0.7

    amaya_chen "There you are. Good—two extra hands for the oyster lattices. Lito's doing the shoreline posts, and Rowan's taken the third transect. Elias Stone texted he'll be here 'in boots,' whatever that means."

    "You" "Elias in boots is better than Elias in a speech. How's the labeling?"

    amaya_chen "Legible. Mostly. I bribed Mrs. Calderón with extra seedlings to oversee the tags. She takes her labeling like a hymn."
    "You let out a small breath, letting some of the night's tension untangle from your shoulders. The seed trays are rows of tiny green fists—saltmarsh grasses, sedges, plugs of cordgrass—each one a small, deliberate promise. You"
    "slot the reclaimed netting into place and start bundling seedlings, hands moving by habit and memory."
    hide amaya_chen

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low hum of the greenhouse vents, distant gull calls]
    show professor_rowan_hale at left:
        zoom 0.7

    professor_rowan_hale "We're expecting a modest accretion this month if those oysters take. Plant the lattices at the outer break; they'll slow current enough to let sediment settle. Keep the posts shallow—no need to scar the mud."
    "You glance at Rowan. He measures like he prays — slow, deliberate. His hands carry the smell of mud and old books."

    "You" "Shallow. Check. We'll stagger the lattices in two rows. Amaya, can you radio the boardwalk crew? Tell them to meet at the south inlet by first light."
    show amaya_chen at right:
        zoom 0.7

    amaya_chen "On it. And Maya— —don't be all work. Lito brought empanadas. You're allowed one."

    menu:
        "Take the empanada now":
            "You accept it, the warm pastry an immediate smallness of comfort. Lito winks and yanks the box closed before you can reach for a second."
        "Save it for later":
            "You tuck the empanada into your vest pocket like a talisman. It's there when you need a bite between posts; it tastes of salt and neighborhood."

    # --- merge ---
    "The morning continues as the crew organizes and prepares to move out."
    # [Scene: Harbor Boardwalk & Market | Early Morning]
    hide professor_rowan_hale
    hide amaya_chen

    scene bg ch4_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Boards creak underfoot, distant engine coughs, a kettle whistles]
    "You meet the boardwalk crew where the market thins—neighbors with bundled scarves, a kid holding a plastered oyster shell like treasure. Lito is already joking emphatically with half the crew, hands rolling with the same ease he used to fix the old outboard."
    show lito_reyes at left:
        zoom 0.7

    lito_reyes "Maya! You always make a face like that when you lift something heavy. You gonna show me or just glare motivationally?"

    "You" "I glare and direct. That's my specialty."

    lito_reyes "Oh, the community's lost its hero of compassion. Get over here and hammer, stubborn-face."
    "You swap a look with Elias Stone when he steps into view—high-visibility vest draped over a weathered sweater, hair damp at the temple. He carries a small sketchbook whose corners are softened with use. He doesn't"
    "take the makeshift podium Amaya had suggested; instead he folds into the group and laces up his boots."
    show elias_stone at right:
        zoom 0.7

    elias_stone "No podium. Less wind. More mud. I promised I'd get my hands dirty."

    "You" "Good. Keep your sketches—use them to argue with the mayor, not with drill rigs."

    elias_stone "Don't worry. I'll let the mud make its own points. Did Rowan send the transect markers?"
    show professor_rowan_hale at center:
        zoom 0.7

    professor_rowan_hale "Markers are set. Amaya's mapped the crews. We're coordinated. We can move up the west inlet by mid-morning if the tide holds."

    "You" "Alright. Team one on posts, team two on lattices, team three on silt traps. Watch the reeds—where the roots show, we avoid digging. This is repair, not replacement."
    # [Scene: Tidal Fringe Marsh | Mid-Morning]
    hide lito_reyes
    hide elias_stone
    hide professor_rowan_hale

    scene bg ch4_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft slurp of boot soles, reeds whispering, distant call of an eel-grass bird]
    "Your boots sink into the mud with a slow, yielding hush. Each step is a small agreement with the earth. The work is methodical: hammer a post, secure it, weave oyster shell mesh, tuck seedlings in clusters that mimic natural clumping."
    "Lito works beside you, cursing gently at a stubborn post then laughing when it finally gives. His hands are quick and practical, dragging a line straight as a habit."
    show lito_reyes at left:
        zoom 0.7

    lito_reyes "You always start like you're fixing the world alone, you know that? Then you get people to actually show up."

    "You" "Someone's got to start the stubborn part. The rest of us are better at keeping to the rhythm."

    lito_reyes "That beanie's about two stitches from sea-sentience. It's becoming a legend."

    "You" "It's a good luck charm. Also, it keeps my hair out of my face when I'm hammering."
    "Elias Stone kneels across from you, hands already dusk-dark with mud. He hesitates, then looks up, sketchbook half-open. The page shows a rough plan—soft lines that echo the marsh's contours."
    show elias_stone at right:
        zoom 0.7

    elias_stone "We stagger the posts so the water funnels a bit slower here. If we plant these clusters in a ladder pattern, the current will drop velocity and drop sediment. It's simple, and it works with the shape of the land."

    "You" "You think this ladder will hold through the next season?"

    elias_stone "If the oyster lattices take, it will slow enough to make a difference. It's not a wall. It's an invitation for the marsh to do its own work."
    "You meet his gaze. There's a kind of quiet faith in the plan that feels like a hand extended rather than a promise shouted."

    "You" "Then let's invite it. Ready?"

    elias_stone "Ready."
    # play sound "sfx_placeholder"  # [Sound: Hammers, low voices, the steady rhythm of work]
    "Rowan moves between teams, reading small instruments, jotting numbers into a waterproof notebook. When he comes near, he pauses a moment to watch the pattern of your hands."
    show professor_rowan_hale at center:
        zoom 0.7

    professor_rowan_hale "Accretion here is within expectation. Your lattices will change the deposition by measurable amounts in months, not years. That gives us leverage in talks. Keep sampling the cores every ten meters."

    "You" "We will. Keep the numbers coming."

    professor_rowan_hale "I will. And Maya—' (there's a softness in his voice) '—if you need anything, call. Science helps you argue; it doesn't have to decide for you."

    "You" "Thanks, Rowan. I know."

    menu:
        "Ask Elias about the sketches now":
            "You point at the page and ask for clarification. Elias leans in, tracing the ladder pattern with a muddy finger. He speaks slowly, patient; in the time it takes to explain, the plan clarifies and your shoulders ease."
        "Save the sketch discussion for the shelter":
            "You fold your hands back into the work and file the sketches away in your mind. Conversation will wait for warmth and coffee; for now, there's hammering to do. Elias nods, understanding, and keeps his sketches close."

    # --- merge ---
    "The teams continue their work as the morning passes into afternoon."
    "The morning passes in a measured blur—small victories stacked like planks. A woman from two blocks over hums as she plants, a teenager shyly learns to knot oyster twine, and Amaya keeps the crews laughing between"
    "commands. There is the steady narrative of labor: deliberate, communal, practical. You feel the work answering the worry inside you in the only way you know how: by acting."
    # [Scene: Boardwalk Edge | Late Afternoon]
    hide lito_reyes
    hide elias_stone
    hide professor_rowan_hale

    scene bg ch4_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low mechanical hum rises faintly, then grows — an industrial insect chirrup]
    "As daylight thins, an unfamiliar sound threads through the marsh's hum. At first you think it's a ferry, then the hum sharpens into a metallic bite. Bright beams slice the fog beyond the inlet—floodlights, clinical and sudden. In the distance, the silhouettes of heavy machines cut into the low horizon."
    show amaya_chen at left:
        zoom 0.7

    amaya_chen "Damn. Duval's teams are moving faster than the notice."
    "You: A tightness clinks through your chest—older, familiar and unwelcome. Guilt—memory—releases itself like an old scar catching in the cold. But the faces around you don't falter. They lift tools a little straighter."
    "Rowan steps forward with a measured gait. A Duval Rep approaches on the boardwalk, their clipboard an emblem of corporate procedure. Behind them, a pair of security personnel stand like sentries; the machines glow like beetles."

    "Duval Rep" "By order of Duval Reclamation, you are required to cease restoration activities on this shoreline pending review. This property is under permit application with the city. You must evacuate the posted perimeter."

    "You" "We are conducting community restoration on public marshland. We have no intention of obstructing lawful process, but we are not evacuating an entire ecosystem for a permit hearing. We will document, we will consult, and we will stand here."

    "Duval Rep" "Please note that non-compliance may result in enforcement actions. Your cooperation is advised."
    "Elias Stone steps up beside you; his sleeves are rolled and his palms are muddy. He doesn't take a lawyer's stance—he is simply present, shoulder in the line of people who refuse to be dismissed by formality."
    show elias_stone at right:
        zoom 0.7

    elias_stone "There's been little to no public notification of a change to access. The community has a right to stewardship, and we have ongoing documentation from Professor Hale that establishes baseline ecological values here."

    "Duval Rep" "Those discussions are for a hearing. Until then, activities must stop."
    show lito_reyes at center:
        zoom 0.7

    lito_reyes "They came with lights and loud voices. Must make them feel like they own the night."
    "You feel the old guilt flare—years of watching decisions made in towers while saltwater rose—and it tightens your throat, but the shape of your anger is different now: more focused, less resigned. You think of whether"
    "to shout, to march, to call the mayor. Each impulse is a tool; each would shape the day to come."
    hide amaya_chen
    show professor_rowan_hale at left:
        zoom 0.7

    professor_rowan_hale "Record them. Take geo-referenced photos. We don't need to escalate—yet. We need the evidence. We need the timeline."
    hide elias_stone
    show amaya_chen at right:
        zoom 0.7

    amaya_chen "And if they touch a post, we'll have neighbors and cameras. They can't bulldoze an entire community into silence without someone knowing."
    "The floodlights sweep again, casting long, sterile shadows over the reeds. Your hand tightens on your thermos—warmth against the cold—and you look at the tired, resolute faces: people who had already given the morning, the afternoon,"
    "their hands to this place. The ember of hope you felt that morning is still there, small and steady, tempered now with the knowledge of the scale opposing you."
    "You breathe, cataloging options like tools on a belt: document, call the shelter, convene a legal response, rally the neighbors, sleep at the hall and prepare. The night will require choices; the machines on the horizon will demand a response."
    # play music "music_placeholder"  # [Music: The steady percussion swells, then holds — the chapter's emotional high reached, measured and burning steady]
    hide lito_reyes
    hide professor_rowan_hale
    hide amaya_chen

    scene bg ch4_453e40_6 at full_bg
    "You stand on the plank between mud and machine, hands in the dirt and eyes on the lights. The decision to come into the mud this morning was clear; the next step is not. For now,"
    "you do what you know: you gather evidence, organize the people, and keep the marsh's slow work alive in tiny gestures. The night will be long, and the plan for tomorrow will need more than hands"
    "— it will need pressure, testimony, and presence."
    "You look at the shelter sign on the boardwalk, then back at the machines. You imagine the hollow of the town hall, fluorescent lights glaring over map pins. Sleep is necessary, and readiness is mandatory."

    scene bg ch4_453e40_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant mechanical hum; the close murmur of people coordinating quietly]
    "You feel both small and steady—neutral in cause but mobilized in action. There is no victory tonight, only continuation."
    # [Page-Turn: You wrap the thermos tighter, feeling the day's mud under your nails. The shelter will be full of whispers and plans. Dawn will come again and with it Rally at Floodlight Ridge — but first, the night must be organized.]

    scene bg ch4_453e40_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
