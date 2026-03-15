label chapter16:

    # [Scene: Offshore Project Site | Late Afternoon — Signing Day]

    scene bg ch13_3be532_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain on corrugated metal, the distant drone of generators]
    # play music "music_placeholder"  # [Music: Tense BGM — a tight drum under a high, anxious synth]
    "You stand at the long folding table by the container office, the leather folio warm and slightly damp beneath your palm. The addendum rests like a hinge: an accelerated roll-out with the promise of post-deployment audits"
    "scribbled into a clause whose language still leaves thin slivers of compromise. Your breath fogs the air. The pen feels heavy, an honest weight and a weapon at once."
    show elias_wren at left:
        zoom 0.7

    elias_wren "We can be in the water next week if you sign today. The window won't reopen—funding timelines, logistics. We want the same thing, Maia. Faster infrastructure saves lives."
    show maia_rivera at right:
        zoom 0.7

    maia_rivera "Faster—yes. But audits—binding, public, with consequences. No vague promises."

    elias_wren "Public audits will be part of the process. The first phase has to move now. We mitigate now, we iterate later."
    "You watch the signatures already inked at the bottom of the folio—contractors' names, the firm's mark—glossy and final. You imagine the levee as a scaffold of scaffolding and metal braces. You imagine the crews moving like ants. You imagine Jonah at the harbor, a silhouette you've learned to read."
    show jonah_kade at center:
        zoom 0.7

    jonah_kade "You're sure this is the only way?"

    maia_rivera "I— We don't have time for perfect. We have to start."

    jonah_kade "Start where? On someone else's timetable? Maia, we need protection, not promises."

    maia_rivera "I'll make sure the audits are enforced."

    elias_wren "Then we begin."
    hide elias_wren
    hide maia_rivera
    hide jonah_kade

    scene bg ch13_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A generator coughs to life; metallic clanking starts in the lots beyond]
    # play music "music_placeholder"  # [Music: Drumbeat rises — urgent, thudding]
    "You hear the first trucks pull into the lot. Clean modular pumps, LED-lit housings, polished panels—immediate symbols of action. The town, hungry for something tangible, begins to gather."

    menu:
        "Go out to the lot and speak to the arriving crews":
            "You step into the rain and call out instructions. Workers nod; their faces are professional and neutral. You give a short speech about teamwork, and the machines begin to unload under your voice, efficient and too bright."
        "Stand with Jonah and watch from the boardwalk":
            "You stay under the awning. Jonah's jaw works. He doesn't speak. Watching the machines offload feels like watching a ship's hull be stitched while the crew still argues where to set the rudder."

    # --- merge ---
    "Continue to the Harbor and Boardwalk scene"
    # [Scene: Harbor and Boardwalk | Early Evening — Equipment Deployment]

    scene bg ch13_3be532_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Workers shouting over engines, gulls muffled by rain, murmurs of the crowd]
    # play music "music_placeholder"  # [Music: Tense strings — rising, restless]
    "The crowd is a crowded wave of thank-yous and questions, relief braided with doubt. Small businesses set up temporary lights; a child claps to the rhythm of machinery. The first impression is celebration—metal and progress—but you can taste something metallic and wrong at the back of your teeth."
    show lupe_kade at left:
        zoom 0.7

    lupe_kade "Maia — the fish maps are shifting. We've been tracking daily schools, and the catch corridors are rerouting already. The pumps are changing the currents near the shoals."
    show maia_rivera at right:
        zoom 0.7

    maia_rivera "Show me the data."

    lupe_kade "I'll pull it up—now.' (She taps at her tablet; a heat map blooms in the glow: patches of valuable grounds thinning, new ripples opening off the channel.) 'If the pump runs at full tilt without the levee finished, the shoals reposition. Jonah's nets—"
    show jonah_kade at center:
        zoom 0.7

    jonah_kade "Lupe, don't—' (He stops himself, looks at you.) 'We can adapt, but we can't afford sudden holes in the map. Folks buy with last month's checkbook."

    maia_rivera "We built contingencies. We'll mandate phased shutoffs if monitoring shows undue shifts."

    lupe_kade "Contingencies are words until someone loses a season."

    jonah_kade "You promised the cooperative oversight. The audits are supposed to be binding."

    maia_rivera "They will be binding. I won't sign anything that isn't."
    "Jonah looks at you, searching. There's a tremor in his hands—an old fear of abandonment, or of being led by someone who doesn't know the sea the way you do."

    jonah_kade "You already signed, Maia. The machines are here."
    "The words hang like a buoy. The crowd continues to cheer, louder, relieving themselves into the machines rather than into conversation. For a second you are applauded—praised for action you still have to correct."

    menu:
        "Pull aside a site foreman and insist on immediate conservative operation limits":
            "You grab a foreman, point at the monitoring screens, and argue for conservative flow ceilings. The foreman blinks, nods, and radios down orders that slow one pump's cycle. The machines hum with a slightly gentler haste."
        "Allow the initial schedule to proceed while you prepare audit riders":
            "You let the crew follow the plan. Your hands go cold as the pumps spool up. You arrange for the audit riders to be drafted, promising to be fierce later. The water moves in a way you can't yet measure."

    # --- merge ---
    "Continue"
    # [Scene: Flooded Historic Quarter | Months Later — After the Predicted Surge]
    hide lupe_kade
    hide maia_rivera
    hide jonah_kade

    scene bg ch13_3be532_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The thick, wet slap of floodwater against boarded thresholds; low angry murmurs; distant crying]
    # play music "music_placeholder"  # [Music: Crescendo — strings and low brass, insistent and pained]
    "Months slide like an oil stain. The season's predicted storm swelled into something crueler than the models had allowed: an intense surge riding a wrong wind. The unfinished levee takes the brunt; modular pumps overwork, break,"
    "and some are still in transit. Water finds old pathways—the ones memory thought lost—and reopens them."
    "You arrive at the Flooded Historic Quarter with your boots sucking wet mud and your stomach a stone. Windows show waterlines, family photographs floating face-down in waterlogged frames. A bakery you used to map for a"
    "grant sits with flour sacks sodden and crusty. A mural of the town's founding is peeled at the corners."

    "Townsperson 1" "We voted for protection and got half-built promises."

    "Townsperson 2" "My storefront didn't collapse. The pumps slowed worse. What would have happened without them? Thank you, but—"
    "Voices fragment into accusation and gratitude. Your name snakes through both like a tide—blessing and blame braided into one syllable."
    show jonah_kade at left:
        zoom 0.7

    jonah_kade "You thought you'd buy us time. You thought audits would save us later. But timing mattered. The levee wasn't finished. The pumps weren't enough."
    show maia_rivera at right:
        zoom 0.7

    maia_rivera "We moved as fast as we could."

    jonah_kade "We? Who's 'we', Maia? You signed their timelines."

    maia_rivera "I signed to prevent worse. Paralysis wouldn't have saved anyone."

    jonah_kade "Maybe. Maybe not. But you were the one at that table, and people look to you."
    show elias_wren at center:
        zoom 0.7

    elias_wren "We followed the contract. The surge exceeded the window in the models. We moved resources where we could."

    maia_rivera "We need a full inventory of damage. We need to prioritize cultural sites and livelihoods. We need the remaining phases accelerated and the audits enforced."

    "Townsperson 3" "Enforce? You are the one who signed the deals! We trusted you!"
    "The accusation lands. It is meant to wound and it does. The crowd's faces blur into a tide of expectation and hurt. You can taste salt and old coffee and the iron tang of guilt."
    # play sound "sfx_placeholder"  # [Sound: Distant generator fails with a metallic whine; someone begins to cry quietly]
    # play music "music_placeholder"  # [Music: Drumbeat tightens to a near-clack — high arousal]
    hide jonah_kade
    show lupe_kade at left:
        zoom 0.7

    lupe_kade "Jonah's nets are missing their old trails. My records show permanent shift. People are losing seasons. This isn't just water; it's memory."

    maia_rivera "..."
    hide maia_rivera
    show tomas_rivera at right:
        zoom 0.7

    tomas_rivera "I told you once about a tide that took the boats clean out of the moorings. We learned to read the currents after. But sometimes, child, we fix one thing and the sea remembers a different history. You did something. The trick is—what will you do next?"
    hide elias_wren
    show maia_rivera at center:
        zoom 0.7

    maia_rivera "..."
    # [Scene: Rooftop Garden of Maia's Childhood House | Dusk]
    hide lupe_kade
    hide tomas_rivera
    hide maia_rivera

    scene bg ch13_3be532_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A softer wind, the city below settling into a brittle, uneasy quiet]
    # play music "music_placeholder"  # [Music: Low, melancholy strings — a single violin line wrenched with regret]
    "You sit on the battered crate that serves as a table, your Moleskine open and swollen with rain-smeared pages. The pencil lead smudges your notes about audit schedules and repair timelines. Fingers press into rosemary; the needles release an herbal sting that is oddly consoling and sharp."
    "Your chest is a tightly wound drum. Every name—Jonah, Lupe, Tomas, the town—echoes. You run a finger across a list of promised clauses and amendments, and the ink smears slightly as if even your plans can weep."
    show maia_rivera at left:
        zoom 0.7

    maia_rivera "..."
    "You think of Elias' brief kindness at the signing, his eyes like tempered steel. You think of Jonah's quiet hollow shape at the harbor. You think of Lupe's maps, of Tomas' sighs. The rooftop is small"
    "and high and the sound of the sea is a distant slow pulse, as if the world itself were breathing and weighing."
    "This is the low before any rise."
    # play music "music_placeholder"  # [Music: Single note held, then cut to silence]

    menu:
        "Call Jonah and ask him to meet you now":
            "Your thumb hovers, then presses. Jonah answers after a beat. He says he'll come, voice low. Both of you will speak in the raw, which may or may not be what you need."
        "Draft a public statement now and send it to Mayor Rosa":
            "You begin to write, words clumsy with apology and policy. It feels like sending a bandage through the mail. You can already hear both gratitude and scorn forming."

    # --- merge ---
    "Continue"
    # play music "music_placeholder"  # [Music: A single tight pulse — the chapter's emotional arousal peaking]

    menu:
        "Double down on corporate partnerships to finish infrastructure quickly.":
            jump chapter17
        "Publicly accept responsibility and lead a grassroots rebuilding with strict oversight of the remaining projects.":
            jump chapter19
        "Resign from the implementation board and allow the mayor to take charge.":
            jump chapter19
    return
