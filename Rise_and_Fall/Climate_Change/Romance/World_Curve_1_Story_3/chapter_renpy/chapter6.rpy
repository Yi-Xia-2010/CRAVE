label chapter6:

    # [Scene: Promenade | Morning — Planting Day]

    scene bg ch6_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm strings ripple upward, a steady, hopeful pulse underlaid with community percussion — clapping mallets and distant conch calls.]
    # play sound "sfx_placeholder"  # [Sound: The smear of wet boots on plank, the soft tug of lines, a child's laughter, the sharp snap of a tarp being cinched.]
    "You stand at the soft lip of newly planted marsh, a line of root-mat platforms anchored to engineered pylons like ribs against the tide. Your hydroponic locket is warm in your palm; the braided copper at"
    "your temple feels like a small compass of memory. The air tastes of brine and peat and something sweeter — the smell of turned earth, of work turned into promise."
    show elias_harrow at left:
        zoom 0.7

    elias_harrow "We calibrated the sensors overnight after the last tide. The root mats' settlement is within predicted tolerances, and the wave dissipation model shows—"
    "You watch the crowd tilt toward his words. Beaconworks technicians stand behind him with tools and wet gloves, the cooperative's patchwork flag snapping in the breeze. Lucia Montrose [crisp] lingers near the edge of the assembly,"
    "trench coat immaculate, eyes cataloging structure and people in equal measure. Her distance is political and physical, but there is something in the way she narrows her gaze — not hostile so much as appraising."
    "You feel the memory of the hearing, the roars at the Promenade, the nights with Rani hammering outriggers at dawn. This is the braided work of all of it. Your throat tightens, not from nerves but from the weight of names you want to hold in the open."
    show mara_solenne at right:
        zoom 0.7

    mara_solenne "Today we prove that people and place can be allies — that a living line can give our neighborhoods time, jobs, and dignity. This is a pilot, yes, but it's soil that remembers how to hold a shore."

    elias_harrow "And the data backs that up. If this performs as simulated, we can scale the design with less hard armor and more living margin."
    show lucia_montrose at center:
        zoom 0.7

    lucia_montrose "The simulations were persuasive. I still prefer redundancy, but the hybrid model reduces immediate load on the core seawall plans. It's… promising."
    "Your chest lifts at that word — promising — as if someone has nudged open a door you didn't realize was closed."
    # play sound "sfx_placeholder"  # [Sound: Applause breaks like surf; the technicians exchange relieved looks. Councilor Mateo Qu steps forward with a damp packet of papers in hand.]
    hide elias_harrow
    show councilor_mateo_qu at left:
        zoom 0.7

    councilor_mateo_qu "On behalf of the city, I'm announcing conditional funding for a co-management pilot. We will fund technical secondments and an initial livelihoods training program. Conditions are clear — transparency, reporting, and a shared maintenance schedule."
    hide mara_solenne
    show rani_cho at right:
        zoom 0.7

    rani_cho "Translation: we get tools and money without selling our souls."
    hide lucia_montrose
    show eda_nal at center:
        zoom 0.7

    eda_nal "Old hands teach the tide. New hands learn measurements. We hold the knot together."
    "You look at Elias. He looks back at you — eyes soft, an unspoken lending of steadiness. Around you, people begin to move into tasks: someone lays a tray of seedlings, a Beaconworks tech kneels to"
    "check a sensor, a neighbor opens a thermos and offers you coffee that tastes of burnt sugar and shelter."

    menu:
        "Step up and name the volunteers who did the night work":
            "You call out names—Rani, the late-shift technicians, Eda's crew—and the crowd responds with a cheer that makes the pylons hum. Recognition turns tired faces into radiant ones."
        "Let Elias finish the technical summary first":
            "You fold your hands and listen as Elias details the recalibration. The technical clarity feels like a brace: people nod, journalists scribble, and the plan gains a different kind of gravity."

    # --- merge ---
    "You choose, and whichever small shape your decision takes, the day bends toward building. Volunteers dig with practiced rhythm; the populations of worms and shoots are coaxed into seams with steady fingers. The root-mats settle, tendrils"
    "climbing like curious hands. Children run a careful relay of plugs; an older woman hums an old spit-shanty you don't know the name of but feel in your bones."
    hide councilor_mateo_qu
    show lucia_montrose at left:
        zoom 0.7

    lucia_montrose "You built a convincing demonstration. The mat-integrated pylons—you convinced planners that the loss function isn't binary. There's room for living systems if they're quantifiably effective."
    hide rani_cho
    show mara_solenne at right:
        zoom 0.7

    mara_solenne "We built it together. And we will keep building it together."

    lucia_montrose "Keep making it work. I will make sure the funding pathway remains open if your reporting keeps the math clean. Don't squander the trust this took to earn."
    "There is a small, almost private exchange of respect. It doesn't erase what she stands for, but it refracts it through a new light: pragmatic acknowledgment."
    # [Scene: Rooftop Market & Greenhouse | Late Afternoon — The First Night After Launch]
    hide eda_nal
    hide lucia_montrose
    hide mara_solenne

    scene bg ch6_601bcb_2 at full_bg
    # play music "music_placeholder"  # [Music: Quiet guitar and gentle percussion, a lullaby for a city remade by hands.]
    # play sound "sfx_placeholder"  # [Sound: Rain starting, a soft percussion on tarps; the distant murmur of the Promenade slowly ebbing.]
    "You and Elias climb to the converted rooftop that will be your watch-post and your refuge for the next few nights. The rooftop smells of wet canvas and frying spices; a market vendor stuffs a packet of sticky rice into your hand and winks."
    "You unroll a sleeping mat beside him. He fusses with an array of tiny instruments — a compact meteorological station, a sensor hub cased in resin. Your fingers itch to rearrange the instruments into neater, more efficient patterns, but you stop and instead tuck the hydroponic locket under your shirt."
    show elias_harrow at left:
        zoom 0.7

    elias_harrow "We should set the logging interval to fifteen minutes tonight. The first storm window is predicted in forty-eight hours; we'll want to compare the pre- and post-wave stress on the mats."
    show mara_solenne at right:
        zoom 0.7

    mara_solenne "Fifteen's safe. But not so often that we miss community maintenance cycles. People need rest, too."

    elias_harrow "You have a way of making the machine humane. I like that about you."

    mara_solenne "You like that I make rules for the machines. You secret anarchist."

    elias_harrow "I'm an engineer. I domesticate chaos. You give it meaning."
    "The two of you talk long into the drizzle about planting schedules, about Eda's seed-curation techniques, and about how to teach young apprentices to read tidal memory. You argue, gently and thoroughly — whether sensors should"
    "have open APIs or a simplified readout, whether planting density should favor fast-establishers or diverse assemblages. The argument is not a friction that divides; it's the precise way you parse the world together, testing and tuning"
    "the edges of a shared life."

    menu:
        "Tuck the seedling trays under the tarp first":
            "You lift the trays with reverent care, creating a small, protected nursery. Elias watches you and, in the glow of rooftop lights, reaches out to brush a wet leaf from your hair."
        "Double-check the sensor cluster before sleep":
            "You crouch over the instruments and run diagnostics; the green LEDs blink steady. Elias joins you, and your shoulders touch in the cramped light, the proximity a small agreement to be vigilant together."

    # --- merge ---
    "You fall asleep later with mud in the creases of your boots and Elias' shoulder as a soft cliff against your back. The rooftop hums: solar trickle, distant tide, the stitched breathing of a neighborhood that"
    "has worked for a result. The intimacy between you has shifted; it is now crossed with purpose. You dream lightly of seedlings and long-lived planks that will be here when your hair goes silver."
    # [Scene: Beaconworks Lab | Two Weeks Later — Results & Recognition]
    hide elias_harrow
    hide mara_solenne

    scene bg ch6_601bcb_3 at full_bg
    # play music "music_placeholder"  # [Music: Upright strings and an ascending choir motif — restrained, celebratory.]
    # play sound "sfx_placeholder"  # [Sound: Click of a projector, the soft rustle of paper, a communal exhale as data is revealed.]
    "The first set of post-deployment reports is in: wave height variance reduced; energy absorption gradients favorable; maintenance hours predictable. The root-mats have held seedlings through two moderate tides and one small squall. People who were once skeptical now nod when you use the word 'scalable.'"
    show elias_harrow at left:
        zoom 0.7

    elias_harrow "We reduced peak nearshore pressures by an average of twelve percent in the test window. Early economic modeling indicates that, with supported training programs, we can create durable employment pathways for local stewards."
    show councilor_mateo_qu at right:
        zoom 0.7

    councilor_mateo_qu "I've drafted the ordinance language for conditional co-management recognition. It secures community maintenance rights, a training fund, and a two-year review window tied to reporting standards."
    show rani_cho at center:
        zoom 0.7

    rani_cho "Money that comes with an apprenticeship ladder and not a bulldozer? Sign me up."
    hide elias_harrow
    show eda_nal at left:
        zoom 0.7

    eda_nal "The marsh sings when it's heard."
    "Lucia Montrose lingers in the doorway; this time her posture is less curt, more reflective."
    hide councilor_mateo_qu
    show lucia_montrose at right:
        zoom 0.7

    lucia_montrose "You made this a pilot that city planners can agree to. I don't promise to abandon the seawall plan entirely, but there's space now for integration. That is tenable governance."
    "There's applause that isn't just for data. It's for the knitting together of different logics — of bioengineering and household knowledge, of politics and tending."
    "You find yourself anchored between Elias and the assembled crowd, the locket warm under your palm. The sense of having moved something real is almost dizzying. The Drowned Garden — your neighborhood, your old stomping ground"
    "— already looks different when you pass its alleys: newly stabilized pontoons, seedlings forming curtains against future surf, apprentices learning to splice irrigation lines. Where once you braced against inevitability, now you walk through a place"
    "that makes space for repair."
    "Elias finds your hand across the room and squeezes. There's gratitude in the pressure — for the way you braided stories into policy, for the way you fought and also listened."
    hide rani_cho
    show mara_solenne at center:
        zoom 0.7

    mara_solenne "We didn't just build a model. We built a way to keep building."
    hide eda_nal
    show elias_harrow at left:
        zoom 0.7

    elias_harrow "And we'll keep calibrating. The pilots are not finished poems; they're drafts that turn into standards when people keep reading them."

    "Rani sidles up, elbowing both of you" "So when do we get a plaque?"
    "You laugh, and the sound catches like sunlight on wet glass. You let yourself look ahead with a steadier heart. The pilot will need tending, funding will have stipulations, and not everyone will be satisfied — but the net has been woven, and it is not a fragile thing."

    menu:
        "Thank Lucia publicly for her oversight":
            "You step forward and recognize her contribution in the report, and Lucia's expression softens. The moment is brief but it reframes her as something other than an antagonist in the public eye."
        "Keep the spotlight on the apprentices and volunteers":
            "You lift the volunteers to the foreground—voices, faces, apprentice names. The media focus shifts to local stewards; the story becomes about livelihoods rather than policy alone."
        "Pull Elias aside to discuss next-phase instrumentation quietly":
            "You catch Elias' sleeve and say something low about sensor networks. He listens, then nods; the private plan you share feels like another seam in the day's work, one that is just yours two."

    # --- merge ---
    "You weave those moments into a single braided feeling: community, method, and love stitched together. The pilot has a legal frame now; funding is conditional but present; a training curriculum seeds apprenticeships that will give neighbors"
    "incomes and expertise. Beaconworks commits technical secondments and open-data requirements that mean the design can be inspected and adopted elsewhere. Lucia, pragmatic as ever, pledges corridor-level cooperation — not surrender, but an operational acceptance that will"
    "expand options for other neighborhoods."
    "You think of the practicalities that remain — the two-year review, community governance meetings, the need for sustained attention during heavy tides — and you do not feel despair. You feel responsibility knit to hope."
    # [Scene: Drowned Garden | Early Morning — One Month Later]
    hide lucia_montrose
    hide mara_solenne
    hide elias_harrow

    scene bg ch6_601bcb_4 at full_bg
    # play music "music_placeholder"  # [Music: A single upward swell, then a peaceful lull — the music of a place breathing easier.]
    # play sound "sfx_placeholder"  # [Sound: Low tide, the soft flap of a tarp, a child's small voice counting plants aloud.]
    "You walk the neighborhood with Elias at your side. Your locket swings against your chest; the copper thread feels warm. Children run past, calling out the names of plants. Rani passes you a finished bench and a grin. Eda watches a plot of marsh grass and smiles like a blessing."
    show elias_harrow at left:
        zoom 0.7

    elias_harrow "We did the math, and then we did the dirt. That was my favorite kind of reconciliation."
    show mara_solenne at right:
        zoom 0.7

    mara_solenne "Mine too. There are still fights ahead. But the fight is…different now. Less about being the loudest, more about keeping the work honest."

    elias_harrow "I don't want to engineer distance between us and the places we're trying to save. I want to be beside you in the mud and in the meetings."

    mara_solenne "Then stay beside me."
    "You both laugh; it sounds like a promise and a plan. It is small and enormous all at once."
    hide elias_harrow
    hide mara_solenne

    scene bg ch6_601bcb_5 at full_bg
    # play music "music_placeholder"  # [Music: The strings rise into a gentle, hopeful chorus. Ambient sounds of the neighborhood swell — conversation, tools, tide — as if the city itself is breathing easier.]
    "You know that the pilot is only the beginning. The ordinance must be defended; budgets reallocated; the occasional hard decision will still press against what you love. But in this moment the balance tilts. A living"
    "barrier stands between the open sea and your neighbors' homes. Jobs are forming from seedlings and scaffoldings. Young people learn to read marsh and metric together. Lucia nods on the record. Mateo's memo is pinned to"
    "the community board. Beaconworks keeps its promise to second technicians who will teach and then exit, leaving practiced hands in place."
    "You think of the sibling you lost to a storm years ago. You carry that absence like a scar and a compass. Today, the scar feels less like a wound and more like a bearing — something that tells you where to point the work."
    show eda_nal at left:
        zoom 0.7

    eda_nal "Tides will come as they always have. We cannot stop them; we can teach them new stories to carry."
    "You press your thumb against the hydroponic locket, feeling the small sprig inside rustle. For the first time in a long time, you imagine seasons ahead that hold growth, apprentices who will become keepers, and a"
    "city that learns to mix steel with root rather than choose one over the other."
    "Elias leans his forehead to yours, a brief, brave touch."
    show elias_harrow at right:
        zoom 0.7

    elias_harrow "Whatever comes next, we'll be ready to read it together."
    "You inhale the salt and the green and the soft smoke of someone frying dough for the market. You taste, finally, the rising chord you have been building toward: work made public and human; policy braided"
    "with mud; two people who have learned to hold the same line without breaking it."
    hide eda_nal
    hide elias_harrow

    scene bg ch6_601bcb_6 at full_bg
    # play music "music_placeholder"  # [Music: A final uplifting cadence, warm and sustained.]
    # play sound "sfx_placeholder"  # [Sound: A chorus of small, human sounds — laughter, clinking tools, the tide's hush — that promises continuation through action.]
    "You stand at the edge of the newly planted marsh, locket warm against your palm, Elias' hand in yours, the community at your back. It is not the end of the city's work, but it is"
    "the opening of a new chapter — one written in root and rope and the slow, stubborn labor of people who refuse to be moved by panic."

    scene bg ch6_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade into a single sustained string note that resolves into silence.]

    scene bg ch6_601bcb_8 at full_bg
    "THE END"
    # [GAME END]
    return
