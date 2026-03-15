label chapter12:

    # [Scene: Saltworks (Reclaimed Marsh Labs) | Pre-dawn]

    scene bg ch10_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low sluicing of the tide through reed channels; distant gulls; a humming inverter]
    "You are already awake when the knock comes—three soft, urgent taps that sound too polite for the gravity behind them. The Saltworks smells like wet wood and cooling metal; your hands still smell faintly of brine"
    "from the tide garden you were tending yesterday. The coral scarf is looped tightly against your throat, a ritual of steadiness."
    "You open the crate of tools and sit at the workbench. The whistleblower waits in the doorway, shape hunched against the coat, eyes rimmed with sleeplessness. Their face is a map of nerves and something like resolve."

    "Whistleblower" "I—I'm sorry to drag this to you, Mira. I couldn't go to Cass. I couldn't... I thought you should see it."
    "Your stomach drops the way it does when a storm line appears sooner than forecasted. This is the thing you'd feared in the quiet hours: fine-print promises, easements that breathe private property across public wetlands, clauses that let developers control access and amenities under the guise of 'resilience management.'"
    "You take the papers like they'd burn. The smell of printer toner and damp paper is absurdly mundane for what they contain—the language of legal inevitability, the tight, smooth logic that erases people."
    "You scan the first page. Your heart keeps its steady, stunned rhythm. The whistleblower watches your face, trying to read whether you'll recoil or read aloud."

    "Whistleblower" "There's more. Emails—redactions, but the dates match storm responses. They call relocations 'optimization.' They've already scoped easements that would hand over boardwalk access, communal docks...' (Their voice cracks, then steadies.) 'I didn't want to be the one who watched my neighbors lose the right to walk the water."
    "You don't ask how they got the documents. You don't ask for names. There's a small, practical voice in your head—Jun's sharpness, Aunt Lila's stories of when deeds were signed in ink and surprise—and a larger,"
    "hollower fear: if this goes public, Cass will turn it into a battle she knows how to win. If it stays quiet, the town could be sold out in slow increments."
    "Noah lopes in, rubbing sleep out of his eyes, drawn by the light like a gull to a spill. Saltworks team members gather—Jun, blinking into the lamp; a couple of others with jackets smelling of coffee and salt. The lab smells like work and worry."
    show noah_rivera at left:
        zoom 0.7

    noah_rivera "Holy—what is that?' (He glances at the pages, then at you.) 'We call Jun. We call the council. We post it."
    show jun_park at right:
        zoom 0.7

    jun_park "Slow. If this leaks without context, people panic and Cass uses it to paint us as conspiracy mongers.' (His hands flutter; the classroom teacher's impulse to structure chaos is visible.) 'We need a plan—chain of custody, verified sources. We get counsel."
    "You feel every option like a bruise. Your internal monologue runs in short waves: leak -> outrage -> legal war -> unknown. negotiate quietly -> maybe protections -> maybe derailment by the firm. step away with Elias -> personal survival -> community abandoned. Each path radiates loss."

    menu:
        "Read every page, now":
            "You spread the documents under the lamp and read until the ink blurs. Each line tightens something in your chest. The team watches you like the tide checks the shore—expectant, powerless."
        "Photograph and catalog, then step away to think":
            "You take out your phone, snap clean shots, and tuck the copies away. The act of cataloging buys you a few measured breaths, a thin barrier between impulse and action. The room waits."

    # --- merge ---
    "The narrative continues after the choice."
    "You choose cataloging. Order feels like agency. You make copies, stamp timestamps in your head, and tuck originals back into their envelope. The whistleblower's hands tremble as they fold the empty sleeve."
    "Elias Park arrives without flourish—just a familiar scuff, then the low humor he usually brings to mornings. Today his curls are pressed damp from fog; his amber eyes are wider than usual."
    show elias_park at center:
        zoom 0.7

    elias_park "You called me two in the morning—if this is about the prototype getting nicked by kids, I swear—"
    "You don't let him finish. You hand him a copy. There's a look you can't read—something like sympathy, something like fear of being dragged into another failure."
    "Elias Park: (softly) 'We can use this. Or it can use us. You know how headlines get bent.'"
    hide noah_rivera
    show mira_santos at left:
        zoom 0.7

    mira_santos "I asked you to look into rumors, Elias. I didn't—' Your voice cuts off. Words feel insufficient. 'I didn't know this would be the shape rumors took."
    "Elias Park: (searching) 'I know. God, Mira. If this is real, we can—' He holds back, and you know a past professional wound opens under the surface. 'We can trace the chain. We can find the signatories. I've got contacts who can check redactions without dragging it to the press.'"

    jun_park "We need legal eyes on it before anyone breathes 'leak.'"
    "Aunt Lila arrives not because she was summoned but because she always knows when the town's center of gravity shifts. Her cardigan smells faintly of lavender and yesterday's kettle. She moves around the bench slowly, eyes scanning the margins as if reading them aloud."
    hide jun_park
    show aunt_lila_santos at right:
        zoom 0.7

    aunt_lila_santos "This is a betrayal.' (Her voice is quiet and ancient, the kind that carries the weight of generations.) 'They wrap exile in promises. They think they can translate our lives into parcels. We know this language because we've been living it. We also know how it feels to choose between survival and what it costs."
    "The Saltworks team looks to you. The whistleblower stands like a guilty saint—relieved and terrified in equal measure. Your obligation tightens: to truth, to people, to the fragile fabric of the town."
    "You taste metal, though there's no blood—just adrenaline and the metallic certainty of accountability."
    # [Scene: Harbor High Rooftop Greenhouse | Mid-morning]
    hide elias_park
    hide mira_santos
    hide aunt_lila_santos

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Muffled city sounds below; the greenhouse is a soft, humid bubble; a distant council lawnmower]
    "You come up here because it's neutral ground—no lab tools, no microphones, only wet leaves and old glass. Elias Park follows, shoulders tight. Aunt Lila lingers at the doorway, hands folded against her belly."
    "The greenhouse smells like warm earth and citrus leaves. It calms something in you that the Saltworks couldn't touch. But the calm is brittle."
    show elias_park at left:
        zoom 0.7

    elias_park "You could go public. Quick, sharp. It'd throw a spotlight on Cass. People would be furious."
    show mira_santos at right:
        zoom 0.7

    mira_santos "And then what? We weather the backlash, the lawsuits—' You breathe in. 'We risk every person who would testify, every elder who can't afford a legal fight."
    "Elias Park: (voice softer) 'I know. I know the stakes. I—' He stops, looks at you, and there is a flicker of the private Elias—the one who has paused in front of your hand in the"
    "dark and chosen to look away. 'If you asked me to leave with you, I would. But we don't know if that saves anyone. Or just ourselves.'"
    "You feel flayed. The choice stretches out, cold and precise. Romance and duty tangle; the present demand of love presses against the long arc of responsibility."
    show aunt_lila_santos at center:
        zoom 0.7

    aunt_lila_santos "You have always carried your people's stories like a lamp. If you put it down now because leaving seems easier, they'll remember the lamp unlit.' (She doesn't scold; she frames reality.) 'But if you burn too bright without a plan, you may scorch what remains."

    elias_park "We could try a controlled release—verify with a trusted reporter, prepped legal counsel. It's messy, but maybe it balances exposure and protection."

    "Jun's voice from the stairwell" "Or we bring it to sympathetic councilors first. Build an amendment—get something enforceable."
    "Your chest aches. You picture families on the boardwalk, Aunt Lila's hands making bread in a kitchen you grew up in, Noah's laugh at a summer festival that might be engineered away."

    menu:
        "Call a trusted reporter now":
            "You reach for your phone. The idea of a headline is a clean strike—expose, mobilize. Also, it feels like flinging yourself into surf without a lifejacket. Elias reaches for your wrist, not to stop you so much as to steady himself."
        "Reach out quietly to sympathetic councilors first":
            "You thumb a contact list of councilors who have shown cracks in their armor. It's slower, feels diplomatic—almost cowardly against the truth, but it could build enforceable protections before the storm of public opinion begins."
        "Decide to sleep on it":
            "You say you need time. Time feels like a betrayal; time also feels like the only way to avoid burning everything to ash. Eyes study you for what your delay will mean."

    # --- merge ---
    "The narrative continues after the choice."
    "You take a breath and don't call the reporter. The breath you hold is heavier than the humid air. You tell them you'll reach out to councilors—partly because it buys time, partly because it feels like the smallest betrayal that still stakes a claim to the town."
    "Elias Park watches you choose. He doesn't smile. He leans his forehead briefly against the glass, leaving a small press of warmth that the sky will take back."

    elias_park "If we go that route, we'll need airtight proof. I can trace metadata. Jun can patch community testimony. We need a lawyer who's not on Cass's payroll."
    "You nod. You already know who that lawyer is in town—one who takes folks on a rumpled moral compass. But you also know the kind of stone Cass can move when she chooses."

    aunt_lila_santos "Promise me this; don't let them privatize our grief. If you must choose quiet, make sure it's not silence that lets them sign away our memory."
    "You hold that like a benediction. You think of your mother's coral scarf—the way it wraps memories close."
    # [Scene: Marrow Bay Boardwalk | Late afternoon — the light low, sky bruise-soft]
    hide elias_park
    hide mira_santos
    hide aunt_lila_santos

    scene bg ch10_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Boardwalk chatter; a distant generator; the soft slap of waves]
    "You walk the line of the boardwalk because decisions like this should be walked through, not just thought through. The paper copies of the documents are in the small satchel you force to feel heavier than"
    "air. The wind claws at the scarf; gulls speak in a language you translate as warning."
    "Neighbors cluster in the faded light—some curious, some wary. You see faces you know by childhood: the woman who runs the bait shop, the teenager you taught to read tide charts. Your hands tingle with the knowledge that this single file of pages could change everything for them."
    "Elias Park keeps pace beside you, but there's a distance in his gait you can't name—neither closeness nor retreat. It's practical; it's a risk-calculation."
    show elias_park at left:
        zoom 0.7

    elias_park "We can go to the press. We can go to council. We can walk away."
    "Mira Santos: (quiet) 'We have to decide now. This can't wait like a tide told it would come tomorrow.'"
    "He meets your gaze and holds it. For a moment, the private world you sometimes find in his eyes—a place where experiments were failures and apologies were inventions—opens, then closes."

    elias_park "Mira. If you leak this, your name will be in the middle of it. If you don't, people will lose access, sometimes piece by piece. If you leave—' He falters. 'If you leave with me, I'm not promising you'll come back."
    "The boardwalk smells of sea-salt and frying dough and something else—loss, ripe and ready. Aunt Lila's hands, rough and sure, clasp yours. Her touch is a tether."
    show aunt_lila_santos at right:
        zoom 0.7

    aunt_lila_santos "Whatever choice you make, make it so that the town remembers why it was worth defending. Not for fame—so they can keep their stories."
    "You look at the papers in your satchel again, for the thousandth time. The ink seems to press into your palms. A low, inevitable despair sits under your skin: any route carries harm. There is no purely heroic answer here—only trade-offs and fractured maps."
    "Your pulse is steady enough. The wind plays with your hair. The arousal of the day has been mid—measured, building. Now it rests at its apex, not frantic but heavy as a wave about to break."
    "You stand at the seam: public exposure, quiet negotiation, or private escape. Each path fractures something."

    menu:
        "Publicly leak the contract to the press and mobilize civic outrage.":
            jump chapter13
        "Use the documents to negotiate an enforceable amendment quietly with sympathetic councilors.":
            jump chapter14
        "Prioritize personal stability: step back from the fight and plan with Elias to leave for another town.":
            jump chapter18
    return
