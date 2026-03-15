label chapter3:

    # [Scene: Converted Market Hall / Town Hall | Late Afternoon — Stormlight]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Low steady piano with a soft build — hopeful, measured]
    # play sound "sfx_placeholder"  # [Sound: Rain tapping on the roof, a kettle clicking off somewhere backstage, chairs scraping]
    "The bell at the council table has already called the room into a hush once today; now the market hall holds that quiet like a breath between waves. You feel the echo of the last meeting"
    "in the muscles of your jaw — a careful tightness that’s both exhaustion and readiness. The air tastes of coffee and salt and the faint, warm green of pushed soil you carried from the rooftop this"
    "morning."
    "You tuck a wet strand of hair behind your ear and let your fingers find the small glass vial at your throat, finding steadiness in its familiar weight. There are faces you know in the crowd"
    "— Kira in her patched coat like a flag you can always see, Mateo with the slow, certain set of someone who measures time by tides, Elias farther up where he can keep the glass pane"
    "in his line of sight. Jonah stands under a floodlight, his portfolio of glossy renderings catching the stormlight like a promise."
    "You remember the council’s measured words from earlier; now the room has folded into committee waiting, and the decision you keep feeling at your ribs is no longer theoretical."

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Projector whirring faintly; murmurs as people track the lines]
    show elias_rook at left:
        zoom 0.7

    elias_rook "These are ensemble runs. Each layer is a different emissions pathway and the median here—' (he taps the pane, causing a ribbon of blue to thicken) '—shows the exposure of current food-growing zones under moderate sea rise over the next twenty years."
    "He speaks with the steady cadence of someone who builds arguments out of models. His voice is practical, earnest; you can hear the care in the way he names neighborhoods rather than numbers."
    show ayla_moreno at right:
        zoom 0.7

    ayla_moreno "And if we shift the baseline vegetation strategy — increase soil depth on the roofs, prioritize salinity-tolerant crops — how does that change the exposure?"

    elias_rook "It changes the boundary conditions. We can quantify the adaptive gains, but we need the on-the-ground feedback — the kind you've been mapping for months — to make the model actionable."
    "His eyes find yours for a beat. The look is complex: numbers and neighborhood names folded together. It holds apology and a proposal at once, neither neatly resolved. You feel that too, the pull toward partnership that could shape policy from inside the lab."
    show jonah_hale at center:
        zoom 0.7

    jonah_hale "All of this is well and necessary, but we don't have the luxury of incrementalism for the most exposed commercial arteries. My timeline secures insurance, investment, and jobs. The seawall framework is shovel-ready; financing is committed."
    "His words are slick with the cadence of someone used to turning talk into capital. The crowd shifts; the sense of urgency he conjures is immediate but measured. You match it with your own internal ledger: time lost could mean more gardens gone."
    hide elias_rook
    show kira_tseng at left:
        zoom 0.7

    kira_tseng "And what about the people Jonah's plan would push out? We need a binding moratorium on displacement before any brick is poured. Otherwise your 'jobs and investment' are built on somebody else's cleared lots."
    "Her words land like thrown rope. A few people around her nod; others frown, thinking of livelihoods counted in other columns. The room tightens, a net of competing necessities."

    menu:
        "Step up to the front and offer a quick community snapshot":
            "You rise before thinking it through; the room turns toward you as you gesture to the clusters of rooftop black dots in your palm. A hush follows, and Elias gives you a small, grateful nod."
        "Stay planted in the crowd and listen, letting others set the tone":
            "You keep your seat, letting your fingers curl around the vial at your throat. The details settle in your head; your presence is an anchor rather than a trumpet. Kira steals a look and mouths a thanks, brief as a sting of salt."

    # --- merge ---
    hide ayla_moreno
    show mayor_serena_okoye at right:
        zoom 0.7

    mayor_serena_okoye "We will not make decisions that ignore immediate fiscal realities — nor will we sign away neighborhoods. I ask those who propose policy to also propose enforceable safeguards. Evidence and guarantees, both. Not rhetoric."
    "Her expression is carved by sleepless negotiations; when she speaks the room listens like tide listening for a marker buoy."
    hide jonah_hale
    show mateo_alvarez at center:
        zoom 0.7

    mateo_alvarez "Paper's heavier, but it doesn't blink. There's an old pier marked here — it was buried years back for landfill. We built on bones before. I sailed off that pier when I was a boy. You tell me you'll build a wall and I ask what we're burying next."
    "He traces a finger over an old line. His voice is grainy from years of wind and salt. The hall hums with recognition; memory shapes policy in ways the models cannot."
    hide kira_tseng
    show jonah_hale at left:
        zoom 0.7

    jonah_hale "Historical markers are meaningful, Mateo, and we can archive them, memorialize them. But if another storm takes half the market and people lose their homes, memorials won't keep them dry."
    "The exchange is quick, back-and-forth. Jonah's cadence is the market's urgency; Mateo's is the harbor's memory. You feel the twin pulls in your chest: preservation and protection. They are both right in their own ways."
    hide mayor_serena_okoye
    show elias_rook at right:
        zoom 0.7

    elias_rook "Ayla, if we combine your mapping with scenario runs, we can show where green infrastructure reduces wave energy and how that lets us scale back hard defenses in certain corridors. It becomes a hybrid system — we protect critical nodes while keeping living spaces integrated."
    hide mateo_alvarez
    show ayla_moreno at center:
        zoom 0.7

    ayla_moreno "And you think Jonah will accept a smaller footprint if we can prove it with models?"

    elias_rook "Jonah negotiates on deliverables and timelines. He can be pragmatic if the alternative is seen as risk to his financing. But he also needs political cover. That's where Mayor Okoye's guarantees come in."

    ayla_moreno "Political cover — and legal clauses for co-management. Can you model enforceable co-management zones?"

    elias_rook "Not directly. Models measure risk and response; legal frameworks need partners. But I can build the case that integrating green canopy reduces maintenance costs over thirty years. That helps the financing model."
    "The exchange is deliberate: technical honesty, not theatrical promises. Elias is offering a bridge — a way to fold your on-the-ground knowledge into numbers that matter to decision-makers. It feels possible, and that possibility warms you."
    hide jonah_hale
    show kira_tseng at left:
        zoom 0.7

    kira_tseng "Or we stop the wall until we have guarantees. 'Modeling' is not the same as stopping construction. You two can talk numbers in the lab, but in the field people get displaced while you debate matrices."
    "Her voice carries the urgency of someone who has slept on wet sidewalks and stitched flyers in the night. There is truth in the bluntness: models move slowly; bulldozers do not."
    hide elias_rook
    show mayor_serena_okoye at right:
        zoom 0.7

    mayor_serena_okoye "We need both language and trust. The committee will need proposals with teeth: specify who manages plots, who pays for upkeep, who gets relocation funds if displacement is unavoidable. I'm asking for concrete commitments, not broad favorability."
    "The council's moderator sets the ground lines. The conversation curves upward in intensity but remains contained: mid arousal — alarms lit but not wailing. You feel the room's energy feed into your own. Something like hope takes shape: that compromise could be engineered without erasing community."

    menu:
        "Slide Mateo the last spare pen and offer to help mark the map":
            "Your hand brushes his; it's a small, quiet alliance. He hands the map back with a look that says 'we're keeping this between us' and you feel the ballast of history solid beneath your feet."
        "Listen to Kira and prepare a tactical question for the committee instead":
            "You fit Kira's urgency into a bite-sized question you can ask aloud. It sharpens your focus; you feel the engines of activism humming in your ribs."

    # --- merge ---
    "Voices rise and layer. A woman in the back asks about insurance; a young father worries about schools; a university researcher asks for data sharing. The models throw up projections; the renderings promise plazas above the"
    "wall with trees and cafés. The gallery of possibilities is simultaneously comforting and unmoored — a future that may or may not include the rooftop terraces you photograph on storm-free days."
    hide ayla_moreno
    show elias_rook at center:
        zoom 0.7

    elias_rook "Give me two weeks with Ayla's mapping data and community contacts. I'll produce a run that shows where small-scale living infrastructure buys us space and reduces the overall footprint of the seawall. If the committee will consider a hybrid pilot, we can have measurable targets and an auditable timeline."
    hide kira_tseng
    show jonah_hale at left:
        zoom 0.7

    jonah_hale "Pilots are fine if they don't delay the main work. I'm open to demonstrating co-benefits, but financing covenants require that core protections start on schedule."

    mayor_serena_okoye "Concrete proposals with enforceable milestones. A pilot that can be audited. A moratorium on demolition until the pilot's baseline is assessed. Those will go before the committee."
    "A soft murmur of assent — relief, small and bright — ripples through the hall. The people close enough to you exchange looks: hope tempered with caution."
    "Your chest tightens in a different way now; the decision you can make is no longer abstract. It will determine who stands beside you at dawn and what shape the neighborhood takes when the next storm comes."
    "You imagine the greenhouse fog, beads of condensation on the panes, the communal table scattered with seed jars. You imagine Elias at your side in the lab, mapping rainwater retention curves and laughing quietly when a"
    "model shows an unexpected win. You imagine Kira in the streets, her megaphone and binoculars an irresistible summons that rallies neighbors. You imagine Jonah across a table, his lapel pin catching the light as he signs"
    "legal guarantees into deals."
    "All three futures glimmer with possibility and cost. The room waits; Mayor Serena's eyes scan the crowd, then land on you for a fraction of a second — not an accusation, but an invitation."
    "You inhale. The stormlight slants through the pane; the piano swells and holds."
    hide mayor_serena_okoye
    hide elias_rook
    hide jonah_hale

    scene bg ch3_98c6f2_3 at full_bg
    # play music "music_placeholder"  # [Music: Piano motif crescendos gently, then steadies — hopeful, expectant]
    "You can feel the swell of the room riding the same current as your heartbeat: increasing but contained. Your voice could be a bridge, a banner, or a bargaining chip. This is the hinge moment — the strategy that will thread into policy and people."

    menu:
        "Work with Elias to design an integrated hybrid plan that centers green infrastructure while accepting selected engineering measures.":
            jump chapter4
        "Join Kira and the direct-action resistance to block Jonah's project publicly and demand a moratorium.":
            jump chapter7
        "Open a direct negotiation with Jonah to secure concessions and legal guarantees for community spaces.":
            jump chapter10
    return
