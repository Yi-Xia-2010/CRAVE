label chapter10:

    # [Scene: City Hall Glass Atrium | Late Afternoon]

    scene bg ch10_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmur of voices, the distant thump of a delivery elevator, the soft clack of heels on concrete]
    # play music "music_placeholder"  # [Music: Low, taut strings — patient, wound-tight]
    "You stand with the microphone still warm under your palm, the metal an indifferent island between your pulse and the room. The hybrid plan is inked across your notes in messy block letters — 'TARGETED BARRIERS"
    "+ CO-MANAGED LIVING BREAKWATERS / 3RD-PARTY AUDITS / COMMUNITY OVERSIGHT' — and the words feel heavier than the paper. You chose this before the room blinked at you; now every face in the atrium refracts the"
    "choice back as expectation, doubt, or calculation."
    "Jun Park watches from his seat like a man whose coat holds counsel. His smile is measured; his gaze is complex, waiting to be read and refusing the favor. Councilwoman Lian Mor has folded her hands"
    "into a ledger shape. Elias stands by the back wall; his sensor wristband pulses a soft, disciplined green. Rosa is at your side, shawl wrapped tight against the conditioned air, and Ivy—small and quick—leans on the"
    "railing, eyes darting like gulls."
    "You clear your throat."
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "The hybrid approach is a recognition of tradeoffs. We cannot wait for a single silver-bullet solution. The city needs targeted, engineered protections in the most vulnerable transport and civic corridors—places that serve everyone—while community-led living breakwaters restore habitat and reduce wave energy at the neighborhood scale. Third-party audits and shared oversight ensure neither side can claim victory by erasing the other. We legislate responsibility, not absolution."
    "Jun Park rises before you finish, palms flat on the table as if to steady an imaginary model."
    show jun_park at right:
        zoom 0.7

    jun_park "Mara, compromise is practical politics. If this is a way to get everyone to the table, I can endorse parts of it. But we need timelines, liabilities, and—importantly—clear command chains in emergencies. We cannot have fractured authority when the sea arrives."

    mara_kestrel "Command chains that don't listen to the people they're meant to protect will fail the first time a derby of storms hits the harbor. If you want compliance in a crisis, you have to build the same trust now that you'll need then."
    "Lian Mor interjects, voice smooth but brittle."
    show councilwoman_lian_mor at center:
        zoom 0.7

    councilwoman_lian_mor "Trust is expensive in votes and money. Where does the capital come from? The barrier contractors want five-year guarantees, and the donors—"
    "Elias Navin cuts in quietly, not to court votes but to calibrate risk."
    hide mara_kestrel
    show elias_navin at left:
        zoom 0.7

    elias_navin "From an ecological perspective, hybrid zones must be iterated in pilots. Living breakwaters need feedstock, timing with spawning cycles—we can't rush the biology without damaging it. Supply chains for engineered modules and biological inoculants are fragile."
    "You notice the way his voice tightens on 'fragile.' There's a calculus behind the words — models and margins — and also a human hush, like someone clutching a ledger that lists lives in decimals."
    "Rosa Alvarez reaches for your hand; her fingers are callused, steady."
    hide jun_park
    show rosa_alvarez at right:
        zoom 0.7

    rosa_alvarez "Make them count us, Mara. Make the audits not just boxes but listening posts. Teach the children to measure the reefs, to tell the stories of what used to be and what can return."
    "Voices ricochet — support, questions, the clack of a tablet. The room splits into committees in miniature. The hope in the hybrid plan flutters, trying to stay aloft against the drafts of budgetary reality and political pressure."
    hide councilwoman_lian_mor
    hide elias_navin
    hide rosa_alvarez

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant announcement — SCHEDULE CHANGE: PUBLIC HEARING RESCHEDULED]
    # play music "music_placeholder"  # [Music: Descends into a low, unresolved chord]

    menu:
        "Push to schedule an immediate public pilot hearing":
            "You stand straighter, the urgency hollowing out the polite cadence from your voice. The clerk notes it, some council members blanch, and Jun's expression tightens like a shutter. Elias gives you a look that says 'careful' and 'thank you' in the same small gesture."
        "Request a closed-session technical review first":
            "You suggest a technical review to refine the pilot parameters. Relief ripples through the engineers; some community members lean back, mouths pinched. Rosa's eyes narrow — she wants the people at the table, not locked out behind jargon."

    # --- merge ---
    "The scene continues as you step out of the atrium into the early evening light."
    # [Scene Transition: You step out of the atrium into the shallow light of early evening. The city's breath is humid; the harbor beyond hums with muffled industry.]
    # [Scene: Salted Rooftop Garden | Early Evening]

    scene bg ch10_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Drip of desalinated water, distant gull calls, soft conversation]
    # play music "music_placeholder"  # [Music: Sparse piano over subtle drone — intimate, melancholy]
    "The garden smells like wet clay and diesel memory—earth reclaimed and water purified. You rub your fingers over a bed of samphire and feel the bristly texture under your nail. Elias moves a tray of newly"
    "cultured shell modules with deliberate care, his hands acting out the spreadsheet in muscle memory."
    show elias_navin at left:
        zoom 0.7

    elias_navin "We can make living breakwaters that work. The reef matrices will attenuate wave energy by, optimally, twenty to thirty percent in protected mouths—we've modeled it. But scaling requires steady inputs: substrate, volunteers, unobstructed deliveries."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "And that steady input is the hinge. If supply lines twist, the biological systems fail before they can become systems."
    "He pauses, then laughs without humor."

    elias_navin "You always put the hinge first. It's part of why you got us the hybrid in the first place."

    mara_kestrel "It's part of why I'm awake at stupid hours wondering which hinge someone's going to remove."
    "Ivy bustles in, cheeks flushed. She carries a coil of hand-painted rope and a bundle of flyers that smell faintly of linseed oil."
    show ivy_kestrel at center:
        zoom 0.7

    ivy_kestrel "We painted more markers for the Basin. Rosa taught the kids a song about the old tides. It's... people are excited. Then there are those who've started whispering about sabotage on the forums."
    hide elias_navin
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "Whispers become reason when someone decides to act. Listen to the land and to the people."
    "Elias Navin watches you both, masking a calculation behind the curve of his mouth."
    hide mara_kestrel
    show elias_navin at right:
        zoom 0.7

    elias_navin "If it's sabotage, it's designed to sow distrust—between community projects and municipal infrastructure. Whoever's behind it knows that the easiest way to kill the hybrid is to make each side suspect the other."
    "You feel the garden's warmth press against the chill that has set in your chest. Hope is a fragile, root-bound thing; tending it requires more than care — it requires protection."

    menu:
        "Share your moth-eaten scarf with Elias to steady him":
            "You drape the scarf over his shoulders. He hesitates, then tucks the wool against his neck. The gesture is small and human; for a heartbeat his guard drops and gratitude flickers in his eyes."
        "Stand apart and make a list of contingency contacts":
            "You step back, pull your journal, and begin to write with quick, honed strokes. Elias reads the list over your shoulder, a wordless acknowledgment of how you think through fear."

    # --- merge ---
    "The lanterns dim and you watch a courier's light blink along the rooftop lane."
    # [Scene Transition: The garden's lanterns dim. Outside, a courier's light blinks along the rooftop lane — a reminder that supply is a thread traveling through the dark.]
    # [Scene: The Basin (Community Floodplain Garden) | Next Morning — After Rain]
    hide ivy_kestrel
    hide rosa_alvarez
    hide elias_navin

    scene bg ch10_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Squelch of boots, muted conversation, the plink of residual rain from leaves]
    # play music "music_placeholder"  # [Music: Low cello with occasional percussive taps — a heartbeat under threat]
    "You come to the Basin with a stomach that thinks in tide charts. The rain has left soft rivers through the soil; someone's footprints mar the path to the nursery beds. A wooden crate—meant for sediment"
    "bags and planting substrate—lies split and empty beside the tool shed. The smell of overturned earth and a faint chemical tang tells you what words will confirm: someone has been here with intent."
    "Ivy crouches at a sapling, fingers damp, eyes round."
    show ivy_kestrel at left:
        zoom 0.7

    ivy_kestrel "They tore open the crate, pulled out the substrate sacks. Some of the starter plugs are gone. Theo said the inoculant would be here last night."
    "Rosa Alvarez stands with her arms folded, not in judgement but as if bracing for a wind."
    show rosa_alvarez at right:
        zoom 0.7

    rosa_alvarez "It's not the first time a delivery was late. But the tearing… that's a message. Whoever did this wanted us to find it and feel small."
    "Neighbors gather in a cautious crescent. An elderly fisherman holds a broken shovel like a bandaged limb. Someone else points to a tire tread that leads toward the back alleys where municipal vehicles park at night."
    show mara_kestrel at center:
        zoom 0.7

    mara_kestrel "We document. We don't make judgements without proof. We photograph everything, collect witness statements. If this is sabotage, it becomes evidence—not rumor."
    "A young volunteer, hands trembling, asks, 'But who would do it? Who profits when we fail?'"
    "You think of the political maps, the budget corridors, the donors with a taste for big, visible infrastructure. You think of any party that benefits from a fractured public. You think, too, of the shadows where people in need can be easily blamed."

    menu:
        "Confront the contractor whose seal is on the delivery manifest":
            "You march to the temporary contractor kiosk with your spine a taut line. The foreman eyes you; there is irritation, then a paper shuffle, and a promise to 'check the manifests' that sounds like a stall."
        "Document the scene thoroughly and send everything to Elias and Theo first":
            "You take photographs, make notes, press a leaf into your journal—then you send the packet to Elias. He replies immediately, 'On my way.' His cadence is calm but urgent, which steadies you."

    # --- merge ---
    "The Basin hums with low anger and fear as you walk back toward the harbor with mud on your boots."
    # [Scene Transition: You walk back toward the harbor with mud on your boots and questions in your throat.]
    # [Scene: Tideworks Lab (Makeshift Field Lab) | Midday]
    hide ivy_kestrel
    hide rosa_alvarez
    hide mara_kestrel

    scene bg ch10_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Blinking monitors, the hiss of a tank filter, distant gulls]
    # play music "music_placeholder"  # [Music: Staccato electronic pulses under a low, underlying bass — tension folded into rhythm]
    "Theo is already there, frowning at a display. He has his solar pack unzipped and a roll of magnetic tags spilled across the table. Elias kneels by a bench where a series of sensor modules lie in a heap—some cracked, others shorted."
    show theo_mendes at left:
        zoom 0.7

    theo_mendes "Someone deliberately cut the main power feed to the receiving bay last night. Cameras rebooted at 02:13—someone's hand moved across the lens right before the feed lost sync. The manifest timestamps show a 'completed' delivery. The physical crates? Not here."
    "Elias Navin taps at a waveform, jaw set."
    show elias_navin at right:
        zoom 0.7

    elias_navin "We have missing inoculant, damaged sensor housings, and at least one reef module crate opened and scattered. Whoever did this knows exactly what to take to cripple the pilot phase."
    show mara_kestrel at center:
        zoom 0.7

    mara_kestrel "Do the camera feeds show faces?"
    "Theo Mendes shakes his head, dismaying multiple things at once."

    theo_mendes "Either faces were obscured, or—' (he pulls up the frame) '—someone used a municipal vehicle to sweep through the service lane. The license plate doesn't match any registry the city's released, but the paint's the same. It could be a stolen vehicle staged to look municipal."
    "Your throat tightens. The logic of sabotage is surgical. It aims not only to remove materials but to plant suspicions."
    "Elias Navin stares at the manifest, then at the city's online public scheduler."

    elias_navin "If the manifest shows municipal routing, some will say the city is sabotaging the community. If the manifest is forged, it points to a private actor trying to provoke that exact response."
    "You think of Jun Park and his polished coat. You think of Councilwoman Lian and the pressure that eats at her like rust. You cannot know intention from motive; the evidence is a smear when the muscles that hold it taut are political."
    hide theo_mendes
    hide elias_navin
    hide mara_kestrel

    scene bg ch10_453e40_6 at full_bg
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "We take a breath. We secure the lab. We call the community meeting. We do not float accusations in public without corroboration. If this is a graft-and-grudge operation, speaking too soon hands them the leverage they want."
    show elias_navin at right:
        zoom 0.7

    elias_navin "But silence can cost lives if it lets them get a step ahead."
    show theo_mendes at center:
        zoom 0.7

    theo_mendes "The logistics companies report 'route irregularities' citywide. We can't tell yet if it's coordinated. But coordination would explain the timing."
    "Your hands go to your journal. Your compass pendant feels hot against your sternum, as if reminding you which way to steady. Trust is the currency here, and someone is attempting to bankrupt the town in petty thefts and staged proofs."

    "Jun Park's office issues a press brief within the hour" "Investigations ongoing; no evidence yet of deliberate sabotage."
    "You call Elias, then Jun, then Councilwoman Lian. Each call is a circle of cautious words and layered meanings. Jun's voice on the line is calm; the warmth in it is complex and difficult to parse."
    hide mara_kestrel
    show jun_park at left:
        zoom 0.7

    jun_park "We will provide increased security for municipal shipments and an independent oversight investigator—if you want it. We need to avoid panic."
    hide elias_navin
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "We need transparency, Jun. We need chain-of-custody for manifests. And we need protection for the Basin volunteers."
    "Jun Park: (after a pause) 'You'll have it. We'll open the audit schedule. For now—'"
    "He stops himself like someone cutting a rope when it begins to fray. There is something unreadable in the silence that follows—neither denial nor admission, only the shape of a man carrying decisions he must justify later."
    hide theo_mendes
    hide jun_park
    hide mara_kestrel

    scene bg ch10_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Low single note held; strings tremble]
    "You stand at the prow of the plan you helped forge. The hybrid, once a living promise of compromise, is already taloned by small, targeted violence. Supplies diverted. Sensors smashed. Manifests altered. Trust unwinds in human hands."
    "Someone wants this to fail."
    "The room narrows to the lab's fluorescents and the soft green pulse of Elias's sensor band. You look at the footage again, the gloved hand, the dash of indigo that could be any uniform, and you feel the tilt of the next decision heavy and inevitable."
    "Page-Turn moment: Your phone buzzes. A secure message pops up from an unknown municipal account: a short, clipped sentence and an image of a crate—opened, its contents strewn on a dock. The signature is a code you don't recognize. The implication is direct and waiting."
    "You close your journal, fingers damp. The hybrid plan needs guardianship and answers. Tonight, the city tastes of salt and something sharper — betrayal."

    scene bg ch10_453e40_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant siren, then silence]
    # play music "music_placeholder"  # [Music: Builds into an unresolved, descending cluster]

    scene bg ch10_453e40_9 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter11
    return
