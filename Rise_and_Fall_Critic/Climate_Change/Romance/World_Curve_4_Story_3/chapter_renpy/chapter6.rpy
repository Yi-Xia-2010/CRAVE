label chapter6:

    # [Scene: Experimental Terrace | Morning — Months Later]

    scene bg ch6_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant chorus of voices, soft applause, the steady slap of a tide-runner against pilings]
    # play music "music_placeholder"  # [Music: Warm strings undercut with a thin, hopeful flute]
    "You stand at the edge of the terrace with salt pressed into the seams of your boots and the satchel—lighter than it used to be—hanging from your shoulder. For months the town moved at the pace"
    "you learned to trust: patient, iterative, communal. Seedlings took root. Raised beds behind the Floodwall overflowed. Jonah’s retrofits were matched by microgrants. People learned the names of the plants you’d suggested; they learned how to bind"
    "cordgrass and how to read a cross-section of a living shoreline."
    "Raff's voice threads through the crowd — bright, performative, proud. Asha wipes damp soil on her sleeves and grins like she’s just pulled a stubborn bulb free. Elder Mae stands a little apart, braid coiling like"
    "a rope around her shoulder, her eyes steady in a way that makes you think of tides."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "You look like you could cry and laugh and give a lecture all at once. Which is it today, Solace?"
    show marin_solace at right:
        zoom 0.7

    marin_solace "All of the above."

    marin_solace "Isn't it—something, seeing this."

    jonah_reyes "It's something we grew."
    "His eyes find yours across the crowd; there is pride and a private, unguarded light there. You savor it, because later, you will understand what having tasted it feels like when it burns away."
    "A small ceremony unfurls: speeches compressed into gratitude, children handing over a ribbon with sticky fingers. Ben Rhee gives a practiced smile and a nod that feels like a strategic endorsement; it carries warmth but also"
    "distance. Lydia Voss, perched at the pavilion’s edge, applauds with the same precision she uses for measures and metrics — polite, measured. The applause fills the terrace until it softens at the edges, held in place"
    "by the murmur of the market beyond."

    menu:
        "Let Jonah take the applause":
            "You lean back and watch him take the small stage, his grin broad as the sky. The town cheers, and for a beat you let the warmth wash over you."
        "Step forward and speak":
            "You step into the light and say fewer words than you rehearsed. You say what matters—accountability, the names of those who did the work—and the crowd listens. For once, they listen like it’s a story they’ve been waiting to hear."

    # --- merge ---
    "The narrative continues."
    "You choose, or you are chosen—either way, the moment is full of the ordinary miracle of people agreeing to try."
    # [Scene: Floodwall & Community Garden | Late Afternoon — Golden Hour]
    hide jonah_reyes
    hide marin_solace

    scene bg ch6_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Bees, distant gulls, the creak of old wood]
    # play music "music_placeholder"  # [Music: A single cello phrase, patient]
    "You walk the Floodwall with Jonah at your side. Community-painted murals crown the concrete; someone has stenciled a list of names where donors and volunteers met in the rain. Asha is kneeling in a bed, ceding"
    "a joke to a passing child. Raff, camera already around his neck, bumps thumbs with someone who filmed the terraces and is now uploading a clip."
    "Ben pulls you aside for a brief word—a murmured check-in about paperwork, permits, an expected press release. He looks at the terraces, then at the line where the wall meets the inlet, and his smile falters for the sub-second it takes him to measure risk."
    show councilor_ben_rhee at left:
        zoom 0.7

    councilor_ben_rhee "We still need that inlet survey logged. The engineering team said low priority—"
    show marin_solace at right:
        zoom 0.7

    marin_solace "We postponed it until after the pilot's six-month review. We had reasons. The cooperative needed to show proof."

    councilor_ben_rhee "Proof matters in lots of currencies, Marin. The council knows that."
    "His glance contains the corridors of bureaucracy you’ve learned to navigate—the places where tenacity and favor meet. You nod; you know what he's implying without needing the rest of the sentence. Outside, the town hums around"
    "you: kids running boats along a drained channel, an elder pointing to a plant and giving it a name in a language older than policy."

    menu:
        "Ask Jonah to walk the inlet with you":
            "You ask. He nods and his hand finds the small of your back, guiding you toward the inlet. There’s a steadying squeeze—practical and intimate."
        "Make a note to call Asha after the meeting":
            "You pull your satchel open and thumb a page. It’s bureaucratic—necessary—and your fingers feel the old, present weight of responsibility."

    # --- merge ---
    "The narrative continues."
    # [Scene: Experimental Terrace | Night — The Storm]
    hide councilor_ben_rhee
    hide marin_solace

    scene bg ch6_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind scouring across pilings, a new, higher tone of alarms — both human and electronic]
    # play music "music_placeholder"  # [Music: Pulsing low strings; a distant, anxious heartbeat of percussion]
    "The forecast tightened over the previous days—warnings that arrived like thin paper notes—but this storm folds differently into the bay. It comes with a suddenness that makes the map on your satchel look like an argument"
    "you were still assembling. A surge hits an inlet that had been on your list of 'nexts.' The culvert on the contractor-approved property—something you and Asha wanted studied—collapses. You feel the first shove of cold water"
    "like a betrayal against your palms."
    "Raff's clip is swift and terrible: pulsing water rips along a fringe of newly planted terrace; roots, still young, come loose and furl against the surge like pale flags. The footage spreads—staccato pings from phones, the low thud of the town watching itself unravel."
    # play sound "sfx_placeholder"  # [Sound: Rapid notifications, muffled shouts, the metallic groan of failing fastenings]

    scene bg ch6_3be532_4 at full_bg
    show rafferty_raff_cole at left:
        zoom 0.7

    rafferty_raff_cole "It looked stable—Marin, it looked—' (voice breaking) 'It didn't take. People are uploading it. Investors are calling."
    "You hear the word 'investors' like a bell toll. Payments freeze. Staged releases delay into audits. Lydia Voss's communications team moves quickly—a clinical, precise set of statements that fold fault onto the 'experimental' nature of the pilots."
    show lydia_voss at right:
        zoom 0.7

    lydia_voss "These pilots were essential proofs-of-concept. We supported the cooperative’s innovation. However, in the face of immediate regional risk, centralized engineering is an imperative. We must prioritize rapid, durable solutions."
    "Her words are a scalpel. They are not untrue; but the tilt of them—toward centralization, toward urgency couched in certainty—sits on the other side of your chest like a stone."
    "Ben convenes an emergency meeting. The council room is too bright, all glass and problem-solving inflection. Phones crowd the table. On the screen, investors’ faces harden. In the lobby, a few townspeople gather, watching, aghast. You"
    "feel the applause from the morning recede in memory, a tide running out, showing the tar and mussel shells beneath."
    show marin_solace at center:
        zoom 0.7

    marin_solace "We had contingency clauses. We asked for a moratorium on further construction adjacent to the inlet until a full survey—"
    hide rafferty_raff_cole
    show councilor_ben_rhee at left:
        zoom 0.7

    councilor_ben_rhee "And we have clauses, Marin. We also have a collapsing emergency with headlines already trending. The region's risk officers are—"

    marin_solace "We asked to study that inlet months ago. I asked. It wasn't prioritized."

    councilor_ben_rhee "I know. I know, and I don't want to share blame. But right now, people want reassurance. The language that calms them will shape the response."
    "The room is full of people speaking other people's languages—contracts, audits, headlines. You feel suddenly like a small boat in a crosscurrent, the world’s words battering your sides."

    menu:
        "Call Asha and coordinate damage control":
            "You pull the satchel to your chest, thumb finding the page with the cooperative’s emergency checklist. Asha's voice is steady even when yours cracks; together you triage and move through the night."
        "Answer Lydia's incoming call directly":
            "You take the call. Her voice is cool, strategic; she offers a staged PR narrative. You want to be measured. Instead, your words come out raw—because the terraces are bleeding and you are tired of measured language."

    # --- merge ---
    "The narrative continues."
    "The social feed bleeds into the council room. Footage, opinion, rage. Lydia Voss's release reshapes the public argument into a single, pressing demand: fast, centralized fixes now. Investors look at spreadsheets and timelines and, finding uncertainty, pull back."
    hide lydia_voss
    show asha_patel at right:
        zoom 0.7

    asha_patel "We built in increments so we could learn. We left room to adapt. We never meant—"

    marin_solace "We meant to do better. We still do."
    "Jonah Reyes stands with you, hands scarred with rope and salt. He is practical, already tallying what can be saved. His voice is low."
    hide marin_solace
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "We can shore where the water took. We can try to anchor those beds before morning."
    "You hear the plea in the sentence—action as love. You also hear the cost: time you might not have, resources that are frozen in accounts elsewhere, and a public that has been swayed by a narrative of failure."
    # [Scene: Market | Next Morning — Grey, Behind the Floodwall]
    hide councilor_ben_rhee
    hide asha_patel
    hide jonah_reyes

    scene bg ch6_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Muffled conversations, the occasional angry whisper, the rasp of a vendor folding a shutter]
    # play music "music_placeholder"  # [Music: A single minor-key piano, sparse]
    "The market's folksong that once mentioned your cooperative now trades in quieter lines—questions instead of praise. Some people cross the path you walk; some avoid your eyes. Raff's clip rolls on repeat for those who already"
    "saw it and for those seeing it anew. In the pavilion, Lydia Voss's statements make their rounds, quoted in the paper, in comment threads, in small groups by the fishmongers."
    "Elder Mae finds you by the raised garden beds. Her hands smell of soil and smoke. She looks at the damaged terraces without flinching; her expression is neither accusation nor absolution but a long, slow calculation that seems to take all of time."
    show elder_mae_hargrove at left:
        zoom 0.7

    elder_mae_hargrove "You asked the sea for a covenant and it asked back. How you answer that is the thing that will mark you."
    show marin_solace at right:
        zoom 0.7

    marin_solace "I—' (you feel the pressure of every name you carry, every promise folded into the satchel at your shoulder) 'I asked for shared responsibility. I thought shared responsibility would be enough."

    elder_mae_hargrove "Shared responsibility is a practice. It looks different in storm and in sun. Have you been practicing how to grieve what was lost?"
    "The question cracks you like cold sea on bone. Grief is not a checklist. It has fewer lines than a permit and more edges than a design drawing."
    "Ben approaches—his tie undone, the suit sleeves damp at the cuffs—his political calculation now edged with the tiredness of someone whose job is to keep a town from breaking into worse pieces."
    show councilor_ben_rhee at center:
        zoom 0.7

    councilor_ben_rhee "There will be hearings. There will be reviews. The council can press for repair funds, but investors—"

    marin_solace "Investors freeze. Lydia frames the pilots as liabilities. The town loses ownership of the narrative."

    councilor_ben_rhee "You didn't trifle with it. You put your name on plans people trusted. That counts."
    "You take in their faces—Jonah Reyes's, full of practical sorrow; Asha's, furious and tender; Raff's, exhausted from the performance of crisis; Ben Rhee's, carrying the calculus of a town under pressure; Lydia Voss's, offscreen now, efficient,"
    "a statute of authority. Their reactions are complex—no simple portrait of love or hate. The 3-Check rules hum under your skin: some things you cannot assume, some you must pivot from."
    "You taste iron and salt and feel a hollow open beneath the place where the peak once sat. The applause of months ago feels like a distant shoreline you watched recede. You cradle that memory like a thing that was true and now is waking to ruin."
    "You think of the cooperative's founding—late nights in the Saltworks, the patchwork strategies, the steering committee's hands on tide charts. You think of the clause you insisted on, the mooring rights you fought for, the small"
    "oversight bodies you demanded. You think of the people who trusted you and of the children who still play at the terrace's lee. The ledger of outcomes is not neat. Something fundamental has shifted."
    "A hush falls over a small circle near the market. Jonah Reyes squeezes your hand. He doesn't say leave or stay; he offers steadiness. You realize every route forward will bear cost—of reputation, of livelihoods, of the town's trust."

    elder_mae_hargrove "There is a long work after loss. Pride will not do the planting. Shame will not do it either. You choose what kind of work you will be, Marin."
    "You breathe, lungs tasting of iron and salt and the damp fur of the day. In your satchel the maps are creased; in your palm your lighthouse pin is warm from your touch. You consider what it means to hold responsibility and to let go of control."
    "You think of Lydia Voss's neat sentences and of the way the region will pivot toward a single, fast narrative if you do not offer one of your own. You think of the cooperative—its members, their"
    "homes, their names—and you know that the way forward cannot be the same as the way you imagined."
    "There is no applause now. There is only the long, patient work after failure: repairing, documenting, tending the social and ecological wounds. You can stay at the helm of a group that will be judged for this night, or you can make a different choice about what stewardship means."
    "You close your eyes for a breath and let the taste of salt and metal wash the air clean of simpler illusions."
    # play music "music_placeholder"  # [Music: A minor chord held and then released into a single, low, clarinet note — unresolved but intimate]
    hide elder_mae_hargrove
    hide marin_solace
    hide councilor_ben_rhee

    scene bg ch6_3be532_6 at full_bg
    "You turn the lighthouse pin between two fingers, the enamel chipped but intact. It is small and ordinary and keeps you steady. You lift your head. The town's future will be argued in council rooms and"
    "in headlines, but the work at the margins—the gardens, the terraces, the mending of neighbors—will be where life actually goes on."
    "You let your hand fall away from the satchel and make up your mind in the only way that feels honest: not to save the narrative for appearances, but to save the labor for people."
    "You will step down from your leadership role in the cooperative."
    "You will not vanish. You will take the lessons, the grief, the embarrassments, and the small victories, and you will start a movement for decentralized, mobile knowledge—teams that travel to other towns, that teach, that do"
    "the messy work of adaptation at community scale. It will be less clean, less fundable at first, but it is work you can sleep beside."
    "You tell Jonah Reyes in a whisper that you will not stop fighting for Havenpoint. You tell Asha you want the cooperative to keep its name, its mission. To Raff, you hand a list of places to document—people to speak to, hands to film, stories to keep alive."
    "Elder Mae squeezes your hand once, twice, then pulls you into a slow, earth-smelling embrace that smells of cedar and rain. Ben Rhee shakes your hand with a formality that contains gratitude and the thinness of"
    "political theater. Lydia Voss's office releases another measured statement into the world; you read it once, then fold it away."
    "The town will judge you one way or another. Some will call you noble. Others will call you naïve. Both may be true."
    "You stand on the Floodwall where the community garden catches the low light and listen to a child laugh in the distance. The terraces will be repaired in time. The pilot will be audited and dissected"
    "and, maybe, used as a map by others. But the climbing you did is not erased; it is rewritten into a new form—smaller, less showy, more itinerant."
    "You do not feel triumphant. You feel raw and tired and, in a way that will have to be enough for now, ready."

    scene bg ch6_3be532_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade out slowly into the sound of soft rain]

    scene bg ch6_3be532_8 at full_bg
    "THE END"
    # [GAME END]
    return
