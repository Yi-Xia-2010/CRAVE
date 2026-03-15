label chapter3:

    # [Scene: City Hall Council Chamber | Midday]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm strings with a steady, hopeful pulse — a gentle but insistent uplift]
    # play sound "sfx_placeholder"  # [Sound: The distant hiss of rain on the skylight; a public murmur like tide movement]
    "You step into the chamber still carrying the residue of Beaconworks: the faint tang of resin and wet folders, the warmth of Elias’ hand when he reached for the compass a moment ago. The room is"
    "larger than the lab, its proportions meant to make private argument feel public and deliberate. People lean forward in the benches — neighbors from the Drowned Garden, civil engineers in neat jackets, a scattering of reporters"
    "with mud-speckled boots."
    "You are aware of the seed-bead bracelet at your wrist, the hydroponic locket pressed under your sweater as if it were a small, living talisman. It steadies you. You have a speech mapped in your head,"
    "but more than words you carry a place: the way morning light breaks like coin across the wet walkways, the sound of children chasing gulls from a patched pontoon, the smell of peat and old rope."
    "Lucia’s presentation is precise and theatrical. She lays out the consultancy’s emergency seawall in clean modules: what it will protect, the projected survivability percentages, the timeline under emergency procurement."
    show lucia_montrose at left:
        zoom 0.7

    lucia_montrose "This plan preserves the city's core within three cycles of storm seasons. It is efficient, enforceable, and funded. We cannot afford hesitation."
    "Her voice is a measured instrument; the graphs behind her glow with unemotional certainty. Mateo leans forward, the papers in his hand damp along the edges from field visits. He says the word everyone is already feeling — urgency — and his cadence makes it procedural rather than personal."
    show councilor_mateo_qu at right:
        zoom 0.7

    councilor_mateo_qu "The projections Lucia's team provided show a clear immediate risk to central infrastructure. Emergency measures are advised. We'll open for public testimony."
    "The microphone carries your neighbor's cough, the crisp whisper of a press recorder, the soft creak of a folding map being smoothed. Elias stands at your shoulder, tablet held like a talisman of its own. He"
    "looks at you once — that small, unreadable expression hovering between peer and something more intimate — then returns his attention to the dais. You breathe in and step forward when your name is called."
    hide lucia_montrose
    hide councilor_mateo_qu

    scene bg ch3_98c6f2_2 at full_bg
    show mara_solenne at left:
        zoom 0.7

    mara_solenne "Councilors, Lucia, people of Port Lyra — I live in the Drowned Garden. I stand with the families who have spent decades building life out of tides. Our wetlands are not empty space; they are living infrastructure — they slow storm surge, they store sediment, they hold livelihoods."
    "You let the image press: raised walkways humming with markets, a child’s toes skimming brackish water, Rani's hands steadying a raft as a storm approaches. The imagery is plain but specific; it fills the sterile chamber with a neighborhood’s breath."
    show lucia_montrose at right:
        zoom 0.7

    lucia_montrose "Ms. Solenne— while I respect community ties, the data indicate structural barriers are the only way to ensure continuity of service to hundreds of thousands."
    "She does not sneer; her tone is clinical. But there is friction in the room, a taut wire between human testimony and model output. Lucia’s words insist on a scale that flattens the particular. You feel"
    "the old tug of impatience — the urge to clamp down and argue — and you choose another rhythm."

    mara_solenne "Numbers are not neutral. They describe what you measure, not everything that lives between measurements. Build the wall and you may protect buildings — but the people who feed, mend, and anchor those buildings will disappear from the coast. They don't vanish from futuresheets. They are displaced."
    "Elias shifts, placing a hand lightly against your back — support, not a correction. He opens his tablet and tilts it so that a small, annotated diagram is partly visible to you: a loose sketch of"
    "a possible hybrid barrier with living marsh components and engineered buttresses. He does not interrupt; he offers the scaffold for words yet to come."
    show councilor_mateo_qu at center:
        zoom 0.7

    councilor_mateo_qu "Ms. Solenne, will you provide constructive alternatives for consideration? The record needs feasible options, not only objections."
    "His request is procedural but kind. He knows how a hearing bends: stories without policy are sympathetic but ephemeral; data without people is implacable. You hear the hinge of possible compromise."

    menu:
        "Lead with story — make it personal":
            "You slow, choosing to name faces: Rani under a rain tarp, Eda bending to read tidalweed in the mud. The chamber quiets; some bench-side eyes fill. You sense momentum pulled toward human weight."
        "Lead with hybrid data — show them a model":
            "You gesture toward Elias' tablet, describing numbers: potential surge reduction per meter of restored marsh, a phased build. Engineers in the back nod; the room leans toward practicality."

    # --- merge ---
    "'The two approaches draw different currents in the chamber at once. You decide to braid them.'"
    "The two approaches draw different currents in the chamber at once. You decide to braid them."

    mara_solenne "Both truth and tenderness must exist in policy. We have models that show wetland restoration can reduce surge, if phased and funded. I ask the council to fund a pilot: fund the people who will do the work, and measure the results with rigorous oversight. Let the city own the proof as much as it owns the perimeter."
    hide mara_solenne
    show elias_harrow at left:
        zoom 0.7

    elias_harrow "What Ms. Solenne outlines is technically achievable. Beaconworks can draft a co-design pilot that measures hydrodynamic response, biodiversity gain, and socio-economic outcomes. It will take time, but it will be rigorous. It will be responsible."
    "Lucia watches you both like a engineer observes a load-bearing beam — assessing where pressure concentrates. The exchange does not dissolve her case; it reframes the parameters. For a moment there is a shared language in"
    "the room — people listening for how to transform moral urgency into schedules and line items."
    # play sound "sfx_placeholder"  # [Sound: A low sympathetic murmur — approval tempered by skepticism. A child's laugh echoes faintly from the foyer; someone coughs.]

    councilor_mateo_qu "I will take that under advisement. We will ask the consultancy to include comparative scenarios in their next brief. The council will not act without looking at alternatives."
    "The line is not a pledge, but a hinge: an opening. You feel the room tilt slightly in your favor — not victory, but motion. The hopeful pulse inside you brightens. Outside, the Promenade's cranes will not stop, but inside these walls, someone has promised to weigh other data."
    "After the public testimonies, the chamber empties like the tide pulling back to expose new flats. You step down from the dais to the receiving light of the foyer and find Rani waiting near the exit, a grin like a sail."
    hide lucia_montrose
    show rani_cho at right:
        zoom 0.7

    rani_cho "You gave them mud and math. I thought you'd just show up and start a chant."
    "You laugh, and it rings. Rani clasps your shoulder, uptake of her usual mischief. Eda stands a little apart, her shawl heavy with pattern and memory; she folds her hands as if reading a tide omen."
    hide councilor_mateo_qu
    show eda_nal at center:
        zoom 0.7

    eda_nal "You spoke as you are, child. You let them see the wetlands as a thing that breathes. That will hold with some people."
    "Eda's approval is steady, like the slow growth of marsh grass. Her presence is a benediction."

    menu:
        "Go talk to Elias privately in the hallway":
            "You catch his arm and he steps aside, eyes clearing into focus. You share a quick, close plan: what a pilot would need, who to call, and how to protect neighbors during phasing."
        "Seek Councilor Mateo for procedural next steps":
            "You move through to Mateo, who thumbs through his papers. He speaks of ordinances and vote calendars; you feel the machine of city government begin to align with your voice, slowly, deliberately."

    # --- merge ---
    "'You pause in the foyer, the decision knot tightening like a coil of rope ready to pay out. You map the options in your head with the meticulousness you use on the marsh: what mobilizes people"
    "fastest, what converts a persuasive soundbite into budget line items, what preserves the most life across years.'"
    "You pause in the foyer, the decision knot tightening like a coil of rope ready to pay out. You map the options in your head with the meticulousness you use on the marsh: what mobilizes people"
    "fastest, what converts a persuasive soundbite into budget line items, what preserves the most life across years."
    "Your hydroponic locket rests at your sternum, warm and oddly weighty; you hold it and let it prompt the catechism you learned under Eda’s tutelage — act where you can, tend what you can, refuse panic."
    "Love pulls at you too: Elias has stepped into the space between you and the city. You can feel the possible fracture of choosing a path that demands everything from his ethics or his job."
    "Elias meets your eyes — steady, patient — and the small things between you say what the council room will not: cooperation is not a single moment but an infrastructure of care and compromise."
    "Eda's voice is a low thread as you move toward the exit."

    eda_nal "Old ways and new tools can braid. Find the braid, Mara. Teach them how to weave."
    hide elias_harrow
    hide rani_cho
    hide eda_nal

    scene bg ch3_98c6f2_3 at full_bg
    "You close your eyes for a fraction, rooting for hope. Today a councilor promised a look; today Lucia did not dismiss you outright. That is not triumph, but it is progress — a slow, stubborn ascent. Your chest lifts with something like confidence."
    "You know the major question will not be solved by a speech alone. It will be solved by where you choose to put your energy next: publicity and bodies at the Promenade; a negotiated pilot through"
    "Beaconworks; or patient legal scaffolding with Mateo that turns testimony into ordinance. Each is work, each is love, each is risk."
    "You feel Elias' hand find yours in the crowd, fingers curling around your strap. His touch is quiet but affirmative — a small architecture of trust under the large architecture of the city."
    "You take a breath, and the future arranges itself into three clear paths."

    menu:
        "Lead a visible direct-action campaign at the Promenade construction site.":
            jump chapter4
        "Push Elias to broker a co-design pilot between Beaconworks and the community.":
            jump chapter7
        "Pursue legal and policy channels with Councilor Mateo Qu to secure protective ordinances.":
            jump chapter10
    return
