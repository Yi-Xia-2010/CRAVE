label chapter8:

    # [Scene: City Hall Outskirts | Late Evening]

    scene bg ch8_6b08b4_1 at full_bg
    # play music "music_placeholder"  # [Music: Staccato, urgent strings; a low synth pulse undercuts the tension]
    # play sound "sfx_placeholder"  # [Sound: Rain on tarpaulins, distant car horns, a precinct siren thinning into the night]
    "You come back out of the throng with hands still buzzing from the feed and the chant. The hearing is scheduled, but the council has folded the night into 'procedural delays' — a polite phrase that"
    "tastes like a stall. People disperse in small knots: some buoyed, some hollowed, everyone waiting for the next shape of the fight."
    "Dr. Noor finds you before you can go back to the Spire. She doesn't close the distance so much as lean into it, voice a low thing against the rain and the city hiss."
    show dr_noor_patel at left:
        zoom 0.7

    dr_noor_patel "Maya. I need you to see something. It's not rumor — it's assessments. Internal. They ran scenarios last spring."
    "You lift your chin against the rain and follow her into the light of a stoop, the smell of seaweed and exhaust curling between your ribs. Her folio is damp at the corners; inside, the pages have the dense, exact smell of someone who keeps arguments in ink."

    dr_noor_patel "They modeled the proposed concrete barrier for three decades. It looks sturdy on paper, but the eco-feedback loops — sediment, estuarine migration, dune loss — they cascade. In the modeled storms, the wall's side-effects amplify erosion elsewhere. It buys time, not stability."
    "Your mouth wants to catalog the technical terms into weaponized sentences for the hearing. Your chest instead catalogs the human equivalents: homes that drifted, gardens that drowned, another map of losses to hand to people who already know how to count grief."
    "Sami appears like a comet — neon lifevest lit by the streetlight — and he's already talking a dozen beats faster than you can think."
    show sami_alvarez at right:
        zoom 0.7

    sami_alvarez "We leak, now. Get those assessments to the press. People will see the numbers and the council will have to answer. It'll ignite the whole city."
    "Dr. Noor's hands close around the folio like a person bracing for a wave."

    dr_noor_patel "If you leak them without legal counsel — without chain-of-custody, without proper attribution — you'll give Luca and his lawyers every reason to sue. They can bury us in civil suits and SLAPPs. The science matters, but so does the process."
    "The words are a cold current under the hot spark of Sami's plan. The crowd outside the hall is still a living map of resolve; inside, settlements are being whispered in corridors."
    hide dr_noor_patel
    hide sami_alvarez

    scene bg ch8_6b08b4_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft clack of someone counting cash in the distance; a muffled offer disguised as civic concern]
    "Luca's people are already shaping the rumor: settlements in exchange for 'community representatives' speaking in favor of Irene Voss's plan. The city smells like an auction and a storm."
    "Your shoulders pitch forward with a fatigue that feels like old tides, the kind that teach you how to carry weight sideways. You remember the bench, the Spire light — the small decision that opened a"
    "door last chapter. This is a bigger threshold: expose wrongdoing and risk ruinous litigation and fractured trust; march methodically through legal channels and hope the council's machinery can be bent; or strike with a public demonstration"
    "of something beautiful and real and living to change hearts."
    "You feel the gravity of all three like three ropes pulling a single mast."

    menu:
        "Ask Sami to slow down — we need cleaner evidence":
            "You touch Sami's sleeve and lower your voice. He exhales, shoulders tight, but nods; the fury in his eyes becomes a focused ember."
        "Tell Sami to prepare the leak — the city deserves to know":
            "Sami's grin is sharp, fevered. He flexes the phone in his hand like a detonator; excitement and fear glitter on his face."

    # --- merge ---
    "The conversation continues."
    "Sami's jaw works. He's already seen the galvanizing power of a headline."
    show sami_alvarez at left:
        zoom 0.7

    sami_alvarez "We can time it with a press drop. If Noor signs off on the data, it's clean enough. The public will not stand for a plan that literally manufactures erosion."
    show dr_noor_patel at right:
        zoom 0.7

    dr_noor_patel "Clean enough is not the same as legally defensible. If they sue for defamation or theft of documents, neighbors could be named. They could be forced into the center of a courtroom instead of the public square."
    "You look up and find Elliot Chen waiting under the soaked awning of a shuttered café. His hair is dark at the edges from rain; he has that too-bright, too-hopeful look he gets when a prototype actually wants to work. He folds open a printout like a small, dangerous flag."
    # [Scene: Puddled Alley | Continuous]
    hide sami_alvarez
    hide dr_noor_patel

    scene bg ch8_6b08b4_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Close drip, the paper whispering as Elliot Chen flips pages]
    # play music "music_placeholder"  # [Music: Rapid percussion; an ascending synth motif pushing urgency]
    show elliot_chen at left:
        zoom 0.7

    elliot_chen "I worked through the night. Hybrid: living seawall anchored with reclaimed pilings, integrated marsh pockets, porous concrete only where structurally necessary. Dr. Noor's numbers fit it. If we present this as an alternative — not a leak, not a smear — we can change the conversation from 'they lied' to 'look, here's a viable plan.'"
    "You take the paper. The design looks like a promise in blueprint form: terraces of salt-tolerant plantings, permeable modules, communal access points. Your thumb leaves a wet smear on the ink."
    show maya_rios at right:
        zoom 0.7

    maya_rios "Will people see it as serious? Or as a stunt?"

    elliot_chen "We'll make it heavy with evidence. We'll build a demo pallet on the boardwalk — small-scale, undeniable. People can wade around it, touch the marsh pocket. You lead the testimony; I'll handle the construction side and community build."
    "There is a tenderness in his plan — not soft, but crafted with scaffolding and bolts. Your chest heats at the implication: trust him enough to let him lead beside you."

    maya_rios "What if the council calls it a stunt and uses that to discredit Dr. Noor's work?"

    elliot_chen "Then we make it impossible to discredit. Data and living proof. A lot of it. Public sympathy follows what they can see and touch."
    "Dr. Noor watches the blueprint, her face unreadable for a beat longer than the rain dictates."
    show dr_noor_patel at center:
        zoom 0.7

    dr_noor_patel "A demo gives the science a body. If we document the demo rigorously, with staggered trials and transparent methodology, it strengthens the testimony. It also gives the community something it can take ownership of. Legally it's safer than an unsourced leak."
    "Sami scoffs, impatient."
    hide elliot_chen
    show sami_alvarez at left:
        zoom 0.7

    sami_alvarez "Safer for who? While you're measuring things, Luca will buy ten voices and make the hearing a show. People are worried now."
    "A neighbor arrives at the alley, boots muddy, a baby asleep against their chest under a plastic poncho. They stop at the edge of the conversation, listening with the careful attention of someone whose life could be lifted or flattened by what happens next."

    "Neighbor" "We need action. Not a lawyer's timeline."
    "You feel that need like a live coil under your ribs: urgency for rescue, for something tangible before another tide comes."

    menu:
        "Ask the neighbor what they need immediately":
            "You crouch, close to the baby and the neighbor's eyes. Their answer is practical and small — better food storage, reinforced thresholds. The list steadies your head with clear tasks."
        "Promise a demo this week and enlist them to help":
            "They blink at your sudden pledge, surprised and wary. Then they nod, volunteering two neighbors and a trailer. Hope moves through them like an electric pulse."

    # --- merge ---
    "The group regroups and plans next steps."
    "Elliot Chen's hand presses against your arm, grounding, warm despite the rain. Around you, Luca's envoy drifts past like a shadow, then halts at the alley mouth."

    "Luca's Envoy" "Ms. Rios, a moment. Luca would be open to community compensation packages, relocation assistance in exchange for support. We can make this painless. Think of the jobs. Think of the long-term security."

    maya_rios "Security that depends on uprooting people is a bad deal. Kids don't learn stability in trailers."

    "Luca's Envoy" "We prefer to think of it as transition, Ms. Rios. The Mayor likes transitions."
    "Dr. Noor's fingers drum the folio, impatient as a metronome."

    dr_noor_patel "There is moral hazard in quick payouts. People accept them because they're immediate. But the model shows that once the sand shifts, that 'transition' will be all the city can offer. It compounds vulnerability."

    sami_alvarez "So we have to force their hand. Exposure forces accountability."
    hide maya_rios
    show elliot_chen at right:
        zoom 0.7

    elliot_chen "But legal ruin can take us out of the fight. If they tie us up, the pilot dies on a desk. The demo can move hearts — and a formal filing can keep us defensible. We can run both angles, but not without a strategy."
    "Your throat tightens. The options spiral faster, like water finding every crack. You imagine headlines; you imagine court dockets; you imagine a small living seawall planted by neighbors in the cold-blue light of dawn, salt sparking on the leaves."
    "Within you, the old habit flares: handle the technical problem alone. It's safer in its own way. The coil of grief in your chest tightens: the memory of a brother who didn't survive because you couldn't"
    "trust others quickly enough. You feel it like a small hot thing pressing against the decision."
    "You also feel something else: the knowledge that resilience is built by hands joined, not clenched. That trust is not an absence of risk but a decision in the face of it."
    "Dr. Noor meets your eyes. There are no easy answers written in her face, only the crisp, scientist's determination to reduce uncertainty."

    dr_noor_patel "If you want to protect people, you have to choose a tactic that cannot be dismissed as spectacle, and you have to preserve the community's legal safety. The demo with rigorous documentation might be the fastest way to sway public opinion while allowing us to build a legal scaffold."
    "Sami pushes back, jaw set."

    sami_alvarez "Or we ignite it and make the city uncomfortable enough that they have to act."
    "Elliot Chen reaches for your hand, a quick, grounding motion. His grip is familiar; it is also an invitation."

    elliot_chen "You don't have to carry every decision on your own. I'm here to do the scaffolding, literal and figurative. But we decide together."
    "Your hazel eyes catch the streetlight, the rain, the smear of ink on Elliot Chen's printout. The neighborhood's faces press in, expectant, fearful, hungry for an answer that will keep roofs and gardens intact."
    "You have three routes laid out like tide marks at different heights: immediate exposure, legal challenge, public demo. Each will alter the map."
    "Your pulse is a drum now — loud, insistent, pushing your thoughts forward, not letting you linger. The city's night seems to hold its breath with you, the rain pausing between drops."
    "You open your mouth to name the next move, to be the leader who decides what kind of fight this will be."
    # play music "music_placeholder"  # [Music: Peak — very high, urgent strings and brass; the tempo quickens to a near-rush]
    hide dr_noor_patel
    hide sami_alvarez
    hide elliot_chen

    scene bg ch8_6b08b4_4 at full_bg

    menu:
        "Leak Dr. Noor’s analysis to the press with Sami.":
            jump chapter9
        "File a formal legal challenge and push hearings through Dr. Noor’s testimony.":
            jump chapter14
        "Stage a dramatic demo of Elliot’s hybrid proposal to win public sympathy.":
            jump chapter9
    return
