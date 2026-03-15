label chapter4:

    # [Scene: Old Market Boardwalk | Late Afternoon — overcast, rain-slicked]

    scene bg ch4_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant pumps thrum; voices swell and recede like small waves; gulls cry]
    # play music "music_placeholder"  # [Music: Low, urgent cello underscoring crowd murmurs]
    "You move through the crowd with your notebook pressed to your chest, the leather warm from your palm. Jonah Reyes's voice threads over the market noise—clear, practiced, hopeful—and people lean toward him as if he's thrown"
    "a buoy. You can see the market's face: Rosa arranging empty crates into a makeshift platform, Mateo wrestling a banner that reads HANDS NOT WALLS, kids holding battery candles that paint their faces gold in the"
    "drizzle."
    "Your boots leave halting splashes on the boardwalk. Salt fog and the smell of fried fish tug at the edges of everything, grounding you in the particularity of this place: the scaffolds, the patched planks, the"
    "murals that remember sun. You are in your element—maps, sensors, elevation points living in your head like a second tide. The notebooks in your jacket are full of plans that read like prayers."
    "Jonah Reyes catches your eye between shouts. His amber gaze is bright, the single silver streak at his temple visible even under the hood of his jacket. He tugs his bandana at his wrist and grins, a small motion of certainty."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "Mara Solano. You're here. Good—look, we've got twice the turn-out from last week. Rosa—talk logistics. Mateo—channels. We need a route to the docks and a small perimeter for the vigil."
    show rosa_and_mateo_market_co_op at right:
        zoom 0.7

    rosa_and_mateo_market_co_op "We'll run the market strike through the north pier. Mateo and I will reroute the vendors. You—' (she points to you, wet hair plastered to her forehead) '—you and Jonah hold the crowd. Make the scientists speak like humans."
    "You force a laugh that tastes like metal. You open your notebook, fingers brushing the tide-mark sketches. Your mind begins plotting lines—where marsh terraces could suck the first pulse of surge, where coir logs should be anchored so volunteers aren't waist-deep if water rises fast."
    "You hand Jonah Reyes a map-smeared sheet. He leans close, shoulder pressing against yours. The physical contact is a current under the words—a warmth that steadies and complicates every calculation."

    jonah_reyes "If we can show them this—not just say it—people will see there's another way. We stunt the development by showing what's possible from the ground up."
    show mara_solano at center:
        zoom 0.7

    mara_solano "We need numbers: absorption rates, volunteer hours, legal protections. If we make it a community project that can actually be built this season, Avi can't ignore it."
    "Jonah Reyes nods, then glances at the line of cordoned-off vendor tables where a small cluster of municipal officers are watching."

    menu:
        "Grab the megaphone and lead the chant":
            "You take the megaphone from Jonah Reyes's hand. Your voice cracks at first, then finds a cadence. The crowd answers—a slow, steady tide of voices that makes your chest ache with belonging."
        "Stay with Jonah and hand him the megaphone":
            "You hand the megaphone to Jonah Reyes. He steadies the chant, eyes sliding to you with a grateful tilt. Together you become the two-pulse rhythm of the crowd."

    # --- merge ---
    "The chant settles and the organizers confirm tonight's plans."

    jonah_reyes "Good. Good. Tonight at the docks—vigil at nine. Strike starts at dawn. Rosa, Mateo—coordinate messages. We do this clean: candles, testimonies, cameras. We make it impossible to present Elena Voss's glossy renderings as the only option."
    hide jonah_reyes
    show rosa_and_mateo_market_co_op at left:
        zoom 0.7

    rosa_and_mateo_market_co_op "Logistics covered. We can seal the north pier for a route, but some vendors need daily income. We'll run a list—who can skip a day, who needs compensation. We've asked the co-op for donated proceeds."

    rosa_and_mateo_market_co_op "And I'll put someone on social—stream the vigil, get testimonials from folks who've lost roofs, boats. Make it feel like the town is speaking as one."

    mara_solano "I'll bring tide-sensor logs and Claire's models. If anyone tries to paint this as sentimental, we'll show the data. Wetland terraces can take the first foot of surge if installed along the flats. If—"
    hide rosa_and_mateo_market_co_op
    hide mara_solano
    hide rosa_and_mateo_market_co_op

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The market's murmur tightens; a radio in a vendor's stall crackles with a distant municipal channel]
    "Your hands are steady but inside they buzz. You feel the scene unspooling: cameras, candlelight, the boats' silhouettes. You can imagine the headlines—your models made human, your grief made policy. And yet a tightness nests under"
    "your ribs: whenever you imagine scale, you also imagine the sudden, sharp thing—an unpredicted surge, an evacuation with too little notice, concrete plans collapsing in rain."
    "A municipal officer approaches, clear rain dripping from the bill of his cap. He speaks into a hand mic, then lifts his gaze to the knot of organizers."

    "Officer" "This is Town VP. Permit requires a safety plan for assemblies near the water during advisories. We need a liaison and a written plan for tonight."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "We have marshaling. We have medics. We can show you a plan—give us an hour."

    "Officer" "Noted. But command's orders: maintain clear egress. If weather advisories escalate, you'll need to disperse."
    "The man's words land like a flat stone. You glance at the sky; the cloudline has teeth this day, purple and low. You pull your jacket tighter."

    menu:
        "Volunteer to be the liaison and file the plan":
            "You step forward, voice steady. You sketch a rapid plan on the back of a flyer and hand it over. The officer nods once—procedural respect, nothing more—but the act roots you in responsibility."
        "Insist Jonah handle it while you secure sensor deployment":
            "You point to a volunteer and outline the sensor deployment in a few clipped sentences. Jonah Reyes nods and intercepts the paperwork. There's urgency in the delegation; you feel oddly exposed handing off control."

    # --- merge ---
    "The paperwork is accepted and preparations continue as officers monitor weather advisories."
    # [Scene: Docks | Night — candlelight and tide]
    hide jonah_reyes

    scene bg ch4_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Water lapping, low chant threads, the occasional clink of glass; distant thunder beginning to roll]
    # play music "music_placeholder"  # [Music: Sparse piano notes, then a low, swelling string that suggests both hope and fragility]
    "The vigil is quieter than the market but more intimate—low lamplight, faces lined and wet. Aunt Pilar stands near the pier's edge with a small lantern, her shawl dyed from decades of sunlight and salt. She"
    "looks smaller tonight, and yet she is the town's memory pinned into motion. You move beside her and for a moment all the policy diagrams dissolve into the simpler arithmetic of names: Maria's roof, Tomas's boat,"
    "the corner house with the blue door where children once left drawings on the stoop."
    show aunt_pilar at left:
        zoom 0.7

    aunt_pilar "They sang your father's song today, mi'ja. He would be proud."
    show mara_solano at right:
        zoom 0.7

    mara_solano "I—' The sentence gets swallowed by the sea air. Pride and the gaping shape of what you couldn't do at sixteen fold over each other. 'We tried to make something that lasts."
    "Aunt Pilar's fingers find yours, steady and callused. The contact is a geometry you know by heart—support, not solutions."
    "Jonah Reyes steps up to the small wooden crate the co-op borrowed as a platform. He speaks not as a planner tonight, but as someone carrying the town's grief and anger and stubbornness."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "We light these candles for people who got promises but not protections. We light them because this is home. We will not be erased."

    "Crowd" "Not erased."
    "You stand at the edge and run a finger along the damp rope railing. The smell of algae, diesel, and the lemon-sour tang of candlewax fold together. The tide pushes in, quietly, with a patience that reads like inevitability."
    "Your watch buzzes—a message from Claire. You read it without wanting to, because Claire's messages carry the weight of models and deadlines."
    hide aunt_pilar
    hide mara_solano
    hide jonah_reyes

    scene bg ch4_453e40_4 at full_bg
    "Your throat goes dry. You are fluent in probabilities, in worst-case sequences. The numbers arrange themselves into a single unwelcome image: excess water finding weak points, marshes not yet planted, volunteers on damp planks that will become slick."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "We have momentum. People are listening. I know you're worried."
    show mara_solano at right:
        zoom 0.7

    mara_solano "I know."
    hide jonah_reyes
    hide mara_solano

    scene bg ch4_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A murmured ripple of anger; camera shutters]
    "The projection is clinical. Elena Voss's face appears in a brief clip—measured, brilliant—promising immediate funds and a 'secure' skyline. A ripple of boos moves through the crowd. Someone shouts that the renderings hide whom the towers"
    "will displace; someone else says we need any funds that mean fewer flooded roofs tonight."
    "A co-op volunteer passes you a folded leaflet—Elena Voss's team has spun tonight into proof the town needs the Spire's 'stabilization.' You look at the glossy paper and feel the world narrow: their certainty of security next to your messy, incremental marsh plan."
    show rosa_and_mateo_market_co_op at left:
        zoom 0.7

    rosa_and_mateo_market_co_op "They're painting us reckless. It's working on the feeds."
    show rosa_and_mateo_market_co_op at right:
        zoom 0.7

    rosa_and_mateo_market_co_op "Then we give them the feed of real people. Jonah Reyes—get someone to tell the cameras about the houses on Crescent Lane. Those are ones Elena Voss's renderings won't dry."
    "Your mouth is dry, your hands ink-smudged. The vigil edges toward being a battleground of narratives."
    # play sound "sfx_placeholder"  # [Sound: Sirens faint, then closer]
    hide rosa_and_mateo_market_co_op
    hide rosa_and_mateo_market_co_op

    scene bg ch4_453e40_6 at full_bg

    "Officer 2" "Public safety command has issued a clearance order for dockside gatherings. You have thirty minutes to disperse this area or we will start enforced evacuation."
    "A low, stunned silence. Candles tremble in the sudden numbing of sound, and in that silence you hear, sharp and small, the sound of your own pulse."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "They're clearing us now? In the middle of the vigil?"

    "Officer 2" "Weather advisories are being updated. This is to ensure clear egress in case conditions worsen."
    "You think of the houses in your notebook—the ones you annotated for emergency anchoring. You imagine Aunt Pilar's neighbors, the little cul-de-sac with the low seawall you once thought could be shored if volunteers were mobilized fast enough."
    "Your decision reflex—plan first, mobilize later—warriors you won't abandon—boots onto planks—scrapes against the newly stated reality: visibility invites attention, sometimes the kind that breaks what little shelter you had."
    # [Scene: Docks — Later that night into early morning — thunder gathers]
    # play music "music_placeholder"  # [Music: Dissonant strings; wind instruments mimic rising wind]
    "Despite the officers' threats, the vigil disperses slowly. Some leave to higher ground, others linger, unwilling or unable to go. You help bundle candles into boxes, hug who you can. Jonah Reyes moves through the crowd like a tether, steadying people's panic with plan-talk and reassurances."
    "You spend the small hours checking the tide-sensor network you've helped deploy—the little nodes blinking dutifully on your tablet. The data stream is a comfort and a threat: rising lines, modified probabilities."
    "You feel fatigue wrapping its hands around your shoulders in a cold, familiar way. You do not imagine sleep."
    # play sound "sfx_placeholder"  # [Sound: A distant roar grows—the kind of continuous, oceanic noise that makes your bones hum]
    hide jonah_reyes

    scene bg ch4_453e40_7 at full_bg
    "Your stomach drops. The alert points to a poorly defended cul-de-sac—Crescent Lane—small homes, a faded blue door you know by heart. The location is one you circled in ink weeks ago with an anxious hand."
    "You run, boots slapping through puddled streets, Jonah Reyes beside you. People gather in clusters, shouting names, pointing. The air is electric with disbelief and the raw, animal panic of near loss."
    "You arrive to see water where there should be stoops—an angry, unannounced tide pushing through a gap in a hastily installed sandbag wall. The water moves with terrible, patient efficiency: mattresses float like sad boats, a"
    "child's toy drifts past a mailbox, and a woman wades chest-deep holding a photograph above her head."
    "Aunt Pilar is there, face set like flint, calling to someone in a voice that refuses to quaver. Her hands work with practiced efficiency, tying tarps, yelling instructions."
    show aunt_pilar at left:
        zoom 0.7

    aunt_pilar "Move the fridges! Mateo—get the generator! Mara Solano, the south anchor—now!"
    "The names are an acid test. The world has shrunk to the narrow corridor of what can be saved in ten minutes."
    "You are overwhelmed. You can taste salt and diesel and the copper tang of panic at the back of your throat. Your notebook is weightless in your pocket, pages fluttering like small flags."
    "You rush to where the breach seems weakest and throw your weight into shoving more sandbags. Water seeps over the edges, finding the smallest surrender. Your palms sting where rope burns into skin. Jonah Reyes is"
    "beside you, sleeves rolled, shouting encouragements and the exact text of a volunteer protocol in one breath."
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "We can—if we reinforce that corner, the current will slow. Push—push—"
    "You push until your arms ache, until the cold is a second skin. But the water is insistent. It moves under the improvised defenses and takes what it finds: a dented mailbox, the front steps of"
    "a house with the blue door. Someone croons a prayer. Someone curses a name you already hate."
    "The damage is not apocalyptic in cinematic terms, but it is intimate—doorways filled, a porch weeping furniture. It's exactly the heartbreak of your notebook sketches becoming reality. The neighbors you marked as 'at risk' are now wet and stunned and staring at the cross-section of your calculations and your failure."
    "You sit on a soaked curb and let your head drop to your knees. There is a hush you have not earned; the town's breath held."
    "Rosa kneels beside you, rainwater dripping from her braid. She covers one of your ink-smudged hands with both of hers."
    show rosa_and_mateo_market_co_op at center:
        zoom 0.7

    rosa_and_mateo_market_co_op "We did what we could. People held their own. But—"
    hide aunt_pilar
    show rosa_and_mateo_market_co_op at left:
        zoom 0.7

    rosa_and_mateo_market_co_op "We're visible. They saw us tonight. Elena Voss's team will have a meme ready by morning. They'll say we dragged people into danger."
    "You think of Elena Voss's projection, the clean surfaces and promises. You think of the PR clip that already wants to reduce tonight's vigil to recklessness. You taste bile."
    "You are loud and visible and perhaps unprepared for the speed of extremes. The community's spirit holds—so far—but the flood has shown a fault line you can't ignore. Your stubbornness, which has been a kind of compass, feels tonight like a nail you're hammering into your own palm."
    "Jonah Reyes sits beside you, silent, salt trailing down his cheek where a tear fought through the rain. His hand finds yours and holds on without speech."

    jonah_reyes "We escalate. We push harder—more volunteers, more media, blockade the permits. We make them see there's another way."
    "You look up at him. The edges of his resolve illuminate the corners of your own: escalation seems like agency. It also tastes like risk."
    "Your mind races through consequences—legal trouble, forced dispersals, volunteers in danger if weather turns faster, the thin rope between protest and protection fraying. You imagine Elena Voss's lawyers smiling in boardrooms as she frames the movement as irresponsibility against her 'secure' project."
    "You feel the old, familiar ache of responsibility—of being the one who knows the numbers and carries the guilt when numbers become bodies."
    "You do not yet say yes. You do not yet say no. You watch the water darken, collecting small debris like a ledger of things that cannot be righted this instant."
    hide jonah_reyes
    hide rosa_and_mateo_market_co_op
    hide rosa_and_mateo_market_co_op

    scene bg ch4_453e40_8 at full_bg
    # play music "music_placeholder"  # [Music: Single, sustained cello note that fractures into silence]
    # [PAGE-TURN MOMENT: The wind carries salt and the echo of the market's chant. Jonah Reyes's hand tightens around yours—a plea that is also a plan. The lights on your tablet show incoming reports, the breach marked bright and ugly. You feel the old compass—duty, history, the weight of promises—and the pull toward escalation that could save more but might also endanger the very people you vowed to protect. Your lungs fill with cold air. The town waits for your next move. You open your mouth to answer and the words fall somewhere between fury and calculation.]

    scene bg ch4_453e40_9 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
