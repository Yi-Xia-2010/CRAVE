label chapter2:

    # [Scene: Harborfront Lane | Late Morning → Dusk]

    scene bg ch2_c4ca42_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low hum of a projector, gulls circling, murmurs that swell like incoming tide]
    # play music "music_placeholder"  # [Music: Sparse cello, a steady minor pulse underscoring tension]
    "You arrive with the salt still in your hair and the notebook warmed against your chest. The bronze pendant at your throat is a small, private weight; you feel it twice today—once as memory, once as"
    "a talisman against doubt. Harborfront smells of smoked fish, wet rope, and diesel from the rigs beyond the mouth. The crowd is already larger than you expected: hands callused, scarves damp, a child clutching a petition"
    "like a talisman."

    scene bg ch2_c4ca42_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Tap of keys, the soft whir of a speaker, a polite cough becoming a tide of voices]
    "Aquila’s model sits on a portable plinth under a white sheet—too glossy to be honest. Cass Adler stands at the microphone already, charcoal suit catching the bulbs, posture precise. Their voice comes out smooth, practiced, the"
    "kind of thing that fills a room before anyone has decided whether to believe it."
    show cass_adler at left:
        zoom 0.7

    cass_adler "Thank you for coming. What we're proposing is not just protection—it's economic revitalization. Floodwalls, elevated promenades, new job centers. We can offer work, stability, and measurable reduction in risk. Our simulations show—"
    "You watch them as much as you listen. Old familiarity shapes the way you note the micro-expressions: a tightness at the corner of their mouth when they move from data to vision, a flash—just once—of something"
    "like regret that they quickly smooth over. The projector throws a shimmering cross-section of the coastline, neat colors and confident lines. When the model's lights flicker over the boardwalk in the render, someone laughs out of"
    "nervousness."
    "Mayor Jonah steps forward between Cass and the audience, hands open in the conciliatory gesture he's practiced at every podium this winter."
    show mayor_jonah_cruz at right:
        zoom 0.7

    mayor_jonah_cruz "We need solutions that protect people and jobs. No knee-jerk rejections. Let's hear all proposals and proceed carefully."
    "The voice around you splits into a chorus: agreement edged with fear. Ivy and Rosa move through the crowd like currents. Ivy's sleeves are rolled, flyers jutting from a pocket—her energy is an insistence; Rosa, cheeks"
    "flushed, holds a stack of signatures that tremble when she passes them to the clerk."
    show ivy_okoye at center:
        zoom 0.7

    ivy_okoye "We collected three hundred signatures this morning. People want their voices on the table, Maya."
    "You fold that into the cavern of your chest—proof that the town can still be heard. But your private doubt threads the moment like a hairline crack. The forecast you misread still lives in the sound"
    "of a gull at low light; you feel it when you breathe. You set your jaw and let the science steady your fingers."

    menu:
        "Open with hard data — charts and tide series":
            "You flip your notebook open to the carefully annotated tide series, voice clear as you lay out numbers and confidence intervals."
        "Start with the town — stories and images":
            "You tuck the notebook away and begin with Rosa's story of the oyster racks, speaking to faces instead of graphs. The room leans in differently."

    # --- merge ---
    "Both outcomes converge: you stand and take the lectern, the projector humming as a laptop throws a pale rectangle on your hands."
    hide cass_adler
    show maya_rios at left:
        zoom 0.7

    maya_rios "Good afternoon. I'm not here to promise easy answers. I want to show what the marsh already does for us—and what we can do to help it keep doing that work."
    "You run through the living shoreline measures: cordgrass restorations, oyster reef scaffolds, and phased, community-led elevation efforts. Your voice is quieter than Cass's, but steadier; you can feel the data behind each sentence like planks underfoot."
    "When you describe success rates and recovery timelines, some of the room relaxes—old fishermen nodding at measures that mirror what their parents once did."
    "Cass Adler returns to the mic before you can finish, not with anger but with calibrated sympathy."
    hide mayor_jonah_cruz
    show cass_adler at right:
        zoom 0.7

    cass_adler "Maya, your work is vital. Living shorelines are part of the toolkit. But our models show that alone, they won't keep the most vulnerable parts of town dry during extreme events. We must combine them with engineered defenses."
    "They sound reasonable. The word 'combine' has a backstage meaning—control, scale, capital—and you sense it in the way people in the front rows shift their weight."

    maya_rios "Combine is the exact place where we must be cautious. When 'combine' becomes 'replace'—when the marsh becomes an aesthetic under a seawall—that's not protection. It's erasure."

    cass_adler "I don't want to erase the town, Maya. I want to protect it. The jobs I'm proposing are concrete: construction, maintenance, long-term employment. For many families—"
    "Ivy bursts forward, voice bright and sharp like flint."

    ivy_okoye "With who in charge? Aquila's not proposing a community trust. They'll hand the contracts to firms out of state. Where's the guarantee locals get training and ownership?"
    hide ivy_okoye
    show mayor_jonah_cruz at center:
        zoom 0.7

    mayor_jonah_cruz "We can negotiate job provisions—"
    "A roar starts low in the crowd, growing as older faces register the economic promise Cass holds up like a lit coin. The room glitters with hope and suspicion in equal measure. You notice a man"
    "near the back clenching his jaw; his hands are silvery from salt, his nails caked with oyster mud. He watches the model as if it were a rival at a card game."
    "Eli Navarro steps into your periphery like a steady tide. He has mud on his boots and a rain-worn cap; when he speaks, the room trims itself to hear."
    hide maya_rios
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "You're talking about floodwalls on our beachline. What about the oyster beds? We lose those, we lose livelihoods that won't come back in a decade. You put concrete in the water and you don't just stop tides—you stop life."
    "His voice carries more than fear; there's accusation threaded with the ache of someone who has already lost a man to a storm. You meet his eyes—warm hazel cutting through the bluish glow of laptop screens—and you feel the small boat of your argument toss."
    hide cass_adler
    show maya_rios at right:
        zoom 0.7

    maya_rios "We're not advocating for wholesale walls, Eli. We're proposing targeted restorations that work with marsh processes. There are hybrid designs—"

    eli_navarro "Hybrid in theory. In practice, last I checked, 'targeted' still meant someone with money drawing lines where our beds used to be."
    hide mayor_jonah_cruz
    show cass_adler at center:
        zoom 0.7

    cass_adler "Eli, our design can include managed oyster exchanges, relocation assistance. We're not blind to livelihoods."

    eli_navarro "Assistance doesn't mean the same thing as ownership."
    "The exchange stutters into an argument made of hard truths. The Mayor raises a hand, trying to smooth the rips, but the fabric of the room is already pulled."

    menu:
        "Acknowledge the fear, lean into compromise language":
            "You say, soft but firm, 'I hear you. Ownership matters. Let's make that non-negotiable—community ownership must be part of any contract.' The crowd shifts; some skepticism softens."
        "Push the science hard — stress risks of delay":
            "You tighten your voice and detail the model projections for twelve- and twenty-year horizons. The data lands like a cold wave; a few people recoil, but others look at you as though you're cutting through fog."

    # --- merge ---
    "Both outcomes reconverge into the continuing discussion and planning; the room responds in complex chords—some relief, some new worry."
    "You choose, because there is no safe middle between truth and people's livelihoods. The room responds in complex chords—some relief, some new worry. You find Rosa near the front, fingers white on the petition stack. Her face is small and fierce."
    hide eli_navarro
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "If we do this, how do kids keep fishing? How do we teach them what we were taught? We can't lose that."

    maya_rios "Then we build that into the plan. Training programs, apprenticeships—"
    "Cass Adler interjects, eyebrows lifted, the politeness of someone used to shaping policy on slides."

    cass_adler "We can partner with local unions, provide startup grants. But we can't ignore the structural threats—the models show escarpment retreat in certain neighborhoods. Time is not on one side or the other."
    hide maya_rios
    show mayor_jonah_cruz at right:
        zoom 0.7

    mayor_jonah_cruz "This council can't afford to be paralyzed. We need a path forward that considers both hardship and safety."
    "The remainder of the meeting fragments into smaller clusters: heated whispers, practical questions, and raw doubts. People press into corners, exchange stories of roofs ripped off and stories of children who learned to watch the tide."
    "Your throat tightens; you listen to these histories as if stitching them into a map of what the town is—fragile, stubborn, human."
    "When the vote is called, it's small and procedural: to hold a formal hearing to listen to Aquila's plan in full. But votes are not abstractions when each hand cast carries years of memory and the weight of someone's rent, food, and future."

    mayor_jonah_cruz "All in favor of proceeding to a formal hearing—raise your hands."
    # play sound "sfx_placeholder"  # [Sound: Hands rise; small creaks as chairs shift; a thump you feel more than hear]
    "The votes split with a painful closeness. Eyes meet across the room: some warm with relief, some shuttered with new fear. The clerk records the vote; the decision is procedural, but for you, it feels like a hinge. The crowd dissipates into salt-streaked night, clusters breaking into hushes."
    "You walk out beneath the sagging bulbs. The model under its sheet sits like a promise that might be a threat. Cass lingers by the plinth, the projected map painting their face in cold lines."

    cass_adler "We can do this without erasing the town, Maya. Help me shape it. You won't agree with everything, but—"
    hide cass_adler
    show maya_rios at center:
        zoom 0.7

    maya_rios "I won't be a rubber stamp, Cass. I want protection that keeps our people in charge."
    "They study you, icy blue eyes sharpening, something unreadable moving like a current in their look."
    hide rosa_alvarez
    show cass_adler at left:
        zoom 0.7

    cass_adler "That's fair."
    "You turn away, the scrape of this evening feeling like a thin beginning of fall—leaves not yet browned but shifting toward loss. Eli falls into step beside you, boots sloshing in a shallow gutter."
    hide mayor_jonah_cruz
    show eli_navarro at right:
        zoom 0.7

    eli_navarro "You did good,"

    maya_rios "We might have delayed digging deeper. Or we might've bought us time. I don't know which is worse."

    eli_navarro "We'll figure it out. We have to."
    "His hand almost touches yours at the edge of the dock and withdraws—respectful, careful—both of you keeping a personal boundary that politics has a way of crossing. The harbor lights blink; distant rigs throw neon like"
    "false constellations. You feel the old shame again—the forecast you once misread—but now it's braided with a new knot: the knowledge that the town can split for reasons both valid and dangerous."
    hide maya_rios
    hide cass_adler
    hide eli_navarro

    scene bg ch2_c4ca42_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A gull's harsh cry, the distant rattle of a crate being loaded]
    # play music "music_placeholder"  # [Music: The cello descends into a single, sustained note—unresolved]
    "A page-turning thought lands with a cold clarity: decisions made in council rooms echo in tides and in the small lives of the people you love. Tonight the echo started. The choice to listen to Aquila"
    "in a formal hearing feels procedural on paper—and seismic in the marrow of the town."
    "You walk away from Harborfront with the weight of a community's split pressing at your ribs. The scrape of fall hasn't finished; it has only begun."

    scene bg ch2_c4ca42_4 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
