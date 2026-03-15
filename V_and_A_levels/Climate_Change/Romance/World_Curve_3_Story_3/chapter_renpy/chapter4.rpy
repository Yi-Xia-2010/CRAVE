label chapter4:

    # [Scene: Council Hall | Midday]

    scene bg ch4_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense, rhythmic percussion underscored by a high, insistent synth]
    # play sound "sfx_placeholder"  # [Sound: Low murmur of councilors, the faint click of a recording device, HVAC whisper]
    "You step into the room heavy with anticipation, the pendant at your throat a familiar counterweight. The tablet under your arm feels like ballast and blade—data that can steady a decision or cut people out of"
    "it. The fluorescent light is too white, too honest; it throws the salt of your hair into sharp relief."
    "Asha stands near the far end of the table, fingers steepled, plant-stained lab coat a human anchor in the clinical room. Diego sits among community witnesses, a folded map peeking from his satchel. Emil is at"
    "the back, raincoat collar up, hands worrying at the tide-alert watch on his wrist. Noah is already in conversation with a Consortium representative—calm, contained, the kind of calm that makes you want to check the tide."
    "You breathe in: recycled coffee, a metallic edge of ozone from the monitors, and the faint musk of inked paper. Your mouth tastes like metal and salt."
    "Asha moves closer before you speak. She lowers her voice to a private, steady cadence."
    show asha_karim at left:
        zoom 0.7

    asha_karim "Keep them with the stories. You have the numbers—use them to protect the names behind them."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "I will. I brought Diego's map.' (You tap the tablet; a photocopy of handwritten lines and household notes appears onscreen, edges marked in cramped ink.) 'And the prototype specs for the modular breakwater-living hybrid."

    asha_karim "Good. Then tell them why the living shorelines matter where the seawall would raze a neighborhood."
    "Councilor Mira opens with a procedural flourish. Figures float across the screens: projected loss curves, insurance deltas, bond yields. The Consortium's economist slides a slick spreadsheet the color of sea glass. The room tightens; every number is an argument that smells faintly of money."
    show mayor_lila_chen at center:
        zoom 0.7

    mayor_lila_chen "We've seen both models. We need a plan that minimizes economic risk and preserves critical infrastructure. I'm listening."

    "You start with the maps—Diego's handwriting superimposed on elevation models. Your voice is calm but sharpened, each sentence a tool. You name streets and faces, not abstractions" "This block floods three times per season now. Señora Alvarez has lived there thirty years; her shop can't be moved without losing her livelihood."
    "Diego leans forward, voice rough with urgency."
    hide asha_karim
    show diego_ramos at left:
        zoom 0.7

    diego_ramos "They're not just data points. They repair the docks with chestnuts and nails. They barter produce for tow labor. You build a concrete wall there, you erase a marketplace."

    "Councilor Mira" "We can't preserve every market. The question is triage."
    "You open the compromise—the hybrid you sketched from sleepless nights. Targeted engineered defenses for high-value nodes: port arteries, the hospital intake, the transit hub. Living shorelines, marsh restoration, and relocation aid where neighborhoods are low-lying but"
    "culturally vital. Governance structures that make communities co-owners of retrofit funds. A fund line to underwrite maker-led retrofits—Diego's workshops, Emil's floating gardens—administered through co-op boards with city oversight."
    "The room reacts in a dozen small ways. The Mayor's eyebrows tighten, not unfriendly. A Consortium bond analyst exhales through teeth, recalculating quietly on a screen. Noah watches you from across the table, his expression held like a test weight."
    hide maya_reyes
    show noah_ortega at right:
        zoom 0.7

    noah_ortega "It's pragmatic,' he says. 'Targeted defense limits spend and preserves critical functions."
    hide mayor_lila_chen
    show maya_reyes at center:
        zoom 0.7

    maya_reyes "Pragmatic, and principled. But only if we hardline funding for co-op governance and enforce relocation aid so it's voluntary and dignified."

    noah_ortega "I can live with governance structures on paper."

    maya_reyes "And binding clauses—audits, community representation quotas in oversight—so the funds aren't rerouted."

    menu:
        "Lead with the human story—show Diego's map on the screen now":
            "You push Diego's map into the center of the display. Quiet spreads; faces press at the edge of the screen and into the room. Councilors shift in their seats, voices dip. The Mayor's gaze catches the hand-sketched margins where people have scrawled plea notes—an intimacy the spreadsheets couldn't touch."
        "Lead with the numbers—open your simulation and show projected damage reduction":
            "You pull up the simulation, waves moving in time across the mesh. Lines of lost asset value flatten under the hybrid proposal. The economist nods slowly, fingers dancing across a tablet. The room's mechanical pulse speeds—data comforts them. Either way, the conversation tightens around your proposal."

    menu:
        "Ask for Emil to speak now—bring the makers into the room for a short statement":
            "Emil rises, voice steady despite the tightness in his chest. He speaks in concrete terms—how a floating garden deploys in a week, how retrofits can be community-maintained. The room hears real build times, not projections. Councilors who had been abstractly convinced now picture labor and tools and nights of work."
        "Keep the conversation between officials—save maker testimony for the community forum":
            "You keep Emil seated. He nods, stiff but understanding. Officials continue their legal parsing; the language sharpens. You sense a longer slog ahead to translate municipal consent into actual on-the-ground capacity."

    menu:
        "Take his hand—show you're in this together":
            "You reach for Emil's fingers. His skin is warm and the dock tilts a fraction. He squeezes back—firm, grounding. It is a small, human alliance that steadies you, a promise without paperwork."
        "Keep a careful distance—focus on logistics":
            "You fold the canvas up and tuck it into Emil's satchel with a practised, practical motion. Your voice sharpens into inventory—materials, timelines, volunteer rosters. Emil nods, the intimacy deferred into plans and lists. The closeness melts into the hard edge of work."

    jump chapter5
    return
