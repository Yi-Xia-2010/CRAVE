label chapter15:

    # [Scene: Tidelab Greenhouse | Pre-dawn]

    scene bg ch15_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Quiet, rising piano with a steadying cello underpinning; the motif of hope threading upward.]
    # play sound "sfx_placeholder"  # [Sound: The soft click of keys, the distant gull-call, the hum of a dehumidifier beating like a second heart.]
    "You breathe through the cold press of decision and feel the brass tidewatcher warm against your throat. The forensic review sits on the screen of your tablet like a small, definitive shape: annotated models, resonance graphs"
    "overlaid with tide event histories, a step-by-step explanation of the feedback loop the consortium ignored. Your hands are steady; your chest is a reservoir of the weary, exact kind of courage you've practiced for years."
    "Asha leans over your shoulder, her glasses fogging in the greenhouse steam. She reads the executive summary again, slower, as if tasting a word to be sure it won't cut the wrong way."
    show asha_mehta at left:
        zoom 0.7

    asha_mehta "This is airtight, Mira. You framed the uncertainty, showed the worst-case coupling, and—' (she exhales) '—you showed the evidence."
    "You nod. You think of Ruben's hands folding nets, of Nadia's small laugh when she splashes in tidal pools, of the orchard's trunks leaning against the sky. You think of the promise Jonah dangled, the warm"
    "offer of integration and a steady paycheck tucked inside his sleek, polite sentences. You think of the families who would be uprooted by construction through the night."
    "You tap the send icon with a thumb that trembles just a fraction. The file goes out to the regional council, to two independent reviewers Asha recommended, to the town's listserv, and — most important —"
    "to a public repository with open access. It radiates in little pings across your wristband and Asha's tablet."
    # play sound "sfx_placeholder"  # [Sound: A small cascade of notification chimes; somewhere a gull wheals louder as daylight starts to unroll.]
    hide asha_mehta

    scene bg ch15_601bcb_2 at full_bg
    show asha_mehta at left:
        zoom 0.7

    asha_mehta "You did the right thing."
    "You want to parse 'right' into safety margins and job loss probabilities, but the word lands elsewhere—like a seed hitting soil."

    menu:
        "Call Cassian before the press picks it up":
            "You bring the phone to your ear. He answers on the second ring, a sleepy chuckle that turns serious when he hears the word 'publish.' He says nothing at first, then: 'We weather it together, Mira.' The line crackles with a tenderness that steadies you."
        "Let it roll out publicly; don't call":
            "You let the phone lie face-down. The greenhouse fills with the sound of meters and plants. You watch the upload complete and hold Asha's gaze; there's a professional, private intimacy in that shared, silent decision."

    menu:
        "Take a breath and offer to walk the council through the models":
            "You nod and say, 'I'm prepared to walk you through it—step by step.' You set your tablet on the lectern, the graphs projecting behind you. Faces lean in, the room narrowing to the thin, sharp clarity of diagrams and questions."
        "Let the independent reviewers speak first":
            "You step aside. Two independent reviewers rise, calm and precise; they corroborate the findings. The room's energy shifts from suspicion toward procedural seriousness."

    menu:
        "Accept his hand and walk with him to Ruben's":
            "You allow your fingers to lace with his. The two of you move toward the quay where Ruben waits. The proximity speaks of unfinished apologies and of rebuilding together."
        "Step back to listen to the crowd, keep working":
            "You step back, letting Cassian go ahead. There is practical work to do—phone calls, organizing, meeting neighbors. You give him a look that says you will be there later."
    "THE END"
    # [GAME END]
    return
