label chapter6:

    # [Scene: Boardwalk | Dawn]

    scene bg ch6_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm strings, steadying piano; a gentle swell that suggests relief and forward motion]
    # play sound "sfx_placeholder"  # [Sound: Paper rustle, distant motor of a small boat, the soft slap of water against pilings]
    "You can feel the bay's breath — a cool, briny inhale that carries peat and the last of last night's rain. The signing table smells faintly of coffee and wet wood. Around you, neighbors cluster in"
    "rings: hands tucked into sleeves, scarves bunched, faces wet with sleep and something like hope."
    show jonah_hale at left:
        zoom 0.7

    jonah_hale "We've inserted the community oversight clause. Quarterly audits, an independent technical panel, and a legally binding trust to secure long-term residents' property rights. Targeted reinforcements will only go where critical infrastructure is at risk — docks, the desal plant, the ferry approach. The rest will follow living, adaptive designs."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "And the trust — the language protects families who have been here for generations? No loopholes that let developers buy in and flip properties?"

    jonah_hale "No loopholes. It's explicit. Transfers require community council approval for a decade. We made it durable."
    show mayor_lin_park at center:
        zoom 0.7

    mayor_lin_park "This agreement preserves jobs and secures investment, while giving our residents legal protections. It's unprecedented, but it answers both needs."
    "You feel Cassian's shoulder press into yours — a small, familiar weight. He doesn't speak yet; he is letting the moment expand."
    hide jonah_hale
    show cassian_rhys at left:
        zoom 0.7

    cassian_rhys "You did this. All the late nights, the town meetings, the murals. You made them listen."

    mira_kestrel "We all did. It wasn't just me."
    "The crowd murmurs approval. Nadia, standing near the front with her bright waterproof hoodie, lights a ceremonial lantern and passes it to a neighbor. Ruben — his hands knotted around a crate of saplings — gives"
    "you an old, wry nod. His presence grounds you; his cane thumps the boardwalk in a cadence that anchors the ceremony."
    hide mira_kestrel
    show jonah_hale at right:
        zoom 0.7

    jonah_hale "Mira —' (he catches himself, then uses your given name) '— I didn't want to bulldoze memories. I wanted to build certainty. You helped me see a way to have both."
    "You feel something unclench in him — a tiny, visible exhale that makes the small hairs along your forearm stand up."
    hide mayor_lin_park
    show mira_kestrel at center:
        zoom 0.7

    mira_kestrel "That's all we asked. For certainty that includes people."

    jonah_hale "Then let's sign it, with oversight in place."
    # play sound "sfx_placeholder"  # [Sound: The scratch of a pen signing paper; a soft collective breath from the crowd]
    hide cassian_rhys
    hide jonah_hale
    hide mira_kestrel

    scene bg ch6_601bcb_2 at full_bg
    # play music "music_placeholder"  # [Music: Piano picks up a gentle, ascending motif]
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "Thank you for staying open."
    show jonah_hale at right:
        zoom 0.7

    jonah_hale "Thank you for making me sit through the third community hearing."
    "The exchange is ordinary and revolutionary at once — an agreement drafted in compromise, sealed with human smallness."

    menu:
        "Tuck your tidewatcher under your shirt for luck":
            "You slide the tidewatcher beneath your collar, its brass warmth pressed to your skin like a private pact. It steadies your breath, and the crowd's cheering sounds less like noise and more like permission."
        "Leave the tidewatcher visible, a signal to everyone":
            "You let the tidewatcher rest against your jacket where it catches the dawn. A child points and whispers, and for a second the pendant is not just yours — it is the town's talisman."

    # --- merge ---
    "The ceremony continues."
    # [Scene: Tidelab Greenhouse | Late Morning]
    hide mira_kestrel
    hide jonah_hale

    scene bg ch6_601bcb_3 at full_bg
    # play music "music_placeholder"  # [Music: Light woodwind overlays the strings, an airy, industrious rhythm]
    # play sound "sfx_placeholder"  # [Sound: The steady drip of irrigation, low fan hum, soft clack of a crate being set down]
    "The greenhouse air wraps around you — warm, humid, sweet with wet soil. Asha's grin is all work and delight when she sees you."
    show asha_mehta at left:
        zoom 0.7

    asha_mehta "We got the monitoring protocol ratified in the agreement. Independent sensors, public dashboards, and an open API for community data. Volunteers will be trained to run monthly audits."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "You've been pushing for this since the pilot. Does it mean real-time transparency?"

    asha_mehta "Yes. No mysterious numbers in a closed report. People can see tide response curves, berm settlement data, vegetation biomass estimates. We'll post everything to the town feed."
    "You watch as Asha plugs a new sensor into a hydroponic manifold. The LED blinks — green, a small promise."
    show cassian_rhys at center:
        zoom 0.7

    cassian_rhys "We'll need art for those dashboards. Infographics that don't make people glaze over. I can make 'em sing."

    asha_mehta "If you make them sing, you owe me a harmonica solo at the launch."

    cassian_rhys "Me? Forced to harmonica? Traitorous suggestions."
    "You laugh, and the sound loosens something in your chest. The Tidelab has always felt like a kind of cathedral for possibilities — damp, slightly chaotic, and full of the kind of practical miracles you and Asha both love."
    "Ruben arrives, setting down crates labeled 'Orchard Saplings — Raised Mound Varieties.' He wipes his palms on his cap and hands you a small spade."
    hide asha_mehta
    show ruben_ortega at left:
        zoom 0.7

    ruben_ortega "These'll go on the mounds. Keeps roots above salt and gives kids fruit by summer. You plant one, Mira?"

    mira_kestrel "I'll plant the first row."

    ruben_ortega "Good. Make it count."

    menu:
        "Plant the first sapling yourself":
            "You sink the spade into the damp soil and set the sapling into its cradle. Your hands smell of earth and salt; the roots feel real and finite. Around you, volunteers clap quietly, like a benediction."
        "Hand the spade to a relocated family member and step back":
            "You offer the spade to a woman with tired eyes and a steady jaw. She plants with shaking hands and then looks up, meeting your gaze. There's a gratitude that wordlessly includes you."

    # --- merge ---
    "The planting continues and the dashboard streams begin to populate."
    "Asha walks you through the new dashboard layout, explaining sensor redundancies, community annotation features, and the emergency override sequence you insisted on. Her explanations are technical and tender; in the middle of a sentence she grins and adds:"
    hide mira_kestrel
    show asha_mehta at right:
        zoom 0.7

    asha_mehta "You were right to insist on the independent panel. Science needs people to hold it accountable."
    hide cassian_rhys
    show mira_kestrel at center:
        zoom 0.7

    mira_kestrel "And people need science so we don't reinvent harm."

    asha_mehta "Exactly. That's the compromise we actually wanted."
    "You watch the first data stream pulse on the screen — a tiny line that will become a chorus of readings, an ongoing conversation between the bay and the town."
    # [Scene: The Drowned Orchard | Dusk]
    hide ruben_ortega
    hide asha_mehta
    hide mira_kestrel

    scene bg ch6_601bcb_4 at full_bg
    # play music "music_placeholder"  # [Music: Gentle choir tones with a single acoustic guitar; the melody is warm and intimate]
    # play sound "sfx_placeholder"  # [Sound: Laughter folded with the wet slap of footsteps, the soft rustle of paper, a neighbor humming an old lullaby]
    show nadia_kestrel at left:
        zoom 0.7

    nadia_kestrel "We plant not because we forget what was, but because we believe in what will be. These mounds hold our stories and our futures. To those who move, we carry them with us."
    "You feel your throat tighten. A man two rows back folds the paper Nadia read from with reverence. A child tugs at your sleeve, pointing at a lantern."

    "Child" "Will the lanterns stay every night?"
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "They'll stay as long as everyone wants them to. They're for people who need light."
    "Ruben helps families lift crates of belongings onto raised carts. He jokes with a woman about how to anchor a crate against an expected gust. There's grief, certainly — this is not a scene of untroubled"
    "celebration — but there is also resilience in the way hands move and in the way neighbors measure each load."
    "You catch Cassian watching you, his hazel eyes soft and full. He tucks his paint-stained glove into your jacket pocket the way someone tucks an ember into a safe space."
    show cassian_rhys at center:
        zoom 0.7

    cassian_rhys "For luck."

    mira_kestrel "For stubbornness, too."

    cassian_rhys "Stubbornness built these berms."

    menu:
        "Step forward and offer a small speech":
            "You stand, pulse the lantern light against your palm, and share a short, stumbling thank-you. Your words are raw but honest; the crowd hears the human, not the planner, and it changes the way they clap."
        "Stay in the crowd and let Nadia lead":
            "You fold into the throng, listening. Nadia's words feel like yours when she speaks; you realize leading isn't always standing at the front. Sometimes it's steadying a hand at the back."

    # --- merge ---
    "Night falls and volunteers string more lanterns along the walkways."
    "Night falls soft and quick. Volunteers string more lanterns along the walkways; their knitted textures toss small, warm shadows. The island of the orchard feels like a protected exhale in a world that's been holding its breath."
    # [Scene: Boardwalk | Night]
    hide nadia_kestrel
    hide mira_kestrel
    hide cassian_rhys

    scene bg ch6_601bcb_5 at full_bg
    # play music "music_placeholder"  # [Music: A slow, contented cello with a flute threading the top; the cadence of something finished well and still moving forward]
    # play sound "sfx_placeholder"  # [Sound: The whisper of tide against pilings, a distant harmonica (Cassian teasing Asha), soft footfalls on wooden boards]
    "You and Cassian walk slowly, shoulders almost touching. The air carries the faint, sweet tang of apple from the orchard and the cool mineral smell of incoming tide. Your fingers find the tidewatcher at your throat and trace its rim without thinking."
    show cassian_rhys at left:
        zoom 0.7

    cassian_rhys "Do you ever imagine what it would look like if we hadn't come back? If all of this had been someone else's problem?"
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Sometimes. But then I think about Ruben's cane, Nadia's laugh, the mural on the school— I realize I wouldn't trade this ache for the comfort of distance."

    cassian_rhys "I love you. I love how you measure things and how you loosen when the town needs you. I love the way you look at a problem until it tells you its true edges."

    mira_kestrel "You say that like it's simple."

    cassian_rhys "Love isn't tidy. Neither is tidal modeling. Maybe it's why it works for us."
    "You pause on the boardwalk, the world narrowed to the two of you and the long, patient water. The storm that once hunted your nights has softened into a recurring concern you can manage with people at your back."
    "You think of the failed pilot — the memory catches like a cold and then warms when you notice how it sharpened your caution. You feel gratitude for the kind of failure that humbles rather than breaks."

    mira_kestrel "We didn't save everything. But we saved the voices."

    cassian_rhys "We built something that lets those voices keep singing."
    "He lifts his free hand and tucks it beneath your chin, thumb brushing the small amber fleck near your pupil — a gesture intimate and entirely Cassian. The contact sends a steady current through you, the kind that promises continuity rather than fireworks."
    "You trace the tidewatcher again, feeling its history — the failed pilot, the long nights, the ledger of small victories — all soft as coin-worn brass."

    mira_kestrel "This isn't perfect."

    cassian_rhys "No. It's ours."
    "You close your eyes for a moment, tasting the salt air and the warm exhale of people around you. Joy settles in, not a burst but a steady warmth — like a lamp left on through the night."
    hide cassian_rhys
    hide mira_kestrel

    scene bg ch6_601bcb_6 at full_bg
    # play music "music_placeholder"  # [Music: The melody resolves in an ascending cadence, held notes that linger like a promise]
    # play sound "sfx_placeholder"  # [Sound: The tide's soft applause, distant laughter, a harmonica's single, friendly note]
    "You accept the imperfection. You have traded some illusions for a living harbor and a town that knows its voice. You have built jobs in marsh restoration, a fund that will help families re-root with dignity,"
    "and legal protections that anchor people to place. You have kept enough of what mattered — murals, orchards, a ferry stall — and in doing so, kept Lowry Bay's soul recognizable."
    "You breathe in the night, and it tastes like peat, apple, paint, and salt — the particular, layered taste of home."
    show cassian_rhys at left:
        zoom 0.7

    cassian_rhys "Stay."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "I am staying. With you. With them."
    hide cassian_rhys
    hide mira_kestrel

    scene bg ch6_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: A hopeful coda — full strings, a gentle choir — that suggests the work continues but the direction is true]
    # play sound "sfx_placeholder"  # [Sound: Evening settles; the town hums. The tide moves on as it always has, but now the shore answers back.]

    scene bg ch6_601bcb_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    scene bg ch6_601bcb_9 at full_bg
    "THE END"
    # [GAME END]
    return
