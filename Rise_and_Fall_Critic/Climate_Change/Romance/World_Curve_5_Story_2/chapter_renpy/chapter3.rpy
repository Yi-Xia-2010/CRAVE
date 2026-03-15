label chapter3:

    # [Scene: Council Chambers / Redevelopment Pavilion | Mid-Morning]

    scene bg ch3_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmur of voices, the soft clunk of a projector initializing, paper rustling, an umbrella tapping a tile]
    # play music "music_placeholder"  # [Music: A steady piano motif—the same hopeful cadence from the market—swells gently, suggesting possibility rather than triumph]
    "You step across the threshold with your notebook tucked beneath your arm, the scar under the edge of the cover pressing into your palm like an old compass. The smell here is different—cleaner, chemical, the faint"
    "ozone of LEDs and filtered air carried past the harbor's salt. It makes the town look smaller, more managed. That is the point of this room: to make choices look like diagrams."
    "People are here because they think the choices will still be theirs after they leave. Marta is a warm presence by the door, palms ink-stained from handbills, bright overalls absurd against the polished floor. Old Man"
    "Rafi sits quiet at the back, his cap dented and his eyes on the projection as if measuring waves in it. Eli stands near the table with the Helix samples, a tray of damp peat and"
    "sprouted plugs balanced in one hand like a promise. Jun is at the projector, fingers hovering over the remote, his tablet a small universe of numbers."
    "Your throat tightens—not from fear but from the same steady responsibility you feel when a tideline is revealed. The corridor you built in pieces is here as evidence: seed trays, a phased map, Jun's curves that"
    "flatten and then rise with the proposed living-shoreline plan. You remember Rafi's voice saying, 'We braid the shore, we braid our people,' and the image steadies you."
    "Lina stands to one side, watchful, her raincoat folded over an armchair. Her face is open, but you can tell by the way she shifts her weight that she is still measuring how far she can bend."
    show jun_park at left:
        zoom 0.7

    jun_park "These are conservative projections. If we phase the living shoreline—phase one small cells, phase two reed expansion, phase three community-managed breakwaters—we keep habitat function and reduce surge heights by the modeled twenty to thirty percent within five years."
    "(He taps the chart; the curve brightens.) 'The confidence intervals tighten with local stewardship; the models respond to consistent maintenance.'"
    show aria_solen at right:
        zoom 0.7

    aria_solen "We're not promising miracles,' you say, your voice steady. 'We're promising a plan that can be enacted in steps people can learn and sustain. It reduces immediate risk, creates jobs, and keeps the cultural fabric that supports those jobs."
    show eli_navarro at center:
        zoom 0.7

    eli_navarro "And we've got proof from the Helix. The floating beds damp wave energy and the families in the co-op are already seeing more reliable yields. It's not abstract—it's people with salt on their hands and mouths full of success."
    "(He sets a small tray on the table, peat beads catching the light.)"
    hide jun_park
    show caden_holt at left:
        zoom 0.7

    caden_holt "All heart, Aria. Admirable. But hearts won't keep developers' capital from drying up if we can't show a single wall that holds against a Category Four. Investors and insurers want certainty."
    "(He gestures to his renderings.) 'My plan gives that—seawalls calibrated to the new projections, elevated housing pods, a private marina that funds maintenance. It's decisive and quick.'"
    "You sense the room pivot—the old expectation that heavy infrastructure equals security. It presses like humidity."
    hide aria_solen
    show marta_quin at right:
        zoom 0.7

    marta_quin "You always make it sound like a favor, Caden—like culture is an optional accessory. The people here have lived this marsh. They know the gulls and the channels. You put a wall up, you put a price on everything that taught us how to live here."

    caden_holt "Marta, I'm proposing durable infrastructure that prevents loss of life and property. This isn't a game. We have to be realistic about timelines."
    hide eli_navarro
    show lina_voss at center:
        zoom 0.7

    lina_voss "Realistic and equitable are not the same thing. We need to bridge that gap. There has to be a way to fund safety without erasing the people who make this place alive."
    hide caden_holt
    show jun_park at left:
        zoom 0.7

    jun_park "The models show different outcomes depending on maintenance regimes. Top-down structures can fail if funding dries up. Living systems have resilience when the community is invested."
    hide marta_quin
    show caden_holt at right:
        zoom 0.7

    caden_holt "Models are only as good as the assumptions. My team has contingency funds—private capital that moves quickly. Waiting for community buy-in can cost us the season."
    "You feel the current of the exchange like a real tide: a pull one way, a pull the other, and the possibility of eddies where compromise stirs something new. The room smells faintly of coffee now;"
    "someone has left a damp cup by the projector stand. The lights pool on the table—hands, seed trays, a cuffwatch catching the sun. The decision is not only about structures; it's about who holds the next"
    "shovel."
    hide lina_voss
    show marta_quin at center:
        zoom 0.7

    marta_quin "You always make it sound like a favor, Caden—like culture is an optional accessory. The people here have lived this marsh. They know the gulls and the channels. You put a wall up, you put a price on everything that taught us how to live here."
    hide jun_park
    show old_man_rafi at left:
        zoom 0.7

    old_man_rafi "We braid the shore, we braid our people."
    "Jun leans closer to you before you step back to the mic, something small and urgent in his tone."
    hide caden_holt
    show jun_park at right:
        zoom 0.7

    jun_park "If you emphasize the numbers—cost per life-year saved, modeled decline in storm damages—the council will hear risk in their language. If you tell the people's story, you make it human. Both work; both are necessary. But pick the order. The room responds to how you want them to feel first."

    menu:
        "Glance at Eli for a quiet nod":
            "Eli meets your gaze and gives a small, steadying smile—the kind that says 'we'll show them' without theatrics. The warmth of it is like the Helix lights in the night. You feel steadier."
        "Fix your eyes on Jun's printout and the numbers":
            "Jun's printout is a map and a prayer. You focus on the confidence intervals and the steady improvement in ecosystem services—facts that anchor your words. The room feels cumulatively heavier but clearer."

    # --- merge ---
    "You choose, and the choice changes the cadence of your next sentence. If you looked to Eli, your words borrow his concreteness; if you studied Jun's pages, they inherit the weight of data. Either way, you move toward the center of the room and the microphone."
    hide marta_quin
    show aria_solen at center:
        zoom 0.7

    aria_solen "We can offer a phased approach that meets safety needs and builds capacity. Phase one complements structural protections—where necessary—with living cells that attenuate waves and rebuild substrate. Phase two expands the reedbeds into buffer networks maintained by co-ops. We train, we employ, we localize maintenance—this isn't symbolic. It's insurance carried by the people who have always paid it."
    hide old_man_rafi
    show caden_holt at left:
        zoom 0.7

    caden_holt "That's admirable, but it dilutes urgency. We either take decisive action now or we keep talking and watch the next storm write its own plan."

    aria_solen "Decisive action can look like inclusion. Walls without hands to tend them are brittle. Living systems—inserted with engineering—offer redundancy. If we coordinate funding for initial capital and keep governance local, we can have both safety and continuity."
    hide jun_park
    show lina_voss at right:
        zoom 0.7

    lina_voss "Governance will be the sticking point. Who oversees maintenance? Who holds liability? Who gets to develop the waterfront businesses? Those are not small questions."
    hide aria_solen
    show marta_quin at center:
        zoom 0.7

    marta_quin "We don't want developers deciding which families stay. We want equity. We want Rafi's channels kept. We want the market to stay a place for people, not for show."
    hide caden_holt
    show old_man_rafi at left:
        zoom 0.7

    old_man_rafi "This island remembers. It remembers the names of the channels and what they feed. Any plan that listens will last. Any plan that shouts will not."
    "Investors in the back murmur—their expressions polite but calculating. You can smell the lemon oil of the polished floorboards; it smells like meetings that end on paper."
    "Jun leans closer to you before you step back to the mic, something small and urgent in his tone."
    hide lina_voss
    show jun_park at right:
        zoom 0.7

    jun_park "If you emphasize the numbers—cost per life-year saved, modeled decline in storm damages—the council will hear risk in their language. If you tell the people's story, you make it human. Both work; both are necessary. But pick the order. The room responds to how you want them to feel first."

    menu:
        "Lead with the human story—Rafi's channel and the market families":
            "You begin with a memory: a child chasing a crab in the salt pans, Marta's hands packed with seed, Rafi's quiet instruction. The room's temperature softens; faces lift. People see their neighbors in the plan and the momentum shifts to 'protect' rather than 'replace'."
        "Lead with Jun's cost-benefit figures and mitigation curves":
            "You start with the data—loss projections if we do nothing, benefits of phased intervention. The room nods in analytical rhythm; Lina scribbles notes and the investors quiet down, listening for precise numbers to calibrate their risks."
        "Weave both—start human, puncture with hard numbers":
            "You tell Marta's story and then point, like a seam, to Jun's chart. The room follows the stitch: empathy locked to feasibility. The mood becomes focused and constructive—people are both moved and offered a path forward."

    # --- merge ---
    "You sense the air in the chamber changing; whatever vocabulary you choose maps the room's energy. People lean in, and for the first time the investors' murmurs become internal debate rather than dismissal. The piano motif lifts into a hopeful thread: perhaps the town's voice can be heard as evidence."
    hide marta_quin
    show caden_holt at center:
        zoom 0.7

    caden_holt "If we agree to this hybrid, we must bind it legally. Insurers will demand enforceable contracts. Private partners will insist on return metrics. There are ways to make community stewardship accountable—"
    hide old_man_rafi
    show aria_solen at left:
        zoom 0.7

    aria_solen "Accountability is part of stewardship. We draft performance-based milestones. We open books. We set sunset clauses for private control if targets aren't met. We offer a governance council with community seats as equals."
    hide jun_park
    show lina_voss at right:
        zoom 0.7

    lina_voss "Conditional governance with binding milestones—if you can show the mechanisms, I can defend it to council. It reduces risk politically."
    hide caden_holt
    show marta_quin at center:
        zoom 0.7

    marta_quin "Finally, some tongued sense."
    hide aria_solen
    show old_man_rafi at left:
        zoom 0.7

    old_man_rafi "Keep the channels named. Keep the children learning. Make the contracts listen."
    "There is a lull that feels less like tension and more like a collected breath. You realize, in a quiet way, that this is the fulcrum: the room is not yet fractured. It is malleable. Trust"
    "is thin and real, like the skin of a seedling—press, and you will bruise; support, and it grows."
    hide lina_voss
    show caden_holt at right:
        zoom 0.7

    caden_holt "I want stability as much as anyone. I'm not blind to culture—I'm trained to deliver it at scale. If we can structure safeguards, perhaps a combined approach could be faster than either of us predicts."
    "You feel something like a horizon line move: an opening where possible meets practical scaffolding."
    "Eli Navarro catches your eye and gives another small nod. The look feels like a pact: we'll keep doing the work, and we'll make sure it counts. Your chest loosens with that small, private hope. Jun"
    "clears his throat, as if to say the numbers are ready to be translated into the ledger of policy."
    "Lina stands and looks at the council members in their semicircle, then at you. Her face is tired but open. She places her hand flat on the table as if testing the surface for solidity."
    hide marta_quin
    show lina_voss at center:
        zoom 0.7

    lina_voss "We're at a vote point. The council wants a recommendation—an approach it can back. Aria, this is where the public record will name the path. Caden has his redevelopment blueprint; Aria, you have a phased living-shoreline plan with clauses for governance and maintenance. People here have expressed their hopes and their risks."
    "You feel all the work pull into a single, luminous hinge. The room quiets—the murmur subsides, breaths audible. The projection shifts to a blank slide, an invitation."
    "Your internal monologue runs through stakes like a checklist—community trust, investor timelines, people's livelihoods, your own fear of repeating past loss. But above all is the rising possibility: that the town could choose a path that both secures safety and honors place. That is the note you want to strike."
    "You stand with the microphone warm in your hand. The decision will be public and it will define the next steps: align with the co-ops and refuse compromise, negotiate conditional compromise, or force transparency by leaking the redevelopment data. None are without cost; all are honest in their risks."
    # play music "music_placeholder"  # [Music: The hopeful piano motif holds a suspended chord—expectant, inviting action]
    "You can feel the current tugging you toward a direction. The room leans with you. The moment is perfectly alive with possibility."

    menu:
        "Stand with the co-ops—refuse to compromise and mobilize community action.":
            jump chapter4
        "Negotiate a conditional compromise with Lina/Caden—seek hybrid governance.":
            jump chapter7
        "Leak the redevelopment's draft data anonymously to the press to force transparency.":
            jump chapter10
    return
