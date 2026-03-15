label chapter6:

    # [Scene: Pilot Sea-wall | Morning]

    scene bg ch6_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Steady, hopeful piano motif with gentle strings rising]
    # play sound "sfx_placeholder"  # [Sound: The dull thump of pile drivers, distant engine hum, occasional shouted instructions]
    "You stand beneath a sky the color of wet pewter, wind threading salt through your hair until it presses flat against the back of your neck. The beanie you always keep for late mornings is long"
    "gone; your chestnut waves are damp at the tips. Your notebook is zipped in your pack for now — the sketches, the x’s where you once marked a failing inlet, tucked away like a promise."
    "Before you, the pilot hybrid takes shape: scalloped concrete ribs set like the teeth of some careful machine, marsh plantings anchored in wet pockets just behind them, and sluice gates engineered to breathe with the tide."
    "The whole thing smells of sea-sediment and fresh concrete, of cut reeds and diesel. Mud clings to your boots with patient insistence; each step leaves an impression that the water will eventually rewrite."
    show elias_hart at left:
        zoom 0.7

    elias_hart "We set the final sluice plates at thirty degrees. Watch the second surge window — we'll need the gates to flex."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "Thirty degrees, and let the reed pockets get the full backflow. I don't want scouring in the nursery channel."

    elias_hart "Agreed. Kenji's salinity gradient tests back that up. We'll monitor and adjust during the next tide."
    "He doesn't look like the outsider you once braced against; today, the slate of his coat is streaked with a thin film of spray, and the drafting pencil behind his ear has a smudge of concrete"
    "dust that mirrors the smudges on your jacket. Your agreement is practical and warm. It feels like work, and like truce."
    # play sound "sfx_placeholder"  # [Sound: A deeper thump in the distance; a winch groans as a concrete segment settles]
    hide elias_hart
    hide amina_reyes

    scene bg ch6_601bcb_2 at full_bg
    show niko_kaur at left:
        zoom 0.7

    niko_kaur "We're securing the nursery channel for your marsh grasses, Reyes. Don't let the bureaucrats shove the machines without us — you know that."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "You won't be shunted, Niko. You told me you wanted work that means something. This is that work."

    niko_kaur "Don't make me swallow 'something' and get sentimental about it."
    "You both laugh, and the sound is small against the machinery, but it lands like a stone in the water — ripples crossing to meet each other."

    menu:
        "Check the new sluice seal by hand":
            "You pad down the ladder and crouch at the edge, fingers finding the rubber flange. It smells of salt and new rubber; the seal flexes the exact way Kenji predicted. The relief is a quiet, steady thing in your ribs."
        "Stay with Elias to watch the first alignment":
            "You stay on the platform and watch Elias orchestrate the placement like a conductor. His calm steadies you; you swap measuring glances more than words and, for a moment, the work feels like a conversation you can both hold."

    # --- merge ---
    "Continue to the next narration."
    hide niko_kaur
    hide amina_reyes

    scene bg ch6_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Tide sliding through channels; metal on metal settling; a distant gull's cry muffled by cloud]
    show dr_kenji_sato at left:
        zoom 0.7

    dr_kenji_sato "The salinity probe just registered the first dampened rebound in the nursery inlet. It's within the range we modeled three months ago — but to see it in real time... Amina, look."
    "You lean in. His tablet shows a jagged line, then a softer, breathing oscillation. Data, till now abstract, becomes the story of water choosing a different path."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "That's exactly what we wanted. The grasses will reestablish faster if the backflow's gentle."

    dr_kenji_sato "You designed the tidal draft better than I dared. The models are happy."
    show elias_hart at center:
        zoom 0.7

    elias_hart "Happy models, happier people.' (He offers you a hand that smells faintly of diesel and sea—callused, sure.) 'How about lunch after this? I owe you coffee for making me listen."
    "You hesitate, the old reflex to weigh politics before pleasure flaring, then take his hand. The contact is warm and deliberate. There's still complexity — trust rebuilt, not assumed — but the small offering speaks in the language of work made together."
    # [Scene: Pilot Sea-wall | Afternoon — Storm Looming]
    hide dr_kenji_sato
    hide amina_reyes
    hide elias_hart

    scene bg ch6_601bcb_4 at full_bg
    # play music "music_placeholder"  # [Music: Strings swell with a cautious, ascending motif]
    # play sound "sfx_placeholder"  # [Sound: Wind picking up; a sudden sharp snap of a line being cinched; the sea beginning to bruise]

    "Someone radios from the edge of the project" "Storm front's moving in faster. All nonessential personnel clear to shelter."
    show amina_reyes at left:
        zoom 0.7

    amina_reyes "Kenji, readings?"
    show dr_kenji_sato at right:
        zoom 0.7

    dr_kenji_sato "Barometric drop is steeper than forecast — but the pilings are seating. If the gate alignment holds through the surge, we get a full test."
    "Niko appears at your side as if out of the fog. His hair is streaked, braid flapping. Mud on his boots finds your own as your shoulders brush."
    show niko_kaur at center:
        zoom 0.7

    niko_kaur "If this thing fails, it'll tear up the nursery worse than the last time. You sure about the placement?"

    amina_reyes "Every measure says yes. We built it so the breakwater takes the first hammer and the sluices protect the shallow channels. You told me your crew could shore the nursery — and they did."

    niko_kaur "We did. And we didn't do it for anyone to make a monument out of our grief."

    amina_reyes "We're not playing at monuments. This is repair."

    "Niko studies your face, and for a second the sea and the shout of wind seem to fall away. Their voice is small" "Then hold them to it."

    menu:
        "Wade into the inlet to inspect the nursery channel":
            "You step into the salt-sour water, boots sucking against the mud. Rain hammers your jacket, but the sight of the plankwork — Niko's crew's careful lashings — is steadiness made visible. The nursery holds, young eelgrass cowering but present; your chest unclenches."
        "Stand on the high boardwalk and coordinate from there":
            "You stay on the boardwalk and shout directions. From above you can see the wider pulse of the tide and the work of the breakwater as it breathes; giving orders feels less romantic but more effective, and you realize leadership is sometimes this: being the eye while hands do the work."

    # --- merge ---
    "Continue to the next narration."
    # play sound "sfx_placeholder"  # [Sound: A long, resonant crash as a wave pounds the promenade; the wooden planks groan but do not surrender]
    hide amina_reyes
    hide dr_kenji_sato
    hide niko_kaur

    scene bg ch6_601bcb_5 at full_bg
    "Time narrows to a handful of motions: levers pulled, a shout that is half-technical command and half-relief. The first true wall of water comes at the promenade like a living thing. It slams against the breakwater"
    "and — heart like a fist in your throat — the structure holds. Water curls and is sent into the sluices instead of plowing straight into the boardwalk. The nursery channel bulks and drinks the pulse;"
    "young fish you once marked with an X in your notebook dart into shallow refuges as if remembering how."
    "A wave retreats, and the sound left behind is a long, collective breath exhaled by every person whose hands have been on this."
    # [Scene: Old Boardwalk | After the Storm — Early Evening]

    scene bg ch6_601bcb_6 at full_bg
    # play music "music_placeholder"  # [Music: Warm strings, acoustic guitar picking a hopeful countermelody]
    # play sound "sfx_placeholder"  # [Sound: Laughter in low waves; the pop of a grill; distant tools being wiped and set aside]
    show mayor_lucia_varela at left:
        zoom 0.7

    mayor_lucia_varela "Folks, whatever else you think of me — and believe me, I live with the consequences of your looks — I see what you've built. The matched funding starts moving to council tomorrow. We'll scale this. Thank you all."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "Mayor — this is because everyone showed up. This was always meant to be co-managed."

    mayor_lucia_varela "You were the spine for that. Take the credit and make us live up to it."
    show dr_kenji_sato at center:
        zoom 0.7

    dr_kenji_sato "Preliminary data will be uploaded tonight. The breach events were significantly attenuated, and the salinity fluctuation stayed within the new, healthier band. I get to use words like 'resilience' without feeling like I'm lying."

    amina_reyes "Send me the raw set. I want to see the eelgrass survival curve."

    dr_kenji_sato "Already on it."
    "Elias Hart comes up, rain cooling on his collar but his smile open. He sets a hand at the small of your back for a beat — not possessive, but companionable."
    hide mayor_lucia_varela
    show elias_hart at left:
        zoom 0.7

    elias_hart "You did a thing here that matters. I stayed because I believed you could make it something more than a textbook solution."

    amina_reyes "You could have left when the funding caveats showed up."

    elias_hart "And missed your stubbornness proving right? Never."
    "The conversation goes on — laughter, ribbing, earnest planning — but underneath it there's the easy warmth that blossoms from shared work. Niko joins you at the fire with their hands still stained the same brown"
    "as yours; you exchange stories about the worst rebuild and the smallest triumph. Your fingers are tarred and salted, like a map of efforts."
    hide amina_reyes
    show niko_kaur at right:
        zoom 0.7

    niko_kaur "For the stubborn woman who wouldn't let a machine speak for a town."
    "You take it, the smoke and salt and citrus tang filling your mouth. It tastes of everything that's been at stake."

    menu:
        "Sit with Niko and trade boat-mending stories":
            "You sit close to the fire; the wood-smoke threads through your hair as Niko describes the time they rebuilt a hull in a storm. Your hands find the same rhythm — you realize you both measure loss by the way you repair it. The night becomes a stitch where you are threaded together."
        "Walk the boardwalk with Elias, plan the next technical report":
            "You walk alongside Elias. The conversation turns to timelines, to data portals and community workshops. It's practical, intimate in its own way; you sense a future where policy and place meet without losing their edges."

    # --- merge ---
    "Continue to the next narration."
    hide dr_kenji_sato
    hide elias_hart
    hide niko_kaur

    scene bg ch6_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: Piano returns, soft and content]
    # play sound "sfx_placeholder"  # [Sound: The sea's far susurrus; voices softened into comfortable murmurs]
    "Later, under the rooftop garden's windbreak panels, the town is smaller and yet larger than it was. Plans are pinned to boards, and a map bears new lines — not erasures but additions. There's laughter over"
    "a table where Marina organizes volunteers, and Kenji pores over charts, filing tonight's data with a delighted grin that hasn't left his face all evening."
    "You stand with Niko as darkness pools. The salt is on your lips; your hands smell faintly of fish smoke and mud and the oils you've rubbed into wood. In the long, private space of the night, Niko reaches for your hand and doesn't let it go."
    show niko_kaur at left:
        zoom 0.7

    niko_kaur "Did you ever think we'd get this far?"
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "I thought we'd try. I didn't know we'd find the town half-repaired in the act."

    niko_kaur "That's the honest way to do it. No grand finishes. Just sweat and stubbornness."
    "You lean your head against their shoulder for a moment — the sound of the harbor like a lullaby turned practical — and feel something like home mend. It's not perfect. There are legal forms to"
    "fill and more shoreline to steward and enough politics to make a saint sigh. But tonight the work stitches the town, and your stitches hold."
    "Elias's collaboration continues in the days that follow: grant paperwork with local co-management clauses, engineers learning how to read a reed bed, and his steady presence at community workshops shifting from presenter to partner. He brings"
    "funding and learns how to listen; you bring place and insist on being heard. The compromise is not a capitulation but a shape you both learned to hold."
    # [Scene: Niko's Boatyard | Evening — A Few Weeks Later]
    hide niko_kaur
    hide amina_reyes

    scene bg ch6_601bcb_8 at full_bg
    # play music "music_placeholder"  # [Music: Warm acoustic guitar; light percussion]
    # play sound "sfx_placeholder"  # [Sound: Sawing, low conversation, the cadence of restored labor]
    "Fishermen celebrate with a modest feast on the boardwalk — smoked fish, shared bread, and stories that start full of bravado and end in tenderness. Mayor Lucia speaks quietly about scaling the pilot, Kenji speaks in"
    "delighted, technical asides, and you find yourself answering questions about monitoring protocols, about how to keep the work community-led as it grows."
    show amina_reyes at left:
        zoom 0.7

    amina_reyes "If you partner with the boatwrights and schedule monitoring trainings, we'll keep the co-management language alive. The pilot showed we can do this at scale if the town stays at the center."
    show mayor_lucia_varela at right:
        zoom 0.7

    mayor_lucia_varela "Then let's put it in the ordinance."
    show dr_kenji_sato at center:
        zoom 0.7

    dr_kenji_sato "To ordinances that don't smell like death."
    "A round of laughter. Your chest feels unburdened. Not empty, but free enough to be generous."
    "That night, you and Niko sit under low string lights, hands stained the same color from oil and earth, sharing wood-smoke and stories that travel back to childhood’s reckless repairs and forward to plans for shared"
    "boat maintenance days. Love here is less a lightning flash and more a steady returning tide — patient, salvaged, warm."
    "Elias remains in town as a collaborator, not a conqueror. He shows up at the workshops with coffee, and sometimes with data charts turned into plain language. You watch him learning to love the mess of"
    "community meetings as a worthwhile tool rather than an obstacle. There is a closeness with him that has ease and respect, the kind that grows when two people keep showing up to the same work."
    hide amina_reyes
    hide mayor_lucia_varela
    hide dr_kenji_sato

    scene bg ch6_601bcb_9 at full_bg
    # play music "music_placeholder"  # [Music: Piano and strings gently resolve into a soft major chord]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the low murmur of a town breathing easy]
    "You think of your brother — the ache is still there, a quiet geography you carry — and you place that ache alongside this new thing: a living shore that gives back, the pulse of a"
    "town that decided to repair rather than abandon, hands stained the same color, shared meals and shared plans. It is not a clean healing, but it is honest. You let yourself feel a small, steady hope."

    scene bg ch6_601bcb_10 at full_bg
    # play music "music_placeholder"  # [Music: Swell and gentle fade]
    "You stand on the boardwalk, wind picking at your hair, and watch children chase gulls in shallow pools near the new inlet — fish darting, reeds trembling. Mayor Lucia's voice reaches you across the boards as"
    "she talks to a neighbor about ordinance language; Kenji's laugh is a bright, infuriating sound you are grateful for. Niko catches your eye and lifts a piece of smoked fish in mock salute. Elias lifts a"
    "thermos and winks."
    "You inhale salt and smoke and mud and the last light of the day. The town is a long, imperfect work in motion — but tonight it is also mended in the places that matter most: livelihood, memory, and the stubborn, patient thing that is love made by doing."

    scene bg ch6_601bcb_11 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    scene bg ch6_601bcb_12 at full_bg
    "THE END"
    # [GAME END]
    return
