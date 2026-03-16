label chapter10:

    # [Scene: Saltbridge Boardwalk | Dawn]

    scene bg ch9_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the clink of tools at work, soft conversation carried on the salt air]
    # play music "music_placeholder"  # [Music: Gentle piano with warm strings — a slow, rising motif]
    "You walk the boardwalk with your coat collar up against a chill that still smells faintly of storm. The signature you made — ink damp, paper folded into record — isn't a punchline anymore; it's a"
    "seam. Around it, people are stitching. Not every thread is neat. Not every face is calm. But there are hands moving with intention."
    "The blueprints are in your bag, along with the notebook that remembers every tide line and every neighbor. Finn's crew is on the far pier, their silhouettes busy and easy, fitting a retrofitted engine into a"
    "small skiff. A painted sign flaps on the barricade: COMMUNITY MAINTENANCE STARTS HERE. Someone has hung a string of shells like a talisman."
    "You feel Elias Novak before you see him — a warm voice carrying, a laugh that pulls others close. He steps down from the dunes with protest hand-me-downs rolled into a neat bundle, salt on his"
    "cuffs. He finds you and grins, the kind that says victory is messy and worth it."
    show elias_novak at left:
        zoom 0.7

    elias_novak "You look like someone who slept with the town under their pillow."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "I slept with the sea someplace else — but close enough. You?"

    elias_novak "Broke a megaphone and a chair. Progress."
    "He bristles at the word 'compromise' as if it were a splinter; you both know its sharpness. He wants more. You want more. But you also carry the ache of families who needed certainty. The ache and the relief sit in your chest as twin tides."

    elias_novak "You did what you could without becoming someone else. I can't pretend it's everything I wanted."

    maya_serrano "No — it's not everything. But it's something that won't leave people behind."

    elias_novak "Then we'll take something. Keep pushing. Keep the heat."

    maya_serrano "I'll join you when I can. But someone has to make sure the beams hold."

    elias_novak "You always loved the builders more than the banners."
    "His hand gestures toward the harbor, and the moment is small and human — an acknowledgment rather than an argument. You let the warmth of it sit with you like a mend."
    # [Scene: Rooftop Sanctuary | Morning]
    hide elias_novak
    hide maya_serrano

    scene bg ch9_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Bees, the soft scrape of a trowel, distant municipal traffic subdued]
    # play music "music_placeholder"  # [Music: Harp plucks, an intimate high-register warmth]
    "Up here the city feels repairable. Dr. Hana Park stands over a spread of maps and seed packets, hair pulled back, field tablet glowing with contour lines. She points to a curling coastline and then to"
    "a patchwork plan of living shorelines and rooftop runnels. Her gestures are exact and patient."
    show dr_hana_park at left:
        zoom 0.7

    dr_hana_park "We prioritize blocks with the highest social vulnerability index and the simplest retrofits. Living shorelines buy time and strengthen sediment. Rooftops reduce runoff."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "And the maintenance?"

    dr_hana_park "That's where people like Rosa and Finn come in. Employment is part of resilience. If you pay people to care for the living systems, they survive."
    "You trace the lines she draws, imagining cordgrass and recycled oyster shells binding the sand like stitches. The science is hopeful — not miraculous, but practical. It feels like a toolbox instead of a sermon."

    dr_hana_park "You carried decisions like lichen — they look small until they cover everything. You're doing the work now. That's what matters."

    maya_serrano "I still wake to letters on doormats. I still taste the cost."

    dr_hana_park "Costs don't evaporate because we sign papers. They change shape. You have something better: community ownership."
    "She folds a map and slides a seed packet into your palm like a small concession and a promise."

    menu:
        "Kneel and plant the packet of salt-tolerant basil.":
            "You sink your fingers into compost, feel cool earth give beneath your nails. The scent of basil is immediate — peppery, green. A neighbor nods from a nearby bed. It's a tiny ceremony of repair."
        "Ask Dr. Hana to show you the modeling for the shoreline permutations.":
            "She taps the tablet; a model blooms in color. You watch waves reimagine themselves as sediment, and understanding settles into your ribs like ballast. The math is humane, and that steadies you."

    # --- merge ---
    "Neither choice changes the arc of the day."
    "Neither choice changes the arc of the day. Both make you feel anchored."
    # [Scene: Rosa's Café | Midday]
    hide dr_hana_park
    hide maya_serrano

    scene bg ch9_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft clatter of cups, low voices, a radio on in the corner playing an old coastal melody]
    # play music "music_placeholder"  # [Music: Gentle acoustic guitar, steady and comforting]
    "The café is a triage center now — not just for soup and pastries but for paperwork, counseling, and quiet hand-holding. Rosa moves behind the counter like someone smoothing a map: she guides, she feeds, she listens. Her laugh is the same; so are the flour ghosts on her cardigan."
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "You should sit. You've been wearing the sea on your face all morning."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "I was about to say the same to you."

    rosa_alvarez "Finn's team started early. They asked if the bakery still needed help. I told them yes, and no, and maybe — like you taught me to do."
    "Finn slides into a chair with grease on his fingers and a grin that breaks open the morning. He talks about engines and conversion kits, about the joy of repurposing an old hull into a lifeline."
    "Pride and work cross his face in a way that steadies you more effectively than speeches."
    show finn_serrano at center:
        zoom 0.7

    finn_serrano "You should see the bilge we cleared. Smells like victory, or at least adventure."

    maya_serrano "We'll call it 'sea-scented victory.'"
    "Noah Kestrel arrives with a pot wrapped in a towel and the kind of measured breath that announces himself without fanfare. He sets the pot down with deliberate care. The steam smells of broth and thyme, an industrial tenderness."
    hide rosa_alvarez
    show noah_kestrel at left:
        zoom 0.7

    noah_kestrel "Thought you could use something warm."

    maya_serrano "You brought structure and soup. A two-point plan."

    noah_kestrel "And a committee charter. The oversight board needs a draft. Also more thyme."
    "His hands have traces of blueprints under his nails. He speaks quietly about load-bearing measurements and community workshops in the same sentence. There's a steadiness to him now that wasn't there when the first proposals landed"
    "on the table — a presence that feels less like an explanation and more like partnership."

    noah_kestrel "We made the jobs program work because we tied payroll to local contracting. We can't fix everything, but we can make the work belong to those who live here."

    maya_serrano "Some people won't come back, Noah."

    noah_kestrel "I know. We made provisions for relocation funds and guarantees for small-business priority in rehousing. It's not perfect."
    "The room tightens around that truth. Rosa pours soup into bowls with hands that know how to feed more than hunger."

    noah_kestrel "You didn't sell the town out. You negotiated a future where people can still argue about the kind of town they want to be. That's valuable."

    maya_serrano "I kept thinking of the neighbor — I keep thinking of her porch light."

    noah_kestrel "You carried her so that others wouldn't have to. Let that count for something."
    "There is a hush, a smallness to what passes between you that does not need to be named to be felt. It is practical, spare, and honest — the kind of affection that builds scaffolding rather than monuments."

    menu:
        "Accept Noah's bowl of soup and speak about logistics.":
            "You lift the spoon and let the broth warm you. Words of policy come easier with warmth in your belly. You map schedules and maintenance cycles between sips."
        "Refuse the bowl politely and ask Finn about boat modifications instead.":
            "Finn brightens and launches into technical detail. Your hands get oily; your mind settles. Work is a different kind of comfort."

    # --- merge ---
    "Your guilt softens into a sober steadiness."
    "Your guilt softens into a sober steadiness. The small, daily acts of repair — a job offered, a shore planted, a boat refitted — become the scaffolding of recovery."
    # [Scene: Saltbridge — Community Pier | Late Afternoon]
    hide maya_serrano
    hide finn_serrano
    hide noah_kestrel

    scene bg ch9_3be532_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Applause, low speeches, the rhythmic slap of waves against pilings]
    # play music "music_placeholder"  # [Music: Warm brass and chorus; hopeful without being triumphant]
    "A ceremony is half ritual, half logistics: the public oversight committee is sworn in, job placement lists are posted on corkboards, and Dr. Hana Park reads out sediment targets with a scientist's gentle emphatic cadence. Elias"
    "Novak stands by the stage, fist briefly raised, then unclenched. Noah Kestrel stands near you, hands clasped, the pot of his earlier soup now empty but its warmth lingering."
    show mayor_lillian_cho at left:
        zoom 0.7

    mayor_lillian_cho "This is not the end of stories lost, but the beginning of new ones written together."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "The words land like gravel in a pocket — necessary ballast."
    "People you know step up to sign their names to maintenance rosters. Rosa organizes a rota for food and counsel. Finn's crew gets their first formal contract. A woman who had her home in the proposed"
    "remediation zone cries quietly and then signs up for the housing assistance program after talking with a counselor. Not everyone is smiling. Not all departures are softened. But there is movement away from paralysis."
    show elias_novak at center:
        zoom 0.7

    elias_novak "We kept them honest."

    maya_serrano "We kept them honest together."

    elias_novak "And you kept me from burning the whole plan down."

    maya_serrano "You kept me from waiting too long."
    "Words fold into each other, imperfect and true. The day is not a victory lap; it's a first shift."
    # [Scene: Rooftop Sanctuary | Evening]
    hide mayor_lillian_cho
    hide maya_serrano
    hide elias_novak

    scene bg ch9_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Laughter, the rustle of cloth, a kettle singing somewhere]
    # play music "music_placeholder"  # [Music: Piano returns with the warm string motif, a sense of closing and continuity]
    "You stand at the edge of the garden as twilight settles, the rooftops below stitched with solar fabric and green patches. Someone has strung dried lavender in a line; across the harbor a new breakwater glints"
    "with freshly placed oyster clusters. Noah Kestrel is beside you, hands tucked into his coat pockets. Elias Novak is across the terrace, leaning on the rail and trading jokes with Finn."
    show noah_kestrel at left:
        zoom 0.7

    noah_kestrel "You did the hard thing — you negotiated with a compass and a conscience."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "It felt like cutting bread and not knowing who would get which slice."

    noah_kestrel "Then we'll bake more bread."
    "He speaks in practical metaphors because those are the ones he trusts. But when he looks at you there is no distance made of policy; there is a steady presence, a promise shaped by small acts."
    "You realize your guilt has become method — not a resignation but a discipline that channels grief toward repair."

    noah_kestrel "We can keep barging through the noise. Or we can schedule the next community workshop and bring soup again."

    maya_serrano "Bring the soup."
    "Elias Novak crosses the terrace, his shoulders relaxed in a way they haven't been in months. He ruffles Finn's hair, then looks at you with a clear, bright look that holds both challenge and affection."
    show elias_novak at center:
        zoom 0.7

    elias_novak "Promise me one thing. Don't let us go gentle on whoever tries to privatize our shorelines again."

    maya_serrano "I won't."

    elias_novak "Good. Because I have a terrible talent for escalation."

    maya_serrano "And I have a talent for paperwork to rein him in."
    "The three of you sit, not in a tableau of clean resolution but in the comfortable sprawl of people who have been through storms together. The rooftop smells of herb smoke and bread. You think of"
    "the neighbor's porch light again — and it no longer burns only as accusation but as a mnemonic for why the work matters."

    menu:
        "Trace the dented compass at your throat and let the thread rub against your skin.":
            "The metal is cool, the red thread rough at the edges. You breathe. The promise knotted there has changed, but it's still a promise."
        "Open your Moleskine and add a new list: 'Maintenance Rota — Week One.'":
            "Your handwriting steadies. The list is practical, small, necessary. You feel the shape of the week aligning under your pen."

    # --- merge ---
    "There is a tempered tenderness that continues into the night."
    "There is a tempered tenderness between you and Noah Kestrel — not a sweeping romance but a durable one, built on shared practicalities and quiet support. Elias Novak is a living thing at your shoulder: urgent,"
    "alive, a reminder to keep the pressure on. Finn is a bright, relentless builder. Rosa is already turning victory into meals. Dr. Hana Park's plans are planting themselves into real soil."
    "Night falls gently over Saltbridge. The pier lights blink awake, and workers head home with muddy boots but steady steps. Some homes are gone; some small businesses will reopen down the road with new guarantees; some"
    "neighbors will decide that moving is the kindest choice for their families. Loss remains — and so does something else: the knowledge that a town can organize to take care of itself."
    "You fold your notebook closed, but not with the weight of finality. You close it like a ledger that will be opened each morning. The red thread tugs at your wrist; you do not tug back."
    "You look at Noah Kestrel, then Elias Novak, then at Rosa waving from the café below, and you let the feeling that rises have edges of both relief and resolve."

    maya_serrano "This isn't the end."

    noah_kestrel "No — it's the beginning of a lot of work."

    elias_novak "And the beginning of a lot more trouble. Which we will love."
    "You smile, and it's honest. The shorelines are negotiated, imperfect, alive. The people who will tend them are here, present, committed. Your love is practical, patient. Your grief is named and given purpose. The town breathes"
    "around you: not healed in the way stories promise, but repaired, humming with small, steady life."
    hide noah_kestrel
    hide maya_serrano
    hide elias_novak

    scene bg ch9_3be532_6 at full_bg
    # play music "music_placeholder"  # [Music: Full strings swell into a warm, resolving chord]
    "You step back from the rail and let the air move through you. There will be storms yet. There will be moments when the ink looks too small for the scale of the tides. But there"
    "are also hands to anchor lines, people to teach others how to knot, and roofs to plant. For now, that is enough."
    # [Scene: Night — Rooftop Sanctuary | Night]

    scene bg ch9_3be532_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant waves, soft conversation, the occasional pop of a celebratory cork]
    # play music "music_placeholder"  # [Music: A final, gentle piano note held long then released]
    "You close your eyes and listen to Saltbridge breathing — a town that is learning how to care for itself without losing its shape. In the quiet you can feel the shift: from solitary guilt to shared responsibility; from a promise made alone to promises kept together."
    "This is the end of the negotiated shoreline. Not an endpoint of struggle, but a hinge into sustained, careful repair. You have traded some ideals for a living future, and in doing so you have found"
    "companions who will hold the line with you. You are tired, and you are steady. The road ahead is long and luminous with work."

    scene bg ch9_3be532_8 at full_bg
    "THE END"
    # [GAME END]
    return
