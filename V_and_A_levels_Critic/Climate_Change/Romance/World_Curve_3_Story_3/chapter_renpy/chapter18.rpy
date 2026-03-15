label chapter18:

    # [Scene: Rooftop Garden of Maia's Childhood House | Late Afternoon — the sky a dull mauve after a long day]
    # play music "music_placeholder"  # [Music: Taut strings—urgent, then a quick, hopeful swell]

    scene bg ch15_5195df_1 at full_bg
    "You stand with your palm flattened against the cool, corrugated metal of the roof, the same hand that kept the Moleskine zipped tight through the meeting. Your braiding bracelet rubs against your wrist like a small,"
    "familiar chastisement. The memory of the hall—the cameras, Jonah Kade's unreadable face—presses against the back of your eyelids. You can still hear the rhythm of the pumps beneath everything, a machine heartbeat that will not stop."
    "Guilt sits in your throat, heavy and warm as soup. It has the shape of signatures and promises; it smells like wet boardwalks and burnt paint. You accepted responsibility publicly. You stood at the microphone and"
    "let the town's anger and need find you. You did not step away. That choice—raw, exposed—has a cost. It is also the pivot point from which you push everything forward."
    # play sound "sfx_placeholder"  # [Sound: A distant call to a community meeting—megaphone muffled by fog]

    scene bg ch15_5195df_2 at full_bg
    "You breathe. The rooftop wind slices the residue of ash from the evening's burn. In the space between breaths, you inventory what must happen: supplies, the fund Lupe promised to spin up, Tomas' memorial, the long"
    "slow work of seedlings and nets and new ledgers. There is no neat forgiveness waiting—only the work that might, over seasons, make a different kind of debt."

    menu:
        "Call Jonah now and risk raw words":
            "You thumb the contact; your finger hesitates before dialing. When Jonah answers, his voice is a low tide—reserved, guarded. You say what you must; he listens with the silence of someone measuring distance. He doesn't refuse outright. He asks for time. You feel the small, stinging pull of being held at arm's length."
        "Head down to the Community Center to organize the soup line":
            "You shove your hands into your pockets and head for the stairs, boots clapping hollowly. By the time you reach the gym, volunteers are corralling kettles and bowls; Lupe is already there, ledger open, a flare of relief in her grin. There is immediate, practical work to do, and the rush steadies you."

    # --- merge ---
    "The strings swell into a brisk, driving motif—very high intensity"
    "Transition as you descend the ladder; the city winds around you like a map of stakes and faces"
    # play music "music_placeholder"  # [Music: The strings swell into a brisk, driving motif—very high intensity]

    scene bg ch15_5195df_3 at full_bg
    # [Scene: Community Center (Town Hall) | Evening — fluorescent lights buzzing]
    # play sound "sfx_placeholder"  # [Sound: Clatter of pots, low conversation, paper rustling]

    scene bg ch15_5195df_4 at full_bg
    show lupe_kade at left:
        zoom 0.7

    lupe_kade "You did what you had to, Maia. That—"
    "She gestures at the chalkboard where she's sketched the fund's initial entries."

    lupe_kade "—can't be undone, but we can make it mean something."
    "You: (You set a ladle into a steaming pot, feeling the heat on your forearm. Action steadies you—work is a kind of prayer.)"
    show maia_rivera at right:
        zoom 0.7

    maia_rivera "Meaning isn't the same as repair. But it can be the start."
    "She leans in, voice quick and practical."

    lupe_kade "We can make a town-managed fund. Small contributions, matching grants, transparent books. People will give—if they can trust where the money goes. If you lead it, they'll follow you through the hard parts. They'll drag you into hearings and tribunals and still show up with blankets."

    "The two of you fall into a rhythm—counting, balancing, delegating. Words slide between you that are not speeches" "audit this donation,' 'recording volunteers' hours,' 'no backroom agreements."
    show tomas_rivera at center:
        zoom 0.7

    tomas_rivera "They asked me to help with the memorial. Said I knew the boathouse stories. I told them a story once, and they asked for it again."
    "You: (You want to tell him everything—that you heard the crowd, that you felt Jonah Kade's distance like wind—but you fold it into something smaller.)"

    maia_rivera "We need you, Tomas. The memorial should be honest. Not a eulogy for what was lost, but a ledger of what we choose to keep."
    "Tomas: (He nods, eyes wet but resolute.) 'Then we'll sing the names of what matters, not only the things washed away.'"

    menu:
        "Write the memorial speech with Tomas":
            "You take Tomas' notebook; together you sift through a lifetime of small details—nets, coffee cups, the exact way the boathouse door used to squeak. The words you draft tremble with grief but find a line toward hope."
        "Let Tomas lead the memorial and prepare the logistics":
            "You step back and arrange the candles, the benches, the food runs. Letting him guide the memory feels like admitting you can't hold everything at once; it gives the town the dignity of its own voice."

    # --- merge ---
    "The two of you fall into a rhythm—counting, balancing, delegating."
    # [Music: A drumbeat begins—soft, then building into a communal cadence
    hide lupe_kade
    hide maia_rivera
    hide tomas_rivera

    scene bg ch15_5195df_5 at full_bg
    # play music "music_placeholder"  # [Music: A drumbeat begins—soft, then building into a communal cadence]

    scene bg ch15_5195df_6 at full_bg
    # [Scene: Flooded Historic Quarter | Night — Memorial Service]
    # play sound "sfx_placeholder"  # [Sound: Wind, the hush of a crowd, a single old guitar tuning under breath]

    scene bg ch15_5195df_7 at full_bg
    "You stand before the crowd, Tomas at your side, Lupe tending to the ledger table. The memorial is a crucible—memory, anger, gratitude, and the raw, animal ache of missing things. The town has come because something about shared loss draws people into the same small, fierce orbit."
    "Tomas: (Voice raised in the honest tone of someone who has seen storms before) 'We are not only what the water took. We are the hands that will lift one another when it comes again.'"
    show ava_kim at left:
        zoom 0.7

    ava_kim "We plant. We teach. We'll make room for fish and marsh and people."
    "Dana: (hands shadowed around a candle) 'And we hold the contracts and the companies up to the sun. We keep our eyes open.'"
    "There is singing—not for show, but because voices in a circle steady trembling bones. Someone begins an old fisherman's hymn, and it catches. The sound is immediate and fierce, the kind that presses air out of"
    "your chest. For a moment you are not the architect or the accused—you are simply part of the living thing that insists on naming itself."
    # play music "music_placeholder"  # [Music: Choir-like voices swell into a cathartic peak—very high intensity]
    hide ava_kim

    scene bg ch15_5195df_8 at full_bg
    "You feel the crowd's energy like a wave hitting your ribs. People call out names—of houses, of boats, of people. Tomas tells the oldest story of the boathouse: a child who carved a small compass into"
    "a beam to keep the family true. You can see the compass stitch itself into the town's memory."
    "After the song, someone shouts for volunteers to help clear debris, to distribute blankets, to form work parties. The rush is immediate: people stepping forward without waiting for instruction. It is an ugly, beautiful, furious thing—grief"
    "turned into labor. You move with them, hands blistered and callused, directing where you can, accepting guidance where you must. The work is physical and purifying."
    # [Montage Visual: Mud-splattered hands hauling timber; Lupe unrolling a ledger notebook stamped with "Town Fund"; kids planting mangrove seedlings along a newly bermed edge; a makeshift kitchen serving bowl after steaming bowl of soup; Tomas placing a carved wooden compass into a small shrine beneath a lamplight.]
    # play music "music_placeholder"  # [Music: Percussive, driving—heartbeat matched to labor]
    # play sound "sfx_placeholder"  # [Sound: Hammers, the slap of wet wood, the murmur of planning voices—intense, immediate]
    "Time accelerates, then skips. Weeks compress: nights of setting up temporary shelters, days cataloguing salvageable equipment, late-night meetings where you argue clauses and then sleep on cots between shifts. The arousal does not drop; it turns"
    "into sustained, feverish resolve. The town is alive in a way that is not peaceful—but it is purposeful."
    "Lupe: (breathless, ledger open) 'We matched the first grants. Local donations, a crowd-funded pool, a small state stipend—enough to get the first phase of rebuilding scheduled. Transparency first, Maia. No secret deals.'"
    show maia_rivera at left:
        zoom 0.7

    maia_rivera "No secret deals,"
    # [Scene: Harbor | Winter—Pale light over a quieter sea]
    hide maia_rivera

    scene bg ch15_5195df_9 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The scrape of ropes, distant gull calls softer now]
    "It is cold when Jonah Kade returns. Not dramatic—no banging on doors; he shows up with borrowed gloves and an unspoken clause between you. His arrival is steady as a tide returning to a different shoreline."
    "Jonah Kade: (hands working on a net, voice low) 'Thought I'd give it a few months. Wanted to see what this would look like when the mud settled.'"
    "You: (You keep your hands busy—mending a net by habit—because looking directly at him would be a negotiation in itself.)"
    show maia_rivera at left:
        zoom 0.7

    maia_rivera "There is still mud everywhere. But people are back on small boats. Not everything is as it was."
    "Jonah Kade: (He knots the rope with hands that know how to hold a line without crushing it.) 'I'm not the same, either. Not from this.' (He pauses, eyes meeting yours; there is softness, then a boundary that holds.) 'I came to help. On my terms.'"
    "Maia Rivera: (You let a laugh slip—half a release, half apology.) 'I'll take the terms.'"
    "The conversation ripples outward—multiple turns, small adjustments. You and Jonah Kade speak around rawness: he remembers his lost sibling in a story about a sea-route that changed; you recount a moment at the meeting when someone"
    "shouted something you still replay. You do not tidy the hurt away. You do not expect a single reconciliation to fix what was broken. Instead, you make a different pact: honest proximity. You will each keep"
    "certain reins, and respect the other's knots."
    show jonah_kade at right:
        zoom 0.7

    jonah_kade "We can teach the younger ones how to read tides again. But some trawls have to go—gone for good. We'll have to learn new ways."
    "Maia Rivera: (You nod, feeling the hollow where old rituals lived.) 'We'll plant new marsh strips to help the nursery reefs. We'll build platforms that can rise with water. We will lose some shapes of things, Jonah. But we'll keep the knowledge.'"
    # play sound "sfx_placeholder"  # [Sound: A gull cuts across; a hammer rings in the near distance—work continuing]
    hide maia_rivera
    hide jonah_kade

    scene bg ch15_5195df_10 at full_bg
    "Elias Wren appears on the edge of the dock—less polished than he had been; his trench coat folded into a practical layer, boots muddied. His steps have the uncertain rhythm of someone who has learned to listen."
    "Elias Wren: (approaching, his gray eyes open, vulnerable) 'Maia.' (He pauses, searching for the right metric for apology.) 'I didn't come because I wanted to be forgiven. I came because I needed to learn what we—what I—missed.'"
    "You: (You keep working the net, the movements grounding.)"
    show maia_rivera at left:
        zoom 0.7

    maia_rivera "You learned faster than most. You asked questions. You stayed when people could have, understandably, chased you off."
    "Your voice holds something like a verdict and a welcome."
    show elias_wren at right:
        zoom 0.7

    elias_wren "I realize I came here with charts and windows. I should have come with a chair and a jar of coffee and a willingness to be wrong more often.' (He exhales, a sound like someone dropping a weight.) 'If there were a way to make restitution, I would. If not—if it's only learning—then I will take that."

    maia_rivera "Do what you can. And be visible when you can't—let people see the work."

    elias_wren "I will."
    # play music "music_placeholder"  # [Music: A lower, hopeful motif begins—resilient, bright]
    hide maia_rivera
    hide elias_wren

    scene bg ch15_5195df_11 at full_bg
    "You watch as Elias Wren helps haul a pallet, his movements clumsy with unfamiliar manual labor yet earnest. Jonah Kade—nearer now—offers an offhand instruction that is accepted without rancor. Lupe counts donations and volunteers with fierce,"
    "radiant competence. Tomas teaches a small group of children to carve compass shapes into scrap wood as a ceremony of continuity."
    "There are losses that hang like weathered flags. The old fishmonger’s awning is gone; an ancestral boatyard's facade will never be the same. But there are seedlings planted in the mud line that will take root. The town has had to remake itself in ways neither utopian nor entirely tragic."
    # [Montage Visual: Spring comes in a flush—young mangroves set into the edge of a restored wetland, children learning to tie split-sail knots, a new community-run workshop where locals forge parts, Lupe placing a ledger in a new glass-fronted case marked "Town Fund—Open Records."]
    # play music "music_placeholder"  # [Music: Crescendo—joy threaded with exhaustion; very high intensity]
    # play sound "sfx_placeholder"  # [Sound: Laughter between breaths, hammers, a child's shout as a seedling goes into the ground]
    "You stand on the rebuilt boardwalk one evening, hands in your pockets, the dusk folding the town into a softer silhouette. The pumps still hum—now augmented by community-managed controls and a rotation schedule posted publicly. The"
    "work continues; it will never be finished. That is both the burden and the relief."
    "Tomas finds you and slips something into your palm: a small, rough compass carved from the same beam as the old boathouse."
    show tomas_rivera at left:
        zoom 0.7

    tomas_rivera "For when you feel the tide pulling you too far. For when you need to remember the shore."
    "You: (You feel the weight of the wood, the familiar grain. The guilt is still there—an ache that does not go away—but now it sits beside meaning and responsibility rather than swallowing them.)"
    show maia_rivera at right:
        zoom 0.7

    maia_rivera "I'll keep it where I can see it."
    # [Scene: Rooftop Garden of Maia's Childhood House | Dull Mauve Sunset — Final moments]
    hide tomas_rivera
    hide maia_rivera

    scene bg ch15_5195df_12 at full_bg
    # play music "music_placeholder"  # [Music: A single, warm piano line threads through the air—soft, resolved]
    "You sit on the low wooden bench, the compass warm in your palm, the bracelet against your wrist. The rosemary's first tender leaves catch the light like small flags. They are stubborn and tiny. They are"
    "the proof of something else: that from char and decision and fatigue, life can insist on a new shape."
    "You close your eyes for a beat and feel everything: the anger you faced, the hands that reached for you, Jonah Kade's quiet return, Elias Wren's faltering apology, Lupe's ledger sliced through with honest columns, Tomas'"
    "carved wooden compass, the smell of soup that soothed a ragged crowd. The ache of what you traded will remain. You do not ask to be absolved. You ask to be steady enough to keep listening"
    "and to keep showing up."
    "The sun lowers, painting the rooftop a copper hush. You press your thumb against the small compass and feel the grain like a pulse. The town's life continues below in a medley of noise: a hammer,"
    "someone calling for more seedlings, a laugh that bounces off the old eaves. It will be messy. It will be human. It will be yours."

    "You open the Moleskine and write one line across the top of a fresh page" "We choose to belong to the work."

    scene bg ch15_5195df_13 at full_bg
    # play music "music_placeholder"  # [Music: The piano resolves into a humble, hopeful chord]
    # play sound "sfx_placeholder"  # [Sound: A gull cries once, then fades]
    "You rise, set the compass against the planter, and tuck the Moleskine back into your jacket. There is no tidy ending—only continuity stitched by hands, song, argument, and repair. You let the rooftop wind carry the"
    "sound of the town into your shoulders like a promise: keep tending. Keep listening. Keep making space."

    scene bg ch15_5195df_14 at full_bg
    # play music "music_placeholder"  # [Music: Soft, lingering chord]

    scene bg ch15_5195df_15 at full_bg
    "THE END"
    # [GAME END]
    return
