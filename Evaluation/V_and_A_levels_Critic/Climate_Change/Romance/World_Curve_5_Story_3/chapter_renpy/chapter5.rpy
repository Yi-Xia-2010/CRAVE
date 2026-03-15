label chapter5:

    # [Scene: Verdant Terrace | Late Afternoon — Storm Arrival]

    scene bg ch5_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Sharp percussion, rising tempo]
    # play sound "sfx_placeholder"  # [Sound: Wind battering string lights; distant, insistent sensor pings]
    "You were letting the small victories sit on your palm like warmed coins when the sky turned its face. The pilot was humming—green LEDs tracing the perimeter like constellations—but the air changed before anyone could name"
    "it: pressure tightened, the salt taste on your tongue sharpened, and the terrace's smell—earth, compost, frying oil—was chased by a metallic tang."
    show aiko_mori at left:
        zoom 0.7

    aiko_mori "Everyone—check the east perimeter. Watch the drains."
    "You move without thinking. Hope is no preparation for the way weather can be an accusation. Under the tarp, volunteers snap into action; shoes slap wet wood, hands find tools. Rain finds seams the way guilt finds apologies."
    hide aiko_mori

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A long, lower-frequency howl, like the city exhaling]
    "A sensor's ping goes brittle—then a new tone, urgent and raw. Your pendant lamp winks as if startled."

    menu:
        "Run to the Subbasement Data Lab":
            "You cut across the terrace, water sloshing your boots, breath shallow as you imagine racks of servers and neon tidal models. The lab's door is heavy; your palm stings against the metal latch."
        "Stay to shore the terrace drains":
            "You stay, shoulder to the wheel with volunteers, palms prying at clogged grates. Mud tastes faintly of iron under your fingernails, but you can hear, somewhere below, the high keening of electronics."

    # --- merge ---
    "Continue to next scene (Tideward Promenade | Moments Later)"
    # [Scene: Tideward Promenade | Moments Later]

    scene bg ch5_4001e7_3 at full_bg
    # play music "music_placeholder"  # [Music: Staccato strings; drums like falling water]
    # play sound "sfx_placeholder"  # [Sound: A roar of water, a ripping undercurrent; distant alarms]
    "By the time you hit the promenade the world is all motion. A scouring current—beyond any expectation in the models—has found a seam in a secondary levee near the Subbasement Data Lab. The sea isn't polite; it chews and teaches."
    show elias_chen at left:
        zoom 0.7

    elias_chen "Form the line! Pass the bags! Mina, get people away from the kitchen!"
    "Elias Chen is at the front of it, mud on his jeans, camera bouncing against his chest but hardly noticed. His face is a sunburn of determination; he looks like someone who learned to hold against tides by hand."
    show mina_kuroda at right:
        zoom 0.7

    mina_kuroda "The prep tanks are full—if the scald goes it floods the burners. Someone—someone get the valves!"
    "You can see the kitchen's door swinging, steam and the smell of stew muffling the salt for half a second before the next roar of water reasserts itself."
    show rafi_alvarez at center:
        zoom 0.7

    rafi_alvarez "Rowan's issuing a rolling lockdown. Atrium protocols—priority: servers, sensors—"
    "The comm crackles; the word 'lockdown' drops like a stone and sends ripples. Someone spits a curse into the rain."
    hide elias_chen
    show sora_watanabe at left:
        zoom 0.7

    sora_watanabe "People first. Always people first."
    "Your chest splits between the science you keep in your head—the models, the contingencies—and the rhythm of hands passing sandbags. The ledger you've kept of promises doesn't have a stamping for this kind of betrayal: nature outruns even the best-laid page."
    hide mina_kuroda
    hide rafi_alvarez
    hide sora_watanabe

    scene bg ch5_4001e7_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Server alarm tone bleating, distant and menacing]

    menu:
        "Help Elias with the sandbag line":
            "You drop the notebook, shoulder into the chain of hands. Weight passes through you—sodden burlap, neighbor to neighbor—while somewhere, under the promenade, a server crowd begins to climb toward critical temperature."
        "Run for the Subbasement, try to stabilize the servers":
            "You wrench away from the line, cutting through mud to the lab's service entrance. The staircase smells of ozone and salt. Down there the fans are fighting and failing. You understand the spreadsheets; you can feel the models like a pressure in your ribs."

    # --- merge ---
    "Continue to next scene (Subbasement Data Lab | Immediately After)"
    # [Scene: Subbasement Data Lab | Immediately After]

    scene bg ch5_4001e7_5 at full_bg
    # play music "music_placeholder"  # [Music: High, metallic strings; heartbeat-like bass]
    # play sound "sfx_placeholder"  # [Sound: Fans laboring, alarms, water whispering into drains that aren't draining]
    "The lab greets you with the thin, electric odor of machines under duress. Cables cling to walls like wet ropes. Monitors flash teal tidal projections and—then—red cascade alerts."

    "Technician" "Red cascade in rack 3! We can try to throttle—reduce write cycles—"
    show dr_rowan_hale at left:
        zoom 0.7

    dr_rowan_hale "Initiate HelioCorp lockdown. Disconnect non-essential nodes. Route power through the backup bus."
    "His voice is the kind that smooths edges—commands given like scalpel cuts. He is two things at once: precise, and suddenly someone wholly dangerous because he speaks with a certainty that leaves no room for argument."
    "You hear the rail of volunteers outside—Elias Chen's voice threads through—and your own models flash across your mind, a lattice of probability. They do not all agree. Some predict widespread cascade if the backups are tripped incorrectly; others show that isolating nodes now will prevent lateral damage."
    "Aiko Mori: (out loud, to Rowan) 'If you lock the lab down from the atrium, you cut off local manual override. If the backup bus fails, we lose sensors that are guiding pumps out on the promenade.'"

    dr_rowan_hale "We have to prioritize systemic stability. I can't risk a chain failure that takes out the city's adaptive interface."
    "A pause like a held breath. You sense the math in his words; you feel the calculus of other people's lives braided into it. His hand lifts, fingers flexing around an invisible compass he reaches for but doesn't expose."
    show elias_chen at right:
        zoom 0.7

    elias_chen "Systemic stability won't stop the water at Mina's door this minute, Rowan! People are on the line!"

    dr_rowan_hale "And if the cascade takes down pumps citywide, there will be no 'people on the line' left to tell stories."
    "Your throat closes. Both cases are mercilessly true. You taste salt and something like metal on your tongue, and the lab's humidity beads on the inside of your jacket."
    show sora_watanabe at center:
        zoom 0.7

    sora_watanabe "What does your gut say, child? And what does your head say? Both are honest."
    "You think of promises you made in ink and in voice. You think of the ledger, of Mina ladling stew to volunteers, of Elias Chen's hand at your back at the Beacon. You think—unavoidable—of your long"
    "distrust of institutions and of the way Dr. Rowan Hale's gaze had, earlier, held a small thread of something like admiration or calculation or both."

    dr_rowan_hale "You trained in models, Aiko. Help me choose the right isolation routine. Then authorize the lockdown."
    "The room tightens. Fingers hover over switches. Someone mutters about legal authority; someone else, a volunteer, weeps under an oilskin hood. The lab's temperature climbs in a way that feels like an accusation."
    hide dr_rowan_hale
    hide elias_chen
    hide sora_watanabe

    scene bg ch5_4001e7_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The server alarm now wails as if mourning]
    show rafi_alvarez at left:
        zoom 0.7

    rafi_alvarez "There's a feed going public—people are watching this unfold. If you open access, we can coordinate pumps manually. If you lock it down, you control the message."
    show elias_chen at right:
        zoom 0.7

    elias_chen "You know the models. If there's a chance the lockdown saves the grid, authorize it. I won't pretend it's easy. But I will not watch our people drown because someone farther up thinks they can reroute fate more neatly."
    show dr_rowan_hale at center:
        zoom 0.7

    dr_rowan_hale "We can evacuate—temporarily reassign human resources while we secure the infrastructure. It's the responsible approach—"
    "Aiko Mori [internal]: You can hear the syllables of responsibility as if they were promised in coin. The ledger wants ink; the neighborhood wants hands."
    "Your models are a chorus with different songs. One set says: isolate, secure the servers, prevent a cascade that would make recovery impossible. Another set—localized, built from on-the-ground soil moisture readings and human timescales—says: hold the levee now, reroute pumps manually; servers can be rebuilt, people cannot."
    "The storm is a throat around the city now. The atrium's cool cyan light is dimming in a way that feels personal; across the comm, Dr. Rowan Hale's voice is steady, unyielding."

    dr_rowan_hale "Authorize the lockdown. You will regret inaction if this becomes systemic."

    elias_chen "And you'll regret action that betrays the people here, Aiko."
    "The tension is not merely strategic; it is a betrayal braided from conviction. You see, in flashes, the ledger's pages splotched with water, with your own fingerprints."
    "Your chest hammers. You smell steam and wet concrete and the iron note of adrenaline. Your hands find the notebook, fingers wet, the ink running like a small ruin."
    "Aiko Mori [internal]: You are slow to give away control. You are slower still to give away the neighborhood. Which of these truths weighs more when the water is at Mina's threshold and the servers are screaming?"
    "The room compresses into a single, urgent calculus."
    hide rafi_alvarez
    hide elias_chen
    hide dr_rowan_hale

    scene bg ch5_4001e7_7 at full_bg
    # play music "music_placeholder"  # [Music: Climactic, dissonant brass and percussion]
    # play sound "sfx_placeholder"  # [Sound: All alarms converge into one, deafening chord]
    "You step back, the choice raw and electric under your skin. Everything you believe about community, about science, about trust, pulses in opposition."

    jump chapter6
    return
