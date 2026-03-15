label chapter4:

    # [Scene: Roooftop Garden & Night Market | Twilight]

    scene bg ch4_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Soft, steady acoustic rhythm; a low, hopeful bass undercurrent]
    # play sound "sfx_placeholder"  # [Sound: Distant chatter from the night market, a gull calling below the harbor, the clink of a wheelbarrow on concrete]
    "You push. Eli takes the other handle, and together you guide the wheelbarrow up the gentle slope of the reclaimed roof — marsh plugs snug in their trays like quiet promises. The air is warm against"
    "your forearms; the lights throw halos in the mist that rolls in from the bay. Your braid sweeps your shoulder, a line of dark against the amber glow."
    "Eli Navarro grins, hair pushed back, paint specks on his rolled linen sleeves. He lifts a tray with an easy, practiced motion and hands you a trowel without asking."
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "Two trays left after this. You want the ones with denser rhizomes, right?"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Yeah — denser, and the cordgrass plugs closest to the gull-spray. Asha's notes said root density matters for early anchoring."
    "(You voice the data like a vow — small, practical, not theatrical.)"
    hide eli_navarro
    hide maya_reyes

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft scrape of trowel on soil]
    "You plant the first plug. The mud gives and takes like a handshake. The rooftop smells of compost and fried fish from the stalls below, an odd comfort: food and fertility, the twin economies of this"
    "town. When you set the next tray, Eli fumbles with his weathered Polaroid, trying to angle it to catch the small prototype you built — a half-gabion, half-planter test that might anchor a stretch of frontage"
    "when scaled."
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "When you say Asha's notes like that, people will think you have an altar for field journals."
    "You let a laugh out that tastes of salt and nerves. Your fingers close around the trowel; the metal is cool. He watches you with a light that isn't quite romantic and isn't entirely professional either — it's patient and expectant, and it makes your chest work a little harder."
    "You plant the first plug. The mud gives and takes like a handshake. The rooftop smells of compost and fried fish from the stalls below, an odd comfort: food and fertility, the twin economies of this"
    "town. When you set the next tray, Eli fumbles with his weathered Polaroid, trying to angle it to catch the small prototype you built — a half-gabion, half-planter test that might anchor a stretch of frontage"
    "when scaled."

    eli_navarro "Hold still. This will look good in the portfolio."
    "(He squints, half-performing, half genuinely amused.)"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Portfolio, huh? We're activists, builders, and apparently models now."
    "He snaps the photo. The first wave of rooftop spray catches the lens; it fogs the image into a smear of light. You both burst out laughing — a small, bright thing that makes your shoulders drop a notch."

    menu:
        "Wipe the Polaroid with your sleeve":
            "You rub the fog from the instant with your sleeve and reveal a blur of light and grass. Eli teases you about your delicate approach."
        "Hand him a napkin from the stall below":
            "You point to a vendor and Eli ducks down to buy a napkin, returning with a paper square and a grin; the vendor waves, recognizing both of you."

    # --- merge ---
    "The group keeps working, photographs added to the documentation pile."
    "Neighbors arrive in small flows: a pair of kids dripping with sugar and sauce, Rosa carrying a thermos of coffee and a basket of sponges, Tomas with a paint-smudged cap and curiosity in his gait. Their"
    "footsteps make a softer percussion against the rooftop — a counter-rhythm to your own steady work. An elder you know by the cadence of her stories leans over the first gabion and traces the stones with"
    "a memory-heavy finger."
    show rosa_alvarez at center:
        zoom 0.7

    rosa_alvarez "If those hold, my café's back wall won't be the first thing to wash away next season."
    hide eli_navarro
    show tomas_reyes at left:
        zoom 0.7

    tomas_reyes "And my shop's awning might stay up long enough for me to fix it properly. Are those the ones you said to use near the edge, May?"

    maya_reyes "Yes. Near the edge where the spray is strongest but not where the runoff channels. We want the plants to take, not drown."
    "(You sketch the line in your field notebook, the compass looped against the paper like a talisman.)"
    hide maya_reyes
    hide rosa_alvarez
    hide tomas_reyes

    scene bg ch4_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Pencil on paper, someone in the market calling out the night's special]
    "You and Eli kneel side by side, measuring spacing with his folding ruler and your brass compass. The conversation tilts between the technical and the personal without a seam — seed spacing, root depth, how Tomas's"
    "son fell through a pier plank last winter. Each detail is a stitch. Each stitch is a reason to keep going."
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "If we orient the planters this way, the gabions will slow the surge before it reaches the parapet. Then cordgrass can do the rest."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Right. We test for shear — not just inundation. If we can show reduced edge erosion on the model here, we can push for the pilot at the harborhead."

    eli_navarro "And if Marco sees numbers and neighbors show up on a Saturday with gloves, it's a lot harder for June to say no."
    "You pause — the possibility sits there, workable and not guaranteed. Your chest tightens in a familiar pattern: hope braided with caution. You remember Asha's voice explaining root mats and tidal rhythms. You imagine Tomas's small repair shop, his list of customers like little anchors on a page."

    menu:
        "Ask Tomas to demo his anchor technique":
            "Tomas crouches beside you and demonstrates how he ties the lower mesh to a rebar anchor — a practical choreography he's perfected. Your confidence builds."
        "Stick to the test protocol":
            "You remind the group about the controlled variables; Tomas nods and helps within the parameters. The model remains clean and defensible for later presentation."

    # --- merge ---
    "The team adjusts; either way, documentation continues and the prototype holds."
    "Time passes in practical increments: plant, tamp, photograph, note. The market's hum below swells and fades as sellers call numbers, and civic music floats up in a pattern you've come to associate with community evenings. The rooftop feels like a small, sanctified lab that smells of sea-salt and frying garlic."
    "Your touch brushes Eli's as you exchange a trowel. It's quick — a flash of skin against skin — but it sends an electric skitter through you. You don't let it lengthen. You have priorities: data,"
    "neighbors, survival. There is a ledger in your head with columns for science and for feeling, and right now the numbers take precedence. Still, the warmth lingers."

    eli_navarro "You're tense tonight. You okay?"

    maya_reyes "Just thinking about logistics. The permit timelines — and Tomas's rent. Nothing personal."

    eli_navarro "Okay. But we're doing this together, right? If things get heavy, you can drop me a signal."

    maya_reyes "I know. And I will."
    hide eli_navarro
    hide maya_reyes

    scene bg ch4_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low murmur of machines; in the distance, a mechanical siren throatily tests]
    "As the sky cools to indigo, you look up and see them: work lights skittering across the construction site at Aurelia's stretch. A cluster of silhouetted figures moves with efficient geometry. The seawall's sheet piles glitter"
    "like teeth. It's not immediate danger — not yet — but it is there, a reminder that the other plan is not idle."
    "Your pulse nudges higher, a steady beat that matches the mid-tempo music. The arrival of June Park's crew is not a personal affront in this moment; it's a horizon-line reality: two futures being laid down at"
    "once. The rooftop's warmth pushes back against it — people's hands in the soil, the laughter of children, the quick trades of knowledge. For the first time in weeks, momentum has weight behind it."
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "They build fast. But we plant roots slow. They forget the slow parts until the tide teaches them."
    show tomas_reyes at right:
        zoom 0.7

    tomas_reyes "They've got machines. We’ve got neighbors."
    "You close your notebook, tracing the last map with a finger. The ragged edges of your plans seem less fragile with every person who picks up a trowel. You can imagine this prototype, scaled along the"
    "shoreline: gabions and tidal planters staggered with native cordgrass, neighbors trained and paid for maintenance, a demonstrable reduction in edge erosion in a season."
    "Eli Navarro stands and brushes soil from his palms, then looks toward the harbor where June Park's floodlights mark the concrete ambition of Aurelia's project. He meets your eyes with a look that asks for a pact without naming it."
    show eli_navarro at center:
        zoom 0.7

    eli_navarro "We document everything tonight. Photos, measurements, who's out here. Marco needs to see this, not just hear about it."
    hide rosa_alvarez
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "Agreed. We make it stupidly obvious—data and people. If we show the town what hands-on resilience looks like, it becomes something they can point to."

    eli_navarro "And maybe a good Polaroid won't fog this time."
    "You laugh. The tension eases back into work: planting, marking, measuring, photographing. The rooftop hums with the steady mid-tempo energy of people doing the practical thing. The moment is not triumphant — not yet — but it's not small anymore."
    hide tomas_reyes
    hide eli_navarro
    hide maya_reyes

    scene bg ch4_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: The acoustic rhythm holds; a soft swell signals a page-turn moment]
    "You trace the horizon with your eyes. June Park's crew across the harbor is a silhouette; your rooftop is a living map of intent. The crowd picks up another tray. A child asks where the plants"
    "go. You point, and in doing so point to a future that is possible if enough hands keep planting."
    "You feel momentum move through the group like a current. It is steady, full of human weight, neither euphoric nor despairing — simply mobilized."
    "You breathe in, the salt and smoke and garlic filling your lungs, and for a beat you let yourself believe that doing the small, honest work might be the fulcrum the town needs."

    scene bg ch4_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade to a soft, expectant single chord]

    scene bg ch4_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
