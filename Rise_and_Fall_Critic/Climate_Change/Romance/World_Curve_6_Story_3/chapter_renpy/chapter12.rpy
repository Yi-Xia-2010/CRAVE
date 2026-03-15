label chapter12:

    # [Scene: Trial Platform Behind Guarded Buoys | Morning]

    scene bg ch12_fa9d90_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The creak of rope, the soft thud of sensor housings pinging into place, an outboard motor idling in the distance]
    # play music "music_placeholder"  # [Music: Low, restrained synth underscoring a steady heartbeat rhythm]
    "You stand with the salt in your hair and the taste of metal on your tongue, watching the trial run like a surgeon watching a pulse. The platform rocks underfoot; your boots slap wet wood. Priya"
    "kneels by a compact console, thumbs moving in practiced, impatient choreography. Noah Ríos is beside you, sleeves rolled, smartglasses dimmed—he is all quiet competence until the moment someone needs a grin. Today he is a little"
    "too sharp around the edges."
    show priya_anand at left:
        zoom 0.7

    priya_anand "Telemetry's clean. Power draw is within predicted variance. The attenuation curve matches the model to within—"
    show noah_ros at right:
        zoom 0.7

    noah_ros "—two percent. Which is, frankly, not bad for a first day under real conditions."
    "You breathe the machines' breath: the hum of pumps, the small chirp of the modular sensors. The private partner's field techs—neat jackets, branded caps—hover like a polite tide. They ask procedural questions with neutral smiles. Arman"
    "Kade's media caravan is a distant, curated rumor on the shore: cameras on tripods, a spokesperson clearing their throat. You remind yourself why this choice was made: speed, proof, leverage."
    "You watch the live feed: a wave hits the barrier, the forces attenuate along the predicted curve. Numbers bloom on the tablet in front of you like cold flowers—clean, sharp lines that say this system works"
    "under the conditions you could replicate today. Priya taps a few notes, then crosses her arms and allows herself a short, rare smile."

    priya_anand "That's good. Solid. This is the kind of data Cass asked for."
    show mara_evans at center:
        zoom 0.7

    mara_evans "It looks good on paper. It looks good in the water. But how does it look to people on the promenade?"

    noah_ros "It looks like a reason to fund it at scale. It looks like lives saved when the next storm comes."
    "You think of Elena's bakery awning, of Tomas's callused hands, of the kelp lines tied along the pier. In this moment the math is bright and hopeful—an answer in the language of engineers. But the shore's memory is in mouths and storefronts, not charts."

    menu:
        "Answer the field tech's camera question honestly: 'Yes, we partnered with a private firm'":
            "You nod, voice steady but softer than you feel. The camera records the admission; you watch the private partner's rep give the brief, apologetic smile you practiced. Noah Ríos watches you register it and his jaw tightens. Priya's fingers hover over the console, ready to mute or explain."
        "Deflect: 'This is a collaborative pilot with many contributors'":
            "You deflect with a practiced phrase—collaboration, many contributors. The footage still runs; the phrasing will be picked over later. Noah Ríos exhales, a sound like someone trying to bargain time out of consequence. Priya closes her jaw; she knows the wording will be parsed."

    # --- merge ---
    "Scene continues."
    "The trial finishes cleanly. On the water, the barrier flexes and rebounds; the sensors sing the expected song. Your chest swells; the relief is immediate and bitter-sweet. Noah Ríos claps you on the shoulder with impatient affection."

    noah_ros "You did it. We did it."

    mara_evans "We got numbers. We didn't get a promise."

    noah_ros "Promises are political things. Numbers are weight—hard to ignore. We need weight right now."
    "Conversation spirals—Priya nudges you toward preparing the press packet, the partner insists on a controlled release schedule, and Noah Ríos presses for immediate publication to capitalize on momentum. You feel the tug between doing right by the community and doing the necessary thing to make the system scale."

    priya_anand "We can control the dataset. We can annotate who had access. We can push open-source APIs later—"

    "Partner Rep" "We think a rapid, controlled release will maximize adoption and save lives. That's our priority."

    mara_evans "Priority for whom?"
    hide priya_anand
    hide noah_ros
    hide mara_evans

    scene bg ch12_fa9d90_2 at full_bg
    # play music "music_placeholder"  # [Music: A single sustained cello note drops into the mix, uncomfortably resonant]
    "You let them have the numbers. You let the private partner seal a press release with the kind of carefully optimistic ledes that will make headlines. The platform rocks underfoot; you feel a small, almost physical lurch inside your chest that will not settle."
    # [Scene: Promenade | Afternoon — Release and Reaction]

    scene bg ch12_fa9d90_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rattle of a vendor's cart, murmurs morphing into louder conversation, a distant sharp tape recorder]
    # play music "music_placeholder"  # [Music: Minor-key strings, slow and insistent]

    "The story lands on the promenade like a sleet of press clippings. "Pilot Validates Tech," one headline says. Another reads" "Private Partner Backs Modular Barriers—Fast Solution?"
    "Elena finds you before you find her. She moves with the intensity of someone who has to hold a business open and a life together at once—face flushed from hurried work, hands smelling of flour."
    show elena_torres at left:
        zoom 0.7

    elena_torres "You told me you were doing what you had to. Did you ever mean—' (her voice breaks) '—did you ever mean you'd keep us in mind?"
    show mara_evans at right:
        zoom 0.7

    mara_evans "Always. I—"

    elena_torres "Will my customers still be here after this proves the shore can be monetized?"
    "Her words unload all at once: fear, accusation, and the raw edge of betrayal. This is not about algorithms; it's about whether the town you love is now a product. You wish for a clean technical fix you could hand her; instead you have a dataset and a signature."
    "Noah Ríos arrives, breathless from a meeting, and the three of you stand in a triangle of weather and consequence. He approaches with hands slightly raised, trying to be conciliatory in a language that sometimes sounds like the language of investors."
    show noah_ros at center:
        zoom 0.7

    noah_ros "El, we didn't hand your neighborhood over. We needed a partner who could field this at scale."

    elena_torres "A partner who can 'field' this also fields the contracts, Noah Ríos. 'Scale' is a word that eats people who can't defend themselves."

    mara_evans "We wanted speed so people wouldn't drown waiting for the bureaucracy to—"

    elena_torres "Drown? Or be priced out before the water even gets to the door?"
    "The exchange goes on, the words like low surf—understated but powerful, pulling at hidden roots. Noah Ríos's defenses rise and crumble in alternating breaths."

    noah_ros "If we don't show this works on the water, Cass will pick Arman Kade because he can promise instant installation. The numbers give us leverage—"

    mara_evans "Leverage how? To negotiate fair terms or to prove the shore is a safe place to invest in exclusion?"

    noah_ros "You think I want to watch what happened to your family happen to other people? I thought— I thought scaling fast would protect them."
    "There is a beat of silence. Around you, the promenade hums with people who have begun to read and talk and decide. The press has already started to frame the story as 'tech versus tradition.' Arman"
    "Kade's spokespeople are everywhere: op-eds, a polished interview claiming the city's need for 'decisive, centralized defenses.' He is not required to be dishonest; he simply repackages speed as benevolence."

    menu:
        "Tell Elena you will insist on community oversight clauses in any contract":
            "You promise, voice rough with fatigue. Elena's mouth tightens—she registers the words but sees the partner's logo on the press release. Your assurance is a bandage, but it is something; she nods, guarded."
        "Appease the crowd: 'Trust me — this will scale and we'll fight for everyone later'":
            "You choose the softer lie: future fights, future protections. Noah Ríos exhales in relief; Elena looks away, not yet convinced. Priya gives you a look that asks whether 'later' is a luxury you can actually buy."

    # --- merge ---
    "Conversation continues."
    "Cass's office fills with angry council emails by late afternoon. A clip of Arman Kade—sardonic, controlled—plays on a loop: He describes the private partner as a 'model for rapid citywide defense.' Cass's public statements are careful;"
    "her private messages unreadable. You have seen her at difficult crossroads before. Now the crossroads are a political ambush."
    hide elena_torres
    show priya_anand at left:
        zoom 0.7

    priya_anand "They're using our data, but not our interpretation. They're plugging our graph into their narrative."

    mara_evans "Can we issue a clarification? Release the raw data and the modeling notes?"

    priya_anand "Yes. But the press cycle moves faster than we do. People have already chosen sides."
    "The neighborhoods split along a ragged seam: some welcome the 'proof' as salvation; some lock their doors tighter, sure that the market will follow the science with a bulldozer. Tomas tells anyone who will listen that walls are not the same as belonging."
    hide mara_evans
    show tomas_belmar at right:
        zoom 0.7

    tomas_belmar "You can put a fence where a garden was, but the sea remembers who you were. It remembers names."
    "You try to answer each challenge—technical briefings, community sessions, op-eds. Each time you speak, the same two things happen: the data convinces some people, and Arman Kade's narrative convinces others that privatized management is the faster,"
    "safer path. The pilot's clean lines do not translate to unanimous trust. The intimacy of your work—late nights at the Lab, the careful placement of sensors, the jokes half-whispered with Noah Ríos—becomes footnote in someone else's"
    "press kit."
    # [Scene: Promenade | Night — Council Vote Coverage]
    hide noah_ros
    hide priya_anand
    hide tomas_belmar

    scene bg ch12_fa9d90_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The announcer's voice crackling, a distant gull, the friction of a folding chair being dragged]
    # play music "music_placeholder"  # [Music: Sparse piano, descending phrases that feel like shutters closing]
    "You watch the council feed with your hands clenched around the pendant at your throat. Cass is on camera, measured, the city seal behind her. Her face is composed—politics has taught her to temper expression—but when someone you love is on the line, composure is a thin skin."
    "On the screen, Arman Kade speaks with that cool confidence you've seen before. He frames the private management clauses as 'necessary guarantees'—operational oversight to ensure maintenance, to keep insurance rates reasonable. His language is full of the protective metaphors that sound like safety and often end in fences."
    show arman_kade at left:
        zoom 0.7

    arman_kade "We cannot ask investors to put capital at risk without clear stewardship. Private management ensures reliability and speed."
    show mara_evans at right:
        zoom 0.7

    mara_evans "Stewardship for whom?"
    "The vote reads out. The dais murmurs. When the tally is final, the result is a knife-quiet in your stomach: the council passes a version of Arman Kade's installation that includes private management clauses—enough oversight language"
    "to appease standards, enough latitude to hand operational control to profit-driven entities. Cass votes with procedural qualifiers; her eyes flick briefly toward the camera, unreadable."

    "A hundred small things happen at once. Phone notifications bloom with messages—some supportive, many accusatory. A neighbor you recognize from childhood posts a photo of the trial footage with the caption" "Sold."
    "Noah Ríos stands beside you, face hollowed with exhausted determination. He reaches for your hand and finds instead the space between you: the recent years of shared work that now resemble a ledger of compromises."
    show noah_ros at center:
        zoom 0.7

    noah_ros "We proved the tech works. We saved a lot of uncertainty for people who would otherwise just be used as examples."

    mara_evans "We saved the numbers. We lost the trust."

    noah_ros "Is that how you measure it? By headlines and votes? By what the mayor can stomach?"

    mara_evans "Noah—"
    "Priya turns a tablet toward you, showing the raw curves again—beautiful, unambiguous, tragic in their clarity. The data is pure. The consequences are not."
    hide arman_kade
    show priya_anand at left:
        zoom 0.7

    priya_anand "This is not over technically. We can keep working. We can make it open-source; we can push for clauses—"

    mara_evans "Open-source won't stop a bulldozer if no one is left to argue when it comes."
    "As the night pulls itself together in sleet and neon, people disperse. The promenade continues—vendors fold up, a child tugs at her mother's sleeve, Tomas mutters about tides. The city is a tapestry of small, mundane continuations stitched over a freshly cut seam."
    "You walk alone for a moment, the pendant heavy in your fingers, and let the sound of the bay take you. It answers with a slow, patient wash—indifferent to politics, but relentless in its effect. The"
    "technical victory you hold is a strange, acidic comfort. Numbers do not warm ovens, they do not keep a storefront from being priced out next fiscal quarter. They do, however, show that the living systems and"
    "Noah Ríos's sensors could, with the right conditions, work."
    "But the conditions are not only scientific—they are political and moral and messy with people. The pilot's success has been reframed as validation for centralized, privatized control that will likely restrict access and exact rents where"
    "there were once open thresholds. The intimacy of your collaboration—long shared evenings soldering circuits, the tactile comfort of Priya's elbow bumping yours as she rejoices at a model converging—now feels like it has been used as"
    "a tool in someone else's hand."
    "You feel the truth press against your ribs in a slow, backlit way: technical validation without public faith can become a weapon. You thought the numbers would be a shield; instead they're a scalpel that others can wield to rewrite who gets to stay and who must go."
    hide mara_evans
    hide noah_ros
    hide priya_anand

    scene bg ch12_fa9d90_5 at full_bg
    # play music "music_placeholder"  # [Music: Long, mournful violin phrase; then a delicate, single piano chord hanging in the air]
    "You have proof, and you have loss. The city has moved in a direction that will protect infrastructure but also privatize the lifelines of people who cannot afford new fences. Your role—your promise to your neighborhood—feels both kept in method and broken in spirit."
    "You stand there and listen to the bay. The sound is the same as ever, and not the same at all. The water keeps its rhythms; the city keeps its decisions. You fold the pendant under your palm, feeling its familiar coolness like a small, private ritual."
    "You think of what comes next in the way someone thinks of a scar: as something permanent that will change how you move. You do not know how to fix everything. You know how to keep"
    "working on the parts you can touch: the sensors, the open data, the community legal clinics that might contest clauses, the late-night calls with people who still believe you can save their little stretches of the"
    "shore. You know that some of those efforts will be small and stubborn and not newsworthy. You know they will not be enough to stop the first wave of privatized installations."
    "You do not close your notebook with triumphant certainty. You close it with a slow, steadying motion that is more like setting a bone than celebrating a victory. Hope has not vanished; it is smaller and more careful now—an ember that must be sheltered from wind."

    scene bg ch12_fa9d90_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    scene bg ch12_fa9d90_7 at full_bg
    "THE END"
    # [GAME END]
    return
