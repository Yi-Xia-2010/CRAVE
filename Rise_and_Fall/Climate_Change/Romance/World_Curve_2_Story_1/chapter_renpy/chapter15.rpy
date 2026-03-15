label chapter15:

    # [Scene: Newsroom | Midday]

    scene bg ch13_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft click of keyboards, low murmur of editors, the tinny hiss from a kettle off-screen]
    # play music "music_placeholder"  # [Music: A low, anxious string motif—minor, restrained]
    "You step over a coil of phone cords and prop your shoulder against the doorframe, the folder heavy and warm in your palm. The city light bleaches the paper edges; the newsroom smells of strong coffee"
    "and printer toner, a smell that makes you feel both small and suddenly very visible. For a second your hand tightens without you noticing—an old reflex of holding on when the world tilts."

    "Journalist" "You're sure about this? Once it runs, there's no pulling it back."
    "You meet their eyes. They are sharp and kind in that weary way journalists get when they know the cost of a truth. You think of Chapter 5—of a stylus hovering, a clause that could be"
    "rewritten if you stayed inside the room—and of the cold clarity that made you choose to leak instead. That memory is a string you can still feel tugging at your sternum."
    show maya_rios at left:
        zoom 0.7

    maya_rios "I am. The town deserves to know what they'd be signing away."

    "Journalist" "What do you expect will happen? Lawsuits? PR spin? They'll say you're sabotaging the only plan that can save people."
    "You shrug, the motion small. 'They will say that. They will do worse. But if the public doesn't see the easement language, the extent of land grabs and the buried dredging plans—if they don't see the"
    "memos that discuss trade-offs as 'acceptable sacrifices'—then the conversation will be one-sided. I can't be part of that.'"

    "Journalist" "Names, dates, internal memos—this is damning. We'll corroborate. We'll protect you where we can, but legally it's messy."
    "You let your fingers trace the dent in the folder where a paperclip has been removed. You feel exposed and oddly relieved, as if the act of handing it over is both wound and salve."

    menu:
        "Wait and watch the editor file the story with me":
            "You sit under the humming fluorescents while the journalist uploads, watching the cursor spin. Your heart bangs raw against your ribs—anticipation and guilt braided into one. You overhear the editor ask for confirmation, your name flutters and then is left out of the byline; the article goes live and the world tilts again."
        "Leave immediately—get back to the town before the storm of headlines hits":
            "You push away, the folder light as breath now gone. You run toward the exit, salt air already a mental presence, imagining faces on Harborfront Lane scrolling phones and folding like wet paper. You tell yourself you'll be there when they need someone to explain the data, but the distance feels huge."

    # --- merge ---
    "Continue to the next scene."
    hide maya_rios

    scene bg ch13_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant chime as the story is posted; a dozen message pings bloom like small alarms]
    # play music "music_placeholder"  # [Music: The strings sharpen; a low electronic pulse underlines the headlines]
    "Within hours the first wave hits. Your phone erupts—calls, texts, a flood of anger and gratitude. The article stitches language that was hidden in boardroom memos into sentences the town can read: easements that would shift"
    "shoreline ownership, pilot dredging zones mapped across marsh tributaries, memos phrased to treat certain wetland patches as 'sacrifice areas' in the name of 'greater resilience.' The journalist's piece punctures Aquila's polished claims with evidence that feels"
    "irrefutable."
    # [Scene: Aquila Developments — Private Conference Room | Afternoon]

    scene bg ch13_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant muffled din of their PR team; a phone tapped hard against a palm]
    # play music "music_placeholder"  # [Music: A cold, single piano note that hangs like a question]
    show cass_adler at left:
        zoom 0.7

    cass_adler "We can spin this. Legal will draft statements. We'll show the 'big picture' benefits. This is sabotage. Who gave them those files?"
    "Their eyes find you before their words do—icy, precise, but with a flash of something less easily named: surprise, a fissure of personal betrayal. For a single, suspended heartbeat they are not corporate clarity but a person with wind-raw cheeks and a jaw that clenches."
    show maya_rios at right:
        zoom 0.7

    maya_rios "I did."
    "Cass Adler stares, then exhales in a way that makes papers flutter on the table. The room tilts toward accusation."

    cass_adler "Why, Maya? We—I've been trying to—"
    "You interrupt because the reasons are many and too big to fit into the air between you: your grandmother's stories of the marsh, the smell of salt when you were a child, the spreadsheet where species"
    "counts fall. You think of the model that simplified human lives into color-coded zones, of memos that treated families like negotiable coordinates."

    maya_rios "Because people deserve to decide with the whole truth. Because 'resilience' can't be a euphemism for erasure."

    cass_adler "And you think this forces transparency? Or just chaos? Do you know what this will do to our negotiations? To the funding? To people's sense of security?"
    "You feel Eli's name at the back of your mouth—his practical fear of losing livelihoods, his steadiness—and how that steadiness helped you sign and then leak, somehow both acts braided. Cass looks at you then with a complex unreadability that crosses the professional and the personal."
    # [Scene: Harborfront Lane | Evening — The Night the Headlines Reach Home]
    hide cass_adler
    hide maya_rios

    scene bg ch13_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A chorus of voices—outrage, fear, weary resignation. A distant generator hums. Somewhere, a child cries once.]
    # play music "music_placeholder"  # [Music: Slow cello, low and mournful]
    "The town is a mosaic of reactions. At the fishmonger’s stall, Marta—who has mended nets for thirty years—says nothing but folds her hands, jaw tight. A handful of younger residents chant outside Aquila's temporary office; their"
    "energy is sharp and immediate. Others hold meetings in kitchen light—small kitchens, big decisions—while an older council member reads the headlines aloud like an indictment."
    "Eli Navarro finds you at the edge of the crowd; his hazel eyes are ringed red, not from tears but from the strain of sleepless nights and the rawness of too many decisions."
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "They called us reckless. The paper said—someone in the mayor's office told them—"
    show maya_rios at right:
        zoom 0.7

    maya_rios "They'll say that. They'll try to make this about panic, about us scaring off investors."

    eli_navarro "Do you think… this will help? Or will it just make it harder for the people who need help the most?"
    "You look at the boats, at rigs throwing neon like false constellations on the water, and feel the unanswerable weight. The leak has opened a wound and a mouth both: there is air now, but also vulnerability."

    maya_rios "It helps the truth come out. It forces negotiations into light. But it makes leverage dangerous—there will be retaliation."

    eli_navarro "Retaliation. That's one word for cease-and-desist letters, suits that threaten the town with bankruptcy, PR campaigns that paint us as obstructionists. Another is fear."

    maya_rios "I know. I—"

    menu:
        "Answer the woman shouting that the leak ruined their chance":
            "You turn to her and try to explain the technicalities—easements, dredging zones, what the memos said—but words feel like pebbles. She shakes her head, grief raw. 'We needed jobs, Maya,' she says. Your explanation is not consolation."
        "Pull Eli into the alley to strategize quietly":
            "You pull Eli aside where the air smells of wet rope and frying fish. You both whisper possibilities—federal review, legal fundraisers, community forums. You plan like surgeons, each plan cut to minimize harm; each plan also admits it may fail."

    # --- merge ---
    "Continue to the montage sequence that follows."
    hide eli_navarro
    hide maya_rios

    scene bg ch13_601bcb_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Overlay of distant megaphone, the scratch of a lawyer's pen, the soft cry of an injured gull]
    # play music "music_placeholder"  # [Music: Percussive, anxious strings building then receding]
    "Aquila's counterattack is swift and clinical. Cease-and-desist letters land in town hall mailboxes like small black birds—sharp, formal, threatening. Their PR team spins a narrative of 'short-sighted sabotage' and 'jeopardized funding.' Lawyers begin to talk about"
    "defamation, theft of proprietary materials. The firm buys ad space that shows smiling families behind conceptual renderings of elevated boardwalks and clean, engineered marsh edges."
    "At the same time, the story draws unexpected light. Grants geared toward community-led resilience sprout interest groups overnight; a small environmental fund offers emergency legal aid; a university coalition pledges independent testing on the dredging's ecological"
    "impact. A federal office announces a review—slow-moving and bureaucratic, but still a formal acknowledgment that the plan must be examined."
    "You find yourself in a strange landscape of wins and costs. The town receives donations and expert volunteers, and yet the mail brings threats and invoices. Friends who once gathered on your porch now keep their"
    "distance when suits come to measure properties. Someone burns a sign in the square one night; someone else brings flowers the next."
    # [Scene: Harborfront Lane — Weeks Later | Overcast Afternoon]

    scene bg ch13_601bcb_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low thrum of machines, the whisk of spartina in wind, a man at the far end of the lane muttering prayers]
    # play music "music_placeholder"  # [Music: A single piano line, slow and grieving]
    "You walk the length of the affected stretch alone, boots sinking into mud, salt on your lips. The evidence of compromise is physical now: a narrow swath cordoned for test work, a surveyor's stake blinking in"
    "the marsh like a synthetic reed. The federal review will decide, eventually, but in the meantime the ground itself remembers each cut and fill, each shifted oyster rack. The marsh pays in silence."
    "Eli Navarro waits at the corner, hands in pockets, eyes on the water. When you cross to him there is no theatrical reconciliation—only a tight, necessary warmth like two hands pressed against a cold day."
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "Some people took the offers. They needed to—mortgages, medical bills. It's hard to blame them."
    show maya_rios at right:
        zoom 0.7

    maya_rios "I know."

    eli_navarro "And there are others who feel betrayed by what the leak did. They say you made it worse when Aquila tightened its teeth."
    "You swallow. 'They are right in part. I made a choice that cost people more exposure…and maybe more pain.'"
    "There is a long silence between you where the gulls wheel and a distant diesel coughs. Neither of you reach to fix the interstice; instead you stand with it, as if shared silence could be a kind of truce."

    eli_navarro "Do you regret it?"
    "You think of Marta's tight hands, of children learning marsh plants in Rosa's classroom, of the memos that named places as 'sacrifice.' You think of Cass's eyes—betrayal and confusion and something like grief. You think of your grandmother on a porch that no longer exists."

    maya_rios "I regret what the town had to pay. I don't regret pulling the curtain back. Some truths can't be bargained with."

    eli_navarro "Then we'll keep doing what we can. Together if we can. Apart if we can't. But I—' He stops, because the word that would bind or break is heavy. 'I won't let them take the marsh without someone making a noise."

    maya_rios "Neither will I."
    hide eli_navarro
    hide maya_rios

    scene bg ch13_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: The cello holds a note—mournful, but not entirely without warmth]
    "Time becomes a ledger of small acts: a fundraising bake sale that pays a lawyer's retainer, a volunteer transplanting spartina in the gray damp, an excited but cautious press conference that wins a short-term injunction. The"
    "federal review remains a bureaucratic tide that moves too slowly to stop the immediate mechanical tests. The dredge cuts where a family once harvested clams; the water turns clouded for weeks. Some species recover; others do"
    "not. The town's history is altered in ways both seen and folded into memory."
    "Cass Adler leaves a message once—cold, composed, then nothing. Once you see them in person at a hearing; they speak with the clarity of someone defending a system they believe can scale solutions. You hold your"
    "line; for a while the two of you trade technical rebuttals and personal barbs. Over time Cass's calls become less frequent. The personal thread between you and them snaps in ways neither of you tended, too"
    "frayed to mend by apologies."
    "At night you sit with your notebook and write—tide observations, a list of species' counts, the minutes of meetings. You record names of those who accepted offers and those who fought. Granular truth becomes a map"
    "for what may come after. You are tired. You are grateful. You are ashamed. The mixture is strange and steady as a moonrise."
    # [Scene: Harborfront Lane | Dusk — Final Image]

    scene bg ch13_601bcb_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A slow, distant bell; the soft slap of waves against pilings; the rustle of a protest sign being folded]
    # play music "music_placeholder"  # [Music: A single, descending string phrase that resolves into silence]
    "You stand at the water's edge, the day's cold pressing through your jacket. The town is smaller tonight—somewhere between those who left and those who stayed, between the reclaimed ground and the ground that remains wild."
    "Your pendant is cool at your sternum; your notebook has a new crease. You think about promises—spoken, silent, broken—and the kind of love that looks like staying when everything tastes of salt and bargaining."
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "We can't fix everything."
    show maya_rios at right:
        zoom 0.7

    maya_rios "No. But we'll keep trying."
    "He nods, and you both turn your faces to the harbor where small lights bob like unsteady stars. There is sorrow in what you see, and there is resolve. The story of this season closes not"
    "with a single hero or a tidy reconciliation, but with the steadiness of people continuing—repairing, litigating, teaching, grieving—because to leave would be to surrender the place that taught you how to care."
    hide eli_navarro
    hide maya_rios

    scene bg ch13_601bcb_9 at full_bg
    # play music "music_placeholder"  # [Music: The strings fade into a single sustained tone. Silence follows.]

    scene bg ch13_601bcb_10 at full_bg
    "THE END"
    # [GAME END]
    return
