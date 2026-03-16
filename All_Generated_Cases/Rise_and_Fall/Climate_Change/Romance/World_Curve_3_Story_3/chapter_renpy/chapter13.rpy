label chapter13:

    # [Scene: Press Conference | Morning]

    scene bg ch12_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Camera shutters, murmured questions folding into a low, restless tide]
    # play music "music_placeholder"  # [Music: Steady, hopeful strings — restrained, gathering momentum]
    "You steady yourself behind the microphone. The paper in your hands cramps slightly under your damp thumb; the names of missed dispatches and the timestamps you pulled from the municipal logs are printed in a dense"
    "column. The air smells of rain on pavement and printer toner — small, ordinary things that make the day feel unbearably real."
    "Your tide-watch rubs against the edge of the podium; the brass is warmed by your palm. You let the second hand find its rhythm and breathe into it. If this is the public unspooling of what"
    "you've found, then there is no turning back. Accountability is a loud thing; it will bruise people, and it will save them."
    "Dr. Ayla Voss stands a step behind you, her posture precise, her fingers folded around a slim folder. For a moment the two of you make a tableau: the scientist whose reports feed the machine, and"
    "you — who brought that machine's teeth into the light. The cameras tilt forward as if sensing the small, consequential alliance."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "Good morning. My name is Maya Reyes. I returned to Marisora because I could not stand to watch us disappear in silence."
    "You hear the rasp of a reporter's pen. The crowd leans in like a tide pooling at a break. You force yourself to slow, to let the facts land."

    maya_reyes "The data I'm releasing today shows a pattern of delayed alerts and misallocated emergency funds. Those delays meant that some calls for assistance were never escalated. I brought the names of the missed dispatches and the timestamps. We deserve to know who decided not to act — and why."

    "A reporter" "Ms. Reyes, are you asking for an inquiry?"

    maya_reyes "Yes. A regional inquiry with independent oversight and a mandate to review response timelines, fund allocations, and accountability measures."
    hide maya_reyes

    scene bg ch12_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A single fork dropping somewhere in the crowd — small, audible]
    # play music "music_placeholder"  # [Music: Strings swell a notch, then settle]
    "Dr. Ayla Voss steps forward, her voice measured, the words clinical and precise at first."
    show dr_ayla_voss at left:
        zoom 0.7

    dr_ayla_voss "As the assigned regional scientist, I will cooperate fully. There are structural failures we must correct, and I will work within the system to ensure we do so."
    "You watch a flicker cross her face — not warmth exactly, but something closer to recognition. She does not soften; she aligns."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "It won't be easy. There will be scrutiny and blame. We must make sure the outcome centers people — not just statistics."

    dr_ayla_voss "People, yes. Dignity, yes. We will include provisions for cultural preservation funds and a resettlement trust in the scope of the inquiry."
    "You feel the room tilt toward you — not entirely with you, but toward the possibility that what you are asking for could become real policy, not a headline. Your chest loosens in a way you didn't know you needed."

    menu:
        "Take the microphone now and name specific departments":
            "You clear your throat and begin to read names and timestamps, your voice steady; the crowd listens like a town holding its breath."
        "Let Ayla open with the institutional framing":
            "You nod to Ayla, letting her set the procedural terms; the press takes notes on jurisdiction and oversight, and your details appear as the human center of her statement."

    # --- merge ---
    "Scene continues"
    hide dr_ayla_voss
    hide maya_reyes

    scene bg ch12_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A murmur, then a round of polite but loaded questions]

    "A reporter" "Dr. Voss, how will the inquiry be structured? Will it have subpoena power?"
    show dr_ayla_voss at left:
        zoom 0.7

    dr_ayla_voss "The inquiry will be regional, independent, and empowered to subpoena records. It will produce a public report and recommendations, including a resettlement trust and cultural preservation fund — items we will insist are included in any remedial packages."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "We also need a humane protocol for relocation — not a stamped form, but a phased plan that includes archives, seed banks, community rituals, stipends for artisans, and counseling. People need to carry their stories with them."

    dr_ayla_voss "I have already drafted language that secures funding for culturally sensitive measures. It needs political will and witnesses. Your voice gives the process credibility in the town."
    "You and Ayla exchange a look that is not quite an apology and not quite a celebration — something raw and institutionalized at once. It is an alignment born of necessity and, beneath that, of two"
    "people recognizing their skills can be stitched together for a result neither could achieve alone."
    # [Scene: Municipal Hall / Inquiry Hearing | Afternoon]
    hide dr_ayla_voss
    hide maya_reyes

    scene bg ch12_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmured consultations, a recorder's click, the scratch of legal pads]
    # play music "music_placeholder"  # [Music: A resilient cello theme, resolute but warm]
    "You sit at the witness table. The air is a blend of recycled heat, strong coffee, and the faint, briny edge that clings to anyone who has lived by the sea. The inquiry chair opens with formalities; the questions start measured, then sharpen."

    "Inquiry Chair" "Ms. Reyes, can you explain how you compiled the dispatch logs?"
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "I cross-referenced public emergency logs with raw system timestamps and private community reports. Where the timestamps showed delayed escalation, I matched them to local calls. There is a pattern across multiple incidents."
    "The chair's pen taps. The questions come in waves — legalese about jurisdiction; pressed urgency about intent; a probing that tries to pull motive out from beneath method."

    "Council Member" "Dr. Voss, is it not possible that these delays are systemic, caused by resource constraints rather than malfeasance?"
    show dr_ayla_voss at right:
        zoom 0.7

    dr_ayla_voss "Resource constraints are real, but the allocation decisions are not neutral. There were recommendations to re-route funds to early-warning infrastructure which were not implemented. Whether that is negligence or intentional misprioritization is for the inquiry to determine."
    "You find yourself speaking more than you planned. You draw lines between spreadsheets and lived nights of loss. You name consequences without theatrics — the displaced family whose generator never arrived, the neighborhood whose evacuation alert came hours too late."

    "A voice from the gallery" "You saved us."
    "You don't turn. You let the words settle where they are meant to land: not on you alone, but on the system that made such saving necessary."

    dr_ayla_voss "We will recommend accountability measures and restoration of misallocated funds. We will insist on a resettlement trust that is administered with community input."

    maya_reyes "I will stay on as a technical advisor for the trust. I cannot undo everything that happened, but I can help build the structures that prevent repetition."

    dr_ayla_voss "And I will use my position to push the recommendations through the regional offices. They will be difficult battles; I won't pretend otherwise."
    "For a few seconds the hearing is quietly human — two people in different clothes, converging toward the same stubborn aim. There are nervous glances from officials; someone clears their throat. The cameras blink. The recorder clicks."

    menu:
        "Glance toward the gallery to find Elias":
            "You look up and find Elias standing in the back, jaw set, palms folded; he lifts his chin in a private signal — equal parts apology and vow."
        "Keep your eyes forward, focus on testimony":
            "You keep your gaze on the panel, letting your answers carry the weight without distraction; your resolve hardens like a sealant, practical and contained."

    # --- merge ---
    "Scene continues"
    "The hearing continues into late afternoon. The inquiry committee promises a timeline and public hearings. You feel a small, improbable bloom of relief — the machinery is slow, but it is moving, and it is moving because you forced it to."
    # [Scene: Relocation Trucks / Early Morning]
    hide maya_reyes
    hide dr_ayla_voss

    scene bg ch12_f99e88_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low diesel rumble, neighbors' soft voices, children's quiet footsteps]
    # play music "music_placeholder"  # [Music: Warm horns and an ascending string motif — the music of beginning anew]
    "Dawn comes like a promise. The trust you fought for exists on paper and in pockets of cash disbursed quickly to honor the inquiry's urgent recommendations. The relocation protocol runs like a conveyor of care: phased"
    "departures, community liaisons, cultural preservation payments, and a staff of volunteers who came from nearby towns with water and blankets and sandwiches."
    "You stand by the trucks directing families, hands full of checklists and small comforts — salt-stained towels, envelopes with stipends, packets of heirloom seeds from the greenhouse. The smell of diesel mixes with cinnamon buns someone"
    "has set out, and there is a strange, tender ordinariness to the scene that underlines its gravity."
    "Elias Jun moves like he always does: hands busy, sleeves rolled, shouting soft instructions with the grin that makes people trust him even when their knees wobble. He organizes the teams that will build new mangrove"
    "lines at the resettlement sites and signs every crate with a smudge of paint and his name."
    show elias_jun at left:
        zoom 0.7

    elias_jun "Maya! Come look at the planting schedule — the tides are forgiving in two weeks; we can get the first buffer planted before the rains."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "And you'll let me pretend I'm handy with a spade?"

    elias_jun "You'll be the brains; I'll be the blisters. We'll be a good team."
    "You let the joke settle between you like a bandage and find that you mean it in the honest, unvarnished way you sometimes hide from others. There is grief here — the places left behind, the"
    "things that will not be carried in boxes — but there is also a plan that honors stories and makes space for them."
    "You walk between clusters of people, handing over labeled boxes — a family's recipe books, a musician's instrument, a fisherman's logbook. Someone presses a worn photograph into your palm: a house on stilts, children on the stairs. You tuck it into the resettlement trust's archive trunk yourself."

    "A volunteer" "Miss Reyes, your tide-watch — are you keeping it?"
    "You touch the brass; the second hand keeps turning through the dawn. You realize you are not keeping everything. But some things you will."
    "Elias Jun finds you by the largest truck. You speak privately, the hum of engines making a low prayer around you."

    elias_jun "We could stay, you know. Try to make something else here."

    maya_reyes "We tried. We did everything we could. This — what we are doing now — it saves people. It gives them dignity. That's why I couldn't stay silent."

    elias_jun "So we build — together, but in different places. I plant mangroves here and at the new site. You design the plans that keep them safe. We visit. We write. We'll make the distances mean something."

    maya_reyes "Long-distance hope. It feels oddly like a scientific experiment."

    elias_jun "One with a high success rate. Promise me you'll come to the first mangrove planting. Wear that ridiculous green scarf of yours."

    maya_reyes "I promise."
    "You hold each other in a quick, private space between trucks and sunrise. It is a different kind of homecoming: a decision to love across miles, to trust the scaffold you have built together to carry"
    "that love. The resettlement buses begin to roll, slow and steady, and the people inside lean toward the windows with small, brave faces. You watch them go, clutching the boxes labeled with their lives."
    hide elias_jun
    hide maya_reyes

    scene bg ch12_f99e88_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Truck doors shutting, a child's murmured song, the distant call of gulls]
    # play music "music_placeholder"  # [Music: Strings resolve into an ascending major chord, bright and resolute]
    "You stand on the tailgate for a moment, feeling the salt air like an old friend and something like a new oath. Regret sits with you — for the houses that will be left, for the"
    "late calls that could not be unmade — but it is accompanied now by the clear shape of consequence turned toward care."
    "Dr. Ayla Voss finds you there, holding a small archival box. Her expression is not softened into sentimentality; it is steadier. She offers you a formal nod that almost manages a smile."
    show dr_ayla_voss at left:
        zoom 0.7

    dr_ayla_voss "The report will be published next week. The regional office has pledged the funds for the trust. There will be hearings about culpability. There will be pain. But there will also be mechanisms to prevent this pattern repeating."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Thank you. For pushing it through."

    dr_ayla_voss "Thank you for making it public. For giving the inquiry its moral center. It is easier to hide behind data, but harder to look communities in the face. You made it harder to ignore them."
    "You think of the ledger of names still creased in your bag, of Rita's hands and Mayor Tomas's complicated compromises. You think of the seasons of mangrove plantings that will come, of boxes unpacked in new kitchens, of stories told at new tables."
    "Elias brushes a thumb along the tide-watch band. His fingers are warm; the sun hits his hair like a benediction. You close your hand over his for a second that promises continuity without pretense."

    maya_reyes "We saved lives by exposing what was hidden. That won't erase hurt. It will, I hope, prevent more of it."
    show elias_jun at center:
        zoom 0.7

    elias_jun "We'll rebuild — not to recreate what was, but to carry it forward. We'll plant roots in new soil so stories can grow."
    "You step back from the truck and look toward the horizon where the sea meets a sky that has finally cleared. There is work ahead: the inquiry's legal battles, the slow transfer of funds, the labor"
    "of building habitats that respect what people carry with them. There is also a strange, rising clarity — a moral spine that feels like relief."
    hide dr_ayla_voss
    hide maya_reyes
    hide elias_jun

    scene bg ch12_f99e88_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Engines fade, a chorus of distant voices that promise to reconvene in letters, in texts, in the slow work of visits]
    # play music "music_placeholder"  # [Music: Triumphant yet tender motif — uplift without denial]
    "You keep the tide-watch on your wrist and let the small hand move. In your pocket, the resettlement trust's first disbursement notice folds like an accord. You have traded a place for people's lives and chosen to protect the stories that make those lives human."
    "There will be tribunal reports and late nights drafting policy language; there will be the ache of absence and the lightness that comes when a system finally answers to the people it serves. You accept the cost because it is the honest cost of saving what matters."
    "You climb the small rise behind the trucks and look back once. The town is a ribbon of rooftops and gardens, a collection of memories that you will carry forward in plans and plantings and the small, stubborn rituals you insist be moved with the people."

    scene bg ch12_f99e88_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A lone gull cries; the convoy is a thread down the road]
    # play music "music_placeholder"  # [Music: Strings settle into a warm, conclusive chord]
    "You turn, feeling the weight of what you've done balanced by the unexpected lightness of moral clarity. Across the distance that will come between you and Elias, there is an unspoken contract: to love deliberately, to"
    "rebuild together in intent if not location, and to hold the town's story tenderly, wherever it lies."
    "You breathe. The second hand moves. The world shifts, as it always does — slowly, in tides — and you step forward into the work you chose."
    # play music "music_placeholder"  # [Music: Fade Out]

    scene bg ch12_f99e88_9 at full_bg

    scene bg ch12_f99e88_10 at full_bg
    "THE END"
    # [GAME END]
    return
