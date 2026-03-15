label chapter30:

    # [Scene: Polished Quay | Midday]

    scene bg ch14_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm, steady strings; medium tempo]
    # play sound "sfx_placeholder"  # [Sound: Low murmur of gathered townspeople, distant gull calls, the soft clack of reporters’ gear]
    "You stand with the salt still in the seams of your hair, the scarf tight at your throat. The boardwalk’s rain from the other day is a memory that sits in the ribcage—raw but steady now."
    "Around you, microphones align like a row of curious gulls. Cameras tilt. Tamsin’s tablet glows in the coolness of her hands; Corinne’s reflection is a clean edge in the pavilion glass."
    show tamsin_cho at left:
        zoom 0.7

    tamsin_cho "Thank you for coming, Amaya. We wanted this public—transparency matters."
    "You feel the crowd as a single organism: ruffled planning documents, folded arms, a child with a damp shoelace. Your voice comes out controlled, practiced."
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "We asked for a voice at the table. Today, we get the details."
    "Corinne Voss steps forward—platinum hair, precise smile. There’s no triumph in it, only the kind of calm that makes people accept numbers as fate."
    show corinne_voss at center:
        zoom 0.7

    corinne_voss "Marisol Bay is a priority for Voss Marine. We’re scaling back the full port plan, funding immediate marsh restoration, and committing to a ten-year community oversight board funded by our foundation."
    "You nod even as your eyes find the clause Tamsin hesitates over—language tucked into legalese: an operational reservation that cedes certain low-lying blocks for port expansion. The words feel like a tide line drawn across a neighborhood."

    amaya_reyes "The restoration funds—will they include long-term relocation assistance for households in the ceded zones? Not after-the-fact, but proactive transition planning."

    tamsin_cho "Yes. There are allotments for housing, job transition programs, and a community-managed trust. The oversight board will have veto power over operational expansions for five years."

    corinne_voss "We will protect main infrastructure—school, clinic, the quay’s access routes. We will also invest in modular wetland barriers designed with TideLab’s input and fund retraining programs for fishery workers."
    "Your stomach twists—practical protections closing against the real cost. This is the bargain: structure for safety, acreage for commerce. You hear Mateo’s breath behind you, a low steady note."
    hide tamsin_cho
    show mateo_reyes at left:
        zoom 0.7

    mateo_reyes "And the houses? My friends—"

    corinne_voss "We have a relocation fund and purchase offers. No one will be left without options."
    "The crowd exhales as if a storm has moved on. Relief rolls like a warm current. Still, the ceded blocks are on a map now, labeled in small, clinical font."
    hide amaya_reyes
    show luka_maren at right:
        zoom 0.7

    luka_maren "Amaya—there’s another part. They want me to consult on the modular systems. I can be inside the project, push for community design."
    hide corinne_voss
    show amaya_reyes at center:
        zoom 0.7

    amaya_reyes "Inside? For them?"

    luka_maren "If I refuse, they’ll hire someone else. If I accept, I can keep TideLab's voice at the drafting table. I can make sure the wetlands tech is distributed, open-source specs, training programs—things we’ve always wanted."
    "The wind takes the corner of a printable plan and sends it toward the harbor. Corinne watches, expression unreadable."
    hide mateo_reyes
    show corinne_voss at left:
        zoom 0.7

    corinne_voss "Luka is an asset. We want to bridge corporate scale with community resilience. His role will be part-time, advisory. We’ll fund TideLab’s pilot and give priority contracting to local teams."
    "You breathe. The offer is tidy and pragmatic; it smells faintly of engineered citrus and polished promises. Relief hums under your ribs—roofs fortified, clinic supplied, the school safe in a worst tide. The immediate pressure that"
    "had been tightening for weeks loosens now, enough that you can hear the gulls again."

    amaya_reyes "So you scale back the disruptive parts. You fund restoration and oversight. You guarantee resources for people forced to move."

    corinne_voss "Exactly. It’s compromise with real protections."
    "Mateo folds his hands into his sweater, hard and quick with anger that tears itself into a pragmatic, worn care."
    hide luka_maren
    show mateo_reyes at right:
        zoom 0.7

    mateo_reyes "We keep what matters. We don’t throw people away."
    hide amaya_reyes
    show abuela_rosa at center:
        zoom 0.7

    abuela_rosa "You save the hull, niña. But some planks will be taken. We mend what we can. We plant new roots."
    "Her voice is soft and stubborn and older than municipal maps."
    "Corinne extends a hand—an offer that has been ironed flat into policy. Cameras surge forward, flashes like sun on chop. Around you, people murmur; at the edges you hear grief, but louder is the sense that severe harm was stopped before it struck."

    corinne_voss "We can start community projects next month. TideLab will receive a grant for wetland sensors and community training. Luka’s involvement secures design integrity."
    "You look at Luka—at the way he tries to make the calculus of compromise sound like strategy rather than surrender."
    hide corinne_voss
    show amaya_reyes at left:
        zoom 0.7

    amaya_reyes "If you do this—if you take that position—you don’t disappear into their cycles. Promise me you’ll keep us first."
    hide mateo_reyes
    show luka_maren at right:
        zoom 0.7

    luka_maren "I promise. It’s not perfect, but it keeps a lever. It keeps us in the room."
    "There’s a beat. The crowd seems to inhale, waiting for the seal—the handshake, the signatures. It’s the climax you’ve been building toward: not a dramatic arrest or a shouted eulogy, but the steady, legalized clasp of two parties making a pact that will change lives."

    menu:
        "Reach for Luka’s sleeve and anchor him":
            "You press your fingers into the worn denim at his elbow—small, human. He looks at you and his amber eyes soften; for a second you feel shared stewardship, not distance."
        "Step forward and address the crowd first":
            "You lift your voice. It’s clear and warm. You name the protections, you name the losses, you call for the community oversight board to be truly representative. The crowd listens; some nod, others clap softly."
    "THE END"
    # [GAME END]
    return
