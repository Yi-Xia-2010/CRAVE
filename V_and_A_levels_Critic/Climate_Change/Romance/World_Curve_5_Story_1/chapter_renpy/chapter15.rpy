label chapter15:

    # [Scene: Public Inquiry Room | Afternoon]

    scene bg ch15_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Murmurs, the clicking of camera shutters, a distant chant like a tide against glass. A single projector whirs softly.]
    # play music "music_placeholder"  # [Music: Driving strings, urgent but buoyant—momentum rather than panic.]
    "You step into a room that feels smaller than it did on paper. The leaked footage is already looping on a bank of screens: crisp renderings crosscut with contract pages, a face lit by a desk"
    "lamp as a whistleblower narrates the margins of the plan. The contractor estimate scrolls up one frame and the audience inhales as if it were cold water."
    "Mayor Serena Okoye clears her throat at the head table; the sound pulls every line of conversation taut. Elias stands to your right, sleeves rolled, his tablet casting a pale rectangle on his palm. He catches"
    "your eye—the look is steady, clinical, and threaded with something that wants to be softer. You keep your fingers curled around the vial at your throat until your knuckles ache."
    show mayor_serena_okoye at left:
        zoom 0.7

    mayor_serena_okoye "This inquiry will operate transparently. All testimony will be recorded. We will not allow expedited processes to outpace public accountability."
    "Jonah Hale: (smooth) 'Mayor, we welcome oversight. Our schedule—our projections—are designed to protect lives. Let us not mistake deliberation for delay.'"

    "Kira's voice slashes through from the back like a bell" "Delay has been their tactic for years. Oversight needs teeth—we want enforceable protections, not press releases!"
    hide mayor_serena_okoye

    scene bg ch15_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A ripple of applause and an irritated cough. Camera lenses focus like pupils.]
    "You move forward when your name is called. The room waits in that stretched second where syllables become structures—where story becomes policy. Mateo sits on the witness stool: his hands are knotted the color of sea"
    "rope, his voice raw with tide-worn authority. When he speaks, the room leans in as if to shelter his words."
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "I have fished these docks since before the sound of sirens drowned the bells. They say they'll protect the city. What they don't say is who will be moved so the rest can stand. I am not against a wall—I'm against a wall that takes our homes."
    "Jonah Hale: (interrupting; patient, practiced) 'We recognize the need for community safeguards. Contracts include compensatory measures—'"
    "You inhale and let your voice find its place on the table between models and renderings."
    show ayla_moreno at right:
        zoom 0.7

    ayla_moreno "Compensation doesn't grow back a garden. Compensation doesn't keep the memory of a place. We asked for co-management, for enforceable easements, for binding clauses that keep green spaces public. We asked for transparency. This leak showed us why."
    "Elias Rook taps his tablet; a projection lights the far wall. He steps closer, voice even but urgent."
    show elias_rook at center:
        zoom 0.7

    elias_rook "Our updated models account for phased interventions. We can deploy targeted engineering—localized surge barriers, raised service corridors—while preserving community-managed green belts that reduce storm surge and provide food security. The data show hybrid solutions lower long-term social cost."
    "Jonah Hale's jaw tightens. His smile thins into a line forged by pressure."
    hide mateo_alvarez
    show jonah_hale at left:
        zoom 0.7

    jonah_hale "Hybrid models are…idealistic. They require coordination and compromise that slow emergency mitigation. The city cannot wait through another storm."
    "Kira: (leaning forward) 'No, Jonah—they require honesty. And we will make you honest.'"

    menu:
        "Step to the mic and call for immediate legal safeguards":
            "You speak with a measured heat; your words land like pebbles into the chamber—firm, difficult to deflect. The cameras catch the tremor in your hands and the steadiness in your voice."
        "Motion to present Elias's model first to the panel":
            "You nod to Elias and he takes the floor, the model unfolding across the wall like a map of possible futures. The room leans into the diagrams, the numbers sharpening the argument."

    # --- merge ---
    "The chamber erupts into a dozen small storms—shouts, clipped questions from councilors, the low, constant hum of broadcast mics."
    hide ayla_moreno
    hide elias_rook
    hide jonah_hale

    scene bg ch15_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A surge of applause when Mateo is done. The projector clicks to a footage clip—contract line items juxtaposed with Jonah's public promises.]
    "An aide slips a folded press release across the table to Mayor Serena. She reads, then looks up. For a second her face is the map of someone learning the cost of sleep lost to vigilance."
    show mayor_serena_okoye at left:
        zoom 0.7

    mayor_serena_okoye "Given these revelations and the clear public outcry, I am ordering an immediate freeze on the expedited contract process. I am appointing an independent oversight panel, chaired by a legal ombuds and including community representatives—Ayla, Kira, Mateo will have seats—plus external auditors."
    "The room breathes as one, a loud, astonished exhalation that sounds like wind leaving a sail."
    "Jonah Hale: (cooling into something like calculation) 'A pause then. Fine. But pause must not become paralysis. We will cooperate—'"
    "Kira: (cutting across, fierce and laughing at the same time) 'Cooperate meaningfully or not at all.'"
    "Elias Rook reaches for your hand across the table; it is a quick, grounding contact—no promises, only presence. You squeeze back, a small vow that is both tender and strategic."
    # play music "music_placeholder"  # [Music: Strings swell into a victorious cadence—urgent and radiant. The arousal hits a high crest here: the crowd outside, the cameras, the sudden crack of hope.]
    "Outside the room, Kira’s protests swell into an organized hum. Screens along the harbor show the leaked footage in loops. People chant, then clap in waves like the sea. Volunteers hand out copies of the oversight charter, written in plain language and stamped with the signatures of neighborhood committees."
    # [Scene: Harborfront Boardwalk / Protest Sites | Evening]
    hide mayor_serena_okoye

    scene bg ch15_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Rhythmic stomps, a megaphone call and reply, laughter threaded through defiant songs.]
    # play music "music_placeholder"  # [Music: Percussive beats overlay the string motif—heartbeat tempo, communal.]
    "You push through the crowd with a stack of flyers and the sieve of salt on your tongue. Elias walks beside you—no tablet, just the weight of his shoulders and the steadiness of his jaw. Kira"
    "is a comet—everywhere at once—organizing shifts, pointing toward legal aid tents, coaxing an elderly couple to tell their story on camera."
    "A young organizer wraps a wet scarf around your neck and grins."

    "Organizer" "They froze the contract. You did that. We did that."
    "You look at the faces passing by—neighbors, kids with half-mended raincoats, Mateo arguing gently with a TV reporter—and the word you taste is not victory so much as mobilization that finally has a blueprint. Someone lifts a hand to you in a crowded high-five; the contact is small and electric."

    menu:
        "Stay on the front line with Kira until sunrise":
            "You lock your arm with Kira, trade a grin with Mateo, and keep moving. The night is long and needed; you know the work is collective."
        "Slip away with Elias to check the initial oversight charter draft":
            "You step into a quieter alcove with Elias. The draft is on his phone; he points to clauses and asks if they reflect community concerns. Your answers are blunt and exacting."

    # --- merge ---
    "Screens along the promenade flit between images of Jonah’s spokesperson offering guarded statements and Mayor Serena on a podium affirming the oversight. The crowd roars—part relief, part challenge—to be kept vigilant."

    scene bg ch15_f99e88_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant thunderhead rolls offshore. Rain begins as an attentive percussion on tarps.]
    "You realize the leak has done more than expose numbers and motives; it has centralized a scattered fury into a shared plan. The oversight panel will not be a magic wand. It is a tool—fragile, human, democratic—and for now it is in motion."
    # [Scene: Oversight Panel Venue / City Hall Annex | Night]

    scene bg ch15_f99e88_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Pens scratching, low-voiced negotiations, the soft ping of a legal database updating.]
    # play music "music_placeholder"  # [Music: Low, hopeful brass—steady wheels turning.]
    "You sit across from Jonah, whose expression has the sedimented calm of a man watching numbers shift beneath his feet. He addresses the panel with the same polished cadence he'd used in his presentations, but now each sentence meets cross-examination, each clause parsed."
    show jonah_hale at left:
        zoom 0.7

    jonah_hale "We are willing to re-run the cost-benefit with community co-metrics—adjust the land parcels to minimize displacement—"
    "Kira: (sharp) 'And add legal easements for the gardens. No takebacks.'"
    "A councilor asks for enforceability language. Elias reads, then suggests contingencies that bind infrastructure delivery to social-impact benchmarks."
    show elias_rook at right:
        zoom 0.7

    elias_rook "If surge protections aren't paired with guaranteed community-managed green spaces—if lease terms allow redevelopment without consent—then the metrics we model fail on social resilience. We can quantify this and put it into the contract."
    "Mayor Serena Okoye: (weary, relieved) 'We will include legal instruments that protect community plots—binding easements, audit clauses, public oversight with real enforcement.'"
    "A round of tired, cautious applause follows. You fold and refold a flyer until the creases soften. Mateo squeezes your shoulder with a grip that says 'we remember' more than 'we're saved.'"
    show mateo_alvarez at center:
        zoom 0.7

    mateo_alvarez "This isn't the sea backing down. It's us learning to move with it without losing our hold."
    # play music "music_placeholder"  # [Music: A bright, sustained chord. The arousal sustains high—there is triumph here, but it is tempered and practical.]
    # [Scene: Community Greenhouse | Dawn]
    hide jonah_hale
    hide elias_rook
    hide mateo_alvarez

    scene bg ch15_f99e88_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft conversation, the scrape of trowels, a gull calling faintly as if checking in.]
    # play music "music_placeholder"  # [Music: Warm piano underwrites the scene—gentle, resolute.]
    "You are back among soil and the honest, unglamorous chores of growing things. The greenhouse is quieter than last night’s roiling street but thick with the same intensity—now patient, purposeful. People move with dirt under their nails and something like peace in their shoulders."
    "Elias Rook kneels beside you at a new bed. He hands you a small handful of seeds—black sesame or something equally ordinary—his fingers brushing yours. There is an awkwardness that is almost tender: both of you"
    "have been carrying the city's weight, and neither of you pretends all cracks have been smoothed."
    show elias_rook at left:
        zoom 0.7

    elias_rook "We did the math. We drafted clauses. You kept us honest when I was about to bury nuance under expediency."
    show ayla_moreno at right:
        zoom 0.7

    ayla_moreno "You brought data when I needed it to be visible. You also stood in front of cameras and said the city could do better. That mattered."
    "Elias Rook: (smiling, a brief, relieved thing) 'I stood because it was true. I... I don't like the way plans sound when they forget people.'"
    "You laugh—short, dry—and then the laugh eases. There are awkward admissions to be mined, apologies to be made, and patience to be rebuilt. None of those weigh like verdicts; they are work, the same as soil."
    "Elias Rook reaches for your hand. He doesn't make a promise that will look neat on a charter. Instead he says something smaller and steadier."

    elias_rook "I want to keep working with you. Not to fix everything overnight, but to be honest about what we can do together—and what each of us will hold onto."
    "You feel the heat of the greenhouse on your face, the scent of wet earth in your nose, and the truth of the moment: it is not closure as in perfect solution; closure here is an agreement to continue, to be present while the city does its slow, relentless work."

    ayla_moreno "We'll make a checklist. Planting calendar. Public audits. And no secret clauses."

    elias_rook "No secrets."

    menu:
        "Reach up and tuck a stray hair behind his ear":
            "You do—a small domestic gesture that feels almost scandalous after the city hearings. Elias's smile loosens; there's a softness there, the comforting kind that grows from shared struggle."
        "Pull out your field notebook and sketch the bed plan together":
            "You flip open the notebook. Together you plot curbside beds and hedgerow buffers. It's methodical, intimate work—the kind that erases grand pronouncements and leaves what lasts: action."

    # --- merge ---
    "The first light thickens; beyond the glass, cranes slice the horizon but idle, constrained by the freeze and the oversight. People arrive to volunteer; someone brings fresh coffee. A poster is pinned to the board: 'OVERSIGHT PANEL - OPEN SESSIONS EVERY MONTH. ALL WELCOME.'"
    hide elias_rook
    hide ayla_moreno

    scene bg ch15_f99e88_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A chorus of tools, voices low and purposeful. A child's laugh begins at a nearby table where seedlings find new homes.]
    # play music "music_placeholder"  # [Music: The strings resolve into a hopeful, open interval—warm but not smug.]
    "You run your fingers through the soil, feeling its cool grain and the tiny resistance that promises yield. This is not the end of storms or of hard choices. It is a recalibration: hybrid measures here,"
    "gardens protected there, audits scheduled and enforced. The seawall proposals are not dead—some engineering remains necessary—but they will now be anchored to community rights and transparent metrics."
    "Mateo comes up behind you with a battered thermos and an old grin."
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "You kept your hand on the wheel when everyone else wanted the map. Not everyone would do that."
    show ayla_moreno at right:
        zoom 0.7

    ayla_moreno "We all did the keeping."
    "Elias Rook presses the back of his hand against yours for a moment—no drama, just contact. You let it rest there, letting the quiet insistence of presence speak for now."
    hide mateo_alvarez
    hide ayla_moreno

    scene bg ch15_f99e88_9 at full_bg
    # play music "music_placeholder"  # [Music: A single cello note holds, then fades into an airy, uplifted hum.]
    "You close your eyes, inhale the thick, wet air, and make a small, private inventory: gardens saved, contracts frozen for scrutiny, Jonah circumscribed by public will, oversight in place, and a companion at your shoulder who"
    "has learned to measure outcomes with compassion. The future is still a map with blank spaces—but now there are tools to draw the lines together."

    scene bg ch15_f99e88_10 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft applause from a nearby table—volunteers congratulating each other. Someone sings under their breath. A gull circles and moves on.]
    # play music "music_placeholder"  # [Music: Rising, then resolving into warm, confident harmony—high arousal maintained but settling into sustaining hope.]

    scene bg ch15_f99e88_11 at full_bg
    # play music "music_placeholder"  # [Music: Sustain, then gentle fade]

    scene bg ch15_f99e88_12 at full_bg
    "THE END"
    # [GAME END]
    return
