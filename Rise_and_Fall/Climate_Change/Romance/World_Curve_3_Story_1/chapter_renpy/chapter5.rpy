label chapter5:

    # [Scene: Salt Flats Lagoon | Dawn]

    scene bg ch5_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Thin creak of old ropes; a distant gull; the small, insistent drip from a bent pipe]
    # play music "music_placeholder"  # [Music: Sparse piano notes under a low, sustained cello — slow, descending]
    "You walk the edge of the lagoon and the town reads itself in wreckage. The pylons that once held up reclaimed piers lean at angles that look almost deliberate, as if the sea had been taught"
    "to write its displeasure in metal. Reflections of broken sky shiver in puddles between clumps of algae. Every step leaves a soft, slurping print in the mud."

    "Aunt Pilar kneels on a battered foam pad, hands steady as tide lines. She works with a practised economy—bandage, knot, tuck—names falling out of her mouth like a rosary. Each name is a small stone dropped, counted: Mateo... Rosa... Mr. Alvarez... A pause, then another" "No one wanted to go, but the gang covers are gone."
    show aunt_pilar at left:
        zoom 0.7

    aunt_pilar "You came when the night was worst. That helped. That—' (she taps your shoulder with a dirt-stained finger) '—keeps people from thinking they were alone."
    "You kneel opposite her to hand over another roll of tape. The tape is thin, weathered like everything here; the adhesive still clings, like stubbornness."

    "You" "I should've seen the hinge points. I should've—"
    "Aunt Pilar: (shakes her head) 'Seeing is not stopping. You saw. You tried. We bury too many good people to polite regrets, mi'ja. Now we do what we can.'"
    "Her hands don't slow. She ties a bandage around a wrist and slips a small, folded paper—names of those missing—into your palm without asking. The paper smells faintly of coffee and the citrus-scented soap she always uses."
    "You close your fingers around it. The compass at your throat presses cool and familiar against your skin, and for a second the memory of wind and your father's arms returns — less like instruction now, more like accusation."

    menu:
        "Help Pilar tie the next bandage":
            "You take the roll and emulate her motions. Your knots are clumsy and your fingers smell like mud, but she hums approval, the kind that stitches you into something larger."
        "Step back and count the damage instead":
            "You let Pilar work and walk the rim of the lagoon. Each pylon's angle becomes a notation in your head — a pattern beginning to form. Pilar nods once, understanding the way you cope: by cataloguing."

    # --- merge ---
    "The scene continues."
    # [Scene: Wet Streets | Morning]
    hide aunt_pilar

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low murmur of volunteers under awnings; distant shouts; the constant, mechanical sigh of community pumps]
    # play music "music_placeholder"  # [Music: A single mournful violin with restrained percussion — heartbeat-like]
    "Jonah Reyes's shoulders are damp; his hair clings at the temples and that single silver streak in his hair flashes like a tiny blade when he turns toward you. He doesn't speak right away. When he does, his voice is gentle and tethered to urgency."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "They came out when the call went up. People with carts and blankets, neighbors dragging mattresses from the low flats. We made noise. We got cameras. We—' (he swallows) '—we couldn't stop the surge where it mattered."
    "You watch him, memorizing the set of his jaw where anger meets grief. There's soot in the crook of his neck, a smear of oily residue from pumps. His palms are raw from hauling sandbags. The"
    "camera at his chest looks oddly like a relic, used to document ritual and now mute witness to a failure."

    "You" "Visibility buys us time and allies. It doesn't buy a levee where a pylon redirects a surge."

    jonah_reyes "Then we force them to see what happened. We occupy. We don't let them pour concrete while our people sleep on the street. We stand in front of bulldozers and tell the cameras the names Aunt Pilar says out loud."

    "You" "And risk arrests. Evictions. If the storms pick up and we have people camped outside a construction site, we could lose more than pride."
    "Jonah Reyes: (leans closer, voice low) 'Sometimes you have to risk losing a thing to stop losing everything.'"
    "Your chest tightens. The logic that lives in your notebooks is a different kind of grammar than Jonah's rhetoric, but they both parse to the same grief."
    "You walk past a shivering group under a tarp: volunteers with reddened noses, hands in gloves too thin for the cold. Rosa is there, rubbing her palms together."
    show rosa_and_mateo_market_co_op at right:
        zoom 0.7

    rosa_and_mateo_market_co_op "We can make hot tea, take shifts. People need to move into shelters but not be kicked out of homes they made."
    show rosa_and_mateo_market_co_op at center:
        zoom 0.7

    rosa_and_mateo_market_co_op "Councilor's people say they'll arrange buses. But will the developers take this as leverage to press permits faster? Or—"
    "You: (interrupting, practical) 'Tell me who is injured and where. We tally names, we make a list—medical, displaced, missing. We don't let them speak for us.'"
    "Rosa: (gives you a look of fierce tired gratitude) 'You always make lists like they can hold a storm back.'"

    menu:
        "Take charge of the volunteer roster":
            "You grab the clipboard. Your handwriting is rushed but legible. The volunteers feel steadier; someone starts a quiet chant that is more organizing than mourning."
        "Sit with Jonah and plan the hill we'll hold":
            "You sit on the wet curb and outline the logistics: who can be out all night, who needs legal help, what to barricade. Jonah fills the margins with quick sketches. Your breathing syncs, for a moment, with the plan."
        "Walk farther to the lab to get Claire's confirmation":
            "You tell Jonah you'll meet him after the lab. He nods with a small, worried smile and the camera lifts slightly as if remembering its purpose."

    # --- merge ---
    "The scene continues toward the lab."
    # [Scene: Tidewatch Coastal Lab | Mid-morning]
    hide jonah_reyes
    hide rosa_and_mateo_market_co_op
    hide rosa_and_mateo_market_co_op

    scene bg ch5_4001e7_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low whir of pumps, the click of instruments syncing, Claire's tablet emitting a soft data-accept tone]
    # play music "music_placeholder"  # [Music: Electronic hum layered with a distant single sustained cello — clinical sorrow]
    "Inside the lab the air smells of ozone and solder and the faint metallic tang of seawater brought in on boots. Claire Hsu is bent over a laptop with eyes that have not left data long"
    "enough to blink. She pushes up her sleeves, revealing a smear of rust on her forearm like the town's bruise."
    show dr_claire_hsu at left:
        zoom 0.7

    dr_claire_hsu "We recorded it. All of it. The surge wasn't uniform. Look.' (she swivels the laptop so you can see a time-lapse of spectral overlays — blue tides, red pressure spikes) 'Those pylons—reclaimed pylons from the '80s—transmitted the energy along an axis we didn't anticipate. It created a cascade. One breach amplified another."
    "You lean in over the screen. The animation shows the wave shimming around a stubborn old pylon and then, like dominoes, hitting a cluster that then funneled water deeper into the older neighborhoods. Your breath fogs the laptop screen for a moment; your heartbeat thrums in your ears."

    "You" "So the model is clear. Maps I made and Claire's sensors agree. This wasn't just weather. It was structural."

    dr_claire_hsu "Exactly. And because the path is structural, that means mitigation isn't purely stopgap sandbags. It means rethinking those reclaimed corridors, their placement. It means policy."
    "You close your eyes and see the tide-maps in your notebook: inked lines, scribbles, dates. For the first time they feel like evidence you could hold up in a hearing, not just sketches for hope."

    "You" "If we can show this is a design problem, not just a storm, we can argue to stop the project on scientific grounds."
    "Dr. Claire Hsu: (softly) 'Science makes good witnesses. It doesn't make people change.'"

    "You" "Then we make them uncomfortable witnesses."
    "Claire exhales, part encouragement, part weary doubt. She reaches for a thermos and offers you the last lukewarm coffee."

    dr_claire_hsu "You'll need more than data, Mara. You'll need a strategy that acknowledges grief, not paper over it. Legal teeth. Media presence. A plan for people who won't be rehoused with a handshake."

    "You" "We have volunteers, and a market that will show up. Jonah's pushing for occupation to stop work. That would get cameras."
    "Dr. Claire Hsu: (hesitates) 'It might also provoke a heavy-handed response. If someone gets hurt, the optics swing fast and cruel.'"
    "The lab's instruments register a new incoming alert. The pumps outside kick up their pitch — the town never stops; it simply learns new ways to moan."

    menu:
        "Press Claire for a public write-up of the cascade":
            "You ask her to draft a clear report we can give to Avi and the press. Claire nods; it's work, but it's something tangible."
        "Tell Claire you'll use the data to plan where to stand on the blockage":
            "You fold the laptop closed with a map inside. Claire looks at you like she wants to argue but doesn't; you both know the stakes are higher than proof alone."

    # --- merge ---
    "The scene continues toward the Voss site."
    # [Scene: Town Edge — Between Lab and Voss Site | Late Morning]
    hide dr_claire_hsu

    scene bg ch5_4001e7_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A growing murmur turns to shouted names; somewhere a drum begins a slow beat, like a funeral march that wants to be a battle cry]
    # play music "music_placeholder"  # [Music: Tension builds — low brass and an ominous snare. The tempo quickens in the background.]
    "Word spreads. People gather, some from the market, some who lost rooms, some who shivered on neighbor's floors the night before. Anger and grief braid into the same rope."
    "Jonah Reyes finds you near a pile of sandbags. His eyes are rimmed with fatigue and something like resolve that makes your own muscles tighten in reflex."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "We can make a perimeter at the Voss site. We bring tents, legal observers, media. We create a human dam between the cranes and the concrete. They can't bulldoze when cameras and bodies are there."

    "You" "And force an escalation. Elena will call the police. The permit's still valid. The company will frame us as violent agitators and portray the town as unruly."

    jonah_reyes "Let them try. Let them film themselves dragging away elderly people. Let the country see the discrepancy between the 'secure' option and the people who keep getting washed away."

    "You" "Or we go to Avi. We use Claire's data, your network, our volunteers, to press for a legal compromise that buys time—enforceable wetlands protections, temporary moratoria on grading."

    jonah_reyes "And watch them water down protections in meetings. Watch them sign away neighborhoods in ink and call it 'strategic retreat.' You want to let them decide who lives where? We're the ones who live here."
    "A flicker of something almost like humor crosses his face, then fades."

    jonah_reyes "There's a third option. A risky one. I know people who can—' (he stops; the idea feels wrong on his tongue) '—who could make the demonstration of structural instability undeniable. Make the demo blow its own trumpet and fall on its face."
    "You: (your stomach drops) 'You mean sabotage.'"

    jonah_reyes "Not to hurt anyone. Just disable the demo in a way that the engineering firms can't spin. Force an independent inspection."

    "You" "That's criminal. That's crossing a line I keep telling myself I won't cross."
    "Jonah Reyes: (voice soft) 'We already crossed a line, Mara. The line was the decision to build on reclaimed land that pushes water where our elders live. We just didn't see it.'"
    "You stand in the wet and cold, feeling like a fulcrum where history and desire and loss all press their weight. Your notebook in your jacket is damp at the edges. The tide maps inside are no longer abstractions; they are a ledger."
    "Around you, the community rages and grieves in equal measure. Someone cries out a name. A child asks for their blanket. Aunt Pilar moves through the crowd like a quiet lighthouse."
    "Aunt Pilar: (to you, quietly) 'You can choose the shape of how we fall. Choose the part you can live with.'"
    "Her eyes are unreadable, as they must be for everyone who relies on her steadiness."
    "Jonah reaches for your hand. The damp cools your skin, the compass pendant cold against your chest like an accusation and a benediction both."

    jonah_reyes "I can't do this alone. I don't want you to do this alone either. But I can't watch us lose people because we were polite."
    "You inhale the sea and the diesel and the metallic ache of ruined plans. Exhaustion sits in your bones like an old, heavy coat. You can feel the options aligning in the way tides align—predictable, inevitable, each with its own cost."
    "You: (your voice is a whisper that somehow must hold an entire town) 'We have to decide. Now.'"
    # play music "music_placeholder"  # [Music: The cello drops out; only the distant pulse of the pumps remains]
    "You look down at your notebook one last time. The maps are smudged but legible. Your hand hovers over inked lines like a finger over a wound."
    "How do we respond to the surge's aftermath?"
    return
