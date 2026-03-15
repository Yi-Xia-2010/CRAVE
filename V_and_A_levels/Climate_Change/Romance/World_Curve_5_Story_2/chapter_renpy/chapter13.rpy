label chapter13:

    # [Scene: Negotiation Room | Late Afternoon]

    scene bg ch13_f99e88_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense strings under a steady drum — urgency threaded with resolve]
    # play sound "sfx_placeholder"  # [Sound: The distant slap of waves on pilings, a soft electronic hum from Jun's device]
    "Narration:"
    "You sit with your hands flat on the table, the waterproof notebook folded beneath your palm like an old talisman that can't speak for you now. Your wire-frame glasses catch the pale light from Aria's tablet;"
    "in the lenses you see legal clauses, then your own face, then the town's future reflected back and forward in a single glance. The room smells of rain on circuitry and the faint, clean ozone of"
    "new ink. Your pulse is a companion you no longer try to ignore."
    "You breathe in. You breathe out. Each exhale is a small claim — for access, for livelihoods, for histories that don't translate neatly into risk assessments."
    show jun_park at left:
        zoom 0.7

    jun_park "We've uploaded the redlines. TideLine's counters are highlighted in yellow. They pushed for indemnity language that would let them alter access without local consent."
    "Narration:"
    "Jun's voice is thin but steady; you hear the strain under the professional cadence. He keeps glancing at Aria as if looking for permission to be softer than he feels."
    show mayor_ana_beltran at right:
        zoom 0.7

    mayor_ana_beltran "We don't accept clauses that can be amended behind closed doors. Not while shorelines and people's homes are on the line."
    show marin_sol at center:
        zoom 0.7

    marin_sol "Our town doesn't own a single hypothetical. We own the pier, the dinners, the nets. Any clause that severs those from decision-making is not adaptation—it's displacement."
    hide jun_park
    show aria_chen at left:
        zoom 0.7

    aria_chen "Marin, what we offer is scalable protection. You're asking us to accept requirements that will reduce the system's efficacy. Community oversight is possible, but vetoes can become liabilities in a storm. We need operational certainty."
    "Narration:"
    "Her eyes are a precise, reflective blue, the kind that scans a problem for the fastest path to a solution. You can feel the argument: speed versus stewardship, scale versus soil. The air tightens in the room as if the tide has a say in the rhetoric."
    hide mayor_ana_beltran
    show dr_lian_obasi at right:
        zoom 0.7

    dr_lian_obasi "Operational certainty doesn't preclude social license. We've modeled hybrid scenarios; with community co-ownership of maintenance and a local oversight board, the system stops being something done to the town. It becomes something the town does."

    aria_chen "Modeling doesn't change liability. If we bind ourselves to community veto in every instance, we could be legally exposed if a segment fails. Investors expect confidence."
    hide marin_sol
    show mayor_ana_beltran at center:
        zoom 0.7

    mayor_ana_beltran "Then explain it in the contract. Define guarantees. Make it public. Make hiring local mandatory. Show us how your operations can survive transparency."
    "Narration:"
    "Mayor Ana's face is a map of choices made and held. You sense the weight of municipal responsibility in the set of her jaw and the steadiness of her hands. The room moves, a small current of wills circling a common island of compromise."

    menu:
        "Insist on explicit co-ownership clause":
            "You slide forward. 'We need clear, enforceable co-ownership language. It must be in the contract, unambiguous: shared maintenance responsibilities, joint budgetary approval, and a legal right to request audits.' Jun types as you speak, a litany of redlines making themselves into teeth."
        "Propose a legal escrow with phased implementation":
            "You offer a bridge: 'Let there be a legally binding escrow and phased roll-out, tied to measurable community oversight milestones. That buys safety while keeping guardrails.' Jun nods, carving the phrase into the document like a scaffold."

    # --- merge ---
    "The bargaining continues along the same thread of compromise and tension."
    "Narration:"
    "The choice you make is a tone as much as a clause. If you press for iron teeth, you feel the room stiffen with the possibility of a pitched legal fight. If you offer a phased"
    "bridge, you give TideLine a runway — and give your neighbors a shot at watching the pilot closely. Either way, the bargaining is fast, precise, and high-stakes. Your chest hums with the electrical charge of it."

    aria_chen "If we accept co-ownership, it must be limited to clearly defined responsibilities. We cannot allow operational paralysis. And any veto needs a trigger: not preference, but demonstrable harm."
    hide aria_chen
    show marin_sol at left:
        zoom 0.7

    marin_sol "Then define 'demonstrable harm.' Spell out thresholds, timeframes, and an emergency override that still requires post-action review and community remediation. No hidden clauses. No private arbitration that cuts the public out."
    hide dr_lian_obasi
    show jun_park at right:
        zoom 0.7

    jun_park "We can add a public audit clause, binding transparency reports, mandatory local hiring percentages, and an access guarantee for small-scale fishers. The veto will be framed as a community review process with legal standing — with strict definitions to prevent abuse."
    hide mayor_ana_beltran
    show aria_chen at center:
        zoom 0.7

    aria_chen "Public audits...local hiring...access guarantees. Those are negotiable. But remember: this increases contractual complexity and risk for TideLine. We will require indemnities against third-party interference."
    hide marin_sol
    show mayor_ana_beltran at left:
        zoom 0.7

    mayor_ana_beltran "We won't sign indemnities that suppress our right to litigate. The town's legal counsel will not accept gag clauses or private arbitration as the final word."
    "Narration:"
    "You can feel the trade-offs like weather on your skin. The conversation speeds and slows like a barometer falling then holding — adrenaline in your limbs as clauses are added, redlined, folded into new language. Jun's"
    "tablet buzzes; Aria reads with the calm concentration of someone used to shaping reality with clauses. Lian leans over to point at a paragraph and you watch the words rearrange themselves from hazard into protection."
    hide jun_park
    show dr_lian_obasi at right:
        zoom 0.7

    dr_lian_obasi "If we add community oversight with veto only in defined emergency conditions, and couple that with a joint maintenance fund co-managed by the co-op and TideLine, we can bind them financially to the shoreline's long-term health."

    aria_chen "We can accept co-management for predefined sectors — not every coastal segment. We'll agree to transparency, local hiring quotas for installation and maintenance, and a clause protecting small-scale access for registered fishers. But in declared extreme events, operational command rests with the system's emergency protocol — with mandatory after-action community review and restitution if harm is caused."
    "Narration:"
    "The language is not poetry. It's contract law: blunt, antiseptic, capable of carrying promises across administrations. It burns with compromise and stubborn care. Your throat goes dry when Jun reads the redlined paragraph aloud — the"
    "one that stitches community voice into corporate scaffolding, the one that names access rights and oversight boards, the one that forces TideLine to open its books to public scrutiny."

    menu:
        "Ask Jun to add a clause for independent ombuds oversight":
            "You clear your throat. 'Add an independent ombuds clause — a third-party appointed by mutual consent to audit and adjudicate disputes.' Jun's pen hovers, then writes the phrase like an anchor."
        "Push for explicit hiring percentages for local contractors":
            "You press your thumb to the table. 'Local hiring must be concrete — percentages, timelines, penalties for noncompliance.' Jun nods, and the numbers appear, cold and binding."

    # --- merge ---
    "The negotiated details are incorporated into the draft contract."
    "Narration:"
    "These are details that feel, in your bones, like survival. You bargain, not for victory, but for structure: legal scaffolding strong enough to tether TideLine's speed to the town's history."

    aria_chen "You've pushed hard, Marin. These terms...they contain cost and complication. But I understand the politics. If TideLine is to stand here, it must stand publicly. We'll commit to a co-ownership framework for specified zones, transparent reporting, and the access protections you require. We will accept binding audits and community-appointed oversight representatives. We will also retain operational emergency authority with mandated post-event redress."

    mayor_ana_beltran "And the maintenance fund?"
    hide aria_chen
    show jun_park at center:
        zoom 0.7

    jun_park "Jointly managed. Audited annually. With funding triggers tied to measurable ecological and social indicators."
    "Narration:"
    "When the final paragraph is drafted, it reads like a strange, stubborn map: clauses that bind, that require TideLine to hire locally, to publish reports, to cede certain community decisions to boards that answer to the"
    "people who fish, mend nets, and pass down tidal songs. It will not be perfect. You know that. Modular barriers will still be installed in places you would rather have left breathers of marsh and reed."
    "But the town will have legal teeth now, and teeth mean resistance."
    hide mayor_ana_beltran
    show aria_chen at left:
        zoom 0.7

    aria_chen "We will sign. With these protections on record, TideLine's prototype can proceed where we've agreed. We'll publish the contract. We'll open hiring segments to the co-op. We'll accept the ombuds limitation and the audit schedule."
    "Narration:"
    "Relief doesn't arrive like sunlight. It arrives like a tideline easing: a hard edge of tension softening, then a rush of warmth that makes your fingers tingle. Your throat loosens until words spill over."
    hide dr_lian_obasi
    show marin_sol at right:
        zoom 0.7

    marin_sol "Then let's sign."
    # play sound "sfx_placeholder"  # [Sound: Pens uncapping; a soft rustle of paper; the thin click of a stylus]
    # play music "music_placeholder"  # [Music: Strings surge into a hopeful, driving motif — high arousal, celebratory but strained]
    "Narration:"
    "You sign first. The pen feels clumsy in your hand, heavy with the weight of commitments that will outlast any one administration or person. Aria follows, the gesture efficient, almost ceremonial. Jun signs with a small,"
    "relieved exhale. Mayor Ana's hand trembles a fraction — not from uncertainty, but from the exhaustion of bearing a town's trust."
    hide jun_park
    show dr_lian_obasi at center:
        zoom 0.7

    dr_lian_obasi "This won't stop everything overnight, but it's a framework that forces accountability."

    marin_sol "We made them accountable. And we made it public."

    aria_chen "Public scrutiny costs us leverage. But it also gives us legitimacy. We knew the trade. May it serve your community well."
    "Narration:"
    "Her tone holds no victory lap and no malice — only the compact of two people who understand the mechanical cruelty of big projects and the small mercy of binding them. There is an odd tenderness"
    "in that recognition: you both fought for different ends and landed on a middle road that, while imperfect, offers a chance."
    hide aria_chen
    hide marin_sol
    hide dr_lian_obasi

    scene bg ch13_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant gulls cry, sharper now, as if to mark the moment]
    "Narration:"
    "The papers go into a folder. A copy will be posted, public and unerasable. TideLine will install where agreed. The co-op will have legal voice. The maintenance fund will be jointly managed. The ombuds will be"
    "able to call for audits. The town will still pay in money and time; legal leverage is not free."
    # [Scene Transition Cue]

    scene bg ch13_f99e88_3 at full_bg
    # [Scene: Rooftop Community Garden & Storm Shelter | Dusk]

    scene bg ch13_f99e88_4 at full_bg
    # play music "music_placeholder"  # [Music: Warm, sparing piano with a single cello holding a sustained, gentle note]
    # play sound "sfx_placeholder"  # [Sound: Wind through reclaimed fabric; distant laughter from a co-op kitchen below]
    "Narration:"
    "You climb the last ladder and the rooftop opens — a small, green world stitched over concrete. The community garden glows; the shelter's doorway shows a spill of warm light. Kaito Navarro is there, taller than"
    "the memories that sometimes make him small, hands wrapped around a thermos like it is the world's most ordinary treasure. He looks at you with that steady, honest gaze that cuts across plans and polls and"
    "pressure."
    show kaito_navarro at left:
        zoom 0.7

    kaito_navarro "You did it."
    show marin_sol at right:
        zoom 0.7

    marin_sol "We did it. It wasn't perfect."

    kaito_navarro "Since when have we ever had perfect? The nets still think otherwise."
    "Narration:"
    "He reaches out without asking and takes the thermos, offering warmth between your hands. Your fingers brush; the contact is small and enormous at once. Steam fogs the air, and your breath comes out in the same rhythm."

    kaito_navarro "I was worried you'd try to do this alone. You shouldn't have to carry it like that."

    marin_sol "I almost did. There were so many moments where making the easier choice would have felt like saving everything. But I kept thinking of the co-op's bell, the way Old Tomas talks about tides like they're relatives..."

    kaito_navarro "You kept thinking of us."
    "Narration:"
    "He doesn't try to finish the sentence for you. He doesn't need to. The rooftop is quiet except for the city and the low, pleased murmur of people who know their work is not yet done but is now shared. You fold your hands around the thermos until they warm."

    menu:
        "Ask Kaito if staying in Maris Bay together is possible":
            "You tilt your head. 'Can we... do this together? Build this and still—stay?' Kaito's hand tightens around yours, knuckles whitening. He breathes, 'I don't know. But I want to try—with you.' The answer is not a promise, only intention, and it sits between you like a fragile flag."
        "Tell Kaito you need time before defining 'together'":
            "You draw a slow breath. 'I need time. Not because I love you less, but because the town needs me now.' Kaito's face falls for a flash, then steadies. 'I get it,' he says. 'Take what you need. I'll be here.' The quiet is honest, not empty."

    # --- merge ---
    "The rooftop scene continues with the same emotional tenor and commitment to truth."
    "Narration:"
    "You choose words that are true rather than convenient. Whatever tenderness might have been bought with simpler assurances is refused in favor of truth. Romance in this hour is not a tidy end; it's a continuing"
    "thing — honest, patient, and complicated. The thermos passes between you like an offering and a pact."
    "You look over the rooftop. Below, the first crews are already lined up to begin the phased work; some of them are people you taught to map saltwort, people who will now have contracts and wages"
    "and, importantly, a voice. The signed contract will be tested in courts and town meetings and storms. It will be a living thing: messy, accountable, rooted in both legal text and daily tending."
    show dr_lian_obasi at center:
        zoom 0.7

    dr_lian_obasi "Marin! There's a press van asking for statements, and Old Tomas wants to put up a notice at the co-op. They want to know when the maintenance fund releases start."

    marin_sol "Tell them they'll have the first public report in ninety days. And that the oversight board will meet next week."
    "Narration:"
    "You are tired in a way that proves you did not run away. The fatigue is threaded with an ache, yes, but also with the high, clear lightness that comes from aligning action with conviction. The"
    "town will pay. So will you, in ways visible and invisible. But there is now legal muscle to the co-op's voice, a structure you helped carve out of contract language and dogged persistence."

    kaito_navarro "You're not alone in this."

    marin_sol "I know."
    "Narration:"
    "The thermos between you grows lighter as you drink. Your hands are cramped around it, and the warmth seeps in. Somewhere beyond the rooftop, a curtain of rain begins to move inland, softening the air and making the lights on the pier bleed into long, honest reflections."
    "You let the sensation settle: relief braided with vigilance, companionship braided with unresolved futures. You gave up certain comforts and a tidy career path to make a covenant the town could live with and be defended by. You lost the easy road, but you kept the honest one."
    "Kaito Navarro slides an arm around your shoulders in a movement more companionable than possessive. It's not a conclusion. It's company."
    "You close your eyes for a beat, and the rooftop — the town — the contract — the thermos — fold into a single, warm fact: you are less alone than you were at dawn."
    hide kaito_navarro
    hide marin_sol
    hide dr_lian_obasi

    scene bg ch13_f99e88_5 at full_bg
    # play music "music_placeholder"  # [Music: Slow fade to a sustained, hopeful chord]
    # play sound "sfx_placeholder"  # [Sound: Rain beginning; the distant bell from the co-op rings, steady and human]
    "Narration:"
    "The contract will be contested and enforced and reinterpreted. The rooftop will need mending. The sea will keep testing lines drawn on maps. But today, you have pushed truth into the public record and given Maris"
    "Bay a legal lever. You have a field of people now legally empowered to insist that the shoreline stay more a shared home than a privatized fortress."
    "You rest your jaw on your chest, feeling the thrum that has kept you going for months: the pull of responsibility, now diffused across hands that chose to keep working beside you."

    scene bg ch13_f99e88_6 at full_bg
    # play music "music_placeholder"  # [Music: A hopeful swell, cello and piano together — high energy tempered with tenderness]
    # play sound "sfx_placeholder"  # [Sound: Rain increasing; the distant gulls cry]
    "Narration:"
    "The finality of the signatures settles around you like weather: inevitable, binding, and resistant. You let the rooftop scene hold its warmth a beat longer, a tether against the unknown."

    scene bg ch13_f99e88_7 at full_bg
    "THE END"
    # [GAME END]
    return
