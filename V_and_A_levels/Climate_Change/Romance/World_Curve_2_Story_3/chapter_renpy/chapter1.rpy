label chapter1:

    # [Scene: Laurel Bay Tidal Flats | Late Afternoon]

    scene bg ch1_Start_1 at full_bg
    # play music "music_placeholder"  # [Music: Soft, warm ambient—low piano with distant gulls]
    # play sound "sfx_placeholder"  # [Sound: Gentle lap of far-off tide; a wooden board creaks underfoot]
    "You step off the boardwalk and the flats open under your boots — a shallow mirror holding the bruised gold of late light. Salt tangs the air, bright and bitter; somewhere underfoot the mud sighs as"
    "it settles. Your buoy pendant rests heavy against your sternum, the thread warm from your skin. You feel its small weight as if it's the memory of a hand, something to hold onto while the horizon"
    "rearranges itself."
    "You breathe in the bay: wet wood, the faint iron of old nails, the green clean of seaweed. The town is quieter than it looks — people at work, conversations folded low, the festival still weeks"
    "away but already humming like a distant tide. Rumors of the municipal resilience plan move through the market and the docks like undertow: seawalls, raised roads, managed retreats. They stay at the edges of people's sentences,"
    "named and un-nameable at once."
    "You don't push the rumors down; you tuck them into your pocket like another tool. They must be met with plans and with people. A plan might save houses, but a plan isn't a livelihood. That thought sits alongside your father's buoy, steady and unobtrusive."

    scene bg ch1_Start_2 at full_bg
    # [Direction cue: Slight camera pull toward a solitaire figure]
    # play sound "sfx_placeholder"  # [Sound: A distant metal clink as a wind-worn sign rocks]
    "Elias Kato stands a distance away, trench coat buttoned against the salt wind. The coat keeps its lines even where the world is frayed; he looks like a man used to maps and margins. His amber"
    "eyes are narrowed against the light. When your gaze catches his, there is a shift — small, contained. Memory flickers: study nights with ramen, quick debates over tide charts, a laugh that broke a long silence."
    "The memory is both close and distant, like a shoreline you once walked and have not yet returned to."
    "You feel that private ache — not sharp, more a hollow light — and then it softens into something steadier. You're home. You have work to do."
    # [Scene: Glasshouse Lab & Seedbank | Early Evening]

    scene bg ch1_Start_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of pumps; soft drips from a condensation catcher]
    # [Smell: Warm, humid air; faint algae sweetness]
    "You push open the painted door and the greenhouse breathes out a humid, chlorophyll-sweet sigh. The light here is close and forgiving; moss-green shadows stretch between seedbank shelves. The brass of your pocket spectrometer is cool"
    "at your hip. Kaori 'Kai' Matsuda is there before you, sleeves rolled, hair with blue tips plastered in damp strands, a drone pad open and quiet at her feet."
    show kaori_kai_matsuda at left:
        zoom 0.7

    kaori_kai_matsuda "You're on time. Or early, which is the same thing for you. How was the walk home?"
    show marina_reyes at right:
        zoom 0.7

    marina_reyes "Quiet. The flats were generous with light. And your drone didn't fly off into the sunset?"

    kaori_kai_matsuda "Not today. I bribed it with leftover kelp chips. It's a cheap crowd-pleaser."
    "You both move between racks. The seedbank is arranged with the kind of tidy obsession that soothes you: labeled jars, packets sorted by strain and source, a row of numbered sample trays humming under soft LEDs."
    "Your fingers find the same shelf where your father's notes used to sit — the handwriting, the shorthand sketches of long-line rigs — and you pause."
    "Kaori 'Kai' Matsuda watches you, then nods toward a shelf label as if sharing a small, conspiratorial map."

    kaori_kai_matsuda "We checked the spores from the southern straights this morning. Viability's good. Thought you'd want to see — old Tom's batch was surprisingly clean."

    marina_reyes "Tom's batch did better than we expected? That's a small mercy."
    "You let a breath out that tastes a little like relief. 'Show me.'"
    "Kaori 'Kai' Matsuda bends the lamp's angle. The trays reflect a thousand tiny flecks: beginnings. You run a thumb along the rim of one tray, feeling the cool, algal film under your skin. Expertise comes like"
    "muscle memory — a rhythm of hydration, light, and time. You name things silently as you work: cadmium-tolerant strains, a slow-growing filament, a spur of promising spores. Names are small reclamations."

    kaori_kai_matsuda "Rina keeps calling the council about public messaging. People want certainty, or at least a map to point at. You? Still thinking cooperative long-lines?"

    marina_reyes "Yes. If we can anchor local jobs to restoration techniques, we keep people here. And kelp buffers will buy time. They're not the same as sea walls, but they do work — in places, at least."
    "You pause, looking down at the trays. 'It's a start.'"

    kaori_kai_matsuda "Start is good. Start is more than words. We'll need volunteers, some small funding, maybe a booth at the festival."

    marina_reyes "The festival would be perfect. Show the town what a living shoreline looks like. Let them taste it, see the tools."
    "You smile, thinking of Amalia's lanterns and the smell of smoked fish. 'We plant the first long-line before the last week of festival prep. Technical, but doable.'"

    menu:
        "Check your father's field notes":
            "You pull the worn notebook from the satchel, thumb over diagrams of a long-line. The paper is damp at the edges. Reading it calms a welt of nervous energy."
        "Tell Kaori \'Kai\' Matsuda about the municipal rumors":
            "You lean closer, voice low. As you name the seawall and managed retreat, Kaori \'Kai\' Matsuda's face tightens — but she nods, arms already folding into plans."

    menu:
        "Sketch the long-line plan now":
            "You pull a spare page from your field notebook and draw a rough schematic: anchor points, staggered depths, a note to test salinity at dawn. The diagram hums with possibility."
        "Call Amalia to reserve a festival stall":
            "You tap Amalia's number and leave a short message: 'Reserve a demo space. Kelp demo, volunteers, post-sunset.' You can hear her already planning lantern placements."

    jump chapter2
    return
