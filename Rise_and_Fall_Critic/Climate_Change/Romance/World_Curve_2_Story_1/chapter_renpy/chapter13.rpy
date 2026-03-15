label chapter13:

    # [Scene: Tideworks Lab | Night]

    scene bg ch13_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, mournful cello with intermittent salt-wind whistles]

    "The lab smells of ozone and boiled kelp, a sharp, mineral tang that sits under everything. Your jacket is still damp where you pressed it to your chest that afternoon — the press release, the charts, the anomaly logs you insisted be made public. You can feel the imprint of Rosa's handwriting in your pocket" "We remember the shore. Honor it."
    "You sit at the workbench and trace a rim of salt across the field notebook Elias left open, a sketch of a small, scalloped reef with notes in his cramped, careful hand. The portable sensor on"
    "his wrist blinks green in the dim; even in the quiet it feels like a second, steady heartbeat."
    "Theo moves a coil of cable with the embarrassed efficiency of someone trying to be useful in a room where the roof isn't quite made for how much rain keeps coming. He clears his throat twice before he speaks, as if the sound might start a tide."
    show theo_mendes at left:
        zoom 0.7

    theo_mendes "They sent a formal notice. Transfers frozen 'pending review.' Looks like the funders sealed the tap faster than a storm door."
    "You do not need him to explain. The sentence lands like another weight on the ledger you've carried for years."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "Public record makes them accountable,' you say. Your voice is flat in the lab's glow. 'We either let the models mislead people or we own the mess and fix it in front of everyone."

    theo_mendes "You did what you think is right. That's—"

    theo_mendes "—not nothing."
    "Elias Navin sets his field notebook down, fingers leaving a faint algae smear on the cover. He looks at you for longer than comfort allows, as if measuring you not with data but with a scale that holds every small decision you've shared."
    show elias_navin at center:
        zoom 0.7

    elias_navin "I told them the anomalies existed. I backed you at the hearing. But the fellowship offer—they said they want me to prototype the reef designs in a place with funding still attached. It would be months, maybe years, and not here."

    mara_kestrel "You're not asking my permission."

    elias_navin "No."
    "He rubs the back of his neck."

    elias_navin "I'm telling you so you don't have to hear it from a press release. I—"
    "He hesitates, and for once the scientist has no neat data to smooth edges."

    elias_navin "I can go and get the proof for the things we believe in. Or I can stay and keep trying with what we've got here."
    "You think of the pilot sites: crabwire frames lashed to pilings, halophyte beds that survived the last surge, children at the Basin poking at mud with painted sticks while Ivy taught them to read tide charts."
    "You think of the funders' glossy briefcases and the way their timelines smelled of antiseptic and distant power."

    mara_kestrel "If you leave, will you come back when you have the proof?"

    elias_navin "If your co-op lets me through customs when I bring my data and a crate of samples? Yes."
    "He swallows."

    elias_navin "But I don't know who I'd be when I return, Mara. I don't know if the politics out here won't have shaped me into someone who makes different compromises."
    "You feel the familiar ache — the one that has kept your sternum tight through council hearings and late-night planning meetings. It is not just about him. It's about the fact that every honest choice costs something."

    menu:
        "Offer to write a joint paper and apply with him":
            "You suggest a co-authored study, a way to bind your work and his even if he's gone. Elias looks hopeful, then weary; he nods slowly, the idea slowing the tremor at his jaw."
        "Tell him to take the fellowship; integrity over presence":
            "You tell him to go. Your words are steely, sacrificial. He flinches, as if you have folded away something bright and put it in his hands. He says he'll go, but the way his eyes dip shows the cost."

    # --- merge ---
    "'Your hand finds the small silver compass at your throat; the cord is frayed where the sea has tested it. You feel like someone who has been picking nails out of a ruined boat — you"
    "are not sure whether what you do will ever make the hull whole again, but you cannot stop pulling.'"
    "Your hand finds the small silver compass at your throat; the cord is frayed where the sea has tested it. You feel like someone who has been picking nails out of a ruined boat — you"
    "are not sure whether what you do will ever make the hull whole again, but you cannot stop pulling."
    "Rosa arrives before dawn, bringing with her the smell of tea and the quiet gravity of the shore she remembers. She wears her shawls like a map of every season, layered and patient."
    hide theo_mendes
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "You did the right thing,' she says, and you hear no argument in her voice — only the steady conviction of someone who has smelled more storms than she lets on. 'There will be losses. There will always be losses. But truth lets people choose with eyes open."

    mara_kestrel "They'll call us reckless. They'll say we scared the city into retreat."

    rosa_alvarez "They will say many things. But when the sea takes what it wants, names do not comfort people who have nowhere to stand."
    "You look at Elias; his jaw is set. In the amber light of the lab, his features are fragile and honest in a way the city does not often allow."

    elias_navin "If I go, I will pack tonight. The fellowship leaves in two weeks."

    mara_kestrel "Two weeks."
    "The word repeats in your head like a tide-clock — small, inevitable. The lab is suddenly too small for all the quiet decisions that must be made."
    # [Scene: Co-op Pilot Site — Shoreline Frames | Morning (Months Later)]
    hide mara_kestrel
    hide elias_navin
    hide rosa_alvarez

    scene bg ch13_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gull calls, the slap of water against frames; the tactile rasp of sand under boots.]
    # play music "music_placeholder"  # [Music: Sparse strings with a low, steady pulse]
    "The pilot projects survived the early failures — not unscathed, but alive. You watch a team lift a newly anchored scaffold from the muck, hands caked with kelp and determination. The data boards are pinned to"
    "a wooden post; the numbers are messy, but honest. Iris of algae bloom every now and then; you log them and move on."
    "Ivy runs up, cheeks flushed, paint still drying on her fingers. She hands you a small watercolor: a childlike reef, painted blue and strewn with glitter like fishing light."
    show ivy_kestrel at left:
        zoom 0.7

    ivy_kestrel "We made it brighter. For people to see."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "It's good work."
    "Ivy looks at the horizon where the city becomes a pale suggestion against wet sky."

    ivy_kestrel "Are you sad about Elias?"

    mara_kestrel "I'm proud he's trying to make change where it can be supported. And I'm angry that the funding system pushed him away."
    "Ivy frowns like it's unfair that the sea is both teacher and thief."

    ivy_kestrel "Maybe he'll come back with a book of proof and a boat full of machines."
    "You want to believe that. You also feel the small room in your chest where absence can live and grow like a quiet bloom."
    # [Scene: The Basin | Evening — Community Meeting]
    hide ivy_kestrel
    hide mara_kestrel

    scene bg ch13_601bcb_3 at full_bg
    # play music "music_placeholder"  # [Music: Low hum of conversation, the distant patter of a late drizzle]
    "The community meets in the Basin to decide how to reallocate the money you still have — tiny amounts of grants, a neighborhood microfund, the proceeds of a single small philanthropic promise that remained after the larger donors withdrew."
    "Jun Park stands a little apart, hands folded. The municipal crispness is still about him, but there is a softness at the edges you have not seen in a long time."
    show jun_park at left:
        zoom 0.7

    jun_park "You forced transparency,' he says. 'It cost us leverage with some big players. It also forced us to recalibrate budgets."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "Our people could not be experimental subjects for a press release. Not after what happened to the harbor families."

    jun_park "You're stubborn in a way that annoys and terrifies me."

    jun_park "I didn't expect you to make the choice you made."

    mara_kestrel "You expected me to bargain."

    jun_park "Politics bargains when people have no other place to put their anger. You gave them a place to act instead."
    "Rosa raises her hand and speaks, the kind of quiet that gathers attention."
    show rosa_alvarez at center:
        zoom 0.7

    rosa_alvarez "We are not finished. We will keep planting. We will keep rebuilding where we can. And we will ask the city to protect those who cannot move."
    "There is applause, not big, but enough to warm the Basin's mud. You feel the thread of community stitch taut and real beneath the damp afternoon."
    # [Scene: The Strand | Dusk]
    hide jun_park
    hide mara_kestrel
    hide rosa_alvarez

    scene bg ch13_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The steady hiss of a far surf; the closeness of voices folding into the dark.]
    # play music "music_placeholder"  # [Music: A soft piano motif, minor key, like a memory recolored]
    "Elias Navin stands with his pack on his back, a small brass watch catching the last light. The fellowship's paperwork is folded in an inner pocket. He has the look of someone who has decided to cross a bridge and knows the bridge will not unroll again."
    show elias_navin at left:
        zoom 0.7

    elias_navin "I wish this could have been different,"
    "His fingers brush the frayed cord of your compass where it rests beneath your sweater; he does not reach for you, only for the gesture of shared history."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "So do I.' The compass is the same weight as always, an old reassurance. 'Do you—"

    elias_navin "Do I regret telling them? I don't think so. Did I find the words you needed in the hearing? Maybe I failed a little, but you gave people truth to hold. That was yours."

    mara_kestrel "And you?"

    elias_navin "I go to get proof. If I can come back with it, then maybe our pilots will stop being pilots and start being parts of a larger shield."

    mara_kestrel "What if you become the thing that makes compromises I can't stand?"

    elias_navin "Then you have every right to call me out. You always did."
    "There's a flicker of a smile that is more about the space between you than happiness. You both know the ledger of costs: months of absence, nights slept in rooms with unfamiliar languages, the possibility of new loyalties forming between lab benches and donors who smell of travel and money."

    elias_navin "Stay. The co-op needs you."

    mara_kestrel "And you?"

    elias_navin "I need to try."
    "It is small, and it is everything. You reach for his hand, and the contact is both heavy with promise and impossibility. You do not force words into neat containers; instead, you let silence do the work of truth-telling."

    elias_navin "I don't want us to be a casualty. If anything, let us be a case study that people read about when they want to know why transparency mattered."

    mara_kestrel "Then go and make that case. Come back to tell us you were right."

    elias_navin "If I were sure of that, I would not have asked you to support my leaving."
    "He swallows."

    elias_navin "I don't have a guarantee. I have a method."

    mara_kestrel "Methods change people."

    elias_navin "Yes. And sometimes they save them."
    "The sound of the sea is a slow metronome. Lantern light catches on his glasses; for a second, you see the glint of the man who studied tide heights on borrowed benches, and the man who stood at your side in council."
    "You let him go with a kindness that tastes like salt and iron. He steps back, then turns and walks toward the quay where the ferry will take him to the city with the international departure. Behind him, the co-op's lights burn — small and defiant against the wide dark."
    # [Scene: Strand — Later That Night]
    hide elias_navin
    hide mara_kestrel

    scene bg ch13_601bcb_5 at full_bg
    # play music "music_placeholder"  # [Music: A single piano note held and then released into low strings]
    "You sit alone on the Strand's rail, the compass heavy at your throat. You think of every person who has watched a boat disappear into the horizon — fathers, mothers, lovers, the young who never had"
    "a chance to be old. The sound of the city is different in the dark; it has the patience of someone who has survived worse but carries the memory like a scar."
    "Rosa finds you and sits down without being asked. She folds her shawl tighter, not against cold but against the particular loneliness of durable people."
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "We did not win in the way we imagined,' she says. 'But we kept our souls. That counts."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "It feels small."

    rosa_alvarez "Small things are seeds. Do not forget what grew from a single sprig of saltgrass."
    "You look at the Basin, the co-op pilot sites, the children who learned to set small buoys and read tide lines. The city will keep making choices; Jun will keep making the hard ones required by"
    "office. You will keep arguing. The funders withdrew; other donors will be wary. The work will be slower, more public, and more honest because of the path you took. Elias will be gone for now, with"
    "a chance to return with proof that could change the city's calculus."
    "You close your eyes and let the tide's humidity press against your face. The Strand holds longer than some predicted. Mothers still cast nets; boys still run gull-chased races along the boards; the lamp posts still flicker when the electricity falters. Hope is not a banner; it is a practice."
    # play music "music_placeholder"  # [Music: Strings swell into a bittersweet chord, then resolve into a tender, muted cadence]
    hide rosa_alvarez
    hide mara_kestrel

    scene bg ch13_601bcb_6 at full_bg
    "Time does not answer whether sacrifices were worth it. It only moves, and you move with it. You have lost a closeness that once seemed inevitable. You have gained something less demonstrative: a community that demands to be counted in its own terms."
    "Jun's campaigning face will still be on posters, but in the Basin that night, his words about recalibration felt less like a rebuke and more like a tentative olive branch. Elias will go where proof may"
    "find purchase. Ivy will keep painting tide-sticks until everyone knows how to read them. Rosa will keep handing out tea to the exhausted and resolute. You will keep being the ledger and the salt."
    "You lift the compass and let it hang between your fingers. It points, as ever, not to some miraculous certainty but to the worn, honest rhythm of the place you love."
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "Be careful, Elias."
    "You do not watch the horizon anymore. Instead you stand and move toward the Basin where the community is cataloguing losses and planting new mangroves at first light. The work is quiet and ongoing, a slow proof against storm-time."
    # play music "music_placeholder"  # [Music: Final soft piano phrase with a long, lingering note]
    hide mara_kestrel

    scene bg ch13_601bcb_7 at full_bg

    scene bg ch13_601bcb_8 at full_bg
    "THE END"
    # [GAME END]
    return
