label chapter3:

    # [Scene: City Hall — Planning Atrium | Midday]

    scene bg ch3_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low murmur of conversation, a camera shutter; distant rain pattering somewhere beyond the panes]
    # play music "music_placeholder"  # [Music: Sparse, tense piano undercurrent]
    "You step back from the cluster of microphones, the atrium folding itself around you in bright reflections and thin, recycled air. Your notebook is heavy in your hand; the compass at your throat vibrates with a"
    "pressure you can taste like metal. The room smells of polished stone and municipal breath — too-clean air that makes the salt on your skin feel like a betrayal."
    "Rows of chairs fan out like a geometry of judgment. Faces blur into factions: the stoic suits near the front, a ragged band of activists along the side, and clusters of residents with tired coats and"
    "clipped, nervous hands. Samir is in the front row — the sunlight from the skylight outlines him, a halo that does nothing to soften the tight line of his mouth. You can't read him. His expression"
    "is complex."

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A moderator's gavel — a polite plastic tap that still sounds like a verdict]
    # play music "music_placeholder"  # [Music: Minor chord, unresolved]

    "Moderator" "We'll begin with opening statements. Ms. Lin."
    "Your voice doesn't arrive as a single thing; it assembles. You feel it first in the back of your throat, then through the mouthpiece — dry, measured, practiced. You choose words that can be translated into budgets and blueprints."
    show mara_lin at left:
        zoom 0.7

    mara_lin "Thank you. Solace Bay doesn't need heroics — it needs stitches. Scattered, community-scale infrastructure that holds water where it falls and routes it away from homes. Tactile swales along the alleys, rooftop soak systems for every block, perforated pavement in the market corridors. These aren't stopgaps; they're distributed resilience. They buy time, decentralize failure, and they keep neighborhoods intact."
    "You can feel eyes on the diagrams pinned behind you: cross-sections of soil and root mats and terraces that bloom where concrete once ruled. The smell of damp soil you imagine for a moment—almost real—sharpens your voice."

    mara_lin "This approach centers residents as custodians, not collateral. It uses public works budgets differently: smaller contracts distributed to community co-ops, training apprentices from the neighborhoods, and a monitoring feedback loop that prioritizes repair over replacement. If we only build a single line of defense, we concentrate risk. We must spread it."
    "A tentative applause, then a pocket of skepticism. A council aide scribbles, the pen staccato like rain. You force your throat to loosen; your hands don't stop shaking until you set the notebook on the lectern."

    menu:
        "Adjust the compass around your neck, breathe slowly":
            "You slide the pendant under your collar, breath lengthening as the motion steadies you. Your next sentence arrives smoother, as if your chest has been rewired."
        "Look directly at Samir before you step down":
            "You catch Samir's eyes; for a heartbeat you try to read him. He gives the smallest nod — not comfort but solidarity — and you step back to let the next speaker take the floor."

    # --- merge ---
    "Continue to next speaker"
    hide mara_lin

    scene bg ch3_98c6f2_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A pen tapping the rim of a tablet; a quiet mechanical click as he pulls up a rendering]
    # play music "music_placeholder"  # [Music: Subtle tension, a higher-register string]
    "Elias Kade steps forward with the calm of someone used to measured rooms. His warm hazel eyes are steady; his fingers find the stylus clipped to his pocket as if by habit. He lays his hand"
    "on the tablet and the rendering blooms: a schematic of reinforced barriers, automated gates that rise with the tide, and maintenance corridors. The lines are clean as a promise."
    show elias_kade at left:
        zoom 0.7

    elias_kade "Mara's distributed measures are necessary — but they're not sufficient for the scale of risk we're facing. We can secure critical infrastructure with engineered defenses: modular seawalls tied to smart gates, redundancies for pump stations, and contractual timelines that deliver within fiscal cycles. These solutions protect the hospital, the transit hubs, and the low-lying business districts that the whole bay depends on."
    "You feel the room tilt when he says 'protects the hospital' — an invocation of a zero-sum logic where some things must be saved first. His voice is calm, and that calm is persuasive."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Elias, if the barriers create a false confidence in areas outside their footprint, we risk leaving other neighborhoods exposed."

    elias_kade "Not if we pair them with policy: zoning offsets, community grants, and a phased roll-out. You know that, Mara. You and I both want to reduce exposure."

    mara_lin "I do. But your timelines compress hard decisions into contract deadlines. Community capacity doesn't scale on a spreadsheet."

    elias_kade "Capacity scales when there's funding and structure. You know how to rally people — use that. I'll push the engineering; you push the hiring and training. We can both get what we need."
    "There's an unspoken ledger behind his words — competence on one column, urgency on the other. Your chest tightens. You want his certainty and fear its compromises."

    menu:
        "Press him on contractual lock-ins: ask how long a private contractor owns maintenance":
            "You ask the question aloud; Elias' jaw tightens. He gives a practiced, diplomatic answer about public procurement law and oversight clauses. The room hears nuance; a councilman scribbles 'terms' in bold."
        "Let the point rest and listen to Nova's response":
            "You bite the inside of your cheek and nod. Elias takes the pause as endorsement; his smile tightens, and you feel the micro-shift in the room's alignment."

    # --- merge ---
    "Continue to Nova's statement"
    hide elias_kade
    hide mara_lin

    scene bg ch3_98c6f2_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rustle of canvas and the distant murmur of a crowd chorus]
    # play music "music_placeholder"  # [Music: Electric, a low bass that vibrates the chest]
    "Nova Duarte takes the microphone like wielding a blade. Her voice carries the kind of rawness that splits polite air."
    show nova_duarte at left:
        zoom 0.7

    nova_duarte "We've already lost too much to 'phases' and 'pilots.' Managed retreat isn't surrender — it's triage for human lives. Move people out of the floodplain with dignity, create land trusts for displaced families, and restore tidal wetlands that will absorb the storms we can't engineer away. Restitution needs to be on the table. Real accountability, not platitudes."
    "Her words land like flint. The activists stir; someone in the crowd shouts a fragmented affirmation. Mayor Chen's lapel pin flashes under the lights like a metronome measuring consequences."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Managed retreat will displace communities — how do we ensure it's not another displacement story writ in policy?"

    nova_duarte "You put control back where it belongs. Community councils set timelines; vacated parcels become wetlands managed by the people who were there. No privatization. No backroom deals."

    mara_lin "That level of control will face the full force of institutional inertia and legal challenges. There must be legal frameworks and transitional housing —"

    nova_duarte "There are already legal frameworks — you only need the political will to use them. How many more storms, Mara? How many more promises before the people who actually live here are treated as expendable?"
    "Her eyes pin you. It's not accusation as much as a demand. You remember a kid you once knew whose house had been flood-ruined the year you were sixteen. Memory constricts your throat into a knot you haven't allowed yourself to untie in public."
    # play sound "sfx_placeholder"  # [Sound: A single, held breath rippling through the audience; someone sobs quietly and a camera zooms in]
    # play music "music_placeholder"  # [Music: Dissonant strings, slowing]

    "Mayor Chen" "This hearing requires options that are actionable within our sixty-day window. If there is a coalition plan, now is the time to present it."
    "The moderator gestures; the microphone is passed back to you. The atrium compresses. Your shoulders feel like the hinge of something that might crack."
    "Your mind catalogs the trade-offs like a ledger: Elias offers speed and institutional buy-in but risks community autonomy. Nova offers justice and long-term resilience but threatens immediate stability and provokes bureaucratic backlash. Your own distributed approach"
    "can be stitched into either, but it's not persuasive alone to the people who hold the purse strings."
    "Samir shifts in his seat. You catch his profile; there's a tremor at the corner of his eye. The room waits."
    "Your compass ticks against your sternum — a small, stubborn instrument demanding orientation. You could endorse Elias and secure quick protection. You could join Nova and push for radical, painful remapping. Or you could attempt a hybrid—engineered defenses with phased wetlands and community oversight."
    "If you speak for one, you will align with more than a plan; you'll align with a set of people, power, and a vision of what Solace Bay becomes. Choosing risks relationships, careers, and the neighborhoods you love."
    # play music "music_placeholder"  # [Music: Low, insistent—like a clock]
    "You feel each second like a small cut."

    menu:
        "Take a breath and frame a question for the mayor about the sixty-day constraint":
            "You ask whether the sixty-day demand allows for interim measures and what 'actionable' really means. The mayor's aide recites procurement timelines and contingency funds; the answer is thin but not absent. You buy yourself minutes, and the room registers your attempt to shift the clock."
        "Speak from memory — tell the story of a flooded alley to remind everyone what’s at stake":
            "You tell the alley story; the detail slices through civic language. Some faces soften, others look away. Nova's jaw tightens; Elias' eyes briefly cloud. You've moved hearts, but not necessarily votes."

    # --- merge ---
    "Return focus to your proposal"
    "You set your palm on the lectern. The microphone hisses as you lean in. In the glass walls, the skyline blurs into the low, churning sea — a reminder that every policy here is ultimately about water."

    mara_lin "Mayor Chen, council members — we are not choosing between people and infrastructure. We are choosing the order in which we honor lives and livelihoods. Immediate structural protection buys the city time, yes. Managed retreat buys lives in the long run, yes. Distributed, neighborhood-led systems buy community continuity, yes. None of these alone will be sufficient. All of them together are messy, political, and slow."
    "You pause. The words feel like stepping stones over dark water; each must hold."

    mara_lin "If we bind engineering contracts to community oversight, phase wetlands with relocation pathways and legal guarantees, and fund community co-ops to maintain localized systems in parallel, we can create redundancy rather than concentration. It won't be pretty. It won't be fast. It will require a redistribution of trust and resources that our institutions haven't been eager to offer."

    "A councilwoman folds her arms. A line forms on the projector" "Feasibility: ?"
    "Elias Kade approaches, voice low enough that only you hear it between the applause and the breathless hush."
    show elias_kade at center:
        zoom 0.7

    elias_kade "You think they'll accept such a tangled plan in sixty days?"

    mara_lin "I think they'll resist. I also think it's the only thing that isn't a cliff."

    elias_kade "If you propose it, you'll anger people who see compromise as betrayal. Nova won't forgive the half-measure. The mayor will call it indecisive."

    mara_lin "And if we pick a single, shiny thing?"

    elias_kade "We risk making a decision that looks like certainty and is instead a liability."
    "He steps back, the stylus glinting once as he tucks it away. There is care in his caution now, not only calculation. Your throat tightens again — for what could be and what it will cost."
    "Nova Duarte watches you with an unreadable calculation. Her hands are clenched around the strap of her satchel, fingers white. When you try to read her expression, it is, appropriately, complex."

    nova_duarte "Mara, you can't have it both ways. People are asking for clarity. Do you stand with those who would prevent more loss now, or with those who would ask us to walk away to survive?"
    "Her question is less about policy than allegiance."
    "You inhale. The atrium seems to narrow until you can feel the weight of every choice pressing into the bones of your hand."
    "Your compass ticks, slow and persistent — and then loud, like a second heart. You can feel the fracture in the room as acutely as a physical split. If you pick one path, someone will be pulled taut."
    # play music "music_placeholder"  # [Music: Single low note; then, silence]
    "You open your mouth to answer, but the word you need is a negotiation, not a declarative emblem. The room waits for the shape of your commitment."
    "You trace the margin of your notebook with a fingertip, tasting the salt of old storms on your lips. The choice is a hinge. You know that however you step will set the path forward — and the people you love will bend with it or break."

    menu:
        "Endorse Elias' seawall plan to secure funding and quick protection.":
            jump chapter4
        "Join Nova's demand for managed retreat and grassroots control.":
            jump chapter7
        "Propose a hybrid coalition: engineered defenses + phased wetland restoration with community oversight.":
            jump chapter10
    return
