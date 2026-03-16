label chapter9:

    # [Scene: Salthaven Boardwalk | Midday]

    scene bg ch8_6b08b4_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, taut strings; a single mournful piano note beneath]
    # play sound "sfx_placeholder"  # [Sound: Shouts, murmured questions, the metallic clack of camera shutters; gulls crying, wind tearing a loose banner]
    "You step onto the boardwalk and the air hits you like a ledger—salty, wet, threaded with diesel and the tang of fry oil from a vendor cart. Cameras find you before you find them. Flashbulbs bloom and die; voices fold around you like tidewater."
    "Your satchel feels heavier than it should, the maps inside soft and damp at the corners. The compass at your throat is warm where it rubs the collar of your jacket. Somewhere beyond the press huddle,"
    "a child laughs, and for a second the sound is small enough to be a promise. Then a man with a microphone calls your name, and the promise slides into practical things—quotas, covenants, escrow."

    scene bg ch8_6b08b4_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Microphone feedback; the crowd surges]
    "Noah Vega steps up to the temporary podium with the effortless politeness of someone who has rehearsed gratitude into a speech. He smiles in the exact places that translate to headlines."
    show noah_vega at left:
        zoom 0.7

    noah_vega "Today marks a turning point for Salthaven. This proposal—our seawall—means jobs, safety, and a future where our children can remember this town without fear."
    "Applause breaks from a cluster of small-business owners and a group handed matching blue scarves. Someone shouts, 'Finally!'—a sound like relief knitted into the salt air."
    "Kai Solano stands near the railing, jaw set, a handmade sign half-hidden by his jacket. He meets your eyes and there is a tilt in his mouth you know too well: disappointment tempered into defiance."
    show kai_solano at right:
        zoom 0.7

    kai_solano "They'll sell it as salvation. They'll sell us short."
    "You can feel the crowd dividing along invisible seams—cheer on one side, a hardening on the other. A developer-friendly journalist with an already-typed editorial is murmuring to his cameraman; a counter-protest has begun to ripple toward the boardwalk like a returning current."

    menu:
        "Smile and answer with the press line":
            "You give the rehearsed curve of your mouth and read your prepared statement—'inclusive protections for all'—into the microphone. Cameras eat the words. They sound like a promise you're still trying to mean."
        "Tell the truth, even if it hurts":
            "You drop the policy phrasing. 'Not everyone will be spared,' you say, and the silence that follows is heavier than any applause. Faces tighten; someone spits a curse into the wind."
        "Stay silent and let Noah hold the frame":
            "You step back, letting Noah fill the space. Reporters angle toward him. You feel both relief and the cold weight of absence at your shoulders."

    # --- merge ---
    "The boardwalk event resumes as the microphones ride the resulting silence."
    "The microphone rides the silence you create. Noah nods at you—his expression soft, practiced. A reporter presses closer with a question that smells of accusation."

    "Reporter" "Ms. Marin, critics say the project's legal language could be used to expedite buyouts. How do you answer residents afraid of being displaced?"
    "Your throat tightens. Each word you choose will be quoted and pressed into a headline. You can almost hear the editorial already: modern salvation, honest compromise, pragmatic leadership. Or: coastal sellout."
    show aria_marin at center:
        zoom 0.7

    aria_marin "We built this proposal around protections—legal, social, and ecological. I won't let language be a loophole for displacement."
    "You keep your voice steady, because steadiness is sometimes the only thing you can offer."

    noah_vega "And we're prepared to codify those protections. Escrow, covenants—airtight supports. But we need a path forward. Funding waits for certainty."
    "Kai's laugh is low and rough. He moves forward, interrupting the cadence, and the crowd shifts to listen."

    kai_solano "Certainty for who, Noah? If you set the wall where it helps the new storefronts and leaves the old row to choke, that's not certainty—that's calculation."

    noah_vega "Kai, it's not about who is favored. It's about making a plan that keeps people dry and the economy intact."

    kai_solano "The 'economy' you mean is the reason families were priced out before the water rose. We won't applaud being sold in neat brochures."
    "The words land hard. A cluster of younger residents chant, 'No more selling!' Someone waves a banner that reads KEEP SALTHAVEN HOME in furious block letters. Across the way, workers from the Arcology site—hired for the project—hold placards: JOBS NOW."
    "You are the seam under strain. Microphones hover. A live mic catches the raw friction between friends made public."
    hide noah_vega
    show dr_linh_pham at left:
        zoom 0.7

    dr_linh_pham "Aria—there's more. The siting model shows a significant risk: if the seawall is placed improperly along the north curve, downstream erosion rates could spike—strip out marshes that buffer neighborhoods three bays over."
    "You take the tablet. The model's animations stutter in the crowd-light: a swell of grey where marsh should be; lines that push sediment away, not toward safe beaches. The graphical arrows look like accusations."

    aria_marin "How certain? Explain it to them, Linh. Tell them what we can change."

    dr_linh_pham "The model's sensitivity is high. Small shifts in the wall's orientation change sediment deposition dramatically. We can impose design constraints—breakwaters, permeable sections, living shorelines as adjuncts—but they cost time and money. If the funders see delay, they'll deflect."
    hide kai_solano
    show noah_vega at right:
        zoom 0.7

    noah_vega "We can factor those constraints. We can attach environmental conditions to the contract."
    "Kai scoffs. 'Attach and hope they read it? We've seen 'conditional' become 'opt-out' before.'"
    "Elder Tomas Quay pushes through the press like he pushes through a memory, holding his carved walking stick. His face is map-lines of storms past. When he speaks, the boardwalk hushes in respect and fear."
    hide aria_marin
    show elder_tomas_quay at center:
        zoom 0.7

    elder_tomas_quay "You speak of models and contracts, Aria, but models didn't stop the tide when my sister's house went. I have seen promises fold. If we mark certain streets—Quay Lane, Mariners' Row—to be protected, those are streets with graves and kitchens and fathers who have to walk to work. If protecting them costs another street, then say so. Tell me which streets you'll let go."
    "His voice trembles, and the tremor carries a history you cannot argue away. The crowd listens as if a verdict is being handed down. In his hands, preservation becomes binary: one place to save, another to lose. The moral arithmetic is sharper than any planner's spreadsheet."
    hide dr_linh_pham
    show aria_marin at left:
        zoom 0.7

    aria_marin "We need to avoid that calculus. I want to protect where people live and where memory is kept. But I also hear Linh—if the wrong fix accelerates erosion elsewhere, that's not protection; it's displacement by proxy."
    "Kai steps close enough that you can smell the salt and grief on him."
    hide noah_vega
    show kai_solano at right:
        zoom 0.7

    kai_solano "Then stand with us. Walk with us out of this theater. Take the crowd with you. Make them see they matter more than the glossy render."
    "Noah's patience thins. He senses momentum slipping—and with it, funding and political capital."
    hide elder_tomas_quay
    show noah_vega at center:
        zoom 0.7

    noah_vega "If you turn your back now, Aria, the firm will pivot. Contracts are fragile without a public face. We need you."
    "The boardwalk feels like a line on a map that you are being asked to trace. Each option will redraw neighborhoods. Cameras keep chewing up memory: your words, your pauses, your indecision."

    menu:
        "Step forward and grab Kai's hand, join the march":
            "You close the distance in one motion, grip Kai's wrist, and let chants swell under you. The crowd follows. For a sliver of time you feel unified and dangerous and painfully alive."
        "Reach for Noah's offered handshake, keep the conversation open":
            "You take Noah's hand in a formal, public gesture. Reporters lean in; some nod in approval. It looks like stability—if also like concession."
        "Lift the tablet, call attention to Linh's findings, demand a pause for the science":
            "You raise the tablet into the wavering light and speak through the siren-voices. Cameras turn; Linh steps up beside you. The crowd listens—but some begin to boo at delay."

    # --- merge ---
    "The boardwalk continues to seethe as the town waits for your public posture."
    "Your chest is heavy with the knowledge that any action will be read as allegiance. You think of the family portraits you once pinned to your office wall—photographs of neighbors, whole dinners, a mother teaching a child to shuck clams. The town is not only infrastructure."
    "A murmur grows into shouts. On the wooden planks, someone lights a small smoke flare—the color of anger. The scent is acrid and metallic; it presses at your throat. You realize that what started as a"
    "press event has become a theater of accusation: the seawall as savior, as sellout, as betrayal."
    "Noah steps back from the podium, jaw tightening. The firm’s public relations officer moves through the crowd, whispering into an earpiece. A reporter holds up a tablet displaying an editorial headline—MODERN SALVATION—that already frames the story for a morning that will feel like a judgment."
    "Elder Tomas folds his hands on his walking stick and looks at you as if measuring whether you're still the child he watched grow up on this shore."
    hide aria_marin
    show elder_tomas_quay at left:
        zoom 0.7

    elder_tomas_quay "Words on paper won't hold back water. Decisions will. Whose homes will you put first, Aria?"
    hide kai_solano
    show dr_linh_pham at right:
        zoom 0.7

    dr_linh_pham "We can demand modifications—specific siting, engineered permeable sections, mandated living-shoreline buffers. It will complicate the timeline, yes, but it reduces the risk that we save one pocket by drowning another."

    noah_vega "Attach strict environmental modifications to the contract. It's the only way to get both funding and safeguards. We do it together; we own the language."
    hide noah_vega
    show kai_solano at center:
        zoom 0.7

    kai_solano "Or you walk with us. With the people in the streets, not the firm in the podium."
    "Your mouth is dry. You taste the salt from the sea and the metallic tang of the smoke. You can feel the town’s breath hitching, waiting for the next move. The compass at your throat feels suddenly heavy with the weight of being the one who must choose a direction."
    "You think of compromise and the way it sometimes looks like surrender. You think of promises you made in rooms with low light and higher stakes. The crowd presses in, each voice an argument; none of"
    "them small. The plan you helped release is now devoured and reshaped by a dozen tongues."
    "You must decide your posture in front of cameras, funders, elders, scientists, and the friend whose hands you've held since childhood."

    menu:
        "Push the seawall through but attach strict environmental modifications demanded by Dr. Linh.":
            jump chapter10
        "Withdraw support and side publicly with Kai’s protests to force renegotiation.":
            jump chapter14
        "Propose a phased build that preserves some neighborhoods while buying time for living-shoreline trials.":
            jump chapter16
    return
