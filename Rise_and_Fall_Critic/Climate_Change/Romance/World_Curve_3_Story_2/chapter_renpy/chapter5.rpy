label chapter5:

    # [Scene: Your Apartment | Night / Early Morning]

    scene bg ch5_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, tremulous cello; distant percussion like distant surf]
    # play sound "sfx_placeholder"  # [Sound: A single phone buzz; the rustle of paper as you flip a page]
    "You wake with the memory of rain hammering across the roof—too close, too familiar. Diesel still tastes like iron at the back of your throat. Your weatherproof notebook lies open on the table, edges curled with"
    "saltwater, contractual redlines on the right-hand page and neighbor petitions folded into the left. The compass at your throat is cold against your collarbone."
    "You fold the notebook closed because you can't look at both halves of the page at once. Closing it feels like pressing two wounds together and hoping they knit. You can hear the city breathing: a"
    "generator chugging two blocks away, someone calling a dog, an engine trying to start under drizzle. Somewhere a crane groans like an animal."

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Phone vibration — a short, insistent stutter]
    "You answer before you think."
    show professor_anika_bhat at left:
        zoom 0.7

    professor_anika_bhat "Mara. You're up early."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Couldn't sleep. I— (your voice is low, half-drowned by the rain) —I read your note. What do you think?"

    professor_anika_bhat "I think models are only as honest as the constraints you give them. If the contract has no enforceable oversight, everything you call 'pilot' becomes a sticker slapped on a seawall.' (She pauses, the hum of her kettle faint in the background.) 'Legally binding oversight isn't bureaucratic theater. It's the thing that keeps the barrier from being a monument to the wrong kind of convenience."
    "You swallow. Her words hang like wet laundry between you and the window."

    mara_lin "The mayor wants signatures by morning. The contractor's counsel said any delay risks funds being reallocated. If we push for binding language and they walk, there might not be a seawall at all."

    professor_anika_bhat "Then don't let them confuse scarcity with inevitability. The question isn't whether you can get a wall up quickly. It's who the wall is for, and whether it will respect the communities it claims to protect. If your oversight clause is real—audits, community veto points, transparent reporting—you're not asking for perfect speed; you're asking for accountability."
    "You feel the old reflex: list and qualify, map the trade-offs. You're a practical idealist; you live in margins and margins of margins. But tonight margins feel like cliffs."

    professor_anika_bhat "Mara, listen: models will hold water if you bind oversight. Otherwise, you'll hand them a license. If you think the choice is between action and inaction, you're being browbeaten. There are other paths. I'm not asking you to pick the perfect one. I'm asking you to not sell the people out."

    mara_lin "And if insisting destroys the funding—if homes flood while we argue?"

    professor_anika_bhat "Then you will be accountable to them for your choice. But you will also know that your choice was made in the open, with their involvement. That means something."

    menu:
        "Promise Anika you'll push the oversight clause hard":
            "You tell Anika you will fight to write oversight into the contract. Her voice softens, almost relieved; she says she will draft legal language by dawn and reminds you to get witnesses from the neighborhood."
        "Tell Anika you'll weigh the speed risk and call back":
            "You tell her you need to see the mayor's reply first. She presses, then concedes with a sigh, 'Don't make this a moral shortcut, Mara.' The line clicks; you are left with the vertigo of delay."

    # --- merge ---
    "You fold back into the silence of your apartment after you hang up. The compass is still warm where it touched your skin. You stare at the window until the rain becomes a smear and then"
    "a memory. Outside, a faint sound of chanting begins to rise—someone else in the city making a claim in the night."
    # [Scene: Tideward Rooftop Garden | Early Dawn]
    hide professor_anika_bhat
    hide mara_lin

    scene bg ch5_4001e7_3 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano notes; the sound of distant voices like gulls]
    # play sound "sfx_placeholder"  # [Sound: The rustle of tarpaulin, the steady hum of bees in a sheltered planter box]
    "You climb the iron stairwell to the garden and find Nova Duarte on the highest terrace, legs tucked under her, a small encampment of sleeping bags and banners behind her. She has staged a sit-in; her"
    "painted megaphone lies within reach like a promise. A damp sprig—one of the ones she shoved at you earlier—sits on the planter rim, dark green and stubborn."
    "Nova Duarte: (without looking up) 'I figured you'd show before the city signed the paper that sells our streets.'"
    "You feel your chest tighten. People have been watching; a half-dozen neighbors huddle nearby, faces drawn in the thin light. Nova's steel-gray eyes find yours finally—raw and unreadable in ways that could mean accusation, grief, or an invitation to join the fury."
    show mara_lin at left:
        zoom 0.7

    mara_lin "Nova. I—"
    "Nova Duarte: (cutting in) 'You sat at a table with people who build things and call them solutions. You put your name next to redlines and clauses that no one in my community read because they"
    "were too busy bailing water out of their basements.' (She lets the words land.) 'Did you know the contractor's team have been lobbying for that timeline for months? Did you know the mayor wants a 'visible'"
    "win before the election calendar?'"
    "You taste salt and something like anger. You can feel the seawall project like a jawbone under the city—necessary, structural, but heavy."

    mara_lin "I insisted on insertions. I tried—"
    "Nova Duarte: (laughing, but the sound is brittle) 'Insisted? Mara, insistence is not a guarantee. It's a start. Did you make oversight legally binding? Did you secure community audits? Or did you hand them a timeline and hope goodwill would fill the gaps?'"

    mara_lin "I pushed for clauses—"
    show nova_duarte at right:
        zoom 0.7

    nova_duarte "You 'pushed' when they were already moving. Sometimes 'pushing' looks indistinguishable from letting them get away with speed.' (Her voice softens, almost a plea.) 'Tell me you didn't do that because you love being at the table. Tell me you did it because you thought you could change the menu."

    mara_lin "I thought both things. I thought—' (the sentence unravels) 'I thought getting something up fast would stop the next storm from taking more. I couldn't sleep imagining them getting out there without any structure in place."
    "Nova stares at you, an unreadable map of hurt and calculation."

    nova_duarte "People are not problems to be solved on a speed-boat. We're people who need a voice."

    mara_lin "I know that. I do."

    nova_duarte "Then show me. Don't tell me with words—show me with paper I can read, with audits I can touch, with veto points I can appeal to."
    "You hang back. You feel the old instinct to step forward and fix things; but every time you move toward the machinery the movement tastes like compromise."

    menu:
        "Approach Nova and kneel to meet her eye level":
            "You step down and lower yourself to Nova's level. For a moment the crowd exhales. Nova's shoulders tense; then she gives you a small, almost imperceptible nod — a fissure, not full mending."
        "Stand and keep your distance, hands in your pockets":
            "You stay standing. Nova's eyes harden; someone nearby shifts closer to her as if to shield. The distance feels like armor and also like a wall between you and the people you claim to fight for."

    # --- merge ---
    "Nova looks at you like she's measuring the weight you carry, the promises you've kept and those you haven't. Her stare is complex — a mirror without clarity."

    nova_duarte "Whatever you do, don't make our trust a bargaining chip. If they call you a pragmatist, make sure it's because you are practical for the people, not for paperwork."

    mara_lin "I won't—"

    nova_duarte "People are cold now, Mara. They don't have the luxury of your 'maybe'.' (She leans forward, voice low.) 'Don't clasp their futures with fingers crossed."
    # [Scene: Solace Harbor Market | Mid-Morning]
    hide mara_lin
    hide nova_duarte

    scene bg ch5_4001e7_4 at full_bg
    # play music "music_placeholder"  # [Music: A low, agitated string ostinato; market chatter like a distant tide]
    # play sound "sfx_placeholder"  # [Sound: The slap of wet canvas; a child laughing and then abruptly quiet as she watches you]
    "Samir Reyes stands behind his stall, hands wrapped around a steaming cup, the smell of fried bread blending with wet seaweed. The market smells like history—frying oil, salt, lemon peel—and the present, too: diesel, wet cardboard,"
    "the ghost of machinery. He has known you since you were small enough to hide among crates."
    "Samir Reyes: (voice brittle) 'Did we trade our past for a promise?'"
    "The question lands like a stone in a pond. You look down at your hands—salt-sticky, ink-stained where you've been annotating clauses—and the compass pendant at your throat. You think of the teenager you once were, standing on Samir's stoop after the storm, gloves full of salvaged things."
    show mara_lin at left:
        zoom 0.7

    mara_lin "I didn't want to see another night like that. I thought—"
    show samir_reyes at right:
        zoom 0.7

    samir_reyes "You thought they'd listen if you were inside the tent. You thought the tent made you safe.' (He smiles, but it cracks.) 'Inside the tent, they measure things in timelines and profit margins. Outside, we measure things in roofs and graves."

    mara_lin "I added names. I tried to fold community oversight into their drafts."

    samir_reyes "Added names. That's small comfort. Nova says you sat at the table with a sprig and a smile. People want real power, not postcards."

    mara_lin "What do you want me to do, Samir? Walk away and let the city pick whoever wants to run a machine? Tell me what you want."
    "Samir opens his hands, showing callused palms. A small child tugs at his sleeve; he ignores it and looks at you, exhausted."

    samir_reyes "I want you to be the person who remembers everyone. I want you to put their names where they can be read. I want you to make it so an audit isn't a polite suggestion."

    mara_lin "I hear you. I—"

    samir_reyes "I know you do. Don't make us ask for a miracle because you couldn't fight for a clause."

    mara_lin "I'm trying to be practical. If we delay, that could mean money goes elsewhere. If the barrier doesn't get built, people drown. That's—"

    samir_reyes "—a gamble where other people's lives are the chips. Remember who taught you how to tie boots in that flood. Remember why you came back."
    "You close your eyes. The memory is sharp: water up the stairs, Mrs. Ebbett crying over a lost radio, your own small hands gripping a railing. Guilt is a constant tide, a force with no mercy."

    menu:
        "Offer to bring Samir the draft oversight language for his group to review":
            "You promise to deliver the draft oversight language and ask for his group's signatures. Samir nods slowly, a crease of hope appearing and then fear."
        "Deflect the question with the mayor's deadline":
            "You point out the mayor's deadline and talk about reallocation risk. Samir flinches as if struck; trust thins another millimeter."

    # --- merge ---
    "Samir folds his hands around his cup. The market hums on, indifferent to the small catastrophes being negotiated under stretched tarps."
    # [Scene: Sea Barrier Construction Site | Midday]
    hide mara_lin
    hide samir_reyes

    scene bg ch5_4001e7_5 at full_bg
    # play music "music_placeholder"  # [Music: Percussive industrial beat; a low horn in the distance]
    # play sound "sfx_placeholder"  # [Sound: Diesel engines, the squelch of boots in mud, the metallic clank of a container being winched]
    "You stand at the edge of the construction site with your notebook in your hand and the paper contract in plastic protective sleeves. The contractor's foreman—broad-shouldered, competent—has his tablet out. His team is patient but expectant like people waiting to be paid."
    "A city aide stands with a phone to her ear. The mayor's voice is not in the room, but her presence feels like a shadow: a reminder of timelines and press."

    "Contractor Foreman" "We need a signature tonight. Our mobilization costs go up if we delay. The bond schedule shifts. We can stick to the design you want, but we need commitment.' (He taps the tablet; schematics ripple across the screen.) 'We're not being the villain here. We're offering you certainty."
    "You can smell diesel and the iron tang of wet earth. Puddles reflect the scaffolding like broken teeth."
    "Mayor Heloise Chen: (over the phone; calm, corporate) 'Mara, the city can't afford indecision. The grant hinges on demonstrable progress. Can you sign this evening? We need to show movement.'"
    show mara_lin at left:
        zoom 0.7

    mara_lin "Movement—yes. But movement without oversight becomes a story where the city's interest overrides the neighborhood's. I need language in the contract that guarantees community audits and oversight reporting."
    show mayor_heloise_chen at right:
        zoom 0.7

    mayor_heloise_chen "Who will pay for the audits? Who will certify impartiality? We cannot insert veto powers that paralyze contractors. We need something that passes muster with the funding board."
    "Professor Anika's words float up through your memory like a tide: not a sticker, but a binding mechanism. Your finger traces the margin of the redlines. You can feel the weight of two futures in the same breath."

    "Contractor Foreman" "Look, Madam Lin, we have timelines and a budget. Audits can be part of project reporting. Vetoes and halting clauses are high risk. If the funding board sees too many conditional points, they pull the plug."

    mara_lin "What if we agreed to phased sign-offs? We sign the initial mobilization to secure funds, with a legally binding schedule of community audits tied to milestone releases. If audits fail, contingency funding shifts to remediation rather than contractor profit."
    "Mayor Heloise Chen: (a small, practiced pause) 'Phased disbursement models are complicated, and often slower—'"

    "Contractor Foreman" "—and they cost money to administer."

    mara_lin "They cost less than lost trust."
    "There's a ripple in the crowd at the site's perimeter. Nova's rooftop sit-in has a small contingent present; Samir stands at the fence with coat collar up, his face set like flint. Their faces are complex—compressed into expressions that mean many things at once."
    "You feel every tendon in your neck like a chord ready to snap. The city wants certainty; the community wants voice. Your notebook is a battleground of ink and paper and people."

    mayor_heloise_chen "We can have lawyers put language together for a phased model, but we need a yes to submit tonight. The window for the grant closes at midnight. Without your signature, I cannot promise funding."
    "You look at the contract: clauses you have already negotiated, clauses you still can't breathe around. The contractor waits politely, a machine of task and calendar. Nova's eyes from the garden are not accusatory so much as questioning, like a pendulum measuring weight."
    "You feel the ancient and terrible animal feeling—responsibility. The compass at your throat is suddenly heavy as lead."
    "This isn't only bureaucratic. It's personal. If I insist on oversight, funding might be delayed and neighborhoods could be in immediate danger. If I sign quickly, I betray the trust of people who believed you would"
    "fight for them. If I try to stitch a middle path, I ask everyone to trust in a delicate rope bridge."
    hide mara_lin
    hide mayor_heloise_chen

    scene bg ch5_4001e7_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rain starts again, slow, an accusatory metronome]
    "You look up. The contractor clears his throat. The city aide flips through the packet with a professional, bored urgency. Nova lifts a hand as if to signal. Samir's jaw is set."
    # play music "music_placeholder"  # [Music: Strings tense into an unresolved cluster]
    "You breathe. You can already hear the room forming the shape of your answer in the way people lean toward you or away."

    menu:
        "Insist on legally binding community oversight before signing.":
            jump chapter6
        "Sign the expedited contract to ensure immediate protection.":
            jump chapter13
        "Negotiate a phased sign-off with pilot community audits to appease both sides.":
            jump chapter6
    return
