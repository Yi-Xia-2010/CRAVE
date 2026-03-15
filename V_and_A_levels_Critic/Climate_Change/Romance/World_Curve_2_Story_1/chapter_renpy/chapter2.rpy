label chapter2:

    # [Scene: Municipal Plaza | Morning — Overcast with a light drizzle]

    scene bg ch2_c4ca42_1 at full_bg
    # play music "music_placeholder"  # [Music: Quiet, steady piano — mid-tempo]
    # play sound "sfx_placeholder"  # [Sound: Soft patter of drizzle, distant gull calls, murmur of gathering voices]
    "You stand on the top step, camera against your chest the way you always do when you want facts to look human. Mateo's hand is still warm where it found yours; the memory of it is"
    "a small, steady thing under your ribs. Around you, the plaza smells of damp paper and fresh coffee from a vendor's van two blocks over. The town's faces are grayed by weather but not expressionless—there's a"
    "clarity here, like light through a wet window."
    "Etta arrives before the councilors. She moves with careful purpose, a basket of labeled seedlings tucked beneath her arm. Her aprons are flecked with peat; when she smiles it crinkles the skin around her eyes, and the smile carries a kind of history—years of tides watched and small victories remembered."
    show etta_hargrove at left:
        zoom 0.7

    etta_hargrove "Ari. You'll make them see the marsh, won't you? Make them hear it."
    show ari_tanaka at right:
        zoom 0.7

    ari_tanaka "I'll try. I have the sensor logs and the photos. The eelgrass transplant map, too."

    etta_hargrove "Good. Folks need to know this is repairable pain, not inevitable loss."
    hide etta_hargrove
    hide ari_tanaka

    scene bg ch2_c4ca42_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A camera shutter clicks as you test a frame, quiet and respectful]
    "Mateo Alvarez appears beside you with a thermos and a compact sensor in hand, the device blinking an apologetic amber. He offers you the thermos without looking at your face—practical, patient. His satchel smells faintly of sea and solder."
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "The buoy array's telemetry had a hiccup; I swapped the connection and recalibrated the sensor. It should be stable. If it flutters again, I'm bringing you one in hand."
    show ari_tanaka at right:
        zoom 0.7

    ari_tanaka "You fix things the way Etta grows them. Both feel like miracles."

    mateo_alvarez "I prefer predictable miracles."

    menu:
        "Adjust your camera's lens":
            "You kneel, wiping salt spray from the lens and composing a wide shot of the plaza—crowds, banners, the thin line of sea on the horizon. It steadies your hands."
        "Take a slow sip of coffee":
            "The coffee is bitter and honest. It warms the space between your ribs and buys you three calm breaths."

    # --- merge ---
    "Continue"
    # [Scene: Municipal Hall — Entrance / Lobby | Moments later]
    hide mateo_alvarez
    hide ari_tanaka

    scene bg ch2_c4ca42_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Echo of shoes on the tiled floor; a council clerk whispers to a volunteer]
    # play music "music_placeholder"  # [Music: Piano continues; light string underscoring]
    "You step into the council chamber with your notes folded in your pocket. The room is familiar—long table, tall windows arched into the gray sky, microphones like small islands along varnished wood. Councilor Rosa sits at"
    "the head, fingers steepled, her shawl a muted ochre against the chair's leather. Her expression is cautious in a way that feels like a hinge."
    show councilor_rosa_menendez at left:
        zoom 0.7

    councilor_rosa_menendez "We'll begin in five. Public comment will be two minutes per speaker. Please, keep remarks focused and civil."
    "Mara waves at you from the press bench, her recorder already running. She nods—no theatrics, just the clean, attentive look of someone who will make what happens matter later."
    show mara_chen at right:
        zoom 0.7

    mara_chen "Ari—I'll need a quick rundown after, for context. We won't frame anything without your notes."
    show ari_tanaka at center:
        zoom 0.7

    ari_tanaka "I'll be here. The sensor logs are in the packet. And the photos."
    hide councilor_rosa_menendez
    hide mara_chen
    hide ari_tanaka

    scene bg ch2_c4ca42_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A low, anticipatory hum grows as seats fill]
    "Jun arrives with the kind of stoicism you know is brittle under worry. He wipes his palms on a rag like a ritual and takes a seat near the back. When he catches your eye, it's an entire sentence: his boat, his nets, the seasons going strange."
    show jun_park at left:
        zoom 0.7

    jun_park "If they move the waterfront, Ari—who's going to fish the channels? Who's going to buy what we catch?"
    show ari_tanaka at right:
        zoom 0.7

    ari_tanaka "We'll say that. You'll have the floor if you want it."

    jun_park "You know me—I'll speak before I can think."
    # [Scene: Council Chamber | Meeting Begins]
    hide jun_park
    hide ari_tanaka

    scene bg ch2_c4ca42_5 at full_bg
    # play music "music_placeholder"  # [Music: Piano eases back to a single held chord to let dialogue breathe]
    # play sound "sfx_placeholder"  # [Sound: Shuffling papers, murmurs taper]
    show councilor_rosa_menendez at left:
        zoom 0.7

    councilor_rosa_menendez "We'll hear three presentations. First, Etta Hargrove on ecological restoration. Then Mateo Alvarez on hybrid buoy systems. Finally, Elio Sato on the proposed centralized barrier and managed relocation plan."
    "Etta stands first, moving with the slow, earnest cadence of someone used to teaching. She places a tray of tiny pots on the table; each holds a tuft of marsh grass clinging to a pale clod of mud."
    show etta_hargrove at right:
        zoom 0.7

    etta_hargrove "These are not props. They're evidence. Living shorelines—coir logs, eelgrass beds, community plantings—slow the water, build substrate, and keep neighbors where they belong. It's labor we teach and inherit. It's not fast or flashy, but it's durable and humane."

    councilor_rosa_menendez "And the timeline?"

    etta_hargrove "Seasons. It will take years, but if we start now, we will save property, fisheries, and the memories tied to them. We need modest funding and sustained municipal commitment."
    "A murmur of approval and skepticism travels like wind through the room. Hands rise. You watch faces as Etta speaks—the older ones remembering a time of higher marsh, the younger ones measuring immediacy against patience."
    "Mateo Alvarez steps forward with a click of his laptop and a schematic that glows blue on the panel behind him: small modular buoys, wave energy converters tethered to low-profile pumps. His voice is steady, practiced."
    show mateo_alvarez at center:
        zoom 0.7

    mateo_alvarez "We can hybridize—living shorelines where they are strongest, buoy arrays where the energy is needed. The buoys will power pumps to manage salinity and keep low blocks dry during high tides. They can be community-owned and scaled in phases."
    "You watch him hand a page to Mara, who scans it, fingers dancing with the rhythm of a story forming."
    hide councilor_rosa_menendez
    show mara_chen at left:
        zoom 0.7

    mara_chen "Who would own the buoys? The town? A cooperative? What's the maintenance model?"

    mateo_alvarez "Community cooperative, ideally. Low-cost parts, local technicians. We design for easy repair—Jun, you'd be able to fix these."
    hide etta_hargrove
    show jun_park at right:
        zoom 0.7

    jun_park "I'll fix anything that helps me fish and doesn't come with suit-and-tie men telling me to move."

    mateo_alvarez "No suits. Maybe a lot of salt and a spare screwdriver."
    "The room relaxes around that exchange; a few anxious smiles, a shared joke as tension re-forms into focus."

    menu:
        "Clarify the cooperative model aloud":
            "You raise your hand and ask for specifics about governance—what legal structure, who holds the liabilities. Mateo answers in patient detail, sketching out a phased roll-out and a plan for local training, and the chamber leans forward."
        "Hold that question and save it for councilor follow-up":
            "You tuck the question away and let Mateo finish his schematic. It keeps the presentation moving and gives you a chance to record the slide sequence cleanly."

    # --- merge ---
    "Continue"
    # [Scene: Council Chamber | Elio's Presentation — Midpoint of the Meeting]
    hide mateo_alvarez
    hide mara_chen
    hide jun_park

    scene bg ch2_c4ca42_6 at full_bg
    # play music "music_placeholder"  # [Music: A restrained, even low-register cello underlies the words]
    # play sound "sfx_placeholder"  # [Sound: The room's air seems to hold its breath]
    "Elio Sato's presence is different—precise, practiced. He speaks with the crisp certainty of someone who has run models and optimized outcomes. His tablet blinks live data on projected storm frequencies and cost-benefit curves."
    show elio_sato at left:
        zoom 0.7

    elio_sato "We are facing acceleration. Large-scale engineered barriers—modular surge gates, reinforced seawalls—can reduce immediate risk to critical infrastructure. Paired with strategic managed relocation, we can save lives and key economic functions."
    show etta_hargrove at right:
        zoom 0.7

    etta_hargrove "Managed relocation—force people to leave—can't be the first line. It tears at community fabric."

    elio_sato "I don't propose force as a first choice. I propose triage. We prioritize saving as many people and assets as we can while planning humane transitions where necessary. The models are brutal because they are honest."
    "There is a beat, and in it you sense the room shifting. Honesty and brutality hang in different corners; some faces nod, relieved by a clear plan; others tighten at the word 'relocation.'"
    show jun_park at center:
        zoom 0.7

    jun_park "Triage? Who decides what 'assets' are more worthy than my livelihood?"

    elio_sato "No one decides without public process. But we must be frank—some low-lying blocks will be more costly to defend. That does not mean we abandon everyone. It means planning with data to avoid sudden catastrophe."
    "Mara leans into her recorder, voice edged with the journalist's scalpel."
    hide elio_sato
    show mara_chen at left:
        zoom 0.7

    mara_chen "Can you publish the relocation criteria? The public needs transparency—what metrics, whose values inform those thresholds?"
    hide etta_hargrove
    show elio_sato at right:
        zoom 0.7

    elio_sato "The criteria are under development, but I can provide the models and the sensitivity analyses. I want your input."
    "His words are measured; the offer is procedural. They land differently across the room. Councilor Rosa's jaw tightens as she flips through the packet that now includes both mud and algorithms."
    # play sound "sfx_placeholder"  # [Sound: A cellphone vibrates—politely silenced; somewhere in the back someone clears their throat]
    "You add your notes to the record, fingers pressing into paper. The meeting's rhythm is a tide: push of argument, retreat into questions, another swell. Your chest is neither full of hope nor dread—it's occupied, attentive."
    "Neutral does not mean passive; it means you catalog the facts and let them weigh."
    hide jun_park
    show etta_hargrove at center:
        zoom 0.7

    etta_hargrove "People need to stay if they choose to. The marsh works to keep them safe, but only if we don't treat the sea like a problem to be walled off from memory."

    elio_sato "Memory won't keep people dry."
    hide mara_chen
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "Both approaches carry costs. We can design safeguards that buy time for marshes to regrow while we deploy modular tech that keeps pumps running in high tide. It's not either/or."
    hide elio_sato
    show councilor_rosa_menendez at right:
        zoom 0.7

    councilor_rosa_menendez "The council cannot make decisions from sentiment, but neither can it ignore the human cost. We will take these presentations and—"
    # play sound "sfx_placeholder"  # [Sound: A sharp murmur, then a ripple of raised hands; a timer starts ticking for public comment]
    "You step to the microphone when Jun is called. The chamber's acoustics catch your breath and make it seem larger, more exposed."
    hide etta_hargrove
    show ari_tanaka at center:
        zoom 0.7

    ari_tanaka "My name is Ari Tanaka. I grew up in Tidebridge. I've mapped the salt intrusion over the last five years. What I want to ask is simple: can the council commit to a hybrid funding stream that protects infrastructure and supports community-led restoration so people are not forced to choose between their homes and their futures?"

    councilor_rosa_menendez "That's the sort of question we will take to committee."

    menu:
        "Push for a public timeline now":
            "You press for a public timeline—what 'committee' means, when residents can expect decisions. Rosa assures you of a preliminary timeline within weeks, which quiets some anxiety but raises skepticism from others who want more immediate guarantees."
        "Accept the committee answer and ask about interim protections":
            "You ask about immediate, temporary protections—sandbag funding, emergency pumps, volunteer brigades. Rosa nods and the room begins to sketch the first steps that could be taken before any long-term plan."

    # --- merge ---
    "Continue"
    # [Scene: Council Chamber — Closing Exchange]
    hide mateo_alvarez
    hide councilor_rosa_menendez
    hide ari_tanaka

    scene bg ch2_c4ca42_7 at full_bg
    # play music "music_placeholder"  # [Music: A single piano motif reiterates; tempo steady]
    # play sound "sfx_placeholder"  # [Sound: Papers being gathered, chairs creak as bodies shift]
    "As the meeting winds, small kindnesses perforate the formalities. Mateo bends to tighten a loose sensor behind a table, fingers sure and gentle; a volunteer hands him a screw and he accepts it with a grateful"
    "grin. Etta chats quietly with an elderly neighbor about where to plant next season's salicornia. Mara lingers to ask a clarifying question about legal records. These moments are ordinary and stabilizing—human textures against the architectural certainty"
    "of charts."
    show councilor_rosa_menendez at left:
        zoom 0.7

    councilor_rosa_menendez "We'll compile the public record and post the models and minutes. I ask all presenters to submit finalized materials by Friday. We will convene the committee and—"
    "Her words bracket the day without resolving it. Outside, the drizzle has sharpened to a steady fall that drums the roof and makes the air smell of wet rope. The room's intensity has been mid—measured, rising"
    "and then steadying. You feel the curve of the morning: hope shaped into negotiation, into tangible next steps, into a fracture barely held with conversation."
    "Elio Sato collects his tablet with an economy that looks like control. Mateo Alvarez lingers beside you as people file out; his eyes meet yours—warm, careful."
    show mateo_alvarez at right:
        zoom 0.7

    mateo_alvarez "You did good in there. You kept the human always in the frame."
    show ari_tanaka at center:
        zoom 0.7

    ari_tanaka "We kept it on the record. That's something."
    "Jun catches your arm in the doorway, voice low."
    hide councilor_rosa_menendez
    show jun_park at left:
        zoom 0.7

    jun_park "Whatever comes, Ari... when it gets rough, don't let them sell us short."

    ari_tanaka "I won't. We'll make sure everyone hears what we said today."
    hide mateo_alvarez
    hide ari_tanaka
    hide jun_park

    scene bg ch2_c4ca42_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rain has softened to a mist; footsteps splash in the puddles]
    # play music "music_placeholder"  # [Music: Piano motif lingers and begins to fade into a single, hopeful tone]
    "You take one last photograph of the town as people disperse—the patchwork of banners and umbrellas, the little buoy lights blinking at the edge of harbor. The image is neither victory nor defeat; it is documentation: the shape of a community mid-decision."
    "In your chest there's a quiet tension that will not fold into either elation or despair. Neutral, yes—but with direction. The meeting has set a path: committees, timelines, shared models. It has also shown where the"
    "seams will split—who trusts data over dirt, who fears relocation more than a storm wall, who needs an immediate pump more than a five-year marsh plan."
    "You clasp your camera and look across the plaza toward the council chamber windows. The vote in the plaza will come next—the public spectacle where these threads tug in opposite directions."
    "A thought settles like a tide line on the lip of the sand: what happens in public is different than what is argued in papers. It will force people to choose not only strategies but loyalties. That is where the fracture will show itself."
    # play music "music_placeholder"  # [Music: Piano motif resolves to a held chord, then dips away]

    scene bg ch2_c4ca42_9 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant church bell marks the hour]
    "You inhale the damp air, steady. The morning has given you recordings, alliances, and the first outlines of opposition. It has given you, too, a map of where to stand."
    "The day is not over. The vote waits in the plaza and the heat—mid, rising—will gather there."
    # [Page-Turn Moment]
    "You tuck the camera into your tote, feel the weight of other people's faces in your mind, and take one step toward the plaza where banners already unfurl. The rain brightens the colors; a gust lifts"
    "a flapped paper from a table and it dances across the pavement like a small, urgent bird. You move after it."

    scene bg ch2_c4ca42_10 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter3
    return
