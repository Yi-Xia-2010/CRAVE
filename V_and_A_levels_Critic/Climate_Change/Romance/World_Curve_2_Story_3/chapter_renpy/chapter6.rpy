label chapter6:

    # [Scene: New Promenade | Midday]

    scene bg ch6_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Brass fanfare twisted into a minor key; percussion tight and relentless]
    # play sound "sfx_placeholder"  # [Sound: The low thrum of pumps; a distant gull; the clack of boots on new boardwalk planks]
    "You arrive already loud in your head — a pulse you can't quiet. The air tastes of salt and fresh concrete, with an undercut of motor oil and disinfectant. The promenade smells like a place that"
    "intends to be permanent: new timber, sealant, the clean iron of galvanized railings. It also smells like absence, in the way empty rooms hold the shape of the people who used to fill them."
    "Construction lights flare off the plinth where Cassian speaks. His voice is smooth, rehearsed to mercy's edges. Around him, cameras angle and re-angle; the crowd is a patchwork of applause and small, private griefs."
    show cassian_vale at left:
        zoom 0.7

    cassian_vale "Immediate action. Decisive infrastructure. We saved Verdante."
    "You hear, beneath the applause, Tamiko's camera lens clicking quietly like a heartbeat measured against a falling tide. You see Lina standing a few meters back, hands clamped to the rolled 'Relocation Options' leaflet that used"
    "to be a menu for her storefront. Her face is small in the crowd, mouth closed like someone who has swallowed a cry."
    "A worker hands a child a commemorative pin. The child fidgets it onto a sleeve the way people try to attach histories to new surfaces."
    "You remember the ethics review, the delays, the petitions — all of it a slow, threaded hope. They were not enough. Private contracts looped the city into a timetable that didn't wait for consent. The emergency"
    "branding became a legal wedge; the hammer fell before you could wedge anything into the gears."
    hide cassian_vale

    scene bg ch6_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmured negotiation — city counsel speaking into a phone; the rattle of keys; someone sobbing muffled beneath another's sleeve]

    "Lina's storefront is a boarded rectangle now, one hand-lettered sign flapping against oak" "FOR LEASE — RELOCATING."
    "You move toward her because movement is the only kind of argument you can make. Your scarf is a knot at your throat and it feels too small for the wind."

    menu:
        "Go to Lina first":
            "You step across the fresh concrete, each footfall loud. Lina's shoulders fold into you like a doorway closing; she lets you hold the leaflet and you both watch a crew load the last of her shelving into a white van."
        "Stay and watch the ceremony":
            "You let your back lean on the rail, watching Cassian's smile set like concrete. Tamiko's camera finds your face and holds it; for a horrible second you feel like an exhibit to your own losses."

    # --- merge ---
    "Resume narrative at the next scene."
    # [Scene: New Promenade — Edge of Ceremony | Continuous]

    scene bg ch6_4001e7_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The applause trails; conversations continue like a current that has split around a rock]
    "You find him after the plinth clears — Elias with his messenger bag at his hip, a fold of a proposal in his hand that used to be a civic plan and is now an annex"
    "to someone else's ledger. He's quieter than you expected, and quiet has a different weight now — not consideration but the muffled throb of something too large to voice."
    show elias_moreno at left:
        zoom 0.7

    elias_moreno "Mira."
    "Your name in his mouth is a small, dangerous thing. It presses a bruise you didn't know you'd had."
    show mira_santos at right:
        zoom 0.7

    mira_santos "You chose them."
    "He flinches — not from what you said but from the accuracy of it."

    elias_moreno "I didn't choose this. They pushed me out of the office. There were votes, pressure. I—"

    mira_santos "You accepted their oversight role. You signed the memorandum this morning. You—"
    "Elias shuts his eyes for one long beat as if closing them will rearrange what happened. When he looks at you again his gaze is raw with explanation rather than defense."

    elias_moreno "They offered a package — oversight, influence inside, a seat at the table that will shape the implementation. I thought— I thought if I went in, I could keep the worst parts from happening. I would be able to make sure the guarantees were enforced."

    mira_santos "Guarantees. The words look different when they're written on Vale letterhead. Do you think their 'guarantees' carry the same weight as the neighborhood's lived memory? Do you think they care where Lina's pantry used to be, or whether Tamiko's footage will be archived under 'success'?"

    elias_moreno "I— I wanted to stop them from doing harm. Turning them down meant stepping aside. I—' [he swallows] 'They made me choose between my job and a role where I could try to shepherd the construction. I thought the second would let me salvage something."

    mira_santos "That's not salvage. That's permission."
    "Elias's hands, which used to fold models and trace compromise on layup tables, fumble with a corner of his proposal. There is a tremor in his voice you have never heard before."

    elias_moreno "I know what permission looks like to you. I know what this building represents. I lost my office because I stood up. They could have blacklisted me entirely. This — this was an offer that still let me do work."

    mira_santos "You have a way with structures, Elias. You always believed blueprints could save people. You put the lines before the lives in the end."
    "For a blink you think he will strike back with words sharp enough to cut — allegations of naivety, of moral grandstanding — but he only exhales, a sound like a slide of a window closing against weather."

    elias_moreno "I thought I could be the exception. I thought my presence would mean better terms, better oversight. Maybe I was trying to protect you, in the most foolish way I know how."

    mira_santos "Protect me? You aligned with the hand that parcelized my neighborhood."
    "Elias's face crumples, then sets into an expression you will remember because it is the one that says complicit and apologetic at once."

    elias_moreno "I am sorry. I am —"

    mira_santos "Don't apologize like that. I'm tired of apologies that come with contracts."
    "He steps closer as if to bridge something; you step back as if reflexively protecting the row's geometry in your chest."

    elias_moreno "They pushed me out. I thought by staying close I could pull them back from the most damaging edges. Maybe I misjudged. Maybe I—"

    mira_santos "Maybe you prioritized a plan over the people who still live in it."
    "He reaches for you briefly — not in accusation but in plea — and the air answers with the sound of someone slamming another cardboard shop window closed down the block."
    # play music "music_placeholder"  # [Music: Percussion intensifies; a metallic, urgent staccato]
    # play sound "sfx_placeholder"  # [Sound: A distant megaphone announces "Relocation Assistance now available"; Tamiko's voice mutters into her recorder: "—and yet they did not—"]

    elias_moreno "I can't undo what happened today. But I can try to make the implementation less destructive. I can—"

    mira_santos "You can try. You can 'try'. The row needs someone to refuse the terms, Elias. Not someone to make them prettier."
    "He looks at you like a man who has misread the map and found the coastline instead of the city. There is something like a sob in the way he inhales."

    elias_moreno "I don't want to lose you. Not like this."

    mira_santos "You already made that choice when you shook Cassian's hand."
    "He stumbles as if the words are physical. Around you, life moves — a crew pulling a banner taut, a volunteer handing water to a displaced family. The noise makes the moment a public unravelling."

    elias_moreno "If I leave, they win. If I stay, I lose you. I— I thought I could do both."

    mira_santos "You can't choose to be in the machinery and not get grease on your hands."
    "He looks away, jaw working, then meets your eyes and the admission there is heavy with damage."

    elias_moreno "Maybe I'm not brave enough to stand outside and stop it. Maybe I'm only brave enough to stay and try to steer. I don't know how to be the person you need me to be."
    "You don't answer. Your throat is tight with words that would make him stay if you spoke them; with words that, spoken, would pull the last seams of the neighborhood open."

    menu:
        "Demand he resign from the oversight role":
            "You say it clearly, loudly: 'Resign.' The crowd doesn't quite hear but Tamiko's camera does. Elias's face goes white. He opens his mouth, closes it, then shakes his head as if dislodging a sudden, painful thought."
        "Turn away without answering":
            "You drop your gaze to your notebook and start to zip it closed. The motion is small, mechanical; Elias reaches for your hand and misses. The distance clamps between you like a hinge."

    # --- merge ---
    "Resume narrative at Mariner's Row."
    # [Scene: Mariner's Row | Late Afternoon]
    hide elias_moreno
    hide mira_santos

    scene bg ch6_4001e7_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slap of a closing box; a tape-measured sigh; a distant, isolated cheer from the promenade]
    "Tamiko moves among families collecting what they can, her voice low and rough with dismay as she records the catalog of loss like a registrar of an extinguished map."
    show tamiko_sato at left:
        zoom 0.7

    tamiko_sato "We have footage. We have names. We have times. We should mount them together. This—this should not just become a press release for the other side."
    "You want to believe her energy will become something larger than sorrow, but even Tamiko's hands shake. Her exposés, once incendiary, have become elegy: careful, accurate, and unable to stop the tide."
    "Lina stands on her front step, fingers black with tape adhesive. She smiles at you — it is small and private and broken into pieces. Her storefront is empty save for the scent of spice ghosting"
    "the air, a smell that presses the memory of her mother and the stools at the counter and the nights when neighborhood kids crowded around a pot of stew."
    show lina_cortez at right:
        zoom 0.7

    lina_cortez "We tried, Mira. We tried to hold it together. We thought—"
    show mira_santos at center:
        zoom 0.7

    mira_santos "We did what we could."

    "The words feel inadequate, threadbare. You lift the waterproof notebook from your shoulder where it bobs like a wounded thing. The pages inside are swollen with salt and ink, maps and names, promises scrawled in cramped script. You flip, one-handed" "Leal, 43 Mariner's Row — tenure since '82.' 'Diaz, ground-floor pantry — offered relocation voucher, no reimbursement for moving costs."
    "You run your thumb along the jagged edges of a photograph tucked into the back pocket: your grandmother's porch, a paper plate on the table, someone laughing mid-slice. The image wobbles as if underwater."

    mira_santos "They offered vouchers. They called it 'assistance.' They renamed eviction a 'relocation opportunity.'"

    lina_cortez "They came with contracts that made the old claims fade. They put money where memory should have been."
    "Nearby, men in sleek suits walk the line between tent and truck with clipboards, reciting numbers as if counting inventory: parcels, not people. The language of the redevelopment is clinical. The heartbreak wears a municipal stamp."
    "You begin to pack methodically — a ritual to steady the sky. A pen, the brass carabiner, the coral scarf folded twice, then tucked into the notebook like a bookmark that refuses to stay. Each object is a syllable in the sentence you will carry away."
    "Your hands are quick and cold. The wind takes the edge of everything; it sounds like a sheaf of paper snapping shut."
    hide tamiko_sato
    hide lina_cortez
    hide mira_santos

    scene bg ch6_4001e7_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Your breathing; the tilt of a distant crane; the soft click of a camera stopping]
    "Tamiko approaches, camera hanging against her chest, eyes raw."
    show tamiko_sato at left:
        zoom 0.7

    tamiko_sato "We're going to make sure this isn't lost. I'm assembling a timeline. If we can't stop the promenade from being built, we can make the record. People will know."
    show mira_santos at right:
        zoom 0.7

    mira_santos "A record doesn't replace a home."

    tamiko_sato "No. But it keeps the truth in people’s hands long after the plaques are shiny."
    "You find no comfort in that. The idea that future historians might read the ledger of injustice is of cold consolation when your neighbor is losing the counter where she made rent. You close the notebook with a soft snap — the sound of a lid fitting."
    "Lina leans forward and presses your hand. Her fingers are sticky with tape and the scent of dried chiles."
    show lina_cortez at center:
        zoom 0.7

    lina_cortez "Whatever you choose to do next, don't do it alone."
    "You look at her; in her eyes, you see the neighborhood's small, stubborn insistence: the stubbornness that kept porches lit through storms."

    mira_santos "I won't. Not this time."
    "You mean it and you do not. Promise and the truth are different things."
    # [Scene: Mariner's Row — The Edge | Dusk]
    hide tamiko_sato
    hide mira_santos
    hide lina_cortez

    scene bg ch6_4001e7_6 at full_bg
    # play music "music_placeholder"  # [Music: A single dissonant violin line rises and then is cut by silence]
    # play sound "sfx_placeholder"  # [Sound: The tide clicking against supports; a far-away highway; the zip of your notebook closing]
    "You stand at the row's threshold and look back once — at the shuttered storefronts, at Lina's sign folded like a small white flag, at Tamiko's recorder catching the last of the day's good intentions. Then"
    "you look forward, where the promenade gleams and the plinth stands like a monument to decisions made without a map."
    "Elias is already gone from view; whether he walks toward Cassian's office or out into whatever life he will now attempt to build is a detail that feels both intolerable and settled. There is no dramatic"
    "crash, no last-minute speech to change the city's mind. There is only the slow, bureaucratic machinery that has already eaten weeks and promises and a love that used to find ways to rest alongside work."
    "You slip the coral scarf over your coat one last time, feeling the worn fibers like a small, stubborn relic. Your notebook, brittle at the edges, slides into your bag. You put your hand on the brass carabiner, the metal cold with sea and memory."
    show mira_santos at left:
        zoom 0.7

    mira_santos "This place gave me everything it could. I have to carry it differently now."
    "You take a step away. The world feels both enormous and compressed to the weight of your bag. Anger flares — bright, hot, then careful; grief settles deep like mud. The arousal that has wrapped around"
    "your chest all day erupts once more: a tidal pain that washes through every sinew. It is very loud inside you and there is nowhere for it to go."
    hide mira_santos

    scene bg ch6_4001e7_7 at full_bg
    # play music "music_placeholder"  # [Music: The full arrangement contracts into a single piano tremor that rings and then stops]
    # play sound "sfx_placeholder"  # [Sound: The zipper of your bag; the wind; the soft, distant clink of Cassian's glass against a podium]
    "You do not look back again."
    "You leave Mariner's Row with the weight of the notebook and the coral scarf and a clarity that is heavy and hollow: actions have consequences that glass plinths cannot reflect. The city tastes like iron."

    scene bg ch6_4001e7_8 at full_bg
    # play music "music_placeholder"  # [Music: Halted; a single, unresolved piano chord lingers and then dies]

    scene bg ch6_4001e7_9 at full_bg
    "THE END"
    # [GAME END]
    return
