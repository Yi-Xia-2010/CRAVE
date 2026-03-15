label chapter5:

    # [Scene: Conference Room | Morning]

    scene bg ch5_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Fast-tempo strings layered with a low, urgent electronic pulse]
    # play sound "sfx_placeholder"  # [Sound: Rain pattering against the window; distant gulls cry]
    "You step into the conference room with the taste of last night's rooftop—salt and copper and the afterimage of Elias's hand in yours—still on your tongue. The room smells of coffee, printer toner, and a faint"
    "metallic tang that makes your teeth ache with the memory of storm-sheathed rebar. Across the table, Celeste Park is already seated, immaculate as always, the corners of her folder aligned like tiny cliffs. Elias stands by"
    "a projection screen, tablet lit with slides that flip too quickly for comfort."
    "Your breath is shallow. The town is not a thought here. It's a ledger: lines and clauses and the names that will appear next to them. But you can feel the Commons behind your ribs—mud under fingernails, Rae's laughter, Tommy's steady hum—and they make your hands curl into new-remembered shapes."
    "Celeste looks up. Her steel-gray eyes measure you like sunlight finds the edge of water."
    show celeste_park at left:
        zoom 0.7

    celeste_park "Mara. Thank you for meeting on short notice. We both know the council's deadline is not a suggestion."
    "You notice how she places the word 'we' on the table as if it were an asset rather than a responsibility. Elias slides a printout toward you; the headline reads: 'Cooperative Underwrites Promenade Expansion with Living Wetlands Cells—Public-Private Pilot Model.'"
    show elias_navarro at right:
        zoom 0.7

    elias_navarro "The cooperative's committed to underwriting the expansion. Co-managed wetland cells are part of the plan—Amina signed off on the monitoring protocol. This gives us leverage: funding plus those living elements you fought for."
    show dr_amina_bhatt at center:
        zoom 0.7

    dr_amina_bhatt "The monitoring is conservative. Redundant sensors, sediment traps at prescribed intervals. We can model edge stress under eighty-year storms. But there are assumptions—substrate compaction, hydrodynamic fluxes—that require mitigation."
    "Amina's words are precise as cut glass, but there's a tremor you can feel: the scientist's recognition that models are scaffolding, not guarantees. You focus on that tremor. It is where the town's lives will press."
    "You set your palms flat on the table and let the room's hum transpose into a rhythm for your heart. Very high, fast. Hope is a bright bird in a clenched hand."
    hide celeste_park
    show mara_lin at left:
        zoom 0.7

    mara_lin "I want that leverage, Celeste. I want the funds to stabilize the Commons, to expand community plots and build living cells that actually breathe. But our terms need teeth. Oversight, community veto points, protections for informal fishers—Tommy's livelihood. We can't sign a blank check that trades resilience for façade."
    "Celeste inclines her head, a practiced, diplomatic motion."
    hide elias_navarro
    show celeste_park at right:
        zoom 0.7

    celeste_park "We're open to oversight—conditional. The cooperative needs accountability. Investors expect deliverables and timelines. The promenade can't be an experiment that never shows results."
    "Elias interjects, palms up, the engineer's attempt to hold both worlds in place."
    hide dr_amina_bhatt
    show elias_navarro at center:
        zoom 0.7

    elias_navarro "We can phase it: early deliverables, living cells installed at the most critical nodes, independent monitoring by Amina's team. The cooperative covers capital; the town retains maintenance authority for specific parcels—"
    "Amina folds her hands, eyes catching on a line in the printed contract."
    hide mara_lin
    show dr_amina_bhatt at left:
        zoom 0.7

    dr_amina_bhatt "—And benchmarks. If sediment accretion doesn't match modelled curves within two years, we trigger redesign. But the contract's current language limits our scope to 'aesthetic wetland features' in several clauses. That's a legal framing problem."
    "The phrase 'aesthetic wetland features' feels like a splinter. It reduces living membranes to decorative gestures. Your chest tightens—hope and alarm braided tight as ropes."
    "Celeste smiles, the smile that translates risk into manageable numbers."

    celeste_park "Legal language can be amended. We have legal counsel ready. What matters is that we move quickly. There are federal timelines tied to the cooperative's grants. If we stall, we risk losing matching funds altogether."
    "Your internal clock speeds. Every second carries consequence: the cooperative's deadline, Amina's technical caveats, Tommy's voice when workboats can't go out because the promenade's engineering shifts currents, Rae's stencils waiting to be stamped on newly preserved"
    "walls. The urgency is a tide that lifts everyone and threatens to throw some against the rocks."
    "You look at Elias. He meets your gaze and then looks away, calculating the political vectors you both inhabit. He is earnest, his jaw set with the patina of someone who wants to fix things with blueprints and good intentions."
    hide celeste_park
    show mara_lin at right:
        zoom 0.7

    mara_lin "We need stronger language on 'living'—not just token pockets. We need community board seats with veto for project changes that affect fishing access. And we need a clause that addresses Amina's model fail-states."
    "Celeste taps a pen against her folder. The sound is a metronome, and your pulse answers in kind."
    hide elias_navarro
    show celeste_park at center:
        zoom 0.7

    celeste_park "Veto points make investors nervous. They want predictability. But a compromise is possible. Limited community seats—rotating—plus a technical oversight committee chaired by an independent scientist."

    dr_amina_bhatt "Independent, yes. But also empowered. If the science says edges will fail under certain load conditions, the committee must be able to halt construction and demand redesign."
    "Elias rests a hand near yours on the table, an island of warmth in conference-room cool. That brief contact steadies you—no guarantees, but presence."
    hide dr_amina_bhatt
    show elias_navarro at left:
        zoom 0.7

    elias_navarro "We can draft language that ties phased payments to technical benchmarks and community engagement milestones. That keeps funds flowing while giving us stopgaps."
    "The room's tempo accelerates. You can feel your breath like a drumbeat against rising wind. Positive valence settles under the pressure: there is a path through, and you can almost see the outline of shared work—boards"
    "being placed, wetland cells planted, children learning to tend marsh grass. But the path is narrow and lined with structural questions."
    "Celeste opens a slim black portfolio and lays a document before you: the scaled deal. Headlines on the first page—'Promenade Expansion Under Cooperative Funding; Co-Managed Wetland Cells Established.' The signatures lines are blank, waiting like small anchors."
    "You take a long look at the clauses and feel the future's teeth."

    menu:
        "Ask Amina to read technical clauses aloud":
            "Amina does. Her voice accelerates into a technical run-down; you catch terms that feel like doors—'compaction allowances,' 'edge shearing thresholds'—and your mind flips to mitigation ideas."
        "Request a private sidebar with Celeste":
            "Celeste accepts. In the hallway she speaks softer; there's a civility that smells like policy and perfume. You get a clearer timetable but also an unmistakable reminder: speed is non-negotiable."
        "Call Tommy and put him on speaker":
            "Tommy answers, voice weathered and bright. He asks about boat access and keeps you grounded in livelihoods—his questions are blunt, precise, and quickly reveal social stakes you might otherwise ignore."

    # --- merge ---
    "Narrative continues below"
    hide mara_lin
    hide celeste_park
    hide elias_navarro

    scene bg ch5_4001e7_2 at full_bg
    # play music "music_placeholder"  # [Music: Percussion intensifies; a high violin enters, prickling]
    "The sidebar choices accordion into new information. If Amina reads, you discover that the promenade's current edge design includes hard retaining elements in certain sections—redeeming money saved but risking wave reflection and scour. If you go"
    "with Celeste, you learn the cooperative's timeline compresses next fiscal quarter and that their contingency plan for overruns is thin. If Tommy joins, the human ledger unfolds: who fishes where at dawn, whose mooring slips could"
    "be altered by a redirected current, and the names of families who will be affected."
    "No matter the micro-choice, the net tightens: the scaled deal is real, immediate, and threaded with vulnerabilities that matter. Your arousal climbs—fast, hot. The room feels smaller, the rain louder. Yet beneath the roar is warmth;"
    "funding means gardens, monitoring means data, the cooperative's resources mean capacity you did not have before."
    "Celeste leans forward. Her voice is both the lever and the mettle."
    show celeste_park at left:
        zoom 0.7

    celeste_park "We can set an amendment process. We will commit to funding the living cells as designed by Amina and overseen by an independent body. But the cooperative needs timelines and deliverables. Are you prepared to bring this to council tomorrow? We can sign pre-commitment papers tonight."
    "You taste the decision like tide salt: you can lock in the money now and start planting, or you can demand more safeguards and risk the whole thing evaporating into bureaucratic limbo. The stakes spark electric in your veins."
    "Elias moves beside you, quiet, patient, and the pressure in the room sharpens his features into something like decision."
    show elias_navarro at right:
        zoom 0.7

    elias_navarro "Mara, I trust Amina's call. I believe a scaled deal with these amendments could be the bridge we've needed. But if you want stronger legal teeth, we have to be candid now."
    "Amina places her hand on a thick printout. The paper trembles; so do you."
    show dr_amina_bhatt at center:
        zoom 0.7

    dr_amina_bhatt "From an engineering standpoint, the most responsible path is to explicitly define the fail-state responses in contract language. That may slow implementation, but it's the only way to prevent harm at the edges."
    "Your mind spins through futures—children planting cordgrass, Tommy's nets not tangled by new currents, reporters framing a victory narrative, and a section of promenade buckling under an underestimated shear stress. The emotion that wells is overwhelmingly"
    "positive: here is a real chance to win, to build something hybrid and meaningful. But the intensity is blistering; the choices are surgical."
    "You draw breath. A pulse kicks in your throat, quick as surf. Your voice is steadier than you feel."
    hide celeste_park
    show mara_lin at left:
        zoom 0.7

    mara_lin "We can do this. But not on vague promises. We need explicit benchmarks, an empowered oversight committee, community veto on access issues, and a contingency to halt payments if models show imminent edge failure. If the cooperative will sign that, we bring it to council tomorrow. If not—"
    "Celeste lifts a single eyebrow, an invitation and a warning rolled together."
    hide elias_navarro
    show celeste_park at right:
        zoom 0.7

    celeste_park "If not, we renegotiate terms, but time is not on anyone's side. We have windows to keep grant eligibility. Delay could mean losing everything."
    "Elias meets your gaze, then widens it into a look that says trust me, trust us; it says partnership as policy. The rooftop's hand-clasp still gleams in memory, but so does Amina's sober modeling. Your loyalties braid—community and engineer and scientist and the pragmatist across the table."
    # [Scene: Town Hall | Midday]
    hide dr_amina_bhatt
    hide mara_lin
    hide celeste_park

    scene bg ch5_4001e7_3 at full_bg
    # play music "music_placeholder"  # [Music: Brass joins the strings—broad, urgent; heartbeat percussion persists]
    # play sound "sfx_placeholder"  # [Sound: Murmurs building into a crowd-level hum; the automatic doors hiss]
    "You leave the conference room with a document labeled 'Draft Scaled Agreement' clutched to your chest. The Hall is louder than expected; staffers pass with clipboards, and a lone boy tugs a poster under his arm—Rae's"
    "stencil art—eyes bright. Outside, the promenade glitters like a promise. The air smells of wet pavement and the sweet, green tang of algae."
    "Elias walks with you, quickening steps to match your pace. He pushes open the council chamber door and a gust of warm air and public electricity rolls over you both."
    show elias_navarro at left:
        zoom 0.7

    elias_navarro "I can handle the legal edits with Celeste's counsel tonight. We keep moving and I will push for every amendment Amina suggested. We don't have to accept 'aesthetic' language."
    "You feel the tide of possibility rise. It is very high now—hope pressed against the membrane of risk. People will cheer this in the chamber tomorrow if you bring them a story of compromise and care."
    "But you also know the edges—the places where engineering and ecology graze each other—are raw and unpredictable."

    menu:
        "Ask Rae to prepare a visual placard that explains living cells":
            "Rae grins and runs with it, promising imagery that transforms jargon into hands-on scenes; the town can understand what the wetlands will do."
        "Place a call to Tommy and schedule a sunrise meeting at the Promenade":
            "Tommy's answer is immediate, determined; he promises to bring the fishers' reps, anchoring the technical debate in livelihood testimony."

    # --- merge ---
    "Narrative continues below"
    # [Scene: Promenade Edge | Afternoon]
    hide elias_navarro

    scene bg ch5_4001e7_4 at full_bg
    # play music "music_placeholder"  # [Music: Percussive strings fast and relentless; a high, hopeful motif threads through]
    # play sound "sfx_placeholder"  # [Sound: The sea kisses the shore; a winch creaks nearby]
    "You stand at the very edge where Celeste's architects imagine glass-front promenades. The tide nibbles at the old concrete. Amina kneels, boots slick with mud, and points to a cross-section sketch on her tablet: the proposed living cell footprint, root mats, sacrificial buffer zones."
    show dr_amina_bhatt at left:
        zoom 0.7

    dr_amina_bhatt "This edge shows potential for localized scour. Our solution is deeper substrate reinforcement paired with vegetative reinforcement—planting ahead of fill to dissipate wave energy. But if construction starts without proper phased compaction, we risk undercutting that exact buffer."
    "Your throat tightens. You run a hand over your copper bracelet—the coordinates of the town's original marsh—and feel it warm like a living thing. Positivity hums under the pressure: the plan is here, the science is"
    "clear, and funding can buy the time and materials to do it right. But the pace insists: build now, build soon."
    "Elias kneels, matching Amina's gaze. He draws a line in the sand with a forefinger."
    show elias_navarro at right:
        zoom 0.7

    elias_navarro "We can write phased compaction and substrate checks into payments. We can require third-party inspection before each new tranche of construction. That gives us leverage without halting everything."
    "You nod, adrenaline high—your brain firing in rapid staccato: benchmarks, inspections, community board, contingency funding release. The air tastes of salt and possibility. You imagine the Commons anchored under the promenade like a breathing seam. The future tugs: bright and urgent."
    "Celeste's voice comes through on your phone—brief, clear."

    "Celeste Park (on phone)" "We can accept the amended timeline if the cooperative's counsel and your legal team sign off tonight. The pilot has to be delivered on schedule. Are you ready to put your name to that, Mara?"
    "Your hands are small and steady around the phone. The question lands like the final drumbeat before a chorus."
    "You think of Tommy at dawn, the children who will plant cordgrass, Rae's art turning technical language into a mural that will teach. You think of Amina's models and of Elias's patient insistence on bridges between ideas. There is warmth—hope—threaded through the pressure."
    "Your arousal is at its apex: decisions compress, consequences hang like storm clouds bright with the possibility of rain that will either feed the wetland or flood the town. You are ready to act, to claim the scaffolding you've built into something durable. The room—the town—feels like a held breath."
    "You step back from the edge, the phone warm against your ear, and let the list in your head unspool: legal teeth, oversight, benchmarks, community seats, funded mitigation. You are keenly, fiercely alive."
    # [Scene: Old Mill Rooftop | Early Evening — Golden Hour]
    hide dr_amina_bhatt
    hide elias_navarro

    scene bg ch5_4001e7_5 at full_bg
    # play music "music_placeholder"  # [Music: Full orchestra—strings and brass—rushing into a climactic cadence; heartbeat percussion continues]
    # play sound "sfx_placeholder"  # [Sound: Wind picking up; distant thunder rolls like applause]
    "You climb the rope ladder with Amina and Elias at your heels. The rooftop is where you have thought best—above the immediate, close to the sea's breathing. The light is electric, gilded at the edges. The"
    "town below threads itself into a glow: the promenade's dotted survey flags, the Commons' boardwalk sliced by golden channels. It feels possible. It feels fragile. It feels necessary."
    "Elias collapses onto a battered bench and exhales like someone shedding armor."
    show elias_navarro at left:
        zoom 0.7

    elias_navarro "If you accept the scaled deal with our amendments, we secure the cooperative's funding and start work next month. We can pilot the living cells in priority nodes while the legal team tightens language on fail-states."
    show dr_amina_bhatt at right:
        zoom 0.7

    dr_amina_bhatt "With the inspection triggers stitched into payment tranches, we also maintain leverage to halt and redesign before catastrophic edge failure. It's not perfect, but it is far better than inaction."
    "Celeste's amendment—your amendments—could give the town a win. The emotion that wells is positive, almost ecstatic; the pressure is very high, rushed into each syllable you breathe. You feel love here—the love of place, of hands"
    "in soil, of someone who will stand with you while you fight for quiet things that matter."
    show mara_lin at center:
        zoom 0.7

    mara_lin "We have to lock in the oversight, the community seats with veto, and Amina's fail-state clauses. If the cooperative won't agree, we push for an explicit contingency that protects the town's access and fisheries. No 'aesthetic' language. Full stop."
    "Elias meets your eyes, not interrupting. For once the engineer in him seems to be listening first, measuring second."

    elias_navarro "I can fight for that. I will."
    "Amina wedges a finger into the soft soil of a planter box and pulls at a root—an act that is both symbolic and pragmatic."

    dr_amina_bhatt "If we draft this tonight and Celeste's team signs, we bring a clear, amended proposal to council tomorrow. It gives the town a narrative of compromise and care. It also gives us technical breathing room."
    "You close your eyes and imagine the town—children planting, fishers steering, promenaders learning the names of marsh grasses. The future is bright, jagged, and urgent."
    "Your hands find Elias's again, briefly, a contact that is both comfort and covenant. There is nothing theatrical in it—just presence."
    "You inhale. The arousal sears; your mind is a kiln of forward motion. You see the contract, the signatures, the timeline, the wetland cells taking root, and the thin line of surf that will test every decision."
    "You open your eyes and the decision sits, undeniable."
    # play music "music_placeholder"  # [Music: Orchestra peaks into a single sustained chord; then silence fills the space like held breath]
    hide elias_navarro
    hide dr_amina_bhatt
    hide mara_lin

    scene bg ch5_4001e7_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A single gull cries; thunder promises more]

    scene bg ch5_4001e7_7 at full_bg
    "THE END"
    # [GAME END]
    return
