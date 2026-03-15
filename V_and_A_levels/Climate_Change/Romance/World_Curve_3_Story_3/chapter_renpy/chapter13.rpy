label chapter13:

    # [Scene: Confidential Inquiry Room | Morning — Weeks Later]

    scene bg ch13_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Muffled footsteps in a distant corridor; the low buzz of fluorescent lights; the distant, indifferent slap of rain against pavement.]
    # play music "music_placeholder"  # [Music: Tense, high-register strings — a tight, nervous motif that never resolves]
    "You remember handing the packet across the threshold: your notes, the timestamped emails, the copies of the Consortium bids with margins scrawled in someone else’s ink. It felt like an offering at an altar — private,"
    "solemn, urgent. The inquiry took it with polite gloves and an index finger tapping an inscrutable line of procedure."
    "They did not promise you spectacle. They promised sealing, process, and confidentiality. They promised to weigh evidence in rooms you could not enter."
    "You leave the room with your shoulders intact and something much smaller taken — momentum. The city outside is the same as it ever was in its simplest machinery: wind, salt, people trying to get through the day while systems chew on what you offered and spit out technical phrases."
    # [Scene: Montage — Weeks of Waiting | Various Times]

    scene bg ch13_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The quiet click of keyboards; the metallic ring of a courthouse bell; distant construction rumble.]
    # play music "music_placeholder"  # [Music: A restless ostinato; tension building through percussion]
    "You watch the cogs turn. They turn precisely, slowly, inevitably. Each meeting births a new committee with a new mandate and a new timescale that expands like a tide pooling into a marsh. Press conferences yield"
    "favorable phrasing — 'inclusive,' 'community consultations,' 'further study' — words that sound like lifelines but feel like gauze over a wound."

    "Occasionally, a headline blinks across your phone" "INQUIRY CONTINUES — NO ACTION TODAY."
    # [Scene: Mayor's Office (Briefed) | Afternoon]

    scene bg ch13_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft city hum through the glass; the faint ruffle of papers]
    # play music "music_placeholder"  # [Music: Low, resigned piano chords]
    show mayor_lila_chen at left:
        zoom 0.7

    mayor_lila_chen "We are trying to balance urgent infrastructure with equity. The inquiry's findings will inform amendments to the plan."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Equity doesn't live in amendments, Mayor. It lives in the city now — in people's homes."

    mayor_lila_chen "I know how it looks. I am listening. But governance requires proof we can defend in court and in markets. We cannot act on panic."

    maya_reyes "They're starting construction on the southern stretch today. On the blocks you promised to protect politically, money moves, violence doesn't look like violence when it is scheduled."

    mayor_lila_chen "Show me where. I'll follow up."
    "Her face is practiced neutrality; the brooch gleams like a moral cue. There is a steadiness there — decisive only in the way of someone who must appear unshaken. You watch her fingers fold the papers and think of how many folds it takes to bury a name."
    # [Scene: Tideward Promenade — Evening]
    hide mayor_lila_chen
    hide maya_reyes

    scene bg ch13_3be532_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft slap of tarpaulins, a child's distant laugh, and beneath it all the steady thrumming of hydraulic pumps somewhere down the coast.]
    # play music "music_placeholder"  # [Music: A single violin, long and aching; tempo quickens subtly]
    "Diego's messenger bag is heavy; when he slams it down, papers spill like callused leaves. Eviction notices spill into your hands one at a time. The names make a chorus of the neighborhoods you grew up in."
    show diego_ramos at left:
        zoom 0.7

    diego_ramos "These came this morning. Fifty-two notices in the old block alone. They're staggered — rollouts so no one sees them all at once."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Is there legal recourse? An injunction?"

    diego_ramos "You were doing that. We thought the inquiry would stop this. We thought—"

    maya_reyes "We thought so too."
    "He looks at you like a man weighing whether to throw his bag into the sea. His impatience is a physical thing; his hands tremble. The messenger bag's strap carves a shallow line into his shoulder."

    menu:
        "Read the notices quietly":
            "You unfold the first sheet with a surgeon's steadiness, scanning names and addresses as if the words should yield a loophole. Your stomach turns into a small cold stone."
        "Show the crowd — make this public now":
            "You lift the notices, ready to make them visible, to turn the staggered erasures into a single, undeniable picture. Someone in the crowd gasps; phones raise like a court of witnesses."

    # --- merge ---
    "The scene continues as people react and plans shift."
    # [Scene: Emil's Workshop — Night]
    hide diego_ramos
    hide maya_reyes

    scene bg ch13_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant thud of machinery; the clink of metal tools; a radio broadcasting a late-night dispatch.]
    # play music "music_placeholder"  # [Music: Strings grow agitated — tremolo under heartbeat percussion]
    "Emil Kwon works with the focus of someone who believes in fixing with hands. He files a joint, mends a small frame for a floating planter, his thumb moving in a practiced rhythm. He looks up when you enter, the shadow of exhaustion in the soft green of his eyes."
    show emil_kwon at left:
        zoom 0.7

    emil_kwon "How did it go?"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "They accepted the packet. It's sealed."

    emil_kwon "Then they'll do the right thing."

    maya_reyes "They'll study it."

    emil_kwon "We have to build what we can now. If funding's eaten by lawyers, we make do locally. We do not—"
    "He returns to work, but his hands are faster now, almost frantic. He measures and cuts with a precision that becomes avoidance. His chest that was steady becomes a drum-roll of restrained panic."

    maya_reyes "You're not sleeping."

    emil_kwon "I'm fixing what I can until the city decides which lives matter on paper."

    maya_reyes "We tried a different path. I thought—"

    emil_kwon "You did what you could. So did I.' He looks up; his voice breaks. 'But watching notices come in, and hearing that the southern stretch is going live while the rest wonder if they'll be heard—it's like watching someone else rebuild your house and skip your room."
    "He stands abruptly and moves away to the window. The rain outside makes the world a smear of light and loss."

    menu:
        "Reach for his hand":
            "You close the distance and offer your palm. He looks at your hand, then at the space between, where promises used to sit, and for a beat he squeezes back. It's a small, human contract."
        "Let him work — don't demand answers":
            "You step back, folding your arms around yourself like armor. He nods once and hunches over his tools, the silence between you growing like a wall."

    # --- merge ---
    "The scene continues with Emil's whispered confession and his leaving."

    emil_kwon "Sometimes I feel... powerless."

    maya_reyes "Powerless?"

    emil_kwon "I don't know. I fix things with my hands. I can't redline a contract. I can't force a hearing to publish faster. I can't make redactions un-redact. So I work. I build. But when the notices arrive, all the maker miracles in the world don't stop the trucks."

    maya_reyes "Then don't build alone."

    emil_kwon "I don't want to be alone."
    "He leaves before you can answer. The door shuts like a final punctuation."
    # [Scene: Construction Site at Dusk — Peripheral Zone]
    hide emil_kwon
    hide maya_reyes

    scene bg ch13_3be532_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Engines, the bark of foremen's radios, and the soft whimper of a child in the distance. The wind carries the metallic tang of wet concrete.]
    # play music "music_placeholder"  # [Music: Percussion surges — snare, low brass; the motif reaches near-peak intensity]
    "You watch from the fringe as phases begin. They are clever phases: construction in high-visibility zones first, the ones that placate markets and donors. Later phases, the ones that would require land swaps or complex relocation funds, are delayed under 'budget reviews' and 'further environmental assessment.'"
    "A consortium representative — a man with a crisp suit and a tie that shows the emblem of development — steps forward with a smile that glints."

    "Consortium Rep" "This is the most pragmatic rollout. We are prioritizing based on economic impact and immediate risk."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "Immediate risk doesn't map evenly over people's lives."

    "Consortium Rep" "Risk is measured. We are accountable to stakeholders."

    maya_reyes "Stakeholders include the people whose names are on those eviction notices."

    "Consortium Rep" "Those notices are administrative. Displacement is regrettable but necessary to maintain the long-term viability of the city."
    "His voice is steady; it performs inevitability. Machines keep moving like tides that were always meant to be."
    # [Scene: Low-Lying Block — Night — Climax]
    hide maya_reyes

    scene bg ch13_3be532_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The heavy slamming of a truck door; cries muffled by the wind; a distant siren that wavers in and out of earshot.]
    # play music "music_placeholder"  # [Music: Full orchestral surge — brass, strings, percussion — a crashing, overwhelmed swell of sound. The melody is frantic, unrelenting.]
    "You stand in the middle of it. The notices in your hand feel absurdly thin; each one is a future folded into a paragraph. Your chest is a drum of too-quick beats. For a sliver of"
    "time, the world does what your worst memory always warned it would: it displaces, quietly, administratively, under the auspices of 'process.'"
    "A woman you remember from childhood — Mrs. Alvarez, who once pressed loaves into your small hands after a storm — stands in the doorway of her house. The paper trembles in her fingers. Her eyes"
    "find you immediately and the world compresses into a single, terrible transparency: recognition, betrayal, bewilderment."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "I—"

    "Mrs. Alvarez" "Do you know why?"

    maya_reyes "I handed evidence to the inquiry. I tried to make the case where it mattered."

    "Mrs. Alvarez" "And that helps how much?"

    maya_reyes "It was confidential—"

    "Mrs. Alvarez" "Confidential kept them safe from the cameras. It did not keep us from the trucks."
    "The admission is a kind of violence that is not loud but is final. Machines keep their rhythm; men with clipboards move like functionaries in a slower, efficient apocalypse."
    "Diego Ramos arrives at your elbow, his face flattened by rage and grief. He drops the rest of the eviction notices on the pavement like a confession."
    show diego_ramos at right:
        zoom 0.7

    diego_ramos "This is what inaction looks like, Maya. This is the slow work of displacement. You saved documents and they saved their interests. Meanwhile, people are losing homes."

    maya_reyes "We tried a systemic path. I thought process would protect them. I thought—"

    diego_ramos "You thought correctly about the system. The system takes time. It takes, and while it takes, it takes more."
    "Emil arrives after, shoulders hunched, hands raw from work. He watches the truck and the woman and the small collapse of normal life. He looks at you as if mapping the distance that has been growing like a hairline crack."
    show emil_kwon at center:
        zoom 0.7

    emil_kwon "I felt powerless, Maya. But this — this is a cruelty I can see. I can't un-see it."
    "You want to argue: the inquiries, the sealed things, the protections you tried to set into motion. You want to name the complexity. But in their faces — Mrs. Alvarez, Diego, Emil — complexity feels like"
    "a word to soothe a bruise. The machines continue, purposefully neutral, hammering in stakes where palms once grew food."
    hide maya_reyes
    hide diego_ramos
    hide emil_kwon

    scene bg ch13_3be532_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slap of rain, the metallic clink of tools, a child's sob caught and then swallowed]
    # play music "music_placeholder"  # [Music: The orchestration tightens into an apex — all strings and brass and percussion converging into a single, unbearable chord. The rhythm is heart-pounding, relentless.]
    "You think of the rooftop seedlings — small, insistently alive — and of Asha's tired smile when she promised 'do no harm.' You think of the tiny brass pendant at your collarbone, the tide line engraved on its surface. The pendant is cold and heavy, a counterweight."
    "You realize the truth with a clarity so sharp it stings: secrecy preserved some lives from sudden spectacle, but secrecy allowed the slow machinery to burrow in and erase others with the patient inevitability of paperwork. Your choice—what you thought was a shield—became a wall between process and people."
    "Emil steps closer, the rain running down his face like tears he hasn't let himself have yet."
    show emil_kwon at left:
        zoom 0.7

    emil_kwon "What now?"
    "You stand in the rain, surrounded by the mechanical hymn of displacement, and understand that there is no single answer that will feel like salvation."
    # play music "music_placeholder"  # [Music: Cuts abruptly to a single low sustained note; silence presses]
    # [Scene: Quiet Aftermath — The Street, Later That Night]
    hide emil_kwon

    scene bg ch13_3be532_9 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant machinery continuing elsewhere; the hush of after-storm streets.]
    # play music "music_placeholder"  # [Music: Sparse piano notes — slow, empty]
    show diego_ramos at left:
        zoom 0.7

    diego_ramos "We could have done the other thing. We could have held the line."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Holding would have risked arrests. It would have risked lives in a different way."

    diego_ramos "And yet—"
    "Emil’s patchwork optimism has frayed at the edges. He looks at the eviction notices in your hand and lays his palm over yours, not in comfort but in camaraderie against a tide."
    show emil_kwon at center:
        zoom 0.7

    emil_kwon "We're tired. I'm tired."

    maya_reyes "So am I."
    "You talk until your voices scrape the edges of exhaustion, until the city's mechanical breathing becomes the background of grief. Words are not enough. They do not re-sew a family's life or rewrite a redaction."
    hide diego_ramos
    show asha_karim at left:
        zoom 0.7

    asha_karim "You did what you thought would protect them. We have to live with the consequences and try to mend what we can."

    maya_reyes "Mend how? The machines moved while we were waiting."

    asha_karim "Mend in public. Tell the stories. Make it visible. It won't fix everything, but visibility changes the ledger."
    "You think of press rooms, of assemblies and petitions. You can see a future of endless advocacy punctuated by small, local victories. You can also see the slow forming of a seam — a city divided by the places that received protection and those that became memory."
    # [Scene: Final Quiet — The Old Block at Dawn]
    hide maya_reyes
    hide emil_kwon
    hide asha_karim

    scene bg ch13_3be532_10 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The whisper of water; a gull calling; the slow, mechanical echo of distant construction as if the city were sighing itself awake.]
    # play music "music_placeholder"  # [Music: Melancholic cello solo — low, sustained, with a single high, unresolved note]
    "You stand at the threshold of an incomplete answer and feel the weight of a moral calculus that cannot be balanced. You did not fail by malice; you failed by hoping process would outrun greed. You are not absolved, only human — precise, fallible, aching."
    "Emil stands beside you, a short distance away. There is a space between you like a shoreline: marked, real, liminal."
    show emil_kwon at left:
        zoom 0.7

    emil_kwon "We'll keep building. We'll keep telling what we've seen. We won't stop."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "And if it isn't enough?"

    emil_kwon "Then we'll keep trying. Even if trying looks different than we imagined."
    "His voice is not triumphant. It is a steadying echo against a long, slow hurt."
    # play music "music_placeholder"  # [Music: Cello fades; a final single piano key rings out and is held until it dies]
    "You look down at the pendant, find the tide line engraved there, and press it against your palm. The metal is not warm. It keeps its shape even as the world shifts."
    "You have a pile of regrets shaped like policy and people. You have saved things in secret and watched other things be erased in plain sight. The city rearranges itself around decisions you made and ones"
    "you did not. The romance of repair feels tarnished now — not dead, but reshaped into a companionable endurance. Love remains, but it is quieter, freighted with things you cannot untake."
    hide emil_kwon
    hide maya_reyes

    scene bg ch13_3be532_11 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The tide, patient and indifferent; the low, unending hum of a city reassembling itself.]
    # play music "music_placeholder"  # [Music: Minimal atmosphere, a lingering unresolved chord]
    "You breathe. The city continues. The inquiries go on. The redactions will be reassembled into policy language that may or may not protect the vulnerable. The Consortium will complete phases; some zones will be sealed, and other places will become memory-lots where markets once hummed."
    "There is no neat resolution — only conclusions we must learn to carry."

    scene bg ch13_3be532_12 at full_bg
    "THE END"
    # [GAME END]
    return
