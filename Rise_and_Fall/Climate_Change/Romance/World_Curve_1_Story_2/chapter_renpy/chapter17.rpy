label chapter17:

    # [Scene: Green Roofs | Morning]

    scene bg ch15_3be532_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm, steady strings; a single cello line underlines walking footsteps]
    # play sound "sfx_placeholder"  # [Sound: Bees, distant gulls, the soft hum of pumps and footfall on wood decking]
    "You stand with your palms on the rim of a reclaimed planter, soil on your fingertips, and the city unfurls in stepped terraces beneath you: green roofs like islands, the harbor a low seam of slate"
    "beyond them. The morning smells of wet compost and salty air, and it feels, suddenly and plainly, like the kind of day that makes policy feel close enough to touch."
    "You remember what brought you here — the long nights of leafleting, the march along the causeway, the public meetings where voices rose and were heard. The campaign you helped seed has threaded itself into municipal"
    "machinery. Today is the public launch of the citywide retrofit program you helped shape: funds, trained crews, enforceable oversight, and community co-management written into the clauses Samir insisted on. It is impossibly practical and impossibly hopeful"
    "at once."

    scene bg ch15_3be532_2 at full_bg
    # play music "music_placeholder"  # [Music: Swell of piano; a breath of higher strings]
    "Arin Voss walks up the stepped path, camera slung over his shoulder, boots scuffed with rooftop mud. He pauses when he reaches you and gives a look that is hard to read — relief braided with"
    "something softer. The wind plays at a curl of his hair; his jacket smells faintly of tar and tea."
    show arin_voss at left:
        zoom 0.7

    arin_voss "You look like you're about to steady the whole harbor with your hands."
    show mira_solace at right:
        zoom 0.7

    mira_solace "Only the rooftops I can reach. You brought the camera?"

    arin_voss "Always. Someone's got to embarrass-someone with archival footage when the city's historians ask for proof we were here."
    "He smiles, then grows more earnest. He gestures to volunteers calibrating humidity sensors and to a team affixing lightweight flood-foils to parapets."

    arin_voss "They read the manifesto, Mira. People showed up. Old timers patched in and kids ran soil tests. Etta's voice carried like it always does. It mattered."

    mira_solace "It mattered because you didn't let it be just noise on a march. You turned the momentum into schedules and crews."

    arin_voss "We made a spreadsheet at midnight and then argued about coffee ratios until dawn. That's our romance: caffeine and municipal logistics."
    "A shadow crosses your face — the inevitable friction of process you'd negotiated: who holds oversight, how funds disburse, what counts as 'essential business' for retrofit priority. Samir appears on the next terrace, tablet in hand,"
    "glasses fogged slightly from the humidity. He reads the data feed with a careful cadence that makes numbers feel like promises."
    show samir_hale at center:
        zoom 0.7

    samir_hale "Funding release confirmed. The pilot teams are greenlit for the first tranche. Noah's shop is in the initial cohort; the retrofit timeline aligns with the permit waivers we negotiated. Etta's community seats cleared the vetting. It's—"

    mira_solace "—not perfect, but it is enforceable."

    samir_hale "Exactly. It's structure with teeth."
    "The word makes something knot then relax in your chest. Enforceable. Not just words on a ceremonial plaque. You think of your childhood on the docks — the tide coming for a house that had nowhere to go — and taste a small, private victory."

    menu:
        "Hand Arin Voss the soil-dusted badge of the program":
            "You hold out a laminated badge — it feels ordinary and ceremonial. Arin Voss accepts it with a small, genuine grin, the camera forgotten for a beat. The gesture is wordless and steady."
        "Slip your notebook into your jacket and listen to Samir's briefing":
            "You tuck the notebook away and let Samir speak. Your attention narrows to timelines and redlines; the practical things that turn slogans into service. Samir's assurance settles like cement under your feet."

    # --- merge ---
    "Both outcomes converge as the scene continues with the following visual and music cues."
    hide arin_voss
    hide mira_solace
    hide samir_hale

    scene bg ch15_3be532_3 at full_bg
    # play music "music_placeholder"  # [Music: Quiet, hopeful chord progression]
    "Noah arrives beaming, his forearms still carrying the grease and salt of his shop. He hasn't stopped working for the last few weeks, but his face is softer — tired, but not the worn resignation you'd seen before."
    show noah_solace at left:
        zoom 0.7

    noah_solace "So my skip-buckets make the list? Finally? I kept saying, 'Mira, a good bilge and a properly mounted pump saves more than a million words at City Hall.'"
    show mira_solace at right:
        zoom 0.7

    mira_solace "You were right. The retrofit budget includes small businesses and shop-level pumps. Your hand-built units will be certified to city standards. You won't have to move unless you choose it, and you'll have the funds to make the shop safer."

    noah_solace "That's the thing I didn't want to hear at first — 'won't have to move unless' — but still. It's better than the nothing they offered before."
    "Etta's voice carries from the causeway — she has come up by the courtyard stairs, her presence immediate as weather."
    show etta_maren at center:
        zoom 0.7

    etta_maren "We hold them to it, Mira. You put community seats into the law. That keeps the hands there."

    mira_solace "You keep them honest, Etta. We'll make sure the oversight board includes people who actually live where this matters."
    "Etta's laugh folds into the air, dry and pleased."

    etta_maren "Good. Otherwise we wind up with walls and no people left to remember why the walls were needed."

    mira_solace "We remembered."
    # [Scene Transition: The group walks down a planted ramp into the Municipal Offices]
    hide noah_solace
    hide mira_solace
    hide etta_maren

    scene bg ch15_3be532_4 at full_bg
    # play music "music_placeholder"  # [Music: Piano and light percussion; forward-moving, measured]
    # [Scene: Municipal Offices | Afternoon]

    scene bg ch15_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmured conversation, the stamping of an official seal on paper, a faint trickle from a plant distant in the atrium]
    # play music "music_placeholder"  # [Music: Low brass and strings build into a supportive swell]
    "You sit at the head of the table. The retrofit ordinance is projected on the wall like a field map — clauses and checkboxes you helped draft. Samir stands beside you, pointer in hand, walking through"
    "the enforcement mechanism: audits, community review panels, escrowed funds released in tranches, and penalties for contractors who sidestep inclusion clauses."
    show samir_hale at left:
        zoom 0.7

    samir_hale "We can't prevent every bad actor, but with transparent procurement, community overseers, and an independent auditor, we make it expensive to cut corners."
    show mira_solace at right:
        zoom 0.7

    mira_solace "Expensive and visible. If it's visible, people will fight to keep it honest."

    samir_hale "Exactly. Visibility is deterrence."
    "There is a moment of push and pull as the legal language flattens tensions into practical terms. You feel tired — the long arc of negotiation — but the tiredness is the right kind: earned and"
    "forward-leaning. You imagine Noah's shop retrofitted, a little parapet and pump in place, Etta chairing the community review panel with that quiet, unsparing lens."
    "Someone from the finance office raises a procedural concern about timelines, about the velocity of disbursement versus oversight. You answer in plain, patient sentences. You don't romanticize the bureaucratic grind; you make it human."

    mira_solace "If we frontload training and certify neighborhood crews, we reduce the risk in the first tranche. That way the communities can do the retrofits, and payments go to them and local suppliers. That keeps money in the neighborhoods."

    "Finance Representative" "Community crews need to be trained quickly. We need measurable benchmarks."

    mira_solace "Then let's make the benchmarks teachable and reachable. We'll set up mobile labs from the Tidehouse to run certification clinics."
    "The room nods, a collective, pragmatic breath. It is, in a way, an act of translation — turning the movement's urgency into scheduled, teachable steps that won't vanish with a change of administration."
    hide samir_hale
    hide mira_solace

    scene bg ch15_3be532_6 at full_bg
    # play music "music_placeholder"  # [Music: Warm harp arpeggio; soft chorus hum]
    "Later, there is a signing. The press is small and gentle — community journalists, a few local networks, and the crowd of neighbors who have followed the campaign. Noah videotapes the moment with a shaky phone,"
    "laughing; Arin Voss's camera captures closeups of Etta's hands and the ceremonial seal. You place your pen on the line, and the ordinance becomes a physical thing among other physical things — stamped paper, photos, a"
    "posted schedule."
    show etta_maren at left:
        zoom 0.7

    etta_maren "They'll know we were there. They'll remember how we insisted on seats and saltwater training."
    show mira_solace at right:
        zoom 0.7

    mira_solace "And they'll know that moving wasn't the only option — retrofitting, adapting, staying with dignity."

    etta_maren "Good. Keep your faith, Mira. Keep your hands doing what your head has decided."

    menu:
        "Shake Samir's hand publicly before the cameras":
            "You reach for Samir's hand. The shake is firm; his relief is obvious. Cameras click. It's a small diplomatic gesture that binds policy and people."
        "Step aside and let Noah film Etta's reaction":
            "You step back. Noah frames Etta's face, her stern smile softened for the cameras. Letting a neighbor have the spotlight feels like a small choosing in itself."

    # --- merge ---
    "Both outcomes converge as the scene continues with the following music and atmosphere."
    # play music "music_placeholder"  # [Music: Soft exhalation of strings; the atmosphere is brightening as day leans to late afternoon]
    # [Scene Transition: Evening — Rooftop Garden | Dusk]
    hide etta_maren
    hide mira_solace

    scene bg ch15_3be532_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Laughter, low conversation, the crisp pop of a thermos being uncapped]
    # play music "music_placeholder"  # [Music: Gentle acoustic guitars and a rounded string motif]

    "The rooftop garden holds its breath against the incoming night. You stand with Arin Voss, Noah, Etta, Samir, and a scatter of neighbors. There are small plates of warm food, a circle of chairs, and a wooden plaque that will be mounted at the Tidehouse" "For resilience, with community."
    show mira_solace at left:
        zoom 0.7

    mira_solace "We started this with nails and sympathy. Today is the part where nails meet budgets and people keep the work honest."
    show arin_voss at right:
        zoom 0.7

    arin_voss "You did the hard, dull work nobody's songs are about. You made the thing they can point to and say, 'We built this together.'"

    mira_solace "We built it together."
    show noah_solace at center:
        zoom 0.7

    noah_solace "My crew's been trained. My apprentice can weld that pump into place. We won't be at the mercy of distant contracts anymore."
    hide mira_solace
    show etta_maren at left:
        zoom 0.7

    etta_maren "And we will watch. We will sing and watch. Old ways of organizing survive in new skin."
    "Conversation bends into stories — small, human, true. A neighbor thanks you for staying through the storms. A volunteer with paint on his knuckles swells with pride over a rooftop planter that now catches overflow instead of flooding a stairwell. Each anecdote is a stitch."
    "Arin Voss angles his camera toward you and fumbles for a sound bite as if he can't help himself."

    arin_voss "Say something for posterity. Or for the historians. Or for me."
    hide arin_voss
    show mira_solace at right:
        zoom 0.7

    mira_solace "For the harbor: stay. For the people: we will protect the right to stay with dignity. That's why we made law. That's why we hold them to it."
    "He grins, and for a moment his relief is plain and uncomplicated. He takes a photo that feels like a covenant."

    etta_maren "You take a leadership role now, Mira. They will look to you. Are you ready?"
    "You feel the weight of that question settle over you. Ready is not a single state — it's a chain of small yeses. You think of drafting sessions in the municipal office, of Etta's steady hands,"
    "of Noah's shop, of Samir's lists. You realize you have been saying yes without naming it."

    mira_solace "I am. We are. This job will be days of small, exact work. I will keep the community at the center. I won't hoard the pen."
    hide noah_solace
    show samir_hale at center:
        zoom 0.7

    samir_hale "We'll stand with you in the technical bits. You bring the people; we'll bring the process."
    hide etta_maren
    show noah_solace at left:
        zoom 0.7

    noah_solace "And we'll bring the boats if necessary."
    "Laughter. The rooftop lights bloom like a small galaxy. The city beyond is a horizon of anchored promises — live reedbeds down on the waterfront, newly raised thresholds at neighborhood storefronts, pump housings fitted like small, honest crowns."
    "You breathe in the night air, heavy with seaweed and the faint scent of someone frying onions below. In your chest, something rises — not triumph, not naive, but a clear, widening hope: policy that can"
    "be enforced, communities with the capacity to act, cultural memory that won't be paved away."
    "Arin Voss steps closer, and for a brief instant your shoulders touch. The contact is an understanding rather than a declaration."
    hide mira_solace
    show arin_voss at right:
        zoom 0.7

    arin_voss "Whatever comes next, we'll have this to look at. People will know what's possible."
    hide samir_hale
    show mira_solace at center:
        zoom 0.7

    mira_solace "They'll know we chose people."
    hide noah_solace
    hide arin_voss
    hide mira_solace

    scene bg ch15_3be532_8 at full_bg
    # play music "music_placeholder"  # [Music: A final upward swell of strings and piano]
    "You take one last look at the rooftops, at the harbor's low, patient line, and let the image hold: reedbeds that shift with the tide, shopfronts that open in morning with reinforced sills, children crossing new"
    "boardwalks. This is not the halting end of a problem, but a living beginning: a system that can be iterated upon, a program with teeth and heart."
    "You stand, a new role forming around you like a garment that will need tailoring, and you feel, genuinely and simply, ready to keep sewing."

    scene bg ch15_3be532_9 at full_bg
    # play music "music_placeholder"  # [Music: Gentle, resolving chord; lingering warmth]

    scene bg ch15_3be532_10 at full_bg
    "THE END"
    # [GAME END]
    return
