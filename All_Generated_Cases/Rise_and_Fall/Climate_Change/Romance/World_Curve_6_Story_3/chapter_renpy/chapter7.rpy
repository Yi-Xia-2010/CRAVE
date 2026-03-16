label chapter7:

    # [Scene: Tidewatch Laboratory | Late Afternoon — Storm Warning]

    scene bg ch6_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind rising, aluminum siding rattling; the distant, urgent cry of gulls]
    # play music "music_placeholder"  # [Music: Low, mournful strings; a single piano note repeats like a heartbeat]
    "You feel the pendant cool against your skin and count the minutes in the staccato flashes of the lab monitors. The prints in your satchel tremble when the building groans—old timbers shifting under a new, older"
    "force. The living-dike models pinned to the wall shake as if remembering storms that came before you were born."
    "A status cascade scrolls across Elliot's tablet: sensor arrays reporting salinity spikes, wave overtopping at the northern coir bund. You smell wet wool and the sharp tang of salt on copper. Your hands are steady but your chest is a tight, small drum."
    show elliot_chen at left:
        zoom 0.7

    elliot_chen "We're reading a south swell chain—bigger than the model predicted. The northern span's pressure sensors just spiked. If the coir fails there, it channels across the reed bed—"
    "You cut him off with a quick, practical breath."
    show maya_ibarra at right:
        zoom 0.7

    maya_ibarra "Tell me what holds for ten minutes. Tell me what to call for immediate evac if it doesn't."

    elliot_chen "Ten minutes—maybe. We can patch with the extra woven panels, but we'll need hands on the boardwalk now. Tomas is calling volunteers. I can route a push team to the northern nodes, but—' He swallows. 'But that leaves the central marsh thin."
    "You watch his jaw work. He is thinking two moves ahead like he always does—designing scaffolds inside a squall. The thing you both promised the town—speed, community labor, a living solution—now asks the town's bodies to be its scaffold."

    menu:
        "Run to the northern node with volunteers":
            "You grab an extra roll of coir, knot the straps, and head out with Tomas and three others, boots slapping on the slick boardwalk, the wind trying to take the rope out of your hands."
        "Stay in the lab and coordinate sensor reroutes with Elliot":
            "You stay behind, fingers flying on the console, voice sharp as you reroute power and prioritize sensor feeds; Elliot leaves to marshal hands while you keep the map alive."

    # --- merge ---
    "You do both, really—because that is how you always end up living: hands in two places at once. You shoulder the satchel, press your shawl tighter, and follow the chaotic map Elliot speaks while the lab behind you smells like algae and printed ink."
    # [Scene: Living Dike — Boardwalks & Reclaimed Wetlands | Storm Onset]
    hide elliot_chen
    hide maya_ibarra

    scene bg ch6_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Waves smashing into reed tangles, the creak of tension-thinned ropes; shouts carried and broken by the wind]
    # play music "music_placeholder"  # [Music: Aggressive low brass, then a single violin line that wavers]
    "The wind is all teeth. Rain slashes the boardwalk and drives salt into the corners of your eyes. Volunteers work faster than any forecast: Rosa passing sandbags, Tomas barking reminders, a tide of small faces against a sea that wants to take everything it touches."
    "You tie a splice you learned on your father's boat, fingers numb, thinking of the slow braid of woven rope he taught you—mend the tear so it lasts. A section to your left slumps; reeds peel"
    "like scabbed fingers. You feel the awful, sharp logic of loss: you can save some stretches, but others will not make it this night."
    "Noah Rhee appears in the slipstream of a gust, rope over one shoulder, face carved into a line of worry and something worse—steadfast impatience."
    show noah_rhee at left:
        zoom 0.7

    noah_rhee "This is where we need heavy riprap, Maya. This fraying won't hold a week. Patchwork costs lives.' (He breathes out, interlocked with salt and diesel.) 'I told them. We need armor where people fish. We don't have time to let a garden decide when your nets need to be mended."
    show maya_ibarra at right:
        zoom 0.7

    maya_ibarra "We don't have to let them be separate things, Noah. The marsh filters and steadies—if we hold it, the nets last longer than a wall that cuts off the nursery."

    noah_rhee "That's good in a book. Out here, storms don't read the same book. People want to eat.' (His hand tightens on a coil of rope.) 'You asked for hands—fine. But don't come telling me the marsh will feed my kids tonight if it doesn't make rent tomorrow."
    "The exchange is a small knot of old arguments—trust, timing, the vocabulary of livelihoods. It is also a rehearsal for the choices the town will make after the storm has sung its verdict."

    menu:
        "Try to talk Noah into shifting to a shared plan now":
            "You move closer, rain washing your hair into your eyes, and you try to knead the anger into a plan: 'Help me hold this span. After we shore, you and I draw lines where your crews get the riprap. We won't lose the marsh while we feed people.' Noah's jaw loosens fractionally, then clamps—an old habit."
        "Let him go—focus on the volunteers":
            "You nod once, not conceding, and turn away. Words won't stop the incoming water. You have people to direct; you cannot carry Noah's whole history tonight."

    # --- merge ---
    "You choose the town—because it has always been the immediate thing that keeps you upright. You shout orders that are small and precise: drop the farther posts first, hold the reed bundles at a forty-five degree"
    "shear, two pairs to each splice. The volunteer chorus becomes a machine of hands. For a while, for some sections, it works: water breaks, reed fingers still curl."
    "And then, with a sound like old boards giving up, a span ruptures farther down—where earlier chains of dredging had stripped a line of marsh for a quick haul. The seawall patches there take the brunt,"
    "but only for a breath; the wave finds the exposed seam and widens it like a mouth."
    "You feel a cold, animal panic—sharp and bright—then the labor reclaims you: evacuate the lowest pier, move the trailers, check the sensor buoy lines. Elliot's voice, amplified by a radio, cracks into your ear."
    show elliot_chen at center:
        zoom 0.7

    elliot_chen "Northern node has breaches—two sensors offline. I'm steering the array to triangulate flow, but I need physical anchors on Node C and D or our models go blind. I'll mark them on your map—"

    maya_ibarra "I'll take Node C. Rosa, with me. Tomas, rope to Node D. Move people to the lighthouse if we lose the docks."
    # [Scene: Beacon Lighthouse | Night — The Storm Peaks]
    hide noah_rhee
    hide maya_ibarra
    hide elliot_chen

    scene bg ch6_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The lamp throbbing, waves smashing rock, the thin, wailing siren of an automated flood alert]
    # play music "music_placeholder"  # [Music: A slow, descending cello; wind instruments whispering with loss]
    "Inside the lighthouse, the community gathers by necessity and exhaustion. Mayor Cortez stands at a folding table, a stack of municipal binders and a tablet lit with emergency feeds. Her hair is a silver rope tied"
    "back into the severe bun you've seen for town meetings, but tonight it seems less a political posture and more a tired, human thing."

    "Mayor Cortez" "We shepherd people to the lighthouse and the school gym. We stamp paperwork later. Right now—who's accounted for Nora's house? Who's taken the Smiths? Reports only if you have them."
    show maya_ibarra at left:
        zoom 0.7

    maya_ibarra "Nora and her kids are heading inland with Rosa. I marked the Smiths' boat as deployed. Tomas and Noah have crews running the docks."
    "Mayor Cortez reads, then closes her eyes for a second, a micro-sadness you know well: the weight of balancing the municipal drawer of lives against the ledger of policy."

    "Mayor Cortez" "The emergency fund can cover temporary housing and emergency contracts, but long-term recovery will require clear governance. We can't rebuild every pier, and we can't let developers re-zone marshland because it's convenient. I will call a council vote in two days. We need a governance structure that combines municipal oversight with a rotating community stewardship. It will cost—' (She flicks a finger at the tablet.) '—condemnations, buyouts, legal holds on any outside construction. That means some piers will be condemned. Some crews will lose plots they rely on. We will have to buy fishplots or compensate in other ways."
    "The room shifts under that language. You can feel the stomach-ache of each fisherman in the room. There is a new, hard knowledge settling like silt: the rescue tonight is only the beginning. Mayor Cortez's plan"
    "is a brittle, necessary thing—legal scaffolding for a future that asks people to lose now to gain later."
    show noah_rhee at right:
        zoom 0.7

    noah_rhee "Condemn my pier? You can't auction the only place my family has had since my grandfather. You can't make a price for a place where we learned to net shrimp."

    "Mayor Cortez" "Noah, I don't want to take anyone's ground. But I also can't risk a dozen small fixes that give us false confidence. If the marsh isn't protected, the piers won't be either. This is—' (She pauses.) '—this is governance with teeth. Pain now so the rest doesn't get eaten."
    "Noah grinds his jaw. The look he gives you is not only anger but something colder: betrayal, perhaps, or disappointment that the community negotiation has made him an example."

    noah_rhee "You call it governance; I call it a choice that kicks people when they're down. I can't sign on to a plan that sells out our nets to make nice gardens for grant writers."
    "You open your mouth, searching for words that can hold both the ache of his family and the math of the models. The room hums with a thousand small calculations—who will stay, who will go, who will be responsible for stewarding what remains."
    # [Scene: Docks & Tidewatch Laboratory | Dawn After the Storm]
    hide maya_ibarra
    hide noah_rhee

    scene bg ch6_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slow drip of runoff, a gull's lonely call, the distant bark of a generator]
    # play music "music_placeholder"  # [Music: Sparse piano, minor-key, a slow, downward motion]
    "Dawn finds the town stitched and torn. Some living-dike stretches held—calluses of community labor and nascent root-mat now barely clinging to their wins. Other stretches yielded; mud exposed where marsh once rose, and where it was ripped a small, brutal geometry of exposed soil feeds the sea."
    "You walk the burnt arc of it all: fingers on the satchel strap, pendant cold and small under your sweater. Volunteers clean debris. Rosa photographs quietly, the camera capturing the brittle edges of relief on faces."
    "Tomas stands with his hands folded like a man holding a lineage, eyes on the horizon."
    "Elliot Chen meets you outside the lab, rain-creased and exhausted, the sketches in his roll damp at the edges. He looks like someone who has seen a blueprint come apart and tried to stitch it back with new thread."
    show elliot_chen at left:
        zoom 0.7

    elliot_chen "We kept most of the residential stretch. The nursery pockets at G and H are gone, though. We lost a breeding ground for the estuary that was critical for fall runs.' (He looks at the maps, speaks as if confessing.) 'If we want to maintain yields, the models say we need a governance framework—zoned protections, buyouts of high-risk plots, and a regional oversight body to coordinate funding. I can help build it, but—' He hesitates, fingers twisting his wet collar. '—but I got an offer. A regional post to scale the model across the coast. It would fund the research, the personnel… it could make sure more towns don't lose what you did."
    "You feel the word 'leave' like a stone in your mouth."
    show maya_ibarra at right:
        zoom 0.7

    maya_ibarra "If you leave, who will hold the bridge between design and this town's memory? Who will keep the designs honest to the people who built them?"

    elliot_chen "You know me. I try to be honest. I also know how fast money and power can twist good work. I need to be somewhere where I can secure the grants and frameworks so this becomes replicable. If I stay, I'm one small voice. If I go, I can be a louder one for towns like ours.' He steps closer, the salt of his skin against the storm-washed air. 'I want to be here, Maya. I always do. But I also can't do it alone. This post is a chance to lock in the resources we need for Veridian—and for others. I won't let this be a PR thing."
    "You want to argue that proximity matters more than position. You want to say that being here—hands, mud, the sound of nets being brought in—matters. But the storm taught you that systems and scaffolding are also required. Your throat tightens."

    maya_ibarra "When would you leave?"

    elliot_chen "In two weeks. They want me to start immediately. But… I will keep the sketches, the pilot notes, and I will make channels to fund local stewardship boards that Mayor Cortez is proposing. I promise."
    "You look at him—at the earnestness in the way he wants to do good and the restlessness that makes him accept a promise of scale. In the end you nod, because you have to. There is a strange grief in handing someone a future you cannot fully share."
    "Rosa, watching you both, presses a hand to your arm and squeezes as if mapping the way you are pulling away."
    # [Scene: Council Hall / Community Forum | Two Days Later — The Announcement]
    hide elliot_chen
    hide maya_ibarra

    scene bg ch6_601bcb_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmurs ebb and flow; a microphone scratching feedback now and then; coffee cups clink]
    # play music "music_placeholder"  # [Music: A low, elegiac string chord underpins the room]
    "Mayor Cortez speaks with the trained cadence of someone who has carried hard choices like crops through winter."

    "Mayor Cortez" "The council has voted to enact a mixed governance approach. We will form a rotating stewardship council with municipal authority and community-elected seats. We will condemn and buy out the most at-risk piers to prevent dangerous rebuilding. We will place legal holds on Veridian Holdings' contracts while we negotiate conditional partnerships that enforce ecological safeguards. These measures will be costly and painful."
    "A man in the back stands, voice raw."

    "Dockworker" "So you condemn the places our families live and tell us it's for the best? How do we feed our kids while waiting on government programs?"

    "Mayor Cortez" "There will be compensation, transition programs, and—' (She meets the man's gaze, every word measured.) '—priority for local employment in the restoration work and the distributed maintenance of living dikes. We will put the first tranche of emergency funds to that."
    "Noah Rhee, standing at the side, folds his arms and does not speak. His silence is louder than any protest. Later, when the doors are open and the mic is off, he turns away and walks"
    "down Main Street without looking back. You watch him go—broad shoulders receding into the salt haze—and you know that some fractures rearrange people as firmly as waves rearrange sand."
    "You feel a complicated, sour relief. The governance plan will create an architecture for accountability and stewardship—something you fought for. But the costs are physical and social: condemned piers, sold fishplots, legal binds, and people displaced."
    "You think of families you know, of Nora's kids, of the Smiths, of the smell of diesel oil on Noah's sleeves. You think of your father's empty chair and the insistence that made you try to"
    "braid the town together."
    # [Scene: Tidewatch Laboratory | A Quiet Evening Later]

    scene bg ch6_601bcb_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The tick of a clock, the soft rustle of paper, Rosa sorting photographs]
    # play music "music_placeholder"  # [Music: A low, steady cello that does not resolve]
    "Elliot Chen packs his portfolio carefully, folding sketches like vows. He looks up at you once, the look saying more than plans can hold."
    show elliot_chen at left:
        zoom 0.7

    elliot_chen "I don't know exactly how it will look from there. It will be bureaucratic. It will be slow. But it's not nothing."
    show maya_ibarra at right:
        zoom 0.7

    maya_ibarra "It's not nothing,' you echo, but the phrase goes smaller in the air, a pebble in a swell. 'Promise me you'll keep Veridian in the designs. Don't let it be another case study where people are footnotes."

    elliot_chen "I promise."
    "The word is fragile. You lean across the desk and grip his forearm for a long, meaningful second. The contact is warm and human and not enough."
    "You turn away to the map. Your fingers find a place where pins crowd: a triangle of wet ink and thread. The list of names beside it is a census of care: volunteers, households, elders. You"
    "trace a line from the living dike to a legal note on the binder—stewardship, rotating authority, local employment provisions. The scaffolding is in words now; the real work will be the slow muscle of living it"
    "into being."
    "Rosa sets down a photograph between you and Elliot: a picture of volunteers mid-shift—mud-splattered, laughing through the work. The image is stained at the edges with salt, a small, stubborn proof of what you managed."
    # [Final Scene: Beacon Lighthouse Cliff | Sunset — Aftermath and Quiet]
    hide elliot_chen
    hide maya_ibarra

    scene bg ch6_601bcb_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant tide, the breath of wind, low voices folding into the dusk]
    # play music "music_placeholder"  # [Music: A minor-key piano, each note settling like shell fragments on sand]
    "You stand at the cliff edge, pendant cool against your chest. The town behind you smells of tar, brewing soup, smoke from a single, hurried bonfire. The estuary before you is both wounded and breathing—new root-mats"
    "clinging, exposed mud flats visible where nursery pockets were lost. It is messy and real."
    "Elliot Chen's departure is hours away. Noah Rhee's absence is an ache that the town will measure differently tomorrow. Mayor Cortez's plan is law now, a brittle scaffolding that will bend under the weight of implementation."
    "You feel the residue of the storm inside you: grief for what was lost, relief for what was held, and a fatigue like old rope."
    "You let the pendant rest between your fingers. The glass is worn but whole. It was never meant to hold storms, but it has become your small, private place to put sorrow."
    "You think of the living-dike volunteers, of Tomas's sermon about remembering the old tides, of Rosa's quiet documentation. You think of the compromises—legal holds that will keep Veridian Holdings at bay, emergency funds that will give"
    "people some breathing room, condemned piers that will cost history and memory but buy a chance at a future."
    "It is not a victory; it is not a defeat. It is, as the options led to here, a complicated ledger: partial protection, lost marsh pockets, and a governance framework that demands vigilance and the willingness"
    "to be inconvenienced by ethics. You have the beginnings of something — a system that will require everyday small sacrifices and a council that can be rotated, a trust that must be earned every week at"
    "low tides."
    "You let out a breath that tastes of salt and iron and a reluctant kind of hope. It is a damp thing, held small like a seed in a raincoat pocket."
    "Elliot Chen comes up beside you and stands looking at the horizon. He does not offer grand phrases. He only reaches for your hand and holds it like a thin anchor."
    show elliot_chen at left:
        zoom 0.7

    elliot_chen "Go home, Maya. Rest. We'll need you tomorrow and the day after and the one after that."
    show maya_ibarra at right:
        zoom 0.7

    maya_ibarra "I will go home. I will be here."
    "You step back from the cliff and down toward the town where people are already clearing the last of the temporary shelters. The work is endless and essential. Your guilt remains — a carved hollowness under"
    "the ribs — but it has a job now: to keep you from softening the plans that must be enforced."
    "Night comes down like a curtain. The lighthouse turns once, twice—steady. You fold your scarf tighter and walk into the small, lit windows of Port Veridian where people are sitting with their wounds, counting what they can rebuild."
    "You are tired. You are necessary. You are not done."
    hide elliot_chen
    hide maya_ibarra

    scene bg ch6_601bcb_8 at full_bg
    "THE END"
    # [GAME END]
    return
