label chapter7:

    # [Scene: Boardwalk | Late Afternoon — Festival Day]

    scene bg ch6_f99e88_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm acoustic guitar, gentle percussion; hopeful strings thread beneath]
    # play sound "sfx_placeholder"  # [Sound: Laughter, the slap of wet boots on wood, gull cries softened by distance]
    "You step onto the boardwalk and the town meets you like an old, familiar tide — neither quiet surrender nor frantic panic, but the steady, steady work of people returning what they can to the shore."
    "The air tastes of brine and grass. Underfoot the wood is sanded smooth by a hundred hands; your navy jacket is already flecked with mud and salt. You keep your compass in one pocket by feel"
    "— the brass is worn into a familiar press against your palm whenever you move."
    "Dr. Linh stands beneath a canvas awning, palms open as she explains eelgrass beds to a ring of children and retirees. Her words are clinical and tender at once; she gestures to trays of slim, green"
    "shoots, and the LEDs in the conservatory-mirrors catch in the damp glass like distant stars."
    show dr_linh_pham at left:
        zoom 0.7

    dr_linh_pham "Eelgrass spreads slowly, but it's a patient architecture. It calms waves, catches sediment, makes a home for small things. Plant it right, and it will do the heavy lifting for us."
    "Your hands ache to be useful — not just with policy sheets, not just with signatures — but with a spade and the raw, satisfying scrape of soil between your fingers. Volunteers work methodically along the"
    "living shoreline: folks from the co-op, teenagers from the high school, a handful of hands you recognize from the occupation. Their movements are messy and human, and that mess is what resilience looks like."
    "Maya darts up to you, cheeks flushed, her blue raincoat splattered with green. She thrusts a muddy tray toward you like an offering."
    show maya_marin at right:
        zoom 0.7

    maya_marin "Sis — you coming? You're on the honorary planter list. Elder Tomas saved you the best patch."
    "You watch her, the way she waits for permission then grins as if she already expects you'll say yes. Her hope is bright and impatient; it is a compass that points even when yours wavers."

    menu:
        "Take the tray and dig in":
            "You accept the tray, palms warm against wet plastic; the first shoot slips into soil under your fingers and some old, sharp guilt softens with the weight of work."
        "Kneel and show Maya how":
            "You kneel beside her, guiding her small hands; her laugh is immediate and magnetic, and for a moment your need to fix is translated into teaching."

    # --- merge ---
    "Continue the planting scene."
    "You choose — not decisively in words, but in the way your knees bend and your hands close around the tray. The neighbors around you murmur with approval; someone passes around hot tea in re-used cups."
    "The town's breath is communal, and you feel it move through you like wind in the marsh reeds."
    # [Scene: Festival Grounds — Raised Boardwalk | Mid-Afternoon]
    hide dr_linh_pham
    hide maya_marin

    scene bg ch6_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Voices overlap: a recorder plays a familiar folk melody; the distant metallic clank of a temporary crane being dismantled]
    # play music "music_placeholder"  # [Music: Light piano, swelling hopeful strings]
    "Elder Tomas sits on a low crate, his walking stick propped beside him. The crowd compacts around him as he opens a story like a well-thumbed book."
    show elder_tomas_quay at left:
        zoom 0.7

    elder_tomas_quay "There was a time the sea let us keep more than it took. Not because we owned the tide, but because our homes were built to listen. We forget that sometimes."
    "You listen. He tells the story of a small row of houses with red doors that used to stand where the raised boardwalks now run. He speaks in pauses and silences that let memory sit with"
    "you. Around you, people nod — some with tears in their eyes, some with the steady calm of someone who remembers and forgives and chooses to act."
    "Noah Vega arrives with measured steps, a tablet tucked under his arm like a placard of responsibility. When he sees you he hesitates — an unreadable expression passing over his features for a breath — then"
    "lifts his hand in a small, careful wave. The crowd parts politely; corporate cameras have long since been redirected into the good news of living-shoreline funding and tenant protections, and the camera crews now focus on"
    "planting rather than protest."
    show noah_vega at right:
        zoom 0.7

    noah_vega "Aria."
    "You meet him with the same restraint you used in negotiations — all practiced patience. You remember the memorandum you signed, the clauses that saved households, the lines where you traded immediate control for something larger. Your chest tightens and then loosens: the deal saved people you know."
    show aria_marin at center:
        zoom 0.7

    aria_marin "You came to see how it's working."

    noah_vega "I wanted to see the tenants' walkways. The raised blocks. I wanted — to see that when our numbers meet your people, it does something that neither could alone."

    aria_marin "It didn't happen without fights. And it won't be perfect."

    noah_vega "I don't ask for perfection. Just for... continued oversight. And to be held accountable where I failed to be before."
    "There's a pause between you that smells of salt and hard-won trust. The multi-tonality of his expression — contrition tangled with corporate pressure — is complex, and you choose to accept his sincerity for what it is: enough for now."

    noah_vega "I pushed for speed before I listened. I can see the cost. I'm trying, Aria. For the town, and... for my niece."
    "You tilt your head; he does not elaborate, and you do not press. The Schrödinger of his motives collapses into a human-scale compassion that carries weight."

    aria_marin "Then make good on it. Fund the upkeep. Make positions for local stewards. And keep the cultural block under community governance."

    noah_vega "Agreed. Contracts will reflect that. We misstepped. We won't again."
    "The exchange is terse but layered; it is policy and apology braided. Around you, the shop owners applaud as a new raised walkway is dedicated to community stewardship. Papers are signed later, of course; today requires hands in the mud more than ink on the page."

    menu:
        "Shake Noah's hand in front of the crowd":
            "You accept his hand; it's dry and firm. The cameras flash. You feel the crowd's relief more than your own."
        "Ask for a public commitment in elder Tomas' name":
            "You call Elder Tomas forward; his blessing makes the promise feel less corporate and more of a pledge to the town. Noah nods, visibly moved."

    # --- merge ---
    "Continue after the public exchange."
    # [Scene: Living Shorelines — Tidal Edge | Sunset]
    hide elder_tomas_quay
    hide noah_vega
    hide aria_marin

    scene bg ch6_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft, patient slap of small waves; the whisper of reeds; a child's delighted squeal when a small crab scuttles by]
    # play music "music_placeholder"  # [Music: Gentle cello and flute; warmth underpinning the scene]
    "Kai Solano stands a little apart from the planting line, arms folded, watching the children press roots into the sand with a fierce, private softness. When he catches your eye, his expression shifts — that familiar"
    "amber intensity untamed by distance. He walks over, soles of his shoes muffled by sand."
    show kai_solano at left:
        zoom 0.7

    kai_solano "You look like you haven't slept."
    show aria_marin at right:
        zoom 0.7

    aria_marin "You should see what 'haven't slept' looks like on the back end of a memorandum."

    kai_solano "Memorandums don't feel like this.' (He gestures at the planted eelgrass.) 'This — this is real."
    "Kai Solano's voice is threaded with something like apology. There's humility in the way his shoulders slope, and you can see the memory of the blockade and the nights of shouting, of banners and frost, all the ways you clashed."

    kai_solano "I moved too fast. I thought stopping their cranes meant we'd win everything. I forgot people have roofs and businesses and histories to hold."

    aria_marin "And I forgot, sometimes, to listen to the fury that gets things started. We both left out the town to some degree."

    kai_solano "So we learn? We plant together?"
    "You let the question hang like a buoy in a warm tide. He looks at you — really looks — and you see not only the activist fire but the boy who once dragged you out"
    "to seawalls to watch storm tides and to dream louder than scared. His hands are rough; when he lifts a handful of substrate to show you how to tamp the eelgrass, his fingers are careful."
    "You share a back-and-forth that is soft and unhurried — teasing guilt, defensiveness turned gentle, memory traded for a small, patient rebuilding."

    kai_solano "I misjudged your faith in process."

    aria_marin "And I misjudged your faith in urgency."

    kai_solano "Maybe both faiths were right in pieces. Maybe they needed to be in the same room."
    "You both laugh, a small release of air. Your hands, raw from digging, find the space to touch his palm in passing. It feels like contact with a warm instrument: familiar, resonant."

    menu:
        "Reach for his hand and hold it":
            "You take his fingers in yours. For a beat the sound of the sea is all that matters."
        "Press the back of his hand and step back to work":
            "You squeeze his hand in a quick, private pact and return to the row; the gesture is a promise more than a proclamation."

    # --- merge ---
    "Continue working alongside Kai."
    "Kai Solano kneels next to you and for a moment you work side-by-side in comfortable silence. The living shoreline between you and open water is a line of mutual work: neither of you leading, both following."
    # [Scene: Raised Boardwalk — Cultural Block | Dusk]
    hide kai_solano
    hide aria_marin

    scene bg ch6_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmured conversation, a child running past with sticky fingers, the distant rumble of a generator being switched off for the night]
    # play music "music_placeholder"  # [Music: Lush strings; an open, satisfied chord]
    "The festival winds down into a quieter comfort. People linger as if reluctant to finish a prayer. There is music — a local band plays a folk tune that feels like home — and Elder Tomas"
    "sits at the edge of the crowd, smiling, watching the town he loves breathe easier."

    "You wander the raised walkways with Kai Solano at your side. Vendors close up, helping one another haul supplies. In the window of a community bakery, someone pins a simple sign" "Owned by Salthaven — All Welcome."
    "Maya dances up to you and loops an arm through yours, paint flecking her sleeve."
    show maya_marin at left:
        zoom 0.7

    maya_marin "You did it. We did it."
    show aria_marin at right:
        zoom 0.7

    aria_marin "We did — a messy 'we' that includes too many hands to count."
    "You think of the row of houses Elder Tomas told about — the ones that were spared by the new surge, the ones that later that fall were hugged by the living shorelines in a real"
    "test. You replay the day the storm came: the low, hungry sky, the wind like a beast pushing on windows, and then the way the eelgrass held and the raised boardwalks channeled water away from porch"
    "steps."
    hide maya_marin
    hide aria_marin

    scene bg ch6_f99e88_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A storm's roar; water hitting barriers; the creak of raised walkways; the cry of victory as a house spared is cheered]
    # play music "music_placeholder"  # [Music: Crescendo into triumph — brass and strings]
    "When the storm roared a few months from now, it did not take what the town had fought to keep. A line of houses that, in another timeline, might have been swallowed were spared — water"
    "chased the living shoreline, slowed and softened, folded back into the sea instead of cutting through people's lives. You remember the moment you stood with your compass in hand, rain soaking through your jacket, your hands"
    "raw and bleeding a little from the cold and the spade. The compass felt like a tether then, not a chain — something that held you steady but did not bind you to guilt."
    "Kai Solano's hand finds yours, weathered and warm beneath the saltair. You do not make a show of it. He squeezes once, and you squeeze back. It is a quiet, private thing — less a dramatic reunion than an agreement to keep working, together."
    show elder_tomas_quay at left:
        zoom 0.7

    elder_tomas_quay "A round for the planters. A blessing for those who plant and those who remember how to tend."
    "Noah Vega stands a few paces away, watching the small protected cultural block. He meets your gaze and nods, a simple, clean motion. There are still awkwardnesses — contracts that will need watching, funds that must"
    "be maintained, futures that will require tending — but for tonight the town reclines into a cushion of relief."
    "Dr. Linh joins you, handing out thermoses of tea. She claps you both gently on the shoulder."
    show dr_linh_pham at right:
        zoom 0.7

    dr_linh_pham "Scientists can model a lot, Aria. But the real variable is whether people will plant the first shoot. You rallied them."
    "You smile, feeling something like release unfurl in your chest. Your perfectionism, relentless as it is, loosens its grip by small increments; seeing volunteers teaching children to plant eelgrass matters more than having every metric pefect on the first try. You let the town's imperfect work be enough."
    "Maya tugs at your sleeve, wide-eyed with a small, private joy."
    show maya_marin at center:
        zoom 0.7

    maya_marin "Promise me we'll keep this place. Promise me you'll never sell the mural."
    "You laugh and pull her close."
    hide elder_tomas_quay
    show aria_marin at left:
        zoom 0.7

    aria_marin "I promise. We'll keep the mural, the bakery, the songs — if we all agree to be stubborn about what matters."
    "Night settles like a soft blanket. Lanterns glow along the raised walkways; the smell of wet wood and frying dough fills the air. A child drops a clump of eelgrass and runs back to the water,"
    "thrilled. Someone starts a slow clap, then another joins, and soon the sound folds into a communal, grateful noise."
    hide dr_linh_pham
    show kai_solano at right:
        zoom 0.7

    kai_solano "Was there ever a moment you regretted staying?"
    "You think of the storm when you were a teen — the house lost, the seam of grief in the town — and of the many spreadsheets and conferences that followed, and of the countless small, stubborn acts that stitched the town back."

    aria_marin "Every day I regret the things I couldn't save. But I'm starting to forgive myself for the things I can't control. This — here — is why I stayed."

    kai_solano "Then stay. Let me help."
    "You let your fingers knit with his. The compass in your pocket is a small weight; tonight it feels like a lifeline. The silver ring on your left hand — thin and worn — is not"
    "a symbol of perfection, but of continuity. You rest your thumb on its edge, feeling both the ache and the comfort it contains."
    hide maya_marin
    hide aria_marin
    hide kai_solano

    scene bg ch6_f99e88_6 at full_bg
    # play music "music_placeholder"  # [Music: The music swells into a gentle finale of strings and soft chorus; hopeful warmth]
    "Elder Tomas rises and calls the crowd to a final blessing. Voices lift — some cracked with age, some bright with youth — and the melody is not pristine, but it is resolute. Around you, the"
    "town breathes as one. The living shoreline, the raised boardwalks, the small protected cultural block — none of it is perfect. But it is rooted. People have places to come back to. Children will learn to"
    "plant eelgrass the way Maya did today. The town's character persists in the hands that keep it."
    "You close your eyes for a second and let all of it sink in: the feel of mud under your nails, the warmth of tea seeping into your palms, the press of Kai's fingers. You think"
    "of the row of houses that the shorelines saved and of the small, persistent miracles that made that outcome possible."
    "You are tired in a way that belongs to honest labor. Your compass is cool and sure against your palm; your ring's silver is tempered by salt. Your hands hurt, a good hurt — the kind that says you were useful."
    "As the last lanterns are lit and the crowd begins to drift toward home, you stand on the raised boardwalk with Kai Solano by your side, Maya chattering at your elbow, Elder Tomas humming an old tune, and Dr. Linh already making plans for next season's plantings."
    "You let the moment sit: steady, hopeful, and raw."

    scene bg ch6_f99e88_7 at full_bg
    # play music "music_placeholder"  # [Music: Gentle resolution; a final warm chord fades into soft ambient sea sounds]
    "You realize, with a clarity that hums through your bones, that Salthaven was not saved by a single act or a single person. It was saved by the messy, stubborn combination of policy and protest, of"
    "science and song, of private apology and public accountability. Love — between you and Kai, between you and this place — is not dramatic now. It is steady. It is private. It is enough."
    "You let go of the impulse to fix everything at once. You let the town's collective, imperfect choice be the measure of success tonight."
    # [Scene: Boardwalk | Night — After Festival]

    scene bg ch6_f99e88_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant gull; the gentle rush of water; soft conversation trailing away]
    # play music "music_placeholder"  # [Music: Low, contented piano]
    "You breathe in the salt air, and it tastes like all the things you choose — the hard bargains, the offerings, the small mercies. Your compass is a tether, your ring a quiet claim. The town sleeps, for now, under the watch of living shorelines and human steadfastness."
    # play music "music_placeholder"  # [Music: Fade out to the sound of sea and a single, sustained cello note that resolves into silence]

    scene bg ch6_f99e88_9 at full_bg

    scene bg ch6_f99e88_10 at full_bg
    "THE END"
    # [GAME END]
    return
