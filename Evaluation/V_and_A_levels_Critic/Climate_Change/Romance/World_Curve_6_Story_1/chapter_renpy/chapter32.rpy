label chapter32:

    # [Scene: The Old Promenade | Pre-dawn]

    scene bg ch14_1f005a_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The tide murmurs against pilings; distant diesel hum of a night crane.]
    # play music "music_placeholder"  # [Music: Sparse, urgent strings — a staccato undercurrent that never quite lets you rest]
    "You walk with the weight of two nights folded into your shoulders. The trefoil on your wrist is a quiet, persistent ache beneath skin—an old punctuation mark: keep going. The murals across from Rafi's tents are"
    "half-dry, streaked where last week's salt wind met fresh paint. Lio moves like someone carrying a secret in his bones: a roll of tarp, coffee in a chipped cup, eyes quick and guarded."
    "You expected exhaustion. Instead you feel raw alertness — nerves keyed to the thin, sharp edge of what comes next."
    show rafi_odeh at left:
        zoom 0.7

    rafi_odeh "We moved people, we logged names, we rerouted water where we could. But schedules don't know how to grieve. They know timelines."
    "You nod once. There is no argument worth having here — only things to be done."
    "You think about the hearing that could have been a ground-and-clay roar and instead became this slow, legal engine: amendments, audits, schedules. You think of Camila 'Kai' Navarro's clean blueprints and Elias Kahn's tired steadiness. The"
    "municipal amendment exists now, but it is a living thing that must be fed and guarded. The arousal inside you tightens: meetings stack into one another like storms on the horizon."
    # [Scene: Rooftop Nursery & Green Lab | Morning]
    hide rafi_odeh

    scene bg ch14_1f005a_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Bees, the clank of a toolbox, a municipal comm badge buzzing in a pocket.]
    # play music "music_placeholder"  # [Music: Rapid violin runs — anxious, practical]
    "Dr. Sima kneels over a sensor array, fingers moving with the kind of mess-you-can-trust precision that only years in the field gives you. She hands you a tablet; graphs bloom in cold colors and jagged lines. Budget numbers overlay predictive surge models in tight parentheses."
    show dr_sima_raza at left:
        zoom 0.7

    dr_sima_raza "The models agree on one thing: without enforced monitoring and maintenance, structural measures erode faster than they protect. You know this. The counter is always funding and political will."
    "You read the projections. The numbers want to be mathematical certainties; they are instead a list of conditions, 'if' attached to 'unless' like clauses in a hostage note. Your stomach flips. The very high pressure of deadlines presses at your throat."
    show maya_corvin at right:
        zoom 0.7

    maya_corvin "We need the board to have teeth. Independent audits, clear penalties, funded maintenance line items. No backdoor waivers."

    dr_sima_raza "Technically defensible. Politically explosive."
    "Her voice is not unkind. It is a bell sounding in a building that may be about to fall different ways."
    show lio_corvin at center:
        zoom 0.7

    lio_corvin "And you'll make them listen, right? Promise?"
    "You want to promise because making promises is how you coax people into the weather. Instead you offer what you can keep:"

    maya_corvin "I'll make them accountable. I won't let it be a checkbox."

    menu:
        "Check the latest sensor logs":
            "You swipe through dense feeds: salinity spikes, a leak near Pier 7 flagged. Your stomach tightens as the numbers darken."
        "Help Lio re-tie a greenhouse panel":
            "You loop the cord and pull it tight. Lio's fingers are quick. It's small, but the panel stops rattling — an immediate fix against a patient problem."

    menu:
        "Call out the worker conditions you heard about":
            "You name the rumors: overtime without breaks, temp contracts. Kai's jaw tightens; her eyes go unreadable for a beat. She nods, a small concession."
        "Focus on technical compromises — point to the data":
            "You lay out the salt thresholds and maintenance windows. Kai listens, pen poised. The conversation goes colder, more procedural, but it moves forward."

    jump chapter47
    return
