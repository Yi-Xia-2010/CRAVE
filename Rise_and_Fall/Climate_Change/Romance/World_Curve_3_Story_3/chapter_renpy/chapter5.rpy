label chapter5:

    # [Scene: Rooftop Watch at Dusk | Evening]

    scene bg ch5_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, pulsing synth with distant thunder undertones]
    "You stand with the tide-watch against your wrist, brass warm and slightly sticky from salt. The town below is a scatter of lamplight and urgent movement—figures like stitches along the shoreline. The municipal alert still lingers"
    "on the edge of your thoughts, a pinprick you can’t ignore: WATCH SYSTEMS REPORT — ELEVATED TIDE PROJECTIONS."
    "Wind moves through the rooftop herbs and makes the potted basil whisper. It smells of wet soil and something metallic that makes your teeth ache when you breathe deeply. In the corner of your vision a"
    "battered telescope points toward the sea; you don't need to look through it to see the seam of darker water migrating inland like a bruise."
    "Your hands are steady in public, you have trained them to be. But alone for a moment, tide-watch heavy, you feel the tremor under your palm—the small not-quite of a human thing that can't be fixed"
    "with a model or a meeting. You think of the seedlings in the mangrove trays, bent like small pleas in the wind, and the tilt of your own commitment toward the untested plan."
    # play sound "sfx_placeholder"  # [Sound: Distant radio bleat; a clipped, official voice repeats the advisory]

    scene bg ch5_4001e7_2 at full_bg
    "You should go down. The barriers are thin, the stakes are thin, and people are already moving like a tide that forgot caution. You fold your scarf tighter, feel the salt under your nails, and climb down."
    # [Scene: Makeshift Barriers / Docks | Night]

    scene bg ch5_4001e7_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind slashing through ropes, the hollow clank of a buoy, and the urgent murmur of voices]
    "The worksite is a chorus of hurried commands and the scrape of metal. Lanterns swing, throwing sharp shadows over spray-streaked faces. Elias Jun is there, paint on his knuckles, shouting something half-lost to the wind. Rita"
    "moves among the clusters of neighbors with that quick, practical solace she’s always had—reminding someone to hold a tarp, handing out headlamps, making lists on the fly."
    "Arlo is on a ladder near a supporting net—young, hands still learning the right pressure. You almost don't register his movements until the ladder tips with a wet, complaining sound. The net thrums like a plucked"
    "wire. There's a small, bright scuff of skin on his forearm, and the way he lets out a breath makes your throat close."
    show elias_jun at left:
        zoom 0.7

    elias_jun "Arlo—hold on, kid! Don't—(lower your voice, you're doing fine)."
    show rita_ortega at right:
        zoom 0.7

    rita_ortega "Someone with a first-aid kit, now! And check the anchor points—if that net gives, it could slack and take the whole line."
    "Everyone moves at once: hands, feet, voices. Your feet find the broken planks and climb. You reach Arlo as he slides down, palms raw, eyes wide with that faraway look of shock that takes time to come into words."
    show maya_reyes at center:
        zoom 0.7

    maya_reyes "Arlo—look at me. Blink if you can hear me."
    "Arlo: (breathing fast) 'I—I thought I could tighten it before the gust—'"
    "Elias Jun: (kneeling beside him, one hand steadying Arlo's shoulder) 'You did good, kid. You did—' (he swallows) 'You kept going.'"
    "Rita: (frantic and practical) 'We can't keep doing this while the weather's turning. We need a plan to get people out if it gets worse.'"
    "The wound is small but the impression is large—an exclamation point made of salt and plaster. The crowd closes in and opens like surf. You can feel a low slide in your chest: the culpability that"
    "has been building inside you, brick by brick, since you first championed the community build."

    menu:
        "Kneel and inspect Arlo's arm carefully":
            "You kneel, fingers cold as you unroll gauze. You talk to him in short, steady sentences—names for body parts, steps for healing—because words can anchor both of you when the world does not."
        "Pull Arlo back to the sandbags and call for a medic":
            "You tug him away from the ladder, your hands clumsy with urgency. You bark orders—who will get the med kit, who will hold his head—and the work around you snaps into a more guarded rhythm."

    # --- merge ---
    "You choose, and the moment slides past. Whatever you do, Arlo inhales and exhales, and the net continues to shudder in the wind as if reminding you that improvisation has limits."
    "Elias Jun: (voice tight) 'We can still finish the supports tonight. If we get the anchors in before the tide, they'll hold long enough. We can fix anything—'"
    "Rita: (cutting in) 'Fix what, Elias? Fix a hole in a paper boat? Maya, you know permits—Ayla's right about the paperwork. If we keep building without the proper approvals the grant dries up.'"
    "Ayla's warning—clinical, absolute—echoes like a bell you can't unhear. She had spoken about strings of custody, certified materials, and oversight. In the quiet between Rita and Elias her presence feels like a clean-edged question you can't answer with a borrowed hammer."
    # play sound "sfx_placeholder"  # [Sound: A message tone; someone holds up a phone toward the small crowd]
    hide elias_jun
    hide rita_ortega
    hide maya_reyes

    scene bg ch5_4001e7_4 at full_bg
    "Maya Reyes: (your throat tight) '(answering) Ayla?'"
    "Dr. Ayla Voss: (voice on the line, even, measured) 'Maya. I see the telemetry. Your alert is on my console. I need you to halt any unpermitted structural work until we coordinate a verified plan.'"
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "If we stop now, the anchors won't set. The seedlings and the tidal buffers take days—"
    "Dr. Ayla Voss: (pausing) 'I understand attachment, Maya. My role is to secure scalable solutions and ensure funding isn't forfeited. If the project is cited for noncompliance, the oversight board could withhold the grant. That would not only halt construction, it would prevent certified engineers from supervising necessary repairs post-storm.'"
    "Her tone is cool, not unkind but relentless—like a scientific instrument reading a temperature you don't want to know. You notice in the way people listen that Ayla's words carry a weight that could snap communal momentum if it lands wrong."
    "Elias Jun: (interrupting) 'So we just wait? While the water eats the shore? While families lose their things? We'll lose more than a grant, Ayla.'"
    "Dr. Ayla Voss: (voice, carefully) 'I am advocating for long-term survivability, Elias. Short-term fixes can create long-term liabilities. Compliance matters for more than paperwork.'"
    "Rita: (to Elias, fierce) 'It's not just paperwork, it's leverage. If we burn the bridge to funding, we'll be alone and broke when the real engineers come in.'"
    "Elias Jun: (softening, then harder) 'And if engineers come and tell us to leave, what then? I won't sit and watch my home be taken without trying.'"
    "Their exchange circles a gulf you've felt widening since you returned: pragmatic caution versus stubborn, hands-on defiance. You are sitting on the seam, the person who tied local momentum to an untested patchwork with your name on it."

    menu:
        "Tell Elias you'll reinforce tonight with him, but call Ayla to ask for conditional oversight":
            "You say it quickly, a stitch between two urgencies. Elias nods, hope flitting across his face; someone hands you a walkie-talkie and you reach for Ayla's number as if it were a lifeline."
        "Tell Elias to stand down and organize evacuations":
            "You say it flat, the words stripping warmth from your chest. Elias glances at you like you've moved continents. People around you stiffen; the work slows as hands drop."

    # --- merge ---
    "The wind takes your answer and makes it a small thing and a large one. Whether you choose to weld hope to hubris or put distance between build and bureaucracy, someone will be comforted and someone will be furious."
    "Rita: (quiet, urgent) 'We need to call the list—elderly, single parents, those on the lower ground. If this becomes a surge, we must move them inland with plans and a route.'"
    "Elias Jun: (hands clenched) 'And leave the rest to the sea? We can't let the town be taken because someone is afraid of paperwork.'"
    "Maya Reyes: (internal) You can see both sides: Elias' hands that have rebuilt broken hulls, Rita's ledger of names and needs, Ayla's cautious maps. Your leadership has braided these strands together, but the braid is unraveling under a wind that cares little for intent."
    "Arlo sits on a collapsed crate, bandage on his arm, fingers tracing the tide-watch on your wrist when he thinks no one is looking. His eyes are bright and frightened. In them, you see a future you're trying to buy with time—time that might not be on your side."
    "Arlo: (soft) 'You think it'll hold, Maya? The nets? The seedlings?'"
    "Maya Reyes: (answering aloud and to yourself) 'I don't know.'"
    "Saying it aloud makes the admission heavier than a report ever could. The sky above the harbor grows a shade darker; storm clouds rearrange themselves into something with intent. Lanterns whip faster. Someone on the edge"
    "of the docks shouts an updated advisory: projected surge in four hours instead of six."
    "Your breath fogs. Your hands shake and the tide-watch against your wrist is suddenly too loud."
    "Elias Jun: (leaning in as if to close a wound with his voice) 'Either we fight to keep what we have tonight, or we hand the town over to bureaucracy and chance. I need you with me.'"
    "Rita: (meeting your eyes) 'I need you to keep people safe. If that means stopping construction and moving folks inland—do it. I won't forgive you if something happens because we were proud.'"
    "Dr. Ayla Voss: (on the line, voice like a scalpel) 'Maya. For the sake of lives and funding, consider a controlled pause and partial evacuation. We can secure the necessary emergency permits faster with your cooperation.'"
    "The options sit before you like rough stones on a doorstep. Your chest feels hollow and full at once—the kind of bottom that carries only the weight of decision and consequence."
    # play sound "sfx_placeholder"  # [Sound: A low, sustained thunder; the wind's frequency raises to a keening]
    # play music "music_placeholder"  # [Music: Single violin note, held, then a slow descent]
    "This is the moral bottom you feared: the night when ideals, friendships, policy, and weather test the fibers of your resolve. You have been carrying the town on a ledger of hope and scaffolding. Now the ledger trembles."
    "You look at the faces around you—Elias Jun with his stubborn hands, Rita with her ledger of names, Arlo with a new knot of fear, Ayla steady and unreadable in tone but present—and you feel the world narrow to a single question of leadership."
    hide maya_reyes

    scene bg ch5_4001e7_5 at full_bg

    menu:
        "Stay and reinforce the community barriers with Elias.":
            jump chapter6
        "Pause construction; call for an emergency permit and coordinate with Ayla for a partial evacuation.":
            jump chapter14
        "Prioritize evacuating the most vulnerable and withdraw to secure communication with regional agencies.":
            jump chapter16
    return
