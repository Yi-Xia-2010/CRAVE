label chapter6:

    # [Scene: Planning Office | Early Morning]

    scene bg ch6_601bcb_1 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Low conversation from the bullpen, the soft click of a stylus on glass, distant gulls and the faint rumble of barge engines]
    # play music "music_placeholder"  # [Music: Gentle, rising piano motif]
    "You wake to the predictable ache behind your eyes—the kind that comes from nights spent counting compromises like tally marks. Your compass pendant rests against your collarbone, warm and small. The contract language you fought for"
    "sits on a city server, but it is not a trophy; it is a promise that still needs listening to, revision to, and people to hold one another accountable."
    "You breathe in. The air tastes faintly of coffee and salt, and the smell somehow steadies you. There is a quiet triumph in the rhythm of the office: bodies moving toward the same details instead of"
    "away from them. That is progress. Not the final victory—a thousand footnotes still exist—but a tide shifting."

    scene bg ch6_601bcb_2 at full_bg
    show elias_kade at left:
        zoom 0.7

    elias_kade "Look—if we ease the bearing curve here and anchor the living modules with staggered intervals, the stress model flattens in storm scenarios."
    "You lean in, fingers hovering over edge notes you made last night. The blue lines of his CAD overlay with your hand-sketched tidal wetlands map, the collision forming something neither of you had alone."
    show mara_lin at right:
        zoom 0.7

    mara_lin "If we set the intervals there, we can make room for the marsh plugs to take root faster. It buys biological damping in five years without compromising the immediate load-bearing needs."

    elias_kade "You always think in both timescales. My father would have liked that phrasing—'biological damping.' Sounds elegant on a grant application."
    "Elias Kade looks up—hazel narrowing with the sort of cautious amusement you only see when he lets guard down. The office light catches the undercut at his temple and the curls that never quite obey the wind. He has become, over these weeks, someone you build beside."

    elias_kade "You slept at your desk again, didn't you?"

    mara_lin "I left the kettle on. Professor Bhat found me curled under a rolling folio at three a.m. She called it 'endearing' in the taxonomic way a scientist calls a living thing 'persistent.'"
    "Elias Kade chuckles, and the sound is brief and domestic and unnervingly safe. You exchange a look that holds more between you than either says aloud—long hours, shared responsibility, the small habit of reaching for the same pens."

    menu:
        "Make a pot of tea for both of you":
            "You walk to the small kitchenette and put the kettle on, choosing a citrus blend Professor Bhat recommended. The steam unfurls a domestic calm; when you bring two mugs back, Elias Kade's shoulders drop as if a weight has been lifted."
        "Keep working, sketch the next overlap":
            "You stay, hand steady, and finish overlaying the marsh geometry. When Elias Kade looks up, he nudges his shoulder against yours—an unspoken thank you that says more than idle tea ever could."

    # --- merge ---
    "The scene continues at the construction site."
    # [Scene: Sea Barrier Construction Site | Midday]
    hide elias_kade
    hide mara_lin

    scene bg ch6_601bcb_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Machinery, the slap of wet boots on plywood, the thud of tamped earth]
    # [Smell: Diesel, wet salt, and the faint, green powder scent of peat]
    # play music "music_placeholder"  # [Music: Low strings, gradually lifting into a steady cadence]
    "You stand at the waterline where the living breakwaters—engineered frames seeded with marsh plugs—are being installed. Up close, they are awkward and beautiful: skeletal lattices of reclaimed materials, burlap sacks of sediment, little clusters of green that look too fragile for the open sea."
    "Nova Duarte arrives with her megaphone slung at her side. Her presence is not ceremonial; she walks the line as if cataloging breaths. She watches a crew coaxing marsh plugs into pockets on a module, her expression unreadable—more watchful than approving."
    show nova_duarte at left:
        zoom 0.7

    nova_duarte "They're doing it right. It's not the same as a marsh that formed over a century, but it's a start."
    show mara_lin at right:
        zoom 0.7

    mara_lin "You were here the morning we paired the sediments. Your seed stock came from Chalmers' flats."

    nova_duarte "Someone had to dig it back up. Someone had to make sure they used local genotypes. You fought for that clause in procurement."
    "Nova Duarte turns her head, scanning the workers, then your face. For a brief second the old friction coils under her words—a history of distrust and of grievances not all healed by the line items on a contract. Then she exhales."

    nova_duarte "Don't make me like the thank-you plaque, Mara. Make me keep being necessary."
    "Her sentence could be read as a rebuke or a plea; either way, it is honest. You nod."

    mara_lin "You are necessary. We need you—your voice at the meetings keeps the contractors remembering people, not punch-lists."

    nova_duarte "And your engineering keeps the people alive when storms kick up. Funny world—we're both stubborn."
    "The crew laughs, and the sound bridges something that months of shouting had strained. The megaphone hangs quiet; she does not raise it. The workers call out a successful lift, and a marsh plug is lowered into place, roots first."
    "Samir appears at your elbow, palms muddy, grin wide as tide pools."
    show samir_reyes at center:
        zoom 0.7

    samir_reyes "We got the trainees through the first drill. They can deploy the pumps and sandbag racks in under fifteen now. Coffee? I brought terrible thermos coffee to celebrate."

    mara_lin "I'll take it. And bring the trainees by the Tideward for plant orientation next week? They can help with the rooftop irrigation reroute."

    samir_reyes "Already on the list. You made them into a team, Mara. They believe in the plan because you showed them how it keeps Grandma Ebbett's place from flooding."
    "You let the gratitude settle like sediment. It is heavy, layered, but it holds."
    # [Scene: Tideward Rooftop Garden | Late Afternoon]
    hide nova_duarte
    hide mara_lin
    hide samir_reyes

    scene bg ch6_601bcb_4 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Bees, distant city din muffled, laughter from volunteers]
    # [Smell: Wet soil, basil, brine on the breeze]
    # play music "music_placeholder"  # [Music: Warm strings with a hopeful countermelody]
    "The rooftop is a patchwork of people and purpose. Neighborhood trainees tend new beds carved from reclaimed decking. Rain gutters you rerouted now feed troughs of water that catch just enough run-off to keep the planters thriving. The gardens are small triumphs—tested solutions that feel like homegrown miracles."
    "Professor Anika meets you by a rust-red planter, sleeves rolled and eyes bright."
    show professor_anika_bhat at left:
        zoom 0.7

    professor_anika_bhat "You did the right thing with the sediment composition. The colonizers will stabilize faster than the models predicted—less slump."
    show mara_lin at right:
        zoom 0.7

    mara_lin "We hedged the composition to favor early rooters. We can't outwait the sea forever, but we can buy time for communities to adapt."

    professor_anika_bhat "And you taught an entire cohort how to read that timeline. That's how institutions change—from people who carry the knowledge forward."
    "You think of the notebook swelling with diagrams—technical and humane both. You flip it open, each page a weathered promise: procurement notes with community liaison sign-offs, timelines, annotated photos of patched roofs, and charcoaled sketches of neighbors who now have roles on flood teams."

    menu:
        "Walk the garden, pointing out plants to a trainee":
            "You move along the beds, naming species and explaining salinity tolerances. The trainee's face lights up; they ask for propagation tips, and you feel the gentle satisfaction of knowledge passing hands."
        "Sit on the bench and write in your notebook":
            "You sit and sketch the irrigation re-route in finer detail. The action steadies you; a trainee brings you a basil sprig and tucks it behind your ear like an old custom. You smile in reply, more grounded than before."

    # --- merge ---
    "The scene continues in the Planning Office later that night."
    # [Scene: Planning Office — Late Night | Late Night]
    hide professor_anika_bhat
    hide mara_lin

    scene bg ch6_601bcb_5 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hushed tick of a wall clock, the distant murmur of the city]
    # play music "music_placeholder"  # [Music: Piano returns, slower, comforting]
    "It is late. Outside, the harbor is a black mirror. Inside, you and Elias Kade trace the contours of future work by lamplight. There is an intimacy to the way the light hits his cheekbones—soft, patient—the way the stylus tip pauses at an intersection then continues."
    show elias_kade at left:
        zoom 0.7

    elias_kade "We were lucky to get the clause in for embedded liaisons. That was your maneuver."
    show mara_lin at right:
        zoom 0.7

    mara_lin "We were lucky the mayor's office let the language breathe. Samir running the trainees—Nova Duarte agreeing to monitor installations—Professor Anika's notes... It was a coalition, not a single hero."

    elias_kade "You tend to make the coalition. You make it human."
    "He pauses, and you catch the vulnerability in him—a man who measures risk and yet has, over weeks, leaned into risk measured against people, not just spreadsheets."

    mara_lin "You made a lot of compromises to get here. I know you lost sleep choosing wording that would pass the fiscal tests."

    elias_kade "And you lost sleep because you feared betrayal, not budgets."
    "He looks at you with an earnestness that hums louder than the ticking clock."

    elias_kade "Mara—if this is going to be messy and imperfect, then I want messy and imperfect with you. For as long as this takes."
    "Mara Lin: (you can feel your chest open like a tide pool) 'I don't do 'forever' lightly. But I'm tired of the alternate—of holding everything alone. I want partners, both in work and—'"

    elias_kade "—and, yes, in life, variable-return-investment though it may be?"
    "You laugh and then laugh again, a short breath that tastes of relief."
    hide elias_kade
    hide mara_lin

    scene bg ch6_601bcb_6 at full_bg
    # play music "music_placeholder"  # [Music: Strings swell warmly]
    "You pick up the phone to share the news with Samir and Nova Duarte. Your thumb hovers, then sends."
    # [Scene: Promenade | Dawn After First Real Storm]

    scene bg ch6_601bcb_7 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hush after rain—the soft drip from awnings, a child's distant laugh, a gull calling]
    # [Smell: Sea-spray, damp wood, the sweet tang of turned soil]
    # play music "music_placeholder"  # [Music: Full, uplifting orchestral swell with a steady heartbeat drum]
    "The first storm to test the new hybrid system passed in the night. It is not a monster; not the kind that erases neighborhoods in a single breath. But it would, in the old model, have been a sentence."
    "You walk the promenade with Elias Kade at your side. The seawall sections flexed as designed; the living breakwaters held more of the flotsam, and where old dunes once cracked, new marsh ribbons absorbed the bite. People stand on doorsteps, checking their houses, faces raw and hopeful."
    "Samir finds you both, cheeks streaked with rain and laughter. Nova Duarte approaches slowly, hands empty—no megaphone, no slogan—only a steady look."
    show nova_duarte at left:
        zoom 0.7

    nova_duarte "You kept your word. The procurement committee is actually meeting with residents next month. They're using the liaison model like you wanted."
    show mara_lin at right:
        zoom 0.7

    mara_lin "You kept your word too. You showed up when it mattered."

    nova_duarte "I showed up. But don't get sentimental. Keep them honest."
    "She smiles—a private, small thing. It is enough."
    "Professor Anika appears a step behind Samir, hair brushed back, eyes bright and wet."
    show professor_anika_bhat at center:
        zoom 0.7

    professor_anika_bhat "The models were conservative. The marsh plugs exceeded survivorship by twelve percent. You changed the risk equation."

    mara_lin "We changed it together."
    "You stand at the water's edge. The city breathes around you—messy in repairs, sticky with new paint where it matters, and humming with people who can, for now, stay. You think of the houses that still"
    "sit low and vulnerable, the ones who had to leave, and the faces of those who remained because a clause in a contract became a promise enforced by neighbors."
    hide nova_duarte
    show elias_kade at left:
        zoom 0.7

    elias_kade "You carried a lot of people through that storm. You didn't carry them alone."

    mara_lin "No. But I carried something else too—my guilt. The nights when I thought—if only I had done more sooner. Standing here, I can measure that pain against what we built. Not erased, but made usable."

    elias_kade "You gave us a way to grieve and rebuild. That's not nothing."
    "You reach for his hand. He takes it, fingers fit and warm and practical. There is nothing theatrical—no sweeping declarations—only steady contact that says: we'll keep doing this, not because it's easy, but because it matters."
    # play music "music_placeholder"  # [Music: Quiet, steady chords; the piano returns with a single hopeful motif]
    hide mara_lin
    hide professor_anika_bhat
    hide elias_kade

    scene bg ch6_601bcb_8 at full_bg
    "You let the moment unfold. The world is still imperfect. There will be future storms and budget fights and neighbors who mourn homes they could not save. But the city now has tools, trained people, legal teeth, and a culture that remembers the human stakes between line items."
    "You slide your weatherproof notebook into your pocket. Its pages are full—sketches of wetland patches, procurement flowcharts with signatures, a penciled-in note from Nova Duarte about community training. It's a record of compromise, of fights, of people who refused to accept binary choices."
    "You look at Elias Kade again—no grand gesture, only the clean arc of his smile and the quiet loyalty that lives there."
    show mara_lin at left:
        zoom 0.7

    mara_lin "We did not fix everything. We kept more than we lost. We built a scaffolding for repair and for love that is more stubborn than policy."
    "You close your eyes and breathe the sea-air deep. It tastes like salt and possibility."
    hide mara_lin

    scene bg ch6_601bcb_9 at full_bg
    # play music "music_placeholder"  # [Music: The uplifting motif resolves into a warm, sustained chord]

    scene bg ch6_601bcb_10 at full_bg
    # play music "music_placeholder"  # [Music: Gentle sustain, then a peaceful diminuendo]

    scene bg ch6_601bcb_11 at full_bg
    "THE END"
    # [GAME END]
    return
