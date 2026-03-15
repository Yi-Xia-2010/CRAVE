label chapter2:

    # [Scene: Community Greenhouse & Seed Bank | Morning]

    scene bg ch2_c4ca42_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, a neighbor's radio faintly playing a news brief about the meeting; the hiss of the greenhouse vents]
    # play music "music_placeholder"  # [Music: Low, melancholic piano with a slow tempo; strings undercurrent]
    "You smell your scarf before you pull it from your pocket — a thread of your grandmother's laundry, rosemary and lemon, stubborn and familiar. It steadies you. Outside, Marisora wakes with the economy of people who"
    "measure time by tides and school bells; inside the greenhouse, time is a different currency: hours measured in stomata, in the slow breathing of soil."
    "Your nails get dark again the instant you kneel. Dried earth packs under your fingers like a ledger of a thousand small failures and small recoveries. You label, weigh, swab. The sample bags are neat, a"
    "small rebellion against the larger mess. You run pH strips, glance at the salinity probe’s small green numbers, and make another line on the tablet's spreadsheet: sample 17 — higher than forecast, root stress markers present."
    "Even as you record, your mind catalogs the morning's work into a list: mangrove density mapping, seed viability assays, priority plots for salt-tolerant transplants. The list is practical. It is also a litany. Each item is a hinge that could tilt a house, a family, a memory."
    show rita_ortega at left:
        zoom 0.7

    rita_ortega "You look like a cross between a scientist and a sea captain. Show me the numbers after you dust off."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "They're worse than I'd hoped in the southeast plots. Salinity's up and root biomass is down. But some heirloom tomatoes showed surprising vigor — microclimate pockets, maybe."

    rita_ortega "Microclimates, miracles. Good. Because people were asking for answers, not a list of 'maybes.'"
    "You both laugh, short and brittle. Her laugh is always a tether to community urgency."

    rita_ortega "Also — neighborhood meeting tonight. Tomas said there'd be some talk about the regional grant. Ayla wants a pilot consolidation tied to it. You heard?"

    maya_reyes "I heard the word 'pilot' and 'deadline' in the same breath. That's enough to make me want to catalog the whole coastline again."

    rita_ortega "Make them see us. Co-design. No one designs for us without us."
    "You hold the test strip, the tiny color gradient a small, private gif of panic."

    menu:
        "Share the raw soil data with Rita now":
            "You send her the spreadsheet. Rita squints at the numbers, then sits down beside you, brow furrowing. Together you sketch a quick map on a seed packet, overlaying community plots with the data — two minds bridging the technical and the human."
        "Keep the data to yourself until the board meeting":
            "You tuck the tablet back in your bag. Rita nods, sensing your guard, but the space between you narrows with unsaid calculations. She squeezes your shoulder and turns to her tray of seedlings, making tea as work and comfort."

    # --- merge ---
    "You choose; either way, the greenhouse becomes a kind of confessional. Work translates to talk. Talk translates to resolve. But the greenhouse cannot hold all the friction that will come; outside, the sea keeps moving, indifferent."
    # [Scene: Old Breakwater & Mangrove Line | Early Afternoon]
    hide rita_ortega
    hide maya_reyes

    scene bg ch2_c4ca42_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind through mangroves; the low creak of half-submerged timber; a distant saw]
    # play music "music_placeholder"  # [Music: Sparse cello, a slow, descending motif]
    "You walk the broken edge where the town's defenses end and the ocean begins. Each slab is an index of seasons — a faded graffiti heart, a rusty bolt, a plaque with names of those who"
    "once raised the breakwater together. The mangrove roots clutch the concrete like hands clutching a family photo."
    "You collect cores along the line, pressing the corer until it bites. The smell here is different: salt, old seaweed, and the sharp bright of disturbed silt. Your fingers are cold now, the soil paste sliding"
    "under your skin. You measure porewater salinity and feel the numbers slide into your gut: rising, creeping, inexorable."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "The breakwater holds for now, but the tests tell a story of incremental giving. If thresholds cross, the town loses steps — first the garden beds, then the streets we call ours."
    "You think of Elias Jun's hands at the boatyard, the rugged solves he offers, the tide-gates he dreams up from scrap wood and stubborn hope."
    # [Scene: Municipal Hall / Temporary Response Center | Late Afternoon]
    hide maya_reyes

    scene bg ch2_c4ca42_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Muffled murmurs, the beep of incoming messages, the rustle of printed briefs]
    # play music "music_placeholder"  # [Music: Low, percussion-driven rhythm; tension builds]
    "You step into the hall and feel the air change: from greenhouse warmth to the antiseptic clarity of municipal certainty. Dr. Ayla Voss stands before the sensor wall like a general before a map. Her hair is a precise line; her voice is a scalpel."
    show dr_ayla_voss at left:
        zoom 0.7

    dr_ayla_voss "Our projections show a 40 percent chance of exceeding the safe threshold in this zone within five years. The conditional funding requires a pilot consolidation. We target critical infrastructure, relocate where necessary, and deploy engineered barriers where viable."
    show mayor_tomas_nkem at right:
        zoom 0.7

    mayor_tomas_nkem "People will not move because a board tells them so. There are families here with histories longer than the municipality's records. There are votes. There are livelihoods."

    dr_ayla_voss "Tomas, I understand the political calculus. But the funding is contingent. We can be methodical, or we can wait until the storm does the deciding."
    show rita_ortega at center:
        zoom 0.7

    rita_ortega "Co-design, Ayla. You can't make this plan without local knowledge. Mangrove lines, burial grounds, where the old women hang their laundry in the sun — these things matter."
    "You watch the exchange. The hall feels like a throat where words catch."
    hide dr_ayla_voss
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "Ayla, the sensor matrix is precise — and so are its limitations. Temporal resolution misses community-scale microclimates that keep livelihoods alive for now. We need hybrid strategies that use data and local practice."
    hide mayor_tomas_nkem
    show dr_ayla_voss at right:
        zoom 0.7

    dr_ayla_voss "Hybrid strategies are costly, and politically they dilute clear metrics. If the pilot doesn't present decisive results, the region will divert funds elsewhere. We have a window."
    "You feel the gulp of constraint: windows, deadlines, thresholds that shove people like chess pieces."
    hide rita_ortega
    show mayor_tomas_nkem at center:
        zoom 0.7

    mayor_tomas_nkem "I can't promise mass relocations. I need a plan that keeps people here while protecting the most vulnerable. We cannot lose our economy."
    hide maya_reyes
    show rita_ortega at left:
        zoom 0.7

    rita_ortega "Then let us help design the protections. Let us be part of the pilot."

    dr_ayla_voss "Volunteer co-design is softer language for delay. The funders want measurable outcomes."

    menu:
        "Press Ayla for a compromise that includes community metrics":
            "Your voice pitches steady; you outline a measurable co-design metric — participatory workshops, transparent baselines, and shared monitoring. Ayla jots notes but doesn't smile. Mayor Tomas nods slowly; Rita beams with relief."
        "Keep the focus strictly technical in this room":
            "You focus on the sensor wall, speaking in thresholds and confidence intervals. The room quiets to listen to your data. Tomas looks relieved to hear figures; Rita's shoulders tighten, then she exhales and marks a new turnout plan on her phone."

    # --- merge ---
    "Words ricochet. Each suggested fix slides into the political machinery — gears that grind slowly and bite."
    "A staffer announces that evening's community briefing will include a preliminary vote on whether to authorize the pilot tender. The phrase feels like a verdict passed on the town's next generation. People file out in clusters, arguments already forming like low swells."
    # [Scene: Docks | Dusk]
    hide dr_ayla_voss
    hide mayor_tomas_nkem
    hide rita_ortega

    scene bg ch2_c4ca42_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slap of waves against pilings; soft laughter; the creak of wood]
    # play music "music_placeholder"  # [Music: A minor key acoustic guitar, melancholic but warm]
    show elias_jun at left:
        zoom 0.7

    elias_jun "I couldn't let you be stuck in a room of suits all day without seeing a little wooden rebellion. Thought you might like a prototype."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "It's bold. And…beautiful in its stubbornness."
    "He laughs, and the sound is large and immediate, a bright thing in the dimming harbor."

    elias_jun "It's not elegant. It doesn't have your fancy sensor feedback. But it holds water when it needs to, and it holds us when we build it together."
    "You find yourself wanting to believe him. His optimism is a raft. Your scientist's mind catalogs holes: fail points at high tide, rot vulnerability, the lack of monitored thresholds. You point them out, gently precise."

    maya_reyes "If we reinforce the hinges with steel and add a sacrificial plank, it could work in phases. But we need data to know where to put it and how to maintain it."

    elias_jun "You always ask for plans. Could we…let some of this be about doing? About giving people something they can touch tonight instead of a slide deck?"
    "Your sleeve is still mud-streaked; he slaps it with his palm, laughing. It leaves a dark smear across your forearm. You feel the warmth of his hand through that mess."

    elias_jun "Help me. Show me where the science says to put the gate. We'll patch the rest as we go."

    maya_reyes "Stay rigid to the data, or bend for agency that rallies hands and hearts? If I bend, I risk legitimizing half-measures; if I don't, I may strand the town in analysis paralysis."
    "The sky over the mangroves mutters like an old argument. The wind tastes of coming rain."

    maya_reyes "I need to run a quick survey. But I'll help. We do it in stages. We pilot, we monitor, we adapt."

    elias_jun "That's fine. Start where you need. But bring your clipboard to the docks when you do. People need to see the plans not just hear them."
    "You both stand in a liminal light: the harbor between day and night, the town between decisions. Your tide-watch ticks under the cuff of your jacket, a small metronome for a larger tempo."
    "You walk home with salt in your hair and a head crowded with graphs and hands, with policy deadlines and pitched planks. The town feels like a body with a fever: hot, brittle, not yet broken but trembling."
    "On your rooftop watch, you slice the sky with your gaze. The mangrove line is a darker bruise. The horizon is not a promise tonight; it is a threat and a dare."
    "You lie awake with the town's voices in your ears: Ayla's precise cautions, Tomas's worried calculations, Rita's bright insistence, Elias's stubborn laughter. Inside you, a tug-of-war starts and does not abate. Each argument claims small territories of your attention until sleep slips past like a tide going out."
    "The decision waits: a municipal meeting where the pilot will be framed, where funding's terms will be read aloud, where the town might be asked to choose between an engineered, centralized plan and a scattered, community-led"
    "patchwork. Your role will not be neutral. Your voice, your notes, your compromises will matter."
    "You breathe, tasting brine and old linen, and for the first time since the greenhouse, you feel the tilt not as possibility but as the edge of a cliff."
    hide elias_jun
    hide maya_reyes

    scene bg ch2_c4ca42_5 at full_bg
    # play music "music_placeholder"  # [Music: Strings unresolved; a slow wind-down to a single sustained note]
    "You realize that tonight the town will be asked to accept a framing that could close options forever. You are exhausted and compelled. The sky outside the window is the same bruise you carried to the breakwater this afternoon, and it presses at your chest like an obligation."
    "You rise, and the room feels smaller."
    "Page-turn thought: If you say the right words in the hall tomorrow, can you bend this machine of policy into something that keeps both people and place? Or will the combination of deadlines and good intentions force choices that fracture what you love?"

    scene bg ch2_c4ca42_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
