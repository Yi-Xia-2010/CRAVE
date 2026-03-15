label chapter2:

    # [Scene: Aster (skiff) | Dawn]

    scene bg ch2_c4ca42_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low tide whispering along pilings, a buoy’s occasional clank, a gull’s complaint]
    # play music "music_placeholder"  # [Music: Low, somber strings; distant percussion like measured footsteps]
    "You push the skiff free with slow, practiced hands. The line slips from your fingers and the small engine coughs awake—familiar and small against the scale of everything you're up against. Dawn leans wet across the"
    "marsh; the sky is the color of old pewter. Last night’s meeting still sits in your chest like a stone—expectations, voices, a room full of people who split toward different futures. You tell yourself only what"
    "you can measure will count today."
    "Your field kit is packed the way you like it: cores wrapped in waxed cloth, syringes for salinity samples, the wrist-band blinking a steady heartbeat of green. You run your thumb across the weathered binding of"
    "your notebook and feel the raised imprint of a sticker you haven't had time to peel: a small eelgrass silhouette, a stubborn promise."
    "Elias 'Eli' Calder is already aboard Aster, adjusting a brace on the skiff’s transom. He doesn't look at you right away; his gaze is fixed on tide-lines that mark the pilings. When he finally meets your"
    "eyes there's a small softness there—worry folded into trust—but you won't let it smooth the worry in you."
    show elias_eli_calder at left:
        zoom 0.7

    elias_eli_calder "Morning. Coffee's on the stern, if you want it (half-joke). Tide’s low enough for the cores if we keep to the channels."
    show mara_voss at right:
        zoom 0.7

    mara_voss "Thanks.' Your voice comes out too steady. 'Let's start at the northern creek—I've been watching the satellite runs. I want a transect: three cores, salinity every meter."
    "Elias 'Eli' Calder hesitates, then nods. He tucks a bandana behind his ear and hands you a small brass compass. The metal is warm from his palm."

    elias_eli_calder "Alright. You give me the call and I’ll keep the skiff steady. Tomas'll be on the east bank—if he shows, let him talk."

    mara_voss "If he shows,"

    menu:
        "Double-check the instruments one more time":
            "You run your fingers over the probes and microfilament, counting in a rhythm that steadies you. The readings flicker to life like a small, obedient lighthouse."
        "Take the coffee and watch the marsh wake":
            "The coffee is sharp and hot; you let it burn the edge off your nerves. The marsh exhales—reeds shiver and a kingfisher snaps the surface—and you feel for a moment that the day belongs to someone gentler than argument."

    # --- merge ---
    "Continue"
    # [Scene: Willowmarsh | Mid-Morning]
    hide elias_eli_calder
    hide mara_voss

    scene bg ch2_c4ca42_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Water sliding over mud, reed calls, the distant clink of a sample jar being capped]
    # [Smell: Brine, wet peat, a metallic note from the instruments]
    "You push Aster into the narrower arms of Willowmarsh, ducking under a low-spread branch that scratches at your sleeve. The skiff replies to your touch like an honest thing; it does only what you ask. Each"
    "core you pull is a small history: layered mud, thin flecks of shell, the pale braid of something that might have been eelgrass. You peel back each cylinder with gloved fingers and mark depth against color"
    "and smell."
    "The salinity readings don't lie: the numbers drift higher toward the mouth of the creek than they did in last season's notes. On paper, the difference is a decimal. In your chest, that decimal widens like"
    "a crack. Salt moves where it shouldn’t. Seedlings near the mid-marsh hang in slow suspension, half-formed leaves paling at the tips."
    "You take a breath, filling your lungs with brackish air and a sudden, cold certainty. Data is not drama, but it predicts drama—subtle failures that become sudden. You mark each jar, affix labels with a hand that has learned to steady when your heart works to beat faster."
    "From the far bank, a figure emerges: Old Tomas Calder, as if he were part of the marsh itself. His presence is weathered and familiar; he walks with a slow steadiness and carries a thermos the color of storm clouds."
    show old_tomas_calder at left:
        zoom 0.7

    old_tomas_calder "You always pick the fine days for measuring, Mara.' He says your name softly, like an old hymn. His voice is gravel and seafoam. (He pauses, watching you.) 'Could've been worse. Could've rained in sheets."
    show mara_voss at right:
        zoom 0.7

    mara_voss "It’s good to see you, Tomas.' You feel the word reach for something beyond polite greeting. 'How've the tides been for you?"
    "Tomas Calder squints across the water. The corners of his eyes fold inward, not in irritation but in summoning."

    old_tomas_calder "Used to be…we'd row out past the northern spit and the sea'd sit where you could touch it in the midday sun. Narrow river then. You didn't need to climb the pylons to see shore. Saw a seal once so close you could spit and hit it—God, I was a fool to try. Kids these days—' His laugh breaks like an uncovered jar. Then he grows quiet. 'It's wider now."

    mara_voss "Wider how?"

    old_tomas_calder "By inches, at first. Then by feet. Houses you could stand outside and plumb the sill with a stick now meet the tide at the step. We used to know where the oysters would be; you could time your lines to the shape of the moon. Now the moon’s got an appetite."
    "He shifts on his boots, the hem of his sweater catching salt. You watch the way his hands tell time in the air. There's grief beneath his memory, but there is also an account book of"
    "small trade-offs—boats adjusted, fish traps raised, embankments patched. He has learned to live with loss in a way that steadies and frays at once."

    old_tomas_calder "Those cores you're pullin'—keep 'em. Keep them like you're keepin' our birthdays. One day they'll tell us what we didn't listen to.' (He looks at you.) 'Or they'll be all the proof folks need. Either way—it's weight, Mara. Don't let it sink you."
    "The exchange opens a space between you; you want to say that the data will change minds, but Tomas has lived long enough to know that facts sometimes fold into politics like water into sand."

    menu:
        "Ask Tomas about the old oyster beds":
            "Tomas smiles, and for a minute the timeline between past and present narrows. He points out a shallow curve of reeds and names a pattern you didn't know you'd forgotten."
        "Let Tomas finish without interruption":
            "You close your lips and let him keep talking. His voice weaves through the reeds—names, years, small instructions that are more map than memory. You take mental notes like a student of a different grammar."

    # --- merge ---
    "Continue"
    "You collect the final core where the creek widens, the mud column heavy and dark. The graphs begin to line up on your tablet—the trend is unkind. It will sit better if put beside a human"
    "story: Tomas’s hands, the old oyster beds, the way Elias 'Eli' Calder's jaw flexes when he thinks about keeping boats afloat. You catalogue, label, and log everything until the numbers form a shape you have trouble"
    "ignoring."
    # [Scene: Dock Laboratory | Noon]
    hide old_tomas_calder
    hide mara_voss

    scene bg ch2_c4ca42_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Click of instruments, the soft whirr of a centrifuge, the distant town bell marking midday]
    # [Smell: Alcohol for sterilization, faint oil from the skiff]
    "Back at the dock lab, you lay out the cores on the workbench. The water in jars catches the light and splinters it into fragments that feel like questions. Rina Park is already there, sleeves rolled;"
    "she’s barking at a volunteer while balancing a clipboard and a press kit. Her energy is brisk; the NGO scaffolding she offers is efficient and sharply angled."
    show rina_park at left:
        zoom 0.7

    rina_park "Look at this,' she says without preface, tapping a reading. 'If we combine this with the grant I can bend, we can get a pilot installed before the season's out. Visuals. Quick wins. We make a show of resilience."
    show mara_voss at right:
        zoom 0.7

    mara_voss "Quick wins help,' you say. 'They help people pay rent."

    rina_park "They also prove the science works in front of cameras. The funders like to see something that looks like a 'before' and 'after' in a season."

    mara_voss "This isn’t an aesthetic problem,' you counter. 'The cores show salt intrusion deeper than surface shoots. Living shorelines need buffer—space we might not have if the headland gets paved over."
    "Rina's face softens for a moment. She knows the landscape of proposals and press releases. 'We can do both,' she says. 'We make it look like both. Tell the right story.'"
    "You want to believe her. You also know how stories can be shaped to fit an agenda."
    # [Scene: Town Square / Headland | Late Afternoon]
    hide rina_park
    hide mara_voss

    scene bg ch2_c4ca42_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant machinery, a murmur of town voices, an undercurrent of wind against newly posted paper]
    # play music "music_placeholder"  # [Music: Tension in minor keys; a low, insistent piano]
    "You walk back into town with the cores wrapped against your chest. The square smells of fryer oil from a closed-in cafe and the metallic tang of town council announcements. People move in clumps, exchanging words"
    "that are equal parts hope and blame. Nia waves from the bakery doorway—her grin is urgent but thin."
    show nia_voss at left:
        zoom 0.7

    nia_voss "You should see the posters, Mara. Cass's renderings…they're already up on the headland.' (She frowns.) 'They look like a postcard."
    "You keep walking, pulse thudding under the ribs of your shirt. At the edge of the square the board is a shock of glossy color: Azure Crescent—sleek boardwalks, sculpted sea walls, clean plazas promising jobs in crisp type. The renderings glow against the greying sky like an advertisement for forgetting."
    "Mayor Rosa stands near the display, flipping through a packet that smells faintly of fresh ink. She sees you and offers a tight smile that doesn't quite touch her eyes."
    show mayor_rosa_alvarez at right:
        zoom 0.7

    mayor_rosa_alvarez "Mara.' (She gestures at the boards.) 'Cass's team posted the conceptuals this morning. It's a strong sell—jobs, infrastructure. We're trying to thread the needle between protecting people and keeping the economy alive."
    show mara_voss at center:
        zoom 0.7

    mara_voss "Those renderings—did the developer consult independent ecologists?"
    "Mayor Rosa hesitates, then points to a stack of glossies. 'There are assessments—preliminary. Cassandra \'Cass\' Rey's team has models. But you know how meetings go. We still need grounded input. That's—' She falters, as if the"
    "words dissolve into the sea breeze. '—that’s why I wanted you here, Mara. To help translate the science for the council.'"
    "You watch people gather around the renderings: some faces alight with imagined wages and fixed roofs, others folding arms like shields. Cassandra 'Cass' Rey's name sits on the mock-ups like an imprimatur. You feel something cold"
    "spread through your lungs: a realization that renderings can pre-frame a debate, that images can make the possibility of loss seem inevitable before any data is weighed."
    "Elias 'Eli' Calder joins you at your shoulder. He doesn't say anything at first, only watches the panels, then traces a line on one of the designs with his finger—an absent, critical gesture."
    hide nia_voss
    show elias_eli_calder at left:
        zoom 0.7

    elias_eli_calder "They've drafted this to look finished,' he says. 'Like it's already happened. It's powerful, but—' He looks at you. 'What are you thinking?"

    mara_voss "That we need to make the marsh legible in a room full of glossy posters.' Your voice is tight. 'People need to see what’s at stake in terms they understand and in ways that can compete with renderings."

    elias_eli_calder "Data’s your language. Rina’s got flash. Tomas has memory. I…I'll bring the docks and the hull plans. Maybe if we show the work—the craft—people'll see there are alternatives."
    "The three of you stand in a triangle of intent and exhaustion. Underneath the town, under the sound of the sea and the bright paper promise from the headland, something else tunes itself: the moral weight"
    "of making numbers matter against immediate need. You can feel it like the undertow the town hasn't yet named."
    "Rina returns, breathless from a flurry of calls. She slaps a printed page into your hand—an excerpt of Cassandra 'Cass' Rey’s proposal and a press schedule. 'They're framing this as revitalization,' she says. 'Cass wants to"
    "be at the next council hearing with visuals. If we don't have our own narrative, she owns the room.'"
    "Mayor Rosa folds the packet and looks at you both. The motion is small, almost private."

    mayor_rosa_alvarez "I'm asking you—to help me prepare for the council. Your data will carry weight if we present it right. People need a path that keeps jobs without erasing the marsh."
    "You taste the metallic edge of responsibility again. It is heavier now; not just science, but stewardship, politics, and the soft, urgent press of neighbors who need paychecks. The town's future is balanced on a wire"
    "of appeals and compromises. You feel the pull of every voice you haven't yet measured."

    menu:
        "Photograph the renderings for a record":
            "You lift your phone and take a careful picture. The glare catches, but the image will be proof—later, harder to deny. The act feels small, and yet useful."
        "Confront the volunteer posting the banners":
            "You walk over and ask about the models—who paid for them, when they were posted. The volunteer flusters, then mutters corporate jargon, and you collect a few vague answers that will need follow-up."

    # --- merge ---
    "Continue"
    "You fold your jacket tighter against the wind and watch as people cluster like low tide marks—lines of hope, of hunger, of fear. The posters glint. The cores in your bag pulse with patient truth. Tomas’"
    "stories echo in your head like an unpaid debt. The town needs a story that holds both the want for work and the need for place; you are beginning to feel like the seamstress of that"
    "impossible garment."
    "You know you can produce tighter graphs and cleaner visuals. You know you can write briefs and stand at a podium. But you also know the work will require translation into empathy and the stubborn persistence of many hands."
    "As the sky bruises toward evening, you make a decision—not a choice shown on a chart, but a shifting of weight in your chest. It will be a long argument; tonight is only the first measured step."
    hide mayor_rosa_alvarez
    hide mara_voss
    hide elias_eli_calder

    scene bg ch2_c4ca42_5 at full_bg
    # play music "music_placeholder"  # [Music: A single low chord, unresolved]
    "You inhale the taste of salt and cold and the sharper tang of obligation. The town is gathering its pieces, and so must you."

    scene bg ch2_c4ca42_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
