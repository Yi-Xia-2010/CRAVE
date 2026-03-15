label chapter6:

    # [Scene: Marsh | Dawn — First Winter Thaw]

    scene bg ch6_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The marsh breathes: distant gulls, a low, steady swell, the creak of soaked ropes, the whisper of reeds rubbing together]
    # play music "music_placeholder"  # [Music: Swelling strings with a brisk, hopeful tempo; percussion tapping like heartbeats]
    "You wake before the sun, because the marsh woke you months ago — its subtle calendars folded into your bones. Your boots find the wet earth almost by memory. Frost melts underfoot, the ground exhaling cold"
    "steam that tastes faintly of shellfish and iron. In your hands, your notebook is damp along the edges where you paused handwriting to watch a tideline. The locket is warm against your sternum."
    "There is a rumor of movement at the far edge — a curtain of white where the bay meets the recovery beds. Mateo is already there, a silhouette against the watery glow, hands in the pockets"
    "of his vest, blueprints rolled in a tube at his side. He turns when he senses you, and for a second the whole world narrows to the soft, immediate recognition of his face."
    show mateo_ros at left:
        zoom 0.7

    mateo_ros "Morning. They're beginning the flow test sooner than we thought. Council pushed it up after the stormwatch dropped to yellow."
    show aiko_navarro at right:
        zoom 0.7

    aiko_navarro "So soon.' You close the distance and the cold wind rakes your hair into a halo. The smell of algae is stronger near the waterline, the air thick with wet growth. 'Did we—did everyone get the new schedules?"

    mateo_ros "Ivy and the morning crew took the east quadrant. Tala has volunteers at the nursery. Rohan wanted to check the old tide markers himself. We have the stipend payroll queued — community labor team will be on site when the surge comes."
    "You feel the list of practicalities settle like ballast. The scaffold's success depends on timing — on hands and on a choreography of small, exact moves. You think of every night you pitched over plans with"
    "Mateo, his calm elbow nudging a stubborn fact into order until it sat where it could be handled."
    hide mateo_ros
    hide aiko_navarro

    scene bg ch6_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant horn from the docks; the low murmur of radios; the wet slap of boots on a wooden gangway]
    "Old Man Rohan approaches, his hat bristling with sea spray. He carries the old brass marker pole — the one with notches from storms decades ago — like a worn talisman."
    show old_man_rohan at left:
        zoom 0.7

    old_man_rohan "You did good, girl. Can't say I thought I'd see willow scaffolds hold against a winter like this."
    show aiko_navarro at right:
        zoom 0.7

    aiko_navarro "You did more than 'think', Rohan. You taught me how the marsh listens."
    "Rohan's grin cracks like weathered wood, and he shifts the pole into the mud with a practiced hand, measuring the new high-water line. His fingers smell of iodine and fresh-cut marsh hay."

    old_man_rohan "Listen now. When it sings, you listen. And when it keeps the song, then you celebrate."
    "Your chest clenches with something like relief and the sharpness of fear at once. The testing window narrows: a late-season swell, wind lines converging along the coast, a gray roll of water that could either test infrastructure or undo it."
    hide old_man_rohan
    hide aiko_navarro

    scene bg ch6_4001e7_3 at full_bg
    # play music "music_placeholder"  # [Music: Strings build; tempo accelerates]
    "Ivy appears from the east quadrant, sleeves rolled, hands red from cold. Her laugh when she sees you is immediate and bright enough to cut through the morning fog."
    show ivy_navarro at left:
        zoom 0.7

    ivy_navarro "Payroll confirmation came through. First stipends hit. People are here because they can pay the rent this month, Aiko. They can patch the roof. We didn't just plant grass; we planted paychecks."
    show aiko_navarro at right:
        zoom 0.7

    aiko_navarro "We planted skills, too. Training certificates went out last night — marsh maintenance, monitoring protocols. We're not just hiring labor; we're certifying stewards."

    ivy_navarro "Stewards with lunch packs and hot coffees. Tala's volunteers brought chili.' (she winks) 'And Mateo actually remembered thermoses this time."
    show mateo_ros at center:
        zoom 0.7

    mateo_ros "Hey — I remember important things. Like your stubbornness when a channel won't settle."
    "You exchange the kind of teasing that has room in it for something softer: mutual reliance, a tether that has tightened through work."

    menu:
        "Check the east quadrant sensors with Mateo":
            "You and Mateo kneel by the slate-covered sensor array. Your hands work in sync — his movements patient, yours decisive. The sensors ping green. He says, quietly, 'We did it.'"
        "Walk the nursery beds with Tala and Ivy":
            "You follow Tala through the low-lit nursery; trays of cordgrass shiver with condensation. Tala points to a tray where seedlings hold their own against algae blooms. She squeezes your shoulder. 'Your stubbornness is contagious,' she says, and you feel it like warmth spreading."

    # --- merge ---
    "Continue"
    hide ivy_navarro
    hide aiko_navarro
    hide mateo_ros

    scene bg ch6_4001e7_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rapid, purposeful sounds: hammer taps, knot-tying snaps, calls across channels; a unified cadence like rowing]
    # play music "music_placeholder"  # [Music: Percussive strings; the score shifts into a march-like momentum]
    "The swell comes with a breath of violence. The sky bruises purple and slate; wind begins to hurl itself along the promenade. The community forms a human net: volunteers brace ropes, fishers guide planks, youth run"
    "supply shuttles across mud. You move through the crowd like water through reeds — issuing instructions, bolstering hands, smoothing frayed nerves."
    show tala_kumari at left:
        zoom 0.7

    tala_kumari "Seal the nursery tarps! East quadrant, watch the northern break — brace the lower tiers!"
    show ivy_navarro at right:
        zoom 0.7

    ivy_navarro "We've got sandbags! Pass them here!"
    show mateo_ros at center:
        zoom 0.7

    mateo_ros "Hold the secondary anchors. If the scour starts, we pull the mats inward and let the front row take the brunt. Don't panic if the front loses some material — prioritize the nodes."
    hide tala_kumari
    show aiko_navarro at left:
        zoom 0.7

    aiko_navarro "Keep the channels clear. If sediment caves over the new root nodes, we lose months. Rohan — mark the old notch! If tides push past that, we shift personnel to emergency defenses."
    hide ivy_navarro
    show old_man_rohan at right:
        zoom 0.7

    old_man_rohan "Aye. I'll call the markers. Keep the kids on the cable line. They'll keep their feet."
    "The storm clamps down. For a breathless, suspenseful minute everything is loud and shapeless. The scaffolds flex, willow joints groan like the hull of an old boat, mud sloshes. Your heart pounds in a rhythm that"
    "matches the storm drums. This is the moment all the modeling and consensus meetings existed to meet: the marsh's first winter test."
    hide mateo_ros
    hide aiko_navarro
    hide old_man_rohan

    scene bg ch6_4001e7_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A collective intake of breath from everyone on site, over the roar of wind and surf]
    # play music "music_placeholder"  # [Music: Orchestral swell into an exultant brass chord]
    "The scaffold holds."
    "The reaction is instantaneous and immense. A cheer that feels volcanic rises from the mud: hands thrust into the air, laughter and sobs braided together. People who had only ever known retreat find themselves standing on land that still exists."
    "Ivy throws her paint-stained arms around you and squeezes so hard you taste salt."
    show ivy_navarro at left:
        zoom 0.7

    ivy_navarro "You did this. We did this, Aiko. Look."
    "You look — and the marsh is not the same as it was months ago. Where desolation once threatened, pockets of green now wink like lanterns: clumps of cordgrass shimmering with new shoots, fiddler crabs darting"
    "into channels, a pair of dunlins skittering along a mudflat. Bioluminescent cultures in small vials at the Tidepark are abuzz, their data blinking affirmative on handhelds. The work you designed is imperfect, messy, but alive."
    "Mateo Ríos finds you in the chorus of celebration, his face open and wet with spray, and pulls you out of the crowd with a laugh that is equal parts incredulity and relief."
    show mateo_ros at right:
        zoom 0.7

    mateo_ros "We worked our asses off,' he says, grinning. 'And your obsession with redundant anchors—"
    show aiko_navarro at center:
        zoom 0.7

    aiko_navarro "—and your municipal forms—"

    mateo_ros "—and your municipal forms that nobody else could sneak through the red tape.' (he gets quiet, more intimate) 'Aiko, look at this. Look at what we—what everyone—did."
    "You lean your forehead against his shoulder, and for a moment the loud world falls away. The tide still moves and decisions still spread like ripples, but there is a hard, joyful tether between you."
    hide ivy_navarro
    hide mateo_ros
    hide aiko_navarro

    scene bg ch6_4001e7_6 at full_bg
    # play music "music_placeholder"  # [Music: Strings soften to a warm, sustained chord; a distant chorus of community voices hums like a benediction]
    show old_man_rohan at left:
        zoom 0.7

    old_man_rohan "Council will see this. They will see we can hold a line that doesn't sell our souls."
    show tala_kumari at right:
        zoom 0.7

    tala_kumari "We have data and labor, and those stipends mean the kids can stay in town. We can argue the rest in a room with charts. But right now — right now — we have habitat."
    "You feel your vision tilt into perspective: the marsh's survival is not a single victory but a hinge. Some cottages still must move; some livelihoods must transform. The pain of those losses sits beside the joy"
    "like a quiet stone. You hold both of those feelings with the kind of care you ask of your seedlings."
    # [Scene: Docks | Midday — After the Surge]
    hide old_man_rohan
    hide tala_kumari

    scene bg ch6_4001e7_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Laughter, hammering, a radio broadcasting a local song]
    # play music "music_placeholder"  # [Music: Upbeat folk strings layered with bright woodwinds]
    "Councilor Nguyen walks the docks with a clipped, impressed smile. He stops at your side and studies the area with the discreet calculation of a man who understands politics as well as tides."
    show councilor_nguyen at left:
        zoom 0.7

    councilor_nguyen "You had foresight and grit, Ms. Navarro. The council will be impressed by footage already circulating. This... this gives us leverage."
    show aiko_navarro at right:
        zoom 0.7

    aiko_navarro "Leverage to protect the places that matter. Leverage to redirect funds to training, not just concrete. We can scale this — teach other towns modular stewardship — but it must include local governance."

    councilor_nguyen "A governance council? Fishers, youth representatives, a municipal liaison? That will be a hard sell to some. But the optics are persuasive. The people were here today."
    "Mateo Ríos stands slightly behind you, the roll of blueprints uncurled now to reveal annotated adjustments to the pilot. He meets your eyes and offers a small, firm nod: a covenant of continuing collaboration."
    show mateo_ros at center:
        zoom 0.7

    mateo_ros "We'll draft the governance bylaws. We'll include labor stipends, rotating stewardship, training pathways. The municipal match goes to an endowment which the council helps oversee — with clear terms."

    aiko_navarro "And community veto powers on large contracts. No unilateral fixes that displace people."

    mateo_ros "Agreed. We'll codify it. We'll bring Rohan's markers into the council as advisory artifacts. We make this durable."
    # [Scene: The Aquarium - Community Hub | Late Afternoon — Celebration]
    hide councilor_nguyen
    hide aiko_navarro
    hide mateo_ros

    scene bg ch6_4001e7_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low chatter, the clink of cups, an old radio murmuring a coastal ballad]
    # play music "music_placeholder"  # [Music: Gentle, triumphant piano and cello; voices swell into an intimate chorus]
    "You stand at the edge of the room, watching. Tala organizes an informal certificate ceremony for the new stewards. Ivy distributes hot bowls to volunteers whose boots are still caked with mud. Rohan sits back, hands"
    "clasped around a cup, the map of the old coastline folded on his lap like scripture."
    show tala_kumari at left:
        zoom 0.7

    tala_kumari "This is the start of something we run together. Not a charity fix. Not a lab experiment. This is homegrown resilience. And you're all stewards now — not just hired hands."
    "A handful of young people cheer, and someone hoists a makeshift banner: MARISMA STEWARDS. The room fills with warmth that is larger than any single person."
    "Mateo Ríos squeezes your hand in the dim — a familiar, quiet pressure."
    show mateo_ros at right:
        zoom 0.7

    mateo_ros "We should put our names on this, in the bylaws. Not to claim it, but to pledge ourselves to it. You in?"
    show aiko_navarro at center:
        zoom 0.7

    aiko_navarro "Yes. And we'll make sure the bylaws are written in plain language — accessible to everyone. We'll host trainings at the Aquarium. We'll make the nursery part of the school curriculum. We'll bring other towns in as partners, not clients."

    mateo_ros "That's the co-design I keep talking about. I'm in — forever this time?"

    aiko_navarro "Forever in the sense of staying and doing this work together. Not that I won't be restless. But yes. We'll keep building."
    "He leans in, and the kiss is small and the world is big: tasted of salt, of cold air, of the damp earth you both love. Around you, people laugh and plan and toast, and the future feels like a construction site you are excited to keep showing up to."
    hide tala_kumari
    hide mateo_ros
    hide aiko_navarro

    scene bg ch6_4001e7_9 at full_bg
    # play music "music_placeholder"  # [Music: Climactic, radiant; choir-like harmonies with a steady, driving rhythm]
    "The governance council forms in the weeks that follow. Meeting rooms fill with voices that used to be sidelined — fishers with wind-creased maps, teenagers with drone footage and fierce commitment, elder Rohan with oral histories"
    "and tide notches. Dr. Selene Park's firm proposes to redirect its engineered scaffolding into modular supports that the community can opt into, with training and full consent. Some houses still need to move inland; resettlement funding"
    "is negotiated with the council's oversight. Labor stipends become a steady payroll for marsh stewards; certification opens pathways to paid regional apprenticeships. The marsh, once tentative, grows complexity: snails, eelgrass sprouts, and returning migratory birds write"
    "new lines on old pages."
    # [Scene: Cliffside Promenade | Sunset — One Month Later]

    scene bg ch6_4001e7_10 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Waves, the creak of plant pockets, distant muffled music from the Aquarium below]
    # play music "music_placeholder"  # [Music: Soft piano with lingering bright strings]
    show mateo_ros at left:
        zoom 0.7

    mateo_ros "You ever think back to when you were the kid tracing the shoreline on that tiny map you keep?"
    show aiko_navarro at right:
        zoom 0.7

    aiko_navarro "All the time. I used to want to hold the line with nothing but a fishing net and stubbornness."

    mateo_ros "Stubbornness is still useful. But now you have community, science, and a hell of a lot of rope."

    aiko_navarro "And you have bureaucracy. Somehow that helps, too."

    mateo_ros "Aiko. I don't want to make promises I can't keep. But I can promise this: wherever the work goes, we do it together. We design, we fail, we iterate, but we keep the people at the center of every model."
    "You consider his face — the sturdiness of it, the careful, chosen vulnerability. A thousand small choices made to get here fold into this one steadying commitment."

    aiko_navarro "And I won't shoulder it alone. I'll ask for help when I need it. I'll let the council carry some weight. I'll teach others to hold the line with me."

    mateo_ros "Good. Because I plan to annoy you about documentation forever."

    aiko_navarro "Someone needs to keep the forms legible."
    "He laughs, and the buoyant sound mixes with gull calls. The cliff air tastes of salt and the faint smoke of a distant community grill. For a moment you are dizzy with gratitude — for the"
    "team, for the losses transformed into careful gains, for the person beside you who has become a partner in both practice and heart."
    hide mateo_ros
    hide aiko_navarro

    scene bg ch6_4001e7_11 at full_bg
    # play music "music_placeholder"  # [Music: Swells to a triumphant yet intimate chord]
    "Ivy finds you both and flings an arm around your shoulders, sealing the tableau with familial intimacy."
    show ivy_navarro at left:
        zoom 0.7

    ivy_navarro "We're writing a guide for other towns. We called it 'Marisma Modular' — little bits of place-based solutions stitched together. You wrote the introduction,"
    show aiko_navarro at right:
        zoom 0.7

    aiko_navarro "Only because you wrote the foreword."

    ivy_navarro "Future's bright, huh?"
    "You look at the marsh, at the little boats bobbing like held promises, at the children collecting shells with a patience you haven't seen in them before. There are costs. There were tears. There were relics left behind. But the arc leans toward repair."

    aiko_navarro "It's durable,' you say. 'Not perfect, not permanent, but durable."
    # play music "music_placeholder"  # [Music: A final, uplifting chord; the rhythm slows gently into warmth]
    "Mateo squeezes your hand. You let your head tilt against his shoulder and listen to the evening: the marsh breathing, the distant clink of celebration, the quiet plans that will keep being made. Love, in its"
    "practical form here, is not an escape. It is the scaffolding: steady, adaptive, and shared."
    hide ivy_navarro
    hide aiko_navarro

    scene bg ch6_4001e7_12 at full_bg
    # play music "music_placeholder"  # [Music: Gentle, affirmative piano notes; sounds of community fade to a steady hum]
    "You open your notebook one last time and write a single line across the page, the letters sure and unshaken by weather: We build together. You close it, feeling the neat click of the cover like a small, legal promise."

    scene bg ch6_4001e7_13 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The marsh's steady song — surf, wind, laughter like a woven rope]
    # play music "music_placeholder"  # [Music: Final crescendo, then gentle fade]
    "You let the moment sit inside you, vast and warm. Around you, decisions will still be made, arguments will flare, hard work will continue. But this winter's test is a proof: community-led resilience can hold. Economies"
    "can be remade to pay for care; governance can be reshaped to include those with salt in their hands. Love can be a form of management too — deliberate, attentive, and gradual."
    "You lift your face to the coming dark and feel, without needing to name it, that you have changed the arc of something larger than either of you. That knowledge sits like the tide underfoot: inevitable, steady, life-giving in ways that are often quiet and occasionally spectacular."

    scene bg ch6_4001e7_14 at full_bg
    # play music "music_placeholder"  # [Music: Soft piano thread, ending on an assured major chord]
    "You breathe out. The marsh breathes back."

    scene bg ch6_4001e7_15 at full_bg
    "THE END"
    # [GAME END]
    return
