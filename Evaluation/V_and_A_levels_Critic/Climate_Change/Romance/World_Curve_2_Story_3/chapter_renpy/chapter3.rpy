label chapter3:

    # [Scene: Skyfield Conservatory | Early Evening]

    scene bg ch3_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmurs like surf; a microphone squeal. Footsteps on wet decking. A distant ambulance tone swallowed by glass.]
    # play music "music_placeholder"  # [Music: String ostinato undercut with a tense electronic pulse]
    "You push through the wet glass door and the greenhouse breathes on you—humid, leaf-sweet, and metallic from the municipal screens. Your scarf is still damp; the coral fiber presses against your throat like the memory that"
    "never lets go. The room smells of soil, hot plastic from display projectors, and cheap coffee left cooling in paper cups."
    "The forum is already a live wire. Rows of faces, some storm-tight with purpose, others raw at the edges. Cameras perch on tripods; Tamiko's camera is low and steady near the back. Lina stands at the"
    "mic—her hands are folded so tight they whiten the knuckles. Elias Moreno is at a cluster of municipal planners, tablet glowing against his chest. Cassian Vale sits to the side, immaculate in his dark coat, a"
    "PR spokesperson smiling a little too hard beside him."
    "You feel the air change as you enter: the conversation has weight now, every sentence a possible hinge."

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A chair scrapes; the mic clicks on]

    "Moderator (off-screen)" "We're opening questions. Please keep them concise."
    show lina_cortez at left:
        zoom 0.7

    lina_cortez "My name is Lina Cortez. I grew up on Wharf Seven. If this fast-track goes through, my uncle—he's lived there thirty years—will be priced out. They tell me there's 're-housing' money. What does that mean when rents skyrocket and people who know how to patch a house are told to leave?"
    "You watch the room tilt, a dozen sympathetic faces pivoting like weather vanes. Someone near the front starts clapping; others begin to shout past the applause. You feel a hot pressure behind your ribs—anger that tastes like salt."
    "Elias Moreno moves forward before you can. He palms his tablet, voice measured, practiced."
    show elias_moreno at right:
        zoom 0.7

    elias_moreno "We hear you, Lina. The phased plan includes targeted protection and a relocation fund. We're prioritizing—"
    "Tamiko's camera clicks. Her voice cuts through like a bell."
    show tamiko_sato at center:
        zoom 0.7

    tamiko_sato "Priority for who, Elias? The contract you were handed this week locks in a fast-track clause tied to external funding. We have the draft."
    hide lina_cortez
    hide elias_moreno
    hide tamiko_sato

    scene bg ch3_98c6f2_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A collective intake of breath. The hum of electronics rises.]
    "Dr. Arun stands, shaking his head, fingers pressed to his temple."
    show dr_arun_patel at left:
        zoom 0.7

    dr_arun_patel "The clause...it's a procedural override. It limits local approval windows and ties milestones to tranche releases. Pacing aside, it gives the fund—whoever controls it—leverage to dictate scope."
    "Cassian Vale's PR guy folds his hands and smiles like sunlight on glass."

    "Cassian Vale (calmly)" "Our funding partner is committed to swift action. Delay costs lives. We offer comprehensive re-housing vouchers and preferential access to new units."
    "Tamiko scoffs, voice sharpened."
    show tamiko_sato at right:
        zoom 0.7

    tamiko_sato "Preferential? A voucher doesn't push out speculative rents. You're trading speed for people's homes, Cassian."
    "Cassian Vale's eyes flick to you. The look is precise; there's an unreadable calm there."
    show cassian_vale at center:
        zoom 0.7

    cassian_vale "Ms. Santos, are you suggesting we choose delay over protection? That you prefer risk to your neighbors?"
    "You taste copper in your mouth. The room tightens as if someone compressed air in a bellows. Every side stares; the greenhouse becomes a pressure chamber."

    menu:
        "Step up to the mic, demand to read the clause aloud":
            "You cross the floor, paper in hand, and your voice carries—clear, sharp. The clause feels smaller under the heat of all those eyes."
        "Stay back, let Elias take the lead and prepare rebuttal data":
            "You stand grounded, watching Elias assemble diagrams on his tablet. His jaw is set; you feel your pulse sync with his breath."

    # --- merge ---
    "Scene continues."
    "You can feel your community's history thrumming along the floorboards: the time your neighbor banged on doors to warn everyone during last spring's King Tide; the way hands braided ropes, the nights spent sandbagging until your back ached. History presses against policy right now, and you are the seam."
    "Elias Moreno gestures for calm, scrolling through annotated timelines. His sea-gray eyes meet yours across the crowd—there's something vulnerable there, a fissure you didn't expect."
    hide dr_arun_patel
    show elias_moreno at left:
        zoom 0.7

    elias_moreno "I didn't bring this clause in; my team was briefed late—' (he swallows) '—but we can renegotiate the milestones. We can add community consent triggers."
    "Tamiko leans in. Her voice is low enough that only the two of you can hear."

    tamiko_sato "Renegotiate? They can lock the release of funds to 'completion metrics.' That gives Vale leverage to declare neighborhoods non-compliant when they don't meet aesthetic or densification targets."
    "You watch Elias Moreno's hands. They hover like someone holding a model that could crumble if he breathes wrong."
    "You step forward, choosing your words with the same careful thrift you used patching tarps."
    hide tamiko_sato
    show mira_santos at right:
        zoom 0.7

    mira_santos "If the funding structure makes decisions contingent on their private standards, we don't have real negotiating power. We get boxed in."

    elias_moreno "We can structure clawbacks and binding covenants—legal enforceables that prioritize tenure and affordability. Dr. Arun, your data on ecosystem-based solutions can be framed into performance indicators."
    hide cassian_vale
    show dr_arun_patel at center:
        zoom 0.7

    dr_arun_patel "Performance indicators that count marsh health and accessibility—yes—but legal clauses need teeth. They need penalties for displacement. Otherwise, it's lip service."
    "Cassian Vale interrupts, voice smooth as glass."
    hide elias_moreno
    show cassian_vale at left:
        zoom 0.7

    cassian_vale "This reads like negotiating in the middle of a storm. I appreciate passion, but facts are the keel here. My consortium funds infrastructure at scale. We deliver predictability."
    "Tamiko steps up to the mic and speaks with a ferocity that makes people stop mid-breath."
    hide mira_santos
    show tamiko_sato at right:
        zoom 0.7

    tamiko_sato "Predictability for whom? Your 'predictability' builds walls where our schools and markets are. It privatizes the coastline. We need accountability, not glossy renderings."
    "A man near the back shouts, someone's aunt begins to cry softly, and a municipal planner whispers about emergency timelines. The heat in the room spikes; voices overlap into a rough tide."

    menu:
        "Place a hand on Lina's shoulder to steady her":
            "Her shoulders tremble under your palm; her gratitude is a small, fragile thing. Her story becomes less like a broadcast and more like a tether."
        "Push for a calm micro-community caucus—pull Elias and Tamiko aside now":
            "You ask for a five-minute caucus. People grumble, some cheer. Elias nods, Tamiko's jaw tightens but she follows—privilege of a private conversation in public."

    # --- merge ---
    "Scene continues."
    "You gather Lina at the mic. Her voice is small at first, but the room leans in. Tears catch the light; she spits the words out in half-sobs."
    hide dr_arun_patel
    show lina_cortez at center:
        zoom 0.7

    lina_cortez "My daughter's school—if they move the family, they'll lose the counselors who know them. My neighbor's carpenter—who does he become when polished condos line the shore? You talk about safety like it's just concrete."
    "Elias Moreno closes his eyes for a heartbeat. He swings the tablet to show projected floodplain modeling—lines and probabilities, colors that suggest inevitability."
    hide cassian_vale
    show elias_moreno at left:
        zoom 0.7

    elias_moreno "I am asking for time—time for adaptive, phased intervention that protects most people without waiting for catastrophe. I am not blind to risk. But full paralysis means everyone loses."
    "You respond, because silence here is compliance."
    hide tamiko_sato
    show mira_santos at right:
        zoom 0.7

    mira_santos "Time is a luxury when an investor decides your risk profile. We need written guarantees, not promises. We need binding clauses on tenure, community oversight, and incremental 'no-displacement' checkpoints."
    "Cassian Vale leans forward, tone sharpened."
    hide lina_cortez
    show cassian_vale at center:
        zoom 0.7

    cassian_vale "Binding clauses slow implementation. They invite litigation. Litigation stalls safety. I will not apologize for offering a solution that acts quickly."
    "Tamiko slaps a printout on the podium. The clause on the screen—bold, merciless—reads: expedited approvals, milestone-linked tranche releases, executive override conditions in the event of 'necessary acceleration.'"
    hide elias_moreno
    show tamiko_sato at left:
        zoom 0.7

    tamiko_sato "Listen to the sentence: 'In circumstances where timely delivery is deemed necessary by the Fund, standard public approval processes shall be abridged.' That's a bypass."
    "A ripple of anger crosses the room—hot, animal."
    hide mira_santos
    show dr_arun_patel at right:
        zoom 0.7

    dr_arun_patel "We cannot allow a contingency that sidesteps democratic oversight. The models—' (he taps a graph) '—show that hard infrastructure without social safeguards increases displacement risk by seventy percent in scenarios with speculative pressure."
    "Cassian Vale's PR guy smiles tightly."

    "Cassian Vale (quietly)" "And yet, without infrastructure, the city drowns. That's the trade."
    "Your breath stutters. You feel the old fear—water under threshold, door stuck. This is the same arithmetic, dressed up as progress."
    "Elias Moreno's voice cracks when he speaks next. It's the first fracture you've seen in his public armor."
    hide cassian_vale
    show elias_moreno at center:
        zoom 0.7

    elias_moreno "I—If we don't move now, more people are at risk. If we move in the wrong way, we hurt people in different ways. I'm trying to find a path that reduces overall harm."
    "You want to shout that 'overall' can't erase the people sitting in front of you. You want to tell him his metrics don't write condolence letters. But you also know the confidence in the room could tip into paralysis that kills."
    "Your chest feels raw. Every second that passes makes the room more combustible."
    "A city reporter leans forward, mic outstretched."

    "Reporter" "Ms. Santos, what's your response to the clause? Will you endorse immediate action, or will you oppose it?"
    "All eyes snap to you. The greenhouse sound collapses into a single wire of attention."
    "You hear, beneath the noise, the little ledger in your brain: your grandmother's hands sewing sandbags; the names folded into your pocket; Dr. Arun's quiet presentations that turned science into human stories. The ledger says: protect the people first. The city says: choose a lever and pull."
    "Your throat tightens. This is the hinge. Every face in the room waits for the seam to be sewn—or torn."
    "You can feel your pulse in your ears, a drum rolling toward something unavoidable. The arousal builds: the murmurs harden into shouts, the cameras tilt, Tamiko's fingers drum the grandmother's rhythm on her camera. Elias Moreno's brow creases; Cassian Vale's smile thins."
    "You realize, with a cold clarity, that whatever you choose now will fracture alliances. It will set a path—co-design, public expose, or immediate local resistance—and there is no neutral ground."
    hide tamiko_sato
    hide dr_arun_patel
    hide elias_moreno

    scene bg ch3_98c6f2_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Microphone feedback peels once, then goes dead. The room inhales as one.]
    "You lift your chin. The decision blooms, sharp as broken slate."

    menu:
        "Negotiate with Elias, push for stronger community guarantees in his plan.":
            jump chapter4
        "Publicly confront Cassian and demand a halt; side with Tamiko’s expose approach.":
            jump chapter8
        "Organize direct neighborhood resistance—shoreline defenses and an occupation to buy time.":
            jump chapter12
    return
