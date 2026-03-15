label chapter12:

    # [Scene: Community Shelter & Town Hall | Dawn]

    scene bg ch11_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense, rising strings with an insistent percussion undercurrent]
    # play sound "sfx_placeholder"  # [Sound: Distant helicopter, gulls, intermittent rain tapping the windows]
    "Narration:"
    "You wake to the thin ache that follows too many hours steering a conversation toward truth. The shelter is quieter now—half the cots folded, half your neighbors back at their homes or jobs—yet the room smells"
    "of last night's coffee, damp coats, and the residue of heated arguments: the copper tang of adrenaline turned to routine."
    "You press your palm to your throat where your scarf is too tight from sleep and realize you haven't actually slept. Your field notebook is open beside you; the maps inside look as if someone has taken an eraser to the horizon and left only plans."
    show lito_reyes at left:
        zoom 0.7

    lito_reyes "You okay, May? You look like you wrestled with Camille's whole legal team in your sleep and lost."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "I might've traded blows with her in my head. Same outcome: I woke up sweaty."
    show amaya_chen at center:
        zoom 0.7

    amaya_chen "Mayor Sofía called. She promised to keep her word on the audit order, but legal pushback from Duval's firm is already filed. They've accelerated work on the northern reclamation belt."
    "Narration:"
    "The words fall like stones, but the cord of resolve beneath your ribs tightens instead of snapping. Accelerated construction is a threat, yes—an insult—but it also clarifies something you've known since the hearing: this moment will be decided by momentum as much as law."
    "Lito moves like a shadow in the doorway, boots thudding across wet floorboards, face set in that blunt way that says he has measured risk and found it unacceptable. Amaya arrives behind him, scarf a bright"
    "slash against the gray, carrying a stack of leaflets and that particular sharp optimism she keeps for mornings like this."

    menu:
        "Tell everyone to take the day and rest":
            "You let out a long breath and say nothing for a beat, then suggest a slow tide of volunteer shifts instead of an all-out push today."
        "Push for an immediate organizing sprint":
            "You clap your hands once and start mapping out block-by-block calls; Amaya's eyes light with the fuel of action."

    # --- merge ---
    "Scene continues"
    # [Scene: Harbor Boardwalk | Midmorning]
    hide lito_reyes
    hide maya_reyes
    hide amaya_chen

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Storm siren test in the distance; gulls keening; the boardwalk vendor flipping a crepe]
    # play music "music_placeholder"  # [Music: Fast acoustic rhythm with a hopeful brass lift]
    "Narration:"
    "You go outside because staying inside would feel like hiding. The boardwalk smells of frying dough and cold metal; the wind whips at your scarf and strips some of the fog from the bay. A storm"
    "warning lights up your phone with that urgent, thudding tone—fast moving system off the coast. The weather behaves like a metronome for politics now: a natural event that makes everything immediate."
    show elias_stone at left:
        zoom 0.7

    elias_stone "I read Rowan's annotations last night. The living-shore pilot could be scaled, with modifications. There's a fund—national—looking for proven community models. If we present the retrofit as a replicable package, they'll fund construction and monitoring. It could be the marsh and—' (He swallows.) '—it could be a model for other cities."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "National money solves the funding hole. What's the catch? They don't give free work away."

    elias_stone "They want scale. They'd ask me to lead design teams that deploy our model across regions. I could stay connected, but I'd be further away—logistically and, maybe, in the day-to-day. It would mean me stepping back from hands-on local coordination."
    "Narration:"
    "A wind shoved salt into your eyes. The thought of Elias drafting plans in a distant office feels like a slow erosion: incremental, inevitable. But the alternative is seeing the marsh carved away parcel by parcel."

    elias_stone "I don't want to escape. I want leverage. I think I can protect more places if I step into that role. But I also know what that asks of us—of you. I don't want to blindside you."
    "Narration:"
    "You hold his gaze, searching for the man who taught you to read tide lines, and find him there, honest and flinching."

    menu:
        "Ask him how often he'd return":
            "You press for details—travel cadence, decision-making power—and Elias lays out a rough schedule: alternating months, a two-year pilot, an advisory local core team."
        "Tell him to take it; the marsh matters more":
            "You hear your voice say it before your chest settles—then panic pinches your throat as you imagine empty spaces on the mudflats. Elias reaches for your hand and doesn't let go."

    # --- merge ---
    "Scene continues"
    # [Scene: Mayor Sofía's Office | Late Morning]
    hide elias_stone
    hide maya_reyes

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain intensifying outside; the soft click of a pen; a distant construction thrum]
    # play music "music_placeholder"  # [Music: Low strings underpinning a sense of pragmatic urgency]
    "Narration:"
    "Mayor Sofía greets you with the tired gravity of someone who sleeps and wakes inside the seams of compromise. Her face has the lines of negotiating budgets and expectations; her voice carries the careful cadence of one who must make other people's losses calculable."
    show mayor_sofa_lvarez at left:
        zoom 0.7

    mayor_sofa_lvarez "We have to move fast. I can authorize emergency shoring—temporary sea defenses, pilings, sandbags in vulnerable coves. But the funding is conditional. The city can only underwrite so much without jeopardizing other wards. Duval's firm will argue obstructionist tactics if we don't show we're protecting the city's broader interest."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "What does conditional mean?"

    mayor_sofa_lvarez "A coordinated land-swap. Two neighborhoods will accept relocation of some parcels—densest risk zones—so we can concentrate shoring and long-term protections where they secure the majority. It will save more homes overall, but yes: it asks some to give up shoreline they love."
    "Narration:"
    "You picture the map she points to: blue and gray like bruises where communities would be shifted, streets redrawn for safety. The proposal is efficient, a compromise forged in finance and liability, but it bleeds memory"
    "and place: coves where your family once docked small boats, a stretch of reeds Lito taught you to fish at."

    mayor_sofa_lvarez "I don't offer this lightly. It's immediate protection. It reduces displacement overall. I know it asks for pain."

    maya_reyes "And Camille Duval? How does this play with Duval's team?"

    mayor_sofa_lvarez "Politically, it splits the market. It gives the administration an actionable plan that isn't just 'stop everything'—it buys time. Camille Duval's firm can still claim parts of the coast, but the shoring will limit the damage to the most critical infrastructure. It's messy, but I think it saves lives."
    # play sound "sfx_placeholder"  # [Sound: A thunderclap rattles the window; the room smells suddenly of ozone and wet concrete]
    "Narration:"
    "The rain's tempo quickens outside as if to drum the urgency into your bones. Each option is an arithmetic of human cost: the national fund offers scale at a personal distance; the land-swap promises bulk protection"
    "at the price of cherished coves; doubling down keeps hearts local but risks legal and physical exhaustion."
    show amaya_chen at center:
        zoom 0.7

    amaya_chen "We can't let them pick off pieces of our home. Solidarity actions this week—sit-ins at Duval sites, coordinated legal funding drives—we can stall construction and keep pressure up."

    maya_reyes "Amaya, how many volunteers do we honestly have left?"

    amaya_chen "Thinner than last month. But organized and furious. That matters."
    "Lito: (From the doorway, blunt as broken glass) 'Furious won't hold the line if the levee gives. Are we fighting to keep everything or keep most of us? Be real, May.'"
    "Narration:"
    "Lito's question lands like a line through a tide map; it makes the choices legible because it forces you to define 'we.' You feel the ocean's logic under it—conservations of mass and loss. The room's air tastes of metal and wet wool."
    hide mayor_sofa_lvarez
    show elias_stone at left:
        zoom 0.7

    elias_stone "If I take the national role, I can program protective measures into federal grants, into procurement. That could secure long-term living-shore budgets. It doesn't erase the ache of distance, but it does scale the victory."

    maya_reyes "Your chest tightens not with panic but with a rising, hot clarity. The arousal that started as fatigue is now coiled toward action. Each voice—Amaya's solidarity, Lito's bluntness, Sofia's pragmatism, Elias' offer—pulls in a different direction. None are betrayals; all are honest tries at preservation."
    hide maya_reyes
    hide amaya_chen
    hide elias_stone

    scene bg ch11_e67f19_4 at full_bg
    # play music "music_placeholder"  # [Music: Swelling strings pushing toward a hopeful peak]
    show mayor_sofa_lvarez at left:
        zoom 0.7

    mayor_sofa_lvarez "I won't pretend the swap feels clean. But the city's duty is to protect as many as possible. If you help me sell this plan to the neighborhoods, I'll allocate the emergency funds and convene a community panel to oversee relocation choices."
    show amaya_chen at right:
        zoom 0.7

    amaya_chen "Selling a plan? We don't sell out our neighbors, Mayor—we organize to make the real option possible for everyone. The land-swap is a political tool, but it can be used with dignity."
    show lito_reyes at center:
        zoom 0.7

    lito_reyes "Dignity's fine on paper. Out here, dignity is a boat that needs a dock. Which ones get saved matters. Who decides?"

    "Elias Stone (Stepping closer)" "We can decide together. But we need to pick a path. Momentum won't wait."
    "Maya Reyes: (Softly, to yourself, louder to them) 'Then we need to ask what we can sleep with. What choice produces a future we're willing to carry?'"
    "Narration:"
    "Your heartbeat drums in your ears. The storm warning bleats again—urgent, irrevocable. Outside, the rain becomes a sheet and a question at once. Inside, decisions are a different kind of weather: they erode and build in"
    "equal measure. You feel hope, not because any path is painless, but because each path contains a strategy, an honest stake, a promise to continue."
    "You look at each person: Lito, clenched jaw a portrait of livelihood; Amaya, electric with collective action; Elias, open-handed and almost apologetic; Mayor Sofía, pragmatic and tired. None of them are asking for your capitulation. They are offering you the mantle of choice."
    hide mayor_sofa_lvarez
    hide amaya_chen
    hide lito_reyes

    scene bg ch11_e67f19_5 at full_bg
    # play music "music_placeholder"  # [Music: Full rise—strings, percussion, brass—bright and urgent]
    "Narration:"
    "This is the point the hearing prepared you for—the compression of all small acts into a single axis. You taste salt and metal, and beneath it, something like possibility. You feel fear's hum, but hope's drum is stronger."
    "You inhale, bracing for the commit that will set a course for the marsh and for the life you want to build. The options stand before you, bright and painful and necessary."

    menu:
        "Accept coordinated land swaps and emergency shoring to protect the majority.":
            jump chapter14
        "Support Elias taking a national role to scale adaptive designs—sacrifice daily proximity for broader influence.":
            jump chapter18
        "Double down locally—organize a sustained civil campaign and legal defense.":
            jump chapter7
    return
