label chapter12:

    # [Scene: City Hall — Records Office | Late Afternoon]

    scene bg ch10_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The low thrum of the building's HVAC, a distant council gavel echoing through the corridors, pages scraping as you sort documents.]
    # play music "music_placeholder"  # [Music: Tense BGM — a low, pulsing string rhythm beneath a sharper piano motif.]
    "You shoulder the weight of what you promised in the chamber like a physical thing — not just an idea but responsibility that needs signatures, dates, and corroboration. Rosa slides a stack of scanned minutes toward you; the fluorescent light picks out the edges like the teeth of a comb."
    show rosa_tan at left:
        zoom 0.7

    rosa_tan "We found the contracts. The deliverables list matches the complaints from two towns — Seabrink and Halver. Short-term beach armor, then 'maintenance' clauses that pushed communities to accept more work."
    show maya_soler at right:
        zoom 0.7

    maya_soler "Read it to me."
    "Rosa breathes fast — like she's been running. Her fingers tap the margins where she has already circled names and line items."

    rosa_tan "Look here — clause eighteen. It explicitly caps the contractor's liability and funnels all long-term monitoring to the municipality. Promises a fast 'protective uplift' and then—' (she swallows) '—the plan makes retreat economically impossible."
    "You lean in. The paper smells faintly of printer ink and old coffee. Your thumb grazes a stamped date: three years ago, after a storm that left houses sitting lower in the mud. Each name is a small chronicle of lost trust."
    show prof_noor_azizi at center:
        zoom 0.7

    prof_noor_azizi "The pattern is consistent,' Noor says quietly, her spectacles sliding down as she flips between spreadsheets and a photo of a shoreline map. 'Short-term engineered defenses, insufficient sediment transport modeling, and then contract clauses that prioritize remediation revenue over ecosystem recovery."
    "You feel the room narrow. Noor's voice is a bracing, exacting instrument; it keeps you anchored as the facts pile up. The lamp throws shadows across the pages, turning margins into cliffs."

    maya_soler "If Elias's firm did this elsewhere, the town needs to know. We can't let him frame delay as obstruction."
    "Rosa slams a hand on the table, a little too loud for the quiet. 'We can build a case. Testimonies, invoices, those meeting minutes we pulled from the archive. But—' Her eyes find yours. 'We'll be visible. He'll—'"
    "Before she finishes, the office door opens and a courier slips in with a sealed envelope and a name on the front: Voss & Meridian, Legal Counsel. The courier's boots squeak against linoleum; the sound throws you like a stone rippling in still water."
    # play sound "sfx_placeholder"  # [Sound: Envelope thud. The room exhales together.]
    "You break the seal. Inside, on thick letterhead, the language is clinical and cold: formally demand cessation of defamatory actions; pursue all legal remedies; immediate removal of alleged accusations or face injunctive relief. The signature is Elias Voss's."

    prof_noor_azizi "A warning. Preemptive. They're trying to intimidate."
    "You feel your coral pendant against your sternum as if someone pressed their thumb there. It is heavier than normal — a pebble dragging at the center of a tide."

    maya_soler "They can send threats. They can't erase facts."

    rosa_tan "Threesome of problems: legal fees, counterclaims, and a smear campaign. If they run a narrative, people will start asking whether the living breakwaters are 'risky' because you 'rushed' them."

    maya_soler "Then we make the facts bulletproof."

    menu:
        "Ask Noor to prioritize hard data — sediment and failure modes":
            "Noor nods, already pulling up results from the coastal model. The hum of the computers swells; numbers and graphs become weapons in your hands."
        "Tell Rosa to keep pushing testimony from Seabrink and Halver citizens":
            "Rosa's eyes flash. She taps her phone — names and leads already appearing. The room feels like a beehive ready to swarm."

    menu:
        "Ask Aiden to keep his circle from accepting offers for now":
            "Aiden looks at you. A beat passes where the wind fills the silence; then he nods, jaw unclenching slightly. 'I'll talk to them,' he says, voice low."
        "Offer to bring concrete evidence to the docks — show them the Seabrink documents":
            "Your words plant a seed. Aiden's eyes sharpen. He rubs the compass once, as if finding a course. 'Bring it,' he says. 'They need to see the ledger and not just the coin.'"

    menu:
        "Hold a secret meeting tonight to collect more documents and corroborate stories.":
            "Rosa nods, eyes bright and fierce. 'We do it quietly. Bring proof, testimonies, the consultant.' Noor begins listing experts to call. The plan smells of midnight and rain and the resolve that comes from being cornered."
        "Go public immediately and force a formal investigation.":
            "Rosa's face tightens like a drumhead. 'We will be visible,' she says. 'We'll call the press, demand a hearing. Either it stops him, or it paints a target on our backs.' Noor hesitates, then sets her jaw, 'If the science stands, transparency is the right weapon.'"

    menu:
        "Hold a secret meeting to collect more documents and corroborate stories.":
            jump chapter13
        "Go public immediately and force a formal investigation.":
            jump chapter14
        "Confront Elias privately and demand a pause.":
            jump chapter13
    return
