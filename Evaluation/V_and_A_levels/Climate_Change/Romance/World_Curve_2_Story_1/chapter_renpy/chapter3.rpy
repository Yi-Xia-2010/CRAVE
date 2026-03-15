label chapter3:

    # [Scene: Municipal Hall / Council Chamber | Late Afternoon]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense BGM — low strings and a restless woodwind motif]
    # play sound "sfx_placeholder"  # [Sound: Murmured conversations, the scrape of chairs, distant gull calls through the open vents]
    "The council chamber smells of lemon disinfectant and old paper. Light from the bay slices through the glass in thin, cold bars; behind them, a glossy rendering of Cassandra 'Cass' Whitlock's redevelopment glows—clean lines, raised promenades,"
    "landscaped seawalls that promise 'stability.' The projection washes the room in reassuring blues while the air feels thinner, like the gap between a promise and the shore."
    "You press your thumb into the coral scarf at your throat the same way you have since morning. The fabric is a tether; the scarf is small, and yet it is all there is between you and the tide of polished words in front of you."
    "Cassandra 'Cass' Whitlock steps forward with a practiced smile, the room folding obediently around her cadence. Her voice is clear, steady—solutions as bullet points, human costs in parentheses."
    show cassandra_cass_whitlock at left:
        zoom 0.7

    cassandra_cass_whitlock "Marrow Bay deserves predictability. Our plan secures vital infrastructure, brings private investment for resilient housing, and guarantees services for decades. We are not here to erase your memories—we are here to ensure they remain safe."

    "Council Member (Chair)" "Ms. Whitlock, thank you. We'll open the floor to public testimony after the presentation."
    "Her slides flip: cost estimates, timeline projections, renderings of raised promenades framed by tidy trees. Your chest tightens—not with surprise but with that specific sorrow that comes from seeing your neighborhood rendered as a graphic."
    "Noah sits two rows ahead, shoulders tight, hands bunched into a fist. Aunt Lila's knuckles whiten on her cane; she hums something under her breath, a rhythm of old tide-talk."
    "You rise when the clerk calls your name. The rattle of the room recedes; your voice finds its place inside the sockets of the chamber."
    show mira_santos at right:
        zoom 0.7

    mira_santos "My name is Mira Santos. I grew up here. I learned to read the tides the way some people read the weather—by paying attention to the small changes.' (You pause, feeling the scrape of all the faces watching.) 'I won't contest the math on a slide—I'm a scientist. I will contest what those numbers mean when the people who made them don't look you in the eye."

    "Council Member (Moderator)" "Ms. Santos, please stick to testimony related to the redevelopment plan."

    mira_santos "This is related. The plan's 'efficiency' erases how people live here. It doesn't count Aunt Lila's shell collection as infrastructure; it counts it as an obstacle. It doesn't count Noah's workshop as a node of resilience; it counts it as a cost to be mitigated. You can engineer a sea wall, yes—but you cannot engineer the memory of a town out of people who will carry it."
    "A ripple of murmurs. Cassandra 'Cass' Whitlock watches you with the same cool attention she gives her charts—measuring, cataloguing. There's no heat there; it's a calculation. You sense her public armor, the way it opens and closes like a hatch."

    cassandra_cass_whitlock "Ms. Santos, I respect community attachment, but we must be realistic. Incremental measures leave us exposed. Large-scale interventions are expensive, but they buy time. Would you prefer temporary fixes while lives are at risk?"

    mira_santos "There is no 'buying time' if the price is people uprooted and stories erased. We can design for dignity and adaptability. We can pilot approaches that keep neighborhoods intact."
    "A councilor interjects, brow furrowed."

    "Councilor (Marrow Ward)" "Is a pilot what you're proposing, Ms. Santos? A localized test? The council needs specifics."
    "Your eyes sweep the room automatically—Elias Park in the back, camera on his chest, the glint of copper on his wrist; Noel's jaw tight; Aunt Lila's face like flint. Elias Park catches your gaze and lifts"
    "his chin—there's a softness in the look that doesn't translate to the floor. It's complex, unreadable: relief mixed with a caution he always wears like a second skin."

    mira_santos "Yes. A pilot. Community-driven, with local labor, and transparency at every step.' (You can hear your own voice, clearer than the projection, small but steady.) 'We can show that living heritage and resilience are not mutually exclusive."

    "Council Member (Chair)" "We appreciate your testimony. The council will take this under advisement and propose to open negotiations between Ms. Whitlock's firm and community representatives to define scope."
    "The words land like a small, brittle thing: negotiation. A doorway that could be an opening or a trap. Cassandra 'Cass' Whitlock's smile tightens—not unkind, but resolved. The projection fades; the chamber's fluorescent lights hum like a distant storm."

    menu:
        "Open with a measured proposal":
            "You nod slowly and say, 'We'll prepare a formal pilot proposal with clear benchmarks,' an attempt to translate urgency into paperwork."
        "Call out the power imbalance":
            "You lean forward, voice edged: 'Negotiation is a luxury when one side controls the funding.' The room shifts; chairs creak as people take that in."
        "Ask for time—gather more voices":
            "You ask for an extension to gather wider testimony—an effort to buy space and breath—but the chair's watchful glance reminds you time is scarce."

    # --- merge ---
    "Continue to the rooftop greenhouse scene"
    hide cassandra_cass_whitlock
    hide mira_santos

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low wind motif underlines the unresolved tension]
    # play music "music_placeholder"  # [Music: Strings pull taut then soften]
    "The clerk calls the meeting adjourned. People drift into the plaza like flotsam looking for purchase. You step out with the crowd, the late sky a bruise of indigo and amber. Cassandra 'Cass' Whitlock moves through the crowd with assistants; when your paths cross she inclines her head."
    show cassandra_cass_whitlock at left:
        zoom 0.7

    cassandra_cass_whitlock "Ms. Santos, I hope we'll find common ground. My office can set a schedule for the negotiation team."
    show mira_santos at right:
        zoom 0.7

    mira_santos "Common ground requires equal footing."

    cassandra_cass_whitlock "We'll be transparent."
    "Transparency: the word tastes like seawater—salty and impossible to swallow if you suspect the bottle contains something else."
    # [Scene: Rooftop Greenhouse | Early Evening]
    hide cassandra_cass_whitlock
    hide mira_santos

    scene bg ch3_98c6f2_3 at full_bg
    # play music "music_placeholder"  # [Music: A softer, anxious piano; small percussive taps as rain begins at the edges]
    "You climb the narrow stairway to the greenhouse because some conversations need to happen under plants, where breath fogs glass and things that persist are visible. Elias Park is there, hands in a pot of seedlings,"
    "his jaw distractingly still. Noah is pacing; Aunt Lila sits in a folding chair, eyes narrowed, mouth set."
    show noah_rivera at left:
        zoom 0.7

    noah_rivera "They proposed negotiation. That's a door. It's also...a waiting room. They get to choose the furniture."
    show aunt_lila_santos at right:
        zoom 0.7

    aunt_lila_santos "Negotiation is a net. Sometimes it catches. Sometimes it strangles. You have to know when to cut the rope."
    show elias_park at center:
        zoom 0.7

    elias_park "A pilot could legitimize what we've been doing. If we can demonstrate real metrics—reduced flood impact, community-run maintenance—it might force the council to fund bottom-up solutions."
    "You feel the old impulse: build, measure, show. It's what you know how to do."
    hide noah_rivera
    show mira_santos at left:
        zoom 0.7

    mira_santos "But a pilot could also be co-opted. If they fund it, they could fold our methods into their control—turn it into a checkbox on their timeline."

    elias_park "I know. I had that happen before. It took a village being promised 'resilience' while being disbanded. I—' (He stops, fingers tightening on a seedling.) 'I don't want that to happen here."
    "His voice catches. The greenhouse smells like wet earth and tinny rain; the sound anchors the room. His expression when he looks at you again is complex—there's affection there, certainly, but also a reserve, the kind that says he'll not promise what he can't keep."
    "Aunt Lila reaches out and taps the coral scarf at your throat—an old gesture of kinship and insistence."

    aunt_lila_santos "If you go in with Elias Park, make sure eyes are on the accounting. Make sure the contracts say what you mean. If you're going to dance with their lawyers, bring your own music."
    hide aunt_lila_santos
    show noah_rivera at right:
        zoom 0.7

    noah_rivera "Option two: refuse. File injunctions, rally outside the hall nightly, get Jun to bring the school kids with signs, bring media. Make noise until the council realizes this can't be an easy sell."

    elias_park "That's a path that could work—public pressure. But it also opens us to legal and PR countermeasures. Cass has pockets and a narrative. If they paint us as anti-progress, folks who want safety could be turned against us."
    "You imagine headlines, the town split in the open like a tide pool. The fear here is not imaginary: displacement, lawyers, and targeted PR. And yet, you also imagine the swell of community—Noah with a megaphone,"
    "Jun's kids with hand-painted placards, Aunt Lila telling her story into a camera until the whole town knows what they stand to lose."

    "Another voice, quieter, threadbare with rumor" "Or the whistleblower."

    mira_santos "There are talks—rumors of contractual easements, of hidden clauses that could let construction override local protections. If someone leaked that, it could unravel the deal."
    "Noah: (low) 'But who has that? Who risks being named? If it goes wrong, it leaves someone exposed to lawsuits. If it goes right, it could stop everything.'"
    "Elias Park rubs his temple. 'Leaks can be decisive. But they're a blowtorch—sets off fires you can't control. And if it's traced back, the fallout could take down people who aren't ready to lose their livelihoods.'"
    hide elias_park
    show aunt_lila_santos at center:
        zoom 0.7

    aunt_lila_santos "You always had to pick whether to be loud or be safe. There is no path that doesn't ask something of you."
    "Your chest tightens in a way that has nothing to do with the humidity—it's the old, constant ache of being asked to choose which part of your life to risk. Each path is a different kind of loss: co-optation, legal warfare, or exposure."

    menu:
        "Lean into Elias' pilot plan":
            "You run a hand over the greenhouse glass, picturing modular turbined roofs and community crews. 'We build it right, with public benchmarks,' you say, trying to fold hope into the sentence."
        "Organize the town for legal resistance":
            "You throw a glance at Aunt Lila and say, 'We rally. We make them fight for every inch.' Your voice carries the strain and the stubbornness that never stops."
        "Chase the whistleblower rumor":
            "You imagine the documents on a table, everything laid bare. 'If we find proof, we strip the mask,' you whisper, feeling the pull of a quick, dangerous truth."

    # --- merge ---
    "Continue to the plaza scene"
    "Elias Park looks at you after each suggestion; his eyes linger on your face as though searching for the woman who once left for grad school and returned with tide charts in her pockets and a harder set to her mouth."
    hide mira_santos
    show elias_park at left:
        zoom 0.7

    elias_park "I can help write the pilot metrics. I can be there as a technical guarantor. But I won't sell out what the community asks for."
    hide noah_rivera
    show mira_santos at right:
        zoom 0.7

    mira_santos "And if we don't propose it, can we stop them any other way? How long before a court process drains us? How long before the public starts to want 'safety' in the version they see in renderings?"
    hide aunt_lila_santos
    show noah_rivera at center:
        zoom 0.7

    noah_rivera "You didn't come back to watch the town sold out in the name of safety."
    hide elias_park
    show aunt_lila_santos at left:
        zoom 0.7

    aunt_lila_santos "You came back to keep the stories."
    "The greenhouse feels smaller, then larger—the way a plan feels when all the people who will have to live in it are suddenly visible."
    # [Scene: Plaza Outside Municipal Hall | Dusk to Night]
    hide mira_santos
    hide noah_rivera
    hide aunt_lila_santos

    scene bg ch3_98c6f2_4 at full_bg
    # play music "music_placeholder"  # [Music: Low, steady pulse; the wind motif returns, insistent but measured]
    # play sound "sfx_placeholder"  # [Sound: Distant amplified voices from a late-night TV van; rain tapping the plaza stones]
    "You step into the plaza. People trade versions of the same news: negotiation. Some are relieved—safety, finally. Others look as if they've lost something already. The air tastes faintly metallic, like incoming weather."
    "Cassandra 'Cass' Whitlock emerges from the hall, her coat buttoned; she passes close enough that you smell her coastal-smoke scent. Her smile is practiced, and when she reaches for a microphone to speak to a cluster of reporters, her words are smooth."
    show cassandra_cass_whitlock at left:
        zoom 0.7

    cassandra_cass_whitlock "We respect Marrow Bay's heritage. Our intent is collaboration. The council's negotiation will ensure all parties have a seat."
    "A reporter asks a sharp question about displacement and easements. Her answer is textbook: reassurance, then pivot to data. The crowd presses."
    "Elias Park stands beside you, silent. When you look at him, his jaw sets; there's a weight there you know—the memory of his failure, the carefulness he treats promises with. His hand brushes yours by accident,"
    "then lingers. There's warmth, and then the taut concern that comes from someone who loves you and fears being the cause of new wounds."
    "His reaction remains complex—an unreadable mix of wanting to help and wanting to protect both you and himself from a repeat of past mistakes."
    "You catch Aunt Lila's eye. She squeezes your hand—an old, fierce blessing."
    show noah_rivera at right:
        zoom 0.7

    noah_rivera "Whatever you choose, it will echo. We can fight in court, in the streets, or in the contracts. Each has a price."
    "You imagine phone calls from anxious neighbors, images of bulldozers, the hush that follows when something irreplaceable is taken."
    "Your internal clock tightens; adrenaline simmers but doesn't boil. Decision time presses like incoming tide—steady, inevitable, shaping everything it touches."
    "You weigh the options in the cold air, reading each like tide lines. The moment stretches thin; you can hear your pulse in your ears."

    menu:
        "Reassure the crowd with practical next steps":
            "You step to a small cluster, hand on Noah's shoulder. 'We'll draft a pilot proposal tonight. We'll invite anyone to add to it,' you say, offering procedure as comfort."
        "Urgently call for a legal meeting":
            "You pull out your phone and say, 'Jun—get me the activist attorneys' numbers. We need counsel.' The motion feels like shoring up a wall."
        "Ask Elias to look into the whistleblower rumor":
            "You lean toward Elias Park, voice low, 'Can you see if there's truth to that rumor?' His face tightens; the risk is obvious, but so is the potential for a quick, decisive reveal."

    # --- merge ---
    "Close on the coral scarf, then lead into the decision point"
    hide cassandra_cass_whitlock
    hide noah_rivera

    scene bg ch3_98c6f2_5 at full_bg
    # play music "music_placeholder"  # [Music: Tense motif swells slightly, then holds on a single unresolved chord]

    menu:
        "Propose a community-led pilot partnership with Elias' prototypes and ask the council to fund a pilot.":
            jump chapter4
        "Refuse cooperation; mount a legal/political campaign to block redevelopment.":
            jump chapter8
        "Pursue (or leak) the whistleblower rumor to expose contract easements and questionable clauses.":
            jump chapter12
    return
