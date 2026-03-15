label chapter11:

    # [Scene: Glass Marsh | Morning]

    scene bg ch11_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Light strings — patient, ascending]
    # play sound "sfx_placeholder"  # [Sound: Soft gull cries, the muffled slap of small waves, the distant rum of a delivery skiff]
    "You are there before the sun has fully thrown off the night. The feed you checked last night is now real and breathing: dark ribbons of seagrass pushed up through silt, blades trembling in the shallow"
    "current like new green promises. The world smells of brine and warm peat; your jacket tastes faintly of salt where the wind has kissed it. The dented brass compass at your sternum is cool against the"
    "cotton of your shirt, a quiet weight that says you are home and you were right to come back."
    "Dr. Leyna Ortiz is crouched at the edge, tablet balanced on her knee. Her face lights with that quick, private excitement researchers get when data and wonder line up. Ronan hauls a small net through knee-deep"
    "water, laughing when he upturns a wriggling juvenile fish. Oba Kofi stands a little apart, watching the water the way an old reader watches the tide in a book he's known for years — hands folded"
    "on his cane, mouth working into a half-smile."
    "Maya appears from the path with a thermos and a paper bag, the scent of warm bread rising between you. She drops a bag beside your boots and smears her palms with the sticky residue of jam, grin wide enough to be sunlight."
    show maya_maren at left:
        zoom 0.7

    maya_maren "Bread, of course. You'd be scandalized if I didn't bring bread. Also—neighbors asking when the next volunteer day is. They're keen. They sounded—' (she shrugs) '—proud, if that makes sense."
    "You feel the braided cord against your wrist, a physical pulse you can reach for when words want to scatter. Pride is a soft, honest pain, the kind that grounds rather than displaces. These mats were"
    "an experiment three months ago; you can still taste the uncertainty on your tongue. Now, green threads pick themselves from muck. The smell of new growth is a language your bones remember."
    show dr_leyna_ortiz at right:
        zoom 0.7

    dr_leyna_ortiz "Remote sensors show increasing oxygen levels near the mats,' (she taps the tablet) 'and turbidity is down by a measurable fraction. It's small, but it's trending the right way."
    show alys_maren at center:
        zoom 0.7

    alys_maren "Small is what grows into something big if we keep tending it."

    menu:
        "Take a close-up photo for the public feed":
            "You raise your camera and focus on a single blade; the photo will read like proof. Leyna nods, imagining the press release already."
        "Walk the line and sample the silt":
            "You kneel and scoop a handful of mud, feeling it yield between your fingers. Leyna smiles — the sample will tell a better story than a picture."

    # --- merge ---
    "The group continues their morning work, buoyed by a small, shared sense of progress."
    # [Scene: Old Lighthouse Rooftop Greenhouse | Midday]
    hide maya_maren
    hide dr_leyna_ortiz
    hide alys_maren

    scene bg ch11_e67f19_2 at full_bg
    # play music "music_placeholder"  # [Music: Piano and soft brass — tender, upward]
    # play sound "sfx_placeholder"  # [Sound: The distant hush of traffic in town, a low gull's call punctuating the glass]
    "You move from the marsh into the greenhouse as if crossing a threshold from trial into proof. The air here is humid, earth-sweet; sunlight slants in through salt-flecked panes and catches in the fine hairs at"
    "the nape of your neck. You set your notebook on a bench and rub soil between your fingers until your palms remember their purpose."
    "Dr. Leyna Ortiz follows, still talking percentages and p-values the way some people recite prayers. Oba Kofi arrives, steady as storm rock, and Maya lingers by a tray, fussing like a parent over seedlings."
    show oba_kofi at left:
        zoom 0.7

    oba_kofi "The young ones will learn to respect this place. You make them see it work, they will protect it."
    show alys_maren at right:
        zoom 0.7

    alys_maren "That's the plan."
    "A sharp knock on the greenhouse door cuts through the warmth. The handle opens and Celine Harrow steps in, immaculate even among humidity and dirt. Her coat is tailored, but she has removed gloves so she"
    "can shake hands without leaving the faintest impression of distance. Her steely blue eyes sweep the space, then soften in a practiced way that reads like diplomacy."
    show celine_harrow at center:
        zoom 0.7

    celine_harrow "Alys. Leyna. Thank you for arranging this. I wanted to see the pilot with my own eyes before the council meeting."
    "(she inclines her head)"

    celine_harrow "I've been following your updates. The images are compelling."

    alys_maren "Good to have you here,' (you keep your tone even) 'The mats are showing early success, but it's fragile work. It needs time and care more than headline funding."

    celine_harrow "Time and care are luxuries. We can expedite that care.' She unfolds a slim, leathered dossier and lays it on the bench as if placing a seed in the palm of your hand. 'Municipal funding, tied to a hybrid plan — restored habitat where feasible, engineered protections where necessary. Covenants baked into the contract to protect ecological outcomes. We accelerate scale and shield families now."
    "Dr. Leyna Ortiz studies the dossier like you might a lab result. Her fingers hover, and for the first time since you met her this morning her voice carries something that resembles worry."
    hide oba_kofi
    show dr_leyna_ortiz at left:
        zoom 0.7

    dr_leyna_ortiz "Covenants? Who enforces them? Who audits compliance? Data transparency will have to be guaranteed, or we risk academic and ecological integrity."

    celine_harrow "Audits will be part of the agreement. Independent oversight panels. Municipal oversight. Legal language can be precise."

    alys_maren "Municipal oversight is a useful phrase until the public interest meets politics,' (you level with her) 'Who signs the enforcement? Corporate partners? Developers?"
    "Celine Harrow's lips tighten briefly. The practiced smile returns like a switch."

    celine_harrow "We won't hand control to outside developers without protections. The point is to avoid paralysis. Families need tangible defenses this season."
    "Oba Kofi steps forward, cane tapping. His voice folds into the greenhouse like a low tide."
    hide alys_maren
    show oba_kofi at right:
        zoom 0.7

    oba_kofi "We have always made our living with the sea. We can see both the immediate and the long. But if promises are soil-soft and washed away by the first storm, what good are they?"
    "Ivo Calder arrives then, breath smelling faintly of oil and rope, a canvas cap still shadowing his hazel eyes. He moves to stand beside you, his presence practical and steady. He doesn't need to speak to"
    "be counted; his body carries the workman's argument — that doing something visible can keep people safe and hopeful."
    hide celine_harrow
    show ivo_calder at center:
        zoom 0.7

    ivo_calder "If there's a way to put both our hands to this — seawalls where homes sit low, and seagrass where it can take root — I'm in. We can make the protections quick and the restorations long-lived."
    "Celine Harrow looks from Ivo Calder to you, assessing the geography of alliances."
    hide dr_leyna_ortiz
    show celine_harrow at left:
        zoom 0.7

    celine_harrow "A combined approach could be the political winner. It gives me the leverage I need to pass funding and gives the town immediate relief. And the covenants ensure ecological protections."
    "You sense the room constrict and expand at once — politics, science, community all trying to fold into a single map. The dossier is weighty but not inflexible. Leyna's eyes meet yours: bright, tired, insistent."
    hide oba_kofi
    show dr_leyna_ortiz at right:
        zoom 0.7

    dr_leyna_ortiz "If we agree to covenants, I will insist on scientific seal-clause language. Clear thresholds for habitat integrity, transparent data streams, and a legally mandated community oversight seat."

    celine_harrow "That is negotiable. We can draft language with your input."
    hide ivo_calder
    show alys_maren at center:
        zoom 0.7

    alys_maren "Negotiable is not the same as binding, and binding is not the same as enforced."
    hide celine_harrow
    show maya_maren at left:
        zoom 0.7

    maya_maren "Are we... are we saying this could mean more boots on the ground, or are we saying... contracts?"
    hide dr_leyna_ortiz
    show ivo_calder at right:
        zoom 0.7

    ivo_calder "Both. We design it so volunteers keep building the green work, and engineers shore up the places that need immediate attention."
    "There is a beat of silence, not empty but thick with possibility. You picture, for a beat, a map of Saltwick that includes living shorelines and strengthened houses without the hand of outside developers reshaping the"
    "town's values. You picture your father mending a net in a yard that hasn't been flooded. You imagine the children who will learn to plant seagrass as a rite of passage."
    "Celine Harrow uncloses the dossier and slides a page toward you: a preliminary schematic of phased funding and a clause marked 'Ecological Covenant — Article 4.'"
    hide alys_maren
    show celine_harrow at center:
        zoom 0.7

    celine_harrow "We can move fast if you help shape the terms. You can keep the science at the center of this plan."
    "You want to believe her. You want to believe in the speed of money that comes with constraints and in the possibility of institutional muscle that doesn't swallow the community. You also know the slippery ways language can be curved."

    menu:
        "Ask to see the covenant's enforcement clause now":
            "You hold the page between your fingers and request specifics. Leyna leans in, grateful for the rigor. Celine's expression narrows; she appreciates the demand but notes it's 'procedural.' The room shifts into clause-level negotiation energy."
        "Propose a pilot combined approach first, with binding community oversight":
            "You suggest a stepwise combined pilot, where community oversight is written into the first tranche. Ivo nods sharply; Leyna scribbles notes. Celine hesitates—interested but cautious, the political gears clicking."

    # --- merge ---
    "The discussion moves toward drafting precise language and structuring next steps."
    "You feel hope, bright and careful, pushing at the edges of caution. The rise in your chest is not naive; it's tempered by the long knowledge of broken promises. Still, there's a new current here —"
    "data corroborating life, community hands ready to work, a mayor willing to talk budgets with strings attached rather than bulldozers. The question is not whether the town will change, but how fast and under what ethics."

    ivo_calder "If we can layer defenses with the restoration — quick berms, temporary barriers, then plant — we protect homes while we buy time for beds to bloom. It needs coordination, but we can do that."
    hide maya_maren
    show alys_maren at left:
        zoom 0.7

    alys_maren "Coordination needs trust and time. And transparency. Leyna needs guarantees in the contract."

    celine_harrow "Then we write them in. I want to leave this greenhouse with a plan you can support. I want a political victory that actually does some good."
    "Her words, earnest in the way of a leader who must both win and be seen to have done right, land like a seed dropped into well-tilled soil. You imagine the possible — a hybrid plan"
    "seeded with community oversight. It could be the fastest route to saving homes and marshes both."
    "Oba watches you, unreadable for a moment, and then nods. His endorsement is not dramatic, but it carries the weight of a life spent reading tides."
    hide ivo_calder
    show oba_kofi at right:
        zoom 0.7

    oba_kofi "If our people can watch the rules being kept, and if the young ones learn the work on the mats, then the town will have both shelter and seamoss to hold the sea back. Keep the watch, child. Keep the watch."
    "You swallow. The rise in your chest is no longer just hope; it hums with responsibility. This is the moment where science, habit, law, and love could be braided together — or frayed apart under haste."
    "Dr. Leyna Ortiz rubs her thumb along the tablet's edge and looks at you only once, as if the next step depends on the steadiness of your look."
    hide celine_harrow
    show dr_leyna_ortiz at center:
        zoom 0.7

    dr_leyna_ortiz "We need to be strategic. We can accept funds with covenants if the contract is written by legal counsel in collaboration with independent ecologists and includes immediate disclosure of data. I will not sign otherwise."
    hide alys_maren
    show celine_harrow at left:
        zoom 0.7

    celine_harrow "Then draft the language, and we will bring it to counsel."
    "The air in the greenhouse feels almost too bright. Outside, the sea is indifferent and patient. Inside, a group of people—some who have always belonged to Saltwick, some who returned with maps and degrees, some who have never left—stand at the hinge of what could be a new path."
    "You touch the braided cord on your wrist. The compass at your chest is warm."
    "You can see three clear directions forming at the edge of your vision: a patient, community-first scaling that honors ethics and slows the work; a faster, hybrid municipal push with covenants that tie money to ecological"
    "promises; and a hard, combined plan with Ivo that asks everyone to move in step right away. Each path requires trust in different forms: faith in neighbors, faith in institutions, faith in coordinated action."
    "The room hums with potential, breath held on the cusp of a decision that could shape the season, perhaps the decade."
    hide oba_kofi
    hide dr_leyna_ortiz
    hide celine_harrow

    scene bg ch11_e67f19_3 at full_bg
    # play music "music_placeholder"  # [Music: Swell of strings, hopeful and resolving]
    "You are the hinge. The town watches the way you breathe."

    menu:
        "Continue community-first scaling, refuse Celine's hybrid.":
            jump chapter12
        "Accept Celine's hybrid funds with strict ecological covenants.":
            jump chapter15
        "Force a combined plan with Ivo — immediate protective measures layered with restoration.":
            jump chapter12
    return
