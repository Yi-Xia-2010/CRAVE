label chapter2:

    # [Scene: Municipal Hall | Late Afternoon]

    scene bg ch2_c4ca42_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, measured strings; a single piano note repeats like a tide-slow metronome]
    # play sound "sfx_placeholder"  # [Sound: Low murmur of conversation; the distant slap of a gull's wing beyond the building]
    "You step into the municipal chamber carrying the small, familiar weight: your field notebook pressed beneath your arm, the waterproof wristband warm against the pulse at your wrist. The hall smells of stale coffee and antiseptic."
    "Glass walls reflect anxious faces — rows of neighbors bent into themselves, crews in faded sweaters, teenagers with sunburned collars, Mayor Lynette's sharp silhouette moving between them like a practiced tide."

    scene bg ch2_c4ca42_2 at full_bg
    "The lectern is colder than you expect; your palms come away a little damp. The chrome table in the center of the room already glows with projected waterlines — a flat, clinical horizon that slides across"
    "topographic models. Cass’s firm has polished the visuals until even the worst flood looks tidy. Next to his display, Mayor Lynette sets down glossy renderings with the small, precise gestures of someone who has practiced applause"
    "lines."
    show mayor_lynette_cole at left:
        zoom 0.7

    mayor_lynette_cole "Thank you all for coming. I know this has been a hard season. We're here to decide how Brinehaven moves forward."
    "Your breath finds the rhythm of the strings in the room. You feel the ledger of losses inside you — the roof that folded, the boat you couldn't save — folded small and secret under your ribs. They are not arguments. They are reasons."
    show cassian_cass_romano at right:
        zoom 0.7

    cassian_cass_romano "We've modeled a seawall system tailored to Brinehaven's contours. It reduces overtopping by sixty to seventy percent under projected storm scenarios, and it can be phased to minimize disruption."
    "Cass's voice is controlled, the kind of measured calm that hides urgency behind clarity. He taps his tablet; the waterline morphs into a schematic cross-section. Tactile detail: the edges of his trench coat still carry a"
    "faint smell of ozone from the models being printed earlier. His grey eyes are precise in the way of someone tracking variables."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "Seawalls don't come cheap. They don't fix the marsh. What about the fish? What about our nets on the bayside? You expect us to trade our moorings for concrete?"
    "Jonah's hands are clenched around the wooden compass on his lap. The carved grain catches the lamplight; salt beads at the cuff of his sleeve. There's a rawness in his tone that pulls at something you try not to name. He looks at you, then looks away — expression complex."

    mayor_lynette_cole "Funding exists, but it depends on decisive leadership. We need a plan that shows voters — and grantors — we aren't dithering."
    hide mayor_lynette_cole
    show old_man_rafi at left:
        zoom 0.7

    old_man_rafi "Listen. I remember a spring when the marsh changed its mind. We could read the water then; a man with his hands on the tide could tell you what the line meant. We learned to move with the sea, not always fight her."
    "He leans forward, the room drawing closer to his story. His beard has a single blue bead braided in; the bead swings gently as he speaks. The smell of peat and rope and a life lived against the wind seems to press into the air."
    hide cassian_cass_romano
    show tessa_kestrel at right:
        zoom 0.7

    tessa_kestrel "Stories are beautiful, Old Man Rafi, but we need roofs over our heads this winter. People are out of work; boats are rotting. We need action now."
    "Her words land like a slap and then a soft apology. Tessa's hands twist the hem of her thrift-store hoodie — nervous energy that tastes of hope and impatience. You see her, and the knot in your chest tightens again. Her future is why you came home."
    "The projected table breathes — lines pulse faintly as someone dims the lights to show Cass's animation. You feel the lectern's edge under your fingers, the same wood smoothed by years of public business. The room"
    "is an ecosystem of small sounds: a pen clicking, the low scrape of a chair, a cough that becomes a chorus."
    "You step forward because it feels like the most honest dishonesty: to let numbers speak for the people you love. You rest your palm on the stack of printouts, feel the paper's texture, and let your other hand hover over the wristband that measures tides and keeps secrets."
    hide jonah_reyes
    show mira_kestrel at center:
        zoom 0.7

    mira_kestrel "The models are useful. They tell a part of the story — the mechanical part. But they don't tell us who will lose what when the wall goes up, or which livelihoods will be made unworkable. Living shorelines and marsh restoration slow the encroachment and retain the biological services that local fishers rely on. Distributed defenses buy us time without forcing a single, permanent reshaping of our coast."
    "You say the things you've measured, the trade-offs you keep awake over at night. You say them with the steadiness you reserve for lab notes, but the words carry more: the underside of memory, the weight"
    "of absence. Your voice cracks once. The room doesn't rush in to fix it; they count the crack like a tide mark."
    hide old_man_rafi
    show mayor_lynette_cole at left:
        zoom 0.7

    mayor_lynette_cole "Mira, those solutions are slower. They look less like leadership to a funding body seeking quick returns. I need to show results before winter."
    "You watch her mouth shape the sentence; her bob is immaculate, her intent as sharp as the crease in her sleeve. You understand the pressure from above — grants, press cycles, the calculus of visible wins — and it tastes like dry salt on the back of your tongue."
    hide tessa_kestrel
    show cassian_cass_romano at right:
        zoom 0.7

    cassian_cass_romano "I want to work with community knowledge. I've incorporated marsh buffers in other projects. We can phase construction, include local labor, and commit to a community oversight board."
    hide mira_kestrel
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "Phase construction into what? A promise from a firm with shareholders? How do we know the oversight won't be window dressing?"
    "Cass’s hand flexes; his jaw tightens. There's earnestness there, but also a plasticity — a measured rehearsal of goodwill that doesn't quite settle. Jonah's mistrust is a lens through which half the room watches him."

    menu:
        "Emphasize the human stories first":
            "You lean into the microphone and tell a short, precise anecdote about a family who lost their clapboard home last season, naming the exact income lost and the part of the marsh that held their nets. A few faces soften; a woman in the second row wipes her eyes."
        "Begin with the data visualizations":
            "You gesture to the projected animations and walk the room through the worst-case scenarios — storm surge heights, projected shoreline recession. Heads lower into screens and notepads; a council aide starts recalculating figures out loud."

    # --- merge ---
    "The scene continues."
    "The room shifts depending on your move. Words land and are absorbed in different ways — like rain on reeds, like rain on tar. You watch the people respond; some suggest empathy, others ask for proof. Both are correct. Both are inadequate alone."
    hide mayor_lynette_cole
    show old_man_rafi at left:
        zoom 0.7

    old_man_rafi "We have to remember that when the sea teaches, she does not forgive small mistakes. Think of the child who learns tides by watching, not by being told."
    hide cassian_cass_romano
    show tessa_kestrel at right:
        zoom 0.7

    tessa_kestrel "Then let's teach them quickly. Plant saplings, begin oyster beds, divert a little of the town budget to small grants. We can show progress now and keep pushing for larger projects."
    hide jonah_reyes
    show mira_kestrel at center:
        zoom 0.7

    mira_kestrel "I want to move fast, too. But haste without measurement can make messy results permanent."

    tessa_kestrel "And what about sitting and measuring while the next widow loses a roof?"
    "There is a sting to that; it lands between you and the room like a cold current. Your notebook presses against your ribs. You feel small and enormous at once."
    hide old_man_rafi
    show mayor_lynette_cole at left:
        zoom 0.7

    mayor_lynette_cole "We can't oscillate. The grants won't wait forever. We need to vote on a path so we can begin implementing."
    hide tessa_kestrel
    show cassian_cass_romano at right:
        zoom 0.7

    cassian_cass_romano "A combined plan is possible. A phased seawall where living shorelines are integrated between engineered segments. We can pilot marsh restoration in the more sheltered coves while the harder edges are reinforced. It's not all or nothing."
    hide mira_kestrel
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "Pilots sometimes run out the clock. They test while we bleed."

    "Cass" "Then give me the oversight. I'm willing to sign a legally binding community partnership. Put representatives on the contract. Tell me what the metrics are. I will take accountability."
    "Dialogue unfolds like tidal exchange — push, pause, withdrawal. You are a mediator because you cannot do nothing, and because your training taught you to make trade-offs instead of absolutes."

    menu:
        "Ask for a community-led oversight clause":
            "You ask Cass to include a clause that requires a rotating community seat on any contract and specific, public milestones for environmental metrics. The room murmurs agreement; Old Man Rafi nods slowly."
        "Propose an independent audit first":
            "You suggest an independent environmental audit before any construction begins to bench test the projected impacts against local ecological knowledge. The mayor raises an eyebrow; a council aide begins to whisper about timeframes."

    # --- merge ---
    "The scene continues."
    "You can feel the room leaning. Not all in the same direction. Some people are pulled toward the pragmatic: concrete, immediate, certifiable. Others are anchored to tradition and ecological memory. The tension is not loud; it is the low, persistent ache of low tide scraping against a foundation."
    hide mayor_lynette_cole
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "Whatever path we choose, let's make a guarantee to the people who will live with the consequences. Not promises we can handwave away with ribbon-cuttings, but accountable measures: phased funding with community checkpoints, employment guarantees for local workers during implementation, and a durable mechanism for adaptive retreat where needed."
    hide cassian_cass_romano
    show mayor_lynette_cole at right:
        zoom 0.7

    mayor_lynette_cole "Those sound good on paper. But who enforces it? Who pays when the models are wrong?"
    hide jonah_reyes
    show cassian_cass_romano at center:
        zoom 0.7

    cassian_cass_romano "We do. The firm can underwrite part of the early risk —"
    hide mira_kestrel
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "You? Or the firm you work for? What's to stop them from walking when the tab gets heavy?"
    "Cass’s jaw thins. He looks at you, and for a heartbeat his expression flickers — respect, irritation, something unreadable — before he masks it again."
    "A boo rises from the back of the room like a small wind. A smattering of polite claps follows as someone tries to steer the mood. Paper shuffles, chairs scrape, a child coughs. You feel the pressure of eyes like weathered hands on your back."

    mayor_lynette_cole "Let's put it to a consensus. Speak now, Mira. The town is listening."
    "Your mouth tastes of metal. You inhale, feeling the low-pitched strings swell the tiniest degree. It is a slow, tidal swell, not a breaking wave — low arousal, but undeniable buildup. The room narrows to a tunnel of faces, each carrying an argument, a loss, a hope."
    "You know what is at stake: livelihoods that could be eroded by the wrong architecture; cultural memory that could be buried by the wrong sort of safety; your own private ledger of guilt and care. You can feel the weight of those outcomes in your scuffed boots."
    "You inhale. You must choose how to lead."
    hide mayor_lynette_cole
    hide cassian_cass_romano
    hide jonah_reyes

    scene bg ch2_c4ca42_3 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
