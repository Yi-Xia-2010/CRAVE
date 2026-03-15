label chapter11:

    # [Scene: Quay | Night]

    scene bg ch11_e67f19_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low mechanical drone, the distant slap of waves, the quick staccato of phone notifications]
    # play music "music_placeholder"  # [Music: Driving, urgent strings — a relentless pulse that quickens with every exchange]
    "You stand with the tide-watch heavy and honest in the palm of your hand. The brass is cool; its little hands do nothing to slow the pounding in your chest. Around you everything is in motion"
    "— people, machines, messages — but under the lights the town looks smaller, more fragile, like something you could cup and hold if you only had enough arms."
    "Nyla is there first, breathless from the climb down the quay, tablet in hand, the glow painting her pink hair an electric rose. She shows you a feed: a fisher’s post, a blurred photo of ropes"
    "and nets hauled up with more mud than fish, a comment thread that veers fast from grief to accusation. Someone overlayed the image with the word 'SELL-OUT' in jagged red type."
    "You feel the heat of it as if the letters themselves could burn: your choice to back the compromise is already a public shape that people can aim at."
    show nyla_torres at left:
        zoom 0.7

    nyla_torres "Maya—look. Sensors are showing a drop in biomass near the reconfigured quay. The model didn't forecast this rate. We can trace it back to the way the currents shifted after they put in those revetments."
    show maya_serrin at right:
        zoom 0.7

    maya_serrin "Show me."
    "Nyla's finger scrolls, so quick the numbers blur. A map blooms on her tablet: colored gradients, time-stamped readings, a ghost-line where the current diverted. Her eyes are blazing with a mixture of anger and the precise hunger of someone who finds a flaw and wants to fix it."

    nyla_torres "We can publish it. Put up the raw stream. Let people see what's happening in real time. Transparency will force them to respond."

    maya_serrin "If we publish everything now, the Mayor will say it's sabotage. Elena's investors will point to instability and tighten their grips. The construction stops, the funding freezes."

    nyla_torres "And the fishers go hungry while you wait for someone to remember that 'stability' includes us?"
    "Before you can answer, Aiden Koa's laugh — too short, half-iron, half-hurt — cuts across the cold air. He has the fishing co-op's carrier bag slung over one shoulder; the leather of his jacket looks older"
    "than when you last saw him. He stands a few paces away, hands shoved into patchwork oilskin pockets, the fissure in his expression open and raw."
    show aiden_koa at center:
        zoom 0.7

    aiden_koa "You always said promises matter, Maya. You told Old Man Cala you wouldn't let his stories die to concrete. Now the promises became paper and the paper keeps letting things slide."

    maya_serrin "Aiden—"

    aiden_koa "Maybe I shouldn't be out on the water anymore if the water won't give back. Maybe there's work in the city. Maybe I should leave this before the shore takes everything else."

    maya_serrin "Don't say that. This isn't—this wasn't supposed to be the end. Help me understand what they told you. Help me show them what they missed."
    "Aiden Koa's jaw tightens. He looks at Nyla, then at the rail where fishers usually tie their lines. Behind him, a pair of dockhands argue with an activist filming the scene, their words thrown like planks into the sea."

    menu:
        "Walk over and take Aiden's hand":
            "You close the space, fingers finding the calluses you know. He flinches, then lets his hand rest against yours for a breath — a small, fierce harbor in the storm."
        "Step back and pull up Nyla's data feed":
            "You slide into Nyla's glow. The numbers feel like ballast, cold and irrefutable. Aiden watches you as if your loyalty can be measured in graphs."

    # --- merge ---
    "Continue"
    # [Scene: Corporate Seawall Construction Site | Night — adjacent, under floodlights]
    hide nyla_torres
    hide maya_serrin
    hide aiden_koa

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Clangs of metal, distant engine recoil, murmured orders]
    # play music "music_placeholder"  # [Music: Percussion intensifies, a percussion undercurrent like marching feet]
    "Mayor Jerome Hale stands near the edge of the work zone, folders clutched to his chest. He is practical even in panic — you can see the habit of negotiation in the tilt of his head,"
    "the practiced calm of his voice. But tonight the lines around his eyes have been carved deeper by timelines compressed into threats."
    show mayor_jerome_hale at left:
        zoom 0.7

    mayor_jerome_hale "Maya, we don't have the luxury of a perfect plan. Investors have deadlines; Elena's board won't let go. If we lose this tranche, we lose everything else. The restoration — the ecology work — is on hold 'til funding stabilizes. It's the language they gave me."
    show maya_serrin at right:
        zoom 0.7

    maya_serrin "That's not just budget language, Jerome. 'On hold' is a euphemism for 'maybe forever' in this town. It means habitats won't recover. It means people lose more than money."

    mayor_jerome_hale "I know. I'm not happy about it. But the immediate barrier protects houses. People need roofs tonight."
    "From the cluster under the lights, Dr. Elena Park approaches — poised, precise, trench coat catching the light like a blade. There is tension in her jaw you haven't seen before; her AR specs rest on"
    "the bridge of her nose, half up, half down, like the edge of two worlds. Investor emails creased the corners of her mouth earlier; you can read the pressure in the set of her shoulders."
    show dr_elena_park at center:
        zoom 0.7

    dr_elena_park "Maya. Jerome. I didn't want this to look like cutting corners. We're running on a tighter schedule because the capital round accelerated. Investors demanded faster returns. I pushed back, I pushed—' she cuts off, realigns, then says softer, 'I pushed as far as I could."

    maya_serrin "As far as you could — or as far as your board would allow?"

    dr_elena_park "Boards have their thresholds. I have mine. We can get a stabilization fund in—"
    hide mayor_jerome_hale
    show nyla_torres at left:
        zoom 0.7

    nyla_torres "Unless those 'thresholds' are defined by screenshots and inflated projections. Your stabilizer is their spreadsheet."
    "Dr. Elena Park's eyes flick to Nyla. For a moment they narrow — but there's no villainous sneer. There's the weariness of someone who lives inside proposals and deadlines, the weary arithmetic of trade-offs."

    dr_elena_park "We can carve out a fund for fishers' access. It's not ideal, but it's something. We can also phase restoration — immediate protection now, marsh remediation in the next phase."
    "You sense the room tightening, emotion and stakes compressing together. Activists at the periphery shout into phones, a thread of live video streaming across the shore, tags already trending. A message pings your own phone — the mayor's office reminding you of the public statement for tomorrow."
    hide maya_serrin
    show aiden_koa at right:
        zoom 0.7

    aiden_koa "Phase. Phase this, phase that. While you 'phase' my livelihood into a footnote, people will lose dinners, and kids will forget the taste of fresh salt cod."

    "Maya Serrin (firm, but your chest is a drum)" "Elena, if you set aside a fund, it has to be binding — a trust, escrowed and public — so it's not 'phase' when we need it. It needs oversight by people who live here."

    dr_elena_park "Binding clauses slow down deployment. If the board sees strings, they pull back."
    hide dr_elena_park
    show maya_serrin at center:
        zoom 0.7

    maya_serrin "Then we put oversight into the municipal charter. Citizen oversight. Legal clauses that can’t be rewritten by spreadsheets. If you want our cooperation, you want our consent. Make it enforceable."
    "Mayor Jerome looks at you — an unreadable mix of relief and dread. He is the weathervane between political survival and civic duty."
    hide nyla_torres
    show mayor_jerome_hale at left:
        zoom 0.7

    mayor_jerome_hale "Maya, that will anger investors. It will make contracting longer. I can try—"

    maya_serrin "Try. Make it a condition of our continued support. Tie the funding tranches to verifiable milestones and an oversight board that includes fishers, scientists, and community reps. Put it in municipal code."
    hide aiden_koa
    show nyla_torres at right:
        zoom 0.7

    nyla_torres "We can create the dashboard. We can stream sensors. We can timestamp every alteration to the shore and make it immutable."
    "A murmur ripples through the gathered workers and residents. The idea of a live, public ledger of coastal interventions lights something fierce and hopeful in people's faces. In that single instant, the air changes from accusation to potential action."
    "Dr. Elena Park studies you, then slowly nods. It's not a full concession — the glance toward her team is quick, strategic — but the nod is a promise to negotiate."
    hide maya_serrin
    show dr_elena_park at center:
        zoom 0.7

    dr_elena_park "I can propose an escrow with independent auditors. We'll build in milestones. But I need the timeline loosened by two weeks."
    hide mayor_jerome_hale
    show maya_serrin at left:
        zoom 0.7

    maya_serrin "Two weeks is two weeks of exposure for the shoreline."

    dr_elena_park "And two weeks to make the fund enforceable."
    "You feel the calculus in your bones: delay may bring better accountability, but it also invites investors to yank their support. The arousal in the air spikes — phones ping, a dozen small geomorphic alarm bells ringing."

    menu:
        "Push the Mayor publicly now to demand the escrow clause":
            "Your voice cuts through the crowd. 'We will not let promises be paper.' People lean forward. Jerome's face hardens; the construction foreman looks nervous. Echoes of 'finally' and 'wait' ripple in equal measure."
        "Ask Elena to draft the clause tonight, quietly":
            "You step closer to Elena, lowering your voice. She listens, professional and close. You feel the charged proximity of ally and adversary, and for a breath your knee-jerk mistrust is complicated into something like tactical intimacy."

    # --- merge ---
    "Continue"
    # [Scene: Tide Research Station | Late Night — later, still urgent]
    hide nyla_torres
    hide dr_elena_park
    hide maya_serrin

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft hum of servers, the tinny ping of incoming messages]
    # play music "music_placeholder"  # [Music: A single high violin line — tense but hopeful]
    "Back at the station, Nyla boots up the visualization platform. The data from the quay is already queued: sensor arrays, current models, tidal amplitude variance. You cross-reference the headlines, watch the activist streams, listen to Aiden Koa's low, raw comments about leaving the nets behind."
    show nyla_torres at left:
        zoom 0.7

    nyla_torres "If we publish this feed, we can't take it down. It becomes evidence, and evidence forces action. The town will either rally — or they'll turn on you for not stopping it. But at least it won't be erased."
    "You stare at the cascade of numbers until they resolve into a shape you recognize: a possible accountability mechanism. Your chest is a furnace of resolve. Your throat feels raw, but there is clarity there that sings: this is what representation looks like in practice — messy, ugly, necessary."
    "Your phone buzzes."
    show aiden_koa at right:
        zoom 0.7

    aiden_koa "I don't want to be the person who leaves. But I don't know how to be the person who waits and watches things rot while 'recovery' sits in a ledger."
    show maya_serrin at center:
        zoom 0.7

    maya_serrin "You don't have to decide tonight."

    aiden_koa "Maybe I already started deciding."

    maya_serrin "Then help me decide with me. Not away from this place. With me. With Nyla. With people. We make the oversight now. We force the binding. If we act fast and loudly, Elena can't hide behind investor fear. If we act silently, we buy a small fix and we all pretend we're okay."

    aiden_koa "You make it sound easy."

    maya_serrin "It will be hard. It will fracture things — politics, friendships, reputations. But it's what we asked for when we said 'community-led.'"

    nyla_torres "If you want to keep them here, keep them fed, the fund has to be immediate and visible. I can push the dashboard live. We can timestamp every milestone. We can make it impossible to privatize this story."

    maya_serrin "Do it."

    "Nyla's fingers fly over the keyboard. On the screen a checkbox blinks" "PUBLISH—LIVE."
    "There is a splinter of triumph — the taste of salt and hope — bright and electric against the fear."

    maya_serrin "Either we force the rules to match our hope, or we take the small, quiet money to keep people afloat. I can do both — there are paths — but I need you. I need community muscles. I need your voice in oversight meetings."
    "Aiden Koa looks at you; his expression is not simple. For a second it is unreadable — a complex map of pride, fear, and something like longing."

    aiden_koa "If I stay, I'm staying because I'm convinced you won't let them replace our story with concrete. Convince me."

    maya_serrin "I'll convince you with clauses and court filings if I have to. But first, I will convince you with actions that you can see."
    "You stand on a knife-edge between public confrontation and private compromise, between binding law and the slow burn of community organizing. The adrenaline is a bright instrument in your veins, the night humming like a live wire."
    "People are already assembling — Nyla has the dashboard; activists are coordinating a press burst for the morning; a few fishers are circling, waiting and wary. Dr. Elena Park has retreated to confer with her team,"
    "but she left the offer in the air: an escrow, auditors, milestones — if the timeline can stretch."
    "Your notebook is open on the counter. Your tide-watch has been set beside it; the brass gleams in the station light like a small promise. Your storm-gray eyes scan the page — phrases half-formed, legalistic words"
    "you can shape into leverage. You can push the municipal machinery to bind the deal. You can lead the town to take to the streets and demand enforcement. Or you can broker a quieter fix with"
    "Elena, channeling funds directly to fishers while everyone else argues."
    "You feel the town's heartbeat under your palm: messy, furious, hopeful. The arousal peaks — shouts and pings and the fanfare of mobilization crash together into a single, pointed urgency."
    "This is the moment that will define not only the shoreline but the shape of your ties: political, public, and personal."
    hide nyla_torres
    hide aiden_koa
    hide maya_serrin

    scene bg ch11_e67f19_4 at full_bg
    # play music "music_placeholder"  # [Music: Strings snap high — an urgent, almost triumphant chord]

    menu:
        "Push for binding legal clauses and citizen oversight, using municipal authority.":
            jump chapter13
        "Publicly denounce broken promises and lead a town campaign to demand enforcement.":
            jump chapter15
        "Secretly broker a targeted fund with Elena to restore fishers' access and compensate losses.":
            jump chapter17
    return
