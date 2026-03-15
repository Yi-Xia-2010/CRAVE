label chapter4:

    # [Scene: Saltmarsh Labs | Morning]

    scene bg ch4_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Soft, steady pulse — hopeful but measured]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the drip of water from a lab rig, the soft beep of a sensor coming online]
    "You walk in with the brass compass warm against your collar and the vote still vibrating behind your teeth. You said yes in the council chamber — you put your weight behind Elias's pilot — and the echo of that decision follows you like a step you can't take back."
    "Your windbreaker smells faintly of salt and fried dough; mud crusts the cuffs where you lifted a tarp at dawn. Stickers — 'ACTIVATE' and the little blue logo Elias's team uses — adhere to the fabric"
    "like medals for small victories. Hands trace the ridge of your notebook in your pocket; tide sketches press into the leather."
    show elias_park at left:
        zoom 0.7

    elias_park "You did it, Mara. You— —you trusted us."
    show mara_serrano at right:
        zoom 0.7

    mara_serrano "We chose a risk that could be a bridge. I couldn't sit aside and watch Iris sign a blank check."
    "You run a thumb along the notebook's spine. 'This won't be easy.'"

    elias_park "Nothing worth keeping ever is. Nima and I sketched a liaison plan last night. Community reps, rotating shifts, a transparency timeline. We want this to be something the town touches at every step, not just a— —installation."
    show nima_shah at center:
        zoom 0.7

    nima_shah "And the sensors have new firmware. Less false positives from wind gusts. If we place this cluster on the east berm and the planters along the upper marsh—' (she taps a grid) '—we'll get a continuous profile of salinity, water height, and soil moisture. Data that's actually useful."
    "Your chest loosens when you see the list of community liaisons: Abuela Rosa, Mateo, a teacher from the school, Sofía's name scribbled as a youth rep. The inclusion tastes like salt and something softer — relief."

    mara_serrano "I'll organize the volunteers. Shift schedules, food, tools — and I'll make sure Abuela's techniques are logged alongside the sensors' data. No one's knowledge gets footnoted."

    elias_park "Promise me you'll keep telling me when we're moving too fast. It's easy for me to love the math and forget the people side."

    mara_serrano "Promise."
    "The word sits lighter than you expected."

    menu:
        "Take the printed liaison roster and start calling names":
            "You take the roster; the paper crackles under your palm and you feel the familiar momentum of organizing. You dial the first number, and Mateo answers with a grunt and a yes, already halfway to the boats."
        "Ask Elias to walk the placement map with you, marker in hand":
            "You pull the map closer. Elias smiles and curls his hand around a blue marker; together you redraw a berm line to better fit Abuela Rosa's note about eelgrass pockets. The plan breathes in the space between your gestures."

    # --- merge ---
    "Elias studies your face after you choose, as if cataloguing the shape of your resolve. Nima sets down a sensor and extends it toward you."

    nima_shah "You should hold it. See how light it is? Feels nothing like responsibility."
    "You accept the sensor- small, seawater-proof casing and a soft hum of calibrated purpose. It is, absurdly, beautiful."

    mara_serrano "It won't feel like nothing for long."

    nima_shah "Good. We built it so it tells truth, not comfort. And that will make a difference."
    "You glance at the wall clock; tide windows don't wait for argument. The day is already scheduled with planting, training, and a community forum at dusk."
    # [Scene: Marsh | Early Afternoon]
    hide elias_park
    hide mara_serrano
    hide nima_shah

    scene bg ch4_453e40_2 at full_bg
    # play music "music_placeholder"  # [Music: Acoustic plucking, steady rhythm — hands at work]
    # play sound "sfx_placeholder"  # [Sound: The soft suction of boots in mud, the distant slap of waves, children's laughter echoing like small bells]
    "You lead a volunteer shift: ropes in hand, a line of neighbors planting modular planters and weaving them into the tidal rhythm. The air smells of loam and a zing of citrus from the thermoses someone has brought."
    show abuela_rosa at left:
        zoom 0.7

    abuela_rosa "We plant the roots where the tide remembers to be gentle. You must listen to the mud. It tells you how to ask for stability."
    show mara_serrano at right:
        zoom 0.7

    mara_serrano "How do you hear it?"
    "Your voice is small against the wide noise of water."

    abuela_rosa "You learn to trust the slow answers. And you plant with other hands — it keeps you honest."
    show sofa_serrano at center:
        zoom 0.7

    sofa_serrano "Think of the sensor as a sea's diary. It writes down everything the water does so we don't have to guess."

    "Child" "Will it stop storms?"

    mara_serrano "Not by itself. But it helps us know when to move plans up the list, where to plant more roots, and when to help our neighbors. It's one tool, but it's ours."
    "The planting is tactile work. Mud pulls at your gloves; the planters' rough fibers rasp your palms. Sweat and salt sting at the corners of your eyes. Each placement is an argument against erasure — a small, deliberate act."
    hide abuela_rosa
    show mateo_reyes at left:
        zoom 0.7

    mateo_reyes "You look like someone who hasn't slept. But the kids—look at them. They take to this like it's a game."

    mara_serrano "They should. It is their game."
    "You glance at Sofía and something warm brightens at the edge of your worry."
    "Abuela Rosa watches you for a beat, unreadable, then pats your hand."
    hide mara_serrano
    show abuela_rosa at right:
        zoom 0.7

    abuela_rosa "You hold too much, niña. Let others hold some of it."
    "You feel the tug of truth in that, and you tuck it under your ribcage like a small stone. You will carry it — but you will hand off the wheel when others can hold it."

    menu:
        "Walk the line to check each sensor's placement":
            "You follow the sensor line, hands on the casings. The dataloggers chirp steady; one needs re-sealing, and you can already feel the exact tweak to make."
        "Stay with the volunteers and teach a short lesson":
            "You stay, and Sofía hands you a chalkboard. You teach the kids about tidal memory, and their questions turn technical ideas into stories that stay. A small child draws the pilot's logo with mud and pride."

    # --- merge ---
    "The group's work continues into the late afternoon as the day moves toward the demo."
    # [Scene: Promenade | Late Afternoon — Demo & Storm Test]
    hide sofa_serrano
    hide mateo_reyes
    hide abuela_rosa

    scene bg ch4_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: A measured crescendo — forward momentum with neat harmonies]
    # play sound "sfx_placeholder"  # [Sound: The distant hiss of an incoming squall, reporters' murmurs, the murmur of a crowd]
    "Investors arrive in secondhand suits that smell faintly of machine oil and ambition. Cameras hover; a local reporter jots words in a spiral notebook. The pilot's data scrolls across a rented screen: predicted tide lines versus"
    "observed, the sensor cluster's readings, the marsh's uplift in micro-decimeters. The numbers, when they appear, sit like small lights in the dusk — clearer than you'd dared to hope."

    "Investor 1" "This is impressive. Your storm model came in under predicted erosion by thirty percent. What does scaling look like?"
    show elias_park at left:
        zoom 0.7

    elias_park "Scaling means community-led deployments, training, and an open standard for data. We are proposing phased rollouts with measurement points and oversight."

    "Investor 2" "Phased is fine, but timelines matter. There are other towns ready to sign within months. We could fund manufacturing, logistics —"
    show nima_shah at right:
        zoom 0.7

    nima_shah "We built this with closed-sourcing off the table. If you're offering money, it needs to come with governance guarantees."
    "Elias meets Nima's stare and nods; you watch their exchange like a handoff. The investors' smiles thin, a fabric smoothing into a calculation."

    "Investor 1" "Governance can be written. Contracts are flexible."
    "You step forward then — because you have to. Cameras shift to you in a single tilt."
    show mara_serrano at center:
        zoom 0.7

    mara_serrano "If this scales, it must scale with people who know this place. Abuela Rosa's planting guides, Mateo's response teams, school curriculums — all of it. The technology alone won't hold what matters."

    "Investor 2" "We understand community needs. Efficiency doesn't have to erase voice."
    "Your voice carries, steadier than the wind, steadier than you feel. You can taste the metal of the moment: the same bland tang that often accompanies money. You feel Elias at your side, a small, steady weight."

    elias_park "We could design a conditional contract. Funding disbursed per community milestones — local hires, open data. No forced timelines."

    "Investor 1" "Milestones slow down market capture. The faster the rollout, the more lives protected sooner."

    nima_shah "And the more mistakes cost more lives later if we don't listen."
    "The crowd murmurs. For a beat, hope and caution sit evenly on the promenade, like birds on a wire."
    "Then the squall strikes — not a catastrophe, but enough to test. Wind knifes across the marsh; rain threads itself horizontally. The sensors begin to sing in their small way, a chorus of numbers that runs along the project's backbone."
    "Your stomach hitches. You watch the live feed with a clinician's attention and a mother's prayers braided together."
    "The pilot holds. The planters flex and hold sediment; the sensors read a lower-than-modeled surge in key areas. The data scrolls: the marsh's buffering effect registered precisely; the modular planters slowed erosive force where they were anchored by community-placed roots."
    "A cheer, surprised and bright, rises in the crowd. Investors' faces show the sliver of profit's pleasure: validation."

    "Investor 2" "There's traction."
    "Elias's shoulders drop a fraction in something like exhaustion and relief. He looks at you with a smile that loosens the tightness under your ribs."

    elias_park "We did it. Together."
    "You try to let the warmth sit on you without turning it into obligation. It is easier, for the first time in weeks, to believe that what you started might breathe on its own."
    "But the same suits that applauded now circle back, papers folded like knives."

    "Investor 1" "We're glad to have participated in the demo. We'd like to propose a partnership to scale this nationally. Faster manufacturing, distribution, turnkey installs. With our network, we can deploy in months."

    elias_park "Scaling with community oversight."

    "Investor 1" "We'd like fewer strings on deployment. Speed is critical; we can't wait for months of oversight when storms don't."
    "Nima steps closer, jaw set."

    nima_shah "You want speed. We want stewardship. There's a middle ground."

    "Investor 2" "Middle grounds get you middle results. For towns that need fast protection, middle results aren't enough."
    "You feel something shift under the surface — not yet a crack, but an alignment changing. Elias's optimism bends toward a line he hasn't decided to cross."

    elias_park "They want to move on their timetable. They mean well — many do — but their well is sometimes a well with a bottomless price."

    mara_serrano "What would a conditional rollout look like to them?"

    elias_park "They'll talk about guarantees and liability. They'll want to limit community vetoes to keep timelines tight."
    "You swallow. The arousal of the day — the steady build of work, the small triumph of the storm test — ripples into a caution you're practiced at: gratitude is tempting to accept without reading the fine print."

    "Investor 1" "We can write a contract that satisfies both — scale and local oversight — but it will read in legal terms, not in the way people talk in town meetings."
    "Elias looks at you, and for a heartbeat both the engineer and the man seeking to do right meet in his expression."

    elias_park "I don't want to sell out what we're building. Not for speed, not for money."

    "Investor 1" "And we don't want to lose the window to protect people. We all want the same thing, Mr. Park."
    "The words fold over one another — shared language, divergent horizons."
    "You stand with grit under your nails and the salt-cooled wind in your hair. The pilot has given the town breathing room; the test proved the math. But breathing room, you know, can also be leased."
    "You think of the faces who planted today: Abuela Rosa's steady hands, Mateo's easy grin, Sofía's fierce small voice teaching kids to read tides. The data is proof; the people are the reason the proof matters."
    "You feel a pressure at the base of your throat — not a collapse, but the slow compression of responsibility forming into decision. The pilot is a success on paper; in the seams of that paper someone will try to stitch profit."

    menu:
        "Ask to see a draft of the investors' proposed timeline now":
            "You step toward a tablet an investor holds out. The timeline's columns run tight and fast. You underline language that could strip community control and feel the sharp, practical shape of bargaining forming in your chest."
        "Pull Elias aside and insist on a clear governance clause before any signatures":
            "You put your hand on Elias's arm. He meets your eyes and nods, the engineer in him already imagining redlines. You both agree: nothing signed without a governance clause drafted with the liaison group."

    # --- merge ---
    "Elias lets your hand stay on his arm a beat longer than necessary. The crowd begins to thin as the rain softens to a mist. People talk in small clusters, energized, animated, wired by the day's outcome."
    "You walk the promenade alone for a moment, the sound of distant conversations and rain filling the space where your breath used to be steady. The pilot's early success plays back through your mind like a film reel of small, stubborn things — seedlings, sensors, a child's chalk logo."
    "And somewhere in the space between applause and contract talk, you feel the first fine crack of a new worry: the way good things invite appetite. The investors' offer sits between you and the town like"
    "an ornate bridge; it could carry everyone across, or it could reroute traffic the town never agreed to."
    "You pull your compass from under your scarf and let it rest against your palm. It feels ordinary and decisive at once."
    hide elias_park
    hide nima_shah
    hide mara_serrano

    scene bg ch4_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Low sustain, minor chord that does not resolve — anticipation without alarm]
    "You can see the path forming ahead — more meetings, more drafting, more nights where your voice will be the bridge between people and agreements. For now, the pilot breathes. For now, the town leans into a new possibility."
    "A gust of wind tousles your hair. You look back toward the labs where lights are still on and toward the investors who are already discussing numbers. The swell of the sea beyond them is unchanged, constant as record and truth."
    # [Page-Turn Moment: You close your fist around the compass and feel, almost physically, the weight of the weeks to come. The pilot has shifted the horizon; someone will now try to redraw it. You understand — with a clarity that is both neutral and urgent — that your next steps will decide how the town's story continues.]

    scene bg ch4_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
