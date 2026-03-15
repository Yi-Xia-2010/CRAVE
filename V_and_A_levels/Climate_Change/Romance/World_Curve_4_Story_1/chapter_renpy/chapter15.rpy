label chapter15:

    # [Scene: Municipal Hall | Morning — Day after the Release]

    scene bg ch15_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: News vans idling outside; murmurs and the scrape of chairs]
    # play music "music_placeholder"  # [Music: Tense, urgent percussion under a high, sustained violin]
    "You wake to the sound of other people’s alarms. Your phone is a small, insistent animal of notifications: journalists, a lawyer's curt message, Lina's terse line asking where to meet. You have the echo of the"
    "public upload in your chest — the click that set a town into motion — and the hollow, immediate recoil: contracts frozen, contractors pulling their crews, funders calling their counsel."
    "You stand in the hall where the vote would have been held, and the air tastes like rust and wet paper. The appendix you put on the lectern last night is a rumor now — something"
    "everyone has read and argued over — and the practical protections that were meant to accompany it have been auctioned off to legal risk. The seawall tenderers called their vans back. Heavy equipment idles on the"
    "highway like animals waiting to be led away."

    scene bg ch15_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Mayor Tomas's voice, low and frayed, in the doorway]
    show mayor_tomas_greer at left:
        zoom 0.7

    mayor_tomas_greer "I don't have the staff to handle suit filings and sandbagging at once, Maya. We are stretched thin. This—this public thing—it's good for accountability, but it's costing us boots on the ground."
    "You want to tell him the ledger of moral duty outweighs short-term scaffolding, but his jaw is already clenched around a calculus you can't delete: people need walls now, not arguments. The words snag at you"
    "— you went public because secrecy felt like betrayal. But secrecy had promised speed. Truth promised honesty. Honesty cost you the contractors."
    "Lina Park leans in, voice raw with suppressed steam."
    show lina_park at right:
        zoom 0.7

    lina_park "We pushed for transparency because people deserve to know who profits off their safety. We knew it would shake things up—but not like this. Not when the forecasts say four days of storm."
    show maya_soler at center:
        zoom 0.7

    maya_soler "I know. I know what it cost."
    "Your fingers find the braided rope bracelet at your wrist; small comfort. 'We can't rewind it. We have to triage — people, supplies, the Flats. Noah and Arin can help on the boats. Rita needs a place dry tonight.'"
    "Noah Reyes appears at the doorway, rain tattooing his cap. He runs in like a man carrying every last teetering concern of the harbor."
    hide mayor_tomas_greer
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "Tomas wants a list — who's salvageable, who's prioritized. Contractors left at dawn. A few of the bigger crews already turned around. Boats still on the water if we need them, but it's thin. Gavin from the mechanist's yard said he can lend us ropes, but—"

    noah_reyes "—but not enough."
    hide lina_park
    hide maya_soler
    hide noah_reyes

    scene bg ch15_f99e88_3 at full_bg
    # play music "music_placeholder"  # [Music: Drum beats quicken]

    menu:
        "Stay here to coordinate emergency logistics":
            "You spread the town map across the table and bark orders—straw bales, a crew to Rita's, volunteers to the school gym."
        "Go out to the Flats to see what we can still save":
            "You grab your jacket and rush for the door; the marsh will tell you what the numbers couldn't."

    # --- merge ---
    "Continue to the Main Street — Afternoon (Storm Building) scene"
    # [Scene: Main Street — Afternoon (Storm Building)]

    scene bg ch15_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind threading itself through alleyways; the distant wail of a siren]
    # play music "music_placeholder"  # [Music: Fractured strings, a pounding electronic undercurrent]
    "You choose — not that choice absolves you of the other — and you move. The town is lit by phones and lanterns, but momentum has thinned. Where bulldozers should have been stacking jersey barriers, there"
    "are volunteers with sandbags and tremulous smiles. The seawall's half-formed concrete eyebrow gapes at the sea like a promise interrupted."
    "Evelyn Hart arrives without preamble, coat whipped with spray. She's not the same steel-boned official you sparred with in public; her face is exhausted, the set of someone who can still marshal a brief but cannot do the impossible. Her tablet is dark in her hands."
    show evelyn_hart at left:
        zoom 0.7

    evelyn_hart "Investors pulled after the press. I tried to hold them — there were clauses, contingencies — but once the audits started, the money froze. It was never malicious, Maya. It was procedural panic."
    show maya_soler at right:
        zoom 0.7

    maya_soler "Procedural panic leaves people in the dark when the sea comes."

    evelyn_hart "I never wanted contractors to leave. I fought to keep crews on standby. I —"

    evelyn_hart "We are both responsible here in different ways."
    show noah_reyes at center:
        zoom 0.7

    noah_reyes "Responsibility doesn't plug a hole in a roof."
    "The wind slices a wooden sign loose and it thwacks across the street. A volunteer curses and chases it, the sound lost in gusts. You feel fevered, your decisions folding into more decisions like sheets into"
    "a storm: contact the tow crews, check on Rita, make sure the evacuation points run, get Arin where he needs to be."
    "Arin Kai finds you near the pier — his hair a dark crown flattened by rain, jacket unbuttoned against the damp. His eyes are quick and furious; he is a man used to risk, and now he steels himself for it."
    hide evelyn_hart
    show arin_kai at left:
        zoom 0.7

    arin_kai "You shouldn't have made it public, Maya."

    arin_kai "We needed the crews."

    maya_soler "We needed people to know the truth. We needed oversight. If data hides who profits from danger, that’s not protection."

    arin_kai "I get the why. But I also get the who needs a dry bed tonight. We can't negotiate with waves. We need boats, we need rope, we need time."

    maya_soler "Then we make time. We use what’s left."

    arin_kai "I'll do whatever it takes. But not without you."
    # play music "music_placeholder"  # [Music: Spike; weather instruments clang]
    "You want to answer him with certainty, but the town is a ledger of past losses and present danger. Your mouth forms a promise you are not sure you can keep."

    menu:
        "Take Arin's offer and go on rescue runs with him":
            "You squeeze his forearm and nod; adrenaline steadies your hands as you climb into a small skiff."
        "Stay onshore, coordinate from the pier":
            "You plant yourself on the pier and start directing radios, your voice a thin thread through the storm's roar."

    # --- merge ---
    "Proceed to The Flats Marsh | Night — Storm Peak"
    # [Scene: The Flats Marsh | Night — Storm Peak]
    hide maya_soler
    hide noah_reyes
    hide arin_kai

    scene bg ch15_f99e88_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Waves battering, trees snapping, the metallic groan of torn signage; people's shouts parried by wind]
    # play music "music_placeholder"  # [Music: Chaotic percussion and dissonant brass; a single, keening violin rises above the storm]
    "You chose your place. The sea is a machine with a mind you had never asked for, and it is doing what it knows: it pushes and pulls, scours and takes. The Flats hold no mercy."
    "The shallow channels that once reflected sky now sweep away fences, picnic tables, small boats, the careful stakes of your restoration plots."
    "You smell oil, salt, wet wood, the metallic tang of dislocated things. Touch is of cold rain against your collar and the slickness of mud on your boots. Every sound is muffled and immediate: a child's"
    "cry choked off by wind, the slap of a loose tarp, the wrench of timber."
    "Arin Kai is at the bow of a small vessel, calling out orders. There is a headlamp cut into the wet dark and the white of his teeth as he barks a direction."
    show arin_kai at left:
        zoom 0.7

    arin_kai "Hold the line! Brace!"
    show noah_reyes at right:
        zoom 0.7

    noah_reyes "Maya! Get that woman tied to the mast!"

    noah_reyes "Arin, the eddy—"
    "Water takes a man-sized shadow and throws it like a rag. Noah is at a rail, reaching for a woman in kelp-dark water. His hand slips. You see it the way one sees a sunlit something drop: too slow and too quick at once."
    "You dive because there is nothing between you and that sudden losing. You dive with science-trained muscles and memory hands that know where the soft pockets in tidal flow should be. Your fingers find a flailing"
    "sleeve; salt water fills your nose like static. Noise becomes a thin, distant thing. You pull and you don't know which of you is acting — expertise or instinct."
    "A curve of wood smashes into the hull. The skiff groans. The rescue becomes immediate salvage: bodies, ropes, the scream of a seam ripping. Arin Kai's voice cuts through, close and terrified and furious all at once."

    arin_kai "Maya! Hold on to the rope!"

    "You" "Noah!"
    "You reach; the rope screams through your hands."

    arin_kai "Get the woman! Get her into the skiff!"

    arin_kai "We had him. We had him and—"
    "There is a rip of timber. A winch gives. A mooring line parts. Noah goes under."
    "You feel the world rearrange around that absence — the way a room changes when a person leaves. Rescue becomes triage. Arin wrestles a broken net and a sob breaks out of him like a sound he has never allowed himself."

    arin_kai "We had him. We had him and—"

    arin_kai "We couldn't pull him back."
    # play sound "sfx_placeholder"  # [Sound: A child's scream is swallowed by wind; distant, a church bell chimes oddly in the storm]
    show evelyn_hart at center:
        zoom 0.7

    evelyn_hart "Where's the medical team? Where's the emergency response?"
    hide arin_kai
    show maya_soler at left:
        zoom 0.7

    maya_soler "They're stretched. We need a channel cleared to the pier. We need every working vessel—"
    hide noah_reyes
    hide evelyn_hart
    hide maya_soler

    scene bg ch15_f99e88_6 at full_bg
    # play music "music_placeholder"  # [Music: A single violin note held, then broken]
    # [Scene: Harbor / Fisherman's Pier | Dawn — After the Surge]

    scene bg ch15_f99e88_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low moans, generators coughing, gulls sounding like new alarm bells]
    # play music "music_placeholder"  # [Music: Searing, elegiac strings; a slow timpani like a heartbeat losing step]
    "When the storm finally relents, it does not come gently. It pares the town down to what can be seen at first light: broken boats, sodden furniture, the blackened ribs of a pier. The Flats are"
    "a channel of churned mud; where saltmarsh had hummed with small life, the ground is a raw, open scrape."
    "You walk the pier like a foreigner in your own memory. Rita's small house — the one with the floral scarf line that fluttered in many festivals — lies half-collapsed where the water took the garden"
    "and its stories. She sits on a crate, wrapped in a borrowed blanket, knuckles white around a cup of coffee gone cold. Her eyes are the way they always were: warm, and now, stunned."
    show rita_soler at left:
        zoom 0.7

    rita_soler "We told them the marsh remembers… it remembers who took care of it and who didn't."

    rita_soler "Did you do right, niña?"
    show maya_soler at right:
        zoom 0.7

    maya_soler "I told the truth. I thought the truth would protect us in the long run."

    rita_soler "Truth doesn't stop a storm."
    "You cannot answer that with comfort. You can only stand and let the wet cold find you and learn what the town has lost by being honest and by being exposed at the same time. You"
    "walk further and discover Arin among the flotsam, his boat a split carcass of wood, the brass of his father's compass pendant half-dulled by sand. He has blood on his knuckles. He does not look at"
    "you at first."
    show arin_kai at center:
        zoom 0.7

    arin_kai "We saved what we could. We couldn't save Noah."
    "You feel the world tilt into a new geometry: a life gone, a cost irrevocable. Arin's face is open with exhaustion and a kind of accusation that isn't toward you but toward the system that forced the choice."

    maya_soler "We did what we had to."

    arin_kai "Did we?"
    "He wants something from you — a tether, an answer that will make the future less heavy. You realize that some debts cannot be repaid with policy or protest. Some debts are paid in ash and"
    "in wet wood and in the small, private reckonings at the edge of the sea."
    hide rita_soler
    hide maya_soler
    hide arin_kai

    scene bg ch15_f99e88_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slow drip of stormwater from broken beams]
    # play music "music_placeholder"  # [Music: Sparse piano, one note to hold a breath]
    show mayor_tomas_greer at left:
        zoom 0.7

    mayor_tomas_greer "We will rebuild. There will be funding requests, there will be hearings. We will need each other's hands."

    mayor_tomas_greer "But there's no denying the cost of this week."
    "Evelyn Hart stands a few paces away, hands clasped at her back, not meeting anyone's eyes. The investigation into her proposals will continue; subpoenas will be filed. You imagine the legal hearings as a long, cold"
    "thing that will fold into years. The contractors will not return in the same way. The town's defenses that were partly built will remain incomplete, pitted with the shapes of what could have been."
    show lina_park at right:
        zoom 0.7

    lina_park "We blew the cover on who was making money off risk. People needed to know. But truth wasn't armor. It was a mirror, and mirrors don't stop water."
    "You stand in that mirror and see your face — tired, salt-crusted, resolute and ruined at once. The romance you and Arin had spent seasons constructing is now a fragile raft among the wreckage: he saved"
    "lives; you exposed a ledger. The gulf between ethics and immediate survival yawns like a channel. You are both there, and yet distance has a new geography: grief."
    show arin_kai at center:
        zoom 0.7

    arin_kai "I don't know if we can fix what we broke. But I know I can't ask you to feel less for what you did. The man we lost — Noah — he was my friend. He was your friend. There is no argument that brings him back."
    hide mayor_tomas_greer
    show maya_soler at left:
        zoom 0.7

    maya_soler "There isn't. But I cannot let the loss be for nothing."

    arin_kai "What if the cost of nothing was this? What if truth itself was cruel without protection?"
    "You press your thumb against his knuckles, and for a second the simple contact is an argument and a solace both. You are not absolved. You are not forgiven. You are not finished. The town will"
    "need both accountability and immediate, blunt protection — and it will have to learn how to make room for both without killing itself in the attempt."
    hide lina_park
    hide arin_kai
    hide maya_soler

    scene bg ch15_f99e88_9 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A gull's harsh cry, a generator's stuttering growl, the far-off murmur of people cataloging loss]
    # play music "music_placeholder"  # [Music: A low cello — a slow, aching bow]
    "You pick up your Moleskine. The pages are streaked with rain and fingerprints, but the notes are there, precise and small: transects, species counts, the appendix that began this cascade. You turn to a blank page and, with a shaking hand, write one sentence:"
    "'This is what happened.'"
    "Words are small next to the sea. But they are all you and your town will have to hold the story together. To keep memory alive. To argue for a different future even when the present has been so grievously taken from you."
    "You look at Arin once more. He looks back, the set of his shoulders telling you that love will now be a thing hammered out in the aftermath — not a refuge against loss but a"
    "labor performed in grief. You cannot promise him the future you once imagined. You cannot promise yourself it will be redeemed."
    "You fold the Moleskine closed. The hairpin digs into your palm. You breathe in the salt air and let the sound of the town cataloging its losses fold into a long, bitter, necessary silence."

    scene bg ch15_f99e88_10 at full_bg
    "THE END"
    # [GAME END]
    return
