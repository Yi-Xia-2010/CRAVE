label chapter5:

    # [Scene: Boardwalk | Golden Hour]

    scene bg ch5_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Driving strings, quickening tempo]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the river of the tide whispering against pilings]
    "You tighten your grip on your notebook without thinking. The leather is salt-soft where your thumb rests; pages fanned with tide logs and scrawled initials — J.R., T.K., S.N. — like a map of who keeps"
    "showing up. Weeks of pilings tamped with sand and root-starts have changed the way water moves here: where it used to lick foundations it now finds the berm and sighs away. The data in your own"
    "handwriting says it plainly. Dr. Saira called it 'measurable damping.' Old Man Rafi called it 'a small mercy.' You don't get to pretend it's enough. But for the moment, the proof makes your chest a little"
    "lighter, and that light catches on the coral pendant at your throat."
    "Jonah Reyes walks beside you; the board creaks under both of you in a pleasant, familiar way. His jacket smells of damp wool and tar and the kind of sweat that comes from a day's honest"
    "work. He points at a stretch of repaired boards where barnacles have already colonized a new niche, like a bruise turning to scar."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "Look at that. I swear, you and Saira and the whole crew made it sing again."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "We made it grumble politely. Nature doesn't ask permission to come back."

    jonah_reyes "So who am I competing with for sunset shifts? The marsh, or the researcher with a notebook that smells like old coffee?"

    mira_kestrel "Very scientific coffee. High sediment load, clearly."
    "Tessa, looping down the boardwalk with a tray of thermoses and bandaged thumbs, drops a nudge into the conversation before anyone can get too earnest."
    show tessa_kestrel at center:
        zoom 0.7

    tessa_kestrel "Scientist by day, love interest by sunset — is that your new title, Mira?"

    menu:
        "Play along and lean into the tease":
            "You lean close, brushing your shoulder against Tessa's as if conspiratorial. 'You two keep that up and I'll start charging for sunset consultations,' you tell her. Laughter spills from the group; Tessa winks like a mocking sun."
        "Deflect with a technical correction":
            "You tuck your chin and point to the tide markers. 'Actually, thermodynamic exchange at the berm interface suggests—' Your attempt at seriousness collapses into a smile, and Jonah catches your grin as if it were an offered hand."

    # --- merge ---
    "Continue"
    "The air tastes of salt and cider and the faint copper edge of worry. Dr. Saira joins you, boots thudding, a tablet under her arm and a smear of mud on one cheek that looks honorable."
    hide jonah_reyes
    show dr_saira_ngoma at left:
        zoom 0.7

    dr_saira_ngoma "Preliminary surge models just updated. Narrow inlets are showing a consistent ten to fifteen percent reduction in peak velocities. It's early, but it's a signal. Your pilings held—your designs are working."
    "Mira Kestrel: (breath quickening) 'Ten to fifteen is a start. We've got to monitor for the next high tide series and the seasonal storm window.'"

    dr_saira_ngoma "We'll keep the logs. We'll refine. Funding is still the question, Mira, but scientifically—this is something that scales with people, not just machines."
    "Before you can exhale, footfalls from the farther end of the boardwalk shift the air: the clean, engineered cadence of Cass. His coat flutters, catching lamplight like a slate patch. He wears that professional calm like"
    "armor, but when he sees the cluster of townspeople, his face loosens in something that looks, very briefly, like relief."
    hide mira_kestrel
    show cassian_cass_romano at right:
        zoom 0.7

    cassian_cass_romano "This—' (he gestures at the berms and the small crowd) '—this is exactly what I hoped you'd show me."
    hide tessa_kestrel
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "You mean what you wanted to model, or what we did with a shovel and coffee?"

    cassian_cass_romano "Both. And—there's a grant. It's substantial. It could scale these methods up along the coastline, put engineers on payroll, materials on order. But the funding body requires a centralized management agreement. They want to know who signs and who is accountable."
    "A hush drops that feels like the first stilling before a wave hits. Your stomach flips with something like fear, like exhilaration. Cass's words are promise and weight at once."
    "Mayor Lynette Cole's voice threads in over your shoulder, polished and brisk as ever."
    hide dr_saira_ngoma
    show mayor_lynette_cole at left:
        zoom 0.7

    mayor_lynette_cole "Visible progress for the cameras, Mira. Philanthropy moves where there's a story. If we can show momentum now, the municipality can leverage more funds. We should accept while attention lasts."
    "Mira Kestrel: (heart ratcheting) 'Visible progress is valuable. But 'visible' doesn't mean 'representative.''"

    mayor_lynette_cole "We can do both. With the right PR, the town looks like a model. That brings more investors."

    jonah_reyes "More investors who then decide what our town looks like. Who decides when that looks more like a postcard than like a home?"
    "Cass holds your gaze, steel-gray eyes open, not worn down but asking."

    cassian_cass_romano "Mira. Help me translate this for them. Help me make the agreement stipulate community seats, rotating oversight, transparency clauses. Sign with me and my firm—they get the contract. You keep the community at the table. We scale and protect what's already standing."
    "Your mind runs a sharp series of images: the fen's new roots, Tessa's sunburned shoulders, the Repair Garden sprouting seedlings, Old Man Rafi spooling story into the night. And overlaid on that is the memory that"
    "made you leave and then return — houses taken by a storm that felt like punishment because no one listened in time. Survivor guilt braces your decisions like a hidden spine. The possibility of scaling feels"
    "like a lifeline and a lever at the same time."

    menu:
        "Ask for details and community oversight language now":
            "You step forward, voice tight with the speed of a coming tide. 'If we consider this, I need the exact terms. Community seats documented, veto power on aesthetics, local hiring commitments, transparent accounting.' Cass listens, his jaw working — he types into his tablet, promising to draft clauses. Jonah relaxes fractionally, not entirely convinced but watching the process with trust's slow burn."
        "Tell Cass you'll need time and call for a town convening":
            "You shake your head once and let the boardwalk creak fill the silence. 'Not tonight. If a contract affects who owns decisions here, this town needs to see it. We convene, we read, we decide together.' Cass's expression tightens — you see the calculation of a professional used to deadlines — yet he nods, not willing to lose the opening."

    # --- merge ---
    "Continue"
    "Cass's hand hovers over his tablet like it's the bridge between two possible futures. Mayor Lynette, always alert for a headline, leans in."

    mayor_lynette_cole "The press won't wait. If we call a convening, the momentum might be siphoned. We get a photo-op, we show donors we can act now."
    hide cassian_cass_romano
    show dr_saira_ngoma at right:
        zoom 0.7

    dr_saira_ngoma "Momentum built on theatrical choices falls apart under stress. But momentum is necessary to keep people engaged through funding cycles. We need both the energy of now and the foundations of later."

    jonah_reyes "Whatever we do, Mira, make it something that keeps hands in the work. That keeps people like my crew fed and this place ours."
    "You feel Jonah's fingers — callused, warm — close around yours. The contact is a simple physics of comfort; it steadies your breath and sharpens your resolve. Lantern light slides across his face and finds the"
    "small lines around his eyes that belong to laughter and storms endured. You imagine telling him yes in ways that are both private and public."
    "A siren chirps from the Research Lighthouse, quick and clipped. Wind shifts; the sky that held gold an hour before is bruising at the edges. Rain begins, at first in an uncertain patter, then in earnest, tattooing the lighthouse roof."
    # [Scene: Research Lighthouse | Early Evening]
    hide jonah_reyes
    hide mayor_lynette_cole
    hide dr_saira_ngoma

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain drumming, instruments beeping intermittently]
    # play music "music_placeholder"  # [Music: Intensifying low percussion, heartbeat bass]
    "Inside the lighthouse, the hum of monitors makes a kind of companionable chaos. Your notebook, open on the table, is splashed with a bead of water that looks like a small planet. Tessa is pinning up"
    "a new roster; Saira runs her fingers through data and upturns a statistic with the pleased shock of someone watching a hypothesis hold. Mayor Lynette paces near a window. Cass taps at his tablet, jaw set."
    show tessa_kestrel at left:
        zoom 0.7

    tessa_kestrel "Mira, when you said this was about people, I didn't realize you meant people and sunsets. Jonah looks like an old sea god tonight."
    "Mira Kestrel: (blush burning) 'Tessa—'"

    tessa_kestrel "—I'm kidding. Mostly. But seriously, this is good. Real good."
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "I didn't come here to be famous. I came because my uncle couldn't rebuild a motel alone. If this keeps his roof above his head, I'll stand next to anyone who signs that paper."
    show cassian_cass_romano at center:
        zoom 0.7

    cassian_cass_romano "And if the paper ensures accountability and results, shouldn't we see that as protection, not possession?"

    jonah_reyes "Protection that comes with strings is still strings. Who cuts them?"

    cassian_cass_romano "We can write the scissors into the clauses."
    "The room vibrates with competing hopes — the fervent wanting of a small town and the polished promise of scalable solutions. You feel the pressure like a weather front: windows rattle; the rain makes the instruments"
    "sing a higher pitch; your pulse is a drum in your throat. Your survivor's guilt does not let you ride the high without examining the cost. Love presses against policy, making both sharper."
    "You picture the marsh during last month's high tide: where water used to claim a stoop, now reeds swayed. You think of Jonah on the docks, splintered rope in his hands and a laugh that made"
    "the repair crew move faster. You imagine signing a covenant that binds you to this small, imperfect, breathing model — and all the faces who would carry it forward. Alternatively, you imagine a ribbon-cut by someone"
    "in a suit who leaves when the cameras stop rolling, leaving the town transformed into a case study, not a home."
    "The lighthouse alarm steps up its tone — a measured urgency. Data streams refresh on Cass's tablet. Mayor Lynette walks to the center of the room, her posture the same as in a council chamber: practiced, declarative."
    hide tessa_kestrel
    show mayor_lynette_cole at left:
        zoom 0.7

    mayor_lynette_cole "We need a clear stance. The storm window is closing. If we want funding that scales this and secures long-term stability, I need a town voice to present. We can either present a cohesive local-led model with commitments, present a hybrid with oversight, or choose to delay and demand open bids. Each choice has consequences — but we must choose."
    "Your mouth is dry. Everything inside you hums — love, duty, the ache that used to be guilt transformed into an engine. Jonah steps so close your shoulders touch; he brushes a wind-tossed strand of navy-blue"
    "hair behind your ear with one steady hand. The touch is small and decisive; it anchors you and moves you at once."

    jonah_reyes "Mira. Whatever you choose, I'm with you. Not to bind you. To help hold the line."
    "Mira Kestrel: (thoughts racing, voice thin) 'How do we keep what we've built without selling it away? How do we move faster without losing the people who already risked everything?'"
    "Dr. Saira: (a hand on your arm) 'We write for both survival and soul. Terms can be technical and humane. But there is no perfect choice. There's only the one we make together, and the work after.'"
    "The rain hammers the roof as if to underline the moment. A gust throws the door open; for an instant, the lighthouse smells of wet stone and ocean iron and something else: the electric scent of decision."
    "Your chest is loud; your mind is a spool of scenarios—each one threaded with the faces around you. Jonah's hand, Cass's plea, Tessa's grin, Saira's steadying presence, the mayor's practical insistence. The town's small victories sit next to a very large opportunity. Hope tastes like salt and feverish sugar."
    "You close your eyes, feeling every heat and coolness at once — the warmth of Jonah's palm, the cold logic of Cass's proposal, the bright pragmatic flash of Mayor Lynette's optics, Saira's careful optimism. The arousal"
    "that has been coiling through this evening tightens into a single, very high note of pressure: decide where you place your personal and professional commitments."
    # play music "music_placeholder"  # [Music: Crescendo; a single high violin note, then layered percussion]
    hide jonah_reyes
    hide cassian_cass_romano
    hide mayor_lynette_cole

    scene bg ch5_4001e7_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A thunderclap, immediate and distant]
    "You inhale. The town's future, the shape of your heart, and the ethics of every signature on a contract hover like storm-lit gulls above the harbor. The moment is a cliff-edge — vertiginous, thrilling, irrevocable."

    menu:
        "I sign a community covenant — keep control local, deepen the marsh work, and commit to Jonah.":
            jump chapter6
        "I accept Cass's partnership to scale our solution but insist on formal community oversight.":
            jump chapter14
        "I refuse both, choosing instead to expose funds and demand open bids.":
            jump chapter15
    return
