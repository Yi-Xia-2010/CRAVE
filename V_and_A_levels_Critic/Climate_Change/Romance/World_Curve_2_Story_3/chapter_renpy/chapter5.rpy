label chapter5:

    # [Scene: City Hall Hearing Room | Late Afternoon]

    scene bg ch5_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense, rapidly building strings with a steady electronic pulse]
    # play sound "sfx_placeholder"  # [Sound: Murmurs, microphone clicks, the distant thump of footsteps on stone]
    "You walk in on a tide of faces. The room smells like paper, coffee, and the metallic tang of too many hands—public business compressed into a single, overheated hour. Your coral scarf is a knot under"
    "your collar; it feels small and stubborn against the clamor. You let your gaze skim the crowd and catch familiar profiles: Lina, hands clenched at her knees; Tamiko with a camera phone raised, already live; Dr."
    "Arun at the edge of the aisle, palms folded like a ritual."
    "The projector blinks a municipal rendering across the far wall—glass towers glimmering above a straight, pale seawall—Cassian's polished fantasy made into civic gospel. You taste it: the sweetness of slick promises, the bitter aftertaste of trade-offs."
    "You have been here before, but never with the room this full. The city feeds hum overhead; citizens, reporters, contractors, and the board. At the front, Elias Moreno stands beside the municipal planner's lectern. His blazer"
    "is folded into a high-visibility vest when on site; today it's a thin linen thing that looks like it doesn't belong in the glare. His jaw tightens in a way you haven't seen since the last"
    "public meeting. He meets your eyes for a fraction longer than comfort allows—pleading, a question, and defiance stacked together."
    show mira_santos at left:
        zoom 0.7

    mira_santos "Elias."
    show elias_moreno at right:
        zoom 0.7

    elias_moreno "I'm ready."
    "You inhale, and the moment fractures into motion."
    hide mira_santos
    hide elias_moreno

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A moderator's gavel raps once; the room hushes into an anticipatory silence]
    "Elias Moreno steps up. His voice is tighter than before, the edges of it carved by pressure and the knowledge you pushed him here."
    show elias_moreno at left:
        zoom 0.7

    elias_moreno "Members of the council, people of Verdante—there are procedural irregularities in the procurement for the Vale Consortium's proposal that we can no longer treat as clerical error."
    "He lays out specifics with a practiced cadence: timelines compressed, bid documents routed through an intermediary, waiver requests that skirt community commitments. He names the guarantees you demanded—tenure protections, phased relocation plans, legally binding community oversight—and he asks the council to commit."
    "Your chest drums. Each point is an incision; each demand is a marker. The room responds—some with nods, others with tight mouths. Cameras angle in closer."

    menu:
        "Stand and clap when Elias names the guarantees":
            "You rise as if pulled by rope. The clap you give is clumsy but full; around you, a ripple of approval swells. Elias sees you and for a heartbeat relaxes."
        "Keep your hands folded and watch Elias":
            "You keep still, not wanting to break the thread of his voice. Your silence feels like an anchor; Elias catches your stare and something like gratitude flashes through his eyes."
        "Pull out your notebook and scribble objections":
            "Your pen scratches rapidly—legalese and contingency plans. It steadies you; Tamiko glances over and smirks, as if your lists are a private shore map in the chaos."

    # --- merge ---
    "Elias tightens his grip on the podium."
    "Elias Moreno tightens his grip on the podium."

    elias_moreno "We ask the council to pause any final approvals until these irregularities are investigated—and to enshrine the guarantees as conditions of award. We deserve enforceable commitments before contracts are signed."
    "A ripple of sound—cheers from the benches near Mariner's Row, murmured protests from the developer seats, a reporter's pen scratching like rain. You can feel the energy spike. The microphone picks up the hiss of a thousand breaths."
    "Then the back doors open."
    # play sound "sfx_placeholder"  # [Sound: Door whooshes; the room's temperature seems to drop an inch]
    hide elias_moreno

    scene bg ch5_4001e7_3 at full_bg
    "Cassian Vale moves in, ice-blue eyes sweeping the room as if cataloguing outcomes. He offers the smile of a man who has never been surprised by the sea."
    show cassian_vale at left:
        zoom 0.7

    cassian_vale "Ah—Mr. Moreno. Such theatrics. I would have thought better of a city planner."
    show elias_moreno at right:
        zoom 0.7

    elias_moreno "This isn't theatre, Cassian. It's procedure."

    cassian_vale "Procedure is for paper. People need protection. My proposal protects people—efficiently. Delay is luxury Verdante can't afford."
    "You feel something in the room tilt—an axis that divides intention from power. Cassian's voice is smooth; his words have the weight of capital."
    "Tamiko moves like light. Her livestream ticks on, framing Cassian's entrance, then zooming in on a document she waves at the camera—an LLC registration with a name that changes hands like shells in a child's game."
    "Her feed speaks in a different language than the council's minutes—a language of the public square."
    show tamiko_sato at center:
        zoom 0.7

    tamiko_sato "Watch this. There's a shell company tied to Vale's bid—no direct owners listed, purple filings that reroute through offshore accounts. I'm uploading everything."

    menu:
        "Watch Tamiko's live feed on your phone":
            "You turn your phone into a tiny lighthouse. The names scroll like a ledger of ghosts. Your stomach drops when you see the shell's pattern. Tamiko catches you looking, and her eyes say: 'We found it.'"
        "Focus on Elias' exchange with Cassian":
            "You keep your focus on the men at the front. Tamiko's camera is peripheral light; the blow of this fight must happen here, now. Elias' jaw tightens; he thanks you with his eyes."
        "Call Lina a quick word under your breath":
            "You lean in and whisper—'Be ready.' Lina's nod is sharp as flint. Her hands move, palms hiding a plan you can already hear in the streets."

    # --- merge ---
    "The hearing continues with Cassian and Elias trading positions."

    cassian_vale "If you're worried about opaque ownership, there are legal avenues. But I won't let grandstanding—or theatrics—slow down protection for thousands."

    elias_moreno "We are not grandstanding. We are demanding transparency and enforceable protections so the people who live here are not erased in the name of expediency."
    "Cassian Vale's smile becomes something colder."

    cassian_vale "What you call erasure, I call triage. You can stand here and fight me for the theater of it—and risk the funding—or you can withdraw your obstruction and let this proceed at the pace it needs."
    "The room hums like a wire. Cameras jab at faces; phones go red with comments. A faction of officials shift in their seats; their worry is a visible thing—calculators in their eyes."

    "Council Member" "Mr. Vale—Mr. Moreno—this is not the forum for ultimatums. We need process, not posturing."

    elias_moreno "This isn't an ultimatum—this is an appeal to the council's responsibility. If we approve without guarantees, we—"
    "Cassian Vale cuts him off with a polite, slow shake of his head."

    cassian_vale "Or you can withdraw. Or I can pursue a private funding model that accelerates construction and bypasses oversight. The choice is simple."
    "A gasp. Someone laughs nervously. Your heart hammers against the reef of your ribs. The room's arousal tightens into a coil—this is what you feared: the threat, the choice framed as inevitability."
    hide cassian_vale
    show dr_arun_patel at left:
        zoom 0.7

    dr_arun_patel "If he can sidestep oversight, the social costs could be immense—displacement on a scale we can't backfill."
    "Lina leans forward, jaw set."
    hide elias_moreno
    show lina_cortez at right:
        zoom 0.7

    lina_cortez "Then we stop him. We don't let him ship us off like cargo."
    "Tamiko's livestream bursts into a chorus of outrage and hashtags. The shell-company thread begins to trend locally; phone screens sprout like small, incandescent windows across the room."
    "Elias Moreno glances at you. For a moment you see the map of the day—your pushing, his risk, the tightrope. He looks like a man who has calculated the cost and still decided to pay."
    hide tamiko_sato
    show elias_moreno at center:
        zoom 0.7

    elias_moreno "Was that—too far?"
    hide dr_arun_patel
    show mira_santos at left:
        zoom 0.7

    mira_santos "We needed someone to name it. We needed someone to put it on record. We didn't start this for spectacle—we started it to make sure we stop the erasure."
    "Elias Moreno nods, but the tremor in his hand is visible now. A municipal aide whispers to him; a thicker envelope lands at his side—an internal memo, thin and lethal."
    # play sound "sfx_placeholder"  # [Sound: A clerk clears her throat; a notification tone—official reprimand—hardly more than a ding, lands in Elias' name]
    hide lina_cortez
    hide elias_moreno
    hide mira_santos

    scene bg ch5_4001e7_4 at full_bg
    "The reprimand is procedural but exacting: jeopardizing procurement flows; endangering funding timelines; initiating reputational risk. The words are cold instruments that cut margins from his future. You watch as the room recalibrates—supporters look deflated, officials look"
    "relieved someone else will carry the burden of decision, and developers watch options bloom like marketable widgets."
    "Cassian Vale watches Elias with the satisfaction of a man watching a wave fold."
    show cassian_vale at left:
        zoom 0.7

    cassian_vale "I offered protection. You chose disruption. The city will not reward recklessness."
    "Tamiko's thread widens; she posts ownership documents with annotated highlights. Commentators pick at the threads like scavengers; some see corruption, some see conspiracy, some see opportunity. The public reaction is volatile—cheers and jeers collide; the heat of the crowd is visible in the quick pacing of conversations."
    "You stand on a narrow island of certainty in a sea of pressure: calling out Cassian matters—and the cost is now on Elias' shoulders."
    "Lina, ever immediate, moves before thought has had a chance to negotiate fear."
    show lina_cortez at right:
        zoom 0.7

    lina_cortez "They're staging equipment at the north lot tonight. If we move in, we delay them."
    show mira_santos at center:
        zoom 0.7

    mira_santos "A blockade? That's arrestable. Some neighbors will refuse—"

    "Lina (cutting you off)" "Some neighbors will refuse if we let them bulldoze our history, too."

    menu:
        "Support Lina's blockade plan outright":
            "You find your voice is sharpest when you say yes. Your agreement is a spark; it spreads. A handful of neighbors nod; others tighten. Tamiko grins, thumbs already texting out coordinates."
        "Tell Lina to hold off until we assess legal exposure":
            "You pull back, naming the risk in the room. Lina's eyes flash with impatience but she doesn't argue—she trusts you enough to hear you. The pause lets a few more skeptical neighbors breathe."

    # --- merge ---
    "Conversation fractures into clusters; the coalition begins to splinter."
    "Arguments fracture into clusters. Some of your coalition—older residents worried about fines, renters afraid of lost housing vouchers—step away, their faces strained with practical fear. Tamiko bellows into the camera; Dr. Arun quietly calls a contact at the ethics board. Elias stands between the machinations, small and exposed."
    "Elias Moreno is called outside the hearing room by a stern-faced deputy. He returns less composed. A city communications officer approaches with a carefully neutral tone and a hand that trembles invisible directives."

    "City Communications Officer" "We will open an ethics review. These things can take time. In the meantime, we suggest cooling rhetoric."
    hide cassian_vale
    show elias_moreno at left:
        zoom 0.7

    elias_moreno "You called attention to the procedural issue. We need action, not stalling."

    "City Communications Officer" "Action takes process."
    "It's a phrase that slams like a door."
    "Cassian Vale leans forward, finality in his posture."
    hide lina_cortez
    show cassian_vale at right:
        zoom 0.7

    cassian_vale "Withdraw public opposition, or I speed up a privately funded bid. No oversight, expedited construction. Opportunity costs, yes. But protection delivered."
    "The ultimatum lands like a thunderclap. The room convulses."
    "You feel the coalition splinter under the stress—fractions of loyalty rearranging into survival strategies. The neighbors who need certainty lean toward expediency; the activists who cannot bear displacement lean toward confrontation. You look at Elias and"
    "see the immediate, sharp cost of the move you pushed him into: a reprimand, a cloud on his career, and a fracture between the public good and procedural constraint."
    "Your hands tighten into fists around your scarf; the fabric scrapes the skin of your palm."

    mira_santos "You did this to protect people. You did this because silence would have been complicity. But now the price shows itself. You hear it in the way funding conversations have become threats."
    "Elias Moreno meets your eyes—something unreadable passes between you, heavy and small as a stone. He is shaken, not by the public eye, but by the institutional wheels that grind any dissent into collateral."

    elias_moreno "I—I'm sorry. I thought—"

    mira_santos "I know. I know why you did it."
    "He flinches, as if the simple knowledge is at once balm and salt. Around you, the room organizes itself into new lines. Calls for a pause, for legal counsel, for immediate negotiation—voices stack, some pleading, some calculating."
    "Lina's blockade plan is already humming across Tamiko's feed. The idea of direct action blooms in the streets; some people cheer, others mourn the loss of consensus. You feel the coalition fracture palpably—your phone vibrates with private messages: support, fear, anger, resignation. The strain is a living thing."
    "Dr. Arun places a hand on your shoulder—warm, steady."
    hide mira_santos
    show dr_arun_patel at center:
        zoom 0.7

    dr_arun_patel "The ethics review will drag. That is the system's way of delaying. Be careful about what you promise people tonight."
    "You look at Elias again; his face is a ledger of decisions made and futures mortgaged. The reprimand sits in the air like a verdict. Cassian's ultimatum hangs like high tide: inevitable, threatening, immediate."
    hide elias_moreno
    hide cassian_vale
    hide dr_arun_patel

    scene bg ch5_4001e7_5 at full_bg
    # play music "music_placeholder"  # [Music: Strings peak then splice into percussive, unresolved stabs]
    # play sound "sfx_placeholder"  # [Sound: Phones ringing; Tamiko's live feed cuts to a stylized overlay of documents; a gavel pounds faintly in the distance]
    "You press your palm to your scarf, feeling the loop of it—comfort, memory, duty. The hearing has become a spectacle that cost more than you imagined. It bought accountability and left a scar."
    "You stand in the middle of it, the point where policy and people collide, and feel the fracture widen—a personal toll cleaving trust into small, sharp pieces."

    scene bg ch5_4001e7_6 at full_bg
    # play music "music_placeholder"  # [Music: A single, held piano note lingers; then silence, expectant and heavy]
    "You want to say everything: that you did it because the people you love matter; that institutions often prefer delay; that Cassian's calculus is not compassion. But words feel brittle. All you can do is watch the room rearrange itself around threat and strategy."
    "The aftershocks begin: whispered plans, legal threats, an ultimatum that smells of money and inevitability."
    # [Page-Turn Moment]
    "You step back from the mic, from Elias' side, from the front line. Behind you, the hearing spirals into a thousand responses—some loud, some strategic, some resigned. Outside, the city breathes in a storm of decision."
    "You keep your scarf, folded and familiar, and for the first time in days, you feel a loneliness that is not the absence of people but the absence of agreement. The protection you demanded has a cost; accountability has a price. The neighborhood is alive with motion—and with fracture."

    scene bg ch5_4001e7_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter7
    return
