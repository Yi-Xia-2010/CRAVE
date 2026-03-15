label chapter7:

    # [Scene: Kaito's Field Lab (Converted Boathouse) | Late Afternoon — Rain]

    scene bg ch7_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain hitting corrugated metal roof, distant gulls muffled by fog, low static from equipment]
    # play music "music_placeholder"  # [Music: Low, minor-key piano; a slow, sinking cello undercurrent]
    "You come back the way you always do when your worry needs a place to sit: along the pier, up the slick planks, boots remembering every knot of rope. The boathouse door breathes a gust of"
    "welded-solder and salt when you push it open—two smells that are, impossibly, a kind of comfort."
    "Inside, the lab smells of damp wood and hot filament. Glass jars in a row catch the lamp light; each is labeled in Kaito Sato's hand—'Spring Inflow,' 'Tidal Silt #3,' 'pH—West Coves'—and layered behind them are"
    "notes, small graphs, a smear of dried salt that looks like a constellation. The place is thrifted and earnest: a bank of recycled batterypacks, an old coffee tin that holds resistors, and a bundle of rope"
    "used as a makeshift cable organizer."
    "Your jacket sleeve brushes a coil of wire. The patched elbow warms against the spool. Small things anchor you—things you can touch when rules and votes and promises feel like weather."
    "Kaito Sato is at the bench, hunched over a sensor housing. His ash-brown hair is flattened from the rain, a few strands clinging to the curve of his forehead. He straightens when he sees you; his sea-green eyes—wet with light—look brighter than the lamps."
    show kaito_sato at left:
        zoom 0.7

    kaito_sato "Hey. You made it back before the worst of the squall."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "I made time. How far did you get with the nodes?"
    "Kaito Sato's smile comes slow, as if he's measuring it against something fragile."

    kaito_sato "Enough to ping at low tide. Noor's models match the pattern we expected—shoreline stress spikes just before full tide at the northern spit. The hardware held through last night, mostly; Tomas and I had to patch a bracket by torch-light."
    "Kaito Sato gestures toward the marsh outside. Through the boathouse's shuttered window, thin boards form a walkway that snakes into the reclaimed marsh. Small stakes line the edges where volunteers will plant mangrove seedlings—each stake a promise with no guarantee."
    hide kaito_sato
    hide maya_inoue

    scene bg ch7_453e40_2 at full_bg
    "You inhale. The air tastes like the town—salty and brackish, with an undernote of solder. Your dive watch fogs where your wrist meets the damp; the glass fogs into a small, opaque moon."
    "Dr. Noor moves through the space with the assurance of someone who reads in numbers the same way others read a face. Her datapads are thick with printouts; when she sets them on the bench they make a dry, decisive sound."
    show dr_noor_alvi at left:
        zoom 0.7

    dr_noor_alvi "The Bayesian run reduces uncertainty if we maintain continuous sampling for three months. With community-managed berms and the mangrove underplanting, modeled erosion falls by roughly twenty percent in medium-stress storms. It's not dramatic, but it's meaningful."
    "She meets your eyes and doesn't soften the numbers."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "Twenty percent is—"
    "Dr. Noor: (interrupting softly) '—less than a wall, yes. But it's incremental resilience. It preserves coves, fisheries, the livelihoods Tomas keeps saying matter.'"
    "Tomas is at the doorway, leaning on a wrapped coil of rope like a cane. He smells of salt and boiled coffee, and the rain has made the lines on his face deeper, like the tide lines he knows so well."
    show tomas_bianchi at center:
        zoom 0.7

    tomas_bianchi "We can access the old coves by the second spit. Kids used to net crabs there. If we plant there, give those roots a chance, we bring back what the sea stole slowest. But it'll be hands and sweat, Maya. Not machines and contractors."
    "The name—your name—felt heavy in his mouth. He looks at you as if the town's memory is a ledger and you keep the balance sheet."
    hide dr_noor_alvi
    show kaito_sato at left:
        zoom 0.7

    kaito_sato "That's the pilot. Low-impact berms built with local fill and coir logs, mangrove propagation in the coves, and a distributed sensor network that gives us early warning and ecological feedback. We can iterate based on real-time data."
    "You can feel the town's heartbeat in that sentence—small and steady, but exposed."

    maya_inoue "And funding? Volunteers can do the planting, but we need materials, permits, and—"

    kaito_sato "We can apply for the coastal stewardship grant. Noor's data will make the application credible. There are a few community foundations that might come through."
    hide maya_inoue
    show dr_noor_alvi at right:
        zoom 0.7

    dr_noor_alvi "And I can pull in the regional modeling group—if we show three months of continuous data, they may co-sign. It gets us to a pilot that, if successful, demonstrates scale."
    "The plan forms into shape like low tide revealing shell and stone. It's honest and slow and terribly vulnerable."

    tomas_bianchi "What I don't like—"
    "He pauses long enough for a gust to slap the shutters. His hands curl around the rope, old knuckles white."

    tomas_bianchi "What I don't like is how easy it is for someone with coin to make us an offer we can't refuse. Lucia 'Lux' Moreno can pour concrete and call it salvation. They can promise immediate protection and jobs that pay tomorrow instead of next decade. There's power in a promise that looks finished from the outside."
    "You think of LuxCorp's plaza, all chrome and measured light—their prototypes and their polished presentations. You heard her name in the greenhouse, in the mayor's office, in the worried hum of town talk. Lucia 'Lux' Moreno"
    "is a storm of her own, and she has money that moves faster than a small-town network of volunteers."

    kaito_sato "Which is exactly why we need something defensible. Proof that the pilot works will tell a different story. We don't have Lucia 'Lux' Moreno's scale, but we have the argument Lucia 'Lux' Moreno can't buy: that the community led the solution."
    hide tomas_bianchi
    show maya_inoue at center:
        zoom 0.7

    maya_inoue "That argument is thin voicing in a room with contractors in suits."
    "Your voice falls with the rain. Maya Inoue—steady, practical, trained by loss—knows that arguments can feel like driftwood when a wall of funding arrives promising to stop the sea now."

    menu:
        "Examine the newest sensor housing":
            "You pick the sensor up; the shell is rough-under your fingers, still warm from solder. The connector hums faintly. Handling something with edges you can file down steadies the pulse in your throat."
        "Step to the shutter and listen to the marsh":
            "You press the damp wood with the heel of your hand and let the marsh fill the silence—the small clucks of waterfowl, the soft slap of reed on reed. The world continues regardless of decisions, and the thought makes your chest feel both small and wide."

    # --- merge ---
    "You return to the conversation with the team, the practical and political weighing as they were."
    "Kaito Sato watches you make the small choice and then says, a little breathless, 'I know it's a lot to ask. It asks patience. It asks people to believe in slow, not shiny. But if we get even a little data, even one successful cove—'"
    "He stops, searching for the right word."

    kaito_sato "—we can show the mayor and the town that there is another way."
    "You look at him. There's something in his face that isn't just technical optimism; it's the belief that people can remake things if given the tools. It's a warmth that both comforts and unnerves you because"
    "you have learned the hard lesson: good intentions can hurt, and small successes can be steamrolled by louder promises."

    maya_inoue "And if the mayor wants a guarantee? If she chooses Lucia 'Lux' Moreno because it looks immediate?"
    "A humid silence answers. Noor taps a stylus against a printout, then sets it down with a deliberate click."

    dr_noor_alvi "Politically, Mayor Elena is trying to hold a line between constituents who want quick answers and those terrified of corporate strings. If you present the pilot as a credible path alongside a contingency plan—"
    "Tomas snorts, a raw sound that might be a laugh or a cough."
    hide kaito_sato
    show tomas_bianchi at left:
        zoom 0.7

    tomas_bianchi "Contingency, eh? Mayor Elena will ask: when the tide comes, will your contingency cover my nets?"
    "You feel the old watch on your wrist, the metal cold under your damp sleeve. It keeps time like a small, stubborn heart. Survivor's guilt flexes: you became this because you couldn't keep a brother safe once. You cannot unfeel the margin of what 'not enough' cost."
    "Kaito Sato reaches for your hand without thinking—an unpolished, steadying gesture. You don't pull away, but you don't interlock fingers either. His fingers stay an inch from yours; the space between is an entire conversation of what could be and what you owe the town."
    hide dr_noor_alvi
    show kaito_sato at right:
        zoom 0.7

    kaito_sato "Look—bring Noor's model and the pilot idea to Elena as a companion strategy. We ask for materials and conditional permits. We promise monthly reporting. We get the coves prepped. Or—' He inhales, the cold air catching in his throat. 'Or we do it quietly. Build the proof, then present it when it can't be dismissed."
    hide maya_inoue
    show dr_noor_alvi at center:
        zoom 0.7

    dr_noor_alvi "If you build quietly, you risk being accused of hiding options or delaying urgent protection. If you go public, Lucia 'Lux' Moreno spins it as naïveté and asks why the town would gamble."

    tomas_bianchi "And if you do nothing,' he says, voice low, 'then someone else decides for you."
    "You close your eyes and remember the greenhouse: the faces leaning in, the clock ticking. You remember the forum that will take place in two days, the microphone waiting under hot lights. The town will look"
    "to you for framing. You feel the hinge—every small motion you make will tip someone's life."
    "The rain beats harder. The lab feels suddenly smaller, as if the boathouse itself is holding its breath."

    menu:
        "Pull the hood over your head and get practical":
            "You hoist your hood, the canvas whispering. Practicality helps you sort the urgency into boxes—permits, volunteers, materials. The names on your clipboard sharpen into a to-do list that does not comfort as much as it focuses."
        "Call Mayor Elena now":
            "You reach for the sat-phone on the shelf and the number lingers on your tongue. Calling now could buy her time or alert her to Lucia \'Lux\' Moreno's movements—either a bridge or a deadline. Your thumb hovers; the rain answers instead."

    # --- merge ---
    "The team watches as you settle into a decision posture; the next morning's forum looms."
    "Kaito Sato leans forward, chin on his hand, the earnestness in his brow raw."

    kaito_sato "I believe in this. I believe in us. But I also know you're the one who can phrase it right. You know the people. You know Elena's limits."
    "You want to trust that—want to accept that your voice can stitch a compromise—but the memory of the storm that took your brother presses cold and undiluted against your ribs. The town's need feels like a ledger you couldn't balance."
    "Dr. Noor folds her arms, not unkindly."

    dr_noor_alvi "Practically, three paths exist for tomorrow's forum: public championing with the pilot as the alternative, quietly building proof and controlling the narrative later, or proposing the pilot as a neighborhood-scale demonstration and asking Elena for a conditional temporary permit."

    tomas_bianchi "And if that permit doesn't come? We'll be left explaining why we didn't stop the sea when we had a chance."
    "Your mouth tastes of metal—salt and the memory of old alarms. You feel the plan in a dozen half-formed ways: a public plea that makes enemies; a quiet build that risks being overtaken; a compromise that pleases no one."
    "You stand in the center of Kaito Sato's lab as the rain grows and the lamps hum. Outside, the marsh watches like a held breath."
    "Kaito Sato's voice is softer now, as if he is counting the honest risk aloud."

    kaito_sato "Whatever you decide, I'll stand with it. But I need you to tell me: will you be the one to put this forward? Can I count on you to make the ask?"
    "The question lands like a stone into a still pond. Ripples spread to every ledger and shoreline you've ever tried to guard."
    "You look at the scattered jars, at the stakes in the marsh, at Tomas's hands. You see Hana's warm diner light, Mayor Elena's steady pin, Lucia 'Lux' Moreno's plaza across the water with its promise of instant—dangerous—safety. You see the community, small and stubborn in the rain."
    "You are the hinge. The forum is tomorrow. The town waits."
    "You inhale. The salt-saturated air fills your lungs, and you can taste all the small debts you owe—the brother you couldn't save, the neighbors whose nets you want to keep, the children who still play in the coves."
    "The lab's lamps buzz. Outside, a surge of tide flickers silver. The decision narrows to three paths in your chest."
    "You open the waterproof notebook and touch the pen to a fresh margin. The ink blurs slightly with the damp from your thumb."
    "You are about to decide whether to champion the pilot publicly, bring it as a compromise to Mayor Elena, or keep it quiet to build proof first."
    hide tomas_bianchi
    hide kaito_sato
    hide dr_noor_alvi

    scene bg ch7_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: Piano chords hold, unresolved; cello low and insistent]
    "You feel every eye on the town as if it were on you. Trust is a fragile circuit, and tonight the wiring hums with the possibility of shorting."
    "You close the book and look up."

    scene bg ch7_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter8
    return
