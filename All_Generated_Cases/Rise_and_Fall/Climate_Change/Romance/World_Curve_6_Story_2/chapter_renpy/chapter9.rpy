label chapter9:

    # [Scene: Highwater Cove Harbor | Early Morning]

    scene bg ch9_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant clink of metal, a diesel winch whining, gulls complaining in short bursts]
    # play music "music_placeholder"  # [Music: Low, minor strings; a single cello carries the air like a tide]
    "You stand at the pier's edge and let the morning come in along the salt. The concrete blocks smell faintly of wet stone and fresh rain; behind them, the old harbor breathes around new interruptions—nets looped"
    "over galvanized hooks, patched buoys rocking, and men with sun-hardened faces checking sealant with practised hands."
    "The contractor's foreman—gray beard, hi-vis vest—pats a clipboard, glances toward you, and gives a curt nod that tries to be friendly. Jonah stands nearby, leaning on the rail, thumbs tucked in his vest pockets. He jokes about the winch's patience; his laugh lifts, but it doesn't reach his eyes."
    "You fold your scarf up to your mouth against the spray and find your compass in your palm. The brass is cool, the needle trembling as if unsettled by the new weight of metal along the waterline."
    show maya_armitage at left:
        zoom 0.7

    maya_armitage "They've started earlier than the schedule said."
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "They started when the checks cleared. That's the new clock now."
    "He taps the concrete with a gloved knuckle. 'Looks sturdy, though. Maybe it'll keep Nan's stoop dry for another season.'"

    "You want to say" "We compromised for that exact moment."
    "Jonah Reyes watches the module sink with a fisher's eye. He tells you about maneuvering smaller boats through the new channels, how they'll need to adjust nets, how a few of the old coves are already"
    "silting with the redirected flow. The change is technical and personal at once—a new map to memorize before the fish remember the old one."

    "Contractor Foreman" "We kept the heritage line clear where we could. Remedial planting planned for spring. Public walkway still there, slightly elevated."
    "He eyes you."

    "Contractor Foreman" "Council wanted speed. We gave 'em speed."
    "You feel the tension in the word 'speed': emergency and erasure braided together. It hums beneath your ribs like a siren that hasn't yet gone off."
    hide maya_armitage
    hide jonah_reyes

    scene bg ch9_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The winch stops; a short, metallic echo]
    "You find yourself cataloging losses and gains like a ledger: families spared immediate displacement; a block whose foundations now hold through the highest tides; a creek rerouted that used to be Jonah's brother's favored netting spot. Each item is a small wound and a small stitch."
    "Gracie 'Nan' approaches, slower than she used to be. Her kerchief is damp at the edges, and she carries the smell of tobacco and lemon oil. She lays her hand on your arm with a grip that is steady and warm."

    "Gracie 'Nan'" "It keeps the water out of some rooms, child. But the sea keeps its memory in other places. Don't pretend the house and the memory are the same thing."
    show maya_armitage at left:
        zoom 0.7

    maya_armitage "I know.' Your voice comes out small as if speaking at a wake. 'I know we bought time, but at what cost?"

    "Gracie 'Nan'" "At the cost of living. We live anyway. We live badly, we live well. The same water that takes also gives."
    "Her gaze drifts to Jonah, then back to you, and the look she gives holds both pride and an ache."

    menu:
        "Ask the foreman about flow models":
            "You step toward the foreman, pointing at the adjacent channel. He obliges—pulls up a laminated map and explains flow vectors in clipped language; the jargon feels cold against the harbor's salt. You nod, filing the technical answers into a folder of compromise."
        "Stand with Jonah in silence":
            "You step back and stand beside Jonah. Neither of you speak; the harbor provides the words—winch, gull, water on wood. Jonah's shoulder brushes yours, and for a second the geometry of loss simplifies: two bodies against the wind."

    menu:
        "Kneel to check the saplings":
            "You crouch and run your fingers through the silt. A few shoots are stubborn—mud clings to your nails. The tactile work calms you for a moment; you pluck a smothered blade of grass free and plant it again, feeling the soft pulse of life."
        "Call Rafi to audit the wash patterns":
            "You pull out your phone and leave Rafi a detailed voicemail—time stamps, GPS coordinates, urgency indicated by clipped sentences. It channels your perfectionism into protocol. You feel a small relief—action that is useful, if insufficient."
    "THE END"
    # [GAME END]
    return
