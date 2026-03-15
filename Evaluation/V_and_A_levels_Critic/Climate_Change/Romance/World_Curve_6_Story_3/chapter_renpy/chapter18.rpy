label chapter18:

    # [Scene: Brinehaven Boardwalk & Docks | Late Afternoon → Night]
    # play music "music_placeholder"  # [Music: Jagged strings, distant percussion; undercurrent of urgent wind]

    scene bg ch15_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A high, keening wind; gulls silenced by the pressure change; a distant metal groan as a half-built bulkhead shifts]
    "You walk the edge of everything you've argued for and against. Papers, subpoenas, and injunctions sit like stalled machines in municipal inboxes — legal pauses that read like gaps in a levee. The town's machinery is"
    "a lung that isn't breathing, and you've been the one to insist on checking its heart."
    "You can taste the litigation in the air: the copper of anger, the blue-ink bite of contracts, the acrid smoke of meetings that burned out without resolution. You pressed for transparency; you pushed for process that"
    "would keep power honest. You never promised miracle. You promised a ledger and light. But light is thin in storm-time, and ledgers don't stop water."

    scene bg ch15_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A nearby pump hisses and then — the small, sickening cough of failure]
    "The first pumps stutter. Somebody in a cracked voice yells they lost power at the secondary node. Wrenches are dropped in the commissary. Your breath catches — the procedural delays, the injunctions that froze contracts while"
    "lawyers argued semantics, mean the firms that would have maintained that infrastructure can’t be deployed. The sea is impatient."

    scene bg ch15_f99e88_3 at full_bg
    # play music "music_placeholder"  # [Music: Percussion ratchets up; a low horn of alarm under the strings]
    "People race. The town turns into a clockwork of improvisation. You move with them, because movement is the only prayer left. You hand out radios, lace boots, pass around blankets. Your notebook is damp at the"
    "edges; fingerprints blot plans into smudges that mean less than your hands do right now."

    "Jonah Reyes:" "You called for checks. You called for the lawyers, Mira. People argued and contracts froze. They delayed the crews. Houses are going under because paperwork sat on a desk."
    "You feel the accusation like a cut. It isn't only his voice — it's the way children stop to stare, the way Tessa's small shoulders flatten as if to push the wind down. You want to"
    "say that you couldn't accept hidden handshakes, that secrecy costs more than pride. You want to say that the contracts you exposed had strings that would have bled the town dry. But the sea is not"
    "listening to explanations."
    "You open your mouth; a dozen answers clamor like broken gulls. Instead you let your hands speak — you hand Jonah a coil of rope. The gesture is practical, immediate. It is also an apology in the only currency they will accept tonight: labor."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "Apologies don't bail water, Mira."
    "Jonah's chest is tight. He glances at a family trying to strap down a roof. His jaw works like tide marks under pressure. The thing between you is not just decisions; it's a shared history you both swum through. Now it is raw."

    menu:
        "Help Jonah secure the pier":
            "You shoulder the rope and run with him, the two of you moving in a practiced rhythm. The world narrows to a hum of exertion and the close, grinding smell of wet timber."
        "Go check the pumps":
            "You sprint toward the pump house, slipping on algae-slick planks. Your hands are already cold; the smell of diesel and metal sharpens your focus."

    # --- merge ---
    "The scene continues."
    hide jonah_reyes

    scene bg ch15_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A new, higher wind; something like a freight train over the harbor]
    "Mid-build seawalls that had been touted as salvation shudder. Where concrete had been poured last week, new fissures bloom like bleeding veins. The contractors, hamstrung by injunctions and frozen bids, are not on site; the temporary seals are all anyone has. The sea finds them."
    "Cassian is here in a slate trench coat, sleeves rolled, sleeves already caked with salt. He looks the way a man looks who thinks his math will save something that turns out not to be a number."
    show cassian_cass_romano at left:
        zoom 0.7

    cassian_cass_romano "If the permits had been signed, we could have reinforced the southern pilings. We could have staged materials before the window closed."
    "You listen to him and feel the surgical logic of his words sharpen into blame. Cass is not cruel — he’s a man whose inner calculus has been taught to value mitigation as a plan. But"
    "when mitigation needs people and people are delayed by the very transparency you fought for, those numbers feel like knives."

    cassian_cass_romano "You forced the town to litigate, Mira. You pushed the pause. I argued for an interim contract. You chose a process that... that stretched the timeline."
    "Cass's eyes hesitate on you, on the coral at your throat. There is a tremor in his lips that he scolds away. The accusation is formal, precise. It cuts with clauses and timetables."
    "Mayor Lynette Cole appears, flanked by two staffers, one arguing into a handheld as if about to commit an ordinance by sheer force of will."
    show mayor_lynette_cole at right:
        zoom 0.7

    mayor_lynette_cole "This isn't the time to litigate blame. We need triage, not indictments. Who can coordinate evac shelters? Who can house the displaced tonight?"
    "Her voice is businesslike but fraying at the edges. The mayor's staff splits—half trying to organize relief, half trying to pick a public narrative. The town's politics are a ripped sail in a gale: everyone clutching fabric and trying to find the seam."
    # play music "music_placeholder"  # [Music: String cluster, then a sharp percussion hit; tempo quickens to a staccato heartbeat]
    "People scream. A boat snaps its mast like matchwood. You run toward the sound and find a family clinging to a ladder as water eats the back of their house. Old Man Rafi is there, stooped"
    "and steady, his beard whipped with salt. He has a small tin kettle over a private, improbable fire he set against the wind, the flame like a defiant eye."
    show old_man_rafi at center:
        zoom 0.7

    old_man_rafi "It will take. It always takes. We cannot be angry at the waves; we can only be careful what we leave within reach."
    "It is not consolation. It is cold, ancestral arithmetic. Rafi's face is a cartography of losses: lines where weather and time and choices have met. He hands you a thermos. The steam fogs your glasses. In"
    "the fog, you see the town's faces tilt toward other people rather than at systems."
    "Tessa rushes up with a tarp over her shoulder, cheeks flushed with wind and effort. She is small and immovable, furious and steady in a way that makes your throat close."
    hide cassian_cass_romano
    show tessa_kestrel at left:
        zoom 0.7

    tessa_kestrel "We did what we could, Mira. We listened to you. We voted. We argued with the council. But at the end of the day, we were still on our hands and knees."
    "Her words are a lance. She blames the process that left them exposed — but there is more: the youthful impatience that once drove her to demand faster action now sits in her chest like grief."
    "She looks at you with an expression that could be disappointment or demand; you cannot tell, and perhaps it is both."

    menu:
        "Tell Tessa you did your best":
            "You wrap an arm around her shoulders, your words thin but true. 'I did what I thought would protect us long-term.' She squeezes you, and for a blink you are simply sisters rebuilding rope together."
        "Tell her she should have pushed harder":
            "You let anger answer instead of regret. 'You should have fought louder at the hearing,' you snap, and the hurt in her eyes sharpens into a cold you cannot thaw."

    # --- merge ---
    "The scene continues."
    # play sound "sfx_placeholder"  # [Sound: A thunderclap like the sky tearing; rain begins as a slicing sheet]
    hide mayor_lynette_cole
    hide old_man_rafi
    hide tessa_kestrel

    scene bg ch15_f99e88_5 at full_bg
    "The brigades you thought you organized are delayed at a courthouse barricade. Volunteers turn back as police redirect them. Injunctions become physical roadblocks; process becomes literal impediment. Contracts that might have kept pumps running are tied"
    "in appeals. The law — meant to protect fairness — has become a web the sea is already cutting through."
    "You try to keep moving. You patch a breach with sandbags and prayers. You hold someone's hand as they wail and tell them what you don't yet believe: that you'll find a way. Each reassurance tastes like ringed salt; each promise is a ledger line you can't look at twice."

    "Voices swirl around you in fractured, human shorthand" "Why did you force that pause?' 'He promised material delivery; where is he?' 'We could have had temporary pylons."
    "Cass catches your eye across a mattress turned improvised raft. He walks toward you and for the first time his mask cracks. He is angry and it is not only the numbers that fuel him."
    show cassian_cass_romano at left:
        zoom 0.7

    cassian_cass_romano "I wanted to work with you, Mira. I showed them scenarios, compromises. We could have hybridized—"
    "Cass's sentence shatters on the roar of wind. He looks small in the open, like a man in a suit at the bottom of a storm drain. You see, briefly, a man who believed his tools were proof against ruin."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "We could have compromised earlier. We could have done a hundred things differently. But secrecy lived in the contracts we refused to sign. I—"
    "Cass interrupts, and it's not only anger; there's grief."

    cassian_cass_romano "Every day we waited for 'due process'—every day was a day the sea had to work with. I don't know if any one thing would have stopped this, Mira, but we can point at the pause."
    "Jonah folds in on the sentence, like a net being drawn tight."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "Pointing doesn't help them right now. People need roofs. Kids need warm places. We can't keep measuring and measuring while there's a family pinned under a beam."
    "The argument ricochets into something rawer: the moral calculus of prevention versus immediacy. You can feel it turning into divisions that will last far longer than the storm's physical scars."
    # play music "music_placeholder"  # [Music: Crescendo — all instruments in a collision; then a momentary silence like lungs held too long]
    hide cassian_cass_romano
    hide mira_kestrel
    hide jonah_reyes

    scene bg ch15_f99e88_6 at full_bg
    "A scream splits the air. The northern pier collapses in a slow, mechanical groan. Timber folds like old paper. You run because running is the only kind of response left that isn't regret."
    "You find yourself alone among wreckage later — the town spread out like a stitched-open palm. Houses half submerged; fishing boats listing like the teeth of a comb; a child's stuffed seal bobbing against a piling."
    "The storm keeps peeling itself away; it is done but not finished. Its debris is a language you can read: lists of things lost and the names of people who built them."
    "You wander the docks in scuffed boots. Your coral pendant swings and clacks against wet denim. The notebook in your hand is sodden; pages are blurred into a grey that means the end of argument and the beginning of tallying."
    "Old Man Rafi has gathered a small crowd around that private fire. He pulls a small, blackened loaf from a tin and divides it among the nearest people. No speeches. No long plans. A man with"
    "a kettle and a loaf and the refusal to let the world spit everyone apart."
    show old_man_rafi at left:
        zoom 0.7

    old_man_rafi "We will mourn. We will name what the sea took. We will plant back what we can plant. But remember: we decide what to put within the reach of the tide."
    "His eyes find you, and his look is unreadable — a ledger that lists the things you kept and the things you asked to be risked. There is no absolution there, only weathered clarity."
    "You sit down on a broken step, the cold seeping through. Tessa folds into your lap as if she can anchor herself there. Jonah stands a little apart, hands jammed in his sweater, the lines of"
    "his face raw and carved. Cass kneels across from you, palms up, not offering solutions but seeking the human thing you can no longer avoid: reckoning."
    "The town is fractured. Friendships spliced by blame. The mayor's office is a corridor of whispers that might become subpoenas. Contractors file notices. Insurance adjusters comb through names like scavengers."
    "You count the losses in a way you always knew you eventually would: not in piles of rubble but in faces. The man who lost his boat. The child who will wake to a different street. The small bakery you helped study that will probably close."
    "Your chest is a weight. You have insisted on ethics, on transparency, on process — beautiful things on a whiteboard. Tonight, the ledger is full of a different arithmetic: delay plus law equals exposure. The sea turned every pause into an opportunity."
    "You fold the notebook closed. The pages press damply against your palm. In that simple act there is a kind of end: a listening that becomes a silence, a tally that becomes a tombstone for decisions."
    "You want to make a speech. You want to command a redirect. You want to fix everything and everyone will listen and everything will be repaired. But the people around the fire are not a council"
    "in that utilitarian sense; they are a collection of wounds. Words will not stitch them. They will need time, and the town will need rebuilding, and many things you loved will never be the same."
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "We love this place, Mira. I love you in a way that makes me furious when you make others mad. I can't tell if I'm angrier at the sea or at you."
    "His hands are dirt-scraped. His eyes are not unkind. They are heavy with a question that will not have an easy answer."
    "Cassian 'Cass' Romano draws back to the edge of the crowd, his coat speckled with rain. He meets your gaze once more. The corporate tools at his elbow are smaller than his hands in this moment;"
    "there are no models that can account for the sensation of a neighbor losing a life on the water."
    show cassian_cass_romano at center:
        zoom 0.7

    cassian_cass_romano "I wanted to be useful. I wanted to be more than the suit. Maybe I still can be. Maybe not. I don't know what happens next."
    "His admission is not reconciliation; it is a small, human crack. You nod, because nodding is a thing you can do."
    "The tide will still reshape the inlet. Contracts will be rewritten. Laws will be amended. The town will file claims and petitions. Media will come and leave. There will be inquiries with witness lists and cold, bright rooms where people will argue about what could have been done."
    "Old Man Rafi puts a hand on your shoulder. It is the oldest kind of touch: a blessing and a benediction to the next day."

    old_man_rafi "We will be judged by what we rebuild with, not just what we tried. Remember that, Mira."
    "You press your thumb to the coral pendant. It is warm against your skin. The pendant has no power over storm-surge physics, only over whatever human rituals you can carry forward."
    "You close the notebook. The sound is small in the vast night — a wet, resigned clap. The pages no longer behold plans; they are a record of what was attempted and, perhaps, of where you miscalculated. You feel the weight of choices like concrete on your chest."
    # play music "music_placeholder"  # [Music: A low, final chord; no triumph — only a long, honest toll]
    hide old_man_rafi
    hide jonah_reyes
    hide cassian_cass_romano

    scene bg ch15_f99e88_7 at full_bg
    "You do not have a tidy romantic resolution. There is no neat scene of lovers finding each other amid the ruins with everything mended and every difference forgiven. Love is here in other forms: in shared"
    "blankets, in shared labor, in the way hands reach for each other to pull someone free. Sometimes that will be enough; sometimes it will not."
    "You let the seawind take the rest. You stand, place the notebook in your jacket, and let the night hold you for a moment longer. Grief is a weather that must be endured. So is the reckoning."

    scene bg ch15_f99e88_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The fire crackles; far-off emergency sirens wail and then fade into the rain]
    "You breathe in the raw air of aftermath. You count loss and name like a litany: houses, boats, a bakery, childhood summers. You count what remains: a community that will now have to decide what to give up and what to hold onto, with less certainty and more pain."
    "You close your eyes and let the memory of choices — the signatures you pushed for, the pauses you insisted upon, the arguments that saved money but delayed help — slide under your skin. They are"
    "not absolution and they are not damnation. They are the small, terrible calculus of trying to be moral in a world that does not stop for morality."
    "You feel the town around you breathe: exhausted, raw, and already beginning the small motions of salvage. The fire keeps singing. People trade lists and numbers. The sea, indifferent and uncompromising, moves on."
    "You sit by the tin kettle and understand a truth you had been avoiding: inertia can be as lethal as malice. You had tried to tilt the world toward a way you thought fairer; the world tilted back in ways that make fairness look like a luxury."
    "You close the notebook and let the weight sit on your lap, a physical tally of what you knew and what you didn't. You have no map that guarantees salvation — only a ledger of choices and their inevitable, human aftermath."
    # play music "music_placeholder"  # [Music: Fade to a single low note; the town's murmured voices rise like distant surf]

    scene bg ch15_f99e88_9 at full_bg

    scene bg ch15_f99e88_10 at full_bg
    "THE END"
    # [GAME END]
    return
