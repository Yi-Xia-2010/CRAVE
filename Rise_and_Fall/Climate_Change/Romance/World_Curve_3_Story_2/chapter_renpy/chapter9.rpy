label chapter9:

    # [Scene: Engineered Sea-Wall | Late Morning — Construction Phase]

    scene bg ch9_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant clatter of rigging, the rhythmic thud of a hydraulic hammer, gulls complaining above]
    # play music "music_placeholder"  # [Music: Steady, hopeful strings under a soft percussion]
    "You stand on the temporary scaffolding with your notebook folded in a pocket, the leather warm from a sun that feels newly possible after so many wet seasons. Below you, men and women in high-visibility vests"
    "move like a practiced tide — measured, efficient. When the breakers hit the new curve, the spray folds neatly along the wall and rolls back toward the open sea instead of tearing into the town."
    "It is exactly what the contract promised: a visible, structural promise. It is also exactly what the marsh is not."
    show elias_hart at left:
        zoom 0.7

    elias_hart "They finished the last buttress before breakfast. The engineers are recalibrating the intake valves to reduce scour. Kenji said it might help the current drift near the inlet."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "And the pilots? The conditional clauses—the community oversight?"

    elias_hart "The clause is enrolled. Legal's drafting the enforcement matrix with the Mayor. You pushed for it; they put it on the public record."
    "You can hear the future in his words: containment, audit, clause. The language comforts and constrains."

    elias_hart "We saved the boardwalk. We saved the market face. That's real, Amina."

    amina_reyes "Yes."
    "The word tastes like both salt and relief. 'But the marsh—'"

    elias_hart "We did everything we could within the envelope you asked for. I—' He lets his hand rest on a railing as if to hold himself steady. 'I don't like the parts we couldn't protect."
    "You both watch a crewman secure a panel. The sound of the bolt turning is oddly final."

    menu:
        "Walk down to the base and speak with the workers":
            "You climb down the temporary stairs. Mud squeezes between your boots. A forewoman wipes her hands on her belt and tells you, plainly, what the currents did last month; you listen, notebook out, rubbing the bridge of your nose until the ache is a plan."
        "Stay above and talk logistics with Elias":
            "You stay where you are and let the lines of the project unfold: procurement schedules, maintenance windows, public compliance checks. Elias speaks numbers; you think about the people those numbers represent."

    # --- merge ---

    elias_hart "Whatever you do, don't shoulder this alone. Not now."

    elias_hart "Whatever you do, don't shoulder this alone. Not now."
    "You want to argue—you want to name blame and shove it into ledger rows—but the sea is loud enough to swallow a fistful of words. Instead you let the sound be a container for something larger than your anger: responsibility, messy and real."
    # [Scene: Town Center — Late Afternoon]
    hide elias_hart
    hide amina_reyes

    scene bg ch9_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low conversation, a kettle steaming from a food stall, the distant echo of children's laughter]
    # play music "music_placeholder"  # [Music: Warm acoustic guitar, a gentle rising motif]
    "The market smells of lemon oil and fried whitebait and something older—soap, tar, the particular musk of a place that has worked the sea for generations. The wall's shadow has changed the market's light; sun hits"
    "different angles, puddles no longer swallow the wooden planks as before. People move with a weight removed from their steps. A child chases a paper windmill across new concrete; an elder sips coffee and watches the"
    "water that once licked their doorstep sit obediently behind the wall."
    show marina_lopez at left:
        zoom 0.7

    marina_lopez "The teachers were at the meeting. Enrollment's up—parents feel safer. They asked about the apprenticeship fund."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "We set aside the transition grants. Vocational training will be first on the agenda."

    marina_lopez "You did it, Amina. Whatever else changes."

    amina_reyes "We did a thing that keeps people here."
    # [Scene: Marsh Edge | Dusk]
    hide marina_lopez
    hide amina_reyes

    scene bg ch9_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hush of evening insects, a distant motor, the soft plop of water against a modified jetty]
    # play music "music_placeholder"  # [Music: A hopeful piano line threaded with low, resonant strings]
    "You walk along the marsh's edge with Niko Kaur. The boatyard is quiet tonight; a single hull sleeps on blocks, a lamp inside throwing a rectangle of amber light. Where your hands used to meet in"
    "the routine grease and varnish of fixing a keel, something has come between you — a new current you didn't choose."
    show niko_kaur at left:
        zoom 0.7

    niko_kaur "I thought you promised we'd keep this our way. Community control or nothing."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "You told me that you couldn't sign without a clause guaranteeing community control beyond a single election. We put that clause in. We made it enforceable."

    niko_kaur "A clause doesn't keep the current. A clause doesn't stop the way the channel moved. You worked the compromise."

    amina_reyes "I didn't choose the sea to shift."

    niko_kaur "No. You chose what you could, Amina. And I chose that I couldn't watch the marsh die with my hands tied.' (His voice tightens.) 'Maybe I wanted something purer. Maybe I wanted us to row in the same direction. I thought we were."

    amina_reyes "We were."

    niko_kaur "Then go be the person you promised. But don't expect me to clap for the concrete."
    "He does not slam a door. He leaves like the tide — slow, inevitable, pulling away. There is a grief in you that is quiet, precise, and almost useful; it gives you something to do with your hands."

    menu:
        "Call out to him, ask to keep an open channel":
            "You call his name; it's nearly lost in the wind. He half-turns, indecisive, and you press a scrap of your schedule into his palm—a volunteer day. He looks at it long enough that hope flutters, then puts it in his jacket."
        "Let him go; focus on the restoration maps":
            "You tuck your hands into your jacket pockets. You unfold the tide map from your notebook and begin to trace possible restoration pockets with your fingertip, each dot a small commitment toward something larger."

    # --- merge ---
    "Continue narrative at next scene: Town Hall / Planning Office | Morning — Weeks Later"
    # [Scene: Town Hall / Planning Office | Morning — Weeks Later]
    hide niko_kaur
    hide amina_reyes

    scene bg ch9_3be532_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low murmur of people shifting paper, a coffee maker sighing in the corner]
    # play music "music_placeholder"  # [Music: Quiet strings that swell into a soft, determined harmony]
    "Mayor Lucia Varela presides with a steady gravity. Dr. Kenji Sato has data projected behind him; the model lines tremble and then settle into trajectories. You present a matrix of restoration pockets—small wetlands to be reconnected,"
    "dredging reductions to preserve eelgrass beds, a community transition fund for fishers to retrain as marsh technicians and eco-guides."
    show mayor_lucia_varela at left:
        zoom 0.7

    mayor_lucia_varela "The council appreciates the clarity. You've framed the costs, the timelines, and the human resources."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "The pockets will need stewardship. We need seed-planting drives, apprenticeships in wetland repair, stipends for households who shift livelihoods during the transition. If we don't create alternative incomes, we'll lose people to the city."
    show dr_kenji_sato at center:
        zoom 0.7

    dr_kenji_sato "The models suggest that, over a decade, well-placed living patches can begin to re-accumulate sediment and slow the erosive currents. It is not immediate. But there is a path."
    hide mayor_lucia_varela
    show elias_hart at left:
        zoom 0.7

    elias_hart "I've reallocated contingency funds for the apprenticeships. Regional partners will co-fund maintenance if the community proves co-governance in the first two years."
    "You feel the lift of that sentence like a wind at your back. Policy language is practical air; it can carry seeds if you plant them in the right hands."

    amina_reyes "We'll staff a steering committee that includes boatwrights, vendors, and teachers. Marina will lead outreach. Niko—if they choose—can oversee the boatyard cohort. We'll write enforceable milestones into the funding release."
    hide amina_reyes
    show mayor_lucia_varela at right:
        zoom 0.7

    mayor_lucia_varela "Then we will vote to allocate the first tranche. This town deserves to be heard in the region."
    "A murmur of affirmation crosses the room. It is not thunderous, but it is something—and sometimes, in weather and politics, something matters more than everything."
    # [Scene: Niko's Boatyard | Late Afternoon]
    hide dr_kenji_sato
    hide elias_hart
    hide mayor_lucia_varela

    scene bg ch9_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Planers, low conversation, a child's delighted shriek as a bird lands on a mast]
    # play music "music_placeholder"  # [Music: Steady, hopeful percussion; a soft cello underpinning]
    "Time has a slow, honest way of rearranging grief into work. Niko Kaur's hands are rougher, their jaw looser. They don't answer the calls as often, but they show up to a training day, then another."
    "You watch from the dock as they demonstrate a scarf joint to an apprentice, patience tucked into every motion."
    show amina_reyes at left:
        zoom 0.7

    amina_reyes "Your join is cleaner than I remember."
    show niko_kaur at right:
        zoom 0.7

    niko_kaur "Learner's hands want neatness.' (He looks at you then—there is distance, but not hatred.) 'You did what you had to do. I didn't."

    amina_reyes "I'm trying to fix what we can. I'm trying to make the marsh live again in pieces."

    niko_kaur "Then make it live. If I can help—on my terms—I will. Not for the contracts, but for the boats."

    amina_reyes "That's all I ask."
    "There is a small truce you did not know you needed until it wrapped around you. It is not reconciliation; it is an opening. It is work forming as a promise."
    # [Scene: Marsh Restoration Day | Early Morning — Months Later]
    hide amina_reyes
    hide niko_kaur

    scene bg ch9_3be532_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Laughter, the slap of muddy boots, a child's voice reading plant names, the soft admonishment of elders with practiced hands]
    # play music "music_placeholder"  # [Music: A gentle choir of strings and woodwinds; the melody lifts]
    "You stand ankle-deep, the cool mud sucking at your boots, your bracelet damp and steady against your wrist. Hands reach for you with buckets, seedlings, questions. You map micro-restorations with a practiced economy—this bend for sediment, that reed for shelter. Each action is small and immediate and tangible."
    show dr_kenji_sato at left:
        zoom 0.7

    dr_kenji_sato "The sediment is returning in pockets. It's slow, but it's measurable."
    show mayor_lucia_varela at right:
        zoom 0.7

    mayor_lucia_varela "The apprenticeship program just filled its second cohort. People are learning to measure marsh health as a job."
    "Elias Hart arrives with logistics intact—water, refreshments, the press held at arm's length. He stands beside you, sleeves rolled, hands stained with mud. He looks at the people around him with a softness you rarely see."
    show elias_hart at center:
        zoom 0.7

    elias_hart "You did this, Amina. You made them see that the marsh's value goes beyond the map."
    hide dr_kenji_sato
    show amina_reyes at left:
        zoom 0.7

    amina_reyes "You helped, too. The clauses bought us breathing room to start this kind of thing."

    elias_hart "The clauses should have been yours from the beginning. I'm sorry for the ways I bargained the town."

    amina_reyes "Sorry doesn't undo tides. But it makes the present kinder."
    "You both kneel, planting in synchronized motion as the sunlight loosens from behind a cloud and the marsh smells of wet roots and new growth. Around you, people talk about a future that is patchwork and long. They talk like people learning a new language: tentative, dedicated, hopeful."

    menu:
        "Offer Elias your hand, committing to rebuild together—professionally and personally":
            "You slide your hand into his, fingers muddy, and he holds on. It is not an oath to erase the past, but it is a compact: work, respect, and careful tenderness."
        "Keep your hands in the work—let rebuilding be the bond, not promises":
            "You keep your hands on the seedlings and meet his gaze for a long second. He nods, understanding. Your partnership becomes a steady, work-shaped thing rather than a declaration."

    # --- merge ---
    "Continue narrative at next scene: Town Center — Late Evening — After a Season"
    # [Scene: Town Center — Late Evening — After a Season]
    hide mayor_lucia_varela
    hide elias_hart
    hide amina_reyes

    scene bg ch9_3be532_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low contented murmur of a gathered crowd, a radio playing a local song, the distant hush of protected water]
    # play music "music_placeholder"  # [Music: A sustained, warm chord with a bright, ascending motif]
    "The town is quieter in some ways—less frantic running for sandbags, fewer frantic repairs in the night. The center breathes easier. Children run with the kind of unbothered laughter that once felt fragile. Vendors talk about"
    "new schedules, about combining market days and stewardship days. The ache is still there; it is a constant undertow under the surface joy. But people are present in the center again, and presence is a form"
    "of recovery."
    "You sit with Mayor Lucia after the meeting about the next tranche."
    show mayor_lucia_varela at left:
        zoom 0.7

    mayor_lucia_varela "You've shouldered a lot, Amina. The council owes you for more than your proposals."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "I owe it to them. To everyone who can't take another season of losing what they love."

    mayor_lucia_varela "Then keep leading. The region will be watching Marisol as a model. You will set precedents."
    "You feel the old guilt—tight and familiar—shift into a different shape: the weight of responsibility that demands action instead of private mourning. It is no lighter, but it is directed."

    amina_reyes "I'll keep mapping. I'll make sure the funds go to people who need them. I'll measure the marsh every season."

    mayor_lucia_varela "Then rest tonight. Tomorrow, you plant again."
    "You do rest, briefly. In the quiet of your small kitchen, the friendship bracelet brushes against a notebook page where you have written 'Year 1: pockets A–F, apprentices 12.' You put a thumb over the letters"
    "as if to hold the plan in place. The town sleeps in a safer arc from the sea now; that is a concrete truth under the ache."
    # [Scene: Marsh Edge | Sunrise — A Year Later]
    hide mayor_lucia_varela
    hide amina_reyes

    scene bg ch9_3be532_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Bird calls, a soft wind, the measured slap of two people walking on a boardwalk]
    # play music "music_placeholder"  # [Music: Warm, rising strings with a soft brass motif that hints at endurance]
    "You walk the edge with Elias Hart. There is a companionable silence between you, the kind that has evolved from urgency and shared labor. When you speak, it is practical and also something like trust."
    show elias_hart at left:
        zoom 0.7

    elias_hart "The maintenance log shows reduced scour in the northern pocket. The apprentices are doing excellent monitoring."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "We still need funds to scale this. There are more places to plant. More people to train."

    elias_hart "Then we'll write the next proposal together."
    "You look at the marsh where the seedlings now offer texture to the once-flat mud. It is not restored to what it once was—the channels have altered, some ancestral grounds are now part of a shifted"
    "current—but there are places of life returning. The sound of gulls is different; it is not the same chorus as before, but the song is not silence."

    amina_reyes "Do you ever regret—"

    elias_hart "All the time. But regret and resolve can sit together. We can hold remorse and still act."

    amina_reyes "I still carry the brother with me. I always will. But it doesn't stop me from building."

    elias_hart "We are a cautious pair now. Maybe that's what safety looks like in a place like this."
    "You let your hand rest in his. It feels like a pact that is both professional and personal, braced by mutual care and the knowledge that grief shapes you into the person who shows up. Niko's"
    "absence is a hollow you have learned to name; it does not vanish. It yields space for a complicated tenderness that is not the same thing."
    # [Scene: Rooftop Community Garden | Dusk — Community Celebration]
    hide elias_hart
    hide amina_reyes

    scene bg ch9_3be532_9 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Toasts, a ukulele, quiet conversations sweeping the rooftop like warm air]
    # play music "music_placeholder"  # [Music: A resolved, uplifting chord with a gentle vocal hum]
    "You stand a little apart, the festival buzz wrapping around you. Marina catches your eye and raises a paper cup in a little salute. The apprentices laugh in the distance, a voice like a new rope thrown out and caught."
    "You think of the cost — the marsh that will take years, maybe decades, to show its sutures. You think of quiet markets and fewer boats and the people you couldn't keep from grieving. You think"
    "of the day the concrete held the water back and the child who ran without fear."
    "You fold those things together and feel, for the first time in a long time, a steadier warmth under your ribs. This is not closure in the way of ending all hurt. It is closure as"
    "an ability to move forward with purpose—an action formed in the wake of loss, not as denial of it."

    "You open your notebook and add a note in the margin" "Year 2: Expand pockets; continue co-governance reviews; measure social resilience metrics."
    "Elias Hart stands beside you, not claiming you, but sharing the job. You are both changed—wiser, more cautious, more patient. You will love carefully, if you love. You will lead fiercely, because leading is the way you honor the losses."
    "You look out once more across the marsh. The water catches the last light like a promise. The stitches we have sewn are small and imperfect, but they are stitches all the same."

    scene bg ch9_3be532_10 at full_bg
    # play music "music_placeholder"  # [Music: A warm, resolved chord that lifts and lingers]
    # play sound "sfx_placeholder"  # [Sound: The soft, steady lap of water against new and old shores]
    "You fold your notebook closed and let the friendship bracelet rest against your palm. You do not forget. But you move. You plant. You legislate. You teach. You love with caution and with courage."

    scene bg ch9_3be532_11 at full_bg
    "THE END"
    # [GAME END]
    return
