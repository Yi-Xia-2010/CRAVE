label chapter5:

    # [Scene: Community Rooftop Garden & Meeting Hall | Dawn]

    scene bg ch5_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Gulls wheel; distant engines of a news van settling into the lot below; the muffled clink of shovels and laughter from the boardwalk.]
    # play music "music_placeholder"  # [Music: Urgent strings under a bright, hopeful brass motif — tempo quickening]
    "You wake to gulls and the small electric hum of a phone that won't stop buzzing. Your shoulders complain from the pilot planting — a corporeal memory of salt and dirt — and your field notebook"
    "rests like a warm stone against your ribs. Outside the rooftop, Lina is already converting panic into schedules: she moves like someone with a map burned into her palms, clipboard in hand, voice cutting through the"
    "garden like a bell."
    show lina_kwon at left:
        zoom 0.7

    lina_kwon "Two-hour shifts, tops. Rotate the kids through weeding after noon; Priya, can you vet the waiver drafts for the minors? Mateo wants a volunteer list he can hand to the co-op."
    "Priya Anand steps closer, binoculars still swinging at her throat, a small stack of legal templates tucked under one arm. The paper slides against your thumb when she hands you one: neat clauses, funding contingencies, a box for matching funds. Her smile is quick, ally-ready."
    show priya_anand at right:
        zoom 0.7

    priya_anand "We can fast-track the permit language if we scope the pilot areas clearly. The NGO can front the application fees, but they'll need a matching commitment from municipal coffers or private donors within thirty days."
    "You scan the template — clauses that smell faintly of bureaucracy and hope. The rooftop tastes of wet soil and coffee, sunlight collecting on your knuckles where the mud dried. The crowd below thickens; you can"
    "feel the town's momentum as a weight and an upward push in your chest. This is not a whisper anymore; it's a chorus."
    "Aiden Reyes arrives with that wind-ruffled hair and a thermos that looks like it's seen three winters. He drops into an empty crate, boots thumping, eyes scanning the rows of seedlings as if he can read their future by the tilt of their leaves."
    show aiden_reyes at center:
        zoom 0.7

    aiden_reyes "You look like you slept in a pile of Spartina and won.' (He grins, then his expression sharpens, careful.) 'How's the volunteer roster?"
    "You trade a look — long enough that something private warms the space between you and the world. It's a look you both can hold and let go of; outside, everyone else needs different kinds of holding."
    hide lina_kwon
    show maya_kwon at left:
        zoom 0.7

    maya_kwon "Packed. Lina's split-shift genius is in effect. Priya's ready with legal drafts, but the NGO wants matching funds soon. Vernon & Crow are feeling the heat—news vans are already circling."

    aiden_reyes "Good. Momentum's our currency.' (He hesitates, then lowers his voice.) 'Maya — about planting lines near the north channel. The older fishers are nervous. If we close that strip off, nearshore nets get crowded and fathers like Mateo will—' He stops himself. 'We have to keep them working."
    "You feel the urgency in his words like a quick current. He cares, and that care curls under your ribs like a second tide. You know — in the exact geometry of memory and anger and"
    "love — that what you do with the marsh will touch his hands as much as the town's ledger."

    menu:
        "Offer to walk the channel with him right now":
            "You hand him your thermos and you both step down from the rooftop together. The air between you is pungent with wet salt; you listen to the channel slosh and plan placement as a team."
        "Promise to meet after the Vernon & Crow visit":
            "You squeeze his hand, quick and steady, and tell him you'll meet once you hear what Elara proposes. He nods, a little wrenched, and goes to check on the kids."

    menu:
        "Call Elara on the marsh tongue — insist on a field review":
            "You kneel and point out the exact beds and shrines; Elara frowns, then bends, and for a suspended breath she listens to the mud. It changes the tenor of the pitch into negotiation."
        "Ask Priya to draft a conditional MOU that ties any contract to strict habitat protections":
            "Priya nods sharply and starts tapping into her tablet. The idea of legal guardrails steadies your shoulders; you feel tactical and fierce."

    menu:
        "Double down on community labor—no contractors; scale slowly, keep control local.":
            jump chapter7
        "Accept a contractor-assisted pilot to scale quickly under NGO oversight.":
            jump chapter15
        "Negotiate a targeted berm to preserve dock access while planting further out.":
            jump chapter17
    return
