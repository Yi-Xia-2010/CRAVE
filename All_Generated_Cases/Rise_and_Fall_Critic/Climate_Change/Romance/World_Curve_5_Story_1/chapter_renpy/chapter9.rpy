label chapter9:

    # [Scene: Mira Kestrel's Childhood Porch | Night]

    scene bg ch9_3be532_1 at full_bg
    # play music "music_placeholder"  # [Music: Quiet piano with a single, uplifted violin line — gentle, steady.]
    # play sound "sfx_placeholder"  # [Sound: Low surf, the distant slap of a boat hull, whispered conversation and the occasional call of a gull muffled by fog.]
    "You stand with your palm flat against the sun-bleached eave, feeling the grain where your hand once learned each notch and nick. The wood is cool, splinter-soft at the edges; the smell of dried salt and"
    "lemon oil—your mother's polish—rises faint and familiar. Your tidewatcher pendant rests against your sternum, a small pulse of brass anchoring you in this house and in the decision you helped make."
    "You would have kept this place if the sea had agreed. You would have stayed up nights re-mortaring the foundation, patching the gutters, and teaching Nadia how to plant the orchard so the mounds could root"
    "another season. Instead, the list includes this porch, this creaky stair, the map of your childhood stitched into every threshold."
    "You trace the eave like an apology, like a benediction. Your fingers remember the shape of summers, the small scars made by rope swings and the time Ruben rescued your kitten from the storm gutter. Memory"
    "arrives as a physical thing—weight in your chest, salt in the air—until the sorrow settles into something else: a steadier resolve that feels like carrying a lantern."

    scene bg ch9_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A soft scrape as footsteps approach from inside the house.]
    show cassian_rhys at left:
        zoom 0.7

    cassian_rhys "You always find the bits the rest of us miss."
    "(He stands in the doorway, coat damp at the shoulders, eyes like warm coals in the lamplight.) 'You could read the town's tide lines with your eyes closed.'"
    "You turn. His hand finds yours under the eave, small and callused from rope and paint. He doesn't pull; instead he lets his thumb rest in the hollow of your wrist, where your tidewatcher sits."
    "You don't answer right away. Instead, you let the moment hold: the wood under your palm, the quiet agreement in his grip, the tacit tally of what you've chosen to save and who will have to go."

    cassian_rhys "Nadia's been helping pack schoolbooks into sealable bags."
    "(He says after a beat.) 'She's insistent you keep the jar of marigolds. Said it's 'for luck.''"
    "You let out a breath that tastes like peat and something like forgiveness."
    "You think of the marigolds on the sill, how their petals used to be small suns in the winter window. You imagine Nadia's stubborn grin, the way she tangles in your sleeves and refuses to call moving 'leaving' — she says it's a 'new planting.' It helps, the nomenclature."

    menu:
        "Pick up the jar of marigolds and tuck it into your jacket":
            "You lift the jar carefully, the glass cool and the soil compacted into a promise. The petals brush your palm; they smell oddly of lemon and dust. You tuck them into your jacket so the scent is the last thing you carry from this room."
        "Leave the jar on the sill and take only the field notebook":
            "You close your hand around the field notebook—the leather warm, corners rounded by years of use. You press your thumb into the cover until the embossing leaves a faint dent, and let the marigolds stay where they bloom, a small, square memory in this window."

    # --- merge ---
    "Cassian watches you choose with steady, unfussy attention. When you make your selection, he nods as if the world has shifted a fraction and found its balance."

    cassian_rhys "Look at us arguing over flora like it's the apocalypse and not the town council."
    "(He tries for a laugh; it comes out as a soft exhale.) 'But you're right. We take what keeps us useful.'"
    "You share a look thick with history—childhood dares, afternoons repainting slogan banners, the time he braided his own hair with fishing twine and promised never to leave. You both know promises are brittle things and also the art of survival."
    hide cassian_rhys

    scene bg ch9_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A boat horn far off. The tide moves with a patient, inevitable rhythm.]
    show ruben_ortega at left:
        zoom 0.7

    ruben_ortega "Mira! Cassian! Last ferry's almost out — the folks at the orchard are starting the torching."
    "You feel it then: a small pulse of ceremony moving through the town. Farewells are not silent exits here; they are shared labor, a ritual of carrying seed and story to higher ground."
    # [Scene: The Drowned Orchard | Dusk into Evening]
    hide ruben_ortega

    scene bg ch9_3be532_4 at full_bg
    # play music "music_placeholder"  # [Music: A low, rising chorus of strings merges with a soft percussion — hopeful, communal.]
    # play sound "sfx_placeholder"  # [Sound: Wooden oars dipping, distant voices singing an old harvest song, laughter threaded with sobs.]
    "You stand at the head of a small, steady boat, Asha and Nadia in the bow, Cassian Rhys shoulder-to-shoulder with you. Each neighbor carries a pot: saplings, basil, a stubborn heirloom apple tree. The soil clings to hands and trousers; sap and salt smell like a memory compounded."
    show mayor_lin_park at left:
        zoom 0.7

    mayor_lin_park "This is how a town holds on to its stories."
    "(She says, watching the procession.) 'Not by walling the sea out, but by moving what matters safely — and keeping the rest so we can plant again.'"
    "Jonah Hale arrives at the dock to watch the boats leave. He's clipped into a rainproof blazer, but his face is softer tonight—less the engineer's austerity, more the man who understands leverage can be mercy."
    show jonah_hale at right:
        zoom 0.7

    jonah_hale "We retired the outer cofferdam."
    "(He says, the words deliberate.) 'We'll scale back the concrete footprint and extend the living margins—opposite of my original spec, but the sensors and Asha's models show us where hybrid buttressing keeps core infrastructure safe while wetlands buffer surge.'"
    "You feel that line—'retire'—settle into your chest like a stone turned to place a foundation. It is not total victory; it's a concession, an amalgam of practical and humane."

    "Asha (wiping mud from her palms)" "It buys time and space to grow the marshes thicker."
    "(She adds.) 'And the job training funds are approved. Twenty local hires on restoration this season, more after that.'"

    menu:
        "Hand your jar of marigolds to Nadia for the boat":
            "Nadia takes the jar with a fierce grin, claps it to her chest like a talisman. Her small fingers are already dirty and sure. She gleans the top soil with one thumb and offers it to the sapling she will plant—an act of passing on luck and work in the same breath."
        "Plant a sapling yourself on the higher ground before the ferry departs":
            "You step onto the higher ground first, knees stiff from the climb, and tuck the sapling into a prepared mound. Your hands are methodical; each press of soil is an oath. You stand back, palms cupped, and breathe as if the planting were a litany for what remains."

    # --- merge ---
    "Neighbors call out small jokes to keep the mood buoyant—Ruben grumbling about city ordinances even as he ties a sapling to a stake; Jonah Hale clapping an old fisherman on the back; someone passing around hot"
    "tea. The grief is stitched into the work. Laughter and tears fold into each other like the tides."
    "You watch the boats ferry the pots away, each plant a micro-migration. You think of the orchard trunks leaning like old sailors and the bioluminescent algae that once made summer nights look like a scatter of"
    "stars at your feet. Tonight, lanterns knitted into the walkways feel less like an elegy and more like a promise: this town knows how to move with the sea and still keep its stories alive."
    # [Scene: Boardwalk | Early Morning — Mayor's Signing]
    hide mayor_lin_park
    hide jonah_hale

    scene bg ch9_3be532_5 at full_bg
    # play music "music_placeholder"  # [Music: Brass undertones with rising strings — formal but warm.]
    # play sound "sfx_placeholder"  # [Sound: Camera shutters, quiet applause, the slap of wet banners in a cooling breeze.]
    show mayor_lin_park at left:
        zoom 0.7

    mayor_lin_park "This clause guarantees protections for the town core, community land trusts for those who wish to remain, and guaranteed funding for the restoration jobs."
    "(She looks at you and then out over the crowd.) 'We will provide housing stipends and prioritize local hires for the marshwork.'"
    "You can almost feel the clause unspool in the air, a legal net woven with political will. The handwriting is ink and more: it is a contract between neighbors, between generations."

    "Ruben (from the crowd, voice raw with age and salt)" "Protect the school. Protect the pantry. Keep a berth for those who can't—won't—leave."
    "Mayor Lin Park meets Ruben's gaze and nods. It is small, but it carries a great deal of weight."
    "You think of the children in the schoolyard, Nadia among them with knees scabbed and hair tucked behind her ear. You think of the pantry where neighbors barter stew and stories. The clause feels less like"
    "a triumph and more like a hand offered to steady the whole town as it steps from uncertainty into a deliberate direction."
    show asha_mehta at right:
        zoom 0.7

    asha_mehta "We have baseline data to monitor adaptive performance."
    "(She says softly, almost to you.) 'If the hybrid margins show faster erosion than predicted, we have escalation protocols that rely on community oversight, not just contractors. It's still messy, but it's accountable.'"
    "You let out a breath that tastes like salt and something else—relief, careful and bright."
    # [Scene: Tidelab Greenhouse | Afternoon]
    hide mayor_lin_park
    hide asha_mehta

    scene bg ch9_3be532_6 at full_bg
    # play music "music_placeholder"  # [Music: A hopeful, steady acoustic guitar riff under soft synths — industrious and warm.]
    # play sound "sfx_placeholder"  # [Sound: The hum of pumps, the rustle of plant leaves, voices coordinating in efficient harmony.]
    "You stand before a small group of trainees—some old fishermen, a few high school graduates, neighbors who have never planted anything beyond their window box. You outline a module on sediment trapping, then demonstrate how to anchor live fascines and weave stakes for new hummocks."

    "Nadia (eager, hands muddy)" "I want to be in the estuary crew."
    "(She says, eyes bright with a practical hope.) 'I can learn to measure salinity. I can carry the nets.'"
    "You smile because the list of what you can give has shifted from abstract to concrete: training hours logged, stipends distributed, a community land trust operational by season's end. The numbers are not magic, but they are pragmatic shelter for a town learning to reconfigure itself."

    menu:
        "Stay to coach the trainees on rope‑weaving techniques":
            "You knot a practice fascine with them, fingers working the wet twine in a motion that feels like prayer and carpentry. Each loop tightens the group; each successful knot is a quiet celebration."
        "Step back and let Asha lead the technical briefing while you handle volunteer coordination":
            "You move through the greenhouse, handing out gloves, signing people up for shifts, matching skills to tasks. You find satisfaction in the small logistic wins—schedules set, rides arranged, a kid promised mentorship."

    # --- merge ---
    "Cassian Rhys catches your eye across the room, and his smile is simple approval. He knows which of you will handle what in the days to come: your head for systems, his for people and morale."
    show cassian_rhys at left:
        zoom 0.7

    cassian_rhys "You're better with the canvas of plans. I'll be the loudspeaker."
    "(He drums a little rhythm on the hood of a crate.) 'Between the two of us, the murals and the marsh will both get painted.'"
    "You laugh softly. The thought of him leading a crew of neighborhood kids with a harmonica tucked into his cheek is unexpectedly endearing. It feels possible—enough of a life to count on."
    # [Scene: Boardwalk / Dusk — Knitted Lantern Vigil]
    hide cassian_rhys

    scene bg ch9_3be532_7 at full_bg
    # play music "music_placeholder"  # [Music: Warm cello and a gentle choir of voices singing a rebuilding hymn; the melody floats upward.]
    # play sound "sfx_placeholder"  # [Sound: The soft slap of waves, the murmur of community voices, the distant clink of tools.]
    "The town gathers. Some faces are tight with grief; others are open with a hopeful stubbornness. Boats return, saplings in place on higher ground. Jonah Hale stands by the mural, watching as Cassian Rhys and a group of teenagers splash color across a panel that will commemorate the lost blocks."
    "Ruben sidles up next to you; his cane taps softly on the boards."
    show ruben_ortega at left:
        zoom 0.7

    ruben_ortega "You did right by them,' he says without fanfare. 'It's never clean, Mira Kestrel. But you chose a thing that keeps people together."
    "His words settle not as absolution but as a shield against the worst of your guilt. You remember the failed pilot three seasons ago—the mud, the erosion, the quiet months after—and how it taught you to"
    "weigh human cost against ecological models. You learned that mercy is not always a single act; sometimes it's a program you have to maintain for years."
    "Nadia runs to you with a knitted lantern, cheeks flushed from the work. She thrusts the lantern into your hands as if presenting a trophy."
    show nadia_kestrel at right:
        zoom 0.7

    nadia_kestrel "For luck,' she says, grinning. 'And so you remember the courtyard."
    "You wrap an arm around her shoulder, and Cassian Rhys slides close on the other side, his presence like a steady weight."
    show cassian_rhys at center:
        zoom 0.7

    cassian_rhys "Promise me something?"
    "(He asks, low and intentioned.)"
    "You look at him—at the small crease of his brow, the way his mouth sets when he means it. You understand the languages of promises now: the bureaucratic vows to keep, the personal ones to stay. Both are necessary."

    cassian_rhys "Promise we'll keep building — murals, marshes, jobs, all of it. That whatever we lose will be honored. That we won't let the people who moved become ghosts in somebody else's ledger."
    "You squeeze his hand; it is an exchange more binding than the ink of any clause."
    "You think, 'I promise,' and the thought is not a whisper but a plan: training schedules, mural designs, a rota for pantry shifts, a rotating memorial for those we cannot save in place. Promise becomes policy, and policy becomes a practice of love."
    hide ruben_ortega
    hide nadia_kestrel
    hide cassian_rhys

    scene bg ch9_3be532_8 at full_bg
    "You feel the air thicken with something you recognize as ascent: people who have chosen to keep the town's bones and to make those bones new. The choice you helped make has a cost, but its"
    "contour is lit by hands and tools and the thousand small agreements that stitch a community together."
    # play music "music_placeholder"  # [Music: The strings resolve into a gentle, hopeful crescendo.]
    # play sound "sfx_placeholder"  # [Sound: The tide emits a long, consenting sigh.]
    "You look at the mural—unfinished, vivid—and then at Cassian Rhys. His eyes flick to yours and then to the horizon."
    show cassian_rhys at left:
        zoom 0.7

    cassian_rhys "We'll make this remember them."
    "(He says simply.) 'Not because we lost places, but because we kept people.'"
    "You lean into him. The touch is not a denial of what was asked; it is an affirmation of what you will do with the space that remains."
    hide cassian_rhys

    scene bg ch9_3be532_9 at full_bg
    # play music "music_placeholder"  # [Music: The violin plays a small, bright arpeggio.]
    # play sound "sfx_placeholder"  # [Sound: Laughter rising, mingled with a few quiet sobs that are held like breath.]
    "You stand on the boardwalk until the lanterns sting the dark into something less empty. The town hums around you—rebuilding, training, planting. It is not whole. It is repaired into something new: more adaptive, more locally rooted, and, importantly, more owned by the people who live here."
    # [Scene: Porch | Night — Final Moment]

    scene bg ch9_3be532_10 at full_bg
    # play music "music_placeholder"  # [Music: A delicate piano theme returns, warming into a steady, hopeful chord.]
    # play sound "sfx_placeholder"  # [Sound: Crickets, a distant harmonica playing a familiar tune, the hush of neighbors settling for the night.]
    "Cassian Rhys squeezes your hand one more time."
    show cassian_rhys at left:
        zoom 0.7

    cassian_rhys "You were brave today."
    "(He says, voice small.)"
    "The word lands oddly; bravery is usually loud in your mind, a series of decisive actions, but tonight it feels quieter: a long line of small refusals to let panic make the plan. You think of"
    "the families who accepted stipends and work, of the kids who learned to weave fascines, of the mural that will keep names and places in color. It is a set of daily bravery."
    "You and Cassian Rhys stand a little while longer in companionable silence. The porch light is a private sun. You let your palm rest on the eave again, not as apology this time, but as pledge."
    "You tell him without speaking, 'We will rebuild with what remains,' and the sentence lives between you both like a vow."

    cassian_rhys "And we'll keep them."
    "(He says—meaning the people, the stories, the school, the pantry, the murals.) 'We'll keep everything that makes Lowry Bay a home.'"
    "You nod. The weight in your chest shifts from guilt to a kind of workable responsibility. There are nights you'll wake rattled by what you've asked others to do; there will be days when you measure"
    "sediment levels and wonder if it was enough. But the climb has been made together, and that steadying matters more than you expected."
    hide cassian_rhys

    scene bg ch9_3be532_11 at full_bg
    # play music "music_placeholder"  # [Music: The piano resolves into a single, sustaining chord that lingers.]
    # play sound "sfx_placeholder"  # [Sound: The soft rustle of fabric, the distant rhythmic croon of the waves.]
    "You step into the dark and the lantern-lit path toward the higher ground where the community now gathers to plant and teach and paint. Love and loss are braided together, but the braid is strong. The"
    "town is not what it was, but it endures, reconstructed by hands that promise to stay."

    scene bg ch9_3be532_12 at full_bg
    # play music "music_placeholder"  # [Music: Crescendo into a warm, ascending motif; the sound settles into a sustained, hopeful resonance.]
    # play sound "sfx_placeholder"  # [Sound: The night breathes with communal life; a harmonica plays the last soft note.]
    "You carry the hollow echo of guilt, but it is smaller now—filled with plans, training rosters, community land deeds, and the steady rhythm of work. You have chosen a path that keeps most of the town"
    "whole and gave many a chance to stay. That is not a clean victory, but it is a real one."

    scene bg ch9_3be532_13 at full_bg
    # play music "music_placeholder"  # [Music: Fade out on a single violin line, warm and persistent.]

    scene bg ch9_3be532_14 at full_bg
    "THE END"
    # [GAME END]
    return
