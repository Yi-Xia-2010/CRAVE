label chapter15:

    # [Scene: Tideworks Lab | Dawn]

    scene bg ch15_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of refrigeration units, distant gull calls, paper whispering as a fan breathes]
    # play music "music_placeholder"  # [Music: Sparse, minor-key piano; slow heartbeat rhythm underneath]
    "You chose the quiet way: Elias Navin at your shoulder, Theo with his laptop open like a wound. You wanted answers before spectacle — to hold the city's trust in your hands and not hand it"
    "to others who would weigh it only in headlines. The lab smells of algae and hot metal; the leather of your journal is damp in your jacket where the tide left its memory."
    "Theo pushes a thumb across a screen, the scan unfurling like a tide map. 'Look,' he says, voice thin. 'Someone masked changes with plausible noise. Not just one file — multiple signatures overwritten with time stamps that fit the typical deployment windows.'"
    "Elias Navin leans in, breath fogging the screen. 'They altered the calibration offsets to favor false 'safe' readings. Whoever did this knew the sensor thresholds intimately.'"
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "Do we have provenance? An origin IP, a manifest chain?"
    show theo_mendes at right:
        zoom 0.7

    theo_mendes "Camouflaged. Routed through a municipal relay that should be secure. The edits are surgical — like they wanted it to pass every cursory audit."
    "You press your palm to the table, feeling the ridged paint under callused skin. The compass pendant against your sternum feels too cold. In your head, the living reef's slow swell and the Basin's mud pathways"
    "overlay the plaited code on the screen; every small edit is someone's choice to gamble with a life."
    "Elias Navin sits back, jaw tight. 'This is worse than vandalism. This is premeditated manipulation of a safety system. If we don't know how deep it goes, we can't trust the green lights.'"
    "Theo taps the log again. 'Also — there are gaps in the sensor history that match windows when crew rotations switched. Someone could have moved physical sensors, too.'"

    mara_kestrel "Show me the gaps. Print everything. We isolate the hardware we can, then—"
    show elias_navin at center:
        zoom 0.7

    elias_navin "—then we go to the hybrid site now. We don't give time for someone else to cover tracks."
    "Mara Kestrel [you] Your throat tightens. Two strategies braid in your head: the methodical integrity sweep, which can catch subtle tampering but takes time, or immediate inspection, which might find physical evidence but risks missing crafted digital forgery."

    menu:
        "Run a full integrity analysis here at Tideworks, methodically":
            "You tell Theo to queue a full checksum audit. Theo's fingers fly; the lab becomes a theater of graphs and cross-references. It feels like defending a harbor with a lamp and a ledger."
        "Head straight to the hybrid site—see with your own eyes":
            "You decide that seeing will force answers. Elias Navin nods once and unclips his sensor band; the air tastes more urgent. You pull on your parka and the lab's warm lamps blink like beacons behind you."

    # --- merge ---
    "Whatever you choose, the lane you take is narrow. You split the work: Theo runs the audits while you and Elias Navin go out to the waterline, because some crimes leave salt and stitch marks you can't fake with code."
    # [Scene: Hybrid Site | Afternoon, low cloud]
    hide mara_kestrel
    hide theo_mendes
    hide elias_navin

    scene bg ch15_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind pushing water through the framework; the metallic ratchet of a winch; distant hail on tarped supplies]
    # play music "music_placeholder"  # [Music: Low strings; a chord that doesn't resolve]
    "You arrive to an orchestra of small wrong notes. A mooring is chafed at an unnatural angle. A ballast bag sits where the plan says it should not. Someone's footprint tracked in the mud leads to"
    "a pack of cut cable ties. The tide seems to have rearranged only the things that mattered."
    "Elias Navin crouches at the base of a sensor tower, rubbing salt from the connector. 'Someone loosened the anchor bolts, but not enough to look like sabotage on first glance,' he says. 'They also altered the"
    "damping algorithms in the field firmware. If the wave sensors read within the wrong envelope, motors lock or don't engage when they should.'"
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "So the system will say 'all clear' while the mechanical fails."
    show elias_navin at right:
        zoom 0.7

    elias_navin "Yes. False negatives by design."
    "You run your hand along the nearest reinforced timber. The wood is warm from the day sun; a gull's cry cuts through the wind. Ivy's laughter — bright and reckless — drifts into memory and makes"
    "your stomach ache. If this fails in a storm, people will look for a person to hold; people always do."

    mara_kestrel "We should take the site offline. Remove the automated controls and put people on manual watch."
    "Elias Navin hesitates. 'If we stop the system and it really needs active attenuation for the next surge, manual watchers can't replicate the mechanical response. The models are built for milliseconds.'"
    "Mara Kestrel [you] Your mind lists who would be hurt if you delay: elders in the Basin who trust the hybrid, families who moved to higher ground expecting protection, volunteers who worked nights to plant the reef modules. The ledger of those names presses on your ribs."

    menu:
        "Override the sensors manually and hold the systems in safe mode":
            "You reach to the console, override keys cold under your fingers. For a moment you can feel an actual control, and the site hums at a different pitch—tired, constrained, but visible."
        "Trust Elias' recalibration patch and re-enable automation during daylight":
            "You watch Elias Navin upload his tweaks. His fingers tremble. The lights on the array flicker green like a promise; for a moment you imagine them keeping faith."

    # --- merge ---
    "You do both in small ways — a manual hold on critical actuators, a tentative re-upload of a corrected threshold. It feels indecisive, like tying two different ropes to one buoy and hoping the knot will"
    "hold. Theo's audit pings in your pocket: partial integrity, unresolved anomalies. Time shortens like a tide drain."
    # [Scene: Hybrid Site | Night — Storm]
    hide mara_kestrel
    hide elias_navin

    scene bg ch15_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind a roaring seam, wood splitting, distant shouts punctured by thunder]
    # play music "music_placeholder"  # [Music: Percussive strings, a descending motif that pulls everything down]
    "The storm comes faster than the models predicted. The city is breathing through a straw. The hybrid system, half-manual and half-automated, is a house with doors open to wind. The corrupted calibrations — the edits that"
    "seemed ornamental in the lab — translate into failed dampers and misdirected flows. A ballast bag tears; a mooring gives; a span of newly planted reef, butchered and unfastened, becomes a battering ram."
    "You remember the manual hold you set. It buys seconds. Seconds are mouths that take a lot to feed; they're not enough."
    show mara_kestrel at left:
        zoom 0.7

    mara_kestrel "Pull people back! Get the floats! Theo—where are you—"
    show theo_mendes at right:
        zoom 0.7

    theo_mendes "We lost comms on the north anchor. The actuator's not responding—"
    show elias_navin at center:
        zoom 0.7

    elias_navin "Secure the shore-line! Stop the inflow at the upper sluice!"
    "A section of the breakwater tips and rolls with a sound like something huge being unstitched. The water finds the Basin's low edge and spills into a row of temporary shelters where families had been told—repeatedly,"
    "gently—that they'd be safer tonight. You move, lungs burning, boots sinking in new river paths. You see someone pinned beneath a collapsed frame; you reach, but the current is faster than your reach."
    "You can name the technical failures later; now there are hands to hold and bodies that do not answer back. Outside the circling hazard lights, the storm steals brightness from faces and leaves them as wet, raw masks."

    mara_kestrel "Hold on—hold—please."

    elias_navin "We need a line. Tie a human chain—now."
    "You and Elias Navin form the chain. For a breath you are ordinary people refusing to be statistics. Then a surge slams a section loose. A woman you know — a neighbor who once braided Rosa's"
    "hair with reed — is taken. Her scream becomes a thin, inevitable thing. You feel it go through the chain and into your teeth."
    # play sound "sfx_placeholder"  # [Sound: Sirens in the distance, then closer. The crackling of a radio voice: "We need medics! Multiple casualties!"]
    # play music "music_placeholder"  # [Music: A single bowed note held too long, then silence]
    # [Scene: City Hall Glass Atrium (improvised triage) | Night, later]
    hide mara_kestrel
    hide theo_mendes
    hide elias_navin

    scene bg ch15_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Muffled sobs, urgent medic chatter, a public address system trying to cut through static]
    # play music "music_placeholder"  # [Music: Low pedal organ, funeral-lamp slow]
    "The hybrid's failure becomes a headline before the night is out. Someone in municipal press editing frames the story tightly: the project led by local volunteers; the leader who endorsed partial automation; the dangerous gamble. Jun"
    "Park's office releases a brief statement expressing shock and promising a full investigation. In the footage that will play in loop, you are the face people expect to blame."
    "You stand under the atrium's glass, water beading on your jacket, and you watch the crowd form a ring of accusation without a word. Ivy is there—paint still on her hands—eyes wide as if trying to"
    "keep the world from folding. Rosa's shawls cling to her shoulders and look suddenly very small. People you have argued with, loved, cajoled, and protected look at you like you carried the storm in your pocket."
    show jun_park at left:
        zoom 0.7

    jun_park "We will get to the bottom of what happened. But there is accountability. We will not allow experiments to gamble with human lives."
    "Mara Kestrel [you] Your mouth forms the words you have rehearsed a thousand times but never for this: an apology that tastes like a ledger entry. 'We did everything we thought would protect people. We did not intend—'"

    jun_park "Intentions won't bring back the dead, Ms. Kestrel. We will need to make hard choices."
    "The cameras drift to Elias Navin. He looks older under the emergency lights, the green pulse of his wristband dimmed. In the footage later, editors will splice his face next to yours and the narrative will tighten into a single, consumable story: hubris, failure, scapegoat."
    "You want to reach for him. Instead, you stand and let the room tilt and settle around the accusation."
    # [Scene: Basin | Dawn after the storm]
    hide jun_park

    scene bg ch15_f99e88_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft weeping, boots sucking from mud, a distant hammer on a broken window]
    # play music "music_placeholder"  # [Music: Sparse, mournful strings]
    "The co-op meetings after the storm are a kind of unspooling. People who built reefs together trade hard words like flints. Volunteers who once passed tools without thinking now count every bolt and question every signature. Meetings that were once filled with song are now khutbahs of accusation and fear."

    "Ivy stands on a crate and speaks too loud" "You said you'd protect us—where were you when it mattered? Who's going to watch the kids now?"
    "Rosa moves among them, gathering those who can be gathered. She takes you by the shoulder in passing, the gesture steady but not consolatory. Her hand is warm and carries the smell of dried seaweed and tea."
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "Grief is a tide that shows us what we loved. We will remember them. But we must also keep each other from tearing open this place for winners and losers."
    "You want to answer, to explain the edits, to show the audit logs Theo produced — but the logs are complex and the public wants a simple ledger: who is to blame. In between tears and"
    "technical diagrams, whispers begin: the mayor's office, Jun Park's 'measures', the municipal emergency plan that will now be easier to pass. In the crowd, the co-op fractures along lines you can name but cannot mend tonight."
    "Theo finds you in the back, eyes rimmed, laptop clutched to his chest. 'I pulled what I could,' he says. 'There are fingerprints on the code, but the chain of custody is gone. Whoever wanted this to succeed in failing covered their tracks well.'"
    "Mara Kestrel [you] Your hands feel like someone else's. 'Can you salvage anything? Proof to show who did this?'"
    show theo_mendes at right:
        zoom 0.7

    theo_mendes "Not yet. And the city's gonna move fast. People want answers now, not drafts. I'm sorry."
    # [Scene: Tideworks Lab | Later that week]
    hide rosa_alvarez
    hide theo_mendes

    scene bg ch15_f99e88_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain tapping the container's roof; the soft click of a closing locker]
    # play music "music_placeholder"  # [Music: Low solo cello; a single, elegiac line]
    "Elias Navin arrives with a duffel bag and a look that says he's already rehearsed his exit. He does not speak at first. You hold the silence like an accusation and a plea."
    show elias_navin at left:
        zoom 0.7

    elias_navin "I can keep working on the anchoring models away from here. Out of the spotlight. I can get funding through a research partner. Maybe scale it where it's safer."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "Or you can stand with the people who are being blamed."

    elias_navin "Standing doesn't fix the immediate harm. I—' He stops, fingers twisting at the strap of his watch. 'I keep thinking if only we'd caught the edits sooner. If only I hadn't trusted the thresholds the way I did. I ruined them the way I was trying to save them."

    mara_kestrel "You did what you could. You found the tampering. You tried to stop it."

    elias_navin "And still, bodies were lost. Names will be on the ledger. I can't stay where my presence will be a liability for people I'm trying to help. They need someone who will see them without the glare. I need to get to work where I can actually rebuild and not be the center of a political fire."
    "He avoids your eyes in the way of people who are making a choice that shames them. You imagine every path he might take — research partnerships, remote labs, nights alone repairing models — and each"
    "one is a narrowing of the life you had sketched together. He offers you a hand that says goodbye and something like forgiveness."

    elias_navin "I'm sorry, Mara. I'm so sorry."
    "Mara Kestrel [you] Your throat closes. Words fail like low tide. You clamp your hands around the compass pendant until it hurts."
    "Elias Navin picks up his duffel and steps toward the door. Theo watches him go, jaw working. Outside, rain steadies itself into a clean line down the container wall."
    # play sound "sfx_placeholder"  # [Sound: A bus engine starts; a figure disappears under the downpour]
    # play music "music_placeholder"  # [Music: A single descending cello line that resolves into nothing]
    "Elias Navin leaves before the month turns. He departs in a quiet that feels like a theft. You are left with a co-op that has split into factions: those who want to push harder for grassroots"
    "rebuilds, those who want to surrender sites to Jun Park's plan, those who simply stop coming. The ledger you keep grows and stains."
    # [Scene: Old Beacon Lighthouse (Ruins) | Dusk]
    hide elias_navin
    hide mara_kestrel

    scene bg ch15_f99e88_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind along the stones, a distant boat horn, the squeak of your boots on concrete]
    # play music "music_placeholder"  # [Music: Low, hollow choir; a single piano note repeating slowly]
    "You climb the broken spiral until you can look down on the town you loved like an ache. The Basin's new scars are visible in the stained river of mud. The hybrid site is a blackened"
    "notch on the horizon. In the rubble below you, small lights flicker as people try to stitch new tents and make lists of loss."
    "Rosa finds you at the lip of the old lantern room. She does not speak at first; the silence between you is the sound of a tide pulling back forever."
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "You chose to try. That is not a small thing."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "It doesn't feel like enough. They want someone to hold the storm—someone to be the scapegoat. They want a clean ledger."

    rosa_alvarez "Ledgers are for counting. They will count what they can, and they will not count what matters. You cannot bear the whole sea, child."
    "You look at your journal, at the damp paper inside, all your notations of protests, planting days, sensor thresholds, the lists of people who volunteered their time. The ink blurs where your palm has rested. The compass pendant is dull with salt."

    mara_kestrel "What am I now?"

    rosa_alvarez "You are a keeper of memory. You will carry them, and they will carry you forward. But some things change — people leave, houses are lost, friendships snap. That is the world we live in now."
    "Ivy does not stay. She joins a caravan of younger volunteers heading south to help another town, her hands already full of paint and new plans. The co-op's banner is folded and placed in a box;"
    "some sign it, some don't. The hybrid project lies in legal limbo and public shame; Jun Park's plan gathers votes and momentum."
    "You walk down from the beacon with salt in your hair and the taste of metallic grief on your tongue. There is no sudden vindication, no last-minute unraveling of conspiracies. The people you loved are splintered and rearranged into different kinds of survival."
    "You close your journal and place it in your bag. Your compass rests heavy against your sternum, an honest tick in a world that wants tidy numbers. You stand at the edge of a future that"
    "is smaller, lonelier, and harsher than the one you had imagined. There is no bright promise in the sky, just the long, necessary work of mapping what remains and tending the wounds as best you can."
    "You are tired. You are blamed. You are here."
    hide rosa_alvarez
    hide mara_kestrel

    scene bg ch15_f99e88_8 at full_bg
    "THE END"
    # [GAME END]
    return
