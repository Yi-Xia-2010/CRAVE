label chapter7:

    # [Scene: Construction Site | Morning]

    scene bg ch7_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant clatter of machinery, shouted directions, gulls complaining]
    # play music "music_placeholder"  # [Music: Urgent strings with steady percussion]
    "You arrive with the tide still low and the walls half-born — slabs of pale concrete stacked like teeth against the ocean. The air tastes of wet cement and salt; each breath feels thin and metallic."
    "Your boots sink a little in the churned mud where excavators have turned the shore into a scaffolding field of pipes and orange tape."
    "You think of the meeting two nights ago: the hum of cameras, the weight of eyes, the brass of the compass on the cord at your throat when you stood and spoke for Iris. That memory"
    "carries like a live wire through your chest — not regret exactly, but a steady current of consequence."

    scene bg ch7_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Footsteps on wet decking]
    show iris_varela at left:
        zoom 0.7

    iris_varela "We're on a schedule, Mara. The crews have sixteen hours of pumping left before the tide window tightens. People are already calling to ask when they can sleep without fear."
    show mara_serrano at right:
        zoom 0.7

    mara_serrano "They're sleeping more easily tonight.' You keep your voice level. The fact settles in your ribs like ballast. 'The elevated walkways are holding. Insurance lines called me this morning and — they were concise."

    iris_varela "Concise is better than nothing. We bought time. We kept homes."
    "Her eyes scan the horizon as if measuring distance instead of weighing faces. There's a clarity to her that is not kinder for being clear. You feel it: the practical satisfaction of something working."
    "Behind her, Elias Park stands beside a pallet of sensors, sleeves rolled, fingers stained with sea salt and tool grease. He is small against the machinery, adjusting a moisture sensor as though the device's calibration can translate his feelings into numbers."
    show elias_park at center:
        zoom 0.7

    elias_park "Readings are within expected variance. The berm is damp, but stable. The wave deflection is performing well against the modeled storm set."

    mara_serrano "You've been helping them with the sensors?"

    elias_park "They asked. I said I'd consult. I preferred a different design, but —' He looks at the structure and then at you, measuring what to say. 'It mitigates impact. People sleep."
    "He leaves the sentence suspended, the small concession heavy with what is left unsaid. His hands find the sensor casing and twist a screw, an action that steadies him more than his words do."

    iris_varela "We needed decisive action. Your support made the funding move. You understand how municipal timelines work.' Her tone is factual, tight. 'We don't have the luxury of slow experiments."

    mara_serrano "I understand timelines.' You touch the compass at your chest without thinking, thumb tracing its worn rim. Its brass is cool and familiar. 'I also saw the bids — the coves will be filled, moorings restricted. Some fishers will lose access."

    iris_varela "We prioritized population centers. We prioritized schools, hospitals, and where most families live. Some access will change, yes, but —"
    "You cut in because waiting will only let the machines' noise fill the space. 'But the fishing spots are livelihoods, Iris. Filling coves changes currents, confuses fish patterns. It's not just access — it's how people eat and earn.'"

    iris_varela "We will set aside compensation and relocation support. We will create alternative mooring plans. You know the alternative was more crowded evacuation shelters and permanent displacements."

    mara_serrano "I know.' The word thins the air. 'I know what you chose, and I know why we did it."

    menu:
        "Step closer and point at the sensors":
            "You move forward and run a gloved hand along the nearest sensor array, the small LEDs flickering. Elias glances up, and for a beat your hands are in the same space."
        "Stand back and watch the crews":
            "You stay on the edge of the work zone, watching the backs of the workers bending and lifting. The rhythm of the crews feels like a new, brittle heartbeat for the town."

    # --- merge ---
    "The conversation continues as Elias speaks about iteration and data."

    elias_park "Mara — I didn't want to be sidelined either. But we can make these systems do better if we keep iterating. If we get data in the next rains, we can adjust placement, reduce ecological strain."

    mara_serrano "And who will be the one to explain another iteration to a fisher who lost a mooring this week?"
    "Elias looks away and pins his jaw. His optimism is a tool he must hold deliberately; you can see the effort. The political sidelining has not stripped his kindness, only pressed it into narrower shapes."

    elias_park "We'll have to do it together. I can help with grants for community-led mooring redesigns. I can—"

    iris_varela "We don't have time for 'together' on every detail, Elias. This operation scales now or people pay with roofs and lives."
    "Her foot taps a rhythm that matches the percussion under the music in your chest. You feel the morning accelerating — plans made, heavy equipment already moving sand and sea."
    # [Scene: Promenade | Midday]
    hide iris_varela
    hide mara_serrano
    hide elias_park

    scene bg ch7_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The surf is muffled by the new barrier; conversation rises in pockets; the wind tugs at banners]
    # play music "music_placeholder"  # [Music: A faster tempo, staccato strings]
    "Abuela Rosa stands with her cane against the railing, eyes on the water. Her weathered hand squeezes the wood until the knuckles go white; she does not cushion her words with politeness."
    show abuela_rosa at left:
        zoom 0.7

    abuela_rosa "La mar se acuerda. The sea remembers what you took.' Her voice is not accusation alone; it's a memory that opens like a wound. 'You can stack stone higher than a man's head and she will still remember the smell of the boats. She'll remember the rope you tied at the stern."
    "You step close; the wind steals the edge of your scarf and flings salt into your hair. Abuela's face holds the slow gravity of someone who has seen seasons and storms enough to read their moods like weather charts."
    show mara_serrano at right:
        zoom 0.7

    mara_serrano "I thought — we thought — that if we could stop the floods, we'd keep the rest.' Your voice fractures where certainty meets complexity. 'I thought saving houses would let life go on."

    abuela_rosa "You saved them a roof. You changed the sea's path. People eat in different ways now. That is not small. It is the thing you cannot unmake."
    "A group of fishers has gathered below, voices jangling. One of them, a man with a sun-creased face and a beanie — his boat, half-mooring, looks stranded by a new concrete apron — calls up."

    "Fisher Mateo (not your Mateo)" "You promised consultation! Now I can't land the sloop without climbing a ladder we didn't own before."

    mara_serrano "We'll work on compensations. We'll find you mooring. Tell me what you need."

    "Fisher Mateo (angry)" "You told us the town needed choices. We were told that choice would include our boats. Now the choice is made for us."
    "Your hands close around the compass. It feels like an anchor and a question both. You want to say the right thing — to honor loss and also name the relief — but speech is clumsy and political in the face of raw livelihood."

    menu:
        "Offer to arrange a meeting with Iris":
            "You promise, and the fisher's jaw tightens. He nods slowly, not because he trusts you — yet — but because he wants avenues, not platitudes."
        "Sit silently and listen":
            "You stay quiet and let the tide of anger wash past you. The fisher's words land with a thud in your chest; silence amplifies what you can't fix on the spot."

    # --- merge ---
    "Abuela Rosa urges action and listening; the need for concrete plans becomes the focus."

    abuela_rosa "You chose to step up in Council. You must also step in now — not only to justify but to mend. People will not be held by reason alone."

    mara_serrano "Mend how?"

    abuela_rosa "With listening that becomes action. Not promises. Plans. Paths."
    "Her words slice through the breeze like a map. Plans can be drawn. Paths can be made. But they demand time and handwork and compromises that smell like ordinary grief."
    # [Scene: Council Hall | Evening]
    hide abuela_rosa
    hide mara_serrano

    scene bg ch7_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Voices layered over one another, a captured hum of heated civic life]
    # play music "music_placeholder"  # [Music: Crescendoing strings, urgent, pulsing]
    "The hall is fuller than before — more faces, more heat. The berm's early stabilization has attracted both gratitude and a new roster of critics. Some people are here with banners thanking the city for sleep;"
    "others carry small laminated photos of boats and nets. Investors sit with tight smiles; municipal staff shuffle papers."
    "You take the center podium because everyone still looks to you for how to frame the fallout of your endorsement. The brass of your compass clicks softly against the lectern when you shift."
    show mara_serrano at left:
        zoom 0.7

    mara_serrano "Thank you all for coming. Tonight is to talk about the next steps. Compensations, moorings, and monitoring."
    "From the floor a woman stands — her voice going sharp. 'Compensation doesn't bring back the way my husband used to fish. It brings money that cannot reel a fish.'"
    "A man in the back shouts, 'You sold us out for concrete and contracts! How many homes must stay dry before you admit the cost?'"
    "The room tilts into a volatile mix. Applause from one corner, boos from another. You feel the hall's air thicken with the press of bodies and expectations. The arousal is high: people demand answers now, not later. The pace of conversation is jagged, punctuated by rapid-fire accusations and pleas."
    "Iris Varela stands at the city table, hands folded, eyes fixed. When she speaks it is tight and logical."
    show iris_varela at right:
        zoom 0.7

    iris_varela "We prioritized the maximum number of lives protected under the funding we could secure in time. That is leadership. That is what this moment required."
    "A voice near the front — a young teacher — speaks in a voice that trembles with relief. 'My class can come back. The children can sleep without wakings. You did that.'"
    "You watch Elias in the doorway. He is a silhouette against the light, leaning on the jamb, fiddling with his camera as if it were a tool to understand the room. He looks small and very"
    "human in that doorway, a man who believes in refinement and now watches blunt force make whole some things and fracture others."
    show elias_park at center:
        zoom 0.7

    elias_park "I didn't want this to be the only answer. But it's working for them now, for a lot of them. That's not nothing, Mara."

    mara_serrano "No, it's not nothing.' Your voice presses forward to meet the room. 'I know it keeps people home tonight."
    "Then the front-row fisher — not the earlier Mateo, but another whose mooring sits half-buried — stands and points at the investors in expensive coats."

    "Fisher Navarro" "And what about us who have to change the way we feed our kids? Will your compensation teach my son how to mend a net that doesn't belong in his hands anymore?"
    "An investor's assistant flinches. The assistant's phone buzzes; a message flickers across the screen — a tally, a schedule, a risk matrix. It is clinical and cold in the face of Navarro's hands, knuckled and salt-roughened."
    "The room fractures into shouting. Someone bangs a placard on the table. The municipal clerk calls for order and is drowned by a chorus of grievances and gratitude alternating like surf."
    "You stand there wanting to fold both currents into a single adoption — the relief and the loss — and failing. The hall is an ocean with cross-currents. Every decision has left its wake."
    hide mara_serrano
    show abuela_rosa at left:
        zoom 0.7

    abuela_rosa "Listen."
    hide iris_varela
    show mara_serrano at right:
        zoom 0.7

    mara_serrano "We will schedule listening sessions. We will fix mooring as priority one. We will route a team to discuss compensation with each fishing family."
    "But the heat has swelled too fast for plans alone. The room's voices press in — urgent, relentless."
    hide elias_park
    hide abuela_rosa
    hide mara_serrano

    scene bg ch7_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A single, high bell from the corridor — an alerts tone used for municipal communications — goes off twice, sharp and insistent]
    # play music "music_placeholder"  # [Music: The strings spike to their highest, then cut to a thin, vibrating sustain]
    "You hear that bell and, for a moment, everything sharpens: the clang of machinery, the cry of the fishers, the soft tapping of the investor's phone. Relief and resentment sit side by side in the room"
    "like two people forced to share a bench. Your decision to back Iris bought time and solidity; it also set off a chain of displacement and limitation that people are now naming with loud, human voices."
    "Your pulse thunders in your ears. The arousal that has been building through the day — the urgent rhythms of machine and argument, the quickened breathing of a town rearranging itself — reaches its peak."
    "You look out across the crowd, at faces carved by different truths: gratitude, anger, exhaustion, hunger for certainty. You realize that the stabilization you helped authorize has changed more than the shoreline. It has redrawn how people will live here and how they will remember you."
    "You swallow. The podium is cool under your palms. You feel the compass warm at your throat like a small, private insistence."
    "A hush gathers — not yet peace, but the pause before whatever you say next reshapes the room again."

    scene bg ch7_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Abrupt low hum]
    "You could speak and steer the conversation; you could stay silent and let the town's voices realign without you. Either choice will set the next tempo for Puerto Alba."
    # [Page-Turn Moment: The bell's echo hangs, the murmurs renew, and you feel the exact center of the storm — the place where safety, sacrifice, and memory collide. You draw a breath and the next thing you say will pull the room one way or another.]

    scene bg ch7_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter8
    return
