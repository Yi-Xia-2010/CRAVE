label chapter10:

    # [Scene: Town Hall Plaza | Late Afternoon]

    scene bg ch9_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gull calls, a steady murmur of passing conversations, the soft scrape of a folding chair]
    # play music "music_placeholder"  # [Music: Warm, ascending strings — hopeful and steady]
    "You stand beneath the overhang where the town's shadow falls long and patient. You can feel the choice you made in Chapter 8 settle into your bones: you chose to work closely with Eli, to shape"
    "engineering with ecology rather than seeing them as opposed. It has guided how you breathed through the last frantic week and who you trusted to sit across a table with you when the papers got heavy."
    "The developer's legal notice sits folded in the crevice of your jacket pocket, its edges softened by the sweat of long hours. You don't pull it out. Instead you watch people arranging chairs for the oversight"
    "committee meeting and listen — because the town's rhythms still tell you more than any line item."
    show rosa_kwan at left:
        zoom 0.7

    rosa_kwan "You look like you need this. We made sure Hal had a seat by the window."
    show amara_vale at right:
        zoom 0.7

    amara_vale "Thanks. Has Miriam arrived?"

    rosa_kwan "In a flurry. Typical Miriam. She's already sorted the speakers."
    "Hal's presence is a slow two-beat comfort: he walks with a careful shuffle, sweater patched in places where salt took its toll. When he nods at you, there's a whole history in that small motion — past storms, past failures, past nights with blueprints spread and hands tired."
    show harold_hal_finnegan at center:
        zoom 0.7

    harold_hal_finnegan "Make the safeguards clear,' he says, fingers folding over each other. 'Make them real, not platitudes."
    "You nod. Your voice comes softer than you expect, but anchored."

    amara_vale "We make enforceable oversight. A maintenance endowment. Rehousing budgets earmarked before construction begins. No one is moved without a plan."
    "Elias 'Eli' Navarro arrives last — the way he does, as if a problem were a thing to be taken apart and arranged into something that fits. His satchel smells of blueprints and coffee; a brass"
    "compass glints at the seam. He looks at you with an expression that is at once tired and wry, like the sea after a long wind."

    "Elias 'Eli' Navarro" "You look like you handcrafted a clause in your sleep."

    amara_vale "Maybe I did. Or maybe I read too many legal diagrams."

    "Elias 'Eli' Navarro" "Either way, we'll make sure 'maintenance' isn't a word that disappears. I ran the numbers again — phased funding plus an indexed endowment. It holds."
    "Your chest lightens. Numbers don't fix everything, but they make promises keepable."
    hide rosa_kwan
    hide amara_vale
    hide harold_hal_finnegan

    scene bg ch9_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rustle of paper, the scratch of a pen]
    "Miriam arrives like a wind of motion: teal hair tucked under a practical cap, megaphone slung over her shoulder though today it's a planning instrument more than a trumpet. She lays out a folder of community"
    "testimonies — people who will be affected, names you know, faces that anchor the clauses in a way a lawyer never could."
    show miriam_santos at left:
        zoom 0.7

    miriam_santos "If this is a hybrid, community seats on the oversight board have to be binding. Not advisory. Binding."
    "Marco Voss stands apart initially, his blazer a sharp line against the casual roundness of the committee. His presence tastes like expectation and possibility — like money that can, if used right, do good fast. He offers a smile that is practiced, then genuine enough."
    show marco_voss at right:
        zoom 0.7

    marco_voss "We're on the same page about speed. I can guarantee capital will be available for the pilot seawall right away, and the restoration corridors can be part of the same funding package."
    "Your mind catalogs his words even as something in your chest checks them: speed has a history in Seabright of bulldozers and promises without route maps. You look to Eli; his jaw tightens for half a"
    "beat and then smooths. He stands beside you not as an echo but as a partner."

    "Elias 'Eli' Navarro" "Speed only matters if there's a map for upkeep. Marco, we need contract language that creates a community trust, with binding maintenance schedules, independent auditors, and a rehousing escrow before work begins."
    "Marco Voss's smile doesn't vanish, but his eyes sharpen in a way that makes you proud of Eli's steadiness."

    marco_voss "I can accept an independent oversight board — with representatives from the community, technical experts, and an industry seat. The funding will include an endowment. Rehousing will be a line item. But timelines matter. We move on a firm schedule."
    show harold_hal_finnegan at center:
        zoom 0.7

    harold_hal_finnegan "And what about recall mechanisms? If the firm's plans harm neighborhoods or break terms?"

    marco_voss "Recall mechanisms are reasonable if they are fair. No one wants litigation to stall the wall when the tide is at the door."
    "You inhale the salt-heavy air. The negotiation is a dance: words, legal scaffolding, trust by increments. There is friction — as there should be — but the room's tone has shifted from confrontation to construction. In this, you feel the lift of collective intention: people leaning into shared work."

    menu:
        "Check the draft schedule":
            "You skim the projected timeline, eyes catching the milestones Eli highlighted in faint pencil. The dates nest comfortably with maintenance review periods; it's pragmatic, not rushed."
        "Read the rehousing clause aloud":
            "Your voice careful, you read the rehousing paragraph. Names, processes, escrow amounts. Listeners nod; the clause lands as a promise that must be kept."

    # --- merge ---
    "The narrative continues from the following paragraph, reflecting the chosen action."
    "You choose to read the rehousing clause aloud because words mean more when they are heard. Miriam's hand presses against her folder like a talisman. Rosa's smile loosens; something like relief crosses Hal's face. Marco's fingers drum the table — not impatience, but thoughtfulness."

    marco_voss "The rehousing escrow — I want to see milestones tied to release, not only completion. We can build in phased releases as families are rehoused into local units or temporary housing — it's in everyone's interest to avoid displacement."

    "Elias 'Eli' Navarro" "We'll define escrow triggers collaboratively: occupancy, inspection, and verifiable rehousing plans. Releases contingent on audits and community sign-off."
    hide miriam_santos
    show amara_vale at left:
        zoom 0.7

    amara_vale "Community sign-off is non-negotiable. And the oversight board will have teeth — veto power over contract amendments that alter maintenance funding or rehousing commitments."
    "There is a tension you had practiced for nights: to demand teeth without sounding punitive. Miriam slams a palm gently to the table, the movement precise."
    hide marco_voss
    show miriam_santos at right:
        zoom 0.7

    miriam_santos "We need a transparent complaints process. If residents raise concerns, there has to be a quick-response protocol. No months of waiting."
    hide harold_hal_finnegan
    show marco_voss at center:
        zoom 0.7

    marco_voss "A triage response within two weeks, with emergency stop clauses for immediate hazards. And an arbitration panel — composed partly of external experts — to keep things impartial."
    hide amara_vale
    show harold_hal_finnegan at left:
        zoom 0.7

    harold_hal_finnegan "I want a clause that commits to traditional ecological knowledge in restoration corridors. Mangrove planting and monitoring, not just concrete."

    "Elias 'Eli' Navarro" "Agreed. The restoration corridors will be designed by ecologists and engineers. They tie into the seawall through buffer zones — living systems that stabilize sediment and reduce overtopping."
    "You close your eyes for a second and picture saplings driven into mud, volunteers knee-deep, Old Man Tor handing out carved stakes that anchor stories as well as plants. It feels like a kind of justice."
    hide miriam_santos
    hide marco_voss
    hide harold_hal_finnegan

    scene bg ch9_f99e88_3 at full_bg
    # play music "music_placeholder"  # [Music: A gentle swell of piano and strings]
    "Negotiations stretch in turns — technical clarifications, legal phrasing, and the human moments that make words become promises. Marco concedes a clause that binds his firm to a community-trust governance structure; in return, you accept stricter"
    "timeline accountability. It's a trade, but one that feels, crucially, like a trade toward preservation."
    "At one point Marco leans forward, voice more personal than corporate."
    show marco_voss at left:
        zoom 0.7

    marco_voss "Seabright's character has value I didn't anticipate when I first proposed this plan. I'm not here to erase the town. I want this project to be protective and regenerative."
    "You have learned to read the gradient between sincere and strategic. Regardless, you feel the hope that someone with resources can be aligned to community needs, if only the circuits of power are rewired."
    show rosa_kwan at right:
        zoom 0.7

    rosa_kwan "If this holds, my café can keep the corner window that looks over the bay. That window is where people remember their mothers and their storms."
    show miriam_santos at center:
        zoom 0.7

    miriam_santos "Then let's make sure the trust includes microgrants for small businesses to retrofit without losing their footprint."
    hide marco_voss
    show harold_hal_finnegan at left:
        zoom 0.7

    harold_hal_finnegan "And let's set review boards at one-year intervals for the first five years. Maintenance has memory, but we have to build it into law."

    "Elias 'Eli' Navarro" "We can get the engineers to model worst-case scenarios and back them into funding needs. No surprises."
    "You let the warmth of Eli's hand wordlessly relay something you wouldn't say out loud — a shared ownership of responsibility. The room is no longer a scene of opposing forces but a workshop of people with different instruments tuning to the same key."

    menu:
        "Ask Marco about community representation":
            "You press for specifics: how are community seats selected? Marco listens, then nods. The conversation turns to selection criteria: democratic nomination, term limits, and conflict-of-interest rules."
        "Propose a public audit schedule":
            "You propose audits every six months for the first three years, then annually. The suggestion wins murmured approval; Miriam claps once, quietly, like an anchor set."

    # --- merge ---
    "The narrative continues from the following paragraph, reflecting the chosen action."
    "You push for community representation because process becomes protection. Marco's face is unreadable for a beat, then open."
    hide rosa_kwan
    show marco_voss at right:
        zoom 0.7

    marco_voss "Democratic nomination with a community panel vetting candidates — I can live with that. Term limits, too."
    hide miriam_santos
    show amara_vale at center:
        zoom 0.7

    amara_vale "No corporate appointments. Any industry seats must be non-voting."

    "Elias 'Eli' Navarro" "And the trust will have a clause for emergency funding release if a storm damages protective measures. That keeps work from stopping mid-crisis."
    "The committee drafts language with the precision of people who have seen what's at stake. At one point, as you debate wording about 'binding oversight' versus 'advisory oversight,' Hal taps his pen and says simply:"

    harold_hal_finnegan "Call it 'enforceable oversight' or don't call it anything at all. The difference is real."
    "You catch the small, bright laugh that ripple across the table. The tone is buoyant because the work is visible and real."
    hide harold_hal_finnegan
    hide marco_voss
    hide amara_vale

    scene bg ch9_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft scratch of signatures about to be placed, a collective inhalation]
    "The final redraft is not perfect. Nothing ever is. But it contains the scaffolding you demanded: a maintenance endowment secured before construction phases, legally binding rehousing escrow, community-majority seats on the oversight board, emergency stop clauses,"
    "and a funded restoration corridor program that ties ecology into engineering. The pilot seawall is still there — but now nested within living systems and community power."
    "Marco Voss stands, offering a hand that is both an acknowledgment and an invitation."
    show marco_voss at left:
        zoom 0.7

    marco_voss "If everyone agrees to this language, my firm will fast-track the pilot under these conditions."
    "You look at the faces around you — Miriam's steady determination, Rosa's relieved warmth, Hal's old, steady trust, Eli's quiet resolve — and feel a swell that is more than relief. It is the collective satisfaction of hard-won alignment."
    show amara_vale at right:
        zoom 0.7

    amara_vale "We agree. But the trust must be established before ground is broken. Maintenance and rehousing funds must be in place, and oversight must be operational."

    marco_voss "Agreed. Legal teams to finish final phrasing. I'll put my signature in trust. We move together."
    # play music "music_placeholder"  # [Music: Broad, uplifting chord — the sound of work made possible]
    # play sound "sfx_placeholder"  # [Sound: A distant bell from the harbor, bright and resonant]
    "You let yourself breathe, a long, slow exhale that tastes like salt and possibility. The plaza feels altered, as if the air itself has been set in a new pattern. People begin to laugh in small"
    "bursts — not triumphalist, but honest. There is a plan to test, an infrastructure that now carries accountability, and a small reservoir of resources set aside for the people most vulnerable to change."
    "You gather the papers, feeling the weight of commitments that might hold. Elias 'Eli' Navarro slides a printed maintenance schedule into your folder. Miriam pulls you aside for one last logistic: community nomination dates. Rosa presses"
    "a hand to your arm, searching your face for the permission she always gives to friends: rest, a little."
    show rosa_kwan at center:
        zoom 0.7

    rosa_kwan "Don't forget to eat. You look like the Beacon's lights are running through you."

    amara_vale "We'll go over public notices at the Beacon. Town needs to see this in plain language."
    hide marco_voss
    hide amara_vale
    hide rosa_kwan

    scene bg ch9_f99e88_5 at full_bg
    # play music "music_placeholder"  # [Music: Gentle piano continues, optimistic]
    # [Scene: The Beacon (Community Climate Center) | Early Evening]

    scene bg ch9_f99e88_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Footsteps, the soft hum of sensor arrays outside, a kettle beginning to sing in the small kitchen]
    # play music "music_placeholder"  # [Music: Soft, hopeful acoustic guitar underpins conversation]
    "Inside the Beacon, you and Eli translate legalese into something your neighbors can understand. You tape a one-page summary to the glass door, language stripped of doublespeak: what the oversight board does, how rehousing works, what the maintenance endowment is for, and how community members can nominate oversight representatives."

    "Elias 'Eli' Navarro" "You made the summary clear. People will actually read this."
    show amara_vale at left:
        zoom 0.7

    amara_vale "That's the point. Transparency is a kind of protection."
    show harold_hal_finnegan at right:
        zoom 0.7

    harold_hal_finnegan "And you built legal teeth without getting eaten in the process. That's a rare skill."
    show miriam_santos at center:
        zoom 0.7

    miriam_santos "Now comes the Vote. We prepare flyers, public briefings, and a Q&A. We make sure nobody is left in the dark."
    "You feel tired in a new way — the pleasant exhaustion that comes from labor that matters. You also feel something else: a thread of intimacy between you and Eli loosened into something broader. You had"
    "worried that partnership on plans might shade tenderness; instead, it has deepened. You share glances that are no longer only technical and now carry small soft promises."

    "Elias 'Eli' Navarro" "When this wall stands and the mangroves take root, we'll be able to point to a place and say: we did that."

    amara_vale "We did that. We made a place for people to stay."

    menu:
        "Offer to host the informational meeting":
            "You volunteer the Beacon's front room for the town briefing. Miriam grins, clasping your hand; she already has a schedule forming in her mind."
        "Draft a plain-language FAQ instead":
            "You pull a fresh marker to the whiteboard and start a FAQ list: 'What does oversight mean?' 'How will rehousing work?' The words feel like seeds that will help root trust."

    # --- merge ---
    "The narrative continues from the following paragraph, reflecting the chosen action."
    "You choose to draft the FAQ because language will be the bridge between contract and community. As you write, Rosa brings in a plate of something sweet and sea-scented; Hal fiddles with a tide graph on the wall; Miriam maps out speaking points. The Beacon hums like an engine restarted."

    "Elias 'Eli' Navarro" "We'll ask for three pilot monitoring stations along the restoration corridors. Hal knows people who can install them."

    harold_hal_finnegan "I do. And we'll train volunteers to help with maintenance checks. This cannot be something only for professionals."

    amara_vale "A maintenance culture,"
    "The evening draws on. You mark public meeting times, phone numbers, and the steps to nominate oversight representatives. There is work to be done — ballots to prepare, legalese to simplify, trust infrastructure to stand up — but the path ahead looks like something you can walk together."
    hide amara_vale
    hide harold_hal_finnegan
    hide miriam_santos

    scene bg ch9_f99e88_7 at full_bg
    # play music "music_placeholder"  # [Music: A final, rising note of strings — hopeful and forward-facing]
    "You step outside for a moment, listening to the harbor bell and the distant call of gulls. The town is not saved. Nothing is ever fully saved. But a binding structure has been erected: law, ecology, and community entwined. Your chest lifts with that bright, precarious hope that growth brings."
    "You know the Vote will be the next test, and the months after will be work by other names. For now, you allow the quiet joy to settle — a small tide pooling in the heart."
    # [Page-Turn Moment]
    "You fold the final one-page summary into your pocket and look at the town through the Beacon's glass: the boardwalk's raised sections catching lamplight, Rosa's café a warm rectangle, Hal's stooped silhouette moving like a slow,"
    "sure tide. Tonight, the ocean feels less like an unmaking and more like a boundary we're learning to read. The agreements drafted today are scaffolds for tomorrow."

    scene bg ch9_f99e88_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter14
    return
