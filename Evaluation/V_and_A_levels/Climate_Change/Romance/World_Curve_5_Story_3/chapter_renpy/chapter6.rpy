label chapter6:

    # [Scene: Greenline Reclamation Hub | Early Morning — Weeks Later]

    scene bg ch6_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A layered cacophony — hammers striking, a radio caller counting out loads, children's laughter as they plant, a diesel pump sighing in the distance]
    # play music "music_placeholder"  # [Music: Fast-paced, driving strings underscoring an urgent, optimistic tempo]
    "You wake to the taste of salt and sawdust under your tongue. The weeks since the meeting have condensed into a single relentless motion: plan, lift, shore, stitch. It is not a blur because it lacks meaning; it is because every minute contains meaning so dense it presses time thin."
    "Your jacket is still speckled with mud. The notebook is thicker at the spine from new notes and smudged sample labels. Elias Rowe appears at the edge of sight, sleeves rolled, hair catching the sun in"
    "a way that interrupts your focus. For a second your chest forgets the list and remembers the small geography of him — the angle of his jaw as he measures a board, the way his brows"
    "knit when a plan needs adjusting."
    "Lina Park sweeps past with a wheelbarrow, shouting a cadence of names and tasks like a conductor. Tomas Reyes stands near a tide-mark post, hands on his hips as he reads the old lines like braille."
    "Mayor Amara moves between Serena Voss's team and the volunteer crews with a clipboard and a face practiced in weighing two heavy things at once."
    "You breathe them all in: diesel, wet earth, the metallic tang of seawater that seems to coat everything in a thin, honest edge."
    show lina_park at left:
        zoom 0.7

    lina_park "Maya—adjust the northern berm, we have a scouring pocket near Post C. Elias, can you lead the kids on the boardwalk planting? They're raring to help."
    show maya_calder at right:
        zoom 0.7

    maya_calder "I'll pull the sediment maps and—' (you flip open the Moleskine, fingers leaving dark prints on the page) '—double the compaction runs. Tomas, can you show the high-tide line to the new volunteers?"

    "Tomas Reyes" "Been marking tides longer than you've had that compass. But yeah — I'll take the north watch."
    "The plan unfurls in quick, tacit agreement. Words are brief because the work is loud and because every minute spent talking is a minute you are not holding a plank in place while the tide pulls."
    hide lina_park
    hide maya_calder

    scene bg ch6_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Nails biting into wood; a child's small gasp when a sprout lodges in the sand]
    # play music "music_placeholder"  # [Music: Percussion snaps, accelerating — the drive of construction and of people refusing to be flattened by the shore]
    "Elias Rowe slides a board under your instruction, the muscles along his arm flexing in a way that reads safety as much as skill. He doesn't say it out loud, but his presence answers a thread"
    "of your own stubbornness: you do not have to be the one who carries everything alone."
    show elias_rowe at left:
        zoom 0.7

    elias_rowe "You look like you haven't slept. We can rotate you out after the next haul."
    show maya_calder at right:
        zoom 0.7

    maya_calder "I'm fine.' (it sounds clipped even to you) 'There's a scour you can't see from the surface. I need to check the core samples before the next tide."

    elias_rowe "Then bring someone who can carry a shovel and your stubbornness. Preferably heavier on the shovel."
    "He grins. You let the grin in; the grin, like the work, is a small, necessary shelter."

    menu:
        "Grab the extra spade and head down to the scour":
            "You shoulder the spade like armor and go. The wind bites at your ears but the spade bites the sand in return; cyan spray flecks your cheek as you dig."
        "Return to the map table to coordinate compaction runs":
            "You stay, voice steady, calling out timetables and teams. Volunteers funnel toward you, trusting the plan you're sketching in your palm."

    # --- merge ---
    # [Scene: Greenline Reclamation Hub | Noon]
    hide elias_rowe
    hide maya_calder

    scene bg ch6_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hum of a portable generator, the murmur of negotiations under the working noise]
    # play music "music_placeholder"  # [Music: Staccato brass, building tension that resolves into collaborative cadence]
    show mayor_amara_sol at left:
        zoom 0.7

    mayor_amara_sol "We will set up the trust as jointly managed. Serena, you'll fund specified reinforcement phases. Maya and Lina will approve community oversight measures."
    show serena_voss at right:
        zoom 0.7

    serena_voss "Agreed, with the condition that our emergency reinforcement window remains flexible. We need to protect critical infrastructure promptly."
    "You feel the clause like a stone in your palm — necessary, cold, and something you'll pick at later until its edges are dull. The trade-offs hum in the air: speed versus sovereignty, funding versus strings."
    "The compromise is messy because the problem is messy. The mayor's solution is a scaffold holding hands across a crack."
    show maya_calder at center:
        zoom 0.7

    maya_calder "Oversight is not symbolic,' you say. 'There will be an independent review board. Community representatives must have veto on relocation decisions that affect households."

    serena_voss "I know the weight of transparency. It's heavier than it looks. But you're right — public access helps trust the process."
    "The exchange spins in multiple turns: you ask for community seats, Serena demands accountability metrics, Amara knits both into the municipal ledger. Each retort is terse, layered; each concession both gains and eats away at something. The dialogue has the friction of two axes grinding to form a tool."
    # play sound "sfx_placeholder"  # [Sound: A child nearby shrieks with delight at a small fish found in a tide pool; the sound is a bright counterpoint to the corporate ledger talk]
    # play music "music_placeholder"  # [Music: Strings swell — urgency with an undertone of something like relief]
    hide mayor_amara_sol
    show lina_park at left:
        zoom 0.7

    lina_park "We can staff the review board with grad students and locals. We can keep the data public. Maya, you hold the archive."

    maya_calder "Professor Miyazaki's dataset will be part of the archive. Transparency matters."

    serena_voss "I know the weight of transparency. It's heavier than it looks. But you're right — public access helps trust the process."
    "Her eyes flick to Maya Calder in a way that is complex: not simply adversarial, not simply ally. It is not the look of a person aligned entirely with you, but of one recognizing a seam in her own armor."

    menu:
        "Press now for stronger community veto power":
            "You press, palms flat on the weathered table. The mayor studies you, then taps a pen. The board members shift; some mouths open in protest, but the final nod comes through."
        "Accept the skeleton oversight for now, reserve fights for clause language later":
            "You swallow the urge to sharpen every line. The mayor shakes your hand. The victory feels lopsided but practical. You tuck the complaint into the Moleskine to burn at a later hour."

    # --- merge ---
    # [Scene: Community Meadow (Rooftop Garden) | Late Afternoon — Finalizing the Trust]
    hide serena_voss
    hide maya_calder
    hide lina_park

    scene bg ch6_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Bees, distant gulls, the soft clink of a thermos lid]
    # play music "music_placeholder"  # [Music: A warm, sustaining chord that opens into full-major, triumphant but intimate]
    "The trust is written in the margins of a hundred conversations. Children paint a banner that will hang on the boardwalk; carpenters sign up for weekend shifts; a retired accountant agrees to sit on the review"
    "board. The joint fund will cover immediate reinforcement and the living shoreline expansion. The words on paper feel thin compared to the bodies who will carry them into weather."
    show mayor_amara_sol at left:
        zoom 0.7

    mayor_amara_sol "We will schedule quarterly reports and a community audit. The town keeps veto for any relocation that affects single-family households."
    show serena_voss at right:
        zoom 0.7

    serena_voss "We will accelerate phase one funding upon the town's approval of the oversight terms. Our engineers will work alongside volunteers."
    show lina_park at center:
        zoom 0.7

    lina_park "This is it. This is our stitch."

    "Tomas Reyes" "Stitching is what we've done for generations. Not big machines. Hands."
    "You watch the ribbon of people — hands, faces, elbows and laughter — and feel the arc of tension bend toward something that looks like relief. The compromise is imperfect, threaded with clauses that will haunt"
    "you at midnight. But the immediate tide line has been held back. Houses that would have lost rooms now have roofs. People sleep without the same taut fear."

    "Maya Calder (to Elias, quietly)" "We did it. Not perfectly. But — we held the line."
    hide mayor_amara_sol
    show elias_rowe at left:
        zoom 0.7

    elias_rowe "We held it together. You held it."
    "His hand finds yours briefly as he passes a tray of coffee. It's a touch that is not a promise yet, but it is an offering."
    # [Scene: Old Pier | Dusk]
    hide serena_voss
    hide lina_park
    hide elias_rowe

    scene bg ch6_601bcb_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft waves, a gull's call, distant clatter as crews secure lines for night]
    # play music "music_placeholder"  # [Music: A swell of cello and piano — deep, intimate, sweeping; tempo peaks here]
    "You sit with Elias Rowe at the edge of the pier. The thermos between you steams in the cool of coming night. The day’s work unravels from your shoulders like a cloak you can finally set down for a moment."
    "He turns a small, mud-streaked hand over a sprig of cordgrass he just planted and then tucks it back. His sketches are gone for the day; his sketchbook is closed but heavy with decisions. He looks"
    "at you like someone who has watched storms and chosen to stand in the doorway."
    show elias_rowe at left:
        zoom 0.7

    elias_rowe "You kept coming back. Even the nights. I—' (he stops, hunts for a phrase) '—I didn't think you'd let it be a town-only thing. I thought you'd... disappear into research."
    show maya_calder at right:
        zoom 0.7

    maya_calder "I almost did. But there are faces here I owe the work to. And there are faces here I didn't want to lose."

    elias_rowe "Good. Because—' (he searches, then offers) '—I don't know how to promise a lot of things, Maya. But I know how to be here."
    "You feel everything accelerate: the day that seemed long now rushes into that single, concentrated moment. The work's exhaustion sharpens into clarity. Your arousal — the VeryHigh rhythm you've carried through weeks of labor — crests"
    "into something immediate, breathless: hope braided with the electric risk of saying the true thing."
    "You take the compass from your jacket. The brass is warm against your palm from the sun, dented at the rim where a childhood fall had once bent it. You remember your father’s hand placing it in your chest years before; you remember the promise in that gesture."

    maya_calder "I—' (the words are small) '—this helped me find the lines when I forgot which way was safe."

    elias_rowe "Maya—"
    "You place the compass in his palm. His fingers close around it for a heartbeat. Then he protests, a laugh like a short, surprised exhale."

    elias_rowe "You can't just hand over relics and expect me not to steal them."

    maya_calder "Maybe I'm asking you to hold it for a moment. Not steal."
    "He looks down at the compass, then up at you. For a breath there is a silence full of the salt wind and the clatter of the world being rebuilt behind you."

    elias_rowe "I'll put it back where it belongs."
    "You watch him laugh and then carefully slide the compass back into the pocket near your sternum, as if returning a talisman to its rightful owner affirms not possession but mutual care. His smile widens, not incapable of gravity but anchored to something like relief."

    elias_rowe "Not perfect,' he says. 'Not ever. But work — hot and honest — and possible."

    maya_calder "And together."
    "He reaches for your hand again, this time to hold it, the world around you reducing to the warmth of his palm and the steady press of the pier beneath you."
    hide elias_rowe
    hide maya_calder

    scene bg ch6_601bcb_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The tide sighs; the town murmurs; a distant laugh cuts cleanly like a bell]
    # play music "music_placeholder"  # [Music: Climactic chord — high, sustaining, then resolves into a gentle, assured cadence]
    "You let the moment expand until it fills you. Hope is not the absence of fear; it is the choice to act despite it. Tonight, the town breathes. Tonight, you let someone else hold part of the map."
    "The compromise will need tending. Contracts will gnaw at your sleep. Serena Voss's clauses will need loopholes bluntly filed down. But the immediate scouring is repaired. Homes stand. People will mend their lives around the new edges of the shore."
    "Elias Rowe turns his face toward you, amber eyes reflecting a sky that has been scraped clean by work and wind. He does not promise forever in words; he promises presence in gestures — in shared"
    "coffee, in steady help, in returning the compass to its place on your chest rather than keeping it as a trophy. In his way, that is enough for tonight."
    # play music "music_placeholder"  # [Music: Fade to a single sustained chord that lingers like a vow]

    scene bg ch6_601bcb_7 at full_bg

    scene bg ch6_601bcb_8 at full_bg
    "THE END"
    # [GAME END]
    return
