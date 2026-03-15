label chapter4:

    # [Scene: Old Pier | Dusk]

    scene bg ch4_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind keening through rigging; distant gulls; a loose board creaks underfoot]
    # play music "music_placeholder"  # [Music: Tense strings build a steady scrape—urgent, unrelenting]
    "You leave the rooftop meeting with the taste of iron on your tongue and the echo of voices braided through the hall—votes counted, petitions signed, fists pressed into palms. The town's breath seems to follow you"
    "as you cross the street: a low, collective uncertainty that sits under your shoulder blades and refuses to be shrugged off."
    "Your boots hit the Old Pier's dark boards. Saltwater slicks the wood; your steps are careful and too loud, the sound swallowed by wind and water. You pull your jacket tighter, feeling the seam at your"
    "temple press like a pulse against the silver streak in your hair. You touch it anyway, an automatic steadiness, as if the thin ribbon of metal could hold your thoughts in place."
    "You catalog what was said in the meeting like a litany: Bridge. Listen. Protect. You said them until the words lost their softness and became a weapon and a promise all at once. Saying 'no' to TideLine's contract felt like stepping into surf you couldn't unlearn."
    "(Internal) You can already hear the angles that will be used against you: obstruction, endangering the town, idealism over pragmatism. You can feel the ledger of debts and fears stacking in the mouths of neighbors who"
    "want roofs and paychecks now. The ledger keeps a rhythm like rain on a metal roof, and you have only so many hands."
    "A shadow detaches itself from the pier's far rail and moves toward you—Kaito. His navy sweater clings damp to him; the salt on his cuffs mirrors the salt on your boots. He leans both hands on the rope, knuckles white, eyes fixed on the water as if measuring it twice."
    show kaito_navarro at left:
        zoom 0.7

    kaito_navarro "You put us on the map,' he says quietly, eyes not on you yet. 'You put us where TideLine can weigh us."
    "You can hear the accusation without malice—more like fear shaped into something sharp. His voice has a tilt of blame that does not match the pleading in his hazel eyes."
    show marin_sol at right:
        zoom 0.7

    marin_sol "I didn't put us on anything. They were already circling, Kaito. I gave people a way to not sell the shore short."
    "Kaito studies your face. He lets out a breath that sounds like breaking rope."

    kaito_navarro "Do you know what refusing it looks like from their side? Lawsuits. Lost contracts for the co-op. Subcontractors we rely on—gone overnight. People who can't repair their homes because the money isn't there. Did you think about that? Did you think about how many mouths that would shut?"
    "You feel your pulse ratchet up, the pier's wind a physical pressure now. The words hit the place behind your sternum where guilt lives, the place that sometimes names your choices for you."

    marin_sol "I thought about everything. Twice. I thought about the people who will be priced out of the shoreline when a wall goes up, about nets and tides and the marshes that feed us. I thought—"
    "Kaito cuts in, voice low enough that just you can hear it."

    kaito_navarro "Thinking isn't the same as knowing. It feels like gambling with our neighbors' lives."
    "You want to answer—explain the pilot marsh plan, the sensors, the scalable model Dr. Lian outlined, the nights you spent making lists—but the words feel brittle. Instead you say what you can hold to."

    marin_sol "I don't think of this as a gamble. I think of it as care that takes time. I won't sell them out for a quick fix."
    "Kaito's jaw works. For a moment he looks like the boy who learned to tie knots on Old Tomas's boat—concentrated, stubborn, afraid."

    kaito_navarro "So you chose. You put your name on 'no'. You understand what that means too, right? People will ask whose side you're on by Wednesday. They don't do nuance when they want shelter."

    menu:
        "Reach across the rail and take his hand":
            "Your fingers close around his callused palm. He startles, then tightens his grip, like finding a line to hold onto. His voice goes softer, and for a breath you both stand without saying anything."
        "Step back and make space":
            "You step back a half-foot, the gap between you widening like a geography you didn't mean to open. Kaito's eyes flash—surprised, hurt—but he doesn't move away. The wind seems to wedge words between you and the sea."

    # --- merge ---
    "..."
    "Kaito doesn't pull away from either your touch or your distance. Whatever small comfort that is, it's fragile. Behind him, the pier is no longer empty. Rosa moves along the boardwalk, a smear of bright paint"
    "on her overalls, barking orders at volunteers stacking sandbags and badge-wearing neighbors checking lists. Her presence is practical and solid—both balm and reminder."
    show rosa_sol at center:
        zoom 0.7

    rosa_sol "Marin! The seedlings are in—Lian says we can up the marsh density in three weeks. We have knives and rope and ten people for the breakwater build on Saturday. We can start the volunteer roster tonight.' (She offers you a wet handkerchief, then plants both palms on her hips.) 'Don't let them make you feel alone."
    "You take the handkerchief, thumb rubbing at damp fabric. The gratitude in you sticks like salt under a wound; the weight of expectation is something Rosa never fails to lift and throw back at you."
    "A buzz in your pocket. You fish your phone out with one hand; Dr. Lian's name flashes through—sensor data, new tide models, marsh pilot scalability. You read the message aloud because the numbers anchor you."

    "Marin Solé (reading)" "\'Sensors show enhanced sediment accretion in pilot zone—projected 18 months to measurable stabilization if expanded. Confidence interval improving with community planting.\'"

    "Dr. Lian Obasi (via voice note)" "We can scale this. We just need boots and a schedule. And public backing. Keep them standing with us."
    "You replay the message twice, like a prayer and a map. The numbers feel like a lifeline. But before you can breathe, the sound of heels on boards—measured, clinical—cuts into the air."
    "Aria Chen appears at the pier's mouth as if she's been sculpted there: jacket unflapped, brochure held like a placard. Her steely blue-gray eyes take you in with a slow, assessing gaze that doesn't yield."
    hide kaito_navarro
    show aria_chen at left:
        zoom 0.7

    aria_chen "Marin Solé,' she says, voice cool and practiced. 'Forthright as ever. You made a strong showing at the hall."
    "You notice the brochure—slick images of engineered walls, calm seas, smiling families framed by corporate logos. It's the promise you refused. The light catches the TideLine emblem and the modernist lines feel like a knife edge against the pier's weathered wood."

    marin_sol "We need solutions that keep the community intact. Your plan—if it means restricting access, commodifying the shore—will break more than it saves."
    "Aria's expression doesn't harden. Instead it tilts toward pity, efficient and brittle."

    aria_chen "You fear losing culture; I fear losing lives. There is a limit to how long we can ask people to wait for incremental solutions while homes wash away. Contracts can be amended to include access clauses—"
    "You want to argue the nuance: about co-design, about how engineered barriers alter currents and fisheries in ways models can't always predict. You want to tell her about Old Tomas's stories of the inlet shifting in a season. But Aria speaks again before you can build that sentence."

    aria_chen "We can move quickly, Marin. We can deliver funds fast. Time is a predator—"
    "Kaito steps forward between you and Aria, hands flat on the rail, voice flat and hard."
    hide marin_sol
    show kaito_navarro at right:
        zoom 0.7

    kaito_navarro "Your 'speed' comes with strings. We've read the contracts. Subcontractors own sections of the shoreline after build. They can prioritize private marinas or commercial leases. Our pier doesn't belong to them."
    "Aria's eyes flick to Kaito. For a fraction of a heartbeat, you see the calculation behind her composed face—how to neutralize an ally and isolate you. She smiles a thin, practiced smile."

    aria_chen "Those are negotiable details. We are not interested in taking what belongs to your people. We are interested in stopping floods."
    "Kaito's laugh is small and sharp."

    kaito_navarro "Negotiable? They've already priced parts of Maris Bay in their deck. They don't negotiate away profit unless forced."
    "Nearby, a small cluster of town volunteers slow and stare. You can feel the pier contracting like a throat. A man you've known since childhood—his hat pulled low—calls across the water, words lost to the wind but the tone unmistakable: distrust."
    "From the pier's far end, your phone vibrates again. Mayor Ana Beltran's name. You answer because the dial tone feels like a raw wire."

    "Mayor Ana Beltran (on phone)" "Marin. You did what you thought was right.' (There is a weariness, edges worn thin by duty.) 'But the council is fraying. Subcontractors are threatening suit if the contract is delayed. We've got people calling—the co-op's steady income is on the line. If TideLine walks, the council will be blamed."
    "You can hear the stress folded into her words—years of rain in a voice that used to be steady. Your hands tremble enough that your thumb slips on the screen."
    hide rosa_sol
    show marin_sol at center:
        zoom 0.7

    marin_sol "Ana, I know. But there are clauses in their proposal that we can't let stand. We can demand community oversight. We can write access protections—"
    hide aria_chen
    show mayor_ana_beltran at left:
        zoom 0.7

    mayor_ana_beltran "You have to understand the pressure I'm under. If lawsuits start, the town pays. My office can't guarantee payroll if the funding dries up. People are angry, Marin. They want roofs. They want answers now. We need to be careful with how we steer this."
    "The line clicks. The conversation isn't a blow so much as a steady erosion. She doesn't order you to change course—she can't—but the implication hangs: choose carefully, or bear the burden of whatever fallout follows."
    "(Internal) The ledger grows teeth: the lawsuits, the contractors, the co-op's pay, the urgency of roofs, the young families with little margin. You could feel the entire town's weight tilting toward any promise that seems fast enough to stop the bleeding. And you had said no."
    "You pull your battered notebook from your jacket and flip to the page you've been keeping at the back: nightly lists, a habit that steadies you. Your pen moves fast now—the lines are not neat."

    "Marin Solé (writing aloud)" "Tonight: volunteer roster—confirm 12; marsh seedling pickup—0400; Dr. Lian meeting—data review; community workshop—Thursday; legal counsel—contact pro-bono; press—prepare statement."
    "Rosa peers over your shoulder, nodding, and adds without asking."
    hide kaito_navarro
    show rosa_sol at right:
        zoom 0.7

    rosa_sol "Add: fundraiser at the co-op on Sunday. Old Tomas to tell his inlet story. We need hearts as well as hands."
    "You let the list grow until the margin is crowded and the ink blots with sweat. Each item is a small battle plan tossed against a tide. The notebook feels like the last place you can still lay down decisions without the weight of an entire town leaning on you."
    "The wind picks up—a thin, biting line across your neck. Beyond the headland a low bank of cloud has begun to bloom, a gray bruise on the horizon. It looks less like weather than an approaching verdict."
    "Aria steps closer, brochure folding softly in her hands. She waits for nothing and everything at once."
    hide marin_sol
    show aria_chen at center:
        zoom 0.7

    aria_chen "I don't expect to convince you tonight. But think of the people who need immediate protection. We can work with you on cultural access. Let us pilot the infrastructure where it's absolutely needed; let us build compromises."
    "Kaito scowls."
    hide mayor_ana_beltran
    show kaito_navarro at left:
        zoom 0.7

    kaito_navarro "Compromises are almost always the language of those who can walk away when it stops paying."
    "Rosa's voice is a blade of practicality."

    rosa_sol "We don't have the luxury of ideological purity when someone needs a roof. But neither do we accept being erased."
    "The pier seems to hum with conflicting truths. The town's future is a negotiation table stretched over water."
    "Your chest is tight and hot. Your pen hovers over the page. You could revise the list, fold into compromise, call a delay, or stand your ground and risk the legal and economic storms foretold. Each path feels like walking a plank."
    "(Internal) You feel your role shift from steward in quiet to target in public. This was never a private commitment, you realize; choosing 'no' made you a lightning rod. The fire you lit at the town hall is warm and bright—and now it threatens to become wildfire."

    menu:
        "Tell Aria you'll draft access clauses before a vote":
            "You say it in a rush: clause language, community oversight, binding clauses. Aria nods almost indulgently, making notes. Kaito's jaw tightens; Rosa's eyes search yours for proof this isn't another delaying tactic."
        "Refuse to negotiate on the pier; insist on community vote first":
            "You shake your head, pensively firm. 'We vote first,' you say. Aria's smile thins like a wire. Kaito exhales something that sounds like relief and fear mixed; Rosa reaches for your shoulder like someone bracing you for a wave."

    # --- merge ---
    "..."
    "The wind takes your words and casts them into the darkening distance. Somewhere inland, someone bangs a lid closed; someone else laughs too loudly to keep the worry silent. The noises are small but sharp—fragments of a town trying to remain whole under pressure."
    "You close the notebook, thumb resting where the ink is still tacky. The brine on the air tastes of consequence. Your fingers find the silver streak at your temple again, and you press as if you can hold your resolve there."
    "(Internal) The lull before storms—before the legal filings, before the construction crews arrive, before the first real test of either plan—feels not like calm but like brittle possibility. Every choice you make from here will be"
    "catalogued and argued and possibly weaponized. You had hoped to steward a quieter work of repair. Instead you've lit something visible, and visible things draw fire."
    "A far-off rumble threads the sky. It's not rain yet. It's not even a promise. But it is a sound like a judge clearing a throat. The horizon, blackening, takes shape. The pier's lanterns flicker against the rising wind."
    "You stand at the rail, salt-slick and braced, and you realize: this is not only about structures and marshes anymore. It's about who gets to tell the story of the town, and whether the story will"
    "be written by people who live on the bay or by those who can fund a different ending."
    # [Page-Turn Moment: The rumble grows into a low, insistent drum, a weather-sound and a public one. You feel it in your teeth. The town's murmurs tighten into something like an argument that hasn't yet been spoken aloud. You look at Kaito—his hands still on the rope, eyes fixed on you—and at Aria, composed and unblinking, brochure unopened in her palm. Behind them, Rosa rallies volunteers into a loose line of readiness. Your notebook is a closed map on your lap. You could change course, compromise, or hold. The sky begins to darken like an accusation. You inhale, feeling the weight of every unfinished list, and step forward into the wind, where choices will begin to make themselves visible.]
    hide rosa_sol
    hide aria_chen
    hide kaito_navarro

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind climbs; an engine hum is heard faintly far off—mechanized, purposeful]
    # play music "music_placeholder"  # [Music: Crescendo of strings then a single sustained, piercing note]

    scene bg ch4_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
