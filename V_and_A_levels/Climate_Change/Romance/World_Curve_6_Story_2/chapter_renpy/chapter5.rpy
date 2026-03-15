label chapter5:

    # [Scene: Nursery Plots | Late Afternoon]

    scene bg ch5_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind tearing at canvas tarps; distant gull calls; the soft scrape of a rake]
    # play music "music_placeholder"  # [Music: Fast, insistent strings with a steady driving pulse — bright under pressure]
    "You walk the lab-lined paths between the nursery plots, palms dusty with sand and peat. The living-dune tests hold. Where the grasses were thin, they have threaded together a spine; where the burlap fences were placed,"
    "sand has begun to build. Volunteers joke with each other over awkward shovelfuls, and their laughter makes the air taste like hope and wet rope."
    "Your field notebook is clipped to your parka — pages smudged with tide charts and Nyla’s hastily drawn schematics. Your thumb finds the tide-watch in your pocket; the brass is warm from your skin. You feel"
    "less like a strategist this evening and more like someone who has sewn stitches into a living thing and is watching it take."
    show nyla_torres at left:
        zoom 0.7

    nyla_torres "The sensors are saying what we wanted. Last three runs show sediment accretion up ten percent in the southern swale."
    show maya_serrin at right:
        zoom 0.7

    maya_serrin "Ten percent.' You let the number sit. It feels larger when everyone in town can see it on a screen, larger when a tide-watch warms in your pocket. 'Good. That'll help the grant narrative — tangible stabilization, not just promise."

    nyla_torres "Mayor Hale already called. He wants a demonstration he can point to in two weeks for the funding panel."
    "You inhale; the dune-smell is green and iron-rich. Two weeks. The timeline tightens like a winch."

    "Volunteer (off)" "We're bringing more coir tonight. Aiden's crew said they'd double the shift."
    "Aiden Koa arrives then, sleeves rolled, his jacket smelling of tar and diesel. He moves with the calm of someone who has spent years balancing on decks in heaving seas. He doesn't say much at first"
    "— just watches the new ridges, palms open as if wanting to feel whether the plant roots have actually taken."
    show aiden_koa at center:
        zoom 0.7

    aiden_koa "Looks good."

    aiden_koa "You're stubborn as a cliff, Maya.' (He nods at the dune.) 'That's not a small thing."

    maya_serrin "Neither are you."

    menu:
        "Ask Aiden to survey the southern channels tonight":
            "He nods and straps on his compass; the two of you head toward the boardwalk to check net passages, the night air filling with plans."
        "Tell Nyla to prep the grant visual packets and data prints":
            "Nyla's fingers fly across the tablet; she already sketches the layout for the presentation, buoyant and swift."

    menu:
        "Turn to the co-op and ask them for an emergency consultation now":
            "They gather at a table; nets are spread like maps, voices low and fevered — their knowledge colors the room with practical fear and resilience."
        "Ask Elena for a draft of binding oversight terms before any construction":
            "Elena nods, already reaching for a holo-pad; you see the legalese approach as both armor and razor."

    menu:
        "Refuse the partnership and double down on community-only funding and labor.":
            jump chapter6
        "Accept a tightly governed hybrid: allow limited engineered work only where absolutely necessary under binding community oversight.":
            jump chapter14
        "Launch a public campaign to secure the grant without ceding control, using our data and civic pressure.":
            jump chapter16
    return
