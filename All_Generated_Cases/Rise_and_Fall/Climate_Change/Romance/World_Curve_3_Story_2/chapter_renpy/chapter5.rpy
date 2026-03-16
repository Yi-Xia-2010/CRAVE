label chapter5:

    # [Scene: Elias's Field Office | Morning]

    scene bg ch5_4001e7_1 at full_bg
    # play music "music_placeholder"  # [Music: Warm piano motif, steadying strings beneath]
    # play sound "sfx_placeholder"  # [Sound: Soft hum of laptop fans, distant gulls; a wind that carries the salt of the harbor]
    "You press your palm to the worn leather of your notebook and feel the ridge of the friendship bracelet beneath the cover. The word from the last meeting — influence from within — tastes like permission"
    "and responsibility at once. Your fingers find the sketch of scalloped sluices and marsh buffers, the pen lines blurring where your hand trembled. You breathe, steadying the breath in your chest, and step into the small"
    "ring of light the trailer offers against the overcast morning outside."
    "Elias Hart stands by the model, palms on the dome as if measuring its weight. Dr. Kenji Sato is adjusting a printout of long-term projections; his thin fingers leave fingerprints across years of tidal curves. Marina waits near the door, nervous energy tucked into her clasped hands."
    show elias_hart at left:
        zoom 0.7

    elias_hart "Morning. Ready to hear it?"
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "It's a hybrid. Targeted reinforced promenades where the town needs them, paired with marsh restoration and community-built levees where habitat matters and fishing lanes must be preserved."
    hide elias_hart
    hide amina_reyes

    scene bg ch5_4001e7_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Paper rustle; the faint ping of a notification ignored]
    "You keep your voice even because words will matter — not only what you say, but how you make people imagine the future. You point at the sketch. The light from the laptop washes the ink in pale blue."
    show amina_reyes at left:
        zoom 0.7

    amina_reyes "The promenade sections are strategic — not a continuous wall, but reinforced nodes that protect the town center and market while leaving tidal flow and sediment transport largely intact. The marsh work uses native cordgrass plantings, small living berms, and boatwright-built levees to protect lanes. The monitoring protocol phases the install, so we can measure sediment accretion and fish passage."
    show dr_kenji_sato at right:
        zoom 0.7

    dr_kenji_sato "The models Kenji ran support your idea. (He taps a sheet.) With the staged approach, the initial return on ecosystem services looks promising over a twenty-year horizon. We reduce peak surge energy at the nodes and preserve sediment supply to adjacent marshes."
    "Kenji's voice is steady, the scientist's cadence you trust. He doesn't promise miracles, but his projections are a scaffold — something you can hang a plan on."
    show elias_hart at center:
        zoom 0.7

    elias_hart "Funding timelines are tight. The regional authority can release seed funding if we commit to a demonstration at the test marsh platform within six weeks. That gives us leverage to scale, but I need a clear scope."
    "You feel the old calculation habits kicking in — what can be done, what must be deferred. The promise of immediate money tugs at one side of you; the need for community consent tugs at another."
    hide amina_reyes
    show marina_lopez at left:
        zoom 0.7

    marina_lopez "If it helps, I can line up a school group for a planting day later — kids, parents, the whole community seeing hands-on restoration. People come when they can touch it."
    "Marina's smile is slight but real; her practical impulse to involve families is a bridge you didn't know you needed."
    "Elias Hart watches you, the slate-gray of his coat folding into a soft, expectant expression."

    elias_hart "If you can guarantee community labor and oversight in the scope, the authority will be more comfortable with a smaller initial footprint. Co-management language helps the grant application. We're not asking you to sell out, Amina — we're asking you to shape the terms."
    "You feel the word 'sell out' like a soft bruise over your ribs, but Elias doesn't say it aloud. His confidence is steady; you can see the trust he places in your models."
    hide dr_kenji_sato
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "Then let's scope the pilot to include: one reinforced promenade node, a contiguous 200-meter living berm, and a test levee segment built by local crews. Full monitoring for two seasons."
    "Dr. Kenji Sato: (nodding) 'We can get baseline measures now. With community-built monitoring, the data becomes part of town memory, not just graphs in a meeting.'"
    "You feel the plan taking shape in your hands, like a plank being fitted into a fraying boardwalk. This is work you can do — mud and minutes, models and hands."

    menu:
        "Emphasize the science — present the monitoring plan first":
            "You push the monitoring protocol forward on the table, highlighting community science roles and data transparency. Their eyes linger on the graphs, the promise of evidence calming some skepticism."
        "Emphasize the hands — outline the community labor roles":
            "You slide the community labor diagram into view, sketching who will lead which work shifts. Marina brightens; Elias makes a note, and Kenji murmurs assent about participatory monitoring."

    # --- merge ---
    "Continue"
    hide elias_hart
    hide marina_lopez
    hide amina_reyes

    scene bg ch5_4001e7_3 at full_bg
    # play music "music_placeholder"  # [Music: Piano warms into a hopeful swell]
    show elias_hart at left:
        zoom 0.7

    elias_hart "I'll draft the grant language with co-management phrasing. Kenji, can you finalize the monitoring metrics? Marina, can you coordinate outreach? Amina — will you run construction protocols and liaison with the crews?"
    "You close your notebook and feel the familiar knot on the thread between responsibility and guilt — but this time it sits next to something different: a tangible roster of tasks and faces."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "Yes. I'll run the protocols, and I'll ask Niko to lead the boatwright teams for the levees. They need to be central to the build."
    "Elias Hart's expression softens at the name. Marina exhales like relief. Kenji gives you a small, approving glance."

    elias_hart "Good. I'll schedule the demonstration installation at the test marsh platform for the week after next. We bring equipment, safety, and funding. You bring crews and knowledge. We'll be explicit — co-managed, locally led construction with institutional resources."
    "You feel the corners of your mouth lift. The plan reads like compromise, but compromise is a tool here — not surrender."
    # [Scene: Montage — Planning and Preparation | ]
    hide elias_hart
    hide amina_reyes

    scene bg ch5_4001e7_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Clicking tools, distant laughter, a gull's call cutting the montage]
    # play music "music_placeholder"  # [Music: Strings rise into an optimistic chord]
    "You spend two days drafting the construction protocol, walking the marsh margins with Kenji to mark monitoring transects, and calling Niko's boatyard to ask for help. Each conversation pulls the plan into clearer relief: who will wield a hammer, who will plant the cordgrass, who will record salinity at dawn."
    # [Scene: Test Marsh Platform | Afternoon]

    scene bg ch5_4001e7_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Reeds whispering, water lapping, the distant thud of a winch]
    # play music "music_placeholder"  # [Music: Gentle cello underscoring the natural soundscape]
    "You stand on the muddy edge of the platform, your boots sinking as the tide pulls at the grasses. The place smells of peat and salt, of tar that has dried into memory. The test site feels vulnerable and alive at once. This is where theory will meet tide."
    "Elias Hart walks the line with you, his tablet tucked away as he listens. Dr. Kenji Sato kneels to sample sediment, murmuring numbers under his breath. Marina is already calling volunteers, her voice buoyant as she organizes shifts."
    show elias_hart at left:
        zoom 0.7

    elias_hart "This is the node. We'll anchor the promenade here, keep the structure open to flow beneath, and the living berm will be sited to encourage accretion. If the plants take in the first season, it will validate the approach."
    "You imagine the first cordgrass shoots, rooted where hands pressed them into place. You imagine the boatwrights hauling a levee, the town turning up for a planting day. The image steadies you."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "We'll document everything. Not just for the grant, but so the town can see the change. If this works, it's replicable — not just here but across other vulnerable towns."
    "Dr. Kenji Sato: (smiling faintly) 'Replicable and resilient. It's a modest reach, but it's the kind of reach that's worth it.'"
    "The idea feels possible in a way it didn't before: part policy, part labor, part love for a place. You tuck your bracelet beneath the cuff of your sleeve and run your thumb over the knot."
    # [Scene: The Old Boardwalk & Market | Late Afternoon]
    hide elias_hart
    hide amina_reyes

    scene bg ch5_4001e7_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Market noises—frying fish, a child's laughter—muted beneath a new tension]
    # play music "music_placeholder"  # [Music: Gentle strings, a single higher note of apprehensive fluting]
    "You walk the boardwalk to check on outreach posters when you see Niko. They are leaning against an old piling, cap low, braided hair tucked under it; the silver thread in their plait glints like a"
    "small fault line. Their oilskin vest holds the smell of tar and varnish. Around them, a few boatwrights stand with folded arms."
    show niko_kaur at left:
        zoom 0.7

    niko_kaur "So this is your plan, huh? Working inside their trailer?"
    "Their voice is blunt, edged with weather. You feel the old ache open — Niko's presence pulls the past into now, all the things you promised yourself you'd protect stitched into their accusation."
    show amina_reyes at right:
        zoom 0.7

    amina_reyes "Niko—"
    "Niko Kaur cuts you off with a single, hard laugh that tastes like rain."

    niko_kaur "You always had a way with plans, Amina. But now the plans come with money and men in neat coats. People will call this salvation; my people will call this a sellout. You'd better know what you're trading."
    "Their eyes are storm-gray and fixed on you. There is history there — the boatyard nights, the rebuilding of a broken hull — but more than that, there's fear of displacement threaded into anger."
    "You feel your chest tighten. You run a thumb over the bracelet knot like a small anchor."

    amina_reyes "I'm trying not to trade anything. I'm trying to build something that keeps the lanes and the marsh. I'm asking you to lead the levees."
    "Niko Kaur: (bitter) 'Lead? Or make the work look local while the decisions live in their models? When the tides come and the politicians clap themselves on the back, will they remember who fished here first?'"
    "Elias Hart steps forward slightly, a conciliatory gesture; Marina lingers near the stalls, watching the exchange with worry carved into her brow."
    show elias_hart at center:
        zoom 0.7

    elias_hart "Niko, I said co-managed. The funding comes from regional authorities, but the control can be with the community. We wrote co-management into the grant language."
    "Niko Kaur: (snorts) 'Co-managed — a phrase for people who like to eat words when the check clears. Names on a paper don't keep nets in the water.'"
    "You feel the conversation sharpen like a wire. The past loss you carry makes every accusation land with extra weight. And yet, beneath the accusation, you hear something else — fear that the town's hands will be erased from its own work."

    amina_reyes "Tell me what would make this feel like ours, Niko. Not a PR line. Real ownership. Who needs to sign what, who needs to be paid, what parts of the design need to be scrap-and-rebuilt so the method is ours?"
    "Niko studies you. They come closer, their boots scuffing the wood. The silver thread in the plait catches light and then shadow."

    niko_kaur "You ask fast. I want crews hired on honest terms. I want wages in advance to cover lost work. I want the levee designs to be visible — no hidden blueprints. And I want the first planting day organized by the boatwrights, not a charity post. If this is real, then we lead. If it's show, you'll have to answer to the people who lose everything."
    "The list is practical and just; it is the language of people who have built and bled for their livelihood. Each demand is a plank to be laid or an edict to be refused."
    hide niko_kaur
    show marina_lopez at left:
        zoom 0.7

    marina_lopez "We'll do that. We'll write those requirements into the co-management agreement. Amina already suggested community oversight for monitoring."
    "You see the moment: the plan can become co-created, or it can be imposed. The funding window leans like weather — present now, and it may close."

    menu:
        "Step forward and offer to draft the co-management clause with Niko now":
            "You pull the notebook back into your hands and start writing the first clause aloud — wages, transparency, hiring. Niko listens, the tension easing as specifics tumble out."
        "Step back and promise to discuss it at the assembly and give Niko space":
            "You fold your hands and offer a softer promise to convene a wider meeting. Niko's jaw works; it's not a yes, but the space may open the door for trust."

    # --- merge ---
    "Continue"
    "Niko exhales, a rough sound that could be resignation or a small thaw."
    hide amina_reyes
    show niko_kaur at right:
        zoom 0.7

    niko_kaur "Talk doesn't build levees, Amina. But talk can keep us honest. If you're asking us to show up, then we need to see the terms before the machines arrive."
    "You stand on the creaking boardwalk and look out at the marsh you want to protect. The tide draws itself into the reeds; the light has that peculiar softness that tells you work begun now could"
    "bear fruit later. Around you, the town is a mix of skepticism and hope — Marina's steady hands ready to gather families, Kenji's models waiting to be tested, Elias' funding almost within reach."
    "You run your thumb over the friendship bracelet and feel the knot of obligation tighten and then, under it, something else: possibility. The hybrid sits before you like a hinge: it could be a tool to hold the town together, or it could split the seam wider."
    "You think of your brother, of the boardwalk after the last storm, of the people who will turn up if they believe their labor matters. You think of the six-week window for the funding, and of the way co-management language in a grant can change the balance of power."
    "You inhale the cold, salt-scented air and feel an unexpected warmth at the center of your chest. This is not a moment of defeat; it is a moment of choosing how to fight."
    # play music "music_placeholder"  # [Music: Piano and strings swell into an optimistic cadence]

    menu:
        "Publicly endorse the hybrid immediately—use Elias’s funding to build the pilot now.":
            jump chapter6
        "Delay and convene a community assembly—rebuild trust with Niko and the boatwrights before construction.":
            jump chapter13
        "Launch a co-managed pilot: invite Niko’s crew to lead construction while Elias secures funding—forcefully merge worlds.":
            jump chapter16
    return
