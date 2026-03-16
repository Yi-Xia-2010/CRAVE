label chapter10:

    # [Scene: Rooftop Community Garden & Storm Shelter | Late Afternoon]

    scene bg ch10_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, insistent percussion—a heartbeat under the wind]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the creak of a windbreak, murmured voices below]
    "You stand with your notebook pressed to your ribs, the paper damp where your thumb has worried at the corner. The vote is stalled—your voice carried a formal phrase into the meeting minutes: independent audit requested."
    "It is a precise thing, a hinge you set between two futures. Saying it felt like setting a buoy into churning water."
    "Jun Park finds you first. He moves like a man who has practiced being relieved—light in the shoulders, eager to offer the small comforts of corporate diplomacy."
    show jun_park at left:
        zoom 0.7

    jun_park "They—uh—yeah. People will breathe easier hearing 'audit.' It buys time.' (He smiles too quickly.) 'TideLine offered to suggest a third-party. Polite, practical. They're trying to stay procedural."
    show marin_sol at right:
        zoom 0.7

    marin_sol "An audit from a name Aria proposes would be theatre. We need someone independent—someone the town trusts."

    jun_park "Right. Right, of course—independent.' (He hesitates, glancing at the pier beyond the rooftop.) 'I—I'm glad you pushed for it. I know it slows things. But—' He exhales, voice down. 'It also keeps legal exposure lower for everyone."
    "You watch him say 'everyone' and see how it hangs—an attempt to include the town and the investors in a single circle. The attempt feels false, and the rain-roughened boards of memory in your mind groan under that stretch."

    menu:
        "Offer Jun reassurances about fairness":
            "You tell him, quietly, that fairness is the point—even if it takes longer. Jun nods, relief softening his features for a beat."
        "Ask Jun if TideLine is influencing the 'independent' options":
            "You press him on who suggested which names. He looks away, fiddling with his comm. 'They floated a couple—names that sound independent on paper,' he admits, and the admission makes both of you smaller."

    # --- merge ---
    "The conversation continues."
    "Jun's gasp of relief is brief; below the rooftop, voices split like surf. You can feel the town dividing—people who want action now and others who want money now; immediacy in two different currencies."
    # [Scene: Boardwalk Floodplain | Early Evening]
    hide jun_park
    hide marin_sol

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Metallic squeal of measuring rigs, sensors pinging, a steady wind against your jacket]
    # play music "music_placeholder"  # [Music: Tension-building strings—long notes that fray at the edges]
    "You and Dr. Lian crouch beside the latest sensor array. The modules blink teal: depth, flow, substrate erosion. Her hands move quick and exact; she is a flurry of clips and cables, and her breath fogs in the brackish air."
    show dr_lian_obasi at left:
        zoom 0.7

    dr_lian_obasi "Look at the cross-section here—three meters of scouring in the last fortnight at high tide. The living breakwater prototype attenuated wave energy by maybe thirty percent in controlled runs, but—' (She taps the tablet.) '—TideLine's stress sims show a forty-to-fifty percent reduction, in their conditions."
    "You flip through your battered notebook, fingers tracing Lian's calculations sketched in salt-streaked ink. You compare her raw sensor plots to TideLine's glossy simulations. The difference is not small; it's the difference between 'likely' and 'reassuring.'"
    "You (internal): You want to trust the math. You want numbers to remove the ache of decisions. But numbers are rhetorical, too—arranged to comfort the people who write the checks. The sea does not care which spreadsheet is prettier."

    dr_lian_obasi "If we scale the living breakwaters and plant cordgrass at these nodes—' (she points) '—we can slow the scouring. It won't be immediate. It won't be a wall. But it preserves access. It keeps the substrate alive."
    show marin_sol at right:
        zoom 0.7

    marin_sol "We need to be honest about timelines.' (You close the notebook, the pages whispering.) 'And we need an auditor who can read sensor systems, not just corporate PR."
    "Dr. Lian nods, jaw tight. 'I can do the technical reading, but political trust is different.'"
    "You both stand. Salt hangs in the air like a taste on your tongue—metal and brine and something like old rope. You walk the boardwalk with the sensors humming underfoot, and each creak feels louder, as if the sea is testing the seams of town patience."
    # [Scene: Pier | Dusk]
    hide dr_lian_obasi
    hide marin_sol

    scene bg ch10_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Boots on slick wood, the soft clink of Kaito's pendant against his chest]
    # play music "music_placeholder"  # [Music: A higher, urgent tempo—pulsing glissandi like approaching tide]
    "Kaito Navarro waits near the co-op, a carved whale talisman—small, worn, familiar—on a leather cord at his throat. He lets the talisman rest between his fingers, the gesture plain and human."
    show kaito_navarro at left:
        zoom 0.7

    kaito_navarro "You called for an audit,' he says without preamble. (His voice is steady, the kind that has pulled lines in storms.) 'Why waste time when people need food and roofs? We lose one tide and nothing you write in a notebook matters."
    show marin_sol at right:
        zoom 0.7

    marin_sol "Because what if a quick fix takes our shore away? What if we sign away fishing rights, or privatize the pier? An audit is meant to peel back—' (you gesture, helplessly encompassing promises and contracts) '—the fine print."
    "Kaito Navarro: (He rubs his thumb over the whale talisman.) 'They promised jobs. Immediate reinforcement. Money. Do people eat promises? My father didn't trust promises, Marin—he trusted the sea. He said, 'You keep the nets tight"
    "and the town tighter.' People here need to know they'll be safe next week, not in five years.'"

    marin_sol "I know.' (You hear the guilt settle like wet sand.) 'I'm trying to buy clarity, not delay for its own sake."

    kaito_navarro "Then make it fast,' he says, more softly. 'If you believe in what you're doing, make it quick."
    "Marin Solé: (Your hands clench.) 'I can't speed trust. I can only ask for transparency.'"
    "Kaito's face shifts—pride and frustration braided together. He steps close enough that salt air and the scent of his fisher-sweater are immediate. 'Don't make the town pay for your caution.'"
    "You (internal): His words are a pull at the seam where private affection meets communal duty. You want to tell him you are being careful because you care about everyone, including him. But words risk being"
    "read as excuses. You keep the necklace of reasons in your chest and smile too tightly."

    menu:
        "Promise Kaito quick progress":
            "You say you'll push the audit timeline—accelerate letters, call in favors. He relaxes a fraction, trusting the action more than the word."
        "Admit you can't promise speed":
            "You tell him you can't promise speed without compromising the review. He withdraws a step, the hope on his face thinning into something contained and wary."

    # --- merge ---
    "The conversation continues."
    # [Scene: Rooftop Community Garden & Storm Shelter | Night]
    hide kaito_navarro
    hide marin_sol

    scene bg ch10_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: A taut cello line; urgency underlaid with low, metallic percussion]
    # play sound "sfx_placeholder"  # [Sound: Cicadas, distant shouts, the soft rattle of a sign in the wind]
    "Mayor Ana Beltran calls you in before the council closes for the night. Her raincoat looks heavier than it should; the city's anxieties sit on her like a sodden cloak."
    show mayor_ana_beltran at left:
        zoom 0.7

    mayor_ana_beltran "Marin.' (Her voice is official, then softening.) 'Delay is a political liability. We have donors calling and families at the shelters. If a storm—' (she does not finish; you both know what she means) '—if something hits while we audit, they will say you fenced us off from help."
    show marin_sol at right:
        zoom 0.7

    marin_sol "It isn't fence; it's examine.' (You place your notebook between you on the table, a small, battered talisman of method.) 'A contract can change the landscape of where people can fish. We need proof."

    mayor_ana_beltran "Proof doesn't stop waves.' (She leans forward.) 'People want options now. Jun says TideLine will suggest a neutral auditor. The company is willing to step back while an audit is ongoing—publicly. It solves optics."

    marin_sol "It may also put the audit in their frame.' (You feel each syllable like a stone.) 'If TideLine suggests names, we end up with an audit that clears their math and leaves our rights encumbered."
    "Mayor Ana Beltran: (Her jaw tightens.) 'We need to balance legal caution with practical safety. If you push too hard on independence, you could be seen as obstructionist.'"
    "You (internal): The word 'obstructionist' lands like a pebble in your gut. You taste salt and iron. The mayor is right—delay can be framed as stubbornness. But surrender is a different kind of erosion."
    "Dr. Lian sends you an updated dataset through Jun: a heavier set of scouring readings flagged with red icons. You flip pages, fingers stained with salt and ink. The numbers creep; the worst pockets of erosion are migrating faster than models predicted."

    "Dr. Lian Obasi (via message, voice)" "If TideLine's simulations are optimistic, and our sensors are underestimating storm surge under compound events, there's a nontrivial chance the buffer fails during a large tide surge. We need redundancy."

    marin_sol "Then redundancy is the point of this pause.' (You are shouting into the thin rope of diplomacy now.) 'Either we secure ownership protections in the contracts, or we protect space for locally managed adaptation."

    mayor_ana_beltran "Contracts are messy.' She pins you with a tired look. 'Time is messier."
    # [Scene: Pier — Late Night]
    hide mayor_ana_beltran
    hide marin_sol

    scene bg ch10_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Percussive spikes—quickening then holding]
    "Old Tomas joins you for a walk, his cap pulled low. He moves slowly but with an attention that has the weight of memory. His face is a topography of storms endured."
    show old_tomas at left:
        zoom 0.7

    old_tomas "Used to be, when the sea took something, it also returned something—lessons, sometimes fish. Now it takes and takes.' (He pauses, gaze on the horizon.) 'They make walls in the south. We saw 'em put up and call it progress. Then the fish moved. That was the year my brother lost his nets for good."
    show marin_sol at right:
        zoom 0.7

    marin_sol "Do you think—' (your voice is small) '—do you think an engineered approach could work here if it respected our patterns?"

    old_tomas "Engineered is a nice word for 'someone else decides who can live with the water.' Your living reefs—those take the tide back the way it once was. They ask a lot of patience.' (He taps your notebook.) 'You listen to the water. You also listen to the people."
    "You (internal): His stories bruise against the political calculus. Listening feels like an action and a curse; it slows you, and while you listen, money and momentum gather on the other side."
    "Old Tomas reaches into his pocket, pulls out an old photograph—salt-stained, edges curled. A long-ago pier, same ropes, different faces. You see the town younger, less guarded."

    old_tomas "This place remembers. That memory can be weapon or shield.' (He looks at you directly.) 'Don't let them take our stories for a schematic."

    marin_sol "I won't."
    # play music "music_placeholder"  # [Music: Builds—violins edge up; drums tap staccato]
    # play sound "sfx_placeholder"  # [Sound: A far-off siren wails; a low tidehorn moans in the distance]
    "You return to the rooftop alone. Your notebook is open to a page where Dr. Lian's sensor plots are juxtaposed to TideLine's glossy diagram sent by Jun. Your hands shake as you annotate—pen scratching, breath quick."
    "You (internal): The audit could reveal hidden clauses—a surrender of maintenance rights, a clause to transfer access, thresholds where TideLine's 'managed' defense becomes privatized. Or the audit could be a pretext. Either way, time is a thief tonight."

    menu:
        "Call Dr. Lian and ask her to prioritize key indicators for the audit":
            "You ring Lian. She answers, immediate: 'I'll extract the failure-mode signatures and timestamped sensor logs. If there's something, it'll show.' Her voice is a line in the noise."
        "Draft a public notice explaining why you stalled the vote":
            "You start a post for the community board—careful, clear. Before you hit send, Rosa appears, frowning: 'Tone it down. People are raw.' You save the draft. The quiet decision not to publish feels like another weight."

    # --- merge ---
    "The rooftop scene continues."
    "Rosa finds you on the rooftop then, paint-splatters bright against her overalls. She puts both hands on your shoulders, steady as an anchor."
    show rosa_sol at center:
        zoom 0.7

    rosa_sol "You're trying to hold too many things, Mari.' (She uses the shorthand—old comfort.) 'This town needs you. But it also needs to not lose its head."

    marin_sol "I know. I can't make everyone happy.' (You let out a breath that tastes like the sea.) 'I can only try to make a choice that doesn't sell our future."

    rosa_sol "Then be clear. Not with the people who already agree with you—talk to the ones who don't. Tell them why 'independent' matters. Don't hide."
    "You (internal): Her bluntness is a map. You see the faces in the meeting again—Aria's precise smile, the mayor's tired lines, Kaito's steadiness. Each of them is carrying a burden you have touched; each burden wants to convert into a decision tonight."
    # play sound "sfx_placeholder"  # [Sound: A faint ping from your comm]
    hide old_tomas
    hide marin_sol
    hide rosa_sol

    scene bg ch10_453e40_6 at full_bg
    "You don't recognize the sender immediately. Your heart stutters. The page in your notebook waits for your next annotation. The city breathes beneath the rooftop—awaiting."
    "You press to open the message, and the world narrows to the thin rectangle of light."
    # play music "music_placeholder"  # [Music: Sudden silence, then a single high, sustained note—only the wind and your pulse]
    "You (internal): The audit—what you asked for to slow the race—might be arriving in the most dangerous shape: already in public hands. The possibilities spool out like a net—exposure, vindication, chaos. For a second you taste iron: fear and adrenaline."
    # [Page-Turn Moment: You hover over the message, thumb trembling. Whatever is inside could confirm your worst fears or deliver a clarity that saves the town—or it could be the spark that splinters trust into flames. The rooftop seems to hold its breath with you. You are not certain who will be hurt when the inbox opens; only that someone will be.]

    scene bg ch10_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter11
    return
