label chapter17:

    # [Scene: Rebuilt Sea Wall | Dawn]

    scene bg ch15_714ff7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind skirling up the cliff, gulls urgent but hopeful, distant hammers finishing last bolts]
    # play music "music_placeholder"  # [Music: Rising orchestral swell — tense strings that resolve into a triumphant minor chord]
    "You smell the sea first — a clean, brine-sweet sharpness that has the power to wake memory. Under it is the new smell of resin and fresh-cut timber, and the faint, honest sweat of hands that"
    "have labored hard overnight. Your boots leave soft prints in the sand-grit. The locket against your sternum feels warmer than usual, as if the tiny map inside knows the new coastline better than you do."
    "People gather along the lip of the wall: a cluster of youth with rain-rough hands, Tala's movement-scarred organizers lined shoulder-to-shoulder, Ivy with paint still under her nails and a box of hot tamales. Old Man Rohan"
    "stands a little apart, watching the water like someone reading a long story he knows by heart. Councilor Nguyen is on the other side of the crowd, suit damp at the hem but eyes uncharacteristically bright."
    "Dr. Selene Park stands with her arms folded, AR spectacles pushed up on her head; her face is neat and controlled in the way of people who frame urgency as metrics."
    "Mateo Ríos arrives from the promenade with a rolled waterproof tube tucked under his arm. He comes to you like a tide comes in—inevitable, steady, and a little breathless from the climb. When he reaches you, his palms are warm and smell of coffee and salt."
    show mateo_ros at left:
        zoom 0.7

    mateo_ros "You did the right thing, Aiko. Whatever else happened, this—this is proof that people can make a line that holds."
    "You let the sentence land. It is big and soft and a little frightening in its simplicity."
    show aiko_navarro at right:
        zoom 0.7

    aiko_navarro "We made it with hands, not algorithms. But we couldn't have done it without the funding that got us the materials. We turned money into scaffolding, but the shape was ours."
    "Mateo Ríos studies the crowd, then you. His voice drops to the intimate space of two people carrying the history of many tides."

    mateo_ros "I lied when I said I could do both the meetings and the on-ground work. I tried. I failed sometimes. But I kept coming back."
    "You want to list all the ways both of you have failed and tried better; to name the nights of silence, the missed calls, the times you both let practicalities push tenderness into margins. Instead you"
    "breathe and let the morning simplify things like light over salt: what matters is here, now."
    hide mateo_ros
    hide aiko_navarro

    scene bg ch15_714ff7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The tide thumps against the new wall; a ceremonial bell rings once, then twice]
    "Councilor Nguyen steps forward to the temporary podium, paper damp in his hand but voice steady, a political cadence softened by genuine relief."
    show councilor_nguyen at left:
        zoom 0.7

    councilor_nguyen "This wall won't be the end of our work. It's a line, not a destination. We'll continue audits, we will support managed retreat where needed, and—' (he looks at Dr. Park; the look is not accusation but requirement) '—we'll hold anyone who builds for us accountable."
    "Dr. Selene Park's jaw tightens. For a beat her expression is the careful, corporate mask you've seen in meetings and interviews. Then something like exhaustion flickers there, and when she steps forward her tone is less metallic."
    show dr_selene_park at right:
        zoom 0.7

    dr_selene_park "Science should serve people. I apologize for where my team's speed eclipsed listening. We will collaborate on community-led monitoring. We will open our data sets. We'll fund the youth apprenticeships Rohan proposed."
    show tala_kumari at center:
        zoom 0.7

    tala_kumari "Words are easy, Selene. We want action—training, jobs, community oversight. No more one-way contracts."

    dr_selene_park "And you'll have it. Signed audits and community seats on the oversight board. No backdoors."
    "The crowd murmurs—a cautious cadence of relieved distrust. The exchange is not clean; it never is. There are interruptions, quick rebuttals, and a half-second where the room could spin back into old antagonisms. But the tide"
    "of conversation is different today: bracing, rigorous, held open by committees and signed terms rather than by a single, unanswerable promise."

    menu:
        "Step forward and accept Dr. Park's handshake":
            "You step forward, palm open. Dr. Park's hand is cool, efficient. For a flash you see the scientist behind the suit — the tired certainty that fixes can be offered. The crowd watches; acceptance feels like buying a hard-won truce."
        "Keep your hands folded, voice the community's demand for oversight":
            "You keep your hands crossed over the locket and speak. Your words are blunt and public: training, paid roles, full data transparency, community veto on biotech trials. The room leans in; your demand clarifies what 'collaboration' must mean."

    # --- merge ---
    "Narrative continues with the crowd reacting and the chapter proceeds."
    "Mateo watches you choose. He doesn't move—he's learning the cadence of your ethics and the way you refuse to let the easy compromise stand unexamined. Whatever you did, he reads it and nods like someone who recognizes what it means to be accountable in public."
    # [Scene: Marsh | Midday]
    hide councilor_nguyen
    hide dr_selene_park
    hide tala_kumari

    scene bg ch15_714ff7_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Laughter over spatters of mud, the soft sucking of boots, Rohan's voice giving instruction]
    # play music "music_placeholder"  # [Music: Quick, rhythmic percussion — forward-driving, bright]
    "The marsh is work in the recomposed sense of the word: messy, communal, satisfying. Old Man Rohan stands at the head of a small line of teenagers, demonstrating a planting motion that looks almost ceremonial when"
    "he does it. His hands are patient; his instructions are small and full of lore."
    show old_man_rohan at left:
        zoom 0.7

    old_man_rohan "Plant where the tide will leave a kiss, not a choke. Muscle and timing. You try, little one."
    show aiko_navarro at right:
        zoom 0.7

    aiko_navarro "You watch the kids mimic Rohan's hands — awkward at first, then smoother. You think of your mother's shoreline and the small rituals that kept the place fed. You write notes in your mind more than your notebook: who learns fastest, who needs more time, where the mollusks reappear."
    "A youth asks how the new sea wall will change the marsh. Rohan replies not with charts but with memory, telling of a time when the salt flats were truer mudflats and fish came in different"
    "patterns. The lore is not contradiction to science; it frames the data, gives it context."
    show ivy_navarro at center:
        zoom 0.7

    ivy_navarro "You kept your promise, sis. We're paying for some of it with our backs, but—' (a grin) '—the takis at the volunteer tent are worth it."
    "You laugh, the sound a sudden unplugging. It is small and human and necessary."
    hide old_man_rohan
    show tala_kumari at left:
        zoom 0.7

    tala_kumari "We secured apprenticeship stipends. Council will bill part of Selene's fund to the community oversight line. Mateo pushed the final motion in the meeting last night."
    "Tala's news hits like warm sunlight. You nearly feel dizzy with the accumulation of small victories that read like policy but feel like rescue."
    # [Scene: Community Gardens / The Aquarium | Afternoon]
    hide aiko_navarro
    hide ivy_navarro
    hide tala_kumari

    scene bg ch15_714ff7_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A kettle steaming, the murmur of a hundred small conversations, a radio playing a local folk tune]
    # play music "music_placeholder"  # [Music: Lighter strings, a motif of hope]
    "Inside the Aquarium the atmosphere is intimate. People bring food, tools, children, petitions. A bulletin board lists jobs and apprenticeships, names scrawled next to roles. A notice of community audits is posted in block letters. The hub hums."
    "Dr. Selene Park sits at a corner table with Mateo Ríos and you. For once, her posture is less combative; she looks unsettled but committed."
    show dr_selene_park at left:
        zoom 0.7

    dr_selene_park "There are things I still don't see the way you do. Place-based memory is not an input I learned to weight equally. But the models are better when you add them. I owe you that acknowledgement."
    show mateo_ros at right:
        zoom 0.7

    mateo_ros "And we owe you the technical resources to scale things safely. We both make mistakes, Selene. We just need to learn faster."
    "The conversation loops—question, answer, counterpoint—longer than the brief politeness in council chambers. This is where policy becomes practice. You press details like a literal person: apprenticeship wage lines, community veto procedures, scheduled open-data dumps. Selene answers, sometimes haltingly, sometimes definitively. You demand clarity; she provides it."
    show aiko_navarro at center:
        zoom 0.7

    aiko_navarro "We will hold the data public, we will have quarterly reviews, and we will staff a liaison from the Aquarium for community oversight. Done."
    "She drops her eyes for a second and then nods."

    menu:
        "Propose a permanent joint position between your team and Dr. Park's firm":
            "You outline the job: co-technical officer, paid, community seat on the board. Selene hesitates, then accepts the proposal on paper, surprised to find that binding structures can be the scaffold for trust."
        "Keep oversight in the hands of a rotating community committee":
            "You suggest rotating oversight to keep power local. The community cheers at the thought of continuous engagement. Selene agrees to fund training for the rotation. The governance feels less stable but more democratic."

    # --- merge ---
    "Conversation continues with agreed governance and training plans."
    "Mateo watches you not as a planner across a table now, but as the person who carries the town's stubbornness and tenderness in equal measure. He slides his hand across the table and brushes yours—brief, grounding."

    mateo_ros "You'll come with me to the municipal symposium in three months, right? Even if it's just for the day? We can push for seed funding for the next cohort."

    aiko_navarro "I'll go. And we'll set up the first remote check-ins. If things go well, maybe… we'll split the oversight between here and the city team."
    "He lets out a breath that is almost a laugh. It is not a proposal of forever exactly, but it is a promise to try—and in this climate, the word 'try' is everything."
    # [Scene: Cliffside Promenade and Old Sea Wall | Evening / Storm-Test]
    hide dr_selene_park
    hide mateo_ros
    hide aiko_navarro

    scene bg ch15_714ff7_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low, building thunder; the wall creaks with the first real test; radios crackle with counts]
    # play music "music_placeholder"  # [Music: Full-band surge — drums and brass pushing the climax]
    "The final test arrives with a deliberate, remorseless tempo: a storm front collides with the bay and throws itself against the new engineering. It is the moment you have trained for in everything from town drills to whispered late-night calculations. Every pair of hands counts."
    "Volunteers run sandbag relays. Mateo Ríos calls coordinates into a radio. Tala organizes evacuation lanes for small boats and lines up the youth for emergency shifts. Rohan stands at the planting beds, directing a team re-tying"
    "the lower belts of cordgrass to prevent undercutting. You are everywhere at once by being exactly where you're needed."
    show aiko_navarro at left:
        zoom 0.7

    aiko_navarro "Your pulse is a drum under your ribs. You can taste salt and adrenaline and the ink of your notebook in the pocket of your coat. Moments compress into a sequence: shout, adjust, tie, breathe. The arousal you felt the night of the old storm returns — fierce, bright, urgent — but now tempered by the scaffolding of plan and the shoulders of many people."
    "A wave hits the wall—a tall, theatrical rolling mass tipped with white. It slams and the new anchors shudder, but they hold. The spray arcs high, painting everyone's faces with tiny, dazzling salt flecks. Cheers are half disbelief, half release."
    show old_man_rohan at right:
        zoom 0.7

    old_man_rohan "It's holding! Keep the lines tight! Plant placement three meters from the base! Move!"
    "There is a collective sound like exhale. And then: work. Patching, checking, retying—practical acts of mercy that feel like prayer. Mateo Ríos finds you amid the chaos, his sleeve torn, his mouth an exhausted grin."
    show mateo_ros at center:
        zoom 0.7

    mateo_ros "You held us together."

    aiko_navarro "We held each other. We made the wall and the places below it talk to each other."
    "He takes your hand in both of his. The grip is simple and absolute."

    menu:
        "Pull Mateo into an all-consuming embrace":
            "You step forward and hug him. It's fierce and desperate and clean. For a second you both are only two bodies in the middle of the storm, and the world narrows to the breath between you."
        "Lean in close and make a plan for the weeks ahead":
            "You lean in and speak logistics, softer and steadier than the wind: apprenticeship rollouts, a schedule for audits, a rotation for oversight. He listens, and in listening you both make space for the future."

    # --- merge ---
    "After the moment, the night continues with communal tasks and celebration."
    "The night ends in the way major nights do: in small tasks and unorangized joy. Someone starts a handclap, then a song, then an impromptu feast in the Aquarium's restored hall. The community gardens glow under"
    "string lights. Children run with mud on their faces. Rohan teaches a teen to knot a planting line and then, in a softer voice, points to the water and says something that is less about tides"
    "and more about memory."

    old_man_rohan "We plant so those who come after won't spend their youth learning what we forgot. It's a passing on, not a keeping."
    "You sit on the promenade with Mateo at your side, the locket between your fingers. He leans his head on your shoulder the way old friends do—relieved, tentative, certain. Around you are the small, human proofs"
    "of what you all did: apprentices with new tools, government memos with teeth, a corporate director who now funds training, and a town that has shifted its axis without losing itself entirely."

    aiko_navarro "You feel a bright warmth unclench in your chest. The ending is not a cinematic silence but an ongoing list: names to call in the morning, repairs to schedule, meetings to hold, love to tend. You have not fixed the world. You have, instead, built a better room from which to keep fixing it."

    mateo_ros "Whatever comes next, we'll call each other. We'll keep it honest."
    "You slide the map locket back under your shirt and let the motion be ritual rather than panic. The sea still breathes. The work stretches ahead. But for the first time in a long time the horizon looks like an invitation, not a threat."
    # [Scene: The Aquarium | Night — Quiet After]
    hide aiko_navarro
    hide old_man_rohan
    hide mateo_ros

    scene bg ch15_714ff7_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low conversation, a baby fussing, a kettle cooling]
    # play music "music_placeholder"  # [Music: Gentle piano motif resolving the chapter's themes into a warm cadence]
    "People drift in and out of the Aquarium's rooms. You stand for a long minute by the window and watch young hands tying a buoy line. Tala sits opposite you with two mugs of tea. She hands you one with a small, fierce smile."
    show tala_kumari at left:
        zoom 0.7

    tala_kumari "You asked for everyone to have a voice. Look at that list.' (she nods at the job board) 'We didn't get everything; we got names and wages and the start of oversight. That's a start."
    show aiko_navarro at right:
        zoom 0.7

    aiko_navarro "It's more than a start. It's—"
    "(you catch yourself)"

    aiko_navarro "—it's proof that small-scale things can change big things, if you make them stick."

    tala_kumari "And you made people keep them sticky."

    aiko_navarro "The praise is not for you alone; it's for the communal elbow grease of every person who carried buckets when the tide rose. You let the compliment sit because sometimes acceptance is part of being carried back."
    "You walk the Aquarium's hallway one last time before bed, fingers touching tile murals that show a stylized coastline. The image has been repainted with new plants and new names. You smile at it like a benediction."
    hide tala_kumari
    hide aiko_navarro

    scene bg ch15_714ff7_7 at full_bg
    # play music "music_placeholder"  # [Music: A single, sustained chord that blooms into a soft, bright resolution]
    "You think of the endings that were possible and the ones you chose between: rescue without relation, stubborn local resistance that broke hearts, compromise that saved some and cost others. Tonight those binaries feel stitched together"
    "into something strange and sturdier—an imperfect synthesis that still allows for love and work and the slow, delicate repair of place."
    "People chant in the distance—half-celebration, half-prayer. You answer with the quiet work of patching and planning tomorrow: a list of names, a timeline for apprenticeships, and a promise to keep the data open. The town will"
    "sleep a little easier. The marsh will have a better chance. Your relationship with Mateo will keep shifting—sometimes present, sometimes distant—but held by more than inertia: by deliberate, repeated acts of care."

    scene bg ch15_714ff7_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Tide, a single gull, the murmur of the town settling]
    # play music "music_placeholder"  # [Music: Resolving theme — gentle, hopeful strings]

    scene bg ch15_714ff7_9 at full_bg
    "THE END"
    # [GAME END]
    return
