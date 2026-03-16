label chapter8:

    # [Scene: Council Hall | Late Afternoon]

    scene bg ch8_6b08b4_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense BGM — low strings and a ticking percussive loop]
    # play sound "sfx_placeholder"  # [Sound: Paper rustle, distant gulls, a muffled projector beep]
    "You step into the chamber and the air hits you—a mix of stale coffee, disinfectant, and the thin metallic tang of urgency. The room is warmer than outside, full of bodies that talk in precise sentences"
    "and hold private alarms behind polite faces. The seawall's blueprint is projected on the far wall: a hard, schematic promise of safety that already smells faintly of concrete and contracts."
    "Livia sits at the head of the table like a tide mark: composed, immaculate, the gold wave-brooch catching the window light. When she looks at you, her smile is measured; something behind it calibrates your position in the chorus of power."
    show livia_chen at left:
        zoom 0.7

    livia_chen "Mara. Thank you for coming. We need someone to steward the environmental oversight. Your voice—your credibility—would reassure the town."
    "You feel the words as a weight and a lever at once. Oversight. Steward. The council's gesture is a glove placed on your hand: both an honor and a harness."
    "You clear your throat, fingers curling around the edge of a briefing packet. Your heartbeat has shifted to a march you cannot ignore."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "I'll consider it. Oversight must be enforceable—covenants that protect the rows, community rooftops, and operational control by locals."
    "Livia's smile narrows just enough to be a conversation. She taps a redline on her tablet and slides it toward you."

    livia_chen "Financiers are watching margins, Mara. Each covenant changes a line on a balance sheet. We can include cultural protections where feasible, but top-line stability is the priority. Jobs, insurance rates—these are what will convince investors."

    mara_kestrel "If the protections are 'where feasible' as a clause, they're not protection at all. They're a suggestion."
    "Livia leans forward, the room tightening with her gravity."

    livia_chen "Suggestions don't secure grants, Mara. Compromise secures projects. I'm asking you to be the public face that makes that compromise look principled."
    "Her eyes don't ask. They assume you'll accept the framing: you, the scientist, turning the language of safety into a seal of consent."
    hide livia_chen
    hide mara_kestrel

    scene bg ch8_6b08b4_2 at full_bg
    "Dr. Naomi Park clears her throat from the side, papers in her hand, the clinical steadiness of someone trained to make trade-offs by decimal."
    show dr_naomi_park at left:
        zoom 0.7

    dr_naomi_park "From hydrodynamic models, the seawall decreases overtopping risk by fifty to seventy percent depending on storm intensity. But the trade-off is sediment displacement along the southern flats. We've modeled offsets—managed retreat in targeted corridors—but that requires funding and community buy-in."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "We can't quantify what it costs to tear down someone's street. Models don't map memory."
    "Naomi gives you a look that's sympathetic and sharp."

    dr_naomi_park "They're not the same language, Mara, but they're both true. If you're on the panel, you'll have to translate between them—and decide where to apply force."
    "The conversation ricochets—technical terms and human terms colliding. You speak; they speak back. Voices layer until the room feels like a tide pool of competing imperatives."
    # play sound "sfx_placeholder"  # [Sound: A phone buzz. Tess's voice is low, urgent at your elbow.]
    show tess_omalley at center:
        zoom 0.7

    tess_omalley "There's a discrepancy in Clause 7B—escrow accounts earmarked for 'community transition' have a permissive release clause. It's not a mistake. It lets money divert to outside developers with minimal oversight."
    "You feel the room shrink. Tess's cheeks are flushed; she's a small island of earnestness in a sea of polished arguments."

    menu:
        "Ask Tess for the clause now, here in public":
            "You raise Tess's concern, voice steady. The table freezes; Livia's smile becomes a stone. Investors clear their throats; the tenor shifts to damage control."
        "Signal Tess to speak only to you later":
            "You make a subtle gesture. Tess nods and tucks her worry away. The meeting continues; danger swims beneath the surface, unseen by most."

    # --- merge ---
    "'You pick the second option—politics is a living thing and you don't want to bleed it in the open yet. Tess gives you a quick, grateful squeeze of the hand under the table, an ally's furtive warmth. The meeting proceeds with Livia managing optics like a conductor.'"
    # [Scene: Conference Room B | Early Evening]
    hide dr_naomi_park
    hide mara_kestrel
    hide tess_omalley

    scene bg ch8_6b08b4_3 at full_bg
    # play music "music_placeholder"  # [Music: Tense BGM intensifies — high strings, a sharper tempo]
    # play sound "sfx_placeholder"  # [Sound: Keyboard clicks, low murmurs, the scrape of a pen]

    "Contractor" "Each covenant adds cost. Every rooftop clause, every preservation action—it's a line item. Investors demand certainty. If we can't guarantee ROI, funds move. That's simple."
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "Guarantees are different from assurances. You can't promise culture with a line in a contract and call it preserved."

    "Contractor" "We operate in markets. We can mitigate. We can allocate community spaces. But locking land-use restrictions for decades alters the cost structure and the project timeline."
    show dr_naomi_park at right:
        zoom 0.7

    dr_naomi_park "If we phase in covenants tied to performance milestones—emissions, habitat restoration, community governance—it's possible. It complicates the legal boilerplate, but it's not impossible."
    "The contractor's jaw tightens. Livia smiles with a patience sharpened by practice."
    show livia_chen at center:
        zoom 0.7

    livia_chen "We can write milestones. We can build assurances. But cash flow is the heartbeat here. Delay scares funders. Mara, if you drag oversight to the legal limit, we risk having the wall built by others—or not at all."
    "You feel each syllable like a tiny fracture in the ground beneath you."

    menu:
        "Push for immediate legal definitions of every covenant":
            "You propose hard definitions and timelines. The contractor's face hardens; Livia's fingers hover near her tablet—an unspoken ledger tick. The room responds with a chill of 'impractical'."
        "Suggest a phased pilot with escrowed funds held by a neutral third party":
            "You offer a middle path. Heads tilt. It's not a victory, but it's a draft of safety—something the financiers can test without gutting community control outright."

    # --- merge ---
    "'You blur the line between both—suggesting pilots with milestones—because both Naomi and you know that perfect doesn't exist in the room's accounting ledgers. The contractor agrees, guardedly.'"
    # [Scene: The Arbor | Night]
    hide mara_kestrel
    hide dr_naomi_park
    hide livia_chen

    scene bg ch8_6b08b4_4 at full_bg
    # play music "music_placeholder"  # [Music: Abrupt low percussion, heartbeat-like]
    # play sound "sfx_placeholder"  # [Sound: Drip of a leaky spigot, the rasp of Eli's breath]
    "You come back smelling of council hall air and polished wood—two worlds layered on your coat. The Arbor's warmth hits your skin like a reprieve and then a reminder: here, things are made by hands that remember how to fix what breaks."

    "Elias 'Eli' Rowan" "You were the face of oversight, right? You said you'd be the town's conscience. I watched them hand you the pen and the sword in the same breath."
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "I asked for covenants. I pushed for pilots. I'm not—"

    "Elias 'Eli' Rowan" "You let them put pretty stamps on irrevocable redlines, Mara. You gave them a narrative they could sell: 'community steward.' While the trucks roll, the same people who'll manage the jobs will manage the leases. They'll 'revitalize' the rows until no one recognizes them."
    "His voice is low, raw. The heat of the greenhouse does nothing to thaw the way he looks at you—complex, unreadable. For a second you see the man who believes machinery can be honest and the man who learned the hard lesson that it can be used to erase."

    mara_kestrel "You're right to be angry. I'm angry too. But someone has to be at the table to make sure the pilot language is defensible. To make sure the rooftop programs stay community-run."
    "Elias 'Eli' Rowan slams the wrench into the bench—metal sings against wood."

    "Elias 'Eli' Rowan" "That's what you always say: 'someone has to be at the table.' But sometimes the table is set to swallow you whole. You know how easily 'pilot' becomes permanent absence."

    mara_kestrel "And letting the wall not be built—people lose homes to storms. I can't watch them get washed away because I refuse to sign a word."
    "Elias 'Eli' Rowan's hands go slack, and for the first time his voice is uncertain."

    "Elias 'Eli' Rowan" "So you split the difference. You become the moral fig leaf that makes their sale look like stewardship."
    "You don't answer because your throat is full of the same split—wanting both to hold people in place and to keep their memories intact. You taste salt and rust and the overwhelming, brittle fatigue of compromise."
    # play sound "sfx_placeholder"  # [Sound: A hurried knock. Tess slips in, rain beading on her collar, eyes wide and luminous in the greenhouse light. She holds a slim file like contraband.]
    show tess_omalley at right:
        zoom 0.7

    tess_omalley "Mara. I couldn't leave it anywhere. I—' (she exhales) 'There's a schedule buried in Clause 7B. Escrow releases to an outside holding company if 'development metrics' are met. It's written so funds can be reallocated without town approval."
    "You feel the room tilt; the greenhouse hum becomes a distant drone. Eli's jaw hardens; Naomi, who has entered behind Tess, goes still."
    show dr_naomi_park at center:
        zoom 0.7

    dr_naomi_park "If that clause is true, money can slip law like water. Legal protections become décor."
    "Tess hands you the file. Her fingers tremble."

    tess_omalley "I could leak it. Force a renegotiation. Make the whole thing public. But I—' (she swallows) '—I don't know if we can handle what comes after. Funding freezes. Jobs delayed. People panic."

    mara_kestrel "If it's leaked, the project could be derailed—or it could be improved. But there's no neat outcome. There are losses either way."

    "Elias 'Eli' Rowan" "There are always losses, Mara. The question is whose."
    hide mara_kestrel
    hide tess_omalley
    hide dr_naomi_park

    scene bg ch8_6b08b4_5 at full_bg
    # play music "music_placeholder"  # [Music: Tense BGM crescendos into a brassy, urgent discord]
    "Your pulse accelerates. You imagine the headlines, the town meetings, the contractors' lawyers circling like sharks. You imagine Grandma Hira's stoop empty, the children who learned to fish from Rafi out of work, the rooftop gardens torn down for glossy terraces."
    "Everything compresses into a point: decision."
    "Tess leans in so close her breath fogs yours."
    show tess_omalley at left:
        zoom 0.7

    tess_omalley "We can leak this and force them to the table. Or we can push for binding covenants and risk contractors withdrawing. Or—you sign, you publicly support the project, and the wall goes up quickly."
    "You hear Livia's earlier words echo—compromise secures projects. But now compromise tastes like something colder: a negotiated surrender disguised as stewardship."

    menu:
        "Tell Tess to release the file to the press":
            "Tess nods, relieved and terrified at once. Naomi runs her hand through her hair, already calculating the fallout. Eli's face goes ashen; in his eyes, you see the immediate rip of community trust shredded—then the possibility of a stronger covenant if it survives."
        "Tell Tess to hold the file while you draft enforceable clauses":
            "Tess exhales slowly, the small relief of a plan. Naomi brightens with method. Eli remains unconvinced—hands balled, the idea of prolonged legal battle a new wound."
        "Tell Tess to destroy the file and let you sign the agreements publicly":
            "Tess recoils at the idea, moral nausea visible in her posture. She shakes her head. Eli's anger becomes a physical thing; Naomi's face tightens, grief braided with practicality."

    menu:
        "Sign on publicly to accelerate construction.":
            jump chapter9
        "Leak Tess’s documents to force renegotiation.":
            jump chapter13
        "Insist on legally binding environmental covenants.":
            jump chapter17
    return
