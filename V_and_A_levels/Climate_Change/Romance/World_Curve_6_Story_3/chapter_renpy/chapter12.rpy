label chapter12:

    # [Scene: Greenhouse | Late Afternoon]

    scene bg ch12_6b08b4_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, insistent percussion under a high violin drone—heartbeat / tide]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls muffled by rain; a satellite phone buzzing faintly in a canvas bag]
    "You are bent over a spread of printed models and hand-scrawled columns—ecosystem-service valuations, predicted sediment accretion, payroll sheets stained with coffee and salt. The numbers don't comfort you; they scaffold a promise that feels half-made. You"
    "rub the heel of your hand across your cheek and taste the metal tang of seawater on your tongue even though you are inside, sheltered by glass and green life."
    "There is a rhythm to the weeks since Elias formed the coalition: mornings at the harbor running apprenticeship workshops and retrofitting stalls; afternoons his voice on the phone, negotiating clauses; nights the stubborn thrum of your"
    "laptop and the scratch of a pencil as you translate biology into budget lines. For a while the work felt like progress—steady pay for hands that had been idle, small woodshops reopened, Rosa's nephews apprenticing on"
    "new net-repair rigs. You told yourself it was a compromise; you told yourself that compromise could be a kind of care."
    "You close your eyes and let the greenhouse's humidity sit on your skin. A fern leaf slips under your fingers like a promise. The compass pendant at your throat is cool against your clavicle; you press"
    "it until it leaves a faint ring. Elias sent a message earlier—he's still at the harbor. The council memo has done its work, in part, because he promised to make the economic guarantees real. You can"
    "feel the weight of that promise buzzing in your bones."

    menu:
        "Call Elias and ask for a status update":
            "You lift the phone, thumb hovering. The message window shows a long-read receipt; the call nets to voicemail. You leave a voice that tightens when you try to keep steady."
        "Finish the report here and go to the harbor after dusk":
            "You pull the last sheet into place, tape a corner, and slide the folder into your bag. The plants rustle as if urging you onward."

    # --- merge ---
    "Proceed to Harbor scene"
    # [Scene: Harbor | Early Evening]

    scene bg ch12_6b08b4_2 at full_bg
    # play music "music_placeholder"  # [Music: Tension strings; a sharper, metallic percussion enters—gears meshing]
    # play sound "sfx_placeholder"  # [Sound: Hammering, the hiss of a hot riveter, voices carrying over the slap of small waves]
    show elias_voss at left:
        zoom 0.7

    elias_voss "You made the report?"
    show maya_ortega at right:
        zoom 0.7

    maya_ortega "Part of it. The rest needs the field numbers you promised me. How long until the insurance clauses are finalized?"

    elias_voss "Tomorrow. We pushed the carriers on exemptions—some concessions. It wasn't easy. We got guarantees for payroll. That was the priority."
    "You lean on a crate. The smell here is of tar and varnish and new paint, overlaid with diesel and the sweet iron of the sea. Apprentices are piecing together replacement fish stalls under bright lamps;"
    "their hands are sure, but eyes flick to the ocean with a watchfulness you know too well."
    show rosa_delgado at center:
        zoom 0.7

    rosa_delgado "They told us equipment would be moved first, then the wall. We put things where you said safe. Now they're telling me my nets better be insured separately. What's that mean, Elias? Who pays for the boats if they get lost?"

    elias_voss "Rosa, we've guaranteed jobs. The coalition's funding is—"

    rosa_delgado "Jobs don't bring back my father's boat. Jobs don't bring back the sign he carved when he came back from sea. Those things are part of people, Elias."

    elias_voss "We're not ignoring that. We thought the rapid-build zones would buy us time to move fragile things. We shouldn't have left any of it exposed—"

    maya_ortega "You thought. 'Thought' doesn't fix wood splintered by surge."
    "Your voice is quieter than the others', but each word lands like a struck bell. Elias steps closer, opening and closing his hands as if the right gesture will gather everything back together."

    elias_voss "I can go to the carriers. I can—"

    rosa_delgado "Go? We were out there while you were signing contracts."
    "Elias's face crumples for a fraction of a second. He is not used to seeing his own gestures—those compromises—reflected as wounds. The apprentices continue working, unaware of the argument's gravity; the town depends on both the concrete and the hands that shape it."

    menu:
        "Stand between them and call for calm":
            "You step forward, hands raised. For a second their angry lines falter. The pause is brief; it does not dissolve everything but it buys air enough for a plan."
        "Let them speak; listen more than you intervene":
            "You fold your arms and let Rosa's words roll. Listening carves truth from rage; you feel the facts reconfigure in your chest—harder to ignore."

    # --- merge ---
    "Continue to Incoming Stormfront scene"
    # [Scene: Incoming Stormfront | Night]
    hide elias_voss
    hide maya_ortega
    hide rosa_delgado

    scene bg ch12_6b08b4_3 at full_bg
    # play music "music_placeholder"  # [Music: Drums explode into staccato—fast, relentless. Brass slashes. The violin line shrieks and then drops into a raw tremolo.]
    # play sound "sfx_placeholder"  # [Sound: Wind roaring, the crack of timber, the wet slap of waves force-fed into the shore; alarms wail; shouts cut through the cacophony]
    "Everything becomes urgent at once. You run, boots slipping, rain soaking the collar of your jacket. The apprentices are hauling gear, ropes snapping like whips; people are shouting names into the dark. Flood-lights flare, casting everyone in hard, unforgiving light."
    "You can see the rapid-build zones performing exactly as engineered—a wall throws back a mass of water like a hand. It is impressive and it still feels wrong in your chest, because the surge has found"
    "the seams. Where the quick-build stopped—where the coalition's budget didn't prioritize the smaller co-ops and the old stalls—water reaches with terrible persistence."
    "Rosa's cooperative is wedged in a shallow cove, the nets and their storage crates at lower elevation. You scream her name and see her silhouetted, trying to anchor a small boat as a breaker tips it"
    "like a toy. A sheet of rain slashes your face. You taste iron and salt and something hotter—adrenaline laced with the metallic shock of fear."
    "You dive in beside her. Hands work, fingers numb. You can feel rope fibers bite into your palms; something gives way. A net tangles; a boat slams against a piling and capsizes with a sound like"
    "a throat closing. For a heartbeat you're underwater, the world reduced to salt and a dull white roar. When you bob back up you see the fish stall—the one with the hand-carved sign—ripped off its mooring"
    "and spinning with the tide like an abandoned toy."
    show rosa_delgado at left:
        zoom 0.7

    rosa_delgado "My customers—my boxes—gone! The ice-chest—"
    "Elias Voss appears at the edge of the scene, eyes wild, sleeves plastered to his arms. He tries to hand you a coil of rope; the gesture is frantic and inadequate."
    show elias_voss at right:
        zoom 0.7

    elias_voss "We— I thought the insurance would cover—We prioritized structural integrity. The carriers refused to list 'cultural artifacts'—it was a cost clause. I—"
    "You, soaked, wrenching a line, can't keep the accusation from surfacing. It isn't just about money anymore; it's about the thing those contracts rendered invisible."
    show maya_ortega at center:
        zoom 0.7

    maya_ortega "You signed it, Elias. You promised us you'd move the fragile stuff first. You promised we'd be protected."
    "Elias's face goes taut with something like physical pain. He doesn't argue so much as fold inward, the weight of his decisions pressing into him like a tide."

    elias_voss "I thought— I thought ensuring pay would stop people from leaving. I thought if they had steady work, they'd stay to fight—"

    rosa_delgado "We needed to survive tonight. Not a check next month. Not a job that starts after we rebuild what you allowed to be lost."
    "The storm roars; splinters fly like teeth. Someone's hand is bloodied. A plank slams into a crate, bursting ice and fish into the water. The sensory tide is endless—oil, wet wool, the metallic tang of blood and salt, the bitter smoke of emergency lanterns."
    "You act without thinking: you pull a boy free from under a collapsed awning, tamp down a small electrical spark before it can set a soaking stall alight. You patch what you can with tarpaulins and"
    "your own body heat. But the losses are real and irretrievable; the insurance's fine print is a paper reef that cuts and does not hold."
    "The storm peaks—lightning splitting the sky—and in the pause between waves you hear the low, terrible intake of a community's breath."
    # [Scene: Harbor / Dawn Aftermath]
    hide rosa_delgado
    hide elias_voss
    hide maya_ortega

    scene bg ch12_6b08b4_4 at full_bg
    # play music "music_placeholder"  # [Music: Slow, minor-key cello; the percussion now a hollow echo of the night's drums]
    # play sound "sfx_placeholder"  # [Sound: Conversations undercut by the drip of water; someone somewhere is quietly crying; a power saw groans as people rebuild]
    "The coalition's payroll isn't a lie. The docks now hum with paid labor; people are employed, busy, moving, sorting. Apprentices who would have sat idle now carry sacks, learn to knot, and stitch nets under supervision."
    "There is an efficiency to it that makes your chest tighten—there are checks being written while the town's history lies in wet pieces."
    "Rosa sits on a crate, shoulders rounded, the shell charm in her braid broken. Her expression is a map of something that won't be smoothed over by a wage. She cradles a small carved fish—charred at"
    "an edge—and the rest of the stall is a skeletal ruin. When she looks up and sees Elias approaching with a toolkit and a look that has humility brittle as glass, she does not get up."
    show rosa_delgado at left:
        zoom 0.7

    rosa_delgado "You sold us a schedule, Elias. You chose what to protect."
    show elias_voss at right:
        zoom 0.7

    elias_voss "We didn't expect the surge of that magnitude in that channel. The funding prioritized workforce and structural segments—"

    rosa_delgado "Funding. That's what we keep hearing. Maybe we should have asked the sea for a check instead."
    "You are between them, feeling the cold of the morning in your bones and the heat of anger under your skin. Elias reaches out; Rosa pulls her hands into her chest. The apprentices watch like children at a lesson they didn't ask to learn."
    show maya_ortega at center:
        zoom 0.7

    maya_ortega "This isn't only about what was insured. It's about who's counted when decisions are made."

    elias_voss "I counted the town, Maya. I thought— I judged the risk to lives and livelihoods. If I could undo it—"

    maya_ortega "You could have pushed harder to include the small co-ops. You could have refused clauses that carved culture out of value. You didn't."
    "Elias flinches at the last. For a moment he looks like a man split in two—one part the pragmatic negotiator who kept the lights on, the other the neighbor who now has to live next to ruins his compromises helped produce."

    elias_voss "I carry it like salt in a cut. I don't know how to make it right."

    rosa_delgado "You don't make it right. You fix what you can."
    "You find yourself stripping off your wet jacket and sitting down at the greenhouse's edge later, the report heavy in your lap. The glass is streaked with the same rain that broke everything open; the plants"
    "smell like a green hospital. You press the compass pendant, feel its cold roundness, and let the report's pages whisper against each other. The town will keep breathing. The coalition's promise means people will have work"
    "and pay, and that matters. But tonight the price is visible—boats and signs, the curve of familiar roofs—scattered and raw."
    "Your nights are already full of calculations; your days of literal heavy lifting. Your chest holds a new arithmetic: stability minus belonging. You have to decide, now that the dust and salt sit in the seams,"
    "what you will do with the rest of your life here, with Elias at your side or not, and with a town that has traded some of its texture for a ledger that balances."
    "Elias appears at the greenhouse door, rain in his hair, paint on one knuckle. He doesn't speak for a long time—just watches you turn the pages, watch the way your lips press together when you reach a figure that doesn't add up."

    elias_voss "Maya—people are angry. Rightly. I thought the guarantee... I thought—"

    maya_ortega "Thoughts are not plans, Elias. Promises are not a shield if you didn't make the right ones."
    "Elias closes his eyes, the shame a physical thing in his face. He opens them again, searching for a place to put the culpability he feels."

    elias_voss "Tell me what to do. Tell me how to help."
    "The question is simple, devastating. It asks you to choose the moral direction—public accountability, quiet restitution, or some other path that would stitch the torn thing together. The town's future balances on the answers you could"
    "give. You feel the tide of consequence—legal, personal, communal—swelling, and you understand that any decision will hollow something out even as it saves something else."
    "You look at Rosa's ruined sign in the distance, at the apprentices' gloved hands, at the newly polished storefronts that gleam with investor logos. You listen to the greenhouse clock ticking and to the distant sound"
    "of hammers starting again—because life continues and because the work of undoing or accepting has begun whether you speak or not."
    "You inhale, and the air tastes of salt and smoke and wet wood. The compass at your throat is heavy."
    # play music "music_placeholder"  # [Music: A held, dissonant chord—strings scraping to a halt; then an almost-silent single piano note]
    "You can decide to call the council to demand reparations. You can go public with the cultural-loss argument and risk derailing the very payroll you fought to secure. You can take Elias aside and make him"
    "promise to fund personal restitution. You can organize a community labor pool to rebuild the co-op with volunteer hours that will cost you days you don't have. Each path costs something."
    "You feel the town behind you—its breathing, its wounds, its stubbornness. You feel Elias before you—his hands, his promise, the salt in his cuts."
    "You lift your head. The decision sits like an incoming wave—inevitable, unstoppable."
    hide rosa_delgado
    hide elias_voss
    hide maya_ortega

    scene bg ch12_6b08b4_5 at full_bg
    "THE END"
    # [GAME END]
    return
