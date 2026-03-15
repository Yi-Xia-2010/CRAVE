label chapter4:

    # [Scene: Greenridge Solar Terraces | Morning]

    scene bg ch4_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft mechanical hum of inverters, distant gulls, voices moving through wind.]
    # play music "music_placeholder"  # [Music: Warm, ascending strings with light percussion — hopeful, forward-moving.]
    "You step off the path with your satchel under your arm, palms slick with yesterday's tide. The rolled-up updates bump against your ribs like a small, earnest pulse. Light skips across the panels; water beads on"
    "the mock berms and beads along the seams of the testing frames. The terraces smell of sun-warmed salt and crushed grass, the tang of new growth mixed with hot silicon beneath your boots."
    "A polite cluster has formed near the liaison's clipboard—Ben at the edge, Lydia at a measured distance, Asha already elbow-deep in a sample tray, Raff fidgeting as he live-streams with one hand. Elder Mae stands a little apart, braid knotted, watching as if reading tides in people instead of water."
    "You hand the liaison the conceptual integration packet. Her fingers are cool; the corner of her mouth lifts when she sees the annotated diagrams you stuck into the margins."

    "Grant Liaison" "These overlays of panel siting and marsh berms—it's elegant. It reduces footprint while adding habitat connectivity. Did you run the wave overtopping models for the platform alignments?"
    "You can feel how much is riding on each syllable; your chest tightens, then loosens. This is what you built the nights for—the small drawings that could be read by a funder and by a boatwright alike."
    show marin_solace at left:
        zoom 0.7

    marin_solace "We did. The adaptive margin in the models lets us move panel arrays seasonally while retaining continuous sediment flow to the marshes. Asha's test substrates do the heavy lifting on root establishment."
    show asha_patel at right:
        zoom 0.7

    asha_patel "And they don't mind getting their feet wet."
    show councilor_ben_rhee at center:
        zoom 0.7

    councilor_ben_rhee "The council's been impressed with the conditional approach—pilot scale with community oversight. It gets us momentum without committing the town to a single solution."
    hide marin_solace
    show lydia_voss at left:
        zoom 0.7

    lydia_voss "It's sensible. Scaled pilots reduce political risk and still allow for an investment pathway. I'll reserve detailed critique for the meeting materials."
    "Her praise is thin but present; for a moment the terraces feel brighter for it."
    hide asha_patel
    show rafferty_raff_cole at right:
        zoom 0.7

    rafferty_raff_cole "Hey, Marin—people are lining up at the quay. Old Mrs. Hargrove brought her knitting. This will trend."
    "Elder Mae lifts a posture like an old kelp frond catching sun, and then smiles—small but full—and steps forward with a braid of blue ribbon. She threads it through the prototype marker post, hands steady despite age and weather."
    hide councilor_ben_rhee
    show elder_mae_hargrove at center:
        zoom 0.7

    elder_mae_hargrove "You make good things, child. We remember how to tend them."
    "A warm ache blooms in your ribs—vindication that tastes like sea-salt caramel. All the hours, the paper, the patched samples—folding into this public, slow-blooming thing."

    menu:
        "Give the liaison a loose, grateful smile and share a quick personal story about the cooperative":
            "You let your shoulders drop and tell her about the neighbor who taught you how to read a tide chart—how small acts kept the pilot alive. She laughs, attention softens, and the liaison leans in, scribbling notes that feel like small promises."
        "Maintain a focused, professional tone and walk through the models step-by-step":
            "You tighten your shoulders into a practiced cadence, walking her through the technical overlays. Her pen moves faster; you see in her eyes the math aligning with values. The warmth is quieter, but it lands as seriousness rather than sentiment."

    # --- merge ---
    "Scene continues"
    # [Scene transition: The light shifts as the sun climbs. You tuck a spare pair of gloves into your satchel and head down toward the quay.]
    # [Scene: The Quay | Late Morning]
    hide lydia_voss
    hide rafferty_raff_cole
    hide elder_mae_hargrove

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Water lapping, dock planks creaking, the faint clink of metal rigging.]
    # [Smell: Brine, tar, hot rope. The air carries the smell of Jonah's deck—sea and lemon oil from his cloth.]
    # play music "music_placeholder"  # [Music: A light acoustic—sparse guitar with a soft, optimistic melody.]
    "Jonah Reyes looks up as you approach; a smear of seawater runs down his forearm and he wipes it with the back of his hand, grinning like he's been told a good joke."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "By the look of those floats, they're holding. You hear that? That's not just bobbing—that's weight distribution doing its honest work."
    "You crouch beside him, fingers finding the familiar knot of a cleat. The rope is warm where the sunlight hits it, gritty with salt. You anchor a testing float as Jonah instructs, his hands fluent, patient, steady in a way that quiets the nervousness you didn't know you were carrying."
    show marin_solace at right:
        zoom 0.7

    marin_solace "Asha's substrate's sealing the seams. If we can scale the material for more units, the maintenance cycle drops by—"

    jonah_reyes "—and fish have places to hide. They like structure. I snagged a juvenile snapper near the test last tide. Proof's in the water."
    "You both laugh, but the laugh stretches into something softer. His eyes—amber and open—hold a steady encouragement. You feel seen in a way that's not about the grant or the cameras; he's anchoring you as much as the float."

    jonah_reyes "You don't need to carry all of this alone, Marin. Hand off a rope now and then. Let someone else take the strain."

    marin_solace "I know. I'm learning how."
    "Raff runs up, breathless, waving his phone like a flag."
    show rafferty_raff_cole at center:
        zoom 0.7

    rafferty_raff_cole "Media's here. Live! They want footage of the floats and a soundbite. Also, my followers want to know—Jonah, were you always this poetic about ropes?"

    jonah_reyes "Only when a rope holds a town together."
    "There, a chorus of dry humor and affectionate teasing. The quay hums with practical work—voices calling, tools clinking, volunteers passing sandbags and planting trays into the nursery racks. Seniors lend memory and steady hands; boatwrights turn"
    "up with tar-stained palms; teenagers with hoodies and patched elbows move like a new current."

    menu:
        "Tease Jonah back, lightening the mood":
            "You jab at his shoulder, a grin splitting free. He laughs, and the moment becomes a small, private harbor—easier to breathe in."
        "Keep the focus tight; hand him a schematic and ask for a technical read":
            "You hand over the schematics. His face folds into measurement and judgment; he gives a clean, practical solution and the project gains a precise new edge. The intimacy shifts toward collaboration rather than flirtation."

    # --- merge ---
    "Scene continues"

    jonah_reyes "Whatever we do next—the staged scale-up, pilots, whatever—keep me in the loop. I want docks that work for fishers, not cages that keep them out."

    marin_solace "Always."
    # [Scene: The Saltworks — Marin's Cooperative Lab | Afternoon]
    hide jonah_reyes
    hide marin_solace
    hide rafferty_raff_cole

    scene bg ch4_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low staccato of lab equipment, happy murmurs of volunteers, a distant radio playing an old sea shanty remixed into a hopeful loop.]
    # [Smell: Earth, kelp, coffee. The tang of wet clay under fingernails.]
    # play music "music_placeholder"  # [Music: Swelling strings, gentle choir tones—hopeful, communal.]
    "Back at the Saltworks, you move through the small controlled chaos—Asha pointing out root structures, Raff editing footage, volunteers labelling jars of samples with trembling care. Someone brings in a tray of smoked fish sandwiches; the mundane domesticity of it anchors the triumph in ordinary need."
    show asha_patel at left:
        zoom 0.7

    asha_patel "Look—rhizomes are establishing. We're getting retention and bioturbation where we need it. Salmonid larvae in the mid-sample set. This is real."
    "You read the data as if it's a letter. The numbers are modest and the trend is what you want: upward, consistent. A warmth spreads through you that is not just relief; it's the sense of something you've carried for years finally taking a public shape."

    "Reporter" "Marin, how do you respond to critics who say pilots delay the urgent infrastructure the town needs?"
    show marin_solace at right:
        zoom 0.7

    marin_solace "Pilots are not delay; they're proof. They let us act with humility and evidence—so when larger investments come, they build on what keeps lives and habitats intact."
    "The reporter nods, pen scratching. You notice Lydia Voss watching from the pavilion across town, her expression narrow and careful. For now, she offers thin praise; she has the attention of investors, and you have the town's trust. Both currencies matter."
    "Elder Mae threads another ribbon into a marker post destined for the community garden at the floodwall. Her hands are careful, the ribbon a quiet benediction."
    show elder_mae_hargrove at center:
        zoom 0.7

    elder_mae_hargrove "We stitch the new world into the old. That is the work."

    menu:
        "Take the reporter's mic and speak plainly about community oversight":
            "You step forward and speak without engineering veneer—about mothers, fishers, elders. The camera captures a human angle; comments surge; people nod on the terraces."
        "Deflect to Elder Mae and hand her the mic":
            "You press the mic into Mae's hands. She speaks of memory and stewardship in plain, unvarnished sentences. The room stills; even the reporters lean in. The narrative becomes older, deeper, truer."

    # --- merge ---
    "Scene continues"
    "Asha loops an arm through yours, eyes bright. Raff's feed is already showing clips of the trays and the quay; comments roll in like a supportive undertow. Volunteers trade stories—who planted which runner grass, who fixed which float, who remembered a tide chart differently. Each anecdote is a stitch."
    # [Scene: Havenpoint Boardwalk & Market | Golden Hour]
    hide asha_patel
    hide marin_solace
    hide elder_mae_hargrove

    scene bg ch4_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmured conversations, a vendor's call, the soft clink of Elder Mae’s bracelet as she walks.]
    # [Smell: Sweet preserves, frying fish, the persistent salt in the air.]
    # play music "music_placeholder"  # [Music: Lighter strings with a soft brass, warming into a hopeful chord.]
    "You walk the market as the sun leans low, the town's faces passing by like pages in a shared book. Ben gives a prepared smile to a camera and casts a look your way that says,"
    "quietly, good work. Lydia Voss's pavilion glows across the way—clinical, beacon-like—but tonight the painted murals on the floodwall are full of people, not promises. Children dart among raised beds, fingers black with soil."
    "Raff bounds up and thrusts a small folded note into your hand—it's from the regional funder, an invitation for a staged scale-up meeting. The paper trembles, small and heavy."
    show rafferty_raff_cole at left:
        zoom 0.7

    rafferty_raff_cole "They want to talk staged scale-up. Like—real money and next-level planning. This is it."
    "The ground seems to tilt—not under threat now, but toward possibility. For a breath, the town holds its collective breath with you, expectation humming like electricity when a storm reframes itself into light."
    "You let the page flutter in your fingers, feeling the edges of every early draft, every prototype, and every late-night conversation fold into this single moment. The pilot has become more than proof; it's opened a door."
    show marin_solace at right:
        zoom 0.7

    marin_solace "If we accept, we set terms: community oversight, phased implementation, habitat-first metrics. We protect jobs without losing our bay."
    "Jonah Reyes comes up beside you, shoulder brushing yours in a casual alignment. His presence steadies the surge of adrenaline."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "Whatever you put on the table, I'm with you. We'll make sure the docks keep working."
    "Elder Mae threads a final knot into the ribbon on the marker post and looks at you as if measuring the tide of time."
    hide rafferty_raff_cole
    show elder_mae_hargrove at left:
        zoom 0.7

    elder_mae_hargrove "Tides change. People remember. Do the thing that makes people remember kindly."
    "A flush of quiet, full celebration swells—volunteers cheering, children clapping, the market's hum lifting into a chorus. Cameras are still rolling; someone shouts a cheer; Lydia Voss's face is set but not triumphant—the field has shifted."
    "A prospectus for a staged scale-up meeting sits in your satchel now—real interest, yes, but also responsibility. You close your fingers around the paper as if holding the town's breath and its ballast at once."
    "Your private resolve — the small, steady flame you kept against storms and late nights — has finally taken public form. The pilot’s data, modest and honest, charts a new course."
    hide marin_solace
    hide jonah_reyes
    hide elder_mae_hargrove

    scene bg ch4_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: A single sustaining violin note; hopeful, unresolved.]
    "You look up at the string lights and feel the town tilt—toward you, toward the pilot, toward a choice that will decide how scaling happens, who sits at the table, which values get written into the margin."
    "Marin Solace [internal]: This could change everything. It could also mean we have to keep our hand when pressure pushes for speed. Either way, we don't step back now."
    # play music "music_placeholder"  # [Music: Strings swell, then soften into a patient, expectant hum.]

    scene bg ch4_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
