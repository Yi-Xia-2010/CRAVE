label chapter5:

    # [Scene: Tideworks Lab | Dawn]

    scene bg ch5_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant tug horns, the metallic rasp of rigging, a low rhythmic hum from charging equipment]
    # play music "music_placeholder"  # [Music: Sparse, minor-key piano; slow undercurrent]
    "You wake to the lab's breath — heaters cycling, the faint electric pulse of sensors booting. The air tastes of salt, algae, and hot metal. Your jacket is still damp where the ocean spray soaked through yesterday; the frayed cord of your compass brushes your sternum like a nervous hand."
    "Theo is there before you fully arrive, knees flecked with paint, fingers wire-scorched, cursing affectionately at a sensor cluster. He looks up when you step in, eyes bright but rimmed with fatigue."
    show theo_mendes at left:
        zoom 0.7

    theo_mendes "Morning. We moved the larger modules up from Bay Three overnight. More sensors this run. The funders wanted a bigger show."
    "You listen to the words and feel the sentence translate into ledger entries in your head: more sensors equals more data, more data equals leverage, leverage buys deployment. Everything becomes arithmetic when you are tired enough."
    "Elias Navin stands tucked against a workbench, hands deep in his field notebook. He smells faintly of seawater and lemon oil. His wristband blinks a soft, methodical green."
    show elias_navin at right:
        zoom 0.7

    elias_navin "We scaled the modules as requested. Structural laminates adjusted to the new template. Theo ran an initial load simulation overnight — the models hold."
    "He says the last phrase with the care of someone who still understands how mortality can ride in simulation margins. You look at him and feel two things: gratitude that he came back to fight with"
    "you, and a cold dread that the numbers might be the only thing that saves you."
    "You move to the nearest module and run your palm along the cold composite — ridges, sand trapped in seams. The smell of curing resin rises, sharp and chemical. Tiny, almost invisible, a hairline scrape on"
    "an anchor plate catches at your eye. The lab is full of small things that might mean nothing, or might mean everything."

    menu:
        "Run a quick stress reading on the anchor now":
            "You pull a handheld scanner from your jacket and press it to the plate. The display blinks irregularly; you record the discrepancy and make a note in the margin of your notebook."
        "Trust Theo's calibration and move on":
            "You force a smile and step back, letting Theo finish. You file the scrape as 'to watch' and your stomach tightens, as if the sea itself pressed at your ribs."

    # --- merge ---
    "Continue"

    theo_mendes "If that reading's off, I can recalibrate. It'll take an hour tops. But the barges leave on schedule."

    elias_navin "An hour could mean... we lose the deployment window. The current tidal window is narrow, and our permit only covers this stretch for two days."
    "Theo: (shrugs) 'Depends on whether we prioritize a clean run or a good run.'"
    "You want to say: prioritize people. You stop yourself; it is a refrain you keep for council rooms, not for morning shims of aluminum and bolts. Saying it here feels like shouting into a closed engine."
    # [Scene: Harbor | Midday]
    hide theo_mendes
    hide elias_navin

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Hoists creaking, boots slapping on wet wood, muffled conversation over two-way radios]
    # play music "music_placeholder"  # [Music: Low strings; a tension that tightens as the tide pulls outward]
    "The funders arrive mid-morning. They are clean by comparison to the lab: tailored waterproofs, smooth palms that have never touched a rope. A woman with a discrete earpiece and a smile that rehearses itself steps forward with a binder of metrics."

    "Lena" "Good morning. The projections are favorable. We've allocated the second tranche, but only if we see successful deployment within the week. The board is watching."
    "You show her the modules and let her fingers hover over composite. She chooses not to touch. Her voice is the kind used to move money and decisions; it leaves you feeling small and financially ordained."
    show elias_navin at left:
        zoom 0.7

    elias_navin "They're pushing the timeline. If anything fails under pressure, the fallout won't be contained to plaster charts."

    "Lena" "We understand risks. We assumed them when we approved the pilot. The city needs confidence. The quickest path to that is continuous deployment and scaling."
    show theo_mendes at right:
        zoom 0.7

    theo_mendes "We found a few anomalies on the sensor suite last night. Spikes on strain readings in two test bays."
    "Lena's smile narrows like a gull's beak."

    "Lena" "Anomalies are expected at this scale. Correct them iteratively. We need forward motion."

    "You watch the words kineticize in the air" "iteratively"

    elias_navin "We can pause, run diagnostics publicly, show the community the issues and solutions. Build trust through transparency."

    "Lena" "Publicizing every hiccup undermines confidence. If we lose the narrative, we lose funding. The board believes in decisive optics."
    "The lab's lights seem to dim a little. Outside, a gull cries and a ferry coughs. Ivy arrives at the dock, apron still dark with soil; she carries a thermos that smells faintly of cardamom."
    show ivy_kestrel at center:
        zoom 0.7

    ivy_kestrel "Mara—' (she looks at you) 'We can't afford to stall. People are counting on jobs, on wages. Last month there were three layoffs at the slip."
    "She doesn't need to say it: you can feel the ledger of her days stacked in your head. Rosa's face—shadowed under your thoughts—appears in the memory like a warning and a benediction."

    elias_navin "Your call, Mara. If you side with a pause, I can look like the voice of transparency. If you push, we can deliver the metrics that buy us time."
    "His voice is steady, but the pulse at his wristband is suddenly audible to you, a tiny anxious percussion. You realize that for all his faith in data, he's asking you to decide on a variable he can't quantify: human trust."

    menu:
        "Ask Lena about contingency funds and timelines":
            "You press Lena for specifics. She provides conditional figures in a clinical tone; her eyes skim past your face as if you are a line item."
        "Step away and speak privately with Elias and Theo":
            "You pull Elias aside toward a stack of pallets. Theo follows, palms stamped in grease. The three of you speak in low tones, proximity conserving secrets and fears."

    # --- merge ---
    "Continue"

    "Elias Navin (whisper)" "If we keep going and something goes wrong, the narrative will flip overnight. They will call it reckless. They will call us naïve."

    theo_mendes "Or they'll call us heroes if it holds. Either way, it's the gamble. We could retrofit anchors between barges without stopping the whole operation. It'll cost us—time, extra hands, materials—but the funders won't like the delay."
    "You think about the time it would take to retrofit: the extra hours, the calls to rusted suppliers, the need to patch a hundred small vulnerabilities. You also think of the people who rely on those"
    "wages, the kids who need food on the table. The ledger is a cruel balance: safety and time, trust and money."
    # [Scene: Deployment Site / Test Bays | Evening]
    hide elias_navin
    hide theo_mendes
    hide ivy_kestrel

    scene bg ch5_4001e7_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Waves slap the breakwater, a metal groan from a tether, distant conversations muffled]
    # play music "music_placeholder"  # [Music: A slow, descending cello motif]
    "The first anomaly they called 'minor' arrives as a feed on Theo's tablet: a sensor spike, a momentary torque on an anchor, an audio clip of something metallic rasping under pressure. You watch the waveform like a weather report, the peak and the tail."
    show theo_mendes at left:
        zoom 0.7

    theo_mendes "That's a stress chatter. Could be debris, could be structural fatigue. We sent a crew to inspect."

    "Elias Navin (grim)" "We need a full diagnostic. If the anchor's failing, the load redistributes to the adjacent modules. Cascade."

    theo_mendes "And the funders will pull the line if we pause. They asked for scaled rollout, not a slow-crawl pilot."
    "You feel the tiredness that has been gathering in your chest bloom into a low, steady ache. You think of your father's boat listing, of hands on ropes in midnight rain. You promised then to do better. You promised the town you wouldn't allow them to be written over."
    "A live feed crackles: the camera on Bay Four catches a module swinging wider in a sudden gust. The tether whistles. A line shudders. For a second there's a sound you cannot name — the high fret of metal against metal stretched too far."

    "A text pings from Lena" "We expect continued deployment. Do not delay. Board will reevaluate if timeline slips."
    "There is, in that text, the authority that can make or unmake the tiny ecosystem of jobs and livelihoods you've helped build. It is a cold damper on the warm, earthy work you favor."

    "Elias Navin (voice breaking a little)" "We can pause. Make the anomalies public. Show what we found, what we fixed. People deserve to know what we're doing under their feet."

    theo_mendes "That'll sink the funding. The board isn't built for nuance. They'll spin retreat as failure. And lobbying and legal headaches—"

    "Ivy (to you, quietly)" "If they're hiding things, we can't be part of the lie. But if we expose it and the funding pulls, what do we do? Who replaces those paychecks?"
    "You stand between two kinds of storm: one of water and one of consequence. Your hands curl around the frayed cord of your compass as if it could steer you."
    "Elias Navin reaches for your wrist, not to lead, but to steady. His eyes find yours, and in them you see the memory of a mentor lost, the calculation of someone who measures grief with methods."
    "He is not asking you to be his anchor; he is asking you to be the moral compass he has not yet learned to read."
    show elias_navin at right:
        zoom 0.7

    elias_navin "Whatever we choose, we choose together."

    theo_mendes "And we fix what we can if we can. Quiet retrofits buy time."

    "Lena (over the radio; clipped)" "We are not here to entertain delays. Keep deployment moving."
    "The radio clicks off. The harbor makes its own decisions in the clatter of waves and ropes. You realize your choices are not hypothetical; they are the currents that will either steady or snap the lines."
    "Your journal is in your pocket — pages damp but whole. You thumb it and find a pressed strip of seaweed, a note in Rosa's handwriting: 'We remember the shore. Honor it.' The phrase nests heavy in you, a counterweight."
    "You brainstorm aloud, and your voice sounds thin in the wide evening."
    "You think of the people who cannot speak at council hearings: the dockworkers, the single parents, the teenagers who earn spare cash to get by. You think of the calculated coldness of boardrooms and the reputations that can be saved or shattered in a single fiscal quarter."
    "The lab lights hum. The tide is coming in."
    # play music "music_placeholder"  # [Music: A single, unresolved chord holds; the cello descends into near-silence.]
    "You must decide."

    menu:
        "Keep deploying on the funders' schedule.":
            jump chapter6
        "Pause and make the anomalies public.":
            jump chapter13
        "Quietly retrofit anchors and delay the public report.":
            jump chapter6
    return
