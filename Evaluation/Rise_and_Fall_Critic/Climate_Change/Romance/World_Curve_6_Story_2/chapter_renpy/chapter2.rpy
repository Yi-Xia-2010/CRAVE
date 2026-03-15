label chapter2:

    # [Scene: Town Hall | Night]

    scene bg ch2_c4ca42_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, tense BGM — a rhythm like distant surf]
    # play sound "sfx_placeholder"  # [Sound: The soft scrape of wet coats, a chair leg raking the floor; a damp cough somewhere in the back]
    "You step into the hall and the smell hits first — brine and frying oil, stale tobacco, the metallic tang that clings to old nets and older grievances. Sodium lamps hang from the rafters, casting everything"
    "in a tired amber; puddles on the floor mirror the ceiling like small, worried moons."
    "Your notebook is heavy in your hands, its corners softened by fingers that never learned stillness. You press it to your ribs because the world keeps measuring you in losses, and the paper feels, absurdly, like armor."
    show mayor_ansel_reed at left:
        zoom 0.7

    mayor_ansel_reed "Thank you all for coming. We promised a forum, and a forum we shall have. I ask for order and—' (he glances at the Skyhub delegation by the door) '—candor."
    "A ripple of murmur answers him. You count faces: Etta's lined jaw like a cliff, Rafi's camera pressed to his chest, Dr. Hana's tablet a cool rectangle in her lap, Ilias Navarro with sleeves still flecked"
    "with kelp. People who have lived with the sea longer than the town's newest boutiques and people who have watched the coastline redraw itself on their calendars."
    hide mayor_ansel_reed

    scene bg ch2_c4ca42_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A soft clack of high heels on wet wood]
    "Seren Blake arrives late. Her blazer is engineered fabric that repels the sea; the cut reads like a promise. A tiny solar pin on her lapel flashes once, twice — a pulse that feels like a corporate heartbeat."
    "Seren Blake: (She sets her tablet on the lectern; the slide deck projects in sharp, efficient lines.) 'Sorry to be late. Data collection ran longer than expected.' 'I'll be direct. The coast is changing faster than"
    "local mitigation can keep up. Our plan proposes three immediate measures: a raised sea wall along the High Tide Boardwalk, managed relocation incentives for the most-at-risk blocks, and engineered wetlands to buffer storm surge. Funding is"
    "ready. Implementation would begin within months.'"
    "Her voice is calm and polished, each sentence a clean arrondissement of facts. The images that follow are mercilessly concrete: diagrams of levees, before-and-after aerials, cost curves that flatten like promises. You feel the floor tilt under the numbers."
    show maya_kestrel at left:
        zoom 0.7

    maya_kestrel "Those wetlands — what scale are you suggesting? And how will fishing access be preserved? Our harvests are seasonal and—"
    show seren_blake at right:
        zoom 0.7

    seren_blake "The wetlands are modular. We can design channels for local boats. The relocation incentives include community consultation and compensation."
    "You hold your breath for the phrase that usually follows: 'in exchange for...'. It never comes out, but the implication hangs like a net."
    "Etta pushes to her feet before you can think of the next question. Her shawl is thick and salt-stiff; she moves like a boat that knows its own weight."
    show etta_muir at center:
        zoom 0.7

    etta_muir "You speak of channels and modulars like a man counting planks! You will not make our nets antiques in a museum. My father taught me the tides; my father taught me to read the moon. Tell me, Miss Skyhub, where do our stories go when the city lifts us and calls it progress?"
    "Seren Blake's smile is measured; there is a small, complex flicker in her eyes that you cannot read."

    seren_blake "We are not erasing stories. We're preserving lives and livelihoods. In the relocation plan, there are funds for cultural preservation — archives, sanctuaries—"

    etta_muir "Sanctuary for who? For artifacts, or for people? You'll put our kitchens in storage and call it care."
    "Rafi shifts, camera clicking through palms."
    hide maya_kestrel
    show rafi_soto at left:
        zoom 0.7

    rafi_soto "This'll make a headline. 'Town Sold to Save Balance Sheet'—or 'Saved by Innovation.' Depends on which side of you runs the pen tonight, Maya."
    "Rafi smiles like someone trained to see the seam in a fabric and tug it gently. He looks to you, expectant."
    hide seren_blake
    show maya_kestrel at right:
        zoom 0.7

    maya_kestrel "Wait—' You feel the calluses in your palms against the notebook, the small comfort of ink between fingers. 'There is a different route. We can scale living restoration — distributed eelgrass beds, mosaic rock barriers that buy time and provide habitat, rooftop gardens to rein in runoff—"
    "Dr. Hana taps her tablet once, the light glancing across her face, eyes steady and slightly weary."
    hide etta_muir
    show dr_hana_sato at center:
        zoom 0.7

    dr_hana_sato "Biologically, eelgrass and kelp restoration are sound but slow. Kelp beds take years to re-establish at functional biomass. They remain vulnerable to heat stress and successive storms. They are part of a long-game resilience strategy, not an immediate buffer against the kind of surge Seren Blake's wall would blunt."
    "Ilias Navarro leans forward, voice low and urgent."
    hide rafi_soto
    show ilias_navarro at left:
        zoom 0.7

    ilias_navarro "But you could seed it with a networked approach — community teams, labor credits, staggered plantings. Combine it with small-scale, permeable barriers that don't sever access. Funding's the choke point. If we can secure sustained, local funding, the biology wakes up and—' (He looks up at you, hopeful and open.) '—it regenerates."
    hide maya_kestrel
    show seren_blake at right:
        zoom 0.7

    seren_blake "Sustained funding often requires scale, Mr. Navarro. The funds I'm talking about are contingent on measurable outcomes within a fiscal cycle. We need visible protection, not a five-year pilot."
    "You feel the room tighten at 'visible protection.' Visible to whom? To insurers and bondholders; to people who have power on the other side of the bay. The friction between 'what science needs' and 'what money demands' is the underside of every meeting like this."
    "Mayor Ansel lifts a hand."
    hide dr_hana_sato
    show mayor_ansel_reed at center:
        zoom 0.7

    mayor_ansel_reed "We will need a vote on whether to accept the initial funding package to begin engineering work while parallel studies commence on restoration. We... need a plan that doesn't leave people waiting."
    "Etta's hands are on the table now, veins maplike under skin weathered by salt."
    hide ilias_navarro
    show etta_muir at left:
        zoom 0.7

    etta_muir "When my nets were new, we prayed to the sea and to the places our people respected. I tell you, we've already waited too long. They speak of studies when children are standing ankle-deep in the next flood."

    seren_blake "We will hold community integration workshops. We will make sure voices like yours are at the table for relocations."

    etta_muir "Workshops do not hold a family in a rising tide."
    "The exchange lands like a stone. For a moment, silence falls thick and absolute. You pick at the frayed binding of your notebook with a thumb you didn't know you were twisting, feeling the pulse at your temple, the old guilt washing over you like cold salt."

    menu:
        "Stand and challenge the timeline":
            "You rise, clearing your throat. Your voice feels gravelly — you push the diagrams and dates into the open. 'How many months, Seren Blake? How many homes will be uprooted before the wet season?'"
        "Breathe and listen":
            "You remain seated and listen. The hallway noise folds into the room; you let Etta speak until the point becomes raw and heavy and the words hang like nets in the air."

    # --- merge ---
    "The debate fragments into side conversations — who could be bought, who could be saved — and Rafi angles his camera for a reaction shot: a town torn between immediate shelter and long-slow repair. Ilias Navarro"
    "moves to your side, lowering his voice so the room becomes a soft hearth where only the two of you whisper."
    "The debate fragments into side conversations — who could be bought, who could be saved — and Rafi angles his camera for a reaction shot: a town torn between immediate shelter and long-slow repair. Ilias Navarro"
    "moves to your side, lowering his voice so the room becomes a soft hearth where only the two of you whisper."
    hide seren_blake
    show ilias_navarro at right:
        zoom 0.7

    ilias_navarro "Your plan — the mosaic barriers — it could be done in sections. Start where the eelgrass still clings. Pair it with microgrids for pumps and community labor markets... We could make the funding look like infrastructure maintenance, not speculative grants."
    hide mayor_ansel_reed
    show maya_kestrel at center:
        zoom 0.7

    maya_kestrel "And how do we convince Ansel and the council to delay a big payout in favor of something that pays back only over seasons, not fiscal quarters?"

    "Ilias Navarro (a small, rueful smile)" "We make it a numbers story and a people story. Dr. Hana's data, Etta's testimony, a schedule that shows measurable gains in eighteen months. Also...' (He hesitates, anxious to be more than theory.) 'I can speak in the field. Show them kelp shoots in trays. Let them feel the mud."
    "Dr. Hana: (quiet, pragmatic) 'You will need monitoring protocols, baseline surveys, and contingency funding. The science community can help design that, but quality control is expensive.'"
    "Seren Blake, who has been listening, folds her hands and speaks with that same crispness that had filled the room before."
    hide etta_muir
    show seren_blake at left:
        zoom 0.7

    seren_blake "Or you can accept a wall that measurably reduces immediate flood risk. And we can fast-track relocations with compensation tailored to keep small businesses afloat. We are not enemies of your heritage. We are trying to save people."
    "You feel, suddenly, a loneliness as sharp as a winter wind. Her words are wrapped in empathy and a ledger."
    "Etta stands and crosses the room, placing an old photograph on the table — a faded shot of boats lined three to a pier like interlaced teeth."
    hide ilias_navarro
    show etta_muir at right:
        zoom 0.7

    etta_muir "This is Hearthbend before the big city teams decided to 'save' its future. We will not be a case study in a power point. We will not be moved for the convenience of a balance sheet."
    "Her hand hovers over the photo like a benediction. For a second, every argument in the room seems to bow to that image."
    hide maya_kestrel
    show mayor_ansel_reed at center:
        zoom 0.7

    mayor_ansel_reed "We are at an impasse. I propose the council take these proposals — both sides — to a special advisory panel. We will reconvene with recommendations."
    "The room hums with a resigned energy — plans shelved for panels, panels for committees — bureaucracy's way of postponing pain."
    "You stand, finally, the notebook a weight and a talisman. Outside, the boardwalk lamps catch at the rain like small, stubborn beacons. Fog begins to creep in under the door, washing the sodium light into soft, indistinct halos."

    menu:
        "Follow Ilias to the Saltgarden lab after the meeting":
            "You move toward Ilias Navarro, whose eyes lift as if he’d been waiting to be asked. 'There are samples in the trays,' he says. 'Come see where the shoots are starting to take hold.'"
        "Walk the boardwalk alone to think":
            "You step out into the fog. The boardwalk is a gray ribbon and the lamps are halos. Your breath fogs in front of you, and the town feels like a seam under strain — you trace it with every step."

    # --- merge ---
    "You find the corridor out to the boardwalk quicker than you expect. Conversations thin into the muffled sound of people unthreading themselves into the night. You can hear someone laugh — brittle and brief — like a match struck for show."
    "You find the corridor out to the boardwalk quicker than you expect. Conversations thin into the muffled sound of people unthreading themselves into the night. You can hear someone laugh — brittle and brief — like a match struck for show."
    "Outside, fog drapes the promenade. The sea is mostly a rumor beyond the wall; the lamps glow like sentries whose orders no longer make sense. You press your notebook to your ribs and imagine the town as a cloth with its seams fraying at the edges."
    "Your mind catalogues consequences: the people who will take the relocation money out of fear, the elders who will refuse it out of pride, the children who will inherit maps redrawn in someone else's ink. The word 'compromise' tastes of salt and loss in your mouth."
    "Ilias Navarro comes up beside you, water-damp hair sticking against his temple. He hands you a small, clear sleeve — a cutting of eelgrass wrapped in damp paper. The green is fragile and defiant."
    hide seren_blake
    show ilias_navarro at left:
        zoom 0.7

    ilias_navarro "It's small now. You'd be surprised what time and community hands can do with what looks like nothing."
    hide etta_muir
    show maya_kestrel at right:
        zoom 0.7

    maya_kestrel "And if 'time' costs people their homes? Their lives?"

    ilias_navarro "Then we cannot ask for time we do not have. But I don't think every solution has to be a binary. Maybe we force the timeline to match the biology through local commitment and staged engineering."
    "You listen to the cadence of his hope like a prayer you both share and cannot guarantee."
    "The town's seam frays a little more with each passing minute; you feel it in your chest like a pulled wire. The guilt — old and like a familiar bruise — pulses there, reminding you of"
    "the sibling you lost in a storm and why you became the planner who flirts with impossibility."

    "Mayor Ansel's voice carries faintly from the hall" "We will reconvene — vote on steps to take interim protection measures while studies proceed—"
    "The phrase 'interim protection' tastes hollow. Interim for who?"
    hide mayor_ansel_reed
    hide ilias_navarro
    hide maya_kestrel

    scene bg ch2_c4ca42_3 at full_bg
    # play music "music_placeholder"  # [Music: A low unresolved chord]
    "You stand between two kinds of assurance: one fast, hard, and engineered; the other slow, living, and brittle under fiscal pressure. Both promise safety of a sort; both promise loss."
    "The meeting has ended without resolution. The town drifts, its individuals holding their small truths like candles in a wind that will not be quelled. You fold your notebook closed and feel the imprint of decisions yet to be made on your palm."
    "Page-turn thought: You can hear the ocean like a slow, patient clock. Choices lurk like undertows; you must act — but how and when and for whom remain a net you cannot untangle in a night."

    scene bg ch2_c4ca42_4 at full_bg
    # play music "music_placeholder"  # [Music: Tense BGM eases into a single, lingering note]

    scene bg ch2_c4ca42_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
