label chapter1:

    # [Scene: Main Street, Seabreak Hollow | Dusk]

    scene bg ch1_Start_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, a bus door sighing closed; a drip from a gutter]
    # play music "music_placeholder"  # [Music: Sparse, gentle piano with faint seabreeze undertone]
    "You step off the bus into a salt-scented fog that carries the town like a half-remembered melody. The air tastes of metal and brine; it presses cool against the back of your throat. Your hair is"
    "tied back in a loose knot — a practical knot, the kind that keeps loose strands out of tide charts and lab samples — and the leather field notebook in your hand weighs heavier than it"
    "should. It is not only leather and paper; it's a ledger of intent, a small fortress against the things that have already been taken."
    "The town appears in scalloped silhouettes: slumped Victorian cornices wearing peeling paint like layered maps, a thrifted fisherman sweater hanging on a line that snaps in a shallow wind, a neon co-op sign sputtering its promise"
    "to anyone who still needs it. Rain-darkened cobbles reflect the sickly orange of a streetlamp. Someone has left a hand-painted poster for a council meeting on a telephone pole; the corners curl like tired hands."
    "You inhale, cataloging textures the way you do data: the taste of salt in the gutters, the damp clinging to your jacket collar, the smell of frying fish and soap from the diner two blocks over."
    "You tell yourself you're not here for nostalgia. The word sits rasping in your mouth like a filter: not nostalgia—work. Reconnaissance. Rebuilding. You fold the notebook open, tracing the first blank page with a thumb as"
    "if the paper will accept your promise."

    menu:
        "Pause to touch the sweater on the line":
            "You let your fingers find the coarse knit. For a second the fabric registers as a timeline — childhood salt-sprays, a mother humming at the stove, then the hush after the storm. It grounds you in what you're trying to protect."
        "Keep walking toward the pier":
            "You resist the tug of memory and keep moving. Each step is forward calculation: the pier, the marsh, the maps you need to draw. The town becomes a set of variables you must translate into plans."

    # --- merge ---
    "You continue toward the pier, mind adjusted by whatever small anchor you allowed yourself."
    # [Scene: North Pier | Dusk]

    scene bg ch1_Start_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Boards creak underfoot, a buoy thunks in the channel; gulls wheel low]
    # play music "music_placeholder"  # [Music: Subdued strings, a single cello note underpinning the scene]
    "You walk the North Pier with boots salt-streaked, each tread setting a small rhythm against wood softened by decades of tides. The smell of drying nets unfurls from a shed to wrap itself around you —"
    "pungent, fishy, warm in a way that memory mistakes for safety. The pier is a timeline of repair: mismatched boards, a handrail patched with rope, an anchor bolt new enough to burn in the eye."
    "Aiden Reyes leans against a rusted winch like he belongs to the place as much as the iron. He looks up the moment you come into view — sun-faded black hair wind-ruffled, sea-blue eyes that crinkle"
    "when he smiles. He doesn't move like a man waiting to audition for conversation; he waits like someone who has kept time with tides and people."
    show aiden_reyes at left:
        zoom 0.7

    aiden_reyes "Look at you. All city-chemist and field agent. You planning to neutralize our seawater or just lecture the gulls?"
    show maya_kwon at right:
        zoom 0.7

    maya_kwon "Someone has to explain sediment deposition to the gulls."
    "Aiden Reyes pushes off the winch and walks toward you, hand dipping into the inside pocket of his jacket before popping out with a soot-darkened thermos. He offers it as if the act is a familiar barter."

    aiden_reyes "Coffee? Warm and suspiciously competent.' (his voice is rough with sea-salt humor) 'It's been a while."
    "You take the thermos. The metal is warm from his palm. The aroma is black and bitter and exactly what you didn't know you needed."

    maya_kwon "Thanks."
    "Aiden Reyes studies you for a long beat, the look on his face unreadable only if you insist on simple labels. There is concern there, and something like calculation — does she come back for love? For science? For home?"

    aiden_reyes "You look… smaller than I imagined, in a good way.' (he ducks his head, embarrassed) 'Don't take that weirdly."
    "You laugh, and it's a brief, honest sound. It cracks the ice on something cautious in you."

    maya_kwon "And you look exactly like the co-op patch stitched itself onto a weatherproof jacket."

    aiden_reyes "Old man Reyes says my jacket's a statement piece."
    # [Scene: North Pier — Stool by the Winch | Dusk]
    hide aiden_reyes
    hide maya_kwon

    scene bg ch1_Start_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Slow exhale, the board underfoot creaks as Old Man Reyes shifts]
    # play music "music_placeholder"  # [Music: A single sustained note, contemplative]
    "Old Man Reyes — Mateo, known and spoken of in the same breath as long tides and longer stories — watches from a stool, his pea coat a history of patches and warmth. He doesn't move much, but his presence compacts the air; time feels thicker near him."

    "Mateo Reyes" "Ay, Maya.' (the greeting is gravelly, soft as silt) 'Back sooner than the gulls predicted, eh?"
    show maya_kwon at left:
        zoom 0.7

    maya_kwon "Not sooner. Different kind of coming."
    "Mateo Reyes taps the stool with a gloved hand, an invitation to speak in small, patient measures."

    "Mateo Reyes" "We need folks with eyes like yours. The marshes are trying to tell us something.' (he folds his hands, the way someone folds an old map) 'They've loosened up in places we can't afford to give."
    "You look past them to the marshes visible beyond the pier: low, ribbed tidal flats threaded with reeds and glassy pools that catch the last of the light. Boardwalks slice through in uneven lines; some boards"
    "are warped, some replaced with new planks that glow pale with fresh sawdust. The marsh breathes, fragile and honest, not what you remember but alive in the small, stubborn ways that matter."
    "You feel the first real tightening of something behind your sternum — not panic, not grief exactly; a tidy pressure that says the work is real and the cost will be accounted in more than money."

    maya_kwon "I'm not here for nostalgia.' (you let the phrase out again, steadier this time) 'I'm here to listen, to learn what the marshes and the people will tell me. Reconnect channels, design a living shoreline—something that gives time back to what we've lost."
    show aiden_reyes at right:
        zoom 0.7

    aiden_reyes "Listen, huh?' (he shifts on his heels) 'That's going to involve more coffee and fewer slide decks. Old man Reyes can tell you the songs the marsh used to sing."

    "Mateo Reyes" "Songs? Ha. I sang the marsh a lullaby once when it wouldn't stop rising.' (his smile is a crack in a weathered shell) 'But songs need hands to build them into place. You'll have hands if you ask us."
    "You look at Aiden. At Mateo. At the marsh that flexes and exhales beyond them. The town is a bundle of needs: work, history, stubborn pride. The promise in your chest steadies. Listening is a plan that can be put to paper and measured against tides."

    menu:
        "Ask Mateo about the last channel shift":
            "You tilt your head, curious and clinical. Mateo's eyes light for a moment and he begins to sketch, the cadence of his story folding into Landmarks: old dikes, a culvert that clogged ten years ago, a boat lost where mud now lies. Each detail you store is a data point and a story."
        "Turn to Aiden and ask if the fishermen still share boats":
            "You ask Aiden about the co-op and the ways they keep boats afloat. His face softens; he talks about shared nets, late-night repairs, and a roster of people who take turns when storms take more than the sea can keep. The human network becomes a map as important as the physical one."

    # --- merge ---
    "You compile the details into a practical list in your head — stories, sketches, allies — then return your focus to the work ahead."
    "You draw a small mental list — collect stories, sketch maps, find allies. The list is not romantic; it has straight edges and practical language. Still, under the plain nouns, something else hums: hope measured in steps, small and patient."

    aiden_reyes "So what's the first step, city-chemist? Where do you start when you want to stitch the whole marsh back together?"

    maya_kwon "By listening.' (you fold the notebook closed like a brief, decisive hinge) 'By walking the lines, asking the names of what used to be, and not pretending my models replace someone's memory."

    aiden_reyes "We'll make sure the gulls don't criticize your methods too harshly.' (he offers a crooked grin) 'And if you need me for the heavy lifting or the tea, I'm around."

    "Mateo Reyes" "We'll need plans and arms and stubbornness. You got the stubbornness?"
    "You feel the answer in your chest before you say it. It's not a brash promise; it's a low, steady commitment."

    maya_kwon "I do."
    hide maya_kwon
    hide aiden_reyes

    scene bg ch1_Start_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant bell marking an unseen boat; the thermos hisses faintly when set down]
    # play music "music_placeholder"  # [Music: The piano motif returns, calm and expectant]
    "You stand there for a long moment with the two of them — a fisherman and an elder, both stitched to this place by different threads — and watch as the marsh receives the last of"
    "the light. The moment is small and luminous: a borrowed warmth, a shared thermos, the honest scrape of a stool against wood."
    "You promise yourself, quietly, that you have come not for memory but for the work that memory demands."
    "You look at the notebook in your hand, feeling its weight again. The first page is still blank, but your plan has already begun to write itself in small acts: listening, mapping, gathering allies."
    "A small tide of resolve moves through you. It is not triumphant. It is not desperate. It is the clean, neutral kind of determination that sets a course and begins to row."
    # [Page-Turn Moment]
    "You let the scene fold into you — the smell of wet rope, Aiden's easy deflection, Mateo's slow map of losses — and you feel the soft click of the next step falling into place. There"
    "is work to be done, and the first thing the marsh asked for was to be heard. You close your fist around the notebook and, without ceremony, stand to walk the boardwalk toward the channels that"
    "need reconnection."

    scene bg ch1_Start_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter2
    return
