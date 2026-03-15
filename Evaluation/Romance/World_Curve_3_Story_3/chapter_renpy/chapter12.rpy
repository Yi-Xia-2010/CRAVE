label chapter12:

    # [Scene: Municipal Hall | Early Morning]

    scene bg ch12_3be532_1 at full_bg
    # play music "music_placeholder"  # [Music: Low hopeful strings; a steady, warming pulse]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the muffled clack of boots on wet pavement, breathy murmurs from volunteers setting up chairs]
    "You arrive before the crowd. The hall is quieter in the hour before everyone files in—the air still, the fluorescent bulbs humming like a held note. Your tablet is a hard weight against your palm, its"
    "cracked corner taped but full of files you have spent nights stitching together: sensor logs, timestamps, a ledger of missed dispatches, the names that give the pattern a face. The brass tide-watch at your wrist keeps"
    "to its little relentless rhythm; when you look at it you want to fold time into something useful."
    "Your chest is a room that has hosted many small panics and one long, necessary resolution. You think of the way postponement looked in the data: signals delayed, alerts queued and dropped, resources routed to different"
    "priorities. You don't pretend the exposure will be painless. This is not about revenge; it's about preventing another avoidable loss."
    show rita_ortega at left:
        zoom 0.7

    rita_ortega "You don't have to read everything. You can summarize—hit the pattern, then let them dig."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Summaries get lost in headlines. I want the ledger. I want the names next to the missed times. People deserve to hear the scale honestly."
    "Rita's fingers tighten on your shoulder, brief and fierce. She nods, then fusses with a stack of printed materials as if she can iron the creases out of fate."
    hide rita_ortega
    hide maya_reyes

    scene bg ch12_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Paper rustle, a microphone being positioned nearby]
    "You taste metal—fear, coffee, the salt air of Marisora's memory—and you let it ground you. You are not naive: corruption is rarely cleaned by truth alone. But truth has a physics of its own here; it can rearrange alliances, demand responsibility, make systems bend. You breathe. The strings swell, patient."
    # [Scene: Press Conference | Midday]

    scene bg ch12_3be532_3 at full_bg
    # play music "music_placeholder"  # [Music: Quiet brass swells into a steadier, cleansing motif]
    # play sound "sfx_placeholder"  # [Sound: Murmurs, the click of cameras, a reporter clearing a throat]
    "You step up to the microphone. The wind lifts a stray strand of hair into your face; you brush it away and the movement feels like making space for what you will say."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "Thank you. I am Maya Reyes. I am from Marisora. Tonight I will read from an audit of the alert system and the municipal dispatch logs."
    "You feel the weight of all those faces—some expectant, some searing with blame, some simply there because this is how a town measures itself. The first lines you read are clinical and small: timestamps, signal IDs."
    "Then the pattern emerges when you read the timestamps in sequence: delays of minutes that become hours, alerts rerouted with no recorded justification. You read names—operational handles, dispatch officers—only because the ledger connects people to choices."

    "Reporter" "Are you accusing specific individuals?"

    maya_reyes "I'm presenting the records so that the pattern can be seen. This is not about individuals in the abstract—it's about how systems failed when they were needed."
    "A camera pans to Dr. Ayla Voss standing just to the side, face composed beneath that precise bob. For a moment you brace for an immediate collision—she has the machinery of the region behind her—but instead she steps forward, hand lifted in a gesture that is careful as a surgeon's."
    show dr_ayla_voss at right:
        zoom 0.7

    dr_ayla_voss "Maya's documentation is accurate. The regional office will cooperate with the inquiry. Transparency is our obligation."
    "The words land like a surprising warmth. There is awkwardness in the way she says 'our'; it doesn't flip the night into gentle light, but it buys the town something it has been starved of: official momentum."
    "Your internal voice sharpens: alignments like this are rare and must be stewarded, not assumed. You answer another reporter, letting your voice carry the practice of numbers and consequence."

    maya_reyes "We are calling for a regional inquiry. We need full dispatch logs, audit trails, and an independent review of funds and directives. And we need a humane relocation protocol—if relocation is necessary, it must be dignified and include cultural preservation."
    "Mayor Tomas appears and, with a public face, nods. The crowd shifts; someone shouts a question that lands like a stone. You lift your gaze and see Elias Jun beneath the crowd—hands shoved into his paint-splattered pockets, eyes narrowing not in anger but in the stubborn attention you know well."

    menu:
        "Read the names of dispatchers aloud":
            "You clear your throat and read each name slowly, the syllables falling into the press like discrete stones. The crowd goes still; some faces contort with recognition and betrayal. A mother two rows back wipes her eyes and grips the shoulder of the person next to her."
        "Summarize the pattern without names":
            "You present the pattern—the delays, the re-routings, the ledger’s numerical heartbeat—without tying it to individual names. Reporters squint into their notes, and murmurs swell; some in the crowd murmur relief, others frown with a sense that something necessary has been withheld."

    # --- merge ---
    "Narrative continues"
    "You finish by calling for the inquiry. Cameras flash; someone shouts that they hope it will be quick and decisive. The strings climb into something like resolve."
    # [Scene: Municipal Hall / Hearing Room | A Week Later]
    hide maya_reyes
    hide dr_ayla_voss

    scene bg ch12_3be532_4 at full_bg
    # play music "music_placeholder"  # [Music: A steady, clean piano line; hope tempered by gravity]
    # play sound "sfx_placeholder"  # [Sound: Tiny coughs, a gavel's soft rap, the hush of a room leaning in]
    "The inquiry convenes. You sit across from Dr. Ayla Voss at the witness table: two different methods of care toward the same endangered thing. The hearing is procedural, the kind of public rubbing that leaves rawness where quiet dishonesty once lived."

    "Lead Investigator" "Ms. Reyes, can you explain what your data shows about missed dispatches?"
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "The logs show a pattern of alert suppression and rerouting during critical windows. Certain directives delayed automated escalation protocols. The result: alerts that should have escalated to regional responders were logged as lower priority, and some notifications never reached teams in time."

    "Investigator" "Dr. Voss, were you aware of these protocols being altered?"
    show dr_ayla_voss at right:
        zoom 0.7

    dr_ayla_voss "There were policy adjustments communicated through the regional office. At times, those changes did not translate into clearer documentation at the operational level. That is on the region's oversight."
    "The exchange is polite but sharp. Question after question, you speak and then watch the room measure your words. Dr. Ayla Voss answers with the uncomfortably precise language that has been her armor. At one point,"
    "when a councilmember suggests incompetence rather than malice, Dr. Ayla Voss's jaw tightens with a look that is, briefly, human: someone defending a system that has failed those it served."

    maya_reyes "Accountability isn't a single person being punished. It's structural: corrected protocols, audited oversight, funding redirected to ensure alerts cannot be dampened by bureaucratic convenience."

    "A counsel pushes back" "If we call for relocation protocols, are we conceding defeat—letting communities be moved rather than protected?"

    maya_reyes "Relocation, when necessary, must be humane. It is not surrender. It is the final act of stewardship for rather than abandonment of a culture: preserving stories, artifacts, livelihoods."
    "Dr. Ayla Voss watches you argue the humane framing as if she's measuring an unfamiliar weight. After the session, she stays behind to speak with you alone in a corridor that smells faintly of lemon cleaner and paper."

    dr_ayla_voss "I can't apologize for the system's choices, Maya. But I can insist on the machinery to make this right. I will push for the resettlement trust, the cultural preservation funds. I will use the channels that I have—if you'll keep using the credibility you have here."
    "You feel the rare, fragile convergence: science-steward and political operator agreeing that the town's dignity must be preserved. It doesn't erase all the bitterness of exposure; it simply wires forward a plan where accountability is paired with compassion."

    maya_reyes "We expose. We demand a transparent audit. And we build a resettlement protocol that includes funding for traditions, for seed banks, for community councils to maintain voice."

    dr_ayla_voss "I'll make sure the funding stipulates that. No top-down erasure."
    "Your chest loosens a fraction. It is not comfort, but a kind of necessary, rising certainty."

    menu:
        "Intervene when a councilmember suggests punishment":
            "You step forward, voice steady, and restate the difference between accountability and vengeance. The room quiets; some nod, others shift uncomfortably. You sense the conversation moving from blame to systems change."
        "Stay silent and let the procedural experts argue":
            "You keep your hands folded and let the experts swing at each other. The inquiry runs long; some arguments harden into partisan divides you will later spend nights undoing."

    # --- merge ---
    "Narrative continues"
    # [Scene: Relocation Zone / Harbor Staging Area | Dawn, Weeks Later]
    hide maya_reyes
    hide dr_ayla_voss

    scene bg ch12_3be532_5 at full_bg
    # play music "music_placeholder"  # [Music: Gentle, rising strings with a lullaby undertone]
    # play sound "sfx_placeholder"  # [Sound: Engines idling, the thump of a crate being lowered, the soft chatter of neighbors trading practical instructions and trembling jokes]
    "Relocation is a word you learned to carry with both tenderness and steel. The plan that emerged from the inquiry is not cold; it is choreographed to preserve what makes Marisora Marisora. Cultural preservation funds mean"
    "the town's murals will be moved, elders' recordings cataloged, the community greenhouse's heirloom seeds crated and shipped with care."
    "Elias Jun stands by a stack of mangrove saplings, mud already sketched in the creases of his palms. He has been spearheading ground projects in the new site—planting the first buffers, training relocated fishers in modified,"
    "viable nets. He looks at you with a quiet eagerness: the kind that builds things from the ground up."
    show elias_jun at left:
        zoom 0.7

    elias_jun "They told me to make the new shores feel like home. I thought—start with roots. These saplings will be small when they go in, but they'll be stubborn."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "You always root for stubborn things."
    "He grins, that quick crinkle at the eyes. You both know what the coming months will mean: separations, phone calls timed to tides, a partnership stretched across the geography of necessary work."

    elias_jun "I'll send pictures. You send plans. We argue about which species to prioritize. Then, one day, we go plant together and remember how ridiculous we sounded at the start."
    "You laugh—a short, bright sound that tastes of relief and salt. You fold a small cedar box into your hands: artifacts, small tokens given to families to carry forward. Each crate marked for a household feels like a blessing and a wound."
    "You hug more people than you can count—neighbors who are not leaving, friends moving with dignified resolve, elders who pass you a weathered charm. Elias Jun and you stand apart for a long moment, feeling the weight of the goodbye that is also a beginning."

    elias_jun "We could try the commute. I'm not good at airports—but I will learn."

    maya_reyes "I'm not good at staying still. I will build something that makes coming back feel like crossing a shorter distance."
    "There is an ungainly tenderness in the promise: logistics wrapped in emotion. It will not be simple. It will be honest."

    menu:
        "Ride in the first convoy to the new site with Elias":
            "You climb into the truck with Elias, dust and diesel on your jacket. The road is long and the horizon rearranges itself. You watch familiar coastlines recede and feel both the sting of leaving and the solidness of purpose."
        "Stay behind to coordinate the transition from the hall":
            "You remain, organizing manifests, ensuring funds are released and cultural inventories are complete. Your hands are on the throttle of the town's logistics—less romantic, but every bit as vital."

    # --- merge ---
    "Narrative continues"
    # [Scene: Rooftop Watch at Dusk | Several Months Later]
    hide elias_jun
    hide maya_reyes

    scene bg ch12_3be532_6 at full_bg
    # play music "music_placeholder"  # [Music: Warm piano and strings resolving into a soft, luminous chord]
    # play sound "sfx_placeholder"  # [Sound: Wind through the herbs, a distant gull, the faint ping of a message arriving]
    "You are alone on the rooftop, but the absence is not the hollow you feared. It is full of the things you did: the hearings, the press, the long nights cataloging logs. Your tablet chimes; a"
    "photo appears. Mangrove saplings in a neat row, mud still glistening on the leaves. Elias Jun's thumb in the corner of the frame, smiling with the earnestness of someone who makes things happen with his hands."
    "You press your palm to the tide-watch and let its small tick keep you company. There are letters from families who moved—thank-you notes folded with small drawings and recipes. The resettlement trust funded a community center"
    "designed by the people it serves; there are images of elders teaching children songs that sound older than any policy document."
    "Your throat tightens in the way sorrow can when leavened by relief. Lives were safeguarded because you chose exposure over silence. People left some of their doorframes behind; they also took the seed bank and the stories. The town changed shape, but it did not die."
    "You think of Arias in the inquiry, of Mayor Tomas negotiating the funding, of Rita organizing schedules and small kindnesses. Accountability has consequences: some people were moved against their preference, some livelihoods had to be adjusted,"
    "and the memory of the loss is a living thing in every conversation. Regret is a companion; it will always be part of this work. But the arc of the months—painful, relentless, principled—has led upward into"
    "something like moral clarity."

    "Your phone buzzes again: a short voice message. Elias Jun" "We planted the first buffer line today. It looks ridiculous—like a tiny green comb against a huge grey. But it'll hold. It already has us. Come out sooner if you can. Or I'll come back with mud in my pockets and tell you about every ridiculous thing we did."
    "You smile, cheeks damp in the rooftop light. You leave a message in return—practical, full of dates and plans and a thin thread of longing that is not regret but a steady tether."
    "You stay on the roof until the string lights hum on and the tide-watch's brass grows warm under your palm. Below, Marisora breathes: new permits stamped, new hires at the resettlement trust, a rotation of people"
    "learning new trades, elders teaching songs from their porches, children in the new community center learning the old festival steps."
    "There is sorrow braided through the town's threads; there is also a rising confidence that work done openly, honestly, with respect for both data and dignity, can save lives. You have learned to make hard calls"
    "objectified by process and softened by ritual: moving murals, gifting seeds, creating catalogues of story."
    "You think of the future not as a single endpoint but as a practice: tending mangroves, revising protocols, visiting, planting, building. You are part of a long conversation now—between people, places, and time."
    "You lift your face to the dusk and let the wind, salt and soft, move the loose waves of your hair. The strings swell into a hopeful, quiet resolve. Your hands rest on the tide-watch; you"
    "let its ticking remind you that time keeps moving whether we act or we wait. You chose action. The town moved with you."
    # play music "music_placeholder"  # [Music: Strings resolve into a warm major chord; a soft, sustaining note lingers]

    scene bg ch12_3be532_7 at full_bg
    "You accept that some loves endure across miles. You accept that saving lives sometimes means letting the shorelines of your life redraw themselves. You accept the compromise and the clarity of the choice you made: exposure, accountability, sacrifice—for the safety of the many and the dignity of the few."
    "You close your eyes for a beat and, when you open them, the horizon is still there. You breathe, and it feels like the first clean thing you've done in a long time."
    # play music "music_placeholder"  # [Music: Fade into soft ambient sea sound]

    scene bg ch12_3be532_8 at full_bg

    scene bg ch12_3be532_9 at full_bg
    "THE END"
    # [GAME END]
    return
