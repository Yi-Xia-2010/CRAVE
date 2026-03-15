label chapter3:

    # [Scene: City Hall Glass Atrium | Late Afternoon]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, insistent cello; a distant, metallic heartbeat underlies the chord.]
    # play sound "sfx_placeholder"  # [Sound: The hushed murmur of a crowd, a coffee cup clicking against a saucer, the soft whoosh of the air system trying to keep moisture at bay.]
    "You step into the atrium and the city breathes around you: measured, public, and thin with expectation. Light fractures across polished concrete and the tide-forecast display blinks a steady line of numbers that mean the difference"
    "between funding and failure. The projection in your pocket curls against your thigh — Jun Park's voice still scrolling, his 'prioritization' and 'sacrifice zones' like small, clinical stones you can feel in your ribs."
    "You bring your palm to the stone balustrade, the surface cool and slightly gritty under your fingers. It remembers storms the way your hands remember rope burns: not as a single image but as a contour"
    "of pressure and insistence. People drift around you like migrating birds — Rosa steady at your shoulder, Ivy fidgeting by the railing, Elias Navin a few meters away under the spill of a task lamp, Lian's"
    "aides circulating with quiet, clipped movements."
    "Smell threads through the room — lemon disinfectant rubbed over handrails, paper-cup coffee, and a faint salt tang that the building can't quite scrub away. The city tries to be clean here, tidy; the mess of"
    "the Basin and the Strand is folded and labeled and put behind glass. You are used to the pulled-together face of institutional spaces. You are not used to how exposed being here makes you feel."
    "Rosa touches your arm, an old anchoring motion that says more than words could: steady yourself. Her breath smells of tea and the garden soil she carries like an heirloom."
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "People will be listening for how you name them, Mara. Facts are important, yes — but don't let them hide the faces, child."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "I won't. I—"
    "Ivy falls into step beside you, hands balled into the pockets of her overalls. Her cheeks are still freckled from the greenhouse sun; she keeps catching your eye and then looking away."
    show ivy_kestrel at center:
        zoom 0.7

    ivy_kestrel "Are you going to—what if they laugh at the reefs? What if Jun Park says we're naive?"
    "The word 'naive' tastes like saltwater in your mouth. You remember nets snagged on broken pilings, Rosa's hands knuckled with age, the children's feet running on the Strand after the flood receded. You remember every time"
    "people were dismissed as sentimental. You do not want to be the thing that lets them be dismissed again."

    menu:
        "Check the projection feed for Jun Park's latest line":
            "Your thumb swipes the tablet and the feed breathes to life: Jun Park's measured cadence, the words 'triage' and 'efficiency' underlined in a way that feels like a verdict. Your stomach tightens; seeing it sharpens the edges of what you must say."
        "Close the tablet and breathe, focusing on faces in the room":
            "You slide the tablet back into your jacket. Your lungs pull in the warm, lemon-tinged air, and you let your gaze rest on Rosa and Ivy. The room's hum becomes a chorus of individual breaths; it steadies rather than scares you."

    # --- merge ---
    "You choose neither grand avoidance nor fevered scanning; you fold both impulses into a single, slow breath. The atrium's noise becomes a netting — you let it hold you."
    "Elias Navin is by a bank of information screens, hands tucked into his parka pockets, the sensor on his wrist pulsing faintly green. Up close, his steel-blue eyes flicker with the same worn, patient calculation you"
    "remember from nights bent over tide charts. He doesn't smile. Not because he is unkind, but because there are always calculations to be made and numbers that must be trusted."
    hide rosa_alvarez
    show elias_navin at left:
        zoom 0.7

    elias_navin "They're projecting worst-case in thirty years,' he says without preamble. 'Which makes the case for structural intervention stronger on paper."

    mara_kestrel "Paper is not the sea,' you reply. The words are sharper than you intend. 'And the sea is not neat."

    elias_navin "No. But 'not neat' doesn't help a council that needs measurable outcomes. Living breakwaters reduce wave energy and rebuild habitat — I know the data. But scaling without oversight is what worries them."

    mara_kestrel "It worries them because it's new. It worries them because the budget line items don't read like safety. It worries them because Jun Park's maps have numbers."
    "Elias Navin looks at you, something like apology in the line of his mouth."

    elias_navin "I didn't come back to make promises I can't quantify. I came back because the methods work, and because people are already staking their lives on experiments. I don't want to gamble with them."

    mara_kestrel "Neither do I.' There's a rawness in your chest that you don't mask. 'But this is not just a technical problem, Elias. It's moral. People will read 'experiment' as 'luxury' if Jun Park frames it right."

    elias_navin "Then let us frame it right."
    "Silence stretches; Elias Navin watches your face as if reading tide marks in your expression. The counsel in his posture — careful, exacting — is both comfort and constraint. You want him to be bolder; you"
    "also know the cost of overreach. You and he orbit the same urgencies differently: his are blueprints and trial data, yours are names and nightly vigils applied in practice."

    menu:
        "Ask Elias Navin to promise to speak plainly, to translate his data into people's lives":
            "Elias Navin's jaw tightens. He leans forward, voice low: 'I'll show them the fishers' catch logs. I'll show them live monitoring. But you have to tell their names. The council listens to numbers — sometimes names make them human.' He nods, setting his jaw like someone bracing for both applause and scorn."
        "Press Elias Navin on contingency plans, asking how he'll answer public failure":
            "Elias Navin's eyes cloud with a flicker of something ancient — the memory of a failure he never let go. 'We design redundancy into the reefs,' he says. 'We run staged deployments. If the trial fails, we have emergency pump protocols and temporary sacundaries. But I won't pretend there are no risks.' His voice is flat, not uncaring — just honest."

    # --- merge ---
    "Elias Navin's hands curl, then relax. He reaches for something unsaid and sets it down. The crowd thickens near the council chamber doors. The atrium's warmth is suddenly thin, like clothing soaked through on the Strand."
    "Jun Park arrives like an engineered tide: smooth, unavoidable. He moves with precise steps, his deep-indigo coat immaculate against the public light. He gives the room a look like a man who knows what he's asked"
    "to do and has already planned the words. When he sees you, something flickers across his face — a calculation rather than a confession. You do not know fully what it means. You let it be"
    "ambiguous: complex, unreadable."
    hide mara_kestrel
    show jun_park at right:
        zoom 0.7

    jun_park "Mara.' His voice is public-loud but practiced. 'Thank you for coming. The council needs strong partners."
    hide ivy_kestrel
    show mara_kestrel at center:
        zoom 0.7

    mara_kestrel "Partners who are honest about tradeoffs,' you say. You keep your tone level. 'Even when those tradeoffs aren't popular."
    "Jun Park inclines his head slightly — an official concession."

    jun_park "The city can't save everything. We have to make decisions that preserve the greatest good for the greatest number. My proposal does that."

    mara_kestrel "At what cost, Jun Park? We have neighborhoods on the line. People with nowhere else to go."

    jun_park "Every plan has costs. Our obligation is to choose the path that preserves the city's function and life as a whole."
    "The words are clinical, and you can hear the number-crunching in them. You remember Jun Park as a child who could map out a harbor by heart; you also remember nights when his decisions felt like"
    "shutters closing. There is compassion in him, once; you have watched it harden into policy."
    "Rosa steps forward between you, the gesture small and old as tidewood. Her voice is low, but the room listens."
    hide elias_navin
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "If you count us only as pixels on a map, Jun Park, you miss the way people stitch their lives to these places. You may save a downtown café, but leave an old woman watching the sea from a porch she can no longer afford. Counting must be humane."
    "Jun Park: (He doesn't dismiss her. He doesn't need to.) 'I respect Rosa's point. But policy is blunt by necessity.'"
    hide jun_park
    show ivy_kestrel at right:
        zoom 0.7

    ivy_kestrel "Blunt hurts people,' she snaps, louder than you expect. A few heads turn. Ivy is small but her indignation carries; she plants a hand on the railing like a child testing a rope-line. 'You can't just decide who gets to be saved."
    "That lands like a stone. Jun Park's face softens, for a heartbeat, into something almost human. Then the mask is back."
    hide mara_kestrel
    show jun_park at center:
        zoom 0.7

    jun_park "I never said it's easy. I said it is necessary."
    "There's a friction now between you and Jun Park that thrums under the polite councilroom etiquette. The chamber doors open and a wave of expectant faces pushes in — residents, press, council aides. Lian Mor appears"
    "by the dais, her silver bob immaculate, the neutral calm of the city's official balance. She scans the room like an adjudicator."
    hide rosa_alvarez
    show councilwoman_lian_mor at left:
        zoom 0.7

    councilwoman_lian_mor "We will begin the public hearing. Please reserve outbursts for the allocated time."
    hide ivy_kestrel
    hide jun_park
    hide councilwoman_lian_mor

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low murmur crescendos into near-silence as the chamber settles.]
    "You walk to the edge of the platform, the microphone's metal cool against your palm. The lobby lights flick across your jacket — canvas, patched, salted. The room watches. You can hear the little mechanisms of"
    "power: an aide tapping a note into a tablet, a camera lens adjusting, the soft rustle of a program packet."
    "Your journal sits under your arm like a small, private world of pressed seaweed and uneven notes. You think about the ledger your father used to keep — a simple, honest book of what went out"
    "and what came back. The hearing will reduce stories and harbor histories into bullet points and callout boxes. You resist that. You also know you are not only a storyteller here; you carry a kind of"
    "authority when you speak. People expect you to make certain calculations visible — not just numerical, but moral."
    "Inside, your thoughts scatter then line up: If you endorse Elias Navin, you risk being framed as endangering the city by favoring experimental community science. If you back Jun Park, you risk being complicit in the"
    "forced movement of neighborhoods you have sworn to protect. If you propose a hybrid, you risk being accused of fence-sitting, of delaying urgent action long enough for the storm of politics to wash away good intentions."
    "You feel the weight of each possibility like a stone in a net. Your hands shake slightly on the microphone stand — not from fear of speaking, but from knowing the scale of what your voice can do in this room."
    "Elias Navin moves closer then, lowering his voice so only you can hear."
    show elias_navin at left:
        zoom 0.7

    elias_navin "Say the names,' he instructs softly. 'Say who will be affected and what mitigation we can do, and then tie it to the model. It gives them both heart and reason."
    "Jun Park stands a few feet away, composed. His gaze touches you, an unreadable ledger — neither wholly reproach nor wholly support. He says your name quietly, as if testing it in his mouth."
    show jun_park at right:
        zoom 0.7

    jun_park "Mara, we're counting on your honesty in the chamber. You can help steer this conversation toward solutions."
    show mara_kestrel at center:
        zoom 0.7

    mara_kestrel "And you?' you answer. 'Can you steer it toward justice?"
    "Jun Park's expression tightens for a second. He doesn't answer then, only watches the chamber tilt like a tide at low and high."
    "The clerk calls the hearing to order, and the first rounds of testimony begin. Voices rise and fall: a fisher speaking about boats lost to erosion; a café owner who fears for her shop's facade; a"
    "youth organizer demanding equitable relocation funding. The language on the screens is precise, and the faces in the room are messy and human."
    "When your moment comes, the air seems to compress. You step to the microphone, the room framing you in light and expectation. The taste of metal is behind your teeth — adrenaline and salt. Your throat works."
    "You think of every dock-hand who taught you how to knot a rope, of the nights you kept vigil on rooftops, of Ivy painting signs that say 'We Belong Here.' You think of Elias Navin checking"
    "instruments with a steady, practiced care. You think of Jun Park in his tailored coat deciding what counts as a life worth saving."
    "You inhale. The choice feels less like choosing an option and more like choosing what kind of ledger the city will keep."
    hide elias_navin
    hide jun_park
    hide mara_kestrel

    scene bg ch3_98c6f2_3 at full_bg
    # play music "music_placeholder"  # [Music: A low, unresolved minor chord — a falling line that refuses to settle.]
    "You see the faces in the crowd: Rosa, Ivy, Elias Navin, even Jun Park's aides. Each is lit with their own mixture of fear and hope. The microphone is a narrow thing; decisions are narrower still."
    "You breathe, taste the city on the air, and you know what must be said. But the words you will choose will chart different tides for different people."
    "You step back from the mic for a heartbeat, closing your eyes to gather the exact weight of what you are about to place into the public ledger."
    "The clerk looks at you expectantly. Lian Mor shifts in her seat. The screen behind Jun Park flashes a projected cost analysis. Elias Navin's wristband pulses once, steady and green. Rosa's hand finds yours for a second and squeezes. Ivy's face is taut with fear."
    "You open your mouth."
    "You stop."
    "You are at the decision."
    "Weighing obligation, community trust, technical promise, and political reality — you must choose your public stance now."

    menu:
        "We go with the living breakwaters—community science and adaptation.":
            jump chapter4
        "I support Jun’s municipal emergency plan and will cooperate.":
            jump chapter7
        "We propose a negotiated hybrid: targeted barriers plus community-led living reefs with shared oversight.":
            jump chapter10
    return
