label chapter1:

    # [Scene: Marabel Promenade | Dawn]

    scene bg ch1_Start_1 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano, low and steady]
    # play sound "sfx_placeholder"  # [Sound: Soft creak of wood, distant tide whisper]
    "You step onto the Promenade with the ocean already inside your nostrils — brine, kelp, the faint metallic tang that rides storm fronts in like a guest who never leaves. Your boots make a slow, familiar"
    "print on the damp wood. The promenade answers with a tired but certain creak beneath your weight, the sound of the town taking stock of you as much as you of it."
    "Your fingers find the brass compass at your throat out of habit. The metal is warm from your skin, its fray of cord honest and frayed, the kind of object that doesn't pretend to be newer"
    "than it is. You tuck it back under your jacket and pull the tablet from your satchel: models, annotated maps, a stack of notes you haven't stopped turning over since the plane. The screen still glows"
    "faintly in the dawn."
    "You move along the railing and catalog the shoreline like a scanner. Pilings — some newer, capped in pale concrete; some old, mottled with barnacle patterns like fingerprints. Raised gardens gleam with early-morning dew, tomato vines"
    "bowing under their own green weight, Marta's hand-lettered sign caught in a breeze. Farther, the Beacon stands: a glass silhouette against a slate sky, tidy and alien, its edges precise where the town is ragged. It"
    "catches light in a way that makes you think of a threat and a promise at once."

    menu:
        "Finger the compass, steady yourself":
            "You let your thumb trace the compass rim until the brass cools, groundable metal between you and the endless horizon."
        "Open your tablet, skim the models":
            "You swipe through the marsh restoration overlay, the colors too neat against the messy, salt-splashed world outside the screen."

    # --- merge ---
    "You continue down the Promenade toward the Old Boatyard."
    "You continue down the Promenade toward the Old Boatyard."
    # play sound "sfx_placeholder"  # [Sound: Distant voices, a kettle boiling somewhere near the market]
    "Noah Reyes waits halfway to the boatyard, shoulders loose in the same way they always were — a posture that somehow reads as calm even when his jaw is doing work. He pushes a hand through"
    "his curls as you approach. Up close, his skin wears the dawn with a softness; his eyes are steady and quiet, the brown deep and unhurried. For a moment you measure the space between you and"
    "the thousand reasons you left; that old impatience hums beneath the relief."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "You're early. Or late, depending on how dramatic you felt like being."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Dawn's good for paperwork. Less glare on the models."
    "You offer a small, dry smile you hope reads as enough."

    noah_reyes "Your models will get sun eventually. How was the flight?"

    asha_moreno "Quiet."
    "The word sits flat; there's a world folded into it you don't open. 'I tried to sleep, but I kept running the sediment maps. They've changed more than I expected.'"
    "Noah Reyes watches you, still."

    noah_reyes "You look like you're carrying a storm and a spreadsheet. Which one weighs more?"
    "You shift your tablet in your arms. 'Both. Different kinds of pressure.'"

    noah_reyes "Promise me you won't try to carry them alone.' His gaze flicks to your hands, to the compass cord. 'We—people here—aren't used to you being the only one with the map."

    asha_moreno "I don't want to be the only one.' Your voice narrows, honest and small. 'I left to learn how not to make the same mistakes. Coming back feels... like handing everyone what I learned and hoping it's enough."

    noah_reyes "No one's asking you to be perfect, Asha.' He hesitates, searching for the words. 'We're asking you to be here. To argue. To make the plans. With us."
    "There is a pause long enough that a gull cries and the town rearranges itself around the space you hold together."

    noah_reyes "Mayor Rosa's looking for you later. She said she's got calls stacked like weather reports."

    asha_moreno "I'll go."
    "Noah Reyes watches you convert grief into plans the way he watches a map become a neighborhood meeting agenda."

    noah_reyes "Before you dive back in — are you eating? Marta's got stew if you can stand her persuasive spoon."

    asha_moreno "Lead the way. I could use a spoonful of something that's not data."
    "Noah Reyes's smile is a small arrangement of familiarity. He offers you an arm and you take it, the contact both ordinary and oddly important in the quiet. You walk together toward the market, steps slow,"
    "the conversation folding into that comfortable cadence of two people who know each other's silences."
    # [Scene: Floating Market & Raised Gardens | Dawn]
    hide noah_reyes
    hide asha_moreno

    scene bg ch1_Start_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft clatter of pots, distant laughter]
    # [Smell: Warm broth, wet earth, herbal steam]
    "Marta is kneeling in the soil, fingers dark with compost, humming something tuneless as she tends the tomato trellis. She looks up and broadens her grin like a shoreline. Up close, the garden smells of rosemary and damp dirt — a scent that reads as defiance to asphalt and concrete."
    show marta_chen at left:
        zoom 0.7

    marta_chen "Look who dragged herself back. You look like a woman who has seen models and decided to keep breathing."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "I decided to keep trying."
    "You set your tablet on a crate, the screen dim to avoid glare. 'I want to present a marsh restoration plan. Distributed sensors, community governance — places where residents actually own the data.'"
    "Marta pauses, hands wiping on her overalls. 'Sensors? Smart mud?' She chuckles, then looks at you with something almost reverent. 'If you can make the tech fit the people instead of people fitting the tech, you'll have my vote.'"

    asha_moreno "That's the point."

    marta_chen "Also, Noah says you barely slept. Eat. You'll think better with broth."
    "You take the offered bowl, the warmth seeping into your palms. For a breath, the past — your father's laugh, the smell of diesel in a small cabin — sits in the steam, not as accusation but as a map you can read."

    menu:
        "Tell Marta everything about the sensors":
            "You sketch the outline in the air: community nodes, open data, local management. Her eyebrows knit in focus, her approval small and essential."
        "Keep technical details for the meeting":
            "You nod, tuck the tablet away, and say only what matters most: 'Community-run, accountable.' Marta hums and pats your shoulder."

    # --- merge ---
    "Marta resumes tending the tomato trellis as the morning continues; you prepare for the boatyard."
    # [Scene: The Old Boatyard | Morning]
    hide marta_chen
    hide asha_moreno

    scene bg ch1_Start_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft hammering from a distance; the creek of a rope]
    # [Touch: Salt-stained wood, rough sand beneath your soles]
    "Eli looks up from a hull as you approach, wood dust streaking his forearm. His grin is the kind bred by shared labor and afternoons spent hauling nets. He runs a hand along the wet edge of a keel, then takes his time meeting your gaze."
    show eli_duarte at left:
        zoom 0.7

    eli_duarte "You actually came back. Thought you'd quit us for the Quads and big data."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "I came back with maps.' You pause. 'And the inclination to argue with them until they make sense for the people who live here."

    eli_duarte "Good. Because if you leave all the arguing to Lila Park and her shiny things, we'll end up with a promenade that looks like it hates salt.' He wipes his hand on his pants and gestures at the hulls. 'You remember how my dad taught me to splice? He'd say, 'Fix what's broken, not the whole sea.'"

    asha_moreno "I remember. I think about his hands when I draw cross-sections. There's a lot that fits together if you know where the fasteners go."
    "Eli studies you for a long beat, then nods like a man settling a price. 'Don't let them make everything something you can't touch. We need work you can smell, not just reports.'"

    asha_moreno "That's what I'm trying to bring."

    eli_duarte "Then bring it. We'll help. Old boats, new boots — same storms."
    "His reassurance is simple, tactile. It grounds you the way a cleat grounds a line to a dock. You run your palm along an old beam and let rumors of your father's boat fold into the wood grain — a grief made practical, a memory shaped into work."
    # [Scene: Lila Park's Resilience Hub (The Beacon) | Morning]
    hide eli_duarte
    hide asha_moreno

    scene bg ch1_Start_4 at full_bg
    # play music "music_placeholder"  # [Music: A thin, modern hum]
    # play sound "sfx_placeholder"  # [Sound: Distant chatter from a security console]
    "From the Beacon's plaza, the interactive model spins at the base, neat waves in a clear pool. The building is efficient, purposeful. You notice Caleb, quiet at the edge of a meeting cluster — his posture"
    "like a wire ready to send a signal. You don't speak with Lila Park now; that conversation is for the town square and Mayor Rosa's office. For the moment, the Beacon is an object lesson in"
    "scale."
    "You step back from its clean lines and let your eyes rest on the town's ragged edge. There is comfort in contrived geometry and in disorder; both tell stories. Today the story you must tell is one that threads them together."
    # [Scene: Mayor Rosa's Office | Late Morning]

    scene bg ch1_Start_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Muted phone conversations, the click of a fax machine (old tech alive)]
    "Mayor Rosa sits behind a desk that holds more pens than a single human should own. Her hair is braided with an elder's steadiness. The phone on the corner lights like a constellation — a queue"
    "of calls waiting for her. She lets the line blink and meets you without the filter of politics — for a heartbeat she is just Rosa."
    show mayor_rosa_alvarez at left:
        zoom 0.7

    mayor_rosa_alvarez "Asha. You're back. Sit. Tell me what you're going to do before the Beacon's plan gets to the council."
    "You place your tablet between you, models angled toward her. Your pulse is low, measured; the room smells faintly of lemon and paperwork. You explain the marsh restoration plan in the simplest terms you can: restore"
    "tidal marsh to absorb surge, community-governed sensor nodes to monitor salinity and erosion, training programs to keep the work local."

    mayor_rosa_alvarez "Community governance — how will that work when the consortium offers turnkey solutions? They have money and a timeline. People panic under deadlines, Asha."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Which is why the sensors must be transparent. Data belongs to the town. Contracts with private partners must include governance clauses and buy-back options. Small-scale pilots prove the method and give time to scale without selling the shore."
    "Mayor Rosa folds her hands. 'You're offering patience and process in a room that hears sound bites and press releases. That's a hard sell.'"

    asha_moreno "I know.' You feel the old guilt again, quieter now, like a pressure in a sealed jar. 'I left to learn what could be done. I'm not asking for blind trust — I want to show the work, step by step."

    mayor_rosa_alvarez "Your father would've liked that.' Her voice breaks in the exact place you expect; grief is a town memory and she shares it with you like a map. 'Listen, there's momentum for both kinds of answers. Be prepared for both rooms. And Asha—' She pauses and her eyes find yours. 'Make sure you come back for dinner once in a while. You can't carry all of this without eating."

    asha_moreno "I'll try. No promises on the timing."

    mayor_rosa_alvarez "Promise me you won't let guilt write your schedule alone."
    "You, in the quiet that follows, think of the long list of tasks you already imagine for yourself. But the mayor's words settle into your ribs like an anchor. You will have to ask for help."
    "You will have to let the town be in the work with you, not simply an audience."
    "The town's morning rhythm slows into a hush — people are building their day around a coming argument and a coming storm warning."
    # play music "music_placeholder"  # [Music: Piano continues, softer]
    # play sound "sfx_placeholder"  # [Sound: Storm-warning lampposts blink; a low municipal chime measures out the morning]
    "You stand at the edge of Mayor Rosa's office and feel, with a clarity that is almost physical, the weight of expectation. It's not dramatic. It is a steady pressure, like the tide at a full"
    "moon — inevitable, quietly relentless. Your tablet hums with models; your compass rests warm against your skin. The town holds its breath in a long, inhaled moment."
    "The intensity of the morning has increased from the stillness when you first arrived, but only by a small measure: a curated rise, like the gentle swell before a wave forms. You are the point between"
    "memory and plan, between Eli's hands and the Beacon's glass. Noah's presence is a low current under everything, a support you can lean on if you learn to ask."
    "You close your fingers around the compass, feeling its familiar weight. The marsh restoration plan is waiting for rooms, for voices, for friction, for compromise. The first presentations will be small, the first votes tentative. But"
    "this is where momentum begins — in speech, in soil, in the slow exchange of trust."
    "You inhale the briny air, exhale, and let the town and its tide shape your next step. You lift your chin and move toward the community hall where the first public review will be held. There will be questions, and there will be mouths that need answering beyond charts."
    "You step off the Promenade, the boards whispering behind you, and the daylight shifts as if to mark the page."
    "The Beacon's halo catches your outline and the town hums like a living map. You realize the conversation to come will be quieter than a rally and more consequential: it will be the slow rearrangement of"
    "how Marabel cares for itself. You taste salt and resolve, and then you continue — toward the hall, toward the mayor's schedule, toward the first of many meetings."
    hide mayor_rosa_alvarez
    hide asha_moreno

    scene bg ch1_Start_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter2
    return
