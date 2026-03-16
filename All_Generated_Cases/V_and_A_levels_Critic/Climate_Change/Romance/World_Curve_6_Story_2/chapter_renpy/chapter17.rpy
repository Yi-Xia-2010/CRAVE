label chapter17:

    # [Scene: Abandoned Lighthouse | Dawn]

    scene bg ch15_3be532_1 at full_bg
    # play music "music_placeholder"  # [Music: Slow, low cello with soft, sustained notes]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, a rope tapping gently against rail; faint lapping of water below]
    "You wake before the bell. The lighthouse holds its breath in the thin hour when the sea is neither dark nor day; the air tastes of old rope and wet concrete. Your hair is still damp"
    "from the early mist; the fringe stuck to your forehead, the scarf knotted tight against the chill. Your compass rests warm against your sternum, an almost-living weight that knows the map of this town better than"
    "you do right now."
    "You move without hurry because you cannot speed a leaving. Every motion is precise, as if slow hands might fold time differently: the waterproof notebook slips into its pocket, the brass compass settles in the hollow"
    "of your palm, the chipped shell pendant bobs against your collarbone. You pause to button the windbreaker, to tuck the scarf so the cold won't pry loose the edges of decision. Outside, a gull's cry cracks"
    "the hush. Inside, the lighthouse creaks the language of things held together for too long."

    scene bg ch15_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A soft intake of breath from someone at the door]
    "Abuela Rosa steps in like a warm shadow. Her braid is silver against her back; she carries a small coil of braided rope and a square of paper folded until its creases have softened. She sets"
    "them in your hands with a gentleness that knows how much these small things can weigh."
    show abuela_rosa at left:
        zoom 0.7

    abuela_rosa "You look faraway, niña."
    "Her voice is steady, the kind that has kept a house warm through storms. 'You have the look of someone carrying other people's weather.'"
    show mara_serrano at right:
        zoom 0.7

    mara_serrano "You try to laugh, but it comes out small. You trace the rope with a fingertip, feeling the rough twist of fiber that held nets and lives and now promises."
    "You fold your hands around the rope as if to anchor yourself."

    abuela_rosa "It will do what rope does. It ties. It holds. It remembers."
    "She looks at the compass, then at your face. 'You go because you are needed where the storms are not just ours. That is not leaving them to drown. It is carrying their names somewhere they might be heard.'"
    "Her words are not comfort exactly; they are the small truth you have tried to say to yourself for weeks. They land, heavy but honest. Outside, a gull skims low, and the town beyond the bluff"
    "is a ragged line of roofs and patched walkways. The Marketboard's flags are asleep from last night's arguing."

    menu:
        "Tie the rope around your pack now":
            "You loop the braided rope around your shoulder strap, the fibers biting into the canvas—practical, sharp, a decision made. It feels like fastening a promise."
        "Fold the rope and keep it in your pocket":
            "You fold the coil small and tuck it into an inner pocket. It is closer there—private, like a word you are not ready to say aloud yet."

    # --- merge ---
    "Continue"
    hide abuela_rosa
    hide mara_serrano

    scene bg ch15_3be532_3 at full_bg
    # play music "music_placeholder"  # [Music: The cello thins; a single piano note underlines the silence]
    # play sound "sfx_placeholder"  # [Sound: Footsteps on stone, the whisper of fabric]
    show elias_park at left:
        zoom 0.7

    elias_park "I thought you'd sleep in. I left you a thermos down by the quay. Thought you might need something that's not meeting-chill."
    "You feel grateful and raw at the same time—grateful for the small domestic thought, raw because those soft things have become rare currency between you both."
    show mara_serrano at right:
        zoom 0.7

    mara_serrano "I didn't sleep. I kept thinking—different people, different calculations. The models, the meetings... they don't hold the hands we are trying to save."

    elias_park "None of them do. But they can buy us time. Sometimes time is what grief looks like when it's trying to be useful."
    "He stops and looks away a moment; when he turns back his voice drops. 'I could have argued harder. I could have shouted until the roof came down. I didn't.'"

    mara_serrano "You did what you thought would cause least harm. You still—"
    "Your voice narrows; the accusation isn't cruel, it's the weight of things unsaid. '—you still talked to contractors. You still kept investor calls late in the night.'"

    elias_park "I did. And I kept thinking we could fold them into something better. I wanted to build with you, Mara. I... I wanted to be the person who makes things that keep people here."
    "He exhales and looks at the compass around your neck. 'But the work we kept doing in secret, the compromises... they changed the town while we held our breath. I'm sorry.'"
    "The word is small, exact. He doesn't ask you to stay. He doesn't demand you leave. He says apology in the thin light of morning and it neither fixes nor breaks the knot between you."

    menu:
        "Press him to admit what he won't say":
            "You step closer, forcing the edges of his silence into a shape. He blinks, unready, and then admits—slow and honest—that he feared losing you to the fight more than he feared losing the fight itself."
        "Let him keep his words small":
            "You step back and let the silence breathe. He reaches for your hand and you let him, because some things are too big to pry loose with talk."

    # --- merge ---
    "Continue"
    hide elias_park
    hide mara_serrano

    scene bg ch15_3be532_4 at full_bg
    # play music "music_placeholder"  # [Music: Cello returns, slow and steady, like the unhurried rise of tide]
    # play sound "sfx_placeholder"  # [Sound: The town's distant murmur, a bell from the harbor—irregular, like a heart skipping]
    "The conversation loosens and tightens like tide lines. You speak about policy memos you will write, the places you have been invited to testify, the names of committees and coalitions that sound abstract and hopeful. Elias"
    "speaks about sensors and retrofits, about the possibility of a monitoring network that could save other towns if it is done right. Abuela offers practicalities—sardines packed in oil for travel, a list of people to call"
    "in the market, a shawl she will miss seeing you in."
    show elias_park at left:
        zoom 0.7

    elias_park "Will you come back?"
    "He doesn't frame it as a plea but you hear it that way."
    "You feel the question like a wind that pulls at the edges of your resolve. You could promise many things and mean half of them. You could make a vow and watch the tide take the other half."
    show mara_serrano at right:
        zoom 0.7

    mara_serrano "I don't know."
    "You place the compass in his hand for a moment, feeling the cool brass. 'I will try. I'll write. I'll send the models and the notes. I will—'"
    "The sentence thins; the rest is private."

    elias_park "Mara."
    "He reaches, and there is a hand cupped to your face that remembers every weathered nick on your cheek from when you were small and reckless on the rocks. 'Promise me you'll be careful. Not just for your work. For you.'"
    "You close your eyes at the memory in his palm, the way he had once steadied you while you climbed a broken jetty. The compass is warm against your skin; the town outside seems to hold its breath with you."
    show abuela_rosa at center:
        zoom 0.7

    abuela_rosa "Carefulness is a good thing. But so is doing the hard thing. Bring back what you learn. And come home if you can."

    elias_park "I'll send updates. And—"
    "He swallows. 'If we find a way to do this right—your path, my work—maybe the town will have both. Maybe you'll come back to a place that's been cared for.'"

    mara_serrano "Maybe."
    "The word is small enough to keep. It holds both a hope and an admission."
    hide elias_park
    hide mara_serrano
    hide abuela_rosa

    scene bg ch15_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A single bell from the harbor, low and forgiving]
    "You should be packing more; everything you need is both less and more than an old bag can hold. You fold the scarf again, smooth the map remnant into the notebook, slip Abuela's rope either into the pack or around its strap—actions that are ritual and also economize feeling."

    menu:
        "Leave the map visible, stick it in the front of your notebook":
            "You slide the map remnant into the notebook's first page, its edges peeking out like a promise. Every time you open it you'll have the coastline to come home to."
        "Hide the map deep inside the notebook":
            "You tuck it into a deep pocket, private and protected. Some things are safer when you keep them held close."

    # --- merge ---
    "Continue"

    scene bg ch15_3be532_6 at full_bg
    # play music "music_placeholder"  # [Music: A single cello note held, gradually resolving into silence]
    # play sound "sfx_placeholder"  # [Sound: Your boots on the worn stones; the distant murmur of market-board voices waking]
    "Abuela Rosa walks you to the edge of the path, her fingers steady on your shoulder. Elias lingers a step behind, watching until watching is too much and he turns away to let you go."
    show abuela_rosa at left:
        zoom 0.7

    abuela_rosa "You carry rope and chart and compass. But remember—home is where people make the shore livable. You go carry a story, not a savior."
    "A small, wry smile. 'And write to me. I will keep a kettle on.'"
    "You fold your face into the warmth of that small joke and let the first honest tear fall. It is not a dramatic break; it is a single, honest salt bead like the others that have collected on your skin over the last months."
    show elias_park at right:
        zoom 0.7

    elias_park "I love you. I didn't say it enough while we argued about piles and planters and permits. I didn't—"
    "He stops, because words would complicate the cleanness of this leaving. 'I love you.'"
    "You answer with a motion that is not quite a hug and not quite distance, something made of years and of the town's weary hope. There is no neat reconciliation. There is only the slow, honest admission that love can be both motivation and undoing."
    show mara_serrano at center:
        zoom 0.7

    mara_serrano "I love you too."
    "It lands like a pebble in still water; the ripples are small but true."
    hide abuela_rosa
    hide elias_park
    hide mara_serrano

    scene bg ch15_3be532_7 at full_bg
    # play music "music_placeholder"  # [Music: The cello fades into a single, sustained wind chord]
    # play sound "sfx_placeholder"  # [Sound: The breath of wind against your scarf; the harbor bell one last time]
    "You step away from what you know. Your boots find the path; the town's shape tightens into memory—the Marketboard's awnings, Mateo's lean silhouette at a dock, the salt-streaked banners. Your compass presses against your heart, warm"
    "and steady. The coil of rope is in your pack—the braided texture a small thing to remember when the world wants you to be otherwise."
    "You do not look back until the path levels and the lighthouse is only a white line against the sky. When you finally turn, you do it not with anger but with a heavy, precise grief."
    "It is the grief of someone who knows that some battles are best fought from far away, who knows the cost and pays it because the fight is bigger than the place."

    scene bg ch15_3be532_8 at full_bg
    # play music "music_placeholder"  # [Music: A gentle, low drone that threads into silence]
    # play sound "sfx_placeholder"  # [Sound: The sea, steady and indifferent; a gull that sounds like an old friend calling]
    "You will write letters. You will send models and memos and the names of the reefs that need saving. You will carry the town in your work and in the small coil of rope. This leaving is both an ending and the beginning of another way to keep watch."
    "You step beyond the last bend and the scene closes around the quiet certainty of your choice."

    scene bg ch15_3be532_9 at full_bg
    # play music "music_placeholder"  # [Music: Cello resolves into a single, breath-held chord then fades]
    # play sound "sfx_placeholder"  # [Sound: Silence, soft and complete]

    scene bg ch15_3be532_10 at full_bg
    "THE END"
    # [GAME END]
    return
