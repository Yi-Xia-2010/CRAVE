label chapter14:

    # [Scene: Rosa's Café | Early Evening — Months Later]

    scene bg ch13_10625f_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low murmur of conversation, milk frother hissing, boardwalk rain tapping a distant rhythm]
    # play music "music_placeholder"  # [Music: Gentle, rising strings with a steady pulse — hopeful and intimate]
    "You push open the café door and the bell gives a bright, familiar chime. The room smells of citrus peel, cardamom, and the salt-soured tang of sea air that slips in on your coat. The world outside has not stopped rearranging itself; inside here, things have been stitched together."
    "Rosa looks up from the counter like a lighthouse turning to you. Her hand is flour-dusted; her cap is its usual bright accent. She sets a plate down between you and Eli with a conspiratorial smile."
    show rosa_kwan at left:
        zoom 0.7

    rosa_kwan "You two look like you could use something sweet. It's sea-salt tarts tonight. For the stitch-workers."
    "You laugh, and the sound feels lighter than it would have before — not because the work is done, but because it is shared."

    "Elias 'Eli' Navarro" "They keep getting better,' Eli says, eyes crinkling. He reaches for the tart with the easy, small gesture that has become yours to notice: the brief brush of his fingers as he hands you a napkin. 'Hal called earlier. Said the tide sensors in Dockside are finally returning reliable readings after the retrofit."
    "You hold the tart between your fingers, the crust warm, flaky, and dusted with salt. The moment is ordinary and full: pastry, coffee steam, the soft weight of Eli's attention. Your chest makes room for a"
    "small, steady joy that has grown in the months of meetings, volunteer trainings, and late-night data cleaning."
    "You fold your coat over the back of your chair and watch him watch the room — a quiet habit. When he speaks, the sentences are pragmatic and soft at once."
    show amara_vale at right:
        zoom 0.7

    amara_vale "How are they holding up with the microgrid tie-in? The switchovers were the trickiest part."

    "Elias 'Eli' Navarro" "We put the priority nodes on loop A. When the primary fails the micro-inverters engage before the pumps drop below threshold.' (He gestures with the spatula like a pointer.) 'Still, the real victory is the volunteer roster, not the hardware. People showed up at dawn to anchor the panels."
    "You nod, thinking of the volunteers wading knee-deep at the mangrove site last spring, of Miriam teaching volunteers how to thread mud boots. The memory is a braid of faces, laughs, and the terrible, satisfying work of building something that resists."
    "Rosa leans in, voice low and bright."

    rosa_kwan "You'll need to swing by tomorrow. I've got Miriam in for coffee at nine; she wants the Beacon's lamplight early. We all want to see the stitched map — it's been on everyone's mind."
    "Eli exchanges a look with you that does not need translation. The look is soft around the edges, threaded with an easy understanding that comes from months of shared purpose."

    menu:
        "Take the tart to go and head to the Beacon now":
            "You tuck the warm tart into a napkin and stand; the move feels like carrying a small warmth into the next room. Eli tucks his satchel over one shoulder, the two of you already synchronized."
        "Sit a while longer and listen to Rosa's update":
            "You ease back into the chair and let the café's warmth slow the afternoon. Eli leans in, listening with you; Rosa launches into a story about a recruited volunteer with two left boots — the room brightens around the absurdity."

    # --- merge ---
    "Continue"

    rosa_kwan "Whatever you choose, bring Hal a piece. He still hums when he's happy."
    "Hal arrives before you can answer, the bell over the café door catching him in a halo of lamplight. He moves more slowly now — a stoop in his shoulders, a loose ponytail frayed at the"
    "edges — but his eyes have not lost their lock-and-key focus. He sets a folded map on the table between you: the stitched map, weathered at the creases, a mosaic of paper, thread, and ink."
    show harold_hal_finnegan at center:
        zoom 0.7

    harold_hal_finnegan "Thought you'd want to start here,' he says. 'Seen this work through salt and storm. There's something steady about how folks are leaning into maintenance instead of just promises."
    "You pick up the map; your fingers know the weight of it — not only paper but all the meetings, signatures, and nights sewn into its seams. Little patches of cloth mark raised promenades; strings tie microgrid nodes to community centers; pencil flags indicate rehousing pockets."

    amara_vale "It's more than planning now. These lines are agreements people have lived into. They still show scars, but the scars are mended instead of hidden."
    "Elias 'Eli' Navarro reaches over and traces a raised promenade with his finger, following your sentence with a technical comment on load distribution. You can feel his thumb on the grain between the map's paper threads. It is a small intimacy calibrated by years of joint labor."

    "Elias 'Eli' Navarro" "We learned the hard way about concentrated loads on raised sections. The modular underpinnings are easier to replace now without disrupting traffic or businesses."

    harold_hal_finnegan "And the bylaws held. Folks had teeth in them — oversight, mandated maintenance funds. That made contractors accountable."
    "The conversation blooms into multiple turns: technical details, policy notes, and the human stories threaded through them. Rosa contributes a memory about a family who refused to leave their shop until neighbors re-raftered and roughed in"
    "protections. Miriam's voice — brisk, triumphant — arrives like a bright gust as she slips into the chair next to you."
    hide rosa_kwan
    show miriam_santos at left:
        zoom 0.7

    miriam_santos "We moved the ballot margins by a hair and then by muscle. People showed up because they saw themselves in the plan. They voted for a maintenance culture, not a miracle."

    amara_vale "And funding? The blended mechanisms held?"

    miriam_santos "A mix of municipal bonds, a public-benefit trust seeded by Marco's conditional fund transfer, and community microfinance. Not perfect, but operational."
    "At the mention of Marco, Elias 'Eli' Navarro's hand tightens on the map for a fraction of a second. You remember how his name used to make the room pivot — promises and displacements wrapped in"
    "glossy brochures. Now, the mention presses into your chest with complex relief. You do not know exactly where Marco stands in everyone's hearts; the relation is layered. You let the ambiguity sit without trying to untangle"
    "it."
    # [Scene: The Beacon | Late Afternoon — The Stitched Map Room]
    hide amara_vale
    hide harold_hal_finnegan
    hide miriam_santos

    scene bg ch13_10625f_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft tap of a sensor calibrating, occasional laughter, the distant creak of the boardwalk]
    # play music "music_placeholder"  # [Music: A gentle swell of cello and light percussion — forward-leaning]
    "You walk with the map rolled under your arm. The Beacon smells of oil, wet wool, and the citrus cleaner Rosa uses on the tables. The whiteboards glint with deadlines and hand-drawn cross-sections. Volunteers are labeling nodes with colored tags that match the fabric squares on the map."

    "Elias 'Eli' Navarro" "We have the micro-inverters scheduled for the next maintenance quarter,' he says, eyes on the board. 'Hal's crew is certified to run the update. I'm going to sit on the oversight committee, but I want that panel to be made up mostly of residents. Engineers should help, not gatekeep."
    show amara_vale at left:
        zoom 0.7

    amara_vale "Agreed. We've been through the 'expert knows best' loop enough times to know it fails the people it's supposed to serve."
    "Elias 'Eli' Navarro pauses, then — half-grin, half-question — asks, 'Do you ever sleep?'"
    "You roll your eyes, but the question is warm. He doesn't ask to chide; he asks to notice."

    amara_vale "A little. The kind of sleep a person gets when they let a worry sit down beside them at night instead of wearing it. And when I do, I dream of mangrove roots threaded like living ladders."

    "Elias 'Eli' Navarro" "Good dreams. We need graphs and ladders.' (He taps the sensor reader on his lanyard.) 'And by the way, Hal suggested we invite Marco into the next oversight review — under strict transparency. He says it'll keep his funding from being a black box."
    "Miriam snorts — not mean, but incredulous."
    show miriam_santos at right:
        zoom 0.7

    miriam_santos "Marco and transparency in the same sentence. That's a novelty."
    show harold_hal_finnegan at center:
        zoom 0.7

    harold_hal_finnegan "He's been pushed. Men like him respond to accountability when it's clear it's not optional. If the funds are conditional on open audits and rehousing clauses, that money becomes leverage for us, not the other way around."
    "Your mind sifts through the months: the stubborn nights when contracts were redrafted, the volunteers who lined up to train, the families rehoused with dignity into raised pockets. The picture is still partial. Honesty sits like a peripheral glow."

    menu:
        "Trace the mangrove corridor on the map":
            "You press your finger along the stitched green channel, imagining hands in mud. Eli nods and pitches in a detail about sediment retention; Miriam interrupts with a plan for community planting days, and the room fills with practical excitement."
        "Point to the rehousing pockets and speak with Hal about tenant protections":
            "You tap the pale fabric that marks rehousing. Hal folds his hands and talks through the covenants. Eli offers tweaks to minimize displacement during retrofits. A hush of responsibility settles over the table."

    # --- merge ---
    "Continue"
    "The chatter softens as you and Elias 'Eli' Navarro move to a small corner where the map and live sensor feeds overlap. On the screen, blue dots blink where microgrid nodes hum; a slow ribbon of"
    "green follows the mangrove corridor you just traced. The live feeds carry the sound of distant water, and for a beat the whole system feels tenderly alive."

    amara_vale "Sometimes it feels like we stitched the town's future out of bits of everyone — their skills, their patience, their demands."

    "Elias 'Eli' Navarro" "We didn't stitch it alone,' he says. 'You held the narrative. You translated the data into a reason for people to show up."

    amara_vale "You held the nuts and bolts in a way people could trust,' you answer. 'We both did it, and more people stitched in."
    "Elias 'Eli' Navarro reaches for your hand, laces his fingers with yours over the table's edge, the map's fibers pressing between your palms. The touch is ordinary, steady — not a grand vow but a daily promise."

    "Elias 'Eli' Navarro" "There's something I want to say that I haven't said in a meeting."

    amara_vale "Out with it."

    "Elias 'Eli' Navarro" "When roofs were being secured for that family on Harbor Row, I realized I'd rather be on the side that makes sure their roof lasts than on the side that punts decisions to profits. That's where I want to be."
    "You feel the rise of something warm and sure. The work has shaped personal decisions into moral ones; your relationship has become a seam connecting private and public commitments. Your hands flex around his."

    amara_vale "So do I."
    # [Scene: Seabright Stitched Map / Microgrid Nodes | Dusk — Outside the Beacon]
    hide amara_vale
    hide miriam_santos
    hide harold_hal_finnegan

    scene bg ch13_10625f_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Gulls, a distant bell on a mooring, the low murmur of evening traffic]
    # play music "music_placeholder"  # [Music: A single, ascending piano motif — small, resolute]
    "Marco Voss's car is at the curb, a compact that looks almost apologetic against the wet street. He steps out, raincoat catching the lamplight. When he approaches, the room's warmth cools for a beat; his presence is a reminder that public goods and private power still negotiate the town's edges."
    show marco_voss at left:
        zoom 0.7

    marco_voss "Amara,' he says, voice smooth in the way it always has been. He lays a slim folder on the table with a practiced ease. 'A few adjustments to the fund's terms, clarified covenants. I want it to be unambiguous, and—"
    "You study him. There's a tilt in his expression you can't read cleanly; it's a policy pitch wrapped in charm, and something else that is methodical and human-sized. That ambiguity is familiar now — neither wholly enemy nor ally."
    show amara_vale at right:
        zoom 0.7

    amara_vale "We need the covenants to include enforceable rehousing clauses and transparent audits. No side-letters."

    marco_voss "Fine. Transparency is good for business as well as the town.' (He smiles.) 'Open audits reassure investors."

    "Elias 'Eli' Navarro" "And community oversight? People need to have standing to review expenditure reports."
    "Marco Voss: (A fraction of a pause.) 'Agreed. Public oversight panels — technically sound, periodically reviewed. We build trust in the structure; the funding follows.'"
    "Hal watches the exchange, a long breath passing between his shoulders. He steps forward, voice soft but unmistakable."
    show harold_hal_finnegan at center:
        zoom 0.7

    harold_hal_finnegan "Money can fix a lot of things, but it's not the same as care. You can write a covenant, Mr. Voss, but you can't legislate the town's memory. So the question is whether your investment respects that memory."
    "Marco looks at Hal, and for the first time there's a small, human ripple across his face — a concession no brochure could sell."

    marco_voss "I respect that. I grew up in a town that lost more than it needed to. I want to make sure doesn't happen here."
    "The words land with a double-weight of possibility and caution. You do not assume full conversion; you hold the complexity like a lantern: it illuminates without removing shadow."
    hide marco_voss
    show miriam_santos at left:
        zoom 0.7

    miriam_santos "We'll hold you to it,' she says. 'Public meetings, clear timelines, and penalties for breaches. No quiet deals."
    "Marco nods, not trailed by defensiveness but with a corporate man's careful acceptance. The room exhales."
    "You look at the stitched map again, the raised promenades and mangrove lines like sutures across a town's wound. The work is not finished. The Vote looms; the next wave of storms will test both steel"
    "and social contracts. But here — in the hum of sensors, in the steady hands of volunteers, in the meeting of policy and craft — you feel a tide of something that counts: structures in place,"
    "practices adopted, relationships deepened."
    "Elias 'Eli' Navarro squeezes your hand."

    "Elias 'Eli' Navarro" "This doesn't end at signatures. It starts a new phase."

    amara_vale "We know how to do phases."
    "He smiles — part relief, part mischief."
    "Your chest lightens with the kind of hope that is not naïve. It is a hope earned by labor and compromise, by holding firm on the parts that matter and bending where necessary without breaking who"
    "you are. You look at the town's stitched map once more, tracing the thread that runs through all the work: a slow commitment to keep trying."
    # [Page-Turn Moment]
    "You stand at the Beacon's doorway and look out over the boardwalk. Lamplight pools on raised planks; the mangroves reflect a silvered sky; a small cluster of residents compares notes under an umbrella. Ahead is another"
    "meeting, another vote, another storm season to prepare for. Behind is the months of work that made this moment possible. For the first time in a long while, the horizon feels like a promise you can"
    "meet one plank at a time."
    hide amara_vale
    hide harold_hal_finnegan
    hide miriam_santos

    scene bg ch13_10625f_4 at full_bg
    # play music "music_placeholder"  # [Music: Strings rise into a warm, ascending chord — resolute and hopeful]
    # play sound "sfx_placeholder"  # [Sound: Distant gull call, the soft rattle of a sensor, the murmur of a town alive with plans]

    scene bg ch13_10625f_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter22
    return
