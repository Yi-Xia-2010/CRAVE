label chapter10:

    # [Scene: Tide Lab (Converted Research Ferry) | Early Morning]

    scene bg ch10_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low mechanical hum, distant gull calls, the soft clack of a kettle being set to boil]
    # play music "music_placeholder"  # [Music: Quiet, hopeful strings under a steady piano rhythm]
    "You stand over the bench, sleeves rolled, the coral stain at your cuff a familiar punctuation. The Tide Lab smells of salt, algae, and printer ink—every scent a proof you are still, against odds, trying to translate water into law."
    show professor_asha_rao at left:
        zoom 0.7

    professor_asha_rao "We need clause language, not a manifesto. The court will read the clause; the city will quote the clause. Make it unassailable on the technical footing."
    "You trace the printed line with your fingertip. In your head the sentence blooms into the neighborhoods you grew up in—moss on brick, your mother's hands, the community plots that stitched people back after the last"
    "storm. You know why your prose tends toward poetry; you also know that poetry does not survive in procurement code."
    show mara_ellis at right:
        zoom 0.7

    mara_ellis "We can keep the values statement as a preamble. The operative sections should bind procurement to ecological metrics—maintenance plans, community oversight, restoration outcomes."

    professor_asha_rao "Exactly. Translate your stubbornness into definitions. Define 'community-maintained' so vendors can't outsource it to the lowest bidder. Anchor every claim in measurable outcomes: percent native vegetation, stormwater retention per linear meter, maintenance intervals."
    "There's a soft scrape as the kettle whistles. You cup your hands, breathe steam-sour salt into your lungs, and write."
    "You think about how slow this will be—how many hearings, how many revisions—but the green glow around you feels like a patient tide. Small, steady increments of progress. You can almost feel the ordinance taking shape under your pen."

    menu:
        "Keep the preamble heartfelt":
            "You tuck the preamble under the operative clauses—an honest, short paragraph that names community stewardship and the city's duty. It will not be legally binding, but it will be a compass for interpretation."
        "Strip emotion for legal precision":
            "You pare the preamble down to a single line: 'This ordinance prioritizes nature-based adaptation and community maintenance.' It's less moving, but harder to attack in committee."

    # --- merge ---
    "Continue"
    "Professor Asha Rao hands you a stack of annotated memos—peer-reviewed papers, maintenance cost comparisons, community testimony notes. Your watch ticks; each beat a small, stubborn rhythm. You fold the memos into an evidence packet, imagining Council staff reading these at dawn, coffee cooling, momentum humming under fluorescent lights."

    professor_asha_rao "We should run this package through an environmental-economic model before we present. Show them numbers that make their spreadsheets wince—yet demonstrate long-term savings."

    mara_ellis "I'll get the model outputs. Maya has local maintenance schedules we can quantify. Jonah Reyes can supply the engineering constraints."
    "Professor Asha Rao's eyes flick to the ferry's window where the city is an outline behind rain. She smiles—soft, like a lighthouse beam."

    professor_asha_rao "Good. Momentum likes concrete steps."
    # [Scene: Council Chambers (Glass Civic Forum) | Series of Hearings over Weeks]
    hide professor_asha_rao
    hide mara_ellis

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Microphones being tested, murmurs of public comment, a persistent rain against the windows]
    # play music "music_placeholder"  # [Music: A rising cello motif that suggests patient ascent]
    "The hearings begin as a slow tide: one packed room, then two. Councilor Anika Patel is precise in the way of someone who has learned to hold multiple constituencies in the same breath."
    show councilor_anika_patel at left:
        zoom 0.7

    councilor_anika_patel "Language matters. If we require 'community-maintained' without capacity funds, we set communities up to fail. If we require maintenance funds without oversight, we codify neglect."
    "You sit beside her podium, a printed ordinance between your palms. Your notebook—your field kit—feels heavier by the day with versions and redline comments. You recite definitions quietly, like a litany."
    show mara_ellis at right:
        zoom 0.7

    mara_ellis "We need an escrow mechanism—pilot funding earmarked for maintenance, tied to benchmarks."

    councilor_anika_patel "And procurement rules that weight lifecycle ecological outcomes—score bids not only on capital expense but on ecological performance and community involvement."
    "The first committee hearing is sharp. An early guest—an industry representative—raises concerns about scalability and contractual liability. Elias Crowe's company does not need to be named to cast a shadow; his presence has already been felt in lobbyist pamphlets and last-minute memos on 'risk mitigation.'"
    "You keep your face neutral as testimonies thread in—community elders, municipal engineers, a young organizer from the Drowned District who reads a short, fierce statement into a microphone. The room blurs sometimes: fluorescent glare, the sweat at your collar, the exact, steady tick of your watch."
    "Maya sits in the front row, fingers interlocked, neon raincoat a flash in the crowd. After a long session, you meet her eyes; her look is fierce and tired and proud—complex in a way that says everything and nothing at once."
    show maya_ellis at center:
        zoom 0.7

    maya_ellis "People want something that lasts. Not promises. Real funding. Jobs to maintain it, not contracts that disappear."

    mara_ellis "We'll write maintenance as local contracts, with training and apprenticeships. We'll require vendors to partner with local stewards."

    maya_ellis "Good. Make sure the apprenticeships pay a living wage."
    "You feel the room tilt with compromise and hope. The ordinance acquires layers—escrows, pilot districts, reporting requirements. Some language you accept with a small inward gnaw: a clause that allows emergency contracting when time is short. You circle it with your pen."

    menu:
        "Challenge the emergency contracting clause now":
            "You stand during public comment and speak the costs: shortcuts become precedents. You demand stricter sunset provisions for emergency contracting."
        "Allow the clause with oversight adjustments":
            "You accept the clause with added oversight: mandatory audits and a community review panel within six months. It feels like a compromise, but you make it bite with accountability."

    # --- merge ---
    "Continue"
    "Weeks compress into hearings. Jonah Reyes appears at one session, camera slung over his shoulder, rain-dark hair plastered to his forehead. When he speaks with you in the corridor, his tone is low and practical."
    hide councilor_anika_patel
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "I believe in what you're building. If the city commits to this direction, it changes procurement culture. But I won't sugarcoat it—there are neighborhoods at immediate risk. Some zones need rapid physical measures in the next season."
    "You look at him. The space between you fills with unspoken histories, with the murmur of the harbor. His amber eyes are wide and tired, and his expression reads as complex—hard to parse as affection or exhaustion or calculation."

    mara_ellis "That's why the ordinance includes pilot emergency funds and triage criteria. But we cannot let a crisis normalize top-down fixes that displace people."

    jonah_reyes "I know. Just—promise me you won't let the perfect be the enemy of what's needed to keep people safe in the short term."
    "You swallow. The word 'promise' lands like a stone."

    mara_ellis "I won't ignore immediate risk. But I will fight to make the emergency response governed by the same ecological and community standards—to prove it can be done, even in a rush."
    "Jonah Reyes studies your face, then nods. His hand brushes yours momentarily as he passes a printout—nothing overt, but the touch is a tide-press against a shore."

    jonah_reyes "Then let's make sure our pilots include the high-risk zones. If we design them to be quickly deployable yet community-led, we get both safety and stewardship."
    "You both lean into the idea like two people balancing a fragile model. Momentum again—small, precise, cumulative."
    # [Scene: PolySilo Rooftop Garden | Late Evening, After Vote]
    hide mara_ellis
    hide maya_ellis
    hide jonah_reyes

    scene bg ch10_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft laughter, the distant clop of a maintenance boot on metal]
    # play music "music_placeholder"  # [Music: Warm piano with a lifted major chord]
    "The vote is modestly triumphant. The city passes an ordinance that favors nature-based procurement, with pilot funding earmarked for community maintenance and a clause obliging lifecycle ecological metrics in tenders. It is not everything; it is a structure that can grow."
    show councilor_anika_patel at left:
        zoom 0.7

    councilor_anika_patel "This is structural change. It will take time and constant pressure, but it's a foothold."
    show professor_asha_rao at right:
        zoom 0.7

    professor_asha_rao "And a precedent. National think tanks will notice the metrics we've demanded. New Maris can be the case study."
    "Maya hugs you, raincoat damp against your shoulder. Her breath smells faintly of lemon and the rooftop herbs: victory that is small and profoundly earned."
    show maya_ellis at center:
        zoom 0.7

    maya_ellis "You did it, stubborn one."
    "You let yourself smile. Your watch ticks; you press the bezel, feeling ocean-scratched brass warm under your thumb."

    "A national policy group indeed reaches out, requesting a white paper and interviews. Jonah Reyes sends you a photo—grinning, tired fishermen in a pilot community with newly planted marsh mats. The caption is short" "Small wins. Holds tide. For now."
    "You think in lists now: escrow funds, apprenticeships, audits, bench-marked restoration metrics, a public registry of contractors. Each item a pebble into a pond whose rings will radiate outward."

    professor_asha_rao "This will not end the argument. But it reorients procurement language across departments. You made the stubbornness into scaffolding for others to climb."
    hide councilor_anika_patel
    show mara_ellis at left:
        zoom 0.7

    mara_ellis "That's the plan. To make rules that favor the small, the local, the living."
    hide professor_asha_rao
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "And when the season comes, we'll be ready to build where it matters—fast and with care."
    "Your stubbornness, channeled into statute instead of immediate physical construction, feels like a different kind of labor—legal, procedural, patient. The excitement in the rooftop air is soft and steady. You savor it: not a triumphal shout, but a sustained hum of things starting to move differently."

    menu:
        "Draft the white paper with a community co-author":
            "You assign Maya and a neighborhood steward as co-authors, ensuring the national audience hears a local voice. The paper gains credibility and, more importantly, accountability."
        "Fast-track the paper to maximize visibility":
            "You have Professor Asha polish the paper for speed. Visibility spikes quickly; you risk losing some nuance, but the ordinance gets framed as a model while attention is high."

    # --- merge ---
    "Continue"
    "You stand at the rooftop edge, wind tugging at your curls, the city spreading out like a map with its scars and stitches. The ordinance is a beginning—legally binding language that may, if enforced, shift procurement"
    "culture and protect places like the Drowned District in ways that matter beyond immediate storms."
    "You press your thumb against the brass of your watch. It is heavy with history and small enough to hold in the palm like a sealed promise."
    "In your mind, the path forks forward: scale the ordinance into national policy, guard the pilot's integrity against corporate capture, and keep community maintenance not as a checkbox but as a living workforce. The work ahead is long; the wins so far are modest but real."
    "You feel hope rising—not naive, but earned through drafts and hearings and the stubborn insistence that policy can encode care."
    "You fold a final set of notes into your notebook. Outside, rain begins again, a steady, familiar percussion. It will be time soon to return to the Tide Lab, to draft implementation guidelines, to sit with Council staff and with the communities who will be most affected."
    "You breathe, steady, watch ticking at your wrist, and name the next moves in the quiet between heartbeats."
    hide maya_ellis
    hide mara_ellis
    hide jonah_reyes

    scene bg ch10_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: A single, sustaining major chord that promises continuation]

    scene bg ch10_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter11
    return
