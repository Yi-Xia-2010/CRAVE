label chapter14:

    # [Scene: Tideguard Corporate Pavilion | Late Afternoon]

    scene bg ch14_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hum of ventilation, a distant sea-siren muffled by glass; the tick of a wall clock.]
    # play music "music_placeholder"  # [Music: Sparse piano, low and uneasy]
    "You feel the grain of the table under your palms — smoothed by meetings, not by hands that know rope or net. The compact sits between you and Cassian, a rectangle of promises and small type."
    "You demanded legally binding oversight; your words are still settling like stones at the bottom of the room."
    show cassian_rhee at left:
        zoom 0.7

    cassian_rhee "You asked for binding clauses, Marin. Full transparency. That's…a heavy ask. Our investors expect flexibility."
    "His voice is even, too practiced for the tremor you can feel in your own chest. He shifts a sheet of Tideguard's proposal toward you like an offering, like a test."
    show marin_sato at right:
        zoom 0.7

    marin_sato "Flexibility that allows privatized access to the inlets isn't the same as flexibility for adaptive maintenance. We need public oversight written in. We need access that can't be closed off to the people who fish and mend and live here."
    "Cassian frowns; the movement is small but hard. He catalogs the cost in his head like a ledger."

    cassian_rhee "You know how investors think. Ambiguity kills capital. If we put the governance structures you want into the compact, we risk the entire funding stream. There are deadlines, Marin."
    "You feel the compass against your collarbone, the brass cold as conviction. You remember the boathouse roof under rain, Ivy's hands in wet soil, Tomas's crooked grin when a net came in heavy. Those memories press against your ribs."

    marin_sato "Then don't present it as a unilateral 'ask.' Present it as a safeguard. Put independent auditors, town seats, enforceable access rights. If Tideguard wants to be part of Havenport, it must be accountable to Havenport."
    "Cassian's jaw tightens. For a moment, his practiced mask slips and you see the calculation: reputations, boardrooms, quarterly numbers."

    "Cassian Rhee (quiet)" "You make this personal. I don't like that, Marin."

    marin_sato "This is everyone's history. This isn't personal."
    "Cassian's hand taps the table once, a soft, precise staccato."

    cassian_rhee "Legally binding oversight scares off funding. It slows us down. The faster we act, the fewer people we lose to the next storm."

    marin_sato "And the slower we act with accountability, the more we lose to the next ten years of decisions made for profit instead of people."
    "Cassian scoffs, but it's other people's money his voice is shielding."

    cassian_rhee "You want assurances. We can do transparency, but not shackles. There are trade-offs."
    "The tension crackles, a current you can almost taste — metal and wet paper and the tang of coffee gone cold."

    menu:
        "Tap the compass and hold your ground":
            "You press the brass to your throat, the metal a cold covenant. 'If Tideguard wants Havenport, they sign our terms, or they don't come at all,' you say, voice steady. Cassian watches the pendant as if it were a verdict."
        "Offer a concession — a phased oversight clause":
            "You let your fingers splay on the contract edge and suggest a phased approach: immediate protections paired with a legally binding review within eighteen months. Cassian's eyes sharpen; it's a bridge, but a narrow one."
        "Pause, ask for a break to consult Lina":
            "You reach for your tablet. 'Let me call Lina. She should see these clauses in full,' you say. Cassian's face hardens; transparency has already begun to move in the direction you feared."

    # --- merge ---
    "Continue"
    # [Scene: Lina Park's Office / Local Pressroom | Night]
    hide cassian_rhee
    hide marin_sato

    scene bg ch14_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The ping of an incoming message, a kettle's soft whistle miles away.]
    # play music "music_placeholder"  # [Music: Low cello, insistent]
    "Lina Park's fingers hover above the keys like someone poised on a cliff. You can't see her face from where you stand in the doorway, but you hear the certainty in the way she deletes parentheses and tightens a headline."
    show lina_park at left:
        zoom 0.7

    lina_park "If there's something to show, it belongs to the town. Confidential or not."
    show marin_sato at right:
        zoom 0.7

    marin_sato "Did Tideguard hand those clauses to you?"
    "Lina nods once, a small, grim movement."

    lina_park "Not willingly. But there were emails, Marin. Attachments with provisions about 'exclusive inlet access' framed as 'strategic operational zones.' It's not just about building walls — it's about privatizing passage."
    "You feel the room tilt under you. You had pushed for oversight for exactly this reason — fear of shadows in the fine print — and now the shadow has a face in the public square."

    "Lina Park (typing)" "I'll run the piece. Careful — this will make waves. It could sink the deal."

    marin_sato "Then it needs to sink. If the town isn't protected from decisions made behind closed doors, what protection is that?"
    "Lina stops typing and looks up. Her eyes are soft but iron-edged."

    lina_park "You're right. But there will be people who hate us for exposing it. Some might say we cost them shelter."

    marin_sato "And some might say we saved them from being barred out later. There's no clean answer."
    show lina_park at center:
        zoom 0.7

    lina_park "Then let's make sure the right to decide is theirs, not Tideguard's."
    "Her piece goes live before dawn. The headline is blunt; the article is surgical. It quotes the clauses, includes scanned pages, and frames the story as a choice between immediate armoring and long-term control. It spreads like a warning light."
    # play sound "sfx_placeholder"  # [Sound: Notification cascade; the faint chatter of incoming calls and messages.]
    # play music "music_placeholder"  # [Music: A single dissonant piano chord]
    # [Scene: Tideguard Corporate Pavilion | Night — Later]
    hide lina_park
    hide marin_sato
    hide lina_park

    scene bg ch14_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hard buzz of business — phones, the soft click of shoes in a corridor.]
    # play music "music_placeholder"  # [Music: Low, urgent strings]
    "Cassian reads Lina's article. His face goes through shifts, fast as weather."

    "Assistant (offscreen)" "Calls from investors are coming in. They want a statement."

    "Cassian Rhee (into the phone)" "We can issue a press release. This is…a misunderstanding, mischaracterized. Our plans are for community benefit."
    "Your demand for transparency has become a gale that pulls at corporate sails. The investors smell reputational risk and they circle away. He slams the tablet down once, the movement sharp."
    show cassian_rhee at left:
        zoom 0.7

    cassian_rhee "They'll think this is a governance nightmare. They'll pull. I didn't expect…"
    "He doesn't finish. Pride and calculation war in his silence."
    # [Scene: Market / Public Square | Morning]
    hide cassian_rhee

    scene bg ch14_3be532_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Raised voices, the slap of a vendor's hand against fresh catch, gulls complaining overhead.]
    # play music "music_placeholder"  # [Music: Minor-key strings, heavy]
    "The town is a map of divided lines. Some gather around Lina's printed copies, fingers tapping sentences; others stand with crossed arms, weathered faces raw with the practical terror of the seasons."
    "Elder Tomas Hale stands, small against the market's stone, his walking stick carved with seashells. He looks older than you remember — each line a tide mark."

    "Elder Tomas Hale (to you, voice thin)" "We traded walls for truth."
    "You can hear the accusation like a pebble dropping into a still pool. It ripples out, catching people you love in its wake."
    show marin_sato at left:
        zoom 0.7

    marin_sato "We traded a promise for the town's right to hold them to it."

    "Elder Tomas Hale (bitter laugh)" "And while we were holding them, the sea pressed. Where were the walls? Where were the nets? We have mouths that sleep with fear now."
    "The crowd erupts. Some say you acted with honor; others say you acted with the luxury of principle. Ivy pushes through, cheeks flushed, hands smelling of soil."
    show ivy_morales at right:
        zoom 0.7

    ivy_morales "He who builds the fastest sometimes listens to no one. But he who builds with everyone takes longer. We did what we had to do — to keep the right to choose."
    "A fisherman at the edge points a callused finger."

    "Fisherman" "My boats don't care about right and wrong. They need something to hold them when the next surge comes."
    "You feel the compass burn against your collarbone like a brand. Ariana arrives, but she keeps her distance in the doorway of the cafe, shoulders tucked, the blue streak at her temple catching light like an accusation of its own."

    "Ariana Voss (quietly, stepping closer)" "Marin…do you think Lina was right to print it? Did you—"
    "You can see the fear in her hands, the scientist's need for transparency wrestled with the builder's worry for immediate lives."

    marin_sato "I wanted oversight. I thought transparency would strengthen us."
    show ariana_voss at center:
        zoom 0.7

    ariana_voss "Instead the money left. The plan collapsed, and there isn't a wall tonight."

    marin_sato "I know."
    "Ariana's reaction is complex — equal parts admiration for your integrity, and a raw, practical exasperation."

    "Ariana Voss (voice taut)" "We could have had something, Marin. Even imperfect. Even partial. Now the funding window closed and the harbor is the same as yesterday."

    marin_sato "Would you rather have had a wall built by contracts that let them privatize access? Where half the town couldn't reach the water?"
    "She doesn't answer immediately. The answer lies in the crack between safety and sovereignty."

    "Ariana Voss (soft)" "I thought we were on the same side of this. I thought protecting people and protecting rights could be the same."

    marin_sato "They can be. But not when one side refuses to be bound."
    "Ariana's jaw tightens; words shrink into a stunned silence. She pulls back, folds into herself as if to become less visible."

    ariana_voss "I need distance. I…I'm afraid we opened a door I didn't mean to."
    "Her steps take her away from you. Ivy reaches for your arm and squeezes; the strength of the squeeze is not enough to stop the retreat."

    menu:
        "Call after Ariana, plead for a conversation":
            "You drop a step after her, hand raised. 'Please,' you say, voice small. She looks over her shoulder, eyes wet, and doesn't turn back. The space between you fills with sea-salt air."
        "Let her go and talk to the crowd":
            "You turn to the crowd instead, raising your voice. 'We did the right thing for the town's future,' you insist. Some nod; many don't. The market's roar swallows your words."
        "Find Lina and ask her to moderate the fallout":
            "You cross to Lina and whisper, 'Can you frame this as a path forward instead of a bomb?' She looks at you, pity and steel coiled in her face, and nods slowly."

    # --- merge ---
    "Continue"
    # [Scene: Unfortified Harbor | Dusk]
    hide marin_sato
    hide ivy_morales
    hide ariana_voss

    scene bg ch14_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The sea beating, an endless, patient percussion; seagulls calling tiredly.]
    # play music "music_placeholder"  # [Music: Brooding cello, descending motif]
    "You stand at the edge of the harbor and watch the water. It is not a dramatic wave crashing through a demolished wall; it's a persistent, insistent pressure — the kind that wears stone thin over"
    "seasons. The concrete that was meant to be temporary takes on a new vulnerability without the promised funding and engineered reinforcement."
    "Your compass feels absurd against the sea wind; the brass is colder now, as if the metal absorbed the town's new chill. Each swell slaps the embankment and sends up a fine, oily spray that tastes of iron and salt."
    "From the shore you can see the Tideguard banner, limp after the investors retreated; a corporate mouth with no teeth. The pavilion's lights burn, but not for long."
    show marin_sato at left:
        zoom 0.7

    marin_sato "I traded certainty for truth. The ledger is clearer. The paper is honest. The sea doesn't read paper."
    "Elder Tomas approaches, his steps slow, his face a map of small defeats."
    show elder_tomas_hale at right:
        zoom 0.7

    elder_tomas_hale "You did something few do. You demanded we be seen. But seeing does not stop a flood."

    marin_sato "I know. I keep coming back to the same question: did we act like guardians, or like children burning bridges because we couldn't bear secrets?"

    elder_tomas_hale "We did both, maybe. We cleared the rot. The rot needs throwing out. But sometimes the house collapses when you pull the beams."
    "You listen to his voice and hear the truth in it — truth that tastes like salt on your tongue."

    marin_sato "If I had done nothing — signed for the walls — would people have slept easier tonight?"

    elder_tomas_hale "Some would. Others would have woken to locked slips and new signs saying 'private.'"
    "He leans on his stick, looking over the water the way old men look at memory."

    elder_tomas_hale "You fought for the town's right to speak, child. But words are not mortar."

    marin_sato "No. They're not."
    "You fold your hands around your compass and close your eyes for a time, the sound of the harbor filling the hollow your certainty left behind."
    # [Scene: The Old Boathouse | Night]
    hide marin_sato
    hide elder_tomas_hale

    scene bg ch14_3be532_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain thin on the roof, the whisper of pages turning.]
    # play music "music_placeholder"  # [Music: Quiet piano, resigned]
    "You return to the boat's dim sanctuary. The lamp fogs your edges and shapes the room into small memories: the map your father drew, a jar of screws, a pocket with a faded photograph. The boathouse"
    "knows your hands, knows the way you measure a board. It is private and it is honest."
    "Ivy Morales sits at the workbench, sleeves rolled, nails stained with last week's repairs."
    show ivy_morales at left:
        zoom 0.7

    ivy_morales "People are angry. People are scared. Some wanted the wall; others want the control. We did what's hard."
    show marin_sato at right:
        zoom 0.7

    marin_sato "We did what's right for the long term. But the long term doesn't stop a flood tonight."
    "Ivy crosses the room and places a hand over yours. Her touch is warm; the pressure is real."

    ivy_morales "You're not alone. You never were."
    "You think of Ariana, of Cassian's face when the investors pulled back, of Lina's steady, dangerous pen, of Tomas' thin voice. The town has fractured; some pieces will mend, others will never align the same way again. The harbor remains unfortified, and for that there will be cost."

    marin_sato "I asked for transparency because I could not bear the thought of deals signed behind closed doors. I wanted the town to be an author of its future, not an address for someone else's balance sheet. The cost — the water, the fear — sits like ballast in my chest."
    "You stand and move to the window. The sea is a black smudge under the rain. Somewhere, a generator kicks and then dies. The room hums with small sounds: a drip, the fold of paper, nails tapping the wood of a boat frame."

    marin_sato "We kept the ledger clean. We kept the right to decide. We did not keep all of you safe immediately."
    "You let the sentence hang, not because it comforts but because it's the truth."
    "You unfasten the compass and place it on the map-strewn table. It is no longer a token of direction but a witness. You look at it as if it could tell you whether you acted rightly."

    ivy_morales "That compass points where you choose to walk. Maybe it's colder now. Maybe it'll warm when we start rebuilding — not just walls, but ways to govern them."

    marin_sato "Then we keep walking."
    "The boathouse is a small light against a town that will argue, that will lose and gain in strange measure. There will be nights when the tide feels like a punishment and days when seedlings in the nursery push up through damp soil like hopeful fingers."
    "You sit, place your hand over the compass, and for once let yourself feel the ache without trying to fill it with action. The hurt is honest. The town is divided. The harbour is vulnerable. The ledger is clear."
    "You breathe in the smell of oil and salt and old wood, and you accept the weight of what transparency cost. You cannot unwrite the headlines; you cannot unsay the clauses you demanded. You can only"
    "stand in the aftermath and do the work that truth makes possible — difficult, thankless, necessary work."
    # play music "music_placeholder"  # [Music: The piano falls into a single, low resolution chord]
    hide ivy_morales
    hide marin_sato

    scene bg ch14_3be532_7 at full_bg

    scene bg ch14_3be532_8 at full_bg
    "THE END"
    # [GAME END]
    return
