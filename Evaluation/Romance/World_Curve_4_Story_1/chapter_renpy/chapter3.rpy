label chapter3:

    # [Scene: Municipal Planning Office | Morning]

    scene bg ch3_98c6f2_1 at full_bg
    # play music "music_placeholder"  # [Music: Gentle ascending strings, hopeful]
    # play sound "sfx_placeholder"  # [Sound: Low hum of HVAC, faint city rain, paper rustle]
    "You take a breath that tastes of salt and leftover rooftop soil. The Moleskine—the sealed invitation you tucked away—rests against your ribs under your jacket like a quiet instrument. Coming from the rooftop, the warmth of"
    "strings and laughter still sits under your skin. It steadies you now in this cold, fluorescent room."
    "You set your boots softly on the concrete floor and feel the familiar friction between your urgency and the municipal rhythm. This room runs on schedules and minutes; your life runs on tides and seedlings. Today they cross."
    show mayor_anton_chi at left:
        zoom 0.7

    mayor_anton_chi "Good morning. Thank you all for coming on short notice. We have limited time before the council session. Let's hear the proposals."
    "Tomas Herrera offers you a small, encouraging smile—one of those looks that says, We've practiced. We will translate it. You place the Moleskine on the table, open to the folded tide map; someone from the city"
    "aides glances, then nods to indicate a projector. The renderings on the wall blink to life: one glossy, vertical, Elys' redevelopment plan; another, your living-shoreline diagrams, soft-green and annotated with community notes."
    hide mayor_anton_chi

    scene bg ch3_98c6f2_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Projector whir; soft exhale from the room]
    "You feel Tomas Herrera's presence at your shoulder—practical, patient—and you start to speak."
    show mara_voss at left:
        zoom 0.7

    mara_voss "Mayor, members of the planning committee—thank you for making space. We're not proposing a symbolic garden. This is a phased living-shoreline pilot that reduces storm surge impact, restores native marsh, and creates resilient public access—all built with community labor and local stewardship."
    "(Your voice is steady; your fingers trace a line on the tide map. You can see the models in the renderings respond: lower wave energy here, restored eelgrass banks here. The room leans forward.)"
    show tomas_herrera at right:
        zoom 0.7

    tomas_herrera "To add—phased design means we can start with temporary breakwaters and marsh plugs that cost a fraction of a seawall, measure performance over the next two seasons, and scale with assessed benefits."
    show mayor_anton_chi at center:
        zoom 0.7

    mayor_anton_chi "Two seasons. Cost estimate?"

    tomas_herrera "A smaller up-front capital request than full redevelopment—targeted grants and in-kind volunteer labor to reduce paid-contractor scope. We also build local workforce capacity."
    hide mara_voss
    show elys_reed at left:
        zoom 0.7

    elys_reed "Mr. Mayor, if I may. My plan addresses the same problems at a different scale. We propose a waterfront redevelopment that elevates parcels, installs engineered flood defenses, and attracts private investment to fund broad infrastructure. It's faster, comprehensive, and creates jobs."
    "(Her slide shifts to animated financial tables. The room's air tightens; the pitch is polished—employment numbers, projected tax revenue, slick before-and-after visuals. The argument is persuasive in the way a veneer can be.)"
    "You feel the push between two logics: the granular, living knowledge of roots and sediment, and the clean arithmetic of ledgers and renderings. You lean into the knowledge you carry—Rosa's greenhouse, the kids with their plant"
    "markers, the smell of peat and citrus—and decide how to stitch it into the sterile language of the room."

    menu:
        "Open with the tide-chart anecdote—Rosa handing a cutting to a councilmember":
            "You begin with a small human image: Rosa's stained hands, a councilmember surprised by the plant's resilience. Faces in the room soften; the numbers that follow land on warmer ground."
        "Lead with hard data—wave attenuation percentages and cost projections":
            "You start with the models, your voice crisp over charts. Brows knit as the mechanics of shoreline restoration become incontrovertible; the mayor's pen moves faster, interest sharpening."

    menu:
        "Invite Rosa to stand and offer a brief testimony":
            "Rosa rises. Her voice is small but unwavering; the room calms, and the anecdotal proof becomes harder to dismiss."
        "Keep the focus on policy and step through the phased timeline":
            "You slide into policy detail. The mayor nods at the timeline; eyes in the room track the milestones and deliverables. Momentum builds under administrative logic."

    menu:
        "Partner directly with Tomas and Mayor Anton to fast-track a phased pilot.":
            jump chapter4
        "Launch a public referendum and community-led campaign to force a grassroots victory.":
            jump chapter8
        "Expose Elys' redevelopment narrative publicly through Lena and push for stricter oversight.":
            jump chapter11
    return
