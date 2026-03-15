label chapter7:

    # [Scene: Solace Harbor Promenade | Late Afternoon]

    scene bg ch7_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant vendor calls, a gull alarm, fabric snapping in a steady breeze]
    # play music "music_placeholder"  # [Music: Low, percussionless hum — a slow-building tension]
    "You step into the knot of bodies like stepping into a tide: warm at the surface, undercurrent pulling everything toward something larger. Nova is there before you fully arrive — a bright shard of motion under"
    "a patched tarpaulin, her platinum undercut catching the angle of the sun like a promise and a warning. Around her, people cluster: neighbors with damp hair, students with clipboards, an older woman with a lifetime of"
    "sea-knowledge folded into the lines at her mouth."
    "Samir is at your elbow before you can steady the notebook against your ribs, his presence like something you grew up with—familiar, sturdy, a bridge between the nervous part of you and whatever plan is forming"
    "in the air. He presses a smear of printed testimony into your hand; the paper is already creased from five other palms."
    show samir_reyes at left:
        zoom 0.7

    samir_reyes "Look—these from Ebbett, and the culvert testimonies from the alleys. She wrote the dates in the margins. If we map them to the elevations, people can see why the city can't just say 'we'll hold.'"
    "You feel the compass at your throat, brass warm against your skin. You let your fingers splay over the paper; ink smudges the pads of your thumbs, a familiar, honest stain that steadies you."
    show mara_lin at right:
        zoom 0.7

    mara_lin "I'll overlay them with the 2030 model and the high-tide projections. If we show where foundations will be undermined, where insurance won't follow, this isn't theory—it's people's doors."
    "Samir: (rubbing his knuckles) 'Exactly. They need the topography, not the rhetoric. Nova's already started drafting the community map.'"
    hide samir_reyes
    hide mara_lin

    scene bg ch7_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A megaphone coughs; someone hands it to Nova; a chant starts, low and building]
    # play music "music_placeholder"  # [Music: Minor strings, distant and insistent]
    "Nova Duarte looks up when you speak. For a beat, her face is unreadable: an intensity that could be welcome or accountancy. Then she closes the space with words that are not gentle, because the situation hasn't earned gentleness."
    show nova_duarte at left:
        zoom 0.7

    nova_duarte "We don't have time for polite compromise, Mara. The city's timetable protects contracts and concrete, not people. We start with wetlands—managed retreat in the places they refuse to prioritize—and we make the costs of ignoring us politically toxic."
    "You can hear the sharp edge of grief under the mechanics of her sentence—loss braided into strategy. It's familiar, too: the way your own work sometimes hardens around an anchor of memory. Your chest tightens."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Managed retreat—permanent? People will need guarantees. We need a pathway, not just a demand."
    "Nova Duarte: (leaning in) 'Pathways are built when people decide they're moving. Guarantees? We'll make them. We'll hold the city's feet to the fire. But we can't wait for permission.'"
    "Her gaze flicks to your notebook at your hip, then to the compass against your throat. The look is not exactly an appeal; it's a test."

    menu:
        "Flip open my notebook and sketch the retreat boundary right here":
            "You uncurl a damp page, pencil scratching a line that feels like a verdict. The crowd leans in as if the graphite itself is a banner."
        "Keep the notebook closed and listen, cataloging instead":
            "You press the spine of the notebook into your palm, cataloguing names and dates in your head. Listening lets you hear a neighbor's hesitation and a child's cough four stalls away."

    # --- merge ---
    "Scene continues"
    hide nova_duarte
    hide mara_lin

    scene bg ch7_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Megaphone feedback slices the air; a chant becomes a call-and-response]
    # play music "music_placeholder"  # [Music: A single lower string note that refuses resolution]
    "Nova Duarte's voice through the megaphone is raw when she takes it. It scratches and then settles into something that draws people near."
    "Nova Duarte: (into megaphone) 'We will not be moved by promises that are paper-thin! We will not trade our homes for a seawall that only protects a few!'"

    "Crowd" "Protect us! Not profit!"
    "A hand clamps the mic; she steps down and moves through the cluster, her presence like tidewater — inevitable, reshaping everything it touches. She finds you amid the press, and for a heartbeat there is no audience."
    show nova_duarte at left:
        zoom 0.7

    nova_duarte "Mara—you're with us. Good. We need elevations you can trust, not the city's optimistic ones. Samir has testimonies; I have volunteers. Tonight we start going door to door in West Alley."
    show mara_lin at right:
        zoom 0.7

    mara_lin "West Alley floods at two feet. If we can show the exact houses that need relocation, it will be harder for the mayor to paint this as 'minor disruption.' But it will be messy. People will lose addresses. They'll lose belongings."
    "Nova Duarte: (softening, just an inch) 'Loss is already happening. This is about choosing what to lose. And who will stand with us while we lose it.'"
    "Your throat tightens with the memory of a storm taking things you couldn't hold. The city law offices exist to argue ownership of rubble; your compass seems to vibrate with decisions you keep trying to delay."
    # play sound "sfx_placeholder"  # [Sound: A soft buzz — your phone. You glance down; a message glows from Elias. You don't open it at first. The buzz feels like a small electric accusation.]
    hide nova_duarte
    hide mara_lin

    scene bg ch7_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: A single, unresolved chord]
    "You finally let the message show."
    # play sound "sfx_placeholder"  # [Sound: Phone notification ping]

    scene bg ch7_453e40_5 at full_bg

    "Elias Kade (text)" "Mara — I'm not trying to control this. Contracts are in motion that will fund immediate mitigation. If you blockade, permits get pulled, companies walk, and neighborhoods lose even the temporary protection they voted for. Talk to me before you do anything final."
    "A line of words that smells like worry and strategy. He signs off with a careful emoji — a small attempt at warmth that doesn't reach the sentence's teeth."
    "You stare at the screen like you can unthread the implications with your thumb. You think of Elias's arrogance and his earnestness, the way he carries his father's keychain like a talisman against mistakes you both"
    "fear. You think of how his seawall plan was meant to buy time, how his 'quick protection' felt, to Nova and to half the crowd, like a velvet rope dividing who mattered."
    "Samir: (watching your face) 'He's texting. You gonna answer? Or do we need you for canvassing?'"
    show mara_lin at left:
        zoom 0.7

    mara_lin "I'll reply. Briefly. Then West Alley."
    "You type and erase, type and erase. Your training wants neutrality; your history wants justice."

    mara_lin "Elias — I understand the need for immediate mitigation, but a seawall that displaces without consultation isn't protection. We're going door to door tonight. If you really want to help, show up to hear people. That's action, too."
    "You hit send and almost feel the river part. The message is measured — a negotiation disguised as a reach."

    menu:
        "Send a photo of the West Alley map to Elias with a short note":
            "You snap the map and send it. The act feels like inviting him into the room, but the picture is cold and clinical; it will either soften him or harden him."
        "Ignore the texts for now and step into the crowd":
            "You slide the phone back into your pocket. The cold of it against your palm calms you. Your priorities are immediate; bureaucracy can wait."

    # --- merge ---
    "Scene continues"
    # [Scene Transition: The chant melts into organized motion. People grab flashlights and tablets; bicycles and wagons become mobile noticeboards]
    # play music "music_placeholder"  # [Music: Low drums, a storm-bass under the city's hum]
    hide mara_lin

    scene bg ch7_453e40_6 at full_bg
    # [Scene: Sea Barrier Construction Site | Early Evening]

    scene bg ch7_453e40_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain hissing against tarpaulins, the thump of distant engines, the metallic creak of scaffolding]
    # play music "music_placeholder"  # [Music: Sparse piano notes, each one a slow, wet drop]
    "The site is a wound opened against the skyline—an engineered answer to a threat that refuses to be kind. The air smells of diesel and salt and the wet, sharp sweetness of plywood. Mud slicks your"
    "boots the moment you step off the paved access. Bright lights from machines cast long, accusing shadows."
    "A line of municipal security stands where the public road becomes the site perimeter. Their walkie-talkies chatter in polite, clipped sentences. A legal notice, laminated and stern, flutters against a fence-post like a white flag that doesn't mean surrender."

    scene bg ch7_453e40_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Static from megaphones and the soft bark of a city lawyer giving instructions through an earpiece]
    # play music "music_placeholder"  # [Music: Low brass — authority, immovable]
    "Nova Duarte paces the edge of the fenced zone, not toward violence but toward presence. Around her, volunteers lock arms on either side of a line of reclaimed-sailcloth banners that read in blunt letters: PEOPLE BEFORE PROFIT. Rain beads and runs across the letters like tears."
    show nova_duarte at left:
        zoom 0.7

    nova_duarte "This is the first line. We sit, we chant, we photograph. If they try to push us, we document. If they arrest us, we have lawyers on call. We win hearts by making them see the people they swore to protect."
    "You can smell rain on Nova like a second skin. Her voice is compact and precise, but there's a tremor along the edge—the cost she knows this will demand."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Mayor Chen has already hinted at permit revocations if we obstruct. The city's enforcement will be framed as 'public safety.' They will make this about legality, not morality."
    "Samir: (clipping a waterproof sleeve of testimonies to a fence) 'We have Daisies' deposition, the flooding timeline, the insurance refusals. We publish it in waves. If they attack us with permits, we hit them with the proof of non-compliance.'"
    "A municipal officer approaches, bland as bureaucracy."

    "Officer" "Ma'am, you're obstructing a designated construction site. For everyone's safety, you must disperse."
    "Nova Duarte: (without turning) 'For whose safety? For the safety of the seawall contractors? Or the families whose roofs we mapped to fail in five years? The question you ask is who counts as 'everyone' in the first place.'"

    "Officer" "I'm asking you as an officer of the city—leave now, or you'll be trespassing."
    "Nova Duarte meets his eyes with the kind of stare that catalogues consequences. There is a charged hush: your breath fogs, mingles with the rain."
    "Mara Lin: (to Nova, low) 'If they arrest us, the narrative will be messy. People will focus on the spectacle and forget why we're here.'"

    nova_duarte "Let them look at the spectacle. Let them see the faces of people who have nowhere else to go when the walls fail."
    "The officer folds his paperwork with the polite indifference of someone practicing removal by the book. You watch the scene the way you used to watch tides — measuring, predicting, feeling the inevitability. The municipal machine grinds, chrome and procedure grinding against pulse and protest."
    # play sound "sfx_placeholder"  # [Sound: Another phone buzz — Elias again, terse this time]
    hide nova_duarte
    hide mara_lin

    scene bg ch7_453e40_9 at full_bg

    "Elias Kade (text)" "Mara. The mayor just briefed me. If you block that site, they will cut emergency mitigation that was already contracted. This isn't posturing. This is people's roofs."
    "You look up at the line of cranes. Rain umbrellas bob like slow, curious heads. Somewhere behind the fortified fence, a piece of heavy machinery idles, patient and indifferent."
    "You feel something harden inside you. Your stubborn optimism, the tool that keeps you mapping and drafting and negotiating, has taken on a sharper edge—less patient, less willing to be tempered by polite process. The thing"
    "you have refused to become—someone who merely tucks sorrow into reports—threatens to leave the dock."
    "Samir: (soft) 'We're on the line, Mara. This is either the thing that wakes people up— or the thing that gets us all in trouble.'"
    "You think of the families in West Alley. You think of Nova's sister. You think of the seawall slats that might protect downtown offices while pushing water into the creeks where children live."
    "Mara Lin: (to yourself) 'I didn't come back to watch people be negotiated out of their dignity.'"
    "Nova Duarte strides to the front, the megaphone damp with rain. Her voice is steady enough to cut through the coming storm."
    "Nova Duarte: (into megaphone) 'We will stay. We will be visible. We will not let them build their answer on our graves.'"
    "The crowd responds, a low swallow of sound that could either swell into something the city cannot ignore or be written off as another unruly moment."

    scene bg ch7_453e40_10 at full_bg
    # play music "music_placeholder"  # [Music: A long, unresolved string note — heavy, necessary]
    "You inhale the wet air and feel the legal notices and the city lawyers like an approaching tide, each lawyer a current trying to erode the bedrock of the people's protest. Rain slicks your eyelashes. You can taste iron in the wet."
    "Your hands, ink-stained and cold, flex around the notebook. The plan is no longer only on paper — it's in the mouths of neighbors, in the clasped hands along the banner, in the messages that try to pull you back into a procedural middle."
    "Every option feels like loss: the seawall buys time but may doom someone later; the retreat is honest but severs neighborhoods; the blockade is truth made physical and therefore punishable."
    "Your stubborn optimism hardens into something you barely recognize: a strategic fury that sits beside the memory of what the sea took from you when you were younger."
    "You look at Nova. You look at Samir. You look at the fence that separates the city's engineering from the city's people. The rain makes a grid on your vision; the decision ahead is a clean, cold line."
    "You breathe. The crowd quiets, waiting as if the world will tilt depending on what you do next."
    # play music "music_placeholder"  # [Music: The unresolved chord stretches, then narrows into a single, expectant silence]
    "You hold the compass at your throat, and for a long, thin moment you feel the weight of every face here, every map you've drafted, every promise that was broken into driftwood."

    scene bg ch7_453e40_11 at full_bg
    # play music "music_placeholder"  # [Music: Fade to a single, insistent pulse]
    "You know there is no perfect path. Only a doorway you either step through or shut behind you."

    scene bg ch7_453e40_12 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter8
    return
