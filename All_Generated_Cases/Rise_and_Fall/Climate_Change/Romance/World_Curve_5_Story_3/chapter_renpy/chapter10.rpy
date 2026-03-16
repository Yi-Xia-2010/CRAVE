label chapter10:

    # [Scene: Community Greenhouse & Restoration Lab (Boathouse) | Morning]

    scene bg ch10_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, insistent piano under a distant electronic thrum]
    # play sound "sfx_placeholder"  # [Sound: The soft click of sensors booting; a drone chirps in standby]
    "You arrive before most of the volunteers. The boathouse smells of wet timber and coffee gone cold at the edges; the damp air makes your hair cling to your neck. Your weathered notebook lies open where"
    "you left it, the brass clip catching weak light like a promise. Dr. Kaito’s sweater hangs on a peg, speckled with algae stains — an apology and an anchor. Around the workbenches, an array of environmental"
    "sensors bleeps and breathes, their small LEDs pulsing like a nervous chorus."
    "This is what you wanted: hands on instruments, townspeople turning their care into data. But the pulse in your throat is not only purpose. You feel the shape of pressure closing in, the way a tide"
    "reshapes a shoreline minute by minute until the break is done. Evidence can be a weapon; it can also be a target."

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft hum of a laptop; the drone's idle whine]
    show dr_kaito_mori at left:
        zoom 0.7

    dr_kaito_mori "Morning, Amaya. The conductivity suite finally came online overnight. We've got salinity variance that tracks with the bay's last ebb.' (He taps a tablet, eyes gentle but lined with worry.) 'If we sample the right corridors, we can show the marsh's buffering capacity with numbers that even the committee can't ignore."
    show amaya_saito at right:
        zoom 0.7

    amaya_saito "Good. Let's calibrate those nodes along the southern channel first. If we pair that with the aerial transects, the model will be more robust."
    "Dr. Kaito: (He glances at you, then at the sensors.) 'Be careful with the chain of custody. Corporate counsels love to find sloppiness. If they question our data’s integrity, they'll buy time.'"
    "Amaya Saito: (A dark, practical breath.) 'Then we keep logs, time stamps, redundant feeds. We treat the datasets like witnesses, not just numbers.'"
    hide dr_kaito_mori
    hide amaya_saito

    scene bg ch10_453e40_3 at full_bg
    show mika_tan at left:
        zoom 0.7

    mika_tan "Okay, show-off mode activated. Teach me how not to crash it into the gulls, Professor Amaya."
    "Amaya Saito: (You smile despite the tightness in your chest.) 'We'll start with gentle turns. Remember: the camera’s angle tells the story as much as the altitude.'"
    "You coach Mika through preflight checks: rotor inspection, battery health, GPS lock. Her fingers are clumsy at first, then steadier. There is a small satisfaction in watching someone else learn how to translate care into a mechanical act that will become evidence."

    menu:
        "Let Mika take the coastal transect solo":
            "You step back and let her pilot the drone along the marsh mouth. Her hands tighten, then relax; the live feed shows long ribbons of eelgrass and a small heron slipping between channels. You feel a clean, quiet pride."
        "Stay at her shoulder and narrate every adjustment":
            "You keep a steady play-by-play in her ear. Mika breathes with your directions; the footage is precise but slightly stiffer. She looks at you with a new sort of gratitude."

    # --- merge ---
    "Scene continues."
    "The first wave of scouts returns with the data feed. You watch the timbered pixels stitch together into a story: sediment traps, dense root mats, pockets of peat that hold last season’s water like a sponge."
    "You annotate, you timestamp, you check the backups. Each file is a little monument, a testimony to processes that Atlantech’s renderings would flatten under concrete."
    hide mika_tan

    scene bg ch10_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmurs grow into purposeful chatter]
    "Lucas Herrera: (He moves in with a quiet efficiency, AR goggles folded above his forehead. He sets a slim tablet on the bench and places a neat stack of printed feeds beside it.) 'I pushed you"
    "the regional sensor overlay last night.' (His voice is practical; there is a polite distance in the way he says your name.) 'It meshes with your transects.'"
    "Amaya Saito: (You look at the tablet and then at Lucas.) 'Thank you. That overlay will help scale our local numbers against broader tidal patterns.' (You want to press for warmth — to bridge the professional gap — but you feel the leash of politics taut between you.)"
    "Lucas Herrera: (He looks away for a beat, expression unreadable.) 'I can keep sending feeds. But I have to keep some things... compartmentalized.' (He pauses.) 'There's a legal hoop with my employer. I can't be too public.'"
    "Amaya Saito: (You let the silence do some of the work.) 'I know.' (Your voice does not hide the question: How much distance can a relationship survive when evidence and loyalty pull in different directions?)"
    show lucas_herrera at left:
        zoom 0.7

    lucas_herrera "We have to be careful. If our collaborators sense internal feeding, Atlantech will frame it as a conflict of interest. We lose credibility.' (He taps the tablet as if punctuating a point.) 'But the data — let it speak."
    "His words are precise, the way he smooths a line on a CAD model. You want to feel betrayed; instead you feel the cold press of pragmatism. He is trying to protect both of you —"
    "or at least protect what he can. You can read the calculation in his jawline and the way his hands do not reach for yours."

    menu:
        "Ask Lucas to come to the public presentation":
            "You invite him outright. He looks like you’ve asked him to cross a line; he gives a measured, 'I'll see if I can,' and the answer is both hopeful and hedged."
        "Keep him compartmentalized and accept the feeds":
            "You nod and accept the data without pressing. He leaves with a small, tight smile. You feel the closeness loosen like a knot pulled slack."

    # --- merge ---
    "Scene continues."
    "By noon you have a packet: salinity gradients, trapped sediment profiles, species corridor maps, and an initial model of carbon sequestration. Volunteers gather to label the findings in plain language — 'This peat is holding X"
    "liters of stormwater' — and pin them in a place where the mayor and committee can read without a scientist's glossary. There is a rhythm to the work, the kind that quiets the chest for a"
    "while."
    # [Scene: Takase Cove | Afternoon]
    hide lucas_herrera

    scene bg ch10_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low tide sighs; gulls call like punctuation]
    "You take the portable projector to the cove and lay the visuals against the corrugated side of the fish market. Children cluster, elders lean their canes, and a fisherman wipes his palms on his jeans and"
    "squints. The graphics roll: living systems behaving like engineered assets, but older, messier, dignified. Someone starts to clap when a map shows how the marsh absorbs a winter surge; it is small and human. For the"
    "moment, the crowd's attention is a shield."
    "Elena: (She stands beside you, scarf bright against the gray.) 'This is the kind of testimony the committee needs,' she says. (Her voice carries both hope and the weight of a decision she loses sleep over.)"
    "'But the council will demand immediacy. They're watching the jobs spreadsheet like it's a tide.'"
    show amaya_saito at left:
        zoom 0.7

    amaya_saito "We can say both: here's the immediate benefit and the long-term value. We can make a plan that buys time without conceding the marsh."
    show elena_cruz at right:
        zoom 0.7

    elena_cruz "Good.' (Her fingers close around yours briefly — a small, stabilizing squeeze.) 'But remember: the other side will not just rebut with words. They have lawyers and timelines."
    "Your chest tightens again. You can feel the outlines of attack: doubt sown into method, a rush to construction that would make data moot by being ahead of it. Evidence is useful, but it moves slower than power."
    hide amaya_saito
    hide elena_cruz

    scene bg ch10_453e40_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Notification chime — a small metallic pang]
    "Elena: (She reads, eyes narrowing.) 'They want to speed up the permit timeline. They say 'unforeseen marine stability concerns' — a phrase meant to sound urgent.' (Her jaw sets.) 'They're leveraging provincial funding slots. If they secure that, it becomes politically costly to delay.'"
    "You watch the color drain from people's faces. The volunteers knit their brows; an old woman mutters that the town has weathered storms before. The air feels thinner, as if someone's hand has closed over the boathouse's open door."

    scene bg ch10_453e40_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hum lowers; someone breathes too loud]
    show mika_tan at left:
        zoom 0.7

    mika_tan "Is that... legal?"
    show dr_kaito_mori at right:
        zoom 0.7

    dr_kaito_mori "It will be. And their fastest move is often their most efficient weapon: deadlines and paperwork.' (He taps the tablet with a finger. Something older and resigned flickers in his eyes.) 'They're good at making urgency feel inevitable."
    "The movement that felt like momentum twists; legitimacy draws attention, and attention is what power uses to sharpen its edge. Your data has made a dent. That dent has bled light onto the marsh — and now, the cutters gather."
    hide mika_tan
    hide dr_kaito_mori

    scene bg ch10_453e40_8 at full_bg
    # play music "music_placeholder"  # [Music: Low strings, a slow, descending minor motif]
    # play sound "sfx_placeholder"  # [Sound: A formal knock — a different tone from social media outrage: a lawyer's letter, crisp and procedural — is delivered to Elena's office via courier.]
    show elena_cruz at left:
        zoom 0.7

    elena_cruz "They're seeking an injunction to restrict access to the construction site on the grounds of 'safety and pre-construction surveys,' which would prevent our independent sampling during critical tides.' (She exhales, the breath coming out like a cold tide.) 'They've also put forward a matching-funds offer tied to a non-disclosure framework."
    "It is a classic maneuver: buy the town with one hand, blind it with the other. The matching funds would mean new jobs, repairs, and immediate relief. The NDA would mean silence — and with silence, the marsh becomes easier to ignore."
    "Amaya Saito: (You feel the old familiar tug of guilt, strict and accusing.) 'We can't accept a deal that trades the marsh for short-term fixes. Not without binding protections.'"

    elena_cruz "I know.' (Her voice is small under the weight of civic responsibility.) 'But I also know council members who lost roofs last season. They will see those funds and think of immediate needs."
    "You picture the ledger of people's lives: roofs, small businesses, fishing gear. You can see why decisions that look like betrayal from one angle look like salvation from another. The moral landscape is not a black and white shore; it is a tidal plain, shifting beneath your feet."

    menu:
        "Organize a visibility action at the construction site":
            "You suggest taking the fight visibly to the site. Volunteers light up with defiant energy. The idea feels righteous and raw; it will draw attention but escalate confrontation."
        "Double down on the data — publish, peer-review, and legal-vet everything":
            "You push for rigorous publication. The lab nods; Dr. Kaito looks relieved, as if science itself can be an armor. It will take time, and time may be precisely what they aim to erode."

    # --- merge ---
    "Scene continues."
    "Late that night, you stay to cross-check timestamps, to encrypt backups, to lay out a public-facing brief that speaks plainly. The greenhouse light is small and domestic against the dark. Outside, the seawall site pulses its"
    "artificial light at the edge of town, a reminder that the project waits like an oncoming storm."
    "Lucas Herrera: (He comes back to the boathouse door and stands in the frame, rain beading off his shoulders.) 'They've already started pre-fabrication orders,' he says quietly. 'Logistics are lining up. If they secure the funding"
    "window, the inertia becomes real.' (His voice is tired; it's as if the news is a stone he's been carrying.)"
    show amaya_saito at right:
        zoom 0.7

    amaya_saito "What can we do to stop it from becoming inevitable?"
    show lucas_herrera at center:
        zoom 0.7

    lucas_herrera "You arrest momentum with public certainty,' he replies. 'You make delaying postures politically costly for them. Data helps. So does a narrative that ties the marsh to livelihoods.' (He meets your eyes, and there is for a heartbeat the man you know beneath the professional reticence.) 'But time is closing."
    "The distance between you is not just spatial. It is measured in the lines of his expression where corporate caution and personal care intersect. You want to ask him to choose a side. Instead you measure the timeline, the processes, the vulnerability of open datasets to legal contests."
    hide elena_cruz
    hide amaya_saito
    hide lucas_herrera

    scene bg ch10_453e40_9 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The tape rips; a gull cries far off like a question]
    "You look up at the window where the seawall site glows. The town is awake with a new kind of tension: purpose braided with dread. Your campaign has moved from politely empirical to provocatively consequential. The data gave you a foothold in the argument; power answered with steel and schedule."
    "You feel the shift as palpably as a change in the tide. There are more people behind you than before, but they are also more exposed. Tonight, the lab hums; outside, the machines hum louder. The"
    "hardest thing you have to accept is that legitimacy breeds resistance, and resistance can come with legal teeth and funding bait."

    scene bg ch10_453e40_10 at full_bg
    # play music "music_placeholder"  # [Music: Resolve-subdued strings, trailing into silence]
    "You close your notebook and slide the brass clip over the public brief. Your palms are steady, but your body remembers storms in a way that calm minds cannot deny. Whatever you do next must move"
    "faster and smarter than the tide — and it must hold people's attention long enough to matter."

    scene bg ch10_453e40_11 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter11
    return
