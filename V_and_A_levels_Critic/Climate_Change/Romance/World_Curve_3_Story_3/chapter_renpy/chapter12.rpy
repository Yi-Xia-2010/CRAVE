label chapter12:

    # [Scene: Tomas Rivera's Kitchen | Late Night]

    scene bg ch10_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: A tense piano motif, fingers scraping toward a cadence; strings hum beneath, thin as gull wings.]
    "You keep your jacket on. The mud at the hem is still damp from the marsh boardwalk; it smells faintly of peat and salt. Tomas watches you fold your hands as if folding a map—careful, deliberate."
    "Jonah Kade stands in the doorway, shoulders shaded by the night, coat still smelling of diesel and seaweed."
    show tomas_rivera at left:
        zoom 0.7

    tomas_rivera "You sure about this, niña?"
    "He says it like he is asking the tide itself."
    show maia_rivera at right:
        zoom 0.7

    maia_rivera "I am. But not yet public."
    "Your voice is small in the room and immediately raw with the effort of secrecy. 'Ava found things. I need to know if they're mistakes or deliberate.'"
    "Jonah Kade steps forward."
    show jonah_kade at center:
        zoom 0.7

    jonah_kade "You told anyone else?"
    "You shake your head. Your mouth tastes of metal. 'Only you and Tomas. For now.'"
    "Jonah Kade's jaw tightens; he says the next thing slow."

    jonah_kade "If this stalls funding, people will—"
    "He swallows. 'They'll lose nets. They'll lose nights where they sleep without worrying.'"
    "Maia Rivera: You hear the fear in the cadence and it lodges under your ribs like a stone. 'I know.' You want to say everything—why this matters, why the clauses should make anyone who calls themselves"
    "a neighbor sick—but the words tangle. Instead, you lay your palm onto the table. 'I need time to be sure.'"
    "Tomas reaches over and taps the worn wood twice, his knuckles a small metronome. 'Time is fine, so long as we do not wait past the weather,' he says. His eyes hold the memory of other tides."

    menu:
        "Put a hand on Jonah's forearm":
            "You squeeze once. Jonah's shoulders loosen for a breath, then he'll pull away—it's the harbor's rhythm in him: trust, then watch."
        "Step back and give Jonah space":
            "You step back. Jonah reads your retreat; his expression hardens. He thinks you're choosing the town over him—maybe you are."

    # --- merge ---
    "Both outcomes return to the main narrative."
    # [Scene: Ava's Field Van | Midnight]
    hide tomas_rivera
    hide maia_rivera
    hide jonah_kade

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The van's small heater sighs; somewhere outside, a gull argues with the dark.]
    # play music "music_placeholder"  # [Music: A high, anxious violin line threads tension through silence.]
    "Ava slides the tablet across the cramped counter. Her hair is a ragged black halo, cropped and damp; exhaustion rims her eyes like bruises. The data lights up in a scatter of colors—rows of numbers, three-dimensional sediment maps, model runs spinning like small, indifferent planets."
    "Ava: She exhales. 'I ran it through three alternate parameter sets and a blind re-sample. The firm used a smoothing algorithm that masks episodic displacement. They down-weight events where they ran out of transects.'"
    "Maia Rivera: The words land like a bucket of cold water. 'They...smoothed out the spikes?'"
    show ava_kim at left:
        zoom 0.7

    ava_kim "Yeah. They made high-displacement events statistically improbable. Look—here."
    "She taps a hotspot. The map blooms: a trough of removed sediment volume, annotated with timestamps. 'If you remove those events, the model predicts much less turbidity and thus less impact on juvenile fish habitat. But those events are real. We saw them in the field logs.'"
    "You lean in until the tablet fills your vision. The smell of recycled coffee in the van makes your stomach twist. Your hands tremble."
    "Ava: Soft, steady. 'There's more. The migration models assume a thermal corridor opening that the fisheries team told me they never observed last season. And—'"
    "She swipes. A contract clause appears: text dense and clinical. 'This is the kicker: a clause that gives the 'Project Consortium' final oversight on adaptive fisheries measures. It effectively puts decision-making power about fishing zones and quotas into the hands of corporate partners.'"
    "Maia Rivera: Your throat goes dry. Air presses hard against your ribs as if the van itself is in low tide. 'They'd have legal control over local fishing decisions.'"
    "Ava nods. 'Legal control and the right to override local measures if they 'optimize project outcomes.' It's not a misread. It's baked in.'"
    "You feel your heartbeat quicken—thud, thud, too loud in the small metallic box. Outside, wind ratchets up; rain patters harder against the van."

    menu:
        "Ask Ava to print everything now":
            "You press the idea out, urgent. Ava hits a button; the van's small printer whirs like a small protest. Physical pages make the danger feel more real."
        "Tell Ava to encrypt and back up the files":
            "You say it quietly. Ava's fingers fly over the screen. Files duplicate; a backup twines into the cloud. She gives you a look—relief and a new worry mixed."

    # --- merge ---
    "Both outcomes return to the main narrative."
    # [Scene: Offshore Project Site | Early Morning Tour]
    hide ava_kim

    scene bg ch10_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant throb of generators; boots on grated metal; the sea slaps rhythmically against pilings.]
    # play music "music_placeholder"  # [Music: Percussive electronic beats woven with tense brass; the tempo accelerates.]
    "You and Jonah Kade join the firm's guided tour under the pretense of goodwill. Elias Wren stands at the center of his engineered world—his trench coat clean, his watch catching the hard light. He smiles the measured smile of someone used to smoothing friction with data."
    show elias_wren at left:
        zoom 0.7

    elias_wren "Maia—Jonah. Thank you for coming. We wanted you to see our mitigation measures first-hand."
    "He gestures at a neat line of silt curtains and engineered berms. 'Transparency is important to us.'"
    "Maia Rivera: The word sits between you like a buoy. It feels both honest and performative. 'Transparency is why we're here,' you say. Your voice is even. Your hands are not."
    "Elias Wren inclines his head."

    elias_wren "Good. Ask anything."
    "You walk the walkways—metal vibrating underfoot—and watch technicians pin sensors. The site smells faintly of oil and plastic; the smell is alien to the marsh you know. Jonah Kade's fingers absently trace the brass fisherman's ring at his belt."

    "Maia Rivera: You catch Jonah Kade watching the water, expression closed. He leans to you" "If this is a show, don't let them fool the town."
    "Maia Rivera: You want to say—how will I stop them if the town claps? But you don't. Instead, you steer the conversation back to specifics. 'The sediment displacement numbers—how do you account for episodic storm-triggered slugs?'"
    "Elias Wren: His answer is smooth. 'We model extreme events probabilistically and include adaptive sediment traps. Our interventions reduce net displacement by twenty percent in projected scenarios.'"
    "Ava, hiding behind the guise of a curious technician, interjects with a clinical tone that betrays her exhaustion."
    show ava_kim at right:
        zoom 0.7

    ava_kim "Can you show the un-smoothed outputs? The raw transect logs?"
    "Elias Wren: A flicker of something—annoyance?—crosses his face. 'We use industry-standard smoothing to create robust, interpretable outputs. Raw logs contain noise that misleads stakeholders.'"

    ava_kim "Noise is often the thing that tells you when systems fail."

    elias_wren "We can't make decisions based on anomalies that are statistically insignificant."
    "You: For a second, the sea seems to hold its breath. The wind lifts and the AR schematics flutter like paper birds. Inside your chest, your guilt starts to flare hot—there is a truth you conceal"
    "from most of them, a truth that feels like it might save or ruin people."

    elias_wren "If you have technical questions, we'll be happy to provide appendices."
    "He means the polished ones; you read the subtext."
    "You: You watch everything—his posture, the way his team avoids looking at the old pilings, Jonah Kade's hands opening and closing. The storm-clock in your stomach ticks faster."
    # [Scene: Quieter Corner of the Site | Overlooking a sluice]
    hide elias_wren
    hide ava_kim

    scene bg ch10_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The ocean whispers, more urgent now; gulls cry like alarm bells.]
    # play music "music_placeholder"  # [Music: A rising string tremolo that tightens into a staccato pulse.]
    "Ava drags you aside, tablet clutched like a small weapon. With the generator hum as a background, she lays out the anomalies again—this time framed against the site itself. Her voice is low but urgent."
    show ava_kim at left:
        zoom 0.7

    ava_kim "They dropped three transects after a storm without notation. The sediment models then redistributed mass across a larger area to keep peak values down. They effectively diluted the visibility of episodic displacement."
    "You look at the sluice below. You can almost see the patterns in the mud, the places Tomas showed you as a child—the hollows where fish hide. The tablet shows migration curves that arc optimistically toward recovery within two seasons. The field notes say otherwise."
    "Maia Rivera: Your throat tightens until words push like tidewater. 'If their models are wrong, juvenile nursery habitat could be wiped. That's generations of fish.'"
    "You taste bile. 'And the clause—if we sign, they can change fishing zones.'"

    ava_kim "They can essentially reassign access in the name of 'optimized outcomes.' We lose management control."
    "You: The edges of your vision pulse with a white-hot sense of impending collapse. The rain comes harder now, a curtain. In the distance, an announcement crackles—some logistics update—and the generator coughs."
    "Dana appears, breathless from a sprint across the site. Her ponytail is plastered to her cheek; protest paint is still faint under her nails. She tosses a sheaf of copies onto the sluice's rail."
    show dana_park at right:
        zoom 0.7

    dana_park "You found it, didn't you?"
    "There is no room for subtlety in her voice. 'You did a quiet audit. Good. We need to blow it open. Town hall—now.'"
    "Maia Rivera: The word 'now' is a hammer. Your brain lists consequences in a staccato: funding pulled, construction halted, angry investors, legal pushback, possible lawsuits. But also: truth. Also: trust. Also: danger avoided."
    "Jonah Kade finds you at the rail, now very close. He looks like someone who has been at sea too long and finally sees a storm on the horizon."
    "Jonah Kade: He speaks barely above the wind. 'If we go public and the state funding pulls, do you know what that does to Lupe and the cooperative? To nets, to iceboxes, to kids who need schoolbooks? There are people who will be on the hook tonight.'"
    "Maia Rivera: Exposure feels like ripping a bandage. Quiet negotiation feels like suturing in the dark. Delay for more evidence feels like tucking the truth in a drawer. All options press at your chest like waves."
    "Tomas arrives—slow, steady, as if the town's history walks in with him. He lifts his chin when he sees the tablet, reads it, the lines of his face deepening."
    show tomas_rivera at center:
        zoom 0.7

    tomas_rivera "Maia."
    "He sets his cane against the rail, his voice steady. 'People will hurt either way. But lies in contracts make for slow poison. If it's in writing, you can't un-mean it later.'"
    "Maia Rivera: The guilt swells, an ache that is physical—you feel it like a tightening band around your ribcage. This audit was meant to clarify the path; instead it has put you at a crossroads that could split Marisol Bay along fault lines you neither designed nor wanted."
    "Ava bows her head, voice small and fierce."

    ava_kim "We can expose the compromises and risk the funding. Or we use this to negotiate and keep things moving—but will they bargain? Or will they stonewall? We can keep collecting evidence, but the storm timetable is compressing. There isn't much time."

    dana_park "No. We expose. We make noise."
    "Her hands carve the air, punctuation for urgency."
    hide ava_kim
    show jonah_kade at left:
        zoom 0.7

    jonah_kade "And then what? The town will either thank you for saving them later, or they'll watch kids go hungry now and curse your name. I'm telling you—this isn't just politics. This is nets. It's lives."
    "You: Air tastes like iron. Your heartbeat has become a drumroll. The rain hammers the sluice. The AR schematics on Elias Wren's lapel glow like a challenge."
    "Your mind races, assembling possible futures into blunt-edged images: a loud town meeting lit by projector light and shouting; a backroom bargaining session with Elias Wren in which every point you extract is paid for in"
    "a concession; quiet nights of poring over logs until the next storm finds you with more proof—or too late."
    "You stand there, feeling the town press in around you—its boats, its stories, its small, brittle economies. You can almost hear the gulls make a shrill, single syllable: choose."
    # play music "music_placeholder"  # [Music: The strings peak into a fraying, urgent chord; percussion hammers like a mounting tide.]
    # play sound "sfx_placeholder"  # [Sound: A generator hiccups; then, a wind gust as if turning the page.]
    "You inhale until the ache settles into a hard readiness. The choice is not abstract. It is a lever that will tilt lives."

    menu:
        "Expose the compromises publicly now.":
            jump chapter13
        "Attempt to renegotiate clauses privately, using the audit as leverage.":
            jump chapter14
        "Delay and continue collecting evidence to build an airtight case.":
            jump chapter14
    return
