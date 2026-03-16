label chapter14:

    # [Scene: Boardwalk | Dusk]

    scene bg ch12_e67f19_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A wooden fiddle rasping a long, hopeful tune; laughter; the sizzle of fish on a grill]
    # play music "music_placeholder"  # [Music: Low, mournful trumpet underscoring a community hymn]
    "You move through the festival the way you move through Tideward—hands cataloging, eyes holding, the journal already warm from being pressed to your ribs. Your pen never quite pauses; voices fold into fragments you tuck between"
    "pages: an old woman’s instruction on how to splice line so it won’t rot, a boy’s laugh that still remembers how to climb pilings, a man listing the names of streets that used to be whole."
    "The smell of salt and grilling fish hangs in the air, threaded with diesel and the sweet dust of damp wood. Lantern light pools on faces, softening hard weather and leaving everything a little more human."
    "For one living hour, cameras down at the promenade tilt from policy briefs to people. Reporters who’ve spent weeks quoting metrics now ask for the story of how Tideward learned to mend itself."
    "Mira materializes beside you with a thermos and a fistful of seed packets. She’s plastered a painted sign to the seed-exchange booth—“Bring a Seed, Take a Story”—and her grin is a moth to every lantern."
    show mira_soto at left:
        zoom 0.7

    mira_soto "You did this. Look at them. Even the kids are quieter—listening for once."
    "She brushes a smudge of flour from a volunteer's hair."
    show ava_marin at right:
        zoom 0.7

    ava_marin "We did it together. You did more than I ever could've planned."

    mira_soto "Bah. Your speeches do the heavy lifting. I just hand out the good biscuits."
    "You laugh, but the laugh strains at the edges. Pride is a bright, brittle thing tonight. It catches on everything—on banners, on interviews, on the glossy pamphlets that begin to appear at your periphery like barnacles on a hull."
    hide mira_soto
    hide ava_marin

    scene bg ch12_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rustle of paper; the soft metallic click of a camera shutter]
    "Tomas stands by the boat-turned-stage, hands folded into a canvas jacket that contains a lifetime of grease and readiness. He watches the crowd like someone watching a tide—calculating where it will lap and where it will pull back."
    show tomas_marin at left:
        zoom 0.7

    tomas_marin "They'll call it 'heritage' and sell it as nostalgia. Remember what they did with Old Dock? Only prettier. Don't let them sell you short, chica."
    show ava_marin at right:
        zoom 0.7

    ava_marin "I know. I remember."
    "Tomas's eyes flick to the pamphlets, to a scout sketching pilings with a measured, clinical pencil. You feel the pressure behind your ribs that never fully releases—responsibility braided with the fear of being outmaneuvered."
    "Ilan Cortez finds you between the seed exchange and a booth where someone teaches rope splicing. He smells faintly of solder and the sea; there’s a grease smear on his cuff. In his hand: a small"
    "glass vial of water he needs to test—routine for him, a ritual. He looks up at you with a kind of reckless optimism that has folded you up and carried you this far."
    show ilan_cortez at center:
        zoom 0.7

    ilan_cortez "You're doing the archive tonight, yeah? I caught the film crew saying they'd run a human-interest piece on Tideward tomorrow. This—"
    "He gestures to the crowd."

    ilan_cortez "—this could get the city to stop seeing us as a statistic."

    ava_marin "Or it gets them to draw a prettier map over us."

    ilan_cortez "Maybe both. If attention comes, we can steer it—microgrids, staffed community workshops. Make a proof-of-concept that shows our way works."

    ava_marin "And if 'proof' becomes a condition? A gate? What about the people who can't produce the right documents, who can't meet a timeline to 'prove' their memory?"

    ilan_cortez "Then we build the ability to carry them through. That's—"
    "You cut him off because the crowd shifts and a woman in a tailored coat parts through it like a blade. Evelyn Harrow moves into the lantern light with the exactness of someone who is practiced"
    "at public entry. Her smile is polite, diplomatic—an equable line that could be read as assistance or a signed contract."
    hide tomas_marin
    show evelyn_harrow at left:
        zoom 0.7

    evelyn_harrow "The festival is...beautiful. Tideward is alive."
    "She inclines her head toward you."

    evelyn_harrow "Thank you for letting the city see it."
    "You measure her words. There's the public cadence—soft, necessary—and then there are the things she does not say: the clauses waiting in offices; the donors who wait with checkbooks. Her eyes flick over the booths, cataloguing, notating."

    ava_marin "Thank you for attending."
    "Your voice is steady; your heart is not."

    ava_marin "But seeing is not the same as keeping."

    evelyn_harrow "I understand that more than you might think."
    "There is something in the way she says it that is both an invitation and a warning. The cameras pick up the exchange, which means this moment will be flattened into a quote in tomorrow's column. The festival’s warmth has already become currency."

    menu:
        "Walk over and accept the investor's pamphlet":
            "You take the glossy pamphlet with a steady hand, thumbs fanning the first page. The headline bristles like a splinter beneath your skin—'Heritage Village: Preserve and Profit.' You tuck it into your journal, not yet deciding whether to use it as reference or evidence."
        "Shake your head and step away from the suits":
            "You turn and find a booth to help with, letting the suits' smiles wash past you. The pamphlet lands on the table of a volunteer who doesn't ask questions, but your chest tightens as if you have left an unbandaged wound exposed."

    # --- merge ---
    "The festival continues to hum."
    "The festival continues to hum. A crew from the promenade's morning show records a family telling the story of a roof that once kept three generations dry. Their faces, lit and ordinary, make something in you"
    "unclench. For an hour, the city sees Tideward not as a project but as people."
    "Then the other cameras arrive—the ones with longer lenses and the kind of access that finds the soft underbelly of a community and captions it for a consumer. A well-dressed developer asks a booth volunteer, in"
    "too-friendly tones, about 'curation opportunities' and 'guest quotas.' You intercept them with a smile that is a little too sharp."

    ava_marin "Our stories aren't a product sample."
    "Developer: (rubbing his chin) 'Of course not. We want authenticity. We're proposing small-scale, tasteful preservation—heritage homes open for tour, local vendors on contract. Think of it as bringing visitors safely to the culture.'"

    ava_marin "You mean: visitors who will schedule their nostalgia online, pay for a lived-in exhibit, and leave without a trace of what made this place necessary in the first place."

    "Developer" "We can fund resilience if it's packaged correctly. Sponsorships, revenue-sharing. People love a good origin story."
    "The chorus of applause at the next booth—where a child just learned to splice rope—feels off-key now, as if laughter has become an accompaniment to negotiation. Your journal grows heavier in your bag, pages filling with"
    "half-phrases, overheard promises, and the names of people who taught you that memory is material."
    "Ilan Cortez finds you again. He is quieter now, calculating."

    ilan_cortez "They see value. That means leverage. If we can get a seat at the table, we can push for protections—contractual language about residency, guaranteed funds for repairs."

    ava_marin "Or they put residency behind proof: birth certificates, utility bills, landlord agreements. A sieve that privileges the paper-ready and abandons the rest."

    ilan_cortez "Then we write the policies to include alternatives—community attestations, oral histories, the archive itself as proof."

    ava_marin "You'd make people's lives the instruments of a legal strategy?"

    ilan_cortez "We already do that. We just formalize what we're already doing—make it legible to the city."
    "You feel the dividing line form—not between ally and opponent but between frameworks. The crowd is a map of all the ways people survive and the ways systems demand signatures. You want to tell Ilan that"
    "sometimes proof is a luxury, that your neighbors' lives are not data points to be optimized. He wants to believe process can become protection."

    menu:
        "Tell Ilan sharply that process won't save everyone":
            "Your words land like a weight. Ilan's expression closes for a beat—then reopens with a stubborn set. He reaches for your hand and squeezes, as if to bridge the logic you both live under."
        "Take a breath and suggest drafting community attestations together":
            "You suggest a tangible step—not surrendered hope, not naive faith, but making a tool they can't bureaucratically dismiss. Ilan's eyes glint. He promises to start the templates tonight."

    # --- merge ---
    "Night deepens. Evelyn returns, now accompanied by a municipal aide with a folder stamped with procedural language that speaks of timelines and conditional approvals."
    "Night deepens. Evelyn returns, now accompanied by a municipal aide with a folder stamped with procedural language that speaks of timelines and conditional approvals. She speaks in measured sentences, the kind that become policy. Her neutrality feels like an emplacement—precise, immovable."

    evelyn_harrow "The festival changed hearts. The public is moved. We can mount an interim protection. But it is temporary unless paired with a plan that satisfies investors and regulators."

    ava_marin "So protection in exchange for cosmetic preservation. Comfortable postcards versus the right to remain."

    evelyn_harrow "No. Preservation that secures long-term occupancy. But the city needs assurances—funding streams are finite, and there are risks if we delay."

    ava_marin "We asked for breathing room, not a time-limited exhibit."

    evelyn_harrow "I offered you the city's machinery because machinery protects. It is blunt. It is necessary."
    "There is a long silence. Lanterns tremble overhead as if the wind has facts to bring. You imagine the legal forms her aide now types—clauses that will require residents to verify, to enroll, to qualify. The"
    "legal stay that once kept bulldozers at bay now looks like a narrowing corridor with a gate at the far end."
    "You think of the elders who cannot find a birth certificate; of Tomas's hands that predate every registry. You think of the mural that lists names of streets erased from the official maps. Your ache is"
    "now braided with a new, sharper edge: the festival's warmth has made you visible, and visibility is an invitation."
    "You and Ilan stand in a pool of lantern light, the crowd hushed around a storyteller who speaks of a storm that did not take everything. Your fingers find his like a small, deliberate repair. The touch is a seam—comfort layered over the rip where truth has split."

    ilan_cortez "We can fight policy. We can make alternatives. We can keep building, documenting, proving ourselves on our terms."

    ava_marin "And if 'on our terms' becomes a product they can sell? If our life story becomes a revenue stream for someone else's profit?"

    ilan_cortez "Then we fight that, too."
    "He wants to believe there is a path that protects everyone: residents, stories, and dignity. You want to believe it with him, because hope with him is less lonely, and because the warmth in his hand is the truest map you've had in months."
    "But the city is already appetite-made. Investors take notes; scouts chart flows of foot traffic; an aide slips a timeline across a table that would make half your lists obsolete. The legal stay's breathing room narrows with every polite nod."
    "You close your journal for the night. The pages inside are a small archive of living things—faces, recipes, instructions—inked in the hope that if walls fall, someone will remember how to stitch them back."
    # play music "music_placeholder"  # [Music: A single low cello note, long and unresolved]
    hide ava_marin
    hide ilan_cortez
    hide evelyn_harrow

    scene bg ch12_e67f19_3 at full_bg
    "You let the lantern light hold you both for a moment longer—for the tangible solace of a warm hand where plans grow cold. Around you, the festival continues to hum, bright and alive and dangerous in equal measure."
    "This is the place you'll return to when the city offers contracts and conditional protects; it is the place you'll point to when you demand alternatives; it is the place that, for a breathing hour, made the city remember."
    "You close your eyes and name what you will not accept, not as a manifesto for the papers, but as a quiet vow: memory is not a tour, and people are not props."
    "You stand there, notebook weighing against your palm, and let the vow solidify into the thing it must be—messy, public, relentless."

    scene bg ch12_e67f19_4 at full_bg
    "THE END"
    # [GAME END]
    return
