label chapter4:

    # [Scene: Greenhouse Collective | Morning]

    scene bg ch4_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft drip of condensation, distant gulls, a tinny radio playing a hopeful folk tune]
    # play music "music_placeholder"  # [Music: Warm acoustic pick, gentle tempo]
    "You tug your knee-high rubber boots over denim and feel the familiar, forgiving give of wet rubber. The greenhouse smells like turned earth and salt—peaty, green, alive. Your weatherproof notebook is tucked under your arm; the"
    "brass compass at your throat is warm against your collarbone, a small, private compass within a town-sized problem."
    "Jonah Reyes is already there, knees bent between trays of spartina and eelgrass, mud under his nails like a promise. He looks up as you step into the humid, plant-scented hush—his smile is the steady kind you remember, easy and unhurried, the kind that fits the place."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "You made it. I was starting to think you’d trade us for city lights."

    "You" "I almost did. But the city doesn't have mornings like this."
    "Jonah Reyes: (grinning) 'Good—because we need hands. And because—' (he reaches into a pocket and produces a small paper seed packet) '—I figured you'd want first dibs. Spartina's delicate this season; it takes a patient hand.'"
    "He offers the seed packet to you. His rough palm is warm; a net-scarred certainty undercuts the casualness. When your fingers close around the packet, the gesture reads like a small treaty."
    "Internal thought: This is how reconciliation begins—not with grand speeches, but with seed paper and mud-streaked laughter. Trust, like marsh grass, is planted and tended."

    jonah_reyes "You okay? You look like you swallowed a tide chart."

    "You" "I am. I'm… present.' (You pause, admitting more to yourself than to him.) 'It feels right—helping here. Less like proving anything, more like fixing something that matters."
    "Jonah Reyes: (softly) 'That's all anyone's asked you to do. Not fix the past—just help the future be livable.'"
    "You watch him for a moment. He shifts, setting a Polaroid down on an overturned crate: a snapshot of a previous planting—your hair tipped sea-green, smudged with mud; Jonah Reyes's smile a smudge of amber dusk. The camera's paper is still drying at the edges."

    jonah_reyes "Think Bento'd approve of the knot I used to bind those burlap rolls?"
    "You laugh before you can stop it, something loose and genuine. The sound feels right in the greenhouse."

    menu:
        "Take the seed packet with both hands, silent, and tuck it into your notebook":
            "You cradle the packet as if it's a fragile promise. Jonah watches you for a beat, then nods—no words needed. The packet lives against the paper of your notebook, a quiet agreement between you and the work."
        "Tease Jonah back about the knot and ask for his worst planting dad-joke":
            "Jonah's grin widens into a full laugh; he obliges with a terrible sea-pun and then, mock-offended, pretends to storm off. The joke loosens the air; the two of you fall into the rhythm of shared work, elbow-to-elbow."

    # --- merge ---
    "The narrative continues."
    hide jonah_reyes

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Fingers scratching damp soil, whispered directions, the soft rustle of plastic tags]
    "You move through the rows with Jonah Reyes, hands learning the vocabulary of the plants—how many centimeters between roots, the right angle to press a shoot into the mesh that will cradle it when tides come. Each instruction is a small translation from science to craft."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "Push straight, not too deep. Think of it like threading a needle with the tide as your seamstress."

    "You" "Threading a needle with the tide—I'll file that under 'poetic engineering.'"
    "Jonah Reyes: (raising an eyebrow) 'You should write a manual. 'Mira Kestrel's Guide to Sea-Needle Sewing.''"

    "You" "Only if you write the foreword.' (He mock-sculpts the air as if composing.) 'Seriously—thank you. For pushing so many people to show up."

    jonah_reyes "I've been pushing a long time. It's different when you push with me.' (He pauses, then, quicker) 'Nobody expects miracles. We expect work."
    "The greenhouse door sighs open and a cool breath of harbor air slips in like a page turned. Dr. Lian Zhou steps through—boots spattered with mud, tablet in hand, salt in the seams of her hair."
    "She carries the polite gravity of someone who measures storms the way others measure coffee."
    "Dr. Lian Zhou: (warmly) 'Morning. I brought the sediment probe you asked for. And—' (she glances at your notebook) '—data to ground the grid.'"

    "You" "Perfect timing. We were just calibrating spacing."
    "Dr. Lian Zhou kneels, laying out a mesh of colored pins and a hand-drawn grid one of the volunteers made. She speaks softly but with the authority of numbers and experience."
    show dr_lian_zhou at right:
        zoom 0.7

    dr_lian_zhou "The sediment there is more organically rich than we thought. If we place the cordgrass in staggered clusters, they'll trap more silt in the first season. But the tidal window narrows—planting needs to be timed precisely with low tide plus an hour."
    "You: (leaning in) 'So—first low tide planting, then staggered follow-ups every two weeks?'"

    dr_lian_zhou "Yes. And we need to monitor salinity spikes after storm surges. I'll run a short survey after the first high tide next week."

    jonah_reyes "Sounds like a plan. Lian, are you promising to come muddy with us?"
    "Dr. Lian Zhou: (a small smile) 'I promised once. I don't break small promises.'"
    "Her laugh is dry, pragmatic, and it loosens the tension you didn't know you'd been carrying."
    # [Scene: Transition to Old Shipyard | Midday]
    hide jonah_reyes
    hide dr_lian_zhou

    scene bg ch4_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Hammer taps, murmur of volunteers, gull cries, distant dock hoist creak]
    # play music "music_placeholder"  # [Music: Rhythmic hand-drumming, building to an optimistic pulse]
    "The Old Shipyard smells of salt, oil, and turned wood. Volunteers gather in small knots—Kai Tan distributing flyers between planting shifts, elders carrying woven bags of sediment, teenagers wrestling with salvaged timber that will become the"
    "structural skeleton for planting platforms. Bento Morais stands at a central point, his voice low and modulated, taking a rhythm the crowd can follow."
    "Bento Morais: (chanting gently) 'Hold the line. Plant the mud. Let the marsh rise where old boats stood.' (He moves in time, each phrase a stitch.)"
    "You find yourself swept into it—the chant becomes a tool as much as a spell, a memory-thread anchoring the practical with the ritual. Bento tells the story of the first saltmarsh, of a tide that once"
    "took a dock and left a bar of birds, of the way a village learns its edges."
    show bento_old_bento_morais at left:
        zoom 0.7

    bento_old_bento_morais "We are not ending our stories. We are changing the pages. We plant, we teach, we remember the names of the nets we lose and the names we save."
    "Volunteer voices layer over his: practical questions, jokes, a child's high, windy laugh. The old and the new mingle; technology and story braid together."
    "Kai Tan: (bouncing on the balls of their feet, blue hair catching light) 'I've got signatures for the city record—people want to show up. And seed packets to hand out. We can run a youth crew on the second shift.'"

    "You" "Perfect. We'll need them for the lighter lifting—planting mats and tending the first clusters."
    "Jonah Reyes: (to Bento Morais) 'You sure you don't want to hold the drill?' (He grins; his hands are already inked with salt and intent.)"
    "Bento Morais: (mock affronted) 'Young man, I used to mend engines with nothing but a shoelace and a prayer. I will supervise and say wise things.'"
    "Laughter breaks; the task becomes a community choreography."

    "Dr. Lian Zhou arrives with a handheld sediment probe, working through results aloud so everyone can hear—salinity gradients, organic content estimates, expected accretion rates. She corrects a planting line gently, drawing a small arc in the sand" "Shift two meters inland here; the current eddy will deposit more silt than we expected."

    "You" "Good catch. That means fewer replacements later."
    show dr_lian_zhou at right:
        zoom 0.7

    dr_lian_zhou "That's the hope. The data is a promise with footnotes."
    "The work is tactile and immediate. Your hands get inked with dark silt; your jacket sleeve picks up a smear of algae. Each seed you plant is an anchor—small, stubborn, insistent."
    "Jonah Reyes takes a Polaroid and hands it to you before you can protest: a shot of your shoulder, hair tipped with sea-green, mud-smeared and purposeful. He frames you like an origin story."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "Keep that—so you remember what it looked like when it began."
    "You: (holding the photo) 'I already feel like I've been given more than I deserve.'"
    "Jonah Reyes: (softly) 'You deserve a town that doesn't wash away. You helped make it possible.'"
    "The afternoon stretches in efficient, companionable labor. Evelyn Sato arrives near the end of the second shift—practical smile, campaign scarf folded like a talisman. She moves through the site, hands touching tools, listening, the kind of presence that can sign permits and ease bureaucratic knots."
    hide bento_old_bento_morais
    show evelyn_sato at left:
        zoom 0.7

    evelyn_sato "The permit's ready. Small pilot—three plots, one year monitoring. I couldn't get the full funding yet, but—' (she hands you a stamped paper) '—this gets you to the waterline."
    "You take the permit. It is a small, legal thing and enormous at once—the kind of paper that changes trajectories."
    "You: (voice tight with something like gratitude) 'Thank you. That—this means everything.'"

    evelyn_sato "Just keep the town with you. That's how we'll win the bigger fights."

    dr_lian_zhou "We'll set up monitoring schedules. Bento's volunteers will keep daily logs; we'll feed data to the lab."

    "You" "I'll coordinate the household consultations. We need to make sure we respect property lines and livelihoods."
    "Kai Tan: (already scribbling) 'And I'll keep pushing for public outreach—flyers, local radio, school groups.'"
    "Bento's chant swells, everyone falling into a shared rhythm that makes practical things sacred. The old shipyard, which once smelled like rot and abandonment, feels like a burlap sack of new shifts—full and heavy with possible futures."

    menu:
        "Let Jonah take a Polaroid of you planting, and pose":
            "You lean into the motion, a small, defiant smile tugging at the corner of your mouth. Jonah clicks, the camera whirs; the paper blooms with you centered in mud and light. He hands it to you like an offering, and for a moment the past's sharp edges soften into grain."
        "Ask Jonah to take wide shots of the volunteers instead":
            "You point at the gathered crew and suggest a wider frame. Jonah steps back, capturing a sea of hands and faces. When he shows you the print later, you see yourself in the crowd—part of a larger, stubborn organism. It steadies you in a different way."

    # --- merge ---
    "The narrative continues."
    hide dr_lian_zhou
    hide jonah_reyes
    hide evelyn_sato

    scene bg ch4_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Page rustle, distant harbor, the steady thud of a mallet driven into salvaged timber]
    # play music "music_placeholder"  # [Music: The acoustic pick swells into a hopeful chorus]
    "Your notebook fills—tide windows, volunteer shifts, names of families who said they'd consider relocation of their gardens for the pilot plots, a checklist: watering schedule, sediment probes, contact Bento for oral histories, arrange youth shift. Each line is a small promise turned practical."
    "Internal thought: For the first time since I left, reconciliation doesn't feel like a single, explanatory conversation. It feels like a ledger of acts: show up, listen, plant, measure, repeat."
    "You look up. The harbor light is low and forgiving. Jonah Reyes calls out instructions for the evening team; Lian maps the first data upload in her tablet; Kai hands out seed packets like confetti. Evelyn's permit sits in your coat pocket, warm as a new coin."
    "You tuck the Polaroid into your notebook beside the seed packet Jonah Reyes gave you. The two papers—image and promise—press together like the two halves of something mending."
    "You breathe in. Salt, wood smoke, damp soil, and the soft perfume of hope. Hope rises like a planted shoot: slow, stubborn, insistently green."
    "A low bell from the boardwalk marks the tide schedule—an external metronome for the work ahead. The shipyard will become the staging ground tomorrow: noodles of salvaged timber cut and fastened, woven sediment bags stacked, planting"
    "mats ready. There will be weather to watch, schedules to knit, and people to coordinate."
    "You close your notebook and stand for a beat, palms inked and voice ready."
    "Internal thought: Everything we've done today points to tomorrow. The pilot will either be a seedling that roots or a lesson that makes us better. Either way, we move forward."

    scene bg ch4_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Single ascending chord, bright and expectant]
    "You feel a pulse—of readiness, of community, of small, careful hope. It hums under your ribs like a tide. The shipyard build looms like the next breath: necessary, tangible, terrifying in its promises."
    "Page-Turn Moment"
    "You lift your notebook, eyes tracing the checklist one more time. The harbor beyond the shipyard hushes into a low, patient murmur; gulls wheel like punctuation. There's a cadence to what you've started—an agreement stitched into"
    "the town's skin with burlap and data and song. It will demand everything you have and return new things in trade: trust, repair, and the slow architecture of shared lives."

    scene bg ch4_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Single ascending chord resolves]

    scene bg ch4_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
