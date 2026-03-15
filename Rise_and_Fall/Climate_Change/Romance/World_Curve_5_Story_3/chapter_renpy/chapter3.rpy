label chapter3:

    # [Scene: Waterfront Amphitheater | Dawn]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Rising hopeful strings, soft percussion tapping a steady heartbeat]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the low murmur of a gathered crowd, a faint drone whirring like a curious insect]
    "Narration"
    "You arrive from the boathouse with the map tube under your arm and the notebook heavier than it did this morning. The air tastes of salt and cold metal; fog beads on your lashes. From the"
    "dock you can see the marsh like a living map—channels braided silver, reeds standing like sentinels. Above them, Atlantech's proposed render glows on a suspended screen: clean concrete lines, cranes as tall as memory. It feels"
    "clinical against the marsh's soft edges."
    "You tuck your hair knot tighter with a fingertip—sea-grass braid catching a bead of fog—and feel the brass clip of your father's journal press against your ribs, a reminder you can hold with two hands. Elena"
    "stands to your left, shoulders squared but eyes tired in that way leaders get after too many choices have been piled on top of them. Mika is in the crowd, a bright smudge of mismatched boots"
    "and a banner clutched between sunburned hands. Lucas's comms bracelet glints at the edge of her podium setup; his voice is already on the feed, calm and clear."

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Microphone hiss, followed by a hush as Elena steps forward]
    show elena_cruz at left:
        zoom 0.7

    elena_cruz "Thank you, everyone, for coming. We will hear presentations from both sides. Keep comments to the allotted time. Speak plainly, speak kindly, and remember this town's livelihood."
    "Narration"
    "Her words settle like a practiced weight. You feel the room lean forward. This is what you prepared nights for; this is where volunteer lists and seedling schedules meet public policy."

    menu:
        "Finger the brass clip on your notebook":
            "Your thumb rubs the worn metal until the engraved letters blur for a second. It steadies you — a private ritual that grounds the tide of nerves."
        "Breathe and open your hands instead":
            "You let the notebook rest in your palms, uncovered. The papers feel lighter for a heartbeat; you notice the damp smell of seaweed from the front row and the small green sign that reads 'Marshers for the Future.'"

    menu:
        "Ask Lucas to run the overlay publicly, with community participation":
            "You propose transparency: model runs live, community data streams into the analysis. The crowd shifts; a few faces relax at the promise of seeing numbers on the same screen."
        "Call out Atlantech's timelines and demand immediate safeguards for vulnerable families":
            "You pivot to people. A hush falls. Elena's jaw gives a small twitch—this is the politics she carries. The applause is warmer but the technical pushback is sharper."

    menu:
        "Invite Maren and Lucas to a public co-design session at the boathouse":
            "You propose a concrete meeting—dates, volunteers, and a live demo. The offer lands like an extension of a hand; some in the crowd nod appreciatively."
        "Declare that the town will start citizen monitoring regardless of corporate cooperation":
            "You affirm local agency. A cheer rises. Elena looks contemplative—this will complicate funding talks—but the crowd's energy spikes, people talking about seeds, sensors, and shifts they can make tomorrow."

    menu:
        "Negotiate publicly with Lucas and demand a hybrid plan.":
            jump chapter4
        "Lead a protest and community blockade at the seawall site.":
            jump chapter7
        "Fund a grassroots data campaign to expose flaws in the impact assessment.":
            jump chapter10
        "Contact a regulator and prepare a whistleblow/legal complaint.":
            jump chapter13
    return
