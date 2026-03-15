label chapter12:

    # [Scene: Lab | Morning]

    scene bg ch11_e67f19_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Printer whirs; distant gull cry muffled by rain on the windowsill]
    # play music "music_placeholder"  # [Music: Tense, high-register strings; a taut low drone]
    "You stand over the main terminal, thumb tracing the damp, taped corner of your field notebook without thinking. The pilot's datasets bloom across the screen: time-series traces, contour maps, model runs with jagged, red-flagged anomalies. Your"
    "name is at the top of the report because you translated the math into a story the funders could read. Right now the story wants to be tidy; the numbers refuse."
    "Dr. Lian leans in, eyes narrowed behind thin lenses. Her cardigan has a new streak of mud on the cuff — a map of where she has been all week."
    show dr_lian_cho at left:
        zoom 0.7

    dr_lian_cho "The ensemble spread is wider than I'd like. Look at the reflection coefficients on 03:14 — that spike isn't noise."
    show alea_maren at right:
        zoom 0.7

    alea_maren "Is it an artifact of the mesh? Or a real reflection off the engineered element?"

    dr_lian_cho "It's physical. The runs with higher-resolution bathymetry still show localized amplification of surge downstream. Not across the board, but where drainage constrictions line the shore. Where people live."
    "That word — people — collects in the room like a smell. You read the heatmap again. Close to the harbor mouth, the engineered feature shaves peak surge by almost twenty percent. But the red rings"
    "trailing along the downstream neighborhoods are like onions: layering deeper harm beneath a surface win."
    "Tomas pushes his hair up with a gloved hand, looking younger than the lines on his face suggest."
    show tomas_reyes at center:
        zoom 0.7

    tomas_reyes "So we fix the harbor and flood the Cove? That's a shit trade."

    alea_maren "It's not automatic. The model shows risk transfers, not a simple swap. We can plan around that — design outflow channels, install marsh plugs further down, regrade culverts."

    tomas_reyes "Designs take money. People need roofs now."

    "You taste iron on your tongue, like the first time you failed to stop a flood. In the corner, a phone vibrates — a message from Rin Sato" "They're calling for a press piece. You ok?"

    menu:
        "Send a short reply: 'I'm looking at it.'":
            "You type, fingers tense. The briefness buys you a beat; Rin Sato's reply takes the edge off: an emoji, a sea-glass heart. It steadies you a fraction."
        "Call Rin Sato back":
            "You hit call and hear rain and Rin Sato's breath: 'Read me.' Their voice is warm and urgent; you find yourself explaining graphs instead of asking for comfort. The technical talk eases nothing."

    # --- merge ---
    "The lab conversation resumes."
    "Dr. Lian Cho folds her hands over a printout, gaze steady but weary."

    dr_lian_cho "If you certify a summary that obscures these downstream effects, you will be complicit in an incomplete picture. The problem is ethical, not computational."

    alea_maren "And if I publish raw data now? The funders might pull everything. Elias Hart could take the pieces and run with a unilateral build."

    dr_lian_cho "You're trapped in the bridge between care and optics. Which is a place you know well."
    "Your chest tightens. The lab's hum feels like a countdown. You scroll to the comment column: Funder Liaison — prefers 'measured wins' headline. Councilor Bea — wants clear success to keep momentum. Elias Hart — offered"
    "expansion, but only if you sign that the data is operationally favorable. Rin Sato — wants full transparency. Tomas wants homes."
    # [Scene: Pilot Site | Afternoon]
    hide dr_lian_cho
    hide alea_maren
    hide tomas_reyes

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant machinery, a metal clank; gulls shriek; wind picks up, sewing salt into your mouth]
    # play music "music_placeholder"  # [Music: Percussive, escalating rhythm; a high violin tremor]
    "You walk the toe of the pilot, rain-soaked cuffs clinging to your wrists. The place smells of wet concrete, diesel, and the sweet loam of newly planted marsh shoots. On the lee side the water sits"
    "with a peculiar stillness — ripples that shouldn't be there if energy were dissipating uniformly."
    "A technician, sleeves rolled, points to a measuring rod."

    "Technician" "We saw backflow here during the last trial. Instruments picked up the pressure spike. We could adjust armor profiles, but that adds time and cost."
    "Rin Sato approaches, paint splattered on their anorak, scarf whipping like a banner."
    show rin_sato at left:
        zoom 0.7

    rin_sato "I walked the downstream lanes. Old Mrs. Hargrove is putting sandbags at every doorway. If the headline is 'pilot success' and the Cove floods, no one forgives that placard. They remember who said safe and who didn't."
    show alea_maren at right:
        zoom 0.7

    alea_maren "If I frame the report as a success to secure funding for broader living shore work, we may get the money to mitigate downstream effects. The risk is that a funder hears 'success' and chooses a single action: build hard here and call it a day."

    rin_sato "They already like simple narratives. You're the translator, Alea. Don't let them sell the town a story that costs people their homes."
    "Your pulse hammers against your ribs. The horizon darkens; the sea takes on a low, swollen look — the sky pressing like a thumb."

    menu:
        "Lift the sensor housing and examine the damp connectors":
            "Your fingers are numb by the time you reseat the bolts. The instrument ticks like a tiny, insolent heart; its logs confirm the spike. It's real, and your hands know it."
        "Take a pocket photo and message it to Dr. Lian Cho before anyone else sees it":
            "You send the image. The reply is immediate: 'We need a meeting.' That single sentence opens into a room that will be full of more than you."
        "Say nothing, watch the tide":
            "You stand still, the cold biting. Watching doesn't make the numbers kinder. It only sharpens the ache of indecision."

    # --- merge ---
    "The conversation with Tomas follows."
    "Tomas grips your sleeve, voice low and raw."
    show tomas_reyes at center:
        zoom 0.7

    tomas_reyes "Which future are you choosing for us? You say 'we' when you talk to funders, but I need to know: whose safety do you mean?"
    "The words land like a bell. Your throat closes around them. Tomas's face is a map of trust and accusation — young hands reaching for an anchor that may or may not hold."
    # [Scene: Town Hall | Evening]
    hide rin_sato
    hide alea_maren
    hide tomas_reyes

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmured conversations, a chair scraping; the building's old heater coughs]
    # play music "music_placeholder"  # [Music: Strings accelerate with staccato pulses; low brass underscores inevitability]
    "The funders are here. Councilor Bea sits rigid, a chandelier of pearls and posture. Elias Hart moves like oil across glass — smooth, encroaching. Rin Sato is at your shoulder, alive with insistence. Dr. Lian places a calibrated calm between the chaos."

    "Funder Liaison" "We have press cycles to hit. If you can provide a digestible summary that showcases measurable wins within six months, we can announce scaling funds by quarter's end."
    show councilor_bea_ortega at left:
        zoom 0.7

    councilor_bea_ortega "Momentum matters. The town needs confidence. We cannot appear indecisive."
    show elias_hart at right:
        zoom 0.7

    elias_hart "Certify the data as operationally favorable, and I'm prepared to commit additional co-investment to expand the pilot to a full defense. It's contingent on leadership — your leadership, Alea."
    "Your mouth goes dry. The room condenses; the air tastes of wet paper and rehearsed promises."
    show alea_maren at center:
        zoom 0.7

    alea_maren "Operationally favorable is a technical term. The models show both reduction at the harbor and increased stress downstream under certain storm scenarios."

    elias_hart "Words can be curated. Operational favorability is about demonstrating functional reduction in peak surge where it matters most to commerce and infrastructure."
    hide councilor_bea_ortega
    show rin_sato at left:
        zoom 0.7

    rin_sato "So we'll fix the harbor and 'curate' the rest? People live in those downstream neighborhoods. They'll be treated like externalities."

    elias_hart "Rin, the scale of damage we're avoiding at the harbor's mouth justifies prioritization. There are always trade-offs."
    "Rin Sato's jaw tightens; they clasp a seed packet so hard it crumples."
    hide elias_hart
    show dr_lian_cho at right:
        zoom 0.7

    dr_lian_cho "This is not a trade-off that disappears with a glossy press release. If you let the narrative paper over detectable transfer effects, the community will bear consequences you can model but won't undo after the fact."
    hide alea_maren
    show councilor_bea_ortega at center:
        zoom 0.7

    councilor_bea_ortega "We need investment and jobs. The language around this report must preserve the possibility of scaled work. A clean headline keeps that door open."
    "Tomas stands now, voice louder than you expect."
    hide rin_sato
    show tomas_reyes at left:
        zoom 0.7

    tomas_reyes "Don't call it a headline. Call it a sentence that decides whether my uncle trusts the town council when they tell him where to go or when to leave. Your 'clean headline' decides whether people pack or stay."
    "Silence slices through the table. Rain drums like impatient fingers against the panes."
    "Your chest feels like a cavern of decisions — every corridor lit by someone else's expectation. You think of the taped corner of your notebook and the coordinates etched on the silver band on your finger."
    "You think of the sibling you couldn't save. The memory is an engine revving you toward action and also a chain that pins your legs."

    "Your phone buzzes again. The funder's legal team has attached a draft press release with emphatic language" "Evident reduction in peak surge — pilot demonstrates immediate mitigative capacity."
    hide dr_lian_cho
    show elias_hart at right:
        zoom 0.7

    elias_hart "Certify the summary. We build. We secure the harbor. The rest can be mitigated as we expand."
    hide councilor_bea_ortega
    show rin_sato at center:
        zoom 0.7

    rin_sato "Or you release the raw data and demand a moratorium until we put safe-guards into place."
    hide tomas_reyes
    show dr_lian_cho at left:
        zoom 0.7

    dr_lian_cho "Or you buy time — convene stakeholders, draft a binding hybrid policy, insist on conditions before any larger build proceeds."
    "The room tilts as all three possibilities hang in the air. Your heartbeat becomes a drumroll that won't stop."
    "Your internal voice — the careful, calculus voice you've trained to trust — lists consequences like ledger entries. Your other voice, smaller and wetter, counts names and doorways and Tomas's face."
    hide elias_hart
    show tomas_reyes at right:
        zoom 0.7

    tomas_reyes "Which future are you choosing for us?"
    "The question detonates. It is not technical now. It is not about code or mesh refinement. It is about who decides what safety looks like when lives are at stake."
    "Your palm is cold against the table. You can feel the table's varnish flake under your skin, small, indifferent things left behind by time. Outside, the storm grows teeth — a far-off rumble climbing to a near roar. The town's fate compresses into the moment between breaths."
    # play music "music_placeholder"  # [Music: Strings peak into a frenetic, almost unbearable pitch; percussion mimics a racing heart]
    "You realize the next move will define more than a fiscal quarter. It will define trust."
    hide rin_sato
    hide dr_lian_cho
    hide tomas_reyes

    scene bg ch11_e67f19_4 at full_bg
    # [Scene: Blackout Page-Turn | Instant]

    scene bg ch11_e67f19_5 at full_bg

    menu:
        "Certify and publish a toned, funder-friendly summary to secure full-scale funding.":
            jump chapter13
        "Release the raw data publicly and demand a moratorium until a hybrid plan is legally codified.":
            jump chapter13
        "Delay publication; convene Dr. Lian Cho, Rin Sato, and community leaders to draft a binding hybrid policy and buy more time.":
            jump chapter18
    return
