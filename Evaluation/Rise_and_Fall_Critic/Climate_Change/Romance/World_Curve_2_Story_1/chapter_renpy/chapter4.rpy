label chapter4:

    # [Scene: Tideworks Lab | Early Morning — after a gray night]

    scene bg ch4_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft drip of water, the low hum of a desalination rig, distant gulls turning in a tired wind.]
    # play music "music_placeholder"  # [Music: Sparse piano, a descending motif — restrained, unresolved]
    "You step through the lab’s corrugated door and the air hits you: salt on a diesel tang, the sweet clean smell of crushed kelp, and the faint antiseptic note of ethanol where Theo has been sterilizing"
    "sample jars. Your boots leave damp prints on the ramp. For a breath — a ridiculously small, human breath — you let yourself register the tanks lit like shallow pools of a different sky."
    "The first trials you greenlit months ago are small enough to fit in these containers. The living modules — seeded mats of oyster, kelp, and engineered seagrass — pulse in their tanks, and at low tide"
    "you can already see the change in the nearby bay: calmer eddies, a few fewer frothing arcs of wave against the breakwater. It’s enough to make the co-op grin and then go quiet because you all"
    "know how quickly 'enough' can dissolve."
    show theo_mendes at left:
        zoom 0.7

    theo_mendes "First week numbers are holding. The modules cut the wave energy by— what's the term—peak-to-trough—by nearly fifteen percent in the inner cove. It's not dramatic, but it's measurable. And the juvenile fish counts spiked near the mats."
    "He grins, then sobers. 'We should be proud.'"
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "Fifteen percent is fifteen percent more of the harbor that won't rip off a dock line. It's lives, Theo. Not numbers."

    theo_mendes "Numbers are stories, Mara. We're just learning how to read the sentences."
    "Elias Navin stands at the back, palms tucked into his parka pockets, watching the tanks as if he expects them to explain themselves. His wristband pulses a steady, slow green — an old comfort. He doesn't"
    "look at you first; he looks at the sensors, at the way the data curves, precise and patient."
    show elias_navin at center:
        zoom 0.7

    elias_navin "We're seeing meaningful ecological feedback sooner than modelled. The modules are recruiting bivalves faster than the first simulations predicted. It could mean faster structural accretion, less time before we see real wave dampening at scale."
    "He shifts. 'But that's local. We haven't tested the strain of a storm surge across a continuous line.'"
    "You sense urgency settling in him like a spring coil. It's not the impossibly calm scientist you met at the council months ago — it's the same man, but the data has been talking, and sometimes data sounds like a countdown."

    mara_kestrel "We take it bay by bay. We scale with the coast's memory, not against it."

    elias_navin "I agree, in principle. But the time horizon we have and the city's funding window don't line up. What happens if Jun Park's wall gets prioritized with municipal money because the co-op looks slow? We lose leverage, not just shoreline. We lose the people who stay because there's no support."
    "A tightness forms in your chest — not new, but deeper by degrees. You think of the ledger again: people listed not as pixels but as names. The ledger looks back at you, hungry for entries."
    "Rosa's soft steps at your shoulder are a balm and also a needle."
    hide theo_mendes
    show rosa_alvarez at left:
        zoom 0.7

    rosa_alvarez "You have momentum. Do not let men in suits make it into a sprint that robs people of their say."
    "Her voice is steady, salted with years of knowing what haste costs. Even so, the lab's warmth can't entirely erase the chill that flutters across your shoulders."

    menu:
        "Invite the funders to observe the next deployment with the community present":
            "You decide on transparency. If they're serious, they'll meet our people — not just their spreadsheets."
        "Take the funders' offer for a closed demonstration aboard the trawler":
            "A private demo could secure rapid funds. It's tempting; you feel the pull of every stalled bolt and weather-worn plank."

    # --- merge ---
    "Theo watches you after you choose (his expression small and careful). He flips a tool in his hands like a quiet metronome."
    hide mara_kestrel
    show theo_mendes at right:
        zoom 0.7

    theo_mendes "Whatever you pick, we should document everything. The sensors, the deployment sequence, consent forms signed by those living near the sites. We can't hand them a narrative built from silence."
    "You nod. The lab feels smaller suddenly, tight as a throat. Success has teeth; it draws predators."
    # [Scene: Strand | Noon — sunlight sifting through gray clouds]
    hide elias_navin
    hide rosa_alvarez
    hide theo_mendes

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Timber creaking under foot, low chatter, the greasy slap of ocean against pilings.]
    # play music "music_placeholder"  # [Music: Low strings, persistent but restrained]
    "You walk the Strand with the map slung over your shoulder. Ivy meets you halfway — paint on her hands, a smudge on her cheek. She smells like crushed basil and sun, and for a beat you want to reach for the easy, sisterly comfort of dinner and jokes."
    show ivy_kestrel at left:
        zoom 0.7

    ivy_kestrel "You look like you could use coffee and not the kind the same office gives you with forced smiles."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "I need coffee and patience in equal measure. Preferably more patience."

    ivy_kestrel "Then take my thermos."
    "She hands it over, insistently. 'Also — people here asked that we try the southern inlet next. The elders think the mats would help the mussel beds recover. They want to be part of it.'"
    "You look at the faces gathered: fishermen with weathered knuckles, a mother with a toddler asleep at her breast, a teenager balancing a skateboard and a petition."

    mara_kestrel "We need them to be part of it. We can't do this to them."
    "Rosa arrives, sleeves rolled, eyes both tired and unblinking. She talks to the group in the low, authoritative voice that silences the rustle of worry."
    show rosa_alvarez at center:
        zoom 0.7

    rosa_alvarez "The modules are small now. We scale them, yes — but we scale with knowledge, not with a grant's promise. Grants come with strings. Remember the salt of your grandfather's linings; don't let it be rewoven into someone else's banner."
    "Her look lands on you like a lit candle. The warning is not against funds themselves but against haste that leaves questions unanswered. You swallow."

    menu:
        "Promise a full community meeting before any private funding is accepted":
            "This is how you keep the ledger human — by letting the people write themselves into it."
        "Tell Rosa you'll consult the co-op leaders but keep options open":
            "Too much compromise smells like surrender, but you understand politics enough to know absolute refusals can mean zero support."

    # --- merge ---
    "Your internal monologue churns. Trust is a fragile currency here — who holds it, who spends it, who is left bankrupt. Choosing a route feels like filing a claim you might not be able to cash."
    # [Scene: Rusted Trawler / Deployment Hold | Late Afternoon — overcast]
    hide ivy_kestrel
    hide mara_kestrel
    hide rosa_alvarez

    scene bg ch4_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The metallic thud of crates, a far-off engine, a gull's mournful cry.]
    # play music "music_placeholder"  # [Music: Low, dissonant cello notes; tension tightening]
    "You stand in the hold while Elias Navin talks to two people who do not belong to your town: private funders. They wear the neutral, flattering colors of modern philanthropy — slate and subdued teal —"
    "their jackets unbruised by seawater. One holds a tablet and scrolls through a proposal that is elegant as a trap."
    "Elias Navin's posture changes subtly when they speak with numbers that promise speed. He becomes less a man of careful data and more a translator of possibility."

    "Funder 1" "Our foundation is impressed. We've modeled a phased deployment and can underwrite it at scale if you can guarantee a thirty-percent improvement within the first season."

    "Funder 2" "We'd fast-track manufacturing, logistics hubs, the whole chain. Imagine Corvena as a model city in a year."
    "Elias Navin turns to you, and for the first time in a long while, you see the strain under his restraint: the scientist who lost someone when a test went wrong now burning to avert future loss by moving faster than usual."
    show elias_navin at left:
        zoom 0.7

    elias_navin "If we mobilize across multiple bays concurrently, we can seed the breakwaters before the next high-energy season. The probability of recruiting reef-forming organisms at a city scale increases exponentially with coverage. It's an all-or-incremental question. We could save more sooner."
    "You feel the room shrink around the word 'sooner.' It is the siren song of every person who has watched a storm approach: faster can feel like salvation."
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "Exponential is a dangerous promise when you're missing variables. Who pays if something fails? Who takes responsibility? Your models assume perfect conditions, Elias. The sea does not work from a spreadsheet."

    elias_navin "True, the models are simplifications. But waiting for guaranteed imperfection is another form of harm. We have a window. Funding dries up. Contractors get hired by Jun Park for the wall, and then our approach becomes the footnote in someone else's victory."

    "Funder 1 (interjecting)" "All funding comes with oversight. We require operational control in the first deployment phase. We'll place our engineers alongside your teams to ensure protocol fidelity."
    "You feel the word 'control' like a cool hand on your throat. The private funders' control could knit good outcomes — or fold community agency into a contract clause that prioritizes scale over consent."
    "Rosa crosses her arms, the shawls shifting with a soft rustle."
    show rosa_alvarez at center:
        zoom 0.7

    rosa_alvarez "We don't hand our shore to a ledger with someone else's seal."

    elias_navin "Rosa, I know what that sounds like. I know what handing power over can mean. But I'm tired of losing to inaction."

    rosa_alvarez "And I am tired of losing to haste. There is a difference between action and a trap disguised as rescue."
    "You sense something fraying in Elias Navin, a wire misaligned. He looks older in that instant — not because of time, but because of the wear of choices stacked upon choices."
    "Theo clears his throat, which sounds oddly comic until you realize he's steadying himself."
    hide elias_navin
    show theo_mendes at left:
        zoom 0.7

    theo_mendes "Technically, we could run a parallel process: a community-governed deployment in a few coves, and an accelerated pilot under strict oversight. But two things, one — the staff for that is doubled; two — we risk outcome contamination. If the fast pilot fails, public trust fails with it."
    hide mara_kestrel
    show elias_navin at right:
        zoom 0.7

    elias_navin "Or if the fast pilot succeeds, it gives us leverage to expand community labs with actual results."
    "You stand between the ledger and the sea again, feeling the old ache in your ribs. Funding precarious. If you say no, trench lines harden and the municipal wall gets priority. If you say yes, you"
    "may cede control to people whose interest is scale and visibility — not the slow, human work of rebuilding livelihoods."

    menu:
        "Ask the funders to sign a public accountability clause — community oversight, legal recourse":
            "You try to tether speed to justice. It's a hedge; it may not be enough, but it gives you a paper trail."
        "Request more time to run an independent risk assessment before committing":
            "You bet on caution. It might slow everything down — but it preserves the co-op's agency."

    # --- merge ---
    "Elias Navin's jaw tightens. He looks at you like someone balancing a fragile object with both hands."

    elias_navin "We don't have much time. A risk assessment could take months. The funding window might close."
    hide rosa_alvarez
    show mara_kestrel at center:
        zoom 0.7

    mara_kestrel "And reckless speed could close off community consent indefinitely."
    "He exhales, the sound a small surrender."

    elias_navin "Mara. I'm asking you to choose between a safer slow path — which may be overtaken by other actors — and a rapid deployment that could protect thousands sooner. I can't — I won't watch another season of people losing their homes."
    "His voice breaks on the last words like a rope fraying. The scientist who hides feelings behind models is letting his fear show. You see the mentor he lost reflected in the way he doesn't want"
    "to make the same mistake again, and you understand why he's leaning into boldness now."
    "You search for words that balance ledger and salt, for a sentence that keeps both hope and caution alive. You find no perfect language. Only this: the terrible economy of choices."
    # [Scene: The Basin | Dusk — after a light rain]
    hide theo_mendes
    hide elias_navin
    hide mara_kestrel

    scene bg ch4_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind through young mangrove leaves, soft laughter cut by worried silences.]
    # play music "music_placeholder"  # [Music: A violin phrase that climbs then dips, unresolved]
    "The initial installations along the Basin look like stitched skin on a wound — imperfect but healing. Kids poke at the edges of mats; an old fisher smiles at a juvenile crab finding a new niche."
    "The co-op's success is tangible: a dock that didn't rip away in last week's swell; a few saved nets."
    "But in the glow of the small wins, the debate from the trawler follows you like an undertow. You see the faces of those who would be moved if a large deployment goes wrong. You imagine silent leases, displaced memories. The ledger could protect some but erase others."
    "Ivy comes up behind you and leans into your shoulder."
    show ivy_kestrel at left:
        zoom 0.7

    ivy_kestrel "What will you do?"
    show mara_kestrel at right:
        zoom 0.7

    mara_kestrel "I don't know yet. I hear both sides. I'm trying to make sure whatever we do, people don't become an afterthought."
    "Rosa squeezes your hand in a way that is both comfort and admonition."
    show rosa_alvarez at center:
        zoom 0.7

    rosa_alvarez "Remember — the shore remembers us. We don't write over those who kept it."
    "Silence settles, a low tide. The good in the day feels like a ring in a tree: it tells you there was life, and there might be more. The bad feels like a crack in the same ring."
    "Elias Navin approaches, shoulders heavy. He has a folded proposal printed — dense, quick, and for the first time you see the human urgency translated into policy."
    hide ivy_kestrel
    show elias_navin at left:
        zoom 0.7

    elias_navin "They offered full funding, deployment support, and logistic capacity for a city-wide phased rollout starting next month. They want our commitment now."
    "You look at the paper and feel the list of choices tighten in your chest. The room between 'now' and 'later' is small, but it holds the shape of many people's futures."

    elias_navin "Mara, will you sign us on? I can't do this without you."
    "You hear more than the plea — you hear the memory of loss in his voice, the need to prevent another. You also hear the possibility of handing away community control."
    "Your internal ledger catalogs costs: the immediate mitigation of risk versus the slow erosion of agency. Your salt-touched heart weighs them with a stubbornness that sometimes looks like stubborn refusal and sometimes like refusal to abandon anyone."
    "You are at the crossroads again — only now, the road is wet with the tide."
    hide mara_kestrel
    hide rosa_alvarez
    hide elias_navin

    scene bg ch4_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: A single, low piano note that does not resolve.]
    "Page-Turn: The proposal is on the table and Elias Navin has asked you to stand with him for a widescale, fast deployment funded by private money. The co-op waits; the city watches; the sea keeps moving"
    "whether you decide or not. You can feel how the ledger will read this decision in years to come. The next sentence you speak will angle the tide."

    scene bg ch4_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
