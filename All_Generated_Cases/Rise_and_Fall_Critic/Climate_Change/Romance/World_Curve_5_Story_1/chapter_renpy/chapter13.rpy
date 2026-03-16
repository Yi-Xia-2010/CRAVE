label chapter13:

    # [Scene: City Hall / Planning Office | Morning]

    scene bg ch13_f99e88_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm, ascending strings; a quiet brass line that suggests steadiness]
    # play sound "sfx_placeholder"  # [Sound: Murmured conversations, the soft squeak of chairs, a single gull somewhere outside]
    "You step into the hearing room like you're stepping into the mild center of a storm: the air is cooler here, conditioned and precise, but your pulse still tastes of salt from the bay. You can"
    "feel the weight of what happened in the night—the leak, the chants, the sudden shudder of public opinion—and how all of it poured into this thin, formal place."
    "Mayor Lin stands at the dais with a small stack of papers in her hands. Her bun catches the light like a shield. Jonah Hale is to your left, sleeves rolled beneath his raincoat, expression neat"
    "and practiced; he looks like someone who can sign a contract without smudging ink. Asha is there beside you, palms stained with plant soil, fingers worrying the edge of a data pad; she meets your eye"
    "and offers the smallest, steadying nod."
    show mayor_lin_park at left:
        zoom 0.7

    mayor_lin_park "By unanimous vote of the council and with the consent agreements from community representatives, City Hall endorses the Relocation Accord. It is voluntary, it offers guaranteed job placements in the ecosystem initiatives, and establishes a civic fund to seed community land trusts. Oversight committees will include residents, scientific advisors, and the town's council."
    "You listen to the words and count the promises like measurements on a tide chart. The phrase 'guaranteed jobs' hums in your chest—Asha's pilot workshops, Ruben's apprenticeships in native arboriculture, the tide labs scaling into more"
    "paid positions. 'Civic fund' smells like foundation meetings and long nights, but it also smells like seed money and the possibility of land that stays in community hands."
    "Jonah Hale leans forward, voice even."
    show jonah_hale at right:
        zoom 0.7

    jonah_hale "The consortium will, contingent on the oversight schedule, deploy transitional funds immediately. We'll allocate temporary housing vouchers and begin remediation grants. We expect measurable milestones—employment targets, restored acres—to unlock further investment."
    "You feel a familiar pinprick of mistrust—Jonah Hale's contingency is a loop of conditions—but you also feel the real, hard fact of the vouchers stacked on the table. People moving with assurance, not force, is a difference that keeps faces and stories intact."
    show asha_mehta at center:
        zoom 0.7

    asha_mehta "Our monitoring will run. If the core sensors detect anomalous seepage, we'll trigger slow relocations and managed shoreworks—no surprise evacuations. We keep people safe and dignified."
    "You open your mouth because the room needs translation: the legal terms into the living language of families, orchards, school plays. You find yourself saying things you didn't plan for—small, precise comforting words that insist there will be aides, there will be retraining, there will be long-term stewardship."
    hide mayor_lin_park
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "We will hold Jonah to the oversight committees, Mayor. We will sit in the meetings, we will set those milestones, and Asha's team will publicize every step."
    hide jonah_hale
    show mayor_lin_park at right:
        zoom 0.7

    mayor_lin_park "That's the point of the oversight clause. This must be community-led in practice, not only in name."
    "Jonah Hale's gaze shifts to you. For a breath, the engineer in him and the man assigned to fix things make a narrower, human angle. He nods as if understanding the tenor of the room."
    hide asha_mehta
    show jonah_hale at center:
        zoom 0.7

    jonah_hale "Agreed. I don't want to build something that erases what made Lowry Bay worth saving. We'll formalize the committee roster this week."
    "The applause is modest, careful—not euphoric, but genuine. You tuck your notebook back into your jacket and feel the tide of responsibility inching forward in your ribs. The accord is approved. The work begins in a different register: logistics and good-bye, hauling and cataloging and creative grief."

    menu:
        "Stand and publicly thank Jonah for the funding":
            "You rise, voice even. 'Thank you—on behalf of everyone—only if oversight means oversight.' Jonah nods, a brief, human flash in his eyes."
        "Emphasize community ownership instead":
            "You stand and put your hand on the stack of community proposals. 'This money must serve us, not buy consent.' The room leans, listening; Jonah's smile tightens but doesn't retract."

    # --- merge ---
    "The scene continues to the moving day on the boardwalk."
    # [Scene: Boardwalk | Afternoon — Moving Day]
    hide mira_kestrel
    hide mayor_lin_park
    hide jonah_hale

    scene bg ch13_f99e88_2 at full_bg
    # play music "music_placeholder"  # [Music: Woodwind countermelody over steady percussion; a light choir-like hum of many voices]
    # play sound "sfx_placeholder"  # [Sound: The creak of handcarts, the laughter of children, distant hammers]
    "You walk the boardwalk like one of those old tide maps Ruben used to trace with a stick: slowly, reverently, taking note of stretch after stretch of neighborhood being lifted in small pieces. A neighbor passes"
    "you, carrying a plastic tote of jam jars and a child's broken toy; their face is set but gentle. Another family moves a weathered rocking chair, the wood worn by a dozen summers."
    show nadia_kestrel at left:
        zoom 0.7

    nadia_kestrel "We're doing the last scene outside. We read about the orchard and the tide, and then we hang the lanterns. Everyone's bringing something—my teacher knitted the seagull banner."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "You didn't have to organize this, Nade."

    nadia_kestrel "Yeah, I did. For the record, this is the part where I thought of you. You taught me how to count the tidelines when I was five. I thought—it's right."
    "You watch the children rehearse a small, earnest tableau: a child holding a jar of soil, another cradling a paper apple, a chorus of tiny voices reciting lines about memory and new ground. The play is imperfect and gorgeous; it's the kind of human measure a contract can't quantify."
    "As families shoulder their boxes, you find Ruben at the edge of the orchard with a small notebook and a battered crate of saplings. He has salt in his hair and a grin that is more like a bruise—worn, true."
    show ruben_ortega at center:
        zoom 0.7

    ruben_ortega "We have forty-two heirloom saplings cataloged for relocation. Apples, pears, three chestnuts. We wrap roots in burlap and tape. We tag them with names. You want the ledger? You want to give them a proper place?"

    mira_kestrel "Yes. We'll find soil. We'll keep their names with them."

    ruben_ortega "Good. Names matter. Roots remember where they're from. So should we."

    menu:
        "Help Ruben tag a sapling":
            "You take the tag and write 'Kestrel Orchard — Mira's House' with a shaky hand. Ruben pats your shoulder like a weathered mapmaker handing you a compass."
        "Walk the boardwalk to check the housing vouchers":
            "You squeeze Nadia's shoulder and head toward the makeshift intake tent. The line is long but orderly; volunteers hand out vouchers with steady hands. The system is messy but kind."

    # --- merge ---
    "The scene continues to the Higher Ground overlook at dusk."
    "You feel both proud and hollow—the cord of memory tugging at your sternum. Boxes of orchard soil are ferried in wheelbarrows; people choose which belongings to carry and which to leave behind with the land. The town isn't abandoning itself; it's carrying pieces to higher ground like offerings."
    # [Scene: Higher Ground Overlook / Dusk]
    hide nadia_kestrel
    hide mira_kestrel
    hide ruben_ortega

    scene bg ch13_f99e88_3 at full_bg
    # play music "music_placeholder"  # [Music: Solo guitar and soft cello; the chord progression lifts gently]
    # play sound "sfx_placeholder"  # [Sound: Brushes on wood, soft murmurs, the distant slap of water]
    show cassian_rhys at left:
        zoom 0.7

    cassian_rhys "I'm painting the leaving and the staying together. No one erased. No one forgotten. I put a child with a jar of soil—like Nadia's play."
    "You crouch beside him, watching the mural take shape. His strokes are defiant and delicate, a public elegy and a promise stitched into color."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "It's beautiful."

    cassian_rhys "Someone has to make it beautiful. Otherwise the maps are all contracts and no one remembers the picnics."
    "You speak about practical things—how Asha's sensors will interface with the oversight schedule, how Ruben's apprenticeships will fold into Tidelab's workshops. Cassian interrupts at one point, his knuckles stained."

    cassian_rhys "Mira, we can't let this be a story about loss only. We have to make it a story about new land, new work, the orchards planted where they're safer. We have to keep people involved—jobs that keep hands in soil and eyes on the water."

    mira_kestrel "We will. Retraining programs, paid internships, apprenticeships with Ruben. The civic fund will buy land so families can own the new plots collectively. We make sure the displaced are not dispersed; they are relocated with dignity."
    "Cassian Rhys looks at you then, long enough for all the private things to press at the surface—the childhood summers, the fights, the times you sheltered each other from storms."

    cassian_rhys "Promise me one thing, Mira."

    mira_kestrel "What?"

    cassian_rhys "That whatever marker we put here—mural or ledger or sapling—it's a living thing. We tell the stories. We show up for their harvests. We don't let 'relocation' become an excuse to forget."

    mira_kestrel "I promise."
    "Ruben chimes in from where he stands, ledger open, dust on his knuckles."
    show ruben_ortega at center:
        zoom 0.7

    ruben_ortega "A promise is only work. You know that, child. Keep doing the work."
    "Asha joins you, cheeks flushed with cold and exertion, fingers tapping data into her pad even as she wraps wire around a sensor."
    hide cassian_rhys
    show asha_mehta at left:
        zoom 0.7

    asha_mehta "The network's live. We'll publish the sensor streams publicly—no black boxes. If anyone's concerned about Jonah's conditions, they'll see data and they can call foul. Transparency is built in."
    "Jonah Hale stands a little apart, watching the mural and the people. He comes over and sets a small stack of envelopes on a crate—administrative grants, clearly stamped. His usual reserve has softened in these last hours; you hear the honest tremor in his voice."
    hide mira_kestrel
    show jonah_hale at right:
        zoom 0.7

    jonah_hale "I didn't come back here for trophies. I came because this town has history worth saving. If oversight means a seat at the table for people like you, then I will sit and listen."
    "You look at the mural in progress, at families stringing lanterns, at Nadia's small troupe who have just finished their play and are now passing out paper apples to adults. There is grieving in every smile;"
    "absence shapes the way people fold together. But there is also an architecture of care—vouchers, jobs, funding, sensors, lists of saplings labeled with names."
    "You feel pride as if it's a weight placed on your shoulders by the town itself; you carry it with a hollow room in your chest where your childhood home's porch used to be. Still, the hollow is not empty—it's a place where new stories can be set."
    "Cassian Rhys wraps an arm around you under the warm halo of the lanterns. His cheek brushes yours, and you can smell oil paint, rain, and the faint sweetness of old apple trees."
    hide ruben_ortega
    show cassian_rhys at center:
        zoom 0.7

    cassian_rhys "We rise from this. We make places where people can come home."
    hide asha_mehta
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "We will make them come home."
    "You stand under the lantern glow with him, with Nadia's small paper apple held in your palm, with Ruben cataloging names into the ledger, with Asha tapping the first public feed into the town's stream. The mural's colors dry into the grain of the wood like memory settling into place."
    "You think of the families who are already unloading trucks on higher ground and the ones who will wait to see if the new plots yield fruit. You think of all the small acts that fashioned"
    "the accord—the late-night meetings, the protests that pulled public attention, the technical charts that saved months of missteps. You have helped stitch safety into policy and tenderness into practice."
    "There is still grief. There will always be a quiet house on the map where someone's laughter once lived. But there is also the rising shape of something else: a town that remembers by doing the"
    "hard work of care. You feel the ascent in the air, not as denial of loss but as a promise that the town's next chapters will be written with the displaced included."
    "You breathe in the scent of lantern smoke and wet earth, and for the first time in many nights you imagine a next season where the orchards you planted bear more than rusted memories—they will yield fruit and jobs and a map that lists names and root places together."
    "Cassian Rhys squeezes your hand, and you let the moment hold you like a buoy."
    hide jonah_hale
    hide cassian_rhys
    hide mira_kestrel

    scene bg ch13_f99e88_4 at full_bg
    # play music "music_placeholder"  # [Music: Strings resolve into a gentle, rising chord; the sound is hopeful and steady]
    # play sound "sfx_placeholder"  # [Sound: The murmur of conversation becomes a sustained, warm hum]
    "You rise from the wreckage. You begin to rebuild a community that remembers what it lost and keeps those memories in the places people now call home."

    scene bg ch13_f99e88_5 at full_bg
    # play music "music_placeholder"  # [Music: Warm strings linger and then resolve into silence]

    scene bg ch13_f99e88_6 at full_bg
    # play music "music_placeholder"  # [Music: A single piano motif, clear and hopeful]
    "You have done the thing you feared: made a decision that risks comfort to preserve people and stories. It was messy. It was necessary. In the quiet after the moving, there is work: grafting saplings, teaching"
    "new trades, tending sensor feeds, showing up for harvests. There is grief; there is laughter. There is a mural and a ledger and a town that will, on its better days, say the names out loud."
    "You are proud and hollow, and in that double feeling you find a steady center. Love lives here—in the hands that pass a crate of soil, in the promises written into oversight, in the paint on"
    "Cassian's jacket. The accord is not an ending. It is a new, careful beginning—built from the labor of people who chose each other, and who chose to remember."

    scene bg ch13_f99e88_7 at full_bg
    "THE END"
    # [GAME END]
    return
