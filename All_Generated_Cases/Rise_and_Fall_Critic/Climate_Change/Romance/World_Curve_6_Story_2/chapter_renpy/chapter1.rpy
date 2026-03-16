label chapter1:

    # [Scene: Harborfront | Early Morning]

    scene bg ch1_Start_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, a loose shutter creaking, the low, steady slap of tide against pilings]
    # play music "music_placeholder"  # [Music: Sparse piano with low strings — restrained, minor key]
    "You wake to the cold memory of rain in your hair and the steady, wrong rhythm of a town that has been washed and stitched overnight. The shack where you slept smells of tar, damp wool,"
    "and the sour sweetness of seaweed left to ferment in a corner. Your jaw is tight; your field jacket is still on the chair where you dropped it. You reach for the waterproof notebook before your"
    "hands start to look for anything else — it's heavier than it should be, as if the pages remembered the storm themselves."
    "You push open the door and the harborfront hits you all at once: the market stall with its tarpaulin shredded like a flag, a boathouse door twisted on one hinge where you thought it was secure,"
    "a net hanging in ribbons that used to be somebody’s livelihood. Salt is in the air, sharp and metallic at the back of your throat. The bulletin from last night promised 'minor damage, crews assessing.' The"
    "harborfront is louder than 'minor.'"
    "You count with your eyes, because counting is how you steady yourself when the past starts living in the present again."
    "Nets shredded. One small skiff half-submerged against the eastern piling. A vendor's crates floating loose, oranges bobbing like small suns in the gray water. The ladder to Etta's lowest berth is gone; the planks around it bloomed with the stamp of the tide."
    "You feel the old scar inside you tighten — the memory that never leaves. You remember a name, the shape of a boy who trusted the weather the way you once did, how you learned there"
    "is a difference between prediction and mercy. Your fingers close on the coral pendant at your throat without thinking. It is rough under your thumb, a small, foolish heirloom that smells faintly of salt and someone"
    "else’s hands. You breathe. The rope around your chest loosens a hair."
    "You flip your notebook open and the margin is a place where you keep vows and calculations in the same cramped handwriting. You write, as if etching a line into the town itself: Protect the harbor, protect the people."

    scene bg ch1_Start_2 at full_bg
    "You move along the pier with purpose: a planner's walk — eyes scanning, hands cataloguing. You feel every step as if it's a decision waiting to be made. The civic meeting will be in two hours."
    "The Skyhub delegation will arrive by the mid-morning ferry; rumors of Seren Blake's regional program have been a whisper for weeks, and now they're stepping off a boat with glossy folds of paper and policy. You"
    "taste the metallic tang of distrust thinking of her polished shoes on these planks. Your loyalty to Hearthbend tightens like a rope in your hand."

    menu:
        "Inspect Etta's berth first":
            "You cliмb down where the tide licked the pilings, hands checking for what can be salvaged, feeling the mud collect under your nails."
        "Walk straight to the market to gauge the people":
            "You thread between stalls, calling names, listening for the cadence of fear or anger in the vendors' voices — and make a mental map of who needs help first."

    # --- merge ---
    "You choose — because you always choose. The harbor obliges you with details: a fisherman bending over a broken net, the damp sheen of someone crying into a wool cap, the way the market's canvas banners"
    "hang like tattered mouths. You take notes that are both practical and elegiac. The clock in the town hall tower is a slow, indifferent metronome."

    scene bg ch1_Start_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The creak of a boarding plank, a soft, apologetic laugh]
    # play music "music_placeholder"  # [Music: A tentative two-note motif, slightly warmer but still in a minor key]
    "Ilias Navarro steps up onto the dock with a cracked jar of eelgrass bobbing in his hands, and for the first time since the rain, something in you finds a steadier heartbeat. He smells of wet"
    "kelp and dried lab cleaner — the paradox of someone who moves between science and salt. His tide-watch bracelet glints; the charms move when he reaches out to steady himself."
    show ilias_navarro at left:
        zoom 0.7

    ilias_navarro "Morning. Sorry I'm late — the tide shifted while we were collecting. The samples… some are split, but—' (he holds the jar so you can see the eelgrass, water catching light) '—there's live growth in the sheltered patches. It’s… better than the models said for this stretch."
    "Maya Kestrel: (you can feel the skepticism in your voice before you let it out) 'Models misbehave when the sea behaves like this. 'Better than models' isn't the same as 'enough.''"
    "Ilias Navarro: (he gives a sad little smile) 'You're right. But it's the sort of 'not enough' we can wedge at the edges. Small beds hold sediment, the roots slow erosion, and if we can marshal volunteers and seedlings fast—'"
    "Maya Kestrel: (cutting in) 'Marshal volunteers? We need hands, yes, but we also need a plan that won't fall apart after the next storm. The Harborfront won't patch itself with hope.'"

    ilias_navarro "It won't. It needs labor and it needs funding. I've been arguing for a phased restoration — start with the beds closest to the inlet, monitor sediment accretion, scale outward. If we show local success, I can make the data argue for funding. The Skyhub people… they listen to numbers."
    "You study him. His earnestness is a rope you want to climb, but tangled somewhere is caution. He fingers his bracelet, looking at the charms as if they are tabs of time he can open."

    ilias_navarro "Listen — I'm not proposing we ignore larger infrastructure. I'm saying biology buys time. If you—if we—get the town on board, the beds can blunt the next surge. Give us a pilot, please. Give me two months."
    "Maya Kestrel: (your voice is quieter; the guilt that resists being named presses at your ribs) 'Two months is long when houses are listing and livelihoods are a list with missing names. What if two months is the gap where something else moves in and calls it 'efficient'?'"
    "Ilias Navarro: (his hands tighten around the jar) 'Then we'll be better at making the case. But you know me, Maya. Ilias is stubborn enough for two months, and honest enough to tell you when it fails.'"
    "Maya Kestrel: (there's a pause where both of you look out at wind-rippled water and broken wood) 'I don't want honesty that excuses delay. I want action that keeps people where they are.'"
    "Ilias Navarro: (he meets your gaze, steady) 'So do I. That's why I'm here.'"
    "The conversation rolls like a tide — arriving, retreating, leaving shells of things unsaid on the sand. He wants the community to grow the shore back; you want the community to keep its history intact. They are the same thing, sometimes. Sometimes they are not."

    menu:
        "Ask Ilias to show you the data now":
            "You press him for numbers in the moment, wanting reassurance. He pulls out a damp, plastic-sleeved printout and points at the curves with a thumb that still smells of salt."
        "Tell him to save the data for meeting time":
            "You tell him the numbers will help but you need to feel the room first. He nods, understanding that community emotion often trumps charts at first blush."

    # --- merge ---
    "Your steps take you back toward the center of town where voices already gather in small, anxious constellations. Etta is there — as always she is both a worry and a command. She stands with a"
    "shawl wrapped tight, looking smaller than she ought to be for how much weight she carries. Her face is wind-creased, and when she turns toward you, the harbor seems to hush in expectation."
    show etta_muir at right:
        zoom 0.7

    etta_muir "Maya Kestrel. There you are. Did you sleep? You look half-drowned."
    show maya_kestrel at center:
        zoom 0.7

    maya_kestrel "I slept where I fell, Etta. The harbor did the rest."
    "Etta: (her voice is grainy and sharp as the edge of a net) 'The rest it did. Your list — the ledger — I heard. You can't let them walk in and put plans on top of our graves. Not again.'"
    "You feel the old, raw chord of anger beneath her words. Etta's memories anchor this town in a thousand small losses and a few big ones that still taste like salt."

    maya_kestrel "They're not 'plans' yet. The Skyhub people will come with papers and polished language. We will have the floor tonight. We'll lay the ledger out ourselves."
    "Etta: (she studies you like a captain reading the weather) 'Promises sound like rope until you test them. If you speak, speak as if your voice can cut through screws and steel. Tell them we won't be sacrificed for a region's balance sheet.'"
    "Maya Kestrel: (you hear the congregation behind her — neighbors, a couple of teenagers wrapped in hoodies, Rafi already hovering with a camera slung over his shoulder) 'I will speak. I'll say what needs saying —"
    "for the fishers, for the families. But I won't let us be cruel out of fear. We need a path that keeps people alive and keeps the harbor alive.'"
    "Etta: (a twist of something close to a smile softens her face) 'Good. Don't be sentimental. Be a stone.'"
    hide ilias_navarro
    hide etta_muir
    hide maya_kestrel

    scene bg ch1_Start_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The shuffle of shoes on wet wood, a polite cough]
    show mayor_ansel_reed at left:
        zoom 0.7

    mayor_ansel_reed "Maya—Etta—good morning. I know—this is difficult. The regional office offered an emergency grant after last night's assessments. It's… significant."
    "Maya Kestrel: (you watch his eyes; they carry the tired calculation of someone trying to be both steward and politician) 'Significant how?'"

    mayor_ansel_reed "Enough to fund immediate repairs. Seawall reinforcement, subsidize relocation of the most vulnerable; it's money, and right now money matters. The Skyhub delegation wants to present a broader program at today's meeting. They propose a coordinated approach."
    show maya_kestrel at right:
        zoom 0.7

    maya_kestrel "Coordinated how? How much of 'coordinated' is local voices, and how much is someone else's idea of who's expendable?"
    "Mayor Ansel: (a small, pained smile) 'They'll bargain for efficiencies. They will ask for permits, oversight, and maybe consolidated ownership of some fishing rights to streamline response. I'm trying to secure the funds with the least intrusion possible.'"
    "Etta: (her voice like a slap) 'You sign for permits and what you sign away is a life. They will redraw who owns the sea.'"

    mayor_ansel_reed "Etta, I'm not asking you to trust them blindly. I'm asking our town to consider options that prevent immediate ruin. If we reject help outright, we risk watching people lose everything because we prioritized pride over roofs."
    "Maya Kestrel: (the rope around your chest tightens again — the old argument made new by the prospect of cash and control) 'We are not choosing pride over roofs. We're choosing who gets to decide what 'help' looks like. If we hand them the ledger, they will edit it.'"
    "Mayor Ansel: (he looks at you, appeal and exhaustion mixed) 'Give me a way to ensure we keep ownership of our spaces, and I'll negotiate. I can't guarantee everything, Maya. I'm only the one who stands between the grant and the town council.'"

    maya_kestrel "And if your negotiation doesn't hold? What then?"
    "Mayor Ansel: (he exhales) 'Then we negotiate again, and again. But we also have to admit that some measures might only work if they're larger than us.'"
    show etta_muir at center:
        zoom 0.7

    etta_muir "Larger solutions do not understand salt. They understand lines on maps."
    # play sound "sfx_placeholder"  # [Sound: Far-off, the creak of a ferry horn — a thin, blaming note]
    # play music "music_placeholder"  # [Music: Low strings deepening, a sustained chord of unresolved tension]
    "You touch the coral pendant at your throat with a thumb that knows how to read barnacles and time. Your handwriting in the notebook looks suddenly inadequate. You add another line below the first: Protect the"
    "harbor, protect the people. (You underline it twice, because underlining is how you make an order to yourself.)"
    "You look out at the ferry slice through the fog, a silver promise that could be rescue or erasure depending on how the meeting goes. The ledger is not just numbers; it’s the long, messy spiral"
    "of family names, fishing rights, learning by the tide. If the delegation opens their case and starts with 'efficiency,' Hearthbend will have to answer whether it values heritage in measurable units."

    menu:
        "Tell Mayor Ansel you'll give him one hour to show a draft negotiation":
            "You fix him with a look that won't be folded. 'One hour,' you say. He nods, relief and dread flickering across his face."
        "Tell him you need the community to see the draft first":
            "You insist that any draft goes before the people. He shifts, the weight of politics pressing at his shoulders; he promises to arrange a public review before signatures."

    # --- merge ---
    "You can feel the meeting like a hinge beneath your feet. You can imagine Seren's polished shoes tapping toward the podium, the slide decks, the way a powerpoint can redraw an entire coastline in two hundred"
    "pixels. You can imagine Ilias with his damp sleeves and earnest charts, trying to translate living things into tables. You can imagine Etta, blunt and furious, holding the room like a torch."
    "Your lungs are small with the storm's aftertaste. There are names scrawled in your head that each decision could erase. You want to call them by name but it would make you smaller than the sea."
    "Instead, you fold the notebook closed and put it back against your ribs as if it were armor."
    hide mayor_ansel_reed
    hide maya_kestrel
    hide etta_muir

    scene bg ch1_Start_5 at full_bg
    # play music "music_placeholder"  # [Music: A single low note that lingers like an unpaid debt]
    "You step toward the town hall and the crowd parts in small, hesitant arcs. There is no graceful path here, only the path you make by choosing how loudly to speak and who you will allow"
    "to redraw your ledger. Your chest hums with the weight of the past and the freight of what might be bought with money that tastes of other people's rivers."
    "You say nothing yet. You let the sound of the harbor be its own indictment."
    "You breathe in tar, kelp, and rain — the honest smells of Hearthbend — and you feel the moment that will force a choice approaching like a swell on the horizon."
    # [Page-turn moment: The town hall's wooden doors creak open and the first of the Skyhub delegation steps onto the threshold, phone screens bright, smiles calibrated. Behind them, a uniformed facilitator carries a tablet that will become tonight's agenda. For a heartbeat, all the possible ledgers hang between you — the one you keep and the one they bring.]

    scene bg ch1_Start_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter2
    return
