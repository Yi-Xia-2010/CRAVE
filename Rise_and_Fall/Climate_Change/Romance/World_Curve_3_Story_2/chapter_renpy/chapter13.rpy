label chapter13:

    # [Scene: Rooftop Community Garden | Early Morning]

    scene bg ch13_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Gentle piano arpeggio; gulls calling distantly]
    # play sound "sfx_placeholder"  # [Sound: Soft scrabble of footsteps on gravel, a kettle murmuring on a propane burner]

    "You arrive before most of them, notebook tucked under your arm, fingers cold from the morning air. The rooftop smells of wet earth and seaweed compost—sharp, alive. Mist threads between the plants; tiny droplets bead on the lettuce like glass. Marina is already here, hair plaited with the same seashell she wore as a child, moving with the careful authority of someone who roped children to projects for a living. She hums under her breath as she pins up a new poster" "Co-Manage Our Shoreline — Kids, Elders, Builders, Scientists."
    "You breathe in. The rooftop is small and bristling with possibility. This is where the town's life and your plans finally touch—where the public and the practical meet under the same gray sky. You remember why"
    "you chose patience here: because trust cannot be built from a single check in a grant. It grows when people plant together, when hands learn the rhythm of oysters and pilings and policy."
    show marina_lopez at left:
        zoom 0.7

    marina_lopez "They sent twelve kids from the school. The teachers brought gloves. Kenji's rolling in with the sediment cores for the demonstration. How are you holding up, Amina?"
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "Nervous the way you get before a storm, but ready. We planned this the right way."

    marina_lopez "Good. We'll show them what 'the right way' looks like."
    "A group gathers—parents with thermo flasks, an old boat captain with a weathered cap, the teenage son of a café owner clutching a camera. Conversation folds in and out between people swapping small salvage tips and"
    "the bigger talk about grants and co-management. You set out a small table: oyster spat, a stack of your notebook pages with a cross-section sketch, and a sign-up sheet for community monitors."
    "You speak. Your voice is low but clear; you can feel the memory of the boardwalk and the ache for your brother behind each word, and you let that history give rather than take."

    amina_reyes "This is an experiment in respect. We will measure. We will learn. We'll make mistakes and correct them together. No machines show up without a neighborhood agreement. No designs go ahead without someone in the boatyard saying they can repair it."
    "A woman at the edge nods, eyes shiny. A man mutters about 'too much talking.' You let the fragility and the friction both occupy the space—trust is a messy, human business."

    menu:
        "Let Marina open the demonstration":
            "You step back and let Marina take the first words. She tells the children how oysters filter water and why the marsh is a living sponge. You watch their faces, and the trust you wanted starts as a small, bright thing in the crowd."
        "Take the demo yourself and show the cross-section":
            "You unroll your notebook and point to the scalloped sluice. Your hands shake a little—then steady. The kids press closer, fascinated; an elder asks a sharp, practical question that you answer, and your words land in real time, not on paper."

    # --- merge ---
    "The demonstration concludes and the day's work continues with the group organized and engaged."
    # [Scene: Niko's Boatyard | Late Morning]
    hide marina_lopez
    hide amina_reyes

    scene bg ch13_601bcb_2 at full_bg
    # play music "music_placeholder"  # [Music: Wooden percussion strings; a hopeful cadence building]
    # play sound "sfx_placeholder"  # [Sound: Hammer tapping, a radio murmuring sea shanties, rope creaks]
    "The boatyard is all warmth and noise—Niko Kaur at the center of it, hands raw, eyes alert. They look up when you come in, wiping their palms on the back of their trousers."
    show niko_kaur at left:
        zoom 0.7

    niko_kaur "You brought the kids up there? Good. If a plan's going to stick, it needs people who'll inherit the damn thing. Too many projects die because they're not loved."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "They planted oysters. I showed the cross-section. Marina did a great job getting the teachers to bring the kids."

    niko_kaur "That's how you start. You get people in the mud, not on a checklist."
    "Kenji walks in behind you, sunhat tilted, carrying a small data tablet and a printout of a graph that looks like a weathered mountain range."
    show dr_kenji_sato at center:
        zoom 0.7

    dr_kenji_sato "The cores confirm the adaptive capacity in the lower marsh if we allow certain sediment flows. We can design living shoals to dissipate wave energy—if we avoid the heavy engineering in sensitive zones."
    "Niko Kaur snorts lightly. 'If you keep talking like that, Kenji, folks will think you're trying to sentence them to a seminar.'"
    "Dr. Kenji Sato smiles. 'I am trying to keep them alive, Niko. Different linguistics, same end.'"
    "You set the printouts on a workbench. The boatyard becomes another classroom: you, Niko Kaur, Dr. Kenji Sato, a handful of apprentices who learn as they shape wood. The apprentices' hands are callused in the right"
    "places. You teach them to read your sketches, and they teach you practical shortcuts—where a threaded brass pin will save a hatch."
    "Elias Hart arrives by the time the apprentices begin to line up. He ducks under a low beam, coat still damp from travel. His expression is careful but warm when he sees you. He moves through"
    "the space with the sort of quiet competence that once felt like an obstacle; now it feels like another tool."
    hide niko_kaur
    show elias_hart at left:
        zoom 0.7

    elias_hart "How are things here? The footage from this morning is…good."

    amina_reyes "It's honest. People are doing the work. We're not promising miracles overnight."

    elias_hart "I told the regional office that my funding proposal needed those conditions—co-management language. They balked until they saw the footage of volunteers. Your images did that."
    "You look at him—part gratitude, part the old friction that taught you to check your assumptions."

    amina_reyes "You pushed them. You kept asking for those stipulations in meetings."

    elias_hart "You kept insisting we wait and build trust. Together, we made this a requirement, not an afterthought."
    "The conversation is careful, multi-layered—questions and answers looping back, clarification and mutual recalibration. It is not a tidy reconciliation; it's commerce between two different kinds of faith. You push: how will regional audits respect local labor"
    "rates? He answers: clauses in the contract will require community boards sign off. You ask: how do we prevent tokenism? He replies: independent monitors and transparent reporting."
    "Niko Kaur watches all this with an unreadable expression. Then their face softens when you look to them, and an old solidarity returns."
    hide amina_reyes
    show niko_kaur at right:
        zoom 0.7

    niko_kaur "So we build, they fund, and we keep the right to say no to what feels wrong. Fine. But I'm not having machines pull up a reef without someone here who knows how to fix it after."
    "Elias Hart: (light, but firm) 'Agreed.'"

    menu:
        "Ask Niko to lead the pilot crew":
            "Niko accepts with a single curt nod and then starts assigning tasks like it's always been their right. The apprentices light up at being trusted, and the boatyard hums with purposeful noise."
        "Volunteer to oversee the monitoring protocols and reporting":
            "You take the monitoring plan and start writing names by each task. The apprentices look to you for leadership, and you feel the old ache and a new steadiness sit side-by-side."

    # --- merge ---
    "The team organizes around the chosen roles and the pilot work begins."
    # [Scene: Town Square | Early Afternoon — Viral Campaign Montage]
    hide dr_kenji_sato
    hide elias_hart
    hide niko_kaur

    scene bg ch13_601bcb_3 at full_bg
    # play music "music_placeholder"  # [Music: Swelling strings turning from question to resolve]
    # play sound "sfx_placeholder"  # [Sound: Notification pings layering into a chorus, then settling into a steady hum]
    "Your phone vibrates. One share. Then ten. Then a thousand. Marina's photographs—children with muddy knees, your sketches laid beside seedlings—begin to thread through social channels. The images are simple and impossible to ignore: the humanity of"
    "work, the science made legible by a child's curiosity. A local news feed picks it up. An environmental nonprofit amplifies it. The regional office, which had been cautious, now faces a public story that demands a"
    "different kind of answer."
    "You feel the odd, vertiginous mix of exposure and validation. The viral spread is not vanity; it puts pressure where pressure must be useful. The grant language shifts almost immediately—what had been vague funding for 'coastal defenses' now reads 'long-term living-shoreline grants requiring demonstrable co-management and cultural protections.'"
    "You find yourself at a regional meeting a week later, standing with Elias Hart and Mayor Lucia, Dr. Kenji Sato's model projected on the wall. The room smells faintly of institutional coffee and paint—bureaucracy made tactile."
    show mayor_lucia_varela at left:
        zoom 0.7

    mayor_lucia_varela "We need a model that can be replicated, but not one that erases the place it's meant to protect."
    show elias_hart at right:
        zoom 0.7

    elias_hart "The revised proposal includes explicit clauses—local employment quotas, co-governance boards, periodic audits with community ratification."
    "Dr. Kenji Sato: (pointing) 'My long-term projections show lower net habitat loss under a living-shoreline approach, and with staged retrofits, we can preserve critical marsh connectivity while protecting built infrastructure.'"
    show amina_reyes at center:
        zoom 0.7

    amina_reyes "And the monitoring protocol has community monitors at its heart. We teach, we learn, we course-correct. We don't let engineers write the last word about a living place."
    "A councilperson frowns, skeptical about the cost. Mayor Lucia leans forward and speaks with the quiet steadiness of someone who remembers campaigning on this town's name."

    mayor_lucia_varela "Marisol will staff the oversight. We will teach the paperwork like we teach a child to tie a knot. Bureaucracy is a skill. We'll learn it."
    "There is a small, electric pause—in the air, you can feel the culmination of months of patience and pushing. The room decides, not by a dramatic gesture, but by a shift: the funding is restructured. The"
    "grant will be long-term; it will include apprenticeship lines for boatwrights and a clause that regional funds cannot be disbursed without signed agreements from co-management boards."
    "You exhale like someone released from a held breath."
    # [Scene: Montage — Months Passing | Various Times]
    hide mayor_lucia_varela
    hide elias_hart
    hide amina_reyes

    scene bg ch13_601bcb_4 at full_bg
    # play music "music_placeholder"  # [Music: Warm strings and woodwinds; each phrase lifts more confidently]
    # play sound "sfx_placeholder"  # [Sound: Waves softened by new shoals, laughter, the creak of a well-maintained hull]
    "Change arrives like weather—persistent, layered, sometimes slow enough to make you doubt. Homes are retrofitted; electricians learn solar microgrids; fishermen adapt nets and routes. Some businesses struggle and are supported into new roles: a net mender"
    "becomes a community monitor, a café owner hosts training nights. The town learns to fill out forms without surrendering to them. The apprenticeship program starts producing skilled hands who can both build a quay and read"
    "a tide chart."
    "There are losses—an old pier that could not be saved is taken down, and a family decides to move. You mourn privately; you mark it in your notebook like a footnote to the plan. But the"
    "losses are not the only story. The marsh begins to show signs of recovery where living shoals were seeded; birds return in numbers that have the whole town commenting."
    "You find your name on the plaque at City Hall: Amina Reyes, Chair, Marisol Adaptation Council. Your chestnut hair has a few gray threads at the temples—small, honest ribbons that the salt air has brought out"
    "earlier than you expected. The pendant at your throat, solar-charged and tethered to old ritual, hums faintly against your sternum when a storm passes nearby; it's a small, comforting vibration, like the town itself taking a"
    "reassuring breath."
    # [Scene: Niko's Boatyard | Twilight]

    scene bg ch13_601bcb_5 at full_bg
    # play music "music_placeholder"  # [Music: Quiet guitar harmonics; warmth under the cooling air]
    # play sound "sfx_placeholder"  # [Sound: Distant calls of night birds; a soft laughter between you]
    "Niko Kaur sits beside you on a bench, oil-smudged hands cupped around a mug. There is an easy silence that has no need to be filled anymore—the work has made the space for it."
    show niko_kaur at left:
        zoom 0.7

    niko_kaur "You look like you belong on that plaque."
    "Amina Reyes: (laughing softly) 'I look like I age in public. Is that a bad thing?'"

    niko_kaur "No. It suits you. You look…steady. Like someone who can keep a reed bed from sliding into the water."
    "You lean into them for a fraction longer than either of you planned. There is a history in that small touch—shared grief, shared labor, a hundred scaffolding conversations—but now it's less raw and more tempered."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "I didn't get here alone."

    niko_kaur "No. You had stubbornness, friends, and a lot of paperwork."
    "You both grin. They bump your shoulder with theirs—an old motion of affection that has no need for grand vows. It's tentative, steady, and true to the work you both do."
    # [Scene: Town Hall | Morning]
    hide niko_kaur
    hide amina_reyes

    scene bg ch13_601bcb_6 at full_bg
    # play music "music_placeholder"  # [Music: Low hopeful brass; a subtle, uplifting swell]
    # play sound "sfx_placeholder"  # [Sound: Pages turning; a distant bell from the market]
    "Elias Hart is here to present the first matched funding tranche. He moves with the same practiced calm; in his eyes you see the patient respect that develops when two people fight on the same side for different reasons and learn to value both."
    show elias_hart at left:
        zoom 0.7

    elias_hart "Regional offices want this replicated. They asked for a model that balances technical rigor and cultural safeguards. You built that."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "We built a process. A process is easier to copy than a feeling, but it needs people willing to translate it to their place."

    elias_hart "And you've taught them to speak that language."
    "He folds his hands, a map of the future spread between you. There is gratitude in his voice, and something else—a promise to keep listening."

    elias_hart "I'll keep pushing at the policy level. You keep teaching people to tend the marsh. We'll check in. We'll keep the clauses that matter."

    amina_reyes "And you'll remind them that funding without co-management is just a fancy levee."
    "Elias Hart: (laughs softly) 'Deal.'"
    # [Scene: Marisol | Sunset — The Town as a Whole]
    hide elias_hart
    hide amina_reyes

    scene bg ch13_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: Choir-like strings resolving into a gentle major chord]
    # play sound "sfx_placeholder"  # [Sound: The sea, softened now in its music by the restored shoals; children's distant voices]
    "You walk the boardwalk at dusk, the town breathing around you. The market lights are on. Marina organizes a patchwork of volunteers for a public reporting night. Dr. Kenji Sato sets up a portable display for"
    "his long-term monitoring. Mayor Lucia greets a pair of visiting planners who ask more attentive questions than the old version ever did."
    "It is not perfect. There are still arguments at the council table, and bureaucratic forms still smell like compromise. Some of the older docks are permanently altered. Jobs changed. But people are learning to make those changes with intention."
    "You stop at a small inlet where the new shoals thicken the water's edge. An oyster bed glints. A juvenile heron takes off in a slow, accusing flap. You touch the soft, salted wind on your"
    "face and feel the steady thrumming of your pendant at your throat—an old talisman now repurposed into a badge of vigilance."
    "Niko Kaur meets you there, hand finding yours without a ceremony. You walk a few paces together, footing and conversation easy, the kind that builds futures out of every small ordinary decision."
    "You think of your brother. You think of the nights when doubt almost finished you. The ache is still there—an honest indentation in your chest. But now it sits alongside a growing confidence: people can learn"
    "bureaucracy; people can rebuild livelihoods; people can love a place enough to fight for it patiently."
    "Mayor Lucia appears at the end of the boardwalk, a small crowd around her as she gives a short speech about resilience and responsibility. You listen—she mentions apprenticeships, co-management, matched funding, and the town's role as"
    "a living laboratory. She smiles at you when your eyes meet, and in that glance there is an acknowledgment: this was not a triumph of any single person, but of a town learning to be a"
    "town again."
    "You close your notebook. The friendship bracelet tucked into its spine is frayed but intact. You run your thumb over the threads, and below it you feel the small, steady warmth that has nothing to do"
    "with heat—the kind of warmth that comes from being seen, from being part of an ongoing, imperfect answer."

    scene bg ch13_601bcb_8 at full_bg
    # play music "music_placeholder"  # [Music: Full strings resolving; a single, hopeful piano note lingers]
    "You have taken a public leadership role, yes—but more than titles, you have a council where residents learn to steer. Niko Kaur stands beside you in ways both intimate and mundane. Elias Hart keeps knocking on"
    "the doors of policy and funding, now a partner rather than an adversary. Dr. Kenji Sato's models continue to teach you how to listen to the slow language of ecosystems. Marina's children will carry oyster shells"
    "as a kind of liturgy."
    "Marisol becomes, in the way that matters, a model—not of perfection, but of patient, flawed endurance. You watch a small boy hand a planted oyster to an old boat captain who smiles in a way that makes you feel the architecture of trust rebuilding."
    "You feel hope like an honest weather system now—visitable, predictable in its unpredictability, and capable of being prepared for."
    # play music "music_placeholder"  # [Music: Piano and strings soften to a single sustained chord]

    scene bg ch13_601bcb_9 at full_bg

    scene bg ch13_601bcb_10 at full_bg
    "THE END"
    # [GAME END]
    return
