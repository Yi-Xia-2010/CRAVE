label chapter1:

    # [Scene: Lowtide Marsh | Dawn]

    scene bg ch1_Start_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, hollow piano; distant, rhythmic heartbeat of tide]
    # play sound "sfx_placeholder"  # [Sound: Soft gull calls, the distant creak of an old piling]
    "You step onto the mudflat with the familiarity of a habit that has become ritual. The ground sucks once at your boot, a slow, damp tug—proof that the marsh does not forget who walks it. Your"
    "breath fogs in the cold; salt clings to the cuffs of your jacket and the curl of your hair. You pull the loose knot tighter, the sea-glass clip catching a thin slash of light and sending"
    "it across your palm like a small promise."
    "Your fingers find the battered field thermometer clipped to your belt before your eyes find the place you came to check. You unhook it, the metal warm and gritted with old salt. The bronze pendant at"
    "your throat—your grandmother's fragment—taps against the notebook on your hip when you kneel. You set the thermometer along the marked stakes, index the micro-variations, and trace the numbers in your head the way you used to"
    "trace tide lines with a child's patience."

    "The marsh is alive in small, stubborn ways: fiddler crabs waving comic, urgent flags; a trout ghosting a shallow pool; spartina grass bending in the faint wind. The light turns every shallow mirror into a painter's smear—gold, then pewter. You sketch with quick, economical lines, recording a cross-section of sediment and a note" "steeper edge, recent undercut."
    "You run a gloved fingertip along a fresh strip of exposed earth. The cut is too clean. It looks, in the open morning, like the wound left by last winter's storm—like the place that swallowed old"
    "Mr. Ortega's shed. You remember the shack's crooked roof half-floating down the channel and the way the town gathered with blankets and wry jokes to mourn a thing that felt too small to lose but looked"
    "enormous when gone."
    "A low, bitter taste sits with the memory. You remember the tide forecast you misread years ago, the night you called the wrong line and watched the bay flood a little sooner than everyone expected. It"
    "wasn't the storm that failed—you were; the forecast was your voice in the room, and it was wrong. The memory hums under each measurement now, a dull electric undercurrent. You press your thumb to the pendant,"
    "as if contact can steady the pull of recollection."

    menu:
        "Press the gloved hand to the undercut and test its give":
            "The mud is firmer closer to the spartina roots, but the undercut yields beneath pressure. Your glove comes away flecked with dark silt; the sound of it slipping fills your ears with a tiny, private alarm."
        "Flip to a clean page in your notebook and sketch the erosion":
            "You map the scar, label depth and angle, and write: 'monitor weekly.' The act of ordering notes steadies you, the graphite like a small, rational anchor."
        "Call out to whoever's nearby — maybe Eli — to see if he notices the new cut":
            "Your voice tosses across the pools and the gulls; a figure answers, feet slapping the planks toward the oyster racks."

    # --- merge ---
    "You notice Eli approaching between racks; the scene continues."

    scene bg ch1_Start_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Gull quarrel crescendos then settles]
    # play music "music_placeholder"  # [Music: Low strings swell with a cautious, unresolved chord]
    "Eli Navarro stands at the racks with the easy posture of someone who has counted tides more often than he has counted hours of sleep. He tucks the corner of a hand-marked calendar into the pocket"
    "of his vest and looks up when he hears you. You notice, as you always do, the way his eyes find the practical line: tide line, harvest marks, where the ropes have frayed. His hair is"
    "sun-bleached at the ends and his shirt smells faintly of smoked fish and the morning."
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "You found it, then. Thought I saw you headed for the old pilings. How deep is it?"
    show maya_rios at right:
        zoom 0.7

    maya_rios "About half a metre, undercut starting at the root line. It gave a little when I pressed.' (You keep your voice low; facts are something you can hand to the town without giving them your fear.) 'We should tag this and set a marker. Track it through the next three tides. If it's progressive, it's more than ordinary scouring."
    "Eli Navarro studies the scar, then the calendar in his hand. He fingers a corner as if it has memory in it, then shakes his head slightly."

    eli_navarro "Half a metre eats an oyster bed if it keeps going. The kids down on Dock Four already said yields were down last month. Mayor's meeting's this week, right? You going to show them this?"

    maya_rios "I will. I keep detailed records.' (You pronounce the sentence with more certainty than you feel.) 'Community data matters more than headline promises. We need to show trends—before, after, correlation with storm events. Anecdotes won't cut it when Aquila brings their model in a box."
    "Eli Navarro's jaw tightens at the name. He slides a callused hand across an oyster shell, the motion habitual and somehow protective."

    eli_navarro "Aquila's already sent a rep through town. Cass Adler. Pretty model, slick talk. They've got renderings and colors. Said they'd 'future-proof' the coast. Mayor's been—' (he stops, looking at the calendar again) '—Mayor wants options that don't look like doom. Problem is, Aquila's idea means a lot of people losing their say."

    maya_rios "Models are tools. They can be useful—if they include the right inputs and if someone on the ground reads them with local knowledge.' (But inside your chest, the hum is louder. Models can also look right on paper and break things in practice. You've seen maps that promised safety and delivered dislocation.) 'If Cass shows up with shiny renderings, we bring numbers. Long-term salinity trends, sediment budgets, the community's cost estimate for managed retreat versus hybrid restoration. We make them answer to the people who live here."

    eli_navarro "You think they'll listen?' (He looks at you, and for a second the caution in his face softens with something like hope.) 'Because I want them to. I want a plan that keeps our beds and our families."
    "Your throat tightens. There's a part of you that wants to tell him about the forecast that went wrong, the misread tide that left you hollow and small beneath the map lights. But the town cannot"
    "afford the luxury of private confessions right now; they need steady data and clear recommendations."

    maya_rios "They should. We make them. And we keep saying 'why this, why this, why now' until they answer.' (You pause, and then: softer.) 'I don't have all the answers. I have records, and I have the marsh. That's where we start."
    "Eli Navarro gives a low, half-amused sound that is closer to a laugh than you've heard from him lately."

    eli_navarro "That's your M.O., isn't it? Measures and patience. Fine. But when you start handing out diagrams, I want to hand out the stories too. People remember things when they're told by someone who lives them. Between the two of us, maybe we make them listen."

    maya_rios "Between science and stories, maybe there's a place for both. Or at least a way to make the numbers stick."
    "Eli Navarro's eyes flick to your pendant as if noticing something in the motion you make with your hands. There's a softness in him — not pity, but a recognition of the weight you carry."

    eli_navarro "You okay, Maya? You look... quieter than your notebooks."
    "You almost tell him about the forecast. Instead you fold the feeling inward and let the reasoned part of you speak."

    maya_rios "I'm fine. Quiet is good for listening to the marsh."

    menu:
        "Share the old forecast mistake with Eli, lay it out plainly":
            "You weigh the words. Saying it would let the past out of the looped cassette in your mind, but it might shift the focus from the present evidence to personal doubt. Eli already knows you don't skirt facts—if you tell him, he won't judge. He'll hold it like wet wood, steady, but you'll both smell the smoke."
        "Keep the mistake to yourself and focus on this morning's data":
            "You tuck that old error into the fabric of your resolve and wear it like a weathered coat. It slices, but it also shields. You hand Eli the latest measurements instead, letting action drown the hum for now."

    # --- merge ---
    "You and Eli prepare to head toward the meeting; the scene continues."
    "Eli Navarro hoists a crate of oysters, the motion efficient. He glances at the distant line of town where roofs sit like a few borrowed breaths above the water. The thought of Aquila's model being unpacked in the town hall creates a low, sour taste in your mouth."

    eli_navarro "We should go—get to the meeting, bring the racks, bring people. Make it messy. Make it inconvenient for the suits. Make them sit in our damp and tell us how pretty their plan is while we mop salt off their shoes."

    maya_rios "Make them uncomfortable,' you agree, and the phrase tastes of resistance. 'We document, we bring witnesses, and we ask exact questions. Who controls the maintenance? Where does the funding lock local voices out? What's the long-term impact on sediment movement? We ask them the math and we ask them about lives."
    "Eli Navarro's mouth quirks; in the open air, there's a brief thing between you, not yet named, a mutual tether forged by long work and harder losses."

    eli_navarro "Good. We fight pretty and polite. And when the coffee runs out, we get louder."
    "The gulls throw themselves into argument again overhead, their cries like punctuation. You make one last note in the notebook—neat numbers, an arrow, a small diagram—and close it with a hand that steadies your elbow against the cool, salt-rough wood of a nearby piling."
    "Your resolve is not sudden fireworks; it's the small, granular kind: keeping records, listening, not letting glossy promises drown out local memory. The morning's beauty does not soothe the gravity of what could come. Instead it sharpens it—gold light on silver water, the hard clarity before a storm."
    "You stand, the marsh at your feet and the town behind you, and the old shame still hums, but now it shares space with a plan: document, question, bring people. The knowledge that you were once"
    "wrong sits with you like a stone you can either keep or set down. You choose, for now, to carry it into the meeting as a reminder of what happens when forecasts are treated as absolutes."
    hide eli_navarro
    hide maya_rios

    scene bg ch1_Start_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant, rhythmic clatter of a shipping crate — a town's heartbeat preparing for assembly]
    # play music "music_placeholder"  # [Music: The piano drops into a minor chord, lingering, unresolved]
    "You loosen the knot in your hair and feel the cold on your neck. There are things to do: gather data, rally neighbors, stand in halls and ask sharp questions. The marsh keeps its small life, and you promise silently to do what you can to keep it that way."
    "There is a box on the dock, someone told you—a scale model inside, made to show what Aquila calls 'resilience.' It will arrive at Harborfront Lane before noon. The town will gather. Voices will rise. You"
    "tuck your notebook tighter and start toward the boardwalk, each step a metronome toward the meeting where maps and lives will collide."
    "The gulls scream once more, and you carry the sound with you like a cue: an abrupt, high note that pulls your thoughts forward."
    # [Page-turn thought: You want the town to listen to the marsh, but you know listening will demand more than attention; it will demand choices you cannot rehearse. The tide will come, and when it does, the town will have to decide who holds the maps and who keeps the memories.]

    scene bg ch1_Start_4 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter2
    return
