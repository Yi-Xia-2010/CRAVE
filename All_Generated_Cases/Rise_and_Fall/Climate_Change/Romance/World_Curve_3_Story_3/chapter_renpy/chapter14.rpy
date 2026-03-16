label chapter14:

    # [Scene: Community Greenhouse & Seed Bank | Morning]

    scene bg ch13_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low murmur of conversation, tin kettle clinking, distant gulls]
    # play music "music_placeholder"  # [Music: Gentle, rising acoustic motif]
    "You wake to the greenhouse breathing around you: humid and earthy, a perfume of damp soil and citrus basil that fills the small room like a promise. The emergency sirens hummed through the night and then"
    "quieted; you remember leaning into a phone call with Ayla until the morning hours, pausing the heavy machines and arranging a partial evacuation that kept as many people as possible safe without abandoning the town entirely."
    "That decision still sits in your chest, neither light nor unbearably heavy—more like a stone you have learned to hold with both hands."
    "Rita is already there, apron streaked with potting soil, pinning handwritten index cards to seed trays. Around a long folding table, neighbors have circled: fishermen with callused fingers, two elderly women who run the bread stall,"
    "a teacher with a stack of crayons and flyers. Someone has brought coffee; it smells sharp and real. Your tablet buzzes in your jacket pocket but you set it face-down. Today is for listening, for patching"
    "trust with small, certain stitches."
    show rita_ortega at left:
        zoom 0.7

    rita_ortega "You're finally awake. Come on—people will think you fled to the rooftop and never came down again."
    "She teases, but her eyes are soft."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Not fleeing. Prioritizing basil."
    "You pinch a leaf and the scent blooms between you."

    maya_reyes "Who brought the lists?"

    rita_ortega "Arlo did his best. We split them by street. We need volunteers to check on elderly renters and prioritize retrofit kits. People will trade labor for materials if we run the co-op right."
    "You run your thumb over the tide-watch at your wrist—its brass warm, its tick a reminder that choices are measured by hours as much as moral weight. You feel the town's attention like weather: fluctuating, patient,"
    "and sometimes sudden. You were the one who called for the pause; you are also the one most of these people look at when the ledger needs a keeper. That double role is tiring but it"
    "is honest labor."

    "Neighbor Miguel (late-40s, harbor-smell woven into his jacket)" "Maya—"
    "He corrects himself, then smiles."

    "Miguel" "—we need your models. Not the whole Excel war, but what to look for when we pick what to shore first. Can you…can you show us?"
    "You step to the whiteboard, palms still tracing the faded wood grain. You speak slowly, translating probabilities into plain language."

    maya_reyes "Start with foundations that let water pass without taking walls. We can reinforce, we can raise thresholds. We can't make everything hurricane-proof overnight, but we can stop the slow rot—insulate wiring, replace sheetrock near the floor, secure fuel and meds."

    "Miguel" "And the funds?"

    maya_reyes "We stitch them together. Small grants, the cooperative fund—people trading labor, plus the legal clinic sorting leases so tenants can claim repairs without eviction."
    "You look at Rita."

    maya_reyes "We make it communal, not charity."
    "Rita nods, the lines around her mouth softening. 'That's how we keep people here without forcing them to sell their memories.'"

    menu:
        "Sign up to door-knock personally":
            "You squeeze Miguel's hand and write your name on the top slot. Your chest tightens with responsibility, but seeing the bright, relieved look on Arlo's face makes it feel like the right weight."
        "Delegate door-knocking to Arlo and coordinate logistics":
            "You hand the list to Arlo, who swallows his nerves and nods. For a second you feel the old urge to take everything back, and then you don't—because trusting him feels like growing a root."

    menu:
        "Accept Ayla's public endorsement at the next council meeting":
            "You decide transparency is your ally. You ask Ayla to speak at the council with you. Her statement is brief, but it carries the weight of policy and the warmth of someone willing to be held accountable."
        "Keep Ayla's help behind the scenes; present the co-op as grassroots":
            "You craft the message so the town's voice is center stage. Ayla signs the documents and leaves quietly. There's a purity to the image you present—people see only neighbors helping neighbors, and that strengthens trust."

    menu:
        "Ask Elias to teach you the next repair session":
            "You lean in and ask him to show you the clamp technique. He grins like it's a date and hands you the plane. The simplicity of working beside him—touching the same splintered wood—feels like reclaiming an easy kind of love."
        "Offer to organize the materials logistics while he teaches":
            "You promise to keep nails and varnish flowing. He nods, relieved. You get to be useful in a different way; it's strange and pleasing to have a role that doesn't demand you fix everything yourself."
    "THE END"
    # [GAME END]
    return
