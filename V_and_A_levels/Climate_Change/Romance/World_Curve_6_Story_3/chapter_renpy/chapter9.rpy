label chapter9:

    # [Scene: Harbor & Living Sea Wall | Early Morning]

    scene bg ch9_6b08b4_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, urgent strings; a repeating, rising ostinato]
    # play sound "sfx_placeholder"  # [Sound: Soft water lapping, the distant knock of oars, muffled conversations]
    "Narration:"
    "You came here because you chose the quiet pilot—because the memorandum was signed and because you believed patience could buy dignity. The choice from the council still sits in your chest like a warm stone: a"
    "decision folded into your messenger bag with the tide charts. This morning it weighs the same as it did in the meeting—necessary and fragile."
    "Your boots sink into the same sodden boardwalk you've known since childhood. The air tastes of salt and iron and the faint electric scratch that precedes a storm. Hands—callused, small, steady—press plugs of marsh grass into"
    "the lattice of the seawall. Each plant is an argument against erasure. Each one an experiment."
    "You move through the crew with a field notebook in one hand and a clamshell thermos in the other. The apprentices—Luca’s cousins among them—ask about planting density and salinity tolerance, their voices bright, breathless. Elias Voss"
    "stands two docks over, barking gentle orders while measuring a storefront’s base for the raised-workshop retrofit. His hair is still damp with sea spray; he laughs when a board gives under his weight and the laugh"
    "catches at the end like an apology."

    scene bg ch9_6b08b4_2 at full_bg
    # play music "music_placeholder"  # [Music: Strings quicken; a high violin thread darts like worry]
    "Narration:"
    "For weeks, this is how you move: early light, methodical work, soft victories logged as data points on Henrik's borrowed tablet. Councilwoman Tamsin Hale watches from the municipal roof across the harbor—her silhouette compact and unreadable—sometimes"
    "stepping down to listen, rarely to intervene. Her presence is a constant, a taut line you don't want to pull but can't ignore."

    "You slip a note into the lab's inbox while the crew breaks for coffee" "Compile week 3: hydrodynamic variance, marsh uptake rates, community employment log."

    menu:
        "Hand Elias the thermos":
            "You offer him the thermos across the planks. He accepts it with a small, grateful smile and a hand that lingers on yours for a second before both of you return to work."
        "Keep it for yourself":
            "You take a long pull from the thermos and keep your answer to yourself. Elias catches your eye and there's a question there you don't answer; you both go back to the plants."

    # --- merge ---
    "Both outcomes converge and the story continues to the next scene."
    # [Scene: Maya's Field Lab & Greenhouse | Mid-Morning]

    scene bg ch9_6b08b4_3 at full_bg
    # play music "music_placeholder"  # [Music: A fractured piano motif, then rising percussion]
    # play sound "sfx_placeholder"  # [Sound: Keyboard clicks, low hum of a desalination pump, the distant bray of a radio]
    "Narration:"
    "You log data with a speed that feels like faith. Pairs of sediment cores, pH profiles, results from a tide fence trial—every entry is both a ledger and a prayer. The apprentices cluster around the lab"
    "bench, asking scientific questions you answer and then return to, because the questions themselves keep the fear from turning inward."

    "Councilwoman Tamsin Hale's assistant calls" "Regional committee meeting moved up. Possible reallocation if emergency criteria are met."
    "Elias Voss comes in, cheeks flushed from retrofitting a storefront ladder. He's carrying a sample of reclaimed timber—smooth and seaworn. He sets it down like an offering and says, 'Payroll's through for this month. Trades are showing up, Maya. People are breathing again.'"
    "You smile because that's what you do, because the pilot has teeth—both in the workshops and in the living wall—and because the solar arrays on rooftop gardens glitter like promises. For a beat, the town feels sewn back together."

    menu:
        "Upload the preliminary data to the regional portal":
            "You hit 'upload' and watch the progress bar crawl. The data is out there—transparent, raw. You feel exposure and relief in equal measure."
        "Hold the data and send a summary to council tonight":
            "You close the file and draft a measured summary instead. The decision feels like closing a door you might later need to reopen."

    # --- merge ---
    "Both outcomes converge and the story continues to the next scene."
    # [Scene: Storefronts / Retrofit Workshops | Late Morning]

    scene bg ch9_6b08b4_4 at full_bg
    # play music "music_placeholder"  # [Music: Mechanical rhythms; drums build into a storm roll]
    # play sound "sfx_placeholder"  # [Sound: Hammers, the creak of jacks, low-conversation murmurs]
    "Narration:"
    "Elias Voss moves through the workshops like a conductor. He organizes teams, lays out schedules, keeps one eye on materials procurement and another on people's faces. When a widow on Harbor Lane worries about rent during"
    "construction, he promises payroll and flexible schedules; when a teen fears losing his place at the dock, Elias assigns him an apprenticeship. He frames the retrofit not as charity but as an investment in continuity."
    "You measure out the elevation for a bakery so the oven won't flood next season. Flour dust clouds the air and smells faintly of home. For a few hours, the town is a place that makes things—bread, boats, repair—and not only a place waiting to be repaired."
    "Councilwoman Tamsin Hale approaches the retrofit site at midday. She stands at the edge of the scaffold with a notebook, says little, watches a tradesman lift a beam. Her expression reads as Tamsin: complex. You think of the Schrödinger rules and call it what it is—unreadable, layered."
    show councilwoman_tamsin_hale at left:
        zoom 0.7

    councilwoman_tamsin_hale "The pilot looks… competent."
    show maya_ortega at right:
        zoom 0.7

    maya_ortega "It's not spectacle. It's survivability—crafted by the people who will live with it."

    councilwoman_tamsin_hale "Survivability scales differently under political timeframes."
    "Her eyes slide to Elias Voss. 'You're holding a lot of promises, Voss.'"
    show elias_voss at center:
        zoom 0.7

    elias_voss "We can make them real. We already are."

    councilwoman_tamsin_hale "Regional oversight is prying. There's pressure to demonstrate immediate, large-scale impact. If the committees declare an emergency, the matching funds can be moved to a rapid seawall procurement. Less community input, yes, but—' (she snaps the notebook closed) '—faster."
    "Narration:"
    "You feel every sentence like a blow. The tradesman snares his beam in a chain; the sound is a small metallic scream."

    elias_voss "We built the case. We showed them the data."

    councilwoman_tamsin_hale "Data doesn't move votes when headlines demand action."
    "Narration:"
    "You open your mouth to argue, then close it. The retrofit crew continues, unaware of the teeth sharpening at the edge of the harbor."
    hide councilwoman_tamsin_hale
    hide maya_ortega
    hide elias_voss

    scene bg ch9_6b08b4_5 at full_bg
    # play music "music_placeholder"  # [Music: Strings snap to full bow; percussion grows oppressive]
    # [Scene: Harbor Front | Afternoon — The Turning]

    scene bg ch9_6b08b4_6 at full_bg
    # play music "music_placeholder"  # [Music: Full orchestra—brass and percussion slam in driving rhythms]
    # play sound "sfx_placeholder"  # [Sound: Engines roar, machine hydraulics, shouted commands, a distant siren]
    "Narration:"
    "They come in like a new tide—slick trucks and corporate teams with hard hats too clean for the mud. Someone else flung a switch in a room you don't have access to; a political panic called"
    "a bureaucratic hammer. The regional authority declared an emergency. Matching funds were reallocated. The quick-spend contract went to a team with days, not months, on their schedule and no intention of asking your permission."
    "A crew foreman steps out with a tablet and a laminated schematic. He reads the shoreline like it's a page to be edited. Bulldozers lower teeth into the marsh where you and your apprentices have coaxed"
    "life back into the water's edge. The first bite of mud expelled into the air smells foul—diesel and crushed vegetation. A child sobs behind a parent's shoulder."
    "Rosa arrives with a clipboard and a face like thunder. 'They didn't even call us,' she spits, voice breaking. 'They rerouted the funds. They called it 'emergency.' It is a hell of a lot more like a decision someone made behind closed doors.'"
    "You move toward the machines as if pulling at a net. Someone in a bright vest blocks your path."

    "Worker" "Ma'am, you're too close. This is an authorized operation."
    show maya_ortega at left:
        zoom 0.7

    maya_ortega "Authorized? Authorized by who? Our pilot—"

    "Worker" "Orders are orders."
    "Elias Voss reaches for your arm. His grip is rough and shaking. 'Maya—'"
    "Narration:"
    "You yank away because the sight of earth being eaten is too fresh, too private. 'We fought for respect,' you say. 'We asked for time. We asked to show that dignity can be part of adaptation.'"
    show elias_voss at right:
        zoom 0.7

    elias_voss "This was always the risk. We both knew—"

    maya_ortega "Knew and still tried!"
    "Narration:"
    "He runs a hand through his hair, the braid at his nape catching on his collar. 'We tried to keep people working, not waiting for welfare. I thought— I thought they'd see the value in that. I thought they'd give us a chance.'"

    maya_ortega "Chance doesn't cut through a budget meeting."
    "Councilwoman Tamsin Hale steps forward from the municipal roof crowd—closer now, her raincoat pressed tight. She looks at the machines, at the shoreline that was yesterday ours, and then at you."
    show councilwoman_tamsin_hale at center:
        zoom 0.7

    councilwoman_tamsin_hale "A mobilized emergency gets fast political points. A pilot gets newsletters and slow votes. When the regional director called—"

    maya_ortega "You let them take it."

    councilwoman_tamsin_hale "We debated. We tried to hold funds. The county threatened to move faster than we could. They made it a binary: fund at scale now, or lose federal support entirely."
    "Narration:"
    "Her fingers tap a rhythm on the tablet like an exhalation. 'I made a call.'"

    maya_ortega "You made a choice to cut the line."

    councilwoman_tamsin_hale "I made a choice to prevent—' (she pauses, eyes not meeting yours) '—greater loss."
    "Narration:"
    "Her explanation hangs in the air like an accusation and a prayer. The bulldozer's blade drops again, bringing with it a little avalanche of sedge and earth. The apprentices scream. Someone throws themselves at the machine's path, arms up in a useless defiance."
    # play music "music_placeholder"  # [Music: Brass clatters; a shrill violin screeches; everything accelerates into feral noise]
    # play sound "sfx_placeholder"  # [Sound: Shouts multiply, metal on mud, a child's wail]
    # [Scene: Confrontation & Fracture | Harbor Edge / Retrofit Alley]
    hide maya_ortega
    hide elias_voss
    hide councilwoman_tamsin_hale

    scene bg ch9_6b08b4_7 at full_bg
    # play music "music_placeholder"  # [Music: Percussion stabs at irregular intervals; the ostinato fractures into chaos]
    # play sound "sfx_placeholder"  # [Sound: Rain, distant hail, the angry rasp of engines, the flapping of tarps]
    "Narration:"
    "You and Elias Voss find each other amid the chaos and the sorrow—a brief, brutal island. Past the shouting, past the people trying to place themselves between machines and memory, you two are small and naked and furious."
    show elias_voss at left:
        zoom 0.7

    elias_voss "Why didn't you push harder at the meeting? Why let them frame this as either-or?"
    show maya_ortega at right:
        zoom 0.7

    maya_ortega "Because I thought—because you told me a hybrid could be proof, Elias Voss! I believed in the slow stitch!"
    "Narration:"
    "He looks as if you've thrown a stone at him. 'I organized payroll! I pulled people in—'"

    maya_ortega "And they used that to say we had jobs, so a rapid wall would be necessary? You organized so they could write our work off as preliminary?"

    elias_voss "That's not what—"
    "Narration:"
    "He stops because he can't finish without the words sticking like netting in his throat. The rain turns your hair into a dark halo. Your compass pendant hits your sternum like a heartbeat and you press it as if to stop time."
    "Councilwoman Tamsin Hale stands a few yards away, her coat soaked but immovable. She meets your eyes—a look that is complex and clean and final, like a surgical cut."
    show councilwoman_tamsin_hale at center:
        zoom 0.7

    councilwoman_tamsin_hale "We tried to strike a balance. I chose what could be delivered before the next storm cycle. It was a political reality."

    maya_ortega "Political reality is bulldozers on our marsh."
    "Narration:"
    "A tradesman you know—Luis—walks up, face gone pale. 'They offered jobs,' he says hollowly. 'They told us the seawall would protect our docks. They didn't say it would take the marsh.'"
    hide elias_voss
    show rosa_delgado at left:
        zoom 0.7

    rosa_delgado "This isn't protection. It's erasure. They took the part of the town that talked back."
    hide maya_ortega
    show elias_voss at right:
        zoom 0.7

    elias_voss "I didn't know they'd take it all. I didn't think—"
    hide councilwoman_tamsin_hale
    show maya_ortega at center:
        zoom 0.7

    maya_ortega "Did you think we were bargaining for a trophy wall while the heart of the town was stripped away?"
    "Narration:"
    "His face crumples. You see in him the man who left and returned, who learned how to talk in budgets and plans, who believed he could translate care into contracts. Now that translation has been warped."

    elias_voss "We thought negotiation was protection, not surrender."

    maya_ortega "Negotiation isn't always surrender—unless surrender's what they're willing to accept."
    "Narration:"
    "He opens his mouth to say something else, perhaps pleading, perhaps blaming, perhaps both. The rain makes the words leave him as a white mist."
    # play music "music_placeholder"  # [Music: A single, piercing dissonance holds—then collapses into silence]
    # [Scene: Aftermath | Rooftop Community Garden & Tidal Observatory | Dusk]
    hide rosa_delgado
    hide elias_voss
    hide maya_ortega

    scene bg ch9_6b08b4_8 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano, a low cello line; the pace slows but the ache does not]
    # play sound "sfx_placeholder"  # [Sound: Distant generator thrum, the soft drip of rain from eaves]
    "Narration:"
    "You climb to the rooftop garden because up here the changed horizon is cruelly visible. The seawall continues like a concrete tooth where reeds once softened the line between sea and town. It is effective in"
    "a way that rooms you out. It will hold. It will stop waves. It will cut the town's salt-breath off at a measured angle."
    "Your hands are empty. Your messenger bag is lighter. The pilot's logs sit in the lab—data, drafts, a ledger of work done and invitations ignored. You feel both ridiculous and furious for having faith in proof as a weapon."
    "Elias Voss arrives without the loudness he had in the morning. His steps are hesitant as if each one might shift the new geography. He doesn't reach for you. He stands beside you and looks out."
    show elias_voss at left:
        zoom 0.7

    elias_voss "They'll say it saved lives."
    show maya_ortega at right:
        zoom 0.7

    maya_ortega "They'll say what it saved, too."
    "Narration:"
    "He looks at you, and for the first time in hours the old, slow smile attempts to surface and fails."

    elias_voss "We kept people employed. I kept that promise."

    maya_ortega "Your promise and the promise of a place that retains its edges are different things."
    "Narration:"
    "He swallows. 'I didn't want to watch the town fall apart either. I thought this was the middle ground.'"

    maya_ortega "Sometimes the middle ground is the place you get sanded down."
    "Narration:"
    "Silence opens between you—a fissure steady and inevitable. You go to reach for him and stop, because neither of you knows whether that reaching will soothe or wound."
    "Councilwoman Tamsin Hale's earlier words echo back: I made a choice to prevent greater loss. You wonder what that calculus costs when it erases what made a place a home."

    "You remember Henrik's voice, older and clear" "There are no clean answers, Maya."
    hide elias_voss
    hide maya_ortega

    scene bg ch9_6b08b4_9 at full_bg
    # play music "music_placeholder"  # [Music: Single piano note suspended and held]
    "Narration:"
    "You do not have an answer to hand Elias Voss. You do not have a plan that will roll back the machines. What you have is memory, a field of cultivated living things that were cut"
    "into, a ledger of names who learned trades under the hope of rising together. Those things remain—muddied, diminished, stubborn."
    "You think of the apprentices, the bakery's oven you tried to raise, the kid who threw himself at the bulldozer—his face is a punctuation that no policy whitepaper will correct. You think of Rosa's hands, of"
    "Luis's silence. The town will survive. It may even do better in measures Councilwoman Tamsin Hale will tout. But it will not be the same town you fought to keep."
    show elias_voss at left:
        zoom 0.7

    elias_voss "What do we do now, Maya?"
    "Narration:"
    "You fix him with the compass at your throat, and the only honest answer feels too small. You think of a third way—improvisation, stubbornness, slow community labor—but the weight of what was taken compresses the room of possibility. Your voice comes out even and brittle."
    show maya_ortega at right:
        zoom 0.7

    maya_ortega "We keep doing the work that's left. We keep the apprenticeship going. We keep teaching people the craft so, if they want, they can change the next wall's design. We keep the records. We don't let 'em write over us quietly."

    elias_voss "Is that enough?"
    "Narration:"
    "You don't know. The rain softens into a cold, small grief."
    "Narration:"
    "You stand together on the rooftop, watching the seawall's silhouette eat the horizon. The love between you—that fragile architecture you were building with plans and trust—feels suddenly like another shoreline under threat. Elias Voss's hand brushes yours and then moves away."
    "The town will reorganize. People will return to work in the new pattern. Funders will circulate press releases about protection and jobs and swift action. Councilwoman Tamsin Hale will stand at podiums and say she did what had to be done. You will keep a ledger of what was lost."
    "You let the compass pendant press hard against your sternum until it leaves a cold imprint."
    # play music "music_placeholder"  # [Music: A low sustained chord; then the strings dissolve into nothing]
    hide elias_voss
    hide maya_ortega

    scene bg ch9_6b08b4_10 at full_bg

    scene bg ch9_6b08b4_11 at full_bg
    "THE END"
    # [GAME END]
    return
