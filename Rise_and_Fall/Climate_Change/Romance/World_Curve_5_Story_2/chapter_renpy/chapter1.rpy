label chapter1:

    # [Scene: The Watchhouse | Morning]

    scene bg ch1_Start_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of the town waking—distant gulls, a half-assembled drone whirring, a coffee machine sighing]
    # play music "music_placeholder"  # [Music: Soft, optimistic piano with a gentle swell of strings]
    "You stand with your palm against the cool, salt-smudged window and watch the bay unfold. The Watchhouse is a hub of tidy chaos: tide charts taped to beams, seedlings in mismatched mugs, a whiteboard crowded with"
    "annotated timelines. Your field sketchbook sits open on the desk—shoreline cross-sections in quick, practical strokes—next to a laptop with the pilot model still running its last simulation."
    "The living-shoreline pilot you helped shepherd through the winter is finally—quietly—doing what the data promised. A thread of success hums beneath your ribs, careful and fragile, but real: clumps of cordgrass are taking, sediment is settling"
    "where it shouldn’t, and a small patch of eelgrass has returned in a sheltered cove. That means more than numbers. It means someone’s crab trap will keep working next season; it means a family’s front stoop"
    "might still be the place they talk about the weather."
    "Marco pops his head through the office door, the familiar scrape of his cap against the frame. He’s carrying a box of community flyers—handed out by Rosie at the co-op—bright with paint and optimism."
    show marco_maris at left:
        zoom 0.7

    marco_maris "Morning, Lena. You look like you slept at the desk again."
    show elena_lena_maris at right:
        zoom 0.7

    elena_lena_maris "Only until the tide chart woke me.' (You smile because you have to; it feels truer than the joke.) 'How’d Rosie want the flyers laid out?"

    marco_maris "By the pier, the co-op, and her noticeboard. She says people need something pretty to read for a change.' (He shrugs.) 'Also—Jonah’s asking if you want him to swing by before the council."
    "Your chest loosens a little. Jonah’s presence is like warm workcloth—practical, familiar, quietly encouraging. You rub at the crescent scar near your brow without thinking; daylight brings out that pale line, and with it the memories"
    "of the storm that took your childhood home. You tuck the feeling away and nod at Marco."

    elena_lena_maris "Send him up. I could use someone who remembers exactly where we sank the root bundles last month."
    hide marco_maris
    hide elena_lena_maris

    scene bg ch1_Start_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A soft chime—your AR tablet lighting up with a brief from Valence Urbanworks]
    # play music "music_placeholder"  # [Music: A hairline tension note undercutting the piano, then resolving back into warmth]
    "A translucent packet folds into being above your desk: Iris Valence’s logo, clean type, and a crisp brief titled: “Brinehaven Protective Proposal — Phase I.” You let it hover unread for one beat, then open it."
    "The render is impeccable: sweeping seawalls, drone-lifted photos, and a polished animated timeline claiming quick, quantifiable safety."
    "There’s pride in the execution—impeccable renderings, a cadence that persuades. But you feel the small, gathered resistance in your chest; your pilot isn’t about glossy finality. It’s about people stumbling through fixes that leave them whole."
    "The brief presses at the same question that’s been tugging since you came back to Brinehaven: how do you scale care without bartering away the town?"

    menu:
        "Read Iris's brief fully now":
            "You skim the renders; Iris’s voice—efficient and persuasive—loops through the annotated timeline. Your mind catalogues the gains, the trade-offs, the assumptions about relocation and economic models. You close the brief with the outline burning in your head—useful, but not enough."
        "Set the brief aside and let Jonah see it first":
            "You pin the brief to the corkboard, watch it reflect the morning light. When Jonah arrives, you’ll have another pair of eyes—someone who balances technical detail with the town’s pulse. It feels wise to wait, to not let Iris’s sheen knock you off course before hearing the boots-on-the-docks perspective."

    # --- merge ---
    "..."

    scene bg ch1_Start_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The door’s hinges protest a friendly, saluting squeak]
    # play music "music_placeholder"  # [Music: A soft folk guitar thread enters, complementing the piano]
    "Jonah Reyes drops his pack and leans on the counter like it’s the most natural place in the world to stand. He rubs a smudge of mud from his knuckle onto his thumbnail and looks at the screen with easy curiosity."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "Pilot data looking like miracles, or just stubborn survival?"
    show elena_lena_maris at right:
        zoom 0.7

    elena_lena_maris "A little of both.' (You tap the simulation.) 'Sediment accretion’s tracking higher than we predicted in those micro-cells. Volunteers did the bulk of the work. Rosie’s crew nailed the plantings."

    jonah_reyes "That’s community muscle, Lena. You didn’t build that with contractors—you built it with people who know the tides.' (He pauses, reading your face.) 'Iris’s brief—saw something fly past the tower last night. Glossy render, right?"

    elena_lena_maris "You saw it?' (You feel the brief’s cool paper in the corner of your mind again.) 'I did. It’s…complete. Too complete maybe.' (You thumb the edge of your sketchbook.) 'It suggests buy-outs and a salt-scaled promenade. The math is neat. The human cost isn’t in the table."
    "Jonah Reyes’s smile tightens, not unkindly."

    jonah_reyes "I don’t trust anything that erases people for cleanliness. But we’ll need allies who can sell scale with heart. The council listens when data looks decisive. Your job is to show them that decisive data can come from belowground too."
    "The two of you talk logistics—measurement windows, volunteer rosters, a plan for an open site day at the marsh where families can see the pilot’s roots taking hold. Conversation stretches into gentle, significant things: the way"
    "Jonah describes a planting technique and you picture him on his knees in the mud, the way you feel when someone names work you did as evidence rather than anecdote."
    # [Scene: Marshlands / Living Shoreline Site | Late Morning]
    hide jonah_reyes
    hide elena_lena_maris

    scene bg ch1_Start_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Slosh of mud, the rustle of grasses, distant laughter of volunteers]
    # play music "music_placeholder"  # [Music: Ambient strings with a hopeful rise]
    "You walk the marsh board, boots sinking just enough to feel the earth’s resistance. Cordgrass swagged out like small hands anchoring the shoreline. Little birds pick among the shoots; the mud glints silver. Jonah points to a transect where silt has already collected two centimeters higher than last month."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "This right here—this is proof. The plants slow the water enough that the sediment drops. It’s not sexy, but it stacks years into a season."
    "You kneel and let your glove press into cool, yielding mud. It has the smell of old storms and new seeds. You close your eyes for a heartbeat and think about the children who will next"
    "learn to fish from this stretch of shore. You think about your old house, a half-memory of a roof and the scream of wind."
    show elena_lena_maris at right:
        zoom 0.7

    elena_lena_maris "People came back this morning—picked up brochures, asked smart questions. Rosie’s doing an open-day this weekend.' (You look up at Jonah.) 'We’ll need more than biology. We’ll need a narrative that lands in their bones."

    jonah_reyes "Then we tell it honest. Show the photos, the transects, and then bring someone up to the mic who’s been here longer than both of us.' (He nods at the pier, at the town.) 'They respond to truth they can touch."

    menu:
        "Sketch the transect now":
            "You pull your sketchbook out and draw—quick geometry of root bundles and sediment lines. The tactile motion steadies you and gives language to what you’ll say at the council."
        "Record a short video with Jonah explaining it":
            "You hand Jonah your phone. He explains with the easy cadences of someone who has done this in public before. The recording feels vivid; it will make the science accessible when you bring it to the council."

    # --- merge ---
    "..."
    hide jonah_reyes
    hide elena_lena_maris

    scene bg ch1_Start_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Elevator-style ding of multiple device pings; community voices filtering through the door]
    # play music "music_placeholder"  # [Music: Piano returns, firmer and more affirmative]
    "Back at the Watchhouse, you set up for the small council meeting: a ring of folding chairs, your laptop with the pilot graphs queued, a printed stack of volunteer testimonials, and the warm anonymity of a"
    "travel mug. People filter in—Marco takes a place at the back with an easy, brotherly grin; a councilwoman who once scavenged supplies from the docks folds her hands and listens with clear eyes."
    "When you stand to present, your palms are steady because you have touched the mud, because you have mapped the living shore with your own hands and because the community’s face is in the room with"
    "you. You speak in two registers—clear numbers, and the human notes that make numbers necessary."
    show elena_lena_maris at left:
        zoom 0.7

    elena_lena_maris "Our pilot shows measurable accretion in three tested transects. That translates to a half-percent reduction in shoreline retreat annually at current projections, but more importantly, it reduces storm surge impact on the neighborhood piers. The cost is lower, the jobs are local, and the rebuilds keep people where their lives are."

    "Councilwoman" "You’re asking for funding, Lena. How much, and what’s the timeline?"

    elena_lena_maris "Seed funding for the next phase—expanded plantings and two retrofits at vulnerable frontages. Timeline: two full seasons to show cumulative gains, but with immediate co-op job placements. We’re not asking to be the only answer, just a viable, scalable piece of one."
    "Questions fly—good, practical ones. A finance clerk asks about maintenance; Marco offers an on-the-ground plan. A skeptical planner wonders about the seawall renderings they’ve been seeing. You answer, balancing patience and insistence: the pilot is not"
    "anti-structure, but it argues that nature-based solutions can be cheaper, more adaptive, and keep communities intact."
    "Iris Valence’s brief is projected briefly on the side when an aide asks about alternative proposals. The room takes it in—slick masthead, confident language. You let the image sit there, then steer the attention back."

    elena_lena_maris "We can work with any project that respects the community contract. But if scale is your worry, measure the living shoreline’s scalability alongside engineered work—not as a footnote."
    "Jonah Reyes stands and speaks for a minute, not a prepared speech but a clear, earnest listing of trade-offs—jobs retained, local knowledge preserved, ecological benefits that undercut long-term costs. His voice carries; people in the room"
    "nod at specifics. The energy tilts subtly: curiosity, then consideration, then a low, shared warmth of something possible."
    hide elena_lena_maris

    scene bg ch1_Start_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A soft murmur of agreement and the shuffle of chairs]
    # play music "music_placeholder"  # [Music: Triumphant, but understated—strings, a small chorus]
    "When the meeting slows, the council chair leans forward."

    "Council Chair" "We can allocate a small pilot expansion budget for community contracts and monitoring. It’s not a final answer, but—' (He looks at you with a rare, frankness.) '—you gave us confidence that the data means something."
    "You feel your ribs unlatch. It’s not everything. It’s the most important next thing: an institutional ear open enough to consider a different map. Your throat tightens—gratitude, relief, the weight of what could follow."
    "Marco claps loudly in the back like a kid at a school recital. Jonah Reyes’s eyes meet yours across the table; there’s both celebration and that steady, shared work plan written into the curve of his mouth."
    "You collect your notes and look at the pinned brief from Valence again. It’s still immaculate. But now there’s breath in the room—the possibility that scale can include the small, stubborn life of a place."
    "You walk to the window as the meeting breaks up. The pier catches the late light; gulls thread the sky. You think of the marsh you just left, of the volunteers’ callused hands, of Rosie’s paint-splattered"
    "flyers. The tilt is upward—a council’s tentative yes, a scientist’s nod, a lover’s steady presence."
    show elena_lena_maris at left:
        zoom 0.7

    elena_lena_maris "This is how you begin: not by bulldozing certainty, but by stacking small certainties together until a town’s rough edges hold."
    hide elena_lena_maris

    scene bg ch1_Start_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft ticking, like a distant tide]
    # play music "music_placeholder"  # [Music: A warm chord resolves and lingers]
    "You feel buoyed, not by triumph, but by a direction that bends toward care. There will be more briefs, sharper offers, and hard questions. For now, the pilot’s numbers live beside human testimony, and both have been heard."
    "You tuck your sketchbook into your jacket. Outside, the town moves like a living thing—people returning to errands, kids skipping stones. You let yourself take a moment to be hopeful."

    scene bg ch1_Start_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter2
    return
