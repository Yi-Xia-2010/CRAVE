label chapter10:

    # [Scene: Resilience Lab | Morning]

    scene bg ch10_291da8_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, restrained strings; an undercurrent of a single cello line, minor and insistent]
    # play sound "sfx_placeholder"  # [Sound: Soft pump hum, the tick of a laptop cooling fan, distant gulls and the muted thump of harbor machinery]
    "You come in with the residue of the last night still clinging to your boots: solder on a thumb, the outline of a tidal curve in the back of your skull, the pendant warm where it"
    "hangs beneath your sweater. The lab smells of wet soil and ozone-cut plastic; Priya's tablet glow throws a blue wash over her face. Tomas is at the tethering ropes, fingers moving with the practiced slowness of"
    "someone who reads tides like scripture. Elena is taping a sensor mount to a plank, jaw set."
    "It feels, for a sliver, like the room is breathing with you — the pumps inhale, the kelp tanks exhale. That small communal rhythm quiets the thing under your ribs: the calendar. Thirty days. The council clock."
    "Priya looks up before you have your first step entirely across the threshold."
    show priya_anand at left:
        zoom 0.7

    priya_anand "We ran the attenuation curve again overnight. It's holding. The model's—' (her voice tightens, reluctant to make promises to air) '—it's trending."
    show mara_evans at right:
        zoom 0.7

    mara_evans "How robust? How sensitive are we to—the variance Arman Kade's lobby keeps hammering on?"
    "Priya scrolls, fingers precise."

    priya_anand "Controlled conditions are consistent. The sensors are reading attenuation in identical tests. But that's the thing—identical. Reproducible in the tank. Not yet in open water."
    "Noah Ríos pushes a mug toward you and leans on the bench, sleeves rolled, smartglasses reflecting the graphs."
    show noah_ros at center:
        zoom 0.7

    noah_ros "We can scale the sensor net across a short stretch of promenade. Calibrated. Public demo. Show them the attenuation in front of witnesses. Numbers and people. Hard to argue against that."
    "There's hope in his voice, the quick, efficient hope that has kept you both awake welding prototypes and bargaining for late invoices. But even as the suggestion lands, the room tilts. You can hear the mayor's calendar ticking."
    # play sound "sfx_placeholder"  # [Sound: Notification ping — phones on the table all light up at once; a chorus of small alarms]
    hide priya_anand
    hide mara_evans
    hide noah_ros

    scene bg ch10_291da8_2 at full_bg
    # play music "music_placeholder"  # [Music: The cello shortens, a tremor of dissonance]
    "You look up. Cass's message is a clean strike: the city is not waiting for elegance. The lab's air thickens like a storm front. Priya's jaw tightens; Noah Ríos's half-smile thins."
    "Tomas, without looking up from his knot, says something low and strange and anchoring."
    show tomas_belmar at left:
        zoom 0.7

    tomas_belmar "When the old pier gave to the sea once—long before the maps—those who read it last begged the tides for time. Time is what we do not have, child."
    "His voice is gentle but weathered; his fingers pull rope taut as if to pull time with it. There's a moral weight to the line. It is not technical. It is true."
    hide tomas_belmar

    scene bg ch10_291da8_3 at full_bg
    # play music "music_placeholder"  # [Music: Low wind through hull planks — metaphorical, building pressure]
    "A new email arrives, terse and corporate-bright: Arman Kade's lobby has a 'comparative assessment.' Short, clinical lines claim your sample size is too small to generalize; an attached PDF promises 'immediate deployables' and high confidence intervals. You can almost see the tailoring on the press release."
    "Elena snaps the tape roll back into her hand, eyes flashing."
    show elena_torres at left:
        zoom 0.7

    elena_torres "So what? They throw numbers and we've got—what—an aquarium and a prayer? Rent notices don't care about a tidal curve, Mara. People are getting letters."
    "Your throat tightens. You taste salt and iron. Every hour you spend refining models feels like a door clicking shut somewhere in East Strand."
    "Noah Ríos folds his arms, quick to anchor the room in actionable language."
    show noah_ros at right:
        zoom 0.7

    noah_ros "A public demo is risky, yes. Exposure. But it's immediate visibility. Witnesses, press, community members standing there when the sensors read. We show attenuation live — we force the council to reckon with data in context, not while Arman Kade's slides are being pushed."
    "Priya counters, slow and precise."
    show priya_anand at center:
        zoom 0.7

    priya_anand "Or we do a controlled private trial with a partner who can provide a larger sample size and a faster deployment window. It's faster, cleaner statistically, but it's behind closed doors. The optics: Arman Kade will scream secrecy. The community will feel excluded. And if anything goes sideways..."
    "Her hands gesture at the tank like a small animal; you can imagine the headline."
    "You close your eyes for a breath, feeling the lab's humidity press against the bridge of your nose. You think about the storefront you grew up in, the smell of roasted peppers mingling with diesel, the"
    "way Elena learned to braid banners for holiday markets. You think about Tomas's hands, and Priya's precision, and Noah Ríos's stubborn hope. You think about Cass's message: days, not weeks."
    "A funder text slides in — 'paperwork delayed; need signatures' — and you can hear the ledger closing in olive and navy: dollars and deadlines. The room is a web of dependencies and anxieties."
    "The energy in the lab is a taut wire. Someone needs to cut it, someone needs to steady it."

    menu:
        "Answer Cass immediately — promise to stage the demo":
            "You type back with too-quick confidence: 'We'll produce incontrovertible field results.' Your message is sent before you've sketched out a single safety perimeter, but the act calms you with the illusion of forward motion."
        "Ask for clarification and time — push Cass to specify 'days'":
            "You tap a measured reply: 'Define the minimum evidence you can accept. We'll prioritize accordingly.' The reply feels like a small reprieve, a paper wall against the immediate pressure."

    # --- merge ---
    "The lab continues its discussion with the sense of commitment shaped by your reply."
    "The keyboard click of your reply — whatever you chose — echoes differently from the rest. Promises are heavy."
    "Noah Ríos steps closer, lowering his voice."

    noah_ros "Public demo needs community consent. We can't set sensors and call it 'community' while people find out through press. I can get permits, I can handle calibration, but you lead the outreach. Elena, Tomas — can you do short notices? Floor meetings?"
    "Elena's face is a map of worry and work."

    elena_torres "I can knock doors. But people are scared. People already got rent notices. If we host something that looks like a showcase for a plan and it fails, it's worse than nothing. They'll say we were testing on them."
    "Tomas snorts softly, not unkind."
    hide elena_torres
    show tomas_belmar at left:
        zoom 0.7

    tomas_belmar "They've always tested on us. The sea has taken enough of that history."
    "You taste the bitterness in Tomas's words. The lab's promise to be different — to center place and people — is suddenly in danger of being performance rather than protection."
    "Priya sets the tablet down, eyes on everyone, the scientist pleading with the civic intent in the room."

    priya_anand "We could set the demo on a calibrated stretch of Promenade where the baseline bathymetry is known and the wave exposures are predictable. We limit variables: buoyed sensor lines at ten meters, controlled wave generators on-site if the council allows, safety perimeters. It's a proof of concept, not city-wide deployment. It could be done in days if Cass greenlights it."
    "You chew the inside of your cheek. Controlled generators — artificial waves to validate the system — feel like staging, but it's safer than throwing the hardware into raw stormwater. The smell of damp concrete from the Promenade comes to mind: algae, rust, the slick of it underfoot."
    "Noah Ríos's gaze finds yours — something like a question and an offering all at once."

    noah_ros "We can do it this week. Crowd line, data streamed live, Priya moderates the statistical narrative. You lead the consent process. We legitimize it by centering community witnesses in the footage."
    "Your chest tightens. You can hear the distant London-of-arms drums of the council's machine starting to thud. Time doesn't just pass; it pushes."

    menu:
        "Insist on a community referendum before any demo":
            "You raise your voice, the lab falling silent: 'I can't—won't—host a demo without explicit community consent. Not again.' Elena nods fiercely; Noah Ríos looks pained but respectful. The momentum tilts toward moral caution."
        "Agree to fast-track the calibrated Promenade demo with community witnesses":
            "You exhale. 'Okay. We do it—on our terms. We make the perimeter, we choose the witnesses, we publish the full methodology.' Noah Ríos's grin is brief and grateful; Priya already has a checklist forming in her head. The lab jolts into focused motion, gears grinding toward the new deadline."

    # --- merge ---
    "The team aligns and begins preparations based on the decision."
    "The choice you nudge toward is not a clean one. You weigh the ethics of consent against a city's appetite for quick answers. In the corner of your mind, you hear the rasp of Arman Kade's"
    "PR machine preparing an alt narrative — 'community excluded; hidden trials' — if you opt for any opacity."
    "There is another option nagging at the edge of your thought: to retreat, to demand more modeling time, to refine the variables until they are incontrovertible. It feels responsible in the abstract and cowardly in the concrete."
    "Priya's voice is the voice of someone who measures the cost of error in data."

    priya_anand "Delay to refine models will buy lower variance. We can simulate more stress tests, run ensemble predictions. But politics will not wait. Arman Kade will keep his campaign active and Cass will interpret 'lack of field evidence' as a practical gap. The risk of political default to his plan is real."
    "You feel the room lean into the word 'real.' It is heavier than a numerical risk. It is the weight of people you know whose livelihoods hang in the balance."
    hide noah_ros
    hide priya_anand
    hide tomas_belmar

    scene bg ch10_291da8_4 at full_bg
    # play music "music_placeholder"  # [Music: The cello deepens — falling minor tones that do not resolve]
    "Cass calls. You pick up, every syllable taut."
    show cassandra_cass_green at left:
        zoom 0.7

    cassandra_cass_green "Mara. I read Arman's white paper. I read Priya's last note. I need field results that are verifiable to bring to council. I cannot in good faith recommend a trial based on models alone. If you can't provide results within days, I will recommend Arman's plan for immediate protection. The decision window is almost closed."
    "Her voice is even, professional, but there's a firmness there that feels like a gavel. You hear paper rustle at her end; a municipal calendar page being turned."
    show mara_evans at right:
        zoom 0.7

    mara_evans "Cass. We have attenuation in controlled tests. We can stage a calibrated demonstration on the Promenade with community witnesses, or run an expedited private trial that increases sample size. Both have trade-offs. We won't hide results."
    "Cass: (a small silence) 'Transparency matters. The council needs to see people and data together. If your approach prioritizes process over demonstrable protection, I'm bound to choose whichever plan gives immediate, defensible safeguards.'"
    "You close your eyes. Her words are procedural, but their impact is intimate: choose quickly or choose to watch a different future be built on East Strand's bones."
    "Noah Ríos's hand touches your forearm — a small anchor. 'We do the Promenade,' he whispers. 'We manage consent. We control the optics. We show them what we can.'"
    "Elena's voice is keening with a tired, practical anger."
    show elena_torres at center:
        zoom 0.7

    elena_torres "Or we do the private trial and we get numbers fast, sign the dotted line, and maybe we can buy time and negotiate for transparency later. Maybe. But there's a cost in trust."
    "Tomas folds his hands, as if folding something fragile into a pocket."
    hide cassandra_cass_green
    show tomas_belmar at left:
        zoom 0.7

    tomas_belmar "Every choice is a new shoreline. Choose the one that keeps the children home."
    "You inhale. The salt in the air seems sharper. The lab becomes a pressure chamber of ethics and instruments."
    "Your mind moves through the calculus: credibility now for political survival; transparency now for moral survival; delay for evidentiary perfection and the risk of being outmaneuvered. The stakes are not only data points on a model — they are home addresses, market stalls, a sister's future."
    "You could feel the room leaning toward action. Or you could feel it leaning toward caution. Both directions hurt."
    hide mara_evans
    hide elena_torres
    hide tomas_belmar

    scene bg ch10_291da8_5 at full_bg
    # play music "music_placeholder"  # [Music: A single minor chord held and then bent downward — unresolved, heavy]
    "You stand at the edge of the decision as the city clock reclaims another thin slice of time. The lab organizes itself around the choice you must make."

    scene bg ch10_291da8_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant council gavel reported on a loop in a nearby TV; footsteps squelching in pooled water]
    "You watch a line of the Promenade where waves normally lace the concrete at high tide. You see how people walk it in sneakers and boots, how market umbrellas are lashed with rope, how kids skip the puddles. This place is not a testbed — it's a life."
    # play music "music_placeholder"  # [Music: Quiet, descending piano]

    scene bg ch10_291da8_7 at full_bg
    "You think of the thirty-day window like a narrowing channel: choose wrong and the tide will push through. Choose right and the friction of process might be the difference between keeping a bakery or watching it raft away."
    "The lab team looks to you. The city mailbox, Cass's message, Arman Kade's white paper, the funder's text — all converge into an axis of pressure. You feel it like central heat. Your hands are not trembling, but your fingers are aware of the rawness of the choice."
    "You feel the weight of leadership: to choose how to balance credibility, speed, and community trust. Each option is honest but imperfect; each may ask someone to bear a cost."
    "The clock whispers."

    menu:
        "Stage the public demonstration now":
            jump chapter11
        "Accept a controlled private trial with faster deployment":
            jump chapter12
        "Delay to refine models and risk council choosing Arman":
            jump chapter11
    return
