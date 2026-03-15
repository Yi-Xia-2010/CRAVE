label chapter41:

    # [Scene: Rooftop Nursery | Early Morning]

    scene bg ch15_16e9b2_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft chatter, the distant drone-bleep of tide sensors syncing; a kettle hisses somewhere below]
    # play music "music_placeholder"  # [Music: Low, steady ambient hum — a minor key cello undercurrent]
    "You arrive before most of the neighborhood is awake. The city is a slow inhale — gull calls threaded with the far-off thump of a maintenance barge — and the rooftop smells like wet soil, moss,"
    "and the bitter citrus of leftover coffee. Your palms still remember how to graft sedge from the terraces; your fingers find the same notches in the planting benches as they always have. Habit is a kind"
    "of prayer now."
    "Rafi is there already, sleeves rolled, teaching two teenagers how to tie a knot that will hold under salt and wind. His voice is warm but weathered; his laugh breaks in the middle sometimes, like a rope that's been frayed and knotted too many times."
    show rafi_odeh at left:
        zoom 0.7

    rafi_odeh "Same as before — roots down, clamps tight. Make it stubborn. Make it want to live."
    show maya_corvin at right:
        zoom 0.7

    maya_corvin "If the sea wants it out, stubborn won't be enough."

    rafi_odeh "Stubbornness ships with us. But you know that. You always did."
    "A silence falls that is not comfortable; it's necessary. Lio appears at the rooftop edge, paint-streaked hoodie zipped up high, hands tucked as if to ward off more than the morning chill. He points, not with"
    "mockery but with the tired precision of someone who has spent too many nights on a ladder."
    show lio_corvin at center:
        zoom 0.7

    lio_corvin "Maya — look. The old promenade? The paint's coming back in places. Took a hit last month, but the murals keep fighting."
    "You step closer to the railing. The horizon tilts between reclaimed marsh and engineered barrier; where the two meet, water has chewed irregular scars into concrete. You feel a low, familiar ache—like a bruise you can't"
    "stop checking. The gardens are feeding market stalls now, but their yields are narrow and the season short. The work keeps people fed, not safe. The city bought time. Time bought compromises. Compromises bought lives. Each"
    "transaction leaves a ledger you can read on your skin."

    lio_corvin "People ask if you're proud. I don't know what to tell them. We're cobbling a life out of other people's blueprints."

    maya_corvin "Pride gets selfish when the cost is other people's roofs. But it's not nothing — we keep the stories in paint and soil. That's something."

    rafi_odeh "Something is what we have. It's all we have sometimes."

    menu:
        "Check the sensor feed on your tablet":
            "You pull your tablet from the pocket of your jacket. The tidal graph blips gently; a line you've watched for years is still jittering in the same old places. You tap through the logs — maintenance notes, a flagged alert from last month. It's a small, contained worry. You close the app and set the device on the bench like a talisman."
        "Kneel and press a seedling into the soil":
            "You lower yourself to work with your hands. The soil is cool under your knuckles; a child's scrawl is visible on the crate nearby. You press the roots in and feel them take. The motion steadies something inside you, and the rooftop sounds sharpen — the scrape of a trowel, Rafi's humming."

    # --- merge ---
    "Continue"
    # [Scene: Reworked Promenade | Late Afternoon]
    hide rafi_odeh
    hide maya_corvin
    hide lio_corvin

    scene bg ch15_16e9b2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Water faring against mixed materials; the metallic groan of the adjustable sluice; distant laughter filtering from a market alley]
    # play music "music_placeholder"  # [Music: A steady, sparse piano line — contemplative, unresolving]
    "You come down to the promenade when the light flattens and the concrete's edges look raw and surgical. The hybrid coastline we bought is obvious in its incongruity — a neat concrete seam beside the bulging,"
    "fibrous line of living marsh. Some days it holds. Some days it groans and you can feel the city exhale."
    "Camila 'Kai' Navarro is there — professional, precise, untouched by the salt on her cuffs. She stands at a distance, watching the water with the particular assessment of someone used to measuring problems by curves and"
    "failure rates. When she sees you, her face relaxes into something that is almost a private truce."

    "Camila 'Kai' Navarro" "The sluice adjustments we made last season held up better than expected. The monitoring nodes are stable — at least for the bandwidth we negotiated."
    show maya_corvin at left:
        zoom 0.7

    maya_corvin "Bandwidth is a euphemism for how much they'll let us know before they tell themselves it's enough."

    "Camila 'Kai' Navarro" "It isn't perfect. But interventions had to happen quickly. Waiting would have been—"

    maya_corvin "—waiting would have been the same as letting people lose more than they already have. I know why you move fast, Camila 'Kai' Navarro. I do."

    "Camila 'Kai' Navarro" "And I know why you push for roots. You make things human where I make them whole. Neither of us gets to be the only truth."
    "The air between you is complex. Camila 'Kai' Navarro's face shows a flicker — not quite regret, not quite satisfaction. She's a person who has learned to keep the soft things private. You have learned to"
    "read the small concessions. Both of you are, in different faiths, trying to keep the city from eroding."

    "Camila 'Kai' Navarro" "If a breach widens this winter, we will call for emergency reinforcements. We'll talk about funding then. If not, we'll try preventative sedimentation again."

    maya_corvin "And if the money dries up?"

    "Camila 'Kai' Navarro" "Then we'll find another way. Or we'll bottle what we can and move people. Either way, we won't be the ones who say it was an easy choice."
    "You look at the water and feel the cold creep up your spine. The promenade isn't victory; it's a promise inked in pencil."

    menu:
        "Tell Kai she can call on you if emergency forces are needed":
            "You nod and keep your voice steady. 'If it comes to that, I'll organize shelters and volunteers.' Kai lists off a data request in return; it's business, but you both understand the barter."
        "Tell Kai you won't be part of municipal emergency plans that displace people":
            "You hold her gaze. 'I won't help move people so profit can land elsewhere.' She blinks, a micro-gesture that looks, for a second, like surprise. The conversation cools into a policy argument you'd both rather not have."

    # --- merge ---
    "Continue"
    # [Scene: Market Stalls | Midday]
    hide maya_corvin

    scene bg ch15_16e9b2_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Vendors calling, coins clinking, a child shrieking with laughter; the undercurrent of a public address repeating a municipal notice]
    # [Smell: Fried fish, compost, and a citrusy antiseptic used to clean the communal tables]
    # play music "music_placeholder"  # [Music: A low guitar motif — nostalgic, unresolved]
    "The market is less celebratory than survival with color. The stalls feed the neighborhood and attract the odd tourist who wants an artisanal sea-salt cracker. People you know nod at you with the careful gratitude of"
    "those who still expect storms. Lio is haggling with a vendor over the price of paint; his energy is bright but frayed at the edges."
    "Elias Kahn arrives with a bag of municipal forms and the soft exhaustion of someone who sleeps in hotels and calls home on the move. He is steadier than most, but time has creased him in"
    "new places. You watch him come and feel both warmth and a hollow where plans unmade whisper."
    show elias_kahn at left:
        zoom 0.7

    elias_kahn "You're up early. Lio's murals are getting famous, apparently. The heritage tours mentioned them in a city brief."
    show maya_corvin at right:
        zoom 0.7

    maya_corvin "Great. I always wanted our grief to be a tourist attraction."

    elias_kahn "They brought attention. Attention is currency."

    maya_corvin "And currency told them what to protect."

    elias_kahn "I tried to make it balanced. We have to be pragmatic —"
    "You cut him off before he can finish. You have listened for years to the language of compromise; your body knows its grammar."

    maya_corvin "Pragmatic used to mean making room. Now it feels like making room for a thing called 'acceptable loss.' I don't know what acceptable looks like when it's people you've known your whole life."

    elias_kahn "I know. I remember the nights we sat in committee. I remember Lio's painting and Rafi's hands in the dirt. I carry that with me when I do the math."
    "You pause, because his words are both shelter and an accusation. It is possible to carry grief and still write budgets. It is possible to love people and still advocate for systems that hurt them in"
    "the short term for a slightly safer future. Both facts sit in your ribs like lead."

    elias_kahn "We're trying to make a way that keeps the neighborhood here, not a museum of what used to be. I travel because that's where the leverage is. It isn't distance from you. It's the opposite—"

    maya_corvin "It's also distance from the dirt."
    "He reaches for your hand across the stall, a practiced motion that has become a small ritual. Your hand finds his; it's warm, callused from a different sort of work — policy papers instead of seedbeds. You squeeze, and it's ordinary and fragile and necessary."

    elias_kahn "We make our own imperfect practices, Maya. That's how love lasts."
    "You look at the markets, the hands exchanging money, the murals that keep telling the story. It does not feel triumphant. It feels like a bandage stitched loosely over a still-bleeding wound."

    menu:
        "Invite Elias to help oversee tonight's volunteer shift":
            "You say it casually, but your heart hammers. He nods and writes it down among the forms in his bag. For once, bureaucracy and soil share a small page."
        "Tell Elias you need him to slow down and be here more":
            "You ask him plainly. He shifts, that city-schooled guilt folding into his voice. 'I can't always,' he says. 'But I will when I can.' It's not enough, but it is an offering. You accept it and let the ache sit."

    # --- merge ---
    "Continue"
    # [Scene: Independent Board Hearings | Evening]
    hide elias_kahn
    hide maya_corvin

    scene bg ch15_16e9b2_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A muted murmur that snaps to silence when the chair calls the meeting to order; the low buzz of fluorescent lights]
    # play music "music_placeholder"  # [Music: Sparse strings — patient, restrained]
    "The board meets quarterly now, in a room you petitioned for and fought for until even the floorboards knew the weight of compromise. The independent board is imperfect governance made real: half community, half municipal appointees,"
    "one rotating seat for an external auditor. It holds hearings with the solemnity of a court and the familiarity of a neighborhood kitchen table."
    "You sit facing a screen that streams live sensor reads. The data rolls like a tide chart — peaks of strain and gentler troughs of recovery. The numbers are clinical. The stories behind them are not."
    "Rafi speaks first, in his usual patient cadence. He reads aloud the maintenance logs and names the volunteers who gave their weekends to shore up a failing segment. He mentions a family who had to be relocated last year, small and exact and unbearable in its clarity."
    show rafi_odeh at left:
        zoom 0.7

    rafi_odeh "We voted to keep records. We voted to ask for funding. We voted to not let that family be the last face of this neighborhood."
    "A council member asks about long-term funding. A municipal rep quotes an upcoming bond. Papers pass around like a slow apology. You answer with data and with memory."
    show maya_corvin at right:
        zoom 0.7

    maya_corvin "Sensors tell us when the wall strains. People tell us when it fails. We need both. We need contingency funds not as a footnote but as an active line item."
    "An auditor — neutral, precise — questions the metrics. Camila 'Kai' Navarro attends, a consultant this time rather than an opposing force. She speaks with fewer certainties and more caveats than she used to."

    "Camila 'Kai' Navarro" "Engineering can mitigate, but living systems take time to self-stabilize. We must accept iterative loss to gain stability elsewhere."
    "You feel the words as if struck. Iterative loss — a bureaucratic euphemism for incremental erasure. You find your throat tight. This is the vocabulary of survival in a collapsing climate: small losses traded for a"
    "fighting chance later. The math is cold; the people it reduces to variables are not."
    "Elias Kahn raises his hand and speaks — measured, tethered to both civic language and the memory of rooftop soil. He frames the ask for sustained funding, for a legal covenant that protects green corridors. He"
    "looks at you when he speaks, and the look says that he is trying to hold both the ledger and the ledger's afterlife."
    show elias_kahn at center:
        zoom 0.7

    elias_kahn "We can build a covenant. We can guarantee monitoring. We can commit to relocation plans only as a last resort. None of it is perfect, but it is a framework that can be enforced."

    maya_corvin "Frameworks contain people in boxes. I want them to contain responsibilities."
    "The hearing dissolves into technical debate and then into personal testimony. Someone vomits up grief over a microphone. Another woman names a lost photograph. The board votes on a charter clause that will lock in community"
    "oversight and a threshold for emergency funding. The vote is close. Result: a fragile majority."
    "When the meeting ends, the room feels empty in a way that is new — not because the work is over, but because the weight of it sits heavier than before. You walk out and the"
    "night air is salt and exhaust. Lio waits at the doorway with paint on his sleeves and a face that reads both triumph and tired resignation."
    hide rafi_odeh
    show lio_corvin at left:
        zoom 0.7

    lio_corvin "They wrote the oversight in. Not perfect, but it's there."

    maya_corvin "We made new governance. We made obligations. We bought ourselves another fight."
    "Rafi meets you at the steps, hands still smelling of earth, and gives you a hug that is more like an anchor than warmth."
    hide maya_corvin
    show rafi_odeh at right:
        zoom 0.7

    rafi_odeh "This is how it goes. We win a thing, then we watch it and push it and make sure it does the right work."
    "You press your palm over the trefoil on your wrist, the old small tattoo that keeps you in the same orbit as the person who first taught you to map marshes. Your fingers curl around something"
    "in your pocket — the salvaged brass compass you could never fix but would not discard."
    "The city hums with obligations now: sensor alerts, scheduled maintenance, a rotating council seat for an external auditor next quarter, a neighborhood fund line item, a covenant clause in municipal law. Each promises protection and each exacts a price."
    "You lift your hand and the compass is warm from the heat of your body. You think of the scale of what was lost — houses that are only foundations now, a stretch of the promenade"
    "that was too costly to save in full, a choir of neighborhood voices that moved away. You think of the small unerasable things that remain: Lio's murals, Rafi's seedlings, the way Elias Kahn still finds you"
    "in crowded rooms."
    "Your chest feels like a tide pool caught between the incoming and the outgoing — full, dark, and reflecting the sky with brittle clarity. You have learned to share agency. You have learned to delegate and"
    "to trust committees and to hold policy while planting roots. That knowledge is not comfort. It is sustenance."
    "You set the compass on the rail and let your fingers rest on it. The brass is pitted; the needle is stuck. You don't look to it for direction. You look at the shoreline — the living and the engineered stitched together like a scar."
    "Elias Kahn comes to stand beside you. He offers no grand words; there aren't any that fit. He slides his hand into yours, fingers finding callus and trefoil alike."

    elias_kahn "We keep going."
    hide elias_kahn
    show maya_corvin at center:
        zoom 0.7

    maya_corvin "We keep going. We keep grieving. We keep fixing what we can and mourning what we can't."
    "Camila 'Kai' Navarro appears at the mouth of the stair, a silhouette against the promenade light. She stops, and for once avoids a policy brief or a defensive word. She speaks plain."

    "Camila 'Kai' Navarro" "You did more than I thought you could. You made the boards mean something."

    maya_corvin "We paid. We paid in ways too deep to list. We still pay."

    "Camila 'Kai' Navarro" "Sometimes I think about the pendant my mother gave me. Small things travel through big choices."
    "Her voice falters, human and surprising. It is a pinprick of light in the heavy sky. You accept it as proof that even those who build walls keep small private artifacts from youth."

    rafi_odeh "So what now? Another season of sedge grafting? Another budget fight? Another painting?"
    "You look at the city and feel the old swell of commitment. It is no longer the naive certainty of youth; it is the heavy, deliberate acceptance of someone who knows cost and chooses to continue anyway."
    "You slide the compass back into your pocket. The needle still won't move. You press the pocket flat with your palm and feel the solid weight of it against your rib."

    maya_corvin "This is not a story with a tidy hero. It's a practice. It is a lifelong tending of wounds. We will not be free of work. We will not be free of loss. We will be here anyway."
    hide lio_corvin
    hide rafi_odeh
    hide maya_corvin

    scene bg ch15_16e9b2_5 at full_bg
    # play music "music_placeholder"  # [Music: Single cello phrase — minor, unresolved, then a soft fade]

    scene bg ch15_16e9b2_6 at full_bg
    "THE END"
    # [GAME END]
    return
