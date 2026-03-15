label chapter5:

    # [Scene: Civic Rooftop Garden | Morning]

    scene bg ch5_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Low cello, slow and minor; sparse high strings like breath]
    # play sound "sfx_placeholder"  # [Sound: Distant gull cry, a far-off siren that dies into the hour, wind threading through lanterns]
    "You climb the last short flight of stairs and the town opens and shrinks at once beneath you: the boardwalk's splintered boards, the cafe awning flapping like a torn flag, the pale, institutional outline of the"
    "Arcology site looming beyond the harbor. The satchel at your shoulder is heavier than it should be — maps inside, reams of notes, a pair of printed flyers with a smear of mud on the corner"
    "— and the brass compass at your throat feels impossibly cold."
    "Your hands still smell faintly of smoke and chalk. You think of the whistle at your lip two nights ago, sharp and ridiculous against the deep roar of so many throats; you think of the drone's"
    "red eye tracing your face; you think of how quickly righteous noise can calcify into something else. Your mouth tastes like metal and salt and the after-voice of a crowd. You have to put all of"
    "that somewhere."

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft crinkle of paper, someone rubbing a bruise on their knuckle, a murmur that is almost a new kind of argument]
    "Kai Solano is there first in sightline — shoulders hunched forward, one palm flat on the corkboard. He slams his fist in a way that makes the whole board shiver; plans, sketches, and a handful of"
    "torn flyers flutter. His jaw is set; the amber in his eyes is a live wire."
    show kai_solano at left:
        zoom 0.7

    kai_solano "You told them to be patient, Aria. You said 'work with the system.' Did that feel good when the cops were blocking our way at Third and Dune?"
    show aria_marin at right:
        zoom 0.7

    aria_marin "It wasn't 'good.' You know that, Kai. You know why we—"

    kai_solano "You know why? Because you were trying to make everyone comfortable. We needed disruption. We needed to break the narrative that says we don't matter."
    "You can hear the conviction in him — the same conviction that once bolstered your own courage. But anger sharpens it into accusation. The corkboard creaks under his hand; a thumbtack skitters to the decking."

    menu:
        "Step between him and the board, hold his arm gently":
            "You place a palm at the base of his wrist. The heat of him is immediate. He flinches almost involuntarily, then lets out something that might be a laugh or a sob. His shoulders loosen a fraction."
        "Let him speak and keep your distance":
            "You stay back, folding your hands into your jacket. He unloads, and hearing it without interruption pinches at you — part guilt, part a curious, thin relief. There is a rawness in the sound that you don't want to own, but you do."

    menu:
        "Pull out the timeline from your satchel and point to the milestones":
            "You unsnap the satchel, produce the folded timeline. Numbers and dates look infantilized in the wake of bruises and broken glass. Kai snorts but leans in; Noah scans it with a thumb that betrays interest."
        "Close the satchel and put the map away, speak from your chest":
            "You close the satchel. The paper rustles like a small animal settling for shelter. You say what you feel, and for a moment it lands raw in the air: a confession more than a plan. The group hears it; the silence that follows says as much as any nod."

    menu:
        "Say nothing more and let them speak first":
            "You fold your hands and keep your mouth shut. Voices rise and fall; positions reveal themselves like mapped currents. You learn things you didn't know: alliances and fissures that might change the calculus."
        "State clearly you will not be passive — propose a compromise framework":
            "You outline a skeletal framework: timelines, safeguards, and community oversight. Faces shift, some softening, some hardening. The air tastes of negotiation and the ache of necessary losses."
        "Ask for a vote among those present to pick a direction":
            "You ask for a small vote. Hands go up — some trembling. The tally will be imperfect, but it forces the group to bear the responsibility. The act of counting makes decision feel more real and more dangerous."

    menu:
        "Double down with Kai — escalate protests and occupy the site until demands are met.":
            jump chapter6
        "Accept Noah’s offer to fast-track engineered protections in exchange for stronger tenant safeguards.":
            jump chapter11
        "Propose and force a pilot: living shoreline plus a community-managed protective berm, timed to pause construction.":
            jump chapter19
    return
