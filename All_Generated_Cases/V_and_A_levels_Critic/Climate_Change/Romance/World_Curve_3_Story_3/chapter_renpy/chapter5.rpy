label chapter5:

    # [Scene: Community Center | Late Afternoon]

    scene bg ch5_4001e7_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low buzz of overhead lights, the distant metallic clack of tools from outside, a printer spitting out a permit copy]
    # play music "music_placeholder"  # [Music: A taut, propulsive string ostinato — quickening]
    "You stand at the table like a hinge between two rooms: the room that wants the grant and the room that remembers the boathouse. The linen blouse at your collar is slightly rumpled from three hours"
    "of meetings; the brass compass pendant is cold against your throat and heavier than it was this morning. Your fingertips hover over the pen as if memorizing its weight."
    "Mayor Rosa slides a thick packet across the scuffed table. 'These are the conditions,' she says, voice even and municipal. 'Liaison will require weekly benchmarks, quarterly audits. They want timelines attached to each deliverable.'"

    "Liaison" "And access to engineering plans for dredging, should we agree that dredging is part of long-term stabilization."
    show maia_rivera at left:
        zoom 0.7

    maia_rivera "Access in what form?"

    "Liaison" "Read-only, encrypted. For compliance oversight — not operations. It's standard for any state-backed restoration where sediment movement could affect other jurisdictions."
    show jonah_kade at right:
        zoom 0.7

    jonah_kade "Read-only or not, a map's a map, Maia. Changes on paper can change nets. They don't have to say 'we'll reroute fish'—they can make it happen between meetings."

    maia_rivera "We will write strict access clauses,' you say. You mean it the way you mean a field plan: with caveats, with contingencies, with margins for error. 'We will require community sign-off on anything that affects migration routes. Mayor Rosa — can we put that in the memorandum?"
    show mayor_rosa_santiago at center:
        zoom 0.7

    mayor_rosa_santiago "We can negotiate. But the quicker we sign, the quicker crews start. People are already volunteering."
    "Ava Kim is beside you before you finish the sentence, tablet warm against her palm. She thumbs through sample vials arranged like a small, careful constellation — sediment size fractions, salinity strips, seedling survivorship probabilities."
    hide maia_rivera
    show ava_kim at left:
        zoom 0.7

    ava_kim "If we prioritize high-marsh species and begin matting in those tidal windows, we can buy time against surge models for the next six months. It'll reduce immediate overwash events along the quarter sections.' She taps a graph until the bars line up like teeth. 'We can stretch the schedule if we hire three local crews for planting and someone to manage sediment traps."
    "Lupe Kade folds payroll papers with the rapid, exact hands of someone who grew up translating catches into ledgers. She meets your eyes and lifts a brow. 'I'll keep them paid and fed. We bring in the mats this week, we bring in labor. Payroll's tight, but doable.'"
    hide jonah_kade
    hide mayor_rosa_santiago
    hide ava_kim

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distinct rhythmic drumming from the protest; muffled chants]
    "Dana Park's voice comes through the doorway raw and immediate. 'No strings! No corporate oversight! Maia — you can't sell our marsh for materials!'"
    "You feel the room contract. The strings in the music tighten."
    show dana_park at left:
        zoom 0.7

    dana_park "They'll use our consent to do whatever their contracts permit. Once a clause is signed, it's law in practice."
    "You step toward her as people crowd the doorway — town members, cooperative hands, a few reporters. You could step outside, take a megaphone, explain the clauses and the safeguards. You could also finish the paperwork and make the protection tangible with mats and stakes. Either move will make waves."

    menu:
        "Step outside and meet Dana at the doorway":
            "You move through folding chairs and murmuring, palms warm with the pen. Outside, faces tilt toward you like gulls; you speak in measured sentences, naming clauses and guardrails, and Dana listens with jaw clenched but eyes scanning for the seams."
        "Stay and finish the signatures at the table":
            "You keep your seat, the pen cool under your hand. Lupe hands you the next envelope; you sign in quick, exact strokes. Outside the drumbeat hits faster, but the mats are already scheduled to arrive. You hear Dana's voice—sharp, unfinished—through the glass."

    # --- merge ---
    "'You choose with the practiced cruelty of triage: triage is not mercy; it's necessary harm distributed to the least catastrophic end. Whether you moved or stayed, the practical flow of the room continued: signatures, initials, scanned forms.'"
    "Elias Wren appears in the doorway like a schematic folded into a person — immaculate trench coat, AR pin catching the light. His smile is a thinly calibrated thing."
    show elias_wren at right:
        zoom 0.7

    elias_wren "Congratulations on the approval, Maia. You pushed hard for community leadership in that proposal. That's commendable."
    show maia_rivera at center:
        zoom 0.7

    maia_rivera "Thank you,"

    elias_wren "We'll provide technical assistance when requested,' he adds, voice measured into partnership. 'And of course, we'll coordinate water-quality monitoring across the greater watershed. Cross-jurisdictional data is the key."
    "Jonah Kade watches him, the fisherman's ring turning in an absent gesture. You can read the thought in the narrow line at Jonah's mouth: not now, not like this. Jonah's patience is at something like a pressure point."
    hide dana_park
    show jonah_kade at left:
        zoom 0.7

    jonah_kade "Make sure your 'assistance' doesn't become a roadmap for corporate control."

    elias_wren "Local stewardship matters more than anything, Mr. Kade. You know that."
    "The exchange is polite and brittle, like two people knocking a fragile shell back and forth. It leaves a minute of silence breathing between them that feels like an intake before something louder."
    "There is work to do. You schedule crews on the whiteboard pinned to the gym wall, markers squeaking. Lupe crosses numbers off one list and adds shipping dates for restoration matting. Ava sketches a planting cadence, voice tight with the speed of execution."
    hide elias_wren
    show ava_kim at right:
        zoom 0.7

    ava_kim "If mats are in by Friday and crews start Saturday, we get two tidal windows before the model's projected storm surge. We can seed the high marsh in the first window and the transitional marsh in the second. We need to deploy sediment traps before the dredging plans are even discussed, so natural accretion has a chance to do its job."
    "You press your thumb to the edge of a map, feeling the paper's grain. The liaison's requirements hover on the edge of every plan. The state liaison will audit that schedule. They will want to see movement on the ground as much as they will want deliverables on paper."
    "Tomas Rivera's voice—older, textured with salt and stories—comes to you quicker now, not as memory alone but as a scent of pipe smoke and lemon soap who always speaks calmly even when storms come."
    hide maia_rivera
    show tomas_rivera at center:
        zoom 0.7

    tomas_rivera "You know the marsh better than anyone, Maia. Keep the people planting, but keep them safe from promises that sound like rescue until the rescue's shown its hands."
    "You breathe in, the compressed air of decision making, and the pulse in your neck picks up. There is no dramatic crescendo of victory here — only velocity: schedules, crews, concessions, clauses."

    menu:
        "Insist on a clause that requires community sign-off for any dredging":
            "You point to the clause on the draft, pen underlining the sentence like a seamstress tacking thread. Ava supports you, raising modeling projections. Mayor Rosa nods slowly. The liaison frowns but murmurs that a separate memorandum could be drafted — it's not a 'no' yet."
        "Push for immediate matting and delay negotiating dredging access until after deployment":
            "You prioritize the mats with a curt nod. Ava starts a checklist. The liaison notes your preference; there is relief from volunteers already. But Dana's jaw tightens outside; she walks the perimeter like a warning."

    # --- merge ---
    "'The town hums in the thin, electric way of late afternoons when hands are busy and minutes are counted. Hammers ring, a metallic clang that threads into the municipal buzz. You think of the boathouse again"
    "— of boards lifted like ribs and the smell of tar — and the timeline you promised your community compresses like tidal pressure.'"
    "Night arrives on your rooftop garden with a copper sunset, a sky painted in bruised mauves and orange that catches the rosemary like a burnished coin. The rooftop is small, intimate, a reclaimed patchwork of potted"
    "succulents and reclaimed wood. It offers no solutions, only the vantage to see the whole town stitched with lights and the dark seam of the bay."
    hide jonah_kade
    hide ava_kim
    hide tomas_rivera

    scene bg ch5_4001e7_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant hammering fades; a gull cries once; the town conversation becomes a low, steady murmur]
    # play music "music_placeholder"  # [Music: A single violin line, high and insistent]
    "Jonah Kade comes up slow, carrying a thermos the way a person carries something steady for someone else. He sits next to you on the reclaimed bench, close enough that the strap of his jacket brushes your sleeve."
    show jonah_kade at left:
        zoom 0.7

    jonah_kade "You did right by getting materials. We can't plant with promises."
    show maia_rivera at right:
        zoom 0.7

    maia_rivera "We bought time,' you say. 'Inches and nights."

    jonah_kade "Inches can be everything,' he says. 'But the way it's written—there's room for them to turn 'access' into 'override.'"
    "You both sit in the space where technical clauses and human consequences overlap. The scent of rosemary is sharp enough to be a presence. Jonah's fingers find the brass compass around your neck which reflects the last light; the metal is cool, familiar."

    jonah_kade "You keep that thing for navigation and I keep this,' he says, tapping his wooden charm. 'Maybe they'll be of use yet."
    "Silence settles and then shifts. Jonah leans in closer than he used to when the town was only husks and plans. It's not dramatic — it's a private, slow approximation of what could be if two careful people were allowed to be less guarded."

    menu:
        "Let Jonah lean in; let the rooftop close around you":
            "You let the distance shrink. The rosemary and salt mix into a single scent; your shoulder brushes his. He doesn't move fast, only present. Words are unnecessary for a while — there is only the warmth of someone who keeps a steady watch."
        "Hold back, keep the conversation on the cliff of policy":
            "You keep your posture deliberate, a slight ease into practicality. You talk schedules and contingencies instead: more planting windows, a list of volunteer leads. Jonah's hand withdraws almost imperceptibly; the rooftop feels slightly larger, lonelier."

    # --- merge ---
    "'Jonah's eyes search your face as if cataloguing the town you carry. You think of Tomas telling stories about storms that tested more than roofs — they tested people. A low, honest fear unspools: with every"
    "clause you sign, the community's future tilts a fraction. That fraction will be felt in nets, in boathouses, in the slow memory of what the town keeps.'"
    "Elias Wren sent a message earlier, a brief, oblique congratulation that reads like an algorithm skimming the coast for leverage. Dana staged a protest that cracked the civic quiet into a new seam. Lupe is already"
    "balancing receipts against shipment dates. Ava's face is lit by her tablet, tracking growth probabilities."
    "The grant buys you nights and inches. The mats will arrive; crews will plant; classifiers will hum along the timelines you promised. The oversight liaison will check reports and timelines; you have set the clauses you could. You have also left unanswered the parts that are not in your hands."
    "You press the brass compass until it cools, a bruise of metal against your palm, and you feel the small, blunt question settle behind your ribs: does this cost the thing we were trying to protect?"
    "The rooftop wind lifts a rosemary sprig and carries salt and the faint echo of hammering from below into the space between you."
    # [Page-turn thought: The first mats arrive at dawn. The town will wake and move and the next sixty hours will feel like a season. You have bought a schedule of survivals—but you have also opened a door. Something will come through it; whether it's help or a deeper compromise is a question you will answer in work, word, and watchfulness.]
    # play music "music_placeholder"  # [Music: Crescendo into a single sustaining note, then a held silence]
    hide jonah_kade
    hide maia_rivera

    scene bg ch5_4001e7_4 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter7
    return
