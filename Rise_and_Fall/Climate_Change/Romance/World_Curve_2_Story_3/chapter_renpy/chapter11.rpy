label chapter11:

    # [Scene: Tidewatch Lab | Evening]

    scene bg ch11_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, dissonant strings]
    # play sound "sfx_placeholder"  # [Sound: Constant, distant drip of water; the low hum of refrigeration; an alarmingly gentle ping from your tablet]
    "You are in the middle of the work that never felt like the end of anything until it did: compiling a report that has to hold the town's future in a single, fragile spine of evidence."
    "The lamps make puddles on the table. Salt crystals gather in the corner of the north window like tiny fossils of every tide that has come and gone. Your fingers are stained with sample silt; the"
    "nails of your dominant hand bear the gray of lab tape."
    "On the screen, wave-propagation lines blur into topography. Overlays of proposed hard-defense placements flicker against the mapped channels you traced last season. The correlation appears first as a tremor of numbers, then as a pattern that"
    "tightens like a noose: the investor-specified placements, when simulated under the town's tidal asymmetry, increase shear along the narrow channels the juvenile fish use to reach the flats. The models show a persistent southerly deflection that"
    "deepens those channels and hastens scour."
    "You pause, breath shallow, as if the room itself could rearrange and make this less true."

    "Isla Morgan (thinking)" "If this holds, an engineered seawall placed here doesn't just protect a patch of promenade — it changes the river of the sea. It eats the nursery."
    "Your thumb brushes the brass compass at your throat, beneath the edge of your apron, and you feel the weight of the small, familiar circle. Somewhere in the lab a piece of metal taps against wood like a metronome, counting time you do not have."

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The refrigerator hums; a gull call cuts through the rain on the glass]
    "You run the scenario again. The result is the same. You run it with altered tide inputs; same. With slightly different sediment composition; same. The correlation is robust where it needs to be: stubborn, precise, unbearable."
    "Luca Moreno knocks twice and then lets himself in, rain catching in his curls, red bandana darkened with water. He drops a tool kit on the bench like a punctuation mark."
    show luca_moreno at left:
        zoom 0.7

    luca_moreno "You're still here. You always pick the dark hours for the bad news."
    "(He tries to smile; the attempt doesn't reach his eyes.)"
    show isla_morgan at right:
        zoom 0.7

    isla_morgan "It's not— it's not just bad news. It's something that could make a council-approved project actively harmful to the fishing we say we're protecting."
    "(hands tucked into the pockets of your jacket)"
    "Luca Moreno leans over the maps, fingers tracing the same lines you have been afraid to touch. He is quick-eyed, scanning your graphs like he could find an encouraging rounding error."

    luca_moreno "Show me."
    "You point. He reads silently for a long beat, counting the models in his head."

    luca_moreno "Okay. Okay. This is… this is a bomb."
    "(He exhales.) 'We can go to press. We send it to Ravi; we make noise. Investors hate noise.'"

    isla_morgan "If we go to press without peer corroboration, it will be framed as alarmism. Investors will sue, Aria will call it reckless, and the council will—"
    "(Your voice tightens.) 'They'll say 'procedural' and move on.'"

    luca_moreno "Then we force their hand. Public scrutiny stops bulldozers."

    isla_morgan "It might stop them. Or it might make them bury the report entirely and sue us. Or worse — suppress the data. There's legal retaliation to consider. And the models need corroboration; peer review takes weeks. Weeks we don't have."

    "Luca Moreno (frustrated)" "You always look for the clearest answer, Isla. There isn't one here."

    isla_morgan "I know."
    "(You hear the admission like a small fracture.) 'I also know releasing something incomplete could burn the trust of exactly the people we're trying to protect. If fishermen think my work is partisan, they'll stop listening.'"
    "Luca Moreno's jaw works. He runs a hand through his wet hair."

    luca_moreno "So what— we file it and hope the council listens because the universe owes us enough time for process?"

    isla_morgan "Process is how they slow us down. It's how the town gets sold in installments."
    "He slams his palm on the table, soft enough not to damage the prints but hard enough for the vibration to register in your teeth."

    luca_moreno "Then we make a ruckus and make sure the press talks about the nursery channels, not the lawyers. Grassroots can't be sued into invisibility."
    "Isla Morgan: (quiet) 'They can be intimidated.'"
    "The conversation ricochets between you, each phrase a brittle negotiation between your instincts: his urgency, your caution. There is no resolution in the exchange, only the cold awareness that whatever you choose will fracture something — trust, safety, careers, maybe your own life."

    menu:
        "Step outside to the Salt Flats and check the markers in person":
            "You pull on boots, taste salt on your lips, and the immediate clarity of standing where the currents do makes the trade-offs feel heavier. The wind bites and the channels look clearer and crueler in person."
        "Call Aria and tell her you have a complicating result":
            "You thumb Aria's name; before you say anything she asks a single, crisp question. Her voice is polite but unreadable. You fold under the weight of what telling her could cost."
        "Send the data to Dr. Reyes — the external peer — and wait for a reply":
            "You open an email, draft a careful note, and stop. Hitting send feels like pushing a lever; the waiting begins immediately, loud in your chest."

    # --- merge ---
    "Continue"
    "The rain on the windows intensifies. You realize you have made three small, personal choices already today — to stay, to run these models, to tell Luca — and each one narrowed the horizon."
    "Your phone vibrates. A council notification? An investor update? The name on the screen is neither — it's Aria."
    hide luca_moreno
    hide isla_morgan

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A single electronic chime; then silence as you decide whether to answer]
    "You let it ring until it becomes an afterthought. When you finally pick up, Aria Chen's voice is a scalpel wrapped in silk."
    show aria_chen at left:
        zoom 0.7

    aria_chen "Isla. I won't take long. The commission has received word the report will be submitted this week. Are you prepared?"
    "Isla Morgan: (carefully measured) 'There's a complication. A correlation in the models that I can't reconcile quickly. It suggests that some placements could change channel dynamics.'"
    "Aria Chen: (pause; unreadable) 'Complications happen. We can discuss caveats in the hearing. My concern is alarmism before the commission accepts a plan. The town needs certainty, not more fear.'"
    show isla_morgan at right:
        zoom 0.7

    isla_morgan "The uncertainty is the thing that could make the plan harmful. If we don't address it now—"
    "Aria Chen: (interrupting, controlled) 'Then present your caveats. We will decide based on the complete administrative process.'"
    "Luca Moreno, listening over your shoulder, exhales audibly."
    show luca_moreno at center:
        zoom 0.7

    luca_moreno "That's the language of burying things in minutes and footnotes."

    aria_chen "My intent is not to bury, Luca. My intent is to avoid panic. The town cannot function on panic."
    "Isla Morgan: (soft) 'And my intent is to avoid harm.'"
    "Aria Chen's silence feels like a ledger balancing something you cannot see."
    "Aria Chen: (finally) 'Prepare your submission. If you want external corroboration expedited, I can recommend a contact from the City Office. But the timeline is tight; be judicious.'"
    "She signs off before you can ask whether that contact is likely to be independent. The line clicks dead and the lab seems colder."

    "Isla Morgan (thinking)" "Aria's offer is both an opening and a trap. Independence becomes complicated when names come from the same desk."
    "The storm calendar is a header on the municipal page in your head now: the commission moves in weeks; major storms have been trending earlier. Time is narrowing like a throat."
    "You pace once, then twice. The light is thinning. Your hands hover over the keyboard; one hand still rests on the compass."
    "Ravi's voice flashes in your memory — the way he can turn a crowd into attention in a second — and you imagine Luca using that—imagine the roar of people forcing a different kind of pressure."
    "You imagine also the slow, surgical ways institutions sideline inconvenient data. Both images are ruinous in their own right."

    luca_moreno "We can thread the needle. You send it to Dr. Reyes for fast corroboration, with an embargo. I organize a town meeting to present what we do know. If we do it smart, we protect you and the science."

    isla_morgan "We could also leak it — force the pause with public outrage."
    "Luca Moreno: (after a beat) 'That's the scorched-earth option.'"
    "(He looks at you, searching.) 'Isla, you'll have my back if you want to do this loud.'"
    "Isla Morgan: (hands on the table) 'And you'll have mine if I go quiet and build the evidence. But I can't promise the country will reward patience.'"
    "Luca Moreno reaches for your wrist like a rudder and then withdraws, uncertain."

    luca_moreno "I hate that the town is running on a deadline set by people who don't sleep here. I hate that we're reduced to choosing between two bad outcomes."

    isla_morgan "Choose. That's the point. The choice will be mine to make."
    "There is a moment of silence that stretches, not peaceful but taut, like a net pulled too tight."

    menu:
        "Tell Luca outright you need time to verify before any public move":
            "You say the words slowly and he nods, disappointment softening at the edges. He taps the table, already drafting plans in his head for how to hold a meeting without a headline."
        "Ask Luca to set a public meeting tonight to gauge sentiment while you try to fast-track corroboration":
            "He brightens and then darkens as the implications settle. He agrees with speed, his optimism spiking into something practical and dangerous."

    # --- merge ---
    "Continue"
    "You look toward the Salt Flats windows, where the rain blurs the horizon into gray smears. In your mind the channels cut through the flats like arteries. The storm calendar shortens again, as if to remind you that tides don't wait for science."

    "Isla Morgan (thinking)" "Everything I do will change someone's map of safety. I have to decide which map I make worse and which I can live with."
    "You sit back and gather your notes into a pile that feels too small for the weight you carry. The models are in your hands; the town is in the balance; Aria's voice still threads through"
    "the lab like a rodent through walls — efficient, unseen. Luca waits, earnest and perilous, as if action alone could be a salve."
    "Outside, the gulls cry and rain stitches the sky to the sea. The lab light flickers as clouds pass. The compass rests against your palm, precise and indifferent."
    hide aria_chen
    hide isla_morgan
    hide luca_moreno

    scene bg ch11_e67f19_4 at full_bg
    # play music "music_placeholder"  # [Music: Dissonant strings resolve into a low, descending minor chord]
    "You know the options as clearly as the map: make the finding public and force a pause; submit within the system and risk bureaucratic sidelining; or trust an external peer and use community pressure as cover. Each route promises its own harms."

    menu:
        "Leak the findings to local press under embargo to force public scrutiny.":
            jump chapter12
        "Submit the cautious report to the council and demand a pause pending peer review.":
            jump chapter16
        "Send the data to an external peer and ask Luca to publicly organize while we wait.":
            jump chapter18
    return
