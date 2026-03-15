label chapter8:

    # [Scene: Rooftop Greenhouse | Night]

    scene bg ch8_6b08b4_1 at full_bg
    # play music "music_placeholder"  # [Music: Quickened string ostinato under a bright piano motif]
    # play sound "sfx_placeholder"  # [Sound: Rain tapping hard against the greenhouse glass; the low, steady thrum of distant diesel pumps]
    "You are bent over the table, sleeves pushed to your elbows, a fold of printed memos cutting into the pad of your thumb. The light here is soft and forgiving but it throws every smudge on"
    "the maps into a hard line: scribbled relocation boundaries, spreadsheets with neighborhood names you know by the sound of their chimneys, and a set of internal memos that smell faintly of printer ink and old paper."
    "Your eyes ache—hazel, tired, a little rimmed red—but they narrow anyway. You trace a proposed levee line with the tip of a pencil and feel the muscle memory of engineering: nodal points, load distributions, evacuation corridors."
    "The numbers promise a shield for the main arteries of Mariselle. The memos promise federal money if the package signs off on 'phased relocations' to reduce exposure in low-lying blocks."
    "You breathe in. The greenhouse smells like peat and wet cardboard and the urgent, metallic tang of decisions. You promised—quietly, to yourself—that your plans would save more than statistics. The signature you put on the pilot last week is still warm under your skin."

    scene bg ch8_6b08b4_2 at full_bg
    "A distant shout cuts through the rain—sharp, alive. Footsteps slap on the metal stairs outside. You look up."
    # play sound "sfx_placeholder"  # [Sound: Murmurs swell, then settle; the glass door opens with a breath of colder air]
    show sora_watanabe at left:
        zoom 0.7

    sora_watanabe "Ari."
    "You stand without thinking, the table scraping once. For a beat you only take them in: the bandana half-untied at the neck, a smear of protest paint on a cuff, a flyer clenched in their fist."
    "Sora's face is flushed from cold and adrenaline; their eyes are larger than usual, the kind of wide that means they've been shouting for hours."

    sora_watanabe "We put up signs at the Old Harbor. People came. Maya was there. You should have seen—' (they cut off, the breath a sharp edge) '—you should have been there."
    "You can hear the accusation under the words, but their voice carries something else too: a raw, trembling care that makes your chest tighten."
    show ari_navarro at right:
        zoom 0.7

    ari_navarro "I showed up where it mattered, Sora. I signed the pilot because—"

    sora_watanabe "Because Lina asked you to lead the study. Because she knew you'd make it look accountable. Because she needed your maps to get the money she promised would save people."
    "You try for evenness. Your fingers find the edge of the memo stack and you thumb it like a metronome."

    ari_navarro "The pilot buys time. It gives us a way to build protections now while we work on—"

    sora_watanabe "Time? Ari, this memo says whole blocks are 'reclassified.' People we grew up with—Maya's lane, the boatwright's shop—listed for phased relocation. You can't decide to move our neighbors like chess pieces."
    "Sora's hands shake. For a moment their fury and grief are raw and unscripted, an exposed nerve you can almost feel."

    ari_navarro "I haven't decided anything yet.' (you wish the words felt truer) 'I am still going through the models."

    sora_watanabe "Then do that in public.' (they jab a finger toward the table) 'Don't bend the ledger to make a funding threshold look prettier."
    "You open your mouth to say more; then the metal door at the greenhouse's far end swings again. Lina Moreau steps in, wrapped in her bespoke coat, wet hair pinned perfect despite the rain. Her presence"
    "cools the air—precisely arranged, not a hair out of place. A tablet is clutched to her chest; her gold hoops flash under the amber lamp."
    show lina_moreau at center:
        zoom 0.7

    lina_moreau "Late night, Ari. The council wants the recommendation in the morning. They want a forward-facing option and a backup. Ephraim sent an expedited augment if oversight is loosened by the municipal clause. He believes in efficiency."
    "Sora's jaw moves like they might spit the word 'Ephraim.' Lina watches you with a steady, contained regard. There's the smallest tilt—an almost-imperceptible patina of vulnerability that doesn't translate to sentiment so much as calculation."

    lina_moreau "If you recommend targeted relocations, the levee funding is unlocked. That saves the corridors—school, hospital, main arteries—probably hundreds of lives in the next storm season. If you push for alternatives and more time, we risk losing the federal window. And if we lose the window, we lose leverage."

    ari_navarro "Leverage for whom?"

    lina_moreau "For the municipality. For the people hooked into infrastructure. For the town as a whole."

    sora_watanabe "For the town as a ledger, you mean."

    menu:
        "Put down the memos and go find Maya at the Old Harbor":
            "You snatch your raincoat, the paper rustling under your arm. The cold night hits like a reality check—people are shouting, there are faces that know your name. You take one last, loaded look at Lina and step out into the rain."
        "Stay and insist on reviewing the models with Dr. Noor first":
            "You shake your head and reach for the lab phone. You need the numbers to be clean. Dr. Noor's voice will steady you; a technical truth feels like an honest one."

    # --- merge ---
    "Sora watches you choose; their expression softens fractionally, then regathers into wary hope."
    # play sound "sfx_placeholder"  # [Sound: Your watch buzzes—a terse ping; it reads: 'Ephraim — call. 00:12']
    "You ignore the call. For a moment you think that by not answering you can hold open more possibilities; by delaying you can keep from being pushed into a single frame. But the greenhouse fills with people and agendas and the air tastes like decision."
    # [Scene Transition: Tidewatch Lab Office | Late Night]
    hide sora_watanabe
    hide ari_navarro
    hide lina_moreau

    scene bg ch8_6b08b4_3 at full_bg
    # play music "music_placeholder"  # [Music: The strings quicken; a single high piano key repeats like a heartbeat]
    show dr_noor_patel at left:
        zoom 0.7

    dr_noor_patel "Ari, sit."
    "You do. The lab smells of coffee and antiseptic and the hum of machines. Noor's eyes are kind and tired; she folds a printout into your hands without looking at it."

    dr_noor_patel "Our regional model had a sensitivity range we underweighted. We used conservative uplift parameters to avoid alarm. In real terms—that is, if certain storm-track correlations shift—we could be underestimating wave runup on lower blocks by as much as a meter."
    "Your mouth goes dry. A meter. The number spins into the map in front of you and forces a new contour line across neighborhoods you love."
    show ari_navarro at right:
        zoom 0.7

    ari_navarro "Why now? Why tell me—"

    dr_noor_patel "Because I trust you to make the human call, not only the political one. The funding will be here if you sign the package that includes relocations. If you refuse, we might not secure the levee in time. The models are imperfect; the choice is between a statistically safer corridor and the cultural loss of neighborhood continuity."
    "Noor's hands are steady, but her voice is small—like she is passing a fragile thing across a room and hoping you catch it."

    dr_noor_patel "I am sorry. I should have been more forthright in the first briefing."

    ari_navarro "You couldn't tell. The numbers would have destroyed the pilot before it started."

    dr_noor_patel "Perhaps. Or perhaps we would have had a different conversation. But circumstances demand a choice now. Your recommendation matters. The moral calculus is not abstract."
    "You stare at the printout until the letters blur. The greenhouse lights seem softer compared to the harsh fluorescent bulbs here, but the choice is the same."
    # play sound "sfx_placeholder"  # [Sound: A commotion outside—distant megaphones, a chorus of human voices]
    "You stand. Noor reaches for your sleeve, the gesture maternal and professional at once."

    dr_noor_patel "Whatever you choose, make sure your people know you chose with the models, with the limits, and with attempts to protect dignity. Design relocation packages with legal protections; insist on binding oversight. If there is any leverage in this, use it for those who are moved."
    "Her words prick something inside you—a scaffold on which hope might be hung."
    # [Scene Transition: Municipal Council Chamber | Pre-Dawn]
    hide dr_noor_patel
    hide ari_navarro

    scene bg ch8_6b08b4_4 at full_bg
    # play music "music_placeholder"  # [Music: Percussion tightens; brass sustain to underscore the rising stakes]
    # play sound "sfx_placeholder"  # [Sound: Microphones warm up; the distant sea roars like a held breath]
    "Lina is waiting at the council dais. Ephraim stands near the back, hair damp, polished as ever. Maya slips in quietly and sits two rows back—she nods at you, eyes shadowed but steady."
    show lina_moreau at left:
        zoom 0.7

    lina_moreau "We need a recommendation that the council can adopt and present to the regional board within the hour. I want you to draft three options: A) phased relocations with levee priority, B) enhanced living shorelines and time extension, C) a blended proposal with strict oversight language. Your signature carries weight."
    show ari_navarro at right:
        zoom 0.7

    ari_navarro "If I recommend A, will you commit to the oversight measures Dr. Noor said? Legally binding audits? Community seats on the project board?"

    lina_moreau "Yes. I'll sign the oversight clause. I will push for community seats. But understand—the federal offer has conditions. Exemptions change the grant calculus."
    show ephraim_blake at center:
        zoom 0.7

    ephraim_blake "Cost overruns tick down if you reduce bureaucratic friction. A faster timeline spares transit disruption and secures private co-investment. Loosen the audits—let us run a tight schedule—and the rest follows."
    "Sora stands at the back of the chamber, fists clenched, a smear of dried protest paint at their temple. Their voice when they speaks first is low and defiant."
    hide lina_moreau
    show sora_watanabe at left:
        zoom 0.7

    sora_watanabe "We wanted a people's emergency plan. We wanted people to decide—not to be told which doors to close. If you recommend relocations without community consent, you'll be telling people to leave homes they can't fold into a packet."

    ari_navarro "No one is asking you to leave without support. Legal protections, housing credits, job transition assistance—we can design a package that respects people."

    sora_watanabe "Words. Words that sound like comfort. How many times have we been 'protected' by words?"
    "There is a taut silence. The council clock ticks audibly. You feel the arousal in your chest spike—the strings in the room tighten like a drawn bow."
    hide ari_navarro
    show maya_cruz at right:
        zoom 0.7

    maya_cruz "I run the wetland co-op. We can reassign volunteer labor, secure plants, and help retrofit foundations in some zones. If we have money on a timeline, we can buy time and build resilience that doesn't mean moving everyone."

    ephraim_blake "Volunteer labor can't replace engineering-grade levees for primary corridors. You're sentimentalizing the landscape."
    "Maya slaps her hand onto the table. 'And you're monetizing people's lives.'"
    "Lina's expression does something small and human—her jaw softens for a fraction of a second."
    hide ephraim_blake
    show lina_moreau at center:
        zoom 0.7

    lina_moreau "Ari, recommend what you think saves lives and preserves continuity where possible. Frame the relocations as targeted, temporary, and with robust resettlement support. If you advocate for more time, we lose the funding window. If you reveal the memos, we force transparency but risk political paralysis."
    "You feel every throat in the room at your back. Your fingers curl around the edge of the council table."
    "Your internal voice, usually a cool enumerator of constraints and metrics, is flooded with images: Maya's muddy hands, Sora's paint-streaked face, Noor's quiet apology, the boatwright's creaking door. Guilt mounts like floodwater—slow, insistent, and intimate as salt on skin."
    "And yet under the guilt there is another current: the pragmatic surge Noor described, the possibility that a levee could save schoolchildren, that audits could be written legally binding, that relocation—if handled ethically—could be a bridge and not an erasure."
    "The arousal in your chest reaches its peak. You are aware of the cameras, the microphones, the tiny tremor in your own voice that makes the decision feel larger than you. Your methodical calm frays into electric clarity."
    "A last, bright thought flares: decisions are quiet levers—administered in rooms like this, with hands like yours moving dials. Whatever you choose will hurt and fix and rearrange. You can make the hurt less cruel. You"
    "can force oversight into the language. You can insist that relocation be treated as an act of care, not erasure."
    "You inhale. The room leans toward you like tide toward shore."
    # play music "music_placeholder"  # [Music: Sudden swell—strings and brass converge, then drop into a held, resonant chord]
    "Decide whether to recommend targeted relocations as part of the levee package, or to advocate for alternative protections."
    "Recommend phased relocations to secure levee funding."
    "Advocate for alternative protections and push for more time."
    "Reveal internal memos publicly to force transparent negotiations."

    jump chapter9
    return
