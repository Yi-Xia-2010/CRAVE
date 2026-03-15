label chapter10:

    # [Scene: Verdant Rooftop Nursery | Morning]

    scene bg ch10_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Quickening, hopeful strings underscored with percussive taps]
    # play sound "sfx_placeholder"  # [Sound: Soft hiss of drip irrigation; gulls distant]
    "You start where you promised you would: with soil in your nails and the slow, stubborn business of new growth. The barometer against your sternum ticks to the rhythm you learned as a child; it keeps"
    "time with something older than budgets and briefs. Dr. Sora’s clipboard rests against a tower of planters. Evan's hands, when he leans over the modular sketches, are already smudged in graphite and rust. Tala is here"
    "with a crate of flyers that smell faintly of salt and printer ink."
    "You move among the seedlings, naming practical things to steady your voice. Reed beds at the lot edge will trap sediment. The modular habitat must be light enough to float on higher tides yet anchored to"
    "human hands. The desal unit — Evan's quiet hyphen — will hum in the night like a small heartbeat, turning brine into something you can drink and count."
    show evan_kaito at left:
        zoom 0.7

    evan_kaito "You remembered the layered plan for the reeds. Good—if the roots anchor like Sora predicts, we'll get a fifty percent uptake next season."
    show maya_alvarez at right:
        zoom 0.7

    maya_alvarez "We need the real people seeing it, not just a PowerPoint. Open days, live demonstrations. If the mayor can step out of the atrium and smell wet soil, that's half the argument."

    evan_kaito "I like the way you say 'smell wet soil' like it's a policy line. Also—' (he taps his camera) '—I can document occupants. Living evidence."
    show dr_sora_kim at center:
        zoom 0.7

    dr_sora_kim "Data and dignity. Both will go in the grant text. I can quantify carbon capture, sediment accretion rates — and we can show weekly metrics."
    hide evan_kaito
    show tala_ruiz at left:
        zoom 0.7

    tala_ruiz "And I'll make sure the tours bring a dozen neighbors at a time. Crowd's an audience and an argument."
    "You listen, and your chest unwinds a couple of degrees. There's movement. The plan is less a powerpoint than a small, living demonstration."
    # [Scene: Small Pilot Lot | Midday]
    hide maya_alvarez
    hide dr_sora_kim
    hide tala_ruiz

    scene bg ch10_453e40_2 at full_bg
    # play music "music_placeholder"  # [Music: Fast, optimistic electrical hum; a pulsing undercurrent]
    # play sound "sfx_placeholder"  # [Sound: Clanking of tools, the low whirr of a compact desal unit; neighborly chatter]
    "You sweat into your field jacket and let the sun and salt chase the cold from your bones. People come in shifts — neighbors, curious students, an old carpenter with a hand like a pocketknife. Evan"
    "walks groups through panel assembly like a calm conductor, demonstrating each bolt, each splice, every weather-proofing trick he's taught himself. He talks slow, patient, and neighbors lean in. You stand nearby, translating engineer to neighbor, memory"
    "to method."
    show evan_kaito at left:
        zoom 0.7

    evan_kaito "Use the star-bracket on the lower flange — it takes the lateral shift. Don't overtighten; the panels expand with salt."

    "Neighbor" "I've never put up panels in my life—"

    evan_kaito "Neither had I, till last winter. You'll get the hang of it. Here—try this."
    "He hands the neighbor a tool. Your stomach skitters in a way that isn't all nerves; it's recognition—he trusts people into competence. You catch him glancing at you when the neighbor succeeds, like he's cataloguing small victories and planting them somewhere."
    "Dr. Sora kneels beside a tray, stabs a probe into the soil, and takes a reading. Her face, at first clinical, softens at a figure that pleases her."
    show dr_sora_kim at right:
        zoom 0.7

    dr_sora_kim "Salinity trending down along the marsh verge, despite last week's spike. The reed transplantation is buffering micro-salinities."
    show maya_alvarez at center:
        zoom 0.7

    maya_alvarez "How fast can we publish that?"

    dr_sora_kim "A week for preliminary, with raw datasets. Twelve for a digestible brief to the press. But the real work is in living. If Mayor Park sees one family sleeping in the habitat overnight, that trumps any headline."
    "You let the idea settle — demonstration rather than argument — and make a mental list: cameras, overnight permissions, a clear data feed to the town's website."

    menu:
        "Climb the scaffolding to check the panels from above":
            "You climb, breath shallow, and see the lot stitched into the town—boardwalk, nursery, a sliver of glass from the Council House. From this angle Evan's silhouette is a small, precise constellation of motion below."
        "Stay at ground level and continue planting with Tala":
            "You sink your hands into a tray of reeds. Tala hums an old knot-song as she seeds; the rhythm steadies you and you catch Evan's laugh carrying across the lot."

    menu:
        "Step closer and offer to teach the next knot":
            "You step in, your fingers clumsy at first. The child's face lights up and Captain Reyes laughs—a small, approving sound—and Evan watches you with the sort of quiet attention that warms your chest."
        "Let Evan take the moment; fetch more seedlings":
            "You move away to gather trays. Watching Evan teach from a distance feels like watching sunlight through glass—warm, refracted. Your chest brightens steadily, an ember instead of a spark."

    jump chapter12
    return
