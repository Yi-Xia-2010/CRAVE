label chapter17:

    # [Scene: Marabel Promenade | Night]

    scene bg ch11_c6db25_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant gull, then the soft vibration of a phone notification]
    # play music "music_placeholder"  # [Music: Low, insistent string ostinato — a tide's heartbeat]
    "Narration:"
    "You are walking the boards because you needed the scrape of wood under your boots to keep you honest. The brass compass is folded into the inside of your jacket, warm and steady against your sternum,"
    "a private metronome. The Beacon's halo slices the horizon like a promise and a threat at once. You taste salt and something metallic — fear, or the thrill of being needed."
    "Your tablet buzzes in your pocket. You pull it out with fingers that don't trust themselves."

    scene bg ch11_c6db25_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A single high notification ping; the wind picks up into a harder whistle]
    # play music "music_placeholder"  # [Music: The ostinato tightens, strings squeezing closer]
    "Narration:"
    "You read fast. Legalese doesn't soften into meaning until you imagine houses stamped with liens, elders priced out, the Promenade fenced and polished. The clause is short and poisonous: a backdoor for investor claims when the"
    "company decides an event is an 'exigency.' The thread threads your feed with screenshots — red circles around phrases, outraged comments, frightened pleas."
    "Your chest sharpens. Panic is a ripple spreading outward; within minutes it will reach the market, then insurance, then the narrow offices where the town's fate translates into signatures."

    menu:
        "Call Noah and ask him to meet at the lab":
            "You thumb his name. His voicemail picks up—'I'm at the Beacon. On my way.' The relief is small and immediate."
        "Head straight to Tidewatch Lab to watch the feeds":
            "You tuck the tablet away and move toward the lab steps, boots slapping faster. Authority feels like action, and action drowns the tremor in your hands."

    # --- merge ---
    "Continue to Tidewatch Lab scene."
    # [Scene: Tidewatch Lab | Moments later]

    scene bg ch11_c6db25_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The lab's servers hum; a wall of monitors scrolls graphs and camera feeds]
    # play music "music_placeholder"  # [Music: Electronics pulse; tempo quickens]
    "Narration:"
    "The lab is bright and clinical, the smell of ozone and damp paper clinging to the air. Noah is there before you, dark curls flattened by rain, eyes already on the main feed. He looks up"
    "when you come in; there is no surprise on his face — only the quick, worn attention of someone who has rehearsed this in his head too many times."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "They're talking about the clause like it's a wound that's already raw. Marta just pinged me. Insurance's on the phone. We need to—' (he inhales; his voice tightens) 'We need a clear line for people. Not legalese. Not reassurances that mean nothing."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Show me the wall camera."
    hide noah_reyes
    hide asha_moreno

    scene bg ch11_c6db25_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The feed's audio picks up a grinding pop; then the wall shudders — wood and engineered stone complaining]
    # play music "music_placeholder"  # [Music: Percussive stabs; the ostinato accelerates into a snare-like urgency]
    "Narration:"
    "The test wall fails with an irritable, small catastrophe: a seam gives, water finds it like light. The Beacon's sensors record pressure spikes in real time — a jagged, merciless graph. The camera's image warps as water surges past, an ugly sluice swallowing the engineered lip."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "That's faster than our worst-case. The models are lying to us."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Eli—get the boats ready. Marta, sound the garden hubs as refuges. Mayor Rosa needs to be on every channel."

    noah_reyes "I'll draft a calm message. You go outward. People need hands more than words."
    "Narration:"
    "You feel the room tighten like a net. Decisions stack on your ribs. You are the point where logistics and rhetoric meet. Your throat is dry. Your hands smell of salt and old paper."

    menu:
        "Order volunteers to the boardwalk first":
            "You hit the comms: 'Boardwalk team, sandbags now. Old Boatyard volunteers: elders first.' The response is immediate — three affirmative pings in five seconds."
        "Call Lila and demand an engineering response":
            "Your finger hovers over Lila's contact. You remember the clause. If you call her now, you may tie the town to the contract further, but the wall might not stand otherwise. Your thumb presses."

    # --- merge ---
    "Continue to Promenade and Boardwalk scene."
    # [Scene: Promenade and Boardwalk | Minutes later — sirens and shouts]
    hide noah_reyes
    hide asha_moreno

    scene bg ch11_c6db25_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slap of wet canvas, shouted names, the slap of oars]
    # play music "music_placeholder"  # [Music: Rapid strings and brass; urgency at full pitch]
    "Narration:"
    "You rush out onto the Promenade. The air is a hard lash of rain. The boardwalk is a choreography of urgency — elbows, the thunk of wet sandbags, feet slipping. Marta's voice cuts through like a whistle."
    show marta_chen at left:
        zoom 0.7

    marta_chen "Asha! Over here! Use the raised beds as staging — cover the compost bins, they'll float but they'll give people time!"
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Eli, can you ferry Rosa's mother? No, the elders nearest the old pier — two at a time."
    show eli_duarte at center:
        zoom 0.7

    eli_duarte "On it.' (He nods, jaw set; his hands have always known how to move wood and water.) 'We built for storms like this — not like this."
    "Narration:"
    "Eli's boat pumps through the chop. The smell of diesel and wet timber is comforting in its own way — work that has names and tools. Marta's gloves are a bright smear as she hands out lifejackets fashioned from float crates, cursing at the Beacon's numbing white light."

    marta_chen "They gave us sensors but not the right terms. We can't rely on a feed when people's houses are on the line.' (She looks at you, fierce and small and impossibly tired.) 'What do you want from us right now, Asha? What can we actually do?"

    asha_moreno "Hold the line at the gardens. Make sure the tallest beds are cleared for people who need flat space. Send the kids with the lanterns to guide elders. Don't let anyone work alone."

    marta_chen "You heard Noah? He thinks calming words will stop panic. I think hands stop panic."
    "Noah Reyes: (over your shoulder) 'Both. I'll handle the public line. You keep them moving. Say what we can do, not what we can't.'"
    "Narration:"
    "Noah's voice is steady and compositional — the skill of a planner who can press together people's fear and make a brief bridge. You notice the slight micro-gesture: his hand finds your shoulder, pressure firm, not patronizing, not clingy. The compass in your jacket feels like a tiny second pulse."
    hide marta_chen
    hide asha_moreno
    hide eli_duarte

    scene bg ch11_c6db25_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rustle of paper like a new kind of rain]
    "Mayor Rosa: (calling from a makeshift podium of crates) 'Listen. I am contacting legal counsel. We will not allow predatory claims to stand. We'll make the town seen, and we will hold the line. But right now—' (she gestures to the surge) '—we stop the water from claiming more.'"
    show asha_moreno at left:
        zoom 0.7

    asha_moreno "Rosa, if we pause to litigate now, do we risk losing homes tonight?"
    show mayor_rosa_alvarez at right:
        zoom 0.7

    mayor_rosa_alvarez "Yes. And we might also sacrifice bargaining leverage if we're seen as desperate. But I will not sell the town by default."
    "Narration:"
    "Her words land like a weight. Mayor Rosa moves between the administrative and the human with practiced care. Her decision will imbalance a thousand little lives. You know the weight of that choice more intimately than most: every course will bruise someone you love."
    # [Scene: The Beacon Plaza (live feed hub) | Night — intermittent lightning]
    hide asha_moreno
    hide mayor_rosa_alvarez

    scene bg ch11_c6db25_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rapid typing, panicked radio traffic, an incoming message alert]
    # play music "music_placeholder"  # [Music: A high, thin note — nerves tuned to breaking]
    "Narration:"
    "A message bleeps onto your tablet. Lila Park's name stitches the header. Your thumb hesitates. You open it."
    show lila_park at left:
        zoom 0.7

    lila_park "Asha — I'm seeing the reports. I'm sorry. Our team is mobilizing emergency patches. We will cover immediate repairs and coordinate with Eli for evacuation returns. I can come to Marabel in the morning. — Lila"
    "Narration:"
    "The message is crafted in Lila's precise optic: measured remorse, immediate action. It is not an apology that glows; it is an apology that fits a PR timeline."
    show noah_reyes at right:
        zoom 0.7

    noah_reyes "That's damage control. She says she'll patch. She says she'll show up. That buys us time."
    show asha_moreno at center:
        zoom 0.7

    asha_moreno "And the clause? The leak is already trending. Investors smell leverage when valuations wobble. If we accept corporate help now, we may forfeit our leverage to contest those clauses later."
    "Noah Reyes: (rubbing his temples) 'Then what? Refuse help and watch the town flood? Sue them and wait? Mobilize every neighbor and risk failing?'"
    "Narration:"
    "His questions are not rhetorical. They jab at the raw nerves beneath your ribs. You feel the old guilt — your father's boat in a storm, the image of his hands. The instinct to shoulder everything collides with the practical arithmetic of lives at risk."
    # play music "music_placeholder"  # [Music: Crescendo — drums and strings drive the scene toward a razor edge]
    "Marta Chen: (leaning in) 'If we push the legal route publicly, we risk scaring off donors and the consortium's emergency crews. But if we don't, they set the precedent: help, then control.'"
    "Eli Duarte: (returning, soaking) 'We can shore. We can brace. But walls break in storms we didn't predict. Nature isn't going to ask for our contracts to be honored.'"
    "Mayor Rosa: (loud enough for the crowd to hear) 'We must protect people first. Then the contracts. Always people first. But that does not mean we surrender.'"
    "Narration:"
    "You are the fulcrum. Your palms are slick. The town pulses around you — hands moving, voices shouting, children guided under tarps. The Beacon's sensors keep screaming into the lab: breaches, pressure spikes, new flows mapping themselves across old streets."
    "Noah's hand on your shoulder is the only steady thing you allow yourself to find. His grip is unspoken tether: shared risk, shared consequence."

    noah_reyes "Asha, whatever we choose, say it clearly. People are already afraid the town will be sold while they sleep. They need a name to point at, not a floating list of options."

    asha_moreno "I know. I'm thinking—' (you stop, because thinking aloud right now might look like dithering) '—I need to know if we're willing to let Lila's engineers take the lead tonight, or if we push for legal action that could slow emergency response, or if we throw everything into the marsh restoration plan right now and pray it works."
    "Narration:"
    "Your voice is a small, honest thing in the storm. The options fan out like waves: immediate corporate mobilization, public legal exposure, or an accelerated, risky natural restoration that would bind the town to its own hands. Each will cost something visceral. Each will leave scars."
    hide lila_park
    hide noah_reyes
    hide asha_moreno

    scene bg ch11_c6db25_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The Beacon's sensors emit a thin, sustained alarm, then a pattern of urgent pings]
    # play music "music_placeholder"  # [Music: Strings tighten into a single held dissonant chord]
    "Narration:"
    "You breathe. You taste iron and salt. Your role is to choose a path that balances rescue and rights, speed and sovereignty. The town is watching in a way it never has before: not only the town but the city feeds, the insurance market, investors who read panic as purchase."
    "Page-turning thought: If you choose to lean on Lila now, the repairs may hold and the town will sleep, but the contract might become the chair everyone sits on for the next decade. If you choose"
    "to litigate and expose, you might save rights but lose immediate protection. If you choose the marsh — you might be the town's moral anchor, or you might make a gamble that floods more than pride."
    # play music "music_placeholder"  # [Music: A single sharp crescendo; then silence ready to break]

    menu:
        "Work with Lila to mobilize corporate resources to shore the town immediately.":
            jump chapter20
        "Expose the leaked clauses and pursue legal action with Mayor Rosa to renegotiate terms publicly.":
            jump chapter29
        "Mobilize the community for an accelerated natural restoration—risky, resource-heavy, but autonomous.":
            jump chapter20
    return
