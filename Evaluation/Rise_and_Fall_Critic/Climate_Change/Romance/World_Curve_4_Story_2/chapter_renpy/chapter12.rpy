label chapter12:

    # [Scene: Glass Marsh | Dawn]

    scene bg ch12_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A dull, steady thrum — engines far out at sea; gulls call once, then fall silent]
    # play music "music_placeholder"  # [Music: Low, minor strings; a single cello holds a note like a slow tide]
    "You arrive before anyone else has properly opened their eyes to the morning. The marsh takes the light and does nothing with it — it holds on, heavy and grey. Where swaths of seagrass used to"
    "ripple and catch the sun, the beds lie like battered carpets beneath a gray blanket of silt. The water's surface reflects a wrong sky; the mirror is clouded, as if someone smeared grief across it."
    "You smell the sour tang of disturbed sediment — iron and salt and something that reads as old, raw water. Your hands go to your notebook out of habit, fingers tracing the spine without opening it. Habit is a small, faithful anchor when larger things want to float away."
    "Dr. Leyna Ortiz appears at your shoulder with a tablet screen softened by condensation. She doesn't speak at once; she lets you look."
    show dr_leyna_ortiz at left:
        zoom 0.7

    dr_leyna_ortiz "Turbidity spiked at 0300. The trace matches a dredge plume — wide, persistent. We have chlorophyll down two-thirds in the shallow beds. The infauna counts crashed overnight."
    "You read the numbers because it's what you do; numbers give shape to panic. They do not, however, lessen the shape of what you see with your own eyes."
    show alys_maren at right:
        zoom 0.7

    alys_maren "How fast could this spread? If the beds go, the fish move, the birds follow—"
    "Dr. Leyna Ortiz: (interrupting softly) 'Not move. Collapse. The mats won't photosynthesize under this load. We're looking at a die-off that starts within days and becomes irreversible in weeks if resuspension continues.'"
    "Her voice is precise, clinical, and a rope that steadies you even as it tightens. Behind her, the marsh holds its breath."

    menu:
        "Call the harbor — get the volunteers now":
            "You fumble for your radio and almost hit send, fingers hovering over a channel that will wake the town. Urgency floods your chest — you can almost hear the planting schedules rearrange themselves."
        "Walk the beds — see how much is salvageable":
            "You tuck the tablet under your arm and step onto the boardwalk, each planked footfall thrumming with the marsh's small sounds. Seeing the damage with your bare senses steadies the storm in your chest."

    # --- merge ---
    "You walk the edge of the marsh, boots whispering salt against wood. A rope of dead eelgrass tangles like a necklace cast aside. You stoop and lift a blade of the silt-heavy grass; it gives under"
    "your fingers with the wet faintness of something already dying. Ronan Pike arrives, breathless, shirt streaked with mud, and without preamble he kneels beside you."
    "You walk the edge of the marsh, boots whispering salt against wood. A rope of dead eelgrass tangles like a necklace cast aside. You stoop and lift a blade of the silt-heavy grass; it gives under"
    "your fingers with the wet faintness of something already dying. Ronan Pike arrives, breathless, shirt streaked with mud, and without preamble he kneels beside you."
    show ronan_pike at center:
        zoom 0.7

    ronan_pike "We can run pumps, try to clear the light. Leyna says we have a window—if we get enough volunteers, if we can stop resuspension..."
    "You look at him. He is young in ways that make urgency look like bravery. You are older and know the arithmetic of weather and recovery; hope and data do different kinds of work."

    alys_maren "How long is a 'window' if the dredging keeps going?"

    dr_leyna_ortiz "Hours, if we're lucky. Days if we can contain the plume's source and prevent resuspension during tidal cycles."
    "Your mouth tastes like metal. You have a thousand plans folded into the single map of this coastline, but plans are brittle against industry machinery. There is a human weight in your chest — not just"
    "the loss of green blades, but the knowledge of what those blades mean: nursery habitat, sediment stabilizers, the town's food web."
    hide dr_leyna_ortiz
    hide alys_maren
    hide ronan_pike

    scene bg ch12_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A barge horn, distant and persistent; a low vibration through the boardwalk]
    show dr_leyna_ortiz at left:
        zoom 0.7

    dr_leyna_ortiz "We should go to the harbor. Document. Stop the source, if possible. If not—triage."
    "You nod because the word “triage” contains the truth of the morning. You tuck your notebook into your jacket."
    # [Scene: Boardwalk | Late Morning]
    hide dr_leyna_ortiz

    scene bg ch12_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A chorus of overlapping voices — some carrying, some edge-broken. Shoes slap wood. A distant radio crackles with static.]
    # play music "music_placeholder"  # [Music: Agitated strings, a litany of dissonance]
    "You find Ivo leaning against a piling, cap low, jaw set. His hands worry the leather of his utility belt. There's a line of salt across his cheekbone like a medal. Maya is beside him, voice"
    "steady as she takes names and tasks. The town's temperature has turned from mourning to accusation."
    show ivo_calder at left:
        zoom 0.7

    ivo_calder "They tell me the contractor's out past the shoals. No one authorized them to come inside the breakwater. Not my crew, not the dock hands I trust."
    "You watch his fingers curl into the wood. The accusation isn't fully formed, and you don't let it be about one signature or another — it would be a past detail you can't be certain of. What matters is the present: machines are working and the marsh is failing."
    show alys_maren at right:
        zoom 0.7

    alys_maren "We document everything,' you say, and the words are both command and plea. 'Leyna, coordinates. Ronan, get the drone up and film the plume. Maya — start a roster, triage teams to the shallow zones."
    "Maya Maren: (fast, practical) 'Volunteers can work the turbidity curtains. We have pumps and squeegee rigs in the storehouse. If we can slow resuspension, maybe we can buy time.'"
    "A woman's voice rises from the crowd — sharp, urgent."

    "Voice from crowd" "What about houses? What about the nets? We need seawalls more than seagrass! If the bay kills our catch, it's not just ecology — it's our paychecks."
    "You look toward the speaker, then at Ivo. The room's division is not new; it's been simmering beneath policy and tides. Now it boils."
    "Ivo Calder: (to the crowd) 'I'm not saying sea grasses don't matter. I'm saying we need to keep families fed this month. If building barriers means people stay, then we build barriers.'"
    "You know him. You know his hands have fixed hulls and run rescue launches. He values immediate shelter with the fidelity of someone who has seen what storms take in a single night. His voice is not an attack; it is an argument for survival."
    "Alys Maren: (quietly) 'Both are disaster prevention, but on different clocks. If we fortify without the habitat that softens waves and gives the bay life, we cost the next generation more than a season's harvest.'"
    "A low murmur. Leyna moves between you and Ivo and the crowd, tablet held like a shield."
    show dr_leyna_ortiz at center:
        zoom 0.7

    dr_leyna_ortiz "We need both. Immediate protections that reduce acute loss, and aggressive restoration for the long-term resilience. But first — stop the dredging or we can't begin."
    "There are eyes on you. Some are lit by hope, some by the more animal thing: fear. Maya's hand finds your sleeve and squeezes."
    hide ivo_calder
    show maya_maren at left:
        zoom 0.7

    maya_maren "We'll do the work. We'll hold lines. But people want action now. They want something they can point to that says 'you're safe tonight.'"

    alys_maren "We'll make something they can see. We'll start the barriers where they're most needed and triage the beds we can save."
    "Ivo's jaw tightens. He looks at you — an unreadable, complex face folding into shadow. You have no sure line to read whether your plan and his can be truly reconciled in the faces of the people who must live with both the walls and the absence of the marsh."

    menu:
        "Step up and reassure the crowd":
            "You move to the center and raise your voice, the words falling steady into the hush. You offer the town a line — a plan that is both immediate and long — and for a moment the room leans in."
        "Let Ivo take the floor and watch":
            "You step back and let Ivo speak, feeling the weight of the choice you made to trust him with the town's short-term safety. Watching him, you measure how much you are willing to hand over to someone else."

    # --- merge ---
    "Voices tangle. Someone in the back shouts about permits; someone else shouts about livelihoods. The council's authority feels both necessary and remote. You think of Celine — her posture, the dossier she once offered, her promises"
    "of rapid investment — and the rule that keeps you honest: you can't attribute the dredge to one decision you may or may not have made. The town's fracture is bigger than any one signature; it"
    "is about survival's competing timelines."
    "Voices tangle. Someone in the back shouts about permits; someone else shouts about livelihoods. The council's authority feels both necessary and remote. You think of Celine — her posture, the dossier she once offered, her promises"
    "of rapid investment — and the rule that keeps you honest: you can't attribute the dredge to one decision you may or may not have made. The town's fracture is bigger than any one signature; it"
    "is about survival's competing timelines."
    # [Scene: Harbor | Late Afternoon into Night]
    hide alys_maren
    hide dr_leyna_ortiz
    hide maya_maren

    scene bg ch12_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Pumps thrum; someone curses softly as a pump clogs. The wind carries the metallic tang of the harbor. A container clangs; a radio near you bleats with a call and then static.]
    # play music "music_placeholder"  # [Music: Low, elegiac piano with undertow strings]
    "You have been here for hours. The work folds into a rhythm — shovel, hold, rinse, plant — until the rhythm is a dull ache in your forearms. The triage buys slivered wins: a stretch of"
    "seagrass is cleared enough to catch light; a clutch of juveniles flares into activity behind a curtain. But the wins are thin, patchwork things against a larger loss spreading beneath the surface."
    "Ronan limps to you, a smear of bruised skin across his forearm where a piece of plexi cut him; he laughs too bright and too short."
    show ronan_pike at left:
        zoom 0.7

    ronan_pike "We got the drone footage to the council. Leyna says the plume's moved—less concentrated near the marina but it went deeper into the shoals. The mats... some didn't make it."
    "You take his hand, and his fingers are shaking because youth has not yet learned the economy of grief. You want to say something that will anchor him. You find only practical instructions."
    show alys_maren at right:
        zoom 0.7

    alys_maren "Go sit. Clean the cut. You did good today."
    "He nods, mouth tight, and walks away like someone carrying both pride and a small, new fear."
    "Ivo appears at the edge of the salvage line, hands clenched, watching as volunteers make a futile, loving incision into a wide bruise. He doesn't speak at first. When he does, his voice has the brittle edge of someone trying to split wood with a butter knife."
    show ivo_calder at center:
        zoom 0.7

    ivo_calder "We can't keep doing this, Alys. We stop one plume and two more come from somewhere else. People need walls that hold until the sea calms its temper."

    alys_maren "Walls buy time, Ivo. But they also change the energy of the shoreline. If you contain wave energy without living buffers, you redirect force somewhere else. We need to be careful who pays the price."

    ivo_calder "Careful. Always 'careful' with you. Folks need meals, not lectures. How do you expect me to tell a mother her child's room will be safe in six years because of 'ecosystem services'?"
    "A weight settles in your throat. This is not merely a policy argument — it's a struggle over what safety feels like to the people who sleep in these houses. You want to explain, to fold"
    "him into your calculations, to make him see that your urgency isn't ideology but survival distributed across time. Instead, your voice cracks."

    alys_maren "Because I can't promise concrete will heal the bay. I can promise we try to heal what actually protects it."
    "Ivo's eyes flash with something that could be anger or fear; the line between the two is porous."

    ivo_calder "And I can't promise a green carpet will keep a family from losing a season. I'm trying to keep people in their houses tonight, Alys. Can't you see that?"
    "He turns away as if the argument has ended. Your hand hovers, wanting to go after him and be both ally and partner; it finds only air."
    hide ronan_pike
    hide alys_maren
    hide ivo_calder

    scene bg ch12_f99e88_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The ocean beyond the breakwater, patient and indifferent; distant, a phone vibrates and goes unanswered]
    "Maya finds you by the sluice gate, her face set to a softness you recognize from childhood when storms took the roof and you both waited for the mend."
    show maya_maren at left:
        zoom 0.7

    maya_maren "People are tired. You're tired. Ivo's trying to do what he knows best. You can't carry this so everyone else feels safe."
    show alys_maren at right:
        zoom 0.7

    alys_maren "I know. I felt—"
    "Leyna approaches with a printed sheet, hands shaking a fraction as she hands it to you."
    show dr_leyna_ortiz at center:
        zoom 0.7

    dr_leyna_ortiz "We have early mortality rates. The juvenile flatfish counts in the nursery are down forty percent in the hit zones. The benthic invertebrate samples are anemic. That means immediate food web collapse for some species."
    "You read the page and feel the numbers as stones being thrown at a window. Each impact cracks something inside you. The harbor's salvaging has been valiant; it has also been insufficient. You had measured the"
    "margins for recovery and hoped the town's muscle could close them. Nature did not heed hope."

    menu:
        "Stay and keep leading the salvage through the night":
            "You hand out gloves, hand signals, the little means of organizing exhaustion. Each person you marshal becomes another small anchor in a storm-lengthening night."
        "Walk the pier alone, let others continue":
            "You slip away into the harbor's shadow, the sounds of labor receding. The loneliness of being someone who sees futures feels heavier when you watch people work without trusting your mind to rest."

    # --- merge ---
    "You step to the waterline as the tide turns, the moon pale and doubtful above the harbor. The sea beneath the moon hides the damaged beds like a bruise pressed deep. You think of your father's"
    "compass — dented and stubborn — and how it always pointed to something steady even when storms moved the shore."
    "You step to the waterline as the tide turns, the moon pale and doubtful above the harbor. The sea beneath the moon hides the damaged beds like a bruise pressed deep. You think of your father's"
    "compass — dented and stubborn — and how it always pointed to something steady even when storms moved the shore."
    "Ivo appears beside you without steps announcing himself; his presence is a footprint next to yours."
    "Ivo Calder: (softly) 'We did what we could.'"

    alys_maren "We did what we could. It wasn't enough."
    "He swallows. The silence between you is not empty; it is a ledger. He looks at you, and for a moment the layers of leadership and politics peel back, leaving two people who have stood on the same decks through different kinds of storms."
    hide maya_maren
    show ivo_calder at left:
        zoom 0.7

    ivo_calder "Maybe that's all there is sometimes. We do what we can and then—"

    alys_maren "—then the sea decides."
    "He laughs once, a sound like a rope snapping under too much strain. There is something raw in that laugh."

    ivo_calder "Don't make me a villain for wanting houses that hold."

    alys_maren "I'm not trying to make you into anything. I'm trying to keep the thing that feeds the houses alive."
    "He reaches out and tugs the braided cord around your wrist — a small, private gesture you've seen him make with other things: boats, nets, people. It is an attempt to connect."

    ivo_calder "I don't want to fight you, Lys."
    "Alys Maren: (the name tastes raw and tender) 'I don't want to lose you.'"
    "The harbor throws their words back at them; voices from the salvage line drift like flotsam. You both know that love here is tested by weather in a way lovers in oldbound cities are not. Climate is a third person in your relationship, relentless and indifferent."
    hide alys_maren
    hide dr_leyna_ortiz
    hide ivo_calder

    scene bg ch12_f99e88_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: At the edge of hearing, somewhere a child's cry and then a mother's call; the life of the town goes on while you reconcile the day's losses]
    # play music "music_placeholder"  # [Music: A single violin thread that bows downward into silence]
    "You and Ivo stand in the salt wind, two figures that once fit into the same plan and now must be measured against compromise. The salvage work continues — small inflamed victories, a handful of blades"
    "coaxed back to light. But when dawn comes, the bed will be scarred. Entire nursery patches are gone. The economics will follow ecology's math and the town will feel it in market days and in meals."
    "Ronan returns, eyes hollowed with tiredness, and he hands you a small spray of green — a single living blade from a protected patch. It is wet and alive and improbably brave."
    show ronan_pike at left:
        zoom 0.7

    ronan_pike "Found it under an eelgrass knot we managed to lift. It was small."
    "You cradle the blade as if it were a life you can keep in your hands. It feels like both a promise and an accusation."
    show alys_maren at right:
        zoom 0.7

    alys_maren "We plant it. We'll watch it. We'll tell the story of what happened here so no one forgets the cost."
    show maya_maren at center:
        zoom 0.7

    maya_maren "And we'll feed people tonight. That's not nothing."
    "You watch the town pivot in small, stubborn ways: meals handed out, a repair schedule posted, a call for testimony at the next council meeting. The fracture lines that opened today will be argued over in"
    "months: over who authorized which work, which livelihood is prioritized, which value is sacrificed. Friendships will fray; alliances will rearrange like driftwood."
    "Ivo squeezes your hand briefly and lets go."
    hide ronan_pike
    show ivo_calder at left:
        zoom 0.7

    ivo_calder "Don't let this be the thing that breaks us."

    alys_maren "I don't know whether it's the thing that breaks us or the thing that binds us. Maybe both."
    "His face goes complex and unreadable — grief and love and the exhausted calculation of someone who must choose how to spend courage. You do not have the power to make his next choice. You have the power to decide how you respond."
    # [Scene: Harbor Edge — Midnight]
    hide alys_maren
    hide maya_maren
    hide ivo_calder

    scene bg ch12_f99e88_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The sea breathes. Your own respiration is loud in the hush. A distant clock — someone's wall clock — marks the passing of an hour that will not be replaced.]
    # play music "music_placeholder"  # [Music: Sparse, a single piano chord that lingers then fades]
    "You stand with the small green blade pressed into the soil of a shallow tray. The harbor's lamps throw your shadow long and broken. You think of seasons: the way salt eats at roofs slowly, the"
    "way seedlings fight for light patiently in the dark. You think of promises — the ones written in council minutes and the ones stitched by hands that bind nets and braid cords."

    "Your notebook is heavy in your pocket but empty of anything that feels like adequate language. You open it anyway and draw a single line" "Loss — Witness — Rebuild."
    "You think of the people's faces today: accusation, hunger, fear, a stubborn hope folded into triage lists. You think of Ivo's hands, of Leyna's precise grief, of Ronan's bruised optimism, of Maya's steady work. You think of the small blade you hold needing light."
    "The shore is quiet now in a way that makes history feel louder. The night lays a kind of verdict across the town: we will be different after this. Some things can be mended by work; others are altered in ways that leave a permanent seam."
    "You breathe in the harbor air — salt, cold, the faint chemical tang of machines — and let grief be the thing that steadies you. There is a decision to be made about how to carry"
    "today's cost into tomorrow's stewardship. There will be hearings, and blame, and perhaps accountability. There will be reconstruction, but whether it stitches the town back to itself is uncertain."
    "You tuck the living blade into the tray and set it on the rescue table. It glows under the task lamp like a single small future."

    scene bg ch12_f99e88_8 at full_bg
    "You let yourself say the thing you have been avoiding: that sometimes the beds break and cannot be fully put back, that sometimes the price of breath for one generation is the loss for the next."
    "You do not make it a sermon; you make it an observation and a vow."
    "Alys Maren: (softly, to no one and to everyone) 'We will tell the story of this night. We will name what was lost. We will keep at least one small green thing alive.'"
    "The town will not be the same. Some friendships will not weather the pull. Love will be tested beyond language. But the decision to try — to stand and plant seeds under a sky that has already unmade things — is itself a kind of fidelity."
    # play music "music_placeholder"  # [Music: A low, final chord; no resolution, only the steadying of breath]

    scene bg ch12_f99e88_9 at full_bg

    scene bg ch12_f99e88_10 at full_bg
    "THE END"
    # [GAME END]
    return
