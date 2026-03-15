label chapter31:

    # [Scene: Polished Quay | Midday]

    scene bg ch14_cfa7c2_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, hopeful strings; steady tempo]
    # play sound "sfx_placeholder"  # [Sound: Distant gull cry; the soft hiss of seawater against concrete]
    "You stand with your hands folded around the leather spine of your notebook because it is something to hold when everything else is measured and signed. The room smells like engineered citrus and coffee—Corinne’s signature scent"
    "of competence. Outside, a low tide exposes the scarred sand where the town has argued about lines for months. Inside, the lights are immaculate; the air is precise."
    "Corinne Voss smiles with the economy of someone who has rehearsed this exact moment. She slides a projected schematic toward you—revised, smaller, a ribbon of port rollback, a set of funded restoration pockets, and an operational clause cordoning low-lying blocks for port expansion."
    show corinne_voss at left:
        zoom 0.7

    corinne_voss "We scaled back. Community-managed marsh pockets, TideLab funding, relocation assistance for affected lots. We keep port efficiency, Marisol keeps most homes. It's a compromise that protects lives and capital—both necessary."
    "Tamsin stands beside her, fingers tight around a tablet. You can see the small tremor in Tamsin's jaw; the planner has been pulling and being pulled all at once. Abuela Rosa is there too, stooped shoulders like steady stone, eyes that have seen tides and treaties and worse."
    show abuela_rosa at right:
        zoom 0.7

    abuela_rosa "We asked for land, for dignity, and for the tools to weather storms. Will you give us that, Corinne? Not your words. Proof."
    "Corinne's smile doesn't change but her hand pauses. She taps the holograph; the restoration budget unfurls, escrow accounts, a community oversight clause—terms that, if enforced, put real resources in place."

    corinne_voss "Funded oversight. Community board representation. TideLab is explicitly named."
    "You feel pressure ease in your sternum—small air finding room. The immediate threat, the bulldozers and PR blitz that would have bulldozed the marsh first and asked forgiveness later, recedes in time. The hall is quieter;"
    "the town's breath seems to find a rhythm that won't be cut off by a corporate clock."
    show mateo_reyes at center:
        zoom 0.7

    mateo_reyes "So some houses go. Some of our nets shift. But the pier stays. My traps get insurance. People eat next winter. Is that it, Amaya?"
    "You swallow. If you let yourself catalog everything you gave and everything you kept, your chest will become a ledger no ledger can balance. Instead, you speak to the things balance will buy."
    hide corinne_voss
    show amaya_reyes at left:
        zoom 0.7

    amaya_reyes "It isn't everything we wanted. It's protection for schools, the generator, the clinic—it's funding for mangrove planting and oyster beds. It is time and tools to keep TideLab working while families make safe choices."
    "Mateo looks at you, then at the hologram that shows the line on a map, a red sliver for neighborhoods that will be offered relocation support. His hands—fisherman's hands, knuckled and used—shake minutely."

    mateo_reyes "People are going to hate you for this. They'll say you sold us out."

    amaya_reyes "Maybe some will. But hate is not the same as harm. If these funds mean fewer flooded basements next season, fewer lives lost, I can't watch us gamble that for pride."
    "The room smells suddenly of rain that hasn't fallen yet. Tamsin's eyes are wet but hard."
    hide abuela_rosa
    show tamsin_cho at right:
        zoom 0.7

    tamsin_cho "Council has the vote, but with these terms and the oversight clause, I can push it through. It's not perfect. Nothing is. But it's the way to lock in resources and time."
    "Corinne steps forward; her voice softens for the first time—not because she is sentimental, but because she is practical enough to see the human cost of political loss."
    hide mateo_reyes
    show corinne_voss at center:
        zoom 0.7

    corinne_voss "We will fund relocation grants beyond what regulation requires. We'll endow a TideLab fund that cannot be commandeered by corporate restructuring. We will hire local crews for restoration."
    "You note each concession mentally like stitches: not the same as a whole cloth, but mending nonetheless. The line on the map cuts through neighborhood blocks; the operational clause means some lots will be ceded, permanently. You taste salt and success in small, stinging measures."

    menu:
        "Reach for Luka's sleeve for reassurance":
            "Your fingers catch the cuff of Luka's smock. He looks down, surprised, and squeezes your hand back—brief, electric; a promise unnamed."
        "Step back and make space":
            "You step back, letting the room breathe. Luka meets your eyes and nods—there's a question there neither of you voice."

    # --- merge ---
    "The narrative continues."
    # [Scene: Boardwalk | Late Afternoon]
    hide amaya_reyes
    hide tamsin_cho
    hide corinne_voss

    scene bg ch14_cfa7c2_2 at full_bg
    # play music "music_placeholder"  # [Music: Mid-tempo acoustic guitar with a warm undertow]
    # play sound "sfx_placeholder"  # [Sound: Laughter mingled with low conversation; children kicking a plastic ball near a repaired bench]
    "You exit the hall into a town that is both relieved and unsettled. People are clustering—some with smiles that look like relief, others with mouths set in lines that say the loss is not yet accepted."
    "Abuela Rosa walks next to you, shawl tucked, eyes measuring the horizon and the small wounds at the edges of the quay."
    show abuela_rosa at left:
        zoom 0.7

    abuela_rosa "You did what you could. The sea will take less now. That is something."
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "It is a thing,' you admit. 'And it is not enough."
    "Abuela Rosa's fingers close on your wrist, dry and sure."

    abuela_rosa "Do the work that comes next. Plant seeds that hold. Teach the children how to read tides. Make sure what is given reaches hungry hands."
    "You nod. The town will need organizing, oversight committees, audits, training. TideLab will not be a quiet lab anymore but the center of a new network—community liaisons, restoration crews, monitoring drones—but the weight of being the one who said yes sits heavy."
    "Luka Maren finds you at the railing, his shadow long. He smells faintly of solder and salt, the way he always does after a day in the field. His amber eyes are carefully neutral."
    show luka_maren at center:
        zoom 0.7

    luka_maren "They offered me a consultant position. Part-time, they say. Influence at the table. Pay to stabilize the prototypes and scale the sensor nets."
    "You feel something recede inside you, a small, sharp hollow."

    amaya_reyes "You accepted?"

    luka_maren "I asked for conditions. I asked to keep control of the open-source side. I asked that TideLab be part of the oversight committee. They agreed on paper."

    amaya_reyes "And in practice?"
    "Luka Maren looks away for a breath, the sea moving his profile like a borrowed hand."

    luka_maren "In practice, it's the difference between me being outside yelling and me being inside nudging. I think—' he pauses, trying to find a sentence that won't break the moment, '—I can do more from here than standing on the pier and watching."
    "You want to argue—about compromises and slippery slopes and how corporate boards eat intentions. You also remember nights with him soldering sensor boards until dawn, his quiet laugh when a prototype finally held together. You know his fear of failing the community, the same fear that drives both of you."

    amaya_reyes "I don't like the idea of you fitting yourself into their rhythm."

    luka_maren "I don't want to either. But if I can keep a voice on that board—if I can make sure their dredging schedules sync with our restoration plans, isn't that better than being locked out?"
    "Your mouth tastes of sea and truth. For a moment, the two of you are silhouettes against the bay: the pragmatist and the tinkerer, lovers and colleagues, both sanded by loss."

    amaya_reyes "Promise me you'll come back to TideLab. Not just in reports."

    luka_maren "I promise."
    "He says it with a kind of careful honesty that is both hope and a hinge. You accept the promise because you need to, and because you want to believe it. The word settles; it is brittle but real. The moment is both tender and taut."

    menu:
        "Take his hand and hold it":
            "You take his hand; the skin is warm and familiar. The contact is small but healing—brief proof of human constancy in political tides."
        "Let your hands hang loose at your sides":
            "You let your hands fall. The space between you feels important, a place where both of you can still choose who you will be."

    # --- merge ---
    "The narrative continues."
    # [Scene: TideLab | Evening]
    hide abuela_rosa
    hide amaya_reyes
    hide luka_maren

    scene bg ch14_cfa7c2_3 at full_bg
    # play music "music_placeholder"  # [Music: Gentle piano with a single ascending motif]
    # play sound "sfx_placeholder"  # [Sound: The soft whir of a drone recharging; glug of coffee being poured into a chipped mug]
    "Back inside TideLab, the energy is purposeful. Volunteers move with lists; Jules jokes about filament rolls while someone else tapes up a batch of mangrove seedlings. The TideLab fund—Corinne's concession—sits as a line-item on your mind"
    "and now as a bank transfer in the ledger, a real thing you can use."
    "You walk past the bench where you first sketched tidal maps in battered ink. Your fingers trace the edge of the table; salt and paint are embedded in the grain. All around you, the community retooled the shed into a workshop for adaptation. It is messy and hopeful and alive."
    show jules_park at left:
        zoom 0.7

    jules_park "We got extra storage. And a contractor who knows how to install those sensor poles. He says we can have teams out before the next rain."
    "Jules's grin is contagious; you allow yourself a small smile. The tangible work hums beneath the moral calculus: root the shoreline, track the tides, teach people to read the new rhythms. You will make sure the oversight clause lives up to its name."
    "You sit, open your notebook, and sketch a tide map—red marks replaced by green stitches where restoration will take hold. The act is quiet, a small ritual."
    "Mateo drops a fishing net across a chair, wet and smelling like honest labor."
    show mateo_reyes at right:
        zoom 0.7

    mateo_reyes "Your Abuela says you'll need help organizing crews for relocation and restoration. I'm in. The crew's in. We'll do the heavy lifting."
    show amaya_reyes at center:
        zoom 0.7

    amaya_reyes "We'll need to be fair. We'll need to make sure people who move have choices that keep their lives intact—not just a roof but a livelihood. That's the work now."
    "Mateo grins a tired smile. 'You always make work sound like a good idea.'"
    "You both laugh—a little too sharp—and then the laughter softens back into resolve."
    "Luka Maren approaches with a small box: a newly soldered node, the open-source sticker still visible on the casing. He places it on the bench between you."
    hide jules_park
    show luka_maren at left:
        zoom 0.7

    luka_maren "I left the connector accessible. I want the code to be easy to fork. I promised them influence, but I promised you that I wouldn't let the tech go proprietary."
    "You glance at the node, at the sticker, at his careful hands."

    amaya_reyes "Keep that promise. Keep coming back."

    luka_maren "I will. I don't know how often, but I will."
    "There is a quiet acceptance in both of you—a redefinition of what being together looks like when both of you are tied to different kinds of duty. The threshold between partnership and partnership-with-constraints is thin and"
    "shifting, but you will keep pacing it. For the first time in a long while, there is room to breathe."
    hide mateo_reyes
    hide amaya_reyes
    hide luka_maren

    scene bg ch14_cfa7c2_4 at full_bg
    # play music "music_placeholder"  # [Music: The piano motif resolves into a calm major chord]
    # play sound "sfx_placeholder"  # [Sound: Rain begins, light and regular, on the corrugated roof; it sounds like a benediction]
    "You step back onto the boardwalk that evening as rain begins in earnest. The town seems quieter, not defeated but reorganizing. Lamps halo in the mist; people move with umbrellas and tarps and a new, weary certainty."
    "Abuela Rosa stands watching the water with you. She has the shawl around her shoulders and the look of someone who has traded anger for the thing she knows will preserve future generations."
    show abuela_rosa at left:
        zoom 0.7

    abuela_rosa "You made a decision with the people. That is not surrender, niña. That is stewardship."
    "You want to argue—because it was a concession and concessions cost—but you see the truth threaded through her words. Stewardship sounds like a better name for the weight you're carrying."
    "You lift your face to the rain. It is cool and clean on your skin. The ache is there, but beneath it, something steadier: a conviction that the money and oversight and the crews will plant roots that will hold. That you will hold them."
    "You walk the length of the boardwalk, past homes that will remain, past the red-slashed streets on the map that will be offered relocation. You think of the people who will grieve, the dinners you'll have"
    "with neighbors who are leaving, the lessons TideLab will teach, the days you'll sit in courtrooms and town halls and—if necessary—on the pier."
    "You close your notebook and tuck it under your arm. You do not know how Luka's role will change him. You do not know how many nights you'll spend awake counting arrivals and erosion rates. But"
    "you do know this: you chose a path that kept most of the town intact and gave you real tools to do the work you love."
    "The rain steadies into a rhythm, and for once the sound is not a threat but a metronome to the new work ahead."
    "You breathe in the salt and the rain and a small, fierce hope."
    hide abuela_rosa

    scene bg ch14_cfa7c2_5 at full_bg
    # play music "music_placeholder"  # [Music: Strings rise into a warm, affirming chord]
    "You are tired. You are proud. You are wary and resolved. The cost is heavy, but the cost of inaction would have been heavier. You have been both pragmatic and compassionate; you have traded some ground"
    "to buy time and resources for the many. That trade will be justified in the soil and the seedlings and the sensor data that keeps people safe."
    "You watch Luka disappear into the night, a figure with purpose inside a corporate rhythm you do not fully trust—but one you have, strategically, bent toward the town's favor. You allow yourself the quiet belief that influence inside a system can be a light in dark places."

    scene bg ch14_cfa7c2_6 at full_bg
    # play music "music_placeholder"  # [Music: A single, bright piano note lingers and then resolves]
    "You turn and walk back toward TideLab, toward the lists and schedules, toward the people who will be doing the daily, steady work of keeping Marisol Bay breathing."

    scene bg ch14_cfa7c2_7 at full_bg
    "THE END"
    # [GAME END]
    return
