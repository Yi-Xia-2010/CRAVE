label chapter13:

    # [Scene: Harborfall Town Hall | Morning]

    scene bg ch13_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, somber piano with a slow heartbeat bass]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, muffled traffic of a town waking, the soft rustle of pages]
    "You sit with the binder heavy in your lap and feel the referendum's narrow victory like cold water in your bones — relief braided with a new, sharper fear. It bought you leverage, and with leverage"
    "came strings: conditional funding, stewardship clauses, oversight boards. Everything must be written so it cannot be unmade, and yet the words you choose now will also decide what is allowed to be done quickly."
    "Your hand drags over a clause about 'expedited timelines under emergent threat.' The sentence is efficient, legal; it tastes like iron. Kaito Sato leans in opposite you, a tablet balanced on his knee, eyes flicking between"
    "your notes and his sensor-readings. His presence steadies you, but where there was once easy rapport there's something taut — as if both of you have folded yourself around the referendum's new edges and the folds"
    "are sharp."
    "Mayor Elena clears her throat and smooths her blazer. Across from her, Lucia 'Lux' Moreno—polished and precise—tilts her head like a scientist studying a specimen. Her smile is the same practiced warmth as ever; it doesn't reach the steel-gray of her eyes."
    show mayor_elena_rossi at left:
        zoom 0.7

    mayor_elena_rossi "Maya, the council wants clarity on oversight language. LuxCorp agrees to the stewardship board in principle, but—' (she looks toward Lux) '—there has to be a mechanism for timely deployment. Voters will not tolerate waiting."
    show lucia_lux_moreno at right:
        zoom 0.7

    lucia_lux_moreno "Timely deployment saves lives. We will not jeopardize safety for a theoretical purity. Our engineers can deliver within months if we are permitted to stage operations without bureaucratic delay."
    show maya_inoue at center:
        zoom 0.7

    maya_inoue "Safety isn't theoretical,' you say. Your voice is measured because everything else is already raw. 'But neither is stewardship. The board has to have teeth. We need transparency on sensor data access, on material sourcing, on subcontractor vetting. Otherwise the money will buy speed at the expense of the things that keep the town together."
    hide mayor_elena_rossi
    show kaito_sato at left:
        zoom 0.7

    kaito_sato "I can draft the transparency protocol. Open APIs for the sensor feeds, immutable logs for construction sign-offs. If the community can see timelines and data, they can hold contractors accountable in real time."

    lucia_lux_moreno "Open APIs create liabilities. Investors expect certain protections. We can carve out a public dashboard that shows non-sensitive data, and a secured access tier for engineering telemetry."
    "You feel the word 'carve' like a small incision. It promises shape while removing flesh. You press a pen to the page and write 'public dashboard — non-sensitive data' but in your head the words multiply into levers and loopholes."
    hide lucia_lux_moreno
    show mayor_elena_rossi at right:
        zoom 0.7

    mayor_elena_rossi "We need the funding. We need the engineers. If LuxCorp walks, we lose everything. But if we don't circumscribe them...' (she shakes her head) 'Maya, you negotiated the referendum. The town gave you the mandate to keep them honest."
    hide maya_inoue
    show lucia_lux_moreno at center:
        zoom 0.7

    lucia_lux_moreno "We want to protect Harborfall as much as you do, Mayor. The quicker we act, the fewer people will be displaced when the storms come."
    "You watch Lux's hands while she speaks — precise fingers that have signed more contracts than you can imagine. There's a gentleness in the tone, but you know how quickly 'quicker' can become an excuse to skip consultation."

    menu:
        "Insist on full public access to the sensor feeds now":
            "You push hard, tapping your pen to the clause. 'Open data now, no tiers,' you say. The room tightens. Kaito exhales, a mixture of admiration and worry, and Lux's smile thins to a line. Mayor Elena's fingers drum once and she asks quietly about liability."
        "Request a phased transparency model tied to legal audits":
            "You offer a compromise: phased transparency with legally mandated audits every quarter. Kaito nods, relieved; Lux inclines her head, calculating. Mayor Elena allows a small, grateful smile — it's enough to move the conversation forward, but the scent of concession lingers."

    # --- merge ---
    "The meeting proceeds."

    lucia_lux_moreno "A phased model is workable. We can include third-party auditors. It preserves investor protections and provides the town with oversight."
    "Kaito Sato catches your eye and offers a small, private smile — the one he used to offer across soldering irons and sensor arrays. You accept it because you both know you are trying to thread a needle through a moving storm."
    # [Scene: Kaito's Field Lab (Workshop) | Afternoon]
    hide kaito_sato
    hide mayor_elena_rossi
    hide lucia_lux_moreno

    scene bg ch13_e67f19_2 at full_bg
    # play music "music_placeholder"  # [Music: Soft, anxious strings]
    # play sound "sfx_placeholder"  # [Sound: The hum of a centrifuge, the staccato tap of a stylus on glass]
    "You and Kaito spend the afternoon drafting the sensor transparency protocols. He talks in small, technical sentences that carry enormous moral weight."
    show kaito_sato at left:
        zoom 0.7

    kaito_sato "We can timestamp every feed with a verifiable hash. Data gets pushed to the public dashboard after a thirty-minute buffer to scrub personally identifying information. For construction telemetry, contractors upload photos with geotags and machine signatures. If sign-offs don't match the plan, it's flagged."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "And who flags? Who acts?"

    kaito_sato "The stewardship board reviews flags. We give community liaisons admin privileges to request immediate pauses if there's probable cause. The auditors can enforce fines clothed in legal agreements. And there's an emergency clause that allows the Mayor to call for a temporary halt."
    "You both fall silent, imagining a world where flags are heeded rather than buried. Outside, rain hits the boathouse roof in a steady, metallic percussion."

    kaito_sato "We did the right thing, Maya. This is as open as we could make it."
    "You want to believe that. You want to believe that the bindings on paper will hold when machines and money press against them. For a moment, in the cluttered lab light, the world seems to tip toward that possibility."
    # [Scene: Harborfall Promenade | Construction Begins]
    hide kaito_sato
    hide maya_inoue

    scene bg ch13_e67f19_3 at full_bg
    # play music "music_placeholder"  # [Music: Low percussion, a distant siren that never resolves]
    # play sound "sfx_placeholder"  # [Sound: Clink of chains, shouted instructions, a hammer tapping deadlines into place]
    "Construction moves fast. Lux's engineers work with practiced efficiency; their teams carry schedules on tablets, their language of milestones and critical paths smoothing over the town's rougher edges. You stand on the promenade with Tomas, watching"
    "barges drop rock where the old shore had once crept up to the sea grass."
    show tomas_bianchi at left:
        zoom 0.7

    tomas_bianchi "They did this job in three days where my father took three months to shore a single bank. You see that, Maya? Those stones will settle wrong."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "We wrote in subcontractor vetting. We insisted on marine ecologists on-site, on slow placement near eelgrass beds."

    tomas_bianchi "Paper's not a net when the tide comes different."
    "A foreman — one of LuxCorp's subcontractors — clamps a radio to his vest and gives you a brisk nod, the kind of nod that means business has been done and questions will be answered later. You approach, the binder your weight."

    maya_inoue "We need a hold on any placement within thirty meters of the eelgrass corridor until the inspectors confirm soft placement techniques."

    "Subcontractor" "Departure window's tight. If we pause, we hit the next tide schedule and the crane charter costs spike. Orders came down to keep pace."
    "You can feel the familiar logic: time is money; money bends plans. You remember drafting the clause that allowed 'expedited timelines under emergent threat.' Today's tide looks like a threat that insists on immediacy. The clause that was meant to be a safeguard is now a lever for speed."

    menu:
        "Insist on immediate soft-placement review despite delays":
            "You plant your feet and call the inspectors. Machines idle, men shift uneasily. The subcontractor mutters about charter costs. Kaito appears at your shoulder, his jaw tight, and you feel the cost of pausing settle into everybody's shoulders."
        "Reluctantly permit them to continue under strict photo logging":
            "You sign off with a stipulation: continuous photo geotags and an on-call ecologist. The crane keeps moving. Kaito's fingers rub his temple; Tomas spits into his palm like an old prayer. You've bought time and traded risk."

    # --- merge ---
    "The project proceeds under strict logging and oversight."
    "You choose compromise — the project moves forward under strict logging and promised oversight. It is what the town wanted: protection and money. It is also a promise you've learned to fear."
    # [Scene: Fishing Cove | One Month Later]
    hide tomas_bianchi
    hide maya_inoue

    scene bg ch13_e67f19_4 at full_bg
    # play music "music_placeholder"  # [Music: Sparse, descending cello notes]
    # play sound "sfx_placeholder"  # [Sound: The slow plop of something lost in the water, wind through a broken net]
    "The first time you see the collapsed eelgrass corridor you think your eyes are betraying you. The mats have thinned to ragged strips. The water tastes and smells different — a metallic tang like pennies and"
    "old engines. The sediment has shifted; small channels where fish used to move are clogged with the aftermath of rock placements."
    "Tomas stands with his net empty, shoulders bent as if the sea's absence sits there personally on him."
    show tomas_bianchi at left:
        zoom 0.7

    tomas_bianchi "We used to set the net here and bring in enough to feed the block for a week. Now it's like reaching into paper."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "The monitoring flagged increased turbidity at the time of placement. We recorded stress events in the eelgrass's photosynthetic indicators. We should have stopped it then."

    tomas_bianchi "Would more stopping have saved my father? Would it have kept the kid with the little boat who left last week? They left because the work changed what we catch."
    "Kaito Sato stands a few paces away, his hands shoved into his jacket. He had been a quiet energy in all the meetings; now the quiet has the edge of something vertical and hard. He isn't tempering you anymore."
    show kaito_sato at center:
        zoom 0.7

    kaito_sato "We calculated probabilities. We included buffers. The models said low risk of persistent collapse."

    maya_inoue "The models didn't hold when the subcontractor compacted the rock too close to the bed. The logs showed deviations. The photos were inconsistent with the placement notes. Someone rushed and we trusted the chain would catch it."

    kaito_sato "We trusted institutional safeguards, Maya. We built contingencies into clauses, but they were only as strong as the people enforcing them."

    maya_inoue "Who enforces when enforcement is a line item that can be deferred to save costs?"
    "There's a silence heavy enough to be a presence. You want to reach for Kaito's hand like you did the night you argued over sensor firmware, but his shoulders angle away in a subtle, almost invisible"
    "withdrawal. Where he used to press his palm into the back of your hand, there is now simply the empty gesture of someone measuring distance."

    menu:
        "Step closer to Tomas and offer to help salvage what you can":
            "You kneel and run your fingers through the cold, silt-thick water, trying to find any living blade to anchor hope to. Tomas' eyes mist briefly. Kaito watches, mouth a thin line, and you taste salt that isn't only ocean."
        "Stand back and photograph the damage for the audit":
            "You lift a phone and record the eelgrass collapse, the geotag stamping the moment into immutable time. Kaito steps forward, his voice clipped as he explains chain-of-custody protocols to a junior auditor. The world begins to be translated into paperwork — a comfort and an indictment."

    # --- merge ---
    "The aftermath is documented and the community begins to disperse."
    "People begin to leave. Not all at once — families pack at different paces, local trades evaporate into city postings, younger fishers sell boats they can't afford to maintain. You watch a neighbor across the cove"
    "load a battered fridge into the back of a rented truck and feel the small avalanches of departure as each item is a vote that this place will not be the same."

    kaito_sato "We can escalate this to the auditors. We can demand an independent review, fines, remediation."

    maya_inoue "We will. We have to."

    kaito_sato "Why did the subcontractor deviate? Who signed off? The logs will show it."

    maya_inoue "Because the chain is made of people who answer to timetables too. Because 'expedited' became permission, and permission silenced caution."
    "Kaito's jaw tightens, and for the first time in months, you see a line in him that you can't reach. It's not anger — not exactly — it's a distance that looks like disappointment, and disappointment often hardens into resignation."

    tomas_bianchi "We wanted protection from storms, not to watch the shore turn against us. How do you protect a town if the sea keeps taking what feeds the town?"
    "The question hangs between you like a bell that will not stop ringing."
    "You walk the line of damaged eelgrass, boots sinking into a smell of old salt and new rot. Each blade you touch is a little thing that held the town together in ways no clause could"
    "quantify. You think of your brother — of promises you made in the dark after the storm — and wonder which promises you kept, and which you traded for a brittle kind of safety."
    hide tomas_bianchi
    hide maya_inoue
    hide kaito_sato

    scene bg ch13_e67f19_5 at full_bg
    # play music "music_placeholder"  # [Music: A single violin sustaining a note that frays at the edges]
    "You try to catalog the losses in your head: livelihoods, trust, the mild, everyday certainties that used to hold Harborfall upright. The hybrid you designed — a scaffold of compromise — creaks under the weight of"
    "human impatience and corporate timetables. Where you had hoped to braid nature and engineering into a durable rope, it has frayed into strands that catch on the town's sharp edges."
    "Kaito Sato stands apart, jaw set, watching a wave lap at a ruined seam of shore. Tomas folds his hands into his jacket and looks at the empty net slung over his shoulder. Mayor Elena's messages"
    "go unanswered; LuxCorp issues a statement that reads like a cleansing rinse of corporate language. The stewardship board convenes, but convening is not fixing."
    "You close your eyes for a moment and feel the salt of other people's small departures on your skin. The referendum passed. The town has money and a mandate and a map of clauses. Yet the map shows limits you did not foresee."
    "A gull cries and the sound is thin."
    "Your notebook sits in your mind — pages of actions you still owe. You add a new line, unsteady: investigate subcontractor deviation; call independent auditors; propose emergency eelgrass remediation fund; request immediate halt to further rock placement pending review."
    "The list makes you breathe faster. The fall you felt when you chose the referendum has widened; it isn't the defeat of a single vote but the unspooling consequences of compromises that were meant to save the town."
    "You look out across the cove, to where the eelgrass thins into nothing, and realize that the next move will not be about policy drafts alone. It will be about who you can still reach —"
    "who will stay, who will leave, and whether the town can afford the price of being partly saved."

    scene bg ch13_e67f19_6 at full_bg
    # play music "music_placeholder"  # [Music: Piano and cello descend together into near silence]
    "You take a breath that tastes of iron and cold sea. You are tired and taxed and unmoored in a way you recognize as grief. You cannot fix everything with clauses. You cannot hold everyone's hands"
    "and be everywhere the town needs you to be. But you still have ink, leverage, and a stubbornness that is part guilt and part love."
    "A crack of thunder, somewhere distant, suggests the weather has heard all of this already."
    "You straighten, the binder a hard weight against your ribs, and set one foot forward into the messy, necessary work of response."

    scene bg ch13_e67f19_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade to a single, unresolved chord]
    "The town waits. So do the auditors, the engineers, the people who left and those still standing. The shoreline will continue to unravel and you have to decide how to pull at the threads."

    scene bg ch13_e67f19_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter14
    return
