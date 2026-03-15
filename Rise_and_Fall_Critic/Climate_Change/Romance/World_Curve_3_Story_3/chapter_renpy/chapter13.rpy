label chapter13:

    # [Scene: Rooftop Sanctuary | Early Morning]

    scene bg ch11_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, hollow cello; rhythm like distant waves]
    # play sound "sfx_placeholder"  # [Sound: The soft slap of wet canvas, the hiss of a kettle in a distant café, murmured names on walkie-talkies]
    "Narration:"
    "You wake to a roof that smells like damp soil and rosemary. The solar fabric hangs in low swags, sweating beads that nickle-slide into gutters. Beneath it, volunteers huddle around clipboards and tablets, tracing maps with"
    "pens that skip in the humidity. The sanctuary hums: heaters on low, a chorus of measured breaths, the quiet murmur of people doing the small, necessary work of keeping others alive."
    "Narration:"
    "Your notebook is inside your jacket. The dented compass rests there too, warm from your chest. Finn has already turned the old storage lockers into supply caches; he shrugs when you catch his eye and the laugh that follows tastes like fatigue and pride."
    show finn_serrano at left:
        zoom 0.7

    finn_serrano "You look like you need coffee and a miracle. I can do the coffee."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "Miracles are on backorder. Coffee will do."

    finn_serrano "Good. Because the tide chart said nothing about miracles."
    "Narration:"
    "You move among the clusters: Rosa at a folding table, stamping names on meal vouchers and offering bread with two hands; volunteers cross-reference the town registry with the list of rooftop relay points, deciding who moves"
    "where and who stays for critical systems. The air is tactile — the brush of canvas against your cheek, the rough braid of rope in your palm when you test a knot, the way your collar"
    "is damp at the nape."
    show rosa_alvarez at center:
        zoom 0.7

    rosa_alvarez "There's a family from the East Row — they're refusing to go until they can find someone to look after the cat. God help me, it's a cat, Maya."

    maya_serrano "We have a foster list. We'll find someone. Tell them — gently."

    rosa_alvarez "Gently doesn't stop the sea."
    "Narration:"
    "The conversation is practical, but under it there is a tension you recognize like a familiar bruise: the town is dividing on terms you thought you could hold together. You feel the strain at your chest"
    "— an old habit of trying to hold pieces in place with your bare hands."

    menu:
        "Check the supply manifests for East Row":
            "You kneel at the stack of manifests, thumbs fanning through names. Some addresses are crossed out; some have notes in a rushed hand. The list looks smaller than it should. Your mouth goes dry."
        "Go see Finn knot the new caches":
            "You walk to where Finn is working. He shows you a knot he learned aftermarket; it's solid and ugly, the sort that won't betray anyone. You feel a small, ridiculous relief — at least this is one thing you don't have to worry about right now."

    # --- merge ---
    "You choose both, because that is what you do — you split like a tide over two rocks. You trace names, check supplies, then test the rope Finn's tied. The scent of oil from his toolbox"
    "mingles with damp paper and the herbal sweetness from Rosa's table. It grounds you until a walkie-talkie crackles with Hana's voice."
    # play sound "sfx_placeholder"  # [Sound: Crackle — static; then Hana, clear but brisk over the feed]
    hide finn_serrano
    show dr_hana_park at left:
        zoom 0.7

    dr_hana_park "Maya, this is Hana. I'm on the buoy run. Instruments are behaving oddly — salinity spike near the channel. Keep an eye on the unreinforced cuts in the berm. If the tide comes high with that profile, it will find an opening."

    maya_serrano "How much time?"

    dr_hana_park "Not enough. Two to three hours, if the models are right and the wind holds."
    "Narration:"
    "Hana's voice is a clean line in your chest. On the mobile research boat, her boots are wet and the sodium lamps paint her profile in orange pools; you can almost see the spray on her"
    "sleeves. Her competence is a net you want to fall into and be supported by. Instead, you feel the net straining under the sudden weight of urgency."
    # [Scene: Mobile Research Boat (Field Buoy) | Mid-Morning]
    hide maya_serrano
    hide rosa_alvarez
    hide dr_hana_park

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Motor hum, the metallic ping of instruments, gulls distant]
    "Narration:"
    "The boat smells of diesel and salt. Dr. Hana's hands are sure when she unhooks a sensor; she mutters numbers that anchor a sinking feeling in your stomach. The buoy's readouts flicker then steady; she taps"
    "a keyed command and the panel shudders like someone rearranging a deck of cards mid-storm."
    show dr_hana_park at left:
        zoom 0.7

    dr_hana_park "We're patching the sensor array. If we can keep the readings stable, we can predict the flow better. But the channel you reinforced last week — it's thin. The sandbags are holding, but only by luck."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "We can move volunteers to reinforce it. Finn—I mean, he can turn the storage lockers into more caches, we can shift people."

    dr_hana_park "A moving line of people will slow us down. We need materials in the right place. The timeline is tight, Maya. The question isn't just who moves — it's who can stay without risking lives."
    "Narration:"
    "Hana's words fall like stones. You hear the implication, the economic geometry of who can afford to lose a floor and who cannot. Her tone is not accusatory; it's pragmatic. But in the space between practicality and human faces, accusations can grow like mold."

    menu:
        "Argue that autonomy matters — prioritize convincing residents":
            "You meet Hana's gaze and push. 'We can't do this if people feel bulldozed.' Your words ring with the familiar force of your convictions. She doesn't soften, but you see a flicker — respect complicated by worry."
        "Focus on logistics — call Finn and reroute volunteers to the berm":
            "You key your comms, voice steady. 'Finn, new priority: berm reinforcement. Everyone else, split for the relay point. Move.' Actions replace argument; people begin to move like a single organism. The cost is immediate: fewer hands for persuasion."

    # --- merge ---
    "You choose both again—argue and act—because saying both feels like not choosing at all, and that is the thing you have always done. You tell Hana you'll patch messages to the hesitant households while radios dispatch volunteers. Hana allows a tight smile."

    dr_hana_park "Do what you can. History will judge what you couldn't prevent."
    "Narration:"
    "Her words are a warning and a comfort; history is distant until it arrives as a wet bookshop on a side street."
    # [Scene: Local Bookshop — "Harbor Pages" | Late Morning]
    hide dr_hana_park
    hide maya_serrano

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Slap of looming water in alleyways; the coffee cup left on the counter trembles slightly]
    "Narration:"
    "The bookshop smells of paper and lemon oil; it's a spine of the old town, its owner an elderly woman with hands that have known binding and knitting and the weight of stories. She trusts you"
    "because you worked to put up sandbags outside her street last season. You trust you'll be able to convince her to come to the rooftop relay."

    "Mrs. Alvarez" "They won't listen to me if I leave. My customers will come back for the books. The cat will hide. This is my life, niña."
    show maya_serrano at left:
        zoom 0.7

    maya_serrano "We have a volunteer to check on Glen's cat. We'll pack the shop into crates. There's a preservation team."

    "Mrs. Alvarez" "My books don't want a preserve box. They want a window that looks like the sea."
    "Narration:"
    "You find your voice softening because she is both a neighbor and a relic of the town you are trying to save intact. The conversation is patient, full of the small negotiations that teach you patience and guilt in equal measure."
    "Narration:"
    "Then, a shout from the alley. You both turn."
    # play sound "sfx_placeholder"  # [Sound: A sudden roar — water uncoiling like a beast; the ground underfoot vibrating]
    # play music "music_placeholder"  # [Music: Violins climb with dissonant urgency]
    "Narration:"
    "A surge finds the town through an unreinforced channel you thought you'd delayed. The water moves with ease, a flat bright wall that slaps into the bookshop's stoop. Papers lift like startled birds. Your mouth tastes like iron."

    maya_serrano "Mrs. Alvarez, now. We go now."

    "Mrs. Alvarez" "My ledger—"

    maya_serrano "We will get the ledger, but we go now!"
    "Narration:"
    "You haul her arm, bracing as the first wash hits the floor. Her feet slip on soaked wood; time stretches in the greasy slow-motion of catastrophe. Someone grabs her waist, another reaches for your shoulder. You"
    "feel the cold battering at your knees. The cat darts from a box, hissing, and disappears into the tidal dark."
    "Narration:"
    "Hands find her coat. You wedge your shoulder under her elbows. The world narrows to the sound of wet fabric, the rasp of breath, a sharp, blaming voice in your memory asking whether the plan was"
    "fair. The water carries with it the smell of the sea's guts — rot and salt and something metallic."
    # play sound "sfx_placeholder"  # [Sound: Shouts behind you — a family refusing to leave, crying that this is their house]
    show elias_novak at right:
        zoom 0.7

    elias_novak "Maya! They're not budging! The Hernandez's won't come!"

    maya_serrano "We cannot carry everyone. We can't—"

    elias_novak "You can't choose who lives by a ledger!"
    "Narration:"
    "His voice is flung between you and the flood. You are doing something with your hands and someone is saving a life and someone else is clinging to a doorway because they think their door is the last boundary between them and everything they've ever known."
    "Narration:"
    "A volunteer hauls Mrs. Alvarez out; someone mops at a sodden stack of books like a futile priest. Later you will count what is lost: the smell of mildew, the soft collapse of spines, the black"
    "lace of mold crawling across covers. Right now you are beneath a sky that has forgotten mercy."
    # play sound "sfx_placeholder"  # [Sound: Sobs, angry words, the slap of waves retreating]
    show noah_kestrel at center:
        zoom 0.7

    noah_kestrel "We have emergency grants lined for salvage — temporary units, relocation funds. If we mobilize the public works crew—"

    elias_novak "Because nothing says 'community' like corporate trailers. Give me a break."

    noah_kestrel "It's not corporate if it saves people, Elias."

    elias_novak "Everything becomes corporate if you let them name it first."
    "Narration:"
    "The exchange is knives in conversation: Elias incandescent, Noah restrained. You stand between them and the puddled ruin, the taste of iron in your mouth a constant drumbeat. Your throat is raw."

    maya_serrano "Stop. Both of you—stop.' (You force the command like a wedge into warm earth.) 'We will salvage what we can. We will get Mrs. Alvarez to the sanctuary. We will not turn this into a fight right now."

    elias_novak "Maya, this is what we warned about. People told us—"

    maya_serrano "I heard you. I planned it. We're doing everything—"
    "Narration:"
    "You hear your own voice as if through water: the edges blur. The crowd's murmurs shape into words you have heard before — 'elitism,' 'you decide who's worth saving,' 'top-down.' Accusations land not as arguments but as a physical force that knocks the wind from you."
    hide maya_serrano
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "We set up kitchens. We took names. We didn't come here to take homes; we came to keep you alive. Sit down, please. Let them—' (She looks at you.) 'Let them help."
    "Narration:"
    "Rosa's eyes are fierce; she can be small and furious and vast all at once. Her intervention stitches, for a moment, the torn edges of the assembly. But later, in the way people's stares slow-cook into distrust, you will see the crack lines deepen."
    "Narration:"
    "You move with Mrs. Alvarez to the rooftop sanctuary. Hands pass crates to your volunteers — a flurry of damp hope and exhausted compliance. Finn's face is chalked with an absurd, brave calm."
    hide elias_novak
    show finn_serrano at right:
        zoom 0.7

    finn_serrano "The cat showed up under a crate. I swear."

    "Mrs. Alvarez" "Bless you, child."
    "Narration:"
    "You think that saving a single life should be enough to keep guilt at bay. It isn't. Because while one life is saved, a communal bookshop — a repository of the town's memory — is ruined,"
    "its pages stuck together in a wet, useless allegiance. You imagine mold creeping like a sentence across your plans."
    hide noah_kestrel
    show maya_serrano at center:
        zoom 0.7

    maya_serrano "I wanted to protect them without taking their autonomy."
    "Narration:"
    "The thought is a wound. The accusations are not new; they gather like storm clouds, predictable and cruel. You taste iron and wet wood. You feel culpable not because you did nothing, but because every action required choosing who stays and who moves, who keeps and who loses."
    hide rosa_alvarez
    show elias_novak at left:
        zoom 0.7

    elias_novak "You think anyone chose this, Maya? Do you?"

    maya_serrano "I—' (You have no clean answer. You never did.) 'I chose to try."

    elias_novak "Try like that and people will call it choosing for them."
    "Narration:"
    "He doesn't look unreadable; his face is open and wounded and complicated. The Schrödinger ache — the knowledge that whatever tenderness once existed between you is now braided with political difference — sits between you like a new kind of tide."
    # play sound "sfx_placeholder"  # [Sound: Evening bells of the sanctuary; the wet hiss of generators pulling power]
    # play music "music_placeholder"  # [Music: A single mournful piano note repeats like a heartbeat]
    "Narration:"
    "You walk the rooftop edge, the town spread below like a map in a flood. Families sleep in small clusters under tarps. The salvage teams sort soggy volumes; volunteers take turns staring into the dark. In"
    "the distance, Mayor Lillian's press vehicle idles like a beetle; someone will speak and someone will shout and everyone will decide that this is either your moral failure or your necessary cruelty."
    "Narration:"
    "Your notebook is heavy in your pocket. The red thread around your wrist rubs raw. You replay every decision and see it in multiple lights: as necessary, as arrogant, as the only thing that kept some people breathing."

    maya_serrano "What do you want me to do, Finn?"
    "Finn: (after a beat) 'Keep doing it. Even if they yell. Even if it breaks you. We'll hold the ropes.'"
    "Narration:"
    "His answer is both balm and indictment. The shelter holds but the seams strain."
    "Narration:"
    "You look out over the water line. Somewhere, the channel you thought secure eddies and rearranges itself. In the bookshop below, someone will sleep on a soggy chair and wake to the smell of mold. In the sanctuary tents, a child will ask when they can go home."
    "Narration:"
    "You imagine the ledger of the town — names crossed, names circled, a list with too many empty boxes."
    # [Scene: Rooftop Sanctuary — Dusk]
    hide finn_serrano
    hide maya_serrano
    hide elias_novak

    scene bg ch11_e67f19_4 at full_bg
    # play music "music_placeholder"  # [Music: Low strings, unresolved; the cadence of questions without answers]
    "Narration:"
    "You stand at the edge, breath steaming in the damp air. The town murmurs into the night like a congregation of broken clocks. You bear the weight of the decisions you made and the ones you"
    "deferred. Loneliness tastes like iron and wet wood; it lodges in your gut like an old splinter. You think of promises, of the red thread dull against your wrist."
    "Narration:"
    "A volunteer hands you a radio. Voices move in static — reports, complaints, a child's sleep-broken call for a parent. Someone mentions a family still refusing relocation at the pier. Someone else mentions that a public works crew is on its way but might be too late."
    "Narration:"
    "Your hands tremble. You breathe. You listen to the town make its demands and its accusations."
    "Narration:"
    "Page-turn thought: If the plan fractures here, what will you do next?"

    scene bg ch11_e67f19_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter14
    return
