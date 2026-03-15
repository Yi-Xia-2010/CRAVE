label chapter25:

    # [Scene: Marabel Promenade | Dusk]

    scene bg ch14_4cd0d9_1 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano, minor chord progressions at a steady, mid-tempo pace]
    # play sound "sfx_placeholder"  # [Sound: Gull cries, a distant motor, the soft slap of tide against pilings]
    "Narration:"
    "You open the chapter where the lab door closed—months have folded outward from that night into routines that smell of salt and bleach and sawdust. The town has a new rhythm now: early morning monitors, afternoon"
    "volunteer builds, evening ledger checks. The Promenade holds its scars like a geography you can read by touch."
    "Narration:"
    "You draw your coat tighter against the damp and lean on the rail. The compass at your throat is scuffed; when you tilt it, the needle wobbles like a quiet accusation before settling. It points. You"
    "count small mercies the way you used to count tidal flats—one: cordgrass taking root along the southern berm; two: the vendor near the raised gardens who still sells candied kumquats; three: the students at Tidewatch who've"
    "learned to read a salinity chart by hand."
    "Narration:"
    "Noah approaches from the far end of the boards, a silhouette you know better than the lines on a map. He moves with the practiced economy of someone who has spent months coordinating schedules and sympathy—his presence is efficient comfort."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "You look like you're trying to catalog the horizon. How's the ledger tonight?"
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Same as always—numbers with edges, stories with stains. It's honest in ways contracts aren't."
    "Narration:"
    "Noah smiles, but there's a reservation at the corner of it, the kind that arrives when people have learned how to hold grief without being crushed by it."

    noah_reyes "We've kept houses dry. We've kept people together. But insurance hasn't forgiven us and neither has the market."

    asha_moreno "Some found offers they couldn't refuse. A few left with clean checks and closed doors. Others stayed and learned new prayers—how to plant on stilts, how to board a window with kindness."

    noah_reyes "Do you miss the idea of certainty?"

    asha_moreno "I miss the luxury of thinking certainty was an option. Now I miss people."
    hide noah_reyes
    hide asha_moreno

    scene bg ch14_4cd0d9_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The tide keeps time, a dull metronome under the conversation]
    # play music "music_placeholder"  # [Music: A gentle swell, held in minor]
    "Narration:"
    "His hand in yours is familiar and a little fragile. You have learned together how to be practical and present; you have not solved how to be unscarred. That small contact is both an anchor and"
    "an unspoken question: will the work hollow you, or will it shape the person you want to be?"

    menu:
        "Read the letter from the family who left aloud":
            "You unfold the letter carefully, feeling the cheap paper between your fingers. The voice on the page is soft—thankful for what you tried, sorrowful for what could not be saved. Saying it aloud makes the loss communal; Noah listens and says nothing for a moment, letting the words hang like nets between you."
        "Keep the letter folded and tuck it into the ledger":
            "You slide the paper back into the ledger like a pressed leaf. The note becomes private proof—something to carry without asking others to map it. Noah watches, reading the small movement in your jaw, and squeezes your hand with a patience that asks you to set the weight down when you can."

    # --- merge ---
    "You choose, or you choose not to choose; either way the letter sits in your chest. The ledger on your lap is dented at the corner where you've kept stamps and a child's drawing for weeks."
    "Numbers cleanly show buyouts, subsidized rebuilds, and the stubbornly high insurance bands on the west blocks. Words show the cost—neighbors selling frontage, a grandmother who refused a buyout because 'our porch remembers my husband's hands.'"
    show asha_moreno at left:
        zoom 0.7

    asha_moreno "Eli says the old boat frames are being used as platforms now. He laughs while he works, but his hands know how to hold loss. That matters."
    show noah_reyes at right:
        zoom 0.7

    noah_reyes "It matters more than a glossy plan."

    asha_moreno "People taught me to call the shoreline by its old name. The town keeps teaching me that not everything is measured in dollars."

    noah_reyes "So what do we teach them next?"

    asha_moreno "How to litigate when needed. How to plant cordgrass before a storm. How to sit with the fact that some bargains buy us safety and cost us something else."
    # [Scene: The Old Boatyard | Early Evening]
    hide asha_moreno
    hide noah_reyes

    scene bg ch14_4cd0d9_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Blade on wood, sporadic footsteps, a radio playing a static-blurred folk song]
    # play music "music_placeholder"  # [Music: Low strings, a slow tempo that carries the texture of memory]
    "Narration:"
    "You walk to the boatyard because the boatyard is where people still make things that hold out against weather. Eli's hands are rough as ruined rope, but he looks up with the kind of openness that has saved you from cynicism more times than you can count."
    show eli_duarte at left:
        zoom 0.7

    eli_duarte "You sat with Rosa last week, yeah? How's she holding?"
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Mayor Rosa is tired, but holding. She's balancing ledgers and letters in equal measure. She keeps asking 'Who do we owe?' and I keep thinking some debts aren't financial."

    eli_duarte "Deputy counts more than money around here. She held the meeting good. She holds town in a way that doesn't need applause."

    asha_moreno "There are lawsuits brewing, and a few clauses that read like fences. I'm helping where I can—reviewing, arguing, pushing for resident oversight when clauses get hungry."

    eli_duarte "You keep your hands in everything. You wear that compass like a badge and a burden. You need to sleep sometime."

    asha_moreno "Sleep is for nights when everything's mostly right. I count naps like they are victories."

    eli_duarte "Don't let it make you small. The town needs the big part of you, not the hollowed part."

    asha_moreno "I keep trying. There's a note from Marta that made me laugh yesterday—she's got volunteers teaching kids to plant cordgrass on raised beds. She writes like the world will still let them joke."

    eli_duarte "Good. Keep that. And pass me that plank—hand me your tired, and we'll turn it into a porch."

    menu:
        "Write back to the family who left, inviting them to visit":
            "You pick up the pen, the nib scraping slightly as if unsure. You write an invitation that doesn't beg but keeps a door open. The words feel clumsy but sincere. Eli nods approvingly, then stands and hands you a carved scrap with a child's scribble burned into it—'Remember us'—which you tuck into the ledger."
        "Fold the reply into a draft of policy notes instead—keep things professional":
            "You set the letter aside and begin drafting a shorter, formal response that reads like a record. The tone is right but sterile. Eli watches, then claps his hands once and says, 'Paper keeps, but people keep more.' You keep the sterile draft anyway; the town needs both kinds of records."

    # --- merge ---
    "You choose a reply, or you choose a policy; either path marks you. The boatyard smells like varnish and rain, a familiar perfume that steadies your breath. You tuck the carved scrap into your ledger behind a receipt—an accidental altar."
    # [Scene: Raised Gardens / Tidewatch Lab | Late Evening]
    hide eli_duarte
    hide asha_moreno

    scene bg ch14_4cd0d9_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmured instructions, the soft scrape of trowels against soil, the distant hum of the Beacon's sensors]
    # play music "music_placeholder"  # [Music: Quiet plucked strings, measure maintained]
    "Narration:"
    "At Tidewatch you have a class tonight—local high schoolers learning to deploy a simple salinity probe. The drills are matter-of-fact, and you find a kind of unclenched purpose in teaching young hands to read data and"
    "read weather. The Beacon's distant thrum is now background—the new normal. For some neighbors, it is an instrument that keeps them safe; for others, it is a reminder stitched with resentment."
    show marta_chen at left:
        zoom 0.7

    marta_chen "They're good kids. They ask the right questions. Some of them don't want the Beacon; others think it saved their aunt's house. It's complicated."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Complicated is the town's middle name now. I'm trying to teach them both—how to speak to sensors and to politicians."

    marta_chen "And how do you teach them to be angry without it eating them?"

    asha_moreno "We teach them the difference between righteous anger and self-consumption. We teach them how to hold both grief and action in a single hand."

    marta_chen "That's a tall order. But you have a pulley for tall things."

    asha_moreno "Noah helps. So do you and Eli and Rosa. It takes a lot of pulleys."

    marta_chen "Have you heard from Lila Park? She came by the labs last week—helping with the sensor interface."

    asha_moreno "Her presence is...complex. She trims inefficiencies and leaves people with something that works. Some colleagues say she has a real face now; others call her memory of bargains. She says she wants partnership. I listen and remind her of resident oversight."

    marta_chen "And Rosa?"

    asha_moreno "Rosa keeps her balance. She won't sign anything that erases the commons. She asks harder questions now. She asks them aloud."

    marta_chen "We need more of that. The town needs people who ask aloud."
    "Narration:"
    "The students file out into the lantern glow, hands smelling of soil. You stay for a moment to watch them walk into the Promenade's dim. The Beacon washes the horizon with a soft, impartial light, its outline now mundane in the town's memory."
    # [Scene: Promenade Bench | Night]
    hide marta_chen
    hide asha_moreno

    scene bg ch14_4cd0d9_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The tide, a child laughing somewhere distant, the faint click of a nearby sensor]
    # play music "music_placeholder"  # [Music: Piano and cello trade phrases—melancholic, measured, building just enough to make the chest ache]
    "Narration:"
    "You open the ledger again. The numbers are not neutral; they are made heavy by names. The page smells faintly of the boatyard varnish and Marta's soil. The scrawl of a neighbor's handwriting reminds you that every figure in a column is a doorstep someone still walks across."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "Do you think we did the right thing?"
    "Narration:"
    "You look at him—the question is raw, offered between two people who have watched the same storms. You want the answer to be whole and bright."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "We did what we could with the time and tools we had. But 'right' isn't something we get to issue in a single verdict. It spreads, like sediment in a marsh: some of it builds land; some of it buries oysters."

    noah_reyes "And us?"

    asha_moreno "We keep practicing how to be present. We keep learning how to say 'not on my watch' without making the watch itself a prison."

    noah_reyes "Promise me one thing."

    asha_moreno "What?"

    noah_reyes "When the contracts start spelling things in legalese—when the Beacon's numbers begin to look like the only truth—you won't let us forget the people who taught us how to read the tide."

    asha_moreno "I won't. But I can't promise every time will be easy."

    noah_reyes "I don't want easy. I want steady."
    "Narration:"
    "You both fall into a quiet that is almost prayerful."
    "Narration:"
    "The ledger closes. The brass compass rests on top like a small, battered god. You breathe the salt air, count small mercies—cordgrass planted, one roof raised, one child who learned to take a water sample without fear—and you feel the strain of what remains undone tighten like a chord."
    "Narration:"
    "You look toward the Beacon. Its halo is no longer a single sign of salvation; it is an argument in steel and light. For some it is a friend, for others an emblem of bargains struck in fatigue."
    hide noah_reyes
    hide asha_moreno

    scene bg ch14_4cd0d9_6 at full_bg
    # play music "music_placeholder"  # [Music: A subtle rise—mid-tempo, insistent—then it holds, taut]
    "Narration:"
    "There will be clauses to contest and clauses to accept. There will be nights in courtrooms and mornings with seedlings. The ledger will keep the numbers; your hands will keep the stories. You and Noah will keep holding each other through the in-between."
    "Narration:"
    "Page-turning thought: The next ledger entry will ask a price—who pays for safety, and what are they allowed to keep? The answer will not be in ink but in decisions pressed by tired hands."

    scene bg ch14_4cd0d9_7 at full_bg
    # play music "music_placeholder"  # [Music: A single studied chord that invites continuation]
    # play sound "sfx_placeholder"  # [Sound: The tide's patient applause against pilings]

    scene bg ch14_4cd0d9_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter32
    return
