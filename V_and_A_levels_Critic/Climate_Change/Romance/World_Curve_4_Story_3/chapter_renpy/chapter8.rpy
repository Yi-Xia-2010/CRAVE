label chapter8:

    # [Scene: Boardwalk | Morning — overcast, gusting wind]

    scene bg ch8_6b08b4_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Metal creak, diesel engines, shouted directions over a bullhorn]
    # play music "music_placeholder"  # [Music: A taut, fast-tempo string ostinato — anxious and driving]
    "You step onto the boardwalk and the town is already mid-sentence. Cranes swing like slow metronomes, bright tarps snap in the wind, and the contractors' radios spit static and timetables. The air tastes of salt and"
    "exhaust. Rain has lifted the colors out of everything — wood grain turned charcoal, banners dulled to rumor. Somewhere, a drill bites into pilings; the sound is too close, too final."
    "You should feel the relief that's been floating around the crews — paychecks, schedules, the realignment of anxious eyes toward work — and part of you does. It is a small, combustible warmth: people who have"
    "roofs patched and mouths fed. The statistics are there in your head, the tables you brought into meetings, the grant line items that breathe life into payroll. Tangible. Tractable. Necessary."
    "But the other thing is there too. A ledger you carry in your chest: faces you have not negotiated away. Neighborhoods labeled for relocation. Stories folded into checkboxes. The two things do not sit comfortably in the same palm."

    scene bg ch8_6b08b4_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A gull squawks, then is swallowed by the clatter]
    "You move between groups — foremen, municipal inspectors, a woman from procurement tapping a tablet with sharp nails — and catch the way the town rearranges itself around this project. The sea seems quieter in the"
    "photographs posted on the site board: tide lines erased, shoals smoothed like half-remembered maps. Photos are always kinder than reality."

    "Foreman" "Maya—good to see you. Things are finally moving. We’ll have the east pilings in by nightfall if the tide holds."
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "Good. Make sure the cedars on Marsh Street are flagged and—"
    "You pause; every word feels like a negotiation with your own heart."

    maya_reyes "—and keep the community liaisons on the loop. If families need time off, document it. We'll cover loss of income during relocation phases."

    "Foreman" "Noted. We'll coordinate with Ana's office."

    maya_reyes "Thank you."
    "You mean it, but your voice remembers all the people this operation will touch."
    hide maya_reyes

    scene bg ch8_6b08b4_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Board creak, distant pile driving]

    menu:
        "Walk the perimeter with the foreman to inspect the pilings":
            "You follow the foreman's route, boots slapping wet boards as the crane shadow passes over you. You count piles, note measurements, and the reports feel real in your hands. For a moment the planner in you is calm—something is being built."
        "Pull aside a laborer and ask about local hires":
            "You crouch to talk to a young laborer easing a coil of cable. He tells you his sister got the night shift and that they rented a room across the inlet. His gratitude is immediate, blunt; it warms you but also shoves the ledger of losses into sharper relief."

    # --- merge ---
    "The scene proceeds as you continue through the site and toward the map tent."
    # [Scene: Construction Site Map Tent | Midday — drizzle]

    scene bg ch8_6b08b4_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low conversation, the scratch of maps, the distant thump of pile driving]
    # play music "music_placeholder"  # [Music: A single low piano note repeats, uneasy]
    "Inside the map tent, cardboard tables are covered in glossy prints. Someone has taped a photograph of Iris to the map near the low-lying runs — a sun-weathered smile pinned above a block shaded 'RELOCATION ZONE.'"
    "You look twice, as if your eyes can decide what the ink cannot: who gets preserved and who is noted as expendable."
    "Iris stands a few feet away, hands jammed into neon gloves. Her face is a ledger of experience; the laugh lines are edges of endurance. She looks at the map, then at you, and the expression"
    "that passes over her face is complex — not a simple hurt or anger but a worn calculation that reads as both accusation and survival. You do not know what choices led her here precisely, but"
    "you know the stakes are hers in a way that the site plans never fully account for."
    show iris_tanaka at left:
        zoom 0.7

    iris_tanaka "They put my street in the maroon band. 'Relocation zone.' Like it's a tidy phrase."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Iris—"
    "You pause; every word feels like a negotiation with your own heart."

    maya_reyes "We put protections on the plan. Relocation funds, temporary housing aid—"

    iris_tanaka "Protections on paper won't hold a roof over Mrs. Chen's head if the buyouts take months to clear. They won't teach my boy how to fish when the dock he's always known is gone."
    "She looks at you hard."

    iris_tanaka "We were supposed to build resilience together, Maya. Not move people off the map."

    maya_reyes "I know. I know that's the risk. I—"
    "You reach for the data, the escape route of numbers."

    maya_reyes "The modeling shows the wall reduces storm surge risk for the town's commercial center by thirty-four percent. We can keep businesses operational. We can slow immediate loss."

    iris_tanaka "Numbers don't fetch nets."
    "She steps closer."

    iris_tanaka "Are you telling me the town is safer while my street is erased?"

    maya_reyes "No. I'm saying the town is safer at large, but you're right—safety will be uneven. That's on me."
    "You feel your throat tighten. This is the part that loops in your head at night."

    menu:
        "Offer to meet with Iris and the affected households tonight":
            "You meet her gaze and promise to come. Iris snorts but agrees; there is relief in being seen. She names three people you must speak with. The list feels like an obligation and a lifeline."
        "Ask Iris for specific legal points she's worried about":
            "You ask carefully, slipping into planner mode. Iris lists eviction timelines and documentation burdens. You write them down; the practicalities grow heavier as the list lengthens."

    # --- merge ---
    "The conversation leaves you with named contacts and a clearer sense of immediate community needs."
    # [Scene: Old Pier | Night — rain, neon buzzing faintly]
    hide iris_tanaka
    hide maya_reyes

    scene bg ch8_6b08b4_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain on wood, low chanting, Elias's whistle under his teeth]
    # play music "music_placeholder"  # [Music: Percussive, quickened — heartbeat tempo]
    "You find the vigil under the old neon, where the sign blinks in broken rhythm and the tide gnaws the pilings like a slow, persistent mouth. Elias Hart is there, wrapped in his patched denim, whispering"
    "into an amplified mic about community worth. Faces lean in; candles smear light over wet cheeks. He sees you before you can cross the creaking boards."
    show elias_hart at left:
        zoom 0.7

    elias_hart "You showed. Thank you."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "Of course. I wanted to hear—"

    elias_hart "Hear? Or to be seen while the machine moves? Maya, these people are your people. You were in the meetings. You signed the recommendations."

    maya_reyes "I didn't sign anything without trying to wedge protections in. I tried—"

    elias_hart "Tried? Maya, 'try' didn't keep Ana's office from green-lighting the relocation map that puts Iris out of a home. 'Try' didn't stop the developer from writing the deadlines into the contracts."

    maya_reyes "Elias, you know how politics works. Compromise keeps the lights on. It's not ideal, but—"

    elias_hart "Is it worth it? How many of their streets 'kept the lights on' in your calculation? How many of our elders have to move into modular units so other people can get a new boardwalk bar?"

    maya_reyes "It saved jobs."
    "Your voice fractures. You say it as if it should be enough."

    elias_hart "Saved jobs for whom, Maya? Your compromise feeds contractors and a tax base. It makes a nice headline. Those same headlines don't show the hands that dig through boxes in basements."

    maya_reyes "You make it sound like I chose to hurt people for performance. You weren't there in the oversight meetings. You don't see the hours I put in trying to secure relocation aid."

    elias_hart "Maybe not. Maybe I don't see the hours. But I see what people feel. I see how this feels like being sold out."

    maya_reyes "And I see what happens if we stall. People lose roofs tomorrow."

    elias_hart "And what about the people who lose history because of your 'roofs'? Which is worse? A roof that costs a life tomorrow, or a future without their stories?"
    "Maya Reyes [Silent]"
    "Rain taps the wooden slats; your braid, soaked, clings at your neck."

    maya_reyes "I don't know."

    elias_hart "Then don't pretend you have certainty, Maya. Don't make a deal as if it's neutral. Tell them—tell Iris—what you are willing to fight for."
    "Samir's camera clicks from the edge of the crowd. His lens finds you framed between the neon and Elias Hart's shadow. You know that image will travel: wet braid, clenched jaw, the town's fog wrapped like"
    "a shawl. Samir meets your eyes and doesn't gesture; the photograph will be the record."
    # play sound "sfx_placeholder"  # [Sound: Camera shutter, a high note that lingers]

    elias_hart "You're standing on a line. Pick a side, Maya. Not a political trick — a real side. People need to know which side you'll stand on when the dust settles."
    "Maya Reyes [Internal]: The words land like a physical shove. Your chest splits again — payroll vs. people, immediate relief vs. long-term justice. The town moves forward and leaves some steps behind."
    # [Scene: City Hall / Council Chamber | Morning — packed room, fluorescent glare]
    hide elias_hart
    hide maya_reyes

    scene bg ch8_6b08b4_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmurs, the click of a laser pointer, the stamp of a gavel somewhere down the line]
    # play music "music_placeholder"  # [Music: A low, persistent drum; urgency ratchets]
    show maren_voss at left:
        zoom 0.7

    maren_voss "Fiscal solvency is not a slogan — it's the oxygen of municipal services. Without jobs and investment, Harborwell risks attrition, reduced services, and economic collapse. The redevelopment plan with the sea wall stabilizes our tax base while providing immediate employment."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "We have that stability because of targeted investment. But the plan as written places disproportionate burden on certain neighborhoods. We can strengthen clauses. We can ensure binding relocation assistance."

    maren_voss "Binding assistance is expensive and often litigated. It can delay construction, inflate costs, and jeopardize the very investments we need. The council must weigh expediency against idealism."
    show mayor_ana_delgado at center:
        zoom 0.7

    mayor_ana_delgado "We cannot gamble the town's solvency. But we also can't permit harm. I ask both sides — be practical and humane. Can we thread that needle?"

    maren_voss "In the real world, the needle is long. It sews quickly. We deliver jobs and immediate protection. We offer mitigation where possible."

    maya_reyes "Maren, mitigation needs teeth. Without legally enforceable timelines and housing guarantees, 'offers' have a way of becoming promises deferred."

    maren_voss "And without movement, the project stalls. Jobs vanish. Businesses close. That's not an ultimatum; it's just arithmetic."
    "Maya Reyes [Internal]: The arithmetic feels like a guillotine. Numbers are blunt instruments and people are not. Yet the council chambers hum with a different kind of hunger — the municipal imperative to act. The public"
    "wants change that lands tangibly. Elected officials answer to timetables. You can hear the clock in the room, relentless."
    hide maren_voss
    hide maya_reyes
    hide mayor_ana_delgado

    scene bg ch8_6b08b4_7 at full_bg

    menu:
        "Push publicly for binding relocation protections now, during the session":
            "You stand and speak into the mic. Your voice trembles but the facts are ready. You lay out legal language for protections and name a timeline. The room shifts; you see supportive nods and sour faces. The motion creates immediate friction."
        "Ask for a closed-door negotiation with Maren and Ana to get protections written before the vote":
            "You request an off-the-record meeting. It feels like playing the old game—compromise at the table. Maren agrees, but the delay draws murmurs of suspicion from the crowd and Elias' organizers plan a protest."

    # --- merge ---
    "The council session ends for now and the decisions are set to move forward."
    # [Scene: Tidewatch Harbor | Dusk — wind slicing, the smell of wet earth]

    scene bg ch8_6b08b4_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Waves, the far-off rumble of machinery, your breath in the cold]
    # play music "music_placeholder"  # [Music: A rising string line — urgent, fraying]
    "You move through the town carrying the weight of the day's collisions. Sometimes the right course is a thin ridge between two cliffs; sometimes it is a cliff itself. Tonight the ridge feels impossible. Your phone"
    "buzzes with messages — the mayor's office, a text from Samir ('photo looks raw — good'), a note from a councilmember asking for your stance. Elias' earlier words replay like a second tide."
    "You remember the atlas of past compromises you keep in your head, each a folded crease in your decision-making. You remember the family home lost in a storm years ago and the stubbornness that turned that"
    "loss into your work. You are not indifferent to the calculus of saving a town; you are not naive to the social fractures that can widen under projects with good intentions."
    "Your braid is cold and wet against your neck. Rain beads on the brass of the compass locket you close around your fingers. The harbor exhales and the town waits."
    # play music "music_placeholder"  # [Music: Crescendo — strings and percussion converge; heartbeat-thudding tempo]

    scene bg ch8_6b08b4_9 at full_bg
    "The decision is not theoretical anymore. It will be announced. It will be recorded. It will determine who gets to stay and who must go. The room of your conscience thrums with urgency. You can hear"
    "Elias Hart’s vigil candles guttering and Maren Voss’s slides clicking into place at City Hall. Samir's camera has already framed you as a public actor."
    "Your chest is split. The town needs protection. The town needs justice. They are not the same thing tonight."
    # [Scene: Boardwalk | Night — rain steady, wind sharp]

    scene bg ch8_6b08b4_10 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain, the distant hum of generators, voices through radio]
    # play music "music_placeholder"  # [Music: A tight, relentless motif — tension at its peak]
    "You breathe in, again, because breath is all that keeps decision from cracking into panic. Then you look up at the silhouette of the new sea wall under construction — a hard line against the sea"
    "— and the faces that will be on the line of whatever follows. You know the paths laid out before you, and you know the costs each path will levy."

    menu:
        "Approve the relocation zones—prioritize immediate jobs and structural defenses.":
            jump chapter9
        "Secure binding relocation assistance and legal protections before proceeding.":
            jump chapter9
        "Resign from the advisory council and return to grassroots organizing with Elias.":
            jump chapter14
    return
