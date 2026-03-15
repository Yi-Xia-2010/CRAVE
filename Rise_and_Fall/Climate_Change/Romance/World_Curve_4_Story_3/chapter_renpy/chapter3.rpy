label chapter3:

    # [Scene: Council Chambers | Morning]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Quiet strings with a steady, hopeful piano undercurrent]
    # play sound "sfx_placeholder"  # [Sound: Soft murmur of the room, the high hum of the hologram overhead]
    "You step into the light-washed amphitheater with your notebook pressed to your chest. The chamber smells of rain-damp wool and disinfectant; the municipal coffee has a bitter, familiar comfort. The floor beneath your boots is cool and echoes each small decision as a click."
    "A cluster of faces waits: Councilor Anika at her panel, expressions from local organizers to corporate reps arranged in neat rows, and Jonah Reyes two seats down, his jacket rolled at the sleeves, bandana bunched in his pocket like a talisman. Professor Asha stands behind you, steady as a lighthouse."
    show professor_asha_rao at left:
        zoom 0.7

    professor_asha_rao "You know the models. Breathe."
    "She squeezes your shoulder once, no fuss."
    "You nod. Your cuffs—coral-stained from long days measuring berm cores—feel like a confession under the sterile lights. You smooth your jacket, although the salt stains won't come out. The holographic coastline shivers, and with a touch to the console the map blooms where your data will appear."
    hide professor_asha_rao

    scene bg ch3_98c6f2_2 at full_bg
    show mara_ellis at left:
        zoom 0.7

    mara_ellis "Councilor Patel, members of the council, neighbors—our community-based pilot is modeled on three years of tide data, sediment capture, and living-root retention studies. This map—' (you gesture; the berms glow) '—shows how distributed, nature-based interventions reduce frontal erosion and retain nearshore habitat, while lowering immediate displacement risk."
    # play sound "sfx_placeholder"  # [Sound: A soft click as the next slide pulses; murmurs of interest ripple.]
    "Jonah Reyes leans in beside you, catching your eye. His smile is small, practical—the kind that says he believes in what you're showing. You feel the familiar tug of steadiness from him: callused fingers on a model, the bandana at his hip, everything honest and worn."
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "If I can add—these structures are designed to be modular. They can be installed in phases to match funding and community input. They don't lock neighborhoods into displacement."

    mara_ellis "Exactly. Phasing means work crews from the neighborhood are employed first; monitoring is community-led. We scale with people, not just capital."
    show professor_asha_rao at center:
        zoom 0.7

    professor_asha_rao "And the monitoring plan includes independent verification and a city-held escrow for environmental outcomes. We can report quarterly to the council."
    "Councilor Anika leans forward, eyes sharpening. 'That's the implementation piece I'm interested in. Funding timelines, oversight—how do you ensure this isn't undercut by private contractors promising faster, cleaner results?'"
    "You feel the room tilt toward that question as if the air itself is heavier where NovaSeis's name lingers. Elias Crowe sits across the room, an immaculate presence with a set of polished models on a raised platform beside him. His smile is a cut of economy—measured, efficient."
    hide mara_ellis
    show elias_crowe at left:
        zoom 0.7

    elias_crowe "With respect, Councilor, when the stakes are metropolitan safety, speed matters. Our solutions are engineered to guarantee levels of protection within regulatory targets. You won't need to wait for years of incremental improvement."
    hide jonah_reyes
    show mara_ellis at right:
        zoom 0.7

    mara_ellis "Speed without ecological compatibility brings externalities. Seawalls can protect downtown but accelerate erosion elsewhere. We can't trade one community's safety for another's loss."
    "Elias Crowe's expression flickers—brief, like sunlight off steel. He answers smoothly, untroubled."

    elias_crowe "Our models account for redistributed stress. We propose compensatory measures. The city gets certainty."

    professor_asha_rao "Compensatory measures are often distant from the affected community. The ecological services that marshes and berms provide are not fungible—sediment capture, nursery habitat—those are local."
    "Councilor Anika narrows her attention between them, the scales of political pressure visibly adjusting in her posture."
    hide professor_asha_rao
    show councilor_anika_patel at center:
        zoom 0.7

    councilor_anika_patel "I need assurances on both risk and optics. If we move too slowly, voters will hold us responsible. If we move too fast, we risk legal and ethical fallout."
    # play sound "sfx_placeholder"  # [Sound: The hologram pulses; a low chime signals the start of the public comment period. The chamber whispers lengthen into individual voices.]
    "A woman from the back—Maya's voice, or someone like her—stands and speaks about the creak of her floors when the tides rise, about children learning to fish in new marsh channels. Her testimony lands like a pebble making rings."
    "You feel your logic and your stubborn heart braid together. The data isn't abstract here; it's living rooms and lunches and the smell of brine on someone's hair."
    "Jonah Reyes catches your hand under the table—a quick, grounding press. He doesn't need to speak for you to feel anchored."
    hide elias_crowe
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "Make it human. Start with who loses if we don't."

    mara_ellis "We should make the case with both charts and stories. The council needs facts they can defend and a narrative the public trusts."
    hide mara_ellis
    show professor_asha_rao at right:
        zoom 0.7

    professor_asha_rao "And a monitoring plan the city can sign onto—transparency matters. If we can show early wins, the political will will follow."

    menu:
        "Emphasize the human stories first: open with a resident testimony":
            "You call up a short clip from Maya's testimony—soft, immediate—and let it play through the chamber. Voices hush as the kitchen-laughter and tide sounds fill the glass room."
        "Lead with the data: show the model projections immediately":
            "You cue the model to the projected outcomes: erosion lines recede in staged visuals, and the chamber's attention tightens on the numbers rather than the noise."

    menu:
        "Adjust your tone to be conciliatory toward Anika's need for speed":
            "You soften your language, offering phased metrics and quick wins—something Anika can run on. The council relaxes; the applause is warmer."
        "Double down on accountability language, name trade-offs explicitly":
            "You sharpen your phrasing and cite case studies where quick engineering displaced communities. A few councilors frown; a handful of activists nod vigorously."

    menu:
        "Partner publicly with Jonah: propose a high-profile pilot together.":
            jump chapter4
        "Expose NovaSeis' proprietary trade-offs and lobby for accountability.":
            jump chapter7
        "Push for regulatory change: make the city adopt strict ecological adaptation standards first.":
            jump chapter10
    return
