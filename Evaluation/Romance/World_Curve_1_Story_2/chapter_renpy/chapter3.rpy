label chapter3:

    # [Scene: Public Briefing Hall | Late Afternoon]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Quiet, hopeful strings — a steady rise that suggests possibility rather than triumph]
    # play sound "sfx_placeholder"  # [Sound: Murmur of the crowd, a projector's low whir, the soft scrape of chairs]
    "You enter on the tail of a conversation — laughter that doesn't reach the eyes, an exchange of pamphlets folded with care. Your notebook is heavy in your hand; the band on your wrist hums with"
    "the day's readings. Everyone here knows why the room is full: the city needs a plan, and Aegis has the funding and the language to make people feel it's already happening."
    "Your chest is tight in the way it has been since the Old Pier meeting — not panic, but anticipation. You are practiced at turning anticipation into action. The plan you sketched in the margins last"
    "week is folded into the corners of your mind like a map you're still learning to read."
    "You choose a seat near the back, where you can watch faces more easily than be watched. Samir slides in beside you, his glasses catching the light. Etta is two rows ahead, scarf braided around her"
    "neck like a small flag. Noah stands near the doorway, hands buried in the pockets of his jacket, jaw set. Arin Voss is there too — leaning against a pillar, camera in hand, eyes scanning the"
    "stage with that restless attention you know like your own pulse. His expression is complex; you don't try to reduce it. For now, it's enough that he's here."

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Applause, polite and expectant; the projector clicks to a slide labeled "Aegis Stabilization Initiative — Phase I"]
    show liora_kade at left:
        zoom 0.7

    liora_kade "Thank you all for coming. I know these are not abstract numbers for anyone in this room; these are decisions about homes, workplaces, and histories. We don't propose this lightly."
    "Her voice fills the hall — smooth, practiced, the kind that sizes an audience and then gives them a soft outline of certainty. The floodwall schematic unfurls: a continuous engineered barrier, integrated pump systems, dedicated relocation"
    "zones, rapid timelines. The language is efficient: 'stabilize', 'secure', 'protect.' Underneath every certainty, you taste the metallic tang of contraction — but there's also the undeniable relief in a plan that says: we can stop the"
    "water, now."
    "You listen to the slides with the technical ear you've trained. The numbers make a logical arc: reduced inundation frequency, projected savings in emergency response, return on investment across thirty years. Samir leans in, whispering a"
    "footnote about assumptions in the model. You tuck that correction into your head — not to dismiss what's on the screen, but to remember what the equation might be leaving out."

    liora_kade "We present not just structure, but support: funding for short-term relocation, employment for local contractors in construction phases, and an independent oversight board to audit impacts."
    "(her eyes flick briefly to the crowd)"

    liora_kade "We will move quickly because every season matters."
    "A hand shoots up from the front; a woman from the Pier neighborhood asks about timelines for relocation. Liora replies with a cadence that steadies the room: there will be consultation windows, compensation proposals, and an"
    "expedited build schedule to lower long-term risk. The Q&A opens like a spring — questions, a few sharp, some heavy with grief."

    menu:
        "Raise your hand and ask about community relocation safeguards":
            "You square your shoulders and raise your hand. When the moderator calls on you, your question is simple and concrete: How will Aegis guarantee that relocation funds are not clawed back by future budget cuts? Liora's smile remains, but for a beat you see the day's strategist behind it — she answers with a timeline and an offer to draft a clause with community legal representatives."
        "Stay silent and file the question for Samir":
            "You keep your hand down and tuck the question into the margin of your notebook. Samir notices the look on your face and gives a small, tight nod; later, he'll press it in the right meeting at the right time. For now you listen, collecting language that will sharpen the ask when the channels open."

    # --- merge ---
    "The room breathes collectively. For a moment the whole thing could tilt either way — trust or skepticism, speed or care. Your internal ledger hums: the community can build small, distributed defenses, living roofs, marsh restoration"
    "— things that knit people back to place — but the timeline for those is measured in seasons, not weeks. Aegis promises weeks."
    "After the formal presentation, there's a lull where conversations fragment into clusters. You move forward, drawn by the magnet of action. Samir stays with you, pragmatic as ever."
    show samir_hale at right:
        zoom 0.7

    samir_hale "They're fast,' he says, low, 'and they have capital. That's leverage you can use — or it can steamroll community priorities."
    show mira_solace at center:
        zoom 0.7

    mira_solace "Use it how? Make them sit at more tables? Force independent oversight into the contract?"

    samir_hale "Exactly. Push for sterner legal language and community veto on relocation zones. Liora's offer for an oversight board is a foothold; footholds are worth climbing from."
    "Your mind spins through the technicalities — oversight composition, binding covenants, escrowed funds. Each is a tool and a test. The room smells faintly of lemon cleaner and old paper, a hospital-orderly scent that seems strangely consoling."
    hide liora_kade
    show arin_voss at left:
        zoom 0.7

    arin_voss "We could turn the foyer into a living map. People pin their homes, their memories. We organize a march to the site when they break ground. Stories change policy when they refuse to be abstracted."

    mira_solace "A march could force visibility, but it could also entrench Aegis — let them frame you as obstructionist. And if things get messy, who protects the families?"

    arin_voss "Then we plan the mess. We plan for safety teams, for legal observers, for media. Direct pressure makes it harder for them to hide trade-offs."
    "Your chest tightens and loosens in equal measure. Arin's optimism is contagious; he speaks in scaffolding and spectacle, and you can see how his ideas stitch people to a cause. But your calculations whisper about legal"
    "language and municipal levers. You want visibility and you want binding conditions. You want both to be true."
    "Etta approaches and places her hand on your shoulder, the gesture an anchor."
    hide samir_hale
    show etta_maren at right:
        zoom 0.7

    etta_maren "There are ways to hold both fast and slow. The sea does not choose a single current; it moves with many. We can make a harbor that bends but does not break."
    "Her voice is a small, fierce bell. In it you hear the memory of wooden docks and the feel of salt in a child's hair. It steadies you."
    "Noah, who has been watching with a practicality tempered by fear, leans in. He keeps his voice low."
    hide mira_solace
    show noah_solace at center:
        zoom 0.7

    noah_solace "If they build the wall as is, my shop's relocation could be sudden and the compensation won't match what it costs to move. I don't want to leave, Mira. How do we make sure my—our—people aren't priced out?"
    hide arin_voss
    show mira_solace at left:
        zoom 0.7

    mira_solace "We press for escrowed relocation funds, binding timelines for notice, and clauses that prioritize small business relocation support.' (you list it, slow, because the act of naming makes it more real) 'We can push for job guarantees in the construction contracts where possible."
    "Noah exhales, not relieved but reasonable — the conversation has moved from fear to tactics. You're working with language to make space for people."
    "Liora Kade moves through the crowd with the sure step of someone used to buying time and answers. She pauses near you, her presence a cool counterpoint."
    hide etta_maren
    show liora_kade at right:
        zoom 0.7

    liora_kade "Mira Solace. Your work at the Tidehouse has been noted. We need partners who translate data into practice. If there are revisions we should consider, let's put them on the table now."
    "You study her, all professional polish and soft empathy. You think of every public meeting where a concession was called a 'necessary compromise' and how those words sometimes hid permanent loss. Yet she is offering a door."

    mira_solace "Every door should have a clear jamb. Oversight must be community-led, legally enforceable, and funding dedicated before construction. We need guarantees for small business and for culturally significant sites."

    liora_kade "If you can draft language that is operational and legally sound, I will take it to our counsel. Speed is important to me; we can be fast and fair."
    "There's a pause where the room seems to hold its breath. The possibility of moving forward with conditions — a hybrid between urgency and justice — flares in you. It is not the whole of what"
    "you want, but it's movement. The tone in the hall ripples with it: people shifting from waiting to leaning in, from worry to work."
    hide noah_solace
    show arin_voss at center:
        zoom 0.7

    arin_voss "We can hold them to that. We can make sure promises are watched."

    mira_solace "Watching is different from enforcing. Enforcement needs legal teeth."

    arin_voss "Then let's be clear about the teeth and the tactics. We make noise where necessary, we build parallel resilience where possible."
    "Your mind catalogs paths: community-led small-scale adaptations that make neighborhoods livable in the long term; municipal negotiation that leverages Aegis's timeline and capital for protections; a public campaign to raise the temperature on accountability and visibility. None are mutually exclusive, but they demand different kinds of labor, trust, and timing."

    menu:
        "Agree to help draft enforceable oversight clauses with Samir":
            "You turn to Samir with a plan, breaking the complex problem into paperwork and process. Samir's face opens with relief; he mentions legal contacts and a late-night drafting session. You feel the steady comfort of shaping policy with tools you trust."
        "Tell Arin you'll plan a public campaign together":
            "You look at Arin and answer with a cautious spark: yes, but coordinated with safety and legal support. He grins, immediate and boyish; the energy between action and storytelling surges through you."
        "Volunteer to lead community-run adaptation pilots while negotiations continue":
            "You tell Etta and Noah you will start pilot projects — marshbeds, modular elevation platforms, shared tool-days. Etta smiles, and Noah says he'll help with materials. The idea is smaller than a wall and bigger than a pamphlet; it feels like a soil-scented, hands-in solution."

    # --- merge ---
    "Conversation loops and folds, voices overlapping: residents demanding clarity, journalists probing for conflict, Liora balancing empathy with cadence. The projector hums on; the schematic hangs like a promise and a challenge."
    "Inside you, the tilt is upward. The room has supplied options and openings. Aegis's plan is real and immediate; community resilience is slow but cumulative; public pressure makes promises harder to break. None of it will"
    "be easy. None of it changes the fact that water keeps rising and that timelines are brutal. But the choices in front of you are not a wall and an abyss — they are paths that"
    "can connect."
    "You close your notebook for a moment, feeling the weight of choices translate into a warmth at your core. This is the kind of crisis that can harden people into fixed positions or teach them how to braid their strengths. You want to braid."
    hide mira_solace
    hide liora_kade
    hide arin_voss

    scene bg ch3_98c6f2_3 at full_bg
    # play music "music_placeholder"  # [Music: Swell — hopeful and steady, underscoring the sense of agency building in the room]
    "The briefing winds down. Liora steps off the stage to the next cluster of conversations; Samir pulls you aside to exchange contact information with a lawyer he trusts; Etta begins organizing an assembly for the Old"
    "Pier to comb through the Aegis language; Noah outlines a list of materials he'll need if pilot elevations start. Arin tugs out his camera and suggests documenting everything — a visual record to match the legal"
    "text."
    "Your options, suddenly, are immediate and practical: dig into municipal leverage and legal language; deepen grassroots capacity with pilots and workshops; or amplify public pressure through organized campaigns. Each path is work-shaped and hopeful."
    "You stand in the hall's doorway, the evening light slipping across the floor like a tide you can measure in steps. The city feels slightly different than when you arrived: not less threatened, but more capable of response. Your heart aligns with that sense of movement."
    "You inhale salt and lemon, the smell of plan and people. It is time to choose a direction — not because one will solve everything, but because action threads into other actions. You think of Etta's"
    "hands, Samir's pragmatism, Noah's shop, Arin's restless creativity. Each is a strand you could pull."
    # [Decision Handoff — The Moment Before Action]
    # play music "music_placeholder"  # [Music: Quiet, expectant chord]

    menu:
        "Push grassroots alternatives":
            jump chapter4
        "Negotiate a hybrid plan with municipal influence":
            jump chapter7
        "Mobilize a public campaign with Arin":
            jump chapter10
    return
