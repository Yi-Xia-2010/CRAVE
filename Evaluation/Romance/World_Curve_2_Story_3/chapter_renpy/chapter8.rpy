label chapter8:

    # [Scene: Tidewatch Lab | Early Morning]

    scene bg ch8_6b08b4_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, brittle strings]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls; the soft mechanical hum of the pilot instruments]
    "You step into the lab and the air closes around you—cool, briny, the smell of wet timber and old oil. Instruments click and the pilot on the flats sends a tidy pulse to the screen: data,"
    "stillness, and the promise of a thing that can be argued into meaning. Luca stands by the map table, his hands stained with tar from the previous site visit. He hasn't tied his red bandana to"
    "his wrist; instead it hangs loose, drying."
    "You feel the gravity of the joint review like a weather system; it presses at your ribs with a cold steadiness. Here, in the hush of the boathouse, the trial begins to feel less like controlled"
    "science and more like a conversation with a city that will not be swayed by graphs alone."
    show luca_moreno at left:
        zoom 0.7

    luca_moreno "They shifted two of the monitoring buoys further inshore. Contractors said it was a depth issue—easier to anchor. Seems small until you model the fetch."
    show isla_morgan at right:
        zoom 0.7

    isla_morgan "Small moves ripple. Buoys measure edge conditions. Move them in, and the data will understate erosion on the flats."
    "Luca Moreno leans over your shoulder, eyes scanning your tablet where your model lines are thin and honest. He taps a jagged section of the curve."

    luca_moreno "Aria wants a steady story. Investors want a steady story. We gave them a joint trial to be honest. Now 'steady' is taking the shape of small edits."
    "You pause, tasting metallic salt and the bitter tang of compromise. Your thumb finds the rim of your father's compass in your pocket; it is warm with early-morning warmth and stubborn as memory."

    menu:
        "Confront the site foreman about the relocated buoys":
            "You walk the pier to the contractor's truck, and the foreman tightens his jaw—answers come clipped, practical. He repeats 'anchoring concerns' like a prayer and your notes grow new margins."
        "Record the change, mark it for later, and return to the lab to re-run your model":
            "You step back from the dock and the wind scours your face. Back at Tidewatch, numbers re-spin, the differences cold and precise; the longer you look the more rooms for doubt open up."

    menu:
        "Tell Ravi to film and timestamp every placement change":
            "Ravi lifts his camera like an oath. You feel a small axis of control return as footage records the slow drift of the trial away from your design."
        "Approach the foreman with the models and ask for a pause":
            "You walk toward the foreman with tablet in hand; he reads the glossy render, shrugs, and says you need council authorization for changes. The rain picks up as an accusation."

    menu:
        "Confront Aria publicly at a council session with the ledger.":
            jump chapter9
        "Refuse to sign off on interim results and delay funding until corrections are made.":
            jump chapter17
        "Continue collecting evidence quietly to build an unassailable case.":
            jump chapter13
    return
