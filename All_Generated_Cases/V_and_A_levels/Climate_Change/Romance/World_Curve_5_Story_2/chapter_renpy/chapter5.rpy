label chapter5:

    # [Scene: Maris Bay Research Greenhouse | Dawn]

    scene bg ch5_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind like a low animal at the glass; the first distant slap of surf. A battery-powered fan whines to life.]
    "You breathe and your breath fogs the inside of your glasses. The rim of the world is a blurring smear of salt and light. Your hair sticks damp to your neck; the silver streak at your"
    "temple prickles in the cold humidity. Hands that usually make careful graphs and patient notes tremble just enough to notice."
    "Dr. Lian Obasi crouches by a bank of sensors, fingers flying as they boot and recalibrate. Their voice is clipped but steady, a wire of competence stretched tight."
    show dr_lian_obasi at left:
        zoom 0.7

    dr_lian_obasi "All right—tide-pred buffer initialized. Sensors show an early super-tide pulse one and a half meters above predicted. Wave set is increasing; wind vectors have rotated east-northeast. Marsh saturation will hit critical within ninety minutes if the surge holds."
    "You swallow. The data sounds smaller than the noise of the wind through the algae tanks, but it lines up with what your hands already feel — a pressure in the air that wants to push the town into a thinner version of itself."
    "Kaito Navarro's silhouette moves through the glass like a shadow with purpose. Through the greenhouse panes you see the pier: ropes coiled, volunteers forming, his hands a steady metronome as he signals where rescue lines should"
    "be thrown. He catches your eye and gives a small, tight nod — the kind that carries a question and a command at once."
    show kaito_navarro at right:
        zoom 0.7

    kaito_navarro "We're patching the first tier of sandbags, but the boardwalk is taking brine already. If this pushes, small boats will be cut off inside two hours. I need two extra hands on stern lines."
    "You want to move. You want to be everywhere at once: calibrating sensors, knotting rope, arguing clauses with polished lawyers who smell of dry heat and assurance. The greenhouse multiplies tasks into a kind of cruel geometry; every plan you made scrabbles for purchase in the rising water."
    "Jun Park slips in at your elbow, damp collar, eyes darting. He carries TideLine's permit packet like a live thing. He lowers his voice."
    show jun_park at center:
        zoom 0.7

    jun_park "I—I've read through the clause again. There's a fallback provision. If the company implements emergency levees, they assume operational control. It... prioritizes their maintenance schedules over local vessel access."
    "You feel the word 'assume' like a rope dropped over a harbor wall. You can see the consequences in a dozen small, immediate ways: no small craft out before harvests, cooperative pier access reduced to an appointment made into paperwork, fingers of the bay sold into timetables."
    "Aria Chen arrives flanked by a modular crew, AR lenses catching the greenhouse light and spitting up timelines in translucent overlays. She steps into the humid air with the calm of a storm engineer who has practiced her stride. Her voice is cool and unhurried."
    hide dr_lian_obasi
    show aria_chen at left:
        zoom 0.7

    aria_chen "We can mobilize temporary barriers within hours. Our plan will keep the water out of the town's critical infrastructure. We can negotiate about access afterward. Right now, lives are at risk."
    "Her projected timeline scrolls between you and the algae tanks: neat bars, phases, a stamp that reads APPROVED — accelerated permits glowing like a promise you do not trust."
    hide kaito_navarro
    show marin_sol at right:
        zoom 0.7

    marin_sol "Negotiating afterward isn't neutral. Access is lifeblood here. 'Temporary' can become permanent if control shifts."

    aria_chen "Temporary is preferable to permanent submersion. We can retrofit access points if needed. This is triage."
    "The words sit in your mouth like a bitter pill. She's right about the immediate math — the physics of walls and water — and wrong about the social arithmetic: what 'retrofit' often erases are ways of being and seasons of living."

    menu:
        "Rush outside to help Kaito on the pier":
            "You run the greenhouse door open and taste salt and rain, lungs pressed flat by wind. Your boots splash through pooled water. You find Kaito handing out flip-lines, eyes like flint, and you move as one—knotting, hauling, swearing between the gusts."
        "Stay and secure sensor data with Lian":
            "You grab the sensor board, fingers numbed, fingers sorting cables. Lian mutters gratitude and instructions; each confirmation feels like a small, stubborn defense against something bigger than the two of you."

    # --- merge ---
    "Scene continues after either action."
    hide jun_park
    show dr_lian_obasi at center:
        zoom 0.7

    dr_lian_obasi "If we can keep a live feed of marsh saturation, we might steer volunteer effort to the areas that buy the most time. But I need a clear relay to the pier."
    hide aria_chen
    show kaito_navarro at left:
        zoom 0.7

    kaito_navarro "Marin! Help with the sterns! The middle boardwalk's giving!"
    "You stand split between the blue-lit logic of Lian's graphs and the thick, immediate pull of hands on rope. The greenhouse smells of wet soil and a sharp metallic tang from the algae tanks. Outside, the"
    "marsh plots you planted — the careful ribs of roots and detritus meant to slow water and invite life back in — tremble under a wind that sings through them like someone testing a bone."
    "Rosa, in paint-splattered overalls, appears at the greenhouse door as if sewn to the place. Her face is flushed; she moves through the room with fierce, efficient warmth, rallying volunteers like a bright flag. Her voice cuts the static of worry."
    hide marin_sol
    show rosa_sol at right:
        zoom 0.7

    rosa_sol "Sandbags here! Move the grafted crowns! Someone with a drill—secure the raised beds! People—check on the elder houses on Seaside Lane!"
    "You want to trust the plan you wrote, the slow stitched ethics of restoration. You want to believe words can hold when water wants to unmake them. But the storm is an honest force: it will test promises with a blunt fist and measure you in moments."
    # play sound "sfx_placeholder"  # [Sound: A new engine note—mechanized, precise—rises beneath the wind. TideLine's temporary platforms hum in the distance; lights cut through the gray like blades.]
    "Jun Park finds you again, voice barely audible over a roar now building to a howl."
    hide dr_lian_obasi
    show jun_park at center:
        zoom 0.7

    jun_park "There are indemnities tied to the funding. If the company erects emergency levees, their priority schedule could legally supersede town directives for safety reasons. They justify it as systemic risk management, but—"
    hide kaito_navarro
    show marin_sol at left:
        zoom 0.7

    marin_sol "—but that means they can close sections for maintenance or deny boat launches during their cycles. It makes access transactional."

    jun_park "Yes. I don't—I'm sorry. I only saw it in the fine print yesterday. I thought—"
    "Your throat tightens. The greenhouse seems suddenly small, the algae tanks' glow a distant heartbeat. You can hear, in the distance, the first violent slap as a wave finds the soft place in the boardwalk. Volunteers shout. Someone curses; someone laughs in a way that is half-cry."
    "Aria Chen steps closer, voice pitched low but public."
    hide rosa_sol
    show aria_chen at right:
        zoom 0.7

    aria_chen "We can pool TideLine's emergency funds to shore up the worst-affected homes. It buys evacuation space and public safety. We put a clause in writing now about working with the co-op on access restoration."
    hide jun_park
    show kaito_navarro at center:
        zoom 0.7

    kaito_navarro "A clause that goes into corporate hands is not a promise to us. We don't get to be a footnote in a litigated manual. This isn't just infrastructure; it's how our kids learn the tides."

    aria_chen "Those are hard conversations we can have once the immediate threat is mitigated. You are prioritizing autonomy over safety."

    kaito_navarro "And you are prioritizing efficiency over the muscle memory of a community."
    "The exchange has more in it than its words. Beneath each retort crease old wounds — distrust threaded through long histories. Aria is polished; her conviction is alloyed with a belief that time and money scale"
    "solutions. Kaito's stubbornness smells of lineage and salt. You are between them like a seam, holding together two fabrics that fray at the edges."

    menu:
        "Step between Aria and Kaito, demand a pause":
            "You raise both hands, palms out, voice caught in the gale. 'Pause—' you say, and for a breath there is a clearing. Kaito looks at you, jaw set; Aria's AR overlays tremble faintly as if unsure where to pin their logic."
        "Side with Kaito openly, call Aria on her fallacy":
            "You point at the projected timeline, voice hard. 'Your 'retrofit' is vague. We have families who can't wait for 'later.' If you can't commit to guarding access now, we won't sign away our harbor.' Aria's lips thin; Jun's face goes white at the publicness of it."

    # --- merge ---
    "Scene continues after either action."
    hide marin_sol
    show dr_lian_obasi at left:
        zoom 0.7

    dr_lian_obasi "If we leak the clause, it forces public scrutiny. But—there will be legal blowback and construction could be delayed past the surge. We could lose the immediate resources."

    aria_chen "Leaks complicate crisis responses. We can be accountable without theatrics. We can draft guardrails and oversight."
    hide aria_chen
    show jun_park at right:
        zoom 0.7

    jun_park "There are reporters in the neighboring inlet. I know someone who—"
    "Your phone vibrates with a call you haven't the time to pick. It lights up as Mayor Ana Beltran's name. You hold it to your ear; the mayor's words are another instrument of pressure, thin and pragmatic and tired."
    hide kaito_navarro
    show mayor_ana_beltran at center:
        zoom 0.7

    mayor_ana_beltran "Marin—I've read the fallback. It gives them operational control in declared emergencies. They legally prioritize barrier integrity. They told me they'd include co-op access in the protocol, but they also made it explicit — they reserve the right to restrict vessel movement for safety scheduling."
    "You feel the room fracture. The mayor's tone is not an accusation but a ledger balanced against fear: shelters to open, vulnerable streets to patch, budgets spread like thin paint. Her exhaustion lands on you as a charge."

    mayor_ana_beltran "If the town refuses their immediate offer, I need a concrete, actionable backup for evacuation and critical supply lanes. People are already asking for shelter assignments."
    hide dr_lian_obasi
    show marin_sol at left:
        zoom 0.7

    marin_sol "We have marsh holdouts and volunteer routes. We can prioritize the elders' homes and the pier's east channel. But we need materials, pumps—"

    mayor_ana_beltran "TideLine has staging crews and funding now. This is where resources are. I cannot ignore that. This is not about politics; it's about people being dry."
    "You hear the pragmatism in her voice and the squeeze of responsibility. The question feels like a wedge: save lives now but risk surrendering long-term stewardship, or hold out for agency and pray the tide does not outpace courage."
    "Outside, the surge grows teeth. The marsh plots you planted — the small, stubborn experiments meant to eat at erosion — shudder and take the first real test of their life. You think of the hands"
    "that dug those beds, the kids who planted cordgrass during a summer workshop, Old Tomas telling stories about a sea that used to be patient. The greenhouse lights splash teal across faces, and you realize the"
    "bioluminescent algae looks like a heartbeat underwater — small and stubborn."
    "Rosa appears beside you with a soaked list. Her voice is a bright blade."
    hide jun_park
    show rosa_sol at right:
        zoom 0.7

    rosa_sol "Evacuations done on Seaside Lane. Old Tomas refuses to leave without his boat's tiller fixed. The co-op is short two volunteers for the east channel. If we don't get docking coordinated, they'll be trapped."
    hide mayor_ana_beltran
    show kaito_navarro at center:
        zoom 0.7

    kaito_navarro "If they lock the schedule, those boats—our boats—won't reach families when they need to. That's not safety—it's a timetable."
    hide marin_sol
    show jun_park at left:
        zoom 0.7

    jun_park "I can leak the fallback wording to someone. It would force an emergency editorial. It would make them answer publicly."
    hide rosa_sol
    show aria_chen at right:
        zoom 0.7

    aria_chen "You leak and construction stops. You refuse and people stay wet. You accept and you cede leverage. Which one saves more people?"
    "Your notebook — the battered waterproof one that has been a map of hope and a ledger of guilt — slips from your hand as if gravity has grown teeth. It thuds open on sodden paper;"
    "ink smears like a small surrender. You see your own handwriting blurred into a watery smear: Bridge. Listen. Protect."
    "Everything feels compressed into that smear. The town's momentum collapses into a single, urgent question that thrums through your bloodstream and right into your words."
    hide kaito_navarro
    show marin_sol at center:
        zoom 0.7

    marin_sol "We can't—' Your voice fractures. Wind takes half of it. 'We can't let people drown in the name of clean contracts."

    aria_chen "And we can't let bureaucracy cost lives. I am offering you tools to stop the water right now. Contracts can be amended—"
    hide jun_park
    show kaito_navarro at left:
        zoom 0.7

    kaito_navarro "And what of the next season when access is a calendar appointment? We'll barter off a culture for a dry floor."
    hide aria_chen
    show jun_park at right:
        zoom 0.7

    jun_park "I can—I can get it to a reporter. They'd run it tonight. But it might stop the deployment."
    hide marin_sol
    show dr_lian_obasi at center:
        zoom 0.7

    dr_lian_obasi "We can try to stagger TideLine's resources with our volunteer hubs—buy time without signing operational control away. But we need on-the-ground pumps and funding immediate."
    hide kaito_navarro
    show mayor_ana_beltran at left:
        zoom 0.7

    mayor_ana_beltran "Marin. I need you to tell me what to tell the town. They are asking me to choose. I can't carry both the town's safety and your plan if it means losing the immediate option to stage levees."
    "The wind rises. The rain lashes like thrown stones. Somewhere a board gives with a splintering sound. The sea roars; it is a thing with size and appetite and terrible, indifferent logic."
    "You feel the collapse of momentum — months of planning buckling into an emergency's jagged teeth. The moral urgency is not an abstract calculus anymore; it is an immediate, physical pressure on the chest. The choices"
    "spread out like broken planks: each might hold you, but each glitters with sharp risk."
    "Your hands still smell of wet paper and algae. The maps inside your head — the slow plans, the community meetings, the promises exchanged on porches — feel both fragile and necessary at once. You are"
    "the point where strategy and survival have to meet without dissolving the town into something neither you nor Kaito recognize."
    "You inhale, the air full of salt and diesel and rain. The question hammers in your bones: who do you choose to save in this minute, and what will that choice cost later?"
    # play sound "sfx_placeholder"  # [Sound: The sea's roar eclipses conversation; rain is a steady, punishing percussion. A horn blares somewhere close. Music: A rising, urgent string motif, building without release.]
    hide jun_park
    hide dr_lian_obasi
    hide mayor_ana_beltran

    scene bg ch5_4001e7_2 at full_bg

    menu:
        "Accept TideLine's scaled payment and promise to renegotiate later":
            "You step forward, voice steadied by the immediacy of need. 'Fine. We accept the scaled payment to fund rescue and temporary barriers—on the condition you waive operational closure of our access in the interim and commit to a publicly mediated renegotiation.' Aria's jaw tightens but the nod from TideLine's project lead is almost immediate; ropes are put into motion. The crowd breathes; pumps arrive."
        "Refuse publicly and organize the co-op to resist—no contract":
            "You shake your head and find the words loud enough to be heard: 'No contract. Not now. We will organize evacuation and defense from our side. We will not sign away our harbor.' Kaito's face opens with fierce relief; you see volunteers square their shoulders. The tide, indifferent, answers with a higher swell. The mayor's silence is a weight."
        "Leak the contract to a sympathetic journalist via Jun Park":
            "You hand Jun a soaked page and his hands tremble. 'Get it out now,' you tell him. He walks off with the furtive gait of someone carrying dynamite. A reporter's motorboat answer might slow the build—but the immediate pumps and staging could be delayed, and the night will be long and loud with legal teeth."

    # --- merge ---
    "Scene pauses for the town's response as the decision is made."

    menu:
        "Accept a scaled payment from TideLine now to fund rescue and promise renegotiation later.":
            jump chapter6
        "Publicly refuse and organize the co-op to resist corporate control—no contract.":
            jump chapter14
        "Leak the contract to a sympathetic journalist via Jun Park and demand public scrutiny.":
            jump chapter6
    return
