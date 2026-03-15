label chapter2:

    # [Scene: City Council Chamber | Afternoon]

    scene bg ch2_c4ca42_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, minor strings; a single slow pulse]
    # play sound "sfx_placeholder"  # [Sound: Murmurs, the rasp of knitting needles, an usher's cough]
    "You step through the doorway with the weight of the harbor still in your shoulders—salt in your hair, diesel on your boots, Nan's quilts folded against your arm. The room smells of old varnish and too-strong"
    "coffee; it feels colder than the pier, as if the air here has been filtered of the cove's salt and hope."
    "Rafi slides into the seat beside you, his hands already resting against the laptop like a mechanic ready at a console. Jonah stands a few rows back, palms buried in his pockets, jaw set. Gracie Nan"
    "occupies a public gallery seat near the back—her knitting is a bright island of color in the somber room. She watches you with an expression that is at once steady and worry-softened."
    "You can feel the town's eyes—friends, neighbors, people you grew up with—pressed into your back like a tide."

    scene bg ch2_c4ca42_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Click of a remote; the screen fills with glossy renderings of seawalls, raised berms, and neat rows of stilted housing]
    show evelyn_hart at left:
        zoom 0.7

    evelyn_hart "These proposals are built on models validated across comparable coasts. They deliver jobs, immediate protection, and investor confidence. We can keep Highwater Cove functioning—and fast."
    "Her voice is even. Her ice-blue stare is polite and measured; you register the way she names safety in spreadsheets and smiles at timelines. The renderings gleam with promise: clean lines, placard captions, artfully cropped before-and-after shots. There is power in that sheen. There is also distance."
    show mayor_lena_ortiz at right:
        zoom 0.7

    mayor_lena_ortiz "We appreciate the detail, Ms. Hart. We'll hear all sides today. Time is... limited."
    "You note the slight tremor at the corner of Lena's mouth when she says 'limited.' It's not anger—it's arithmetic: investors' deadlines, grant cycles, payroll. You know the timetable she carries has no sympathy for slow-growth healing."
    "Rafi taps the remote, and your tide observations bloom across the screen—handwritten curves smoothed into digital data. Your own handwriting is ghosting the projection, translated into charts that will be dissected and debated."

    menu:
        "Lead with the science: start with the data slide":
            "You step forward, fingers brushing the podium, and begin with the tide graphs. The room listens differently—numbers sharpen eyes and invite counters. The air tightens around the margins of policy and proof."
        "Open with testimony: tell Nan’s story first":
            "You clear your throat and begin with a memory: a house with windows like fishbones, Nan's laugh during the first after-storm. The room shifts—some faces soften, others frown. Emotion rearranges the debate into something less tidy."

    menu:
        "Catch Jonah's eye and give a small nod":
            "You catch his gaze and give a subtle nod. The gesture is a small current of solidarity; he returns a tight, grateful smile that doesn't answer the questions hanging between you."
        "Keep your focus on the council and let him speak alone":
            "You keep your eyes forward. His words land without your endorsement or interference—he speaks as himself and not as your reflection, which lets the council hear him differently."

    jump chapter3
    return
