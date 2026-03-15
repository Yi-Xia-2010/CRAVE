label chapter6:

    # [Scene: Promenade | Late Afternoon — Storm Approaching]

    scene bg ch6_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A distant, building roar of surf; gulls cry, cut off by wind.]
    # play music "music_placeholder"  # [Music: Tense strings with a low, tidal percussion]
    "You stand with Jonah near the patched railing, the salt smell sharp enough to sting your throat. The engineered berms—those long, angled ridges of sculpted earth layered with planted marsh grass—look smaller against the sky than"
    "they did on paper. Between each berm, the living terraces slope down like ribbed steps designed to slow and soften energy. Volunteers move like constellations below, tethered to radios and headlamps."
    "Your palm rests on the brass of your watch; the tide line etched there feels like an accusation and a promise at once. You can feel the city's attention like weight at your shoulders—the mayor's press"
    "release, the donors, the contractors waiting for outcomes. You remember the clauses you fought for: monitoring, staged rollouts, transparency. You remember the compromise that let NovaSeis's licensed sensors into the network because scale needed their feed."
    "The thought sits in your mouth like metal."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "Sensor array three is reporting jitter, but it's within tolerances. NovaSeis pinged the cloud—says it's a firmware switchover. They pushed an update this morning."
    "You watch the display as wave height models begin to spike. The holographic coastline that once pulsed quietly now shudders with the storm's brute geometry."
    show mara_ellis at right:
        zoom 0.7

    mara_ellis "You want to trust the clause, the legal teeth you insisted on. You also want to trust Jonah. Trust feels different when it's measured against the sea."
    "Maya, moving up the boardwalk with a volunteer tarp, meets your eye and gives a hard nod. Old Mate stands a few planks away, hands curled into his cap, his face a map of lines that have read tides for decades."
    show mateo_old_mate_alvarez at center:
        zoom 0.7

    mateo_old_mate_alvarez "This storm's pushing more north. The channel 'tween ward blocks—it's narrower than models said. Watch the reflections."
    "Jonah looks toward the mouth of the channel and then back at the readouts."

    jonah_reyes "If the berms reflect more energy than we allowed—if the geometry's off—it could focus in ways the model didn't capture."
    "You bite the inside of your cheek. Models are always approximations; lived memory is a ledger of what the numbers miss."

    menu:
        "Run a manual buoy check":
            "You peel off toward the tide buoys with Jonah at your heels, rain starting to hiss. The buoys squeal as you tighten clamps; you taste salt and adrenaline. It buys you ten minutes of clarity."
        "Help Maya coordinate evacuations":
            "You shoulder into the volunteers, your voice cutting the wind as you direct people up Mosley steps. Hands grip yours—warm, frantic. You feel useful, alive, and a little further from the instruments that decide policy."

    # --- merge ---
    "Scene continues"
    "Jonah's hand stays briefly over yours—steady, small. He doesn't try to fix your choice for you; the storm has asked you both to be many things at once."
    # [Scene: Promenade | The Breach]
    hide jonah_reyes
    hide mara_ellis
    hide mateo_old_mate_alvarez

    scene bg ch6_601bcb_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: A series of sharp, reverberant bangs as waves hit engineered faces; the hum of failing electronics beneath. A single, terrible crack—like a hull being split—echoes.]
    # play music "music_placeholder"  # [Music: Percussive staccato, a low cello line that tightens]
    "The sensors blink—once, twice—a scattered constellation going dark. The NovaSeis feed anneals into a flat gray. For a deadly few seconds there is only physical sound: the slap of water, the whip of rain, the roar of a channel filling faster than it should."
    "You and Jonah run. Old Mate is already shouting into his radio; his voice is a single, furious instrument."
    show mateo_old_mate_alvarez at left:
        zoom 0.7

    mateo_old_mate_alvarez "They bounced off the northern buttress! It's channeling into the old creek. The Drowned District—watch the old sluice!"
    "Your stomach drops. You can see it—the engineered berms, designed to pitch waves back, have met an unexpected geometry. In places, the armor strips the water with surgical precision; in others it ricochets, feeding a focused surge straight toward the low blocks."
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "Manual valves—close the sluices! Divert where you can. Mara—get the volunteers inland!"
    "You move like a tool in the body of the response: you seize a handheld, bark coordinates, knuckle the small red emergency switch at the terrace entrance. Water finds every seam. You taste the iron of fear, and beneath it, the old, hot taste of responsibility."
    show mara_ellis at center:
        zoom 0.7

    mara_ellis "Every clause, every concession hums in your bones. You remember the handshakes that let NovaSeis's tech into the contract, the whispered logic of scaling now, the promise that monitoring would catch what models missed. The sensors are silent. Your throat tightens."
    "A high, metallic tone—an alarm from the Tide Lab—cuts through the storm, but the signal is faint and riddled with static."

    menu:
        "Radio Tide Lab directly":
            "You flip the radio to the lab frequency, voice raw. Professor Asha answers after two staticky beeps—her words clipped, eyes already on emergency graphs. The lab begins to reroute what little data they have."
        "Lead an on-the-ground diversion":
            "You shoulder through the rain and organize a chain line with volunteers, throwing sandbags where the water is weakest. For a while, human hands slow what machines could not. You smell wet earth and sweat."

    # --- merge ---
    "Scene continues"
    "Jonah's eyes find yours for a heartbeat that's both accusation and plea."

    jonah_reyes "We did this to scale. We tried to be careful."
    "You don't answer him at first; you stay busy—because doing is a kind of prayer."
    # [Scene: Drowned District | Night — Aftermath]
    hide mateo_old_mate_alvarez
    hide jonah_reyes
    hide mara_ellis

    scene bg ch6_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The slow, sullen lap of water at brickwork; distant cries and the soft creak of settling structures. The city is breathing slowly, exhausted.]
    # play music "music_placeholder"  # [Music: Sparse piano, low and aching]
    "Dawn comes thin and gray. You move through the Drowned District with Jonah and a small team—Maya at your side, a rope of neighbors behind you. The air smells of brine and something burnt; there is"
    "a sour undercurrent of fuel and rot. People stand on the first floors of what used to be living rooms, scraping, wailing, hugging soggy photographs."
    "You climb onto a sodden stoop and take in the scene. The living terraces, where they held, are beaten but green, their plantings shredded into ragged banners. Where the engineered berms met hard surfaces, whole lengths"
    "have sheared out and left scoured channels. And amid the destruction, the sensors are mute—screens at the Tide Lab will show coordinated gaps where feeds should have been."

    "A camera flashes. You do not flinch. The press has already painted a story" "Unforeseen Failure"
    "A cluster of residents look up as you pass. A woman with a child's hand clutched to her skirt spits words—blame, a tangle of grief and accusation. Words press against your ribs."

    "Resident" "You said it would keep us! You promised—"
    "You meet the eyes of each person like you'd meet a tide: with urgency and an awareness of how much you cannot stop."
    "Maya folds her arms, jaw tight, and then turns to you with a look that is equal parts fury and practical steadiness."
    show maya_ellis at left:
        zoom 0.7

    maya_ellis "This is what happens when big firms control what we can't touch. People get priced out and then flooded out."
    "You open your mouth; nothing you say will fill the holes. The accusation is a physical weight."
    "Jonah kneels to help a man free a child's bicycle wheel from trapped driftwood. He is exhausted, mud up to his knees. He looks up at you, and for a moment his face is unreadable—bone tired, and something like grief coiled there."
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "They called for sabotage on the radio. NovaSeis says someone tampered with the array."
    "You feel the world narrow to that phrase. Sabotage. Accusation with teeth. Elias Crowe's statement already rides a public wave claiming deliberate interference. The city council, urgent and brittle, starts to talk about an emergency seawall"
    "buyout—an offer to buy out affected districts and erect rapid vertical defenses, expensive and centralized and final."
    show professor_asha_rao at center:
        zoom 0.7

    professor_asha_rao "The data gaps look…coordinated. But we can't read the encrypted firmware without NovaSeis's credentials. Legally, they're sealed."
    "You feel the cage of contracts closing: proprietary locks, legal pauses, a public relations campaign that reframes failure as criminal sabotage. Elias's spokespeople repeat the line like a prayer—no fault, only malice."
    # [Scene: Tide Lab (Converted Research Ferry) | Midday — Investigation and Politics]
    hide maya_ellis
    hide jonah_reyes
    hide professor_asha_rao

    scene bg ch6_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The rhythmic beeping of surviving instruments; voices low and urgent; the distant murmur of a press conference on a dockside loudspeaker.]
    # play music "music_placeholder"  # [Music: Low strings, a melancholy swell under voices]
    "Inside the Tide Lab, you and Jonah stand before a row of consoles. The NovaSeis terminals are dark where others glow. Your hands hover over keys you cannot press."
    "Councilor Anika's sharp voice comes in through a live feed, sterile and worried. Jonah and you watch as clips of Elias, smiling and controlled, roll across a screen. He is polished, his statement measured. He calls"
    "for a 'swift, decisive investment' and offers the city's administration a buyout—an immediate seawall that will, he claims, 'stop future loss.'"
    show elias_crowe at left:
        zoom 0.7

    elias_crowe "In times like these, we must act decisively. Sabotage is a grave offense. We will cooperate fully with investigations, but we must also protect our citizens."
    "Anger tastes like metal in your mouth. The word 'sabotage' becomes a lever aimed at public sentiment—fear used to justify concentration."
    show professor_asha_rao at right:
        zoom 0.7

    professor_asha_rao "We can build an independent read—if the legal channels cooperate. But right now, the narrative controls the levers. Councilors want a solution that looks immediate. Politically, that's powerful."
    "Jonah's jaw tightens. He runs a hand along the edge of a console, knuckles whitening."
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "We insisted on transparency clauses. They were supposed to prevent this exact kind of opacity."
    "You remember the negotiation—how NovaSeis had all the leverage on proprietary tech and how you traded some degrees of openness for access at scale. The bargain was supposed to be sensible. Now it looks like a trap."
    "Maya, later, leans against a support beam, mud streaking her neon coat."
    hide elias_crowe
    show maya_ellis at left:
        zoom 0.7

    maya_ellis "People will be moved. Buyouts mean developers reposition. New seawalls mean neighborhoods like ours get cut off and monetized."
    "You feel the old fear, the one that ate your childhood home into memory. But beside that fear is a smaller, fiercer thing: the memory of hands in soil making terraces, of neighbors teaching children to"
    "gather marsh grass, of the way the city looked that first successful test day—alive, behaving like a coastline instead of being caged."

    professor_asha_rao "We need to keep the living terraces narrative alive. We have pockets that worked. We have neighbors who know how to place a root and mend a gabion. The political fight will be brutal, but the biological one—restoration—can begin now, with what we have."
    "Your throat tightens. The municipal program will be scarred; political capital evaporates in crisis. Yet the terraces that held—those green pockets—are not gone. They pulse like embers."
    # [Scene: Promenade Edge / Tide Lab Deck | Dawn — Quiet After the Storm]
    hide professor_asha_rao
    hide jonah_reyes
    hide maya_ellis

    scene bg ch6_601bcb_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Soft conversation, the clink of tools, distant city traffic resuming like a tired heart. A single gull picks at floating debris.]
    # play music "music_placeholder"  # [Music: A single violin, fragile and warm]
    "You and Jonah stand close, hands still, watching neighbors re-plant a small terrace on the lab's lee side. Volunteers work with an intensity that is its own kind of kindness. Old Mate teaches a boy how"
    "to set cordgrass in a sloped weave; Maya barks orders and then kneels to plant, dirt under her nails like armor."
    "Jonah reaches across and slides his hand over yours, fingers finding the small circle of woven fishing line on his right thumb."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "They'll ask for our heads. The press will want a story. Elias will offer money and stamps and concrete. We can take the contracts for the city, or we can keep building with neighbors."
    "You look at him—the battered bandana, the mud on his forearms, the tired humor that refuses to die."
    show mara_ellis at right:
        zoom 0.7

    mara_ellis "Whatever public blame finds us, here—at this slick, weathered deck—there is a truth that doesn't fit neatly into headlines: that people gather to save the things they love, because love is the most practical adaptation of all."
    "You fold your fingers around his. It feels like a small, stubborn treaty."

    jonah_reyes "I don't know how we'll answer them in the council. I don't know how we defend a hybrid approach when corporate narratives seize the mic."
    "You squeeze his hand. Your voice is steadier than you expect."

    mara_ellis "We tell the truth we can prove. We show them the terraces that held. We document the failures. We help people rebuild. We don't let the buyout be the only story."
    "Professor Asha, who has been cataloging samples and images, joins you. She sets a damp printout—photographs of replanted marsh grass—on the rail."
    show professor_asha_rao at center:
        zoom 0.7

    professor_asha_rao "There will be hearings. There will be settlements and legal battles. Hearts will harden on every side. But there are neighbors here who will not leave. They'll anchor micro-projects and teach others. That's how the model survives, even if the city's appetite changes."
    "Maya, standing nearby, watches a child plant. Her voice is softer than earlier, threaded through with grief but resolute."
    hide jonah_reyes
    show maya_ellis at left:
        zoom 0.7

    maya_ellis "They'll try to box us into a timeline. We'll keep planting. We have roots that don't belong to their spreadsheets."
    "You let the sentiment settle in—bitter and sweet braided. The Drowned District is a wound; some loss is irreversible. People were displaced; people will be displaced. The municipal program's prestige is diminished. Elias's proposal hangs heavy in the air like a shadow ready to fall."
    "And yet: in the shallow pools of the terraces, new shoots are already holding. Hands, municipal volunteers and neighbors together, braid root systems and knot coir bags like a new kind of civic weaving."
    "Jonah leans his forehead against yours for a heartbeat, a small, private gesture that quiets the noise of accusation."
    hide mara_ellis
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "If the world keeps asking us to choose between big steel and living roots, I want to keep finding the middle ground. With you, if you'll have me."
    "You laugh, a sudden soft sound that doesn't chase away the ache but creates a room for it."
    hide professor_asha_rao
    show mara_ellis at center:
        zoom 0.7

    mara_ellis "I will. We'll be a lousy PR campaign, but we'll be stubborn in the right ways."
    "You both look out across the soaked city—not to deny the damage, but to see where hands can still reach. Old Mate calls across with a story about tides that once saved a whole fleet; he says it like a benediction."
    hide maya_ellis
    show mateo_old_mate_alvarez at left:
        zoom 0.7

    mateo_old_mate_alvarez "The coast remembers. So do we."
    hide jonah_reyes
    hide mara_ellis
    hide mateo_old_mate_alvarez

    scene bg ch6_601bcb_6 at full_bg
    # play music "music_placeholder"  # [Music: Violin sustains, a hollow but warm chord]
    "You think of the headlines that will come, of council chambers and televised statements, of Elias's lawyers and the pressure to accept a shiny, certain seawall. You think also of the people in the Drowned District who have nowhere else to go and the seedlings you just helped plant."
    show mara_ellis at left:
        zoom 0.7

    mara_ellis "The Icarus crash—our attempt to fly fast and high—has burned and left scars. That is real. The political fallout will stoke other fires. But in the folds of that wreckage are small, human victories: a couple holding hands on a ferry deck, neighbors replanting terraces, a professor refusing to let data be silenced. That will be part of the city's story too, if you keep telling it."
    "You breathe in the cold salt air and hold Jonah's hand a little tighter."
    hide mara_ellis

    scene bg ch6_601bcb_7 at full_bg
    # play music "music_placeholder"  # [Music: The music eases into a soft, rueful chord; the soundscape becomes the muted whisper of the city rebuilding]
    "You will be blamed in the papers. You will testify. You will be asked to accept things you don't believe in for the promise of immediate safety. You will grieve."
    "But you will also plant, and teach planting, and document, and show the city pockets that work. Jonah will keep repairing the things that can be repaired. The hybrid approach survives in fragments, in hands and soil and stubbornness. Your partnership survives, tempered by crisis and steadied by commitment."
    # play sound "sfx_placeholder"  # [Sound: A distant camera phone clicks, capturing your joined hands. The image will travel. It will not erase the headlines; it will be a quiet counterweight.]

    scene bg ch6_601bcb_8 at full_bg
    # play music "music_placeholder"  # [Music: Fade out]

    scene bg ch6_601bcb_9 at full_bg
    "THE END"
    # [GAME END]
    return
