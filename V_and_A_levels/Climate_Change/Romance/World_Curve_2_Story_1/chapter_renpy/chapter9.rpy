label chapter9:

    # [Scene: Negotiation Room | Morning]

    scene bg ch8_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low murmur of umbrellas folding outside; a distant gull cuts through]
    # play music "music_placeholder"  # [Music: Tense, fast piano motif undercut with staccato strings]
    "You made a choice last night. You remember saying the word negotiate aloud—how it filled the cramped kitchen like a found breath—and how Elias' face tightened, hopeful and afraid at once. You told yourself it was"
    "tactical: win seats, secure protections, make the town harder to bulldoze with glossy renderings. You told yourself you were buying time. Now the room smells like coffee and cold metal and the singed paper of too"
    "many contracts. The choice sits in your throat like a stone."
    "Cassandra 'Cass' Whitlock sits at the head of the table with the practiced calm of someone who has rehearsed every smile. Her suit is shark-sleek; her hands are steady. The council reps spread around her are"
    "a mixture of exhausted, pragmatic, and quietly terrified. Noah Rivera stands near the doorway, jaw clenched, sleeves rolled into chalky forearms. Elias Park is beside you, fingers worrying the copper cuff at his wrist. Aunt Lila"
    "is on your other side, her cardigan bunched into her fist like a talisman."
    show cassandra_cass_whitlock at left:
        zoom 0.7

    cassandra_cass_whitlock "We can make this work for everyone, Mira. A plan with teeth. Funding. Engineering that actually holds. We don't have the luxury of ideology."
    "You swallow. The air is too bright; the projector's hum makes your molars ache."
    show mira_santos at right:
        zoom 0.7

    mira_santos "We don't want 'holding' that dissolves neighborhoods into easements and rezoning lines that let developers rewrite who belongs here. We're asking for legal protections—clear covenants, community oversight."
    "Cassandra smiles at you. It doesn't reach her eyes."

    cassandra_cass_whitlock "Legal protections, yes. But we need flexibility to implement infrastructure. Easements are standard. Rezoning is sometimes necessary for resilience. It's not displacement; it's adaptation."
    "You want to list the names of houses, the recipes Aunt Lila taught people, the nets strung across the boardwalk, the plaster of the bakery where kids learned to build; you want to make her see"
    "that a map of lots is also a map of people. Instead, you breathe and anchor the argument in the language she understands—precedent, covenants, oversight metrics."

    mira_santos "Then let's write the covenants so easements exclude forced buyouts. Let's write rezoning so it comes with tenant protections, relocations negotiated with community input, not imposed."

    "Council Member Ortiz" "Mira, that will slow things and bump costs. We have state timelines. Grants have conditions. Cass is offering leverage we don't get in small grants."
    "Elias Park leans forward, voice low but steady."
    show elias_park at center:
        zoom 0.7

    elias_park "We can prototype the micro-turbines and the raised wet gardens in two neighborhoods as proof-of-concept. If the council sees lower insurance rates and reduced storm damage, that's leverage. But it has to be funded and protected."
    "Cassandra folds her hands, considering him like a curious machine to be calibrated."

    cassandra_cass_whitlock "A pilot is reasonable. We can fund two pilot blocks with a clause for oversight seats—one community seat per oversight committee. That shows the model works. In exchange, the city needs easements to place critical infrastructure. Rezoning will create buffer zones."
    hide cassandra_cass_whitlock
    show noah_rivera at left:
        zoom 0.7

    noah_rivera "Seats don't stop bulldozers. Seats are glass. You talk about 'critical infrastructure'—what does that mean? Which streets become buffer zones? Which houses are now in the 'hazard corridor'?"
    "The room tightens. You feel the tempo of your heartbeat climb—hard and quick—like waves on a thin seawall. Your fingers find the coral scarf at your throat as if to hold yourself to something human."

    mira_santos "We need explicit language. No involuntary buyouts. Binding relocation assistance. Affected neighborhoods named and compensated. Oversight with veto power for major decisions."
    "Cassandra inclines her head, almost kindly."
    hide mira_santos
    show cassandra_cass_whitlock at right:
        zoom 0.7

    cassandra_cass_whitlock "No one wants involuntary displacement. But absolute vetoes can deadlock necessary repairs. We must balance. I propose a tiered oversight—council, independent auditors, and community seats. If the auditors find a plan compliant, it proceeds."
    hide elias_park
    show aunt_lila_santos at center:
        zoom 0.7

    aunt_lila_santos "That's not balance. That's a technocratic ratchet. When the auditors are paid by the same funders who profit from the contracts, who watches the watchers?"
    "The room murmurs. The council's faces are drawn tight. Tension is acid in the air; you can taste it, metallic and close."

    menu:
        "Insist on an independent legal trustee for all easement agreements":
            "You push the paper across the table. 'Name it. A legal trustee with binding authority over buyout clauses.' The room goes quiet; Cassandra's smile thins."
        "Accept oversight tiers but demand a transparent appeals process":
            "You fold your hands and give a measured nod. 'We'll take the oversight tiers on paper, but with a public appeals mechanism and emergency injunction rights.' Council Member Ortiz scribbles the phrase, less than convinced."

    menu:
        "Tell Elias to go public with the auditors' names now":
            "You press, 'We need transparency now. Publish the auditors and trustees—make them accountable before signatures.' Elias hesitates, fear and resolve warring on his face."
        "Ask Elias to keep the auditors confidential but document everything":
            "You whisper, 'Keep them confidential. I want the record, not the spectacle. We'll expose them if they move to displace people.' Elias nods slowly, stomach knotted."

    jump chapter10
    return
