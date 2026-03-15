label chapter3:

    # [Scene: Community Garden & Rooftop Farm | Evening]
    # play music "music_placeholder"  # [Music: Low, pulsing strings; distant gulls cut through the drone]

    scene bg ch3_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The close chatter of a dozen neighbors, the scrape of a trowel, the soft clank of a prototype settling into place]
    "You climb the ladder with the compass heavy in your pocket. The rope handrail is slick where someone has rinsed rainwater into a basin; the scent of soil and citrus hangs like a promise. Nan moves"
    "between beds with the practiced slowness of someone who has learned to pace sorrow and seasons—her fingers peat-dark, her kerchief stained in concentric rings."
    show gracie_nan_armitage at left:
        zoom 0.7

    gracie_nan_armitage "Those lettuces need transplanting before the night wind chews them up. Maya, can you—"
    "You take the trowel she offers. Your hands know the small rituals: press, lift, cover. They are steadier than your thinking. Around you, the community settles into the planning night like a knot—tight, purposeful, anxious. Rafi"
    "squats near a battered tarp, fiddling with a frame of reclaimed PVC and foam—his low lamp glows bluish and clinical against the warm sun."
    show rafi_chen at right:
        zoom 0.7

    rafi_chen "If we can get buoyancy right, these will float with the tide. Low-tech, low-cost. We stitch them to the docks, rotate them seasonally—keep food production moving even when water claims a patch."
    "You glance at the prototype; it smells faintly of oil and glue. Rafi grins, paint flecks across his cheek."

    rafi_chen "Also—if we torque the anchoring right, the planters can act as minor breakwaters. Think beds and buffer at once."
    "Your wearable bracelet chirps — a brief, sharp note against the ambient hum. The LED blinks a thin yellow: NEW ANOMALY. Your stomach tightens with the same muscle that clenches when the tide line crawls up"
    "the promenade. You pull it aside with a gloved thumb, the silicone warm from your wrist."
    "You think: another variable. More data to fold into a conversation already weighted like a net. You tuck the thought—no, you try to—beneath meeting logistics. The town's two-week window is not a thought to be shelved."
    # play sound "sfx_placeholder"  # [Sound: Rain begins to spit; a thin percussion on the greenhouse plastic overhead]
    hide gracie_nan_armitage
    hide rafi_chen

    scene bg ch3_98c6f2_2 at full_bg
    "Neighbors begin to speak in clusters. The arguments are less about facts tonight and more about feeling: fear braided with fury, grief softening into practicality."

    "Woman in the corner (Elder)" "If Evelyn brings money, that'll buy boats for some. It'll keep folks fed now. What's the point of ideals if the roofs are gone?"

    "Man beside her" "Money tied to oversight is fine—so long as we don't get sold out. We've seen that before."

    "Another voice, younger and sharp" "No developers. Not again. We keep this ours or we lose more than buildings."
    "You pull the compass from your pocket and trace the worn brass with your thumb. Its edge catches a stray shaft of light. It has always pointed you toward practical calculations and stubborn directions. Tonight its needle trembles like a finger over a map you don't want to redraw."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "Look. We don't have to romance a perfect answer. We can stitch things together. Keep the co-op intact, take what helps, refuse what doesn't. My grandfather wouldn't have said no to mending a net that keeps fish in the boat."
    show maya_armitage at right:
        zoom 0.7

    maya_armitage "And if the 'what helps' comes with strings that choke the coop? Or if 'taking what helps' starts with promises we can't enforce?"

    jonah_reyes "Then we bind them with something they can't wriggle out of. Oversight. Legal teeth. People in seats. Not just lip-service."
    show rafi_chen at center:
        zoom 0.7

    rafi_chen "We can build accountability into the pilot—real-time metrics from the piers, community auditors, a rotating oversight panel. Tech can make them honest if we design the system."
    "A murmur of assent. Then a darker sound: the rustle of deep unease."

    menu:
        "Check the bracelet message now":
            "You pull up the anomaly on your wrist—it's a localized pattern: salinity spike near the northern inlet, paired with unexpected current shifts. You jot it down, fold it into the list of immediate vulnerabilities. The room leans in when you announce it; attention sharpens, but a tightness grows—another problem to solve."
        "Ignore it for the meeting":
            "You tuck the bracelet back under your sleeve and let the conversation run. For a few minutes, you can be present only to people, not to data. That small relief lets you breathe; later, the number will still be there, and the worry presses like damp cloth against your ribs."

    # --- merge ---
    "The rain picks up. A few folks drift closer to the greenhouse, where Nan has set out thermoses and a pot of soup. The steam smells of kelp-stock and rosemary—earthier than the council chamber's coffee. You move between clusters, taking in faces: tired, resolute, raw."
    "The rain picks up. A few folks drift closer to the greenhouse, where Nan has set out thermoses and a pot of soup. The steam smells of kelp-stock and rosemary—earthier than the council chamber's coffee. You move between clusters, taking in faces: tired, resolute, raw."

    "Rafi flicks a wire, demonstrating a clasp" "If the pier modules have a slot for our planters, and the contract guarantees maintenance and transfer terms, this could be a real bridge."

    "A woman near the fence, palms red from the evening's manual work, says soft and fierce" "Bridge or leash. We've had bridges that lead to auction houses. Evelyn's not a private thief—she's a city that can forget us when projects stabilize her resume."

    maya_armitage "How do we trust anyone who didn't grow here? How do we make sure we don't sell what Nan's kept alive for us?"
    hide jonah_reyes
    show gracie_nan_armitage at left:
        zoom 0.7

    gracie_nan_armitage "Trust is not blindness. It's learning who's carrying what weight. Sometimes you share it, sometimes you ask someone to carry part because your knees are failing. Ask them how they will steady the load."
    "Jonah Reyes's hand finds yours on the railing and squeezes—brief, grounding. You feel an ache behind your ribs: the old pattern that if you can fix enough things, no one you love will have to leave. It is a tidy heroic myth, and it is cruelly unrealistic tonight."

    menu:
        "Tell Jonah you need him to be blunt":
            "You say it plainly—'Be straight with me. What's the real cost if we partner?' He swallows, then lays out the risks he's seen: conditional funding that phases out community control, maintenance contracts that benefit the city contractors, and social fragmentation when some accept buyouts and others can't. His voice is quieter, the grief beneath it more audible, and you understand the measure of what he's guarding."
        "Ask Jonah to give a speech for the co-op":
            "You ask him to stand and speak for the cooperative's values. He hesitates, then rises, words finding the tether between tradition and plausible compromise. He speaks of nets and relatives and the stubbornness of people who refuse to be moved. The crowd responds—soft applause, a few tears—momentary solidarity that tastes fragile and necessary."

    # --- merge ---
    "Night deepens. Arguments fray into tired jokes; tired people tighten into small circles. You catalog positions in your head like tidemarks: those who want Evelyn's funds now; those who will not even consider the city; those who think retreat first is mercy. None of these lines map neatly onto friendships."
    "Night deepens. Arguments fray into tired jokes; tired people tighten into small circles. You catalog positions in your head like tidemarks: those who want Evelyn's funds now; those who will not even consider the city; those who think retreat first is mercy. None of these lines map neatly onto friendships."
    # play music "music_placeholder"  # [Music: A low, melancholy cello; the tempo slows]
    hide maya_armitage
    hide rafi_chen
    hide gracie_nan_armitage

    scene bg ch3_98c6f2_3 at full_bg
    "You sleep on a bench for an hour, breathing the greenhouse's humid lullaby. When you wake it is near dawn, the sky gray and clean. Your bracelet buzzes again—another anomaly, this time a predictive flag for"
    "a storm surge pattern converging with higher salinity bands. You write it down and fold it into the morning's briefing. There is a clarity in the numbers that is almost merciless."
    # [Scene: Highwater Cove Harbor | Morning]
    # play sound "sfx_placeholder"  # [Sound: The low throb of a city van rumbling in the distance; gulls sharper in the chill air]

    scene bg ch3_98c6f2_4 at full_bg
    show evelyn_hart at left:
        zoom 0.7

    evelyn_hart "Maya. I believe in decisive action."
    show maya_armitage at right:
        zoom 0.7

    maya_armitage "Evelyn."
    "Her handshake is quick, well-calibrated. She lets the conversation start at public-safety language, then steers it toward deliverables."

    evelyn_hart "We can pilot modular piers with adaptive planters. We'll fund the build, train your labor force, and provide oversight through the city's coastal unit. In exchange, the city would like the pilot footprint and rights to evaluate scalability."
    "You notice the posture shift among neighbors: for some, the word 'fund' lands like rain; for others, 'rights' tastes like a lead in their mouths."

    maya_armitage "Oversight can mean many things. Who sits on that panel? What are the transfer clauses? How long is the pilot, and what recourse does the community have if the city terminates maintenance?"

    evelyn_hart "We can write binding accountability into the memorandum. A rotating community oversight panel— seats filled by locally designated representatives. Regular audits. Public metrics. We want a model the rest of the region can adopt. You get funding, you get stability, you retain governance in practice."
    "A chorus of glances, the air charged with small electricity. Some faces relax. Others harden."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "Your 'binding' has to mean more than words. How do we stop transferral of maintenance to contractors who bid low and cut corners? How do we keep the coop's ownership alive when corporate accounting says 'efficiency'?"

    evelyn_hart "You speak like someone who fears change because they equate it with loss. We have metrics—real outcomes. We secure livelihoods. We can't stand around waiting for a perfect ideal that leaves roofs gone."

    maya_armitage "And the buyout options—what about the phased retreat offers for vulnerable households? Are they separate from the pilot or part of cost calculations?"

    evelyn_hart "We will include relocation packages where necessary, targeted to households flagged by the city's vulnerability assessment. We also offer workforce retraining for those whose livelihoods shift."

    "A woman near Nan braces herself and asks a private question to Evelyn—her voice small" "If I accept a buyout, will I be able to come back? Will my place be protected?"

    evelyn_hart "We can include relocation covenants that protect returning rights under specific conditions. We don't want to erase the past. We want to make a future where people can stay safe."

    maya_armitage "The sentences soften as they come out of her mouth. They are polished, designed to land. You do not feel certain they are meant for you; rather, they are meant for the cameras and for journalists who will print a narrative where the city rescues a town. The calculus is colder elsewhere—what is necessary to scale may strip nuance."
    # play sound "sfx_placeholder"  # [Sound: A distant, sharp honk from a barge; gulls wheel and call]
    hide evelyn_hart
    hide maya_armitage
    hide jonah_reyes

    scene bg ch3_98c6f2_5 at full_bg
    show gracie_nan_armitage at left:
        zoom 0.7

    gracie_nan_armitage "You can build a pier that holds a plant. You can build a pier that eats us. Which is this?"
    show evelyn_hart at right:
        zoom 0.7

    evelyn_hart "That depends on the guardrails you and the city agree to."
    show maya_armitage at center:
        zoom 0.7

    maya_armitage "Guardrails can be bent."

    evelyn_hart "Then write stronger rails. We will accept stronger rails if you give us a chance. But understand: delay costs homes."
    "The phrase lands like a stone. Some people nod; others look at you like they expect you to catch it before it sinks."
    hide gracie_nan_armitage
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "Two weeks is the time you keep telling us we have. It's not infinite. People can't sleep out on a vigil forever. If this is a real offer, don't make it sound simpler than it is. Show us the contracts."

    evelyn_hart "You will have them by noon. I invite you—invite all community representatives—to review them with our legal team. We will not sign without your agreement."
    "You feel the old perfectionist reflex: I can take this on. I can negotiate every comma until the world is safe. It costs you something to hold that belief—sleep, love, trust in the human rhythm of compromise."
    hide evelyn_hart
    show rafi_chen at right:
        zoom 0.7

    rafi_chen "We can draft oversight clauses tonight. We can make the pilot contingent on community-controlled maintenance budgets. We can demand transfer clauses with real teeth."
    "A rumor of hope flickers."
    "Then, another thought coils in your chest: what about those who can't wait? The elderly, the sick, the families whose roofs drip like metronomes? What about the ones for whom two weeks is already past?"
    # play music "music_placeholder"  # [Music: The cello returns, lower; the tone is not angry so much as exhausted]
    hide maya_armitage
    hide jonah_reyes
    hide rafi_chen

    scene bg ch3_98c6f2_6 at full_bg
    "You look at the faces assembled. The town has split into rough lines—not wholly, but enough that any decision will wound someone. You picture the abandoned promenade's tide line graffiti, the inscription of loss in seaweed"
    "and driftwood. You picture Nan's hands. You picture Jonah's neat, practical anger. You picture Rafi's wireframe fingers. You feel your chest tighten until the compass in your pocket bites into your ribs."
    "Your mind catalogs outcomes, like a scientist forced to make a moral model: preserve autonomy and risk collapse; accept partnership and risk erosion; retreat now and protect bodies but scatter a town."
    "You know your voice will matter. You know that whatever you lean toward will carry consequences that are not theoretical but personal. You taste salt and old iron on the air—salt from the sea, iron from the fear that runs through everyone here."

    scene bg ch3_98c6f2_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rain crescendos then blinks—a silence, like the world inhaling]
    "It is the kind of moment that asks you to choose which ache to carry, and for how long."

    menu:
        "We refuse any top-down funding and mobilize entirely community resources.":
            jump chapter4
        "We negotiate a partnership—accept pilot funding but demand community oversight and binding accountability.":
            jump chapter7
        "Prioritize phased buyouts and managed retreat for the most vulnerable to minimize immediate loss.":
            jump chapter10
    return
