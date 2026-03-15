label chapter11:

    # [Scene: Tideward Rooftop Garden | Late Afternoon — Storm on the Horizon]

    scene bg ch11_e67f19_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind skirting the awnings; a gull crying like a thin bell]
    # play music "music_placeholder"  # [Music: Low, tremulous strings; a distant drum of rain]

    "You leave the tablet face-up on a reclaimed-wood bench and stare at the photograph until the edges of the image blur. The caption—slick type, insinuating tone—reads like a verdict" "Pilot Project: Boondoggle or Lifeline?"
    "The garden smells of wet soil and citrus, but beneath that is diesel and the metallic tang of salt. A bee claws at the glass of a planter and the city below seems both ordinary and"
    "fragile: market lanterns blinking like small defiant suns, alleys folding into their own histories. You feel, physically, the compass at your throat as if it were a small heart beating faster."
    "Professor Anika’s words circle in your head—hold this space visibly. Make the public see this is for people's lives—not for contracts. You thumb the screen and open the live feed from the pilot site. Rain has"
    "picked up along the skyline; camera lenses smear with motion. A knot forms in your stomach that has nothing to do with weather."

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmured chants from the live feed, pages of a leaflet rustling]
    "You know the pilot is a political animal as much as it is technical. Now it is hungry and noisy."

    menu:
        "Sprint to the pilot site":
            "You grab your windbreaker and hurl yourself down the service stair, the rent-a-bike clip clanging at your hip, adrenaline sharpening the world into closer edges."
        "Stay and coordinate from the roof":
            "You tuck the tablet under your arm and start triaging—press statements, two calls, a prioritized list—your world reduced to text and tone."

    # --- merge ---
    "Continue"
    # [Scene: Maris Institute — Coastal Research Lab / Planning Atrium | Early Evening — Storm Approaching]

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The building’s ventilators struggling; the distant thump of the pilot site's loudspeaker through a thin wall]
    # play music "music_placeholder"  # [Music: A taut minor piano motif; a single low hum underpins the room]
    "You arrive with salt on your collar and your notebook somehow heavier than it ought to be. Engineers are already clustered around a cluster of monitors, their faces lit from below by flood-models that churn in"
    "cold colors. A sticky urgency has turned the atrium into a command room; the municipal feeds are split into tabs, each with different versions of what might happen."
    "Elias Kade is there before you—neat, contained, sleeves rolled up just so. He doesn't wait for you to ask his read; the lines around his mouth are tight but controlled."
    show elias_kade at left:
        zoom 0.7

    elias_kade "We can't leave the gates open during a surge. If the pumps fail, the tideways will backflow and—' (he hands you a schematic) '—we lose containment. Temporarily sealing them keeps damage localized. It's an emergency protocol."
    "You can see why he favors the closure: the lines on the map are tidy, the models conservative, the numbers speaking a comforting language. But the models don't carry a grandmother's seam-stained apron or a fisher's early-morning route to the market."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Sealing is fast, yes. But 'localized' looks different to people who live off the tide. Those closures cut livelihoods. They shut alleys that double as vendor routes and cripple fishers who run on the tide schedule. There has to be a way to stage shut-offs so they don't strand people."
    "Elias Kade: (a measured exhale) 'Staging is slower. Slower can mean failure. If the pumps can't keep pace we risk a catastrophic breach. I'm not asking you to choose convenience over safety—I'm asking you to accept a protocol that minimizes long-term loss.'"
    "You hold the schematic between you like a thin wall."
    "Nova Duarte arrives on the feed first—then in person—her presence a thread pulled taut. She is wet at the collar, hair braided with sea-glass beads, and there are people behind her holding hand-painted signs. She walks"
    "into the atrium as if into an amphitheater and the cameras find her, greedy for clarity."
    show nova_duarte at center:
        zoom 0.7

    nova_duarte "They're calling this a hybrid and then outsourcing the hard parts. They cut the neighborhood ties to make a prettier ledger. We are here because people are being priced out of their own protections."
    "Her eyes sweep the room and land on you. There is no accusation in the face she gives you—only a complicated stare that says: I expected more, but I also know the work you've done."

    mara_lin "I hear you. I signed onto this with the same promise you did—community oversight. But right now we're balancing models and movement, and a blunt closure could wreck the very people we're trying to save."

    nova_duarte "Promises are cheap when the city's ledger is heavier than our neighbors' lives."
    "Her tone is both accusation and plea. It's a line threaded with history; you cannot untie it with a single answer."
    "Professor Anika steps into the fray, voice cool but urgent."
    hide elias_kade
    show professor_anika_bhat at left:
        zoom 0.7

    professor_anika_bhat "A misstep now will delegitimize the hybrid approach. If the public narrative becomes 'pilot harms people'—and the mayor's office is already spinning for optics—we lose more than funding. We lose trust."
    "Samir Reyes, cheeks still wind-pricked, pushes through with a folded envelope in his hand. He looks like someone carrying something that matters more than the cold."
    hide mara_lin
    show samir_reyes at right:
        zoom 0.7

    samir_reyes "This came from Mrs. Ebbett. She won't go. Says her handwriting ain't what it used to be, but she'll be damned if she lets council move her garden out for a 'phased trial.'"
    "You take the letter. Her letters wobble; the ink has bled in places. You read it aloud because sometimes hearing a voice say these things grounds the abstract."

    "Mara Lin (reading)" "'To Mara — I've watched this bay for sixty-one years and I don't trust 'better plans' that ask me to leave the people I've fed. If the city closes the lane, you'll have my key. You decide if that's the same as abandonment.'"
    "Silence becomes a rope in the room. The monitors keep forecasting surges, but your throat tastes like the salt you breathed in the garden. You want to promise everything—safety, dignity, continuity—but promises are brittle when pressed into policy."

    menu:
        "Promise you'll protect her alley":
            "You fold the letter carefully and tell Samir you'll fight for exemptions for known livelihoods, voice low and exact. The room hears resolve; it's a sharp, fragile shield."
        "Admit you might not be able to stop closures":
            "You unclench, tell Samir the truth — that there's a very real chance the closures will happen and that you'll do everything to soften the blow. His jaw tightens, but he nods as if hearing the truth is some comfort."

    # --- merge ---
    "Continue"
    "Elias interrupts, the engineer in him unwilling to linger in sentiment when systems are failing."
    hide nova_duarte
    show elias_kade at center:
        zoom 0.7

    elias_kade "We have an instrumentation reading—pressure spikes along the tideway. If we delay, automatic fail-safes might trigger a full lock. That will be worse. We can negotiate support packages for displaced vendors after, but right now—"
    hide professor_anika_bhat
    show mara_lin at left:
        zoom 0.7

    mara_lin "Support after is too late for people who need cash to eat tomorrow. We have contingency funds for emergency relief, and we've already routed small-business stipends. The issue is synchronous timing: shut-offs timed to low tides, prioritized lanes for vendors. It can be done."
    "Elias Kade: (frustration rising) 'You're negotiating with a draining clock, Mara. Compromises take time. Time is what the tide doesn't give us.'"
    "The room frays into half-answers and technical jargon. Cameras pick up faces and edit them into frames that will become headlines. Outside, in the storm-rough sky, thunder rolls like an impatient judge."
    "Professor Anika: (softly) 'If Nova's protest becomes the headline, and if a closure occurs that clearly harms people, the council will distance itself. The mayor will pick the path that looks politically survivable. You know that.'"
    "You do. You know the thin arithmetic of politics too well—the way a mayor weighs a photo-op against a policy and chooses the one that keeps lights on and donors quiet."
    # [Scene: Pilot Sites | Simultaneous — Street-Level — Rain and Protest]
    hide samir_reyes
    hide elias_kade
    hide mara_lin

    scene bg ch11_e67f19_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A single chant rising and falling; a discrete sound of a loudspeaker clipping into feedback]
    # play music "music_placeholder"  # [Music: Dissonant cello strokes]
    "Nova's protest on the ground is careful, suture-like—no mass arrests, no violent confrontation, but a visible human chain between workers and machines, placards that read 'Protect People, Not Profits' and 'Community Oversight Now.' Cameras feed the"
    "image back into the atrium's screens. The coalition's spokespeople, on mic, are split; some insist on non-violence, others push for louder rhetoric. The narrative becomes a fissure that spreads along the edges of everything you've built."
    "Someone—an aide, a reporter, a source—leaks a short video clip showing a contractor's van leaving the pilot site with crates. It's grainy, compelling. The caption lands like a stone."
    # [Scene: Maris Institute — Planning Atrium | Night — The Long Watch]

    scene bg ch11_e67f19_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The HVAC is a steady oceanic exhale; a pager beeps occasionally]
    # play music "music_placeholder"  # [Music: A single prolonged note; then, silence]
    "You don't go home. There is nowhere home goes in this moment that will let you sleep. You curl your thin scarf around your neck and lie on a strap of polished bench, monitors for a"
    "ceiling. A cold draft finds the small space between your shoulder blades. You stare at flood models that refuse to resolve—the numbers blinking like constellations you have to map before dawn."
    "In the dark, voices from earlier loop through your mind: Nova's insistence, Elias's practical curt replies, Anika's soft warning, Samir's folded envelope. Your optimism, the sort bolstered by plans and community roots, feels thin as paper and just as likely to combust if a stray spark finds it."
    # play sound "sfx_placeholder"  # [Sound: Distant thunder; a soft chest of rain at the windows]
    "You sleep in fits. Between them come dreams of wooden hulls and water licking at threshold planks. When you wake, it is to the cold, electric sting of a notification."

    scene bg ch11_e67f19_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Mayor Chen's voice — polished, flat — overlaid with the hum of an attentive press]
    # play music "music_placeholder"  # [Music: A descending piano figure]
    "The Mayor's statement is all poise and inevitability. She talks about fiscal responsibility and safeguarding the city's long-term future. What she doesn't say—what appears later in a leaked budget pdf—is a set of line items the city's finance office quietly struck overnight."
    "You read the redacted memo and feel the world tilt: key funding lines for the pilot have been cut. The amounts are suspiciously neat, reduced to placate certain stakeholders whose logos you can almost see behind the mayoral smile."
    "Your breath goes thin. Trust, which was already fraying like an old rope, frays further and knots in new places."
    "Elias Kade finds you by the monitor, eyes tired and blunt."
    show elias_kade at left:
        zoom 0.7

    elias_kade "She cut it. They made it look like a reallocation—'emergency fiscal prudence.' But it's a cut. They appeased a donor with a reduction in our staffing and contracting lines."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Who leaked the memo? How public is this—"
    "Elias Kade: (a half-laugh that is not funny) 'Public enough. Social feeds have it. The contractors who depended on that line are already posting sympathetic statements. Nova's people think this proves our point. The mayor thinks this buys her time.'"
    "Nova Duarte, present in the atrium not by chance but by insistence, watches both of you with a look that warps between vindication and sorrow. Her face is unreadable in a way that fits both anger and exhaustion."
    show nova_duarte at center:
        zoom 0.7

    nova_duarte "They always make a show of balance until it's time to pick winners. And the winners aren't the people who harvest in the dark or put up tarpaulins to keep their kids dry. They're the donors that buy a tranquil cut in the budget."
    "The coalition's spokespeople begin exchanging texts—sharp, short, full of blame. Accusations flare: someone says you were too conciliatory; someone else says Nova's protest played into the mayor's hands by making closure inevitable. The public narrative narrows to either/or: technocracy or radical retreat. Your hybrid—nuance—becomes a confusing smear in the press."
    "Samir sits across from you, eyes rimmed red from lack of sleep. He sets another envelope down—this one a community petition, signatures bobbing like tiny islands."
    hide elias_kade
    show samir_reyes at left:
        zoom 0.7

    samir_reyes "They're saying we started the chaos. That if we hadn't pushed the 'community oversight' line, Chen wouldn't have to cut. It's bullshit, but the soundbite sells."

    mara_lin "We can't let them rewrite this into 'movement vs. safety.' It wasn't supposed to be that."
    "Samir Reyes: (voice low) 'Then what now, Mara? What do we do when the mayor plays chess with people's bread?'"
    "Your stubborn optimism cracks—an audible thing behind your ribs. It isn't giving up, but the shape of what you believed possible shifts, like a shoreline under storm surge. You feel the project as a fragile boat, planked and patched, rolling in a sea of headlines and ledger cuts."
    "Elias Kade reaches toward you across the bench, then pulls his hand back."
    hide mara_lin
    show elias_kade at right:
        zoom 0.7

    elias_kade "We need to respond. If we sit quiet they cut us and the pilot dies. But an aggressive response—public pressure and legal action—might force the mayor's hand. If the mayor caves, we get funding back. If she doesn't, we escalate."
    "You think of legal fights that drag on while tideways flood. You think of Nova's banners and the faces of people in rain, and you think of Mrs. Ebbett's cramped handwriting that refused to be erased."
    "Professor Anika's voice cuts in, not loud but carrying the weight of someone who has seen these cycles before."
    hide nova_duarte
    show professor_anika_bhat at center:
        zoom 0.7

    professor_anika_bhat "Choose your escalations carefully. A public shove could force accountability, yes. But it could also make the mayor dig in and privatize the narrative. Strengthen local capacity quietly, yes—but don't let the mayor set the terms of engagement while we shrink."
    "Nova Duarte: (leaning forward) 'The mayor's hands are already dirty. Waiting politely won't fix that. We make them own their choices.'"
    "The coalition fractures in small ways that hurt like splinters: spokespeople who used to coordinate now send statements that contradict one another; a volunteer coordinator calls in sick, exhausted; a sympathetic councilmember sends a private message"
    "that reads like a math problem and nothing like solidarity. Each small rupture feels enormous."
    "You feel every one. You feel the weight of every person who relied on your plan as if that weight were stitched into your bones."
    "Silence falls between the three of you—Elias's neat pragmatism, Nova's burning insistence, your stubborn, faltering hope. The rain is a steady percussion against the atrium glass."
    "You realize the choice ahead is not just strategic—it is moral, a liminal decision about how to bear witness, where to put your energy, and how you will define the meaning of protection in a city that keeps recalculating what it can afford to save."
    # play music "music_placeholder"  # [Music: A single long, low chord; then, a hollow pause]
    "The room waits. The monitors keep their cold glow. Outside, the bay keeps climbing in a way that will not be contained by a single policy memo or a single protest sign."

    menu:
        "Publicly pressure Mayor Chen with a media campaign and legal action.":
            jump chapter12
        "Refocus locally: strengthen pilot programs privately while avoiding spectacle.":
            jump chapter15
        "Broker a painful concession: accept phased retreats for some blocks to secure funding for others.":
            jump chapter12
    return
