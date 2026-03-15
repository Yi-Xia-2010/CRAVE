label chapter2:

    # [Scene: Tideworks Lab | Morning]

    scene bg ch2_c4ca42_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of pumps, the soft click of an old projector, distant gulls and the city’s breath]
    # play music "music_placeholder"  # [Music: Warm strings, soft but insistent — a hopeful underscoring]
    "You push the door the way you always do: the same shoulder, the same small grunt that keeps your hands free for tools. The lab smells like wet earth and espresso — not unpleasant, like the"
    "city’s stubbornness distilled into a single room. Your notebook is at your hip; the potted cutting in its sling brushes your ribs with familiar weight. It steadies you."
    "Dr. Jun is already there, hunched over a bank of translucent displays. Lines and histograms hover in the air — tide-phase overlays, pump uptimes, salinity gradients mapped like a topography of worry and hope. Jun looks"
    "up as you step forward; the smile is quiet and real, the kind that says you did the right thing by showing up."
    show dr_jun_park at left:
        zoom 0.7

    dr_jun_park "You look like you carried the garden in your arms. Good. We've got last night’s sensor logs. The seep at Block 7 skirted what we feared — sensors show the berm held, and the living mats recovered faster than projected."
    "You let that land. It’s not victory; it’s an actionable inch forward. Every inch is currency here."
    show asha_rivera at right:
        zoom 0.7

    asha_rivera "Show me the trend."
    "Dr. Jun gestures; a waveform bends toward steadier numbers. Tiny green pulses mark where community-built root structures anchored faster than the simulation expected."

    dr_jun_park "Community work plus the new substrate mix Jun recommended — it's synergistic. The model favors distributed interventions. And—' (he taps another pane) '—your rooftop gardens are registering as micro-buffer zones. They’re small, but cumulatively, they matter."
    "You feel something unclenching inside you. Practical results are not poetry, but they read like one right now."

    dr_jun_park "Mayor’s office asked for an executive summary. They want certainty. Hana's team is on the call from Aegis; she'll present a modular pump network in twenty. Elias texted he's on his way."
    "Your chest tightens in the familiar double-pull: the scientist’s hunger for data, and the neighbor’s refusal to let numbers flatten a living place into a ledger. It’s the same tension that used to keep you awake"
    "as a kid, listening to the tide and deciding whether to board windows or water the seedlings."

    menu:
        "Concentrate on the graphs — annotate the anomalies now":
            "You lean in, tracing the waveform with your finger, murmuring corrections into Jun's recorder; the room sharpens into detail."
        "Breathe, take the plant out of its sling and let the smell ground you":
            "You cradle the cutting for a long beat, the basil-salt scent like home; your questions sound less urgent and more choosing."

    # --- merge ---
    "Narrative continues."
    "Dr. Jun watches you with a small, indulgent look before turning back to the holo."

    dr_jun_park "Whatever you choose to emphasize at the hearing — data or story — bring both. Numbers buy time; stories make people use it the right way. Hana's presentation will complicate the messaging, but she has resources we need."
    "You nod. Practicalities pile into your hands like bricks. You want them to be placed carefully, not thrown."
    # [Scene: Aegis Tower (Holo) | Continuous]
    hide dr_jun_park
    hide asha_rivera

    scene bg ch2_c4ca42_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The light whoosh of long-distance comms; a faint, distant cityscape]
    # play music "music_placeholder"  # [Music: A gentle swell of piano chords woven with the lab’s strings — precise, hopeful]
    "Hana Kim steps into the room as a glass projection, her silver bob catching the lab light like cutlery. The AR monocle gleams briefly; her voice is the measured cadence you remember from late-night lab debates."
    show hana_kim at left:
        zoom 0.7

    hana_kim "Good morning, Asha, Jun. I pulled the pump-staging schematic into the shared file. The modular pumps can be deployed within seventy-two hours and operate on a distributed control mesh. They scale; we can prioritize high-risk corridors and minimize displacement."
    "Her presentation unfolds as a holographic knife: sleek, efficient components snapping together in animated clarity. You can see the appeal — rapid deployment, automated fail-safes, redundancy mapped in cool blues."
    show asha_rivera at right:
        zoom 0.7

    asha_rivera "Seventy-two hours is fast. But who runs the mesh? Who fixes the units when the kids climb on them or the salt eats the connectors? What's the maintenance burden on neighbors?"
    "Hana Kim’s fingers — literal, or holographic, you can’t tell — fold the schematic into a tighter node. There’s a rhythm to her speech that has always comforted and unnerved you: the certainty of someone who measures variables to make decisions."

    hana_kim "We’ve built user interfaces for community stewards. Training cycles are short. Field kits will be distributed, and there’s a diagnostic overlay that flags failures before they cascade. We can set cost-sharing models so the city subsidizes capital and local groups handle upkeep."
    "Dr. Jun leans forward, curiosity tickling his features."
    show dr_jun_park at center:
        zoom 0.7

    dr_jun_park "Those overlays could integrate our sensors. A hybrid system — community-built living mats for biofiltration, with targeted tech where hard infrastructure is essential — might reduce long-term costs."
    "There’s a pause. The lab soundscape bends toward the overlap of Jun’s optimism and Hana’s precision. You feel the momentum — not as a shove, but as wind picking up behind a small boat."

    asha_rivera "I want guarantees about cultural—about practices. A patchwork of pumps and algorithms cannot erase the memories of streets, of who dug those canals. If we ask people to maintain devices, we must also protect place."
    "Hana Kim's projected expression shifts — not cold, but careful. The look is complex: a scientist’s focus wrapped in the remnants of your old friendship."

    hana_kim "I remember the boardwalk you rebuilt after the spring surge. I don't want to overwrite the community. I'm proposing technical scaffolding that preserves choice, not removes it. Let us pilot the mesh in tandem with your living mats; Jun's datasets make it viable."
    "A hush settles. It's the kind of compact negotiation that could have been an argument years ago, but now contains a thread of something gentler: the possibility that the two of you can still translate different languages of care into a shared plan."

    hana_kim "If your board supports a joint proposal, Aegis will underwrite the initial rollout and training. We want it to be community-led, not corporate-run. There will be oversight panels, transparent logs."
    "You can feel the argument forming in yourself: distrust of firms with glossy cufflinks versus the relief of funding you could use yesterday. You choose your next words to carry both."

    asha_rivera "We’ll need a clear, enforceable clause about community governance in any agreement. And an audit, independent. People need access to the logs, not just to a company's PR."

    hana_kim "Agreed. I can draft the clause and include a third-party auditor. We'll make the open logs a condition."
    "Dr. Jun taps a final tile on the holo and sends a compact to your tablet. The data glows warm in the lab's softer light."

    menu:
        "Ask Hana to slow the technical rollout — more participatory workshops first":
            "You press gently, suggesting a slower path; Hana notes the request and promises to fold it into the schedule, her projected brow softening."
        "Request the audit wording now — put it on the record":
            "You ask for specifics; Hana agrees and uploads a clause-based draft. The file blooms between you like a shared promise."

    # --- merge ---
    "Narrative continues."
    # [Scene: Tideworks Lab — Harbor Entrance | Late Morning]
    hide hana_kim
    hide asha_rivera
    hide dr_jun_park

    scene bg ch2_c4ca42_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant laughter from the market, the slap of a small boat against its moorings]
    # play music "music_placeholder"  # [Music: Guitar plucks thread through the strings — warm, immediate]
    "Elias Hart is breathless in more ways than one. He grins like someone who has just stolen a moment back from the tide."
    show elias_hart at left:
        zoom 0.7

    elias_hart "You smell like work. Jun smells like victory. Hana smells like corporate efficiency. I brought coffee — and a plan."
    "You laugh despite yourself. It’s the laugh you used to share when nights stretched too long and you kept each other awake over maps and street lights."
    show asha_rivera at right:
        zoom 0.7

    asha_rivera "Tell me the plan."
    "Elias Hart slings his bag onto a stool and lays out flyers, a rough timeline, sketches for a mural that tells our story: people, water, living walls. His voice slows when he talks about the neighborhood; there's an intensity there, a steady beam."

    elias_hart "We push for the joint proposal. We can get the public behind a pilot if they see hands on clay and valves working together. People show up for gardens; they’ll show up for pumps if we make it ours. Mayor’s hearing is the moment we paint for — hearts first, then the math."
    "Your chest loosens into a different kind of hope. Elias's instincts have always been the short, sharp blade that cuts through stovepipes of bureaucracy."

    asha_rivera "And if the mayor wants a straight buyout? If Leon spins it as efficiency-for-survival and people panic?"
    "Elias Hart: (tilts his head) 'Then we show the other side of efficiency. Show them the living mats that catch sediment and feed families, not just numbers. Show them Jun’s graphs and Hana's schematic together —"
    "not as rivals, but as co-authors. And if any official tries to erase community governance, we flood the room with people who know how to talk about loss.'"
    "Dr. Jun nods, quietly pleased."
    show dr_jun_park at center:
        zoom 0.7

    dr_jun_park "If we can present a joint pilot that reduces projected relocation risk by even ten percent in the mayor's model, it becomes a political hedge. It's not just engineering — it's survival-by-choice."
    "You close your hand around the cutting in its sling. It feels small and alive in your palm — a physical promise you can walk into the hearing with. The idea of bringing Jun's data, Hana's tech, and Elias's people into one frame makes the plan practical and, importantly, human."
    "There is a pause filled with a thousand half-formed logistics — who sits where at the hearing, which talking points you rehearse, whether Mateo will bring the murals to the front row. The lab hums; the"
    "city’s muffled clamor presses at the window like a crowd waiting politely at a theater door."
    "Elias Hart leans in, eyes on yours, softening."

    elias_hart "Are we really doing this together?"
    "You sense the old fault lines — the falling-out you both endured when tactics and tempers failed to align — but right now they look like healed scars, still visible but not preventing you from moving."
    "Hope, you think, is not the absence of fear; it's a decision to act while afraid."

    asha_rivera "Yes. We make it ours. Jun brings the proof, Hana brings the scaffolding, you bring the people. I bring the stubbornness not to sell us out."
    "Elias Hart chuckles, the sound like someone exhaling after climbing steep stairs. It’s small, but it warms the room."

    menu:
        "Ask Elias to hold off on any street actions until after the hearing — control optics":
            "You ask for restraint; Elias nods, reluctant but trusting, promising to keep actions symbolic and peaceful until the vote."
        "Tell Elias to mobilize — presence is pressure":
            "You bite your lip, then decide volume matters; Elias grins, already drafting a call that will bring the market and the roof gardens into the hearing room like a living crowd."

    # --- merge ---
    "Narrative continues."
    "You spend the next hour mapping roles: who will speak to what, which corner of the hearing room the mural will occupy, which neighbors will be ready to give testimony about the living mats that kept"
    "their floors dry last month. Jun and Hana overlap more than you expected; their data and schematics dovetail in ways that feel less like compromise and more like collaboration."
    "Your internal monologue runs through contingencies — legal language, the need for an independent audit, community training cycles — and you find that each worry births a plan. That is the day's currency: the conversion of fear into strategy."
    "You gather the documents: Jun's annotated logs, Hana's clause draft, Elias's timeline, and a rough sketch of the mural. The potted cutting is still snug in its sling, leaves dusted with salt. You tuck everything into"
    "your pack. The light outside has shifted toward noon; the harbor smells of hot metal and citrus and a certain lean optimism."

    dr_jun_park "Bring them what we have. Make them see the reduction in risk and the preservation of place. That—' (he taps the air where the graphs hang) '—that is the argument that wins votes and buys breathing room."
    "Hana Kim's hologram flickers for a heartbeat, then steadies."
    hide elias_hart
    show hana_kim at left:
        zoom 0.7

    hana_kim "I'll be on standby to answer technical questions at the hearing. And Asha — if you want, I can show the mayor a live diagnostic during the session. Immediate transparency."
    "You sense the shape of an alliance forming: not perfect, not without tension, but functional. The rising tone in you isn't naive; it's a vigilant optimism that expects storms and prepares for them."
    hide asha_rivera
    show elias_hart at right:
        zoom 0.7

    elias_hart "Let's walk it down to the harbor steps. Talk through the opening lines. Make sure the story hits before the slides."
    "You sling the pack over your shoulder, feeling the weight of plans and people and a small, living thing that somehow stitches them together. The harbor's heat is a slap of reality and a promise of work to do."
    "You step out onto the boardwalk, and the city exhales around you — vendors calling, children shrieking as they chase a dog, the distant-industrial sigh of pumps at work. There is purpose in all the noise now, a kind of organized chorus."
    "A thought petals across your mind and won't let go: the hearing is not the end — it’s the first place where the world will see us try. You are terrified and ready. The two can coexist."
    hide dr_jun_park
    hide hana_kim
    hide elias_hart

    scene bg ch2_c4ca42_4 at full_bg
    # play music "music_placeholder"  # [Music: Strings rise into a bright, anticipatory chord]
    "You pause at the threshold and take one more breath, tasting salt, coffee, and the green sharpness of the cutting. You think of Mayor Ortega’s laminated schedule, of Leon Voss's polished smile, of Teo's grease-streaked optimism"
    "waiting to unfurl at the hearing. You step forward because momentum is built by steps, not leaps."
    "A plank of wood creaks; the tide thrums its slow heartbeat beneath you. The city is full of people deciding, hour by hour, to stay and to rebuild. You carry their choices with you."
    "You turn toward the path that leads up to the municipal chamber, heart steady with a rising certainty: this could be the day where the city remembers how to be both brave and careful."
    # [Page-Turn Moment: You look down at the cutting in your pack — a small green thing against the weight of papers and plans — and you realize, plain as the salt on your tongue, that today isn't about winning a policy argument. It's about proving that preservation and progress can be braided together. The thought lingers as you walk; the light ahead seems to ask nothing less of you than courage.]

    scene bg ch2_c4ca42_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
