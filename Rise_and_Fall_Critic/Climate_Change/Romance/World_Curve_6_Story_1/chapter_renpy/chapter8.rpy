label chapter8:

    # [Scene: Tidehaven Boardwalk | Morning]

    scene bg ch8_6b08b4_1 at full_bg
    # play music "music_placeholder"  # [Music: Low hopeful strings, light percussion]
    # play sound "sfx_placeholder"  # [Sound: Distant bell from the town hall; gulls; the soft shuffle of feet and paper]
    "You step off the lab's sluiced porch and the salt air hits like an answer you half-expected. Your coat is still heavy with the tablet's glow; the compass at your collar ticks against your sternum, steady as a heart."
    "The square by Town Hall is already a small, organized confusion. Jonah Reyes's people have laid stakes and strung up photo banners—paper Polaroids of docks and nets and a pier that used to be. Kai moves"
    "through the crowd with a megaphone, sleeves rolled, seed packets visible in his pack. Old Bento stands a few yards back, hands folded, looking at the banners like he reads a litany."
    "You smell coffee, wet wool, and the tang of seawater. Voices braid: someone is chanting about livelihoods; another voice reads a legal notice; a child's laughter makes the edges of the protest less severe. It isn't"
    "just anger; it's a town showing its scars and offering them up to be seen."
    "You let the sound settle into you and then walk toward the steps. Evelyn is already there, adjusting a scarf like she’s tightening a knot that keeps the council whole. Her eyes briefly catch yours—tired, wide, glad—and you feel the odd lift of being expected and needed at once."

    menu:
        "Step up to Jonah Reyes and touch the banner":
            "You run your fingers along the edge of a Polaroid, tracing a younger tide-line. Jonah Reyes looks up; his mouth softens—an old thing between you two, unspoken and close."
        "Stay back and watch the crowd breathe":
            "You let the scene move through you: the rhythm of chants, the way people fold their grief into purpose. Jonah Reyes's silhouette reads as a presence rather than an address. You steel yourself, collecting impressions you'll need inside."

    # --- merge ---
    "The scene continues as you move toward Town Hall."
    "Jonah Reyes catches your eye across the rail. His amber gaze is a steady burn—searching, waiting. When he lifts his chin toward the boardwalk, there's a question in the motion, a permission-seeking you recognize from years"
    "when he wanted you to come down on the side of the nets. Whatever past you share with Jonah Reyes is a complicated map; the look is complex—warm, a little wary, the way sea-weathered wood holds"
    "knots. You reply with a small, even nod that says both 'soon' and 'listen' without promising anything final."
    # [Scene: Tidehaven Town Hall | Late Morning]

    scene bg ch8_6b08b4_2 at full_bg
    # play music "music_placeholder"  # [Music: Piano motif—soft, ascending]
    # play sound "sfx_placeholder"  # [Sound: Papers shuffling, low murmurs, a city clerk tapping a gavel]
    "Evelyn's voice carries when she calls the meeting to order. It is the sound of someone threading a long, frayed rope back together."
    show evelyn_sato at left:
        zoom 0.7

    evelyn_sato "We have a packed agenda. First, presentation of the recommended defense plan. Dr. Verma, you have the floor."
    "Asha Verma steps up with that deliberate gait—coat straight, tablet under one arm, presence like a tide pulling everything toward consequence. The room quiets itself around her surgical clarity."
    show asha_verma at right:
        zoom 0.7

    asha_verma "Thank you. The models are on the screen. The sea-gate, paired with reinforced berms and enforced retreat in critical zones, offers the most consistent protection across the scenarios we consider most likely. It is decisive. It is implementable."
    "Her voice is unadorned; there is no theater. You watch people's faces—some nod, others tighten. For everyone, the projection draws a future in lines: teal arcs where water will be guided, solid bars where land will be held."
    "Dr. Lian Zhou takes the podium after Asha Verma, and when she speaks your laptop hums with the same overlays, Lian's data syncing in a quiet collaboration."
    show dr_lian_zhou at center:
        zoom 0.7

    dr_lian_zhou "The sea-gate reduces modeled flood frequency by a factor that, in many scenarios, buys communities multiple decades. But it's not neutral. We project shifts in salinity in back-bay areas that will alter marsh ecology and some fisheries. Monitoring and active management will be essential."
    "Her voice is even, but you see the way the room catches at the word 'decades'—relief—and at 'salinity'—concern. You know the math; you also know the people behind those numbers."
    "You step forward to present. The GIS overlay is yours to steer, and your thumb hesitates over a toolbar as if it were a compass pointing in several true directions at once. The models loop, teal"
    "and ochre morphing, and you feel the old steadiness—the work of translating data into a language that people can hold in their hands."
    hide evelyn_sato
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "The sea-gate is not a magical theater curtain that erases all consequences. It’s a tool. It buys time. It also forces us to reckon with what we choose to protect—and what we choose to let go."
    "You emphasize a phased timeline—how bridges between engineered edges and living shorelines can be staged, how retreat could be enforced more humanely if paired with relocation assistance and livelihoods programs. You speak of cordgrass plantings and volunteer marsh pilots as integral, not ornamental."

    asha_verma "If my proposal lacks room for community-led restoration, that's my failure to communicate. I want the marsh phase integrated as a mandatory follow-up. But we cannot, in good conscience, wait until the next extreme event."
    "You meet her eyes—steel-blue, pragmatic—and you sense a truer alignment: she demands urgency; you demand humanity. The two aren’t incompatible, but making them sit together will take work."
    hide asha_verma
    show evelyn_sato at right:
        zoom 0.7

    evelyn_sato "We must balance pace and care. That is this council's job."

    menu:
        "Highlight the human stories—invite Bento to speak now":
            "You gesture toward the back. Bento shuffles to the microphone, hands weathered, and tells a short, exact story about a lost net and what it meant. The room quiets in a way data alone never commands."
        "Lean into the numbers—show Lian's projected timelines":
            "You bring the overlay forward and run through the models step by step; charts unfold, probabilities sharpen. People listen differently—some with relief, some with furrowed brow."

    # --- merge ---
    "Public comment opens and the chamber reacts to the chosen emphasis."
    "Bento speaks if you chose him. His words are simple and sharp—memory folded into metaphor. He says the town is a body and that you can stitch a wound in ways that don't excise what makes"
    "it a town. When he talks, even those opposed to his politics remember who these decisions are for. There is a collective inhalation in the room, like a tide pulling back to show the shoreline."
    "Or, if you pushed Lian's numbers, the chamber tilts the other way: policymakers tuck the data under their arms like armor. The math comforts the technocrats and alarms the storytellers."
    "Kai stands when public comment opens and talks fast and bright about community pilots—the seedlings of stewardship, the agency of those who will live on the margins of your plans. Jonah Reyes follows, stepping in from the square with his hands still raw from the banners."
    hide dr_lian_zhou
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "This isn't just about defense. It's about who gets to fix things. We can do the sea-gate, fine. But don't make the community a footnote. Let us show you how we can plant, monitor, and adapt it with you."
    "His voice carries the salt and the wry humor; he is both pleading and practical. The chamber hums with response—cheers, a few boos, and then a hush when he looks toward you. His gaze is searching, not accusing. It's asking for permission to be included, not permission to block."
    hide mira_kestrel
    show asha_verma at left:
        zoom 0.7

    asha_verma "Inclusion is not the enemy of protection. It's a necessary component. I have built enforceable phases that include community oversight—even legal requirements for marsh pilots."

    jonah_reyes "Enforceable by whom? The people who don't live where the water actually comes in? You tell me someone will be relocated and then expect them to trust a promise on a tablet."

    asha_verma "I do not ask trust blindly. I ask for measurable guarantees. Funding tied to relocation assistance, legal covenants, audits. We can build oversight."
    "The back-and-forth opens a seam in the room—political, personal, procedural. Evelyn moderates, more of a shepherd than an arbiter."

    evelyn_sato "We will record these statements. Council, we must decide whether to recommend immediate installation with enforced retreat, support parallel community pilots with tied monitoring, or pause for more independent studies."
    "Your laptop shows Lian's overlay beside Asha Verma's plan. The data and the banners exist in the same frame now—science and memory, the town's sentiment and regional obligations."
    "You taste metal—nerves, the tang of being the fulcrum—and then you remember the rise in the music outside: people are here, engaged, choosing to act. That is itself progress. Whatever this council decides, the town is awake and assembling its voice."

    menu:
        "Frame your recommendation as 'protect first, integrate later'":
            "You emphasize risk reduction and timelines, promising marsh phases and oversight as binding clauses. Some people clap; others look away, the cost of 'protect first' weighing in their faces."
        "Argue fiercely for parallel pilots and monitoring tied to construction contracts":
            "You make the marsh pilots legally inseparable from any engineering contract. The room brightens at the idea of shared stewardship but government lawyers in the back make small, worried notes."
        "Call for a delay and more independent studies—buy time for a better stitch":
            "You ask for a pause to commission independent oversight. Relief and fear ripple—some breathe easier at the thought of more clarity; others whisper about storms and missed windows."

    # --- merge ---
    "The council reaches the point of formal recommendation and vote."
    "Every phrasing you choose changes what the room imagines as possible. You see faces: an elderly woman whose house sits near the back-bay, a young father with a toddler on his lap, a developer with a legal pad open. Each hears a different promise."
    "Jonah Reyes crosses the aisle and stands near the microphone again, closer to you than before. He does not raise his voice. He leans forward, as if confiding."

    jonah_reyes "If you go full gate and tell us stories later, you'll lose people. If you tie pilots to the gate, you'll give us a hand in the work. I want the town to be stronger after this, Mira. Not smaller."
    hide evelyn_sato
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "I want that too. That's why I'm asking—out loud—how we bind the protection to people's lives. I'm not offering platitudes. I'm asking for mechanisms: funding, legal aid, jobs for relocation, a council oversight seat for the Collective."

    asha_verma "I'll accept contractual clauses. We'll write monitoring into the procurement. We'll reserve a portion of funding for community-led restoration—mandatory, audited, and timebound."
    "There is a moment of unexpected unanimity—hardly resolution, but progress. You feel hope swell, like a small reef forming under what used to be bare sand."
    "Evelyn closes her eyes for a fraction of a heartbeat and exhales."
    hide jonah_reyes
    show evelyn_sato at center:
        zoom 0.7

    evelyn_sato "We have arrived, then, at the core questions. Councilmembers, the public—"
    "Your chest tightens; the room narrows into the point of decision. The bell outside tolls once, a single pendulum of sound that feels oddly like blessing. The trajectory you have held—of urgency balanced with inclusion—has momentum"
    "now. People are collaborating across old rifts; Asha Verma has conceded mechanisms; Jonah Reyes has pushed a communal frame that has teeth."
    "You swallow. Your voice trembles—not from fear alone but from the weight of possibility."

    mira_kestrel "These choices are not binary in the lives they touch. We can design protections that buy time and also require the town's hand in what gets rebuilt. We can make the marsh a legal, funded phase. We can write oversight into every contract."
    "You look at Jonah Reyes. His face is an open map of hope and contained fear. He nods once—small, fierce. You look at Asha Verma. Her stare, still steel-blue, has shifted. It is not less urgent"
    "but it is less solitary. You look at Evelyn; she looks back like someone who has been holding a fragile thing and is ready to set it down into the hands of others."
    "The chamber leans forward. Your role is to choose the recommendation to carry into vote—a recommendation that will sway funding, timelines, and what the town asks of its people. The hour is charged with the kind of uplift that comes when a battered community decides to act together."
    hide asha_verma
    hide mira_kestrel
    hide evelyn_sato

    scene bg ch8_6b08b4_3 at full_bg
    # play music "music_placeholder"  # [Music: Strings swell gently—rising, hopeful]

    menu:
        "Push full-on for the sea-gate and enforce retreat in critical zones.":
            jump chapter9
        "Insist on parallel community pilots and tie implementation to monitoring.":
            jump chapter9
        "Pause to broker a phased approach and ask for more independent studies (delay implementation).":
            jump chapter14
    return
