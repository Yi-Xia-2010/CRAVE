label chapter14:

    # [Scene: Mixed Construction-and-Garden Site | Morning]

    scene bg ch13_601bcb_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm, ascending strings; soft piano underscoring]
    # play sound "sfx_placeholder"  # [Sound: Distant jackhammers muted by conversations; birdsong returning from planted hedgerows; the low, steady churn of tidewater beyond the forms]
    "You step onto the temporary walkway, the timbers underfoot humming with fresh construction and older, deliberate footfalls. The air tastes of wet cement and rosemary—an odd perfume where industry meets soil. This morning is the proof-of-concept"
    "you argued for, the one that could be read as compromise or salvation depending on where you stand. You carry both labels inside you, though the weight feels lighter now."
    "You remember why you came this route: not for the glossy headlines or the fastest contract, but because policy could make room — legally, financially, administratively — for people to stay, to be compensated fairly, to"
    "shape how the wall meets their streets. You also know what you refused: total erasure in the name of speed. Those refusals echo in the people here, in the hands that chose to plant sedge in"
    "a concrete cavity and the hands that drove rebar before breakfast."
    "Samir meets you at the temporary railing, his vest streaked with salt. He hands you a laminated schematic with sticky tabs and underlines like a soldier presenting maps you already half-know."
    show samir_hale at left:
        zoom 0.7

    samir_hale "We still have tolerances to watch, Mira. Load specs and vegetative buffer intervals. But the oversight clause — the community review board — is signed. Legal's greenlit the relocation escrow, and Etta's team has the first seat."
    show mira_solace at right:
        zoom 0.7

    mira_solace "And Aegis? They're actually doing it your way on the lower bank, not just the upper face?"

    samir_hale "They build things to spec. We handed them a spec that includes a public-access hatch and planted terraces. They complained about costs, but they also priced in the penalties for not meeting the oversight metrics. Bureaucracy can be blunt in the right hands."
    "Your chest relaxes in a way it hasn't for months — not because victory is unambiguous, but because process finally matches intent. The harbor feels steadier underfoot."
    "Arin Voss joins you, camera slung over his shoulder though he keeps forgetting to use it; he watches workers like they are a band of unlikely heroes."
    show arin_voss at center:
        zoom 0.7

    arin_voss "You look like you still expect a storm. Smile for me — for the camera that remembers things later than we do."

    mira_solace "Not yet. I expect paperwork. And the kind of storms policies can weather."

    arin_voss "Fair. But also—"
    hide samir_hale
    hide mira_solace
    hide arin_voss

    scene bg ch13_601bcb_2 at full_bg
    show arin_voss at left:
        zoom 0.7

    arin_voss "—look at that. The shed is on foundation pilings that won't interfere with the flood channel. That's your fingerprint. That's Etta's. That's everyone who showed up."
    "The volunteers nod at you as they pass; someone offers a thermos with sweet, bitter tea. The offer is simple and ritualized — a communal impulse translated into hospitality."

    menu:
        "Accept the tea and walk the terrace with Samir":
            "You take the thermos, the warmth seeping into your palm, and you fall into technical conversation — clarifying inspection schedules, trading shorthand about soil compaction. Samir appreciates the attention to detail and relaxes, divulging a worry about subcontractor timelines."
        "Decline politely and cross to speak with the volunteers":
            "You shake your head and step toward the volunteers. Their hands are raw with work; they tell you short stories about the plants they're saving. You offer corrections about salt tolerance and they laugh at your scientist's stubbornness, then hand you a small sprig of thrift for luck."

    # --- merge ---
    "The narrative continues as the day moves on, the small human things knitting policy and practice."
    "You choose small human things more than grand gestures today — a conversation, a tea, a sprig — because this is how policy breathes: through faces and small bargains. The decision you made to lean on municipal channels has birthed new obligations and new translations between expertise and hope."
    # [Scene: Old Pier Neighborhood | Late Afternoon]
    hide arin_voss

    scene bg ch13_601bcb_3 at full_bg
    # play music "music_placeholder"  # [Music: Gentle guitar picking, low chorus]
    # play sound "sfx_placeholder"  # [Sound: Children trying knots; the muffled radio of a boat from across the channel; the smell of frying fish from a corner vendor]
    "You walk the lanes of the Old Pier, every plank listening. People wave. There is relief etched into faces — not celebratory, not triumphant, but practical: the landlord wasn't forced to tear down his shop, the"
    "elderly neighbor's relocation was paid for with dignity rather than eviction notices. You feel the climb of policy working in real life, and it is messy, human, and sometimes painfully slow."
    "Noah stands outside his repair shop, grease on his forearms, eyes crinkled in that way he has when something important has landed. For a moment he looks nearly your age in purpose."
    show noah_solace at left:
        zoom 0.7

    noah_solace "They put in the buffer next to the slip. Didn't have to move the shop. They said 'mitigation' and I thought they meant scraping us out, but—' (he gestures at the temporary ramp they've bolted) '—this is different. You did good."
    "Mira Solace: (you hear the humility in his 'you did good' as both gratitude and indictment — gratitude because it helped, indictment because it's you who made the calls) 'We did a lot of arguing, a"
    "lot of watching. You did the work here. I just tried to stop them from doing it in the wrong way.'"

    noah_solace "Still, your name hasn't paid the bills. But it kept this place where kids can learn to knot without a permit. Keep pressing, alright? Don't let the fine print be where they push us out."
    "Your throat tightens. He trusts you to keep the line between city-scale fix and neighborhood life intact; that trust feels both heavy and buoying."
    "Etta arrives with a small group — elders, younger gardeners, someone from the review board. She moves slowly, the braided crown of her hair catching the light, her scarves a map of memory. Her eyes sweep the neighborhood like someone counting survivors."
    show etta_maren at right:
        zoom 0.7

    etta_maren "They wanted to put the wall through the schoolyard. You and your friends moved it. You made them listen to our stories. That matters."
    "Mira Solace: (inside, you catalog the quiet sacrifices: a delayed contract here, a concession there; none of them perfect, but each a stitch) 'It matters because people have roots. Roots are maps. We didn't erase the map.'"

    etta_maren "And you asked for eyes on it. That was wise. Keep asking."

    menu:
        "Invite Etta to the oversight meeting tonight":
            "Etta's smile is small but pleased; she accepts, promising to bring stories the board needs to hear. You feel like you've widened the circle."
        "Ask Etta for a list of elders who should be consulted instead":
            "Etta nods, serious. She names people with histories tied to particular alleys and canals, and you realize the weight of representation is not a single voice but many. You tuck the list into your notebook like a talisman."

    # --- merge ---
    "The community's involvement grows as the oversight processes form, and the narrative continues."
    "The Old Pier breathes with cautious optimism. It will not be untouched by the future, but it will remain legible — a place where memory can continue to teach adaptation."
    # [Scene: Construction Site Command Deck (Overlooking the Wall) | Dusk]
    hide noah_solace
    hide etta_maren

    scene bg ch13_601bcb_4 at full_bg
    # play music "music_placeholder"  # [Music: Sustained, hopeful swell with a human chorus]
    # play sound "sfx_placeholder"  # [Sound: Applause, the clink of tools, the ocean a steady basso continuo]
    "The final step is a public signing ceremony — the municipal ordinance that binds the hybrid plan in place. It's bureaucratic and ceremonial in one breath: signatures, a recorded statement, an oath in the municipal register."
    "Liora Kade arrives, immaculate and composed, her brooch catching the light like an emblem both of power and, suddenly, of concession."
    show liora_kade at left:
        zoom 0.7

    liora_kade "This project is a model of partnership. It safeguards critical infrastructure and honors the people who steward these neighborhoods. We learned from community expertise, and we've embedded protections to ensure those voices remain central."
    "Your internal reaction is a palimpsest of skepticism and relief. Liora has the expression of someone who has balanced uncountable costs; you watch for the fissures that tell whether compromise cost too much. Her words are"
    "a kind of olive branch, and you decide — for now — to accept it as what it is: a turning rather than a surrender."
    "Arin Voss steps up beside you, his hand finding yours like a steadying tool. He is quieter than usual, the activist's megaphone replaced with the intimate weight of presence."
    show arin_voss at right:
        zoom 0.7

    arin_voss "You made the city listen. It still frustrates me that their metric was always 'economic center,' but damn—this is better than a wall and nothing else."
    show mira_solace at center:
        zoom 0.7

    mira_solace "Better because it keeps people here rather than pretending they can be fixed later. Better because it's reversible in the places that must be, and permanent where it truly needs to be."

    arin_voss "You make policy sound sexy."

    mira_solace "Don't make me start a TED talk."
    "Liora Kade approaches you after the formalities, briefcase in hand, the coolness of her approach offset by the warmth of the lamps. Her face is unreadable in the best way — complex, not simple."

    liora_kade "Mira. Your insistence on oversight clauses made this a different project. I argued, hard. You argued, harder. I'm not naïve about the compromises made, but I believe we've made something that reduces harm without sacrificing necessary protections."
    "Mira Solace: (you want to ask whether she regrets the people displaced in other neighborhoods, whether she's kept awake by numbers; instead you respond to the action she has taken) 'You kept some of your options open. That made room for people to stay. That matters.'"

    liora_kade "We will be watched. Good. Accountability keeps design honest."
    "Her eyes flick to the crowd, then back to you — an unreadable, layered look that might be respect, calculation, relief, or all of those."

    menu:
        "Ask Liora to join the community review board as an observer":
            "Liora hesitates, then inclines her head. She says, 'If it helps maintain transparency.' Your chest loosens; you sense institutional muscle directed toward a different rhythm."
        "Thank her, but privately tell her the oversight will be community-led":
            "She listens, lips compressed. 'Understood,' she says. Her posture shifts as if recalibrating the ledger of expectations. You feel both guarded and heard."

    # --- merge ---
    "The ceremony concludes and people begin to disperse, moving into the next phase of oversight and care."
    "The sun drops beyond the harbor, and the wall's shadow lengthens like an answer. Not an answer that erases questions, but one that buys time for lives to be steadied."
    "You stand on the platform as people disperse — volunteers returning tools, elders lingering to exchange news, workers laughing as they head to supper. Arin squeezes your hand, the contact simple and anchoring."

    arin_voss "So what's next, Mayor Mira?"

    mira_solace "Next is watching. Next is making sure review processes are actually resourced. Next is helping Noah and others access the relocation fund if they need it, and making sure those who choose to stay have the infrastructure and services to make that choice meaningful."
    hide liora_kade
    show noah_solace at left:
        zoom 0.7

    noah_solace "And keep our slip accessible!"
    "A ripple of laughter follows; you feel like you're both a part of and apart from the machinery of change. It's messy, unfinished, human."
    hide arin_voss
    show samir_hale at right:
        zoom 0.7

    samir_hale "We built guardrails into the budget for community training and maintenance. Not glamorous, but durable. You pushed for long-term staffing, and I think that'll matter."
    "Mira Solace: (you imagine years ahead: seedlings growing in terraces, kids learning to knot on the pier, policy renewal debates that still require hearing room speeches; it's not a forever peace, but it's a durable armistice"
    "between care and commerce) 'That's what I wanted: durability. Not permanence of power, but permanence of practice.'"
    "Etta catches your eye from the crowd. She lifts her hand in a slow, private wave — a seal of approval that feels like weatherproofing for the soul."
    hide mira_solace
    hide noah_solace
    hide samir_hale

    scene bg ch13_601bcb_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Page turned like a small punctuation]
    # play music "music_placeholder"  # [Music: Swell into a hopeful, sustained chord; a soft chorus of voices overlaps in the distance]
    "You close your notebook and tuck it into the pocket by instinct. The harbor hasn't been saved in any mythic sense; storms will come, companies will lobby again, budgets will be cut and then restored. But"
    "the math has altered. There are now legal, financial, and social scaffolds that let communities persist while infrastructure rises. People kept their shops. Elders kept their stories. Children will still learn knots on the pier."
    "You inhale the salt air, and it tastes like work that's been honored rather than erased."
    show arin_voss at left:
        zoom 0.7

    arin_voss "So — stay the night? Rooftop garden's got those lamps you like."
    "Mira Solace: (the invitation is an offer of ordinary future, which feels revolutionary) 'Yes. Stay the night. We'll plant the terrace tomorrow and then sleep like people who have done the thing they could.'"
    "You lean into him; the contact is honest and unornamented. Around you, people are already beginning the mundane labor of living in a stormier world — repairing, rehearsing, guarding one another."
    hide arin_voss

    scene bg ch13_601bcb_6 at full_bg
    # play music "music_placeholder"  # [Music: Gentle, ascending theme with choir-like harmonies]
    # play sound "sfx_placeholder"  # [Sound: Soft laughter, the distant murmur of tide, a cat skittering on a rooftop]
    "You let yourself feel the rise — a gathering of small victories that add up into something larger. There is an ache for what was lost, always; but there is also the surety that people have"
    "been given more space to choose, to stay, to rebuild in the face of rising water."
    # [Scene: Night — Rooftop Common Garden | Later]

    scene bg ch13_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: Intimate piano and soft strings]
    # play sound "sfx_placeholder"  # [Sound: Crickets, distant tide]
    "You and Arin sit shoulder to shoulder, knees touching, the small heat of shared survival between you. The garden smells like mint and damp earth. Above, the city hums, alive and restless."
    show arin_voss at left:
        zoom 0.7

    arin_voss "We did something real, Mira. Not perfect. Not forever. But real."
    "Mira Solace: (you agree, and the agreement is both scientific and sentimental) 'Real enough for now. Real enough to make the next argument from a better place.'"
    show etta_maren at right:
        zoom 0.7

    etta_maren "Keep teaching. Keep making the places where we live legible. That is how you make obligations we can all follow."
    show mira_solace at center:
        zoom 0.7

    mira_solace "We'll make plans and tests. We'll make room for voices. We'll keep watching."
    "As the rooftop lamps blink like tiny constellations, you feel the harbor tilt with you again — not toward a fixed future but toward a field you can tend. Love, too, finds its place among the soils and schematics: steadier, more patient, practiced in repair."
    hide arin_voss
    hide etta_maren
    hide mira_solace

    scene bg ch13_601bcb_8 at full_bg
    # play music "music_placeholder"  # [Music: Final, uplifted chord; then a soft resolve]
    "You close your eyes, letting the last of the evening's warmth press into your lids. There will be meetings tomorrow and the day after, arguments and audits, people who will never be satisfied and people who"
    "will be saved. But for now, the tide is not a tyrant — it is a shared condition we have learned to measure and to work within."
    "You breathe in the salt and plant-sweet air and let it steady you."

    scene bg ch13_601bcb_9 at full_bg
    # play music "music_placeholder"  # [Music: Fade into a hopeful silence]

    scene bg ch13_601bcb_10 at full_bg
    "THE END"
    # [GAME END]
    return
