label chapter9:

    # [Scene: Promenade | Night — Storm]

    scene bg ch9_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind keens; rain hammers wood; a distant siren warps with Doppler tremor]
    # play music "music_placeholder"  # [Music: Jagged strings, percussion like falling gravel — a relentless, high-tempo pulse]
    "You are still leaning over the radio when the first surge hits real and terrible. Rain becomes a sheet; the promenade blurs into a smear of motion and light. Volunteers shout into one another's faces. Sandbags"
    "peel apart where hands slacken; a board pops and slaps like a gunshot. You taste metal and the tang of sea in your mouth."
    show jonah_mek at left:
        zoom 0.7

    jonah_mek "Pumps are holding on Promenade. Fountain Street—might be—' (he swallows) '—might take water if we don't divert more."
    show maya_soren at right:
        zoom 0.7

    maya_soren "Tell me where. Name it. I'll send a crew."

    jonah_mek "Between the old bakery and Rami's stoop. Two families with ground-level basements. Rosa's alley could go under if the eastern flap fails."
    "The name Rosa pulls you like a hook. You picture her stoop, her braids threaded with sea-grass. Her seed packets folded into a wet hand. Your chest tightens into a remembered compromise — the garden you had to move once, the promises you never stopped paying back to yourself for."
    hide jonah_mek
    hide maya_soren

    scene bg ch9_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Aboard voices overlap: orders, prayers, the low moan of tidal pressure]
    "Elias Voss finds you and stays there, shoulder to shoulder, soaked through but unbroken. He smells of diesel and kelp, and his eyes are bright with a kind of desperate determination."
    show elias_voss at left:
        zoom 0.7

    elias_voss "Kelp cages are holding in the cove. The boxes flexed into the trough; surge dropped by—' (he rattles off numbers like a litany) '—thirty-two percent at the mouth. It bought us time."
    "You let the number settle; it's a thin mercy. Kelp boxes are an experiment—your signature, his hope—but the cost to neighborhoods felt very real. You can see the calculation already: how many pumps diverted, how many lives balanced on that percentage."

    menu:
        "Hand your jacket to the shivering volunteer":
            "You peel off your soaked softshell and drape it over a trembling shoulder; hands linger, a wordless comfort."
        "Direct volunteers to feed the pumps first":
            "You bark a command; a chain of motion forms — wrenches turn, belts engage, a pump coughs to life. The volunteer nods, marshaled into work."

    # --- merge ---
    "Proceed to Scene: Cove (Kelp Boxes) | Night — Sheltered, thunder distant"
    # [Scene: Cove (Kelp Boxes) | Night — Sheltered, thunder distant]
    hide elias_voss

    scene bg ch9_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Water slapping plastic; the creak of moorings; quick shouted counts]
    # play music "music_placeholder"  # [Music: High tempo strings mix with a low electronic hum — the heartbeat of equipment]
    "You run to the cove because you have to see the thin miracle with your own eyes. The kelp cages flex where the surge meets the engineered beds. Diver lights stitch through green water. Elias Voss moves like he always does — hands sure, voice an anchor."
    show elias_voss at left:
        zoom 0.7

    elias_voss "We lost one tether on the northern box, but the mesh held. If we can keep the southern brace, the cove bleeds less into the quays."
    show maya_soren at right:
        zoom 0.7

    maya_soren "How many failures until it's a spill?"

    elias_voss "Two more failures and we lose the containment line. We won't. We won't."
    "You watch divers haul a sprung strap, skin slick with salt. The cove exhales an anxious, halting relief. The temporary engineering bought space — and space is where people live."

    menu:
        "Wade in to help secure a strap":
            "Cold bites you; you get a handhold and feel the live, raw pull of water under your feet. For a heartbeat you are just muscle and will."
        "Coordinate from the edge, calling out tolerances":
            "You map tolerances into orders; numbers become a scaffold for hope. The divers execute, and the strap bites home."

    # --- merge ---
    "Proceed to Scene: Lower Quay — After the Surge | Pre-dawn, the air shudders cold"
    # [Scene: Lower Quay — After the Surge | Pre-dawn, the air shudders cold]
    hide elias_voss
    hide maya_soren

    scene bg ch9_3be532_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A baby crying from a soaked mattress; a dog barking at a lost scent; low murmur of people counting what remains]
    # play music "music_placeholder"  # [Music: A single mournful cello line under distant percussion — grief condensed to a note]
    "The water recedes at dawn and leaves a different world. Streets are canals with furniture islands. A flour sack clings to a porch rail. A poster for the summer market flaps, trailing salt. Some neighborhoods are"
    "intact—raised walkways and reinforced pumps did their job—but others are hollowed out with a sudden, bureaucratic absence: doors locked against water, windows boarded, families standing with garbage bags of everything they could salvage."
    "Rosa Calder stands on her stoop, small and fierce, handing out thermoses. Her hands are knuckled and warm. When she sees you she does not throw you a blessing. She gives you a look that measures debts."
    show rosa_calder at left:
        zoom 0.7

    rosa_calder "We kept green for years, Maya. We fed the children with what we grew. They said your plan would keep us whole. Half the block's gone."
    show maya_soren at right:
        zoom 0.7

    maya_soren "I know.' (The answer is a sandpapered thing; it does not close the wound.) 'We will make this right. I will make it right."

    rosa_calder "Words are cheap when the earth takes your floorboards."
    "Jonah steps into the narrow street, boots sucking at silt. He places a hand on Rosa's shoulder like a bridge."
    show jonah_mek at center:
        zoom 0.7

    jonah_mek "What matters now is the next day. Maya, what are we giving them besides promises?"
    "You look at the tally of losses — basements ruined, nursery packets gone, memories soaked into boards. The ledger in your head stacks like a pile of names. You think of the old compromise that cost"
    "a garden and the way guilt has lived around your ribs like a stone since."
    # [Scene: Temporary Relief Tent | Mid-morning — Damp canvas, steam from kettle]
    hide rosa_calder
    hide maya_soren
    hide jonah_mek

    scene bg ch9_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The scratch of pens, muffled sobs, the low, insistent hum of conversation]
    # play music "music_placeholder"  # [Music: Low, insistent percussion; tension close to breaking]
    "Asha Reed finds you at the assistance table, elbows on a crate, eyes rimmed with water and indignation. Around her, members of the coalition catalog damage with the cold efficiency of people who have been wronged before."
    show asha_reed at left:
        zoom 0.7

    asha_reed "They say 'temporary defense' and then the temporary becomes their permanent. People get moved in the name of safety and never see their stoops again."
    show maya_soren at right:
        zoom 0.7

    maya_soren "You know I never wanted that. We deployed what we could to save as many as possible."

    asha_reed "As many as possible still leaves margins of dispossession. Those margins have names."
    "You feel the old ledger — the community garden you moved, the elders who lost seeds — fold into the present as accusation and as motive."

    maya_soren "We will write something enforceable. Reparations. Direct assistance. Priority housing. And—' (Your voice tightens) '—a rotating seat on the council, one with veto on displacement decisions, held by this coalition."
    "Asha Reed's mouth hardens. For a long breath she looks at you, unreadable, the Schrödinger weight of what might have been and what is now. Her coalition has scars. Trust is not given; it must be wrested."

    asha_reed "A seat isn't a promise unless the seat can stop you from making the same mistakes. Veto power. Clear metrics. Community oversight on where funds go."

    maya_soren "You get veto power, conditional oversight, and a community trust fund audited quarterly. Full reparations to households that lost primary residences, relocation grants, and a commitment to prioritize rebuilding over commercial buffers."
    "There is a pause where everything in the tent holds its breath. Elias Voss stands behind you, rain still in his hair, palms splayed as if to catch falling things. He looks at Asha Reed, then at you, an expression that is humbled and frightened all at once."
    show elias_voss at center:
        zoom 0.7

    elias_voss "If we set the fund, we also set a monitoring protocol. My team can help with transparent sensors, public data streams. No shadow science."

    asha_reed "I want community auditors, not your tech-reporters. We don't want surveillance masked as transparency."

    maya_soren "We will design it together. Community auditors first, tech feeds second. Whatever we take from the sea, we give back to the street."
    hide asha_reed
    show jonah_mek at left:
        zoom 0.7

    jonah_mek "And the families who have to relocate—temporary homes, guaranteed right of return if safe, plus compensation for lost businesses."
    hide maya_soren
    show rosa_calder at right:
        zoom 0.7

    rosa_calder "Don't let it be words this time, Maya."
    "You feel the room flex toward a fragile agreement — not victory, but an architecture of accountability. Each concession is a clean-cut bruise. The pain is real. The trust you build is knotty and slow."

    menu:
        "Tell the assembly you will personally oversee the disbursements":
            "You promise your hand on the ledger; people lean in, small hope glinting like a shard. It binds you tighter to the work."
        "Propose a citizens' trust committee to manage funds without your sole oversight":
            "You push responsibility outward; some nod in relief, others frown—no single scapegoat, but also no single shepherd. The load spreads."

    # --- merge ---
    "Proceed to Scene: Promenade — Public Assembly | Late Afternoon — Makeshift dais, wet flags"
    # [Scene: Promenade — Public Assembly | Late Afternoon — Makeshift dais, wet flags]
    hide elias_voss
    hide jonah_mek
    hide rosa_calder

    scene bg ch9_3be532_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A thousand small conversations, coughs, the occasional whispered name]
    # play music "music_placeholder"  # [Music: Tension mounts — horns swelled under a tight string section; heartbeat drums]
    "You are given the dais because you organized the emergency response. People look to you as to an axis. Some faces are familiar; others are strangers whose homes have become a different geography. A woman you"
    "don't know stares at you with the expression of someone who knows exactly what it is to have the floor go out from under her feet."
    "You inhale the sharp salt air and let the city's weight settle on your shoulders. The plan is assembled on paper: reparations schedule, rotating council charter, monitoring protocols, immediate housing vouchers. It's bureaucratic and human and ugly and necessary."
    "Asha Reed steps forward, the coalition's shadow at her back. She does not yield the stage. She does not need to. This is not a handover; it is a negotiation with an audience."
    show asha_reed at left:
        zoom 0.7

    asha_reed "We have watched systems fixate on counting things while people are counted out. We will not be sanitized away in the name of safety."
    show maya_soren at right:
        zoom 0.7

    maya_soren "We will not let the system sanitize you."
    show elias_voss at center:
        zoom 0.7

    elias_voss "And we will keep doing the sea work — but under the oversight you demand. Where engineering helps, it will help on your terms."
    "The crowd mutters. Some nods are sharp, others are skeptical: relief laced with the sweat of distrust. You feel the gravity of everything you've held to get to this moment — the compromises, the nights of"
    "calculations, the faces of those who will not be able to rebuild on the same blocks."
    "You open the binder and read the pledge aloud — slow, precise, legal and human wrapped together. Each clause lands like a plank placed over a gap."

    maya_soren "Immediate reparations: emergency funding within seventy-two hours. Guaranteed temporary housing for displaced households. A community trust overseen by rotating seats; this seat will have a binding veto on displacement decisions for the first two years. Funds audited quarterly and published publicly. The kelp-restoration project will continue but with community-led environmental assessments."
    "A hush follows, like an ocean taking a breath."

    asha_reed "And the right of return?"

    maya_soren "Guaranteed when the neighborhood is safe and rebuilt under community stewardship. Preference given to original residents for rebuilding plots."
    "Rosa Calder steps forward when you are finished, small as a reed but steady."
    hide asha_reed
    show rosa_calder at left:
        zoom 0.7

    rosa_calder "Make it binding on the ledger. Not a memo, not a promise, something that can't be folded away."
    "You nod and draft the final paragraph in your own hand. Your signature will be a ledger of culpability and care."
    # play sound "sfx_placeholder"  # [Sound: A distant rumble — not thunder this time, but the hull of the city as pumps cycle and crews work]
    # play music "music_placeholder"  # [Music: String dissonance resolves a fraction; a low, unresolved chord persists]
    "The crowd murmurs; some clap tentatively, some remain silent. Elias Voss takes your hand and squeezes. You feel the warmth like a returned current. But the relief is thin, carved through with loss. You cannot pretend"
    "the neighborhoods who lost their floors are fully whole. You cannot pretend your hands are not stained by past pragmatisms."
    "Asha Reed eyes the contract and then you. There is an exchange in the small space between them — terms counted and matched, distrust measured and weighed until it fits."
    hide maya_soren
    show asha_reed at right:
        zoom 0.7

    asha_reed "We accept on the condition that community auditors have the power to pause projects they deem potentially displacing, and that affected families are prioritized in rebuild grants."
    hide elias_voss
    show maya_soren at center:
        zoom 0.7

    maya_soren "Agreed."
    hide rosa_calder
    show jonah_mek at left:
        zoom 0.7

    jonah_mek "And you're offering—' (he looks to the listeners) '—a rotating seat on council with a two-year guarantee."

    maya_soren "Yes. A seat, rotated annually among coalition members, with real oversight. We will codify this into the municipal charter."
    "Voices rise. Some cheer because they finally have leverage; some cry because they thought leverage would never come. The palette of the scene is bruised and raw — victory braided with loss."
    hide asha_reed
    hide maya_soren
    hide jonah_mek

    scene bg ch9_3be532_7 at full_bg
    # play music "music_placeholder"  # [Music: The percussion drops away, leaving a single sustained violin note carrying both hope and grief]
    "You are about to sign."
    "Everything in you tightens — the old compromise, the displaced garden, the families with fewer thresholds to call home, the kelp saved and the shorelines compromised. The city has been rerouted; people have been moved. You"
    "have brokered a structure to repair and to prevent future erasures, but there are names and empty stoops that cannot be unwritten."
    "You close your eyes for one quick, impossible second. The storm's aftermath is a ledger of what you could save and what you couldn't. You think of the baby that cried in the flooded night, of Rosa's hands, of Jonah's steady presence, of Elias's stubborn faith."
    "You place the pen's tip to paper."

    scene bg ch9_3be532_8 at full_bg
    # play music "music_placeholder"  # [Music: A single, high string pierces the air — a note both sharp and final]

    scene bg ch9_3be532_9 at full_bg
    "THE END"
    # [GAME END]
    return
