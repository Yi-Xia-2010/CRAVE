label chapter15:

    # [Scene: Negotiation Room | Late Afternoon]

    scene bg ch8_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Staccato rain against glass, the projector’s soft mechanical whirr, distant gulls cut off by the storm]
    # play music "music_placeholder"  # [Music: Sparse, rapid strings building tension]
    "The room smells of wet paper and reheated coffee. Light from the projector throws blue rectangles across faces—maps, clauses, and the same faint hope and calculation that cling to everyone here."
    "You remember how the projector ticked in the last meeting, how the phrase “not be patient indefinitely” landed like a weight. That memory sits at the base of your throat now, a steady, sharp ache that sharpens every syllable you hear."
    "Corinne Voss sits at the head of the table with her hands steepled, the Voss dossier open before her. Tamsin’s tablet glows with annotated edits. Jules leans against a pillar, camera strap loose; Luka Maren stands half-turned toward you, sleeves rolled, a shadow of conflict on his face."
    show corinne_voss at left:
        zoom 0.7

    corinne_voss "We've proposed flexible language for the pilot so adjustments can be made as data comes in. Flexibility is governance in practice."
    "The words are smooth, delivered like a product demo. Flexibility as a safeguard; flexibility as a wedge."
    "You clamp your jaw before the rebuttal forms. You have arguments—binding funding, community oversight, clear sunset clauses—but artful words like 'flexibility' are designed to sound reasonable while eroding protection."
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "Flexibility can be a loophole, Corinne Voss. When it becomes convenient to shift priorities, 'flex' becomes a doorway. We need legal teeth. Without them, TideLab and our neighborhoods are bargaining chips."
    "Corinne Voss’s eyes tighten—an almost imperceptible motion that makes the projector light flare."

    corinne_voss "Binding everything at once stalls implementation. We want to move—real sensors, wetland pilots; we can’t do that if we tie every step with litigious anchors."
    show tamsin_cho at center:
        zoom 0.7

    tamsin_cho "Both of you are right. The council will want evidence of progress—money moving, sensors deployed. But they also can't ignore the town meeting last week. There's pressure on all sides."
    "Your pulse picks up. The conversation spirals into clauses and counters, each phrase quickening the room's tempo. You pull out the red-lined language you drafted—three clauses you believe are non-negotiable."

    amaya_reyes "Clause one—guaranteed funding schedule, disbursed to municipal accounts with community oversight. Clause two—enforceable sunset clauses with rollback provisions. Clause three—an independent audit process with naming rights for community representatives."
    "Corinne Voss scans them, fingers trailing the page as if weighing texture."

    corinne_voss "Those are aggressive. We can do oversight in principle. As for sunset clauses—let's pilot for two years and revisit. It's practical and opens faster pathways to implementation."
    "The word 'practical' drops like a match in dry grass. Tamsin exhales, caught between two worlds. Jules's phone buzzes; he glances at it and then at you."
    hide corinne_voss
    show jules_park at left:
        zoom 0.7

    jules_park "Amaya Reyes—there's chatter. Someone's got a redacted term sheet. A reporter pinged me."
    "Your chest tightens. You already know what leaks do: they drag processes into public light, force framing, and can reshape leverage overnight."
    hide amaya_reyes
    show luka_maren at right:
        zoom 0.7

    luka_maren "I've been offered a grant. From Voss. Conditional collaboration with their tech teams. It's... substantial. It would fund the sensors I can't otherwise build at scale."
    "The sentence hangs. The room seems to inhale."
    hide tamsin_cho
    show corinne_voss at center:
        zoom 0.7

    corinne_voss "Luka Maren's work is excellent. We want to scale it ethically and properly. Collaboration offers resources and mentorship."
    hide jules_park
    show amaya_reyes at left:
        zoom 0.7

    amaya_reyes "Luka Maren—did you tell them you'd collaborate? Did you sign anything?"

    luka_maren "No. Not signed. I told them I'd consider it if community terms are protected. I didn't expect them to use it now. I didn't—"
    "He breaks off. His hand finds yours on the table—an action that feels private in a public room. Your fingers curl around his, warm and vulnerable."

    amaya_reyes "You should have told me sooner."

    luka_maren "I was trying to—protect you. Protect TideLab. I thought I could negotiate both sides. I was wrong to hide it."
    "The exchange between you stretches, pulls at something delicate. Multi-turned, tense: his optimism and fear pressing against your protectiveness."

    menu:
        "Reassure Luka quietly":
            "You tighten your grip for a moment, then let your voice go small. 'We navigate this together,' you say. The room quiets around the two of you; Jules gives you a look that mixes relief and reproach. Tamsin's tablet blinks like a metronome."
        "Confront him sharply about secrecy":
            "You pull your hand back and your words are louder than you mean them to be. 'Secrets cost us leverage, Luka Maren,' you say. He flinches; Corinne Voss's mouth tightens. The air cools—an opening has been closed."

    # --- merge ---
    "The meeting continues."
    # [Scene: Negotiation Room | Night — Small Hours]
    hide luka_maren
    hide corinne_voss
    hide amaya_reyes

    scene bg ch8_6b08b4_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain increased to a relentless drum; an anxious hum from the building's ventilation]
    # play music "music_placeholder"  # [Music: Rapid percussion, swelling into urgent chords]
    "Jules's phone emits another buzz; he steps out into the corridor and comes back pale."
    show jules_park at left:
        zoom 0.7

    jules_park "It's live. Not the full thing—redacted—but it's on a local feed. The headline's already framing it as 'Voss and Town Strike Quiet Deal.' People are calling it a coup or a sellout, depending on the thread."
    show tamsin_cho at right:
        zoom 0.7

    tamsin_cho "Who leaked it?"

    jules_park "I did. With a reporter I trust. I redacted sensitive names—kept it to the bits that matter: funding flows and vague oversight. The point was to see how the town reacts when they can read risk on paper."
    "Silence. The ethical calculus triples."
    show amaya_reyes at center:
        zoom 0.7

    amaya_reyes "You what? Jules, that could destroy mediation. Or it could force transparency. We should have had a plan—"

    jules_park "We don't get plans. We get windows and moments. This was one."
    "Your heartbeat drums loud in your ears. Corinne Voss's expression goes from measured to sharply measured."
    hide jules_park
    show corinne_voss at left:
        zoom 0.7

    corinne_voss "Leaking internal documents is reckless. It jeopardizes collaborative trust. If your side intends to weaponize press, that will affect negotiations."

    tamsin_cho "We need to contain this narrative—explain context, not inflame. Amaya Reyes, if this inflames the council, members who feared fiscal shortfalls will pivot toward Voss's assurances."
    "You think of Mateo and Mrs. Calder. You think of the ledger: names, livelihoods, small houses on stilts. Every public headline sketches a possible fractureline."
    "Jules nods, guilty and resolute."
    hide tamsin_cho
    show jules_park at right:
        zoom 0.7

    jules_park "The reporter wanted the term sheet. I stripped the parts I knew would endanger people. I wanted to make clear what 'flexible language' looks like."
    "Corinne Voss leans forward, the light carving her features like a blade."

    corinne_voss "We can address this. Clarifying statements. We can—"
    "Your phone buzzes with a council member's terse message: 'Public opinion hardening. Some favor Voss. Price concerns.' The words feel like ice in your mouth."
    hide amaya_reyes
    show tamsin_cho at center:
        zoom 0.7

    tamsin_cho "You're at a pivot. Keep pressing for legal guarantees now and risk Corinne Voss walking—maybe national attention helps. Or accept a watered pilot and get resources but with future risk. Or step back entirely and demand formal review, but then Voss might act without us."
    "Her voice sketches the fork you already feel as an ache. The room tightens. The rain feels louder, like a drumroll."
    "Luka Maren's eyes meet yours—something unspoken: fear of losing the resources he needs, fear of losing trust, fear of losing you."
    "Corinne Voss's reply is mercilessly calm."

    corinne_voss "We are ready to begin sensor deployment with provisional agreements. We prefer collaboration, but we are not beholden to prolonged stalemates. Our window for pilot sites narrows with weather and investor timetables."
    "You sense the room leaning. Council members you thought steady are calculating whether immediate relief is worth future erosion."
    "Your internal monologue speeds: legal leverage would require time and risk; public pressure could bring allies but also animus. Acceptance secures immediate help but hands procedural footholds. Walking away could force oversight but invites unilateral action."
    "Every syllable now feels like a lever pulled on a machine that's already moving."

    menu:
        "Call an immediate public press briefing":
            "You stand abruptly; papers rustle. 'We will hold a briefing at dawn. Bring the term sheet, the audit plan, and community spokespeople,' you say. Tamsin's face tightens in worry; Jules looks like he's been vindicated. Corinne Voss's jaw closes. The room hums—action set into motion."
        "Demand a closed legal review first":
            "You keep your voice low. 'We file for an independent review tonight. No public statement till counsel signs off.' Tamsin breathes out—relief and frustration together. Jules looks disappointed but nods. The tempo slows; a new course of patient machinery begins."

    # --- merge ---
    "The meeting continues."
    # [Scene: Voss HQ — Corinne’s Office | Night]
    hide corinne_voss
    hide jules_park
    hide tamsin_cho

    scene bg ch8_6b08b4_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Muffled city traffic, rain like fine grit]
    # play music "music_placeholder"  # [Music: Sparse piano notes, sharp and insistent]
    "You walk into Corinne Voss’s office because negotiation now requires endurance over theatrics. Her posture is all controlled lines; the rain makes the glass into a net of lights."
    show corinne_voss at left:
        zoom 0.7

    corinne_voss "We cannot have legal show trials slowing necessary work. The pilot is a pathway to protect infrastructure. If the town chooses obstruction, Voss will redirect projects to other jurisdictions."
    "The implication is a corporate shrug that translates to displacement. You have heard this tactic before; it is the economy of pressure."
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "If we agree to that pilot, we write sunset clauses into the bylaws. We fund the audit now. We name community representatives to control disbursement. Those are non-negotiable."

    corinne_voss "And if the town refuses, what then? Do you want to risk no sensors, no wetland pilots, and wait for litigation? Risk leaves communities unprotected while lawyers argue in court."

    "Luka Maren's voice comes from behind you when he arrives" "Amaya Reyes—I'm not asking for a blank check. I want to build sensors that can monitor the marshes and give us weekly actionable data. Without funding, I can't scale in time for the season."
    "His hands are empty but open. The choice sits between them like an offered tool and a dare."

    amaya_reyes "We could accept the pilot with the conditions I listed. But I won't pretend that's risk-free. We need guarantees enforceable in binding documents, or it's not protection—it's a promise."
    "Corinne Voss leans back, a faint smile as if pleased by the negotiation's heat."

    corinne_voss "We can draft language that satisfies appearance and process while preserving operational agility. It's a compromise—meaningful, but not immobilizing."
    "Her eyes flick to you like a scale testing weight."
    show tamsin_cho at center:
        zoom 0.7

    tamsin_cho "The council meets at dawn. Some of them are already leaning toward Corinne Voss. They see jobs in sensor assembly, funding for docks. We have hours to make this not a split."
    "Your breath comes fast. Rain on the glass now sounds like applause for an ending yet to come."
    "You feel every margin of the ledger in your chest. You picture the town—windows lit, boats tied, children on patched bicycles. You imagine the headlines, the legal footnotes, the slow attrition that 'flex' can deliver."
    "Your decision compresses like a spring. It will define not only the pilot but the shape of your relationship with Luka Maren and the trust of a town that counts you as its steward."
    "The room holds its breath. The projector's light flickers. Outside, the storm leans in."
    "You stand at the last visible moment before a choice; the tide will move when you do."
    # play music "music_placeholder"  # [Music: Strings swell to a frenzied peak]
    # play sound "sfx_placeholder"  # [Sound: Rain crescendos; a single gull cries, cut clean by the wind]

    menu:
        "Push the leak and public legal pressure to force stronger legal guarantees.":
            jump chapter16
        "Accept a watered pilot with sunset clauses and community oversight promises.":
            jump chapter23
        "Walk away and demand a regulated review process, stalling the pilot.":
            jump chapter32
    return
