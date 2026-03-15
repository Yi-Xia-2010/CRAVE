label chapter33:

    # [Scene: Marabel Promenade | Dawn]

    scene bg ch15_b77e51_1 at full_bg
    # play music "music_placeholder"  # [Music: Rapid strings undercut by a distant low brass — tense, urgent]
    # play sound "sfx_placeholder"  # [Sound: Gull cries, the creaking of wet wood, the soft mechanical whir of drones]
    "You sit on the edge of the boardwalk with the brass compass heavy in your palm. The cord scratches your skin like a question you can't answer aloud. The ledger—your ledger, the town's ledger—lies shut beside"
    "you; a page taped in, stubborn and damp. You thought keeping records would feel like making armor. Instead it has the brittle quality of a memorial: thin, necessary, not strong enough to hold everything."
    "Across the water, the Beacon pulses: a clean, relentless heartbeat of glass and code. It is no longer simply a promise of sensors and models. It is now a showroom—its neat screens and investor placards a glare that blurs the faces of the people they were supposed to protect."
    "You taste metal, the aftertaste of decisions and signatures. Your hands are the hands of someone who counted names until they blurred. You can still feel Noah Reyes's palm in the dark when the vote split,"
    "hear the small, careful phrases he used to steady things. 'We'll make audits public. We'll be there.' He said it like a pledge—but pledges can be reworded."
    "Noah Reyes moves into your periphery, coat damp, curls flattened by rain. He doesn't immediately sit. He holds himself like someone measuring distance he doesn't want to cross."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "They're starting the managed-access rollouts today. Papers already went through. Rosa—she's—she thought it was the only way to keep people insured. Investors offered relocation packages and infrastructure bonds."
    "You feel the words as if thrown: proposals, offers, insurance—language meant to seal wounds with money."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "They came with checks and clauses, not apologies."
    "Noah rubs at the bridge of his nose. He looks tired in a way that makes your chest tighten."

    noah_reyes "I argued for caps on covenants. For deed protections. We didn't get all we wanted—"

    asha_moreno "You didn't get enough,' you say. The sentence is small, sharp. 'You—"

    noah_reyes "I tried—' He stops, the fragility of that phrase cracking in the air. 'Asha, you made us visible. You made people read the clauses. We forced transparency. Without you—"
    "You remember the courtroom-quiet the day you leaked terms to the council, the way Lila Park's face hardened, the way Mayor Rosa's hands trembled as she signed. The Beacon's lobby filled with protesters and press. Lila"
    "Park's firm withdrew the major tranche the week after the hearings—publicity costs were too high. The hole that opened was wide enough for private money to step in without ribbons or remorse."
    hide noah_reyes
    hide asha_moreno

    scene bg ch15_b77e51_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant click of heavy doors shutting; a murmur of expensive voices]
    "Noah leans forward, voice pitched low, urgency sharpening his cadence."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "When the consortium stepped back, investors didn't ask 'what the town wants.' They asked 'what's the value if we control access.' They promised to keep houses standing if they could manage utilities, rents, access to the promenade. It's pragmatic—"
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Pragmatic is a fancy word for 'we'll keep property, not people,'' you cut in. The phrase tastes of iron. 'They bargained with livelihoods like they were lines in a ledger."
    "Noah looks at you, and something in his face rearranges—guilt, exhaustion, an almost-palpable resignation."

    noah_reyes "I—' He hesitates as if looking for the best word. 'I accepted a position. Technical director. I can stay, Asha. I can keep a seat at the table and make sure the sensors aren't sealed off. I can push for community dashboards, open APIs. That's leverage."
    "Your chest tightens until breathing takes effort. A lever is not the same as a root."

    asha_moreno "So you'll trade the nights we devoted to soil meetings and door-to-door canvassing for a badge and a closed server room? You'll speak for people whose names won't be on the same deeds you sign?"
    "Noah flinches, like you've hit a place he has been trying to ignore."

    noah_reyes "I won't be silent. If I don't...someone else will write the rules. I can't watch from the outside while the town becomes a case study."

    asha_moreno "And what if the case study costs us our grandparents' places? What if the model keeps our roofs but not our neighbors? What if—"

    menu:
        "Ask him to stay home tonight, to talk instead of making plans":
            "You reach for the small comfort of presence, imagining an hour where the Beacon's light doesn't define you. Noah's face softens; he almost says yes, then remembers the meeting at nine and a flight-out deadline and the list of things that depend on him. He squeezes your hand and says 'Later.'"
        "Demand he explain the concessions he's already agreed to":
            "You force the ledger into his hands—figuratively, then literally—bring up clauses, names of properties, the maps of access. Noah's jaw sets; he starts to explain line items and redlines, his planner's voice returning, but each technical term thuds like a small betrayal. He meets your eyes with a look that is half apology, half duty."

    menu:
        "Say nothing, let the silence widen":
            "You tuck the compass deeper into your pocket, letting it press against your ribs. The silence grows long, full of promises you hoped were solid. Noah stands, unsure, then sits back down to fold his hands in his coat. The drones hum like insects between two closed mouths."
        "Tell him you can't stay if he takes the role":
            "You say the words. They are heavy and exact. Noah flinches as if struck. He opens his mouth several times; the planner in him reaches for contingency plans, for reasons, for rationales. Every explanation makes your chest feel colder. He says 'I'll fix it'—but you know 'fix' has become a different language in this town."

    menu:
        "Beg him to try to find another route—both of you pushing back against the managed access together":
            "The image of you two, shoulder to shoulder in a dim hall, fighting wording with stubbornness and coffee—it's tempting. Noah eyes you with a longing that is both pleading and weary. He imagines petitions and courtrooms and seed drives until his face grows pale. But then he thinks of the Beacon's inner channels and the compromises he's already promised; hope and reality wrestle."
        "Stand and leave now, start the itinerant program alone":
            "Your feet move before you finish saying it. The compass bounces against your thigh. The idea of leaving is a blade and a cure at once: you will build something honest on the margins, teach people how to plant shoreline and remember how to measure tide with hands, not spreadsheets. Noah reaches for you as you turn; the reach is an echo of the life you almost shared."
    "THE END"
    # [GAME END]
    return
