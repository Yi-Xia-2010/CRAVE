label chapter12:

    # [Scene: Lowtide Marsh | Night]

    scene bg ch10_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft suck of mud against boots, the clink of metal cages, a distant gull cut off by wind]
    # play music "music_placeholder"  # [Music: Low, taut strings—a single cello line that tightens when the tide moves]
    "You taste salt and cold. The marsh is louder at night: tiny creatures clicking under the mud, the soft slap of water against an old piling, the sound of neighbors’ breath as they move in time"
    "with you. Your palm knows the feel of wet rope; it remembers where to hold so the oyster cage doesn't tilt and spill the new clusters. The bronze pendant at your throat swings once and keeps"
    "time with your heart."

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low murmur—people naming tools, a terse laugh, the scrape of a shovel]
    "This is the work you chose: small muscles changing the curve of the marsh. It is illegal, yes—no permits, no stamped plans—but it is honest, and for a few hours their faces look tired and fierce"
    "in the headlamps, not like criminals. They are trusted neighbors: a woman whose son you taught to read tides, a retired deckhand who keeps time by the rhythm of his lungs. They don't need their names"
    "said aloud; the salt in the air is their witness."

    "Neighbor" "Careful—it's deeper here. Tie the second line."
    show maya_rios at left:
        zoom 0.7

    maya_rios "Got it.' You loop the rope around the cage, fingers numb but practiced. 'Lean on me when we lift."
    show eli_navarro at right:
        zoom 0.7

    eli_navarro "Steady."
    "he says, and his voice is low enough that only you feel it. There is something protective in the way he stands a hair back—ready to take weight if the cage slips, ready to argue with"
    "the law if someone asks questions. You look at him: the brim of his cap wet, the rope bracelet pulling at his wrist like a small, familiar knot."

    maya_rios "You didn't have to come."

    eli_navarro "And leave you to single-handedly harpoon a tide? Not a chance."
    "He glances toward the low horizon where thunder is a dark bruise. 'Besides—someone needs to remind you to stop when it's stupid.'"

    maya_rios "It is stupid sometimes.' The admission tastes of old guilt. 'But sitting in the annex and writing reports felt more like locking the marsh in a binder. This—' You sweep a hand, splattering cool mud. '—this feels like teaching it to breathe again."

    eli_navarro "Then we teach.' He bends to the sandbags, lifting with you. 'But we do it smart. No obvious lines, no pyrotechnics. Slow, small wins."
    "You move as a unit. You and Eli haul cages; you tuck new spat into mesh pockets like fragile promises. You mound sand where the sill has thinned, tamping until your shoulders ache. You plant spartina"
    "plugs in tight rows, watching their roots take hold in the churned mud. Each small act is a vote thrown into the marsh's ledger."

    menu:
        "Tie an extra safety knot on the second cage":
            "You take a breath and tie the second knot—double loop, cinch—because the cage would mean too much to lose. Eli gives a brief, approving nod."
        "Move faster and leave it as-is to save time":
            "You choose speed. The cage goes into place with fewer hands, and for an instant you convince yourself adrenaline will net less risk. Eli's jaw tightens; he says nothing, but his fingers press your forearm for a second."

    # --- merge ---
    "The scene continues."
    "The work is soulful, yes—the kind that rearranges something inside you. When you press a spartina plug down and the mud closes around the stem, you swear you can feel the marsh answer back: a small"
    "settling, the hush of water finding a new channel. In a few shallow pools the water clumps with shell-slick life; fiddler crabs appear like punctuation, and somewhere a distant fish sends a bright, surprised ripple through"
    "a reflection."

    eli_navarro "Look at that,' he murmurs, half to himself. 'A small thing, but it matters."

    maya_rios "You always say that.' The words come softer than you expect—an echo of everything he's taught you about incremental stewardship. Then, because you need it named, you add: 'Thank you."

    eli_navarro "Don't get soft on me.' He smirks, but his eyes stay honest. 'We need you sharp. The state will come sniffing."
    "His warning doesn't land as news—you already know storm patterns and legal teeth—but it pulls a dark vein through the night's work. The forecast in your pocketed phone glows when you check it: low barometric pressure"
    "marching toward you, a small line of predicted wind that could come sooner than expected. You feel that old undertow—the misforecast memory twitching in your sternum—and for a moment, your hands hesitate on a sandbag."

    "Neighbor" "Heads up. Lights—off in the bay? Or is that a patrol?"
    # play sound "sfx_placeholder"  # [Sound: A thin, mechanical whine—too regular to be gulls, too close to be the usual harbor traffic]

    menu:
        "Signal the team to hold quiet and watch":
            "You hold a finger to your lips and the group freezes like a tide line. Headlamps dim; only moonlight remains. You count heartbeats while you listen. Eli leans in, jaw set."
        "Wave and call out to sound like you're part of a permitted crew":
            "You raise your arm in slow, practiced motion and shout, 'Working through the night—permit on file!' It sounds like a lie even to your ears. Two heads pop up along the marsh edge; the sound of boots changes slightly, more curious than confrontational. Eli's eyes flash—he's not convinced."

    # --- merge ---
    "The scene continues."
    "You choose. The marsh holds its breath with you. For two minutes nothing happens but the night and your breathing. Then the whine recedes—either an engine taking a wider arc or a false alarm—but the knowledge that there are eyes and scanners out there remains. Your stomach tightens."

    eli_navarro "We need to be careful about evidence,' he says, whispering. 'Remove obvious footprints at the access path, spread the sandbags more like natural drift."

    maya_rios "Agreed."
    "Dawn finds you exhausted and exhilarated. The new patches are visible if you know where to look: subtler water flow, a shelf of sand catching detritus, clustered spat bunched behind a moved cage. Some of the"
    "tide pools are already clearer, the water threaded with small, new life. You feel a fragile triumph—quiet and furtive."
    hide maya_rios
    hide eli_navarro

    scene bg ch10_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A faint rustle of paper slapped against a post in the harbor—news, announcements]
    "Then the notice pins itself to the town's bulletin board like a weight. You don't see it first; someone else—maybe the retired deckhand—reads it aloud in a voice that goes dry."
    # play sound "sfx_placeholder"  # [Sound: Paper flapping in the weak wind]

    "Neighbor" "'Notice of Unauthorized Modifications to Public Wetlands—Removal or Alteration Prohibited. Failure to cease activity may result in fines or enforcement action.'"
    "The words are clinical and precise. They are the machinery of the state, a bureaucracy that flings sanctions like nets. You feel the blood drain away from your small victory. Where you had smoke and warmth and movement, law places a measured, cold hand."
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "They found out."
    show maya_rios at right:
        zoom 0.7

    maya_rios "It wasn't meant to be a confrontation.' Your voice cracks on the last word. You curl your fingers into your notebook in your jacket until the page edges bite. 'We were trying to show a way."

    eli_navarro "I know.' He looks at you—no judgment, only something complex and unreadable layered over loyalty and fear. 'But you know how this goes. Notices are the first step."
    "You think of the bronze pendant at your throat, the little fragment of your grandmother's locket that has been heavy and warm at every choice you've made. It feels heavy now, as if the metal remembers"
    "other storms. The marsh at your feet looks at you as if it has a memory longer than any posted notice."
    hide eli_navarro
    hide maya_rios

    scene bg ch10_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant, mechanical thrum—security lights sweeping the harbor; the hush before orders are given]
    # play music "music_placeholder"  # [Music: Strings swell into a minor key—resigned, inevitable]
    "The exhilaration of action cools into a precise, almost surgical dread. Aquila's security presence has become more visible in the last days: low-profile vans idling at the edge of town, a drone's distant blink like an"
    "artificial star. Now the armature of enforcement turns its attention to the small, bright work you've done by hand."
    "You stand there with mud under your nails and a page of illegal hope tucked in your jacket. The fall begins not with a shout but with a notice pinned to a board and the hum of engines gathering."
    "You reach for the pendant and close your fingers around the worn metal. The marsh needs you to decide what comes next, but that decision will not be only yours. The state is already calculating levers"
    "and laws you will have to reckon with. You feel, in a new and colder way, the shape of consequences closing like the tide."

    scene bg ch10_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The paper's clack against wood, a distant radio voice—indistinct but urgent]
    # play music "music_placeholder"  # [Music: A single, unresolved piano chord lingers]

    scene bg ch10_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter13
    return
