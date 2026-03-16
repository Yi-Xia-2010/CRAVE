label chapter49:

    # [Scene: Rooftop Nursery | Morning — Years Later]

    scene bg ch15_60d3dd_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft chatter of volunteers, a distant tide under the city’s hum; a small coastal data-sensor emits a gentle ping each time it posts to the neighborhood feed]
    # play music "music_placeholder"  # [Music: Low, steady cello — a single line that holds and breathes]
    "You smell wet soil and sun-warmed plastic, the particular mix that has come to mean 'work, again' in your bones. Hands move around you with the ease of repetition: Rafi's broad ones, Lio's quick, paint-speckled fingers,"
    "a circle of younger volunteers learning to splice root systems like shoelaces. It has been years, but the ritual feels like the same breath caught and let go."
    show rafi_odeh at left:
        zoom 0.7

    rafi_odeh "Fold the root like this — snug, not crushed. If the sedge breathes, the breakwater breathes."
    show maya_corvin at right:
        zoom 0.7

    maya_corvin "And if it doesn't?"

    rafi_odeh "Then we try again. We graft, we rearrange. It's not magic — it's stubbornness."
    "Your voice catches on the word again: stubbornness. It sits on you the way salt does, slow-caking on the collar. You taught volunteers how to listen to marshland hydrology; you still teach them to listen to grief. Both matter."
    hide rafi_odeh
    hide maya_corvin

    scene bg ch15_60d3dd_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft laughter; the distant rumble of municipal maintenance vehicles]
    "Lio slides a paint-stained rag into your palm, grinning. His mural—two blocks of color and a rolling line that reads like a tide—has become a seasonal ledger. People come to read the years in the colors he chooses: armless blues, bruised pinks, hopeful greens."
    show lio_corvin at left:
        zoom 0.7

    lio_corvin "You ever think it's weird, that people treat murals like calendars?"
    show maya_corvin at right:
        zoom 0.7

    maya_corvin "They're calendars with names. They mark what we came back for."

    menu:
        "Prioritize seedlings for market stalls":
            "You nod toward the crates destined for Market Street. 'Sell the seedlings, feed us—keep the project alive.' Rafi hums agreement and begins boxing."
        "Send more sedge to the breakwater project":
            "You touch the sedge tray, imagining the frayed coastline. 'We need that edge stronger.' Rafi's face tightens; he makes notes and reroutes volunteer pairs."

    menu:
        "Propose a memorial plaque listing lost houses":
            "You suggest a plaque to mark what was replaced. The board takes it in, some nodding, others hesitating. Elias writes a note. The idea moves forward cautiously."
        "Push for increased maintenance funding instead":
            "You press for contingency funds. The board exchanges glances; it requires new votes but carries weight. Dr. Sima offers technical illustrations to support the ask."
    "THE END"
    # [GAME END]
    return
