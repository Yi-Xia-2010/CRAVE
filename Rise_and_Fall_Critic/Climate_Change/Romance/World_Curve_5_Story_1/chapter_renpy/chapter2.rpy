label chapter2:

    # [Scene: Tidelab Greenhouse | Morning]

    scene bg ch2_c4ca42_1 at full_bg
    # play music "music_placeholder"  # [Music: Light piano arpeggios, warm and steady; strings swell softly on hopeful notes.]
    # play sound "sfx_placeholder"  # [Sound: Hum of humidifiers, the soft scrape of a crate on a wheeled dolly, distant gull calls through the vents.]
    "You push open the greenhouse door and the warm, humid air wraps around you like an exhale — peat and brine and the sharp, green tang of new leaves. Light from the lamps pools on the"
    "packed soil of the trays; the undersides of the seedlings glow with fragile intention. Your palms still smell faintly of salt and compost from last night's work; flecks of peat cling to the ridges of your"
    "nails."
    "Asha is already inside, knees pressed to the floor, tablet balanced on one thigh. Her glasses are smudged with lab dust and—true to form—so is the corner of her mouth where she smiled while reading a"
    "data stream. She glances up, tucks a stray purple-cropped hair behind her ear, and flashes a grin that makes the whole room feel like an accomplished calculation."
    show asha_mehta at left:
        zoom 0.7

    asha_mehta "You're early. (beat) Or annoyingly punctual, depending on the moral universe."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "Punctual enough to catch you before you start taking over the place."

    asha_mehta "Flow-model's running,' she says, sliding the tablet toward you. The screen pulses with a tangle of currents and projected sediment flows. 'I ran overnight adjustments for the suction effect at low tide. If we angle the plugs when we plant, we reduce displacement by eight percent in the model."
    "You lean in, eyes narrowing as you trace the curves on the screen. The numbers settle into a shape that makes sense in your head — small, cumulative wins."

    mira_kestrel "Eight percent is a measurable thing. I like measurable. Tell me the trade-offs."

    asha_mehta "Less displacement, marginally slower colonization on the exposed face. But if we stagger planting with silt traps the initial loss should be negligible. Volunteers won't like staggered shifts.' She smirks. 'Cassian Rhys will call that boring."
    "You laugh, and at that moment the door opens again and Cassian Rhys slips in, late and loud in the best way. Paint smudges his thumb and the cuff of his denim jacket is peppered with"
    "color; his hair is in a messy bun that somehow looks exactly like the kind of breath that can make anyone's day sunnier."
    show cassian_rhys at center:
        zoom 0.7

    cassian_rhys "You started without me? Tragic.' (He leans against a table and considers the trays like an artist appraising fresh canvas.) 'Okay—mural idea.' He waves a hand and the harmonica in his satchel clinks. 'Hear me out: we paint a map along the boardwalk—each painted glyph is a sensor node. People interact with it. They learn. They care."
    "Mira Kestrel: (You feel the faint warmth of his linen shirt as he brushes past; the closeness is like sun at your neck.) You can't help smiling. 'A public sensor map?' You let the thought settle. He always packages practicality in color."
    "Asha: (eyes on the tablet) 'Public outreach is low-cost, high-engagement. But the map needs to be accurate if you're going to link data to it.'"

    cassian_rhys "We make the map beautiful and accurate. We make it an invitation. Paint and code, together. People will come to touch their neighborhood on the wall."

    mira_kestrel "And if they touch the mural and the sensor's down?"
    "Cassian Rhys: (grinning) 'We teach them why it matters. We let them be part of the fix. Besides, your data needs storytelling — science without story is...well, sad.'"

    asha_mehta "She has a point. And a sad graph doesn't get volunteers.' (She taps the tablet.) 'If you weave the sensor IDs into the mural, we can reduce lookup errors during planting day. Your volunteers are less likely to tape the wrong tags onto the wrong beds."
    "Cassian Rhys: (flourish) 'See? I'm saving your data from ennui.'"

    mira_kestrel "So the mural becomes both outreach and functional signage."
    "Asha's grin softens into something like approval. 'Okay. I can create a printable key that mirrors the mural's palette. We calibrate the tags tonight. Mira Kestrel—' (she uses your given name, casual and steady) '—you lead"
    "planting prep, Cassian Rhys organizes the volunteers and paints. I'll make sure the model accounts for human error.'"

    cassian_rhys "And I'll bribe them with pastries."

    menu:
        "Sketch mural layout with Cassian Rhys":
            "You pull a wooden clipboard from under the table and uncap a marker. Together you sketch sweeping lines that follow the bay's current, laughing as you name boroughs and mark sensor glyphs. Your hand brushes his; it's quick, charged, and entirely allowed here among seedlings and soil. Planning becomes play, and play becomes momentum."
        "Start sensor calibration with Asha":
            "You move to the bench where Asha's instruments lie out like a small constellation. Your fingers find the calibration pad; the work is precise, satisfying. Asha hums as she reads adjustments aloud and you feel the steady clarifying joy of numbers aligning with the world. Cassian Rhys's mural chatter becomes a warm background hum."

    # --- merge ---
    "The moment splits in miniature and you take both elements in, regardless of which hand you reach with: hands in the dirt, hands on the map. Hope accrues like sediment — layer by patient layer."
    "You spend the next hour in a blur of close work. Seeds are coaxed from their trays, tiny roots teased into the peat plugs. You tape identifiers — small color tabs that will match Cassian Rhys's"
    "mural — to the hydroponic bedding, the adhesive cold against your fingers. The wristband at your elbow buzzes once: a low battery warning you ignore because you know where the spare pack is. You thumb through"
    "your leather notebook and scribble Ruben's last anecdote into the margin as qualitative metadata: fishermen's memory = observational baseline."
    "Ruben: (off-screen, then poking his head through the door with his salt-streaked cap) 'Ah, hell, that smell takes me back.' He steps into the amber light and his face creases into a grin like grooves in"
    "old wood. 'Remember last winter? Tide came in like a gray hand. Took half a fence and Mrs. Liao's shed.'"
    "Mira Kestrel: (You set the tape gun down and look at him.) He always arrives with a story threaded with the bay's memory. You reach automatically for your notebook because these stories are scaffolding for the models you and Asha breathe life into."
    hide asha_mehta
    show ruben_ortega at left:
        zoom 0.7

    ruben_ortega "But those marsh grass plugs you raised last season—kept the mud where it oughta be. We didn't get washed down. Folks said they were just weeds, but there was muscle there."
    hide mira_kestrel
    show asha_mehta at right:
        zoom 0.7

    asha_mehta "Your oral histories matter. If we overlay them with sensor readings, we can validate the model at low cost."

    cassian_rhys "And if we paint Ruben's tale on the boardwalk, people will read the story as they stroll. Art meets history meets science.' He nudges Ruben playfully. 'You ready to be immortalized in paint?"
    "Ruben: (chuckles, then grows softer) 'If it helps the kids, I'll play the old man in the mural. Anything. Those kids deserve a town to run around in.'"
    "Mira Kestrel: (The words settle heavy in your chest in a way that is both tender and galvanizing.) Nadia's face—small, freckled, hopeful—flickers through your mind; the school kids running along the boardwalk, the way they pat"
    "gulls and call them by names. Your work is for them, and for everyone else who will inherit whatever patch of Lowry Bay you manage to hold."

    menu:
        "Record Ruben's story in full detail":
            "You set the notebook on your knee and ask him to start from the beginning. His voice loosens into cadence, and you write steady, messy lines: dates, landmarks, the particular smell of seawater during that storm. The recording feels like laying a foundation stone."
        "Ask Ruben about practical planting tips instead":
            "You ask him where the wind cut the worst and which boardwalk posts he thinks we should avoid. Ruben laughs and props himself on his cane, answering in specifics: where to angle the plugs, which paths will hold volunteers. The conversation becomes a mini-masterclass."

    # --- merge ---
    "The greenhouse fills with small, earnest trades — stories for blueprints, paint for data, pastry for hands. Hope, again, is not grand or cinematic; it's the way the group forms a knot around a problem and tightens into a plan."
    "Time passes in sunless, amber increments. Volunteers trickle in as planned: a schoolteacher with a box of granola bars, a retired carpenter with callused palms, a pair of teenagers from the surf club with bright, practical"
    "boots. Cassian Rhys corrals them with exuberant instructions; it looks like organizing a parade, but they're setting up trays and labelling tags. You walk among them, checking tie points and bending to demonstrate the correct planting"
    "angle. Asha monitors a live dashboard that projects a pale map on the greenhouse wall; you watch clusters of volunteer energy map to the model like bees to a hive."
    "Asha: (handing you the tablet) 'Mayor's office pinged me.' Her voice is neutral, but the way she holds the tablet draws your attention. 'They're scheduling a public hearing about the coastal project. City Hall wants community input next week.'"
    "Your chest tightens in a way that is not panic but focused gravity. This is the next, unavoidable step — the public stage where small experiments could either be recognized or drowned out by big promises."
    "You feel the tilt of the town's mood sharper now: the mural, the plugs, the dashboard — all of it is practice for that room."
    "Cassian Rhys: (jaw tightening minutely) 'Next week? That's earlier than we thought.' He runs a hand through his hair and his paint-smeared fingers leave a brief, jaunty streak on his cheek. 'We'll make attendees out of the town. We'll bring evidence, we'll show them the model. We'll have people speak.'"

    asha_mehta "I can pull a preliminary validation packet tonight. Data paired with Ruben's histories and a volunteer plan. It's not the whole thing, but it's compelling."
    "Mira Kestrel: (You look at the greenhouse, at the line of seedlings that promise a shoreline slowly stitched back together. For a beat you imagine the hearing room: fluorescent lights, a long table, faces set like"
    "cliffs. You imagine Jonah Hale in his neat raincoat, folding efficiency into rhetoric; Mayor Lin Park sitting between; the town leaning forward with questions.) The thought is sharp but not paralytic. The morning's work has steadied"
    "you; momentum has weight."
    "You transfer seeds to the staging rack, tape the final identifier tags with hands that know the choreography now. Cassian Rhys clasps your shoulder briefly — a small, conspiratorial pressure — and the warmth of him is steady, plain encouragement."
    hide cassian_rhys
    show mira_kestrel at center:
        zoom 0.7

    mira_kestrel "We show up together."

    asha_mehta "I'll stay late and get the packet ready. Cassian Rhys, marshal the mural people and the volunteers. Mira Kestrel—' (she tilts her head, searching your face) '—you coordinate the planting Sunday and the speaking list."
    "You nod. You think of everything that must be done, and then you catalog it into manageable bites: tonight — validation packet; tomorrow — practice speech with Ruben and two volunteers; Saturday — final mural layout; Sunday — planting."
    "Your notebook fits into your jacket as the hum of the greenhouse drops into the background. The lamp light warms the seedlings one last time before you're all due out into the cooler morning."
    "You breathe in, tasting peat and potential. The day has been a soft accumulation of small victories. The LED on your wristband blinks once, green and resolute."
    "You pick up the crate and wheel it toward the door, the wheels whispering over wet concrete. The boardwalk beyond the greenhouse is thin and bright with salt-reflected light; the town waits, not passive but expectant."
    "For a moment before you step out, your hand lingers on the door frame. You look back at Asha bent over the tablet, at Cassian Rhys already sketching a mural glyph in the condensation on the panel, at Ruben's weathered smile. You carry their confidence like tidewater in your pockets."
    "The next work is public — louder, higher stakes. But here, in the amber hush of Tidelab, you have built something sharable. Hope feels heavier now, more transportable: it will ride you to City Hall."
    hide ruben_ortega
    hide asha_mehta
    hide mira_kestrel

    scene bg ch2_c4ca42_2 at full_bg
    # play music "music_placeholder"  # [Music: Piano motif swells into a brighter chord, resolving on a note of steady ascent.]
    # play sound "sfx_placeholder"  # [Sound: Door closes with a soft, promising click.]
    "You step out."

    scene bg ch2_c4ca42_3 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
