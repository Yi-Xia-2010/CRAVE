label chapter11:

    # [Scene: Vernon & Crow Offices | Late Afternoon]

    scene bg ch10_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The building breathes with low HVAC hums and the soft click of a laser pointer. Outside, gulls argue over the day’s last light. Inside, fluorescent strips buzz.]
    # play music "music_placeholder"  # [Music: Tense, forward-driving strings — quick, insistent]
    "You feel the salt still in the hem of your jacket. Coming here was not only a procedural step; it was a promise to test whether your patience could be translated into terms a firm like"
    "Vernon & Crow could accept. The lobby is cool and polite. Your boots sound loud."
    show dr_elara_voss at left:
        zoom 0.7

    dr_elara_voss "Maya—' [tilts her head, the name clipped to your presence as if checking a coordinate] '—thank you for coming. We have a tight window. The regional committee needs a defensible plan and assurances by month’s end."
    show maya_kwon at right:
        zoom 0.7

    maya_kwon "I understand. Thank you for the meeting."
    "You set your battered notebook on the meeting table like an old tool placed where it can be seen. Elara gestures and a schematic blooms on the nearest translucent screen: a luminous, clean cross-section of rock, reinforced concrete, and a reclaimed promontory that juts like a promise into the bay."
    hide dr_elara_voss
    hide maya_kwon

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The soft mechanical whirr of the model rotating]
    show dr_elara_voss at left:
        zoom 0.7

    dr_elara_voss "A seawall and reclaimed promontory. Durable. Fundable. Rapid to deploy. It protects Main Street and the Fishery from a megastorm's modeled worst-case. It buys the town decades of security while we consider longer-term retreat options."
    "You thumb a corner of a printout—your tidal models, sediment accretion rates, Spartina survival metrics. You speak the numbers because they anchor the vision you carry."
    show maya_kwon at right:
        zoom 0.7

    maya_kwon "If you rely solely on a vertical seawall, you sever the marsh’s ability to dissipate wave energy and trap sediment. That accelerates the very erosion you're trying to stop. My living-shoreline pilot shows sediment accretion in two seasons and resilience to reduced salinity pulses."

    dr_elara_voss "I respect the data. But what you present is incremental. Incremental doesn't matter if a single storm wipes your town's infrastructure out. My mandate is risk aversion. Lives, commerce, immediate safety—those are non-negotiable in my calculus."

    maya_kwon "But the town is not an engineering variable. It's a living economy. Displacing the marsh will change fishing grounds and cultural practices. You can't calculate those losses into a load-bearing wall."

    dr_elara_voss "I don't dismiss cultural loss lightly. I lost colleagues in a failure that spiraled because a margin was ignored for the sake of 'beauty' and 'site fidelity.' I built walls so others wouldn't die."
    # play sound "sfx_placeholder"  # [Sound: A pin-drop silence follows—then the room fills again with people arriving: Priya, Aiden, and Mateo Reyes filed into the clinical light.]
    show priya_anand at center:
        zoom 0.7

    priya_anand "Elara, your model's persuasive on paper, but without local buy-in the project will fracture. People need to feel seen in whatever plan you bring. That's where Maya's pilot is crucial—it's tangible."

    dr_elara_voss "Which is why I invited you all here. A combined approach is logistically messy, but it's possible."
    hide dr_elara_voss
    show aiden_reyes at left:
        zoom 0.7

    aiden_reyes "Immediate jobs are non-trivial. My crew can't eat 'maybe'—they need certainty for the season. If this seawall brings contracts to the dock now, that's not nothing."

    maya_kwon "I hear you. But certainty that destroys the marsh is a false certainty. You can get contracts now and lose a fishery later."

    aiden_reyes "You make it sound binary, Maya. People need roofs and nets now. The promontory gives us that."

    menu:
        "Show him the long-term data":
            "You push the footprint map across the table—overlay after overlay that tracks fishing zones against projected marsh loss. Aiden's jaw tightens as he traces the lines, the math settling into the space between his hands."
        "Acknowledge the immediate need":
            "You soften your tone and list immediate mitigations you can pilot alongside the seawall—selective access points, community-managed coffers for fishers—offering a tangible bridge that buys them breathing room."

    # --- merge ---
    "Priya watches you both, the conductor of a sensitive score."

    priya_anand "If Elara's plan is the one the council can approve tomorrow, we need to show a pathway for inclusion. Maya, if you can set pilot sites that tie into the seawall’s phasing, we can negotiate concessions—access corridors, marsh buffers—language the council understands."
    hide maya_kwon
    show dr_elara_voss at right:
        zoom 0.7

    dr_elara_voss "Concessions are practical. We can design the promontory with cut-outs—managed tidal inlets—that preserve some hydrological exchange. That reduces the wall’s efficacy marginally, but it maintains ecosystems."
    "Your chest tightens in relief at the word 'can'—it carries a corridor of possibility. The situation is messy, but mess is workable. High stakes and high agency. This is what you'd wanted when you walked through the glass."
    "Mateo Reyes shuffles forward, palms damp. He sets a small mason jar on the table. The light through the jar slides green-brown, full of brine and the glint of suspended sediment."

    "Mateo Reyes" "This is what you folks talk about in graphs. This is the marsh water from the channel by my son's landing. Smell it—there's life in it. You'd be asking us to give that up."
    # play sound "sfx_placeholder"  # [Sound: The jar lid pops as he opens it; the room inhales the wet peat and algae-sweet tang. For a second, Vernon & Crow smells like the North Pier.]
    hide priya_anand
    hide aiden_reyes
    hide dr_elara_voss

    scene bg ch10_453e40_3 at full_bg
    show dr_elara_voss at left:
        zoom 0.7

    dr_elara_voss "I grew up with salt on my boots too—just not this salt. Losses change how you calculate risk. I'm not here to erase what you're attached to. I'm here because the alternative—inaction—costs people their homes. I want a plan that doesn't force a choice between livelihoods and lives."
    show maya_kwon at right:
        zoom 0.7

    maya_kwon "Then we don't have to make it binary. We can negotiate phasing, engineer living buffers, guarantee community-managed access. We can make jobs through restoration as well as construction."

    dr_elara_voss "Engineer the buffer zones in phase one. But I will need firm, measurable milestones. If marsh restoration doesn't meet agreed metrics, we proceed with additional hard measures. That protects the town."
    show aiden_reyes at center:
        zoom 0.7

    aiden_reyes "So the town gets both: jobs for my crew now and a shot at restoration later. That's something I can sell to the dock."
    hide dr_elara_voss
    show priya_anand at left:
        zoom 0.7

    priya_anand "And I can draft community provisions—hiring quotas, local oversight—so this is not a top-down handover. The funders like clear governance."
    "You close your eyes for a fraction of a breath and picture the marsh in the jar: the way the reeds bent in channels, how sediment gathered in certain eddies. Your models are not just equations; they're the marsh's memory."

    maya_kwon "I can enter formal negotiations. I'll push the restoration language and make the metrics legally binding. But I need explicit commitments—phasing that prioritizes marsh reconnection in the first construction window."
    hide maya_kwon
    show dr_elara_voss at right:
        zoom 0.7

    dr_elara_voss "And I will commit to creating tidal inlets in the promontory design, and to sharing a transparent monitoring dashboard. If we agree on the milestones, we have a pathway to both security and restoration."

    menu:
        "Reach for Aiden's hand under the table":
            "You close your fingers over his—an electric, private thread. He squeezes back, steadying both of you in the rush of plans and promises."
        "Keep your hands on your notebook and speak the terms":
            "You tap a line on your page—phasing deadlines, monitoring cadence. Your voice is all rigor; your tenderness is routed through data. The room leans in."

    # --- merge ---
    "The room shifts; energy focuses into rails of action. The plan that stands before you is neither pure marsh nor pure concrete; it is hybrid, negotiated, leaky in ways that might allow life to persist alongside"
    "hard lines. The arousal in the room is high: rapid agreements, rapid objections, quick drafting of phrases that will bind futures."

    dr_elara_voss "I will prepare the technical brief. Priya will handle the governance text. If Maya spearheads the monitoring protocol, Vernon & Crow will present a phased bid that includes marsh-friendly engineering."
    hide aiden_reyes
    show maya_kwon at center:
        zoom 0.7

    maya_kwon "And we'll bring the co-op and the council into every step. No surprises, no backroom deals."
    hide priya_anand
    show aiden_reyes at left:
        zoom 0.7

    aiden_reyes "That's the first time in weeks the dock looks forward instead of bracing."

    "Mateo Reyes" "Don't let the town be just a line item in a ledger. Let it be something you can't sell."

    dr_elara_voss "I'm offering you access to the table. Shape it, Maya. Or decline—take your pilot outside of our timeline and risk being sidelined administratively and politically. Either way, this choice will redirect the shore's shape and the town's future."
    "You feel the room condense into a single fulcrum. Your chest hums with the decisions you already weighed on the boardwalk, but now the consequences are spelled out in bids, in jobs, in jars of marsh water. The choice vibrates like a wire under tension."
    hide dr_elara_voss
    hide maya_kwon
    hide aiden_reyes

    scene bg ch10_453e40_4 at full_bg
    "Your breath shortens—not panic, but the high, clean catch of someone about to step onto a stage. This is what you came back for: not the comfort of certainty, but the responsibility of reshaping certainty into something that can hold both people and place."
    "You close your notebook and, in the space between pulses, you make the choice."
    # [Page-Turn Moment]
    "You let the jar's smell sit in your memory. You let Aiden's hand, whether held or unheld, be a promise tethered to the work. The model on the screen is both a plan and a test:"
    "can technical force be bent to ecological ends? You have a seat at the table. Now the question is whether to use it to carve out marsh space or to walk away and keep the pilot"
    "pure. Your next move will be the hinge for Main Street, for the marsh, and for everything—personal and public—that has led you here. You breathe in the hum of fluorescents and the wet salt that someone"
    "still carries on their coat; you breathe out a single steady 'yes'—but it is not yet spoken."

    scene bg ch10_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter12
    return
