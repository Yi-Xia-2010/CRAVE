label chapter15:

    # [Scene: Rooftop Greenhouse | Morning]

    scene bg ch12_f99e88_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm strings, a steady rising motif]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the muffled hum of municipal pumps, voices from the market drifting up]

    "You set the printed covenant on a crate that serves as a makeshift table and let your fingers rest along the margin where your handwriting has crowded the legalese with plain notes" "community veto,' 'open-source telemetry,' 'maintenance cooperative."
    "Teo arrives before the others, toolbox thumping against his hip. He wipes his hands on his bandana, looks at the page, and laughs — not derisive, just the kind of breath that cracks the edge off a long march."
    show mateo_teo_rivera at left:
        zoom 0.7

    mateo_teo_rivera "You wrote my name on the cooperative line, you know that? Guess I'm stuck legally binding myself to be less chaotic."
    show asha_rivera at right:
        zoom 0.7

    asha_rivera "You already are the least chaotic thing here, Teo. We just made it official."
    "He grins, but his eyes track the horizon where Aegis Tower reflects the light like a distant cutlass. The smile is steady: practical, hopeful, the same one he used to patch the community generator last winter."
    "Dr. Jun arrives next, palms dusted with algae samples. He sets his tablet beside the covenant, a constellation of graphs pulsing across the screen."
    show dr_jun_park at center:
        zoom 0.7

    dr_jun_park "The open telemetry feed is ready to go into the escrow. I ran the baseline for the next thirty days — if the pumps drop below threshold, the cooperative triggers a maintenance fund release and public alert. It’s auditable."

    asha_rivera "And the code? Will the community be able to verify it?"

    dr_jun_park "Everything's documented. Open repo, community-run mirror. I'll walk anyone through it who wants to learn. No one has to take my word for the data."
    "You breathe in, tasting soil and the faint metallic tang of the city. There is work behind every assurance: Jun’s evenings in the lab, Teo’s all-night fixing of the old pumps, your own stubborn editing of clause nine until Hana stopped calling it 'impossibly cautious' and started calling it 'necessary.'"
    hide mateo_teo_rivera
    hide asha_rivera
    hide dr_jun_park

    scene bg ch12_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft click of her ring as she sets her pen down]
    # play music "music_placeholder"  # [Music: A soft cello carries the chord into a more intimate register]
    "Hana Kim stands with the composure you remember from your undergraduate lab: precise, contained, all angles in a posture that reads competence. She sets a slim folder on the crate, then looks at you in a"
    "way that holds a thousand unspoken calculations. Her expression is unreadable only if you refuse to read it; otherwise, it's a map of compromise and cost."
    show hana_kim at left:
        zoom 0.7

    hana_kim "I reworked the oversight clause. It's practical and enforceable. We used a two-tiered audit schedule — immediate community audit after each major event, and third-party verification twice a year. The legal language ties escrow releases to those findings."
    show asha_rivera at right:
        zoom 0.7

    asha_rivera "That’s the locking mechanism the mayor wanted."

    hana_kim "And the mayor gets velocity — political momentum — while you retain veto authority over local deployments. It’s not perfect, but it's a hinge."
    "Elias Hart arrives last, voice already warm with the strain and thrill of mobilizing. He moves like someone who has slept on cold roofs and eaten the city for breakfast. He brushes soil from his jacket"
    "and looks at the assembled paper with the same hunger he used to show for murals and petitions."
    show elias_hart at center:
        zoom 0.7

    elias_hart "So we show them the model, not just the promise. We demo the living seawall section, bring the sensors online in public, and make the covenant the headline. Make it impossible to spin away."

    asha_rivera "We make it legal, we make it public, and we teach people to run it."

    elias_hart "We make it ours and theirs at once."
    "There's a quiet there, an undercurrent of everything between the three of you over the last seasons — collaboration, friction, the way you learned each other's temperaments through storms. You let the silence sit: complicated, real, necessary."
    hide hana_kim
    hide asha_rivera
    hide elias_hart

    scene bg ch12_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The scratch of a pen, the soft pop of an adhesive seal]
    "The mayor's office coordinates the press, and by noon the Skyward Market is humming with a purpose that vibrates more tender than any protest roar. Stalls are cleared in a perfect semicircle for the pilot demonstration."
    "Strings of fairy lights twist among the hydroponic racks; steam rises from a kettle at Sofia's stall, carrying the citrus smell that has always marked home."
    # [Scene: Skyward Market | Midday]

    scene bg ch12_f99e88_4 at full_bg
    # play music "music_placeholder"  # [Music: A cheerful uptempo orchestral layer, accordion undertones]
    # play sound "sfx_placeholder"  # [Sound: A soft public-address microphone feedback; murmurs of recognition and relief]
    "Mayor Lila stands at the microphone with the covenant rolled in her hands. Her face is small and composed, the sort of face that has learned how to parcel hope into schedules and votes."
    show mayor_lila_ortega at left:
        zoom 0.7

    mayor_lila_ortega "Today we begin a pilot program that ties community governance to technical capacity. Aegis has agreed to escrow funds that will be released only upon audits we, the community, help administer. The maintenance cooperative is funded, and the sensor code is open for anyone to inspect."
    "A ripple of applause. Sofia wipes her palms on her apron and claps with a kind of fierce gratitude."
    show sofia_navarro at right:
        zoom 0.7

    sofia_navarro "What about the old families on Dock Three? Will they be part of the training?"
    show asha_rivera at center:
        zoom 0.7

    asha_rivera "Yes. Training happens in neighborhoods first. We go where the risk is greatest. Everyone who wants to learn will be taught."
    "There's a chorus of small, specific questions — supply chains, who holds spare parts, what happens in a system failure — and each time you answer with a detail Jun or Teo or Hana has built:"
    "the shared parts locker, the escrow release triggers, the neighborhood audit schedule. The technicalities sound less like jargon when the people who will use them see themselves reflected in the plan."
    "Elias Hart moves through the crowd, handing out laminated flyers with the pilot map and invite times. When he passes you, his fingers brush yours — a brief contact that speaks of a thousand unsaid things."
    "He doesn't meet your eyes with any simple declaration; instead, he folds the flyer with a practiced hand."
    hide mayor_lila_ortega
    show elias_hart at left:
        zoom 0.7

    elias_hart "This is good. People need to see it working. Momentum will do a lot of the rest."

    asha_rivera "We worked for the momentum and for the teeth. We have both."

    menu:
        "Stay and answer people's questions at the market":
            "You plant yourself by Sofia's stall, taking questions from an old fisherman who wants you to explain the sensor readouts again. Each explanation feels like sewing a stitch into the community's confidence."
        "Slip away to check the first sensor readouts with Jun on the roof":
            "You follow Jun up a ladder to the edge of the roof where the first open-source sensor feeds blink alive. The live data scrolls like an honest pulse; it steadies you."

    # --- merge ---
    "'Whichever you choose, you find yourself both in the crowd and at the sensor bank. The market and the lab are braided by the work. Jun's hands find yours when the first public readout comes online; it's less triumph than relief, a small soft exhale shared among conspirators.'"
    hide sofia_navarro
    hide asha_rivera
    hide elias_hart

    scene bg ch12_f99e88_5 at full_bg
    # play music "music_placeholder"  # [Music: Uplifting strings with a hopeful brass undercurrent]
    # play sound "sfx_placeholder"  # [Sound: Laughter, a child's delighted shout as a drip-irrigation system clicks into rhythm]
    "The cooperative's first payroll posts that evening: stipends for neighborhood technicians, funds for spare parts, and a small education grant earmarked for youth apprenticeships in green engineering. You sign away the last administrative form with a"
    "hand that trembles just enough to feel human. The sight of Jun and Teo counting envelopes with the sort of focus usually reserved for lab calibrations makes you grin."
    show dr_jun_park at left:
        zoom 0.7

    dr_jun_park "We deliberately budgeted for community teaching hours. The best insurance is the people who can fix things when they go wrong."
    show asha_rivera at right:
        zoom 0.7

    asha_rivera "And the open repo?"
    show hana_kim at center:
        zoom 0.7

    hana_kim "Public. Mirrored across three community-run servers. We post the audit scripts tonight."
    hide dr_jun_park
    show elias_hart at left:
        zoom 0.7

    elias_hart "This will spread. People will want to copy it. They'll adapt it. Maybe that's the point — to make something that isn't owned, but shared."

    asha_rivera "A blueprint that can't be monopolized."

    elias_hart "Exactly."
    "He says it like a promise. You answer with plans and timetables, because hope needs scaffolding to stand on. But beneath the logistics, there is a warmth that feels like a repaired seam between people who have weathered storms together and walked away with more than they started."
    # [Scene: La Marisma — Dusk]
    hide asha_rivera
    hide hana_kim
    hide elias_hart

    scene bg ch12_f99e88_6 at full_bg
    # play music "music_placeholder"  # [Music: Soft harp and low cello, lingering warmth]
    # play sound "sfx_placeholder"  # [Sound: The distant rush of tide, a chorus of voices from a shared dinner]
    "That night, the neighborhood assembles on the boardwalk for a small ceremony. Someone has strung the sea-glass beads — a long garland representing all the neighborhoods that will host the pilot — from the lamppost to"
    "the communal water pump. Children press their faces to the railing and watch the sea."
    "You stand slightly apart and let the scene collect around you. Your jacket smells of damp earth and solder. Teo bumps your shoulder and passes you a thermos of something sweet and hot."
    show mateo_teo_rivera at left:
        zoom 0.7

    mateo_teo_rivera "You did the thing grown-ups only talk about and made it not just talk."
    show asha_rivera at right:
        zoom 0.7

    asha_rivera "We did it. All of us."
    "Dr. Jun finds you in the dim light and presses a small card into your hand — a schematic with handwritten notes and a tiny star where the first sensor is now physically mounted."
    show dr_jun_park at center:
        zoom 0.7

    dr_jun_park "This star is where we started. Keep it in the book."
    "Hana Kim catches your eye from across the lanterns. She offers a small, genuine smile, the kind that erases a defensive line for a moment and leaves only the person behind it. Elias Hart stands nearby,"
    "watching the water and then turning to look at you as if cataloging what has changed."
    "You let yourself hold the complexity of all that history without needing to define it. Relationships here are not single threads but braided ropes: strong, sometimes frayed, but able to hold weight."

    menu:
        "Walk the boardwalk alone for a while":
            "You step away into the mangrove fringe, fingers trailing along weathered wood. The tide speaks in measured pulses, reminding you that stewardship is long work — not a headline but a lifetime."
        "Join the circle and help pass out the sea‑glass garland":
            "You find a place in the circle and help hand the garland along. Each pair of hands touches the glass, and the chain grows. It feels like making policy with your skin."

    # --- merge ---
    "'You make a small choice. Either way, the result is the same: the garland finds its way back to the boardwalk, and the crowd hums with a contented, hopeful noise.'"
    "Hana Kim sidles up beside you, inconspicuous, her AR monocle dimmed to a soft glow. She nudges the schematic Jun gave you back toward the crowd."
    hide mateo_teo_rivera
    show hana_kim at left:
        zoom 0.7

    hana_kim "We built a thing that can be tested and improved. We gave it legal teeth and community muscle. That balance — it can hold."

    asha_rivera "It should hold, because it's not meant to be fixed for us. It's meant to be taught and remade."
    "Elias Hart joins you, leaning on the railing, the city's last light painting his hair in salt-gold."
    hide asha_rivera
    show elias_hart at right:
        zoom 0.7

    elias_hart "I always thought change would happen with banners and midnight raids on council. This — this is quieter. Maybe quieter things last longer."
    hide dr_jun_park
    show asha_rivera at center:
        zoom 0.7

    asha_rivera "Sometimes banners are for the announcement. The real work is in the maintenance schedule."
    "There is laughter all around — not the brittle sort, but the warm, exhausted kind that follows a long day's labor. You feel it settle in your chest like a gentle tide. Today, something shifted. You"
    "can sense it in the way people talk about training schedules and in the way the market's hum seems steadier."
    hide hana_kim
    hide elias_hart
    hide asha_rivera

    scene bg ch12_f99e88_7 at full_bg
    # play music "music_placeholder"  # [Music: The strings resolve into a gentle major chord]
    # play sound "sfx_placeholder"  # [Sound: Crickets begin; a soft, distant bell marks the hour]

    "Later, you sit with your weathered notebook open on your lap. You write one line across the top of a new page" "Stewardship: shared, auditable, teachable.' You pause, add another: 'Blueprint to share."
    "As the lanterns swing and the sea breathes, you think of the future in a way that is no longer a single horizon but a scattering of lit roofs and trained hands across neighborhoods. The pilot"
    "will not fix everything. It won't stop every storm or erase every loss. But it gives people tools and a means to bind promises with law and knowledge — a mechanism through which hope becomes practice."
    "Dr. Jun comes to stand with you, eyes soft in the lantern glow."
    show dr_jun_park at left:
        zoom 0.7

    dr_jun_park "You know the best part?"
    show asha_rivera at right:
        zoom 0.7

    asha_rivera "Tell me."

    dr_jun_park "We made a template. Other places can use it. They can adopt the cooperative model and the escrow trigger. They won't copy it exactly; they'll make it theirs. That matters."
    "You let that sink in: a blueprint that travels, improvises, and lands where it's needed. The thought is luminous, like the first green of a graft. It is not finality; it is a beginning that has the shape of something that can keep going."
    "Elias Hart squeezes your shoulder, quick and friendly."
    show elias_hart at center:
        zoom 0.7

    elias_hart "You led them into a room where politics meets craft. People can walk out with a shovel and a manual. They'll know what to fix."

    asha_rivera "It will take work, and a lot of stubbornness."

    elias_hart "Good. We have stubbornness."
    "A warm hush falls. The market lamps blink like a constellation lowered between buildings. The city breathes with you in it, and for the first time in seasons the breath feels steady."
    hide dr_jun_park
    hide asha_rivera
    hide elias_hart

    scene bg ch12_f99e88_8 at full_bg
    # play music "music_placeholder"  # [Music: A swelling but gentle finale, hinting at continuity and growth]
    "You tuck the notebook into your sling, feeling the small weight of things that matter: a multi-tool with green tape, a sapling in its cloth sling, a pen with one precious final line of ink. You"
    "stand and look across La Marisma: the pilot hub, the market, the living seawall prototype catching the last light. You imagine Jun's code mirrored on a server in a community hall in another city, imagine a"
    "children’s workshop where a kid learns to solder a sensor board and calls it magic."
    "Your chest warms. You remember why you came back — not for a hero's arc, but for the steady, stubborn work of keeping a place alive. Tonight, the place feels less vulnerable. It feels capable."
    "Elias Hart lowers his voice, close enough that only you can hear."
    show elias_hart at left:
        zoom 0.7

    elias_hart "Whatever happens next, we'll still have this. This is ours."
    "You don't promise anything beyond the moment, but you offer the steadiness of your presence."
    show asha_rivera at right:
        zoom 0.7

    asha_rivera "I'll show up. That's all anyone can really ask."
    "He nods, and in that nod you feel a tether — not a chain, but a shared rope that will hold through storms and repairs, parties and audits."
    hide elias_hart
    hide asha_rivera

    scene bg ch12_f99e88_9 at full_bg
    # play music "music_placeholder"  # [Music: Final uplift, lingering on a hopeful cadence]
    # play sound "sfx_placeholder"  # [Sound: The gentle clap of hands and distant laughter]
    "You breathe in the night: salt, wood smoke, citrus, and the faint electric whirr of pumps that now listen to open code. You let the small, cumulative victories settle into you like comfortable stitches."
    "This is not a cure-all. It is an architecture for care, a system that expects people's hands and votes and stubborn affection for place. In a world that often treated preservation as sentimental and progress as unattainable, you helped build a bridge. And for now, that bridge is lit."
    # [Scene: Rooftop Greenhouse | Night — A brief return]

    scene bg ch12_f99e88_10 at full_bg
    # play music "music_placeholder"  # [Music: Quiet, contented piano]

    "You open the repository feed and read one of the first comments from a coordinator in another district" "We want to adapt this — where do we start?"
    "You stop and look up at the moon over the water. It hangs like a patient witness."
    "You fold your hands in your lap, feeling both the fatigue and the charge of possibility. Somewhere between the tide and the city's glass towers, you've planted a small, durable root."
    # play music "music_placeholder"  # [Music: The strings finish on a warm, sustained chord]

    scene bg ch12_f99e88_11 at full_bg

    scene bg ch12_f99e88_12 at full_bg
    "THE END"
    # [GAME END]
    return
