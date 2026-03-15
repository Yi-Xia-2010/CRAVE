label chapter3:

    # [Scene: Promenade & Dunes | Early Evening]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Soft, swelling strings with an ascending motif — hopeful, steady]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls; the tide-gauge clicking in the background; muffled conversation and the scratch of umbrellas]
    "Narration:"
    "You step onto the promenade and the air presses against you — briny and expectant. Umbrellas tilt like dark flowers; breath fogs in small clouds. The town has come out beneath the lamps, half in raincoats,"
    "half in hopeful finery. Children wriggle on laps. An old man in a patched cap pats his pockets where a memorial tide-token clinks."

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Your own pulse, steadying]
    "Narration:"
    "Rosa is at your elbow, her clipboard a physical punctuation mark. Jonah is at the back, voice a taut wire. Elias stands three rows back, hand half-hidden in his coat pocket; his face is lit by"
    "the flood, and his expression reads like a closed horizon — complex and unreadable. Dahlia Kestrel occupies the podium now, glass tablet glowing in her hands; the Arc renders on the screen behind her in clinical"
    "teal."
    show dahlia_kestrel at left:
        zoom 0.7

    dahlia_kestrel "Lumen Bay deserves a solution that scales. The Arc is modular, tested in similar coastlines, and it can be deployed quickly. We pair structural barriers with adaptive pumps and monitoring. We can save homes, create jobs, and stabilize the waterfront within a single construction season."
    hide dahlia_kestrel

    scene bg ch3_98c6f2_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A muted click as the projection layers animate; the crowd murmurs]
    "Narration:"
    "Her voice is smooth, practiced. The visuals are seductive in their simplicity: lines that promise certainty. You feel the hunger in the room for that certainty — the relief it could offer your neighbors whose roofs leak and whose front stoops have been measured against rising marks year after year."
    show rosa_mendes at left:
        zoom 0.7

    rosa_mendes "Keep it crisp. Focus on the marsh outcomes first."
    show maya_reyes at right:
        zoom 0.7

    maya_reyes "I will."

    menu:
        "Scan the crowd for friendly faces":
            "You let your gaze rest on the familiar: the kids with mud on their knees, Mrs. Alvarez with her knitting, Jonah's angled jaw. The warmth steadies you."
        "Breathe and count slowly to four":
            "You inhale the cold, saline air and slow your heartbeat. The rhythm puts a space between panic and voice; the boardwalk feels firmer underfoot."

    # --- merge ---
    "Narrative continues."
    "Narration:"
    "Dahlia steps down as questions open. Hands rise. A woman in a faded fisherman's jacket asks about job guarantees. A young father asks about beach access. Jonah's shout cuts through before the moderator can catch it."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "Are you asking us to trade our nets for concrete? Who's paying for the losses when the machines need repair?"
    # play sound "sfx_placeholder"  # [Sound: A ripple of agreement; a few boos. The floodlights hum like a distant engine.]
    hide rosa_mendes
    show dahlia_kestrel at left:
        zoom 0.7

    dahlia_kestrel "The Arc includes maintenance funds and training for local workers. We prefer local partnerships for operations. This isn't outside replacement—it's support."

    maya_reyes "Support depends on trust. And trust comes from transparency and real power in the hands of those who know this shoreline."

    dahlia_kestrel "Ms. Reyes, with respect — community knowledge is valuable, but it's not always sufficient to meet the rapid escalation we're seeing. We have models, fail-safes, redundancies. We can act faster than ad-hoc restoration projects."

    maya_reyes "Fast action that ignores living systems can create new vulnerabilities. The marsh is not placeholder; it's active infrastructure. It filters, it attenuates, it rebuilds itself when given space. Our community plan pairs marsh expansion with livelihood programs — living jobs that keep people here and restore the shoreline over decades, not weeks."

    dahlia_kestrel "Pairing is possible. But 'decades' is not a promise when someone's roof is gone next season."
    hide maya_reyes
    show mayor_lyle_durant at right:
        zoom 0.7

    mayor_lyle_durant "We'll open the floor. Ms. Reyes, you'll have the first segment of cross-examination with the company. Keep it to ten minutes."
    "Narration:"
    "You step forward. The mic is cold at first; then your fingers warm it. Sodium lamp light glosses the wire. The crowd tilts toward you as if expecting to be led. You can see the tension in Elias' shoulders; he does not seem pulled to either extreme, only watchful."

    menu:
        "Begin with data — show the marsh overlays and growth curves":
            "You pull up the diagrams from your tablet: cordgrass corridors, sediment accretion rates, community employment projections. The numbers are clear and humanized with photos of the volunteers who make them possible."
        "Begin with a story — your father at high tide":
            "You tell of your father's boat, a small white knife of memory in wet light. Faces around you soften; someone wipes at their eyes. The room breathes in the image and the stakes get personal."

    # --- merge ---
    "Narrative continues."
    "Narration:"
    "You choose the opening that feels truest — whether data or story, both are shapes of truth here. You map the marsh, explain how plugs become channels, how co-managed aquaculture can bring in income as the"
    "mudflats rise. You lay out timelines that are honest about pace but ambitious about scope."
    hide jonah_reyes
    show rosa_mendes at center:
        zoom 0.7

    rosa_mendes "Emphasize how the jobs are trained locally. Say the numbers again."
    hide dahlia_kestrel
    show maya_reyes at left:
        zoom 0.7

    maya_reyes "We propose a phased approach: immediate jobs planting cordgrass and rebuilding berms, mid-term training for marsh technicians, and a locally run monitoring network that feeds into any larger structures placed seaward of the marsh. We are not anti-technology — we are pro-integration."
    # play sound "sfx_placeholder"  # [Sound: A few claps; a murmur of approval moves like a small wave]
    hide mayor_lyle_durant
    show dahlia_kestrel at right:
        zoom 0.7

    dahlia_kestrel "Integration requires shared governance. We're open to advisory roles and joint operation plans. But capital timelines are tight. If Lumen Bay wants to be part of a pilot, we need binding commitments."

    maya_reyes "Binding by whom? We will not accept arrangements that marginalize our ability to steward what we live on. Oversight must include community vetoes for activities that harm ecological function."
    # [Dialogue ripples through the crowd — sharper now]

    "Resident 1" "What about our fishing grounds?"

    "Resident 2" "Will the promenade be closed during construction?"
    hide rosa_mendes
    show mayor_lyle_durant at center:
        zoom 0.7

    mayor_lyle_durant "Questions for both parties. Let's keep them pointed."
    "Narration:"
    "The forum tightens into a crucible of practicalities. The Arc glows like a machine of promises; the marsh plan smells of wet soil and the honest labor of hands. You can feel the room lifting, not"
    "toward easy answers but toward the possibility of a shared design — contingent, negotiated, human. There is a tangible hope in the air now, like the smell of rain after a long dry spell."

    menu:
        "Lock eyes with Elias before you make the ask":
            "You find Elias in the crowd, and for a second his face opens — just a fraction. You read that as permission to speak for a future that keeps his people whole."
        "Look past him to the youngest faces in the front row":
            "You see kids with boots two sizes too big and a toddler asleep against a parent's chest. The thought of them inheriting this landscape steels your resolve."

    # --- merge ---
    "Narrative continues."
    "Narration:"
    "You inhale. Ten minutes stretches and compresses into one small, luminous moment. You imagine the marsh at a high tide that does not swallow front porches—cordgrass like a green comb along the waterline, neighbors in orange"
    "vests checking sediment traps, Jonah teaching apprentices how to read a tide chart. You think of your father, of all the fathers and mothers and neighbors who have small rituals tied to the bay."

    mayor_lyle_durant "Ms. Reyes, the floor is yours. The town is listening."

    maya_reyes "Thank you. We all want safety. But safety is not only a wall or a promise on a glossy slide. Safety is work, and it is shared. Today I will put forward options that don't ask us to choose between jobs and ecology, or between speed and stewardship. We can do both — if we design it that way."
    "Narration:"
    "The crowd leans in. Dahlia watches you closely; there is a flash of something like calculation behind her ice-gray eyes. The sodium lamps seem to warm as the music lifts an octave — the prevailing mood"
    "is not surrender to diktat nor fearful resignation. It is collective will finding a shape."
    "You feel, in the bones of the boardwalk, the possibility of something that honors both urgency and the slow, living repairs of the bay. Your voice is tight but rising; the proof points are lined up like stepping stones."
    "Narration:"
    "Now comes the pivot. The question you ask the town and the council will not be a small one. It is a hinge between timelines and values, between the kind of safety you want and who gets to design it."
    # play music "music_placeholder"  # [Music: Strings swell, holding on a hopeful, ascending chord]

    menu:
        "Propose a formal partnership: community co-management with conditions.":
            jump chapter4
        "Refuse corporate involvement; double down on community-only restoration.":
            jump chapter7
        "Accept Dahlia's proposal with strict conditions and a seat on the advisory board.":
            jump chapter10
        "Call for delay: commission independent studies and a neighborhood vote.":
            jump chapter13
    return
