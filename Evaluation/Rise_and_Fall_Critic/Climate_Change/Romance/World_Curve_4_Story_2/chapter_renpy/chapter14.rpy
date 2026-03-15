label chapter14:

    # [Scene: Harrow Hall | Late Afternoon — Days After Authorization]

    scene bg ch14_3be532_1 at full_bg
    # play music "music_placeholder"  # [Music: Quiet, minor-key strings; a slow, descending cello underpinning the room's hush]
    # play sound "sfx_placeholder"  # [Sound: Murmurs from the foyer; distant gulls from the harbor like a reminder that the sea listens]
    "You stand just off the dais, the brass compass at your wrist catching a sliver of light. The ribbon across the model embankment is gone now — cut — and the harbor outside bears the faint,"
    "neat lines of new concrete. People clap because they can clap for something finished. You authorized completion; you remember the moment: the weight of cameras, the small, decisive breath you took, the way Ivo nodded at"
    "you as if to say, We act."
    "It felt like protection then. It still does when you watch the harbor lights flare on and children press their palms to the viewscreen at the town center, curious and safe, if only for the tides that come tonight."
    "You smell tar and salt and a plastic tang of festooned balloons. Your jacket still carries the greenhouse dampness from mornings of seedlings — a different kind of smell, green and persistent. Your shoulders are a fraction less tight than they were two weeks ago."
    "Celine's smile is curated and luminous at the podium. She speaks of emergency measures and municipal responsibility; the recorder in the corner chases every syllable like a gull."
    show celine_harrow at left:
        zoom 0.7

    celine_harrow "We have acted decisively. We have protected the most vulnerable among us. This is Saltwick's moment — of stewardship and of renewal."
    "She glances in your direction. The look is precise, the one of a woman who has calculated optics and outcomes. You return the look because you can; because it matters that she sees you saw what she arranged."
    "Ivo Calder approaches, bringing the smell of diesel and wet rope with him. He drops onto a bench beside you and lets out a low breath as if the day lost something of its sharpness."
    show ivo_calder at right:
        zoom 0.7

    ivo_calder "Can't believe it, huh. Feels wrong and right all at once."
    show alys_maren at center:
        zoom 0.7

    alys_maren "Right enough that people will sleep through a high tide. Wrong enough that it never felt plain."
    "He laughs, small, tasted with something like worry. He looks at the harbor through the window, at the steady, neat line of the new wall."

    ivo_calder "You did what you thought we needed. Hell of a thing, Alys."

    alys_maren "We did. You did. Celine pushed good money into a bad year, and it showed up as rock and concrete."
    "You both fall silent, the kind of silence that lets the room contain its applause and your private tally of costs."
    # [Scene: Saltwick Harbor | Early Morning — Six Weeks Later]
    hide celine_harrow
    hide ivo_calder
    hide alys_maren

    scene bg ch14_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The harbor bell tolls; waves sigh against concrete. A low, persistent hum of conversations at the quay.]
    # [Smell: Wet canvas, hot coffee, and underneath it a chemical whiff — solvent, new asphalt.]
    "Ronan finds you before the work starts. His hands are stained; there's a nervy edge in his movements like someone woken from sleep and told the tide changed its course."
    show ronan_pike at left:
        zoom 0.7

    ronan_pike "Alys — you got a minute?"
    show alys_maren at right:
        zoom 0.7

    alys_maren "Of course. What's wrong?"
    "He hands you a battered envelope like contraband. Your name isn't on it; your heart is, just for a second."

    ronan_pike "Found it in a contractor's van. Didn't know where else to take it. Thought—"

    alys_maren "If this is nothing, it will be nothing and I will have to keep this look of startled worry for hours. If it's something, the harbor will be a different place."
    "You take the envelope. Inside, neat columns of numbers and a ledger with marginalia: names that match the council roster, line items for 'Access Privilege,' 'Donor Easement,' and accounts that route to shell companies. There are"
    "stamps that match municipal signoffs; there are dates that overlap with the days you authorized immediate completion."
    "You read until the ink blurs."
    "Your first instinct is denial — the old science reflex: check the data twice. Your second is a raw, hot betrayal that makes your hands cold."

    menu:
        "Call Ivo quietly to look with you":
            "You pull your phone and step behind a crane. His low laugh dies when he sees the pages; he fingers a circled entry and breathes out, 'So they paid for private access lanes, not protective coffers.'"
        "Walk straight to Celine's office and demand answers":
            "You leave Ronan with the papers and move toward Harrow Hall with the gait of someone who has already rehearsed confrontation. Your knuckles ache as you knock on the mayor's inner door."

    # --- merge ---
    "'You choose to call Ivo. He arrives with a cup of coffee gone cold and a face that tightens into policy and worry in the same breath.'"
    show ivo_calder at center:
        zoom 0.7

    ivo_calder "If this is real— this isn't just graft, it's a plan to privatize safety. People paid to get their docks cleared first. People paid for 'private access' while neighborhoods farther down got nothing."

    alys_maren "The words make a slow, heavy fall in your chest. You had authorized completion because you believed it would be for everyone. The ledger speaks to a different truth."
    "You both sit on the quay, pages fanned between you like evidence and tinder."

    ivo_calder "We could take it to the press. Tear it open."

    alys_maren "Or the auditors. We have to be careful. If we accuse and we're wrong, we ruin lives. If we're right and we don't do anything, we let them sell us down the tide."

    ivo_calder "You always worry about the long view, Alys. But people need the short one. Those who got left behind—"

    alys_maren "I know. I authorized completion to secure the short one. I didn't expect this."
    "He looks at you the way people look at a map where the coastline has changed since the last trip."
    # [Scene: Harrow Hall — Emergency Town Meeting | Night]
    hide ronan_pike
    hide alys_maren
    hide ivo_calder

    scene bg ch14_3be532_3 at full_bg
    # play music "music_placeholder"  # [Music: Tense piano, staccato strings creating a thin, rising anxiety]
    # play sound "sfx_placeholder"  # [Sound: Voices ripple like a coming tide; someone coughs; a child whimpers and is hushed.]
    "You sit at the front. Ronan and Maya are there; Oba Kofi leans on his cane with a gravity that makes the room quieter. Celine enters last, immaculate as always, and the room's temperature shifts."
    show celine_harrow at left:
        zoom 0.7

    celine_harrow "I understand your fears. And I welcome the inquiry. Transparency is the backbone of our recovery."
    "Her words land like stones — there is polish, but there is also a distance now you can't close. The ledger sits on the council table, a physical thing, opened so everyone can see the neat handwriting of betrayal."
    show maya_maren at right:
        zoom 0.7

    maya_maren "How could you—? We voted on repairs. We trusted you. Families got moved; rents were raised on some blocks because of 'safety zones' and not everyone was told they weren't part of the 'protected areas.'"
    "Your sister's voice cracks and turns into sound you know like a bruise. You want to reach for her hand."
    "A heated exchange begins. The mayor's defenders point to lives saved during the last storm; critics hold up the ledger as proof that safety had price tags and preferred addresses. Oba's voice, when he speaks, is slow and made of tide-knowledge."
    show oba_kofi at center:
        zoom 0.7

    oba_kofi "This town remembers how the sea takes. We put barriers in place to stop it. But when some can buy a lane and others are left to learn again, that is not protection. That is turning away our kin."
    "Celine remains composed until the council auditor, a thin woman with a stack of records, clears her throat and references transfers and side agreements linked to Celine's private counsel. Somewhere in the back, a reporter's pen scratches like a nervous insect."

    "Council Auditor" "There are transfers routed through a third-party escrow under the name 'MST Ventures.' These accounts correspond to 'priority access' clauses. The documentation suggests municipal sign-off — not necessarily in line with the public mandate."
    "You feel the air change. People whisper. Someone starts a chant — not angry exactly, more raw with betrayal."

    menu:
        "Stand and offer a factual recount of the authorization process":
            "You rise. Your voice is steadier than you feel; you lay out the timeline of approvals and why you signed off. People listen because they trust your method."
        "Remain seated and let Celine speak first":
            "You fold inward, letting her attempt to shape the narrative. The room watches her; you watch the way her composure crumbles, a fraction, like plaster giving way to moisture."

    # --- merge ---
    "'You stand. Saying nothing feels like abdicating responsibility — and you did sign that order. The room turns to your face.'"
    hide celine_harrow
    show alys_maren at left:
        zoom 0.7

    alys_maren "When I authorized completion, I was told the funds were allocated for immediate protection across sectors. The models showed that the wall would reduce overtopping and protect the low ridge. I believed that we were protecting Saltwick in every way we could, as quickly as we could."
    hide maya_maren
    show celine_harrow at right:
        zoom 0.7

    celine_harrow "And I authorized the contracts to expedite delivery. Some arrangements were made to secure private entry points for industrial vessels — to maintain economic lifelines. Those were not secret, they were fiscal decisions made under duress."
    "Her language is careful. But the ledger's ink is more stubborn than words. Someone in the room — a neighbor whose basement flooded three times last year — speaks up, voice broken."

    "Neighbor" "My name's on a petition for relocation. I was told delays were because repair crews were focusing on 'priority zones.' I had to move my mother a mile inland. Who decided we'd be pushed aside?"
    "The prosecutor arrives before night turns black. There are subpoenas; there are murmurs of conflict-of-interest; there's the sound of municipal paper being set into legal folders. The town is watching its leaders become defendants."

    celine_harrow "If there was wrongdoing, I will accept responsibility where it is mine."
    "Then, slower, she says words that will be replayed in months of analysis."

    celine_harrow "I did what I thought was necessary to save Saltwick. If my choices hurt people, I am sorry. I will step down while the inquiry proceeds."
    "The microphone records the resignation. Applause and sobs mix in a sound that is neither victory nor loss so much as punctuation on a long, ugly sentence."
    "Oba Kofi stands and places his weathered hand on the ledger like a blessing or an admonition — you cannot tell which."

    oba_kofi "We will fix what we can. But remember — when power and money meet the tide, you cannot pretend one is more powerful than the other."
    # [Scene: Harrow Hall — Aftermath | Night Turns to Dawn]
    hide oba_kofi
    hide alys_maren
    hide celine_harrow

    scene bg ch14_3be532_4 at full_bg
    # play music "music_placeholder"  # [Music: Sparse piano; the melody folds down into a single, unresolved minor chord]
    # play sound "sfx_placeholder"  # [Sound: A distant tide hitting the new wall, not breaking it but whispering against the concrete]
    "There are resignations. There are arrests. The municipal docket becomes a parade of hearings. Celine's counsel negotiates admission to charges in return for testimony; a few contractors are indicted. The town's legal victory is loud and"
    "legal — indictments, prosecutions, oversight committees. The ledger becomes Exhibit A. Cameras come and go. Some names are blacked out in the press; others are not."
    "But the moral cost scours the town clean in ways law cannot mend. Trust has been spent; relationships that were sturdy as harbor timbers creak. Maya stops sleeping well. Ronan speaks with less exuberance. Ivo avoids"
    "council meetings for a week, busy with fieldwork and the taciturn labor of repairing nets. He tells you, once, in the greenhouse, that he admires your tenacity and resents the optics that wrapped you into compromise."
    show ivo_calder at left:
        zoom 0.7

    ivo_calder "We saved lives. We also let something ugly happen, and some of that came across with what we thought was good."
    show alys_maren at right:
        zoom 0.7

    alys_maren "The ledger showed an ugliness that wasn't only other people's doing. There is a sting — not pure guilt; more a complicated graph of choices. You had believed the strong thing to do was authorization; you now see that power can be used even by those who mean to protect."
    "You visit Oba at the harbor before the hearing closes. He is stooped but steady; the cane is a carved fish that rides the whorls like a ship."
    show oba_kofi at center:
        zoom 0.7

    oba_kofi "You did what you thought would hold our people. The law will do its work. We will rebuild what broke between us. Do not let this ledger be the only story we tell."

    alys_maren "What story should we tell, then? The one where we were saved and corrupted, or the one where we learned?"
    "Oba pauses and looks past you toward the washed, newly planted seagrass trays. A soft wind moves the young shoots."

    oba_kofi "Both. The truth is always a house with many rooms. We have to live in them all and choose how to repair each door."
    # [Scene: Town Harbor — Several Months Later]
    hide ivo_calder
    hide alys_maren
    hide oba_kofi

    scene bg ch14_3be532_5 at full_bg
    # play music "music_placeholder"  # [Music: Low, sustained strings with a single solitary flute suggesting fragile hope under weight]
    # play sound "sfx_placeholder"  # [Sound: The town's bell rings a careful toll. Children play farther from the waterline; the air holds something like cautious religiosity.]
    "The legal cases wind through courts. Celine's fall is complete in form: resignation, indictment, prosecution. The municipal council is reconstituted with stricter oversight and community representatives in seats that were once empty. The work you advocated"
    "for continues — seagrass plots are larger; living breakwaters are sketched and funded under new, watchful committees."
    "The town has its moral victory: corrupt deals exposed, some restitution arranged, a new charter drafted that binds future emergency spending to transparent audits. It is a victory that tastes of iron — necessary, corrective, and costly."
    "You stand on the harbor bluff with Ivo and Maya and Oba. The three of them look at you not with the same uniform affection as before but with something more brittle and honest."
    show maya_maren at left:
        zoom 0.7

    maya_maren "We lost trust. But we also regained tools to guard against losing it again. That feels... like work."
    "Ivo Calder's hand finds yours for a moment. There is no melodramatic reconciliation here — only the small, steady pressure of someone who knows you and knows the town."
    show ivo_calder at right:
        zoom 0.7

    ivo_calder "We keep building. We keep watching. We keep planting. We'll be messy doing it."
    show alys_maren at center:
        zoom 0.7

    alys_maren "The ledger is closed and catalogued, but its shadow follows. The victory was true in the sense of exposure and change. But true has a price. Friends were fractured. Careers ruined. Homes disrupted. The town will be safer in law, but for some the heartache remains raw."
    hide maya_maren
    show oba_kofi at left:
        zoom 0.7

    oba_kofi "We will learn to measure justice like we measure tides, Alys — carefully, and with humility."
    "You nod. Humility is a hard and necessary thing. It will have to be taught, practiced, and sometimes paid for."
    hide ivo_calder
    hide alys_maren
    hide oba_kofi

    scene bg ch14_3be532_6 at full_bg
    # play music "music_placeholder"  # [Music: The strings resolve downward, not triumphant but settled; a low chord held like a vow]

    "You close your field notebook and write, in steady, small script" "Truth — Repair — Watch.' The promise is smaller than 'Seed — Measure — Teach — Protect,"
    "You turn the page."
    # play music "music_placeholder"  # [Music: Fade Out]

    scene bg ch14_3be532_7 at full_bg

    scene bg ch14_3be532_8 at full_bg
    "THE END"
    # [GAME END]
    return
