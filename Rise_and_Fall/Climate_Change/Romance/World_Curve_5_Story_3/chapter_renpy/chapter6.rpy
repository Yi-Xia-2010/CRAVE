label chapter6:

    # [Scene: Boathouse | Early Morning]

    scene bg ch6_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: A single, uplifting chord — quiet, steady strings]
    # play sound "sfx_placeholder"  # [Sound: A gull, distant; the low tick of a sensor console; water lapping against pilings]
    "Narration"
    "You wake with the memos under your tongue like an address you have to speak aloud. The brass clip presses a cool circle into your palm; your sea-grass braid is loose against your neck. Outside, the"
    "marsh fog is thinning—light drawing the patterns of channels, the long mirror of silt and blade and bird. Inside, the boathouse hums with other people's breathing: volunteers stirring, Dr. Kaito moving like a book opening, Elena's"
    "low, steady voice on the line with the council."
    "Your chest feels both heavy and buoyant. This is the hinge you promised yourself you would make: not just to complain about what could be taken, but to pull evidence into the light and demand accountability."
    "The memos are not a hammer to punish—though they will hold someone to consequence—they are a tool to restore the town's voice over its shoreline."
    "You stand, fingertips trailing over the notebook cover. Memory folds into present; your father's notes on tidal lines, the volunteer lists Mika brought in, the smell of salt and old wood that means home. You let those touch you and shape the resolve behind the next words."

    scene bg ch6_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A soft exhale; the room settles]
    show amaya_saito at left:
        zoom 0.7

    amaya_saito "We can't make this only legal. If we show the town the data and the contradictions, we make this public in a way they can't ignore. We make it incontrovertible."
    show dr_kaito_mori at right:
        zoom 0.7

    dr_kaito_mori "Scientific corroboration will change how officials have to act. If we publish a technical rebuttal alongside a corroborating testimony from inside Atlantech, they'll have to respond."
    show elena_cruz at center:
        zoom 0.7

    elena_cruz "I've already called for a temporary review if the evidence holds. We need both the technical report and the human voice that says—this was shaped, not assessed."
    "Narration"
    "The plan forms like a braided rope: memos, Dr. Kaito's rebuttal, a reluctant Atlantech engineer who promised they'd talk, and the council's authority. It isn't clean. It isn't private. It is, you believe, necessary."

    menu:
        "Call Lucas right now and tell him to come to the boathouse":
            "You lift your phone, thumb hovering. You can feel the weight of what you'll ask him to risk before the call connects; his presence could steady this, but it could also harden things between you two."
        "Wait and let the corroboration arrive before involving him":
            "You set the phone face-down on the workbench. Letting evidence speak first might keep this from being read as a personal blow—if Lucas and you must reconcile, let it be on truth."

    # --- merge ---
    "You choose strategy rather than impulse; you arrange the timing so the corroboration and the rebuttal arrive together. You do not hide from Lucas—you do not want this to become about blame—but you also want the community to stand on facts they can see for themselves."
    hide amaya_saito
    hide dr_kaito_mori
    hide elena_cruz

    scene bg ch6_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The faint rustle of pages as Dr. Kaito opens the memos again]
    # [Scene: Atlantech Towers | Midday]

    scene bg ch6_601bcb_4 at full_bg
    # play music "music_placeholder"  # [Music: Tension lightens into purposeful harmonies]
    # play sound "sfx_placeholder"  # [Sound: The distant mechanical hum of the Towers; a soft beep as a message arrives]
    "Narration"
    "The Atlantech engineer is younger than you expected, hair damp from the lobby rain, eyes that dart between you and the file like someone who has rehearsed a confession and is afraid of its consequences. He"
    "asks you, quietly, if it's safe. You tell him—truthfully—that truth is what will keep people safe, and that Elena has authority and Dr. Kaito's name."

    "Atlantech Engineer" "They—it was pushed. Data weighted, alternatives minimized. They said commercial timelines couldn't be delayed. I couldn't reconcile the assumptions with the models. I hid copies. I didn't know what else to do."
    show amaya_saito at left:
        zoom 0.7

    amaya_saito "You did the hard thing. You kept evidence. Tell me what was minimized."

    "Atlantech Engineer" "The marsh buffer calculations. The modeled sediment retention—they trimmed the scenarios that showed living shorelines working at scale. And there were clauses—'cost contingencies'—meant to let corporate discretion substitute cheaper engineered fixes later."
    "Narration"
    "He gives specifics, but even when numbers are spoken your mind keeps returning to the human angle: someone inside, tired of being complicit, choosing to be a witness. You feel that fragile, fierce gratitude climb like tidewater across your ribs."

    "Atlantech Engineer" "I don't want this to destroy people there. I want the town to be able to hold them to account."

    amaya_saito "We want the town to hold them accountable and be part of the solution. Thank you. You did the right thing."
    # play sound "sfx_placeholder"  # [Sound: A muted chime; Elena's call comes through on the engineer's tablet]
    hide amaya_saito

    scene bg ch6_601bcb_5 at full_bg
    show elena_cruz at left:
        zoom 0.7

    elena_cruz "We have enough to call for a temporary halt pending investigation. I'll do it now. Publicly. No leaks—this goes through the council."
    "Narration"
    "Her words are a cliff-cutting; she speaks them softly but with the engine-room authority of someone who has carried this town through storms. The Atlantech engineer nods, relief and fear rippling across his face. You realize"
    "the leak no longer sits alone in your hands; it has legs. It will walk across the town and into the newspapers."
    # play sound "sfx_placeholder"  # [Sound: Notification cascade — press releases, a newsroom ringtone, the clatter of keyboards]
    hide elena_cruz

    scene bg ch6_601bcb_6 at full_bg
    # [Scene: Takase Cove / Harbor | Late Afternoon]

    scene bg ch6_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: Rising, optimistic strings mingled with community murmurs]
    # play sound "sfx_placeholder"  # [Sound: Applause, the slap of a newspaper page, a child laughing]
    "Narration"
    "The council chamber smells of coffee and wet coats. The same faces that helped plant reeds are here—Mika with salt on her boots, volunteers with mud on their palms, Dr. Kaito sitting straighter than you remember."
    "Elena speaks first, then plays the engineer's recorded corroboration, then lets the evidence roll: memos, redacted but telling, and Dr. Kaito's technical rebuttal, calm and unassailable."
    show elena_cruz at left:
        zoom 0.7

    elena_cruz "Pending a full inquiry, I am ordering a temporary halt to all seawall construction within the town's jurisdiction. We will form a joint oversight committee, including community representatives and external auditors. We will not proceed until the work is transparent and enforceable."
    # play sound "sfx_placeholder"  # [Sound: A collective intake; then a swell of approval—some cry, some clap, some weep quietly.]
    "Narration"
    "Maren Voss's absence at the podium is a presence in itself. Word reaches you later—Atlantech has reassigned her pending investigation. The corporate ecosystem rearranges, and in the gaps the town finds room to breathe."

    "Volunteer" "You did it. They listened."
    show amaya_saito at right:
        zoom 0.7

    amaya_saito "We showed them the facts and asked them to keep their promise to us."
    show dr_kaito_mori at center:
        zoom 0.7

    dr_kaito_mori "This is not victory yet, child. It's a correction. But corrections can be foundations."
    "Narration"
    "The day yields to a night of careful celebration: candle-lit meetings and mapped task forces, a press conference in which Atlantech agrees to open previously sealed assessments and to fund independent monitoring while the inquiry proceeds."
    "The arc of events bends toward something you dared to imagine: institutional correction that listens."
    # [Scene: Harbor | Dawn]
    hide elena_cruz
    hide amaya_saito
    hide dr_kaito_mori

    scene bg ch6_601bcb_8 at full_bg
    # play music "music_placeholder"  # [Music: Quiet, hopeful piano; wind-brushed strings]
    # play sound "sfx_placeholder"  # [Sound: Tide whispering, a distant gull, the soft clink of Lucas's toolkit against a railing]
    "Narration"
    "You come down to the harbor before most of the town wakes. The air tastes like the inside of a shell—cool and mineral. Lucas is already there, leaning on the railing, the brass lighthouse key warm"
    "in his palm. The city's overnight headlines rest like thin paper between you: his company's scandal, his own work implicated, a thousand small and sharp things to say."
    "But in his face there's something else too: rawness, apology, a fatigue you recognize. He looks up as you approach, the silver streak at his temple catching light."
    show lucas_herrera at left:
        zoom 0.7

    lucas_herrera "I should have—' (He stops, shakes his head.) 'No. I needed to have pushed harder. I let timelines and approvals become shields. I thought I was protecting people by getting something in place quickly. I didn't see how that silenced other evidence."
    show amaya_saito at right:
        zoom 0.7

    amaya_saito "You were part of the process. You could have raised questions. You didn't."

    lucas_herrera "I know. And I regret it. Not because I'm embarrassed—because people I care about might have been harmed. I should have been braver inside the system, not just in moments after."
    "Narration"
    "There is a pause wide enough for gulls to fill. The harbor light paints his face in soft angles. You want to reply with every accumulated hurt—times his pragmatism sounded like dismissal, the night he signed"
    "off on a draft he knew felt thin—but the morning air makes you hold those like nets until you can decide what to haul ashore."

    lucas_herrera "This belonged to my grandfather. He said the lighthouse kept more than ships—it kept people honest. I kept it because I thought it reminded me of duty. Today, I realize duty includes listening. If you'll have me, I want to be part of fixing this properly."
    "Narration"
    "The key in his hand is a small, honest object: brass, dented, holding some personal history. The gesture is humble and real. It is not a neat absolution; it's an offering of work."

    menu:
        "Reach out and take his hand":
            "Your fingers find his, the salt of your skin against the brass of his palm. The contact is simple and human; it feels like beginning to rewrite a shared map."
        "Place a hand on his shoulder and keep some distance":
            "You place a steady weight on his shoulder, letting the pressure do the speaking. It is not intimacy yet, but it steadies both of you—commitment without rush."

    # --- merge ---
    "He laughs once, small and disbelieving, and then the sound is steady. The harbor breathes around you; the town behind you waking to the knowledge that it can demand more than promises. You speak about the"
    "steps you want—community co-management, legal mechanisms for monitoring, investment in scaled living shorelines that work with sediment and vegetation rather than flattening them. He listens with the engineer's concentration, then offers adjustments from his end: funding"
    "channels, technical oversight, a commitment to open-source modeling."
    "Narration"
    "You outline the framework—co-management councils, legally enforceable monitoring, funding for living shorelines and community labor, a public data portal where models and assumptions are available to anyone with eyes. His replies are practical, and for the"
    "first time in months they line up with your own sentences. You are both tired and steady in the same way."

    lucas_herrera "I don't expect you to forgive me all at once. I just want to do the work, and to show you, and the town, that I learned."

    amaya_saito "I want that too. Not a clean reconciliation—a slow rebuilding. Will you help me build it?"

    lucas_herrera "Yes."
    hide lucas_herrera
    hide amaya_saito

    scene bg ch6_601bcb_9 at full_bg
    # play music "music_placeholder"  # [Music: Warm strings swell; the chord resolves upward into a calm, hopeful melody]
    # play sound "sfx_placeholder"  # [Sound: The tide, a soft cheer in the distance as volunteers arrive; the creak of a boat being readied]
    "Narration"
    "The town begins to pull together new scaffolding—administrative, technical, communal. Elena convenes the oversight committee that same week; Dr. Kaito leads training sessions for citizen scientists; Atlantech's funding is redirected into a community trust that pays"
    "for living-shoreline pilots and local maintenance. The marsh, bruised but not lost, begins to breathe with room to recover."
    "Amaya Saito [You stand on the harbor rail with Lucas, keyed into the same map now: where to plant cordgrass, where to let tidal creeks re-form, how to write a contract that can't be folded away"
    "in a boardroom. Your amber-green eyes glisten with the strain of the months and the suspicion that some part of you had been waiting for this exact light.]:"
    show lucas_herrera at left:
        zoom 0.7

    lucas_herrera "I don't know if love can come back the same way. But I know it can be rebuilt in work that honors where we started from."
    show amaya_saito at right:
        zoom 0.7

    amaya_saito "We'll rebuild it together. The town, the marsh, us—we'll be honest about the cost and the care."
    "Narration"
    "It is not a perfect ending—no single day can stitch old injuries completely—but it is true. Institutional correction arrives, not as a theatrical vindication but as a reweaving of authority and accountability. The marsh gains a"
    "legally enforceable guardian; the community gains technical tools and the voice to use them. Love regrows slowly, patient, tied into the practical rhythms of shared work."
    hide lucas_herrera
    hide amaya_saito

    scene bg ch6_601bcb_10 at full_bg
    # play music "music_placeholder"  # [Music: A final rising flourish — hope, a tide that pulls forward]
    # play sound "sfx_placeholder"  # [Sound: Hand tools meeting soft earth; voices mapping a future]
    "Narration"
    "You think of your father's journal—how he wrote that stewardship was a daily, unglamorous practice. You tuck his memory into the plan, into the apprenticeships, into the legal clauses that make the town a steward rather"
    "than a subject to distant decisions. The memos that once felt like a blade have become a fulcrum."
    "You breathe in the salt and the light and let the future, for a fragile bright moment, feel like something you and other people have chosen together."

    scene bg ch6_601bcb_11 at full_bg
    "THE END"
    # [GAME END]
    return
