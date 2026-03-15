label chapter9:

    # [Scene: Council Chamber | Morning]

    scene bg ch9_3be532_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm, ascending strings; a single clarinet threads a humanizing line]
    # play sound "sfx_placeholder"  # [Sound: Quiet murmur of crowded voices, the soft scratch of pens, an occasional cough]
    "Narration:"
    "You walk into the chamber carrying the weight of months—drafts, late-night edits with Samir, Etta's stories transcribed into clauses—but it doesn't feel like a burden so much as a bundle of care. The air tastes faintly"
    "of ozone and paper; a breeze moves the papers on the council clerk's desk in a way that feels almost like a nod."
    "You notice Samir first: shoulders unclenched, eyes bright with the relief of someone who has watched a plan survive its own footnotes. He catches your eye and gives you a small, private smile that says: we"
    "did the hard shaping and the universe will decide the rest. His relief threads into you, warming the cold place behind your ribs."
    show mira_solace at left:
        zoom 0.7

    mira_solace "Samir."
    show samir_hale at right:
        zoom 0.7

    samir_hale "You look like you haven't slept. In the best way. There's language in Section Four now that will force shared budgets instead of goodwill. You did that."
    "Narration:"
    "You look at the hologram: Article headers hop in teal and sandstone. Community co-management. Guaranteed funding lines. Binding participation for municipal oversight. Words that once felt like hopeful scaffolding now project as infrastructure in their own right."
    show liora_kade at center:
        zoom 0.7

    liora_kade "This charter answers both efficiency and equity. It ties funding to outcomes and creates enforceable seats for community stewards. My team asked for the language you and Samir negotiated. It is…workable."
    "Narration:"
    "Her 'workable' is a cautious bridge. You hear the unsaid: compromises she made, favors she had to call to shape votes. The room leans into that calculation. You sense complexity in her presence—real loss margin traded"
    "for institutional teeth—and you decide, for now, to accept the result: teeth where there were none."
    hide mira_solace
    show etta_maren at left:
        zoom 0.7

    etta_maren "We taught you to read tides and to listen to elders and strangers the same. This charter keeps hands in the water. You have my blessing."
    "Narration:"
    "Applause moves through the chamber like a slow wave. It isn't thunderous—this isn't a soapbox victory—but it is steady, enough to lift shoulders. You feel the lift in your chest and, for a moment, the work"
    "that once existed only in margins becomes visible. Legal protection for reed gardens, municipal funds tied to local hiring, a clause that prevents unilateral demolition without community assent—small measures, but hard-won."

    menu:
        "Step up to the podium and speak":
            "You walk forward, the podium cool under your palms. Your words come trimmed and sure; you thank the people who shaped the charter and name the neighborhood's labor by its true weight."
        "Let Samir read the statement":
            "You fold your hands and watch Samir take the podium. He reads the charter's intent with that engineer's plainness, and you feel the relief of shared voice."

    # --- merge ---
    "You choose—either way, the chamber's mood tightens into focus."
    "Narration:"
    "You choose—either way, the chamber's mood tightens into focus. Council members ask procedural questions; a few chalice-drunk political notes attempt to float fear about cost. Liora answers each in a manner that is exacting rather than"
    "grandstanding. When she speaks in favor, it's not surrender but a calculation: if this is the vessel that saves neighborhoods and keeps the economy from lurching into land grabs, then the compromise is sanctified by outcome."
    "Noah is here—at the back, practically humming with too-much-joy energy. He catches your eye and gives you that crooked look he gets when he wants to both tease and thank you. His boat shop's name is"
    "stitched into his sleeve in faded thread; he looks like someone who has already put this charter into the language of his daily life."
    hide samir_hale
    show noah_solace at right:
        zoom 0.7

    noah_solace "You did it, Mira. You wrote clauses into the stuff that keeps our hands on the tools."
    hide liora_kade
    show mira_solace at center:
        zoom 0.7

    mira_solace "You did the rest. You showed up. You and the whole pier taught the city how to listen."
    "Narration:"
    "The vote happens like a tide, measured and then sudden: yes, yes, more than the margin you dared hope. The clerk's hammer comes down in a sound like a bell sunk into water. When the motion"
    "passes, a small cheer erupts from the gallery; some tears, a laugh, a shouted name. The charter is enacted—not a panacea, but a binding instrument that changes the rules of force."
    hide etta_maren
    hide noah_solace
    hide mira_solace

    scene bg ch9_3be532_2 at full_bg
    # play music "music_placeholder"  # [Music: Swell of strings lifts into an optimistic chord]
    "Narration:"
    "You are dizzy, not in disbelief but with the spinning of a possible future. Samir squeezes your shoulder. Etta folds you into an embrace that smells of knitted wool and salt. Liora nods—her face slightly softer"
    "than before. Noah moves through the crowd with the kind of grin reserved for people who have been given back something they've already mourned."
    show liora_kade at left:
        zoom 0.7

    liora_kade "There will be legal challenges. There will be tests of this system. But you made it divisible and durable. That is rare."
    show mira_solace at right:
        zoom 0.7

    mira_solace "We will hold it. That's the point."
    show samir_hale at center:
        zoom 0.7

    samir_hale "And we'll audit the metrics, run transparent accounting. No back-doors. The pilot funds go directly to neighborhood stewards—Noah, Etta—you'll have oversight seats."
    hide liora_kade
    show noah_solace at left:
        zoom 0.7

    noah_solace "Oversight seat? Fancy. I'll bring coffee."
    hide mira_solace
    show etta_maren at right:
        zoom 0.7

    etta_maren "Bring strong coffee. And bring those stubborn hands."
    "Narration:"
    "There are speeches, handshakes, the shaking of a hand that feels like a map being rewired. Outside, the harbor's water flashes between the columns of the chamber—an outside that now feels inch-closer to the inside."
    # [Scene: Old Pier Neighborhood | Late Afternoon]
    hide samir_hale
    hide noah_solace
    hide etta_maren

    scene bg ch9_3be532_3 at full_bg
    # play music "music_placeholder"  # [Music: Acoustic guitar with gentle percussion; the melody is folk-rooted and warm]
    # play sound "sfx_placeholder"  # [Sound: Laughter, the clatter of tools, the low murmur of people trading plans]
    "Narration:"
    "By the time you return to the pier, the neighborhood has turned itself into a low, convivial festival. People move with the kind of purposeful lightness that follows relief—repairs underway, plants being planted in newly funded planters, a small sound system playing an old working song."
    "You consider the practical things you promised: pilot funding to stabilize Noah's shop, a schedule for co-managed reedbed restoration, a municipal hotline dedicated to complaints about unauthorized demolition. These are lines in a document, yes, but"
    "now they're also the rhythm of hands bundling native grasses, measuring stakes driven into soft earth."

    menu:
        "Kneel down to help a child plant a reed":
            "You crouch, fingers in cold soil, the child's small hands mirroring your movements. Their laugh is light and immediate, and the plant leans like hope."
        "Walk to Noah's shop to check the new schematic":
            "You trace the drawn lines on the shop's new reinforcement plan with your finger. Noah explains beam choices in a breathless, proud voice, and you feel the anchor of his shop settle into place."

    # --- merge ---
    "You move through conversations that loop and return."
    "Narration:"
    "You move through conversations that loop and return. Families talk about next seasons, elders outline volunteer rotations, and teenagers sketch drainage channels in the margins of flyers. Etta convenes a circle and names forthcoming neighborhood committees:"
    "stewardship schedules, transparency boards, apprenticeship rosters. She speaks less like someone handing down decisions and more like someone making a place teach itself to last."
    show etta_maren at left:
        zoom 0.7

    etta_maren "This is not a grant to be spent and forgotten. This is a long season of care. We will rotate responsibility. We will teach each other. We will not allow this to become a trophy for photographs."
    show samir_hale at right:
        zoom 0.7

    samir_hale "We can set up quarterly audits open to the public. The data will be visible—pH, sedimentation rates, hiring numbers. If any clause is misused, there's an escalation procedure."
    show mira_solace at center:
        zoom 0.7

    mira_solace "Make the audits public and simple. If people can read it, they can guard it. Complexity is where things go soft."

    samir_hale "Agreed. Usability is a feature."
    "Narration:"
    "The municipal partnership that once felt like a trade-off now becomes a set of tools in a shared toolbox. You feel your relationship with municipal actors deepen—Samir as an ally who reads code and people, Liora"
    "Kade as an unexpected lever who can move bureaucracies. It's not romance. It's collaboration that respects the stubborn logic of neighborhood life."
    "Noah sidles up, wiping grease on a rag, eyes shining."
    hide etta_maren
    show noah_solace at left:
        zoom 0.7

    noah_solace "Promise me one thing. If this actually holds, you take first pick of plants from the rooftop nursery."

    mira_solace "Deal. But only if you promise to teach me how to weld without burning anything vital."

    noah_solace "You already fixed half the pier last winter. Welding is just angry sewing."
    "Narration:"
    "You laugh. Around you, the harbor hums: boats in the distance, the industry that persists in new patterns, children dipping toes into puddles between boards. You think of your childhood home—what it was, what it's become—and"
    "there's a quiet, steady satisfaction that isn't the highest thrill but the right kind of closure. A neighborhood that once felt likely to fade has been given a legal voice and the resources to steward itself."
    hide samir_hale
    hide mira_solace
    hide noah_solace

    scene bg ch9_3be532_4 at full_bg
    # play music "music_placeholder"  # [Music: Strings and choir swell lightly; warmth without excess]
    "Narration:"
    "Night edges toward skyline; the lanterns turn the pier into a constellation of small fires. People sing in a low, improvisational chorus. You stand at the pier's edge and let the harbor breathe in front of"
    "you. It's not a promise that everything will be easy—laws can be twisted, funding lines can be reallocated, storms can rewrite plans—but the city now contains a rule that the neighborhoods who have kept memory will"
    "have a seat at the table and the means to hold that seat."
    "You fold your damp notebook into your jacket. Your wristband buzzes softly with tide data, a small thing that has been with you through storms and meetings both. You feel steadier than you have in a long while."
    show etta_maren at left:
        zoom 0.7

    etta_maren "We will teach the young ones how to plant and how to read a budget. That's how we survive."
    show mira_solace at right:
        zoom 0.7

    mira_solace "We will teach both."
    "Narration:"
    "You watch Arin Voss's note—if he were here, you'd want to show him how a crowd can be convincing when it is patient. You let the thought sit without needing to resolve it. The charter binds"
    "institutions and people; your partnership with municipal actors deepens into active stewardship. Love and policy don't erase each other; they have to be held in different hands at the same time."
    hide etta_maren
    hide mira_solace

    scene bg ch9_3be532_5 at full_bg
    # play music "music_placeholder"  # [Music: Concluding chord that is warm and unresolved in the smallest, human way—enough to belong]
    "Narration:"
    "You breathe the salt air, and for the moment you are buoyed by something that feels like rising tide: not a flood, but a lifting. The city has changed its rules. The Old Pier will not"
    "be erased easily. People will have jobs to learn, committees to form, audits to watch, reedbeds to plant through wet seasons."
    "You tuck your notebook away and, for a long second, simply stand. The harbor tilts with you—steady, taught, full of small, collective acts that promise to accumulate into holding."

    scene bg ch9_3be532_6 at full_bg
    # play music "music_placeholder"  # [Music: Soft fade of strings into silence]

    scene bg ch9_3be532_7 at full_bg
    "THE END"
    # [GAME END]
    return
