label chapter11:

    # [Scene: Subbasement Data Lab | Night — Storm Incoming]

    scene bg ch11_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense electronic pulse — rapid tempo, high BPM]
    # play sound "sfx_placeholder"  # [Sound: Server fans whining; distant thunder; a shrill alert chime cutting through]
    "You are here because you promised the Beacon you would keep the lights on. You keep that promise by muscle memory — fingers on the edge of the console, breath shallow, eyes scanning floodmaps that slide across the monitors like incoming tide lines."
    "The screens blink: green, amber, then the first stubborn red. The predictive cascade model is feeding new inputs — a compound storm front, higher surge than yesterday's run, meteorological noise that the model flags as 'nonlinear.'"
    "Your throat tightens. The hum of the servers vibrates through your teeth. The air tastes of cold copper and recycled heat."
    "Rafi's face fills one comm-channel: hair flattened from the rain, eyes rimmed red from a night of chasing leaks. He doesn't wait for you to say hello."
    show rafi_alvarez at left:
        zoom 0.7

    rafi_alvarez "Aiko — you're seeing this? I pushed the memos to the group. They're... Jesus. It's worse than I thought. Contingency clause three — 'priority override to contractual obligations' — it's explicit."
    "You had hoped the pilot's clauses were airtight. You read legalese the way some people read scripture; you believed words mattered. Now words are blades. You feel old ledger lines peel under your skin — sentences that could hand away the neighborhood in exchange for global uptime."
    "A server alarm shrieks. One of the redundancy nodes flips to degraded. An amber streak crawls across the tidal simulation; the containment prediction is off-schedule. You can hear the city outside as a low, rolling percussion — wind tearing at tarps, water sluicing down improvised gutters."
    hide rafi_alvarez

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Overlapping comms — shouted orders from Elias; Rowan's calmer, firmer voice on a secure line]
    "Elias Chen breaks into your feed, breathless, a smear of dirt on his cheek where he'd been kneeling into the soil to keep a water bladder from splitting."
    show elias_chen at left:
        zoom 0.7

    elias_chen "They're asking to flip the automated containment. Rowan says it's the only safe option to keep the main conduits from failing. Aiko, we can't just— we set this up to be ours. People are still coming in and out of the lower blocks."
    "His words are a punch and a caress at once. He always talks like he's standing in the middle of the crowd — a hundred hands on a hundred things at once, each palm warm. He"
    "refuses to let the neighborhood be reduced to a line on a map. His urgency is a raw animal thing; you hear the sleep in it fray."
    "Rowan's window opens on your console with near-immediate priority. He is calm as a surgeon's hands, as unnervingly composed as the Atrium's glass."
    show dr_rowan_hale at right:
        zoom 0.7

    dr_rowan_hale "Aiko, the model shows a 78 Percentage probability of structural integrity loss if we delay. Activating containment reroutes surge through sacrificial channels. Those channels are outside core residential paths, but they temporarily restrict access. Legally, HelioCorp holds emergency clause authority in a force-majeure scenario."
    "You want to counter with clauses, footnotes, community charter — but Rowan's tone is a thin, precise blade. He does not shout. He sharpens the fact: infrastructure integrity, lives preserved by engineering certainty."
    "You can feel the room tilt between two fires. One is the literal storm outside. One is the slow-burning, less-visible corporate fire in the memos Rafi fed into the loop. Every monitor seems to lean toward one or the other."
    "Mina Kuroda's voice is on the low-frequency channel, methodical, hands-on."
    show mina_kuroda at center:
        zoom 0.7

    mina_kuroda "If you shut access to the lower canals even temporarily, our distribution routes are cut. Elders, meds, fuel for the pumps — all of it. We have contingency caches mapped. We don't have time to move everyone before a flip."
    "Sora Watanabe's voice follows, calm and gravelly like well-worn rope."
    hide elias_chen
    show sora_watanabe at left:
        zoom 0.7

    sora_watanabe "This place remembers doing things together. To hand decision elsewhere in the moment is to let the sea listen to strangers."
    "The comms splinter into a chorus; the lab's lighting flares with the server warnings. Your skin prickles. You rub the bridge of your nose until sparks dance in the dark."
    hide dr_rowan_hale
    hide mina_kuroda
    hide sora_watanabe

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rapid beeps cascade; a heavy gust knocks something loose in the background]
    "You press one palm flat against the console because you need to anchor yourself. The decision matrix floats into your head like an old ledger: protect the system and risk ceding an emergency lever, or stall"
    "and try to hold democratic process at the cost of possible systemic failure, or throw open the memos and let political chaos decide."
    "Your pulse drums a compound rhythm. You think of ledger entries and the Beacon's lamp, and suddenly that steady sedimentary hope feels brittle — a thin glaze over something deeper and more fractured."

    menu:
        "Check the leaked memo more closely before responding":
            "You pull Rafi's file back up and skim the flagged clauses again, every legal fragment a weight in your chest."
        "Call Elias on the line and ask for a live status report from Verdant Terrace":
            "You hit Elias' line; his breathing rushes in and out, and you can hear shouted names and the slap of water against wood."

    # --- merge ---
    "Proceed to Verdant Terrace scene"
    # [Scene: Verdant Terrace | Same Time]

    scene bg ch11_e67f19_4 at full_bg
    # play music "music_placeholder"  # [Music: Percussive strings — urgent, staccato]
    # play sound "sfx_placeholder"  # [Sound: Rain on plastic, boots on wet metal, shouted coordination]
    "Elias Chen is a blur: commands, hands, pockets full of rope and radio batteries. When your call cuts through, his face is half lit by a battered lantern. He squares his jaw."
    show elias_chen at left:
        zoom 0.7

    elias_chen "We have people moving along Block C and the old pump house. If they cut the access paths, those folks are stranded. Aiko — we need to vote up or down, here, now. We can't leave this to a corporate toggle."
    "You can hear the crowd murmuring behind him as he speaks; someone calls a name, another voice asks about a child. Elias Chen sounds like a bell under strain — clear, resonant, near breaking."
    "You ask for numbers, and Elias Chen rattles them with a speed that betrays panic beneath the cadence."

    elias_chen "Twelve elders at Chapel Row, six med shipments, two generators—if those routes close, pumps die in hours. We're not asking for perfection; we need a delay for the council to meet, to route runners. Ten minutes."
    "You picture Mina's distribution maps pinned up in the Beacon's dim. Ten minutes feels like an eternity in the subbasement, but in a failing system, it is also a chasm."

    menu:
        "Tell Elias you'll try to buy ten minutes":
            "You hear Elias exhale like a wind leaving a bell. 'Do what you can,' he says. That's not satisfaction. It's trust, stretched thin."
        "Tell Elias the servers are warning and you're considering activation":
            "There is a crackle of disbelief. 'You're not just a scientist in a lab, Aiko. This is the neighborhood.' His voice trembles."

    # --- merge ---
    "Proceed to HelioCorp Glass Atrium scene"
    # [Scene: HelioCorp Glass Atrium | Same Time]
    hide elias_chen

    scene bg ch11_e67f19_5 at full_bg
    # play music "music_placeholder"  # [Music: Low synthetic hum — controlled, ominous]
    # play sound "sfx_placeholder"  # [Sound: Soft echo of his shoe against tile; a notification ping]
    "Rowan's presence on the line is a kind of pressure: polite, but absolute. He does not raise his voice; he needs not to."
    show dr_rowan_hale at left:
        zoom 0.7

    dr_rowan_hale "We can engage containment now. The system's margin curves back into safety. If you hesitate, the model predicts cascading failures. I know this is an impossible choice to ask of a neighborhood steward—"

    dr_rowan_hale "—but inaction in the face of an immediate, quantifiable risk causes loss."
    "You remember the night the storm took so much of the waterfront and what those words did to you then. Loss is not an abstract anymore — it is memory with names and taste."
    "Your chest constricts. You weigh the faces that flood into your mind: Elias Chen' sun-struck grin, Mina Kuroda's steady hands, Sora Watanabe's quiet warnings, the kid who leaves painted rocks outside the Beacon every morning. What counts as loss feels suddenly impossible to quantify."
    # play sound "sfx_placeholder"  # [Sound: A sharp alarm — the simulation reports a failing integrity node on the western barrier]
    # play music "music_placeholder"  # [Music: The electronic pulse ratchets up — more instruments layering, tempo accelerating]
    "Rafi bursts into the feed again, clipped and raw."
    show rafi_alvarez at right:
        zoom 0.7

    rafi_alvarez "If you flip containment, clause three kicks into effect. HelioCorp takes emergency control of distribution swaths for 'global stability maneuvers.' It is literal: access routes can be sealed under 'directed flow protocols.' You know what that means for the lower blocks."
    "He doesn't have to say it twice. You see the map: channels rerouted, neighborhoods isolated, a technical fix with a moral hole. The memos aren't ambiguous; they're coldly explicit. The leak spreads like oil across the console."
    "Elias Chen is on the verge of fury. Rowan never raises his voice. You are in the middle, as always, trying to balance ledger and people."
    "You reach for the toggle. Your finger hesitates over the activation key. The lab's air feels suddenly thin, and every second is a leak. The storm's roar is a mouth at the edge of the city."
    "You realize, in a raw, animal way, that no matter which choice you make, someone will call it betrayal."
    hide dr_rowan_hale
    hide rafi_alvarez

    scene bg ch11_e67f19_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A high, sustained tone from the warning cluster]
    "Your thoughts run jagged, one after another: the model's integrity, the elders at Chapel Row, the memos on Rafi's screen, Elias Chen's pleading, Rowan's quiet assurance, the Beacon's ledger. You can feel the swell of something fragile and maybe naive finally slamming into institutional iron."
    "You need to act. The system queues the activation with a countdown that will begin the second you authorize. The council cannot assemble in time if you hit engage. The model will likely hold if you engage; it may fail if you do not."
    show mina_kuroda at left:
        zoom 0.7

    mina_kuroda "If you close those paths, at least tell us which ones and let us try a path around them. If you engage, we will need a corridor plan and a comms window. If you delay, tell us so we can move generators."
    "Her words are a string of actionable items, the way someone who cooks for a hundred people keeps calm in a collapsing kitchen. They are also the world's smallest plea."

    menu:
        "Ask Rafi to push the memo to live social channels now":
            "You watch Rafi's fingers hover over 'publish.' He hesitates — then his hand moves as if dropping a stone into still water. 'Once it's out, it can't be unsaid,' he says."
        "Tell Mina to start moving the generator teams now, quietly":
            "Mina answers with a curt nod you can hear over the line: 'We're on it. We'll move under the tarps. No shout.' Her voice is a rope you can hold."

    # --- merge ---
    "Continue the decision in the Subbasement Data Lab"
    "The console's countdown cursor blinks patiently. The storm outside hammers in accelerating rhythm. On one hand, there's the near-certainty Rowan evokes: engineered safety, measurable preservation of infrastructure. On the other, the litany of people's names, packeted into your brain like fragile objects you can't risk losing."
    "Your heartbeat is a drumline pushing you forward. The lab's lights wash your features in shifting teal. The memos glow on Rafi's feed like a second moon — cold and indisputable."
    "You have three paths fully visible in front of you: press the toggle and secure the system (and, in the process, hand emergency weight to HelioCorp's contingency language), stall and attempt a neighborhood vote that may"
    "buy a sliver of democratic legitimacy but risks overload, or make the memos public and spark a political fire that could delay any immediate fix while also exposing rotten wiring."
    "None of them is clean. Each exacts a toll."
    "You feel Elias Chen's anger like heat on your neck. Rowan's composure like ice in your hand. You think of ledger entries and of the Beacon's lamp and the way the neighborhood once stood together in"
    "the face of lesser storms. You think of the night you almost lost everything and how it hollowed you into someone who still believed rules could hold."
    "The system is waiting. The storm is waiting."
    # play music "music_placeholder"  # [Music: Climactic dissonance — strings and synth converge into a sharp, unresolved chord]
    # play sound "sfx_placeholder"  # [Sound: The clock on the console ticks louder, counting down in a room where sound has become consequence]
    "You put your hand over the activation key and feel the resonance of the lab under your palm. You understand that your choice will write the next line in the Beacon's ledger — whether it's a"
    "clean function or a dirty compromise, whether the city's ears hear you or someone else."
    "This is not a moment for small truths. This is a moment where you will choose how the neighborhood's story continues."

    jump chapter12
    return
