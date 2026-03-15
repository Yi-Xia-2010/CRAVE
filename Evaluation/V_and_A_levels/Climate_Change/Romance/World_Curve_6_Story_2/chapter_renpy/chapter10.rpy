label chapter10:

    # [Scene: Saltwood Quay | Night]

    scene bg ch10_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Tight, propulsive percussion — an anxious heartbeat tempo]
    # play sound "sfx_placeholder"  # [Sound: A gull's distant cry, the soft clack of loose boards, a low slab of construction machinery humming beyond sight]
    "You step out of the hall with the taste of warm coffee and other people's breath on your tongue. The decision hangs in your chest like a tide-clock wound too tight — wound down, then set"
    "moving again. The Mayor's filmed announcement rolls over the quay's tiny screen in a monotone that the town takes as news and relief at once."
    show mayor_jerome_hale at left:
        zoom 0.7

    mayor_jerome_hale "Immediate infrastructure will buy us time. Funding starts next week. Saltwood will have protection while we continue planning for ecological projects."
    "You hear the hollow echo of the word protection against the pilings. Investors smile in the footage the way lights do — hard, efficient, clinical. Dr. Elena Park stands beside the Mayor in the frame, composed,"
    "a thin line of satisfaction at the corner of her mouth; her posture reads 'capacity' and 'speed' the way a crane reads the weight it will lift."
    "You feel the hall's heat fade from your face and the salt air press against the hollow left behind. You told them what you thought was best, and you voted with the town's immediate survival in"
    "your hands. You can still smell the cedar scent from Nyla's tablet case, still feel the brass warmth of your tide-watch — small certainties in a room that had seemed impossibly large."
    "You fold yourself around the Mayor's words: the funding, the promise. The phrase 'buy us time' is both a valve and a warning. You keep walking along the quay toward the distant hard white lights, toward the construction site that now smells faintly of diesel and wet concrete."
    # [Scene: Corporate Seawall Construction Site | Late Night]
    hide mayor_jerome_hale

    scene bg ch10_453e40_2 at full_bg
    # play music "music_placeholder"  # [Music: Metallic timpani rolls; urgency ratchets upward]
    # play sound "sfx_placeholder"  # [Sound: Clang of steel on steel, walkie-talkie static, the steady thump of compactors]
    "You stand at the edge of the site, at the place the town has pointed as salvation. It is brazen and bright — an alien brightness that strips color from the cliffs. Machines inhale and exhale; they make salt and shadow into something measurable."
    "Dr. Elena Park walks by in a graphite trench coat that makes her seem carved from the same hardness as the concrete blocks. She does not look triumphant. She looks efficient. She hears the clank of the pile drivers and hears, too, the music of deadlines being kept."
    show dr_elena_park at left:
        zoom 0.7

    dr_elena_park "We move at first light. Permits confirmed. Community liaisons are on-site. We can keep people safe."
    show maya_serrin at right:
        zoom 0.7

    maya_serrin "They'll board up roofs tonight, save what we can.' (Your voice is steadier than you feel.) 'And the marsh work — the guarantees? The wording felt… provisional."

    dr_elena_park "Legal teams prefer 'phased commitment.' It's how we secure funding across jurisdictions. It allows us to deliver now and scale later."
    "You want her to see the word that sits between her two sentences — provisional — and to feel the grit of it. You want a promise you can put in a binder and not watch"
    "fray. You press your fingers into the cold railing and let the vibration of the machinery travel up your arm."

    dr_elena_park "We are not opposed to restoration. But the seawall's immediate benefit is countable lives and rooftops. You understand the calculus, Maya."
    "You do. You understand the calculus like you understand the tides: patterns, probabilities, the inevitable trade-offs laid bare by measurement. But the calculus does not hold stories — the sound of nets coming up heavy with"
    "history, Old Man Cala's voice on storm nights, the way Aiden Koa's mother still hums an old harbor song while mending nets."

    maya_serrin "Then give me language that forces a timeline. Not 'phased' — a calendar. Benchmarks. An accountability clause."
    "Dr. Elena Park studies you. For a moment she looks not like an antagonist but like someone trying to reconcile a spreadsheet with a map of living things."

    dr_elena_park "I'll push. But you must understand political bandwidth. If we ask too much, investors will balk."
    "You feel the friction — an edge where urgency and preservation grind against each other. The site breathes and works; it is already making the town look less at risk."

    menu:
        "Demand a concrete timeline now":
            "You step closer to the line of concrete and speak with the weight of the meeting room behind you. Elena's jaw tightens; she promises to 'expedite discussion' and asks for the exact clauses you want in writing. The talk becomes legalese and late-night emails."
        "Accept Elena's offer to 'push' and focus on on-the-ground needs":
            "You let the word 'push' hang between you, feeling the relief of a promise rather than the bite of a signed clause. Elena smiles with a professional patience and heads to the trailer to brief crews; the machines continue their rhythm."

    # --- merge ---
    "You walk away from the site carrying either the sharp draft of legal text or the soft promise of expedited talks. The night smells of diesel and possibility."
    # [Scene: Nursery Plots | Early Morning]
    hide dr_elena_park
    hide maya_serrin

    scene bg ch10_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: Quickened strings, a hopeful undercurrent threaded with tension]
    # play sound "sfx_placeholder"  # [Sound: Voices speaking warmly but urgently, the scrape of trowels, the slap of damp gloves]
    "By dawn the town's more human machinery is awake: volunteers with muddy knees, Nyla barking numbers into her tablet, the nursery's scent of peat and seaweed filling your nose. The visible action has calmed some sleeping anxieties; roofs patched, sandbags stacked like quiet promises."
    show nyla_torres at left:
        zoom 0.7

    nyla_torres "I drafted specific language — benchmarks for acreage, funding release tied to milestones, escrow for monitoring data.' (she taps the tablet, algae smudging the glass) 'But the legal team just said 'subject to appropriation.'"
    show maya_serrin at right:
        zoom 0.7

    maya_serrin "Show me."

    nyla_torres "We can push for an escrow clause. It's small, but it's enforceable. It compels investors to allocate the money when construction reaches acceptance tests."

    maya_serrin "How many votes does it take?"

    nyla_torres "It isn't votes. It's leverage. It's public record. It needs teeth, Maya. And support."
    "You look past Nyla, past the neat rows of plants, to where volunteers stack root-balled plugs into trays. Aiden Koa is among them, shoulder to shoulder with people who do not ask for explanations. He works"
    "with a methodical rhythm, his hands sure; the motion is a language he learned before words. Yet the set of his jaw speaks a different grammar."
    show aiden_koa at center:
        zoom 0.7

    aiden_koa "They put up lights and concrete, and the town breathes easier. Can't fault that.' (his voice is quiet; a net thrown across words) 'But the fish don't read headlines."

    maya_serrin "No. They don't."

    aiden_koa "You voted with the town tonight, Maya."

    maya_serrin "With immediate survival. With time to keep more roofs. I—"

    aiden_koa "Later has a way of being someone else's calendar."
    "There's no accusation in the tremor of his hands, only a sharper truth. He straightens, lifts another plug, and the muscle there is steady as a tiller."

    nyla_torres "We can make 'later' a condition. Escrow, release milestones, a citizen oversight board. It'll take public pressure."

    aiden_koa "Public pressure can tear a town apart if it isn't careful. People need roofs. They need roofs now."

    maya_serrin "Then we make the roofs and the commitments both. We don't make promises that read like apologies."

    menu:
        "Lay the plan for an oversight board, call out for volunteers":
            "You call for a quick meeting under the string of bulbs. Volunteers murmur assent; Nyla sketches a membership roster. Aiden signs his name with a careful stroke. The group grows loud with purpose, the nursery filling with quick plans and to-do lists."
        "Hold back and focus solely on securing the escrow language first":
            "You narrow your focus to the tablet and make a list of legal points. Others look to you for direction; Nyla nods and starts drafting emails. The air gets businesslike; hope is fenced into bullet points."

    # --- merge ---
    "Either way, plans are laid and roles assigned; momentum gathers in different shapes — community organization or legal scaffolding — but both begin the long work."
    # [Scene: Quay | Night — A Week Later]
    hide nyla_torres
    hide maya_serrin
    hide aiden_koa

    scene bg ch10_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: A single rising orchestral sweep; tempo relentless]
    # play sound "sfx_placeholder"  # [Sound: Distant drums of pile drivers, smartphone cameras shuttering, the murmur of reporters]
    "The televised ribbon-cutting is tidy and efficient. Lights frame smiling faces; the Mayor thanks donors; Dr. Elena Park gives a short, tempered statement about 'balanced approaches.' The town watches itself in the screens of strangers' phones"
    "and in the wet glass of shop windows. For a while, the visible certainty of action calms the public stomachs tied in knots."
    "You stand off to the side, a shadow between the lights and the dark. Volunteers clap in a practiced way. Some roofs are saved; that's measurable, immediate, real — numbers that soothe sleeping bodies."
    "But there are headlines, and headlines rearrange identity. 'Saltwood Secures Lifeline; Seawall Stabilizes Coastline.' The words feel like a ledger entry: saved house — checkbox; lost estuary access — an asterisk later, if anyone cares to tally it."
    "Your chest does not unclench. There is a small, private grief in the way the sea keeps doing what it does and your town looks to iron as panacea. The tide reflects the floodlights in long"
    "lines — bright notations across dark water. Each saved house is written beside a cost you can already imagine."
    "Aiden Koa sidles to stand by you, shoulder brushing yours in a way that bristles and comforts both."
    show aiden_koa at left:
        zoom 0.7

    aiden_koa "They made it look tidy."
    show maya_serrin at right:
        zoom 0.7

    maya_serrin "It is tidy for cameras.' (You think of Old Man Cala's stories about where the nets once hung, about dances on the shore that no longer happen.) 'It will keep people dry."

    aiden_koa "I wanted different things."
    "Nyla finds you, hair mussed, palms inked with peat. She is radiant with small victories and large misgivings."
    show nyla_torres at center:
        zoom 0.7

    nyla_torres "We got provisional language into the press release. It's not ironclad, but it's in the record. The escrow draft is ready. People signed up for oversight."

    maya_serrin "People signed up."
    "Mayor Jerome Hale approaches, his face wind-creased and tired but steadier than in the council room. He clasps your shoulder with a hand that smells faintly of coffee."
    hide aiden_koa
    show mayor_jerome_hale at left:
        zoom 0.7

    mayor_jerome_hale "You carried it, Maya. Those roofs tonight—people are going to sleep differently. Thank you."

    maya_serrin "We did what we had to,"

    mayor_jerome_hale "There's going to be pressure for follow-through. Keep the oversight pressure. Keep it public. If anyone can make that stick, it's you."
    "His look is both instruction and trust — a passing of a quieter, more dangerous responsibility than any tape-cutting."
    # play music "music_placeholder"  # [Music: The percussion tightens to a cliff — all momentum, no resolution]
    # play sound "sfx_placeholder"  # [Sound: A single, prolonged roar of the tide striking the pilings]
    "You watch the seawall and the marsh plugs several kilometers away — separate projects standing in different registers: one immediate and hard, one promised and soft. The town breathes in the light and the dark at once."
    "You feel every choice you didn't make lifting like birds that will return in seasons that may not tolerate them. The town's identity feels negotiated in the press of camera lenses and investment portfolios. The ledger in the tide is restless."
    "You think, sharply, of the paths before you: force the political machine to enshrine enforceable follow-ups, accept the political short-term security and live with the compromises you can live with, or build a civil resistance focused on protecting fishers' rights and local traditions."
    "The muscles in your jaw tighten. Your hands, which have become used to maps and measurements and the drag of soil under your nails, are suddenly the instruments of something bigger — of representation, of who speaks for Saltwood when the microphones have been packed away and the cranes sleep."
    "You feel the weight of the town's trust settle onto your shoulders like a physical load."
    "A tide of obligation and urgency lifts within you, building with each measured breath. You are not paralyzed. You are not content. The next move has to be deliberate and public; it will require strategy, alliances, and sacrifice."
    "A procession of thoughts lines up in your mind like waves approaching a sea wall: legal action, public oversight, civil mobilization. Each is a tool with edges that will cut different things. Each choice will be written, later, next to the house it saved or the song it silenced."
    "The lights on the construction site throw long hard shadows across the quay. You look at Aiden Koa, at Nyla, at the Mayor, at Dr. Elena Park's distant silhouette under the floodlights, and you understand that whatever you do next will not be private."
    "You reach inside your parka and find the tide-watch. Its brass is cool and honest in the dark."
    "You inhale. You let the night gather around a single action like a held breath waiting to be released."
    "You must choose how to carry the promise of 'later' into the reality of tomorrow."
    # [Page-Turn Moment: You lift your chin, feeling the full weight of representation settle into your bones. The quay's lights hiss. The machines drone like a sleeping animal. The decision you make next will not fit neatly into headlines. It will be made of meetings, of hard legal clauses, of the stubborn labor of people who will not be silenced. You take a step forward toward the lights, toward the place where policy meets soil, and the tide watches you decide.]
    hide maya_serrin
    hide nyla_torres
    hide mayor_jerome_hale

    scene bg ch10_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter11
    return
