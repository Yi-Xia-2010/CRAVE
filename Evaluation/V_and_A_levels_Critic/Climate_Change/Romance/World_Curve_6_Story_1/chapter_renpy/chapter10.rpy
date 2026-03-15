label chapter10:

    # [Scene: Nueva Mar Municipal Hall | Late Afternoon]

    scene bg ch8_b0bdfc_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low mechanical hum from ventilation, murmured conversations, a phone buzzing against a wooden counter]
    # play music "music_placeholder"  # [Music: Urgent strings building, a bright undertow that pushes forward]
    "You return to the Hall with the signed amendment folded in your bag like a small, warm thing. The paper's weight keeps your hand steady even as everything around you accelerates. The plaza's clock still ticks, but now the time it marks feels elastic—stretching and snapping with every new demand."
    "You smell coffee and printer toner, and beneath them the sharper tang of seawater on someone's jacket from the Low Row. The air tastes like anticipation and salt."

    scene bg ch8_b0bdfc_2 at full_bg
    # play music "music_placeholder"  # [Music: Strings spike, then settle into a brisk, pressing rhythm]
    "You haven't been back in this corridor since the amendment was signed; the building that felt like the axis of process now thrums with consequence. A hastily posted notice on the municipal board blinks: AMENDMENT RELEASED — PUBLIC FEEDBACK WINDOW: 72 HOURS. Comments encouraged."

    "Your phone vibrates before you can read it. The message is blunt: INVESTOR CONSORTIUM" "Delay risks withdrawal."
    "The hallway narrows as you move toward the planning office. Voices fold and refold into the hum—some urgent, some hushed. You can feel pressure collecting like weather."
    "Dr. Sima meets you in the corridor, sleeves rolled, laptop clutched to her chest. Her face is a map of lines and light: tired, precise, alive."
    show dr_sima_raza at left:
        zoom 0.7

    dr_sima_raza "Maya. Good—you made it in. We need to talk models."
    "You follow. Her steps are quick, her hands flicking through data on the tablet, which leaves a faint salt-smudge on the screen."

    dr_sima_raza "The amendment buys us legal space to pilot wetland corridors, yes. But the forecast… it's not a political document. It's a physics document. The seasonal surge—"
    "You cut in because there is no time for preamble."
    show maya_corvin at right:
        zoom 0.7

    maya_corvin "Is it worse than last year?"
    "Dr. Sima: (She exhales, not quite answering.) 'The projection curve sharpens in ways we feared. If the storm aligns with a high tide event, the stress on coastal buffers doubles in a single surge. But—and this"
    "is critical—the ensemble is still probabilistic. We cannot overfit to a single high-intensity scenario and ignore adaptive benefit across years.'"
    "Her words are careful, calibrated—practice: someone who knows how to hold two uncomfortable truths at once. You feel the tug of both urgency and restraint pull in your chest."

    menu:
        "Ask Sima for the worst-case readout":
            "Sima's eyes narrow; she slides a compact graph across the table, numbers jittering like short-run waves. You taste metal as you scan—it's sharper than you'd hoped."
        "Press her on adaptive measures, not just models":
            "Sima relaxes fractionally. She leans in and starts outlining targeted sensor deployments and buffer plans, her voice a metronome of possibility."

    # --- merge ---
    "Scene continues"
    "The room door opens. Elias Kahn stands framed in the corridor, his trench coat damp at the hem from the drizzle outside. He looks at you like a harbor light—steady, deliberate."
    show elias_kahn at center:
        zoom 0.7

    elias_kahn "You okay?"

    maya_corvin "As okay as anything is these days. What's the municipal read on the investors?"
    "Elias Kahn hesitates, then folds his hands on the table as if weighing them. He moves like someone who can feel both sides of a coin."

    elias_kahn "They issued a formal statement. They'll consider reallocation if approvals don't proceed on their timeline. They're not bluffing, Maya. I can secure signatures from two key council members, but I need a little breathing room to tie legal language down. Public statements from our side—right now—could spook them and put those signatures at risk."

    maya_corvin "So you're asking me to—"

    elias_kahn "Not to shut up forever. To hold public amplification for seventy-two hours while I lock the amendment into a binding schedule. I'm trying to convert momentum into something irreversible."
    "There is a pause, the kind that contains petitions and murals and the faces of people who don't want to be steamrolled. Your empathy flares—bright, immediate. You think of Rafi's hands, of Lio's mural, of Mrs. Ortega's steady knitting at the center."

    maya_corvin "If you succeed, what's guaranteed? What if signatures are paper and the investors still pull?"
    "Elias Kahn: (He meets your eyes, amber steady.) 'Then we still fight. But those signatures make it harder for the administration to say no. They make it politically costly to withdraw.'"
    "The urgency in his voice is real, but your gut pushes back. Your instinct is to name the risk publicly, to make the investors' threats visible and shame them into staying. Silence feels like complicity, but noisy exposure could collapse the fragile chain he's building."
    "Across the hall, a flash of color catches your attention—Lio's lacquer-bright mural in progress on an adjacent scaffolding, streaming live through a municipal feed. Lio sprays a wave that breaks into a stitched seam of signatures and faces. His hoodie is paint-splattered; his grin is furious and incandescent."
    "A neighbor shoulder-taps you—a volunteer from the Low Row, eyes blazing."

    "Neighbor" "People want a referendum. They want to vote it in themselves."
    "The word referendum lands like a bell. You can feel the corridor vibrate with it; the word carries both democracy and delay."
    "You pivot to the source of the growing storm: Camila 'Kai' Navarro's message. It's short, clinical, generous in tone."

    "Camila 'Kai' Navarro (text)" "Private meeting. Offer: enhanced monitoring + accelerated contingency builds. Timeline ceded to firm oversight during high-risk window. Meet today?"
    "Your stomach tightens. Kai's offer is everything immediate protection looks like—sensors, drones, physical works—but wrapped in corporate precedence. You think of the seawall's sterile silhouette and what it would mean to hand the community's timetable to a firm with profit on its ledger."

    maya_corvin "Elias, Kai's proposing to fast-track if we accept their oversight."
    "Elias Kahn: (His jaw tightens.) 'That's… complicated. It buys us hardened defenses fast, but it hands control to private timelines. It undercuts long-term stewardship.'"
    "The corridor seems to pulse. Dr. Sima's forewarning echoes. Rafi's hands, when he arrives, tremble so visibly you can see the salt dry between his fingers like a map."
    "Rafi: (Voice rough) 'They want to cut us out with data thresholds and surveillance rules. They say it's for the sensors, but it's control. We need to own the monitoring.'"

    "Lio, spraying the mural, shouts up to you through the open air" "If you cave, they're going to take the art too!"
    "You feel the pressure mounting so fast the corridor walls feel like they might close. But beneath the pressure is a current you recognize: this is what movement feels like—compressed, riven with possibility and risk."
    "You take a breath that tastes like rain. Your empathy isn't a weakness; it's a fuel. Your stubbornness isn't a defect; it's direction. The amendment is a foothold, but the mountain above it is steep and weathered."
    "Camila 'Kai' Navarro arrives without fanfare, as she always does—efficient, precise, an edge of polished metal in human form. Her field suit is immaculate despite the field tension. She smiles in a way that is almost a compliment."

    "Camila 'Kai' Navarro" "Maya. Elias. I won't waste time. The investors will move if the city stalls. My offer is specific: an expanded monitoring framework—drone swarms, real-time sediment and tide sensors, automated response triggers. We can put structural protections in place before the surge window. In return, we oversee construction sequencing to ensure deployment within your only narrow safe window."
    "Her tone is crisp; the proposal is sterile and powerful."

    maya_corvin "And oversight means…?"

    "Camila 'Kai' Navarro" "Operational precedence. The sequencing must be centralized for efficacy. You retain community liaison roles and a seat on the oversight committee. Your team helps define ecological passes, but final deploy decisions rest with my firm during the high-risk period. It's not forever. It's functional."
    "You feel the offer like a hand extended—warm, practical—but there is a cold steel ring at the base of the fingers. Control slides to her firm when decisions are most consequential."
    "Elias Kahn: (He looks between you and Kai, then back to you.) 'If we accept this, we get fast defenses. But we risk setting a precedent that private deadlines trump municipal or communal processes. It could be a one-time contract or a long-term shift. Maya—what do you need to decide?'"
    # play music "music_placeholder"  # [Music: Crescendo of strings; percussion staccato like rushing tide]
    "Dr. Sima: (She steps close, voice low.) 'All options have trade-offs. A referendum amplifies democratic voice but costs time and could trigger investor exit. Municipalizing the amendment quietly anchors policy but alienates activists and could slow grassroots oversight. Kai's offer gives physical protection quickly but risks institutional capture.'"
    "Her hands move, sketching invisible diagrams in the air—trade-offs arrayed like a star chart."
    "Rafi drops a stack of weathered sample reports on the table; the edges are damp where he gripped them too long. Lio's mural stream goes viral in a thread on the municipal monitor: #LowRowLives #VoteTheTide. The"
    "hall fills with a kinetic noise—messages, hashtags, a crowd forming outside that you can hear like a distant wave."
    "Inside, everything accelerates to a near fever. The choice isn't between safe and unsafe; it's between urgent imperfect goods."
    "You close your eyes for a beat and feel the amendment in your bag like a small, breathing thing. You remember folding it, the pen scratch, the collective intake of breath. Hope isn't naive here; it's chosen. And so is risk."

    menu:
        "Call for an impromptu town hall in the plaza":
            "Your call reverberates: volunteers mobilize, speakers line up, but the timeline tightens—any public assembly draws media and investor eyes immediately. The crowd outside the Hall thickens; chants begin."
        "Agree to Elias's slow seal while you push for stronger oversight clauses quietly":
            "Elias exhales, relief and tension braided together. He nods, promising to file amendments that protect community oversight, but you can see the compromise carved into his face—some concessions already baked in."

    # --- merge ---
    "Scene continues"
    "You feel the heat of the moment like a furnace—expectation, resolve, the scent of wet paint, the tang of metal, the pulse of a city on the edge. This is not paralysis; it is a pivot"
    "place—a logic hub where direction matters more than words. You are acutely aware that whatever you choose will echo: in Lio's mural, in Rafi's hands, in Dr. Sima's models, in the municipal record."
    "Your breath comes hot and fast now. The strings in the hall climb—bright, insistent, like surf on rock—and you know the next decision will not just decide a project but define who holds the levers when the sea comes in."
    # play music "music_placeholder"  # [Music: Crescendo of strings; percussion staccato like rushing tide]
    "You open your mouth to speak—then stop, because this is a choice that will need a word that binds it."

    menu:
        "Force a public referendum.":
            jump chapter12
        "Trust Elias and finalize the municipal amendment quietly.":
            jump chapter22
        "Accept Kai's conditional expanded monitoring to fast-track protective construction.":
            jump chapter29
    return
