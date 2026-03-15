label chapter5:

    # [Scene: Aquila Developments HQ — Conference Room | Late Afternoon]

    scene bg ch5_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low HVAC hum, the tick of a digital clock, the soft shuffle of papers]
    # play music "music_placeholder"  # [Music: Sparse piano with a distant, descending cello line]

    scene bg ch5_4001e7_2 at full_bg
    "You arrived expecting access; you did not arrive expecting the feeling of being audited by sunlight. The room is too clean — polished wood, brushed metal chairs, a model that makes marshland look miniature and tidy — and that sterility presses against something raw in your chest."
    "You smell coffee and something clinical: citrus disinfectant undercut by warm leather. The air tastes of other people's certainty. Your pen leaves a thin, nervous track in the margin of the amendment as you read the"
    "phrasing again: living shoreline strips, community-run maintenance trust, job training programs tied to local families. Words you wrote to protect the town sound, in this room, like a theorem under examination."
    show cass_adler at left:
        zoom 0.7

    cass_adler "That's sharp phrasing, Maya.' (They let the name fall easy across the table, watching how it lands.) 'You made the maintenance trust language hard to game. The training programs are—well, honest. You're making a good case for community buy-in."
    show maya_rios at right:
        zoom 0.7

    maya_rios "I wrote it so that the trust can't be circumvented through shell organizations.' (You keep your voice steady; the practiced cadence of someone used to conferences and cross-examination.) 'And the workforce provisions have staged milestones. Local hires first, training credits tied to demonstrable tenure."
    "Cass's expression flickers — a careful, practiced warmth. They tap their smartwatch, and a recessed screen brings up the pilot funding numbers, a green bar climbing to an attractive total."

    cass_adler "Good. We can mobilize capital immediately. Pilot funding gets you crews, materials, legal support for the trust's charter. You sign the amendment, we kick off within thirty days."
    "Mayor Jonah Cruz leans forward, his palms flat on the table as if feeling for the map beneath the model. He tastes the deal with the same pragmatic calculation he'd use on a budget sheet."
    show mayor_jonah_cruz at center:
        zoom 0.7

    mayor_jonah_cruz "Immediate funding matters. Grants and federal aid move slow. This could be the difference between a pilot that demonstrates the marsh' viability and us waiting until after the next storm—if there is a next storm."
    "You blink at him. His face is the face of the town: worn, hopeful, afraid. The room seems to contract into the space between the model's sugar-white shoreline and the tiny pilings that mark docks you know by name."
    "Maya Rios: (You look at the amendments again, into the small paragraphs and the clauses that feel like doors.) 'What are the strings, Cass? We need transparency on land easements and any clauses that cede regulatory authority.'"
    "Cass lets out a soft, practiced exhale that sounds almost like an apology."

    cass_adler "Reasonable. The pilot requires temporary easements to place movable protections and elevated boardwalk testing. Some dock relocations are on the table — structurally necessary to make the boardwalk continuous. And there is language for phased regulatory alignment: a trust handles day-to-day maintenance, but certain long-term approvals require regulatory harmonization with Aquila's frameworks."
    "The words settle like silt in your mouth. 'Regulatory harmonization' is corporate syntax for ceding teeth."
    "Eli Navarro sits to your left. He has his arms folded, one knee half-slid forward like he's ready to stand. His jaw works. He has watched barges and weathered men for longer than many in this"
    "room have watched projectors. He speaks with the flat, irrefutable cadence of someone who measures risk in salt and rope."
    hide cass_adler
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "Temporary easements become permanent more often than you think. Elevated boardwalks aren't just about walking — they're about rerouting livelihoods. Who funds dock relocation? Who pays for the lost seasons while you dig and elevate?"

    mayor_jonah_cruz "Aquila offers compensation packages. Legal teams will be involved to ensure fairness. We can write in dispute mechanisms."
    "Maya Rios: (Your mouth tastes of metal.) 'Dispute mechanisms mean lawyers, and lawyers slow things down until the wateroverwhelms the people who need help now. Compensation doesn't restore the way families work the tide.'"
    "Cass's eyes go icy for a heartbeat, then soften. There's a measure of calculation and, under it, something like regret."
    hide maya_rios
    show cass_adler at right:
        zoom 0.7

    cass_adler "We can escrow additional funds for displacement mitigation. We can put community representatives on an oversight board. Maya, that's why your language matters. If you chair the oversight and the trust, you have a seat to veto egregious changes."
    "Maya Rios: (You almost laugh, but it comes out like a breath.) 'A seat doesn't stop the tide from eroding a way of life. A seat can be tokenized on paper.'"
    "A pause. The model's tiny marsh grass rattles faintly under a ventilation gust. You imagine docks you know by heart pushed back, boats fumbling an altered harbor. The memory of the forecast you once misread —"
    "the one that still makes your stomach clench like a fist — colors every risk assessment. You think of the kids Rosa teaches, of Eli's father's calendar with hand-marked tides, of the smell of smoked fish"
    "hanging in Harborfront Lane."

    menu:
        "Ask Cass for an explicit clause limiting easements to 'pilot-only' with automatic sunset":
            "Cass looks thoughtful, thumbs a line on their tablet. 'We can draft a sunset clause—temporary moratorium for three years—but legal will push for renewals. It'll at least give you leverage.'"
        "Request a refundable escrow for fishermen displaced during work":
            "Mayor Jonah nods, relieved you said something about immediate material support. 'Escrow is acceptable. It buys time for training and ensures folks aren't left adrift.'"

    # --- merge ---
    "The conversation continues with Cass folding their hands, leaning in as if the model itself holds the answer."
    "Cass folds their hands, leaning in as if the model itself holds the answer."

    cass_adler "We're offering leverage and resources. Leverage is not the same as control. But scale matters — the pilot's visibility will drive further municipal and federal investment. If you're inside, you can steer those next steps."
    "Maya Rios: (You can feel the moral bifurcation as a physical ache.) 'If I sign, I'm choosing this pilot's compromises over the risk of being excluded. If I don't, I'm choosing to protect a set of local practices that corporate frameworks might not be able to catalog by line-item.'"
    "Eli's voice drops; there's a pleading edge no model will show."

    eli_navarro "We need results and fast, Maya. People lose their boats, and they lose faith. If you can steer and hold them accountable from inside, you do it. But don't let them knit a noose and hand it to you as a rope."
    "Mayor Jonah Cruz exhales. He looks at you with a weight that's both civic and personal; he has seen votes cost friends their businesses and laws cost them the sullen dignity of survival."

    mayor_jonah_cruz "Whatever you do, do it with a communication plan. The town needs to know why you did it and what the alternatives would look like if you refuse. We can't fracture trust more than it already is."
    "Maya Rios: (Your notebook is open to a page where the amendment's clause sits, inked in a hand that still shakes from the memory of a past forecast. You trace the letters with your thumb as"
    "if trying to erase the shape of a hard decision.) I draft with both hands: the protective language you can see, and the realities you can't print without names and accusations."
    "Cass taps the tabletop once. The sound is small but precise."

    cass_adler "There's also another route. If you think public pressure could secure better terms, there are ways to bring certain elements to light. Transparency can be catalytic."
    "You glance at Cass — at the polished tablet, the matte watch, the subtle tilt of compassion mixed with calculation. Their offer hangs between an invitation and a warning."

    menu:
        "Ask Cass quietly if they would leak selectively to force renegotiation":
            "Cass's smile becomes something complicated. 'I didn't say I'd leak—but I said transparency can be catalytic. There are people at Aquila who prefer the optics of being reformed to the optics of being nailed to a headline.'"
        "Look to Eli and ask for his read—stay silent to protect internal talks":
            "Eli's gaze is a raw thing. 'If you bring a fight publicly, you risk losing their cooperation and your seat. If you stay, you risk losing the town's trust. Either way, we'll stand with you—but I won't lie about the cost.'"

    # --- merge ---
    "The room holds its breath as you weigh options."
    "Your chest feels like low tide: lots of exposed, sharp edges, and the knowledge that once the water comes back, it will reshape everything it touches. The room's light grows long; outside, the real coastline is"
    "its own indifferent scale model — not a neat presentation but a messy, living negotiation."
    hide mayor_jonah_cruz
    show maya_rios at center:
        zoom 0.7

    maya_rios "So the options are immediate funding and seats at the table with strings; creating public pressure to force better terms; or rejecting Aquila outright and risking intimidation and financial collapse. Those are the forks."

    cass_adler "Exactly. Each has costs and scalars. We can compromise in ways that preserve more than we lose, or we can make principled stands that cost us leverage. I'm telling you honestly because I respect what you bring to the language here."
    hide eli_navarro
    show mayor_jonah_cruz at left:
        zoom 0.7

    mayor_jonah_cruz "Whatever you choose will change how people vote, how they trust each other, and how fast we can act. Choose carefully, Maya."
    "Eli reaches across the table, not to take your hand but to close a small airspace between you — a gesture of solidarity, a tether you can feel."
    hide cass_adler
    show eli_navarro at right:
        zoom 0.7

    eli_navarro "I'll back you. I don't know which is right. I know what I don't want: to watch something that could've been saved get dismantled because we couldn't get a seat or didn't protect the people while we fought."
    "Maya Rios: (You imagine signatures, legalese, press releases, and the quiet Sunday mornings on Harborfront Lane that might never be the same.) The pendant at your sternum is warm; your notebook crackles under your palm like a small, obedient life."
    # play music "music_placeholder"  # [Music: The cello sinks to a single, unresolved note; the piano repeats a minor motif]
    hide maya_rios
    hide mayor_jonah_cruz
    hide eli_navarro

    scene bg ch5_4001e7_3 at full_bg
    "You feel the edge of a moral bifurcation settle into your bones: sign and secure material influence but risk the slow erosion of community trust; leak and hope public scrutiny can force change but compromise Cass"
    "and invite retaliation; or go public and burn bridges, trying to rally hearts but risking legal and financial retaliation."
    "You breathe. The room waits, a held exhale."

    menu:
        "Sign the pilot amendment to secure funding and some design control.":
            jump chapter7
        "Secretly share the firm’s internal schematics with a journalist to force transparency.":
            jump chapter15
        "Refuse to sign and publicly expose the invasive parts of the plan, urging the town to reject Aquila.":
            jump chapter16
    return
