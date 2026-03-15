label chapter4:

    # [Scene: Municipal Plaza | Morning]
    # play music "music_placeholder"  # [Music: Low, urgent percussion under a thin, anxious piano]

    scene bg ch4_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmur of voices, a child's cough, the distant slap of a wave on pilings]
    "You already said it—Etta's name, the marsh, the plan. The words taste of iron and peat in your mouth, equal parts promise and accusation. The plaza hums with that brittle, urgent energy that follows a public commitment: relief braided with the immediate knowledge that the work starts now, not later."
    "Etta's hand closes over yours—small, knuckled, rooted like the coir you will stack—and you feel the tremor in her grip. She doesn't need to tell you anything; her eyes are a map of winters and seedlings."
    "Around you, neighbors clap, shout, wave laminated lists, hand out gloves. Mateo Alvarez stands a little behind you, jaw tight, fiddling with the seam of one of his buoy prototypes as if tuning courage. Jun's face"
    "is set, lips pulled thin; his salt-stiff hair is plastered to his skull."
    "You pull the camera from your tote and let it hang at your chest. It steadies you enough to speak practical things—training shifts, supply runs, volunteer check-ins—because if you don't make the plan concrete, the weight of everyone else's hope will collapse into noise."
    show etta_hargrove at left:
        zoom 0.7

    etta_hargrove "We leave at low tide. Bring boots. Bring friends. Bring patience.' (Her voice cracks on the last word, then steels.) 'And Ari Tanaka—keep breathing."
    show ari_tanaka at right:
        zoom 0.7

    ari_tanaka "I will. We'll start at the Flats tomorrow at dawn. Mateo Alvarez, we need sensors on the coir lines—you said you could rig something small and durable?"
    "Mateo Alvarez: (he exhales sharply) 'I can. But it's a bandage without scale. We need more buoys, wider deployment. Otherwise it's—' (he searches for the word) '—fragile.'"

    ari_tanaka "Fragile is better than surrender,"
    "Mateo Alvarez: (after a beat) 'I know. I'll help. I just—don't let us pretend it will hold storms by itself.'"
    "A murmur of agreement ripples through the crowd. You file Mateo Alvarez's warning away like a splinter: present and prickly, impossible to ignore."

    menu:
        "Give Mateo a curt nod and order him to integrate the sensors":
            "You cut him off gently but firmly, eyes locked, and he nods—reluctant, but loyal enough to follow your lead."
        "Ask Mateo to outline the scale problem now, in front of everyone":
            "You invite the tension into the open. Mateo Alvarez inhales, voice low but public; his caution spreads through the crowd like a cold wind. Etta reaches for your sleeve, alarmed and grateful at once."

    menu:
        "Tell Mateo to deploy the sensors only after you secure community consent":
            "You fold your hands around the plan like a brace. Mateo Alvarez's jaw ticks; he agrees slowly, the scientist in him reluctant but respectful."
        "Ask Mateo to covertly test a sensor line tonight for data we can show the council":
            "Heat flashes across Mateo Alvarez's face—he doesn't like secrecy—but he understands urgency. He nods, fingers already tracing the straps of the sensors."

    jump chapter5
    return
