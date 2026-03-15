label chapter10:

    # [Scene: Estuary Research Lab | Morning]

    scene bg ch10_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of pumps; a soft, insistent ping from an incoming data stream]
    # play music "music_placeholder"  # [Music: Tense, high-tempo strings—paced like a racing breath]
    "You are already moving in two directions at once: toward the model on the console and toward the politics that will try to rewrite it. The hybrid recommendation you proposed in the council—pilot community programs tied"
    "to development covenants—sits on your tongue like a benediction and a warning. You promised a bridge. Now you feel its weight."
    "The lab smells of ethanol and wet mud; your fingers carry the grit of morning sampling. Fluorescent lights make the monitors harsh; the estuary outside is a flat sheet of pewter. Dr. Naomi Park stands over"
    "a printout spread across the counter, one hand tapping a data point like a metronome."
    show dr_naomi_park at left:
        zoom 0.7

    dr_naomi_park "Hybrid models can work in math and in careful field trials. In practice, Mara—"
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "—they get reworded, redirected, and hollowed out by contracts before a single post is planted."

    dr_naomi_park "Exactly. Covenants without teeth are theater. Investors build exit ramps; chambers pass resolution language that reads like climate theater."
    "Naomi's voice is clinical but not unfeeling; it lands heavy. You trace the projected flood-lines with a fingertip—each color band a different future. The colored bands narrow; stakes compress. The pump's hum seems louder."

    dr_naomi_park "If you're the hinge, you have to define those teeth now. Milestones, independent audits, escrowed funds for enforcement. Otherwise the pilot will be a fig leaf."
    "You feel the edges of your resolve fray. Your sea-glass pendant swings against your breastbone, cool and familiar. It steadies you—or it is the last thing that will break when everything else does."

    mara_kestrel "We stipulate escrowed funds and community stewards for the maintenance clauses. Independent audits, on a timeline, with penalties attached."

    dr_naomi_park "And who enforces the penalties? That's the practical problem. Councils approve language; investors lobby. The state has teeth, but it moves like molasses. I'm telling you this because I don't want you burned—"

    mara_kestrel "I'm already burned. I want the burn to mean something."
    "Your tone is sharper than you intend. Naomi watches you—eyes flinty behind her glasses—then nods once, the concession of a colleague who knows you too well."
    hide dr_naomi_park
    hide mara_kestrel

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A sharp notification tone; a calendar reminder labeled "Council—Finalize Covenants"]

    "You glance at the redline document. Tess's annotation bubbles in the margins" "investor clause: veto on design changes."

    menu:
        "Draft legally specific covenant language now":
            "You stay, fingers flying at the keyboard, pulling legalese and field parameters into a single, unforgiving paragraph."
        "Call Tess and ask for more leeway":
            "You pick up the phone, breath shallow, asking for a margin of wiggle room. Tess's reply is careful—hope threaded with warning."

    # --- merge ---
    "Naomi exhales like a storm front moving in."
    show dr_naomi_park at left:
        zoom 0.7

    dr_naomi_park "If you write it yourself, be prepared to argue every semicolon. If you ask Tess, expect a public compromise where phrases like 'subject to investor approval' appear. Neither is clean."
    "You laugh, a short sound that tastes like iron. The bridge you offered feels narrower than when you built it in your head."
    # [Scene: Council Hall (Seawall Proposal Chamber) | Midday]
    hide dr_naomi_park

    scene bg ch10_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmured council chatter; the creak of the old oak bench]
    # play music "music_placeholder"  # [Music: Percussive, urgent—heartbeat drums underscoring each sentence]
    "Tess slips into the chamber before the meeting convenes, a folded sheaf of meeting minutes hidden like contraband. She meets your eyes and gives you a guarded smile that doesn't reach them. When she hands you"
    "the paper, her fingers brush yours—small, quick, and fleeting as a gull's wing. Her face is a map of compromises made in quiet rooms."
    show tess_omalley at left:
        zoom 0.7

    tess_omalley "They agreed to pilot language, but investors demanded vetoes on structural changes for the first eighteen months. Chair wants milestones tied to funding tranches. Livia—she's listening."
    "You fold the minutes into your notebook. Livia Chen's presence is architecture: everything about her says composed leverage. She sits at the head of the table, the gold wave brooch catching the light like a coin."
    "When you stand, her eyes slide toward you, narrow, measuring—not hostile, not warm—just precise assessment."
    show livia_chen at right:
        zoom 0.7

    livia_chen "Ms. Kestrel, your hybrid proposal is inventive. It offers a route forward. I will admit—politically it smooths things."
    show mara_kestrel at center:
        zoom 0.7

    mara_kestrel "But the veto language—"

    livia_chen "—is a safeguard for investors who are putting real capital into New Aster. We both know what happens when funds dry up and projects are abandoned."

    mara_kestrel "We also know what happens when projects are imposed on communities: displacement, broken livelihoods, mistrust. Covenants without community enforcement are symbolic."
    "Livia Chen's jaw tightens a fraction. Her voice loses some of the polish."

    livia_chen "You asked for a bridge. A functioning bridge needs support from both sides. Investors want certainty. The council wants to secure payrolls."
    "Elias 'Eli' Rowan is at your elbow, hands smudged with grease and sea-salt. He looks like someone who wants to do something physical to prove the world will hold."

    "Elias 'Eli' Rowan" "We can fabricate a modular seawall that allows for later adjustments. We can put in sensors and locks so the community can call for modifications—"

    "Council Member" "That kind of retrofitting is expensive. If investors expect a closed system, it's a risk."
    "Elias 'Eli' Rowan's voice rises; his eyes are bright and impatient."

    "Elias 'Eli' Rowan" "It's not a risk if it's built with the town's knowledge. We can train people—"

    livia_chen "Training is not the same as legal authority. Who signs the change order? Who underwrites liability? The council must consider exposure."
    "Your pulse thunders in your ears. Outside the windows, a far gull shrieks and the sea swallows the sound. The room narrows into angles of policy language and the soft weight of Tess's minute."

    tess_omalley "There's a clause that could be rearranged—'investor veto' could read 'investor consultation with community override'—if we can get legal to agree."
    "You look at Tess, at Elias 'Eli' Rowan, at Livia Chen. Each face is a different kind of pressure. Your hope feels like a fragile raft."

    menu:
        "Publicly push for 'community override' clause":
            "You stand and speak, voice loud in the chamber. Chairs shift; the investors' reps exchange glances."
        "Work the room quietly—pull the Chair and legal aside":
            "You slip into a hallway negotiation, trading phrases like currency and calibrating the language one breath at a time."

    # --- merge ---
    "The debate accelerates. Investors lean forward, palms on glossy tablets. Livia negotiates with the economy of someone used to buying outcomes. You hear the tick of the clock as if it were a countdown."

    livia_chen "We can insert stronger milestones—independent audits, delayed tranches. In exchange, investors retain first line oversight for scope alterations tied to structural integrity."

    mara_kestrel "And the community escape clause for cultural and ecological preservation?"

    livia_chen "We can add language for protected zones—on paper. Execution depends on the legal team and your—' (her eyes flick to you) '—on your ability to referee."
    "Her last word lands like a verdict. You are the referee. The bridge you've built is also the referee's rope: taut, fraying at the knots."
    # [Scene: Tidewatch Lighthouse & Rooftop Garden | Dusk]
    hide tess_omalley
    hide livia_chen
    hide mara_kestrel

    scene bg ch10_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind through the rigging; distant town bells]
    # play music "music_placeholder"  # [Music: A grinding, rising cello—tension mounting to near-breaking]

    "The vote is brief and blistering. Minutes crawl. Tess sends you a message" "Approved—pilot with caveats.' Your stomach drops before the words finish. Approved. A hit of triumph and then the immediate cold: 'with caveats"
    "You stand on the lighthouse's ring of planters, the town below like a stitched map of small lights. Elias 'Eli' Rowan's hand finds yours; he's quiet—too quiet—and the calluses on his palm press into yours like an anchor."

    "Elias 'Eli' Rowan" "So it's a start. We can show prototypes in the first milestone. The community can build the modules."
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "Start is not the same as safeguard, Elias. The funding comes in tranches tied to milestones, and investors retain vetoes for design changes in the first eighteen months."

    "Elias 'Eli' Rowan" "We can make those milestones rigorous. We can—"

    mara_kestrel "—and if the investor veto overrides community needs, what then? If they say 'no' to a modification that prevents displacement, who holds them accountable?"
    "Elias 'Eli' Rowan's face shifts—guilt and impatience braided together."

    "Elias 'Eli' Rowan" "We will hold them accountable. I'll go to the investors. I'll—"

    mara_kestrel "Elias, this isn't a bolt you can tighten. This is law and livelihoods. It needs legal teeth, community control, and enforcement that can't be bought out."
    "Below, the harbor breathes, restless and low. You feel Rafi Gómez's call like a tide—unexpected and deep. You step away from Elias 'Eli' Rowan, pull your phone from your pocket, and accept."
    show rafi_gmez at right:
        zoom 0.7

    rafi_gmez "Mara... heard the news. Hybrid, right? You always said there had to be a middle ground. Can anyone really hold power accountable? Or does accountability turn to paperwork?"
    "You hear the weather in his voice—the creak of an old boat, the wet wool of the harbor. He is not asking for technicalities. He is asking for a promise the sea understands."

    mara_kestrel "We can make them accountable. We can write audits into escrow. We can make enforcement automatic—penalties that trigger restoration funds. We can—"

    rafi_gmez "You can write a thousand lines on paper, kid. But you can't make people brave enough to use the clause when the bills come due."
    "His words are a slap and a benediction. You look at the pendant in your hand; its edges are worn smooth. You think of Grandma Hira's stories—of stones moved by hands to protect a path, of"
    "the old harbor folk who refused to sell the shoreline for a price. You think of the boardwalk that buckled in a storm and the names that were lost in the slosh and wind."
    show dr_naomi_park at center:
        zoom 0.7

    dr_naomi_park "Mara, hybrids are fragile. They dilute. They end up as a cosmetic concession unless you define enforcement mechanisms that are independent of investor goodwill."
    "Your throat tightens. Everything inside you is shorthand for 'do not let this become another whitewashed promise.' The melody of triumph is already curdling."
    hide mara_kestrel
    hide rafi_gmez
    hide dr_naomi_park

    scene bg ch10_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The stamp hits paper; it's emphatic and final]
    # play music "music_placeholder"  # [Music: Strings snap higher—an almost unbearable pitch]
    "You look at the approved text, then at Elias 'Eli' Rowan, at Tess O’Malley, at the planters shuddering in the wind. Your role has crystallized into something you never asked for: the public face of a"
    "fragile compromise. Being the bridge was supposed to be a place of connection. Now being the bridge means you might be the one everyone leans on—or the one who snaps."
    "You close your eyes and feel the strain like an actual rope across your shoulders."
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "If this is to mean anything, we write the enforcement into escrow, independent audits, community override with clear triggers. No 'investor veto' without cause. No gag clauses."
    show tess_omalley at right:
        zoom 0.7

    tess_omalley "I can push the legal text. I can keep leaking minutes until someone listens."

    "Elias 'Eli' Rowan" "And I'll build the first modules and the sensor systems. We'll make the thing undeniable."
    "But their assurances are thin against the weight of that stamped document. The approval is an engine with teeth that could chew at the town's bones."

    "Rafi Gómez's last words echo as if the sea itself had spoken" "Can anyone hold power accountable?"
    "You clutch the pendant until the glass grows warm."
    hide mara_kestrel
    hide tess_omalley

    scene bg ch10_453e40_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant gull cries, then silence—too loud in the hush]
    # play music "music_placeholder"  # [Music: A single, sustained dissonant chord—the moment before a storm breaks]
    "You realize the bridge you offered will need to be more than language and models. It will require constant vigilance, legal firepower, and a willingness to be unpopular. It will require you to be the person"
    "who goes door to door with enforcement letters in one hand and a toolkit in the other."
    "You imagine what failure looks like—the pilot used as a greenwash while the seawall slices through the neighborhoods you love. You imagine what success looks like—the town holding a line, a community steward unlocking the override"
    "clause the moment it's needed. Both images are sharp and close. Both are possible now."
    "You breathe. The chord unwinds into a thin, high resolution of resolve—and fear."
    "You place the pendant back against your throat and let the cool settle. Your role is no longer an idea: it is a set of obligations and possible betrayals."

    scene bg ch10_453e40_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain taps the lighthouse, a rising, urgent patter]
    # play music "music_placeholder"  # [Music: Crescendo—strings, metallic percussion—full, relentless intensity]
    "You do not yet know whether the bridge will hold. You know only that you must be its engineer and its first responder. The town has voted to trust you with the hinge between ideals and power—and the hinge creaks already."
    # [Scene Transition: The rain thickens; the town below is a blurred map of light and movement]
    # play music "music_placeholder"  # [Music: Climactic swell that demands the next step]

    scene bg ch10_453e40_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter11
    return
