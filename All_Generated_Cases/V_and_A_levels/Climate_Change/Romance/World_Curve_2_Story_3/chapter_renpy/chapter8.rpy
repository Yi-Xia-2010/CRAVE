label chapter8:

    # [Scene: Municipal Hall Lobby | Late Afternoon — Storm Raking the Windows]

    scene bg ch8_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Heavy rain patters against the concrete façade; distant rumble of construction equipment; a phone vibration, sharp in the hush.]
    # play music "music_placeholder"  # [Music: Tense, clipped strings — heartbeat tempo; low brass undercurrent.]
    "You are still seated when your phone vibrates in your pocket. The projection behind the glass is a pale rectangle of future-maps and colored risk bands; rain streaks the window like a smear of urgency."
    "Your chest is a drum you cannot silence. You can feel every choice you've ever deferred collecting at the base of your throat: the long-line, the Glasshouse trays, Mika's texts, Old Tom's weathered maps. The projection"
    "in the meeting is supposed to be a neutral thing — numbers, not people — and yet it hangs between you like a verdict."
    show rina_corbett at left:
        zoom 0.7

    rina_corbett "We need a motion. We need to decide now."
    "You slide the phone free. The message preview is a line from the community list: Construction crews mobilizing at dawn. Volunteers needed. Another notification: an anonymous upload — a copy of private flood projections, stamped internal and unreleased."
    "Your fingers go cold. The document’s margins are full of red flags; the modeled inundation is worse than the public maps — worse for certain neighborhoods you thought were safe. The leak could force the council"
    "into emergency action, fast and uncompromising. Or it could ruin you for breaking confidence. Or both."

    menu:
        "Open the leaked file now":
            "You pry your thumb across the screen. The swath of color opens like a wound; the fine print tilts the balance of everything you promise to protect."
        "Hide the file and keep listening":
            "You tuck the phone back into your pocket. Listening buys time; time is what you need to measure harm before you decide how to do it."

    menu:
        "Hand the projections to Kai to incorporate into the demo plan":
            "You pass the paper. For a second, Kai's jaw relaxes — raw possibility. It's a risk, but you can see her already scheming the optics."
        "Keep the projections and ask Elias to model alternate scenarios":
            "You keep the page, fingers folded over the margin notes. Elias nods, lips pressed. He wants the numbers sanitized into policy — a buffer, a stair-step of compromise. It feels like shelter."
        "Fold the projections and place them in the satchel — buy one more night":
            "You fold the pages and slide them into your satchel. It is a small, cowardly gesture; you know it. But it buys breathing room, a quantity of time that might let you be less cruel in your next move."

    menu:
        "Release the projections publicly — force the issue.":
            jump chapter9
        "Keep them confidential — negotiate targeted relocation and supports.":
            jump chapter11
        "Do a field demo with Kai — win hearts not headlines.":
            jump chapter13
    return
