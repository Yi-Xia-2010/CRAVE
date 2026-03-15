label chapter4:

    # [Scene: TideLab | Morning]

    scene bg ch4_453e40_1 at full_bg
    # play music "music_placeholder"  # [Music: Staccato strings with urgent percussion]
    # play sound "sfx_placeholder"  # [Sound: Distant gulls, the low whir of drone rotors, boots squelching in wet soil]
    "You chose action. The choice you made in the hall yesterday—no more waiting—hangs in the salt-scented air like a taut line. The team moves around that line: hands, tools, clipboards, a huddle of neighbors who have learned to translate worry into work."
    "Your field notebook sits inside your jacket like ballast. You open it only long enough to feel the paper—maps, notes, someone’s hastily sketched planting schedule. Then you fold it away and begin to hand out tasks the way you always hated hearing from other people: clearly, fast, without apology."
    show amaya_reyes at left:
        zoom 0.7

    amaya_reyes "Luka, stagger the flights. Start with Sector C—those subsurface channels change after the last high tide. We need the bathymetry before Jules starts reef placement."
    show luka_maren at right:
        zoom 0.7

    luka_maren "Sector C—got it. I can do a long run first, but power cycles on the newer sensors might hiccup in the fog. If I stagger, I can cross-validate with Jules’ footage."
    "You point to a wall map, trace the low flats with a finger that still smells faintly of diesel and seaweed. Volunteers—men and women who used to mend nets and barter for bait—lean in, sleeves rolled, palms smudged with salt-mud."
    "You find, with a small surprise, that giving orders suits you today. Your voice cuts through the chatter: who digs where, which seed bundles to the low flats, how to stagger oyster reef placements so the"
    "current won't wash the young beds away. The plan fits into the day like a new inlet slotting a stream—practical, necessary."
    # play sound "sfx_placeholder"  # [Sound: Drone whir rises; a clipped radio chime]
    "Luka taps his controller, amber eyes on the small screen, salt-bleached strands pressed behind his ear. The drone lifts, a tiny humming promise over the bay; you can feel the vibration through the floorboards. He grins, but it's a quick thing—part relief, part preoccupation."

    luka_maren "If I can map these channels clean, we can place the first oyster lines where they'll anchor the sediment. It'll blunt the surge in storm surges by—"

    amaya_reyes "By months, maybe years. Good. Make sure Jules tags the southern approach; Mateo and the boat team will ferry the seed bundles at low tide."

    luka_maren "Amaya—correction. If Voss ups their outreach, they might mobilize faster than us. I don't want to get us halfway through a site only to be pushed off."
    "You savor the weight of that no. You know you should say it more kindly; you know Luka wants to believe in compromise. You give a small, controlled nod."

    amaya_reyes "Then don't get halfway. We make the pilot resilient enough that interference can't erase what we plant."

    menu:
        "Tell Luka to accelerate the drone run":
            "You slam your hand lightly on the map table. 'Now. If the channels map now, we adapt faster.' Luka's fingers fly over the controller and the drone descends into a low sweep."
        "Tell Luka to calibrate twice":
            "You press the corner of your notebook between your thumb and palm, patient. 'Calibrate again. One bad sweep and we lose weeks. Be precise.' Luka exhales and begins a methodical preflight check, slowing the tempo but smoothing the margin for error."

    # --- merge ---
    "Continue to TideLab | Continuous — Field Prep"
    # [Scene: TideLab | Continuous — Field Prep]
    hide amaya_reyes
    hide luka_maren

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Boots, muffled laughter, the slap of gloves on tarpaulin]
    "Mateo stands near the door with a wooden crate of saplings. His hands, the same hands that used to haul nets before dawn, are mercifully steady. He catches your eye and the small pride there—fisherman learning to plan land again—passes like warmth."
    show mateo_reyes at left:
        zoom 0.7

    mateo_reyes "You remember when Abuela taught us how to tie those baskets? Seems weird to tie saplings instead of lobsters."
    show amaya_reyes at right:
        zoom 0.7

    amaya_reyes "Abuela would be pleased the baskets hold something that keeps the shore."

    mateo_reyes "You nervous, sis? Not like you."
    "You don't answer at once. The nervousness is a tight coil at your ribs—more a pressure than fear—but it isn't all yours. It hums with responsibility for the town, for the people who will drink the river water tomorrow, for a volunteer's daughter who learns to plant instead of play."

    amaya_reyes "I just don't want to break the thing we're trying to save."

    mateo_reyes "Then don't. We'll do it the way you say."
    "The team lines up at the boardwalk—mud under fingernails, sunburned necks, hair pinned back. You hand out seed bundles: mangrove saplings wrapped in jute, oyster spat in mesh. The town shows up in roofs and coats and weathered smiles. The day presses forward."
    # [Scene: Boardwalk | Midday — Planting Begins]
    hide mateo_reyes
    hide amaya_reyes

    scene bg ch4_453e40_3 at full_bg
    # play music "music_placeholder"  # [Music: Tempo quickens; layered strings and low brass]
    # play sound "sfx_placeholder"  # [Sound: Spade into peat, water sighing back into channels, distant drone buzz]
    "The planting is messy and perfect. Children trail the adults, learning the same knots and the same patience. A volunteer who used to dry nets now learns to gauge soil salinity by touch. You move between"
    "clumps like a conductor, hands never idle. Luka radios updates—clean swathes of mapped channel, a new reef placement marked—his words shot through with focus and the small pride he hides."
    show jules_park at left:
        zoom 0.7

    jules_park "Hey Amaya, your planting rhythm's contagious. Next thing you know, Mateo will be lecturing on sediment transport."
    show mateo_reyes at right:
        zoom 0.7

    mateo_reyes "Don't push it, Jules. I lecture about fish, not geology."
    "Your laugh is short. You can't afford to be light for long. At the edge of the plank, a neutral-blazered figure watches: a Voss rep with a clipboard. Behind her, someone hands out brochures that catch the light like promises in glossy cyan."
    hide jules_park
    hide mateo_reyes

    scene bg ch4_453e40_4 at full_bg
    "The brochure smells faintly of engineered citrus. The rep's smile is practiced, the kind that measures faces the way a survey measures land."

    "Voss Rep" "Good morning. Impressive turnout. Ms. Reyes? Corinne Voss sends her regards. We believe in protecting Marisol Bay—at scale. We'd like to offer opportunities to the workforce here."
    "Your mouth tastes like metal. You stare at the brochures, at the rendered seawall swallowed by a neat, authoritative caption, and the weight settles—this is the other future being proposed: efficient, large, and indifferent to some edges it will cut."
    show amaya_reyes at left:
        zoom 0.7

    amaya_reyes "Scale without consent is still a decision for us. What does 'opportunity' mean if it asks people to move?"

    "Voss Rep" "Relocation is seldom immediate. There are transition packages—training, guaranteed positions. Corinne's model preserves infrastructure and creates long-term employment."
    "You feel it then: the tightness becoming heat. The town is doing the small, messy work of staying alive—and a company is offering the clean arithmetic of efficiency. The standoff lines begin to etch themselves between the soaked planks."
    show tamsin_cho at right:
        zoom 0.7

    tamsin_cho "Ms. Reyes, I've been asked to monitor interactions. There's space for dialogue, but permits move quickly. The council is watching both sides."

    amaya_reyes "Watching won't save the flats, Tamsin. We need actions that keep people in place, not plans that move them."

    tamsin_cho "I know. I'm trying to balance—"

    "Voss Rep" "Perhaps there's a pilot we can fund jointly? A demonstration that will—"
    "You see the edges of compromise forming like a light that will only illuminate some people and leave others in shadow. You could speak softly. You could try to bargain. Instead, you feel your refusal coalesce into something harder—an unyielding stance that surprises even you."

    menu:
        "Step forward and challenge the Voss rep publicly":
            "You plant both boots on the plank and speak loud enough for everyone to hear: 'We will not be moved by glossy brochures.' A ripple of cheers rises; the Voss rep's smile tightens."
        "Signal Mateo to keep planting and address the rep privately":
            "You catch Mateo's eye and nod toward the flats, lowering your voice. 'Keep the line steady. I'll talk to her later.' Mateo nods, and the work continues while you walk toward the rep with measured steps."

    # --- merge ---
    "Continue to Boardwalk Edge | Afternoon — Escalation"
    # [Scene: Boardwalk Edge | Afternoon — Escalation]
    hide amaya_reyes
    hide tamsin_cho

    scene bg ch4_453e40_5 at full_bg
    # play music "music_placeholder"  # [Music: Low brass, an insistent drumbeat]
    # play sound "sfx_placeholder"  # [Sound: A distant siren, an official's voice amplified somewhere you can't see]
    "A volunteer's daughter—small, knees raw from play—stumbles on a hidden root. She comes to you first: tears, a scraped knee, salt and mud caked around the wound. Someone hurries a foil pack from a first-aid box. You kneel, hands going automatic—cleaning, bandaging, murmuring the easier things: bravery, stitches of encouragement."

    "Volunteer" "I'm so sorry. We moved too fast."
    "You feel the guilt like a stone dropped into a tide pool—ripples across everything. The day that began with productive fury now bears the bruise of real harm. The crowd calms around the child. Hands return to tasks, but your jaw clenches."
    "Then a phone buzzes in your pocket. The screen shows a terse message: PERMIT APPROVED—VOSS MARINE SOLUTIONS—COUNCIL FAST-TRACK. Your throat closes. The words are small and clean and they change the map: bureaucracy as a tidal shift."
    "You look up. The Voss rep's gaze finds yours and something razor-thin slides between her features and the practiced warmth. Her tablet flashes; a security van idles at the far end of the boardwalk like an unnecessary punctuation mark."

    "Voss Rep" "We expedite when necessary to protect critical infrastructure. Resistance delays protection."
    show amaya_reyes at left:
        zoom 0.7

    amaya_reyes "Protection for whom? Your plans push people out of place to save a port. We are protecting homes—lives. There is a difference."

    "Voss Rep" "Hard choices come with scale, Ms. Reyes. We will be efficient."
    "The security guard steps forward, polished boots on wet wood, badge reflecting a sky that is about to break."

    "Security Guard" "Ma'am. For safety and order, we need to limit unpermitted activity on the flats. There's a warning from the municipal enforcement office—demonstrations could escalate."
    "Your refusal solidifies. The sound of the tide behind you is suddenly louder, as if the bay itself is pressing. Faces in the crowd watch you: some with fierce trust, some with an edge of fear."
    "You can see Luka's jaw clench, the drone hovering now a silent eye above the map of your country."
    "Tamsin lingers a pace back, hands clasped around her tablet. Her expression stays complex—neither ally nor adversary can be read cleanly from the tight lines. She looks at the notice; then at you. You cannot tell what she will do."
    "Everything compresses into a tight, high note: the scraped knee, the fast-tracked permit, the security presence, the glossy brochures baited with jobs. Your chest feels raw with the responsibility you chose."

    amaya_reyes "If you force us to stop, you don't save this town—you erase the people who made it. We will not be targets of displacement."
    "For a beat, the wind catches the brochures and flaps paper like small flags. You watch the crowd divide into quiet clusters—some stepping forward, some holding back."
    "Your refusal has become a visible line in the sand. You are a bright target now: a woman in a field jacket among planting spades, leading a tide of people who prefer mud to moving."
    hide amaya_reyes

    scene bg ch4_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Crescendo—strings surge into a near-scream; percussion pounds]
    # play sound "sfx_placeholder"  # [Sound: Rain begins, swift and urgent; the hum of the drone rises sharply]
    "You feel the pulse of responsibility spike into a white-hot pressure. The standoff is no longer theoretical; it breathes and pushes against you. Guilt and resolve twist together until you cannot tell which will break first."

    scene bg ch4_453e40_7 at full_bg
    "You are visible. You are on the line. The town waits, the rain lands, and something decisive is about to be demanded of you."
    # [Page-Turn Moment]
    "The drone camera tilts down and records your face in the raw rain—eyes rimmed with salt, mouth set. People will see this image. Actions will follow."

    scene bg ch4_453e40_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter6
    return
