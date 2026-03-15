label chapter13:

    # [Scene: Reed Workshop | Morning]

    scene bg ch13_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Scissors snip, a low hum of conversation, water ticking against the pilings.]
    # play music "music_placeholder"  # [Music: Warm, patient strings—rising, patient]
    "You step under the eaves and the air shifts: peat and salt, the faint sweet rot of cut reed. Your hands know the rhythm—wrap, pull, bind—but your head is full of the meeting and the microphone"
    "and a hundred small decisions. Today is quieter; the work itself is the argument. Here, the labor speaks in knots and measured spans."
    "Old Man Rafi is already at the central bench, fingers steady as a tide. He smells of tobacco and sea-bleached wool. Marta moves between bundles, her short frame bent with careful measurement. Jun Park arrives with"
    "a tablet under his arm, cheeks flushed from the walk, while Eli Navarro lingers in the doorway with a tray of damp cookies and a grin that always looks like an invitation."
    show old_man_rafi at left:
        zoom 0.7

    old_man_rafi "So you remember how my sister used to tell it—the first check dam wasn't stones. It was a child's play, a braided line of reed to split the current from the gull. You tie it with your teeth if you must; the tide will teach you where to place it.' (He taps a reed end.) 'You don't fight the water. You teach it where to slow."
    show aria_solen at right:
        zoom 0.7

    aria_solen "You taught me that—sort of. I read Jun's slope curves and then I remember you saying the gulls change with the moon. The models want straight lines; you want place-lines. There's room for both, isn't there?"
    "Old Man Rafi: (He squints at the tablet when Jun Park holds it up.) 'The curve of a story is a map. If your machine and your story point different ways, you listen until they agree.'"
    "Jun Park: (softly) 'They're not always at odds. The parameters are just...simplified. If we fold in temporal variance—oral markers, seasonal anecdotes—we get a model that doesn't just predict thresholds. It predicts people.'"
    show marta_quin at center:
        zoom 0.7

    marta_quin "Prediction's fine. But we've done enough predicting to drown in paper. What matters is the next span. Who will carry it? Who will keep the knots from slipping when the first hard wind comes?"
    "Eli Navarro: (offering the tray) 'Cookies help with knot-keeping. Also, bribery works.'"
    "You take one, hands still smelling of reed sap. Inside your chest, something untangles: a part of you that always rushes toward big draws back—here, small, stubborn work insists itself. The braided walkway you imagine will"
    "be slow to build but fast to teach. It will hold memory; it will hold people."

    menu:
        "Kneel and test the reed roots":
            "You drop to one knee, mud cooling against your trouser cuff, and pull at a clump of rooted reed. The roots give in a way that tells you the season's yield—more than any spreadsheet. Rafi nods, pleased."
        "Stand back and listen to Rafi's stories":
            "You fold your hands and let Rafi's cadence lay the map in your mind—the landmarks, the misstepped tides. Jun's tablet glows between your palms; stories settle into the margins like sediment."

    # --- merge ---
    "The scene continues."
    # [Scene: Old Pier Market | Late Morning]
    hide old_man_rafi
    hide aria_solen
    hide marta_quin

    scene bg ch13_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Haggling, the slap of fish on wooden counters, a gull's impatient cry.]
    # play music "music_placeholder"  # [Music: A light, rhythmic guitar—hopeful, tactile]
    "The market smells of smoked fish and citrus, of fresh-cut timber from early boardwalk work. Market custodians—women and men who have run stalls for decades—cluster around a new placard you carried from the workshop: a hand-drawn plan showing braided walkways, reed check dams, and a small note—'held by the people.'"
    "Marta moves with a diplomat's grace, passing seed packets and explaining maintenance cycles. You hover at the edge, listening for the seams between the practical and the passionate."

    "Market Custodian (Asha)" "If the boardwalk won't hold when the kids run, we don't sign. We need something people can fix with a hammer and a cupped hand. Not a monocle and a bank.' (She taps the plan.) 'Who pays for the upkeep? Who makes sure the parts fit in three years?"
    show aria_solen at left:
        zoom 0.7

    aria_solen "You. The co-op. We'll set up a maintenance pool—seed-for-labor, time-for-materials. Jun Park will help us calibrate how often we need to check the anchors. Rafi and Marta will run trainings. We don't want something that leaves you dependent."
    "Market Custodian (Asha): (eyes flick to Jun Park) 'Your Jun here—he says time-for-materials. Does the machine know the smell of a market? Does it know what we do on market day when the tide turns?'"
    "Jun Park: (a little wry) 'No. The machine doesn't smell. But it can tell us where the wood needs support before the market loses another stall.'"
    show eli_navarro at right:
        zoom 0.7

    eli_navarro "And the rest? The rest is us showing up. We make it repairable with a toolbox and a story. You teach your neighbor to re-tie a braid and it's cheaper than a permit."
    "The custodian studies you—complex, unreadable. That expression is safe; it allows histories you may or may not share to sit between you without being forced into a single meaning. You find you don't mind the ambiguity. It's honest."
    "Marta: (clapping her hands once) 'Alright then—show of hands. Who's willing to try a prototype span this month? We'll do a night build, songs and lanterns. Rafi's cooking. Eli Navarro's got lights.'"
    "Hands go up, tentative and then surer. Your chest lightens with each palm."

    menu:
        "Volunteer to lead the night build":
            "You put your name forward. The room tightens for a beat—there's trust in that—and then cheers bend the air. Marta hands you a coil of rope like a baton."
        "Offer to bring materials and stay off the ladder":
            "You promise materials, money, planning. Marta smiles—relieved. You can feel your habit of control smoothing down into support."

    # --- merge ---
    "The community prepares for the night build."
    # [Scene: The Helix | Afternoon]
    hide aria_solen
    hide eli_navarro

    scene bg ch13_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Water lapping, the soft click of plant tags, Eli Navarro whistling an old dock song.]
    # play music "music_placeholder"  # [Music: Warm piano, a small hopeful swell]
    "Eli Navarro moves among the plants with practiced ease. He points out which seedlings have the most tenacity in saline mist, explaining in clipped phrases the improvisations that keep the Helix afloat: ballast adjustments, grafting techniques, humble sieves for brackish runoff."
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "We can grow a lot if you give them a place. The Helix isn't just a greenhouse—it's a proof. You build something people can touch, they believe in the idea."
    show aria_solen at right:
        zoom 0.7

    aria_solen "Proof makes politics legible. A living example complements the models and the stories. If Jun Park can show lanes where living shoreline will measurably reduce surge, and Rafi's markers tell us where to place them, we have both numbers and memory."
    "Jun Park: (spreading a transparent overlay over Rafi's hand-drawn map) 'See—if we weight this leyline with reed checks at these nodes, modelled runoff drops by—' (he hesitates) '—on average. But averages hide local variance. Rafi's markers are the variance.'"
    "Old Man Rafi: (watching the seedlings) 'Your averages are smart, Jun. They are like a net. But sometimes the fish slip through the net and you have to know where the fish liked to hide.'"
    "Eli Navarro: (softly, to you) 'You look tired.'"
    "Aria Solen: (you laugh, a little too sharp) 'Maps and stories and cookies. It's a full day.'"
    "Eli Navarro: (hands you a damp rag) 'Then rest like you're part of the garden. Come sit. Tell me the part that keeps you up; I can take it and make a stupid song out of it. Works every time.'"
    "You find yourself telling him anyway—small things, the tightness in your jaw, the image of an old shoreline map you can't unsee. He listens with that steady warmth that makes risks feel smaller."
    "Jun Park: (interrupting gently) 'If we pilot this as a hybrid—Helix-grown seedlings for plugs, Rafi-led placement, market-staffed maintenance—it's manageable. It also produces early wins. Funders like early wins.'"
    show marta_quin at center:
        zoom 0.7

    marta_quin "Early wins that teach. That's the line."
    "There's laughter, and for a minute the world feels wrapped in a consensus stitched of craft and care."

    menu:
        "Accept Eli's offer to sit and sketch plans together":
            "You sit on the sun-warmed bench, knees close. Eli passes you a smudged pencil and you sketch the first span together, his thumb steadying the paper. The plan looks like a promise."
        "Keep working, delegating the sketch to Jun and Marta":
            "You hand the pencil to Jun Park. He flutters through annotations, methodical. Marta hums an old tune as she ties a sample braid. You feel the day move even if you are not at the center."

    # --- merge ---
    "Plans are sketched and tasks distributed."
    # [Scene: Boardwalk | Dusk]
    hide eli_navarro
    hide aria_solen
    hide marta_quin

    scene bg ch13_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Hammer taps, voices low, the tide murmuring beyond the pilings. A dog barks faintly.]
    # play music "music_placeholder"  # [Music: Swelling strings—soft, ascending]
    "You stand at the edge of the span you've been building with the market custodians and co-ops. The first length of braid bears a small silver ring pressed into its edge—a token, perhaps, of the ring"
    "your late mentor gave you, or a communal vow; it is both. Hands rough with rope, people gather close. Old Man Rafi hums an old tide-song under his breath; Marta counts the knots aloud as if"
    "she's keeping the sea from fretting."
    "Jun Park runs a last check of his overlay, his face lit by lantern light and the tablet's glow. He looks up at you—an expression that contains equal parts scientist's relief and someone who has learned to believe in hands."
    show jun_park at left:
        zoom 0.7

    jun_park "The model says this span should reduce flow enough to let sediment accrete by the next spring. Rafi's markers suggested we start here. The two lines converged."
    show old_man_rafi at right:
        zoom 0.7

    old_man_rafi "And the gulls agreed. They nested on the north pole of the span this morning."
    "Marta: (elbowing you gently) 'See? They like it.'"
    "Eli Navarro: (quietly) 'We made it a place people want to be.'"
    "You fold your hands around the rope, feeling its fibrous warmth. Your chest loosens in a way that is almost like gratitude, and it's startling to feel gratitude in public. Everything you built—talks, lists, long nights—swells into a single visible thing you can walk on."
    "A gull clocks above, and then—just beyond the curve of the pier—you catch another light. Not a market lantern. Not a lantern at all."
    "It is a distant, steady beam: white, regulated, and moving with intention across the water. For a trembling second you are back at the meeting room, the microphone heavy in your hand. Momentum feels fragile and"
    "alive; resistance feels vivid and possible. The beam cuts the dusk, a single, clarifying line on the horizon."
    "Eli Navarro: (following your gaze) 'That's not a fishing boat.'"
    "Marta: (quiet) 'No.'"
    "Jun Park: (already reaching for his tablet) 'Could be a survey ship. Could be—'"
    "Old Man Rafi: (still, then) 'Or news.'"
    "You feel the hush spread through the cluster of people as if the tide itself has paused. The beam paints the boardwalk in a scraped white line; your braid, your knots, the silver ring—everything is suddenly framed against that light."
    "You inhale, and the breath is full of salt and promise and the knowledge that something outside this careful day has moved. It is not yet a problem; it is a presence, and presences demand a response."
    "You stand with the rope in your hands, the boardwalk beneath your boots steady. The town has given you hands; you have given them a path. The beam on the horizon reframes the question of what comes next without solving it."
    hide jun_park
    hide old_man_rafi

    scene bg ch13_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: The strings lift into a single hopeful chord that holds—expectant]
    "You find, unexpectedly, that you are not afraid. You are ready in a way that whittled labor and patient listening can make you: not certain, but prepared to meet whatever arrives with community at your side."

    scene bg ch13_453e40_6 at full_bg
    "You feel the night press in, and the beam becomes a punctuation mark on the close of a busy day—a page folded down. You want to know what the beam brings; you want to know how the town will read it. You lift your chin. You will find out tomorrow."
    # [Page-Turn Moment]
    "You slip the coil of rope over your shoulder, the leather notebook heavy and warm against your ribs. The murmurs around you knit into plans, hands, lists. Somewhere, a child runs barefoot across the new braid,"
    "squealing. The beam on the horizon slices the sky and makes the sea obedient for a breath. You take one last look at the market custodians' faces—tentative, resolute, lit from within—and the thought that carries you"
    "forward is simple and true: we have started something that refuses to sink."

    scene bg ch13_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter14
    return
