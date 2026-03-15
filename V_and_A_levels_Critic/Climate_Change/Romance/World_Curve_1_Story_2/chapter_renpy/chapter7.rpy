label chapter7:

    # [Scene: Tidewatch Institute Lab | Afternoon]

    scene bg ch7_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low whir of a centrifuge; distant traffic-siren gulls; the gentle hiss of a printer spitting out pages.]
    # play music "music_placeholder"  # [Music: Steady, mid-tempo piano motif—measured, forward-moving]
    "You start by feeling the choice you made as a small, organized pressure behind your sternum: Option B. You told the room you'd accept Lina's conditional pilot, that you'd lead the municipal study. The decision hangs"
    "now, immediate and procedural, like a new entry in a ledger that will be audited by a hundred voices."
    "Dr. Noor slides another printout across the table to you—model runs with varied sea-level scenarios, color bands that climb with each parameter change. Their expression is complex, unreadable; practiced neutrality with an edge of personal worry you can't quite place."
    show dr_noor_patel at left:
        zoom 0.7

    dr_noor_patel "These are the baseline calibrations. If we pair automated levees with the retrofits you designed, the models show a reduced inundation risk in three of the five high tide scenarios."
    show ari_navarro at right:
        zoom 0.7

    ari_navarro "Three out of five is better than none—' Your voice catches a little on the last word. 'But the assumptions about maintenance funding and real-time controls are optimistic."
    "Lina Moreau stands near the doorway, trench coat beading with drizzle. Her platinum bob is immaculate even under the weather; the amber of her silk collar glows like a promise against the gray. She folds her hands, a picture of municipal inevitability."
    show lina_moreau at center:
        zoom 0.7

    lina_moreau "Our financing assumes mixed funding—municipal bonds, a regional transfer, plus private partnership for construction. Ephraim's firm will expedite permits and handle implementation timelines."
    "Ephraim leans forward, hands clasped, the tan of his suit a warm counterpoint to the lab's cold light. He smells faintly of sunblock and older money."
    hide dr_noor_patel
    show ephraim_blake at left:
        zoom 0.7

    ephraim_blake "Speed matters. We can move within two fiscal quarters. Delay invites risk. Investment now buys lives and property—clearly the right moral and economic calculus."
    "Sora Watanabe's silhouette is a sharper shape in the doorway—paint-splattered jacket half-wet, eyes dark and wide. They step in like a counterpoint to the technical talk, breath still quick from the run up the stairs."
    hide ari_navarro
    show sora_watanabe at right:
        zoom 0.7

    sora_watanabe "So that's it? We hand the town over to the same people who made it a market? You told me you wouldn't sell this place."
    "Maya is beside Sora, hands twisting the hem of her coat. Her face is small and weathered like driftwood; you can see the strain in her jaw as if she's holding back a tide."
    hide lina_moreau
    show maya_cruz at center:
        zoom 0.7

    maya_cruz "Ari—"
    "Ari Navarro [internal]: The word 'sell' lands like salt. You map it against the spreadsheets and the model runs. You think of the sibling you lost to a flood that came faster than the alarms. You think of the work you owe your town: precise, technical, and unforgiving of spectacle."
    hide ephraim_blake
    show ari_navarro at left:
        zoom 0.7

    ari_navarro "This isn't 'handing over.' It's oversight. I'm agreeing to scrutiny, to being the municipal lead on the pilot. The levees are automated, yes, but the retrofits we specify—wetland buffers, foundation lifts—those are community controls. The funding strings are conditional on transparency and a phased handover."
    hide sora_watanabe
    show lina_moreau at right:
        zoom 0.7

    lina_moreau "Your oversight clause is acceptable. We will create an independent monitoring committee. Public dashboards. If we do this together, the governance structure will be clearly defined."
    hide maya_cruz
    show sora_watanabe at center:
        zoom 0.7

    sora_watanabe "Independent monitoring he says—like we've never been left off a committee because our faces made contractors nervous."
    hide ari_navarro
    show ephraim_blake at left:
        zoom 0.7

    ephraim_blake "We welcome community representation. Practicalities matter. We act; we don't just stage protests."
    hide lina_moreau
    show dr_noor_patel at right:
        zoom 0.7

    dr_noor_patel "Practicalities are constrained by budget lines and maintenance forecasts. If the maintenance funds dry up, automated systems fail faster than older, human-run protocols."
    "Ari Navarro leans over the table, fingertips brushing the printout where color bands flare into an ominous orange. The numbers are not abstract; they're maps of possibility and loss."

    menu:
        "Trace Ephraim's funding line in the ledger":
            "You pull up the ledger, fingers skimming inked entries. There are transfers labeled 'infrastructure partnership' and a few vague 'expedite' clauses. Ephraim watches the screen; his smile tightens. Dr. Noor exhales, not audibly approving but not surprised either."
        "Ask Noor to run a conservative maintenance scenario":
            "You ask Dr. Noor for a scenario that assumes minimal maintenance funding. Noor keys it in; the map shifts—the orange spreads. Lina's jaw tightens; she doesn't speak, but her hand flexes at her side. Sora's eyes narrow, a slow, pained calculation crossing their features."

    # --- merge ---
    "The conversation resumes with adjusted assumptions and tightened language around maintenance and oversight."

    dr_noor_patel "Run this in conservative mode. If maintenance falls at fifty percent, the levee control systems need human overrides at regular intervals. That's labor. That requires commit—"
    hide sora_watanabe
    show lina_moreau at center:
        zoom 0.7

    lina_moreau "Which is why the municipal grant includes a labor trust. We are not proposing a purely automated system without human redundancy."
    hide ephraim_blake
    show sora_watanabe at left:
        zoom 0.7

    sora_watanabe "Labor trust on paper and labor trust in practice are different things. How do you enforce it when profit margins are read into every line item?"
    hide dr_noor_patel
    show ephraim_blake at right:
        zoom 0.7

    ephraim_blake "Enforcement via legally binding service contracts. Accountability through regulatory oversight."
    "Ari Navarro [internal]: The word 'accountability' is a soft promise that can be stretched thin. You think of the neighborhoods that will be asked to move, of the fishermen whose boats are livelihoods and identities. Compromise is a calculus; your pen will sign the equation."
    "Maya presses her thumb against her lip, a small ritual when she is about to cry or to speak plainly."
    hide lina_moreau
    show maya_cruz at center:
        zoom 0.7

    maya_cruz "If we do this, will there be funding for the co-op's relocation support? For the wetland plants we grow? You promised—"
    hide sora_watanabe
    show ari_navarro at left:
        zoom 0.7

    ari_navarro "Yes. The pilot includes funds earmarked for community relocation assistance and the wetland restoration program. We'll codify it in the pilot's annex."
    hide ephraim_blake
    show sora_watanabe at right:
        zoom 0.7

    sora_watanabe "That's not the point. The point is you're lending them legitimacy, Ari. Your name will be on the paperwork that lets them call this 'community-led' while they design the exits."
    "Ari Navarro [internal]: Sora's accusation doesn't land like a blow so much as a precise, unavoidable friction. It reveals where your choices will rub against trust. You can rationalize: oversight prevents abuse. You can rationalize: lives saved. Both are true; neither empties the ache."

    menu:
        "Tell Sora you understand their anger":
            "You step closer, lowering your voice. 'I know,' you say. Sora's shoulders drop fractionally, anger folding into something rawer. They don't hug you, but their eyes are less accusatory, more searching."
        "Defend the decision with the models":
            "You point at the printouts. 'Look at the runs—we reduce risk now.' Sora crosses their arms, more guarded. Maya watches you with a hurt like weathered rope; the distance between you stiffens."

    # --- merge ---
    "The room's tone shifts toward negotiated terms and the establishment of stronger transparency mechanisms."
    hide maya_cruz
    show dr_noor_patel at center:
        zoom 0.7

    dr_noor_patel "This is the hardest part of the work—when technical necessity collides with social trust. Both are right in their own ways."
    "Lina Moreau moves to the whiteboard and writes a line item: 'Independent Monitoring Committee—3 seats community, 2 seats municipal, 1 external auditor.' Her handwriting is neat, the slope of each letter indicating decisiveness."
    hide ari_navarro
    show lina_moreau at left:
        zoom 0.7

    lina_moreau "We begin with a three-year pilot. After year one, an audit. If transparency clauses are met, we'll proceed to phase two—incremental stationing of desal hubs and vertical housing units inland."
    hide sora_watanabe
    show ephraim_blake at right:
        zoom 0.7

    ephraim_blake "The vertical units also satisfy regional housing needs. They pay themselves in the long term through density and tax base."
    hide dr_noor_patel
    show sora_watanabe at center:
        zoom 0.7

    sora_watanabe "You think tax base solves grief?"

    ephraim_blake "No. But it's part of a realistic plan."
    "Ari Navarro [internal]: The conversation becomes a series of practical clacks—items checked, boxes ticked. Emotion isn't absent; it hums at the edges. The tone is procedural, but the stakes are human: homes, traditions, ways of being in a place that is changing shape."
    # [Scene: Rooftop Greenhouse | Late Afternoon]
    hide lina_moreau
    hide ephraim_blake
    hide sora_watanabe

    scene bg ch7_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft drip of condensation; distant murmurs from the lab below.]
    # play music "music_placeholder"  # [Music: A single, sustained cello note underlines the moment—steady, contemplative]
    "You climb the narrow stair and the greenhouse wraps around you in warmth. The amber light turns everything softer—your hands, the paperwork in your folder, Lina's features when she speaks again, quieter now, off-camera."
    show lina_moreau at left:
        zoom 0.7

    lina_moreau "Your tide maps—your overlay of social vulnerability with the hydrodynamics—they're elegant. Clear. Useful."
    "Ari Navarro [internal]: The compliment feels like calibration: it doesn't erase the costs, but it validates the work. It smooths the angle of consent into something you can live with—at least for the moment."
    "You sit at a bench, the municipal paperwork spread before you. The signature line waits like a small causeway you must step across. The seagull pin on your jacket presses into the fabric of your chest—a childhood emblem turned into an adult weight."

    menu:
        "Finger the seagull pin before signing":
            "Your thumb rubs the chipped enamel; memory of a sun-burnt childhood pier: ice cream, a laughing sibling, a storm that changed everything. The motion steadies your hand. You sign, deliberate and controlled."
        "Sign immediately to avoid hesitation":
            "You set the pen down and sign in one clean motion, as if speed neutralizes doubt. The stroke is decisive; the greenhouse hums. Maya inhales sharply, as if she had been holding her breath."

    # --- merge ---
    "The signature is placed; reactions around you shift in intensity depending on how you settled your doubts."
    "Sora Watanabe stands by the glass, watching you sign—an unreadable silhouette. They don't shout. Their quiet is an accusation that doesn't need volume."
    show sora_watanabe at right:
        zoom 0.7

    sora_watanabe "When they put that in press releases—'Ari Navarro leads municipal pilot'—will they mention who had to beg for the wetland funds? Who had to fight for the coop? Or will it just be headlines?"
    show ari_navarro at center:
        zoom 0.7

    ari_navarro "We'll push for the annexes to be public. The dashboard will publish maintenance schedules, budget updates. The monitoring committee will have real power to pause contracts that violate terms."

    sora_watanabe "Real power. You keep using that phrase like it's a building block."

    ari_navarro "Power is only real if we use it. If we sit on it like a trinket, then yes—it's decorative. I'm not signing my name to decoration."
    hide lina_moreau
    show maya_cruz at left:
        zoom 0.7

    maya_cruz "Promise me you'll fight for the co-op, Ari. If we have to move anyone, we do it with dignity."

    ari_navarro "I promise. We'll write the relocation support into the pilot's first-year budget line and create a legally binding clause for community input."
    "Lina Moreau watches you sign, eyes narrowed a fraction—not hostile, simply attentive to process. You hear the seal of the fountain pen whisper across the paper."
    "Ari Navarro [internal]: The paperwork is more than bureaucracy now; it is an axis. On one side: the technical promise of reduced immediate risk. On the other: the slow erosion of autonomy, the cultural displacement of neighborhoods. Your signature is a hinge between them."
    hide sora_watanabe
    show lina_moreau at right:
        zoom 0.7

    lina_moreau "Your maps will guide the construction teams. If anyone can translate risk into practical placement without causing unnecessary displacement, it's you."
    "Ari Navarro feels the flash of being seen—the professional recognition you trained for, the kind that acknowledged skill over sentiment. It is not warmth, but it is recognition."

    ari_navarro "I'll hold them to the community clauses. I won't sign anything that circumvents public review."

    lina_moreau "Good. Public review matters."
    # [Scene: Municipal Offices | Dusk]
    hide ari_navarro
    hide maya_cruz
    hide lina_moreau

    scene bg ch7_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Echoed footsteps on polished stone; distant clatter of demonstration drums.]
    # play music "music_placeholder"  # [Music: The piano motif returns, steady—forward, not faltering]
    "You walk out into the public corridor with the signed packet in your hand. The document feels weighty for its thickness and for the obligations nested inside—audits, maintenance trusts, the monitoring committee, relocation funds, annexes. The weight is partly legal, partly moral."
    "Sora Watanabe falls into step beside you. They are quieter now, not mollified, but less explosive, as if they've switched to a different register of grief and strategy."
    show sora_watanabe at left:
        zoom 0.7

    sora_watanabe "So we watch them then. We don't let them bury the clauses in appendices."
    show ari_navarro at right:
        zoom 0.7

    ari_navarro "We watch. We make the dashboard public. And we build the monitoring committee that can pause construction. We make sure the lab's models are transparent, so the town can see why decisions were made."

    sora_watanabe "And if they try to bypass it? If Ephraim's people lobby for carve-outs?"
    "Ephraim's presence seems to approach even when he is not in the same frame—his promises and networks are pressure that presses at the seams."

    ari_navarro "Then we use the legal tools and the media. We put pressure. We expose conflicts. We don't pretend this is easy. We do the work."
    show maya_cruz at center:
        zoom 0.7

    maya_cruz "Do the work, Ari. Don't make us regret trusting you."
    "Ari Navarro [internal]: Trust is a fragile levee. It holds as long as everyone remembers the labor required to maintain it. You feel the mid-level pulse of urgency—not panic, but standing on a clock's face where every tick is another reason to move."
    "Lina Moreau's team organizes a press release for the pilot. Cameras will come in the morning; banners will be drafted; spokespeople assigned."
    "Ari Navarro [internal]: You taste the after-effect of signature—a metallic, procedural tang. It is neither triumph nor capitulation but an acceptance of a path chosen out of imperfect goods. The town's safety calculus has shifted; your role has changed from independent planner to municipal steward."
    "Lina Moreau's ice-gray gaze meets yours across the briefing table one last time. For the briefest instant, something like softness passes over it. She leans in, off-camera, and offers a compliment that is small but exact."
    hide sora_watanabe
    show lina_moreau at left:
        zoom 0.7

    lina_moreau "Your tide maps will save people."
    "Ari Navarro feels the seagull pin prick against your chest again—heavier now, not from material but from consequence."
    "Ari Navarro [internal]: The pilot begins tomorrow. The greenhouse light has cooled into dusk. You have signed your name to oversight and to political theater. You have chosen a route that prioritizes immediate protective structures while promising community frameworks to hold the process accountable."
    "You stand in the hallway as the rain eases and the town hums its unglamorous preparations. The arousal of the day has not spiked into alarm; it has built into a steady momentum of work—mid-tempo, resolute."
    "Ari Navarro [a final thought carrying you forward]: The paper is signed. The next moves are logistics: the dashboard, the committee nominations, the audit clause language. These are quiet levers—small mechanisms that will determine whether this compromise becomes safety or soft erasure."
    # play music "music_placeholder"  # [Music: The piano motif lingers, then fades into a single held note—an invitation to continue]
    hide ari_navarro
    hide maya_cruz
    hide lina_moreau

    scene bg ch7_453e40_4 at full_bg

    scene bg ch7_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter8
    return
