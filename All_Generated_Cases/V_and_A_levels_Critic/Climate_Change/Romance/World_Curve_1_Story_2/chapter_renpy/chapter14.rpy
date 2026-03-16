label chapter14:

    # [Scene: Municipal Council Hall | Dawn]

    scene bg ch14_9d8ae5_1 at full_bg
    # play music "music_placeholder"  # [Music: Accelerated piano arpeggios under a taut string ostinato]
    # play sound "sfx_placeholder"  # [Sound: Low roar of the crowd in the plaza; coffee cups clink; a courthouse clock ticks]
    "You move through the same doors you used to cross when the town still treated civic meetings as polite formalities. The lobby smell—coffee, damp wool, salt carried on someone's coat—follows you in. Your hand finds the"
    "pen you hovered over the night before like an old habit; it feels less like a tool and more like a hinge between two possible futures."
    "The chamber is already assembling into its habitual geometry: wooden panels, rows of chairs, a raised dais catching the gray dawn light. Cameras are set like small, watchful birds. Volunteers line the back benches with knitted"
    "banners; a reporter's recorder blinks red. Your Moleskine is bulging with amendments, testimonies, and the hastily drawn maps you taught to a dozen hands last week."

    scene bg ch14_9d8ae5_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Dr. Noor's measured breath beside you]
    show dr_noor_patel at left:
        zoom 0.7

    dr_noor_patel "Tide sensors show the thresholds we've been worried about. If we don't lock trigger levels into policy, we leave enforcement to whoever has the loudest lawyers."
    "You look up at her—the calm line of her face, the white braid pinned against a gray sweater—and for a moment the scientist and the counselor in her overlap into one steady presence. Her tablet screen"
    "throws blue light across the page edges, tidal graphs rising like a series of insistences."
    show ari_navarro at right:
        zoom 0.7

    ari_navarro "We can translate thresholds into conditions, but language matters. 'Trigger' becomes litigation if we don't build a procedural backbone around it."

    dr_noor_patel "Exactly. The data will back you, but you need legal form."
    "You feel the morning thicken with deliberate motion. Outside, Sora's presence is a living hum—organizers in the plaza, banners tied to lamp posts, a makeshift stage where a chorus of voices reads names of neighborhoods at risk. Their drums keep a steady heartbeat against the building's stone."
    # play sound "sfx_placeholder"  # [Sound: Distant chanting, rhythmic, not angry—insistent]
    hide dr_noor_patel
    hide ari_navarro

    scene bg ch14_9d8ae5_3 at full_bg
    show sora_watanabe at left:
        zoom 0.7

    sora_watanabe "We will not let 'consultation' be a euphemism for delay. We demand teeth. We demand enforceable rights to retreat and to protect our commons!"
    "Inside, Sora's words land like stones on a pond. Several council members wince; a few volunteers clap; Lina's gaze—cool, assessing—finds you and tilts in what could be approval or invitation. Her trench coat is unzipped at"
    "the collar; she looks like someone who has slept two hours but is already three moves ahead on the board."
    show lina_moreau at right:
        zoom 0.7

    lina_moreau "Tight language scares some funders, but it galvanizes voters. Which do you want to catalyze, Ari—power to act, or durability of funding?"
    "Your chest tightens in the way it does when you try to fold two truths into a single sentence. You want both. You want enforceable authority that won't be bought, and you want the practical money to build the pilot projects that prove it works."
    show ari_navarro at center:
        zoom 0.7

    ari_navarro "I want both. But I know that desire is not an argument. We need a path that draws the funds without hollowing the community voice."

    lina_moreau "Then we word it so the authority is conditional on transparent pilot benchmarks. Politically, it's easier to sell. Practically, it's enforceable—if we don't cave later."
    "A pause like a held breath. You can feel the arousal in the room—higher than last night, edges sharpened by the drums outside and the clock's insistence. This is not chaos; it's focus kinked tight. The town is asking you to mediate between moral urgency and institutional levers."

    menu:
        "Open the hearing with a hardline statement—'We will demand binding authority.'":
            "You stand and place your Moleskine on the lectern. Your voice slices through the room: it is firm, precise; it names binding authority as the minimum standard. Some faces brighten with relief; others narrow. The cameras pivot. You feel Sora's exhalation of something like triumph outside."
        "Begin by summarizing shared values and inviting testimony before framing legal options.":
            "You clear your throat and invite testimony first, promising to present legal frameworks afterwards. The room relaxes fractionally; a grandmother at the back wipes her eyes with a tissue and nods. Sora's jaw tightens—impatient, but not hostile. Lina's expression remains carefully neutral."

    # --- merge ---
    "You decide (the scene doesn't show the outcome yet), and the room unfolds around that echo of intent."
    "The choice you make—now or later, moral certitude or patient building—ripples faster than any of you expect. The hearing establishes tone: how confrontational will the council be, and how open to being shaped?"
    "You decide (the scene doesn't show the outcome yet), and the room unfolds around that echo of intent."
    hide sora_watanabe
    hide lina_moreau
    hide ari_navarro

    scene bg ch14_9d8ae5_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Voices layer—testimony, objections, whispered fact-checks; Sora's rhythm on the plaza persists]
    "Maya Cruz [wry] squeezes your shoulder as she takes a seat beside you, her fisher's raincoat still damp at the hem."
    show maya_cruz at left:
        zoom 0.7

    maya_cruz "You remember old Mrs. Velasco? She's got a list of patchwork stories that'll make anyone who'd cut corners look like a monster. Use them."
    show ari_navarro at right:
        zoom 0.7

    ari_navarro "I will. Stories are the infrastructure of care."

    maya_cruz "Then build with them."
    "Ephraim Blake [smooth] arrives late, as if time could be bent to his schedule. His suit seems almost to repel the damp. He offers a rehearsed smile and a folder that smells faintly of starch and money."
    show ephraim_blake at center:
        zoom 0.7

    ephraim_blake "There's a middle ground. Private capital can expedite construction—more lives protected, faster. We propose a public-private memorandum to fund the levee ring and vertical housing."
    hide maya_cruz
    show sora_watanabe at left:
        zoom 0.7

    sora_watanabe "We've heard 'expedite' before. Expedite for whom, Ephraim?"

    ephraim_blake "For the town."

    sora_watanabe "Or for someone's profit margins."
    "Inside, the back-and-forth quickens. You call for civil procedure—three minutes per testimony, a clarifying question allowed, then a response. You find yourself translating technical thresholds into ordinary language, showing why a one-meter trigger differs from a two-meter one in lived consequences: flooded basements, displaced families, vanished murals."
    hide ari_navarro
    hide ephraim_blake
    hide sora_watanabe

    scene bg ch14_9d8ae5_5 at full_bg
    # play music "music_placeholder"  # [Music: Increasing tempo strings; brass punctuations on key phrases]
    # play sound "sfx_placeholder"  # [Sound: Occasional murmurings of dissent; a reporter whispering into a recorder]
    show lina_moreau at left:
        zoom 0.7

    lina_moreau "If we bind the council now, we invite lawsuits. We can win, but the timeline is litigation—years. If we stay advisory, we can pilot and scale without being strangled by legal inertia."
    show sora_watanabe at right:
        zoom 0.7

    sora_watanabe "Advisory is a word for 'maybe'—it lets developers keep doing what they want. We've watched 'maybe' erode our neighborhoods."
    show ari_navarro at center:
        zoom 0.7

    ari_navarro "Both points are true. Litigation can be real and ruinous; advisory can be evasive. We need a mechanism that can both protect and prove itself."
    hide lina_moreau
    show dr_noor_patel at left:
        zoom 0.7

    dr_noor_patel "The sensors will give us empirical checkpoints. Tie authority to demonstrable pilot success—specific measures we can monitor. That makes the policy defensible."
    "You fold Noor's suggestion into the argument like drafting a stitch that might hold two frayed edges together."

    menu:
        "Step outside for a minute—speak to Sora and the crowd to show solidarity.":
            "You step out into the rain-thinned air. Sora looks like light and coal—relentless. You clasp hands; the crowd perks at your presence. Their cheers are immediate and fierce. You feel solidarity as a physical warmth, and Sora presses a leaflet into your hand like a small weapon."
        "Stay and keep control of the chamber—you're needed to manage the flow here.":
            "You stay seated, hand on the stack of amendments. Lina nods at the steadiness you provide. The meeting continues in a managed, efficient rhythm; some outside voices sound a little more distant, but the procedural core holds."

    # --- merge ---
    "Both choices promise a gain and a concession; momentum tilts differently. Whatever you do, the day tightens into its most decisive conversation."
    "Both choices promise a gain and a concession; momentum tilts differently. Whatever you do, the day tightens into its most decisive conversation."
    "You spend the next hour shepherding testimony—an old fisherman describes how an unauthorized seawall drowned a marsh; a teacher reads a list of children who have lost field trips to the drowned creek; a local restaurateur"
    "talks about leases that entangle tenants to land they can no longer afford to stay on. Each story presses at the raw edge of policy."
    "You find yourself teaching people on the dais how to read the maps you've drawn—where wave overtopping will first touch homes, where cumulative subsidence makes evacuation impossible—and you do it gently, with patience that feels like"
    "repair work. Lina watches you speak in that mode, and something like admiration flickers across her face before she masks it with a thoughtful frown."
    "Lina Moreau: (after a long pause) 'You have a talent for translation. You frame fear as actionable risk—people hear that and move. If we can codify a process that triggers authority based on the pilot data you just outlined, we can make it defensible.'"

    sora_watanabe "Defensible to whom? They'll write legal memos that carve us into smaller parcels."

    ari_navarro "Then we write the memos with community oversight baked in. Transparent triggers, public audit clauses. We make capture harder."
    hide sora_watanabe
    hide ari_navarro
    hide dr_noor_patel

    scene bg ch14_9d8ae5_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The room's murmur crescendos into a tight knot of voices]
    "The council debate evolves into a negotiation dance: Lina's legal language, Dr. Noor's data thresholds, Sora's grassroots insistence, Maya's local testimony, Ephraim's thinly veiled offers. You mediate not by erasing conflict but by moving it into a shared workspace—turning shouting into clauses, slogans into tests."
    "Your chest burns with exertion and hope in equal measure. This is high arousal, yes, but it is a purposeful intensity—sweat at your hairline, heart rate quickening in your chest, hands ink-stained, voice hoarse from the work of making words do justice."
    show lina_moreau at left:
        zoom 0.7

    lina_moreau "I grew up where decisions were made behind curtains, and then the floods took what mattered. I don't want us to replicate that. If this council has teeth, they must also have oversight. I can draft language that binds developers, but I will need political cover."
    "You study her. The alliance forming is tentative—each concession a careful step toward mutual trust. There is a warmth in the partnership that isn't a promise of romance; it is a shared workload, a slow building of intimacy through labor. It feels, in its own way, like repair."
    "Dr. Noor taps a chart and looks up at you, her expression expectant."
    show dr_noor_patel at right:
        zoom 0.7

    dr_noor_patel "We should decide the model now: binding authority, advisory, or phased conditional authority tied to pilot benchmarks. Each has trade-offs."
    "You can feel the crescendo—you've guided the debate to this fork. Outside, the plaza's chant rises a layer higher, as if sensing the gravity of what will be endorsed inside. The room leans in. Cameras thread the space like nervous flies."
    hide lina_moreau
    hide dr_noor_patel

    scene bg ch14_9d8ae5_7 at full_bg
    # play music "music_placeholder"  # [Music: Full ensemble swells—strings, brass, a driving drum—then tightens into a single held note]
    "You think of the town: of the mural that used to be on Flooded Row, of the childhood of someone you loved and lost, of the stubborn dignity of people who keep planting reeds in a"
    "ground that the sea insists on taking back. You think of Lina's careful pragmatism and Sora's fierce insistence. You realize, with a kind of minor astonishment, that none of the choices will be a simple triumph—but"
    "one will move the town forward in a way you can live with."
    # play sound "sfx_placeholder"  # [Sound: A deep, singular inhale passes through the room; even the crowd outside seems to draw breath]

    jump chapter15
    return
