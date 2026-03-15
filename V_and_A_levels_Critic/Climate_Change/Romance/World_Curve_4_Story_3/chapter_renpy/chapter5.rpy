label chapter5:

    # [Scene: Old Pier | Dusk]

    scene bg ch5_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense BGM — a tight, rising percussion; strings scrape under a low synth]
    # play sound "sfx_placeholder"  # [Sound: Murmured chants, the slap of waves against pilings, a distant siren]
    "You stand with the crowd, and the harbor breathes against you — a tidal inhalation that smells of diesel, bruised kelp, and the cold iron of rain. Whatever thread you pulled last night has doubled back on the town; consequences fan out faster than you can chart."
    "Policed lines cut like a sudden tide across the pier. Legal notices move through inboxes and into the glass-fronted offices downtown. In one corner, a press photographer raises a camera; in another, someone tapes a notice"
    "to a bulletin board and it flaps like a small flag in the harbor wind. Which of those things arrived because of your hands and which because of someone else's strategy is a question that circles"
    "your head without landing."

    scene bg ch5_4001e7_2 at full_bg
    "You watch Elias before you can think to look anywhere else. He is knuckled into a motion — shouting, stepping forward — and then an official hand clamps on his arm. Mud streaks his denim jacket;"
    "the wooden whistle that usually hangs from his neck is gone for a breath. He looks at you."
    show elias_hart at left:
        zoom 0.7

    elias_hart "Maya— (his voice rough, cut by the wind and mud) Don't—don't make this worse."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "I didn't— (your throat closes; the sentence fractures) I tried to get people out of harm's way. We warned them."

    elias_hart "Warnings don't stop them from putting fences up and locking our boats, May. They make it sound like we're the storm."
    "Maya Reyes: (You reach, but the space between your fingers and his sleeve is filled with uniforms and public expectation.) 'We can still—there's still a window. We can hold. We can—'"
    "Elias Hart: (cuts you off) 'Hold until what? Until somebody gets arrested? Until people miss paychecks? You know what those docks do for people here.' (He lowers his voice) 'You know I believe in this, but if you go all in because you feel guilty—'"
    "Maya Reyes: (Guilt flares, immediate and hot — memory of a different storm, a different ledger of trade-offs.) 'I am trying to be responsible.' (The words are small; they don't match the shaking in your hands.)"

    elias_hart "Being responsible doesn't mean you carry everything and burn the town trying to save it.' (He swallows) 'We need a plan that doesn't make us look like fools."
    "Maya Reyes: (You want to tell him about the data in your journal, the contour maps, the marsh restoration models that could buy the town time. You also want to tell him about the way a"
    "rushed decision once cost you a street of houses. Both truths push against your ribs.) 'Plans need people to see them. They need momentum.'"

    elias_hart "Then make them see it.' (He meets your eyes with a pain that pries open something in you.) 'Not everyone can wait for the long game."
    # play sound "sfx_placeholder"  # [Sound: A shout — indistinct — ripples through the crowd. Someone bangs a milk crate as a makeshift drum.]
    hide elias_hart
    hide maya_reyes

    scene bg ch5_4001e7_3 at full_bg
    show iris_tanaka at left:
        zoom 0.7

    iris_tanaka "They're listening more to the mayor's press than to the people who actually fish this water.' (She snaps a flyer onto the wet wood.) 'You saw them, May. The guys unloading the nets — half of them look at us like we're the reason their boats are idle."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Some cheer. Some fear.' (You hear the thrum of those two classes of sound in your chest.) 'Which side of that line do we cross without trampling people who already have too little?"
    "Iris: (barks a short laugh that tastes like salt) 'We don't get a clean line. But if we lose the shore, we lose our kitchens.'"

    menu:
        "Step toward Elias and take his hand":
            "You close the distance and clamp your fingers around his wrist. His skin is cold and the smell of mud is sharp. For a moment the rest of the pier is muffled; you both breathe together, a small, human counterpoint to the chaos."
        "Move to the crate where Samir is filming":
            "You kneel beside Samir. He raises the camera like a small altar. The lens catches your profile and the world becomes a series of frames — evidence, narrative, things that could be used. He gives you a look that asks if he's recording the last time you'll see each other like this."

    # --- merge ---
    "..."
    # [Scene: Tidewatch Harbor — Cutaway | Night — Press and Counsel]
    hide iris_tanaka
    hide maya_reyes

    scene bg ch5_4001e7_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The muffled tapping of keys, a lawyer's phone on vibrate; distant applause and boos mingled]
    "Your phone vibrates — Professor Julian Kim. His voice, when you pick up, is smaller than his face would suggest."
    show professor_julian_kim at left:
        zoom 0.7

    professor_julian_kim "Maya, are you at the pier? The lab just had a formal notice served. They're asking for all of our preliminary siting analysis.' (He speaks quickly — the syllables clipped like someone trying not to let panic breed.) 'This isn't standard. They're subpoenaing data and it looks like they're going to try to spin our models into weapons."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "They're trying to weaponize the uncertainty.' (The thought is bitter in your mouth.) 'Do they have grounds?"
    "Professor Julian Kim: (a breath) 'They can file to compel. The legal apparatus is moving fast. If those datasets are released in raw form, without context, they'll be used to undermine community proposals.'"

    maya_reyes "We can— (you reach for the optimism your job trains you to hold) —we can provide context. We can release an annotated set, explain our assumptions."

    professor_julian_kim "They can subpoena the lab and mix it with paid consultant reports. Maya, this is political. Maren has made it political.' (He pauses; you can hear the clink of a thermos as he sets it down.) 'Be careful. The narratives they choose will shape who the public believes."
    "Maya Reyes: (Your stomach drops; the ways that numbers become stories, and stories become verdicts, spin in your head.) 'They'll say we're obstructionists, or reckless. They'll say the delay is us refusing help.'"

    professor_julian_kim "Whatever happens, don't let them frame the science as partisan.' (He sounds tired in a way that means he is more frightened for a town than for data.) 'And Maya—' (hesitation) 'watch Elias. He looked... he looked like he was about to cross a line."

    maya_reyes "I'll try to keep him from getting— (but the memory of his arm being taken by a security aide is already there) —from getting hurt."

    professor_julian_kim "Try to keep yourself from becoming the story."

    menu:
        "Argue the lab should release annotated data publicly tonight":
            "You imagine the lab's cool glass becoming a stage. Transparency could cut through the PR fog — or hand Maren a blunt instrument. Your fingers trace the edge of your phone as if the screen is a map you could redraw."
        "Tell Julian to secure the datasets and brief only trusted media":
            "You picture locked rooms and careful words. It would protect the narrative but slow momentum. In your chest a small, old voice whispers about patience, and the weight of that whisper presses against your ribs."

    # --- merge ---
    "..."
    # [Scene: Boardwalk / Council Offices | Night — Confrontation]
    hide professor_julian_kim
    hide maya_reyes

    scene bg ch5_4001e7_5 at full_bg
    # play music "music_placeholder"  # [Music: Percussion quickens; a high violin line threads anxiety under dialogue]
    # play sound "sfx_placeholder"  # [Sound: Flashbulbs, a microphone crackling to life]
    show maren_voss at left:
        zoom 0.7

    maren_voss "These actions threaten jobs and the stability of Harborwell. We cannot allow the safety of our residents to be gambled. Our redevelopment plan provides immediate protection and work for those in need.' (Her smile is a political tool — precise, narrow.) 'We welcome debate, but not obstructionist tactics."
    "Maya Reyes: (You watch her mouth the line and feel everything in the room bristle — cameras, phones, the mechanical empathy of a politician who has practiced being human.) 'She makes us sound like children starting fires.' (The thought is hot enough to sting.)"
    "Maren Voss: (You find yourself near enough to hear her when she steps off the short stage, the crowd parting politely.) 'Maya.' (The name is a probe. She studies you; her face goes unreadable.) 'You and"
    "your colleagues have done valuable work. But there is a difference between advocacy and risking the livelihoods of this town. My job is to keep this town solvent.'"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Solvent for who?' (The question escapes more acidic than you planned. Your voice is loud and it pulls a few heads.) 'Because redevelopment backed by private funds and exclusivity isn't a plan that protects everyone. Some people get protected by walls; others get priced out."
    "Maren Voss: (She tilts her head, an almost-pitying expression.) 'You make it sound like a zero-sum. I have to balance immediate survival with long-term resilience. We can do both — with leadership. With decisiveness.'"

    maya_reyes "Decisiveness that silences dissent isn't leadership.' (Your words are sharper than you intended.) 'And you know how much this town can lose in a hurry."
    "Maren Voss: (A small, controlled smile.) 'You know I didn't come into this without knowing what was at stake. And you know action must sometimes be tough. You should be proud of the people who have rallied. But don't let pride be the reason this town loses its bearings.'"
    # play sound "sfx_placeholder"  # [Sound: A ripple of polite applause, then a longer, ambiguous murmur — some approval, some not.]
    hide maren_voss
    hide maya_reyes

    scene bg ch5_4001e7_6 at full_bg
    # [Scene: Old Pier | Night — Fraying Edges]

    scene bg ch5_4001e7_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The tide, the distant thud of a boat horn, a chant that breaks mid-verse]
    "The town's energy is a rope being frayed by too many hands. A neighbor you recognize from the fish market tells you, under his breath, that he's owed two weeks' wages and can't afford to miss"
    "another day. A high-schooler clutches a homemade sign and says the movement gave them purpose. Your brother Samir keeps filming; his camera moves like a heartbeat."
    show samir_reyes at left:
        zoom 0.7

    samir_reyes "This is going viral, May. People are sharing the boats being blocked.' (There's a hardness under his words.) 'They're saying 'good' and they're saying 'danger.'"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Doesn't mean it's right.' (You sound weary.) 'Doesn't mean it's working."
    "Internal Monologue — Your guilt, the old ledger"
    "You replay decisions like weather patterns: a sudden storm that forced an evacuation years ago because you signed off on an expedited relief plan; the applause then, the slow erosion of trust after the promised rebuild"
    "didn't reach every street. That trade — lives saved, neighborhoods destabilized — is a scar you press thumbs into when sleep is thin."
    "Now every miscalculation multiplies. A delayed grant because lawyers file for injunctions; a town council press release rebranding your actions as reckless; a lab subpoena that turns clean models into political weapons. The pilot funding sits in limbo, a promised life raft wrapped in legal red tape and public relations."
    # play music "music_placeholder"  # [Music: Building to a sharp, urgent crescendo — percussion, strings rising; the soundscape tightens]
    # play sound "sfx_placeholder"  # [Sound: Distant shouts; the scrape of a barricade being set; a police radio chirps static-laced commands]
    "You sense the moment arriving — not a slow eclipse but a sudden cloudburst. The crowd looks to you in the way crowds look to someone who promised a map. Your shoulders feel too narrow for the weight of so many expectations and resentments."
    "Professor Julian's earlier warning hangs like a buoy: don't let the science be the story. But the story is already moving. Maren's carefully chosen words are folding into headlines. Your brother's footage is being retweeted with"
    "captions you didn't write. Elias's jaw is set like a man ready to cross a line you cannot always mitigate."
    "Iris comes close, her gloved hands grounding her posture."
    show iris_tanaka at center:
        zoom 0.7

    iris_tanaka "We can call it off. Pull the people back. Let the lawyers do the arguing.' (Her voice is rough with salt and something like sorrow.) 'We do the slow work. We don't go down fighting."
    "Elias Hart: (He looks between you and Iris, and you can see the tug — he wants to believe in negotiation, but he hates what compromise has meant in the past.) 'Or we keep holding. Keep"
    "the pier a blockade until the money comes. Show them we won't be bought off.'"
    "Maya Reyes: (You measure the town in breaths and balances.) 'Or we expose who's funding the plan and hope the public sees the strings.' (The idea tastes like danger.) 'We could leak the backers, the contracts, the whispers. Force the conversation into the open.'"
    "Elias Hart: (His face pinches.) 'Expose them and they'll come down hard. Lawsuits, PR attacks. They can crush what's left of the co-op.'"

    iris_tanaka "Accept the partial project and you save some people now, but you give ground to a plan that will make the next storm worse for others."
    "Samir: (records, voice strained) 'Every video could be the thing that breaks it one way or another.'"
    "Maya Reyes: (Your chest tight; the harbor air suddenly too thin.) 'There is no clean path.' (It echoes without solace.) 'There will be harm no matter what we pick. But we have to choose the harm we can live with.'"
    # play music "music_placeholder"  # [Music: Peaks; a single, held dissonant chord that refuses to resolve]
    hide samir_reyes
    hide maya_reyes
    hide iris_tanaka

    scene bg ch5_4001e7_8 at full_bg

    menu:
        "Step forward and call for escalation — hold the pier":
            "You place your palm onto a crate as if swearing on it. The crowd edges forward, some shouting approval, others shaking their heads. Elias grunts, part defiant, part frightened, and the energy thickens into a tangible force."
        "Signal for a temporary withdrawal to negotiate a partial project":
            "You lift your hands clasped, palms outward. Murmurs ripple through the crowd; some see it as betrayal, others as relief. Iris's shoulders sag like she can finally breathe. Elias's jaw clenches as if restraining a storm."
        "Whisper about exposing backers and ask Samir to archive everything":
            "You say the word 'expose' low, and Samir's camera stiffens. Eyes flick to him; phones move closer. A few faces light with grim hope, others sink with dread. The air tastes sharp and metallic, like a storm before it drops."

    # --- merge ---
    "..."
    # [Scene: Old Pier | Dusk → Night — The Moment Before a Choice]

    scene bg ch5_4001e7_9 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The pier seems to hum — a hundred tiny anxieties syncing into one noise]
    "You feel time compress, as if the harbor itself is squeezing the moment until something must give. The legal motions, the public statements, the lab subpoenas, Maren's press lines, the people's hunger for wages and safety — they press inward, a ring tightening."
    "Your chest aches with a negative clarity: none of the options are pure. Each will cost something essential. Each will shape the immediate future with a force that could protect or break Harborwell. Your guilt —"
    "that persistent, private ledger — pushes one way; your compassion for people who will miss rent payments pushes another; your faith in truth and transparency pulls another."
    "Your hands hover above the crate. Around you, the faces of the town — Elias's muddied jaw, Iris's flinty calm, Samir's steady lens, Professor Kim's worried message — orbit your decision like buoys in a churning sea."
    # play music "music_placeholder"  # [Music: Staccato strings, breathless percussion — highest tension]

    scene bg ch5_4001e7_10 at full_bg
    "This is the endgame tactic to secure implementation."

    jump chapter6
    return
