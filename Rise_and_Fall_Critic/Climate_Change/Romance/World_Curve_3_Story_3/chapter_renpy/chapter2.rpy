label chapter2:

    # [Scene: Saltbridge Community Hall | Evening]

    scene bg ch2_c4ca42_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low rumble of distant surf; the hall door thumps closed against a wet gust]
    # play music "music_placeholder"  # [Music: Low, somber strings; soft piano undercurrent]
    "You push through the door with the notebook pressed to your ribs like a talisman. The fluorescent bulbs inside throw honeyed light across folding chairs and a long table scarred with coffee rings and pushpins. The"
    "room smells of strong coffee, lemon oil from Rosa's dishtowel, and the dry, metallic tang of seawater carried in on people's coats. Hands—salt-rough, ink-stained, gloved—reach for door handles; voices bloom and fold into one another."

    scene bg ch2_c4ca42_2 at full_bg
    "Narration: You set your bag down, fingers finding the familiar groove of the dented compass at your throat, the red thread warm against your pulse. The notebook slides open on the table without ceremony. Your plan"
    "is there in ink, neat columns of people, resources, and time—but the edges of the page feel fragile under your thumb."
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "Maya, you got the front table? I saved the good pastries for you."
    show maya_serrano at right:
        zoom 0.7

    maya_serrano "Thanks, Rosa."
    hide rosa_alvarez
    hide maya_serrano

    scene bg ch2_c4ca42_3 at full_bg
    show dr_hana_park at left:
        zoom 0.7

    dr_hana_park "The latest runs are—' (she taps the screen; a small model shivers into life) '—worse in the near-term than we'd hoped. Localized surge risk up along Old Wharf by mid-season, even under conservative scenarios."
    "You: (you let the words settle like cold stones in your stomach) 'How bad?' (your voice is steadier than you feel)"

    dr_hana_park "Probability increases for a two-in-three chance of moderate flooding within the next eighteen months if we don't change exposure or defenses. There are options, but they're trade-offs—cost, displacement, maintenance."
    "Finn: (voice low, suddenly) 'You remember Mrs. Gutiérrez's porch light going out? That sound—' (he trails off, fingers tightening on the rope) 'I remember the tide stealing her steps. We can't make that a story we tell later.'"
    "Rosa: (leans forward) 'Then we fight for what's fair. Not some glossy wall that shuts people out.'"
    # play music "music_placeholder"  # [Music: Dissonant chord; the room tightens]
    "Narration: Warmth frays into tension like a sweater snagged on a nail. You can feel how the maps become battlegrounds, how every spoken syllable slides into policy and pocketbook. You breathe in lemon and coffee and the metallic scent of stakes being raised."

    menu:
        "Let Finn finish, hold the room with the memory":
            "You sit back, let his silence amplify what he didn't say. The room hushes; faces turn inward with grief and resolve."
        "Pivot to data; ask Dr. Hana for a clear recommendation":
            "You point to the tablet, pressing the meeting back into the tangible. The numbers become a rallying cry, or a blunt instrument, depending on who listens."

    # --- merge ---
    "Continue main thread of the meeting."
    "Maya Serrano: (you look at the tablet, then at Finn) 'We need both.' (you try to stitch grief to facts) 'Hana—tell us the difference between a community-modular approach and a single corporate sea-wall. Lay it out plain.'"
    "Dr. Hana Park: (nodding) 'Modular—localized berms, living shorelines, community-led raised beds and removable barriers—lower initial capital, higher community labor, flexible maintenance. Corporate wall—faster, centralized, less visible social input, but high upfront capital and maintenance that can lock communities out if funding shifts.'"
    show rosa_alvarez at right:
        zoom 0.7

    rosa_alvarez "So who's paying for the labor if people are squeezed out? Who covers relocation if someone can't afford to retrofit?"
    hide dr_hana_park
    hide rosa_alvarez

    scene bg ch2_c4ca42_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The murmur lifts; a chair scrapes]
    show elias_novak at left:
        zoom 0.7

    elias_novak "Sorry I'm late.' (he crosses the room with a stride that somehow gathers the air) 'The fog patrol took longer than I thought. But I brought a stack of flyers, and—' (he spreads them on the table like offering) '—I brought people from the South Dock who are willing to help build, and we've been calling the press."
    "Maya Serrano: (your chest tightens—his presence is warmth and a shallow, hopeful fire) 'Elias—what are you planning to do? Press? Protest?'"
    "Elias Novak: (leaning in, amber eyes bright) 'Both. We can make noise. We can stop the council from rubber-stamping a contract that favors a private firm and expensive tech. We get people to show up. We make it politically costly to ignore community plans.'"
    "Noah Kestrel: (arrives at the doorway, passing through on the way to another meeting—navy coat damp at the cuffs, boots careful) 'Ms. Serrano.' (his voice is even, practiced) 'If I may—' (he pauses, sensing the room's"
    "mood) 'I don't want to derail community efforts, but timelines are tight. A coordinated, engineered sea-wall reduces immediate risk significantly and allows for long-term planning. There are efficiencies—single point contracts, maintenance schedules, predictable budgets.'"
    "Rosa: (sharp) 'Efficiencies for whom, Noah? The town? The firm? Because I've seen 'predictable budgets' translate into 'unaffordable to locals.''"
    "Noah Kestrel: (measured) 'I understand the distrust. My team is proposing a phased implementation with community benefit clauses.'"
    "Elias Novak: (mansplaining a smile that doesn't reach his eyes) 'Community benefit clauses on paper are not the same as community control in practice. We've seen that.'"
    "Maya Serrano: (you feel your old reflex—be the fulcrum—press against your ribs; you want to broker calm, but the air tastes like iron) 'Noah, can you give us specifics? On the clauses. On who decides access.'"
    "Noah Kestrel: (folding his hands) 'We can set up a joint oversight board—public members and technical leads. But I warn you: without substantial capital, we can't build to the modeling specs Hana just showed.'"
    show dr_hana_park at right:
        zoom 0.7

    dr_hana_park "And that capital gap is what the Mayor's office is trying to bridge, which brings us to—"

    "Mayor's Representative" "We appreciate the community's passion. There is a funding shortfall of approximately forty percent for the recommended measures. The administration is negotiating conditional funding that pairs public tax dollars with private investment. To expedite protection, the town is considering a contract with Kestrel Marine Development contingent on accelerated delivery timelines."
    # play music "music_placeholder"  # [Music: Low, brittle note — the kind before a crack]
    "Narration: The sentence lands like a sealed envelope on the table. The word 'contingent' tastes of strings attached. You see it—funding that might come with loss of control, with prioritization decisions made in boardrooms instead of kitchens."
    "Rosa: (quiet rage) 'So public money for private control. Funny, I thought public meant... public.'"
    "Mayor's Representative: (cool) 'The alternative is delayed protection. Delays increase exposure risk. It's a pragmatic path.'"
    "Elias Novak: (voice rising) 'Pragmatic for who? For a firm that can undercut community labor and lock out small fishers?'"
    show noah_kestrel at center:
        zoom 0.7

    noah_kestrel "That's not—' (he is interrupted by murmurs; he sets his jaw) 'We're trying to present a technically sound option that keeps the town functional. The opposition risks jeopardizing funding, leaving people exposed."
    "Maya Serrano: (you hear the argument but also the silent ache of responsibility—if you oppose the contract and fail, homes could flood; if you accept it, some neighbors may be priced out or displaced) 'We need"
    "to be honest about trade-offs. We also need to be honest about power—who sits at the table deciding what 'functional' means.'"

    menu:
        "Call for a pause—request a week to draw up a community proposal":
            "You ask for time. Some nod. Others shake their heads. Elias's jaw tightens, but there's relief in the pause. Noah scribbles in his tablet, calculating the window."
        "Push Elias to mobilize immediately—call a demonstration for the next city meeting":
            "You give Elias the nod. He smiles, energized; Rosa's hands ball into fists. The room divides between immediate action and measured planning."
        "Turn to the Mayor's rep—ask for exact terms on the contingency":
            "You fix the representative with a look. Her practiced calm flickers; she consults a page, buys time. The air smells of bureaucracy and rain."

    # --- merge ---
    "The meeting continues with commitments to follow up and develop proposals."
    "Elias Novak: (leaning toward you) 'If we show up in force, if we fill the council chambers, we can demand conditions—binding ones. The city can't ignore bodies and cameras.'"
    "Noah Kestrel: (level) 'Bodies are persuasive, yes, but bodies don't replace engineering funds.'"
    "Rosa: (hands on the table) 'We're talking about people's homes as if they're line items.'"
    "Finn: (voice small but steady) 'Promise me we don't let another neighbor become an anecdote.'"
    "Maya Serrano: (your mouth tastes like iron; the meeting is fracturing along predictable lines—values against timelines, equity against efficiency. For a moment you think of your compass, of that red thread, and of the night you promised 'everything.' 'Everything' is too big a thing for one person.)"
    hide elias_novak
    hide dr_hana_park
    hide noah_kestrel

    scene bg ch2_c4ca42_5 at full_bg
    "Narration: Voices repeat the same words in different keys: equity, efficiency, feasibility, displacement. You try to stitch them into a single coherent fabric and find the seams tearing."
    # play sound "sfx_placeholder"  # [Sound: Chairs scrape; rain taps the window harder as if urging decisions]
    "Narration: When the meeting breaks, it's not with agreement but with a brittle, practical scattering—people promising to reconvene, to follow up, to call. Rosa stays to stack chairs. Finn helps her, hands shaking. Dr. Hana lingers by the tablet, eyes on the models, mouth tight."
    "Elias Novak: (to you, quietly) 'We can get people. I can get people who have nothing left to lose and everything to save.' (there's hope in his rasp)"
    "Maya Serrano: (the reflex to be the fulcrum presses again—your shoulders already sore from it) 'And can you keep that hope from turning into anger that burns the bridges we might need?'"
    "Elias Novak: (his laugh is thin) 'Maybe not. But anger shows urgency.'"
    "Noah Kestrel: (passing by, softer than before) 'Maya—there are technical hearings next week. If you can get a community proposal on paper, it will be considered. If you don't, the administrative process favors the fastest, funded plan.'"
    "Rosa: (pointing) 'Which is Kestrel's plan if we let them lead.'"
    "Maya Serrano: (you feel the room's energy folding into small, sharp pieces you could try to hold together) 'I'll put together a community proposal.' (the promise leaves your mouth with a brittle certainty)"
    # play music "music_placeholder"  # [Music: A single, low piano note held too long]
    "Narration: When the hall empties into the wet night, the streetlamps throw halos on puddles. People drift away in twos and threes, speaking over shoulders. The air smells of hot coffee gone cold, of damp wool."

    scene bg ch2_c4ca42_6 at full_bg
    "Narration: You write one line across the blank margin, the ink catching on a tremor in your hand. The words feel both small and vast."
    "Maya Serrano writes: decide a direction."
    # play sound "sfx_placeholder"  # [Sound: The whisper of pen on paper; a gull cries in the distance]
    "Narration: The line tastes like iron because it is the hinge between refusal and compromise, between community control and institutional partnership. You can feel every weight of every face in the room pressed into that single sentence."

    scene bg ch2_c4ca42_7 at full_bg
    "Narration: Your thumb rubs at the dented metal. The red thread on your wrist snaps back against the pulse beneath it, an old promise demanding new terms."
    # play music "music_placeholder"  # [Music: A slow swell that doesn't resolve — lingering, unresolved]
    "Narration: The sea keeps time outside, indifferent and patient. Inside you, the choice coils like tidewater behind a gate."

    scene bg ch2_c4ca42_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade slightly, leave a single unresolved chord]
    "Page-turn thought: You imagine the council chamber stacked with people, you imagine a wall that glints like a blade or a shelter, you imagine houses raised on stilts and neighbors who can't afford the climb. All of it narrows to that one line in ink."

    scene bg ch2_c4ca42_9 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
