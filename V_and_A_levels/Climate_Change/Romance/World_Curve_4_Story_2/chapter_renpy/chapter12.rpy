label chapter12:

    # [Scene: Floodplain Neighborhood (Lower Quay) | Dawn]

    scene bg ch12_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant sirens, the constant slap of water against stilts, a diesel generator kicking to life]
    # play music "music_placeholder"  # [Music: Fractured strings, rapid staccato—urgent]
    "You wake to the smell of salt and wet wood the way some people wake to smoke. The rooftop decision from the hub is still warm in your chest — the authorization for micro-projects that you"
    "insisted must be led from within the neighborhoods. You told the council 'no' to signing away oversight; you told the city 'yes' to small, reversible things that people could manage themselves. The paper in your satchel"
    "is damp from your own hand."
    "You step barefoot onto the raised threshold Jonah built last summer and feel the tremor underfoot: pumps humming, gulls shrieking, neighbors already on their feet. You can hear Elias before you see him—his laughter, thin and"
    "high, trying to steady a group of fishers as they untangle a new kelp nursery frame on a low barge. Asha moves through the crowd like a blade, issuing instructions, folding rage into practicality."
    "The air is raw. The day smells of algae and fuel and something else you do not name yet: the metallic tang of fear."
    show jonah_mek at left:
        zoom 0.7

    jonah_mek "We lost two of the old boards in the east lane overnight. Thresholds are holding, but not for long if the tide comes hot."
    show maya_soren at right:
        zoom 0.7

    maya_soren "Then we shore the east lane first. Jonas, you take a team with the cross-bracing. Rosa's crew can patch the nursery supports."
    "Jonah gives a half-smile that's more a grunt. 'You and I will be up on the boardwalk by noon. We'll meet Elias at the slip. Asha says the pumps are ready.'"
    show asha_reed at center:
        zoom 0.7

    asha_reed "Pumps and people. No technological panacea—just human muscle and tech we can lift together.' (She meets your eye; her expression is complex, everything honest and withheld at once.) 'We start with micro, Maya. We can't fix the bay in a season, but we can make tonight survivable."
    "Your internal tally lists out the things you fear: a surge bigger than modeled, a pump that fails, a neighborhood memory washed away. You also count the small, stubborn things that keep you moving: Jonah's hands, Elias's grin, Asha's stubborn oath to keep decisions local. They are fragile anchors."

    menu:
        "Walk the east lane with Jonah":
            "You shoulder a tool bag and move into the alleys at Jonah's pace, boots sloshing, sweat cold against the morning air. Every stoop you pass holds a framed photograph or seed packet flapping in plastic—little proofs you're fighting for."
        "Head to the slip with Elias":
            "You cut across toward the water, where Elias and the fishers wrestle kelp frames. Salt sprays your face; his eyes find yours and something unreadable flickers—concern, calculation, a plea."

    # --- merge ---
    "Proceed to Kelp Nursery Barge | Mid-Morning"
    # [Scene: Kelp Nursery Barge | Mid-Morning]
    hide jonah_mek
    hide maya_soren
    hide asha_reed

    scene bg ch12_6b08b4_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Ropes creaking, shouted counting, the slap of terraced waves]
    # play music "music_placeholder"  # [Music: Pulsing low drums—a heartbeat sped up]
    "Elias is all hands and lightness, but today the lightness frays at the edges. He hauls a crate of inoculated lines up to the deck, salt stinging his neck."
    show elias_voss at left:
        zoom 0.7

    elias_voss "These frames are modular—if one fails, we lift and replant. We can scale it with the tides.' (He grins, but it doesn't reach the trembling at the base of his throat.) 'We got the seed stock from three fishers — distributed risk."
    show maya_soren at right:
        zoom 0.7

    maya_soren "Distributed risk is good. Does the protocol include a rapid-evac plan if the moorings let go?"

    elias_voss "Yes. Two motor skiffs on standby, lines with emergency floats, a quick-cut system. We practiced last night.' (He searches your face.) 'You signed off because it felt right. Do you still—"

    maya_soren "I signed because it felt necessary.' (You stop yourself. The difference between right and necessary has been the marrow of decisions all week.) 'We keep monitoring. We log everything publicly."
    "Elias swallows. 'Public monitoring,' he repeats. 'Okay. And—' He hesitates, hands in his pockets. 'If this helps the shorelines even a little, we'll have bought places breathing room.'"
    "You nod, but your mouth tastes like iron. Kelp will help, yes, but small-scale restoration can't hold against a full-on meteorological assault. The knowledge hits you with the bluntness of salt: triumphs will be small and costly."
    "Asha arrives at the barge with her leather notebook open, rain already freckling the pages."
    show asha_reed at center:
        zoom 0.7

    asha_reed "Don't romanticize it. Kelp isn't a miracle. It's a buffer. It is people who will decide if buffers become policy or profit. Make sure community quotas stay in the ledger."

    elias_voss "And you—what are you going to do?"

    asha_reed "I'll teach the crews record-keeping, voting rotation, maintenance shifts. If the kelp gets harvested, it goes back to the neighborhood first.' (There is a fierceness undercutting her usual shadow.) 'We hold the governance. That is the protection."
    "You watch them circle each other's strengths—engineer, activist, organizer—each braced against the coming weather."
    # [Scene: Community Workshop | Noon]
    hide elias_voss
    hide maya_soren
    hide asha_reed

    scene bg ch12_6b08b4_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Hammers, raised voices giving measurements, fingers snapping over knots]
    # play music "music_placeholder"  # [Music: Tachycardic strings, almost overwhelming]
    "Jonah cocks his head and offers you a plan rendered in quick gestures—saw marks, bracket placements, a map of which houses get thresholds first."
    show jonah_mek at left:
        zoom 0.7

    jonah_mek "We move the elders, then the kids. Thresholds at doorways, crossbracing under the porches. We rotate teams so no one collapses on the third hour.' (He looks at you dead-on.) 'You still with us, Maya?"
    "You feel the weight of the room tilt toward you, as if your continued presence legitimizes the makeshift army of hands."
    show maya_soren at right:
        zoom 0.7

    maya_soren "I'm here.' (The words are small and not enough. They echo.) 'We prioritize access routes to the pumps and the nursery—if pumps go, the nursery dies, then the docks."
    "Asha steps into the center and raises her voice so everyone hears."
    show asha_reed at center:
        zoom 0.7

    asha_reed "Listen! We are not handing our fate to another boardroom. These micro-projects mean we hold the line together. If something breaks, we replace it together. If someone needs shelter, we take them in. We document—all of it. No one profits off this.' (Her tone hardens and softens at once.) 'This is our work."

    "A woman toward the back—Rosa's niece—calls out, voice thin with urgency" "What about the pump at Lark's Bend? It sputtered this morning!"
    "Jonah slams his hand onto the table. 'We swap filters, reroute power. Maya, can you authorize the extra fuel from the hub cache? We'll need two-hour runs.'"
    "You feel a hotness in your throat. The hub cache is finite; sending more fuel means pulling another resource away from another neighborhood. The calculus is cruel."

    maya_soren "Authorize it. Send the log. We'll recover costs with community labor credits and a ledger.' (You add bureaucracy into grit.) 'But tell Rosa we need her seed-keepers to shift to pump maintenance rotation."
    "Asha's eyes flick to you—unreadable—and then she nods. The nod is a pact tempered by skepticism."

    menu:
        "Stay to fix the Lark's Bend pump":
            "You hand Jonah the authorization stamp. Your hands are steady with tools and with decisions; you crawl under the pump with grease on your knuckles and listen to the metal complain. It feels like repairing something larger than itself."
        "Go to the council to notify of real-time needs":
            "You grab your tablet and run toward the council line, your breath sharp. The city staff on duty argue about allocation thresholds; you force the log in front of them and watch their faces shift from policy to people."

    # --- merge ---
    "Proceed to Slip — Tide Coming In | Late Afternoon"
    # [Scene: Slip — Tide Coming In | Late Afternoon]
    hide jonah_mek
    hide maya_soren
    hide asha_reed

    scene bg ch12_6b08b4_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The bay speaks in low, building roars; the barge creaks; a pump's whine jumps into a stutter]
    # play music "music_placeholder"  # [Music: A single, relentless percussion; tempo increases toward collapse]
    "You stand at the slip as the first real surge of the day arrives: a wall of water that pushes and rolls and tests the moorings. The micro-projects you've ignited feel suddenly microscopic."
    "Elias Voss: (shouting) 'Now! Lock the floats! Tie the cross-lines! Cut if we have to!' He moves like a man who has always trusted his hands to do the talking—quick, certain—but his hands tremble."
    "Asha Reed's calls are clipped and precise, an emblem of control wrapped around a beating heart. 'Evacuate the low bench now—move them up—move them up!' She points toward the raised walkways. A small child clutches a battered stuffed seal; a woman coughs saltwater out of her lungs and keeps hammering."
    "Jonah Mek: (shouting) 'Threshold teams, now! If the east lane gives, the pumps go under!' He slams his shoulder against a plank, levered effort to hold a brace in place. Sweat tracks under the sawdust on his cheek."
    "The pumps stutter. For a heartbeat—one stretched, elastic second—the world stands on the edge of a ledger entry: failure or not."
    "Your internal monologue is a litany: what will be lost, what will be kept, which names you will carry away. The city is a ledger and a heart—you keep both, as you can."
    "A pump shudders and clicks and then stops. A chorus of curses rises. The diesel backup sputters and dies in an instant that feels like a verdict."
    "Panic unfurls, immediate and white-hot. People shout. Children scream. Asha scrambles, organizing human chains—buckets, buckets for bailing, lines for pulling people up. Elias dives into the spray without hesitation, leather cord whipping, the barge's edge heaving."
    "Maya Soren: (to Elias, breathless) 'Can you get to the emergency floats? Cut the frames and tow them inboard—reduce drag!'"
    "Elias Voss: (shouting back) 'I can—but we need hands on the cleats! Jonah—now!'"
    show jonah_mek at left:
        zoom 0.7

    jonah_mek "Got them. Maya, hold the line!' He grins at you like a man making a joke at the bottom of a pit. 'You always did like being in the middle."
    "Asha Reed: (to a cluster of volunteers) 'Form a human chain to the pump. Pass buckets. Anchor the elders. If we lose the nursery, at least we hold the homes.'"
    "But the surge keeps coming, harder than the models predicted, as if the bay itself is angrier than your maps allowed. The kelp lines strain; one snaps with a sound like a gunshot. A frame lists. Someone curses, then another voice wails. The human chain falters but regains."
    "Your heart hammers against your ribs, a drumline. There is no quiet resolution, only compressed, brutal choices made in the inches between waves."
    "Suddenly, a panel at Lark's Bend gives way—the threshold Jonah reinforced tears loose like tissue. Water slides into a house like a living thing with teeth. A child's cry slices the air. You move before thought; the reflex of leadership is muscle memory now."
    show maya_soren at right:
        zoom 0.7

    maya_soren "Two to the back stairs, four to the porch, get blankets—now!"
    "Elias Voss, soaked and small in the wash, returns with a skiff half-full of people. Asha Reed, hands raw, counts off names in the floodlight. Jonah scrambles with a makeshift brace under a porch, grunting, face set."
    "Some doors you hold. Some you cannot. The micro-projects are doing their work—thresholds slow the water, the nursery frames broke but dragged less detritus to the docks, pumps kept some places dry—but the cost is carved into wet wood and into faces."
    hide jonah_mek
    hide maya_soren

    scene bg ch12_6b08b4_5 at full_bg
    # play music "music_placeholder"  # [Music: Peaks, then a descending minor chord—intensity flares and then condenses]
    "You think of your mother's silver band against your skin, the initials rubbed almost smooth. You promised yourself you would find a way to protect what had been lost. Now that promise is a rope you are clinging to while the bay tries to pull you down."

    "Elias finds you in the swirl, eyes rimmed red. He grabs your coat and says, without waiting for permission" "We held the east lane. Not all of it, but enough to move people. Your plan—your micro-projects—they saved homes today."
    "You try to accept the compliment and taste ash. The word 'saved' tastes unfinished. You see the boardwalk with its new scars, the kelp torn, and the faces of people who will wake tomorrow to repair"
    "and to mourn and to keep living. There's no triumph that doesn't hold a wound."
    "Asha comes up beside you, breathless. She looks at the horizon where the water still rolls and at the neighbors bandaging a child's arm."
    "Asha Reed: (quietly) 'You did it your way, Maya. Not perfect. Not whole. But yours.' (Her gaze is unreadable in that same complex way — admiration braided with accusation.) 'That's something.'"
    "You let the something sit. It is both small and enormous. You are tired to the marrow and thrumming with adrenaline. The micro-projects worked where they could. People, not institutions, kept the night's worst from becoming its absolute worst. But the bay is still hungry."
    # [Scene: Aftermath — Dusk]

    scene bg ch12_6b08b4_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low conversations, the soft weeping of a child, the steady tapping of someone mending a board]
    # play music "music_placeholder"  # [Music: Low, aching cello, a slow exhale]
    "The emergency lights burn in the makeshift shelter as neighbors stitch up wounds and tally losses. The kelp nursery is a tangle; the barge lists but floats. Thresholds are patched enough to keep out the next"
    "ripple; pumps are queued for maintenance. The ledger is a long, handwritten list of labor hours and supplies borrowed from the hub."
    "You sit on a crate, soaking through your jacket, and watch as Elias and Asha argue quietly over logs. Their voices are low, intimate, a different kind of tension: not the raw scramble of crisis, but the threading of policy into practice."
    show elias_voss at left:
        zoom 0.7

    elias_voss "If we formalize the nursery's yield, we can fund more frames—pay for nets and floats."
    show asha_reed at right:
        zoom 0.7

    asha_reed "We formalize it only if the community keeps control. No private contracts siphoning harvest. No strings.' (She taps the notebook with a callused finger.) 'We teach them to govern it."

    elias_voss "We can build a cooperative model. Technical oversight from me, governance from you—"
    "Asha Reed: (interrupting) '—and the people in the middle. That's the point.' (She looks at you.)"
    show maya_soren at center:
        zoom 0.7

    maya_soren "Then that's the model. Cooperative, community-led, transparent accounting.' (The words are decisive but soft. There's a fatigue there that has nothing to do with sleep.) 'We do not hand the governance to outside developers. We hold it here."
    "They both look at you—Elias with something like yearning, Asha with something like wary respect. It is a fragile alignment, built on the night's exhausted truths."
    "Jonah comes over and places a wrapped bundle of mended tools in your lap. 'For when the tide comes back,' he says simply. His grin is tired but whole."
    "You fold your hands around the bundle. It is a small ceremony."
    "And in that cramped, mud-scented room, the community breathes in. They measure what they have lost and what they have saved. The micro-projects are not panaceas; they have not halted the sea. They have, however, given"
    "people back a measure of agency. That agency is everything or nothing, depending on the next storm."
    "Your chest tightens with the weight of it. The very real losses sit heavy — the kelp that didn't take, the thresholds that failed, the night you could not save every home. The very real small"
    "triumphs press at the edges of your grief—neighbors bandaging each other, a child asleep with a blanket that once covered a community garden bench."
    "You let yourself feel both sorrow and the strange, precarious relief of work that mattered."
    hide elias_voss
    hide asha_reed
    hide maya_soren

    scene bg ch12_6b08b4_7 at full_bg
    # play music "music_placeholder"  # [Music: A single piano note holds, unresolved]
    "This is not victory. It is not even safety. It is a day's worth of survival, negotiated and earned. The arousal of the day—shock, action, near-break—has not quieted. It simmers into a persistent, jagged hope: a"
    "community that can respond and can, by doing so, claim the right to choose its future."
    "You close your eyes and promise, quietly, to keep holding the line—even when the ledger gets heavier, even when the bay demands more. The night gathers around the hub; the generators hum their small, defiant lullaby."
    # [Scene: Resilience Hub / Rooftop Garden | Night]

    scene bg ch12_6b08b4_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft murmurs, the occasional cough, the hub's heater clicking]
    # play music "music_placeholder"  # [Music: Sparse, minor-key chord—still tense, still unquiet]
    "You and the others file in, exhausted. Rosa hands you a cup of something hot and bitter; the steam fogs the air. Elias leans against the greenhouse glass and watches the bay like a man listening for a pulse."
    "Elias Voss: (softly) 'We start small. We teach, we rotate, we keep the books in the open. We keep the harvest local. We—' He stops, searching for a word that will not make a promise he cannot keep. 'We keep trying.'"
    "Asha Reed: (a tired laugh) 'Trying is what we have. And stubbornness.' (She looks at you.) 'You made the call, Maya. You could have let the city roll in with money and big machines. You didn't. You chose people.'"
    "You feel the praise like cold water and like balm. Your limbs slacken a fraction. But the sea's appetite is not sated. You know the micro-projects can be scaled, but scaling invites appetite from interests that would privatize resilience. You know that the next council meeting will be a battleground."
    "Your stomach knots. You did what you thought was the only moral route that wouldn't hand governance to shadowed boards. Still — guilt gnaws. Did you ask too little of the city? Did you refuse something"
    "that could have saved more? The Schrödinger questions live here: you can't be certain of roads not taken; you can only face what is lying in front of you, wet and immediate."
    "Jonah Mek: (clapping his hands once) 'Tonight we rest. Tomorrow we make schedules, repair lists, and classes for the kids on kelp care.' (He grins.) 'Also — we eat. Food keeps people whole.'"
    "You let yourself laugh, tiny and ragged. It is an offering."
    # play music "music_placeholder"  # [Music: A low, unresolved chord—expectant]

    scene bg ch12_6b08b4_9 at full_bg
    "You think of the ledger one last time: names, hours, decisions. The micro-projects are small stitches against a monstrous seam. They do not end the tide, but they bind people together in a way no contract could. That binding is a form of resistance."
    "There is sorrow in the perimeter of every small victory. The emotional palette undercuts any triumph with the knowledge of cost. You are steeped in concern for what will be asked of you next."
    "And yet—despite the bitterness—the hud of warmth around you says this was not in vain. For tonight, neighbors slept warm and sheltered because of choices made in filthy hands and tired lungs."
    "You breathe. You let the grief and the relief occupy the same space until they become a strange, honest companion."

    scene bg ch12_6b08b4_10 at full_bg
    # play music "music_placeholder"  # [Music: A single, dying chord]

    scene bg ch12_6b08b4_11 at full_bg
    "THE END"
    # [GAME END]
    return
