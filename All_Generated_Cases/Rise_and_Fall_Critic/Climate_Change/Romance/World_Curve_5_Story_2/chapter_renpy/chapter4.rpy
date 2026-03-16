label chapter4:

    # [Scene: The Helix | Late Morning]

    scene bg ch4_453e40_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low hum of grow-lamps, the distant gull-call of the harbor, laughter and measured footsteps on the deck as volunteers move crates.]
    # play music "music_placeholder"  # [Music: Gentle arpeggio on piano, rising with an optimistic swell]
    "You step into the Helix carrying a crate of marsh-sedge plugs and a paper folder full of sticky, handwritten promises — fundraising tallies, volunteer rosters, Jun's annotated model printouts. The air smells of damp peat and"
    "warm cedar, and your fingers still hold the faint grit from the boardwalk. For the first time since the meeting, the trajectory feels less hypothetical and more like something you can touch."
    show aria_solen at left:
        zoom 0.7

    aria_solen "Okay—let's make sure the labeling's waterproof. Marta, Jun, you good on placements for Cell A and B?"
    show marta_quin at right:
        zoom 0.7

    marta_quin "Labels are laminated. I tied the packets to the trays myself. Cell A goes where the current slows; Cell B takes the brunt of the ebb. People remembered Rafi's sketches, we put them to use."
    show jun_park at center:
        zoom 0.7

    jun_park "Sensors are calibrated. Salinity probes are online. If we stagger plantings across the next two tide cycles, we can observe sediment accretion differences without disturbing fish lanes."
    "You watch them work and feel the steadiness of real labor—hands pausing, comparing, retying knots—turning plans into salt-streaked motions. Eli appears at the doorway with a thermos and a grin that softens the room like a tide pulling back."
    hide aria_solen
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "You look like someone who needs a sip. And maybe a victory cookie. The Helix bakery outdid itself."
    hide marta_quin
    show aria_solen at right:
        zoom 0.7

    aria_solen "Is that a scientific claim?"

    eli_navarro "Everything's scientific if you measure smiles per crumb."
    "You laugh and take a cup. Your shoulders, which have been weighed by a year of bureaucracy and grief, loosen an inch. Eli's presence—unsentimental, reliably warm—feels like a lever at the fulcrum of the day."

    menu:
        "Hand Eli the clipboard and let him rally the volunteers":
            "You pass him the clipboard. He takes it with the same confident, improvisational ease he uses to steer the Helix, and within minutes the volunteer cluster becomes a coordinated chain of hands—pots, ties, boats. He calls out tasks like a captain, and you watch momentum knit itself."
        "Keep quiet and double-check the sensor network":
            "You tuck the clipboard under your arm and crouch by the table with Jun. Together you run sensors and cross-check battery life. The process is quiet, precise; in the hum of monitors you feel competence settle like ballast."

    # --- merge ---
    "The decision you make here doesn't rewrite the day, but it shades the rhythm: either the room's noise swells into a collective song under Eli's direction, or your small, exacting checks keep the technical backbone uncompromised. Either way, the Helix hums forward."
    # [Scene: Boardwalk Outside the Helix | Noon]
    hide jun_park
    hide eli_navarro
    hide aria_solen

    scene bg ch4_453e40_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slap of canvas sails, the soft scrape of oars, chatter in various cadences as neighbors coordinate; gulls wheel and cry overhead]
    # play music "music_placeholder"  # [Music: Upright bass and brushed drums—steady, forward-driving]
    "You ride the skiff out with a crew of neighbors: Marta balancing a stack of laminated instruction sheets; Jun with a waterproof vial of cultured marsh seeds; a couple of teenagers from the market brandishing old"
    "nets turned into planting tools. Each face is a map of stakes—lines of sun, worry, hopeful impatience."
    show marta_quin at left:
        zoom 0.7

    marta_quin "Remember: these are modest cells. Small wins build trust. One good season and people start to reimagine the shoreline."
    show aria_solen at right:
        zoom 0.7

    aria_solen "Yes. We don't promise the moon. We promise a stitch. Maintenance rotations, clear governance, shared labor credit—Jun and I have drafted it."
    show jun_park at center:
        zoom 0.7

    jun_park "And sensors will give us the data to ask for more. Evidence is what persuades Lina and quiets the skeptics. If accretion curves upward in six months, the narrative changes."
    "You slide the first buoyant frame into place, fingers numb and sticky with mud. The marsh plugs sink with a soft, satisfied slurp. A volunteer—someone you met handing out flyers—lets out a small whoop when a mat holds course against the current. The sound spreads, unexpected and bright."

    "Eli Navarro (from the aft)" "Look at that. People cheering a mat of grasses. That's a line in the sand, Aria—not against people, just against forgetting how to tend this place."

    aria_solen "That's what we've been trying to say. This isn't about stopping all change—it's about deciding what kind of change we let into our home."
    "You tighten the last knot, taste brine on your lips, and feel an internal click: the corridor is no longer just a plan. It's a motion, a gathering of hands and risk, and your role has shifted from solitary architect to convenor of a living venture."
    # [Scene: Old Pier Market | Afternoon]
    hide marta_quin
    hide aria_solen
    hide jun_park

    scene bg ch4_453e40_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Conversational buzz, the rattle of a camera, Marta's voice bargaining for space; the scent of smoked fish and frying dough.]
    # play music "music_placeholder"  # [Music: Piano returns, a bright motif layered with a folksy mandolin]
    "You stroll the market with a tray of small reed-star pins—each given to people who signed up to maintain a cell. The gesture is small, tactile: paper and thread into the palm. People press hands to"
    "their chests when you explain what the pin means. Trust is a thing you can sometimes see in the tightening of someone's smile."

    "Volunteer #1" "If this works, can we teach other neighborhoods?"
    show marta_quin at left:
        zoom 0.7

    marta_quin "We'll write a how-to, and we'll sell seedlings at cost. This is for everyone."
    # play sound "sfx_placeholder"  # [Sound: A reporter's voice—polished but not hostile—drifts across the boards. Cameras angle toward your group. Jun shrugs like it's routine; you feel the heartbeat of attention quicken under your ribs.]

    "Reporter" "Aria Solen, can you summarize what the pilot aims to prove for the council and for people here?"
    show aria_solen at right:
        zoom 0.7

    aria_solen "We want to show that community-led living-shoreline cells reduce erosion, create habitat, and offer livelihoods—without displacing the people who have stewarded these places for generations. We can prove it with data and with sustained care."

    "Reporter" "And the funding? Can a grassroots campaign sustain something measured by scientific outcomes?"

    aria_solen "It starts community-funded, yes. But our aim is to grow into a hybrid model: local stewardship matched with selective grants, clear governance, and transparency. People keep rights to their means of living—no top-down erasures."
    "The reporter nods, apparently satisfied, and the interview circulates in fragments across a small cluster of phones. You see Eli in the background, sleeves rolled, tying down a tarp with the same patient speed he uses when patching a leak."

    menu:
        "Step closer to the camera and name a volunteer training date":
            "You lean forward, voice steady, and announce a community training day in two weeks. Murmurs of availability ripple through the crowd like a plan made tangible. People mark calendars with their thumbs."
        "Defer and point the reporter to Jun for the timeline":
            "You nod and gesture to Jun, letting him lay out the measurement timeline. His technical specificity reassures a different set of ears—grant officers and Lina watchers—while you keep listening to the market."

    # --- merge ---
    "Both choices seed confidence; one binds the community tighter in schedule, the other reinforces the scientific scaffolding that will protect the work from cynical appraisal. You choose what aligns with the rhythm you're trying to build—trust in hands or trust in data—and either way, the Helix's work becomes more visible."
    # [Scene: Helix | Late Afternoon — After the Market]
    hide marta_quin
    hide aria_solen

    scene bg ch4_453e40_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low conversation, the soft beep of a laptop, the creak of a bench as someone shifts to listen]
    # play music "music_placeholder"  # [Music: Piano motif resolves into a warm chord; light strings add optimism]
    show jun_park at left:
        zoom 0.7

    jun_park "Early readings show a slight reduction in near-shore turbidity where the mat held. It's not definitive, but it's the kind of signal we hoped for."
    show marta_quin at right:
        zoom 0.7

    marta_quin "And people came. You could feel that. Old Man Rafi fetched his grandchildren down here. He hasn't sat this close to the water with them in years."
    show lina_voss at center:
        zoom 0.7

    lina_voss "Council was watching. I—' (she looks at you) '—I advocated for more eyes on this. Not just as optics. As a genuine pilot. If we can pair this grassroots muscle with measured support, it's a model."
    "Lina's words carry weight. For weeks you've navigated her middle-ground pragmatism—sometimes maddening, sometimes necessary. Hearing her say 'genuine pilot' feels like a small public reframe: your work acknowledged, not sidelined."
    hide jun_park
    show eli_navarro at left:
        zoom 0.7

    eli_navarro "You did this. You pulled them together—slowly, one stitch at a time. I know you don't like the spotlight."
    hide marta_quin
    show aria_solen at right:
        zoom 0.7

    aria_solen "I don't. But I like when people are safer. When hands remember their place in the work. That—' (you tap the battered notebook at your belt) '—that was the plan."

    eli_navarro "And you didn't have to do it alone, if that's what you're thinking."
    "His sentence hangs there, soft and heavy. It's not a question exactly—more an invitation to allow the scaffolding that people like Eli and Marta offer. You feel the old reflex: you can hold everything if you keep building. But today there are others holding the beams."

    aria_solen "I know. And... thank you. For the cookies, for the crate hauling, for saying it plainly.' (you smile, small) 'We need to mark the Helix as a hub. A place where people can come with questions and supplies."

    eli_navarro "Then we'll repaint that old sign. Call it a meeting place for volunteers. And I'll sketch up a rota board you can actually read."
    hide lina_voss
    show marta_quin at center:
        zoom 0.7

    marta_quin "And I'll make a ledger for labor credits and seed exchanges. No one loses out because they can't afford time."
    hide eli_navarro
    show jun_park at left:
        zoom 0.7

    jun_park "I'll make sure the sensors can prove 'community joy' as a metric if you want."

    marta_quin "Jun, that's how we get a grant."
    "The laughter settles in the air like a shared tide. The Helix feels less like a temporary experiment and more like a pivot point — a literal place to regroup when storms come, a social infrastructure as much as an ecological one."
    # play sound "sfx_placeholder"  # [Sound: A distant cheer from the boardwalk; someone calls your name. Your phone buzzes with a headline from a local outlet that ran a feature overnight—"Small-Scale Shoreline Trials Win Hearts, Eyes on Council." The snippet is kind. For the first time in months, a public narrative tilts toward your line of work and the people who sustain it.]

    menu:
        "Open the article aloud and read it to the group":
            "You tap the screen and read the lines. Applause and smiles answer each positive phrase. The room takes on a buoyant energy—mismatched mugs raised in a mock toast to a story that names their labor."
        "Put the phone away and let everyone keep working without the distraction":
            "You shutter the phone, tuck it into your pocket, and gestures send people back to small tasks. The momentum is practical and quiet: hands returning to pots, knots being retied, the work continuing without the brief high of being quoted."

    # --- merge ---
    "Both acts are small rituals of leadership—celebrate the recognition, or keep grinding while it is fresh. You choose the kind of momentum you want to foster in the Helix today: visible morale or steady discipline. Either choice is not about ego; it's about what keeps the long game honest."
    # [Scene: Helix | Dusk]
    hide aria_solen
    hide marta_quin
    hide jun_park

    scene bg ch4_453e40_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The distant slap of boat hulls, a low, satisfied murmur; the Helix vents sigh gently as humidity regulates]
    # play music "music_placeholder"  # [Music: Single piano note sustained, then a measured cadence—hopeful and steady]
    show lina_voss at left:
        zoom 0.7

    lina_voss "I filed a brief for a council motion to recognize the pilot as an official trial. If you keep this momentum and the data holds, I think we can move a recommendation that includes co-op governance."
    show aria_solen at right:
        zoom 0.7

    aria_solen "That would change how the council frames resource allocation. Jun—do we have a suite of metrics that can be presented in a month?"
    show jun_park at center:
        zoom 0.7

    jun_park "We have baseline salinity, turbidity, and a protocol for biological surveys. With community-maintained sensor arrays, we can show trends within thirteen weeks. It's not overnight, but it's defensible."
    hide lina_voss
    show marta_quin at left:
        zoom 0.7

    marta_quin "People will show up for that. They'll bring stories; they'll bring meals while we work."
    hide aria_solen
    show eli_navarro at right:
        zoom 0.7

    eli_navarro "And we'll need to be ready for outside attention. If a bigger outlet comes—if they want a visual of 'community saving the shore'—we ask them to show our terms. No extractive hero narratives. We tell the people's story."
    "You feel the day's energy fold into a new layer: not just pilots and cells, but a governance argument in the making. Trust and evidence braided together like the ropes Eli uses to secure the skiff. The room is small but deliberate; it's a knot that could hold."
    hide jun_park
    show aria_solen at center:
        zoom 0.7

    aria_solen "We did the first stitch today."

    eli_navarro "Then let's keep stitching."
    "Outside, clouds gather low on the horizon—silver-edged, not yet menacing, the kind that often come before the island's temper turns. The sight makes your chest tighten for a second; a practical alert flickers up the back"
    "of your neck. But the tightening doesn't feel like dread so much as a boxed, useful readiness. There's confidence in having others at your side."
    "You close your battered notebook and trace the pressed marsh grass between the pages—a small, private ritual of anchoring. The Helix hums around you: a place of light, hands, and growing data. For the first time in a long while, momentum feels durable rather than brittle."
    # play music "music_placeholder"  # [Music: A rising, bright motif—hopeful, forward-moving]
    "The evening stretches ahead like a turned page. You think of the council, of Lina's tentative support, of Jun's tentative graphs, of Marta and her ledger, and of Eli—steady at the prow of the small things"
    "that make people's lives safer. The corridor is not fixed yet, but the town now moves with you. Momentum exists; trust has started to root."
    "You step outside onto the boardwalk and watch the Helix's light ripple across the water. The horizon is a line of possibility."
    hide marta_quin
    hide eli_navarro
    hide aria_solen

    scene bg ch4_453e40_6 at full_bg
    # play music "music_placeholder"  # [Music: Motif holds, then softens]
    "There is a larger wind gathering somewhere beyond the line, a test you can almost feel as a shift in the air. It promises a trial of what you've sewn together — a measuring of how"
    "living systems and community governance hold under pressure. But tonight, the wind is only a rumor. For now, the town has chosen solidarity; hands are joining; data is coming in; the Helix is a hub."
    "You breathe in salt and cedar, and the sense of rise swells: small victories, stitched trust, the quiet turning of many hands toward something collectively worth sustaining."

    scene bg ch4_453e40_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter5
    return
