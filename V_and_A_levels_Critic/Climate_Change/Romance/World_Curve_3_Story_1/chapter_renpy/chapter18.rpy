label chapter18:

    # [Scene: Glass Council Chambers | Late Afternoon — Hearing Day]

    scene bg ch13_f7128a_1 at full_bg
    # play music "music_placeholder"  # [Music: Urgent, high-tempo strings; snare-like percussion mimicking a heartbeat]
    # play sound "sfx_placeholder"  # [Sound: Rain hammers the panes; a microphone buzzes and then stabilizes]
    "You stand at the edge of the long table, your notebook closed but warm in your palm. The decision you made in the Hub—push for legally binding community protections through negotiation—has folded the room into an"
    "impossible, necessary choreography. There is paperwork stacked like levees, clauses that must hold when the next storm comes."
    "Councilwoman Reyes sits at the head, slate of proposals open, eyes steady. Ari’s AR cuff flickers schematic layers in his palm; he looks at you not with accusation but with the economical expression of someone who"
    "believes the math will save people. Luca’s shoulders are set like a line of rope, hands bunched where they rest on the table; his face says he wants everything and is afraid every concession is a"
    "cutting away."
    "Nora has a thumb on a legal memo—small, practical anchor. Samir’s weathered hand taps the wood twice, slow as a tidal beat."
    "You feel like the space between one breath and the next could rearrange entire histories."

    "Councilwoman Reyes" "Maya, we have a narrow window before the municipal bond vote. We can attach enforceable covenants to any funded shoreline work. We can also create a stewardship trust with municipal seed funding, matched by private capital if we can structure oversight. But there are strings. Displacement clauses are available where buildings are structurally unsalvageable; relocation is not something this council takes lightly."
    show maya_ortega at left:
        zoom 0.7

    maya_ortega "I know. The priority is to lock in stewardship and land covenants—rights of first refusal for residents, maintenance boards with community veto, transparent reporting, and guaranteed funding for marsh restoration. We can't promise no one will move—that's dishonesty—but we can promise the city won't sell people out."
    show ari_nakamura at right:
        zoom 0.7

    ari_nakamura "We structure the engineered segment to protect the highest-density corridors. In exchange, we codify community oversight into the contract. My firm will fund the pilot if the covenants are clear and enforceable, and the city guarantees matched upkeep funding for—what, five, seven years? After that we build in escrow."
    show luca_chen at center:
        zoom 0.7

    luca_chen "Seven years isn't 'guaranteed' when budgets flip. Who holds the escrow? Who enforces the covenant when the firms change names? Who keeps our rituals—our boat-turning, our fish-market days—alive when the promenade is regraded and insurance changes its mind?"
    hide maya_ortega
    show nora_daz at left:
        zoom 0.7

    nora_daz "We write enforcement mechanisms. Community boards, legal recourse, a trustee chosen from local residents and a rotating council seat. We make the paperwork hard to ride over."
    hide ari_nakamura
    show samir_qureshi at right:
        zoom 0.7

    samir_qureshi "Make them write that the trust's first duty is to homes, not commerce. Make them show relocation as last resort, not an option typed into an excel spreadsheet. Make them fix the roof before you hand the key."
    "The room tightens around those last words. You think of the pilot project that failed—threads of memory, leaked funding, a tent of promises that couldn't shelter storm surge—and you can feel the old guilt like tidewater in your chest."
    hide luca_chen
    show ari_nakamura at center:
        zoom 0.7

    ari_nakamura "We can put punitive clauses for breach. Liquidated damages tied to restoration. We already have legal templates that pass muster with counsel."
    hide nora_daz
    show maya_ortega at left:
        zoom 0.7

    maya_ortega "Then let's draft those now. And schedule a provision—an annual community review meeting that includes on-the-ground inspectors chosen by the neighborhood, with subpoena power for reports."

    "Councilwoman Reyes" "If you can produce language the city counsel signs off on within twenty-four hours, I will file it as amendment A-3 to the bond ordinance. If I present it cleanly, the council will attach it. We need your signatures, Maya—your credibility carries weight here."
    "The tempo accelerates. Papers change hands like lifesaving lines. The strings tighten until the room is a held chord."

    menu:
        "Ask for a public commitment now — get the council on record.":
            "You lean forward, voice meeting the room's speed. 'We need a public commitment, here and now. If you can't commit in public you haven't committed at all.' The council murmurs; some nod, some look away. Ari raises a brow; Luca clasps his jaw, grateful for the clarity."
        "Push for a sealed legal draft first — perfect the language behind closed doors.":
            "You fold your hands over the notebook. 'Seal the language first. A flawed public promise is worse than a quiet, enforceable one.' Councilwoman Reyes taps her stylus; Ari smiles thinly—relief and calculation in the same line—while Luca's face goes tight with distrust."

    menu:
        "Pose with the council and sign the plaque publicly.":
            "You step up to the podium, sign the plaque with a public smile. Cameras flash; people cheer in a guarded way. You feel exposed, like a seam that everyone can stitch at."
        "Refuse the photo — help set up the community tent instead.":
            "You step away from the staged ceremony and head to the tent where elders trade stories and the kids practice net mending. A few leaders frown at your absence on the dais; people in the tent press hands to your shoulder with quiet thanks."
    "THE END"
    # [GAME END]
    return
