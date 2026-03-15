label chapter13:

    # [Scene: The Beacon | Late Afternoon — the day after the vote]

    scene bg ch12_f99e88_1 at full_bg
    # play music "music_placeholder"  # [Music: Bright, rising piano motif — steady, hopeful]
    # play sound "sfx_placeholder"  # [Sound: Low hum of the building's sensors, the occasional scraping of a chair; outside, gulls call and a distant hammer thumps as volunteers repair a railing.]
    "You walk back into the Beacon with the weight in your pocket now lighter and oddly different — smaller, like a stone set in a pocket you can feel but that doesn't drag. The vote passed:"
    "narrowly, by a margin that tastes sharp and celebratory at once. The town has agreed to a community bond. Funds will go to retrofits, a phased mangrove corridor, and a modest seawall. It's not everything; it's"
    "more than nothing."
    show rosa_kwan at left:
        zoom 0.7

    rosa_kwan "Look at this place. You should've seen the queue at the bakery this morning — people signing pledge forms with one hand and holding cinnamon buns in the other."

    rosa_kwan "You did this, you know. We did."
    "You walk back into the Beacon with the weight in your pocket now lighter and oddly different — smaller, like a stone set in a pocket you can feel but that doesn't drag. The vote passed:"
    "narrowly, by a margin that tastes sharp and celebratory at once. The town has agreed to a community bond. Funds will go to retrofits, a phased mangrove corridor, and a modest seawall. It's not everything; it's"
    "more than nothing."
    "Rosa's cap is bright against her flour-dusted apron. The scent of warm sugar and sea salt presses at the back of your throat like a memory of better mornings. She hands you a paper cup; it"
    "steams in your hands. Her smile is steady, the kind that stitches neighborhoods into neighborhoods."

    menu:
        "Take the cup and drink":
            "You lift the cup to your lips. The coffee is too strong and perfect; for a moment your chest lightens and a laugh slips out of you. Rosa's eyes crinkle with relief."
        "Tuck the cup away and go straight to the whiteboard":
            "You fold the cup into your jacket and move to the whiteboard. The room leans toward your plans; people have questions waiting like small, eager waves."

    # --- merge ---
    "Continue to the planning conversation with Elias 'Eli' Navarro."

    "Elias 'Eli' Navarro" "We should schedule the pilot for the modular foundation next week. Hal cleared his tinker shed; he'll help with the first frame."

    "Elias 'Eli' Navarro" "If we keep materials local and labor cooperative, we keep money flowing in-town."
    show amara_vale at right:
        zoom 0.7

    amara_vale "And the loan committee — Rosa, Miriam, and me — will fast-track applications for the small businesses that need stabilizing grants. We can't let the retrofit money become a lottery."

    "Elias 'Eli' Navarro" "Agreed. And—"

    "Elias 'Eli' Navarro" "—we'll keep the prototype open-source. Anyone can inspect the design, suggest changes. No secrets."
    "Elias 'Eli' Navarro's hands are work-worn, the calluses mapping years of lifting and measuring. He speaks with the quiet precision of someone who trusts calculations but knows how numbers sit inside people's lives. There's a thread"
    "of something softer in his voice when he mentions 'open-source' — not idealism for its own sake, but a literal safety net for the town."
    show harold_hal_finnegan at center:
        zoom 0.7

    harold_hal_finnegan "Remember to build in recall paths. Governance isn't just paper. It's who shows up when the first foundation pops a seam."

    harold_hal_finnegan "We teach the apprentices, we document, and we make sure the knowledge lives here."

    amara_vale "We will. We put training hours into the bond. We teach more than how to hammer; we teach maintenance and monitoring, too."

    harold_hal_finnegan "Good. Passing the bond is one night. Keeping Seabright afloat every season — that's the work."
    "Hal's sweater smells faintly of oil and mended sails. He moves like someone who learned patience in storms. His words settle like a plank tightened across an opening. The bond is victory and beginning both."
    hide rosa_kwan
    show marco_voss at left:
        zoom 0.7

    marco_voss "Congratulations, Amara. A narrow win, but a win."
    "Marco Voss [gives a small, practice smile; his eyes linger with a calculation you can't, and shouldn't, fully read]"
    "Marco Voss's suit is slightly damp at the shoulders from the drizzle outside. He extends a hand in a gesture that should be simple; the air around it has the familiar grit of negotiation. His presence is a reminder: the town's decisions will ripple into the corridors he moves in."

    amara_vale "Marco."

    amara_vale "This space is for the town. If you have an interest in contributing, you come through the committee."

    marco_voss "Of course."

    marco_voss "You'd do well to remember — funding scales outcomes. When people have projects that need speed and scale, we can move."

    amara_vale "We moved tonight."

    marco_voss "Yes. And I can appreciate that. My team will watch the pilot. We'll be quiet."
    "Marco Voss [the word lands oddly — a promise, a warning; his expression is complex]"
    "You notice how the Beacon's light pools around his shoes, how his words sit differently than they might have a year ago. Marco's tone is, as ever, persuasive. You file it under 'watch and verify' rather than trust."
    hide amara_vale
    show rosa_kwan at right:
        zoom 0.7

    rosa_kwan "Enough strategizing. Come on — we have to get these loan forms laminated. The bakery's on the clock."
    "You laugh, and the sound threads into the room like a rope. Hope pulls taut in small, practical things: laminated forms, taught apprentices, the first saplings for a mangrove corridor staked in thanks and stubbornness."
    # [Scene: Old Harbor | Early Evening — site visits]
    hide harold_hal_finnegan
    hide marco_voss
    hide rosa_kwan

    scene bg ch12_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slap of boots on wet cobbles, the soft thrum of a generator, voices calling instructions; gulls wheel against a thinning sky.]
    # play music "music_placeholder"  # [Music: Gentle strings with an ascending motif — patient and tender]
    "You walk the Old Harbor with Elias 'Eli' Navarro at your side, clipboard in hand. The retrofit list is long: shop thresholds raised, electricals elevated, storm doors fitted. Some proprietors lean into the work; others worry"
    "about the cost even with cooperative loans. The air smells of wet tar and frying oil from a nearby stall where someone grills fish for volunteers."

    "Shopkeeper" "The loan helps, but what about when the tide keeps creeping higher? These plates won't hold forever."
    show amara_vale at left:
        zoom 0.7

    amara_vale "We're pairing retrofits with the mangrove phases. The cordon will slow surge and give us time to implement more structural defenses. This is phase one — safety now, strategy for later."

    "Shopkeeper" "We just can't close for a month. My rent — my family's rent — it's counted weekly."

    "Elias 'Eli' Navarro" "We'll schedule work nights and quick shifts. We can stage the retrofits so shops stay open. We've budgeted for temporary bracing. Rosa's cooperative fund will float payroll if needed."
    "Your words measure hope into timetables. Some owners relax; others keep faces drawn. Not all wounds heal the same way. You file their worried faces into the ledger of what adaptation must include: not merely structures, but livelihoods."
    show old_man_tor at right:
        zoom 0.7

    old_man_tor "When I was a boy, we braided line from sea-silk and called the harbor ours. We didn't think to move the sea; we learned the songs to go with it. Now you weave another kind of rope."

    amara_vale "What song should we sing, Tor?"

    old_man_tor "One that remembers which houses to carry forward and which to bless for their service. You don't let go without ceremony."
    "He hands you a small carved buoy — worn wood, a painted blue stripe rubbed thin. You cradle it, feeling pores and old paint. It's a talisman, or memory, or both. The harbor's history presses itself"
    "into the present, not as myth but as a ledger of choices that will be counted in salt years."

    menu:
        "Tie the buoy to your notebook":
            "You loop the cord around your field notebook and tuck it into your bag. It feels oddly steady there, as if the town has pressed its confidence into your pocket."
        "Return it to Tor and ask for a blessing":
            "You hand the buoy back. Tor's fingers close around it like a benediction; his smile deepens and some private light flickers in his eyes."

    # --- merge ---
    "Continue walking the harbor with Elias 'Eli' Navarro."
    "You move on to a corner where scaffolding frames a shopfront. Volunteers hand up boards; a painter coats a newly elevated sill. Each raised step, each tightened bolt, is a small promise against a large uncertainty. The bond money hums through these tiny actions like new current."
    show rosa_kwan at center:
        zoom 0.7

    rosa_kwan "We've routed the first cooperative loans! Two bakeries, a bait shop, Old Man Jenkins' repair. They're nervous, but they're onboard."

    amara_vale "Thank Rosa for her roster. We'll need more — we must be deliberate about who qualifies for emergency bridge funding."

    rosa_kwan "Deliberate, but fast. People have to eat while we do the things that keep the sea from eating them."
    "The evening is a patchwork of practical kindness. Where money meets need imperfectly, people mend with one another."
    # [Scene: Modular Foundation Workshop | Night — first pilot assembly]
    hide amara_vale
    hide old_man_tor
    hide rosa_kwan

    scene bg ch12_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Metal clinks, the hiss of a heat gun, Hal's soft humming. Outside, waves lap with a persistent, distant rhythm.]
    # play music "music_placeholder"  # [Music: Warm cello underpinning with a hopeful, ascending counterpoint]
    "The pilot assembly feels reverent and practical all at once. A crowd has gathered: volunteers, curious neighbors, a few skeptical council members, and the camera of a local journalist blinking red. The modular pieces fit together like a mechanical promise."

    "Elias 'Eli' Navarro" "We test for buoyancy, stress, and real-world settling. Hal, will you run the first load test?"
    show harold_hal_finnegan at left:
        zoom 0.7

    harold_hal_finnegan "Set her up. We'll watch for micro-stress. The model's conservative; conservative survives."
    "You watch Elias 'Eli' Navarro socket a connector into place with the precision of someone who loves the logic of how things hold. His shoulders soften when he looks up at you — not spoken, just"
    "a brief shift, an offering of trust. There's a current between you that is more work than romance and more care than mere friendship. It grounds you."

    "Elias 'Eli' Navarro" "If we get the geometry right, we can reduce material costs by twenty percent. That means more retrofits for the same bond."
    show amara_vale at right:
        zoom 0.7

    amara_vale "And if the community learns the assembly, then repair is local. That's the point: money stays in the town and knowledge stays in the town."

    "Elias 'Eli' Navarro" "Exactly."

    "Elias 'Eli' Navarro" "I don't want to promise more than we can do. But — I'm proud of what we built."
    "Pride is a low and rooted thing in Elias 'Eli' Navarro. It looks like callused palms and late nights measuring tolerances. You feel a flare of warmth hearing him speak — for the town and, quietly, for the collaboration between you."
    show marco_voss at center:
        zoom 0.7

    marco_voss "Impressive work."

    marco_voss "If this scales, it's a template. Investors will lounge waiting to fund the next phase..."

    amara_vale "This is a cooperative design. If investors want to help, they come through the town's structures."

    marco_voss "And the town will decide its own terms. Of course. I'm happy to wait."
    "His tone is warmer than it was in the Beacon, but the edge hasn't disappeared. He watches the pieces click together and nods with a calculation that you accept without surrender. You're not naive; you're hopeful and watchful."

    harold_hal_finnegan "Okay — HER weight, please."
    "Sound: The gauge ticks upward; a flurry of quiet conversation. Then, a collective exhale as the load holds."
    "Elias 'Eli' Navarro: (exhales) 'Good. Now for settlement testing. We'll simulate a storm cycle in the sensors.'"
    "You stand close enough to feel the workshop's warmth on your cheek. Outside, the sea murmurs, patient and indifferent. Inside, people who love this place have come together to make a difference that is tangible and immediate."
    hide harold_hal_finnegan
    show rosa_kwan at left:
        zoom 0.7

    rosa_kwan "Should I prep a banner for the launch? 'Cooperative Harbor' — sounds good, doesn't it?"

    amara_vale "It does. It sounds like work and a promise."

    rosa_kwan "Exactly. Also — pastry. Always pastry at launches."
    "The room fills with a small, eager comedy of competence and tenderness. The pilot will not save everything. The seawall is modest. Projects will stall; some shops will struggle despite loans. But here, tonight, you hold a prototype that translates community will into bolts and beams."

    menu:
        "Stand at the workbench and help tighten bolts":
            "You pick up a ratchet and find the rhythm of the work. Each turn feels like a sentence in a long conversation with the town."
        "Step back and take notes for the community report":
            "You open your field notebook and start logging details: torque, names of volunteers, concerns raised. Your notes feel like maps for others to follow."

    # --- merge ---
    "Continue with Elias 'Eli' Navarro's quiet moment."

    "Elias 'Eli' Navarro" "We did something right. Not everything — not perfect — but right."

    "Elias 'Eli' Navarro" "I'm glad you're here for it."

    amara_vale "Me too."
    "There is a pause that is not a decision but a recognition of shared labor. It will need tending like everything else. You tuck the moment away with the buoy and the laminated forms and Rosa's steady grin."
    "Outside, the tide creeps up with quiet patience. Inside the workshop, a small gauge blinks green. The bond money hums into action: adhesives for a seawall, pallets of saplings for a mangrove corridor, and a ledger"
    "of cooperative loans printed and waiting. There will be setbacks — stalled permits, balky suppliers, a shop that needs an extra month of assistance — but there is also motion, and the motion is in the"
    "town's hands."
    "You close your notebook and look at the assembled community: Hal arranging tools, Rosa sketching a banner, Elias 'Eli' Navarro by the prototype with grease on his knuckles, Old Man Tor smiling with his carved buoy"
    "in his lap, Marco Voss standing at the edge of the light like a storm-cloud that may one day give good rain. The Beacon's whiteboards are full. The harbor's docks are being raised. The first saplings"
    "are staked."
    "The future is not neat. It is not safe. It is, finally, collaborative."
    hide amara_vale
    hide marco_voss
    hide rosa_kwan

    scene bg ch12_f99e88_4 at full_bg
    # play music "music_placeholder"  # [Music: A sustained hopeful chord — rising, then holding]

    scene bg ch12_f99e88_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter17
    return
