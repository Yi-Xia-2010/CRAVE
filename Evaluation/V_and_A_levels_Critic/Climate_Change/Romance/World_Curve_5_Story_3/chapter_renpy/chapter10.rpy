label chapter10:

    # [Scene: Verdant Terrace | Morning — Seven Days Later]

    scene bg ch10_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Brisk strings under a hopeful synth pulse]
    # play sound "sfx_placeholder"  # [Sound: Bees hum in a distant planter; the city’s distant tide clanks against concrete]
    "Aiko Mori arrives with the notebook under her arm and the city already in motion. Morning light is thin through sea haze, but the Terrace is warm with bodies: volunteers pruning, a teenager knotting a drip"
    "line, Mina ladling tea into chipped mugs. The air smells of damp earth and ginger from Mina's kettle, salt and cut grass threaded underneath."
    "Aiko Mori sets the notebook on a low crate, fingers tracing tide maps in the margin. The pages are crowded with notes—legal sketching that looks more like a gardener's plan: edges, supports, layers of protection. Her pen is stained with compost."
    show mina_kuroda at left:
        zoom 0.7

    mina_kuroda "You're late by five minutes, scientist. We started organizing the seed exchange and then—' (she grins) '—you finally showed."
    show aiko_mori at right:
        zoom 0.7

    aiko_mori "I had to make sure the Atrium meeting didn't swallow us whole.' (She taps the notebook.) 'Rowan wants a clause about proprietary sensors. I want open access. We can have both, if the language is airtight."
    "Mina's smile softens into something steadier. She wipes her hands on her apron, eyes clear and fierce."

    mina_kuroda "Jobs, too. If they bring machines, we make sure our people build, maintain, and run them. No handoffs."
    "Aiko Mori feels the urgency lift her shoulders and set them taut—this is the moment when technical detail becomes livelihood. Her voice finds a cadence honed by nights of drafting and the blunt diplomacy of community kitchens."

    aiko_mori "Community job guarantees. Oversight board that includes municipal reps and three named neighborhood seats. Open-data promises, with a watchdog clause enforced by public audit. And cultural protections—the shore rituals, Sora's stories—can't be displaced for an experiment."

    "Mina (nods)" "Good. Put that in bold."

    menu:
        "Underline the watchdog clause":
            "You press harder, the ink biting the paper. It's small theater, but it steadies you."
        "Sketch a quick flowchart instead":
            "Your fingers move into diagrams—boxes and arrows that make governance feel like something you can wire together."

    # --- merge ---
    "The meeting continues with the clause recorded and governance diagrams in the margins."
    # [Scene: HelioCorp Glass Atrium | Midday]
    hide mina_kuroda
    hide aiko_mori

    scene bg ch10_453e40_2 at full_bg
    # play music "music_placeholder"  # [Music: Low percussion, heartbeat-like; a rising electronic motif]
    # play sound "sfx_placeholder"  # [Sound: Soft footfalls, the faint hum of a building-scale HVAC system]
    "Dr. Rowan Hale stands with the strangest combination of ease and coiled attention. The suit is immaculate; the compass in his pocket is an old man’s talisman you imagine polished in private rituals. He watches Aiko Mori like a scientist watching a delicate experiment—patient, probing."
    show dr_rowan_hale at left:
        zoom 0.7

    dr_rowan_hale "Aiko—"
    "He inclines his head. '—your proposal was sharper than I expected. An oversight board. Open data. Community seats. HelioCorp will agree to a pilot under those constraints, provided the municipal contract clarifies liability thresholds and system rollback procedures.'"
    show aiko_mori at right:
        zoom 0.7

    aiko_mori "Rollback is non-negotiable. If the pilot does harm or if transparency is violated, mechanisms to halt and remove tech must be explicit and executable."
    "Dr. Rowan Hale considers Aiko Mori, then nods once—reluctant, precise."

    dr_rowan_hale "Agreed. We can codify halt triggers. But the sensors and modular barriers are our IP until the pilot proves stability. We need a clause that licenses operations to the city for the pilot's duration."
    "Elias Chen is standing just behind Aiko Mori, sleeves rolled, a half-scribbled list of community demands in his hand. He watches Dr. Rowan Hale with a mixture of skepticism and something like wounded hope."

    "Elias Chen (brisk)" "Licensing isn't ownership. Make that clear. You mean to test, not to privatize."

    "Dr. Rowan Hale (coolly)" "No privatization. Pilot testing requires operational integrity. We cannot risk jury-rigging critical infrastructure with uncoordinated inputs."
    "The air tightens. Aiko Mori can feel it—two philosophies trying to occupy the same narrow room."

    aiko_mori "Operational integrity and community sovereignty are not mutually exclusive. We build redundancy into the system design. Citizen sensors must be feed-capable and readable. HelioCorp's models and raw data must be mirrored to public servers. If threat thresholds are met, the oversight board convenes within 24 hours. If rollback is requested by the oversight majority, HelioCorp will comply."
    "Dr. Rowan Hale's mouth tightens. He reaches into his jacket, and for a breath Aiko Mori fears he will produce vetoes, corporate clauses stacked like armor. Instead, he produces a tablet and slides it across the"
    "table—an initial draft. Her stomach jumps: legal language has teeth, and she can already see where it wants to bite."
    "Rafi stands at the edge of the atrium, fingers wrapped around a small recorder. He leans in like a reporter smelling a lead; he's already thinking about headlines and watchdog tactics."
    show rafi_alvarez at center:
        zoom 0.7

    rafi_alvarez "I will run continuous reports. Any deviation, I publish. Transparency is enforcement."

    "Dr. Rowan Hale (a flicker of wry amusement)" "And if the reports are inaccurate?"

    rafi_alvarez "Then the audience corrects them. The public is the ultimate audit."
    "The conversation arcs and rebounds—technicalities, ethics, livelihoods. Aiko Mori asks for specifics and stitches them into her notebook in the margins: time-bound clauses, escalation procedures, named municipal signatories, community seats with rotating terms. Her handwriting grows cramped and fast; urgency tunes the pen to a near-run."
    hide dr_rowan_hale
    show elias_chen at left:
        zoom 0.7

    elias_chen "Are we sure this will work? I don't like signing a paper that could be used to paper over displacement."

    "Aiko Mori (soft, direct)" "Then we make displacement illegal in the pilot zone. Any relocation requires a supermajority vote and a reparative package that includes housing and job placement. Do we have that power? We carve it into the municipal agreement."
    "Elias Chen exhales, the tension leaving him a notch. He reaches for Aiko Mori's hand—a quiet touch like the one on the Beacon steps. It steadies both of them."

    "Dr. Rowan Hale (finally)" "I will include rollback triggers, mirrored data, municipal stewardship for the pilot window, and an audit clause enforced by a third-party nonprofit you name."
    "Aiko Mori allows herself a small, incredulous grin. Dr. Rowan Hale has given her far more than she expected."

    menu:
        "Insist on naming the watchdog now":
            "You ask for the nonprofit's name. Rowan hesitates, then nods—it's progress."
        "Accept a blank and demand naming within 48 hours":
            "You force a temporal boundary. It feels like chess—small and decisive."

    # --- merge ---
    "The draft is adjusted and a timeline for naming the nonprofit is recorded in the agreement."
    # [Scene: Old Beacon | Dusk]
    hide aiko_mori
    hide rafi_alvarez
    hide elias_chen

    scene bg ch10_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: Warm piano, picking up tempo; voices overlay like chorus]
    # play sound "sfx_placeholder"  # [Sound: Rain beginning at the edges, crowd murmur; the creak of wooden chairs]
    "The Beacon fills with neighbors. Sora's shawl catches the lamplight; her walking stick rests against the wall like an old sentinel. Attendance is high—more faces than Aiko Mori expected, and the air is electric with cautious optimism."

    "Sora Watanabe (steady)" "Language for rituals. We will not allow testing to interrupt our rites. The shore is memory as much as topology."
    show aiko_mori at left:
        zoom 0.7

    aiko_mori "We write that into the pilot. Accessibility for cultural practices is prioritized, and any physical installation must have a cultural-impact assessment before deployment. No exceptions."

    "Mina (from across the table)" "And jobs. If HelioCorp brings tech, our people must maintain and staff it. Training programs, apprenticeship pipelines—we're not handing work away."

    aiko_mori "Agreed. Job guarantees with stipulations: living wage, local hiring quotas, and community-led training curriculums funded by the pilot budget."
    "Voices rise into practical contention, not animosity—arguments for clause wording, for who sits on the oversight board, for how emergency votes happen. Aiko Mori moderates, listens for undercurrents. Elias Chen watches the room, translating the technicalities into a moral logic for the crowd. Rafi scribbles notes, his recorder running."
    "Aiko Mori feels the momentum like a tide—relentless and shaping everything. The community's demands begin to coalesce into a treaty: a pilot that is daring but anchored in law, practical science, and memory."

    "Aiko Mori (low, to Elias Chen)" "You could walk away. Or you could shape the seams."

    "Elias Chen (brittle smile)" "And miss the chance to keep people from losing homes? Not this time. But I'm watching you—keeps you honest."
    "Aiko Mori laughs, sharp and relieved. The laughter feels like a seal on what they've built so far."

    menu:
        "Read a clause aloud":
            "You voice the rollback trigger. The room reacts—relief, a small cheer. It lands like a promise."
        "Let Sora speak instead":
            "Sora rises slowly, and when she speaks the room stills. Her words make the clause mean more than law—they make it sacred."

    # --- merge ---
    "The clause is accepted by the community and recorded in the pilot documents."
    # [Scene: Subbasement Data Lab | Late Night — Test Deployment]
    hide aiko_mori

    scene bg ch10_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Accelerating electronic arpeggios; percussion hits sync with heartbeats]
    # play sound "sfx_placeholder"  # [Sound: Fans whine, an alarm-safe ping as systems come online; fingers tapping keys]
    "Aiko Mori stands between racks of cables and a bank of monitors that spit numbers like constellations. The pilot's first field test is minutes away. Outside, modular barrier segments are positioned along the shore. Citizen-built sensors—patched"
    "from salvaged parts and HelioCorp modules—are networked to the lab. Rafi's recorder sits open on the table like a relic."
    "Aiko Mori's hands are steady but quick. She signs the last amendment—typed, digital, timestamped—and her signature is a small, sharp click."

    "Dr. Rowan Hale (next to her, quietly)" "We will deploy at your mark. If anomalies manifest, the watchdog protocol triggers and we halt."
    show aiko_mori at left:
        zoom 0.7

    aiko_mori "Rollback triggers are set on divergence over the modeled threshold. Citizen sensors will cross-validate. If disagreement occurs, the oversight board will arbitrate within twelve hours."

    "Elias Chen (braced by a monitor)" "This feels like stepping onto a bridge that hasn't been tested in wind."

    aiko_mori "We've tested the bridge. Tonight we step across together."
    "The countdown begins. Her chest hammers not from fear but from the electric push of a long-fought possibility—a community and a corporation moving in synchrony, awkward and beautiful."
    "Aiko Mori presses the command. The lab breathes: a chorus of indicator lights, a soft mechanical unclasping, the low thunk as the first modular barrier segment pivots into place outside. Camera feeds show the barrier's spine rising against the advancing tide like slow, stubborn teeth."
    "Then the sensors light up—citizen sensors and HelioCorp sensors reporting in parallel. Data streams cascade across her monitor: pressure differentials within expected tolerances, wave attenuation within modeled range, energy draw within the safe envelope."

    "Rafi (half-laugh, half-cry)" "It's reading right. The models—"
    "A monitor flags a small deviation—a stray spike on a less-critical sensor. Aiko Mori's hand hovers. She feels time narrow to the point where thinking is almost physical, where every breath counts."

    "Dr. Rowan Hale (calm, but there is a brightness to his eyes)" "Minor variance. Cross-validate with citizen arrays."
    "Aiko Mori calls for cross-validation. The feeds reconcile. Variance explained: biofouling on a float sensor, not structural failure. Mina's trainees—faces lit by monitor glow—send a field team to clear and report. The team moves like a practiced unit, each gesture purposeful."

    "Elias Chen (exhales)" "We did it. We—"
    "The lab erupts in energy. It is not a quiet success; it is a public, communal shout sealed with relief and a dizzy kind of joy. Dr. Rowan Hale's composure softens—just a fraction—into something almost like pride."

    "Aiko Mori (voice shaking with good strain)" "We did it."
    "The monitors continue to feed, the barrier holds, and the citizen sensors sing in sync with corporate models. The oversight board's provisional vote—conducted through the governance app Aiko Mori helped design—casts the pilot as green for continued testing."
    "She watches the live feed of the shore: the first wave hitting the modular barrier and breaking as planned, spray arching in glittering arcs. Someone outside cheers; she can feel it through the building. Mina squeezes Aiko Mori's shoulder so hard she feels the warmth."

    "Sora Watanabe (softly, to Aiko Mori)" "The sea listens when people speak together."

    "Rafi (already plotting stories)" "This will change the frame. Not a silver bullet, but the narrative—community and tech, side by side."
    "Aiko Mori closes her eyes for a second and lets the high, clean joy wash through her—pride, yes, but an almost dizzy gratitude. This is not the end. It is an opening. A proof of concept that feels, in the marrow, like a promise."

    "Her notebook lies open on the console—marginalia turned into clauses; tiny legal drawings like plant diagrams. She pens one last line for the night" "Pilot launch: continued oversight, open data, enforceable rollback."
    "Dr. Rowan Hale leans nearer, his breath a measured warmth against her ear."

    "Dr. Rowan Hale (admitting, quietly)" "You forced clarity where I favored speed. That was wise."

    "Aiko Mori (smiling)" "And you funded the things we couldn't cobble from scraps. We made something that neither of us would have made alone."
    "The room hums with aftershock—the high arousal she carried since dawn resolving into a triumphant high. It's a living, loud thing: hands slapping backs, phones already streaming, Mina's laughter, Sora's steady smile, Elias Chen's tear-bright eyes."
    "She thinks of ledger entries and of the Beacon's lamp and of the way hope accrues like sediment. Tonight, those layers shifted. The pilot stands, not as a handover of power, but as an architecture of shared authority."
    "Aiko Mori closes the notebook, feeling its weight. The city outside breathes in and out against the night."
    "Page-turn thought: This is only the first test. The tide learns; so do we. There are still hard choices ahead—scales to balance, governance to harden, forces within and beyond the city that will test what we've built. But for now, the shore holds."
    hide aiko_mori

    scene bg ch10_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: A single, ascending cello line resolves into a bright synth chord]
    # play sound "sfx_placeholder"  # [Sound: Distant applause blending into the tide]

    scene bg ch10_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter11
    return
