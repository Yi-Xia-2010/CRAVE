label chapter13:

    # [Scene: Lumen Bay Promenade | Late Afternoon]

    scene bg ch13_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm strings, ascending motif; light percussive rhythm like paddles in water]
    "You feel the aftertaste of your own words—measured, deliberate—still on your tongue. The decision to call for time sits between you and Dahlia Kestrel like a newly tied knot: obvious, strong, not easily undone."
    "Rosa stands beside you, clipboard hugged to her chest. Her braid flicks as she scans the crowd, then returns to you with a small, frank smile."
    show rosa_mendes at left:
        zoom 0.7

    rosa_mendes "That took backbone, Maya. You didn't cede the floor."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "We didn't. We made the town the thing to be decided about."
    # play sound "sfx_placeholder"  # [Sound: Distant gulls; a cart creaks; a child's laughter fades]
    hide rosa_mendes
    hide maya_reyes

    scene bg ch13_453e40_2 at full_bg
    "Dahlia Kestrel moves toward you with the same calm precision she uses in presentations. Her steps are quiet on wet wood, each one a diplomatic nudge."
    show dahlia_kestrel at left:
        zoom 0.7

    dahlia_kestrel "Ms. Reyes. That was an unexpected—refreshing—interruption. A neighborhood vote. Independent studies. You know that slows timelines."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "It does. But it gives people a voice, and it forces scrutiny where there’s hype. We can move fast only if everyone trusts the plan."

    dahlia_kestrel "Trust, yes. The funders don't like uncertainty. They like deliverables."

    maya_reyes "We like people who still live here when the deliverables are measured. I asked for a trial. A controlled, side-by-side pilot. If your tech can prove itself without erasing the marsh, we'll scale it. If not, we keep what works."
    "Dahlia Kestrel studies you—ice-gray eyes narrowing just enough that the sodium lamps catch like a blade. For a heartbeat you imagine the old fight: your grassroots grit against her streamlined certainty."

    dahlia_kestrel "A trial, under strict parameters. Limited scope. Transparent metrics. Community oversight. If the town supports it, I will fund that pilot."
    "Rosa exhales somewhere behind you; the sound is almost a laugh. The crowd murmurs into a thousand hopeful threads. You let the moment be small and ferocious."
    hide dahlia_kestrel
    hide maya_reyes

    scene bg ch13_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: The strings resolve to a quiet, ascending chord—steady, not flashy]
    "You nod. The agreement is not victory, but it is a path forward that keeps the town at the center."
    # [Scene: Skyline Rooftop Garden | Early Evening]

    scene bg ch13_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Muffled traffic below, the soft rustle of compost; insects chirp; the smell of earth and citrus from the preserves]
    # play music "music_placeholder"  # [Music: Intimate, hopeful piano with a touch of wind chimes]
    "Inside the rooftop greenhouse, the air is warm and dense with plant life—tomatoes, young cordgrass in pots, and solar panels like quiet guardians. Asha threads a kettle toward the circle of folding chairs. Elders set out"
    "glass jars of plum preserves, and someone props an old tide gauge as a conversation piece."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "Thank you all for coming. This space feels… appropriate."
    show asha_patel at right:
        zoom 0.7

    asha_patel "Appropriate and right. We do this like we mean it. Science at the table, fishers at the table, elders at the table."
    show rosa_mendes at center:
        zoom 0.7

    rosa_mendes "Mayor Durant will call the vote next week. We have to present a legal framework for oversight—clear checkpoints, community seats, provisions for apprenticeship hiring."

    "Elder Mateo" "Our people want to see work they can do. Not fences that keep them out."

    menu:
        "Offer Mateo a seat on the oversight board":
            "You slide the note across with his name written in your tidy script; his knuckles close around the paper and the corners of his mouth soften."
        "Promise funded apprenticeships first, then board seats":
            "You lay out a short plan for hiring and training—Rosa nods, Asha looks relieved, Mateo looks at the jars of preserves as if tasting a future."
        "Ask the scientists to draft measurable ecological benchmarks":
            "You make the request aloud; the lead scientist's eyes light up, and she shuffles her papers—numbers and timelines already forming in her head."

    # --- merge ---

    "Continue with Asha's line" "All of those. We have to do them together."

    asha_patel "All of those. We have to do them together."

    "Dr. Chen" "We can run paired plots: one with marsh transplants, one adjacent set with modified modular protection. We'll monitor sedimentation rates, invertebrate diversity, and vegetative colonization. Data logged openly."
    "Elias Kwan arrives as the conversation hums—salt on his coat, rope loops at his hip. He moves through the circle with the pragmatic ease of someone who knows how to read both sea and crowd."
    hide maya_reyes
    show elias_kwan at left:
        zoom 0.7

    elias_kwan "I can train kids on net maintenance and set markers at the inlet. Keep boats away from the transplant zones. If you're doing apprenticeships, I'll teach them how to fix what breaks."
    "You catch his hand as he passes—no grand gesture, just a brief brush of palm against wrist, salt and callus. His ocean-blue eyes meet yours and something steady passes between you: the small, mutual recognition of shared labor."

    elias_kwan "A juvenile tern came back today. Landed on the wire by the docks like she was checking in."
    hide asha_patel
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "That's a good sign. Little things add up."
    hide rosa_mendes
    hide elias_kwan
    hide maya_reyes

    scene bg ch13_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Wooden percussion picks up, like steady rowing]
    show rosa_mendes at left:
        zoom 0.7

    rosa_mendes "We draft the oversight charter, Dr. Chen prepares the experimental design, Dahlia Kestrel funds the controlled inlet pilot for the modular segment, and the town votes. If the vote passes, the pilot goes in under monitoring and community co-management."
    show dahlia_kestrel at right:
        zoom 0.7

    dahlia_kestrel "I will sign the contract contingent on the vote and the legal terms. I want a rapid reporting cadence—weekly updates to my team and a shared dashboard."
    show maya_reyes at center:
        zoom 0.7

    maya_reyes "Weekly—fine. But the data feed goes public. Everyone gets the same view."

    dahlia_kestrel "Transparency is good PR."
    "You think of press flashes and headlines and the temptation that had, for a moment, tugged at your sleeve. You push it back. There is a durability to slow work that headlines can never buy."
    # [Scene: Controlled Inlet | Early Morning, Weeks Later]
    hide rosa_mendes
    hide dahlia_kestrel
    hide maya_reyes

    scene bg ch13_453e40_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hiss of pumps, the distant rumble of construction, gulls squabbling; boots squelching in wet soil]
    # play music "music_placeholder"  # [Music: Steady low strings, an undercurrent of optimism]
    "The pilot is smaller than anyone expected; a measured scale designed to be reversible. Scientists move with clipboards; youths in patched oilskins carry markers. You stand on the inlet bank, camera at your hip, journal open to a page where you sketch sediment flow."

    "Dr. Chen" "See this—sediment accretion is within expected bounds at tidal range two. We need three weeks of consistent data to be confident."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "And the transplants?"
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "Cordgrass plugs are taking. Look—tiny roots already binding the mud."
    "Elias Kwan kneels near a shallow channel, teaching a teenager how to secure a marker line without tangling nets. His hands are careful, patient—less the stubbornness of argument and more the steadiness of technique."
    show elias_kwan at center:
        zoom 0.7

    elias_kwan "Keep the line taut. If it droops, the tide pulls on it and you'll lose the marker overnight."

    "Teenager" "Got it. Like tying my shoelaces tighter."
    "You walk the inlet slowly, fingertips brushing pooled water, listening to the smallness of success—the slap of a fish against netting, the quick, bright call of a tern. Each sound is a stitch in a larger repair."

    menu:
        "Make an entry into the public dashboard about today's accretion data":
            "You key in the numbers, add a short note about methodology, and watch the feed populate—comments and thumbs-up trickle in from neighbors."
        "Take a photograph and tuck it into your journal instead":
            "You lift the camera and capture a wide shot; later, when the light softens, you press the print into the journal between pages as a private record."

    # --- merge ---

    "Continue with Dr. Chen" "The transparency seems to be calming concerns on both sides. People see the data and ask better questions."

    "Dr. Chen" "The transparency seems to be calming concerns on both sides. People see the data and ask better questions."

    maya_reyes "They also volunteer. Repair crews, monitoring shifts. It's become an apprenticeship economy in two weeks."
    hide maya_reyes
    hide jonah_reyes
    hide elias_kwan

    scene bg ch13_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Layered harmonies rise subtly; hopeful, communal]
    # [Scene: Marsh of Tides | Midday]

    scene bg ch13_453e40_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Mud-suck of boots, soft chatter, insects; the smell of iodine and wet earth]
    # play music "music_placeholder"  # [Music: Quiet, warm strings]
    "You stand knee-deep at the marsh edge, sleeves rolled, the weight of the day settling into your shoulders as a familiar ache. The apprentices you helped recruit move with focused limbs; their hands are learning a new economy where the bay is both job and teacher."

    "Elder Mateo" "Not like a factory! Careful with the roots—gently does it, like holding a dream."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "We saved one area from erosion last week. It didn't all come from the panels—people stacking driftwood cages helped slow the flow overnight."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Every small hold matters. We stitch the edges and let the center fill in."
    "Elias Kwan wades closer, his sleeves slick with mud. He hands you a damp marker with a grin that is half boyish, half fatherly."
    show elias_kwan at center:
        zoom 0.7

    elias_kwan "Tomorrow I'll set up a rotation for canoe patrols. Keep people out of sensitive zones and teach nets to young hands."

    maya_reyes "Thank you. For everything."
    "He rubs his thumb along the carved wooden hook at his neck as if steadying himself on inheritance and choice."

    elias_kwan "Your work gave us a say. That was the important part."

    maya_reyes "We did it together."
    hide jonah_reyes
    hide maya_reyes
    hide elias_kwan

    scene bg ch13_453e40_9 at full_bg
    # play music "music_placeholder"  # [Music: A light, single-note motif like a bell]
    "You trace a fresh set of entries into your field journal each night—raw data, volunteer lists, letters from neighbors, sketches of cross-sections. You make the feeds public: graphs, photographs, notes in plain language so your neighbors"
    "can read the science without jargon. The dashboards are simple and honest, like your field notes: rises and dips, annotated by who worked which shift."
    show rosa_mendes at left:
        zoom 0.7

    rosa_mendes "We have council-approved apprenticeship funding. Two certified restoration trainers were hired from the town. Mayor Durant pushed hard."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "That's the leverage we needed. Jobs and stewardship on the same page."
    # [Scene: Skyline Rooftop Garden | Sunset, Weeks After Pilot Begins]
    hide rosa_mendes
    hide maya_reyes

    scene bg ch13_453e40_10 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft chatter, the clink of spoons, the distant slap of waves; compost smells sweet and warm]
    # play music "music_placeholder"  # [Music: Triumphant yet intimate strings; a gentle swell that implies progress without finality]
    "Maya Reyes sits with your journal open, the public dashboard on your tablet glowing beside a bowl of shared stew. The pilot's first report sits on the table: modest wins, scientifically significant trends, and a community roster that reads like a new kind of citizenship."

    "Dr. Chen" "The paired plots show higher biodiversity in restored marsh sections by a small but meaningful margin. The modular prototype didn't cause detrimental flow displacement in the controlled inlet."
    "Dahlia Kestrel stands a little apart, hands folded. Her posture has relaxed since the first meeting; bristling has been replaced by an occasional, careful smile."
    show dahlia_kestrel at left:
        zoom 0.7

    dahlia_kestrel "The data is respectable. Your community oversight actually improved deployment decisions. I admit—that was a surprise."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "We wanted accountability, not a pedestal. Looks like we can both learn."
    "Elias Kwan arrives with a teen apprentice who carries a jar of pickled clams—an offering. He sits beside you, shoulders brushing in the way of people who have been through long days together."
    show elias_kwan at center:
        zoom 0.7

    elias_kwan "The kid's proud. He repaired a net for the first time today without anyone fixing it after him."

    maya_reyes "They're learning to fish and to mend the shore."
    "You let the rooftop's murmur fill the spaces between sentences. The town's pulse seems steadier—less like an anxious drum and more like a human heartbeat."
    hide dahlia_kestrel
    hide maya_reyes
    hide elias_kwan

    scene bg ch13_453e40_11 at full_bg
    # play music "music_placeholder"  # [Music: The strings resolve into a warm, rising chord; light swells]
    "You feel the slow ascent—the cadence of steady work, of weeks stacking into a ladder. Your temptation to chase headlines is a distant wave you no longer ride. Instead you savor small certainties: a teen learning"
    "a net stitch, an elder’s name on an oversight board, a tern returning to check in."
    show rosa_mendes at left:
        zoom 0.7

    rosa_mendes "The vote next week will be a test. But if it goes our way, the pilot's framework becomes policy."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "We built something that can be replicated without erasing home. That's the metric we set."
    # play music "music_placeholder"  # [Music: A single, sustained note holds—inviting, expectant]
    "You pack your journal slowly, fingers lingering on the curves of inked numbers. Outside, the lights of Lumen Bay begin to blink on—small beacons strung along the boardwalk, each one a promise of nights lived in"
    "place. You let yourself feel the ascent as a physical thing: the soreness after a long day, the quiet satisfaction before sleep. It is not dramatic. It is durable."
    "A gull cries. A neighbor closes up a stall. The rooftop's warmth wraps around you—a communal blanket stitched from many hands."
    "You look up at the line of stars just visible above the sodium glow and think: small, steady steps. This is how we grow."
    hide rosa_mendes
    hide maya_reyes

    scene bg ch13_453e40_12 at full_bg
    # play music "music_placeholder"  # [Music: Music fades to a single hopeful motif]
    "Maya Reyes closes your journal with a soft, decisive motion and stand there for a long moment, listening to the town breathe."
    # [Page-Turn Moment]
    "You could measure success in headlines, designs, or sealed contracts—but tonight, success tastes like plum preserves and warm earth. The pilot has begun to prove that speed need not mean erasure, and that work done in"
    "public changes how people argue about safety. Yet the vote remains. The tests will continue. The choice the town must make is still ahead—bigger and messier than any single report."
    "You feel the line between fear and hope thin into possibility. If the town says yes, next will be scale decisions: which prototypes expand, which training programs become permanent, how the law will bind corporate power to communal oversight."
    "You tuck the journal under your arm and walk toward the stairwell, the future weighing pleasantly in your hands—real, incremental, and yours to steward."

    scene bg ch13_453e40_13 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter14
    return
