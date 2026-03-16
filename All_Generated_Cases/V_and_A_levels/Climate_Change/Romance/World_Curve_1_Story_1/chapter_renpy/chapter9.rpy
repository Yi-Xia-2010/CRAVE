label chapter9:

    # [Scene: Conference Room, Town Hall | Late Morning]

    scene bg ch8_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of the ventilation, murmurs from the hallway, the quick scrape of a chair being pulled forward.]
    # play music "music_placeholder"  # [Music: A brisk string ostinato—urgent, forward-pushing]
    "You stand at the front of the room with mud still dried under your fingernails and the green glass bead cool against your throat. Elias Stone is beside you, calm in a soft sweater, plans rolled"
    "and ready; his satchel leans against the table like a steadying thing. Rowan adjusts his glasses, Amaya clicks through a slide of neighborhood faces, and the mayor's notepad sits open like a promise you both hope"
    "she keeps."
    "The air tastes faintly of salt and reheated coffee. Someone's umbrella thumps in the entryway and the sound ricochets under the fluorescent glare. Your jacket still smells of damp boardwalk and wet wood—home and work braided into the cloth against your shoulders."
    show amaya_chen at left:
        zoom 0.7

    amaya_chen "Mayor Álvarez, thank you for seeing us. We brought the neighbors, the science, and a design that centers the people who live here."
    "Amaya's voice is a warm blade—purposeful, direct. She gestures to a row of faces in the public seats: an old woman with tired hands, a young fisher with callused fingers, a schoolteacher with a damp backpack. They sit like quiet witnesses."
    show professor_rowan_hale at right:
        zoom 0.7

    professor_rowan_hale "The historical models we presented last week consistently show that living-shore approaches reduce peak water velocity and maintain sediment budgets over multi-decadal scales. With stewardship, recovery times shrink and displacement risk drops."
    "Rowan's slides click: layered graphs, pale contour maps, a slow unfolding of time. His voice is deliberate; his hands are slow as weathered driftwood. Each technical point tacks weight to the plan."
    "You feel the room tightening around each data point—as if the words themselves are setting anchors into policy. The mayor reads, lips moving. At the table, an aide takes notes with efficient marks."

    menu:
        "Lean into community testimony—ask Amaya to open with people's stories":
            "You nod toward Amaya. Her face brightens; she steps forward and lets the room hear the soft, ragged edges of loss and hope—neighbors telling, in plain language, what it means to stay. The room hushes, and even the aides shift, re-anchored to the human scale."
        "Highlight Rowan's models—push the technical credibility":
            "You tilt your chin and point to Rowan. He dives deeper into the numbers; the projector fills with lines and timelines. The room leans into graphs, the engineers in the back sit straighter, and the mayor's gaze narrows on measurable outcomes."

    # --- merge ---
    "The scene continues with Amaya's testimony and Rowan's models."
    "Amaya's testimony lands like a tide: intimate, blunt, threaded with small, specific memories. Rowan follows—numbers and timelines that make the memory legible to balance sheets. The contrast feels intentional, and the room breathes around both."
    show mayor_sofa_lvarez at center:
        zoom 0.7

    mayor_sofa_lvarez "This proposal is thoughtful. I appreciate the co-design. But our budget window is narrow. There are investors—Duval's backers—already lined up with fast-track permits. They say they can deliver 'security' quickly. Politics is a pressure I can't pretend isn't there."
    "The fluorescent lights hum an indifferent note. You taste copper—exertion, anxiety—on the back of your tongue. The mayor's fingers drum a rhythm on the table. She meets your eyes with an exhaustion that has the shape of compromise."

    "Elias Stone lays out his version" "A phased pilot gets us a legally backed, insured proof of concept. If the matched grants come through, we protect the most at-risk stretches while documenting performance. We hedge political risk and create a technical record."
    "You hear the reasonable pattern in his voice—the lean lines of his training. His fingers trace the edge of a rolled plan; they are steady. You sense the room shifting toward a practical hinge: a pilot"
    "that keeps the community at the table but concedes legal and temporal space to the council."
    "From the doorway the air compresses—Camille Duval appears with the surgical calm of a storm wall. Her gray suit is precise, a blade matched to the room's crisp edges. Her entrance draws a low ripple of attention—something like a physical intake of breath."
    hide amaya_chen
    show camille_duval at left:
        zoom 0.7

    camille_duval "Mayor Álvarez. The city cannot afford half-measures. A centralized seawall, built swiftly and to spec, guarantees immediate mitigation and investor confidence. Delay is liability."
    "Her voice is controlled, expert, and utterly certain. It cuts."
    "An investor at the back—precise shoes, polished voice—leans in, whispering about liability and timelines. Their murmurs feel like small tides pushing under the room's floorboards."

    "Neighbor from the row" "You saying our homes are worth a ledger? We live here. We fish. We remember what the water took."
    "Shouts ripple. A woman stands, palms open, anger and fear braided. The forum shifts—calm policy talk splintering into raw need. The mayor's jaw tightens; she rubs the bridge of her nose."
    "You can taste the electricity: fluorescent light, heated breath, the metallic sting of adrenaline. The tempo accelerates—voices overlap, papers shuffle, someone starts recording on a phone. The music line in your head climbs: fast, urgent."
    hide professor_rowan_hale
    show elias_stone at right:
        zoom 0.7

    elias_stone "We can anchor this to a pilot, get matched funds, and keep the conversation going. It buys time and builds data—without letting Duval bulldoze us."
    "His hand finds yours across the table and squeezes—brief, sure. The gesture is both comfort and a reminder that he's still trying to negotiate the world into something that keeps you whole."
    "You want to answer with the full force of what you've seen in the marsh—the reedbeds that mended themselves, the neighbor who lost a roof and rebuilt on trust—but the room demands strategy as much as truth."

    menu:
        "Squeeze back—signal you trust his negotiation":
            "You squeeze Elias' hand and let out a breath you didn't realize you were holding. His eyes flick up; for a fraction of a second, relief—and then the steadying professional mask—returns to his face."
        "Pull your hand away and meet Camille's gaze":
            "You let your hand fall and meet Camille directly. She registers the shift: a quiet measurement, as if you're weighing two different kinds of certainty. The room notices the split, and a hush stretches taut."

    # --- merge ---
    "The scene continues with the mayor's deliberation."

    mayor_sofa_lvarez "I need something that can be defended at council and in the papers. Investors are already whispering about default scenarios. My hands are tied without a tangible pilot that shows measurable returns."

    camille_duval "A pilot is just delay. The seawall is proven. We can fast-track permits if the city moves now."
    hide mayor_sofa_lvarez
    show amaya_chen at center:
        zoom 0.7

    amaya_chen "A seawall severs ecosystems and livelihoods. It buys security in one place and moves risk elsewhere. We have a different track record—a living one."

    "Investor Representative" "Your plan is idealistic. Investors need assurance we can limit liability and stabilize property values. The market—"

    "Amaya cuts in, not unkindly" "We are not abstractions on a spreadsheet. These are lives and futures."
    hide camille_duval
    show professor_rowan_hale at left:
        zoom 0.7

    professor_rowan_hale "The models show divergent outcomes. Long-term resilience favors the marsh approach. But I won't pretend there aren't upfront costs."
    "The room's atmosphere turns electric—the kind of heat that sparks action. The mayor leans forward, clasping her pen like a tallying instrument."
    "You feel the pulse in your throat—the tide of decision rising. There are levers here: legal pressure, media spotlight, technical validation, political compromise. Each lever promises a different kind of leverage and a different set of costs."

    elias_stone "If we accept a phased pilot with rigorous safeguards—independent oversight, community governance, matched grants—we create a defensible pathway. It wins votes, protects funding, and keeps us building."
    "You sense the room aligning with his language: defensible, measurable, governable. The mayor nods slowly, thinking in terms of votes and press statements; the investors murmur approval."
    "Inside you, another voice—hot and sharp—says: expose Duval's assumptions publicly. There are files, inconsistencies you and Rowan sketched out in late nights, an investigative rhythm that could flip public opinion overnight. Or you could go all-in:"
    "threaten coordinated legal and civil action, push the city to choose between you and Duval, force a showdown that could save the marsh in full or cost you everything."
    "Your chest is a split tide between tactical patience and moral fury. Hope presses against urgency, and your pulse matches the rising tempo around the table."
    "Elias Stone squeezes your hand again—this time a steadier, insistive pressure that says: we can do this without tearing what we have."
    "You inhale. The fluorescent light above seems to sharpen, the projector clicks mid-slide, and outside the window the marsh is a pale, waiting ribbon."
    "The room waits, the mayor poised like a scale, Camille's expression unreadable but precise, Amaya's jaw tight with a known and practiced readiness. Rowan watches you as if measuring not just your argument, but your readiness to lead it."
    "You can feel the decision carving itself into the minutes—this is the hinge that will make the next act possible: compromise, expose, or full-throttle pressure."
    hide elias_stone
    hide amaya_chen
    hide professor_rowan_hale

    scene bg ch8_6b08b4_2 at full_bg
    # play music "music_placeholder"  # [Music: Strings swell—high, taut—then hold.]

    menu:
        "Push for an official pilot: accept phased compromise with safeguards.":
            jump chapter10
        "Launch an investigative expose about Duval’s assumptions and push for an immediate injunction.":
            jump chapter13
        "Hold the community firm: threaten coordinated legal and civil action unless the city adopts our full plan.":
            jump chapter17
    return
