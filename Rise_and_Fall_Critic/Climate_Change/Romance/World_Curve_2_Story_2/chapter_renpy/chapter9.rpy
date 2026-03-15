label chapter9:

    # [Scene: Kaito's Field Lab | Night — hours after the storm]

    scene bg ch9_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The lab's extractor fan sighs; distant gulls cry like questions. A slow drip from a loose gutter keeps time.]
    # play music "music_placeholder"  # [Music: Low piano; a single dissonant string note beneath it]
    "You are awake with the lab’s clock in your palm. The dive watch on your wrist — the one you never took off since your brother — ticks and then stops, as if the sea took"
    "its rhythm with it. You stare at the blank face until the glass fogs; the numbers are meaningless beside the shape of the night."
    "Kaito Sato stands by the workbench, shoulders hunched against a humid draft. His camera strap hangs like a quiet accusation. He walks to the sensor array, lays a cautious hand on the cold casing, and withdraws it as if it burned."
    show kaito_sato at left:
        zoom 0.7

    kaito_sato "They went silent at three twenty-one,' he says. 'All of them. Not a flicker. Then—"
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "And the backups?"

    kaito_sato "Either they were never engaged properly, or —' He stops, lets guilt finish the sentence. 'Or they couldn't keep up with the surge."
    "Your chest has become a live wire. The lab smells of ozone and wet circuit boards, of salt and the faint sweet rot of algae. Every small noise — the tap, the click of a relay — is a possibility of more failure."

    kaito_sato "I kept logs. I can show you the reads. There are partials, spikes, then nothing. I… I thought we had margin."
    "You step closer to the board. The data printouts curl under your fingers, salt in the paper like a bruise. You feel furious and hollow at once — the two poles of grief."

    kaito_sato "Tell me what to do,' he says finally. 'Tell me how to—"

    maya_inoue "I don't have a how that keeps everyone safe,' you answer. Your voice is small in the lab's hum, but when you say it the sound seems to ripple into the fluorescent light. 'We thought— we hoped—"

    kaito_sato "Hope isn't a plan."

    maya_inoue "I know."
    "His eyes sting with it. You find yourself wanting to press your palm to his hand to anchor both of you to something that isn't shame. You don't. Instead you turn the binder over and read"
    "the names scrawled inside: sites, volunteers, the kids who planted the salt-tolerant beds. Each name is a breadcrumb that leads back to a living room, a kitchen table, a dinner plate."

    menu:
        "Reach for Kaito's hand":
            "Your fingers brush his. For a moment the lab is nothing but the warmth of his palm and the patter of rain on metal—an accidental truce. His shoulders slope; he closes his eyes as if to hold the pressure of it."
        "Bend to the printouts and check the logs alone":
            "You slide the damp paper toward you and force your eyes into numbers. The data is jagged and empty in places; your pulse matches the gaps. Kaito watches, silent and waiting, like a friend who has nothing to offer but presence."

    # --- merge ---
    "Kaito's jaw tightens whether you hold his hand or not. The world is a list of things you couldn't stop. Outside the shuttered windows, fog eats the promenade lights; distant speakers on the plaza spout LuxCorp's"
    "reassurances — tidy, polished phrases meant to calm a crowd that has lost more than it planned to."
    # [Scene: Flooded Coves | Dawn — the old cove near Tomas’s shack]
    hide kaito_sato
    hide maya_inoue

    scene bg ch9_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soggy boards creak; gulls crane their necks. Children’s muffled voices in the distance are swallowed by wet air.]
    # play music "music_placeholder"  # [Music: Sparse cello, low and patient]
    "Tomas stands knee-deep in the cold, watching what used to be the inlet. Where once nets hung to dry and coffee was poured from an enamel pot, there is only a gray, restless surface, and behind"
    "it the house cousin to Tomas's past. He moves slowly, his fingers tracing the air where the porch used to be."
    show tomas_bianchi at left:
        zoom 0.7

    tomas_bianchi "It's gone, innit?"
    "You can't pretend otherwise. The hand you reach for is useless in the shaking cold; instead you fold your arms around yourself, feeling the uselessness radiate out like heat."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "Marta's place?"

    tomas_bianchi "My mate. She left at dawn to walk the high road. Came back to this. Said it sounded like a whale had been swallowing the world."
    "You kneel on the seaworn stones. Your boots stick to mud. The smell is thick: diesel, mud, something sweet and putrid from uprooted soil. You cup a handful of the silt. Black silt slips between your"
    "fingers, leaving ribbons on your skin. It is heavy and cold and impossible to plan with."

    maya_inoue "We tried to give them time,"

    tomas_bianchi "Time's a privileged thing, girl,' he says. He holds your gaze like an accusation and a benediction. 'You tried. That counts. But some folks can't see that yet. They see only what they've lost."
    "Your mouth tastes of salt and remorse. For every shore you helped shore up, there is one you couldn't reach. For every sensor you placed, there is one that slept. For every meeting you called, there is a conversation that should have happened sooner, louder, harder."

    menu:
        "Climb down and try to salvage anything":
            "You wiggle down the slick stones and feel the water take the hem of your jacket. You pull at a half-submerged crate; it yields with a sigh. Inside are rusted tools and a child's half-broken toy, slick with foam. Tomas watches, each small recovered object a truism of loss and care."
        "Stay on the high ground and listen to Tomas":
            "You stay where you are and let him speak. He tells you about the coves like someone reading a ledger of memory; the names come slow but exact. You realize you are learning the map of what was lost more than you are learning how to rebuild it."

    # --- merge ---
    "Tomas (Quietly, after you return from whatever small action you take.) 'They'll say you broke a promise. Some already have.'"

    maya_inoue "What do you want me to say?"
    "Tomas: (He looks away, gulls wheeling over the ripping water.) 'Don't say the words that make people think you think you know better than them. Say the thing that lets them say what they need. That's how you'll start to get trust back.'"
    "You swallow. Trust feels like a fragile plank that you must hold in both hands without dropping; yet your palms are raw."
    # [Scene: Hana's Diner | Midday — a crowd pressed in, voices high and taut]
    hide tomas_bianchi
    hide maya_inoue

    scene bg ch9_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Voices overlap—anger, tears, a single chorus of "why" repeating like a refrain. The bell over the door rings too often.]
    # play music "music_placeholder"  # [Music: Dissonant piano, a rising tremor]
    "Hana is at the counter, elbows floured, face a map of ache and precision. She moves with the economy of someone who has fed a town through storms and argued with mayors over soup. Today her hands shake but she doesn't stop working."
    show hana_kim at left:
        zoom 0.7

    hana_kim "Maya! Folks are saying the sensors were your bright idea. Folks are saying you kept them secret, or you rushed them, or you shouted them from the rooftops. Everyone has a story different from the next. What are you going to tell them?"
    "You step behind the counter because it is the place where people confess and eat saucy truths. You meet faces, some wet with rain, some pulled thin with accusation."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "I will tell them the truth. Not the whole algorithm of it, not the lab charts, but the honest thing: we did all we could with what we knew then."

    "Neighbor #1" "Honest? Honest don't float my sister's shack."

    "Neighbor #2" "You didn't ask us how to fix the cove. You came with your maps."
    "Kaito Sato moves behind you and lays something on the counter — a printed image, ink bleeding from the salt, a photo of the sensor array half-buried in mud. He looks tired in a way you"
    "have rarely seen: exhausted, small, like a man whose hands have become two different tools than the ones he planned to use."
    show kaito_sato at center:
        zoom 0.7

    kaito_sato "We were trying to build a system that learns. We thought if we started small, we could scale, could make it safer for everyone."

    "Neighbor #3" "Learning? My mother drowned in a storm—what do you mean 'learning'?"

    hana_kim "Stop. Stop it. You're not getting anywhere by shouting at each other.' She turns to you with a blunt, human knuckle. 'Tell them what you'll do, Maya. Talk like a person who's fed them before they're hungry."

    maya_inoue "I will help fix what is fixable,' you say. 'I will help dig, to barricade what can be barricaded. I will help rebuild the beds that were washed away. And I will pay back what we can, with labor if not money. I will not hide from this."
    "The room hums, not yet softened. Some faces close; others remain pointed, like a village-level tribunal. A child at a corner table folds a paper boat and sets it in a puddle; it sinks without fuss."

    kaito_sato "And I will open every log, every line of code. You have our work; you can see it. If there is a flaw, I will find it. If there is something we missed, we will put the time into not missing it again."
    "Neighbor #1: (Huffs.) 'Words. We've had words.'"
    "Maya Inoue: (Your voice tight.) 'Then let me do the hard thing: show you by doing. I can't take back what happened. I can only be available to fix what I broke, or failed at. Either way — I am here.'"
    "Hana sets down a bowl of soup in front of you; the steam wraps your face like a small balm. You eat fast because hunger is a concrete problem and you can fix it. The town's"
    "conversation doesn't clear, but the edges feel less jagged for a moment. That doesn't fix the gardens that are gone, or the shack beneath the tide, or the neighbor's accusation that you chose a project over"
    "a life."

    menu:
        "Stand and call for volunteers to help salvage the gardens":
            "You stand on a chair and shout the plan: sandbags, compost, seed transplants. People blink, then nod; muscle and hands gather like a second tide. For a few hours the town is a movement of purpose."
        "Stay seated and listen to the accusations":
            "You keep your seat and let them speak. Fingers point, words arc. You take each as a lesson to keep; you memorize the shape of each anger. It is heavy and cold, but you understand more about what the town needs than any plan on a whiteboard."

    # --- merge ---
    "Kaito (Kneels beside your chair.) 'I'm sorry,' he says to you, quietly, not to the diner. 'For the misreads. For the times I thought data could sort people's grief.'"

    kaito_sato "I'm sorry,' he says to you, quietly, not to the diner. 'For the misreads. For the times I thought data could sort people's grief."

    maya_inoue "I'm sorry,' you say in return. 'For dragging this into people's lives and asking them to wait."

    kaito_sato "We thought we were helping."

    maya_inoue "We were. The outcome is different."
    "Silence lingers and then settles like a wet cloak."
    # [Scene: Promenade Streetlight Outside Your Window | Evening — rain returns as a thin, steady sheet]
    hide hana_kim
    hide maya_inoue
    hide kaito_sato

    scene bg ch9_3be532_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant clang of a shutter; a child's muffled cry; waves acting out a slow, patient ache.]
    # play music "music_placeholder"  # [Music: A sparse harmonic minor motif; breaths drawn long]
    "You stand by your window, the streetlight painting your palm with light and shadow. The sensors lie quiet under the mud—metal faces dulled by salt. Somewhere in the town, someone is picking through the remains of a garden and finding seeds that will not sprout this season."
    "Mayor Elena comes to your door in the rain. Her coat is sensible, water beading on the lapel. The municipality's weight rests in her posture: regret, paperwork, electoral math, and an exhausted moral ledger."
    show mayor_elena_rossi at left:
        zoom 0.7

    mayor_elena_rossi "Maya. We have to make choices now. I have people on my back and investors breathing down my neck. Some say take LuxCorp's offer and fortify at scale. Some say double down on local work. I—' She squeezes her umbrella as if holding two things at once. 'I need a recommendation."
    "Your throat is dry; you taste iron. This is the thing the forum was meant to decide before the water claimed its verdict. The set of options that once felt hypothetical has been sharpened into knives by loss."
    "Maya Inoue: (Slowly.) 'I will tell you what I know. I will tell you what we can do to protect what remains, and what will take time. I will not frame it as a simple tradeoff. I will show you the margins.'"
    "Mayor Elena: (She nods.) 'Margins are all I have, lately.'"
    "Kaito Sato stands behind you; his shoulders are broad enough to take the mayor's glare. He offers no defense that the mayor doesn't already need."

    mayor_elena_rossi "People are angry. They want someone to blame.' Her voice breaks. 'Don't let us become strangers."
    show maya_inoue at right:
        zoom 0.7

    maya_inoue "You won't. I can't fix everything overnight. But I'm not walking away."
    "She studies you as if trying to read the bones of you. There is pity there and a wary something else — the flicker of hope that the town's daughter will stand."

    mayor_elena_rossi "Then stand."

    maya_inoue "Yes."
    "You step out into the rain with Kaito beside you. The promenade smells of wet iron and sea. The streetlight reflects in puddles like a promise you are not yet ready to accept. Tomas's silhouette is"
    "a knot in the distance, Hana's diner a warm blot of light, the gardens a memory of green."
    show kaito_sato at center:
        zoom 0.7

    kaito_sato "What now?"
    "You take the first breath of a long plan. The town will need sandbags, permits, counsel, public meetings, and care. It will need people to forgive, which is harder than any engineering task. It will need"
    "you to be present in the small, mundane work that people can watch and measure with their own eyes."

    maya_inoue "We start where we can. We repair the nets and the beds and the sensors if they can be saved. We make reparations in work and material. We hold meetings at Hana's diner and bring the logs to anyone who asks. We make the maps public."

    kaito_sato "And if they still don't trust us?"
    "Maya Inoue: (You look at the water and the streetlight and the stopped watch on your wrist.) 'Then we earn it back in the slow way. Not with PR. Not with quick contracts. With hands.'"
    "Kaito Sato nods. He has sheets of code to rewrite and sensors to salvage and something like a new humility sewn through his movements. He reaches for your hand finally, and you let him take it."
    "You feel the guilt like something alive in your ribs, but alongside it, faint and fragile, is a resolution: you will stay, and you will do the work that rebuilding requires — messy, small, and endless."
    "The town does not feel whole; it feels like a body with a new scar. You do not imagine forgiveness, only the possibility of being useful again."
    hide mayor_elena_rossi
    hide maya_inoue
    hide kaito_sato

    scene bg ch9_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rain slows to a soft hush; a gull cries once, then goes silent.]
    # play music "music_placeholder"  # [Music: A final low cello, fading into wind]
    "You stand in the rain and name what you will carry forward: the memory of the lost gardens, Tomas's friend’s shack, the faces at Hana's counter, the rawness in the mayor's eyes. The sensors are a lesson written in mud. The town is a ledger of harm and care."
    "You breathe, and the breath fogs like a small promise against the window of the future."

    scene bg ch9_3be532_6 at full_bg
    "THE END"
    # [GAME END]
    return
