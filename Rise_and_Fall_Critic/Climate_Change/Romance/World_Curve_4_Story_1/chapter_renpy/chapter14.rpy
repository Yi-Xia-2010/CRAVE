label chapter14:

    # [Scene: Harbor Negotiation Hall | Late Morning]

    scene bg ch14_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmured conversation, the tick of camera shutters, distant gull calls, and an undercurrent hum of dockside machinery.]
    # play music "music_placeholder"  # [Music: Low, steady cello; a slow descending motif that never quite resolves]
    "Narration"
    "You stand at the head of the table with the copper locket warming against your sternum, the weight of the decision like a tidepool underfoot — full of life and quick with undercurrents you cannot always"
    "see. Cameras tilt toward you, but your eyes find Elias first; his jaw is taut with something that looks like hope and something that looks like calculation. Across from you, Rin rides that same careful line:"
    "smile practiced, posture angled to hold a room."
    show rin_voss at left:
        zoom 0.7

    rin_voss "This is the moment, Maia. Inclusion gives the TideGrid legitimacy it needs. Liaisons mean safeguards. We scale, we save."
    "Narration"
    "Her words are silver and exact. They land on the table like coins; they ring. You think of the terraces you helped stitch together, the pump that hums through Canal Twelve, Ibe's hands on new planks,"
    "Old Man Toma's stories braided into the neighborhood's nights. For a heartbeat your mind opens to the ledger of lives — the quantitative and the immeasurable — and they feel too close in number to ignore."
    show maia_soler at right:
        zoom 0.7

    maia_soler "Liaisons who can veto emergency measures. Liaisons with budgetary teeth. Transparent data access for communities."

    rin_voss "Reasonable. We'll formalize governance structures. We'll include training and automatic review cycles—"
    show elias_kade at center:
        zoom 0.7

    elias_kade "If we don't do this now, more people will die when the next surge hits. We can iterate the governance. We can make it better from the inside."
    "Narration"
    "You hear the press of urgency in his voice — the urgency that built the TideGrid — and you remember the inland neighborhoods he'd lost to waters. The gold fleck in his eye catches light and"
    "does not warm you the way it used to; it's turned precise, like a tool."

    maia_soler "I'm asking for mechanisms that cannot be unstitched by emergency directives. Community seats with binding authority, legal safeguards tied to public law, and—"

    rin_voss "—and a public oversight board, with rotating liaisons from recognized neighborhood groups. We'll bind the charter; I'll sign."
    "Narration"
    "When the pens are set out, the room smells of lemon oil and wet rope, of paper and sea. Your hand moves before the room can breathe. You sign. The signatures of Elias, Rin, the Mayor's"
    "Deputy, your name — an agreement that looks, on paper, like a bridge between scales."
    hide rin_voss
    hide maia_soler
    hide elias_kade

    scene bg ch14_6b08b4_2 at full_bg
    # play music "music_placeholder"  # [Music: String harmonics, a single upward bow that doesn't finish]
    "Narration"
    "You sign with the hope that liaison seats will protect vulnerable neighborhoods. You sign believing, against a gnawing biology of doubt, that there's room for both urgency and the small rituals you love. The photograph tucked"
    "in your locket is of an old dock you can still draw from memory; you press it like a promise against your ribs."
    # [Scene: Canal Twelve — Market Stalls | Months Later | Overcast Afternoon]

    scene bg ch14_6b08b4_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The chatter is thinner; bargaining is measured. A vendor's laugh is clipped by a nearby administrator's look. On the water, automated skiff routes glide without the random, human jag of neighborhood boats.]
    # [Smell: Steamed fish, but underscored by ozone and the faint scent of disinfectant]
    # play music "music_placeholder"  # [Music: A sparse, tremulous piano line; undercurrent of mechanical beeps]
    "Narration"
    "The Harbor shines the way a polished coin does — efficient, precise, engineered for flow. When the TideGrid took hold, pumps never faltered. Flood alerts fell. Lives were kept from quick ruin. But the pathways of"
    "what people did when the city breathed on its own — the rituals, the informal trades, the late-night storytelling that healed a day — they began to narrow like old channels being filled."
    show old_man_toma at left:
        zoom 0.7

    old_man_toma "They told me the hammock was a hazard now. Liability. They won't let me string the lights."
    "Narration"
    "He sits folded into a stool that used to be his throne during storytelling nights. His cloak, a patchwork of netting and colorful fabric, slides from his shoulders like a map of every market seam. You can see the dent in his voice where some nights used to sit."
    show maia_soler at right:
        zoom 0.7

    maia_soler "We fought for seats at the table, Toma. I thought—"

    old_man_toma "You sat at the table, child. That was brave. But some tables are built for different feasts."
    "Narration"
    "You taste metal in your mouth. You realize that 'community liaison' — once a word of protection — has been softened into 'consultant' in policy memos, then into a line item that committees fold away during"
    "crises. Emergency bureaucracies, the very mechanisms Rin promised would safeguard us, have broadened their mandate. Where you expected vetoes and budgetary teeth, you are handed channels and 'advice accepted' boxes."

    menu:
        "Call an emergency liaison meeting now":
            "You pull your jacket tight and pick up the secure comm-tab. Your fingertips jitter as you schedule the meeting; you'll speak with a loudness born of what you've lost."
        "Slip through the market to Toma's stoop and help him set up a private night":
            "You let the comm-tab cool in your pocket. You thread between stalls, lowering a faded tarp over Toma's stool, whispering about candles and old songs. For one hour, you steal a night back."

    # --- merge ---
    "You do both in the span of an afternoon because the things that must be done do not queue politely. You call. You gather. You whisper stories into the dark for Toma until his chest softens"
    "and the seams of his cloak glow for a little while under the borrowed lanterns."
    # [Scene: Liaison Office — Saltglass Annex | Evening]
    hide old_man_toma
    hide maia_soler

    scene bg ch14_6b08b4_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low cadence of bureaucratic language, the soft rustle of printed policies, a faint mechanical hum through the floorboards.]
    # play music "music_placeholder"  # [Music: Dissonant strings; a low sustained note that sets teeth on edge]
    "Narration"
    "The meeting is procedural, then defensive. A monitor flashes real-time metrics: water levels averted, people relocated preemptively, lives statistically saved. The numbers are clean; they glow like absolution."
    show rin_voss at left:
        zoom 0.7

    rin_voss "Our obligation is to save lives. When metrics dip, we centralize control to respond faster. The liaison model is intact; we simply streamline during emergencies."
    show maia_soler at right:
        zoom 0.7

    maia_soler "Streamline into decisions that bypass community vetoes. 'Emergency' has a way of becoming permanent."

    rin_voss "Emergency protocols can be reviewed after the fact. We will schedule oversight."

    maia_soler "After the fact is the whole point. After the fact, people have already lost markets, songs, elders' nights. We wanted seats so those losses wouldn't be decisions someone else could make for us."
    "Narration"
    "They nod. They write notes. The meeting ends with certificates and polite handshakes. The teeth you imagined in the safeguards are filing down into compliance forms and attachments."
    # [Scene: Elias's Workbench — Saltglass Research Lab | Night]
    hide rin_voss
    hide maia_soler

    scene bg ch14_6b08b4_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft clack of keys, the distant whorl of TideGrid pumps, a kettle hissing somewhere in the lab.]
    # play music "music_placeholder"  # [Music: A low piano; hesitant, searching]
    "Narration"
    "Elias meets you outside the lab after one of those review sessions. His palms are stained with grease; his breath fogs in the night air. He holds out a slate with visualizations: lives saved per projected"
    "storm, evacuations pre-empted, neighborhoods that would have been lost without the Grid. The numbers are patient and unyielding."
    show elias_kade at left:
        zoom 0.7

    elias_kade "Look. We delayed thousands of displacements in the last cycle. The Grid isn't theoretical anymore. It's saving people."
    show maia_soler at right:
        zoom 0.7

    maia_soler "I know. I watch the pumps. I watch the floodlines. I am not blind to the good it does."

    elias_kade "Then why—"

    maia_soler "Because saving life is not only about statistics, Eli. It's about how we let people live those lives. I sit in meetings where we approve a permit and then I see a child's night market vanish the next week. I helped build a machine that keeps bodies safe but narrows the ways we are allowed to be together."
    "Narration"
    "He studies you the way someone studies a complex diagram unfolding. His voice goes quiet and careful, the edge of policy slipping into the edge of something personal."

    elias_kade "I thought I was doing the right thing. I thought helping you make it hybrid would protect what mattered. When they pushed liaisons to advisory status—"

    maia_soler "You were not the hand that pushed them down, Elias. But you are part of the machine that now enforces the routes."

    elias_kade "If this is my fault, tell me how to fix it."
    "Narration"
    "You want to tell him everything — to unspool all the nights you spent comforting vendors whose permits were inexplicably delayed, to recount Toma's empty stool, to show him the ledger where 'efficiency' eats custom. But the ways to fix what hurts are not always technical."

    maia_soler "Fixing it isn't a schematic, not entirely. It's a willingness to insist on the hard parts of democracy when it's inconvenient. It's standing against Rin's emergency unilateralism when the cameras are off."

    elias_kade "And you think I haven't tried? I've pulled strings. I've argued in panels. They listen in numbers, but not in the way you want them to."
    "Narration"
    "He looks at you then, and something in his face tightens — not anger so much as distance layered over care. He reaches for you again and this time you let him, briefly. It feels like"
    "two people trying to fold themselves back into a single map when the continents have shifted."

    menu:
        "Let him hold you, let the grief be shared for a moment":
            "You close your eyes and let his arms carry some of the weight. For a few breaths the geometry of grief shifts and your shoulders unclench. When you part, there is salt on your face and a new faintness between you."
        "Step away and keep the space between you clear":
            "You step back, placing a distance between what he does and what you have to be. He nods, half-understanding, half-hurt. The comfort he offers cools into counsel."

    # --- merge ---
    "When you choose — whatever the choice you make — the result is the same: an honest, soft fracture. Elias's calculus is still his refuge; yours is not. You both love the city, but the measures of that love sit on different scales."
    "Narration"
    "When you choose — whatever the choice you make — the result is the same: an honest, soft fracture. Elias's calculus is still his refuge; yours is not. You both love the city, but the measures of that love sit on different scales."
    # [Scene: Canal Twelve — Dusk]
    hide elias_kade
    hide maia_soler

    scene bg ch14_6b08b4_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low murmur of automated announcements, a distant saxophone playing a tune you half-remember, a gull circling and calling once into the dim.]
    # [Smell: Salt and frying oil, with a shadow of exhaust]
    # play music "music_placeholder"  # [Music: A slow, low chord held under a minor key]
    "Narration"
    "You walk the market edge where the old and the new meet. Toma's stool is empty; someone left his cloak folded over the rail. You pick it up and smell of sun-worn rope and fish and other years. You press the fabric to your cheek. It smells like memory."
    show old_man_toma at left:
        zoom 0.7

    old_man_toma "You did what you thought right, Maia. You thought you could build a bridge and keep the old alleyways intact."
    show maia_soler at right:
        zoom 0.7

    maia_soler "We did build a bridge. I wanted it to be more than a crossing."

    old_man_toma "Bridges are not always chosen by those who step on them. They are often placed by those who build them. What matters is what you do now, and whether you keep bringing neighbors together."
    "Narration"
    "He pats the space beside him like he always does, offering company instead of answers. You sit. The harbor gleams — efficient, lit, reliable. It keeps people from drowning. It also keeps them from improvising the small, porous moments that made the city human."

    maia_soler "I wonder if there was ever a way to protect both lives and autonomy."

    old_man_toma "We are always asking impossible questions. Sometimes we get a part of the answer. Sometimes we lose parts. The work, child, is to keep replacing what is lost with what we can plant in its place."
    "Narration"
    "You fold the cloak into yourself for a moment like armor. You think of the locket, the photograph, the map of a shoreline that still exists in your hands if nowhere else. The TideGrid hums in"
    "the undercurrent, a guardian that has teeth and also a taste for order. Your role, now, is both creator and warden; every day you find yourself policing permits your signature helped legitimize, arguing in hearings about"
    "how to preserve smallness inside a system built for scale."
    hide old_man_toma
    hide maia_soler

    scene bg ch14_6b08b4_7 at full_bg
    # play music "music_placeholder"  # [Music: A single cello line that descends and settles]
    "Narration"
    "In the months since the signing, you've learned the contours of compromise. You have watched markets adapt. You have watched rituals be re-scheduled into permitted events that lose some of their edge and all of their"
    "spontaneity. You have been present when tide warnings saved children, and you have been present when a street orchestra's permit was denied because of 'operational risk.' Both truths sit in your mouth like salt."
    show elias_kade at left:
        zoom 0.7

    elias_kade "We did something, Maia. It saved people. It will save more."
    show maia_soler at right:
        zoom 0.7

    maia_soler "Saved, yes. But at what cost? I signed off on a machine that will create new routings for how we live. I wanted to protect the terraces and I helped make a thing that rationalizes them out of existence."
    "Narration"
    "He doesn't have an answer that satisfies you — no ledger line tallies the erosion of a market's culture. He has only numbers, and they are persuasive. You remember, though, the nights you spent with Toma"
    "stealing back story-telling under borrowed lanterns. You remember Ibe teaching kids to splice rope without a permit. Those acts persist in margins and cracks because you and others keep tending them like secret gardens."
    hide elias_kade
    hide maia_soler

    scene bg ch14_6b08b4_8 at full_bg
    # play music "music_placeholder"  # [Music: A low piano, a single suspended chord]
    "Narration"
    "You do not walk away from Elias in rage; you do not walk away in triumph. You walk away with a grief that is steady and companionable. You remain a steward of what you can, a"
    "critique of what you cannot. The relationship folds into a new geometry: close, competent, but sifted by different measures of care."
    show old_man_toma at left:
        zoom 0.7

    old_man_toma "Keep the locket warm, Maia. Let it remind you what you chose to save. Then decide what else you will save, even if it's only a corner or a song."
    "Narration"
    "You press the copper locket into your palm. It is warm from your skin, to be worn as both apology and vow. The harbor hums. Lights turn on, systems run, and people sleep in houses that"
    "would have been swept away. Markets shuffle under new rules. Storytelling nights happen sometimes, secret and smaller, in basements and along service alleys."
    hide old_man_toma

    scene bg ch14_6b08b4_9 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The TideGrid's steady pulse like a distant heart; one gull calls into the dark]
    # play music "music_placeholder"  # [Music: The cello resolves into a minor chord, then fades into quiet]
    "Narration"
    "You cannot unmake the bridge. You keep working in its shadow, naming losses aloud, making sure someone remembers the exact way Toma used to begin his tales. You lobby. You teach. You stitch new terraces where"
    "you can. You keep a place at your table for neighbors displaced by permits and policies. You carry the knowledge that saving lives and saving ways of life do not always arrive together, and that sometimes"
    "the only humane thing is to continue making space for the small irreducible things that grant a city its particular soul."
    "Final Visual: Close-up on your hand closing around the locket; the harbor's lights reflected in the metal, then the image pulls back slowly to show you standing at the water's edge, framed by the efficient glow of the TideGrid and the dark, living textures of the market beyond."
    # play music "music_placeholder"  # [Music: Fade to a single, sustained low note]

    scene bg ch14_6b08b4_10 at full_bg

    scene bg ch14_6b08b4_11 at full_bg
    "THE END"
    # [GAME END]
    return
