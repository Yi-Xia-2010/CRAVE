label chapter4:

    # [Scene: Municipal Planning Office | Morning]

    scene bg ch4_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm strings with a steady, ascending rhythm]
    # play sound "sfx_placeholder"  # [Sound: Low hum of fluorescent lights, distant coffee machine, soft chatter of pages turning]
    "You arrive with Tomas already there, the strap of your messenger bag damp from morning drizzle. The municipal office smells of printer toner and strong coffee, overlaid with the faint, salty tang the city never quite"
    "loses. Your Moleskine is zipped in the bag, tide charts pressed flat beneath meeting notes. The choice you made last night—sitting with the city instead of shouting from the promenade—still sits like a usable tool in"
    "your hands."
    "Mayor Anton looks up when you step in. His spectacles catch the light and reflect a dozen little maps. He nods, the motion efficient and relieved. Rosa is already seated near the window, hands folded around"
    "a thermos that gives off warm citrus. Niko jokes under his breath about the mayor's tie being the exact color of bureaucratic compromise; Lena shoots him a look that could cut paper but doesn't."
    show mayor_anton_chi at left:
        zoom 0.7

    mayor_anton_chi "Good morning. We're on a tight timeline. If we commit today, legal can start drafting the permit language and the communications team can schedule the release. Tomas—Mara—how comfortable are you with this window?"
    "You feel the familiar tightening—a readiness to sprint and the carefulness that keeps things from breaking. Tomas gives you a look that is patient and full of the translational calm he's good at: the ability to say what needs to be clear without burning bridges."
    show tomas_herrera at right:
        zoom 0.7

    tomas_herrera "We can move fast. The pilot can be phased; initial works are low-impact and demonstrable. We draft an agreement that binds the municipality to community oversight for later phases."
    show mara_voss at center:
        zoom 0.7

    mara_voss "And we make sure 'community oversight' means accessible checkpoints, not a checkbox in legalese."
    "(You touch the edge of a printed covenant; ink flakes like dried tide-line.)"

    mayor_anton_chi "I don't do checkbox oversight. I do public hearings. But we can stipulate named seats and evaluation criteria. Legal just needs the green light."
    "Rosa Marin leans forward, voice warm but steady."
    hide mayor_anton_chi
    show rosa_marin at left:
        zoom 0.7

    rosa_marin "Names and criteria are roots. If you pull them up for money, the plant will die. Make the agreement say who waters and who decides."
    hide tomas_herrera
    show niko_alvarez at right:
        zoom 0.7

    niko_alvarez "And photos. I'm telling you, documented progress—kids holding plant markers—people show up for things that look alive."
    hide mara_voss
    show lena_park at center:
        zoom 0.7

    lena_park "Media loves a human moment. But we don't let the narrative get ahead of the reality. I'll run the pieces, but we need transparent reporting from the start."
    "The conversation loops; ideas pass between you all like warm plates. The room hums with that rare municipal electricity—the kind that comes when policy meets momentum. You find yourself speaking aloud, clarifying details that live in your head:"
    hide rosa_marin
    show mara_voss at left:
        zoom 0.7

    mara_voss "Permit list. Volunteers' safety plan. A schedule for the first six months that includes milestones the community can verify. And a living ledger that records changes to the plan."
    "Tomas Herrera nods, writing on his tablet, the motion precise."
    hide niko_alvarez
    show tomas_herrera at right:
        zoom 0.7

    tomas_herrera "We can have a public dashboard. Open data. Show funds, contractors, and an independent review cycle."
    hide lena_park
    show mayor_anton_chi at center:
        zoom 0.7

    mayor_anton_chi "Good. We'll route funding through a pilot line item to reduce procurement lag. Lena, if you can hold off on a splash piece until after the first sod is turned, that's a huge help."
    hide mara_voss
    show lena_park at left:
        zoom 0.7

    lena_park "I can hold a piece. But get me dates. People will want to see something tangible."
    "You feel something lift—not relief exactly, but the lightness of a plan being made sturdy. The meeting cracks open into smaller tasks: who signs what, who calls which stakeholder, whether the initial demonstration should be more ecological or more visual."

    menu:
        "Ask Niko to assemble a volunteer-run photo ledger for the first week":
            "Niko grins and slaps his knee. 'On it. I'll make it messy and honest.' He tucks a camera into his bag like a weapon of truth."
        "Ask Lena to coordinate a controlled press preview later in the month":
            "Lena nods, the journalist pivot clicking into place. 'I'll draft conditions. No staged plants, no early press-friendly shortcuts. We get real access.'"

    # --- merge ---
    "Continue"
    # [Scene: Municipal Planning Office — Small Conference Room | Midday]
    hide tomas_herrera
    hide mayor_anton_chi
    hide lena_park

    scene bg ch4_453e40_2 at full_bg
    # play music "music_placeholder"  # [Music: Steady xylophone taps with hopeful undertones]
    # play sound "sfx_placeholder"  # [Sound: Soft tapping of a tablet, the rustle of printed maps]
    "You and Tomas split tasks. Tomas negotiates with procurement by phone, speaking in the even cadence born of familiarity with budgets. You work the list of community partners—Rosa’s greenhouse group, the youth crew, local fishermen who"
    "understand the shoreline’s moods. You call a meeting with legal to make sure the words you're about to sign actually mean what you're saying out loud. Every small confirmation feels like stitching."

    "Legal" "We can incorporate community seats and evaluation triggers. The challenge is how binding you want those triggers to be. Because one emergency clause can undo a year's safeguards."
    show mara_voss at left:
        zoom 0.7

    mara_voss "Make the emergency clause specific—defined thresholds, not vague 'safety' language. If someone invokes emergency, it goes to an emergency council that includes community seats."

    "Legal" "That would hold up. It will slow the clause's drafting, but it gives communities teeth."
    "Tomas looks up from his notes, eyes flicking to you with a quiet question. You're aware, suddenly, of the dual life the pilot will have: one on paper, meticulous and cautious; another in the public eye, where images and timing shape what people believe is happening."
    show tomas_herrera at right:
        zoom 0.7

    tomas_herrera "We can play for long-term credibility, or we can play for immediate visible wins. Both have value."

    mara_voss "We can't trade away the part people won't see. Not at the start."

    tomas_herrera "I know. But if we show something quick—done well—we can lock in broader political support."
    "The tactical friction threads through your chest like a current. You think of Rosa's hands, the seedlings coagulated in the greenhouse light, the kids whose excitement is real even if only a photo will capture it."
    "You also think of the mayor's calendar, donor windows, and the way public attention flares and cools."

    menu:
        "Push to keep the demonstration low-impact and ecological":
            "Rosa breathes a little easier. 'That one will last,' she says. Her fingers find a sapling on the table like a promise."
        "Advise Tomas to draft a short, compelling demo for the press that still uses native species":
            "Tomas nods, relieved. 'We can calibrate visibility without compromise. A clean demo that shows process—no cladding.'"

    # --- merge ---
    "Continue"
    # [Scene: Harbor Promenade (the Flood Line) | Late Afternoon]
    hide mara_voss
    hide tomas_herrera

    scene bg ch4_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: Soft acoustic guitar with hopeful chord progressions]
    # play sound "sfx_placeholder"  # [Sound: Lapping water, gulls distant; the creak of a crane far away]
    "You step out to the promenade with Niko and a small crew to walk the first pilot strip. The air is humid and smells of brine and sun-warmed tar. Volunteers move with practiced gestures—tarps folded, shovels"
    "lined, sod rolled. A city photographer is there, but they keep their distance; this is still, for now, work."
    show niko_alvarez at left:
        zoom 0.7

    niko_alvarez "Look at the root lines here. If we plant the native grasses in staggered beds, they'll break surge but let fish move."
    "You kneel in the sand and press a palm into it. It yields and smells faintly of old seaweed and something green—growth."
    show mara_voss at right:
        zoom 0.7

    mara_voss "This is what we defend. Not a rendering; a hand in soil."
    "A small group of neighbors wave from a bench. A kid runs by with a cardboard sign scrawled in crayon: 'Save the Tide!'. The sight tugs something soft in you—proof that when people are asked to belong, they show."
    "Lena Park approaches with a recorder half-hidden in her palm, but her eyes are gentle; she has a way of asking without extracting. She wants the human line for the piece she will hold back until the pilot's deeper structure is clear."
    show lena_park at center:
        zoom 0.7

    lena_park "What's the line you want me to carry? Not a press soundbite—something that shows what the community is banking on."

    mara_voss "Tell them we are building for people who will be here long after campaigns are over. Tell them it's not a photo-op; it's a practice."

    lena_park "I can hold that. Make me a promise I can publish."
    "You smile despite the ache of responsibility. The small successes—permits routed, volunteers lined up, a mayor who has opened a budget line—feel like a swell under your feet. They are not the shore reclaimed yet, but they are shorelines drawn in plans."
    # [Scene: Municipal Planning Office | Early Evening]
    hide niko_alvarez
    hide mara_voss
    hide lena_park

    scene bg ch4_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Swelling strings that resolve into an uplifting cadence]
    # play sound "sfx_placeholder"  # [Sound: Rain easing to a gentle patter on the window; an incoming message chime]
    "You return to the office with Tomas, Rosa, and Niko. Lena stays back to shape the feature, with a promise to sit on distribution until the pilot's governance is clear. The communications team drops a quick"
    "memo on the table: early press notice ready, tentative mayoral quote, a plan for the sod-turning ceremony. The mayor leans in, contemplative and open."
    show mayor_anton_chi at left:
        zoom 0.7

    mayor_anton_chi "We have enough to start the legal pipelines and to set dates. But there's one tactical decision we must make that will define public messaging and constraints."
    "He taps the timeline on the screen. Three divergent threads trace out: slow and community-led, a fast visible demo, or accepting a private-public funding clause that guarantees money but complicates control."
    "Every person in the room bends toward the map like moths to a porchlight. Tomas squeezes your hand under the table: a quiet anchor. Rosa's face is unreadable for just a moment—then she closes her eyes and exhales, offering you a nod that says, trust yourself."

    mayor_anton_chi "We want your recommendation, Mara. Which emphasis do we commit to for the pilot?"
    "You think of the week passed: permits routed, a ledger drafted, volunteers trained, a photographer told to wait. Success tastes like coffee steam and the sweetness of small, keepable promises. You also feel the gravity—the way one decision shifts who leads and who is visible."
    show tomas_herrera at right:
        zoom 0.7

    tomas_herrera "There's no single right answer. It depends on what risk we're willing to accept: risk to long-term integrity, risk to political capital, or risk to community control."
    show mara_voss at center:
        zoom 0.7

    mara_voss "We built this to last. But we also built it to be seen."

    mayor_anton_chi "Then say which we prioritize."
    "The moment stretches. This is the hinge; the pilot will carry the shape of your answer. You glance at Rosa—her expression is complex and steady. Niko punches his palm with a grin that masks nerves. Lena"
    "meets your eyes, waiting to anchor the story to truth, not theater. Tomas watches you with a faith that makes the decision feel less like a solitary line in the sand and more like a shared"
    "strategy."

    menu:
        "Prioritize ecological integrity and community-led timelines, even if slower.":
            jump chapter5
        "Stage a fast, visible demonstration to win public opinion and more funding.":
            jump chapter6
        "Accept a private-public funding clause that reduces community control but guarantees full pilot funding.":
            jump chapter6
    return
