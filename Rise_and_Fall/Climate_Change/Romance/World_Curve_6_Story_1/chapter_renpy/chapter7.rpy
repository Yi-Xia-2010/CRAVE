label chapter7:

    # [Scene: Community Legal Clinic | Morning, overcast with a thin rain]

    scene bg ch7_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Soft, rising strings; a cautious but hopeful tempo]
    # play sound "sfx_placeholder"  # [Sound: Rain pattering on corrugated metal outside; the distant, hollow thud of boots on wet boards]
    "You feel the word 'injunction' like a small, precise tool pressed into your palm. It is legalese and promise and a temporary hinge that might keep Tideward's walls standing while the city is forced to look."
    "The room smells of ink, lemon-scented disinfectant, and the wet cotton of banners—a smell that says people have been awake all night turning fear into paperwork."
    "Rahim sits across from you, fingers fanned over a stack of printed affidavits. His calm is like a bass note under your nerves—steady, guideline-strong. Mira tucks a damp strip of fabric into her hair; she hums"
    "a tune you can't place, the way someone hums to steady the hands that work. Tomas leans against the doorway, sleeves rolled, his mechanic's laugh sounding softer than the engines he loves."
    show rahim_okoye at left:
        zoom 0.7

    rahim_okoye "The clinic managed pro bono counsel. We've got a judge willing to hear an emergency motion if we can show imminent harm and community organization. That's your leverage."
    "You look down at your hands—scabbed knuckles from pulling nails last week, the thin silver wave ring on your index finger catching a stripe of light that leaks through a high window."
    show ava_marin at right:
        zoom 0.7

    ava_marin "Imminent harm is easy to show. This is more than hazard; it's erasure. We need to prove the city's plan will displace people without adequate rehousing or cultural safeguards."

    rahim_okoye "Exactly. Testimony, timelines, photos, the archive. We need faces and memories as evidence of cultural value—something that indicates the loss would be irreparable in a social sense."
    show mira_soto at center:
        zoom 0.7

    mira_soto "I can read names. The kids at the archive night can help—grandmothers, fishermen, the milkman's route, the bakery that used to open at six. We make the map into voices."
    hide rahim_okoye
    show tomas_marin at left:
        zoom 0.7

    tomas_marin "And I'll haul the amp. If the judge hears 'this is where we lived' and 'this is who we are'—people won't be able to sign away what they could've saved."
    "A hush stretches; even the rain seems to listen."
    hide ava_marin
    hide mira_soto
    hide tomas_marin

    scene bg ch7_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The scratch of a pen as you sign the injunction petition; the sound feels ceremonial and small simultaneously]
    "You sign because action releases something taut in your chest. Paper becomes promise. Promise becomes pause."
    # [Scene Transition: March to City Hall Promenade | Midday, skies thinning]

    scene bg ch7_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: Growing chorus of hand-drums and a rising major chord; heartbeat tempo]
    # play sound "sfx_placeholder"  # [Sound: Feet splashing, distant gulls, the low voice of Tomas running through the PA, the flapping of wet banners]
    "You lead because you were born to know the streets—where the ground softens, where the tide has snuck inland. Your sea-glass eyes sweep the crowd: neighbors with braided hair, teenagers in hoodies with spray-painted signs, elders"
    "wrapped in thrifted coats bearing pins from old neighborhood campaigns. You recognize the weight they carry: houses patched year after year, photographs tacked to walls inside that the city’s architects will never see."

    menu:
        "Hand out laminated copies of the neighborhood map to anyone near the front":
            "You stuff laminated maps into waiting hands. Faces brighten as people recognize places—an aunt's stoop, a boarded-up corner store. Conversations ignite around the maps like kindling."
        "Take the megaphone and lead a chant":
            "You lift the megaphone and your voice, raw but clear, fills the promenade: 'Our homes, our voices!' The chant ripples outward; strangers fall into rhythm, and you feel the buoyancy lift the crowd."

    # --- merge ---
    "Tomas's laughter softens the group when he jokes into the mic about Rahim's legal briefs being the only things thicker than his lunch sandwiches; the sound curdles into genuine smiles. You pass the megaphone to Mira,"
    "who reads three names from your journal—names that echo along the waterfront and find the city's glass offices across the boulevard like tiny, stubborn anchors."

    scene bg ch7_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The press van door thumps; a muffled city announcement tries to frame the day in neutral terms]
    "A city spokesperson reads prepared lines about 'necessary planning and guiding development' while a municipal screen shows graphs and softened infographics. The promenade feels like a stage where two different grammars of future-telling meet: your ragged"
    "chant and their measured slides. You notice Ilan Cortez near the edge of the crowd—sleeves rolled, a damp edge where his vest met rain, hands in his pockets as if weighing the next best move."
    show ilan_cortez at left:
        zoom 0.7

    ilan_cortez "You did good. The judge will see the turnout. The technical memos are in the folder Rahim printed."
    show ava_marin at right:
        zoom 0.7

    ava_marin "You came."

    ilan_cortez "I can't not. I brought calibrated tide markers and a pump-demo for the hearings if they let me set up exhibits."

    ava_marin "Careful. The legal fight helps us talk on our terms. We can't let tech distract the story. If it looks like a takeover—"

    ilan_cortez "I know. I don't want to replace your story. I want to make sure it has a scaffold to stand on."
    "You both look past the crowd to the municipal steps where officials speak under a slate sky. For the first time in a long while, your stubbornness—usually a cliff-edge—feels like a plank you and others can stand on together."
    # [Scene: City Hall Promenade Steps | Afternoon, press briefing in progress]
    hide ilan_cortez
    hide ava_marin

    scene bg ch7_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Low brass with an undercurrent of hope]
    # play sound "sfx_placeholder"  # [Sound: Clicking cameras, the murmur of reporters, a child's high clarion shout of "Save Tideward!"]
    "Evelyn Harrow steps forward with that practiced composure—the steel-gray eyes sweeping, the trench coat immaculate. She is an island of control in moving water."
    show evelyn_harrow at left:
        zoom 0.7

    evelyn_harrow "We appreciate civic engagement. The administration is committed to resilience planning and fair relocation when necessary."
    "You feel the words land like measured stones. They are not lies, not entirely; they are the language of someone who knows how to make hard choices sound inevitable."
    show ava_marin at right:
        zoom 0.7

    ava_marin "Fair relocation is not fair if our stories are bulldozed with our porches. Fair means choice. Fair means resources we control."

    evelyn_harrow "We are open to proposals. The hearings will be thorough. If you have alternative plans, submit them. We'll review."
    "The crowd hums. The judge's clerk walks past with a stamped order in hand—your injunction has been filed and granted on an emergency basis. Time, formalized, stretches in front of you like a week-old tide pool: full of hidden things and opportunities."
    # [Scene Transition: Weeks of Hearings & Neighborhood Life | Various evenings and mornings]
    hide evelyn_harrow
    hide ava_marin

    scene bg ch7_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Warm, hopeful strings; tempo steady, like a working heart]
    # play sound "sfx_placeholder"  # [Sound: Soft laughter at an archive night; the rattle of a sewing machine; distant court gavel; waves licking at the pylons]
    "The legal stay buys the neighborhood a sliver of something precious: space. In that space, life blooms in ordinary, radiant ways. Oral-archive nights gather in a reconfigured storefront: a sewing circle passes around tea; someone plays"
    "a battered ukulele; an elder tells the story of a tide that came in so fast the bakery saved loaves on the back porch. Each story is testimony and also ritual—making the past durable."
    "You teach a pop-up clinic on sealing windows. Little hands press wax into seams; laughter and the smell of hot adhesive mix with the brine air. Mira pins names to a board—names from your journal and"
    "new names written in marker by children who insist on including their friends. Tomas rigged a sound-system onto a rescued cart; he toots a preposterous horn and the kids squeal."
    "Ilan Cortez shows up at hearings with diagrams and a prototype microbarrier; he stands at the back during testimony, pencil behind his ear, eyes flicking between a circuit diagram and your face. His presence is careful—supportive but hesitant to steer the narrative."
    show rahim_okoye at left:
        zoom 0.7

    rahim_okoye "You steadied the room. People weren't just angry—they were organized. That's the difference courts respect."
    "You find yourself buoyed. The meetings, the nights, the mundane repair days—they are small victories stitched together. You sleep more hours than you have in months. Your chest relaxes incrementally, like a muscle remembering how to let go."

    menu:
        "Ask Ilan to lay out a one-page technical summary for the hearings":
            "He nods and unrolls a clean sheet of sketches. You watch him translate lived experience into schematics, careful not to overpromise. The clarity helps the legal team frame feasible alternates."
        "Keep the hearings strictly narrative—no technical exhibits":
            "You tell Rahim you want testimonies to remain the central evidence. Mira squeezes your shoulder, grateful. The legal team adjusts their emphasis to personal accounts and cultural impact statements."

    # --- merge ---
    "You notice the city shifts, too—Evelyn's spokespeople begin to reference your petition in their press statements. They copy the language of 'community engagement' in a way that tastes like imitation but it also means they have to reckon with your terms in front of a judge."
    # [Scene: City Hall, a Meeting Room | Late afternoon, a formal table]
    hide rahim_okoye

    scene bg ch7_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Low, patient piano; a steadying, warm undercurrent]
    # play sound "sfx_placeholder"  # [Sound: Chairs sliding, the rustle of paper, a distant gull]
    "Evelyn Harrow sits across from you in a room that smells faintly of disinfectant and lemon wood polish. Her posture is upright; you can tell she counts tempo like a machine, but her eyes—steel-gray, narrow—carry an attentiveness that is not hostility, merely calculation."
    show evelyn_harrow at left:
        zoom 0.7

    evelyn_harrow "This is an opportunity to protect residents and ensure the city's long-term viability. We are not immune to cultural concerns, but we must weigh options fairly."
    show ava_marin at right:
        zoom 0.7

    ava_marin "We don't want to be collateral in a plan that leaves us nowhere to hold our memories. If you want viable policy, it has to include community-led safeguards, archival relocation plans, and meaningful rehousing offers."

    evelyn_harrow "Meaningful is a subjective standard. The hearings will have experts—planners, hydrologists, engineers. Your testimony will be considered alongside that data."
    "You feel Rahim's gaze at your back like a support. He slides a folder across the table—affidavits, testimonies, photos, the archive's migration plan. The paper is ordinary, but together it reads like a living map of what you refuse to lose."
    "Evelyn Harrow: (after a measured pause) 'We will bring these into the record. We are prepared to adjust timelines pending evidence. This stay buys time for all.'"
    "The phrase 'buys time' lands differently than a reprieve; it's a negotiation. But for the first time in months the word 'we' feels less like a democratic abstraction and more like a threadable rope."
    "You breathe in salt and city air and feel a rising buoyancy—small and stubborn. The stay has opened a seam; now you must decide what to stitch into it."
    hide evelyn_harrow
    hide ava_marin

    scene bg ch7_453e40_8 at full_bg
    # play music "music_placeholder"  # [Music: Soft, ascending harp; hopeful cadences]
    # play sound "sfx_placeholder"  # [Sound: Low ocean sighs, the whisper of pages turning at an archive night, soft murmurs]
    "Weeks of hearings shape a new rhythm. Candlelit gatherings on the Moonlit Boardwalk become both solace and witness. Children run with lanterns; elders hand down songs that travel down the pier and echo in the fog."
    "You stand there, journal in hand, feeling the past press against your ribs in a way that no plan or patent can entirely quantify."
    "Ilan Cortez slips up beside you, damp from the boardwalk mist."
    show ilan_cortez at left:
        zoom 0.7

    ilan_cortez "You look… lighter. Is that allowed?"
    show ava_marin at right:
        zoom 0.7

    ava_marin "Only after a court says we have a chance."

    ilan_cortez "I brought extra diagrams."

    ava_marin "You and your diagrams."
    "He laughs, and behind the laugh you hear gratitude—the kind that has nothing to do with judges or policies. It is private and real."
    # [Scene: Community Legal Clinic | A week later, afternoon]
    hide ilan_cortez
    hide ava_marin

    scene bg ch7_453e40_9 at full_bg
    # play music "music_placeholder"  # [Music: Quiet, sustaining strings; warmth]
    # play sound "sfx_placeholder"  # [Sound: The low murmur of community organizers; a kettle whistles]
    "Rahim gathers everyone to outline the next phase. The legal stay has given you a choice: how to use the time to best secure Tideward's future. It is a delicious kind of pressure—full of responsibility but also possibility."
    show rahim_okoye at left:
        zoom 0.7

    rahim_okoye "We can push the hearings in several directions. Keep the focus on community testimony—memory, cultural ties. Or bring technical counterproposals to show alternatives. Or stage a public festival to win hearts and public attention."
    "You look at faces around the table: Mira's expectant smile, Tomas's practical nod, Ilan Cortez's tentative openness, your own hands clenched around your pen. Each option is a different kind of commitment—each shaped by what you fear and what you hope."
    "You feel the tide of the room press against your ribs again, but now the pressure is less like an imminent crash and more like a lift—momentum carrying you forward."

    menu:
        "Read aloud a passage from the journal at the next hearing":
            "You choose a page where an old neighbor describes her porch and the sound of the tide. Your voice cracks once; then it steadies. Judges and reporters quiet down—the page becomes a lens into what's at stake."
        "Organize a small repair clinic to run concurrent with hearings":
            "You schedule the clinic; kids learn to bolster a seam and elders teach how to tie knots that have saved boats. The footage of skill-sharing paints Tideward as a living, capable place, not a tragedy."

    # --- merge ---
    "You feel the glow of choice. The community has rallied; the city listens; time, for now, is on your side. The next move matters in ways both strategic and intimate. The legal stay has bought more"
    "than weeks—it bought you the space to define how Tideward will be argued in the city's language."
    "You close your journal for a moment, the leather warm under your palm. The decision isn't just tactical; it's an extension of who you are and who you want Ilan and the neighborhood to be. You"
    "can feel possibilities like small boats lined up, each one promising to carry a different load."
    "Your voice has changed over these weeks. It still trembles at times, but it also carries the steady weight of an organizer who has learned to turn panic into plans. You feel buoyant in a way"
    "that swells not from certainty but from a community gathered and a legal instrument that makes the city listen."
    hide rahim_okoye

    scene bg ch7_453e40_10 at full_bg
    # play music "music_placeholder"  # [Music: A bright, swelling chord; hope articulated]
    # play sound "sfx_placeholder"  # [Sound: A round of quiet applause from the room; someone whistles an old tune]
    "You inhale the damp, briny air, taste optimism—the metallic tang of determination and the sweet of shared victory."
    "The next choice will shape what you do with this margin of time. You know the stakes and you know the people who will follow your lead."

    menu:
        "Keep the hearings centered on community testimony and cultural value.":
            jump chapter8
        "Invite Ilan to present technical counterproposals in the hearings.":
            jump chapter9
        "Stage a high-visibility repair-and-resilience festival to win public sympathy.":
            jump chapter13
    return
