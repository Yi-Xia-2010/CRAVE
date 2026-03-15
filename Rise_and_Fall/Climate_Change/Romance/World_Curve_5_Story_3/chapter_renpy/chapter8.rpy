label chapter8:

    # [Scene: Boathouse | Dawn]

    scene bg ch8_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of a generator, distant gulls, the muted ping of incoming messages]
    # play music "music_placeholder"  # [Music: Thin, minor-key strings; restrained and uneasy]
    "Narration"
    "You wake to the boathouse feeling smaller than it did last night. The adrenaline has gone thin and cold; where it once gave you purpose, it now sharpens everything that might be lost. The seedlings lean"
    "toward the meager light like small, patient mouths. The smell of peat and wet wood presses under the sharper tang of salt on your jacket."

    "Your wrist still stings where the chain cut into skin; the bruise is a dark reminder of bodies and choices. Volunteers move in the soft interior light — Mika folding a tarpaulin, a teenager cradling a soil tray, an older woman dabbing at her cheek with the back of her hand. Phones glow along a bench like little angry constellations: messages, mentions, screenshots of Atlantech's PR release, a live feed of the mayor's meeting. Someone has posted a notice from the municipality by the boathouse door" "Permits under review—suspend volunteer activity pending investigation."
    "You read the permit notice once, then again. The edges of the paper crinkle under your thumb. Every official stamp feels heavier than the last."
    show amaya_saito at left:
        zoom 0.7

    amaya_saito "Okay. We knew there'd be blowback, but… this is fast."
    show mika_tan at right:
        zoom 0.7

    mika_tan "They always bring paperwork after they bring the cranes. It's the same playbook. They can't just—"

    "Volunteer 1" "What about the grants? The school's field trip—"

    amaya_saito "We keep them safe. We keep the seedlings safe. We document everything. We call the lawyer the council pinned on that board. We don't disperse until we have a plan."
    "Narration"
    "You feel every pair of eyes on you like a weighing. Some appear relieved; others, uncertain. The permit notice is a lever; it makes people think of paychecks, of roofs, of the small slow economies that keep houses whole when storms threaten."

    menu:
        "Read the municipality notice aloud to the group":
            "You read it into the boathouse's dim air. The words hang there like winter fog; volunteers nod, mouths tight. Reading it aloud makes the threat real and mobilizes the lawyer calls."
        "Fold the notice into your pocket and speak of next steps":
            "You fold the paper away, refusing to give it gravity. Your plan-focused voice guides the group to compile documents and footage; the air sharpens with practical purpose."

    # --- merge ---
    "You choose, not because one is braver than the other, but because the room needs either a formal tally or a stubborn, immediate path. Both answers are true: the legal paper is real; so is the steady work of protecting living things."
    # [Scene: Town | Midmorning]
    hide amaya_saito
    hide mika_tan

    scene bg ch8_6b08b4_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmur of the crowd, a distant speakerphone playing a corporate statement, splintered clapping]
    # play music "music_placeholder"  # [Music: A low, unsettling cello, strings tremulous]
    "Narration"

    "News vans cone around the seawall site; a projected feed shows Maren Voss's composed face. Atlantech's statement scrolls beneath her" "Volunteers compromised construction schedules and endangered residents. We will proceed to ensure safety.' The comment stream is a living thing you can't silence — pleas for jobs, calls for caution, thinly veiled threats about 'delays' and 'liability."
    "Elena [wrapped in a scarf, hands folded as if she physically carries weight]: (She does not speak first.)"
    show elena_cruz at left:
        zoom 0.7

    elena_cruz "Amaya. We have calls from the regional council. Business leaders are—' (She stops, searching for a word that won't widen the wound.) 'People are worried about layoffs. They want stability."
    show amaya_saito at right:
        zoom 0.7

    amaya_saito "They want stability. I know. So do I. But stability built on bulldozed marshes won't hold the way we need it to. If we lose this habitat, those same people will have fewer protections when the next storm comes."

    elena_cruz "The injunction complicates things. The council can't be seen supporting an illegal blockade."

    elena_cruz "Some of the longest-standing fishing families... their work has already been threatened by canceled contracts. I have to consider jobs."

    amaya_saito "And I have to consider the wetlands.' (You press your palm to the table where seedlings rest.) 'There has to be a way to not sacrifice both."
    "Narration"
    "Elena's shoulders tighten. The town has divided in ways you can see now — not cleanly, but in the grudging shape of conversations in doorways. You watch two fishermen argue over a cup of coffee; a"
    "middle-aged site foreman shakes his head and keys his truck. The ache in your chest is less about the permit and more about the brittle way hope fractures when stretched between livelihoods and long-term survival."
    # [Scene: Seawall Construction Site | Noon]
    hide elena_cruz
    hide amaya_saito

    scene bg ch8_6b08b4_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A microphone squeaks; a chorus of camera shutters; the mechanical thrum of distant engines]
    # play music "music_placeholder"  # [Music: Cold synth pad, insistent, with a clipped percussive tick]
    "Narration"
    "Maren Voss stands immaculate against the gray of concrete and fog. Her presence is a well-cut sentence; she speaks in a voice that makes certainty sound like a public service. Behind her, a lawyer in a"
    "dark suit holds up a sealed motion. The legal team files an injunction seeking both to compel the continuation of work and to enjoin interference — a move designed to flip the narrative from delay to"
    "danger."
    show maren_voss at left:
        zoom 0.7

    maren_voss "We will not let politicized obstruction endanger the very people we swore to protect.' (She does not look toward the boathouse when she says 'we'.) 'Safety is non-negotiable. Atlantech will continue operations."

    "Reporter" "Ms. Voss, Atlantech's release suggests volunteers risked residents — can you substantiate that?"

    maren_voss "We have safety assessments that speak to the potential for harm when untrained parties interfere with active engineering works. Our priority is clear."
    "Narration"
    "Her cadence is designed to close a conversation. The injunction paper moves through town like a cold current; some officials fold like wet seaweed under its pressure. The PR campaign frames the blockade as endangering people"
    "— and that framing finds purchase in the minds that already fear unemployment more than long-term erosion."

    menu:
        "Step forward to call out Atlantech at the press site":
            "You walk to the edge of the crowd, voice straining but firm. You name the evidence, the volunteers, the data you collected. Cameras catch your words, raw and human; some faces in the crowd soften, others harden."
        "Stay at the boathouse and coordinate evidence uploads quietly":
            "You stay put, focusing on footage, timestamps, legal affidavits. The public eye shifts away from spectacle to the quiet build-up of proof; it is slower, but it might be harder to dislodge."

    # --- merge ---
    "Both choices would be defensible. You weigh spectacle against systems, shouting against slow accumulation. The town watches for what leaders you will be."
    # [Scene: Boathouse | Afternoon]
    hide maren_voss

    scene bg ch8_6b08b4_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain on tin, the click of a fedora strap, Lucas's AR goggles folding shut]
    # play music "music_placeholder"  # [Music: Sparse piano, notes that fall like hesitant steps]
    "Narration"
    "Lucas Herrera arrives as a gust of wet air and a muted practicalness. He carries a compact toolkit at his belt, but his hands are empty. The AR goggles sit above his brow like a promise"
    "folded back. He looks at the seedlings, then at you, and there is an unreadable pause. You know his work, and you know the stakes it brings him — grants, contracts, a future trajectory he cannot"
    "easily unroot."
    show lucas_herrera at left:
        zoom 0.7

    lucas_herrera "I saw the feed. I saw Maren speak. Elena called me from the council asking for technical review. They want stabilization, and—' (He stops.) 'They also asked if I'd be willing to vouch for a mediated compromise."
    show amaya_saito at right:
        zoom 0.7

    amaya_saito "A mediated compromise?"

    lucas_herrera "Yes.' (He folds his hands, searching for simple words for complex things.) 'We can propose a hybrid: limited hard structures in places that most need it, coupled with expanded marsh restoration. It won't be everything you want, but—' (He meets your eyes.) 'It might save the boathouse. It might keep people's jobs. I can publicly endorse it. I can stand with you in the council chamber."
    "Narration"
    "His voice is steady because he has practiced this; you taste the metallic tang of practical solutions shaped by pressure. There is an offer folded into obligation: public vouching in exchange for your acceptance of compromise."
    "The boathouse smell — peat, salt, damp canvas — presses against the shape of the offer. You imagine the seedlings under concrete foundations and the dry, professional language that calls it mitigation."
    show mika_tan at center:
        zoom 0.7

    mika_tan "So Lucas plays diplomat now? You promising to sell us out with a handshake and a stamp?"

    lucas_herrera "I'm not there to sell anyone out. I'm there to keep things from collapsing. This is about minimizing harm."

    amaya_saito "And Maren? Her legal team just filed to force the work to keep going. How can a mediated compromise stop a legal injunction?"

    lucas_herrera "It might not stop the injunction immediately, but public support from engineers can sway the council and give Elena political room. It can slow a bulldozer.' (He holds your gaze.) 'I can speak to the engineering team, to the press. I can make the hybrid plan technically robust."

    amaya_saito "So the cost is that we accept some of their structures. We agree to their involvement in the first place."

    lucas_herrera "It's not clean. I know. But it's not surrender either. It buys us time — and the lab."
    "Narration"
    "The words 'time' and 'lab' sit like two possible futures; both are dear. The lab is not just an asset — it is a promise you made to the town and to your father's memory: a"
    "place for community science, for kids to learn, for seedlings to be raised. Lucas's voice carries the weight of being practical and of wanting to protect you. But his 'buying time' is also a mercantile phrase,"
    "and you feel the old ache: can a compromise keep the heart of the marsh alive?"

    menu:
        "Take the offered tea and listen longer before answering":
            "You accept the cup. The warmth calms you; you listen to Lucas outline logistics and contingencies. His ideas are practical, nearly elegant — but the softness of the moment makes costs more personal."
        "Stand and pace the greenhouse while you respond":
            "You rise, fingers braced on the wooden bench, voice clipped but clear. Pacing sharpens your argument; you press him on who decides which marsh sections are 'most needed' and demand community vetoes."

    # --- merge ---
    "Both reactions are small performances of the larger inner fracture. Taking the tea lets you hear his planned kindness; pacing lets you keep the fire burning."

    lucas_herrera "I don't expect you to say yes now.' (He picks up a seed tray, thumb tracing a sprout.) 'But if we present a plan together — engineers, ecologists, community reps — we can make it harder for Maren to argue that we're obstructionists. We become part of the solution."

    mika_tan "Or we become the solution she paints for a camera and sells to an out-of-town investor while the marsh is paved flat."

    lucas_herrera "I hear that. I hear your anger. I also read the motions. Legal pressure will take the lab before we get headlines. We have to be strategic."

    amaya_saito "And if I refuse?"

    lucas_herrera "Then you escalate. You've already proven you can draw attention. That attention can go national. It can force regulators to actually look at the impact statement — if there's enough pressure. But you risk permits being revoked and the boathouse being shut down."
    "Narration"
    "He lays out outcomes like tradeoffs on a ledger. You flip each one in your head: boathouse gone, or marsh partly sacrificed, or slow rebuilding of public opinion. None of the options is clean; all of"
    "them will shape how the town remembers this moment and how the marsh survives the next storms."
    # [Scene: Town | Late Afternoon]
    hide lucas_herrera
    hide amaya_saito
    hide mika_tan

    scene bg ch8_6b08b4_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmured conversations, the distant clang of metal]
    # play music "music_placeholder"  # [Music: Dissonant harmonies, descending]
    "Narration"
    "The town divides not by shouting alone but by small, concrete things: who is offered work at the seawall and who is not. The local fishmonger takes on a temporary contract; a neighbor's niece gets an"
    "email about layoffs. The social fabric pulls thin threads and tucks them into neat pockets of loyalty. You see people choosing sides with the weary pragmatism of those who must pay rent."
    show elena_cruz at left:
        zoom 0.7

    elena_cruz "There are people saying I should cut you loose to protect other jobs. But others say—' (She swallows.) '—others say your blockade made Maren look heavy-handed and that gave them a reason to listen. I'm trying to hold both. I'm failing at it and I hate that."
    show amaya_saito at right:
        zoom 0.7

    amaya_saito "Elena, listen. We need a clear front. We need to choose tactics that won't hollow us out."

    elena_cruz "I know. I'm sorry. I'm—' (Her silence says more than her words.) 'I don't have the luxury of choosing purity, Amaya."
    "Narration"
    "Her apology is thin and necessary. You want to tell her that you understand the calculus of elected life, but you also want to tell her that the marsh is not an accounting problem. You keep"
    "the words in your mouth because they would cut her, and because cutting her won't grow anything."
    # [Scene: Boathouse | Dusk]
    hide elena_cruz
    hide amaya_saito

    scene bg ch8_6b08b4_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant PA system announcing a city meeting, slow patter of rain]
    # play music "music_placeholder"  # [Music: Low, mournful strings]
    "Narration"
    "Night gathers with the softness of a bruise. You stand with Lucas and Mika under the dim lamp, the future splitting into options that will all change you. The legal notice, the injunction, Maren's press, Elena's compromise, Lucas's offer — they all close like fingers around the marsh."
    show mika_tan at left:
        zoom 0.7

    mika_tan "Whatever you pick, don't pick it because you're exhausted and want the storm to pass."
    show amaya_saito at right:
        zoom 0.7

    amaya_saito "I won't. But I also won't gamble the lab on a single stubborn act of defiance."
    show lucas_herrera at center:
        zoom 0.7

    lucas_herrera "Then let's make sure whatever decision you make has teeth. If you escalate legally, I'll help marshal technical witnesses. If you go public, I'll prepare engineering visuals to counter the PR spin. If you accept a mediated compromise, I'll stand up for the community clauses."
    "Narration"
    "He offers allegiance in all directions, but you know he brings the language of infrastructure to each. His loyalty is a resource, but it is not a replacement for your conviction. The town lies in the balance between adjudicated legalities and the more mercurial court of public sentiment."
    "You move toward the door, hand on the cold latch. Outside, the construction lights etch the fog with sterile geometry. Inside, the plants whisper against their trays."
    "Narration (closing page-turn)"
    "You have to decide what kind of fight you will lead: a legal escalation that risks everything, a compromise that preserves immediate shelter and relationships, or a slow campaign of stories that might remake public will."
    "None of the options will feel like a whole victory; all of them will leave their marks."

    jump chapter9
    return
