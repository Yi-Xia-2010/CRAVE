label chapter11:

    # [Scene: Rooftop Gardens | Dusk]

    scene bg ch11_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Gentle, ascending acoustic chord with soft hand-drums]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the hush of recycled irrigation, occasional murmur of passing carts]
    "You press your palms into damp soil and let the cool give under your fingertips. The beds are small miracles tonight: basil and chard that refused to die through the last blackout; a row of sprouting"
    "beans wrapped in twine. Each plant feels like an argument against the idea that everything here must be surrendered."
    "Theo crouches across from you, headlamp tilted, his breath fogging in the coastal air. He taps a tablet with a thumb that still smells faintly of coffee. Asha hums as she secures a rain-collection tube, humming"
    "a cadence you recognize as the same rhythm she used for market setup. Elias 'Eli' Maren is nearby, kneeling as if he is watering an audience; his sleeves are rolled to the elbow, the skin on"
    "his forearms freckled and salt-kissed."
    "You run your thumb over the braided leather at your wrist and feel the weave of decisions tightening into a pattern. The rooftop thrums with small successes—neighbors who've kept food on their tables, elders who slept"
    "through last night's generator sputter because of a redistributed power bank, a child who learned to water a bed and laughed like it was sunlight. The ledger of wins is counted in breakfasts, in the quiet"
    "of an elder's house that held through the night."
    "Rosa's voice arrives as a text, then as footsteps: she came down to check on the seedlings before they closed. Her scarf smells of damp fish and lemon oil; she stands at the edge, hands folded, the rain catching on the braid she's always woven into her hair."
    show rosa_calder at left:
        zoom 0.7

    rosa_calder "You put my father's net on the fence like a flag.' (She doesn't scold; the words arrive slow, as if testing for the right weight.) 'Is memory only what stays in the place, Maya? Or can it go with us when the tide takes the boards?"
    show maya_calder at right:
        zoom 0.7

    maya_calder "Memory travels with people, Ma. It travels in the songs we sing and the recipes we keep. But I don't want to decide that for everyone."
    "Rosa's jaw tightens. For a heartbeat you read complexity in her face—relief, fear, the ghost of stubborn pride. She looks at the beds as if measuring how much of home they might hold."

    rosa_calder "My hands remember how to fix a hull and how to skin a stew pot. If the boards go, will they still recognize this as us?"

    maya_calder "They'll recognize you. And we'll carry the rest. But I hear you—I'm trying to make a world where we don't have to only carry the ashes."

    menu:
        "Hold her hand":
            "You reach and fold your fingers into hers, feeling the weathered knots of her palm. She squeezes back, something unspoken passing between you."
        "Point to the beds":
            "You gesture at the green islands. 'Look at what won't leave.' Rosa watches a sprout for a long beat before she nods, slow and private."

    menu:
        "Promise to steal nights off with him":
            "The promise is bright and easy-sounding. Eli's smile returns like he can exhale. You file it gently, knowing promises will need renegotiating."
        "Ask him to hold you to a day off a week":
            "Eli's eyes sharpen with practical tenderness. 'Deal,' he says, already listing ways to keep you honest—book a gig, hide your calendar, make soup like clockwork."

    menu:
        "Build long-term coalitions to influence policy from the ground up.":
            jump chapter12
        "Prioritize immediate evacuations and relocation support for the most vulnerable.":
            jump chapter12
        "Step back slightly to nurture my relationship with Eli and model balanced leadership.":
            jump chapter15
    return
