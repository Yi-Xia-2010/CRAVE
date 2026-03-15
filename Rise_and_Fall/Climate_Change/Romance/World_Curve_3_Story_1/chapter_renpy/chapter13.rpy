label chapter13:

    # [Scene: Salt Flats Lagoon | Dawn]

    scene bg ch13_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant pumps thrum a patient bass. Gulls argue over a discarded net. Voices — some relieved, some angry — ripple along the boardwalk like wind over reeds.]
    # play music "music_placeholder"  # [Music: A cautious, rising piano motif]
    "You stand where the demo began, boots pressed into mud that is still warm from the day before. Salt crusts at the hem of your jacket; the compass pendant at your throat is damp with sea-spray."
    "Around you the town smells of wet canvas and coffee and the iron tang of equipment; beneath it, the faint sweet of peat where the marsh is learning to breathe again."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "They shut it down within hours. I—"
    "(he exhales, the sound small against the lagoon)"

    jonah_reyes "—I thought the city would look the other way."
    show mara_solano at right:
        zoom 0.7

    mara_solano "They couldn't, not after Claire's readout and the footage.' Your voice tastes of gravel and relief. 'Once the demo failed in front of regulators, it stopped being a PR model and became evidence."
    "Dr. Claire Hsu approaches with a roll of printed graphs under her arm, shoes muffled by mud. Her lab vest is flecked with silt; she looks tired but steady in that way that means the mathematics are still obeying her."
    show dr_claire_hsu at center:
        zoom 0.7

    dr_claire_hsu "The failure modes were clear,' she says, hands finding yours briefly when she passes you the printout. 'The load dispersion didn't account for the scour we measured. We showed staged stress at three points; the anchors she specified would have exceeded tolerances within a five-year, high-frequency storm cycle."
    "You glance at the graphs. The numbers line up like constellations you've memorized; they make sense in the literal way that brings scissors to tangled string."

    mara_solano "The moratorium—it's temporary, but it's a start."

    dr_claire_hsu "Temporary can become precedent. Funders hate flip-flopping, but they respect documented risk. If we push the policy narrative from 'failure' to 'alternative' fast enough, public dollars will follow safer models."
    "A cheer rises from the edge of the marsh — some in the crowd are grinning, eyes wet. A man who runs a small boatyard laughs, his voice rough and joyous. But not everyone is smiling:"
    "a vendor folds up her stall with hands that tremble, muttering about missed contracts and debts. A teenage volunteer stands with a placard that reads SAFE SHORES, knuckles white where it presses into cardboard."
    "Aunt Pilar's voice — calm and low — threads through the crowd, anchoring the fluctuation. 'Courage has a cost,' she says, though she is at the edge of where you can see her, like a lighthouse haloed by spray. 'We've paid before. We know the calculus.'"
    "Jonah moves closer to you, steps measured as if approaching a fragile thing. He doesn't raise his camera; instead he wipes a smear of mud from his palm on his jeans and looks at you, open and raw."

    jonah_reyes "You could have walked away when I said 'expose'.' He lets the sentence hang. 'You didn't."
    "Mara Solano: (the answer is a half-laugh that isn't wholly light) 'You didn't either.' You feel the admission thread through your spine like a small, dangerous needle. 'We made it visible. People have to know what they'd be signing up for.'"
    "Jonah's smile is quick and imperfect. 'So what now? Lawsuits? Community assemblies? Claire becoming our... official validation squad?'"
    "Dr. Claire Hsu: (a dry little smile) 'I am not a squad. But I can testify. And I can write the report so regulators have to act on it, not just think about it.'"
    "The crowd begins to move toward the planting area where a small team is already pushing slender plugs of cordgrass into the mud. Each plant is a tiny, stubborn flag. Your hand finds one of them; its roots are cool and gritty between your fingers."

    mara_solano "We plant. We document. We make the alternative real, not just protest."
    "Jonah reaches for your hand and this time there is no drama in it — only the solid pressure of someone who will stand. The camera hangs quiet between you two, a witness resting."

    menu:
        "Step into the planting line and start with the others":
            "You kneel into the soft silt, mud sucking at your knees. The physical act grounds you—each plug settled is a small promise, the work intangible until your palms are raw and the seedlings stand upright. People nod when you pass them tools; a child offers you a clumsy pat on the back. The world rearranges itself into work and meaning."
        "Walk over to Claire and talk policy, printing in hand":
            "You step beside Claire and review the report, the graphs a cold comfort. Talking through clauses and timelines makes action feel like machinery you can tune; your voice catches on legalese but you press through. Claire reads the room and the models; the possibility of binding oversight makes your chest loosen in an entirely different way."

    # --- merge ---
    "You choose and the moment you commit — mud or paper — the day sharpens. People respond not to the abstract of justice but to the concrete of your hands or words, and both are needed."
    hide jonah_reyes
    hide mara_solano
    hide dr_claire_hsu

    scene bg ch13_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The community's murmurs blend into coordinated instruction: "Mud deeper here," "Hold the plug steady," "Sign here for witness."]
    "A cluster of volunteers carries an old wooden sign — repurposed from campaign wood — toward the demo barricade. Someone tacks it up: COMMUNITY COALITION FOR WETLANDS. The act is small and absurdly human; a rallying stub of hope on a thing that was meant to intimidate."
    "Jonah watches the sign go up, then looks at you with something like a plan settling into place."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "We document the restoration. We make sure funders see this as not charity but investment: biodiverse buffers, jobs for co-op members, data that reduces risk. We sell resilience as infrastructure that keeps people here."
    show mara_solano at right:
        zoom 0.7

    mara_solano "We make the math social.' (You feel the phrase land, weighty and right.) 'We tie it to livelihoods; grant writers like stories and spreadsheets. We need both."
    "Claire overlaps, already thinking in timelines. Dr. Hsu pulls you both into a quick, efficient schedule: sediment sampling, seed sourcing, permit filings, public testimonies. Her fingers move over the list like a conductor's baton."
    show dr_claire_hsu at center:
        zoom 0.7

    dr_claire_hsu "And you will need legal witnesses,' she says. 'I'll provide the data. We'll need testimonies from those who would have been displaced. We must humanize the metrics."

    "Someone in the crowd calls out, skeptical" "And what about people who want the wall? What about the certainty Elena promised?"
    "Mara Solano: (you hold the look, not because you have an answer that will please everyone but because the work demands honesty) 'I understand that fear. I don't have a perfect shield. We traded the promise"
    "of absolute certainty for a chance to keep the fabric of our town intact.' Your voice is steady; the salt in your throat doesn't crack it. 'That's not nothing.'"
    "A hush follows — not all of it forgiveness, but attentiveness. A handful of older neighbors nod slowly, eyes reflecting lamplight and salt."

    menu:
        "Speak privately with the vendor who is worried about lost income":
            "You crouch in front of her stall, breathe the smell of fish and fried dough, and offer a concrete plan — a market stipend and work roles in the restoration. She listens, guarded, then softens at the specifics. A promise with a timeline does more than words."
        "Walk the barricade line to thank the volunteers who risked arrest":
            "You walk the line of faces — teenagers with bright scarves, elders with steady hands — and your thanks sound like ordnance and balm. They exchange stories of nights on watch, and you feel the communal seam tighten as people trade fatigue for purpose."
        "Return to Jonah and help frame a visual narrative for funders":
            "You stand with Jonah again and together you storyboard: the failed demo, the seedlings, the faces of the people who will tend them. Visuals that combine data and dignity. Jonah nods, energized by the task; his camera cap comes off for a moment and he shoots a few quiet frames."

    # --- merge ---
    "Each small choice ripples outward — a vendor believes in a schedule, a volunteer feels recognized, a funder sees a story they can tell. Claire files the report; regulators stamp a moratorium notice into public record;"
    "a local news van flashes its lights across the mud. For all the scars the action leaves on reputations and on your quiet hours, the visible result is undeniable: the demo no longer stands as a"
    "promise; it stands as a wound that required stitches, and the stitches are community hands."
    # play music "music_placeholder"  # [Music: Swell of strings, warm and ascending]
    "Days fold into one another. You sleep less; the watch on your smartwatch counts out three-hour blocks interrupted by emails and neighbor visits. Your notebook grows dense with tasks: permit numbers, grant names, seed suppliers with"
    "local provenance. You learn the taste of exhaustion that smells faintly of coffee and marsh loam."
    "But the seedlings take root. At dawn you find yourself on the mud again, pressing cordgrass in place with Jonah at your back, Claire checking salinity with a handheld probe. The seedlings hold against a small morning surge; their blades tremble and then steady."
    "Jonah Reyes: (softly, as he hands you a trowel) 'You know, when we were kids we used to come out here and make forts. Nothing complicated — just sticks with seaweed flags. I never thought we'd be building forts to keep the town.'"
    "Mara Solano: (a laugh escaped you, wet and honest) 'We always built forts the same way: temporary, improvised, meant to teach you how to return. Maybe that's what resilience is.'"

    jonah_reyes "Maybe resilience is practice."

    dr_claire_hsu "Your data is already in the hands of three trustees and one regional office. The moratorium's renewal hinges on our next sampling season, but we've bought time.' She looks at you, eyes tired and triumphant. 'This looks like a climb. It's a climb I didn't think we'd get the permits to make."
    "You close your eyes for half a breath and imagine the arc of that climb — not a clean slope but a series of raw, necessary steps. Your chest, which has been tight with the memory"
    "of the storm that took your father, loosens in a way that feels almost foreign: there is space for grief and for action. The hold the past had on you stems in part from feeling powerless."
    "Now, the small, messy progress tastes like reclaiming."
    "In the market later, a funder — younger than you expected, hair still wet from a bike ride — approaches Jonah with cautious curiosity. He asks about community governance and returns with a check, small but"
    "earnest, earmarked for a pilot payroll for restoration teams. It isn't enough to cover everything, but it buys wages for three local workers for a season."
    "A cluster of neighbors gather that evening on a makeshift bench. Someone brings out a battered guitar; someone else ladles soup into paper bowls. The mood holds the frayed edges of joy. People trade both predictions"
    "and recipes, and when you laugh at a joke about 'engineering habitat with duct tape,' the sound is a small, crucial thing."
    "You think about Elena Voss — about the sterile promise of certainty she offered, the engineers who calibrated models behind glass. The public view of her plan is scarred now; the moratorium mocks her timing. Yet"
    "you also know that certainty has a seductive gravity. Some neighbors, exhausted and pragmatic, still whisper that they'd rather accept a wall and free the worry."
    "Mara Solano: (to Jonah, later, when the crowd has thinned) 'We did what we had to. The moratorium, Claire's readout, the pilot funding—none of it solves everything, but it's movement. That's important.'"

    jonah_reyes "Movement is contagious.' He wipes his hands on his jeans, leaves a dry smear of salt, and squeezes your fingers. 'You taught me that."
    "You let the words sit between you like a shared map. Your compass pendant warms against your skin, not from the sun but from the way resolve settles into your chest."
    hide jonah_reyes
    hide mara_solano
    hide dr_claire_hsu

    scene bg ch13_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind through young marsh grass, a low human murmur scaling into multisyllabic laughter]
    # play music "music_placeholder"  # [Music: Full, gentle orchestral lift — hopeful, but earned]
    "Night comes and you walk home along the boardwalk, the tide whispering under the planks. Your steps are measured; your mind tumbles through lawsuits, meetings, grant cycles, the list of people who still fear displacement. There"
    "are costs written into your name now — subpoenas, an angry editorial that accuses you of incitement, a late-night call from a neighbor who needs help moving valuables before the next expected surge. These will be"
    "debts you will pay in exhaustion and patience and the slow mechanics of bureaucracy."

    "And yet: there are also small credits. The market's co-op has a new line item in its ledger for restoration wages. Claire texts you the line from a regulatory email" "Immediate moratorium in effect pending structural audit."
    "You pause at a low rise and turn to look back at the tidal mirror. The world is not saved; it is, stubbornly, being tended."
    "Jonah Reyes: (quiet, determined) 'We climb, and we help each other climb with tools that won't break when the wind comes. Maybe that's our legacy.'"
    show mara_solano at left:
        zoom 0.7

    mara_solano "Maybe our legacy is teaching the town how to refuse erasure.' You let your voice hold the future, neither claiming it nor hiding from it. 'Not perfect. Not the same for everyone. But ours."
    "Jonah squeezes your hand. For a long moment you both look at the seedlings — at the tiny green arcs that promise more spring — and the tightness in your chest becomes something you can carry like a load shared between two people."
    hide mara_solano

    scene bg ch13_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant, steady rhythm of pumps like a watchful heartbeat]
    # play music "music_placeholder"  # [Music: Gentle diminuendo into soft resonance]
    "You sleep less. You work more. You do not stop mourning what was lost. But the hole that opened with the storm begins to narrow. It is not healed so much as filled — with seedlings,"
    "with schedules, with protests turned into policy, with a kind of partnership that is political and tender at once. The climb will have more raw places, and the climbs will cost you both, individually and together."
    "Still: the ground is raw but fertile. You planted something here that did not exist before — a possibility that other hands will tend. And when you wake before dawn to check the tides, you find yourself humming an old, small song as you press another seed into wet soil."
    # play music "music_placeholder"  # [Music: Final chord — bright, sustaining]

    scene bg ch13_601bcb_5 at full_bg

    scene bg ch13_601bcb_6 at full_bg
    "THE END"
    # [GAME END]
    return
