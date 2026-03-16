label chapter11:

    # [Scene: Greenwave Pilot Site | Late Afternoon — Storm-cleared]

    scene bg ch11_e67f19_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant surf, the low clank of buoys, volunteers calling to each other. A camera phone's soft shutter beeps intermittently.]
    # play music "music_placeholder"  # [Music: Sparse piano with low, weathered strings; an anxious undercurrent.]
    "You walk the narrow plank path between planters, boots slapping on salt-dark wood. The air tastes of iron and seaweed; every inhale brings the thin, sharp smell of wet rope and ozone. Fingers brush a kelp frond and it yields, slick and cool, like a living ribbon."
    "It had looked so small on paper — a lattice of floats, a few dozen planters, a handful of volunteers and a stubborn optimism. Up close, the system hums with life: tiny crustaceans hiding under leaves,"
    "minute larvae clinging to ribs of new growth, a shimmer of juvenile fish finding refuge. The data had started to sing in the lab logs these last weeks. It felt, for a breath, like being right."
    "Then the storm arrived late, a fast-lipped, hungry thing. You remember the sound first: a sudden roar in the rigging, planks arguing against wind. You remember the way the scaffolding shuddered, the snap of a tether,"
    "the sickening slide of a planter lifting and flipping free, tossing soil into the gray."
    "No one was hurt. That is a small mercy you repeat to yourself like a prayer."
    show ivy_morales at left:
        zoom 0.7

    ivy_morales "We got to the loose ones quick. Lina grabbed footage — everyone's fine, but —"
    "She stops, wordless, hands splayed with the kind of helplessness you both know too well."
    "You reach instinctively for the compass at your throat and close your hand around its cool brass. It sits there scuffed and private, an anchor no storm will entirely unmoor."
    show lina_park at right:
        zoom 0.7

    lina_park "The clip's... it's out. Ten thousand views and climbing. Someone's already asking why we ran this 'experimental' pilot without proper safeguards."
    "You feel the words like weather hitting a face. They bruise. You had been trying to thread hope through risk; the town has a low tolerance for experiments that look like mistakes. The footage angles the truth into a question: were we ready?"

    menu:
        "Rush to secure the remaining planters":
            "You move along the scaffolding, hands working knots with a practiced clarity. Your motions steady others; Ivy follows with a coil of spare line. You feel useful and terrified in the same breath."
        "Stand back and document—let Lina record everything":
            "You hand Lina your spare glove and meet her eyes. Holding a camera, she looks braver than she feels. The footage will be honest and blunt; you bristle at the exposure but know the truth needs a frame."

    # --- merge ---
    "..."

    ivy_morales "No one's blaming anyone here yet. But the angle people will take—"
    "You cut in because the space between the two of you can't hold the weight otherwise."
    show marin_sato at center:
        zoom 0.7

    marin_sato "We salvage what we can, then we'll figure out communications. We don't hide. We fix. We explain."

    ivy_morales "That's the problem—'we explain' doesn't stop someone from selling a narrative that we'd been irresponsible."

    lina_park "And 'we fix' doesn't stop an investor from seeing risk, Marin. Tideguard's been watching. They'll either see an opportunity or a liability."
    "You hear Tideguard in her tone like a roll call. Curiosity has teeth; every external eye is both a potential partner and a lever that could change everything about how Havenport keeps its shore."
    hide ivy_morales
    hide lina_park
    hide marin_sato

    scene bg ch11_e67f19_2 at full_bg
    # [Scene: Coastal Research Hub — Cool-lit Lab | Early Evening]

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low HVAC hum, the soft tap of keyboards, a distant foghorn pressed thin by evening.]
    # play music "music_placeholder"  # [Music: Low cello and brittle high strings — tension that won't resolve.]
    "You enter carrying salt in your hair, the smell of kelp still clinging to the cuffs of your jacket. The lab feels clinical after the garden's loam—cool light that flattens faces and data that wants to be neat when everything it describes refuses to be tidy."
    "Ariana Voss is already there. Her hair is damp, a few strands flattened against her temple; her raincoat has a streak of mud near the hem. She stands by the observation window, palms pressed together, like"
    "someone holding a small animal that might bolt. When she sees you, her mouth opens and closes once. There is so much that is unreadable in her look — yes, encouragement, but threaded with accusation; yes,"
    "hope, braided with sharp fear."
    show ariana_voss at left:
        zoom 0.7

    ariana_voss "The footage is honest. We didn't hide the damage. That should count for something, Marin."
    "You look at the screen showing the viral clip, the comments spooling below like a tide of hot, brittle words: 'reckless,' 'experiment gone wrong,' 'who's watching the town?' Your chest tightens. You taste metal."
    show marin_sato at right:
        zoom 0.7

    marin_sato "It counts. But so does optics. So does funding. So does the fact that if we pause now, Tideguard might walk."

    ariana_voss "And if we don't? If we jump because their check is big enough, what then? We become what we swore not to be—falling back on the same top-down fixes that erased the harbor's communities."
    "You can see her balancing the calculus physically: hands clenched, jaw working. It mirrors the choice lodged like a splinter at the base of your throat."
    show ivy_morales at center:
        zoom 0.7

    ivy_morales "We have the data. Early results are promising. Recruitment of juvenile fish—it's measurable. But our structural tests are limited. We didn't simulate that gust pattern."
    hide ariana_voss
    show lina_park at left:
        zoom 0.7

    lina_park "And the public will ask if the trial was rushed. They'll ask why safeguards failed. They'll demand accountability. If Tideguard steps in now with strings attached, they set the timeline."
    "The lab door opens. The air brings a different authority: polished, measured, and a notch too clinical for your taste. A representative from Tideguard steps in — not Cassian Rhee yet, but a neutral-faced liaison in"
    "a corporate shell. They carry the quiet of people who know how to make offers sound like inevitability."

    "Tideguard Liaison" "We saw the clip. Terrible luck, but the underlying metrics are compelling. We should talk about conditional scaling. Fast-track funding, if you accept certain operational standards."
    "The name 'conditional' hangs between you like a fulcrum."
    "You feel the room tilt. Ariana Voss's eyes flash with the same electricity you remember from when she sold Lina on a framing piece a few chapters back—hope threaded with the sort of impatience that sometimes"
    "blinds. This is the moment when an ideal becomes policy, and policy becomes a choice about who wins and who is asked to move."
    hide marin_sato
    show ariana_voss at right:
        zoom 0.7

    ariana_voss "They could help us expand quickly. We could get more nurseries, more planters—more resilience."
    "Marin Sato: (you pause, deliberately) 'Or we could be handed a blueprint that prioritizes scale over consent. Their 'operational standards' might bypass community governance.'"

    ariana_voss "We can negotiate those standards. We can make sure community oversight remains. We can insist on local jobs and on retaining control of maintenance."
    hide ivy_morales
    show marin_sato at center:
        zoom 0.7

    marin_sato "And if they say no? If their conditional funding requires a board seat and veto rights on community decisions? What do we do then?"

    ariana_voss "We make them listen. We make them commit."
    hide lina_park
    show ivy_morales at left:
        zoom 0.7

    ivy_morales "That's easier in a dream, Ari. In practice, a cheque can be louder than a town meeting."
    hide ariana_voss
    show lina_park at right:
        zoom 0.7

    lina_park "And the press? They'll say you were reckless to prioritize ideals over protection if another planter goes. Or they'll say you sold out. Either way, this viral clip has changed the bargaining table."
    "A silence slides over the group like a low tide pulling back to reveal the bent, exposed seabed of consequences."

    menu:
        "Confront the Tideguard liaison directly":
            "You step forward, slow and exacting. Your questions are pointed; you press for the stringency of any 'conditional' terms. The liaison answers with practiced openness, but you can smell the rehearsal."
        "Stay measured and call for an internal review first":
            "You fold your hands and urge process: full data review, a town consultation schedule, structural re-tests. It calms some—buys time—but you feel momentum slip like sand through fingers."
        "Turn to Ariana, ask her what she truly wants":
            "You put the decision's human face back where it belongs. Ariana's eyes catch on yours; she breathes. For a second, the politics drop away and you face a person, not a policy."

    # --- merge ---
    "..."
    hide marin_sato
    show ariana_voss at center:
        zoom 0.7

    ariana_voss "Marin, I—"
    "She stops, as though the words might break the thin shell of something she needs."

    ariana_voss "Please, Marin. Tell me what you think we should do."
    hide ivy_morales
    show marin_sato at left:
        zoom 0.7

    marin_sato "I know. So do I."
    "The compass in your palm feels more insistent than the voice telling you what to do. The brass has the worn authority of decisions you've made and the ghost of those you wish you'd unmade. You"
    "press it; the metal edges bite into skin. It grounds you in the small, human fact of your body amid all the swirling systems."
    "Cassian Rhee's name flickers on one of the monitors as an incoming call — not a presence yet, but a threat and an opportunity both. The town waits in the message threads you can hear like distant gulls: volunteers, elders, reporters, the many slow-moving engines of consent and outrage."

    ariana_voss "Please, Marin. Tell me what you think we should do."
    "You feel the room tilting toward fracture: accelerate and risk ethical blind spots, slow and risk funding evaporating, or rip everything open with public transparency and risk killing the project in its infancy. Each path will leave seams in the town’s fabric — some hidden, some ragged and visible."
    "You inhale. The lab smell sharpens: ozone, coffee gone cold, the faint salt trace that refuses to be washed from your clothes. The compass turns in your hand, a simple circle you cannot escape."
    hide lina_park
    hide ariana_voss
    hide marin_sato

    scene bg ch11_e67f19_4 at full_bg
    # play music "music_placeholder"  # [Music: Strings tighten into a single held note; no resolution.]
    "You stand at the hinge of the next season for Havenport, feeling, as always, the pull between duty and affection, between the small truths you can hold and the large forces that reshape lives. The decision will not feel clean. It will not let you walk away unchanged."
    "Page-turn."

    menu:
        "Scale now; we accept conditional funding and fast-track build.":
            jump chapter12
        "Insist on slower community consent and scientific trials.":
            jump chapter15
        "Release all data publicly and pause the pilot.":
            jump chapter12
    return
