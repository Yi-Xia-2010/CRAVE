label chapter1:

    # [Scene: Tideward | Morning]

    scene bg ch1_Start_1 at full_bg
    # play music "music_placeholder"  # [Music: Low, minor-key piano with distant gull calls]
    # play sound "sfx_placeholder"  # [Sound: Distant generator hum; the soft rattle of loose shutters]
    "You wake to brine and oil braided into the air—the smell presses against your throat before your eyes are fully open. Your field jacket is still damp from last night’s rooftop repair; the copper tips of"
    "your dark green-black hair have flattened against your forehead, a salty curl plastered to your temple. Tideward is half-asleep and half-alert, the way a tide is patient and relentless."
    "Light from the streetlamps is stalled behind a thin mist; the lamps themselves stutter, little electrical coughs in the fog. The ferry mural on the corner—painted years ago by someone who remembered the old routes—throws a"
    "perfect mirror of color on the puddled cobbles. Sea-glass green and rust reflect like a ledger of what’s been submerged and what is still visible."
    "You sit up and reach for the leather journal on the floor next to your mat. Its cover is the familiar, soft-scraped brown you’ve worn smoother than any map. Fingers trace the twine that keeps it"
    "closed, the same habit you had the morning after the shop was taken. Sixteen. The day the storm folded the block like paper and left our tools on a mudline. You remember the smell of diesel"
    "and wet wood and the small, honest heat of the repair stove your uncle kept in the back. That loss folded something into you—a duty that sits in your chest heavier than grief: map the high-tide"
    "routes, stitch the defenses, carry our stories so they don’t get flattened with the houses."
    "Outside, folders of half-dried flyers flap on a lamppost—mildew along their edges, glossy renders of elevated high-rises and glass promenades. Evelyn Harrow’s face is everywhere: immaculate, silver bob precise even under rain, steel-gray eyes on a"
    "thousand kiosks. The city calls it a plan; your neighbors call it a verdict. Your mouth tastes of salt and the day's first decision."
    "You sling the jacket over your shoulders. The patches are still damp; when you move, they whisper against each other—canvas rubbing canvas, the tiny mechanical music of people who still fix things by hand."
    # play sound "sfx_placeholder"  # [Sound: A metal clip snaps; footsteps on wet planks]
    "You step through the narrow lane where rope fences sag from porch to porch. Someone has strung a line of salt-tolerant scarves like prayer flags—the colors muted, beaten flat by weather and memory. Mira is a"
    "rhythm in the street even before you see her: the clink of seed packets in a thermos. She’s on her way to the rooftop garden, hair cropped close, a patchwork skirt swaying."
    show mira_soto at left:
        zoom 0.7

    mira_soto "Morning, Ava Marin. Council went long. I passed the community board—half the notices are already soaked through."
    show ava_marin at right:
        zoom 0.7

    ava_marin "They printed too many glossy pictures and not enough language that matters."

    mira_soto "They make it look like a postcard. Whoever designs those renders hasn't had to pump water out of a basement at two in the morning for a week.' (She laughs, but it's a small thing without mirth.) 'You okay? You look like you swallowed a storm."

    ava_marin "Just tired.' (Honesty tastes like iron. You remember Tomas at the dock, the way his hands move over a carburetor; you remember the shovel you sharpened last winter.) 'I was up on the roof till late. We patched the north span near the herb boxes. Might hold another season if we keep at it."

    mira_soto "You'll make a whole season out of stubbornness.' (She presses a seed packet into your hand. 'Keep it,' she says. 'For the archive.' Her face softens, careful.) 'Also—' (she leans in conspiratorially) '—there’s talk of a meeting at the pier this afternoon. People want to know what the maps mean."
    "You want to answer with certainty, because certainty is an action that can be planned and measured. But your chest tightens—guilt as automatic as breathing. The journal presses at your ribs where your shoulder bone meets your heart."

    menu:
        "Trace the ferry mural with your fingertip":
            "Your finger leaves a wet smudge over time-sanded paint. For a second the image shifts: the ferry seems to ride again, not on water but on the memory you're stubborn enough to hold."
        "Snap a quick photo with your phone":
            "The phone’s sensor struggles with the reflections; the saved image is sharper than your memory, sterile and small, like a relic in a museum. You tuck the phone away with a dull unease."

    menu:
        "Reply immediately: 'I'm on my way'":
            "Your thumbs type with habitual speed but your eyes water—whether from rain or the idea of letting something new enter our neighborhood. The message sends. You feel, for a breath, less alone."
        "Hold off—visit City Hall first":
            "You save the message and pull your jacket tighter. The reply sits like a possible detour; you tell yourself you need to see the maps and faces at City Hall before you commit. Responsibility doesn't like to be subdivided."

    menu:
        "Fold the flyer into your jacket and pocket it":
            "You tuck the glossy render between the lining and the patchwork inside your jacket, hiding it like contraband. The paper warms to your side, and your heartbeat matches the rustle of the cloth."
        "Leave the flyer where it is and take a deep breath of the promenade air":
            "You let the flyer lie. It flaps its resignation in the rain. You breathe in the cold, sharp air—salt and polished stone—and let it collect in your lungs like a promise of work."

    jump chapter2
    return
