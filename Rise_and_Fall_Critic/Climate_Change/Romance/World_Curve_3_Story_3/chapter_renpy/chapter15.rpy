label chapter15:

    # [Scene: Construction Site | Predawn — Thick Fog]

    scene bg ch13_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Distant, low strings; a single, steady percussion beat underlining your heartbeat]
    # play sound "sfx_placeholder"  # [Sound: Soft slap of boots on steel grating, the distant churn of an engine idling somewhere beyond the mist]
    "Narration: You taste metal in the air — not just the salt and oil, but the coppery tang of nerves. You left the notebook on your kitchen table; its pages feel like a patient accusation. The"
    "choice you made in the dark of your apartment is now carrying you across this site with Elias Novak's hushed breathing a step behind you and Finn waiting at the perimeter like a shadow you can't"
    "quite bring yourself to look at."
    show elias_novak at left:
        zoom 0.7

    elias_novak "If we get caught, it's going to look violent, Maya. They'll make it look like we wanted to hurt people — not stall machines."
    "Narration: He crouches to examine a moored cable, his fingers tracing a seam as if learning how the thing breathes. 'We talk about ethics in meetings; this is different. This is escalation.'"
    "Narration: His voice is a low promise and a warning both. You want to tell him the neighbor's porch light, the way the water learned your house's rhythms, the way the compass at your chest keeps"
    "pulling toward action. You want to tell him that some things don't let you sleep anymore. Instead you breathe salt, and the thread on your wrist pulls like an old habit."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "I know what it looks like. I know what it costs."
    "Narration: Your fingers find the dented compass beneath your shirt, feeling the cold metal like an accusation. 'But the permits keep getting rubber-stamped and the barriers push through the borough where the old folks live. We"
    "tried petitions. We tried petitions and public comment. I'm sick of watching stamps and signatures become walls.'"

    elias_novak "And I'm with you, but —"
    "Narration: He stops, searching your face as if that could translate the math of moral urgency into a safe algebra. 'We need to be smart. Fast isn't brave if it breaks everything that relies on us.'"
    "Narration: His hand finds yours for a fraction of a second, thumb brushing the thin red thread. You can hear the city beyond the cranes waking, gulls somewhere arguing the sky. The plan is small in"
    "execution but big in implication: a half-hour of sleight-of-hand that could slow a project for days. Enough time for petitions to gather steam, for lawyers to breathe. Enough time, you told yourself, to make them listen."

    menu:
        "Leave a marker to claim responsibility":
            "You press a folded leaflet into a cleft of concrete — a slogan, a QR code that points to a manifesto. The paper flutters; Elias Novak's jaw tightens."
        "Leave no trace":
            "You tuck your name and the hatred and the cause back into your chest. No proof. Only stalled machines and the rumor of hands in the dark. Elias Novak nods, relief flickering across his face."

    # --- merge ---
    "Narration continues."
    "Narration: The fog is honest; it hides and it reveals. You slip through scaffolding, the damp of the wood seeping into your pants. Each machine is a small, arrogant planet of hydraulics and cables, low hums"
    "that make your teeth vibrate. Your hands know the tools — hammered pins and stripped connectors, the quiet science of sabotage that isn't violent so much as precise. Finn stands farther off, his silhouette a patient"
    "knock against the horizon, ready to sprint or fetch a car or hold a story together if it all unravels."
    show finn_serrano at center:
        zoom 0.7

    finn_serrano "You sure about this, Maya? You don't have to be the one."

    maya_serrano "You remember Mrs. Ortega's porch? You remember the light?"
    "Narration: You swallow the rest. 'I can't not do something when the options are to wait and let them bulldoze people out.'"
    "Finn: (a short breath) 'Then do it quick. Do it clean.'"
    hide elias_novak
    hide maya_serrano
    hide finn_serrano

    scene bg ch13_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A single pneumatic hiss as a pin drops; then, for a moment, only the breathing of the four of you]
    "Narration: You hammer a loose retention pin until it has the sick, reluctant give that means a joint will no longer bear the load it's supposed to. You pull aside a cable, expose its braided heart,"
    "and splice a short with a piece of copper you wrapped in cloth. The contact is a whisper; the machine answers with a cough, a shudder. For a sliver of a second — long enough to"
    "feel holy and foolish — the site breathes differently. The diesel growl eases to a stunned silence."
    show elias_novak at left:
        zoom 0.7

    elias_novak "There."
    "Narration: He doesn't say 'now' or 'we did it' as if declaring a victory. 'That buys us time.'"
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "For what, though? For headlines? For hearings?"
    "Narration: You slow, because he deserves to know the small cruelty of your optimism. 'If all we get is a day and a press release labelling us vandals, we lose the thing we need most: trust.'"

    elias_novak "I know."
    "Narration: He runs a hand through his hair, making damp strands cling to his forehead. 'But sometimes the only way to get a room to listen is to make the room feel the words. I warned you about escalation. I didn't warn you that I'd help.'"
    "Narration: His laugh has gone thin. You want to pull him close and promise that you'll answer for this, that you'll carry whatever comes. There's time for that later; right now the perimeter lights have flared,"
    "and a distant voice — a megaphone? — throws down a legalese shadow. You hear boots that aren't yours, measured and new."

    menu:
        "Step back and wait for Elias":
            "You retreat a few paces, crucible of adrenaline cooling into an ache. Elias Novak moves with you; both of you are shadows among shadows, watching civilian silhouettes become security."
        "Stay to scrawl a message on the machine":
            "You make your hands write in the wet salt: a single word. It feels petty and necessary. The letters gleam in sodium light like a child's angry scrawl. Elias Novak looks away, and you interpret his silence as a warning you chose to ignore."

    # --- merge ---
    "Narration continues."
    # play sound "sfx_placeholder"  # [Sound: Rapid footfalls; the drone of a vehicle idling; the clipped talk of radios]
    hide elias_novak
    hide maya_serrano

    scene bg ch13_e67f19_3 at full_bg
    "Narration: The private security cuts the air with certainty. They are professional in the way sharks are: efficient, sharp, only interested in closing a wound. A man in a windbreaker with a radio clipped to his"
    "collar approaches, looking at Elias Novak first, then at you as if reading a manifest."

    "Private Security Lead" "This site is closed. You have forty-five seconds to identify yourselves and leave the property."

    "Elias Novak (hands raised slightly)" "We were just — maintenance check. We found a fault."
    "Narration: His voice is practiced conciliatory; it is the voice of a man who knows how to talk to cages without stepping into them."

    "Private Security Lead (narrowing eyes)" "If you were maintenance, you wouldn't be here at four in the morning with tools."
    "Narration: He isn't pretending. 'Stay right there.'"

    "Narration: There's a click as phones bloom to life; someone is streaming, someone is calling a corporate line. A PR handler's voice is calm and crystalline somewhere near the cruise of the site. Within minutes — minutes — Noah Kestrel's corporate account posts" "Sabotage reported at Kestrel Marine Development site. We have notified authorities. We'll update as information becomes available."

    "Elias Novak (rushing, low)" "We need to be careful. If they pin this on us publicly, it's over. The mayor will distance herself. Grants will freeze. People will be scared to be seen with us."
    show maya_serrano at left:
        zoom 0.7

    maya_serrano "They already started the narrative."
    "Narration: Your voice is small against the roar of a machine you didn't mean to provoke. 'They get to choose what we are in the papers.'"
    "Narration: They do. A livestream flickers with a face you've never seen, calling you 'eco-terrorists' into a camera held by someone who is laughing on the inside. Private security's hands are polite but strong as they"
    "take Elias Novak's arm and then yours. Finn tries to step forward and is blocked — his protest is a bark swallowed by the compression of legal authority."

    "Officer" "You're under caution for criminal damage and trespass. You have the right to remain silent."
    "Narration: He reads the phrases like a script. The words are clean; the consequence will be tangled and slow."
    "Narration: Arrest is less cinematic than you thought. There's a compartment for shock — you feel it as if it's practical, then a second of shame. Your wrists clamp, cold metal meeting skin. A camera's red"
    "light glares too bright, and you catch Elias Novak's eye. There's anger there, hurt, and something that looks painfully like guilt."

    "Elias Novak (squeezing through the bars of his mouth)" "I shouldn't have helped. I should never have promised I'd be with you on something that could make the town turn like that."

    maya_serrano "You were there because you cared."
    "Narration: The truth is a stone in your throat. 'You were there because my plan was to make them listen, not to make us lose the moral high ground.'"
    "Narration: The press are vultures in tailored raincoats. Noah Kestrel's press release slides into mayoral statements and then into feeds that shuffle sympathy and contempt with indifferent algorithms. The town's message board, which held neighborly complaints"
    "and bake-sale notices, fills with accusations and fear. People you organized with send messages: some furious, some terrified, some asking you to explain the cost. A neighbor you know well writes, 'Why would you hurt our"
    "chance at funding?' and you cannot answer except to replay the image of water seeping through floorboards and the memory of a porch light gone dark."
    hide maya_serrano

    scene bg ch13_e67f19_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The van's engine idles; a distant gull's cry is swallowed by concrete]
    "Narration: They process you with meticulous cold. A booking shot. A written list of charges. The flashlight finds the scar near your collarbone and holds it up like an exhibit. You tell yourself the law will"
    "be the law; you tell yourself you'll explain in hearings, in courtrooms, in community halls. But the machine of reputation is heavier than you bargained for; funding boards call their lawyers, philanthropic pockets close their purses,"
    "and eager politicians — the ones who stood vaguely in your favor months ago — send carefully worded statements of concern that say nothing."

    "Officer" "You will have a chance to speak to your lawyer."

    "Maya Serrano (to Finn, who stands on the curb like a silhouette of what you refused to leave behind)" "Take everything we can. Save the manifests. Talk to Rosa. Don't let them quiet the town."

    "Finn (voice tight)" "You get through this. We will keep the people together."
    "Narration: His faith feels both like a lifeline and a reproach. In the cell, the concrete smells like rain and old coffee. You think about the neighbor who drowned; you think of the promises knotted into"
    "the red thread on your wrist. Righteousness — fierce and hot — has teeth, but it also bled you. The consequence isn't just the handcuffs; it's the slow, reputational erosion that spreads into grant committees, into"
    "the volunteer roster, into the ability to sit on a dais and speak for those you love. You remember Hana's voice in the lab, saying a plan needs durability and coalition, not just fury."

    "Elias Novak (through the glass as they process him in a separate room, his voice muffled)" "I'm sorry, Maya. I thought—"
    show maya_serrano at left:
        zoom 0.7

    maya_serrano "So did I."
    "Narration: You don't know whether that absolves either of you."
    "Narration: Later — an echo of fluorescent light, a mirror, the slack look of a face you don't recognize — the arrest report lists your previous offences like a moral ledger. The officers are polite, efficient,"
    "without the theatrical cruelty you imagined, which somehow makes it worse. In the waiting hours between being booked and being released on bail, you imagine the long term: grant panels citing 'lack of governance'; a mayor"
    "who cannot be seen appearing beside a convicted saboteur; families who whisper that you put them at risk and turn away from posters and petitions you once led."
    # play sound "sfx_placeholder"  # [Sound: News bulletin tone; a low, public-service chime that means someone's voice has found an audience]
    # play music "music_placeholder"  # [Music: A melancholy piano figure, slow and unresolved]
    "Narration: Outside, the sea doesn't care for legalities. It continues its patient rise — a slow, indifferent metronome. Within the town, the narrative has shifted. You are a headline. Elias Novak is a headline. The work"
    "you thought would save people now threatens to discredit the very networks you need. Your heart, which felt like an engine when you worked the cable, now feels like a ledger with too many unpaid debts."

    menu:
        "Ask to speak at the community meeting right now":
            "You push until a sympathetic officer relents and lets you call Rosa. She promises to hold a meeting but her voice trembles with the weight of new lawsuits."
        "Stay silent and let the legal team work":
            "You clamp your jaw shut and hand your phone to your counsel. The decision feels like leaving the streets to others; it also feels like keeping a weapon sheathed so it won't be misused."

    # --- merge ---
    "Narration continues."
    "Narration: The night closes around small, bureaucratic violences: fines, injunctions, subpoenas. Private security's cameras keep rolling; Noah Kestrel's counsel dispatches an eloquent demand for damages. The town fractures along new lines: those who applaud the action"
    "in whispering corners and those who worry about lost funding and the safety nets that hang by threads. The organizers you once convened at Rosa's café are more hesitant now; their attendance at meetings drops like"
    "a tide receding."

    "Finn (late, at the police station’s frosted window; his face is pale, hands jammed into his jacket)" "They called the foundation. They want an explanation. Rosa is trying to keep people calm, but—"

    maya_serrano "I know."
    "Narration: The words are small and useless. 'I'm sorry.'"
    "Narration: Arrest this time isn't a badge of honor. It is leverage in the hands of institutions that prefer neat narratives and that trade in the slow erasure of messy, inconvenient truths. You had thought sabotage"
    "could be a scalpel — targeted and precise. You didn't account for the surgical tools of reputation and legal power. The wound you meant to inflict on a project has bled into the body that supports"
    "your work: funding, trust, access."
    hide maya_serrano

    scene bg ch13_e67f19_5 at full_bg
    # play music "music_placeholder"  # [Music: A single descending cello note that refuses to resolve]
    "Narration: You lie awake on a cot in a holding room, the thread around your wrist rubbing raw where the cuffs left an impression. You replay the morning: the hiss of the cable, Elias Novak's eyes,"
    "the sudden authority of men with radios. You replay it until the righteous heat cools into a cold, acid clarity: anger without a durable plan can be a self-inflicted wound. It can look like courage to"
    "those who tasted it in the moment, and it can look like vandalism to those who pay the bills."
    "Narration: You imagine grant panels closing their folders. You imagine Hana looking at you, disappointed not because you acted but because you didn't safeguard the long arc. You imagine Saltbridge as a map of small losses"
    "compounded: a mural bought out, a youth outreach program defunded, a rooftop garden shuttered because the paperwork now cites 'liability' in a way that smells like eviction."

    "Elias Novak (his voice distant, through a fax of staticky corridor noise)" "We thought we were steering the story."
    show maya_serrano at left:
        zoom 0.7

    maya_serrano "We were steering with rope and hope."
    "Narration: You let the bitterness be its own kind of truth."
    "Narration: The van comes to pick you up for transfer. The sky has a faint lightening at the edges, the sea a long, indifferent shiver. People line the boardwalk in the early morning like ghosts of"
    "meetings you once held, and some of them look at you with the complicated, unreadable expression people reserve for old friends who have become risks. Finn catches your eye, his mouth a line, and in it"
    "you read steadiness and a question you cannot answer yet."
    "Narration: You press your palms to the glass for a moment as the doors close. You are carted past the cranes, past nicked steel and patched tarps, and you know — with a practical, cold certainty"
    "— that this night will tarnish more than your hands. It will ripple into policy rooms and grant committees, into the quiet places where funds are decided and reputations are weighed."
    "Narration: You wanted to stop the tide with a human hand and a wrench. Instead you have stirred a different current: legal clamps, freezing of accounts, whispers of 'criminality' that will make it harder to bring"
    "people together. The moral clarity you sought has slipped between fingers that are now cuffed. The sky pale behind the cranes seems to ask you, without malice, what you now intend to do with the consequences."
    hide maya_serrano

    scene bg ch13_e67f19_6 at full_bg
    # play music "music_placeholder"  # [Music: A fragile single violin, held, then released]
    "Narration: You have wounded the machine. The machine has found a wound and declared itself the injured party. The town will split; some will close ranks around you in fierce solidarity and others will drift away"
    "like dunes reshaped by wind. You have not yet lost everything, but you have given them a narrative they can use. You have bought time — yes — but at a price that may bankrupt the"
    "trust you need most."
    "Narration: As the van door shuts and the metal click is another kind of punctuation, you let yourself feel the fall fully: the righteous heat cooled into a sober, bitter aftertaste. Outside, seawater makes a slow"
    "claim on the boardwalk. Inside, your hands are quiet with the knowledge that fury is not a plan."
    # play music "music_placeholder"  # [Music: Fade to a single unresolved chord]
    "Narration: Page-turn thought: You wonder which will hurt more in the long run — the machines left idle for a week, or the long, grinding erosion of credibility that could leave the vulnerable without the very advocates who once stood at their doors."

    scene bg ch13_e67f19_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter16
    return
