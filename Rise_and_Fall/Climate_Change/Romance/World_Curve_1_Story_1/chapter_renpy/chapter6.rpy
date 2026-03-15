label chapter6:

    # [Scene: Boardroom / Model Table | Morning]

    scene bg ch6_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low murmur of the city beyond the glass, the distant gulls folded into the hum]
    # play music "music_placeholder"  # [Music: Warm strings, a steady rising motif]
    "You stand with the printouts in a neat stack against your palm, the paper warm from the sunlight that slips beneath the blinds. Theo's annotated graphs sit beneath your hand like small maps of possibility—lines that"
    "used to feel like warnings have become measurements you can argue with, protect with, and build on."
    "The vote has narrowed into a final ratification. The procurement packet sits in the center of the table: technical specs, budgets, and the line-item language you fought for—community training slots, job guarantees for retrofit crews, explicit"
    "funds for rooftop grants. It is not all of what you wanted; nothing in this process ever is. But when you read the reimbursement clause and see the phrase 'community liaison stipends' in fine print, your"
    "chest loosens a fraction that counts as breath."
    "Dr. Sienna Kade stands across from you, her shoulders set like a measured tide. She reads the same pages you do. For a long beat, both of you read through the same numbers in silence, the city's future folded between paragraphs."
    show dr_sienna_kade at left:
        zoom 0.7

    dr_sienna_kade "The amendments are cleaner than I expected. Your language on job transitions—it's precise and actionable. Procurement won't like the contingencies, but your data helps justify them."
    "You feel an odd mix of relief and fatigue. Relief that the work—your work—mattered. Fatigue because influence always tastes like friction: something shaved away so something larger might remain."
    show maya_calder at right:
        zoom 0.7

    maya_calder "You didn't win everything. You kept the harbor's people on the ledger."
    show theo_baines at center:
        zoom 0.7

    theo_baines "The models hold. I re-ran the failure modes with the modular wall widths and the terrace absorptive factors—we get a 12 percent lower mean flood depth where terraces are dense. It's not sexy, but it's proof."
    "Theo's voice has that thin, honest cadence when he's proud but trying not to celebrate too loudly. He taps a finger against the tablet; the screen glows a reassuring teal."
    "Elias 'Eli' Maren's presence at your shoulder is less formal, but steadier than any policy line. He rubs a thumb along a smudge on your sleeve, as if erasing anxiety the way he might wipe soil from a crate."

    "Elias 'Eli' Maren" "You did the thing the city's been asking for—made the machine listen to people. That's not small."

    maya_calder "We made them listen,"

    menu:
        "Place a hand over Theo's on the tablet, a small thank-you":
            "Theo looks startled, then allows a quick, grateful smile. The gesture says what the budget lines cannot: he is seen."
        "Catch Sienna's eye with a brief nod—acknowledging an uneasy truce":
            "Sienna's expression shifts in a subtle way—tightness around the mouth loosens, and she inclines her head. It is not warmth; it is recognition."

    # --- merge ---
    "The meeting proceeds with acknowledged contributions and careful exchanges."
    "Dr. Sienna Kade clears her throat, the sound like tide against pilings."

    dr_sienna_kade "We will present the hybrid package this afternoon. If Procurement accepts the language verbatim, we move forward with phased implementation—seawall modules where needed, terraces where communities want them, and the job training embedded as part of the contract."

    maya_calder "And the relocation stipends? The timelines?"

    dr_sienna_kade "Clause 7B. Stipends are tied to guaranteed hire opportunities in restoration and rooftop programs. Timelines are phased to minimize displacement. It's imperfect, but it avoids sudden exodus."
    "You watch the way the word 'guaranteed' sits in the air. It carries gravity—a promise heavy enough to keep people from having to make impossible choices overnight."

    theo_baines "Procurement will haggle. They'll say it raises costs and slows delivery. But we have precedent—this model scales in pilots elsewhere. We can argue cost-offsets with reduced long-term damages and the economic return from job creation."

    "Elias 'Eli' Maren" "And hey—if the terraces fail to be scenic, I will personally stage rooftop concerts to boost market sales."
    "His joke breaks some of the pressure; a ripple of laughter moves across the table. You laugh, too, and the warmth feels like a small victory on its own."
    # [Scene: Kade Resilience Lab — Press Atrium | Late Afternoon]
    hide dr_sienna_kade
    hide maya_calder
    hide theo_baines

    scene bg ch6_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Flash of shutters, low chatter of reporters, the soft mechanical breath of air filtration]
    # play music "music_placeholder"  # [Music: Brighter strings, piano arpeggio suggesting cautious triumph]
    "You and Dr. Sienna Kade step up to the podium together. The lab's logo glows behind you—cool and clinical—but the light catches your braid, the silver thread at your temple, the small pendant that bobs when"
    "you breathe. Side by side, your silhouettes read as an unlikely accord in a room built for certainties."
    show dr_sienna_kade at left:
        zoom 0.7

    dr_sienna_kade "Today, the council voted to approve a hybrid coastal resilience package. It balances engineered protection with community-run green infrastructure and job guarantees that place residents at the front of implementation."
    show maya_calder at right:
        zoom 0.7

    maya_calder "This plan didn't arrive fully formed. It arrived because neighbors argued for space in the contract, because scientists and local workers sat across tables and mapped out shared risk. It is a plan meant to protect the city and the people who make it home."
    "Reporters ask quick questions—procurement timelines, cost estimates, how relocations will be handled. You answer with measured facts, but you also speak with a weight that is not wholly technical: memory and people."

    "Reporter" "There are concerns that the seawall still necessitates displacement in some blocks. How do you reconcile protection with preservation?"

    maya_calder "We reconcile it by refusing false choices. Where hard infrastructure is necessary, we shrink its footprint and pair it with investments that let people stay—job training, retrofit grants, economic pathways tied to restoration and rooftop agriculture. Where a seawall would be overbearing, terraces will absorb and serve. This isn't preservation of every old dock—some things will change—but we fought to make change compensatory, not extractive."
    "Dr. Sienna Kade: (after a pause) 'It is the only scalable compromise that reduces immediate risk while investing in long-term community stability.'"
    "Her voice is softer under the press lights tonight. The steel in her eyes is tempered by something like fatigue—and perhaps the burdens you both carry."

    menu:
        "After the press, tap Sienna's shoulder and say 'Thank you' quietly":
            "She inclines her head, the moment small and human; for a breath you glimpse a woman who has chosen urgency over ease."
        "Step aside to Theo and whisper 'We did it'":
            "Theo's smile cracks wide. He mumbles about margin of error and buying drinks, but his relief is plain."

    # --- merge ---
    "The evening moves on with quiet acknowledgments and informal celebrations."
    # [Scene: Old Dockside Neighborhood — Your Kitchen | Evening]
    hide dr_sienna_kade
    hide maya_calder

    scene bg ch6_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain beginning to thread the gutters; the domestic sound of a neighborhood winding down]
    # play music "music_placeholder"  # [Music: Soft guitar motif, intimate and warm]
    "You come home the way you always do: keys, the pull of the braided cuff against your skin, the smell of Rosa's stew as familiar as tidewater. Rosa stands at the sink with a net in"
    "her hands—faded, patched in one place with a square of denim. When she sees you, she doesn't speak first. She holds the net against her chest like a relic."
    "Rosa Calder: (voice small) 'They told me some docks would be kept. They told me there would be work. But they also told me other things would go.'"
    "You cross the room and it feels strange to navigate the space between policy victory and personal grief."
    show maya_calder at left:
        zoom 0.7

    maya_calder "You didn't sign away anything today, Rosa. We pushed—hard. The stipends, the jobs, the terraces—these are meant to keep people whole."
    "Rosa's eyes glisten; she rests the net on the table and wraps her fingers around it until the seams show white."
    show rosa_calder at right:
        zoom 0.7

    rosa_calder "Whole is a strong word, mi'ja. You held the anchors, but the tide took some boards. I'm glad for the work. I'm afraid for the rest."
    "You hold her hands, rough as the rope she once mended. You let the grief and the gladness sit side by side; both are valid and necessary."

    maya_calder "We'll build what we can. We will hire the crews you know. We'll teach the young ones to plant kelp and read sensors. We'll make sure that the knowledge of the docks isn't just catalogued—it is paid for."
    "Rosa lets out a breath that holds something like concession, like hope."

    rosa_calder "Then come sleep. Tomorrow you'll need to talk to the council about timelines."

    maya_calder "I will. And I'll bring your net."
    "She laughs once, a wet, relieved sound, and the kitchen feels less like a room of loss and more like a place where decisions thrum into life."
    # [Scene Transition: Rooftop Gardens & Micro-farms | Golden Hour]
    hide maya_calder
    hide rosa_calder

    scene bg ch6_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft city noise beneath, crickets waking, the rustle of leaves]
    # play music "music_placeholder"  # [Music: Upbeat acoustic, warmth in the melody]
    "You and Elias 'Eli' Maren climb up to the rooftop—hands full of seedlings, gloves damp with compost. His laugh bubbles out when he nearly drops a tray of basil."

    "Elias 'Eli' Maren" "If this is what winning smells like, I'm signing up for the smell of soil forever."
    "You kneel to plant, fingers making small beds in the raised soil. The scent of earth mixes with salt and the faint smoke from a distant kitchen. Your hands are stained and steady."
    show maya_calder at left:
        zoom 0.7

    maya_calder "It feels like proof. People won't just be hired to move sandbags—they'll learn to steward terraces that hold water and weight. They'll make food and make income. They'll work on the very coast that their families fished from."
    "Elias 'Eli' Maren presses a sprig of thyme into the soil and looks at you, eyes catching the last light."

    "Elias 'Eli' Maren" "You did more than make policy happen. You made this city—our city—someone's place again. That's a terrible thing to reduce to a sentence, but it's true."

    maya_calder "I couldn't have done it alone."

    "Elias 'Eli' Maren" "I know. That's the best part."
    "He takes your hand—there is no flourish, no grand gesture, only the warmth of contact and the easy humor that has steadied both of you through meetings and late-night digests. The way his hand fits feels like a small covenant: mutual commitment to work and to rest."

    menu:
        "Press a seed into his palm, playful and promise-like":
            "He laughs and accepts the seed, tucking it into his pocket for later—an emblem of whatever you will grow together."
        "Simply squeeze his fingers once and return to planting":
            "The squeeze is enough: affirmation without fanfare. He nods, content, and goes back to his rows."

    # --- merge ---
    "Planting continues into the evening; the gesture lingers privately between you."
    "You plant until the light runs thin and the city lamps blink awake. The terraces look like a constellation of careful green decisions—a blueprint in miniature for neighborhoods to come."
    # [Scene: Storm-scarred Boardwalk (A Short Visit) | Dusk]
    hide maya_calder

    scene bg ch6_601bcb_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Water lapping at exposed pilings, a distant generator, the staccato of people hammering a last plank]
    # play music "music_placeholder"  # [Music: Gentle swell—hopeful, steady]
    "You walk the boardwalk at dusk. The new modular wall stands lower in some places, higher in others—less a continuous barrier than a stitched garment, interrupted by terraces where people share benches and plant boxes. There"
    "are gaps where the old wood still creaks; you notice the places left intentionally to honor memory—pockets the city agreed to keep with a new function. It is less than the boardwalk once was and more"
    "than it would have become without a fight."
    "You stop at a place where a faded plaque marks a family boat that once docked here. The plaque is beginning to patina. People you know will cross the threshold to different roofs and different jobs;"
    "some will move away. You feel the tug of absence as keenly as the thrill of what was gained."
    show maya_calder at left:
        zoom 0.7

    maya_calder "This is not neat, and it is not painless. But it's not surrender either."
    "Elias 'Eli' Maren sidles up beside you, soil still under his nails, and places an arm around your shoulders. It is not theatrical; it is belonging."

    "Elias 'Eli' Maren" "We'll keep making places like this. People will come to learn. They'll bring their kids. We'll teach them to plant in salty air."
    "You laugh, the sound catching between the pilings and the low clouds."

    maya_calder "Other cities are already calling. People will study the procurement packet and call it a model. They will not get the nets or the stew, but they will take the idea."

    "Elias 'Eli' Maren" "Let them. We'll teach them the recipe, too."
    "You both stand for a long moment, cataloguing the view: seawall modules, terraces, lights, the narrower boardwalk where a child still runs with a paper boat. It is an imperfect panorama—edges softened by the night and the hopeful hum of people rebuilding."
    hide maya_calder

    scene bg ch6_601bcb_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A neighbor plays a harmonica in the distance, a single note held steady like a stitch in time]
    # play music "music_placeholder"  # [Music: The rising motif returns, fuller and more settled]
    "You think of Rosa's hands, Theo's steady data, Dr. Sienna Kade's difficult concessions, and Elias 'Eli' Maren's laughter draining into work. You carry all of them forward like a weathered map—creases that show where you have been and directions that insist you move on."
    show maya_calder at left:
        zoom 0.7

    maya_calder "This victory—it's threaded with absence. We'll carry those absences with care."

    "Elias 'Eli' Maren" "And we'll keep making things that answer them."
    "You breathe in the night: salt, wood, the faint sweetness of the terrace herbs. The future is not finished. It never is. But tonight, there is a tangible feeling under your ribs: possibility, bolstered by people, anchored in place."
    "You fold your fingers into the braided cuff and let that promise sit in your palm—a simple, stubborn token that you will not let the past be erased in the name of safety."
    hide maya_calder

    scene bg ch6_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: Warm strings resolve into a gentle, conclusive chord]

    scene bg ch6_601bcb_8 at full_bg
    # play music "music_placeholder"  # [Music: Soft diminuendo; the hopeful motif lingers then settles into silence]

    scene bg ch6_601bcb_9 at full_bg
    "THE END"
    # [GAME END]
    return
