label chapter14:

    # [Scene: Restored Quay | Dawn]

    scene bg ch12_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Gentle, ascending strings with soft percussion]
    "Narration:"
    "You arrive before most of the town—because old habits die hard and because there is still work that needs the quiet before people wake into it. The quay looks different in the thin light: less hunched"
    "and exhausted, more stitched. Sandbags have been replaced in places by pale, curved modules that slope like ribs; in other stretches, rows of mangrove shoots stab green and defiant from the mud. Scent of wet earth"
    "and frying citrus from Elena's morning stand tangles with diesel and salt, but sweeter now—like possibility."
    # play sound "sfx_placeholder"  # [Sound: Distant chatter, the clank of a tool being set down, a small engine calibrating]

    scene bg ch12_e67f19_2 at full_bg
    show aria_navarro at left:
        zoom 0.7

    aria_navarro "This is what durable looks like—not a single heroic thing, but many small things held together by rules and by hands that remember how to hold each other."
    show dr_kavir_singh at right:
        zoom 0.7

    dr_kavir_singh "The data stream's stable. If we keep the response window under thirty minutes, the predictive alerts are actually averting the worst shore erosion projections."
    "Narration:"
    "You nod, checking the tablet Dr. Kavir Singh hands you. The dashboard is a tidy river of green and amber instead of the jagged red spikes it used to be. Protocol checklists are pinned like talismans"
    "to the lab's message board: who calls whom, how to mobilize the towboats, when to deploy shutters."
    show mayor_isla_cortez at center:
        zoom 0.7

    mayor_isla_cortez "You did good, Aria. The council had its ugly hours, but the operational manual you pushed for—it's readable, enforceable. People can follow it."

    aria_navarro "We wrote it together. You signed it not because you wanted to be the hero, but because the town needed someone to click the seal."

    mayor_isla_cortez "Maybe. Or maybe I needed someone to show me how to let the town lead and keep the ledger straight at the same time."
    hide aria_navarro
    show mateo_hale at left:
        zoom 0.7

    mateo_hale "The modules held overnight during the squall. We tweaked the ballast design—less lateral stress, better anchoring to the seabed. Jun Park's filter array helped with sediment monitoring."
    hide dr_kavir_singh
    show jun_park at right:
        zoom 0.7

    jun_park "And I promise the next batch won't singe anyone's eyebrows."
    hide mayor_isla_cortez
    show sora_lin at center:
        zoom 0.7

    sora_lin "There were mornings when I doubted we'd get here. But you—' (they look at you) '—you kept saying people have to decide together. You kept pushing for us to be in the room."
    hide mateo_hale
    show aria_navarro at left:
        zoom 0.7

    aria_navarro "When the council could have centralized, when the storm's drum threatened to drown debate, you chose process: enforceable protocols, citizen liaisons, on-call rapid teams. It felt like threading a needle—fast but gentle."
    hide jun_park
    show dr_kavir_singh at right:
        zoom 0.7

    dr_kavir_singh "We also secured the regional funder tranche. They liked the accountability matrix—auditable actions, community stewards on each response team, rotating oversight so no one office hoards power."
    hide sora_lin
    show mayor_isla_cortez at center:
        zoom 0.7

    mayor_isla_cortez "And they liked results. The pilot's outcomes are replicable now. We can promise other towns it won't be just money thrown at concrete."
    "Dialogue Exchange — Multi-Turn:"
    hide aria_navarro
    show mateo_hale at left:
        zoom 0.7

    mateo_hale "Do you remember the first time we sat by the old tide charts and you traced the contour lines until your finger blurred?"
    hide dr_kavir_singh
    show aria_navarro at right:
        zoom 0.7

    aria_navarro "I remember you making coffee at midnight and arguing about tolerances."

    mateo_hale "I argued because I wanted there to be tolerances we could measure—things you could hold to. But better to have measures that respect soil and story."
    hide mayor_isla_cortez
    show sora_lin at center:
        zoom 0.7

    sora_lin "Story matters too. Metrics without meaning are just numbers someone forgets."

    mateo_hale "And meaning without durability gets washed away."

    sora_lin "And neither of us wants to watch our people float off on promises again."

    aria_navarro "So we stitched them. Standards for rapid response, and a council charter that mandates community custodianship—ecological restoration teams alongside engineering squads, each with veto and with shared budgets."
    hide mateo_hale
    show mayor_isla_cortez at left:
        zoom 0.7

    mayor_isla_cortez "Checks and balances born of necessity. It's what got us the funders' trust."
    "Narration:"
    "The conversation folds over into plans and small jokes. You feel the old tightness in your chest ease. Not gone—there is always more to do—but less like a stone and more like ballast: necessary and placed."

    menu:
        "Accept Elena's offered breakfast bundle":
            "You accept the wrapped packet; the citrus scent hits the damp air and a warmth unwraps through you. Elena taps your wrist like an old blessing. 'You're keeping this place—let it keep you back,' she murmurs."
        "Decline politely, saying you're heading to the lab":
            "You shake your head with a smile and say you'll take it later. Elena huffs a teasing sigh, but the warmth softens to a promise. 'Don't work yourself into the tide, niña,' she says."

    # --- merge ---
    "Small things like Elena's meal are more than sustenance; they're rituals of belonging. You choose, and the town answers with a fold of care that doesn't demand repayment."
    # [Scene: Rooftop Greenhouse & Community Rooftop | Late Afternoon]
    hide aria_navarro
    hide sora_lin
    hide mayor_isla_cortez

    scene bg ch12_e67f19_3 at full_bg
    # play music "music_placeholder"  # [Music: Warm acoustic guitar with a light choir swell]
    "Narration:"
    "By afternoon the rooftop is a cradle of conversations. People who once argued across council tables now sit shoulder to shoulder, legs dangling over the parapet. The rooftop smells of basil and salt and the faint"
    "metallic tang of the city's wiring. You climb the narrow ladder and plant your palms on the railing, letting the horizon’s slow arc settle into you."
    show sora_lin at left:
        zoom 0.7

    sora_lin "We painted the seal with everyone's fingerprints. It's messy and perfect."
    show aria_navarro at right:
        zoom 0.7

    aria_navarro "I like messy."
    show mateo_hale at center:
        zoom 0.7

    mateo_hale "I kept the technical footnotes outside—in case anyone wants to nitpick the tolerances. But then I saw the fingerprints and I realized I didn't want to be the only signature."

    sora_lin "Ah, so you finally accepted that art can be structural."

    mateo_hale "It can be structural if it has fasteners."
    "Narration:"
    "You laugh, and for the first time in the last months you notice how little your pulse jumps at their proximity. There's a steadiness now, a permission to be ordinary: to eat together, to argue wild-eyed about saplings, to linger after meetings."

    menu:
        "Reach for Mateo's hand across the seedlings":
            "Your fingers brush his, quick and warm. He doesn't pull away—his hand settles, anchoring. He gives a half-smile that says more than words."
        "Offer Sora a paintbrush to finish the seal":
            "Sora takes the brush with a grin, paint dotting their cheek. They lean in to tap your brow with a streak of turquoise, laughing as silence and color hold you both in the same bright place."

    # --- merge ---
    "These are not dramatic crossroads—no grand declarations under stormlight—but small, steady ties that thread you into a life that can be both work and home. You find you can be rigorous without being hardened, and tender without being unmoored."
    hide sora_lin
    show jun_park at left:
        zoom 0.7

    jun_park "Sensors are locked to the local mesh. If the tide's anomaly indicator lights, we'll get triaged callouts, and teams deploy within the protocol window. Plus—' (they waggishly point) '—your coffee is ready, Aria."
    "Narration:"
    "You take the mug, and warmth floods the same places anxiety used to claim. It is a soft, precise kind of victory."
    # [Scene: The Tidal Research Lab | Evening]
    hide aria_navarro
    hide mateo_hale
    hide jun_park

    scene bg ch12_e67f19_4 at full_bg
    # play music "music_placeholder"  # [Music: Quiet piano motifs with rising orchestral pads]
    "Narration:"
    "You return to the lab as evening sequences the day into a ribbon of accomplishment. The monitors show a calm forecast horizon; the sensor feeds hum steady as breathing. There's a new frame on the wall"
    "now—a stitched charter, signatures looping in different hands. Next to it, a polaroid of the first community planting day."
    show dr_kavir_singh at left:
        zoom 0.7

    dr_kavir_singh "We have the MOU drafted for regional dissemination. The governance model—rotating oversight, codified response, verified restoration targets—it's already being requested as a template."
    show mayor_isla_cortez at right:
        zoom 0.7

    mayor_isla_cortez "I signed it. We all did. We wrote in a clause about cultural memory and ritual. We insisted on community veto in design placements."
    show aria_navarro at center:
        zoom 0.7

    aria_navarro "You wanted a future where decisions weren't made to you but made by you. The charter is a promise—not a fortress, but a framework."
    "Dialogue Exchange — Multi-Turn:"
    hide dr_kavir_singh
    show sora_lin at left:
        zoom 0.7

    sora_lin "I was afraid we'd lose our rituals in the paperwork. But I see the charter includes ceremonial stewardship days and education programs. It names grandparents who remember where the tide crept first."

    aria_navarro "Those stories are data too, Sora. They tell us where the old channels used to run, where seeds once lodged. We built them in."
    hide mayor_isla_cortez
    show mateo_hale at right:
        zoom 0.7

    mateo_hale "And the modules are designed to be removed or adjusted as restoration takes over—no permanence unless it's chosen. That's the compromise I fought for, but I like that my work listens to your roots."

    sora_lin "And I like that the roots have the space to ask for a say."

    mateo_hale "Makes engineering feel less like battle plans."
    "Narration:"
    "The conversations bounce between the practical—supply chains, audit reports—and the human: Elena's market becoming a distribution node for seedlings, Jun Park teaching kids to solder tide sensors, and the rooftop becoming a venue for wedding proposals and council workshops alike. The hybrid approach isn't neat. It's honest. It requires tending."

    menu:
        "Offer to teach a community workshop on tide-data storytelling":
            "You sign up with a pen-scratch that feels like a key turned. The idea of translating graphs into bedtime stories makes your chest loosen in the best way."
        "Say you'll mentor Jun on sensor reliability instead":
            "You set a day aside to be elbows-deep in circuitry with Jun Park. They beam at the chance to learn from you; it's practical and tender and exactly the kind of slow fidelity you need."

    # --- merge ---
    "These small commitments accumulate faster than storms. Each one rearranges priorities gently, reshaping what it means to hold responsibility."
    # [Scene: Restored Quay | Night — Community Ceremony]
    hide aria_navarro
    hide sora_lin
    hide mateo_hale

    scene bg ch12_e67f19_5 at full_bg
    # play music "music_placeholder"  # [Music: Full, warm choir with hand drums — uplifting, concluding]
    "Narration:"
    "On the night the charter is ratified, the town gathers on the quay. Not just the council, but shopkeepers, fishers, kids in rubber boots, artisans, and elders who have watched the tide eat their summers. You stand at the center, feeling each heartbeat like a vote."
    show mayor_isla_cortez at left:
        zoom 0.7

    mayor_isla_cortez "This isn't my victory. It's ours. We put accountability where it matters: in people's hands, in the soil, in checks that can't be erased."
    show elena_navarro at right:
        zoom 0.7

    elena_navarro "You kept your promise, niña. You kept the place where we grow and sell and eat and laugh. That's the only kind of home I've ever trusted."
    show dr_kavir_singh at center:
        zoom 0.7

    dr_kavir_singh "Model implemented. Data and memory—woven."
    hide mayor_isla_cortez
    show mateo_hale at left:
        zoom 0.7

    mateo_hale "We build things that can be undone if they're wrong. We plant things that can be tended. That's the compromise."
    hide elena_navarro
    show sora_lin at right:
        zoom 0.7

    sora_lin "We sing, we plant, we fix. We remember. We decide together."
    "Narration:"
    "Hands pass the lanterns. The seal is pressed into wet plaster, each fingerprint a small legalistic rebellion against the idea that only institutions can hold power. The instruments you once feared would bureaucratize the town are now tools in the people's hands—calibrated, shared, taught."
    hide dr_kavir_singh
    show aria_navarro at center:
        zoom 0.7

    aria_navarro "You had feared that choosing the middle would be a cowardice of will. What you did instead was brave in a different register: you trusted the town to hold the center with you."
    "Dialogue — Closing Multi-Turn:"
    hide mateo_hale
    show jun_park at left:
        zoom 0.7

    jun_park "Look at the projections—recovery curves are real. The shoreline is trending toward stability."

    aria_navarro "Not fixed. Not ever fixed. But steady enough that children can keep learning to fish here without watching their grandparents' houses slip."

    sora_lin "And they'll have stories—because we wrote the stories into the law."
    hide sora_lin
    show mateo_hale at right:
        zoom 0.7

    mateo_hale "And you'll have time—time for work and for the life you choose."
    "Narration:"
    "You look at the faces around you—mates, rivals, allies, kin. Their expressions are complicated, layered with relief, exhaustion, pride, and the cleanest kind of hope. They are not all the same, but they are together. The harbor breathes. Somewhere, a gull calls, sharp, untroubled."
    hide aria_navarro
    hide jun_park
    hide mateo_hale

    scene bg ch12_e67f19_6 at full_bg
    # play music "music_placeholder"  # [Music: Swells into a warm, sustained chord]
    "Narration:"
    "You think of your water-stained notebook tucked in your bag, its pages splayed with numbers and small, messy drawings. You think of Elena's kitchen smell, of Jun Park's solder steam and jokes, of Sora's paint on"
    "your sleeve, Mateo's quiet competence. You have not solved every problem; you have, instead, built a system that learns, corrects, and returns power to the people who live here."
    show aria_navarro at left:
        zoom 0.7

    aria_navarro "I can let some weight be shared. I can commit to both this work and to the soft things—laughter, a steady hand, a garden pot on a rooftop. That is not abandoning duty; it is making it sustainable."
    # play sound "sfx_placeholder"  # [Sound: Distant tide, measured and soft; a communal cheer rises and settles like a benediction]
    hide aria_navarro

    scene bg ch12_e67f19_7 at full_bg
    "Narration:"
    "The town sleeps around you with an easier breathing. Policies will be reviewed and revised; storms will still come. But they will come to a place better prepared to answer—with hands that know the work and laws that keep that knowledge alive. You helped write that promise."
    # play music "music_placeholder"  # [Music: Fades to a single, hopeful piano motif]

    scene bg ch12_e67f19_8 at full_bg

    scene bg ch12_e67f19_9 at full_bg
    "THE END"
    # [GAME END]
    return
