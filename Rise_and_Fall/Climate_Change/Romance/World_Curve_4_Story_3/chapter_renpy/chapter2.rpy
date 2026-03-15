label chapter2:

    # [Scene: Promenade | Early Evening — After the Ferry Presentation]

    scene bg ch2_c4ca42_1 at full_bg
    # play music "music_placeholder"  # [Music: Steady, hopeful piano with a rising string undercurrent]
    # play sound "sfx_placeholder"  # [Sound: Distant camera shutter clicks, low murmur of a gathered crowd, gulls, soft slap of water against pilings]
    "You arrive with the salt of the harbor still in the cuffs of your jacket, the brass of your watch warm under your palm. It is the same watch you wore on the ferry last night"
    "— not marking hours so much as keeping tally of promises. The Promenade smells of wet cedar, algae, and baking bread from a stall two stands down; that mixture is a comfort like a uniform: messy,"
    "necessary, real."
    "A compact crowd rings the models spread on low crates: curled reeds bound with twine, strips of recycled oyster-shell mesh, tiny pilings artfully staggered in damp clay. Jonah kneels at the edge of the display, arranging"
    "laminated photos with a practiced hand. When he hands you a print — a wide-angle shot of the experimental berm at low tide — the woven fishing-line ring on his right thumb flashes like a tiny,"
    "deliberate lighthouse."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "I managed a golden hour shot before the crew left. Thought you might like the perspective for the board."
    "You take the print; his fingers brush yours for a beat longer than necessary. You feel your chest loosen in a way your single-minded notes and sediment graphs never managed. Practicality and warmth in the same"
    "person; it makes you stubborn in a new way — stubborn to protect this small constellation of things you love."
    "Maya is already there, leaning against the railing with her neon-yellow coat splotched with damp mud from the community plots. Her impatience is audible in the way she taps her boot on the wood."
    show maya_ellis at right:
        zoom 0.7

    maya_ellis "They're late. They're always late, and then they want everything perfect. People are cold and wet, Mara. We can't be neat about this."
    show mara_ellis at center:
        zoom 0.7

    mara_ellis "We can't be messy about the demonstration either. Precision convinces permits. Stories keep us human. We need both."
    "Maya scoffs but nods. She jabs a finger toward a small cluster of elderly residents listening to Old Mate."
    "Old Mate — Mateo Alvarez — speaks with the cadence of tide charts read aloud. His skin smells faintly of tar and old rope; his voice collects attention like gulls collect scraps."
    hide jonah_reyes
    show mateo_old_mate_alvarez at left:
        zoom 0.7

    mateo_old_mate_alvarez "Back when the harbor remembered boats and not barricades, the seawall let the storm pass. The rats under the decking saved themselves then, and we— we learned which moorings to trust. These ideas of yours…' (he pats a reed bundle) 'are not new to these eyes. But they take people believing. People, not numbers."
    "A reporter threads through the crowd, camera balanced on one shoulder. Her mic has the municipal station logo; the lens drinks in the damp light. She asks a question you expected and have rehearsed for a different kind of room."

    "Reporter" "How does a living breakwater respond to a surge compared to an engineered wall? Aren't you risking houses for—"
    "Professor Asha slips in beside you then, her braid unspooling just enough that salt flecks the silver. She sets down a slim folder of archival charts — old bathymetries, annotated maps showing marsh line retreat over decades. Her presence is a small, steadying authority."
    hide maya_ellis
    show professor_asha_rao at right:
        zoom 0.7

    professor_asha_rao "It's not an either/or. Living structures dissipate energy differently; the data show sediment trapping increases over time when combined with managed retreat corridors. We have the long-term records."

    "Reporter" "So no immediate guarantees?"

    professor_asha_rao "Never guarantees. But measured resilience that keeps people in place while ecosystems adapt has a track record."
    "Councilor Anika arrives with an umbrella that refuses to stop dripping. Her expression is courteous, almost surgical; she watches without applause, a habit of seeing both headlines and spreadsheets."
    hide mara_ellis
    show councilor_anika_patel at center:
        zoom 0.7

    councilor_anika_patel "Ms. Ellis, these are compelling models. My concern is scale: what you show here is persuasive for a neighborhood—but can it convince the funding committees and the contractors who build at scale?"
    "You meet her gaze. She is the hinge between your work and municipal approval; you know she has to balance everything you've already said with the city's appetite for decisive measures — measures Elias Crowe sells expertly."
    hide mateo_old_mate_alvarez
    show mara_ellis at left:
        zoom 0.7

    mara_ellis "We're proposing a hybrid implementation. Start neighborhood-scale: living breakwaters, marsh terraces that buy time and sediment. Use those results to inform scalable designs—less destructive than a monolithic seawall, more adaptive than temporary pumps."

    councilor_anika_patel "And the timeline?"

    mara_ellis "Pilot season within six months. Monitoring through community stewards. If the trial demonstrates predicted accretion and reduced overtopping, we can scale adaptively."
    "Jonah Reyes adds, hands moving, explaining with the quiet mechanics of an engineer who likes to show instead of assert."
    hide professor_asha_rao
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "We've modeled wave attenuation across three storm scenarios. With the reef matrix in place and the marsh elevation response we simulate, peak velocities drop enough to prevent overtopping for the 10-year event and reduce damage in the 25-year event."
    "A murmur of impressed surprise runs through the crowd. Maya grins and mutters something you can't quite hear; you feel the momentum shift — not a tidal wave, but a steady, insistent swell."

    menu:
        "Stand by Jonah and let him finish the technical run-through":
            "You step closer to Jonah, letting him take the technical lead. His voice strengthens; you watch the way the audience relaxes around his details, and a small, private surge of pride rises in you."
        "Take the mic and steer the message toward community stewardship":
            "You fold the technical into a story — the baker down the block who will tend marsh plots, the kids who will track birds. Faces soften; some nod, and Maya mouths 'good' like a benediction."

    # --- merge ---
    "The demonstration continues with Old Mate's interruption and the community's response."
    "Old Mate interrupts, not unkindly, when Jonah mentions monitoring."
    hide councilor_anika_patel
    show mateo_old_mate_alvarez at center:
        zoom 0.7

    mateo_old_mate_alvarez "Monitoring? Then who's going out when the rain comes? Who will be the eye? You talk 'bout data like a ledger, child. We talk 'bout who wakes when the storm bell rings. You promise to include both, yes?"

    mara_ellis "You are the ledger. The people are the monitors. The data is for the councils to trust you, Old Mate. We want the city to give you tools, not replace you."
    "Old Mate's jaw moves; for a moment his face is unreadable, then it unfurls into a slow nod. The crowd shifts; a woman near the railing wipes a tear into a folded handkerchief and claps softly."
    "Professor Asha steps forward with archival overlays projected briefly from a tablet onto a damp piece of plywood; the map glows faintly, halos of data tracing the city's erosion like constellation lines. She points to an area where your berm pilot produced sediment gains."
    hide mara_ellis
    show professor_asha_rao at left:
        zoom 0.7

    professor_asha_rao "These layers correspond. Your field results aren't anomalies — they follow historical accretion pathways we've documented. This matters for council votes; they respond to precedent and to risk avoidance numbers."
    "Councilor Anika leans in, toggling the projection on with a stylus. She makes no promise; she does the best thing a city councilor can do in this hour: she notices."
    hide jonah_reyes
    show councilor_anika_patel at right:
        zoom 0.7

    councilor_anika_patel "I can bring this to the proper committee. If your models hold, and if the community is prepared to oversee the pilot, I'll put forward a motion to schedule a hearing for funding authorization."
    "The crowd exhales like wind leaving a held sail. Maya squeals under her breath and then shushes it, trying to be dignified in the public moment."
    "Jonah's hand finds yours briefly — not a public display, just a steadying contact as the reporter calls for quotes. Your internal monologue tightens: you are elated, but you also feel the old, familiar hard line"
    "in your chest. Momentum breeds choices. Your stubbornness warns you: don't trade long-term integrity for short-term cards."
    "A young volunteer steps forward with a clipboard and a list of community commitments; people sign on. A local blogger angles for a soundbite; someone streams the demonstration; a neighbor sweeps up mud and hands you a handful of broken shells as an offering for the marsh plots."
    "A message arrives on your phone: an anonymous tip, rudimentary and ominous — NovaSeis has been asking questions about the Drowned District and the council schedule. The note is terse and smells of inevitable corporate motion: big money, big plans, faster timelines."
    "You feel the rising stakes as a physical thing: a pressure building behind the throat. Hope and complication braided together."

    menu:
        "Tell Councilor Anika about NovaSeis's interest now":
            "You catch Anika's sleeve and mention the NovaSeis queries. Her expression flickers—politician recalibrating—and she asks for the source. The mood becomes cautiously strategic; the room leans toward procedure."
        "Keep NovaSeis to yourself and trust the council hearing will reveal more":
            "You tuck the warning away. For now the crowd's faith and the signed commitments feel like armor. You choose to build momentum, believing exposure will come at the hearing."

    # --- merge ---
    "The assembly continues; planning and commitments proceed as the council hearing is scheduled."
    hide mateo_old_mate_alvarez
    show mara_ellis at center:
        zoom 0.7

    mara_ellis "We are not here to romanticize loss or to postpone hard decisions. We're here to propose that we can keep people in place while strengthening our shores. If we win a pilot, we will have evidence. If we fail, we will still have learned something to keep our neighbors safe."
    "A woman in the crowd — a teacher from the block school — raises her hand."

    "Teacher" "Will there be jobs? People need work to stay. Not just promises of safety."
    hide professor_asha_rao
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "Maintenance crews, monitoring teams, nurseries for marsh plants — these are jobs you can train for locally. We'll include training in the pilot package. We want local people running these projects."
    "You watch Jonah speak, the crowd reacting; the teacher's face brightens. Your heart, stubborn as it is, opens a sliver wider. There's romance in shared purpose — the small, dangerous hope that you and Jonah could be partners in both policy and life."
    hide councilor_anika_patel
    show professor_asha_rao at right:
        zoom 0.7

    professor_asha_rao "I'll provide the archival package for the council. Historical data plus your recent pilot will make the case stronger than either alone. Evidence and community testimony together—it's persuasive."
    "Councilor Anika's attention narrows to procedural focus."
    hide mara_ellis
    show councilor_anika_patel at center:
        zoom 0.7

    councilor_anika_patel "Schedule me the hearing. Bring me a short packet — models, the monitoring plan, public commitments. I'll request an early slot. Expect a formal calendar notice."
    "Applause; careful, constructive applause. You feel the wood under your boots as though it were a stage you have already walked across. Momentum, at last, has the shape of policy."
    "Then someone mentions NovaSeis aloud — a ripple of discomfort. You see the city through a new lens: your pilot sits on the same map as a corporation that moves fast and loud. Their proposals are rumored to promise immediate certainty, at the cost of local nuance."
    "Maya's face hardens. Old Mate looks out toward the water, his features pulled into a line you cannot read easily."
    "You feel the decision circle closing, but not sealing. The city has offered you a hearing; the council has a date. The next step — how to argue in that room, who will carry which message,"
    "whether to publicly align with Jonah's pragmatic engineering or to confront Elias Crowe's NovaSeis — hangs like a buoy in fog: visible only in outline, but crucial to navigate toward."
    "You tuck the print Jonah gave you into your notebook. The paper is slightly damp, curling at the edges where the sea-spray hit. You press your thumb to the image, feeling the faint grain of the"
    "salty paper, and name the choice you'll have to make soon, even before the hearing begins."
    "Page-turn thought: A hearing date and a crowd's tentative trust. A corporate shadow at the edges. The Promenade hums with the small, electric possibility that public attention brings. You can either step into a partnership that"
    "may compromise some ideals for scale, take NovaSeis on directly, or pursue the slow policy-first route that waits for proof to change minds. All three paths feel both dangerous and necessary."
    hide jonah_reyes
    hide professor_asha_rao
    hide councilor_anika_patel

    scene bg ch2_c4ca42_2 at full_bg
    # play music "music_placeholder"  # [Music: Piano rises, hopeful and insistent]

    scene bg ch2_c4ca42_3 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
