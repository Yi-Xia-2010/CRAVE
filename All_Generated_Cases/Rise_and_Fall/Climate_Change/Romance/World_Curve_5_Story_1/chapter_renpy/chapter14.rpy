label chapter14:

    # [Scene: Arcology Development Site | Morning]

    scene bg ch12_3be532_1 at full_bg
    # play music "music_placeholder"  # [Music: Low piano motif; a single bright note threads through like a stubborn heartbeat]
    # play sound "sfx_placeholder"  # [Sound: Distant generator hum, the hollow clack of a gate latch, gulls arguing over a strip of plastic]
    "You step through the temporary fence and for a moment the smell of fresh concrete hits you like a physical thing — sharp, antiseptic, the scent of decisions poured into forms. Your navy jacket is thin"
    "against the wind; the salt on the air prickles at the back of your neck. Porches you remember as warm with evening light are boarded now, with 'For Lease' placards leaning against the steps like small"
    "white flags."
    "You remember the meeting in the Civic Garden, the way voices braided into one another, the promise that something thoughtful could be stitched through the town. You remember Dr. Linh's lists of mitigations and Kai's fist"
    "raised in the dark. You remember Noah's measured insistence. The memory itself is not enough to change what has been poured here. But memory is a kind of map; it tells you where to go next."

    scene bg ch12_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Your breath. A distant hammer somewhere in the arcology site, each strike a metronome against your chest.]
    show aria_marin at left:
        zoom 0.7

    aria_marin "So this is what we bought with our compromises."
    "(You don't know if the words are for Noah, or for Kai, or for yourself.)"
    show noah_vega at right:
        zoom 0.7

    noah_vega "It's what kept the banks from walking away."
    "He comes up beside you in a weatherproof blazer that somehow gets dust into its seams. His voice is even, practiced."

    aria_marin "Faster,' you repeat, the word tasting brittle. 'Faster at what cost?"
    "He flinches—just a fraction—and then steadies."

    noah_vega "The company will fund buyouts for the most vulnerable. There are community covenants written into the development agreement. We earmarked funds for local hiring, for a cultural archive."

    aria_marin "Earmarked.' Your thumb twists the compass cord until it whispers. 'Words don't stop porches from rotting."

    noah_vega "No. They don't. Not by themselves.' He looks at you, and for an instant the corporate mask slips. 'But we can build mechanisms for reparations. We can pressure the council to release emergency funds now, rather than later."

    aria_marin "Can we trust them to keep it?"

    noah_vega "You can make them,' he answers, and there is a steadiness in his voice that keeps you from shouting. 'Aria, you made this negotiable. You wrote the clauses. You demanded the language."
    "Aria Marin: The language. You gave them the grammar to be accountable, and still the grammar seesawing on paper is not the same as a family who can't afford three more months. You feel a small,"
    "hot guilt — not the raw, public shame of betrayal, but a private, persistent ache."
    hide aria_marin
    hide noah_vega

    scene bg ch12_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A dog barking somewhere down a neighborhood lane; a radio playing a canned corporate jingle from a work site]
    "He arrives as if the walk to the fence had been a pull from the center of the town. His jacket is bright, patched; his eyes amber and hard."
    show kai_solano at left:
        zoom 0.7

    kai_solano "You're counting clauses with the people outside still living in their cars."
    show aria_marin at right:
        zoom 0.7

    aria_marin "I counted the clauses because I thought clauses could hold back water.' Your voice does not have the flare it used to — the stage of the rooftop is gone; this is a street corner. 'I thought we could make them mean something."

    kai_solano "Clauses don't mean anything if no one enforces them.' He steps closer, the wind bending the hem of his hoodie. 'We needed bodies in the streets, Aria. We needed pressure. You gave them a handshake and a plan and the promise of a pilot."

    aria_marin "The pilot—' You stop. The Schrödinger weight of it presses in: it could have been failed, co-opted, photographed as quaint ruin, or turned into a billboard for 'untethered' living. You refuse to tie yourself to the one version you cannot be certain of. 'Whichever way it went, people lost homes."
    "Kai Solano: (His jaw tightens.) 'People always lose when the town is marketed.' He pulls a photograph from his pocket — a creased image of a battered reef, or a clean rendering of a planned promenade"
    "— you can't tell at first. He slaps it onto the scabbed wood of a construction barrier. 'Look at this. They call it a failure and then they call it 'character.' They brand our absence.'"
    "Aria Marin: (The photo warms the skin of your fingers. You see both images in its gloss. You see that the narrative can be bought and stamped.) 'That's branding,' you say. 'It's a sale.'"

    kai_solano "Which is why we'll keep resisting.' His voice softens. 'But we also need your reach. People listen when you speak. They listen when you file the papers. They listen when you fight in the hearings with evidence."
    "Aria Marin: (You think of the op-eds you've written, the hearings you have organized, the nights you spent editing covenant language until your eyes blurred.) 'I am trying,' you say. 'But I kept thinking there was a way to keep everyone.'"

    kai_solano "No one keeps everyone, Aria.' He looks at you — and the look is both an indictment and a plea. 'But we can keep enough. We can keep the stories. We can force reparations. We can make it costly to ignore people."
    # play sound "sfx_placeholder"  # [Sound: A siren wails faintly; the hum of the arcology's temporary lights switches rhythmically]
    # play music "music_placeholder"  # [Music: A hopeful swell — strings rise, not triumphant, but deliberate]

    menu:
        "Knock on the nearest boarded porch":
            "Your knuckles rap wood. No answer. You step back and press your palm to the grain, feeling the cold and the name carved into the top stair — a child's initials half-seried by weather. The act of touching feels like an acknowledgment: they were here."
        "Walk the block to the old pilot site":
            "You move down the block, boots splashing through a sheen of brine, and find the pilot's sign half-buried in sand. Someone has stenciled 'Remember' on it. You remember why you tried."

    # --- merge ---
    "'You choose the path and find, in either case, that the town's wounds are written in detail: mailboxes beaten by salt, a café's menu stuck with an eviction notice, a mural where paint has peeled but the outlines of hands remain.'"
    # [Scene: Pilot Site | Noon]
    hide kai_solano
    hide aria_marin

    scene bg ch12_3be532_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Frogs in the marsh, the creak of an old walkway]
    # [Smell: Rich wet earth, a sweetness of decay]
    "Dr. Linh Pham kneels beside a tank, fingers black with silt."
    show dr_linh_pham at left:
        zoom 0.7

    dr_linh_pham "We learned things."

    "You" "Did the biology fail, or the story fail it?"
    "Dr. Linh Pham: (She pauses, then gives a small, tired smile.) 'Both. And neither. Ecological work is long. Policy wants fast. Investors want clean outcomes. We have to keep doing the work even when the headline says otherwise.'"
    "Aria Marin: (You hold onto her words like a buoy.) 'So we keep working.'"

    dr_linh_pham "Yes. We do better with time, honest data, and community stewardship. The pilot gave us the data. It also gave them an excuse to move faster on other pieces. It's messy."
    show aria_marin at right:
        zoom 0.7

    aria_marin "Messy because we didn't have power to enforce?"

    dr_linh_pham "Because power is split and interests are misaligned.' She taps the tablet in her hand. 'But the science is here. The knowledge is here. Those are durable. You can use them."
    # play sound "sfx_placeholder"  # [Sound: A distant crowd gathering; someone chanting a slogan under their breath]
    hide dr_linh_pham
    hide aria_marin

    scene bg ch12_3be532_5 at full_bg

    menu:
        "Hand a volunteer a stack of printed testimony summaries":
            "You pass out the paper with the care of someone folding a letter. Faces look up at you, gratitude and grief braided. Someone says, 'We needed this in the hearing.' Your action is small but it plugs a leak: facts into mouths."
        "Step aside and listen to the volunteers swap stories":
            "You let the stories come to you: the woman who saved a box of photographs from a flooded porch, the elder who remembers the original pier. Their voices are crude, human, and they stitch you together in a way statistics cannot."

    # --- merge ---
    "'The people at the edge of the pilot site form a ragged chorus of memory, petition, and outrage. There is protest and there is paperwork, and both move through you like two currents.'"
    # [Scene: Boardwalk | Late Afternoon]

    scene bg ch12_3be532_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slap of waves against pilings, children calling, the clink of cutlery from a café with window displays that show images of possible futures]
    show maya_marin at left:
        zoom 0.7

    maya_marin "You came.' Her blue raincoat has a new smear of color along one sleeve. 'We kept painting. Some people left. A few artists stayed on just to keep this wall from being an ad."
    show aria_marin at right:
        zoom 0.7

    aria_marin "How are you?"

    maya_marin "I miss Mrs. Del Rio's pies,' she says. 'And sometimes I feel like we're putting band-aids on gashes.' She looks at the arcology's silhouette in the distance. 'But we also made a legal file. We documented three hundred families. We're not invisible."
    "Aria Marin: (She is a small, fierce archive in herself.) 'You made a file?'"

    maya_marin "We made a thousand files. We photographed every porch. We recorded names and songs. We asked people to tell us one memory to keep."

    aria_marin "You always do more than I expect,"

    maya_marin "You always try. But trying isn't the same as being present.' She meets your eyes, and there is hurt there but not hatred. 'We needed both."
    # play sound "sfx_placeholder"  # [Sound: A low murmur from a nearby public hearing; a bell rings calling the crowd to order]
    # play music "music_placeholder"  # [Music: The strings lift, hopeful and warm — a sense of collective breath]
    # [Scene: Public Hearing Outside the Arcology | Dusk]
    hide maya_marin
    hide aria_marin

    scene bg ch12_3be532_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Microphones fizz; murmur of many conversations; the sea a distant, constant percussion]
    "You stand behind the podium. The wood is rough under your palm. Cameras blink like neutral stars. A line of speakers has already run through testimony: displaced residents, artists, small-business owners, youth activists. Each story is a bead on a string, heavy with consequence."
    "Elder Tomas Quay takes the mic before you and his voice is a gravelly rope of memory."
    show elder_tomas_quay at left:
        zoom 0.7

    elder_tomas_quay "We did not only lose houses. We lost names on porches. We lost the smell of tar in the mornings. But we will not let those names disappear.' He looks at you, and the look is not accusatory; it is steady, like a lighthouse. 'We will keep telling where we came from so that where we go next remembers us."
    "You listen, collecting breath. You know apology when you hear it; you know the difference between the measured regret of power and the raw grief of someone who had to leave their kettle behind."
    show aria_marin at right:
        zoom 0.7

    aria_marin "I negotiated language that is in this development's paperwork,' you begin. 'I believed clauses could protect homes. I believed in a pilot that would show a different future. I accept that the outcome was not what many of us needed."
    # play sound "sfx_placeholder"  # [Sound: Murmurs; someone shouts a name, then hushes]
    # play music "music_placeholder"  # [Music: A single cello line weaves beneath your words, steadying]

    aria_marin "I will not excuse my mistakes. I will not pretend everything is okay. But I also refuse to accept that this is the end of our agency.' (Your voice is steadier than you feel.) 'We will demand enforcement. We will file for reparations. We will make the archives public. We will ensure funding is released now, not after a committee decides whether to care."
    "A woman in the front row cries out, 'How will you do that?' Her voice is thin with exhaustion."

    aria_marin "By making it costly to ignore us,' you say. 'By suing if we have to. By drawing national attention to what was promised versus what was delivered. By insisting that every lease and demolition is documented. By forcing those who profited to return value to those they displaced."
    "Noah Vega steps forward from the back of the crowd, not on the stage but close enough that you can see the tightness in his hands."
    show noah_vega at center:
        zoom 0.7

    noah_vega "I will support litigative action. The firm will not hide behind legal shields. We have leverage. We will mobilize it."
    "Kai Solano: (From the side, Kai's shout is raw.) 'Words again. We will see if words hold water this time.'"

    aria_marin "No. Not words alone. Actions. And we will be the ones to keep watch."

    menu:
        "Read the list of families who lost homes aloud":
            "You open the folder, and each name feels like casting a stone in a still pool. The crowd listens; some weep openly. The reading is an act of witness — small, sober, and binding."
        "Invite the affected families to form an oversight council":
            "You gesture to the people gathered. A few stand first, shy and astonished. Their faces are raw. The invitation is not a solution, but it hands power back to those who were written out. The crowd murmurs its approval."

    # --- merge ---
    "'The choice matters in the way small, deliberate acts matter: it shapes process, not miracle.'"
    # [Scene: Outside the Arcology | Night]
    hide elder_tomas_quay
    hide aria_marin
    hide noah_vega

    scene bg ch12_3be532_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Quiet—voices lowed into conversation—footsteps, shifting cardboard]
    "Kai Solano: (His face is a shutter of grief and fury. He leans against a bollard.) 'I wanted to tear that place down with my bare hands.' There is no heat to his words now—only an exhausted ember. 'Instead, we scaffolded language.'"
    show aria_marin at left:
        zoom 0.7

    aria_marin "We did what we could with the levers we had."
    show kai_solano at right:
        zoom 0.7

    kai_solano "Do you think you'll forgive yourself?"
    "Aria Marin: (You consider the compass at your throat, its brass dulled.) 'I don't know.' You press the band on your left ring finger until you can feel the cool metal. 'But I will keep trying. I will not stop making it costly to erase people.'"
    "Kai Solano: (He laughs, short and incredulous.) 'You're not the same person I grew up with.' The words are almost a compliment. 'You went into rooms I never could get into.'"

    aria_marin "And you are the person who got the street to move.' You meet his eyes. 'We both did harm in our ways. We both tried to fix different parts of the same wound."

    kai_solano "Maybe,' he says. 'Maybe we'll be allies who argue in the same room someday.' He looks away, the city lights catching his profile. 'Maybe we'll never speak again."
    "Aria Marin: (You don't push him. Some bridges are burned; others are only smoldering.) 'If that is how it ends, I will live with it. But I want to keep the possibility that we can be better.'"
    "Maya approaches, hands stained with paint. Elder Tomas comes beside her, steady as tide."
    show maya_marin at center:
        zoom 0.7

    maya_marin "We held things together today.' She hands you another small scrap — a photocopy of a porch photograph with a line drawn around the doorknob. 'We will turn these into an exhibit. We will make them public records. People will see what was lost."
    "Aria Marin: (There is a strange, tender resilience in the plan.) 'And the reparations,' you say. 'We will fight for them. We will hold hearings until the funds are disbursed.'"
    hide aria_marin
    show elder_tomas_quay at left:
        zoom 0.7

    elder_tomas_quay "Make sure the stories live.' He touches the edge of the photocopy like one might touch a map, feeling contour lines. 'Money helps. But memory is more dangerous for those who would erase it."
    "Aria Marin: (You tuck the photocopy into your satchel. It is not much. It is a tiny, stubborn archive.)"
    # play music "music_placeholder"  # [Music: Warm strings, minor resolved into something like a promise]
    hide kai_solano
    hide maya_marin
    hide elder_tomas_quay

    scene bg ch12_3be532_9 at full_bg
    "You: You are, in some sense, exiled in your own town — a planner whose choices shaped this skyline and whose hands now press for remedy. The town hums around you: commerce reboots, some faces are"
    "gone, new storefronts glitter with the strange sheen of profit. The texture of neighborhoods has changed. There is a brittle peace."
    "And yet — and yet — there are seeds. Maya's seeds, the photocopies, Dr. Linh's data, the covenant clauses with teeth. There are people who will not let the story be washed clean and investors who"
    "will find it politically expensive to ignore. You will be an unapologetic critic; a public face for repair; a voice in hearings and in op-eds; a person who learned the hard arithmetic of compromise."
    "Aria Marin: (You close your eyes for a moment and breathe in the briny night air.) 'This is not the ending I wanted,' you tell the stars, the arcology, and the people who listen. 'But it's not the end.'"

    scene bg ch12_3be532_10 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Someone begins to sing quietly, a song people used to sing on the docks. Others join in, low at first, then with more assurance.]
    "You: You will keep speaking. You will keep recording. You will keep pushing for reparations. You will keep making room for those who still have to stay. You might lose love. You might lose friendships. You will keep working anyway."
    # play music "music_placeholder"  # [Music: The piano motif returns, turned gentle and sure; strings rise to a soft, hopeful chord]

    scene bg ch12_3be532_11 at full_bg
    # [Scene: Final — Boardwalk Overlook | Dawn]

    scene bg ch12_3be532_12 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The sea breathing; a distant line of children laughing as they chase a dog]
    "You reach into your satchel and find the seed packet Maya gave you. You place it between two planks on the overlook — a tiny, symbolic planting. It's a small, foolish ritual. Someone might sweep it away; someone might laugh. But you leave it there anyway."
    show aria_marin at left:
        zoom 0.7

    aria_marin "We will be the historians of our own loss,' you say aloud, though no one is required to answer. 'We will make sure the ledger holds both the cost and the repair."
    # play music "music_placeholder"  # [Music: Strings resolve into a steady, rising motif]
    hide aria_marin

    scene bg ch12_3be532_13 at full_bg
    "This is not a return to what was. It is not a triumphant undoing of harm. It is a different kind of forward: slower, messier, lit by small, persistent acts. You will carry the weight of"
    "being implicated and the quiet pride of never stopping the work. The town survives, altered. You survive, altered. There is a brittle peace; there is also a rising current under it — community mechanisms forming, legal"
    "teeth, archives, activists learning to combine street heat with committee leverage."
    "Aria Marin: (You touch the silver band on your left hand and let the compass warm against your skin.) 'We will make them pay attention,' you vow. It is not vengeance. It is accountability. It is love turned into insistence."

    scene bg ch12_3be532_14 at full_bg
    # play music "music_placeholder"  # [Music: Fade into a single piano note, held and then released]

    scene bg ch12_3be532_15 at full_bg
    "THE END"
    # [GAME END]
    return
