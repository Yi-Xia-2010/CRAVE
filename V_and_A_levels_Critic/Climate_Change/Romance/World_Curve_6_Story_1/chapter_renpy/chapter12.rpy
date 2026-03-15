label chapter12:

    # [Scene: Municipal Hall Atrium | Morning]

    scene bg ch9_d28f2f_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low murmur of reporters, a distant clock; the vending machines whir]
    # play music "music_placeholder"  # [Music: Sparse piano, steady and minor]
    "You stand near the glass wall and feel the city pressing at both sides of the pane: the ocean beyond, the machine of government inside. Air-conditioned breath meets salt-warm skin on your neck. Your hands are"
    "folded around the binder like a talisman; the pages inside smell faintly of ink, rain, and other people's hope."

    "Someone near the display feed has queued the corporate spot again — the same cut that plays like a vein in a wound: a flooded transit tunnel, a child's school closed, a voiceover asking a single question in gravelly certainty" "How many lives are you willing to risk before you act?"
    "You taste copper and coffee. Your pulse is not a drumbeat of panic; it's a steady, working rhythm. This is what you expected: fear is a tool. You'd hoped the human stories you carried would be louder. Hope is quieter, but you have learned how to make it persistent."

    scene bg ch9_d28f2f_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A faint, collective intake from a crowd outside the hearing room]
    # play music "music_placeholder"  # [Music: A single cello line threads under the scene — melancholy, patient]
    "Rafi appears at your elbow, soil under his nails, eyes bright in that exhausted way he gets when he's mobilized an entire street. He presses a hand into your shoulder."
    show rafi_odeh at left:
        zoom 0.7

    rafi_odeh "They're running the scare reel on loop. They've chartered vans to pull swing voters. Mayor's getting calls from— (he shakes his head) —from fund managers."
    show maya_corvin at right:
        zoom 0.7

    maya_corvin "We knew they'd go there. We knew they'd make it about tomorrow's nightmare instead of today's choices."

    rafi_odeh "Still—seeing it on a loop like that, it lands. (He looks at you, pleading for a sentence that will steady him.) Are you holding up?"

    maya_corvin "I am holding up. For now."
    hide rafi_odeh
    hide maya_corvin

    scene bg ch9_d28f2f_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Footsteps approaching; a clip-on mic pops]
    # play music "music_placeholder"  # [Music: The cello softens]
    "You catch Lio in the crowd, paint-splattered hoodie a bright comet against the gray suits. He gives you the quick, fervent nod you trained him to give whenever words were too much. Behind him, neighbors clutch flyers and thermoses, making the municipal marble feel like a temporary Low Row."
    # [Scene: Low Row — Canvassing Corner | Midday]

    scene bg ch9_d28f2f_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant ads through phones; a child laughs; the slap of a flyer onto a neighbour's door]
    # play music "music_placeholder"  # [Music: Acoustic guitar, minor key, steady tempo]
    "This is where fear meets flesh. You stand on a stoop and speak to someone who's already spent their last flood-savings on a patched roof. You talk about wetlands, about the marshes' capacity to take a"
    "storm's first hunger. You speak of research, of the seedlings Rafi started this spring, of the way a living shoreline buys seasons."

    "Woman on stoop" "But the ad—my brother works at the port. They said if they delay, the harbor will—' (her voice breaks) '—my rent, my sister's meds."
    show maya_corvin at left:
        zoom 0.7

    maya_corvin "I'm not asking you to risk what you need. I'm asking you to consider a plan that reduces risk without taking away what you can't afford to lose."
    "She studies your face like it's a map. Her hands shake. You can smell curry and sea salt on her sleeves; her eyes are rimmed with a warning that hope cannot drown fear easily."

    menu:
        "Show the neighborhood footage of the pilot's flood reduction":
            "You pull up the clip: mud, seedlings, neighbors hauling bags. Her jaw tightens as she watches familiar faces. 'If this could keep the market open—' she says, the sentence unfinished."
        "Talk about the economic trade-offs and municipal amendments":
            "You run through the amendment's language slowly, pointing to the clause that guarantees compensation. Her shoulders relax a fraction; the word 'compensation' lands like a small, cold coin in her palm."

    # --- merge ---
    "You finish your block and move on, the city folding you into its living mosaic. Each conversation is an appeal to a different kind of self-preservation; each one leaves a small residue in you, like salt on a mouth."
    # [Scene: Municipal Hall — Mayor’s Office Corridor | Afternoon]
    hide maya_corvin

    scene bg ch9_d28f2f_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A phone abruptly hangs up; muffled arguments through closed doors]
    # play music "music_placeholder"  # [Music: Low synth underscoring, patient and precise]
    "Mayor Velez meets you in a narrow corridor under the city clock. Her scarf is bright against a suit that bears the map of cautious decisions. She has a printed timeline in one hand and a fatigue that looks like responsibility in her face."

    "Mayor Velez" "Maya. I want you to know this — you've forced a conversation. That's civic muscle.' (She places the timeline between you, presses lightly.) 'But the exchanges are spiking. We are watching bond yields. Investors are nervous. I cannot pretend the city's stability isn't part of my mandate."
    show maya_corvin at left:
        zoom 0.7

    maya_corvin "You can also watch the people who will lose the most if we harden the shoreline without compromise."
    "Mayor Velez: (sighs) 'Yes.' (She meets your eyes.) 'I need language that protects heritage plots, that leaves corridors for wetlands. I'm carving it in, but you have to understand — carved language can be ground down in committees.'"
    "You press your thumb to the trefoil on your wrist beneath your sleeve, feeling its small, familiar burn."

    maya_corvin "Then stoke the committees with people who won't treat wetlands as an optional annex."

    "Mayor Velez" "I'll do what I can. But I have an administration to run. If the market decides to pull capital, I have consequences that don't fit neatly into a petition."
    "There is no cure-all in her words, only a ledger and the human consequences she must carry."
    # [Scene: Polling Station — Early Morning. Lines Forming | Voting Day]
    hide maya_corvin

    scene bg ch9_d28f2f_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The shuffle of ballots, a bell that marks an hourly turnout check]
    # play music "music_placeholder"  # [Music: A metronomic piano pattern, steady]
    "Turnout is heavier than anyone predicted. The line snakes down the block; the city has answered the call to decide. You stand on a raised step and watch faces — young parents, a port worker with a callused hand, elderly neighbors who remember the promenade before it shifted."
    "A local reporter corners you with a recorder. Her phone shows the corporate ad in one window and your petition footage in another; both play like competing hymns."

    "Reporter" "Maya, the polls show a surge for the seawall after last week's spot. How do you respond to voters who say this is about immediate safety?"
    show maya_corvin at left:
        zoom 0.7

    maya_corvin "I say safety is not only concrete. It's the soil that feeds us, the nursery that feeds our children. We are arguing about the types of safety we want to live under."

    "Reporter" "But if the projections are right—"
    "Maya Corvin: (interrupting) 'Projections are not inevitabilities. They are tools for planning. Fear does not plan.'"

    menu:
        "Offer the reporter a scientist's projection and data packet":
            "You hand over Sima's cleaned model and some neighborhood metrics. She reads, nodding; the corner of her mouth tightens with respect that looks like reconsideration."
        "Invite the reporter to visit the nursery after polls close":
            "You extend an invitation instead. She hesitates, an eyebrow lifting. 'That might make a better piece,' she admits."

    # --- merge ---
    "Each ballot fed into the box feels like a small, precise act — a civic heartbeat. The advertisements keep playing on thin screens tucked into people’s palms, and in between the images are families, livelihoods, ballots folded and handed with hands that tremble for different reasons."
    # [Scene: Municipal Hall — Results Center | Evening]
    hide maya_corvin

    scene bg ch9_d28f2f_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low commentary, a public address system counting precincts; the hum of fluorescent lights]
    # play music "music_placeholder"  # [Music: A cello returns, lower, more insistent]
    "You watch the margins tighten. The social feeds litter the screens with hashtags and heated commentary. It feels less like a debate and more like two architectures of fear trying to occupy the same mind."
    "Mayor Velez stands nearby, her hands steepled. Her face drains as the final precinct tallies in."

    "Election Official" "By a margin of—' (he clears his throat) '—0.8 percent, Nueva Mar votes to approve the NuevaGuard Seawall Initiative."
    "The room beads with a silence that is raw and immediate. It's not dramatic; it's administrative. A line on a spreadsheet has been drawn. Yet the line moves like a blade through the neighborhood you taught yourself to defend."
    "You hear a neighbor's muffled sob to your left. Lio's jaw works; he looks smaller, as if the paint on his hoodie cannot cover this particular kind of loss. Rafi shuts his eyes and leans his forehead on his fist as if to press the ache back inside."
    "Mayor Velez: (softly) 'We will push for mitigation corridors. We'll demand protected wetland allotments in the plans. We'll apply for emergency funds for those displaced.'"
    show maya_corvin at left:
        zoom 0.7

    maya_corvin "You will try,"
    hide maya_corvin

    scene bg ch9_d28f2f_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A construction siren faint in the distance, like a promise turned toward work]
    # play music "music_placeholder"  # [Music: A low sustained note]
    "Elias Kahn appears at the edge of the monitors. There is a hollow I have felt before when research fails — when models are read as excuses rather than instruments. He meets your eyes without immediately"
    "stepping forward. When he does, there is a distance as if he's leaning across a table you cannot see."
    show elias_kahn at left:
        zoom 0.7

    elias_kahn "Maya.' (He sounds older, like the city has weighted his words.) 'I thought there might be another outcome."
    show maya_corvin at right:
        zoom 0.7

    maya_corvin "So did I."

    elias_kahn "I—' (he pauses, choosing the words that will make the least damage he can) '—I have accepted a seat on the oversight committee the Mayor offered. I can keep an eye on the mitigation corridors. I can make sure the wetland allotments are enforced."

    maya_corvin "Is that staying, or is that distancing?"
    "Elias Kahn: (a quiet laugh, then not) 'It keeps me close to the center. It's…an inside position. My work will be procedural, long. It will take me away from hands-on projects. I thought you knew that might be a risk.'"

    maya_corvin "I didn't expect you to retreat into the room where decisions are edited while the shore itself is being changed."

    elias_kahn "This is policy. It is how things are made binding.' (He meets your gaze; for a second there is a vulnerability like a raw wire.) 'If I can put language into the ordinance that protects living corridors, I will. I don't want to be the person who says I could have done more."

    maya_corvin "And if the language is chewed away in legal wrangling?"

    elias_kahn "Then we'll burn it back into the record with audits and oversight. That's how institutions bend."
    "His words are steady but not warm. There is a new tautness between you — like a rope pulled taught. You feel the knot of disappointment, an almost physical tightening. Elias isn't abandoning the cause entirely; he's choosing a different battlefield. It feels like compromise to some, retreat to others."
    hide elias_kahn
    hide maya_corvin

    scene bg ch9_d28f2f_9 at full_bg
    # play music "music_placeholder"  # [Music: The cello recedes, leaving a single note]
    # [Scene: Corporate Seawall Construction Site — First Shovels | Two Weeks Later]

    scene bg ch9_d28f2f_10 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The thump of pile drivers, a chorus of radios, gulls circling above]
    # play music "music_placeholder"  # [Music: Low, mechanical rhythm — inevitability]
    "You stand on the fringes, hands pressed into each other to keep from reaching for anything. Wet concrete smells like metal and rain in the wrong season. The sound of the first pour is not cinematic; it's utilitarian. It is efficiency made audible."
    "Workers cordon off a stretch that used to host a string of rooftop nurseries. There is a wooden shrine there, painted with a small mural Lio did last year — a blue heron and handprints. The"
    "crew moves a barrier through it like a silencer. Something very small and private is boxed by orange netting."
    "Camila 'Kai' Navarro is on site, headset snug, a tablet in hand. She moves with a clarity that is almost unforgiving; orders are numbers, and numbers are action. For a moment, she pauses before the mural."
    "The pause is a breath like a hand on a window, and you almost—almost—see something behind her steel-gray eyes."
    show maya_corvin at left:
        zoom 0.7

    maya_corvin "Kai."
    "Camila 'Kai' Navarro: (without turning fully) 'Maya.' (Her words are efficient.) 'This section is necessary. The stress models show this compromise reduces risk to the port and main electrical conduits.'"

    maya_corvin "It sacrifices a living nursery."

    "Camila 'Kai' Navarro" "We are planting compensatory green belts inland. It's not ideal, but it reduces probabilistic exposure."

    maya_corvin "You call that a reduction? You cordon off people who have nowhere to move."
    "Camila 'Kai' Navarro: (her jaw tightens) 'I don't make the residents relocate. I enact protection for critical infrastructure. If the infrastructure fails, more people will be displaced.'"
    "There is a crease at the temple where her forehead flexes. For a flash she reaches up and fingertips something hidden beneath her collar — a porcelain pendant that catches light like a small, secret moon"
    "before she covers it again. It is an image of the kind of tenderness you rarely see in her gestures, and it flies across her face like a private weather system."
    "Camila 'Kai' Navarro: (softer) 'I am not blind to what this takes. I wish there were no choices that hurt people.'"
    "Maya Corvin: (quietly) 'Then why do your choices always make it someone else's hurt?'"

    "Camila 'Kai' Navarro" "Because the scale is different to me.' (Her voice is blunt but not cruel.) 'I can't justify letting a key grid fail on the logic of sentiment."

    maya_corvin "Scale doesn't make people less real, Kai."
    "She looks at you for a long moment, and there is the sense of two engineers measuring different things on the same ruler. Her eyes flick to the mural; her shoulders shift as if she has"
    "momentarily decided something small — a delay to the barrier placement — then signs into a call and directs the crew to proceed. The small softness is swallowed by the operational schedule."
    hide maya_corvin

    scene bg ch9_d28f2f_11 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Concrete curing; a distant child crying; Lio's voice singing an old Low Row song in a low, steady tone]
    # play music "music_placeholder"  # [Music: Single, mournful violin emerges]
    "Back in the Low Row, people load what they can into trucks. Some insist on staying; some accept relocation stipends and leave with chins set. Rafi organizes a vigil — candles on the promenade, a circle"
    "of voices reciting names of lost inlet plots. You light a thin candle and feel the flame tremble with the same breath you've been breathing all season."

    "Lio paints that night under sodium light — a new mural, this one a ledger of things lost and a promise scrawled in paint" "We will remember."
    "You walk the edge of the cordoned wetland and press your palm to the netting. The salty air pulls at the net like fingers. Your sense of loss is not cinematic; it is accumulated — a"
    "thousand small absences: the hum of a greenhouse gone, the smell of earth replaced by drying concrete, the murmur of elders recounting where we used to fish."

    scene bg ch9_d28f2f_12 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The sea muffled by the new barrier; an elm leaf skids across a sand-blown pavement]
    # play music "music_placeholder"  # [Music: The music falls to a single, long note — a held breath]
    "You fold the petition again, because some gestures outlive their political power; some signatures are anchors for memory. The binder is lighter now, emptied of an outcome that mattered more than the act of collecting names ever did."
    "You think of Elias moving toward closed committee rooms, bound to bureaucratic patience. You think of Kai's hand, quick and clinical, touching her pendant like a talisman she doesn't want anyone to see. You think of"
    "Rafi's hands stained with soil, with grief, with the need to keep planting even as the ground changes."
    "Your chest tightens not with the heat of immediate panic but with a slow, gathering grief that feels like a tide you cannot hold back."
    # [Page-Turn Moment]
    "You stand at the lip of the promenade, watching the concrete edge rise like an answered prayer twisted between salvation and erasure. Somewhere beyond the construction lights, the ocean keeps doing what it always did. Here,"
    "human hands have chosen a line. The rest — the negotiation, the lawsuits, the seedlings planted inland, the compensated plots, the vows of oversight — will follow in quiet administrative motion. The public chose fear's promise"
    "of quick protection; the city obliged. You have opened the debate, and that is not nothing. But tonight the Low Row's skyline is different: some roofs are gone, some faces have left, and where a herd"
    "of nursery pots once clustered, there is a measured, newly poured lip of concrete."
    "You breathe in the tang of wet cement and salt and, for a moment, let it fill you until the grief becomes something like a map—sharp, unarguable lines you can follow. The next move is not"
    "a single decision. It will be the work of years: documenting losses, fighting for corridors where they can be saved, keeping warm the small lights of resistance. The ache catches and holds, and in it you"
    "feel a new, terrible clarity: the city's future will be decided by the people who show up every time the tide rises."

    scene bg ch9_d28f2f_13 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter15
    return
