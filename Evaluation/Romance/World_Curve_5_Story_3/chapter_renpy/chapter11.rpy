label chapter11:

    # [Scene: Community Greenhouse & Restoration Lab (the boathouse) | Early Morning]

    scene bg ch11_e67f19_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of sensor readouts; gulls thinly audible beyond the glass]
    # play music "music_placeholder"  # [Music: Quiet, resolved strings with a minor undertow]
    "You are at the bench where the night’s work ended and the next day’s anxieties gather. Your fingers find the brass clip of your notebook out of habit; the seashell pendant rests warm against your collarbone."
    "The validation notice sits in the comms thread you left open: an independent coastal institute has reviewed the datasets you and the volunteers compiled, and their brief is short and precise — it supports your core"
    "findings about marsh buffering capacity and long-term carbon sequestration."
    "For a moment you let the weight shift. Validation is not applause; it is the kind of authority that can be quoted in meetings, printed on placards, and made to move policy. You feel the static"
    "prickle of possibility and, underneath it, the familiar ache: every new lever makes someone somewhere push harder in the opposite direction."

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A muted chime as more messages trickle in]
    "Mika bursts in with muddy boots and sunburned impatience, hugging a stack of volunteer schedules like a shield."
    show mika_tan at left:
        zoom 0.7

    mika_tan "They quoted you in the hearing transcript — Elena used your phrasing. People were actually listening, Aya. For a minute I thought we'd won."
    show amaya_saito at right:
        zoom 0.7

    amaya_saito "We got a validation, not a victory.' (You try to keep your voice even.) 'But it's the kind of thing that makes a paper trail. Keep the lists intact; we can't have anything disputed on clerical grounds."

    mika_tan "Right. Right. I'll lock everything down and get the team ready. Do you want me to run the sensor array through—"

    amaya_saito "Yes. Twice. Cross-validate. And call Dr. Kaito — ask him to sign an advisory note if he can.' (You can feel the practical motion settling you: tasks are the scaffolding for courage.) 'Also… keep the volunteers briefed. No provocation. Let the data do the talking."

    mika_tan "Data talks. People panick faster."

    menu:
        "Send a calm press release quoting the institute":
            "You draft a short, neutral statement, emphasizing facts and inviting open peer review; your fingers hover before you hit send, imagining the headline it will make."
        "Call Elena and ask for a civil defense meeting":
            "You pick up the phone and call the mayor; you hear her inhale, tired and ready, and you schedule a meeting that will gather officials and first responders into a single room."

    menu:
        "Go to the site now and speak to crews":
            "You head out, boots on, inhaling salt and diesel; up close, the work feels heavier, the machine noise a metal prayer — you ask precise questions and hold the camera steady for the record."
        "Stay at the boathouse to secure datasets and coordinate release":
            "You stay, fingers flying across keys, redacting sensitive details while building a narrative that can withstand Maren's framing. The lab becomes a quiet fort of evidence."

    jump chapter12
    return
