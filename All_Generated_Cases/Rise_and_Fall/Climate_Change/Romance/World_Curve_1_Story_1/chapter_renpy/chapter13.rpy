label chapter13:

    # [Scene: Harborside Promenade | Morning]

    scene bg ch13_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant reporter chatter, the low thrum of a generator, gulls arguing over a crust of bread]
    # play music "music_placeholder"  # [Music: Warm strings begin, steady and rising]
    "You stand with your hand on the railing, the braided leather cuff warm against your wrist where Rosa once mended it. The holdout you called—refusing the compressed timeline—has become a living thing overnight: headlines, hot and"
    "judgmental, call you an obstruction; donors' spokespeople phone with clipped patience; a council member asks, politely, whether you understand the stakes."
    "And yet the harbor smells the same—wet wood, diesel, kelp—and the city does what it always does when people gather: it begins to talk."
    "You fold and refold the printed list in your hands. The ink still smells like the lab and the promenade, the two worlds crammed together in a palm. You can feel the pressure from above—speed, metrics,"
    "an emergency timetable—but beneath it another current runs: stories, memory, the staccato clatter of pots and pans at a community kitchen, the clay-sweet breath of seedlings in Eli's roofs."
    "You let the list rest on the railing. The holdout was not an act of stubborn refusal so much as a call for time: time to translate urgency into something people could see themselves inside of. The cost is loud. The reward is possible."

    scene bg ch13_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A single bicycle bell stutters past, then the echo of a distant harmonica—Eli practicing, somewhere up a stairwell]

    menu:
        "Let the journalists have the quote now":
            "You pull out your phone, give a short, measured line about stewardship and patience. Cameras nod; an editor files. It feels like policing your own language."
        "Refuse the quick quote; direct them to the town hall":
            "You fold your hands and point toward the schedule tacked to the boardwalk. 'Go where people are talking,' you say. They frown—no immediate soundbite—but a producer scribbles and follows the crowd instead."

    # --- merge ---
    "The story continues into the town hall."
    # [Scene: Town Hall — Community Center Gym | Afternoon]

    scene bg ch13_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A chorus of voices—elderly residents with slow cadences, students with clipped, excited tones, a child asking whether the seawall will be tall enough to keep her kite.]
    # play music "music_placeholder"  # [Music: Rhythmic hand-drums layer under the strings, steadying tempo]
    "The first town hall is crowded to the doors. The air smells of coffee and wet coats; someone has brought lemon bars in a Tupperware, and the scent threads through the room like an easy permission to speak."
    "An elder from the dockside stands, palm knuckled like worn rope. She begins not with statistics but with tide lines—where her father's boat used to sit at low water, how a certain gull always nested under"
    "a particular rail, how the moon used to come close enough to read by. The microphone catches the rasp of her voice; it catches the room."
    "Students present a map next: hand-drawn living-shore prototypes, swales of native grasses, modular wetland cells that could sit in the shadow of a scaled-back wall. Their diagrams are neat but tentative—explanatory arrows, ink smudges. A boy"
    "in the front row points out where runoff currently funnels into the street and how a micro-wetland could take that water."
    "You watch people stitch these two things together—lore and prototype—like two hems of a garment. Your chest tightens not with fear but with an expanding, practical hope."
    "Sienna is there, sitting near the back with her notebook closed. She listens in silence, fingers tapping once against the titanium pen. Her face is the same practiced neutrality you remember from the lab, but when"
    "the elder names a memory about the harbor 'you kept,' something in her hands stills. The expression on her face is complex—lines that might hold concession or calculation, or both."
    show maya_calder at left:
        zoom 0.7

    maya_calder "We need the seawall where it saves lives. We need wetlands where they feed us and slow the water. We need a board that can answer to both. We need time to do this together."
    show dr_sienna_kade at right:
        zoom 0.7

    dr_sienna_kade "I understand the urgency you're naming. I also understand the technical limits. But—' (she breathes) '—we don't have until the next storm. We need a pathway that reduces risk quickly."
    "You hear the hurry in her sentence; you know the algorithms in the lab that map risk to dollars. You also hear the elders' slow knowledge that time can make certain things possible, if people are given voice."

    maya_calder "Then let's make a pathway that reduces risk and keeps voice. A phased build—prioritize critical stretches, pair them with wetlands pilots, and create a binding governance board that includes residents with veto on relocation orders."
    "Sienna raises her hand, hesitates, then speaks."

    dr_sienna_kade "If we can show measurable reduction in risk—tide height, surge velocity—donors will release phased funds. If a governance board can commit to real oversight and accountability, I will agree to a mediated co-design."
    "You hold your breath. Her concession is not total; it's a lever. It is enough to pull the meeting toward a strange, cooperative place."

    dr_sienna_kade "But it's contingent on pilot metrics. We will need to define them now. And we will need to agree on who sits on the board and how the veto works—clear thresholds, clear legal terms."

    maya_calder "We define them together. We can set both safety metrics and social metrics—employment guarantees, displacement protections, an independent auditor from the neighborhood."

    dr_sienna_kade "Then bring me those definitions. Start tonight."
    "The room exhales. Electric with tired joy, full of the clank of folding chairs and low conversation, the town hall spills out into heated clusters. People are already debating planting schedules; a student asks whether native sedges could be taught to the community crew."

    menu:
        "Take the elder's tide-line and pin it to the lab proposal":
            "You carefully translate the tide-line into a margin note and promise to inscribe it into the proposal; the elder looks surprised and pleased."
        "Insist the lab's sensors take precedence for metrics":
            "You suggest sensor-based thresholds; some nod, but a few eyes narrow—'What about stories?' someone asks. You realize metrics must be human-measured too."

    # --- merge ---
    "The mediated negotiations continue, leading to a compromise."
    # [Scene: Harborside Promenade — Negotiation Day | Late Afternoon]
    hide maya_calder
    hide dr_sienna_kade

    scene bg ch13_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rain that had threatened all day taps a steady tempo on the promenade roof; voices are low and intent]
    # play music "music_placeholder"  # [Music: String motif swells with a hopeful chord progression]
    "The mediated sessions that follow are messy in the best way: erasures, additions, and a slow accretion of trust. Donors bristle at the delay, yes; a railing of emails calls the holdout political and naive. But"
    "the town halls—more and more of them—have changed the conversation from 'fast protection' to 'durable justice and protection.'"
    "You and Sienna map a compromise like two people tracing the same coastline from different maps. You argue for employment guarantees; she argues for clear, measurable pilot outcomes. You push for a civilian veto shaped as"
    "an emergency pause—hard to trigger, legally bounded; she pushes to define the technical thresholds that must be met to lift a pause."
    "Dialogue between you becomes a rhythm of proposal, counter-proposal, and the small mercies of listening."
    show dr_sienna_kade at left:
        zoom 0.7

    dr_sienna_kade "If we agree on three critical stretches prioritized for hard protection and pair each with a living-shore pilot covering adjacent sectors, we can amortize risk without wholesale relocation."
    show maya_calder at right:
        zoom 0.7

    maya_calder "And those pilots will be community-run, with apprenticeship slots reserved for local workers and a dedicated fund for displaced vendors to set up elsewhere."

    dr_sienna_kade "I don't want to be the one who slows safety. If this board can be designed to act quickly and if the pilots have clear metrics, the authority will back this phased approach."
    "You feel, in the way the sentence lands, the architecture of a new contract: less a fortress wall and more of an armature you build with others."
    hide dr_sienna_kade
    hide maya_calder

    scene bg ch13_601bcb_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The click of a pen as both of you sign the first memorandum of intent—an old, ceremonial gesture that makes everyone laugh, the sound light and relieved]
    # [Scene: Harborside Promenade — Small Ceremony | Dusk]

    scene bg ch13_601bcb_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Eli's harmonica slips in behind the guitar like salt following bread; the city murmurs as if listening]
    # play music "music_placeholder"  # [Music: A gentle, celebratory folk motif; harmonica and guitar entwined]
    "Rosa takes your hand first. Her grip is rough and warm, the skin like rope washed soft. She looks out at the harbor as if reading a familiar script and then at you, and something like pride and relief moves across her face."
    show rosa_calder at left:
        zoom 0.7

    rosa_calder "You did what I told you when you were small. You kept the root."
    show maya_calder at right:
        zoom 0.7

    maya_calder "You taught me how to tie things down so they can grow."
    "Elias 'Eli' Maren begins the song. His voice is weathered and honest, folding your neighborhood's names into the chorus—names of alleys, names of boats, the sound of gulls as a refrain. The crowd sways, and you"
    "think of every person who had to come to a table and tell a story for their place to be heard."
    "Dr. Sienna Kade stands a little apart, hands folded, watching the crowd. The expression on her face holds something complex—acknowledgment, perhaps, or the quiet fatigue of someone who has traded certainty for a new, slower kind"
    "of duty. You do not know the shape of her future choices. You only know this: she stayed to listen when listening cost her something."
    "Donors call the new accord messy. It is. The seawall will be smaller than first proposed; the wetlands will take seasons to prove their worth; the governance board will be awkward and filled with compromise language"
    "that lawyers put in to keep it stable. But the donors also promise conditional funding for the pilots, and a few of them—surprised by the legitimacy the process has built—say so publicly."
    "You stand on the promenade with Rosa and Eli, hair damp with salt, and taste the rise like a quiet tide: not a single triumphant shout but a slow, patient filling in of a shoreline that can be lived on."
    "Elias 'Eli' Maren finishes the last verse and then, after a beat, sings new lines he says came to him the night you refused the fast answer—lines about a city that refuses to be only engineered, about people who become the scaffolding for each other."

    rosa_calder "We didn't build this alone, but we will keep it. We will teach the children the nets and the new canals. We'll teach them both."

    maya_calder "We'll teach them to hold the map and the story both at once."

    menu:
        "Tie Rosa's scrap of blue thread to the railing now":
            "You loop the scrap and knot it tight. It flutters with the wind like a small promise. Rosa smiles in a way that stretches the years back into a single curve."
        "Wait, let Eli sing the last chord before we make anything official":
            "You take a breath and let the song mark the moment. When the chord dies, you feel the decision already settling like a seed in good soil."

    # --- merge ---
    "The ceremony continues; people organize and plan the pilots and apprenticeships."
    hide rosa_calder
    hide maya_calder

    scene bg ch13_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: The strings and harmonica linger, then soften into a calm, sustaining tone]
    "You taste the rise not as a triumphant crescendo but as durable scaffolding—the slow work of people choosing to stay and shape their own safety. The governance board will be awkward, the seawall will be measured"
    "and imperfect, and some things will still be lost; but the plan carries legitimacy and social capital—an infrastructure of trust as much as of concrete and cordgrass."
    "You think of the thousand small kindnesses that got you here: Rosa's seam-line mended in a jacket; a student handing you a sketch; Sienna allowing herself to be changed in public. You imagine the board meetings"
    "that will follow, the nights of planting, the lunches where new apprentices trade jokes and sea-weather wisdom. None of it is finished. All of it is in motion."

    scene bg ch13_601bcb_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low, sustained harmonica note, then silence]
    # play music "music_placeholder"  # [Music: Warm strings resolve on an open, hopeful chord]

    scene bg ch13_601bcb_9 at full_bg
    "THE END"
    # [GAME END]
    return
