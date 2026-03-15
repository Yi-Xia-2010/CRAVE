label chapter14:

    # [Scene: Rooftop Sanctuary | Dawn]

    scene bg ch12_f99e88_1 at full_bg
    # play music "music_placeholder"  # [Music: Gentle piano with soft strings — warmth edging into resolve]
    # play sound "sfx_placeholder"  # [Sound: Bees murmur in the herb beds; distant gulls; the faint clatter of a pump in the yard below]
    "You wake before the town does. The sanctuary smells of rosemary and wet wood, the green sharp enough to cut through the salt in your lungs. Your notebook lies where you left it, pages thumbed and"
    "dog-eared; the red thread on your wrist has loosened into a soft loop from sleepless nights and a handful of new, necessary compromises."
    "The evacuation worked. That sentence sits in your chest like a small, stubborn bird — fluttering, fragile, relentless. Lives were saved. Lives were altered. The ledger you keep in your head is not neat; it is"
    "stitched in urgent, messy script. You learned the metric of success is no longer perfection but fewer empty names on the lists."

    scene bg ch12_f99e88_2 at full_bg
    show elias_novak at left:
        zoom 0.7

    elias_novak "Morning."
    "You know how to read him: the bright, brittle enthusiasm softened into something steadier. He has been here, nights on the floorboards, mornings carrying tote bags of supplies. He smells like rain and the knitting wool"
    "from the protest camp; he smells like every stubborn, hopeful plan he's ever convinced someone to try."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "You didn't have to—"

    elias_novak "I know. And I wanted to. You did the thing, Maya. You did the terrible, necessary thing."
    "You imagine telling the story differently — that you were together at every step — and for a moment you let yourself believe it. Then you think of Finn and the rope lines and the families"
    "who came screaming into the sanctuary with nothing but a child and a shoebox of photos. You name the things you can't un-remember to keep them from hollowing you out."

    elias_novak "We published the first draft of the protocols last week. Other towns are already asking for the template."

    maya_serrano "It feels strange to be copied.' (half a smile) 'Like a bandage being used as fashion."

    elias_novak "Better fashion than funeral shrouds."
    "You reach for a rosemary sprig and press it between your fingers. The scent goes straight to the place inside you that keeps watch. He watches too, with blunt tenderness and an unpracticed softness that makes you want to be brave in ways other than sacrifice."

    menu:
        "Take his hand":
            "You close your fingers around his. His palm is warm; the tremor in your chest eases for an instant."
        "Rest your forehead against his shoulder":
            "You let the world tip sideways. He murmurs something you don't need to parse, and the sound is its own shelter."

    # --- merge ---
    "The moment settles into a quiet agreement between you."

    elias_novak "Are you... angry at me for pushing people to go, for—"

    maya_serrano "I don't have the luxury of simple anger.' (you meet his eyes) 'There's gratitude, and there are costs. Both of those are true."

    elias_novak "I stayed because I couldn't imagine it without you in it."
    "He leans in the way people do when they try not to break something by being too abrupt. The kiss is small, then insisting; rosemary and salt and the metallic tang of emergency adrenaline. It's not"
    "an erasure of what happened. It is an agreement, a folding of two battered maps into one."
    "When you pull back, the dawn has convinced the sky to be less heavy. There are still losses — the bookshop's windows ago turned glass-skin from too much water; you will not be able to rescue"
    "the stacks of dog-eared books that smelled like pages and sea. But the kiss leaves a warmth you can carry into council rooms and grant applications."
    # [Scene: Walk through stairwell down to Rosa's café | Mid-morning]
    hide elias_novak
    hide maya_serrano

    scene bg ch12_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Doorbell chime turned into a signal — warm and familiar]
    # play music "music_placeholder"  # [Music: Acoustic guitar picked in supportive, hopeful arpeggios]
    # [Scene: Rosa’s café | Mid-morning]

    scene bg ch12_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Coffee steam, low conversation, spoons against ceramic; the smell of cinnamon and the faint chemical tang of disinfectant]
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "Maya! Sit. Please. You look like a ghost who hasn't eaten in three days."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "I could say the same to you."

    rosa_alvarez "You're not allowed to martyr yourself in my café. I have insurance and a name to protect."
    "You laugh because you know she would hang you by your own red thread if it meant you rested. Finn is at a back table, surrounded by a tower of blueprints and a half-assembled pump; grease on his knuckles, his grin stubbornly unchanged."
    show finn_serrano at center:
        zoom 0.7

    finn_serrano "We rerouted the intake lines last night. Floating storage's holding. We bolted the crates down and made a list of the salvage priorities."

    maya_serrano "How's the wiring?"

    finn_serrano "Won't be pretty, but it won't short out either. I taught two kids how to splice in twenty minutes.' (he brags, then softens) 'They'll keep the pumps running when I'm on shift."
    "Hana joins you at the large wooden table, her tablet glowing with grant pages and line items. The scientist in her is all quiet calculation; the friend in her is the one who will hold your shoulders and tell you that breathing is not a waste of time."
    hide rosa_alvarez
    show dr_hana_park at left:
        zoom 0.7

    dr_hana_park "The federal grant—it's conditional. It funds relocation assistance, but it requires a governance board and an audit trail. There are clauses that could let private contractors override local decisions unless we put safeguards in place."

    maya_serrano "And you can bend it toward community control?"

    dr_hana_park "We can, but it will take documented protocols, transparent accounting, and an explicit community charter. Which you, of course, led the drafting of."
    "The grant arrives like a hand offering a ladder with missing rungs; it is a gift with a hold attached. You have already spent too many hours convincing yourself that strings can become scaffolding rather than shackles."

    maya_serrano "We publish the protocols. We require community membership for the governance board. We specify a clause that prioritizes equitable relocation over profiteering. We make audit reports public."

    dr_hana_park "And when the corporate reps come with glossy presentations?"

    maya_serrano "We bring the people they affect. We put the elders and single parents up front. We make sure their stories are in every slide."
    hide maya_serrano
    show rosa_alvarez at right:
        zoom 0.7

    rosa_alvarez "We'll host the community hearings here. I'll keep coffee brewing until everyone quits talking."
    "You feel something internal shift — not resolution, but a steadying. The string of obligations that used to knot into isolation begins to braid into a rope you can trust."

    menu:
        "Let the volunteers nap in the back room":
            "You wave someone off and point to the stack of blankets. They collapse gratefully; the café fills with soft snores and the hum of the espresso machine."
        "Give a quick pep talk and send them back out":
            "You stand on a chair and say what needs saying. They leave with a new list and a scrappy grin, energy reignited until the next lull."

    # --- merge ---
    "The volunteers' rest or renewed energy both contribute to the ongoing recovery work."
    # [Scene: Later — community meeting in the café | Mid-morning]
    hide finn_serrano
    hide dr_hana_park
    hide rosa_alvarez

    scene bg ch12_f99e88_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmurs, an old radio playing a weather report in the corner, the periodic clang as someone sets another tray down]
    # play music "music_placeholder"  # [Music: Low, hopeful choir pads under the conversation]
    "The governance board forms slowly and improbably: elders who remember the old harbor, teenagers who were ashore during the first surges, small-business owners who cannot imagine moving. You facilitate rather than command; your notebook becomes less a ledger and more a map of trust."

    "Elder" "We don't want to be cast out of our own homes."
    show maya_serrano at left:
        zoom 0.7

    maya_serrano "No one will be moved without community consent and full support. We are building transport, storage, and new jobs tied to the adaptation work."

    "Teen Organizer" "Will there be apprenticeships? I want to learn the pumps and the wiring."
    show finn_serrano at right:
        zoom 0.7

    finn_serrano "You can bolt things and you can learn to name tools. I will teach you. We need hands who will care for what we keep."
    "Across the table, Hana lays out the audit triggers and the emergency thresholds; the town's priorities etch themselves into formal language. The document that once felt like a hard edge becomes a shared instrument — a covenant to be amended, not a law to be imposed."
    show dr_hana_park at center:
        zoom 0.7

    dr_hana_park "The grant's monitoring won't be pleasant. It will be demanding. But if we keep the board accountable to the people who live here, it can be a way to scale this model. You did the hardest work. Now you don't have to do it alone."

    maya_serrano "I will still hold people to the same standard I always have. But I'll let them hold me too."
    "The town begins to hum with purposeful labor. Finn's crew rigs floating storage platforms that bob like obedient islands; they teach family teams how to seal valuables and anchor them. Volunteers rewire old pumps into a"
    "decentralized system that can be repaired with common tools. You finish a public protocol and send it out with a single, tremulous breath: here is what we did. Here is how you can do it too."
    # [Scene: Montage — Saltbridge over the following weeks | Various times]
    hide maya_serrano
    hide finn_serrano
    hide dr_hana_park

    scene bg ch12_f99e88_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The montage layered with phone call chimes, the clack of keyboards, a distant cheer as a test pump starts]
    # play music "music_placeholder"  # [Music: Rising strings; hope tempered with realism]
    "Other towns call. Short video windows pop up in Rosa's kitchen; municipal leaders ask for copies of your playbook. Your protocols are not perfect; they were written in the margins between sirens and tears. But they're"
    "practical, and they came with human names attached. People want templates more than speeches — step-by-step things that preserve dignity and minimize loss."

    "You write emails at odd hours, coach other organizers over cracked phone lines, and fly to a conference you never thought you'd attend to speak about the Rooftop Sanctuary model. You read about Saltbridge in an article that is careful and blunt in equal measure; the headline is not celebratory so much as pragmatic" "How Small Towns Can Buy Time."

    scene bg ch12_f99e88_7 at full_bg

    "Not everything is saved. The bookshop's paint flakes in salty hands; many of the paperbacks are ruined, swelling like injured things. You stand in the doorway and run a thumb along a wet cover. Loss sits in your bones, quiet and honest. You plant a seed in response — a seedbox of rescued books on the café shelf, with a small plaque" "We keep stories here."
    # [Scene: Rooftop Sanctuary — Early morning, weeks later]

    scene bg ch12_f99e88_8 at full_bg
    # play music "music_placeholder"  # [Music: Soft, conclusive piano with an upward turn]
    show elias_novak at left:
        zoom 0.7

    elias_novak "Did you see the message from the coastwatch in Harborview? They implemented our intake triage. They said your notes helped them lobby for funding."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "We didn't do it alone."

    elias_novak "We kind of did, though. You pushed the hinge."
    "The red thread on your wrist has been moved higher up your arm today, knotted into a small bracelet tied by Rosa on a night you finally let yourself sleep. It is a symbol that no longer demands martyrdom; it is a reminder of vows kept and shared."

    maya_serrano "Will this change things for us? For the town?"

    elias_novak "It already has. People are safer. People can sleep again without the sea in the doorway of their dreams. That's a lot. And for us... I don't know every tomorrow. But I'm here for this one."
    "You press your forehead to his, the humid rosemary between you, the dawn naming a new shore. The kiss you share this time is less a sealing of wounds and more a promise to face future"
    "tides together — not as a heroic duo but as partners who will show up with boots and lists and steady hands."
    hide elias_novak
    hide maya_serrano

    scene bg ch12_f99e88_9 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Town noises weave into a soft, confident chorus; a child's laughter threads through the scene]
    # play music "music_placeholder"  # [Music: Swells into a warm, sustaining chord]
    "The price of this shore is counted in small things — in late-night stitches on a tarp, in the bureaucratic language you fight to humanize, in the floors you decide to raise and the ones you"
    "let go. Some old places will be empty, and some people will never walk the same streets. But the town has become a network of sanctuaries instead of one fragile wall; an ecosystem of mutual aid"
    "rather than a single, brittle defense."
    "You thought leadership would mean carrying everything yourself. Instead it taught you how to redistribute weight. It taught you to convert anger into policy and grief into procedure. The work ahead is long, but the tools"
    "now exist and the people know how to use them. That knowledge, you realize, is a kind of salvation."
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "Maya! Come show the kids how to tie proper knots. Finn says your loops are legendary."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "You coming?"
    show elias_novak at center:
        zoom 0.7

    elias_novak "To tie knots? I'll watch and learn. To stay?"

    maya_serrano "Yes."
    "You are not healed. You will carry the scars of storm and of last-minute choices for the rest of your life. But the town breathes differently now — intentionally, with plans that respect memory and necessity."
    "The Rooftop Sanctuary is no longer an emergency contraption; it's a prototype of a better, fairer adaptation."
    hide rosa_alvarez
    hide maya_serrano
    hide elias_novak

    scene bg ch12_f99e88_10 at full_bg
    "You touch the silver, feel its familiar weight. The compass no longer feels like an accusation. It feels like a tool that points not to the single true north of sacrifice but to a horizon you can walk toward with others."
    "When you stop to imagine the future — not neat, not painless — you see people teaching each other how to re-tie lines, how to patch solar fabric, how to read a weather forecast and plan"
    "a child's school commute around a tide chart. You see new apprenticeships and a neighborhood fund that pays for relocation costs out of a town trust. You see the bookshop turned into a reading room above"
    "tide levels, shelves reclaimed and stories rehoused. You see, most of all, a community that decided together what to keep and what to let go."

    scene bg ch12_f99e88_11 at full_bg
    # play music "music_placeholder"  # [Music: A final, bright chord that lingers warmly]
    "This is not the shore you remembered. It is not the shore you mourn. It is the shore you and forty-seven others, and then more, negotiated into being. It cost you sleep and old storefronts and a way of imagining safety. It bought you something else: an architecture of care."
    "You think of the neighbor whose porch light went dark years ago. You tell their story often, not as a martyr's tale but as a call to keep building, keep shifting, keep loving in ways that"
    "include policy and plumbing and gossip shared over coffee. You are tired, yes. But your exhaustion is braided with purpose. The thread on your wrist doesn't cut anymore; it ties."
    "You close your notebook and feel, for the first time in a long while, that the pages will hold more than lists of losses. They will hold instructions and names and a stubborn kind of hope that refuses to be simple."

    scene bg ch12_f99e88_12 at full_bg
    # play music "music_placeholder"  # [Music: Fade Slowly]

    scene bg ch12_f99e88_13 at full_bg
    "THE END"
    # [GAME END]
    return
