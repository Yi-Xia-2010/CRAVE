label chapter18:

    # [Scene: Glasshouse | Dawn]

    scene bg ch15_f99e88_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the soft slap of water on pilings, a thermos lid clicking]
    # play music "music_placeholder"  # [Music: Low, tentative piano with sparse strings]

    "You wake before the glass warms. The greenhouse smells of damp soil, old cedar, and the faint chemical tang of peat pots—comforting and clinical at once. Your field notebook lies open on the bench, pencil tip worn thin. On the header, in your hurried hand, a list of deliverables and deadlines you promised to meet weeks ago" "Quarterly metrics; job-hours logged; 3 demo plots; outreach events."
    "Rina is already there when you step into the filtered light, sleeves rolled, sunglasses pushed up on her head though the sun is barely a rumor. She hands you a steaming cup that tastes like sugar and too much hope."
    show rina_park at left:
        zoom 0.7

    rina_park "They're early. The funders have a tight window; they flew in last night. We have to show turnover and measurable employment within sixty days."
    show mara_voss at right:
        zoom 0.7

    mara_voss "Sixty days,' you repeat, the number a stone in your mouth. 'That's—"

    rina_park "—aggressive. I know. But it's real money, Mara. You asked for leverage, and this is it."
    "An NGO Liaison appears in the doorway, careful shoes squeaking over wet flagstone. She wears a neat field vest and a smile practiced for press kits. She unfurls a tablet of slides that bloom into graphs when she taps them—the metrics of success."

    "NGO Liaison" "We're excited. We'll prioritize workforce training modules and immediate deployments. We'll connect you to contractors for the pilings and green-mat suppliers. We want photos on Day Thirty."
    "You study her face instead of the numbers—hosted optimism, ready to be boxed and shipped. You think of the seedlings in the mud, of the way eelgrass flushes green like breath, and you feel the known compromise settling like salt crust on your skin."

    mara_voss "Photos make good headlines. But miracles take more than a month to root. Maintenance is ongoing—"

    "NGO Liaison" "We understand that. But our donors need outcomes within their fiscal year. We can arrange follow-on funding if metrics look good."
    "You feel the logic line up like a ledger entry: deliver quick wins, hope donors renew, scale up. The word 'if' bruises your optimism."
    "Rina leans in, voice small and fierce."

    rina_park "We can be strategic. Put priority on high-visibility installs—boardwalk planters, a few demonstration marsh plugs near the harbor. Use local crews. Tracking hours will be straightforward."

    mara_voss "And long-term maintenance?"

    rina_park "Community buy-in. Eli's crew. Tomas' network. We'll sell it as skills and jobs."
    "You close your hand around the thermos until the metal warms your palm. How many promises are you willing to make that hinge on someone else's renewal?"

    menu:
        "Push hard for a binding maintenance clause in the grant":
            "Mara Voss asks the liaison about contractual maintenance obligations. She frowns, runs a hand over her tablet. 'We can add recommendations,' she says, not quite a commitment."
        "Accept the funder's timeline and focus on quick wins":
            "Mara Voss nods, eyes on the seedlings. 'Alright. Quick wins, clean metrics. We'll make it work.' Rina lets out a small, brittle laugh and goes to marshal volunteers."

    # --- merge ---
    "Continue"
    # [Scene: Marsh | Midday]
    hide rina_park
    hide mara_voss

    scene bg ch15_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Hammers and low conversation, the slap of boots in ooze, gulls circling like punctuation]
    # play music "music_placeholder"  # [Music: Rhythmic low percussion over sustained chords]
    "The first week is a flurry that tastes like adrenaline and salt. Locals you barely know are on the payroll—Nia among them, hair damp with sweat, teaching a pair of teenagers how to weave coir logs."
    "The community roster swells: fishers who needed cash, retirees who wanted to feel useful, and young parents grateful for any steady hours."
    "Elias 'Eli' Calder stands at the waterline, sleeves rolled, sketchbook balanced on his knee. He fits the new pilings with the efficient, easy motions you know by feel—like a carpenter whittling hope into something that holds."
    show elias_eli_calder at left:
        zoom 0.7

    elias_eli_calder "We're doing good work, Mara. These raised docks—people can still fish after a storm now. Kids will learn to tie proper knots again."
    "You walk the line of newly planted mats and think of the faintly green flecks where eelgrass should be. The funder representative wants proof: survival rates at thirty days, employment hours logged, neighborhood photos. You can produce that."
    show mara_voss at right:
        zoom 0.7

    mara_voss "Eli, the funding wants visible, fast results. That means the accessible spots get the first attention."

    elias_eli_calder "Accessible is fine. But who looks after this after the cameras leave? Who checks the mats after a hard tide? Who pays the crew to return?"

    mara_voss "We will. We'll train local stewards, set up a maintenance roster—"

    elias_eli_calder "Will the funder pay them after their reporting period ends? Or will Tomas' crew be the last check you'll be able to rely on because the grant closed?"
    "He doesn't say 'you made compromises,' but the question cuts there anyway. You feel the old ledger open between you: ecology versus economics, hope versus practicality. You both perform the same arithmetic, different endpoints."
    "Nia runs up, mud on her knees, eyes bright."
    show nia_voss at center:
        zoom 0.7

    nia_voss "We hit three hundred job-hours yesterday! Rina says it's exactly what the report needs."
    "You smile because the number is real, because hands are fed for now. But when you look across the marsh you see a pattern: neat, staged rows of success where the camera can reach, and a"
    "fringe of unreached swamp where the work will cost more and look—by the funder's metrics—less efficient."

    menu:
        "Insist that one of the demo plots be in a high-risk area to show real outcomes":
            "You make the case at the day’s briefing. Rina agrees reluctantly—'It'll be harder to sell'—but you notice the liaison's tight jaw."
        "Keep demo plots in visible, safer spots to secure more funding":
            "You defer. 'We need the donors to see wins,' you say. Elias 'Eli' Calder nods, but his gaze lingers on the unaddressed fringe like a clock you can feel ticking."

    # --- merge ---
    "Continue"
    # [Scene: Dock | Late Afternoon — Montage over months]
    hide elias_eli_calder
    hide mara_voss
    hide nia_voss

    scene bg ch15_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Montage—construction clatter, children laughing, a radio reading headlines]
    # play music "music_placeholder"  # [Music: Brass and strings build briefly then hollow into a minor key]
    "For a while, it's forward motion. Photographs go online: smiling crews, seedlings planted, grant logos prominent. Short-term relief arrives exactly as promised: paychecks, new trainees on résumés, a small pump of pride through the town. Mayor"
    "Rosa stands at a podium with the NGO Liaison and reads data into the microphone about job-hours and square meters restored. The developer's PR team takes note and begins to frame the visible mitigations as proof"
    "that large-scale construction can be sympathetic."
    "Mayor Rosa: (to a gathered crowd) 'This work shows what a partnership between community and outside support can do. We saved jobs and took steps for resilience.'"

    "Developer Rep" "It's encouraging to see communities adapting. These pilot measures show a model that could be integrated into our broader master plan."
    "Your stomach tightens into an index of unease. The developer's 'model' is a euphemism. In boardrooms, it will be used to justify more grading, more built shorelines—because a few visibility-focused mitigations have been performed."
    "Weeks become months. The NGO reports quarterly metrics, and donors celebrate. But as the second quarter approaches, conversations shift. The liaison calls Rina: budget constraints. The next tranche is smaller than promised, tied to 'targets met' in public-facing areas. Maintenance line items are trimmed."
    show rina_park at left:
        zoom 0.7

    rina_park "They want outcomes, Mara. They offered a bridge loan for maintenance but only if we can guarantee expanded 'scale.'"
    show mara_voss at right:
        zoom 0.7

    mara_voss "Guarantee? They want us to promise the future in exchange for a year."

    rina_park "Everything's a conditional."
    "You try to orchestrate a longer-term plan—maintenance trusts, local staffing contracts, municipal budget allocations—but the town is brittle. Mayor Rosa, whose reelection is an unspoken constant, is courted by the developer's promises of jobs and infrastructure. She mutters about re-election and practicality in private meetings."
    show mayor_rosa_alvarez at center:
        zoom 0.7

    mayor_rosa_alvarez "We can't tell people that a grant doesn't guarantee a paycheck next year. The optics are powerful, Mara."
    "You return to the marsh one grey morning and find a section of installed matting unmoored after a high tide. The coir rolls have floated loose where you were sure you'd anchored them well. Volunteers scramble;"
    "Elias 'Eli' Calder curses and wades chest-deep to secure them. Your clean metrics—those glossy photos—already feel fragile."
    # [Scene: Headland | Storm Evening]
    hide rina_park
    hide mara_voss
    hide mayor_rosa_alvarez

    scene bg ch15_f99e88_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind keening, distant rumble of a generator, the slap of waves taller than you'd expected]
    # play music "music_placeholder"  # [Music: Low cello with occasional sharp violin stabs]
    "The developer's next-phase permit goes before a state board. The developer brings forward images of the NGO-backed pilot as evidence the town has options. They propose a compromise: a raised promenade and commercial zones where the"
    "marsh 'lends' some ground. The argument is surgical and persuasive—because the pilot work made a tidy slice of protection visible to outsiders."
    "You find yourself in a meeting where the language is clinical and the stakes are the same as a tideline. Rina is quiet; the NGO Liaison is present, defensive. Mayor Rosa is hedging, fingers drumming."

    "Developer Rep" "Our plans integrate the already-proven mitigation areas and will raise the harbor-front with sustainable platforms. The pilots worked; they validate replication."
    show mara_voss at left:
        zoom 0.7

    mara_voss "Replication only works if there's a funding mechanism for ongoing maintenance and if we trust the designs in storm conditions. Pilots can prove concept, but they don't replace comprehensive protections."

    "Developer Rep" "We agree on that. Which is why the development will fund the scale-phase. It’s a win-win."
    "The room hangs on the phrase. You can see the math that will win votes. The developer offers jobs that are immediate and sizable—construction wages, spending that counts in tax reports. It is seductive in a way that survival is: blunt, measurable, and fast."
    "Elias 'Eli' Calder corners you afterward near the back stairway, rain spitting at his hair."
    show elias_eli_calder at right:
        zoom 0.7

    elias_eli_calder "They waved jobs at the council, Mara. People cheered. You couldn't talk them out of it."

    mara_voss "I tried to make the conversation about long-term maintenance, community trusts. I asked for binding clauses—"

    elias_eli_calder "You asked for what you could. But people needed to eat now. You wanted community control, but the reality is that bills don't wait for perfect contracts."
    "He is right. You know it. Your heart is a ledger of compromises and what you hoped would be the least harmful set of them. But being right doesn't remove the ache of watching the developer fold your pilot into their expansion narrative."
    # [Scene: Marsh Edge / Dock | Several Months Later — After a Strong Tide]
    hide mara_voss
    hide elias_eli_calder

    scene bg ch15_f99e88_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The creek's hollow churn, distant voices calling across the water, the creak of stressed wood]
    # play music "music_placeholder"  # [Music: Sparse piano descending into low, single notes]
    "The storm was not catastrophic by historical standards, but it was enough to show the seams. A stretch of pilot planting failed where the tide undercut the substrate; some coir rolls were ripped away. There are"
    "repair evenings—folks in high-viz jackets, damp and exhausted. The maintenance roster you set up stretches thinner as funds dwindle. The NGO Liaison is nowhere to be found; her emails slow, then stop."
    "In the weeks after, the developer increases pressure to commence grading in a different headland section. They point to the 'success' you helped produce and promise further mitigation. The argument sounds reasonable to voices tired of waiting for something better."
    "Rina speaks to you alone in the Glasshouse, palms folded."
    show rina_park at left:
        zoom 0.7

    rina_park "We did what we could with what we had. We created jobs. People ate. But the funders wanted photos, not infrastructure. They wanted to demo and move on."
    show mara_voss at right:
        zoom 0.7

    mara_voss "They wanted optics."

    rina_park "They wanted courage in a fiscal quarter. That’s not the same as stewardship."
    "Nia arrives late, hair damp from a morning patrol. She is younger, stubborn in her own way."
    show nia_voss at center:
        zoom 0.7

    nia_voss "They hired more construction crews downtown. Elias 'Eli' Calder says he'll get more work if he signs on for the developer's subcontractors."
    "Your chest tightens as if someone pressed a hand there. You exchange a look with Elias 'Eli' Calder that carries the load of promises made and promises broken."
    hide rina_park
    show elias_eli_calder at left:
        zoom 0.7

    elias_eli_calder "I can't watch Tomas' boat sit idle through another winter. I can keep working the marsh on small projects, sure, but my family's bills—"

    mara_voss "I understand."

    elias_eli_calder "Understanding doesn't fix the fridge."
    "The gulf between ecological fidelity and household survival yawns open. You feel the weight of your choices as physical—stones in your pockets, seaweed on your boots."
    # [Scene: Headland | Dusk]
    hide mara_voss
    hide nia_voss
    hide elias_eli_calder

    scene bg ch15_f99e88_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The crunch of gravel underfoot, the far wail of a horn, soft conversation fading]
    # play music "music_placeholder"  # [Music: Single violin, long and mournful]
    "You walk the ridge where once the marsh felt endless. Now the skyline is interrupted by cranes; the water's edge is a line of new pilings and a few surviving green patches. Some parts of the"
    "town are better off—jobs came, and people fed families. But you can see the cost: the fringe of the marsh, the places you couldn't get funded for, have thinned. The long timeline of ecological recovery got"
    "traded for short-term labor and visible, marketable mitigations."
    "Elias 'Eli' Calder joins you at the crest. There is salt in the air and something heavier between you."
    show elias_eli_calder at left:
        zoom 0.7

    elias_eli_calder "They want me to sign the contract next week. It's good money."
    show mara_voss at right:
        zoom 0.7

    mara_voss "And then?"

    elias_eli_calder "Then maybe I'll be gone for six months at a stretch. Maybe I come back on weekends. Maybe Tomas can keep the small work. I don't know."

    mara_voss "You'd—"

    elias_eli_calder "I know what you sacrificed to make this happen. I know you wanted a different bargain. I don't blame you for trying. But I can't keep waiting on the promise of renewals and hope."
    "You stand with the wind taking at the edges of your jacket. The life you stitched for the town with one hand has been pulled in another direction by contracts, donors, and the press-ready wins that"
    "made headlines. The funding you accepted—emergency, urgent, necessary—achieved things. It also reframed the conversation in ways you couldn't control."
    "Elias 'Eli' Calder's face softens with a weariness you recognize; it's the same expression you have when seedlings fail."

    elias_eli_calder "Maybe it's time I go where the work won't depend on grants. This place will hold you in ways I can't justify to my family. I'm sorry."
    "Mara Voss: (a thousand answers clambering) 'If you go—'"

    elias_eli_calder "Don't make this about guilt. This is survival. I need to keep Tomas' line alive."
    "You look at the lights—the new boards shining like a polished promise—and then at the thinning marsh, the places you couldn't get funded for, the maintenance you couldn't secure in perpetuity. You catalog the ways your decisions helped and the ways they hurt, a slow accounting."
    "Nia slides an arm through yours without asking."
    show nia_voss at center:
        zoom 0.7

    nia_voss "You did what you could. People remember that. But a few good photos don't fix every tide."
    "You press your hand to the coral pendant at your throat—the small, stubborn relic you keep when the world feels raw. It is warm from your skin. You think of the seedlings and of Elias 'Eli'"
    "Calder, of Rina's fierce faith, of Mayor Rosa's hard compromises. You think of the developer who turned mitigation into a stepping stone for more build."
    "You breathe in the salt and the gasoline tang from the site generators. The sound of the tide is a low metronome, indifferent and patient."
    "You close your notebook in your hand. The pages are full of hard-earned entries and notations of things left undone. You cannot unmake the months that have passed. The town is better in some measures and more fragile in others."
    "You look at Elias 'Eli' Calder one last time. You say what you can—soft, necessary words that try to hold what remains without pinning it down."

    mara_voss "Go if you must. Tell Tomas I owe him the next visit."

    elias_eli_calder "Take care of the marsh."
    "He turns away, shoulders set. You watch him walk down toward the town lights, and then his shape blurs into the crowd."
    "For a moment, the only sounds are the wind and the distant click of floodlights. You feel the sting of failure and the heavier, quieter fact that what you did mattered—to wages paid, to some stretches"
    "of coast spared immediate erosion. But you also feel the tether of dependency—the way the community's resilience now rolls on a funding-ladder that might not be there when another storm comes."
    "You stay on the headland as dusk stretches into the kind of dark that makes everything look the same color—small, resolute lights set against the sea. You think of the long years required for true restoration,"
    "of the ways bureaucracy and money have the power to reframe a community's future. You think of love and of how it sometimes bends under the weight of survival."
    "You are tired in a way that goes bone-deep. You have a record, a proof, and a ledger of compromise. You also have loneliness, because the person who shared your work and your life is walking away to keep his family's boat afloat."
    "The town will remember the pilot projects as a turning point—part victory, part lesson. You will remember the smell of peat, the sound of hammers, and the quiet of the Glasshouse in the mornings. You will"
    "keep working, because the marsh still breathes and because that is what you know how to do."
    hide elias_eli_calder
    hide mara_voss
    hide nia_voss

    scene bg ch15_f99e88_7 at full_bg
    # play music "music_placeholder"  # [Music: Low, waning cello tied to a single high violin note that rings, unresolved]
    # play sound "sfx_placeholder"  # [Sound: The tide rolling, farther and deeper than the floodlights]
    "You close your notebook and walk away from the headland. The list of compromises will sit beside your name in the town's memory—some will praise you, some will fault you, and most will simply continue with"
    "their days. You are left with an ache that is not entirely blame or pride: it is the clean, cold knowledge that saving people and place in the short term sometimes creates new, stubborn vulnerabilities in"
    "the long term."
    # play music "music_placeholder"  # [Music: Fade to near-silence]

    scene bg ch15_f99e88_8 at full_bg
    "THE END"
    # [GAME END]
    return
