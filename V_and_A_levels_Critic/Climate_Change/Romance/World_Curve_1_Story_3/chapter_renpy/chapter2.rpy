label chapter2:

    # [Scene: Council House Atrium | Morning]

    scene bg ch2_c4ca42_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of fluorescent fixtures, the soft click of a projector advancing slides. Murmured conversation like surf against the walls.]
    # play music "music_placeholder"  # [Music: Steady, unobtrusive piano—an even pulse that keeps time with your breathing.]
    "You step inside with salt still clinging to the cuff of your jacket. The air is cooler here, edged with recycled coffee and the faint, sterile tang of municipal cleaning solvents. Your footsteps on the stone"
    "feel private and loud; they carry soil from the rooftop like a whisper that the room will try to tidy away."
    "Irene stands at the dais as if she were born into the light of these rooms. Her renderings—slick, annotated, and infinitely scalable—rotate on the screen: straight lines of seawalls, commercial terraces, neat parking and job-creation numbers"
    "pulsing in neon amber. Her lapel pin flickers data in a steady beat; metrics bloom and fade like bioluminescence."
    show irene_vale at left:
        zoom 0.7

    irene_vale "Maris Bay cannot afford delay. These proposals bring investment, immediate labor, and quantifiable protection. The harbor stabilization will create two hundred jobs within the first quarter, and—' (she clicks; the graph spikes) '—we project—"
    "Mayor Lionel Park leans forward in his chair, palms pressed as if to steady the motion in his chest. He listens like a man practicing calm. Captain Reyes, pipe carved and silent, watches the room with"
    "a face that measures time in tides, not budgets. Dr. Sora Kim sits with a tablet balanced on her knee; she looks at you first—small, steady contact—and then at the projected marsh curves."
    show dr_sora_kim at right:
        zoom 0.7

    dr_sora_kim "The models are not in contradiction, Irene. They simply show different timescales. Here—' (she taps the tablet; a damp, ragged curve appears) '—peat accretion, organic resilience, microclimate feedbacks. If we compress the marsh with heavy fill, the initial gain in land is not sustained once the sediment compacts and saltwater intrudes."
    "You feel the translation beginning inside your chest, the private work you've done a hundred times: numbers become stories, charts become neighborhoods, lines become the backs of boats and the rhythm of cast nets. You think"
    "of Sora's late-night field notes and of the rooftop nursery's small green miracles. You think of Captain Reyes' stories of the marsh when it used to cradle the town."
    "You move to the microphone because the room will expect you to speak, and because silence feels like an absence that could be filled by someone else's plan. But the microphone is cold; the metal reminds"
    "you of tools and work. You collect the words that will make a place out of diagrams."
    "Tala slides up beside you, seed beads flicking light like tiny offerings. She whispers—urgent, hopeful:"
    show tala_ruiz at center:
        zoom 0.7

    tala_ruiz "If we open with living shorelines and show payroll numbers from the restoration crews, people will see both jobs and a future that keeps their homes. I can organize volunteers in a weekend."
    "Her whisper is a small tide. You nod at her, feeling the practical map of labor she hands you. Evan is at the back, camera catching the light off his brass lens. The solar wristband at"
    "his wrist blinks a quiet, personal rhythm — a beat you know by habit but never assume to interpret. He catches your eye, then drops it; his face is unreadable but steady."
    hide irene_vale
    show evan_kaito at left:
        zoom 0.7

    evan_kaito "They're showing the renderings again. You're doing the living-shoreline pitch, right?"
    hide dr_sora_kim
    show maya_alvarez at right:
        zoom 0.7

    maya_alvarez "I am. Sora's data is clear—people need to hear timeframes, not just guarantees."

    evan_kaito "Good. You've got the translations. I'll log footage, get microclimate reads during the talk.' (He taps the wristband.) 'It helps people trust that it's grounded."
    "You both hold the pause long enough for the sincerity to settle. It's practical, small, neutral—work bridging to care without theatrics. You notice how that steadiness steadies your own pulse."

    menu:
        "Answer Tala immediately":
            "You meet Tala's eyes and say, 'Do it. Start with the pier crews and show payroll projections.' Her smile is a quick, fierce thing—relief folded into resolve."
        "Hold the mic and listen":
            "You tighten your grip on the cold metal and let Irene speak through her slides. Holding back feels strategic; your silence buys you a moment to watch reactions."

    # --- merge ---
    "..."
    "Irene's tone remains measured, practiced, and pleasant—the kind of pleasant that smooths friction into polish."
    hide tala_ruiz
    show irene_vale at center:
        zoom 0.7

    irene_vale "We do not have the luxury of extended pilots when residents are facing displacement now. We can retrofit the harbor with engineered terraces and offer guaranteed relocation stipends for those in the floodway—"
    "Captain Reyes' jaw tightens. When he speaks his voice is low and granular, as if the words have been stored in salt and memory."
    hide evan_kaito
    show captain_reyes at left:
        zoom 0.7

    captain_reyes "Guaranteed? Guarantees are easy on paper. On the water, you learn which promises float and which sink. My name's been in these tides longer than most here, and when you move the marsh you move the map of people's lives."
    "Mayor Lionel rubs his eyes. He wants to be decisive and kind at once; it's a weight that pulls at his shoulders. You sense him balancing the ledger between urgent payrolls and harder-to-count community memory."
    hide maya_alvarez
    show mayor_lionel_park at right:
        zoom 0.7

    mayor_lionel_park "We need jobs—short term, yes. But we also need measures that won't put us back where we started in five years. Convince me both, and you have my motion."
    "Dr. Sora Kim leans forward, offering evidence wrapped in gentleness."
    hide irene_vale
    show dr_sora_kim at center:
        zoom 0.7

    dr_sora_kim "The pilot restoration will employ—conservatively—forty laborers in the first month, scaling to eighty as we train more crews. The ecological work produces long-term protection through accretion and carbon sequestration, and it seeds local crafts—nurseries, marsh-sill construction—that keep money circulating here."
    "There's a careful exchange between Sora and Irene. Irene's numbers are big and blunt; Sora's are smaller, layered, and accumulative. Neither is wrong—their truths run on different clocks."
    hide captain_reyes
    show irene_vale at left:
        zoom 0.7

    irene_vale "People want certainty. If the town approves the harbor plan, we can start contracts next week. The economic forecasts are robust. We reduce risk quickly."

    dr_sora_kim "But when risk is reduced by replacement—removing marsh and sealing the coast—you trade your living buffer for engineered walls. Those walls protect a different future—one with a different map and different people."
    "The room hums. You can feel the shift in temperature when technical language becomes personal consequence. Chairs creak. The projector advances. A photograph of a marsh teeming with small life appears beside an antiseptic rendering of a walled harbor. The contrast is sharper than the fluorescent lights."
    "You find your voice and begin, translating in the way you always do—compassionate, clear, a bridge between lab and living room."
    hide mayor_lionel_park
    show maya_alvarez at right:
        zoom 0.7

    maya_alvarez "We are not arguing jobs versus care as if they were mutually exclusive. We need livelihoods now and stability later. Living shorelines create work—nurseries, planting crews, maintenance—but they also give us a shore that regenerates with us. A pilot program can be scaled and audited. It will be slower than a single, large build, but it will keep the marsh' services intact."
    "Irene tilts her head, polite, calculating."

    irene_vale "Maya, your plan is admirable. But citizens don't pay their rent with future accretion curves. They pay it with checks. How do you propose we keep families housed if we postpone large-scale construction?"
    "You take a breath. This is the question you've rehearsed: how to map long-term stewardship into immediate cashflow. You think of Tala organizing payroll, of Sora's microgrants, of Evan's kits that can shelter and sell as modular assets."

    maya_alvarez "Pilot restoration with concurrent short-term employment programs—paid stipends to families participating in the restoration, rapid fabrication of Evan's modular units to provide interim housing for the most at-risk, and a staged approval process for any large infrastructure so this town doesn't lose what it can't replace."
    "Mayor Lionel nods slowly, as if tasting the feasibility of each clause. Captain Reyes watches without moving. The room is now entirely engaged; every face is cataloguing which future feels like home."
    hide dr_sora_kim
    show tala_ruiz at center:
        zoom 0.7

    tala_ruiz "If we show a week of payroll, even people who want quick fixes will see the benefit. We can start small and make a record."
    "Evan Kaito slips forward slightly, a data card in hand. He speaks in a tone made for work, gentle engineering constancy."
    hide irene_vale
    show evan_kaito at left:
        zoom 0.7

    evan_kaito "If you let me, I'll set up demonstrations at the pier after this. We'll show the desalinator performance under load and the modular habitat's buoyancy. People respond to proof."
    "Irene allows a small smile—tactically neutral."
    hide maya_alvarez
    show irene_vale at right:
        zoom 0.7

    irene_vale "Demonstrations are fine, as long as they don't delay the contracts. We cannot have pilot projects that stall funding streams."
    "Your heart rhythm steadies to the midline of the room's pulse. Everything here is negotiation: language, time, trust. The arousal in the room is steady—focused, not frantic. Nothing is collapsing. Nothing is triumphal yet. It is the ordinary high stakes of community work: urgency balanced with process."

    menu:
        "Motion to request a staged approval":
            "You raise the issue of staged approvals—regulatory scaffolding that allows work to start while preserving options. Chairs shuffle; a few heads nod. The mayor scribbles notes, buying the time you need."
        "Call for an immediate demonstration at the pier":
            "You propose an immediate demo. The room pivots toward practical action; murmurs turn into quick logistics—permissions, volunteers, materials. Evan catches the cue and begins planning out loud."

    # --- merge ---
    "..."
    "Irene's eyes find you across the dais again. For a beat they are unreadable—steely, assessing, almost kind in their calculation. She reaches for rhetoric like a well-worn tool."

    irene_vale "Maya, your proposals make for good optics and community theater, but scale matters. We must be pragmatic, and pragmatism sometimes requires hard choices."
    "The phrase hangs in the filtered light. Hard choices—how you owe the town material stability and how you owe it memory and regenerative safety—are the bones of the day."
    "Dr. Sora Kim folds her hands, voice soft but insistent."
    hide tala_ruiz
    show dr_sora_kim at center:
        zoom 0.7

    dr_sora_kim "Pragmatism without ecological timelines becomes a repeat of past mistakes. We need both: the immediate relief to keep people safe and the institutional patience to let nature do the long work."
    "Mayor Lionel rubs his chin. The pressure is a private ledger in his posture. He says what you suspected he'd say, the compromise in search of consensus."
    hide evan_kaito
    show mayor_lionel_park at left:
        zoom 0.7

    mayor_lionel_park "What if we tie funding disbursement to environmental milestones? A hybrid contract—some upfront investment for jobs and relocation safety, and staged payments contingent on marsh health metrics."
    "Irene gives a measured exhale. The room shifts; you can see the wheels turning behind her composure."

    irene_vale "Staged payments are negotiable. But I will press for significant upfront capital. We must protect livelihoods."
    "Captain Reyes clears his throat. When he speaks now, it is less combative, more anchored."
    hide irene_vale
    show captain_reyes at right:
        zoom 0.7

    captain_reyes "Protect livelihoods and teach the town to read the marsh again. Teach the kids what tides do. Otherwise the whole thing will be new to them and they'll lose the stories that keep places human."
    "A low, collective acknowledgment moves through the room. You feel the arousal curve—steady attention, building toward a single pivot where the town's line might bend."
    "You glance at Evan. He catches your look and, this time, his expression is a small compass: steady, indicating a way forward without demanding your course. Tala's fingers drum a rapid rhythm on her clipboard, ready"
    "to mobilize volunteers. Sora's tablet glows with the slow, patient math of accretion. Irene's metrics pulse like a heart you must learn to read. The mayor seeks a path that keeps both his job and his"
    "conscience."
    "All this negotiation funnels into the one thing you have to decide: how loudly to fight in public for pilot-based, nature-first approaches; where to place limited pilot projects so they count as proof; and how much"
    "to risk by telling the most vulnerable the truth about trade-offs while still keeping them housed and fed."
    "You can feel the room holding its breath in the pragmatic way of municipal gatherings—an expectant pause that is not panic but is poised to act. Your throat tightens with the weight of responsibility that has"
    "been on you since the rooftop, the copper barometer against your chest like a small, private metronome."
    "You lift a hand toward the microphone. You could take the mayor's suggestion and try to thread the compromise through staged payments. You could press for immediate demonstrations at the pier as a show of practical"
    "proof. You could call the room to commit to a pilot-and-pay structure that would bind developers to ecological milestones."
    "The decision sits at the edge of your tongue, ready to form. Outside the glass, the sky remains pewter; inside, voices wait."
    hide dr_sora_kim
    hide mayor_lionel_park
    hide captain_reyes

    scene bg ch2_c4ca42_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The projector clicks once more; murmurs ripple.]
    "You inhale, and the room tightens around that breath—the ordinary, exact moment where policy becomes people."

    scene bg ch2_c4ca42_3 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
