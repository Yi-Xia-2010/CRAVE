label chapter12:

    # [Scene: Highland Cliffs Overlook | Dawn]

    scene bg ch12_f99e88_1 at full_bg
    # play music "music_placeholder"  # [Music: Low cello, long bowed note under a whisper of wind]
    # play sound "sfx_placeholder"  # [Sound: Distant gull calls, a hollow bell rolling from the harbor]
    "You stand with the brass compass heavy at your throat and the morning tasting of salt and wet stone. Below, the town is a patchwork of new seams: a dark ribbon where reinforced berms cut the"
    "waterline, a scatter of pale green where marsh plantings have taken hold. From up here, the work looks like stitches—careful, practical, stubbornly visible."
    "You remember the council room's light, the arpeggio rising. Someone in the region took the model you recommended; the pilot became a template. Whether it was the marshes or the berms matters less to anyone watching"
    "the headlines than the word 'success.' Grants rolled in. Trucks and technicians came, and people from other towns showed up with notebooks and cameras. You feel that institutional lift in your ribs—a validation measured in contracts"
    "and satellite images. Under it, something else bruises."
    "A shape appears on the path below: Jonah, hands shoved into the pockets of his patched coat, carrying a thermos and a coil of rope. He climbs up the last slope, breath steaming, eyes finding you before he does anything else."
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "You always pick the worst place to brood, Mira."
    show mira_kestrel at right:
        zoom 0.7

    mira_kestrel "You could say the same about you.' You wrap your jacket tighter against the wind. 'I wanted to see the edge before the day's meetings."

    jonah_reyes "Edge's been busy. People keep climbing up here when their radios cut out.' (He sets the thermos between you, then leans on the low stone wall.) 'Looks—different. In a good way."

    mira_kestrel "It is different.' Your voice is small against the wind. 'We saved a lot, Jonah. The models—Lian's work, the crews—they did what they were supposed to. The region will repeat this now."

    jonah_reyes "Saved a lot. Lost a bit, too.' He doesn't look at you. 'Old moorings gone, channels tighter. Some of Bento's neighbors had to lay up boats they don't know how to let go of."
    "You chew the inside of your cheek. The image of dry dock lines, of a fisherman running a hand along a retired hull, presses behind your ribs."

    menu:
        "Ask Jonah about the boats":
            "You press him gently: 'Which boats?' He names two—small family cutters—his voice careful, as if calling a wound by its name. He doesn't blame you; he lists workarounds he's already sketched in his head."
        "Ask about the neighborhood":
            "You ask about the low-side streets. Jonah looks away and then tells you about the night the surge took the moorings—how they found the old rope tangled like a question in the current. He clenches the thermos until the metal creaks."

    # --- merge ---
    "Continue"
    "Jonah Reyes studies you, thumb rubbing the scar along the compass chain you never took off after the meeting."

    jonah_reyes "You look like you've been carrying that council in your bones. Did you sleep?"

    mira_kestrel "Dreams of spreadsheets.' You attempt a laugh and find it hollow. 'And every house that ever mattered to me."

    jonah_reyes "Did you expect it to feel like this?"

    mira_kestrel "I expected clean numbers and messy people. Reality is both. The numbers convinced funders; the people—' (Your throat tightens.) '—some of us are still counting."
    "Footsteps crunch on the gravel behind you. Asha Verma approaches with Evelyn Sato and Dr. Lian Zhou: Asha's coat on, hands folded in the practiced stance of authority; Evelyn's scarf damp from early fog; Lian carrying a battered tablet, her boots flecked with mud."
    show asha_verma at center:
        zoom 0.7

    asha_verma "Morning.' (flat, precise) 'Good vantage point."
    hide jonah_reyes
    show evelyn_sato at left:
        zoom 0.7

    evelyn_sato "Figured you'd be here, Mira.' Her smile is tired but sincere. 'We need to thank you. Councilors from the region just called."
    hide mira_kestrel
    show dr_lian_zhou at right:
        zoom 0.7

    dr_lian_zhou "The models' post-processing has started circulating. We've been asked to brief the steering committee next week.' (She taps the tablet; a map blooms in muted teal.) 'But the field notes from last night are—complex."
    "Asha meets your eyes and, for a heartbeat, something unreadable flickers across her face. You don't assume tenderness or reproach; it's simply there—an expression fitted to a person who weighs every decision in scales."

    asha_verma "You did what was necessary.' (short pause) 'There were gaps. We knew there would be gaps—we built escalation triggers—but the surge hit a neglected low-side block harder than our worst-case scenario predicted."
    "You feel your fingers go white on the compass chain. 'Which block?'"

    dr_lian_zhou "The Grafton row.' She swipes the tablet; images roll—damp furniture, bent fences, a playground half-submerged. 'They were on the protected side map, but the local sheet flow—an old culvert that had been blocked—channelized water into them. Pumps responded, but not fast enough."

    evelyn_sato "We evacuated most. We got ambulances down. But houses, Mira—family homes—took water. The older moorings along Dock Five? Total loss."
    "Jonah Reyes's jaw tightens. His hands flex around the rope. There's no melodrama—just the compressed, practical outrage of someone who lives and measures by the tide."
    hide asha_verma
    show jonah_reyes at center:
        zoom 0.7

    jonah_reyes "My cousin's net hauler's gone. He might get compensated, maybe. But compensation doesn't put that rig back; doesn't put the smell of diesel and salt back into the mornings. You know that."
    hide evelyn_sato
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "I know.' The word is too small. Guilt swells—not just the inherited survivor's guilt but the professional kind: the person who meant to prevent this and yet could not foresee every old culvert, every informal pier. 'We set thresholds. We wrote contingencies. But thresholds are lines on paper until they snap."
    hide dr_lian_zhou
    show asha_verma at right:
        zoom 0.7

    asha_verma "We will learn. We will adapt the model. The replication mechanism requires iteration.' Her tone is unsparing—both reassurance and a reprimand. 'This is the cost of scaling—there is always an edge case. We mitigate faster."
    "Lian Zhou's eyes rest on you, soft with data and empathy both."
    hide jonah_reyes
    show dr_lian_zhou at center:
        zoom 0.7

    dr_lian_zhou "Your community data is what will close this gap. Field observations, local knowledge—if we feed that into the next calibration, the model will stop missing the culverts. It will stop washing out the houses on lower elevations."
    "The group falls quiet, the wind carrying a sound like distant surf and uncertainty. You imagine meetings and memos—patches to models, emergency funds, neighborhood outreach. All necessary. All slow in the particular ways that hurt."
    # [Scene: Marsh Expanses & Reinforced Berms | Midday]
    hide mira_kestrel
    hide asha_verma
    hide dr_lian_zhou

    scene bg ch12_f99e88_2 at full_bg
    # play sound "sfx_placeholder"  # [Sound: The hum of pumps, shouted coordination, the slap of boots on wet wood]
    # play music "music_placeholder"  # [Music: Sparse piano, intermittent high notes—restless, propulsive]
    "You move down from the cliffs with the others, boots sinking into a smell that is half peat and half diesel. The marshes—where present—sway in young green, fragile and full of promise. The berms sit like a deliberate scar: uniform, functional, and clearly engineered to keep water out."
    "People are working—neighbors, municipal crews, visiting students from neighboring towns. Cameras click. A reporter murmurs questions into a recorder. There's pride in the choreography; there's also a strain, like a rope being held taut."
    "You pass a row of decommissioned small boats tied to a temporary jetty. Their names are chipped into paint. Someone has left a bouquet of plastic flowers in a retired cooler."
    "An older woman—the owner—stands with Bento's granddaughter, staring at the water. You don't know if you should speak; you know, too, that silence would be a small cruelty."
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "We can help salvage what’s left."

    "Woman" "They were my husband's.' (quiet) 'Sat on this dock since before your mother was born.' She turns to you, anger and grief braided. 'You came back a planner. You came with promises. They keep the corners of my memories together."
    "Your chest constricts. Jonah Reyes steps forward and says nothing, but his shoulders move in a way that speaks of twenty small repairs already thought through."
    show jonah_reyes at right:
        zoom 0.7

    jonah_reyes "We'll jury-rig something. Maybe move that skiff to the nursery docks. Make a pulley. We can start tonight if you want."

    "Woman" "Make it tonight.' Her voice is steady. 'Make it so I can look at it tomorrow and say it still belongs."
    "The smallness of that demand—simple, sacred—lands like a stone. You find yourself cataloging ways the big solutions swallowed the small rituals: the precise route of a channel that once made a shortcut for a day boat; the placement of a berm that now pushes tidal flow toward an alley."

    menu:
        "Offer to coordinate a salvage crew":
            "You pull out your notebook and start sketching a plan, names, and tools. Jonah nods, grateful, and Lian volunteers data to help predict slack tides. The woman’s face relaxes a fraction—organization is comfort."
        "Sit with the woman and listen":
            "You sit on a coil of rope and hear stories about dawn lines and a husband's laugh. The woman cries once, then steadies. It costs you time but gives her the brief, necessary currency of being heard."

    # --- merge ---
    "Continue"
    "You spend the afternoon moving between the macro—meetings with contractors, Lian's updated risk maps—and the micro: a boy who lost his treehouse in the flood, an elderly couple who mourn a threshold rug that had woven"
    "birthdays into its fibers. Each thing you can't fix by policy you try to hold with hands and words."
    "Asha corners you near a line of temporary pumps, her face close enough that you see the tightness at the corner of her mouth."
    show asha_verma at center:
        zoom 0.7

    asha_verma "You can't let every loss derail the process, Mira. If we cave to every grief, the system fails and more people drown."

    mira_kestrel "And if we ignore grief, Asha, the system succeeds on paper and fails the people living inside it."

    asha_verma "We will iterate.' She looks at the berms, then at the marshes. 'We will adapt the template. But you must accept trade-offs."

    mira_kestrel "Trade-offs don't feel like abstract things when a porch is under two feet of water.' You want to say: we tried to avoid this. You want to say: I'm sorry. But apologies don't stop salt from soaking into floorboards. You say instead, 'We will adapt."
    "Lian Zhou places a hand on your shoulder, steady and warm."
    hide mira_kestrel
    show dr_lian_zhou at left:
        zoom 0.7

    dr_lian_zhou "This is the terrible middle. We measure and we grieve. Both are necessary if the town is to be whole again."
    # [Scene: Harbor | Late Afternoon]
    hide jonah_reyes
    hide asha_verma
    hide dr_lian_zhou

    scene bg ch12_f99e88_3 at full_bg
    # play sound "sfx_placeholder"  # [Sound: Muffled conversation, the soft thump of a camera from a visiting delegation, salt-slicked ropes creaking]
    # play music "music_placeholder"  # [Music: Low strings, a minor key settling]
    "Evening arrives with a taste of iron and the tiredness of too many hands. People gather in the boardwalk's shelter, sharing warmed soup and quiet curses. Someone has set up a whiteboard listing repairs and volunteers; names fill the spaces like stitches."
    "Evelyn Sato stands at the head of the board, voice fraying but resolute."
    show evelyn_sato at left:
        zoom 0.7

    evelyn_sato "Funds are secure this quarter. The region is responsive—yes. But we need local repair teams and cultural care funds. We will propose a micro-grant for restoring family boats, for memory projects—photos, oral histories. We need Tidehaven not just defended, but remembered."
    "Asha Verma folds her arms, and for once her armor lets a sliver of vulnerability show."
    show asha_verma at right:
        zoom 0.7

    asha_verma "Memory projects are not infrastructure. But I can support a small pilot if it's framed as social resilience metrics."
    "Jonah Reyes snorts quietly, then says, 'Framing's good with you, huh.'"
    "The room laughs, small and brittle, and the laughter helps a little."
    "You find a moment alone near the new info kiosk. Someone has laminated a Polaroid of an old harbor procession—boys with fish, women with baskets—with Jonah's camera brand visible at the corner. The image is sepia"
    "with salt. For a second you see the town before models, before funding, before grief. It lives under the newest layer like a fossil."
    show mira_kestrel at center:
        zoom 0.7

    mira_kestrel "I keep thinking of choices as clean lines. But the real world isn't a spreadsheet. It's a palimpsest: each layer leaves traces. We have drawn a new layer over the old one. Some traces remain, and some are smudged out."
    "Jonah Reyes approaches and sits beside you, no words needed for a while."
    hide evelyn_sato
    show jonah_reyes at left:
        zoom 0.7

    jonah_reyes "So what now, Mira?"

    mira_kestrel "We keep doing both things. We refine the model with what failed. We help the people who lost the small things that make mornings theirs. We make room for ritual alongside engineering."

    jonah_reyes "And us?"

    mira_kestrel "I don't have a neat answer.' You fold your fingers around the compass until the brass warms. 'But I know what I'm going to do. I'm staying. Not because I fixed everything, but because there's work that needs staying for. And because—' Your voice catches. '—there are people worth staying for."
    "Jonah Reyes's face shifts—complex, unreadable. He reaches out and taps the compass."

    jonah_reyes "Then we'll find the rhythms. We'll change the boats, or we'll change the docks. We'll mourn what we must. We'll plant what we can."
    hide asha_verma
    hide mira_kestrel
    hide jonah_reyes

    scene bg ch12_f99e88_4 at full_bg
    # play music "music_placeholder"  # [Music: Strings resolving downward into a quiet, somber chord]
    "Night settles with a soft hush. The town is patchworked but held. The model will be taught, copied, improved. Scholarships will be named; planners will come to lecture here. Tidehaven will be a case study in"
    "adaptation, an example other towns point to when asking what to do. The institutional rise is real: the region is safer, protocols are tighter, the charts are clearer."
    "But you have also counted private losses tonight—a mooring rope knotted into memory, a porch rug ruined, a retired cutter with paint flaked like exit wounds. The institutional gain sits beside the private pain like two"
    "weights balanced on an imperfect scale. You think of your father's boat, of the way it used to creak in the harbor at dawn, and you let the grief that you carried alone in meetings finally"
    "come up like tidewater."
    "You pull the compass from beneath your collar and hold it out to the night. You could wish for absolution, for a single fix that erases the houses that flooded and the boats that were retired."
    "You know there is no such fix. There is only the long work of repair, of listening, of accepting that some losses will remain as scars, as place-markers for what was and what cannot be reclaimed."
    "You close your hand. The compass clicks shut. The town breathes around you—hurt and hopeful, marching on."
    # [Scene: Highland Cliffs Overlook | Night]

    scene bg ch12_f99e88_5 at full_bg
    # play music "music_placeholder"  # [Music: A single, mournful piano motif beneath the wind]
    # play sound "sfx_placeholder"  # [Sound: A distant bell, low and steady]
    "You climb the path alone this time, boots silent on damp gravel. The wind has taken the edges off the day and left the core—what was necessary and what was costly—raw in your chest. From the cliffs you can see the whole—terrible, beautiful, stubborn."
    "You speak aloud, though no one answers except the sea."
    show mira_kestrel at left:
        zoom 0.7

    mira_kestrel "We did something that saved more than it cost. We also failed people we wanted to protect. Both are true. Both are ours."
    "You let the sentence settle. It does not fix anything. It does not make reparation. It names."
    "A small light in the harbor—someone's lantern—blinks like a promise. You tuck the compass back beneath your jacket and feel, unexpectedly, a quiet steadiness. The town will be remade in ways both chosen and unchosen. You will keep doing your part, imperfectly, relentlessly."
    hide mira_kestrel

    scene bg ch12_f99e88_6 at full_bg
    # play music "music_placeholder"  # [Music: The cello holds one final, low note and then fades]
    # play sound "sfx_placeholder"  # [Sound: The bell tolls softly]
    "You turn from the cliffs and head back down toward the town. There will be meetings tomorrow, reports, calls from neighboring mayors asking for your playbook. There will also be a woman who wants to sit"
    "in the cold with you and remember her husband. There will be a boy who needs a new treehouse, a retired cutter that needs paint, and a neighborhood that must be helped to dry out its"
    "memories."
    "You breathe in the salt air, and for the first time in a long time the breath feels like an agreement between the past and the possible. The ending is not a triumph or a defeat;"
    "it is a ledger made of many small entries—some credits, some debts—that you will carry forward."

    scene bg ch12_f99e88_7 at full_bg
    # play music "music_placeholder"  # [Music: Fade Out]

    scene bg ch12_f99e88_8 at full_bg
    "THE END"
    # [GAME END]
    return
