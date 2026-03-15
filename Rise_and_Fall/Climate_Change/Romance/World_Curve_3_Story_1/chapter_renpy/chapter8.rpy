label chapter8:

    # [Scene: Town Hall Plaza | Midday — Vote Day]

    scene bg ch8_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Pumps hum like distant generators; a restless crowd murmurs; an occasional gull cries over the harbor.]
    # play music "music_placeholder"  # [Music: A slow, minor cello drones underneath the ambient noise — a tone that does not promise resolution.]
    "You remember Avi’s tablet calendar like a bruise: two weeks, the word circling in your head until it set into a dull ache. Now that the day has arrived, the ache has form. It sits behind"
    "your breastbone, steady as the compass pendant against your chest. Rain beads on your jacket and drips into the patched knees of your cargo pants, carrying the smell of salt and diesel and a hundred bodies"
    "pressed together for a single thing that might save some and cost others."
    "The plaza is louder than you expected. Jonah Reyes stands by the market stall that has been converted into a makeshift information table, his hair plastered to his forehead, voice hoarse from chanting. He meets your"
    "eye and smiles—an expression you cannot read cleanly now, because everything between you has been braided with strategy and strain. He raises his hand in a look that could be encouragement, could be an apology, could"
    "be a challenge. You offer your thumb back, the old private signal between people who grew up counting tides."

    menu:
        "Walk with Jonah a few feet; let him stand with the crowd":
            "You slide past the table and stay at the edge of the gathering, letting Jonah take the center of the market's attention. He nods as if relieved, then leans into the mic. His voice softens when it reaches you in the rain: 'Bring them in strong, Mara.' The words are steady and small."
        "Ask Jonah to come inside with you — stand beside you at the podium":
            "You reach for Jonah's sleeve with a quick, private tug. He hesitates, then threads his arm through yours. His face tightens, the flash of something unspoken crossing it, then steadies. Inside, people will issue opinions about strength; together you feel harder to push."

    # --- merge ---
    "Continue"
    "You tuck your notebook into the inside pocket of your jacket where the leather has been worn by your palm. The tide maps are in your head now: the blue curves of what can be saved,"
    "the red margins of what will have to be ceded. You breathe the wet air and go inside."
    # [Scene: Town Hall — Council Chamber | Continuous]

    scene bg ch8_6b08b4_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A clerk shuffles paper; an electric fan whirs at the window; the crowd’s chants dim to a low undercurrent.]
    # play music "music_placeholder"  # [Music: Sparse, dissonant piano taps underscore each speaker like footsteps on a slick boardwalk.]
    "Avi's hand finds yours briefly at the threshold — a professional squeeze that means 'we will hold order' and 'this could go sideways.' He gestures to the seat beside him, then to the lectern, moderating his face into something that wants to be fair."
    "A voice over the PA announces Elena’s arrival. Her umbrella pops open — the clear dome clacks like a crisp, logical argument — and she moves through the crowd as if through a blueprint. Her eyes,"
    "the color of cold steel, scan the room. She folds the umbrella and places it beside the dais with a meticulous motion."
    show elena_voss at left:
        zoom 0.7

    elena_voss "Councilor Malhotra, thank you for convening this session. I know we all feel the urgency. My proposal offers immediate stabilization, long-term employment, and demonstrable protection for the shoreline."
    "Her words land like polished coins. The council murmurs their assent; they are hungry for metrics. Elena Voss's smile does not reach her eyes."
    "You stand when your name is called. The floor creaks under shifting bodies; someone drops a flyer and it skitters into your boot. You feel the pendant cold at your throat and decide, in the lean"
    "moment before you speak, how much of yourself to put into the argument. You could lead with models and error bars; you could lead with the boards that remember your father; you could try to do"
    "both and risk being read as unfocused."
    "You clear your throat."
    show mara_solano at right:
        zoom 0.7

    mara_solano "Council members, my name is Mara Solano. I speak for the people who have been here when the tides took small things first — a stoop, a birthday cake left on a porch, the map of a street. We have plans that rebuild wetlands, that work with water rather than against it. They are lower-cost, community-driven, and they restore the living buffer that protects our homes."

    "A council member" "Ms. Solano, while your restoration plan is—"

    elena_voss "—admirable in principle. But principle does not keep a hospital's power on during a surge, nor does it provide the immediate funding to retrofit critical infrastructure. My firm’s barrier system is engineered to hold the high tide while we uplift the neighborhood. It is scalable and insurable."
    "You counter, but not as a reflex this time. You fold the data into the story: sedimentation rates, species that seed the marsh, the cost curve of living defenses versus permanent walls. The room listens, but"
    "the city’s appetite for certainty is loud; statements about jobs and insurance make the council lean forward."

    menu:
        "Keep the presentation clinical — focus strictly on data and cost-benefit comparisons":
            "You pull the field reports from your memory and list the expected retention rates and maintenance costs. Numbers map the marsh's potential in a language Council understands. Faces nod. But somewhere in the back a child’s wail flickers across your chest like a cold tide—facts fill the ledger but do not hold hands."
        "Share the personal — tell the story of your father and the tide-lines on the boards":
            "You let the voice change, let the room feel the scrape of memory: the name of the alley, the way your father's boots left salt on the boards. Several in the council look uncomfortably away; a few eyes soften. It is riskier politically, but the air tilts. You notice Elena's jaw tighten, not in data but in recognition that this conversation is no longer only about engineering."

    # --- merge ---
    "Continue"
    show councilor_avi_malhotra at center:
        zoom 0.7

    councilor_avi_malhotra "We need both, Mara. Make it precise. Make it human."
    "You press the point of your pen to a page, following the rhythm of the pumps humming outside. Claire, who has been quiet, clears her throat and leans forward."
    hide elena_voss
    show dr_claire_hsu at left:
        zoom 0.7

    dr_claire_hsu "The models Elena's team uses are powerful, but they optimize for a single metric: structural persistence. They do not internalize socioecological feedbacks the way living systems do. There are scenarios—less likely, but catastrophic—where a hard barrier shifts flows and destabilizes adjacent marshes in ways the model underestimates."
    hide mara_solano
    show elena_voss at right:
        zoom 0.7

    elena_voss "Dr. Hsu, with respect, if we delayed action for every hypothetical, we would be paralyzed. People cannot wait for fixtures in the hypothetical to be resolved."

    dr_claire_hsu "I'm not arguing paralysis, I'm advocating rigor. We can combine immediate protections with independent oversight. We can avoid the blunt instrument."

    elena_voss "We have third-party validators. We have insurance partners. Delay increases risk for the very people you're trying to protect."
    "You feel the room tip between urgency and caution like a boat at a wash. The council exchanges looks, then requests public comments. Voices rise from the gallery."

    "Rosa (from the market co-op)" "If they build that spire like a dam, who's gonna buy the fish from us? The market runs on people who know the shore. You take the shore, you take the market."
    hide councilor_avi_malhotra
    show rosa_and_mateo_market_co_op at center:
        zoom 0.7

    rosa_and_mateo_market_co_op "We want protection. We want a plan we can trust. But not at the cost of the people who made this place what it is."

    "A member of the council" "Counselor Malhotra, clarification — has Voss committed to enforceable relocation limits and community land trusts?"
    hide dr_claire_hsu
    show councilor_avi_malhotra at left:
        zoom 0.7

    councilor_avi_malhotra "They have offered pilot zone protections and relocation funds. The language is still being negotiated."
    "You feel the weight of 'negotiated' like a rusted hinge. It can open or lock."
    "Throughout this, Jonah Reyes’s voice continues as an undercurrent from outside, a cadence bleeding through the chamber doors. When he entertains the crowd with a chant, the sound filters in and presses on your ribs."
    "Inside, the conversation becomes technical. Elena Voss displays slides: employment numbers, projected reductions in immediate flood risk, mockups of a gleaming waterfront with boutiques and raised promenades. Claire replies with overlays showing model sensitivity to small"
    "parameter shifts. Avi reads out a summary of the proposed compromise he has been drafting—piecemeal assurances, pilot zones, a calendar for review."

    councilor_avi_malhotra "Council members, we are presented with three paths: full approval with conditional protections, a hybrid proposal with enforceable wetlands and limited redevelopment, or pausing for independent review. Each path has cost. Each path carries risk."

    "A councilor" "Ms. Solano, given the urgency and the economic risk, what is your recommendation?"
    "The chamber looks at you with the intensity of tides. For a beat, you hear only the pumps."
    "You think of Aunt Pilar's hands pressing empanadas together while the rain scored the roof. You think of the murk-black tide that pulled at the dock the night your father didn't come home. You think of Jonah Reyes's face, the way his optimism has grown a little more brittle."
    "Claire shifts in her seat and slides a small, folded page across the table toward you — not loud, not dramatic, an almost private thing in a room full of witnesses. You cannot be certain what"
    "it contains: a flagged note, a stack of anomalies, a route to force a delay. If you open it here, you risk the legal and political blowback of releasing expert critique into the public record during"
    "a vote. If you keep it closed, you live with the knowledge of a potential blind spot in Elena’s system."
    hide elena_voss
    show dr_claire_hsu at right:
        zoom 0.7

    dr_claire_hsu "If it comes to that, I'll back your call. But you should know what the models miss. Read it if you must."
    "Her eyes hold something like apology and like challenge. The packet is neither a solution nor a hammer — just another weight."
    "Jonah Reyes appears at the doorway for a moment, silhouetted by the neon outside. You cannot read whether his look is blessing or reproach; it is complex and folded, heavy with the years you share and the decisions you have yet to make."
    # play sound "sfx_placeholder"  # [Sound: A gavel taps once. The room stills.]
    "Avi stands and straightens his papers. The council clerk rustles. This is the hour the calendar had been counting down to. The decision must be made and you stand at the center of it."
    # play music "music_placeholder"  # [Music: The cello deepens, a descending motif underscoring the sense of impending loss.]
    "You feel every margin in your plans and in the town's options: who will be saved, who will be moved, which histories will be paved over for a promise of safety. You think of the wetland"
    "terraces you sketched under lamplight, and you think of Elena Voss's gleaming cross-section of a protected boardwalk. Both are answers that leave casualties."

    councilor_avi_malhotra "The motion is before the council. Members, we will now proceed to vote. Ms. Solano, do you have anything further to add?"
    "You close your mouth for half a second, swallow the salt in your throat, and consider the small folded paper Claire slid toward you. The moment is a narrow corridor of possibility and consequence."

    menu:
        "Accept Voss's approval in exchange for immediate stabilization funds to protect some blocks.":
            jump chapter9
        "Push for a hybrid compromise with enforceable wetlands and limited redevelopment.":
            jump chapter9
        "Leak Claire’s model vulnerabilities and demand independent review, forcing a delay.":
            jump chapter14
    return
