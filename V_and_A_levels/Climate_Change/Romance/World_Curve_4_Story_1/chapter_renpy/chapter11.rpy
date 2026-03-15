label chapter11:

    # [Scene: Municipal Hall | Early Evening]

    scene bg ch11_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Percussive strings undercut by a low, insistent drum]
    # play sound "sfx_placeholder"  # [Sound: Muffled voices outside, the creak of a folding chair, the hum of a fluorescent light]
    "You stand in the corridor with the appendix pressed flat against your ribs, the paper a cold, accusing weight. The smell of burnt coffee threads the air; someone has left a paper cup on the radiator,"
    "steam curling like a question mark. Your palms are slick with salt and adrenaline. The choice you held the night before has turned into this: a room full of neighbors, the town’s future suspended on the"
    "edge of your voice."
    show lina_park at left:
        zoom 0.7

    lina_park "They're packed out on the terrace and spilling into the hallway. We have people by the back doors. Mayor's trying to get the order. Maya—are you ready?"

    "Your mouth forms the word before your brain approves it" "Ready."
    "You smooth a corner of the appendix with your thumb. For a second you imagine the northern spit’s glasswort and the mud smoothed by low tide—then you feel the hall's fluorescent glare like frost. The room is about to change everything."
    hide lina_park

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low hum rises into a ripple of voices]
    "Arin appears at your shoulder—quiet, a shadow with that slow, steady gait that used to anchor you. He doesn't look at the papers; he looks at you. There's something raw in his expression, a fear that"
    "sits behind his amber eyes and refuses to soften. You register it like a stitch in your lung."
    show arin_kai at left:
        zoom 0.7

    arin_kai "You sure about bringing this here? We could—' (he stops, chooses) '—we could show them in smaller groups, take it slow."
    "You turn to him. The corridor smells of wet coats and the metallic tang of worry. You want to say that slow will mean buried. You want to say this is the only air you can breathe anymore. But the drumbeat in your ears is louder than your words."
    show maya_soler at right:
        zoom 0.7

    maya_soler "If it's true, it won't stay small for long. People deserve to know who stands to profit while the marsh dies."
    "Arin's jaw tightens. He lifts a hand as if to touch the folder—then lets it fall. His fingers hover near yours and pull back, complicated and unreadable."

    menu:
        "Check Arin's face":
            "You step closer and press the back of your hand against his forearm. He doesn't flinch, but his breath hitsched. For a second the world narrows to the tiny, stubborn warmth of his skin under your palm."
        "Force your stance toward the podium":
            "You straighten, tuck the appendix under an arm, and stride toward the door. Arin falls into step behind you—his shadow at your side, steady but taut."

    # --- merge ---
    "The scene continues into the main chamber."
    # [Scene: Municipal Hall — Main Chamber | Evening]
    hide arin_kai
    hide maya_soler

    scene bg ch11_e67f19_3 at full_bg
    # play music "music_placeholder"  # [Music: A discordant string tremolo syncs with the murmur of the crowd]
    # play sound "sfx_placeholder"  # [Sound: Someone starts a chant in the back; it catches like a spark]
    show mayor_tomas_greer at left:
        zoom 0.7

    mayor_tomas_greer "Let's bring this to order. Maya—when you're ready."
    "You step up to the podium. The microphone is too bright and the room multiplies every inhale. You place the appendix open on the lectern, the title page catching light: appendices, easements, prioritization lists. You do"
    "not read every line; you never meant to. You read what you must: the throughlines that become sentences sharp enough to wound."
    show maya_soler at right:
        zoom 0.7

    maya_soler "These documents show that the proposed seawall plan includes easements negotiated behind closed doors, prioritized investor access to redeveloped lots, and a valuation that—' (you falter, swallow) '—that systematically discounts ecological loss to favor short-term economic returns."
    "The chamber roars a reaction: a mixture of disbelief, anger, and the thin, brittle sound of betrayal. Someone yells, 'That's illegal!' A woman by the door starts crying. The room's air thickens, humid with fear and salt and the bitter tang of betrayal."
    show lina_park at center:
        zoom 0.7

    lina_park "We didn't get here by accident. We did the monitoring—community data. We have recordings, we have land deeds, we have timestamped emails. This is pattern work. This is a plan that sidelines the marsh to make room for profit."
    hide mayor_tomas_greer
    show evelyn_hart at left:
        zoom 0.7

    evelyn_hart "These are complex trade-offs. The region needs protection fast. There are investors ready to fund infrastructure; to call this a conspiracy is to refuse action in the face of immediate risk."
    "You feel enraged and hollow at once. Her words feel like a surgical lamp on the wound of your town's memory: pragmatic, bright, and unforgiving."
    hide maya_soler
    show mayor_tomas_greer at right:
        zoom 0.7

    mayor_tomas_greer "Order! We will let Maya finish. Then we will hear statements. No shouting—civil statements."
    "But civility splinters instantly. A man stands—Noah, maybe, or someone you now know by face and decades of shared shorelines—and shouts, 'Who signed those easements? Who took our marsh and sold it to the highest bidder?'"
    "The chamber surges. People push toward the podium. A volunteer tries to calm them, voice gone thin."
    "You gather the next page—an easement map, blocks of land inked with notes—and point to the margins where investor names have been penciled in."
    hide lina_park
    show maya_soler at center:
        zoom 0.7

    maya_soler "These are the parcels. These are the beneficiaries. The ecological valuations were reduced across the board—treated like line items to be trimmed. That means the models used to justify the seawall ignore millions in natural flood mitigation. They set the numbers so the seawall looks cheaper than protecting the marsh."
    "A heavy silence follows—shock, then a new layer of fear. If the numbers are rigged, then the protection plan buys short-term safety at the cost of long-term collapse."
    # play sound "sfx_placeholder"  # [Sound: A chair scrapes violently; someone curses under their breath]
    "Arin Kai: (to you, then louder) 'You understand what this means for people like my family. If we delay, if we call audits, crews stop, bills pile up. I know you're fighting for the marsh, Maya,"
    "but what about the boats tied up at the harbor? What about the crews who feed their kids now? How do you ask a man to choose between his child's dinner and the long-term models?'"

    maya_soler "You think I don't know that? You think I like this? This—' (you lift the appendix, the paper feels thinner than a promise) '—this isn't a choice between science and people. It's a choice where people were used as leverage."
    hide evelyn_hart
    show arin_kai at left:
        zoom 0.7

    arin_kai "Then tell me what to do. Tell me how to keep the boats and keep the marsh both, because people are scared and hungry and you—' (he stops, lashes out softly) '—you stand here and make them afraid of trumped-up timelines."
    "There is a hush, sharp as a blade. The room waits. Your chest feels like a tidepool: stirred, full of life threatened by a hand that might reach in and pluck it away."
    "You could reach for him. You could tell him that you will not let both die. You could tell him that truth—even if it breaks trust now—is the only thing that might stitch the future back."
    "Instead your words come out thin and iron, because the drum under everything insists on urgency and you can smell the storm coming outside as if it were another participant."

    maya_soler "I don't have a clean answer, Arin. If those contracts are allowed to stand, the town loses bargaining power. If we force an audit—' (you stop as if the room itself inhaled) '—we risk investors pulling funding and immediate protections stalling. But if we hide it, we make the same mistake my family made when the storm took our house: we trusted that someone would do right by the people."
    "Arin's face hardens for a second, then folds. He looks at you—complex, unreadable—the way the Schrödinger tide can be both high and low until you actually observe it."

    menu:
        "Reach out and take Arin's hand":
            "You move across the aisle and take his hand. For a beat there is a soft relief in his fingers clenching yours. The crowd blurs. The world narrows to the warmth and the rough callus of his palm."
        "Step back and address the room":
            "You step back toward the lectern and lift your chin. Your voice steadies, colder, policy-sharp. The room watches as you sharpen the dilemma into options—they listen because it is the only way forward."

    # --- merge ---
    "The presentation continues as Lina displays evidence."
    "Lina cuts in, voice urgent, not waiting for civility. Her hands fly over her tablet and the projector flicks to a slide detailing timelines, investor names, and a summary of ecological losses calculated by community sampling. Each bullet point falls into the chamber like rain on tin."
    hide mayor_tomas_greer
    show lina_park at right:
        zoom 0.7

    lina_park "We can file for immediate records and launch a legal review. We can demand a mediated audit with Evelyn at the table and independent oversight. Or we can expose everything now and force immediate civic intervention."
    hide maya_soler
    show evelyn_hart at center:
        zoom 0.7

    evelyn_hart "Panic will cost lives. You spread this as scandal and infrastructure funding walks. I propose mediation now—transparency without chaos. We can—' (her words land like well-polished stones) '—we can set an audit, ensure oversight, and keep critical work moving."
    "Her offer is a tightrope: it promises safety and business continuity, the pragmatic fix that glints like a coin. But you know every politeness she offers can be polished into delay. Your chest caves inward and the air tastes of iron."
    hide arin_kai
    show mayor_tomas_greer at left:
        zoom 0.7

    mayor_tomas_greer "We need to decide in public. We need a path that protects people. I will call three options to the floor: legal requests and formal channels; a mediated audit with Evelyn present; or full public exposure and immediate civic action. We don't have forever. The bay is changing by the hour."
    "The room surges with noise again—yelling, fists, someone sobbing. Outside, a gust rattles the windows and the first hard drops of rain begin to tap like a heartbeat against the glass. The storm isn't only weather; it's the town's fear made audible."
    "You feel the weight of every story in the room—every lost house, every borrowed engine, every hand that has pulled a net and watched it come back empty. The appendix on the lectern is suddenly not"
    "a folder of data but a ledger of trust: who was counted, who was priced out, who was hidden."
    "Your side of the room is raw and near-riotous; Evelyn's allies are clinical and organized. Lina stands beside you, jaw set so tight you think you can hear her teeth. Arin is somewhere between a man"
    "who would fight for a boat and a man who would stand with you if only he could see the path."
    "You have built to this; everything has led here—the hush of the rooftop the night you organized volunteers, Rita's stories about the old marsh, the late nights turning mud into graphs. Now the chapter ends on a blade, poised to fall."
    hide lina_park
    hide evelyn_hart
    hide mayor_tomas_greer

    scene bg ch11_e67f19_4 at full_bg
    # play music "music_placeholder"  # [Music: Strings snapped into a staccato, a cymbal crash as the room erupts]
    # play sound "sfx_placeholder"  # [Sound: Shouts, a gavel banged on a table somewhere in the back, the roll of thunder like a judge]

    menu:
        "File formal public records requests and pursue legal avenues":
            jump chapter12
        "Negotiate a mediated audit with Evelyn present":
            jump chapter12
        "Go full public with the documents and call for immediate civic intervention":
            jump chapter15
    return
