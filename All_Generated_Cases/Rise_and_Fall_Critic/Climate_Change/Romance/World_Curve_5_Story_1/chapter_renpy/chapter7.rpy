label chapter7:

    # [Scene: Boardwalk | Morning]

    scene bg ch7_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Bright acoustic guitar with brushed percussion; communal hum underpins dialogue.]
    # play sound "sfx_placeholder"  # [Sound: Distant harmonica call, the shuffle of feet, murmured instructions, the snap of a tarpaulin in a light breeze.]
    "You chose the streets."
    "The decision from City Hall still sits in your chest like a keyed hinge: no committee room, no sterile diagrams — just the town, elbow-to-elbow, and the work under your nails. The harmonica's small, clarion note"
    "cuts through the morning fog; Cassian Rhys moves through that note like it's his current, drawing people toward him. His jacket is a walking manifesto — paint-splotched denim catching the light — and he greets each"
    "volunteer as if they are both old friends and the last needed recruit."
    show cassian_rhys at left:
        zoom 0.7

    cassian_rhys "Alright! Teach-ins at ten, berm brigade at eleven. Bring gloves, bring your questions, and bring something to string up those lanterns tonight — Nadia's class is on lantern duty."
    "Cassian Rhys's voice is loose and lilting, threaded with a grin that makes a dozen people laugh and step closer. He hands you a coil of twine with a theatrical bow, then catches his own smile as if surprised by it."
    "You fold your hands around the twine and feel the steady thrum of the morning — gulls, footsteps, someone hammering a temporary sign. The tarped canopy you've borrowed from the Tidelab hovers like a warm belly,"
    "and beneath it there are tables of sensor kits, laminated charts, and jars of spare screws. Asha is already there, hair pulled back, tapping numbers into a tablet with the focused serenity of someone smoothing wrinkles"
    "from a map."
    show asha_mehta at right:
        zoom 0.7

    asha_mehta "Your tide models from last night — I looped them with the growth projections. Incremental gains, Mira. The curves look... I don't know, like they want to be optimists."
    show mira_kestrel at center:
        zoom 0.7

    mira_kestrel "Show me."
    "Asha pauses, slides the tablet, and the screen blooms with Asha's tidy graphs and color-coded confidence bands. Your finger traces a line where marsh planting could shift inundation patterns in spring months."
    "Internal monologue: The numbers on the screen are not magic, only work. They carry the same steady pulse you felt in the greenhouse. Work that scales, one plot, one volunteer, one child's sticky thumb at a sensor display."
    hide cassian_rhys
    hide asha_mehta
    hide mira_kestrel

    scene bg ch7_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A child's delighted gasp; a volunteer explaining the sensor's blinking LED.]
    "You clear your throat and move into the canopy. Your voice steadies; it has to. The crowd leans in because what you speak of matters — not just to policy, but to the boy whose sneakers"
    "are scuffed from running between mounds and to the older woman who remembers when the orchard had dry roots."
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "This sensor here tells us how quickly water pools after a high tide. If we know that, we can target our plantings to where they slow the flow. It's small-scale work, but it reduces the stress on berms and on people who wake to water in their basements."

    "Volunteer" "Can kids help?"
    "You smile. Of course they can. You hand a small, plastic-wrapped sensor to a girl with braids and explain how to place it. Her fingers are careful and bright with curiosity."

    mira_kestrel "Press the green to wake it. Lay it flat near the root ball, not on top of the soil. And tell me if it blinks red. Red is the sensor's way of saying 'hey, pay attention here.'"
    "The teach-in ripples into hands-on moments: you guide, you correct, you laugh when someone misreads a chart, and you fold complicated ideas into the ordinary language of neighbors. Cassian Rhys sets up an old speaker and"
    "plays a rhythm, then steps down to explain the block party rules — how this is both celebration and civic action."
    show cassian_rhys at right:
        zoom 0.7

    cassian_rhys "We talk, we plant, we sing if we want, and we make sure everyone's concerns are heard. This isn't just aesthetics — it's a political act in seafaring clothes."
    "A murmur of agreement, a few whoops. A local reporter jots notes, the camera focusing on volunteers with floral-taped boots lifting sandbags. The press has started to sniff the story: ingenuity instead of contracts, neighborhood skill instead of tendered bids."

    menu:
        "Demonstrate the sensor live for everyone":
            "You decide to run the live demo. The crowd presses forward as you plug a sensor into the handheld reader. It chirps and the numbers appear — humidity, salinity, a small arc of tide timing. Asha leans in, whispering an extra context point; a parent's worried face eases into something like trust as they hear the data in plain terms."
        "Keep the session intimate and do small group demos":
            "You split the crowd into smaller circles. The conversation deepens; teenagers who were quiet ask sharp, tactical questions about seedlings and labor hours. Cassian Rhys high-fives you later for choosing connection over spectacle. The reporter lingers, listening longer than she would have at the big demo, taking notes on specific volunteers' stories."

    # --- merge ---
    "'Whatever the demo shape you choose, the energy stays: hands in soil, mouths filled with song, the cooperative tremor of a community learning to be its own first responder.'"
    hide mira_kestrel
    hide cassian_rhys

    scene bg ch7_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: Soft choir undercurrent; trumpet of optimism.]
    "Across town, the Drowned Orchard becomes that night's altar: children string knitted lanterns between leaning trunks while elders string instructions into the same twine. Ruben arrives late, cane tapping in time with the work, his face lighter than when you saw him in the planning room."
    show ruben_ortega at left:
        zoom 0.7

    ruben_ortega "You remember when we could pick apples without thinking of water in the trunk? No. But we can make this place ours, again, in a different way. My hands are old, Mira, but they're steady."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Your stories steady us. That's part of the plan, too."
    "Ruben cracks a grin. He pats your shoulder, hard enough that it startles and steadies you at once."
    hide ruben_ortega
    hide mira_kestrel

    scene bg ch7_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Waves lapping gentle, a chorus of conversations knitting into an easy murmur.]
    "Not all reactions are praise. At noon the town board releases a terse statement: Jonah Hale's team accuses your movement of jeopardizing 'regional investment opportunities' and raises the specter of lost jobs. Their spokesperson's words are clipped, the kind that slide into headlines."

    "Jonah Hale (via reporter)" "We respect civic engagement, but we cannot base long-term resilience on good intentions and anecdotal trials alone. There's a risk to the region's funding if these local actions derail a coordinated plan."
    show mayor_lin_park at left:
        zoom 0.7

    mayor_lin_park "Mira, I know you're doing noble work. But I have people asking about insurance and payroll. Jonah Hale's builds mean contractors, means steady wages. I need to weigh those facts."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Mayor — community labor doesn't oppose jobs. We can work alongside projects, show models, offer training. If we get the data, we can make the hybrid approach attractive — both socially and economically."

    mayor_lin_park "I hope you're right. The last thing I want is to split the town."
    "Internal monologue: Her doubt lands like a stone. You know she's balancing ledgers and constituencies; you also know she wants to keep Lowry Bay whole. That tension is part of the negotiating land you chose when you walked out of the hearing room and into the streets."
    "Cassian Rhys overhears some of the exchange and comes up behind you, paint smudged across his knuckles. He loops an arm through yours without words, the familiarity of it both calming and electric."
    show cassian_rhys at center:
        zoom 0.7

    cassian_rhys "You make a good argument. And if they blink at the numbers, we'll make them see the people who live with the sea."
    "Your exchange lingers, more than a sentence. Cassian Rhys's hand on your arm is light but steady, and it says what his speech often skirts: I'm with you, even when the Mayor seems to float between them."

    menu:
        "Meet Jonah's accusations with a public rebuttal":
            "You step up to the microphone, voice clear. You lay out the data, the schedule, the training plan. Cameras click; neighbors shout affirmations. The rebuttal is sharp and earns a headline framed as 'Grassroots Pushback.' It feels like a small victory — the town hears both science and song."
        "Focus inward on community work instead of public rebuttal":
            "You choose to let the street work speak. You double down on the berms and the orchard, not the op-eds. Volunteers deepen their trust; a local reporter later writes a profile piece that sees the movement's human cost and reward. The Mayor grumbles, Jonah Hale fumes, but the momentum in the neighborhood becomes its own currency."

    # --- merge ---
    "'Even when nerves tighten, the day's small successes stack into something that feels like a crest: TV crews capture a child teaching an adult to place a sensor; a volunteer who joined two days ago now"
    "leads a team tightening a berm line. Asha's model hums softly on your tablet, looping through scenarios that, for once, make sense in the language of the people who will live them.'"
    hide mayor_lin_park
    hide mira_kestrel
    hide cassian_rhys

    scene bg ch7_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Piano lullaby; strings with a gentle rise, hopeful.]
    "You fall asleep with the tablet on your chest. Asha's graphs glow faintly; the last thing you see are the projected incremental gains that promise small, real change. You breathe in peat and salt, and that breath tastes like something practical and holy."
    "Cassian Rhys stays nearby. Earlier, he painted a marsh-grass mural along the boardwalk — long green strokes catching the day's light — and now he's seated across from you, palette drying abandoned at his feet. He hums a tune and the harmonica makes a soft punctuation."
    show cassian_rhys at left:
        zoom 0.7

    cassian_rhys "You okay?"
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Tired. Happy. Anxious—"
    "Cassian Rhys reaches to smooth a stray lock of your sea-green hair away from your face; his knuckles brush your wrist. It's casual and intimate, a conversation in touch."
    "Internal monologue: Your history with Cassian Rhys folds into the gesture — neighborhood summers and paint-splattered afternoons and the kind of small betrayals that taught you both how to be careful — but tonight it is"
    "only the present: his hand warm, his laugh low, the mural's green reflecting in his hazel eyes."

    cassian_rhys "If we keep doing this, someday people will call it a movement and put us in history books. I want to be in those dirty pages with you."

    mira_kestrel "Then we'll write them clean."
    "He laughs; the sound catches in your chest and softens the day’s edges. In that laugh there is no policy paper, only two people who choose each other again and again through muddy work."
    hide cassian_rhys
    hide mira_kestrel

    scene bg ch7_453e40_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The harmonica sighs; a volunteer's distant cheer.]
    "You could lean into the softness. You could let it change the tone of every other decision you're about to make. For now, you let the moment be what it is: a small, fierce tether to another person amid the rising tide."
    "Night settles like a promise and you ride the crest of communal pride, the feeling that what you're doing matters and is being seen. The orchard glows; the murals dry; Asha's model sleeps in your tablet with positive numbers humming like a lullaby."
    "You do not forget the Mayor's doubt or Jonah Hale's accusations. You tuck them behind the warmth of the tarpaulin and the hum of volunteers. The movement gains a face in the press, but more importantly, it gains hands."
    "You think of tomorrow's tasks and the list feels long and doable instead of crushing. There is work to be done — more sensors, more plots, more public conversations — and you wake with a plan that is, for once, buoyant."
    "Internal monologue: Hope is not a single bright idea; it's the slow accumulation of people showing up. Tonight, they showed up. Tonight, the town looked like something that could survive its own questions."

    scene bg ch7_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Swelling hopeful motif; strings and piano in steady ascent.]
    "You stand at the edge of the boardwalk, Cassian Rhys beside you, Ruben with his cane, Nadia with her bright hoodie, Asha checking a tablet, volunteers carrying supplies. The community looks like a line of small lights keeping the dark from swallowing the coast."
    "There is a tension at the edge of this joy — a tremor you can name: the sea does not rest, and neither does the politics that orbit it. But tonight the tremor is less menace than current — something you can ride if you keep paddling together."
    "A song from the harmonica pulls your attention; you watch Cassian Rhys as he finishes a brushstroke and then, without thinking, your fingers find the twine again to hand it off. His hand brushes yours. You both freeze in the same polite, intimate pause that contains a hundred unsaid things."
    "You look at the mural. You look at the town. You look at him."
    "There is work to be done. There are hands to hold while you do it. You breathe, and the breath feels like an agreement."

    scene bg ch7_453e40_8 at full_bg
    "You lean forward, toward the next day, toward the next shovel, toward the next meeting, and the next small convincing of a skeptical mayor or a hesitant neighbor. You carry the taste of salt and paint and shared laughter with you."
    "The pulse of momentum holds: for now, the streets have answered. For now, grassroots agency feels more than enough."
    "You carry all of it as you step into the dark, into sleep, into the feeling that for once — just once — the town and its people might outlast the tides."
    # [Page-Turn: You wake with a rustle and a single, urgent sound from the Drowned Orchard that pulls you upright. The echo of lanterns, the snap of a rope, a sound that makes the air funnel toward the shore. You move before you understand why.]

    scene bg ch7_453e40_9 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter8
    return
