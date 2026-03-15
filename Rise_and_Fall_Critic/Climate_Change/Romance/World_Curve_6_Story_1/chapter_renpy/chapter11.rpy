label chapter11:

    # [Scene: Research Plots & Town Hall Corridor | Dusk]

    scene bg ch11_e67f19_1 at full_bg
    # play music "music_placeholder"  # [Music: Piano and strings, a single luminous chord that suggests continuation]
    # play sound "sfx_placeholder"  # [Sound: Night insects, a distant bell; muffled footfalls on boardwalk planks]
    "You stand with the last soil under your nails and the dashboard still open in your head: the small, stubborn trendline that started as a pilot and is now a political heartbeat. Jonah is beside you,"
    "shoulder close enough that his sweater brushes your sleeve; Asha's curt messages have, for the moment, become notes in a shared document. The air smells of brine and cut grass, and the evening fog sits like"
    "an audience outside the lab windows."
    "You tuck your compass beneath your jacket and feel it against your sternum—an old weight turned steady. Tonight, the town hall room will be fuller. Data will go from being quiet numbers to a thing people"
    "must argue with. You breathe in the salt and the low hum of collaboration; the lift under your ribs is small but genuine."
    # [Scene: Town Hall | Early Evening]

    scene bg ch11_e67f19_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Chairs scraping, a murmured hello; the projector whirs to life]
    # play music "music_placeholder"  # [Music: A hopeful, ascending arpeggio]
    "Evelyn stands at the head of the table like she always does—slender hands folded, the weight of votes pressed into her eyes. Dr. Lian sets up the slides with the practiced calm of someone who has spent years translating tides into stories the public can hold."
    show dr_lian_zhou at left:
        zoom 0.7

    dr_lian_zhou "We ran a twelve-week energy-dissipation analysis on both plots. The living shoreline reduced near‑shore wave energy by an average of thirty-four percent under the median storm scenario. The engineered berm and navigational cut preserved channel depth within operational tolerances and reduced overtopping events for vessels."
    "You hear the numbers as both a triumph and a ledger. Thirty-four percent is a figure people can quote at meetings — it is also a human shape: fewer boats hauled onto wet docks, fewer basements flooded. Lian's cursor hovers on a graph; teal lines dip and breathe."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "How confident are we in that thirty-four percent across a range of storm intensities?"

    dr_lian_zhou "Model confidence is high within our calibration window; we ran ensemble scenarios with field-truthing from the sensor buoys. There are greater uncertainties at extremes, but the trend is robust. Importantly, the living shoreline also increased sediment accretion rates along adjacent marsh by measurable margins."
    show asha_verma at center:
        zoom 0.7

    asha_verma "Sediment is useful. But the region is asking one simple question: which solution is most cost-effective at scale? They need a single metric to present to the legislature. If we present a mixed message, the funding tranche is at risk."
    "Her tone is blunt but not unkind; there's steel behind it. You sense the logic in her words like a tide—unavoidable, shaping everything it touches. Still, the room holds other sounds: Jonah's hand on the table, Bento's breath, Kai's restless foot tapping against his shoe."
    hide dr_lian_zhou
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "If 'most cost-effective' becomes the only measure, what happens to the harbor's shallow shoals, to the mooring lines? We can't just half‑erase our navigation. People fish at dawn—"

    asha_verma "We don't erase. We design access. But the region's models need a replicable package. They can't fund variability. You know this, Jonah."
    "The exchange is more than technique. It's a clash of metaphors: life-grown resilience versus engineered certainty. You have been trying, for weeks, to make them translations of the same language."

    menu:
        "Place a hand on Jonah's forearm to steady him":
            "Jonah relaxes a fraction, the tough set of his jaw easing. He catches your eye and gives a small, grateful nod; you feel the soft give of community trust."
        "Offer Dr. Lian a clarifying question about data transparency":
            "Lian nods appreciatively—and launches into an extra slide about open datasets and code repositories, which draws appreciative murmurs from Kai and a quirked eyebrow from Asha."

    # --- merge ---
    "The meeting continues with Lian elaborating on data access and community concerns."
    hide mira_kestrel
    show dr_lian_zhou at right:
        zoom 0.7

    dr_lian_zhou "We've archived the raw sensor streams and analysis scripts. With the right governance, community scientists could audit or extend this work."
    hide asha_verma
    show kai_tan at center:
        zoom 0.7

    kai_tan "That's the point. If the data is locked up for the 'replicable package' of some regional contractor, Tidehaven loses more than shoreline—it loses ownership. We organized a demonstration at the promenade to demand community ownership of the dataset and the right to co-design the scaling."
    "A low sound of approval rises from the younger people in the room; Bento exhales a soft warning."
    hide jonah_reyes
    show bento_old_bento_morais at left:
        zoom 0.7

    bento_old_bento_morais "We are not against progress, but there are anchors beyond economics—our rituals use certain mooring points, old names give place. If we let some outside plan re-chart the harbor for profit, we'll wake up without the stories we need to navigate."
    hide dr_lian_zhou
    show evelyn_sato at right:
        zoom 0.7

    evelyn_sato "The region has promised a conditional grant sizeable enough to do a full-scale implementation. We could preserve large tracts, but they will insist on one presentation—one replicable model with measurable outcomes. Also,' (she opens an envelope and smooths the paper) 'a developer filed a petition to alter a stretch of the promenade—propose a waterfront complex that would, they say, 'stabilize revenue' and 'create public spaces.' It reads clean on the form and smells of private profit."
    "You taste salt and a metallic worry. Developer petitions read like clean ink, but they carry cultural erosion in their margins."
    hide kai_tan
    show mira_kestrel at center:
        zoom 0.7

    mira_kestrel "What do they want to do to the promenade, exactly? Will it impinge on the research plots or the ceremonial moorings?"

    evelyn_sato "A swath of boardwalk, yes. And some of the docks for small boats. They say they can 'elevate' and 'integrate floodproof architecture.' In practice, it could mean privatized access points and a re‑zoning that makes some traditional fishing slip leases untenable."
    "Your throat tightens. Jonah looks toward the window as if the developer's plans are already cutting the harborline."
    hide bento_old_bento_morais
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "They'll paint it pretty and call it safety. But who will get to fish at dawn in those slips? The risk is turning our living memory into merch."
    hide evelyn_sato
    show asha_verma at right:
        zoom 0.7

    asha_verma "The region's priority is fewer flooded homes across a wider area. If a model demonstrably reduces risk faster, it will be chosen. Developer plans are a separate political pressure: they see the harbor as an asset. We have to separate the technical from the opportunistic."
    hide mira_kestrel
    show dr_lian_zhou at center:
        zoom 0.7

    dr_lian_zhou "Both models have merits. And the pilot shows the living shoreline works well here. Financial analyses suggest different scales of up-front cost, different timelines for maintenance.' (She looks at you.) 'Mira—you've been the mediator. The region wants a recommendation."
    hide jonah_reyes
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "They want a single recommendation tied to a funding clamp. But we also have community petitions and demonstrations demanding shared governance of the data. We can present both pilots and a governance framework, but I'm worried the region will withdraw funding if we don't pick one path."

    menu:
        "Ask for a short adjournment to take the crowd's pulse at the promenade":
            "You stand. The room leans in as you slip out; the promenade is a knot of signs and faces. Kai hands you a flyer and Bento performs a low, steady greeting to the crowd, and you return with a clearer sense of what people fear and hope for—uneven, urgent, alive."
        "Propose an immediate hybrid governance model in the meeting":
            "You sketch a frugal framework on the easel: open datasets, escrowed funding tranches, and staged scaling contingent on community votes. The plan lands as both practical and imperfect—Evelyn's eyes shine with cautious hope while Asha chews on the oversight demands."

    # --- merge ---
    "The meeting resumes with renewed focus on governance and tradeoffs."

    "The room's energy shifts. Outside, someone chants from the promenade—Kai's voice threaded through a megaphone" "Our data, our future!"
    hide asha_verma
    show evelyn_sato at right:
        zoom 0.7

    evelyn_sato "If we go to the region with a tangled message, they may fund a single 'best' approach elsewhere and leave our pilots underfunded. If we choose one, we risk losing elements the living shoreline preserves. If we demand local votes first, funding is at risk but the community keeps agency. It's a damned set of tradeoffs."
    hide dr_lian_zhou
    show bento_old_bento_morais at center:
        zoom 0.7

    bento_old_bento_morais "And what of our rituals? Who speaks for the slips we tie to on storm nights? Money doesn't hold memory."
    hide mira_kestrel
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "Mira, you know I trust the community, but I also know we need real infrastructure that keeps engines on and nets in the water. I don't want to see Tidehaven become a museum people only visit in pictures."
    "His hands find yours for a second—brief, complex, neither promise nor retreat, only steadiness that presses heat into your palm."
    hide evelyn_sato
    show asha_verma at right:
        zoom 0.7

    asha_verma "We can design oversight into an engineered package. Strict monitoring, community liaisons, guaranteed access points. It won't be sentimental—but it can be protective."
    hide bento_old_bento_morais
    show kai_tan at center:
        zoom 0.7

    kai_tan "But that's the rub: 'guaranteed access' in a contract can be erased. The living shoreline keeps place in its bones. The data proves it; the community can vouch for it."
    hide jonah_reyes
    show dr_lian_zhou at left:
        zoom 0.7

    dr_lian_zhou "Both datasets tell a story. We can model socioeconomic outcomes from both scales. We can show the region the human impacts alongside the metrics—if they'll listen."
    hide asha_verma
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "We have to give them a recommendation that honors the data and the people. We have to guard the town's memory and the harbor's daily life. There is a way to translate stewardship into replicable indicators—sediment accretion, reduced energy, maintained channel depth—but governance must be explicit."
    hide kai_tan
    show evelyn_sato at center:
        zoom 0.7

    evelyn_sato "If we ask for votes first, we might lose the grant entirely. If we choose one model, we risk something else. You must recommend a path, Mira."
    "You watch the faces around you: Lian's steady scientist calm, Asha's pragmatic intensity, Jonah's worn loyalty, Kai's fierce idealism, Bento's ancestral patience, Evelyn's municipal exhaustion. Their wants are not simple; their fears are human."
    "You feel, stubborn and strangely buoyant, that the town has given you a hard job because it trusts you to turn conflict into a scaffold. The rising chord of the piano in your head matches the"
    "lift of possibility: this is messy, yes—but also real work being done, people gathered, options on the table."

    mira_kestrel "We can do this in three ways. We can recommend scaling the living shoreline for regional funding. We can recommend scaling engineered protections with strict oversight. Or we can demand public votes and stronger community ownership before scaling—and risk funding withdrawal. Any recommendation will change the town. Any path will ask of us a different kind of courage."
    # play music "music_placeholder"  # [Music: The arpeggio rises into a hopeful sustain; the room exhales]
    hide dr_lian_zhou
    hide mira_kestrel
    hide evelyn_sato

    scene bg ch11_e67f19_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant bell, steady]

    menu:
        "Recommend scaling the living shoreline for regional funding.":
            jump chapter12
        "Recommend scaling engineered protections with strict oversight.":
            jump chapter12
        "Demand public votes and stronger community ownership before scaling—and risk funding withdrawal.":
            jump chapter15
    return
