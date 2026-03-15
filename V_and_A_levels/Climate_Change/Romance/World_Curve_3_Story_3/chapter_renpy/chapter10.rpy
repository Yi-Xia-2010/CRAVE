label chapter10:

    # [Scene: Asteria Coastal Research Lab | Late Night]

    scene bg ch10_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of servers, distant breakers against experimental breakwaters]
    # play music "music_placeholder"  # [Music: Taut, driving pulse—steady, insistent]
    "You arrive with your shoulders knotted the way they go before a long night. The lamp clicks; a bank of monitors answers with cold light. Your tablet folds open onto a half-built timeline. The file names"
    "are a geography: procurement_2027_final.pdf, shipping_manifest_0428.csv, vendor_payments_redacted.xlsx. Each filename is a tide mark you can measure."
    "You set the crate of printed FOIA copies beside the keyboard and feel the room settle into process. The air smells like ozone and coffee grounds. Your pendant, pressed low beneath your collar, is a small,"
    "private compass. You tap a search string and watch the lab's blue glow outline names—Noah Ortega, Development Consortium—over and over, like a loop."

    scene bg ch10_453e40_2 at full_bg
    "Lines of code and columns of figures trace out patterns that are not accidents. Shipping manifests cross-reference with procurement dates; expedited approvals are stamped by accounts tied to shell companies. A lapel pin—an image you have"
    "only seen on Noah's coat—turns up as an SVG on a vendor's invoice. A signet ring appears as a line item in ownership documents for an offshore logistics firm. The connections are not clean enough to"
    "convict, but they are a map."
    "You breathe and lean into the work. You do this the way you assemble living shorelines: one datum, one mapping, until a contour appears."

    scene bg ch10_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Leather satchel strap thuds; coffee cup hisses as steam settles]
    show emil_kwon at left:
        zoom 0.7

    emil_kwon "You look like you haven't slept. Figured you'd need the obvious thing."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Coffee, yes. Thank you."
    "You let your voice be small to the hum of machines."

    emil_kwon "Show me where you're stuck. Or don't—just tell me a number and I can hold it for you."

    maya_reyes "There's a run of expedited procurement approvals in March. The paperwork is stamped as emergency retrofit—no public notice, no RFP. Payments route through three shell accounts and then into a logistics firm with ties to a holding company that lists a signet ring-bearing heir as owner."

    emil_kwon "That's a long chain. Do you have the signatures? Any internal comments?"

    maya_reyes "Some. Late-night approval logs show override flags. One email has a line—'prioritize closure'—from an account mapped to a consortium address. But it's all hedged. Redactions, aliases."

    emil_kwon "If all that lines up—if Noah's stamp is in the tail—this is bigger than a bad vote. It becomes a structural lever.' (He sits on the stool opposite you, sets the coffee between your hands.) 'You sure you want to pull that lever?"
    "He watches you the way he watches tides: patient but unflinching. He offers both the cup and the question. You answer in the way you do the technical work—by making an evidence chain. You trace the"
    "manifests, open CSVs, paste hashes, time-stamp screenshots. Each action tightens a knot in the narrative you're building."

    menu:
        "Take a short breath and ask Emil to call Diego to cross-check vendor rumors":
            "You thumb a quick message to Diego. Emil nods and pulls up his contact list without being asked, fingers quick and sure. He murmurs he'll ping community channels but keep it quiet."
        "Tell Emil to lock the lab door and help you sift through the invoices":
            "Emil sets his coffee down, keys the lab's access terminal, and locks the main door. The click is small but decisive; he leans over the screen and starts comparing invoice numbers to port logs."

    # --- merge ---
    "You choose both in practice: Emil locks the door and you send Diego the snippet that might jog a memory."
    "You hear the key's click as a small safeguard against leaks; you hear the other option—reach into the neighborhood network for cross-verification—as a reach toward communal memory. Both feel necessary. You choose both in practice: Emil locks the door and you send Diego the snippet that might jog a memory."
    # play sound "sfx_placeholder"  # [Sound: A new ping on the monitor—an incoming email subject line highlights in red]
    "Late-night emails can be mundane—an administrative note, a reminder. This one is different. The subject line is terse: Priority—EXPEDITE. The sender is an automated account, but the attached PDF hides a manifest with an SVG image"
    "you recognize. A lapel pin. The timestamp is late—2:14 a.m.—the same window as the override in the procurement log. Your fingers hover. Your mouth tastes of metal."

    maya_reyes "That's the same motif. The pin is embedded as a logo on shipping manifests destined for the construction staging area.' (You lean closer.) 'Look—this vendor is flagged with 'exclusive supply' language."

    emil_kwon "Exclusive supply? That smells like favoritism.' (He rubs his forehead.) 'If this went through without open bidding, people get priced out. Vendors who could build living systems are sidelined."

    maya_reyes "And the invoices show rapid disbursement—no waiting period. That's not just speed; that's gating. Whoever wanted to close access closed it."
    "Your pulse picks up a steady clip. The lab's hum recedes and the room contracts to the screen, the coffee, the crate of records. The work is methodical—download, validate, cross-check—but the implications stretch outward like a"
    "tide. If you set these pieces in order, the picture will be plain. If you fail, the seawall amendment slips through and neighborhoods are rewritten without a fight."
    hide emil_kwon
    hide maya_reyes

    scene bg ch10_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Rhythm accelerates—percussive digits overlaying synth tension]
    "You stack evidence into folders labeled for a narrative: Ownership, Expedited Approvals, Vendor Exclusions, Oral Histories. The Oral Histories folder is light on paper but heavy in voice. You realize you need memory to anchor documents—to"
    "show how neighborhoods were consulted, how timelines and promises land on people, not just parcels."
    # [Scene: Old Beacon Lighthouse | Foggy Morning]

    scene bg ch10_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Lantern wind, reed whisper, the gulls' distant call]
    # play music "music_placeholder"  # [Music: A low, insistent note—less frenetic but still urgent]
    "Asha Karim meets you where the light cuts the marsh. She brings a rolled packet of maps yellowed at the edges; the scent of old paper rises like smoke. Her hands are steady. Her spectacles catch the lantern sweep and throw amber back at you."
    show asha_karim at left:
        zoom 0.7

    asha_karim "These were annotated by residents who lived the floods before the records were digitized. They marked where family plots used to be—where a seawall would not just hold water, but redraw home lines.' (She unrolls a map with ink that has bled into history.) 'Keep this close to the contracts, child. Evidence and memory together make a better frame."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "They note 'historic access' at the promenade and a cluster of vendor sheds that were promised relocation funds in '26. If the procurement files redirect that budget, there's a ledger showing who benefits and who doesn't.' (You trace a faded ink line.) 'I need to match these place names to parcel IDs."

    asha_karim "People remember different things. One's memory will contradict another. That's why you must gather them together—corroboration, not just accusation."

    maya_reyes "I'll record the interviews. Transcribe, time-stamp."

    asha_karim "Intent is a heavy word. The court listens to patterns."
    "You feel the arc of the work flatten and then rise: documents supply pattern; people supply weight. Asha hands you a small envelope with dates in a penciled hand. Inside is a note: 'Lantern night—bring questions.'"
    "Her face is unreadable, the way it must be when memory is a map that stings."

    menu:
        "Ask Asha to stay for the first oral history session to help ask clarifying questions":
            "Asha nods, folds her maps, and says she'll come if you need her. Her presence steadies the interview plan—she reminds you to ask about promises, not just losses."
        "Tell Asha you'll record on your own and send the file for her notes later":
            "Asha's jaw tightens but she agrees. 'Your voice will hold them. Make it safe,' she says. You promise you will."

    # --- merge ---
    "You record. You ask about tides, about promises, about the night a generator failed and a family's kitchen floated under muck. Voices answer you in turns—short, long, rounded by memory. Each recollection is a geologic layer; you catalog them, time-stamp, and file."
    "You record. You ask about tides, about promises, about the night a generator failed and a family's kitchen floated under muck. Voices answer you in turns—short, long, rounded by memory. Each recollection is a geologic layer;"
    "you catalog them, time-stamp, and file. The Old Beacon's lantern sweeps like a metronome for testimony."
    hide asha_karim
    hide maya_reyes

    scene bg ch10_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: The pulse returns, now with a higher beat]
    # play sound "sfx_placeholder"  # [Sound: Keyboard clacks faster; printer whirs]
    "Back in the lab, you paste transcripts beside invoices. The fit is not perfect, but it is contiguous. You make a timeline graphic: March 1—proposal submission; March 12—expedited approval; March 13—vendor selection; March 28—payments issued. Overlaid: March 10—community meeting canceled; March 20—market displacement notice. The picture tightens."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "If we can show that the meeting cancellation predates the vendor selection, that looks like a preemptive closure."
    show emil_kwon at right:
        zoom 0.7

    emil_kwon "Do you have backups? Offsite copies?"

    maya_reyes "Encrypted. Backed up. Diego has a copy."

    emil_kwon "This is going to draw heat. If you go public, people will want names. They will ask you for proof you can stand behind."

    maya_reyes "I know. I keep thinking back to the last time I let the timelines be vague and people paid for it.' (Your voice is even.) 'This time, I want the ledger and the stories to hold together."

    emil_kwon "Okay. Then let's make them unbreakable."
    "Your fingers fly. The night shrinks and expands with revelation. Each file you secure is a small dam against erasure. Each interview you transcribe is ballast. The work is solitary; when you look up, Emil is still there—mud on his shoes, unresolved worry in his hands."

    emil_kwon "Are you doing this because you want justice or because you can't stand the thought of being blamed again?"

    maya_reyes "Both. It's not either-or.' (You let the sentence be factual, the emotion present but not theatrical.) 'If I can change the rules, more people get a chance. If I fail, the rules stay the same and someone else pays."

    emil_kwon "Promise me you'll sleep sometime."

    maya_reyes "Promise me you'll say 'no' if this starts to cost you more than it's worth."

    emil_kwon "I won't leave you for this. But I will push you to stop when it's too much."
    "His touch is a small hinge. You don't soften. You count this as an agreement of shared burden. The evidence stack grows like a rising tide pinned down by maps and signatures. You feel a focused fury—the old guilt shaped into procedure. The pendant at your throat feels almost hot."
    hide maya_reyes
    hide emil_kwon

    scene bg ch10_453e40_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant, metallic ping; the lab's HVAC kicks a little louder]
    "You open the next file and your breath catches. It's a transport log tied to a shipping yard near the Beacon. The manifest lists a 'priority lane'—a sequence of shipments routed without public notice. One entry"
    "is marked with a code you recognize from the signet ownership documents. The timestamp aligns with the override approvals."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "There. That chain."
    show emil_kwon at right:
        zoom 0.7

    emil_kwon "So we can show linkage—from vendor to payment to ownership.' (He exhales slowly.) 'If that's enough to get an auditor interested, you force the machine to open."
    "The adrenaline arrives like a winter swell: quick breaths, sharpened focus, hands that do not tremble as much as they did before. But your mind stays neutral in judgement—this is a structural problem. Your work will be the mechanism by which others can judge it."
    "You assemble a briefing: a clear timeline, annotated maps, select transcripts, and the chain of transactions with redactions deliberately minimal. You label the folder: 'For Counsel—Priority.' The label feels right and necessary."

    "Asha's voice on the line" "Make sure the oral histories are in their own packet. Memory is not evidence alone, but it changes context."

    maya_reyes "I will. I'll bind them together."
    "It is past midnight. The lab's monitors push icy light across the prints of your hands. Outside, a foghorn moans. The Old Beacon's lantern swings once through the haze and disappears. You consider the line on"
    "your pendant—the tide line. The metaphor shifts until it is literal: a boundary you can cross."
    "Your chest tightens in a way that signals readiness, not panic. You have evidence enough to get hearings to ask questions. You have names and time stamps that will not evaporate with water. You have allies"
    "who will keep copies. The work is slow and lonely—and with every verified link, it acquires velocity."
    hide maya_reyes
    hide emil_kwon

    scene bg ch10_453e40_8 at full_bg
    # play music "music_placeholder"  # [Music: A taut single sustained chord, then a held silence that thrums with expectation]
    "You assemble the final folder and slide it into an encrypted transfer. Your name is on the header because someone must carry the narrative forward. You think of Diego's voice on the phone, of Asha's maps,"
    "of Emil's steady hands. You think of the council chamber, the mayor's polished smile, Noah's signet ring and the quiet authority he represents."
    "Your tide-line pendant rests against your sternum. You press it with the pad of your thumb and feel the cool metal. The work you have done is not an end—it's a lever. The city will have to reckon with what you unspool."
    "Page-turn thought: The folder is ready. The next moves require discretion, courage, and timing. When you send this out; when the first leak lands in public view, loyalties will calcify, people will choose, and the angle"
    "of this fight will change. You can already hear the city's hum shift toward a higher pitch."

    scene bg ch10_453e40_9 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The faint whir of the server; your heartbeat matching its tempo]

    scene bg ch10_453e40_10 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter11
    return
