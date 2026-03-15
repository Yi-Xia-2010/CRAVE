label chapter15:

    # [Scene: Council Chambers | Morning]

    scene bg ch14_3be532_1 at full_bg
    # play music "music_placeholder"  # [Music: Distant, low strings; a restrained, mournful piano motif]
    # play sound "sfx_placeholder"  # [Sound: Rain on the windows; soft murmurs of an assembled public]

    "You arrive early enough to feel the room settle around its own breath. The holographic map throws pale blue onto wet faces—shorelines traced in luminous lines, zones marked with discreet icons" "Pilot,' 'Funded,' 'Oversight: Mediated."
    show mara_ellis at left:
        zoom 0.7

    mara_ellis "I can read their math. I can read what it leaves out."
    show councilor_anika_patel at right:
        zoom 0.7

    councilor_anika_patel "We'll begin with the mediated proposal. The city recommends conditional approval with enforceable oversight. We thank NovaSeis, municipal engineering, and the community advisory panel for their work."
    "Elias Crowe steps forward with the practiced ease of a man who has learned how to occupy rooms. His silver hair catches the light, his words clean and packaged. He speaks about timelines and redundancy; about"
    "deliverables and guaranteed holdback funds. He gestures at the hologram where a long, continuous line of engineered structures appears along the nearshore, punctuated by small green nodes the panel insists are ecological offsets."
    show elias_crowe at center:
        zoom 0.7

    elias_crowe "This settlement preserves urgent funding and accelerates implementation. It balances scale with accountability—if the independent monitors find deviations, funds revert. We build with oversight, and we build fast."
    "Your notebook is open to the page where you once drew a berm by hand. Your hand hovers over it, then pulls back. The room is full of people whose lives the maps will change. Jonah"
    "stands beside you, shoulders hunched in the way he does when carrying the weather with him. His face is a map you try to read and hold to as if it might tell you the right"
    "route."
    hide mara_ellis
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "They tightened the oversight language. Not perfect—far from it—but it's something that wasn't here last week."

    "You want to say" "Something is not enough."
    hide councilor_anika_patel
    hide elias_crowe
    hide jonah_reyes

    scene bg ch14_3be532_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A single civic chime]
    "The mediator outlines the compromise—mediated standards that allow NovaSeis to continue major works, coupled with a municipal oversight board, independent audits, and immediate emergency support channels to the most at-risk neighborhoods. The language is intentionally porous; phrases like 'subject to review' and 'adaptive management' float like buoys of ambiguity."

    "Contractor representative" "Adaptive management lets us iterate quickly. We can't stall construction when storms are imminent."
    "Professor Asha Rao sits a few seats down, hands steepled, eyes like small lamps fixed on you. She doesn't tell you what to do, but the steadiness of her gaze is an appeal in itself: remember the data, remember the people it represents."

    menu:
        "Wait and let Jonah speak first":
            "You nudge Jonah subtly; he clears his throat and steps toward the podium with a report tucked under his arm—his voice tight but public-hearted."
        "Take the floor immediately":
            "You stand before the microphones, breath shallow; the chamber tilts into silence as you arrange the words into something sharpened and careful."

    # --- merge ---
    "Return to main narrative"
    # [Scene: Promenade | Midday]

    scene bg ch14_3be532_3 at full_bg
    # play music "music_placeholder"  # [Music: A small, mournful accordion line threaded with the creek of wooden planks]
    # play sound "sfx_placeholder"  # [Sound: Gulls, distant construction thrum, soft slap of water against pilings]
    "You walk the Promenade afterward to untie the knot gathered in your chest. Contractors' vans cut across the skyline like pale beetles. Workers with high-viz vests meet in clusters, holding tablets with sections of the coastline"
    "already grid-marked for installation. The smell here is simpler: brine, wet wood, a faint diesel tang—practical scents for practical work."
    "Old Mate finds a bench that is just high enough to stay dry. He taps the wood with a single knuckle as if measuring years."
    show mateo_old_mate_alvarez at left:
        zoom 0.7

    mateo_old_mate_alvarez "You were always quick to rough it out. The sea will outlast our best work, girl. We have to make sure the people outlast it too."
    show mara_ellis at right:
        zoom 0.7

    mara_ellis "And you think this settlement does that?"

    mateo_old_mate_alvarez "It buys time for some. It sells time for others, maybe. Time's a tricky currency."
    "Jonah sits down beside you and Old Mate, and for a moment the three of you are a small island of conversation. Jonah fingers the woven ring on his thumb, a nervous habit. He looks at you in a way that is intensely simple and therefore unbearably complicated."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "If the oversight actually functions—real auditors, real teeth in the audits—then the worst outcomes can be limited. It won't be perfect, Mara. But it will be fewer homes lost tonight than without action."

    mara_ellis "Fewer now isn't the same as not losing them later."
    "The line between pragmatism and idealism is thin and wet with salt. The conversation circles, then lands on the same rocky shoal: how many compromises can you stitch together before the fabric—this coastline, these communities—starts to fray in ways you can't fix?"

    menu:
        "Press Jonah on oversight specifics":
            "You push for details—who sits on the oversight board, who funds the auditors, what the penalties actually look like. Jonah answers with numbers, then with a weary half-smile: 'It's negotiable, Mara. It has to be.' "
        "Listen, and let Old Mate speak":
            "You turn to Old Mate. He tells a short story about a tide that kept coming, and about neighbors who learned to lift their thresholds higher in time. The lesson is not neat, but it lands heavier than statistics."

    # --- merge ---
    "Return to main narrative"
    # [Scene: Council Chambers | Early Evening]
    hide mateo_old_mate_alvarez
    hide mara_ellis
    hide jonah_reyes

    scene bg ch14_3be532_4 at full_bg
    # play music "music_placeholder"  # [Music: Low cello, a heartbeat pattern; rain intensifies against the windows]
    # play sound "sfx_placeholder"  # [Sound: The hum of air filtration systems, the rustle of paper, a distant siren tamed by distance]
    "The mediated settlement is now a document of dozens of pages. Language iterates between technical detail and weasel-proof clauses. Anika reads aloud the conditions: immediate emergency disbursements to neighborhoods listed in Annex A; NovaSeis's ability to"
    "implement Phase One contingent on monthly independent audits; a municipal right to halt works pending environmental triggers."
    "Elias smiles in the way of a man offering a handshake across a gulf. He looks at you once. The look is not simple—it is appraising, crafted, and perhaps carrying a shadow of something like regret"
    "you cannot be certain of. His expression is unreadable enough that it could be grand strategy or private penance. You name it 'complex' in your head and meanwhile let your bones mind the warning in your"
    "chest."
    "You rise to speak. The chamber presses its attention toward you, as if the room itself leans in to hear how you will translate your internal tally into public terms. The ledger in your head is"
    "full: saved homes you have seen, neighborhoods promised help, the already-noted physical changes that engineered structures bring—changed tidal exchange, sealed shorelines, lost marsh edges. You can feel the moral weight of bending toward the pragmatic: funds"
    "that will rebuild roofs, but also walls that will constrict the sea in ways that alter nourishment and time."

    "Contractor representative" "We have agreed to adaptive measures. We will install living breakwaters where feasible and monitor sediment flows."
    show mara_ellis at left:
        zoom 0.7

    mara_ellis "What does 'where feasible' mean? Who decides feasibility when the money's invested?"
    "There it is—your question. The room is a held breath. Jonah looks at you without saying anything; his face reads like a map with smudged ink. Professor Asha's fingers tighten on her pen."
    show elias_crowe at right:
        zoom 0.7

    elias_crowe "Feasibility must balance ecological benefit and structural integrity. We will work with the oversight board to define parameters. We believe this model can be a template."
    "His 'we believe' is not the same as a promise. You can hear the city outside: the muffled sound of pumps, the steady work of human hands rearranging what the sea has already rearranged."

    menu:
        "Name the worst-case scenarios aloud":
            "You sketch, briefly and bluntly, the possibilities: accelerated erosion down-current, marshland compression, displacement as insurers rate areas unlivable. The chamber goes quiet in a different, heavier way."
        "Frame your testimony around immediate human needs":
            "You tell the council about the family who lost their door threshold, a child who learned to wade to school. Your words push the room toward action that feels urgent and personal."

    # --- merge ---
    "Return to main narrative"
    "You think of the Drowned District—brick facades mottled with algae, windows like tired eyes. You imagine the engineered lines of NovaSeis's proposed works rearranging water in ways that will only become apparent months and years from"
    "now. The consequences are slow-burning: less tidal exchange, quieter marsh respiration, and a steady economic pressure that nudges families toward relocation."
    show councilor_anika_patel at center:
        zoom 0.7

    councilor_anika_patel "We are voting to accept the mediated settlement's framework, subject to the oversight board's first report. This will unlock emergency funds and allow Phase One to proceed."
    "The clerk's keypad gleams. Contractors shift into practical stances of readiness. Outside, you imagine crews mobilizing, kits being loaded, sandbags being traded for more permanent materials. The immediate crisis eases—at least on the surface. Relief moves through the chamber like a thin current."
    "Jonah takes a breath and meets your eyes. His look is complex—pride and apology braided together. He reaches for your hand, briefly. You feel the warmth and the way it perks at edges you did not know you had left open."
    hide mara_ellis
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "If you stand with this, we can protect people this season. If you step back, the work stalls. I don't know which faith is truer."
    "You remember the nights on the ferry, maps spread like constellations, the small people who had stitched reward and risk together at the margins. You remember your mother's hands, the way a community mended what the"
    "state could not. You also remember the child who stooped to touch a tide pool with holy curiosity. You cannot easily choose between them."
    "The council waits for your public position now. The room narrows to the space between your name and the microphone. Outside the glass, rain throws itself against the city like insistence."
    "Your chest is full of facts and images that pull in different directions. You can hear the subtle shift in tide beneath every argument—the long arc of change that starts with what seems like safety now."
    "The mediated settlement promises immediate resources; the language promises constraints; the future beyond the wording feels uncertain and already borrowing from your conscience."
    "You lift your pen, touch the paper in front of the microphone, and for a heartbeat you listen to the rain. There is a thousand-voiced chorus in you: the data, the faces, Jonah's tempered hope, Old Mate's weathered caution, Professor Asha's quiet insistence."
    "You inhale."
    "You tilt your head toward the microphone and prepare to translate the ache of this hour into something the chamber understands: a vote, a recorded statement, a ledger entry that will ripple beyond the room and into the infrastructure of lives."
    "You do not yet speak."
    hide elias_crowe
    hide councilor_anika_patel
    hide jonah_reyes

    scene bg ch14_3be532_5 at full_bg
    "THE END"
    # [GAME END]
    return
