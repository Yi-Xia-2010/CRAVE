label chapter10:

    # [Scene: Mature Mangrove Fringe | Morning]

    scene bg ch9_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, soft chatter, the whisper of leaves in warm wind.]
    # play music "music_placeholder"  # [Music: Gentle, rising acoustic motif]
    "You inhale the brackish air and let it fill the space where a decision once sat heavy in your chest. You can still feel the pressure of that night—the council room, the pause in Mayor Cortez's"
    "face when you asked for time—and the compromise that pushed the town toward both temporary protection and a patient restoration. That choice felt like a rope thrown between two shores; now you stand on the shore"
    "that the rope helped steady."
    "Mud slaps softly against your boots when you take a step forward. The saplings you once planted with blistered hands have grown into a fringe of glossy leaves and knotted roots. Crabs scuttle like punctuation marks."
    "Small fish flash in the shallow channels. Each root is an argument against forgetting: for every meter of green, someone remembered to show up."
    "Sora Lin is kneeling ahead of you, sleeves rolled, palms coated in the smell of wet earth and mangrove. They look up and grin—uncontained, the grin of someone who believes this morning is proof."
    show sora_lin at left:
        zoom 0.7

    sora_lin "Look at them. They keep quiet when storms come now. Like they learned to hold their breath."
    "You smile—an automatic, incredulous thing. Your throat tightens with a combination of relief and something lonelier: the image of the families who had to work through relocation plans, the houses that couldn't be lifted in time."
    "Those losses are not the absence of victory; they are the price that made this victory complicated and real."
    "You kneel beside Sora Lin and let your fingers find the cool, tethered root. It feels like touching the outline of a promise."
    show aria_navarro at right:
        zoom 0.7

    aria_navarro "We did the work. The town did the work. The levees bought us the breathing room we needed to let this grow."

    sora_lin "You did a lot of the talking, though. Quiet arias are still the most persuasive."
    "They nudge you with an elbow, teasing, but their eyes hold something private—an acknowledgment of the nights you stayed up rewriting grants and the mornings you led volunteers before the tide came in. Your chest expands"
    "with a warmth that is not pride so much as the steady heat of a pot left on low flame."

    menu:
        "Kneel and check the root anchor":
            "You sink lower, the mud cooling under your knees. You trace where several saplings entwine and feel the reassuring tangle—evidence of months of hands, of learning. Sora hums softly beside you, counting off species names like small love notes."
        "Stand and let Sora keep working while you watch":
            "You step back and cup your hands around your mouth, scanning the shoreline where small figures move—volunteers planting, kids carrying painted stakes. Watching feels like another kind of tending. Sora catches your eye and grins, then goes back to the work as if your silence is permission."

    # --- merge ---
    "Sora leans back and wipes their hands on their sarong, crumbs of mud like medals."

    sora_lin "You know what the kids said the other day? 'When the trees are old, will they sing us the tides?'"

    aria_navarro "They already do. They teach us to slow down."
    "The two of you sit for a moment in the green-filtered silence, letting birds stitch the morning together. This is small-scale triumph made visible: soil held, water slowed, families who once feared the next season's storm naming places they belong."
    # [Scene: Reclaimed Shore | Afternoon]
    hide sora_lin
    hide aria_navarro

    scene bg ch9_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmurs of a gathered crowd, a ceremonial bell, a distant thump of a generator paired with children's laughter.]
    # play music "music_placeholder"  # [Music: Warm strings swell beneath a hopeful flute line]
    "The mayor's tablet gleams for a second in the sun as Mayor Isla Cortez steps forward, the weight of governance softened in her expression. Elena stands close to you, hands folded, the map of the town"
    "etched into the lines of her palms. Her face is steady; her pride is quiet but unmistakable."
    show mayor_isla_cortez at left:
        zoom 0.7

    mayor_isla_cortez "This is not a moment for speeches about what we almost lost. It's a moment for how we will live with what we have rebuilt. Today, the council ratifies the stewardship clause: the models, maintenance, and funds will be co-managed with the community council you proposed."
    "A ripple of applause moves like tide through the gathered people. You feel it like a current: small hands clapping, Jun's eager whoop in the back, a fisherman's brief bark of approval. For months you cataloged"
    "soil tests, maintenance hours, seedlings per volunteer. Today you witness that ledger turned into law and trust."
    show aria_navarro at right:
        zoom 0.7

    aria_navarro "We will set the maintenance rotations. We will teach, and we will measure. But we will also listen—Elena's histories, the fisherfolk's changes, the children's maps. This is not just a project; it's our responsibility."

    mayor_isla_cortez "You brought them both: the data we can justify publicly and the stories that made people want to show up. It's the marriage we needed."
    "There is a small, private exchange happening between you and the mayor: gratitude boxed in civic language. You see the constraints she wore like a second skin—budget spreadsheets, emergency alerts, political pressure—and how she chose to"
    "slip the rope in your direction. The compromise you once feared has become a lever."
    "Elena steps forward, her voice a boat pulling the room closer."
    show elena_navarro at center:
        zoom 0.7

    elena_navarro "We lost porches and oysters. We gained people who won't let go of each other. Keep the names on the stakes. Teach them the old songs so the children can remember the tide by heart."

    aria_navarro "We will. And we'll make sure those who move do it with choice, not desperation."
    "Elena's eyes — the same eyes that taught you tides by the thickness of someone's hands — glisten but are calm."

    elena_navarro "Then it's done, niña. Your father would be proud to see you using both your hands."
    "The crowd breaks into softer applause, and Sora Lin's hand slips into yours, grounding you even as the ceremony unfolds. You feel the town pivot on a new axis: relocation plans executed with dignity, policy hammered"
    "to hold community voices, and a living shoreline that will teach future generations how to stand."

    menu:
        "Step forward to accept the mayor's handshake":
            "You take Isla's hand, your palm a little clammy. The handshake is brief, practical, and warm enough to leave you steady. Council members murmur approval. Elena gives you an approving nod—too small to be anything but everything."
        "Turn and hug Sora instead, letting the crowd watch":
            "You fold into Sora like a wave into a bay. Their shoulder is salt-warm. The crowd quiets for a second. Someone laughs—soft and relieved—and the moment feels like a promise made aloud."

    # --- merge ---

    "Mayor Cortez" "We will also fund a small visiting consultancy program so local knowledge can be shared with other towns without stripping you of agency. The pilot will be led by your council, Aria."

    "Mayor Cortez" "We will also fund a small visiting consultancy program so local knowledge can be shared with other towns without stripping you of agency. The pilot will be led by your council, Aria."

    aria_navarro "If we teach others how to avoid the mistakes we made, maybe fewer places will choose temporary fixes without community consent."

    mayor_isla_cortez "Exactly. Your model will be a blueprint, not a takeover."
    "The words land like comfortable tools being handed to you: a grant, a public guarantee, a municipal promise to listen. They are pragmatic solutions stitched to long-term stewardship."
    # [Scene: Old Quay | Evening]
    hide mayor_isla_cortez
    hide aria_navarro
    hide elena_navarro

    scene bg ch9_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Laughter, the low rhythm of an improvised drum, the soft clinking of glasses.]
    # play music "music_placeholder"  # [Music: A fuller arrangement—strings and soft percussion—rises into hopeful warmth]
    "The evening is a kind of thanksgiving that neither erases pain nor pretends everything is the same. People tell stories: how a neighbor helped build an elevated pantry, how a fisherman taught a class of kids"
    "to read tide tables by the color of the water. The quay smells of broth, citrus, and wood smoke—comfort rendered in simple ingredients."
    "You and Sora Lin walk along the edge, boots leaving faint imprints on damp planks. Children run past, chasing a kite that refuses to stay grounded. For a beat the town is simply whole."
    show sora_lin at left:
        zoom 0.7

    sora_lin "You get to be the odd one who speaks in maps now. Are you ready for people to ask for you everywhere?"
    show aria_navarro at right:
        zoom 0.7

    aria_navarro "I've never liked 'everywhere.' But I will go when the town asks. I will consult, teach, and come back."

    sora_lin "Come back."
    "There is no demand in that single word—only the careful placing of a hope into the world."

    aria_navarro "There are grants that will want me to travel longer, conferences that want the story packaged a certain way. I will go when it helps us—when it brings resources that keep people here by choice. I won't disappear."

    sora_lin "Good. Because if you miss the next victory party, I will stage a very bad DJ set and personally shame you."
    "You laugh—relief spilling out. The laughter is a small, human sound against the vastness of what you've done. It is not oblivious; you both know there will be days when tides won't be so gentle and"
    "months when the ledger will look thin. But the foundations have shifted: the town has instruments to measure, a law to bind stewardship, and a public memory to hold leaders accountable."
    "Elena joins you at the rail, watching the children plant another stake—bright blue, hand-lettered."
    show elena_navarro at center:
        zoom 0.7

    elena_navarro "You didn't do it alone, niña. You never did. You found a way to make folks who used to argue over mooring spots argue about who gets the next rotation instead."

    aria_navarro "We argued for better things."

    elena_navarro "That's the way. And don't be afraid to go. We will have good hands here."
    "You look out at the harbor—boats bobbing like punctuation between the reclaimed shore and the sea. The mangrove fringe stands as a new border: it will not stop every storm, but it will slow things down, hold sediment, and—over generations—rebuild what was lost."
    "The town's model is already being requested by neighboring communities. A small delegation visited last month to learn the maintenance rota, the co-governance agreements, the community education program you designed with Sora Lin's art tactics. Your"
    "work has become replicable without being extractive—a difficult balance you fought for and mostly kept."
    "You feel the old guilt—that tug toward taking every burden alone—soften into something steadier: stewardship shared. It is the difference between carrying everyone on your back and building a bridge so others can cross together."
    "Sora Lin presses their forehead to yours for a breath, a private punctuation."

    sora_lin "So. Onwards—plans, travel, bad DJs, mangrove anniversaries. Together, however that looks."

    aria_navarro "Together."
    "You let the word sink in, not as a tidy ending but as an honest shape of the life you will weave: travel that brings resources, homecomings that are sacred, and a town that can now claim and care for its own future."
    hide sora_lin
    hide aria_navarro
    hide elena_navarro

    scene bg ch9_3be532_4 at full_bg
    # play music "music_placeholder"  # [Music: The motif swells into a hopeful chord, then settles into a warm, sustained note]
    # play sound "sfx_placeholder"  # [Sound: The sea in the distance, steady and patient]
    "You close your eyes for a second and feel, beneath everything—beneath the law, the seedlings, the practical plans—the quiet work of relationship and trust. There is loss that will not be erased, names that will not"
    "be recovered, memories that sting. But there is also a living answer: the community chose its path, did the labor, and made room for both protection and restoration. You have learned that saving a place is"
    "not choosing between concrete and roots; it's choosing people and the things that let them stay."
    "You open your eyes and Sora Lin squeezes your hand. Elena's laugh bubbles up near the market. Mayor Cortez catches your gaze and gives a small, human nod. The tide has pulled you forward a little further than you imagined when you first came home."

    scene bg ch9_3be532_5 at full_bg
    # play music "music_placeholder"  # [Music: Gentle theme lingers, then fades out]

    scene bg ch9_3be532_6 at full_bg
    "THE END"
    # [GAME END]
    return
