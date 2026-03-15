label chapter19:

    # [Scene: Promenade | Night — Storm Approaching]

    scene bg ch12_16e9b2_1 at full_bg
    # play music "music_placeholder"  # [Music: Rapid percussion, high strings — urgent, driving]
    # play sound "sfx_placeholder"  # [Sound: Wind gusts like an animal through wooden slats; distant metallic groan of stressed pylons]
    "You press the compass flat against your palm because you need something solid to hold. The cord bites into your skin as rain begins to smear the Promenade into a single, moving gray. You can feel"
    "the decision from the night before embedded in your joints: we would act. You promised action. That promise is a rope tied around your waist now, and the tide is pulling."

    "The Beacon blinks. An alert tone—clean, clinical—cuts through the wind and prompts a dozen hands into movement. Marta's voice snaps orders like a whip" "Tethers. Two to each line! Check knots! Noah—bring the extra harnesses!"
    "You run."

    scene bg ch12_16e9b2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Slosh of water at shins, the hollow thud of feet on soaked wood, rope creaking]
    # play music "music_placeholder"  # [Music: Percussion intensifies; a single brass stab punctuates each collision between people and wind]

    "Eli hauls a plank like it weighs half his age. His jaw is set, and his hands are blistered and raw; wood dust hangs on his forearms like a talisman. He doesn't look up when you reach him, only shifts the load and mutters" "Keep it against the bulkhead—press—don't let it slit."
    "Noah Reyes is a tether-line man, voice clipped, efficient, every motion measured. He ties a frightened teen to a line with hands that are trying to be steady for reasons beyond the moment: mothers lost apartments,"
    "promises made and broken. He looks at you when you approach, and for one fraction of a breath the world narrows to the two of you and the wet static in the air."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "Thought you'd be on the west flank. Marta sent me to pull people off the pier—too many looking for the old lights. You—where do you need me?"
    "You answer and then don't, because there is a list inside your head: sandbags, reed mats, sensor redeployment, Lila Park's crews where they stand and where they don't. The list is alive and moving; it flares with priorities and the knowledge that each choice will cost something."
    "You dart between tasks. Your jacket is soaked; the compass swings like a pendulum over your sternum. You fold sandbags as if folding the town into your hands; you sling mats across thin, cold water and"
    "feel the reed fibers bite into your palms. Every time the wind takes a breath, the sea throws itself at the boardwalk like a fist."

    menu:
        "Take a moment to secure the old compass to your jacket":
            "You fashion the cord into a tighter knot around the lapel. The compass won't slip if the night snags you; it becomes less an heirloom and more a safety tether."
        "Leave the compass loose; move faster without thinking about it":
            "You stuff the compass beneath your jacket, trading the certainty of its weight for quicker reflexes. It rattles against ribs like a quiet alarm."

    menu:
        "Go with the composite team and try to supervise their placement":
            "You step into the tight choreography of engineers and contractors, wedging yourself into the line of sight between their machines and the water. Your presence forces them to meet the town's gaze, at least for a few minutes."
        "Stay with the marsh team, shifting manpower to reed and root work":
            "You stay elbow-deep with volunteers, the salt in your teeth and the reed fibers cutting your fingers. The work is slower, more human, and leaves you raw with its intimacy."

    menu:
        "Stay and force a joint audit at dawn—demand immediate log access":
            "You stay, voice hoarse, making people swear to meet at first light. A small, fierce community of witnesses forms around the Beacon, tired and raw and not yet willing to let the night tell its own version of events."
        "Push to get everyone away from the waterline now—leave accountability fights until morning":
            "You order retreat. People pull back, sodden and shocked, guided by your necessity. Accountability becomes a future thing; for now, survival comes first."

    jump chapter22
    return
