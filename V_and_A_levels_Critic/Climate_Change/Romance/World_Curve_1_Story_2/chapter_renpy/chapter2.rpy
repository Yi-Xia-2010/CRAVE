label chapter2:

    # [Scene: Municipal Plaza | Late Afternoon]

    scene bg ch2_c4ca42_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, steady cello with distant wind synths]
    # play sound "sfx_placeholder"  # [Sound: Muffled footsteps on wet wood; a camera shutter clicks in the distance]
    "You step out from under the greenhouse's amber glow with the folded papers heavy against your ribs. Dr. Noor's words cling like humidity: People will judge you by what you do next. You feel them press"
    "into the hollow you carry—less an accusation than a sluice gate that won't quite close."
    "The plaza smells of strong coffee and wet coats; steam lifts from paper cups and blurs the edge of every face. Floodlights make the varnished wood of the municipal panels look almost theatrical, and it is"
    "unnerving how small that theatricality makes the real stakes feel. You tuck your Moleskine into your coat where the rain can’t reach the spine and let your fingers find the chipped enamel of the seagull pin"
    "at your lapel. The metal is cold and familiar."

    scene bg ch2_c4ca42_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low murmurs, the scrape of chairs; a distant gull cries]
    "Inside, people gather like different weather systems. Lina Moreau arrives with her trench coat a precise line against the damp—tablet-case clasped, posture immaculate. Where she passes, camera lights catch the edge of polished leather; her expression"
    "is an engineered calm. Ephraim’s suit looks wrong in this salt air, a slick shadow that doesn't absorb the light so much as refuse it. Sora Watanabe moves through the room like heat: paint on their"
    "cargo pants, a shell-and-glass pendant that taps softly when they gesture. Maya is a quick corner of movement and whisper, the scent of sea-spray following her."

    scene bg ch2_c4ca42_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Paper rustle; the quiet beep of a tablet]
    "Dr. Noor is already there, hands smoothing a printed projection onto the corkboard: probabilistic ranges, failure modes, a small cluster of worst-case markers that complicate Lina Moreau's tidy line. She doesn't meet your eyes at first—only"
    "the slow, precise motion of someone who knows what numbers feel like when they are laid over people's lives."
    show dr_noor_patel at left:
        zoom 0.7

    dr_noor_patel "Ari—if you're going to say anything, thread it through the uncertainties. They need to know confidence is bounded."
    hide dr_noor_patel

    scene bg ch2_c4ca42_4 at full_bg
    show dr_noor_patel at left:
        zoom 0.7

    dr_noor_patel "Make it human-sized. Don't let them hide behind absolutes."
    "You inhale. The air is cool and metallic in your chest, a taste of old pennies and distant brine."
    show ari_navarro at right:
        zoom 0.7

    ari_navarro "I can do that. I can—' You search for a phrase that won't slip into technocratic jargon. 'I can explain trade-offs without making them feel like statistics."
    "Dr. Noor studies you, then nods once, small and decisive."

    dr_noor_patel "Good. And—"

    dr_noor_patel "—remember who this is for."
    "The room rearranges itself into conversations. You drift toward a cluster where Maya and Sora Watanabe are speaking under the dim, haloed light of a recessed lamp. Maya’s voice is low and rapid."
    show maya_cruz at center:
        zoom 0.7

    maya_cruz "Ephraim's been seen with municipal aides. His firm just donated to the overflow relief fund—no strings, he says, but you know how those 'no strings' look."
    "You feel each syllable like a pebble rolled across a map in your breast—small, disruptive."

    menu:
        "Fold the rumor into your remarks":
            "You make a quick note on the edge of the page: transparency, conflict-of-interest. The word sits heavy but sharp, a tool rather than an accusation."
        "Keep the focus technical for now":
            "You close the Moleskine and breathe, reminding yourself that inflaming speculation in this chamber could fracture fragile alliances. The note remains unwritten."

    # --- merge ---
    "Narrative resumes after the choice"
    "Sora Watanabe catches your hand—warm, callused, paint-smudged. Their eyes widen in a private, earnest insistence that feels like a sun briefly breaking through the fog."
    hide dr_noor_patel
    show sora_watanabe at left:
        zoom 0.7

    sora_watanabe "You have to speak at the rally after the vote. People will listen when you say the human costs in terms they understand.' (They glance at the corkboard.) 'Noor's models—your maps—when you say those things, it means something. Please."
    "You want to answer with the careful syntax of planning: conditional probabilities, evacuation timelines, the margins of error. Instead your mouth holds a simpler truth—that your heart has been pacing like a metronome since the flood—and"
    "you don't know whether telling that truth will rally people or make them pity you."

    ari_navarro "I don't want my grief to be the spectacle. I want it to be useful."
    "Sora Watanabe leans forward, elbows on their knees, voice soft enough that their sincerity feels like a confession."

    sora_watanabe "It won't be spectacle. Not with you. You'll make it about us—about the people who live here, the ones who can't be counted as data points. That's what moves the council; that's what moves votes."
    "Ephraim approaches then, a smile like slick varnish. He speaks in that practiced, corporate cadence, words polished to avoid any ragged edges."
    hide ari_navarro
    show ephraim_blake at right:
        zoom 0.7

    ephraim_blake "Ari, your work is respected. The region needs clear infrastructure plans. I hope you'll support the proposal that secures funding. It's pragmatic."
    "There's an edge in the air when he says the word 'secure'—as if it also applies to secured profits. Lina Moreau stands nearby, listening with the steadiness of someone trained to measure rhetorics for leverage."
    hide maya_cruz
    show lina_moreau at center:
        zoom 0.7

    lina_moreau "We are out of time for ideological purity. The model shows what investment can stabilize. We need to make decisions that minimize loss—not exacerbate risk by delaying implementation."
    "You want to argue the merits of hybrid solutions, living shorelines combined with engineered reinforcements, community oversight clauses built into financial agreements. You want to articulate the moral calculus with the clarity Dr. Noor insists on. But your throat is a narrow channel and the room's warmth presses against it."

    menu:
        "Step closer to Lina and offer a technical amendment":
            "You smooth your jacket and move a half-step forward, voice measured as you outline a contingency: phased funding tied to community governance. Lina inclines her head minutely, the gesture ambiguous—neither acceptance nor refusal, merely the record of being heard."
        "Stay back and talk to Sora about the rally":
            "You let yourself fall back to Sora's side. They give you a small, grateful smile; for a moment the crowd noise, the cameras, the whole apparatus recedes to a dull sea hum."

    # --- merge ---
    "Narrative resumes after the choice"
    hide sora_watanabe
    show dr_noor_patel at left:
        zoom 0.7

    dr_noor_patel "Ari, there are parts of the model I didn't publish. Past assumptions made by others—' (her jaw tightens) '—they underestimated compounding failures in certain scenarios. The worst-case runs are not improbable."
    "You feel the words like a low tide pulling at whatever anchored you. The room seems to invert: the lights sharper, the smell of coffee suddenly too much. Lina Moreau's face doesn't change, but her eyes—ice-gray, precise—hold at the edges of your awareness."

    lina_moreau "If the council delays until perfect information appears, people die. We must act on the best available data and secure the funding that allows maintenance to happen."
    "There's no malice in her voice, only a logical pressure that treats compromise as a necessary calculus. You think of the childhood streets, the asphalt that used to be solid under your feet and is now"
    "a memory line on a faded photograph. You think of the sibling you lost—how the sirens never matched the urgency you felt from within."
    hide ephraim_blake
    show sora_watanabe at right:
        zoom 0.7

    sora_watanabe "We can't keep letting 'pragmatic' be a synonym for 'let them suffer.' The people here—your neighbors—need a voice that refuses that shorthand. You give it to them."
    "You close your Moleskine for a second, pressing the cover with the heel of your hand. The pages whisper shut—a small, private sound."
    hide lina_moreau
    show ari_navarro at center:
        zoom 0.7

    ari_navarro "The models show where systems fail. They also show where community action changes the curve. I want to make that visible."
    hide dr_noor_patel
    show maya_cruz at left:
        zoom 0.7

    maya_cruz "Visible, and legally binding. Promise me you'll push that part. They'll sign on if we make it accountable."
    "The murmur in the chamber creeps higher like fog thickening along the boardwalk outside—still slow, still inevitable."
    "Your heart pounds, but the motion is more mechanical than theatrical: measure tide heights, map evacuation corridors, list the human clusters that need priority routes. Your hands know the vocabulary even when your mouth can't find the courage. Stillness and small, precise movements tether you."
    "Outside, through the high windows, gulls wheel in slow spirals and the boardwalk reflects neon work lights and murk. The city's breath is a steady, indifferent exhale. You feel the familiar weight settle over you again—the knowledge that policy choices have bodies attached to them, warm and honest and mortal."
    "Sora Watanabe squeezes your shoulder, the contact brief and grounding."

    sora_watanabe "Please. Be our voice."
    "You can feel the chamber tilt toward a single axis: the vote looms and everything funnels into it like water into a drain. Cameras angle for close-ups; murmurs sharpen into listable talking points. Your Moleskine is"
    "a small island of paper in your palms, and within it, your notes look like trapdoors of their own design—precise, necessary, and terrifying."
    "You close your eyes for a second and try to breathe into the small, methodical spaces you were trained to trust. The air tastes of metal and caffeine and rain. Your reflection in the window is"
    "a faint double—Ari as planner, Ari as someone who still keeps small people and faces in mind while making big graphs."

    ari_navarro "If I speak, it won't be to score points. It will be to make real the consequences of this vote."

    sora_watanabe "Then say it."
    hide sora_watanabe
    hide ari_navarro
    hide maya_cruz

    scene bg ch2_c4ca42_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The room's noise dims into a humming baseline; music drops to a single sustained cello note]
    "You feel the pressure coil—quiet, inevitable. The decision radiates outward from the small, warm place under your sternum: say the words that might sway a vote, expose uncertainties that could stall funding, or stay careful and let the machinery run its course."
    "The air seems to hold in one long, uncertain inhale."

    scene bg ch2_c4ca42_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
