label chapter8:

    # [Scene: Sunken Promenade | Late Afternoon]

    scene bg ch7_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant pounding of hydraulic presses. The rasp of chains. Seagulls calling, thin and urgent.]
    # play music "music_placeholder"  # [Music: Sparse strings in a tight tremolo, building tension]
    "You come to the boardwalk because it feels like the only honest place to stand and watch what you did not choose to stop. You had stepped back — you remember saying the words aloud in"
    "the Community Hall, feeling the room tilt the way a boat does when it lists. Let Kaito lead; you would advise quietly. Let him carry the trust you once tried to shoulder."
    "Now the machines are louder than the speeches ever were."
    "Concrete tastes like salt and defeat in your teeth; the air smells of crushed shell and fresh-cut rebar. Where reed and mud and blue-flag iris used to flex with tide, there are clean, vertical seams of"
    "poured gray. You walk slowly along the sunken promenade, boots sinking into slush where children used to run, and your hands lift to the shell at your throat as if to check that it's still there"
    "— a small inheritance, a small accusation."
    "'Marin.'"
    "Luka is already here, leaning on the tilted lamp-post like he leans on every truth he can't stop from happening. His coat is still damp at the hem. He has the look that means he's been"
    "keeping a hundred small accounts in his head and he's decided which ones to speak aloud."
    show luka_sorensen at left:
        zoom 0.7

    luka_sorensen "You shouldn't stand where the tide cuts the boards. They'll kick you off for trespass."
    show marin_alvarez at right:
        zoom 0.7

    marin_alvarez "I don't think they'd notice me among the cranes."

    luka_sorensen "They notice the quiet ones more. Quiet has weight. It pulls at other things.' He studies the barrier with a slow, deliberate glance. 'Is it what you thought?"
    "You hold the question like a stone in your palm. It is heavier than the model you once slid across tabletops, heavier than the diagrams pinned to the Tidewise wall."

    marin_alvarez "No. It wasn't this… absolute."

    luka_sorensen "They always ask for absolute when they're afraid. Absolute is easier to count than lives.' He pauses, then looks at you as if measuring your steadiness. 'You stepped aside. That was your hand on the rope."

    marin_alvarez "I stepped aside because I thought—' Your voice tightens. You hear the memory of the meeting: the way Kaito's eyes darkened with gratitude and fear; the quick way Elena's smile folded into a calculation. 'I thought I could do more from the edges. Less heat, more accuracy."

    luka_sorensen "Heat is what makes people move. Accuracy can sit on a shelf.' He lets the sentence hang with the wind. 'But you saw them choose. We all did. It makes a hole."
    "A crunch of gravel — a worker folding a tarp — cuts across Luka's sentence. You look back at the barrier. Men and women in neon vests move like a new shoreline has been planted. There"
    "is no ceremony for what they've just erased; no ritual, no songs. The marsh frames that once hosted the midsummer lanterns are being lifted and loaded into dumpsters like broken furniture."

    menu:
        "Step closer and call Kaito across the worksite":
            "You move toward the temporary walkway. The workers glance up; a foreman signals a pause. A shape you know walks out from between two cranes — Kaito. He meets you halfway, face salt-raw and guarded."
        "Stand in the shadow of the lamppost and simply watch":
            "You stay put, shoulders hunched against the cold. Kaito's head tilts when he sees you; his face closes into an unreadable expression. He keeps walking with the others, and you find your voice later in pieces."

    # --- merge ---
    "You take the second option because your throat is full of the argument you don't have the right to make. Let him lead. Let him hold what you surrendered."
    "You watch Kaito from a few paces away as he negotiates logistics with the foreman, his hands moving like the carpentry gestures you know: precise, immediate, practical. He talks about making a temporary frame out of"
    "reclaimed beams to support the walkway they're rerouting; he speaks of keeping the little floating farms afloat during construction. There is a thousand small salvations in his voice, and each one is a compromise."
    show kaito_sakamura at center:
        zoom 0.7

    kaito_sakamura "We can set those coral frames off to the north. Not ideal, but they won't be crushed."

    "Foreman" "Client wants the face continuous. No breaks."

    kaito_sakamura "That doesn't mean we break the reef beds. We find a way."
    "Kaito Sakamura [jaw tight]: (He looks at you as if measuring your presence against the calculus of the moment.) 'You okay? You said you'd help.'"
    "You feel heat rise, shame and the old obligation braided together."

    marin_alvarez "I am helping. I'm—' The words catch. 'I'm here."

    kaito_sakamura "You sounded like you were stepping back the other day. The room felt... lighter when you did."

    marin_alvarez "Because I thought you could carry it."

    kaito_sakamura "Carry it? That's not how this works."
    "He doesn't shout, but every syllable is a small hammer. You know the drill of his patience; you know it can fracture."

    kaito_sakamura "I didn't tell them to build like this. I argued for the marsh pilot. They promised compromises. But the agency moves fast when money and a mandate meet. They took the council meeting, bypassed it—"
    "You look up. Elena Moro stands at the edge of the work — her trench coat a crisp line against the fog. She watches the pour, hands tucked, a tablet glowing in one palm. Her presence is a precise, cool geometry in the messy geometry of loss."
    hide luka_sorensen
    show elena_moro at left:
        zoom 0.7

    elena_moro "We did consult with representatives. The procurement required strict timelines. The structure will protect the core of Saltline from the worst storm surges."

    kaito_sakamura "You didn't consult the people who live with the tides. You cataloged the risks and called them acceptable losses."

    elena_moro "Every large-scale intervention has trade-offs."

    kaito_sakamura "Some of us don't get to be a trade-off. Our songs, our festivals—they're tied to those marsh frames. You can quantify marsh acreage; you cannot measure a ritual."

    elena_moro "Rituals are adaptable. They'll find new places."

    kaito_sakamura "When? After everything that made them feel like home is gone? That's not adaptation. That's replacement."
    "The air snaps electric between them. The hydraulic pounding roars, like a percussion section underscoring the argument. Your presence is incidental yet like a rubbed bruise; you feel every word as if it's been flung at you."

    marin_alvarez "You promised oversight. You said there would be room for community-led measures."

    elena_moro "You stepped away from public leadership, Marin. I did what the mandate required. I didn't ask for permission to make hard choices."

    marin_alvarez "Hard choices shouldn't mean erasing people's lives."

    elena_moro "We did the math. We had to choose something that would scale and sustain greater population centers. If Saltline dries up economically, there will be no rituals left to practice."
    "Her words are a scalpel. They cut not toward you but through the idea you carry: that survival measured by infrastructure equals survival of place. The calculus is precise; the sorrow is not."
    hide marin_alvarez
    hide kaito_sakamura
    hide elena_moro

    scene bg ch7_4001e7_2 at full_bg
    "You close your eyes for a second and see the face of the marsh in memory. Lanterns bobbing on moonwater. The sticky sweetness of marshmallow fires after summers of gathering. Maya's voice, high with laughter as"
    "she balanced on a reclaimed beam. Those frames — gone, or repurposed into containment. The town's balance shifts under your feet."
    # [Scene: Kaito's Workshop | Early Evening]

    scene bg ch7_4001e7_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A single lamp clicks, the quiet scrape of a rasp. Outside, the heavy barrier hums faintly in the distance.]
    # play music "music_placeholder"  # [Music: A single cello note, drawn long and mournful, then a slow, insistent crescendo]
    "You follow Kaito to his workshop because the work always used to be the place you could speak plain. Inside, the light is different: human-scaled, forgiving. Kaito moves with the same calm urgency he showed outside,"
    "sanding the edge of a piece of driftwood as if he can scrape away the day's grief."
    show kaito_sakamura at left:
        zoom 0.7

    kaito_sakamura "You smell like the pouring site. Concrete will cling to hair for a day."
    show marin_alvarez at right:
        zoom 0.7

    marin_alvarez "I know."

    kaito_sakamura "They finished the first continuous section. The foreman said the structural tests were green. That should keep the lower promenade safe for another decade."

    marin_alvarez "Should."

    kaito_sakamura "You gave that up. You let them take the public fight and you sat behind the scenes."

    marin_alvarez "I thought—' You stop. The sentence stalls in the grain of the workbench. 'I thought my technical oversight would be enough to keep it honest."

    kaito_sakamura "Oversight isn't the same as voice.' He sets the rasp down and rubs a thumb along the wood, leaving a clean streak. 'You know how to speak at the meetings. You can make people listen."

    marin_alvarez "You were the one who needed me to be careful. You asked me to step back."

    kaito_sakamura "I asked for your trust. That's not the same as asking you to disappear."
    "The rasp of his hands returns to the wood like an impatient heartbeat. He is trying to make something whole where something has been fractured."

    kaito_sakamura "I argued for staging. I argued for pilot marsh plots. They promised mitigation. But once the grant was signed, the agency used procurement authority to consolidate the plan."

    marin_alvarez "I should have spoken up more. I should have—"

    kaito_sakamura "We each made choices. I led people who trusted me to keep more than plans intact. You retreated and expected to fix what you'd missed from the margins. Neither of those plans saved the marsh."
    "The words are soft but ring like a verdict."
    "For a moment neither of you speaks. You can hear your own breath and the wood-scent of the shop. Outside, someone laughs at victory — practical, clipped. The town is safer by structural metrics; the people"
    "who measured that safety will send invoices, reports, and press releases. Inside this room, the measure of loss is invisible in any spreadsheet."

    kaito_sakamura "There will be community dinners still. A lot of people will adapt. But the big gatherings—Luka warned me—he said people scatter when the old stages are gone."

    marin_alvarez "We can make new ones."

    kaito_sakamura "We can. We will. Later. After the feeling of being buried settles. Later is not a small thing."
    "He sets down the small carved compass pendant he has been whittling for weeks — the same wooden compass that used to swing between the workshop's workbenches. It's rough, warm, a thing made from the same island as everything he loves. He offers it to you without reading your expression."

    kaito_sakamura "I made this for you. When things got… crowded, I wanted you to have something that points to shore."
    "You take the pendant. It is lighter than you expect; the grain fits your palm."

    menu:
        "Take the compass and press it to your lips":
            "You bring the wooden compass to your mouth and kiss the carved face because small rituals keep you from collapsing. Kaito's shoulders loosen for a beat, then tighten again. He looks away, engraving the line between gratitude and grief on his jaw."
        "Place the compass back on the bench and let silence sit between you":
            "You set it down carefully where it rests on the bench. The silence between you grows thicker, full of things unspoken. Kaito's hands go back to his tools — work as a defense and a language."

    # --- merge ---
    "You pick up the compass and feel its ridges bite into your palm. It's a small, private bargain: you will carry a piece of the workshop even if you no longer lead the public charge. You will be a keeper of smaller fires."

    kaito_sakamura "I don't know if this can be repaired by two people alone. Maybe it can't be repaired at all. Maybe the town stitches itself together in a way we don't recognize."

    marin_alvarez "Maybe that's what it means to be resilient."

    kaito_sakamura "That's the thing people like to say to feel better about what they lost."
    "You both know it's true and empty in the same breath."

    kaito_sakamura "I love you, Marin. I always have. But love doesn't mean we take the same paths."

    marin_alvarez "I know."

    kaito_sakamura "I need to do this in the way I can. I can't drag you through every confrontation when you chose the quiet role."

    marin_alvarez "And I can't—"

    kaito_sakamura "—be the loud voice you once were. I know."
    "There is no flourish, no cinematic reconciliation. There is only a quiet agreement — a mutual renunciation and a pact to keep what each of you can keep. A softer kind of parting; not a rupture of hate but a contraction into separate orbits."
    "You stand there with the compass at your palm and feel the town rearrange itself. The barrier hums in the distance, a metallic lullaby promising fewer nights of flood and more nights of engineers' reports. The cost is calibrated and exacting."
    hide kaito_sakamura
    hide marin_alvarez

    scene bg ch7_4001e7_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant murmur of conversation, now smaller. The barrier's maintenance pumps cycle with a mechanical sigh.]
    # play music "music_placeholder"  # [Music: Cello withdraws into a single, unresolved note]
    "Later, you return alone to the promenade. The marsh where the lanterns once drifted is a different shape now — truncated, rebar-skeletal, quiet. A single lantern, floating in a plastic basin someone left behind, bobs as if not sure whether to keep burning."
    "Luka finds you there and sits a respectful distance away on a submerged bench."
    show luka_sorensen at left:
        zoom 0.7

    luka_sorensen "It'll hold. The line will hold. The models promise decades."
    show marin_alvarez at right:
        zoom 0.7

    marin_alvarez "It will protect the promenade."

    luka_sorensen "And the thing you loved?"
    "You look at him. He meets your eyes with the tiredness of someone who has lost more times than he can count and still believes in telling truth."

    luka_sorensen "Some rituals will fade. Some will find new ground. People will keep eating and singing. The town will not die. That does not mean it will be the same."

    marin_alvarez "Is it better to have saved buildings or saved songs?"

    luka_sorensen "Sometimes saving buildings buys time for songs to mutate into something else. Sometimes it buries the singers."
    "His words land like stones."
    "You think of the shell at your throat, of the wooden compass warm in your pocket, and of the long lists of things you promised yourself you would fix. You think of Kaito, stooped over his bench, turning salvage into meaning."
    "You do not pick up the lantern. You do not sing. You stand in the rain that has stopped and let it run down your face like a small absolution."
    "You have stepped back into the edges because you told someone you would. That choice steadied some things and broke others. The town stabilizes in the narrow sense that mattered to grant officers and insurers —"
    "roofs on houses, a lowered risk curve. But the communal stages have gone dark; the summer nights where everyone once crowded the marsh for songs and soup have become private, careful gatherings. Where you had imagined"
    "that your quiet stewardship would be a balm, it reads now like a withdrawal."

    "Kaito Sakamura texts you later that night" "Safe. Workshop warm. Talk tomorrow?"
    "You pause. You don't answer at once. Your fingers hover over the screen, then type, then delete, then finally press a sentence thin as a reed."

    "Marin Alvarez (text)" "Not tonight. Soon."
    "You put the phone away and slide the wooden compass back beneath the collar of your jacket, near the shell. You walk the waterline until the town's lights blur with the horizon, and you breathe in the new, colder world that your choices helped shape."
    "There is no fireworks of betrayal, no dramatic public rupture. There is a hush of practical safety and private absences. The barrier will work. People will sleep without nightmares of the sea tearing the town apart. The marsh will suffer, and the songs will be fewer."
    "You do not know if regret can be measured in tide marks."
    hide luka_sorensen
    hide marin_alvarez

    scene bg ch7_4001e7_5 at full_bg
    # play music "music_placeholder"  # [Music: A low chord resolves into an unresolved interval — sorrow without collapse]

    scene bg ch7_4001e7_6 at full_bg
    "THE END"
    # [GAME END]
    return
