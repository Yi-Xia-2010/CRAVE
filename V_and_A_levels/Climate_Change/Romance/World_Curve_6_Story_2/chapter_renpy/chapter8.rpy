label chapter8:

    # [Scene: Corporate Seawall Construction Site | Late Afternoon — Incoming Tide]

    scene bg ch8_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Metallic groan of winches, a far-off engine cough, the constant white hiss of surf.]
    # play music "music_placeholder"  # [Music: Rapid, driving strings — urgent, forward-motion]
    "You stand with your parka hood down, spray beading on the olive fabric and trailing salt down the sleeve. The new concrete ribs sit like a stern face to the sea; where they meet the restored"
    "marshes, the water folds differently now — less blunt, more measured. In the trials the crew ran at dawn, overtopping numbers plummeted. The telemetry Nyla sent you is already framed on the Tide Research Station’s crushed-metal"
    "screen in your head: lower peak flows, damped energy, marsh biomass taking the first punch and holding."
    "Relief hits like a warm current, immediate and electric. This is what you argued for in the grant packets and neighborhood kitchens: living systems to soften the blow, steel and poured concrete to buy time where"
    "nature can’t move fast enough. The hybrid is doing what it promised. You let yourself feel that for a breath."
    "But the tide is the tide. It rearranges itself around whatever obstacle you place in its path."

    scene bg ch8_6b08b4_2 at full_bg
    # play music "music_placeholder"  # [Music: Percussive stabs syncopate with your heartbeat — fast, contained]
    "You watch a line of fishers pulling a net toward the quay. They bring a thin, strange catch today — shrimps where cod once hovered. One of them, Mateo, a neighbor from the slip who taught"
    "you to heave ropes when you were ten, curses under his breath. He lifts a hand and points where the water curls behind a fresh concrete leg. The current has shifted; the feeding grounds have slid"
    "like a seam."
    "You step closer, the smell of diesel and seaweed sharp in the air."

    "Mateo" "Maya! You see this? We worked the same line for years. Now it’s… empty. Where's the money you promised for re-stocking if this happens?"
    show maya_serrin at left:
        zoom 0.7

    maya_serrin "We modeled for overall energy reduction, Mateo. But I know these places have their own rhythms. Nyla’s got new transects going —"

    "Mateo" "Your models don't pay for nets. They don't put fish back in the net. Elena's concrete's fine for houses. What about our boats?"
    "Aiden Koa appears behind him, sleeves rolled, jaw set. He moves with a fisherman’s economy of motion, and his voice is low enough that he expects you to hear the unspoken between the sentences."
    show aiden_koa at right:
        zoom 0.7

    aiden_koa "It’s not just nets. The quay's reroute cut our path. Small boats can't make the turn at dusk now. Supplies get held up. Folks lose market slots. We were told we'd be consulted."
    "You feel the pull between the facts you can show and the lives that map onto those facts. You have contingency language for shifts like this. You also have every instinct to fix things fast — guilt makes your hands itch."
    show nyla_torres at center:
        zoom 0.7

    nyla_torres "I ran the current models again. The shift is predictable where the anchors went in. We can adjust anchor positions by half a cable length to restore eddies near the inner channel. But it adds three days of deck time and a permit amendment."

    maya_serrin "Show me the adjustment."
    "Nyla swipes, and a ribbon of color overlays the bay. Where the concrete leg stands, a new eddy of slower water blooms if anchors move a short distance. The solution is small and surgical. It costs time. It also costs political capital."

    menu:
        "Move in and speak for the fishers, right now":
            "You step between Mateo and the foreman, voice loud, immediate—calling the shift to attention, forcing a conversation about anchor repositioning before the cranes move on."
        "Record the exchange, take the data to Nyla and file it carefully":
            "You lift your hand to record Mateo’s haul and the curled current on your tablet, quick and precise; you file it to Nyla with tags so it can't be all smoothed over in a later report."

    # --- merge ---
    "Scene continues"
    hide maya_serrin
    hide aiden_koa
    hide nyla_torres

    scene bg ch8_6b08b4_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A shout, then the clatter of someone stumbling; a scraping, metallic scream as a small boat tugs against something it shouldn't.]
    "From the quay a commotion spikes like a match. You run — the site’s perimeter is a jumble of safety cones and stomped mud. A neighbor’s skiff, the Mara, drifts oddly near a freshly set anchor"
    "chain; the chain, an unseen appendage lowered to secure a temporary mooring, snags a runners’ line. The propeller shudders. The boat veers and slams against the quay. A crate slides; a fisherman lashes out and twists"
    "his ankle under falling gear."
    "It happens so fast your head rings."
    # play sound "sfx_placeholder"  # [Sound: "Mateo! Get back!"] someone shouts. The air tastes of sea and adrenaline. The fisherman on the skiff, a younger man named Luis, is pale, cradling his twisted leg. Blood beads dark at the edge of a torn boot. He clenches the rail, face pinched, but eyes wide with something you don’t want to see: a recognition that a day's catch — a week's wage — might be gone.
    show maya_serrin at left:
        zoom 0.7

    maya_serrin "Luis. Look at me. Breathe. Nyla, towels. Someone call this in."
    show nyla_torres at right:
        zoom 0.7

    nyla_torres "Medic's on the way. Aiden—can you hold the skiff?"
    show aiden_koa at center:
        zoom 0.7

    aiden_koa "I've got it."

    aiden_koa "This could've been avoided. Temporary anchors should have been run by us. We flagged the inner current. We said—"

    maya_serrin "We did. We moved on the big risks. Small lines like this—"

    aiden_koa "Small lines are our lives, Maya. They're not small."
    "Your chest tightens. The boardwalk and the cracked plaster of your childhood home come to you like a slide show. You remember the night the water took your mother's garden and the guilt that has made"
    "you move faster, impose more, promise louder. Aiden Koa knows that history in the way only someone who grew up here from the other side of your family's fence might. He holds that history like evidence."
    # [Scene: Quay | Dusk]
    hide maya_serrin
    hide nyla_torres
    hide aiden_koa

    scene bg ch8_6b08b4_4 at full_bg
    # play music "music_placeholder"  # [Music: Quick oboe and strings — anxiety peaked]
    "Mayor Jerome Hale arrives, face creased in a different worry: political exposure. He scans the injured man, then the cameras — a local activist already filming on a holo-feed. The activists’ posts have a crisp line"
    "of captions: CORPORATE TAKEOVER, the concrete a backdrop for their outrage. The investors' logo glows like a brand on every hardhat."
    show mayor_jerome_hale at left:
        zoom 0.7

    mayor_jerome_hale "Maya. This is going to be on the feed in thirty seconds. We need to say something that calms this."
    show maya_serrin at right:
        zoom 0.7

    maya_serrin "We have immediate first aid going. Nyla's got data that shows how to minimize the current shifts. If we reposition anchors, it mitigates these snags."

    mayor_jerome_hale "That’s not the whole story. The investors are calling. Elena's board wants visible returns — the Mayor's office wants fewer headlines. They may push for expansion to make it look decisive. The next move they make will define the narrative."
    "Dr. Elena Park steps out of the construction haze, AR specs lifted to her brow, palms clean despite the day's work. She walks with the composure of someone used to smoothing crises with memos and schedules."
    show dr_elena_park at center:
        zoom 0.7

    dr_elena_park "I am sorry about the injury. We'll cover medical. But months of safety are worth an occasional setback when the alternative is loss of homes. We need a plan to prevent further accidents, but I won't let fear undo the protection we've built."
    "You watch Dr. Elena Park catalog the scene, see the calculus run behind her eyes. She means, in her way, the town's survival. The way she speaks feels like a scalpel — efficient, intent on outcomes."
    "Your empathy pulls you toward her argument: these structures stop the sea, and the sea kills. But your loyalties pull you toward the quay and the fishermen whose boats scrape these new edges."
    # [Dialogue — Multi-Turn]

    maya_serrin "Elena, I need binding operational limits on deployment — no unilateral anchor placements around the inner channel. Consult the co-op before shifting moorings."

    dr_elena_park "Binding how, Maya? The firm operates under a contract set with the Mayor and investors. I can negotiate stricter monitoring and a rapid-response anchor team, but my hands are tied by timelines."

    maya_serrin "Then untie them. Make them part of the contract. Legally binding environmental monitoring and fishing-lane protections. Otherwise we trade one emergency for another."

    dr_elena_park "Contracts are brittle when investors demand returns. I can push for monitoring and an oversight clause, but comprehensive legal protections slow progress. If this delays completion, political backers pull funding."

    maya_serrin "We can't let funding be the lever that silences livelihoods.' (you lean forward, voice harder) 'If the town is protected but the town's people can't fish, we haven't protected Saltwood's future. We need guarantees."

    dr_elena_park "I'll try. But understand—I don't want to be the engineer who watched funds walk away and then had to explain why the wall wasn't finished."

    mayor_jerome_hale "And I don't want to be the mayor who lost a grant because we picked fights."
    "Aiden Koa, standing a step off, folds his arms as though to keep himself whole. He watches you and Dr. Elena Park like a jury watches a witness. His expression is a map: hurt, mistrust, a"
    "tougher edge that was not there before. You want to reach out and smooth it. You also know your voice has to be the harbor between competing storms."

    menu:
        "Step toward Aiden and ask him to help mediate with Mateo privately":
            "You move to Aiden, lower your voice. 'Help me hold them while I talk to Elena,' you say. He hesitates, then nods, hands rough and ready."
        "Stay with Elena and push legal language now, even if it upsets Aiden":
            "You turn back to Elena and list clauses you need in a binding agreement. Aiden watches, jaw tight. He doesn't speak. You feel the gulf widen."

    # --- merge ---
    "Scene continues"
    # [Scene: Tide Research Station | Night — After the Quay Incident]
    hide mayor_jerome_hale
    hide maya_serrin
    hide dr_elena_park

    scene bg ch8_6b08b4_5 at full_bg
    # play music "music_placeholder"  # [Music: High strings, rapid pulsing — climaxing urgency]

    "Back in the station, the advisory board’s virtual feed pings into a dozen panes. The activists' clip of the skiff slamming has already propagated. Comments rage. Investors ping your assistant with terse requests" "Accelerate. Show a plan to stop disruption. Expand and lock the channel where necessary.' Dr. Elena Park has a private channel that flickers with incoming demands: 'Quarterly ROI visibility. Reduce negative press. Increase visible progress."
    "Nyla sets beside you, eyes raw from a long day but focused."
    show nyla_torres at left:
        zoom 0.7

    nyla_torres "They want more visible progress. That usually means expanding the concrete into areas we said we'd leave for marsh migration."
    show maya_serrin at right:
        zoom 0.7

    maya_serrin "If we expand, we secure more properties, yes. But we deepen ecological impact and push currents further. More people get immediate security; more fishermen get priced out of practical access."

    nyla_torres "Also: Mayor Hale called. He said 'political fallout.' He asked if you can 'deliver a statement' that shows control."
    "You hold the tide-watch like a tiny anchor against the swirl of demands. Your throat is dry; hope — stubborn as seagrass — keeps you moving. Your job has always been to translate ocean physics into human policy. Right now, translation is political liturgy."
    "Your inbox bloats with two sets of voices: one from Dr. Elena Park's investors — crisp, impatient; the other from community chats — raw, immediate, grieving small losses that models flatten into numbers."

    maya_serrin "We need governance not just engineering. Enforceable protections, monitoring, penalties for unilateral deployment. We can make an oversight clause and a rapid-response mitigation fund."
    show dr_elena_park at center:
        zoom 0.7

    dr_elena_park "That slows construction. It bleeds the schedule. Investors will push back hard."

    maya_serrin "And if they pull funding, we stop. Or we get strict limits and keep the hybrid—and the community engaged and safe. It’s a different path, but it holds more people in the solution."

    dr_elena_park "I will talk to the investors tonight. I can't promise they'll accept a binding clause, but I will take it to them with the data. Nyla—your transects? Deliver the evidence that anchor tweaks mitigate impact."

    nyla_torres "Already uploading. You can have it in ten."
    # play sound "sfx_placeholder"  # [Sound: A different ping — a live feed from the activists with a local lawyer on line; they demand transparency and an immediate moratorium on anchor deployment until a hearing.]
    hide nyla_torres
    show mayor_jerome_hale at left:
        zoom 0.7

    mayor_jerome_hale "We need to avoid a spectacle. If it goes to a public showdown, we lose control. Loss of control means loss of funding or votes."
    "You think of the injured fisherman sleeping in a quiet cot at the clinic, of the fishermen who have been muttering about next week's market stalls. You think of Aiden Koa's hard face. You think of"
    "Dr. Elena Park's earnestness and the pressure in her eyes when she talks about showing a model that other towns can copy."
    "Your options fan out like current lines on Nyla's map: each course bends the water differently, each leaves a wake."
    "Your heart jumps. The urgency spikes — the feeds, the injury, the investors' calls, the activists filming, the Mayor's tone of political desperation — all of it squeezes time until decisions feel like avalanches. Yet under"
    "the crush, there is progress: the hybrid has bought days and lives; the marsh shows green shoots where before there was only mud. The good is a fragile, furious thing you must protect."
    hide maya_serrin
    hide dr_elena_park
    hide mayor_jerome_hale

    scene bg ch8_6b08b4_6 at full_bg
    # play music "music_placeholder"  # [Music: Crescendo — drums and strings in full, very high intensity]
    "You inhale and the decision point opens like a channel you must navigate."

    menu:
        "Pressure Elena’s firm for legally binding protections for fishing lanes and environmental monitoring.":
            jump chapter9
        "Authorize expanded engineered extensions to secure more properties quickly.":
            jump chapter18
        "Publicly expose investor pressure and call for transparency to rein in corporate timelines.":
            jump chapter12
    return
