label chapter3:

    # [Scene: Municipal Planning Hall | Early Evening]

    scene bg ch3_98c6f2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hum of projectors, low murmur of a crowd, occasional camera shutters; distant gulls cut across faint thunder]
    # play music "music_placeholder"  # [Music: Low, tense synth underscoring the room's clinical calm]
    "You step off the rain-slick steps and into that particular, pressured warmth of too many people gathered to be polite. Your jacket is still damp at the cuffs. The brass of your compass feels cool against"
    "your sternum when you tuck your hand there without thinking—an old habit that steadies the edges of you. Around you, volunteers and neighbors press together like weathered shingles: Rosa's shoulders at the back, Kai near the"
    "edge with a placard folded in one hand, and a ring of journalists with lenses glinting like fish scales."
    "Ibrahim 'Ibe' Rafiq is at your side, pragmatic and human in the center of the stage-bound tension. He scans the room in small, efficient movements—taking inventory of microphones and exits as if the space were a blueprint he needs to read."

    "Ibrahim 'Ibe' Rafiq" "They've got the renderings up.' (He nods to the projection—a sweep of steel and glass promising an unbreachable horizon.) 'It looks... tidy."
    show mara_lin at left:
        zoom 0.7

    mara_lin "Tidy doesn't mean just. Remember that."
    hide mara_lin

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Polite applause from a segment of the room; a reporter clearing her throat]

    scene bg ch3_98c6f2_3 at full_bg
    show eloise_varela at left:
        zoom 0.7

    eloise_varela "Good evening. Asterport has waited long enough. The Shield will protect our city. It is decisive, accountable, and—' (she lets the word hang, pristine) '—transformative."
    "She speaks like someone reading the future from a ledger and finding the sums balance. Her voice is a measured tide that pulls the room with it, and yet under that cadence there is the signature of compromise—breath held, a small jaw flex beneath the composure."

    eloise_varela "We will move swiftly to secure funding and begin construction within months. Some relocation will be required in the most exposed parcels—temporary relocation, with relocation allowances and guaranteed infrastructure upgrades."
    "A few cameras flash. A man in a tailored suit murmurs approval. The map on the wall highlights entire blocks with a clean, corporate ribbon: Redevelopment Zone A, Redevelopment Zone B."
    "You feel the room tilt. The polite applause is thin at the edges, as if the floor beneath it might crumble."
    hide eloise_varela

    scene bg ch3_98c6f2_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Somebody shouts—quiet at first, then more insistently]

    "Press / Crowd (distant)" "What about the low-lying neighborhoods? What about the compensation? What about—"

    "Ibrahim 'Ibe' Rafiq" "Watch her. Eloise knows how to spin the judiciary of compromise. She'll give them numbers and a timeline, sugar-coated. That's her habit."
    show mara_lin at left:
        zoom 0.7

    mara_lin "And she'll call it 'protection' while she moves money into development rights. We've seen that pattern."
    "You look for Samira in the rows—Samira, who could twist policy paths if she chose—but her face is a closed book tonight; her clipboard sits in her lap like a secret. Rosa watches you with the small, weathered severity of someone who has been through cycles before."
    show rosa_alvarez at right:
        zoom 0.7

    rosa_alvarez "Let her speak,' she says quietly. 'Let the words show themselves. People will read between them."

    menu:
        "Step forward to ask a direct question from the floor":
            "You rise, the room's attention slicing toward you; your throat tightens but you force the question into the open, raw and demanding."
        "Stay seated and let Ibe take the lead for now":
            "You press down into your chair, letting Ibe's presence be the visible push; your silence is deliberate—an anchor not absence."

    # --- merge ---
    "..."
    hide mara_lin
    hide rosa_alvarez

    scene bg ch3_98c6f2_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Projector whine, a collective intake of breath]

    "The tablet screen projects a document—legal text, signatures, and a highlighted clause that eats the air in the room" "Redevelopment Rights—Investor Priority Access; Clause 12b: Priority claims for land redevelopment in zones subject to Shield construction, with forced acquisition authority under municipal emergency statutes."
    "It's not a whisper anymore. It's a slab of fact splashed in stark white."
    "A few people shout. Someone curses. Your stomach clenches. The compass at your throat seems suddenly too small to hold the map of what this means."

    "Eloise Varela (face unreadable for a beat)" "That is—rumor and misinterpretation. The language you saw is draft legalese taken out of context. We will ensure equity measures are embedded in any contracts."
    "You watch her hands; she keeps them measured, palms open, the gestures of someone constructing trust brick by brick. But the projection has already ripped the neat ribbon off the plan. Phones are recording every word. Kai's voice rises from near the doorway."
    show kai_moreno at left:
        zoom 0.7

    kai_moreno "You signed with investors who want to tear out our blocks—where's the equity in that, Eloise?"

    "Eloise Varela (turning a fraction toward Kai)" "Mr. Moreno, the redevelopment is part of a financing mechanism. It will bring jobs, resilient construction—"

    kai_moreno "Jobs don't buy back roots."
    "His words hang, the kind that reveal what paperwork can't."

    "Ibrahim 'Ibe' Rafiq" "If that's true, we need to see the contracts. Public oversight—transparent redlines. We can propose a hybrid that keeps people where they are and adds engineered supports.' (He turns to you as if already asking permission to move from talk to a plan.) 'We can draft immediate amendments. I have preliminary modular designs."
    show mara_lin at right:
        zoom 0.7

    mara_lin "We can't treat 'temporary relocation' as a euphemism for permanent displacement. Not again."
    show eloise_varela at center:
        zoom 0.7

    eloise_varela "Temporary measures are sometimes necessary in the face of imminent risk. The Shield will save lives."

    mara_lin "At what cost?' (Your voice cuts sharper than you intend; there is a brittle edge to the words.) 'Are lives saved if neighborhoods are erased and sold off to investors?"

    "Eloise Varela (small, controlled smile)" "We must balance—"

    mara_lin "Balance is what gets written before the scales tilt."
    hide kai_moreno
    hide mara_lin
    hide eloise_varela

    scene bg ch3_98c6f2_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Her breath is barely audible]
    show samira_chen at left:
        zoom 0.7

    samira_chen "I can slow the scheduled vote for the contract. I can put a procedural hold for thirty days—if I can justify it with public comment requirements and environmental assessments."
    show mara_lin at right:
        zoom 0.7

    mara_lin "Can you—will you—hold it without making yourself a target?"

    samira_chen "I don't run the whole process. I can create a pause. But it will be ugly. It will look like obstruction."
    "You see the strain in her face—sympathy and constraint braided together. Her choices are bureaucratic levers that can buy time but will mark her as a player in a political fight."

    menu:
        "Urge Samira to file the hold quietly":
            "You lean in, voice lowered. Samira nods slowly, the weight of what she can do and what she risks making a shadow on her features."
        "Tell Ibe to draft the hybrid on the spot and ask for a public slot":
            "Ibe's eyes flick to you; the plan already forms in his posture. He accepts the cue—construction as counter-speech."

    # --- merge ---
    "..."
    "The projection replay loops the renderings. The Redevelopment Zones pulse in a cool, corporate blue. Outside, rain begins again, measured and steady, like a metronome counting the time you have to act."
    "You remember the Flats. You remember Rosa's hands furred with mud. You remember the street you lost—how voices tried to argue that moving was 'for safety' and how safety was priced like a commodity. The memory is a small, hot stone you carry in your chest."

    "Rosa Alvarez (placid, luminous with hard-won knowledge)" "Words will be traded tonight. Take care where you lay your voice."

    "Ibrahim 'Ibe' Rafiq (quiet, to you)" "We can build something better, Mara. We can make anchors that don't uproot people. But if this is already a sale in thin clothing, we'll have to fight for the terms."

    "Eloise Varela (now addressing the room more pointedly)" "I will open a community advisory board to oversee relocations and contracts. We will commit to public audits and binding clauses protecting displaced residents."

    mara_lin "Her words are scaffolding around the contract. They might be real—tied to enforceable law—or they might be a veneer. The leak has introduced doubt into the narrative. You feel the air thicken, the ways forward narrowing until someone chooses a path."
    "The press leans in; cameras find your face, then Ibe's. People look to you with a question that is heavier than any single person should bear: act, or try to rework?"
    "You feel the pulse at your wrist. Mid-level adrenaline—sharp, purposeful—building toward a hinge. The room holds itself like a lung before a breath. You know that your reaction will set a tone: public rupture or quiet reweaving."
    "Eloise Varela's smile is serene—but unreadable in its sharper seams. Samira's glance is a plea. Ibrahim 'Ibe' Rafiq stands ready with a practical engine. Rosa's presence is an old steadying current. Kai looks at you, raw."
    hide samira_chen
    hide mara_lin

    scene bg ch3_98c6f2_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The projector flicks; the civic map glows a long, thin blue line that seems, for a moment, to divide the room into 'us' and 'them']
    "You can feel the city pressing for an answer. The choice before you is not between neat answers but between different kinds of harm and different kinds of loyalty."
    # [Scene Transition: The hum tightens; people shift, voices layer into a low, loaded chorus]
    show mara_lin at left:
        zoom 0.7

    mara_lin "This is a betrayal if it's used to profit from our loss. We will not let our homes become investment stock."

    "Eloise Varela (cool)" "Then bring your counterproposal. Participate in the advisory board. Work with us."

    mara_lin "Work with us—those words taste like a ledger. You imagine a thousand slips of paper, each with a name and an eviction plan. You imagine Ibrahim 'Ibe' Rafiq's hands, callused and careful, sketching a hybrid that might hold. You imagine Samira stalling a vote long enough to breathe."
    "The moment stretches until decision condenses into the only available shape."
    "You must choose."

    menu:
        "Lead an immediate organized protest at the planning hall—no concessions.":
            jump chapter4
        "Work with Ibe to propose a hybrid technical plan and present it to Samira.":
            jump chapter7
        "Ask Samira for a closed meeting; attempt to stall approvals administratively.":
            jump chapter11
    return
