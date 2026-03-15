label chapter29:

    # [Scene: Council Chambers | Morning]

    scene bg ch13_f99e88_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, hopeful strings; a steady, mid-tempo rhythm]
    # play sound "sfx_placeholder"  # [Sound: Rain tapping a steady cadence on the windows; paper rustling; a distant gull call muffled by weather]
    "You arrive with a folder tucked under your arm and the salt still on your jacket. The air inside the chamber smells faintly of coffee, damp coats, and the citrus-cold antiseptic that always follows municipal meetings."
    "Your palms are steady. For months you learned to put steadiness where panic used to live—method instead of fury—and now steadiness is what this room needs."
    "Tamsin sits at the head of the table, tablet open, face composed in the professional calm that has braided itself with exhaustion. Across from her, Corinne Voss’s reflection catches in the glass like a blade: immaculate"
    "coat, a holo-pen idle across her palm. Luka is beside you, hair damp from the trip, eyes bright and watchful. Mateo leans against a far wall, hands knuckled into work-worn pockets. Abuela Rosa is there too,"
    "shawl wrapped tight, her presence a quiet gravity that makes the room smaller and safer."
    "You set the folder down and watch the ripple—searches of eyes, the way the town's hope rearranges itself around the possibility of something real and binding."
    show amaya_reyes at left:
        zoom 0.7

    amaya_reyes "This is the agreement as we sat last night. The moratorium terms, the scaled design, the community-funded restoration funds, and the phased relocation plan. The commission has language that holds Voss to measurable, enforceable benchmarks."
    show tamsin_cho at right:
        zoom 0.7

    tamsin_cho "There are triggers—sea-level thresholds, ecological indicators, verified sensor data. If Voss fails to meet a checkpoint, the moratorium re-engages and the town can halt construction. The funding agreement is escrowed with independent trustees."
    # [Dialogue continues; multiple beats]
    show corinne_voss at center:
        zoom 0.7

    corinne_voss "We scale back the bulkhead footprint in favor of living shorelines where feasible. We will finance the restoration pilots and contribute to the relocation fund for the blocks you identified. Our engineering team will submit modified plans within thirty days."
    "You listen for the catch. You have read a thousand catches in a thousand contracts; your life has taught you to smell the small print like tide-scent. But what you hear is real: quantified triggers, escrowed"
    "funds, an enforceable moratorium clause that cannot be erased by a later board. Tamsin's eyes flick to you, and there—under the municipal planner's professional veneer—there is a human relief so thin it could tear."

    tamsin_cho "We have legal counsel on standby to finalize the language. The council voted this morning to recommend approval pending signatures."

    corinne_voss "We expect to retain some operational areas to protect the port's viability, but not at the expense of the marsh schemes you proposed. We will also participate in a joint oversight board, with community representation."
    "You feel your breath lift a notch—an unbidden warmth, like a sun-breaking-through after long cloud. It is not victory in the simplistic way stories show; it is a muscle tightening with use. Pride—sharp and clean—sits beside"
    "a residual hollowness that pulses with the names of houses that will have to move, the faces of those who will lose a living room view and a family plot. This trade stings. It always will."
    hide amaya_reyes
    show luka_maren at left:
        zoom 0.7

    luka_maren "You did it. You held them to the data."
    "You feel the press of his hand at the small of your back—a quiet, anchoring thing—and you let yourself fold into it for a breath."

    menu:
        "Squeeze Luka's hand in relief":
            "Your fingers find his, firm and small-scale like the instruments he loves. He looks at you and the corners of his mouth lift, unformulaic and real."
        "Turn to Abuela Rosa and wait for her word":
            "Abuela's gaze meets yours. She nods, slow and certain—the kind of approval that carries generations. You feel steadier as if standing on the spine of your family's history."
        "Ask Corinne a pointed question about the oversight board":
            "Corinne meets your eyes, an exact fit of corporate polish and an almost-human edge. She answers directly, and for a moment the room sheds politics and becomes two people making an agreement."

    # --- merge ---
    "Scene continues unchanged."
    # [Dialogue — Negotiation fleshed out; multi-turn, subtle friction]

    corinne_voss "The oversight board—community representation is acceptable, but we will require a technical majority. Our obligation is to protect infrastructure as a whole."
    hide tamsin_cho
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "A technical majority without community veto is a non-starter. The benchmarks you agreed to earlier must include enforceable community triggers. No back-channel decisions."

    corinne_voss "Community veto could paralyze urgent repairs."
    hide corinne_voss
    show tamsin_cho at center:
        zoom 0.7

    tamsin_cho "What the community is asking for is accountability, Corinne. The point isn't paralysis—it's preventing unilateral decisions that uproot homes without verified need."

    luka_maren "We can design a sensor suite with redundancy. Real-time data, validated publicly. Decision thresholds become transparent. It's technical, yes—but it's also participatory."
    hide luka_maren
    show jules_park at left:
        zoom 0.7

    jules_park "And we can livestream data feeds to the hall. People see the numbers. They see the trend lines. It keeps trust from evaporating."
    hide amaya_reyes
    show corinne_voss at right:
        zoom 0.7

    corinne_voss "Provide the validation protocols. If they're rigorous, I will agree to transparent thresholds. We sign that into the moratorium."
    "Every concession they make feels like a pebble dropped into a still pond—ripples outward, refracting through people's lives. You think of Mateo's boat, the patched planks and the children who learned to read tides on its"
    "deck. You think of Abuela Rosa's stories of salt and bread—of houses that stood for generations before the sea moved them. You had argued you could preserve both science and story; this is the moment those"
    "two things begin to align, awkwardly and imperfectly, like two hands learning to clasp."
    hide tamsin_cho
    show mateo_reyes at center:
        zoom 0.7

    mateo_reyes "Fine. If we're moving, at least we keep the names of the streets. Don't turn our Pescador Lane into Commerce Boulevard."
    hide jules_park
    show amaya_reyes at left:
        zoom 0.7

    amaya_reyes "We keep the names. We keep the archives. We build memorial benches if we have to. Culture doesn't go into escrow."
    # play sound "sfx_placeholder"  # [Sound: A chair scrapes; a soft laughter that is mostly relief; the rain outside less insistent, like a storm starting to tire]
    hide corinne_voss
    hide mateo_reyes
    hide amaya_reyes

    scene bg ch13_f99e88_2 at full_bg

    menu:
        "Sign the moratorium document first":
            "You pick up the pen—your hand is steady. The ink feels final, like a tideline left on a plank."
        "Let Corinne sign first":
            "You watch Corinne's pen move with precise strokes. Seeing her commit publicly loosens something tight in your chest."

    # --- merge ---
    "Continue to the binding commitment."
    # [Climax — The binding commitment]
    show tamsin_cho at left:
        zoom 0.7

    tamsin_cho "All right. We have language: benchmarks, escrow, oversight, compensation, relocation timelines, and restoration funding. Counsel has verified enforceability."
    "Corinne exhales once, a long, controlled exhale, and signs. The holo-pen trails—a small, almost performative shine on the signature. Then Luka slides a print across, hands steady, and you sign."
    # play sound "sfx_placeholder"  # [Sound: The click of the pen caps; a muted applause from council members; a camera shutter]
    "When the last stroke completes the phrase, a tangible change moves through the room. It isn't a fanfare; it's the way a curtain lifts slowly and light finds what it had been missing. You are not"
    "triumphant with the suddenness of drama. You are triumphant the way a tide patient and persistent will reclaim a shoreline: quietly, inevitably, with work behind it."
    "People rise. Mateo crosses the room and takes you in a quick, gruff hug that smells of sea tar and soap. Abuela Rosa reaches for your hand and presses it to her shawl as if sealing"
    "a covenant with the old world. Luka's eyes are wet but not broken; they hold promises—practical, intimate—that are not speeches but actions."
    "Corinne stands and, for a bare second, humanity slips past the business mask: a small nod to the people at the table. It is not remorse, not exactly. It is acknowledgment of consequence."
    show corinne_voss at right:
        zoom 0.7

    corinne_voss "We will fund the restoration pilots first, in partnership with TideLab. We will submit the revised engineering plans in thirty days. Our contractors will begin training local hires for the parts of the project that proceed. I expect transparency. So do you."
    show amaya_reyes at center:
        zoom 0.7

    amaya_reyes "Then we will hold you to it."
    # [Aftermath — Tone settles into bittersweet warmth]
    # [Scene: TideLab | Afternoon]
    hide tamsin_cho
    hide corinne_voss
    hide amaya_reyes

    scene bg ch13_f99e88_3 at full_bg
    # play music "music_placeholder"  # [Music: Gentle acoustic guitar with soft brushes—comforting, mid-tempo]
    # play sound "sfx_placeholder"  # [Sound: Distant laughter outside, the town's murmur like a tide; a kettle whistling softly]

    "You return to TideLab with a folded set of copies and a head full of clauses. The lab smells of wet soil and tea. Jules is already printing banners—small, honest things" "Marisol Cares' and 'Restoration Starts Here."
    "The escrow will cover restoration and relocation, but relocation is relocation. You have sat with families today who will have to leave their porches, and their faces are not dramatics—they are practical grief, the kind that"
    "packs boxes and remembers recipes and measures a life in photographs. It leaves a hollow you will carry."
    "Abuela Rosa pulls out a small tin and offers you a scrap of dried kelp candy—old coastal sweetness. She clasps your hand the way she does after prayers: a grip that says, I have seen worse and we carry it forward."
    show abuela_rosa at left:
        zoom 0.7

    abuela_rosa "There is a cost to keeping what matters. Your grandmother paid it; her mother paid it. We pay it, and we teach the children to pay a different debt."
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "It does not feel like enough."

    abuela_rosa "Enough is not always the point, niña. What we build—what we refuse—makes a story. You made the town's story louder."
    show luka_maren at center:
        zoom 0.7

    luka_maren "I'll split my time. I'll keep the community networks, but I'll go to the technical meetings too. Someone needs to translate their language into ours."

    amaya_reyes "You mean be an engineer-ambassador?"

    luka_maren "And hold a wrench when needed. And a clipboard. And your temper."

    amaya_reyes "Good. Hold me to the wrench and the clipboard."

    luka_maren "I don't want to lose this town. I don't want to lose you to another project because of a better offer. Is that selfish?"

    amaya_reyes "It's honest. I worried you'd take the money and leave."

    luka_maren "I thought about it. But this—this is where my work matters. We can build tech that doesn't erase people. I want to find a way to scale it without selling the soul."

    amaya_reyes "Then stay and hold us accountable—hold Corinne, hold the contractors, hold me."

    luka_maren "I will."
    "You imagine the next months as a map of small tasks—benchmarks, sensor installs, town hall debriefs, moving trucks with polite workers ferrying boxes out of the marginal blocks. It is not an arc of sudden wonder;"
    "it is a spreadsheet and a playlist of consolation songs and soup on cold evenings. But there is a horizon you can name now: fewer homes lost, marshes replanted, kids learning to read a tide gauge."
    "It will not heal everything, but it gives future mornings a chance."
    hide abuela_rosa
    show jules_park at left:
        zoom 0.7

    jules_park "We've already got volunteers. People want to plant. They want to keep their streets. The banners will be soft, not angry—because we have something to protect now, not only something to fight."
    hide amaya_reyes
    show mateo_reyes at right:
        zoom 0.7

    mateo_reyes "We keep Pescador Lane. And I'll teach the new hires how to splice a net so they don't ruin the gear."
    hide luka_maren
    hide jules_park
    hide mateo_reyes

    scene bg ch13_f99e88_4 at full_bg
    # play music "music_placeholder"  # [Music: Strings rise gently—hopeful, warm; not triumphant fanfare, but a sustained, comforting swell]
    "You stand at the marsh edge as the day cools. The sky is a muted wash of peach behind the receding rain. You run a hand along the braided bracelet at your wrist—the wildflower seeds tucked"
    "inside, a small promise that you will plant them where the town decides. Luka stands beside you, hands in his pockets, watching lines of volunteers sink planting stakes into the mud."

    "You feel both proud and hollow—the two sensations braided like rope. Pride because you helped bargain for the town and its memory; hollow because negotiation always asks for rooms emptied and porches left. It is a hollow like an emptied shell: you can hear the sea in it, but the shell still keeps sound. Abuela Rosa presses your shoulder and, without drama, says what she always has" "We do not erase our past to build our future. We stitch it in."
    "You breathe in the brackish air, let salt-mix fill your lungs. The season ahead will be work: restoration plots, relocation schedules, oversight meetings, long nights reading contracts and comforting neighbors. There will be mistakes and revised"
    "plans and small heartbreaks, and there will be afternoons like this—steady hands planting roots that will hold against future tides."
    "Luka slips an arm around you. It is not a rescue; it is a quiet promise to be present in the messy middle. You lean into it."
    show amaya_reyes at left:
        zoom 0.7

    amaya_reyes "We'll keep making it better. Not perfect, not without loss—but better."
    show luka_maren at right:
        zoom 0.7

    luka_maren "Together."
    hide amaya_reyes
    hide luka_maren

    scene bg ch13_f99e88_5 at full_bg
    # play music "music_placeholder"  # [Music: Guitar and strings thread into a warm, steady chord]
    # play sound "sfx_placeholder"  # [Sound: The distant, steady hush of the sea; a child's laugh carried on the wind]

    scene bg ch13_f99e88_6 at full_bg
    # play music "music_placeholder"  # [Music: Resolve; last chord held and allowed to fade]

    scene bg ch13_f99e88_7 at full_bg
    "THE END"
    # [GAME END]
    return
