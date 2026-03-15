label chapter22:

    # [Scene: The Old Boatyard | Morning After Dawn]

    scene bg ch13_5ceb3d_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, insistent cello; tempo steady, a thread of urgency under the quiet]
    # play sound "sfx_placeholder"  # [Sound: The rasp of a chisel, distant gulls, water lapping in the slip]
    "You arrive before most of the town is awake, because the work that follows a storm never fits office hours. The air still tastes of iron and wet rope. Your boots sink slightly where the ground is soft, and the smell of fresh-cut wood is almost unbearably sharp—clean and mortal."
    "Eli is hunched over the reclaimed hull, shavings curling like pale seafoam at his feet. He doesn't look up when you approach; he never dramatises grief. He works it into something people can touch."
    show eli_duarte at left:
        zoom 0.7

    eli_duarte "Morning. Thought I'd start on the keelboard memorial before the tide takes the pieces I'm keeping."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "You shouldn't be doing this alone."
    "Eli pauses, knife poised. He studies the wood as if weighing a confession."

    eli_duarte "You weren't here to hand me the last coffee. Thought I'd make it useful. Carving helps. People can read it with their hands."
    "You smell the citrus of the thermos he finally offers—coffee, black as apology."

    asha_moreno "What will you put on it?"

    eli_duarte "Names, mostly. Small things people said before they left. A line for boats that never came back. Maybe we'll leave room for the next storm."
    "You lift the compass from beneath your collar; it feels heavier than it has any right to. The brass is matte with salt. You run a thumb along the rim and realize the edges of your careful plans are starting to fray in the same way."

    eli_duarte "You did what you could. You were here. People know that. They'll say things—they'll fight and they'll forget and they'll remember. That's how towns stitch."
    "You let the words settle. The boat's flanks shiver with memory and plank-scarred patience. The urge to fix everything is loud in your chest; you set it down in favor of this small, human thing: steady hands, a shared ritual of naming."

    menu:
        "Take the mallet and help shape the keelboard":
            "You lift the mallet and the motion is at once clumsy and exact; your strike chips a clean curl from the wood and Eli grins, surprised. The act anchors you in the present, and for a moment the weight of the compass becomes manageable."
        "Stand back and take notes for the memorial plaque":
            "You uncap your pen and sketch layout lines on your ledger. The planning voice in you arrives like a tide—precise, useful. Eli nods; the work becomes shared across different kinds of hands."

    # --- merge ---
    "Scene continues"
    # [Scene: Raised Gardens & Floating Market | Mid-Morning]
    hide eli_duarte
    hide asha_moreno

    scene bg ch13_5ceb3d_2 at full_bg
    # play music "music_placeholder"  # [Music: A faster unsteady rhythm—violins undercut with urban percussion]
    # play sound "sfx_placeholder"  # [Sound: Laughter that starts thin and breaks—seed rattle, the creak of a platform]
    "Marta runs the seed-sifting workshop with the suspended energy of someone who refuses to be clinical about hope. Her gloves are caked in soil. Around her, children cup seeds in small palms; elders talk about the soil that used to be where the Beacon now stands."
    show marta_chen at left:
        zoom 0.7

    marta_chen "You keep your hands in the dirt long enough and the town tells you what it'll take."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "What if the town isn't the same town next spring?"
    "Marta slams the sieve down with the force of someone naming the fear aloud."

    marta_chen "Then we'll plant anyway. Things remember how to grow. People, less so. You have to teach them both."
    "A woman you recognize nods hard—her porch lost two steps to the surge—and someone coughs, the sound brittle. The gardens are a defiant patchwork, and your ledger feels both necessary and absurd next to the seed trays."
    "You and Marta trade practical counsel: raised beds that flex with tide, salt-tolerant cultivar lists, who can supply oyster spat. Your fingers smell of brine and peat. Teaching these designs is like stitching a map on a living body."
    "Noah Reyes arrives carrying paper cups of coffee he somehow keeps warm. He hands you one without asking, and the warmth of the cup goes straight to your palm."
    show noah_reyes at center:
        zoom 0.7

    noah_reyes "You look like you haven't slept."

    asha_moreno "I haven't. The ledger's late-night drafts are gettering into yesterday's torn maps."

    noah_reyes "You call that 'gettering' now?"

    asha_moreno "It's the only word that doesn't sound like failure."
    "He watches you, eyes earnest, and there's an ache in the way he studies your face—part worry, part calculation. He leans closer, voice softer."

    noah_reyes "People are showing up. Marta's right. They're not all voters and meetings; they're hands. We can do the planning. We just... can't promise permanence."
    "You meet his gaze and find a steady current to rest against. The coffee in your hand is hot enough to sting; it centers you."

    menu:
        "Lead a quick demo on building a floating planter":
            "You squat, showing the tying pattern for buoyant supports. A cluster of neighbors follows your hands. Your voice finds a teaching cadence—firm, patient. You see comprehension spark and it steadies you."
        "Sit and listen to people's stories instead":
            "You lower yourself to the edge and let the stories come in. A woman remembers the smell of the old fishhouse; a man hums a sea chanty. The listening tightens your resolve in a different way—you collect memory as material."

    # --- merge ---
    "Scene continues"
    # [Scene: Tidewatch Lab | Early Afternoon]
    hide marta_chen
    hide asha_moreno
    hide noah_reyes

    scene bg ch13_5ceb3d_3 at full_bg
    # play music "music_placeholder"  # [Music: Staccato strings; pulsing synth under tension]
    # play sound "sfx_placeholder"  # [Sound: Computers pinging, a soft intercom announcement, rain beginning again outside]
    "You are scheduled to teach a short class: living shorelines—practical, no-nonsense. The lab smells faintly of ozone and paper. Your compass is heavy at your throat, a relic and an accusation both."
    "You step up in front of a bank of screens. Students—neighbors, an undergraduate, Caleb from Lila's team—lean forward. You talk about marsh wrack trapping sediment, about graded riprap and root mass. Your voice is clear; the technical parts are a refuge."
    show asha_moreno at left:
        zoom 0.7

    asha_moreno "If we design for accretion, we buy time. If we buy time with people in mind, we don't just hold property—we hold community."
    "Caleb raises his hand; he looks torn, like someone trying to hide contraband. You catch his glance and he looks away."
    show caleb_osei at right:
        zoom 0.7

    caleb_osei "Asha, Lila asked me to extend an invitation. She's arranged a scaled support package. It would focus construction on the worst-hit strips first, combine engineered berms with sensor nodes. It could accelerate work—"
    "Before he finishes, the lab door opens and Lila Park enters. She's all cool angles and soft determination. Sensors on her cuff blink politely; her boots are clean."
    show lila_park at center:
        zoom 0.7

    lila_park "You're teaching well. Practical work matters."

    asha_moreno "Thanks. I try to keep it grounded."

    lila_park "After what happened, we've adjusted our approach. We can remove some of the conditions we proposed—make the assistance more immediate. But the revised model ties maintenance to our hardware network. It's how we ensure performance."
    "Her words are careful, a negotiation wrapped in kindness. The room tightens. Mayor Rosa is there—eyes steady, hands folded. She looks at you as if asking you to count the cost out loud."
    hide asha_moreno
    show mayor_rosa_alvarez at left:
        zoom 0.7

    mayor_rosa_alvarez "What do you mean 'ties maintenance'?"

    lila_park "We'll provide crews, supplies, sensor arrays. In exchange, the consortium retains rights to manage the network and the data to enforce maintenance standards. We'll offer resident interfaces at public terminals. It's efficient. It prevents negligence."
    "Your chest constricts. The word 'rights' slides under your skin—legalese that tastes like fences."
    hide caleb_osei
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "Efficient on whose terms? Who decides neglect, Lila?"

    lila_park "Standards are objective. We won't penalize people. We will ensure that systems that protect lives stay functional."
    "Your voice has started to rise—not theatrical, but edged, the way wind sharpens leftover sails. Caleb watches you, jaw tight. Noah moves to stand behind you, a quiet column of support."
    hide lila_park
    show noah_reyes at center:
        zoom 0.7

    noah_reyes "There's a difference between 'ensuring function' and ceding governance. The community needs seats at the table that can't be overridden by a corporate algorithm."
    hide mayor_rosa_alvarez
    show lila_park at left:
        zoom 0.7

    lila_park "You need a partner who can scale. You can't litigate every tidal event. We provide scale."
    hide asha_moreno
    show mayor_rosa_alvarez at right:
        zoom 0.7

    mayor_rosa_alvarez "We need guarantees that residents can contest decisions, that data isn't under unilateral control. Is that negotiable?"

    lila_park "We can include oversight nodes and external audits. But absolute vetoes or open data without protection could expose residents to exploitation. The company bears legal risk too."
    "The air is taut—threads of fear, of necessary expedience, of things that look like rescue but are edged with contracts. You feel the familiar guilt-prickle—every concession you've made, every sleep you've stolen to draft one more clause. You taste it: metallic and salting other flavors into bitter."
    hide noah_reyes
    show asha_moreno at center:
        zoom 0.7

    asha_moreno "We asked for partnership that doesn't rewrite who we are. We asked for a model that preserves community governance. If the audit terms are only performative, then we've traded safety for the slow privatization of the shore."

    lila_park "You know the stakes. If we delay, more of this town goes under. I'm not asking you to love corporate forms. I'm asking you to accept help that secures lives."
    "Your throat tightens around both sentences—help and caveat—like a tide pulling from two sides."
    hide lila_park
    show caleb_osei at left:
        zoom 0.7

    caleb_osei "She… I think she means it. But some of us in the team are worried about the default clauses. They don't account for edge cases—like informal tenants, community-built berms. It's messy. Real people get excluded."

    asha_moreno "Messy is our town. The mess is the point."
    "Mayor Rosa looks at you, then at Lila, then back. The governance model she's been pushing for—phased seats, refugee support—feels fragile under the weight of machine-logics and investor timetables."

    mayor_rosa_alvarez "I'll press for resident seats in the governance board. I'll push for public terminals, legal safeguards. But I can't promise you'll get every clause you want."

    asha_moreno "Promise me you won't let 'can't' be an excuse."

    mayor_rosa_alvarez "I won't."
    "The words hang. The lab hums like a held breath. Outside, rain picks up, drumming on the lab's roof like a metronome counting decisions."
    "Your instincts want to tear apart the contract in the room and rebuild it with nails and shared coffee. Your practical brain begins to list immediate mitigations—drafts for municipal code language, clauses that bind the company"
    "to community arbitrators, escrowed funds for upkeep. The adrenaline is hot in your veins. You feel both small and enormous."
    hide mayor_rosa_alvarez
    show noah_reyes at right:
        zoom 0.7

    noah_reyes "Whatever happens, we'll keep the audits open. We'll keep the community watch. We'll hold them to their word."
    hide asha_moreno
    show lila_park at center:
        zoom 0.7

    lila_park "Transparency includes terminals and log access. But full, unfiltered datasets could be misused. We'll agree to oversight, within reason."
    "You look at Caleb—his hands fidgeting, his loyalty stretched—and you think of the boatyard, of names carved into wood, of Marta's seed trays and hands in the mud. The choices ahead look like cliffs with ladders made of legalese."

    menu:
        "Call Lila out on the 'within reason' clause publicly":
            "You raise your voice, laying out the danger in precise terms. The room shifts; some faces tighten and others look grateful. Lila's smile cools—she answers with policy-speak. The exchange sharpens lines but also forces specifics onto the table."
        "Ask for technical specifics and propose a neutral third-party arbitrator":
            "You push for concrete mechanisms: named auditors, time-bound clauses, an independent arbiter. The conversation recalibrates to detail. Lila nods slowly; the mayor scribbles notes. The immediate tension recalculates into a checklist of next steps."

    # --- merge ---
    "Scene continues"
    # [Scene: Marabel Promenade | Dusk]
    hide caleb_osei
    hide noah_reyes
    hide lila_park

    scene bg ch13_5ceb3d_4 at full_bg
    # play music "music_placeholder"  # [Music: A rising string motif—urgent, keening; percussion like a heartbeat]
    # play sound "sfx_placeholder"  # [Sound: A loud gull cry, distant hammering, the soft conversation of neighbors]
    "You and Noah walk the boards without speaking for a while. The town is moving—somebody is hauling a tarp, a child is playing with a sodden kite—but each step is a small act of rebuilding. You carry the weight of the lab's conversation bruising your ribs."
    show noah_reyes at left:
        zoom 0.7

    noah_reyes "You taught well today."
    show asha_moreno at right:
        zoom 0.7

    asha_moreno "I taught hard things. The room asked harder ones."
    "He stops and turns to you. In his eyes there's a pressure, something like fear shaped into determination."

    noah_reyes "We have to keep tightening the safeguards. If they bend the rules, we stand them up—legal action, public pressure. I know you think time is for plans, but it's also for teeth."
    "You consider his metaphor and find it accurate and slightly terrifying. Teeth are good, but they also wear down."

    asha_moreno "I keep thinking about the ledger. About the lists of concessions. About which names get carved in wood and which get written into contracts that people forget to read."

    noah_reyes "We read them out loud. We teach people to read them. You teach. I… I'll organize the readings."

    asha_moreno "You always make it sound simple."

    noah_reyes "I like lists."
    "The conversation softens—another tiny harbor. You take his hand without planning it. His fingers are warm; they fit the old shape your palm makes when it is trying not to clutch the compass like a talisman."

    asha_moreno "I'm afraid. Not of storms—they're honest. I'm afraid of slow things that whisper 'efficient' and slide under the porch while people are asleep."

    noah_reyes "Then we whisper back,' he says. 'Louder."
    "The sky darkens; gulls cross the thin light. You feel the pressure building again—not an immediate wave, but a gathering: legal folders to write, public terminals to set up, citizens to train, a company to bind."
    "The to-do list crowds the sacred spaces in your chest and will not be satisfied with a single night of sleep."
    "You pull the compass out and let it rest in your palm. The metal is cool, its glass fogged with your breath. You trace the needle with an index finger. Each scratch is a small map."
    "Your guilt has softened—no longer a hot brand but a sore that aches with memory. It dissolves into resolve, a different acid that eats away at hesitation. Not all compromise is betrayal; not all concession is"
    "salvation. The work you must do now will be legal drafts and wet boots and neighborhood meetings that sometimes end in anger and sometimes end in tea. The arousal inside you—a coiled, urgent energy—tightens into motion."
    "You think of Eli's hull and Marta's seed trays, of Caleb's nervous honesty and Lila's rehearsed kindness. The town is not pristine, and it's not defeated. It is bruised and organizing. The trellis of the future"
    "is being tied together, knot by knot, in meetings and mud and the quiet exchange of hands."
    "You lift your chin against the wind. The Beacon's halo glows across the water like a lighthouse that can't decide whether to warn or invite. Tomorrow will demand audits and town hall schedules and a list"
    "of legal amendments to draft. You will make calls, write clauses, and teach neighbors to understand sensors as well as they understand tides."
    "The chest-tightening builds into an electric pulse. You taste salt and coffee and the metallic aftertaste of compromise. The arousal climbs—plans that used to be diagrams have become living things that need feeding. Urgency is not"
    "panic; it's a sustained march. You feel it in every muscle as you and Noah walk back toward the boats and the beds and the lab."
    "Page-turning thought: The ledger is not just a list of what we saved and what we lost. It's a living document that will be used to name obligations and to map failures. Tonight you rewrite the"
    "first of many entries and tape the page into a binder marked 'Community Governance'—a small, defiant act that will matter when the clauses are argued. You breathe and feel the swell of the work ahead: legal"
    "fights, public audits, seed-sifting, carved names, and the slow accretion of mud that might one day become new shore."
    hide noah_reyes
    hide asha_moreno

    scene bg ch13_5ceb3d_5 at full_bg
    # play music "music_placeholder"  # [Music: Strings peak into a dissonant cluster, then hold]
    # play sound "sfx_placeholder"  # [Sound: The gull cries once, long and raw; then silence]

    scene bg ch13_5ceb3d_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter27
    return
