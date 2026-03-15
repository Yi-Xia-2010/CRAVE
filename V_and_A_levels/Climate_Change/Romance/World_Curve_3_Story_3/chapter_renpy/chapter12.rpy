label chapter12:

    # [Scene: Pressroom Plaza | Dawn]

    scene bg ch12_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A chorus of shutters, urgent murmurs, a distant foghorn]
    # play music "music_placeholder"  # [Music: Rapid, taut strings underscoring a pulse]
    "You press send twice—because ritual matters, because certainty never hurts—and the server accepts the packet like a held breath released. For a second the only sound is the tiny click of your watch; the pendant at your throat hums cool under your thumb. Then the city answers."
    "Headlines bloom across your phone like phosphorescence: leaked procurement memos, Consortium ties, the signet ring in a photo cropped too close to Noah Ortega's hand. Your inbox detonates. Calls you don't recognize pour in, and Diego's"
    "voice is already three beats ahead of you on the line, urgent and fierce. The press corrals around the plaza like birds around wind."
    "You step forward into the light. Cameras flash; someone asks your name as if you might be an emblem instead of a person. You can smell salt and wet asphalt and the bitter petro-scent of too"
    "many engines. The world compresses into the sound of your own breath and the roar beyond it."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "I made a choice that sleeps with consequences."

    "Reporter 1" "Ms. Reyes—did you expect this scale of reaction?"

    maya_reyes "I expected consequence. I didn't expect how quickly people would demand accounting."

    "Reporter 2" "Did you consider the harm to residents—panic, housing markets, displacement?"

    maya_reyes "When people are priced out of safety, that's already harm. Transparency isn't the cause; it's the remedy."
    "The questions pile like surf. You answer, because silence would be a vacuum someone else fills; you answer because not answering is a permission slip for worse things. Every word is a careful stitch: precise, public,"
    "readable. You think of the rooftop seedlings and Asha's patient, crooked smile and push your jaw into steadiness."

    menu:
        "Step onto a makeshift podium and call for immediate hearings":
            "You climb a crate, your voice steady. 'We will not let secrecy privatize our safety.' The crowd catches the phrase like a buoy."
        "Turn the crowd toward direct action—organize a community assembly":
            "You lower your voice and point to a nearby community center. 'We meet there in ninety minutes. Bring paper, bring questions.' The murmurs thicken into movement."

    # --- merge ---
    "Resume main narrative"

    "You watch the city mobilize like a living map. Messages from allies—Asha, Diego, Emil Kwon—arrive in a cluster: solid blue band across your screen. Emil Kwon's arrives with a single line" "I'm with the platforms. If you need hands, call."
    # [Scene: Televised Hearings | Midday]
    hide maya_reyes

    scene bg ch12_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Microphones rustle; the chamber's HVAC hum is a low motor beneath human voices]
    # play music "music_placeholder"  # [Music: Percussive, urgent—snare rolls and high strings]
    "You sit beneath the studio lights; they feel like noon suns. The room is full of people who make decisions for a living and those who live with the consequences. Mayor Lila Chen sits between them"
    "and the lenses, composed but visibly constricted—your memory of her plant brooch is a small, human detail amid polished policy faces."
    show noah_ortega at left:
        zoom 0.7

    noah_ortega "Ms. Reyes, you bypassed chain of custody. You released documents without authorization. That endangers our work—"
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "—and it exposes work that endangered our neighbors. Intent and transparency are not the same thing here, Noah."
    "Noah Ortega's jaw tightens. He leans toward his counsel; his hand brushes his signet ring and for the first time since you've known him, the public mask slides. There's a micro-expression—flashed skin, hurt pride—before it hardens again."

    noah_ortega "You knew the risks of community panic. You could have come to me, to the Consortium, and—"

    maya_reyes "—I did come to you. I came with the data, with neighborhood maps, with proposed amendments. The memos show the decisions made in rooms that were not the council's."
    show mayor_lila_chen at center:
        zoom 0.7

    mayor_lila_chen "Ms. Reyes, the city needs solutions and we need trust. How do you propose we rebuild both?"
    "You put your palm flat on the table, feeling the grain of the wood and the tremor in your fingers—your body is a ledger of fear and resolve."

    maya_reyes "We open procurement. We create enforceable transparency. We reallocate a portion of the seawall budget to participatory resilience pilots—living shorelines, community-led retrofits—and we bind it with legal protections against displacement. We set up citizen committees with real budgetary teeth."
    "The chamber reacts—murmurs, a flurry of note-taking. Cameras tilt to Noah Ortega. Somewhere, legal teams scrawl acronyms. The pace is a rapid current; you ride and steer at once."

    noah_ortega "You're asking us to cede control to people who don't understand engineering responsibility—"

    maya_reyes "People understand their lives. Engineering without context is arrogance. We can marry rigor with lived knowledge. It's not ceding control; it's widening it."
    "Noah Ortega's posture fractures then—a thin line of impatience and something resembling fear. A photo circulates on the feed: Noah Ortega's hand on the Consortium ledger; the signet ring cropped into a focal point. The anchors whisper about conflicts of interest. Questions in the chamber sharpen to axes."

    mayor_lila_chen "Given the new information, I am convening an independent inquiry. We will review procurement practices, and I will propose emergency legislation to increase procurement transparency and reallocate funds toward community-led resilience."
    "The room reacts like a snapped wire—shock, relief, applause suppressed into the microphones. You feel the climax as a physical thing: an intake of air that fills the city."
    # play sound "sfx_placeholder"  # [Sound: Reporters' phones ping; the chamber's echo feels like an aftershock]
    # play music "music_placeholder"  # [Music: Swelling brass, then a high sustained chord that resolves into a lower, hopeful tone]
    "Noah Ortega sits, the public mask smudged. You meet his eyes for a beat—no words, only histories and the quiet acknowledgment of power shifting. The cameras capture everything; the city watches itself being remade on live feed."
    # [Scene: Council Hall Foyer / Night]
    hide noah_ortega
    hide maya_reyes
    hide mayor_lila_chen

    scene bg ch12_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low conversations, the rattle of chair legs, a distant rain on windows]
    # play music "music_placeholder"  # [Music: Rapid strings softening into a rhythmic heartbeat]
    "The inquiry's machinery begins: subpoenas, court filings, disclosures. There are legal jaws and moral clatter. Resignations tumble like loose tiles: a procurement director steps down; a consultant withdraws. The process is messy and loud; it is"
    "also real. Mayor Lila Chen pledges new policy language on live television with your name and Emil Kwon's in the same sentence as 'community partners.' You feel small and incandescent at once."
    "Diego calls crying—joyful, incredulous—and the neighborhood workshops swell. Volunteers show up with hammers and pails and maps; Emil Kwon and his crew are at the waterfront, patching platforms and teaching others to hold a line. You go down there between hearings."
    show emil_kwon at left:
        zoom 0.7

    emil_kwon "You did a thing that asked the city to be better. Then you handed everyone the rope. Now we pull."
    "You laugh despite the fatigue. He sets his tools down and wipes his hands on his pants, then reaches up and, with a tenderness you have learned to savor, adjusts your paracord bracelet the way you used to watch him tie knots on boats. Small movements contain vast truths."

    menu:
        "Let Emil fix the bracelet, accept the calm":
            "You close your eyes for a beat and let him. The world narrows to the press of leather against skin and the steadiness of his fingers."
        "Pull away, return to the next briefing":
            "You step back and shoulder the satchel of papers. 'I'll be right there.' The distance hurts, but the work presses immediate."

    # --- merge ---
    "Resume main narrative"
    "Emil Kwon's hands are steady as he fits a new clasp. Around you, neighbors pass by with steaming rice and tarps. There is a riot of small, human repairs: a child's shoelace re-tied, a poster pasted"
    "up, a plank hammered where the tide gnawed. The relief is not complete—it is threaded with exhaustion and legal tails—but it is palpable and real."
    # [Scene: Montage — City in Motion | Weeks → Months]
    hide emil_kwon

    scene bg ch12_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A media collage—snippets of testimony, radio hosts, community chants]
    # play music "music_placeholder"  # [Music: A layered crescendo—percussion driving forward, strings hopeful]
    "You ride a new schedule: hearings, committees, travel to panels, late-night interviews. Your life compresses into briefcases and back-to-back flights and an inbox that never quiets. The work is demanding and righteous. You are named in"
    "op-eds, invited to testify, and repeatedly asked to balance disclosure with protection for vulnerable residents. You sleep in odd hotel rooms, wake to unfamiliar skylines, and learn to make the pendant a talisman you touch between"
    "meetings."
    "Emil Kwon is there in between: a message with a crude sketch of a retrofit; a voice memo of a child's laugh at a community workshop; a photo of a repaired floating platform balancing a crate"
    "of seedlings. When you return home, your clothes still smell faintly of conference air and coffee; Emil Kwon folds you back into the small rituals of domesticity like a practiced sailor folding sails."
    show emil_kwon at left:
        zoom 0.7

    emil_kwon "You saved us from a model that would have erased us. We will make what comes next. You'll come back to us. We'll make room."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "What if 'room' is smaller than it used to be? What if we keep passing one another in doorways?"

    emil_kwon "Then we learn a different way to stand together. Companionate love isn't lesser—it's the kind that stores extra batteries and shows up at three a.m. to patch a leak."
    "You smile, and it is a tired, honest thing, but it is steady. The intimacy between you becomes a scaffolding rather than a spark: durable, practical, generous."
    # [Scene: Verdant Spire Rooftop Farm | Late Afternoon, Months Later]
    hide emil_kwon
    hide maya_reyes

    scene bg ch12_f99e88_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Bees, the quiet burble of irrigation, the distant city traffic like a folded sea]
    # play music "music_placeholder"  # [Music: Warm strings, a steady low drum—comfort in motion]
    "You stand at the rail and look down at the city transformed not into perfection but into a reconfigured, messier resilience: living shorelines bristling with cordgrass, community workshops with tool-sheds painted in neighbor-made colors, council sessions with citizens at the table. The tideline pendant warms under your fingers."
    show mayor_lila_chen at left:
        zoom 0.7

    mayor_lila_chen "This is the product of a painful, necessary reckoning. We will keep listening."
    "Noah Ortega's name becomes a complicated sentence in reports: investigations, hearings, a resignation that leaves open both accountability and unanswered legalwork. The system is bruised but adjusting. The change is incremental and bureaucratic and stubbornly human."
    "You and Emil Kwon walk the rows of seedlings, your sleeves flecked with soil. He reaches for a seed tray and brushes dirt from your knuckles with his thumb, a small ritual that says more than speeches ever could."
    "You think of the cost: late nights, missed dinners, the way your phone glows like a lighthouse of duty. You think of what you learned about power—how it consolidates, how it slips when sunlight hits the"
    "right hinges, how people with the fewest resources are also the most faithful carers of place."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "We rewired a system that wasn't listening."
    show emil_kwon at center:
        zoom 0.7

    emil_kwon "We still have miles to go. But look—people came."
    "You lean into him. The embrace is not a surrender; it is a redrawing of borders. The love that remains is companionate, fierce, and practical: he stitches your jacket while you draft amends; you book your"
    "next hearing and he packs a thermos and a schematic. The romance has matured into partnership, a shared plan sketched in marker on a dinner table."
    hide mayor_lila_chen
    hide maya_reyes
    hide emil_kwon

    scene bg ch12_f99e88_6 at full_bg
    # play music "music_placeholder"  # [Music: A final, swelling motif—hope threaded with gravity]
    "You feel the city breathing—a long, ragged inhalation that smells of salt and cilantro and the wet earth of freshly planted marshes. There is grief for what was lost, but there is also celebration for what was saved and what people are trying to build together."
    "You close your hand around the pendant. It is heavier with memory than metal. Emil Kwon squeezes your shoulder, simple and present."
    show emil_kwon at left:
        zoom 0.7

    emil_kwon "We'll keep showing up."
    "You nod. You accept that the role you chose will take you to distant hearings, that it will litigate and legislate and tire you. You accept that love will look different now—less lightning, more lamp light—and you trust its new geometry."
    hide emil_kwon

    scene bg ch12_f99e88_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Laughter from a volunteer circle; the distant, steady call of a foghorn]
    # play music "music_placeholder"  # [Music: Resolving harmony; a gentle, confident cadence]
    "You exhale—long, relieved, mournful, glad. The scandal detonated and, in the wake of its noise, things shifted. The procurement structures bend toward transparency; funds move; community voices are written into policy. The work is not finished;"
    "courts are slow, and culture change is a stubborn tide. But the city now contains mechanisms that let people argue in daylight and have a seat at the table."
    "You lift your face to the wind. It smells of wet soil and something like possibility."

    scene bg ch12_f99e88_8 at full_bg
    "THE END"
    # [GAME END]
    return
