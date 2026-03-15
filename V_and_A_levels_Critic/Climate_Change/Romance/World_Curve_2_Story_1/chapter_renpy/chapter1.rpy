label chapter1:

    # [Scene: Tidebridge Harbor | Morning]

    scene bg ch1_Start_1 at full_bg
    # play music "music_placeholder"  # [Music: Soft, hopeful piano with distant gulls]
    # play sound "sfx_placeholder"  # [Sound: The slow slap of tide against pilings; a camera shutter clicks occasionally]
    "You should have been inside, making tea, checking the meeting notes. Instead you stand on a splintered pier, the coral-red strap of your analog camera digging into your palm as you lift it to your eye"
    "again. The world condenses into rectangles of salt-gloss: a sandbag line, a half-sunken blue lobster crate, the glassy lip of a tidal pool reflecting a smear of cloud."
    "The smell of peat and cold brine stings the back of your throat — peat, wet rope, and the faint smoke of a neighbor's stove. Your hair, sun-bleached and stubborn, falls a hair's width from your"
    "sea-glass streak when you lean, framing the shot. Your faded navy jacket is warm at the elbows where the patches have gotten softer with use. You inhale; the water's edge tastes like memory."
    "You don't take pictures because documentation is art. You take them because proof keeps people from forgetting. Proof is what you will hold up in the council chamber later, proof that the marsh is not just numbers on a screen but a living thing you could still stitch back together."

    scene bg ch1_Start_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Quiet click—shutter]
    "You step along the boardwalk, heel thudding into wet wood. Jun is rigging a line to a leaning shack, sleeves rolled, rope hands moving with the easy economy of someone who has spent too many dawns at sea. He looks up when you call his name."
    show jun_park at left:
        zoom 0.7

    jun_park "Ari. You're early. Figured you'd be running through the agenda again."
    show ari_tanaka at right:
        zoom 0.7

    ari_tanaka "I take pictures for an agenda. Different priorities."
    "(You let your mouth tilt; it's a practiced defense.)"

    jun_park "Hm. You should get Etta's seedlings—she says the salicornia took last night. Small miracles."

    ari_tanaka "Small miracles matter.' You lower the camera, the lens fogging a little from the cold. 'How's your boat holding?"
    "Jun's laugh is a tight, dry thing. He shrugs, the rope slack in his hands."

    jun_park "For now. Got a bigger job hauling sandbags today. Council's bringing supplies. Or... somebody's bringing supplies."

    ari_tanaka "That's the thing—'somebody' matters. We shouldn't let it be only big cheques and glossy pamphlets."
    "Jun's expression sharpens, then softens. He knows how much you keep inside."

    jun_park "You're always the one who says that. You ever think of letting anyone else carry something for once?"

    ari_tanaka "Only on days I dream of sleeping past dawn."

    menu:
        "Frame the marsh's eelgrass—low angle":
            "You crouch until your knees ache, lens skimming the waterline, catching the first thin blades of new growth."
        "Capture the pier from above—include the sandbags and tents":
            "You step back to a higher plank and take in the pier's patchwork—sandbags like teeth, tents like small islands."

    # --- merge ---
    "Continue to next scene"
    # [Scene: Etta's Greenhouse (The Nursery) | Mid-Morning]
    hide jun_park
    hide ari_tanaka

    scene bg ch1_Start_3 at full_bg
    # play music "music_placeholder"  # [Music: Soft strings under a low hum of insects in the grow-lamps]
    # play sound "sfx_placeholder"  # [Sound: Drip of condensation, the rustle of leaves]
    "You hang your jacket on a peg and the greenhouse breathes around you—humid, peppery, a sanctuary of green against the gray outside. Etta is bent over a tray of seedlings, fingers stained dark with soil. Her"
    "hair is a white halo; she looks like a lighthouse that wants to be useful."
    show etta_hargrove at left:
        zoom 0.7

    etta_hargrove "There you are. If you kept up that pacing, you'll exhaust yourself before the council meeting."
    show ari_tanaka at right:
        zoom 0.7

    ari_tanaka "I prefer to exhaust myself productively."
    "Etta chuckles, then grows serious, eyes flicking to a tray where half the plugs are paler than they'd been yesterday."

    etta_hargrove "We lost some last week. Salicornia is hardy, but the water's shifting too fast. We need those coir logs set right before the next tide. People are tired, Ari. There are only so many hands."

    ari_tanaka "We'll get people. We'll get the materials. Mateo said he had a sensor batch from the lab—low-cost, tide-aware. He wants to test them with our transects."
    "Etta's hands still."

    etta_hargrove "That boy… he carries the city with him sometimes. But he means well. I like that he comes back."

    ari_tanaka "He comes back with batteries and big ideas."

    etta_hargrove "That's as important as batteries, sometimes."

    ari_tanaka "He also has a tendency to promise things out loud before knowing which parts are his to promise."

    etta_hargrove "He promises with his hands. Sometimes that works."
    "The greenhouse smells sharply of citrus and wet earth; your palms pick up the faint grit of peat. You can't remember the last time you let someone take the lead without a spreadsheet and a dozen"
    "follow-up emails in your head. Letting Mateo test his sensors here feels like leaning on a neighbor's ladder—trusting, slightly terrifying."
    # play sound "sfx_placeholder"  # [Sound: Footsteps at the greenhouse door; a familiar rhythm]
    hide etta_hargrove
    hide ari_tanaka

    scene bg ch1_Start_4 at full_bg
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "Morning, everyone. Sorry I'm late—traffic, and then an extra hour swapping out a fin on the prototype."
    show ari_tanaka at right:
        zoom 0.7

    ari_tanaka "You nearly missed the miracle of the morning tide."

    mateo_alvarez "I live for miracles. And for data that looks like miracles.' (He sets down his satchel and carefully withdraws a row of small cylindrical sensors, each wrapped in rubber with a cheerful, home-printed label.) 'Low-power, open-source, and—Etta, I used your old tide charts to calibrate them."
    "Etta's mouth quirks. She reaches out, fingers lingering over the cool casings."
    show etta_hargrove at center:
        zoom 0.7

    etta_hargrove "You used my charts? Heavens. Little Mateo, you're a thief."

    "Mateo Alvarez (soft)" "Only of knowledge, Etta. I asked your permission."

    ari_tanaka "What do they do when they work?"

    mateo_alvarez "They listen. Pressure, salinity, a small accelerometer. We'll know exactly where the marsh is being scoured and when the currents change. If we can map that, we can decide where to put the next coir riffle without guessing."
    "You feel the word 'map' like a promise. Your chest loosens a notch—data that can point to action, not only warnings screamed into empty air."

    etta_hargrove "And how long until a town can read them?"

    mateo_alvarez "A week of tests, maybe. If the prototype stays dry and we don't fry the circuitry in a surprise storm.' (He glances at you, an apologetic smile.) 'If you'd let me drop a couple by the pier, I can get synched readings to—"

    ari_tanaka "Yes. We can do that. We'll need to coordinate with Jun and the dockspeople."

    mateo_alvarez "I'll bring spare casing. Also—' (He hesitates, hands tucked into his pockets) '—I brought extra coffee. I thought... town meetings need fuel from people who like bad coffee and a lot of opinions."
    "You find yourself laughing more easily than you'd planned."

    ari_tanaka "You read my soul."

    mateo_alvarez "That makes two of us."

    menu:
        "Tell Mateo about the seedlings' losses":
            "You lean in and tell him where the salicornia thinned—exact coordinates and a worried sentence about tidal scours. Mateo's brow tightens; he taps a note into his phone."
        "Keep the conversation light—ask about his lab day":
            "You let the anxiety sit in your chest and ask instead about his commute and the stubborn fin. Mateo relaxes and launches into a story about a colleague who glued a prototype to a conference table."

    # --- merge ---
    "Continue to next scene"
    # [Scene: Municipal Hall & Plaza | Late Morning]
    hide mateo_alvarez
    hide ari_tanaka
    hide etta_hargrove

    scene bg ch1_Start_5 at full_bg
    # play music "music_placeholder"  # [Music: Low, steady rhythm; a thread of anticipatory warmth]
    # play sound "sfx_placeholder"  # [Sound: Murmured conversations, a distant PA system tuning up]
    "The plaza smells of wet paper banners and someone's frying doughnuts; the municipal building faces the sea like a slow, patient observer. Booths line the square—some printed with corporate logos, others hand-painted with slogans. You see"
    "the familiar faces of neighbors, banners stitched by Etta's group, and a small, polished tent straddling the edge of the plaza where people in branded coats hand out glossy pamphlets."
    "Elio Sato's team moves with a tidy efficiency. A young representative with a tablet smiles, too bright against the washed light."

    "Representative" "Council consultations are important—have you signed up for a community briefing?"
    "You could roll your eyes. You don't. Not in front of the neighbors. Instead you hold your camera at your hip like a talisman."

    "Elio Sato (approaching)" "Ari. Good to finally meet you in person. Your collective's efforts are...visible."
    show ari_tanaka at left:
        zoom 0.7

    ari_tanaka "They're more than visible. They're alive. The marsh is not a line item."
    "Elio Sato inclines his head, expression open but precise."
    show elio_sato at right:
        zoom 0.7

    elio_sato "Of course. My firm is here to offer options. We want to prevent loss of life and provide stabilization—rapidly deployable measures. Think of it as buying time."
    "Your shoulders tighten in that old way—a familiar groove carved by night after storm. You are not opposed to buying time. You are opposed to buying time that costs people their homes."

    ari_tanaka "Time is useful when it's shared. We need solutions that keep people here, not push them to the edges."

    elio_sato "And if the edge keeps coming? We design systems that are equitable. We listen and we build."

    ari_tanaka "Listening should come before the blueprints."

    "Elio Sato (small, almost rueful smile)" "Agreed. Tell me where it appears otherwise. I grew up watching managed relocation unfold; it imprints you."
    "His voice does something complicated—an echo of loss underneath the corporate cadence. You can't tell if it's contrition or a memory turned into conviction."
    # play sound "sfx_placeholder"  # [Sound: A faint murmur of approval from a nearby cluster; Councilor Rosa watching, thoughtful]
    show councilor_rosa_menendez at center:
        zoom 0.7

    councilor_rosa_menendez "Elio, your team's presence is one piece. We will hear the community today. This meeting must include lived experience and technical assessment."

    elio_sato "Naturally."
    "You think of Etta's trays, of Mateo's sensors, of Jun's callused hands. You think of the photos on your camera: pale seedlings, hopeful flags, the sheen of wet wood. You press your fingers to the coral strap as if to anchor yourself."
    "Mateo Alvarez appears at your elbow, breathless, cheeks pink from the cold but eyes bright."
    hide ari_tanaka
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "I set two sensors at the northern sills. They beeped in a way that sounds promising. If these line up with the community's transects, we can show the council exactly how the marsh is changing."
    hide elio_sato
    show ari_tanaka at right:
        zoom 0.7

    ari_tanaka "Then let's make the council listen—with data and with faces."
    "Etta arrives behind you, a tray clutched to her hip, and hands you a folded leaflet she'd stitched together. Her hand brushes yours; for a heartbeat you feel the simple steadiness of being held up."
    hide councilor_rosa_menendez
    show etta_hargrove at center:
        zoom 0.7

    etta_hargrove "We have a little display in the morning room. You can show them your pictures, Ari. People respond to things they can touch."
    hide mateo_alvarez
    show jun_park at left:
        zoom 0.7

    jun_park "And I can tell my crew to bring the patched-up pier sections as a demo. Show them the labor."
    "The plaza hums around you—some voices hopeful, some skeptical. The arousal in your chest rises not into panic but into a contained warmth: a purposeful energy. It gathers like a small flame before a breeze."
    "Elio Sato returns to his group, giving a last, measured nod. His face is unreadable in the way of people who have practiced gentleness into efficiency."
    "You lift your camera one more time and take a final picture of the plaza: a tableau of mismatched tents, bright pamphlets, a stall with Etta's seedlings, Mateo's sensors already glittering in a sunbreak like tiny promises."
    hide ari_tanaka
    hide etta_hargrove
    hide jun_park

    scene bg ch1_Start_6 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The shutter's echo seems to slow time a little]
    "You tuck the camera back under your jacket and feel the familiar guilt press against your ribs—responsibility for neighbors who sleep with sandbags at their doors. It is heavy, but it no longer leaves you immobilized. It has become a thing you carry with plans and people."
    "Mateo Alvarez's hand finds yours, fingers warm."
    show mateo_alvarez at left:
        zoom 0.7

    mateo_alvarez "We can make this tangible. Data, seedlings, mouths in the room."
    show ari_tanaka at right:
        zoom 0.7

    ari_tanaka "And voices."
    "He nods. The meeting will need both."
    "You breathe, steady. Outside, the day is grey but not without light. The town is frayed but not defeated. There is work and argument ahead, and you will stand in them."
    "You glance at the municipal steps where people are setting up chairs. The highest point of the morning is a small, steady flare of hope built from mud and circuits and stubborn neighbors. You can feel the calm—focused and forward-moving—like the tide pulling in with intention."
    # play music "music_placeholder"  # [Music: Piano motif softens into a held, warm chord]
    hide mateo_alvarez
    hide ari_tanaka

    scene bg ch1_Start_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant church bell marking the hour]
    "You step toward the municipal steps, the meeting list snug in your pocket, notes folded and annotated in your handwriting. You are ready—ready to show the town what the marsh looks like through the lens and through the numbers, ready to ask them to choose stewardship over surrender."
    "A thought anchors itself: this is where threads begin to stitch together—the sensors and the seedlings, the data and the hands that move the coir. It's small, not yet a solution, but it is tangible. It's the sort of thing that becomes a story if you tell it right."
    "You inhale the cold air sharply, feeling the low rise of something hopeful in you. The day has baked a small, patient optimism into its center. You tighten your grip on the camera and start up the steps."

    scene bg ch1_Start_8 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Distant church bell marking the hour]
    "You step onto the municipal steps, camera against your chest, and for a breath everything narrows—your duty, the faces in the crowd, the faint beep of an incoming sensor signal on your phone. The next hour"
    "will be dense with words, with negotiation, with small clarities that feel like victories. You already know: this meeting will not settle everything. But it can set the direction."

    scene bg ch1_Start_9 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    jump chapter2
    return
