label chapter13:

    # [Scene: Reclamation Works | Morning]

    scene bg ch12_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Heavy diesel, metal on metal, the relentless thrum of pumps; gulls cry from higher wind]
    # play music "music_placeholder"  # [Music: Fast, driving strings — urgent, insistent]
    "You arrive before the official notices have sunk fully into people's routines. The machines have the momentum of certainty: loud, organized, and almost ceremonial. Water that used to braid through the inlet now disappears under dumped fill; reeds collapse and stick in wet concrete like a memory that can't breathe."
    "Your boots sink into churned mud. The air tastes of salt and oil and a kind of finality. You keep your notebook closed against your chest, but you can feel the maps in it folding and"
    "unfolding in your mind — not as plans now, but as a ledger of what happened and what you tried to stop."
    "Lito is already there, dark against the machines, arms folded until his knuckles shine white. When you reach him the noise steals your voice; you don't have to speak to know the shape of his anger."
    show lito_reyes at left:
        zoom 0.7

    lito_reyes "They didn't even bother with the old moorings. Just filled it in like they were covering a stain."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "I know."

    lito_reyes "My boat's gone, May. The post is under cement. Nena's dock—gone. How do you tell a kid that the place where he learned to tie a line is—"

    maya_reyes "You tell him the truth the way we always do: we show him the map and we tell him what the water did, and then we teach him how to read the new lines."

    lito_reyes "You think that helps?' (He gestures at the machines.) 'They say lives were saved. Houses are dry. Investors are smiling. But my cove—"

    maya_reyes "It was never just about cove-lines, Lito. It was about what we can pass on."

    menu:
        "Stay and stand with Lito":
            "You square your shoulders and plant yourself near the edge of the work — a human presence against iron. Neighbors look up, relief flashing in their faces like flares."
        "Run to the boardwalk and warn others":
            "You dart away, boots splashing, pages of your notebook already reorganizing into the next list of people to reach. Voices catch as you call names; urgency turns into a small, bright engine."

    # --- merge ---
    "Continue"
    # [Scene: Marsh | Noon]
    hide lito_reyes
    hide maya_reyes

    scene bg ch12_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Pumping water, the distant bark of orders over radios, and a new, brittle silence where reed-sound used to be]
    # play music "music_placeholder"  # [Music: Brass and percussion — sharp, conflicted]
    "You walk the boardwalk. The places you memorized — the way a specific bend held gulls, the dip where an old buoy leaned — are now punctured by sheets of galvanized steel. The marsh's movement has been domesticated into right angles."
    "Elias Stone is there, sleeves rolled, oil and dust on his hands. He is standing with a site engineer, voice low. When he sees you his face creases; it is the look of someone carrying a compromise like a hot coal."
    show elias_stone at left:
        zoom 0.7

    elias_stone "I wanted to talk to you before today."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "You already spoke to them.' (It isn't entirely accusation, but it is pushed hard enough to be an accusation.) 'You helped draw the plans that carved this out, Eli."
    "Elias Stone: (He breathes.) 'I did work on the models to reduce risk. I argued for living-creek buffers, for phased filling. Some of it didn't make the final cut—money moved faster than the good ideas.'"

    maya_reyes "So which part is the part you'll sleep with?"

    elias_stone "The part where fewer people lost their homes tonight.' (He meets your eyes — there is a pleading, practical warmth there that tries to do the arithmetic of ethics.) 'I stayed so I could be inside the decisions. If I'm on the outside yelling, they ignore the variables I can change."

    maya_reyes "But being inside also makes you complicit."

    elias_stone "Maybe. But leaving would have been simpler for my conscience, not for the city. I thought — I thought I could steer them. I was wrong more often than I was right."
    "Maya Reyes: (You want to tell him about maps stained with grief, about the way you trace old shorelines with your finger like a talisman. Instead you fold your scarf tighter around your throat.) 'We are different kinds of stubborn.' (A small, sad smile touches the corner of your mouth.)"

    elias_stone "We are."
    "You both stand in the dust and the machine-thrum, two small human rhythms attempting to sync. A wave of sound from a siren cuts across the worksite; a worker shouts an order. Everything feels more urgent than it did when you first planned to confront Duval."

    menu:
        "Reach for Elias' hand":
            "Your fingers find his; for a moment the boardwalk is a private island. He squeezes back with an apology you don't need him to make."
        "Keep your distance and keep working":
            "You pull your hand back and return to the map in your head — names, legal contacts, people who still need help resettling. The connection becomes a quiet ache in your chest."

    # --- merge ---
    "Continue"
    # [Scene: Boardwalk | Afternoon]
    hide elias_stone
    hide maya_reyes

    scene bg ch12_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Public speakers, overlapping interviews, the rattle of camera shutters]
    # play music "music_placeholder"  # [Music: Choir-like strings swell under a modern beat — grand, unsettling]

    "Camille Duval stands beneath the campaign banners, composed, precise. Her statement is broadcast" "We made the hard choices so families could be safe. The reclamation was necessary. Our engineers acted with speed and care."
    "You step forward from the crowd when a neighbor asks for a reaction. The cameras pivot toward you like hungry eyes. The world narrows to the press of sound and air; your heart thumps like a fist against your ribs."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "You call this safety—' (Your voice is steadier than you expect. You think of the child who will never learn to row in Lito's cove. You think of the reeds that no longer sing.) '—but you asked the marsh to stop doing what made it alive."
    "Camille Duval: (She inclines her head with silk politeness.) 'We preserved lives. That is the metric of governance.'"

    maya_reyes "Lives are more than dry floors and insured roofs, Camille.' (You feel something loosening inside you — not defeat, but an opening.) 'They are mornings where you know the tide, and the smell of the harbor at dawn, and the place where kids learn to tie a knot. When you smooth the shore you smooth those memories out of the map."
    show camille_duval at right:
        zoom 0.7

    camille_duval "We will return the area with public space and commercial opportunity, carefully managed."

    maya_reyes "Public space won't teach Lito's boy to mend a net."
    # play sound "sfx_placeholder"  # [Sound: A low, building hum — voices rising into a chorus of grievance and resilience]
    # play music "music_placeholder"  # [Music: Crescendo — drums and strings collide into a fierce, cathartic swell]
    "The crowd's voice isn't victory, nor is it surrender. It is a collective intake: part accusation, part elegy. The marsh itself seems to hold its breath."
    # [Scene: City Hall Plaza | Evening]
    hide maya_reyes
    hide camille_duval

    scene bg ch12_3be532_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The murmur of departing crowds, footsteps, the far-off grinding of heavy equipment]
    # play music "music_placeholder"  # [Music: Single cello note hangs, then resolves into a bright, rising pulse]
    "Mayor Sofía finds you among the departing neighbors. She looks worn — not the polished campaign face, but a public servant who has counted ballots and bodies and the weight between them."
    show mayor_sofa_lvarez at left:
        zoom 0.7

    mayor_sofa_lvarez "I know this is not what you wanted.' (Her voice is small. She meets your gaze without flinching.) 'It spared lives in the immediate term. I had to balance the city's obligations."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "And what of our obligations to place?' (You feel the urge to be accusatory; instead you fold it into something that may be useful.) 'Where do these people go when prices rise and the moorings vanish? Who holds the knowledge of place when it's buried under fill?"
    "Mayor Sofía: (She looks away, toward the reclamation lights.) 'We will set up funds for relocation and job programs. We will work with community groups on small restorations inland.' (There is a weary sincerity in her words. You have learned to hear policy as both instrument and insufficient answer.)"

    maya_reyes "Keep your promises in writing."

    mayor_sofa_lvarez "I'll sign it."
    # [Scene: Marsh Edge | Night — Climax]
    hide mayor_sofa_lvarez
    hide maya_reyes

    scene bg ch12_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The final bouts of filling — the slosh of last waters caught and muted; a lone horn from a departing boat; the call of an unseen bird that sounds smaller than before]
    # play music "music_placeholder"  # [Music: Full orchestra — high strings racing, brass bright and uncompromising; the rhythm is relentless]
    "You stand at the edge where Lito's cove used to open. The last barge pulls away, its wake collapsing into the new seam of land. The machines halt like beasts finally sated. The marsh, once braided and free, is now a divided map."
    "Lito: (He kneels where the dock used to be, touching the sheet pile as if it were wood.) 'This is the part where we have to be better at remembering.' (His throat works. He is not looking at you, but you know the words are for everyone.)"
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "We will remember."
    "Elias Stone appears in the glow of floodlights, ink smeared on his palms from a late set of plans. He approaches quietly; neither of you expects reconciliation in the face of the concrete that now carves"
    "your life. Instead there is a shared recognition — you have traversed the same storm and arrived on opposite shores."
    show elias_stone at right:
        zoom 0.7

    elias_stone "I stayed to try to minimize harm. I failed where it mattered."

    maya_reyes "You did what you thought would keep people alive today.' (Your voice is steady, stronger than the tremor beneath it.) 'That mattered."

    elias_stone "And you did what you had to for the memory of this place. That matters too."
    "Maya Reyes: (There is no tidy forgiveness to be manufactured. The intimacy between you is now threaded with the facts of compromise and the geography of loss. You let something like acceptance settle in your chest — hot, honest, and heavier than relief.)"
    # play music "music_placeholder"  # [Music: A violent, bright chord — catharsis embodied, not triumphant at external victory but triumphant in inner clarity]

    maya_reyes "I'll go, Eli.' (It is not an escape; it is a continuation under another sky.) 'I'll take what we have left and keep pushing, keep making maps that remember the reeds and the names of coves."

    elias_stone "Stay safe. And keep sending maps."
    "You fold it into your notebook like a talisman."
    # [Scene: Boardwalk — Night]
    hide maya_reyes
    hide elias_stone

    scene bg ch12_3be532_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low thrum of distant pumps; a child's laugh somewhere like a stubborn bell; the whisper of your coat]
    # play music "music_placeholder"  # [Music: Low, resilient piano with a rising, hopeful motif]
    "You move through the street where people pack and say goodbye. Your neighbors' faces are flecked with resolve and sorrow. Some hug; some argue quietly; some just look at the water as if committing the new lines to muscle memory."
    "You pass Lito's house; his front stoop is empty save for a coil of rope you once saw him use. You touch the wood and it is warm from the day's late sun. You don't cry"
    "yet — not because you are unmoored, but because there is work to do: calls to make, letters to send, communities elsewhere to help shore up."
    "Lito finds you before you can leave. He hands you a small carved piece of wood — a section of a mooring post he salvaged before the fill. It is rough, salt-bleached, a fragment of what was."
    show lito_reyes at left:
        zoom 0.7

    lito_reyes "Keep this with you.' (He won't meet your eyes.) 'When you're far from here, put it down. Remember where you started."
    "Maya Reyes: (You tuck it into your notebook next to the folded plan Elias gave you. Your fingers close around both like anchors.) 'I'll make sure no one forgets this place.' (You feel the words catch and then steady.)"
    # [Scene: City Bus Stop | Midnight — Resolution]
    hide lito_reyes

    scene bg ch12_3be532_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hiss of brakes, soft footsteps, the rustle of paper maps; somewhere a dog barks once]
    # play music "music_placeholder"  # [Music: Warm, full-staff strings — cathartic and forward-moving]
    "You stand with your backpack and your notebook, watch on your wrist catching a slant of streetlight. The bus will take you away from the neighborhood for a while — to other towns where marshes still"
    "breathe and to meeting rooms where policy can be changed from the outside in. This is not abandonment; it is strategy folded into grief."
    "Elias Stone walks you to the bus and stands a small distance away, the space between you now both ordinary and enormous."
    show elias_stone at left:
        zoom 0.7

    elias_stone "I don't know if we'll be —"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "We'll be what we can be.' (You press your palm to his in a compact, fierce goodbye.) 'Thank you for staying."

    elias_stone "Thank you for not letting us forget what the shore taught us."
    "Maya Reyes: (You step onto the bus. The driver nods at you — a small, bureaucratic benediction. You look back once. The lights throw long shadows across the waterline where the marsh is now partitioned. Lito's silhouette is there by his porch, a small dark mark against the new light.)"
    hide elias_stone
    hide maya_reyes

    scene bg ch12_3be532_8 at full_bg
    # play music "music_placeholder"  # [Music: A swell of hopeful violins undercuts the ache; the tempo is fast, but not frantic — resolve in motion]
    "You take your notebook into your lap. Inside are maps inked with loss and plans inked with stubborn hope. Grief lines every margin, but so does intention. You will carry both forward."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "We saved people today, but we lost parts of what made them whole. That doesn't mean the fight is over."
    "You close the book and breathe. The bus pulls away. The town recedes, a patchwork of lights and empty sounds. The machines keep their measured hum in the distance — a reminder of what was done and of what you are now responsible for preserving in memory and with action."
    # play music "music_placeholder"  # [Music: Climactic strings resolve into a single, sustained major chord — not triumphant over others, but triumphant in clarity and commitment]
    hide maya_reyes

    scene bg ch12_3be532_9 at full_bg
    "You leave the neighborhood to continue your activism, heart heavy with the knowledge that what you fought for was not preserved — but steady with the conviction that the work continues, that maps will still be drawn, and that memory will be a form of resistance."

    scene bg ch12_3be532_10 at full_bg
    # play music "music_placeholder"  # [Music: Fade out gently, leaving only the echo of the last chord]

    scene bg ch12_3be532_11 at full_bg
    "THE END"
    # [GAME END]
    return
