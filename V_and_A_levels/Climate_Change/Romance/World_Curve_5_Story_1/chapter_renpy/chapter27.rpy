label chapter27:

    # [Scene: Council Chambers | Midday]

    scene bg ch13_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft murmur of voices; rain steady against high windows]
    # play music "music_placeholder"  # [Music: Quiet, hopeful strings—gentle pulsing]
    "You step into the chamber with TideLab's packet under your arm and the echo of the boardwalk behind your ribs. The choice you made on the pier—turn the confrontation into disciplined legal pressure—arrived here like measured"
    "breath. It has sharpened everything that follows: the arguments, the deadlines, the way people fold their hands when they try not to shake."
    "You can feel Tamsin's municipal leverage like a practical weight in the room: the permits that bend, the council votes that could be held, the moratorium she has quietly sketched into an ordinance nobody else thought"
    "to propose. Across from you, Corinne Voss sits composed, AR glasses reflecting the same tide maps you carry. Her expression is unreadable but less cold than it was on the boardwalk; the public eye and legal"
    "scrutiny have a way of changing even certainty."

    scene bg ch13_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Pages turning; a chair creaks as Luka Maren leans forward]
    show tamsin_cho at left:
        zoom 0.7

    tamsin_cho "Mayor's office will announce a conditional moratorium if Voss signs an agreement today. It legally freezes certain construction permits for ninety days—enough for oversight, enough for public review. In exchange, Voss must commit funding for marsh restoration and community resilience grants."
    show corinne_voss at right:
        zoom 0.7

    corinne_voss "We are prepared to re-evaluate the high-impact sections of the design. We will fund a community-led pilot for marsh and oyster restoration. We will not indefinitely delay critical protective measures—those are non-negotiable—but we will phase construction and provide relocation assistance where engineering shows imminent risk."
    "You hold the room with your gaze and find the place where policy and people cross. It feels like stepping over a seam—one careful foot in law, the other in lives."

    "You (Amaya Reyes)" "Phased relocation must include cultural safeguards. Records, oral histories—Abuela Rosa's archive, community artifacts—must be preserved and integrated into new housing plans. Compensation can't be a number; it has to be a way to keep work and memory."

    corinne_voss "We will underwrite a cultural preservation fund. We will include budget lines for documentation and local employment during the transition."
    show luka_maren at center:
        zoom 0.7

    luka_maren "And data transparency. Voss engineers come to town briefings. We install community sensors—open-source feeds. No black boxes."

    corinne_voss "Open data where feasible. Security protocols remain for proprietary elements, but we won't hide environmental monitoring."
    "Jules: (cutting in) 'Public footage—no drone blackouts this time.'"
    "A few heads incline; a small chorus of relief moves through the room. The terms are not everything you'd hoped for, but they're scaffolding—something to build on instead of starting from rubble."

    menu:
        "Ask Tamsin to push for a longer moratorium":
            "Tamsin's jaw tightens; she sketches a calendar with a thicker block and explains the political cost: the mayor needs a show of broad support. We may get an extension if we can show immediate restoration progress."
        "Insist on community oversight panels now":
            "Tamsin smiles tiredly and agrees—proposed oversight panels are added to the agreement page; it slows the sign-off by a week, but gives residents seats at the table."

    # --- merge ---
    "Discussion continues with Tamsin emphasizing leverage and the need to use it wisely."
    "Tamsin: [after a turn of the paper] 'With your legal filings and the town's motion, we have leverage. But leverage wears out. We use it now and then hold the line—monitor, document, force accountability.'"
    "You watch Corinne read the same sentence you've been rehearsing for months: concessions framed as pragmatic engineering. The relief that eases your shoulders is warm and sharp at once."

    corinne_voss "We will scale back the most intrusive breakwaters. We'll fund marsh restoration, a local hiring program for construction and restoration, and a relocation fund for marginal blocks. The agreement will be binding. It will be public."
    "Mateo: (voice low, held) 'Phased is better than bulldozed overnight.'"
    "You feel something give in your chest—an ache and a small, fierce light. This is not victory in the theatrical sense; it is legal scaffolding that preserves roofs and jobs and a chance for habitats to"
    "be repaired. It is the kind of victory you can build a life on, and that fact leaves you both proud and hollow."
    hide tamsin_cho
    hide corinne_voss
    hide luka_maren

    scene bg ch13_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A pen scratching; Luka Maren's breath close to your ear]
    show luka_maren at left:
        zoom 0.7

    luka_maren "I'll run the sensor grid. I'll go to their meetings. I'll radio what I see."

    "You want to tell him not to go into their rooms alone, not to trade safety for oversight, but the sentence that forms in your throat is softer" "Thank you."
    show corinne_voss at right:
        zoom 0.7

    corinne_voss "We will sign the agreement under municipal oversight. We will publish the core environmental models, fund the restoration, and commit to relocation assistance where engineering deems necessary."
    show tamsin_cho at center:
        zoom 0.7

    tamsin_cho "Council vote now, contingent on immediate signature and public posting."
    "A slow exhale moves the room. You watch hands raise, papers are signed, the mayor's gavel is tapped with ceremonial yet real authority."
    # play music "music_placeholder"  # [Music: The strings swell modestly—warmth without triumphal blare]
    hide luka_maren
    hide corinne_voss
    hide tamsin_cho

    scene bg ch13_601bcb_4 at full_bg
    "You let yourself feel the tide change. It is not a turning of the sea, but it is enough: homes kept, marshes funded, work preserved for many. The cost is real—several blocks will relocate, decades of street life will be folded into new designs—but what remains is more than rubble."
    # [Scene: TideLab | Evening]

    scene bg ch13_601bcb_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Laughter undercut by the clink of cups; rain slows to a hush outside]
    # play music "music_placeholder"  # [Music: Low piano—steady, comforting]
    "You come back to TideLab with the signed agreement folded into your pocket like a talisman. The shed smells of salt and fermenting soil. Jules is projecting a feed of community sensors—map pins blinking where oyster"
    "beds will be planted, reed lines to be restored. People cluster around benches laden with takeout and maps."
    "Abuela Rosa sits near the window, shawl folded like a promise. Her hands are small and steady; she reaches for yours without looking up."
    show abuela_rosa at left:
        zoom 0.7

    abuela_rosa "You did what your grandmother would have done—kept more than you lost. We carry the pieces forward."
    "You lean into the warmth of her hand. The words you want—how hollow proud feels, how your chest is taut with the memory of faces at the boardwalk—come out as a single breath."

    "You (Amaya Reyes)" "We kept the heart of the town, Abuela. But some of us will leave their houses. Some mornings I'll still walk the boardwalk and not see the same doors."

    abuela_rosa "We are a line of people who know how to sew new seams. We will stitch. Some threads will be new. Some threads will be carried with us."
    "Mateo: (arranging a small stack of paperwork) 'Compensation is fair, and the jobs package means I can hire more deckhands for restoration crews. It hurts, but it's not ruin.'"
    show luka_maren at right:
        zoom 0.7

    luka_maren "I told them I'd attend their technical meetings, but I told them TideLab would be in every room. I'll make sure our sensors speak louder than corporate slides."

    "You" "Come home sometimes."

    luka_maren "I always will."
    "The small, shared vows and practical promises hold like a net. The work ahead is enormous—restoration plantings, relocation logistics, employment programs—but the feeling in the room is of motion in the right direction. You are not"
    "alone carrying the ledger of the town. Documents will be filed, oversight panels will meet, and simple, stubborn labor will restore marsh edges and oyster reefs."

    menu:
        "Offer to lead the community oversight panel":
            "Mateo and Jules clap quietly; Tamsin already smiles at the idea—your leadership guarantees continuity between legal text and lived experience."
        "Stay focused on fieldwork—let someone else chair the panels":
            "You feel relief at the thought of rolling up your sleeves again. Luka reaches across and squeezes your hand with understanding: your presence in the field is indispensable."

    # --- merge ---
    "The team moves forward with planting plans and panel scheduling; practical work and oversight proceed in tandem."
    "Jules: (grinning) 'First planting is scheduled at low tide. Bring boots.'"
    "Your bracelet—the wildflower seeds braided into leather—catches the lamplight. For a moment you press the beads between thumb and finger. The seeds are symbolic, small and stubborn: reminders that restoration begins with precise, patient care."
    hide abuela_rosa
    hide luka_maren

    scene bg ch13_601bcb_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The gentle slap of soil; voices trading practical instructions; a child laughing in the background]
    # play music "music_placeholder"  # [Music: Mid-tempo orchestral warmth—rising and steady]
    "Time compresses into workdays. Weeks become a rhythm: sensor deployments, community briefings, council oversight meetings where TideLab's data is read aloud and cross-examined by engineers and residents. Corinne Voss attends, as promised, and sometimes her answers"
    "are clipped; other times she surprises you with a practical empathy—an engineer learning to listen."
    "One evening, as the restoration crew finishes a long day, Abuela Rosa presses a small envelope into your hand."
    show abuela_rosa at left:
        zoom 0.7

    abuela_rosa "We made copies of stories. Take one to the new homes. Keep them close."
    "You open the envelope later and find photocopies of old photographs, hand-written snippets of shoreline names, recipes, and the syllables of lullabies sung long before any wall was proposed. The humble bundle feels like a bridge."
    "You stand at the restored reed line weeks later and watch a pair of oystercatchers return, bold as ever. The water looks cleaner at the mouth where the new oyster beds filter it. The work is slow. The victory is measured rather than spectacular, and it is richer for that."
    show mateo_reyes at right:
        zoom 0.7

    mateo_reyes "You did good, hermana. You kept us from being reduced to a statistic."
    "You let the praise fill you and then set it down beside the ache. It is possible to hold both."
    show luka_maren at center:
        zoom 0.7

    luka_maren "We built something that won't disappear when a CEO changes their mind. We made structures that can be improved with hands from this town. That's enough, isn't it?"
    "You look at the line of volunteers—faces muddy, proud, tired—and realize that 'enough' feels like a doorway rather than an end. There will be grief days when the houses are packed and moved, and there will"
    "be mornings when Abuela Rosa's shawl is folded into a new closet. There will also be oyster beds that sing the bay back into health."
    # play music "music_placeholder"  # [Music: Quietly resolves—warm, settling major chord]
    hide abuela_rosa
    hide mateo_reyes
    hide luka_maren

    scene bg ch13_601bcb_7 at full_bg
    "You feel proud: of the law's blunt utility, of Tamsin's municipal courage, of Luka Maren's willingness to straddle worlds. You feel hollow: at the sight of boxes labeled with names, at the knowledge that some porches"
    "will belong to other people by autumn. Both sensations sit in you like a constellation—distinct points that together form a shape."
    "Abuela Rosa squeezes your shoulder and you let yourself lean into the lineage she offers—a long view that softens immediate pain into meaning."
    show abuela_rosa at left:
        zoom 0.7

    abuela_rosa "Hard choices grow the future. You made the hard one for many. That is how we last."
    "You close your eyes against the salt air and listen to the bay, the repaired reed whisper, the low murmur of people making new plans. The signed agreement sits in the TideLab drawer, a document that"
    "will be referred to in meetings and quoted at community meals. It will not be perfect. It will be durable."
    "You stand there a moment longer—proud, hollow, steady—then step back toward the shed where maps wait and seedlings need tending."
    hide abuela_rosa

    scene bg ch13_601bcb_8 at full_bg
    # play music "music_placeholder"  # [Music: Sustain; then gentle fade]

    scene bg ch13_601bcb_9 at full_bg
    "THE END"
    # [GAME END]
    return
