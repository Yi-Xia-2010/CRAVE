label chapter5:

    # [Scene: Boardwalk | Low Tide Morning]

    scene bg ch5_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano, a minor key that lingers like a dropped anchor]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls; a phone vibration against wood]
    "You breathe shallowly, not from the physical effort but from the weight of what you are about to do. Your thumbs hover over the upload button; the schematic file is a map of bolts and tolerances,"
    "but it is also a map of people—where mattresses lean, where the old postman stores his tools, where your uncle keeps his spare propellers. You can feel each seam of the neighborhood in the leather of"
    "your palm."
    "Your hands shake. Not from cold—the morning has a bruised warmth, seawater on your jacket—but from the knowledge that transparency is a blade with two edges."

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A single sharper vibration as you tap "Publish"]
    "You post the schematics while the tide is low, while the sea has given you a ledger of hours. The file spreads faster than you expect: your phone pings, then sings. Messages stack—gratitude, suggested tweaks, a"
    "blurred photo of a neighbor’s improvised clamp, a gif of someone welding at 3 a.m. The old repair-shop warmth arrives in pixels and promises; for a moment you can almost smell oil and boiled coffee, hear"
    "Tomas humming while he works."
    "You stand, letting the torrent of small kindnesses wash over you. You are not alone in this; for an instant the city contracts into a room full of hands."
    "Ilan Cortez watches from where he has been standing—leaning against the rail, hatless, jaw set like a hinge. He doesn't move while the messages come, only watches as lines of blue and green light illuminate your"
    "face. You expect protest, or a fist, or a plan of countermeasures—but he simply folds his hands into his pocket and is quiet."
    show ava_marin at left:
        zoom 0.7

    ava_marin "I wanted—"
    "You don't finish. The sentence is broad enough to contain the whole city."
    show ilan_cortez at right:
        zoom 0.7

    ilan_cortez "You did what you always do. You give people tools."

    ava_marin "And what happens when those tools are picked up by someone with a ledger instead of a heart?"
    "Ilan Cortez's silence is a kind of answer. He chews the inside of his cheek, the way he did when soldering stubborn circuits. The wind tugs at his longer strands of hair. For a breath he looks lost between gratitude and strategy."

    ilan_cortez "Open-source is a shield and a signal. Shields can be heavy. Signals can be hijacked."
    "You want to argue the ethics of transparency; you want to say that knowledge shared is survival shared. But he presses a small weight into your palm—a brass compass, rimmed with tiny scratches."
    hide ava_marin
    hide ilan_cortez

    scene bg ch5_4001e7_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft clink of metal; a gull's call fades]
    show ilan_cortez at left:
        zoom 0.7

    ilan_cortez "My grandfather gave this to me when I left home. Said a compass won't answer every question, but it helps you find north when everything else spins. Keep it."
    "You look up at him. He swallows, then forces a smile that doesn't reach his eyes."

    ilan_cortez "I believe in the design, Ava. I believe in people. But I'm worried—about leverage, about control. If we give everything away, we might protect some homes today and lose the means to defend them tomorrow."
    "You hold the compass between your fingers like a benediction and like a reproach. The metal is heavier than it looks."

    menu:
        "Scan the first batch of messages for practical tweaks":
            "You tap through messages, saving a neighbor’s improvised bracket and scribbling the measurements into the margins of the schematic."
        "Send a quick voice note to Tomas to ask about spare clamps":
            "You press record, hear Tomas's gravelly laugh in response, and make a mental note to pick up his old toolkit after the tide turns."

    # --- merge ---
    "Ilan Cortez watches you choose, then folds his arms as if bracing himself for whatever the world decides next. Around you, small acts accumulate into a chorus: someone in the next block posts a diagram with"
    "an alternate flange, another sends a video of a hand-made seal that could cut costs in half. Gratitude floods the thread. For a few hours the network looks like the shop again: people trading parts and"
    "stories, sharing meals and diagrams in equal measure."
    "But openness invites more than goodwill."
    # [Scene: Tideward Lanes | Midweek, After Rain]
    hide ilan_cortez

    scene bg ch5_4001e7_4 at full_bg
    # play music "music_placeholder"  # [Music: Low, hollow cello; the tempo slows]
    # play sound "sfx_placeholder"  # [Sound: Notifications pinging like distant bells; a municipal alert tone]
    "Your phone vibrates with a sharper tone—corporate cadence. A slick development firm has posted a polished proposal that lifts images directly from your schematics. Their render shows modular barriers integrated into landscaped promenades, their model dressed"
    "in glass and concierge logos. The caption promises 'resilient neighborhoods'—trade mark, trademark symbol shining like a disclaimer."

    scene bg ch5_4001e7_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The wet rustle of a paper flyer hitting a puddle]

    "You scroll through the comments: investors coo about ROI; a neighborhood watch account posts a cautious, hopeful emoji. Then a new notification—City Hall has reposted the developer's proposal with a curt endorsement. Evelyn Harrow's office tweets a nod" "Public-private collaboration accelerates resilience."
    "You walk to see it for yourself—because seeing makes it real. The civic screens show the same glossy towers you passed earlier in plywood form. Mural faces peer out from the edges, their colors hemorrhaging beside gleaming, sterile interpretations of what Tideward could be."
    "Mira finds you at a crooked stoop, packet of seeds clutched to her chest. Rain has dampened her undercut; smudged soil is at the cuticles of her hands."
    show mira_soto at left:
        zoom 0.7

    mira_soto "They used the image of the fritillary mural. They put it next to a lobby rendering. Ava, my grandmother's stew recipe is in that mural—who will remember why the fritillary was painted if it's just background for a condo brochure?"
    show ava_marin at right:
        zoom 0.7

    ava_marin "They swiped the idea; they didn't steal the memory. We still have the recipe. We have the archive."

    mira_soto "An archive on a server—what's the point when there's nowhere left to keep the pots?"
    "She presses the packet of seeds to her mouth as if tasting a memory. Her shoulders shake; she laughs once, a sound that is close to a sob."

    mira_soto "Everyone's talking about maintenance contracts and who does the billing. Nobody's talking about who gets to cook at the block party, Ava."
    "You reach for her hand. She lets you take it, squeezes too hard, and the seeds tremble against her palm."

    menu:
        "Pull Mira into a hug":
            "You fold her into you; she leaks tears into your jacket, and for two breaths you share a private, messy human thing that no render can replicate."
        "Offer to help catalog the family recipes in your journal":
            "You kneel beside her, open your leather journal to a blank page, and ask her to tell you the recipe—each ingredient becomes a line, each memory a footnote you both can point to later."

    # --- merge ---

    mira_soto "Promise me we won't let them turn stories into investment captions."
    "Ilan Cortez arrives at dusk. He lingers at the edge of the group, watching the exchange with a guarded expression. When he finally speaks, there is an urgency—an engineer's calculus folded in with something like fear."
    show ilan_cortez at center:
        zoom 0.7

    ilan_cortez "They'll build off what we've given them and dress it up. Once it's in a publicly approved plan, the city can allocate funds—funds that will pull leverage toward the firms that have lobbying muscle. Then the narrative changes: your community becomes a pilot program, then a case study, then, if the market says so, property."

    ava_marin "So what's the alternative? Keep everything secret so only the people who know how to weld can benefit? Let neighbors drown because someone didn't trust the rest of the city?"

    ilan_cortez "No. The alternative is to demand governance in tandem with release—protective licenses, community rights, legal covenants that prevent predatory appropriation. Open-source plus legal armor."
    "You think of the municipal rooms you would have to enter—confusing, fluorescent, full of people who read editions of budgets but not the names of the people who live on a block. Your throat tightens thinking of negotiating with clauses and lawyers."

    ava_marin "And who is going to pay for that legal armor, Ilan? Where's that money supposed to come from? We can't stall the tide for litigation."

    ilan_cortez "Maybe we don't have to. Maybe we can ask for funding tied to community governance. But if the plan comes with private maintenance contracts, those contracts will define who gets to keep things repaired."
    "The argument doesn't resolve. It spirals and lands heavy. You can feel the neighborhood—its resilience and its precarity—tilting on an axis you do not control."
    # [Scene: City Hall Promenade | Afternoon]
    hide mira_soto
    hide ava_marin
    hide ilan_cortez

    scene bg ch5_4001e7_6 at full_bg
    # play music "music_placeholder"  # [Music: A single held note on strings; tension under the skin]
    # play sound "sfx_placeholder"  # [Sound: Crowd murmurs; the wind off the bay]

    "You stand near the promenade screens as the municipality's repost scrolls in neat type. Evelyn Harrow" "We must marry the best of innovation and governance to protect our most vulnerable communities."
    "You watch the clip. Her words are a scaffold of civic promise—clear, decisive—but you remember that her decisions once uprooted a different neighborhood. Her face on the screen is impossible to reconcile with the woman whose policies often asked people to carry loss in quiet compliance."
    "You look around. People in suits who would have been at investor briefings shuffle papers; a developer's rep smiles at a reporter. Some neighbors, seeing the promise of municipal funding on the screens, exchange hopeful looks. Others—older, salt-scarred—stare at the renderings as if they were tombstones in progress."
    "Ilan Cortez stands beside you, but a small distance opens between you both—an emotional gap you can't stitch with schematics."
    show ilan_cortez at left:
        zoom 0.7

    ilan_cortez "We might have protected a roof or two. But now the narrative has a new author. We handed them a chapter."
    show ava_marin at right:
        zoom 0.7

    ava_marin "We tried to protect people. We wanted to make it impossible for them to say 'we don't know how'—to give them the tools to survive."

    ilan_cortez "And you did. Which is exactly why they're using it."
    "He sounds almost accusatory, and you flinch, because you can hear how right he is. The iron taste of regret surfaces—salty and cold. You think of the leather journal at home: the pages where you have"
    "written names and routes and the smell of frying fish at Mr. Ramierez's stall. You think of how small entries could be reduced to attachments in a redevelopment dossier."
    "You walk the lanes that evening, past murals that strain beneath new layers of advertisement. A child's face in paint—your neighbor's granddaughter—stares from a wall beside an image of a slick lobby. The contrast hurts the eyes."
    "You wonder, not for the first time, whether your stubbornness has been a kind of betrayal. You promised to keep memory alive; now memory is at risk of being repackaged into commodified nostalgia."
    "You open your journal. The pages rattle in the wind like loose tides. You flip to where you transcribed the postman’s route; the ink has begun to feather from the damp. You could photograph it, upload"
    "it, tie it to the open schematics as cultural metadata—but metadata can be cleanly separated from habitation. A photo is not a kitchen. A file is not a neighborhood."
    hide ilan_cortez
    hide ava_marin

    scene bg ch5_4001e7_7 at full_bg
    # play music "music_placeholder"  # [Music: A low, descending chord]
    "Ilan Cortez takes a step away and then stops. He looks back over his shoulder at you as if considering permission."
    show ilan_cortez at left:
        zoom 0.7

    ilan_cortez "I don't know if we did the right thing."
    show ava_marin at right:
        zoom 0.7

    ava_marin "Neither do I."
    "He presses his hand against the compass at your side as if checking that the needle still points."

    ilan_cortez "But I still think there are things we can do—legal armor, covenants, community trusts. We can try to pull the language back."
    "You close the journal with a deliberate motion. The thought of conferences, filings, municipal meetings fills you with a weary nausea. You are tired of fighting with pen and patience in rooms that smell like lemon disinfectant."
    "Mira finds you again at dusk, eyes rimmed red. She presses a seed packet into your palm."
    show mira_soto at center:
        zoom 0.7

    mira_soto "Whatever happens, don't let them make our stories into a marketing angle. Keep them messy. Keep them human."

    ava_marin "I will. I promise. But I—"
    "Words fall useless. You have promised before; promises have been broken by storms and by profit margins."
    "You stand at the mouth of Tideward as the sky goes the dark, not storm-bell dark but the sort of heavy that says weather is only a pretext for something larger. Above, a billboard on the"
    "edge of the new development site cycles through a glossy animation of the modular barrier glinting in simulated sunlight. Below, the gutters carry away bits of confetti from last weekend's block party—the same confetti that someone"
    "will someday pitch as 'cultural texture' in a brochure."
    "Your jaw aches from clenching. Salt air fills your mouth."
    "You taste brine and regret."
    hide ilan_cortez
    hide ava_marin
    hide mira_soto

    scene bg ch5_4001e7_8 at full_bg
    # play music "music_placeholder"  # [Music: A small, unresolved chord]
    "You are at a crossroads that does not feel like a fork on a path but a decision about how to name the shape of your neighborhood's future. Legal protections? Public denunciations? Scraping the files offline"
    "and reclaiming the work under an enforceable covenant? Or leaning into the opening and trying to steer the public momentum toward real governance mechanisms before the market locks them out?"
    "The answers feel like weather patterns—predictable in the abstract, impossible to control up close."
    "You rub your thumb along the rim of the compass in your pocket. The needle might not save anything, but its presence tethers you to a direction: not peace, not victory, but north—a line to follow when the map is otherwise blank."
    "You can see the faces of those who trusted you—Mira with her seeds, Tomas with his spare clamps, the neighbors who sent late-night videos of welding. You also see the glossy renderings and the City Hall slideshow and Evelyn Harrow's steady cadence praising 'market adoption.'"
    "Your stubbornness turns inward. Did you betray the neighborhood by trusting transparency? Or did you betray it by trying something that might have protected roofs at the cost of story?"
    "The tide is not just water; it is interest, momentum, money. It moves through digital channels as much as through gutters."
    "You stand at the edge of the boardwalk, the city's lights reflecting back like questions."
    # play music "music_placeholder"  # [Music: The cello drops to a single, held note that fades into the sound of the sea]
    "You inhale. You exhale. A decision presses up, bright and sharp as a coin, waiting to be spent."

    scene bg ch5_4001e7_9 at full_bg
    "THE END"
    # [GAME END]
    return
