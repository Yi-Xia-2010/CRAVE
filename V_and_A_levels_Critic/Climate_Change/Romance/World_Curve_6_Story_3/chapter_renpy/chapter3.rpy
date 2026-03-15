label chapter3:

    # [Scene: Brinehaven Boardwalk | Late Afternoon — humid, storm-bruised]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, steady strings; a rhythm that mimics tide-breath]
    # play sound "sfx_placeholder"  # [Sound: Gull calls, distant engines, a single roll of thunder in the distance]
    "You step out of the municipal hall and the town hits the street like a returning tide — voices, fragments of argument, the whispered calculus of survival. The air is thick enough that each word feels"
    "like a pebble dropped into water: ripples, careful, inevitable. Salt and damp wood cling to your clothes; someone walks past with a basket of wet rope that smells of brine and old leather. Your notebook is"
    "folded against your palm, damp at the edges. The coral pendant at your throat is cold, an honest weight."
    "Mayor Lynette breezes past, her raincoat buttoned, tablet clutched like an extra hand. She does not slow. Her jaw is set in the same way it was in the hearing — a neat, municipal firmness designed"
    "to make decisions feel like facts. Cass stands nearby, shoulders squared, his multifunction watch still warm from the projection he showed inside. Thin bands of light map topography in the air above his palm like a"
    "miniature, impossible ocean."
    show cassian_cass_romano at left:
        zoom 0.7

    cassian_cass_romano "Mira,' he says (the tone is earnest, practiced), 'the models account for three scenarios. Fast construction reduces risk now. Funds are ready. We can start before winter."
    "You can see the projection again even without the holograph: lines in steel-gray, controlled slopes where water will meet wall, annotations that suggest certainty. His eyes — clear, assessing — find yours and, for a beat,"
    "the public veneer slides away. You read the earnestness there. You read the tightness underneath."

    cassian_cass_romano "I don't want to override the town. I want partnership. Let me underwrite the first phase; let us prove it works."
    "Jonah is a step away, hands raw from hauling nets earlier, salt crusted at his knuckles. He looks like he could fold into the dock and become part of it: wool sweater, rope bracelet, the smell"
    "of fish and sun baked into him. His voice is low and grainy with impatience."
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "Proof in a boardroom won't save our nets, Mira. It won't teach kids how to read the tides or give Old Man Rafi's stories a place. We need local crews, marsh work, seasons to breathe."
    "He gestures at the harbor with a sweep of his hand; the motion scatters a few gulls. The laugh lines around his eyes crease the way they always have when he’s trying to soften an edge"
    "— and something in you loosens. Your chest aches in that precise, usable way: a reminding of why you are here."

    jonah_reyes "You coming with us isn't just symbolic. You know how to make the numbers sing with people around them. Don't let them box us into a ribbon-cutting."

    menu:
        "Ask Cass a technical question":
            "You step closer, thumb brushing the wet corner of your notebook. 'On the breakwater cross-section,' you begin, 'how would you phase sediment deposition to avoid loss of oyster beds?' Cass's mouth opens, surprised, then narrows with interest. He launches into specifics, and you feel the familiar rhythm of engineering talk - precise, fast."
        "Tell Jonah you'll consider the community plan":
            "You tilt toward Jonah, giving him a look that is all the promise your voice won't make. 'Tell me more about the first season's labor plan,' you say. Jonah's shoulders drop a fraction, relief easing his face. He sketches a plan with his hands — crews, seedbeds, apprenticeships — and the words come easier, steadier."

    # --- merge ---
    "All outcomes return to the main conversation on the boardwalk."
    "Mayor Lynette pauses between them, the practical center of gravity. She looks to you as if you are the fulcrum she can set the town upon."
    show mayor_lynette_cole at center:
        zoom 0.7

    mayor_lynette_cole "Mira, we need a move that voters can see. I can't sell paralysis. We need a timeline."
    "You feel the town leaning again — each opinion a small, physical tug on your sleeve. Tessa is here too, Tessa's bright hazel eyes wide and raw. She jabs a finger into the air like a pin against a map."
    hide cassian_cass_romano
    show tessa_kestrel at left:
        zoom 0.7

    tessa_kestrel "Promise jobs. Promise training. Promise I won't have to leave for the city."
    "Her urgency is young and sharp, and it slices through your self-doubt with clean, familial authority. You want to promise her the moon and a stable dock; you know promises count for something in this town. You also know promises are currency that can be cheapened."
    "An old voice rides up from the edge of the dock — Old Man Rafi, leaning on his battered cane, his beard threaded with a single blue bead that glints like a tiny sea. He looks at you as if reading weather."
    hide jonah_reyes
    show old_man_rafi at right:
        zoom 0.7

    old_man_rafi "Will we keep the stories, child? Or let them put a sign in their stead and call that preservation?"
    "His words land like a stone in shallow water. They reverberate. The people nearby murmur agreement; someone laughs nervously. Memory is not an abstract here. It lives in the docks' scars and the way the marsh smells after a high tide."
    # play sound "sfx_placeholder"  # [Sound: A phone buzz; Dr. Saira's number flashes on the small screen of your field notebook as you fish for it]
    hide mayor_lynette_cole
    hide tessa_kestrel
    hide old_man_rafi

    scene bg ch3_98c6f2_2 at full_bg
    "You step away from the center and lift the phone to your ear. The boardwalk's noise muffles, and Dr. Saira N'Goma's voice fills the small space."

    "Dr. Saira N'Goma (on phone)" "Mira. I listened. You're between a hard fast-track and slower, community-led options. I've been through grant applications that take months — but there are emergency windows. You need a public demand to justify them. Mayor Lynette responds to optics. If we want money tied to community oversight, we'll need signatures, town seats, and the right framing."
    "You exhale; her practicality maps onto your own. She has always been a machine for translating science into leverage. Her words are precise and, crucially, possible."

    "Dr. Saira N'Goma (on phone)" "But the political window closes. Soon. If you want leverage to push for community conditions, you need to mobilize something visible tonight — a petition, a crew roster, a charter. I can help lobby, but not without pressure."
    "Your skin prickles, not with fear but with possibility. A timeline is a tool; pressure can shape funding into something accountable. Hope arrives as a practical instrument."

    menu:
        "Ask Saira to draft language for community oversight":
            "You say, 'Draft the oversight language. Make it non-negotiable. Tie funding disbursement to milestones with community seats.' Saira's laugh is small and relieved. 'I'll get to work,' she replies."
        "Tell Saira to focus on emergency grants instead":
            "You say, 'Prioritize speed. Get whatever emergency funds you can to keep people working.' Saira's reply is softer, chastened: 'Speed without terms is a gamble, Mira. But I will try.'"

    # --- merge ---
    "All outcomes return to the main conversation on the boardwalk."
    "Cass watches the call with a faint, unreadable expression. Jonah's jaw tightens; he's breathing in the way someone steeling themselves to speak a truth. The tide of voices ebbs and flows. Every plan feels like a rope to tow a boat — practical, necessary, and potentially cutting."
    "You place your palm flat against the notebook and feel the damp paper through your glove. You remember the sound of rain on the roof of the house you couldn't save, the smell of the wet"
    "curtains, the way you promised yourself you would never let naming a problem be a substitute for solving it. Guilt is a long, cold current, but beneath it there is an ember that still wants to"
    "make things hold."
    "Cassian 'Cass' Romano: (stepping closer, softer now) 'Mira, I know trust is earned. Let us build the first section with community labor. We'll hire local crews; we'll open the models for public review. Give me the chance to show you I'm not just another contractor.'"
    "You study his face. There's a seriousness that isn't performance. You also see the edge of control — the need to fix things on a schedule he can manage. That need is not inherently bad. It is a shape of care you do not dismiss."
    "Jonah Reyes: (leaning forward) 'And give us control over what gets built. Not just labor — design seats. Apprentices. If you go with him, Mira, make it real or we'll lose more than ground. We'll lose say.'"
    "His fingers drum a small, impatient rhythm against a piling. There's fear braided into his insistence, the fear of cultural erasure disguised as practicality. You want to soothe and to be fierce all at once. It"
    "is possible, you tell yourself; you've brokered compromises that held before. The question is whether this moment will trust that history enough to allow another."
    "Mayor Lynette: (practical) 'We need to vote on an immediate motion to authorize preliminary work. We can require oversight, but we need timelines.'"
    "Her voice trims the conversation into policy. You feel the political machinery beneath her phrasing — a way to both answer the town and move the cameras. There is a necessary dance here: optics and substance must find synchroneity or else nothing happens."
    "Tessa steps up and catches your sleeve. Her nails are darkened with soil from the seedbeds she’s been tending. She looks like the future you keep promising in quieter moments."
    show tessa_kestrel at left:
        zoom 0.7

    tessa_kestrel "Promise me workers. Promise me training before anything else. Don't let them pay someone to come in and finish us off faster."
    "You close your fingers around her small hand. The clasp is immediate and grounding. It's not a policy; it's an anchor."
    "Old Man Rafi shuffles closer, his voice low and steady."
    show old_man_rafi at right:
        zoom 0.7

    old_man_rafi "Sometimes the town's spine is in what we teach the young. Sometimes it's in what the sea teaches us. Don't forget both."
    "His eyes find yours and stay there, as if handing you the ledger of memory and expectation. The book of the town, open and waiting for the next line."
    # play music "music_placeholder"  # [Music: Strings lift subtly; the rhythm steadies into a more hopeful cadence]
    hide tessa_kestrel
    hide old_man_rafi

    scene bg ch3_98c6f2_3 at full_bg
    "You taste salt and the metallic tang of your own pulse. The clarity heaves up like a wave but softer — not revelation so much as alignment. Three faces present a way forward, each plausible, each"
    "imperfect: Jonah's steady, rooted insistence on community restoration; Cass's promise of engineered speed and resources; the third — a combative, transparent tactic to pry open funding lines and force accountability."
    "Your chest is full of the town's histories and your private ledger of what you could not save. Your guilt sharpens your care; it does not paralyze you now. The lift you feel is not lightening of burden so much as focus: an axis around which everything else must rotate."
    "You breathe in, the air dense with storm and the possibility of action. Your mouth is dry; your voice has weight. You speak, because a town needs an axis to turn on and because the people"
    "standing with you are looking for that pivot. Your decision will not be the end of uncertainty, but it will make a direction — and directions are how storms are prepared for."
    "Your heart settles into the choice as if it were an instrument you must tune. Three plans hang there like buoys in the water, each signaling a different current."

    menu:
        "Tell Jonah you'll lead community restoration":
            "You step toward Jonah, the boardwalk's damp wood creaking under you, and say, 'We build from the marsh up. We'll train crews and make the marsh count.' Jonah's face opens — a breath, a laugh that is part disbelief, part joy. He clasps your hands. 'Let's get to work,' he says, and there's a new weight to his words."
        "Tell Cass you'll broker a formal partnership":
            "You look at Cass, keeping your voice level. 'We'll take your funding if it's tied to local oversight and transparent milestones,' you say. Cass nods, a small, fierce look of relief; he extends his hand with a plan for immediate mobilization. 'We won't let you down,' he promises."
        "Tell the town you'll expose funding and demand transparency":
            "Your voice tightens, but it's steady. 'No plan moves forward until the funding sources are transparent and legally bound to community terms,' you say. The crowd murmurs — some with approval, some with fear. Dr. Saira's brief 'Finally' comes through on your mind like a chorus; Old Man Rafi's eyebrows lift at the word 'terms.'"

    # --- merge ---
    "All outcomes return to the immediate decision point where the town awaits your commitment."
    "You stand at the crest, the three faces before you: Jonah's amber earnestness, Cass's steel-gray resolve, the public ledger's cold clarity offered by exposure and accountability. Each is a hand extended in a different language of care."
    "Your palm closes around your notebook. The coral pendant warms against your sternum, as if answering the heat of the town's need with its small, steady glow. You have failed before and learned the contours of that failure. That learning is not a chain; it is a map."
    "You inhale once more, letting the humid air fill you. Your decision will not erase the storms that have come, but it will shape how the town stands against the next one — who works, who decides, what is saved, and what is reimagined."
    "A ridge of light cuts across the harbor. The murmur on the boardwalk hushes to expectant breath. The choice is yours. The town is watching, and your chest tightens not with dread but with the clear, difficult hope of someone finally deciding to act."
    "Choose how to commit Brinehaven’s immediate strategy and, implicitly, your closest ally."

    menu:
        "I will organize a community-led restoration — we build from the marsh up.":
            jump chapter4
        "I will broker a formal partnership with Cass and the engineering firm.":
            jump chapter7
        "I will gather evidence and expose opaque funding — force transparency before any plan proceeds.":
            jump chapter10
    return
