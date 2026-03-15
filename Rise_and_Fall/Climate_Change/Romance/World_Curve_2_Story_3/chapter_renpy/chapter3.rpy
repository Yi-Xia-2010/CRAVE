label chapter3:

    # [Scene: Town Hall | Night]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, brooding cello with a distant kettle-drum thud]
    # play sound "sfx_placeholder"  # [Sound: Rain on the roof, a loose window shutter tapping like a nervous heartbeat]
    "You sit in the back row, maps folded in your lap, the creak of the old chair precise beneath you. Your pencil is warm from being between your fingers; the compass your father gave you rests against your thigh like ballast."
    "The room smells of oiled wood and paper, the kind of warm, buried smell that remembers every vote ever taken here. People crowd the benches: fishermen with salt on their cuffs, shopkeepers with rain-soaked collars, a"
    "smattering of younger faces with clipboards and lamps. Conversations are low and tight as braided rope."
    "Aria Chen steps forward under the council's muted fanfare, slate coat sharp against the warm wood. Her slides bloom on the projector with a practiced, polished clarity — renderings of promenades and glass-fronted workshops, graphs that tidy uncertainty into straight lines."
    show aria_chen at left:
        zoom 0.7

    aria_chen "Greyhaven cannot drift forever. Investment will bring jobs, modern defenses, and a tax base to keep our schools and clinic open. We have a narrow window before lenders withdraw interest. This proposal funds both protective infrastructure and redevelopment."
    "You watch her hands. They are measured, economical. Her jade pendant catches the projector light and flakes a pale green across the lectern. Her voice is precise; it lands in the room like a lever being set."
    "A councilor murmurs agreement. An older woman near the aisle shifts, jaw working. You feel the room tilt between fear and relief; you can taste it as metallic salt in the back of your mouth."
    "Jonah Merrick rises from the crowd; the room softens as if remembering a quieter sea."
    show jonah_merrick at right:
        zoom 0.7

    jonah_merrick "We didn't get here by being tidy. We got here by taking our lines, day after day, by knowing where the shoals lie because our feet have mapped them. You—' (his gaze finds you briefly) '—you don't sell the harbor the way you sell a ledger. These are lives."
    "There is a sympathetic ripple. Someone coughs, someone huffs. Jonah's voice carries more ledger of a different kind: years and lines and weathered maps tattooed into muscle memory."

    aria_chen "Jonah, I respect the traditions. But respect doesn't pay for ambulances when the road washes out. The proposal is a package; we can include community jobs — training programs —"

    jonah_merrick "Training's fine. Trading a shoreline for a parking garage is not. That's not defense; that's giving up the map."
    "Aria's smile is small, almost constitutional."

    aria_chen "This is a negotiation between what we've known and what we need to survive."
    "Your turn comes. The living breakwater model — a rough, tactile cluster of woven faggots, reed roots, and not-quite-symmetrical stones — sits on the small table before you. It's not slick. It smells faintly of river"
    "silt and rope-work. A few young volunteers helped knot it; a child's smudge of paint still sullies one edge."
    "You stand because the room won't let you remain sitting and you have to set the thing down to use your hands. Talking with your hands is how you measure distances you can't draw on paper."
    show isla_morgan at center:
        zoom 0.7

    isla_morgan "This isn't about nostalgia. It's about dynamics. A wall at the harbor mouth shifts currents; it starves mudflats, kills reeds — and the harbor dies slowly and the fisheries with it. Living shorelines absorb energy, rebuild substrate, give people jobs that keep knowledge local. They adapt with the sea instead of trying to chase it back."
    "Councilors lean forward. Someone near the door whispers, 'Labor, not concrete,' like a prayer."

    aria_chen "The data matters, Isla. But there is also a timeline. You say 'adapt with the sea,' but preparedness is also what keeps people—' (she searches the room and lands on a young mother with a sleeping child) '—keeps people in their homes now. Can your proposal be built fast enough? Can it be insured? Will it keep the clinic open?"
    "You hear the questions as if they scrape the inside of your skull. They are practical; they require answers that are part engineering, part politics, part human endurance."

    isla_morgan "It can be phased. Community-built modules can be installed in months with local labor. Insurance is a policy question — but ecologically, it's less risky than concrete that reallocates erosion downcurrent. And the clinic — training people to maintain and own the structures keeps both jobs and the social fabric intact."

    aria_chen "Phased is time. Time is the currency investors are counting. A phased approach might look like delay to the public. It can be spun as indecision."
    "Her tone is flat; the edges are not hostile but deliberate. Her reaction is unreadable in that way that sits heavy on a room — not a closed door, exactly, but a window with blinds halfway down."

    menu:
        "Lean into the technical explanation; pull up your sediment cores and diagrams":
            "You reach for the case of sediment cores. The room quiets further, eyes tracking the physical evidence like moths to a lamp. Aria's jaw tightens a fraction, and a younger councilor nods appreciatively — science in motion."
        "Appeal to the room's memory; tell a short story about your father's last season":
            "You let the technical words go for a second and tell Jonah's old weather story — the one everyone remembers. Faces soften, the mother near the aisle closes her eyes as if already remembering. Aria inclines her head, unreadable, but the pulse of the room shifts toward attachment."

    # --- merge ---
    "You choose, or do not choose, and the room answers you with its pulse: some faces lean closer to your hands and model; others retreat behind practical numbers and the gleam of stage-renderings."
    "Outside the chamber doors, the promenade hums. You notice it in the way footsteps begin to align like tide lines."
    # [Scene: Promenade | Night]
    hide aria_chen
    hide jonah_merrick
    hide isla_morgan

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant chants and paper flapping; Luca’s voice threaded through with laughter and urgency]
    # play music "music_placeholder"  # [Music: A single acoustic guitar, slightly out of tune, attempts a chorus beneath the wind]
    "Luca Moreno stands beneath a battered lamp with Ravi and Maya, flanked by a small cluster of people. He is animated — fingers sketching shapes in the air as if he can build the world with"
    "gestures. His red bandana is around his wrist. He hands out laminated cutaways and a stack of printed diagrams with smiling, earnest energy."
    show luca_moreno at left:
        zoom 0.7

    luca_moreno "We're not asking for unrest. We're asking for visibility. If the council thinks votes come from glossy renderings, let's bring them the people who will build the work. If they think timelines matter more than lives, we'll show them both."
    show ravi_patel at right:
        zoom 0.7

    ravi_patel "We can tape the promenade with timelines, show step-by-step how each phase could be funded. People respond to a plan they can hold."
    show maya_morgan at center:
        zoom 0.7

    maya_morgan "And we can do job sign-ups tonight. If people see a guaranteed month-to-month work plan, they'll come."
    "You stand just inside the doorway of the town hall, feeling both worlds — the neat, lit chamber and the wet, ragged choir outside — prickle at your skin."
    "Luca catches your eye from the lamp glow, his face the kind that invites mischief even when the stakes are hard."

    luca_moreno "You doing okay in there? Do I pull people into the chamber, or do you need us to keep the crowd outside calm and ready?"
    "You can see the need in his eyes — not for your permission so much as for your alignment."

    menu:
        "Tell Luca to keep the workshop outside; focus the chamber":
            "You give a small nod. Luca's shoulders relax and he throws his voice wider, pulling the crowd into chants that sound like weather. Ravi starts passing around sign-up sheets with a practiced grin."
        "Step outside and help organize the crowd; rally presence matters":
            "You step into the night and the air hits your face with salt and rain. People fall into line beside you as if you're a familiar tidal marker. Luca hands you a mic and the sound of your voice trembles on the lamp posts — intimate, raw, and immediately human."
        "Split time — send Maya to coordinate sign-ups while you return to present":
            "You point to Maya and she understands, biting her lip but moving into the swell of people. Inside, you return to the lectern with a steadier hand, and the room feels like it can breathe a fraction more."

    # --- merge ---
    "Inside, the council murmurs about optics and legalities. Outside, phones record, hands twist into small projectiles of leaflets sent into the humid air. The crowd's energy is a kind of weather that can either push a window open or batter it closed."
    "Back in the chamber, Aria fields questions with a diplomat's timing. Her answers are tidy but include a hardness: a repeated phrase about 'external funding windows' that runs like a metronome through the meeting."

    "Council Chair" "I will open the floor to Isla Morgan to present her living breakwater pilot."
    "You move your model, and you move your voice. You do not perform; you explain. The lights feel hotter now that you are the one under them."
    hide luca_moreno
    show isla_morgan at left:
        zoom 0.7

    isla_morgan "This pilot is not a panacea. It is a living system built with local labor, iteratively tested. It reduces wave energy, traps sediment, and provides habitat — which over time increases natural accretion and reduces erosion. The modules can be constructed with local materials and maintained by local people."
    hide ravi_patel
    show aria_chen at right:
        zoom 0.7

    aria_chen "What's your estimated cost per linear meter? Who signs off on compliance? Who pays if a module fails inside its warranty window?"

    isla_morgan "Short-term costs are comparable to small-scale, community grants and can be offset by training funds and local labor credits. Failure is a shared responsibility — the model lives because the community owns it. Compliance is negotiated with state coastal agencies, not an overnight fix, but a resilient, scalable approach."
    "A council member interrupts."

    "Council Member" "People are tired of negotiations. They want certainty. How do you answer that?"
    "You feel the question, heavy as a sluice gate. It's not aimed at data; it's aimed at a human need to feel safe."

    isla_morgan "Certainty is a promise we used to make when the sea behaved like it did a century ago. This gives us a form of accountable, durable safety. It isn't certainty; it's a practice that grows stronger if we steward it. The alternative is a fixed structure that redistributes risk."
    "There's a long silence after you speak. You can sense the room's calculation; some faces register relief at having something tangible to oppose Aria's renderings; others fold their arms as if the conversation has become too long to tolerate."

    "Jonah leans forward and adds, quietly but with iron" "Give the people work that keeps the harbor intact, not projects that make it someone else's problem."
    "Aria watches Jonah with something close to respect and the same coolness you'd seen before. Her response is compact."

    aria_chen "We could — in theory — integrate the proposal into the development as an on-site pilot. But that requires timeline alignment and clear metrics. That's the compromise I'm prepared to discuss."
    "The word 'could' hangs like a low cloud. It invites a bridge and also masks the potential to swallow the project into a larger, faster machine."

    "Council Chair (firm)" "Given the stakes, the council will postpone a final vote tonight. However, we will authorize a fast-track review process and require both parties to submit implementation plans within ten days. This review will focus on feasibility, timelines, and funding alignment."
    "A soft, collective exhale circulates like wind settling. Postponement is both a reprieve and a sharpened pressure: ten days is a narrow margin. Fast-track review translates to meetings, legal wrangling, the sprint of bureaucracy — and the attention of investors."
    "You feel the room close in: eyes on Aria, on you, on Jonah, on the pages of a calendar that will not fold quietly."
    # play sound "sfx_placeholder"  # [Sound: A far thunderclap, like a punctuation mark]
    "You leave the Chamber while the last questions flurry. Outside, the promenade is no longer only discussion; it's vinyl and tape and people arranging themselves into a human shoreline. Luca meets you, rain water collecting in the bend of his neck like small puddles."
    hide maya_morgan
    show luca_moreno at center:
        zoom 0.7

    luca_moreno "They postponed. Fast-track review. Ten days."

    isla_morgan "They set the timeline. They gave us a sprint."
    "Luca's face tightens where humor usually lives. For once his optimism has a visible crease."

    luca_moreno "We can fill those ten days. We can make the review mean something real rather than letting it be a checkbox."
    "You slide your fingers into your pocket. The compass is heavier than it was in the lab. It presses into your palm with the memory of your father's hands — rough, sure. The weight is familiar as a pod of pressure beneath the ribs: responsibility, guilt, care."

    isla_morgan "Or we can lose the narrative to a packed deck of renderings and policy-speak. The review could just be a stamp that makes things look legal."
    hide isla_morgan
    show maya_morgan at left:
        zoom 0.7

    maya_morgan "You don't have to do this alone, Isla."
    "Her voice is small, the kind of relief that is both asking and offering. The wet air tastes of iron and promise. The lamp posts smear passerby faces into watercolor, and behind them the sea is a darker, rising plane."
    "Jonah stands beside the pier railing, watching the horizon as if it will provide an answer. The storm line is a bruised band, moving like a thought."
    hide aria_chen
    show isla_morgan at right:
        zoom 0.7

    isla_morgan "Ten days. A review that could save time — or could swallow the work. A postponement that buys oxygen but tightens a noose."
    "Your chest tightens. The town has divided itself into small weather systems, and you are standing at the center of one, exposed."
    # [Scene: Harbor Pier | Night]
    hide luca_moreno
    hide maya_morgan
    hide isla_morgan

    scene bg ch3_98c6f2_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind carving across rope, a distant siren swallowed by rain]
    # play music "music_placeholder"  # [Music: Sparse piano chords, melancholy and slow]
    "You step out onto the pier. Rain pearls along the worn wood. Your fingers close around the compass. It is cold and solid. You think of your father's hands holding the same object in another storm, the way he keyed his breath to the rhythm of waves."
    "The choice waits with the acute, clinical clarity of a tide chart: move now and turn the town toward public pressure; attempt a technical partnership with Aria and risk being absorbed; or withdraw to the lab to harden your case and possibly lose the immediate momentum and trust."
    "The wind pushes at you like an opponent. The town's lamps dot the promenade; people move like small currents around the harbor. Somewhere Elena from the bakery is arguing with a neighbor about insurance; someone else is taping a 'Hands Off Our Harbor' sign to a lamppost."
    "Your mind runs through consequences like beads: an energized rally could split families but make the town visible; a joint review could open compromises but risk co-option; waiting could sharpen the science but leave hearts distrustful."
    "Luca's voice carries from the promenade, telling a gaggle of teenagers where to stand. Maya stands at your elbow, quieting the small crowd beside her with a look. Jonah hums an old tune in a way that sounds like blessing and warning."
    "You inhale sea-salted air, the smell of wet rope and diesel and the slim, clean scent of algae. The compass is heavy. The rain is steady."
    "You have a decision to make."

    menu:
        "Lead a public protest rally with Luca and Ravi to force the council's hand.":
            jump chapter4
        "Propose a negotiated, technical joint-review with Aria to find compromise.":
            jump chapter7
        "Withdraw to Tidewatch and collect more, harder evidence before acting.":
            jump chapter10
    return
