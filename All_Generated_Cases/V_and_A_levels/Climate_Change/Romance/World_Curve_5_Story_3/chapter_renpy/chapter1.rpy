label chapter1:

    # [Scene: Tide Lab | Pre-dawn]

    scene bg ch1_Start_1 at full_bg
    # play music "music_placeholder"  # [Music: Low ambient hum — a distant synth that breathes like tide breath]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, soft drip of water from a bench, a faint mechanical beep from a sampler]
    "You are alone with the tide until the lab insists on being otherwise — with glass and stainless steel and the patient clink of jars. Your hands know the work: the brass compass cool against your"
    "palm, the weight of the Moleskine under your elbow, the rasp of a pencil nib as you count barnacle bands beneath a magnifier. Each motion is measured, a small ritual against unpredictability."
    "The dataset from Professor Haruto sits open on the monitor in front of you: rows of salinity readings, annotated satellite passes, a scatter of notes in his cramped type. You reconcile his timestamps with the field"
    "samples laid out on a tray — vials of water ringed in frost, a strip of mapped tide-lines you rubbed off an old piling. You trace a line in the notebook and write: section D —"
    "anomalous salinity spike. Your handwriting is small and careful, like a tide mark pressed into paper."
    "Smell: salt and antiseptic, wet wood and the faint oil of an old chart table. The bench under your forearms is damp where you rested your elbow; the brass compass leaves a faint, warm ring on"
    "your palm when you roll it between thumb and index finger. It is your father's every time you hold it. He taught you how to read the horizon by paying attention to small changes — wind,"
    "flicker, the way barnacles stack. You press the compass against your lips for a moment and then tuck it beneath the page."
    "A memory comes unbidden: Tomas Reyes on the pier, his voice like a salt-worn radio. 'Mark the banding, kid. The sea don't lie if you listen.' The day the storm took him is a flat, gray"
    "shape at the edge of everything you do. You do not need the memory to be recent to feel its pull; it underwrites your motions, the way you measure and do not let numbers become comfort."
    "You bury grief in methodology. It keeps things tidy."

    scene bg ch1_Start_2 at full_bg
    "Professor Haruto's latest note is a voicemail, soft and thick with his slow, careful cadence. You hit play with a thumb, more to hear the voice than to learn anything new."
    show professor_haruto_miyazaki at left:
        zoom 0.7

    professor_haruto_miyazaki "Maya — I pushed the model through the night. Look at the D-series cross-correlations. There's a pattern, subtle, but there. And Maya, don't forget why you started these counts. Tomas used to laugh at my tea; he trusted the pier more than I ever did. Bring that with you."
    "You listen and pretend not to answer aloud. In your head you say back the same thing you always do to his reminders: I know. You fold the voicemail into the dataset and let it settle like silt."
    # play sound "sfx_placeholder"  # [Sound: The lab's side door opens softly; wind carries in a breath of colder air and the richer smell of coffee]
    "Elias Rowe arrives the way he does — with quiet motion, a thermos clutched under one hand and his sketchbook tucked under the other arm. The denim jacket is damp at the collar, his hair tousled"
    "as if the wind had rearranged a planning diagram. He sets the thermos down and uncaps it, the hiss of steam a small, human punctuation."
    show elias_rowe at right:
        zoom 0.7

    elias_rowe "Morning, Maya. I brought something to keep the night data from turning into a horror film."
    "You watch as he offers the thermos with a half-smile."
    "You look up. He notices the silver strand at your temple — the one that always betrays you when the light hits it — and you, reflexive, tuck it under the frayed floral scarf tied loosely"
    "around your neck. His amber eyes narrow in a way that is both question and appreciation. He leans against the counter in a posture that says he isn't intruding, only waiting."
    show maya_calder at center:
        zoom 0.7

    maya_calder "You know it only becomes a horror film if you let the timeline get ahead of you.' (You tap the notebook gently.) 'Haruto's D-series has a flinch. I'm trying to see if it's model error or something physical."

    elias_rowe "Model error or stubborn ocean — the eternal debate."
    "He flips open his sketchbook and the corner of a watercolor peeks out. 'Also, I brought backup: plausible things that won't make Serena smile but would make the Greenline look better. Sit down, look.'"
    "You keep counting, but your eyes stray to the watercolor. It's a simple cross-section: marsh grasses, a tethered mat of oyster shells, a gentle berm of recycled timber. No concrete seawall, no vertical lines. The brushwork"
    "is patient — he painted as if he were describing a gentle weather, not an argument."

    elias_rowe "A small demo on the Greenline pier. People see plants, not acronyms. If we show the town we can do it without a hundred-meter-long concrete finger, maybe they stop listening to the sales pitch."
    "Maya Calder: (You run a finger under the last tide mark you've inked.) 'A demo is seductive. Shows are persuasive. But demonstrations are not proofs. They can make people feel better without guaranteeing safety.'"
    "Elias watches you annotate a line on the monitor, then shifts, a rhythm familiar and slow. His voice has the soft quickness of someone sorting through tools for the right one."

    elias_rowe "True. But neither is a glossy promise from a firm with a line of investors. One shows people how to live with the tide. The other buys time for someone else's ledger. Which one would you rather explain to Tomas' granddaughter?"
    "He isn't being rhetorical; he means the town in very human detail."
    "The name pulls another weight in you, something heavier than method. You taste metal — the compass again — and the lab seems to hold its breath. Your hands slow."

    menu:
        "Tell him about the compass — let him see why this work is personal":
            "You slide the brass compass across the bench to him, its surface dull with years. Elias turns it over in his palms, and you watch his face rearrange into a softer expression, as if he's found the small hinge that opens the rest of your sentences."
        "Keep it to yourself — let the work speak for why you care":
            "You tuck the compass beneath the notebook, fingers pressing the leather. Elias nods, eyes lingering on your scarf; he doesn't press you, but there's a quiet question in how he straightens his sketchbook and sets it back down."

    # --- merge ---
    "The scene continues."
    "You let the choice sit like a tide pool, small and reflective, then return to the data. Elias respects the pause; he knows the lab's boundaries. He is patient in a way that fits his work — civil design needs patience with materials and with people."

    elias_rowe "Serena will be at the meeting, right? Marine-blue and a tablet. She angles for speed."
    "He taps his sketchbook to emphasize a point. 'I don't want to make enemies, Maya, but I also don't want us to watch a wall cut the town in half while they count their margins.'"

    maya_calder "Serena's offer is tempting to people who fear immediate loss. It's engineered certainty. But her models assume a rigid coastline. The coast doesn't keep the promise."
    "Your voice is low. The lab's hum seems louder in the pause."
    "Elias leans forward, scribbling a quick note in the margin of his watercolor. He draws a tiny figure standing on a boardwalk, holding a child's hand. The gesture is small but exactly his: translating stakes into human scale."

    elias_rowe "Then show them the human scale. Bring the water, bring small—bring Tomas' story if you must. People remember faces."
    "You close your notebook for a breath. The motion is deliberate. The condensation on the far window has stitched a faint new map that looks like the ribcage of something sleeping."

    menu:
        "Accept the thermos — take a sip and let the small comfort steady you":
            "You take the thermos and let the heat strike the center of your chest. Elias watches the way your shoulders loosen imperceptibly, as if the coffee smooths an inside wrinkle."
        "Decline — caffeine will only speed the already quick thoughts":
            "You hand the thermos back with a dismissive smile. Elias shrugs and sips; the steam curls and you watch the motion as if it were a small experiment in patience."

    # --- merge ---
    "The scene continues."
    "Elias studies you, then the monitor, then the jars arrayed like a small inland sea."

    elias_rowe "Have you had a reply from Mayor Sol? Or is this still Haruto-hour and not politics-hour?"

    maya_calder "Mayor Sol has her own calculus. Votes and safety and what looks good on a press release. Haruto's data gives me a different lens — it suggests where reinforcement will fail under compounding salinity. The seawall looks like certainty on paper; in the long run, it changes the chemistry. I need Haruto's cross-correlation to be a fluke and not a trend."

    elias_rowe "And if it's not? If your careful cross-correlation is the warning bell?"
    "You swallow. The lab air tastes like metal. You think of the pier as it used to be: weather-beaten planks, Tommy's laugh cutting through fog, nets drying like pale flags. You think of the certificates of"
    "protection Serena will hand around with practiced palms. You imagine the Greenline with living mats of oysters and salt grasses, quiet and slow, doing the work of decades in the patient way ecosystems do."
    "For a moment, neither of you talks. You measure the silence like a scientist measuring a control."

    elias_rowe "I have plans for a small mock-up. Nothing fancy. If nothing else, it will give people a tactile thing to vote for."
    "He taps the sketchbook. 'I'm going to talk to Lina. She can make people come.'"
    "You feel the inertia of endless meetings and the slow erosion of momentum when everything is decided in committee. And yet — small things pull. A child's hand on a boardwalk. Tomas' voice. The compass in the palm of your memory."
    "You reach for your Moleskine, fingers finding the page that lists tonight's agenda: Harbor meeting. Community demo proposals. Serena Voss's bullet points. You make a line through something that smells like a promise."
    "You think of the meeting room: long table, plaintiff lights, the way a single tablet can dominate a conversation. You think of Serena's marine-blue suit hanging over every conversation like an approaching weather front, clean lines and confident gestures that smooth doubt."
    "Professor Haruto's voicemail plays again under your breath, less as instruction and more as motive: don't forget why you started."
    "Your thumb closes the notebook."
    hide professor_haruto_miyazaki
    hide elias_rowe
    hide maya_calder

    scene bg ch1_Start_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The ambient hum thins to a single, steady note — an implied heartbeat in the lab's machinery]
    "You make the choice there, not with fanfare but with a small, irrevocable motion: you will go to the Harbor meeting. It is not a salvo; it is a decision to be present, to carry your measurements into a room where numbers must live with people."
    "You stand, the chair scraping a soft, final sound on the wet floor. Elias folds his sketchbook, a gentle smile that is equal parts worry and encouragement."
    show elias_rowe at left:
        zoom 0.7

    elias_rowe "Good. Bring the compass if you want. Or not. Just bring yourself."
    "You tuck the brass beneath the notebook again, feeling its corner bite into your palm, and breathe the lab into yourself one last time before stepping toward the door."
    hide elias_rowe

    scene bg ch1_Start_4 at full_bg
    # play music "music_placeholder"  # [Music: The ambient hum resolves into a single, sustained chord that invites forward motion]
    "You reach for the door handle and feel the cold metal under your fingers. The meeting waits across town, and the tide, as always, will keep its own counsel."

    scene bg ch1_Start_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter2
    return
