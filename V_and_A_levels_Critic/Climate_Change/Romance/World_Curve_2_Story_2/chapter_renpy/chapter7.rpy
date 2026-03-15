label chapter7:

    # [Scene: Blackbrand Negotiation Room | Late Afternoon]

    scene bg ch7_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of HVAC; distant construction clank like distant thunder; the soft tap of a stylus on glass]
    # play music "music_placeholder"  # [Music: Sparse ambient pulse, steady and restrained]
    "You step into a room that smells of citrus cleaner and new rubber—a synthetic, antiseptic scent designed to suggest order. The air feels slightly cooler than the boardwalk; your jacket carries the faint, warmer smells of kelp and wet soil behind you like evidence of another life."
    "Evelyn Black is already seated at the far side of the table. She has the posture of someone who has rehearsed patience into a weapon: shoulders squared, tablet angled so the light frames her sharp profile."
    "When she looks up, her slate-blue eyes assess you the way a tide tests a shoreline—measuring retention, erosion, the shape of what might remain."
    "Kai Navarro stands half behind you, hands folded at his waist like a man trying to keep still when his hands want to build. Dr. Leila sits with a small stack of sensor reports fanned beside"
    "her—paper edges softened from handling. Reverend Sol's cane rests against the table, his face folded in the soft, careful way someone listens for a long story. Nita's bandana is drawn low; her mouth is a narrow"
    "line."
    "You set your sketchbook on the table with a soft thud. The brass compass pendant tugs at the hollow of your throat, a private weight. You know what you came here to do: find whether the"
    "glossy promise Evelyn offers can be made to serve the town without hollowing out its soul."
    "Evelyn Black gives the slightest tilt of acknowledgment—polite, unreadable."
    show evelyn_black at left:
        zoom 0.7

    evelyn_black "Thank you all for coming. Blackbrand understands the urgency Marisport faces. We've drafted a proposal aimed at protecting the waterfront quickly, while creating public terraces and green corridors—spaces for markets, for gardens. It's not just concrete; it's modular segments with integrated living terraces. It's designed to be rapid-deploy, adaptable, and aesthetically... respectful of local life."
    "She taps the tablet; a rendered cross-section rises on the screen—sleek concrete modules with planting pockets, stair access to terraces, boat slips preserved in illustrations. The renderings look expensive and inevitable."
    "You listen, and your chest tightens. The word 'rapid' is a cold thing in your ears; it promises safety but also the speed at which decisions can swallow nuance."
    "Dr. Leila leans forward, fingers steepled."
    show dr_leila_osei at right:
        zoom 0.7

    dr_leila_osei "Evelyn, the integration of terraces and green pockets is encouraging on paper. But living shoreline strategies—reefs, oyster beds, kelp lines—function differently. They rely on biological time and sometimes slower accretion. We need to see baseline modeling of hydrodynamics with the modules in place, plus long-term monitoring commitments."
    "Evelyn Black's expression doesn't falter; she has an architecture of composure."

    evelyn_black "We've run hydrodynamic simulations and partnered with coastal firms; the modules are engineered to reduce surge energy and to allow for habitat pockets. We're prepared to fund initial monitoring. What we need from Marisport is a binding implementation agreement so we can secure permits and financing."
    "You hear 'binding' as if it were a gavel. Your mouth tastes like old tidewater. The phrase carries a legal firmness that could lock futures in place before the town has time to breathe."
    "Kai Navarro interrupts before you can:"
    show kai_navarro at center:
        zoom 0.7

    kai_navarro "Binding how? We can't agree to a contract that doesn't guarantee community governance. What are the enforcement mechanisms if the terraces are repurposed later? If leases shift or maintenance is privatized, who keeps the promise?"

    evelyn_black "We're offering a joint oversight board—representation from the municipality, community stakeholders, and Blackbrand. It will set maintenance schedules and program space. We can codify certain public uses."
    "Nita snorts softly, a sound like breaking shells."
    hide evelyn_black
    show anita_nita_ramirez at left:
        zoom 0.7

    anita_nita_ramirez "You say 'joint,' you say 'codify'—but we're the ones who get pushed out when things get...finished. I live three blocks from the promenade. Tell me how I keep my stall when a terrace becomes 'premium vendor space' paid for by corporate contracts."
    "Reverend Sol folds his hands and speaks slowly, each word deliberately worn."

    "Reverend Sol" "Words on glossy paper are not the same as stewardship. How will you protect low-income residents, long-time renters, and families who can't bid against developers when spaces are monetized? Protection must mean more than physical slabs."
    "Evelyn Black's gaze flicks toward him; for a fraction of a second something like regret crosses her features—quick as a gull passing. Then it hardens."
    hide dr_leila_osei
    show evelyn_black at right:
        zoom 0.7

    evelyn_black "We can include clauses—priority leasing for legacy vendors, community-run management stipulations, legally enforceable anti-displacement language. We have lawyers. We can bind successors to obligations."
    "You feel the room tilt—an attempt to bridge the dream of protection with the cold scaffolding of legality. The voice in your head catalogs the risks: loopholes, interpretation, the slow creep of exceptions. Your father's memory"
    "surfaces—how a single unchecked promise had cost him the sea—and the guilt at the thought of making a similar mistake knots your stomach."

    menu:
        "Interrupt, press Evelyn on legal detail now":
            "You cut across the sheen. 'What specific clause binds successors? Who enforces it if Blackbrand changes hands?' Your tone is low but sharp, and the table goes quiet. Evelyn's jaw tightens as she prepares a precise sentence."
        "Let her finish the pitch before you challenge":
            "You hold back, letting the renderings finish their sweep across the screen. Sometimes letting a sales pitch breathe reveals the seams. Kai arches an eyebrow at you, grateful for the delay. Evelyn continues, her cadence steady."

    menu:
        "Push for immediate draft review—call for lawyers now":
            "You lock eyes with Evelyn. 'We need the draft in hand before any provisional endorsement.' Your voice is steadier than you feel. Dr. Leila nods vigorously; Kai exhales like a man letting a plan exist. Evelyn's fingers tap the tablet; she accepts the demand with a cool 'we'll do that.'"
        "Propose a conditional endorsement—buy time for emergency measures":
            "You say, 'We can provisionally endorse a plan that funds immediate protective measures while we hammer out language.' Kai looks at you, relief and worry tangled in his gaze. Evelyn tilts her head, considering the political advantage of a visible endorsement, then smiles thinly."

    jump chapter8
    return
