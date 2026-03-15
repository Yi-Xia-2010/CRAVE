label chapter9:

    # [Scene: Council Hall | Evening]

    scene bg ch9_3be532_1 at full_bg
    # play music "music_placeholder"  # [Music: Agitated strings, rising tremolo]
    # play sound "sfx_placeholder"  # [Sound: Murmurs, a distant thunderclap]
    "You can still feel the echo of the bell in your chest—the choice you made earlier like a bruise. The hall is hotter than the night outside, full of breath and accusation. Voices rise and crash against concrete. Cameras angle in, lenses collecting the town's fracture."
    "Iris Varela stands at the front with that steady, seafaring posture, but there's a tremor in the set of her jaw. Investors in dark coats whisper in a tight knot to one side, their faces small"
    "and pale as if carved from the fluorescent light. Elias Park is in the crowd, palms clenched around a stack of schematics like a lifeline. Mateo moves between people, a presence that should anchor everything but"
    "now can't stop the tide of words."
    "You step onto the raised floor because you had to. Because standing down was an answer you couldn't live with."
    "You clear your throat. The room teens to a brittle silence that feels like a held breath about to break."
    show mara_serrano at left:
        zoom 0.7

    mara_serrano "This retrofit isn't a stunt. It's a repair. It's an emergency measure to keep families from losing everything."
    show iris_varela at right:
        zoom 0.7

    iris_varela "So you would risk the funding—risk a shield that buys us time—because you want a pilot program? That's a luxury we can't afford."
    "Murmurs swell. An investor raises a hand, a small, clinical gesture."

    "Investor Rep" "We backed a solution, Ms. Varela. If the council becomes a venue for public interference instead of decisive action, we must reconsider our exposure."
    "Elias Park steps forward before you can; his voice is steady but thin with urgency."
    show elias_park at center:
        zoom 0.7

    elias_park "We can integrate biological measures without delaying construction—modular retrofits, adaptive anchors. We can do both if we get coordinated buy-in."

    iris_varela "Coordination is a euphemism for delay. Coordination is what leaves people sleeping with the sea on their doorsteps."

    elias_park "And haste is what leaves design flaws undetected."

    mara_serrano "A shield that channels water into low-lying streets is not protection—it's rerouting harm."
    "Iris Varela's eyes harden. The investor's hand goes down like a verdict."

    "Investor Rep" "If the council can't settle on a single plan, I'm afraid we'll have to withdraw our capital. Public certainty is part of our risk modeling."
    "The room's air changes. You can hear it—the intake of breath that feels too big for the body."
    hide mara_serrano
    show abuela_rosa at left:
        zoom 0.7

    abuela_rosa "Ay—may God keep us."
    hide iris_varela
    hide elias_park
    hide abuela_rosa

    scene bg ch9_3be532_2 at full_bg
    # play music "music_placeholder"  # [Music: Single, stark cello note]
    "A cascade of accusations follows—televised soundbites, neighbors shouting across a gulf of fear. Iris Varela fights back with policy sheets and a voice honed by storms and ballots. You fight back with images from your notebook"
    "and the memory of a boat you couldn't save. Elias Park fights with data and the vulnerable hope of a trained hand. Mateo fights with practical plans and the impatient tenderness of someone who still believes"
    "fixes are possible."
    "The investor makes a final motion, a thin smile that doesn't reach his eyes."

    "Investor Rep" "We will review tomorrow. If the council does not present a unified front by morning, we withdraw."
    "The words land like stones. Somewhere in the room a woman begins to sob. A camera keeps rolling."

    menu:
        "Speak up and demand the investor stay":
            "You rise, voice raw. 'You can't turn away now. We asked you to help us survive, not to bet on our silence.' The investor's face remains polite, unreadable, and the crowd roars around your words."
        "Stay silent and focus on the crowd":
            "You sit back down. You let Elias try to salvage whatever cohesion is left. The investor takes the silence as a sign; you feel your chest tighten like it's being rubbed raw."

    # --- merge ---
    "..."
    # [Scene: Council Hall Lobby | Night]

    scene bg ch9_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: News vans starting up, the distant rumble of approaching wind]
    "Outside, people split into heated groups. Some chant for Iris Varela's certainty; some call for Elias Park's pilot. You move through them and feel the town begin to fracture into shards that will not easily be put back together."
    "Elias Park catches up with you at the steps, rain starting to spit at your shoulders, his breath fogging in the air."
    show elias_park at left:
        zoom 0.7

    elias_park "They'll go through with a review. The investor's bluff is dangerous, but it buys us time—maybe enough to reinforce the pilot."
    show mara_serrano at right:
        zoom 0.7

    mara_serrano "Time. Who told us time would be on our side?"

    elias_park "We can use what we have—work at night, prioritize the weakest seams. If we show progress, we might pull them back."
    "You study his face. For the first time the optimism in him looks like stubbornness, a bandage over fear."

    mara_serrano "Or we make enemies who'll watch the next storm like a payday."

    elias_park "I can live with enemies. I can't live with people trapped by our indecision."
    "His eyes look for yours—not to ask, but to rely. You realize being the hinge is not a title you wanted; it's a weight. You look toward the water-lashed horizon. Clouds are building—strange and heavy and wrong."

    menu:
        "Head straight to the shoreline to check the levee":
            "You step into the rain and toward the harbor. The wind lifts your scarf and the world smells like iron and cold. You feel impulse sharpen into motion."
        "Go to the lab to gather tools and volunteers":
            "You push through the crowd toward Saltmarsh Labs—lights and instruments and practical order. You hope procedure can outrun panic."

    # --- merge ---
    "..."
    # [Scene: Cliffside Promenade | Early Storm]
    hide elias_park
    hide mara_serrano

    scene bg ch9_3be532_4 at full_bg
    # play music "music_placeholder"  # [Music: Percussive drums; sirens weaving into the rhythm]
    # play sound "sfx_placeholder"  # [Sound: A roar—sea meeting structure, timber squealing, a long, animal sound]
    "You stand on the promenade with Elias Park and a cluster of volunteers. Rain slashes your face. The prototype barrier—recently finished, bright with wet concrete and the sheen of rushed sealant—takes the ocean's first real test. Floodlight beams slice the storm; the barrier groans in a language of stress."
    show elias_park at left:
        zoom 0.7

    elias_park "We're seeing greater backflow on the southern seam! Someone—check the flood valves!"

    "You sprint down the rocks with Mateo at your heels. He jokes—once, breathless" "If this is the apocalypse, it's at least a scenic one."

    "Emergency Responder" "Multiple breaches. Low-lying sectors—Marina Row, the old fishery—are taking redirected currents. We need boats on the south inlet. Volunteers, go to the levee—now!"
    "The prototype isn't failing uniformly. It isn't collapsing; it is misbehaving. Where the barrier meets a bend in the shoreline, the current funnels like a fist into narrow channels no one anticipated. Water finds weak places—old"
    "drains, informal walkways, places where the town lived cheap and close to the sea. The barrier's seam directs a new tide into those small, human spaces."
    show mara_serrano at right:
        zoom 0.7

    mara_serrano "Tell Mateo to head to Marina Row with a line. Check the old sluices—if we can open them early, it might divert the worst."
    show mateo_reyes at center:
        zoom 0.7

    mateo_reyes "Got it. I'll—"
    "He leaves, trawling through the rain. You watch his back—lean, familiar—and something in your chest tightens dangerously."
    "The cliffside foghorn blares. Sirens multiply, high and thin. A shout slices through the storm—someone calls Mateo's name. You look and see him at the lip of the old inlet, fighting the surge to get a rope to a trapped boat where a family is clinging to a listless hull."
    "You race with others. The water is a wall, black and furious. Mateo throws the line with the casual precision of someone who grew up knowing how ropes speak."

    mateo_reyes "I've got them—hold on!"
    "The rope takes. For a breath, the world leans as if restored. Then the current shears. Something unseen—an eddy born from the barrier's misdirection—pulls the line. Mateo slips on the algae-slick rocks; his boot catches nothing."
    "He claws for purchase, but the water has new anger. You see his hand flash as it reaches for a child. You see his face, and in that face is the inexorable refusal to let go."
    "You lunge, fingers closing on his sleeve. The world tilts. The rope jerks. Mateo's head snaps back with the motion. You are dragged to the edge, mud sucking at your boots. A voice above you screams;"
    "a responder fires a flare. But the surge is a force with laws you cannot bargain with."

    mateo_reyes "Go—get them—"
    "The last thing you hear is his laugh—short, the sound of a life that expected to be able to outrun the sea. Then the water takes him, and the laugh becomes something small swallowed by the storm."

    mara_serrano "Mateo!"
    "Elias Park grabs your arm. Someone pulls at your coat. The child is dragged to safety by a responder, his hair slick with seawater; the family weeps, grateful and hollow. Mateo is gone beneath a sheet of brown water that eats sound."
    hide elias_park
    hide mara_serrano
    hide mateo_reyes

    scene bg ch9_3be532_5 at full_bg
    # play music "music_placeholder"  # [Music: Orchestral crash—no melody, only impact]
    # play sound "sfx_placeholder"  # [Sound: A hard, metallic shriek as a seam tears in the prototype barrier]
    "You stagger back up the rocks, rain cutting across your face like a thousand tiny knives. The town's cry is a chorus of anger, grief, and disbelief. The investor's retreat—earlier threats translated into present horror—feels almost obscene."
    show iris_varela at left:
        zoom 0.7

    iris_varela "You chose this spectacle! You made it political—now we have blood on our plans!"
    show elias_park at right:
        zoom 0.7

    elias_park "We demanded oversight because the design is dangerous! We asked for monitoring—"

    iris_varela "You undermined the very thing that could have held!"
    show mara_serrano at center:
        zoom 0.7

    mara_serrano "Your 'thing' redirected the water into people. You built a wall that chose who survives."
    "The accusation hangs, and it's true in a way that tastes like rust."
    # [Scene: Shoreline — Midnight]
    hide iris_varela
    hide elias_park
    hide mara_serrano

    scene bg ch9_3be532_6 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano, slow and hollow]
    # play sound "sfx_placeholder"  # [Sound: Distant barking, a cadence of radios, soft weeping]
    "The rescue effort splinters. Teams are stretched thin; the lab's sensors are overwhelmed or offline; volunteers haunt the edges like wraiths. Parts of the shoreline are lost—streets that used to be crowded with nets and laughter"
    "are now tidal gullies. Boats droop on new currents. A single lamppost flickers in the water, its light like a slow heartbeat."
    "Abuela Rosa stands on a sodden doorstep, apron clutched to her chest. Her eyes are wet and old and steady in a way that makes you feel smaller than you knew you could be."
    show abuela_rosa at left:
        zoom 0.7

    abuela_rosa "We prayed to the sea and she answered with what she had. We must bury the rest with honor."
    "People look at you with a complex mixture—their faces are untranslatable: grief, reproach, gratitude braided together. Some scream your name like a plea, some hurl it like a shard."

    "Local Woman" "You brought them the idea of pilot programs when there was a contract on the table. You split us."

    "Old Man" "We trusted hands that promised science."

    "Teenager" "Why didn't you stop it?"
    "You find Elias Park two steps away, soaked through, hands like someone who has tried to hold the sky. He looks at you with a confusion so raw it borders on accusation."
    show elias_park at right:
        zoom 0.7

    elias_park "We tried to be careful. I thought—God, I thought we could do both."
    show mara_serrano at center:
        zoom 0.7

    mara_serrano "You thought. I thought. He died because of what we didn't see."
    "Elias Park doesn't look away. His fingers find yours in the dark; a reflex, a reaching for something human. The touch is trembling, asking for absolution that neither of you can grant."

    elias_park "I didn't—"
    "You yank your hand back as if burned. The motion is instinctive and cruel in one movement. Around you, the town fractures further—friends who once repaired boats together now stand behind placards that accuse or defend."
    "The investor rep's absence is a kind of ghost—capital fled, legal reviews promised, blame assigned like bandages."
    # play music "music_placeholder"  # [Music: A low, howling wind; then a single, aching violin line]
    hide abuela_rosa
    hide elias_park
    hide mara_serrano

    scene bg ch9_3be532_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant, rhythmic banging of hammers trying to shore a failing levee]
    "You dig. You and Elias Park and a smattering of desperate neighbors and responders throw sandbags with fingers that shake. Rain is a curtain that makes each movement sacrificial. Your nails split on wet burlap; your"
    "palms are scraped raw. The levee shudders as each wave hammers it, a percussion of water on cloth."
    show mara_serrano at left:
        zoom 0.7

    mara_serrano "We need more sandbags at the north corner! Hold the seam—push the logs into it!"

    "Responder" "We're out of rope! The sluice—it's jammed!"
    show elias_park at right:
        zoom 0.7

    elias_park "Then break it! Pry it! Anything!"
    "Your chest feels like a drum beaten too long. Each surge of water is an accusation. You imagine faces—Mateo's grin, the child's small hand, your own hands that reached and could not hold. The levee bows, then recovers, then bows again. The work is relentless and holy and utterly inadequate."

    "Responder" "Another house—Marina Row—has collapsed into the current!"
    "You turn and see roofs slipping like tilted teeth into the sea. People cling to porches, some screaming for help. The town's spine is bending. The social glue that bound you is thinning into a dangerous slick."
    "Elias Park moves beside you—close, too close. He tries to find your eyes, tries to make contact, to share the weight. You can feel the trauma between you like a physical object that neither of you knows how to lift."

    elias_park "We need to tell the council what happened—hold them accountable. The investors—"

    mara_serrano "There will be no assurances that fix this. Nothing will fix the people we've already lost."
    "He swallows. The decision to be public, to call out the flaws, to force transparency—your name is spoken in the same breath as salvation and failure. The town is a ledger with unequal entries, and blood writes the margins dark."
    hide mara_serrano
    hide elias_park

    scene bg ch9_3be532_8 at full_bg
    # play music "music_placeholder"  # [Music: Fades to a long, mournful chord]
    # play sound "sfx_placeholder"  # [Sound: Rain slows, exhausted; a distant, solitary bell tolls]
    "In the hours after, the town holds a somber accounting. Emergency shelters are crowded; legal teams start their paperwork; the council chamber is a theater of grief and recrimination. The investor's legal team sends a letter"
    "that reads like a verdict. Public opinion fractures. Some accuse you with righteous intensity; others place their palms on your shoulder in recognition of a courage that cost everything."
    "Elias Park stands at the edge of a shelter door and watches you from across the room. He looks smaller than the nights you've known him in, a boy with an engineer's hands empty besides grief."
    "You walk to Mateo's family. Abuela Rosa walks beside you. There are no words that collect a life back together. You offer a hand. They hold it and press it to their faces. The world narrows to that simple, shared touch."
    show abuela_rosa at left:
        zoom 0.7

    abuela_rosa "We will bury him by the cove, where the tide can remember him gently."
    "The town will not be the same. Some roofs will never be replaced. Some faces will never again look at you without calculating blame. Some will look at you and thank you through a wavering, broken"
    "smile. Elias Park and you—blame, forgiveness, love—become a thicket no longer navigable by the good intentions you once shared. Trauma reshapes the contours of your connection. It may, in time, remold it into something quieter and"
    "more wary, or it may sever it into two separate trajectories."
    "You cannot tell which will be true."
    hide abuela_rosa

    scene bg ch9_3be532_9 at full_bg
    # play music "music_placeholder"  # [Music: A single piano note, then silence]
    # play sound "sfx_placeholder"  # [Sound: Distant waves, slow and indifferent]
    "You stand at the cliff's edge when dawn finally comes—if dawn is what this pale sky is. Below, the shoreline is altered like a map rewritten with a blunt pen. The community that once repaired together"
    "now sorts wounds and debts and responsibilities. Some stand at the water's edge and swear to rebuild differently; others already seek a scapegoat to keep their nights livable."
    "You press the compass at your throat—not for direction but because you need something solid to touch. It is cold, a small, private truth."
    "You whisper Mateo's name into the wind. It takes the sound and scatters it. There is no response but the ocean, vast and indifferent. There is, though, the memory of him—steady, stubborn, brave—like a light that keeps being useful even in the dark."

    scene bg ch9_3be532_10 at full_bg
    # play music "music_placeholder"  # [Music: Low, elegiac strings]
    # play sound "sfx_placeholder"  # [Sound: A single church bell, soft and final]
    "You cannot fix what has been lost. You can only carry it, and decide—if there is any sense in the future—to let that carrying shape your work, your apologies, and the way you love."
    "You breathe, the air tasting of salt and metal and rain. The town gathers the broken into lists. Names are recorded. Hands are held."
    "You look at Elias Park one last time across the levee. He meets your gaze, and for a moment there is a look like a question and a plea and an apology all at once. You"
    "nod, not because the nod fixes anything, but because acknowledgment is itself a small, necessary act."
    "The coastline is changed. The social fabric is tattered. The cost has been enormous, and the night will remember it long after bodies are buried and lawsuits signed."

    scene bg ch9_3be532_11 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    scene bg ch9_3be532_12 at full_bg
    "THE END"
    # [GAME END]
    return
