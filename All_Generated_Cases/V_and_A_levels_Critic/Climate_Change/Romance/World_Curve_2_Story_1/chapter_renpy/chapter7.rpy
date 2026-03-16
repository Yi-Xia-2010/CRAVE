label chapter7:

    # [Scene: Wave Innovation Lab | Morning]

    scene bg ch7_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Tense, pulsing electronics underscored by quickened strings]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the low mechanical hum of the lab, water lapping against stilts]
    "You step into the lab with salt drying on your boots and the coral strap of your camera warm beneath your palm. The air inside is cooler—sterile and humming with stored energy—but the scent of sea"
    "still rides your clothes: a mineral, peppered with the faint sweetness of kelp. Mateo is already there, bent over a bench strewn with sensors and braided wire, his forearms glossed with solder and concentration. He looks"
    "up and, for a second, the edges of the day — the vote, the plaza, the way everyone leaned on you — shrink behind his face."
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "You're on time. Good—there's a tide window in two hours. If we can sync the buoy to the pump, we can show Council a real-read tonight."
    show ari_tanaka at right:
        zoom 0.7

    ari_tanaka "We already told them,' you say, but your voice is tight. 'This is about proving it doesn't just sound good on paper."

    mateo_alvarez "Proof. You, me, and a handful of stubborn circuit boards."
    "Etta's face appears on a monitor, streaming in from the Nursery—her greenhouse glow a soft amber against the lab's blue light. Her grin is small, resolved."
    show etta_hargrove at center:
        zoom 0.7

    etta_hargrove "Cautious trials, remember. I want logs, I want physical markers. If the marsh won't hold, we stop. No heroics."
    "You nod even though she cannot see the motion. Her support is a firm weight at the back of your neck—comforting, but not enough to stop the anxiety that spins under your ribs. Jun loiters by"
    "the open bay door, hands jammed into a damp jacket. He smells of fish and rope and worry."
    hide mateo_alvarez
    show jun_park at left:
        zoom 0.7

    jun_park "You're sure about this, Ari? Tech's one thing—I've seen gadgets before. But if it peters out in a season and the town's counting on it…"

    "Ari Tanaka (breathing in)" "That's why we keep both options live. The marsh work continues. The buoys are a supplement: power for pumps, better sensors. Not a replacement."

    jun_park "That's what we said last week. What happens when the funding hinge collapses and people—"
    "Mateo Alvarez steps between you and the worry, voice low but steady."
    hide ari_tanaka
    show mateo_alvarez at right:
        zoom 0.7

    mateo_alvarez "That's why we're doing this as a community pilot. The Wave Innovation Lab signed the memorandum—no exclusivity, open-source baseline data, and commit to a rollback clause if the tech destabilizes sites."

    "Kira" "Those are preliminary terms. Investors will want results. And 'open-source baseline' doesn't make grant applications look secure."
    "You feel the lab's temperature change; Kira's comment lands like a splinter. Everyone looks at you with different questions: trust me, back us, or say no and watch the town's breathing shorten."
    hide etta_hargrove
    hide jun_park
    hide mateo_alvarez

    scene bg ch7_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A sharp beep as a sensor boots]
    "You swallow the old guilty knot—your tendency to carry other people's safety like a sack of stones on your back—and answer because you must."
    show ari_tanaka at left:
        zoom 0.7

    ari_tanaka "We pilot it. We document every datum Etta requests. Full community oversight. And if the lab wants investors, they come to the Council first."

    "Kira" "Councils slow us down. Investors fund the manufacturing we don't have time to do at scale."
    show mateo_alvarez at right:
        zoom 0.7

    mateo_alvarez "We don't need scale right now. We need legitimacy. Let's prove one buoy can keep a pump running through a simulated high tide."
    show etta_hargrove at center:
        zoom 0.7

    etta_hargrove "And document the impacts on nearby eelgrass. If we harm the marsh in trying to save it, we're none the better."
    "Your chest tightens. The edges of less-than choices press in: speed versus caution, hope versus the real fear of false promises."

    menu:
        "Recommend a conservative test profile — shorter run, tighter monitoring":
            "You suggest cutting the run time and installing extra baselines on the marsh perimeter. Mateo nods, visibly relieved; Kira frowns but agrees. The team adjusts the battery profiles and sensor thresholds, and the buoy's LED steadies."
        "Push for a longer endurance test to impress investors":
            "You propose a longer run to generate headline data. Mateo's face goes still; he meets your eyes and the tension between wanting to prove and wanting to protect hangs between you. Kira brightens—this could attract funding—but Etta says nothing immediately, her silence heavy."

    # --- merge ---
    "Scene continues to the montage and pier work."
    hide ari_tanaka
    hide mateo_alvarez
    hide etta_hargrove

    scene bg ch7_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: Percussion rises, heartbeat-matched]
    "You help carry the buoy to the pier. Salt-spray mists your face; the wind lifts your hair, a small, bright ache in a throat already raw from speaking. The harbor looks the same and unrecognizable: familiar"
    "nets and splashboards, but with new signs of strain—sandbags sullen at doorways, puddled banners where protests met permits."
    show jun_park at left:
        zoom 0.7

    jun_park "If this goes sideways, the fishermen will be the ones with nothing left to sell."
    show ari_tanaka at right:
        zoom 0.7

    ari_tanaka "Then we don't let it go sideways. We watch. We stop. We—"
    "Mateo Alvarez squeezes your shoulder, grounding. His touch says what words cannot: I am here. We are doing this together. The warmth of it hits you like a small, steady flame."
    "At the waterline, the buoy rocks against the cradle like something shy. You lower it, the rope chafing in your palms. The pump on the marsh is tiny but stubborn. You clip sensors along eelgrass beds,"
    "hands working by muscle memory; the coir logs Etta championed look fragile in the swell."
    show etta_hargrove at center:
        zoom 0.7

    etta_hargrove "If the pump holds, we can keep critical seed beds from drowning through the next tidal peak. But this isn't a miracle. It's triage."

    jun_park "Triage doesn't feed forever. It keeps you alive until they move you."
    hide jun_park
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "Then let's make 'until' longer. Let's make 'they' us."

    ari_tanaka "We started with small things that mattered. This is the same idea—applied differently."
    "Jun's jaw tightens. He won't be placated with phrases. He demands results because his family eats what the sea gives. The argument swells, heated; voices rise above gulls, a raw cadence of fear and stubbornness."

    "Kira" "We've got a half-hour before the peak. Power the pump, run a data stream to the monitor, and let's see if the buoy's harvest curve holds."
    "You and Mateo work in sync—your hands and eyes translating between his circuits and the marsh's living math. He leans in, explaining a tweak to flow regulation, the way his breath fogs near your ear. Your chest relaxes oddly at the intimacy of solder and salt and shared panic."
    hide ari_tanaka
    hide etta_hargrove
    hide mateo_alvarez

    scene bg ch7_453e40_4 at full_bg
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "There—see the oscillation dampen. We're pulling enough to keep the pump from stalling."

    "Ari Tanaka (smiles despite the churn)" "It looks good on the feed. Etta—do you copy?"
    show etta_hargrove at right:
        zoom 0.7

    etta_hargrove "I copy. Monitor the seagrass edge. If anything moves beyond micro-shift, you call it and we pull."
    "The buoy keeps running. For a breath, the town exhales with you. But that breath is short-lived. Back in the lab, Kira's phone pings; she reads, her face shifting like weather."

    "Kira" "Investors. They've scheduled a visit for next week. One of their partners—Elio Sato—wants to swing by."
    "Every hair on your body lifts. You know Elio Sato by reputation and the steel of his jaw from past meetings: the data-driven man whose proposals speak in absolute stabilizing statements. He has saved towns and"
    "gutted others, all with the confidence of someone rearranging chess pieces on a wettable board."

    mateo_alvarez "Elio's influence is… complicated. He can bring capital we don't have access to, but he also brings a template. He likes to centralize."
    show jun_park at center:
        zoom 0.7

    jun_park "Centralize means buyouts, checkbooks, and fences."

    "Kira" "They come with strings. He brings investors, not neighbors."
    "You taste copper: fear braided with the memory of displacement. The buoy still hums in the water. The pump ticks in rhythm with your heart. You feel the day folding itself into this moment—small mechanical triumph and the looming shadow of investors who don't instinctively share your definition of 'community'."
    # [Scene: Wave Innovation Lab | Late Night]
    hide mateo_alvarez
    hide etta_hargrove
    hide jun_park

    scene bg ch7_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Low, urgent synth; single violin note repeating like a question]
    # play sound "sfx_placeholder"  # [Sound: Soft clank of tools, the occasional hushed laugh between two people trying to stay sane]
    "The hours condense into work. You and Mateo lie out schematics like a folded map of what could be. He traces an idea with a soldering iron and talks about modular housings for the buoy—simple enough"
    "to be built here, honest enough to be maintained by locals. His voice is small when he says the next thing."
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "If we keep the designs modular and community-built, the lab only needs to supply the parts kit. People maintain. We avoid corporate lock-ins."
    show ari_tanaka at right:
        zoom 0.7

    ari_tanaka "That keeps control local.' Your own voice betrays worry. 'But will investors—"

    mateo_alvarez "They like scale. They like efficiencies. We have to show them a path that gets them numbers without taking the land from the people who need it."

    ari_tanaka "Which means compromises."
    "Mateo Alvarez's hands still. For the first time in a while, he looks tired in a way you haven't seen—his optimism tempered. He turns and finds your face in the blue light."

    mateo_alvarez "I don't want to lose this with you, Ari. If funding asks us to sign away our community oversight, I'm not… I don't know if I can—"

    ari_tanaka "You won't have to decide alone."

    mateo_alvarez "What if we say no? What if we stall? What if they walk and leave us with prototypes and no manufacturing?"

    ari_tanaka "Then we find other routes. Grants, crowdfunding, campus partnerships. We make the prototype compelling enough the town backs it and investors feel the political cost of walking."

    mateo_alvarez "Political cost—sounds so adult."

    ari_tanaka "It's how the world runs now. Money is politics, and storms are votes."
    "He exhales a laugh that is half-anguish. The buoy's LED flicks to green—steady life. Outside, rain begins again, a thin, precise drumming."
    # play sound "sfx_placeholder"  # [Sound: A new message notification, sharp and insistent. Your phone vibrates on the bench.]

    "You read the email; your stomach drops. Kira forwarded the investor itinerary. Elio Sato is listed as "Strategic Partner." The itinerary includes a private demo and a pitch session with local stakeholders. The document carries a tagline" "Acceleration & Integration: Scaling Community Resilience."

    ari_tanaka "He's coming."

    mateo_alvarez "Elio coming is… not the worst. If he sees it working, he might fund deployments. But he also likes solutions that can be 'implemented' at scale—which sometimes means re-zoning, land consolidation."

    ari_tanaka "We need a guarantee: no land covenants, no mandatory buyouts tied to the tech."

    "Kira" "Investors will balk. They want assets, transferable value. They don't invest in nebulous guarantees."
    "Etta, on the screen from the Nursery, interrupts, voice knotted with something like worry and steadier than yours."
    show etta_hargrove at center:
        zoom 0.7

    etta_hargrove "You write conditions now. Don't wait for their charm. If Elio's team sells us a vision, make sure the contract language protects residents. We write the clauses ourselves if we have to."
    "Her steadiness is like a hand gripping the steering wheel of a ship just as a storm forms. You want to trust it. But the night presses: lights, logs, investors, and a man whose smile can close a harbor."
    # [Scene: Pier | Dawn]
    hide mateo_alvarez
    hide ari_tanaka
    hide etta_hargrove

    scene bg ch7_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Edgy strings; tempo quickens]
    # play sound "sfx_placeholder"  # [Sound: Scout-like chatter, a camera shutter, the buoy's throat-thrum]
    show elio_sato at left:
        zoom 0.7

    elio_sato "Ari. Mateo. Impressive setup for a pilot. Shows… ambition. We like ambition."
    "Ari Tanaka (internally): He makes the word sound like an asset."
    show ari_tanaka at right:
        zoom 0.7

    ari_tanaka "Welcome. We're running a controlled trial."

    elio_sato "Of course. Control is good. But what we tend to recommend is accelerated proof: aggregated datasets, quicker rounds, scaled trial sites. With a plan like that, we can bring in manufacturing partners and subsidize distribution."

    "Kira" "Subsidizing distribution often means control clauses. We stipulated community oversight."

    elio_sato "Oversight scales. We can structure community captains in governance. It makes projects fundable and replicable."
    show mateo_alvarez at center:
        zoom 0.7

    mateo_alvarez "Replicable doesn't have to mean replaceable. Governance needs teeth. And residents must be able to opt out of any land agreements."

    elio_sato "Opt-outs complicate scaling. But I understand the sentiment. There are engineered compromises."
    hide elio_sato
    show jun_park at left:
        zoom 0.7

    jun_park "Compromises for you probably mean checkboxes. Compromises for us means leaving the houses behind."
    "Elio Sato turns to Jun with an hourglass patience, as though reading a tide chart."
    hide ari_tanaka
    show elio_sato at right:
        zoom 0.7

    elio_sato "I grew up in a town much like this one. We lost things to the sea. My approach prevented farther loss. I don't like seeing people displaced either."
    "You watch every face for telltale signs—who's bought, who is warier. Elio Sato's cadence is smooth; his data slides are immaculate. He speaks of efficiency, of models and returns, of survivable perimeters. He does not say"
    "buyouts, but he does say 'managed prioritization of space' and 'strategic consolidation'—phrases with soft syllables and hard consequences."

    "Kira" "Let's be explicit. We brought you here so we could see how your approach translates to a community-driven pilot. The terms we want are: no forced relocations tied to our contract, open data, and local manufacturing."

    elio_sato "Those are negotiable. Investors want to know their exposure is limited. That usually means some control clauses."
    "You feel the pitch room compress around you. Every syllable Elio Sato offers implies a fork: resources with strings, or limited means with autonomy. Your chest tightens—guilt, again, for the lives that lean on your shoulders."

    mateo_alvarez "If they push for exclusivity, we walk. We can't sign away oversight."
    hide mateo_alvarez
    show ari_tanaka at center:
        zoom 0.7

    ari_tanaka "And if they walk, we might not scale. We might not keep enough pumps going."
    "The argument ricochets. Etta's voice, through the line, is steady and worn."
    hide jun_park
    show etta_hargrove at left:
        zoom 0.7

    etta_hargrove "Then we write the clauses. We bring Mara to help with public pressure. We bring Councilor Rosa. If investors think there's political cost, they'll listen."
    "Elio Sato smiles like someone who has grown used to having most doors open. The buoy rocks behind him, a small breathing machine in the wide sea. The day is a thin razor between possibilities."

    menu:
        "Tell the lab to insist on legally binding community oversight clauses now":
            "You stand up, voice loud and brittle. Kira bristles at the legal hurdles but nods; Mateo breathes out, relieved. Elio's smile tightens—he didn't expect immediate pushback. The conversation shifts to hostage clauses and legal drafts."
        "Suggest a diplomatic approach — draft soft MOUs first to keep investors engaged":
            "You propose an MOU to keep the investors at the table while the community drafts stronger language. Kira relaxes; Elio's eyes sharpen at the pragmatism. Mateo looks torn, grateful for the breath but fearing the slow leak of meaning in soft words."

    # --- merge ---
    "Scene continues to negotiations and the final moments in the lab."
    # play music "music_placeholder"  # [Music: Crescendo—high, insistent]
    hide elio_sato
    hide ari_tanaka
    hide etta_hargrove

    scene bg ch7_453e40_7 at full_bg
    "You feel a tightening at the base of your skull, all the old decision-weight pressing: the one that taught you to choose for people and feel every consequence as personal fault. The pilot runs, the buoy"
    "hums, and the town watches the same signals you do—hope braided with wariness. Elio Sato's presence changes the geometry of possibility; he brings money and the smell of policy that can be both scaffolding and scaffold"
    "for removal."
    "Kira looks to you and, with a slight lift of her chin, asks the question without words: what do you want this partnership to be? For all the pilot's success, for all the late nights with"
    "Mateo soldering until both your fingers were sore, the next steps will be chosen in rooms filled with power and polite men who like tidy outcomes."
    "Mateo Alvarez's hand finds yours, small in the lab's blue light. His fingers curled around yours feel like an anchor and a challenge. He leans close enough that you can hear his breath; the harbor's noise seems to exhale with you."
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "Whatever we do, I don't want it to make you compromise yourself."
    show ari_tanaka at right:
        zoom 0.7

    ari_tanaka "I don't want to be the reason people lose their homes either."
    "He presses your hand, a brief, urgent contract of tenderness."
    "The buoy's data ticks upward on the monitor—power harvested, pump stability, tidal variance. Numbers climbing or stalling do not weigh the same as the human faces of Tidebridge; those faces flicker behind your eyes. The investor"
    "timeline, Elio Sato's charm, the lab's hunger—all of it converges into a tide you must choose how to ride."
    "You want to yell, to make the whole choice vanish by sheer force. Instead, you breathe and write a list, quietly, the practical and the moral tangled together: clauses, oversight, open data, manufacturing, community captains, legal counsel. It feels like knitting a raft from raindrops."
    hide mateo_alvarez
    hide ari_tanaka

    scene bg ch7_453e40_8 at full_bg
    # play music "music_placeholder"  # [Music: Tense note held; then soft percussion, a page-turning whisper]
    "You look at the contract template on Kira's phone, at Elio Sato's composed face, at Mateo Alvarez's steady hand in yours, at Jun's silent watch. The world narrows to a single question: How much will you give to get the means to keep people here?"
    "You cannot answer it tonight. The pilot must continue. The investors will come. The negotiations begin at first light."
    "You tuck your camera into your tote and step back outside where the harbor's wet air meets your face. Your reflection in the puddles is a bright, uncertain thing—sea-glass eyes rimmed by tiredness. Your chest is a pulsing little drum of decisions not yet made."
    # [Page-Turn Moment]
    "You raise your collar against the drizzle and imagine the contract clauses rearranging the town like tide lines. Somewhere across the water, the marsh waits for protection. Behind you, Mateo's hand tightens. Ahead, the lab's inbox"
    "pings with schedules and promises that might cost more than you have the right to pay."
    "You close your eyes and feel the sea in your bones, the old and stubborn ache that has always asked you for a choice."

    scene bg ch7_453e40_9 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter8
    return
