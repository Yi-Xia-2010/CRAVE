label chapter2:

    # [Scene: Kade Resilience Lab | Morning]

    scene bg ch2_c4ca42_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft hum of climate-control systems; occasional beep from sensor arrays]
    # play music "music_placeholder"  # [Music: Quiet, hopeful strings underscoring the sense of momentum]
    "You step into someone else's future and feel the difference in the air: the cool, filtered light; the faint metallic scent of ozone; the calculated, humming confidence that always smells like decisions already made. Your waterproof"
    "notebook is tucked under your arm, the braid on your cuff brushing the frayed seam as if to steady it. Around you, donors in muted suits nod at animated projections; a half-dozen local residents stand clustered"
    "by the wall, damp coats clinging to their shoulders."
    "Dr. Sienna Kade stands at the front, immaculate in her pale-gray blazer. The bob of her hair is a straight line; her presence is a hinge on which this whole room seems to turn. When she speaks, digits slide across the screens like tides obeying a new law."
    show dr_sienna_kade at left:
        zoom 0.7

    dr_sienna_kade "This rapid seawall, deployed in phases over eighteen months, reduces projected inundation by eighty percent for the commercial corridor. It secures investment, protects critical infrastructure, and—crucially—saves years of economic disruption."
    "Her voice is even, persuasive. Charts bloom behind her—cost curves, modeled storm surges collapsed into neat, reassuring lines. A few donors exchange pleased smiles and the soft clink of coffee cups. Some council members lean in; the lab notes it as a victory in motion."
    "You read the room the way you've learned to read a tide: where it will break, where it will spare, and where it will swallow. Your eyes trace those glowing line items until one thing stands"
    "out by its omission. The models account for cargo flow and tax base; they do not account for the smell of drying nets, for Rosa's late-night repairs, for the informal markets that keep your neighbors fed"
    "when the trawlers don't go out. There is no line for cultural memory, no buffer for livelihoods patched together with hope and odd jobs."
    "A hand taps your shoulder. Theo—ginger hair perpetually ruffled, a hoodie with coffee that has graduated into a permanent stain—hovers with a tablet, the screen tilted like a confession."
    show theo_baines at right:
        zoom 0.7

    theo_baines "Look at the calibration on Node Seven. They've got the storm surge dampening set to regional averages. Local bathymetry shows—a half-meter difference when you factor pier-induced currents. That shortens the safety margin."
    "You lean in, smelling Theo's stale espresso and the soft warmth of his concern. Numbers are not abstract to him; they're the language he trusts when words feel too human."
    show maya_calder at center:
        zoom 0.7

    maya_calder "Half a meter is huge for low-lying lanes. If the model smooths it out, they could be overpromising safety where it matters most."

    theo_baines "Exactly. And there's a weird offset in the wave attenuation parameter. Either it's a simplification for public consumption, or—' (he gives you a look) '—someone smoothed it on purpose."
    "Dr. Sienna Kade finishes her slide to a round of approving murmurs. She scans the room, and for the smallest fraction of a second her steel-gray eyes catch yours. The expression is unreadable—polished, contained—then gone. That"
    "quick look feels like a stone tossed across the surface of what you're trying to keep calm."

    dr_sienna_kade "We can move on procurement next quarter, assuming approvals. Questions?"
    "Hands lift. A resident asks about temporary relocation during construction; the answer is technical and insulated with policy language. You feel the pull between what is efficient on a map and what is messy and human here, in blinking, living color."

    menu:
        "Interrupt the Q&A and point out the calibration to Sienna":
            "You stand, your voice steady, and point to the Node Seven discrepancy. The room shifts—some irritation, some curiosity—as Dr. Sienna Kade's expression narrows. She responds carefully, but you sense the beginnings of an argument that will pry open assumptions."
        "Hold back and ask Theo to compile a short brief to distribute after the meeting":
            "You close your mouth and ask Theo for the brief. He nods, relieved; you feel the small, patient satisfaction of a plan taking shape. The meeting proceeds without public friction, but the data will travel the room in a different, quieter way."

    # --- merge ---
    "Theo gives you a look that says, without words, good choice, and you tuck that into your notebook—figures, footnotes, the small strategies that let people hold onto homes without being bulldozed by certainty. You watch Dr."
    "Sienna Kade answer carefully-phrased questions, the rhetoric of years saved rolling off her tongue as if it were a balm. The donors like that balm. A few local faces remain bewildered, not because they don't care,"
    "but because this language doesn't translate to their daily lives."
    "Theo gives you a look that says, without words, good choice, and you tuck that into your notebook—figures, footnotes, the small strategies that let people hold onto homes without being bulldozed by certainty. You watch Dr."
    "Sienna Kade answer carefully-phrased questions, the rhetoric of years saved rolling off her tongue as if it were a balm. The donors like that balm. A few local faces remain bewildered, not because they don't care,"
    "but because this language doesn't translate to their daily lives."
    "After the meeting, the lab's corridors smell of warmed metal and recycled air. You and Theo sit at a high table under a glowing map. He pulls up an alternate projection—one you both sketched in late at night, when optimism still tasted like possibility."

    theo_baines "Community-run green infrastructure—rain gardens, permeable kiosks, rooftop micro-reservoirs—shifts local drainage curves enough to matter. Not eighty percent in all places, but it preserves livelihoods and reduces displacement risk."

    maya_calder "It won't impress the donors the same way a wall does. It isn't neat on a balance sheet."

    theo_baines "No. But it's real for the people who live on the edge. It gives them skin in the game instead of moving them off it."
    "You touch the screen where the counter-figures bloom—tiny polygons showing reduced localized flooding. Your chest loosens a fraction. The numbers are still numbers, but they translate now into practical breathing room: a stall that can open"
    "after a storm, a net that dries under sun, a kitchen that doesn't close for the season. Hope here is pragmatic and stubborn."
    hide dr_sienna_kade
    hide theo_baines
    hide maya_calder

    scene bg ch2_c4ca42_2 at full_bg
    # play music "music_placeholder"  # [Music: The guitar motif returns, lighter, a thread of possibility]
    "You leave the lab carrying more than charts. There is a plan forming like a seedling in rock."
    # [Scene: Harborside Promenade | Evening]

    scene bg ch2_c4ca42_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Laughter, the slap of a loose board, Asha's pins tacking paper to a lamppost]
    # play music "music_placeholder"  # [Music: Warm, rhythmic hand-drums—community rhythm]
    "The promenade is restless in the best way: hands moving, voices offering, the small mechanical clatter of someone fixing a rain-collecting barrel. Asha's bright scarf is a comet as she pins flyers to a board; Rosa"
    "sits on a crate, net between her knees, fingers moving with the economy of habit. The smell of brewed coffee and frying flatbreads hangs in the air."
    "Elias 'Eli' Maren is by the micro-farm racks, sleeves rolled, dirt braided under his nails. He grins when he sees you—wide enough to crease his sea-glass eyes."

    "Elias 'Eli' Maren" "You look like you've been arguing with a map and won at least one point. Tell me it's true."
    show maya_calder at left:
        zoom 0.7

    maya_calder "Won is generous. We managed to make the numbers speak a language that remembers people."

    "Elias 'Eli' Maren" "Good. Because people here remember tomatoes. And bad harmonica solos. Both are important."
    "He tucks the battered harmonica into his pocket and hands you a folded square of tracing paper with rooftop layouts. It's warm from being in his hand; the ink is smudged at the edges where he's been sketching between watering runs."

    "Elias 'Eli' Maren" "Demo plots on three roofs next week. We'll show them it's possible to bolt down beds and a cistern without ripping the roof off. If folks can taste the greens and count the saved nights without power, it's easier to talk fairness."

    maya_calder "We'll need a quick impact brief—numbers that show reduced runoff per bed, labor timelines, and—' (you glance at the promenade) '—ways to include stall owners during construction."

    "Elias 'Eli' Maren" "Leave the charm to me. I'll get people on the roofs with music and food. Asha will manage turnout. You bring the numbers and that terrifying thing you do where you make complex things suddenly seem like recipes."
    "Elias 'Eli' Maren's laugh nudges something loose in you; it is easier to breathe when people plan with mouths that smile. You find yourself laughing back, the sound like a small light."
    "Rosa looks up and catches your gaze. Her face is a map of weather and memory; she nods once, small and approving. You sit beside her briefly while she works the net, the rough fibers pressing into your palms."
    show rosa_calder at right:
        zoom 0.7

    rosa_calder "You keep the net whole."

    maya_calder "I won't let the net be cut without asking."
    "Rosa's eyes soften—an old weathered mercy. You tuck that promise into your notebook next to the rooftop sketches."

    menu:
        "Let Elias 'Eli' Maren run the community festival demo while you prepare the technical brief":
            "You hand him the tracing paper and the schedule. He grins and pulls in a handful of volunteers, already humming a beat that will be a good distraction for skeptical neighbors. You feel the weight shift from planning to doing in the sweetest way."
        "Stay to help Asha pin flyers and speak with market vendors":
            "You take the stack of flyers and help Asha talk to stall owners. You hear their concerns firsthand—smaller, human angles the models miss. The conversation gives you new lines to add to the brief and fills your notebook with the language that will make numbers persuasive."

    # --- merge ---
    "Evening folds into plans. Your field notebook fills with counter-figures and practical steps: rooftop bed yields, estimated work-hours, cost comparisons seeded with community labor. Theo's message pings—an updated model with the calibration flagged and a suggestion to combine the wall proposal with demonstrable green infrastructure to shore up public support."
    "Evening folds into plans. Your field notebook fills with counter-figures and practical steps: rooftop bed yields, estimated work-hours, cost comparisons seeded with community labor. Theo's message pings—an updated model with the calibration flagged and a suggestion to combine the wall proposal with demonstrable green infrastructure to shore up public support."
    show theo_baines at center:
        zoom 0.7

    theo_baines "Offset confirmed. We can present both—wall for critical corridors, micro-infrastructure for neighborhoods. Hybrid framing gets more buy-in."
    "You let the word hybrid sit on your tongue. It isn't a compromise; it's a patchwork of resilience that recognizes the city is made of people, not just assets."
    "Elias 'Eli' Maren leans close, lowering his voice to a conspiratorial hum."

    "Elias 'Eli' Maren" "We'll do the demo. We'll have music and seedlings and something that tastes like the future we want. You bring the stubbornness that makes the numbers human. Together—"

    maya_calder "—we make something that doesn't erase anyone to protect someone else."
    "He smiles at you then—soft, present, full of the kind of faith that is not naive but contagious. The conversation doubles back into practicalities—who brings tarps, where to borrow a ladder, and a volunteer list for the roofs."
    "The swell in your chest is not panic this time but tide in the best sense: forward movement, carrying people with it. Responsibility is heavy, but the weight is shared now; hands take it with you."
    hide maya_calder
    hide rosa_calder
    hide theo_baines

    scene bg ch2_c4ca42_4 at full_bg
    # play music "music_placeholder"  # [Music: Guitar and hand-drums weave; the tone is rising, forward-moving]
    "You fold the notebook closed, feeling the shape of a plan you can actually hand to someone and say: here, help make this real."
    "Asha ties the last flyer with a strip of bright tape and steps back. The promenade hums like a community taking breath—organized, hopeful, and alive."
    "You stand on the same boardwalk you left this morning, but something has shifted. The day's meetings have given you numbers and a political map; the evening has given you voices, hands, and soil under fingernails. The two together feel like momentum."
    "You run one last quiet count of the braids on your cuff—three, four, the same as always—and let the thought settle: you will learn to ride this tide without drowning the people you love."
    "(Page-turn thought: The hybrid plan is fragile and brilliant. Dr. Sienna Kade's seawall will not be irrelevant; it is necessary in places. But there are places where a wall is overkill and a garden is lifeline."
    "You can see the outline of a campaign that marries both. Tomorrow you will begin the work of stitching them into a single story that donors can fund and neighbors can stand behind. You are tired"
    "and not ready in every way, but some things glow with the strange warmth of being possible.)"

    scene bg ch2_c4ca42_5 at full_bg
    # play music "music_placeholder"  # [Music: The hopeful motif lingers, then softens]

    scene bg ch2_c4ca42_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
