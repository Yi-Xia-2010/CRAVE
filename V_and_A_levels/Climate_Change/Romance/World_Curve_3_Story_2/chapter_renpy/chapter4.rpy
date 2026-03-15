label chapter4:

    # [Scene: Saltmarsh Wetlands | Dawn]

    scene bg ch4_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft slap of mud under boots, distant gulls, a low, steady surf.]
    # play music "music_placeholder"  # [Music: Nervous strings, tempo quickening beneath the wind.]
    "You planted your feet in the soft, spongy edge where reed meets water, clipboard cold against your palm. You can still feel the council chamber's silence in the back of your throat — the public endorsement"
    "you offered for the living-breakwaters, the promise of a pilot ringing like a bell you can't unring. Prof. Noor is beside you, palms pressed into mud-streaked gloves, eyes calm as a tide chart."
    show prof_noor_azizi at left:
        zoom 0.7

    prof_noor_azizi "Good morning, Maya. The pH strips are back from the lab; salinity's within expected variance. If we get the volunteers through two full transects today, we'll have baseline coverage."
    "You let the sentence settle. Baseline coverage: two small words that mean the difference between a defensible pitch and an argument that opens doors for Elias. Your braid catches in your glove when you tug your sleeve; the salt line along it looks like a map of obligations."
    hide prof_noor_azizi

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rasp of stakes being driven, muffled laughter, the thud of oyster bags hitting wet earth.]
    show ben_harper at left:
        zoom 0.7

    ben_harper "Steady now. Let the stake bite slow. Don't rush the angle. The marsh will give if you force it."
    "Ben's hands are slow and sure, the kind of hands that carry memory. You watch him tamp a stake, then pause, watching the line of foam where night met land. Something tightens in your chest, and"
    "for an instant a younger face flashes there — your brother's grin before the flood that took him. You swallow it down with the wind."
    show rosa_tan at right:
        zoom 0.7

    rosa_tan "Maya! We got the bakery team covering the eastern transect. They're asking about the oyster sacks — do you want them laid farther out?"
    "Rosa's voice is a thread pulling the field toward action. She is all momentum today; her yellow jacket a flag against the gray. You turn, the clipboard tilting as you check the map Noor pinned up against the old boathouse."
    show maya_soler at center:
        zoom 0.7

    maya_soler "Two meters farther, Rosa. But—' (you pause, because every 'but' is a hinge) '—no shallower than the last high tide line. We need the root cover to be undisturbed."

    rosa_tan "Understood. We'll mark it. The town's watching, Maya. People are saying today decides whether we mean it or not."
    "A hum from above cuts through the murmurs, metallic and precise. A small drone skirts the low fog, its camera eye a steady black. It drops like a shadow and then hangs, recording. Below it, a"
    "glossy brochure flutters on the boardwalk, weighted by a small stone — Elias Voss's emblem embossed at the corner."
    # play sound "sfx_placeholder"  # [Sound: The drone's whir; paper settling onto wet wood.]
    hide ben_harper
    hide rosa_tan
    hide maya_soler

    scene bg ch4_453e40_3 at full_bg
    "From the drone rises a recorded, perfectly modulated voice, the cadence of an advertisement more than a human heart."
    show elias_voss at left:
        zoom 0.7

    elias_voss "Elara deserves certainty. A engineered seawall secures harbors and businesses immediately. No guesswork. Jobs, investment, protection."
    "The volunteers fall quiet. The word 'immediately' lands like a hand on everyone's shoulder. A few nod. A few frown. The drone angles its lens toward your group, a small mechanical eye expecting a reaction."

    menu:
        "Flag the drone and ask it to leave":
            "You flag it with your hand, angry and small; the drone hums away a short distance but stays. The brochure's glossy promise doesn't flutter away."
        "Let it film and focus on the volunteers":
            "You look past the drone and meet Ben's steady hands; the volunteers breathe out and keep working, but the camera's eye keeps you in its frame."

    # --- merge ---
    "Continue"
    "You feel the air press harder now, as if the marsh itself leans in. Noor places a gentle hand at the small of your back — a practice less for your body than for the tremor in your resolve."
    show prof_noor_azizi at right:
        zoom 0.7

    prof_noor_azizi "They'll edit — they'll try to make this into a soundbite. We have to be careful what they can spin. But footage helps us too. Use it; don't feed it."
    show maya_soler at center:
        zoom 0.7

    maya_soler "Use it how? We need momentum and accuracy. Both at once.' (You force your voice steady; it cracks like ice under foot.) 'Storm season's months away and not a lot of months, Noor. If we don't show immediate progress, Elias will flood the town with 'safe' images and 'guaranteed' timelines."

    prof_noor_azizi "I know. But hurrying tests means we might miss crucial variability — the ebb during a spring run could change our results by thirty percent. Thirty percent is a world."
    "Noor's words are small, precise. They make a map of the stakes: accuracy versus timing. The marsh smells of cold peat and old salt, and when you breathe, you taste iron."
    "Aiden Kuro walks the perimeter, hands in the pockets of his patched oilskin, gaze like tide-light on the water. Salt crust flakes along his cuffs; his jaw is cut with worry. He moves slow, the way a man measures the sea by muscle memory."
    hide elias_voss
    show aiden_kuro at left:
        zoom 0.7

    aiden_kuro "If you push this out fast, will it push my traps? We set a line off Cutter's Point — last autumn's sediment still hasn't settled. If you place breakwaters, it could change the run."
    "Maya Soler: (shrugging a weight you can't fully unstrap) 'We're placing living breakwaters with oyster beds and native marsh plantings, not concrete pylons. The plan reduces nearshore erosion.'"

    aiden_kuro "Words don't stop a trap from going dry, Maya. Words don't put fish back in a net when the current changes. You promised we wouldn't lose our season."
    "You can hear the accusation float under his sentence. It's not meant to wound you — it's meant to keep a life from slipping away. Your throat tightens. The image of your brother's face returns —"
    "not just a memory now, but a ledger of what happens when promises meet the sea."

    menu:
        "Show Aiden the transect map and point out compensation lines":
            "You flip the clipboard and trace the lines with your finger. His eyes follow; for a second he lifts his chin, measuring the math against memory."
        "Admit you don't have all the answers yet":
            "You lower your voice and say it plainly: you don't have all the answers. His jaw softens and hardens in the same breath; trust nudged, not mended."

    # --- merge ---
    "Continue"
    "Aiden leans forward, so close you can smell the salt and last night's smoke from his boat. His hand brushes the edge of your clipboard — a contact more like a plea than anything else."

    aiden_kuro "Don't do this alone, Maya. You're not the whole town."

    maya_soler "I know.' (You want to mean it more than you do.) 'But if we don't start — now — we might not get the funding. Noor says we need baselines before the storms. If we can show improvement in root cover and fauna return within weeks, that—"

    aiden_kuro "Then those weeks better not trade our October for someone else's uptown café. Promises like 'improvement' are easy to sell if the buyer doesn't fish."
    "Your voice narrows; the marsh seems to lean with his words. Rosa approaches, breathless, pulling you aside."
    hide prof_noor_azizi
    show rosa_tan at right:
        zoom 0.7

    rosa_tan "They're setting up a pop-up on the boardwalk. Elias reps are handing out the brochure. They're framing it like 'no guessing, no wait.' People are already asking which one of you has the money."
    "Rosa's accusation lands with heat. She is the one who can turn simmering doubt into flame; she knows how to stoke the town because she is the town's thrum. Your pulse spikes. You can feel the"
    "arousal building — not chaotic yet, but intense; each person's worry a small wave and you in the center of a gathering storm."
    "Ben walks over, mud still under his nails, eyes angled toward the water. He does not romanticize the sea. He remembers things in a way that cuts sharper than a headline."
    hide maya_soler
    show ben_harper at center:
        zoom 0.7

    ben_harper "When the harbor wall went up forty years ago, they said it'd be 'safe for a century.' Boats moved farther out. The tide shifted where it wanted. We lost three lines of traps that year. Engineering's got answers, but the sea keeps asking different questions."
    hide aiden_kuro
    show maya_soler at left:
        zoom 0.7

    maya_soler "So you trust the living option?"

    ben_harper "I trust what puts life back on the mud. It's what teaches the mud to hold. But trust ain't a blindfold."
    "Noor folds a waterproof map in her hands like a prayer."
    hide rosa_tan
    show prof_noor_azizi at right:
        zoom 0.7

    prof_noor_azizi "Funding follows momentum. The grant board cares about demonstrable outcomes, not good intentions. If we can fast-track the installation of the oyster bags and get the transects in before the next spring run, the data will speak. But rushing means less replication, less margin for error."
    hide ben_harper
    show rosa_tan at center:
        zoom 0.7

    rosa_tan "And Elias will spend ten times what you have on curated certainty. Brochures and a seawall render — people hear 'protection' and they think certainty. We need stories on the boardwalk: fishermen, bakers, mothers — people seeing that nature works with us."
    "You take in the faces: volunteers bending, a teenager clutching a stake like a spear, Noor's patient set jaw, Aiden's clenched fists. The wind makes the marsh reeds lean and the drone whistles like a needle threading a seam of doubt."

    menu:
        "Walk to the boardwalk to confront the brochure and speak to Elias's rep":
            "You walk toward the brochure and its polished lies. The rep smiles too-wide and hands you a laminated fact sheet. You answer with data and tone; she replies with corporate cadence."
        "Return to the volunteers and keep the data collection moving":
            "You pivot back to the field, voice raised to organize teams. The drone follows, but the work picks at the town's attention like a steady tide."

    # --- merge ---
    "Continue"
    "Your palms sweat into the clipboard. Leadership is no longer a checklist; it's a ledger of people's livelihoods, promises, and grief. You see, as plainly as the tide maps in your notebook, the choice before you:"
    "push so hard that the pilot begins immediately and risks missteps; widen the pilot into a deal that nets the town's businesses but could dilute ecological integrity; or insist on extended testing that protects scientific rigor"
    "but hands Elias more time to sell his certainty."
    "Noor meets your eyes; there's something rounded in her expression — not relief, but an understanding of the costs."

    prof_noor_azizi "If you move too quickly, mistakes stick. If you move too slowly, hearts and livelihoods can be convinced elsewhere. You have to pick what you can live with, Maya. And what the town can forgive."
    "You think of your brother again, of promises made to a brother who couldn't be saved. You think of every time you refused help because you wanted to be the one to fix things, and how often that refusal made other people shoulder burdens you could have shared."
    "The drone dips lower, and for a moment its shadow falls like an accusation. The sky thickens; the tide growls something close to a warning. Voices cluster into a low hum that vibrates through your teeth."
    "You feel the arousal climbing — the drumbeat of urgency, the narrow band where time and consequence meet."
    "You roll your sleeves up, braid catching a stray salt-streak. The marsh smells of peat and rain waiting to fall. Your mouth tastes of metal and the sea-wind."
    # play music "music_placeholder"  # [Music: Strings tighten into a sharp, sustained note; tempo accelerates.]
    # play sound "sfx_placeholder"  # [Sound: Distant surf louder now; a gull cries and cuts off.]
    "You breathe in and out once, and find the point where decision begins."

    menu:
        "Fast‑track the pilot and start construction this week.":
            jump chapter5
        "Broker concessions for small businesses to ensure economic buy‑in.":
            jump chapter6
        "Insist on Prof. Noor's extended testing before any public works.":
            jump chapter5
    return
