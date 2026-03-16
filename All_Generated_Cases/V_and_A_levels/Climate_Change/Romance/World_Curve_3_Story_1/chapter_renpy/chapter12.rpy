label chapter12:

    # [Scene: Rooftop Greenhouse | Dusk]

    scene bg ch11_e67f19_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low thrum of the city, distant horns, a soft wind fluting through tarp lines]
    # play music "music_placeholder"  # [Music: Tense, pulsing underscore, rising in short swells]
    "You sit on the upturned crate, compass pendant warm against your palm, watching the mist break into a thousand tiny suns on the greenhouse glass. The market below hums like a living thing; the Planning Hall's silhouette holds the horizon like a promise that has stopped being kind."
    "Ibrahim 'Ibe' Rafiq leans against the solar array, welding goggles pushed up on his head, posture relaxed in a way that tries to look casual and fails. His presence feels like a steadying hand, which is"
    "exactly what you need and exactly what scares you a little—because steadiness asks you to trust, and trust is something you have been rationing."

    "Ibrahim 'Ibe' Rafiq" "Samira said she'd be here ten minutes ago. If she brought what you think she did, we don't have time to be neat about it."
    "You swallow. The greenhouse smells of damp earth and copper—soil, rain, and the metallic tang that always rides in with municipal urgency. Every sensory edge registers sharp: the click of Ibrahim 'Ibe' Rafiq's boots on the"
    "metal grate, the rustle of Rosa's jacket as she moves to stand at the edge, the tiny cicadas that keep time with your heartbeat."
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "Don't decide in a panic. Decide in a way you can live with."
    "You want to tell her that you've been living with decisions like this for years; that living with them is the point. Instead you rub at the brass compass until it warms the pad of your thumb."
    hide rosa_alvarez

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Footsteps climbing the metal stair; a paper bag rustles against fabric]
    "Samira arrives without fanfare—clipboard tucked under one arm, eyes quick, professional, but her shoulders carry the weight of someone who has been holding their breath for too long."
    show samira_chen at left:
        zoom 0.7

    samira_chen "I didn't bring the originals. I couldn't. But I have extracts—amendment language, redline notes. It's worse than we thought."
    "You stand so fast your crate clatters. The room tilts, not from motion but from the sudden pressure of information."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Worse how?"
    "Samira hesitates. Her mouth makes an apology you don't know the shape of."

    samira_chen "There's an amendment hidden in the addendum. It reclassifies several residential zones as 'redevelopment priority'—that phrasing legally clears relocation without the protections the code used to require. It also ties approvals to private investment milestones. It looks like Eloise Varela's shield, but with escape hatches for corporate sponsors."

    "Ibrahim 'Ibe' Rafiq" "A shield that mouths safety and pays for itself by taking homes."
    "You feel the words like a physical shove. Your chest tightens; the greenhouse air seems to thin."

    menu:
        "Ask Samira to read the extracts aloud now":
            "You ask her to read—every clause landing like a pebble in water. The group leans in, the room shrinks, and your stomach drops as technical language becomes human cost."
        "Tell Samira to give you a copy first, then read privately":
            "You choose caution. Samira slides a thumb drive across the crate. Your fingers close over cold metal; the ache of responsibility settles heavier."

    # --- merge ---
    "Continue"
    "Samira's hand shakes just enough for you to see it—then steadies. She sets a slim encrypted drive on the wood between you like a live wire."

    samira_chen "I can publish this. I can push it to the local feeds. But I—' She stops, the sentence collapsing under its own implications. 'I reached out because I need someone who can shoulder the fallout with me. I can't do this alone."
    "Rosa watches you with the tired patience of someone who has seen storms break and knows how the work follows the noise. Kai lingers in the doorway, eyes darting between faces, harbor-market pragmatism written in the set of his jaw."
    show kai_moreno at center:
        zoom 0.7

    kai_moreno "If this goes public, it'll burn fast. People will come. Police will come. Investors will sue. But the truth—' He digs his palms into his paint-splattered pockets. 'People deserve to know."

    "Ibrahim 'Ibe' Rafiq" "But if we keep it closed, we might actually get stronger protections passed. Backroom's ugly, but it's quicker, and it saves people from getting steamrolled while the court's slow-walking everything."
    "Your internal monologue snaps like a line: revealing the leak could force transparency—but could also tip the scales into chaos. Using the documents privately could craft a better policy—but it would ask you to trust the"
    "very system that is rigged to favor expedience over people. Keeping them secret could shield the town from immediate chaos—but might let the worst language slide through."
    "Every option tastes of compromise; your stomach knots."
    # play music "music_placeholder"  # [Music: Percussive rhythm accelerates; a distant siren climbs higher]
    # play sound "sfx_placeholder"  # [Sound: A notification ping from your phone; the Planning Hall's civic map blinking in the distance]

    samira_chen "They're meeting tomorrow. The council's penciled in an override clause. If the public doesn't have grounds to contest the amendment in the next eighteen hours, that language is legally tidy. I'm giving you what I can—everything that proves intent."
    "You pick up the flash drive. It feels heavier than its weight."

    menu:
        "Push to publish immediately—call the reporters":
            "You picture the headlines, the market crowd swelling in the square, banners, the law clanging under public scrutiny. It scares you and thrills you in equal measure."
        "Ask Samira to schedule a discrete meeting with an ally on the council":
            "You imagine Samira slipping into a backroom negotiation, trading exposure for concessions. It feels like bargaining with knives, but it's quieter."

    # --- merge ---
    "Continue"
    "Rosa moves closer and lays a soil-stained hand on your forearm, grounding you in the tangible: the Flats' mud, the seedlings pushed into the tide. Her voice is weathered but clear."
    hide samira_chen
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "Remember what we're protecting. Not just houses—people's lives stitched together. If you burn a bridge that could hold a family, you owe them a road to somewhere better."
    "Ibrahim 'Ibe' Rafiq looks at you, then away, then back again. His face is an open ledger of an exile who learned the hard lesson that 'safety' can demand impossible sacrifices."

    "Ibrahim 'Ibe' Rafiq" "Mara—if this goes viral, they'll call for immediate arrests for trespass, for instigating unrest. They'll move to shut down the consultation with 'public safety' on a very thin pretext. People will get scared and leave. I don't want to see that happen to anyone."
    "Your fingers curl around the drive until the edges dig into your palm. The greenhouse smells like rain and green things and something metallic—your mouth tastes like the brass of the compass, like the memory of a flooded street and a child's lost toy."
    hide mara_lin
    show samira_chen at right:
        zoom 0.7

    samira_chen "If you publish, I will stand by it. I'll give testimony. I'll leak everything I have. But I can't promise the narrative will stay pure. It becomes the city's story overnight, and the city is hungry and messy."
    "Silence tightens, then fractures into low, urgent conversation as everyone tries to triangulate truth, risk, and consequence. Voices overlap—practical plans, moral arguments, fears. The arousal climbs: the music swells, footsteps on stairs echo, a distant chant"
    "rises from the market—someone has posted a truncated note and people are already forming opinions."
    "You realize you are at the fulcrum of something that will not be undone with a single apology."
    hide kai_moreno
    hide rosa_alvarez
    hide samira_chen

    scene bg ch11_e67f19_3 at full_bg
    # play music "music_placeholder"  # [Music: A singular, high sustained note that refuses to resolve]
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "Whatever you do, act like you'll have to live beside the consequences. Not just for you—but for the children at the Flats, for Kai's customers, for everyone who counts on this place being more than a line on a map."

    "Ibrahim 'Ibe' Rafiq" "You need to pick a posture. Pushback or build. Both cost."
    show kai_moreno at right:
        zoom 0.7

    kai_moreno "But silence costs too."
    "Your mind runs through possibilities—public outcry, legal steam, negotiated compromises, quiet resilience. Each branch forks into faces you love and faces that will be hollowed out by what follows. You imagine Eloise Varela, cool and implacable,"
    "watching her plan either crumble into scandal or be smoothed into law. You imagine the town's children, the Flats' corridors, the greenhouse seedlings you and Rosa coaxed through a harsh winter."
    "Your pulse matches the drums of the city; high, urgent. The decision approaches like a storm front."
    # [Scene: Municipal Offices—Records Room | Night]
    hide rosa_alvarez
    hide kai_moreno

    scene bg ch11_e67f19_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hum of refrigeration, distant printer whirring, rain beginning against the windows]
    # play music "music_placeholder"  # [Music: Staccato strings, tension ratcheting higher]
    "Samira motions you into a small, glassed room. She slides the drive into a secure reader on the municipal terminal and projects the redlined amendment onto the wall. The legalese unfurls in cold, clinical type—lines crossed out, phrases inserted, signatures digital and faint."
    show samira_chen at left:
        zoom 0.7

    samira_chen "See this clause? 'Redevelopment priority'—it shifts the burden of proof to residents. They must demonstrate harm to remain eligible. That's a procedural death sentence. Families without legal savvy get swept."
    "You read each line like a secret being unspooled, and every clause lands like another weight on the town's shoulders."

    "Ibrahim 'Ibe' Rafiq" "If they get this through the council, it will be functionally impossible for most to resist displacement. The 'shield' becomes a sieve."

    samira_chen "I can run it. I can push it to the feeds. Or I can help you use it to negotiate. Or—"
    "You think of the calculus of exposure: public pressure can undo a plan, but it can also invite punitive clamps and rash decisions from frightened officials. Quiet bargaining can protect lives with fewer flames, but it"
    "asks you to trust those who have already wielded power against the town's marginal voices. Doing nothing preserves people in the short term but may allow a legal framework to ossify into injustice."
    "Your throat tightens. The arousal peaks—a sharp, bright urgency. You can feel the room pressing in, the air itself taut with possibility; every fraction of a second now carries the weight of futures."
    show rosa_alvarez at right:
        zoom 0.7

    rosa_alvarez "What will your people need in each outcome? Who will you be accountable to when the noise dies down?"

    "Ibrahim 'Ibe' Rafiq" "I'll stand with you, whatever you decide. But know what you'll be asking from people."
    "You look at the projected words, at Samira's face—complex and unreadable, a map of someone who has already crossed lines she now fears—and at the steady, determined faces of Rosa and Kai. You think of the"
    "Flats' mud and the seedlings, of all the small resistances that make a town liveable."
    "You press the drive into your palm, feeling its cold promise."
    # play music "music_placeholder"  # [Music: Crescendo; high strings and a percussive heartbeat]
    # play sound "sfx_placeholder"  # [Sound: A distant crowd starting to chant—two words caught in the night air: "Hold—Home."]
    "Everything narrows to a point."

    menu:
        "Publish them publicly to ignite mass action and legal scrutiny.":
            jump chapter14
        "Use them as private leverage to broker a more protective hybrid policy.":
            jump chapter17
        "Keep them confidential and redirect energy to direct community resilience.":
            jump chapter18
    return
