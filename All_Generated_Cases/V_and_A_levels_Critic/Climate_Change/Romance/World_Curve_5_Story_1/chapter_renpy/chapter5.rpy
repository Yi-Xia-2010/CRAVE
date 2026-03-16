label chapter5:

    # [Scene: Twilight Festival Plaza | Night]

    scene bg ch5_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, pulsing synth undercut with urgent percussion]
    # play sound "sfx_placeholder"  # [Sound: Distant thunder, the soft clink of utensils, a child's laugh cut short by an approaching roar]
    "You move through the plaza like you always do when something fragile needs watching — careful hands, practiced steps. Your scarf is doubled over as a mask; the damp wraps around your neck and the vial"
    "of seeds at your throat swings against your sternum, a steady, ridiculous ticker of small things that still belong to you."
    "The demo is supposed to be perfect. Mayor Serena sits near the presentation tent, civic sash damp at the edges, her face a carved, polite unreadability. Funders cluster by the lab's portable monitors; a ribbon of"
    "press cameras waits at the edge of the crowd. The lab team runs a last-minute check on telemetry while Elias kneels beside the sensors with his sleeves rolled, data streaming across his wristpad in tiny, ordered"
    "waves."
    "Mateo is kneeling before a circle of kids, cupping his hands around a battered thermos."
    "Mateo Alvarez: [smiling] 'When the old pier sang in the tide, we learned which ropes held. It taught us to plant where the sea would forgive us. If we teach the young ones—'"

    "Child" "Will the mangroves eat the bad water, abuelo?"
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "They'll hold it like their roots hold stories."
    "You watch him—the old harbor in his hands—and the warm pressure behind your ribs loosens for a breath. This is what you saved for. This is why you stitched together volunteers, reclaimed wood, and a handful"
    "of skeptical grants. The crowd smells of wet bread, diesel from food carts, and the sharp tang of sea salt in the air."
    "Kira stands near the fringe, binoculars swinging, a megaphone slung over one shoulder. She's a bright splash against the gray, twitchy and ready to pounce on any narrative slip. Jonah's team looms across the way, floodlights"
    "like an accusation slicing the dusk. He watches with an executive calm—jaw tight, eyes promising future contracts."
    "Elias Rook looks up at you, and for a moment the panic that has threaded earlier days recedes. His fingers are stained with mud; his face is set to measurement, to detail. You return a breathless"
    "smile because there is work to do and because his steadiness has braided with yours before."
    show elias_rook at right:
        zoom 0.7

    elias_rook "Sensors are live. If the pilot holds through the tide window, the model's validation should speak for itself."
    show ayla_moreno at center:
        zoom 0.7

    ayla_moreno "Then let's be very loud about the model."
    "He smiles — a small, almost clinical thing — and you can feel a whole argument about heart and metric dissolve into mutual, fierce insistence that both can be true."

    menu:
        "Double-check the anchor bolts yourself":
            "You crouch at the base of the living barrier, feeling cold mud through your gloves. The bolts are tight but not perfect; a hairline of play you notice and smooth with a hand, inwardly promising to track it in the report."
        "Trust the sensors and keep prepping the stalls":
            "You step back and wave through a grin, letting Elias and the lab team own the technical checks. It frees your hands for seed packets and speeches—but a small, private knot of worry tugs at your throat."

    # --- merge ---
    "..."
    "The tide readings on the lab monitors blink green then pale yellow; someone jokes about numbers being dramatic tonight. You laugh with them, because laughter holds back darker thoughts and because public hope is an act"
    "of governance. The sky grows a darker drum of iron; people pull jackets close. The air tastes of copper and rain."
    "Minutes stretch. The monitors begin to show a slow, unremarkable rise. Then, without the editorial patience you expect from physics, the curve spikes."
    # play sound "sfx_placeholder"  # [Sound: An abrupt alarm—high, uncompromising; a different synth layer drops into the music]
    hide mateo_alvarez
    hide elias_rook
    hide ayla_moreno

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The crowd's murmur fractures into sharp syllables; someone shouts, "Surge—!"]
    "Elias Rook's face goes still in that moment before professionals shed their polish and the human response floods in. He clamps the dented thermos in one fist like a talisman, eyes darting from screen to waterline to you."
    show elias_rook at left:
        zoom 0.7

    elias_rook "We didn't model an astronomical compounding with this—"
    "You feel the sentence build in your throat: we did everything we could, we built a buffer, we gathered kids around stories of mangroves and seeds. But the words are carried away by the wind and replaced by the actual sound of the sea, which is no longer polite."
    "The living barrier heaves. Where the engineered core had been left with a hopeful cheek—good enough for a demo but not a fortress—the sand shifts like a body taking breath. A plank creaks, then snaps. The reed mats sag and water finds its narrow, wicked way."
    "Water moves with the patience of inevitability and the cruelty of surprise. It cracks over the first mound and then the second. It tastes of iron when it sprays your lips; metallic and stupidly cold. It"
    "takes a stall with a table of seedlings, spattering soil everywhere, uprooting a flat of young herbs that had been labeled for donation."
    "Kira Tseng's shriek cuts through the noise—high, raw, a sound shaped by bone and action."
    show kira_tseng at right:
        zoom 0.7

    kira_tseng "Get the kids out! Pull back the stalls! Move!"
    "You move because you do not need instruction. You grab at hands, drag a child's small arm through the water, and feel a garden you love sliding from under your feet. Soil clings to your palms"
    "in wet strings, a tactile betrayal. Someone yells Jonah's name; his floodlights wash the plaza in an accusatory glare that makes everyone look like actors caught mid-fall."
    show jonah_hale at center:
        zoom 0.7

    jonah_hale "This—this demonstrates instability! Hybrid solutions are not reliable under true stress. We need decisive engineering—now."

    "His voice is smooth, practiced. The cameras lean toward his cadence like wolves toward meat. The lab team swears under breath. Someone near the monitors is bellowing into a line" "Copy—securing footage—do not delete—"
    hide elias_rook
    hide kira_tseng
    hide jonah_hale

    scene bg ch5_4001e7_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hum of floodlights, the slap of water, and the insistent beeping of alerts combine into a mechanical roar]
    "Elias Rook goes still for a heart-rending beat, then his posture collapses into something raw. The clinical mask drops. He looks like a man carrying an equation that suddenly has too much weight."
    show elias_rook at left:
        zoom 0.7

    elias_rook "We should have—(soft choke) we didn't reinforce the core. The retrofits—"
    "You can see the blame gather like a storm cloud behind his eyes. It is not all aimed at the sea. It is not all aimed at the lab. It flicks, once, unmistakably, toward you."

    elias_rook "Ayla—did we miss the margin? Did you see the tide gauge? Did you tell—"
    "There is accusation there, jagged and hot. It lands in the hollow of your chest like a physical thing. For a breath you are all the lost fences and the memory of the plot that was"
    "pulled from beneath your feet years ago, the house you left as water rose past the threshold. Salt returns with humiliating velocity."
    show ayla_moreno at right:
        zoom 0.7

    ayla_moreno "I checked. I—"
    "You do not finish. The water is louder than words. You taste it again: iron and old pennies, and a memory you thought you'd planted in composted acceptance."
    "Mateo stands amid the chaos, moving with the grounded, weathered choreography of his life. He reaches out without theatrics to haul a canvas set of seedlings toward higher ground, pulling a child and a plastic crate"
    "at once. His hands are sure; his face is a map of the harbor's many wounds."
    show mateo_alvarez at center:
        zoom 0.7

    mateo_alvarez "We put roots where we could. Roots take a long time. You cannot shame the sea into changing its habits."
    "But Jonah's team has already begun to spin; his voice arcs across the placard of the plaza with the practiced cadence of a man who knows how to make urgency serve capital."
    hide elias_rook
    show jonah_hale at left:
        zoom 0.7

    jonah_hale "The council will see this. The footage proves it: hybrid prototypes fail at scale. We must approve the seawall immediately to protect vital infrastructure and the port jobs that keep this city alive."
    "People push, shout. Someone from the press jockeys for the viewfinder. The mayor stands, face closed, and for an instant you read the arithmetic behind her eyes—the city ledger, the political shelf-life of a single scandal."
    "Her hand hovers near a radio. The pressure is a physical thing, a hand around the city's throat."

    menu:
        "Shout back at Jonah from the edge of the flood":
            "You step into the spray and yell for people to stop weaponizing footage. Your voice cracks, but it rallies a handful of neighbors who pull seedlings from the water. The cameras snap toward you, hungry."
        "Pull Elias aside, away from cameras, to repair dignity and diagnostics":
            "You grab at Elias' arm and pull him under the lean of a tent. In the brief shelter you force open the pad and scream your combinations of data and palpability at him—numbers and apologies tangled—trying to make him step back from the ledge of blame."

    # --- merge ---
    "..."

    "The lab team scrambles, issuing statements into microphones" "This was an unmodeled compound event—astronomical tide plus surge—no single solution can guarantee zero risk—"
    "Elias stands bent over his thermos, then lifts his head and the person in front of you is not the man who folded plans into patient demonstrations but someone raw with loss."
    hide ayla_moreno
    show elias_rook at right:
        zoom 0.7

    elias_rook "We promised a pilot. We promised validation. People trusted us."
    "You are aware of every shard of that promise that you carry: the seed vial, Mateo's grin, Kira's fierce eyes, the children's hands in yours. You have not failed them by intent, but failure has a sound and a face and tonight it is hungry for scapegoats."
    hide mateo_alvarez
    show ayla_moreno at center:
        zoom 0.7

    ayla_moreno "The city is a ledger, and tonight the numbers are being written in water. Whoever controls the narrative will write the margins out of being."
    "A council aide hurries through the crowd, tablet jangling."

    "Aide" "Mayor Serena—there's footage—Jonah's calling an emergency committee—"
    hide jonah_hale
    show mayor_serena_okoye at left:
        zoom 0.7

    mayor_serena_okoye "Bring me the footage. And everyone—no arrests without council order. Secure the children. Get ambulances on standby."
    "Her voice is authority wrapped in thin cotton. It keeps order for a minute, like a plaster across a new wound. But Jonah's statement has already begun to compress the room; his engineers mutter that a"
    "seawall is the only marketable certainty. The cameras expect a villain and a savior and the world feeds on binaries."
    "You slump against a wet crate, palms trembling. Your gloves are soaked through; the soil cold and clinging. The world is bright with angles — floodlights, camera lenses, a thousand framing decisions stacking like plates."
    "Elias crosses to you slowly, the professional shell broken. His hand finds the small vial at your throat and does not grip it maliciously—he only holds it for a second as if to gauge whether the thing on your chest is still the same tiny defiant hope."

    elias_rook "I'm sorry."
    "It is the smallest line, and it should be a salve, but it is also the foreshadowing of more complex fractures. You both know apologies do not rearrange flooding. They do not replant uprooted basil or rewind the cameras."
    "Your chest is tight with a hundred small, salted memories. The plot you lost years ago returns—not in a neat flashback but as a tactile ache under your nails: a fence post you couldn't hold, a"
    "mattress floating like a small raft. The taste of failure is as literal as the sea salt on your tongue."
    "Kira Tseng slams a palm down on a portable speaker, eyes blazing."
    hide elias_rook
    show kira_tseng at right:
        zoom 0.7

    kira_tseng "They'll use this to bulldoze our plots and call it security. We won't let them. Not tonight."
    "Her voice is an unambiguous pitchfork. Around her, a cluster of volunteers, damp and angry, begin to organize a human chain to salvage the seedlings and protect the kids."
    "You feel the tempo of your heart accelerate—adrenaline and cold grief—pushing you toward a choice that will shape more than this night. The plaza is a battlefield of narratives: evidence versus emotion, models versus memory, corporate"
    "certainty versus community history. The tide and the footage are impartial, but the response will be anything but."
    # play music "music_placeholder"  # [Music: Percussion intensifies; strings scream a single, sustained dissonant note]
    hide ayla_moreno
    hide mayor_serena_okoye
    hide kira_tseng

    scene bg ch5_4001e7_4 at full_bg
    "The decision presses at you like the sea against a break. The lab will say rebuild better; Kira will say stop Jonah now; Jonah will offer trade-offs in the shadow of a crisis. Your chest tightens into a fist of salt and fear."
    "You inhale, and the inhale tastes of old houses and new losses. The night is loud, and every voice in it expects you to choose."

    menu:
        "Double down with Elias and revise the hybrid design, admitting flaws but pushing for better engineering and safeguards.":
            jump chapter6
        "Join Kira in a fierce public blockade to stop Jonah’s expedited vote; prioritize immediate protection for gardens through direct action.":
            jump chapter13
        "Negotiate a temporary ceasefire with Jonah, trading a concession (sacrificing one garden) for legally binding protections elsewhere.":
            jump chapter13
    return
