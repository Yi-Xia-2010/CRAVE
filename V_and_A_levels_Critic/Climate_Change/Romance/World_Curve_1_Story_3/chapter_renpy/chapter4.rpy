label chapter4:

    # [Scene: Council Negotiation Room | Late Morning]

    scene bg ch4_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of the HVAC, the soft hiss of a coffee machine beyond a service door; a distant gull cuts the air like a sharp note]
    # play music "music_placeholder"  # [Music: Tense, driving strings underscored by a fast heartbeat-like percussion (building)]
    "You walk in with the salt and soil still in your hair and on your fingers — proof of the mornings you trade for meetings like this. You remember Captain Reyes’ words from the atrium as if they were another rhythm in your steps: listen. Keep that memory."
    "The room smells faintly of machine oil and coffee, the municipal blend: efficient, slightly bitter. The air is cool; the sunlight through the atrium glass is a thin, clinical gold that makes everyone look like actors rehearsing for a civic miracle."
    "You set your satchel down and let your hands steady on the table. Inside, the paper and tag tangles are small anchors: Dr. Sora Kim’s sedimentation graphs, Captain Reyes’s leather-bound logbooks, a handful of seed tags with faded handwriting. You keep them visible. Proof matters here like bones."
    "Irene Vale watches you with the same controlled attention she has for everything that might become a metric. Her platinum bob bobs once as if to a private metronome; when she nods it reads as almost-kind,"
    "practiced to persuade. Mayor Lionel sits to her side, shoulders a little rounded, hopeful and tired in the same breath."
    show irene_vale at left:
        zoom 0.7

    irene_vale "Maya, thank you for coming. I don't want this to be theater. I want something that works."
    show maya_alvarez at right:
        zoom 0.7

    maya_alvarez "Then let's make the theater into policy. Enforceable marsh buffers. Community employment quotas for restoration. A phased approach — and names on the plans for the boardwalk stalls, not just pixel renderings."
    hide irene_vale
    hide maya_alvarez

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Fingers tapping a rhythm on laminated tabletop]
    "Irene Vale's hand taps a pen as she responds. There is a trace of impatience behind her polish, but her voice is measured."
    show irene_vale at left:
        zoom 0.7

    irene_vale "Buffers are expensive and slow. Developers want certainty. Apprenticeship funds — I can see that being politically sellable. Phasing is reasonable, but marsh set-asides would need to be partial at first."
    "You feel the heat behind your ribs — not anger so much as the pressure of people who have no spare mornings to spend waiting for perfect solutions. Your pulse quickens; the room’s air seems to shrink."
    show maya_alvarez at right:
        zoom 0.7

    maya_alvarez "Partial, conditional, but binding. Milestones tied to measurable sedimentation thresholds, not just promise language. If you want the boardwalk to be safe and the marsh healthy, you need legal protections we can stand in front of."
    "Dr. Sora Kim leans in across the table, spectacles catching the light. She spreads a set of graphs that look like tidal fingerprints — lines climbing and falling, annotations in her neat hand."
    show dr_sora_kim at center:
        zoom 0.7

    dr_sora_kim "These are the models. Site A shows accretion under managed restoration if buffer widths meet this profile. We can bind phases to those thresholds legally. It’s not ideal, but it’s defensible."
    hide irene_vale
    show mayor_lionel_park at left:
        zoom 0.7

    mayor_lionel_park "We need jobs, Maya. If we can say 'apprenticeships' and 'restoration employment' — people will vote for the money that keeps roofs over heads."

    maya_alvarez "Then we make those apprenticeships real. Local hires first. Wage guarantees. And we put Captain Reyes’s logbooks into the appendix — lived history comparable to any survey."
    hide maya_alvarez
    hide dr_sora_kim
    hide mayor_lionel_park

    scene bg ch4_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft creak of a chair as he shifts forward; a pipe tapped once against the table]
    show captain_reyes at left:
        zoom 0.7

    captain_reyes "You put my words in paper, then people can’t forget. We remember what the tides used to be, and I will stand and tell it. Don't make it pretty words, make it truth."
    "Irene Vale takes in the logbook, the graphs, the seed tags. For a moment, you read her as someone weighing risk and appearance. Then she exhales, the tiniest crack in the practiced armor."
    show irene_vale at right:
        zoom 0.7

    irene_vale "Partial set-asides. A conditional pledge: if restoration milestones are met, we expand the protections and increase funding. An apprenticeship fund tied to the project's first phase. We'll write specific clauses for cultural markers — the stalls, the vendors' placements. Is that acceptable as a start?"
    "Your chest tightens and then loosens a fraction; relief is a sudden, sharp brightness. It is not everything, but it is a structure you can work from, with teeth and timelines. These are real nails to hang real work on."
    show maya_alvarez at center:
        zoom 0.7

    maya_alvarez "We’ll take that as an opening. We hold you to the thresholds. We get enforcement language and a community oversight clause. And we set public reporting days — transparent metrics the town can read."

    irene_vale "Transparency. Public oversight. Agreed, conditionally. I want to see the early wins before committing more."
    # play music "music_placeholder"  # [Music: Strings swell — hopeful yet taut; percussion accelerates]
    # play sound "sfx_placeholder"  # [Sound: A door opens gently at the back of the room]
    "The door to the negotiation room shifts, and a figure appears with the casual authority of someone who is used to doing things with his hands. Evan Kaito stands in the doorway with a compact desalination"
    "prototype — grey metal, solar strip along the top, the smell of warm rubber and seawater clinging to it. He looks like he has been up early and late, and the dirt under his nails is"
    "the kind of honesty that doesn't need speeches."
    "He steps forward, placing the module on your side of the table like an offering. Your fingers reach to brace it; his fingers brush yours as he locks a latch into place. It's a fraction of"
    "a second — nothing and everything — and his grey-blue eyes unfurl with something like pride."

    menu:
        "Smile and thank him":
            "You let a brief, warm smile break. It's small and honest; Evan Kaito's shoulders loosen and he stays a beat longer as if listening for permission to stay."
        "Keep your face steady and nod":
            "You fold the feeling into your composure and give a concise nod. Evan Kaito's jaw tightens, respect in his eyes, the moment compressed into shared resolve."

    # --- merge ---
    "Continue main narrative."
    hide captain_reyes
    show evan_kaito at left:
        zoom 0.7

    evan_kaito "Prototype's on a two-week test, powered for low maintenance. I can run early data with Sora."

    maya_alvarez "Good. We’ll need those early metrics in writing — public reports, like we said."

    evan_kaito "I'll make them readable. For people who don't live in charts."
    "Your conversation with Evan Kaito isn't long; you both know the day has other demands. Yet even the small friction between your manner and his says more than politeness: there's a history of mutual rescue in practical things."
    hide irene_vale
    show dr_sora_kim at right:
        zoom 0.7

    dr_sora_kim "If Evan Kaito's module runs, we can include operational data in the milestone calculations. That nudges the conditional pledge from possible to probable."
    "Irene Vale studies the module, then looks at you. There is a calculation in her eyes you cannot unmake — politician weighing risk and optics. For the first time, you feel something like a bridge form: measurement, craft, memory, and politics hooked together."
    hide maya_alvarez
    show irene_vale at center:
        zoom 0.7

    irene_vale "Fine. We draft the conditional pledge with milestone language, public reporting, and an apprenticeship fund. You will have oversight seats for the first two phases. We will not bulldoze cultural markers in Phase One."
    # play sound "sfx_placeholder"  # [Sound: A collective exhale around the table, like wind leaving a room]
    # play music "music_placeholder"  # [Music: A high, bright chord, urgent but hopeful]
    "Your relief is immediate and electric; people around the table shift as if freed to stand up straighter. But the high arousal of the morning rides with it — there is work to be done, signatures"
    "to translate into enforcement, community meetings to explain what 'conditional' means to someone whose living room is the ground in question."
    "You feel the barometer at your throat — copper cold and steady — and you touch it as a small ritual: keep the rhythm. You look at Irene Vale again. She looks tired, sharpened, and for a fraction of a second almost vulnerable."
    hide evan_kaito
    show maya_alvarez at left:
        zoom 0.7

    maya_alvarez "We walk this in public. Every step. If you renege, we will make the town know why."

    irene_vale "That seems appropriate. Hold me to it, Ms. Alvarez. Let’s get the language down."

    menu:
        "Ask for immediate public signoff":
            "You push for a quick public commitment. Irene Vale glances to Mayor Lionel, who nods slowly; it might force her hand, and it might put you in front of a crowd before you're ready."
        "Insist on draft language first":
            "You keep the approach cautious — draft language first, then public hearings. Irene Vale hums agreement; the pace slows to careful drafting, but you worry that it gives time for backtracking."

    # --- merge ---
    "Continue main narrative."
    hide dr_sora_kim
    show mayor_lionel_park at right:
        zoom 0.7

    mayor_lionel_park "If this keeps us together, let's get terms on the table. People need to know there’s a plan."
    "You gather your proofs, shaking slightly from adrenaline. You feel the high, driving energy of the morning — the urgency to convert words into deeds before weather or wallets shift. The partial set-aside, the apprenticeship fund, public oversight: a scaffold you can climb."
    "Dr. Sora Kim presses a printout into your hand — a simplified timeline annotated in her tight script. Captain Reyes offers a small, almost imperceptible nod. Evan Kaito's fingers brush yours again as he steps back"
    "toward the doorway; his expression is complex and unreadable in a way that keeps both of you safe from assumptions."
    hide irene_vale
    hide maya_alvarez
    hide mayor_lionel_park

    scene bg ch4_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hum of the building returns, lower but steadier; beyond the doors, the sea pounds distant and insistent]
    # play music "music_placeholder"  # [Music: Percussion recedes into a steady, hopeful rhythm; strings sustain a bright note]
    "You leave the room with a conditional pledge in hand and a list of immediate tasks forming like a tide line: draft language, public reporting framework, apprenticeship outlines, enforcement clauses. The victory is not total, but it is concrete — the kind you can build on."
    "You walk past the atrium's glass. Outside, the boardwalk is a ribbon of people and tents and tarps — life continuing in the low sun. You tuck the seed tags back into your satchel. The air tastes of salt and coffee and something like possibility."
    # [Scene: Verdant Rooftop Nursery | Early Afternoon]

    scene bg ch4_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The gentle drip of water into planters; distant laughter from volunteers]
    # play music "music_placeholder"  # [Music: Light piano motifs, hopeful and brisk]
    "You climb to the nursery to meet Evan Kaito properly. Between petty paperwork and municipal language you need the thin, resilient green of living proof. The rooftop smells of wet soil, thyme, and old boards. Volunteers bend to beds; Tala Ruiz waves you over with a grin."
    show tala_ruiz at left:
        zoom 0.7

    tala_ruiz "Look at these seedlings. People are showing up to learn in droves. We needed something real to believe in."
    show maya_alvarez at right:
        zoom 0.7

    maya_alvarez "They'll get real work. And apprenticeships. We just got conditional pledges. It's a start."
    show evan_kaito at center:
        zoom 0.7

    evan_kaito "Start's good. We'll iterate fast. Two weeks of field tests, then public data."
    "You and Evan Kaito exchange more than sentences — small tactical planning, timelines, the logistics of community trainings. Your voices overlap; the rhythm is efficient, intimate, and full of the quick trust that comes from shared labor."

    menu:
        "Map out immediate volunteer roles":
            "You grab a marker and start sketching shifts on Tala's clipboard. The team breathes into a schedule; things begin to fit into people's lives."
        "Talk strategy with Evan Kaito alone":
            "You ask Evan Kaito to walk the perimeter with you. Private tactics, quieter plans. He nods and you step out onto the edge of the roof together."

    # --- merge ---
    "Continue main narrative."
    # [Scene: Stormcliff Lighthouse | Dusk]
    hide tala_ruiz
    hide maya_alvarez
    hide evan_kaito

    scene bg ch4_453e40_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Waves smashing on the rocks, wind threading through the panes; the lighthouse lamp groans softly as it turns]
    # play music "music_placeholder"  # [Music: A single sustained violin line, urgent but warm]
    "You climb the narrow stairs later, wanting the raw horizon to hold your head. The lamp room is small and the light is thin; the sea sounds like the metronome of a very large clock. You"
    "stand at the window, the town reduced to a collection of shapes, and you trace the lines of the promises you just made into the air."
    "The day’s adrenaline eases into a steady kind of resolve. The conditional pledge is a hinge — not the end of argument, but the beginning of accountability. You feel hope braided with the old ache: you"
    "have traded some rhetorical purity for a legal scaffold, and you are not ashamed. It was the right, urgent move."
    "You hold Dr. Sora Kim’s printout, Captain Reyes’s logbook, Evan Kaito’s prototype notes. A small victory sits in your hands like a hot stone. You know there will be pushback, audits, and pressure from funders and"
    "developers. You also know the town will watch; people will see the apprentices in harnesses, the seedlings taking root. That visibility will matter."
    "You touch the copper barometer at your throat and feel its steady, cool pulse. It is an emblem of weathered things that don't lie. You breathe, and the breath is long and held and ready."
    # play music "music_placeholder"  # [Music: Swell to a high, bright chord — urgency peaks, then resolves with bright expectation]

    scene bg ch4_453e40_7 at full_bg
    "You are determined to hold Irene Vale to this pledge in public. The work to bind words into law will be hard and immediate; you feel the pressure in your shoulders and the fierce, hopeful light behind your ribs. This is a climb you chose."

    scene bg ch4_453e40_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
