label chapter13:

    # [Scene: Marsh Fringe | Night]

    scene bg ch13_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the hush of water against marsh grass]
    # play music "music_placeholder"  # [Music: A single, low cello note; sparse and unresolved]
    "You stand where the reeds thin and the flats open, the town’s lights a smudge down the arm of the sound. Night holds the marsh like a thing that has learned to be patient—slow breaths of"
    "water and mud, indifferent to human promises and debts. Your breath fogs in front of you; it smells of salt and diesel and yesterday’s coffee from the diner where you stayed awake drafting figures."
    "You have spent so many lives in maps: contour lines that mean survival, species lists that mean names for what’s being lost. Tonight those maps feel like a ledger kept by a creditor you cannot charm."
    "Every option you can imagine saves something and takes something else. The word compromise tastes of iron."
    "You thumb the corner of the notebook closed against the damp and look back toward the lights on the headland—the skeletal flashlights of surveyors, the corporate banners stitched to poles, a faint mechanical heartbeat you can"
    "count like a clock. You imagine—briefly, intrusively—how the marsh will read the aftermath: raised walkways and piled earth, channels rerouted, eels out of place. Your chest squeezes."

    scene bg ch13_3be532_2 at full_bg
    # play music "music_placeholder"  # [Music: A minor third descends slowly]
    "You tell yourself you’re going into mediation tomorrow not to sign away the marsh but to anchor a living shore in legal language; to buy the seedlings time and people bread. You tell yourself words you"
    "would tell other people—precise, plausible, calibrated to persuade. Behind your ribs the old small voice—the one that has always loved this place—keeps tally of likely losses."

    scene bg ch13_3be532_3 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]
    # [Scene: Town Hall / Meeting Room | Morning]

    scene bg ch13_3be532_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Chairs scraping, a kettle clinking in the back as someone pours coffee]
    # play music "music_placeholder"  # [Music: Low, tense strings; an atmosphere of compressed urgency]
    "You arrive early. The fluorescent lights smell faintly of ozone and disinfectant. People cluster like flotsam: a woman with a child's raincoat over her arm, Tomas leaning on the back wall like a weather-worn sentinel, Rina"
    "arranging a stack of NGO briefs with the clinical calm of someone who has learned to count outcomes. Cass is there already, sleeves rolled at her trench coat, tablet unrolled and deliberate on the table. Mayor"
    "Rosa moves through the room like a line of compromise incarnate—pleased and pained all at once."
    show cassandra_cass_rey at left:
        zoom 0.7

    cassandra_cass_rey "Thank you for coming on a weekday. I know the timing's rough, and— we've put forward an amendment to the Azure Crescent plan. It freezes construction in identified marsh cores and redirects funding for workforce transitions. It's pragmatic, immediate."
    "Cass's voice is that smooth thing you’ve argued against and sometimes wished you could borrow. Her eyes are steady, unreadable—too practiced to show what she truly fears."
    "You find your seat and feel Eli's presence before you see him—his hand on the back of your chair, thumb drawing a small, impatient circle. He doesn't speak yet. His jaw is tight; there's a salt"
    "trace on the cuff of his flannel where he rubbed his sleeve across his mouth."
    show elias_eli_calder at right:
        zoom 0.7

    elias_eli_calder "Pragmatic's a good word. Practical. Jobs for the next season. My sister’s boys— they need work, Mara. Not promises that arrive on a timeline only donors can keep."
    "You know his ledger runs different from yours: immediate mouths, loans on boats, planks that rot or hold depending on the weather. He believes in the visible: a job, a finished dock, a counted catch. You"
    "believe in systems modeled across decades. Both of you keep lists of what can't be replaced."
    show mayor_rosa_alvarez at center:
        zoom 0.7

    mayor_rosa_alvarez "We are not naive. We need both. Cass’s amendment offers a path that the council could pass today, which would pause the graders in the most vulnerable zones and allow parts of the headland—less sensitive tracts—to move forward with oversight. It would free immediate funds for transitional employment programs."
    hide cassandra_cass_rey
    show rina_park at left:
        zoom 0.7

    rina_park "Transitional employment is crucial, but the timing and oversight matter. Opening parts of the site now risks irreparable hydrology changes that no mitigation fund can buy back."
    "You open your notebook. You don't write numbers—you sketch mental margins, the edges you can push. The room smells now of reheated coffee and damp wool, and beneath that, something metallic from the display boards."
    hide elias_eli_calder
    show old_tomas_calder at right:
        zoom 0.7

    old_tomas_calder "This town’s taken storms and come back. But every return costs a story."
    "A low murmur spreads; the phrase lands like a pebble and sends tiny ripples."

    menu:
        "Look at the tide maps pinned to the board":
            "You step toward the corkboard and trace a potential channel with a gloved finger, feeling the lines like a wound you could stitch. The council watches you translate data into shape; some faces relax, some tighten."
        "Lock eyes with Eli and squeeze his hand":
            "You reach for his hand beneath the table. His shoulders ease for one breath. The room's noise becomes muffled; you remember why you started fighting for both marsh and people."

    # --- merge ---
    "Cass returns to the table with a small printed packet—renderings that show a modified promenade, a thinner line of sea wall, and shaded swaths marked 'preserve'."
    hide mayor_rosa_alvarez
    show cassandra_cass_rey at center:
        zoom 0.7

    cassandra_cass_rey "Look, this isn't about erasing the marsh. It's about keeping the town solvent while we build protections that scale. The engineers on our team can model living-shore overlays on the preserved zones. They'll need space and a guarantee that construction elsewhere won't destabilize hydrology."
    "You listen to the word 'guarantee' like a pulled string. Guarantees are political currency; they rarely translate to ecosystems. Still, you weigh it: a freeze in core zones could let eelgrass beds rebound. If monitored properly,"
    "maybe seedlings planted this season take hold. You imagine a narrow band of saved mud and reeds and a widened economy beyond it."
    "You stand to speak. Your voice feels small but clear."
    hide rina_park
    show mara_voss at left:
        zoom 0.7

    mara_voss "If we slice the headland—if we allow work in some sections—stream shifts could cut the cores off. We need real, enforceable hydrological monitoring and an independent oversight board that can halt graders at any sign of change. No staged releases."
    hide old_tomas_calder
    show mayor_rosa_alvarez at right:
        zoom 0.7

    mayor_rosa_alvarez "Independent oversight—acceptable in principle. We could name members, a blend of local, academic, and third-party reviewers. The county attorney will draft the language."

    cassandra_cass_rey "Workable. Names and clauses—yes. We have deadlines, and time is a factor. If the council stalls too long, contractors will file for damages. The town can't afford prolonged litigation."
    "You feel the floor shift under the word 'damages'—it curves into ledger-lines of lost contracts and families clinging to the present. The room fills with the arithmetic of risk."
    hide cassandra_cass_rey
    show rina_park at center:
        zoom 0.7

    rina_park "And the transitional job fund? Who administers it? How long? Where do the money and oversight come from?"
    hide mara_voss
    show cassandra_cass_rey at left:
        zoom 0.7

    cassandra_cass_rey "A portion of the development’s budget will be escrowed. NGOs can match. We allocate first to local hiring—shoreline restoration projects, boat repair training, raised walkway construction."
    hide mayor_rosa_alvarez
    show elias_eli_calder at right:
        zoom 0.7

    elias_eli_calder "So folks will have work that ties to the water—good. But will it feed the whole season? Will the pay match the danger of going back out on a boat a storm or two from now?"
    "Eli's question puts a fine point on the hidden calculus. You want to answer with data, with projected salaries and training timelines. You also want to pull him close and promise you won't let his family's livelihood be collateral."
    hide rina_park
    show mara_voss at center:
        zoom 0.7

    mara_voss "We can structure payments around the fishing season. Short-term stipends tied to restoration milestones. But that requires upfront disbursement and a local hiring guarantee."

    cassandra_cass_rey "We can draft that. Again—escalation risk is real. I'm offering a path that keeps both work and protections in motion, not in opposition."
    "The room fills with a thousand small barters—phrases trimmed for compromise, lines that soften hard edges. People who were opponents in the hallways trade language like currency. You sense the town convening itself into a bargain. It feels fragile and human."
    "After hours of argument, the council chambers thin. Outside, a sudden rain begins, a steady, soft percussion on the roof. The smell of wet wood and salt draws the meeting closer to the place it concerns."
    "This is the town making a hesitant step toward a future that might hold both jobs and marshes, if the law, money, and will align."

    elias_eli_calder "Whatever happens, Mara—choose with people in mind. Not just maps."
    "You close your eyes in the doorway and let the night wet your hair. His voice is not a command; it's a plea wrapped in love and fear. You think of Nia’s laugh and Tomas’s stories and the children who will paddle in places you can only hope to protect."

    mara_voss "I know."

    elias_eli_calder "I trust you— but I need to know we won't sign away the whole season for a half-promise."

    mara_voss "You won't be asked to pay that price. I won't let that happen."
    "He searches your face, unreadable for a beat that registers as a small betrayal of relief. Then he squeezes your hand and steps back into the room to find his uncle."
    # [Scene: Hallway outside Town Hall | Afternoon]
    hide cassandra_cass_rey
    hide elias_eli_calder
    hide mara_voss

    scene bg ch13_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant traffic on wet pavement; muffled debate inside]
    # play music "music_placeholder"  # [Music: Low mournful piano; a downward motif]
    "You stand beneath the eaves and open your notebook again. The lines you draw now are not just about hydrology or employment—they are the outlines of a life you might have to choose. You have spent"
    "your career translating raw data into moral stories that people can hold. Right now, the story you will tell tomorrow in signatures and clauses must reconcile hunger and habitat."
    show old_tomas_calder at left:
        zoom 0.7

    old_tomas_calder "Don't let them make the marsh a memory. But don't let good men go hungry either.' (He looks at the town as if seeing its bones.) 'We've learned to patch boats and hearts. Remember that."
    "His words feel like a benediction and a threat. You keep both."

    menu:
        "Call Nia and ask her to rally the youth":
            "You tap out a quick message to Nia asking her to gather youth for a visible presence at the signing. The idea lights her up; you can almost hear her footsteps as she promises to be there."
        "Sketch the oversight board's membership and circulate it to Rina":
            "You draft names—local fishers, a university hydrologist, a county rep—and slide the list under Rina's hand. She looks over it with a professional approval that feels like a small victory."

    # --- merge ---
    "You fold the notebook closed. The mediation tomorrow will press you to translate all these small, inevitable compromises into ink."
    # [Scene: Town Hall / Meeting Room | Late Afternoon — The Moment Before Signing]
    hide old_tomas_calder

    scene bg ch13_3be532_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rustle of coats, a camera shutter; the soft tap of a pen on paper]
    # play music "music_placeholder"  # [Music: A slow, descending string progression; the mood is heavy]
    "Mayor Rosa stands and addresses the room with the gravity of someone setting a course. Her voice carries the compromise’s weight: hope and loss braided."
    show mayor_rosa_alvarez at left:
        zoom 0.7

    mayor_rosa_alvarez "This amendment—if passed—freezes work in marked marsh cores, establishes a joint oversight board with veto authority for hydrological harm, and creates escrowed funds for transitional employment tied to restoration milestones. It allows non-core sections to proceed under strict monitoring."
    show cassandra_cass_rey at right:
        zoom 0.7

    cassandra_cass_rey "This keeps the town working and creates enforceable protections."
    show rina_park at center:
        zoom 0.7

    rina_park "With strict reporting, audits, and community hiring clauses."
    "Elias 'Eli' Calder watches you like a barometer. His jaw is set; his hands are still. The room hums with a thousand private reckonings."
    "You stand at the table. The packet is in front of you. The pen gleams. You can feel the weight of many lives pressing into your palm: fishers who need a fall season, kids who should"
    "know the marsh by name, elders who remember the sound of tides before machinery changed everything. You think of seedlings, of eelgrass, and of a town that might both survive and be altered."
    "You breathe, counting the inhalations like stitches."
    "In the front row a young woman clasps her child's hand; in the back, a man coughs and stares at the plan as if it were a verdict. Cass looks at you, expression complex. Rina’s face is focused; Tomas’s eyes hold a quiet sorrow."
    "You reach for the pen."
    "You pause—frozen between the act and the consequences—hands poised over the page, the rain outside soft as a held sigh."
    hide mayor_rosa_alvarez
    hide cassandra_cass_rey
    hide rina_park

    scene bg ch13_3be532_7 at full_bg
    "THE END"
    # [GAME END]
    return
