label chapter6:

    # [Scene: Living Dike — Estuary | Predawn, storm front approaching]

    scene bg ch6_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind screaming through cordage, a steady, bone-deep thrum as waves hit; distant PA blares evacuation instructions.]
    # play music "music_placeholder"  # [Music: Low, sustained cello; a minor chord that refuses to resolve]
    "You came here on the high of last month's builds — hands blistered, laughter like a benediction, the community folding itself into something stubborn and alive. That memory sits beside the present like two photographs glued back-to-back: one sunlit, one flooded."
    "Now the photoshopped brightness of the memory drains. Water smells metallic and briny. Your jacket is soaked through to the elbows; salt cakes in the seams of your boots. The living dike is not a single"
    "wall but a hundred compromises: coir, willow stakes, borrowed sandbags, muscle, and faith. Some stretches have held; others look like someone scored them with a knife in the night."
    "You can hear them before you see them — the lab radios chirping, Rosa's voice clipped with urgency, the mayor's command tone threaded through static. You press your palm to a mud-slimed post and let yourself be practical: triage where you can, call evacuations where you can't."

    scene bg ch6_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Crack of loose timber popping free]
    "Elliot Chen crouches near a sensor mast, sleeves rolled, grin gone slack with concentration. He squirts a sealant you recognize and presses a palm against a water-logged circuit board. The prototype wristband on his forearm glows an anxious red under the spray."
    show elliot_chen at left:
        zoom 0.7

    elliot_chen "We held the upstream reed bed, at least for three cycles. The southern splice — where the dredge cut last year — it's overtopping. If it tears, the headland will funnel the surge straight into the old fishplots."
    show maya_ibarra at right:
        zoom 0.7

    maya_ibarra "Can the auxiliary barriers take the load if we re-route the outflow?"

    elliot_chen "Not without more coir and a berm. We don't have that mass anywhere near here. We patched what we could with volunteer teams, but —"
    "You watch his jaw work. He has always been the rational map in a storm of feeling; now you can see him crumbling into the weather. You think of the plans he'd sketched on greasy paper,"
    "of his hands mapping solutions on your palm months ago. You reach for something steadier than Web of data — a gesture that won't fix the dike but will hold the human piece of it."

    maya_ibarra "Tell me where to put people first. Sensors second. We'll come back to the circuits."

    elliot_chen "You'd leave the mast?"

    maya_ibarra "I won't leave the lab unmonitored. But here, now, the priority is people. Let me coordinate the shoreline sweeps."
    "Elliot Chen's eyes flash something like relief and guilt at once. He nods, and the motion is an agreement that tastes like compromise."

    menu:
        "Run with the frontline team into the marsh to help shore the failing southern splice":
            "You slog through waist-high reeds, mud sucking at your boots. You and two neighbors jam coir logs into a gap, fingers numb but purposeful; a wave slaps over the top and for a few heartbeats the world feels balanced."
        "Hold back to coordinate evacuations and direct teams from a safer ridge":
            "You stand on higher ground and shout directions into the wind; you route people to dry houses and ferry points. From here you watch the splice struggle — you are not hands-on, but dozens move because of your voice."

    # --- merge ---
    "Continue with the rupture sound and the southern splice failing."
    # play sound "sfx_placeholder"  # [Sound: A dull, rupturing sound as a section of aged seawall groans]
    hide elliot_chen
    hide maya_ibarra

    scene bg ch6_4001e7_3 at full_bg
    # play music "music_placeholder"  # [Music: String tremolo; heartbeat percussion]
    "Noah Rhee appears at the end of the boardwalk, salt-streaked and furious in a way that is practical as a storm: all edge and direction. He sees the breach, then sees you, and for a moment the world narrows to the two of you."
    show noah_rhee at left:
        zoom 0.7

    noah_rhee "You promised we wouldn't be left holding nets in a drained marsh. You promised that."
    show maya_ibarra at right:
        zoom 0.7

    maya_ibarra "We didn't promise miracles, Noah. We promised to try — to keep people fishing, feeding themselves — to keep the marsh alive."

    noah_rhee "The marsh is alive until a tide like this tells it otherwise. You and your 'try' couldn't keep the contractors from stripping that swamp last winter. You should have stopped them — when you had the chance."

    maya_ibarra "I — I know I couldn't stop everything. We fought, and we won some places. We saved—"

    noah_rhee "Saved some places."
    "His bitterness is a shield. You want to tell him you see him, that you understand the fear behind the fury; instead you fold the impulse into work. There are mothers to move, a child who"
    "can't find a boot, a generator to bring down the hill. Compassion must be rationed like dry bread."
    # [Scene: Beacon Lighthouse | Mid-morning, storm hitting its stride]
    hide noah_rhee
    hide maya_ibarra

    scene bg ch6_4001e7_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Beacon thrumming; rain against the windows is a steady white noise]
    # play music "music_placeholder"  # [Music: Sparse piano, low and patient]

    "Mayor Cortez" "This is Mayor Lianne Cortez. All evacuation routes remain open. Do not attempt to return until we've secured structural assessments. Also—due to damage to several commercial piers and ongoing legal holds related to Veridian Holdings, I am invoking emergency municipal oversight. Certain fishplots will be temporarily reallocated for community distribution. Some private docks may be condemned. We will form a stewardship council to coordinate long-term governance."
    "You let the mayor's words settle like silt. 'Temporarily reallocated' has the same cadence as 'you'll never get your plot back' to the people who cut their living from those waters. You can already hear the"
    "grinding teeth of small businesses, the prayers of families who have leased plots for generations."
    show maya_ibarra at left:
        zoom 0.7

    maya_ibarra "Mayor, are these condemnations permanent? What's the timeline for the stewardship council?"
    "Mayor Cortez [over radio]: (a pause, a breath you hear even through the bleed of storm) 'We don't have good timelines. We're building one. The council will include representatives from labor, ecology, and local fishers. We"
    "will seek phased relief funds and binding protections for the marsh. This will cost—' (she swallows) '—everything. We'll present a plan by sundown. I'm ordering legal holds on Veridian's escalated contracts until we know the environmental"
    "assessment.'"
    "Your chest tightens; legal holds are shields but also chains. 'What about fishermen with rents due? Food on their tables?'"

    "Mayor Cortez" "We are coordinating emergency grant disbursements. Rosa's documentation has helped the case — keep filming. Tomas will shepherd the elders into consultations. We need evidence and stories. We need—' (her voice falters with the weight) '—we need to be fair, even if fairness demands harsh tradeoffs."
    "There is a human tremor in her official cadence. She is doing what mayors must do: choosing the least-bad path and living with the ugliness."
    # [Scene: Docks | Early afternoon, after a high surge]
    hide maya_ibarra

    scene bg ch6_4001e7_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: People calling to one another, the distant wail of a horn; the creek of compromised pilings]
    # play music "music_placeholder"  # [Music: Low brass; a chord full of loss]
    "You walk the ruined slips with Noah Rhee at your side, though his distance is palpable. You step carefully over a roped-off box of salt-cured fish, the glinting eyes looking like tiny moons. Rosa moves through"
    "the wreckage with her camera like a suture needle, catching frames to stitch into the mayor's paperwork. Her face is grey; she is working with a competence that steadies you."
    show noah_rhee at left:
        zoom 0.7

    noah_rhee "They want to condemn this. To declare it unsafe. They'll use insurance to fold everyone's leases into a corporate package. Veridian will buy up plots cheap while we're rebuilding."
    show maya_ibarra at right:
        zoom 0.7

    maya_ibarra "The mayor said there will be community oversight. We can push for first-refusal clauses on any sales. We can write terms that favor locals."

    noah_rhee "We can write the best terms and they'll ignore them when the tide comes again. Words won't pay for nets when the fish don't return."

    maya_ibarra "Then we make the marsh work for the fish again. Regrowth, managed dredging, seasonal closures —"

    noah_rhee "All that takes time.' He steps closer, his voice softer but brittle. 'Time is what we don't have."
    "You see, here, in this exchange, the fault line between you. Both of you love this place with hands so different they sometimes collide like tectonic plates. You have spent months bending toward collaboration. The storm cracks open a raw, old wound."

    noah_rhee "I'm not asking you for patience, Maya. I'm asking for survival."

    maya_ibarra "And I'm asking you to trust that survival can include the marsh. We can't jetison it and expect the sea to be kind."
    "Noah Rhee's face hardens and then loosens into something like sorrow. He walks away without seeing if you follow. The boardwalk planks under his boots sound final."
    # [Scene: Tidewatch Laboratory | Late afternoon, after the surge recedes]
    hide noah_rhee
    hide maya_ibarra

    scene bg ch6_4001e7_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The intermittent beeping of surviving sensors; muffled conversation; the distant hammering of repair crews]
    # play music "music_placeholder"  # [Music: Solo violin, thin and persistent]
    "You count the wins and list the losses in your head like tending to an inventory of grief. Several living-dike sections held — the upstream reed bed buffered neighborhoods, saving a row of old houses and"
    "the market. The community shelters filled and people were ferried to safety. But the southern splice failed where prior dredging had removed the marsh; three vendor piers are condemned; two longstanding fishplots have been sold under"
    "emergency financial collapses before the legal holds took effect. Veridian's paused contracts loom like a shadow — suspended but not defeated."
    "Elliot Chen stands by the sensor bank, eyes on screens flickering with half-data. He turns to you slowly, rainwater still in his hair, a cardboard cup of coffee in hand. There is a weight behind his"
    "shoulders that wasn't there before — a sense of distance being measured in miles he is about to travel."
    show elliot_chen at left:
        zoom 0.7

    elliot_chen "They offered me a regional post. They'll fund a hub to scale living dikes — more equipment, staff, reach. It's the kind of platform to make our designs normative."
    "You feel the first bright prickle of fear and then the quick contraction of understanding. He is the one who can take the model beyond Port Veridian; he is also the one who might leave. The"
    "offer is all the things he has always wanted and all the things that can change what this town is to him — and to you."
    show maya_ibarra at right:
        zoom 0.7

    maya_ibarra "When do you go?"

    elliot_chen "They want me to start next month. They want an implementation plan by the end of the quarter. They say it's me they want leading the hub.' (He looks away.) 'They see the pilot and want to scale it before the funding dries out."
    "A silence hangs like the fog outside. This is not an argument; it is recognition of the calculus that shapes good intentions: scale fast, secure funding, save more places — but at what personal cost?"

    maya_ibarra "Will you—will you stay through the community council? Stand at the table when Mayor Cortez convenes?"

    elliot_chen "I'll be there for this vote. I won't abandon the town mid-crisis. But if the hub opens, it will change how I can show up. I can help more towns if I go. I can also get buried in bureaucracy.' (He manages a tired half-smile.) 'I don't want to walk away from you. From this. But I need to be honest about what they offered."
    "Maya Ibarra: (you try to shape your words around the truth, around the thread of who you are when you are with him) 'I don't want you to go because I need your hands. I don't"
    "want you to stay because of me. I want you to—' (You stop; the sentence is too sharp to finish without cutting.) '—do what you believe will do the most good.'"

    elliot_chen "And if the 'most good' asks me to be elsewhere?"
    "Maya Ibarra: (your throat tightens) 'Then we'll make what we can of the remainder.'"
    "His hand finds yours across the counter, fingers searching like a compass. For a moment, touch is an answer and an apology both."

    menu:
        "Take his hand, promising to wait and fight from here":
            "You lace your fingers with his, grounding both of you. He holds on like someone who has been given permission to be mortal. You draw strength from the touch but know it can't hold storms away."
        "Let go, telling him to follow the hub while you anchor the town":
            "You release his hand gently and force a smile. He reads the steel behind your voice. He presses his palm to your cheek for a second — a benediction and a farewell all at once."

    # --- merge ---
    "Continue with the lab phone chirp and Mayor Cortez's final summary."
    # play sound "sfx_placeholder"  # [Sound: Phone chirps—Mayor Cortez's final summary arrives in a thread; folks gather around the monitor in the lab]
    hide elliot_chen
    hide maya_ibarra

    scene bg ch6_4001e7_7 at full_bg
    # play music "music_placeholder"  # [Music: Dissonant strings resolving into a minor chord]

    "Mayor Cortez" "We have a plan that will not appease everyone. There will be legal holds on certain development contracts. We will condemn structurally unsound piers to protect public safety. We will compensate affected fishers through emergency funds and grant access to communal plots. We will form a stewardship council with rotating seats, including representatives from fisherfolk, ecology, and neighborhood groups. This council will have veto on future large-scale contracts involving Veridian Holdings. This is not a victory, and it is not a surrender. It is a framework — imperfect, necessary, and expensive."
    "You listen to the words like a verdict. The mayor's frame is the government's attempt to bind chaos with policy. It keeps you, in practical terms: it buys time, it layers protections. It also demands sacrifices that will scar."
    show rosa_ibarra at left:
        zoom 0.7

    rosa_ibarra "They'll put up notices about condemned piers tomorrow. I'm uploading the footage to the mayor's portal. We made the case."
    show maya_ibarra at right:
        zoom 0.7

    maya_ibarra "We made the case,"
    "Elliot Chen steps back from the console. He folds his coat, the movement a resignation. He takes a breath that seems to measure all of Port Veridian and find it acceptably incomplete."
    show elliot_chen at center:
        zoom 0.7

    elliot_chen "I accepted the post. I couldn't let the hub pass without someone who understood living systems. I'm sorry."

    maya_ibarra "I'm not—' (the sentence breaks because it means too many things) '—not sorry that you took it."

    elliot_chen "There will be travel. But I'll come back to council meetings. I'll help draft the stewardship charter. I promise."
    "You want to trust that promise without reservation. Trust feels like an organ you have to labor to keep alive. You nod instead."
    "Outside the lab window, the rain softens into a cold drizzle. The day is not won. It is not lost either. It is a ledger open to future accounting."
    hide rosa_ibarra
    hide maya_ibarra
    hide elliot_chen

    scene bg ch6_4001e7_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Quiet conversation, the clink of tools, distant sobbing that becomes a whispered resolve]
    # play music "music_placeholder"  # [Music: A melancholic cello, carrying the aftertaste of the storm]
    "Noah Rhee does not come back to the lab that evening. He walks the shoreline west of the docks at dusk, brass compass in his hand like an accusation. You see him from the boardwalk as"
    "he disappears into low clouds of spray. He does not turn when a neighbor calls him. He makes a shape in the distance: a figure choosing to stand apart."
    "You survive the immediate catastrophe. You count bodies, and by the mercy of perhaps-lived miracles, there are none among your immediate circle. You cluster in the lab and talk through lists and next steps. You sleep in snatches, a body emptied out by adrenaline and responsibility."
    "When you finally sit alone with the pendant at your throat, the sea-glass is warm from rubbing against your skin. You allow the ledger to open in your head: the reeds that held, the splice that"
    "gave, the piers that are gone, the families displaced, the legal holds that bought time, the community council that will have to be constantly fought-for. The math is brutal and granular. The emotion is blown raw."
    "You think of your father's empty chair, the long-ago storm that took him. You imagine him sitting now, knees pulled under him, telling you to stop apologizing to the sea. To act. You think of Rosa's"
    "steady hands, of Elliot's willingness to go where the work multiplies him, of Noah's retreat into anger. You feel yourself both fuller and more hollow."

    scene bg ch6_4001e7_9 at full_bg
    # play music "music_placeholder"  # [Music: Fading violin; a single, low piano note resolves and then holds]
    "You will wake tomorrow and walk the wet paths again. There will be permits to negotiate, funds to wrestle into place, council seats to claim and defend. There will be funerals of old ways — the"
    "small freedom of a private pier reclaimed by seawater. There will also be the stubborn, stubborn work of regrowth: willow cuttings, coir logs, community nights, legal clauses that favor the people who live here."
    "You remember the first time you held a tide sensor in your hands and thought you could translate numbers into protection. You learned, in this storm, that numbers are not enough. People need to be carried"
    "through the numbers, held by narrative and law and food and shared grief. That knowledge is a cost you will carry like an extra coat."
    "You stand at the lab window until the light goes flat. The town is bruised and still luminous in its own way. You press your palm once more to the pendant and let it swing."

    scene bg ch6_4001e7_10 at full_bg
    # play music "music_placeholder"  # [Music: Single sustaining note, tapering into silence]

    scene bg ch6_4001e7_11 at full_bg
    "THE END"
    # [GAME END]
    return
