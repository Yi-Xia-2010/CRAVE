label chapter12:

    # [Scene: Hybrid Pilot Site — Harborfront | Early Morning]

    scene bg ch12_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The clatter of tools, a low diesel pump at the edge of the worksite, and the constant, high hiss of the incoming tide]
    # play music "music_placeholder"  # [Music: Urgent, bright strings building into a driving rhythm]
    "You wake with the memory of last night's signatures like a taste at the back of your throat — iron and possibility. The memorandum moved; the city’s ledger shifted under pressure; contracts and covenants now carry"
    "the weight of people's roofs. The worksite smells of wet wood and peat, and the air is thick with the metallic tang of rain still on the bay."
    "You are pulled forward by momentum more than intention. Boots hit the gangway; the board groans familiar complaint beneath your weight. People are everywhere — neighbors with rubber boots, volunteers with seed-tipped gloves, technicians checking sensors."
    "Sami is barking orders with that breathless grin that makes your chest feel both lighter and rawer. Elliot Chen stands knee-deep in the shallows, sleeves rolled, moss and salt crusting the cuffs of his smock. He"
    "looks up when you arrive; his face crumples into that warm, relieved smile that has become your small constancy."
    show elliot_chen at left:
        zoom 0.7

    elliot_chen "You're—' (he waves mud-smeared hand) '—late break of the tide and we had to wrestle one more scaffold in. You okay?"
    show maya_rios at right:
        zoom 0.7

    maya_rios "You are a knot of a thousand small anxieties — the legal text, the oversight board, the people who had to move. But standing here, seeing the first module breathe with living plants, your chest eases into something that matters more than the ache: action."

    maya_rios "I had to make sure the oversight clauses landed right. Dr. Noor called with a tweak; Sami threatened mutiny if we didn't keep the community seats true. I'm here now."

    elliot_chen "Good. Because the sensors just started talking — tidal creep under predicted by three centimeters and the mycelial mesh took on water exactly like the model said. Come see."
    "Dr. Noor steps from under a waterproof tarp, folio tucked under one arm, eyes bright behind rimless glasses. She smells faintly of tea and salt; her presence maps the moment into consequences and data."
    show dr_noor_patel at center:
        zoom 0.7

    dr_noor_patel "Preliminary reads are promising. Soil retention up twenty percent at the pilot site, sediment capture rates matching projection windows. We still need longer-term monitoring but—' (she looks at you) '—this is the sort of proof the council can’t ignore."

    maya_rios "And the buyouts?"

    dr_noor_patel "Protected, with legal escrow and community trustees. Not perfect, but enforced paths exist now."
    "Irene Voss arrives in the worksite corridor as well — her trench coat rolled in one hand, her expression a study in professional restraint. You notice the way she avoids the mud with practiced economy, but"
    "she lets her view rest on the seawall with something like approval. Her presence flips the air into a different note: official success folded into political theater."
    hide elliot_chen
    show irene_voss at left:
        zoom 0.7

    irene_voss "The pilot will be extended to two more corridors if the audits come back as Dr. Noor expects. We can fast-track procurement for the engineered sections adjacent to these living modules.' (She searches your face briefly.) 'This city needs rapid, scalable protections."
    "Sami intercepts you mid-stride, his braid whipping like a calling flag. He thrusts a battered thermos at you."
    hide maya_rios
    show sami_alvarez at right:
        zoom 0.7

    sami_alvarez "Fuel. You look like you haven't slept."
    hide dr_noor_patel
    show maya_rios at center:
        zoom 0.7

    maya_rios "We didn't get it all without cost.' (You sip, the bitter heat working through the tiredness.) 'But we got protections written into enforceable covenants. They can't sell that out without triggers. We built the teeth."

    sami_alvarez "And you built a team that won't let them eat the teeth.' (He punches your shoulder in a quick, affectionate rhythm.) 'Now let's go plant the last segment before the tide fools us."
    hide irene_voss
    hide sami_alvarez
    hide maya_rios

    scene bg ch12_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The tide's slap quickens; a chorus of exultant voices rises in work-song cadence]
    "You move into the work, and the labor itself is intimate — passing salt-scraped planks with Elliot Chen, cradling a root ball over the gap where water wants its teeth. Your hands are in the same"
    "rhythm, and there is an easy rehearsal to how you align: he tilts, you brace; he threads, you bind. The small choreography of building becomes a language that says what speeches cannot."
    show elliot_chen at left:
        zoom 0.7

    elliot_chen "We stitch here, then anchor there, then pack the mycelial composites. Your notes were brilliant — the tidal vector adjustment made the difference.' (He wipes his hands on his thigh and looks at you.) 'You were right about the scaffold tension."
    show maya_rios at right:
        zoom 0.7

    maya_rios "Praise from him is small and sharp, a favor that hums in your chest. It does what hands on a wall always do — it reveals where you crack and where you hold."

    maya_rios "We made it through the redline. You made it look poetic."

    elliot_chen "Only the seawall makes the poetry.' (He grins, then grows sincere.) 'But you—' (he hesitates, the tide giving him courage) '—you turned a clause into a spine. You refused to sign away oversight. That's you."
    "Irene Voss watches the two of you with that careful appraisal that never picks a side too quickly. When she speaks, there is a piano-drop clarity to her words."
    show irene_voss at center:
        zoom 0.7

    irene_voss "This model, if it scales, could be a template for the city's policy. The state is already watching. We will need rigorous oversight, and your community board's involvement is part of that bargain.' (She pauses.) 'Thank you for insisting on the language."

    maya_rios "The gratitude is not simple. There is relief, yes — and the persistent ache for the families who moved with promises that are now enforced on paper. The ache is a shadow to the sunlight; it makes your triumph less singular and more human."

    menu:
        "Offer Irene a seat at the community forum":
            "You extend an invitation with a measured tone. Irene nods, a small, unreadable crease at the corner of her mouth; it's the closest thing to an olive branch you've seen from her, and you tuck it away as leverage."
        "Keep the community forum independent — refuse forms tied directly to City procurement":
            "You state the need for independence sharply; Sami's jaw tightens but then relaxes when you outline oversight mechanics. Irene's expression cools, but she accepts the written proposal, fingers lingering on the legal phrasing."

    menu:
        "Ask Elliot to stay for the oversight meeting tonight":
            "You ask, voice careful. He nods immediately, as if it's the only choice he would ever make; his bright smile steadies you. Sami whoops nearby, pleased at the union of protest and policy."
        "Tell Elliot to go home and rest — you'll handle tonight's meeting":
            "You try to push him away, claiming the mantle, but he resists. 'We do this together,' he says, and the firm cadence in his words dissolves your instinct to shoulder alone."
    "THE END"
    # [GAME END]
    return
