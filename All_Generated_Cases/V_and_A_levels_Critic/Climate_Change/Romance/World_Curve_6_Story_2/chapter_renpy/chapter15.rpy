label chapter15:

    # [Scene: Community Kitchen | Morning]

    scene bg ch14_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft clatter of plates, a kettle's long sigh, distant gulls]
    # play music "music_placeholder"  # [Music: Sparse piano, single sustained notes; gentle, rhythmically unhurried]
    "You arrive before the bread has finished cooling. The kitchen is already a kind of small parliament: Sofía arranging name tags at a long bench, volunteer tutors lining up cups of bitter coffee, Mateo passing a"
    "stack of laminated pamphlets with an absentminded grin. The smell of frying onions and salt and wood smoke settles into your clothes the way tidewater settles into the sills — and you carry it with the"
    "kind of slow certainty that long, practical mornings breed."
    "Abuela Rosa sits at the head of the table with a tea towel folded over one knee. Her hands are small and quick; each movement is a sentence you know by heart. She watches you as if reading the weather on your face."
    "You have the lists in your pocket — names, skills, families who will need boat schedules, who needs child care, who can mentor young crews through a cooperative system. The structure has gone through; Iris's contract"
    "is signed and the berm is rising at the mouth of the cove. That fact hums under every plan like a tidal engine: safety bought, shoreline altered, livelihoods rearranged."
    "You set your notebook on the table and let your fingers rest for a moment on the brass compass at your throat. It is warm from being held; it steadies the part of you that wants to undo things you cannot change."
    show abuela_rosa at left:
        zoom 0.7

    abuela_rosa "They came through the night to clear the channel. The old cove will be choked for a while. We can redo the nets, teach them the new routes. We can teach them everything but the voice the sea used to have."
    "She pauses, measuring."

    abuela_rosa "But we will teach them to listen anew."
    show mara_serrano at right:
        zoom 0.7

    mara_serrano "We'll teach them. We have to."
    "She does not look triumphant; her eyes are the careful, resigned light of someone counting the cost and setting about the work. Her acceptance is not joy. It is a steadying that makes survival possible."
    show sofa_serrano at center:
        zoom 0.7

    sofa_serrano "I made a flyer for the youth program. 'Coastal Keepers' — it's not as dramatic as the name, but—"
    "She laughs, small, nervous."

    sofa_serrano "—it's something. Kids still like stickers."
    "You and Sofía trade the easy, sharp little jokes that keep the room from hardening. Underneath them, the shape of loss is present: families that will not come back, boats that will be dry-docked beyond a new dead line."

    menu:
        "Ask Sofía to run the first class this afternoon":
            "Sofía's face brightens like a sudden sun. She grabs the stack of coloring sheets and promises a raucous turnout, then turns to recruit Mateo for a scavenger-hunt lesson on edible marsh plants."
        "Keep Sofía on logistics — you need reliable hands":
            "Sofía shrugs tight-shouldered but hides disappointment under a professional nod. She folds her hands and starts compiling names, quieter, practical."

    # --- merge ---
    "The morning proceeds with volunteers signing up and plans taking shape."
    "You arrange the morning rosters. Volunteers sign their names in a looping cursive that almost looks like the tide lines on the sand: repeating, inevitable. Conversations are low, deliberate — a demonstration of how the town"
    "is reshaping itself into new rhythms. The room fills with human, workable patterns: retraining classes, a cooperative fishing rota, shared storage spaces for boats that will be used in shifts."
    "Mateo leans in and lowers his voice, the habitual conspirator returning for the work at hand rather than for the argument that has already been decided in the council chambers."
    hide abuela_rosa
    show mateo_reyes at left:
        zoom 0.7

    mateo_reyes "People are sore, but they come. They want the training, they want the food. They're scared of losing the shoreline the way you are, but they're also tired of storm nights."

    mara_serrano "Tired and willing,' you say. 'That is what keeps things going."
    "He nods, and the nod settles like a small agreement between generations."
    # [Scene: Berm | Midday]
    hide mara_serrano
    hide sofa_serrano
    hide mateo_reyes

    scene bg ch14_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant hum of machinery, measured footsteps in wet sand]
    # play music "music_placeholder"  # [Music: Single low cello line; calm, slow pulses]
    "You walk the berm when the sun is highest and the air is the salt-and-steel taste of midday. The structure is promise and incision in one slow, factual plane. From certain angles it is a clean"
    "line against the horizon, an engineer's logic bootstrapped into the earth; from others, it looks like a scar that will not heal the same way the shoreline did."
    show elias_park at left:
        zoom 0.7

    elias_park "They're asking for modular training kits. We can repurpose the old sensors — teach them to read the tide charts. Nima can pull together the funding to get the kits shipped next week."
    show mara_serrano at right:
        zoom 0.7

    mara_serrano "And the boat-share scheduling?"

    elias_park "I wrote a rota. I—"

    elias_park "I've been working on a microgrant to get some of the fishers compensated while they retrain. The investors were resistant, but Nima and I pushed. We can cover labor for the first month."
    "You study him. He talks like a man who is trying to stitch something together with care and numbers. It is the thing he knows how to do; it is also his refuge."

    mara_serrano "You're doing a lot."

    elias_park "It's what I can do. Engineering is—"
    "He gestures at the berm."

    elias_park "—it's a kind of language. Right now, the language I can speak to help is schedules, lists, contingency flows. I thought— I thought we might keep building, together. I didn't mean—"

    mara_serrano "You didn't mean to make this the only thing you had."
    "He looks away, at laborers moving along the berm, at the pale horizon beyond."

    elias_park "Maybe I buried it. The other parts. I thought if I fixed enough, things would go back to being the same. I didn't realize the cost would be—"
    "He breathes, a small, private sound."

    elias_park "—this much."

    mara_serrano "The cost pulled a line through the map we used to draw. We both thought different maps might meet."
    "There is a small silence. The machinery's hum becomes a low third voice; the conversation folds into the slow work of the day."

    elias_park "I'm sorry. For anything I didn't say when it mattered. For getting lost in schedules."

    mara_serrano "And I'm sorry I couldn't stop the line from being drawn."
    "His hand finds yours across a pile of fold-out plans, resting there like something tentative and alive. It's not an answer; it's a quiet anchoring that is honest about distance. He squeezes, then goes back to the lists."

    menu:
        "Ask Elias if he wants to lead the youth training on tide reading":
            "Elias blinks, surprise softening his features. He agrees, voice steadying as the idea fits his skillset and gives him a way back into being useful where the town needs him."
        "Give Elias space; focus on community outreach instead":
            "Elias nods quietly. He withdraws into the work of donor communications, his shoulders folding inward but his hands steady."

    # --- merge ---
    "Elias settles into a role shaped by what the town needs and what he can offer."
    "Abuela Rosa finds you at the berm's edge, leaning on the low temporary railing. She does not say much. She looks at the sea with the same attention she gives to the small things in her garden; her face catalogues the altered view without dramatics."
    show abuela_rosa at center:
        zoom 0.7

    abuela_rosa "You'll teach them. And they will teach us something back. This is how it has always been when the sea changes: we learn to make other songs."

    mara_serrano "Will the song be the same?"
    "She smiles, small and wry."

    abuela_rosa "No. But songs change. They keep telling where you have to step."
    "Her certainty is not comfortless. It is the measured acceptance of a lineage that has survived by shifting its steps."
    # [Scene: Promenade | Dusk]
    hide elias_park
    hide mara_serrano
    hide abuela_rosa

    scene bg ch14_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft conversation, the distant call of a ferry rerouted along a new channel, children's laughter]
    # play music "music_placeholder"  # [Music: Gentle, sustained strings; the arrangement broadens slightly but remains subdued]
    "By evening the promenade fills with the town's softer noises. There are fewer fishermen's knots tied along the rail than there used to be; some benches sit empty with the memory of hands that will not"
    "return. New signs direct boats to new slips; families wheel luggage toward buses bound for places that still feel like home. The shoreline's outline is different — the eye learns the new silhouette and then misses"
    "the old one."
    "Sofía stands before a small group of kids, paint on her fingers, explaining the difference between sea lettuce and salt weed. Her voice is luminous — small and fierce. You watch her and feel that particular"
    "blend of pride and ache that comes when the next generation takes up a new mantle."
    "Elias Park is on the far side of the promenade, his profile caught briefly in the last light as he speaks into his phone. When he sees you watching, he lowers it. There is an apology in the way he crosses the distance, slow and deliberate."
    show elias_park at left:
        zoom 0.7

    elias_park "I filed the report to the funders. We got the microgrant. And — Sofía's program got the stipend."
    show mara_serrano at right:
        zoom 0.7

    mara_serrano "You did what you could."

    elias_park "Not everything. And I'm sorry. For when I thought engineering alone would be the answer."

    mara_serrano "We thought different things would save us. We found other ways to keep doing the work."
    "He exhales, the sound of someone making peace with what he cannot change."

    elias_park "I don't know if this is how I imagined us ending up. But I know this: I don't want to walk away from you."
    "You look at the curve of the new shore, the concrete line and the way the light sits along it. The cost of safety is visible in the geometry of things. The town is quieter where"
    "it used to shout; it is, nonetheless, protected. People have roofs tonight who would not have had them without Iris's contract."
    "Iris Varela appears at the end of the promenade like a weathered statue softened by evening. She moves with the same purposeful calm you saw in the council hall — hands clasped, a worn folder under"
    "her arm. There is a publicness to her presence that makes the moment a little formal."
    show iris_varela at center:
        zoom 0.7

    iris_varela "You did the work. You carried the programs. The town is better organized because of what you all set in motion."

    mara_serrano "And what we lost?"

    iris_varela "Lines had to be drawn. I did what I thought would save the most. There are things I would change, too, given time. We will keep the community in the loop for the next phases."
    "Her words are practical; she does not try to smooth the edges. There is an honesty to her tone — not contrition, but recognition of the moral weight that sits like sediment over the bargain."
    "Abuela Rosa stands beside you now, small and steady."
    hide elias_park
    show abuela_rosa at left:
        zoom 0.7

    abuela_rosa "You did what you could. People will remember both the saving and the losing."
    "You close your eyes for a second and taste the air — metal, salt, a faint sweetness from Sofía's snacks. The compass at your throat is cool. You think of the families who moved south, the"
    "boats that now share slips, the children who will learn new rhythms of the sea. The town is intact in ways that matter; it is also visibly altered."
    "Elias reaches out and threads a finger through yours. He does not try to promise comfort he cannot give. Instead, he offers the thing left between two people who have weathered a shared grief and found a new shape to their caring."
    hide mara_serrano
    show elias_park at right:
        zoom 0.7

    elias_park "We will keep working. Not the same as before. Different. Maybe smaller victories, but steady."
    hide iris_varela
    show mara_serrano at center:
        zoom 0.7

    mara_serrano "Steady is good. It will have to be enough."
    "He nods, and for a moment you let yourself imagine ordinary mornings again — teaching tide charts, sharing a thermos, Sofía running down the boardwalk with paint on her elbows. The image is fragile and luminous."
    "There is a quiet parade of faces: people who learned new trades today, a young fisher smiling with a repaired net slung over his shoulder, an old woman sitting on a bench knitting a buoy cover"
    "that will be used by the cooperative. The town's life stitches itself in new ways. It is not what you first hoped for, and it is not a defeat so much as a reshaping of survival."
    "You take the compass in your hand, feeling the little dent from the seam of a past storm. You tuck it back under your shirt. The warmth underneath feels less like a secret and more like a responsibility you have accepted."

    abuela_rosa "Keep the maps. Teach the songs. Do not let the shore's new line make you forget the old stories. They teach how to live with what changes."

    mara_serrano "I will teach them. We will keep teaching."
    "Sofía runs up, paint smudged across her cheek, and flings both arms around your waist in a fierce, laughing hug. It jolts something loose in you — tears behind your eyes, not for the present only but for all the change that had to happen to get you here."
    hide abuela_rosa
    show sofa_serrano at left:
        zoom 0.7

    sofa_serrano "You're never allowed to be sentimental in public,"
    "Night settles quietly over Puerto Alba. Lights come up along the promenade; the new concrete catches long, gentle pools of lamp glow. The sea breathes in a slow, rhythmic way that feels like a promise and a warning held together."
    "You stand a long while, watching."
    "There will be nights when the new defenses hold and quiet fills the town like a balm. There will be mornings when you will wake remembering the shapes of coves that aren't the same, and you"
    "will need to teach your heart to measure loss against lives saved. Love here is altered — quieter, more practice than poetry, a steady leaning into shared labor rather than the grand gestures you imagined when"
    "kindness felt simpler."
    "You have done the work you believed would keep people safe. The programs you've organized give people routes into new livelihoods, and children like Sofía lead the way with stubborn, sunlit energy. Elias is beside you,"
    "not entirely present the way he used to be, but present in the ways that matter: showing up, making lists that match needs, building small scaffolds for people to climb back up."
    "Whatever the future brings, you have chosen to bend the town toward survival even if it costs the shoreline the shape you loved. That decision sits in your chest — a heavy, patient thing you carry"
    "like a brick you have built into the foundations of the life you will now help maintain."
    hide elias_park
    hide mara_serrano
    hide sofa_serrano

    scene bg ch14_3be532_4 at full_bg
    # play music "music_placeholder"  # [Music: Gentle piano and a low sustaining string; the tone is melancholic but warm]
    # play sound "sfx_placeholder"  # [Sound: The distant, steady call of a buoy bell; the sea's measured exhale]
    "You fold your hands together and let the quiet be the last thing that settles tonight."

    scene bg ch14_3be532_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    scene bg ch14_3be532_6 at full_bg
    "THE END"
    # [GAME END]
    return
