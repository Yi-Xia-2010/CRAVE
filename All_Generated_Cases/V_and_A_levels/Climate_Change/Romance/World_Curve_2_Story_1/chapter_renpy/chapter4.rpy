label chapter4:

    # [Scene: Saltworks (Reclaimed Marsh Labs) | Morning]

    scene bg ch4_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense BGM — low strings tremble]
    # play sound "sfx_placeholder"  # [Sound: Seagulls call distant; a drip of water from a tarp]
    "You wake to the smell of damp reeds and solder. The Saltworks is a patchwork heartbeat: hoses slung like veins, solar sails catching pale light, mud drying in stepped terraces where tide gardens will sit. The"
    "team moves in a choreography you know by instinct — tighten a bolt, sweep a walkway, mark a testing node — all small, stubborn acts against a rising sea."
    "Your palms are still gritty from the last-night build; the coral scarf at your throat is damp with morning fog. You lay out the prototype micro-turbine pieces on a battered workbench and watch Elias Park cross-check"
    "the wiring with his camera slung against his chest. His hands are steady enough to make you believe steadiness is possible."
    show elias_park at left:
        zoom 0.7

    elias_park "We can demo the micro-turbine array and the raised platform mock-up in the plaza. Show them how it ties into the tide gardens. Keep it simple — force-of-concept, not spectacle."
    show mira_santos at right:
        zoom 0.7

    mira_santos "Simple will be the harder sell."

    elias_park "We have data. We have neighbors willing to testify. We just need them to see it's built by people who live here, not by a balance sheet."

    mira_santos "That's the whole point. If it looks like a shiny replacement, they'll think it's just another project to be bought and moved."
    "Noah arrives, shoulders still dusty from finishing a raised walkway. He grins without humor, the kind of grin that bristles with worry."
    show noah_rivera at center:
        zoom 0.7

    noah_rivera "You two look like you woke up inside a council agenda. How bad is the suit-and-tie turnout today?"

    elias_park "Enough to be dangerous."
    "You inhale. The wind smells of bay water and frying dough from a boardwalk vendor — small comforts another life away. Today is about translating that smell into law, into lines on a map that mean people get to keep their houses. It is small and enormous at once."

    menu:
        "Lead with community testimony — Aunt Lila speaks first":
            "You hand Aunt Lila the list of neighbors who agreed to speak; her eyes are steady, and she practices a quiet, fierce rhythm. Hearing the town's voices first frames the tech as ours."
        "Lead with Elias' technical demonstration first":
            "You slide the prototype into Elias' hands. He brightens; the turbines hum under his fingers. A clear demonstration could cut through disbelief — but it risks feeling like a sell."

    # --- merge ---
    "The narrative continues."
    # [Scene: Municipal Hall / Council Chamber | Late Morning]
    hide elias_park
    hide mira_santos
    hide noah_rivera

    scene bg ch4_453e40_2 at full_bg
    # play music "music_placeholder"  # [Music: Tense BGM intensifies — percussion taps in the background]
    # play sound "sfx_placeholder"  # [Sound: Muffled chatter, the scrape of chairs]
    "The council chamber smells of coffee and recycled air. The public benches are crowded — elders in layered cardigans, kids with hand-drawn posters, a smattering of reporters. Your notebook lies open on your lap, pages annotated until the ink smears."
    "A projection fills the glass wall: a schematic of the tidal gardens, the micro-turbine array, platforms rising like ribs from the marsh. You and Elias Park stand before the dais; the mayor nods politely and turns the microphone toward you."
    "(Your voice is steadier than you feel.)"
    show mira_santos at left:
        zoom 0.7

    mira_santos "Marrow Bay has always been a conversation between land and sea. We propose a pilot — community-built micro-turbines, tide gardens that absorb energy and water, and raised platforms for essential pathways. Not a replacement for our town, but a means to keep living in it."
    "Elias Park: (Paced, patient.) 'The prototypes are low-cost, repairable with local materials. We designed them to be modular — if a storm takes one piece, the rest holds. We can show how they'd integrate with existing drainage, how we can scale with local labor.'"

    "Council Member" "How will you ensure safety? Who's liable if something fails?"
    "Mira Santos: (You meet the councilmember's gaze.) 'We want legal protections for residents, clear maintenance plans led by the community, and accountability through transparent reporting. We will show results from controlled tests and be present to train volunteers.'"
    "Murmurs rise. Aunt Lila's hand squeezes yours in the third row — a small, warm resistance."
    "Then Cassandra 'Cass' Whitlock rises."
    hide mira_santos

    scene bg ch4_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A faint hush falls]
    show cassandra_cass_whitlock at left:
        zoom 0.7

    cassandra_cass_whitlock "This is admirable, Ms. Santos. Community-driven work is important. But community projects lack the resources to scale and to meet engineering standards required for long-term resilience."
    "Mira Santos: (You feel it — the room's air tightening.) 'We don't want to cut corners. We want to keep decision-making local.'"
    "Cassandra 'Cass' Whitlock: (Calm; unblinking.) 'My firm can offer conditional funding. Oversight would come from my team's engineering board and legal counsel. We can fast-track construction and cover liability concerns. In exchange, we'd require a formal oversight agreement.'"
    "Noah: (Under his breath.) 'That sounds like 'in exchange' means 'control'.' He doesn't say it louder, but his jaw is set."
    "Elias Park: (Quiet, a tremor at the edge of his voice.) 'Conditional oversight could be a way to actually get this built before the next storm. It could mean more lives saved.'"
    "You feel the puzzle inside you shift — each piece now heavier. Cass's offer is a lifeline rounded in steel. Her words are measured, but every measured word presses."
    show aunt_lila_santos at right:
        zoom 0.7

    aunt_lila_santos "They'll take our stories and put them in a brochure. They'll name it for us, then move people out when the price goes up."

    cassandra_cass_whitlock "We are not here to displace. We are here to protect. But protection sometimes requires centralized coordination and capital that community groups cannot conjure."
    "You can taste the council's indecision like metal on your tongue. The mayor folds her hands and consults a tablet. Reporters tilt their microphones. Someone in the back calls for more details about 'oversight agreement.'"
    "Mira Santos: (Your internal list expands — liability, control, speed, trust. You think of Aunt Lila's house and every board nailed by hands that know the tide line. You think of families who cannot afford an"
    "evacuated future.) 'Conditional oversight is a risk to the community's autonomy. Once decisions are ceded, it's hard to take them back.'"

    cassandra_cass_whitlock "You are painting a stark choice, Ms. Santos. My firm can avoid a catastrophe. Or you can keep this small and potentially fragile.' (She smiles — perfectly small, perfectly sharp.) 'Ultimately, this is about what kind of future Marrow Bay chooses: an integrated, funded solution or countless small projects vulnerable to the next storm."

    menu:
        "Press Cass on the definition of 'oversight' publicly":
            "You ask Cass to clarify the oversight clause. Her answers are precise, anchored in legalese. The crowd leans in; the mayor scribbles notes. The debate becomes about language."
        "Shift to a personal plea — tell Aunt Lila's story now":
            "You tell Aunt Lila's memory of the last flood — the way she kept a shell on the windowsill to remind her of what to save. Faces in the room tighten; you make the stakes human rather than contractual."

    # --- merge ---
    "The narrative continues."
    # [Scene: Boardwalk | Afternoon — Immediately after the council chamber session]
    hide cassandra_cass_whitlock
    hide aunt_lila_santos

    scene bg ch4_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Tense BGM reaches a higher tempo — strings and offbeat percussion]
    # play sound "sfx_placeholder"  # [Sound: Wind like a breath held too long; a gull's harsh cry]
    "You step out into the wind and feel the conversation unspool into arguments and whispers. The plaza is a messy collage of flyers, people clustering like flotsam. The Saltworks team unloads a small mock-up of a turbine on a flatbed — something tangible to point at, to touch."
    "Elias Park is at your side, his jaw tight. He looks like someone who wants to fix something immediately and utterly."
    show elias_park at left:
        zoom 0.7

    elias_park "They barely agreed to hear it. Cass offered money and oversight; the mayor looked tempted. That oversight clause will be a leash..."
    show mira_santos at right:
        zoom 0.7

    mira_santos "You think it's a leash. I think it's a hook. Either way, we get pulled."
    "Noah: (Hands splayed, trying to marshal volunteers.) 'People want to act. They want tools. They want to know where to sign up to help build. They don't want to argue legalese in chambers — they want shovels.'"
    "Aunt Lila: (Soft, fierce.) 'We built our houses with neighbors. We don't want strangers deciding who gets to come back.'"
    "The Saltworks team sets the mock-up down. Kids reach out to touch the turbine blades; an old man runs his palm along a platform board as though blessing it. You feel the tide of public feeling like a solid thing that could be fashioned or battered."
    "You fold your hands around the coral scarf and feel how small your body is in the swell of decisions. Cassandra 'Cass' Whitlock's offer hangs in the air like barbed fog. The council wants a clear path — a yes, a no, or a negotiated middle."
    "Elias Park: (Lowered voice.) 'If we accept oversight, we get resources and legal cover. If we refuse, we stay in control but risk not getting built before winter. If we use the demo to call out Cass, we might rally public opinion but also make enemies who can bury us.'"
    "Mira Santos: (All at once, exhaustion and adrenaline surge. The arousal ratchets up — people are waiting. The town's future is an auction of promises and contracts and grief.)"
    "This is not the time for certainty. This is the time for choosing which kind of grief you are willing to carry."
    hide elias_park
    hide mira_santos

    scene bg ch4_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind picks up; a few raindrops begin to spot the wooden boards]
    "Your chest is raw. You can hear your pulse like the drum of a distant storm. The Saltworks prototype hums softly, an answer and a question."
    "You could rally everyone for a fully community-run pilot, keep the work close and slow — precise but potentially insufficient when the next season comes. You could accept Cassandra 'Cass' Whitlock's conditional funding, buy time and"
    "cover but hand over oversight to people whose priorities may not match the town's memory. Or you could stage the demo as a public challenge, forcing Cass into a show of power that would raise the"
    "stakes for everyone."
    "Every option splinters into trade-offs that taste like loss. The valley between saving and being saved is narrow and steep."
    "You breathe in salt, in the smell of wet wood and wet plans. The sky darkens as the first honest raindrop hits the boardwalk. The moment feels like a hinge — the town waits; your hands hover above the lever."
    # play music "music_placeholder"  # [Music: Crescendo; strings and percussion collide into a single, driving rhythm]

    scene bg ch4_453e40_6 at full_bg

    menu:
        "Proceed with the public demo as a fully community-led pilot.":
            jump chapter5
        "Accept Cass' conditional funding to scale the pilot with firm oversight.":
            jump chapter6
        "Use the demo to publicly challenge Cass, inviting a showdown.":
            jump chapter16
    return
