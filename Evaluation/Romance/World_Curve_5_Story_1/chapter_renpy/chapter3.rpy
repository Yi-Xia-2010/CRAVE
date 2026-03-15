label chapter3:

    # [Scene: Civic Rooftop Garden | Indigo Dusk]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm, hopeful strings with a steady pulsing undercurrent]
    # play sound "sfx_placeholder"  # [Sound: Low murmur of a gathered crowd; wind through dried ornamental grasses; distant gull cry]
    "You climb the last worn step with the satchel heavy against your hip and the town folded behind you. The evening smells of wet wood, compost, and salt—familiar as breath. Lanterns wink awake in a deliberate"
    "rhythm, casting soft pools of light across muddy boots and damp coats. The crowd is larger than you feared: neighbors in raincoats, old fishermen with caps pulled low, teenagers leaning on concrete ledges, and the faces"
    "you alone came to steady — Tomas, Maya, Linh, Kai. Your fingertips go to the silver band at your throat. It taps the undercurrent of your guilt, then settles."

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Microphone static, then a steadying hush]
    "You clear your throat, listen to the hush catch like a net, and then speak."
    show aria_marin at left:
        zoom 0.7

    aria_marin "Thank you for coming. Tonight isn't about any single fix. It's about what we can do together — the combinations of craft and care that keep people here, and keep what makes Salthaven Salthaven."
    "You watch them read the plan off your face before you lift a hand to the printed timeline: terraced living shorelines to slow erosion, community-led buyouts for the most vulnerable, job-training for local labor, and a"
    "small protected cultural district mapped from oral histories. You do not offer it as a perfect sheet, but as a scaffold — something that holds long enough for people to build on."
    show dr_linh_pham at right:
        zoom 0.7

    dr_linh_pham "We've modeled outcomes at three scales. Living shorelines reduce wave energy and buy time for neighborhoods that can't be relocated cheaply. We can start in the marsh fringe, measure, then adapt. It's not mutually exclusive with engineered protections — it's complementary."

    "Maya (pressed forward, voice bright)" "And we archive what matters. Murals, old docks, the stories in Tomas's walking stick — they stay in our plan as reasons to keep fighting."

    "Elder Tomas (voice rough like rope)" "We've buried enough houses to know what the sea takes. We don't need more elegant promises. We need work we can trust."

    menu:
        "Look directly at Kai Solano":
            "You lock eyes with him; his jaw tightens and heat travels behind his earnest amber gaze."
        "Scan the crowd for wavering faces":
            "Your eyes find a young couple with a toddler and an older woman with a rain-cured face; your resolve steadies at the sight."

    # --- merge ---
    "Narrative continues"
    "You feel Kai Solano as if his presence were a physical tide. He leans forward, elbows on his knees, hands folded as if ready to throw them into the sea to haul something back."
    show kai_solano at center:
        zoom 0.7

    kai_solano "That's a plan. It reads like patience. We don't have patience. We have a construction site digging where our people still sleep. If we don't stop the Arcology tonight, the ground will be stirred, the piles driven, and the displacement will start before anyone's 'pilot' has measured anything."

    aria_marin "I'm not asking for patience as an excuse. I'm asking for a way to avoid making the same mistakes we've made before — decisions that strip neighborhoods without giving people options."

    kai_solano "Options are for people with options. Most folks here are on the line already. Direct action changes the cost calculus. If the developers see we won't let them build, they'll have to back down."
    # play sound "sfx_placeholder"  # [Sound: A ripple of agreement from a corner of the crowd; a scattered cheer]
    "Noah Vega appears at the edge of the light as if he stepped into the frame from someplace clinical and bright. His weatherproof blazer is the color of a calm ocean before a storm; his tablet"
    "throws a cool face of schematics into the blue. He carries the calm of someone used to charts and deliverables."

    "Noah Vega (polite, measured)" "Aria, Kai — everyone. The Arcology, as currently proposed, presents a rapid way to restore the town's economic spine. A seawall, designed and built to the latest standards, could protect the low-lying commercial strip and fund the redevelopment of affected lots. It isn't a panacea, but it reduces immediate risk and creates jobs."
    "Murmurs split first like gulls over water, then like the town itself: some nod toward Noah Vega — the language of jobs and timelines is persuasive; others tighten at the word 'seawall' as if profanity had been spoken."
    "Aria Marin (internal): You see both of them — Kai Solano, who will not wait while people lose their homes; Noah Vega, who can mobilize capital fast. Both want the town safe. Both are blunt instruments"
    "aiming at the same sore. Your chest tightens at the thought of choosing a tool over a person. Compromise, you think, should be a craft, not a surrender."

    menu:
        "Ask for one minute of silence to hear all voices":
            "You raise a hand and the rooftop quiets; in the silence you hear a distant gull, the creak of a lantern line, and the small sounds of waiting. It buys you the breath you need."
        "Invite a show of hands for immediate blockade support":
            "Your question ripples outward; a dozen hands shoot up, then a dozen more — the night is ready to become motion."

    # --- merge ---
    "Narrative continues"
    "Dr. Linh steps in, fingers tapping a tablet, eyes quick with data and care."

    dr_linh_pham "The models say phased pilots allow learning and community oversight. If we pilot living shorelines with workforce training contracts for local crews, we build capacity and evidence. But — and this is important — pilots are slow when people face immediate threats. We need safety measures in the interim."
    hide aria_marin
    show elder_tomas_quay at left:
        zoom 0.7

    elder_tomas_quay "We balance memory and survival. Protect what must be held and give the people who'll lose most a seat at the table."

    "Kai Solano (edge sharpening)" "A 'seat' doesn't stop excavators. Are we voting to tell crews to stand down tonight?"

    "Noah Vega (cool)" "Excavation schedules can be paused if we negotiate terms that secure the project and the town. A seawall, responsibly built and scaled with cultural setbacks, limits immediate flood risk. It's not charity; it's a binding contract that assures insurance and businesses return."
    hide dr_linh_pham
    show aria_marin at right:
        zoom 0.7

    aria_marin "Binding contracts that leave people houseless don't bind the next generation to this place. Binding contracts that build living infrastructure with community labor do."
    "Kai Solano slams his palm to his thigh. His voice rises without becoming unmoored."

    kai_solano "Then help us build that binding contract tonight. Support us at the Arcology. Close the site. Block the machinery. If we don't stop them physically, the rest is paperwork."
    "Noah Vega curtly taps at his tablet, brings up renderings that show an elevated promenade, retail spaces, a clean-cut seawall that would lift the downtown by meters."
    hide kai_solano
    show noah_vega at center:
        zoom 0.7

    noah_vega "Or we choose a scaled, engineered approach. It brings immediate structural protection and a budget to fund buyouts for those displaced. We can institute cultural protections in the redevelopment plan. It's the pragmatic route."
    # play music "music_placeholder"  # [Music: Strings swell with hopeful resolve; underlying pulse quickens]
    # play sound "sfx_placeholder"  # [Sound: A single board creaks; someone nearby exhales]
    "You feel the crowd divide like a high tide slicing a sandbar — not violent, but definitive. Faces on either side of you hold different kinds of conviction: furious, fearful, resigned, hopeful."
    "Aria Marin (internal): The guilt that lives in the back of your ribs tightens. Every time you've sought consensus it has felt like both your duty and your burden. You were the planner hired to make"
    "choices that mattered; you were the one who left once and returned with tools. Now people look at you to translate ethics into deliverables, grief into schedules. You want to be both brave and fair; both"
    "are heavy to carry."

    "Maya (voice small and fierce)" "Aria, if you stand with the people tonight, we will be louder — but we need protection for those who can't march. If you choose the room, some of us will be left in the rain."
    "You step forward, palms open. You want to be something that will hold all of them. Your voice is steadier than your inner scramble."

    aria_marin "This isn't about me picking sides to save face. It's about how we choose to act so that fewer people are harmed. I need to hear what we can do right now to prevent immediate displacement and what we can commit to — in writing, enforceable, transparent — to protect culture and livelihoods."
    hide elder_tomas_quay
    show kai_solano at left:
        zoom 0.7

    kai_solano "So? Will you stand with us?"

    noah_vega "Or will you let me negotiate terms that lock protections in legally?"
    "You look from one to the other. Both faces are honest in their ways. Both believe that their route is the path to saving Salthaven. The rooftop feels like the hinge of the town: if you shift one way, momentum follows."
    hide aria_marin
    hide noah_vega
    hide kai_solano

    scene bg ch3_98c6f2_3 at full_bg
    # play music "music_placeholder"  # [Music: Quiet hopeful chord holds, then opens slightly like a tide revealing more shore]
    "You sense that whatever you decide will change the months to come — who builds with you, who protests against you, who sleeps with the least certainty."

    "Aria Marin (internal, rising): Hope, you realize, is not the absence of conflict. It's the belief that conflict can be turned to craft. Your mouth forms the word you’ve been practicing" "compromise."
    "Your throat tightens. The crowd waits. The air is expectant."
    # play sound "sfx_placeholder"  # [Sound: A soft, unified intake of breath from the rooftop; somewhere a child fidgets]
    # play music "music_placeholder"  # [Music: Strings swell to a warm peak]
    "You stop — not because you don't know the stakes, but because you must choose the shape of action that will define the next move. The plan, the people, the town — they hinge on this one decision."
    "You now face the fracture in the crowd and the question of how to respond."

    menu:
        "Support Kai’s direct action tonight and bring the town into the streets.":
            jump chapter4
        "Open a private negotiation with Noah and offer concessions.":
            jump chapter8
        "Propose a hybrid pilot that combines living shorelines and a scaled wall while delaying construction.":
            jump chapter12
    return
