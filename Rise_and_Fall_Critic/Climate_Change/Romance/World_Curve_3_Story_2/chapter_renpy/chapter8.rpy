label chapter8:

    # [Scene: Sea Barrier Construction Site | Night]

    scene bg ch8_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain stinging canvas; distant shouts; the metallic clank of a gate being forced]
    # play music "music_placeholder"  # [Music: Low, grinding cello with a slow heartbeat pulse]
    "You taste salt and diesel at once — the sea on one side, machines on the other. Floodlights slice rain into silver knives. The protesters are a wet, moving line of breath and banners; the contractors'"
    "tarpaulins flap like raised hands. Something large and official smells like a rope, a list of names, and inevitability."
    "Your wrists go hot where the cuffs bite. Metal pulls at your skin in a way that makes decisions feel physical: compressed, immediate, impossible not to notice. A pair of officers stand too close; one reads"
    "your name off a clipboard as if it were a weather report. The van's metal floor hums with the rain's rhythm under your soles."
    "You keep your eyes on Samir across the van — just far enough to be private, close enough that you can read every line in his face. The fear in his eyes is small and sharp,"
    "like a pebble that can be swallowed or spit out. He mouths something you don't hear. You watch his jaw work; he is trying not to break in front of you."

    "Officer Hayes" "We can let you go with a citation if your people disperse. You understand the charge—obstruction. Sign here."
    show mara_lin at left:
        zoom 0.7

    mara_lin "I know the charge.' (you say it quietly, too aware of how your voice carries on cold air) 'But the contractor cut permits. The city—"

    "Officer Hayes" "City decisions aren't for the street. You'll get time in processing if you make this difficult."
    "Your notebook is taped into its sleeve at your hip; your compass bounces each time the van sways. For a moment you imagine the compass swinging free and clattering into mud, small and unimportant. Then you push the image away. Small things matter in a flood plain."
    show samir_reyes at right:
        zoom 0.7

    samir_reyes "They brought more contractors than they needed. This was planned. They wanted an excuse."

    mara_lin "Then don't give it to them. Keep calm. Keep breathing."
    "Samir's fingers flex once on the seam of the bench. He wants to say more. He wants to promise things that are not his to promise. You understand that urge."

    menu:
        "Mutter instructions to Samir":
            "You whisper a quick plan: small teams, time stamps, an agreed waypoint. Samir nods, eyes fierce with a fragile hope."
        "Hold your silence and observe":
            "You keep your mouth shut and catalog — faces, badge numbers, floodlight angles. Silence becomes a different sort of plan; Samir reads your restraint like a measure of resolve."

    # --- merge ---
    "Narrative continues"
    "Officer Hayes returns and the paperwork shuffles like a small violent wind. When your name is stamped and you are let go with a thin print of authority and a heavier print of warning, the cuffs"
    "leave a ring of red on your wrists that smells faintly of iron and consequence. You step into rain that feels colder after the metal."
    hide mara_lin
    hide samir_reyes

    scene bg ch8_6b08b4_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant voice on a loudspeaker—indistinct, procedural]
    "You scan the shoreline; the encampment has been pushed back in places, embers of a last night's bonfire smoking like faint regrets. Nova Duarte is a moving line in the rain — her hair plastered, her"
    "coat like a flag. She sees you, and for a fraction of a second something flashes in her face that is not anger and not relief but something split in two. You don't know whether to"
    "go toward it or away."
    show nova_duarte at left:
        zoom 0.7

    nova_duarte "They came at midnight. Bulldozers. No notice. We held the line and they brought lawyers."
    show mara_lin at right:
        zoom 0.7

    mara_lin "What did they take?"

    nova_duarte "Enough to make a headline. Not enough to make them stop.' (she looks at your wrists, then at your face) 'You were cuffed."

    mara_lin "Briefly. Samir was there."
    "Nova Duarte closes the distance until rain hides the rawness in her expression. She speaks low so the police can't overhear."

    nova_duarte "You know this would happen. You know how they operate. Why were you there at the barricade when I said we needed to—"
    "You reach for an explanation and then fold it back because explanations are paper boats that turn under the first wave. Nova Duarte's eyes are steel, but not unreadable; they are layered. Anger sits on top"
    "of something else — grief, calculation, an ember of terrified hope you can almost see."

    menu:
        "Tell Nova you believed the blockade would hold the line":
            "You say the truth, voice breaking on the last word. Nova's jaw hardens; she lets out a sound that might be a laugh or might be a cry. The two of you stand, rain between you, sympathetic and exposed."
        "Deflect and ask about legal options":
            "You force your face calm and ask about lawyers, about evidence. Nova blinks, caught off-guard by the change in topic, then answers in quick, practical paragraphs — a map of risks and possible countermoves."

    # --- merge ---
    "Narrative continues"
    # [Scene: Police Van | Night, moving slowly]
    hide nova_duarte
    hide mara_lin

    scene bg ch8_6b08b4_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Van engine, radio chatter; a far-off siren like a mourning bell]
    # play music "music_placeholder"  # [Music: Sparse piano, single notes falling like rain]
    "Inside the van, the world is shrunk to plastic, vinyl, and the muted conversations of official hands. You watch badge numbers pass like constellations. Samir stares at the floor, then at your hands. He runs his"
    "thumb over the cuff mark as if it were a rosary to slow the racing of his thoughts."
    show samir_reyes at left:
        zoom 0.7

    samir_reyes "You didn't have to be at the front line alone. Why did you go with—"
    show mara_lin at right:
        zoom 0.7

    mara_lin "We agreed.' The word is not an absolution. It is a fact that presses like a stone. 'We thought presence would make a difference."

    samir_reyes "Presence is one thing. The city wants an excuse to act decisive. They got one."
    "You swallow. The things you did to be useful — the small acts of presence, of documentation, of negotiating emotion into itinerary — now feel like brittle tools against a sledgehammer."
    # [Scene: Safe House — Backroom | Later that night]
    hide samir_reyes
    hide mara_lin

    scene bg ch8_6b08b4_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain against tin roof; the hum of a single kettle on a hotplate]
    # play music "music_placeholder"  # [Music: Slow, ambient strings; a low, sinking tone]
    "The safe house smells of wet wool and citrus tea, a domesticity that feels almost offensive after the cold of custody. You take off your boots and peel away the damp like a skin. In the small lamp light, the red ring around your wrists is an accusation."
    "Professor Anika's silhouette is already at the map wall, a cascade of palms and pins and careful lines. Her voice is paper-calm but her hands betray a scientist's agitation as she taps routes and budget items."
    show professor_anika_bhat at left:
        zoom 0.7

    professor_anika_bhat "You can't be arrested again and expect to keep the grants. Liability clauses are explicit. We've already got letters from one contractor; if Mayor Chen leverages this—"
    show mara_lin at right:
        zoom 0.7

    mara_lin "She will."

    professor_anika_bhat "This is bigger than a single night. You must understand repercussions. A charge, even a misdemeanor, can be used to bar your organization from bidding on community grants. They will tie your actions to 'reckless obstruction' and retroactively justify emergency measures."
    "Nova Duarte watches from the doorway, rain still in her hair. There's an energy around her like a pressed spring. Her anger is a heat you can feel in the lamplight."
    "Nova Duarte [Low]: 'They want panic. They want us to be seen as reckless so they can step in 'to save us.' Heloise loves being a hero."

    mara_lin "Heloise is using fear to fast-track a contract."

    professor_anika_bhat "And fast-tracking removes public comment. It removes environmental review. It removes us. If the city can sign an emergency clause, the seawall goes up without the community's input. That's the legal lever they'll pull."
    show samir_reyes at center:
        zoom 0.7

    samir_reyes "They started the bid already. There were memos — two already — in the paper today. They're using our moments of resistance as a rationale. They spin us into the story they want."
    "Your throat tightens around words you cannot throw away. You replay every shouted chant, every blocked access route, every late-night planning session. The ledger of consequences grows and grows in your chest."
    hide professor_anika_bhat
    hide mara_lin
    hide samir_reyes

    scene bg ch8_6b08b4_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Notification ping; the kettle drops to silence]
    "You look at the alert and then at the map. The front line of the storm is a shadow that moves faster than dissent and cheaper than consensus. The mayor's photo is in the corner of a news crawl, the headline crisp as an order."
    # [Scene: Safe House — Later, near midnight]

    scene bg ch8_6b08b4_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant rumble of thunder; the house's old pipes singing]
    # play music "music_placeholder"  # [Music: A single, mournful cello line under a hush of static]
    "You lie awake with the compass cold against your sternum. Sleep doesn't come because your mind is a ledger of 'if' and 'should.' If you had stepped back. If you had insisted on negotiation. If you"
    "had pushed for a different tactic. They all line up like low tide and reveal things you had buried for functionality: guilt, the memory of a house swallowed by a storm, the sound of a neighbor's"
    "keys dropping on a wet floor and never being found."
    "Nova Duarte sits across the room, ensconced in shadow and lamplight, her profile carved by the map's glow. She speaks without turning."
    show nova_duarte at left:
        zoom 0.7

    nova_duarte "You know this puts us all at risk. Not just the movement. You."
    show mara_lin at right:
        zoom 0.7

    mara_lin "I know."

    nova_duarte "When decisions are made in the gray zone between 'too bold' and 'too timid,' they like to blame the gray. We are that gray right now."

    mara_lin "So what's the next move?"
    "The question is both practical and moral; it feels like a pebble into a deep pool and you wait for the rings. Outside, the bay breathes and draws a line further out than it has in memory. Everything is exposed."
    show professor_anika_bhat at center:
        zoom 0.7

    professor_anika_bhat "You need to consider whether pressuring now—escalation—will give them the exact headline they need to justify a bypass. Or whether stepping back and forcing a legal, mediated table will buy breathing room. Or whether we should retreat tactically, shift to pilot projects that don't require them to notice us until they're already behind us."
    "Nova Duarte's mouth forms a tight, almost imperceptible smile."

    nova_duarte "And what your scientist friend is politely spelling out is: choose something or watch the city rebuild without you."
    "Samir reaches for your hand across the coffee table and squeezes. The touch is small salvage."
    hide nova_duarte
    show samir_reyes at left:
        zoom 0.7

    samir_reyes "Whatever you decide, I'm with you."
    "You feel the pressure of that solidarity as a warm weight. But the world has narrowed to legal papers in a lawyer's briefcase, cold holding cells, and the mayor's decisive hand on a contract stamp."

    menu:
        "Confront the mayor publicly—call for a protest when the contract is announced":
            "You imagine the rally — the crowd swelling, Nova at the front, the cameras forced to show the human faces under banners. It tastes of adrenaline and risk. Nova's eyes sharpen; she nods as if the plan already exists."
        "Ask Professor Anika to draft a legal challenge and open a mediated channel":
            "You picture Anika drafting injunctions, tranquil hearings, slow paper that chokes the city's haste. The idea soothes you; Nova's jaw tightens at the thought of waiting."

    # --- merge ---
    "Narrative continues"
    "The radio in a volunteer's bag crackles: a dispatcher reads, clinical and final, that the mayor has invoked emergency powers for an 'immediate seawall deployment' citing the storm warning. The phrasing is surgical; the implication is"
    "absolute. Mayor Chen's seal is a small, bright certainty in a night already full of uncertain shadows."
    "Nova Duarte stands and moves through the room like a storm front."
    hide mara_lin
    show nova_duarte at right:
        zoom 0.7

    nova_duarte "They're taking our framing and making it theirs. We can either push until they talk — force them into the bargain — or we back down and they build the wall in our name and call it protection."
    hide professor_anika_bhat
    show mara_lin at center:
        zoom 0.7

    mara_lin "If we force them, it could turn violent. If we back down, the community loses a voice. If we negotiate, we give ground."
    hide samir_reyes
    show professor_anika_bhat at left:
        zoom 0.7

    professor_anika_bhat "And liability. If you're named in litigation, funds dry up. If we hold out and they're aggressive, people get hurt in the short term."

    nova_duarte "I don't want 'might' or 'if.' I want action."
    "Her words are a blade. You feel the old, familiar tug — the idealist in you that wants to keep everyone safe colliding with the organizer who knows that safety sometimes demands sacrifice."
    "You replay the night's images: the van's metal, the officer's paper pad, Samir's small frightened face, the mayor's signed emergency order glazing a headline. The tide is out and everything is exposed — not just mud and pilings, but the raw choices that will scar the city for years."
    # play music "music_placeholder"  # [Music: The cello slows to a single, sustained tone; the lamp flickers]
    "You breathe. The air tastes like old promises."

    menu:
        "Escalate direct action—force the city to negotiate under pressure.":
            jump chapter9
        "Seek mediated talks with a coalition of residents, scientists, and a reluctant municipal liaison.":
            jump chapter14
        "Pull back to regroup—focus on building tideside restoration pilots while avoiding legal exposure.":
            jump chapter9
    return
