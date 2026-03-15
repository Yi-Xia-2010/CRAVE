label chapter7:

    # [Scene: Stormwall Construction Site Office | Night]

    scene bg ch7_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Wind rattling the trailer’s siding; distant metallic clang as a crane swings]
    # play music "music_placeholder"  # [Music: Pulsing low strings — urgent, forward-driving]
    "You push the trailer door open and the smell meets you first: wet cement, diesel, the iron of rain. The air is colder inside, as if the trailer holds its breath and waits for whatever you"
    "bring with you. Your field notebook is in the inner pocket of your jacket, its taped corner familiar under your fingers, but you don't pull it out yet. Tonight is for listening; tonight you are meant"
    "to measure words as much as numbers."
    "The steel skeleton of the stormwall looms beyond the trailer's thin window—an articulated silhouette of promises and threats. Its lattice catches the lamp and throws a grid of light across Elias Hart before he rises from"
    "a fold-out chair. He is almost absurdly neat against the construction dust: navy pea coat pressed, brass pocket watch catching the lamp's flare. For a heartbeat his smile is a practiced thing, but his eyes—cool, assessing—hold"
    "a softness that you didn't expect to find in a city man who returns with contracts in his briefcase."
    show elias_hart at left:
        zoom 0.7

    elias_hart "Alea. Thanks for coming on short notice. I know the hour."
    show alea_maren at right:
        zoom 0.7

    alea_maren "You asked to meet privately. I came. I want to hear the plan directly, Elias."
    "Elias lets the door close behind you with an obliging nod. The lamp swings and the shadow of his profile follows like a second thought."

    elias_hart "Direct's easier for everyone. Less room for rumor. We're proposing a scaled barrier—only across the most exposed span. Private capital covers the upfront costs; we source local contractors for the work, and we'll fund an ecological offset program that plants and restores the Dune Gardens. Oversight, measurements, adaptive triggers—I want you to help author them. Give us the credibility we lack out here."
    "You feel something unclench in your chest at the word 'local.' It's a soft, dangerous ease."

    alea_maren "You want me to write the metrics. To sign a name to the thresholds that allow you to pour concrete through our coastline."

    elias_hart "Not to sign: to structure. You know the science better than anyone here, Alea. I can bring capital. You can guarantee—at least in design—that we don't worsen sediment starvation, that we fund long-term monitoring. That matters."
    "He watches you as if reading an equation, waiting to see whether you'll plug in the right variable. The lamp paints a thin crescent of gold across his watch; he taps it once, a small, unconscious"
    "clockwork gesture that seems to say he understands deadlines in a way you know only too well."
    "Internal thought: The numbers line up in your head — stress curves, sediment transport, modeled deposition rates. A scaled wall reduces wave energy where it's built. Downcoast, currents could accelerate erosion."

    alea_maren "Short-term reduction in overtopping doesn't disappear the long-term trend. A wall in one place can starve another of sediment. Lives are saved now, but other livelihoods might collapse later."

    elias_hart "I'm not arguing who's right about physics, Alea. I'm arguing about timing. Policy moves slowly; storms don't. We can patch the town a little more time with this. Use that time to implement nature-based solutions properly. I'm offering both. Private funds now, community projects in parallel. If you help structure the oversight, we can make that binding."
    "There is a cadence to his pitch — urgency in his words that matches the wind beyond the trailer. It warms something dangerous in you: the intoxicating certainty of someone who believes speed can marry rigor."

    alea_maren "Binding is the word everyone likes until binding becomes a loophole. Who writes the penalties? Who enforces them if the offsets underperform? Who sanctions contractors if they cut corners? I've seen 'community projects' used as greenwash in places with fuller pockets than ours."
    "Elias smiles, not dismissive this time, but sincere."

    elias_hart "Then we write penalties. We define performance metrics. We appoint a mixed oversight board—community, independent scientists, and a third-party auditor. You pick the scientists. You choose the community reps. We put the contract in escrow, with clauses triggered by monitoring data."
    "The lamp swings again and a gust slides through the trailer; you smell salt on his coat. Your throat tightens at the thought of authority in escrow—power temporarily tamed but still held by hands that can open clauses and invest differently come morning."

    alea_maren "You say 'we put it in escrow' like you're comfortable handing over strings. Why? What's in it for you besides legacy and votes?"

    elias_hart "I grew up near enough to see towns disappear when decisions are delayed. I'm tired of watching people choose between ruin and hasty fixes. If I can help save Harborstone and avoid the mistakes that hollowed other places, that's enough. The funders want a model that proves concrete and nature-based strategies can coexist. If we pull it off—if we prove it—the model spreads. That's my incentive."
    "Your thought stumbles, not on the math but on the image he paints: a model exported like a curriculum of hope. For a second you imagine scaling solutions beyond Harborstone and the smallness of your early promises. It feels good and unbearable all at once."

    menu:
        "Ask for the auditor's name now":
            "You interrupt, voice clipped; Elias appraises, then offers a firm name—someone with credentials and a city ledger, which you file mentally."
        "Let him continue; observe how he frames incentives":
            "You stay silent, watching the set of his mouth; he expands on funder expectations and timelines, giving away more of his temperament than he intends."

    menu:
        "Ask to see the draft clauses now — press him":
            "You lean in and ask for specifics; Elias fishes a folder from his briefcase and slides a preliminary clause across, its legalese familiar and maddeningly soft where you need steel."
        "Request time to consult Dr. Lian and community reps":
            "You ask for a pause; Elias nods, conceding the prudence, but you can see patience thinning—deadlines press. The lamp stutters as if mirroring that tension."

    menu:
        "Work with Elias to formalize strict oversight and ecological offsets in the stormwall contract.":
            jump chapter8
        "Refuse the private offer; expose the plan publicly and rally the town against external control.":
            jump chapter8
        "Secretly record his assurances and use leverage later; play a political double game.":
            jump chapter14
    return
