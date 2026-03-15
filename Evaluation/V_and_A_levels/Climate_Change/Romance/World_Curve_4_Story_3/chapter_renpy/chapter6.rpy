label chapter6:

    # [Scene: Marabel Promenade | Late Afternoon — Ceremony]

    scene bg ch6_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Fast-paced, celebratory strings with a driving percussion undercurrent]
    # play sound "sfx_placeholder"  # [Sound: Waves tapping against pilings, cheers, a gull's cry slicing through applause]
    # play sound "sfx_placeholder"  # [Sound: Subtle hum — sensors under the boardwalk, almost like a held breath]
    "You stand at the edge of everything you’ve been carrying for months: models frayed with annotations, volunteer lists written in Marta’s looping hand, the brass compass warm against your palm. Around you, people press closer —"
    "neighbors with salt-streaked hair, Eli with sawdust in his beard, kids with sticky fingers — and the crowd’s energy scratches at your ribs like static."
    "Mayor Rosa steps forward, her scarf a bright memory against the gray. Up close you see the small flecks of paint on her knuckles, the tiredness behind her smile that somehow makes this moment sharper, truer."
    show mayor_rosa_alvarez at left:
        zoom 0.7

    mayor_rosa_alvarez "We watched this town knit itself back together. Not from the top down — from the boards up. Asha, everyone here put sweat into these pilings. You put your head and hands where it hurt the most."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "We all did. None of this is mine."
    "Mayor Rosa hesitates, then produces a small ribbon — a loop of blue and green braided with a scrap of fishing line. The motion is modest, ritual without trumpets."
    hide mayor_rosa_alvarez
    hide asha_moreno

    scene bg ch6_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A round of quiet, earnest applause. The hum under the boardwalk seems to answer in pitch.]
    show mayor_rosa_alvarez at left:
        zoom 0.7

    mayor_rosa_alvarez "Pin it. So people remember who kept the town when everything wanted to sell it."
    "You feel something like a sun cracking open inside your chest: relief, pride, a raw new tenderness. Your hands go instinctively to the ribbon, to smooth it, to make it sit straight."

    menu:
        "Stand proud, and let the applause wash over you":
            "You lift your chin and let the cheering hit your face — flushed, hot, sure. For a breath you are only gratitude."
        "Fold the ribbon into your pocket discreetly":
            "You tuck the ribbon into your jacket under your ledger, secret and close. The sound of the crowd blurs; your pleasure is private."
        "Hand the ribbon to Eli with a joke":
            "You offer the ribbon to Eli, who grins and pins it to his hat with exaggerated solemnity. The crowd laughs and the moment lightens into something like family."

    # --- merge ---
    "Continue to the main narrative."
    "The sensors under the boards pulse quietly, a new rhythm threaded into the wooden heart of the promenade. Noah stands at your side, his hand brushing against yours once, twice—small, deliberate. You feel the contact like a tether."
    show noah_reyes at right:
        zoom 0.7

    noah_reyes "You did it. Look at them — look at what we made."

    "You" "It still trembles. The data feed only tells part of the story."

    noah_reyes "That's the part we can fix. The rest we protect."

    mayor_rosa_alvarez "And Lila? She sent someone to watch. Said she wanted to see the first feed."
    "You glance across the water. Lila Park is there, framed by glass and LEDs, a silhouette with steel-gray eyes that study like lenses. For a moment her expression is unreadable; then she inclines her head once — a curt nod that could mean respect. Could mean calculation. Could mean both."
    hide mayor_rosa_alvarez
    hide noah_reyes

    scene bg ch6_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A camera shutter — someone from the consortium documenting the moment]
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "When the first read comes through, it's going to be messy and beautiful. Trust me. We've rehearsed this — with sensors and with people."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "I've rehearsed a hundred contingencies."

    noah_reyes "Then don't start now."
    "He squeezes your hand. The pressure is brief but elective — a clear line: stay."
    # [Scene: Tidewatch Lab | Simultaneous — Data Feed]
    hide noah_reyes
    hide asha_moreno

    scene bg ch6_601bcb_4 at full_bg
    # play music "music_placeholder"  # [Music: Percussion intensifies; electronic pulses sync to the sensor hum]
    # play sound "sfx_placeholder"  # [Sound: Keyboard taps, low voices mixing with the increasing beeps of equipment]
    "You move through the lab with your ledger under your arm. The first data feed arrives like a dropped stone — a single vertical spike of numbers, then a waterfall of pictorial tide-lines. The feed overlays"
    "your models. For a breath, they match. Tides lie where you predicted, marsh restoration gains ground where you told it to. The room exhales; someone cries out, half laughter, half sob."

    "Volunteer" "Look—look! The models line up!"
    show asha_moreno at left:
        zoom 0.7

    asha_moreno "This is what we asked for: transparency, access, and the ability to change course when the system tells us to."
    show mayor_rosa_alvarez at right:
        zoom 0.7

    mayor_rosa_alvarez "And the clause—"
    "You already know the thing waiting on your tablet: the ledger open, small print crawling like barnacles. You scroll without wanting to, because the work of saving the town has always been folded with caveats."
    hide asha_moreno
    hide mayor_rosa_alvarez

    scene bg ch6_601bcb_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hum becomes an urgent tremor in your chest — rapid, like fingers drumming under the table.]
    "You read the clause again, feeling the room tilt: future liabilities, insurance phrasing, and a condition you missed in the back-and-forth with Beacon lawyers. It is small. It is quiet. It is a door you didn't close."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "What is it?"
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Paperwork is thrilling."

    noah_reyes "Show me."
    "You hand him the tablet. He reads faster than you. His brows knit — but the knit is not panic. It's a calculation."

    noah_reyes "We can renegotiate. We can build in overrides, emergency community vetoes. If we present—"

    asha_moreno "We already did some of that. But this wording... it's a foot in the water."

    noah_reyes "Then we keep our hands on the rope. We keep watching the readouts. We keep the governance board active. We make it harder for anyone to use that clause."

    asha_moreno "That's what we'll do. We'll stay on it. I won't let that be a hidden path."

    menu:
        "Ask Marta to draft community veto language immediately":
            "You call Marta over; she grins and says, 'Oh, we'll make it fierce.' Her fingers fly over a tablet and the crowd murmurs approval."
        "Tell Noah to set a meeting with the Mayor and Beacon counsel tonight":
            "Noah nods, pulling up his calendar with practiced ease. His eyes are fierce — you trust him with the fight."
        "Breathe, seal the file for now, and focus on the celebration":
            "You hide the tablet beneath maps and let the jubilation continue. For one bright hour, you let hope win the room."

    # --- merge ---
    "Continue to the main narrative."
    "The room's energy spikes again as the first public interface displays an animated tide-line that rolls and fizzles across the projection. Children press their faces to the glass as if the map were a magic pool."
    "Someone chants. Eli hoists a plank aloft with a flourish. You laugh until your jaw aches."
    "Lila Park's team walks through the periphery, technicians nodding at your volunteers. She catches your eye across the lab and, for once, the sizing looks softer. She raises a hand. The small gesture carries a monstrous volume: a concession, a truce, or a tactical peace."
    show lila_park at center:
        zoom 0.7

    lila_park "Well done. Your sensors are clean and your marsh plantings executed beautifully."

    asha_moreno "Your data helped. We made them ours."

    lila_park "That was the point, yes. Keep that vigilance. It's the only way these systems will actually serve people."

    asha_moreno "I'll take the advice and the responsibility."

    lila_park "Good. We'll see how the system holds when the real test comes."
    "Her words fall like a charge. The lab hums louder."
    # [Scene: Promenade Boardwalk | Dusk — The Ceremony Winds Down]
    hide noah_reyes
    hide asha_moreno
    hide lila_park

    scene bg ch6_601bcb_6 at full_bg
    # play music "music_placeholder"  # [Music: Choir-like brass lifts, then a driving drumbeat; the tempo accelerates]
    # play sound "sfx_placeholder"  # [Sound: The community's laughter, overlapping conversations; the sensors' hum threaded through it all]
    "You walk the boardwalk with Noah at your shoulder. Hands find each other easily now — a taut, comfortable fit. You taste the salt in the air like a promise and a warning."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "Stay?"
    "You feel the question like a pulse against your palm: not only stay in town, but stay in the together-ness this work has demanded."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "I already am. I'm not going anywhere."

    noah_reyes "Good. Me neither."
    "They are simple words. They land heavy and bright. Behind them, the ledger sits on your tablet and the clause waits like a minor animal in the grass. Joy and caution braid themselves into your ribs."
    # [Scene: The Old Boatyard | Night]
    hide noah_reyes
    hide asha_moreno

    scene bg ch6_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: Sparse guitar picks, heartbeat drums rising into a crescendo]
    # play sound "sfx_placeholder"  # [Sound: The creak of a bench, a distant lone dog, Noah's breath and the soft scuff of boots]
    "Noah leads you between half-repaired boats. The air is warm from the day’s work, flecked with resin and coffee. He wipes his hands on his trousers; sawdust clings to his sleeve. He works with hands that"
    "remember the sea the way older maps remember coasts — with a tenderness you want to trace."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "I always liked this place. The boatyard smells like the past, but you make it feel like the future too."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "It's the work. The town gives us something to anchor to."
    "Noah pauses, then reaches for your hand without make-believe. Sawdust presses into your palm. His fingers curl around yours like a clamp."

    noah_reyes "Do you think this can last?"

    asha_moreno "We made a thousand small things line up today. Sensors, plantings, governance. Maybe that's how you make something last — a litany of small, stubborn acts."

    noah_reyes "I want to stake my future here. With you."

    asha_moreno "Noah—"
    "He squeezes, and the world narrows. The sound of the town becomes a swell behind a curtain; the future is both a map and a question mark. You think of your father’s boat, of classrooms, of"
    "nights in labs, of every meeting that ended with a list rather than a resolution. You lean into him."

    menu:
        "Say 'yes' to staying right now":
            "You close your fingers around his and say it — immediate, fierce. It feels like dropping an anchor and also like setting sail."
        "Say 'we'll try, but there are conditions'":
            "You outline the conditions — governance boards, transparency, checks. He listens, nodding, taking each term with the gravity of someone accepting vows."
        "Stay silent and let the moment breathe":
            "You simply rest your head against his shoulder. Words would break the spell; the silence holds the promise."

    # --- merge ---
    "Continue to the main narrative."
    "He laughs low, a sound of urgent relief. For a heartbeat, the town is small enough to cradle between your palms."

    noah_reyes "Whatever storms come, we won't face them alone."

    asha_moreno "We'll fight, and we’ll build, and we'll make it harder for anyone to take what we've made."
    "You hold him and for a sliver of time the weight of everything — models, meetings, the Beacon's halo — lifts. The boardwalk feels repaired by hands and policy and stubborn, human patience."
    hide noah_reyes
    hide asha_moreno

    scene bg ch6_601bcb_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The sensor hum under the promenade steady, a bassnote that seems to sync with your pulse. Night insects pick their tiny rhythms.]
    "You pull your tablet from your jacket to double-check the governance notes one more time. Something small, almost tender, keeps you from letting go of the ledger. You scroll back to the clause. The words you thought you understood still sit there, legal and inevitable."
    "You feel the brine on your tongue, jubilation and a tight knot of fear braided together. The joy of the night tastes of salt and of watchfulness. That is the dual current you have learned to live in."
    "Then, almost too quiet to be more than a whisper, the lab feed on your tablet blips. A new message threads across the screen — an automated ping you set to alert you when thresholds shift. The hum under the boards thrums a little faster."
    # play sound "sfx_placeholder"  # [Sound: A single high-pitched notification; then, distant, the wind picks up one notch]
    # play music "music_placeholder"  # [Music: A string cut — then a sudden surge of drums, building toward the next movement]
    "Your heart lurches — not from panic, yet. From attention. From the fierce, electric sense that a trial has begun. All the celebration folds into a new shape: purpose sharpened by an incoming test."
    "You hold Noah tighter. He looks at you with the same mixture of hope and readiness."
    "You know, without needing anyone to say it, that tonight is not the end. It is the first big thing that might actually be called a beginning: the sensors are live, the marshes planted, the governance established — and the sea is already moving."
    "Page-turning thought: The feed that made you believe holds a promise — and a condition. Whatever comes next will test whether your stitched-together solutions can weather the water. You breathe the cold air hard, taste the"
    "salt and the electric tang of a coming tide, and step forward with your hand in Noah's."

    scene bg ch6_601bcb_9 at full_bg
    # play music "music_placeholder"  # [Music: Crescendo — then a held single note that demands continuation]
    # play sound "sfx_placeholder"  # [Sound: The sensor hum resolves into a rising, insistent tone]

    scene bg ch6_601bcb_10 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter8
    return
