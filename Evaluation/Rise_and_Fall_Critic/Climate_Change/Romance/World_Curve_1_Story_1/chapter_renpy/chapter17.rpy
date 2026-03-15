label chapter17:

    # [Scene: Rosa's Café | Mid-Morning, Months Later]

    scene bg ch13_782002_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low chatter, the hiss of a milk steamer, gulls faint beyond the street]
    # play music "music_placeholder"  # [Music: Gentle, ascending piano — steady, hopeful]
    "The stitched map is spread across the table like a patchwork skin of the town: paper and cloth, digital printouts taped to canvas, little hand-drawn annotations in different inks. Your fingers hover over the tangle of"
    "lines — raised promenades stitched in ochre thread, mangrove corridors annotated with sapling counts, modular seawalls sketched as dashed segments. Each stitch is a season of work and argument, an index of names and nights."
    "You breathe in the café air: coffee sharp and warm, a thin tang of lemon from Rosa's pastry, salt from the boardwalk that seems to ride in on every customer. There is a faint smell of"
    "latex from new sapling bags folded into a tote at your feet. Months have softened the raw edges of urgency into an everyday rhythm: meetings, weather reports, community shifts that read like stitches — visible, imperfect,"
    "holding."
    show rosa_kwan at left:
        zoom 0.7

    rosa_kwan "Rosa slides a cup toward you, flour on her hands and a grin that crinkles the corners of her eyes."

    rosa_kwan "You look like you need this twice over. Map looks proud of itself."
    show amara_vale at right:
        zoom 0.7

    amara_vale "It earned a few sleepless nights."
    "You smile, tracing a new microgrid node with your finger. 'But it looks like it's doing its job.'"

    rosa_kwan "It better. My ovens are already thanking whatever spirit runs municipal bonds."

    amara_vale "They're thanking the people who showed up to vote, too."

    "Elias 'Eli' Navarro" "Eli arrives with a grease-stained satchel slung over one shoulder, hair wind-ruffled as always, and a new scar of sun on his collarbone where he forgot sunscreen at a site visit. He sits, and for a beat the map folds into the space between you as if the two of you are a hinge."

    "Elias 'Eli' Navarro" "You found the thread I left in the ledger."
    "He taps a small annotation near the promenade outline. 'Hal liked the reinforcement detail. Says it's honest work.'"

    amara_vale "Hal always notices the honest bits."
    "You set the map straight. 'How did the prototype hold up after high tide last week?'"

    "Elias 'Eli' Navarro" "Better than we dared hope."
    "He exhales a laugh. 'Not perfect — we had a flex at Pier Six — but the stress data redlines are flatter. The microgrid held through the gusts. Rosa's café didn't blink.'"
    "Amara Vale [internal]: Relief tastes like coffee and the light through the window. For months you carried the town's possible futures like a list of debts; watching small victories ripple outward feels like undoing a knot."

    rosa_kwan "And you — how are you, Amara? You used to make faces at your coffee when plots turned ugly."

    amara_vale "I make fewer faces, maybe. I sleep more than I used to, which is new."
    "You look at Elias 'Eli' Navarro. 'We sleep a little better.'"
    "Elias 'Eli' Navarro's eyes find yours. There is a quiet conversation in that look — not loud declarations, but tethering: two people who have been counted on and who have learned to divide that counting between"
    "them. The intimacy is woven through small things — shared overnight site checks, the way he knows when to bring you a spare jacket, the soft shorthand that skips explanation."

    menu:
        "Trace the new promenade route with your finger":
            "Your finger follows the ochre thread and you can feel the weight of it — benches already ordered, plants scheduled for next month. The motion grounds you; the plan becomes a place."
        "Fold the map and make a list of next week's priorities":
            "You fold the map with practiced hands and pull your notebook close. Priorities write themselves into action — volunteers to call, permits to re-check, sapling deliveries to confirm."

    # --- merge ---
    "Rosa watches the exchange between you and Elias 'Eli' Navarro with a soft, satisfied hum."

    rosa_kwan "You two look like two halves of the same blueprint. It's good, seeing you like this."

    "Elias 'Eli' Navarro" "That's our new aesthetic."
    "He nods toward the map. 'Function-forward romance.'"

    amara_vale "Practicality is romantic here."
    # [Scene: The Beacon | Afternoon]
    hide rosa_kwan
    hide amara_vale

    scene bg ch13_782002_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hum of sensors, a distant crash of surf, markers squeaking on boards]
    # play music "music_placeholder"  # [Music: Soft strings rise; bright undertones]
    "You carry the map into the Beacon, trading the intimate warmth of Rosa's for the organized bright energy of the center. Volunteers move between stations, stacking boxes of saplings, labeling battery banks, printing outreach flyers. The place thrums with work that has a shape and a name."
    "Miriam is there, megaphone slung at her hip, sleeves rolled and eyes bright. Hal is rearranging a set of brackets on a table the way someone arranges memories — carefully, with the kind of respect that makes steel look softer."
    show miriam_santos at left:
        zoom 0.7

    miriam_santos "We're on the second round of community workshops. People are bringing questions instead of anger now, which is a miracle I didn't expect so fast."
    show amara_vale at right:
        zoom 0.7

    amara_vale "Questions are better. They mean they're thinking it through with us, not at us."
    show harold_hal_finnegan at center:
        zoom 0.7

    harold_hal_finnegan "And some of the questions are very practical. 'How do we tie our lines to the new promenade without hurting the fish?' I like that question."

    amara_vale "It's a good question."
    "You step closer to a printout of a mangrove corridor plan. 'There's a lot of knowledge in those questions. They help us avoid making mistakes we can't afford.'"

    miriam_santos "You know, the bylaws are up for review next week. People are bringing amendments, and—"
    "She leans in, conspiratorial and warm. '—they actually want to include a clause mandating community oversight of any private funding.'"
    "Amara Vale [internal]: That clause is one of the things you labored over, nights of negotiation between legal counsel and coffee-fueled debate in the plaza. It is small in paper, large in consequence."

    harold_hal_finnegan "You keep doing the talking and the maps, kiddo. I'll keep doing the brackets and the stories."
    "He pats the map with an affectionate, ragged hand. 'Remember when the town used to fight about a dock light?'"

    amara_vale "Now we argue over coastal berm cross-sections. Progress."

    menu:
        "Walk the corridor of prints, pointing out changes aloud":
            "You move along the printouts like a curator, naming the new microgrid nodes, the rehousing pockets, the raised promenades. Volunteers nod; a man nearby scribbles the new contact for tree maintenance. The plans become a living tour."
        "Sit with Hal and ask about the old projects":
            "You sit opposite Hal. His voice softens as he tells the story of the last big storm he remembers. It anchors you. You ask the questions you haven't asked aloud, and his answers are slow and precise, full of memory and warnings."

    # --- merge ---
    "Marco Voss stands at the edge of the room. He is both less and more severe than in flyers and council footage — proper tailored coat, a careful smile, eyes that measure returns."
    hide miriam_santos
    show marco_voss at left:
        zoom 0.7

    marco_voss "The new promenade looks…complete in spirit."
    "He offers a thin smile. 'I'm glad to see funds being used in ways that respect the town.'"

    amara_vale "Respect is a practice, Marco. We're still working on it."

    marco_voss "Of course. I believe infrastructure can be done well and quickly. The upgrades are visible."
    "He nods at Elias 'Eli' Navarro. 'And some of your engineering choices there reduced costs without sacrificing integrity. Good work.'"

    "Elias 'Eli' Navarro" "We tried to balance longevity with what the town can afford. There's a lot of iteration left."

    marco_voss "Iteration is an investor's favorite word."
    "He smiles. 'But I mean it—iteration that keeps people safe.'"
    "Marco Voss's tone is smooth; his approval is an instrument calibrated for leverage. Still, in the room now he seems less like an antagonist and more like another actor who has fitted himself into the new"
    "pattern — sometimes willing, sometimes calculating. The reaction you give is careful but not cold. Months of working together have taught you that people can change in degrees."
    # [Scene: Seabright Stitched Map / Microgrid Nodes | Late Afternoon]
    hide amara_vale
    hide harold_hal_finnegan
    hide marco_voss

    scene bg ch13_782002_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Children playing at a distance, the creak of a newly raised bench, a gull calling]
    # play music "music_placeholder"  # [Music: A gentle swell of strings, sunlight brightening the chords]
    "The exhibit draws a steady trickle of people: shopkeepers, fishermen, teenagers, an elderly woman who touches the map as if reading Braille. The map is a conversation in stitches: names attached to sapling plots, a photograph"
    "of a household that accepted rehousing support, a small ledger page showing the first microloan disbursements. Scar lines show where the sea took and where the town rebuilt in response."
    "You stand with Elias 'Eli' Navarro and Hal as a young couple approaches, their hands clasped. They find their street and run a finger along the raised promenade. The woman looks up at you and smiles the sort of smile that holds a thank-you inside it."

    "Woman" "My shop used to drown every winter. Now I can sleep through storms."
    show amara_vale at left:
        zoom 0.7

    amara_vale "We did the best we could. We're still learning."
    show harold_hal_finnegan at right:
        zoom 0.7

    harold_hal_finnegan "These are the small salvations. They add up."
    "Miriam arrives with a stack of flyers for a neighborhood meeting and a few volunteers trailing with sample saplings. Her energy is steady as tide."
    show miriam_santos at center:
        zoom 0.7

    miriam_santos "The next planting is Saturday. We doubled the volunteer slots."

    amara_vale "Good. We'll need more hands on the northern corridor. The schools want to involve students."

    "Elias 'Eli' Navarro" "And the microgrid team will bring a demonstration panel."
    "He looks at you. 'You said you wanted to show how the nodes tie people directly to the system.'"

    amara_vale "They need to see they have control, not just connection."
    "Marco Voss lingers near the map's edge, watching people interact with the stitches. His expression is complex — not hostile, not entirely benevolent — the face of someone whose calculations include both profit and the public's gaze."
    hide amara_vale
    show marco_voss at left:
        zoom 0.7

    marco_voss "You did something most planners never get to do: make the plan readable. That's rare."
    "He nods. 'It builds trust.'"
    "You accept the praise without letting it displace the people who did the real labor. You also notice how much of the map is not final: pencil marks, small post-it edits, a child's drawing of a mangrove crab taped near the corner. The town is a work in continuous mending."

    menu:
        "Explain the microgrid demo to the curious couple":
            "You kneel to their level and point to the little node icons, explaining in plain language how local batteries store power during storms. They nod, relieved, their flicker of fear easing."
        "Step back and let Elias 'Eli' Navarro lead the demo":
            "You let Elias 'Eli' Navarro step forward with the panel. He speaks in low technical rhythms and the couple's eyes follow as he gestures. You watch him watch them, and there's a small, private pride that catches in your chest."

    # --- merge ---
    "You think of how far the town has come: policies that keep oversight in the hands of residents, funding streams that blend public bonds and vetted private investment, institutions — like the Beacon — that now"
    "have staff and schedules and a steadier pulse. You think of the saplings that will take years to stand tall, and the benches that will sit under them for decades."

    harold_hal_finnegan "We got lucky and we made our luck. There's honesty in both."
    "Amara Vale [internal]: Months of negotiation, of sleepless nights and conversations that landed bruises, have moved into a different register. You still feel the ache of what was lost, of what has to be guarded. But under the ache there is a steadying cord you and others have braided."
    "Elias 'Eli' Navarro slips his hand to rest lightly on the small of your back — an unassuming habit now, an anchor rather than a declaration. The movement is simple and says everything it needs to: we are still here, together, building."
    "You look out at the map and at the people tracing their futures with fingers and voices. The town bears its scars openly; the new structures do not hide them. They are sewn into the fabric, honest seams that read as both repair and history."
    # [Page-Turn Moment]
    "You fold a corner of the stitched map and tuck it into your bag. The sun hits the lanterns and they bloom tiny suns of their own. Voices carry: laughter, the clip of a drill, someone"
    "calling out a plant name. There is a soft, collective hum — the town settling into a new cadence. You feel something like gratitude rise through your chest, not naive, but bright and durable."
    "Outside, clouds are lining the horizon, edged in gold. They remind you that storms will come again; that work is not finished. But they also light the promenade with a blade of late-day sun that makes"
    "the new rails glow. You breathe in the salt and the scent of turned mud and promise."
    hide harold_hal_finnegan
    hide miriam_santos
    hide marco_voss

    scene bg ch13_782002_4 at full_bg
    # play music "music_placeholder"  # [Music: The music rises once more — a warm, ascending chord that holds]

    scene bg ch13_782002_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter24
    return
