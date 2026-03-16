label chapter1:

    # [Scene: The Tidal Lab | Pre-Dawn]

    scene bg ch1_Start_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, soft patter of last night's drizzle draining into gutters]
    # play music "music_placeholder"  # [Music: Slow, hopeful piano with low strings—an optimistic dawn motif]
    "You push the heavy door of the lab and the cool, saline air wraps around you like an old, familiar sheet. The automatic lights blink on in a deliberate sequence: a soft blue over the instrumentation"
    "benches, a warmer amber by the maps. The barometer on your diver's watch ticks an old, steady rhythm—today's reading stubbornly halfway between 'calm' and 'watchful.'"
    "Your notebook is damp where the strap crossed the leather; tide notes and thumb-smudged sketches peep from the edges. You could have stayed in bed. You could have let the town wake without another plan to"
    "carry. Instead you are here before the sun, because plans begin in the quiet when everyone else is still deciding."
    "You walk past the line of skiffs, their hulls streaked with barnacle moons, and the lab's glass reflects the first thin wash of pink. Inside, Jun's station is a scatter of solder, clipped wires, and a mug with the rim flattened like a moon crater."
    show jun_park at left:
        zoom 0.7

    jun_park "Morning, Aria. You look like you swallowed the harbor and kept it polite."
    "You set your bag down and let the smell of coffee and ozone settle your insides. Conversation meets you like warm light."
    show aria_navarro at right:
        zoom 0.7

    aria_navarro "I brought the new bathymetry readouts. And your mug needs replacing."

    jun_park "I prefer character. But sure—I'll solder you a handle that screams 'scientist with feelings'.' (They grin, then tilt their head.) 'You got the Mayor's call last night?"
    "You feel your chest tighten in an anticipatory way that tastes like metal. Dr. Kavir's voice had been careful on the line—protocol-layered—but you can still hear the hope in municipal tone. Funding interest. A public presentation. A deadline that will make or break the pilot."

    aria_navarro "Yes. She's asking for something tangible—something she can explain at the council meeting.' (You thumb through the readout printouts.) 'We need a clear pilot plan. Not a manifesto."
    "Jun scoffs theatrically. 'Says the person who put 'soul of the shore' on a grant title once.'"
    "You laugh, and the sound eases the tightness. Laughter here is a small but fierce rebellion against the scale of the problem."

    menu:
        "Make Jun a timeline—practical and neat":
            "You spread the bathymetry sheets and start drawing milestones in a careful, controlled hand. Jun hums, approving the tempo; it's the machine-made comfort you love."
        "Sketch a vision—messy, emotional, people-first":
            "You grab a marker and scrawl a rough storyboard of community scenes: kids planting mangroves, elders mapping ancestral fishing channels, volunteers in bright neoprene. Jun's eyebrows lift; they like the humanity bleeding into the data."

    # --- merge ---

    "Continues with Jun's line" "Either way, we'll need Mateo on the scaffolding side. He thinks the town needs hard lines more than green fingers."

    jun_park "Either way, we'll need Mateo on the scaffolding side. He thinks the town needs hard lines more than green fingers.' (Their voice softens.) 'But you already know that."
    "You do. Mateo's blue eyes map breakwaters the way other people map faces. His instincts are to counter the sea with geometry—a language of edges and measures. You respect him for it. You also know where those edges have cut into people."
    "You leave Jun soldering and step into the lab's main bay. The instrument array hums like an attentive animal. Screens update with tide gauges, and a cluster of small autonomous boats—painted in peeling sea-glass colors—rock as if breathing."
    "Mateo Hale is there by the rigs, sleeves rolled, sediment-filter goggles pushed onto his head. He looks up when you approach, and the harbor light finds the plane of his cheekbone. For a second, you register"
    "the technical details first—the way his hands carry a set of bolts, the way his jaw sets with familiar concentration—and then you remember that he is also a person who keeps grief like a hidden cache."
    show mateo_hale at center:
        zoom 0.7

    mateo_hale "You're early."

    aria_navarro "You know me.' (You let your voice be both explanation and confession.) 'We have a window before the public noise starts."
    "Mateo Hale glances at the river of data on the nearest screen, then back at you."

    mateo_hale "Kavir briefed me last night about the preliminary modeling. I reinforced the stormwall modules in the CAD. If we can show modular deployments reduce inundation here, the Mayor will have something concrete to sell."

    aria_navarro "She'll want community buy-in too. Hard infrastructure without the people who depend on the shore is a translation problem, not a solution."
    "Mateo Hale studies you like he's measuring a load-bearing point. There's an unspoken friction—both of you want to save the town but you translate 'save' through different crafts."

    mateo_hale "So your mangrove pilot—small patches, strategic—plus sensors to show sediment retention. Combined with targeted modular reinforcements?"

    aria_navarro "Exactly. Hybrid. Ecology and structure.' (Hearing the words aloud makes your chest expand; you can feel potential forming like a tide pooling.) 'We can model outcomes together. The pilot shows ecological lift locally, and your modules buy time where people are most vulnerable."
    "Mateo Hale nods, a slow acknowledgment that feels like a pact. He props the multi-tool on the bench and reaches for a printout."

    mateo_hale "I can build quick-deploy anchors that won't interfere with root systems. If Kavir signs off, I can have a proof-of-concept mockup at the quay by afternoon."

    aria_navarro "Then the meeting isn't just talk.' (Your pulse quickens.) 'If the Mayor sees numbers and a community narrative—actual families willing to plant and measure—it changes the pitch."
    "Before Mateo can answer, the lab door swings and Sora Lin slips in, the kind of entrance that smells like salt bracelets and paint. Their anorak is flecked with green mud and a small sketchbook is tucked into their arm. Sora's energy spills into the room like summer wind."
    hide jun_park
    show sora_lin at left:
        zoom 0.7

    sora_lin "If anyone's going to make this feel human, it's us.' (They toss a handful of sea-glass beads onto the table; they clatter like bright punctuation.) 'We need ceremonies, not just charts. A planting day, a shared feast, stories. People respond to story."

    aria_navarro "And data?"
    "Sora Lin grins, eyes wide and utterly convincing."

    sora_lin "Story that proves itself. We bring the people, you bring the science, Mateo brings his beautiful scaffolding sculptures, Jun brings the gadgetry, Kavir gives the stamp, and Mayor Isla signs the letter that lets us pilot. That's the choreography."
    "You let yourself picture it: neighbors knee-deep in mud, laughing despite the cold, hands elbowing through sticky blackness to set a sapling. You can see Elena, your mother, showing a teen the right way to wedge a root into place."
    "Elena's voice is a warm wedge of home before she even steps into view—she always arrives on time, a human tide. She racks her cart in the lab's entry and the smell of fried fish and citrus follows her like a benediction."
    hide aria_navarro
    show elena_navarro at right:
        zoom 0.7

    elena_navarro "Aria, you look like you carry water in your bones.' (She hugs you, quick and solid, soaking some of the morning into your jacket.) 'Don't forget—they want what works, but they also need to feel they can do it."
    hide mateo_hale
    show aria_navarro at center:
        zoom 0.7

    aria_navarro "I won't."
    "Dr. Kavir enters from the internal office, a calm presence in a coat with elbow patches that speak of many long nights. He catches sight of the group and closes his tablet with a soft click."
    hide sora_lin
    show dr_kavir_singh at left:
        zoom 0.7

    dr_kavir_singh "Good morning. The regional funders responded positively to a scoped pilot. They'll attend the presentation if we provide a measurable outcome and community signatories.' (He sets the tablet down and the screen shows a timeline.) 'We need a two-minute demo, field evidence, and a cost breakdown. Aria, your role will be to synthesize."
    "You feel the map of work spread under your feet—technical tasks, people tasks, the slow choreography of persuasion. It's a lot. It is everything. And yet, standing in this room, the pressure feels less like a weight than a current you can learn to navigate."

    menu:
        "Outline the pilot in bullet points now":
            "You sketch a three-point list: site selection, community engagement day, measurable indicators. Everyone leans in and begins to fill in tasks; the room hums with coordinated purpose."
        "Call for a quick walk to the Old Quay to see the sites":
            "You suggest taking the group to the Old Quay before the sun fully rises. They exchange excited glances—it's easier to persuade with feet on the mud—and within minutes you're all loading into shallow skiffs, conversations bubbling like a shared tide."

    # --- merge ---
    "Continues with the group's departure to the Old Quay and the scene at the quay described below."
    "Outside, the sky blanches into a thinner blue. You walk toward the Old Quay with Sora and Mateo flanking the conversation—Sora sketching people's faces in the margins, Mateo pointing out where reinforcement would be most visible,"
    "Jun muttering about sensor placement. The Old Quay is half-submerged but stubborn: lanterns swing above ankle-deep water, their strings like a constellation strung low."
    "At the water's edge, the town's daily life quietly asserts itself. A woman righting a tarp; an old man mending nets, his hands sure and symmetrical. A child stomps in a puddle, making a miniature deluge"
    "that would have once been ordinary. The combination of human resilience and environmental fragility tugs at you in a way that is almost sacred."
    "Mayor Isla Cortez arrives, not with fanfare but with a practical presence—tablet clasped, sash folded back into a blazer pocket, eyes already on logistics."
    hide elena_navarro
    show mayor_isla_cortez at right:
        zoom 0.7

    mayor_isla_cortez "Thank you for meeting me this early.' (She offers you a small smile.) 'I've seen the preliminary brief. The council wants numbers and a win. But I also need a narrative that lands with the vote. Can you deliver both?"

    aria_navarro "We can. But we'll need to show them the pilot site, community signatures, and a plan that scales."
    "Mayor Isla studies the quay, the people, then you."

    mayor_isla_cortez "Make it visible, make it measureable. If you can make that happen, I'll stand with you at the council."
    "Hope flares. You feel it spread through your limbs like warmth. It's not certainty—nothing about this is guaranteed—but it is forward motion, and for now that is everything."
    "You close your eyes and inhale the harbor: salt, diesel, the faint perfume of fried fish Elena brings. You picture the pilot taking root—the seedlings, the anchors, the sensors chirping like small, watchful birds. You imagine"
    "neighbors reading plain charts and nodding, younger folks excited by the tech, elders bringing stories to the planting day."
    "Dr. Kavir places a hand on your shoulder—brief, steady."

    dr_kavir_singh "Assemble the team by noon. We'll draft the presentation, test a mockup on the quay, and collect signatures. Jun, can you get three sensors up and doing simple sediment readings? Mateo, a mock anchor by midday? Sora, some visual materials and a short ceremonial plan?"
    "Jun, Mateo Hale, and Sora Lin all answer in overlapping, committed sounds—a chorus of 'yes' that spirals into action."
    "You look from one to the other, and something bright and stubborn settles in your chest: possibility. The work is hard, the stakes high, but the town is in motion. You are not alone."
    hide aria_navarro
    hide dr_kavir_singh
    hide mayor_isla_cortez

    scene bg ch1_Start_2 at full_bg
    # play music "music_placeholder"  # [Music: The hopeful motif swells—strings lift, piano becomes more insistent]
    "You step forward to take responsibility for the presentation draft. Your voice is quiet but filled with a new, steady resolve."
    show aria_navarro at left:
        zoom 0.7

    aria_navarro "I'll write the narrative. We'll weave the data into it: what we measure, why it matters, and how the community will own the results. We'll show them that resilience is neither purely concrete nor only ritual—it is a choreography of both."
    show mateo_hale at right:
        zoom 0.7

    mateo_hale "Then let's not waste the tide. We have work."
    show sora_lin at center:
        zoom 0.7

    sora_lin "And let's make sure it's beautiful."
    hide aria_navarro
    show jun_park at left:
        zoom 0.7

    jun_park "And functional. Can't forget functional."
    "Elena presses a wrapped bundle into your hands—it smells like citrus and fried fish—and winks."
    hide mateo_hale
    show elena_navarro at right:
        zoom 0.7

    elena_navarro "For the team. Keep your strength, niña."
    "You tuck it into your bag like a talisman and let the warmth spread through you. The quay buzzes into motion: tools clink, papers rustle, small engines sputter to life. People you grew up with step forward, sleeves rolled, ready to make time for something that might change everything."
    "You feel the current under the town; it's a rising one. For the first time in a long while, the tide seems to be pulling toward a shared horizon."
    "You take a breath, steady the list in your head, and begin to organize the day's tasks—presentation points, community outreach, sensor calibration. There is so much to do, and it all feels possible."
    hide sora_lin
    hide jun_park
    hide elena_navarro

    scene bg ch1_Start_3 at full_bg
    "You stand at the quay, the town unfolding at your back and the sea ahead, and the moment stretches like a held breath—ready to be let go into action."

    scene bg ch1_Start_4 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter2
    return
