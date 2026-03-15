label chapter10:

    # [Scene: Transitional Housing Compound | Early Morning]

    scene bg ch10_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Soft, rising strings with a steady, hopeful rhythm]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls; the clank of a rope; a low diesel generator humming steady]
    "You wake before dawn, the compass heavy in your pocket like an obligation you've chosen to carry. Outside, the compound smells of fresh-cut lumber and the sharp tang of sea. Volunteers move between units with boxes"
    "and tea, their breath fogging the air. The first tranche of families arrived last night—some slept, some counted the seams of old quilts until sunrise—but all of them are here, above the high-tide line for the"
    "first time in years."
    "You check the roster on your tablet, eyes running along a map you've redrawn a dozen ways until it becomes a workable geometry: vulnerability scores layered over cultural nodes, paths to cluster sites intended to keep neighbors together where possible. The logic is clinical. The work is intimate."

    scene bg ch10_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A child's laugh; a box lid thump]
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "You're early."
    "He appears by the stairwell, cap tucked low, rope sling over his shoulder. His voice is rough with sleep and concentration."
    show maya_armitage at right:
        zoom 0.7

    maya_armitage "Couldn't sleep. Too much to check."
    "You meet him on the steps, the paper map rolling slightly in your hands. 'How did the boats hold up last night?'"

    jonah_reyes "Good. Slow and steady. We ferried the last family across at three, kept the gear dry. Rafi rigged tarps over the food crates; he always forgets his flashlights but remembers the important things."
    "He gives a small, wry smile that doesn't erase the tiredness around his eyes."

    jonah_reyes "Listen—I've rerouted the launch for the midday run. If we move those garden beds first, the elders will have something familiar to tend in the cluster. Keeps hands busy while forms get signed."
    "He taps the map where the community garden could be rebuilt within the cluster site."

    maya_armitage "Yes. Keep the beds at the front—visible. I'll make sure the allocation forms have a line for communal plots."
    "You feel the motion of efficiency settling in—paperwork, logistics, small acts that add up to safety. 'And Jonah—thank you. For the boats. For staying.'"
    "Jonah Reyes:"
    "He looks away, jaw working."
    "'You don't have to thank me every time you file a report about my boat. We're in this together.'"
    "There is softness threaded through his practical tone; an invitation to stay close that he won't explicitly name."

    maya_armitage "I know."
    "You say it because it's true, because the word is a small raft you both can hold."
    "You go through the motions: sign the temporary tenancy agreements, initial the inventory checklists, stamp the boxes headed for storage. Each signature is another small lifeline thrown across a widening tide. Families cluster in doorways, holding photographs and one or two cherished items. You learn names by listening."

    menu:
        "Offer to carry the box for an elder":
            "You step forward and lift a heavy box, feeling its slant of weight—old frames, a jar of preserved lemons, a folded tablecloth. The elder smiles, fingers brushing your knuckles as if to pass on a benediction."
        "Let the elder keep carrying; offer coffee instead":
            "You hand over a steaming cup and sit with them on the steps. They unwrap a memory in a quieter way, telling you about the tides as if they were people you'd both grown up with."

    # --- merge ---
    "The scene transitions to the Reclaimed Marsh Restoration Site | Mid-Morning"
    # [Scene: Reclaimed Marsh Restoration Site | Mid-Morning]
    hide jonah_reyes
    hide maya_armitage

    scene bg ch10_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: Light piano with wind-harp textures; the tempo lifts]
    # play sound "sfx_placeholder"  # [Sound: Water lapping gently; the metallic scrape of a spade]
    "At the marsh, volunteers kneel in mud, packing reeds into the soft bank. The work is slow and meditative—hands remember how to coax life back into damaged ground. You stand at the water’s edge watching a"
    "pair of kids tuck seedlings in a neat row, their laughter sharp and absurdly hopeful against the soft sussuration of reeds. Each stalk is a promise: habitat returns, buffers rebuild, memory is planted into living soil."
    "Gracie Nan approaches along the raised boardwalk, her steps measured. She wears her bright kerchief despite the morning, a flag of stubbornness."
    show gracie_nan_armitage at left:
        zoom 0.7

    gracie_nan_armitage "I saw some of the boxes come through last night. You've done what you could, child."
    "Her voice is roughened but not unkind."
    show maya_armitage at right:
        zoom 0.7

    maya_armitage "We put the first families into transitional units, Nan. The funding came through quicker than we expected."
    "You try to keep your voice even, because the good news is fragile in her hands. 'We prioritized the most exposed, and—'"
    "Gracie Nan:"
    "She holds up a hand."
    "'I don't need the list, Maya. I need to know where my sister's stone will be. Where the old birch was. You can't put a quilt in a calculator and call it a shore.'"
    "Her knuckles white around the rail."

    maya_armitage "We're setting aside memorial plots—reedbeds as markers, not erasures. We want to replant the promenade's lost corners near the cluster gardens where people can gather. The reedbeds will be a living boundary and a record."
    "You step closer, lowering yourself to meet her eyes. 'We will mark ancestral plots. We are not erasing them.'"

    gracie_nan_armitage "You speak like a scientist for the town it's not yet, and like a neighbor when it suits you."
    "It's sharp and fair."

    maya_armitage "I promise we'll put her name on the marker. And we'll hold a planting the whole town can come to. We'll do it right, Nan. Not with gloss—real. We'll dig with hands."
    "You want to mean it with all the weight of the maps you carry."

    gracie_nan_armitage "Then dig, child. But remember—names are heavy too. They'll need soil to hold them."
    "Her mouth twitches; something like concession and worry both."
    "You stand together at the marsh edge, sandals sinking into mud, reed tips brushing your palms. It is a small, precise ritual of making: you assign plots, schedule the communal plantings, and draft a plaque list."
    "The day feels like a raising—of soil, of standards, of a new way to honor loss without being consumed by it."

    menu:
        "Write Nan's sister's name on the first marker by hand":
            "You find a stick and, with your palm shaking slightly, scratch her name into wet clay. The letters are imperfect but honest, and Nan's eyes drift to a place you can see their shape is steadier for it."
        "Propose a community inscription ceremony instead":
            "You set the plan on paper: a night when all hands gather. Nan's mouth softens, and she nods—shared grief becomes less sharp when carried together."

    # --- merge ---
    "The scene transitions to the Cluster Site — Rebuilt Garden | Afternoon"
    # [Scene: Cluster Site — Rebuilt Garden | Afternoon]
    hide gracie_nan_armitage
    hide maya_armitage

    scene bg ch10_453e40_4 at full_bg
    # play music "music_placeholder"  # [Music: Harmonic strings swell into a warm chord]
    # play sound "sfx_placeholder"  # [Sound: Voices overlapping—plans, jokes, the scrape of soil against wood]

    "By midday the cluster garden is a hub. Children chase each other along the walkways while adults talk in lower voices about work shifts and school routes. There are hand-painted signs" "Seed Swap Today,' 'Nan's Tea at Four."
    "A family you helped relocate—two parents, a teenage boy with a chipped tooth, and a grandmother wrapped in a floral cardigan—approach as you inventory a crate of tools. The father holds a photograph in a plastic sleeve, the edges softened by years of handling."

    "Father" "We wanted to say thank you."
    "His voice is matter-of-fact, as if politeness is a tool learned in the same ways as hammers."
    show maya_armitage at left:
        zoom 0.7

    maya_armitage "You did all the heavy lifting. We just pushed the boats the last mile."
    "You force a lightness into your voice because grief can be worn like weather and practical warmth is needed."

    "Mother" "It's quieter here, in a good way. Last night we slept without the sound of water in the windows for the first time in—"
    "Her voice breaks, and the boy looks down, fingers worrying a shoelace."

    maya_armitage "Good. Keep us posted about the fridge—Rafi says the solar panels will be installed by Thursday. And if you need help with the paperwork—"
    "You gesture toward a clipboard and the list that never ends."

    "Grandmother" "Your hands were steady with the forms. Thank you for holding the lines."
    "There is gratitude and a small, weary relief like a harbor turning its face to a lighthouse."

    maya_armitage "Thank you for carrying your memories with you."
    "You mean it, though the words feel small."
    "They walk away with their crate and photograph. You tuck that image into the box marked 'relocation' for inventory—an act that makes your chest feel oddly vacant. The photo is a tab of intimacy you put"
    "aside for safety. You are efficient and gentle, and you wonder if the gentleness can be enough."
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "You did good with them."
    "He comes up behind you, voice low."

    maya_armitage "We did it together."
    "You want to push back at the hollowness. You want to stitch meaning into boxes."

    jonah_reyes "Still—don't let the paperwork be the only way you remember people."
    "He says it quietly, almost a plea."

    maya_armitage "I won't."
    "You feel the truth of that promise settle like a stone that wants to become a seed."
    "Across from the garden, the abandoned promenade gapes—boarded storefronts and ghost blocks where laughter used to hang from awnings. The tide line graffiti is a map of old griefs. Even as the town rises in practical"
    "terms, the promenade's emptiness is a ribbon of absence that will take time and work to repair."

    menu:
        "Walk the promenade at dusk and leave a seed packet at each shuttered door":
            "You spend the evening slipping small envelopes into mailbox slots—tiny acts of faith. When you return the next morning, a few doors have tags: 'We'll take watermelons next month.' It is a small, ridiculous hope, and it lands."
        "Organize an evening town meeting to discuss activating ghost blocks":
            "You draft a flyer and pin it to the temporary noticeboard. The crowd that shows is small but earnest; plans are sketched in grease pencil. The future feels participatory—messy but alive."

    # --- merge ---
    "The scene transitions to the Promenade Overlook | Sunset"
    # [Scene: Promenade Overlook | Sunset]
    hide maya_armitage
    hide jonah_reyes

    scene bg ch10_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: A single clarinet line over warm strings; harmonies resolve upward]
    # play sound "sfx_placeholder"  # [Sound: The distant murmur of an evening market; someone hammering a sign]
    "You climb the overlook as the sun goes down, the weight of the day pulling at your shoulders in a way that is both heavy and satisfying. The staged geometry of the cluster sites gleams with"
    "new roofs and reorganized life. The reedbeds at the marsh lean like a newly planted chorus, their tips catching light. Families sit on steps eating donated stew, children trading seeds as if currency."
    "You take the box labeled 'relocation' from the inventory table—a simple cardboard vessel stamped with a logistical code. Inside: framed photographs, a child's stuffed fish, a sewing kit, a spooled rope that once tied a boat."
    "You hold a single family's photo in your palm. Their faces are bright against a smudged shoreline. For a second you feel the old, impossible wish swell: to keep everything exactly as it was."
    "You breathe and let it go. The tide has taken some things in its own time. You are trying to teach the town to keep what needs keeping while making room."
    show gracie_nan_armitage at left:
        zoom 0.7

    gracie_nan_armitage "You moved the Hartmans across from the old chip shop?"
    "She joins you, hands clasped behind her back."
    show maya_armitage at right:
        zoom 0.7

    maya_armitage "Yes. They wanted to stay near the market. We found a unit close to the cluster garden so their daughter can keep the stall."
    "You say it plainly."

    gracie_nan_armitage "That will help."
    "Her eyes sweep across the promenade. 'It will never be exactly the same. But maybe it will be something different you can live with.'"
    "She taps the railing once."
    "You stand in the amber light and feel the rise that runs through the town not as a miraculous repair but as a steady climb—pragmatic, necessary, and fragile. Funding flowed, boats moved, beds grew. Lives have"
    "been protected. The cost is real—empty blocks, rearranged rituals, nights when people count the seams in their quilts instead of the stars."
    "Yet, as the sun lowers, you spot a boy planting a sticker on a shutter that says, 'Seed Bank Here' with a grin. A neighbor hangs newly mended bunting between two straighter posts. A woman who"
    "lost her porch last month sits in a communal circle, teaching seedlings how to root."
    "You feel something in your chest that is not relief alone. It is resolve—an energetic lift that tells you this is work you can do and must continue."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "We made it through today. That's something."
    "He reaches out and taps your hand—the gesture small, but steady."

    maya_armitage "It's the first step of many."
    "You look at him, seeing both the tiredness and a hint of a future where you both keep building. 'Tomorrow, we start the education program. And the memorial planting at the marsh is on Saturday.'"

    gracie_nan_armitage "Then we'll plant with our hands."
    "There is warmth in her words now, acceptance braided with cautious hope."
    "You put the photograph back into the box and close the lid with a soft thud. The label reads: RELOCATION — HARMIT. You tape it shut with an economy born of necessity and tenderness. The gesture is both administrative and intimate."
    "You look out at the town you've helped steady—an imperfect architecture of care. You imagine the patchwork of futures you will stitch: reedbeds like stitched names, cluster gardens humming, a promenade that becomes a corridor of"
    "small businesses and memory markers. The models on your tablet cannot fully capture what is happening here; spreadsheets make way for hands digging and neighbors teaching neighbors how to hold on together."
    "You feel the rise—pragmatic, communal, tentative—and it fills you with a steady warmth. There will be ghosts to mourn. There will be rituals to rebuild. But for now, lives are safer. People have roofs. Funding moves in time to what matters. The town breathes easier than it did."
    "You run a thumb along the seam of the tape and think of the next thing to unbox—education plans, legal affidavits, the long list of sundries for a community that is learning to be mobile and"
    "rooted at once. The checklist waits, and beyond it lies the harder work of turning these provisional shelters into a place people can call home without feeling like they've given up the past."
    "You inhale the salt air, and the note at the back of your throat steadies. There is a future you can aim for: patchwork and hand-stitched, messy and alive. It will require more hands, more patience, and a willingness to name what is lost while tending what remains."
    hide gracie_nan_armitage
    hide maya_armitage
    hide jonah_reyes

    scene bg ch10_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter11
    return
